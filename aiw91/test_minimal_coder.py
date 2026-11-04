"""AIW-91 Increment 1 — mechanical contracts for the minimal recursive coder.
Runtime-behaviour tests (not just config). Run: venv/bin/python test_minimal_coder.py
"""
import numpy as np
from minimal_coder import (World, RecursiveCriticalCoder, ridge_decode,
                           branching_sigma, mean_activity, subspace_alignment)


def test_world_has_positive_autocorr():
    w = World(rho=0.9, seed=1)
    z = np.array([w.step() for _ in range(5000)])
    ac1 = np.corrcoef(z[:-1], z[1:])[0, 1]
    assert np.all(np.isfinite(z)) and ac1 > 0.5, f"world lag-1 autocorr {ac1:.2f} too low"


def test_run_shapes():
    c = RecursiveCriticalCoder(N=400, G=1.0, seed=2)
    out = c.run(World(seed=2), T=600, burn=100)
    assert out["R"].shape == (600, 400)
    assert out["z"].shape == (600,) and out["a"].shape == (600,)


def test_gain_knob_is_monotone():
    """The gain knob must do something monotone. NOTE: the naive branching-slope estimate is
    NON-monotone under drive (confounded by saturation — the AIW-90 lesson), so we assert the
    robust contract: mean activity rises with G. Locating the *critical* point is an open
    research step (INCREMENT1_FINDINGS.md: branching-criticality != edge-of-chaos criticality)."""
    act = {}
    for G in (0.6, 0.9, 1.2):
        c = RecursiveCriticalCoder(N=800, G=G, seed=3)
        out = c.run(World(seed=3), T=1500, burn=300)
        act[G] = mean_activity(out["S"])
    assert act[0.6] < act[0.9] < act[1.2], f"activity not monotone in G: {act}"


def test_world_is_decodable_above_chance():
    """Sanity: the world variable is decodable from the critical state, beats a shuffled control."""
    c = RecursiveCriticalCoder(N=800, G=1.0, seed=4)
    out = c.run(World(seed=4), T=2500, burn=300)
    r2, _ = ridge_decode(out["R"], out["z"])
    r2_shuf, _ = ridge_decode(out["R"], np.random.default_rng(0).permutation(out["z"]))
    assert r2 > 0.2 and r2 > r2_shuf + 0.2, f"world R2={r2:.2f} shuf={r2_shuf:.2f}"


def test_alignment_bounded():
    a = subspace_alignment(np.array([1.0, 0, 0]), np.array([1.0, 1.0, 0]))
    assert 0.0 <= a <= 1.0 and abs(a - 1/np.sqrt(2)) < 1e-9


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    fails = 0
    for t in tests:
        try:
            t(); print(f"PASS {t.__name__}")
        except AssertionError as e:
            fails += 1; print(f"FAIL {t.__name__}: {e}")
    print(f"\n{len(tests)-fails}/{len(tests)} passed")
    raise SystemExit(1 if fails else 0)
