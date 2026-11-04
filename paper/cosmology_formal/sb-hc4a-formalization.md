# Toward a Mathematical Formalization of the SB-HC4A Cosmological Model: A Recommended Approach

**Matthias Gruber**

*Independent researcher*

*ORCID: 0009-0005-9697-1665*

*Correspondence: research@matthiasgruber.com*

---

## Abstract

The Singularity-Bounded Holographic Class 4 Automaton (SB-HC4A; Gruber, 2026a) proposes that the universe is a self-referential holographic Class 4 automaton bounded at every scale by singularity surfaces — information-impermeable boundaries of maximum density — where the observable interior is a decompressed projection of boundary-encoded information. The model was derived from a convergence of the Five-Class computational taxonomy, a theoretical framework for self-referential computation in self-modeling systems (Gruber, 2015, 2026b, 2026c), and 't Hooft's (1993, 2016) holographic automaton interpretation — now supported by Wetterich's (2022a, 2022b, 2022c) proven mathematical equivalences between cellular automata and fermionic quantum field theories, including a cellular automaton model of spinor gravity in four dimensions with exact local Lorentz symmetry. The model currently operates in natural language supplemented by structural arguments. This paper outlines a recommended mathematical formalization strategy. Nine formalization modules are proposed: (1) a measure-theoretic definition of the five computational classes replacing Wolfram's visual classification, (2) a topological characterization of singularity boundaries as equivalence classes of Bekenstein-saturated surfaces — including their temporal boundary structure (a three-mode no-arrival taxonomy) and the identification of the emptied late universe as a holographically saturated singularity implying cyclic dynamics, (3) a formal definition of holographic rule sets via dimensional compression operators, (4) the James-Stein Inadmissibility Conjecture grounding quantum entanglement as estimation inadmissibility on shared Bekenstein-saturated substrates — connecting the holographic output claim to the Stein effect via the quantum Fisher information metric, Brown's (1971) admissibility theory, and the identification of the vacuum state with the shrinkage target, (5) the self-referential fixed point Φ(U) = U grounded in Lawvere's fixed-point theorem and the theory of coalgebras — extended to cyclic temporal closure with cycle sequences conjectured to be computationally irreducible, possible CPT signature alternation connecting to the CPT-symmetric universe model of Boyle, Finn and Turok, and a generalization to branching cycles under Big Rip (Caldwell, 2002) scenarios where distributed singularity boundaries produce a multi-valued cycle map, (6) the cross-scale structural correspondence as a functor between categories, (7) the necessity argument in modal logic, (8) energy-information equivalence as a duality principle, and (9) the cognitive ceiling problem formalized as a computability-theoretic bound on self-knowledge. A phased build order prioritizes components that interface with existing mathematical physics. The formalization is offered as a research program specification for mathematically trained collaborators; verification of the formal apparatus is explicitly deferred to domain experts.

**Keywords**: cosmology, cellular automata, holographic principle, formalization, criticality, singularity, self-referential closure, fixed-point theory, category theory, modal logic, Bekenstein bound, cyclic cosmology, CPT symmetry, conformal cyclic cosmology, Big Rip, phantom energy, branching multiverse, James-Stein estimator, quantum entanglement, estimation inadmissibility

---

## 1. Introduction

### 1.1 The Formalization Gap

The SB-HC4A cosmological model (Gruber, 2026a) makes five structural claims: (a) the universe operates at Wolfram Class 4 — the edge of chaos; (b) singularities at every physical scale (Planck regime, particle interiors, event horizons, cosmological horizons, temporal endpoints) are structurally identical instances of the same information boundary; (c) the universe is a holographic Class 4 automaton whose rules, dynamics, and output are all holographic; (d) this architecture is self-referentially closed: Φ(U) = U; and (e) self-referential computational systems, including self-modeling cognitive systems (Gruber, 2015, 2026b), are local, scale-reduced instances of the same computational pattern.

These claims are currently expressed in natural language with structural arguments. The elimination argument for Class 4 is informal. The singularity unification is asserted by shared properties, not by a formal equivalence relation. The holographic rule set is defined verbally. The self-referential fixed point is stated but not derived. The cross-scale structural mapping is presented as a table of correspondences, not as a mathematical morphism.

Without formalization, the model's flexibility is a liability. A verbally specified "structural identity" between self-referential computation and cosmology could potentially accommodate any observation post hoc. The necessity argument — that, given a deterministic substrate, the five axioms select the SB-HC4A architecture class — requires formal demonstration, not verbal persuasion. And the cognitive ceiling problem (Weak Point 5 of Gruber, 2026a) — that Class 4 observers may be constitutionally incapable of determining whether they are describing the universe or the limits of their own cognition — needs formal characterization before it can be analyzed.

### 1.2 The Three-Paper Formalization Program

This paper is the third in a series of formalization specifications. The first (Gruber, 2026c) specified the formalization of the self-referential computation framework (Gruber, 2026b), proposing a continuous model-space framework with a model density ρ(s, ν, t), transfer entropy for permeability, criticality operationalization, ESM redirection dynamics, self-referential closure as a fixed point, and category-theoretic architecture. The second (Gruber, 2026d) specified the formalization of the Recursive Intelligence Model, proposing a domain-structured knowledge manifold, motivation as a self-referential computation functional, coupled stochastic differential equations, the ignition threshold as a stochastic bifurcation, and social coupling dynamics.

The present paper addresses the cosmological level. The three formalizations are not independent — the self-referential computation formalization provides the cognitive-side apparatus that the cosmology formalization must map onto, and the RIM formalization provides the intermediate-scale dynamics that connect self-referential representation to the learning processes that produce cosmological models. The full theoretical architecture, once formalized, forms a three-level system: cosmological substrate → self-referential computation → intelligence, with mathematical morphisms connecting each level. The self-referential computation framework draws substantially on Metzinger's (2003) self-model theory of subjectivity, and the cosmological-level seeds — the universe as a cellular automaton under holographic constraints — were already present in Gruber (2015), though the full SB-HC4A model was not developed until Gruber (2026a).

### 1.3 Scope and Limitations

This paper specifies a formalization research program. It proposes mathematical frameworks, defines quantities, and outlines a build order. It does *not* verify the mathematical apparatus — the author is not a mathematician, and formal verification is explicitly deferred to domain experts. The equations and formal structures presented here are intended as precise specifications of *what needs to be formalized* and *which mathematical tools are appropriate*, not as proven theorems.

The challenge is acute. The cosmological model touches mathematical physics (general relativity, quantum field theory, holographic duality), theoretical computer science (computational complexity, automata theory, Kolmogorov complexity), mathematical logic (fixed-point theorems, incompleteness, modal logic), and category theory. No single mathematician commands all these domains. The formalization is therefore designed as a modular program where each module can be developed independently by domain specialists, with category theory providing the integration language.

The paper is structured as follows. Section 2 proposes measure-theoretic definitions of the five computational classes. Section 3 formalizes singularity boundaries, including their temporal asymptotic structure, the identification of the emptied late universe as a holographically saturated singularity, and the formalization of particles as computational atoms — stable Planck-scale singularity configurations whose finiteness, discreteness, interaction grammar, and charge and angular-momentum conservation follow from the boundary capacity bound. Section 4 defines holographic rule sets and formalizes entanglement as estimation inadmissibility on shared Bekenstein-saturated substrates via the James-Stein Inadmissibility Conjecture. Section 5 addresses self-referential closure, including cyclic temporal dynamics, CPT signature alternation across cycles, and the generalization to branching cycles under Big Rip scenarios. Section 6 constructs the cross-scale structural identity functor. Section 7 formalizes the necessity argument. Section 8 addresses energy-information equivalence. Section 9 formalizes the cognitive ceiling. Section 10 proposes a phased build order. Section 11 identifies what formalization would and would not deliver.

---

## 2. Formalizing the Five Computational Classes

### 2.1 The Problem with Wolfram's Classification

Wolfram's (2002) four-class taxonomy of cellular automaton behavior — static, periodic, random, complex — is empirical: classes are assigned by visual inspection of space-time diagrams. This is scientifically useful for classification but mathematically unsatisfying. The classes lack formal definitions, the boundaries between classes are imprecise, and the extension to continuous, noisy, high-dimensional systems (like the physical universe) is undefined.

The five-class refinement (Gruber, 2015, 2026a) — splitting Wolfram's Class 3 by reducibility: reducible fractals form the new Class 3, irreducible deterministic rules (Rule 30) join Class 4, and Class 5 is reserved for ontic randomness generated by no expressible rule — sharpens the taxonomy but inherits the informality. For the SB-HC4A to be a mathematical object, each class needs a formal definition.

Algorithmic-information classifications of cellular automata already exist. Dubacq, Durand and Formenti (2001) classify rules by the Kolmogorov complexity of their rule tables. Zenil (2010) classifies them by the compressibility of their space-time evolutions, and Zenil and Villarreal-Zapata (2013) define the Wolfram class of a rule as a limit over initial conditions and runtime, a definition under which class membership is uncomputable because Kolmogorov complexity is. Culik and Yu (1988) had shown earlier that membership in Wolfram-style classes is undecidable. Three results from this work constrain the definitions below. Compressibility separates Wolfram's Classes 3 and 4 from Classes 1 and 2, but it does not separate complex from random-looking behaviour: rule 110 compresses no better than rules 30 and 45 (Zenil, 2010). The compressibility of an orbit belongs to the rule together with its initial condition, and the same rule can fall into different classes from different initial conditions, as rule 22 does (Zenil & Villarreal-Zapata, 2013). And no sharp, computable class boundary is available. Each class is therefore defined below as a limiting property, to be estimated by a computable approximation whose error is stated.

### 2.2 Proposed Measure-Theoretic Definitions

Consider a discrete dynamical system Σ = (S, f, s₀) where S is the state space, f: S → S is the transition function, and s₀ is the initial state. The orbit of s₀ under f is the sequence O = {s₀, f(s₀), f²(s₀), ...}. Define the following quantities:

**Topological entropy** $h_{\mathrm{top}}$(f): The exponential growth rate of the number of distinguishable orbits as resolution increases (Adler, Konheim, & McAndrew, 1965). Measures the "complexity" of the dynamics.

**Kolmogorov complexity rate** $\kappa_{\mu}$(f): The asymptotic Kolmogorov complexity per symbol of orbits started from μ-typical initial conditions, for an invariant measure μ. Along almost every orbit it equals the metric entropy $h_{\mu}$(f) (Brudno, 1978). It is a property of the pair (f, μ), not of f alone, and it is zero along the orbit of any computable initial condition (Section 2.4). Measures how much randomness an orbit carries.

**Logical depth** d(Σ): The running time of the near-shortest programs that output finite space-time windows of the orbit, as a function of window size (Bennett, 1990). A random window is shallow, because printing it is both its shortest and its fastest description; a periodic or nested window is shallow, because a short program produces it quickly. Depth is large only when the shortest description of the window has to be run for a long time. Measures structured complexity.

**Lyapunov exponent** $\lambda_{\max}$: The maximum exponential divergence rate of nearby trajectories. Measures sensitivity to initial conditions.

**Computational reducibility** r(Σ): Whether the state at time t can be computed in fewer than t steps. Formally: r(Σ) = 1 if there exists an algorithm A such that A(s₀, t) = f^t(s₀) in time o(t); r(Σ) = 0 otherwise.

**Computational universality** u(Σ): Whether the system can simulate any Turing machine. u(Σ) = 1 if Σ is Turing-complete; u(Σ) = 0 otherwise.

The five classes are then defined by their signatures on these quantities:

| Class | $h_{\mathrm{top}}$ | d(Σ) | $\lambda_{\max}$ | r(Σ) | u(Σ) | Informal |
|:--------:|:--------:|:------------------:|:------------------:|:------:|:------:|---------------------------|
| 1 | 0 | bounded | < 0 | 1 | 0 | Static: converges to fixed point |
| 2 | 0 | bounded | ≤ 0 | 1 | 0 | Periodic: finite-period orbits |
| 3 | > 0 | bounded | ≤ 0 | 1 | 0 | Fractal: self-similar, reducible |
| 4 | > 0 | unbounded | ≈ 0 (band) | 0 | 1 | Complex: irreducible, universal |
| 5 | max | bounded | > 0 | 0 | 0 | Random: maximal complexity, no structure |

The complexity rate $\kappa_{\mu}$ is not a column. From typical initial conditions it is positive for the additive Rule 90 as it is for Rule 30, so it does not separate Class 3 from Classes 4 and 5; from computable initial conditions it is zero for all five. The defining criteria are reducibility and universality. Depth is the output-side signature of the same distinction, and it is the quantity the expressibility argument of Section 2.4 is stated in; the Class 4 entry in the depth column is that section's conjecture.

### 2.3 Key Distinctions

**Class 3 vs. Class 4**: Both have positive topological entropy, but Class 3 is computationally reducible (r = 1) while Class 4 is not. This captures the intuition that fractal systems, however visually complex, are "shortcuttable" — you can compute the Sierpinski triangle's state at time 10^100 without running 10^100 steps, because the structure is self-similar and the rule is algebraically tractable (Wolfram, 2002, p. 870). Class 4 systems resist this: Rule 110 cannot be shortcut (Cook, 2004).

**Class 4 vs. Class 5**: Class 4 is computationally irreducible; Class 5 is non-algorithmic, a stronger condition than irreducibility. Class 4 is computationally universal (u = 1) while Class 5 is not. A truly random system cannot simulate a specific Turing machine because simulation requires deterministic control over the output — which contradicts maximal Kolmogorov complexity. Class 4 achieves maximum *structured* complexity; Class 5 achieves maximum *unstructured* complexity.

Depth expresses the same line on the output: a Class 5 orbit is incompressible and therefore shallow, while a Class 4 orbit is conjectured to grow in depth without bound. Compressibility cannot draw this line (Section 2.1). An empirical measure that does is the transition coefficient C of Zenil (2010), a compression-based analogue of a Lyapunov exponent that measures how the compressed length of an evolution changes across neighbouring initial conditions. On the elementary cellular automata, rule 110 has C > 0 while rules 30 and 1 have C ≈ 0, so random-looking behaviour groups with trivial behaviour on C. Zenil (2010, §5.2.1) conjectures that universality implies C > 0. The conjecture rests on elementary-CA evidence computed with a general-purpose compressor; whether it holds in the limit, and with a compressor-independent estimator, is open. If it does, C is a computable candidate for the Class 4/5 boundary.

**The Lyapunov signature**: Class 4 has $\lambda_{\max}$ ≈ 0 (edge of chaos), which is the formal expression of Langton's (1990) observation that Class 4 lives at the boundary between order ($\lambda_{\max}$ < 0) and chaos ($\lambda_{\max}$ > 0). Class 5 has $\lambda_{\max}$ > 0 — sensitivity to initial conditions without the structured information processing that characterizes Class 4.

Two qualifications on this signature, both of which matter for how the criterion is applied. First, **Class 4 is a band, not a knife-edge point.** The defining criteria are irreducibility (r = 0) and universality (u = 1); $\lambda_{\max}$ ≈ 0 is the signature that regime typically presents, not a value the system must hit. Requiring a system to sit at an exact critical value would make Class 4 a measure-zero set, which no physical system could occupy and no measurement could confirm — and it is not what the expressibility argument of Section 2.4 requires. Second, **$\lambda_{\max}$ and the branching ratio σ are distinct diagnostics with distinct critical values in the same system, and they must not be read as one condition.** In measured recurrent substrates the nominal σ = 1 point and the $\lambda_{\max}$ = 0 point are separated by a wide margin, and computational capacity can peak well inside the ordered side of the band rather than at the Lyapunov edge. Where a criticality signature is used as evidence, the diagnostic and its critical value must therefore be named explicitly.

### 2.4 The Class 4 Expressibility Ceiling

The cosmological model's first premise is that Class 4 is the maximum complexity achievable by expressible rules. Stating it formally requires two facts to be kept apart: incompressibility can enter an orbit through its initial condition, and incompressibility is a different quantity from structured complexity.

**Proposition (finite descriptions give compressible orbits).** Let Σ = (S, f, s₀) have a transition function f with a finite description of length L and a computable initial condition s₀ with description length K(s₀). The Kolmogorov complexity of the first t steps of the orbit is at most L + K(s₀) + O(log t), so the complexity rate of the orbit tends to 0 as t → ∞.

The orbit compresses to "apply rule f to s₀ for t steps." The bound holds in every class, Class 4 included, so it cannot by itself separate Class 4 from anything. The condition on s₀ is necessary. The shift map has a one-line rule, and started from a Martin-Löf random configuration it produces an orbit of maximal complexity rate, as Brudno's (1978) theorem requires of any system with positive metric entropy. A finite rule can therefore produce maximally incompressible output when its initial data are themselves inexpressible. Class 5 randomness enters through an inexpressible rule or through inexpressible initial data; a finite rule acting on finite data does not produce it.

**Conjecture (Expressibility Ceiling).** Among systems with a finite rule and a computable initial condition, orbits whose logical depth grows without bound occur only in systems that are computationally irreducible and universal, that is, in Class 4.

The ceiling is thereby placed in structured complexity, measured by depth. The open direction is the converse: an irreducible system that is not universal might also produce unbounded depth, and whether such systems exist decides whether the ceiling is exactly Class 4. Neither class membership nor the depth of a given orbit is computable (Culik & Yu, 1988; Bennett, 1990; Zenil & Villarreal-Zapata, 2013), so the deliverable for this module is a definition of each class in the limit together with a computable approximation and its error, not a decision procedure.

The Proposition is elementary. The Conjecture needs formulation by a computability theorist; the relevant tools are algorithmic information theory (Downey & Hirschfeldt, 2010), the theory of computable measures (Zvonkin & Levin, 1970), and the theory of logical depth (Bennett, 1990).

### 2.5 Extension to Continuous Systems

The physical universe is not a discrete cellular automaton — it is (at least approximately) a continuous dynamical system on a field-theoretic state space. The five-class definitions must extend to this setting.

The key observation: the measures ($h_{\mathrm{top}}$, $\kappa_{\mu}$, d, $\lambda_{\max}$, r, u) are all defined for continuous dynamical systems, not just discrete automata:

- Topological entropy extends to flows (Bowen, 1971).
- Kolmogorov complexity rate extends via the theory of algorithmic randomness for real-valued sequences (Hertling & Weihrauch, 2003).
- Logical depth applies to any discretised trajectory, as the depth of its finite prefixes (Bennett, 1990).
- Lyapunov exponents are standard for ODEs and PDEs (Eckmann & Ruelle, 1985).
- Computational reducibility extends to the computability of solutions: can the state at time t be computed without integrating through all intermediate times? (Pour-El & Richards, 1989).
- Computational universality for continuous systems: certain PDEs are Turing-complete (Moore, 1991; Cardona et al., 2021).

The classification table (Section 2.2) therefore applies directly to continuous systems, with the caveat that the measures are harder to compute and the class boundaries become less sharp (continuous systems may interpolate between classes in parameter space, with Class 4 occupying a critical manifold between the ordered and chaotic phases).

### 2.6 The Containment Hierarchy

The verbal model claims that Class 4 contains all classes — including itself — as subprocesses. Formally:

**Claim (Downward Containment).** Let Σ₄ be a Class 4 system. For each k ∈ {1, 2, 3}, there exists a subsystem $\Sigma_{k}$ ⊂ Σ₄ and a projection $\pi_{k}$ such that $\pi_{k}$(Σ₄) is Class k.

This follows from computational universality: a Turing-complete system can simulate any computable dynamics, including Class 1 (constant output), Class 2 (periodic output), and Class 3 (fractal/reducible output). The Game of Life demonstrates this concretely — it contains still lifes (Class 1), oscillators (Class 2), and self-similar growth patterns (Class 3) as embedded phenomena.

**Claim (Self-Containment).** Let Σ₄ be a Class 4 system with sufficient resources. There exists a subsystem Σ₄' ⊂ Σ₄ such that Σ₄' is itself Class 4 — Turing-complete, capable of sustaining open-ended computation, and capable of containing further Class 4 subsystems within its own dynamics.

This also follows from universality: a Turing-complete system can simulate any Turing machine, including another Turing-complete system (Cook, 2004). The contained instance Σ₄' is necessarily resource-constrained — it operates on a strict subset of the host's cells and at a slower effective clock rate — but it is genuinely Class 4. Self-containment is unique to Class 4; no Class k system for k < 4 can contain a subsystem of its own class or higher (a non-universal system cannot simulate a universal one). Self-containment is the structural foundation for the cross-scale identity (Section 6): the universe as a Class 4 automaton necessarily contains Class 4 subsystems, of which brains are instances.

---

## 3. Singularity Boundaries as Topological Objects

### 3.1 The Equivalence Relation

The cosmological model claims that singularities at all scales — Planck regime, particle interiors, event horizons, cosmological horizons, temporal endpoints — are instances of the same information boundary. This claim requires a formal equivalence relation.

**Definition (Information Boundary).** An *information boundary* is a codimension-1 surface B in a spacetime manifold M such that:

(IB1) **Information impermeability**: No signal crosses B. Formally, B is an apparent horizon: for every future-directed causal curve γ originating in the interior of B, γ does not exit the region bounded by B. (For cosmological horizons, "interior" and "exterior" reverse — but the impermeability condition holds from the observer's side.)

(IB2) **Holographic (area-law) saturation**: The information content of B satisfies $I(B) = A(B) / (4 l_P^2)$, where A(B) is the surface area and $l_{P}$ is the Planck length. The boundary stores the maximum information permitted by the holographic area bound ('t Hooft, 1993; Susskind, 1995; Bousso, 2002). This is a different bound from the Bekenstein bound (Bekenstein, 1981), which is set by energy and radius; the two coincide only at horizons (Gruber, 2026a, Section 5.2). Where later sections say "Bekenstein-saturated", they mean a boundary satisfying IB2.

(IB3) **Computational domain bound**: B defines the boundary of a computational domain — the set of spacetime events whose states can influence and be influenced by each other through causal processes.

**Definition (Boundary Equivalence).** Two information boundaries B₁ and B₂ are *equivalent* (B₁ ~ B₂) if they satisfy the same three conditions (IB1–IB3) with identical information-theoretic properties up to scale:

$$I(B_1) / A(B_1) = I(B_2) / A(B_2) = 1 / (4 l_P^2)$$

This is an equivalence relation (reflexive, symmetric, transitive).

### 3.2 The Singularity Inventory as an Equivalence Class

The cosmological model's claim becomes: all entries in the singularity inventory (Gruber, 2026a, Section 5.1) belong to the same equivalence class under ~. Specifically:

| Singularity | IB1 | IB2 | IB3 |
|---|---|---|---|
| Planck regime | No sub-Planck measurement possible | Maximum information density at Planck scale | Bounds the computational domain from below |
| Particle "interiors" | Interiors inaccessible | Claimed: Planck-scale Bekenstein saturation (but classical Kerr–Newman electron is super-extremal — naked, Compton-scale; see §3.7 caveat) | Particles are atomic computational units |
| Event horizons | No signal escapes | Bekenstein-Hawking entropy = $A/4l_P^2$ | Bounds the causally connected region |
| Cosmological horizon | No signal from beyond | Gibbons-Hawking entropy = $A/4l_P^2$ | Bounds the observable universe |
| Big Bang | No "before" accessible | Maximum density/temperature → maximum information density | Bounds the temporal computational domain (past) |
| Heat death | Infinite dilution → no distinguishable signals | Interior emptied → horizon-only holographic saturation (Section 3.4) | Bounds the temporal computational domain (future) |
| Big Crunch | Reconvergence → causal disconnection | Maximum density → Bekenstein saturation | Bounds the temporal computational domain (future) |
| Big Rip | Diverging expansion → mutual causal disconnection of all regions | Each fragment reaches Bekenstein saturation | Fragments the computational domain into disjoint bounded regions |

The strongest entries are event horizons (all three conditions established) and the cosmological horizon (Gibbons & Hawking, 1977). The Big Rip (Caldwell, 2002) presents a novel topology: a distributed terminal boundary consisting of many disjoint Bekenstein-saturated surfaces rather than a single connected one (formalized in Section 5.8). The weakest is the particle interior claim, which is a prediction of the model rather than an established result — indeed the classical Kerr–Newman electron is super-extremal (a naked, horizonless ring singularity at the Compton scale, not a Planck-scale horizon-bounded surface), so the identification requires a conjectured torsion-regularized core (see Section 3.7).

### 3.3 Temporal Asymptotic Structure of Singularity Boundaries

The singularity inventory (Section 3.2) treats boundaries as primarily *spatial* information barriers — surfaces in a spacelike hypersurface through which no signal passes. But singularity boundaries are equally *temporal* information barriers, and this temporal structure strengthens the structural identity claim.

**Definition (Temporal Unreachability).** An information boundary B is *temporally asymptotically unreachable* from within its computational domain D if, for every causal curve γ ⊂ D parameterized by proper time τ, the approach to B is asymptotic:

$$\lim_{\tau \to \tau_B} d(\gamma(\tau), B) = 0, \quad \text{but } \gamma(\tau) \notin B \text{ for any finite } \tau$$

where d is the spacetime distance measure appropriate to the geometry and $\tau_{B}$ may be ±∞ in a suitably chosen time coordinate.

**Application to the Big Bang.** In standard FLRW cosmology, the Big Bang is not a point in spacetime but a boundary at t → 0⁺. In conformal time η, defined by dη = dt/a(t) where a(t) is the scale factor, a radiation-dominated universe gives η ∝ 2t^½ → 0 (a finite value) as t → 0⁺: the Big Bang lies at *finite* conformal — and finite proper — depth. This finiteness is not a technicality but the horizon problem of standard cosmology: because the conformal-time depth of the past is finite, widely separated regions of the CMB sky have had no opportunity to causally equilibrate. Causal world-lines traced backward reach the t = 0 boundary at finite proper time and are geodesically incomplete there — they terminate, rather than receding asymptotically as an event horizon does. Only under past-eternal continuations of the spacetime — eternal inflation, Penrose's Conformal Cyclic Cosmology, or the Boyle–Turok CPT-symmetric universe — does the conformal coordinate extend to η → −∞ and the Big Bang recede into an asymptotic boundary.

**Application to the Big Crunch.** A hypothetical Big Crunch singularity (the time-reverse of the Big Bang in a recollapsing universe) shares the same finite-depth structure. The crunch is reached at *finite* conformal and proper time; the boundary does not recede as it is approached. World-lines are geodesically incomplete there — they end at the final singularity at finite proper time. The two temporal boundaries are dual — the bang bounds the computational domain in the past, the crunch in the future — and both terminate world-lines at finite depth rather than receding asymptotically from the interior.

**Generalization.** Approach geometry, however, is *not* uniform across the singularity inventory — it comes in distinct modes. For event horizons, the well-known result that an infalling object crosses the horizon in finite proper time but takes infinite coordinate time (as measured by a distant observer) gives an asymptotic recession in the exterior time parameter. For cosmological horizons, the de Sitter horizon is likewise approached asymptotically but never crossed from the interior perspective. The temporal termini (Big Bang, Big Crunch), by contrast, are reached at finite proper *and* finite conformal depth: world-lines terminate there rather than asymptoting. What all members share is not asymptotic approach but *no-arrival* — no observer is ever at any of these boundaries as an event in the domain. The precise claim is therefore:

**Proposition (No-Arrival, three modes).** No member of the singularity inventory is ever an event in its computational domain, but for three distinct geometric reasons: horizons **recede** (arrival forbidden; asymptotic in the interior parameter), the scale floor is **shielded** (arrival regenerated at larger scale; heuristic), and the temporal termini **terminate without arrival** (world-lines are geodesically incomplete at finite proper time; arrival *undefined*, not merely forbidden). Information impermeability (IB1–IB3) is shared by all three; asymptotic-approach geometry is **not** — it holds for horizons, heuristically for the scale floor, and for the termini only under past-eternal continuations. Temporal *asymptotic* unreachability is therefore **not** a consequence of IB1–IB3.

This refines the structural identity claim (Section 3.2): singularity boundaries share information impermeability (IB1–IB3) and the no-arrival property, but not a single approach geometry. For horizons — and heuristically for the scale floor — the impossibility of "reaching" the boundary is a structural feature of an information-impermeable, Bekenstein-saturated surface in a causally structured spacetime: the boundary recedes under any attempt to reach it. For the temporal termini this fails: they are reached at finite proper and conformal depth, and their no-arrival status is a matter of geodesic incompleteness (world-lines terminate; arrival is undefined) rather than asymptotic recession. Asymptotic unreachability is therefore not a universal consequence of IB1–IB3 but a property of the horizon members, with the termini forming the exception.

### 3.4 Heat Death as Holographically Saturated Singularity

The singularity inventory (Table, Section 3.2) lists heat death as a future temporal boundary but leaves its IB2 status (holographic saturation) implicit. A closer analysis reveals that the late-time configuration satisfies IB2 — and that this has profound consequences for the model's temporal structure.

**Argument.** Heat death as usually conceived is not holographic saturation: the entropy of a dilute equilibrium gas stays far below the area bound, and gravitational collapse does not close the gap (Gruber, 2026a, Section 5.4). Saturation arrives from the other direction. Once all matter has decayed or collapsed into black holes that then evaporate, the interior entropy carriers vanish and the cosmological horizon is the only entropy carrier left. Its Gibbons-Hawking entropy $S_{H}$ = $A_{H}$ / ($4 l_P^2$) (Gibbons & Hawking, 1977) saturates the area bound by construction. The terminal configuration is therefore a holographically saturated boundary enclosing an emptied interior: saturation holds because the interior is empty, not because its contents rise to the boundary's capacity.

**Definition (Entropy Saturation Boundary).** A temporal boundary $B_{t}$ at time $t_{\infty}$ is an *entropy saturation boundary* if:

$$\lim_{t \to t_\infty} \frac{S(t)}{S_{\text{area}}(\partial D)} = 1$$

where S(t) is the total entropy of the computational domain D, horizon included, and $S_{\mathrm{area}}$(∂D) = A(∂D) / ($4 l_P^2$) is the area-law capacity of the domain boundary.

The emptied late-time configuration satisfies this condition, because the horizon is then the only entropy carrier. It therefore satisfies IB2 (holographic saturation) in addition to IB1 (no signal crosses the boundary — there are no distinguishable signals in a maximum-entropy state) and IB3 (computational domain bound — no further computation is possible when all degrees of freedom are thermalized). Heat death is a full information boundary under the definitions of Section 3.1.

**Implication for the self-referential closure.** In the SB-HC4A framework, singularity boundaries are not merely barriers but transformation surfaces: they separate compressed (boundary-encoded) and decompressed (interior) representations of the same information (Section 4). If heat death is a singularity boundary, it is a transformation surface. The information of the universe, having reached maximum entropy (maximum decompression), encounters its own Bekenstein-saturated boundary — and the singularity transforms it back into a compressed representation. This is not thermodynamic reversal but *information-theoretic transformation*: the same information passes through the boundary from the decompressed (interior) to the compressed (boundary) representation.

The self-referential fixed point Φ(U) = U (Section 5.1) thereby acquires a temporal dimension. The universe does not merely compute its own output at each instant — it computes its own *restart*. The fixed point is not static but *cyclic*: Φ maps the heat-death boundary state to a compressed boundary state that decompresses into a new expansion phase. The cycle is:

expansion → entropy increase → emptied interior and holographic saturation → boundary compression → decompression → expansion

This cycle is the temporal expression of the self-referential closure: the universe, upon reaching its own information boundary, transforms through it and reconstitutes its computational domain.

### 3.5 The Topological Characterization

Define the **boundary space** B as the set of all information boundaries in the spacetime manifold M. The equivalence relation ~ partitions B into equivalence classes. The model claims there is a single class: $[B]_\sim = B$ — all information boundaries are equivalent.

The boundary space inherits a topology from M. The scale-invariance claim becomes:

**Claim (Scale Invariance of Boundary Structure).** The boundary space B, equipped with the topology inherited from M, is connected. Moreover, there exists a continuous scaling map $\sigma_{\lambda}$: B → B for each λ > 0 such that $\sigma_{\lambda}$(B) ~ B for all B ∈ B and all λ.

This states that the boundary structure is self-similar: zooming in or out on a boundary produces another boundary in the same equivalence class. This is the formal expression of the model's claim that singularities at all scales share the same information-theoretic character.

### 3.6 Connection to Existing Mathematics

The formalization connects to several established programs:

**Black hole thermodynamics** (Bekenstein, 1973; Hawking, 1975): The Bekenstein-Hawking entropy formula S = A / ($4 l_P^2$) is the paradigm case of IB2. The generalized second law — that the total entropy of matter plus the black hole boundary never decreases — is a conservation law across the boundary.

**The holographic principle** ('t Hooft, 1993; Susskind, 1995; Bousso, 2002): The covariant entropy bound S(L) ≤ A(B(L)) / ($4 l_P^2$) for any light sheet L bounds the entropy of a region by its boundary area. This is the general statement of IB2.

**Causal structure in general relativity** (Penrose, 1979; Hawking & Ellis, 1973): The theory of causal boundaries, event horizons, and apparent horizons provides the mathematical framework for IB1. The key tools are Penrose-Carter diagrams, the notion of a trapped surface, and the theory of causal sets.

**Loop quantum gravity** (Rovelli, 2004; Ashtekar & Lewandowski, 2004): Area quantization in LQG — the result that area comes in discrete quanta proportional to $l_P^2$ — provides a natural interpretation of the Planck-scale boundary as a discrete information-storage surface. Each quantum of area stores approximately one bit.

The technical challenge is proving that the equivalence relation ~ is nontrivial — that the Planck-scale boundary, event horizons, and cosmological horizons demonstrably satisfy the same formal conditions, not merely analogous ones. This requires tools from quantum gravity that do not yet exist in complete form.

### 3.7 Particles as Computational Atoms

The singularity inventory (Section 3.2) includes particle interiors as information boundaries. This section formalizes the consequences: if particles are Planck-scale singularity boundaries, they are the irreducible computational units — *computational atoms* — of the SB-HC4A.

**Definition (Computational Atom).** A *computational atom* is a stable configuration of a Planck-scale singularity boundary. Formally, let $B_{P}$ denote a singularity boundary of area A ~ $l_P^2$. A computational atom is a state σ ∈ Σ($B_{P}$) — the state space of boundary configurations — such that:

(CA1) **Bekenstein capacity**: The state σ encodes information I(σ) ≤ $I_{\max}$ = A($B_{P}$) / ($4 l_P^2 \ln 2$) bits, which is ≈ 0.36 bits per Planck area. Encoding the observed particle spectrum therefore needs a boundary of order 10–20 Planck areas, so "Planck-scale" means of order the Planck area, not exactly one (Gruber, 2026a, Section 5.6).

(CA2) **Dynamical stability**: σ is a fixed point or limit cycle of the boundary dynamics induced by the ambient Class 4 automaton. That is, if F: Σ($B_{P}$) → Σ($B_{P}$) is the local transition function restricted to the boundary, then F^n(σ) = σ for some finite n ≥ 1 (with n = 1 for static configurations).

(CA3) **Propagation**: σ is transportable through the computational domain — the boundary configuration can be displaced in spacetime while maintaining its identity (structural stability under spatial translation within the automaton lattice).

**Proposition (Finiteness of the Particle Spectrum).** The number of computational atoms is finite.

*Proof sketch.* By CA1, each computational atom encodes at most $I_{\max}$ bits of information, a finite number for a boundary of finite area (≈ 0.36 bits per Planck area). The number of distinguishable states on a finite-capacity boundary is at most $2^{I_{\max}}$. By CA2, only the dynamically stable subset of these states qualifies as computational atoms. Since $2^{I_{\max}}$ is finite and the stable subset is a (possibly proper) subset, the number of computational atoms is finite. □

*Remark.* This provides a structural explanation for the finite particle spectrum of the Standard Model: the twelve fundamental fermions, four gauge bosons, and the Higgs boson are the complete set of states satisfying CA1–CA3. The specific number is determined by the detailed dynamics F of the Planck-scale automaton, which is not specified by this formalization. The finiteness, however, follows from CA1 alone and is independent of the specific dynamics.

*Caveat (scale/horizon tension).* The classical Kerr–Newman solution with electron parameters is super-extremal: it has **no horizon** (a naked ring singularity) and its ring radius is of order the **Compton** scale, ~10⁻¹³ m, ~20 orders of magnitude above the Planck length. The identification of a particle with a **Planck-scale, horizon-bounded** Bekenstein-saturated surface (CA1–CA3) is therefore a **model posit requiring a torsion-regularized core** (Poplawski, 2010), not a consequence of the classical field equations. This is the weakest entry in the inventory (cf. Gruber 2026a, §5.7).

**Definition (Quantum Number as Boundary Label).** A *quantum number* is a function q: $\Sigma_{\mathrm{stable}}$($B_{P}$) → Z (or Z/2, or a finite group) that assigns to each computational atom a discrete label invariant under the boundary dynamics F. Formally, q(σ) = q(F(σ)) for all stable σ.

*Remark.* Electric charge and spin are instances of this definition: on the no-hair reading of particles as boundaries, they are the quantities with a boundary home (Gruber, 2026a, Section 5.6). Colour and weak isospin do not appear as boundary labels, and baryon and lepton number have no boundary home at all, so they are not instances. Their discreteness follows from the finiteness of $\Sigma_{\mathrm{stable}}$($B_{P}$): a function from a finite set to a totally ordered set has a discrete range. The quantization of physical properties is therefore a consequence of the Bekenstein bound at the Planck scale, not an additional postulate.

**Definition (Computational Atom Interaction).** An *interaction* between computational atoms σ₁ ∈ $\Sigma_{\mathrm{stable}}$(B₁) and σ₂ ∈ $\Sigma_{\mathrm{stable}}$(B₂) is an information exchange event in which the boundary configurations are jointly transformed:

$$T: \Sigma_{\text{stable}}(B_1) \times \Sigma_{\text{stable}}(B_2) \to \Sigma_{\text{stable}}(B_1') \times \Sigma_{\text{stable}}(B_2') \times \dots \times \Sigma_{\text{stable}}(B_k')$$

where k ≥ 1 (the number of output computational atoms may differ from the number of inputs, as in pair production or annihilation). The transformation T satisfies:

(INT1) **Information conservation**: The total boundary-encoded information is preserved: Σᵢ I($\sigma_i^{\text{in}}$) = Σⱼ I($\sigma_j^{\text{out}}$).

(INT2) **Quantum number conservation**: For each conserved quantum number q, the total is preserved: Σᵢ q($\sigma_i^{\text{in}}$) = Σⱼ q($\sigma_j^{\text{out}}$).

(INT3) **Consistency with ambient dynamics**: T is induced by the Class 4 transition function of the ambient automaton restricted to the local region containing both boundaries.

**Existence proof from Wetterich's CA↔QFT equivalences.** The computational atom formalization (CA1–CA3) is not purely speculative. Wetterich (2022a, 2022b) demonstrated that large classes of reversible cellular automata on space-lattices are exactly equivalent to discretized fermionic quantum field theories via Grassmann functional integral mappings. The equivalence is not approximate — it is a proven mathematical identity. Key results directly relevant to the computational atom formalization:

- *Fermionic spectra from automata*: Specific automata produce specific interacting fermion theories (Thirring model, Gross-Neveu model) with both abelian and non-abelian continuous symmetries (Wetterich, 2022a). This demonstrates that CA1 (finite information capacity) and CA2 (dynamical stability) yield discrete particle spectra in practice, not just in principle.
- *Local gauge symmetry*: Some automata models realize local gauge symmetries — the structure the Standard Model requires (Wetterich, 2022a). This provides a concrete mechanism for the interaction grammar (INT1–INT3): the selection rules at vertices are determined by the gauge symmetry that the automaton's structure generates.
- *Spinor gravity in 4D*: Wetterich (2022c) explicitly constructed a cellular automaton that represents spinor gravity in four dimensions, with exact local Lorentz symmetry on the discrete level and emergent diffeomorphism symmetry in the continuum limit. This is a computational atom model of gravity — not a metaphor.
- *Quantum mechanics from classical statistics*: The probabilistic description of a classical automaton (probability distribution over initial bit configurations) is mathematically equivalent to quantum mechanics — wave functions, density matrices, and non-commuting operators all arise from the automaton's classical structure (Wetterich, 2022d). This grounds the formalization's implicit assumption that quantum-mechanical particle properties emerge from classical automaton dynamics.

The Grassmann functional integral mapping provides a concrete formalization tool for Module 3 (Section 10): rather than formalizing computational atoms purely from the abstract Bekenstein bound, one can use Wetterich's mapping to construct specific automata satisfying CA1–CA3 and verify that their stable configurations match known particle properties. The approach is complementary to the top-down SB-HC4A strategy: Wetterich constructs automata *from* known QFTs (reverse-engineering the automaton from the field theory), while the SB-HC4A constrains the automaton class *from above* (the universality class is determined by axioms). The meeting point — automata that satisfy the SB-HC4A's Class 4 and holographic constraints and are then checked against Wetterich's QFT equivalences for Standard Model-like particle content — is the natural next step.

*Remark.* Feynman diagrams are graphical representations of interaction sequences. Each line represents a propagating computational atom (a boundary configuration satisfying CA1–CA3). Each vertex represents an application of the interaction transformation T. The selection rules of quantum field theory — which vertices are permitted — are the constraints imposed by INT1–INT2 on the transformation T. In this formalization, Feynman diagrams are diagrams of computation: the computational grammar of the Planck-scale automaton.

**Proposition (Conservation Laws from Bekenstein Bound).** Conservation of electric charge and angular momentum is a consequence of information conservation at singularity boundaries (INT1) combined with the identification of quantum numbers as boundary labels. The proposition does not cover baryon and lepton number. With no boundary home, they are predicted to be approximate and violated at boundaries, in agreement with their status as accidental global symmetries violated by electroweak sphalerons and, in expectation, by quantum gravity (Gruber, 2026a, Section 5.6).

*Proof sketch.* By INT1, total boundary-encoded information is conserved in any interaction. Quantum numbers, as functions of boundary states (Definition above), partition this information into independently conserved sectors. A quantum number q is conserved if and only if T preserves the q-labeled component of the boundary information. Since the Bekenstein bound constrains total information and the dynamics F preserve boundary structure (CA2), any label that is invariant under F is necessarily conserved under interactions induced by F (INT3). The specific conservation laws correspond to the specific symmetries of the Planck-scale boundary dynamics. □

**Conjecture (Three Generations from Class 4 Self-Similarity).** The three generations of Standard Model fermions — (e, μ, τ), (u, c, t), (d, s, b), and their neutrino partners — arise from a self-similar (Class 3) hierarchical structure in the space of stable singularity boundary configurations $\Sigma_{\mathrm{stable}}$($B_{P}$).

*Motivation.* Class 4 systems contain Class 3 (self-similar, fractal) dynamics as a subprocess (Gruber, 2026a, Section 2.5). If the ambient Class 4 dynamics impose a self-similar structure on the configuration space Σ($B_{P}$), the stability condition CA2 may be satisfied at multiple energy scales by the same structural configuration type — producing copies of a particle type at different mass scales. Formally, if there exists a scaling operator $S_{\lambda}$: Σ($B_{P}$) → Σ($B_{P}$) for discrete scale factors λ₁, λ₂, λ₃ such that $S_{\lambda_i}$(σ) ∈ $\Sigma_{\mathrm{stable}}$ for i = 1, 2, 3 whenever σ ∈ $\Sigma_{\mathrm{stable}}$, this would produce exactly three copies of each stable configuration.

*Status.* This is explicitly a conjecture, not a derivation. The number three is not predicted by the general argument — it would require a detailed analysis of the stability conditions under scaling in the specific Planck-scale dynamics, which are not available. The conjecture is structurally motivated by the Class 4 containment of Class 3 self-similarity but remains unproven. It is included because the three-generation structure is otherwise entirely unexplained within the Standard Model framework, and the self-similar structure of Class 4 dynamics provides a natural candidate mechanism.

---

## 4. Holographic Rule Sets

### 4.1 The Informal Definition

The cosmological model distinguishes three relationships between holographic systems and Class 4 automata (Gruber, 2026a, Section 6.1):

1. A holographic substrate produces Class 4 dynamics.
2. A Class 4 automaton produces holographic output.
3. A Class 4 automaton whose rule structure is itself holographic.

Relationship 3 — the holographic rule set — is the most novel and the least well-defined. What does it mean for a dynamical system's rules to be "holographic"?

### 4.2 Dimensional Compression Operators

**Definition (Holographic Rule Set).** A rule set R for a dynamical system on a d-dimensional manifold M^d is *holographic* if there exists a dimensional compression operator C: R^(d) → R^(d-1) such that:

(HR1) **Compression**: The full d-dimensional rule R^(d) can be faithfully encoded in a (d-1)-dimensional specification R^(d-1) = C(R^(d)), with no information loss.

(HR2) **Local decompression**: The d-dimensional dynamics at any point x ∈ M^d can be recovered from R^(d-1) restricted to the (d-1)-dimensional boundary ∂M^d in a neighborhood of x. Local application of R^(d-1) at each boundary site implicitly computes global (non-local) relationships in the interior.

(HR3) **Universality preservation**: If R^(d) defines Class 4 dynamics on M^d, then R^(d-1) on ∂M^d also defines Class 4 dynamics (the compression preserves computational universality).

### 4.3 Connection to AdS/CFT

The definition of a holographic rule set is directly modeled on the AdS/CFT correspondence (Maldacena, 1998), which provides the most concrete example:

- A gravitational theory in (d+1)-dimensional anti-de Sitter space (the "bulk" — R^(d+1))
- is fully equivalent to a conformal field theory on the d-dimensional boundary (the boundary theory — R^(d))
- with the boundary theory encoding all bulk physics (HR1)
- and local boundary operators reconstructing bulk observables in their causal wedge (HR2; Ryu & Takayanagi, 2006; Dong, Harlow, & Wall, 2016)

The SB-HC4A model generalizes this: the universe's rule structure is holographic not because of a specific AdS/CFT duality but because any Class 4 system at every scale has its information encoded on its boundary (the singularity surface) with the interior dynamics being a decompression of the boundary encoding.

### 4.4 The Rule Set as a Coalgebra

A more abstract characterization uses coalgebra theory (Rutten, 2000), which provides the natural mathematical language for systems whose behavior unfolds over time from a specification:

Define the state space X and a functor F: Set → Set that describes the system's "type of behavior" (what can be observed at each step). A coalgebra for F is a pair (X, α: X → F(X)). The rule set R is the coalgebra structure map α — it specifies how the system's state determines its next observable behavior.

A **holographic coalgebra** would then be a coalgebra (X, α) together with a boundary functor B: Set → Set and a natural transformation η: F ⇒ B ∘ G such that:

- G is a "restriction to boundary" functor
- η encodes the full coalgebra dynamics in the boundary restriction
- The coalgebra can be recovered from the boundary restriction

This is highly abstract and likely requires substantial development by a category theorist. The value of the coalgebraic formulation is that it makes the holographic property a *structural* property of the system's specification — not a property of any particular state or trajectory, but of the rule structure itself.

### 4.5 Holographic Automata in the Literature

't Hooft (2016) proposed the Cellular Automaton Interpretation of quantum mechanics, in which quantum mechanics is emergent from deterministic automaton dynamics at the Planck scale. The holographic rule set, in 't Hooft's framework, is the automaton rule at the Planck scale that produces quantum behavior as an effective description at larger scales. The dimensional compression (HR1) corresponds to the renormalization group flow from Planck-scale to observable-scale physics — each step in the RG flow "compresses" the full dynamics into an effective description at a coarser scale.

Verlinde's (2011) entropic gravity proposal — that gravity is not a fundamental force but an entropic phenomenon arising from the holographic distribution of information on screens — provides another concrete example of a holographic rule set: the gravitational "rule" (Newton's law, or its relativistic generalization) is derived from the information content of holographic screens.

Wetterich (2022a, 2022b, 2022c) provided the most concrete examples to date of cellular automata functioning as holographic rule sets. His Grassmann functional integral mapping demonstrates that specific reversible automata encode specific fermionic quantum field theories — the automaton rule at the discrete level compresses into the QFT description at the continuum level, satisfying HR1 (compression without information loss). The continuum QFT can be recovered from the automaton's probabilistic description restricted to its boundary conditions, satisfying HR2 (local decompression). Whether HR3 (universality preservation) holds — whether the automata that produce interacting QFTs are themselves Class 4 — is an open question that connects Wetterich's program directly to the SB-HC4A formalization. The spinor gravity automaton (Wetterich, 2022c) is particularly relevant: it implements a holographic rule set for gravity, with the discrete automaton rule compressing into the diffeomorphism-invariant continuum theory via a concrete dimensional compression operator.

### 4.6 Entanglement as Estimation Inadmissibility

Section 6.1 of Gruber (2026a) states that a Class 4 automaton produces holographic output — non-local distributed information encoding — and identifies this as quantum entanglement. Relationship 2 (Class 4 automaton → holographic output) asserts that the computational substrate distributes information across boundary-encoded states in a way that is irreducible to independent local descriptions. Section 6.5 of the same paper provides a statistical-estimation-theoretic grounding for this claim via the James-Stein paradox. The formalization task is to make this connection rigorous: to show that the structure of Bekenstein-saturated singularity boundaries forces the inadmissibility of independent state estimation, and that the dominating estimator is the entangled one.

**The James-Stein Inadmissibility Conjecture (JSIC).** The core formal claim:

*Conjecture (JSIC).* Let B be the configuration space of stable Planck-scale singularity boundary states in an SB-HC4A, with |B| ≥ 3 distinguishable configurations. Let θ = (θ₁, ..., $\theta_{d}$) be the vector of individual boundary states of d particle-singularities on a shared automaton substrate. Then the independent estimator $\hat{\theta}_{\mathrm{MLE}}$ = (θ̂₁, ..., $\hat{\theta}_{d}$), which estimates each particle's state independently, is inadmissible under any loss function L satisfying [conditions specified in JS4 below]. The dominating estimator $\hat{\theta}_{\mathrm{JS}}$ shrinks toward the global vacuum state θ₀ (dominating, not admissible: the James-Stein estimator is itself dominated by its positive-part variant):

$$\hat{\theta}_{\mathrm{JS}} = \theta_0 + (1 - w)(\hat{\theta}_{\mathrm{MLE}} - \theta_0)$$

where w is the shrinkage coefficient. The physical interpretation: independent estimation of particle states ignores information available from the shared substrate, and the estimator that exploits the common prior (the automaton's global state) dominates the independent one. Entanglement is the regime where this dominance is empirically detectable.

**Mathematical structure required.** Five components must be established for a rigorous formulation:

**(JS1) Configuration space metric.** B must be equipped with a metric d(·,·) compatible with the loss function. The natural candidate is the quantum Fisher information metric (Bures metric) on the space of density matrices, restricted to boundary configurations. For Bekenstein-saturated boundaries with finitely many bits (Section 3.7, condition CA1), this is a finite-dimensional simplex. The metric must be compatible with the boundary dynamics F (Section 3.7, condition CA2) in the sense that F acts as an isometry or contraction — the dynamics do not expand distances in configuration space.

**(JS2) Curvature condition.** The classical Stein effect (James & Stein, 1961) operates in Euclidean space. The generalization to curved spaces — the Stein effect for Fréchet means (McCormack & Hoff, 2022) — requires non-positive sectional curvature (CAT(0) / Hadamard condition). The configuration spaces arising from tensor categories (Levin-Wen models, which are the natural mathematical framework for topological phases of matter) have positive combinatorial curvature from vertex branching, so the CAT(0) condition likely fails for non-abelian anyon models. Two routes around this obstruction are available: (a) a Bourgain-type embedding (Bourgain, 1985) of the configuration graph into a Hadamard space with controlled distortion, such that the Stein effect in the target space pulls back to the original space with bounded error; or (b) a discrete Laplacian approach, constructing superharmonic functions on the configuration graph that yield shrinkage estimators without requiring the global curvature condition. Route (b) is more natural for the SB-HC4A because the configuration space is inherently discrete and finite.

**(JS3) Dimensional threshold.** The James-Stein inadmissibility requires dim(B) ≥ 3. Brown (1971) proved that this threshold corresponds exactly to the transience of Brownian diffusion in d dimensions: in d ≤ 2, Brownian motion is recurrent and the MLE is admissible; in d ≥ 3, Brownian motion is transient and the MLE is inadmissible. For the SB-HC4A: condition CA1 (Section 3.7) gives each computational atom ≈ 0.36 bits per Planck area of boundary. The requirement is that these bits encode ≥ 3 distinguishable states, i.e., ≥ log₂(3) ≈ 1.58 bits of boundary information, which needs a boundary of at least about 4–5 Planck areas. The Standard Model's 17 elementary particle types — 12 fermions, 4 gauge bosons, and the Higgs — need log₂(17) ≈ 4.1 bits, hence about 11 Planck areas or more; at that size the threshold is met comfortably, as it is by any non-trivial quantum number with three or more values (e.g., color charge with three states).

**(JS4) Loss function.** The natural candidate is quantum relative entropy (Kullback-Leibler divergence on density matrices), which connects to Brown's (1971) complete class theorem for exponential families: under KL loss, the class of admissible estimators for exponential families is precisely the class of generalized Bayes estimators, and the MLE is excluded for d ≥ 3. An alternative is fidelity loss: Ferrie and Blume-Kohout (2018) proved that maximum likelihood quantum state tomography is inadmissible under fidelity loss, establishing the quantum Stein effect directly. Salmon, Strelchuk, and Arvidsson-Shukur (2024) extended this to quantum Gaussian sensing, demonstrating James-Stein-type estimators that outperform independent estimation in quantum parameter estimation. The choice of loss function determines the shrinkage coefficient w and the quantitative predictions.

**(JS5) Vacuum identification.** The shrinkage target θ₀ must be identified with the physical vacuum state. The formal grounding comes from two independent results. First, Tsang (2020) showed that, on the assumption that the prior density is the square of a wavefunction, the problem of finding the unfavourable prior that tightens the Bayesian Cramér–Rao bound for minimax estimation is — in a special case, not in general — equivalent to finding the ground state of a Schrödinger equation, with the Fisher information playing the role of the potential. Two things about that result must be stated precisely, because the looser version does not survive contact with the source: the correspondence runs between the least-favourable *prior* and a ground-state wavefunction, not between an estimator and a vacuum state, and it is established for a special case rather than as a general theorem. Reading θ₀ as the physical vacuum is an extension we are making on top of it, not something Tsang proves. Second, the classical James-Stein estimator uses the harmonic prior ‖θ‖^(2−d), which is the Green's function of the Laplacian — the electrostatic potential of a point source. The vacuum state is the ground state of the Hamiltonian, which is the minimum of the potential. The shrinkage target and the physical vacuum are therefore the same mathematical object viewed from two different frameworks (estimation theory and quantum mechanics). For the SB-HC4A, θ₀ is the boundary configuration with no excitations above the ground state — the state of minimum boundary information content consistent with the Bekenstein bound.

**Connection to existing formalization modules.** The JSIC connects to three modules already specified:

- *Module 3.7 (computational atoms):* The configuration space B in the JSIC is the same space $\Sigma_{\mathrm{stable}}$($B_{P}$) of stable boundary configurations defined in Section 3.7. The dimensional threshold (JS3) depends on the finiteness proposition proved there. The metric (JS1) must be compatible with the boundary dynamics F defined in CA2.
- *Module 4 (holographic rule sets):* Entanglement is the holographic output that Relationship 2 of Section 6.1 (Gruber, 2026a) describes. The JSIC provides the statistical-mechanical content of the claim that Class 4 automata produce non-local information encoding: the holographic output is the regime where the shared substrate makes the dominating estimator non-local.
- *Module 5 (self-referential closure):* The shared automaton substrate that establishes the common prior — the ground on which the Stein effect operates — is the self-referential automaton itself. The self-referential closure Φ(U) = U guarantees that the substrate is not external to the system; the common prior is internal, which is why entanglement is intrinsic rather than imposed.

**What formalization would deliver.** A proof of the JSIC would give one result directly and would set the target for two others. The parent paper stops at the qualitative claim and does not read w as a scaling law for correlation strength or decoherence (Gruber, 2026a, Section 6.5), so items 1 and 2 state what a discrete Stein-type theorem would have to supply before w could be read that way:

1. **A route to Bell nonlocality.** The Bell inequalities establish that quantum correlations exceed any local hidden variable model. On the JSIC, measuring one boundary configuration updates the global state estimate, because the dominating estimator is not the independent one. For the shrinkage coefficient w to quantify the degree of nonlocality, the theorem would also have to give w a defined meaning for a single boundary locus, where at present it has none.

2. **A route to a decoherence threshold.** In the classical setting w depends on the signal-to-noise ratio σ²/‖θ‖², and when noise dominates w → 1 and the estimate collapses to the vacuum. Reading this as decoherence would need the discrete theorem to carry that dependence over to the boundary configuration space and to identify its noise term with environmental degrees of freedom. Neither step is available yet.

3. **The holographic output claim gains mathematical content.** Section 6.1 of Gruber (2026a) asserts that entanglement *is* holographic output. Without the JSIC, this is a verbal identification. With it, the claim becomes: holographic output is the non-local information structure produced by the dominating estimator on a shared Bekenstein-saturated substrate, and entanglement is its empirical manifestation.

---

## 5. Self-Referential Closure

### 5.1 The Fixed-Point Condition

The model's central formal claim is self-referential closure:

Φ(U) = U

where U is the SB-HC4A (the universe) and Φ is the composition of holographic encoding with decompression: encode the interior onto the boundary, unfold the boundary back into an interior. Φ is not the "compute the output" operator. Read as "whatever the dynamics produce", Φ(U) = U holds of every deterministic system and asserts nothing; read as the composition, it is a losslessness condition — encoding U and decompressing it again returns U, with nothing added and nothing lost — whose denial is information destruction at a singularity boundary (Gruber, 2026a, Section 6.3). The holographic rules encode the system; the Class 4 dynamics decompress the encoding; the holographic output re-encodes the result.

Two senses of self-reference are in play, and they are not interchangeable. **Syntactic** self-reference is the relation just defined: a compressed description unfolds into what re-encodes it, and nothing in the relation requires anything to be *about* anything. **Representational** self-reference is the relation a self-model bears to the system holding it, where the model's content is that system and can misrepresent it. Φ(U) = U is syntactic; the cognitive fixed point Ψ(m\*) = m\* of Section 5.4 is representational.

This is a fixed-point statement. The mathematical program is to define Φ rigorously and prove (or specify the conditions under which) a fixed point exists.

### 5.2 Lawvere's Fixed-Point Theorem

Lawvere's (1969) fixed-point theorem generalizes the diagonal arguments of Cantor, Gödel, and Turing into a single category-theoretic statement: In a Cartesian closed category C, if there exists a point-surjective morphism e: A → B^A (where B^A is the exponential object), then every endomorphism f: B → B has a fixed point.

The cosmological application: Let C be the category of computable dynamical systems. Let A = the set of specifications (rule sets) and B = the set of dynamical behaviors (orbits). A point-surjective morphism e: A → B^A means "every map from specifications to behaviors can be specified" — i.e., the system is expressive enough to encode the relationship between rules and dynamics.

If the SB-HC4A is computationally universal (Class 4, u = 1), it can simulate any computable dynamics, including its own. That is the informal reading of point-surjectivity rather than a demonstration of it: establishing the condition requires exhibiting the category, the exponential object and the morphism e, which is the open task of Module 5.2–5.3 (Section 10).

Granting point-surjectivity, Lawvere's theorem yields that every endomorphism on the behavior space has *a* fixed point. It does not yield *which* one. The theorem therefore supports the existence of some configuration self-consistent under Φ; it does not establish that the actual universe is that configuration, and Φ(U) = U asserts more than Lawvere delivers. Closing that gap needs a uniqueness result, for which the coalgebraic route of Section 5.3 is the candidate — a final coalgebra is unique up to isomorphism. Until one is in hand, Φ(U) = U is the model's central hypothesis rather than a theorem, and the fixed-point machinery constrains it rather than proving it.

### 5.3 Coalgebraic Fixed Points

An alternative formalization uses the theory of final coalgebras (Aczel & Mendler, 1989; Barr, 1993). For a functor F, the final coalgebra — if it exists — is the terminal object in the category of F-coalgebras. It has the property that it is the unique (up to isomorphism) coalgebra that is "maximally consistent": it contains all possible behaviors and is a fixed point of the coalgebra-building process.

Define F as the functor capturing the SB-HC4A's behavior type: F(X) = (holographic boundary information) × (Class 4 interior dynamics). The final F-coalgebra, if it exists, would be the unique self-consistent SB-HC4A: the system that is its own final coalgebra — whose behavior IS its specification.

The fixed-point condition Φ(U) = U becomes: U is the final coalgebra for the SB-HC4A behavior functor. This is a stronger claim than merely "a fixed point exists" — it claims that U is the *unique* self-consistent system of this type.

### 5.4 Connection to the Self-Referential Computation Fixed Point

The self-referential computation formalization (Gruber, 2026c, Section 6.4) defines the self-modeling fixed point as: Ψ(m*) = m*, where Ψ is the "model of" operator acting on the joint explicit state m = (e, w) of self-model and world-model, and m* is the joint state at which the model and the modeled coincide. The cosmological model claims this is the same formal structure at a different scale.

To make this precise, define:

- $\Phi_{\mathrm{cosmo}}$: $U_{\mathrm{cosmo}}$ → $U_{\mathrm{cosmo}}$ (holographic encoding composed with decompression — syntactic)
- $\Psi_{\mathrm{SRC}}$: $M$ → $M$, on the joint state m = (e, w) (the self-referential computation "model of" operator — representational)

The structural identity claim is that there exists a structure-preserving map (a functor; see Section 6) that maps $\Phi_{\mathrm{cosmo}}$ to $\Psi_{\mathrm{SRC}}$. Both are endomorphisms with fixed points, and the claim is that the fixed-point structure is isomorphic rather than merely analogous.

The two operators are not the same operator, and the parallel notation is a convenience. $\Phi_{\mathrm{cosmo}}$ requires nothing to be *about* anything; $\Psi_{\mathrm{SRC}}$'s content is the system that holds it, and can misrepresent it. A functor mapping one to the other must therefore preserve fixed-point structure across a difference in kind, so Module 6 is a substantive construction and not a corollary of the notation. A demonstration that no such functor exists would refute the correspondence claim while leaving both fixed points standing.

### 5.5 Inexpressibility as a Formal Consequence

Gödel's first incompleteness theorem (Gödel, 1931): Any consistent formal system F that is sufficiently expressive (can represent arithmetic) contains statements that are true but not provable in F.

The theorem governs formal systems that represent arithmetic and represent statements about their own derivations. That is the representational sense of self-reference of Section 5.1, and Φ(U) = U is the syntactic one, so the incompleteness result does not follow from the fixed point. It follows from universality together with embedding: the SB-HC4A is computationally universal (Class 4), hence it implements formal systems of the required expressive strength, and each such system is a proper part of U while having U as its subject matter. For any of them there are truths about U it cannot prove.

More specifically, the **Weltformel** (world equation) — a complete specification of U — cannot be a theorem of any formal system implemented within U, since every such system is subject to the incompleteness result while taking U as its subject matter. The "world equation" is therefore not an equation but the process U itself — it can only be expressed by running it.

This connects to Chaitin's (1966) extension of Gödel: no formal system of complexity K can prove theorems about systems of complexity greater than K + c (for a constant c). Since U is at least as complex as any internal formal system, no internal specification can fully capture U.

### 5.6 Cyclic Dynamics and Temporal Self-Referential Closure

The heat-death analysis of Section 3.4 implies that the self-referential fixed point Φ(U) = U has a cyclic temporal structure. This section formalizes the cyclic dynamics and their consequences.

**Definition (Cosmic Cycle).** A *cosmic cycle* is a maximal connected computational domain $D_{n}$ bounded by two temporal singularity boundaries: an initial boundary $B_{n}$^- (expansion onset) and a terminal boundary $B_n^+$ (Bekenstein saturation — heat death, Big Crunch, Big Rip fragmentation, or equivalent). The self-referential closure operator Φ maps the terminal state to the initial state of the successor cycle (or cycles, in the branching case; see Section 5.8):

$$\Phi: B_n^+ \to B_{n+1}^-$$

where the information content is conserved: I($B_n^+$) = I($B_{n+1}^-$). The compressed boundary representation at $B_n^+$ decompresses into the interior dynamics of $D_{n+1}$.

**Proposition (Cyclic Fixed Point).** The fixed-point condition Φ(U) = U, when applied to the temporal sequence of cycles, yields:

$$U = \bigcup_{n \in \mathbb{Z}} D_n$$

with Φ acting as the transition operator between consecutive cycles. The universe as a whole (the union over all cycles) is the fixed point; each individual cycle is a single iteration of the self-referential computation. The sequence $\{D_n\}_{n \in \mathbb{Z}}$ is bi-infinite — there is no first or last cycle, because the fixed-point condition requires the sequence to be invariant under Φ, which precludes boundary terms.

**Alternation of cycle types.** The terminal boundary $B_n^+$ need not be of the same physical type in every cycle. Possible terminal singularities include heat death (entropy saturation at quasi-infinite dilution), Big Crunch (entropy saturation at maximum contraction), Big Rip (fragmentation into distributed Bekenstein-saturated surfaces; see Section 5.8), or other Bekenstein-saturated configurations. The sequence of cycle types — (expansion → heat death), (expansion → crunch), (expansion → Big Rip), or other configurations — is not constrained to be periodic or predictable.

**Conjecture (Computational Irreducibility of Cycle Sequence).** Let T = $\{t_n\}_{n \in \mathbb{Z}}$ be the sequence of cycle types, where $t_{n}$ ∈ {heat death, crunch, Big Rip, ...}. If the SB-HC4A is a Class 4 system, then T is computationally irreducible: there exists no algorithm that computes $t_{n+k}$ from $t_{n}$ in fewer than k applications of Φ.

*Proof sketch:* By the Class 4 characterization (Section 2.2), the system is computationally irreducible (r(Σ) = 0). The cycle-type sequence T is a coarse-grained projection of the full dynamics. If T were computationally reducible (predictable by a shortcut), then the projection would provide a reducibility channel for the full system — contradicting r(Σ) = 0 (unless the projection loses all dynamically relevant information, in which case T is trivially predictable because it is trivially uninformative). For a non-trivial cycle-type taxonomy, T inherits the irreducibility of the underlying dynamics. The dichotomy in this sketch is not exhaustive: an irreducible system can have coarse-grained observables that are informative and still predictable by a shortcut. The missing premise is that the cycle-type map carries enough of the dynamics that a shortcut for T would yield one for the full system, and until that premise is shown the statement is a conjecture.

This irreducibility is consistent with the Class 4 character of the SB-HC4A: no shortcut predicts the next cycle type without running the full computation through the current cycle. The future is genuinely open at the level of cosmic cycles, just as it is at every other scale of Class 4 dynamics.

### 5.7 CPT Signature Alternation

The cyclic dynamics of Section 5.6 raise a natural question: what discrete symmetry properties does the transition operator Φ: $B_n^+$ → $B_{n+1}^-$ preserve? The SB-HC4A framework provides a specific answer.

**Observation.** The singularity boundary transformation between compressed and decompressed information representations is not required to preserve the CPT (charge-parity-time) orientation of the interior dynamics. The information content is conserved (I($B_n^+$) = I($B_{n+1}^-$)), but the *sign conventions* — which configurations count as "matter" vs. "antimatter," "left" vs. "right," "forward" vs. "backward" in time — are properties of the decompressed interior representation, not of the compressed boundary encoding.

**Definition (CPT Signature).** The *CPT signature* $\sigma_{n}$ ∈ {+1, -1} of a cycle $D_{n}$ is the orientation of the CPT transformation relative to a fixed (but arbitrary) reference convention. A cycle with $\sigma_{n}$ = +1 has the same matter/antimatter labeling as the reference; $\sigma_{n}$ = -1 has the conjugate labeling.

**Conjecture (CPT Alternation).** The transition operator Φ may flip the CPT signature between consecutive cycles:

$$\sigma_{n+1} = -\sigma_n$$

producing an alternating sequence of matter-dominated and antimatter-dominated universes: ..., $D_{-1}$(antimatter), $D_{0}$(matter), $D_{1}$(antimatter), $D_{2}$(matter), ...

**Connection to existing models.** This conjecture connects to the CPT-symmetric universe model of Boyle, Finn, and Turok (2018), which proposes that the universe before the Big Bang is the CPT mirror image of the universe after it — the same physical content with all discrete symmetries reversed. In the Boyle-Turok model, CPT symmetry is a boundary condition at the Big Bang singularity. In the SB-HC4A, CPT alternation is a *structural consequence* of the singularity transformation: the compressed boundary encoding does not carry CPT orientation, so each decompression can in principle realize either orientation. The alternating pattern is the simplest non-trivial assignment consistent with CPT symmetry of the overall bi-infinite sequence.

The conjecture also relates to Penrose's (2010) Conformal Cyclic Cosmology (CCC), which proposes that the conformal geometry of one aeon's infinite future (heat death) is identified with the conformal geometry of the next aeon's Big Bang. The SB-HC4A's cyclic structure shares CCC's core insight — that cosmological cycles are connected through conformal/information-theoretic transformations at singularity boundaries — but differs in two respects: (a) the SB-HC4A permits alternation between heat-death and crunch boundaries (CCC requires heat death), and (b) the SB-HC4A adds CPT alternation, which CCC does not address.

**Implication for baryon asymmetry.** If CPT alternation holds, the observed baryon asymmetry (the dominance of matter over antimatter in the present cycle) is not a dynamical accident requiring explanation by baryogenesis mechanisms but a *structural feature* of the current cycle's CPT orientation. The "missing" antimatter is not missing — it constitutes the adjacent cycles. This is a testable consequence: any observation of fundamental CPT violation within a single cycle would be evidence against CPT alternation, while the persistent failure to find a dynamical baryogenesis mechanism would be consistent with it.

**Speculative status.** CPT alternation is the most speculative claim in this paper. It is not derivable from the five axioms (Section 7) without additional assumptions about the singularity transformation's effect on discrete symmetries. It is presented as a *natural possibility* within the SB-HC4A framework — one that connects to established proposals (Boyle, Finn, & Turok, 2018; Penrose, 2010) and generates testable predictions (baryon asymmetry as structural rather than dynamical) — but it requires independent motivation or derivation before it can be promoted to a formal consequence of the model.

### 5.8 The Big Rip: Distributed Singularity Boundaries and Branching Cycles

The cyclic dynamics of Sections 5.6–5.7 assume that the terminal boundary $B_n^+$ is a single connected Bekenstein-saturated surface — whether reached through heat death (entropy saturation at cosmological dilution) or Big Crunch (entropy saturation at maximum contraction). A third cosmological endgame — the Big Rip (Caldwell, 2002) — breaks this assumption and requires a generalization of the cyclic formalism.

**Physical motivation.** If dark energy has an equation-of-state parameter w < −1 (phantom energy), the dark energy density increases without bound as the universe expands. The Friedmann equation implies that the scale factor a(t) diverges at a finite future time $t_{\mathrm{rip}}$:

a(t) → ∞ as t → $t_{\mathrm{rip}}$ < ∞

The diverging expansion rate progressively unbinds all gravitationally and electromagnetically bound structures — galaxy clusters, galaxies, stellar systems, atoms — and ultimately tears apart spacetime itself (Caldwell, Kamionkowski, & Weinberg, 2003). Every point in space becomes a singularity.

**Definition (Distributed Terminal Boundary).** A *distributed terminal boundary* is a terminal singularity $B_n^+$ that is not a single connected surface but a collection of disjoint Bekenstein-saturated surfaces:

$$B_n^+ = \bigsqcup_{j \in J} B_n^{+,j}$$

where J is an index set (possibly infinite or uncountable), each $B_n^{+,j}$ satisfies conditions IB1–IB3 (Section 3.1), and the fragments are mutually causally disconnected: for all j ≠ k, no causal curve connects a point interior to $B_n^{+,j}$ to a point interior to $B_n^{+,k}$.

The Big Rip produces exactly this structure. As the expansion rate diverges, the causal horizon shrinks to zero — every spatial region becomes causally disconnected from every other. Each causally disconnected region is bounded by a Bekenstein-saturated surface (its own local information boundary). The computational domain fragments into a disjoint union of singularity boundaries.

**Proposition (Generalized Cycle Map).** When the terminal boundary $B_n^+$ is distributed, the cycle map Φ: $B_n^+$ → $B_{n+1}^-$ generalizes from a single-valued map to a multi-valued map:

$$\Phi: \bigsqcup_{j \in J} B_n^{+,j} \to \bigsqcup_{j \in J} B_{n+1,j}^-$$

where each fragment $B_n^{+,j}$ independently decompresses into a new computational domain $D_{n+1,j}$ with its own initial boundary $B_{n+1,j}^-$. The information content is conserved fragment-wise:

$$I(B_n^{+,j}) = I(B_{n+1,j}^-)$$

*Proof sketch:* Each fragment $B_n^{+,j}$ satisfies IB1–IB3 and is Bekenstein-saturated. By the same argument that establishes singular-to-singular transitions for connected boundaries (Section 3.4), each fragment is a transformation surface. Since the fragments are mutually causally disconnected, the transformation of each fragment is independent of all others. The cycle map decomposes into independent single-fragment maps, each of which operates by the same information-transformation mechanism as the connected case. □

**Definition (Branching Cycle Structure).** A *branching cycle structure* is a generalization of the cosmic cycle sequence $\{D_n\}_{n \in \mathbb{Z}}$ (Section 5.6) from a linear chain to a tree (or forest). Each node is a computational domain $D_{n,j}$. Each domain has one parent (the fragment of the predecessor domain's terminal boundary from which it decompressed) and potentially many children (if its own terminal boundary is distributed). The branching factor $b_{n}$ = |$J_{n}$| — the number of fragments at cycle n's terminal boundary — satisfies:

- $b_{n}$ = 1 for heat death or Big Crunch terminal boundaries (linear succession)
- $b_{n}$ > 1 (potentially |$J_{n}$| = ∞ or uncountable) for Big Rip terminal boundaries (branching)

**Proposition (Three Endgame Universality).** All three cosmological endgames — heat death, Big Crunch, and Big Rip — are special cases of the generalized cycle map. The framework does not depend on the equation of state of dark energy:

| Endgame | Terminal boundary | Branching factor | Cycle structure |
|---|---|---|---|
| Heat death (w ≥ −1) | Single connected surface | b = 1 | Linear sequence |
| Big Crunch (Ω > 1) | Single connected surface | b = 1 | Linear sequence |
| Big Rip (w < −1) | Distributed disjoint surfaces | b ≫ 1 | Branching tree |

The SB-HC4A cyclic cosmology is therefore robust across the full parameter space of dark energy equations of state.

**CPT signatures in the branching case.** When the cycle map branches, each daughter domain $D_{n+1,j}$ independently realizes a CPT signature $\sigma_{n+1,j}$ ∈ {+1, −1}. The CPT alternation conjecture of Section 5.7 generalizes: rather than a single alternating sequence, the branching tree exhibits a distribution of CPT orientations across its branches. Whether the daughter signatures are correlated (all flip together), independent (each flips with probability 1/2), or constrained by some other principle is undetermined by the current framework — it depends on details of the singularity transformation that the model does not yet specify. This indeterminacy is consistent with Weak Point 6 of Gruber (2026a): the model predicts cyclicity (and now branching cyclicity) but underdetermines the cycle's character.

**Computational irreducibility of branching.** The branching factor $b_{n}$ is itself a dynamical quantity determined by the full Class 4 computation within cycle n. If the irreducibility conjecture of Section 5.6 holds, $b_{n}$ cannot be predicted without running the computation through cycle n. Whether the universe ends in heat death, Big Crunch, or Big Rip — and, in the Big Rip case, how many fragments result — would then be computationally irreducible, consistent with the Class 4 character of the SB-HC4A.

**Connection to multiverse proposals.** The Big Rip branching mechanism provides a concrete physical process — grounded in the SB-HC4A information-theoretic framework — for generating a multiverse. Unlike eternal inflation (which produces a multiverse through quantum fluctuations in an inflaton field) or the string landscape (which populates a space of vacua), the SB-HC4A branching multiverse arises from the fragmentation of a single computational domain at its Bekenstein-saturated terminal boundary. Each daughter universe inherits its information content from a specific fragment of the parent's boundary, providing a well-defined information-conservation principle across the branching event.

---

## 6. The Cross-Scale Structural Correspondence Functor (Proposed)

### 6.1 Two Categories

The cross-scale structural correspondence (Gruber, 2026a, Section 7) is currently expressed as a table of correspondences. To make this a mathematical claim, we need a morphism between mathematical objects.

Following the self-referential computation formalization's category-theoretic approach (Gruber, 2026c, Section 7), define two categories:

- **Cosmo** (Cosmological): Objects are physical states of the universe (field configurations, metric tensors, matter distributions). Morphisms are physical dynamics — time evolution governed by the laws of physics.

- **SRC** (Self-Referential Computation): Objects are the model-density states ρ(s, ν, t) (from the self-referential computation formalization). Morphisms are the dynamics of the model density — the Fokker-Planck equation of the formalization, substrate dynamics, permeability changes.

### 6.2 The Structural Correspondence Functor

The structural correspondence claim is that there is conjectured to exist a functor I: Cosmo → SRC that preserves the relevant structure:

| Cosmo | I | SRC |
|---|---|---|
| Singularity boundary | ↦ | Implicit-explicit boundary |
| Observable interior | ↦ | Explicit models |
| Holographic rule structure | ↦ | Distributed implicit knowledge |
| Class 4 dynamics | ↦ | Free modeling (Class 4), usually near-critical in cortex |
| $\Phi_{\mathrm{cosmo}}$(U) = U (syntactic closure) | ↦ | Ψ(m\*) = m\* (representational closure) |
| Total information conserved, interior projection selective | ↦ | Total information conserved, explicit models generated selectively from the substrate |
| Gödelian inexpressibility | ↦ | Meta-Problem |

For I to be a proper functor, it must:

(F1) **Map objects to objects**: Each physical state maps to a model-density state.

(F2) **Map morphisms to morphisms**: Physical dynamics map to model-density dynamics, preserving composition (if state A evolves to B and B to C in Cosmo, the mapped states evolve correspondingly in SRC).

(F3) **Preserve identity**: The identity morphism in Cosmo (no change) maps to the identity morphism in SRC.

### 6.3 What the Functor Preserves

The functor I is not expected to preserve all structure — the cosmological scale and the self-referential computation scale differ in their physical content, their energy ranges, their characteristic time scales, and their spatial extent. What I preserves is the *computational architecture*:

1. **The boundary structure**: The functor maps information-impermeable boundaries to information-opaque boundaries.
2. **The compression-decompression relationship**: The functor maps holographic encoding/decoding to implicit/explicit information processing.
3. **The computational class**: The functor maps Class 4 dynamics to Class 4 dynamics. On the cosmological side the model places these at the edge of chaos; on the cognitive side they are free modeling, which in cortex shows as near-critical dynamics. Criticality there is a signature, not a condition of consciousness.
4. **The fixed-point structure**: The functor maps self-referential closure to self-referential closure.

More precisely, the functor should be a **forgetful functor** that discards scale-specific content while preserving computational-architectural structure. The category-theoretic framework for this is the theory of **abstract model theory** (Barwise, 1974) or **institutions** (Goguen & Burstall, 1992), which formalize the notion of "same structure, different content."

### 6.4 The Scale Functor

The fractal nature of the SB-HC4A suggests not just a single functor but a family of functors parameterized by scale:

$$I_\lambda: \mathrm{Cosmo}_\lambda \to \mathrm{Cosmo}_{\lambda'}$$

where $\mathrm{Cosmo}_{\lambda}$ is the category of cosmological dynamics at scale λ. The self-similarity of Class 4 systems means that each scale hosts the same computational architecture. The cross-scale functor is then $I_{\mathrm{brain}}$: $\mathrm{Cosmo}_{l_{\text{brain}}}$ → SRC — the specialization of the scale functor at the brain-relevant scale (~10⁻² m).

This formulation makes the structural identity precise: the universe's computational architecture is scale-invariant, and self-referential computation in cognitive systems is the instance at one particular scale. The scale functor $I_{\lambda}$ implements the computational nesting that Class 4 self-containment produces (Section 2.6): a Class 4 system contains Class 4 subsystems, each of which contains further Class 4 subsystems. The cross-scale identity is not merely geometric self-similarity (which would be Class 3) but computational self-containment — the same universality class, recursively nested.

---

## 7. The Necessity Argument

### 7.1 The Five Axioms in Formal Language

The cosmological model's necessity argument (Gruber, 2026a, Section 10) claims that, conditional on substrate determinism (Gruber, 2026a, Section 3.2), five axioms make the SB-HC4A architecture class necessary; it does not claim uniqueness within that class (Gruber, 2026a, Section 10.2). Formalizing this requires expressing the axioms and the derivation in a formal logical framework.

The natural tool is modal logic — specifically, the S5 system for metaphysical necessity (Kripke, 1963), extended with predicates for computational and information-theoretic properties.

**Formal axiom system:**

Let the domain of discourse be the class of all possible dynamical systems. Define predicates:

- E(x): "x exists" (is physically instantiated)
- $C_{k}$(x): "x has computational class k" for k ∈ {1, 2, 3, 4, 5}
- U(x): "x is computationally universal"
- Irr(x): "x is computationally irreducible"
- SOC(x): "x self-maintains criticality via self-organized criticality"
- Contains(x, k): "x contains a Class k subsystem"
- IB(x): "x is bounded by information-impermeable boundaries at every scale"
- Hol(x): "x has holographic structure"
- SRC(x): "x is self-referentially closed"

**Axiom A1 (Ontological Necessity):**
□ ∃x E(x)
(Necessarily, something exists.)

**Axiom A2 (Computational Character):**
∀x [E(x) → ∃k $C_{k}$(x)]
(Everything that exists has a computational class.)

**Axiom A3 (Class 4 Characterization):**
∀x [$C_{4}$(x) ↔ (U(x) ∧ Irr(x) ∧ ∀k≤4 Contains(x, k))]
(Class 4 is uniquely characterized by universality + irreducibility + containment of all classes including itself.)

Self-organized criticality enters as a separate statement, not as a defining condition: $C_{4}$(x) → typically SOC(x) in self-organizing physical substrates. It is the usual route by which a physical Class 4 system maintains its regime, and a Class 4 system that does not show it still satisfies A3.

**Axiom A4 (Information Bound):**
∀x [E(x) → IB(x)]
(Everything that exists is bounded by information horizons.)

**Axiom A5 (Holographic Encoding):**
∀x [IB(x) → Hol(x)]
(Information boundaries encode interior information holographically.)

### 7.2 The Derivation

**Theorem (SB-HC4A Necessity).** From A1–A5:

□ ∃x [E(x) ∧ $C_{4}$(x) ∧ IB(x) ∧ Hol(x) ∧ SRC(x)]

*Proof sketch:*

1. By A1: □ ∃x E(x). Something necessarily exists.
2. By A2: This thing has some computational class k.
3. The elimination argument (Section 3.2 of Gruber, 2026a):
   - k = 1 or k = 2: The universe contains self-referential computational systems and universal computation. By A3, only Class 4 supports these. A Class 1 or 2 system cannot contain a Class 4 subsystem (strict containment hierarchy). Eliminated.
   - k = 3: Class 3 is computationally reducible. Universal computation requires irreducibility. Eliminated.
   - k = 5: If k = 5, the system's dynamics have an inexpressible component, in the rule or in the initial data (Section 2.4). Physics — the expressible-rule description of the universe — would be impossible. By A2, the system has computational character; Class 5 makes this character inexpressible. Eliminated (by coherence with A2, or by abduction: physics is not impossible).
   - Therefore k = 4.
4. By A4: The Class 4 system is bounded by information horizons.
5. By A5: The boundaries encode the interior holographically.
6. By A3 (universality) + step 5 (holographic encoding): A universal system with holographic encoding can encode its own rules on its boundary. The holographic rules produce Class 4 dynamics that produce holographic output — a self-referential loop. By Lawvere's theorem (Section 5.2), this loop has a fixed point: SRC(x). □

### 7.3 Class Selection, Not Uniqueness

**Proposition (Class Selection).** The five axioms select the SB-HC4A architecture class, conditional on the substrate-determinism assumption (Gruber, 2026a, Section 3.2). They do not select a unique model within that class: dimension, the singularity inventory, and cyclic versus branching temporal structure remain open (Gruber, 2026a, Section 10.2).

*Proof strategy:* Show that removing any axiom admits alternatives, and that the conjunction of all five constrains the system to a single architectural class:

- Without A1: Nothing need exist — vacuous satisfaction.
- Without A2: The existent thing need not have computational character — no classification possible.
- Without A3: Any computational class is permissible — no specific dynamics predicted.
- Without A4: No information boundaries — no singularity structure.
- Without A5: No holographic encoding — no dimensional compression.

The conjunction forces: Class 4 dynamics + information boundaries at every scale + holographic encoding + self-referential closure. This is precisely the SB-HC4A definition.

### 7.4 Strengths and Weaknesses of the Formal Argument

**Strengths**: The argument is valid if the axioms and the elimination are accepted. The conclusion follows logically. The use of modal logic makes the necessity claim precise: given a deterministic substrate, any physical universe satisfying the axioms falls in the SB-HC4A architecture class, which leaves its dimension, singularity inventory and temporal structure open.

**Weaknesses**:

1. **A1 is metaphysical**, not mathematical. "Something exists" is not a theorem of any formal system — it is an axiom about reality. The formalization makes this transparent but cannot justify it.

2. **The elimination of Class 5** relies on abduction (physics would be impossible), not deduction. A Class 5 universe that locally appears Class 4 to Class 4 observers is logically consistent — just explanatorily catastrophic. The modal-logical formalization can express this as: the necessity holds *within the scope of A2* (that the system's dynamics are expressible), which may be question-begging if the universe is Class 5 with inexpressible dynamics.

3. **A3 encodes a substantive claim** (that universality, irreducibility and containment single out Class 4) as an axiom. A skeptic could reject A3 — perhaps another class meets these conditions under different assumptions. The axiom's justification is theoretical (universality + containment are unique to Class 4), with self-organized criticality, observed in Class 4 systems, as supporting evidence for how such systems persist rather than as a condition, but it is not a logical necessity.

4. **A5 (holographic encoding)** is well-supported for gravitational systems (AdS/CFT, black hole thermodynamics) but is not proven as a universal principle for all physical systems. The formalization makes this dependence explicit.

---

## 8. Energy-Information Equivalence

### 8.1 The Duality

The cosmological model's Weak Point 1 (Gruber, 2026a, Section 9.1) is the unproven energy-information identity: E = I. The formalization must specify what this means and what it would take to prove.

**Definition (Energy-Information Duality).** Energy and information are dual descriptions of the same physical quantity if there exists a bijection D: E → I (where E is the set of energy configurations and I is the set of information configurations) such that:

(EI1) **Conservation equivalence**: Energy conservation (first law of thermodynamics) is equivalent to information conservation (unitarity of quantum mechanics, no-cloning theorem).

(EI2) **Bound equivalence**: The Bekenstein bound $I_{\max}$ = 2πRE / (ℏc ln 2) is a definitional relationship, not a constraint between independent quantities.

(EI3) **Transformation equivalence**: Every energy transformation corresponds to an information transformation and vice versa, with Landauer's principle (ΔE ≥ kT ln 2 per bit erased) as the marginal exchange rate.

### 8.2 Existing Support

Several results in physics point toward E = I:

- **Landauer's principle** (Landauer, 1961; experimentally confirmed by Berut et al., 2012): Erasing information has a minimum energy cost. This establishes a lower bound on the energy-information exchange rate.

- **The Bekenstein bound** (Bekenstein, 1981): Maximum information content of a region is proportional to its energy content and its radius. If E and I were independent, this bound would be a remarkable coincidence. If E = I, it is a tautology.

- **Black hole thermodynamics** (Bekenstein, 1973; Hawking, 1975): Black holes have entropy S = A / ($4 l_P^2$), temperature T = ℏc³ / (8πGMk), and satisfy the laws of thermodynamics. The information content of a black hole scales with the square of its mass (S = 4πGM²k/ℏc), so it is not proportional to its energy content.

- **The holographic principle** ('t Hooft, 1993; Susskind, 1995): The maximum entropy (= information) of a region scales with surface area, not volume. This is a statement about information density that is simultaneously a statement about energy density.

- **The ER = EPR conjecture** (Maldacena & Susskind, 2013): Einstein-Rosen bridges (wormholes) are equivalent to Einstein-Podolsky-Rosen entanglement (quantum information). Geometry (energy) and entanglement (information) are the same thing.

### 8.3 The Formalization Strategy

A full derivation of E = I would require a fundamental theory of quantum gravity. Short of that, the formalization can specify:

1. **The equivalence conditions** (EI1–EI3) as testable predictions.
2. **The dimensional analysis**: E and I have different units (joules vs. bits). The conversion factor involves fundamental constants: 1 bit = kT ln 2 joules (at temperature T). At the Planck temperature ($T_{P}$ = √(ℏc⁵ / Gk²) ≈ 1.4 × 10³² K), 1 bit = $E_{P}$ ln 2 ≈ 1.36 × 10⁹ J, where $E_{P}$ = √(ℏc⁵ / G) ≈ 1.96 × 10⁹ J is the Planck energy. This is a temperature-dependent rate, not a universal conversion.
3. **The category-theoretic formulation**: E and I are two representations of the same underlying object, related by a natural isomorphism. The category of energy configurations and the category of information configurations are equivalent categories.

---

## 9. The Cognitive Ceiling as a Formal Constraint

### 9.1 The Problem Restated

The deepest objection to the SB-HC4A model (Gruber, 2026a, Section 9.5) is that Class 4 observers may be constitutionally incapable of determining whether the universe is Class 4 or merely appears Class 4 to Class 4 cognition. The formalization must make this objection precise.

### 9.2 Computability-Theoretic Formulation

**Definition (Cognitive Ceiling).** A Class k observer can only detect dynamics up to Class k. Formally: let $O_{k}$ be an observer (measurement/modeling apparatus) of computational class k. Let U be the universe. The observer's model of U is:

M($O_{k}$, U) = $\pi_{k}$(U)

where $\pi_{k}$ is a projection operator that maps U's dynamics onto the subspace of Class ≤ k behavior. If U is Class j > k, then M($O_{k}$, U) = $\pi_{k}$(U) ≠ U — the observer's model is a strict lower-class projection of reality.

**Theorem (Indistinguishability).** A Class 4 observer cannot distinguish between:
- (a) U is Class 4 (and the model is accurate), and
- (b) U is Class 5, but π₄(U) appears Class 4 (and the model is a projection artifact).

*Proof sketch:* By definition, M($O_{4}$, U) = π₄(U). If U is Class 4, then π₄(U) = U and M is faithful. If U is Class 5, then π₄(U) ≠ U but M($O_{4}$, U) = π₄(U) is still Class 4. The observer sees Class 4 in both cases. □

### 9.3 The Self-Referential Trap

This connects to Gödel's incompleteness: the SB-HC4A, if self-referentially closed, contains truths about itself that it cannot prove from within (Section 5.5). Whether U is Class 4 or Class 5 may be one such undecidable truth — a fact about the universe that no internal formal system can determine.

Formally: define the predicate $\mathrm{TrueClass}$(U, k) = "the universe's true computational class is k." The cognitive ceiling theorem states:

¬∃ proof P within U: [P proves $\mathrm{TrueClass}$(U, 4)] ∨ [P proves $\mathrm{TrueClass}$(U, 5)]

if U is computationally universal and embeds formal systems that have U as their subject matter (universality plus embedding, Section 5.5; not from the fixed point alone), by Gödel's first incompleteness theorem applied to those embedded systems.

### 9.4 The Model's Self-Prediction

This is the most remarkable formal feature: the SB-HC4A model *predicts its own potential unfalsifiability*. The cognitive ceiling is not an external objection brought against the model — it is a consequence of the model's own self-referential structure. If the model is correct, then:

1. The universe is a self-referentially closed Class 4 system.
2. Class 4 observers cannot determine whether the universe is Class 4 or Class 5.
3. Therefore, Class 4 observers cannot verify the model — which is exactly what a self-referentially closed system predicts about subsystems' ability to fully characterize the whole.

This is either the deepest confirmation (the model's epistemological predictions are consistent with its ontological claims) or the deepest flaw (the model immunizes itself against falsification). The formalization makes this dilemma precise but cannot resolve it — resolution requires tools from outside the model's own computational class, which, by the cognitive ceiling, are unavailable.

### 9.5 Connection to the Meta-Problem

The self-referential computation framework identifies the Meta-Problem of consciousness (Chalmers, 2018) as structurally identical: a self-modeling system cannot fully model its own substrate because the ESM's self-model is a projection (analogous to π₄), not a faithful representation.

Formally: the ESM's model of the substrate is M(ESM, substrate) = $\pi_{\mathrm{explicit}}$(substrate) ≠ substrate. The substrate has implicit structure that the explicit model cannot access — just as a Class 5 universe would have structure that a Class 4 observer cannot detect.

The cross-scale structural identity functor (Section 6) maps the cosmological cognitive ceiling to the self-referential computation Meta-Problem:

I(cognitive ceiling in Cosmo) = Meta-Problem in SRC

This is the formal expression of the paper's central symmetry claim: the same epistemological limitation operates at both scales, generated by the same self-referential architecture.

---

## 10. Phased Build Order

The formalization project is substantial. A pragmatic build sequence, ordered by the maturity of the relevant mathematical tools and the proximity to existing physics:

### Phase 1: Highest Priority (Connects to Existing Mathematical Physics)

**Module 3 (Sections 3.1–3.7) — Singularity boundaries as equivalence classes and computational atoms.** The mathematical tools exist: causal structure theory (Hawking & Ellis, 1973), the holographic principle ('t Hooft, 1993; Bousso, 2002), black hole thermodynamics (Bekenstein, 1973; Hawking, 1975), loop quantum gravity's area quantization (Rovelli, 2004), and conformal time analysis for temporal asymptotic structure. The expanded scope includes temporal unreachability (Section 3.3), heat death as holographically saturated singularity (Section 3.4), and the formalization of particles as computational atoms (Section 3.7) — stable Planck-scale singularity configurations whose finite spectrum, discrete quantum numbers, interaction grammar, and charge and angular-momentum conservation are derived from the Bekenstein bound and singularity boundary properties. The task is to define the equivalence relation precisely, characterize the temporal boundaries' three-mode no-arrival structure (rather than asserting asymptotic unreachability as a universal consequence of IB1–IB3), establish the entropy saturation boundary condition, and verify the finiteness proposition and conservation law derivation for computational atoms. Wetterich's (2022a, 2022b, 2022c) Grassmann functional integral mapping provides existing formal machinery for the computational atom formalization: his proven CA↔QFT equivalences demonstrate that specific automata produce specific fermionic spectra with specific gauge symmetries, and his spinor gravity automaton (2022c) provides a concrete 4D example satisfying properties analogous to CA1–CA3. The formalization should build on Wetterich's results rather than developing the computational atom framework from scratch. The three-generations conjecture (Section 3.7) is explicitly speculative and requires independent investigation connecting Class 4 self-similarity to the structure of stable boundary configurations. This is a paper-length project for a mathematical relativist, ideally with expertise in cosmological thermodynamics and particle phenomenology.

**Module 5.2–5.3 (Self-referential closure via Lawvere) — The fixed-point argument.** Lawvere's theorem is proven. The application to the SB-HC4A requires specifying the category, the exponential object, and the point-surjection. The cyclic extension (Section 5.6) — formalizing the temporal structure of the fixed point as a bi-infinite sequence of computationally irreducible cycles — requires additional work connecting the fixed-point theory to dynamical systems with temporal boundaries. The CPT alternation conjecture (Section 5.7) is a speculative extension requiring independent investigation but connects to the established CPT-symmetric model of Boyle, Finn, and Turok (2018) and Penrose's (2010) Conformal Cyclic Cosmology. The Big Rip generalization (Section 5.8) — extending the cycle map from single-valued to multi-valued when the terminal boundary is distributed — connects to the theory of branching processes and requires formalization of information partitioning across disjoint Bekenstein-saturated surfaces. This is a paper-length project for a category theorist familiar with Lawvere's work and with background in mathematical physics.

### Phase 2: Core Formalism (Requires Dedicated Development)

**Module 2 (Section 2) — Measure-theoretic class definitions.** The individual measures (topological entropy, Kolmogorov complexity rate, logical depth, Lyapunov exponents, computational reducibility) are well-defined. Class membership is undecidable (Culik & Yu, 1988), and its compression-based formal version is uncomputable (Zenil & Villarreal-Zapata, 2013), so the target is not a proof that sharp class boundaries exist. It is a definition of each class in the limit, a computable approximation for each measure, and a stated error for each approximation, with the existing compression-based classifications (Zenil, 2010; Zenil & Villarreal-Zapata, 2013) as the empirical baseline. The Expressibility Ceiling (Section 2.4) is a conjecture about logical depth and needs an algorithmic information theorist.

**Module 4 (Section 4) — Holographic rule sets.** The AdS/CFT correspondence provides the paradigm case, but the general definition (HR1–HR3) needs development. The coalgebraic formulation (Section 4.4) is the most promising approach but requires original category-theoretic work. Collaboration with researchers working on the interface of quantum gravity and category theory (cf. Baez & Stay, 2011; Abramsky & Coecke, 2004) is recommended.

### Phase 3: Deep Formalism (Hardest, Highest Potential Impact)

**Module 6 (Section 6) — The cross-scale structural correspondence functor.** This requires both the self-referential computation formalization (Gruber, 2026c) and the cosmological formalization to be sufficiently developed. The functor construction is the mathematical expression of the model's strongest claim — that self-referential computational systems and cosmological structure implement the same architecture. Demonstrating that this functor exists, is non-trivial, and preserves the claimed structural properties would be a substantial mathematical achievement.

**Module 4.6 (Section 4.6) — Entanglement as estimation inadmissibility.** The James-Stein Inadmissibility Conjecture requires proving a Stein-type shrinkage theorem on the discrete, finite configuration space of Bekenstein-saturated singularity boundaries. McCormack and Hoff (2022) provide the nearest existing framework (Stein effect for Fréchet means in CAT(0) spaces), but the configuration spaces arising from tensor categories (Levin-Wen models) are not CAT(0). Two approaches are available: (a) embedding into a Hadamard space with controlled distortion (Bourgain-type), or (b) a discrete Laplacian approach. The minimum dimensional requirement (≥ 3 distinguishable states) is comfortably satisfied. The natural loss function (quantum relative entropy or fidelity) connects to Brown's (1971) admissibility theory. This is a paper-length project for a mathematical statistician with background in quantum information geometry.

**Module 7 (Section 7) — The necessity argument in modal logic.** The formal argument depends on the formalization of the axioms and the elimination. The hardest part is the elimination of Class 5 (abductive, not deductive) and the justification of A3 (that universality, irreducibility and containment single out Class 4). A modal logician working with a computability theorist could assess whether the argument is formally valid and what assumptions it requires.

### Phase 4: Speculative Extensions

**Module 8 (Section 8) — Energy-information equivalence.** This depends on progress in quantum gravity. The formalization can specify the equivalence conditions and the testable predictions, but a proof of E = I is beyond current physics.

**Module 9 (Section 9) — Cognitive ceiling formalization.** The computability-theoretic formulation is straightforward; the profound question (whether the model's self-predicted unfalsifiability is a strength or a weakness) is philosophical, not mathematical. The formalization's contribution is to make the question precise.

---

## 11. Scope and Limits

### 11.1 Contributions

**Precision on the central claims.** The verbal model says "singularities are structurally identical at all scales." The formalization says: "singularities belong to the same equivalence class under the relation ~, defined by conditions IB1–IB3." The verbal model says "the cross-scale mapping is not mere analogy but a structural correspondence." The formalization says: "there is conjectured to exist a functor I: Cosmo → SRC preserving computational-architectural structure." These are not interchangeable statements — the formal versions are testable and falsifiable in ways the verbal versions are not.

**Constraint on the model.** A verbally specified "self-referential closure" can mean almost anything. The Lawvere fixed-point formalization constrains it: self-referential closure requires a specific category-theoretic structure (a Cartesian closed category with a point-surjective morphism). If the SB-HC4A's dynamics do not satisfy this structure, the fixed-point argument fails. The formalization turns a vague philosophical claim into a checkable mathematical condition.

**Interoperability with physics.** The singularity equivalence relation connects to black hole thermodynamics, the holographic principle, and loop quantum gravity. The holographic rule set definition connects to AdS/CFT. The Class 4 characterization connects to the theory of critical dynamical systems. The computational atom formalization connects directly to Wetterich's (2022a, 2022b, 2022c) proven CA↔QFT equivalences, which provide the formal bridge between discrete automaton dynamics and continuum field theories. The formalization positions the SB-HC4A model within the existing landscape of mathematical physics, rather than floating free as a verbal speculation.

**Connection to the self-referential computation and RIM formalizations.** The cross-scale structural identity functor (Section 6) and the cognitive ceiling / Meta-Problem connection (Section 9.5) formally link the three-level theoretical architecture: cosmological substrate → self-referential computation → intelligence. The three formalization papers, taken together, specify a single mathematical framework that connects cosmological structure, self-referential computational systems, and intelligence through category-theoretic morphisms.

**Sharpened objections.** The cognitive ceiling formalization (Section 9) makes the model's deepest vulnerability precise: the indistinguishability theorem (Section 9.2) states exactly what a Class 4 observer cannot determine. This is more useful than the verbal formulation — it specifies the exact conditions under which the model is unfalsifiable and the exact sense in which this is a structural prediction rather than an evasion.

### 11.2 Limits

**The formalization cannot prove the axioms.** A1 (something exists) is metaphysical. A3 (universality, irreducibility and containment single out Class 4) is a substantive theoretical claim. A5 (holographic encoding is universal) is conjectural. The formalization derives consequences from axioms; it does not justify the axioms themselves. The model is only as strong as its weakest axiom.

**The formalization cannot resolve the cognitive ceiling.** If the indistinguishability theorem (Section 9.2) is correct, no amount of formal work conducted within the universe can determine whether the universe is truly Class 4 or merely appears so. The formalization makes this limitation precise but cannot overcome it — overcoming it would require computational resources exceeding Class 4, which are by definition unavailable.

**The formalization cannot prove E = I.** Energy-information equivalence depends on a theory of quantum gravity. The formalization specifies what E = I means and what its consequences would be, but the proof (if one is possible) belongs to fundamental physics, not to the formalization program.

**The formalization cannot close the gap between structure and ontology.** Demonstrating that a formal architecture is self-consistent does not demonstrate that the universe instantiates that architecture. Mathematics can show that the SB-HC4A is a well-defined, self-consistent object. Physics must determine whether the universe is an SB-HC4A.

---

## 12. Conclusion

The SB-HC4A cosmological model requires mathematical formalization to constrain its claims, connect to existing mathematical physics, and sharpen both its predictions and its acknowledged vulnerabilities. The formalization strategy proposed here addresses the model's core open questions: What does "Class 4" mean precisely? What is the equivalence relation on singularity boundaries? What does it mean for a rule set to be holographic? What makes entanglement a necessary consequence of shared computational substrates? What category-theoretic structure makes self-referential closure rigorous? In what formal sense is the cross-scale structural mapping a structural identity rather than an analogy?

Nine modules are proposed, spanning measure theory (class definitions), topology (singularity boundaries — now including temporal asymptotic structure, the emptied late universe as horizon-only holographic saturation, and particles formalized as computational atoms with finite spectrum, discrete quantum numbers, interaction grammar, and charge and angular-momentum conservation derived from boundary information theory, with baryon and lepton number predicted to be approximate), category theory (holographic rule sets, self-referential closure, the cross-scale structural identity functor), statistical estimation theory (the James-Stein Inadmissibility Conjecture grounding entanglement as a consequence of estimation inadmissibility on shared Bekenstein-saturated substrates), modal logic (the necessity argument), thermodynamic information theory (energy-information equivalence), and computability theory (the cognitive ceiling). The singularity boundary analysis yields a cyclic temporal structure for the self-referential fixed point: heat death triggers information compression at the Bekenstein-saturated boundary, which decompresses into a new expansion phase — the universe computes its own restart. The cycle sequence is conjectured to be computationally irreducible, consistent with Class 4 dynamics, and may alternate CPT signatures between cycles, connecting to the CPT-symmetric universe model of Boyle, Finn, and Turok (2018) and Penrose's (2010) Conformal Cyclic Cosmology. The Big Rip scenario (Caldwell, 2002) generalizes the cyclic dynamics from a linear sequence to a branching tree: when the terminal boundary fragments into distributed Bekenstein-saturated surfaces, each fragment independently triggers a restart, producing a well-defined multiverse generation mechanism with information conservation across the branching event. The framework is robust across all three cosmological endgames. The James-Stein Inadmissibility Conjecture (Section 4.6) adds a statistical-estimation-theoretic module: if the configuration space of Bekenstein-saturated boundaries satisfies the dimensional and curvature conditions for a Stein-type shrinkage theorem, then independent estimation of particle states on a shared substrate is inadmissible, and the entangled estimator dominates it. This would give the model's identification of entanglement as holographic output (Section 6.1 of Gruber, 2026a) a qualitative grounding in estimation theory; quantitative readings of Bell nonlocality and decoherence would need a further discrete Stein-type theorem. The formalization is not starting from zero: Wetterich's (2022a, 2022b, 2022c, 2022d) proven equivalences between cellular automata and fermionic quantum field theories — including a 4D spinor gravity automaton with exact local Lorentz symmetry — provide concrete formal machinery for the computational atom module, the holographic rule set definition, and the bridge between discrete automaton dynamics and continuum physics. The modular design allows domain specialists to contribute independently, with category theory providing the integration language.

The formalization also achieves a specific meta-theoretical result: it makes precise the model's prediction of its own potential unfalsifiability. The indistinguishability theorem (Section 9.2) — that Class 4 observers cannot distinguish between a Class 4 universe and a Class 5 universe that locally appears Class 4 — is either the model's deepest structural prediction or its deepest flaw. The formalization cannot resolve this dilemma, but it can state it with mathematical precision, which is the prerequisite for any future resolution.

This paper specifies the program. Its execution requires collaboration across mathematical physics, category theory, computability theory, and modal logic. Some of these formalizations may show the model to be wrong in specific, identifiable ways.

---

## References

Abramsky, S., & Coecke, B. (2004). A categorical semantics of quantum protocols. *Proceedings of the 19th Annual IEEE Symposium on Logic in Computer Science*, 415–425.

Aczel, P., & Mendler, N. (1989). A final coalgebra theorem. *Lecture Notes in Computer Science*, 389, 357–365.

Adler, R. L., Konheim, A. G., & McAndrew, M. H. (1965). Topological entropy. *Transactions of the American Mathematical Society*, 114(2), 309–319.

Ashtekar, A., & Lewandowski, J. (2004). Background independent quantum gravity: A status report. *Classical and Quantum Gravity*, 21(15), R53–R152.

Baez, J. C., & Stay, M. (2011). Physics, topology, logic and computation: A Rosetta Stone. *Lecture Notes in Physics*, 813, 95–172.

Bak, P. (1996). *How Nature Works: The Science of Self-Organized Criticality*. Springer.

Bak, P., Tang, C., & Wiesenfeld, K. (1987). Self-organized criticality: An explanation of the 1/f noise. *Physical Review Letters*, 59(4), 381–384.

Barr, M. (1993). Terminal coalgebras in well-founded set theory. *Theoretical Computer Science*, 114(2), 299–315.

Barwise, J. (1974). Axioms for abstract model theory. *Annals of Mathematical Logic*, 7(2–3), 221–265.

Beggs, J. M., & Plenz, D. (2003). Neuronal avalanches in neocortical circuits. *Journal of Neuroscience*, 23(35), 11167–11177.

Bekenstein, J. D. (1973). Black holes and entropy. *Physical Review D*, 7(8), 2333–2346.

Bekenstein, J. D. (1981). Universal upper bound on the entropy-to-energy ratio for bounded systems. *Physical Review D*, 23(2), 287–298.

Bennett, C. H. (1990). Logical depth and physical complexity. In R. Herken (Ed.), *The Universal Turing Machine: A Half-Century Survey* (pp. 227–258). Oxford University Press. https://doi.org/10.1093/oso/9780198537748.003.0008

Berut, A., Arakelyan, A., Petrosyan, A., Ciliberto, S., Dillenschneider, R., & Lutz, E. (2012). Experimental verification of Landauer's principle linking information and thermodynamics. *Nature*, 483, 187–189.

Bourgain, J. (1985). On Lipschitz embedding of finite metric spaces in Hilbert space. *Israel Journal of Mathematics*, 52(1–2), 46–52. https://doi.org/10.1007/BF02776078

Bousso, R. (2002). The holographic principle. *Reviews of Modern Physics*, 74(3), 825–874.

Bowen, R. (1971). Entropy for group endomorphisms and homogeneous spaces. *Transactions of the American Mathematical Society*, 153, 401–414.

Boyle, L., Finn, K., & Turok, N. (2018). CPT-symmetric universe. *Physical Review Letters*, 121(25), 251301. https://doi.org/10.1103/PhysRevLett.121.251301

Brown, L. D. (1971). Admissible estimators, recurrent diffusions, and insoluble boundary value problems. *Annals of Mathematical Statistics*, 42(3), 855–903.

Cardona, R., Miranda, E., Peralta-Salas, D., & Presas, F. (2021). Constructing Turing complete Euler flows in dimension 3. *Proceedings of the National Academy of Sciences*, 118(19), e2026818118.

Caldwell, R. R. (2002). A phantom menace? Cosmological consequences of a dark energy component with super-negative equation of state. *Physics Letters B*, 545(1-2), 23–29.

Caldwell, R. R., Kamionkowski, M., & Weinberg, N. N. (2003). Phantom energy: Dark energy with w < −1 causes a cosmic doomsday. *Physical Review Letters*, 91(7), 071301.

Chaitin, G. J. (1966). On the length of programs for computing finite binary sequences. *Journal of the ACM*, 13(4), 547–569.

Chalmers, D. J. (2018). The meta-problem of consciousness. *Journal of Consciousness Studies*, 25(9-10), 6–61.

Brudno, A. A. (1978). The complexity of the trajectories of a dynamical system. *Russian Mathematical Surveys*, 33(1), 197–198. https://doi.org/10.1070/RM1978v033n01ABEH002243

Cook, M. (2004). Universality in elementary cellular automata. *Complex Systems*, 15(1), 1–40.

Dong, X., Harlow, D., & Wall, A. C. (2016). Reconstruction of bulk operators within the entanglement wedge in gauge-gravity duality. *Physical Review Letters*, 117(2), 021601.

Culik, K., II, & Yu, S. (1988). Undecidability of CA classification schemes. *Complex Systems*, 2(2), 177–190.

Downey, R. G., & Hirschfeldt, D. R. (2010). *Algorithmic Randomness and Complexity*. Springer.

Dubacq, J.-C., Durand, B., & Formenti, E. (2001). Kolmogorov complexity and cellular automata classification. *Theoretical Computer Science*, 259(1–2), 271–285. https://doi.org/10.1016/S0304-3975(00)00012-8

Eckmann, J. P., & Ruelle, D. (1985). Ergodic theory of chaos and strange attractors. *Reviews of Modern Physics*, 57(3), 617–656.

Ferrie, C., & Blume-Kohout, R. (2018). Maximum likelihood quantum state tomography is inadmissible. arXiv:1808.01072.

Gibbons, G. W., & Hawking, S. W. (1977). Cosmological event horizons, thermodynamics, and particle creation. *Physical Review D*, 15(10), 2738–2751.

Gödel, K. (1931). Uber formal unentscheidbare Satze der Principia Mathematica und verwandter Systeme I. *Monatshefte fur Mathematik und Physik*, 38, 173–198.

Goguen, J. A., & Burstall, R. M. (1992). Institutions: Abstract model theory for specification and programming. *Journal of the ACM*, 39(1), 95–146.

Gruber, M. (2015). *Die Emergenz des Bewusstseins*. Lulu Press. ISBN 978-1-326-65207-4. https://doi.org/10.5281/zenodo.23538664

Gruber, M. (2026a). Emergent spacetime from self-referential computation: A hierarchical cellular automaton framework. *Zenodo* preprint. https://doi.org/10.5281/zenodo.18698605

Gruber, M. (2026b). The Four-Model Theory of Consciousness: A simulation-based framework unifying the Hard Problem, binding, and altered states. *Zenodo* preprint. https://doi.org/10.5281/zenodo.18669891

Gruber, M. (2026c). Toward a mathematical formalization of the Four-Model Theory: A recommended approach. *Zenodo* preprint. https://doi.org/10.5281/zenodo.21843693

Gruber, M. (2026d). Toward a mathematical formalization of the Recursive Intelligence Model: A recommended approach. *Zenodo* preprint. https://doi.org/10.5281/zenodo.22133501

Hawking, S. W. (1975). Particle creation by black holes. *Communications in Mathematical Physics*, 43, 199–220.

Hawking, S. W., & Ellis, G. F. R. (1973). *The Large Scale Structure of Space-Time*. Cambridge University Press.

Hertling, P., & Weihrauch, K. (2003). Random elements in effective topological spaces with measure. *Information and Computation*, 181(1), 32–56.

't Hooft, G. (1993). Dimensional reduction in quantum gravity. In *Salamfestschrift* (pp. 284–296). World Scientific.

't Hooft, G. (2016). *The Cellular Automaton Interpretation of Quantum Mechanics*. Springer.

James, W., & Stein, C. (1961). Estimation with quadratic loss. *Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability*, 1, 361–379.

Kripke, S. A. (1963). Semantical considerations on modal logic. *Acta Philosophica Fennica*, 16, 83–94.

Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development*, 5(3), 183–191.

Langton, C. G. (1990). Computation at the edge of chaos: Phase transitions and emergent computation. *Physica D*, 42(1–3), 12–37.

Lawvere, F. W. (1969). Diagonal arguments and Cartesian closed categories. *Lecture Notes in Mathematics*, 92, 134–145.

Maldacena, J. (1998). The large-N limit of superconformal field theories and supergravity. *Advances in Theoretical and Mathematical Physics*, 2(2), 231–252.

Maldacena, J., & Susskind, L. (2013). Cool horizons for entangled black holes. *Fortschritte der Physik*, 61(9), 781–811.

McCormack, A., & Hoff, P. D. (2022). The Stein effect for Fréchet means. *Annals of Statistics*, 50(6), 3647–3676. https://doi.org/10.1214/22-AOS2245

Metzinger, T. (2003). *Being No One: The Self-Model Theory of Subjectivity*. MIT Press.

Moore, C. (1991). Generalized shifts: Unpredictability and undecidability in dynamical systems. *Nonlinearity*, 4(2), 199–230.

Penrose, R. (1979). Singularities and time-asymmetry. In *General Relativity: An Einstein Centenary Survey* (pp. 581–638). Cambridge University Press.

Penrose, R. (2010). *Cycles of Time: An Extraordinary New View of the Universe*. Bodley Head.

Poplawski, N. J. (2010). Cosmology with torsion: An alternative to cosmic inflation. *Physics Letters B*, 694(3), 181–185.

Pour-El, M. B., & Richards, J. I. (1989). *Computability in Analysis and Physics*. Springer.

Rovelli, C. (2004). *Quantum Gravity*. Cambridge University Press.

Rutten, J. J. M. M. (2000). Universal coalgebra: A theory of systems. *Theoretical Computer Science*, 249(1), 3–80.

Ryu, S., & Takayanagi, T. (2006). Holographic derivation of entanglement entropy from the anti-de Sitter space/conformal field theory correspondence. *Physical Review Letters*, 96(18), 181602.

Salmon, W., Strelchuk, S., & Arvidsson-Shukur, D. R. M. (2024). James-Stein estimation in quantum Gaussian sensing. arXiv:2404.02203.

Shew, W. L., & Plenz, D. (2013). The functional benefits of criticality in the cortex. *The Neuroscientist*, 19(1), 88–100.

Susskind, L. (1995). The world as a hologram. *Journal of Mathematical Physics*, 36(11), 6377–6396.

Tsang, M. (2020). Physics-inspired forms of the Bayesian Cramér-Rao bound. *Physical Review A*, 102(6), 062217. https://doi.org/10.1103/PhysRevA.102.062217

Verlinde, E. (2011). On the origin of gravity and the laws of Newton. *Journal of High Energy Physics*, 2011(4), 29.

Wetterich, C. (2022a). Fermion picture for cellular automata. *arXiv preprint*, arXiv:2203.14081.

Wetterich, C. (2022b). Fermionic quantum field theories as probabilistic cellular automata. *Physical Review D*, 105(7), 074502.

Wetterich, C. (2022c). Cellular automaton for spinor gravity in four dimensions. *arXiv preprint*, arXiv:2211.09002.

Wetterich, C. (2022d). Quantum fermions from classical bits. *Philosophical Transactions of the Royal Society A*, 380(2216), 20210066.

Wolfram, S. (2002). *A New Kind of Science*. Wolfram Media.

Zenil, H. (2010). Compression-based investigation of the dynamical properties of cellular automata and other systems. *Complex Systems*, 19(1), 1–28. https://doi.org/10.25088/complexsystems.19.1.1

Zenil, H., & Villarreal-Zapata, E. (2013). Asymptotic behavior and ratios of complexity in cellular automata. *International Journal of Bifurcation and Chaos*, 23(9), 1350159. https://doi.org/10.1142/S0218127413501599

Zvonkin, A. K., & Levin, L. A. (1970). The complexity of finite objects and the development of the concepts of information and randomness by means of the theory of algorithms. *Russian Mathematical Surveys*, 25(6), 83–124.
