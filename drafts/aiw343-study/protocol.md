<!-- AIW-343 — study protocol + OSF pre-registration draft. PRIVATE: drafts/ is excluded from the public mirror. Do not publish before data collection closes — participants are scientists and would find the hypothesis. -->
# Processing leaks and the sense of hidden depth — study protocol (draft v0.1, S358)

**Working title for participants (neutral):** *Perception and beliefs about the mind — a short survey.*
**Internal title:** Trait substrate-leak frequency predicts the hidden-depth form of the hard-problem intuition.
**Host:** Alpine Institute for Advanced Research (hosting, study page). **Controller:** the PI personally. **Language:** English first; DE/IT/FR later. **Ethics:** no ethics-committee review (MG decision 2026-10-28, D-S364-7): the study is anonymous and involves no intervention, so under Austrian law it does not require one (§10). **Closes:** 15 December 2026, 23:59.
**PI:** Matthias Gruber. **Source of the prediction:** FMT master §3.8 (lines 547–549), §3.6 (line 419), §3.7.2 (line 523); derivation in `docs/research/cheap-discriminating-prediction-s358.md` (Candidate 1).

## 1. Background in three sentences
FMT explains why consciousness seems mysterious by two mechanisms: the explicit self-model cannot represent the substrate that generates it (opacity, universal), and that opacity is punctured by occasional leaks of substrate processing into experience — phosphenes, visual snow, hypnagogic imagery, filling-in — which produce the nagging sense that "something vast operates just beyond the edge of introspective access" (§3.8). Leak frequency varies between people. If the second mechanism does any work, people who experience more leaks should hold the hidden-depth intuition more strongly, independent of their metaphysical beliefs.

## 2. Design
Two parts.

**Part 1 (this protocol, n ≈ 200):** one anonymous online questionnaire, ~25–30 min, cross-sectional. Fully anonymous (MG decision S358: no linking code, so RCSEQ fast track): no identifiers, demographics limited to 3 age bands + gender to prevent re-identification in a single-employer sample. Closing page invites volunteers to Part 2 through a **separate, unlinked** contact form. Part 2 cannot be linked to Part 1 answers; 2a/2b are standalone (2a re-measures leak frequency at its own baseline if moderation is wanted).

**Part 1, two recruitment arms (MG S358: *"200 is just a start, ideally i want 1000 participants"*; *"we will open the survey to the public at some point"*):**
- **Arm C (colleagues, n ≈ 200–220):** recruited personally by the PI. This arm runs the confirmatory test of H1–H2. The Arm C invitation link carries the constant URL parameter `?src=ppx`, stored in the hidden question `src` (channel label only: the same value for everyone, no ID). Responses without it are reported as an unlabelled channel.
- **Arm P (public, up to ~800, total ≤ 1,000):** opened later via the Institute website and social channels. It is an identical but separate LimeSurvey copy with its own survey ID. The source is therefore known from which survey a response came through, with no URL parameter and no extra question, so anonymity is unchanged. Arm P is a pre-registered **replication** of H1 with its own smallest effect of interest, partial r = .10. Both arms are covered by the same ethics application.
- The arms are analysed separately (C confirmatory, P replication), then pooled with an arm covariate as a descriptive estimate. The arms are not merged into one sequential test, so there is no optional stopping.

**Part 2 (separate protocol, volunteers from Part 1, target n ≈ 60–120):**
- 2a — causal complement, FMT master Prediction 6 leak arm (§8.7): 20-min dark-room eyes-closed session vs lit relaxation control, hidden-depth ratings before and after.
- 2b — Candidate 2 of the S358 report: imagery control (Gordon TVIC + transformation battery) vs vividness (VVIQ) as predictors of perceptual metacognitive efficiency (2AFC + confidence, meta-d′/d′).
Part 2 gets its own pre-registration once Part 1 is fielded.

## 3. Hypotheses (Part 1)
- **H1 (primary, directional):** leak frequency (Processing-Leak Inventory, PLI) correlates positively with the hidden-depth subscale (HD), controlling for the covariates in §5. Smallest effect of interest: partial r = .15. One-tailed test (the derivation fixes the sign).
- **H2 (differential):** PLI correlates more strongly with HD than with the explanatory-gap subscale (EG). FMT assigns the gap intuition to the universal opacity mechanism and the depth intuition to the leaks. Williams' test for dependent correlations (zero-order; partial version as sensitivity).
- **H3 (secondary, 2015 book claim S116, not a discriminator):** death anxiety correlates positively with dualism.
- **Mediation (exploratory, but decisive for interpretation):** the indirect path PLI → dualism/paranormal belief → HD is estimated; FMT predicts a direct path that survives, the sociocognitive account predicts full mediation.

## 4. Rival positions (for the pre-registration text)
IIT, GNW and PP make no prediction about the relation (none of them accounts for the meta-problem via perceptual leaks). Attention Schema Theory and illusionism locate the intuition in the self-representation's omission of mechanism and predict no relation to perceptual leaks. The sociocognitive account (anomalous experience → dualist/paranormal belief → mystery endorsement) predicts the relation is fully mediated by belief.

## 5. Measures
Full item text, order and response formats: `questionnaire-part1.md`.
- **Predictor:** Processing-Leak Inventory (PLI, new, 14 items, past-12-months frequency 1–5), preceded by an optional 30-s blind-spot demonstration.
- **Outcomes:** Hidden Depth (HD, new, 6 items, 1–7 agreement); Explanatory Gap (EG, 4 new items + 2 items on the Gottlieb & Lombrozo 2018 stem). Díaz (2021) items not used (deceptive vignette). Absorption dropped (licence).
- **Covariates:** unusual experiences (O-LIFE UnEx short), trait dissociation (DES-B, time frame adapted to 12 months), dualism (Riekki et al. 2013 own reflective-dualism items, 6; plus the 5 Navarro-Peña et al. 2026 mind–brain position statements, descriptive and for comparison with neuroscientists), paranormal belief (Tobacyk RPBS, 26 items), religiosity (2 items), death anxiety (DAP-R Fear of Death subscale, 7 items, Wong, Reker & Gesser 1994; German arm DAP-GR, Jansen et al. 2019, CC BY 4.0), openness (BFI-10), philosophy-of-mind exposure (3 items), meditation experience (2 items), sleep quality (1 item), age band (3), gender.
- **Flags:** diagnosed migraine with aura, diagnosed visual snow syndrome, diagnosed tinnitus, perception-affecting medication (prefer-not option on each).
- **Quality:** two infrequency items, one instructed-response item, completion time, funnel debrief.

## 6. Exclusions (pre-registered)
1. Fails ≥ 1 of the two infrequency items or the instructed-response item.
2. Completion time < 40 % of the median.
3. Funnel debrief names the leak–depth link (two blind raters; disagreements resolved by a third rater or excluded conservatively). Primary analysis with exclusion, sensitivity analysis without.
4. Incomplete responses (not submitted on the final page, incl. consent = No rows) are excluded and deleted at close — LimeSurvey stores answers page by page.
5. Missing > 20 % of PLI or HD items. Otherwise person-mean imputation within the scale.
Participants with clinical flags are **kept** in the primary analysis and excluded in a sensitivity analysis (they carry real leak variance; excluding them a priori would restrict range).

## 7. Analysis
Analysis code is pre-registered: `scripts/aiw343_analysis.py` (tested on simulated data, `scripts/test_aiw343_analysis.py`).
- Scale scores: item means after reverse-coding; reliability ordinal ω (report α too).
- CFA: two correlated factors (HD, EG) vs one factor; report CFI, RMSEA, ΔBIC. If HD and EG do not separate (one-factor fits better by ΔBIC > 10), H2 is reported as untestable and H1 is run on the combined mystery score as a pre-registered fallback.
- **H1:** OLS of HD on PLI + covariates, HC3 robust SEs; report partial r with 95 % CI; one-tailed p.
- **H2:** Williams' t for r(PLI,HD) vs r(PLI,EG) given r(HD,EG).
- **H3:** Pearson r(death anxiety, dualism), two-tailed; robustness check without the two afterlife items (`das_5`, `das_7`), which overlap in content with dualism.
- **Mediation:** bootstrap (5,000) indirect effect via dualism and paranormal belief; report proportion mediated. **The full-mediation criterion uses the reliability-corrected (errors-in-variables) direct effect**, not the naive OLS one: measurement error in the mediators leaves a spurious direct path, a bias in FMT's favour. Simulation (S358, n = 200, true direct effect 0, 40 runs): naive OLS falsely finds a direct path in 5/40, the corrected estimate in 1/40. Both are reported; the corrected one decides.
- `block_order` (A: perception block first; B: beliefs first) enters H1 as a covariate. **Exploratory:** HD(A) − HD(B), because attending to one's own leaks (and the blind-spot demo) before the belief items is a mild manipulation of the very mechanism under test; FMT expects HD(A) ≥ HD(B). Reported, not used as confirmation.
- Distributions of all scales reported (range restriction in a scientist sample).
- α = .05 throughout; no correction across H1–H3 (distinct questions, pre-specified).

## 8. Power
n = 200 with 12 covariates (Fisher z, df = n − 3 − 12; computed S358): partial r = .20 → power .87 one-tailed; r = .25 → .97; r = .15 → .66. The design decides r ≥ .20; .10–.20 is inconclusive and will be reported as such. Target 220 completions to absorb ~10 % exclusions. **Arm P** (computed S358, same covariates): n = 800 gives power .88 for partial r = .10 (one-tailed); n = 1,000 total gives .93. The arm P stopping rule is fixed in advance: stop at 800 valid completions or at the expiry date, whichever comes first.

## 9. Falsifier
H1 fails if the partial r ≤ 0 with the 95 % CI excluding .15, **or** if the direct path is fully mediated by dualism and paranormal belief. Then the leak mechanism of master §3.8 contributes nothing measurable to the intuition, and §3.8 is rewritten with one mechanism. A result in .00–.15 is reported as inconclusive, not as support.

## 10. Ethics and data protection
- Anonymous; no IP addresses, no device fingerprints, no login; hosting in the EU.
- Voluntary; recruitment by the PI personally (employer clearance obtained by the PI before recruiting), no record of who participated, no benefit or penalty; the PI never sees who took part.
- Withdrawal: possible until submission; after submission answers cannot be identified and so cannot be removed (stated in the consent text).
- Sensitive items (hallucination-like experiences, dissociation, death anxiety) carry a skip option and a support contact.
- Part-2 contact form: separate database table/survey, email only, deleted after Part 2 recruitment closes or 12 months at the latest.
- Raw data retained 10 years (good scientific practice); de-identified data published with the paper (OSF), minus free-text debrief answers.
- **Public-file anonymisation rule (S361-6, `docs/research/aiw343-ethics-review-impact.md`):** before any deposit, every combination of quasi-identifiers (age band, gender, diagnosis flags) must occur in ≥ 5 rows (k ≥ 5); gender is collapsed to 3 categories and the diagnosis flags to one 'any diagnosed' flag in the public file; the arm indicator (colleague vs public) and the `src` channel label are withheld from the public file; rows that still fail k ≥ 5 have the offending variable suppressed. Legal basis for collection: explicit consent, Art. 6(1)(a) + 9(2)(a) GDPR.
- Data controller: **the PI personally** (MG decision S358); the Institute hosts. Part 2 may move to the Institute once the Verein is registered.
- **No ethics-committee review (MG decision 2026-10-28, D-S364-7):** the study is anonymous and involves no intervention; under Austrian law it does not require review by an ethics committee. This applies to both arms. Participants are told so in the consent text and on the closing page.
- Closing date: 15 December 2026 (survey expiry 23:59). The Part-2 contact form expires on 28 October 2027 (12 months).

## 11. Timeline (to fix with MG)
Instrument licences → 3-response smoke test on the live server (replaces the pilot, MG 2026-10-28) → OSF pre-registration (frozen analysis code) → fielding until 15 December 2026 → Part 2 invitations.
