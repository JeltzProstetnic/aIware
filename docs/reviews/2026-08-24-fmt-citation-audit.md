# FMT Master Paper — Citation Characterization & Arithmetic Audit

Agent audit, 2026-08-24. Scope: `/home/jeltz/aIware/paper/full/four-model-theory-full.md` (line numbers below refer to this file), cross-checked against `.claude/knowledge/didactic-patterns.md` (theory registry) and primary sources via web. NoC propagation checked in `paper/trimmed/noc/four-model-theory-noc.md`.

## Verdict

**Fifteen characterization defects found (11 CONFIRMED against primaries, 4 SUSPECTED/partially confirmed), plus one internal arithmetic inconsistency.** Every confirmed defect fails in the same direction as the RIM paper's six: toward more support than the source provides. **Three warrant an erratum on the published version on their own:** (1) a fabricated verbatim quotation — "largely orthogonal" is attributed in quotation marks to Hohwy & Seth (2020) and does not appear in that paper; (2) the central conclusion of Pinto et al. (2017) is inverted — the paper attributes to them a "finding" of two degraded conscious agents per hemisphere when their stated conclusion is that callosotomy "does not create two independent conscious perceivers within one brain"; (3) two quantitative attributions to Schartner et al. (2017) — "increases of approximately 15-20%" and "dose-response curves" — are absent from that study, which used a single dose per drug and reports no such percentage. A fourth cluster (both species wrong in the animal-evidence table, a drug swapped in a psychedelic claim, a dangling "Siclari et al. (2021)" that appears not to exist) would be caught by any careful referee. The existing gates could not see any of this: every cited work exists and every cite key resolves.

---

## Findings (most severe first)

### 1. CONFIRMED — Fabricated quotation: "largely orthogonal" (Hohwy & Seth, 2020)

- **Claim (line 839):** "Hohwy and Seth (2020) characterize predictive processing as a systematic framework for *locating* the neural correlates of consciousness, 'largely orthogonal' to the question of what *makes* a state conscious in the first place"
- **Source actually says:** Full text searched (PDF from philosophymindscience.org, doi 10.33735/phimisci.2020.II.64). The word "orthogonal" occurs exactly once, about experimental design: "Methodologically, PP has inspired studies of attention and expectation treated as orthogonal factors." The phrase "largely orthogonal" does not occur. The nearest real support is: "It is precisely because PP is not itself a theory of consciousness that it holds unique promise…"
- **Why it matters:** Quotation marks assert verbatim text. A reviewer or the quoted authors checking this finds an invented quote — the single most damaging class of citation error in a published paper. The *substance* of the sentence is defensible; the quotation is not.
- **Minimal repair:** Remove the quotation marks and paraphrase, or quote the genuine sentence "PP is not itself a theory of consciousness."
- **Propagation:** Master only (not in NoC).

### 2. CONFIRMED — Pinto et al. (2017): interpretation inverted, title misquoted

- **Claim (line 897):** "…is consistent with Pinto et al.'s (2017) finding of 'unified consciousness, split perception' — each hemisphere retains a degraded but functionally complete conscious agent."
- **Also (line 662):** "Each hemisphere then generates its own independent simulation… This accounts for each hemisphere sustaining independent consciousness… and the graded deficits observed by Pinto et al. (2017)."
- **Source actually says** (Brain 140(5):1231–1237, abstract conclusion, read via PMC): "These findings suggest that severing the cortical connections between hemispheres splits visual perception, **but does not create two independent conscious perceivers within one brain.**" Actual title: "Split brain: divided perception but undivided consciousness."
- **Why it matters:** Line 897 attributes to Pinto a "finding" of *two* conscious agents ("each hemisphere retains a… conscious agent") — the exact claim their paper was written to reject. This is the author's-interpretation-inverted class (same shape as the RIM R² finding). The quoted phrase is also a reordered paraphrase of their title presented inside quotation marks. FMT may legitimately *reinterpret* Pinto's data (accurate cross-field responding is compatible with either reading), but it must be presented as FMT's reinterpretation against the authors' stated conclusion, not as their finding.
- **Minimal repair:** Line 897: "consistent with Pinto et al.'s (2017) finding of divided perception with preserved unified responding — data the theory reinterprets as two degraded simulations rather than, as Pinto et al. themselves conclude, one undivided conscious agent." Drop the pseudo-quote.
- **Propagation:** NoC line 360 has the milder form ("Each hemisphere sustains independent consciousness… Graded rather than binary deficits (Pinto et al., 2017)…") — same tension, needs the same hedge.

### 3. CONFIRMED — Schartner et al. (2017): "15-20%" and "dose-response curves" are not in the source

- **Claim (line 411):** "Schartner et al. (2017) report Lempel-Ziv complexity increases of approximately 15-20% under psychedelic doses relative to placebo, with dose-response curves that could anchor the permeability parameter to measurable values."
- **Source actually says** (Sci Rep 7:46421, full text read via PMC5396066): No percentage of that kind is reported anywhere; results are given as effect sizes and sign-consistency across participants (e.g., LZs increases in 100% of ketamine and 93% of LSD participants). Design was **one psychoactive dose per drug** (LSD 75 μg IV; psilocybin 2 mg IV; ketamine 0.25 mg/kg bolus + 0.375 mg/h): **no dose-response curves exist in the study.** (Raw normalized diversity increases are on the order of a few percent, not 15–20%.)
- **Why it matters:** This is the paper's "Quantitative grounding" paragraph for permeability — both load-bearing numbers attributed to the source are absent from it, in the direction of more support. Identical shape to RIM's fabricated age-comparison.
- **Minimal repair:** "Schartner et al. (2017) report significantly increased spontaneous MEG signal diversity under single psychoactive doses of ketamine, LSD and psilocybin; dose-response mapping of these measures remains to be done and would be needed to anchor the permeability parameter."
- **Propagation:** Master only.

### 4. CONFIRMED — Animal-evidence table: both species wrong (Shew et al. 2009; Beggs & Plenz 2003), and the row's claim collapses

- **Claim (line 777, criticality row of the FMT-operations table):** "Power-law neuronal avalanches in turtle cortex (Shew, Yang, Petermann, Roy, & Plenz, 2009) and cat visual cortex (Beggs & Plenz, 2003), demonstrating that Class 4 dynamics are not mammal-specific"
- **Sources actually say:** Shew et al. 2009 (J Neurosci 29:15595) used **rat cortex slice cultures** on microelectrode arrays — not turtle. Beggs & Plenz 2003 (J Neurosci 23:11167) used **organotypic cultures and acute slices of rat somatosensory cortex** — not cat. (Verified via abstracts/methods.)
- **Why it matters:** Both attributions are wrong, and since both real preparations are rat, the row's own purpose — "demonstrating that Class 4 dynamics are not mammal-specific" — is unsupported by either citation.
- **Minimal repair:** Turtle avalanche criticality is Shew et al. 2015 (*Nature Physics* 11:659, ex vivo turtle visual cortex); in vivo cat visual cortex avalanches are Hahn et al. 2010 (*J Neurophysiol* 104:3312). Swap in those two and the row (and its non-mammal claim, via the turtle) becomes true. Alternatively keep the current citations and rewrite the row honestly as rat in vitro evidence.
- **Propagation:** Master only (table absent from NoC).

### 5. CONFIRMED — Kawakita et al. (2025): group-level alignment described as "cross-individual", and Prediction 5's "already demonstrated" overstates

- **Claims (line 298):** "…recovers stable cross-individual correspondences without shared labels (Kawakita et al., 2025)"; **(line 947):** "…will generalize across individuals — Gromov–Wasserstein optimal transport… will recover above-chance cross-individual correspondence…"; **(line 951):** "The structural arm is already demonstrated for color similarity across individuals (Kawakita et al., 2025)".
- **Source actually says** (iScience 28(3):112029; methods verified via full-text search): alignment was performed **between pooled participant groups**, "each consisting of 128 participants", resampled 20 times — explicitly because "the number of color pairs reported by each participant was only 162 at most, which is too small to reliably estimate the entire color similarity structure of 93 colors." No individual-to-individual alignment was performed or possible with their data.
- **Why it matters:** Prediction 5's structural arm is claimed as "already demonstrated… across individuals" when the demonstration is group-to-group. The individual-level structural alignment is still an open empirical question — which actually makes Prediction 5 *more* novel, but the current text claims support the source does not give (narrow study, broad subject — the Wechsler-scales shape).
- **Minimal repair:** "recovers stable correspondences between independent groups of observers without shared labels"; and in 8.6: "demonstrated at the group level for color similarity (Kawakita et al., 2025); the individual-level structural arm, like the decoding arm, remains to be tested."
- **Propagation:** Master only.

### 6. CONFIRMED — Timmermann et al. (2023): DMT study cited as psilocybin evidence

- **Claim (line 895):** "…and dose-dependent visual cortex effects demonstrated with psilocybin (Timmermann et al., 2023)."
- **Source actually is** (paper's own reference list, line 1522): "Human brain effects of DMT assessed via EEG-fMRI", PNAS 120(13):e2218949120 — a **DMT** study (single 20 mg IV dosing regimen), not psilocybin, and not a dose-response design.
- **Why it matters:** Wrong drug attributed to the cited work in a sentence claiming convergent support for the permeability-hierarchy prediction; "dose-dependent" additionally unsupported.
- **Minimal repair:** "…and visual-system effects demonstrated with DMT (Timmermann et al., 2023)" — or cite an actual psilocybin dose-response study (e.g., the psilocybin arm of Carhart-Harris et al. 2012/2016 has no dose gradient either; if no dose-response source exists, drop "dose-dependent").
- **Propagation:** NoC cites Timmermann et al. 2023 only as generic "partial evidence" without the psilocybin claim — NoC usage is acceptable.

### 7. CONFIRMED — Byczynski & D'Angiulli (2025): correlational result reported as causal

- **Claim (line 556):** "Byczynski and D'Angiulli (2025) demonstrated that the subjective vividness of voluntary mental imagery — a phenomenal property of the explicit simulation — causally primes detection of subliminal visual stimuli, showing that virtual-level properties modulate substrate-level perceptual processing."
- **Source actually says** (Neurosci Conscious 2025(1):niaf026, read at OUP): the vividness–priming link is **correlational** — "This priming effect seems driven by the gradient of imagery vividness"; vividness was self-reported, not manipulated; the design cannot establish that vividness *causes* the priming.
- **Why it matters:** This citation is the empirical support for FMT's anti-epiphenomenalism claim ("Empirical evidence for this feedback direction is emerging"). Correlational-as-causal is defect class (b), on the paper's most philosophically contested claim.
- **Minimal repair:** "…found that vividness of voluntary imagery predicts (correlationally) enhanced detection of subliminal visual stimuli — consistent with, though not demonstrating, virtual-level properties modulating substrate-level processing."
- **Propagation:** Master only.

### 8. CONFIRMED (Rouault) / SUSPECTED (Rahnev) — §9 Open Question 4 statistics not in the cited sources

- **Claims (line 1003):** "Across 498 participants (Rouault et al., 2018), metacognitive sensitivity is largely decoupled from first-order performance — only about 22% of meta-d′ variance is explained by d′…" and "…a within-subject stimulus-difficulty manipulation (n = 12; Rahnev et al., 2013) triples d′ (1.05 → 3.20) while metacognitive efficiency remains invariant (M-ratio ≈ 0.96 throughout)."
- **Sources actually say:** Rouault et al. 2018 (full text read via PMC6117452) reports **no** meta-d′~d′ variance figure; the only variance-explained statement is "performance accounted for only 3.2% of the variance in confidence levels" — a different quantity. (Expt 1 n=498 is correct; the dissociable-shifts finding is correctly characterized.) Rahnev et al. 2013 as listed (J Neurophysiol 110:1811) is "Continuous theta burst TMS reduces resting state connectivity between visual areas" — a TMS/resting-state-fMRI study, not a "stimulus-difficulty manipulation"; the d′ 1.05→3.20 / M-ratio 0.96 numbers could not be located in it or in any Rahnev publication searched (including Rahnev & Fleming 2019, which deliberately *matched* d′ across conditions).
- **Why it matters:** The paragraph opens "A reanalysis of openly available metacognition data…" — if these numbers are the author's own computations on Confidence Database datasets, the text must say so per-number; as written, both statistics are attributed to papers that do not contain them, and a checking reviewer will find neither. If they are NOT own-reanalysis, the source of the numbers is unknown.
- **Minimal repair:** Either label each number explicitly as "recomputed here from the openly shared data of [dataset]" or replace with statistics the papers actually report (e.g., Rahnev et al. 2020's Confidence Database pooled r, which the same paragraph already uses and declares as reanalysis).
- **Propagation:** Master only.

### 9. MODERATE, CONFIRMED — Hengen & Shew (2025) meta-analysis credited with a consciousness conclusion it does not draw

- **Claims (line 174):** "A ~140-dataset meta-analysis (Hengen & Shew, 2025) confirms criticality tracks consciousness"; **(line 887):** "…the Hengen and Shew (2025) criticality meta-analysis independently confirmed it [that all consciousness-abolishing agents push the substrate subcritical] through empirical consolidation of ~140 datasets."
- **Source actually is** (Neuron 113(16):2582–2598 + bioRxiv version): a perspective containing a genuine meta-analysis of 140 avalanche distributions (73 papers, 2003–2024) whose object is **whether the brain operates at criticality as a setpoint of brain function** and whether the long-standing exponent controversy is a methodological artifact ("a long-standing controversy is the product of a methodological choice with no bearing on underlying dynamics"). It spans wake/sleep/anesthesia but does not test or conclude that "consciousness tracks criticality across pharmacological, pathological, and physiological state changes," and it contains no anesthetic-agent analysis of the kind line 887 attributes to it.
- **Why it matters:** The "~140 datasets" figure is real (good), but the conclusion attributed to the meta-analysis is ConCrit's thesis, not Hengen & Shew's. The convergence claim is one of the paper's headline assets (abstract, §1, §3.7, §7, §8.1, §11), so precision here is cheap and valuable.
- **Minimal repair:** "a ~140-dataset meta-analysis (Hengen & Shew, 2025) consolidates the evidence that waking cortex operates near criticality; the ConCrit framework (Algom & Shriki, 2026) extends this into an explicit criticality–consciousness account." Line 887: drop "independently confirmed it" or re-scope to the setpoint claim.
- **Propagation:** NoC lines 223/226 ("meta-analysis of 140 datasets confirms criticality… confirmed the criticality-consciousness link across 140 datasets") — same repair needed in NoC.

### 10. MODERATE, CONFIRMED — Meisel et al. (2012) and Truccolo et al. (2011): focal-seizure evidence deployed in generalized tonic-clonic claims (registry-flagged)

- **Claims (line 482):** "A generalized tonic-clonic seizure drives a very large fraction of cortex into simultaneous activity… a failure of the self-organized criticality that characterizes the waking state (Meisel et al., 2012; Truccolo et al., 2011)." **(line 1048):** "generalized tonic-clonic seizures drive the cortex out of Class 4 as well — by a route that the ictal literature shows to be phase- and scale-dependent…: human ictal recordings depart from the power-law statistics of the critical regime (Meisel et al., 2012)…"
- **Sources actually are:** Meisel et al. 2012 (PLoS Comput Biol 8:e1002312, abstract read): **focal seizures**, 8 presurgical patients, ECoG, departure from power-law phase-locking statistics — it "does not cover generalized tonic-clonic seizures" (this exact limit is recorded in the theory registry: didactic-patterns.md, seizure caution — "Cite it for *departure from criticality*, nothing narrower"). Truccolo et al. 2011 is likewise human **focal** epilepsy (single-neuron recordings).
- **Why it matters:** The registry's S300 verdict is otherwise well incorporated (no "supercritical"/"Class-2" claims survive — good), but both remaining citations sit inside sentences whose grammatical subject is GTC seizures. A reviewer who reads Meisel will note the scope extension.
- **Minimal repair:** Attribute explicitly: "human focal-seizure recordings depart from the power-law statistics of the critical regime (Meisel et al., 2012), and single-neuron activity in focal seizures is heterogeneous at onset (Truccolo et al., 2011); the theory extrapolates the same departure-from-criticality reading to generalized seizures."
- **Propagation:** Master only.

### 11. CONFIRMED — "Siclari et al. (2021)": dangling citation; no matching publication found; "decoded" overstates

- **Claim (line 751):** "Siclari et al. (2021) further showed that dream content can be decoded from posterior cortical activity during both REM and NREM sleep…"
- **Status:** No "Siclari et al. (2021)" entry exists in the paper's reference list (only Siclari 2017 and Siclari et al. 2018), and web search finds no 2021 Siclari publication decoding dream content. The nearest real result is in Siclari et al. **2017** itself: high-frequency activity in the posterior hot zone **correlated with specific dream contents** — a correlation, not decoding.
- **Why it matters:** A citation that resolves to nothing, carrying a strengthened verb ("decoded" > "correlated"). This one escaped the existence gate because the gate checks the reference list, not narrative citations.
- **Minimal repair:** "…and high-frequency activity within the hot zone correlated with specific dream contents in both REM and NREM sleep (Siclari et al., 2017)." Delete the 2021 citation.
- **Propagation:** Master only.

### 12. CONFIRMED — Benjamin & Kording (2023) cited for basal-ganglia neuron counts it does not contain; counts are unlabeled rat values

- **Claim (line 1011):** "The massive compression ratio from striatum (~2.8 million neurons) to basal ganglia output nuclei (~30,000 neurons) is consistent with an evaluative bottleneck architecture (Benjamin & Kording, 2023)."
- **Source actually is** (PLOS Comput Biol 19:e1011484, read at PLOS): a paper exclusively about **cortical interneurons** as adversarial discriminators; it contains no striatal/output-nuclei counts and no basal-ganglia bottleneck material. Separately, ~2.8 million striatal neurons is the **rat** figure (Oorschot 1996); the human striatum has on the order of 10⁸ neurons — and the surrounding passage is about human schizophrenia.
- **Minimal repair:** Move the Benjamin & Kording citation to the adversarial-discriminator sentence where it belongs (alongside Gershman 2019); source the counts to Oorschot (1996) and state they are rat values, or use human estimates.
- **Propagation:** Master only.

### 13. CONFIRMED — Li et al. (2010): universal "requires" from a single-patient case study

- **Claim (line 636):** "complete conscious anosmia instead requires a cortical lesion in right orbitofrontal cortex (Li et al., 2010)"
- **Source actually is** (Psychol Sci 21:1454, abstract verified): a **single-patient case study** — one patient with right-OFC traumatic injury showing complete anosmia with preserved "blind smell." One case supports "has been observed after," not "requires."
- **Minimal repair:** "…complete conscious anosmia has instead been reported after a right orbitofrontal lesion (single-case evidence: Li et al., 2010; converging TMS evidence exists)." (cTBS over right OFC impairing conscious olfactory perception — e.g., PMC6560072 — would strengthen this honestly.)
- **Propagation:** Master only.

### 14. CONFIRMED — Doyon, Penhune & Ungerleider (2003) mischaracterized as an implicit/explicit dissociation

- **Claim (line 899):** "The implicit/explicit axis corresponds… to the motor learning dissociation between cerebellar-striatal implicit (procedural) learning and hippocampal-prefrontal explicit (declarative) learning (Doyon, Penhune, & Ungerleider, 2003)."
- **Source actually says** (Neuropsychologia 41:252, abstract verified): the dissociation is **cortico-striatal (motor sequence learning) versus cortico-cerebellar (motor adaptation)** — two implicit motor systems contrasted with each other. It contains no hippocampal-prefrontal explicit/declarative arm, so it cannot anchor the implicit/explicit axis.
- **Minimal repair:** Cite Squire (2004) — already in the paper — or Doyon & Benali 2005 plus a declarative-memory source for the explicit arm; or drop the Doyon citation and rest the implicit/explicit axis on Dehaene & Naccache (2001), which the sentence already carries and which is apt.
- **Propagation:** Master only.

### 15. CONFIRMED (minor) — Katlowitz et al. (2026): anesthetic context misdescribed

- **Claim (line 735):** "recorded from hippocampal neurons in patients undergoing propofol **sedation for epilepsy monitoring**…"
- **Source actually is** (Nature 654:714; abstract + coverage verified): intraoperative Neuropixels recordings in seven epilepsy patients **under propofol-based general anesthesia during anteromesial temporal lobectomy** — surgery, not monitoring; general anesthesia, not sedation. (Content claims — oddball/semantic/lexical discrimination, word prediction, representational plasticity — are accurately characterized; note the paper frames plasticity via oddball effect growth, and "syntactic discrimination" corresponds to part-of-speech decoding.) The mislabel actually *understates* FMT's support (general anesthesia is the stronger dissociation), but it misstates the source.
- **Minimal repair:** "…patients undergoing temporal-lobe resection under propofol-based general anesthesia…" Also reconsider Table 1b line 195, which reads as if Katlowitz tested "statistical learning, priming, skill consolidation" — those are proposed paradigms, not the study's content.
- **Propagation:** Master only.

### 16. SUSPECTED — Voss et al. (2014) credited with observational gamma-onset dynamics

- **Claim (line 939):** "Existing work on lucid dream onset (Voss et al., 2014) reports gradual gamma-power increases rather than step-like transitions…"
- **Concern:** Voss et al. 2014 (Nat Neurosci 17:810) is the **tACS induction** study (25/40 Hz stimulation elevating lucidity ratings) — its gamma increases are stimulation-driven, not observations of spontaneous lucid onset. The observational elevated-frontal-gamma finding is Voss et al. **2009** (Sleep 32:1191), and even that paper does not, to my knowledge, characterize onset as "gradual rather than step-like." Could not read either full text to settle the gradual/step claim, so graded SUSPECTED: the citation is very likely the wrong Voss paper, and the "gradual" characterization needs a source.
- **Minimal repair:** Cite Voss et al. 2009 for observational gamma elevation, and either source or delete "gradual… rather than step-like."

---

## Arithmetic defects

1. **Internal inconsistency, line 979 (§8.9, seventh banked result):** "moves downstream *R²* from −0.001 to 0.640 (paired +0.403, s.e.m. 0.027, *t* = 14.6, five seeds)." The endpoint difference is 0.640 − (−0.001) = **0.641**, not 0.403. The t-statistic is internally consistent with the paired value (0.403/0.027 ≈ 14.9 ≈ t), so the +0.403 is presumably a mean paired difference computed over something other than these two endpoint means (medians? per-seed pairing on a different contrast?) — but as written, the parenthesis contradicts the sentence it annotates. Check against Gruber (2026d) and either reconcile the two numbers or label what each is.
2. **Verified clean:** 2159/195 = 11.07 → "elevenfold" ✓ and 6048/2159 = 2.80 → "a further factor of under three" ✓ (line 981 — this is the corrected version of the earlier "order of magnitude" defect; the repair holds). 74.0/14.0 = 5.29 → "5.3×" ✓; 71.5/12.0 = 5.96 → "6.0×" ✓ (line 981). 3.20/1.05 = 3.05 → "triples" ✓ (line 1003, though the numbers' provenance is Finding 8). Casarotto 94.7% ↔ 36/38 MCS ✓. Rank-k channel cost "2kN rather than N²" ✓ (line 419). Li et al. 4.5 min and >1,000 participants ✓. Hengen & Shew "~140 datasets" ✓ (exactly 140). Toker "over 680,000" ✓ (with the nuance that these are 680,000 **ten-second samples**, not independent recordings — consider "samples").

## Known repairs re-confirmed (do not re-report)

- **Wigner 1961 → 1962**: still present in NoC (lines 268, 751), full-tracked (lines 344, 1022), cc variant, and references.bib. Not in the master .md (no Wigner citation there).
- **Penrose & Hameroff 1994**: the master correctly cites Hameroff & Penrose (1996) (lines 997, 1282). The nonexistent joint 1994 version is still present in NoC (lines 485, 697), full-tracked (713, 966), cc variant, and references.bib. Awaiting author, per docs/pending-s305-bib-gate.md.

## Registry cross-check (didactic-patterns.md)

- **Meisel 2012 caution** — partially honored: no "supercritical"/"Class-2"/"dominant hypersynchrony" claims survive in the seizure passages (S300 verdict incorporated), but the no-GTC-coverage limit is breached twice (Finding 10).
- **Pattern 32 (holography)** — paper remains correct (§5.2 attributes distributed storage to implicit models only), as recorded ✅ in the registry.
- **Withdrawn Domhoff & Fox continuum, Schultz & Cole, Terhune, Sikka, dream/two-tags (pattern 34)** — none present in the master; nothing withdrawn is still being asserted. The pattern-34 material is correctly still un-placed (AIW-193(i)).
- **"Consistent with, never as a test" discipline** — the metacognition reanalysis (§9 OQ4) and convergence sections use "consistent with" correctly in framing; the defects there are number-attribution, not framing.

## Coverage — citations checked and found CLEAN

Verified against primary sources (abstract minimum; full text where quantitative):

- **Casarotto et al. 2016** (line 160): benchmark composition (waking; dreaming and ketamine as disconnected consciousness; NREM + midazolam/xenon/propofol as unconscious), 100% benchmark accuracy, PCI* = 0.31, 94.7% MCS sensitivity — all accurate.
- **Priesemann et al. 2014** (lines 174, 194, 451, 468, 472): σ ≈ 0.98 — the paper's best-matching driven slightly subcritical models have α ≈ 0.98–0.99; accurate.
- **Beggs & Plenz 2003** as used at lines 451/472 ("neuronal avalanches… in cortical tissue"; −3/2 exponent) — accurate there (the defect is only the "cat" attribution at line 777).
- **Hengen & Shew 2025** "~140 datasets" figure itself — exact (140 avalanche distributions, 73 papers).
- **Chowdhury et al. 2026** (lines 572, 652, 753): 19–45 Hz central-thalamic oscillation, present waking + REM, absent NREM, from DBS-implanted epilepsy patients — accurate, including the paper's own careful caveat that one band ≠ a 40/20 Hz two-loop confirmation.
- **Li et al. 2025** (line 893): >1,000 participants (1,011 + validation cohort), bifurcation/tipping point with critical slowing, 4.5 min before conventional sleep onset — all accurate.
- **Xu et al. 2024** (line 891): continuous 10–14 day recordings, wake degrades criticality, sleep restores — accurate (note: rat visual cortex; species unstated in FMT text — cosmetic).
- **Meisel et al. 2013** (line 891): fading criticality during sustained human wakefulness — accurate.
- **Mago et al. 2025** (line 520): arXiv 2511.20990 exists; jhana → increased signal diversity, reduced chaoticity, near-critical shift — accurately characterized (and correctly labeled a preprint).
- **Katlowitz et al. 2026** content claims (semantic/lexical discrimination, prediction, plasticity) — accurate (defect 15 concerns only the anesthetic-context description).
- **Toker et al. 2026** (lines 683, 887): adversarial AI, >680,000 electrophysiology samples, basal-ganglia indirect-pathway + inhibitory cortical wiring mechanisms — accurate.
- **Alnagger et al. 2026** (line 652): virtual clinical trial, individualized whole-brain models, simulated LSD/psilocybin shift DoC dynamics toward criticality — accurate (the "strongest in minimally conscious patients" detail not independently verified but consistent with coverage).
- **Passos-Ferreira & Chalmers 2026** (line 782): majority (75%) credit newborns with consciousness; pluralities: consciousness prenatal after ~24 weeks (44%), self-consciousness postnatal after ~6 months (49%) — accurate, and correctly framed as expert opinion, not data.
- **Voss et al. 2014** as used at line 755 (frontal gamma-band tACS induces lucid awareness; causal) — accurate (25/40 Hz tACS elevated LuCiD insight/control/dissociation).
- **Dresler et al. 2012** (line 755): prefrontal/frontolateral activation in lucid dreaming — matches the source; note the source is a combined EEG/fMRI **case study** (disclosed in the paper's own reference entry); consider "in a case study" in text.
- **Northoff et al. 2006** (line 899): meta-analysis of 27 imaging studies, cortical midline structures — accurate.
- **Fox et al. 2005** (line 899): DMN/attention-network anticorrelation — accurate.
- **Rameson, Satpute & Lieberman 2010** (line 899): implicit + explicit self-relevant processing both recruiting MPFC/PCC (DMN) — accurate ("2×2 factorial" is a slight idealization of a two-task schematic/non-schematic design; n=18).
- **Rouault et al. 2018** headline finding (symptom dimensions shift metacognition, not performance; n=498 in Expt 1) — accurate (defect 8 concerns only the 22% figure).
- **Dehaene & Naccache 2001; Dehaene et al. 2006** (ignition/P3b) — accurate.
- **Boly et al. 2012** (propofol thalamocortical connectivity breakdown; lines 164, 429, 737) — accurate.
- **Massimini et al. 2005** (TMS-evoked propagation wake vs NREM) — accurate.
- **Casali et al. 2013** (PCI threshold, complexity collapse under propofol with preserved structure) — accurate.
- **Alkire, Hudetz & Tononi 2008** (line 257) — accurate.
- **Kanders, Lorimer & Stoop 2017** (line 977): avalanche and edge-of-chaos criticality need not co-occur — accurate (it is the paper's title).
- **Kawakita et al. 2025** existence/method (GWOT, label-free, color similarity) — accurate apart from the individual/group issue (defect 5).
- **Nieder et al. 2020** (line 765): corvid pallium single neurons tracking perceptual report — accurate.
- **Hampton 2001; Prior, Schwarz & Güntürkün 2008** (line 775) — accurate to the cited papers (note: magpie MSR has later failed replications; not an error against the cited source).
- **Mukhametov, Supin & Polyakova 1977** (line 776): unihemispheric sleep EEG asymmetry in dolphins — accurate (criticality language clearly FMT's own gloss).
- **Owen et al. 2006** (line 683) — accurate.
- **Siclari et al. 2017** (lines 678, 735, 751): posterior hot zone predicting dream reports independent of stage, real-time prediction — accurate.
- **Steriade et al. 2001** (up-states, line 753) — accurate.
- **Koenig-Robert & Pearson 2019; Soon et al. 2013** (line 590): imagery content/abstract intention decodable seconds before conscious decision — accurate.
- **Schurger et al. 2012** (line 572): RP as stochastic accumulation — accurate.
- **Libet 1985** "350–500 ms" RP-to-awareness interval — within the standard reading of Libet's type-II RP data.
- **Miller 1956 / Cowan 2001** (7±2, 4±1; line 423) — accurate.
- **Clauset, Shalizi & Newman 2009; Touboul & Destexhe 2017; Hardstone et al. 2012** (power-law caveats, DFA range) — accurate.
- **Ölveczky, Andalman & Fee 2005; Chew et al. 2019; Maye et al. 2007** (line 522) — accurate to sources ("removes trial-to-trial variability" slightly strong for LMAN inactivation = strong reduction; Maye et al. is Drosophila, species unstated — cosmetic).
- **Kenet et al. 2003; Merabet et al. 2004; Baylor et al. 1979/1980** (dark-noise phosphenes, line 504) — accurate and carefully hedged.
- **Aru, Suzuki & Larkum 2020** (line 494) — accurate.
- **Tononi, Sporns & Edelman 1994 (C_N); Tononi & Edelman 1998** (line 480) — accurate, and the priority disclaimer is exemplary.
- **Barrett & Mediano 2019** (Φ ill-defined for non-Markovian systems, line 831) — accurate, including IIT's interventional-TPM reply.
- **Doerig et al. 2019** (unfolding argument, line 847) — accurate.
- **COGITATE 2025; IIT-Concerned 2025; Tononi et al. 2025; Gomez-Marin & Seth 2025** (line 31) — accurate.
- **Hohwy & Seth 2020** substance (PP as basis for NCC identification, not itself a theory of consciousness) — accurate in paraphrase (defect 1 is the quotation only).
- **Fleming & Lau 2014** (near-independence of metacognitive efficiency from performance "well established", line 1003) — fair.
- **Rahnev et al. 2020** Confidence Database (2,752 participants across 20 perceptual datasets, pooled r) — declared as the paper's own reanalysis; internally consistent; not checkable against a published number, and honestly framed.
- **Güntürkün & Bugnyar 2016; Godfrey-Smith 2016; Barron & Klein 2016; Birch et al. 2020** (§6.4) — accurate to the cited reviews (minor: "parrots… mirror self-recognition" at line 624 lumps parrots into an ability shown, in the cited literature, only in magpies).
- **Weiskrantz 1986; Phillips 2021** (blindsight + degraded-vision debate, line 788) — accurate, caveat properly carried.
- **Milinkovic & Aru 2025; Beni 2026; Bayne et al. 2024; Kirkeby-Hinrup et al. 2025b; Laukkonen et al. 2025; Fleming & Shea 2024 / Ellia & Tsuchiya 2025; Safron 2020/2022; Storm et al. 2024; Bach & Sorensen 2026; Fitz 2025** (§7.3) — existence and gist verified or consistent with listed metadata; characterizations are hedged and attribution-safe as written.
- **Gruber self-citations (2015, 2026a–d)** — not audited for content (self-authored).

**Not reached / not independently verifiable:** Bieberich 2026 (bioRxiv, nonstandard DOI prefix 10.64898 — worth a bibliographic check, though existence-gate territory); the "effects strongest in MCS" detail of Alnagger et al. 2026; Voss et al. 2014 full text (Finding 16); Gruber 2026d internals backing §8.9 (arithmetic item 1); the Kawakita iScience final-version wording (methods verified via the shared preprint/press full-text search, participant-group numbers from the published methods).
