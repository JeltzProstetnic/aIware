# Derived data and model outputs — preregistered DREAM reanalysis (OSF m4vju)

Outputs of the registered run of the frozen analysis pipeline (commit 2f30cc2bb27d81902662cdbd649b71df438f63ad,
Zenodo concept DOI 10.5281/zenodo.24060863) on the open DREAM datasets (Wong et al., 2025; metadata v9,
doi 10.26180/22133105; CC BY 4.0). Run date 2026-11-08 (run 2; run 1 failed in the model step on the R library
path and produced a byte-identical feature table). Licence: CC BY 4.0.

## Files

| Path | Content |
|---|---|
| `features.csv` | One row per selected DREAM record (920): set, file, subject, report category, stage, role (primary / set3 / set16_merged), clock time, channel, unit, sampling rate, record and window timing, segment counts, SWA (0.5–4 over 0.5–30 Hz, natural log), SWA 0.5–2 Hz (`swa_lo`), status (ok or exclusion reason), and the 20-s-window variants. |
| `features.csv.json` | Run metadata: deposit DOI and commit, manifest hash, metadata md5, software versions, start and end time, status counts. |
| `model-inputs/<analysis>.csv` | The table each model was fitted on: `SetID`, `SubjectID`, `SubjSet` (participant, nested in set), `Filename`, `Experience`, `Stage`, `swa_raw`, `z` (standardised within set), `SWA_between` (participant-by-stage mean of z), `SWA_within` (deviation, unit SD within set), top-decile flags and decile numbers on SWA_within and z, `time_raw` (minutes after 18:00, or awakening number in Set 16), `time_within`. |
| `model-inputs/prepare.json` | Awakening, participant and category counts per analysis; within-participant Spearman correlation of SWA_within with time of night per set. |
| `model-inputs/exclusions.csv` | Counts by set, category, role and status. |
| `model-inputs/deciles.csv` | Exploratory: per decile of SWA_within and of z, pooled and per set, counts of E, EWR, NE and the shares EWR/(EWR+NE), E/all, (E+EWR)/all. |
| `results/<analysis>.json` | Per analysis: sample, convergence ladder (R-hat, effective sample size per fixed effect), fixed effects on the latent and logit scales (posterior median, 95 % HDI), the decision (slope, HDI, verdict, P(slope > 0), P(slope < −0.6)), reported contrasts, variance components, top-decile levels, model-free top-decile proportions (Clopper–Pearson), category curves per decile. `h_lme4.json` holds the lme4 check. |
| `results/<analysis>.log` | R console output of each fit. |
| `run.log` | The run's progress log. |
| `run1/features.csv.json`, `run1/run.log` | Run 1 (failed in the model step on the R library path): its feature metadata, with the time of the first EEG read (`started_utc`), and its log. Its feature table is byte-identical to `features.csv`. |
| `make_figure1.py`, `test_make_figure1.py` | Draw Figure 1 of the results report from `results/primary.json` and `model-inputs/deciles.csv`. |

Analysis names: `primary`; `a_loo_<set>` (robustness a, leaving out one set); `b_n2`; `c_swa_lo`; `d_w20`;
`e_set3`; `f_s16merged_ne`; `g_px`; `h_lme4`; `i_no_slope`; `x_time` (exploratory, time of night added);
`scan` (the SCAN replication, empty until its data arrive).

Absolute paths inside the JSON files refer to the author's machine and are kept unchanged.
