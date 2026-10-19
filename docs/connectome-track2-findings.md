# BANC connectome — Track 2 (criticality / edge-of-chaos): RESULTS

Session 230, 2026-06-18. AIW-90. **Spectral pre-screen DONE + dynamical spiking sweep DONE (68 runs).**
Scripts + data in `tmp/connectome-analysis/` (`07_track2_spectral.py`, `08_build_net.py`,
`_track2_worker3.py`, `09_track2_sweep.py`, `10_sweep_summary.py`; `track2_dynamical_results.json`,
`track2_dynamical_figure.png`, raw traces in `sweep_out/`).
Track 1: `docs/connectome-track1-findings.md`. Plan: `docs/pending-connectome-analysis.md`.

## Method (spectral, the cheap-but-rigorous core)
Theory bridge — **Larremore, Shew & Restrepo, PRL 106:058101 (2011):** for a network of
excitable nodes with weighted connectivity W, the **largest eigenvalue λ_max of W *is* the
dynamical branching parameter**. With a global gain g, the network is critical when
g·λ_max = 1, i.e. critical gain **g\* = 1/λ_max**. So criticality is computable directly from
the wiring — no simulation needed for the first cut. (28 s on one CPU core for the whole CNS.)

Built signed, input-fraction-weighted connectivity M[post,pre] = sign(pre)·norm(pre→post),
norm = synapse fraction of the postsynaptic neuron's total input. NT signs (standard *Drosophila*,
per Shiu et al. PMC10187186): ACh=+1, GABA=−1, glutamate=−1 (GluClα); dopamine/serotonin/
octopamine/tyramine/histamine and unknown = 0 (dropped from fast E/I). Reported: spectral
radius ρ=max|λ| and max-real-part α=max Re λ.

## Results (whole CNS, ≥5-synapse threshold; 118,593 neurons, 1,300,899 signed edges)
- **REAL: ρ = 0.7627, g\* = 1/ρ = 1.31, α = 0.7627.** → The wiring is **near-critical but slightly
  SUBcritical** at unit gain, reaching exact criticality at a modest, biologically plausible
  gain (~31% amplification). It sits *just under* the edge, not deep in either regime.
- **Null (A) sign-shuffle** (permute E/I labels, keep topology+weights): ρ = 0.744 ± 0.035 →
  **REAL z = +0.5 (NOT special).** E/I *placement* is generic — same verdict as Track 1's gross
  closure: a network-statistics triviality, not organization.
- **Null (B) weight-permute** (permute synapse weights across edges, keep topology+signs):
  ρ = **2.154 ± 0.028** → **REAL z = −49.9.** The real weight arrangement holds ρ near 1, where
  reshuffling the *same* weights drives it to ρ≈2.15 (deeply supercritical / chaotic, g\*≈0.46).
  **This is the above-null signal: synaptic weight placement keeps the network near criticality.**
- **Central-brain subnetwork (32,497 neurons):** ρ = 0.742, g\* = 1.35 — same regime as whole CNS.
- **Robustness — glutamate sign:** flipping glutamate to +1 leaves ρ = 0.7627 unchanged → result
  is insensitive to the glutamate-sign convention. (Exact equality flagged for a second look.)

## Honest verdict (interim)
- The connectome is **organized near the critical boundary**: ρ≈0.76, critical at a small
  physiological gain. The real **weight arrangement** is dramatically non-generic (z≈−50) in
  holding it there — random reshuffling of the same weights would make it supercritical.
- This **mirrors Track 1's structure-of-evidence:** the *generic* feature (here E/I placement,
  z=+0.5; there gross recurrence) is a network-size triviality; the *one non-generic, defensible
  signal* (here weight placement → near-criticality; there reciprocal feedback) is the real result.
- **Speaks to FMT's criticality (Class-4) pillar ONLY** — NOT the self-model taxonomy, NOT fly
  consciousness, NOT FMT confirmation. Linear/spectral proxy; the dynamical confirmation is pending.

## CAVEATS (must carry into any writeup)
1. **42% of neurons dropped.** 64,923 of 155,926 have NT="none" (+~4,800 modulatory) → excluded
   from the E/I matrix. Need a robustness rerun including them (e.g. as ACh+, or NT-score-gated).
2. **Weight-permute interpretation.** z≈−50 may partly reflect a weight–degree anticorrelation
   (hubs carry weaker per-synapse weights) rather than bespoke "tuning for criticality." The
   *outcome* (real sits near ρ≈1, null at 2.15) is solid; the *mechanism* needs the degree-
   preserving rewire null (Track 1's gold standard) to separate topology from weight placement.
3. **Linear ≠ dynamical.** ρ is the linear-stability branching proxy. The publishable claim needs
   the spiking sim: avalanche power-laws + branching ratio ≈1 + edge-of-chaos at g≈g\*, real vs null.

## DYNAMICAL RESULTS (Brian2 LIF, 118,593 neurons, gain sweep, real vs weight-shuffled)
Method: connectome-constrained current-based LIF (NT-signed, norm weights), weak Poisson
background → operating point; global-gain sweep G∈[0.8,13]; criticality fingerprint = **Fano
factor** (Var/Mean of population activity = susceptibility, peaks/grows at criticality), plus MR
branching m, rate, saturation. 17 gains × {real, weight-shuffled} × 2 seeds = 68 runs, T=40 s each.
(Drive-free kicks died from sparsity; MR-under-drive got swamped — operating-point Fano is the
robust measure. Raw traces saved for avalanche re-analysis.)

**Headline:** the REAL connectome enters the high-susceptibility (large synchronous fluctuation)
regime at ~HALF the gain of its weight-shuffled null:
| measure | REAL | WSHUF |
|---|---|---|
| Fano > 50 onset | **G ≈ 1.8** | G ≈ 3.0 |
| Fano > 500 onset | **G ≈ 3.0** | G ≈ 6.5 |
| Fano @ G=2.0 | **199** | 12 |
| rate @ G=8 | 28 Hz | 70 Hz (shuffle runs hot/asynchronous instead) |

So the real synaptic-weight arrangement is organized to reach critical-like collective dynamics at
LOW, biologically-plausible gain, where randomizing the same weights instead produces smooth
high-rate (asynchronous, saturating) activity and needs ~2× the gain to match the susceptibility.
This is the **dynamical echo of the spectral z = −50 weight-arrangement signal** — the one genuine
organizational finding, now confirmed in the spiking dynamics.

**Honest nuances (must carry):**
1. ~~**It INVERTS the linear spectral prediction.**~~ **[CORRECTED S231 — this was a NULL-MODEL MISMATCH
   ARTIFACT, not a real inversion. See "SESSION 231 UPDATE" below.]** Script 07 permuted *unsigned
   magnitude* (signs fixed) → ρ=2.15; the spiking worker permuted the *signed* weight as a unit
   (`_track2_worker3.py:35`) → that null's actual ρ=**0.51** (verified). Against the matched null
   (0.51 < real 0.76) the linear and dynamical rankings AGREE — there is no inversion. The residual is
   eigenvector localization: real ρ=0.76 is carried by an isolated 2-neuron inhibitory pair (PR≈2).
2. **Fano rises monotonically, no clean peak within G≤13.** **[RESOLVED S231 — the avalanche analysis is
   done: the high-Fano regime is SYNCHRONOUS BURSTING, not clean criticality. See below.]**
3. **MR branching m saturates ~0.95–0.99 for both** → not discriminating here; Fano is the workhorse.

**Scope (unchanged):** tests the **criticality precondition only**. A real organizational signal is
present (real > weight-null), but this is NOT fly consciousness and NOT FMT confirmation — consciousness
needs the self-model architecture + closure too, which a static connectome + generic LIF cannot show.
For MG's "is the fly conscious": still unlikely-but-not-excluded — we found dynamical *organization*,
not a self-model. **[S230 verdict "clean defensible precondition positive on criticality" is DOWNGRADED
by S231 — see below: the dynamical signal is organized synchronous BURSTING, not edge-of-chaos
criticality.]**

---

## SESSION 231 UPDATE (2026-06-19) — avalanche analysis, inversion correction, robustness reruns

The three S230 follow-ups are done. Net effect: **the criticality claim does not survive; the surviving
signal is organized synchronous bursting.** Scripts/outputs: `11_avalanche.py` + `avalanche_out/`,
`inversion_explanation.md`, `verify_inversion.py`, `08b_build_net_ntunknown.py`, `08c_build_net_rewire.py`,
`robustness_prep.md`.

### 1. Avalanche power-laws → NOT criticality, it's BURSTING  (`avalanche_findings.md`)
Poil/Shew-style thresholded avalanches (median + p25/p75 θ, `powerlaw` 2.0.0 Vuong tests + own CSN MLE)
on all 68 traces. **Four independent lines all reject clean criticality:**
- **Lognormal beats power-law for P(S) at every G and mode** (Vuong R −2…−54, p≪0.001). P(S) is visibly
  convex with a tail knee — a characteristic scale, not scale-free.
- CSN τ comes out **5–42 (not ≈1.5)** over only 0.03–0.5 fit decades; durations span ~1–1.6 decades and
  decay geometrically (near-exponential).
- **Crackling relation fails ~10×**: γ_pred 0.06–0.13 vs γ_fit ≈1.3–1.7 in the high-Fano real regime.
- **Exponents not threshold-robust** (G=2.25 real τ: 13→28→50 across p25/median/p75) — itself the verdict.

**real vs wshuf:** real produces 3–4× larger/longer excursions at matched gain (maxS 4735 vs 1244 at
G=1.8) — i.e. the connectome adds *synchronous burstiness, not criticality*. The G≈1.8 "susceptibility
onset" is where rare large synchronous excursions begin, not an edge-of-chaos point.
**Caveat carried:** the driven operating-point design (weak Poisson background, never-zero baseline,
40 s @ 1 ms bins, in-deg ~11 too sparse for drive-free avalanches) *limits power to detect* criticality —
a cleaner test needs near-threshold/drive-free dynamics and longer runs. But on this design, the evidence
is squarely bursting/lognormal, not power-law.

### 2. The "inversion" was a NULL-MISMATCH ARTIFACT (corrected)  (`inversion_explanation.md`, verified `verify_inversion.py`)
- Script 07 permutes **unsigned magnitude**, signs fixed → ρ=2.15. The spiking worker permutes the
  **signed** weight as a unit → that null's ρ = **0.5133** (independently reproduced by orchestrator).
  So S230 paired a spectral number (07's null) with a dynamical comparison against a *different* null.
- Against the **matched** null (ρ 0.51 < real 0.76), linear and nonlinear rankings AGREE — no inversion.
- **Worse for the spectral story:** real ρ=0.76 is carried by an **isolated 2-neuron reciprocal-inhibition
  pair** (nodes 77312↔3728, leading-eigenvector PR = **2.11**, 97.3% of the mode mass, out-degrees 2–3).
  So the spectral "near-criticality" is a *localized motif*, NOT a global property. λ_max is a poor proxy
  for collective criticality here; lead with dynamics, and attach a leading-mode-localization (PR) check
  to any future spectral pre-screen. The z=−50 magnitude-permute result stands as a number but its
  "tuned for criticality" interpretation is undermined (it moves a ρ that a 2-node island dominates).

### 3. Robustness reruns — DONE (full 17-gain × 2-seed sweeps)  (`robustness_prep.md`, fig `track2_robustness_figure.png`)
- **(a) NT-unknown included** (`track2_net_thr5_ntall.npz`, +87,554 excitatory edges): the susceptibility
  signal is UNCHANGED in direction and slightly STRENGTHENED — Fano>50 onset at **G≈1.4** (vs real 1.8),
  i.e. the extra excitation makes it more susceptible, not less. The criticality/bursting verdict does
  not depend on dropping the 42% NT-unknown neurons.
- **(b) Degree-preserving rewire null** (`track2_net_thr5_rewire_s{1,2}.npz`; in/out-degree + signed-weight
  multiset preserved exactly, topology randomized to 0.28% overlap): Fano>50 onset at **G≈3.0** — identical
  to the weight-shuffle null and ~1.7× the real net's 1.8. So the "real reaches high susceptibility at half
  the gain of its nulls" signal **SURVIVES the gold-standard degree-preserving rewire** — the organization
  lives in the higher-order topology/weight arrangement, not in the degree sequence or weight multiset.

**Fano>50 onset (full sweep):** real **G=1.8** · weight-shuffle G=3.0 · degree-rewire G=3.0 · NT-all G=1.4.
**Fano>500 onset:** real 3.0 · wshuf 6.5 · rewire 6.5 · NT-all 2.0. The organizational signal is real and
robust across both null models and the NT choice — but (per §1) the high-Fano regime it describes is
**synchronous bursting, not clean criticality.**

### Corrected honest verdict (S231)
- **No clean criticality / edge-of-chaos detected** in the BANC connectome on this analysis. Avalanches
  are lognormal/bursting at every gain; the spectral "near-criticality" is a localized 2-node motif.
- **What survives:** the real weight+topology arrangement produces organized *synchronous bursting*
  (large collective fluctuations) at LOWER gain than its nulls (signed-shuffle ρ=0.51; degree-rewire
  smoke Fano ≪ real). A genuine organizational signal — but burstiness/synchrony, **not** criticality.
- **For FMT's criticality (Class-4) pillar:** this is now **neutral-to-negative** evidence from the fly
  connectome — we did NOT find edge-of-chaos; we found driven synchronous bursting. Report honestly;
  do not cite the fly connectome as a criticality-pillar positive.

### Status — AIW-90 CLOSED (S231)
All three follow-ups + both robustness reruns done; figure `track2_robustness_figure.png`. Final verdict:
organized synchronous bursting at lower gain than both nulls (robust), NOT edge-of-chaos criticality;
fly connectome = neutral-to-negative on FMT's criticality pillar.
- (Optional, only if the criticality question becomes load-bearing for a writeup) a near-threshold /
  drive-free or longer-T avalanche test to settle whether the bursting verdict is design-limited.
- The constructive criticality question moves to **AIW-91** (build the minimal critical closed-loop net).

## (Superseded) original plan for the dynamical confirmation — brian2 2.10.1 installed
1. Brian2 LIF connectome-constrained model (E/I signs, norm weights), `cpp_standalone` + OpenMP24
   (CPU, no GPU needed) — or `cuda_standalone` on the 4090 for the full untruncated fine sweep
   (needs CUDA-12 toolkit; see `tmp/cuda-gpu-setup-commands.txt`).
2. **Targeted gain bracket around g\*≈1.3** (not a blind 40-pt sweep — the spectral result already
   located the critical point): measure branching ratio, avalanche size/duration exponents,
   order parameter. Degree-preserving-shuffle control at each gain.
3. Add the two robustness reruns from CAVEATS (1)+(2). Update this file → final.
