# Open-data test of the FMT ESM/EWM double dissociation (d′ ⊥ meta-d′)

**Session 234 · 2026-06-25 · WSL.** Executes the aIware P0 inbox brief (MG directive 2026-06-19),
following the read-only scout catalog `handoff-metacog-dataset-scout-2026-06-19.md` (produced in a `life`
session; ownership migrated here). Distinct from the dropped AIW-47 eNeuro paper — that died because the
Bonn ketamine data was *staircased* (d′ clamped, meta-d′ inflated; Rahnev et al. 2019). This test uses
datasets where **d′ is free to vary**.

## What FMT predicts (the target)
FMT (`paper/full/four-model-theory-full.md` §8, item 4) predicts the **ESM and EWM are independently
disruptable** and states *"the clean double dissociation has not been experimentally demonstrated."*
Operationalised in the type-2 SDT framework:

- **d′** (type-1 sensitivity) = the **EWM** discriminating world states.
- **meta-d′ / M-ratio** (type-2 sensitivity / efficiency) = the **ESM** monitoring its own perceptual states.

Orthogonality of d′ and meta-d′/M-ratio = the metacognition-paradigm form of the ESM/EWM dissociation.

## Data (provenance — raw data NOT committed; re-downloadable)
| Dataset | Source | n | role |
|---|---|---|---|
| Rouault, Seow, Gillan & Fleming 2018, **Expt 1** | github.com/metacoglab/RouaultSeowGillanFleming · DOI 10.1016/j.biopsych.2017.12.017 (MIT repo) | 498 | structural orthogonality + ESM-axis (published) |
| Rahnev 2013 (Confidence DB) | OSF s46pr · DOI 10.1038/s41562-019-0813-1 | 12 | **EWM-axis** within-subject contrast manipulation |
| Shekhar & Rahnev 2018 (Confidence DB) | OSF s46pr | 19 | prefrontal-TMS probe (null here) |

Pipeline: Maniscalco–Lau MLE meta-d′ (`metad_mle.py`, 4 passing unit tests; `metadpy 0.1.2` available as
cross-check). Scripts in this directory reproduce every number below.

## Results

### 1. Data integrity (Rouault) — EXACT
Type-1 d′ recomputed from trial-level data reproduces the authors' published `da` over all 498 subjects:
**max|diff| = 0.0019, mean|diff| = 0.0003.** The authors' peer-reviewed Maniscalco–Lau fits are therefore
used directly for the structural statistics.

### 2. Structural orthogonality (Rouault, n=498)
d′ has genuine spread (mean 1.26, sd 0.41, range 0.28–2.46; difficulty titrated but not clamped — `dotavg`
vs d′ r=0.04).

- **d′ vs meta-d′: r = +0.47 (R² = 0.22)** → **78% of metacognitive-sensitivity variance is not explained by
  first-order performance.**
- **d′ vs M-ratio: r = −0.20** → metacognitive *efficiency* is approximately orthogonal to performance.

### 2b. Multi-dataset robustness (Confidence Database, OSF s46pr) — 20 datasets, n=2,752
Screened the CDB index (`Database_Information.xlsx`) to perceptual datasets with ≥4-point/continuous
confidence, n≥10, ≥100 trials; fit per-subject d′/meta-d′/M-ratio (same Maniscalco–Lau pipeline). 20
datasets yielded usable fits (10 skipped: non-binary Stimulus/Response coding — conservative, no silent
corruption). Figure: `cdb_orthogonality_figure.png`; per-dataset table: `cdb_results.json`.

- **Pooled (2,752 subjects): d′ vs M-ratio r = −0.03** — metacognitive efficiency essentially uncorrelated
  with first-order performance across the whole open perceptual corpus.
- **Per fixed-difficulty dataset: median r(M-ratio, d′) = −0.14** (13 datasets; range −0.37 to +0.78, the two
  positives small-n n≤65). The structural orthogonality replicates broadly, not just in Rouault.
- **Built-in positive control:** an empirical clamp-detector (within-dataset d′ SD < 0.25) independently
  flagged **Rouault Expt 2** — the dataset the scout names as staircased — confirming the staircase compresses
  d′ variance exactly as Rahnev et al. (2019) describe. 7 of 20 datasets flagged clamped; the orthogonality
  statistics above are reported on the 13 fixed ones (pooled value is robust either way).

**Methods gotcha (carry forward):** CDB datasets use *inconsistent* binary codings for Stimulus/Response
({0,1} vs {1,2} vs …). An initial run assumed {1,2} and silently dropped half of each {0,1}-coded dataset,
pinning d′ at ~2.5 — caught only because it contradicted the independently-validated Rouault `.mat` (d′=1.26).
The fitter now auto-detects the two distinct values per dataset. Re-validated against Rouault before re-running.

### 3. EWM-axis manipulation (Rahnev, within-subject contrast, n=12)
A stimulus-difficulty manipulation moves d′ enormously while metacognitive efficiency is invariant:

| contrast | d′ | M-ratio |
|---|---|---|
| low | 1.05 | 0.961 |
| mid | 1.93 | 0.960 |
| high | 3.20 | 0.962 |

high vs low: **d′ Δ=+2.14, t(11)=13.1, p<0.0001, dz=3.78** · **M-ratio Δ=+0.002, t(11)=0.11, p=0.91, dz=0.03.**

### 4. ESM-axis
- **Published (cite directly):** Rouault 2018's headline — *psychiatric symptom dimensions are associated with
  dissociable shifts in metacognition but not task performance* (n=498). Symptoms move meta-d′/M-ratio with d′ matched.
- **Null in this reanalysis (report honestly):** prefrontal TMS (Shekhar DLPFC/aPFC vs S1 control) produced no
  significant change in d′, meta-d′, or M-ratio when collapsed across blocks (all p>0.27); V1 TMS (Rahnev) was
  also null and *sham* showed the only significant drop (time-on-task in both d′ and meta-d′).

## The double dissociation (assembled from open data)
| Axis | Manipulation | d′ (EWM) | meta-d′/M-ratio (ESM) | Evidence |
|---|---|---|---|---|
| **EWM** | stimulus difficulty/contrast | **moves 3×** | invariant | Rahnev reanalysis (this work) |
| **ESM** | psychiatric symptom dims | preserved | **shifts** | Rouault 2018 (published) + structural decoupling |

## Honest caveats (carry into any writing)
1. **Convergence, not discovery.** M-ratio's quasi-independence from d′ is an established finding
   (Fleming & Lau 2014; Rouault 2018). FMT is *consistent with* it and *retro-predicts* it — it does not claim
   to have discovered it. Use "consistent with" / "claims no priority."
2. **EWM-axis = difficulty, not lesion.** It shows metacognitive efficiency is invariant to first-order signal
   strength (the ESM readout is stable while the EWM signal degrades) — a weaker form than a focal selective
   lesion of the EWM.
3. **TMS sets null.** The architectural (TMS) perturbations did not deliver the dissociation here; the ESM-axis
   manipulation rests on Rouault's symptom result.
4. **Rahnev = 2-point confidence** → meta-d′ weakly identified; n=12. Treat the EWM-axis as a clear but small-n,
   exploratory-confidence demonstration. The d′ manipulation check is robust regardless.
5. This does **not** reopen AIW-47 (eNeuro standalone stays dropped). Deliverable = fold into the FMT empirical
   section.

## Extensions
- **[DONE this session] Confidence-DB multi-dataset sweep** → §2b above (20 datasets, n=2,752; pooled r=−0.03).
  Pipeline: `cdb_sweep.py --plan` / `--run N`. Note: **ds001512 (Gherman & Philiastides) is in the CDB as
  `Gherman_2018`** — no separate OpenNeuro pull needed; it's part of the perceptual eligible pool.
- **[remaining] Full sweep beyond top-30** — 67 eligible perceptual datasets exist (`cdb_selection.json`); this
  ran the 30 largest-n (20 usable). Extending to all 67 + recovering the 10 skipped (non-binary coding parsers)
  would push n well past 4,000. Diminishing returns — the result is already stable.
- **[remaining] tDCS-OFC (PMC12293014)** and **Lehmann/Sterzer 2022** — on-request causal/pharmacological
  ESM-axis sets (would add a *causal* ESM-axis arm to complement the correlational/symptom evidence).

---

## DRAFT passage for FMT §8 (Prediction 4) — for review before integration
> *Replaces the current closing sentence "the clean double dissociation has not been experimentally demonstrated."*

A reanalysis of openly available metacognition data is consistent with the predicted dissociation. In the
type-2 signal-detection framework, first-order sensitivity (d′) indexes the explicit world model's
discrimination, while metacognitive efficiency (M-ratio = meta-d′/d′) indexes the explicit self-model's
read-out of its own perceptual states. Across 498 participants (Rouault et al., 2018), metacognitive
sensitivity is largely decoupled from first-order performance — only ~22% of meta-d′ variance is explained by
d′ — and the same study reports that psychiatric symptom dimensions shift metacognition while leaving task
performance intact. This decoupling is not specific to one study: across 20 independent perceptual datasets
from the Confidence Database (2,752 participants; Rahnev et al., 2020), metacognitive efficiency is essentially
uncorrelated with first-order sensitivity (pooled r = −0.03; per-dataset median r = −0.14). Conversely, a
within-subject stimulus-difficulty manipulation (Rahnev et al., 2013)
triples d′ (1.05→3.20) while metacognitive efficiency remains invariant (M-ratio 0.96 throughout). Together
these constitute a double dissociation between first-order discrimination and metacognitive read-out
consistent with the architectural separability of the EWM and ESM. We claim no priority for the underlying
psychophysical regularities — the near-independence of metacognitive efficiency from performance is
well established (Fleming & Lau, 2014) — only that they are what the four-model architecture predicts. A
focal-lesion demonstration of selective EWM disruption with intact self-monitoring (and the converse) remains
the decisive test.
