<!-- Action: reference -->
# AIW-47 Self-Test — Open-Data Scoping (Session 216, 2026-06-10)

**Tracked-by: AIW-47.** Question: can we self-test the eNeuro paper's two operationalization targets on existing open data before publishing? **Answer: meta-d′/d′ YES; PCI NO (cite instead).**

## Prediction 1 — meta-d′ / d′ dissociation → SELF-TESTABLE on open data
**Primary resource: the Confidence Database** (Rahnev et al. 2020, Nat Hum Behav). https://osf.io/s46pr/ — fully open, ~145+ datasets, >8,700 participants, ~4M trials, trial-level CSVs (stimulus/response/accuracy/confidence). Master index **`Database_Information.xlsx`** tags each dataset by paradigm/manipulation/population — **grep this first** to enumerate every pharmacological/clinical/TMS/sleep dissociation candidate in one pass.

**Best dissociation candidates (ranked):**
1. **Ketamine meta-perception (Neuner/Lehmann et al. 2022)** — *the clean textbook case.* d′ held flat by staircase while **meta-d′ dropped under ketamine** (double-blind, placebo-controlled, preregistered, 2AFC). OSF: https://osf.io/gucm2/ — **VERIFY behavioral trial-level CSVs are downloadable** (project currently exposes prereg + analysis scripts; data may be in scripts folder or on request).
2. **Ketamine + episodic-memory metacognition (NoC 2021)** — N=53 (24/29), between-subjects, meta-d′ impaired, **d′ unaffected**. OSF: https://osf.io/numxs/ (behavioral in supplementary).
3. **ccPAS double dissociation (Di Luzio, …, Romei 2025, bioRxiv)** — causal: boost V5/MT→V1 raises d′ sparing metacognition; boost IPS/LIP→V1 raises metacognitive efficiency sparing d′. **Data status unverified** (check Data Availability / email Romei lab, Bologna). Would rank #1 if open.
4. **Schizophrenia visual-motion metacognition (Charles et al.)** — **fully open NOW:** https://osf.io/84wqp/ — d′ slightly lower, **meta-d′/M-ratio preserved**. Best *immediately-confirmed-open* set for an end-to-end **methods rehearsal** of the meta-d′ pipeline (today), though it's a "preserved-meta despite altered-perception" pattern, not a meta-d′ collapse.

**Tooling:** meta-d′ via the hmeta-d / Maniscalco-Lau estimator (Python or MATLAB). 

**Single next action:** (1) pull `Database_Information.xlsx`, filter manipulation column; (2) verify ketamine CSVs at osf.io/gucm2 — if present, that's the clean dissociation to self-test pre-publication; (3) use osf.io/84wqp as the immediate pipeline rehearsal.

## Prediction 2 — PCI (TMS-EEG) → NOT self-testable on open data
- **Code is open** (PCIst: https://github.com/renzocom/PCIst, Comolatti 2019; EBRAINS wrapper). **Data is not.** The Massimini/Casali cross-state benchmark (Casali 2013 / Casarotto 2016: conscious-vs-unconscious controls + DOC across NREM/REM/propofol/xenon/ketamine) is **not** on OpenNeuro/Zenodo/figshare/EBRAINS. Only single-state (wakefulness) TMS-EEG is open → no across-state contrast → can't test the prediction.
- **Recommendation:** keep PCI in the paper as a neural operationalization, but **cite the published PCI cross-state results as confirmatory** rather than re-analysing raw data. (Optional: request the benchmark data from the Milan group — collaboration-gated.)

## Implication for the eNeuro paper
Both operationalizations stay in the paper. Only **meta-d′/d′ is self-tested** by us (open data exists); **PCI is cited**, not re-run. The self-test, if it holds, upgrades the paper from "prediction" to "prediction + preliminary evidence."
