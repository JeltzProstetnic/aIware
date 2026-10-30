# Toward a Mathematical Formalization of the Four-Model Theory: A Recommended Approach

**Matthias Gruber**

*Independent researcher*

*ORCID: 0009-0005-9697-1665*

*Correspondence: research@matthiasgruber.com*

---

## Abstract

The Four-Model Theory of Consciousness (FMT; Gruber, 2015, 2026) proposes that consciousness is constituted by real-time self-simulation across four model kinds — Implicit World Model (IWM), Implicit Self Model (ISM), Explicit World Model (EWM), and Explicit Self Model (ESM) — arranged along two axes, mode (an orthogonal contrast) and scope (a nesting in the normal mode of operation: ESM ⊆ EWM, ISM ⊆ IWM), and running on free modeling, whose usual signature in cortex is edge-of-chaos dynamics. The theory currently operates in natural language. This paper outlines a recommended mathematical formalization strategy. The four model kinds are understood as the *minimum set of model kinds the architecture forces*, not an exhaustive enumeration: the biological substrate — built from spiking neurons atop proteomic networks with their own intracellular learning — implements an effectively uncountable number of overlapping models on both sides of the implicit/explicit divide. The formalization therefore treats models as a continuous density over a model space rather than as discrete, countable objects, with the virtual/non-virtual split as the one hard ontological boundary. Six formalization modules are proposed: (1) a continuous model-space framework replacing the discrete 2×2 taxonomy, formalizing the multiple-generator architecture, (2) permeability as a family of channel-specific information-theoretic selection mechanisms, (3) criticality as a signature hypothesis, empirically motivated, not a requirement on consciousness, and a consequence of self-referential closure only if two open lemmas are proven, (4) ESM redirection dynamics, (5) self-referential closure as the mutual update of the active self and world models, with the observability constraint ($O_{\mathrm{ESM}}$ ⊆ $S_{\mathrm{EWM}}$), and (6) category-theoretic architecture. A phased build order prioritizes empirically testable components. The formalization is offered as a research program specification for mathematically trained collaborators; verification of the formal apparatus is explicitly deferred to domain experts.

**Keywords**: consciousness, formalization, four-model theory, model space, criticality, transfer entropy, self-referential closure, observability constraint, information geometry

---

## 1. Introduction

### 1.1 The Formalization Gap

The Four-Model Theory (Gruber, 2015, 2026) addresses all eight canonical requirements for a theory of consciousness — the Hard Problem, the Explanatory Gap, the Boundary Problem, the Structure of Experience, Unity and Binding, Combination and Emergence, the Causal Role, and the Meta-Problem — within a single framework built on three principles (Gruber, 2026, Section 3): open-ended computation allows free modelling, near-criticality being the signature that property leaves in neural tissue rather than the requirement itself; recurrent non-linear dynamics of sufficient complexity host a second computational level; and phenomenology is real and physical, and is that level's modelling closed on itself, an identity rather than a law connecting two things (Gruber, 2026, Section 3). The four model kinds, redirection of the modelling resource onto the non-self, variable implicit-explicit permeability and forking of the self-model are not among the principles: they follow as consequences with explanatory power (Gruber, 2026, Section 6.0). This matters for what follows, because a formalization that axiomatized the consequences would be formalizing the wrong objects.

The theory is currently stated entirely in natural language. Its rivals carry notation: Integrated Information Theory (IIT; Tononi, 2004; Albantakis et al., 2023) has Φ and the qualia space formalism, Predictive Processing (PP; Friston, 2010; Seth, 2021) has the free energy principle and active inference, and Global Neuronal Workspace (GNW; Baars, 1988; Dehaene & Changeux, 2011) has computational broadcasting models. The Four-Model Theory has verbal descriptions: "permeability increases," "ESM redirects," "criticality threshold."

Notation alone does not make a theory testable. Φ is fully specified yet has never been computed for a real brain and is provably intractable for realistic systems (Aaronson, 2014); what makes a theory testable is functional forms that can turn out wrong and quantities that can be measured and found not to behave as claimed.

By that standard FMT's gap is specific. Its mechanisms are stated so that almost no observation could embarrass them: "permeability increases" names a direction without a magnitude, a functional form or a measurement procedure, so it accommodates any entropy result after the fact. Each verbal mechanism therefore needs a functional form that data can contradict.

### 1.2 Why Not Simply Formalize the Four Models?

The obvious approach — assigning a mathematical object to each of the four models and formalizing their interactions — would be premature and would misrepresent the theory's own commitments.

The four model kinds (IWM, ISM, EWM, ESM) are a *principled lower bound*, not an architectural specification. They represent the minimum configuration the architecture requires for any consciousness: a system must model both the world and itself, and must do so at both the structural/implicit and the dynamic/explicit level. This is a constraint on the *minimum*, not a claim about the *actual*.

The biological substrate — spiking neurons atop proteomic networks, with intracellular signaling pathways constituting their own learning and computational intelligence even within a single cell (Bhalla, 2014), and with structural plasticity operating on the same neurons at the level of dendritic spines (Bhatt et al., 2009) — implements an effectively uncountable number of overlapping models on both sides of the implicit/explicit divide. A motor model of reaching for a cup simultaneously encodes world-geometry (cup location, obstacle positions) and self-kinematics (arm configuration, grip aperture). An emotional model of a social interaction simultaneously encodes other-knowledge (world) and self-assessment (self). The boundaries between "models" are not sharp and their number is not well-defined in a neural architecture.

To formalize the theory correctly, therefore, requires treating the four models as four *corners* of an abstract scope-mode space, neighbourhoods in a coordinate system of modeling activity and not regions of tissue — the canonical extrema around which the actual, high-dimensional modeling ecology of the brain is organized. The formalization must be statistical, not enumerative.

### 1.3 Scope and Limitations

This paper specifies a formalization research program. It proposes mathematical frameworks, defines quantities, and outlines a build order. It does *not* verify the mathematical apparatus — the author is not a mathematician, and formal verification is explicitly deferred to domain experts. The equations presented here are intended as precise specifications of *what needs to be formalized* and *which mathematical tools are appropriate*, not as proven theorems.

The paper develops, in turn, the continuous model-space framework with its multiple-generator interpretation of the model density; permeability as a family of channel-specific selection mechanisms; criticality, framed as a signature of free modeling whose derivation from self-referential closure rests on two open lemmas, and its operationalization; the ESM redirection mechanism; self-referential closure as the mutual update of the active self and world models, with the observability constraint ($O_{\mathrm{ESM}}$ ⊆ $S_{\mathrm{EWM}}$); and a category-theoretic architecture. Section 8 proposes a phased build order and Section 9 identifies what formalization would and would not deliver.

---

## 2. From Discrete Models to a Continuous Model Space

### 2.1 The Model Space

Instead of four enumerable models, define a **model space** M — a high-dimensional manifold whose points are the distinct models the substrate carries. A point of M is a model in the parent theory's sense (Gruber, 2026, Section 3.1): a state or structure M related to a target domain T by a mapping that preserves the relations the system acts on, with two criteria. Write access: M updates so that it follows T. Readability: the system can evaluate M; a structure the system cannot evaluate is a data structure, not a model. T fixes the model's boundary, so boundary recognition is a consequence, not a third criterion. That a model is actually read is required for consciousness, not for being a model. An explicit model is recurring activity meeting both criteria; it may recur after gaps rather than persist through consecutive windows, and an arbitrary direction of the state vector is not a model. Explicit models are generated from the implicit models and current input rather than stored. Each model m ∈ M has two primary properties:

- **Scope** s(m) ∈ [0, 1]: the extent of the model's target, from the self alone (0) to everything the system models, the self included (1).
- **Mode** ν(m) ∈ [0, 1]: a continuous axis from fully implicit/structural (0) to fully explicit (1).

Scope is a nesting, not a contrast: a self model's target is a proper part of the world model's, which is the ESM ⊆ EWM, ISM ⊆ IWM of the parent theory. Nesting is the normal mode of operation and is representational, not a claim that the two share neural locations; the parent theory names hedged exceptions in which the self model has nothing to latch onto or is overwhelmed or damaged (Gruber, 2026, Section 3.2). The explicit world model is therefore the whole explicit stratum, EWM(t) := {m : ν(m) > $\nu_{\mathrm{crit}}$}, the explicit self model is its self-scope part, and the world model with which the self model closes is the remainder EWM∖ESM, all explicit modeling of what is not the self (§6.4). Intermediate s is blending: a motor reaching model encodes both world-geometry and body-kinematics at once. s is assigned by a model's target, not by the source of its momentary content: the self model's target is the system itself whatever input currently fills it, so it stays at s ≈ 0 when its content is drawn from the world. The mode axis captures the theory's claim that the implicit-explicit boundary is graded, not binary (Gruber, 2026, Section 3.6) — while maintaining that there exists a threshold $\nu_{\mathrm{crit}}$ above which modeling activity is explicit (virtual); it is phenomenal where it also enters the closed loop of §6.4.

The four canonical model kinds are the **poles** of this 2D projection:

- IWM-pole (s = 1, ν = 0): stored knowledge of everything, fully implicit.
- ISM-pole (s = 0, ν = 0): stored self-knowledge, fully implicit.
- EWM-pole (s = 1, ν = 1): explicit modeling of everything the system models, fully explicit; the closure partner EWM∖ESM is the explicit stratum outside $N_{\mathrm{ESM}}$, a set of models, not a pole.
- ESM-pole (s = 0, ν = 1): explicit self-modeling, fully explicit.

But the actual substrate populates the *entire* [0, 1]² space with a density of models. Nothing in this space is a location in the brain: implicit models are stored in structure and can be localized, explicit models are distributed activity and cannot (Gruber, 2026, Section 3.2).

### 2.2 The Model Density Function

Define a **model density** ρ(s, ν, t) over the scope-mode space at time t. The quantity ρ(s, ν, t) ds dν represents the "amount of modeling activity" in the region [s, s+ds] × [ν, ν+dν] at time t, which below $\nu_{\mathrm{crit}}$ is substrate processing through stored models and above $\nu_{\mathrm{crit}}$ is generated explicit activity. This is a measure-theoretic quantity, analogous to a probability density but not normalized to 1 — the total modeling activity of the brain can vary across states (more total modeling during waking than during deep sleep). ρ is a finite measure on [0, 1]²; on a finite substrate it is a finite sum of overlapping components, and the density representation is adopted for its invariance to how one counts, not because the number of models is infinite.

The model density function formalizes the theory's commitment to a **multiple-generator architecture** (Gruber, 2026): the conscious substrate is a continuous ecology of overlapping modeling processes. Patchwork models at every scale — from molecular-level proteomic computation through cortical-column processing to whole-brain simulation — contribute to ρ simultaneously. The four canonical models are the extremal peaks of this density; the space between them is densely populated with blended models that are simultaneously about-self-and-about-world to varying degrees. Any biological-type implementation supports a continuous density of modeling activity; the formalization adopts the density representation for generality, not as a further necessity condition.

The virtual/non-virtual split — the one hard ontological claim of the theory — becomes a threshold on the mode axis:

- Virtual (explicit): ν > $\nu_{\mathrm{crit}}$
- Real (substrate): ν < $\nu_{\mathrm{crit}}$

Everything above $\nu_{\mathrm{crit}}$ is part of the running simulation, and is conscious where it enters the self-model's closed loop. Everything below it operates "in the dark." The theory claims $\nu_{\mathrm{crit}}$ is an ontological boundary, though its value must be determined empirically.

The gradedness of the boundary is a property of the *mode coordinate* ν, which varies continuously and on which modeling activity is distributed continuously; the hardness is a property of the *ontological predicate* defined on it. A continuous variable can carry a sharp threshold without ceasing to be continuous — the temperature of water is continuous while the liquid-vapour phase boundary is not — and the claim here is of that form. The gradedness is a fact about the substrate's organization; the hardness is a fact about which side of the boundary a given activity falls on. §4.6 proposes that the threshold may itself be a graph phase transition, which if correct would supply the physical mechanism that makes a sharp boundary on a continuous axis possible.

### 2.3 The Minimum-Configuration Constraint

The theory's claim about the four canonical models becomes a density constraint rather than a discrete architectural specification:

**For any consciousness, ρ must have significant mass near all four extremal points in (s, ν) space.**

Formally, define four neighbourhoods $N_{\mathrm{IWM}}$, $N_{\mathrm{ISM}}$, $N_{\mathrm{EWM}}$, $N_{\mathrm{ESM}}$ of the four corners of the abstract scope-mode space, not of a network, and require:

$$\int_{N_k} \rho(s, \nu, t)\, ds\, d\nu > \theta_k \quad \text{for each } k \in \{\mathrm{IWM}, \mathrm{ISM}, \mathrm{EWM}, \mathrm{ESM}\}$$

where $\theta_{k}$ are minimum-mass thresholds, lowest at the floor of minimal consciousness. Under the nesting, $\theta_{\mathrm{EWM}}$ bounds the explicit mass outside $N_{\mathrm{ESM}}$, $\int_{\nu > \nu_{\mathrm{crit}}} \rho - \int_{N_{\mathrm{ESM}}} \rho > \theta_{\mathrm{EWM}}$, the closure partner EWM∖ESM. $N_{\mathrm{ESM}}$ is defined by target and integration, a model of the system itself or at least the viewpoint to which the senses are referred (Gruber, 2026, Section 3.4.3), not by its s-coordinate alone; whether that mass is in closure is the separate condition $\chi_{\mathrm{act}} > 0$ of §3.5. A system with mass only near (s = 1, ν = 1) — world-simulation without self-simulation — would not be conscious. A system with mass only below $\nu_{\mathrm{crit}}$ — implicit processing without explicit simulation — would not be conscious. Mass at the ESM corner is necessary; mass there outside closure is preconscious. The four-model requirement is a constraint on the density profile, not a count of discrete objects.

This formulation accommodates the effectively uncountable models of the biological brain while preserving the theory's principled claim that the four model kinds are the minimum set the architecture forces, not an exhaustive enumeration.

"A system with mass only near (s = 1, ν = 1) would not be conscious" is **definitional rather than empirical**: the parent theory defines consciousness as self-simulation, so the constraint restates that definition in measurable terms, and the $\theta_{k}$ thresholds are its empirical content.

### 2.4 The Hierarchical Depth Axis

The model density function should be extended to account for the five-system hierarchy (Gruber, 2015, 2026):

ρ(s, ν, ℓ, t) for ν < $\nu_{\mathrm{crit}}$, with ρ(s, ν, t) unchanged above the threshold,

where ℓ ∈ {1, 2, 3, 4} indexes the depth of the implicit side:

1. Physical system (atoms, molecules)
2. Electrochemical system (ion gradients, action potentials)
3. Proteomic system (receptor configurations, protein expression, intracellular signaling)
4. Topological system (synaptic connectivity, circuit architecture)

The fifth level of the hierarchy, the virtual system of real-time dynamical patterns, is the stratum ν > $\nu_{\mathrm{crit}}$ and needs no separate index. The proteomic layer (ℓ = 3) is particularly relevant: receptor configurations encode prediction models about neurotransmitter dynamics, protein expression patterns constitute a slow, molecular-scale computational intelligence operating on timescales of minutes to days (Bhalla, 2014), alongside structural remodeling of dendritic spines on a comparable timescale (Bhatt et al., 2009). These are implicit models in their own right, but at a level below the topological/synaptic level at which the standard four-model description operates.

The real/virtual split remains clean — it is a threshold on ν — but the implicit side has stratified depth, with models within models within models, all the way down to proteomic computation. The four-model description is the top-level statistical summary, analogous to describing a fluid by temperature and pressure when the underlying molecular dynamics are vastly more complex.

### 2.5 Connection to Principal Bundle Geometry

Recent work by Oizumi, Lim, and Kanai (2025) provides a complementary mathematical framework for characterizing qualia structure using principal bundle geometry. Their approach formalizes how symmetry groups G acting on sensory inputs induce a decomposition of neural representation space into orbits (qualia attributes — rigid, universal across individuals) and a quotient space (qualia signatures — plastic, shaped by learning). This rigid/plastic duality parallels the present framework's implicit/explicit distinction: orbit structure is inherited from physical symmetries (analogous to substrate-level constraints), while quotient geometry is learned (analogous to simulation-level content).

The principal bundle framework applies most naturally to the explicit side of the model space (ν > $\nu_{\mathrm{crit}}$), where it formalizes the *geometry* of explicit content within the EWM. The equivariant encoder f: X → Y in their framework maps onto the generation of the explicit model from the implicit one: the IWM stores the encoder's parameters (learned world-knowledge); the EWM is the running representation (the encoder's output). Under equivariance, the explicit model preserves the symmetry structure of the world — formalized as f(g·x) = π(g)·f(x), where π denotes the group representation. (Oizumi et al. write this representation as ρ; it is renamed here because ρ is reserved throughout this paper for the model density.)

Two extensions are required to integrate this framework with FMT's formalization:

1. **Self-referential systems.** Oizumi et al.'s framework assumes feed-forward equivariant encoders. FMT requires self-referential closure — the ESM models the system generating the ESM. Extending principal bundles to recurrent, self-referential systems may require gauge bundle theory with connections, where the gauge connection encodes how self-referential feedback transforms the fiber structure.

2. **Altered states.** The principal bundle framework characterizes normal perceptual processing. Under psychedelic conditions (increased implicit-explicit permeability), equivariance should be disrupted — measurable via Oizumi et al.'s proposed G-empirical equivariance deviation (G-EED) metric. The formalization predicts that ego dissolution should collapse the semidirect product structure of multi-attribute qualia, a testable prediction jointly generated by both frameworks. It is a prediction of this formalization, not one of Gruber (2026, §8).

The compositionality results (direct and semidirect group products for independent and hierarchically entangled attributes) are relevant to FMT's account of binding as an emergent property of the dynamics (Section 5.1 of the parent paper): the EWM's unified scene is a composite principal bundle whose product structure formalizes how features from different cortical areas are integrated.

### 2.6 Cautions on Model-Space Estimation

Two methodological cautions apply to any empirical estimation of the model density ρ:

**Emergent dimensionality.** The 2D projection (scope × mode) is a principled simplification. The effective dimensionality of the model space may itself be emergent — determined by the critical regime of the substrate rather than imposed a priori. Background-independent models of emergent spacetime (Konopka, Markopoulou, & Smolin, 2008) demonstrate that dimensionality can arise from phase transitions in graph connectivity. If an analogous mechanism operates in cortical networks, the number of independent axes in the model space is a quantity to be *measured*, not assumed, with the caveat that the decomposition method fixes part of what it returns, the metric and the number of dimensions among it (Gruber, 2026, Section 7.3). The scope-mode framework should be understood as capturing the dominant structure near the critical point; additional dimensions may become relevant in altered states or non-human substrates.

**Discretization artifacts.** In discrete physics, the Nielsen-Ninomiya theorem (Nielsen & Ninomiya, 1981) proves that discretizing a continuous field inevitably produces spurious extra modes — the "fermion doubling" problem. An analogous effect may occur when estimating the continuous model density from discrete neural data: decomposition methods (ICA, NMF, RSA) may produce apparent "models" that are artifacts of the discretization rather than genuine modeling activity. Any implementation must state its criteria in advance, and correlation with behaviour, stimulus or report is not enough: any rotation of a content-carrying subspace correlates too, and fixed wiring guarantees stable shared directions that carry no content. A candidate mode counts as a model when it meets the write criterion of §2.1 against a time-shifted null with the input area's activity as a covariate, when the claim survives random rotations within the same subspace or the basis is fixed before the data are seen, when drifting targets are scored against a fold-mean baseline, and when the mode is readable by the system (evaluable; in a spiking substrate, that its members project outside the pattern). The same nulls govern the transfer-entropy and closure statistics below.

### 2.7 Locating the Engine: The Modality-Flatness Criterion

The formalization above specifies *what* the model space is without saying *where*, in a given substrate, the machinery that generates explicit models sits. The theory has so far answered that architecturally rather than locatably: an architectural characterization tells you what to look for, not where to point the instrument.

A candidate localization criterion follows from the free-modelling requirement itself. Modality-specific machinery is, by construction, specialized: the capacity it devotes to modelling is concentrated in the modality it serves, and falls away outside it. The machinery that performs *free* modelling has no such attachment — its defining property is that its modelling capacity can be pointed anywhere. **The engine should therefore be identifiable as the region whose distribution of free modelling capacity across sensory and motor modalities is flattest**, with modality-specialized structures showing sharply peaked distributions over the same measure.

This is offered as a **method rather than as a prediction**. As stated it is an identification procedure: it either succeeds in locating a region or it does not, and a failure to find a flat-distribution region is uninformative on its own, since it may equally indicate an inadequate capacity measure. A falsifiable form exists, that disrupting the flattest-distribution region abolishes explicit modelling while modality-specific processing survives, and it becomes a prediction once a free-modelling capacity measure has been validated independently of the localization it serves. The parent theory supplies a candidate: a novel-input probe, in which an unrolled feedforward model of matched capacity, trained on the system's own history, is compared with the system on novel input of increasing compositional depth, criticality signatures recorded alongside and not as the test (Gruber, 2026, Table 1b). It is a design, not yet a validated measure, so the criterion stays a method until the probe has been run. In behaviour, free modelling shows as activity without an immediate payoff, play its clearest form (Gruber, 2026, Section 6.4); that is a marker, not a criterion, and its absence establishes nothing.

Two practical notes for anyone implementing it. First, the measure must be *capacity for* modelling rather than observed modelling activity, since a region idle at the moment of measurement is not thereby unspecialized. Second, the criterion is scale-sensitive in the same way as any localization statistic: a flatness score computed on a substrate too small to support differentiated modality-specific structure has nothing to discriminate, and will report flatness everywhere. Localization results should therefore state the substrate scale and the pass rate of whatever gate defines a positive, rather than reporting the best-scoring region as though it were a detection.

---

## 3. Permeability as an Information-Theoretic Quantity

### 3.1 Transfer Entropy Formulation

The implicit-explicit boundary and its variable permeability are arguably the most explanatorily productive mechanism in the theory, underlying the accounts of psychedelic phenomenology, anosognosia, dreams, meditation, and hypnagogia (Gruber, 2026, Sections 3.6, 6.3). Formalizing permeability is therefore the highest-priority task.

Permeability asks how much of what happens below the implicit–explicit threshold shows up, a moment later, in what happens above it. Transfer entropy (Schreiber, 2000) turns that question into a number. It compares two predictions of the next value of a signal $Y$: one made from $Y$'s own present value alone, and one made from $Y$'s present value together with the present value of a second signal $X$. If knowing $X$ improves the prediction, information flows from $X$ to $Y$, and transfer entropy is the size of that improvement in bits, averaged over time:

$$T_{X \to Y} = \sum p(y_{t+1}, y_t, x_t)\, \log \frac{p(y_{t+1} \mid y_t, x_t)}{p(y_{t+1} \mid y_t)}$$

It is zero when $X$ adds nothing to the prediction of $Y$. Schreiber's quantity is an average over a stationary record; a permeability that changes with state needs the windowed form $T^{(\tau)}_{X \to Y}(t)$, the transfer entropy estimated over $[t - \tau, t]$, or the local transfer entropy of Lizier, Prokopenko and Zomaya (2008) averaged over that window.

Applying it requires two signals. At each scope position $s$, split the modeling mass at the threshold $\nu_{\mathrm{crit}}$ into the part below it and the part above it:

$$A_s(t) = \int_0^{\nu_{\mathrm{crit}}} \rho(s, \nu, t)\, d\nu \qquad\qquad B_s(t) = \int_{\nu_{\mathrm{crit}}}^{1} \rho(s, \nu, t)\, d\nu$$

$A_s(t)$ is how much of the modeling at $s$ is currently implicit: substrate processing through the stored models, estimated from the activity outside the explicit subspaces (§4.1) and not from the weights W, which carry no time series at recording scale (x, W, ι and Equation [1] are defined in §4.1). $B_s(t)$ is how much is explicit. Each is a single number that changes over time, which is the form transfer entropy requires. **Permeability** from scope $s$ to scope $s'$ is the windowed information flow from the implicit signal at $s$ to the explicit signal at $s'$, conditioned on the sensory input ι(t) of Equation [1]:

$$P(s \to s', t) = T^{(\tau)}_{A_s \to B_{s'} \mid \iota(t)}(t)$$

The same-scope case $P(s, t) := P(s \to s, t)$ is the default; the cross-scope form covers flows such as $P(1 \to 0)$, from implicit world knowledge into the explicit self model. Two projections of one recurrent substrate predict each other at short lags whatever their content, so $T$ must be estimated conditionally on the shared drive (the sensory input and activity at other scope positions) and reported against a surrogate that preserves each signal's autocorrelation and the shared drive while destroying only the implicit-to-explicit coupling; a time-shift surrogate is a floor, not the null. Estimating $A_s$ and $B_s$ from neural data, and choosing the basis in which they are estimated, is the problem of §2.6, whose criteria apply here in full.

Permeability can be global (averaged over all $s$) or local (at a specific scope position $s$), which maps the theory's distinction between global permeability changes (psychedelics) and local permeability deficits (anosognosia).

### 3.2 Permeability Profiles as Quantitative Predictions

The theory's phenomenological claims become quantitative predictions about the permeability profile (Table 1):

**Table 1.** Predicted permeability profiles by state.

| State | Global P | Local P anomalies | Predicted measurement |
|---|---|---|---|
| Normal waking | Medium | None (narrow selection) | Baseline transfer entropy |
| Psychedelic (psilocybin, LSD) | High | None (global increase) | Transfer entropy spike, broadband |
| Salvinorin A (ego-dissolving dose, below external-input gating) | High + ESM re-sourcing | Self-scope P unchanged; self-referential sensory input unweighted | $T_{i_{\mathrm{self}} \to e \mid i_{\mathrm{ext}}} \to 0$; $T_{i_{\mathrm{ext}} \to e \mid i_{\mathrm{self}}}$ ↑ (§5.2) |
| Salvinorin A (highest doses) | High; external input gated (Maqueda et al., 2015) | Self-scope P unchanged; self-referential sensory input unweighted | $T_{i_{\mathrm{ext}} \to e \mid i_{\mathrm{self}}}$ ↑ with T from sensory input ≈ 0: $i_{\mathrm{ext}}$ internally generated |
| Anosognosia (right hemisphere stroke) | Normal (most domains) | Low at damaged domain | Domain-specific transfer entropy deficit |
| Deep sleep (NREM) | Very low | Uniform suppression | Transfer entropy at the surrogate floor |
| REM dreaming | Medium | Internally driven (from implicit-mode activity, not from ι(t)) | $T_{A_s \to B_s}$ at waking level; T from sensory input ≈ 0 |
| Meditation | Selectively elevated | Trained domain-specificity | Targeted transfer entropy increases |
| Pre-sleep / hypnagogia | Gradually increasing | Bottom-up (low-level → high-level) | Hierarchical onset of transfer entropy |

These predictions are testable on existing EEG, MEG and fMRI datasets once $A_s$ and $B_s$ can be estimated; transfer entropy itself is routinely estimated from such time series (Vicente et al., 2011; Wibral et al., 2014).

### 3.3 The Selection Operator as a Family of Mechanisms

The parent paper (Gruber, 2026, Section 3.6) clarifies that permeability is not a single parameter but a **family of boundary properties** — in biological brains, modulated independently by serotonergic, GABAergic, dopaminergic, and other neuromodulatory systems across sensory channels, cortical regions, and histological contexts. The formalization must reflect this.

Define a **selection family** $G = \{g_c : W \times X \to [0, 1]^{N_c}\}$, indexed by channel c ∈ C, where C is the set of modulatory channels (e.g., serotonergic, GABAergic, dopaminergic, noradrenergic) and $N_c$ is the dimensionality of channel c's spatial resolution (region count, column count, or voxel count depending on the scale of analysis). Each channel comes with a fixed lift $L_c : [0, 1]^{N_c} \to [0, 1]^{N \times N}$ that assigns each coupling (i, j) of W the value of the parcel containing it, so that channels of different resolution act on one index set. The composite selection state is the element-wise product of the lifted maps:

$$g(W, x(t)) = \prod_{c \in C} L_c\big(g_c(W, x(t))\big) \in [0, 1]^{N \times N}$$

The substrate dynamics (Equation [1]) become:

x(t+1) = f(x(t), ι(t), g(W, x(t)) ⊙ W)

where ⊙ is element-wise multiplication. A single selection level $\bar{g}$, the mean of g over the couplings serving a scope position, summarizes the mechanism; permeability P remains the information flow defined above, and the formalization's commitment is that P is monotone increasing in $\bar{g}$ at fixed input, so a channel-specific change in $g_c$ predicts a change in P of the same sign. The monotonicity is a testable functional form, to be fitted on dose–response data, and a non-monotone relation absent an independently established ceiling effect refutes it (Gruber, 2026, Section 3.6). The parent theory locates selection on a read/write path of rank k between the implicit models and the explicit ones (Gruber, 2026, Section 3.6.1): G specifies what enters that path, and the active parts $e_a$, $w_a$ of §6.4 are what occupies it. The parent theory identifies working-memory capacity with k, and k counts the dimensions held as objects, identified and operated on, not the items present in the simulation: the twelve letters of a Sperling display are all seen, and until identified they occupy the simulation as one low-dimensional pattern (Gruber, 2026, Section 3.6.1).

This decomposition has empirical consequences. The theory predicts that:

- Serotonergic agonism (psilocybin, LSD) primarily increases $g_{\text{5-HT}}$ globally, producing the broadband entropy increase measured by Schartner et al. (2017) and interpreted as a global entropy elevation by the entropic brain hypothesis (Carhart-Harris et al., 2014), an account that arrives at the same signature from an independent starting point.
- GABAergic agonism (propofol, benzodiazepines) primarily decreases $g_{\text{GABA}}$ globally, suppressing the implicit-to-explicit transfer.
- Dopaminergic modulation primarily affects $g_{\text{DA}}$ in reward-related scope bands, altering the *content* of what crosses the boundary without necessarily changing the *total amount* of transfer.
- Stroke damage eliminates structural components of specific $g_{c}$ in specific spatial regions, producing the domain-specific permeability deficits observed in anosognosia.

The selection family depends on three classes of input:

- The substrate state x(t): attentional selection (top-down control of what becomes conscious), operating through all channels simultaneously.
- Neurotransmitter dynamics: pharmacological selection, with each neuromodulatory system operating through its own channel $g_{c}$.
- Structural integrity: lesion-dependent selection (stroke damage eliminates $g_{c}$ in specific pathways), affecting spatial resolution within specific channels.

This connects naturally to the criticality-rhythm relationship that the theory lists as a limitation (Gruber, 2026, Section 10.3).

### 3.4 The Fokker-Planck Dynamics

The dynamics of the model density ρ under variable permeability can be modeled as a Fokker-Planck equation on each side of the threshold, the two sides coupled by generation rather than by transport:

∂ρ/∂t = −∇ · (v ρ) + D ∇²ρ + S(s, ν, t) + Γ(s, ν, t)

with no-flux (reflecting) boundary conditions on ∂[0, 1]² and at $\nu = \nu_{\mathrm{crit}}$ from both sides, and with $v_{\nu}$ > 0 denoting drift toward the explicit end of its side. The explicit models are generated from the substrate, not filled by a copy of it (Gruber, 2026, Section 3.6), so no mass crosses $\nu_{\mathrm{crit}}$. The terms are:

- v(s, ν, t), a drift field: deterministic migration of models within each side. Context shifts direct drift along s (between self-focused and world-focused processing); along ν it moves a model toward or away from the threshold without carrying it across.
- D, a diffusion coefficient: stochastic spread within each side.
- S(s, ν, t), a source/sink term: learning and forgetting on the implicit side, and the decay of explicit models that are no longer regenerated.
- Γ(s, ν, t), the generation term, non-zero only above $\nu_{\mathrm{crit}}$: $\Gamma(s, \nu, t) = \kappa(s, t)\, A_s(t)\, \varphi(\nu)$, with $\kappa$ the recruitment rate set by the selection state g at that scope, $A_s$ the implicit activity, and $\varphi$ a profile over the explicit stratum. The part of $\kappa$ outside attentional selection is the baseline leakage that produces visual snow and spontaneous phosphenes.

State transitions then have specific signatures:

- **Psychedelics**: Global increase in $\kappa$: more implicit activity is drawn into generation at every scope.
- **Propofol**: $\kappa$ → 0 together with a sink S < 0 above $\nu_{\mathrm{crit}}$ (the explicit stratum is no longer regenerated), so the mass above the threshold decays while the implicit mass below is unchanged.
- **Meditation**: Trained, selective control over $\kappa(s, t)$: the meditator learns to steer what is drawn into generation.
- **Sleep onset**: Selected generation falls while unselected leakage rises, producing hypnagogic imagery.

### 3.5 Total Conscious Content

The total explicit content at time t is:

$$C_{\mathrm{exp}}(t) = \int_0^1 \int_{\nu_{\mathrm{crit}}}^{1} \rho(s, \nu, t)\, d\nu\, ds$$

Explicit content is phenomenal only where it is in closure (§6.4). The parent theory distinguishes the active closure, between the active self and world models, which gives the sense of being here and now, from a rudimentary closure that it hypothesizes may hold among the non-active explicit models and that would mark the floor of minimal consciousness (Gruber, 2026, Sections 3.3, 3.5); explicit content in neither is preconscious, what psychology called the subconscious, and implicit content is non-conscious. Let $\chi_{\mathrm{act}}(s, \nu, t) \in [0, 1]$ be the fraction of the modeling activity at (s, ν) that is in the active parts of the explicit models at t: in the part of the world model that enters the self model's update $h_e$, or in the part of the self model that enters the world model's update $h_w$ (Gruber, 2026, Section 3.3; §6.4). Its support is bounded by the channel's occupancy (Gruber, 2026, Section 3.6.1): the active content passes through a channel of rank k, so the active explicit content at any time holds at most k dimensions as objects, identified and operated on; content present in the simulation but not identified occupies it as one low-dimensional pattern and is not counted (Gruber, 2026, Section 3.6.1). The bound is a capacity parameter independent of the two criticality dials, while the mass C(t) below is not bounded by k. A weaker grade $\chi_{\mathrm{rud}}(s, \nu, t)$ may be defined for mutual updating among non-active explicit models; the parent theory assigns it, as a hypothesis, to minimal consciousness. The total conscious content, a single scalar representing the "amount" of phenomenal modeling, is defined on the active grade:

$$C(t) = \int_0^1 \int_{\nu_{\mathrm{crit}}}^{1} \chi_{\mathrm{act}}(s, \nu, t)\, \rho(s, \nu, t)\, d\nu\, ds \;\le\; C_{\mathrm{exp}}(t)$$

Where the rudimentary grade is in question, $C_{\mathrm{rud}}(t) := \int\!\!\int \chi_{\mathrm{rud}}\, \rho$ is reported beside C(t) rather than folded in. PCI (Casali et al., 2013) and Lempel-Ziv complexity are empirical correlates of consciousness states; the formalization predicts that C(t) co-varies with them across states through its complexity component, whose formal counterpart in this framework is the dial K of §4.7, and a state with high extent and low on-cluster complexity would separate the two.

---

## 4. Criticality Operationalization

### 4.1 The Substrate as a Dynamical System

Define the full substrate state at time t as x(t) ∈ X ⊆ $\mathbb{R}^N$, where N is the number of functional units. In the biological brain, these are cortical columns; in artificial substrates, they may be processing nodes, recurrent cells, or other computational units. The dynamics follow:

x(t+1) = f(x(t), ι(t), W)     [1]

where ι(t) is sensory input and W is the connectivity matrix (synaptic weights or, more generally, the coupling parameters of the substrate). The biological brain's instantiation of this dynamical system — the cortical automaton, a discrete system on a high-dimensional lattice (Gruber, 2015, 2026) — is the canonical example, but the formalization is substrate-neutral: any dynamical system satisfying the free-modeling and architectural constraints qualifies.

The implicit models are stored in the *parameters* of this system and evaluated by substrate processing:

- IWM = W, the stored knowledge of everything the system models.
- ISM ⊆ W, the part of it that is knowledge of the system itself.

The explicit models are *patterns of activity* — projections of the state vector:

- EWM(t) = $\Pi_{\mathrm{EWM}}$ · x(t)
- ESM(t) = $\Pi_{\mathrm{ESM}}$ · x(t)

where $\Pi_{\mathrm{EWM}}$ and $\Pi_{\mathrm{ESM}}$ are orthogonal projection operators with range($\Pi_{\mathrm{ESM}}$) ⊆ range($\Pi_{\mathrm{EWM}}$), so $\Pi_{\mathrm{EWM}} \Pi_{\mathrm{ESM}} = \Pi_{\mathrm{ESM}} \Pi_{\mathrm{EWM}} = \Pi_{\mathrm{ESM}}$, the nesting, and $\Pi_{\mathrm{EWM}} - \Pi_{\mathrm{ESM}}$ is the projection onto the closure partner EWM∖ESM, whose state is $(\Pi_{\mathrm{EWM}} - \Pi_{\mathrm{ESM}})\, x(t)$. The projections are onto activity subspaces, not onto sets of units, and they are not cell masks: a projection counts as a model only if $\Pi \cdot x(t)$ meets the write and readability criteria of §2.1 for some target, and how those criteria are tested on activity data, and against which nulls, is the measurement question of §2.6. The substrate processing that evaluates the stored models is the activity outside the explicit subspace, $x_{\mathrm{imp}}(t) := (I - \Pi_{\mathrm{EWM}})\, x(t)$, routed through W; the implicit side of ρ (ν < $\nu_{\mathrm{crit}}$) counts this processing, and $A_s(t)$ is its mass at scope s, while W itself carries no time index at recording scale. This maps the real/virtual split directly: W (parameters, slow, structural) and the processing routed through it = real side; x(t) projected through $\Pi_{\mathrm{EWM}}$ and $\Pi_{\mathrm{ESM}}$ (states, fast, transient) = virtual side.

### 4.2 Three Candidate Criticality Measures

The theory requires free modeling — open-ended computational capability, of the kind Wolfram's Class 4 automata exhibit (Wolfram, 2002) but not confined to them (Gruber, 2026, Section 3.7.3), recruited by the system for its own modeling, including models that serve no present goal — and reads near-criticality as its usual signature in neural tissue, not as a requirement (Gruber, 2015, 2026). Free modeling is weaker than Turing universality: operationally it is the capacity to form models of novel compositional structure that a feedforward model of matched capacity, trained on the same history, cannot match as compositional depth grows (Gruber, 2026, Table 1b). Class 4 is defined for cellular automata, not for continuous, noisy, high-dimensional neural substrates. Three existing measures can operationalize the signature:

**Branching ratio σ**: The average number of descendant activations per ancestor activation across neuronal avalanches (Beggs & Plenz, 2003; Shew & Plenz, 2013).

- σ < 1: subcritical (activity dies out)
- σ = 1: critical
- σ > 1: supercritical (activity explodes)

Under subsampling σ tracks firing rate, so it is reported beside a rate-matched surrogate (Gruber, 2026, Section 8.12). The ConCrit framework (Algom & Shriki, 2026) proposes criticality as a unifying mechanism across theories of consciousness, and Hengen and Shew's (2025) meta-analysis of 143 datasets consolidates the premise that cortex operates near criticality as a setpoint; neither establishes that σ covaries with conscious state. The formalized claim is a **signature hypothesis**, weaker than a requirement: **in the waking human cortex, conscious processing is hypothesized to show σ ∈ [$\sigma_{\mathrm{low}}$, $\sigma_{\mathrm{high}}$]** where $\sigma_{\mathrm{low}}$ ≈ 0.95 and $\sigma_{\mathrm{high}}$ ≈ 1.1 (the lower end anchored by the slightly subcritical waking values of Priesemann et al., 2013, 2014; the upper end is this paper's own margin and has no measured anchor). The band is a region, not a point, and an empirical generalization over the measured cases, not a derived threshold; a conscious system outside it, a subcritical one included, does not count against the theory — the reasons are given in §4.4, and §4.7 makes criticality a regionally varying property rather than a single whole-substrate coordinate. A caution on the numbers themselves: nominal σ = 1 is a normalization convention rather than a substrate-independent edge, and in leaky recurrent substrates the dynamical edge of chaos can sit well away from it, so the band above should be read as calibrated to the neural recordings it was estimated from and re-estimated for any other substrate.

**Maximum Lyapunov exponent $\lambda_{\max}$**: For edge-of-chaos dynamics specifically (Bertschinger & Natschläger, 2004; Boedecker et al., 2012):

- $\lambda_{\max}$ < 0: ordered (stable attractors)
- $\lambda_{\max}$ ≈ 0: edge of chaos
- $\lambda_{\max}$ > 0: chaotic

In a driven substrate a positive time-series estimate of $\lambda_{\max}$ is not by itself evidence of chaos, since a stable linear system driven by noise also reads positive; estimates are compared against a noise-driven stable linear null or taken from the tangent-space Jacobian. The two axes are measured on different signals and need not agree. In human cortex they do not: waking is slightly subcritical by branching ratio (Priesemann et al., 2014) and on the chaotic side of the edge by its slow electrodynamics (Toker et al., 2022); propofol is expected to push the branching axis below critical (Gruber, 2026, Table 4) while its electrodynamics move deeper into the chaotic phase, and LSD moves the electrodynamics closer to the edge (Toker et al., 2022). Class 4 is therefore not read off either scalar alone, and states occupy regions on each axis, not points. Toker et al. label the two sides periodic/stable and chaotic/unstable; "ordered" here keeps its reservoir-computing sense of stable, periodic dynamics.

**Detrended Fluctuation Analysis (DFA) exponent α**: Long-range temporal correlations in neural time series (Hardstone et al., 2012). α in 0.6–0.9 indexes long-range temporal correlations; α ≈ 0.5 indicates uncorrelated fluctuations, and α > 1 non-stationary drift.

A further, model-free readout is the Fisher information metric of a control parameter, or of the observed branching ratio when the control parameter is unknown, whose peak width and height track proximity to criticality across branching, spiking and whole-brain models (Du et al., 2026).

### 4.3 Disambiguating Criticality Types

An important caveat: Kanders et al. (2017) demonstrated that avalanche criticality (σ ≈ 1) and edge-of-chaos criticality ($\lambda_{\max}$ ≈ 0) do not necessarily co-occur in neural networks. These are measuring *different* phase transitions. The theory's reference to "edge of chaos" via Wolfram's Class 4 aligns more naturally with the Lyapunov exponent than with the branching ratio, while the empirical criticality literature (ConCrit) focuses primarily on the branching ratio and avalanche statistics. In deterministic cellular automata, the damage-spreading transition — between a phase in which trajectories from different initial conditions coalesce quickly and one in which they stay different — contains directed percolation as the first level of an infinite hierarchy of renormalization-group fixed points (Nahum & Roy, 2026). Criticality in models inferred from recordings can also arise from the inference itself: as the number of neurons grows, inferred parameters concentrate near critical points without fine-tuning (Carcamo & Lynn, 2026).

The formalization must resolve this ambiguity. Three options:

1. **Both**: the operating regime is characterized by σ ≈ 1 AND $\lambda_{\max}$ ≈ 0 jointly. This is the most restrictive and potentially the most empirically productive — it implies that systems at avalanche criticality but not at edge-of-chaos, or the reverse, fall outside the signature band the theory associates with free modeling in cortex — and whether waking cortex, slightly subcritical by σ and slightly chaotic by $\lambda_{\max}$, lies inside the joint band depends on band widths not yet fixed, which is why §4.7 reports $E^{\sigma}$ and $E^{\lambda}$ separately.

2. **Avalanche criticality sufficient**: The branching ratio is the operative measure; edge-of-chaos is a correlate but not independently required. This aligns with the ConCrit literature.

3. **Edge-of-chaos is primary**: $\lambda_{\max}$ ≈ 0 is the operative coordinate (following Wolfram's framework most closely); avalanche criticality is a consequence. This aligns with the theoretical derivation in Gruber (2015).

These three are options for *which observable indexes the regime*, and they are stated at the level of the signature hypothesis of §4.4 rather than as requirements on consciousness. Choosing among them is an empirical question about measurement, and none of the three is settled by the theory.

The two measures already diverge in waking and under propofol (Toker et al., 2022); the open question is which of them, if either, tracks consciousness across the remaining states.

### 4.4 Criticality: A Signature, Not a Prerequisite

The parent theory requires free modeling and treats near-criticality (Wolfram Class 4 / edge of chaos) as its signature, not as a requirement for consciousness (Gruber, 2026, §3.7). Whether the signature could be *derived* from the theory's commitment to self-referential closure is the question of the chain

> self-referential closure ⇒ universal computation ⇒ Class-4 dynamics ⇒ criticality.

**This chain is a conjecture, not a proof.** It is offered as a research target — a structure that *would*, if established, upgrade criticality from an empirical correlate to a consequence — and it rests on two lemmas that are, at present, **open**:

- **Lemma L1 (closure ⇒ free modeling) — OPEN.** *Does self-referential closure (a system whose explicit self and world models update each other, the self model standing for the system that generates the world model; Gruber, 2026, Section 3.4.3; §6.4) entail free modeling as defined above (L1a), or the stronger property of computational universality, the capacity to simulate an arbitrary program (L1b)?* Neither is established. Self-representation of one's own dynamics is not known to be equivalent to Turing-universality; a system may faithfully model salient aspects of its own operation while being computationally weaker than a universal machine. No proof is known to the author, and the implication may well be false as stated. What can be said rigorously is only that deeper recursive self-modeling requires *more* computational resource (a monotonicity claim), not that it requires *universal* resource.

- **Lemma L2 (universality ⇒ criticality) — OPEN.** *Does computational universality require, or even imply, operation at or near a critical dynamical regime (Class 4 / edge of chaos)?* This is **not** established, and the standard results point the other way. (i) Wolfram's principle relating Class 4 to universality is itself a **conjecture** (the Principle of Computational Equivalence), not a theorem. (ii) Universality has been **proven only for specific rules** (Rule 110, Conway's Life), not for Class 4 as a class. (iii) Class-4 behavior is **not necessary** for universality — universal computation is realized by systems that are not naturally described as edge-of-chaos. (iv) Universality is a statement about what a system *can compute in principle*, whereas criticality is a statement about the *dynamical regime it occupies during operation*; the two are logically distinct, and one does not obviously entail the other. (v) The nearest existing formal handle is compression-based: Zenil (2010) conjectures, from elementary cellular automata, that universality implies a positive phase-transition coefficient — a nonzero sensitivity of a rule's compressed output to its initial condition. That conjecture is unproven, and it concerns sensitivity rather than criticality in the neural sense, but a proof of it would be the first result of L2's shape. For input-driven continuous-time reservoirs, Sugiura et al. (2025) prove that a neighborhood separation property is necessary and sufficient for universal approximation of input–output maps with polynomial readouts; Roig, Muñoz, and Morales (2026) extend the result to driven discrete-time reservoirs and find numerically, in benchmarks with linear readouts, that separability, prediction and representation geometry are optimized together in a narrow window of marginal driven stability. Sugiura et al. also prove that such a reservoir is discontinuous on a dense set of inputs (their Theorem 3), which they read as requiring chaotic dynamics. Physical noise caps the resolution of any physical reservoir (London et al., 2010; Hu et al., 2023), so the infinite resolution of Sugiura et al.'s Theorem 3 is out of reach in every dynamical regime, and in driven random networks the finite-resolution optimum lies where the input-driven dynamics are stable although the undriven network would be chaotic (Schuecker et al., 2018; Haruna & Nakajima, 2019). For reservoir forecasting, Du and Wang (2026) find that the spectral radius giving the best performance does not coincide with the Lyapunov edge of the reservoir, and in a pre-registered replication on thirty rate reservoirs a demand-gated accuracy peak lies in the driven-stable regime, not at the measured edge (Gruber, 2026d). No theorem yet forces the maximal Lyapunov exponent to zero, and approximation universality is not computational (Turing) universality, so L2 remains open.

Accordingly, criticality in this theory is an **empirically motivated signature hypothesis** — well supported as a *correlation* by the consciousness-criticality literature — and the "deductive" chain above should be pursued as an open program: *if* L1 and L2 can each be proven (or given a precise restricted form under which they hold), *then* criticality follows; until then, it does not. A separate derivation route runs through coding optimality rather than closure: in a Gaussian population-coding model, maximizing Fisher information under resource constraints yields soft modes and diverging correlation lengths, and with spatial structure added unifies statistical and dynamical criticality (Xiao et al., 2026). Nothing else in the formalization depends on the derivation succeeding, and neither does the parent theory, whose requirement is free modeling. The transfer-entropy permeability formalism and the criticality *observables* stand entirely on their own as empirical instruments, independent of whether L1 and L2 are ever closed.

### 4.5 The Two Thresholds as a Conjunction

The theory posits two thresholds — free modeling and a self-simulation architecture. Formally these combine as a **conjunction of independently-stated requirements**:

> Consciousness ⟹ [ free modeling: open-ended computation recruited by the system for its own modeling, including models that serve no present goal ] ∧ [ self-simulation architecture: significant modeling mass on both self and world, at both implicit and explicit levels ].

Both conditions are asserted to hold together, and each is independently motivated: a substrate with open-ended dynamics but no self-modeling has complex dynamics but no self-simulation; an architecture with the right model profile whose free modeling is abolished (e.g., deep propofol anesthesia, where cortical dynamics also turn subcritical on the branching axis) retains the structural capacity but cannot instantiate the simulation. The near-critical band is the signature the first condition usually leaves in cortex.

**Neither condition is claimed to entail the other.** That closure entails free modeling is Lemma L1a, which is open, and the architecture condition above does not include closure. Until a lemma of that shape is proven, the two thresholds are stated as **co-required but logically independent** — an empirically-motivated conjunction, not a derived implication. If L1a is later established and closure is added to the architecture condition, this conjunction can be strengthened to an entailment; that strengthening is a goal of the formalization program, not a present result.

The parent theory's sufficient condition is the conjunction of its §3.7.3: the four model kinds under closure, free modeling, embodiment and at least one pain-pleasure axis. This paper formalizes only the two necessary thresholds.

### 4.6 The Implicit-Explicit Threshold as a Graph Phase Transition

The threshold $\nu_{\mathrm{crit}}$ — the ontological boundary between implicit and explicit modeling — may have a more specific mathematical characterization than a simple parameter value.

In Quantum Graphity (Konopka et al., 2008), spacetime emerges from a complete graph through a phase transition: at high energy, the graph is fully connected and symmetric; at low energy, it undergoes a transition to an ordered, low-dimensional, local structure. The transition is a graph phase transition characterized by abrupt changes in clustering coefficient, path length, and modularity.

If the consciousness-cosmology correspondence proposed by the companion cosmological model (Gruber, 2026c), which that paper states for the implicit/explicit axis only and leaves open as to whether it is a strict identity, holds, then the explicit stratum ν > $\nu_{\mathrm{crit}}$ may be a distinct graph phase of the activity: below the threshold, processing is distributed, high-connectivity and unstructured (implicit); above it, low-dimensional and structured, with local (short-range) geometry in the functional-connectivity graph (explicit). "Local" here is a property of that graph, not a claim that explicit models sit in a region of tissue: they are distributed activity and cannot be localized (Gruber, 2026, Section 3.2).

Two measurable consequences follow and must be kept apart. Within a single state, the activity should separate into two connectivity phases, with the explicit phase identifiable by clustering coefficient, modularity and effective dimensionality without reference to consciousness; this is what would make $\nu_{\mathrm{crit}}$ **empirically measurable**. Across states (sleep-wake, anesthesia induction and recovery, psychedelic onset), the mass in the explicit phase, $\int_{\nu > \nu_{\mathrm{crit}}} \rho$, should change abruptly at consciousness transitions, independent of which neural measure supplies the graph's edge weights; that is a transition in a control parameter, the crossing of the thresholds θ, and not a shift of $\nu_{\mathrm{crit}}$ itself.

### 4.7 The Two Dimensions of Criticality: Extent and Complexity

Sections 4.2–4.6 treat criticality as a *single* coordinate: a substrate is sub-, at-, or super-critical, detected by one of three whole-recording scalars (σ, $\lambda_{\max}$, α). The parent theory, however, makes a claim that a single coordinate cannot express — that conscious processing varies along two dimensions that can move independently: **how much** of the substrate is engaged in near-critical (Class-4-like) dynamics, and **how rich** the dynamics on that engaged tissue are (Gruber, 2026, Section 3.7). Taken literally against a single critical point this is a category error: a homogeneous system at one critical point has one order parameter, one correlation length, one set of exponents, and "two independently variable dials off one point" cannot be constructed. Replacing the single critical point with a field of locally critical regions puts the two dials on distinct mathematical objects; the independence of the dials is a conjecture (Orthogonality, below).

**The heterogeneity premise.** Replace "one critical point" with a substrate that is a *field of locally-critical regions*. Partition the N functional units into R local neighborhoods (cortical parcels, columns, or, in an artificial substrate, node blocks) i = 1..R, and estimate criticality *regionally*: each neighborhood i carries a local branching ratio $\sigma_{i}$, a local edge-of-chaos exponent $\lambda_{\max,i}$, and/or a local DFA exponent $\alpha_{i}$. Define two local-criticality indicators,

> $c_{i}^{\sigma}$ = 1 iff $\sigma_{i}$ ∈ [$\sigma_{\mathrm{low}}$, $\sigma_{\mathrm{high}}$], and $c_{i}^{\lambda}$ = 1 iff |$\lambda_{\max,i}$| < ε,

and report extent separately for each ($E^{\sigma}$, $E^{\lambda}$); the conjunction $c_{i} = c_{i}^{\sigma} c_{i}^{\lambda}$ is the strict variant. The two can disagree in the same state (propofol: $c^{\sigma}$ = 0 while $\lambda_{\max}$ > 0; Toker et al., 2022), so a single indicator is not available. In §4.2, σ and α are *whole-recording* estimates; here they are estimated per region and a spatial statistic is taken over {$c_{i}$}. Criticality becomes a spatially varying property, and two independent questions can be asked of the field — *how much* of it is critical, and *how complex* the critical dynamics are. Recorded criticality signatures vary regionally: in mouse visual cortex and hippocampus they change systematically along the anatomical hierarchy, and static and dynamic exponents order the regions in opposite directions (Cambrainha et al., 2026), so the marker chosen to define $c_{i}$ matters.

Estimating $c_{i}$ needs a surrogate that removes causal transmission while preserving each region's temporal structure, since the surrogate fixes the null hypothesis the local estimate is tested against (Theiler et al., 1992). A surrogate that permutes each unit's activity across the whole recording (a column or channel shuffle) keeps its rate but destroys its alignment with population-wide bursts; a near-critical substrate bursts population-wide, so this surrogate underestimates the null exactly there and can manufacture spurious local criticality. Window-jitter surrogates, which keep each unit's count within every time window and randomize timing only inside it (Amarasingham et al., 2012), preserve that alignment. The window width trades retained signal against retained confound, so the cut-off defining $c_{i}$ should be set on the separation between causal and non-causal reference data, not on the raw excess over the surrogate.

**Extent E (a spatial order parameter).** The first dial is a measure over *space*: which regions are in the Class-4 regime. In increasing strength:

> (a) fraction at criticality  $f_{\mathrm{crit}}$ = (1/R) $\Sigma_{i}$ $c_{i}$;
> (b) **giant-critical-cluster size** P∞ = |largest connected component of mutually-correlated critical neighborhoods| / R;
> (c) correlation length over system size, ξ/L.

**P∞ (b) is the recommended order parameter.** Build the critical-connectivity graph on the units {i : $c_{i}$ = 1}, with an edge between two critical units when their activity correlation (or transfer entropy) exceeds threshold; P∞ is then the normalized size of its giant component. This is exactly the percolation order parameter of a *spatial* phase transition (Stauffer & Aharony, 1994) and reuses the graph machinery of §4.6 (clustering, modularity, giant component). It is distinct from the temporal/avalanche critical point σ→1: $\sigma_{i}$ detects whether a *region* is critical at all; P∞ measures how far a single integrated critical process *reaches* across regions. The two can come apart: in a multi-agent model whose agents each run a reservoir, near-critical dynamics inside each agent do not produce collective critical avalanche statistics, which depend on the effective connectivity of the interaction network (Bessone & Plantec, 2026). P∞ makes the binding claim of the parent paper (Gruber, 2026, Section 5.1: maximal correlation length ⇒ substrate-spanning integration) the *same quantity* as extent.

**Complexity K (a dynamical measure).** The second dial is a property of the *dynamics within* the recruited critical region(s), not of space. Let $X_{G}$(t) be the activity restricted to the giant critical cluster G (the units counted by P∞). Define

> K = LZ($X_{G}$) — the Lempel-Ziv complexity rate (Lempel & Ziv, 1976) of the on-cluster activity after symbolization, conditioned on criticality (evaluated only over G), with K := 0 when G is empty.

LZ complexity is defined on a symbol sequence, so the symbolization is part of the definition: each channel in G is binarized at its own median instantaneous amplitude, the binary columns are concatenated in a fixed channel order, and the LZ76 count is normalized by that of a shuffled copy of the same sequence (Schartner et al., 2017); it is reported with every K. For a stationary ergodic source the LZ rate converges to the entropy rate; excess entropy is a distinct quantity and is not used here.

K measures the algorithmic richness of the computation the critical tissue performs. Perturbational complexity (PCI; Casali et al., 2013) and Lempel-Ziv complexity (LZc; Schartner et al., 2017) map onto K, **not** onto extent — the differentiation caveat of the main paper (Gruber, 2026, §3.7) is inherited here as a formal distinction. Note that K is *not* the total-content scalar C(t) of §3.5: C(t) integrates closed-loop modeling mass over the whole density ρ, whereas K is the conditional complexity of the on-cluster trajectory. C(t) is a joint quantity (it rises when either dial rises); K isolates the dynamical dial. K does not by itself identify the regime: compressed length separates chaotic and complex cellular automata (Classes 3 and 4) from ordered ones, but not complex from chaotic (Zenil, 2010), so a high K is equally what a chaotic cluster would produce. K carries regime information only because it is evaluated on the critical cluster G — the conditioning on criticality does that work, and K measures richness within it. A compression measure normalized against sorted and shuffled surrogates, built as the product of distance from order and distance from disorder, peaks at the critical temperature of the 2D Ising model (Jacobus, 2026), and is a candidate independent check on the regime of G.

**Orthogonality (a conjecture, not a theorem).** E and K are defined on different mathematical objects — E is a measure over *space* (which regions are critical), K is a measure over *dynamics* (how rich the on-critical computation is) — so nothing forces them to co-vary. One can grow the critical cluster while each region computes something simple (E↑, K≈const), or hold a small cluster running an intricate computation (K↑, E≈const). The separating case that makes the distinction more than a definitional convenience is the **generalized tonic-clonic seizure**: near-maximal co-activation, but with the substrate driven out of the Class-4 regime. The route out differs by seizure type and phase: focal ictal recordings lose the power-law statistics of the critical regime (Meisel et al., 2012) with heterogeneous single-neuron activity at onset (Truccolo et al., 2011), and in the generalized seizures measured so far, two intracranial and one MEG, the slow cortical electrodynamics crossed the edge of chaos into the periodic phase (Toker et al., 2022), while hypersynchrony dominates the late phase and termination. The decomposition needs only the exit from Class 4, whichever route obtains: under the definitions above such a state has high $\Sigma_{i}$ activity yet a critical fraction near zero, so **E ≈ 0** — and the loss of consciousness the free-modeling requirement predicts is recorded by the extent dial collapsing, not by any drop in raw activity. This is the case in which co-activation and extent are *provably* different functionals (Σ activity vs. |{regions in Class-4}|), and it is what forces E to be defined as Class-4 spatial measure rather than co-activation. Their *independence* over the whole reachable state space, however, is asserted as an **empirical/formal conjecture to be tested** (regionally-resolved criticality mapping jointly with on-cluster LZ across states), not derived here.

**Relation to neural complexity $C_{N}$.** The closest formal precedent is Tononi–Sporns–Edelman neural complexity (Tononi, Sporns, & Edelman, 1994),

$$C_N(X) = \sum_{k=1}^{n} \Big[ \tfrac{k}{n} H(X) - \big\langle H(X_k^j \mid X - X_k^j) \big\rangle_j \Big],$$

which collapses *integration* and *differentiation* into a single scalar that is maximized exactly when the system is simultaneously integrated (high whole-system entropy) and differentiated (subsets near-independent). Integrated information Φ (Tononi, 2004) is a later single-scalar in the same spirit; Barrett et al. (2026) note that Φ is not well defined for real physical systems and has not been computed on one, and propose replacing it with a suite of quantities that characterize states of consciousness in several dimensions. A 2-D plane adds formal content beyond $C_{N}$, instead of re-spreading one optimized scalar over two axes, **iff** the axes are independently measurable *and* independently manipulable, which is why E and K are placed on distinct structures (spatial percolation measure vs. on-cluster dynamical measure). $C_{N}$ assumes a single substrate-wide optimum; the two-dials claim asserts a *frontier* on which one dial is high while the other is low, with the joint corner (both maximal) reachable only rarely. That is a strictly stronger, more falsifiable structure than $C_{N}$ — but only under the distinct-objects definitions above; a Φ- or $C_{\mathrm{N-flavored}}$ quantity would *not* cleanly separate the seizure (its failure is local Class-4 loss, not global irreducibility), which is the diagnostic that the two-axis reading is not a renaming. For this reason Φ is **not** adopted as the extent index (it conflates integration and differentiation and would double-count K); extent is the percolation/fraction/ξ measure, and $C_N$/Φ are cited as measures of the *joint corner*, not of extent alone.

**Processing volume and subjective duration.** A time-dilation claim follows from the two-dials structure — that driving *both* dials high together produces extreme subjective time-dilation, unifying near-death "life-review" reports and high-dose salvia phenomenology. The parent paper treats subjective time through its temporal-echo mechanism (Gruber, 2026, Section 3.4.4), where the constructed "now" is one frame of the recursive self-simulation running on a clock whose speed varies with the organism's situation, and does not state this prediction; it is developed here, and it requires a definition of "processing volume". Using the total-conscious-content scalar C(t), define

$$\text{processing-volume}(\Delta t) := \int_{\Delta t} C(t)\, dt, \qquad \text{subjective duration} \propto \int_{\Delta t} C(t)\, dt,$$

i.e. experienced duration scales with the *quantity of self-simulation processing completed per unit physical time*, the physical clock-second entering only because the substrate runs at a finite rate. This ties the prediction to existing apparatus and makes the joint corner quantitative: both dials up ⇒ more of the substrate computing richer dynamics ⇒ higher C(t) ⇒ larger $\int C(t)\, dt$ over a fixed physical interval ⇒ dilation. The proportionality constant is a calibration parameter, not derived; the claim earns only a *monotone* functional form (dilation increases with accumulated processing), and its falsifier is dilation reported while $\int C(t)\, dt$ over the interval is not elevated; a separate regression of reported dilation on E and K tests whether both dials contribute. The processing volume relates experienced to external duration and is neutral between the unfolding and structure readings of §6.4.

**Where this leaves the two dials.** With E = P∞ (percolation extent), K = on-cluster LZ (dynamical complexity), the seizure as the separating negative control, $C_{N}$ engaged as prior art, and processing-volume $:= \int C(t)\, dt$ tying time-dilation to the total-content scalar, the two-dials decomposition moves from a verbal assertion to a defensible formal structure whose one open conjecture, the independence of E and K, awaits empirical test. The full program — regional σ/α estimation protocols, conditional-LZ estimators on the recruited cluster, and a joint E–K reachability map — is Phase-2 formal work.

---

## 5. ESM Redirection Dynamics

### 5.1 The ESM as an Input-Dependent Attractor

The prediction that ego dissolution content is controllable by controlling what is salient (Gruber, 2026, Prediction 2, Section 8.3) requires a formal account of how the ESM takes up alternative content when normal self-referential input is disrupted.

Model the ESM as a dynamical subsystem whose attractor landscape depends on its inputs. Let e(t) ∈ $\mathbb{R}^{d_e}$ be the ESM state of §4.1, the coordinates of $\Pi_{\mathrm{ESM}}\, x(t)$ in a basis of range($\Pi_{\mathrm{ESM}}$), with $d_e$ = rank $\Pi_{\mathrm{ESM}}$ (the mass ∫ρ over s ≈ 0, ν > $\nu_{\mathrm{crit}}$ is a separate scalar and is not used here). e(t) is a low-dimensional, integrated model of the system itself, drawn from several implicit models together with interoceptive, proprioceptive and motor feedback and modulated by salience and memory (Gruber, 2026, Section 3.2). Self-scope mass counts toward $\theta_{\mathrm{ESM}}$ only if it is integrated: a model of the body, or at least a viewpoint, the origin to which the senses are referred and which binds their input; a position estimate alone does not qualify (Gruber, 2026, Section 3.4.3). In a simple system e(t) and the implicit self model it is generated from are hard to tell apart, which bounds how sharply $\nu_{\mathrm{crit}}$ can be estimated there. The formalization must allow self-scope explicit mass with $\chi_{\mathrm{act}}$ = 0, an explicit self model outside any closure, which the parent theory classes as preconscious (Gruber, 2026, Section 3.3). Under normal conditions:

e(t+1) = h(e(t), $i_{\mathrm{self}}$(t), $i_{\mathrm{ext}}$(t))

where $i_{\mathrm{self}}$(t), the self-referential input (interoceptive, proprioceptive), dominates, and $i_{\mathrm{ext}}$(t) is the highest-salience component of the closure partner's state $(\Pi_{\mathrm{EWM}} - \Pi_{\mathrm{ESM}})\, x(t)$. The ESM has a stable attractor basin around the "normal self" configuration.

During ego dissolution (salvinorin A, the κ-opioid agonist in *Salvia divinorum*), the weight on $i_{\mathrm{self}}$ falls:

e(t+1) = h(e(t), α · $i_{\mathrm{self}}$(t), (1 − α) · $i_{\mathrm{ext}}$(t))

where α → 0 as dose increases. The ESM's attractor basin reshapes around the salient content. This is the formal mechanism underlying the salvia phenomenology described in Gruber (2026, Section 6.1): users "become" objects in their environment, or the figure a television show is displaying, because the ESM takes up the most salient content available. The salient content need carry no contingency with the subject's heartbeat, breathing or movement. Whether classic serotonergic psychedelics produce the same migration onto external content is open, since they also intensify internally generated content, which competes with $i_{\mathrm{ext}}$ for salience.

### 5.2 Quantitative Predictions

The claims are causal, and the two inputs are correlated in any real environment, so the quantitative measure is the directed, conditioned one: the transfer entropy from each input to the ESM state, conditioned on the other,

- $T_{i_{\mathrm{self}} \to e \mid i_{\mathrm{ext}}}$: how much the self-referential input drives the next ESM state beyond what the salient content and the ESM's own past predict;
- $T_{i_{\mathrm{ext}} \to e \mid i_{\mathrm{self}}}$: how much the most salient content of the explicit world model, external or internally generated, drives it (equivalently $I(e(t+1);\, i_{\mathrm{ext}}(t) \mid e(t), i_{\mathrm{self}}(t))$).

The theory predicts:

- Normal waking: $T_{i_{\mathrm{self}} \to e \mid i_{\mathrm{ext}}}$ ≫ $T_{i_{\mathrm{ext}} \to e \mid i_{\mathrm{self}}}$. The ESM is driven primarily by self-referential input.
- Low dose: the first falls; the second begins to rise.
- Ego dissolution, inside the dose window: the first → 0; the second → its maximum. The ESM identity tracks the most salient content, external while external input still reaches the subject and internally generated above the gating dose (Maqueda et al., 2015).
- Controllability prediction: In a controlled sensory environment during ego dissolution, $T_{i_{\mathrm{ext}} \to e \mid i_{\mathrm{self}}}$ should follow experimentally manipulated salience — visual, auditory, or tactile — in a predictable, dose-dependent manner. This holds only inside the dose window: at the highest doses salvinorin A gates external audiovisual input, so external content no longer reaches the subject (Gruber, 2026, Section 8.3).

Input tracking as such is shared with precision-weighted predictive processing, in which relaxed self-priors let the most precise channel set belief about the self. To separate the two, $i_{\mathrm{ext}}$ is split into a salient stream and a stream synchronised with the subject's heartbeat, each conditioned as above. The theory predicts that the transfer is carried by the salient stream when the two fall on different stimuli; predictive accounts of bodily self-attribution predict that it is carried by the synchronised stream (Gruber, 2026, Section 8.3).

This is testable in principle with fMRI: measure the conditioned transfer from controlled sensory input and from interoceptive input into activity in self-referential networks (default mode structures, a candidate correlate of self-simulation and not a location of the ESM; Gruber, 2026, Table 1 note c) across dose levels.

### 5.3 Redirection in the Model Space

In the model-space framework, redirection is not a migration of mass along s. The ESM is individuated by its target, the system itself, so its scope coordinate stays near s ≈ 0 and its mass in $N_{\mathrm{ESM}}$ stays above $\theta_{\mathrm{ESM}}$; what changes is the input that generates it, from $i_{\mathrm{self}}$ to $i_{\mathrm{ext}}$, so the content of the self-scope region comes to resemble the content of the world-scope region. The measurable signature is a change in the content source of the self-scope explicit mass, $T_{i_{\mathrm{ext}} \to e \mid i_{\mathrm{self}}}$ ↑ with $\int_{N_{\mathrm{ESM}}} \rho$ unchanged, not a displacement of mass toward s → 1. Consciousness is preserved because the ESM mass and its closure with EWM∖ESM persist: ego dissolution is ESM re-sourcing, not ESM abolition. Where the self model has nothing to latch onto, as perhaps in disembodied dissolution under salvinorin A (Gruber, 2026, Section 3.2), the nesting itself may fail and the mass in $N_{\mathrm{ESM}}$ may fall; that is a different and more severe case, and the formalization then predicts degraded rather than preserved consciousness.

The re-sourcing should be measurable as a shift in the representational content carried by the self-scope activity toward content typical of sensory processing networks, detectable via representational similarity analysis (RSA) of fMRI data during controlled salvinorin A administration, with the readout caveat of §2.6.

---

## 6. Self-Referential Closure

### 6.1 Closure and the Hard Problem

The theory's central philosophical claim — that self-referential closure is what makes the simulation phenomenal — carries the weight of its transformation of the Hard Problem (Gruber, 2026, Section 3.4). A weather simulation models weather but does not model itself modeling weather; therefore it has an "outside" from which it can be fully described. A self-referential simulation has no such outside in its own representational economy — the simulation *is* its own observer, and observation-from-inside is what the theory identifies as experience. The asymmetry is perspectival: an outside description still exists and captures the structure of the self-model, as the parent theory's own third-person standpoint does, without exhausting the perspective the closed loop constitutes (Gruber, 2026, Section 3.4.3). What cannot appear in the self-model's product is the current act of generating it; past states and even a complete description of the generator can (Gruber, 2026f, Section 7.1).

This argument needs formal grounding. Four mathematical approaches are proposed below, and one subsection bounds their cost.

### 6.2 The Observability Constraint

The parent paper (Gruber, 2026, Section 3.4.3) introduces an **observability constraint** that is architecturally constitutive on the reading the parent theory adopts as its own commitment, not merely epistemic: the ESM's observational horizon is bounded by the EWM. The explicit self-model cannot see with useful resolution beyond the explicit world model to the implicit substrate that generates it.

Formally, define the **observable set** of the ESM as $O_{\mathrm{ESM}}$ — the set of states, properties, and processes that the ESM can represent within its self-simulation. Define the **simulation scope** $S_{\mathrm{EWM}}$ as the set of states, properties, and processes that the EWM currently models. The observability constraint is:

$O_{\mathrm{ESM}}$ ⊆ $S_{\mathrm{EWM}}$

The ESM can only model aspects of the system that are already represented within the explicit simulation. It cannot "reach through" the virtual level to directly represent substrate-level processes (implicit model parameters, synaptic weights, neurotransmitter concentrations) unless those processes have first been drawn into the generation of the explicit models via the permeability mechanism. The explicit models are generated from the substrate, not filled by a copy of it. The constraint's invariant content is $O_{\mathrm{ESM}}$ ⊆ $S_{\mathrm{exp}}$ := {ν > $\nu_{\mathrm{crit}}$}: the ESM represents only explicit content, never the substrate directly. This is a horizon claim, distinct from the content nesting ESM ⊆ EWM. Under the normal nested mode $S_{\mathrm{EWM}}$ is the whole explicit stratum and the two inclusions coincide; where nesting fails (Gruber, 2026, Section 3.2, hedged for disembodied salvinorin A states and Cotard's delusion) the explicit-stratum inclusion still holds, and under the redirection of §5.1 the horizon holds while the nesting may not.

This constraint has three formal consequences:

1. **The Meta-Problem follows from the architecture.** The mechanisms generating the simulation (implicit models, substrate dynamics) are outside $S_{\mathrm{EWM}}$ except where permeability draws them in, so the ESM meets a principled opacity when it models the basis of its own experience. Whatever enters through the selection family enters as content, and the generating of the current explicit state is never among that content, since the generator appears in its product only as a finished state (Gruber, 2026f, Section 7.1). The parent theory adds a second mechanism, near-opacity punctuated by occasional leaks (Gruber, 2026, Section 3.8), which the unselected part of the generation term of §3.4 carries; the felt depth of the problem comes from the two together. That the resulting gap is the phenomenal gap is the parent theory's identity claim, argued for and not proven (Gruber, 2026, Section 4.2.5).

2. **The Hard Problem's formulation presupposes an outside that exhausts.** The Hard Problem asks: "Given a complete physical description, why is there experience?" It presupposes that an outside description exhausts what the system does. The constraint gives that presupposition an architectural form: the perspective constituted by the closed loop is not among the properties an outside description of $S_{\mathrm{EWM}}$ lists, and the system cannot occupy that description of its own generation from inside. Whether this makes the question ill-posed depends on the constitutive reading of closure, which the parent theory argues for rather than proves (Gruber, 2026, Sections 3.4.3, 4.2.5). The explanatory gap is the complement of $S_{\mathrm{EWM}}$ in the set of substrate properties, those not drawn into the generation of the explicit models.

3. **Permeability modulates the constraint's boundary.** When permeability increases (psychedelics, meditation), previously implicit processes enter $S_{\mathrm{EWM}}$, expanding $O_{\mathrm{ESM}}$. This is why psychedelic states produce the subjective sense of "seeing behind the curtain" — the observability boundary temporarily shifts, exposing processing stages that are normally outside $S_{\mathrm{EWM}}$. The formalization predicts that the *content* of psychedelic insight should correspond to processes at the implicit-explicit boundary, not to arbitrary substrate-level processes.

In the model-space framework, the observability constraint becomes: the ESM (ρ at s ≈ 0, ν > $\nu_{\mathrm{crit}}$) can only represent properties of ρ that are themselves above $\nu_{\mathrm{crit}}$. Substrate-level properties (ν < $\nu_{\mathrm{crit}}$) are invisible to the ESM unless they are drawn into the generation of the explicit models through the selection family G.

### 6.3 Self-Referential Depth via Recursive Representation

Let Rep(A) denote the space of representations of A that the system can hold. Define $\Xi_0$ := $X_{\mathrm{EWM} \setminus \mathrm{ESM}}$, the state space of the closure partner, and for n ≥ 1, $\Xi_n$ := $X_{\mathrm{ESM}}$ × Rep($\Xi_{n-1}$). Depth-n self-modeling is a map

$\mu_{n}$: $X_{\mathrm{ESM}}$ → Rep($\Xi_n$),

so $\mu_0$ represents the world model, $\mu_1$ represents the ESM representing the world model, and so on. $\mu_0$ is the self model's half of the depth-0 coupling; closure (§6.4) adds the world model's half, and recursion adds rungs above it. The graduated levels of consciousness (Gruber, 2015, 2026) then formalize as:

| Level | Recursion depth | Description |
|---|---|---|
| Minimal consciousness | μ₀ | Rudimentary closure, hypothesized to hold among non-active explicit models (Gruber, 2026, Section 3.5); the self is mirrored in the world model it closes with without taking itself as an object; same depth as basic, poorer content |
| Basic consciousness | μ₀ | ESM and EWM∖ESM enter each other's update; the self-model is in the loop but does not take itself as an object (Gruber, 2026, Section 3.5) |
| Simply extended | μ₁ | The ESM additionally represents itself in that closure |
| Doubly extended | μ₂ | ESM represents itself representing itself in the closure |
| Triply extended | μ₃ | Third-order recursion; Meta-Problem arises here |

The **self-knowledge measure** quantifies how well the system predicts its own next state:

R = I(e(t+1); ê(t+1)) / H(e(t+1))

where ê(t+1) = $\pi_e$(e(t)) is a readout the system computes from its own ESM state, and e is discretized at the measurement resolution so that R ∈ [0, 1]. R = 1 means perfect self-prediction; R = 0 means no self-knowledge.

### 6.4 Self-Referential Closure as a Coupled Update

The most compact formalization makes closure a property of the update rules, not of a state. Let the joint explicit state be m = (e, w) ∈ $E \times \mathcal{W}$, with e the ESM state and w the state of the explicit world model outside the self model, EWM∖ESM (Gruber, 2026, Section 3.2); under the nesting, "the world model" in this section means this complement, since the whole EWM contains e and a coupling to it would be satisfied trivially through e's dependence on itself. Write $e_a = \Pi^{e}_{a}\, e$ for the active self model, the coordinates of e that enter the update of w, and $w_a = \Pi^{w}_{a}\, w$ for the active world model, the coordinates of w that enter the update of e, with $\Pi^{e}_{a}$ and $\Pi^{w}_{a}$ coordinate projections (Gruber, 2026, Section 3.3). The coupled update is

$\Psi_t$(e, w) = ($h_{e}$(e, $w_a$, u(t)), $h_{w}$(w, $e_a$, u(t))),

where u(t) collects sensory and substrate input. Self-referential closure holds over a window when the coupling is mutual and non-degenerate, $\partial h_e / \partial w_a \neq 0$ and $\partial h_w / \partial e_a \neq 0$ on the window: operationally, $e_a$ and $w_a$ each carry information about the other's next state beyond their own past, beyond their common input, and beyond arbitrary rotations of the same activity subspace (the null of §3.1). Closure is a property of $\Psi_t$ over an interval, not of a point; the trajectory need not be stationary, and a running experience has a changing state. $\chi_{\mathrm{act}}$ of §3.5 is the fraction of the activity at (s, ν) that lies in $e_a$ or $w_a$. A fixed point

Ψ(m\*) = m\*

is the stationary special case of closure, which the theory does not require; and closure is a necessary condition on consciousness here, not a sufficient one (§2.3; Gruber, 2026, Section 3, Principle 3).

The symbol is Ψ and not Φ, which denotes integrated information (Tononi, 2004): Ψ is a map between states of the explicit models, not a scalar quantity of integration, and no relationship between the two is asserted here. $E \times \mathcal{W}$ is the joint explicit state space, distinct from the model space M.

Separately, the self model may hold a representation r of the loop itself. The representational fixed point r\* = 𝔯(r\*) gives a self-description that reproduces itself; fixed points of self-reproducing maps of this kind are guaranteed under the hypotheses of Lawvere's theorem (Lawvere, 1969), read constructively through Kleene's recursion theorem (Gruber, 2026f, Section 5.1; cf. Kauffman, 1987), and this is the formal home of "the model and the modeled coincide". It establishes the existence of complete self-description, not an absence of an outside view. The parent theory's inside/outside asymmetry is a different thing: it concerns the act of generating, which does not appear in its own product, while past states and a complete description of the generator can (Gruber, 2026f, Section 7.1). Formalizing the asymmetry is therefore a limit on the current update step, not a property of m\* or of r\*, and whether such a statement follows from the coupled update is the open question of Phase 3.

The theory's claim that "the computation *is* the thing being computed" (Gruber, 2026, Section 3.4.3) is this mutual dependence: each model's current state is an argument of the other's update, so neither can be described as the modeled without also being the modeler. The category error the theory identifies, seeking phenomenality at the substrate level, becomes precise here: the phenomenal properties belong to the closed loop of $e_a$ and $w_a$, not to the substrate elements that compute Ψ. "Runs" here names the realized dependency of the trajectory's states on one another and nothing about how the process unfolds in time; the theory takes no stance on whether a complete stored record of the trajectory shares its experience (Gruber, 2026, Sections 3.4.5, 3.7.3).

### 6.5 Complexity Cost of Self-Reference

Self-referential modeling has a computational overhead. Let 𝒞(·) denote a fixed resource measure (number of units, or description length at the measurement resolution). For a system to achieve recursion depth n, its total complexity in that measure must satisfy:

$$\mathcal{C}_{\text{total}} \ge \sum_{k=0}^{n} \mathcal{C}_k + \text{overhead}(n)$$

where $\mathcal{C}_{k}$ is the resource required for level-k representation and the overhead grows with depth. This explains why triply-extended consciousness requires a large, complex substrate (human-scale cortex) while simpler organisms support only minimal or basic consciousness — they lack the resource for deeper recursion. The overhead can be paid in depth or in running time: a single ReLU recurrent network with fixed weights and fixed hidden dimension uniformly approximates every continuous function on [−1, 1] if run long enough, and minimax lower bounds show the runtime cannot be avoided (Abadie et al., 2026), so the bound above has a dual in latency. The 2015 monograph read the six-layer neocortex against the one-hidden-layer sufficiency of universal approximation (Cybenko, 1989) and assigned the surplus to recursive self-simulation (Gruber, 2015); the parent theory now treats the six layers as evolution's contingent implementation, not a requirement (Gruber, 2026, Section 4.4), and cortical laminae are not feedforward layers, so the comparison is an analogy, not an account of the overhead.

Closure also costs time. The loop is a simulation layer and runs slower than the substrate beneath it, so on reactive work it adds latency; the parent theory predicts that on tasks where reactive performance has plateaued and the payoff lies at a long horizon, performance rises with the simulation budget b, the time the system runs its model before acting, when closure is in place, and is flat in b when closure is ablated (Gruber, 2026, Section 4.2.4). Formally, $\partial\,\mathrm{perf}/\partial b > 0$ with closure and ≈ 0 without, at matched capacity; this is a price, not a barrier, and it is untested (Phase 4, prediction 4).

### 6.6 Self-Referential Closure and the Renormalization Group: An Analogy

A fourth approach is an analogy to renormalization, and its dependency comes first: if closure were an RG fixed point, scale invariance and a universality class would follow, and with them the closure ⇒ criticality chain that §4.4 leaves open, so the analogy inherits L1 and L2 and is a Phase-3 target, not a result. Wetterich (2022a, 2022b) showed that large classes of reversible cellular automata are equivalent to discretized fermionic quantum field theories — the probabilistic description of such an automaton *is* quantum mechanics. The equivalence is proven for globally reversible automata, the commitment the companion cosmology adopts for its substrate (Gruber, 2026c, Section 8.4); the cortical dynamics of Equation [1] are dissipative and driven, and whether the equivalence extends to them has not been checked, so no QFT dual is available for the cortical automaton as stated.

In QFT, an RG fixed point is a fixed point of a coarse-graining transformation acting on the space of effective theories (couplings): the dynamics are scale-invariant there, and the fixed point attracts along its irrelevant directions and repels along its finitely many relevant ones, and the relevant directions set its exponents (Wilson & Kogut, 1974). The analogy to closure is that a self-description which no further coarse-graining changes behaves like a fixed point of a scale transformation: at such a point the self-description would be the same at every level of recursion, and only the relevant parameters of the self-model would matter. Making it exact would require a coarse-graining map $\Psi_{\mathrm{RG}}$ on self-descriptions, distinct from the state update Ψ above, and a proof that the closed self-model is its fixed point; nothing here supplies either.

RG fixed points are well-studied objects with extensive machinery: critical exponents characterize the universality class, the number of relevant directions determines the predictive power, and the basin of attraction determines which initial conditions reach the fixed point. If the identification could be made, that apparatus would yield quantitative predictions about how perturbations from the fixed point (altered states, lesions, pharmacological interventions) affect the self-model. At an RG fixed point the description is the same at every scale; an outside description still exists and captures the structure, as it does in the parent theory.

The connection to the companion cosmology (Gruber, 2026c) is a conjecture: the cosmological fixed point Φ(U) = U (the universe computes its own structure; Φ is that paper's composition of holographic encoding with decompression, not integrated information) and the representational fixed point r\* = 𝔯(r\*) may be instances of one mathematical object, an RG fixed point, at different scales. Gruber (2026c) states the correspondence between the two closure structures, not between the two operators, limits it to the implicit/explicit axis and leaves identity open; with the reversibility question above, the QFT dual assumed here is a further conjecture.

---

## 7. Category-Theoretic Architecture

### 7.1 Two Categories

Category theory provides the most natural language for the theory's architectural claims because it is designed to formalize structural relationships between mathematical objects (Mac Lane, 1998; Tsuchiya, Taguchi, & Saigo, 2016).

Define two categories:

- **Sub** (Substrate): Objects are substrate states (W, x(t)). Morphisms are physical dynamics, the state transitions of Equation [1].
- **Sim** (Simulation): Objects are explicit-model states (EWM(t), ESM(t), or equivalently, the above-$\nu_{\mathrm{crit}}$ portion of ρ). Morphisms are the transitions of the explicit models, the images of Sub's transitions; they are phenomenal where they lie in the closed loop and preconscious elsewhere.

### 7.2 The Self-Simulation Functor

Self-simulation is a **functor** F: Sub → Sim that maps substrate dynamics to explicit-model dynamics while preserving compositional structure:

- F maps physical state transitions to transitions of the explicit models.
- F preserves composition: if substrate state A transitions to B and B to C, the explicit transition A→C is the composition of the explicit transitions A→B and B→C.

Consciousness is not F but a structure inside Sim: the closure of §6.4 between the active self model and the active world model, an endo-relation on the objects F produces. F is defined on unconscious substrate states too (deep NREM), which is why it is the generation functor and not consciousness. Sim's morphisms are the images of Sub's transitions and add no dynamics of their own; on that ground the theory declines the premise of the chip no-go theorem (Kleiner & Ludwig, 2024; Gruber, 2026, Section 7.3). Phenomenal change is the restriction of those morphisms to the closed loop. The real/virtual split is the distinction between Sub and the image of F. The theory's transformation of the Hard Problem becomes: seeking phenomenal properties in Sub is a category error because they are properties of that Sim-internal structure. F *generates* Sim from Sub, and Sim has properties (qualia, unity, selfhood) that do not exist as properties of Sub — just as the image of a functor can have properties not present in the domain.

### 7.3 Permeability as a Natural Transformation

Permeability is a parameter of the Sub objects (the selection state g ⊙ W), so an altered state is F applied to changed objects, not a second functor. A **natural transformation** η: $F_{\mathrm{normal}}$ ⇒ $F_{\mathrm{altered}}$ between self-simulation functors becomes available only if the functors are indexed by a fixed external parameter, the dose, held apart from the objects; it then expresses that the structural relationships are preserved under the change. That content appears in hierarchical order under psychedelics (V1 → V2/V3 → higher areas, not as random noise) is an empirical regularity about F's image, not a consequence of naturality, which is a commuting condition.

St Clere Smithe's (2024) structured active inference framework, which formalizes active inference using categorical systems theory and treats interfaces as compositional abstractions of Markov blankets, provides a directly applicable technical foundation. The FMT's implicit-explicit boundary could be modeled as a structured interface in this sense — a compositional boundary through which information flows, with the selection function g specifying the interface's permeability properties.

### 7.4 Forking as Coproduct

The theory's virtual model forking — the mechanism underlying dissociative identity disorder (Gruber, 2026, Section 6.2) — formalizes as a **coproduct** in the Sim category. The ESM state space in DID is the coproduct of alter state spaces,

E = $E_{1}$ ⊔ $E_{2}$ ⊔ ... ⊔ $E_{n}$

where ⊔ is the coproduct (disjoint union), one object with an injection from each summand; at each t the state ESM(t) lies in exactly one summand $E_{i(t)}$. This captures the claim that DID involves a single substrate running multiple ESM configurations, each constituting a distinct experiential self, alternating in control of the simulation (Gruber, 2026, Section 6.2).

---

## 8. Phased Build Order

The formalization project is substantial. A pragmatic build sequence, ordered by empirical accessibility and mathematical difficulty:

### Phase 1: Highest Priority (Directly Testable with Existing Data)

**Module 2 — Permeability as transfer entropy**: Compute conditioned transfer entropy from the implicit-mode signal $A_s$ to the explicit-mode signal $B_s$ of §3.1, estimated from the same recordings (the two modes share tissue and differ in mode, not location) at each scope position, against its surrogate and with the criteria of §2.6, across existing neuroimaging datasets from psychedelic, anesthesia, sleep, and meditation studies. Test the permeability profile predictions (Table 1) quantitatively. Transfer entropy estimation itself needs no new mathematical development (Wibral et al., 2014); the estimation of $A_s$ and $B_s$ does.

**Module 3 — Criticality signature mapping**: The branching ratio σ is already measured across states in the avalanche literature (Hengen & Shew, 2025; Algom & Shriki, 2026), and the edge-of-chaos coordinate across waking, propofol, LSD and generalized seizure by Toker et al. (2022). Map FMT's signature predictions onto existing datasets, and ask which of the two axes, if either, tracks consciousness across the remaining states.

### Phase 2: Core Formalism (Requires Dedicated Mathematical Work)

**Module 1 — Continuous model space**: Define the model density function ρ(s, ν, t) rigorously. Specify how to estimate ρ from neuroimaging data using representational similarity analysis (RSA), encoding models, and dimensionality reduction techniques (ICA, NMF). Build a minimal computational model (recurrent spiking network) and estimate ρ from its activity. Include the estimation cautions (emergent dimensionality, discretization artifacts, the nulls) and the principal bundle connection.

**Module 4 — ESM redirection**: Formalize the attractor-switching mechanism. Build a minimal recurrent model in which the self-model is an activity pattern identified by the criteria of §2.6, either found in the substrate's activity or seeded by construction, stated which, and demonstrate input-dependent identity switching under perturbation. Generate quantitative predictions for the salvinorin A controlled-input experiment (Gruber, 2026, Prediction 2, Section 8.3).

**Module 6 — Category-theoretic architecture**: The functor construction. Recent work on emergence from discrete substrates in physics — particularly Levin and Wen's (2005) string-net condensation and Wetterich's (2022a, 2022b) automaton-QFT equivalences — shows that the same categorical structures proposed here (functors, natural transformations, coproducts) appear independently as the canonical mathematical framework for formalizing emergence. This makes Module 6 a likely necessity rather than an elegant option: the categorical framework may be required to ensure that the other modules cohere. Collaboration with a category theorist who has consciousness theory exposure (cf. Tsuchiya et al., 2016; St Clere Smithe, 2024) is recommended. Module 6 sits in Phase 2 because the categorical framework should inform the construction of Modules 1 and 4, not be retrofitted after they are built.

### Phase 3: Deep Formalism (Hardest, Highest Potential Impact)

**Module 5 — Self-referential closure**: The coupled-update formalization. This requires working at the intersection of dynamical systems theory, mathematical logic, and — given the RG analogy — quantum field theory. Investigate whether the asymmetry of the current generating step can be given a formal statement distinct from the fixed point, whether the representational fixed point and the coupled update constrain each other, and whether the RG analogy can be made exact and then yield quantitative predictions about perturbations from the fixed point.

### Phase 4: Computational Validation

The formalization specifies quantities and dynamics; Phase 4 tests whether they produce the predicted behavioral signatures in a concrete computational system. The companion (Gruber, 2026d) reports mechanism demonstrations at toy, reservoir and gridworld scale, not a validation: prediction 1 below has been tested only in a gridworld agent whose self-model is a built module rather than emergent activity, prediction 2 only through reservoir scans on shallow memory-bound tasks, and predictions 3 and 4 not at all; parts of that record are under re-analysis. The specification below does not depend on those results. What Phase 4 can settle is whether the formalized quantities behave as the framework says they should.

**Implementation: Survival gridworld with architectural ablation.** A survival environment (hazards, resources, observable agent deaths) provides a natural testbed because observational learning — extracting causal structure from watching another agent die — is the kind of task on which the ESM-projection mechanism the formalization specifies is predicted to pay, within a sample budget, over reactive architectures of matched capacity. The FMT agent implements:

- **Four-model architecture**: IWM/ISM as learned substrate weights, EWM/ESM as running processes. In an emergent substrate the explicit models are activity, so an ablation targets the write/read path or the loop between self and world activity, never a labelled unit (Gruber, 2026, Section 3.2); the gridworld agent's ESM is a module by construction, so its ablation tests the architecture as a construction, not its emergence, and is labelled as such
- **Selection family G**: Multiple modulatory channels, not a single permeability knob
- **Reservoir computing substrate** with tunable spectral radius: the spectral radius tunes where the substrate's performance peaks; on the shallow, memory-bound tasks measured so far that peak lies in the driven-stable, ordered regime rather than at the edge (§4.4), and whether open-ended free modeling at depth needs a near-critical operating point is untested. Local homeostatic plasticity is an alternative to tuning a global parameter: it drives deep networks from sub- and supercritical starts toward a common critical state with a vanishing largest finite-time Lyapunov exponent (Vock & Meisel, 2026)
- **Observability constraint**: ESM bounded by EWM — the agent cannot know more about itself than its world model permits
- **Self-referential loop**: ESM and EWM∖ESM enter each other's update rules, the self model representing the system as the one doing the modeling (Gruber, 2026, Section 3.4.3); closure sits at depth μ₀ of §6.3, and deeper rungs (μ₁, μ₂) are optional arms that test recursion depth separately from closure

**Architectural ablation as the critical test.** Comparison architectures (flat RL, world-model-only, FMT-minus-ESM: the self–world coupling cut, or in the built-module agent the module removed, with the removal verified by the audit below) provide controlled ablations. The formalization generates four testable consequences:

1. **Cutting the self–world coupling produces a graded, capacity-relative behavioral cost** — setting the cross-terms of $h_e$ and $h_w$ to zero, or disconnecting the path that carries $\Pi_{\mathrm{ESM}} \cdot x(t)$ back into the dynamics, costs a measurable loss in sample efficiency on tasks requiring causal-structure extraction, widening with task horizon and with the richness of the model the intact agent can redeploy; on an architecture where the ESM is a module the test bears on that architecture, not on the activity reading of the theory. **The prediction is graded for a theoretical reason.** A finite closed loop run over a finite horizon can be unrolled into a feedforward computation with memory, so on a deterministic, episode-stationary task there is no capability a closed architecture has and its unrolled equivalent lacks; a clean binary loop-cut test cannot exist on such a task, and the framework's own commitments forbid predicting one. What survives the unrolling argument is a *price*: the unrolled equivalent must actually be built and paid for, and its cost grows with the horizon it must cover, so the licensed claim is an efficiency advantage within a budget. The falsifier is correspondingly a *magnitude* — an ablated agent matching the intact one in sample efficiency at equal capacity and matched task performance would refute the claim, whereas an ablated agent that merely takes longer would not.
2. **Loss of free modeling degrades self-referential processing** — as the substrate's open-ended capability, measured by the novel-input probe of §2.7, is removed (a contracting, memoryless regime or chaos), observational learning should degrade correspondingly; whether depth needs a near-critical operating point is open. The claim is a price: no architecture is asserted to be incapable of the task, and the prediction is about how steeply performance falls with the capability, measured against matched controls at equal capacity.
3. **EWM coverage ablation degrades ESM proportionally** — reducing what the world model represents should directly limit what the self-model can represent about itself (observability constraint).
4. **Capability scales with the simulation budget under closure and stops scaling when the coupling is cut** — on tasks where reactive performance has plateaued and the payoff lies at a long horizon, performance rises with the time the agent runs its model before acting when closure is in place, and is flat in that budget when the coupling is cut, at matched capacity (Gruber, 2026, Section 4.2.4). The claim is a price, not a barrier.

**Ablation-validity audit: a precondition on reading any of these results.** Prediction 1 operationalizes ablation as the removal of a mechanism, and on a recurrent substrate that operationalization can silently fail: an ablation can relocate a loop instead of removing it, in which case the manipulation contrasts *closure here* against *closure there*, and a tie between conditions is then the predicted observation. Any ablation protocol must therefore verify removal — for example by connectivity analysis of both arms, decomposing the effective connectivity of each into strongly-connected components and reporting the counts, and by checking explicitly that the mechanism the ablation was intended to remove has not reconstituted elsewhere in the remaining tissue. This audit is a requirement on the Phase 4 protocol, completed **before** the outcome measures are read. Where removal cannot be shown, the manipulation is properly described as *disconnection of one labelled component*, and the prediction it tests is correspondingly narrower. The audit must also show that the two arms sit at a matched operating point; where disabling closure yields two closed systems, or shifts the operating point, the contrast is between two forms of closure and tests nothing about its absence. If these predictions hold, the formal structure captures computational distinctions; if they fail, they name the formal commitment that is wrong.

**Framing constraint**: The gridworld validates architectural claims, not consciousness claims. It can demonstrate that FMT-architecture agents produce qualitatively different behavioral signatures; it cannot demonstrate that either architecture constitutes consciousness.

---

## 9. Scope and Limits

### 9.1 Contributions

**Constraint**: Verbal descriptions are flexible enough to accommodate post-hoc explanations. The Fokker-Planck dynamics, the transfer entropy measures, and the attractor-switching model commit to specific functional forms that can be empirically wrong.

**Quantitative predictions**: "Permeability increases under psychedelics" becomes "Implicit-to-explicit transfer entropy at scope s increases by factor k at dose d", which a number can falsify.

**Simulation**: A formalized theory can be implemented in code. Predictions can be tested computationally before committing to expensive neuroimaging experiments.

**Interoperability**: The transfer entropy measure connects to Predictive Processing's information-theoretic tools. The branching ratio connects to ConCrit. The category-theoretic framework connects to St Clere Smithe's structured active inference. Formalization turns FMT from an isolated framework into something interoperable with the rest of the field.

**Sharpened transformation of the Hard Problem**: The closure formalization either succeeds or fails. If the coupled-update condition of §6.4 can be shown to entail a formal statement of the inside/outside asymmetry, that is a philosophical result in its own right.

**Bridge to physics**: The mathematical structures this formalization program requires — functors between categories, fixed points of self-referential maps, phase transitions in graph connectivity, renormalization group flows — are independently the canonical tools for formalizing emergence from discrete substrates in fundamental physics. Wetterich's (2022a, 2022b) automaton-QFT equivalences use functorial mappings; Levin and Wen's (2005) string-net condensation uses tensor category theory; Quantum Graphity (Konopka et al., 2008) uses graph phase transitions. The companion cosmological model (Gruber, 2026c) proposes a structural correspondence, limited to the implicit/explicit axis, and leaves open whether it is an identity. If it holds, the FMT formalization and the physics of discrete emergence describe the same mathematical structures, and progress on either informs the other.

### 9.2 Limits

The formalization does not derive phenomenality from mathematics.

The model-space approach introduces a further limitation: the model density ρ(s, ν, t) is a statistical description of something that may not be cleanly decomposable. The brain may not implement "models" in any separable sense — the activity patterns we decompose via ICA or NMF may be artifacts of our decomposition method rather than natural kinds. The formalization should therefore be understood as a measurement framework that makes the theory testable, not as a claim that the brain literally implements a model density function.

---

## 10. Conclusion

The Four-Model Theory requires mathematical formalization to constrain its claims, generate quantitative predictions, and interface with the existing formal landscape of consciousness science. The correct formalization strategy must respect the theory's own commitment: the four canonical model kinds are the minimum set the architecture forces, not an exhaustive enumeration. The biological substrate implements an effectively uncountable ecology of models, and the formalization must be statistical rather than enumerative.

The continuous model-space framework — with scope and mode as continuous axes, the virtual/non-virtual split as a threshold on the mode axis, and the Fokker-Planck equation governing the density dynamics on each side of that threshold — provides the necessary mathematical language. Combined with transfer entropy for permeability, established criticality measures, attractor dynamics for ESM redirection, the coupled-update condition for self-referential closure (with the observability constraint and the renormalization analogy), and a graph-theoretic characterization of the implicit-explicit threshold, the framework generates quantitative predictions that are testable with existing neuroimaging methods and computational models.

The formalization project is substantial but modular. Phase 1 (transfer entropy estimation and criticality mapping) can proceed once the implicit and explicit signals can be estimated from existing data. Phase 2 places the category-theoretic architecture beside the model-space and ESM modules. Phase 3 (self-referential closure) has the renormalization analogy as one candidate route. Phase 4 (computational tests) asks whether the formalized theory's dynamics behave as predicted.

This paper specifies the formal framework. The companion (Gruber, 2026d) reports the in-silico tests to date, mechanism demonstrations and not a validation; the specification does not depend on them. The remaining formal modules (Phases 2-3) require mathematically trained collaborators. Some of these formalizations may show the theory to be wrong in specific, identifiable ways.

---

## References

Aaronson, S. (2014, May 21). Why I am not an integrated information theorist (or, The unconscious expander). *Shtetl-Optimized*. https://scottaaronson.blog/?p=1799

Abadie, V., Hutter, C., & Bölcskei, H. (2026). Recurrent neural networks approximate continuous functions. *arXiv*. https://doi.org/10.48550/arXiv.2606.20325

Albantakis, L., Barbosa, L., Findlay, G., Grasso, M., Haun, A. M., Marshall, W., Mayner, W. G. P., Zaeemzadeh, A., Boly, M., Juel, B. E., Sasai, S., Fujii, K., David, I., Hendren, J., Lang, J. P., & Tononi, G. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms. *PLOS Computational Biology*, 19(10), e1011465. https://doi.org/10.1371/journal.pcbi.1011465

Algom, I., & Shriki, O. (2026). The ConCrit framework: Critical brain dynamics as a unifying mechanistic framework for theories of consciousness. *Neuroscience & Biobehavioral Reviews*, 180, 106483. https://doi.org/10.1016/j.neubiorev.2025.106483

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

Gruber, M. (2015). *Die Emergenz des Bewusstseins*. Lulu Press. ISBN 978-1-326-65207-4. https://doi.org/10.5281/zenodo.23538664

Gruber, M. (2026). The Four-Model Theory of Consciousness: A Simulation-Based Framework Unifying the Hard Problem, Binding, and Altered States. *Zenodo* preprint. https://doi.org/10.5281/zenodo.18669891

Gruber, M. (2026c). Emergent spacetime from self-referential computation: A hierarchical cellular automaton framework. *Zenodo* preprint. https://doi.org/10.5281/zenodo.18698605

Gruber, M. (2026d). In-silico tests of the four-model architecture: Self-referential closure, self-modelling and criticality in model systems. *Zenodo* preprint. https://doi.org/10.5281/zenodo.21610993

Gruber, M. (2026f). *No Outside: The Limits of Mathematics and Logic From Any First-Person Perspective*. Zenodo. https://doi.org/10.5281/zenodo.23473517

Hardstone, R., et al. (2012). Detrended fluctuation analysis: a scale-free view on neuronal oscillations. *Frontiers in Physiology*, 3, 450.

Haruna, T., & Nakajima, K. (2019). Optimal short-term memory before the edge of chaos in driven random recurrent networks. *Physical Review E*, *100*(6), 062312. https://doi.org/10.1103/PhysRevE.100.062312

Hengen, K. B., & Shew, W. L. (2025). Is criticality a unified setpoint of brain function? *Neuron*. https://doi.org/10.1016/j.neuron.2025.05.020

Hu, F., Angelatos, G., Khan, S. A., Vives, M., Türeci, E., Bello, L., Rowlands, G. E., Ribeill, G. J., & Türeci, H. E. (2023). Tackling sampling noise in physical systems for machine learning applications: Fundamental limits and eigentasks. *Physical Review X*, *13*(4), 041020. https://doi.org/10.1103/PhysRevX.13.041020

Jacobus, C. (2026). Finding the edge of chaos in a ferromagnet: Quantifying the "complexity" of 2D Ising phase transitions with image compression. *arXiv*. https://doi.org/10.48550/arXiv.2602.15185

Kanders, K., Lorimer, T., & Stoop, R. (2017). Avalanche and edge-of-chaos criticality do not necessarily co-occur in neural networks. *Chaos*, 27(4), 047408.

Kauffman, L. H. (1987). Self-reference and recursive forms. *Journal of Social and Biological Structures*, 10(1), 53–72. https://doi.org/10.1016/0140-1750(87)90034-0

Kleiner, J., & Ludwig, T. (2024). The case for neurons: A no-go theorem for consciousness on a chip. *Neuroscience of Consciousness*, 2024(1), niae037. https://doi.org/10.1093/nc/niae037

Konopka, T., Markopoulou, F., & Smolin, L. (2008). Quantum Graphity: A model of emergent locality. *Physical Review D*, 77(10), 104029.

Lawvere, F. W. (1969). Diagonal arguments and Cartesian closed categories. *Lecture Notes in Mathematics*, 92, 134–145.

Lempel, A., & Ziv, J. (1976). On the complexity of finite sequences. *IEEE Transactions on Information Theory*, 22(1), 75–81.

Levin, M. A., & Wen, X.-G. (2005). String-net condensation: A physical mechanism for topological phases. *Physical Review B*, 71(4), 045110.

Lizier, J. T., Prokopenko, M., & Zomaya, A. Y. (2008). Local information transfer as a spatiotemporal filter for complex systems. *Physical Review E*, 77(2), 026110. https://doi.org/10.1103/PhysRevE.77.026110

London, M., Roth, A., Beeren, L., Häusser, M., & Latham, P. E. (2010). Sensitivity to perturbations in vivo implies high noise and suggests rate coding in cortex. *Nature*, *466*(7302), 123–127. https://doi.org/10.1038/nature09086

Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer.

Maqueda, A. E., Valle, M., Addy, P. H., Antonijoan, R. M., Puntes, M., Coimbra, J., Ballester, M. R., Garrido, M., González, M., Claramunt, J., Barker, S., Johnson, M. W., Griffiths, R. R., & Riba, J. (2015). Salvinorin-A induces intense dissociative effects, blocking external sensory perception and modulating interoception and sense of body ownership in humans. *International Journal of Neuropsychopharmacology*, 18(12), pyv065. https://doi.org/10.1093/ijnp/pyv065

Meisel, C., Storch, A., Hallmeyer-Elgner, S., Bullmore, E., & Gross, T. (2012). Failure of adaptive self-organized criticality during epileptic seizure attacks. *PLoS Computational Biology*, 8(1), e1002312. https://doi.org/10.1371/journal.pcbi.1002312

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

Toker, D., Pappas, I., Lendner, J. D., Frohlich, J., Mateos, D. M., Muthukumaraswamy, S., Carhart-Harris, R., Paff, M., Vespa, P. M., Monti, M. M., Sommer, F. T., Knight, R. T., & D'Esposito, M. (2022). Consciousness is supported by near-critical slow cortical electrodynamics. *Proceedings of the National Academy of Sciences*, 119(7), e2024455119. https://doi.org/10.1073/pnas.2024455119

Tononi, G., Sporns, O., & Edelman, G. M. (1994). A measure for brain complexity: relating functional segregation and integration in the nervous system. *Proceedings of the National Academy of Sciences*, 91(11), 5033–5037.

Tononi, G. (2004). An information integration theory of consciousness. *BMC Neuroscience*, 5, 42.

Truccolo, W., Donoghue, J. A., Hochberg, L. R., Eskandar, E. N., Madsen, J. R., Anderson, W. S., Brown, E. N., Halgren, E., & Cash, S. S. (2011). Single-neuron dynamics in human focal epilepsy. *Nature Neuroscience*, 14(5), 635–641. https://doi.org/10.1038/nn.2782

Tsuchiya, N., Taguchi, S., & Saigo, H. (2016). Using category theory to assess the relationship between consciousness and integrated information theory. *Neuroscience Research*, 107, 1–7.

Vicente, R., Wibral, M., Lindner, M., & Pipa, G. (2011). Transfer entropy — a model-free measure of effective connectivity for the neurosciences. *Journal of Computational Neuroscience*, 30(1), 45–67.

Vock, S., & Meisel, C. (2026). Adaptive self-organized criticality in deep neural networks. *arXiv*. https://doi.org/10.48550/arXiv.2608.28431

Wibral, M., Vicente, R., & Lizier, J. T. (Eds.). (2014). *Directed Information Measures in Neuroscience*. Springer.

Wetterich, C. (2022a). Fermion picture for cellular automata. *arXiv preprint*, arXiv:2203.14081.

Wetterich, C. (2022b). Fermionic quantum field theories as probabilistic cellular automata. *Physical Review D*, 105(7), 074502.

Wilson, K. G., & Kogut, J. (1974). The renormalization group and the ε expansion. *Physics Reports*, 12(2), 75–199.

Wolfram, S. (2002). *A New Kind of Science*. Wolfram Media.

Xiao, H., Zhao, X., Zhou, H., & Wang, W. (2026). Efficient coding under constraint drives neural systems towards criticality and sloppiness. *arXiv*. https://doi.org/10.48550/arXiv.2605.22598

Zenil, H. (2010). Compression-based investigation of the dynamical properties of cellular automata and other systems. *Complex Systems*, 19(1), 1–28. https://doi.org/10.25088/complexsystems.19.1.1
