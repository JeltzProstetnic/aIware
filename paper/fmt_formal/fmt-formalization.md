# Toward a Mathematical Formalization of the Four-Model Theory: A Recommended Approach

**Matthias Gruber**

*Independent researcher*

*ORCID: 0009-0005-9697-1665*

*Correspondence: matthias@matthiasgruber.com*

---

## Abstract

The Four-Model Theory of Consciousness (FMT; Gruber, 2015, 2026) proposes that consciousness is constituted by real-time self-simulation across four nested models — Implicit World Model (IWM), Implicit Self Model (ISM), Explicit World Model (EWM), and Explicit Self Model (ESM) — operating at the edge of chaos. The theory currently operates in natural language. This paper outlines a recommended mathematical formalization strategy. The four models are understood as a *minimum sufficient set* for human-level consciousness, not an exhaustive enumeration: the biological substrate — built from spiking neurons atop proteomic networks with their own intracellular learning — implements an uncountable number of overlapping models on both sides of the implicit/explicit divide. The formalization must therefore treat models not as discrete, countable objects but as a continuous density over a model space, with the virtual/non-virtual split as the one hard ontological boundary. Six formalization modules are proposed: (1) a continuous model-space framework replacing the discrete 2×2 taxonomy, formalizing the multiple-generator architecture, (2) permeability as a family of channel-specific information-theoretic gating mechanisms, (3) criticality as a conjectured operating-regime hypothesis (empirically motivated, resting on two open lemmas, and neither a derived consequence of self-referential closure nor a stated requirement on consciousness), (4) ESM redirection dynamics, (5) self-referential closure including the observability constraint ($O_{\mathrm{ESM}}$ ⊆ $S_{\mathrm{EWM}}$), and (6) category-theoretic architecture. A phased build order prioritizes empirically testable components. The formalization is offered as a research program specification for mathematically trained collaborators; verification of the formal apparatus is explicitly deferred to domain experts.

**Keywords**: consciousness, formalization, four-model theory, model space, criticality, transfer entropy, self-referential closure, observability constraint, information geometry

---

## 1. Introduction

### 1.1 The Formalization Gap

The Four-Model Theory (Gruber, 2015, 2026) addresses all eight canonical requirements for a theory of consciousness — the Hard Problem, the Explanatory Gap, the Boundary Problem, the Structure of Experience, Unity and Binding, Combination and Emergence, the Causal Role, and the Meta-Problem — within a single framework built on three principles (Gruber, 2026, Section 3): open-ended computation allows free modelling, near-criticality being the signature that property leaves in neural tissue rather than the requirement itself; recurrent non-linear dynamics of sufficient complexity host a second computational level; and phenomenology is a real, physical effect on that level, arising exactly where the modelling closes on itself. The four model kinds, redirection of the modelling resource onto the non-self, variable implicit-explicit permeability and forking of the self-model are not among the principles: they follow as consequences with explanatory power (Gruber, 2026, Section 6.0). This matters for what follows, because a formalization that axiomatized the consequences would be formalizing the wrong objects.

The theory is currently stated entirely in natural language. Its rivals carry notation: Integrated Information Theory (IIT; Tononi, 2004; Albantakis et al., 2023) has Φ and the qualia space formalism, Predictive Processing (PP; Friston, 2010; Seth, 2021) has the free energy principle and active inference, and Global Neuronal Workspace (GNW; Baars, 1988; Dehaene & Changeux, 2011) has computational broadcasting models. The Four-Model Theory has verbal descriptions: "permeability increases," "ESM redirects," "criticality threshold."

Notation alone does not make a theory testable. Φ is a fully specified mathematical object that has never been computed for a real brain and is provably intractable for realistic systems (Aaronson, 2014). Testability comes from **accepting constraints**: functional forms that can turn out to be empirically wrong, and quantities that can be measured and found not to behave as claimed.

By that standard FMT's gap is specific. Its mechanisms are stated so that almost no observation could embarrass them: "permeability increases" names a direction without a magnitude, a functional form or a measurement procedure, so it accommodates any entropy result after the fact. Each verbal mechanism therefore needs a functional form that data can contradict (§9.1).

### 1.2 Why Not Simply Formalize the Four Models?

The obvious approach — assigning a mathematical object to each of the four models and formalizing their interactions — would be premature and would misrepresent the theory's own commitments.

The four models (IWM, ISM, EWM, ESM) are a *principled lower bound*, not an architectural specification. They represent the minimum configuration required for human-level consciousness: a system must model both the world and itself, and must do so at both the structural/implicit and the dynamic/explicit level. This is a constraint on the *minimum*, not a claim about the *actual*.

The biological substrate — spiking neurons atop proteomic networks, with intracellular signaling pathways constituting their own learning and computational intelligence even within a single cell (Bhalla, 2014), and with structural plasticity operating on the same neurons at the level of dendritic spines (Bhatt et al., 2009) — implements an effectively uncountable number of overlapping models on both sides of the implicit/explicit divide. A motor model of reaching for a cup simultaneously encodes world-geometry (cup location, obstacle positions) and self-kinematics (arm configuration, grip aperture). An emotional model of a social interaction simultaneously encodes other-knowledge (world) and self-assessment (self). The boundaries between "models" are not sharp and their number is not well-defined in a neural architecture.

To formalize the theory correctly, therefore, requires treating the four models not as four discrete objects but as four *regions* in a continuous space of modeling activity — the canonical extrema around which the actual, high-dimensional, uncountable modeling ecology of the brain is organized. The formalization must be statistical, not enumerative.

### 1.3 Scope and Limitations

This paper specifies a formalization research program. It proposes mathematical frameworks, defines quantities, and outlines a build order. It does *not* verify the mathematical apparatus — the author is not a mathematician, and formal verification is explicitly deferred to domain experts. The equations presented here are intended as precise specifications of *what needs to be formalized* and *which mathematical tools are appropriate*, not as proven theorems.

The paper is structured as follows. Section 2 develops the continuous model-space framework, including the multiple-generator interpretation of the model density. Section 3 formalizes permeability as a family of channel-specific gating mechanisms. Section 4 addresses criticality — framed as a conjectured operating-regime hypothesis resting on two open lemmas rather than a derived consequence of self-referential closure — and its operationalization. Section 5 formalizes the ESM redirection mechanism. Section 6 addresses self-referential closure, including the observability constraint ($O_{\mathrm{ESM}}$ ⊆ $S_{\mathrm{EWM}}$). Section 7 outlines a category-theoretic architecture. Section 8 proposes a phased build order. Section 9 identifies what formalization would buy and what it cannot deliver.

---

## 2. From Discrete Models to a Continuous Model Space

### 2.1 The Model Space

Instead of four enumerable models, define a **model space** M — a high-dimensional manifold where every point represents a distinct model the substrate is running. Each model m ∈ M has two primary properties:

- **Scope** s(m) ∈ [0, 1]: a continuous axis from pure self-representation (0) to pure world-representation (1).
- **Mode** ν(m) ∈ [0, 1]: a continuous axis from fully implicit/structural (0) to fully explicit/phenomenal (1).

The scope axis captures the observation that most actual neural models blend self and world: a motor reaching model encodes both world-geometry and body-kinematics simultaneously. The mode axis captures the theory's central claim that the implicit-explicit boundary is graded, not binary (Gruber, 2026, Section 3.6) — while maintaining that there exists a threshold $\nu_{\mathrm{crit}}$ above which modeling activity is phenomenal.

The four canonical models are recovered as **extremal points** in this 2D projection:

- IWM ≈ (s = 1, ν = 0): Pure world-knowledge, fully implicit.
- ISM ≈ (s = 0, ν = 0): Pure self-knowledge, fully implicit.
- EWM ≈ (s = 1, ν = 1): Pure world-simulation, fully explicit.
- ESM ≈ (s = 0, ν = 1): Pure self-simulation, fully explicit.

But the actual substrate populates the *entire* [0, 1]² space with a density of models.

### 2.2 The Model Density Function

Define a **model density** ρ(s, ν, t) over the scope-mode space at time t. The quantity ρ(s, ν, t) ds dν represents the "amount of modeling activity" in the region [s, s+ds] × [ν, ν+dν] at time t. This is a measure-theoretic quantity, analogous to a probability density but not normalized to 1 — the total modeling activity of the brain can vary across states (more total modeling during waking than during deep sleep).

The model density function formalizes the theory's commitment to a **multiple-generator architecture** (Gruber, 2026): the conscious substrate is a continuous ecology of overlapping modeling processes. Patchwork models at every scale — from molecular-level proteomic computation through cortical-column processing to whole-brain simulation — contribute to ρ simultaneously. The four canonical models are the extremal peaks of this density; the space between them is densely populated with blended models that are simultaneously about-self-and-about-world to varying degrees. Any system implementing consciousness must therefore support a continuous density of modeling activity.

The virtual/non-virtual split — the one hard ontological claim of the theory — becomes a threshold on the mode axis:

- Virtual (phenomenal): ν > $\nu_{\mathrm{crit}}$
- Real (substrate): ν < $\nu_{\mathrm{crit}}$

Everything above $\nu_{\mathrm{crit}}$ is part of the conscious simulation. Everything below it operates "in the dark." The theory claims $\nu_{\mathrm{crit}}$ is an ontological boundary, though its value must be determined empirically.

This sits in apparent tension with §2.1's statement that the implicit-explicit boundary is graded rather than binary, and the two are reconciled as follows: what is graded is the *mode coordinate* ν, which varies continuously and on which modeling activity is distributed continuously; what is sharp is the *ontological predicate* defined on it. A continuous variable can carry a sharp threshold without ceasing to be continuous — the temperature of water is continuous while the liquid-vapour phase boundary is not — and the claim here is of that form. The gradedness is a fact about the substrate's organization; the hardness is a fact about which side of the boundary a given activity falls on. §4.6 proposes that the threshold may itself be a graph phase transition, which if correct would supply the physical mechanism that makes a sharp boundary on a continuous axis possible rather than merely stipulated.

### 2.3 The Minimum-Configuration Constraint

The theory's claim about the four canonical models becomes a density constraint rather than a discrete architectural specification:

**For consciousness of the human type, ρ must have significant mass near all four extremal points in (s, ν) space.**

Formally, define four regions $R_{\mathrm{IWM}}$, $R_{\mathrm{ISM}}$, $R_{\mathrm{EWM}}$, $R_{\mathrm{ESM}}$ as neighborhoods of the four corners, and require:

$$\int_{R_k} \rho(s, \nu, t)\, ds\, d\nu > \theta_k \quad \text{for each } k \in \{\mathrm{IWM}, \mathrm{ISM}, \mathrm{EWM}, \mathrm{ESM}\}$$

where $\theta_{k}$ are minimum-mass thresholds. A system with mass only near (s = 1, ν = 1) — world-simulation without self-simulation — would not be conscious. A system with mass only below $\nu_{\mathrm{crit}}$ — implicit processing without explicit simulation — would not be conscious. The four-model requirement is a constraint on the density profile, not a count of discrete objects.

This formulation accommodates the uncountable-models reality of the biological brain while preserving the theory's principled claim about the minimum sufficient configuration.

A note on the force of the necessity claims in this subsection. "A system with mass only near (s = 1, ν = 1) would not be conscious" is **definitional rather than empirical**: consciousness of the human type is *defined* in the parent theory as self-simulation, so a system with no self-scope mass fails the definition rather than failing an experiment. This bounds what the constraint can do: it cannot be used as evidence that self-modeling is required — that is what it assumes — and it does no work against a reader who rejects the definition. What it does supply is a precise statement of the definition in measurable terms, which is what makes the $\theta_{k}$ thresholds an empirical target rather than a restatement.

### 2.4 The Hierarchical Depth Axis

The model density function should be extended to account for the five-system hierarchy (Gruber, 2015, 2026):

ρ(s, ν, ℓ, t)

where ℓ ∈ {1, 2, 3, 4, 5} indexes the hierarchical level:

1. Physical system (atoms, molecules)
2. Electrochemical system (ion gradients, action potentials)
3. Proteomic system (receptor configurations, protein expression, intracellular signaling)
4. Topological system (synaptic connectivity, circuit architecture)
5. Virtual system (real-time dynamical patterns, the cortical automaton)

The proteomic layer (ℓ = 3) is particularly relevant: receptor configurations encode prediction models about neurotransmitter dynamics, protein expression patterns constitute a slow, molecular-scale computational intelligence operating on timescales of minutes to days (Bhalla, 2014), alongside structural remodeling of dendritic spines on a comparable timescale (Bhatt et al., 2009). These are implicit models in their own right, but at a level below the topological/synaptic level at which the standard four-model description operates.

The real/virtual split remains clean — it is a threshold on ν — but the implicit side has stratified depth, with models within models within models, all the way down to proteomic computation. The four-model description is the top-level statistical summary, analogous to describing a fluid by temperature and pressure when the underlying molecular dynamics are vastly more complex.

### 2.5 Connection to Principal Bundle Geometry

Recent work by Oizumi, Lim, and Kanai (2025) provides a complementary mathematical framework for characterizing qualia structure using principal bundle geometry. Their approach formalizes how symmetry groups G acting on sensory inputs induce a decomposition of neural representation space into orbits (qualia attributes — rigid, universal across individuals) and a quotient space (qualia signatures — plastic, shaped by learning). This rigid/plastic duality parallels the present framework's implicit/explicit distinction: orbit structure is inherited from physical symmetries (analogous to substrate-level constraints), while quotient geometry is learned (analogous to simulation-level content).

The principal bundle framework applies most naturally to the explicit side of the model space (ν > $\nu_{\mathrm{crit}}$), where it formalizes the *geometry* of phenomenal content within the EWM. The equivariant encoder f: X → Y in their framework maps onto the implicit-to-explicit transfer: the IWM stores the encoder's parameters (learned world-knowledge); the EWM is the active representation (the encoder's output). Under equivariance, the explicit model preserves the symmetry structure of the world — formalized as f(g·x) = π(g)·f(x), where π denotes the group representation. (Oizumi et al. write this representation as ρ; it is renamed here because ρ is reserved throughout this paper for the model density of §2.2.)

Two extensions are required to integrate this framework with FMT's formalization:

1. **Self-referential systems.** Oizumi et al.'s framework assumes feed-forward equivariant encoders. FMT requires self-referential closure — the ESM models the system generating the ESM. Extending principal bundles to recurrent, self-referential systems may require gauge bundle theory with connections, where the gauge connection encodes how self-referential feedback transforms the fiber structure.

2. **Altered states.** The principal bundle framework characterizes normal perceptual processing. Under psychedelic conditions (increased implicit-explicit permeability), equivariance should be disrupted — measurable via Oizumi et al.'s proposed G-empirical equivariance deviation (G-EED) metric. FMT predicts that ego dissolution should collapse the semidirect product structure of multi-attribute qualia, producing a testable prediction jointly generated by both frameworks.

The compositionality results (direct and semidirect group products for independent and hierarchically entangled attributes) are directly relevant to FMT's binding requirement (Section 5 of the parent paper): the EWM's unified scene is a composite principal bundle whose product structure formalizes how features from different cortical areas are integrated.

### 2.6 Cautions on Model-Space Estimation

Two methodological cautions apply to any empirical estimation of the model density ρ:

**Emergent dimensionality.** The 2D projection (scope × mode) is a principled simplification. The effective dimensionality of the model space may itself be emergent — determined by the critical regime of the substrate rather than imposed a priori. Background-independent models of emergent spacetime (Konopka, Markopoulou, & Smolin, 2008) demonstrate that dimensionality can arise from phase transitions in graph connectivity. If an analogous mechanism operates in cortical networks, the number of independent axes in the model space is a quantity to be *measured*, not assumed. The scope-mode framework should be understood as capturing the dominant structure near the critical point; additional dimensions may become relevant in altered states or non-human substrates.

**Discretization artifacts.** In discrete physics, the Nielsen-Ninomiya theorem (Nielsen & Ninomiya, 1981) proves that discretizing a continuous field inevitably produces spurious extra modes — the "fermion doubling" problem. An analogous effect may occur when estimating the continuous model density from discrete neural data: decomposition methods (ICA, NMF, RSA) may produce apparent "models" that are artifacts of the discretization rather than genuine modeling activity. Any implementation of the model-space framework should include criteria for distinguishing real modes from artifacts — for example, requiring that identified modes correlate with behavior, stimulus content, or report, rather than treating every ICA component as a real model.

### 2.7 Locating the Engine: The Modality-Flatness Criterion

The formalization above specifies *what* the model space is without saying *where*, in a given substrate, the machinery that generates explicit models sits. The theory has so far answered that architecturally rather than locatably: an architectural characterization tells you what to look for, not where to point the instrument.

A candidate localization criterion follows from the free-modelling requirement itself. Modality-specific machinery is, by construction, specialized: the capacity it devotes to modelling is concentrated in the modality it serves, and falls away outside it. The machinery that performs *free* modelling has no such attachment — its defining property is that its modelling capacity can be pointed anywhere. **The engine should therefore be identifiable as the region whose distribution of free modelling capacity across sensory and motor modalities is flattest**, with modality-specialized structures showing sharply peaked distributions over the same measure.

This is offered as a **method rather than as a prediction**. As stated it is an identification procedure: it either succeeds in locating a region or it does not, and a failure to find a flat-distribution region is uninformative on its own, since it may equally indicate an inadequate capacity measure. A falsifiable form is available — that the flattest-distribution region is the one whose disruption abolishes explicit modelling while modality-specific processing survives — but that form makes commitments about lesion outcomes the framework has not yet earned, and it is not claimed here. Promotion of the criterion to a prediction should wait on an operational measure of free modelling capacity that has been validated independently of the localization it is being used to perform, on pain of the circularity the cautions of Section 2.6 warn about.

Two practical notes for anyone implementing it. First, the measure must be *capacity for* modelling rather than observed modelling activity, since a region idle at the moment of measurement is not thereby unspecialized. Second, the criterion is scale-sensitive in the same way as any localization statistic: a flatness score computed on a substrate too small to support differentiated modality-specific structure has nothing to discriminate, and will report flatness everywhere. Localization results should therefore state the substrate scale and the pass rate of whatever gate defines a positive, rather than reporting the best-scoring region as though it were a detection.

---

## 3. Permeability as an Information-Theoretic Quantity

### 3.1 Transfer Entropy Formulation

The implicit-explicit boundary and its variable permeability are arguably the most explanatorily productive mechanism in the theory, underlying the accounts of psychedelic phenomenology, anosognosia, dreams, meditation, and hypnagogia (Gruber, 2026, Section 3.6). Formalizing permeability is therefore the highest-priority task.

Permeability asks how much of what happens below the threshold of consciousness shows up, a moment later, in what happens above it. Transfer entropy (Schreiber, 2000) turns that question into a number. It compares two predictions of the next value of a signal $Y$: one made from $Y$'s own present value alone, and one made from $Y$'s present value together with the present value of a second signal $X$. If knowing $X$ improves the prediction, information flows from $X$ to $Y$, and transfer entropy is the size of that improvement in bits, averaged over time:

$$T_{X \to Y} = \sum p(y_{t+1}, y_t, x_t)\, \log \frac{p(y_{t+1} \mid y_t, x_t)}{p(y_{t+1} \mid y_t)}$$

It is zero when $X$ adds nothing to the prediction of $Y$.

Applying it requires two signals. At each scope position $s$, split the modeling mass at the threshold $\nu_{\mathrm{crit}}$ into the part below it and the part above it:

$$A_s(t) = \int_0^{\nu_{\mathrm{crit}}} \rho(s, \nu, t)\, d\nu \qquad\qquad B_s(t) = \int_{\nu_{\mathrm{crit}}}^{1} \rho(s, \nu, t)\, d\nu$$

$A_s(t)$ is how much of the modeling at $s$ is currently implicit, and $B_s(t)$ how much is explicit. Each is a single number that changes over time, which is the form transfer entropy requires. **Permeability** at $s$ is the information flow from the first signal to the second:

$$P_{\text{implicit} \to \text{explicit}}(s, t) = T_{A_s \to B_s}(t)$$

Estimating $A_s$ and $B_s$ from neural data is a separate problem, and the cautions of §2.6 apply to it in full.

Permeability can be global (averaged over all $s$) or local (at a specific scope position $s$), which maps the theory's distinction between global permeability changes (psychedelics) and local permeability deficits (anosognosia).

### 3.2 Permeability Profiles as Quantitative Predictions

The theory's phenomenological claims become quantitative predictions about the permeability profile:

| State | Global P | Local P anomalies | Predicted measurement |
|---|---|---|---|
| Normal waking | Medium | None (selective gating) | Baseline transfer entropy |
| Psychedelic (psilocybin, LSD) | High | None (global increase) | Transfer entropy spike, broadband |
| Salvia divinorum (high dose) | High + ESM disruption | Self-scope P collapses | $T_{\mathrm{ISM} \to \mathrm{ESM}} \to 0$; $T_{\mathrm{IWM} \to \mathrm{ESM}}$ ↑ |
| Anosognosia (right hemisphere stroke) | Normal (most domains) | Low at damaged domain | Domain-specific transfer entropy deficit |
| Deep sleep (NREM) | Very low | Uniform suppression | Near-zero transfer entropy |
| REM dreaming | Medium | Internally driven (from W, not from s(t)) | T from parameters high; T from sensory input ≈ 0 |
| Meditation | Selectively elevated | Trained domain-specificity | Targeted transfer entropy increases |
| Pre-sleep / hypnagogia | Gradually increasing | Bottom-up (low-level → high-level) | Hierarchical onset of transfer entropy |

These predictions are directly testable with existing neuroimaging data — transfer entropy can be estimated from EEG, MEG, and fMRI time series (Vicente et al., 2011; Wibral et al., 2014).

### 3.3 The Gating Operator as a Family of Mechanisms

The parent paper (Gruber, 2026, Section 3.6) clarifies that permeability is not a single parameter but a **family of boundary properties** — in biological brains, modulated independently by serotonergic, GABAergic, dopaminergic, and other neuromodulatory systems across sensory channels, cortical regions, and histological contexts. The formalization must reflect this.

Define a **gating family** $G = \{g_c : W \times X \to [0, 1]^{N_c}\}$, indexed by channel c ∈ C, where C is the set of modulatory channels (e.g., serotonergic, GABAergic, dopaminergic, noradrenergic) and $N_c$ is the dimensionality of channel c's spatial resolution (region count, column count, or voxel count depending on the scale of analysis). The composite gating state is the element-wise product across channels:

$$g(W, x(t)) = \prod_{c \in C} g_c(W, x(t))$$

The substrate dynamics (Equation [1] of Section 4.1) become:

x(t+1) = f(x(t), s(t), g(W, x(t)) ⊙ W)

where ⊙ is element-wise multiplication. A single scalar "permeability" P emerges as a summary statistic — for example, the mean of g over spatial dimensions — but the fundamental quantity is the channel-indexed family.

This decomposition has empirical consequences. The theory predicts that:

- Serotonergic agonism (psilocybin, LSD) primarily increases $g_{\text{5-HT}}$ globally, producing the broadband entropy increase measured by Schartner et al. (2017) and interpreted as a global entropy elevation by the entropic brain hypothesis (Carhart-Harris et al., 2014), an account that arrives at the same signature from an independent starting point.
- GABAergic agonism (propofol, benzodiazepines) primarily decreases $g_{\text{GABA}}$ globally, suppressing the implicit-to-explicit transfer.
- Dopaminergic modulation primarily affects $g_{\text{DA}}$ in reward-related scope bands, altering the *content* of what crosses the boundary without necessarily changing the *total amount* of transfer.
- Stroke damage eliminates structural components of specific $g_{c}$ in specific spatial regions, producing the domain-specific permeability deficits observed in anosognosia.

The gating family depends on three classes of input:

- The substrate state x(t): attentional gating (top-down control of what becomes conscious), operating through all channels simultaneously.
- Neurotransmitter dynamics: pharmacological gating, with each neuromodulatory system operating through its own channel $g_{c}$.
- Structural integrity: lesion-dependent gating (stroke damage eliminates $g_{c}$ in specific pathways), affecting spatial resolution within specific channels.

This connects naturally to the criticality-rhythm relationship that the theory identifies as an open question (Gruber, 2026, Section 9).

### 3.4 The Fokker-Planck Dynamics

The dynamics of the model density ρ under variable permeability can be modeled as a Fokker-Planck equation on the model space:

∂ρ/∂t = −∇ · (v ρ) + D ∇²ρ + S(s, ν, t)

where:

- v(s, ν, t) is a drift field: deterministic migration of models along the scope-mode axes. Attention directs drift along ν (making implicit content explicit); context shifts direct drift along s (shifting between self-focused and world-focused processing).
- D is a diffusion coefficient: stochastic leakage across the implicit-explicit boundary — the baseline permeability noise that produces phenomena like visual snow and spontaneous phosphenes.
- S(s, ν, t) is a source/sink term: creation and destruction of models. Learning creates new implicit models (increases ρ below $\nu_{\mathrm{crit}}$); forgetting destroys them; sensory input injects new explicit models (increases ρ above $\nu_{\mathrm{crit}}$).

State transitions then have specific signatures:

- **Psychedelics**: Global increase in the drift velocity $v_{\nu}$ toward high ν.
- **Propofol**: Collapse of D and $v_{\nu}$ to zero, with an absorbing boundary at $\nu_{\mathrm{crit}}$.
- **Meditation**: Trained, selective control over v(s, ν, t) — the meditator learns to steer the drift field.
- **Sleep onset**: Gradual reduction of $v_{\nu}$ combined with increasing D (controlled drift toward implicitness, with increasing stochastic permeability producing hypnagogic imagery).

### 3.5 Total Conscious Content

The total conscious content at time t — a single scalar representing the "amount" of phenomenal modeling — is:

$$C(t) = \int_0^1 \int_{\nu_{\mathrm{crit}}}^{1} \rho(s, \nu, t)\, d\nu\, ds$$

This is directly analogous to what the Perturbational Complexity Index (PCI; Casali et al., 2013) and Lempel-Ziv complexity attempt to measure empirically. The formalization predicts that C(t) should correlate with PCI and similar complexity measures across consciousness states.

---

## 4. Criticality Operationalization

### 4.1 The Substrate as a Dynamical System

Define the full substrate state at time t as x(t) ∈ X ⊆ R^N, where N is the number of functional units. In the biological brain, these are cortical columns; in artificial substrates, they may be processing nodes, recurrent cells, or other computational units. The dynamics follow:

x(t+1) = f(x(t), s(t), W)

where s(t) is sensory input and W is the connectivity matrix (synaptic weights or, more generally, the coupling parameters of the substrate). The biological brain's instantiation of this dynamical system — the cortical automaton, a discrete system on a high-dimensional lattice (Gruber, 2015, 2026) — is the canonical example, but the formalization is substrate-neutral: any dynamical system satisfying the criticality and architectural constraints qualifies.

The implicit models are the *parameters* of this system:

- IWM = the world-knowledge partition of W.
- ISM = the self-knowledge partition of W.

The explicit models are *patterns of activity* — projections of the state vector:

- EWM(t) = $\Pi_{\mathrm{EWM}}$ · x(t)
- ESM(t) = $\Pi_{\mathrm{ESM}}$ · x(t)

where $\Pi_{\mathrm{EWM}}$ and $\Pi_{\mathrm{ESM}}$ are projection operators. This maps the real/virtual split directly: W (parameters, slow, structural) = real side; x(t) projected through $\Pi_{\mathrm{EWM}}$ and $\Pi_{\mathrm{ESM}}$ (states, fast, transient) = virtual side.

### 4.2 Three Candidate Criticality Measures

The theory specifies Wolfram Class 4 / edge of chaos as the criticality requirement (Gruber, 2015, 2026). Class 4 is defined for cellular automata, not for continuous, noisy, high-dimensional neural substrates. Three existing measures can operationalize the requirement:

**Branching ratio σ**: The average number of descendant activations per ancestor activation across neuronal avalanches (Beggs & Plenz, 2003; Shew & Plenz, 2013).

- σ < 1: subcritical (activity dies out) → Wolfram Class 1/2
- σ = 1: critical → Wolfram Class 4
- σ > 1: supercritical (activity explodes) → Wolfram Class 3

The ConCrit framework (Algom & Shriki, 2026) established that σ tracks consciousness across 140 datasets. The formalized claim is an **operating-regime hypothesis**, and is deliberately weaker than a requirement: **conscious processing is hypothesized to occupy σ ∈ [$\sigma_{\mathrm{low}}$, $\sigma_{\mathrm{high}}$]** where $\sigma_{\mathrm{low}}$ ≈ 0.95 and $\sigma_{\mathrm{high}}$ ≈ 1.1 (slightly subcritical to slightly supercritical, consistent with Priesemann et al., 2013, 2014). The band is an empirical generalization over the measured cases, not a derived threshold — the reasons it cannot presently be stated as a requirement are given in §4.4, and §4.7 further qualifies it by making criticality a regionally varying property rather than a single whole-substrate coordinate. A caution on the numbers themselves: nominal σ = 1 is a normalization convention rather than a substrate-independent edge, and in leaky recurrent substrates the dynamical edge of chaos can sit well away from it, so the band above should be read as calibrated to the neural recordings it was estimated from and re-estimated for any other substrate.

**Maximum Lyapunov exponent $\lambda_{\max}$**: For edge-of-chaos dynamics specifically (Bertschinger & Natschläger, 2004; Boedecker et al., 2012):

- $\lambda_{\max}$ < 0: ordered (stable attractors)
- $\lambda_{\max}$ ≈ 0: edge of chaos
- $\lambda_{\max}$ > 0: chaotic

**Detrended Fluctuation Analysis (DFA) exponent α**: Long-range temporal correlations in neural time series (Hardstone et al., 2012). α ≈ 1 indicates critical dynamics with scale-free temporal structure.

A further, model-free readout is the Fisher information metric of a control parameter, or of the observed branching ratio when the control parameter is unknown, whose peak width and height track proximity to criticality across branching, spiking and whole-brain models (Du et al., 2026).

### 4.3 Disambiguating Criticality Types

An important caveat: Kanders et al. (2017) demonstrated that avalanche criticality (σ ≈ 1) and edge-of-chaos criticality ($\lambda_{\max}$ ≈ 0) do not necessarily co-occur in neural networks. These are measuring *different* phase transitions. The theory's reference to "edge of chaos" via Wolfram's Class 4 aligns more naturally with the Lyapunov exponent than with the branching ratio, while the empirical criticality literature (ConCrit) focuses primarily on the branching ratio and avalanche statistics. In deterministic cellular automata, the damage-spreading transition — between a phase in which trajectories from different initial conditions coalesce quickly and one in which they stay different — contains directed percolation as the first level of an infinite hierarchy of renormalization-group fixed points (Nahum & Roy, 2026). Criticality in models inferred from recordings can also arise from the inference itself: as the number of neurons grows, inferred parameters concentrate near critical points without fine-tuning (Carcamo & Lynn, 2026).

The formalization must resolve this ambiguity. Three options:

1. **Both**: the operating regime is characterized by σ ≈ 1 AND $\lambda_{\max}$ ≈ 0 jointly. This is the most restrictive and potentially the most empirically productive — it implies that systems at avalanche criticality but not at edge-of-chaos, or the reverse, fall outside the regime the theory associates with consciousness.

2. **Avalanche criticality sufficient**: The branching ratio is the operative measure; edge-of-chaos is a correlate but not independently required. This aligns with the ConCrit literature.

3. **Edge-of-chaos is primary**: $\lambda_{\max}$ ≈ 0 is the operative coordinate (following Wolfram's framework most closely); avalanche criticality is a consequence. This aligns with the theoretical derivation in Gruber (2015).

These three are options for *which observable indexes the regime*, and they are stated at the level of the operating-regime hypothesis of §4.4 rather than as requirements on consciousness. Choosing among them is an empirical question about measurement, and none of the three is settled by the theory.

Empirical resolution: compare PCI (or another consciousness-tracking measure) against σ and $\lambda_{\max}$ independently, particularly in states where the two measures diverge.

### 4.4 Criticality: A Conjectured, Not Derived, Prerequisite

The parent theory treats operation near criticality (Wolfram Class 4 / edge of chaos) as a requirement for consciousness. It is tempting to try to *derive* this requirement from the theory's commitment to self-referential closure, via the chain

> self-referential closure ⇒ universal computation ⇒ Class-4 dynamics ⇒ criticality.

**I state plainly that this chain is a conjecture, not a proof.** It is offered as a research target — a structure that *would*, if established, upgrade criticality from an empirical correlate to a consequence — and it rests on two lemmas that are, at present, **open**:

- **Lemma L1 (closure ⇒ universality) — OPEN.** *Does self-referential closure (a system whose explicit self-model represents the dynamics that generate that very self-model) entail computational universality (the capacity to simulate an arbitrary program)?* This is **not** established. Self-representation of one's own dynamics is not known to be equivalent to Turing-universality; a system may faithfully model salient aspects of its own operation while being computationally weaker than a universal machine. No proof is known to the author, and the implication may well be false as stated. What can be said rigorously is only that deeper recursive self-modeling requires *more* computational resource (a monotonicity claim), not that it requires *universal* resource.

- **Lemma L2 (universality ⇒ criticality) — OPEN.** *Does computational universality require, or even imply, operation at or near a critical dynamical regime (Class 4 / edge of chaos)?* This is **not** established, and the standard results point the other way. (i) Wolfram's principle relating Class 4 to universality is itself a **conjecture** (the Principle of Computational Equivalence), not a theorem. (ii) Universality has been **proven only for specific rules** (Rule 110, Conway's Life), not for Class 4 as a class. (iii) Class-4 behavior is **not necessary** for universality — universal computation is realized by systems that are not naturally described as edge-of-chaos. (iv) Universality is a statement about what a system *can compute in principle*, whereas criticality is a statement about the *dynamical regime it occupies during operation*; the two are logically distinct, and one does not obviously entail the other. (v) The nearest existing formal handle is compression-based: Zenil (2010) conjectures, from elementary cellular automata, that universality implies a positive phase-transition coefficient — a nonzero sensitivity of a rule's compressed output to its initial condition. That conjecture is unproven, and it concerns sensitivity rather than criticality in the neural sense, but a proof of it would be the first result of L2's shape. For input-driven continuous-time reservoirs, Sugiura et al. (2025) prove that a neighborhood separation property is necessary and sufficient for universal approximation of input–output maps with polynomial readouts; Roig, Muñoz, and Morales (2026) extend the result to driven discrete-time reservoirs and find numerically, in benchmarks with linear readouts, that separability, prediction and representation geometry are optimized together in a narrow window of marginal driven stability. Sugiura et al. also prove that such a reservoir is discontinuous on a dense set of inputs (their Theorem 3), which they read as requiring chaotic dynamics. Physical noise caps the resolution of any physical reservoir (London et al., 2010; Hu et al., 2023), so the infinite resolution of Sugiura et al.'s Theorem 3 is out of reach in every dynamical regime, and in driven random networks the finite-resolution optimum lies where the input-driven dynamics are stable although the undriven network would be chaotic (Schuecker et al., 2018; Haruna & Nakajima, 2019). For reservoir forecasting, Du and Wang (2026) find that the spectral radius giving the best performance does not coincide with the Lyapunov edge of the reservoir. No theorem yet forces the maximal Lyapunov exponent to zero, and approximation universality is not computational (Turing) universality, so L2 remains open.

Accordingly, the criticality requirement in this theory should be read as an **empirically motivated operating-regime hypothesis** — well supported as a *correlation* by the consciousness-criticality literature (§4.2–4.3) — and the "deductive" chain above should be pursued as an open program: *if* L1 and L2 can each be proven (or given a precise restricted form under which they hold), *then* criticality follows; until then, it does not. A separate derivation route runs through coding optimality rather than closure: in a Gaussian population-coding model, maximizing Fisher information under resource constraints yields soft modes and diverging correlation lengths, and with spatial structure added unifies statistical and dynamical criticality (Xiao et al., 2026). Nothing else in the formalization depends on the derivation succeeding. The transfer-entropy permeability formalism (Section 3) and the criticality *observables* (§4.2–4.3) stand entirely on their own as empirical instruments, independent of whether L1 and L2 are ever closed.

### 4.5 The Two Thresholds as a Conjunction

The theory posits two thresholds — a criticality regime and a self-simulation architecture. Formally these combine as a **conjunction of independently-stated requirements**:

> Consciousness (of the human type) ⟹ [ criticality-observables in the near-critical band ] ∧ [ self-simulation architecture: significant modeling mass on both self and world, at both implicit and explicit levels ].

Both conditions are asserted to hold together, and each is independently motivated: a critical substrate without self-modeling (e.g., a sandpile at its critical point) has complex dynamics but no self-simulation; an architecture with the right model profile but driven below criticality (e.g., deep propofol anesthesia) retains the structural capacity but cannot instantiate the simulation.

**I explicitly do *not* claim that the first condition entails the second, nor the reverse.** The earlier draft asserted that the architectural threshold *entails* the criticality threshold "via the universal-computation bridge." That entailment is exactly the conjectured chain of §4.4, resting on the open lemmas L1 and L2. Until those lemmas are proven, the two thresholds are stated as **co-required but logically independent** — an empirically-motivated conjunction, not a derived implication. If L1 and L2 are later established, this conjunction can be strengthened to an entailment; that strengthening is a stated goal of the formalization program, not a present result.

### 4.6 The Implicit-Explicit Threshold as a Graph Phase Transition

The threshold $\nu_{\mathrm{crit}}$ — the ontological boundary between implicit and explicit modeling (Section 2.1) — may have a more specific mathematical characterization than a simple parameter value.

In Quantum Graphity (Konopka et al., 2008), spacetime emerges from a complete graph through a phase transition: at high energy, the graph is fully connected and symmetric; at low energy, it undergoes a transition to an ordered, low-dimensional, local structure. The transition is a graph phase transition characterized by abrupt changes in clustering coefficient, path length, and modularity.

If the consciousness-cosmology structural identity proposed by the companion cosmological model (Gruber, 2026c) is correct, then $\nu_{\mathrm{crit}}$ may literally be a graph phase transition in cortical functional connectivity: below $\nu_{\mathrm{crit}}$, processing is distributed, high-connectivity, and unstructured (implicit); above $\nu_{\mathrm{crit}}$, it is low-dimensional, structured, and local (explicit). This would make $\nu_{\mathrm{crit}}$ **empirically measurable** as the point at which graph-theoretic measures of EEG or fMRI functional connectivity undergo a structural transition — detectable without any prior commitment to what "consciousness" looks like in neural data.

This hypothesis is testable: track graph-theoretic measures (clustering coefficient, modularity, effective dimensionality) of cortical connectivity across consciousness transitions (sleep-wake, anesthesia induction/recovery, psychedelic onset). If $\nu_{\mathrm{crit}}$ corresponds to a graph phase transition, these measures should show a discontinuity at the consciousness threshold, independent of which neural measure is used as the graph's edge weights.

### 4.7 The Two Dimensions of Criticality: Extent and Complexity

Sections 4.2–4.6 treat criticality as a *single* coordinate: a substrate is sub-, at-, or super-critical, detected by one of three whole-recording scalars (σ, $\lambda_{\max}$, α). The parent theory, however, makes a claim that a single coordinate cannot express — that conscious processing varies along two dimensions that can move independently: **how much** of the substrate is engaged in near-critical (Class-4) dynamics, and **how rich** the dynamics on that engaged tissue are (Gruber, 2026, §3.7). Taken literally against a single critical point this is a category error: a homogeneous system at one critical point has one order parameter, one correlation length, one set of exponents, and "two independently variable dials off one point" cannot be constructed. This subsection gives the decomposition a formal basis by abandoning the single-point picture, and locates the two dials on genuinely distinct mathematical objects. The construction below is offered as the recommended formalization, not as a derived result; the independence claim it rests on is a conjecture (item 4).

**The heterogeneity premise.** Replace "one critical point" with a substrate that is a *field of locally-critical regions*. Partition the N functional units of §4.1 into local neighborhoods (cortical parcels, columns, or, in an artificial substrate, node blocks) i = 1..N, and estimate criticality *regionally*: each unit i carries a local branching ratio $\sigma_{i}$, a local edge-of-chaos exponent $\lambda_{\max}$,i, and/or a local DFA exponent $\alpha_{i}$. Define the local-criticality indicator

> $c_{i}$ = 1  if unit i is locally near-critical ($\sigma_{i}$ ∈ [$\sigma_{\mathrm{low}}$, $\sigma_{\mathrm{high}}$] and/or $\lambda_{\max}$,i ≈ 0),  else 0.

This is a real departure from §4.2, where σ and α are *whole-recording* estimates: the two-dimensional reading is only computable once σ/α are estimated per region and a spatial statistic is taken over {$c_{i}$}. Criticality becomes a spatially varying property, and two independent questions can be asked of the field — *how much* of it is critical, and *how complex* the critical dynamics are. Recorded criticality signatures vary regionally: in mouse visual cortex and hippocampus they change systematically along the anatomical hierarchy, and static and dynamic exponents order the regions in opposite directions (Cambrainha et al., 2026), so the marker chosen to define $c_{i}$ matters.

Estimating $c_{i}$ needs a surrogate that removes causal transmission while preserving each region's temporal structure, since the surrogate fixes the null hypothesis the local estimate is tested against (Theiler et al., 1992). A surrogate that permutes each unit's activity across the whole recording (a column or channel shuffle) keeps its rate but destroys its alignment with population-wide bursts; a near-critical substrate bursts population-wide, so this surrogate underestimates the null exactly there and can manufacture spurious local criticality. Window-jitter surrogates, which keep each unit's count within every time window and randomize timing only inside it (Amarasingham et al., 2012), preserve that alignment. The window width trades retained signal against retained confound, so the cut-off defining $c_{i}$ should be set on the separation between causal and non-causal reference data, not on the raw excess over the surrogate.

**Extent E (a spatial order parameter).** The first dial is a measure over *space*: which regions are in the Class-4 regime. In increasing strength:

> (a) fraction at criticality  $f_{\mathrm{crit}}$ = (1/N) $\Sigma_{i}$ $c_{i}$;
> (b) **giant-critical-cluster size** P∞ = |largest connected component of mutually-correlated critical units| / N;
> (c) correlation length over system size, ξ/L.

**P∞ (b) is the recommended order parameter.** Build the critical-connectivity graph on the units {i : $c_{i}$ = 1}, with an edge between two critical units when their activity correlation (or transfer entropy, §3.1) exceeds threshold; P∞ is then the normalized size of its giant component. This is exactly the percolation order parameter of a *spatial* phase transition (Stauffer & Aharony, 1994) and reuses the graph-phase-transition machinery already introduced in §4.6 (clustering, modularity, giant component) with little new apparatus — the single cheapest formal win. It is distinct from the temporal/avalanche critical point σ→1: $\sigma_{i}$ detects whether a *region* is critical at all; P∞ measures how far a single integrated critical process *reaches* across regions. The two can come apart: in a multi-agent model whose agents each run a reservoir, near-critical dynamics inside each agent do not produce collective critical avalanche statistics, which depend on the effective connectivity of the interaction network (Bessone & Plantec, 2026). P∞ makes the binding claim of §5.1 (maximal correlation length ⇒ substrate-spanning integration) the *same quantity* as extent: integration and extent are one order parameter, not two ideas.

**Complexity K (a dynamical measure).** The second dial is a property of the *dynamics within* the recruited critical region(s), not of space. Let $X_{G}$(t) be the activity restricted to the giant critical cluster G (the units counted by P∞). Define

> K = LZ($X_{G}$) — the Lempel-Ziv complexity (Lempel & Ziv, 1976) of the on-cluster activity, or equivalently its entropy rate / excess entropy — conditioned on criticality (evaluated only over G).

K measures the algorithmic richness of the computation the critical tissue performs. Perturbational complexity (PCI; Casali et al., 2013) and Lempel-Ziv complexity (LZc; Schartner et al., 2017) map onto K, **not** onto extent — the differentiation caveat of the main paper (Gruber, 2026, §3.7) is inherited here as a formal distinction. Note that K is *not* the total-content scalar C(t) of §3.5: C(t) integrates modeling mass over the whole density ρ, whereas K is the conditional complexity of the on-cluster trajectory. C(t) is a joint quantity (it rises when either dial rises); K isolates the dynamical dial. K does not by itself identify the regime: compressed length separates chaotic and complex cellular automata (Classes 3 and 4) from ordered ones, but not complex from chaotic (Zenil, 2010), so a high K is equally what a chaotic cluster would produce. K carries regime information only because it is evaluated on the critical cluster G — the conditioning on criticality does that work, and K measures richness within it. A compression measure normalized against sorted and shuffled surrogates, built as the product of distance from order and distance from disorder, peaks at the critical temperature of the 2D Ising model (Jacobus, 2026), and is a candidate independent check on the regime of G.

**Orthogonality (a conjecture, not a theorem).** E and K are defined on different mathematical objects — E is a measure over *space* (which regions are critical), K is a measure over *dynamics* (how rich the on-critical computation is) — so nothing forces them to co-vary. One can grow the critical cluster while each region computes something simple (E↑, K≈const), or hold a small cluster running an intricate computation (K↑, E≈const). The separating case that makes the distinction more than a definitional convenience is the **generalized tonic-clonic seizure**: near-maximal co-activation, but with the substrate driven out of the Class-4 regime. The *route* out is phase- and scale-dependent and is not settled — onset and spread are heterogeneous and often desynchronized at single-neuron scale, while hypersynchrony dominates the late phase and termination — so the case should be stated route-agnostically as exit from Class 4 rather than as a specific departure direction. What matters for the decomposition is only that the exit occurs: under the definitions above such a state has high $\Sigma_{i}$ activity yet a critical fraction near zero, so **E ≈ 0** — and the theory's prediction of unconsciousness follows from the extent dial collapsing, not from any drop in raw activity. This is the case in which co-activation and extent are *provably* different functionals (Σ activity vs. |{regions in Class-4}|), and it is what forces E to be defined as Class-4 spatial measure rather than co-activation. Their *independence* over the whole reachable state space, however, is asserted as an **empirical/formal conjecture to be tested** (regionally-resolved criticality mapping jointly with on-cluster LZ across states), not derived here.

**Relation to neural complexity $C_{N}$.** The closest formal precedent is Tononi–Sporns–Edelman neural complexity (Tononi, Sporns, & Edelman, 1994),

$$C_N(X) = \sum_{k=1}^{n} \Big[ \tfrac{k}{n} H(X) - \big\langle H(X_k^j \mid X - X_k^j) \big\rangle_j \Big],$$

which collapses *integration* and *differentiation* into a single scalar that is maximized exactly when the system is simultaneously integrated (high whole-system entropy) and differentiated (subsets near-independent). Integrated information Φ (Tononi, 2004) is a later single-scalar in the same spirit; Barrett et al. (2026) note that Φ is not well defined for real physical systems and has not been computed on one, and propose replacing it with a suite of quantities that characterize states of consciousness in several dimensions. A 2-D plane adds formal content beyond $C_{N}$, instead of re-spreading one optimized scalar over two axes, **iff** the axes are independently measurable *and* independently manipulable, which is why E and K are placed on distinct structures (spatial percolation measure vs. on-cluster dynamical measure). $C_{N}$ assumes a single substrate-wide optimum; the two-dials claim asserts a *frontier* on which one dial is high while the other is low, with the joint corner (both maximal) reachable only rarely. That is a strictly stronger, more falsifiable structure than $C_{N}$ — but only under the distinct-objects definitions above; a Φ- or $C_{\mathrm{N-flavored}}$ quantity would *not* cleanly separate the seizure (its failure is local Class-4 loss, not global irreducibility), which is the diagnostic that the two-axis reading is not a renaming. For this reason Φ is **not** adopted as the extent index (it conflates integration and differentiation and would double-count K); extent is the percolation/fraction/ξ measure, and $C_N$/Φ are cited as measures of the *joint corner*, not of extent alone.

**Processing volume and subjective duration.** A time-dilation claim follows from the two-dials structure — that driving *both* dials high together produces extreme subjective time-dilation, unifying near-death "life-review" reports and high-dose salvia phenomenology. It should be attributed carefully: the parent paper does not state this prediction, and treats subjective temporality instead through its temporal-echo mechanism (Gruber, 2026, Section 3.4.4), where the constructed "now" is one frame of the recursive self-simulation running on a clock whose speed varies with the organism's situation. The extension below is developed here, and it requires a definition of "processing volume," which the verbal statement leaves undefined. Using the total-conscious-content scalar of §3.5, define

$$\text{processing-volume}(\Delta t) := \int_{\Delta t} C(t)\, dt, \qquad \text{subjective duration} \propto \int_{\Delta t} C(t)\, dt,$$

i.e. experienced duration scales with the *quantity of self-simulation processing completed per unit physical time*, the physical clock-second entering only because the substrate runs at a finite rate. This ties the prediction to existing apparatus and makes the joint corner quantitative: both dials up ⇒ more of the substrate computing richer dynamics ⇒ higher C(t) ⇒ larger $\int C(t)\, dt$ over a fixed physical interval ⇒ dilation. The proportionality constant is a calibration parameter, not derived; the claim earns only a *monotone* functional form (dilation increases with accumulated processing), and its falsifier is genuine — dilation reported with high complexity but ordinary extent ($\int C\, dt$ not elevated) would refute the processing-volume account. This time-dilation *law* is roadmap-grade, not main-paper-grade; the main paper does not state it.

**Where this leaves the two dials.** With E = P∞ (percolation extent), K = on-cluster LZ (dynamical complexity), the seizure as the separating negative control, $C_{N}$ engaged as prior art, and processing-volume $:= \int C(t)\, dt$ tying time-dilation to §3.5, the two-dials decomposition moves from a verbal assertion to a defensible formal structure whose one open conjecture, the independence of E and K, awaits empirical test. The full program — regional σ/α estimation protocols, conditional-LZ estimators on the recruited cluster, and a joint E–K reachability map — is Phase-2 formal work (§8).

---

## 5. ESM Redirection Dynamics

### 5.1 The ESM as an Input-Dependent Attractor

The theory's most distinctive prediction — that ego dissolution content is controllable via sensory input (Gruber, 2026, Prediction 2, Section 8.3) — requires a formal account of how the ESM latches onto alternative inputs when normal self-referential input is disrupted.

Model the ESM-relevant region of the model density as a dynamical subsystem whose attractor landscape depends on its inputs. Let e(t) represent the aggregate ESM state (the integral of ρ over the self-scope, above-$\nu_{\mathrm{crit}}$ region). Under normal conditions:

e(t+1) = h(e(t), $i_{\mathrm{self}}$(t))

where $i_{\mathrm{self}}$(t) is the normal self-referential input (interoceptive, proprioceptive). The ESM has a stable attractor basin around the "normal self" configuration.

During ego dissolution (high-dose psychedelic, salvia divinorum), $i_{\mathrm{self}}$ is disrupted:

e(t+1) = h(e(t), α · $i_{\mathrm{self}}$(t) + (1 − α) · $i_{\mathrm{ext}}$(t))

where α → 0 as dose increases and $i_{\mathrm{ext}}$(t) is the dominant external input. The ESM's attractor basin reshapes around whatever $i_{\mathrm{ext}}$ dominates. This is the formal mechanism underlying the salvia phenomenology described in Gruber (2026, Section 6.1): users "become" objects in their environment because the ESM latches onto the strongest available sensory input.

### 5.2 Quantitative Predictions

The mutual information between the ESM state and its inputs provides the quantitative measure:

- I(e; $i_{\mathrm{self}}$): How much the ESM state correlates with self-referential input.
- I(e; $i_{\mathrm{ext}}$): How much the ESM state correlates with external sensory input.

The theory predicts:

- Normal waking: I(e; $i_{\mathrm{self}}$) >> I(e; $i_{\mathrm{ext}}$). The ESM is driven primarily by self-referential input.
- Low-dose psychedelic: I(e; $i_{\mathrm{self}}$) decreases; I(e; $i_{\mathrm{ext}}$) begins to increase.
- High-dose (ego dissolution): I(e; $i_{\mathrm{self}}$) → 0; I(e; $i_{\mathrm{ext}}$) → $I_{\max}$. The ESM identity tracks the dominant external input.
- Controllability prediction: In a controlled sensory environment during ego dissolution, I(e; $i_{\mathrm{ext}}$) should track experimentally manipulated sensory input — visual, auditory, or proprioceptive — in a predictable, dose-dependent manner.

This is testable in principle with fMRI: measure the correlation between default mode network activity (proxy for ESM) and controlled sensory input versus interoceptive input across dose levels.

### 5.3 The Density Migration Account

In the model-space framework, ESM redirection corresponds to a specific density migration: ρ at the self-scope (s ≈ 0), explicit (ν > $\nu_{\mathrm{crit}}$) corner migrates toward the world-scope (s → 1) region while remaining above $\nu_{\mathrm{crit}}$. The system still runs an explicit simulation — consciousness is preserved — but the simulation's content shifts from self-dominated to world-dominated. Ego dissolution is not ESM abolition but ESM re-sourcing.

This density migration should be measurable as a shift in representational content within the networks that sustain explicit processing (default mode network shifting toward content typically associated with sensory processing networks), detectable via representational similarity analysis (RSA) of fMRI data during controlled psychedelic administration.

---

## 6. Self-Referential Closure

### 6.1 Closure and the Hard Problem

The theory's central philosophical claim — that self-referential closure is what makes the simulation phenomenal — carries the weight of the Hard Problem dissolution (Gruber, 2026, Section 3.4). A weather simulation models weather but does not model itself modeling weather; therefore it has an "outside" from which it can be fully described. A self-referential simulation at criticality has no such outside — the simulation *is* its own observer, and observation-from-inside is what the theory identifies as experience.

This argument needs formal grounding. Three mathematical approaches are proposed:

### 6.2 The Observability Constraint

The parent paper (Gruber, 2026, Section 3.4.3) introduces an **observability constraint** that is architecturally constitutive, not merely epistemic: the ESM's observational horizon is bounded by the EWM. The explicit self-model cannot see with useful resolution beyond the explicit world model to the implicit substrate that generates it.

Formally, define the **observable set** of the ESM as $O_{\mathrm{ESM}}$ — the set of states, properties, and processes that the ESM can represent within its self-simulation. Define the **simulation scope** $S_{\mathrm{EWM}}$ as the set of states, properties, and processes that the EWM actively models. The observability constraint is:

$O_{\mathrm{ESM}}$ ⊆ $S_{\mathrm{EWM}}$

The ESM can only model aspects of the system that are already represented within the explicit simulation. It cannot "reach through" the virtual level to directly represent substrate-level processes (implicit model parameters, synaptic weights, neurotransmitter concentrations) unless those processes have first been transferred across the implicit-explicit boundary via the permeability mechanism (Section 3).

This constraint has three formal consequences:

1. **The Meta-Problem becomes deductive.** The system's inability to explain its own phenomenality is not a contingent limitation but a structural consequence of $O_{\mathrm{ESM}}$ ⊆ $S_{\mathrm{EWM}}$. The mechanisms generating the simulation (implicit models, substrate dynamics) are outside $S_{\mathrm{EWM}}$ and therefore outside $O_{\mathrm{ESM}}$. The ESM's attempt to model the basis of its own experience encounters a principled opacity — formalized as the complement $S_{\mathrm{EWM}}$^c being inaccessible to the ESM's representational capacity.

2. **The Hard Problem's formulation presupposes a violation.** The Hard Problem asks: "Given a complete physical description, why is there experience?" This presupposes that a system can have complete access to its own substrate — that $O_{\mathrm{ESM}}$ could encompass the full physical description. The observability constraint says this is architecturally impossible for self-referentially closed systems. The "explanatory gap" is the gap between $S_{\mathrm{EWM}}$ and the full substrate state space X.

3. **Permeability modulates the constraint's boundary.** When permeability increases (psychedelics, meditation), previously implicit processes enter $S_{\mathrm{EWM}}$, expanding $O_{\mathrm{ESM}}$. This is why psychedelic states produce the subjective sense of "seeing behind the curtain" — the observability boundary temporarily shifts, exposing processing stages that are normally outside $S_{\mathrm{EWM}}$. The formalization predicts that the *content* of psychedelic insight should correspond to processes at the implicit-explicit boundary, not to arbitrary substrate-level processes.

In the model-space framework, the observability constraint becomes: the ESM (ρ at s ≈ 0, ν > $\nu_{\mathrm{crit}}$) can only represent properties of ρ that are themselves above $\nu_{\mathrm{crit}}$. Substrate-level properties (ν < $\nu_{\mathrm{crit}}$) are invisible to the ESM unless transferred upward through the gating family G (Section 3.3).

### 6.3 Self-Referential Depth via Recursive Representation

Define a representation map $\mu_{n}$ that encodes how a subsystem models another at recursion depth n:

$\mu_{n}$: $X_{\mathrm{ESM}}$ → M($X_{\mathrm{ESM}}$^(n-1))

where M denotes "models of" and the superscript denotes recursion level. The graduated levels of consciousness (Gruber, 2015, 2026) then formalize as:

| Level | Recursion depth | Description |
|---|---|---|
| Basic consciousness | μ₀ | ESM represents the EWM |
| Simply extended | μ₁ | ESM represents itself representing the EWM |
| Doubly extended | μ₂ | ESM represents itself representing itself representing the EWM |
| Triply extended | μ₃ | Third-order recursion; Meta-Problem arises here |

The **self-knowledge measure** quantifies how well the system predicts its own next state:

R = 1 − H(e(t+1) | ê(t+1)) / H(e(t+1))

where ê(t+1) is the system's *own prediction* of its next ESM state. R = 1 means perfect self-prediction; R = 0 means no self-knowledge.

### 6.4 Self-Referential Closure as a Fixed Point

The most compact formalization: consciousness occurs when the ESM reaches a **fixed point** of self-representation. Define a map Ψ: M → M where Ψ(m) is "the model of m." Self-referential closure occurs when:

Ψ(m\*) = m\*

The symbol is Ψ and not Φ, which denotes integrated information (Tononi, 2004; §4.7): Ψ is a map between models, not a scalar quantity of integration, and no relationship between the two is asserted here.

The self-model models itself — the model and the modeled coincide. This is a well-defined mathematical object (a fixed point of a self-referential map), related to Lawvere's fixed-point theorem (Lawvere, 1969) and Kauffman's self-referential forms (Kauffman, 1987).

The theory's claim that "the simulation *is* the thing being simulated" (Gruber, 2026, Section 3.4) is precisely this fixed-point condition. At a fixed point of self-representation, there is no remainder — no "outside view" from which the process can be fully described without participating in it.

The critical connection to the Hard Problem dissolution: the category error identified by the theory (seeking phenomenality at the substrate level) becomes formally precise at the fixed-point level. The phenomenal properties exist at m\*, not at the substrate level that computes Ψ. The function Ψ runs on the substrate; the fixed point m\* is a property of the dynamics, not of any particular substrate element.

### 6.5 Complexity Cost of Self-Reference

Self-referential modeling has a computational overhead. For a system to achieve recursion depth n, its total complexity must satisfy:

$$C_{\text{total}} \ge \sum_{k=0}^{n} C_k + \text{overhead}(n)$$

where $C_{k}$ is the complexity required for level-k representation and the overhead grows with depth. This explains why triply-extended consciousness requires a large, complex substrate (human-scale cortex) while simpler organisms support only basic consciousness — they lack the computational overhead for deeper recursion. It also provides a formal account of why the six-layer neocortex exceeds the three-layer minimum for universal function approximation (Cybenko, 1989): the additional layers provide the overhead needed for recursive self-simulation (Gruber, 2015). Recurrence can substitute running time for depth: a single ReLU recurrent network with fixed weights and fixed hidden dimension uniformly approximates every continuous function on [−1, 1] if run long enough, and minimax lower bounds show the runtime cannot be avoided (Abadie et al., 2026).

### 6.6 Self-Referential Closure as a Renormalization Group Fixed Point

A fourth approach to formalizing self-referential closure comes from an unexpected direction: quantum field theory. Wetterich (2022a, 2022b) demonstrated that reversible cellular automata are exactly equivalent to discretized fermionic quantum field theories — the probabilistic description of a classical automaton *is* quantum mechanics. If the cortical automaton (Section 4.1) has such a QFT dual, then the self-representation map Ψ: M → M (Section 6.4) acquires a natural interpretation within the renormalization group (RG) framework.

In QFT, an RG fixed point is a configuration where the system looks the same at every scale of description — the dynamics are scale-invariant, the fixed point is an attractor of the RG flow, and only a finite number of "relevant directions" (parameters) govern the system's behavior near the fixed point (Wilson & Kogut, 1974). The self-referential closure condition Ψ(m\*) = m\* has precisely these properties: at the fixed point, the model and the modeled coincide (scale-invariance — the self-description is identical at every level of recursion), the system naturally evolves toward the fixed point (it is an attractor of the self-modeling dynamics), and only the relevant parameters of the self-model matter (the system ignores irrelevant substrate details).

This suggests a specific formalization: the self-representation map Ψ operates on the space of effective theories at different "scales" of self-description (analogous to the RG flow operating on coupling constants at different energy scales). The ESM at self-referential closure is the RG fixed point of this flow — the point where further refinement of the self-model no longer changes it. The "no outside view" property of Section 6.1 then becomes: at an RG fixed point, the system cannot distinguish between descriptions at different scales, because all scales give the same description. There is no "more fundamental" level from which the fixed point could be analyzed — it is self-contained.

This connection is promising because RG fixed points are well-studied mathematical objects with extensive machinery for analysis: critical exponents characterize the universality class, the number of relevant directions determines the predictive power, and the basin of attraction determines which initial conditions lead to the fixed point. If Ψ(m\*) = m\* can be rigorously identified as an RG fixed point, the full apparatus of Wilson's renormalization group becomes available for consciousness theory — including quantitative predictions about how perturbations from the fixed point (altered states, lesions, pharmacological interventions) affect the self-model.

The connection to the companion cosmology (Gruber, 2026c) is direct: the cosmological fixed point Ψ(U) = U (the universe computes its own structure) and the consciousness fixed point Ψ(m\*) = m\* (the self-model models itself) would be the same mathematical object — an RG fixed point — at different scales. This is the consciousness-cosmology structural identity expressed in the language of renormalization.

---

## 7. Category-Theoretic Architecture

### 7.1 Two Categories

Category theory provides the most natural language for the theory's architectural claims because it is designed to formalize structural relationships between mathematical objects (Mac Lane, 1998; Tsuchiya, Taguchi, & Saigo, 2016).

Define two categories:

- **Sub** (Substrate): Objects are substrate states (W, x(t)). Morphisms are physical dynamics — the state transitions described by the dynamical system equations.
- **Sim** (Simulation): Objects are virtual-model states (EWM(t), ESM(t), or equivalently, the above-$\nu_{\mathrm{crit}}$ portion of ρ). Morphisms are experiential transitions — phenomenal changes.

### 7.2 The Consciousness Functor

Consciousness is a **functor** F: Sub → Sim that maps substrate dynamics to simulation dynamics while preserving compositional structure:

- F maps physical state transitions to experiential transitions.
- F preserves composition: if substrate state A transitions to B and B to C, the experiential transition A→C is the composition of the experiential transitions A→B and B→C.

The real/virtual split is the distinction between the domain category (Sub) and the codomain category (Sim). The Hard Problem dissolution becomes: seeking phenomenal properties in Sub is a category error because phenomenal properties exist in Sim. The functor F *generates* Sim from Sub, but Sim has properties (qualia, unity, selfhood) that do not exist as properties of Sub — just as the image of a functor can have properties not present in the domain.

### 7.3 Permeability as a Natural Transformation

Variable permeability can be formalized as a **natural transformation** η: $F_{\mathrm{normal}}$ ⇒ $F_{\mathrm{altered}}$ between different consciousness functors. Under psychedelics, the functor changes — more substrate structure maps into the simulation — but the structural relationships are preserved (content appears in hierarchical order, V1 → V2/V3 → higher areas, not as random noise). The natural transformation ensures this structural preservation.

Smithe's (2024) structured active inference framework, which formalizes active inference using categorical systems theory and treats interfaces as compositional abstractions of Markov blankets, provides a directly applicable technical foundation. The FMT's implicit-explicit boundary could be modeled as a structured interface in this sense — a compositional boundary through which information flows, with the gating function g specifying the interface's permeability properties.

### 7.4 Forking as Coproduct

The theory's virtual model forking — the mechanism underlying dissociative identity disorder (Gruber, 2026, Section 6.2) — formalizes as a **coproduct** in the Sim category. A single substrate object in Sub maps to multiple simulation objects in Sim:

F(x(t)) = $\mathrm{ESM}_{1}$(t) ⊔ $\mathrm{ESM}_{2}$(t) ⊔ ... ⊔ $\mathrm{ESM}_{n}$(t)

where ⊔ is the coproduct (disjoint union). This captures the claim that DID involves a single substrate running multiple ESM configurations, each constituting a distinct experiential self, with only one active at any given time.

---

## 8. Phased Build Order

The formalization project is substantial. A pragmatic build sequence, ordered by empirical accessibility and mathematical difficulty:

### Phase 1: Highest Priority (Directly Testable with Existing Data)

**Module 3.2 — Permeability as transfer entropy**: Compute transfer entropy between neural signals in known "implicit" processing regions and known "explicit"/"conscious access" regions across existing neuroimaging datasets from psychedelic, anesthesia, sleep, and meditation studies. Test the permeability profile predictions (Table 1) quantitatively. This requires no new mathematical development — transfer entropy estimation is well-established (Wibral et al., 2014).

**Module 4 — Criticality threshold mapping**: The branching ratio σ and Lyapunov exponent $\lambda_{\max}$ are already measured in the ConCrit literature (Algom & Shriki, 2026; Hengen & Shew, 2025). Map FMT's predictions onto existing datasets. Attempt to disambiguate avalanche criticality from edge-of-chaos criticality in consciousness contexts (Section 4.3).

### Phase 2: Core Formalism (Requires Dedicated Mathematical Work)

**Module 2 — Continuous model space**: Define the model density function ρ(s, ν, t) rigorously. Specify how to estimate ρ from neuroimaging data using representational similarity analysis (RSA), encoding models, and dimensionality reduction techniques (ICA, NMF). Build a minimal computational model (recurrent spiking network) and estimate ρ from its activity. Include the cautions of Section 2.6 (emergent dimensionality and discretization artifacts) and the principal bundle connection of Section 2.5.

**Module 5 — ESM redirection**: Formalize the attractor-switching mechanism. Build a minimal computational model with a self-model unit and demonstrate input-dependent identity switching under perturbation. Generate quantitative predictions for the salvia divinorum controlled-input experiment (Gruber, 2026, Prediction 2, Section 8.3).

**Module 7 — Category-theoretic architecture**: The functor construction. Recent work on emergence from discrete substrates in physics — particularly Levin and Wen's (2005) string-net condensation and Wetterich's (2022a, 2022b) automaton-QFT equivalences — shows that the same categorical structures proposed here (functors, natural transformations, coproducts) appear independently as the canonical mathematical framework for formalizing emergence. This elevates Module 7 from an elegant option to a likely necessity: the categorical framework may be required to ensure that the other modules cohere. Collaboration with a category theorist who has consciousness theory exposure (cf. Tsuchiya et al., 2016; Smithe, 2024) is recommended. Module 7 was originally placed in Phase 3; it is elevated here because the categorical framework should inform the construction of Modules 2 and 5, not be retrofitted after they are built.

### Phase 3: Deep Formalism (Hardest, Highest Potential Impact)

**Module 6 — Self-referential closure**: The fixed-point formalization. This requires working at the intersection of dynamical systems theory, mathematical logic, and — given the RG fixed-point connection (Section 6.6) — quantum field theory. The connection to Lawvere's fixed-point theorem and to renormalization group fixed points needs rigorous development. Investigate whether the fixed-point condition can be shown to formally entail properties that correspond to the "no outside view" argument, and whether the RG framework provides quantitative predictions about perturbations from the fixed point.

### Phase 4: Computational Validation

The formalization specifies quantities and dynamics; Phase 4 demonstrates that they produce the predicted behavioral signatures in a concrete computational system. Computational validation along these lines is under way in a companion programme and will be reported separately. The specification below does not depend on those results, and is offered here without them: what Phase 4 can settle is whether the formalized quantities behave as the framework says they should.

**Implementation: Survival gridworld with architectural ablation.** A survival environment (hazards, resources, observable agent deaths) provides a natural testbed because observational learning — extracting causal structure from watching another agent die — requires exactly the ESM-projection mechanism the formalization specifies (Section 5). The FMT agent implements:

- **Four-model architecture**: IWM/ISM as learned substrate weights, EWM/ESM as running processes
- **Gating family G** (Section 3.3): Multiple modulatory channels, not a single permeability knob
- **Reservoir computing substrate** with tunable spectral radius for criticality (Section 4.4): edge-of-chaos dynamics as the regime in which the substrate has the open-ended computational *capability* the architecture needs. Local homeostatic plasticity is an alternative to tuning a global parameter: it drives deep networks from sub- and supercritical starts toward a common critical state with a vanishing largest finite-time Lyapunov exponent (Vock & Meisel, 2026)
- **Observability constraint** (Section 6.2): ESM bounded by EWM — the agent cannot know more about itself than its world model permits
- **Self-referential loop**: ESM models the system generating the ESM (recursive depth ≥ 2)

**Architectural ablation as the critical test.** Comparison architectures (flat RL, world-model-only, FMT-minus-ESM) provide controlled ablations. The formalization generates three sharp predictions:

1. **ESM ablation produces a graded, capacity-relative behavioral cost** — a measurable loss in sample efficiency on tasks requiring causal-structure extraction, widening with task horizon and with the richness of the model the intact agent can redeploy (Section 5). **The prediction is graded for a theoretical reason.** A finite closed loop run over a finite horizon can be unrolled into a feedforward computation with memory, so on a deterministic, episode-stationary task there is no capability a closed architecture has and its unrolled equivalent lacks; a clean binary loop-cut test cannot exist on such a task, and the framework's own commitments forbid predicting one. What survives the unrolling argument is a *price*: the unrolled equivalent must actually be built and paid for, and its cost grows with the horizon it must cover, so the licensed claim is an efficiency advantage within a budget. The falsifier is correspondingly a *magnitude* — an ablated agent matching the intact one in sample efficiency at equal capacity and matched task performance would refute the claim, whereas an ablated agent that merely takes longer would not.
2. **Sub-critical spectral radius degrades self-referential processing** — as the substrate is driven below the near-critical band, the open-ended computational capability the self-model draws on falls away, and observational learning should degrade correspondingly (Section 4.4). The claim is a price: no architecture is asserted to be incapable of the task, and the prediction is about how steeply performance falls with the capability, measured against matched controls at equal capacity.
3. **EWM coverage ablation degrades ESM proportionally** — reducing what the world model represents should directly limit what the self-model can represent about itself (Section 6.2, observability constraint).

**Ablation-validity audit: a precondition on reading any of these results.** Prediction 1 operationalizes ablation as the removal of a mechanism, and on a recurrent substrate that operationalization can silently fail: ablations on recurrent substrates can relocate rather than remove a loop, in which case the manipulation contrasts *closure here* against *closure there* rather than closure against its absence, and a tie between conditions is the predicted observation rather than a negative result. Any ablation protocol must therefore verify removal rather than assume it — for example by connectivity analysis of both arms, decomposing the effective connectivity of each into strongly-connected components and reporting the counts, and by checking explicitly that the mechanism the ablation was intended to remove has not reconstituted elsewhere in the remaining tissue. This audit is a requirement on the Phase 4 protocol and must be completed **before** the outcome measures are read, not after a null. Where an ablation cannot be shown to remove rather than relocate, the manipulation is properly described as *efferent disconnection of one region*, and the prediction it tests is correspondingly narrower. If these predictions hold, they demonstrate that the formalized framework's mathematical structure captures genuine computational distinctions. If they fail, they identify which formal commitments are wrong. Either outcome advances the theory.

**Framing constraint**: The gridworld validates architectural claims, not consciousness claims. It can demonstrate that FMT-architecture agents produce qualitatively different behavioral signatures; it cannot demonstrate that either architecture constitutes consciousness.

---

## 9. Scope and Limits

### 9.1 Contributions

**Constraint**: Verbal descriptions are flexible enough to accommodate post-hoc explanations. The Fokker-Planck dynamics, the transfer entropy measures, and the attractor-switching model commit to specific functional forms that can be empirically wrong.

**Quantitative predictions**: "Permeability increases under psychedelics" becomes "Transfer entropy from implicit to explicit regions increases by factor k at dose d" — a claim falsifiable with a number.

**Simulation**: A formalized theory can be implemented in code. Predictions can be tested computationally before committing to expensive neuroimaging experiments.

**Interoperability**: The transfer entropy measure connects to Predictive Processing's information-theoretic tools. The branching ratio connects to ConCrit. The category-theoretic framework connects to Smithe's structured active inference. Formalization turns FMT from an isolated framework into something interoperable with the rest of the field.

**Sharpened dissolution**: The fixed-point formalization either succeeds or fails. If self-referential closure can be made rigorous — if the fixed-point condition can be formally shown to entail properties corresponding to inside/outside asymmetry — that is a philosophical result in its own right.

**Bridge to physics**: The mathematical structures this formalization program requires — functors between categories, fixed points of self-referential maps, phase transitions in graph connectivity, renormalization group flows — are independently the canonical tools for formalizing emergence from discrete substrates in fundamental physics. Wetterich's (2022a, 2022b) automaton-QFT equivalences use functorial mappings; Levin and Wen's (2005) string-net condensation uses tensor category theory; Quantum Graphity (Konopka et al., 2008) uses graph phase transitions. The companion cosmological model (Gruber, 2026c) proposes a structural identity: consciousness and the universe instantiate the same computational architecture at different scales. If so, the FMT formalization and the physics of discrete emergence describe the same mathematical structures, and progress on either informs the other.

### 9.2 Limits

The formalization does not derive phenomenality from mathematics.

The model-space approach introduces a further limitation: the model density ρ(s, ν, t) is a statistical description of something that may not be cleanly decomposable. The brain may not implement "models" in any separable sense — the activity patterns we decompose via ICA or NMF may be artifacts of our decomposition method rather than natural kinds. The formalization should therefore be understood as a measurement framework that makes the theory testable, not as a claim that the brain literally implements a model density function.

---

## 10. Conclusion

The Four-Model Theory requires mathematical formalization to constrain its claims, generate quantitative predictions, and interface with the existing formal landscape of consciousness science. The correct formalization strategy must respect the theory's own commitment: the four canonical models are a minimum sufficient set, not an exhaustive enumeration. The biological substrate implements an uncountable ecology of models, and the formalization must be statistical rather than enumerative.

The continuous model-space framework — with scope and mode as continuous axes, the virtual/non-virtual split as a threshold on the mode axis, and the Fokker-Planck equation governing the density dynamics — provides the necessary mathematical language. Combined with transfer entropy for permeability, established criticality measures, attractor dynamics for ESM redirection, fixed-point theory for self-referential closure (including the observability constraint of Section 6.2 and the renormalization group connection of Section 6.6), and a graph-theoretic characterization of the implicit-explicit threshold (Section 4.6), the framework generates quantitative predictions that are testable with existing neuroimaging methods and computational models.

The formalization project is substantial but modular. Phase 1 (transfer entropy estimation and criticality mapping) can proceed immediately with existing tools and data. Phase 2 now includes the category-theoretic architecture alongside the model-space and ESM modules, reflecting the recognition that the categorical framework is not an optional formalism but the canonical mathematical language for emergence from discrete substrates. Phase 3 (self-referential closure) gains new tools from the RG fixed-point connection. Phase 4 (computational validation) provides the ultimate demonstration that the formalized theory's dynamics behave as predicted.

This paper specifies the formal framework; computational validation is under way in a companion programme and will be reported separately. The remaining formal modules (Phases 2-3) require mathematically trained collaborators. Some of these formalizations may show the theory to be wrong in specific, identifiable ways.

---

## References

Aaronson, S. (2014, May 21). Why I am not an integrated information theorist (or, The unconscious expander). *Shtetl-Optimized*. https://scottaaronson.blog/?p=1799

Abadie, V., Hutter, C., & Bölcskei, H. (2026). Recurrent neural networks approximate continuous functions. *arXiv*. https://doi.org/10.48550/arXiv.2606.20325

Albantakis, L., Barbosa, L., Findlay, G., Grasso, M., Haun, A. M., Marshall, W., Mayner, W. G. P., Zaeemzadeh, A., Boly, M., Juel, B. E., Sasai, S., Fujii, K., David, I., Hendren, J., Lang, J. P., & Tononi, G. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms. *PLOS Computational Biology*, 19(10), e1011465. https://doi.org/10.1371/journal.pcbi.1011465

Algom, S., & Shriki, O. (2026). The ConCrit framework: Critical brain dynamics as a unifying mechanism for consciousness theories. *Neuroscience & Biobehavioral Reviews*.

Amarasingham, A., Harrison, M. T., Hatsopoulos, N. G., & Geman, S. (2012). Conditional modeling and the jitter method of spike resampling. *Journal of Neurophysiology*, 107(2), 517–531. https://doi.org/10.1152/jn.00633.2011

Baars, B. J. (1988). *A Cognitive Theory of Consciousness*. Cambridge University Press.

Barrett, A. B., Milinkovic, B., Mediano, P. A. M., Rosas, F. E., Bor, D., Barnett, L., & Seth, A. K. (2026). Integrated information theory: The good, the bad and the misunderstood. *arXiv*. https://doi.org/10.48550/arXiv.2604.11482

Beggs, J. M., & Plenz, D. (2003). Neuronal avalanches in neocortical circuits. *Journal of Neuroscience*, 23(35), 11167–11177.

Bertschinger, N., & Natschläger, T. (2004). Real-time computation at the edge of chaos in recurrent neural networks. *Neural Computation*, 16(7), 1413–1436.

Bessone, N., & Plantec, E. (2026). Emergent macro-criticality from micro-critical agents. *arXiv*. https://doi.org/10.48550/arXiv.2605.01818

Bhalla, U. S. (2014). Molecular computation in neurons: a modeling perspective. *Current Opinion in Neurobiology*, 25, 31–37.

Bhatt, D. H., Zhang, S., & Gan, W.-B. (2009). Dendritic spine dynamics. *Annual Review of Physiology*, 71, 261–282. https://doi.org/10.1146/annurev.physiol.010908.163140

Boedecker, J., Obst, O., Lizier, J. T., Mayer, N. M., & Asada, M. (2012). Information processing in echo state networks at the edge of chaos. *Theory in Biosciences*, 131(3), 205–213.

Cambrainha, G. G., Castro, D. M., Gollo, L. L., Carelli, P. V., & Copelli, M. (2026). Hierarchical organization of critical brain dynamics. *arXiv*. https://doi.org/10.48550/arXiv.2604.21832

Carcamo, D. P., & Lynn, C. W. (2026). Emergence of criticality in models of real neurons. *arXiv*. https://doi.org/10.48550/arXiv.2609.09438

Carhart-Harris, R. L., et al. (2014). The entropic brain: a theory of conscious states informed by neuroimaging research with psychedelic drugs. *Frontiers in Human Neuroscience*, 8, 20.

Casali, A. G., et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. *Science Translational Medicine*, 5(198), 198ra105.

Cybenko, G. (1989). Approximation by superpositions of a sigmoidal function. *Mathematics of Control, Signals and Systems*, 2(4), 303–314.

Dehaene, S., & Changeux, J. P. (2011). Experimental and theoretical approaches to conscious processing. *Neuron*, 70(2), 200–227.

Du, Y., Liardi, A., Rajpal, H., & Jensen, H. J. (2026). Fisher information metric as a model-free measure of proximity to criticality in neural systems. *arXiv*. https://doi.org/10.48550/arXiv.2609.07624

Du, Y., & Wang, X. (2026). Beyond the edge of chaos: Stability–expressivity transfer in reservoir forecasting. *arXiv*. https://doi.org/10.48550/arXiv.2607.17909

Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138.

Gruber, M. (2015). *Die Emergenz des Bewusstseins*. Self-published.

Gruber, M. (2026). The Four-Model Theory of Consciousness: A Simulation-Based Framework Unifying the Hard Problem, Binding, and Altered States. *Zenodo* preprint. https://doi.org/10.5281/zenodo.18669891

Gruber, M. (2026c). Emergent spacetime from self-referential computation: A hierarchical cellular automaton framework. *Zenodo* preprint. https://doi.org/10.5281/zenodo.20294692

Hardstone, R., et al. (2012). Detrended fluctuation analysis: a scale-free view on neuronal oscillations. *Frontiers in Physiology*, 3, 450.

Haruna, T., & Nakajima, K. (2019). Optimal short-term memory before the edge of chaos in driven random recurrent networks. *Physical Review E*, *100*(6), 062312. https://doi.org/10.1103/PhysRevE.100.062312

Hengen, K. B., & Shew, W. L. (2025). Is criticality a unified setpoint of brain function? *Neuron*. https://doi.org/10.1016/j.neuron.2025.05.020

Hu, F., Angelatos, G., Khan, S. A., Vives, M., Türeci, E., Bello, L., Rowlands, G. E., Ribeill, G. J., & Türeci, H. E. (2023). Tackling sampling noise in physical systems for machine learning applications: Fundamental limits and eigentasks. *Physical Review X*, *13*(4), 041020. https://doi.org/10.1103/PhysRevX.13.041020

Jacobus, C. (2026). Finding the edge of chaos in a ferromagnet: Quantifying the "complexity" of 2D Ising phase transitions with image compression. *arXiv*. https://doi.org/10.48550/arXiv.2602.15185

Kanders, K., Lorimer, T., & Stoop, R. (2017). Avalanche and edge-of-chaos criticality do not necessarily co-occur in neural networks. *Chaos*, 27(4), 047408.

Kauffman, L. H. (1987). Self-reference and recursive forms. *Journal of Social and Biological Structures*, 10(1), 53–72. https://doi.org/10.1016/0140-1750(87)90034-0

Konopka, T., Markopoulou, F., & Smolin, L. (2008). Quantum Graphity: A model of emergent locality. *Physical Review D*, 77(10), 104029.

Lawvere, F. W. (1969). Diagonal arguments and Cartesian closed categories. *Lecture Notes in Mathematics*, 92, 134–145.

Lempel, A., & Ziv, J. (1976). On the complexity of finite sequences. *IEEE Transactions on Information Theory*, 22(1), 75–81.

Levin, M. A., & Wen, X.-G. (2005). String-net condensation: A physical mechanism for topological phases. *Physical Review B*, 71(4), 045110.

London, M., Roth, A., Beeren, L., Häusser, M., & Latham, P. E. (2010). Sensitivity to perturbations in vivo implies high noise and suggests rate coding in cortex. *Nature*, *466*(7302), 123–127. https://doi.org/10.1038/nature09086

Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer.

Nahum, A., & Roy, S. (2026). The damage spreading transition: A hierarchy of renormalization group fixed points. *arXiv*. https://doi.org/10.48550/arXiv.2603.22439

Nielsen, H. B., & Ninomiya, M. (1981). Absence of neutrinos on a lattice: (I). Proof by homotopy theory. *Nuclear Physics B*, 185(1), 20–40.

Oizumi, M., Lim, C., & Kanai, R. (2025). Principal bundle geometry of qualia: Understanding the quality of consciousness from symmetry. *PsyArXiv*. https://osf.io/agupq

Priesemann, V., et al. (2013). Neuronal avalanches differ from wakefulness to deep sleep — evidence from intracranial depth recordings in humans. *PLOS Computational Biology*, 9(3), e1002985.

Priesemann, V., et al. (2014). Spike avalanches in vivo suggest a driven, slightly subcritical brain state. *Frontiers in Systems Neuroscience*, 8, 108.

Roig, A., Muñoz, M. A., & Morales, G. B. (2026). Driven criticality links universal computation and optimal representations. *arXiv*. https://doi.org/10.48550/arXiv.2607.21232

Schartner, M. M., et al. (2017). Increased spontaneous MEG signal diversity for psychoactive doses of ketamine, LSD and psilocybin. *Scientific Reports*, 7, 46421.

Schreiber, T. (2000). Measuring information transfer. *Physical Review Letters*, 85(2), 461–464.

Schuecker, J., Goedeke, S., & Helias, M. (2018). Optimal sequence memory in driven random networks. *Physical Review X*, *8*(4), 041029. https://doi.org/10.1103/PhysRevX.8.041029

Seth, A. K. (2021). *Being You: A New Science of Consciousness*. Dutton.

Shew, W. L., & Plenz, D. (2013). The functional benefits of criticality in the cortex. *The Neuroscientist*, 19(1), 88–100.

St Clere Smithe, T. (2024). Structured active inference (extended abstract). *arXiv*. https://doi.org/10.48550/arXiv.2406.07577

Stauffer, D., & Aharony, A. (1994). *Introduction to Percolation Theory* (Rev. 2nd ed.). Taylor & Francis.

Sugiura, S., Ariizumi, R., Asai, T., & Azuma, S. (2025). Necessary and sufficient reservoir condition for universal reservoir computing. *Mathematics*, 13(21), 3440. https://doi.org/10.3390/math13213440

Theiler, J., Eubank, S., Longtin, A., Galdrikian, B., & Farmer, J. D. (1992). Testing for nonlinearity in time series: The method of surrogate data. *Physica D: Nonlinear Phenomena*, 58(1–4), 77–94. https://doi.org/10.1016/0167-2789(92)90102-S

Tononi, G., Sporns, O., & Edelman, G. M. (1994). A measure for brain complexity: relating functional segregation and integration in the nervous system. *Proceedings of the National Academy of Sciences*, 91(11), 5033–5037.

Tononi, G. (2004). An information integration theory of consciousness. *BMC Neuroscience*, 5, 42.

Tsuchiya, N., Taguchi, S., & Saigo, H. (2016). Using category theory to assess the relationship between consciousness and integrated information theory. *Neuroscience Research*, 107, 1–7.

Vicente, R., Wibral, M., Lindner, M., & Pipa, G. (2011). Transfer entropy — a model-free measure of effective connectivity for the neurosciences. *Journal of Computational Neuroscience*, 30(1), 45–67.

Vock, S., & Meisel, C. (2026). Adaptive self-organized criticality in deep neural networks. *arXiv*. https://doi.org/10.48550/arXiv.2608.28431

Wibral, M., et al. (2014). *Directed Information Measures in Neuroscience*. Springer.

Wetterich, C. (2022a). Fermion picture for cellular automata. *arXiv preprint*, arXiv:2203.14081.

Wetterich, C. (2022b). Fermionic quantum field theories as probabilistic cellular automata. *Physical Review D*, 105(7), 074502.

Wilson, K. G., & Kogut, J. (1974). The renormalization group and the ε expansion. *Physics Reports*, 12(2), 75–199.

Wolfram, S. (2002). *A New Kind of Science*. Wolfram Media.

Xiao, H., Zhao, X., Zhou, H., & Wang, W. (2026). Efficient coding under constraint drives neural systems towards criticality and sloppiness. *arXiv*. https://doi.org/10.48550/arXiv.2605.22598

Zenil, H. (2010). Compression-based investigation of the dynamical properties of cellular automata and other systems. *Complex Systems*, 19(1), 1–28. https://doi.org/10.25088/complexsystems.19.1.1
