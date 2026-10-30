# Where the Theories Sit: An Architectural Coordinate System for Comparing Theories of Consciousness, with the Four-Model Theory as Reference Frame

**Matthias Gruber**\
Independent researcher · ORCID 0009-0005-9697-1665 · research@matthiasgruber.com

2026-10-21 · Preprint, version 3

## Abstract

Comparisons between theories of consciousness usually score whole theories against a list of requirements or set two theories against each other in a single experiment. Both procedures treat a theory as one unit. Most theories, however, make claims about mechanism, about what is constitutive of experience, about ontology and about substrate. A theory can be right about one of these and wrong about another. The method described here compares atomic claims. Each claim is placed on a component of a reference architecture and given one of four verdicts: absorbed, compatible, neutral, or contradicting. Every contradiction is recorded with the experiment that would decide it, or with the statement that no empirical decider exists. The method is applied to nineteen theories and theory variants, with the Four-Model Theory (FMT) as the reference frame. The verdicts sort by claim type. FMT absorbs most of the mechanisms the other theories propose; the contradictions concern what is sufficient or constitutive for experience, and the ontology of phenomenal properties. Twenty-one contradicted claims are recorded in eleven records. For nine the named experiment would decide the contradiction: two can be run in principle now, six wait on a protocol shown to remove closure rather than relocate it, and one on a measure of self-model activity during verified reports of selfless experience. For two, an in-silico test separates the architectures and leaves the phenomenal question open. For ten, no empirical decider exists. The reference theory's claims are supplied as subject–predicate–object triples with dependency links, for graph-based comparison.

**Keywords:** theories of consciousness; theory comparison; adversarial collaboration; prediction maps; Four-Model Theory; self-referential closure

## 1. Introduction

Seth and Bayne (2022) review four families of theories of consciousness, and the experimental paradigm a study uses predicts which theory its result supports (Yaron et al., 2022). The first large adversarial collaboration tested integrated information theory (IIT) against global neuronal workspace theory (GNW) and challenged parts of both (COGITATE Consortium, 2025). A single experiment confronts a single pair of predictions, and each theory makes many more claims than that pair.

Two comparison formats are common. Scoring theories against a list of requirements (e.g. Gruber, 2026a, §7.1) shows how much ground each covers, and does not show whether two theories that cover a requirement agree about it. Setting two theories in opposition finds disagreements and leaves agreements unrecorded. Negro et al. (2026) propose a third format: a theory becomes a network of claims and predictions with a core, a periphery and inferential edges, so that theories can be aligned claim by claim.

The method described here uses one theory with many components as a coordinate system. Any architecture with enough components could serve as the frame. The Four-Model Theory (FMT; Gruber, 2015, 2026a) is used because it names a component at each level the other theories address, from substrate and connectivity through dynamical regime, channel, running models, closure and recursive depth to phenomenal ontology and substrate metaphysics. The choice introduces a bias: claims are recorded only where they touch FMT's components. The hatched cells of Figure 2 mark the levels where FMT itself has no mechanism, protocol or formal model.

## 2. Method

### 2.1 Atomic claims

An atomic claim is a single subject–predicate–object statement that a theory's proponents assert and that can be true or false independently of the theory's other claims. "A state is conscious if and only if it is the target of a suitable higher-order representation" is one atomic claim; "an empty higher-order representation suffices for experience" is a second. Each claim is assigned a type: definition, principle, bridging commitment, consequence, mechanism, prediction, or falsifier.

### 2.2 Placement

Each claim is placed on the component of the reference architecture that it is about: a claim about global broadcast on the component that carries content between the stored and running levels, a claim identifying experience with a cause-effect structure at the level of phenomenal ontology. Placement depends on subject matter, not on whether the reference theory agrees.

### 2.3 Verdicts

Each placed claim receives one of four verdicts relative to the reference theory's own claim about the same component.

- **A — absorbed.** The reference theory contains the claim, as a component, a mechanism, or an implementation of one of its components.
- **C — compatible.** The reference theory does not contain the claim, and the claim does not conflict with anything the reference theory asserts.
- **N — neutral.** The reference theory takes no position on the claim.
- **X — contradicts.** The claim and the reference theory's claim about that component cannot both be true.

An A verdict names the reference-theory claim that contains the rival claim, so that the containment can be checked against the supplementary file. A claim that the reference theory restates in its own vocabulary without containing it is not absorbed.

### 2.4 Contradiction records

Each X verdict is recorded in a fixed format: the point of conflict, with the rival claim and the reference theory's claim; evidence that bears on the point; the experiment that would decide it; whether that experiment decides the contradiction (yes), separates the architectures while leaving the phenomenal question open (architecture only), or does not decide it (no); and the linked prediction of the reference theory. The status of each experiment (available, no accepted protocol, in silico only, requires an artificial implementation, or no empirical decider) is given in Table 3. Where no decider exists, the record says so and names the kind of difference that remains, for example an ethical one.

### 2.5 Encoding

The reference theory's claims are encoded as triples with five further fields: section of the source text, claim type, core or periphery, and a list of the claims each one depends on. Core claims are the principles, the definition and the derivation of the architecture. Peripheral claims are mechanisms, consequences and predictions. The dependency list gives the inferential edges a prediction map requires (Negro et al., 2026). The FMT claim set is supplied as a supplementary JSON file (`fmt-claims.json`). Rival-theory claims receive identifiers of the form `GNW-1`, `IIT-2`, and the relations between them and FMT claims form the edges of Table 2.

The FMT prediction map in the format of Negro et al. (2026) is supplied as a second file (`fmt-prediction-map.json`), with node labels by level (A core to F behavioural predictions).

### 2.6 Frame failure

Two patterns would show that the verdicts come from the frame. A high share of N verdicts across theories means that the frame lacks components the theories address. Verdicts that change when the exercise is repeated with a second theory as the frame are artefacts of the frame. A third check is agreement between coders: a verdict that a second coder, preferably a proponent of the rival theory, does not reproduce from the same sources is the coder's rather than the method's. None of the three checks has been run for Table 1; Section 7 states the consequence.

## 3. The Reference Frame

FMT rests on three principles (Gruber, 2026a, §3).

1. **Open-ended computation allows free modelling.** The system must be able to compute in the regime capable of universal computation (Wolfram's Class 4) and must recruit that capability for its own modelling. Free modelling is necessary and not sufficient for consciousness. In neural tissue it usually shows as near-critical dynamics, a signature of free modelling in some substrates, at some task sizes; near-criticality is neither necessary nor sufficient for consciousness, and a conscious system may run subcritically (§3.7, Table 1).
2. **Recurrent non-linear dynamics of sufficient complexity host a second computational level**: persistent activity patterns that interact and compute over one another, individuated by their mutual effects (§3.3).
3. **Phenomenology is real and physical, and it is that level's modelling closed on itself**: the self-model and the world-model each enter the other's update rule (§3.4). The principle is an identity: phenomenality is closure. This is the theory's single bridging commitment. It is argued for and not derived (§3.4.3).

From these follows a minimum architecture of two kinds of model along two axes (§3.2). Mode separates implicit models, stored in substrate connectivity, from explicit models, generated as running processes. Scope separates the world from the self, and is a nesting: the self-model's content is part of the world-model's. The four extremal poles are the implicit world model (IWM), implicit self model (ISM), explicit world model (EWM) and explicit self model (ESM). Four is the floor; the substrate implements an effectively uncountable number of overlapping models around these poles. The explicit models are generated from the implicit models and current input, not filled by a copy of stored content (§3.6). The architecture, like free modelling, is necessary and not sufficient. What suffices is a conjunction: the four model kinds under closure, with free compute, embodiment and at least one pain-pleasure axis, which may be engineered (§3.7.3, §4.4).

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
| SI | Substrate independence: the sufficient conjunction (four model kinds under closure, free compute, embodiment, at least one pain-pleasure axis) suffices on any substrate | §3.7.3, §4.4 |

Three features of the frame govern the verdicts. First, for content in the running simulation, access and phenomenality are two level-descriptions of one process; content that is only accessible, poised for report without being in use, is preconscious: it is stored on the implicit side or held in an explicit model outside the self-model's closed loop, and it becomes conscious on entering that loop (§3.4.6; Dehaene et al., 2006). Added recursive depth converts content that is present into content that is reportable, with no separate broadcast stage (§3.4.6). Second, the ladder starts below basic consciousness. Minimal consciousness is a rudimentary closure of the explicit world and self models whose content is the present moment, with no reflection and no discernible qualia; basic consciousness adds discernible content at the same depth of recursion. Both are phenomenal without first-order self-observation, and awareness that one experiences arrives at the first extended rung (§3.5). Third, FMT's claims about what closure gives a system are claims about one architecture's closure and its efficiency under a resource bound, not claims about what is barred to systems without it (§4.4). Opening a closed loop in a recurrent system tends to relocate closure, leaving two or more smaller closed systems where one stood (§4.4, §8.12).

## 4. The Map

Section numbers in the last column of Table 1 refer to Gruber (2026a).

**Table 1. Placement and verdicts of nineteen theories and theory variants, relative to FMT.** A = absorbed, C = compatible, N = neutral, X = contradicts. Each verdict applies to one atomic claim. Rival claims carry the identifiers used in Table 2 and in the ledger of Section 7.

| Theory (source) | Core claim | FMT component | Verdicts | Rival supplies / FMT lacks | FMT ref. |
|---|---|---|---|---|---|
| IIT (Tononi, 2004; Tononi et al., 2016; Albantakis et al., 2023) | Experience is a maximally irreducible intrinsic cause-effect structure; Φ measures its irreducibility | CL and FM (integration, recurrence); VQ (relational structure of the quality space) | A: experience is irreducible, integrated and causally structured, and recurrence is required (IIT-4; F-ID1, F-P2). A: experience has a relational quality structure (IIT-5; F-VQ3). X: identity with the substrate's intrinsic cause-effect power (IIT-1). X: every complex with Φ > 0 is conscious (IIT-2). X: inactive but available units contribute to experience (IIT-3). N: exclusion as a boundary rule (IIT-6) | A measure (Φ) and a quality-space formalism; FMT has no measure of closure and no formal model | §7.2, §3.4.1, §4.4 |
| GNW (Baars, 1988; Dehaene & Changeux, 2011; Mashour et al., 2020; Changeux & Farisco, 2026) | Content is conscious when broadcast globally after non-linear ignition; capacity-limited | CH (workspace = channel occupancy); PERM (ignition = signature of content entering the running models) | A: workspace and capacity limit (GNW-2; F-CH2, F-CH3). A: ignition as the marker of content entering the running models (GNW-4; F-CH3). X: broadcast is constitutive (GNW-1). X: no ignition, no experience (GNW-3). N: prefrontal anatomy (GNW-5) | Tested access markers (ignition, P3b, masking) and a mapped fronto-parietal implementation; FMT has no measurement protocol for closure | §3.6.1, §3.4.6, §7.2 |
| CTM (Blum & Blum, 2022) | Formal model on workspace lines: up-tree competition, down-tree broadcast, processors including a Model-of-the-World that contains a self | CH (broadcast); EWM ⊇ ESM (world model with self) | A: a world model that contains a self model (CTM-3; F-NEST). X: broadcast as constitutive (CTM-1). X: a machine implementing the CTM architecture is conscious in the phenomenal sense FMT defines, with no condition that it recruit its own capability for self-modelling (CTM-2; the CTM defines conscious awareness as the reception by all processors of the stage's broadcast). N: the internal language format (CTM-4) | A formal specification and a resource-bounded treatment; FMT has no formal model | §7.2, §3.6.1, §3.7.3, §8.10 |
| PP / FEP (Friston, 2010; Hohwy & Seth, 2020) | Perception is inference minimising prediction error; precision weighting | IWM/ISM dynamics; the generation of EWM/ESM | A: prediction-error machinery as the implementation of the implicit, predictive layer (PP-1; F-RV1, F-RV2). A: perception as controlled hallucination (PP-2; F-RV2, F-MOD1). N: FEP as a general principle of self-organisation (PP-3) | Quantitative inference models of the implicit layer; FMT's permeability is specified only qualitatively | §7.2 |
| Beast machine (Seth, 2021; Seth & Bayne, 2022) | Selfhood is control-oriented interoceptive prediction | ISM → ESM generation from interoceptive input | A: interoceptive prediction as one route to the ESM (BM-1; F-2X2, F-RV2). The biological-naturalist rider is recorded under Seth (2025) | A mechanism for generating the self-model from body-state prediction; FMT names no mechanism for ESM generation | §3.2, §4.4, §7.2 |
| REBUS (Carhart-Harris & Friston, 2019) | Psychedelics relax precision on high-level priors | PERM | A: one implementation of a global permeability change (REBUS-1; F-PERM1) | A specified pharmacological mechanism; FMT's permeability is qualitative | §7.2, §8.2–8.3 |
| Beautiful Loop (Laukkonen et al., 2025) | Consciousness is a self-evidencing loop: through epistemic depth the world model contains the knowledge that it exists | CL | C: the self-evidencing loop (BL-1). Closure in FMT's sense requires a model of the system itself in the world model's update rule (F-SM1, F-P3); the source states the loop as the world model knowing itself, distinct from self-consciousness, and does not fix whether it meets that condition | A formal statement of the loop in active inference; FMT has no formal model of closure | §7.3, §3.4.3 |
| HOT (Rosenthal, 2005; Lau & Rosenthal, 2011; Brown et al., 2019) | A state is conscious iff a suitable higher-order representation, usually itself unconscious, targets it; on some versions an empty higher-order representation suffices | LAD; ESM; MP | A: higher-order self-modelling as the mechanism of the extended rungs (HOT-3; F-LAD1). X: a higher-order representation of the particular state as the condition of phenomenality (HOT-1). X: an empty higher-order representation suffices (HOT-2; some versions). N: conceptual or non-conceptual format (HOT-4) | A condition stated at the level of particular states, and a metacognition measurement programme; FMT states no per-state condition | §3.5, §3.4.3, §3.4.6, §7.2 |
| PRM (Lau, 2022) | Experience occurs when a higher-order monitor marks a sensory representation as a reliable reflection of the present world | Source distinguishability (a requirement on the architecture) | A: the reality-monitoring function (PRM-2; F-SRC1). X: the monitor's output as constitutive of experience (PRM-1) | Candidate cues for reality monitoring and their measurement; FMT states only a negative requirement on composition | §7.2, §6.0 |
| RPT (Lamme, 2006, 2010) | Local recurrent processing in sensory cortex suffices for phenomenal experience; global recurrence adds access | Generating dynamics of the EWM (Principle 2) | A: recurrence as the mechanism that hosts the running models (RPT-2; F-P2). X: local recurrence without a self-model in the loop as sufficient (RPT-1). X: phenomenal overflow as phenomenality beyond access (RPT-3) | Cortical timing (feedforward sweep, recurrence) and masking paradigms; FMT has no circuit mechanism of its own | §3.3, §3.4.3, §3.4.6, §7.2 |
| AST (Graziano, 2013, 2024; Wilterson et al., 2020) | The brain models its own attention in simplified, partly inaccurate form; claims of awareness report that model's content, and the non-physical essence it depicts does not exist | ESM (model of selection into CH); MP | A: the attention schema as part of the ESM and the meta-problem mechanism (AST-3; F-MP1, F-CH4). C: attention control as the schema's function (AST-2). X: deflationism about phenomenal properties (AST-1) | A specified mechanism with behavioural predictions; FMT does not model the ESM's representation of attention | §3.8, §3.4.5, §3.6.1 |
| SMT (Metzinger, 2003, 2020) | The phenomenal self is a transparent self-model; minimal phenomenal experience may be selfless | ESM; MP | A: the self-model as constitutive and transparent to its bearer (SMT-1; F-P3, F-CL1, F-MP1). A: no self beyond the self-model (SMT-2; F-DEF2). X (open): selfless minimal phenomenal experience (SMT-3) | A phenomenological analysis of the self-model (transparency, perspectivalness) and the MPE programme; FMT has no phenomenological analysis of comparable detail | §1.3, §3.4.3, §3.5, §7.2, §7.4 |
| IWMT (Safron, 2020; Safron et al., 2022) | Consciousness is integrated world modelling with integrated selfhood; near-critical self-organising harmonic modes | EWM, ESM, FM | A: world and self modelling both necessary (IWMT-2; F-2X2). A: the near-critical signature (IWMT-3; F-FM3). C: formal mechanism (IWMT-4). X (conditional): joint inference of self-pose and world map meets the selfhood condition (IWMT-1). N: the integrated-information component (IWMT-5) | A formal mechanism (harmonic modes, G-SLAM); FMT has none | §7.3 |
| DIT (Aru et al., 2020; Suzuki & Larkum, 2020) | Coupling of apical and basal compartments of layer-5 pyramidal neurons gates consciousness; anaesthetics decouple them | L4 → L5 transition; candidate realizer of CH | A: candidate cortical implementation of the channel (DIT-1; F-CH1, F-CH5). N: whether it is the only realizer (DIT-2) | A cellular mechanism; FMT has none | §3.7.1, §3.6.1 |
| ICT (Chang et al., 2020) | Conscious processes are those that form non-trivial informational closure with respect to the environment at a coarse-grained scale; level of consciousness grows with its degree | CL; L5 | A: closure as primitive at a coarse-grained level (ICT-2; F-P3, F-P2). X: non-trivial informational closure without a self-model as sufficient (ICT-1). N: the information-theoretic quantities (ICT-3) | Measurable information-theoretic quantities; FMT has no measure of closure | §7.2, §3.3, §3.4.3 |
| Illusionism (Dennett, 1991; Frankish, 2016) | Phenomenal properties do not exist; introspection misrepresents quasi-phenomenal properties as phenomenal | RV; MP; VQ | A: introspection misrepresents its own basis (ILL-2; F-MP1). X: no phenomenal properties at any level (ILL-1) | An account with no ontological posit beyond functional states; FMT's realism at the computational level is a posit | §3.4.5 |
| Biological naturalism, Searle (Searle, 1980, 1992) | Brains cause consciousness by their specific causal powers; implementing a program never suffices, and simulation is not duplication | SI | C: brains produce consciousness through their biology, as one realizer (BN-S2). X: the right computation is not sufficient (BN-S1; Searle allows non-biological systems with equivalent causal powers) | — | §7.2, §4.4 |
| Biological naturalism, Seth (Seth, 2025) | Consciousness may depend on being alive; computation alone is probably insufficient | SI; FM recruitment; ISM → ESM | A: autonomy, self-maintenance and interoceptive self-modelling as one route (BN-Seth2; F-FM2, F-2X2). X: life, not computation, as what consciousness depends on (BN-Seth1; held by Seth as a live possibility) | Candidate necessary properties (autopoiesis, interoceptive regulation) with a research programme; FMT names embodiment and a pain-pleasure axis without a mechanism | §4.4 |
| Enactivism (Varela et al., 1991; Thompson, 2007) | Mind is embodied sense-making continuous with life; strong strands deny internal representation | FM recruitment; ESM ⊆ EWM boundary | C: autonomy and embodiment as conditions on recruitment (ENA-3). X: experience without internal models (ENA-1). X (conditional): mind in every living system, if mind includes experience (ENA-2) | An account of autonomy and sense-making; FMT names autonomous recruitment without a mechanism | §7.2, §3.7.3, §6.3, §6.4 |

### 4.1 The pattern

**Mechanisms are absorbed.** The workspace and its capacity limit become the channel and its occupancy, recurrence the dynamics that host the second level, prediction-error minimisation the implementation of the implicit layer, higher-order self-representation the mechanism of the extended rungs, apical-basal coupling a candidate cortical realizer of the step from stored to running models, and the attention schema part of the self-model. Informational closure at a coarse-grained scale is closure's primitive without its self-model condition.

**Sufficiency and constitution claims are contradicted.** GNW makes broadcast constitutive, RPT local recurrence sufficient, ICT informational closure without a self-model sufficient, and IIT any complex with Φ > 0 conscious; HOT makes a higher-order representation of the particular state the condition. FMT makes the self-model's closure the condition and places phenomenality at the minimal and basic rungs, below first-order self-observation.

**Ontological and substrate claims are contradicted.** Illusionism denies that phenomenal properties exist, and AST that the subjective essence depicted in claims of awareness exists; FMT holds that they exist at the computational level. Searle denies that any computation suffices, and Seth holds that consciousness may depend on being alive; on FMT any system meeting the sufficient conjunction is conscious, whatever its substrate. Strong enactivism denies that experience is constituted by internal models; on FMT experience is a running internal simulation.

The groups follow claim type, which a score for the whole theory cannot show.

## 5. Contradictions and Their Deciders

Because cutting a loop in a recurrent system relocates closure (Section 3; Gruber, 2026a, §4.4), any experiment below that intends to abolish self-referential closure must show that its manipulation removed closure, not only that it opened one loop.

### C1. IIT: what the irreducible structure is

*Point.* IIT identifies an experience with the substrate's intrinsic cause-effect structure (Tononi et al., 2016; Albantakis et al., 2023). It follows that any maximally irreducible complex with Φ > 0 has some experience, and that a digital simulation of a brain on conventional hardware lacks the brain's experience despite identical function. FMT adopts IIT's diagnosis that consciousness is irreducible, integrated and causally structured, and locates that structure in the running, substrate-neutral, self-referential updating of the explicit models (Gruber, 2026a, §7.2). On FMT a complex without closure has no experience whatever its Φ, and an implementation that meets the sufficient conjunction is conscious on any substrate (§3.7.3, §4.4, §8.10). The digital case is carried by IIT-1 and not recorded as a further contradiction, since whether a particular simulation on externally clocked hardware meets the recruitment condition is a question about that system (§3.7.3). IIT also holds that inactive but available neurons contribute to the cause-effect structure (Tononi et al., 2016; IIT-3); on FMT idle units contribute only through the implicit substrate (F-RV2).

*Evidence.* COGITATE found content-specific information in posterior cortex and did not find the sustained posterior synchronisation IIT predicted (COGITATE Consortium, 2025). The unfolding argument applies to both theories (Doerig et al., 2019; Gruber, 2026a, §7.2).

*Decider.* (i) Remove the capacity to fire, by block or lesion, from units inside the complex that are not firing during a percept, leaving the active units untouched. IIT predicts a change in experience. FMT predicts a change only where the decoded content of the explicit models changes. (ii) In silico: compare a recurrent system with closure to its unfolded feedforward equivalent under a fixed resource bound. FMT predicts that they diverge in input-output behaviour where the bound binds (Gruber, 2026a, §7.2; Gruber, 2026c). IIT makes no behavioural prediction here and assigns the feedforward system zero Φ whatever its behaviour.

*Decides the contradiction?* IIT-3: yes, limited by the read-out of experience in the animal. IIT-1 and IIT-2: no; test (ii) separates architectures only, and no measure of experience exists for a complex without closure.

*Linked.* F-UNF1 (divergence of closed and unfolded systems under a resource bound), node F10 of the prediction map (the functional-twin refuter).

### C2. GNW and CTM: is broadcast constitutive?

*Point.* GNW holds that content is conscious when it is globally broadcast after ignition (Dehaene & Changeux, 2011; Mashour et al., 2020; Changeux & Farisco, 2026). FMT accepts the workspace as the occupancy of the channel and treats ignition as the signature of content entering the closed explicit simulation (Gruber, 2026a, §3.4.6, §3.6.1). It makes the self-model's closure over that content constitutive (GNW-1). FMT also allows minimal and basic consciousness without global broadcast, a thin simulation below the threshold at which its contents reach the evaluative workspace (§3.4.6), whereas GNW denies experience without ignition (GNW-3). The conscious Turing machine inherits the first conflict (CTM-1; Blum & Blum, 2022). It also defines conscious awareness as the reception by all processors of the stage's broadcast and attributes it to a machine that implements the architecture, with no condition that the machine recruit its own capability for self-modelling (CTM-2); the contradiction concerns sufficiency for phenomenality as FMT defines it, since FMT's recruitment condition excludes a heteronomous universal machine (§3.7.3).

*Evidence.* COGITATE did not find sustained prefrontal content maintenance or the predicted offset ignition (COGITATE Consortium, 2025); a reanalysis of the same data found prefrontal ignition at stimulus offset as well as onset (Bandara, Rowe, & Garrido, 2026), and GNW proponents have argued that the paradigm was not suited to test ignition dynamics (Gruber, 2026a, §7.2). In language models, Gurnee et al. (2026) located a workspace of verbalisable representations, globally available, reportable and switched in an ignition-like way within a feedforward pass: on FMT, broadcast without closure.

*Decider.* A manipulation that disrupts the self-modelling loop while leaving ignition and late sustained prefrontal activity intact, scored with no-report markers of experience (Tsuchiya et al., 2015) in a design that holds decision criteria fixed (Nakamura et al., 2026). FMT predicts that the no-report markers degrade while ignition persists; GNW predicts that experience follows ignition. GNW-3 takes the converse case: no-report markers of experience, or in inspectable systems the white-box trace of Table 1b, in a state without ignition; FMT predicts minimal or basic experience there and GNW none. In either direction the manipulation must show that it removed closure; none exists yet in brains. In silico, closure can be ablated in an artificial system with a workspace (Gruber, 2026c), which separates the architectures only.

*Decides the contradiction?* GNW-1, GNW-3, CTM-1: yes, once a protocol exists. CTM-2: no; it needs an artificial implementation of the full architecture and then faces the problem of other minds.

### C3. HOT: must the state itself be represented?

*Point.* HOT's transitivity principle makes a state conscious when a suitable higher-order representation targets it, and some versions allow an empty higher-order representation to produce experience by itself (Rosenthal, 2005; Lau & Rosenthal, 2011; Brown et al., 2019). HOT's condition is a representation of the particular state; FMT's is system-level closure of self-model and world-model. HOT's higher-order representation corresponds to FMT's extended rungs, and minimal and basic consciousness, where the self model is in the loop without taking itself as an object, have no higher-order representation and are phenomenal without one (Gruber, 2026a, §3.5, §7.2). What remains open is whether the floor self-model, a model of the system itself however simple, counts as a higher-order representation on HOT's terms; if it does, the conflict narrows.

*Evidence.* The debate over prefrontal involvement in conscious perception remains open (Odegaard et al., 2017; Boly et al., 2017). Metacognitive efficiency, measured as meta-d′/d′ so that first-order sensitivity is controlled (Fleming & Lau, 2014), varies independently of first-order performance across individuals and conditions (Rouault et al., 2018; Rahnev et al., 2020). This bears on the architecture, not on the point of conflict.

*Decider.* Disrupt the self-modelling loop itself, beyond metacognitive read-out, and score experience with no-report markers under fixed decision criteria (Gruber, 2026a, Table 1b; Tsuchiya et al., 2015; Nakamura et al., 2026). HOT predicts that experience of a state is lost where its higher-order representation is lost. FMT predicts that experience is lost where closure is lost and survives where closure is intact, including at the minimal and basic rungs. Abolishing metacognitive efficiency (meta-d′/d′ near zero) does not decide between them: HOT does not identify its higher-order representation with metacognitive report (Brown et al., 2019), and FMT predicts that experience survives metacognitive disruption while report may fail with it (Table 1b). The manipulation must show that it removed closure.

*Decides the contradiction?* HOT-1 and HOT-2: yes, once a protocol exists.

### C4. Perceptual reality monitoring: monitor or closure

*Point.* On PRM, a sensory representation is experienced when a higher-order monitor judges it a reliable reflection of the present world (Lau, 2022). FMT requires that the architecture preserve the distinction between live and offline runs of the explicit models (Gruber, 2026a, §6.0). It posits no marker on internally generated states, and makes closure, not the monitor's output, constitutive.

*Evidence.* Reality judgements rest on the combined strength of sensory activity, whether internally or externally generated (Dijkstra & Fleming, 2023). FMT reads this as evidence that source attribution is the fragile term (§6.0).

*Decider.* FMT predicts that under perturbation of the substrate or of communication between its levels, source attribution degrades before phenomenal experience does (§6.0). PRM predicts that experience follows the monitor's output. A graded perturbation, pharmacological or by sleep stage, that tracks reality judgements and experience reports separately can decide between them, provided the subpersonal monitor's output can be read from something other than the explicit reality judgement. A mis-monitored internal representation experienced as perception is predicted by both accounts and does not discriminate.

*Decides the contradiction?* PRM-1: yes, given an independent read-out of the monitor.

### C5. RPT: is local recurrence sufficient?

*Point.* RPT holds that recurrent processing within sensory cortex suffices for phenomenal experience, unreported and unattended, and that widespread recurrence with fronto-parietal areas adds access and report (Lamme, 2006, 2010). FMT agrees that recurrence is the mechanism; recurrent processing likely implements the running simulation (Principle 2; Gruber, 2026a, §7.2). On Principle 3, however, a locally recurrent sensory loop that has no self-model in its update rule is a simulation without an inside (§3.4.3, Stages 1 and 2).

*Evidence.* Masking studies, the loss of V1 figure-ground modulation under anaesthesia (Lamme et al., 1998), and a fragile high-capacity visual store (Sligte et al., 2008) support RPT. FMT reads the overflow cases as phenomenal content of a thin self-model with too little recursion above it for that content to be reported (§3.4.6).

*Decider.* A state in which local sensory recurrence is preserved and self-model dynamics are abolished, scored with no-report markers. Candidates are isolated or disconnected cortical tissue of the kind discussed as islands of awareness (Bayne et al., 2020), anaesthetic or dissociative states that preserve figure-ground modulation, and in-silico ablations. RPT predicts experience. FMT predicts none where the manipulation removed closure, and experience where the isolated tissue closes a loop of its own (§4.4, §8.12). A positive result therefore counts for RPT only where the tissue is shown not to close: in inspectable systems by the white-box trace of Table 1b, in vivo by no protocol yet accepted. The overflow claim (RPT-3) is not decided by these cases: both readings predict the partial-report data (§3.4.6) and differ on what access is.

*Decides the contradiction?* RPT-1: yes, once a manipulation is shown to remove closure. RPT-3: no.

### Differential content without a contradiction: PP, FEP and REBUS

PP's machinery is absorbed (Table 1), and most PP authors do not offer PP as a theory of consciousness (Hohwy & Seth, 2020; Gruber, 2026a, §7.2), so no contradiction is recorded. Markov blankets can be drawn around systems no theory counts as conscious (Bruineberg et al., 2022), and FEP as a general principle receives N. On the same ground FMT adds content: dose-dependent improvement of anosognosia below ego-dissolution doses, strongest in disconnection-type cases (Prediction 1), and identity content during ego dissolution under salvinorin A that tracks the most salient content in the environment (Prediction 2; Gruber, 2026a, §8.2–8.3). REBUS (Carhart-Harris & Friston, 2019) with Fotopoulou's (2014) predictive-coding account of anosognosia yields the coarse form of Prediction 1; the fine structure (dose dependence below ego dissolution, lesioned-hemisphere complexity, the disconnection boundary) is FMT's (§8.2). Input tracking as such in Prediction 2 is shared with PP: relaxed self-priors plus per-channel precision let the most precise channel set belief about the self. The two part where salience and bodily contingency come apart. PP accounts of bodily self-attribution weight heartbeat-synchronised signals (Suzuki et al., 2013; Aspell et al., 2013) and predict identity following a faint synchronised stream; FMT predicts identity following a salient unsynchronised one, tested in a 2 × 2 salience × synchrony design with an under-drug check that contingency-driven self-attribution is intact (§8.3). A failure of Prediction 1, or of Prediction 2's salience claim, counts against FMT's mechanism and leaves PP untouched.

### C6. AST and illusionism: are phenomenal properties real?

*Point.* AST holds that the brain's simplified model of its own attention is the source of claims to subjective awareness: the claims describe a real process, attention, in a caricatured form, and the non-physical experiential essence they depict does not exist (Graziano, 2013, 2024), a "small" illusionism in Graziano's (2024) term. Strong illusionism holds that introspection misrepresents quasi-phenomenal properties as phenomenal, and that there are no phenomenal properties (Frankish, 2016). FMT agrees that the substrate has no phenomenal properties and that the self-model's opacity to its substrate produces the sense of mystery (Gruber, 2026a, §3.8), and holds that phenomenal properties exist at the computational level (§3.4.5).

*Evidence.* None decisive; both sides explain the reports.

*Decider.* No empirical decider exists. The source text states that whether this disagreement is substantive or a relabeling "cannot be settled by empirical observation from outside the system" (§3.4.5). The difference is practical: if FMT is right, a system built to its specification has phenomenal states and is a moral patient for that reason; on strong illusionism any such status has to rest on something other than phenomenal properties. Against AST the conflict may be narrower than against strong illusionism, since FMT also places the experiential properties in a model and denies them to the substrate; what remains is whether the model's depiction is accurate at its own level.

*Decides the contradiction?* AST-1, ILL-1: no.

### C7. Self-model theory: selves and minimal phenomenal experience

*Point.* (a) Metzinger (2003) holds that no one ever was or had a self; FMT holds that the self is real as a running virtual process, and the disagreement may be verbal. (b) Metzinger's minimal phenomenal experience (MPE) programme describes reports of "pure awareness" that are characterised as contentless and selfless, and models their prototype as a representation of tonic alertness (Metzinger, 2020). If phenomenality occurs with no self-model at all, Principle 3 is false.

*FMT's reply.* The floor of the ladder is itself a rudimentary closure (Gruber, 2026a, §3.5, §7.2), so a state at the minimum of content and recursion retains an implicit boundary between self and world, though nothing in it represents a self. Reports of MPE pass through memory and language and are reconstructions made at the recursive rungs, and a state with no represented self leaves nothing in the report to describe as one. On this reading "selfless" records the absence of a represented self, which FMT accepts.

*Decider.* A measure of self-model activity, independent of the default mode network (which FMT does not identify with the ESM; Gruber, 2026a, Table 1, footnote c), recorded during verified MPE episodes. FMT predicts a minimal but non-zero self-modelling signature. The strict selfless reading predicts none.

*Decides the contradiction?* SMT-3: yes; the measure does not yet exist.

### C8. IWMT: self-location or self-reference

*Point.* IWMT's criterion for consciousness includes integrated selfhood alongside spatial, temporal and causal coherence and workspace-capable dynamics (Safron, 2020). The point of conflict is what selfhood requires. A system that jointly infers its own pose and a world map, as in G-SLAM (Safron et al., 2022) or a satellite navigation unit, locates itself without modelling itself as the modelling system (Gruber, 2026a, §7.3). On FMT a self model is a model of the system itself, and a position estimate alone is not one (§3.4.3, §3.5; F-SM1).

*Decider.* A system with high coherence and self-location and no self-reference. If IWMT's integrated selfhood is met by joint inference of self-pose and world, IWMT assigns such a system a non-zero degree and FMT assigns none. If IWMT requires the system to model itself as the modeller, the two criteria coincide on this case and no contradiction remains. Only artificial systems allow the case to be built, and behaviour does not establish experience.

*Decides the contradiction?* IWMT-1: architecture only.

### C9. ICT: informational closure or self-referential closure

*Point.* ICT identifies conscious processes with processes that form non-trivial informational closure with respect to the environment at a coarse-grained scale: their own state predicts their future while they carry information about the environment (Chang et al., 2020). It requires no self-model, so any coarse-grained process with non-trivial informational closure qualifies, to the degree of its closure. FMT's closure requires the self-model to enter the world model's update rule.

*Decider.* Two systems with matched informational closure at a coarse scale, one with and one without a self-model in the world model's update loop, compared on redeployment and sample efficiency at matched budget (Gruber, 2026c). FMT predicts a difference; ICT predicts none in consciousness. Behaviour does not establish consciousness (Gruber, 2026a, §8.11).

*Decides the contradiction?* ICT-1: architecture only.

### C10. Biological naturalism: is biology required?

*Point.* Searle (1980, 1992) holds that brains cause consciousness by their specific causal powers, that implementing a program is never by itself sufficient, and that a simulation is not a duplication; he allows that a non-biological system with causal powers equivalent to the brain's could be conscious. Seth (2025) argues that consciousness may depend on being alive, on autopoiesis and interoceptive self-regulation, and that computation alone is probably insufficient. FMT holds that the sufficient conjunction, whose pain-pleasure axis may be engineered, suffices on any substrate, and treats interoceptive regulation of a body-model as one route to the self-model (Gruber, 2026a, §3.7.3, §4.4, §7.2).

*Evidence.* Corvids, cephalopods, and olfaction's thalamus-free route to cortex show that the architecture has more than one anatomical realizer (§4.4). All are biological, so none decides the question.

*Decider.* An artificial implementation of the full architecture, which does not exist (§8.10). Intermediate: the testable form of biological naturalism distinguished by Klatzmann and Doerig (2026) names the biological property and asks whether a non-biological system that has the property differs from one that lacks it. Partial implementations give graded predictions (§8.10).

*Decides the contradiction?* BN-S1, BN-Seth1: no at present. An artificial implementation of the full architecture would supply the case and then face the problem of other minds; the intermediate tests separate architectures only.

### C11. Enactivism: representation and continuity of life and mind

*Point.* Strong enactivism holds that cognition and experience are enacted in the sensorimotor activity of a living, embodied system and are not constituted by internal representations of a pre-given world (Varela et al., 1991; Thompson, 2007). FMT holds that experience is a running internal simulation. The thesis of deep continuity between life and mind attributes some form of mind to all living systems. If that mind includes experience, it conflicts with FMT, on which systems below self-referential closure lack phenomenal experience regardless of behavioural sophistication (Gruber, 2026a, §6.4).

*Evidence.* Dreaming runs on internally generated input while sensory input is gated and motor output blocked (§6.3). Imagery and locked-in states show experience without ongoing sensorimotor coupling. The enactivist reply appeals to sensorimotor history; history of that kind is what FMT's implicit models store.

*Decider.* Experience in a system whose models were never trained through sensorimotor coupling. FMT's commitments do not exclude it; enactivism does.

*Decides the contradiction?* ENA-1: no at present; it requires an artificial implementation and then faces the problem of other minds. ENA-2: no; no measure of experience exists for living systems below closure (F-INS1).

## 6. Figures

### 6.1 Figure 1 — The reference architecture with theories overlaid

![](figures/theory-map-popsci.png){width=100%}

**Figure 1.** *The Four-Model Theory's architecture with the other theories placed on the component their central claim is about. Green: FMT absorbs the theory's core mechanism. Blue: compatible, with a different emphasis. A red dot marks a theory with at least one claim FMT contradicts; Table 1 names the claims and Section 5 gives the records. Verdicts are the author's (single coder).*

### 6.2 Figure 2 — Levels addressed by each theory

![](figures/theory-map-levels.png){width=100%}

**Figure 2.** *Rows are levels of description, columns are theories. A filled cell means the theory makes a claim at that level; its colour gives FMT's verdict on that claim (a split cell carries two claims with different verdicts). Hatched cells in the FMT column mark levels where FMT makes a claim but has no mechanism, protocol or formal model of its own.*

In the FMT column three levels are hatched: substrate/cellular (no cellular mechanism of its own), closure (no accepted measurement protocol for closure) and formal model (formalisation in progress, Gruber, 2026b).

### 6.3 The claim graph

**Table 2. Claim graph: relations between FMT's atomic claims and rival claims.** Relations: entails or matches, compatible, contradicts (with its record in Section 5), implemented by. Prediction nodes hang from the FMT claims they test.

Rival claim nodes are the claims named in Table 1, under the identifiers given there, one node per verdict except N, which draws no edge.

| FMT claim | Relation | Rival claim | Record |
|---|---|---|---|
| F-ID1 | contradicts | IIT-1 | C1 |
| F-CL1 | contradicts | IIT-2 | C1 |
| F-RV2 | contradicts | IIT-3 | C1 |
| F-ID1, F-P2 | entails | IIT-4 | — |
| F-VQ3 | entails | IIT-5 | — |
| F-CH3 | contradicts | GNW-1 | C2 |
| F-CH2, F-CH3 | entails | GNW-2 | — |
| F-LAD0 | contradicts | GNW-3 | C2 |
| F-CH3 | entails | GNW-4 | — |
| F-CH3 | contradicts | CTM-1 | C2 |
| F-FM4 | contradicts | CTM-2 | C2 |
| F-NEST | entails | CTM-3 | — |
| F-RV1, F-RV2 | implemented-by | PP-1 | — |
| F-RV2, F-MOD1 | entails | PP-2 | — |
| F-2X2, F-RV2 | implemented-by | BM-1 | — |
| F-PERM1 | implemented-by | REBUS-1 | — |
| F-P3, F-SM1 | compatible | BL-1 | — |
| F-LAD2 | contradicts | HOT-1 | C3 |
| F-CL1 | contradicts | HOT-2 | C3 |
| F-LAD1 | entails | HOT-3 | — |
| F-P3 | contradicts | PRM-1 | C4 |
| F-SRC1 | entails | PRM-2 | — |
| F-CL1 | contradicts | RPT-1 | C5 |
| F-P2 | entails | RPT-2 | — |
| F-AP1, F-LAD3 | contradicts | RPT-3 | C5 |
| F-VQ1 | contradicts | AST-1 | C6 |
| F-CH4 | compatible | AST-2 | — |
| F-MP1, F-CH4 | entails | AST-3 | — |
| F-P3, F-MP1 | entails | SMT-1 | — |
| F-DEF2 | entails | SMT-2 | — |
| F-P3 | contradicts | SMT-3 | C7 |
| F-SM1 | contradicts | IWMT-1 | C8 |
| F-2X2 | entails | IWMT-2 | — |
| F-FM3 | entails | IWMT-3 | — |
| F-P2 | compatible | IWMT-4 | — |
| F-CH1, F-CH5 | implemented-by | DIT-1 | — |
| F-CL1 | contradicts | ICT-1 | C9 |
| F-P3, F-P2 | entails | ICT-2 | — |
| F-VQ1 | contradicts | ILL-1 | C6 |
| F-MP1 | entails | ILL-2 | — |
| F-SI1 | contradicts | BN-S1 | C10 |
| F-SI1 | compatible | BN-S2 | — |
| F-SI1 | contradicts | BN-Seth1 | C10 |
| F-FM2, F-2X2 | entails | BN-Seth2 | — |
| F-MOD1 | contradicts | ENA-1 | C11 |
| F-INS1 | contradicts | ENA-2 | C11 |
| F-FM2 | compatible | ENA-3 | — |

Prediction edges: F-PR1 and F-PR2 from F-PERM1; F-PR2 also from F-P3 and F-FORK1; F-PR3 from F-FORK1; F-PR4 from F-FM3 and F-LAD1; F-PR5 from F-VQ3; F-PR6 from F-MP1; F-PR7 from F-TE1 and F-CL1; F-PR8 from F-VQ1 and F-P3; F-FAL1 from F-FM1; F-FAL2 from F-CL1; F-FAL3 from F-RV1.

## 7. Scope and Limits

Proponents of the other theories may place their claims differently or reject the decomposition.

Claims without a counterpart in FMT, such as IIT's exclusion postulate, appear as neutral and receive no further analysis. Where the source text does not address a particular claim, the verdict on it is derived from FMT's stated commitments.

**Table 3. Contradiction records, their deciders and what the deciders decide.**

| Record | Contradicted claims | Decider | Decides the contradiction? | Status |
|---|---|---|---|---|
| C1 IIT | IIT-1, IIT-2, IIT-3 | Block or lesion of non-firing units inside the complex (i); closed system against its unfolded twin under a resource bound (ii) | IIT-3 yes; IIT-1, IIT-2 no ((ii) architecture only) | (i) available in principle; (ii) in silico |
| C2 GNW, CTM | GNW-1, GNW-3, CTM-1, CTM-2 | Self-modelling loop disrupted with ignition intact, no-report markers, fixed criteria; the converse for GNW-3 | GNW-1, GNW-3, CTM-1 yes; CTM-2 no | No accepted protocol; in silico architecture only |
| C3 HOT | HOT-1, HOT-2 | Self-modelling loop disrupted beyond metacognitive read-out, no-report markers | yes | No accepted protocol |
| C4 PRM | PRM-1 | Graded perturbation tracking reality judgements and experience separately | yes | Available in principle |
| C5 RPT | RPT-1, RPT-3 | Local recurrence preserved, self-model loop removed, no-report markers | RPT-1 yes; RPT-3 no | No clean protocol in vivo; in silico |
| C6 AST, illusionism | AST-1, ILL-1 | None | no | No empirical decider |
| C7 SMT | SMT-3 | Self-model signature during verified MPE episodes | yes | Measurement immature |
| C8 IWMT | IWMT-1 | A self-locating system without self-reference | architecture only | In silico |
| C9 ICT | ICT-1 | Matched informational closure with and without a self-model in the loop | architecture only | In silico |
| C10 Searle, Seth | BN-S1, BN-Seth1 | Artificial implementation of the full architecture | no | Requires artificial implementation |
| C11 Enactivism | ENA-1, ENA-2 | Experience in a system never trained through sensorimotor coupling | no | Requires artificial implementation |

The ledger of contradicted claims holds twenty-one claims in eleven records (Table 3). The named experiment decides nine of them: two can be run in principle now (IIT-3, PRM-1), six wait on a protocol that disrupts the self-modelling loop and shows that it removed closure rather than relocating it (GNW-1, GNW-3, CTM-1, HOT-1, HOT-2, RPT-1), and one on a measure of self-model activity during verified MPE (SMT-3). Two are separated at the level of architecture only, since behaviour does not establish experience (IWMT-1, ICT-1). Ten have no empirical decider: four would need an artificial implementation of the full architecture and then face the problem of other minds (CTM-2, BN-S1, BN-Seth1, ENA-1), four concern phenomenal ontology (IIT-1, RPT-3, AST-1, ILL-1), and two concern systems for which no measure of experience exists (IIT-2, ENA-2).

The share of N verdicts in Table 1 is low (eight of fifty-five cells), which is consistent with a frame that reaches the levels the theories address and also with a coder who places claims where the frame has components; only a second coder and a second frame separate these. Until an independent coder has coded Table 1 from the same sources, the A/C line in particular is the author's.

What would count against FMT in the records above: a rival-side result in any record whose decider decides. No-report markers of experience surviving removal of closure (C2, C3, C5), experience following the monitor's output under graded perturbation (C4), or no self-model signature in verified MPE (C7) would each be a case of phenomenality without closure, and Principle 3 fails as an identity on one such case. The mechanism absorptions in Table 1 would survive that result; the constitution claim would not.

## 8. Conclusion

At the level of atomic claims, FMT and the theories compared here mostly agree about mechanism and disagree about what is sufficient for experience and whether its phenomenal character is real. The claim set of the reference theory is supplied in a form that graph-based comparison programmes can ingest, so that the same exercise can be run with any other theory as the reference frame.

## Supplementary material

`fmt-claims.json`: FMT atomic claims as subject–predicate–object triples with section, type, core or periphery, and dependencies.

`fmt-prediction-map.json`: the FMT prediction map (65 nodes, levels A to F) with its inferential edges.

## Declaration of AI use

The ideas, arguments and verdicts are the author's, from his German-language work (Gruber, 2015) and the Four-Model Theory. Claude (Anthropic), a large language model, was used to render them into English, to improve the language, to check the verdicts against the cited sources and to check references. The author reviewed everything and is responsible for all content.

## Competing interests

None.

## References

Albantakis, L., Barbosa, L., et al. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms. *PLOS Computational Biology*, 19(10), e1011465.

Aru, J., Suzuki, M., & Larkum, M.E. (2020). Cellular mechanisms of conscious processing. *Trends in Cognitive Sciences*, 24(10), 814–825. https://doi.org/10.1016/j.tics.2020.07.006

Aspell, J.E., Heydrich, L., Marillier, G., Lavanchy, T., Herbelin, B., & Blanke, O. (2013). Turning body and self inside out: Visualized heartbeats alter bodily self-consciousness and tactile perception. *Psychological Science*, 24(12), 2445–2453. https://doi.org/10.1177/0956797613498395

Baars, B.J. (1988). *A Cognitive Theory of Consciousness*. Cambridge University Press.

Bandara, K.H., Rowe, E.G., & Garrido, M.I. (2026). Testing the spatiotemporal predictions of global neuronal workspace theory and integrated information theory. *bioRxiv*. https://doi.org/10.64898/2026.07.16.738188

Bayne, T., Seth, A.K., & Massimini, M. (2020). Are there islands of awareness? *Trends in Neurosciences*, 43(1), 6–16. https://doi.org/10.1016/j.tins.2019.11.003

Blum, L., & Blum, M. (2022). A theory of consciousness from a theoretical computer science perspective: Insights from the Conscious Turing Machine. *Proceedings of the National Academy of Sciences*, 119(21), e2115934119. https://doi.org/10.1073/pnas.2115934119

Boly, M., Massimini, M., Tsuchiya, N., Postle, B.R., Koch, C., & Tononi, G. (2017). Are the neural correlates of consciousness in the front or in the back of the cerebral cortex? Clinical and neuroimaging evidence. *Journal of Neuroscience*, 37(40), 9603–9613. https://doi.org/10.1523/JNEUROSCI.3218-16.2017

Brown, R., Lau, H., & LeDoux, J.E. (2019). Understanding the higher-order approach to consciousness. *Trends in Cognitive Sciences*, 23(9), 754–768.

Bruineberg, J., Dolega, K., Dewhurst, J., & Baltieri, M. (2022). The Emperor's new Markov blankets. *Behavioral and Brain Sciences*, 45, e183. https://doi.org/10.1017/S0140525X21002351

Carhart-Harris, R.L., & Friston, K.J. (2019). REBUS and the anarchic brain: Toward a unified model of the brain action of psychedelics. *Pharmacological Reviews*, 71(3), 316–344.

Chang, A.Y.C., Biehl, M., Yu, Y., & Kanai, R. (2020). Information closure theory of consciousness. *Frontiers in Psychology*, 11, 1504. https://doi.org/10.3389/fpsyg.2020.01504

Changeux, J.-P., & Farisco, M. (2026). The global neuronal workspace as a multilevel model of conscious processing. *Trends in Cognitive Sciences*, 30(6), 477–479. https://doi.org/10.1016/j.tics.2026.03.004

COGITATE Consortium. (2025). Adversarial testing of global neuronal workspace and integrated information theories of consciousness. *Nature*, 642(8066), 133–142. https://doi.org/10.1038/s41586-025-08888-1

Dehaene, S., & Changeux, J.P. (2011). Experimental and theoretical approaches to conscious processing. *Neuron*, 70(2), 200–227.

Dehaene, S., Changeux, J.P., Naccache, L., Sackur, J., & Sergent, C. (2006). Conscious, preconscious, and subliminal processing: A testable taxonomy. *Trends in Cognitive Sciences*, 10(5), 204–211.

Dennett, D.C. (1991). *Consciousness Explained*. Little, Brown and Company.

Dijkstra, N., & Fleming, S.M. (2023). Subjective signal strength distinguishes reality from imagination. *Nature Communications*, 14, 1627. https://doi.org/10.1038/s41467-023-37322-1

Doerig, A., Schurger, A., Hess, K., & Herzog, M.H. (2019). The unfolding argument: Why IIT and other causal structure theories cannot explain consciousness. *Consciousness and Cognition*, 72, 49–59. https://doi.org/10.1016/j.concog.2019.04.002

Fleming, S.M., & Lau, H.C. (2014). How to measure metacognition. *Frontiers in Human Neuroscience*, 8, 443. https://doi.org/10.3389/fnhum.2014.00443

Fotopoulou, A. (2014). Time to get rid of the 'Modular' in neuropsychology: A unified theory of anosognosia as aberrant predictive coding. *Journal of Neuropsychology*, 8(1), 1–19. https://doi.org/10.1111/jnp.12010

Frankish, K. (2016). Illusionism as a theory of consciousness. *Journal of Consciousness Studies*, 23(11–12), 11–39.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138.

Graziano, M.S.A. (2013). *Consciousness and the Social Brain*. Oxford University Press.

Graziano, M.S.A. (2024). Illusionism big and small: Some options for explaining consciousness. *eNeuro*, 11(10), ENEURO.0210-24.2024.

Gruber, M. (2015). *Die Emergenz des Bewusstseins*. Lulu Press. ISBN 978-1-326-65207-4. https://doi.org/10.5281/zenodo.23538664

Gruber, M. (2026a). The Four-Model Theory of consciousness: A simulation-based framework unifying the hard problem, binding, and altered states. *Zenodo* preprint. https://doi.org/10.5281/zenodo.18669891

Gruber, M. (2026b). Toward a mathematical formalization of the Four-Model Theory: A recommended approach. *Zenodo* preprint. https://doi.org/10.5281/zenodo.21843693

Gruber, M. (2026c). In-silico tests of the four-model architecture: Self-referential closure, self-modelling and criticality in model systems. *Zenodo* preprint. https://doi.org/10.5281/zenodo.21610993

Gurnee, W., Sofroniew, N., Pearce, A., Piotrowski, M., Kauvar, I., Chen, R., Soligo, A., Bogdan, P., Ong, E., Wang, R., Thompson, B., Abrahams, D., Kantamneni, S., Ameisen, E., Batson, J., & Lindsey, J. (2026). Verbalizable representations form a global workspace in language models. *arXiv* preprint arXiv:2607.15495.

Hohwy, J., & Seth, A. (2020). Predictive processing as a systematic basis for identifying the neural correlates of consciousness. *Philosophy and the Mind Sciences*, 1(II), 3. https://doi.org/10.33735/phimisci.2020.II.64

Klatzmann, U., & Doerig, A. (2026). What biology can and cannot tell us about conscious AI. *Trends Open*, 1(4), 662–671. https://doi.org/10.1016/j.treopn.2026.07.012

Lamme, V.A.F. (2006). Towards a true neural stance on consciousness. *Trends in Cognitive Sciences*, 10(11), 494–501.

Lamme, V.A.F. (2010). How neuroscience will change our view on consciousness. *Cognitive Neuroscience*, 1(3), 204–220.

Lamme, V.A.F., Zipser, K., & Spekreijse, H. (1998). Figure-ground activity in primary visual cortex is suppressed by anesthesia. *Proceedings of the National Academy of Sciences*, 95(6), 3263–3268. https://doi.org/10.1073/pnas.95.6.3263

Lau, H. (2022). *In Consciousness We Trust: The Cognitive Neuroscience of Subjective Experience*. Oxford University Press. https://doi.org/10.1093/oso/9780198856771.001.0001

Lau, H., & Rosenthal, D. (2011). Empirical support for higher-order theories of conscious awareness. *Trends in Cognitive Sciences*, 15(8), 365–373.

Laukkonen, R.E., Friston, K.J., & Chandaria, S. (2025). A beautiful loop: An active inference theory of consciousness. *Neuroscience & Biobehavioral Reviews*, 176, 106296. https://doi.org/10.1016/j.neubiorev.2025.106296

Mashour, G.A., Roelfsema, P., Changeux, J.-P., & Dehaene, S. (2020). Conscious processing and the global neuronal workspace hypothesis. *Neuron*, 105(5), 776–798. https://doi.org/10.1016/j.neuron.2020.01.026

Metzinger, T. (2003). *Being No One: The Self-Model Theory of Subjectivity*. MIT Press.

Metzinger, T. (2020). Minimal phenomenal experience: Meditation, tonic alertness, and the phenomenology of "pure" consciousness. *Philosophy and the Mind Sciences*, 1(I), 7. https://doi.org/10.33735/phimisci.2020.I.46

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

Suzuki, K., Garfinkel, S.N., Critchley, H.D., & Seth, A.K. (2013). Multisensory integration across exteroceptive and interoceptive domains modulates self-experience in the rubber-hand illusion. *Neuropsychologia*, 51(13), 2909–2917. https://doi.org/10.1016/j.neuropsychologia.2013.08.014

Suzuki, M., & Larkum, M.E. (2020). General anesthesia decouples cortical pyramidal neurons. *Cell*, 180(4), 666–676. https://doi.org/10.1016/j.cell.2020.01.024

Thompson, E. (2007). *Mind in Life: Biology, Phenomenology, and the Sciences of Mind*. Harvard University Press.

Tononi, G. (2004). An information integration theory of consciousness. *BMC Neuroscience*, 5, 42.

Tononi, G., Boly, M., Massimini, M., & Koch, C. (2016). Integrated information theory: From consciousness to its physical substrate. *Nature Reviews Neuroscience*, 17(7), 450–461. https://doi.org/10.1038/nrn.2016.44

Tsuchiya, N., Wilke, M., Frässle, S., & Lamme, V.A.F. (2015). No-report paradigms: Extracting the true neural correlates of consciousness. *Trends in Cognitive Sciences*, 19(12), 757–770.

Varela, F.J., Thompson, E., & Rosch, E. (1991). *The Embodied Mind: Cognitive Science and Human Experience*. MIT Press.

Wilterson, A.I., Kemper, C.M., Kim, N., Webb, T.W., Reblando, A.M.W., & Graziano, M.S.A. (2020). Attention control and the attention schema theory of consciousness. *Progress in Neurobiology*, 195, 101844. https://doi.org/10.1016/j.pneurobio.2020.101844

Yaron, I., Melloni, L., Pitts, M., & Mudrik, L. (2022). The ConTraSt database for analysing and comparing empirical studies of consciousness theories. *Nature Human Behaviour*, 6(4), 593–604. https://doi.org/10.1038/s41562-021-01284-5

