# AIW-91 Increment 1 — findings & the design forks the build surfaced (S231, 2026-06-19)

Built the scaffold and ran the mechanism proof far enough to find where the real design choices
are. Honest status: **half the claim is showing, the other half needs a substrate decision.**

## What's built (runnable, tested — 5/5 mechanical tests pass)
- `minimal_coder.py`: `World` (AR(1) latent to track); `RecursiveCriticalCoder` (two-hemisphere
  probabilistic **branching** net, Galton-Watson in spikes, refractory, gain knob G, internal
  closure); `ReservoirCoder` (two-hemisphere **rate reservoir**, the tractable edge-of-chaos
  substrate); decoders (`ridge_decode`), criticality measures (`lyapunov`, `reservoir_lyapunov`,
  `branching_sigma`), nesting proxy (`subspace_alignment`).
- `test_minimal_coder.py`, `experiment_mechanism.py` (WIP), `venv/` (numpy, scipy).

## What works
- **EWM present:** the world variable is decodable from the middle-layer state (R² ≈ 0.6 at the
  operating point), and stays decodable with recurrence on.
- **Closure dissociation (spiking net):** decoding the fed-back self `a(t-1)` gives R² ≈ +0.14 with
  the loop CLOSED vs ≈ −1.2 OPEN. Directionally the AIW-66 ESM/EWM dissociation — closure is
  load-bearing — but see the caveat below on what this actually measures.

## What does NOT work yet, and why (the valuable part)
1. **Branching-avalanche criticality ≠ edge-of-chaos/memory criticality.** In the stochastic
   branching net, raising the branching gain G just adds avalanche *noise* — memory capacity
   (decoding delayed world inputs) falls **monotonically** with G; it does NOT peak at σ≈1.
   So nothing "peaks at criticality" on this substrate, and the naive branching-slope estimate is
   non-monotone under drive (the AIW-90 lesson, again). The criticality that *enhances recursive
   computation* — what FMT's Class-4 needs — is the **dynamical** edge of chaos, not the
   branching/avalanche critical point. They are different phenomena and I had conflated them.
2. **Reservoir: the edge is shifted and the dissociation vanishes.** With a leak term the rate
   reservoir stays ordered (λ<0) even past G=1 (effective edge ≈ G/leak), so spectral-radius-1
   normalisation doesn't put it at the edge. And critically: because the action `a` is a
   *deterministic* function of the world-driven state, `a(t-1)` is decodable open-loop too — the
   closure dissociation **disappears** (selfMC_closed ≈ selfMC_open).
3. **Reframe — "decode a(t-1)" is the wrong ESM probe.** If the minimal self is the **reafferent
   echo** of a world-tracking action, then its being world-correlated *is* the nesting
   **O_ESM ⊆ S_EWM** — not a confound. The right probe is **source attribution**: can the state
   represent *which part of the input is self-caused vs world-caused* (MG's 2015 p.260
   direct-vs-indirect feedback / the glass)? That is the operationalisation of closure doing FMT's
   work, and it's substrate-agnostic.

## BOTH FORKS RESOLVED (MG, S231) — see `../docs/aiw92-criticality-dials-conversation-verbatim.md` + decisions.md
- **FORK B → build the edge-of-chaos substrate, measure BOTH dials.** The two "criticalities" are not rival
  build choices — they're orthogonal MEASURES on one Class-4 substrate: Dial 1 = EXTENT (fraction recruited
  into Class-4; integration), Dial 2 = COMPLEXITY (pattern richness; differentiation). Build a **balanced
  E/I spiking net** (inhibition-stabilised, no saturation) tuned to the dynamical edge; read both dials off it.
- **FORK A → base/Level-0 = Picture A (reafferent wake) only.** Self = the self-caused, source-tagged part of
  the world; test = source attribution (self-caused vs world-caused input). NO inward grip / endogenous
  generation at base — that's a HIGHER increment (PRESENCE-vs-ACCESS: base has the content present but not
  accessed; access needs the E-models rich enough to SELF-INTERACT = recursion depth up the erweitert ladder).

## The two design forks as originally posed (theory-owner calls — they emerged FROM building, not before)
- **FORK A — what is the minimal ESM?**
  (a) pure **reafferent echo** of the action (world-correlated, nested by construction → test =
  source attribution / self-vs-world discrimination), or
  (b) carries an **endogenous component** (an internal "intention" not derived from the world →
  test = that component is decodable only with the loop closed)?
  *The verbatim (and p.260) leans (a) reafferent; I lean (a) + a source-attribution probe.*
- **FORK B — which criticality is the load-bearing one for the minimal model?**
  FMT's "Class-4 / C4CA" reads as **branching/cellular-automaton** criticality, but the criticality
  that maximises memory + recursive self-application is the **dynamical edge of chaos** (reservoir).
  In these models they differ. Options: target the dynamical edge (where closure provably gains
  something), or unify both in a **balanced E/I spiking net** (inhibition-stabilised) tuned to the
  dynamical edge — which is spiking AND shows avalanches AND has the memory peak. *I lean unify via
  balanced E/I spiking.*

## Next increment (pending the forks)
Most likely: **balanced E/I spiking net** (add an inhibitory population → inhibition-stabilised, no
saturation) tuned to the **dynamical edge of chaos**, with a **source-attribution ESM probe**
(self-caused vs world-caused input). Then show: source attribution + recursive self-representation
are load-bearing ONLY at the edge and ONLY with the loop closed — the falsifiable kernel.
