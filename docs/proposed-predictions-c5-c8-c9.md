# Proposed predictions for C5, C8 and C9

**C9: C9-1/C9-2 added S339 as E14/E15 (see C9 section). C5/C8 APPROVED by MG 2026-10-19; added to the map as nodes E12 (C5-1, L4 brain-specific), E13 (C5-2, L4 substrate-general; the method puts predictions at L4/L5, not L2/L3) and F11 (C8-1 with its veridical sub-arm and fourth uninterpretable arm, L5 cognitive), status `proposed`, with edges C5 → E12, C5 → E13, C8 → F11; C9 deferred.** None of them is in the FMT master or the wiki yet.

Status (original): proposal for MG's review, 2026-10-19.
Sources: map nodes C5, C8, C9 (`drafts/papers-moc7/fmt-prediction-map.json`); master v19 §2.8, §3.4.3, §3.4.4, §3.8, §4.4, §5.1.
Citation marks: **[CR]** verified on Crossref, **[OA]** verified on OpenAlex (no DOI or repository DOI only), **[UNVERIFIED]** not checked against a registry. Full list at the end.

---

## C5 — temporal echo

**Node:** recursion under closure smears content over time, and the smearing constitutes experienced temporal flow (§3.4.4).

**Derivation base.** §3.4.4: each frame "reverberates through recursive levels … bleeding into subsequent frames", which "is what gives conscious experience its characteristic *flow*". A system without closure "may carry state from frame to frame … but nothing in it models the carrying". The master leaves frame *duration* open ("an open empirical question the theory does not prejudge"), so a prediction has to target the smearing window, not the frame rate.

### C5-1 (human, recommended): shortening the echo window yields supramodal frame-like experience

**Statement.** A manipulation that shortens the window over which each frame's content persists into the next should make experience frame-like ("single frames, single thoughts, step by step"), and it should do so in every modality and in thought together. The size of the frame-like report should covary with the shortening of the brain's temporal integration window.

**Chain.** C5 says flow is the smearing. Less smearing, less flow. Because the echo runs through the explicit simulation as a whole, the loss is not tied to one sensory pathway.

**Measures.**
- Neural: autocorrelation window (ACW) of resting and task EEG/MEG, the standard intrinsic-timescale estimate (Honey et al., 2012 [CR]; Golesorkhi et al., 2021 [CR]; Wolff et al., 2022 [CR]). ACW already separates states of consciousness (Huang et al., 2018 [CR]; Zilio et al., 2021 [CR]).
- Behavioural: two-flash fusion threshold and simultaneity judgements (Samaha & Postle, 2015 [CR]), plus an auditory and a cognitive analogue (e.g. ordering two rapid thoughts in a cued sequence).
- Report: structured items for frame-like experience per modality and for thought, built on Melges's temporal-disintegration construct (Melges et al., 1970a, 1970b [CR]). No validated "stroboscopic experience" scale exists; this one has to be built and validated.

**Design.** Placebo-controlled THC, two doses, crossover, n ≈ 40 occasional users (frequent users show tolerance in time tasks; Sewell et al., 2012 [CR]). Eye tracking throughout.
Control for modality-specific loss: TMS over V5 produces transient motion blindness (Beckers & Zeki, 1995 [CR]), the lab analogue of akinetopsia (Zihl et al., 1983 [CR]). FMT reads this as loss of an implicit-model channel, so V5 TMS should give vision-only discontinuity with no global ACW change.

**Falsified if:** (a) THC produces frame-like reports without ACW shortening; (b) ACW shortens without frame-like reports; (c) frame-like reports are confined to vision or locked to saccades (see the colliculus note below).

**Rivals.** Discrete-perception accounts (VanRullen, 2016 [CR]; Herzog et al., 2020 [CR]) also predict stroboscopic experience, but tie it to the perceptual cycle: frames become visible when the cycle slows (alpha peak frequency down). FMT ties it to the smearing window (ACW down) and predicts that alpha frequency need not move. Uniqueness: **contested** on mechanism, **shared-in-part** on the phenomenon.

**Existing literature.** Melges et al. (1970a, b) reported marihuana-induced "temporal disintegration" (broken sequential, goal-directed thinking) correlated with depersonalization. Later THC work mainly finds interval overestimation (Atakan et al., 2012 [CR]), a different measure. LSD trails look periodic (Dubois & VanRullen, 2011 [CR]), favouring the discrete-perception reading there. ACW under THC is unmeasured. Status: **candidate-test**.

### C5-2 (in silico, recommended): echo ablation removes the self-model's representation of its own passage of time

MG's candidate (a), sharpened so that it targets the self-model.

**Statement.** In a closed architecture, cut the echo (the self-model's input at frame *t+1* no longer contains its own state at *t*; within-frame closure is kept). The self-model should then lose its representation of its own elapsed time and of the order of its own past states. The world-model's representation of external time should survive.

**Chain.** §3.4.4: what makes a "now" is that the carried state is modelled "as the recent past *of a perspective*". Remove the carrying into the self-model and that representation should go.

**Design (crucible).** Three arms: closure + echo; closure + echo cut; recurrence without closure. Probes: linear decoding of "time since my action X" and "order of my last two actions" from self-model units versus world-model units; a behavioural readout (report of own elapsed time). Any recurrent network encodes elapsed time somewhere, so the measure has to be located in the self-model.

**Prediction.** An interaction: self-located time representation present only with closure + echo.
**Falsified if:** the echo-cut arm decodes its own elapsed time from self-model units as well as the full arm does.
**Rivals:** silent; recurrence-based theories would predict time coding wherever there is memory and do not distinguish self-located from world-located coding. **Unique.** It tests representation, not experience, the same standard §3.4.3 applies to self-recognition. Status: **candidate-test**.

### C5-3 (rejected): LLMs cannot experience time as continuous

Vacuous: under §4.4 a current LLM lacks closure, so FMT assigns it no experience to be continuous or not. It is also an untestable extrapolation-class claim (`prediction-framing.md`, item 3).

### Superior colliculus: what holds, what is inference, what is MG's hypothesis

**CB1 density (established, partly).** The quantitative rat autoradiography finds the densest cannabinoid binding in substantia nigra pars reticulata, globus pallidus, entopeduncular nucleus, cerebellar molecular layer and hippocampus (Herkenham et al., 1990, 1991 [CR]). Secondary quotations of the 1991 paper place the colliculus's intermediate grey layer among regions with "slightly lower levels", and an mRNA study reports "little message" for CB1 in rat SC (cited in the chick CB1 mRNA paper, PMC2636724; primary source Mailleux & Vanderhaeghen, 1992 [CR]). I could not open the 1991 full text, so its per-layer values remain unchecked. **On present evidence the colliculus is a moderate-to-low CB1 site, not a high-density one.** Checking the 1991 tables, Tsou et al. (1998 [CR]) and the human map (Glass et al., 1997 [CR]) would settle it.

**SC and continuity (established).** The SC sends a corollary discharge of saccades via mediodorsal thalamus to frontal eye field (Sommer & Wurtz, 2002 [CR]), which supports perceptual continuity across saccades (Wurtz, 2018 [CR]). SC visual responses are suppressed around saccades and microsaccades (Hafed & Krauzlis, 2010 [CR]; Chen & Hafed, 2017 [CR]), and SC contributes to spatial attention (Krauzlis et al., 2013 [CR]; Basso et al., 2021 [CR]).

**Inference:** if THC disrupted the collicular corollary discharge, visual discontinuity would appear at saccades. **MG's hypothesis:** THC acting at the colliculus produces the frame-like experience.

**Assessment.** The collicular route predicts vision-specific, saccade-locked discontinuity; it does not explain thought running "step by step". The colliculus therefore belongs in C5-1 as falsifier (c), with frame reports time-locked to eye tracking. As a prediction of its own it lacks both an FMT derivation and the receptor density.

### The "small brain centre" papers

Most likely the paper MG means: **Chen et al. (2026), *Nature Neuroscience* [CR]**, covered in October 2026 as "Tiny brain structure anticipates what we are about to see or feel" (Medical Xpress). Seven-tesla fMRI, n = 80: pictures drive superficial SC layers, touch drives deeper layers, and the same layer pattern appears during anticipation before the stimulus. It concerns expectation and makes no claim about awareness. Next candidate: Murata et al. (2025, bioRxiv preprint, n = 14 [CR]): SC activity peaks just before recognition in a Mooney-image insight task, which the authors call unconscious.
Neither bears on C5 (no temporal-integration measure). Both bear weakly on C8 as real precursors a display could imitate; fMRI is too slow for real-time use, so they would only template the timing of the simulated build-up.

---

## C8 — meta-problem

**Node:** the explicit self-model cannot model its own generating substrate, which produces the intuition that consciousness is mysterious (§3.8).

**Derivation base.** §3.8: "The ESM can represent that it is having an experience, but it cannot represent the mechanism by which the experience is generated." §3.4.3: the ESM's "observational horizon is bounded by the EWM". §3.8 adds a second mechanism: occasional uninterpreted *leaks* of substrate processing produce the sense that "something vast operates just beyond the edge of introspective access".

### C8-1 (human, recommended, main): a simulated generation display reduces felt mystery

**Statement.** Give the self-model a generation story inside the simulation: an AR or screen display showing a plausible build-up of "your processing", contingent on and preceding the participant's own percept or decision. Reported mystery about that experience should drop. Whether the display is veridical should not matter. A display that is contingent but uninterpretable (noise textures timed to the same events, a leak analogue) should leave mystery unchanged or raise it.

**Chain.** Mystery comes from the self-model representing experience without its generation (§3.8). Anything that lets the simulation contain a generation account removes the absence, whatever its source. The ESM can receive substrate information only as content inside the simulation (§3.4.3), so a fake display and a real one reach it by the same route. The leak arm follows from the second mechanism in §3.8.

**Design.** Within-subject, four arms:
1. contingent display that precedes the experience (coherent build-up);
2. the same display mistimed (after the experience) or uncorrelated;
3. no display;
4. contingent, preceding, uninterpretable display (leak analogue).

Percept trials: stimulus onset is under experimenter control, so the build-up can start before it (degraded-to-clear images, Mooney-style). Decision trials: cued free choices with the build-up locked to the cue, or primed outcomes as in Wegner & Wheatley's (1999 [CR]) "I Spy" paradigm. A veridical sub-arm uses a real-time readiness-potential BCI (Schultze-Kraft et al., 2016 [CR]); FMT predicts veridical = fake.

Precedents for fake precursors changing self-attribution: false heart-rate feedback (Valins, 1966 [CR]), fake tone feedback shifting the reported moment of decision (Banks & Isham, 2009 [CR]), primed effect information raising experienced agency (Aarts et al., 2005 [CR]). Early motor preparation is partly reportable (Parés-Pujolràs et al., 2019 [CR]).

**Measures.** No validated psychometric instrument for felt mystery about one's own experience exists. Nearest: Díaz's (2021 [OA]) hard-problem intuition items, an extension to non-English speakers (Celka et al., 2026 [OA]), and Gottlieb & Lombrozo's (2018 [CR]) ratings of whether science can explain a mental phenomenon. Use per-trial ratings ("how mysterious was how this came about?", "could science explain how this came about?") plus the Sense of Agency Scale (Tapal et al., 2017 [CR]) as a secondary measure. Validating the trial-level item is part of the work.

**Demand characteristics** (Orne, 1962/2002 [CR]):
- arm 2 matches arm 1 in content and belief, differing only in timing and contingency;
- arm 4 matches arm 1 in timing, differing only in interpretability, and FMT predicts the opposite direction there, which demand would not produce;
- trait phenomenological control as covariate (Lush et al., 2020 [CR]);
- an expectation survey in a separate sample: if naive predictions reproduce the pattern, the result cannot be separated from demand.

**Falsified if:** arm 1 does not lower mystery relative to arm 2 at matched belief in the display; or the veridical display beats the fake one; or the leak arm lowers mystery as much as arm 1.

**Rivals.**
- Views on which the mystery tracks a real explanatory gap (cf. Chalmers, 2018 [OA]) predict no effect of a fake display: missing mechanism information is not what the gap consists in.
- AST (Graziano & Webb, 2015 [CR]) shares the explanation (a self-model omitting mechanism) but places it in an automatic attention schema that an external display does not alter, so on our reading it predicts no or a weaker effect. Illusionism reads the same way. Neither is a published prediction.

Uniqueness: **shared-in-part** (AST shares the explanation, not the manipulation's predicted effect). Status: **candidate-test**.

### C8-2 (merged): real-time neurofeedback of decision precursors

Alone, MG's candidate (b) cannot separate "received a generation story" from "received true information". Kept as the veridical sub-arm of C8-1.

### C8-3 (rejected as formulated): an in-silico system with substrate access stops producing hard-problem reports

Language-model reports are contaminated by training text: the master rejects them as evidence (§3.4.3), and Udell & Schwitzgebel (2021 [OA]) raise the same objection to Schneider's AI tests. A non-language agent needs a behavioural proxy for "mystery", and the obvious proxy (residual self-prediction error) falls in any architecture given more information, so it does not discriminate. Revisit if crucible finds a proxy that fails that check.

---

## C9 — binding dissolved

**MG S339:** §5.1 binding means field unity only; feature-to-object assignment is content computed by implicit spatial
models, so FMT owes no account of illusory conjunctions. Evidence base: `docs/c9-binding-evidence.md` (parietal TMS
moves illusory conjunctions in both directions, so it cannot test C9; on existing evidence C9 has no FMT-unique
prediction). **C9-1 approved for map + next FMT version (map node E14); C9-2 map only (E15).** Wording:
`docs/proposed-master-s8-additions.md` (C9 section).

### C9-1 (E14): misbinding and field unity have separate causes
Focal manipulation of feature binding leaves field unity and global complexity markers unchanged; graded sedation
degrades the whole field without raising conjunction errors at matched feature accuracy, and never yields features
outside one field. Shared in part (FIT shares the focal half); candidate-test.

### C9-2 (E15): synchrony is a signature, not the pairing mechanism
In-phase vs anti-phase gamma tACS changes detection and clarity, not which features pair. Contested against
temporal-binding accounts; candidate-test, feasibility uncertain.

---

## Ranked recommendation

| Rank | Candidate | Add to map | Next FMT version | Uniqueness | Risk to FMT if it fails |
|---|---|---|---|---|---|
| 1 | **C8-1** simulated generation display (with veridical and leak arms) | yes, L5 cognitive, C8 → node | §8, as an illustration | shared-in-part (AST) | moderate: refutes §3.8's mechanism, not closure |
| 2 | **C5-1** supramodal frame-like experience with ACW shortening | yes, L4 brain-specific, C5 → node | §8, after the ACW-under-THC pilot | contested (discrete perception) | moderate-high for C5; the core survives |
| 3 | **C5-2** echo ablation in silico | yes, L2/L3 substrate-general, candidate-test | §8.9 | unique (rivals silent) | low-moderate: representation only |
| — | C5-3, C8-3, SC-THC route | no | no | — | — |
| — | C9 | deferred | — | — | — |

---

## References

Verified [CR] unless marked.

- Aarts, H., Custers, R., & Wegner, D. M. (2005). *Consciousness and Cognition*, 14, 439–458. 10.1016/j.concog.2004.11.001
- Atakan, Z., et al. (2012). The effect of cannabis on perception of time: a critical review. *Curr Pharm Des*, 18, 4915–4922. 10.2174/138161212802884852
- Banks, W. P., & Isham, E. A. (2009). *Psychological Science*, 20, 17–21. 10.1111/j.1467-9280.2008.02254.x
- Basso, M. A., Bickford, M. E., & Cang, J. (2021). *Neuron*, 109, 918–937. 10.1016/j.neuron.2021.01.013
- Beckers, G., & Zeki, S. (1995). *Brain*, 118, 49–60. 10.1093/brain/118.1.49
- Braet, W., & Humphreys, G. (2009). *Visual Cognition*, 17, 25–47. 10.1080/13506280802193318
- Celka, K., Wyrwa, M., & Raś, M. (2026). Polishing the meta-problem of consciousness. *Philosophical Psychology*. 10.1080/09515089.2026.2710862 [OA]
- Chalmers, D. J. (2018). The meta-problem of consciousness. *J Consciousness Studies*, 25(9–10). [OA: title, author, year; venue and issue not registry-checked; no DOI]
- Chen, C.-Y., & Hafed, Z. M. (2017). *J Neurophysiol*, 117, 1657–1673. 10.1152/jn.00911.2016
- Chen, D., et al. (2026). Modality-specific reactive and predictive responses in the human superior colliculus. *Nature Neuroscience*. 10.1038/s41593-026-02480-0
- Coslett, H. B., & Saffran, E. (1991). Simultanagnosia. *Brain*, 114, 1523–1545. 10.1093/brain/114.4.1523
- Díaz, R. (2021). Do people think consciousness poses a hard problem? *J Consciousness Studies*. Repository DOI 10.48350/156357 [OA]
- Dubois, J., & VanRullen, R. (2011). *PLoS Biology*, 9, e1001056. 10.1371/journal.pbio.1001056
- Esterman, M., Verstynen, T., & Robertson, L. C. (2007). *NeuroImage*, 35, 1247–1255. 10.1016/j.neuroimage.2006.10.039
- Friedman-Hill, S. R., Robertson, L. C., & Treisman, A. (1995). *Science*, 269, 853–855. 10.1126/science.7638604
- Glass, M., Dragunow, M., & Faull, R. L. M. (1997). *Neuroscience*, 77, 299–318. 10.1016/s0306-4522(96)00428-9
- Golesorkhi, M., et al. (2021). *Communications Biology*, 4. 10.1038/s42003-021-02483-6
- Gottlieb, S., & Lombrozo, T. (2018). *Psychological Science*, 29, 121–130. 10.1177/0956797617722609
- Graziano, M. S. A., & Webb, T. W. (2015). *Frontiers in Psychology*, 6. 10.3389/fpsyg.2015.00500
- Hafed, Z. M., & Krauzlis, R. J. (2010). *J Neurosci*, 30, 9542–9547. 10.1523/jneurosci.1137-10.2010
- Herkenham, M., et al. (1990). *PNAS*, 87, 1932–1936. 10.1073/pnas.87.5.1932
- Herkenham, M., et al. (1991). *J Neurosci*, 11, 563–583. 10.1523/jneurosci.11-02-00563.1991
- Herzog, M. H., Drissi-Daoudi, L., & Doerig, A. (2020). *Trends Cogn Sci*, 24, 826–837. 10.1016/j.tics.2020.07.001
- Honey, C. J., et al. (2012). *Neuron*, 76, 423–434. 10.1016/j.neuron.2012.08.011
- Huang, Z., Liu, X., Mashour, G. A., & Hudetz, A. G. (2018). *J Neurosci*, 38, 2304–2317. 10.1523/jneurosci.2545-17.2018
- Krauzlis, R. J., Lovejoy, L. P., & Zénon, A. (2013). *Annu Rev Neurosci*, 36, 165–182. 10.1146/annurev-neuro-062012-170249
- Lush, P., et al. (2020). *Nature Communications*, 11. 10.1038/s41467-020-18591-6
- Mailleux, P., & Vanderhaeghen, J.-J. (1992). *Neuroscience*, 48, 655–668. 10.1016/0306-4522(92)90409-u
- Melges, F. T., et al. (1970a). Temporal disintegration and depersonalization during marihuana intoxication. *Arch Gen Psychiatry*, 23, 204. 10.1001/archpsyc.1970.01750030012003
- Melges, F. T., Tinklenberg, J. R., Hollister, L. E., & Gillespie, H. K. (1970b). Marihuana and temporal disintegration. *Science*, 168, 1118–1120. 10.1126/science.168.3935.1118
- Murata, T., et al. (2025). The superior colliculus arbitrates whole-brain dynamics for unconscious visual insight. *bioRxiv*. 10.1101/2025.04.09.648050 (preprint)
- Orne, M. T. (1962; reprinted 2002). *Prevention & Treatment*, 5. 10.1037/1522-3736.5.0035a
- Parés-Pujolràs, E., Kim, Y.-W., Im, C.-H., & Haggard, P. (2019). *NeuroImage*, 202, 116140. 10.1016/j.neuroimage.2019.116140
- Samaha, J., & Postle, B. R. (2015). *Current Biology*, 25, 2985–2990. 10.1016/j.cub.2015.10.007
- Schultze-Kraft, M., et al. (2016). The point of no return in vetoing self-initiated movements. *PNAS*, 113, 1080–1085. 10.1073/pnas.1513569112
- Sewell, R. A., et al. (2012). *Psychopharmacology*, 226, 401–413. 10.1007/s00213-012-2915-6
- Sommer, M. A., & Wurtz, R. H. (2002). *Science*, 296, 1480–1482. 10.1126/science.1069590
- Tapal, A., Oren, E., Dar, R., & Eitam, B. (2017). *Frontiers in Psychology*, 8. 10.3389/fpsyg.2017.01552
- Treisman, A., & Gelade, G. (1980). *Cognitive Psychology*, 12, 97–136. 10.1016/0010-0285(80)90005-5
- Treisman, A., & Schmidt, H. (1982). *Cognitive Psychology*, 14, 107–141. 10.1016/0010-0285(82)90006-8
- Tsou, K., et al. (1998). *Neuroscience*, 83, 393–411. 10.1016/s0306-4522(97)00436-3
- Udell, D. B., & Schwitzgebel, E. (2021). Susan Schneider's proposed tests for AI consciousness: promising but flawed. *J Consciousness Studies*. [OA via PhilPapers; volume not checked]
- VanRullen, R. (2016). Perceptual cycles. *Trends Cogn Sci*, 20, 723–735. 10.1016/j.tics.2016.07.006
- Wegner, D. M., & Wheatley, T. (1999). *American Psychologist*, 54, 480–492. 10.1037/0003-066x.54.7.480
- Wolff, A., et al. (2022). *Trends Cogn Sci*, 26, 159–173. 10.1016/j.tics.2021.11.007
- Wurtz, R. H. (2018). *Annu Rev Vision Sci*, 4, 215–237. 10.1146/annurev-vision-102016-061207
- Zihl, J., von Cramon, D., & Mai, N. (1983). *Brain*, 106, 313–340. 10.1093/brain/106.2.313
- Zilio, F., et al. (2021). *NeuroImage*, 226, 117579. 10.1016/j.neuroimage.2020.117579
