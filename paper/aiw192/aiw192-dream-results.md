---
title: "Experience without recall does not give way steeply to no-experience reports as slow-wave activity rises within a person: results of a preregistered reanalysis of the DREAM database"
---

**Matthias Gruber**^a^

^a^ Independent researcher, Vorarlberg, Austria

Corresponding author: Matthias Gruber, research@matthiasgruber.com. ORCID 0009-0005-9697-1665.

Article type: Results of a preregistered secondary data analysis

## Abstract

After an awakening from NREM sleep, a sleeper sometimes reports having experienced something without being able to say what: experience without recall (EWR). A preregistered test asked whether EWR gives way to reports of no experience (NE) as sleep deepens within a person, with relative slow-wave activity (SWA) in the 30 s before each awakening as the depth index. A floor account, on which experience itself fades with depth, predicts a steep decline of EWR against NE; a consolidation account, on which depth impairs the recording of experience more than the experience, allows at most a gentle one. The registered decision rule placed a margin of −0.6 logit per standard deviation on that slope. The analysis code was deposited before any EEG signal was read. In 756 NREM awakenings from 107 participants in five open datasets of the DREAM database, the slope was +0.03 logit per SD (95 % highest-density interval −0.26 to +0.33), entirely above the margin, so the registered verdict is that EWR survives depth. All thirteen registered robustness analyses agreed, among them leaving out the dataset that supplies most N3 awakenings, and adding time of night left the slope unchanged. Within-person SWA moved none of the three report categories credibly, including the loss of content that both accounts predict, which limits the result to excluding a steep within-person decline. In exploratory deciles of SWA standardised within each dataset, which mix depth with differences between participants and stages, reports thinned at the highest SWA and EWR fell from 0.47 to 0.26 of EWR-or-NE awakenings, the direction a floor account expects. The derived tables, model outputs and code are open.

**Keywords:** sleep; dreaming; experience without recall; white dreams; slow-wave activity; NREM; preregistration; DREAM database

## 1. Question

Serial-awakening studies sort what sleepers report into three categories: an experience with recallable content (E), an experience whose content cannot be recalled (EWR, sometimes called a white dream), and no experience (NE) (Siclari et al., 2017). EWR is common in deep sleep. In the sample analysed here, 48 of the 218 awakenings from N3 were EWR and 89 were NE.

What EWR does as sleep deepens separates two accounts. On a floor account, experience itself fades with depth, so deeper sleep leaves less to have an impression of; EWR gives way to NE and falls away at the deepest sleep. On a consolidation account, depth impairs the writing of experience to memory more than it impairs the experience, and the impression of having experienced survives depth better than its content; EWR then declines at most gently against NE. The two accounts differ in the steepness of the EWR-versus-NE gradient over depth, which is what the registered test measures. Sleep stage is a coarse depth index and partly study-specific, and a stage-by-category analysis of DREAM already exists (Stucky, 2025). The test therefore used SWA before each awakening, compared within each participant and stage.

The consolidation account, as registered, is a conjecture within the Four-Model Theory (Gruber, 2026a). It joins that theory's claim that the explicit models write back into the substrate through consolidation with an auxiliary premise the registration states: that the impression of having experienced outlasts its content as depth rises. The theory's architecture does not fix the gradient by itself. On its account, that a sleeper can be woken means that external input can instantiate the explicit models. In deep sleep they may be absent, instantiated too weakly to close, closed so that something is experienced but without the write-back that would leave a memory, or running weakly and leaving a trace whose content may be too indistinct to report. E and EWR come from the last state, EWR where the content is lost; NE pools the first three, which no report can separate. That ladder is compatible with either verdict, and the test bears on how the reportable trace degrades with depth.

## 2. Methods

The registration (Gruber, 2026b; OSF Registries, Secondary Data Preregistration, filed 2026-11-08 and still under embargo when this report was deposited; the registered text is included in this record) governs every choice summarised below.

### 2.1 Freezing the pipeline

The feature and model code (Python 3.12, NumPy 2.5, SciPy 1.18; R 4.3.3, MCMCglmm 2.36, lme4 1.1-35.1) was written test-first on synthetic EDF files and simulated awakenings, reviewed twice against the registration, and deposited on Zenodo with its commit hash before any EEG signal was read (Gruber, 2026c; commit 2f30cc2b, published 2026-11-08 20:57:15 UTC). The feature script reads no EEG unless it is given that deposit's DOI, the deposited commit and the deposit's manifest, which lists a SHA-256 for every file and for the registered text; its own directory must be identical to the deposited commit. The run used a later commit (f6122965) whose code directory is identical to the deposited one. EEG signal was first read at 20:57:32 UTC. Before the deposit, the feature script ran once in a header-only mode (channel labels, units and sampling rates, which the registration declares as read) and found a readable registered channel in all 920 selected records of the six open sets. The registration defines the first EEG read as the first execution of the feature script on any DREAM record, so this pass, which read no signal, departs from that definition.

### 2.2 Data

The data are the open datasets of the DREAM database (Wong et al., 2025a; metadata release of 2025-10-30, Wong et al., 2025b; CC BY 4.0), downloaded on 2026-11-08 and checked against figshare's md5 sums. The primary datasets are those with provoked awakenings whose native scheme separates EWR from NE: Set 2 (daytime naps), Set 13 (Siclari et al., 2017), Set 16 (Wong et al., 2020), and Sets 17 and 18 (evening and morning sleep). Set 3, with spontaneous awakenings, enters one robustness analysis, for which 67 of its 120 awakenings (32 E, 8 EWR, 27 NE) had fewer than 7 clean segments on its registered channel, Fp1-O1. Records were selected as registered: one row per set and file at the highest amendment, healthy participants, last stage N2 or N3, category E, EWR or NE. The registration expected 767 awakenings from 107 participants. Eleven were excluded for unusable EEG, all from Sets 17 and 18 (6 E, 3 EWR, 2 NE): ten with fewer than 7 of 14 clean 4-s segments and one shorter than 32 s. The primary model therefore used 756 awakenings from 107 participants (Table 1). Participant identifiers were nested within datasets; Sets 17 and 18 were treated as distinct samples, as registered.

**Table 1.** Primary sample by dataset, stage and report category (E / EWR / NE).

| Set | Participants | N2 | N3 | Awakenings | Excluded (EEG) |
|---|---|---|---|---|---|
| 2 | 17 | 12 / 7 / 4 | – | 23 | 0 |
| 13 | 39 | 124 / 56 / 107 | – | 287 | 0 |
| 16 | 10 | 24 / 26 / 25 | 46 / 36 / 87 | 244 | 0 |
| 17 | 25 | 68 / 13 / 10 | 28 / 8 / 2 | 129 | 10 |
| 18 | 16 | 43 / 9 / 10 | 7 / 4 / 0 | 73 | 1 |
| All | 107 | 271 / 111 / 156 | 81 / 48 / 89 | 756 | 11 |

### 2.3 Depth index

The analysis window ends at the last sample before a trailing run of constant signal of at least 1 s, or at the end of the file, and spans 30 s up to 2 s before that end. On one registered channel per dataset (Set 2 C3-A2; Set 13 electrode E21 of the HydroCel 256 net, at the Fz position; Set 16 Fz; Sets 17 and 18 Cz-Ref), the window was cut into 14 detrended 4-s segments with 50 % overlap, segments with a peak-to-peak amplitude above 500 µV or a standard deviation below 0.5 µV were dropped, and a Welch spectrum was formed from the rest. SWA is the log of the power in bins centred in 0.5–4 Hz over the power in 0.5–30 Hz. Within each dataset SWA was standardised (z); SWA_between is the participant-by-stage mean of z, and SWA_within is the deviation from it, rescaled to unit SD within the dataset. Centring by participant and stage means that the depth axis of the test is the variation of SWA within one person in one stage.

### 2.4 Model and decision rule

The primary model is a categorical MCMCglmm model (Hadfield, 2010), the family used by the DREAM authors (Wong, 2025), with NE as reference: trait-specific intercepts per stage, slopes on SWA_within and SWA_between, random intercepts for dataset and participant, and an uncorrelated participant random slope on SWA_within; residual covariance fixed. Four chains of 1,000,000 iterations (burn-in 100,000, thinning 20) were pooled. Fixed effects were divided by $\sqrt{1 + c^2}$, $c = 16\sqrt{3}/(15\pi)$, to put them on the logit scale. The decision rests on the 95 % highest-density interval (HDI) of the EWR-versus-NE slope on SWA_within: entirely above −0.6, EWR survives depth as the consolidation account requires; entirely below −0.6, it declines faster than that account allows; otherwise the verdict is inconclusive. The margin is under half of the slope (about −1.3) at which EWR would fall below 5 % of EWR-or-NE awakenings in the top N3 decile. In the registered design analysis, a true slope of −1.2 gave the verdict "falls away" in 95 % of simulated samples and a true slope of 0 gave "survives" in 99 %.

Registered robustness analyses: (a) each dataset left out in turn; (b) N2 only; (c) SWA over 0.5–2 Hz; (d) a 20-s window; (e) Set 3 added; (f) Set 16's merged "no experience or without recall" awakenings recoded as NE; (g) parameter-expanded variance priors; (h) a binomial lme4 model of EWR versus NE (Bates et al., 2015); (i) the primary model without the random slope. None of them can overturn the primary verdict.

### 2.5 Exploratory additions fixed before the freeze

Four additions were written into the code after the two pre-freeze reviews and before any EEG was read; they decide nothing. (1) Time of night: SWA also falls across the night, so a within-person slope can carry time of night. The clock time of each awakening (in Set 16, which has no clock times, the awakening's number within the night) was centred like SWA, and the primary model was refitted with it as an added term. (2) The posterior probabilities P(slope > 0) and P(slope < −0.6). A slope above zero, EWR rising against NE with depth, would be the signature of EWR used as a "don't know" answer under sleep inertia. (3) Report shares per within-dataset decile of SWA_within and of z. (4) The model's probabilities of NE, EWR and E per decile, per posterior draw.

### 2.6 Execution notes and additions to the registered text

Run 1 completed feature extraction and table preparation and then failed in all model fits on the computing environment: the R library holding MCMCglmm was not on the library path of the background job. It was relaunched unchanged with the path set. Run 2's feature table is byte-identical to that of run 1, and its outputs are the ones reported. The lme4 check (h) includes stage and SWA_between as fixed effects in addition to the registered terms. Operational details the registration leaves open (among them channel label strings, the handling of a blank unit field, the length test after the constant tail is removed, the spectral estimator's segment averaging, centring each analysis over its own awakenings, and taking the registered top SWA decile on SWA_within) were fixed in code before the freeze and are listed in the code deposit's README. Twenty-seven awakenings are the only awakening of their participant in their stage, so their SWA_within is zero, and 18 participants contribute no within-person variation. The registered replication on the restricted SCAN dataset (Set 8) awaits data access.

## 3. Results

### 3.1 Primary test

The primary model converged at the first step of the registered ladder (largest R-hat 1.0001; smallest effective sample size 33,165). The EWR-versus-NE slope on SWA_within was +0.03 logit per SD (95 % HDI −0.26 to +0.33). The interval lies entirely above −0.6, so the registered verdict is that EWR survives depth. P(slope > 0) was 0.59 and P(slope < −0.6) below 0.001.

Of the quantities registered as reported, the EWR-versus-E slope was +0.16 (−0.18 to +0.50) and the NE-versus-E slope +0.12 (−0.15 to +0.39); neither interval excludes zero, so within-person SWA did not credibly shift reports from content toward EWR or toward NE. In the top within-person decile of SWA (78 awakenings), the model's probability of EWR was 0.28 (0.23 to 0.35); Table 2 gives it per dataset. That value lies above the model's values in deciles 1 to 9 (0.19 to 0.22) and above the observed EWR share in the top decile (19 of 78, 0.24), while the observed shares in deciles 1 to 10 range from 0.15 to 0.25 without a trend (Figure 1A). The model-free share EWR/(EWR + NE) in that decile was 19 of 45, 0.42 (Clopper–Pearson 95 % interval 0.28 to 0.58), against 0.42 in N2 and 0.35 in N3 over the whole sample.

**Table 2.** Registered top-decile quantities per dataset.

| Set | Top-decile awakenings | Model P(EWR) [95 % HDI] | EWR / (EWR + NE) [Clopper–Pearson 95 %] |
|--------------|----------|--------------------|--------------------------|
| 2 | 3 | 0.23 [0.04, 0.49] | 0 of 2 [0.00, 0.84] |
| 13 | 29 | 0.25 [0.16, 0.35] | 6 of 19, 0.32 [0.13, 0.57] |
| 16 | 25 | 0.34 [0.25, 0.43] | 10 of 19, 0.53 [0.29, 0.76] |
| 17 | 13 | 0.22 [0.11, 0.35] | 2 of 3 [0.09, 0.99] |
| 18 | 8 | 0.25 [0.10, 0.40] | 1 of 2 [0.01, 0.99] |
| All | 78 | 0.28 [0.23, 0.35] | 19 of 45, 0.42 [0.28, 0.58] |
| All, top decile of z (exploratory) | 78 | 0.16 [0.11, 0.20] | 11 of 42, 0.26 [0.14, 0.42] |

### 3.2 Robustness

The twelve MCMC robustness analyses converged at the first step of the ladder (smallest effective sample size 10,361, without Set 16), and all thirteen returned the same verdict (Table 3). The slope ranged from −0.09 (without Set 13) to +0.12 (N2 only). Without Set 16, which supplies 169 of the 218 N3 awakenings from ten participants, it was +0.09 (−0.27 to +0.46). The lme4 check dropped the random slope as singular, as registered, and gave −0.01 (−0.25 to +0.23).

**Table 3.** EWR-versus-NE slope on within-person SWA, logit per SD, in every analysis. Sample: awakenings / participants; P(> 0): posterior probability that the slope is positive.

| Analysis | Sample | Slope, median [95 % HDI] | P(> 0) | Verdict |
|--------------------------------|-----------|---------------------------|-------------|--------------|
| Primary model | 756 / 107 | +0.03 [−0.26, +0.33] | 0.59 | survives |
| (a) without Set 2 | 733 / 90 | +0.08 [−0.22, +0.37] | 0.69 | survives |
| (a) without Set 13 | 469 / 68 | −0.09 [−0.50, +0.32] | 0.33 | survives |
| (a) without Set 16 | 512 / 97 | +0.09 [−0.27, +0.46] | 0.69 | survives |
| (a) without Set 17 | 627 / 82 | −0.03 [−0.35, +0.29] | 0.42 | survives |
| (a) without Set 18 | 683 / 91 | +0.08 [−0.22, +0.40] | 0.70 | survives |
| (b) N2 only | 538 / 106 | +0.12 [−0.22, +0.47] | 0.76 | survives |
| (c) SWA 0.5–2 Hz | 756 / 107 | 0.00 [−0.29, +0.29] | 0.49 | survives |
| (d) 20-s window | 756 / 107 | +0.07 [−0.23, +0.36] | 0.68 | survives |
| (e) Set 3 added | 809 / 126 | +0.04 [−0.25, +0.32] | 0.60 | survives |
| (f) Set 16 merged category as NE | 789 / 107 | 0.00 [−0.28, +0.29] | 0.51 | survives |
| (g) parameter-expanded priors | 756 / 107 | +0.03 [−0.19, +0.26] | 0.60 | survives |
| (h) lme4, EWR versus NE | 404 / 83 | −0.01 [−0.25, +0.23]^a^ | – | survives |
| (i) no participant random slope | 756 / 107 | +0.03 [−0.19, +0.24] | 0.61 | survives |
| Time of night added (exploratory) | 756 / 107 | +0.03 [−0.26, +0.33] | 0.59 | (survives) |

^a^ Maximum-likelihood estimate with a Wald 95 % interval; EWR and NE awakenings only.

### 3.3 Exploratory results

**Time of night.** Within participants, SWA_within correlated with time of night at Spearman $\rho$ = −0.21 in Set 13, +0.22 in Set 16, +0.31 in Set 17, +0.20 in Set 18 and −0.10 in Set 2. With time of night in the model, the EWR-versus-NE slope on SWA_within was unchanged at +0.03 (−0.26 to +0.33), and the time coefficients, in logit per SD against NE, were near zero (EWR −0.03, −0.26 to +0.19; E −0.06, −0.25 to +0.14).

**Sign.** A positive slope, EWR rising against NE with depth, is what EWR used as a default answer under sleep inertia would produce. Across the thirteen MCMC analyses and the time-adjusted refit, P(slope > 0) ranged from 0.33 to 0.76, and every 95 % interval included zero.

**Deciles.** Figure 1 shows the report categories across deciles. On the registered axis (panel A) the shares are flat: the share of awakenings with any report of experience (E or EWR) stays between 0.62 and 0.74, and EWR/(EWR + NE) between 0.31 and 0.49, with no trend. On standardised SWA, which also carries the differences between participants and between stages (panel B), reports thin toward the top: the share of reports of experience falls from 0.76 in the lowest decile to 0.60 in the highest, EWR/(EWR + NE) from 0.47 to 0.26, and the model's probability of NE rises from 0.25 (0.19 to 0.33) to 0.40 (0.34 to 0.45). In Set 16, 1 of the 19 EWR-or-NE awakenings in the top decile of standardised SWA was EWR, against 10 of 19 in its top decile of within-person SWA, and the primary model's EWR-versus-NE slope on SWA_between was −0.21 (−0.71 to +0.31). These deciles mix depth with who was recorded and in which stage, and no test is attached to them.

![](paper/aiw192/figure1.pdf){width=100%}

**Figure 1.** Report category across deciles of slow-wave activity in the 30 s before awakening (756 awakenings, 107 participants; deciles formed within each dataset and pooled). Lines and bands: the primary model's probability of each category, posterior median and 95 % HDI, using each awakening's own covariates and participant effects. Markers: observed shares. (A) SWA within participant and stage, the registered depth axis. (B) SWA standardised within dataset, which also carries the differences between participants and stages. Exploratory.

## 4. Discussion

On the registered axis, within-person SWA within a stage, experience without recall did not give way to reports of no experience: the slope sat near zero, with an interval excluding the steep decline the floor account predicts, and every robustness analysis agreed. A true slope of −1.2 produced the opposite verdict in 95 % of the registered design simulations.

Within-person SWA moved no report category credibly, the shift from content to EWR that both accounts predict included. Variation in SWA within one person and one stage, over the 30 s before an awakening, is therefore a weak lever on what the sleeper reports, and the result excludes a steep decline along that lever. Where slow waves were boosted causally, reports did move: closed-loop acoustic stimulation in N3 shifted reports from content toward both EWR and NE, leaving EWR the most frequent category (15 of 36 reports, against 9 of 33 under sham, with 13 sleepers per arm; Juan et al., 2023). Centring by stage removes the step from N2 to N3, and the deepest sleep in the sample comes from one dataset with ten participants. On the axis that keeps those differences, standardised SWA, reports thinned at the top and EWR lost ground to NE, the direction a floor account expects. Those deciles confound depth with participant and stage, so they mark where a design with more within-person deep sleep should look.

Two rival readings of a surviving EWR remain open. EWR could reflect failed retrieval at awakening rather than failed recording during sleep; public awakening data cannot separate the two, which needs a retrieval manipulation such as delayed or cued re-interview. EWR could also be a default answer under sleep inertia; that reading predicts EWR rising against NE with depth, and the probability of a rise ranged from 0.33 to 0.76 across the analyses. The registered channels are frontal or central, while the low-frequency marker that separated EWR from NE in Set 13's original analysis was posterior (Siclari et al., 2017). A retrospective registration that tested that marker on open data reduced to 9–32 standard channels reports non-replication, which its author restricts to the lower resolution, and treats EWR as a graded target across sleep stages (Wu, 2026).

On the Four-Model Theory's ladder (Section 1), E and EWR mark running explicit models, and the share of awakenings carrying such a trace stayed between 0.62 and 0.74 across within-person deciles of SWA. Whether anything was experienced before an NE awakening is beyond any awakening report: on the theory, only a record of the explicit models themselves could show their absence. Depth measured as arousal threshold, the variable the floor account concerns, is recorded in no public dream dataset. The next step on these data is the registered replication on SCAN (Set 8), analysed with the frozen pipeline as a separate sample once access is granted.

## Data and code availability

This record contains, under CC BY 4.0, the registered text as filed on OSF, the derived per-awakening feature table, every model input table, the model outputs of all fifteen analyses (posterior summaries, convergence diagnostics, decile tables and logs), the metadata and log of run 1, and the script that draws Figure 1. The analysis code is in the code deposit (Gruber, 2026c), with the design-analysis script. The EEG and reports are the DREAM authors' open data (Wong et al., 2025a, 2025b). Posterior draws are kept by the author and are available on request.

## Declaration of competing interest

The author declares no competing interests.

## Funding

None.

## Declaration of generative AI and AI-assisted technologies in the research and manuscript preparation process

The question, the hypothesis, the decision rule and the reading of the results are the author's. During the preparation of this work the author used Claude (Anthropic), a large language model, to implement and test the analysis code against the registered specification, to run the registered analyses, to draft the text and to check references. After using this tool, the author reviewed and edited the content as needed and takes full responsibility for the content of this record.

## References

Bates, D., Mächler, M., Bolker, B., & Walker, S. (2015). Fitting linear mixed-effects models using lme4. *Journal of Statistical Software*, *67*(1), 1–48. https://doi.org/10.18637/jss.v067.i01

Gruber, M. (2026a). *The Four-Model Theory of Consciousness: A simulation-based framework unifying the Hard Problem, binding, and altered states*. Zenodo. https://doi.org/10.5281/zenodo.18669891

Gruber, M. (2026b). *Does experience without recall survive deeper NREM sleep? A preregistered reanalysis of the DREAM database with slow-wave activity as a within-person depth index* [Secondary data preregistration]. OSF Registries. https://osf.io/m4vju

Gruber, M. (2026c). *Analysis pipeline for a preregistered reanalysis of the DREAM database (OSF m4vju)* [Software]. Zenodo. https://doi.org/10.5281/zenodo.24060863

Hadfield, J. D. (2010). MCMC methods for multi-response generalized linear mixed models: The MCMCglmm R package. *Journal of Statistical Software*, *33*(2), 1–22. https://doi.org/10.18637/jss.v033.i02

Juan, E., Arslan, C., Regnath, F., & Talamini, L. M. (2023). *Boosting sleep slow waves suppresses dreaming* [Preprint]. bioRxiv. https://doi.org/10.1101/2023.03.10.532054

Siclari, F., Baird, B., Perogamvros, L., Bernardi, G., LaRocque, J. J., Riedner, B., Boly, M., Postle, B. R., & Tononi, G. (2017). The neural correlates of dreaming. *Nature Neuroscience*, *20*(6), 872–878. https://doi.org/10.1038/nn.4545

Stucky, B. (2025). We are the sensors of consciousness! A review and analysis on how awakenings during sleep influence dream recall. *Nature and Science of Sleep*, *17*, 709–729. https://doi.org/10.2147/NSS.S506461

Wong, W. (2025). *DREAM generalised linear mixed-effect modelling* [Software]. Monash University. https://doi.org/10.26180/29124026

Wong, W., Noreika, V., Móró, L., Revonsuo, A., Windt, J., Valli, K., & Tsuchiya, N. (2020). The Dream Catcher experiment: Blinded analyses failed to detect markers of dreaming consciousness in EEG spectral power. *Neuroscience of Consciousness*, *2020*(1), niaa006. https://doi.org/10.1093/nc/niaa006

Wong, W., Herzog, R., Andrade, K. C., Andrillon, T., et al. (2025a). A dream EEG and mentation database. *Nature Communications*, *16*, 7495. https://doi.org/10.1038/s41467-025-61945-1

Wong, W., Andrillon, T., Decat, N., Herzog, R., Noreika, V., Valli, K., Windt, J., & Tsuchiya, N. (2025b). *The DREAM database* [Data set, metadata release of 2025-10-30]. Monash University. https://doi.org/10.26180/22133105.v9

Wu, G.-H. (2026). *Replicability of EEG markers of dream experience: Non-replication of posterior hot-zone spectral decoding across multiple independent datasets and the sleep-stage gradient of white dreams* [Replication study registration]. OSF Registries. https://doi.org/10.17605/osf.io/vgehz
