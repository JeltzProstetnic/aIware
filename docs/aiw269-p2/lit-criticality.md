<!-- AIW-269 pass 2 (2026-02-17→08-25), criticality slice, S323 subagent. OpenAlex budget exhausted mid-run: dreaming/NDE/psychedelic-time/DoC partial. -->
<!-- AIW-269 pass 2, criticality/states slice, window 2026-02-17 to 2026-08-25. Subagent, S323, 2026-09-28. -->
# AIW-269 pass 2: criticality, complexity, anaesthesia/sleep, altered states, DoC (2026-02-17 to 2026-08-25)

**Sources.** OpenAlex was used for about 8 queries before its shared daily budget ran out (the error was "Insufficient budget … $0 remaining; resets at midnight UTC"). After that I used Crossref, PubMed eutils, the bioRxiv API, arXiv and WebSearch.

**Coverage gap:** OpenAlex relevance sweeps for dreaming/NDE/psychedelic time and for DoC criticality did not run, and Crossref plus web search only partly cover them.

**Verification.** Every item was resolved by its DOI or ID. Summaries come from abstracts unless marked otherwise. Line numbers refer to `paper/full/four-model-theory-full.md`. None of the first authors below appears in its reference list. Items already in `docs/aiw269-lit-criticality.md` (08-26 onwards) are not repeated.

**Bottom line:** Sipling et al. is a published opinion piece, and it needs a one-paragraph answer in §3.7, drafted below. Two items should be cited:
- Selte et al., a large hdEEG replication of the NREM hot zone. It neutralises the pass-1 Wu non-replication.
- Newman, Maschke et al., which extends criticality→PCI to DoC.

Nothing in the window refutes an FMT claim.

---

## A. arXiv 2604.21071: Sipling, Zhang & Di Ventra, "A Critical Assessment of the Brain Criticality Hypothesis"

**Verified.** arXiv v1 2026-04-22, v2 05-07, v3 05-29 (physics.bio-ph). It was **published** as Sipling, C., Zhang, Y.-H., & Di Ventra, M. (2026), *Trends Open*, online 2026-06-30, doi:10.1016/j.treopn.2026.06.001. The authors call it "an opinion paper". Its model basis is Sun et al. (2025), *PRE* 112:064401, and Sipling et al. (2025), *PRE* 112:014124.

**What it argues** (from the v3 full text):
1. **Scale invariance is necessary but not sufficient for criticality.** Avalanche power laws, the crackling-noise scaling relation and even −3/2 exponents occur in non-critical systems. The exponents also depend on bin size and threshold, and on subsampling (Priesemann 2009).
2. **No-one has shown that a critical point exists** in neural parameter space. That would take an RG analysis or a phase diagram.
3. **Information-processing benefits need only power-law correlations,** not a critical point.
4. **The alternative is MILRO (memory-induced long-range order).** Fast activity coupled to slow resources (ATP, vesicle pools, ion gradients, on timescales τ_D) produces an *extended phase* in which power laws and long-range temporal correlations hold across a wide parameter range (25 ≲ τ_D ≲ 82 in the model), with no fine-tuning.
   - The phase has boundaries: "regions of minimal (τ_D ≲ 25) and perpetual (τ_D ≳ 82) activity … where the correlation length shrinks significantly."
   - The paper does not discuss DFA, branching-ratio values, Griffiths phases, anaesthesia or consciousness.
   - Its proposed test is to titrate 2-DG and slow ATP production, then check whether scale invariance persists.

**FMT sentences it hits:**
- l.455: "empirical neuroscience has converged on the same conclusion", and l.467/470: Hengen & Shew "confirms criticality"; "confirmed the near-criticality setpoint". Point 2 goes directly at "confirmed".
- l.472: "The brain sits as close to criticality as stability permits — the operating point is tuned, not accidental." MILRO says no tuning is needed.
- l.476: the three signatures "converge on the same characterization", and the avalanche exponent of −3/2 is treated as "the hallmark of scale-free dynamics". Point 1 says that convergence is also expected in a non-critical MILRO phase. So the "convergence as false-positive guard" argument (l.476, end) is weaker than stated: σ, α and avalanches are not independent tests if one non-critical mechanism produces all three.
- Table 3 row 2025, "confirms criticality".

**What it does *not* hit.** FMT's requirement is Class 4 *capability* (open-ended computation), and near-criticality is only its "signature" (l.439–441). FMT's necessity claim also needs only a *regime with boundaries*: loss of consciousness is exit from it, in either direction (l.472, l.486). MILRO is exactly such a regime, with an ordered or quiescent edge and a runaway or perpetual edge. The Di Ventra group's own memcomputing programme argues that memory-driven long-range order is what makes computation efficient, so MILRO is a candidate *mechanism* for FMT's Class 4 capability, not a rival to it. Two counter-data points exist in window:
- Janbon et al. (2026; item 5 below) found critical exponents only at balanced E/I, with faster-decaying avalanches otherwise.
- Munn et al. (2026; item 6) identified an explicit control parameter (arousal) that tunes across a directed-percolation transition.

**Verdict: MUST-ANSWER** (peer-reviewed venue; it is a direct attack on the premise).

**Proposed paragraph** (for §3.7, after the Touboul & Destexhe caveat at l.476):

> A stronger version of this caveat has recently been pressed: scale-free avalanches, their scaling relations and long-range temporal correlations may arise across an extended phase of "memory-induced long-range order", produced by coupling fast activity to slowly recovering metabolic resources, without any critical point (Sipling, Zhang, & Di Ventra, 2026). If that is right, the three signatures are not independent witnesses to a critical point, and "criticality" in the strict phase-transition sense has not been demonstrated in cortex. The theory can concede this without cost, because its commitment was never to a point. Principle 1 requires a Class 4 regime, meaning dynamics rich enough for open-ended modeling and ordered enough to stay coherent, and it names near-criticality only as that regime's biological signature. An extended long-range-ordered phase, bounded by quiescent dynamics on one side and perpetual runaway activity on the other, is such a regime. On this reading the necessity claim becomes: absent the long-range-ordered regime, whether critical point or extended phase, no consciousness. That claim remains testable. It predicts that manipulations which drive the regime markers out of that phase (propofol, deep NREM, generalized seizure) abolish experience, and that manipulations which merely shift the phase's internal parameters (the metabolic titration Sipling et al. propose) should not, as long as the markers persist. Where the theory has said "criticality" it should be read as this regime, and the stronger phrasing that the operating point is "tuned" should be treated as one of two live mechanisms rather than as settled (compare Munn et al., 2026, on arousal as a control parameter).

**Accompanying edits:** l.467 and l.470 "confirms/confirmed" → "consolidates evidence for". At l.472, add "on the critical-point reading" before "tuned, not accidental". At the end of l.476, add one clause saying the convergence guard presupposes that the signatures have partly independent generators, which Sipling et al. dispute. The references to add are Sipling 2026 and optionally Sun 2025.

---

## B. Other items

### Criticality

**1. Newman, D., Maschke, C., O'Byrne, J., Colombo, M., … Rosanova, M., et al. (2026).** Critical dynamics in spontaneous EEG predict perturbational complexity in disorders of consciousness with measurable evoked responses. bioRxiv, 2026-06-09. doi:10.64898/2026.06.04.730221
- **Claims:** In 26 DoC patients, resting-EEG criticality features did not predict PCImax across the whole cohort. They did predict it in non-anoxic patients and in patients with non-zero PCI.
- **Bears on:** l.480, "PCI … which the theory predicts will co-vary with the criticality measures", and Table 4, vegetative/MCS. It supports the claim with a scope limit: anoxic injury breaks the link.
- **Verdict: MUST-CITE** (with the anoxic caveat).

**2. van Lutterveld, R., Cahaly, T., van Herk, L., Ingram, D.M., & Sacchet, M.D. (2026).** Brain criticality and advanced meditation "cessation" events: an intensively sampled EEG case study. *IBRO Neurosci Rep* 21:375–385, online 2026-07-25. doi:10.1016/j.ibneur.2026.07.011
- **Claims:** 37 cessations (loss of consciousness) were recorded in one meditator. Whole-brain DFA α rose before cessation, briefly dipped at onset, then peaked near-critical or supercritical 1–3 s after it. Some frontal channels were supercritical.
- **Bears on:** l.478, DFA α as the primary measure, and l.441, where the converse does not follow. Unconsciousness alongside near- or supercritical α is accommodated by the one-directional claim and by the supercritical exit route at l.486, but it shows α alone does not index state.
- **Verdict: NICE-TO-HAVE** (n=1). A reviewer could still raise it.

**3. Myrov, V.O., … Palva, S., & Palva, J.M. (2026).** Hierarchical whole-brain modeling of critical synchronization dynamics in the human brain. *PNAS*, 2026-03-17. doi:10.1073/pnas.2505768123
- **Claims:** A two-level Kuramoto model produces long-range temporal correlations (LRTCs) that peak at the synchronization transition. Human MEG fits the model best near that transition.
- **Bears on:** l.476–478 (LRTC/DFA as a criticality signature).
- **Verdict: NICE-TO-HAVE.**

**4. Chang, H., … Oliva, A. (2026).** Dynamic shifts in brain criticality support cognitive processing. bioRxiv, 2026-03-14. doi:10.64898/2026.03.12.711394
- **Claims:** Rodent hippocampus operates near criticality during learning and shifts subcritical during sleep replay. It recovers through CCK-interneuron inhibition.
- **Bears on:** l.441 (unconscious modeling in sleep) and Table 4 NREM, "Predominantly subcritical". The unconscious replay is subcritical, which is compatible.
- **Verdict: NICE-TO-HAVE.**

**5. Janbon, M., … Ponce-Alvarez, A. (2026).** Critical neuronal avalanches arise from excitation-inhibition balanced spontaneous activity. *iScience*, online 2026-08-14. doi:10.1016/j.isci.2026.117212
- **Claims:** In zebrafish tectum, avalanche critical exponents appear only at balanced or slightly excitatory E/I. Imbalance gives faster-decaying avalanches.
- **Bears on:** l.472, where the operating point is tuned. It is the counter-datum to Sipling's "wide phase".
- **Verdict: NICE-TO-HAVE** (use it in the §A answer).

**6. Munn, B.R., Whyte, C.J., Müller, E.J., & Shine, J.M. (2026).** Arousal tunes neuronal avalanches across a directed percolation critical point. *Phys Rev E* 114:024403, 2026-08-18. doi:10.1103/xby9-6mtn
- **Claims** (from APS abstract via search): In a biophysical bursting network, arousal is the control parameter. At intermediate arousal the network shows peaked susceptibility, power-law avalanches, shape collapse and DP hyperscaling.
- **Bears on:** l.472 and Table 4, since arousal states map onto the regime.
- **Verdict: NICE-TO-HAVE** (cite in the §A answer).

### Complexity measures

**7. Moses, B., Doss, M.K., & Tagliazucchi, E. (2026).** A critical review of brain entropy as a biomarker of the psychedelic state. *Neurosci Biobehav Rev*, online 2026-04-29. doi:10.1016/j.neubiorev.2026.106720
- **Claims** (from the ScienceDirect summary; the abstract itself was not retrieved): Entropy changes are not specific to psychedelics, and the many entropy metrics have distinct interpretations. Evidence that brain entropy equals phenomenal richness is limited.
- **Bears on:** l.415, entropy measures as "candidate quantification" of permeability; Table 4, ketamine "↑ EEG entropy" and psychedelics "↑ Complexity"; Table 3, Entropic Brain.
- **Verdict: MUST-CITE.** l.415 already hedges, so add "(entropy changes are, however, not specific to psychedelics; Moses et al., 2026)". Read the full text before citing.

**8. Jeantin, L., Bourdillon, P., Guénot, M., Bastuji, H., Sitt, J.D., & Naccache, L. (2026).** Atlas of intracranial EEG complexity across cortical regions and global states of consciousness in the human brain. *PNAS Nexus*, 2026-02-26. doi:10.1093/pnasnexus/pgag048
- **Claims:** 5,703 iEEG recordings from 106 participants (Kolmogorov complexity, permutation entropy, spectral entropy). Complexity is highest in wake/REM and lowest under propofol, variable in N2/N3, highest frontoparietally, and lower in epileptic cortex.
- **Bears on:** Table 4 "Evidence" column (currently "rich EEG"/"Moderate PCI") and l.486 (epileptic cortex: low differentiation).
- **Verdict: MUST-CITE.** It is the best normative dataset for Table 4.

**9. Newman, D., Maschke, C., Mashour, G.A., & Blain-Moraes, S. (2026).** Reframing "paradoxical" excitation: disentangling EEG complexity and entropy … propofol susceptibility. *Br J Anaesth* 137:525–534, online 2026-06-01. doi:10.1016/j.bja.2026.03.082
- **Claims:** At moderate propofol, responsive subjects showed a rise in LZ (Type I) complexity and a fall in statistical (Type II) complexity; unresponsive subjects showed the reverse. The two classes of complexity measure are often conflated.
- **Bears on:** l.482, where the complexity axis is operationalised as "Lempel-Ziv complexity (or entropy rate)". The paper shows that LZ is entropy-like and can diverge from structured complexity.
- **Verdict: NICE-TO-HAVE.** Consider a footnote noting that Type II measures may fit "differentiated richness" better.

**10. Berjaga-Buisan, T., … Massimini, M., Perl, Y.S., & Deco, G. (2026).** Thermodynamics of consciousness: non-equilibrium brain dynamics track conscious states. *Cell Reports* 45:117782, online 2026-07-31. doi:10.1016/j.celrep.2026.117782
- **Claims:** Violations of the fluctuation-dissipation theorem in whole-brain models mirror PCI across wake, anaesthesia and DoC, in humans and rodents.
- **Bears on:** l.480 (PCI as proxy). This is a rival physical principle (non-equilibrium rather than criticality) for the same marker.
- **Verdict: NICE-TO-HAVE.**

### Anaesthesia

**11. Helfrich, J., … Knight, R.T., & Larsson, P.G. (2026).** Spectral mapping reveals a resemblance of the anesthetic brain state to both sleep and coma. *PNAS*, 2026-05-11. doi:10.1073/pnas.2514098123
- **Claims:** Propofol shares spatiotemporal EEG features with both coma and NREM sleep. It also has unique posterior slow waves, frontocentral delta, and reduced aperiodic activity that overlaps with REM.
- **Bears on:** Table 4, propofol / NREM / vegetative rows.
- **Verdict: NICE-TO-HAVE.**

**Dreaming under anaesthesia: no in-window primary data.** Bajwa, Nilsen, Storm et al. is the closest candidate, a repeated-awakening study with PCIst and LZ under propofol (24/52 awakenings gave experience reports). It is **out of window**: *Sci Rep* 2025-09-24, doi:10.1038/s41598-025-12695-z. It is not cited in FMT and bears on l.441 and Table 4 propofol "Absent". Flag it for the owner as **MUST-CITE regardless of window**, since propofol sedation clearly produces reported experience. Doyal et al., *Anesthesiology* 2026-06-09 (doi:10.1097/aln.0000000000006153), is a commentary only.

### Sleep and dreaming

**12. Selte, A., Haworth, S.E., … Tononi, G., Boly, M., & Struck, A.F. (2026).** Neural signatures of conscious experience during sleep: a serial awakening study using high-density EEG. bioRxiv, 2026-08-20. doi:10.64898/2026.08.16.745040. A *Neurology* abstract precedes it (doi:10.1212/wnl.0000000000216389, 2026-06-09).
- **Claims:** 140 participants with 256-channel hdEEG, 699 N2/N3 awakenings. Dreaming came with reduced posterior alpha/delta, increased gamma measures and altered network organisation. The best classifier reached AUC 0.80.
- **Bears on:** l.767, "hot zone … predicts … with high accuracy". It supports the hot-zone claim at hdEEG resolution and answers the pass-1 Wu non-replication. Rephrase to "reliably above chance (AUC ≈ 0.80 in 140 participants; Selte et al., 2026)".
- **Verdict: MUST-CITE.**

**13. Michalak, … et al. (2026).** Immersive NREM2 dreaming preserves subjective sleep depth against declining sleep pressure. *PLOS Biology*, 2026-03-24. doi:10.1371/journal.pbio.3003683
- **Claims:** hdEEG with serial awakenings in N2. Perceived sleep depth was lowest with a mere "sense of presence" and highest in immersive dreaming or unconsciousness.
- **Bears on:** §6.3 NREM dreaming and ESM grading (§3.5). "Minimal presence" versus "immersive" is a graded-ESM distinction.
- **Verdict: NICE-TO-HAVE.**

**14. Wang, X., Peters, E., … LaBerge, S., Koenig, T., Dresler, M., Erlacher, D. (2026).** EEG microstates reveal distinct network dynamics in lucid and non-lucid REM sleep. *Conscious Cogn*, online 2026-04-13. doi:10.1016/j.concog.2026.104047
- **Claims:** In lucid REM, microstates A and G dominate and B, C and D are reduced. The authors read this as more self-visualisation and metacognition and less DMN-related activity.
- **Bears on:** l.771, lucid onset as ESM → extended consciousness, and Prediction 4. It says nothing about criticality.
- **Verdict: NICE-TO-HAVE.**

### Psychedelics and altered states

**15. Girn, M., Doss, M.K., Roseman, L., Preller, K.H., … (27 authors) (2026).** An international mega-analysis of psychedelic drug effects on brain circuit function. *Nature Medicine* 32:1543–1554, 2026-04-06. doi:10.1038/s41591-026-04287-9
- **Claims** (from press and index pages): 11 rsfMRI datasets, 267 participants, five psychedelics (psilocybin, LSD, mescaline, DMT, ayahuasca). The drugs share common alterations in associative, visual and sensorimotor network connectivity.
- **Bears on:** §6.1 and Table 4, psychedelics "All active, ↑ permeability". It supports a drug-general mechanism.
- **Verdict: NICE-TO-HAVE** (read before citing).

**16. Jajcay, N., … Tylš, F., et al. (2026).** EEG microstate dynamics during psilocybin intoxication relate to acute experience and persisting psychological changes. bioRxiv, 2026-06-12. doi:10.64898/2026.06.09.731183
- **Claims:** A double-blind crossover study (N=15). Psilocybin raised GFP-peak rate and altered microstate temporal organisation, and the changes tracked the acute experience.
- **Verdict: NICE-TO-HAVE.**

**17. Lange, R., & Houran, J. (2026).** Leveraging the Rasch near-death experience hierarchy: toward a phenomenologically precise definition of NDEs. *Psychol Conscious Theory Res Pract*, 2026-08-24. doi:10.1037/cns0000489
- **Claims:** It uses an item hierarchy to define NDEs. The abstract was not retrieved.
- **Verdict: NICE-TO-HAVE** (marginal).

### Disorders of consciousness

**18. Fecchio, M., … Edlow, B.L. (2026).** Covert brain complexity in the intensive care unit. *Cortex* 201:1–9, online 2026-04-17. doi:10.1016/j.cortex.2026.03.021
- **Claims:** A case report. TMS-EEG PCI detected signs of consciousness in an acute-ICU patient whom every other assessment classed as VS/UWS.
- **Bears on:** Table 4, "Covert awareness" row.
- **Verdict: NICE-TO-HAVE.**

---

## Nothing found (in window, verifiable)
- **New human σ/branching-ratio estimates across states, or critical slowing at loss of consciousness:** none.
- **Lucid-dream criticality (Prediction 4):** none (item 14 is microstates only).
- **Time dilation / temporal-echo neural data:** none in window. The pass-1 Taylor et al. is after the window.
- **Primary neural NDE studies:** none. **Dissociatives:** no ketamine criticality study. Clinical ketamine-in-DoC complexity papers (Liang et al., *J Neurosurg Anesthesiol* 2026, doi:10.1097/ana.0000000000001124) were seen but are marginal.
- **5-MeO-DMT / salvinorin:** none.

**Skipped:**
- Zenodo self-deposits (Galindez PCIst v-series, Römer, McCaul, Tiwari, etc.).
- Castellanos-Márquez & Cortés-Poza, "Phase transitions in a stochastic cellular automaton for cortical dynamics under anesthesia", *Chaos Solitons Fractals*, online 2026-07-15, doi:10.1016/j.chaos.2026.118807. The abstract was not retrievable. It is relevant to §3.7.2 (cortical automaton) and worth a read before v16.
