<!-- AIW-281 draft manuscript. Venue-neutral. Source brief: docs/papers-moc7/theory-map-brief.md. Points for MG at the end are NOT part of the manuscript. -->

# Where the Theories Sit: An Architectural Coordinate System for Comparing Theories of Consciousness, with the Four-Model Theory as Reference Frame

**Matthias Gruber**
Independent Researcher. ORCID 0009-0005-9697-1665

## Abstract

Comparisons between theories of consciousness usually score whole theories against a list of requirements or set two theories against each other in a single experiment. Both procedures treat a theory as one unit. Most theories, however, make several claims of different kinds: some about mechanism, some about what is constitutive of experience, some about ontology and some about substrate. A theory can be right about one of these and wrong about another. This paper describes a comparison method that works at the level of atomic claims. Each claim of each theory is placed on a component of a reference architecture and given one of four verdicts relative to that architecture: absorbed, compatible, neutral, or contradicting. Every contradiction is then recorded with the experiment that would decide it, or with the statement that no empirical decider exists. The method is applied to nineteen theories and theory variants, from integrated information and global workspace theories to illusionism and enactivism, with the Four-Model Theory (FMT) as the reference frame. The result has a regular shape. FMT absorbs most of the mechanisms the other theories propose. The contradictions concern what is sufficient or constitutive for experience, and the ontology of phenomenal properties. Twelve contradictions are recorded. For eight, an empirical test, or an in-silico test of the architectural difference, can be specified now; two can be decided only with artificial systems that do not yet exist; for one the measurement is immature, and for one no empirical decider exists. The claim set of the reference theory is supplied as subject–predicate–object triples with dependency links, for use in graph-based comparison programmes.

**Keywords:** theories of consciousness; theory comparison; adversarial collaboration; prediction maps; Four-Model Theory; self-referential closure

## 1. Introduction

Consciousness science has more theories than decisive experiments (Seth & Bayne, 2022). The experimental paradigm a study uses predicts which theory its result supports (Yaron et al., 2022). The first large adversarial collaboration tested integrated information theory (IIT) against global neuronal workspace theory (GNW) and challenged parts of both (COGITATE Consortium, 2025). A single experiment confronts a single pair of predictions, and each theory makes many more claims than that pair.

Two comparison formats are common. Scoring theories against a list of requirements (e.g. Gruber, 2026a, §7.1) shows how much ground each covers, and does not show whether two theories that cover a requirement agree about it. Setting two theories in opposition finds disagreements and leaves agreements unrecorded. Negro et al. (2026) propose a third format: a theory becomes a network of claims and predictions with a core, a periphery and inferential edges, so that theories can be aligned claim by claim.

The method described here uses one theory with many components as a coordinate system. Every atomic claim of every other theory is placed on the component it is about and compared with the reference theory's own claim about that component. Any architecture with enough components could serve as the frame. The Four-Model Theory (FMT; Gruber, 2015, 2026a) is used because it names a component at each level the other theories address, from substrate and connectivity through dynamical regime, channel, running models, closure and recursive depth to phenomenal ontology and substrate metaphysics. The choice introduces a bias: claims are recorded only where they touch FMT's components. The hatched cells of Figure 2 mark the levels where FMT itself has no mechanism, protocol or formal model.

## 2. Method

### 2.1 Atomic claims

An atomic claim is a single subject–predicate–object statement that a theory's proponents assert and that can be true or false independently of the theory's other claims. "A state is conscious if and only if it is the target of a suitable higher-order representation" is one atomic claim; "an empty higher-order representation suffices for experience" is a second. Each claim is assigned a type: definition, principle, bridging commitment, consequence, mechanism, prediction, or falsifier. Two theories can share a mechanism and disagree on whether it is constitutive of experience; separating claims by type keeps the agreement and the disagreement both visible.

### 2.2 Placement

Each claim is placed on the component of the reference architecture that it is about: a claim about global broadcast on the component that carries content between the stored and running levels, a claim identifying experience with a cause-effect structure at the level of phenomenal ontology. Placement depends on subject matter, not on whether the reference theory agrees.

### 2.3 Verdicts

Each placed claim receives one of four verdicts relative to the reference theory's own claim about the same component.

- **A — absorbed.** The reference theory contains the claim, as a component, a mechanism, or an implementation of one of its components.
- **C — compatible.** The reference theory does not contain the claim, and the claim does not conflict with anything the reference theory asserts.
- **N — neutral.** The reference theory takes no position on the claim.
- **X — contradicts.** The claim and the reference theory's claim about that component cannot both be true.

A theory usually receives several verdicts, one per claim.

### 2.4 Contradiction records

Each X verdict is recorded in a fixed format: the point of conflict; the rival claim; the reference theory's claim; evidence that bears on the point; the experiment that would decide it; the reference theory's prediction that is linked to it; and the status of that experiment (available, in silico only, requires an artificial implementation, or no empirical decider). Where no decider exists, the record says so and names the kind of difference that remains, for example an ethical one.

### 2.5 Encoding

The reference theory's claims are encoded as triples with five further fields: section of the source text, claim type, core or periphery, and a list of the claims each one depends on. Core claims are the principles, the definition and the derivation of the architecture. Peripheral claims are mechanisms, consequences and predictions. The dependency list gives the inferential edges a prediction map requires (Negro et al., 2026). The FMT claim set is supplied as a supplementary JSON file (`fmt-claims.json`). Rival-theory claims receive identifiers of the form `GNW-1`, `IIT-2`, and the relations between them and FMT claims form the edges of Figure 3.

## 3. The Reference Frame

FMT rests on three principles (Gruber, 2026a, §3).

1. **Open-ended computation allows free modelling.** The system must be able to compute in the regime capable of universal computation (Wolfram's Class 4) and must recruit that capability for its own modelling. Free modelling is necessary and not sufficient for consciousness. In neural tissue it usually shows as near-critical dynamics. Near-criticality is a signature of free modelling in some substrates, at some task sizes. It is neither necessary nor sufficient for consciousness, and a conscious system may run subcritically (§3.7, Table 1).
2. **Recurrent non-linear dynamics of sufficient complexity host a second computational level**: persistent activity patterns that interact and compute over one another, individuated by their mutual effects (§3.3).
3. **Phenomenology is a real, physical effect on that level, and it arises where the modelling closes on itself**, where the self-model and the world-model each enter the other's update rule (§3.4). This is the theory's single bridging commitment. It is argued for and not derived (§3.4.3).

From these follows a minimum architecture of two kinds of model along two axes (§3.2). Mode separates implicit models, stored in substrate connectivity, from explicit models, generated as running processes. Scope separates the world from the self, and is a nesting: the self-model's content is part of the world-model's. The four extremal poles are the implicit world model (IWM), implicit self model (ISM), explicit world model (EWM) and explicit self model (ESM). Four is the floor; the substrate implements an effectively uncountable number of overlapping models around these poles. The explicit models are generated from the implicit models and current input. They are not filled by a copy of stored content (§3.6).

The components used as coordinates below are:

| Code | Component | Source |
|---|---|---|
| RV | Real/virtual split: implicit models are stored structure and never directly conscious; explicit models are running processes | §3.3 |
| VQ | Virtual qualia: phenomenal properties are real at the computational level and incoherent at the substrate level | §3.4.1–3.4.2 |
| CL | Self-referential closure: the self-model and world-model enter each other's update rule | §3.4.3 |
| TE | Temporal echo: recursion under closure produces experienced temporal flow | §3.4.4 |
| LAD | Graded ladder: minimal, basic, simply, doubly and triply extended consciousness by richness and depth of recursive self-modelling | §3.5 |
| PERM | Permeability: how readily stored content is drawn into the running models, a family of local and global boundary properties | §3.6 |
| CH | Channel: the low-rank path through which explicit models read and write implicit ones; its occupancy is working memory (*Arbeitsmodell*) | §3.6.1 |
| FM | Free modelling: Class-4 capability, free instantiation and autonomous recruitment; criticality as its signature in some brains | §3.7, §3.7.3 |
| L1–L5 | Five-system hierarchy: physical, electrochemical, proteomic, topological (implicit models), virtual (explicit models) | §3.7.1 |
| MP | Meta-problem: the ESM cannot model its own generating substrate | §3.8 |
| SI | Substrate independence: the architecture plus free modelling suffices on any substrate | §4.4 |

Three features of the frame govern the verdicts. First, for content in the running simulation, access and phenomenality are two level-descriptions of one process; content that is only accessible, poised for report without being in use, is preconscious: it is stored on the implicit side or held in an explicit model outside the self-model's closed loop, and it becomes conscious on entering that loop (§3.4.6; Dehaene et al., 2006). Added recursive depth converts content that is present into content that is reportable, with no separate broadcast stage (§3.4.6). Second, basic consciousness has phenomenal experience with a rudimentary ESM and without first-order self-observation; awareness that one experiences arrives at the first extended rung (§3.5). Third, FMT's claims about what closure buys a system are claims about one architecture's closure and its efficiency under a resource bound, not claims about what is barred to systems without it (§4.4). Opening a closed loop in a recurrent system tends to relocate closure, leaving two or more smaller closed systems where one stood (§4.4, §8.11).

## 4. The Map

Table 1 lists the placement and verdicts. Section numbers in the last column refer to Gruber (2026a).

**Table 1. Placement and verdicts of nineteen theories and theory variants, relative to FMT.** A = absorbed, C = compatible, N = neutral, X = contradicts. Each verdict applies to one atomic claim.

| Theory (source) | Core claim | FMT component | Verdicts | FMT ref. |
|---|---|---|---|---|
| IIT (Tononi, 2004; Tononi et al., 2016; Albantakis et al., 2023) | Experience is a maximally irreducible intrinsic cause-effect structure; Φ measures its irreducibility | CL and FM (integration, recurrence); VQ (relational structure of the quality space) | A: experience is irreducible, integrated and causally structured; recurrence is required. C: rich quality structure. X: identity with the substrate's intrinsic cause-effect power. X: every complex with Φ > 0 is conscious. X: functionally identical digital duplicate is not conscious. N: exclusion as a boundary rule | §7.2, §3.4.1, §4.4 |
| GNW (Baars, 1988; Dehaene & Changeux, 2011; Mashour et al., 2020) | Content is conscious when broadcast globally after non-linear ignition; capacity-limited | CH (workspace = channel occupancy); PERM (ignition = signature of content entering the running models) | A: workspace, capacity limit, ignition as marker. X: broadcast is constitutive. X: no ignition, no experience. N: prefrontal anatomy | §3.6.1, §3.4.6, §7.2 |
| CTM (Blum & Blum, 2022) | Formal model on workspace lines: up-tree competition, down-tree broadcast, processors including a Model-of-the-World that contains a self | CH (broadcast); EWM ⊇ ESM (world model with self) | A: world model containing a self model; formal specification. X: broadcast as constitutive. X: a machine implementing the CTM architecture is conscious, with no condition that it recruit its own capability for self-modelling. N: the internal language format | §3.6.1, §3.7.3, §8.9 |
| PP / FEP (Friston, 2010; Hohwy & Seth, 2020) | Perception is inference minimising prediction error; precision weighting | IWM/ISM dynamics; the generation of EWM/ESM | A: prediction-error machinery as the implementation of the implicit, predictive layer. C: perception as controlled hallucination. N: FEP as a general principle of self-organisation. X: PP alone as sufficient for consciousness | §7.2 |
| Beast machine (Seth, 2021; Seth & Bayne, 2022) | Selfhood is control-oriented interoceptive prediction | ISM → ESM generation from interoceptive input | A: one route to the ESM. X: the biological-naturalist rider (see Seth 2025 row) | §3.2, §4.4, §7.2 |
| REBUS (Carhart-Harris & Friston, 2019) | Psychedelics relax precision on high-level priors | PERM | A: one implementation of a global permeability change | §7.2, §8.2–8.3 |
| Beautiful Loop (Laukkonen et al., 2025) | Consciousness is a self-evidencing loop: the generative model models itself generating the model | CL | A (convergent on closure) | §7.3 |
| HOT (Rosenthal, 2005; Lau & Rosenthal, 2011; Brown et al., 2019) | A state is conscious iff a suitable higher-order representation, usually itself unconscious, targets it; on some versions an empty higher-order representation suffices | LAD; ESM; MP | A: higher-order self-modelling as the mechanism of the extended rungs. X: per-state higher-order representation as the condition of phenomenality. X: a higher-order representation in a system without closure suffices. N: conceptual or non-conceptual format | §3.5, §3.4.3, §3.4.6, §7.2 |
| PRM (Lau, 2022) | Experience occurs when a higher-order monitor marks a sensory representation as a reliable reflection of the present world | Source distinguishability (a requirement on the architecture) | A: the reality-monitoring function. X: the monitor's output as constitutive of experience | §6.0 |
| RPT (Lamme, 2006, 2010) | Local recurrent processing in sensory cortex suffices for phenomenal experience; global recurrence adds access | Generating dynamics of the EWM (Principle 2) | A: recurrence as the mechanism that hosts the running models. X: local recurrence without a self-model in the loop as sufficient. X: phenomenal overflow as phenomenality beyond access | §3.3, §3.4.3, §3.4.6, §7.2 |
| AST (Graziano, 2013, 2024; Wilterson et al., 2020) | The brain models its own attention in simplified, partly inaccurate form; claims of awareness report that model's content, and the non-physical essence it depicts does not exist | ESM (model of selection into CH); MP | A: the attention schema as part of the ESM; the meta-problem mechanism. C: attention control as the schema's function. X: deflationism about phenomenal properties | §3.8, §3.4.5, §3.6.1 |
| SMT (Metzinger, 2003, 2020) | The phenomenal self is a transparent self-model; minimal phenomenal experience may be selfless | ESM; MP (transparency ≈ observability constraint) | A: self-model as constitutive; transparency. X (verbal): "there are no selves". X (open): selfless minimal phenomenal experience | §1.3, §3.4.3, §7.4 |
| IWMT (Safron, 2020; Safron et al., 2022) | Consciousness is integrated world modelling with integrated selfhood; near-critical self-organising harmonic modes | EWM, ESM, FM | A: world and self modelling both necessary; near-critical signature. C: formal mechanism. X (mild, conditional): graded multi-factor demarcation. N: the integrated-information component | §7.3 |
| DIT (Aru et al., 2020; Suzuki & Larkum, 2020) | Coupling of apical and basal compartments of layer-5 pyramidal neurons gates consciousness; anaesthetics decouple them | L4 → L5 transition; candidate realizer of CH | A: candidate cortical implementation. N: whether it is the only realizer | §3.7.1, §3.6.1 |
| ICT (Chang et al., 2020) | Conscious processes are those that form non-trivial informational closure with respect to the environment at a coarse-grained scale; level of consciousness grows with its degree | CL; L5 | A: closure as primitive; the coarse-grained level. X: non-trivial informational closure without a self-model as sufficient. N: the information-theoretic quantities | not engaged |
| Illusionism (Dennett, 1991; Frankish, 2016) | Phenomenal properties do not exist; introspection misrepresents quasi-phenomenal properties as phenomenal | RV; MP; VQ | A: no phenomenal properties in the substrate; the mechanics of the seeming. X: no phenomenal properties at any level | §3.4.5 |
| Biological naturalism, Searle (Searle, 1980, 1992) | Brains cause consciousness by their specific causal powers; implementing a program never suffices, and simulation is not duplication | SI | C: brains produce consciousness through their biology, as one realizer. X: the right computation is not sufficient (Searle allows non-biological systems with equivalent causal powers) | §4.4 (Searle not engaged) |
| Biological naturalism, Seth (Seth, 2025) | Consciousness may depend on being alive; computation alone is probably insufficient | SI; FM recruitment; ISM → ESM | A: autonomy, self-maintenance and interoceptive self-modelling as one route. X: life, not computation, as what consciousness depends on (held by Seth as a live possibility) | §4.4 |
| Enactivism (Varela et al., 1991; Thompson, 2007) | Mind is embodied sense-making continuous with life; strong strands deny internal representation | FM recruitment; ESM ⊆ EWM boundary | C: autonomy and embodiment as conditions on recruitment. X: experience without internal models. X (conditional): mind in every living system, if mind includes experience | §3.7.3, §6.3, §6.4 (enactivism not engaged) |

The conscious Turing machine appears in Gruber (2026a, §8.9) only through its AI blueprint (Yu et al., 2026).

### 4.1 The pattern

The verdicts fall into three groups.

**Mechanisms are absorbed.** The workspace and its capacity limit become the channel and its occupancy. Recurrence becomes the dynamics that host the second level. Prediction-error minimisation becomes the implementation of the implicit layer. Higher-order self-representation becomes the mechanism of the extended rungs. Apical-basal coupling becomes a candidate cortical realizer of the step from stored to running models. The attention schema becomes part of the self-model. The self-evidencing loop and informational closure are both closure.

**Sufficiency and constitution claims are contradicted.** GNW makes broadcast constitutive; FMT makes the self-model's closure over the channel's content constitutive. RPT makes local recurrence sufficient; FMT requires the self-model in the loop. HOT makes a higher-order representation of the particular state the condition; FMT makes system-level closure the condition and places phenomenality at the basic rung, before first-order self-observation. ICT makes informational closure sufficient without a self-model. IIT makes any complex with Φ > 0 conscious.

**Ontological and substrate claims are contradicted.** Illusionism denies that phenomenal properties exist, and AST that the subjective essence depicted in claims of awareness exists; FMT holds that they exist at the computational level. Searle denies that any computation suffices, and Seth holds that consciousness may depend on being alive; FMT is substrate-independent given the architecture and free modelling. Strong enactivism denies that experience is constituted by internal models; on FMT experience is a running internal simulation.

The groups follow claim type. Because each theory carries claims of several types, a score for the whole theory cannot show this.

## 5. Contradictions and Their Deciders

One constraint applies to every record that proposes removing closure. In a recurrent system, cutting a loop at one place relocates closure and leaves two closed subsystems (Gruber, 2026a, §4.4). An experiment that intends to abolish self-referential closure must therefore show that its manipulation removed closure, not only that it opened one loop.

### C1. IIT: what the irreducible structure is

*Point.* IIT identifies an experience with the substrate's intrinsic cause-effect structure (Tononi et al., 2016; Albantakis et al., 2023). It follows that any maximally irreducible complex with Φ > 0 has some experience, and that a digital simulation of a brain on conventional hardware lacks the brain's experience despite identical function. FMT adopts IIT's diagnosis that consciousness is irreducible, integrated and causally structured, and locates that structure in the running, substrate-neutral, self-referential updating of the explicit models (Gruber, 2026a, §7.2). On FMT a complex without closure has no experience whatever its Φ, and a functionally matching implementation that runs the architecture with free modelling is conscious (§4.4, §8.9). IIT also holds that inactive but available neurons contribute to the cause-effect structure (Tononi et al., 2016); on FMT idle units contribute only through the implicit substrate.

*Evidence.* COGITATE found content-specific information in posterior cortex and did not find the sustained posterior synchronisation IIT predicted (COGITATE Consortium, 2025). The unfolding argument applies to both theories (Doerig et al., 2019; Gruber, 2026a, §7.2).

*Decider.* (i) Silence neurons that are not firing during a percept, leaving active neurons untouched. IIT predicts a change in experience. FMT predicts none for the current percept. (ii) In silico: compare a recurrent system with closure to its unfolded feedforward equivalent under a fixed resource bound. FMT predicts that they diverge in input-output behaviour where the bound binds (Gruber, 2026a, §7.2; Gruber, 2026d). IIT makes no behavioural prediction here; it assigns the feedforward system zero Φ whatever its behaviour. The second test therefore bears on FMT's reply to the unfolding argument and does not measure experience.

*Status.* (i) available in animal models in principle, limited by the readout of experience; (ii) in silico. Linked: F-UNF1 (divergence of closed and unfolded systems under a resource bound).

### C2. GNW and CTM: is broadcast constitutive?

*Point.* GNW holds that content is conscious when it is globally broadcast after ignition (Dehaene & Changeux, 2011; Mashour et al., 2020). FMT accepts the workspace as the occupancy of the channel and treats ignition as the signature of content entering the closed explicit simulation (Gruber, 2026a, §3.4.6, §3.6.1). It makes the self-model's closure over that content constitutive. The two "converge on the structure and diverge on its role" (§7.2). A second point: FMT allows basic consciousness without global broadcast, a thin simulation below the threshold at which its contents reach the evaluative workspace (§3.4.6). GNW denies experience without ignition. The conscious Turing machine inherits the first conflict (Blum & Blum, 2022). It adds a second, since it attributes consciousness to a machine that implements its architecture without a condition that the machine recruit its own capability for self-modelling; FMT's recruitment condition excludes a heteronomous universal machine (§3.7.3).

*Evidence.* COGITATE did not find sustained prefrontal content maintenance or the predicted offset ignition (COGITATE Consortium, 2025); GNW proponents have argued that the paradigm was not suited to test ignition dynamics (§7.2). No-report paradigms separate the correlates of experience from those of report (Tsuchiya et al., 2015). In language models, Gurnee et al. (2026) located a workspace of verbalisable representations, globally available, reportable and switched in an ignition-like way within a feedforward pass: on FMT, broadcast without closure.

*Decider.* A manipulation that makes content globally available without letting it enter the self-model's update rule. None exists yet in brains. A candidate disrupts self-model dynamics while leaving fronto-parietal ignition intact, with decision criteria held fixed (Nakamura et al., 2026). FMT predicts that experience degrades while the P3b is preserved; GNW predicts that experience follows the P3b. In silico, closure can be ablated in an artificial system with a workspace (Gruber, 2026d).

*Status.* No accepted brain protocol. The closure-relocation constraint above applies. In silico available.

### C3. HOT: must the state itself be represented?

*Point.* HOT's transitivity principle makes a state conscious when a suitable higher-order representation targets it, and some versions allow an empty higher-order representation to produce experience by itself (Rosenthal, 2005; Lau & Rosenthal, 2011; Brown et al., 2019). The higher-order representation is usually itself unconscious, so HOT does not require that the subject be aware of experiencing; introspection is the case in which the higher-order state is itself conscious. The conflict is therefore not over FMT's ladder but over the condition. HOT requires a representation of the particular state. FMT requires system-level closure of self-model and world-model, and places phenomenal experience at the basic rung, where the system generates a world model and a rudimentary self model and has no first-order self-observation (Gruber, 2026a, §3.5); whether a rudimentary self-model represents each of the system's states is left open. Conversely, a higher-order representation in a system without closure, such as a monitor attached to a simulation it does not take part in, is not conscious on FMT (§3.4.3, Stage 2).

*Evidence.* The debate over prefrontal involvement in conscious perception remains open (Odegaard et al., 2017; Boly et al., 2017). Metacognitive efficiency varies independently of first-order performance across individuals and conditions (Rouault et al., 2018; Rahnev et al., 2020), which is consistent with separable world-model and self-model contributions.

*Decider.* Abolish metacognitive read-out (meta-d′/d′ near zero) while sparing first-order sensitivity, and measure whether experience changes, using a no-report or criterion-fixed design. HOT, and in particular its empty-representation versions, predicts that experience is lost or altered. FMT predicts that experience survives if the loop between self-model and world-model is intact, because metacognitive report is one read-out of the self-model and not the closure itself. The experiment must establish which of the two a manipulation removes, and HOT proponents need not accept that meta-d′ indexes the higher-order representation their theory requires. FMT's Table 1b states the closure falsifier accordingly: disrupting the self-modelling loop itself, beyond metacognitive read-out, would have to leave no-report markers of experience intact. Report may fail under metacognitive disruption even where experience survives, because transfer to long-term memory can fail with it.

*Status.* Partly available: selective metacognitive deficits can be produced or found; measuring experience independently of report is the limiting step.

### C3a. Perceptual reality monitoring: monitor or closure

*Point.* On PRM, a sensory representation is experienced when a higher-order monitor judges it a reliable reflection of the present world (Lau, 2022). FMT requires that the architecture preserve the distinction between live and offline runs of the explicit models, without which recall would be hallucination (Gruber, 2026a, §6.0). It posits no marker on internally generated states, and makes closure, not the monitor's output, constitutive.

*Evidence.* Reality judgements rest on the combined strength of sensory activity, whether internally or externally generated (Dijkstra & Fleming, 2023). FMT reads this as evidence that source attribution is the fragile term (§6.0).

*Decider.* FMT predicts an ordering: under perturbation of the substrate or of communication between its levels, source attribution degrades before phenomenal experience does. Dreaming is the everyday instance: experience present, source attribution absent (§6.0). PRM predicts that experience follows the monitor's output. A graded perturbation, pharmacological or by sleep stage, that tracks reality judgements and experience reports separately can decide between them, provided the subpersonal monitor's output can be read from something other than the explicit reality judgement, which on PRM need not coincide with it. The two accounts agree on a mis-monitored internal representation being experienced as perception, so that case does not discriminate.

*Status.* Available in principle; the conflict is narrow.

### C4. RPT: is local recurrence sufficient?

*Point.* RPT holds that recurrent processing within sensory cortex suffices for phenomenal experience, unreported and unattended, and that widespread recurrence with fronto-parietal areas adds access and report (Lamme, 2006, 2010). FMT agrees that recurrence is the mechanism. Recurrent non-linear dynamics host the second level (Principle 2), and recurrent processing likely implements the running simulation (Gruber, 2026a, §7.2). Phenomenality arises only where the modelling closes on itself (Principle 3). A locally recurrent sensory loop that has no self-model in its update rule is a simulation without an inside (§3.4.3, Stages 1 and 2). On the question of local sufficiency the two theories conflict.

*Evidence.* Masking studies, the loss of V1 figure-ground modulation under anaesthesia (Lamme et al., 1998), and a fragile high-capacity visual store (Sligte et al., 2008) support RPT. FMT reads the overflow cases as phenomenal content of a thin self-model with too little recursion above it for that content to be reported (§3.4.6).

*Decider.* A state in which local sensory recurrence is preserved and self-model dynamics are abolished. Candidates: isolated or disconnected cortical tissue of the kind discussed as islands of awareness (Bayne et al., 2020); anaesthetic or dissociative states that preserve figure-ground modulation; in-silico ablations. RPT predicts experience; FMT predicts none.

*Status.* No clean protocol: islands of awareness are inaccessible to report, and disconnected tissue may hold its own closed loop. In silico available.

### C5. PP and FEP: sufficiency and boundary

*Point.* Most PP authors do not offer PP as a theory of consciousness (Hohwy & Seth, 2020), and FMT absorbs its machinery as the implementation of the implicit, predictive layer (Gruber, 2026a, §7.2). Conflict arises only where prediction-error minimisation, or the possession of a Markov blanket, is offered as sufficient. Markov blankets can be drawn around systems no theory counts as conscious (Bruineberg et al., 2022).

*Decider.* FMT's predictions that go beyond relaxed priors: dose-dependent improvement of anosognosia below ego-dissolution doses, strongest in disconnection-type cases (Prediction 1); and identity content during ego dissolution that tracks the dominant sensory modality (Prediction 2; Gruber, 2026a, §8.2–8.3). REBUS (Carhart-Harris & Friston, 2019) with Fotopoulou's (2014) predictive-coding account of anosognosia yields the coarse prediction; the fine structure (dose dependence below ego dissolution, lesioned-hemisphere complexity, the disconnection boundary) carries the discrimination (Gruber, 2026a, §8.2). Prediction 2 may be partly derivable from PP through weakened self-priors plus available sensory evidence (Gruber, 2026a, §7.2).

*Status.* Available.

### C6. AST and illusionism: are phenomenal properties real?

*Point.* AST holds that the brain's simplified model of its own attention is the source of claims to subjective awareness: the claims describe a real process, attention, in a caricatured form, and the non-physical experiential essence they depict does not exist (Graziano, 2013, 2024). Graziano (2024) calls this a "small" illusionism. Strong illusionism holds that introspection misrepresents quasi-phenomenal properties as phenomenal, and that there are no phenomenal properties (Frankish, 2016). FMT agrees that the substrate has no phenomenal properties and that the self-model's opacity to its substrate produces the sense of mystery (Gruber, 2026a, §3.8). It holds that phenomenal properties exist at the computational level (§3.4.5).

*Evidence.* None decisive. Both sides explain the reports.

*Decider.* No empirical decider exists. The source text states that this disagreement "cannot be settled by empirical observation from outside the system" (§3.4.5). The difference is practical: if FMT is right, a system built to its specification has phenomenal states and is a moral patient for that reason; on strong illusionism any such status has to rest on something other than phenomenal properties. Against AST the conflict may be narrower than against strong illusionism, since FMT also places the experiential properties in a model and denies them to the substrate; what remains is whether the model's depiction is accurate at its own level. Tests of AST's attention-control predictions (Wilterson et al., 2020) test the mechanism FMT absorbs and leave the ontology untouched.

*Status.* No empirical decider.

### C7. Self-model theory: selves and minimal phenomenal experience

*Point.* Two separate points. (a) Metzinger (2003) holds that no one ever was or had a self. FMT holds that the self is real as a running virtual process. The disagreement may be verbal, depending on how "self" is read. (b) Metzinger's minimal phenomenal experience (MPE) programme describes reports of "pure awareness" that are characterised as contentless and selfless, and models their prototype as a representation of tonic alertness (Metzinger, 2020). If phenomenality occurs with no self-model at all, Principle 3 is false.

*FMT's available reply.* Reports of MPE pass through the explicit self-model, memory and language, and are reconstructions made at the recursive rungs. The state reported may be a basic, non-recursive ESM, which is thin and has no self-observation, and therefore leaves nothing in the report that would be described as a self.

*Decider.* A measure of self-model activity, independent of the default mode network (which FMT does not identify with the ESM; Gruber, 2026a, Table 1 fn. 3), recorded during verified MPE episodes. FMT predicts a minimal but non-zero self-modelling signature. The strict selfless reading predicts none.

*Status.* Measurement immature. If verified MPE episodes show no self-modelling signature, Principle 3 is false.

### C8. IWMT: graded or binary demarcation

*Point.* IWMT's criterion is graded and multi-factor: spatial, temporal and causal coherence, integrated selfhood, workspace-capable dynamics (Safron, 2020). FMT's closure is a single binary criterion. The difference is sharpest at self-location. A system that jointly infers its own pose and a world map, as in G-SLAM (Safron et al., 2022) or a satellite navigation unit, locates itself without modelling itself as the modelling system (Gruber, 2026a, §7.3).

*Decider.* A system with high coherence and self-location and no self-reference. If IWMT's integrated selfhood is met by joint inference of self-pose and world, IWMT assigns such a system a non-zero degree and FMT assigns none. If IWMT requires the system to model itself as the modeller, the two criteria coincide on this case and the contradiction reduces to graded versus binary demarcation. Only artificial systems allow the case to be built, and behaviour does not establish experience.

*Status.* In silico for the build; no measure of experience.

### C9. ICT: informational closure or self-referential closure

*Point.* ICT identifies conscious processes with processes that form non-trivial informational closure with respect to the environment at a coarse-grained scale: their own state predicts their future while they carry information about the environment (Chang et al., 2020). It requires no self-model, so any coarse-grained process with non-trivial informational closure qualifies, to the degree of its closure. FMT's closure requires the self-model to enter the world model's update rule.

*Decider.* Two systems with matched informational closure at a coarse scale, one with and one without a self-model in the world model's update loop, compared on redeployment and sample efficiency at matched budget (Gruber, 2026d). FMT predicts a difference; ICT predicts none in consciousness. Behaviour does not establish consciousness (Gruber, 2026a, §8.10), so the test separates the architectures and leaves the phenomenal question open.

*Status.* In silico.

### C10. Biological naturalism: is biology required?

*Point.* Searle (1980, 1992) holds that brains cause consciousness by their specific causal powers, that implementing a program is never by itself sufficient, and that a simulation is not a duplication. He allows that a non-biological system with causal powers equivalent to the brain's could be conscious; the conflict with FMT is over computation, not over biology as such. Seth (2025) argues that consciousness may depend on being alive, on autopoiesis and interoceptive self-regulation, that computation alone is probably insufficient, and that artificial consciousness is unlikely on current trajectories. FMT holds that the architecture with free modelling suffices on any substrate, and treats interoceptive regulation of a body-model as one route to the self-model (Gruber, 2026a, §4.4).

*Evidence.* Corvids, cephalopods, and olfaction's thalamus-free route to cortex show that the architecture has more than one anatomical realizer (§4.4). All are biological, so none decides the question.

*Decider.* An artificial implementation of the full architecture, which does not exist (§8.9). Intermediate: the testable form of biological naturalism distinguished by Klatzmann and Doerig (2026) names the biological property and asks whether a non-biological system that has the property differs from one that lacks it. Partial implementations give graded predictions (§8.9).

*Status.* Requires artificial implementation.

### C11. Enactivism: representation and continuity of life and mind

*Point.* Strong enactivism holds that cognition and experience are enacted in the sensorimotor activity of a living, embodied system and are not constituted by internal representations of a pre-given world (Varela et al., 1991; Thompson, 2007). FMT holds that experience is a running internal simulation. The thesis of deep continuity between life and mind attributes some form of mind to all living systems. If that mind includes experience, it conflicts with FMT, on which systems below self-referential closure lack phenomenal experience regardless of behavioural sophistication (Gruber, 2026a, §6.4).

*Evidence.* Dreaming runs on internally generated input while sensory input is gated and motor output blocked (§6.3). Imagery and locked-in states show experience without ongoing sensorimotor coupling. The enactivist reply appeals to sensorimotor history; history of that kind is what FMT's implicit models store.

*Decider.* Experience in a system whose models were never trained through sensorimotor coupling. FMT's commitments do not exclude it; enactivism does.

*Status.* Requires artificial implementation.

## 6. Figures

All three figures use one colour key for verdicts: absorbed green, compatible blue, neutral grey, contradicts red. Colours must remain distinguishable in greyscale and for red-green colour blindness; contradiction edges are therefore also dashed, and absorbed edges solid.

### 6.1 Figure 1 — The reference architecture with theories overlaid

**Caption.** *The Four-Model Theory's architecture with other theories placed on the component their central claim is about. Each theory's colour says whether FMT keeps that claim (green), can live with it (blue), takes no side (grey) or rejects it (red). Red badges name the specific claim FMT rejects.*

**Drawing specification.** Two horizontal bands, not four boxes: the implicit models are regions of one wired band and the explicit models are regions of one running band.

FMT nodes (fixed geometry, bottom to top):

| ID | Label | Placement |
|---|---|---|
| SUB | Substrate (L1–L3: physical, electrochemical, proteomic) | bottom band, full width |
| IWM | Implicit world model | lower band ("wired", L4 topological), left |
| ISM | Implicit self model | lower band, right, drawn inside IWM's region (ISM ⊆ IWM) |
| CH | Channel / *Arbeitsmodell* (working memory) | narrow neck between lower and upper band |
| PERM | Permeability gate | marker on CH |
| EWM | Explicit world model | upper band ("running", L5), full width |
| ESM | Explicit self model | inside EWM (ESM ⊆ EWM) |
| CL | Closure loop | circular arrow ESM → EWM update rule → ESM |
| LAD | Ladder | three stacked rings on ESM: simply, doubly, triply extended |
| VQ | Virtual qualia | label on upper band only |
| MP | Meta-problem | dashed opacity line between ESM and ISM |
| FM | Free modelling (criticality = its signature in some brains) | background field behind both bands |
| SI | Substrate independence | label outside the frame, beside SUB |

FMT edges: IWM → EWM and ISM → ESM, "generated from" (solid; never labelled "transfer"); EWM/ESM → IWM/ISM, "consolidation" (solid, returning); both directions pass through CH; ESM → EWM, closure (bold); ESM ⇢ ISM, blocked (dotted, terminated bar; MP).

Overlays (node attached to an FMT component; colour of the node = verdict on the theory's central claim; badges for rejected claims):

| Theory | Attached to | Colour | Red badge |
|---|---|---|---|
| IIT | halo over upper band and FM; red outline on SUB | green halo | "identity with substrate cause-effect power" |
| GNW | CH | green | "broadcast constitutive" |
| CTM | CH; tag "world model ⊇ self" on EWM ⊇ ESM | green | "broadcast constitutive"; "no recruitment condition" |
| PP / FEP | lower band and the "generated from" edges | green | "PP sufficient" |
| Beast machine | ISM → ESM edge (interoceptive input) | green | "life may be required" |
| REBUS | PERM | green | — |
| Beautiful Loop | CL | green | — |
| ICT | CL | green | "self-model not required" |
| HOT | LAD | green | "per-state transitivity" |
| PRM | tag on ESM/EWM border, "source distinction" | green | "monitor constitutive" |
| RPT | "generated from" edges (recurrence) | green | "local recurrence sufficient" |
| DIT | L4 → L5 boundary at CH | green | — |
| AST | ESM and the attention edge into CH | green | "deflationary" |
| SMT | ESM | green | "selfless MPE" (open) |
| IWMT | large halo over EWM, ESM and FM | blue | "graded demarcation" (mild) |
| Illusionism | RV line and MP | green on MP | badge on VQ: "no phenomenal properties" |
| Searle | outside frame, arrow to SI | red | "computation insufficient" |
| Seth (BN) | outside frame, arrow to SI; secondary link to beast machine | red | "life may be required" |
| Enactivism | outside frame at the body/world edge; blue arrow to FM ("autonomous recruitment") | blue | "anti-representational" |

### 6.2 Figure 2 — Levels addressed by each theory

**Caption.** *Rows are levels of description, columns are theories. A filled cell means the theory makes a claim at that level; its colour gives FMT's verdict on that claim. Hatched cells in the FMT column mark levels where FMT makes a claim but has no mechanism, protocol or formal model of its own.*

**Drawing specification.** Rows, bottom to top:

| Row | Level |
|---|---|
| R0 | Formal model (does the theory have one?) |
| R1 | Substrate / cellular (L1–L3) |
| R2 | Circuit / connectivity (L4, implicit models) |
| R3 | Dynamical regime (FM; criticality signature) |
| R4 | Channel / access (CH, ignition, working memory) |
| R5 | Running models (EWM, ESM; L5) |
| R6 | Closure (CL) |
| R7 | Recursive depth (LAD) |
| R8 | Phenomenal ontology (VQ, illusion, identity) |
| R9 | Meta-problem (MP) |
| R10 | Substrate metaphysics (SI, biology, life) |

Cells (theory: row = verdict; all unlisted cells empty):

- **FMT**: R1 hatched (no cellular mechanism of its own); R2–R5 filled; R6 hatched (no accepted measurement protocol for closure); R7–R10 filled; R0 hatched (formalisation in progress, Gruber, 2026b).
- **IIT**: R0 A; R3 A; R6 A; R8 X; R10 X.
- **GNW**: R4 A; R5 X (broadcast constitutive); R1 N (prefrontal anatomy).
- **CTM**: R0 A; R4 A; R5 A; R10 X.
- **PP/FEP**: R0 A; R2 A; R5 C; R8 X (sufficiency).
- **Beast machine**: R2 A; R5 A; R10 X.
- **REBUS**: R0 A; R2 A.
- **Beautiful Loop**: R0 A; R6 A.
- **HOT**: R7 A; R8 X (transitivity); R9 A.
- **PRM**: R5 A; R8 X.
- **RPT**: R1 A; R2 A; R5 X (local sufficiency).
- **AST**: R4 A; R5 A; R8 X; R9 A.
- **SMT**: R5 A; R8 X (MPE, open); R9 A.
- **IWMT**: R0 C; R3 A; R5 A; R6 X (mild).
- **DIT**: R1 A; R2 A; R4 N.
- **ICT**: R0 A; R6 X (sufficiency); R5 A.
- **Illusionism**: R8 X; R9 A.
- **Searle**: R10 X.
- **Seth (BN)**: R3 A; R10 X.
- **Enactivism**: R3 C; R5 X; R10 X.

The hatched FMT cells are drawn at the same size as filled cells.

### 6.3 Figure 3 — Claim graph

**Caption.** *FMT's atomic claims (left, sized by core or periphery) and rival claims (right). Edge type gives the relation: entails or matches (green), compatible (blue), contradicts (red, dashed, labelled with its record number), implemented by (dotted). Prediction nodes hang from the FMT claims they test.*

**Drawing specification.** Core-periphery layout with FMT core claims at the centre, so that contradiction edges cross the middle. FMT node identifiers follow the supplementary file.

Rival claim nodes are the claims named in Table 1, with identifiers IIT-1 (identity with intrinsic cause-effect structure), IIT-2 (Φ > 0 suffices), IIT-3 (inactive units contribute), GNW-1 (broadcast constitutive), GNW-2 (capacity-limited workspace), CTM-1, HOT-1 (transitivity), HOT-2 (empty representations suffice), PRM-1, RPT-1 (local sufficiency), RPT-2 (recurrence necessary), AST-1 (deflationary schema), AST-2 (attention control), SMT-1, SMT-MPE1, IWMT-1, DIT-1, ICT-1, PP-1, REBUS-1, BL-1, ILL-1, BN-S1, BN-Seth1 and ENA-1.

Edges:

| FMT claim | Relation | Rival claim | Record |
|---|---|---|---|
| F-ID1 | contradicts | IIT-1 | C1 |
| F-CL1 | contradicts | IIT-2 | C1 |
| F-CH3 | contradicts | GNW-1 | C2 |
| F-CH2 | entails | GNW-2 | — |
| F-FM2 | contradicts | CTM-1 | C2 |
| F-LAD2 | contradicts | HOT-1 | C3 |
| F-CL1 | contradicts | HOT-2 | C3 |
| F-LAD1 | entails | HOT-1 (as mechanism of extended rungs) | — |
| F-SRC1 | compatible | PRM-1 (function) | — |
| F-P3 | contradicts | PRM-1 (constitution) | C3a |
| F-P2 | entails | RPT-2 | — |
| F-CL1 | contradicts | RPT-1 | C4 |
| F-RV2 | implemented-by | PP-1 | — |
| F-PERM1 | implemented-by | REBUS-1 | — |
| F-CL1 | entails | BL-1 | — |
| F-VQ1 | contradicts | AST-1, ILL-1 | C6 |
| F-MP1 | entails | AST-1 (mechanism only) | — |
| F-CH4 | compatible | AST-2 | — |
| F-MP1 | entails | SMT-1 | — |
| F-P3 | contradicts | SMT-MPE1 | C7 |
| F-CL1 | contradicts | IWMT-1 | C8 |
| F-CH1 | implemented-by | DIT-1 | — |
| F-CL1 | contradicts | ICT-1 | C9 |
| F-SI1 | contradicts | BN-S1, BN-Seth1 | C10 |
| F-MOD1 | contradicts | ENA-1 | C11 |

Prediction edges: F-PR1 and F-PR2 from F-PERM1; F-PR2 also from F-P3 and F-FORK1; F-PR3 from F-FORK1; F-PR4 from F-FM3 and F-LAD1; F-PR5 from F-VQ3; F-PR6 from F-MP1; F-PR7 from F-TE1 and F-CL1; F-FAL1 from F-FM1; F-FAL2 from F-CL1; F-FAL3 from F-RV1. Each contradiction edge carries a link to its record in Section 5.

## 7. Scope and Limits

The verdicts are the reference theory's own, and proponents of the other theories may place their claims differently or reject the decomposition. "Absorbed" means that FMT contains a claim as one of its components. GNW proponents, for example, would not accept that the workspace is the occupancy of a channel whose content becomes conscious through closure.

Claims without a counterpart in FMT, such as IIT's exclusion postulate as a rule for picking the conscious complex, appear as neutral and receive no further analysis. A different reference frame would produce a different table; running the method with two frames would show which verdicts depend on the frame. Verdicts for theories FMT's source text does not discuss (information closure theory, Searle, enactivism, perceptual reality monitoring and the conscious Turing machine as theories, minimal phenomenal experience) are derived from FMT's stated commitments.

The contradictions with empirical deciders lie on the predictive and higher-order side (C3, C3a, C5), plus the inactive-neuron test against IIT (C1). Broadcast (C2) and local recurrence (C4) require a manipulation of closure that no accepted protocol provides, and in recurrent systems such a manipulation tends to relocate closure. C6 and C7 concern phenomenal ontology or reports of phenomenal states, where measurement does not exist or depends on the introspective machinery whose output is in question. C8 can be built only in silico and has no measure of experience; C10 and C11 need artificial implementations of the full architecture. The phenomenal side of all three faces the problem of other minds.

## 8. Conclusion

At the level of atomic claims, FMT and the theories compared here mostly agree about mechanism and disagree about what is sufficient for experience and whether its phenomenal character is real. The agreements locate each theory on a component of one architecture. The disagreements are few enough to list, and for eight of the twelve an experiment or an in-silico test can be specified now. The claim set of the reference theory is supplied in a form that graph-based comparison programmes can ingest, so that the same exercise can be run with any other theory as the reference frame.

## Supplementary material

`fmt-claims.json`: FMT atomic claims as subject–predicate–object triples with section, type, core or periphery, and dependencies.

## References

Albantakis, L., Barbosa, L., et al. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms. *PLOS Computational Biology*, 19(10), e1011465.

Aru, J., Suzuki, M., & Larkum, M.E. (2020). Cellular mechanisms of conscious processing. *Trends in Cognitive Sciences*, 24(10), 814–825. https://doi.org/10.1016/j.tics.2020.07.006

Baars, B.J. (1988). *A Cognitive Theory of Consciousness*. Cambridge University Press.

Bayne, T., Seth, A.K., & Massimini, M. (2020). Are there islands of awareness? *Trends in Neurosciences*, 43(1), 6–16. https://doi.org/10.1016/j.tins.2019.11.003

Blum, L., & Blum, M. (2022). A theory of consciousness from a theoretical computer science perspective: Insights from the Conscious Turing Machine. *Proceedings of the National Academy of Sciences*, 119(21), e2115934119. https://doi.org/10.1073/pnas.2115934119

Boly, M., Massimini, M., Tsuchiya, N., Postle, B.R., Koch, C., & Tononi, G. (2017). Are the neural correlates of consciousness in the front or in the back of the cerebral cortex? Clinical and neuroimaging evidence. *Journal of Neuroscience*, 37(40), 9603–9613. https://doi.org/10.1523/JNEUROSCI.3218-16.2017

Brown, R., Lau, H., & LeDoux, J.E. (2019). Understanding the higher-order approach to consciousness. *Trends in Cognitive Sciences*, 23(9), 754–768.

Bruineberg, J., Dolega, K., Dewhurst, J., & Baltieri, M. (2022). The Emperor's new Markov blankets. *Behavioral and Brain Sciences*, 45, e183.

Carhart-Harris, R.L., & Friston, K.J. (2019). REBUS and the anarchic brain: Toward a unified model of the brain action of psychedelics. *Pharmacological Reviews*, 71(3), 316–344.

Chang, A.Y.C., Biehl, M., Yu, Y., & Kanai, R. (2020). Information closure theory of consciousness. *Frontiers in Psychology*, 11, 1504. https://doi.org/10.3389/fpsyg.2020.01504

COGITATE Consortium. (2025). Adversarial testing of global neuronal workspace and integrated information theories of consciousness. *Nature*, 642(8066), 133–142. https://doi.org/10.1038/s41586-025-08888-1

Dehaene, S., & Changeux, J.P. (2011). Experimental and theoretical approaches to conscious processing. *Neuron*, 70(2), 200–227.

Dehaene, S., Changeux, J.P., Naccache, L., Sackur, J., & Sergent, C. (2006). Conscious, preconscious, and subliminal processing: A testable taxonomy. *Trends in Cognitive Sciences*, 10(5), 204–211.

Dennett, D.C. (1991). *Consciousness Explained*. Little, Brown and Company.

Dijkstra, N., & Fleming, S.M. (2023). Subjective signal strength distinguishes reality from imagination. *Nature Communications*, 14, 1627. https://doi.org/10.1038/s41467-023-37322-1

Doerig, A., Schurger, A., Hess, K., & Herzog, M.H. (2019). The unfolding argument: Why IIT and other causal structure theories cannot explain consciousness. *Consciousness and Cognition*, 72, 49–59. https://doi.org/10.1016/j.concog.2019.04.002

Fotopoulou, A. (2014). Time to get rid of the 'Modular' in neuropsychology: A unified theory of anosognosia as aberrant predictive coding. *Journal of Neuropsychology*, 8(1), 1–19. https://doi.org/10.1111/jnp.12010

Frankish, K. (2016). Illusionism as a theory of consciousness. *Journal of Consciousness Studies*, 23(11–12), 11–39.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138.

Graziano, M.S.A. (2013). *Consciousness and the Social Brain*. Oxford University Press.

Graziano, M.S.A. (2024). Illusionism big and small: Some options for explaining consciousness. *eNeuro*, 11(10), ENEURO.0210-24.2024.

Gruber, M. (2015). *Die Emergenz des Bewusstseins*. Self-published. ISBN 9781326652074.

Gruber, M. (2026a). The Four-Model Theory of consciousness: A simulation-based framework unifying the hard problem, binding, and altered states. *Zenodo* preprint. https://doi.org/10.5281/zenodo.18669891

Gruber, M. (2026b). Toward a mathematical formalization of the Four-Model Theory: A recommended approach. *Zenodo* preprint. https://doi.org/10.5281/zenodo.21843693

Gruber, M. (2026d). In-silico tests of the four-model architecture: Self-referential closure, self-modelling and criticality in model systems. *Zenodo* preprint. https://doi.org/10.5281/zenodo.21610993

Gurnee, W., Sofroniew, N., Pearce, A., Piotrowski, M., Kauvar, I., Chen, R., Soligo, A., Bogdan, P., Ong, E., Wang, R., Thompson, B., Abrahams, D., Kantamneni, S., Ameisen, E., Batson, J., & Lindsey, J. (2026). Verbalizable representations form a global workspace in language models. *arXiv* preprint arXiv:2607.15495.

Hohwy, J., & Seth, A. (2020). Predictive processing as a systematic basis for identifying the neural correlates of consciousness. *Philosophy and the Mind Sciences*, 1(II), 3. https://doi.org/10.33735/phimisci.2020.II.64

Klatzmann, U., & Doerig, A. (2026). What biology can, and cannot, tell us about conscious AI. *arXiv* preprint arXiv:2606.02121.

Lamme, V.A.F. (2006). Towards a true neural stance on consciousness. *Trends in Cognitive Sciences*, 10(11), 494–501.

Lamme, V.A.F. (2010). How neuroscience will change our view on consciousness. *Cognitive Neuroscience*, 1(3), 204–220.

Lamme, V.A.F., Zipser, K., & Spekreijse, H. (1998). Figure-ground activity in primary visual cortex is suppressed by anesthesia. *Proceedings of the National Academy of Sciences*, 95(6), 3263–3268. https://doi.org/10.1073/pnas.95.6.3263

Lau, H. (2022). *In Consciousness We Trust: The Cognitive Neuroscience of Subjective Experience*. Oxford University Press. https://doi.org/10.1093/oso/9780198856771.001.0001

Lau, H., & Rosenthal, D. (2011). Empirical support for higher-order theories of conscious awareness. *Trends in Cognitive Sciences*, 15(8), 365–373.

Laukkonen, R.E., Friston, K.J., & Chandaria, S. (2025). A beautiful loop: An active inference theory of consciousness. *Neuroscience & Biobehavioral Reviews*, 176, 106296. https://doi.org/10.1016/j.neubiorev.2025.106296

Mashour, G.A., Roelfsema, P., Changeux, J.-P., & Dehaene, S. (2020). Conscious processing and the global neuronal workspace hypothesis. *Neuron*, 105(5), 776–798. https://doi.org/10.1016/j.neuron.2020.01.026

Metzinger, T. (2003). *Being No One: The Self-Model Theory of Subjectivity*. MIT Press.

Metzinger, T. (2020). Minimal phenomenal experience: Meditation, tonic alertness, and the phenomenology of "pure" consciousness. *Philosophy and the Mind Sciences*, 1(I), 7.

Nakamura, T., Michel, M., & Lau, H. (2026). Hitting and missing on consciousness. *Psychiatry and Clinical Neurosciences*. Advance online publication. https://doi.org/10.1111/pcn.70136

Negro, N., Elbaz, E., Fischer, S., Schreiber, M., & Mudrik, L. (2026). Prediction maps as a gateway to better understand and test scientific theories. *PsyArXiv* preprint. https://doi.org/10.31234/osf.io/kqr87_v1

Odegaard, B., Knight, R.T., & Lau, H. (2017). Should a few null findings falsify prefrontal theories of conscious perception? *Journal of Neuroscience*, 37(40), 9593–9602. https://doi.org/10.1523/JNEUROSCI.3217-16.2017

Rahnev, D., Desender, K., Lee, A.L.F., Adler, W.T., et al. (2020). The Confidence Database. *Nature Human Behaviour*, 4(3), 317–325. https://doi.org/10.1038/s41562-019-0813-1

Rosenthal, D. (2005). *Consciousness and Mind*. Oxford University Press.

Rouault, M., Seow, T., Gillan, C.M., & Fleming, S.M. (2018). Psychiatric symptom dimensions are associated with dissociable shifts in metacognition but not task performance. *Biological Psychiatry*, 84(6), 443–451.

Safron, A. (2020). An integrated world modeling theory (IWMT) of consciousness: Combining integrated information and global neuronal workspace theories with the free energy principle and active inference framework; toward solving the hard problem and characterizing agentic causation. *Frontiers in Artificial Intelligence*, 3, 30. https://doi.org/10.3389/frai.2020.00030

Safron, A., Çatal, O., & Verbelen, T. (2022). Generalized simultaneous localization and mapping (G-SLAM) as unification framework for natural and artificial intelligences: Towards reverse-engineering the hippocampal/entorhinal system and principles of high-level cognition. *Frontiers in Systems Neuroscience*, 16, 787659. https://doi.org/10.3389/fnsys.2022.787659

Searle, J.R. (1980). Minds, brains, and programs. *Behavioral and Brain Sciences*, 3(3), 417–457. https://doi.org/10.1017/S0140525X00005756

Searle, J.R. (1992). *The Rediscovery of the Mind*. MIT Press.

Seth, A. (2021). *Being You: A New Science of Consciousness*. Dutton.

Seth, A.K. (2025). Conscious artificial intelligence and biological naturalism. *Behavioral and Brain Sciences*, 49, e315. https://doi.org/10.1017/S0140525X25000032

Seth, A.K., & Bayne, T. (2022). Theories of consciousness. *Nature Reviews Neuroscience*, 23, 439–452.

Sligte, I.G., Scholte, H.S., & Lamme, V.A.F. (2008). Are there multiple visual short-term memory stores? *PLoS ONE*, 3(2), e1699. https://doi.org/10.1371/journal.pone.0001699

Suzuki, M., & Larkum, M.E. (2020). General anesthesia decouples cortical pyramidal neurons. *Cell*, 180(4), 666–676. https://doi.org/10.1016/j.cell.2020.01.024

Thompson, E. (2007). *Mind in Life: Biology, Phenomenology, and the Sciences of Mind*. Harvard University Press.

Tononi, G. (2004). An information integration theory of consciousness. *BMC Neuroscience*, 5, 42.

Tononi, G., Boly, M., Massimini, M., & Koch, C. (2016). Integrated information theory: From consciousness to its physical substrate. *Nature Reviews Neuroscience*, 17(7), 450–461. https://doi.org/10.1038/nrn.2016.44

Tsuchiya, N., Wilke, M., Frässle, S., & Lamme, V.A.F. (2015). No-report paradigms: Extracting the true neural correlates of consciousness. *Trends in Cognitive Sciences*, 19(12), 757–770.

Varela, F.J., Thompson, E., & Rosch, E. (1991). *The Embodied Mind: Cognitive Science and Human Experience*. MIT Press.

Wilterson, A.I., Kemper, C.M., Kim, N., Webb, T.W., Reblando, A.M.W., & Graziano, M.S.A. (2020). Attention control and the attention schema theory of consciousness. *Progress in Neurobiology*, 195, 101844. https://doi.org/10.1016/j.pneurobio.2020.101844

Yaron, I., Melloni, L., Pitts, M., & Mudrik, L. (2022). The ConTraSt database for analysing and comparing empirical studies of consciousness theories. *Nature Human Behaviour*, 6(4), 593–604. https://doi.org/10.1038/s41562-021-01284-5

Yu, H., Zhao, Y., Blum, L., Blum, M., & Liang, P.P. (2026). CTM-AI: A blueprint for general AI inspired by a model of consciousness. *arXiv* preprint arXiv:2605.04097.

---

## Points for MG (not part of the manuscript)

1. **RPT — master says "compatible at the mechanistic level" (§7.2); wiki `vs-rpt` says "compatible".** The draft keeps the master's wording for mechanism (A: recurrence implements the simulation) and adds X on *local sufficiency*, derived from Principle 3 / §3.4.3 — the master never addresses RPT's sufficiency claim. If MG agrees, §7.2 and `vs-rpt` need a sentence (master edit → new version).
2. **HOT — master §3.5 is clear (basic consciousness is phenomenal before first-order self-observation); wiki `vs-hot` says self-representation/meta-representation is *necessary* and maps basic consciousness to "first-order self-modeling".** Draft follows the master. `vs-hot` needs correcting.
3. **Table 1b closure falsifier** reads "Metacognitive disruption leaves phenomenology intact" as disconfirming closure, while §3.5/§3.4.6 imply metacognitive read-out and closure are separable (so an intact phenomenology under metacognitive disruption is what FMT *predicts* if closure is intact). C3 states the experiment neutrally and notes the measurement-approach issue without rewording Table 1b. Resolved S334: MG ruled the reword; master Table 1b now reads "disrupting the self-modelling loop itself leaves no-report markers of experience intact", with metacognitive disruption alone excluded as a test of closure.
4. **PP placement — master §7.2: PP supplies "the inference dynamics of the implicit, predictive layer"; wiki `vs-pp`: "the explicit models are generative, predictive models".** Draft follows the master (PP on the implicit band and the generation edges; beast machine on ISM→ESM as master §4.4 says). `vs-pp` disagrees.
5. **IIT "adopts" — master §7.2 says FMT "adopts" IIT's central diagnosis.** Draft follows the master but narrows the object to what the master itself spells out ("irreducible, integrated and causally structured") and states the departure in the next sentence. An IIT reader may still read "adopts" as a misreading; the brief's softer alternative ("shares IIT's demand…; rejects the substrate identification") would need a master edit.
6. **PRM** — brief suggested C (near-absorption). Draft gives A (function) + X (constitution), with a decider taken from the master's own §6.0 ordering prediction (source attribution degrades before experience). Also note §6.0 says FMT "posits no marker", which sits against a tag reading of PRM. Confirm.
7. **MPE (C7)** — draft lists MPE as an open threat to Principle 3 with the AIW-280 reply, using the S334 ruling (minimal self = basic non-recursive ESM). Confirm MG is content with "open threat + reply".
8. **Theories the master does not engage** (ICT, Searle, enactivism, PRM as theory, CTM as theory, MPE): verdicts are derived and §7 of the draft says so. Decide whether to add short master paragraphs first (brief Q6).
9. **Gruber 2026a–c labels** in this draft differ from the master's own labels (master: 2026b formalization, 2026d in-silico). Harmonise at submission.
10. **Verification:** all references are either in the master's verified list or were web-verified this session (Tononi et al. 2016; Metzinger 2020; Bayne, Seth & Massimini 2020; Lamme et al. 1998; Searle 1980; Sligte et al. 2008; Odegaard et al. 2017; Boly et al. 2017; Varela et al. 1991; Negro et al. 2026 DOI). Doerig et al. 2019 author list expanded from the master's "et al." from memory — check. Wilterson et al. 2020 author list from memory (venue/volume [V] in the brief) — check. Friston 2018, Seth's "The stuff matters" reply and Kleiner's commentary were left out (unverified). The COGITATE offset-ignition reanalysis (Bandara, Rowe & Garrido 2026, in the master §1.1) is not mentioned in C2; add it if MG wants C2 to carry the post-COGITATE state.
11. Word count and venue: venue-neutral per S334; no journal formatting.
12. **Wiki draft:** `article_number: 102` is provisional (comparative pages use 54–62; highest in wiki is 101). Placed at `drafts/papers-moc7/theory-map-wiki.md`; target `wiki/comparative/theory-map.md`. Wiki build tests (llms-full) will need a rebuild when it moves into wiki/.
13. **Review pass (adversarial reviewer, 2026-10-16).** (a) Labels: in-silico paper relabelled 2026c → **2026d** to match the master; formalization stays 2026b (matches); the FMT master stays 2026a here, which in the master's own list is the motivation paper (not cited here). The list now reads a, b, d — renumber at submission if the venue objects. (b) Doerig et al. 2019 and Wilterson et al. 2020 author lists web-verified; DOIs added. (c) Searle row/C10 corrected: Searle allows non-biological systems with equivalent causal powers, so the X is "computation insufficient", not "biology required". Seth's X is now stated as his live possibility, not a commitment. (d) HOT (C3): HOTs are normally unconscious, so the conflict was moved from "awareness of experiencing" to "per-state representation vs system closure"; an open point is whether FMT's rudimentary ESM represents each state — if it does, C3 narrows sharply. (e) AST (C6): Graziano (2024) calls AST "small" illusionism (attention is real, its depiction is a caricature); the conflict with FMT may be narrower than with Frankish — a sentence now says so. (f) C5: the old line that REBUS lacks modality tracking contradicted master §7.2, which concedes Prediction 2 may be partly PP-derivable; Prediction 1 now carries the discrimination. (g) C8 IWMT made conditional on how IWMT reads "integrated selfhood"; "inherited Φ" moved from X to N. (h) C1 decider (ii): IIT makes no behavioural prediction, so the test bears on the unfolding reply only; linked prediction changed from Prediction 4 (unrelated) to F-UNF1. (i) §3: "claims about closure are efficiency claims" scoped to what closure *buys*, so it no longer reads as withdrawing Principle 3.
