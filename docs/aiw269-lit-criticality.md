<!-- AIW-269 half (b), criticality/states slice, S323 2026-09-28 subagent. OpenAlex rate-limited: coverage partial. Citations unverified by main loop. -->
# AIW-269 literature sweep: criticality, complexity, anaesthesia/sleep, altered states, DoC

Window: first published 2026-08-26 to 2026-09-28. Sources: OpenAlex (heavily rate-limited on 2026-09-28, so coverage is partial), Crossref, WebSearch, OSF API. Every item below was resolved by DOI through OpenAlex or Crossref, and its title, authors and date were confirmed. Summaries come from the abstracts; no full texts were read. Line numbers refer to `paper/full/four-model-theory-full.md` (v15).

**Bottom line: nothing in the window contradicts FMT outright. One item needs watching (the dream hot-zone replication, item 1). One item should be cited (psilocybin signal diversity, item 2). The rest are nice-to-have.**

---

## Criticality and edge-of-chaos dynamics

**1. Wu, G.-H. (2026).** *Replicability of EEG markers of dream experience: Non-replication of posterior hot-zone spectral decoding across multiple independent datasets and the sleep-stage gradient of white dreams.* OSF registration (Replication Recipe, post-completion), 2026-09-20. doi:10.17605/osf.io/vgehz
- **Claims:** This is a close replication of Siclari et al. (2017), testing the posterior hot-zone markers (1–4 Hz decrease, 30–40 Hz increase) on open 9–32-channel serial-awakening data such as DREAM Set13. It reports non-replication, but its own rule limits that null to coarse resolution: it "does not refute the original hdEEG finding". It also cites the earlier blinded Dream Catcher null (Wong et al., 2020).
- **Bears on:** l.767, "hot zone whose activation predicts the presence or absence of dream reports with high accuracy, independent of sleep stage", and Table 4, NREM row (l.686). It is filed here because it concerns sleep and dreaming.
- **Verdict: NICE-TO-HAVE now, and it becomes MUST-ANSWER if a peer-reviewed high-density non-replication appears.** It is a single author and not peer-reviewed. Consider softening "with high accuracy" to "in high-density EEG (Siclari et al., 2017; coarse-resolution replications have been mixed)". Related: Lei Wang's code record for the paper "Cross-dataset evaluation of a posterior delta EEG signature of reported dream experience" (Zenodo, 2026-09-06, doi:10.5281/zenodo.22311376). It holds code only; no results are visible and no paper has been found yet.

**2. Fontenele, A.J., Sooter, J.S., Ziarati, E., Barreiro, A.K., Ly, C., & Shew, W.L. (2026).** Critical brain dynamics may be more prevalent than previously thought. *Communications Physics*, online 2026-09-10. doi:10.1038/s42005-026-02833-y
- ⚠ **Window caveat:** the journal version falls inside the window, but the bioRxiv preprint (10.1101/2025.09.02.673722) dates from September 2025.
- **Claims:** Standard analyses can miss criticality ("hidden criticality"). A high-dimensional model separates non-critical dynamics, critical oscillations and scale-invariant avalanches into different subspaces, and the same hidden criticality is found in large-population recordings from mouse V1.
- **Bears on:** l.478, where DFA α is chosen partly to avoid "the distributional ambiguities that plague power-law fitting", and l.482, "criticality … not a single global" property. Both fit this result. It comes from the same group as Hengen & Shew (2025), which is already cited at l.467 and l.1338.
- **Verdict: MUST-CITE if the preprint date is acceptable; otherwise note it as the journal version of 2025 work.**

**3. Pathak, A., & Battaglia, D. (2026).** Arousal-driven critical roaming reproduces human functional connectivity dynamics. *PLoS Biology*, 2026-09-01. doi:10.1371/journal.pbio.3003916
- **Claims:** In a connectome model, slow arousal fluctuations in excitability, gain and noise make the system roam across regime boundaries near a critical point. This roaming, rather than a fixed near-critical tuning, reproduces the fat-tailed functional connectivity dynamics seen in humans.
- **Bears on:** l.482, which treats criticality as regional and time-varying, and l.472, which says slight subcriticality is the expected optimum. Both fit a dynamic, arousal-modulated operating point.
- **Verdict: NICE-TO-HAVE.** The preprint history was not checked.

**4. Hutt, A., McCulloch, M., Hudetz, A.G., Pariz, A., & Lefebvre, J. (2026).** Noise-like fluctuations drive shifts in neuronal timescales and 1/f power spectra across brain states. *PLOS Complex Systems*, 2026-09-25. doi:10.1371/journal.pcsy.0000133
- **Claims:** The 1/f^α scaling and spectral knee vary across states, arousal and drugs. In balanced random recurrent networks, that variability arises generically from state-dependent noise-like fluctuations that shift effective timescales.
- **Bears on:** l.476–478. It is a caution against reading aperiodic 1/f features as criticality markers. FMT's primary marker is DFA α, not 1/f slope, so this does not touch the commitment, but it supports keeping the two separate.
- **Verdict: NICE-TO-HAVE.**

**5. Galindez, N.F. (2026).** Debiased perturbational complexity peaks at the edge of chaos: reproducible response dimensionality in recurrent networks. Zenodo, 2026-09-01. doi:10.5281/zenodo.22100826. A companion record on PCIst selection bias is at doi:10.5281/zenodo.22226531.
- **Claims:** Across 366 recurrent networks, a debiased out-of-sample PCIst follows an inverted-U over the conditional Lyapunov exponent λ. It stays near floor in ordered networks, peaks in the edge band λ ∈ [−0.05, 0) and collapses in chaos.
- **Bears on:** l.480, "PCI is not a criticality measure. A system can have high PCI without being at criticality". In simulation, the two co-peak at the edge. That fits FMT treating PCI as a validated marker of the regime, but it slightly weakens how firmly l.480 separates them.
- **Verdict: NICE-TO-HAVE.** It is a single author, not peer-reviewed, and one of a many-version series.

**6. Huckenpahler, A.L., Luby, J.L., & Hoyniak, C.P. (2026).** Editorial: Criticality: a novel brain metric associated with sleep that may elucidate sleep's influence on adolescent depression. *J Child Psychol Psychiatry*, 2026-09-09. doi:10.1111/jcpp.70233
- **Claims:** Sleep restores a critical set point in adolescents. Depression may show up as a shifted set point, altered drift or failed reset.
- **Bears on:** l.1634 (Xu et al., 2024) and the sleep rows of Table 4.
- **Verdict: NICE-TO-HAVE.**

## Complexity measures

**7. Nikolič, M., Froese, T., Mediano, P.A.M., Koudelka, V., Horáček, J., Tylš, F., et al. (2026).** Psilocybin-induced changes in electroencephalography link acute and long-term effects. *J Psychopharmacology*, 2026-09-04. doi:10.1177/02698811261473445
- **Claims:** In a double-blind placebo crossover study (N=20, 0.26 mg/kg), psilocybin acutely raised gamma-band signal diversity at 1–3 h, back to baseline by 6 h. The rise correlated with acute psychological effects (r=0.71) and was largest in participants with low baseline complexity.
- **Bears on:** l.415, which quantifies permeability through entropy measures (Schartner et al., 2017), and Table 4, psychedelics "↑ Complexity" (l.689). Signal diversity tracking the dose-timed intensity of experience fits permeability as a graded quantity.
- **Verdict: MUST-CITE.** It is the newest controlled dataset for l.415.

**8. Kroupi, E., Araujo, H., Oosterveld, C., Timmermann, C.B., Rosas, F.E., Carhart-Harris, R.L., et al. (2026).** Higher signal diversity, network dysregulation, and increased well-being under DMT administration: An EEG study. *Brain Research*, 2026-09-07. doi:10.1016/j.brainres.2026.150530
- **Claims:** The title and metadata were verified; the abstract was not available through OpenAlex. The title reports higher signal diversity and network dysregulation under DMT, linked to well-being.
- **Bears on:** l.689 and l.726, which lists DMT among the psychedelics.
- **Verdict: NICE-TO-HAVE.** Read the abstract before citing.

**9. Li, M., Pan, J., Han, J., Bao, X., Wu, H., Wang, F., et al. (2026).** Detecting EEG index of arousal in sleeping patients with unresponsive wakefulness syndrome. *iScience*, 2026-09-24. doi:10.1016/j.isci.2026.117448
- **Claims:** Overnight polysomnography was recorded in UWS, MCS and control groups. Spectral slope indexes arousal across sleep stages in every group, while spectral entropy and Lempel-Ziv complexity index awareness and separate conscious from unconscious states.
- **Bears on:** Table 4, vegetative and MCS rows (l.690–692), and l.160, which gives complexity as the observable for consciousness. The arousal/awareness split fits FMT's separation of regime from simulation content.
- **Verdict: NICE-TO-HAVE.**

**10. Johnstone, C., & Alegaonkar, P.S. (2026).** Quantification of brain state into configuration entropy and complexity. *Consciousness and Cognition*, 2026-09-17. doi:10.1016/j.concog.2026.104132
- **Claims:** On open EEG datasets, configuration entropy, permutation entropy and Lempel-Ziv complexity are higher in full waking than in sleep, sedation or seizure.
- **Bears on:** l.486, the seizure as a negative control for extent without differentiation.
- **Verdict: NICE-TO-HAVE** (minor).

## Anaesthesia

**11. Fan, L., Wen, X., Lu, F., Wang, D., Chang, Y., Zhao, G., et al. (2026).** Local and interregional thalamocortical dynamics show temporally dissociable changes during propofol induced loss of consciousness. *NeuroImage*, 2026-09-14. doi:10.1016/j.neuroimage.2026.122235
- **Claims:** In sEEG recordings, permutation-entropy complexity in the anterior thalamic nucleus fell before loss of consciousness, and significantly earlier than in prefrontal and temporal cortex. Low-frequency power changes led high-frequency ones.
- **Bears on:** l.687, "Propofol: forced subcritical", and l.695, which says thalamocortical accounts "draw the same line". A staged, thalamus-first loss of complexity fits this. FMT makes no claim about ordering.
- **Verdict: NICE-TO-HAVE.**

**12. Kunze, J., Student, J., Tune, S., Oster, H., Schmidt, S., Ihmsen, H., et al. (2026).** Low-dose ketamine tilts the cortical excitation–inhibition balance irrespective of systemic physiological response. bioRxiv, 2026-09-21. doi:10.64898/2026.09.17.752361
- **Claims:** In a placebo-controlled crossover study (N=25), subanaesthetic ketamine flattened the aperiodic EEG exponent (toward excitation) and propofol steepened it. Cardiovascular effects did not explain the result.
- **Bears on:** l.687–688 and l.909, where propofol and ketamine push dynamics in opposite directions. The finding fits that pattern, but only at subanaesthetic doses and on an E:I proxy rather than a criticality measure (see item 4).
- **Verdict: NICE-TO-HAVE.**

**13. Kurz, E.-M., Hanert, A., Fudickar, A., Dittmar, M., Hoppe, F., Rave, J., et al. (2026).** Natural sleep, but not propofol-induced anesthesia preserves spatial and procedural memory consolidation. bioRxiv, 2026-09-11. doi:10.64898/2026.09.05.749587
- **Claims:** Spatial and procedural performance dropped after propofol anaesthesia (n=19) but stayed stable after a nap (n=17). Slow oscillations occurred in both conditions, but only in NREM sleep did they couple with spindles.
- **Bears on:** l.195 ("substrate processing … continues under anesthesia") and l.751 (the IWM "actively processing and learning" under propofol). This is not a contradiction: Katlowitz et al. show online encoding and plasticity, while Kurz et al. show that offline consolidation of prior learning is impaired.
- **Verdict: NICE-TO-HAVE.** Consider a scope clause at l.751 so a reviewer cannot set the two against each other.

**14. Lybbert, C., Garrett, C., Webb, T.D., Tsunoda, K., Begum, R., & Kubanek, J. (2026).** Focused ultrasound neuromodulation of the central lateral thalamus in a non-human primate model of disorders of consciousness. bioRxiv, 2026-09-21. doi:10.64898/2026.09.15.751608
- **Claims:** Bilateral focused-ultrasound stimulation of the central lateral thalamus was tested with controls in two macaques under propofol, used as a model of disorders of consciousness.
- **Bears on:** the thalamic gating account and the DoC rows of Table 4.
- **Verdict: NICE-TO-HAVE.**

## Altered states (NDE, time dilation)

**15. Taylor, S., Egeto-Szabo, K., & Wittmann, M. (2026).** Time Expansion Experiences: A survey and a qualitative study. *Timing & Time Perception*, 2026-09-17. doi:10.1163/22134468-bja10139
- **Claims:** 70% of 1,043 US respondents reported at least one experience of dramatically slowed time. Triggers were mostly accidents or emergencies (52%), then trauma (16%), then altered states (11%).
- **Bears on:** l.726, "altered time perception", and the temporal-echo account in §3.4.4.
- **Verdict: NICE-TO-HAVE.**

**16. Miller, M.M., Buck, Z., Zhu, A., & Holecek, A. (2026).** Consciousness at the edge of death: Dark retreat, near-death experience, and generative brain dynamics. PsyArXiv, 2026-09-18. doi:10.31234/osf.io/q7euc_v1
- **Claims:** An active-inference account treats NDEs and dark-retreat phenomenology as offline generative inference. It arises when sensory input is attenuated, action relevance collapses and autobiographical self-models lose precision.
- **Bears on:** §6.3 (l.763ff: the simulation running on attenuated input) and ESM redirection (l.267). It is a converging account in predictive-processing language, the alternative l.740 already concedes.
- **Verdict: NICE-TO-HAVE.**

## Disorders of consciousness

**17. Zhu, S., Xu, X., He, Q., Wang, N., Jia, Y., Wan, K., et al. (2026).** Topological integration and segregation of the conscious connectome as biomarkers for state, behavior, and prognosis. *Communications Medicine*, 2026-09-10. doi:10.1038/s43856-026-01870-6
- **Claims:** In resting-state fMRI (117 DoC patients, 30 controls), disrupted integration and segregation track CRS-R scores and predict long-term outcome.
- **Bears on:** l.484, the integration–differentiation tradeoff (extent vs complexity), which FMT expressly does not claim priority over.
- **Verdict: NICE-TO-HAVE.**

## Nothing found (in window, verifiable)

- **Branching ratio σ and avalanches in humans or anaesthesia:** no new empirical estimates. Only model and tool papers turned up (e.g. pyAvalanches, arXiv 2609.11530).
- **Critical slowing at loss of consciousness, or Lyapunov estimates in human EEG:** none.
- **New clinical PCI studies:** none verified. Only the Zenodo simulation work (item 5) and the eLife *State-dependent brain responsiveness* review, whose v2 assessment is dated 2026-09-21 but whose v1 predates the window.
- **Dreaming under anaesthesia, and new serial-awakening primary data:** none beyond item 1.
- **Lucid-dream criticality (Prediction 4, l.955):** none.
- **Salvia, salvinorin A, identity-content tracking (Prediction 2):** none.
- **Dissociatives beyond item 12:** none.
- **Acute 5-MeO-DMT:** none. Only a post-acute EEG connectivity study (West et al., bioRxiv 2026-08-27, doi:10.64898/2026.08.23.746502), which is not relevant to the FMT claims.

**Out-of-window flag for the owner:** a search surfaced arXiv 2604.21071, *A Critical Assessment of the Brain Criticality Hypothesis* (April 2026). It is not verified here and falls outside this window. Check whether v15 already answers it, because the title reads as a potential MUST-ANSWER for §3.7.
