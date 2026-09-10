<!-- Action: reference -->
<!-- Tracked-by: AIW-47 -->
# AIW-47 — Standard-method meta-d′ reanalysis + certified hierarchical HMeta-d (Session 223, 2026-06-12)

Durable record of the corrected ketamine meta-d′ numbers. **Supersedes the joint-likelihood
values in `docs/aiw47-selftest/results.md` §7 for anything that goes into the paper.**

## THE CRITICAL FINDING (why this session happened)
Our original self-test estimator `tmp/aiw47-data/metad_mle.py` uses a **joint** type-2 likelihood.
The field-standard Maniscalco–Lau / Fleming meta-d′ is **response-conditional** (the method Lehmann
et al. used). They give materially different numbers on these biased-observer data:

| measure | **STANDARD (response-conditional, metadpy.mle)** | our joint metad_mle (WRONG for paper) |
|---|---|---|
| d′ | 0.868 / 0.987 · Welch p=0.114 · MWU 0.096 · g=−0.49 | identical (type-1 unaffected) |
| **meta-d′** | **0.423 / 0.695 · Welch p=0.085 (n.s.) · MWU 0.071 · g=−0.55** | 0.718 / 0.891 · p=0.019 · g=−0.75 |
| M-ratio | 0.501 / 0.724 · Welch p=0.177 · MWU 0.186 · g=−0.42 | 0.834 / 0.914 · p=0.152 · g=−0.45 |
| interaction (meta-d′−d′) | Welch p=0.366 · g=−0.28 | p=0.371 · g=−0.28 |

**The joint likelihood inflated meta-d′ AND turned a non-significant trend (p=0.085) into a "significant"
result (p=0.019).** Submitting the joint numbers would have been caught instantly by Lehmann (he runs
standard HMeta-d). **All paper numbers MUST use the STANDARD column.** (Format: ket / pla.)

## Certified hierarchical Bayesian HMeta-d (our own, independent)
metadpy 0.1.2 stubs its group/between models, so we built the hierarchical between-subjects model in
PyMC **on metadpy's validated single-subject response-conditional likelihood** (verified term-for-term),
vectorized, sampled via numpyro/JAX. Group-level prior on log(M-ratio) per condition.
- Run: `tmp/aiw47-data/hmetad_vec.py 2000 4 4000 0` → **0 divergences/8000, max R-hat 1.027** (residual
  is the small-sample group-SD funnel; result stable across 3 independent runs).
- **group M-ratio: Ketamine 0.465 [0.32, 0.62], Placebo 0.660 [0.45, 0.89]**
- **log-M-ratio diff (ket−pla): mean −0.348, 95% HDI [−0.86, +0.14] (94% equal-tailed [−0.83, +0.13]; both include zero); P(ket<pla)=0.92** (seed 20260612; reproduced exactly S224)
- → The hierarchical fit AGREES with the standard MLE: a direction-consistent efficiency **trend** whose
  credible interval includes zero — NOT robustly established between-subjects. (Authors established
  significance with the better-powered hierarchical model + a per-subject staircase-SD covariate we lack.)

## Design / data facts (confirmed from OSF materials)
- Between-subjects (randomized parallel groups), 26 ketamine / 19 placebo, 1 row/subject → no within-subject
  pairing key exists (the earlier "paired reanalysis could rescue M-ratio" idea is moot).
- Staircase titrated accuracy to ~64% (SPSS: Percent_correct 58–70%) → d′ is held near-flat BY DESIGN
  (H2 staircase caveat stands; decisive test needs FREE d′).
- Authors' own analysis (verified from their OSF scripts `Material_Behavioral_Data_Syntax.sps` +
  `Script_Hmetadprime.m`, Session 224): per-subject meta-d′ via Fleming's `fit_meta_d_mcmc` (Bayesian
  HMeta-d, response-conditional) → **independent-groups t-test** on the per-subject DVs (dprime,
  metadprime, MRatio): *"Significant ketamine effect on meta-d′. Marginally significant effect on MRatio.
  No significant effect on primary task performance [d′], RTs, mean rating, or metacognitive bias."*
  Confirmed by **ANCOVA with Staircase_SD covariate** (`UNIANOVA metadprime BY Drug WITH Staircase_SD`):
  *"No deviation from t-test results."* A group-level `fit_meta_d_mcmc_group` gives the log(M-ratio) diff HDI.
  → **They did NOT run a drug×measure interaction**; their selectivity rests on (sig meta-d′ + n.s. d′).
  → So the original "significant" vs our "trend" gap on meta-d′ is the **per-subject estimator (Bayesian vs
  our MLE) + the staircase-SD covariate**, NOT hierarchical pooling. On M-ratio/efficiency we AGREE with
  them (both marginal/HDI-includes-zero). Abstract (Lehmann et al. 2022 BBR) confirms the behavioral result
  IS in that paper → the citation is correct + complete (resolves the round-2 review's H-2).

## Scripts (in tmp/aiw47-data/ + copied to paper/aiw47/)
- `recompute_standard.py` — STANDARD MLE per subject (metadpy.mle) + corrected stats + regenerates
  `paper/aiw47/figure1.{png,pdf}`. **This is now the canonical Figure-1 generator** (supersedes the
  joint-based `make_figure1.py`). Corrected per-subject table: `tmp/aiw47-data/results_metaketa_standard.csv`.
- `hmetad_vec.py` — certified hierarchical Bayesian fit (PyMC+numpyro on metadpy likelihood).
- `interaction_analysis.py` — the drug×measure interaction (joint values; rerun on standard if needed).
- Toolchain installed into the venv this session: scipy, numpyro, jax, arviz, metadpy, pymc, openpyxl.

## Data protection
Author-shared vectors (`tmp/aiw47-data/data/MetaKetaII_nRS1_nRS2.xlsx`) are NOT redistributable —
never commit to public origin; `paper/aiw47` is already excluded from the public mirror.
