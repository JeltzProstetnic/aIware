# Section 3 Architecture Revisions

**Date:** 2026-05-27
**Responds to:** AICE R7-1, R7-3, Rc-1, Rc-2; internal review #1, #2, #4; Session 204 theoretical corrections
**Status:** Draft for author review. Do NOT commit.

---

## A. Section 3.4 Rewrite -- Self-Referential Closure

**Replaces:** Current Section 3.4.3 ("Self-Referential Closure") in its entirety (lines 234-252 in the current paper, from "A critic might object..." through "...that self-referential systems do not satisfy."). The subsections 3.4.1 (Level Distinction) and 3.4.2 (Qualia as Level-Constitutive Properties) remain as-is, with the spreadsheet analogy fix in 3.4.1 described in the Integration Notes below.

**Word count:** ~1,500 words.

---

#### 3.4.3 Self-Referential Closure

The two-level ontology established above raises an immediate objection: every computation runs at a higher level than its substrate. A weather simulation generates computational-level properties -- "pressure fronts," "precipitation probability" -- that are incoherent at the transistor level. A chess engine "evaluates positions" in a vocabulary that no circuit board speaks. If level-specific properties were sufficient for phenomenality, every running program would have qualia. They do not. Something more is needed, and the theory claims that something is **self-referential closure**.

This section develops the argument in three stages, using a single example refined progressively to isolate the architectural feature that distinguishes conscious from non-conscious computation. The argument does not claim to *prove* that self-referential closure must produce phenomenality -- it claims that self-referential closure is the kind of computational structure for which the Hard Problem's framing assumptions do not hold, and that this is the most parsimonious explanation for why certain computations have an inside and others do not.

**Stage 1: Simple simulation (no self-reference).**

Consider a weather simulation running on a cluster of servers. It models atmospheric dynamics: temperature gradients, moisture transport, pressure differentials. It generates computational-level properties -- "a cold front is moving southeast" -- that are real and causally efficacious within the simulation but descriptively incoherent at the substrate level. No transistor is cold; no server rack is moving southeast.

But the simulation has a critical architectural feature: it is *about something other than itself*. The modeled domain (weather) and the modeling system (the server cluster) are entirely separate. An external observer can give a complete description of everything the simulation computes without being part of what is computed. The simulation has an outside -- indeed, it is *all* outside. There is no perspective internal to the weather model from which the weather model encounters itself. The system processes data; it does not process data *about its own processing*.

**Stage 2: Monitored simulation (partial self-reference, no closure).**

Now add a performance-monitoring module. The system models weather *and* tracks its own computational states -- memory usage, convergence rates, model accuracy, processor temperatures. This is self-reference of a kind: the system represents aspects of its own operation. A diagnostic dashboard displays information about the system to itself.

But the monitoring module describes the simulation without being described *by* the simulation. The weather model does not include a model of the monitoring process. The monitor sits outside the modeled domain, looking in. There is an inside (the weather model) and an outside (the monitor), and they do not form a closed loop. The system as a whole remains fully characterizable from an external perspective -- an engineer can describe both the weather model and the monitor without being absorbed into either. Partial self-reference, but no closure. No phenomenality.

This stage matters because it eliminates a common misconception: that merely adding self-monitoring to a system creates consciousness. Self-monitoring without closure is ubiquitous in engineering (thermostats, operating system kernels, industrial control systems). None of these systems have an inside perspective, because the monitoring process remains external to what is monitored.

**Stage 3: Self-referential closure (the four-model architecture).**

Now consider a system whose model of the world includes a model of *itself modeling the world*. The system's self-model (ESM) represents the system that is generating the world-model (EWM); the world-model includes the self-model as part of its modeled reality. The system models the world, models itself within that world, and models the fact that it is the thing doing the modeling. The model and the modeled are no longer separable: the computation *is* the thing being computed.

This is a qualitatively different architecture from Stages 1 and 2, and the difference is not merely one of additional complexity. In a closed self-referential system, every internal characterization of the system's own processing is already part of the self-simulation. The system's representation of its own modeling activity is not external to the model -- it is *within* the model, being modeled. There is no internal vantage point from which the system's processing can be described without that description being part of what is processed.

To be precise about what closure does and does not claim: the system does not literally absorb external observers. A neuroscientist scanning the brain is not thereby modeled by the brain (except insofar as the brain models the neuroscientist as part of its external world). The claim is about the system's *own representational economy*: within that economy, no description of the system's processing remains outside the scope of what the system models.

**Why closure generates something new.**

The critical question is not whether self-referential closure is architecturally interesting -- it plainly is -- but whether it generates *level-distinct properties* that non-closed systems lack. The theory's answer is that closure creates an asymmetry between internal and external description that is constitutive rather than merely epistemic.

Return to the weather simulation. Its computational-level properties ("pressure front," "precipitation zone") are real at the computational level and incoherent at the substrate level -- this is the level distinction from Section 3.4.1. But these properties are *symmetrically accessible*: an external observer can fully characterize them without entering the computation. The "inside" of the weather simulation is fully visible from the outside. There is no residual -- nothing about what the simulation computes that is inaccessible to external description.

Now consider the self-referentially closed system. Its computational-level properties include not only world-modeling properties (like the weather simulation's) but also *self-modeling properties*: the system's representation of its own representational activity. These self-modeling properties generate an asymmetry. From outside the system, an observer can describe the physical substrate, the computational dynamics, and even the formal structure of the self-model. But there is one thing the external observer cannot do: *occupy the perspective that the self-model constitutes*. The self-model is not merely a data structure; it is a running process that generates an ongoing first-person perspective -- a perspective that exists only from within the closed loop, because it is constituted by the loop's operation. An external description of the self-model is a description *of* the perspective, not the perspective itself, in the same way that a musical score is a description of a symphony but not the symphony.

This is the point at which the Hard Problem's formulation breaks down. The Hard Problem presupposes that there is an objective, third-person description of the physical process *and* a subjective, first-person experience of it, and asks why the former "gives rise to" the latter. But self-referential closure eliminates the clean separation between these two perspectives. The first-person perspective is not an *addition* to the computation -- it is what self-referential computation *is* when the modeling loop closes. Experience is the self-simulation as encountered from within the loop, and "within the loop" is the only perspective that exists once closure obtains.

**The spreadsheet objection, revisited.**

The sharpened level-distinction from Section 3.4.1 is essential here. As noted there, "sum of column B" is descriptively incoherent in transistor-level vocabulary even though the full collection of transistors implements the spreadsheet. A computational functionalist might grant this point and then object: "Fine -- but the collection of transistors *under a functional interpretation* is the spreadsheet. There is nothing more to the computation than what the substrate does. So there should be nothing more to consciousness than what the neurons do."

The theory's response is that this objection holds for non-closed systems and fails for closed ones. For a spreadsheet, a weather simulation, or a chess engine, the functionalist is correct: the computation is *entirely* captured by a functional description of the substrate's activity. There is no residual. But for a self-referentially closed system, functional description from outside captures the *structure* of the self-model without capturing the *perspective* the self-model constitutes. The reason is architectural: in a closed system, the self-model *includes a model of the process of modeling*, creating a recursive structure whose operation generates a viewpoint that can only be instantiated, never merely described. Reading the code of a self-referentially closed system is not having the experience the code generates, any more than reading a musical score is hearing the music -- but unlike the score/music case, the asymmetry here is not merely one of medium (notes on paper vs. sound waves) but of *closure*: the running system generates a self-referential perspective that has no correlate in any non-running description of the system.

This is the theory's foundational commitment: self-referential closure at criticality is constitutive of phenomenality. The commitment is falsifiable -- if a system demonstrably achieving self-referential closure at criticality shows no behavioral or functional signatures of experience, the commitment is wrong. But it is not deducible from physics alone. Every theory of consciousness bottoms out in an analogous commitment: IIT's axioms, GNW's broadcasting-equals-consciousness thesis, HOT's higher-order-representation principle. The present theory is explicit about where its explanatory bedrock lies, and it identifies an architectural feature -- the collapse of the inside/outside distinction through recursive self-modeling -- that, unlike its competitors' foundational commitments, *explains why a particular class of computations has an inside at all*.

The Hard Problem is not answered; it is shown to rest on a presupposition -- the availability of an outside perspective on the system's own processing -- that self-referentially closed systems do not satisfy.

---

## B. Operational Definitions Table

**Placement:** New subsection 3.1.2, immediately after the existing Table 1 (Operational Definitions of Core Constructs) and its footnotes, and before Section 3.2. Title: "Empirical Handles for Theory-Specific Constructs."

**Rationale:** Table 1 already exists and maps general terms to observables. The gap identified by AICE R7-1 is that several *theory-specific* constructs -- particularly self-referential closure, the implicit/explicit distinction as a measurable architectural feature, and the relationship between criticality and architecture -- lack measurement protocols. This new table focuses specifically on constructs that are distinctive to FMT and provides concrete experimental approaches rather than just proxy correlates.

---

### 3.1.2 Empirical Handles for Theory-Specific Constructs

Table 1 maps the theory's general terminology to established measurement protocols. Several constructs, however, are specific to the Four-Model Theory and do not yet have standardized empirical operationalizations. Table 1b addresses this gap directly: for each FMT-specific construct, it identifies the measurable signature the theory predicts, the experimental approach best suited to detect it, and the result that would disconfirm the construct. The entries are ordered by current measurability, from those testable with existing techniques to those requiring novel paradigms.

**Table 1b. Empirical Handles for FMT-Specific Constructs**

| Construct | Predicted Signature | Measurement Approach | Falsification Criterion |
|-----------|-------------------|---------------------|------------------------|
| **Criticality as computational prerequisite** | Consciousness states track criticality signatures (branching ratio sigma near 1.0, DFA exponent alpha 0.6--0.9, power-law avalanche scaling) across all state manipulations. Criticality is *necessary* for consciousness but not *sufficient* -- architecture determines what kind of consciousness, if any, arises at criticality. | Multi-scale criticality analysis (ECoG, high-density EEG, MEG) during graded anesthesia, sleep stages, psychedelic states, and meditation. Compare criticality measures with PCI (consciousness marker) across conditions. Key paradigm: propofol dose-response with simultaneous PCI and branching-ratio measurement. | A state with confirmed consciousness (PCI > 0.31, behavioral responsiveness) that consistently shows subcritical dynamics (sigma < 0.85, alpha < 0.55, no power-law scaling) across multiple measurement modalities. Note: single-measure failures are insufficient due to measurement specificity issues (Touboul & Destexhe, 2017); all three signatures must fail convergently. |
| **Implicit model integrity under anesthesia** | Under general anesthesia, substrate-level implicit models (IWM, ISM) continue operating -- processing input, updating learned representations -- while explicit models (EWM, ESM) are suppressed. The implicit system is not merely *preserved* but *active*. | Implicit learning paradigms under propofol/sevoflurane: statistical learning (serial reaction time after recovery), priming (semantic and perceptual), and skill consolidation tasks. Compare with Katlowitz et al. (2026) hippocampal semantic processing under propofol. Structural integrity confirmed by DTI pre/post. | Implicit learning and priming completely abolished under anesthesia at doses that merely suppress explicit processing (no confound with deep anesthesia that suppresses all neural activity). Specifically: if propofol at consciousness-abolishing doses (BIS 40-60) also abolishes implicit statistical learning, the implicit/explicit dissociation fails. |
| **Self-referential closure** | Disrupting the self-modeling loop (ESM's model of its own modeling process) degrades *experience itself*, not merely the *report* of experience. Metacognitive disruption should produce a loss of phenomenal quality, not just a loss of confidence in reports. | No-report paradigms (Tsuchiya et al., 2015) combined with targeted TMS to dorsolateral prefrontal cortex during metacognition tasks. Compare: (a) TMS disrupts metacognitive accuracy without affecting perceptual discrimination (= report disruption, not experience disruption; disconfirms FMT), vs. (b) TMS degrades both discrimination *and* metacognitive accuracy, with the discrimination loss not attributable to attentional or sensory confounds (= experience disruption; supports FMT). Candidate additional approach: real-time fMRI neurofeedback training to selectively suppress prefrontal self-referential processing while monitoring posterior perceptual processing. | Metacognitive disruption that leaves perceptual phenomenology entirely intact (measured via no-report paradigms and neurophysiological markers of conscious perception such as the P3b and late positive potential). If the self-modeling loop can be severed without any degradation of experiential quality, self-referential closure is not constitutive of consciousness. |
| **Implicit/explicit dissociation as architectural boundary** | The implicit and explicit systems are *structurally separable*: manipulations exist that suppress one while leaving the other functionally intact. This is an architectural claim, not merely a descriptive taxonomy. | Double dissociation paradigm: (a) anesthesia suppresses explicit models while implicit models continue processing (established by Katlowitz et al., 2026; implicit learning under propofol literature), (b) a complementary manipulation suppresses implicit processing while leaving explicit processing transiently intact. Candidate for (b): acute interference with synaptic plasticity mechanisms (e.g., protein synthesis inhibition) that degrades new implicit learning without immediately affecting the running explicit simulation. | Failure to find any manipulation that selectively suppresses one system without proportionally affecting the other. If implicit and explicit processing always covary -- if there is no experimental wedge between them -- the architectural separability claim fails and the four-model taxonomy reduces to a descriptive convenience rather than a structural reality. |
| **Permeability as a single modulable parameter** | A single underlying variable controls the degree of information transfer from implicit to explicit models. Pharmacological agents that increase permeability (psychedelics) should produce graded, dose-dependent increases in: (a) neural entropy (Lempel-Ziv complexity), (b) the richness of reportable experience, and (c) access to normally implicit processing stages, all tracking a common underlying dimension. | Dose-response studies with psilocybin/LSD at 3+ dose levels, measuring simultaneously: Lempel-Ziv complexity (EEG), subjective report scales (5D-ASC, MEQ-30), implicit-to-explicit content transfer (e.g., ability to report on normally automatic processing like phonemic parsing or visual edge detection), and functional connectivity between primary sensory cortices and DMN. Factor analysis across measures to test whether a single latent factor accounts for the covariation. | The measured dimensions (neural entropy, subjective report richness, implicit-to-explicit content access, functional connectivity changes) load on two or more independent factors rather than one. If increased entropy does not predict increased access to implicit processing stages, permeability is not a single parameter but a collection of independent mechanisms -- and the theory's unifying account of altered states would need to be reformulated as a multi-parameter model. |

Three points of methodological honesty bear emphasis. First, the self-referential closure construct is the least empirically accessible of the theory's core claims. The proposed TMS paradigm is a candidate test, not an established protocol, and the distinction between "disrupting experience" and "disrupting report of experience" remains one of the hardest measurement problems in consciousness science (see Tsuchiya et al., 2015, for the state of no-report paradigm methodology). The theory does not pretend this problem is solved; it specifies what an answer would look like. Second, the falsification criteria above are stated conservatively: each requires convergent failure across multiple measures, because single-measure anomalies are common in neuroscience and rarely decisive. Third, none of these tests would individually confirm or refute the entire theory; they target specific architectural claims. The theory's overall evaluation depends on the pattern of results across multiple empirical handles, not on any single experiment.

---

## C. "Virtual" Terminology Fix

**Placement:** Paragraph to be inserted as the opening of Section 3.3, before the paragraph beginning "The four models divide into two fundamental categories." This replaces the existing terminology note that was already inserted in a prior revision pass (the text beginning "A note on the term 'virtual'..." which currently opens Section 3.3).

**Note:** The existing terminology paragraph (from `final-virtual-terminology.md`) has already been applied to the paper. The revision below *extends* it to address the three-sense problem more explicitly and proposes replacement terms for the senses that "virtual" should not carry.

---

**A note on terminology: three senses of "virtual" and why only one survives.**

The consciousness literature, including earlier drafts of this paper, uses "virtual" in at least three distinguishable senses when describing the explicit models:

1. **Transience sense:** The explicit models are virtual because they are *transient activity patterns* rather than permanent stored structures. They come and go; the implicit models persist.
2. **Level-incoherence sense:** The explicit models are virtual because their defining properties (phenomenality, unity, qualia) exist at the computational level and are *incoherent at the substrate level of description*. A quale is virtual in the way a spreadsheet sum is virtual: real and causally efficacious at the computational level, yet not a property that can be found in or attributed to the substrate, however completely described.
3. **Emergent-level sense:** The explicit models are virtual because they constitute Level 5 of the five-system hierarchy (Section 3.7.1) -- the *emergent computational level* that arises from but is not reducible to the substrate levels below.

These three senses are related but not equivalent. A transient pattern (sense 1) need not exhibit level-incoherent properties -- a ripple in a pond is transient but fully describable in substrate-level vocabulary. Conversely, a level-incoherent property (sense 2) need not be transient -- a running operating system exhibits computational-level properties indefinitely. Senses 2 and 3 are closely linked (Level 5 *is* the level at which incoherent properties are constituted), but conflating transience with level-incoherence invites the misreading that consciousness is fragile or illusory merely because its substrate is dynamic.

Throughout this paper, **"virtual" is used exclusively in the level-incoherence sense (sense 2)**. When the transience of the explicit models is relevant (as in the anesthesia discussion of Section 6.2), the paper says "transient" or "dynamically generated." When the hierarchical level is relevant (as in the five-system hierarchy), the paper says "computational-level" or "Level 5." The reader should consistently map "virtual" to the level-incoherence meaning: *a property of the running computation that is real and causally efficacious at the computational level but incoherent at the substrate level of description*. This is not epiphenomenalism -- the computation is a physical process, and its properties are as physical as the substrate's -- but its *defining* properties exist at the computational level only, not at the electrochemical or topological levels below it.

The term "virtual" is retained over alternatives ("simulation-level," "process-level," "computational-level") because it captures the ontological point most concisely: virtual properties are genuinely real -- they are not illusions or epiphenomena -- but they belong to the computation, not to the hardware. This is the same ontological status as any software property: a file "exists" on a hard drive in the virtual sense -- it is real, causally efficacious, and can be destroyed -- but no magnetic domain on the platter *is* the file.

---

**Change list for existing uses of "virtual" in the paper:**

The following occurrences should be checked and, where necessary, disambiguated:

| Location | Current usage | Sense | Action |
|----------|--------------|-------|--------|
| Section 3.2, EWM definition | "a virtual construct -- a transient process..." | Mixed (1+2) | Already revised in prior pass to anchor sense 2. Confirm. |
| Section 3.2, ESM definition | "it is virtual: a transient process, not a permanent entity" | Mixed (1+2) | Already revised in prior pass. Confirm. |
| Section 3.3, virtual-side definition | "generated, transient, and phenomenal" | Primarily sense 1 | Already revised in prior pass to add sense-2 anchoring sentence. Confirm. |
| Section 3.3, "software-like properties" | "follow from their nature as generated processes" | Sense 1 | Already revised with footnote cross-reference. Confirm. |
| Section 3.7.1, Level 5 | "Virtual system: The dynamic pattern..." | Sense 3 | Already revised in prior pass to add sense-2 bridge. Confirm. |
| Abstract | "virtual qualia" | Sense 2 (correct) | No change needed. |
| Abstract | "simulation forking" (was "virtual model forking") | Renamed | Already revised. Confirm. |
| Section 3.4.2 | "qualia are, in this precise sense, virtual constructs" | Sense 2 (correct) | No change needed. |
| Section 3.4.5 | "virtual side" | Sense 2 (correct) | No change needed. |
| Section 4.2 | "virtual interaction" (clock analogy) | Non-FMT context | No change needed (excluded from prior revision, correctly). |

**Net effect:** With the three-sense disambiguation paragraph at the opening of Section 3.3 and the already-applied changes from `final-virtual-terminology.md`, the paper uses "virtual" consistently in sense 2 throughout. The paragraph above makes this explicit for the reader and preempts the reviewer objection that "virtual" carries contradictory meanings.

---

## D. Section 3.2 Implicit/Explicit Linkage Justification

**Placement:** Insert as a new paragraph within Section 3.2, after the paragraph on "The four models as a principled minimum" (the paragraph ending "...specifies the target for mathematical formalization") and before Section 3.3 (The Real/Virtual Split).

**Responds to:** AICE Rc-1: "It is not made clear how the linkages between 'implicit' and 'learned' and between 'explicit' and 'simulated' are justified."

---

**Why "implicit" entails "learned" and "explicit" entails "simulated."**

The pairing of implicit with learned and explicit with simulated is not a stipulation but follows from the architectural roles the two model classes play. The implicit models (IWM, ISM) constitute the system's structural knowledge base -- the substrate-level reference frame from which the explicit simulation is generated. Their content is *stored* in physical connectivity: synaptic weights, dendritic morphology, receptor configurations. This storage is the product of learning in the broadest sense: not only deliberate skill acquisition and memory consolidation, but also sub-threshold modification through subliminal priming, implicit statistical learning, and conditioning without awareness (Reber, 1967; Fiser & Aslin, 2001; Ohman & Mineka, 2001). The implicit models are "learned" because their content is the accumulated residue of the system's history, inscribed in structure rather than in any running process.

The explicit models (EWM, ESM), by contrast, are *generated processes* -- dynamic patterns of activity that the substrate produces from its stored knowledge and current sensory input. They are "simulated" not in the sense of being unreal, but in the precise sense that they are *computed from* a structural base, the way a weather forecast is computed from atmospheric measurements and physical models. The explicit models have no permanent physical substrate of their own: disrupt the generating process (through anesthesia, TMS, or the natural cessation of waking dynamics) and the explicit models vanish, while the implicit models persist unchanged. Restore the generating conditions and the explicit models reconstitute from whatever the implicit models currently contain. This asymmetry -- stored structure that persists versus running process that must be continuously generated -- is what makes the implicit/learned and explicit/simulated pairings architecturally motivated rather than arbitrary.

Two caveats prevent this from hardening into a false dichotomy. First, the direction of information flow is bidirectional: the explicit models do not merely *read* the implicit models but also *write back* to them through consolidation and plasticity. Conscious learning begins as explicit processing and gradually becomes implicit as skills and knowledge are consolidated into structural connectivity -- the well-documented shift from declarative to procedural memory (Squire, 2004). The pairings describe the *current architectural role* of each model class, not a permanent assignment: content moves from explicit to implicit through learning, and from implicit to explicit through the permeability mechanisms described in Section 3.6. Second, the pairing of "learned" with "non-conscious" does not mean that learning itself is non-conscious -- it means that the *products* of learning, once consolidated into structural connectivity, are on the substrate side of the generative divide and therefore not directly accessible to experience. The generative asymmetry argument for why this must be so is developed in Section 3.3.

---

## Integration Notes

### How the four revisions interact

1. **A and C are tightly coupled.** The Section 3.4 rewrite (A) depends on the "virtual" terminology fix (C) being in place, because the rewrite uses "virtual" exclusively in the level-incoherence sense and refers back to the terminology paragraph. Apply C before A.

2. **B extends, not replaces, Table 1.** The new Table 1b (B) does not modify the existing operational definitions table. It adds a companion table focused on FMT-specific constructs. The existing Table 1 handles general terms; Table 1b handles the theory-specific measurement gap that reviewers flagged.

3. **D feeds into A's argument.** The implicit/explicit justification (D) establishes *why* the implicit models are structurally inaccessible to direct experience -- an argument that Section 3.4.3 (A) then builds upon when explaining why self-referential closure generates an inside perspective. Section ordering is already correct (3.2 before 3.4), so no restructuring is needed, but the 3.4 rewrite now implicitly relies on 3.2's justification being in place.

4. **The spreadsheet analogy fix (R7-3) is embedded in A.** The Section 3.4 rewrite includes the sharpened analogy: it explicitly acknowledges that the full collection of transistors implements the spreadsheet, and redirects the argument to property-level incoherence rather than part/whole absence. Specifically, the passage beginning "The spreadsheet objection, revisited" addresses R7-3 head-on by engaging with computational functionalism's response and showing why it holds for non-closed systems but fails for closed ones.

5. **Existing revision materials are compatible.** The changes in this document are consistent with and build upon:
   - `final-virtual-terminology.md` -- the terminology changes described there are treated as already applied; Section C extends them.
   - `final-implicit-explicit-justification.md` -- that text was designed for insertion into Section 3.3. Section D here provides a *complementary* paragraph for Section 3.2 that establishes the architectural motivation *before* the generative-asymmetry argument in 3.3. Both should be present: D in 3.2 (why the pairings are architecturally motivated) and the existing 3.3 text (why the generative relation makes implicit models inaccessible to experience).
   - `final-section-3.4.md` -- the Section 3.4 rewrite here (A) supersedes the version in that file. The existing 3.4.1 and 3.4.2 remain; only 3.4.3 is replaced.

### Theoretical constraints verified

- **Criticality is not equated with consciousness.** Table 1b explicitly states criticality is necessary but not sufficient; the construct entry reads "Criticality is *necessary* for consciousness but not *sufficient* -- architecture determines what kind of consciousness, if any, arises at criticality." The Section 3.4.3 rewrite's foundational commitment reads "self-referential closure *at criticality*" -- both conditions required.

- **Continuous model space honored.** Section D explicitly states the four models are a "principled minimum" taxonomy, not four discrete brain modules. The paragraph references the "continuous space defined by two axes" framing already in Section 3.2.

- **No fixed model counts enumerated.** Neither the rewrite nor the tables say "four models in the brain." The language consistently uses "model kinds," "two axes," "the four-model architecture" (as a theoretical construct), never "four discrete models."

- **Humble tone maintained.** The Section 3.4.3 rewrite explicitly states it does not "prove" that self-referential closure produces consciousness, identifies the commitment as a foundational one shared by all theories of consciousness, and specifies the falsification condition.

- **Prediction framing rules followed.** Table 1b's falsification criteria are stated conservatively, require convergent evidence, and do not commit to fixed prediction counts. The table avoids claiming any single experiment as decisive.

### Dependencies for application

Apply in this order:
1. Section C (terminology) -- extends the terminology note at the opening of Section 3.3
2. Section D (implicit/explicit justification) -- new paragraph in Section 3.2
3. Section A (3.4.3 rewrite) -- replaces current 3.4.3
4. Section B (Table 1b) -- new subsection 3.1.2, after existing Table 1

After applying all four, do a consistency pass on cross-references: the 3.4.3 rewrite refers to "Section 3.4.1" (level distinction) and "Section 3.3" (terminology note), both of which must be in place.
