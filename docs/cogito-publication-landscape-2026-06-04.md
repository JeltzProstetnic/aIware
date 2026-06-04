# COGITO Publication Landscape — Gap Analysis for RIM-on-COGITO

**Compiled**: Session 211, 2026-06-04. Three parallel research subagents.
**Purpose**: Establish whether a RIM (Recursive Intelligence Model) variance-asymmetry test on COGITO data is genuinely novel ground, identify the closest analogues, and recommend publication venues.

---

## 1. COGITO study facts (verified)

- **PIs**: Ulman Lindenberger, Martin Lövdén, Florian Schmiedek
- **Sample**: N=204 (101 young 20-31, 103 older 65-80)
- **Design**: 100 daily test sessions + pre/post + brain imaging subset
- **Measures**: perceptual speed, episodic memory, working memory + daily affect/well-being + self-reports
- **Access**: restricted — application via cogito@mpib-berlin.mpg.de (Maike Kleemeyer), COGITO Steering Committee review + data transfer agreement
- **Publications**: 70+ since 2010

---

## 2. Schmiedek COGITO portfolio (top relevant)

| # | Paper | Year | Journal | Method | Variance dimension touched |
|---|-------|------|---------|--------|---|
| 1 | Hundred Days of Cognitive Training | 2010 | Front Aging Neurosci | Latent change scores, pre/post | Mean change |
| 2 | 2-year follow-up training transfer | 2014 | Dev Psychol | Latent change w/ retest | Mean trajectory |
| 3 | Within-person ≠ between-person structures | 2020 | PeerJ | Multilevel SEM, P-technique, KL divergence | Within-person covariance structure (static) |
| 4 | Ergodic Subspace Analysis (with von Oertzen, Voelkle) | 2020 | J Intelligence | ESA decomposition | **Variance decomposition into ergodic / within-only / between-only — closest to Cattell Data Box, but symmetric treatment** |
| 5 | Daily WM coupled with NA, attention, motivation (Brose et al.) | 2012 | Emotion | Multilevel coupling | **Mean coupling of motivation→WM; closest existing motivation-cognition link** |
| 6 | Daily PA and WM (Brose) | 2014 | Emotion | Multilevel coupling | Mean coupling (symmetric for PA) |
| 7 | DSEM on COGITO affect (Hamaker, Asparouhov, Brose, Schmiedek, Muthén) | 2018 | MBR | Bayesian DSEM in Mplus | **Residual NA variance increases after negative events — directional variance signal, but affect not cognition** |
| 8 | Fixed moderated time series (Adolf, Voelkle, Brose) | 2017 | MBR | Single-subject VAR + moderators | Context-shifting dynamics |
| 9 | Keeping it steady — older adults less variable | 2013 | Psych Science | Variance-component models | **Level of variability by age; not directional change as signal** |
| 10 | Sleep × WM in children (Könen, Dirk, Schmiedek) | 2015 | Dev Science | Multilevel diary | Sleep modulates daily WM |

**Methodological signature**: multilevel SEM first; latent change scores; variance-heterogeneity multilevel models; DSEM/MLM-VAR via collaborators; ergodic subspace methods with von Oertzen. **Not** a primary ctsem user.

**Recent direction (2022-2026)**: Migrating from COGITO to child/school intensive longitudinal work (UPWIND, FLUX projects via DIPF/IDeA).

---

## 3. Völkle ctsem + COGITO

| # | Paper | Year | Journal | Method | Note |
|---|-------|------|---------|--------|---|
| 1 | An SEM approach to continuous-time modelling | 2012 | Psych Methods | ctsem-precursor, stochastic differential equations | Foundational |
| 2 | Continuous-time with individually varying intervals | 2013 | BJMSP | OpenMx-based ctsem, oscillator extensions | Pre-package |
| 3 | ctsem R package release (Driver, Oud, Voelkle) | 2017 | J Stat Software | FIML OpenMx | **Canonical ctsem citation** |
| 4 | Hierarchical Bayesian ctsem (Driver, Voelkle) | 2018 | Psych Methods | Stan, random effects on all params | **Current frontier — N×T mixed-regime capable** |
| 5 | The role of time in psychological mechanisms | 2018 | MBR | Position paper | Lag choice is theoretically loaded |
| 6 | DSEM-on-COGITO benchmark (Hamaker, Asparouhov, Brose, Schmiedek, Muthén) | 2018 | MBR | Bayesian DSEM in Mplus | Völkle co-edited the special issue |
| 7 | CT modeling in prevention research (Hecht, Voelkle) | 2021 | Int J Behav Dev | Worked example | Previews Freiburg Evaluation appointment |
| 8 | Ergodic Subspace Analysis (with von Oertzen, Schmiedek) | 2020 | J Intelligence | ESA | **Völkle's one direct COGITO data touch** |
| 9 | Striving for sparsity / regCtsem (Orzek, Voelkle) | 2023 | SEM / MBR | LASSO/adaptive-LASSO in ctsem | Methodological frontier |
| 10 | Abilities + skill acquisition (Voelkle, Wittmann, Ackerman) | 2006 | Learn Indiv Diff | Early career | g + motivation contributions to learning slopes — only Voelkle paper engaging motivation-cognition |

**Völkle ↔ COGITO**: No first-author ctsem-on-COGITO paper. His direct COGITO touch is the 2020 ESA paper. Driver has no first-author ctsem-on-COGITO either. **Open lane.**

**Driver vs Völkle**: Driver = software/math/Stan. Völkle = conceptual framing, methodological positioning, applied demonstrations, PhD supervisor (Orzek, Gische, Hecht).

---

## 4. Variance-asymmetry tests in COGITO — explicit accounting

**Question**: Has anyone in the COGITO corpus published an analysis treating variance INCREASES vs variance DECREASES over the 100-day window as carrying DIFFERENT psychological signals?

**Answer**: **No.**

Closest approaches and why each is not the same:

| Paper | What it does | Why not variance asymmetry |
|-------|-------------|---------------------------|
| Hamaker et al. 2018 DSEM | NA variance increases after negative events | Affect not cognition; perturbation-response not regulator-loop |
| Brose 2012 (and 2014) | Motivation/affect → WM mean | Mean coupling not variance-direction |
| Schmiedek 2013 *Psych Science* | Older adults less variable on practiced tasks | Level of variance by age, not within-individual asymmetric trajectory |
| Schmiedek 2020 PeerJ | Within-person factor structures | Static decomposition, not temporal asymmetry |
| von Oertzen, Schmiedek, Voelkle 2020 ESA | Ergodic / within-only / between-only subspaces | Symmetric variance decomposition |
| Lövdén 2010 plasticity framework | Plasticity vs flexibility distinction | Theoretical anchor only, never operationalized as directional test |

---

## 5. Adjacent literature

- **Wittmann (2002, 1988)**: Brunswik-Symmetrie, five-Datenbox framework. Intellectual upstream of Schmiedek + Völkle. About predictor-criterion aggregation matching, not variance-direction-as-signal.
- **Hultsch, MacDonald et al. 2000** *Neuropsychology* — IIV-as-pathology framing in dementia.
- **MacDonald, Nyberg, Bäckman 2006** *TINS* — IIV ↔ neuromodulation (dopaminergic).
- **MacDonald, Hultsch, Dixon 2003** *Psych Aging* — variability predicts decline (directional but cohort-level, not within-individual regulator identification).
- **Ram & Gerstorf 2009/2011** *Psych Bull* — IIV-as-developmental-construct framework.
- **Nesselroade & Molenaar P-technique** — would host RIM-style test, never executes one.
- **Mestdagh et al. 2018** *Psych Methods* — mean-corrected variability index.

---

## 6. GAP statement — Is RIM-on-COGITO genuinely new ground?

**Verdict: YES, with one qualifier.**

The Berlin group has decomposed within-person structures (Schmiedek 2020), coupled daily affect/motivation to performance means (Brose 2012, 2014), modeled affect dynamics with DSEM/ctsem (Hamaker 2018, Voelkle 2018), characterized age-related stability (Schmiedek 2013), and built ergodic-subspace decompositions (von Oertzen 2020). Hamaker 2018 demonstrates that residual-variance changes carry signal — but for affect, not cognition, and only in response to external perturbations. The plasticity-flexibility distinction (Lövdén 2010) theoretically anticipates asymmetric variance interpretations but was never operationalized as a directional test.

**Qualifier**: The Brose 2012/2014 line already establishes that motivation is *a* driver of cognitive variability in younger adults. Schmiedek 2013 attributes older-adult consistency partly to stable motivation. So RIM's general thesis — motivation modulates cognitive variance — is not new. The **novel slice** is the *asymmetry-as-identifier* claim: that variance going UP and variance going DOWN flag DIFFERENT recursive regulatory pathways. That specific empirical test is open.

**Risk**: Reviewers may read it as "Brose 2012 with extra steps" unless the asymmetry-as-loop-identification claim is operationalized into a hypothesis the existing mean-coupling models cannot generate.

---

## 7. Identified gap analyses (concrete, not yet published)

1. **Asymmetric variance change models** — decompose within-person residual variance into expanding vs compressing days, test whether each carries different psychological signals (motivation/affect-driven expansion vs fatigue-driven compression).
2. **Motivation × ability interaction on variance-of-variance** — Schmiedek has motivation→mean but not motivation→within-day-variability or motivation×g→variability.
3. **Time-varying drift on COGITO** — regCtsem 2023 on COGITO 100 days: does the drift matrix itself drift as participants learn?
4. **Affect → cognition continuous-time mediation** — multivariate Ornstein-Uhlenbeck on COGITO with directed continuous-time effects from affect latents to cognition latents. Not published.
5. **Ergodic-subspace × motivation** — project motivation/effort indicators onto ergodic vs non-ergodic subspaces from ESA 2020; does motivation live in the shared subspace or the within-person-only?

---

## 8. Recommended target journals for RIM-on-COGITO empirical paper

| Journal | IF | Why fit | Desk-reject risk for independent |
|---------|----|---|---|
| **Psychology and Aging** (APA) | 3.62 | Where Brose 2014/2015, Schmiedek 2013, MacDonald 2003 publish. Editorially familiar with COGITO. | Medium — engages if literature embedding is impeccable |
| **Multivariate Behavioral Research** | 3.57 | Where Hamaker 2018, Voelkle 2018, Adolf 2017 publish. Methods-forward. | Low for methods papers with strong simulations |
| **Intelligence** (Elsevier) | ~3.5 | Wittmann/Brunswik intellectual home; intelligence-motivation interaction lands here | Medium-low — open to independents with solid data |
| **Frontiers in Aging Neuroscience** | ~4.1 | Where Schmiedek 2010 COGITO seminal paper landed | Very low desk-rejection (OA, APC ~$2950) |
| Psychological Methods | ~10 | Top methods journal | High desk bar — only if RIM-asymmetry estimator itself is the contribution |

**Recommended sequencing**: Psychology and Aging first (substantive home) → MBR (methods) → Intelligence (Wittmann tradition) → Frontiers Aging Neuro (fallback).

---

## 9. Recommended framing for the RIM-COGITO paper

> "Brose et al. (2012) and Schmiedek et al. (2013) established that motivation modulates cognitive variability in COGITO; what neither paper distinguishes is the direction of variance change. RIM (Gruber 2026) predicts that this direction is itself an identification signal: expanding variance days reflect mixed intelligence×motivation regulation, while compressing variance days reflect motivation-dominant regulation. We test this prediction on COGITO using [ctsem time-varying drift + asymmetric residual variance components / ergodic-subspace projection of motivation indicators]."

The frame: **predictive specificity** (variance direction → loop identity), not discovering motivation-cognition coupling.

---

## 10. Bottom line

- RIM-on-COGITO is **open ground** narrowly defined as asymmetry-as-identifier.
- The natural co-authors are Schmiedek (substantive COGITO depth) and Völkle (continuous-time methods).
- Wittmann brokers; do not approach Schmiedek/Völkle directly.
- Target Psychology and Aging or Multivariate Behavioral Research first.
- Risk: framed wrong, it reads as "Brose 2012 with extra steps." Framed right, it's a directional-asymmetry estimator that the existing mean-coupling literature cannot generate.
