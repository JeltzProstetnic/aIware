# Ictal Route Verdict — Source A (paper §10.3) vs Source B (didactic-patterns caution)

**Session:** S300 · **Date:** 2026-08-10 · **Task:** resolve the hypersynchrony-vs-supercriticality disagreement on the dynamical route into generalized tonic-clonic (GTC) seizures.

**Sources in conflict:**
- **A** — `paper/full/four-model-theory-full.md` line 1046 (§10.3 seizure passage; companion claim at line 482): GTC seizures exit Class 4 "typically by pathological hypersynchrony and, in some recordings, by supercritical avalanche dynamics at onset and spread" (Meisel et al., 2012).
- **B** — `.claude/knowledge/didactic-patterns.md` line 773 (Pattern-4 caution): "the dynamical mechanism is supercritical + complexity-collapse, NOT 'ordered/synchronous Class-2.' Hypersynchrony is the correlate … (dominant route supercritical)."

---

## (a) Verified citation block — reference-list ready

All entries below verified against publisher pages / PubMed on 2026-08-10. Formatted to match the paper's existing reference style (cf. the existing Meisel 2012 entry at line 1367, which is **already correct as printed**).

```
Arviv, O., Medvedovsky, M., Sheintuch, L., Goldstein, A., & Shriki, O. (2016). Deviations from critical dynamics in interictal epileptiform activity. *Journal of Neuroscience*, 36(48), 12276-12292. https://doi.org/10.1523/JNEUROSCI.0809-16.2016

Hagemann, A., Wilting, J., Samimizad, B., Mormann, F., & Priesemann, V. (2021). Assessing criticality in pre-seizure single-neuron activity of human epileptic cortex. *PLoS Computational Biology*, 17, e1008773. https://doi.org/10.1371/journal.pcbi.1008773

Hobbs, J. P., Smith, J. L., & Beggs, J. M. (2010). Aberrant neuronal avalanches in cortical tissue removed from juvenile epilepsy patients. *Journal of Clinical Neurophysiology*, 27(6), 380-386. https://doi.org/10.1097/WNP.0b013e3181fdf8d3

Jiruska, P., de Curtis, M., Jefferys, J. G. R., Schevon, C. A., Schiff, S. J., & Schindler, K. (2013). Synchronization and desynchronization in epilepsy: Controversies and hypotheses. *The Journal of Physiology*, 591(4), 787-797. https://doi.org/10.1113/jphysiol.2012.239590

Kramer, M. A., Truccolo, W., Eden, U. T., Lepage, K. Q., Hochberg, L. R., Eskandar, E. N., Madsen, J. R., Lee, J. W., Maheshwari, A., Halgren, E., Chu, C. J., & Cash, S. S. (2012). Human seizures self-terminate across spatial scales via a critical transition. *Proceedings of the National Academy of Sciences*, 109(51), 21116-21121. https://doi.org/10.1073/pnas.1210047110

Meisel, C. (2020). Antiepileptic drugs induce subcritical dynamics in human cortical networks. *Proceedings of the National Academy of Sciences*, 117(20), 11118-11125. https://doi.org/10.1073/pnas.1911461117

Meisel, C., Storch, A., Hallmeyer-Elgner, S., Bullmore, E., & Gross, T. (2012). Failure of adaptive self-organized criticality during epileptic seizure attacks. *PLoS Computational Biology*, 8(1), e1002312. https://doi.org/10.1371/journal.pcbi.1002312

Truccolo, W., Donoghue, J. A., Hochberg, L. R., Eskandar, E. N., Madsen, J. R., Anderson, W. S., Brown, E. N., Halgren, E., & Cash, S. S. (2011). Single-neuron dynamics in human focal epilepsy. *Nature Neuroscience*, 14(5), 635-641. https://doi.org/10.1038/nn.2782
```

Notes on verification status:
- The Hagemann 2021 issue number was not shown on the fetched page; the entry above omits it (PLoS style tolerates this). Everything else — author lists, titles, volumes, pages, DOIs — was confirmed verbatim from PLoS, PubMed, or PMC.
- Hobbs 2010: the abstract does **not** report a numeric branching parameter σ > 1; the "supercritical" gloss in secondary summaries is an interpretation of the reported hyperactivity + positive branching–firing-rate feedback loop, not a quoted claim. Treat "Hobbs shows σ > 1" as UNVERIFIED.

---

## (b) What each key source actually establishes

### Meisel et al. 2012 — the citation both files lean on
- **Preparation:** invasive ECoG from **8 patients with focal epilepsy** during presurgical monitoring, electrodes at the presumed focus, 200/256 Hz. **Not GTC seizures** — the paper never claims generalized tonic-clonic; it does not even classify beyond "focal epilepsy."
- **Measure:** distributions of **phase-locking intervals (PLI)** — a synchronization statistic — not avalanche size distributions and not a branching parameter.
- **Findings, quoted:** "While the PLI distribution followed a power-law in time intervals preceding the seizure onset, a deviation from power-law behavior was observed in intervals containing the seizure attack." "The probability to find longer PLI increased during attacks thereby destroying the scale-free property." "After the seizure this distribution slowly relaxed back to a power-law." Abstract conclusion: "Together these results suggest that brain dynamics deviates from criticality during seizures caused by the failure of adaptive SOC."
- **Critical fact for this dispute:** the words **"supercritical," "subcritical," "branching," and "hypersynchron-" do not occur anywhere in the paper.** It establishes *departure from criticality, expressed as excess/prolonged synchronization*, in *focal* seizures. It licenses neither "typically hypersynchrony" nor "dominant route supercritical," and it does not directly cover GTC seizures at all — the paper's citation is a **scope stretch** in both files.

### Truccolo et al. 2011 (Nat Neurosci) — onset is not hypersynchronous at neuronal scale
Human focal epilepsy, single-unit microelectrode arrays. Quoted: "neuronal spiking activity during seizure initiation and spread was highly heterogeneous, not hypersynchronous"; termination by contrast shows "an almost complete cessation of spiking across recorded neuronal ensembles." Directly contradicts "typically by pathological hypersynchrony … at onset and spread."

### Jiruska et al. 2013 (J Physiol review) — the field's own correction of the hypersynchrony dogma
Quoted from abstract: "Epilepsy has been historically seen as … a hypersynchronous state. Recent evidence showed that … seizures result from complex interactions between neuronal networks characterized by heterogeneity of neuronal firing and dynamical evolution of synchronization. **Desynchronization is often observed preceding seizures or during their early stages; in contrast, high levels of synchronization observed towards the end of seizures may facilitate termination.**" I.e., hypersynchrony is real but **late-phase**, not the onset route.

### Arviv et al. 2016 (J Neurosci) — supercritical-direction deviations, but interictal
MEG, epilepsy patients vs controls, **interictal** epileptiform activity: "patients tended to exhibit a higher neural gain and larger avalanches, particularly during interictal epileptiform activity"; "deviations from scale-free behavior were exclusively connected to brief intervals at epileptiform discharges." Supports supercritical-direction excursions tied to epileptiform events — but does not measure seizures themselves, let alone GTC.

### Hobbs et al. 2010 (J Clin Neurophysiol) — epileptic tissue, aberrant avalanche regulation
In vitro slices from juvenile epilepsy patients: "prolonged periods of hyperactivity"; "a positive correlation between the branching parameter … and firing rate … part of a positive feedback loop [that] may contribute to some forms of epilepsy." Consistent with a runaway-gain (supercritical-tending) mechanism; no σ value quoted in abstract (see UNVERIFIED note above).

### Meisel 2020 (PNAS) — the pharmacological arrow
Antiepileptic drugs "decline [cascades and temporal correlations] precisely as predicted for a branching process" — AEDs push cortex **subcritical**, establishing a safety margin against "runaway activity associated with the supercritical phase." Implication: the seizure-*prone* direction is toward/past criticality — supportive of the supercritical picture as the *risk axis*, but indirect evidence about ictal dynamics themselves.

### Hagemann et al. 2021 (PLoS Comput Biol) — the strongest brake on "dominant route supercritical"
Single units, 20 patients, 87 pre-seizure recordings, branching-parameter estimation: "none of the patients consistently showed a systematic trend prior to seizure onset"; "we found no evidence for a transition towards supercritical dynamics in pre-seizure single neuron activity of human cortex"; epileptic cortex "operates in the stable, slightly subcritical regime, just like cortex of other healthy mammalians." At single-neuron scale, the supercritical on-ramp is simply not observed.

### Kramer et al. 2012 (PNAS) — termination, not onset, is the clean critical transition
Multi-scale human recordings (scalp EEG → ECoG → LFP → MUA): "seizures self-terminate via a discontinuous critical transition or bifurcation," with slowing, increased correlation, and flickering on approach; status epilepticus "repeatedly approach[es], but do[es] not cross, the critical transition." Phase-dependence again: the well-characterized critical phenomenology sits at the *end* of the seizure.

### Terminological trap (part of why A and B collided)
"Supercritical" and "hypersynchronous" are **not exclusive alternatives** — they belong to different order parameters. In the branching/avalanche framing, supercritical means σ > 1 runaway propagation. In the synchronization-transition framing (which is Meisel 2012's actual framing), the pathologically *synchronized* state is the far side of the sync transition. Meisel 2012's "longer phase-locking intervals destroy the scale-free property" can be read as either "hypersynchrony" (Source A's reading) or "past-critical excursion" (Source B's reading). Both files projected a specific mechanism onto a paper that asserts only *departure from criticality*.

---

## (c) Verdict

**Both sources are oversimplifications of a phase- and scale-dependent picture, and both over-read Meisel 2012. The dominant route is unsettled.**

1. **Source A is wrong** that hypersynchrony is the *typical onset-and-spread* route: at single-neuron resolution, onset and spread are heterogeneous, often desynchronized (Truccolo 2011; Jiruska 2013). Hypersynchrony is characteristic of the **late seizure and termination**. A's citation of Meisel 2012 for a GTC claim is also a scope stretch (focal seizures, synchronization statistics).
2. **Source B is wrong** that the route is settled as "dominant route supercritical": supercritical-direction evidence is interictal (Arviv 2016), in vitro (Hobbs 2010), or indirect via pharmacology (Meisel 2020), while the most direct pre-seizure test found **no** supercritical transition at single-unit scale (Hagemann 2021). B is right, however, that "ordered/synchronous Class-2" is not the mechanism story and that hypersynchrony ≠ subcriticality.
3. **What is robust:** ictal dynamics *depart from the critical regime* (Meisel 2012; Arviv 2016), the departure's signature depends on seizure phase (heterogeneous onset → synchronization building → hypersynchronous/near-silent termination via a discontinuous critical transition; Jiruska 2013, Kramer 2012, Truccolo 2011) and on recording scale (field-level synchrony vs single-unit heterogeneity; Hagemann 2021). The theory-level invariant — **exit from Class-4, route-unspecified, → Class-4 involvement collapses → unconsciousness** — survives untouched; it is in fact the *only* formulation the literature currently licenses.

Resolution for the data-integrity conflict: **neither file should win; both get replaced** with route-unsettled, phase/scale-dependent wording (below).

---

## (d) Proposed replacement wordings

### D1 — Paper, §10.3 (line 1046), replacing the sentence from "generalized tonic-clonic seizures drive the cortex out of Class 4 as well" through "(Meisel et al., 2012)"

> …generalized tonic-clonic seizures drive the cortex out of Class 4 as well — by a route that the ictal literature shows to be phase- and scale-dependent rather than uniform: human ictal recordings depart from the power-law statistics of the critical regime (Meisel et al., 2012), single-neuron activity at onset and spread is heterogeneous rather than hypersynchronous (Truccolo et al., 2011), and the pathological hypersynchrony classically ascribed to seizures becomes dominant only late in the seizure and toward termination (Jiruska et al., 2013), which itself proceeds as a discontinuous critical transition (Kramer et al., 2012).

The paragraph's existing follow-on — "Either route abolishes the structured, differentiated dynamics Class 4 requires … the invariant the theory commits to is the loss of Class 4 dynamics, not a single value of the branching ratio" — should be kept verbatim, with one word changed: "Either route" → "Every such route." The earlier sentence in the paragraph contrasting supercritical runaway (σ > 1) with pathological hypersynchrony as two departures from Class 4 stands as-is: it presents them as possible routes, not as a frequency claim. (Register check: no "iff"/"only"/one-directional criticality claim introduced; the hedge is now *more* honest — the frequency claim "typically" is dropped because the literature does not support any typicality ranking.)

**Companion edit (line 482, extent-dimension passage):** replace "yet the activity is typically pathologically synchronous and low in differentiation, a failure of the self-organized criticality that characterizes the waking state (Meisel et al., 2012)" with:

> yet the activity is pathologically organized and low in differentiation — hypersynchronous in its classical field-level description, heterogeneous at single-neuron resolution early in the seizure — a failure of the self-organized criticality that characterizes the waking state (Meisel et al., 2012; Truccolo et al., 2011).

**Reference-list additions required by D1:** Truccolo et al. 2011, Jiruska et al. 2013, Kramer et al. 2012 (entries in block (a); Meisel 2012 entry already present and correct).

### D2 — Knowledge file, `.claude/knowledge/didactic-patterns.md` line 773, replacing the whole Pattern-4 caution bullet

> - **Seizure (Pattern 4):** the dynamical mechanism is a **departure from criticality**; the route is **phase- and scale-dependent and NOT settled** — do not write "ordered/synchronous Class-2," and do not write "dominant route supercritical" either (S300 literature check). Onset/spread: heterogeneous, often desynchronized at single-neuron scale (Truccolo 2011; Jiruska 2013); supercritical-direction signatures are interictal/in-vitro/pharmacological (Arviv 2016; Hobbs 2010; Meisel 2020), and pre-seizure single units show **no** supercritical drift (Hagemann 2021); hypersynchrony dominates the late phase and termination (Jiruska 2013; Kramer 2012). Meisel 2012 — the paper's citation — is focal seizures + phase-locking statistics and shows only loss of power-law criticality via excess synchronization; it never says "supercritical" or "hypersynchrony," so cite it for *departure from criticality*, nothing narrower. Reconcile route-independently: "exit from Class-4 (route phase/scale-dependent, unsettled) → Class-4 involvement drops → unconscious." (Earlier passes flipped between "Class-2" and "dominant supercritical"; both overstate.)

---

## Sources consulted (all fetched 2026-08-10)

- PLoS Comp Biol full text, Meisel 2012: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002312
- PLoS Comp Biol full text, Hagemann 2021: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008773
- PubMed: Hobbs 2010 (21076327), Arviv 2016 (27903734), Jiruska 2013 (23184516), Truccolo 2011 (21441925), Meisel 2020 (32358198), Kramer 2012 (23213262); PMC3529091 for the Kramer author list.
