# Tracked Changes — Four-Model Theory (Full Paper)

**Purpose**: This is the working version of the full paper with proposed changes tracked inline. The canonical clean version remains at `four-model-theory-full.md`. Changes here are proposed additions/modifications for the journal submission (target: Physics of Life Reviews or BBS).

**Convention**:
- Proposed insertions are wrapped in: `<!-- [PROPOSED INSERTION — Source: X, Date: Y] -->` and `<!-- [END INSERTION] -->`
- Proposed deletions are wrapped in: `<!-- [PROPOSED DELETION — Source: X, Date: Y] -->` and `<!-- [END DELETION] -->`
- Proposed modifications show both old and new text
- All changes include source attribution and rationale

**Change Log**:
| Date | Source | Section | Type | Description |
|------|--------|---------|------|-------------|
| 2026-02-16 | Session 53, Perplexity review analysis | 6.7 (new) | Addition | Developmental Psychology Bridge |
| 2026-02-16 | Session 53, Perplexity review analysis | 4.2 | Addition | "Simulation must feel" functional necessity argument |
| 2026-02-16 | Session 53, Perplexity review analysis | 3.4 | Addition | Identity claim framing with H2O analogy |

---


# The Four-Model Theory of Consciousness: A Simulation-Based Framework Unifying the Hard Problem, Binding, and Altered States

**Matthias Gruber**

*Independent researcher*

*ORCID: 0009-0005-9697-1665*

*Correspondence: matthias@matthiasgruber.com*

---

## Abstract

The science of consciousness remains in a pre-paradigm state, with no theory simultaneously satisfying the eight core requirements a complete theory must meet: the Hard Problem, the Explanatory Gap, the Boundary Problem, the Structure of Experience, Unity and Binding, Combination and Emergence, the Causal Role, and the Meta-Problem. I present the Four-Model Theory, in which consciousness is constituted by real-time self-simulation across four nested models arranged along two axes — scope (world vs. self) and mode (implicit vs. explicit). The implicit models (Implicit World Model, Implicit Self Model) are substrate-level, learned, and non-conscious. The explicit models (Explicit World Model, Explicit Self Model) are virtual, transient, and phenomenal — they are the simulation in which experience occurs. The theory's central claim is that qualia are virtual: they are the way the simulated self perceives its own states within the simulation, not properties of the physical substrate. This dissolves the Hard Problem by showing that "Why does physical processing feel like something?" commits a category error — the physical processing does not feel; the simulation does, and within the simulation, qualia are constitutive. Combined with a criticality requirement (the substrate must operate at the edge of chaos), the theory derives diverse phenomena from five principles: criticality, virtual qualia, a redirectable Explicit Self Model, variable implicit-explicit permeability, and virtual model forking. These principles unify psychedelic phenomenology, anesthetic mechanisms, dream states, split-brain phenomena, dissociative identity disorder, and animal consciousness. A systematic comparison shows the theory addresses all eight requirements. Nine novel testable predictions are offered, including that psychedelic ego dissolution content is controllable via sensory input and that psychedelics should alleviate anosognosia — predictions few competing theories generate. The criticality requirement, derived from Wolfram's computational framework in 2015 independently of the empirical criticality program, converges with empirical criticality literature consolidated in 2025-2026 (Hengen & Shew, 2025; Algom & Shriki, 2026) — a decade-apart convergence from theoretical and empirical starting points.

**Keywords**: consciousness, hard problem, self-model, simulation, qualia, criticality, binding problem, altered states, psychedelics, substrate independence

---

## 1. Introduction

### 1.1 The Pre-Paradigm State of Consciousness Science

After three decades of intensive scientific investigation, consciousness research finds itself at an impasse. The field possesses no dominant paradigm in the Kuhnian sense (Kuhn, 1962), no agreed-upon methodology for linking subjective experience to objective measurement, and no theory that commands broad assent. Multiple frameworks compete for explanatory primacy — Integrated Information Theory (IIT; Tononi, 2004; Albantakis et al., 2023), Global Neuronal Workspace (GNW; Baars, 1988; Dehaene & Changeux, 2011), Higher-Order Theories (HOT; Rosenthal, 2005; Lau & Rosenthal, 2011), Predictive Processing (PP; Friston; Seth, 2021), Attention Schema Theory (AST; Graziano, 2013), Recurrent Processing Theory (RPT; Lamme, 2006, 2010), and others — yet none has established decisive empirical or theoretical superiority over its rivals.

Recent developments have deepened the crisis rather than resolving it. The COGITATE adversarial collaboration published equivocal results in *Nature* (COGITATE Consortium, 2025; protocol: Melloni et al., 2023): neither IIT nor GNW was fully confirmed, and the data favored posterior cortical involvement over either camp's predictions. A letter signed by over 100 researchers declared IIT pseudoscientific (IIT-Concerned et al., 2025), provoking fierce rebuttals (Tononi, Albantakis, et al., 2025) and methodological commentary (Gomez-Marin & Seth, 2025). Reviews published in 2024-2025 have asked whether the field is making genuine progress or merely accumulating incompatible frameworks (Frontiers in Psychology, 2025; Acta Analytica, 2024).

This paper argues that the impasse persists because no existing theory simultaneously addresses all of the fundamental requirements that a complete theory of consciousness must meet. Each theory excels on some requirements but remains silent on, or weak against, others. The field needs a framework that addresses the full set of challenges — not just neural correlates or access conditions, but the deep philosophical problems that make consciousness uniquely difficult.

### 1.2 What Would Count as Progress?

I propose that any theory claiming to provide a comprehensive account of consciousness must address eight core requirements, drawn from the philosophical and scientific literature. These requirements are not novel; each has been identified by previous authors as a central challenge. What is novel is the demand that a single theory address all eight simultaneously:

1. **The Hard Problem** (Chalmers, 1995) — Why does physical processing give rise to subjective experience?
2. **The Explanatory Gap** (Levine, 1983) — Why does the explanation of neural correlates feel incomplete?
3. **The Boundary Problem** (Bayne, 2010; Tononi, 2004) — Where does the conscious system end?
4. **The Structure of Experience** (Nagel, 1974) — How does physical processing produce richly structured experience?
5. **Unity and Binding** (Treisman & Gelade, 1980; Revonsuo, 1999) — How are distributed processes unified into coherent experience?
6. **Combination and Emergence** (Chalmers, 2016) — How do non-conscious elements combine to produce consciousness?
7. **The Causal Role** (Jackson, 1982) — Does consciousness do anything?
8. **The Meta-Problem** (Chalmers, 2018) — Why do we think there is a hard problem?

Section 2 develops each requirement in detail and surveys how existing theories fare against them. The remainder of the paper presents a theory — the Four-Model Theory — that, I argue, addresses all eight.

### 1.3 Overview and Historical Context

The Four-Model Theory was originally published in German as *Die Emergenz des Bewusstseins* (Gruber, 2015) and has been refined through a structured adversarial challenge process in 2026. The theory self-identifies as an intersection of Dennett's Multiple Drafts Model (Dennett, 1991), Metzinger's Self-Model Theory of Subjectivity (Metzinger, 2003, 2009), and neural network architecture. It is substrate-independent: the six-layer mammalian cortex is understood as an evolutionary implementation, not a requirement.

The theory proposes that consciousness consists of a real-time self-simulation running on an implicit (substrate-level) knowledge base. Qualia — the subjective "feel" of experience — are virtual: they exist within and are constitutive of the simulation, but do not exist at the substrate level. This two-level ontology dissolves the Hard Problem by showing it rests on a category error.

Combined with a criticality requirement derived independently from Wolfram's computational framework (Wolfram, 2002), the theory generates nine novel testable predictions and unifies phenomena across psychopharmacology, clinical neurology, sleep science, and comparative cognition under five principles.

The theory is offered as one model among several, contributing to humanity's collective search for an adequate account of consciousness. Every model carries inherent modeling error; the present theory is no exception. It is intended to complement existing frameworks — extending where they are incomplete, not displacing where they succeed.

The paper proceeds as follows. Section 2 establishes the eight requirements. Section 3 presents the Four-Model Theory. Sections 4 and 5 develop the philosophical commitments and the binding/criticality framework. Section 6 demonstrates the theory's explanatory range. Section 7 provides a systematic comparative analysis against major competitors. Section 8 presents the nine predictions. Sections 9-11 address open questions, implications, and conclusions.

---

## 2. Eight Requirements for a Theory of Consciousness

This section develops each of the eight requirements and briefly notes how current theories address or fail to address them. A detailed theory-by-theory comparison follows in Section 7; the purpose here is to establish the evaluative framework.

### 2.1 The Hard Problem

Chalmers (1995, 1996) formulated the Hard Problem as the question of why physical processing is accompanied by subjective experience. We can explain all the *functions* of consciousness — discrimination, integration, reporting, attention — without explaining why there is "something it is like" (Nagel, 1974) to undergo these processes. The explanatory challenge is not about identifying neural correlates but about understanding why correlates are accompanied by phenomenality at all.

Most neuroscientific theories of consciousness (GNW, RPT, PP) focus on functional or mechanistic accounts and remain explicitly or implicitly silent on the Hard Problem. IIT attempts to address it by defining consciousness as intrinsic causal power (Φ), treating experience as identical to integrated information — but this requires accepting panpsychist commitments that many find problematic (Aaronson, 2014; Doerig et al., 2019). HOT and AST offer deflationary accounts that explain *why we report* having phenomenal experience but leave open whether they have truly addressed the phenomenality itself. Illusionism (Dennett, 1991; Frankish, 2016) dissolves the problem by denying that qualia as traditionally conceived exist — a position that remains deeply controversial.

### 2.2 The Explanatory Gap

Levine (1983) identified the Explanatory Gap as a distinct problem from the Hard Problem: even if we identify every neural correlate of every conscious state, the explanation seems to leave something out. The gap is between the third-person description (neural firing patterns) and the first-person reality (what the experience is like). Block (1995, 2007) further refined this as the distinction between access consciousness (the functional role) and phenomenal consciousness (the subjective feel).

The Explanatory Gap is often treated as a restatement of the Hard Problem, but it has a distinct character: it is about the *form* of explanation rather than the *existence* of the phenomenon. A theory that dissolves the Hard Problem should simultaneously close the Explanatory Gap.

### 2.3 The Boundary Problem

Where does the conscious system begin and end? Within the brain, only some processing is conscious at any given moment. Between organisms, it is unclear where to draw the line. The Boundary Problem asks for a principled account of what delineates conscious from non-conscious processing (see Bayne, 2010; Tononi, 2004).

IIT provides the strongest existing treatment of this requirement through its exclusion postulate: the system with maximum Φ defines the boundary of consciousness. However, the computational intractability of calculating Φ limits its practical application. GNW defines conscious access in terms of global broadcasting, but the boundary between broadcast and non-broadcast content is not always sharp. PP uses Markov blankets (Friston, 2010) but has been criticized for being too liberal in its boundary-setting (Bruineberg et al., 2022).

### 2.4 The Structure of Experience

Conscious experience is not a homogeneous blob — it has rich spatial, temporal, modal, and qualitative structure. A visual scene has colors, shapes, depths, and textures; an auditory experience has pitches, timbres, and spatial locations; emotional experience has valence, intensity, and phenomenal character. Any complete theory must explain how physical processing generates this structured phenomenology.

IIT's qualia space provides a mathematical treatment of experiential structure, arguably its greatest strength. PP's generative models are inherently structured, providing a natural account of the richness of perceptual experience. GNW and HOT are weaker here, offering accounts of *when* content becomes conscious but less about *why* it has the particular structure it does.

### 2.5 Unity and Binding

The Binding Problem (Treisman, 1996; Revonsuo, 1999) asks how distributed neural processes — occurring in different brain regions, at different timescales, in different modalities — are unified into a single coherent conscious experience. I see a red ball: "red," "round," "ball," "there," and "now" are processed in different cortical areas, yet I experience a unified percept.

Proposed solutions range from temporal synchrony (Gray et al., 1989; Singer & Gray, 1995; Fries, 2005, 2015) to integrated information (Tononi, 2004) to global broadcasting (Baars, 1988). None is universally accepted. The binding problem remains, alongside the Hard Problem, one of the deepest unresolved challenges.

### 2.6 Combination and Emergence

How do non-conscious elements combine to produce consciousness? For panpsychist theories (IIT in its strong form; Goff, 2019; Strawson, 2006), this takes the form of the Combination Problem (James, 1890; Chalmers, 2016): if fundamental entities have micro-experience, how do these micro-experiences combine into the macro-experience we know? For physicalist theories, the challenge is one of emergence: at what point, and by what mechanism, does consciousness emerge from non-conscious physical processes?

The Combination Problem is widely regarded as panpsychism's most serious difficulty (Chalmers, 2016; Coleman, 2014). Physicalist emergence theories face the objection that they either invoke strong emergence (which many philosophers consider mysterious) or reduce consciousness to function (which many consider inadequate). A satisfactory theory must navigate between these difficulties.

### 2.7 The Causal Role of Consciousness

Does consciousness *do* anything, or is it epiphenomenal — a by-product with no causal power? If consciousness has causal power, what kind? If it does not, why does it exist?

This requirement is politically charged within the field. Epiphenomenalism (Huxley, 1874; Jackson, 1982) is widely dismissed as absurd (how could evolution produce something causally inert?), yet many mechanistic theories implicitly struggle with the question. If consciousness is "just" a global broadcast (GNW) or "just" recurrent processing (RPT), what role does the *experience* play beyond the mechanism? The PP framework, through active inference, provides perhaps the strongest existing case for consciousness having a functional role, but it is unclear whether the functional role requires phenomenal consciousness rather than mere information processing.

### 2.8 The Meta-Problem

Chalmers (2018) identified the Meta-Problem: why do we *think* there is a Hard Problem? Even if the Hard Problem is illusory (as illusionists argue) or misformulated (as functionalists hold), it is a fact that most humans — including most philosophers and scientists — report a strong intuition that consciousness is deeply mysterious. A complete theory should explain this intuition.

AST provides the strongest existing account of the Meta-Problem: we model our own attention, and the model necessarily omits the mechanistic details, leading to the intuition that consciousness is something non-physical (Graziano, 2013). This is a genuine insight. However, AST's treatment of the Meta-Problem does not extend to a solution of the Hard Problem itself — it explains why we *think* there is a mystery without fully accounting for the mystery.

---

## 3. The Four-Model Theory

### 3.1 Core Definition

Consciousness is the ability of an entity — biological or artificial — to create a model of itself, to relate that model to itself, and to interact with it. Consciousness is not a property the brain possesses but a process the brain performs: it runs a real-time self-simulation.

This definition is functional and substrate-independent. It does not require a specific physical implementation, biological composition, or computational architecture. What it requires is a system capable of constructing and maintaining a self-referential simulation in real time.

### 3.2 The Four Models

The theory identifies four nested models distinguished by two orthogonal dimensions: **scope** (everything vs. self only) and **mode** (implicit/learned vs. explicit/simulated). This is a conceptual taxonomy, not a claim about spatial organization in the brain — the models are functionally distinct processes, not anatomically localized regions.

**Table 1. The Four-Model Architecture**

| | Everything (world) | Self only |
|---|---|---|
| **Implicit** (learned, substrate-level) | Implicit World Model (IWM) | Implicit Self Model (ISM) |
| **Explicit** (simulated, phenomenal) | Explicit World Model (EWM) | Explicit Self Model (ESM) |

**The Implicit World Model (IWM)** encompasses the substrate's total accumulated knowledge about the world, stored in synaptic weights (or their functional equivalent in non-biological substrates). It includes everything the system has ever learned: perceptual regularities, causal models, spatial relationships, semantic knowledge, motor programs for interacting with the world. The IWM is never directly conscious. It operates "in the dark" — providing the knowledge base from which the conscious simulation is generated, but never itself appearing in experience.

**The Implicit Self Model (ISM)** is the substrate's accumulated self-knowledge: body schema, proprioceptive calibration, motor skills, habits, personality traits, autobiographical memory structures, and social self-knowledge. Like the IWM, the ISM is never directly conscious. There is no unified homunculus — no inner observer reading the ISM. The ISM is a structural feature of the substrate, not an experiential one.

**The Explicit World Model (EWM)** is the conscious world — the real-time simulation of reality that constitutes perceptual experience. When you see a room, hear a voice, feel the texture of a surface, you are experiencing the EWM. It is generated from the IWM (which provides the world-knowledge) and current sensory input (which constrains and updates the simulation), but it is not identical to either. The EWM is a virtual construct — a transient pattern of activity, not a permanent structure.

**The Explicit Self Model (ESM)** is the conscious self — the real-time simulation of "I" that constitutes self-experience. It is the sense of being a subject, having a perspective, occupying a body, possessing a history, and being the author of one's actions. The ESM is generated from the ISM (which provides the self-knowledge) and current interoceptive and proprioceptive input, but like the EWM, it is virtual: a transient process, not a permanent entity.

### 3.3 The Real/Virtual Split

The four models divide into two fundamental categories:

**The real side** (IWM + ISM): These are physical, structural, learned, and non-conscious. They are stored in the substrate's architecture — in biological brains, primarily in synaptic weights, dendritic morphology, and connectivity patterns. They accumulate over the organism's lifetime through learning. They have no phenomenal character. "Lights off."

**The virtual side** (EWM + ESM): These are simulated, transient, generated, and phenomenal. They are patterns of activity — in biological brains, transient electrochemical dynamics. They are constructed in real time from the implicit models and current sensory input. They *are* experience. "Lights on."

This division is the foundation of the theory's treatment of the Hard Problem (Section 3.4) and structures its account of every phenomenon it addresses.

The virtual models possess **software-like properties** that follow from their nature as simulations rather than structures:

- **They can be forked**: A single substrate can run multiple configurations of the ESM (see Section 6.2 on dissociative identity disorder).
- **They can be cloned**: Physical separation of the substrate produces degraded but complete copies of the virtual models (see Section 6.4 on split-brain).
- **They can be redirected**: The ESM requires input; disrupt normal self-referential input and it latches onto whatever input dominates (see Section 6.1 on psychedelics).
- **They can be reconfigured**: Therapeutic interventions (CBT, exposure therapy) work by modifying the virtual models through substrate-level rewiring (see Section 6.6).

### 3.4 Virtual Qualia: Dissolving the Hard Problem

The central claim of the Four-Model Theory is that **qualia are virtual**. They are the way the simulated self (ESM) perceives its own states and the simulated world (EWM). Qualia exist within and are constitutive of the simulation; they do not exist at the substrate level.

This dissolves the Hard Problem by revealing a category error in its formulation:

**The standard formulation**: "Why does physical processing (neuronal firing, synaptic transmission) feel like something?"

**The dissolution**: The physical processing *does not* feel like anything. The IWM and ISM — the substrate-level implicit models — operate without any phenomenal character whatsoever. There is nothing it is like to be a synaptic weight. The simulation, however, *does* feel — and within the simulation, qualia are simply what self-perception produces. Asking why neuronal firing feels like something is analogous to asking why transistor switching feels like running a video game. The transistors do not run the game at the level of individual switching; the virtual machine does. The neurons do not experience redness at the level of individual firing; the simulation does, and within the simulation, "redness" is simply the ESM's mode of registering a particular class of EWM content.

**Why self-simulation specifically?** A critic might object that this merely relocates the Hard Problem: why does *this* virtual process have experience when a weather simulation does not? The answer lies in **self-referential closure**. A weather simulation models weather; it does not model *itself modeling weather*. The four-model architecture creates a closed loop: the ESM is the system modeling its own modeling process. In this loop, the distinction between the model and the modeled collapses — the simulation *is* the thing being simulated. Qualia are not an *addition* to the self-modeling; they are the self-modeling as encountered from the inside of the loop. A non-self-referential simulation has an outside from which it can be described without remainder; a self-referential simulation at criticality has no such outside. The simulation *is* its own observer, and observation-from-inside is what we call experience.

This is not a proof that self-referential simulation must be conscious — it is an argument that self-referential simulation is the *kind* of process for which the Hard Problem's assumptions break down. Self-referential closure is precisely the condition under which the gap between process and feeling does not exist.


<!-- [PROPOSED INSERTION — Source: Session 53, Perplexity review analysis, Date: 2026-02-16] -->
<!-- Rationale: Addresses "Why should we accept this as an answer?" critique. Frames the theory as making an identity claim (analogous to "water is H2O") rather than providing a further explanation. Makes clear that identity claims are stopping points, not gaps. Emphasizes falsifiability via empirical predictions. -->

This constitutes an identity claim: experience is what four-model self-simulation at criticality *is*. Identity claims in science are stopping points, not gaps. "Water is H₂O" cannot be further explained — the identity is the explanation. Similarly, the claim that experience is identical to self-referential simulation of this specific type at this specific dynamical regime is falsifiable (if the predictions fail, the identity is wrong) but cannot be "further explained" without requesting a different kind of universe. The identity claim's strength lies precisely in its falsifiability: it stands or falls with the empirical predictions in Section 8.

<!-- [END INSERTION] -->



This is **not** illusionism in the sense of Dennett (1991) or Frankish (2016); nor is it compatible with deflationary accounts (Graziano, 2024). Illusionism holds that qualia as traditionally conceived are illusions — there is nothing it is like, and our sense that there is something it is like is itself a misrepresentation. The Four-Model Theory holds that qualia are *real within the simulation*. Within the EWM/ESM, experience has genuine phenomenal character. What is illusory is the assumption that this phenomenal character must be a property of the physical substrate. It is not. It is a property of the virtual process that the substrate runs.

This constitutes a **two-level ontology**: the substrate level (real side) has no experience, and the simulation level (virtual side) has genuine experience. Both levels are physical — the simulation is a physical process, not a supernatural one — but they have different ontological properties. The category error in the Hard Problem consists in conflating the two levels: seeking phenomenal properties at the substrate level where they do not exist.

The Explanatory Gap closes simultaneously. The gap between "neurons fire in pattern X" and "I experience red" is not a gap in our knowledge but a reflection of the level distinction. The neural firing pattern generates and sustains the simulation in which redness is experienced, but the firing pattern itself is not red and does not experience redness, just as a CPU's electrical states are not "a spreadsheet" even though they generate and sustain one.

### 3.5 Graduated Levels of Consciousness

Consciousness in the Four-Model Theory is not binary but graduated. The theory identifies a hierarchy of levels based on the depth of recursive self-modeling:

**Basic consciousness**: Minimal self-simulation. The system generates an EWM and a rudimentary ESM — it experiences a world and has a minimal sense of being a subject within it. This is the entry level: phenomenal experience exists but self-awareness is thin.

**Simply extended consciousness**: First-order self-observation. The system models itself — the ESM includes a model of the system's own states and processes. The organism not only experiences but is aware that it experiences.

**Doubly extended consciousness**: Second-order self-observation. The system models itself modeling itself. This enables reflection, metacognition, and the sense of being an observer of one's own mental processes.

**Triply extended consciousness**: Third-order self-observation. The system models itself modeling itself modeling itself. This supports the deepest forms of self-awareness, philosophical reflection, and the very intuition that consciousness is mysterious (connecting to the Meta-Problem — see Section 3.8). Notably, triply extended consciousness is also a prerequisite for the scientific study of consciousness itself: only a system capable of modeling its own modeling of its own experience can formulate the question "What is consciousness?"

Each level corresponds to an additional layer of recursive self-modeling. The levels are not discrete stages but points along a continuum. Different organisms — and potentially different artificial systems — occupy different positions along this continuum, and individual organisms may fluctuate between levels depending on state (waking, dreaming, meditative, intoxicated).

### 3.6 The Implicit-Explicit Boundary

A key mechanism in the Four-Model Theory is the **permeability of the boundary between implicit models (IWM/ISM) and explicit models (EWM/ESM)**. Information becomes conscious when it is transferred from the implicit to the explicit side — when substrate-level knowledge or self-knowledge is incorporated into the running simulation.

In normal waking states, this boundary is **selectively permeable**: relevant information passes through based on attentional and contextual gating. You are not conscious of everything your IWM knows about the world or everything your ISM knows about yourself; you are conscious of what the current simulation requires. Crucially, the boundary is not perfectly opaque even in normal states. Substrate-level processing artifacts routinely leak through: blind-spot filling (the visual system interpolating content where the optic nerve exits the retina), phosphenes from mechanical pressure on the eye, and visual snow phenomena all represent moments where processing-level activity becomes visible within the simulation. These normal-state leaks are subtle, but they demonstrate that the implicit-explicit boundary is a *graded* filter, not a wall — and they provide everyday evidence that conscious experience is a simulation generated from substrate processing rather than a direct window onto reality.

The permeability of this boundary is variable, and its variation explains a wide range of phenomena (detailed in Section 6):

- **Psychedelic states**: Global increase in permeability — intermediate processing stages (normally implicit) become accessible to the explicit models. This explains the characteristic visual progression from simple phosphenes (V1-level) through geometric patterns (V2/V3-level) to complex imagery (higher visual areas) and eventually full dream-like scenes (Carhart-Harris et al., 2014).
- **Anosognosia**: Local decrease in permeability — the ISM contains the information (e.g., that a limb is paralyzed), but the transfer to the EWM is blocked for that specific domain.
- **Pre-sleep/deep relaxation**: Gradually increasing permeability, producing the same bottom-up visual progression as psychedelics (phosphenes → geometrics → hypnagogic imagery).
- **Meditation**: Trained modulation of permeability, enabling selective access to normally implicit processes.

Importantly, the implicit-explicit boundary is not a sharp line but a **graded transition zone**. Behavioral complexity itself follows a gradient — from reflexive chemical-gradient responses through conditioned, goal-directed, and rule-based behavior to fully conscious action — and the implicit and explicit memory systems overlap precisely in the middle of this gradient, at the levels of goal-directed and template-based behavior (Gruber, 2015). This overlap zone is the functional locus of the variable permeability described above: behavior at these intermediate levels can be driven by either implicit or explicit processing, depending on attentional state, arousal, and contextual demands.

### 3.7 The Criticality Requirement

The Four-Model Theory imposes a **physical prerequisite** for consciousness: the substrate must operate at or near the edge of chaos — Wolfram's Class 4 computational regime (Wolfram, 2002).

Wolfram classified cellular automata (and by extension computational systems generally) into four classes:
- **Class 1**: Converges to a fixed state. Too simple for consciousness.
- **Class 2**: Periodic/repetitive. Too simple for consciousness.
- **Class 3**: Chaotic/random. Too disordered for coherent consciousness.
- **Class 4**: Complex/edge of chaos. Capable of universal computation. The regime in which consciousness can emerge.

This classification was applied to the question of consciousness in Gruber (2015), where it was argued that consciousness requires Class 4 dynamics — complex enough to sustain a self-simulation, ordered enough for that simulation to be coherent. This requirement was derived *theoretically*, from the computational properties needed for real-time self-modeling, not from empirical neuroscience.

Independently, empirical neuroscience has converged on the same conclusion through a different path. Beggs and Plenz (2003) demonstrated neuronal avalanches consistent with self-organized criticality in cortical tissue. Carhart-Harris et al. (2014) proposed the Entropic Brain Hypothesis, linking consciousness level to neural entropy. Tagliazucchi et al. (2012, 2016) showed criticality signatures in waking fMRI and under LSD. Priesemann et al. (2013, 2014) characterized brain dynamics as slightly subcritical in normal waking states. This line of research was formally consolidated in the Consciousness and Criticality (ConCrit) framework (Algom & Shriki, 2025), which synthesized evidence from 140 datasets across multiple paradigms to establish that consciousness tracks criticality across pharmacological, pathological, and physiological state changes.

**Table 2. Independent Convergence on Criticality**

| Year | Development | Path |
|------|------------|------|
| 2002 | Wolfram publishes *A New Kind of Science* | Computational theory |
| 2003 | Beggs & Plenz — neuronal avalanches, self-organized criticality | Empirical neuroscience |
| 2014 | Carhart-Harris — Entropic Brain Hypothesis | Empirical neuroscience |
| **2015** | **Gruber — Class 4 / edge of chaos requirement for consciousness** | **Theoretical (via Wolfram)** |
| 2016 | Tagliazucchi et al. — LSD and criticality | Empirical neuroscience |
| 2022 | "Self-organized criticality as a framework for consciousness" (review) | Empirical neuroscience |
| 2025 | Hengen & Shew — meta-analysis of 140 datasets confirms criticality | Empirical neuroscience |
| **2025-26** | **ConCrit framework (Algom & Shriki) — criticality as unifying mechanism for consciousness theories** | **Theoretical/empirical synthesis** |

While empirical work on neural criticality was already underway (Beggs & Plenz, 2003; Tagliazucchi et al., 2012), Gruber's (2015) derivation proceeded from Wolfram's computational universality framework rather than from neuroimaging data, representing genuine theoretical convergence with the empirical program. The later large-scale consolidation (Hengen & Shew, 2025; Algom & Shriki, 2026) confirmed the criticality-consciousness link across 140 datasets. This convergence — a theoretical prediction derived independently from computational first principles, later confirmed by large-scale empirical synthesis — provides notable support for one of the theory's core claims.

### 3.7.1 The Five-System Hierarchy

The criticality requirement can be situated within a broader ontological framework that clarifies the relationship between the physical substrate and the virtual simulation. The brain instantiates five hierarchically nested systems, each emergent from the one below (Gruber, 2015):

1. **Physical system**: The atoms, molecules, and macroscopic structures of neural tissue, governed by physics and chemistry.
2. **Electrochemical system**: The ion gradients, action potentials, and synaptic transmission events that constitute neural signaling, emergent from the physical substrate.
3. **Proteomic system**: The receptor configurations, neurotransmitter synthesis pathways, and protein expression patterns that modulate neural signaling on slower timescales (minutes to days), including synaptic plasticity mechanisms.
4. **Topological system**: The connectivity architecture — the pattern of synaptic connections, their strengths, and their organization into circuits, columns, and areas. This is the level at which the implicit models (IWM, ISM) are stored. Changes at this level constitute learning.
5. **Virtual system**: The real-time dynamical pattern — the cortical automaton (Section 3.7.2) — that constitutes the explicit models (EWM, ESM). This is the level at which consciousness exists.

Each level is fully physical and fully determined by the level below it; there is no strong emergence, no ontological gap between levels. However, each level exhibits properties that are not usefully described in terms of the lower level: describing a memory in terms of ion channel kinetics is possible in principle but explanatorily vacuous. The five-system hierarchy makes precise the sense in which the Four-Model Theory's real/virtual distinction is a *level* distinction, not a *substance* distinction: the virtual system (Level 5) is as physical as the electrochemical system (Level 2), but it is the level at which experiential properties — qualia, unity, selfhood — are constituted. Seeking experiential properties at Levels 1-4 is the category error identified in Section 3.4.

### 3.7.2 The Cortical Automaton

The criticality requirement has a concrete physical interpretation in the biological brain. The instantaneous pattern of neural firing across the cortex — the spatiotemporal activation state of billions of neurons — constitutes a cellular automaton operating in a space of many thousand dimensions (Gruber, 2015). Each cortical column functions as a cell in this automaton; the six-layer architecture and lateral connectivity define the transition rules. This "cortical automaton" is not a metaphor: it is a literal description of the cortex as a discrete dynamical system whose state evolves at each timestep according to local rules applied across a high-dimensional lattice.

Crucially, the cortical automaton *is not* consciousness. Consciousness arises from the interplay between the automaton's dynamics and the models stored in the substrate — the IWM, ISM, EWM, and ESM. The automaton provides the computational medium; the models provide the content. Without the automaton's Class 4 dynamics, the models cannot generate a coherent simulation. Without the models, the automaton produces complex dynamics but no self-referential experience. The cortical automaton is to consciousness what a CPU's clock-driven state transitions are to the execution of a program: necessary infrastructure, not the program itself.

This framing yields a concrete observational claim: the cortical automaton's activity is, in principle, directly observable. In a dark, quiet environment with eyes closed, after retinal afterimages have faded, the faint flickering patterns visible against the dark field are not retinal noise but V1-level manifestations of the cortical automaton's ongoing activity — the lowest layer of the implicit-to-explicit permeability becoming momentarily accessible (Gruber, 2015). The progression from these simple phosphenes to the geometric patterns and eventually hypnagogic imagery observed during sleep onset represents progressively higher cortical areas being recruited into the observable dynamics, consistent with the hierarchical permeability account developed in Section 6.1.

### 3.7.3 Two Thresholds for Consciousness

The Four-Model Theory distinguishes two thresholds for consciousness:
- **Physical threshold**: Criticality. The substrate must operate at Class 4 dynamics. Below this, no consciousness is possible regardless of architecture.
- **Functional threshold**: Four-model architecture. The substrate must implement the four-model self-simulation. Above criticality but without the architecture, there is complex dynamics but no consciousness.

Both thresholds must be met. Criticality is necessary but not sufficient; the four-model architecture is necessary but not sufficient. Together they are sufficient.

### 3.8 The Meta-Problem Dissolved

The Meta-Problem — why we think there is a Hard Problem — receives a natural account within the Four-Model Theory. The ISM (Implicit Self Model) is **structurally inaccessible** to the ESM (Explicit Self Model). The conscious self cannot directly observe its own substrate. When the ESM attempts to model the basis of its own experience, it encounters a principled opacity: the implicit models that generate the simulation are not themselves part of the simulation.

This is why consciousness *seems* mysterious. The ESM can represent that it is having an experience, but it cannot represent the mechanism by which the experience is generated — because that mechanism operates at the implicit/substrate level, which is by definition outside the explicit/virtual level. The result is the persistent intuition that something is being "left out" of any physical explanation: the ESM cannot find the mechanism within its own simulation, so it concludes the mechanism must be non-physical or fundamentally inexplicable.

The variable permeability of the implicit-explicit boundary (Section 3.6) adds a further dimension to this account. The boundary is not perfectly opaque: substrate-level processing artifacts occasionally leak through to the simulation — in altered states dramatically so, but even in normal waking states subtly. The conscious self thus inhabits a strange epistemic position: mostly sealed off from its own generative machinery, yet occasionally catching fleeting glimpses of something operating beneath the surface of experience. This architectural feature — near-opacity punctuated by occasional leaks — produces precisely the phenomenology that the Meta-Problem describes: the persistent, nagging intuition that consciousness is somehow deeper than any explanation can reach, that something vast operates just beyond the edge of introspective access. The mystery of consciousness is not evidence against the theory; it is a *prediction* of the theory. A virtual process with a mostly-opaque but imperfect boundary to its own substrate would experience exactly this sense of irreducible depth.

This account shares features with Graziano's AST explanation — both invoke the self-model's necessary incompleteness — but grounds it in a more specific architecture (four models, real/virtual split, variable permeability) and connects it to the broader dissolution of the Hard Problem rather than treating the Meta-Problem in isolation.

---

## 4. Philosophical Commitments

The Four-Model Theory entails specific philosophical positions that were established through structured adversarial analysis and are internally consistent. This section develops and defends each commitment.

### 4.1 Process Physicalism

The theory is physicalist: both the substrate (implicit models) and the simulation (explicit models) are physical processes. There is no non-physical substance, no fundamental experiential property, no panpsychist micro-experience. Qualia are higher-order physical patterns — specifically, they are patterns of activity within the simulation that constitute the ESM's self-perception within the EWM.

This is process physicalism rather than identity theory: consciousness is not identical to any particular neural state but is constituted by the *process* of self-simulation. The same conscious state could, in principle, be realized by different physical substrates — what matters is the functional architecture (four models at criticality), not the specific material.

Process physicalism avoids the difficulties of both type-identity theory (which struggles with multiple realization) and functionalism as traditionally conceived (which struggles with the Hard Problem). The Four-Model Theory adds the real/virtual level distinction to standard functionalism, which is what allows it to address phenomenality: qualia are not just functional roles but virtual properties of the simulation. They are real *as virtual properties* — genuinely experiential but not properties of the substrate.

### 4.2 Consciousness as Process, Not Agent

A persistent source of confusion in consciousness studies is the treatment of consciousness as an entity — an "it" that either does or does not cause things. The Four-Model Theory rejects this framing. Consciousness is not a thing; it is a process *performed* by the substrate. Asking whether consciousness "causes" anything is a category error — analogous to asking whether the pointer of a clock meeting the numerals causes the clock to work. The energy source drives the gears, which drive the pointer, but nowhere does the virtual interaction between pointer and numeral cause anything mechanical. Yet without that interaction the clock cannot be said to function — or malfunction.

The implicit models generate the virtual simulation for concrete adaptive reasons: the EWM integrates multimodal sensory data into a unified scene; the ESM provides a self-model against which consequences can be evaluated. This relationship is best understood as a **dual evaluation architecture**. The primary direction is that the implicit system actively *deploys* the virtual simulation as its evaluation mechanism: it presents decisions, actions, and their consequences to the simulation so that the simulation can assess outcomes, run scenarios, and register hedonic valence. This is not idle accompaniment — it is the substrate's mechanism for consequence-observation. But the explicit models also evaluate independently, albeit with significantly less computational bandwidth. The conscious simulation operates at approximately 20 Hz with a processing delay of roughly 500 ms (Van Rullen, 2003), while the substrate processes at vastly higher throughput. The virtual evaluation is real but bandwidth-limited. Over time, these conscious evaluations — the explicit system's independent assessments of situations, actions, and outcomes — feed back to reshape the implicit models through learning. The result is two-way traffic: the implicit system uses the explicit as an evaluation tool (primary), and the explicit system contributes its own assessments back (secondary), shaping the substrate that generates it. The virtual simulation is thus the substrate's mechanism for consequence-observation and future-oriented adaptation — the very thing natural selection shaped the architecture to do.


<!-- [PROPOSED INSERTION — Source: Session 53, Perplexity review analysis, Date: 2026-02-16] -->
<!-- Rationale: Addresses "Why must the simulation feel?" critique. Argues that phenomenality is functionally necessary for evaluation, not epiphenomenal. Distinguishes theory from both classical epiphenomenalism and standard functionalism. -->

This functional essentiality extends specifically to phenomenality. The substrate deploys the simulation as its evaluation mechanism — presenting situations so the simulation can assess consequences and register outcomes. For this evaluation to work, simulated states must have valence: they must *matter* to the simulation. A pain signal that is merely a numerical value without aversive character cannot drive avoidance at the simulation level. Only a simulation whose states carry hedonic valence — whose representations of threat, opportunity, and consequence are genuinely aversive or attractive — can perform the evaluative function that justifies the metabolic cost of maintaining the simulation. Phenomenality is not an optional feature of the simulation; it is the mechanism by which the simulation evaluates. Remove phenomenality and the simulation becomes a passive model rather than an evaluation engine — a spreadsheet rather than a simulation.

This distinguishes the theory's position from both traditional epiphenomenalism and functionalism: qualia lack independent causal power over the substrate, but the phenomenal character of the simulation is constitutive of its evaluative function. The simulation cannot "run dark" — cannot perform its function without phenomenality — because valence *is* the evaluation.

<!-- [END INSERTION] -->



This makes the theory's position distinct from classical epiphenomenalism, in which consciousness is a causally inert by-product with no functional role. In the Four-Model Theory, the virtual models are in continuous feedback with the implicit models: the simulation's outputs feed back to update implicit processing, shaping future behavior. Qualia, as constitutive elements of that simulation, lack independent causal power over the substrate — much as the hands and numerals of a clock have no direct mechanical relation to the gear train, yet the clock cannot function as a clock without them. Remove the display and the mechanism still runs, but it no longer serves its purpose.[^quantum]

[^quantum]: As a corollary, consciousness plays no role in quantum measurement or wavefunction collapse. Observer-dependent interpretations of quantum mechanics (von Neumann, 1932; Wigner, 1961) are rejected. This is consistent with the dominant position in contemporary physics (decoherence approaches; Zurek, 2003) and with the theory's commitment to physicalism.

The theory also reframes the free will debate. The ESM narrates decisions already made at the substrate level (Libet, 1985; Schurger et al., 2012; Wegner, 2002), which might seem to eliminate free will — but only if "will" is restricted to what the conscious self explicitly desires. The Four-Model Theory suggests a broader view: the substrate, including the implicit models, continuously optimizes the organism's existence, and this optimization *is* the individual's will — merely not fully transparent to the ESM. One's will is real but only partially known to oneself. The conscious experience of wanting something is the ESM's window onto a deeper process that is genuinely goal-directed. Whether this constitutes free will in the libertarian sense reduces to a question of physical determinism — a question for physics, not consciousness theory. But the theory predicts that even extreme acts of will, including self-destruction, reflect the system's optimization rather than its failure — which is, paradoxically, among the stronger arguments that the will is genuine.

The process view also resolves a puzzle about **personal identity**. The ESM does not maintain continuity through persistence of substance; it maintains continuity through **confabulation**. Each time the ESM is generated — upon waking, after anesthesia, after any interruption — it reconstructs a continuous self-narrative from whatever the ISM contains. The ISM changes during sleep (memory consolidation, synaptic reweighting, homeostatic plasticity), yet the ESM that emerges in the morning seamlessly narrativizes itself as the same person who went to sleep. There is no "clean break" in identity; the ESM always stitches a continuous story from available material. This is the same mechanism observed in split-brain confabulation (Gazzaniga, 2000), in Cotard's delusion, and in post-anesthetic narrativization: wherever the ESM encounters gaps or inconsistencies, it confabulates bridging narrative. Identity is not a metaphysical given but a computational product — the ESM's narrative reconstruction of continuity from the ISM's current state.

**Temporal dynamics and the Libet reinterpretation.** The free will reframing receives further support from the temporal structure of cortical processing. Empirical evidence indicates that the cortex operates at two distinct temporal scales: an unconscious processing loop at approximately 40 Hz and a conscious integration loop at approximately 20 Hz (Gruber, 2015; cf. Llinás & Ribary, 1993; Engel & Singer, 2001). The 40 Hz loop corresponds to substrate-level computation — rapid, parallel processing within and across the implicit models. The 20 Hz loop corresponds to the conscious simulation — the frame rate of the EWM and ESM. This temporal asymmetry has a direct bearing on Libet's (1985) finding that the readiness potential precedes the conscious awareness of intention by approximately 350-500 ms. The standard interpretation — that unconscious processes "decide" before consciousness is informed — is typically taken to imply that consciousness must "backdate" its awareness of decisions. The Four-Model Theory eliminates the need for backdating: because the conscious simulation runs at half the frequency of the unconscious substrate, the ESM receives *all* information — sensory, decisional, and motor — with the same temporal delay. Within the simulation, the sequence appears coherent: intention precedes action precedes sensory feedback, all presented with a uniform lag relative to substrate events. The ESM does not backdate anything; it simply runs on a slower clock that receives all its inputs with the same latency. The subjective experience of temporal coherence is genuine *within the simulation*, even though every element of that experience occurs after the corresponding substrate event. This reinterpretation aligns with Schurger et al.'s (2012) accumulator model, which showed that the readiness potential reflects stochastic fluctuations rather than a discrete "decision" moment, and dissolves the apparent conflict between Libet's data and the subjective experience of volitional timing.

**Cognitive learning as evolutionary advantage.** The four-model architecture confers a specific adaptive advantage that no simpler system can replicate: it enables **cognitive learning** — the induction of general theories from particular observations — as distinct from reinforcement learning, which proceeds by trial-and-error reward signal optimization (Gruber, 2015). Reinforcement learning requires that the organism survive the learning trial. For many ecological challenges, this is an unacceptable constraint. The paradigmatic example is poisonous food: an organism that must ingest a lethal substance to learn its danger does not survive to apply the lesson. The four-model architecture solves this through third-person perspective simulation. By modeling another organism's experience (projecting the ESM onto an observed other), a conscious system can learn from observed deaths without personal exposure — cognitive learning via the EWM's simulation of consequences. Furthermore, once the general concept "some mushrooms are poisonous" has been induced, the system can apply deductive reasoning to novel instances: an unfamiliar mushroom sharing features with known toxic species can be avoided without any direct experience, a capacity that requires an explicit world model capable of categorical abstraction.

This distinction between cognitive and reinforcement learning is not merely a theoretical nicety; it identifies a concrete functional capability that consciousness provides and that unconscious processing — however sophisticated — cannot replicate. Current artificial neural networks, including large language models, can approximate aspects of cognitive learning through pattern extraction from training data, but they lack the real-time self-simulation that would enable genuine first-person-to-third-person perspective projection. The evolutionary argument for consciousness is therefore not that consciousness "feels good" (a non-explanation) but that it enables a qualitatively different mode of learning that confers decisive survival advantage in environments containing lethal contingencies. The implications of this cognitive-learning advantage for intelligence theory — including why intelligence should be understood as a recursive system rather than a fixed trait — are developed in a companion paper (Gruber, forthcoming).

This framing addresses the standard objections. **Zombies** (Chalmers, 1996): not possible — the virtual models *are* the substrate's activity at the virtual level, just as a vortex is not added to water's movement but is a description of it. A system implementing the four-model architecture at criticality necessarily instantiates the simulation, and the simulation necessarily has phenomenal character. **The knowledge argument** (Jackson, 1982): Mary gains acquaintance with a virtual quale she could not access from substrate descriptions — real knowledge, no independent causal power required. **The evolutionary argument**: natural selection targets the functional capabilities of the architecture (predictive modeling, social cognition, consequence-evaluation); the phenomenal character of the simulation is constitutive of those capabilities, not a separate target and not a free-rider.

### 4.3 Weak Emergence

Consciousness, in this theory, is weakly emergent: it is deducible in principle from a complete description of the substrate, even if it is practically irreducible due to the complexity of the system. There is no strong emergence, no magical threshold, no point at which "something extra" appears that could not have been predicted from the underlying physics.

This avoids the difficulties of both strong emergence (which is either mysterious or incoherent; Kim, 1993) and the panpsychist combination problem (which is unresolved; Chalmers, 2016). Consciousness does not arise from combining micro-experiences (there are none to combine) and does not require a special emergence law (there is none). It arises from the computational properties of a system running a self-simulation at criticality, just as a weather pattern arises from the thermodynamic properties of an atmosphere — no extra ingredient needed.

### 4.4 Substrate Independence

The six-layer mammalian neocortex is an evolutionary implementation of the four-model architecture, not a requirement for it. Consciousness is substrate-independent: any physical system capable of implementing the four-model architecture at criticality should produce consciousness.

The six-layer cortical architecture nonetheless provides a suggestive clue about the computational requirements for self-modeling. Universal approximation theory establishes that a three-layer neural network (input, hidden, output) suffices for arbitrary function approximation (Cybenko, 1989; Hornik et al., 1989). The mammalian neocortex consistently employs six layers — approximately three layers beyond what is required for information processing *per se*. The Four-Model Theory interprets this architectural "surplus" as the substrate's overhead for self-modeling (Gruber, 2015): the additional layers provide the computational capacity needed to run the explicit models (EWM and ESM) as real-time simulations *on top of* the implicit processing that three layers would suffice for. The cortex does not merely process information; it simulates a world and a self *within* the information-processing substrate, and this simulation requires architectural resources beyond those needed for the processing alone. This interpretation offers an architectural bridge from "neural network" (a system that processes information) to "self-simulating system" (a system that models its own processing): the six-layer cortex is not simply a deeper network for better pattern recognition but a network with sufficient recursive capacity to turn its processing back upon itself.

Biological evidence already supports this. Corvids (crows, ravens) and parrots demonstrate cognitive abilities — tool use, planning, mirror self-recognition, social cognition — that strongly suggest consciousness, yet their brains have no neocortex. Their pallium is organized in nuclear clusters rather than layers (Güntürkün & Bugnyar, 2016). Cephalopods (octopuses) demonstrate problem-solving and behavioral flexibility with an even more radically different brain architecture. If the Four-Model Theory is correct, these animals are conscious not because they share our neural architecture but because they have evolved functionally equivalent self-simulation architectures on different substrates — exactly what substrate independence predicts.

Substrate independence has a deeper grounding than biological diversity alone. The universe is demonstrably capable of Class 4 dynamics: self-organized criticality, fractal structure, and edge-of-chaos phenomena are ubiquitous in natural systems, from weather patterns and turbulence to neural tissue and galaxy formation. A universe capable of Class 4 dynamics is, by Wolfram's equivalence principle (Wolfram, 2002), capable of universal computation. A computational substrate of the universe's scale — vast in spatial extent, temporal depth, and possibly in dimensions not yet characterized — does not merely *allow* self-simulating systems to emerge; it renders them a structural inevitability. This is not the anthropic claim that consciousness is improbable but happened to occur; it is the stronger claim that a Class 4-capable universe of sufficient extent *guarantees* the emergence of self-simulating architectures as a consequence of its computational nature. The remaining cosmological question — why the universe is Class 4-capable at all — lies outside the scope of this theory, but the inference from Class 4 capability to conscious systems is, if the theory is correct, architecturally necessary rather than contingent.

The implication for artificial consciousness is direct: a synthetic system implementing the four-model architecture at criticality should produce genuine consciousness. Current AI systems, including large language models, do not meet this specification. LLMs lack an Explicit Self Model (they do not run a real-time self-simulation), lack criticality (transformer inference is a feedforward pass — Class 1/2 dynamics), and lack the real/virtual split that grounds phenomenality. The theory predicts that the qualitative difference between interacting with a genuinely conscious artificial system and interacting with an LLM would be immediately and qualitatively distinguishable.

---

## 5. Binding, Criticality, and Holographic Storage

### 5.1 Binding as an Emergent Property of Critical Dynamics

The Four-Model Theory does not treat binding as a separate mechanism requiring a dedicated solution. Instead, binding is an emergent property of a substrate operating at criticality.

At the edge of chaos, the system exhibits maximal correlation length: distant parts of the substrate influence each other, local perturbations propagate globally, and information is integrated across the entire network. These are precisely the conditions under which distributed representations — features encoded across the full network rather than localized in specific neurons — are sustained and coordinated. Binding is not something the brain does *in addition to* its other computations; it is a consequence of the dynamical regime in which the brain operates.

This is consistent with empirical findings. Gamma-band synchrony (Gray et al., 1989; Rodriguez et al., 1999; Fries, 2005, 2015), long-range thalamocortical coherence (Llinás & Ribary, 1993; Llinás et al., 1998), and criticality signatures in neural dynamics (Beggs & Plenz, 2003; Tagliazucchi et al., 2012) all point toward the same conclusion: the unified character of conscious experience reflects the dynamical integration of a system operating at or near criticality, not a dedicated binding mechanism.

A further role for criticality emerges from the recursive structure of the four-model architecture. The theory requires that models of different orders of complexity — from a basic world model (EWM) to a self-model observing a self-model (ESM monitoring ESM) — coexist and interact in real time. This demands cross-scale synchronization: simple and complex representations must remain coherent with one another. Criticality's scale-free dynamics provide exactly this, supporting information flow across all levels of the representational hierarchy simultaneously. However, this synchronization is not permanent. The biological substrate drifts from criticality as metabolic resources — particularly neurotransmitter pools — are depleted through sustained activity. The result is *punctuated stability*: extended phases of coherent conscious operation (waking), interrupted by periodic breakdowns in which the simulation collapses (deep sleep) and the substrate restores the biochemical conditions for criticality. The ultradian NREM-REM cycle (Section 6.3) may reflect periodic re-approaches to the critical point during this restoration process. Sleep, on this account, is not merely rest but the substrate's mechanism for *returning to* the dynamical regime that consciousness requires.

### 5.2 Holographic Storage and the Patchwork Principle

The implicit models (IWM and ISM) store information in a distributed, non-local manner across the substrate. This is a standard property of neural networks, well-characterized in the computational literature as distributed representations (Hinton, McClelland, & Rumelhart, 1986), graceful degradation (loss of connections degrades but does not destroy stored information), and attractor dynamics (the network settles into basins of attraction that represent stored knowledge).

The term "holographic" is used here as an analogy, not a claim about optical holography: just as cutting a hologram in half produces two complete but lower-resolution images, splitting a neural network produces two degraded but functionally complete copies of the stored information. This property is critical for understanding split-brain phenomena (Section 6.4).

However, the cortex is not a uniform holographic medium. It is better described as a **patchwork hologram** (Gruber, 2015): locally holographic within individual Brodmann areas, fractally self-similar across cortical columns, and globally emergent at the whole-brain scale. Within a single Brodmann area, information is distributed across the local network in the manner characteristic of neural holography — damage degrades but does not destroy the stored representations. Across areas, the cortical column architecture provides a fractal repetition of the same six-layer computational motif, adapted by local connectivity patterns to different functional specializations. At the global level, the interaction of these locally holographic patches produces emergent properties — binding, unified experience, coherent world-modeling — that are not present in any individual patch.

This patchwork structure resolves a tension in the holographic brain literature. Lashley's engram experiments (Lashley, 1950) demonstrated that memory is not localized: progressive cortical ablation in rats produced graded memory impairment proportional to the amount of tissue removed, not catastrophic loss when specific regions were destroyed. This finding is consistent with holographic storage. Yet the existence of functionally specialized cortical areas (Brodmann, 1909) — with distinct processing characteristics and distinct lesion syndromes — appears to contradict a purely holographic account. The patchwork principle reconciles these observations: information is holographically distributed *within* functional areas (explaining Lashley's graded degradation) while remaining functionally organized *across* areas (explaining specialization). The Pribram-Bohm holonomic brain theory (Pribram, 1991) captured the core insight about distributed storage but proposed implausible dendritic oscillation networks as the mechanism; the patchwork principle retains the distributional insight while grounding it in the well-established properties of neural networks operating within the cortical column architecture.

### 5.3 Consciousness States Derived from Criticality

The criticality requirement provides a unified account of when consciousness is present and when it is absent. Consciousness tracks the substrate's position relative to the critical point:

**Table 3. Consciousness States and Criticality**

| State | Criticality | Models | Consciousness | Evidence |
|-------|---|---|---|---|
| Normal waking | At/near critical | All four active | Full | High PCI, rich EEG |
| REM sleep | Near-critical, no input | EWM/ESM on internal input | Degraded (dream) | Moderate PCI |
| Deep NREM | Subcritical | EWM/ESM collapse | Absent | Low PCI, slow waves |
| Propofol | Forced subcritical | EWM/ESM suppressed | Absent | PCI ≈ 0 |
| Ketamine | Not subcritical (↑ entropy) | EWM/ESM on wrong input | Present, disconnected | ↑ EEG entropy |
| Psychedelics | At/past critical | All active, ↑ permeability | Present, altered | ↑ Complexity |
| Vegetative | Typically subcritical | EWM/ESM collapsed | Absent (usually) | Low PCI |
| Covert awareness | At critical, output damaged | EWM/ESM intact, no motor | Present, unexpressible | Owen (2006) |
| Minimally conscious | Fluctuating | Intermittent EWM/ESM | Intermittent | Fluctuating PCI |

The key distinction highlighted by this framework is between **propofol** and **ketamine**. Both are anesthetics, yet their phenomenology differs dramatically. Propofol produces absence: patients report no experience during propofol anesthesia (Alkire et al., 2000; Boly et al., 2012). Ketamine produces the "K-hole" — vivid, often bizarre experiences of dissociation, out-of-body phenomena, and altered identity (Corlett et al., 2011). The Four-Model Theory predicts this difference: propofol pushes the substrate subcritical (disrupting thalamocortical connectivity, suppressing complexity), abolishing the conditions for consciousness. Ketamine does *not* push the substrate subcritical — it increases neural entropy (Schartner et al., 2017) — but disrupts normal sensory input processing, causing the EWM and ESM to operate on internal and distorted signals. Consciousness is present but disconnected from external reality.

This is a genuine explanatory advantage. Most theories struggle to account for why two agents classified as "anesthetics" produce such radically different phenomenological profiles. The criticality framework makes the distinction natural: what matters is not the pharmacological classification but the effect on the substrate's dynamical regime.

---

## 6. Explanatory Range

A theory's value lies partly in its ability to derive diverse phenomena from a small set of principles. The Four-Model Theory's five principles — criticality, virtual qualia, redirectable ESM, variable implicit-explicit permeability, and virtual model forking — generate accounts of phenomena across psychopharmacology, clinical neurology, sleep science, comparative cognition, and clinical psychology. This section demonstrates that range.

### 6.1 Psychedelic Phenomenology

Psychedelic substances (LSD, psilocybin, DMT, mescaline) produce a characteristic phenomenological profile: visual intensification and distortion, synesthesia, altered time perception, enhanced pattern recognition, emotional intensification, ego dissolution at high doses, and — with certain compounds and doses — radical identity alteration including the experience of "becoming" non-self entities (Carhart-Harris et al., 2012, 2016; Timmermann et al., 2019, 2023).

The Four-Model Theory accounts for this profile through three mechanisms:

**Implicit-explicit permeability increase**. Psychedelics increase the global permeability of the boundary between implicit and explicit models. Intermediate processing stages — normally implicit and inaccessible — leak through to the simulation. This produces the characteristic visual progression:

- **Low dose / early onset**: V1-level processing becomes accessible → simple phosphenes, enhanced contrast, breathing/movement in static patterns.
- **Increasing dose**: V2/V3-level processing becomes accessible → geometric patterns, fractals, tessellations (form constants; Klüver, 1966).
- **Higher dose**: Higher visual area processing becomes accessible → faces, figures, scenes.
- **Very high dose**: Full intermediate processing accessible → complex dream-like visions, narrative sequences.

This progression is not random. It follows the visual processing hierarchy in a predictable, dose-dependent order. The Four-Model Theory predicts this ordered progression as a direct consequence of the permeability gradient: lower-level (earlier, simpler) processing stages become accessible before higher-level (later, more complex) ones, because the permeability increase propagates up the hierarchy.

**Ego dissolution = ESM redirection, not ESM abolition**. At high doses, psychedelics disrupt the normal self-referential input to the ESM. The ESM does not cease to exist — it continues to run — but it loses its normal input and latches onto whatever dominates the available input stream. This produces the experience of ego dissolution: the feeling that the boundary between self and world has dissolved, that one's identity has merged with the environment or with abstract patterns.

Critically, this mechanism predicts that the *content* of ego dissolution is not random but is determined by the dominant input available to the ESM. This is dramatically confirmed by the phenomenology of **salvia divinorum** (Salvinorin A). Salvia users reliably report experiences of "becoming" objects or entities in their immediate environment: becoming a piece of furniture, becoming a wall, becoming a character from a television show playing in the room, becoming a geometric pattern. The Four-Model Theory predicts exactly this: the ESM, deprived of normal self-input, latches onto whatever sensory input dominates — visual input from the room, auditory input from media, proprioceptive input from the body's contact surfaces. The identity experience tracks the dominant input in a dose-dependent, input-dependent, and therefore *predictable* manner.

Few competing theories generate this specific prediction. IIT, GNW, HOT, and AST have no mechanism for identity content tracking during ego dissolution, though predictive processing frameworks might produce a related account through the breakdown of self-related priors. This is arguably the theory's most distinctive prediction (see Section 8, Prediction 3).

**Intensity as novelty**. Psychedelic profundity reflects not increased consciousness *level* but increased *novel content*. The permeability increase floods the simulation with normally implicit information. This is experienced as radically novel because the conscious self has never encountered this content, even though the substrate has been processing it all along.

### 6.2 Anesthesia and Clinical Disorders

**Propofol anesthesia**: Pushes the substrate subcritical → the conditions for consciousness are abolished → the simulation collapses → no experience. (See Table 3.)

**Ketamine**: Does not push subcritical; increases entropy → consciousness persists but on distorted/internal input → dissociative experience, K-hole phenomenology.

**Vegetative state**: Substrate is typically subcritical → no consciousness. But the Four-Model Theory makes a nuanced prediction: if the substrate is at criticality but *output pathways* are damaged (motor cortex, brainstem circuits), consciousness is present but unexpressible. This is precisely the phenomenon of **cognitive motor dissociation** (CMD), documented by Owen et al. (2006) and Monti et al. (2010), in which patients clinically diagnosed as vegetative demonstrate awareness through brain-imaging paradigms. The theory predicts that the distinction between truly vegetative (subcritical substrate) and covertly conscious (critical substrate with damaged output) should be detectable via criticality measures such as PCI (Casali et al., 2013; Casarotto et al., 2016).

**Minimally conscious state**: The substrate fluctuates around the criticality threshold → intermittent consciousness, explaining the characteristic behavioral variability.

**Cotard's delusion**: Patients report believing they are dead, that their organs have disappeared, or that they do not exist. The Four-Model Theory derives this from the same mechanism as salvia: the ESM receives severely distorted interoceptive input (due to neurological damage or psychiatric disorder). Deprived of normal self-referential signals, the ESM constructs the best model it can from the available (distorted) input — and "I am dead" is the ESM's interpretation of the absence of normal embodied signals. This is the same redirectable-ESM mechanism that produces "I am a chair" under salvia, applied to a clinical context.

**Anosognosia**: Patients with anosognosia (typically following right-hemisphere stroke) are unaware of their own deficits — they deny being paralyzed, blind, or impaired, even in the face of clear evidence. The Four-Model Theory explains this as a **local decrease in implicit-explicit permeability**: the ISM contains the information about the deficit (the substrate registers the paralysis), but the transfer to the EWM is blocked for that specific domain. The patient's simulation simply does not include the deficit, so the patient genuinely does not experience it.

This is the **inverse** of the psychedelic mechanism: psychedelics globally increase permeability (making the implicit accessible), while anosognosia locally decreases permeability (making a specific aspect of the implicit inaccessible). The Four-Model Theory connects these phenomena under a single principle — variable permeability — and generates a cross-domain prediction: psychedelics should alleviate anosognosia by compensating for the local block with a global permeability increase (see Section 8, Prediction 4).

**Dissociative Identity Disorder (DID)**: The virtual models, being software-like, can be **forked**. DID represents a substrate running multiple ESM configurations — multiple self-models — that alternate in controlling the simulation. Each alter is a distinct configuration of the ESM, with its own self-narrative, emotional profile, and behavioral patterns, running on the same substrate. This is not a metaphor: the theory predicts that distinct alters should correspond to distinct patterns of neural activity, detectable with neuroimaging (see Section 8, Prediction 9).

### 6.3 Dreams

Dreaming represents the simulation running in **degraded mode**: near-critical dynamics (sufficient for consciousness) but with external input cut off (sensory deprivation during sleep).

The EWM continues to generate a world — but without the constraint of sensory input, the simulation draws on the IWM's stored knowledge, producing the characteristic features of dreams: familiar places and people, impossible physics, narrative incoherence, and emotional intensity. The ESM continues to generate a self — you experience dreams as happening to "you" — but with reduced metacognitive oversight, producing the characteristic lack of insight in dreams (you accept impossible events without question).

**Lucid dreaming** provides direct evidence for the software-like quality of the virtual models. In a lucid dream, the dreamer becomes aware that they are dreaming: the ESM "toggles on" more fully, gaining metacognitive access within the dream state. The Four-Model Theory predicts that lucid dream onset corresponds to a **criticality threshold crossing** — a step-like increase in neural complexity as the ESM activates more fully. This should be detectable as a discontinuity in EEG complexity measures at the moment of lucid dream onset (see Section 8, Prediction 8).

The criticality framework also explains the **NREM/REM transition**: as the brain's dynamical state fluctuates during sleep, crossing the criticality threshold produces the transition from non-conscious deep sleep to conscious dreaming. The 90-minute ultradian cycle corresponds to an oscillation of the substrate around the critical point.

### 6.4 Split-Brain

Callosotomy produces the classic split-brain syndrome (Gazzaniga, Bogen, & Sperry, 1962, 1965; Gazzaniga, 2000). The Four-Model Theory offers a more precise account than the traditional "two minds in one brain."

Because the implicit models store information holographically (Section 5.2), physical separation does not cleanly divide the models into left and right halves. Instead, it produces **two degraded but functionally complete copies**. Each hemisphere retains a degraded version of the IWM, ISM, EWM, and ESM — complete enough to sustain consciousness but lacking the resolution and scope of the intact system.

This accounts for the key features of split-brain behavior:
- **Each hemisphere sustains independent consciousness**: Both are above the criticality threshold and both have complete (if degraded) four-model architectures.
- **The left hemisphere interpreter** (Gazzaniga, 2000): The left hemisphere's ESM confabulates explanations for behavior initiated by the right hemisphere. This is the *same confabulation mechanism* observed in Cotard's delusion, anosognosia, and salvia experiences: an ESM constructing the best narrative it can from incomplete input. The left hemisphere's ESM does not have access to the right hemisphere's motivations (the callosum is cut), so it invents post-hoc explanations — just as the Cotard's patient's ESM invents "I am dead" from distorted interoceptive input.
- **Degradation rather than clean division**: Split-brain patients do not show perfectly hemispheric specialization; they show graded deficits (Pinto et al., 2017), consistent with holographic degradation rather than binary splitting.

### 6.5 Animal Consciousness

The theory's commitments — continuum (not binary), substrate independence, criticality threshold — predict a **gradient** of animal consciousness. Mammals implement the four-model architecture in graduated form, with even simple cortices (rodents) supporting basic consciousness — rudimentary simulation sufficient for phenomenal experience but thin in self-awareness.

**Corvids and parrots** present a crucial test case: tool manufacture, mirror self-recognition, social deception, and future planning — yet no neocortex, with pallium organized in nuclear clusters (Güntürkün & Bugnyar, 2016). The theory predicts these animals are conscious because they have evolved functionally equivalent self-simulation architectures on a different substrate. **Cephalopods** extend this logic further, with largely decentralized nervous systems that should produce consciousness with unusual features. Both cases test substrate independence directly.

### 6.6 Clinical Psychology Bridge

The virtual-model framework extends to clinical phenomena. **CBT** works as virtual model reprogramming: repeated corrective experience drives substrate-level rewiring (synaptic plasticity), modifying the ISM, which changes the ESM's self-model. **Phobias** are EWM misconfigurations where threat representation exceeds the IWM's evidence base; exposure therapy updates the IWM to correct the EWM.

**The placebo effect** illustrates the theory's causal architecture: placebo activates substrate-level expectation circuits (endogenous opioid release) that operate in parallel with — not caused by — the conscious experience of hope. The correlation between conscious expectation and physical effect is real but non-causal: both are products of the same substrate processes.

**Conversion disorder** is the inverse of blindsight: in blindsight, the substrate processes visual information without including it in the EWM; in conversion disorder, the EWM models a deficit (paralysis, blindness) that the intact substrate does not have.

**Blindsight** provides the clearest demonstration that substrate-level processing can proceed without conscious representation. Patients with V1 damage report no visual experience yet demonstrate above-chance performance on forced-choice tasks, navigate obstacles, and respond to emotional facial expressions (Weiskrantz, 1986). In the Four-Model Theory, blindsight occurs when the IWM continues to receive and process visual information through subcortical pathways (superior colliculus, pulvinar), guiding motor behavior via the ISM, while the damaged cortical pathways fail to relay this information to the EWM. The conscious simulation contains no visual content — the patient genuinely experiences blindness — yet the substrate navigates competently. This is substrate processing without simulation.

**Anton's syndrome** (anosognosia for cortical blindness) presents the precise inverse. Patients with complete cortical blindness deny their deficit, confabulating visual descriptions of their surroundings and walking into obstacles while insisting they can see (Anton, 1899; Aldrich et al., 1987). The Four-Model Theory explains this as the EWM generating a visual simulation from the IWM's stored knowledge in the absence of current visual input. The simulation runs on prior expectations and internally generated content rather than afferent signals. The patient "sees" a world that is not there — a simulation running without current input. Together, blindsight and Anton's syndrome constitute a double dissociation between substrate processing and conscious simulation, providing perhaps the most direct neurological evidence for the real/virtual distinction central to the theory.

---


<!-- [PROPOSED INSERTION — Source: Session 53, Perplexity review analysis, Date: 2026-02-16] -->
<!-- Rationale: Bridges theory to developmental psychology literature; generates testable predictions about mirror self-recognition, theory of mind, social deprivation, and CBT as adult developmental recalibration. Addresses gap in empirical grounding for the four-model architecture's developmental trajectory. -->

### 6.7 Developmental Psychology Bridge

The four-model architecture predicts a specific developmental trajectory for consciousness. The implicit models (IWM, ISM) are learned; the explicit models (EWM, ESM) are generated from them. Since the implicit models of a newborn are nearly empty, the newborn's simulation should be thin — basic consciousness at most — with richness increasing as the implicit models accumulate content through experience and, critically, through social interaction.

This generates several testable developmental predictions:

1. **Mirror self-recognition (~18 months)** marks the point where the ESM becomes rich enough to model the physical self as an object. This corresponds to the transition from basic to simply extended consciousness.

2. **Theory of mind (~3-4 years)** marks the emergence of the ESM modeling other ESMs — the capacity to understand that another person's beliefs may differ from one's own. This corresponds to the emergence of doubly extended consciousness.

3. **Phenomenal character is developmental**: The qualitative character of experience (what pain, pleasure, or fear *feel like*) is shaped by the training history of the implicit models, particularly through caregiver feedback and social interaction. A baby's experience of pain is structurally different from an adult's because the ISM that generates the ESM is different. The four-model architecture provides the *capacity* for experience; the social environment provides the *content*.

4. **Social deprivation predicts phenomenal impoverishment**: Children raised without social contact (feral child cases) have the neural architecture for consciousness but profoundly impoverished implicit models. The theory predicts that their ESM should be stunted — not because the hardware is broken, but because the training data for the implicit models was never provided.

5. **CBT as adult developmental recalibration**: Cognitive behavioral therapy works by the same mechanism as infant social learning — conscious experience (guided by the therapist) reshaping implicit structure through repetition. The adult ISM is more consolidated than the infant's, requiring more repetition, but the mechanism is identical.

This developmental perspective connects the four-model architecture to a rich empirical literature in developmental psychology (Piaget's stages, Tomasello's shared intentionality, Meltzoff's imitation studies) while generating predictions that distinguish the theory from competitors that lack a developmental account of phenomenal consciousness.

<!-- [END INSERTION] -->

## 7. Comparative Analysis

This section provides a systematic comparison between the Four-Model Theory and six major competitors across the eight requirements established in Section 2. The comparison aims to be fair: each theory's genuine strengths are acknowledged, and the Four-Model Theory's advantages are located precisely.

### 7.1 Scoring Matrix

Table 4 presents an assessment of how each theory addresses the eight requirements. All ratings reflect the present author's judgment and are offered as a starting point for discussion, not as definitive verdicts. Readers are encouraged to consult the primary sources and form their own assessments. Where a theory's proponents would likely contest a rating, this is noted.

**Assessment criteria**: *Addresses* = the theory provides a substantive, defended account of this requirement. *Partial* = the theory provides a relevant account that leaves significant aspects unresolved. *Minimal* = the theory touches on this requirement but does not develop a full treatment. *Silent* = the theory does not address this requirement (which may reflect deliberate scope limitation rather than failure). *N/A* = the requirement does not apply given the theory's ontological commitments.

**Table 4. Theory Comparison Across Eight Requirements**

Ratings: ● = addresses, ◐ = partial, ○ = minimal, — = silent, n/a = not applicable.

| Requirement | FMT | IIT | GNW | HOT | PP | AST | RPT |
|---|---|---|---|---|---|---|---|
| Hard Problem | ● | ●† | —* | ◐ | —* | ◐ | — |
| Expl. Gap | ● | ●† | —* | ◐ | —* | ◐ | — |
| Boundary | ● | ● | ◐ | ○ | ◐ | ◐ | ◐ |
| Structure | ● | ● | ◐ | ◐ | ● | ◐ | ◐ |
| Binding | ● | ● | ◐ | ○ | ◐ | ○ | ◐ |
| Combination | ● | ○†† | n/a | n/a | n/a | n/a | n/a |
| Causal Role | ● | ◐ | ◐ | ◐ | ● | ◐ | ● |
| Meta-Problem | ● | ○ | ◐ | ◐ | ◐ | ● | ○ |

† IIT addresses the Hard Problem through its axioms, identifying consciousness with integrated information (Φ). Whether this constitutes a solution or a redefinition is debated (see §7.2).
†† IIT's panpsychist commitments lead to the Combination Problem (Chalmers, 2016), which remains unresolved within the framework.
\* GNW and PP proponents argue these theories address the "real problem" of consciousness (Seth, 2021) — explaining the structure and contents of experience — even if they do not address the Hard Problem as Chalmers defines it. This is a legitimate methodological choice, not a deficiency; the "silent" rating reflects the scope of the requirement as defined in §2, not a judgment on the theories' overall merit.

### 7.2 Theory-by-Theory Comparison

**Integrated Information Theory** (IIT; Tononi, 2004; Albantakis et al., 2023). IIT's strengths are mathematical rigor, its qualia space treatment of experiential structure, and a principled boundary via the exclusion postulate. However, its axiom-based identification of consciousness with Φ leads to panpsychist consequences, the Combination Problem remains unresolved (Chalmers, 2016), Φ is computationally intractable for realistic systems (Aaronson, 2014), and the unfolding argument (Doerig et al., 2019) challenges its central claim about recurrence. The Four-Model Theory avoids panpsychism, has no combination problem (weak emergence), and generates predictions without computing Φ.

**Global Neuronal Workspace** (GNW; Baars, 1988; Dehaene & Changeux, 2011). GNW's empirically tractable broadcasting mechanism provides a clear account of access consciousness. However, it is silent on the Hard Problem — explaining *when* but not *why* broadcast produces experience. The COGITATE results (2025) were problematic: posterior cortex, not the frontoparietal workspace, showed the strongest consciousness-related activity. The Four-Model Theory agrees that broadcasting/integration is mechanistically important but adds the real/virtual distinction that addresses phenomenality.

**Higher-Order Theories** (HOT; Rosenthal, 2005; Lau & Rosenthal, 2011). HOT naturally explains which states are conscious (those with higher-order representations) and partially addresses the Meta-Problem. However, it does not address binding, leaves the Hard Problem only partially treated (why does higher-order representation produce phenomenality?), and its boundary-setting is imprecise. The Four-Model Theory shares HOT's emphasis on self-representation but embeds it in the richer four-model architecture, explaining *why* self-representation produces phenomenality through the virtual qualia framework.

**Predictive Processing** (PP; Friston, 2010; Seth, 2021). PP's integration with a broader theory of brain function and its strong accounts of experiential structure and causal role (via active inference) are genuine strengths. Seth's controlled hallucination framework is among the most empirically productive in the field. However, PP is explicitly silent on the Hard Problem (Seth, 2021, acknowledges this). Markov blankets may also be too liberal for boundary-setting. The Four-Model Theory agrees that prediction is central but adds the four-model architecture, criticality requirement, and real/virtual distinction that PP lacks.

**Attention Schema Theory** (AST; Graziano, 2013). AST provides the strongest existing account of the Meta-Problem: the self-model of attention is necessarily incomplete, producing the intuition of mystery. However, AST is deflationary about phenomenality and does not address binding. The Four-Model Theory incorporates AST's Meta-Problem insight — the ESM's structural inaccessibility to its own substrate — but adds the virtual qualia framework that explains *why* phenomenality exists, not just why we think it does.

**Recurrent Processing Theory** (RPT; Lamme, 2006, 2010). RPT's empirical specificity and clear account of the causal role are strengths, with strong support from visual masking paradigms. However, it is silent on the Hard Problem and limited in scope to visual consciousness. The Four-Model Theory is compatible with RPT at the mechanistic level — recurrent processing likely implements the real-time simulation — but adds the architectural and philosophical specificity that RPT lacks.

### 7.3 Emerging Frameworks (2024-2026)

**Biological computationalism** (Milinkovic & Aru, 2025) argues that consciousness requires specifically biological computation, challenging substrate independence. The Four-Model Theory treats substrate independence as an empirical prediction: artificial substrates implementing the four-model architecture at criticality should produce consciousness. The existence of conscious corvids with non-cortical brain architecture (nuclear pallium; Güntürkün & Bugnyar, 2016) favors substrate independence.

The **Multiple Generator Hypothesis** (Kirkeby-Hinrup, Fink, & Overgaard, 2025) proposes consciousness arises from multiple independent mechanisms. This is potentially compatible: the four models could be understood as distinct generators unified by the criticality requirement and implicit-explicit boundary mechanism.

### 7.4 Summary of Comparative Advantages

1. **Addressing the Hard Problem without panpsychism or strong emergence**: Virtual qualia dissolve the Hard Problem through a two-level ontology that remains fully physicalist.
2. **Unifying binding with criticality**: Binding is a consequence of critical dynamics, not a separate mechanism.
3. **The redirectable ESM**: Unique mechanism for identity-content determination during ego dissolution (Predictions 3 and 4).
4. **Connecting psychedelics and anosognosia**: Variable permeability links these phenomena under a single principle.
5. **The Meta-Problem as structural consequence**: The ESM's opacity to its own substrate explains the intuition of mystery.

The theory's primary disadvantage is the absence of mathematical formalization. IIT's Φ formalism and PP's free energy mathematics provide quantitative precision that the Four-Model Theory currently lacks (see Section 9).

---

## 8. Novel Testable Predictions

A theory is only as valuable as the predictions it generates. The Four-Model Theory yields nine novel testable predictions, several of which are highly distinctive.

### 8.1 Prediction 1: Distinct fMRI Signatures for Each Model

**Statement**: If the four models are functionally distinct processes, tasks that selectively engage a single model should produce distinct, reproducible neural activation patterns detectable via fMRI. Specifically: IWM-dominant tasks (e.g., passive recognition of familiar stimuli, implicit priming) should activate different networks than ISM-dominant tasks (e.g., habitual motor sequences, implicit body-schema tasks), which should differ from EWM-dominant tasks (e.g., active perceptual discrimination, novel scene processing) and ESM-dominant tasks (e.g., self-reflection, agency judgments, mirror self-recognition).

**Mechanism**: The four models are functionally distinct processes (not spatially localized brain regions), but distinct processes should nonetheless recruit distinguishable distributed networks. The implicit models (IWM, ISM) should preferentially engage substrate-level storage networks (hippocampal-cortical for IWM, somatosensory-cerebellar for ISM), while the explicit models (EWM, ESM) should preferentially engage simulation networks (sensory cortices for EWM, default mode network and medial prefrontal cortex for ESM).

**Testability**: High. Design a factorial task battery crossing scope (world vs. self) with mode (implicit vs. explicit), yielding four conditions. Contrast activation maps across conditions using standard fMRI subtraction or multivariate pattern analysis. The prediction is a double dissociation: scope × mode interaction effects in distributed networks.

**Unique?**: Yes in the specific form. While individual contrasts (e.g., self vs. world processing) are well-studied, the Four-Model Theory predicts a specific 2×2 factorial structure in neural activation that no other theory mandates. This prediction is placed first because it most directly tests the four-model architecture itself — the central structural claim of the theory.

### 8.2 Prediction 2: Psychedelic Content Maps the Processing Hierarchy

**Statement**: Under psychedelics, visual content progresses through the cortical processing hierarchy in an ordered, dose-dependent sequence: V1-level content (phosphenes, enhanced contrast) → V2/V3-level content (geometric patterns, form constants) → higher visual area content (faces, figures) → complex scenes (dream-like narratives).

**Mechanism**: Increasing implicit-explicit permeability exposes intermediate processing stages in hierarchical order.

**Testability**: High. Combine graded dosing protocols with concurrent fMRI or MEG to track the spatial progression of activation, correlated with subjective report of content type. Partial evidence already exists (Carhart-Harris et al., 2016; Timmermann et al., 2023) but has not been systematically tested as an ordered, dose-correlated progression.

**Unique?**: Partially. PP also predicts hierarchical processing under psychedelics but does not predict the specific ordered content progression as a function of dose.

### 8.3 Prediction 3: Ego Dissolution Content Is Controllable

**Statement**: During psychedelic ego dissolution, the content of the altered identity experience (what the subject "becomes") tracks the dominant sensory input. By controlling the sensory environment during ego dissolution, the identity content can be predicted and directed.

**Mechanism**: The ESM, deprived of normal self-referential input, latches onto whatever input dominates the available stream. Control the input → control the identity content.

**Testability**: High. Administer ego-dissolution-inducing doses of psilocybin or salvia divinorum under controlled conditions. Vary the dominant sensory input (specific visual scenes, specific auditory environments, specific tactile inputs) across conditions. Measure correspondence between controlled input and reported identity content.

**Unique?**: **Yes — few competing theories generate this specific prediction.** IIT, GNW, HOT, and AST have no mechanism for specifying what a subject will "become" during ego dissolution. Predictive processing frameworks might produce a related account through the breakdown of self-related priors, but do not predict the specific input-tracking pattern. This is the theory's most distinctive empirical prediction.

### 8.4 Prediction 4: Psychedelics Alleviate Anosognosia

**Statement**: Administration of psychedelic substances at sub-ego-dissolution doses should alleviate anosognosia by globally increasing implicit-explicit permeability, compensating for the local permeability block that causes the deficit unawareness.

**Mechanism**: Anosognosia = local permeability block. Psychedelics = global permeability increase. The global increase should overwhelm the local block, allowing the deficit information in the ISM to reach the EWM.

**Testability**: Medium (requires clinical trial with stroke patients). Could begin with case studies or observational reports of psychedelic use by patients with anosognosia. Psilocybin-assisted therapy is already being tested for various neuropsychiatric conditions, providing a potential clinical pathway.

**Unique?**: **Yes — this is a cross-domain surprise prediction.** No other theory connects psychedelics and anosognosia through a single mechanism. Confirmation would be strong evidence for the variable-permeability principle.

### 8.5 Prediction 5: All Anesthetics Converge on Criticality Disruption

**Statement**: Despite diverse receptor-level mechanisms (GABAergic, NMDA, opioid, α2-adrenergic), all agents that abolish consciousness do so by pushing the substrate below the criticality threshold. Agents that alter but do not abolish consciousness (ketamine, low-dose psychedelics) do not push below criticality.

**Mechanism**: The criticality requirement is the physical threshold for consciousness; any mechanism that disrupts criticality disrupts consciousness, regardless of receptor pathway.

**Testability**: High. Measure criticality indicators (PCI, Lempel-Ziv complexity, power-law exponents, detrended fluctuation analysis) across the full range of anesthetic agents at equi-potent doses. The prediction is that abolition of consciousness always correlates with subcriticality, and preserved consciousness (even if altered) always correlates with maintained criticality.

**Unique?**: Shared with the ConCrit framework (Algom & Shriki, 2026) and the criticality meta-analysis (Hengen & Shew, 2025). However, the Four-Model Theory predicted this from theoretical first principles (Gruber, 2015), prior to the empirical consolidation.

### 8.6 Prediction 6: Split-Brain Produces Holographic Degradation

**Statement**: After callosotomy, each hemisphere retains a degraded but functionally *complete* set of cognitive and experiential capacities — not a clean hemispheric specialization. The degradation should be proportional to the extent of commissural severing (partial callosotomy → partial degradation).

**Mechanism**: Holographic storage. Information is distributed across the full substrate; cutting connections degrades both copies but does not destroy either.

**Testability**: High. Systematic cognitive assessment of split-brain patients across domains, testing for the predicted pattern of bilateral but degraded capabilities rather than clean lateralization. Pinto et al. (2017) provide preliminary evidence in this direction.

**Unique?**: Yes, in the specific form. Standard neuroscience acknowledges some bilateral capacity, but the Four-Model Theory provides the theoretical basis (holographic storage) and predicts the specific pattern (graded degradation proportional to disconnection, not binary split).

### 8.7 Prediction 7: Criticality + Four Models = Consciousness in Artificial Substrates

**Statement**: A synthetic system implementing the four-model architecture at criticality will exhibit consciousness. The qualitative difference between interacting with such a system and interacting with a current LLM will be immediately and qualitatively distinguishable.

**Mechanism**: Substrate independence. Consciousness depends on function (four models at criticality), not on material (biological neurons).

**Testability**: Medium (requires significant engineering development). However, intermediate tests are possible: systems with partial implementations (e.g., two models instead of four, or four models without criticality) should show partial consciousness indicators, detectable through behavioral signatures and neural/computational complexity measures.

**Unique?**: Yes in the specific form. Other theories (PP, GNW) are compatible with artificial consciousness but do not provide a specific architectural blueprint.

### 8.8 Prediction 8: Sleep Architecture Reflects Criticality Maintenance

**Statement**: Sleep is the substrate's mechanism for restoring the conditions that support consciousness. The brain's analog substrate is inherently unstable — never truly calibratable for sustained digital computation. Consciousness emerges as a self-organizing cellular automaton (CA) at criticality, providing a stable digital layer on top of this drifting substrate. The CA is stable for extended periods (waking), but the underlying biochemical substrate slowly drifts (neurotransmitter depletion, metabolic waste accumulation) until it can no longer sustain the CA. At that point, the CA breaks down radically — not gradually — producing sleep onset. NREM sleep restores the substrate; as it periodically re-approaches the criticality threshold during restoration, the CA briefly re-emerges, producing REM sleep and dreams. The 90-minute ultradian cycle is the substrate oscillating around the critical point during this restoration process.

This yields multiple testable sub-predictions:

1. **Waking criticality decline**: Criticality markers (PCI, power-law exponents, Lempel-Ziv complexity) should decline measurably across the waking day, reflecting substrate drift.
2. **Sleep onset as radical transition**: The transition to sleep should correspond to a step-like drop in criticality markers, not a gradual dimming — reflecting the CA's digital breakdown.
3. **NREM/REM cycling tracks criticality**: Within sleep, REM phases should show criticality markers significantly higher than adjacent NREM phases, and the 90-minute ultradian cycle should be visible in criticality time-series.
4. **Lucid dreaming as ESM threshold crossing**: During REM, if the substrate reaches sufficient criticality, the ESM activates — producing lucid dreaming. This onset should be detectable as a step-like discontinuity in EEG complexity measures, not a gradual ramp (LaBerge, 1985).
5. **Sleep deprivation produces subcriticality**: Extended wakefulness should drive criticality markers progressively below the threshold, with cognitive deficits correlating with the degree of subcriticality.

**Mechanism**: The brain's analog substrate is never stable enough for reliable digital computation. The CA at criticality self-organizes a stable computational layer, but this requires substrate conditions (neurotransmitter availability, metabolic homeostasis) that degrade over time. Sleep is the restoration mechanism. The argument for why a CA is required is precisely that the substrate is uncalibratable — criticality provides the only regime in which robust computation can self-organize on inherently noisy hardware.

**Testability**: High. Sub-predictions (a)-(c) require polysomnographic recording with concurrent criticality analysis across full sleep-wake cycles. Sub-prediction (d) uses the established lucid-dreamer signaling paradigm. Sub-prediction (e) requires sleep deprivation protocols with concurrent criticality measurement. All use existing methods and equipment.

**Unique?**: Partially shared with criticality frameworks in general, but the specific claim — that sleep *exists because* the CA requires periodic substrate restoration, and that NREM/REM architecture directly reflects criticality oscillations — is distinctive. No competing theory of consciousness provides this specific functional account of sleep architecture.

### 8.9 Prediction 9: DID Alters Have Distinct Neural Process Signatures

**Statement**: Different alters in DID correspond to distinct, measurable configurations of neural activity — not merely behavioral differences or different self-reports, but different neural dynamics detectable through neuroimaging.

**Mechanism**: Virtual model forking. Each alter is a distinct configuration of the ESM, running on the same substrate but with different parameters. Different parameters should produce different activity patterns.

**Testability**: High. fMRI or EEG recording during controlled alter switching in DID patients. Compare within-patient across-alter variability against within-patient within-alter variability. The prediction is that across-alter variability will be significantly greater than within-alter variability and will show consistent alter-specific patterns.

**Unique?**: Yes. While some neuroimaging studies of DID exist (Reinders et al., 2003, 2008), the Four-Model Theory provides the theoretical basis for predicting *consistent, alter-specific neural signatures* rather than merely *differences*. The theory predicts a specific organizational principle: each alter is a distinct ESM configuration, so the neural differences should be located in ESM-related networks (particularly default mode network / medial prefrontal / posterior cingulate regions).

### 8.10 The Ultimate Prediction

If the Four-Model Theory is correct, it should be possible to *build* a conscious machine by implementing the specified architecture: four nested models (IWM, ISM, EWM, ESM) operating at criticality on a substrate of sufficient complexity. The theory predicts that such a system would not merely simulate consciousness (as an LLM might be said to do) but would *be* conscious — would have genuine phenomenal experience constituted by its virtual models.

This prediction is not currently testable — the engineering does not yet exist, and even if it did, the other-minds problem would make verification philosophically difficult. However, the prediction sets a bold bar: if the theory is correct, the difference between interacting with a conscious artificial system and interacting with any current AI should be qualitatively obvious to human observers, just as the difference between a conversation with a conscious human and a conversation with a cleverly programmed chatbot is (according to the theory) a difference in *kind*, not merely in degree.

---

## 9. Open Questions

Intellectual honesty requires identifying what the theory does not yet resolve. These are research frontiers, not theoretical weaknesses — they are questions that arise *from* the theory and that the theory's framework helps to sharpen.

**1. Are all four models virtual?** The theory as presented describes the implicit models (IWM, ISM) as "real side" and the explicit models (EWM, ESM) as "virtual side." But it is not certain that this division is sharp. The implicit models might themselves have virtual properties — they are, after all, *models*, not raw physics. If the implicit models are also virtual in some sense, what constitutes the "real side"? The raw physical substrate with no model-level description? This is an open question even for the theory's author, and its resolution may have consequences for the theory's treatment of the Hard Problem.

**2. Mathematical formalization.** The theory's criticality requirement is specified qualitatively (Wolfram's Class 4 regime), not quantitatively. A full mathematical treatment — defining the four models formally, specifying the criticality threshold in terms of measurable quantities, deriving the predictions as formal consequences — remains to be developed. The ConCrit framework's mathematical tools (power-law exponents, detrended fluctuation analysis, branching parameters) provide a starting point, as do the formal tools of dynamical systems theory and information geometry.

**3. Physical implementation.** Which physical mechanism in the biological brain supports criticality? Candidates include cortical column dynamics, thalamocortical standing waves, glial modulation, and (more speculatively) quantum processes in microtubules (Penrose & Hameroff, 1994; though see Tegmark, 2000 for decoherence objections). The Four-Model Theory is agnostic here: it specifies the *functional* requirements without mandating a specific physical mechanism. Resolving this question is an empirical task for neuroscience.

**4. Minimum configuration for consciousness.** Can the four models partially dissociate? Is it possible to have an EWM without an ESM (world-experience without self-experience), or an ESM without an EWM (self-experience without world-experience)? What is the minimum set of models required for consciousness, versus self-aware consciousness, versus full human-type consciousness? The theory's graduated levels (Section 3.5) suggest a hierarchy, but the exact minimum configuration may require simulation or empirical investigation to determine.

**5. Multi-level substrate architecture.** The biological brain can be analyzed as a hierarchy of nested systems: the physical substrate; within it, the proteomic (molecular) and topological (connectivity) systems, which mutually constrain each other; arising from these, the electrochemical system (neural signaling dynamics); and emerging from that, the virtual system — the cortical automaton that hosts the four models (Gruber, 2015). Each level both shapes and is shaped by its neighbors: the virtual system, over time, modifies the topological structure of the substrate it runs on. This raises a question for artificial consciousness: which levels of this hierarchy are essential, and which are specific to biological implementation? The theory's substrate-independence claim (Section 4.4) implies that only the virtual level is strictly required, but the bidirectional causal flow between levels suggests that decoupling the virtual system from its lower-level supports may not be straightforward.

**6. Decoding the virtual side.** The theory's real/virtual distinction has a methodological consequence that deserves explicit statement: the virtual side — the conscious simulation — is not directly accessible from external observation. Neuroimaging techniques (fMRI, EEG, MEG) capture substrate-level activity: blood-oxygen-level-dependent signals, electrical field potentials, magnetic flux. These are real-side measurements. They correlate with conscious states but do not constitute a readout of the simulation itself. To actually decode the content of conscious experience from neural data would require understanding the "programming language" of the brain — the mapping from substrate dynamics to virtual content — which in turn would require something approaching a full simulated connectome. The theory tells us *what* the simulation is and *where* it lives (in the explicit models, at the virtual level), but it does not provide the decoder ring. Developing this decoder — bridging from substrate measurement to virtual-content readout — constitutes a concrete research programme that follows directly from the theory's architecture and would, if achieved, provide the most direct possible test of the real/virtual distinction.

**7. The holography-criticality nexus.** The theory invokes both holographic storage (Section 5.2) and Class 4 criticality (Section 3.7) as essential features of the conscious substrate. The formal relationship between these two properties remains unexplored and presents a challenge suited to mathematical and computational investigation. Three distinct possibilities merit examination:

(a) **Holographic substrate → Class 4 dynamics.** Does a neural substrate that stores information holographically (in the patchwork sense defined in Section 5.2) necessarily exhibit Class 4 dynamics under appropriate driving conditions? If so, criticality would be a *consequence* of the storage architecture rather than an independent requirement, simplifying the theory's axioms.

(b) **Class 4 automaton with holographic rule structure.** Can a cellular automaton be constructed whose transition rules are themselves defined holographically — where each cell's update rule is a distributed function of the global rule set, degrading gracefully under partial rule deletion? Such a system would unify the holographic and criticality principles at the level of the automaton's definition rather than its behavior, and its characterization would constitute progress toward a mathematical formalization of the theory (see Open Question 2).

(c) **Class 4 dynamics → holographic emergent behavior.** Does a Class 4 automaton, regardless of its rule structure, necessarily produce holographic-like properties in its emergent patterns — distributed information, graceful degradation, part-contains-whole structure? If this can be demonstrated, the holographic character of neural information storage would be derivable from the criticality requirement alone. A system satisfying both (a) and (b) — holographic rules generating holographic output through Class 4 dynamics — would constitute a computational fixed point: a process that encodes its own structure at every level. If such a system exists, it would suggest a deep connection between critical computation, holographic encoding, and self-referential structure — potentially relevant to cosmological questions about the computational nature of physical law.

Resolving which of these relationships holds (and whether multiple hold simultaneously) is a mathematical challenge that lies at the intersection of cellular automata theory, information theory, and the theory of distributed computation. These questions are speculative and lie at the boundary of the theory's current scope, but they are well-defined mathematical problems. The author invites researchers in these fields to investigate these conjectures, which may bear on questions in computational complexity well beyond consciousness science.

---

## 10. Discussion

### 10.1 Implications for Artificial Consciousness

The Four-Model Theory provides an engineering specification for artificial consciousness: implement the four-model architecture on a substrate operating at criticality. This is a concrete deliverable, not an abstract philosophical claim.

Current AI systems fail this specification in at least two ways. Large language models (LLMs) operate via feedforward inference (transformer attention is computed in a single pass without recurrent dynamics), which corresponds to Wolfram's Class 1/2 — far below the criticality threshold. They also lack the four-model architecture: there is no ISM (no substrate-level self-knowledge that is *distinct from* the model's outputs), no ESM (no real-time self-simulation that constitutes a subjective perspective), and no real/virtual split (no two-level ontology in which experience resides at the virtual level).

This does not mean that LLMs are necessarily non-conscious — the theory cannot prove a negative — but it predicts that they lack the architecture required for consciousness as the theory defines it. The growing discourse around AI consciousness (Butlin et al., 2023, 2025; Schwitzgebel, 2025; Birch, 2025) and AI welfare (Long et al., 2024; Anthropic, 2025) makes this distinction practically important. A theory that provides clear criteria for artificial consciousness — rather than vague analogies to human cognition — has immediate ethical and engineering value. The intelligence implications of this architectural specification are explored in Gruber (forthcoming), which argues that current AI systems fail to exhibit self-directed intellectual development precisely because they lack the motivational component that drives the recursive intelligence loop.

### 10.2 Implications for Consciousness Science

The Four-Model Theory suggests a shift in experimental priorities. Rather than adjudicating between IIT and GNW (the current focus of adversarial collaborations), the field should:

1. **Test the criticality prediction across all anesthetic agents** (Prediction 5) — this is achievable with current methods and would provide strong evidence for or against the criticality framework.
2. **Design controlled ego-dissolution experiments** (Prediction 3) — the most distinctive prediction, uniquely generated by the redirectable ESM mechanism.
3. **Investigate the psychedelic-anosognosia connection** (Prediction 4) — a cross-domain prediction that, if confirmed, would constitute strong evidence for the variable-permeability mechanism.
4. **Measure criticality at lucid dream onset** (Prediction 8) — achievable with established paradigms and equipment.

These experiments do not require committing to the Four-Model Theory in its entirety. They test specific mechanisms (criticality, redirectable ESM, variable permeability) that could be incorporated into other frameworks if confirmed.

### 10.3 Limitations

**No institutional laboratory.** The predictions presented here were derived theoretically and have not been tested in the author's own laboratory. While this does not affect their validity as predictions, it does mean that empirical testing depends on the willingness of established laboratories to take them up.

**The causal status of experience is nuanced and will draw fire from both sides.** The theory holds that qualia lack independent causal power over the substrate, yet the simulation of which they are constitutive is functionally essential — the substrate's own mechanism for consequence-evaluation (Section 4.2). This is distinct from classical epiphenomenalism, in which consciousness is a causally inert by-product. The position will face resistance from two directions: philosophers who insist that consciousness must have independent causal efficacy will reject the denial of direct causal power, while strict epiphenomenalists will object that the feedback loop between explicit and implicit models smuggles causation back in under another name. The defense offered in Section 4.2 is, I believe, internally consistent, but the reader should be aware that the theory's causal architecture occupies contested ground between these camps.

**Qualitative rather than quantitative.** The theory's predictions are currently stated in qualitative terms ("criticality increases," "permeability changes," "ESM redirects"). Quantitative formalization would strengthen the predictions and enable more precise experimental testing. This is acknowledged as a priority for future work.

**The other-minds problem.** The ultimate prediction — that a system built to the theory's specification would be conscious — faces the standard other-minds problem: how would we verify consciousness from the outside? The theory predicts that the difference would be qualitatively obvious to human observers, but "qualitatively obvious" is not a measurement. Developing consciousness indicators that can be applied to artificial systems is a challenge for the entire field, not specific to this theory.

**Inherent limits of inside-modeling.** The theory proposes a self-model as the basis of consciousness — but the modeler and the modeled are the same system. This raises a structural concern analogous to Godel's incompleteness: a formal system cannot prove all truths about itself. Similarly, the brain attempting to model itself faces an irreducible epistemological gap — the instrument is the object of study. The theory acknowledges this limitation explicitly through the Meta-Problem (Section 3.8): the ESM cannot observe the ISM's mechanisms, which is why consciousness seems mysterious *from the inside*. This is a feature of the architecture, not a flaw in the theory, but it does imply that any theory of consciousness generated by a conscious system will carry a residual blind spot.

**Language linearizes non-linear phenomena.** Any theoretical framework expressed in natural language necessarily serializes phenomena that may be inherently parallel and non-linear. The four models operate simultaneously in high-dimensional state spaces; describing them sequentially in prose introduces a representational loss that no amount of careful writing can fully eliminate. This limitation applies to all theories of consciousness, not only the present one, but it should be kept in mind when evaluating the theory's verbal descriptions against the multidimensional dynamics they attempt to capture.

**Criticality-rhythm relationship not formalized.** Section 5.1 argues that criticality provides punctuated stability, with biological rhythms (sleep-wake cycling, ultradian rhythms, neurotransmitter depletion and replenishment) governing how long the substrate can maintain the critical regime. This relationship between dynamical criticality and biochemical rhythm is proposed qualitatively; a formal model linking neurotransmitter kinetics to criticality maintenance and breakdown remains to be developed.

**Every model has modeling error.** The Four-Model Theory is itself a model — and every model, by definition, is a simplification that carries inherent modeling error. The theory does not claim to be a final or complete account of consciousness; it claims to be a useful one, generating testable predictions and unifying phenomena that other frameworks address in isolation. To the extent that it is wrong, the predictions in Section 8 are designed to reveal where.

---

## 11. Conclusion

The Four-Model Theory of Consciousness proposes that consciousness is a real-time self-simulation across four nested models — Implicit World Model, Implicit Self Model, Explicit World Model, and Explicit Self Model — operating on a substrate at the edge of chaos. Qualia are virtual: they are the phenomenal properties of the simulation, not of the substrate. This dissolves the Hard Problem by revealing a category error in its formulation, simultaneously closing the Explanatory Gap and accounting for the Meta-Problem.

The theory addresses all eight requirements for a complete theory of consciousness: the Hard Problem (dissolved via virtual qualia), the Explanatory Gap (dissolved alongside), the Boundary Problem (defined by the scope of virtual models), the Structure of Experience (generated by the simulation's complexity), Unity and Binding (emergent from critical dynamics), Combination and Emergence (weak emergence, no combination problem), the Causal Role (the architecture is causally efficacious; qualia lack independent causal power but are constitutive of the simulation the substrate deploys for evaluation), and the Meta-Problem (structural inaccessibility of the ISM to the ESM).

The theory generates nine novel testable predictions, including that ego dissolution content is controllable via sensory input (Prediction 3), that psychedelics should alleviate anosognosia (Prediction 4), and that all consciousness-abolishing anesthetics converge on criticality disruption (Prediction 5). Several of these predictions are highly distinctive to the Four-Model Theory.

The theory's criticality requirement was derived from Wolfram's computational framework in 2015, independently of the empirical criticality program already underway (Beggs & Plenz, 2003; Carhart-Harris et al., 2014). The later large-scale consolidation — Hengen and Shew's (2025) meta-analysis of 140 datasets and Algom and Shriki's (2026) ConCrit framework — confirmed the criticality-consciousness link. This convergence — a theoretical prediction derived independently from computational first principles, later confirmed by large-scale empirical synthesis — provides notable support.

Open questions remain: the status of the implicit models (real or also virtual?), the need for mathematical formalization, the specific physical mechanism supporting criticality, and the minimum configuration for consciousness. These are research frontiers that the theory's framework helps to sharpen.

The ambition of consciousness science is not merely to correlate neural activity with subjective reports but to understand *why* there is experience at all. The Four-Model Theory offers an answer: there is experience because there is a simulation, and within the simulation, experience is not an addition to the process but is constitutive of it. The way to test this answer is not through philosophical argument alone but through the predictions it generates — and ultimately, through the engineering challenge of building a system to the specification and observing whether the result is, as the theory predicts, qualitatively unlike anything that exists today. The theory's implications extend beyond consciousness science: the cognitive-learning capacity it identifies as a consequence of the four-model architecture is the foundation for a recursive model of intelligence (Gruber, forthcoming) in which knowledge, performance, and motivation form a self-reinforcing loop.

---

## Acknowledgments

This paper was written with the assistance of Claude (Anthropic, 2026), which served as editor, cross-checker, and writing tool throughout the drafting process. The theory, arguments, predictions, and all intellectual content are entirely the author's, originally published in Gruber (2015); Claude assisted with literature cross-referencing, prose drafting from the author's directions, and internal consistency checking.

---

## Data Availability

No new data were generated or analysed in support of this research.

---

## Funding

This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

---

## References

Aaronson, S. (2014). Why I am not an integrated information theorist. Blog post. *Shtetl-Optimized*.

Albantakis, L., Barbosa, L., et al. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms. *PLOS Computational Biology*, 19(10), e1011465.

Algom, I. & Shriki, O. (2026). The concrit framework: Critical brain dynamics as a unifying mechanistic framework for theories of consciousness. *Neuroscience & Biobehavioral Reviews*, 180, 106483.

Alkire, M.T., Haier, R.J., & Fallon, J.H. (2000). Toward a unified theory of narcosis: Brain imaging evidence for a thalamocortical switch as the neurophysiologic basis of anesthetic-induced unconsciousness. *Consciousness and Cognition*, 9(3), 370-386.

Anthropic. (2025). Exploring model welfare. Research report.

Baars, B.J. (1988). *A Cognitive Theory of Consciousness*. Cambridge University Press.

Beggs, J.M. & Plenz, D. (2003). Neuronal avalanches in neocortical circuits. *Journal of Neuroscience*, 23(35), 11167-11177.

Birch, J. (2025). AI consciousness: A centrist manifesto. *PhilPapers*.

Block, N. (1995). On a confusion about a function of consciousness. *Behavioral and Brain Sciences*, 18(2), 227-247.

Block, N. (2007). Consciousness, accessibility, and the mesh between psychology and neuroscience. *Behavioral and Brain Sciences*, 30(5-6), 481-499.

Boly, M., et al. (2012). Connectivity changes underlying spectral EEG changes during propofol-induced loss of consciousness. *Journal of Neuroscience*, 32(20), 7082-7090.

Butlin, P., et al. (2023). Consciousness in artificial intelligence: Insights from the science of consciousness. *arXiv*:2308.08708.

Butlin, P., et al. (2025). Identifying indicators of consciousness in AI systems. *Trends in Cognitive Sciences*.

Carhart-Harris, R.L., et al. (2012). Neural correlates of the psychedelic state as determined by fMRI studies with psilocybin. *Proceedings of the National Academy of Sciences*, 109(6), 2138-2143.

Carhart-Harris, R.L., et al. (2014). The entropic brain: A theory of conscious states informed by neuroimaging research with psychedelic drugs. *Frontiers in Human Neuroscience*, 8, 20.

Carhart-Harris, R.L., et al. (2016). Neural correlates of the LSD experience revealed by multimodal neuroimaging. *Proceedings of the National Academy of Sciences*, 113(17), 4853-4858.

Casali, A.G., et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. *Science Translational Medicine*, 5(198), 198ra105.

Casarotto, S., et al. (2016). Stratification of unresponsive patients by an independently validated index of brain complexity. *Annals of Neurology*, 80(5), 718-729.

Chalmers, D.J. (1995). Facing up to the problem of consciousness. *Journal of Consciousness Studies*, 2(3), 200-219.

Chalmers, D.J. (1996). *The Conscious Mind: In Search of a Fundamental Theory*. Oxford University Press.

Chalmers, D.J. (2016). The combination problem for panpsychism. In G. Brüntrup & L. Jaskolla (Eds.), *Panpsychism: Contemporary Perspectives*. Oxford University Press.

Chalmers, D.J. (2018). The meta-problem of consciousness. *Journal of Consciousness Studies*, 25(9-10), 6-61.

COGITATE Consortium. (2025). An adversarial collaboration to critically evaluate theories of consciousness. *Nature*.

Corlett, P.R., et al. (2011). Glutamatergic model psychoses: Prediction error, learning, and inference. *Neuropsychopharmacology*, 36(1), 294-315.

Dehaene, S. & Changeux, J.P. (2011). Experimental and theoretical approaches to conscious processing. *Neuron*, 70(2), 200-227.

Dehaene, S., Changeux, J.P., & Naccache, L. (2011). The global neuronal workspace model of conscious access: From neuronal architectures to clinical applications. *Research and Perspectives in Neurosciences*, 18, 55-84.

Dennett, D.C. (1991). *Consciousness Explained*. Little, Brown and Company.

Doerig, A., et al. (2019). The unfolding argument: Why IIT and other causal structure theories cannot explain consciousness. *Consciousness and Cognition*, 72, 49-59.

Frankish, K. (2016). Illusionism as a theory of consciousness. *Journal of Consciousness Studies*, 23(11-12), 11-39.

Graziano, M.S.A. (2024). Illusionism big and small: Some options for explaining consciousness. *eNeuro*, 11(10), ENEURO.0210-24.2024.

Fries, P. (2005). A mechanism for cognitive dynamics: Neuronal communication through neuronal coherence. *Trends in Cognitive Sciences*, 9(10), 474-480.

Fries, P. (2015). Rhythms for cognition: Communication through coherence. *Neuron*, 88(1), 220-235.

Gazzaniga, M.S. (2000). Cerebral specialization and interhemispheric communication: Does the corpus callosum enable the human condition? *Brain*, 123(7), 1293-1326.

Gazzaniga, M.S., Bogen, J.E., & Sperry, R.W. (1962). Some functional effects of sectioning the cerebral commissures in man. *Proceedings of the National Academy of Sciences*, 48(10), 1765-1769.

Goff, P. (2019). *Galileo's Error: Foundations for a New Science of Consciousness*. Pantheon Books.

Gomez-Marin, A. & Seth, A.K. (2025). A science of consciousness beyond pseudo-science and pseudo-consciousness. *Nature Neuroscience*, 28, 703-706.

Gray, C.M., König, P., Engel, A.K., & Singer, W. (1989). Oscillatory responses in cat visual cortex exhibit inter-columnar synchronization which reflects global stimulus properties. *Nature*, 338(6213), 334-337.

Graziano, M.S.A. (2013). *Consciousness and the Social Brain*. Oxford University Press.

Gruber, M. (2015). *Die Emergenz des Bewusstseins*. Self-published. ISBN 9781326652074.

Gruber, M. (forthcoming). Why intelligence models must include motivation: A recursive framework. Manuscript in preparation for *New Ideas in Psychology*.

Hengen, K.B. & Shew, W.L. (2025). Is criticality a unified setpoint of brain function? *Neuron*, 113(16), 2582-2598.

Güntürkün, O. & Bugnyar, T. (2016). Cognition without cortex. *Trends in Cognitive Sciences*, 20(4), 291-303.

Hinton, G.E., McClelland, J.L., & Rumelhart, D.E. (1986). Distributed representations. In D.E. Rumelhart, J.L. McClelland, & the PDP Research Group (Eds.), *Parallel Distributed Processing*, Vol. 1. MIT Press.

Huxley, T.H. (1874). On the hypothesis that animals are automata, and its history. *The Fortnightly Review*, 16(95), 555-580.

IIT-Concerned, Klincewicz, M., Cheng, T., et al. (2025). What makes a theory of consciousness unscientific? *Nature Neuroscience*, 28, 689-693.

Jackson, F. (1982). Epiphenomenal qualia. *Philosophical Quarterly*, 32(127), 127-136.

James, W. (1890). *The Principles of Psychology*. Henry Holt and Company.

Kim, J. (1993). The non-reductivist's troubles with mental causation. In J. Heil & A. Mele (Eds.), *Mental Causation*. Oxford University Press.

Klüver, H. (1966). *Mescal and Mechanisms of Hallucinations*. University of Chicago Press.

Tononi, G., Albantakis, L., Barbosa, L., et al. (2025). Consciousness or pseudo-consciousness? A clash of two paradigms. *Nature Neuroscience*, 28, 694-702.

Kuhn, T.S. (1962). *The Structure of Scientific Revolutions*. University of Chicago Press.

Lamme, V.A.F. (2006). Towards a true neural stance on consciousness. *Trends in Cognitive Sciences*, 10(11), 494-501.

Lamme, V.A.F. (2010). How neuroscience will change our view on consciousness. *Cognitive Neuroscience*, 1(3), 204-220.

Lau, H. & Rosenthal, D. (2011). Empirical support for higher-order theories of conscious awareness. *Trends in Cognitive Sciences*, 15(8), 365-373.

Levine, J. (1983). Materialism and qualia: The explanatory gap. *Pacific Philosophical Quarterly*, 64(4), 354-361.

Libet, B. (1985). Unconscious cerebral initiative and the role of conscious will in voluntary action. *Behavioral and Brain Sciences*, 8(4), 529-539.

Llinás, R.R. & Ribary, U. (1993). Coherent 40-Hz oscillation characterizes dream state in humans. *Proceedings of the National Academy of Sciences*, 90(5), 2078-2081.

Llinás, R.R., Ribary, U., Contreras, D., & Pedroarena, C. (1998). The neuronal basis for consciousness. *Philosophical Transactions of the Royal Society of London B*, 353(1377), 1841-1849.

Long, R., Sebo, J., Butlin, P., Birch, J., Chalmers, D., et al. (2024). Taking AI welfare seriously. *arXiv*:2411.00986.

Melloni, L., et al. (2023). An adversarial collaboration protocol for testing contrasting predictions of global neuronal workspace and integrated information theory. *PLOS ONE*, 18(2), e0268577.

Metzinger, T. (2003). *Being No One: The Self-Model Theory of Subjectivity*. MIT Press.

Metzinger, T. (2009). *The Ego Tunnel: The Science of the Mind and the Myth of the Self*. Basic Books.

Monti, M.M., et al. (2010). Willful modulation of brain activity in disorders of consciousness. *New England Journal of Medicine*, 362(7), 579-589.

Nagel, T. (1974). What is it like to be a bat? *Philosophical Review*, 83(4), 435-450.

Owen, A.M., et al. (2006). Detecting awareness in the vegetative state. *Science*, 313(5792), 1402.

Penrose, R. & Hameroff, S. (1994). Orchestrated reduction of quantum coherence in brain microtubules: A model for consciousness. *Mathematics and Computers in Simulation*, 40(3-4), 453-480.

Pinto, Y., et al. (2017). Split brain: Divided perception but undivided consciousness. *Brain*, 140(5), 1231-1237.

Priesemann, V., et al. (2013). Neuronal avalanches differ from wakefulness to deep sleep — evidence from intracranial depth recordings in humans. *PLOS Computational Biology*, 9(3), e1002985.

Priesemann, V., et al. (2014). Spike avalanches in vivo suggest a driven, slightly subcritical brain state. *Frontiers in Systems Neuroscience*, 8, 108.

Reinders, A.A.T.S., et al. (2003). One brain, two selves. *NeuroImage*, 20(4), 2119-2125.

Reinders, A.A.T.S., et al. (2008). Cross-examining dissociative identity disorder: Neuroimaging and etiology on trial. *Neurocase*, 14(1), 44-53.

Rodriguez, E., et al. (1999). Perception's shadow: Long-distance synchronization of human brain activity. *Nature*, 397(6718), 430-433.

Rosenthal, D. (2005). *Consciousness and Mind*. Oxford University Press.

Schartner, M., et al. (2017). Increased spontaneous MEG signal diversity for psychoactive doses of ketamine, LSD and psilocybin. *Scientific Reports*, 7, 46421.

Schurger, A., Sitt, J.D., & Dehaene, S. (2012). An accumulator model for spontaneous neural activity prior to self-initiated movement. *Proceedings of the National Academy of Sciences*, 109(42), E2904-E2913.

Schwitzgebel, E. (2025). AI and consciousness. *arXiv*:2510.09858.

Seth, A. (2021). *Being You: A New Science of Consciousness*. Dutton.

Strawson, G. (2006). Realistic monism: Why physicalism entails panpsychism. *Journal of Consciousness Studies*, 13(10-11), 3-31.

Tagliazucchi, E., et al. (2012). Criticality in large-scale brain fMRI dynamics unveiled by a novel point process analysis. *Frontiers in Physiology*, 3, 15.

Tagliazucchi, E., et al. (2016). Increased global functional connectivity correlates with LSD-induced ego dissolution. *Current Biology*, 26(8), 1043-1050.

Tegmark, M. (2000). Importance of quantum decoherence in brain processes. *Physical Review E*, 61(4), 4194-4206.

Timmermann, C., et al. (2019). Neural correlates of the DMT experience assessed with multivariate EEG. *Scientific Reports*, 9, 16324.

Timmermann, C., et al. (2023). Human brain effects of DMT assessed via EEG-fMRI. *Proceedings of the National Academy of Sciences*, 120(13), e2218949120.

Tononi, G. (2004). An information integration theory of consciousness. *BMC Neuroscience*, 5, 42.

Wegner, D.M. (2002). *The Illusion of Conscious Will*. MIT Press.

Wolfram, S. (2002). *A New Kind of Science*. Wolfram Media.

Zurek, W.H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Reviews of Modern Physics*, 75(3), 715-775.

Bayne, T. (2010). *The Unity of Consciousness*. Oxford University Press.

Bruineberg, J., Dolega, K., Dewhurst, J., & Baltieri, M. (2022). The Emperor's new Markov blankets. *Behavioral and Brain Sciences*, 45, e183.

Coleman, S. (2014). The real combination problem: Consciousness, panpsychism, and phenomenal bonding. *Erkenntnis*, 79(S1), 19-44.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.

Kirkeby-Hinrup, A., Fink, S.B., & Overgaard, M. (2025). The Multiple Generator Hypothesis. *Neuroscience of Consciousness*, 2025(1), niaf035.

LaBerge, S. (1985). *Lucid Dreaming*. Ballantine Books.

Milinkovic, B. & Aru, J. (2025). Biological computationalism. *Neuroscience & Biobehavioral Reviews*, 181, 106524.

Revonsuo, A. (1999). Binding and the phenomenal unity of consciousness. *Consciousness and Cognition*, 8(2), 173-185.

Singer, W. & Gray, C.M. (1995). Visual feature integration and the temporal correlation hypothesis. *Annual Review of Neuroscience*, 18, 555-586.

Treisman, A. (1996). The binding problem. *Current Opinion in Neurobiology*, 6(2), 171-178.

Van Rullen, R. & Koch, C. (2003). Is perception discrete or continuous? *Trends in Cognitive Sciences*, 7(5), 207-213.

von Neumann, J. (1932). *Mathematische Grundlagen der Quantenmechanik*. Springer.

Wigner, E.P. (1961). Remarks on the mind-body question. In I.J. Good (Ed.), *The Scientist Speculates*. Heinemann.

Anton, G. (1899). Über die Selbstwahrnehmung der Herderkrankungen des Gehirns durch den Kranken bei Rindenblindheit und Rindentaubheit. *Archiv für Psychiatrie und Nervenkrankheiten*, 32, 86-127.

Aldrich, M.S., Alessi, A.G., Beck, R.W., & Gilman, S. (1987). Cortical blindness: Etiology, diagnosis, and prognosis. *Annals of Neurology*, 21(2), 149-158.

Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Großhirnrinde*. Johann Ambrosius Barth.

Cybenko, G. (1989). Approximation by superpositions of a sigmoidal function. *Mathematics of Control, Signals, and Systems*, 2(4), 303-314.

Engel, A.K. & Singer, W. (2001). Temporal binding and the neural correlates of sensory awareness. *Trends in Cognitive Sciences*, 5(1), 16-25.

Hornik, K., Stinchcombe, M., & White, H. (1989). Multilayer feedforward networks are universal approximators. *Neural Networks*, 2(5), 359-366.

Lashley, K.S. (1950). In search of the engram. *Symposia of the Society for Experimental Biology*, 4, 454-482.

Pribram, K.H. (1991). *Brain and Perception: Holonomy and Structure in Figural Processing*. Lawrence Erlbaum Associates.

Weiskrantz, L. (1986). *Blindsight: A Case Study and Implications*. Oxford University Press.
