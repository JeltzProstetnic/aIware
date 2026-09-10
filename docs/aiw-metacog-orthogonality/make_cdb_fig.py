"""CDB multi-dataset robustness figure: metacognitive efficiency (M-ratio) is
orthogonal to first-order performance (d') across many independent perceptual
datasets. Uses cdb_pooled.npy (per-subject d', meta-d', M-ratio) + cdb_results.json
(per-dataset r). Run cdb_sweep.py --run N first."""
import json, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

P = np.load("cdb_pooled.npy")           # cols: d', meta-d', M-ratio
res = json.load(open("cdb_results.json"))
perds = res["perds"]                      # [name, n, d_mean, d_sd, m_mean, r, clamp]

d, mr = P[:, 0], P[:, 2]
ok = np.isfinite(d) & np.isfinite(mr) & (np.abs(mr) < 2.5)
d, mr = d[ok], mr[ok]
r = np.corrcoef(d, mr)[0, 1]
b1, b0 = np.polyfit(d, mr, 1)

fixed = [p for p in perds if p[6] != "CLAMP"]
clamp = [p for p in perds if p[6] == "CLAMP"]
fr = sorted([(p[0], p[5], p[1]) for p in fixed if p[5] == p[5]], key=lambda x: x[1])
med = np.median([x[1] for x in fr])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.2), gridspec_kw={"width_ratios": [1.15, 1]})

ax1.scatter(d, mr, s=6, alpha=0.18, color="#2b6cb0", edgecolor="none")
xs = np.linspace(d.min(), d.max(), 50)
ax1.plot(xs, b0 + b1 * xs, color="#c53030", lw=2, label=f"slope={b1:+.2f}  (r={r:+.2f})")
ax1.axhline(1.0, color="gray", ls=":", lw=1)
ax1.set_ylim(0, 2.5)
ax1.set_xlabel("d′  (first-order sensitivity — EWM)")
ax1.set_ylabel("M-ratio = meta-d′/d′  (metacognitive efficiency — ESM)")
ax1.set_title(f"A. Pooled across {len(perds)} perceptual datasets (n={len(d)} subjects)\n"
              f"metacognitive efficiency ⊥ performance", fontsize=11)
ax1.legend(loc="upper right", fontsize=9, frameon=False)
ax1.spines[["top", "right"]].set_visible(False)

y = np.arange(len(fr))
cols = ["#dd6b20" if abs(rr) < 0.25 else "#888" for _, rr, _ in fr]
ax2.barh(y, [rr for _, rr, _ in fr], color=cols)
ax2.axvline(0, color="k", lw=0.8)
ax2.axvline(med, color="#c53030", ls="--", lw=1.5, label=f"median r={med:+.2f}")
ax2.set_yticks(y); ax2.set_yticklabels([f"{n[:20]} (n={nn})" for n, _, nn in fr], fontsize=7)
ax2.set_xlabel("within-dataset r(M-ratio, d′)")
ax2.set_title(f"B. Per fixed-difficulty dataset ({len(fr)})\n(staircased/clamped excluded)", fontsize=11)
ax2.legend(loc="lower right", fontsize=9, frameon=False)
ax2.spines[["top", "right"]].set_visible(False)

fig.tight_layout()
fig.savefig("cdb_orthogonality_figure.png", dpi=200)
print(f"pooled n={len(d)} r(M-ratio,d')={r:+.3f} | per-dataset median r={med:+.3f} (n_fixed={len(fr)})")
print("saved cdb_orthogonality_figure.png")
