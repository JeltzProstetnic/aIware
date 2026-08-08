# Emergent Spacetime from Self-Referential Computation: A Hierarchical Cellular Automaton Framework

**Matthias Gruber**

*Independent researcher*

*ORCID: 0009-0005-9697-1665*

*Correspondence: matthias@matthiasgruber.com*

---

## Abstract

This paper proposes a cosmological model — the Singularity-Bounded Holographic Class 4 Automaton (SB-HC4A) — derived from the convergence of four independently motivated frameworks: a five-class computational taxonomy that refines Wolfram's (2002) classification by separating fractal from random dynamics, a theoretical framework for self-referential computation in self-modeling systems (Gruber, 2015, 2026a, 2026b) which identifies self-referential computation at criticality as a universal computational pattern, and 't Hooft's (1993, 2016) holographic automaton interpretation of quantum mechanics. Conditional on the assumption that the universe's substrate is deterministic, the model proceeds by elimination: Classes 1–3 cannot sustain the computationally irreducible dynamics the universe demonstrably exhibits; ontic (lawless) randomness would render the success of physics inexplicable; the universe is therefore best characterized as operating at Class 4 — the edge of chaos. Combined with the information-theoretic observation that singularities at every physical scale (Planck regime, particle interiors, event horizons, cosmological horizons, temporal endpoints) share the property of information impermeability and holographic saturation, the model proposes that these singularities are reflections of a single encoding surface — scale-invariant presentations of one information boundary, argued from a single-surface ontology, and connected to (though not established by) the Kerr-Newman black hole/particle correspondence (Carter, 1968; Burinskii, 2008), where black holes and elementary particles share the same characterizing properties (mass, charge, angular momentum) including the electron's gyromagnetic ratio g = 2 — a correspondence that carries an unresolved scale and horizon tension. The resulting architecture is a self-referential holographic Class 4 automaton bounded at every scale by singularity surfaces, where the observable interior is the *decompressed* form and the singularity boundary the *compressed* substrate. Event horizons and the cosmological horizon recede asymptotically from every approach within the computational domain; the temporal termini (the Big Bang and a possible Big Crunch) terminate world-lines at finite proper time yet are never reached as events — a distinct mode of unreachability — and it is information impermeability, shared by every member of the inventory, on which the unification rests. Because singularities transform rather than destroy information, heat death is argued to constitute a singularity transition that triggers cyclic renewal — conditional on a saturation-instability conjecture the paper identifies as one of its weak points — with potential CPT signature alternation across cycles, connecting to Penrose's Conformal Cyclic Cosmology and Boyle and Turok's CPT-symmetric universe. All three cosmological endgames — heat death, Big Crunch, and Big Rip (Caldwell, 2002) — leave a holographically saturated boundary, with the Big Rip uniquely producing a branching tree of daughter universes rather than a linear successor; current data disfavour the Big Rip branch without excluding it (DESI Collaboration, 2025). This architecture structurally corresponds to self-referential computational systems that operate at criticality, where implicit knowledge (substrate) is separated from explicit representation by an information-opaque boundary. Self-modeling cognitive systems are thus argued to be local, scale-reduced instances of the same computational pattern the universe implements globally. Seven weak points are identified, including the fundamental epistemological objection that Class 4 observers may be constitutionally incapable of determining whether this model describes the universe or merely the ceiling of their own computational capacity.

**Keywords**: cosmology, cellular automata, holographic principle, criticality, singularity, computational complexity, edge of chaos, self-referential closure, cyclic cosmology, CPT symmetry, Big Rip, phantom energy, emergent spacetime

---

## 1. Introduction

### 1.1 The Problem

A fundamental question in cosmology is: *Why does the universe have the structure it has?* This paper proposes that the universe's architecture — its dynamics, boundaries, and self-organizing properties — follows from a unique computational pattern: self-referential computation at criticality. This pattern appears not only at cosmological scales but also in self-modeling cognitive systems, suggesting a universal principle rather than a cosmic accident.

The argument proceeds from structural constraints. If certain axioms hold — ontological necessity, computational character, criticality stability, information bounds, and holographic encoding — then a unique architecture emerges: a self-referential holographic automaton operating at the edge of chaos, bounded at every scale by information-impermeable singularities. This is presented not as the unique possible structure but as the best-supported configuration for a system that computes its own existence — the architecture its premises most strongly motivate (Section 10).

### 1.2 Sources and Scope

The model presented here draws on four bodies of work:

1. **The Five-Class Computational Taxonomy** (Gruber, 2015), which refines Wolfram's (2002) four-class classification of dynamical systems by splitting his Class 3 ("random") along the line of computational *reducibility* — the reducible, self-similar cases (genuine fractals) becoming the new Class 3, the irreducible cases such as Rule 30 re-filing with Class 4, and a new Class 5 reserved for genuine, ontic randomness. This produces a clean monotonic gradient from order to disorder and reveals that Class 4 — the edge of chaos — is the maximum complexity achievable by expressible rules.

2. **A framework for self-referential computation** (Gruber, 2015, 2026a, 2026b), originally developed in the context of self-modeling systems, which identifies self-referential computation at criticality as a universal computational pattern. The framework distinguishes implicit knowledge (substrate-level representation) from explicit representation (decompressed representational content), with an information-opaque boundary between them, and establishes self-referential closure as a fixed point: Φ(m*) = m*. This pattern appears in any system that models its own modeling processes.

3. **The Holographic Automaton Interpretation** ('t Hooft, 1993, 2016), which proposes that quantum mechanics emerges from deterministic dynamics at the Planck scale — that the universe is fundamentally a cellular automaton whose holographic structure produces quantum behavior as an emergent phenomenon. Recent work by Wetterich (2022a, 2022b, 2022c) has demonstrated that this is not merely philosophical — specific cellular automata are mathematically equivalent to fermionic quantum field theories, including a model of spinor gravity in four dimensions with exact local Lorentz symmetry.

The model is speculative. It is not a proof. It is a logical argument chain that, if the premises hold, yields a specific cosmological architecture. The paper presents the argument, identifies where it could break, and proposes what would count as evidence for or against it.

### 1.3 Acknowledgment

The importance of symmetries in physical theory — the methodological principle that drove this work — was impressed upon me by my uncle, Bruno J. Gruber, a theoretical physicist who has spent his career working on symmetry groups in quantum mechanics (Gruber, 1968, 1980). The observation that the same computational architecture might appear at multiple scales is, at bottom, a symmetry claim. Whatever merit it has owes much to his influence.

The self-referential computation framework draws on Thomas Metzinger's self-model theory of subjectivity (Metzinger, 2003) as a source for the computational pattern, though the present work applies it to cosmological rather than cognitive questions. The idea that the universe might be a cellular automaton operating under holographic constraints was already present in embryonic form in my 2015 book, where 't Hooft's holographic bound was discussed in a cosmological context (Gruber, 2015, pp. 79–80). The full SB-HC4A architecture developed here represents the mature formulation of those early intuitions.

---

## 2. The Five-Class Framework

### 2.1 Wolfram's Classification and Its Problem

Wolfram (2002) classified the behavior of cellular automata into four classes based on their long-term dynamics:

| Wolfram Class | Behavior | Example |
|:---:|---|---|
| 1 | Uniform (converges to fixed state) | Rule 0 |
| 2 | Periodic (settles into repeating loops) | Rule 4 |
| 3 | Random/chaotic (apparently random) | Rule 30 |
| 4 | Complex (persistent interacting structures) | Rule 110 |

This classification was genuinely useful and applied far beyond cellular automata — to fluid dynamics, biological systems, economic models, and neural networks. But Wolfram's Class 3 was a grab-bag containing two structurally different phenomena: fractal systems like Rule 90 (which generates a Sierpinski triangle — computationally *reducible*, meaning you can calculate any cell without running the full simulation) and apparently chaotic systems like Rule 30 (which produces output that *looks* random but is completely deterministic and computationally *irreducible*).

Nestedness by itself will not draw the line between them, and Rowland (2006) is the reason why. He showed that Rule 30 produces *local* nested structure: at row 2ⁿ a region of the initial condition reappears at the right edge and the automaton begins again locally, a consequence of Rule 30 being reversible in time whenever the right half of each row is white — and the result generalizes to k-color rules with the same bijectivity property. Nested structure is therefore present in both members of the grab-bag, and a classification keyed to its visible presence would put Rule 30 back with Rule 90. What separates them is computational *reducibility*: Rule 90's nesting comes with a closed form, Rule 30's does not. Drawing that line instead does two things at once: it moves the reducible, fractal members (Rule 90) into a class of their own, and it reveals that the irreducible members (Rule 30) belong with Rule 110 at the top of the expressible hierarchy — leaving a fifth slot, beyond all expressible rules, for genuine randomness. These differences matter for cosmology.

### 2.2 The Five Classes

The refined classification, ordered as a monotonic gradient from most ordered to most disordered:

**Class 1 — Static.** Systems that converge to a fixed state. Period: 1. No computation.

**Class 2 — Periodic.** Systems that settle into repeating loops. Information is stored but never transformed. Period: finite.

**Class 3 — Fractal.** Systems that produce self-similar structure at every scale and are computationally *reducible*: a closed-form description exists that lets you compute any cell without running every step. Rule 90 is the paradigm — its evolution is Pascal's triangle modulo 2, the Sierpinski triangle. Structure without processing power. Period: quasi-infinite with exact or statistical self-similarity.

**Class 4 — Complex (edge of chaos).** Systems that are computationally *irreducible* — no closed form, no shortcut: the only way to determine their future is to run them (Wolfram, 2002). Irreducibility is the defining criterion of the class; its other characteristic features accompany it. Class 4 systems produce persistent localized structures capable of interacting and of carrying computation — Rule 110's glider interactions have been harnessed to prove it capable of universal computation (Cook, 2004), and given the right initial conditions, a universal Class 4 system can simulate any algorithm, including itself. This is where self-referential computation emerges. The class also contains the deterministic systems whose output merely *looks* random: Rule 30's irreducible dynamics produce effective randomness (Section 2.4). Visible complexity and apparent randomness are two faces of the same irreducibility.

**Class 5 — Random.** Systems whose output is genuinely — *ontically* — random: maximal Kolmogorov complexity, incompressible, non-algorithmic. The generating process, if it deserves the name, exceeds what formal symbolic systems can express: there is no rule. No deterministic automaton occupies this class (Section 2.3); it is defined by exclusion, as the territory beyond the expressibility ceiling.

### 2.3 Why Deterministic Rules Cannot Produce Genuine Randomness

A cellular automaton has a finite rule table and a finite initial condition — together, a fixed finite amount of information. A truly random infinite sequence has maximal Kolmogorov complexity and cannot be compressed to anything shorter than itself. Therefore, no deterministic automaton can produce genuinely random output: the output's complexity is bounded by the rule-set's complexity (Kolmogorov, 1965; Chaitin, 1966).

This is a generalized pigeonhole argument. The only way to generate infinite output from finite information is to reuse structure — but reuse comes in deterministic modes that must be kept apart, because they ground the class boundaries. Exact reuse is periodicity (Class 2). *Reducible* patterned reuse is fractal behavior (Class 3): Rule 90 generates the Sierpinski triangle, and any cell of its evolution can be computed directly from binomial coefficients modulo 2 — a closed form that lets you skip ahead without running the automaton. *Irreducible* reuse is Class 4 behavior: Rule 30, Rule 110, and Conway's Game of Life produce structure with no such closed form — no shortcut to the future exists, and the only way to find out what the system does is to run it. Their output remains bounded in complexity by their rule-set, hence compressible in principle and never genuinely random; but it is statistically random-looking and unpredictable except by simulation. This is the effective randomness that Section 2.4 distinguishes from the ontic randomness of Class 5.

This split corrects a tempting mislabel. Rule 30 is not a fractal: it has visible structure — triangular motifs at many scales, a regular left edge — but no closed form behind that structure, and its center column is aperiodic as far as it has been computed (it has served as a practical pseudorandom generator for decades). Rule 90 is the genuine fractal; Rule 30 is deterministic effective randomness. What Wolfram's Class 3 grouped together, the reducibility criterion separates: the reducible members (Rule 90) form the new Class 3, while the irreducible members (Rule 30) belong with Rule 110 in Class 4. The new Class 5 is reserved for what neither exemplifies — ontic randomness, the output of no expressible rule at all.

One caveat about the boundary itself. The Class 3/Class 4 distinction cannot be drawn algorithmically: Culik and Yu (1988) proved that classifying an arbitrary cellular automaton into Wolfram-style behavioral classes is formally undecidable — no general procedure takes a rule and returns its class. Class-membership claims therefore rest on case-by-case mathematical facts and, where those run out, on conjecture. Rule 90's reducibility is a theorem (the closed form exists). Rule 110's universality is a theorem (Cook, 2004). Rule 30's irreducibility is a conjecture — as is Wolfram's (2002) Principle of Computational Equivalence, which holds that almost all systems whose behavior is not obviously simple are computationally equivalent, and hence that Rule 30 is itself universal. Nothing here claims that Rule 30 *cannot* support universal computation; the difference between Rule 30 and Rule 110 is programmability, not proven computational power — Rule 110's gliders can be harnessed into a known construction, while Rule 30's computation, if universal, is illegible to us. This undecidability is consistent with the epistemic status the model claims for itself: the Class 4 classification of the universe is empirical, not a theorem (Section 9.2).

### 2.4 Class 4 as the Expressibility Ceiling

Classes 1 through 4 are what finite, expressible rules can produce. Class 5 requires rules that cannot be written down — if the rule were expressible, the output would be compressible (to: "apply this rule"), and therefore not truly random.

This makes available a distinction the cosmological argument will depend on, so it is worth drawing precisely. Call randomness **ontic** when there is no generating rule at all — when the dynamics are lawless, exceeding what any formal system can express. This is Class 5, and only Class 5. Call randomness **effective** when a deterministic, expressible rule produces output that is statistically indistinguishable from randomness and unpredictable in practice. Effective randomness has two sources, and a Class 4 system supplies both. The first is computational irreducibility (Wolfram, 2002): there is no shortcut to the system's future — prediction requires running the dynamics step by step, which is no faster than the system running itself. The second applies specifically to embedded observers: an observer inside a self-referential Class 4 system is a subprocess of the very computation it is trying to predict, with strictly fewer resources than the whole (Section 2.5). For such an observer, unpredictability is not a practical limitation but a structural one. On this view, the observed randomness of quantum measurement can be read as effective rather than ontic — the position developed in 't Hooft's (2016) cellular automaton interpretation of quantum mechanics, which Section 3.2 adopts as an explicit assumption.

Class 4 is therefore the *maximum complexity achievable by expressible rules*. It is as complex as mathematics can get — up to and including output that no statistical test distinguishes from genuine randomness. Beyond it lies only territory that formal systems, by their own nature, cannot map.

This observation — that expressible computation has a ceiling, that the ceiling is Class 4, and that everything beneath the ceiling, effective randomness included, is deterministic — is the first premise of the cosmological argument.

### 2.5 Class 4 Contains All Classes Including Itself

A critical property: Class 4 automata can generate Class 1 behavior (stable states), Class 2 behavior (oscillations), and Class 3 behavior (fractal patterns) as subprocesses within their own dynamics. No lower class can do this. The Game of Life, for instance, contains still lifes (Class 1), blinkers (Class 2), and self-similar growth patterns (Class 3) as embedded phenomena within its Class 4 dynamics.

This containment property means that a Class 4 universe does not merely permit lower-class phenomena — it *generates* them. Static matter, periodic orbits, fractal coastlines, and self-similar galaxy distributions are all Class 4 subprocesses.

But the most consequential containment is self-containment: Class 4 automata can contain Class 4 automata as subprocesses. This follows directly from universality — a Turing-complete system can simulate any Turing machine, including another Turing-complete system (Cook, 2004, proved this for Rule 110). No lower class possesses this property; Classes 1–3 cannot generate dynamics at or above their own complexity. Class 4 is the only class that can nest instances of itself within its own dynamics. The contained instance is necessarily resource-constrained — fewer effective cells, slower clock — but it is genuinely Class 4: capable of universal computation, supporting criticality, and itself capable of containing further Class 4 subprocesses. This self-nesting property is the structural foundation for the cross-scale identity developed in Section 7: if the universe is a Class 4 automaton, then any sufficiently complex subsystem operating at criticality within it — including a brain — is itself a Class 4 automaton embedded within the larger one.

---

## 3. The Case for a Class 4 Universe

### 3.1 The Ontological Starting Point

Pure nothingness cannot exist as a state of affairs, and the reason is not that nothingness is difficult to picture. Anyone asserting that it can must say what is being asserted, and the claim admits only two forms: either the nothing is somewhere or somewhen, or it is not. Both fail, and between them they exhaust the options.

**The first horn: a located nothing.** To place a nothing — before the Big Bang, after a vacuum decay, in some other possible world — is to fix it relative to what actually exists. Fixing anything relative to anything implies a separation between the two, and a separation implies a dimension along which it obtains. The act of saying where or when the nothing is therefore supplies it with a position in a structure, and whatever has a position has a property. The candidate is disqualified by the very move that was supposed to introduce it.

The natural objection is that such relations are merely extrinsic — Cambridge properties, which cost their bearer nothing, as being thought about costs Socrates nothing. They are not free here. Occupying a position in a temporal or spatial order is not like being thought about; it is a determination of what the thing is. This is why cosmology says there was no time *before* the Big Bang rather than that there was nothing before it: "nothing, and then something" smuggles in a temporal frame for the nothing to sit in, and a frame is already something. Section 5.3 reaches the same conclusion about the temporal termini by an independent route.

The physical and modal candidates fail as instances of exactly this. A decay to true vacuum does not terminate in nothing: a true vacuum is an energy level *below* the present one, which presupposes an ordered range of levels for it to lie below, and zero field content at a level does not make the level nothing. A possible world containing nothing is a cell with no content in a space of rule-sets, and a plurality of worlds is a structure whether or not one of its members happens to be empty. In each case what has been described is a universe with nothing *in* it — unobjectionable, and quite possibly correct — and not nothingness. Specifying a state takes a state space, and a state space is something.

**The second horn: an unlocated nothing.** A nothing that is nowhere and nowhen in particular escapes all of the above, and it is the only form in which the claim stays true to its own name. But unqualified is now what it is: the assertion has become that there is nothing, everywhere and everywhen. That claim is refuted by anything whatever — including, immediately and without further argument, by the existence of whoever is in a position to assert it. There is no third form available, because the nothing either has a where and a when or it does not; so the disjunction is not a rhetorical device but the whole of the case.

A second line reaches the same conclusion from the side of evidence, and it does different work. Nothing has ever been observed to come from nothing; every origination on record is a rearrangement of something already present. Taken alone that is induction, and induction is what a critic will say has no purchase on the origin of the universe. But the case is not merely unobserved — it is unobservable in principle. To observe a state of affairs is to stand in some spacetime relation to it, and whatever stands in a spacetime relation to an observer is not nothing: the observer's own presence is already a counterexample to what was to be observed. No evidence for a state of nothingness is available, then, by any means at any time, and the induction cannot be overturned by observation because no observation is to be had on either side. The burden falls to whoever claims the exception. This is the structure Section 5.3 finds at the temporal termini and Section 9.5 identifies at cosmic scale: a boundary that is never an element of the domain.

One deflationary reply deserves recording, since it is the last exit. It denies that modal talk posits anything at all — possible worlds as maximal consistent sets of propositions, or as a manner of speaking, so that "possibly, nothing exists" carries no commitment to any plurality. This rescues the claim by emptying it. Maximality and consistency are themselves structural notions and a set of propositions is no less a something than a space of worlds; while if the locution is instead held to describe no way reality could be, it no longer contradicts anything asserted here. On the first reading the nothing is a something; on the second there is no claim.

The question itself is old — Leibniz ("Why is there something rather than nothing?"), Heidegger's reformulation of the fundamental question of metaphysics — and remains live: Krauss (2012) and Albert (2012) reach opposite conclusions about whether physics has anything to say about it, Albert's objection being that the "nothing" of quantum cosmology is a vacuum state with fields and therefore not nothing at all. That objection is granted here, and is an instance of the first horn. I accept as Axiom 1: something exists.

Whatever exists must have some dynamical character — if it had none, it would be indistinguishable from nothing by the Identity of Indiscernibles (Leibniz, 1686). Therefore, whatever exists has dynamics classifiable within the five-class hierarchy.

### 3.2 The Elimination Argument

Before the elimination, one assumption must be stated explicitly, because the scope of the argument depends on it. **Assumption (substrate determinism).** The model assumes that the universe's fundamental dynamics are deterministic — that the apparent indeterminism of quantum mechanics is effective rather than ontic (Section 2.4), emerging from deterministic dynamics at the substrate level, as in 't Hooft's (2016) cellular automaton interpretation of quantum mechanics. This is an assumption, not a conclusion: nothing in the five-class framework derives it. It is stated once, here, and it does double duty — it scopes the elimination below, which classifies deterministic ontologies, and it is the same premise on which the treatment of entanglement and Bell correlations in Section 6.5 relies. A reader who rejects it — who takes the Born rule to be a fundamental stochastic law — should read everything that follows as conditional: *given* a deterministic substrate, the universe is Class 4 by elimination.

**Classes 1 and 2** (static, periodic): The universe demonstrably contains self-organizing critical systems, including biological computation which requires Class 4 dynamics (supported by empirical criticality research: Beggs & Plenz, 2003; Shew & Plenz, 2013; Algom & Shriki, 2026; and theoretical work on self-referential computation: Gruber, 2015, 2026a). A Class 1 or 2 universe cannot generate Class 4 subprocesses (lower classes cannot produce higher-class behavior). Eliminated.

**Class 3** (fractal): A fractal universe would be computationally *reducible*: like Rule 90, its entire history would be available in closed form, predictable without being run — rich structure, but no processing. The universe demonstrably performs computationally irreducible computation: we build Turing machines, and biological systems perform irreducible computation at criticality. Universality serves here as *evidence* of irreducibility — a universal machine's behavior cannot in general be predicted by any shortcut — rather than as the class criterion itself, which the reducibility split of Section 2.2 supplies. Eliminated.

**Class 5** (ontic randomness): The elimination targets *ontic* randomness only — lawless dynamics, generated by no expressible rule (Section 2.4). If the universe's fundamental dynamics were ontically random, then physics is not merely incomplete but *fundamentally impossible*. The project of writing down laws that predict observations would be an illusion. Our local experience of lawful behavior would be a temporary, coincidental pocket of apparent regularity within genuine randomness — an infinitesimally improbable fluctuation with no mechanism guaranteeing its continued existence. Not logically impossible, but explanatorily empty — it renders the success of physics inexplicable. Eliminated abductively. Two clarifications keep this elimination honest. First, *effective* randomness — including the observed randomness of quantum measurement — is not eliminated; it is *predicted*: Class 4 irreducibility produces exactly the deterministic-but-unpredictable behavior we observe (Section 2.4). Second, the remaining alternative — a lawful but irreducibly stochastic universe, with the Born rule as fundamental law — is removed by the substrate-determinism assumption stated above, not by argument. The five-class taxonomy spans deterministic generators (Classes 1–4) and lawlessness (Class 5); its exhaustiveness is scoped to deterministic ontologies.

**Class 4** (complex, edge of chaos): The universe operates at the maximum expressible complexity. It supports universal computation (demonstrated by the existence of Turing machines and biological computation). It self-maintains criticality — Class 4 dynamics are self-organizing in complex systems (Bak, Tang, & Wiesenfeld, 1987; Bak, 1996). It contains all lower classes as subprocesses (the universe demonstrably contains static matter, periodic phenomena, and fractal structure). It is the *only* class that does all of these simultaneously.

**Conclusion (Proposition 1, conditional)**: Given a deterministic substrate, the universe operates at Class 4 — the edge of chaos — by elimination. Class 4 is the most parsimonious classification consistent with observation, conditional on the substrate-determinism assumption.

The SB-HC4A's ontological starting point should be distinguished from Tegmark's (2008) Mathematical Universe Hypothesis, which asserts that all consistent mathematical structures are physically real. The elimination argument moves in the opposite direction: rather than admitting every structure, it selects. Where Tegmark's framework is maximally permissive (every structure exists), the present argument is selective — among deterministic ontologies, Class 4 is the best candidate: the only class consistent with the observations cited above, and the class the remainder of the architecture requires. This is deliberately a weaker claim than uniqueness of the resulting *model*: the elimination selects a computational class, not a single architecture, and Section 10 returns to what the axioms do and do not pin down.

### 3.3 The Strength of the Elimination

The elimination argument is not deductive proof, and it is conditional. Two of the eliminations are empirical (Classes 1–2: the universe contains self-organizing critical systems; Class 3: the universe performs computationally irreducible computation), one is abductive (Class 5: ontic lawlessness would make the success of physics inexplicable — an explanatory catastrophe, not a logical contradiction), and one alternative is removed by assumption rather than argument (a lawful but fundamentally stochastic universe, excluded by the substrate-determinism assumption declared in Section 3.2). Only the affirmative case for Class 4 combines empirical evidence with a theoretical mechanism (self-organized criticality).

The argument is strongest read as: *given a deterministic substrate, Class 4 is the unique class consistent with all observations and the only class that provides a self-maintaining mechanism for its own persistence.* Read unconditionally, it identifies Class 4 as the best candidate classification — characteristic of the universe we observe, not proven necessary.

---

## 4. Quasi-Infinity and Information Horizons

### 4.1 The Speed Limit and Its Consequences

Information cannot travel faster than c (Einstein, 1905). The universe is expanding, and the expansion is accelerating (Riess et al., 1998; Perlmutter et al., 1999). Together, these facts create a fundamental horizon: for any observer, there exists a maximum distance in space and maximum duration in time from which information can reach them. Beyond this horizon, the universe is informationally inaccessible.

This makes the universe **quasi-infinite** rather than truly infinite. From within, it appears unbounded. But information can never traverse more than approximately one universe-diameter in any direction (spatial or temporal). This is not merely an observational limitation — it is an ontological boundary. In the ontology developed in Section 5, a region beyond an information horizon has no existence independent of its boundary encoding: everything physics can mean by "what lies beyond" is exhausted by the information encoded on the horizon itself. The boundary does not conceal a further fact; it is where the facts are.

### 4.2 The Concept of Quasi-Infinity

I define **quasi-infinity** as the condition of a system that is effectively unbounded for any internal observer but has a finite information content accessible from any given point. Quasi-infinity is distinct from both mathematical infinity (no bound exists) and finitude (a bound is reachable and inspectable). A quasi-infinite system is bounded by surfaces that limit information rather than by edges that can be examined: its bounds either recede faster than any observer can approach them (horizons), retreat in resolution as they are probed in energy (the Planck floor), or terminate information access — ending world-lines without arrival — while revealing nothing beyond (curvature termini).

The universe is quasi-infinite in space (the observable universe is finite; expansion pushes the boundary outward faster than light). It is quasi-infinite in time, in a sense Section 5.3 makes precise: the heat-death future is approached asymptotically and never arrives at any finite time, while the Big Bang — and a Big Crunch, if the universe recollapses — are termini that world-lines reach at finite proper time but across which no information passes in either direction. And it is, I will argue, quasi-infinite in scale.

### 4.3 Scale as a Quasi-Infinite Dimension

The universe presents singularities not only at the boundaries of space and time but at the boundaries of scale:

- At the smallest scale (~10⁻³⁵ m, the Planck regime), spacetime itself loses physical meaning. No measurement below this scale is possible, even in principle (Planck, 1899; Wheeler, 1957).
- At the largest scale, the observable universe boundary is set by the expansion history and the speed of light. Beyond it: informationally inaccessible.

That scale functions as a genuine dimension — and not a mere bookkeeping parameter — is already implicit in the structure of modern physics. The renormalization group (Wilson, 1971) describes how physical couplings flow systematically as a function of scale, much as fields vary as a function of position: the effective laws at one scale are related to those at another by a definite flow, and effective theories occupy positions along this scale axis. The SB-HC4A takes this dimensional character literally: scale is an axis of the computational domain, bounded — like space and time — by information horizons at its extremes.

Between these extremes, the universe spans approximately 60 orders of magnitude in length scale. Both endpoints are singularities — regions where our physical description breaks down and information transfer becomes impossible. The universe is quasi-infinite in scale in the same sense it is quasi-infinite in space and time: effectively unbounded from within, but bounded by information horizons at both extremes.

---

## 5. Singularities as Information Boundaries

### 5.1 The Singularity Inventory

At every physical scale, the universe presents singularities — regions where physical description breaks down and information transfer ceases:

| Scale | Singularity | Information Property |
|---|---|---|
| Planck (~10⁻³⁵ m) | Planck regime | Below this, spacetime loses meaning. No measurement possible. |
| Subatomic (~10⁻¹⁵ m) | "Point-like" particles | Treated as zero-dimensional; actually Planck-sized. Interiors inaccessible. |
| Stellar/galactic | Black hole event horizons | Information cannot escape. Interior causally disconnected from exterior. |
| Cosmological (space) | Observable universe boundary | Expansion + c creates impenetrable information horizon. |
| Cosmological (time, past) | Big Bang | All world-lines converge. No "before" is accessible. |
| Cosmological (time, future) | Heat death / Big Crunch / Big Rip | Infinite dilution, reconvergence, or divergent expansion (Caldwell, 2002) — in every case, a terminus of accessible information. |

### 5.2 The Unification Claim

These singularities share a structural property: they are all **information-impermeable boundaries** — surfaces across which no signal passes. I propose they are not merely analogous but *structurally identical*: not six different boundaries that happen to share properties, but six presentations of one boundary — local reflections, at different scales and locations, of a single encoding surface.

The argument proceeds in four steps.

**Step 1: Holographic saturation.** Two distinct bounds are in play here, and only one of them is the Bekenstein bound. The Bekenstein bound (Bekenstein, 1981) limits the entropy of a system of energy E confined within a sphere of radius R to S ≤ 2πkER/ħc — a bound set by energy and radius, not by area, and one whose rigorous modern form is a relative-entropy inequality in quantum field theory (Casini, 2008). The area law is a separate result: the holographic bound of 't Hooft (1993) and Susskind (1995), S ≤ A/4ℓ_P², in Bousso's (1999) covariant formulation. It is the area law that the argument below requires.

The two coincide at the threshold of gravitational collapse. Load a region of fixed radius with energy until R approaches its Schwarzschild radius, and the Bekenstein bound reduces to the area law — at that threshold, energy × radius *is* area. Event horizons sit exactly there, which is why they saturate both bounds at once and carry entropy A/4ℓ_P² (Bekenstein, 1973; Hawking, 1975). The property shared across the singularity inventory is accordingly saturation of the *area* bound, which I will call **holographic saturation**; for the horizons it is saturation of the Bekenstein bound as well, and the two coincide only there. The holographic principle then generalizes the encoding claim: the information content of any region is encoded on its boundary.

**Step 2: Scale invariance.** If the universe is a Class 4 system (Proposition 1), its dynamics are self-similar — structure at one scale recurs at other scales. Class 4 systems contain Class 3 (fractal) behavior as a subprocess, and fractal behavior is defined by scale invariance. The boundary structure of a Class 4 system should itself be scale-invariant.

**Step 3: Shared boundary properties.** All singularities in the inventory (Section 5.1) share the same three properties: **(IB1)** information impermeability, **(IB2)** holographic saturation (or its scale-appropriate equivalent), and **(IB3)** they bound the computational domain — they define the limits of what can be computed from within. The claim is that these are not six different phenomena that happen to share properties, but one phenomenon — the boundary of the automaton's computational domain — encountered at six different scales.

**IB1 is a two-tier property.** Semiclassically — in effective field theory on a fixed background, which is the description an interior observer has — a horizon is an exact one-way membrane: no signal crosses it outward, and the region behind it is causally sealed. Non-perturbatively this fails, and the modern treatment of the information paradox says precisely how it fails. Information that falls into a black hole is recoverable from the Hawking radiation after the Page time (Penington, 2020; Almheiri et al., 2021), and on the holography-of-information results there is no bulk information that is not already available at the boundary (Raju, 2022; Bahiru et al., 2024). Section 8.2 endorses that resolution. IB1 therefore cannot mean that information is destroyed at a boundary, or withheld from the substrate.

It does not mean that. The impermeability the inventory shares is impermeability *within the computational domain*: of the decompressed interior description to itself, across the boundary. That the same information is meanwhile fully present on the boundary is not an exception to the architecture but its content — compressed on the surface, unreadable from inside, decompressed elsewhere as more interior (Section 8.2). The two tiers are the substrate/interior split stated in the vocabulary of black-hole physics, and IB1 is the claim that the interior cannot read its own substrate. What would break the unification is a signal crossing a boundary *within* the interior description — an observer who stays inside the domain and receives information from behind a horizon. Neither the island results nor the holography of information supplies that: both relocate the information to the boundary, which is where this model already puts it.

The ER=EPR conjecture (Maldacena & Susskind, 2013) provides independent support for this unification: entangled particles are connected by Planck-scale Einstein-Rosen bridges, identifying quantum entanglement with singularity topology. If entanglement is literally a wormhole, then information boundaries and topological singularities are not merely analogous but physically identical, exactly as the present model claims. The Complexity=Action conjecture (Brown et al., 2016) further strengthens the computational interpretation: the computational complexity of a boundary quantum state equals the gravitational action in the enclosed bulk region, implying that the growth of a black hole's interior is literally a computation. This is precisely the relationship the SB-HC4A proposes between singularity boundaries (substrate) and their interiors (the decompressed form).

**Step 4: The single-surface ontology.** The move from shared properties to structural identity rests on an ontological postulate, stated here explicitly. There is **one encoding surface**: the holographically saturated boundary of the computational domain. Every singularity in the inventory — the event horizon of a particular black hole, the Planck-scale boundary of a particular particle, the cosmological horizon of a particular observer, the temporal termini — is a **local reflection of that one surface, seen from a particular vantage point inside the domain**. The unification is therefore not the claim that many distinct interiors are secretly alike. It is the claim that there are no interiors-with-contents at all: the "interior" of a singularity is the same encoding surface viewed from the far side, decompressed into the observer's emergent description. Identity, in this claim, is *numerical* identity of the surface and of the computational process it carries — one surface, many reflections — not a similarity inferred from the indiscernibility of hidden contents.

Note what this postulate does *not* rely on. It makes no appeal to the Identity of Indiscernibles. An indiscernibility argument would first grant that there are distinct interiors and then argue that, since nothing can distinguish them, they must be counted as identical — inviting the immediate reply that unobservable differences might exist all the same. The single-surface ontology makes a stronger and simpler claim: the question "how do the interiors differ?" has no referent, because there is nothing on the far side of any boundary except the boundary itself, seen from elsewhere. The postulate is defended not by a principle of identity but by what it explains, and by parsimony. It explains why IB1–IB3 recur, exactly, at every scale: there is only one boundary to instantiate them. It collapses six kinds of inaccessible region into one surface rather than positing six unobservable interiors. And it is the conclusion Section 5.7 reaches independently from the black-hole side: what lies behind any horizon "is the universe — the same computational process." One postulate, one surface; the inventory of Section 5.1 is its catalogue of reflections.

A weaker, operational relative of that retired argument does, however, survive as a secondary line of support. Even a reader who declines the postulate — who insists on distinct interiors-with-contents — must grant that those interiors are indiscernible *in principle* from within the computational domain: impermeability is nomological, not practical, so no observation available to any observer in causal contact with the domain could ever distinguish them — while their *surfaces* are richly discernible, in mass, charge, and angular momentum, and can even be made to collide (black-hole mergers are observed events). An operational razor — do not multiply entities that differ in no domain-accessible respect — then counsels the same conclusion the postulate asserts. This is offered strictly as corroboration, not foundation: as a metaphysical law the Identity of Indiscernibles is contested (Black, 1952), and indiscernibility-to-the-domain licenses identity only given the reading of horizons Section 4.1 already adopts — which is why the unification rests on the single-surface postulate, with the razor as its operational shadow.

A natural objection is that singularities plainly differ: black holes have mass, charge, and angular momentum; the Big Bang has cosmological parameters; elementary particles have quantum numbers. But these are properties of the *reflection*, not of a hidden interior — they characterize how the one surface presents itself at a particular locus, to observers at a particular vantage point within the computational domain. General relativity makes this point with particular clarity at the event horizon. An observer falling through a black hole's event horizon encounters no local physical discontinuity; there is no membrane, no wall, no detectable marker at the boundary. The "surface" as a located object is a coordinate artifact, a construct of the exterior observer's description. What we measure as distinct about different singularities — their mass, their cosmological parameters, their quantum numbers — pertains entirely to the domain's interface with the boundary as seen from our side. Different singularities differ as reflections differ: in presentation, indexed to the observer's position in space, time, and scale — not as objects differ.

**Observer-relativity, contained.** If every singularity boundary is a reflection indexed to a vantage point, does physics itself become observer-relative? No — and the distinction matters. The *laws* are properties of the one surface: universal, shared, vantage-independent. Only the *reflections* — the descriptions, the apparent inventory of boundaries, which regions present as accessible and which as sealed — are indexical, in precisely the way coordinate choices are indexical in general relativity. Two observers at different loci describe different singularity inventories for the same reason two coordinate systems assign different components to the same metric: they describe one invariant object from different positions. Inter-observer consistency is guaranteed by the numerical identity of the surface, exactly as the consistency of coordinate transformations is guaranteed by the invariance of the underlying geometry.

**A consistency observation, not evidence.** The single-surface ontology has a corollary worth stating, with an explicit caution about its evidential weight. An embedded observer is itself a pattern in the decompressed description — a projection of the surface, not an additional ingredient — so "the observer's relation to a region" is, at bottom, a correlation between loci *on the surface*. That correlation is densest for regions near the observer in space, in time, and in scale, and sparsest for regions remote in any of the three. The corollary: the reflection should be most intricate, volatile, and idiosyncratic where the observer's surface-correlation is densest (the local, the recent, the mesoscale), and smoothest, most stable, and most universal where it is sparsest (the distant, the ancient, the extremes of scale). This is *not* because nearby things possess "more internal physics" — on this ontology there is no interior physics for anything to possess more of — but because the intricacy of a reflection tracks the density of correlation between surface loci. The observed pattern matches: local physics is rich and contingent; the cosmic microwave background is smooth to one part in 10⁵; the largest scales are homogeneous and isotropic; at the far end of the scale axis, the laws are perfectly shared (every electron is exactly identical). But this match must be weighed honestly: finite resolution, lookback time, and statistical averaging *guarantee* that the distant and the ancient appear smooth on entirely conventional grounds. The gradient is therefore presented as *consistent with* the single-surface ontology — a consistency check it passes, not evidence for it.

### 5.3 Unreachability Along Three Axes

Beyond information impermeability — the property on which the unification claim of Section 5.2 rests, and which every member of the inventory shares rigorously in the domain-internal sense fixed there — the singularity inventory exhibits a second shared property: no member of it is ever reached from within the computational domain. But this unreachability is not of one kind. It comes in three distinct modes, one along each of the domain's three bounded axes (Sections 4.2–4.3): *recession* along the spatial axis, *shielding* along the scale axis, and *termination without arrival* along the temporal axis. The differences must be drawn precisely, because the geometry differs in each case and the evidential weight each mode can bear differs accordingly. (A terminological caution: in the technical classification of general relativity, the temporal termini are *spacelike* singular hypersurfaces and event horizons are *null* hypersurfaces. The axis language used here refers to the direction of approach within the computational domain — space, time, or scale — not to the causal character of the boundary.)

**Spatial axis: recession.** The first mode is the familiar one — boundaries that recede as they are approached.

*Event horizons.* For an external observer, an object falling toward a black hole's event horizon never arrives — it asymptotically approaches the horizon in coordinate time, redshifting toward invisibility but never crossing. The infalling observer experiences finite proper time to the horizon (this is the standard textbook account), but from the perspective of the exterior computational domain — the domain in which physics operates and information is exchanged — the horizon is a boundary that recedes as it is approached.

*The cosmological horizon.* The observer-dependent cosmological horizon of an accelerating universe shares this property (Gibbons & Hawking, 1977; Bousso, 2002). Each observer is enclosed by a horizon at finite proper distance, defined relative to that observer's own world-line; no journey, however long, reaches it. Objects carried across it by the expansion appear, from inside, exactly as objects falling onto a black-hole horizon do: frozen at the boundary, redshifting toward invisibility, never quite gone.

**Scale axis: shielding.** The scale axis exhibits the same recede-as-approached geometry, realized in resolution rather than in distance. Spatial resolution improves with collision energy — Δx ~ ħ/p — but only up to the Planck regime. Beyond it, on the standard arguments of the minimal-length literature already invoked in Section 5.5 (Garay, 1995; Hossenfelder, 2013), concentrating trans-Planckian energy into an ever-smaller region triggers horizon formation: the collision region collapses into a black hole whose radius *grows* with further energy. Pushing harder toward the Planck floor therefore makes the boundary recede in resolution exactly as a horizon recedes in distance — every increase in the energy of the probe enlarges the shielded region it was meant to penetrate. The same floor governs interactions generally: no experiment localizes two particles at zero separation, and no interaction resolves the zero-separation limit; interactions exchange information at finite resolution, always. The Planck-scale members of the inventory (Section 5.1) are in this sense *shielded*: the boundary does not move away in space, but every attempt to approach it in energy regenerates it at a larger scale. These arguments are standard but heuristic at the edges — they extrapolate semiclassical gravity into the regime where it is expected to fail — and the shielding mode is offered with that caveat attached.

**Temporal axis: termination without arrival.** The third mode is the one whose scope must be drawn most carefully, because here a concession is required: the termini genuinely lack the asymptotic-approach geometry of the horizons.

*The Big Bang: finite depth.* In standard FRW cosmology with radiation or matter content, conformal time η = ∫dt/a(t) is *finite* as t → 0: the integral converges. The Big Bang therefore sits at a finite conformal — and finite proper — distance in the past. Far from being a technicality, this finiteness is the *horizon problem* of standard cosmology: precisely because the conformal-time depth of the past is finite, widely separated regions of the CMB sky have had no opportunity to causally equilibrate. Causal world-lines traced backward reach the t = 0 boundary at finite proper time and are geodesically incomplete there (Hawking & Penrose, 1970): they terminate. In standard cosmology, the Big Bang is *not* asymptotically unreachable in the way an event horizon is — its depth is finite in every geometric measure.

The picture changes only under past-eternal continuations of the spacetime: eternal inflation (Guth, 2007), Penrose's Conformal Cyclic Cosmology, in which our Big Bang is the conformally rescaled remote future of a preceding aeon (Penrose, 2010), or the Boyle–Turok CPT-symmetric universe, in which the Bang is a mirror point rather than an edge (Boyle, Finn, & Turok, 2018). Under such continuations the conformal coordinate extends to η → −∞, and the Big Bang recedes into an asymptotic boundary. The SB-HC4A's own cyclic cosmology (Section 5.4) is a continuation of exactly this kind — within the model, the Big Bang is the saturated boundary of a predecessor cycle, not an absolute beginning. But this cannot be offered as independent support for the unification claim: it is a consequence of the model's cyclic mechanism, conditional on that mechanism, and the argument must not lean on it.

*The Big Crunch.* The same finiteness applies, more sharply. If the universe recollapses, geodesic incompleteness means world-lines end at the final singularity in *finite proper time*; the boundary does not recede as it is approached.

*Termination is not arrival.* The finite proper time of the termini must, however, be stated with the precision general relativity itself supplies, because "reached" is here a façon de parler. A singularity is not a place. Geodesic incompleteness (Hawking & Penrose, 1970) says that a causal world-line has finite length and admits no extension — it does not say the world-line arrives anywhere. The singular boundary is not a point-set in the spacetime manifold: for every proper time before the end, the observer is at finite curvature, inside perfectly ordinary spacetime; the "endpoint" itself is never an event on the world-line, never an experience, never an element of the domain. It can be attached to the spacetime only as an *ideal* boundary point — an abstract completion of the manifold, not a location within it (Geroch, Kronheimer, & Penrose, 1972). The contrast with the spatial axis is then exact. A horizon is a genuine null hypersurface *in* the spacetime: the boundary exists as a locus, and arrival at it is forbidden. A terminus is a boundary that is not in the spacetime at all: world-lines end at finite proper time, but nothing ever arrives *at* the singularity, because there is no "at." Arrival is not forbidden; it is undefined. "Reached in finite proper time" means only "of finite length." Both are failures of arrival — different modes of the single fact that no observer, ever, is at any member of the inventory.

One sharpening is worth recording, because it shows the taxonomy is geometry rather than rhetoric. Finite conformal time does not by itself separate the termini from the horizons: in ΛCDM the *future* conformal time is also finite (η → η_max as t → ∞), and that finiteness is precisely why a future event horizon exists at all. The discriminator between the modes is proper time — infinite to the de Sitter future, finite to the Bang and the Crunch. The heat-death future accordingly belongs with the horizons, not the termini: the de Sitter-like future is asymptotic in proper time, approached and never attained (as Section 4.2 already states); only the Bang and the Crunch terminate world-lines.

*Informational depth of the past.* The finite geometric depth of the past should also be distinguished from its informational depth. Every observational channel terminates strictly before the boundary: photons at last scattering (~380,000 years), neutrinos at weak decoupling (~1 second), gravitational waves — the deepest channel — at the Planck epoch; and reheating destroys any structured record that could constitute a traversal. The terminus is therefore geometrically finite but informationally shrouded: finite proper time to a boundary no channel reaches. Nor does inflation reopen the question of finite depth: any spacetime with average expansion rate greater than zero along a congruence is past-geodesically incomplete, inflation included (Borde, Guth, & Vilenkin, 2003) — inserting an inflationary epoch does not extend the classical past to infinity. What past-incompleteness leaves open is only the *nature* of the finite-depth boundary: curvature singularity, quantum-gravity region, bounce, or junction.

*The realistic Crunch: fragmentation before termination.* For the Crunch, an idealized and a realistic picture must be distinguished. In the idealized homogeneous recollapse, the final singularity is a global spacelike boundary approached by every comoving observer together: there is no horizon to cross first and no shroud, because there is no "outside." But a realistic recollapse is not homogeneous. During contraction, inhomogeneities grow violently, structure collapses into black holes, and trapped surfaces form and merge until every observer is inside a trapped region — the distinction between "falling into a black hole" and "hitting the Crunch" dissolves into one spacelike singular boundary, generically approached in the chaotic oscillatory manner of the Mixmaster/BKL analysis (Misner, 1969; Belinskii, Khalatnikov, & Lifshitz, 1970). And near a generic spacelike singularity the dynamics exhibit *asymptotic silence*: light cones collapse onto world-lines, causal contact between neighboring world-lines shuts off, and the dynamics become ultralocal (Uggla, van Elst, Wainwright, & Ellis, 2003). In the model's own currency the consequence is striking. The computational domain does not march collectively into a wall; it fragments into causally silent, holographically bounded shards before terminating — the structural time-reverse of the Big Rip fragmentation of Sections 5.4 and 5.7, which shatters the domain outward where the Crunch shatters it inward. And the endpoint at which everything has merged lies in no observer's past light cone: each world-line ends privately, in causal isolation, at finite proper time, without arrival. No observer ever possesses the information that the merging happened. Black-hole complementarity (Section 8.2) sharpens this: its exterior, frozen-infaller description requires a persisting exterior, which a global Crunch denies — with no future null infinity there are no event horizons properly so called, and the would-be distant observers are themselves terminating, so the exterior account loses every holder, and only the infalling description, ending privately and without arrival, remains instantiated.

*Computational depth.* One further remark, flagged explicitly as the model's interpretive layer rather than as established physics. In the vacuum-dominated generic approach to a spacelike singularity, the BKL behavior consists of an infinite sequence of Kasner epochs within finite proper time — unboundedly many dynamical transitions packed into a finite interval. For an ontology in which the substrate evolves by discrete update steps and proper time is emergent (Section 8.4), this matters: finite proper time does not bound computational depth. Measured in dynamical epochs rather than by the emergent geometric clock, the terminus can be asymptotic even where the proper-time reading is finite. Two cautions accompany this. First, the divergent oscillation count is matter-dependent: a stiff fluid or a massless scalar field suppresses the oscillations, so the infinite-epoch behavior is generic for vacuum-dominated approaches, not a theorem for all matter contents. Second, "update steps of the substrate" is not an operationally defined quantity in known physics; the identification of BKL epochs with computational steps is an interpretation the model supplies, not something the singularity theorems deliver. The remark is offered as a suggestive consonance, not as support.

**What survives.** The taxonomy yields a three-tier ladder of decreasing strength, and the unification claim should be located on it explicitly. First, *information impermeability* (IB1–IB3): rigorous in the domain-internal sense fixed in Section 5.2, and shared by every member of the inventory. Nothing returns from beyond a Crunch; no signal emerges from before the Bang; the temporal termini are as information-impermeable as any horizon. This is the property on which the unification of Section 5.2 rests, and nothing in this section touches it. Second, *no-arrival*: also shared by every member, but weaker. No observer is ever at any of these boundaries as an event in the domain — rigorously for the horizons (arrival forbidden) and the termini (arrival undefined), heuristically for the scale floor (arrival shielded). For the termini this is partly a fact about definitions — about what "arrival at a non-place" could even mean — and it is therefore presented as a unifying observation, not a premise the argument leans on. Third, *asymptotic-approach geometry*: not universal. It is rigorous for the horizons, standard but heuristic for the scale floor, and available for the termini only conditionally (under the past-eternal continuations above) or in computational-step count (the flagged remark above) — it is not claimed here as a shared property. The unification rests, as before, on the first tier. What the taxonomy shows is that the termini do not break the pattern of unreachability — they change its mode.

### 5.4 Singularities as Information Transformers and Cyclic Cosmology

The conservation argument of Section 8 holds that singularities do not destroy information but *transform* it between compressed (boundary) and decompressed (interior) forms — conditional, as Section 8.1 states, on the energy–information identity that Section 9.1 lists among the model's weak points. Combined with the impermeability of singularity boundaries, this yields a striking consequence for the fate of the universe.

**Heat death as singularity.** Consider the heat death scenario: entropy increases until the universe reaches thermodynamic equilibrium — maximum entropy, maximum disorder, all gradients erased. In the standard thermodynamic picture the entropy of a dilute gas at heat death remains far below the holographic limit; a single black hole of equivalent energy would carry vastly more. Heat death, as usually conceived, is not holographic saturation.

The gap does not close from below. Gravitational collapse and black-hole mergers raise the interior entropy, but nowhere near far enough. In the observable universe's present budget, supermassive black holes dominate the interior at S_obs ≈ 3 × 10¹⁰⁴ k while the cosmic event horizon carries S_CEH ≈ 2.6 × 10¹²² k (Egan & Lineweaver, 2010) — the boundary exceeds everything inside it by some eighteen orders of magnitude, and collapsing every remaining baryon into black holes does not recover the shortfall.

It closes from the other direction. In the very late universe, after all matter has either evaporated (proton decay) or collapsed into black holes that subsequently evaporate via Hawking radiation, the interior contribution falls to zero and the cosmological horizon is the only entropy carrier left (Gibbons & Hawking, 1977). The de Sitter horizon saturates the holographic bound by construction — its entropy is exactly A/4ℓ_P² for its area — so the terminal configuration is a holographically saturated boundary enclosing an emptied interior. The distinction between interior structure and boundary encoding collapses because the interior vanishes, not because its contents climb to the boundary's value.

**The saturation trigger: a motivated conjecture.** It must be stated plainly what this convergence does and does not establish. The de Sitter horizon entropy (~10¹²² k_B) is not a quantity that appears at late times — it dominates the entropy budget from early epochs, and nothing dynamical happens at the moment the interior finishes emptying. Pointing at the saturated state and declaring a transition would be a definition followed by an assertion, not a mechanism. What the model requires — and what is proposed here as a motivated conjecture, not a result — is a reason why the saturated state cannot persist.

The conjecture is this: the saturated state is an extremum of the computation, but a *maximally disordered* extremum — and that combination is unstable. Distinguish two kinds of extremal state a bounded automaton can occupy. Class 1 dead states (the all-off or all-on lattice) are extremal *and ordered*: trivially stable fixed points at which computation halts and stays halted. The holographically saturated boundary is the opposite extreme: every distinguishable degree of freedom on the surface is in use, and no further distinction can be encoded. For a system whose defining condition is self-referential closure — Φ(U) = U, the requirement that the system continuously recompute its own structure (Section 6.3) — a maximally loaded boundary is a saddle, not a resting place. The closure condition cannot be *statically* maintained at maximum boundary information density, because self-reference is an ongoing encoding operation, not a stored configuration, and a surface on which nothing further can be written cannot sustain it. The dynamics are forced off the extremum. And the only direction "off" a maximally compressed state is decompression: the fully loaded boundary unfolds holographically into a new, ordered, low-entropy interior — a new Big Bang. Irreversibility and computational irreducibility (Section 2.4) entail that the decompression cannot retrace the previous cycle: there is no exact replay and no return to a prior state, though similarly disordered saturated states remain reachable — the cycle is recurrent without being periodic.

If this conjecture holds, heat death does not end the universe — it triggers a phase transition. The information encoded at maximum density on the boundary decompresses into a new interior, and the self-referential closure Φ(U) = U is not merely spatial but *temporal*: the universe computes its own restart. The mechanism has a close cousin in the literature: Penrose's Conformal Cyclic Cosmology (Penrose, 2010) likewise identifies the maximally dilute remote future of one aeon with the Big Bang of the next. The conjecture above is the automaton-theoretic form of that identification, with information saturation playing the role Penrose assigns to conformal rescaling.

The honest status of this mechanism deserves to be stated in full, because the ingredients it requires are individually available in known automata even though no single rule yet combines them. The Game of Life cannot exhibit the transition — driven to a high-entropy soup it does not reorganize but decays into sparse, static "ash" — and the structural reason is that it has a single vacuum and a preferred sparse phase. But the three properties the mechanism needs are each realized elsewhere. First, *complexity sustained at maximal disorder*: the Day & Night rule (B3678/S34678) is exactly self-complementary — its dynamics are unchanged when live and dead are swapped — so it supports complex structures at high density as richly as at low density, and its maximum-entropy state, the half-filled configuration, is not a dead extremum but the self-dual locus of that symmetry, an unstable saddle poised between two equivalent ordered vacua. That is precisely the configuration this section conjectures the saturated boundary to be: maximal disorder as a saddle the dynamics are forced off, into ordered structure rather than into ash. Second, *cycle alternation*: Day & Night's on↔off symmetry is an exact internal analogue of charge conjugation (a C-type symmetry, not yet a full CPT), under which the post-saturation state spontaneously selects one of the two phases with the conjugate realized elsewhere — the automaton form of the matter/antimatter alternation discussed above. Third, *reversibility*: exactly reversible Class 4 block automata exist — Critters (Toffoli & Margolus, 1987), whose law even complements the entire lattice each step — supplying the unitary substrate the architecture requires.

Two limits keep this honest. No Life-family rule satisfies a holographic information bound — cellular-automaton information is extensive, not bounded by a perimeter — so any such demonstration would establish only the *saddle-instability* half of the conjecture, not the *holographic-decompression* half. And, more instructively, a *closed* reversible automaton started from a typical maximally disordered state cannot exhibit the transition at all: with information conserved, coarse-grained disorder stays maximal and Poincaré recurrence replaces renewal. That obstruction is itself a signpost — it shows renewal *requires* a channel into which the interior's entropy can be exported, which is exactly the holographic boundary the architecture posits (Sections 8.2, 8.4). The open task is therefore not to find a rule that happens to have the property but to assemble symmetry, reversibility, and a boundary information channel in one construction; and because a Class 4 rule supporting universal computation can simulate any other, a behavior demonstrated in one such rule is available, by simulation, to any universal substrate — so the substrate need not exhibit the mechanism natively, only host it. The saturation trigger accordingly remains among the model's weak points (Section 9).

**Cyclic dynamics.** The resulting picture is cyclic: expansion → heat death (holographic saturation) → information transformation → new Big Bang → expansion. The cycles may also include Big Crunch phases — contraction to a singularity followed by re-expansion — and the alternation between expansion-dominated and contraction-dominated cycles may itself be unpredictable. This is consistent with Class 4 dynamics, which are computationally irreducible (Section 2.4): you cannot predict which type of cycle comes next without running the computation.

**The Tolman objection.** Any cyclic cosmology must answer Tolman's (1934) argument, which sank the first generation of them. Entropy increases within each cycle, so on a naive accounting each cycle inherits its predecessor's entropy and is larger and longer than it was; running the sequence backwards, the cycles shrink without bound and the cyclic universe turns out to have a beginning after all — reinstating what it was built to avoid.

The saturation mechanism answers this by putting a ceiling where Tolman assumed a ratchet. The transition does not hand the next cycle an entropy budget to be added to; it hands it a holographically saturated boundary, whose information content is fixed by its area and cannot be exceeded. Every cycle begins from a surface in the same maximal condition, so no monotonically accumulating quantity drives the cycles apart. Tolman's argument requires an unbounded entropy variable, and a holographic bound is the denial that one exists.

Two limits on that answer should be recorded. It relocates the question rather than removing it: the ceiling is set by the boundary's area, so cycles are equivalent only if that area is, and nothing in the framework fixes the cosmological constant — hence the de Sitter horizon area — across cycles. And it is an answer available only to a bounded cosmology. Steinhardt and Turok's (2002) cyclic model answers Tolman differently, by having the expansion dilute entropy density while total entropy accumulates in an ever-growing volume. The two answers are compatible; neither is established here.

**The Big Rip as a third endgame.** The heat death and Big Crunch scenarios both produce a single global singularity — one holographically saturated boundary that triggers one restart. But a third cosmological endgame exists. If dark energy is "phantom energy" with equation-of-state parameter w < −1, its density increases without bound as the universe expands (Caldwell, 2002). The expansion rate diverges at a finite future time — the Big Rip. The expansion tears apart galaxy clusters, then galaxies, then stellar systems, then stars, then atoms, then spacetime itself. Every point in space becomes a singularity.

The observational standing of this branch has moved against it, and the paper should not present the three endgames as equally supported. DESI's DR2 baryon-acoustic-oscillation measurements, combined with CMB and supernova data, favour a time-evolving equation of state in the quadrant w₀ > −1, wₐ < 0 — dark energy that is not phantom today and whose equation of state is becoming less negative — at 3.1σ over ΛCDM for BAO with CMB, and at 2.8–4.2σ once supernovae are included, depending on which sample is used (DESI Collaboration, 2025). Future phantom behaviour is disfavoured on that fit. It is not excluded: w₀wₐCDM is a two-parameter fit to a function nobody has derived, the preference is not at discovery significance, and the same data sit in mild tension with ΛCDM itself. The Big Rip accordingly remains a live but currently disfavoured endgame. Nothing in the architecture below depends on which of the three obtains.

Independent support for the Big Rip as a cyclic transition comes from Ruggiero (2020), who showed that Hawking radiation heating at the Big Rip horizon can produce conditions matching the conformal boundary required by Penrose's CCC, arriving at the same structural conclusion (Big Rip as renewal trigger rather than terminus) from entirely different premises.

In SB-HC4A terms, the Big Rip represents a qualitatively different singularity transition. The singularity boundary does not remain at the edges of the computational domain — it propagates *inward*, fragmenting the domain into infinitely many holographically saturated regions. Instead of one global singularity (as in heat death or Big Crunch), the computational domain shatters into a fractal explosion of singularity boundaries. Each fragment is a holographically saturated surface satisfying conditions IB1–IB3 (Section 5.2). A realistic Big Crunch, as Section 5.3 details, is this process run with the arrow reversed: contraction fragments the domain *inward* into causally silent, holographically bounded shards where the Rip fragments it *outward* — two arrows, one endpoint, a computational domain reduced to mutually silent saturated fragments.

If singularities transform information rather than destroying it, each fragment triggers its own information transformation — its own restart. The Big Rip therefore functions as a *multiverse generator*: a single computational domain fragments into many holographically saturated boundaries, each of which decompresses into a new sub-universe. The self-referential closure Φ(U) = U generalizes from a single-valued map (one universe → one universe) to a multi-valued map (one universe → many sub-universes), producing a branching tree rather than a linear sequence of cycles.

This gives three endgame scenarios, all consistent with the SB-HC4A framework:

1. **Heat death** → one global singularity → one restart (the universe computes its successor).
2. **Big Crunch** → one global singularity → one restart (with possible CPT flip; the universe computes its successor with reversed signature).
3. **Big Rip** → many singularities → many restarts (the universe fragments into many daughter universes — a branching rather than linear cycle).

The framework is robust across all three cosmological outcomes. Conditional on the saturation-trigger conjecture above, it does not depend on a specific end-state but predicts cyclic renewal under *any* scenario that drives the computational domain to holographic saturation — whether that saturation is global (heat death, Big Crunch) or distributed (Big Rip). The cyclic cosmology of the SB-HC4A is therefore not contingent on the cosmological constant taking a particular value or dark energy having a particular equation of state — though it is contingent, as stated, on the conjectured instability of the saturated state.

**CPT signature alternation.** A further possibility: each cycle could flip the CPT (charge-parity-time) signature, producing a matter-dominated universe in one cycle and an antimatter-dominated universe in the next. This connects to Boyle, Finn, and Turok's (2018) proposal of a CPT-symmetric universe, extended with a specific prediction that a right-handed neutrino constitutes dark matter (Boyle, Finn, & Turok, 2022), where the Big Bang is a mirror point between a universe and its CPT-conjugate anti-universe. In the SB-HC4A framework, this falls out naturally from the information-transformation property of singularity boundaries: decompression from a singularity boundary need not preserve the matter-antimatter signature of the previous cycle. The boundary encodes information at maximum density; the specific form of the decompression — which particle species dominate — is a property of the new interior, not a constraint inherited from the old one. In the Big Rip scenario, each daughter universe could independently realize either CPT orientation, producing a multiverse with mixed matter-antimatter signatures.

If correct, this resolves the baryon asymmetry problem — the observed absence of antimatter in our universe. We do not see antimatter because our universe is one half of a CPT-alternating cycle (or, in the Big Rip branching case, one branch among many with a particular CPT orientation). The "missing" antimatter is not missing; it constitutes the previous (or next) cycle's universe, or a sibling branch in the Big Rip tree.

### 5.5 Particles as Planck-Scale Singularities

A specific prediction follows: "point-like" elementary particles are not truly zero-dimensional. They are Planck-scale singularities — miniature information boundaries whose interiors are as inaccessible as a black hole's. The standard model treats particles as mathematical points for calculational convenience, but the SB-HC4A model predicts they have Planck-scale structure that saturates the holographic bound at that scale.

This is consistent with approaches in quantum gravity where the Planck scale provides a natural minimum length (Garay, 1995; Hossenfelder, 2013), though the specific claim that particles *are* singularities of the same type as event horizons is novel. Section 5.7 examines the sharpest available instance of this claim — the Kerr-Newman electron correspondence — including a scale and horizon tension that any identification of particles with singularity boundaries must confront.

### 5.6 Particles as Computational Atoms

If particles are Planck-scale singularity boundaries (Section 5.5), they are not merely structural elements of the SB-HC4A — they are its irreducible computational units. The term *computational atoms* (in the original Greek sense of *atomos*: indivisible) captures this role: particles are the basic operations of the universal automaton. Several consequences follow that address otherwise unexplained features of the Standard Model.

**Finite particle spectrum from finite boundary capacity.** A boundary of area A carries at most I = A/(4 ℓ_P² ln 2) bits (Section 5.2), and a finite capacity admits only finitely many distinguishable states. Only a subset of those states will be dynamically stable — stable in the sense that the boundary configuration persists under the Class 4 dynamics of the automaton — and the stable configurations constitute the particle spectrum. That the elementary spectrum is finite and small follows, on this reading, from a capacity bound rather than being an arbitrary catalog.

The same arithmetic constrains the model rather than being predicted by it, and the constraint is sharp enough to be worth stating. A boundary of area exactly ℓ_P² carries I = 1/(4 ln 2) ≈ 0.36 bits — less than one bit, hence fewer than two distinguishable states. Taken literally, a one-Planck-area boundary yields a universe with one kind of particle in it. The observed spectrum runs the argument in reverse: encoding N distinguishable stable configurations requires A ≥ 4 ℓ_P² ln N, so the sixty-odd elementary field degrees of freedom of the Standard Model require a boundary of order ten to twenty Planck areas, and a state count that resolves colour, spin and antiparticle labels requires several times that. Section 5.5's "Planck-scale" must accordingly be read as *of order* the Planck scale — within an order of magnitude in area — rather than as exactly one Planck area. The capacity argument gives an upper bound on the number of stable configurations and a lower bound on the boundary area; it does not give the multiplicity itself. Deriving the observed multiplicity from a boundary of definite size is open, and would be a considerably stronger result than anything claimed here.

This is structurally analogous to the way a cellular automaton's finite rule table admits only finitely many persistent structures (gliders, oscillators, still lifes in the Game of Life). The particle types are the "gliders" of the Planck-scale automaton — the stable, propagating configurations permitted by the underlying computational rules.

**Discreteness of quantum numbers.** Quantum numbers — charge, spin, isospin, color charge, baryon number, lepton number — take discrete values (integer or half-integer multiples of fundamental units). In the computational-atom framework, this discreteness is not imposed but follows from the nature of information encoding on a finite boundary. Boundary configurations are discrete states; the quantum numbers are labels on these states. The quantization of physical properties is a consequence of the finite, discrete nature of information storage at the Planck scale, consistent with the area quantization results of loop quantum gravity (Rovelli, 2004).

**Particle interactions as boundary information exchange.** When two particles interact — when two Planck-scale singularity boundaries come into causal contact — they exchange information across their boundary surfaces. This information exchange *is* the interaction. The Standard Model's force-carrying bosons (photons, gluons, W and Z bosons) are not a separate ontological layer; they are the permitted modes of information transfer between singularity boundaries. The interaction vertices of quantum field theory — the points where Feynman diagrams branch — are information exchange events between computational atoms. Feynman diagrams, in this interpretation, are diagrams of computation: each line is a propagating boundary configuration, each vertex is an information exchange operation.

The selection rules governing which interactions are permitted (e.g., conservation of charge, color neutrality of hadrons) follow from the constraints on information exchange between holographically saturated boundaries. Not every information transfer is consistent with the boundary configurations involved; the permitted transfers define the interaction rules.

**Conservation laws as information conservation — and which conservation laws.** Conservation laws are constraints on how information may be redistributed across boundary interactions: information conservation at singularity surfaces (Section 5.4) requires that the total boundary-encoded information be preserved in any interaction. But identifying particles with no-hair boundaries (Section 5.7) restricts *which* conservation laws can be grounded this way, and the restriction is severe. Discreteness and conservation are separate claims — a quantum number can take integer values and still fail to be exactly conserved — and only the second is at stake here.

A stationary black hole is characterized by mass, charge and angular momentum alone. If a particle is a boundary of that kind, only quantities of that kind have anywhere to live on it. Electric charge does: it is a gauge charge, measurable at infinity by Gauss's law, and one of the three no-hair quantities. Spin does, and Section 5.7 gives it a topological reading. Colour and weak isospin do not appear as boundary labels, for reasons the Standard Model already supplies — colour is confined, so no free colour charge is ever presented to a boundary, and weak isospin is spontaneously broken. Baryon and lepton number have no boundary home at all.

That last consequence is the model agreeing with known physics rather than failing. Baryon and lepton number are not fundamental symmetries of the Standard Model either: they are accidental global symmetries of the renormalizable Lagrangian, violated non-perturbatively by electroweak sphalerons (Klinkhamer & Manton, 1984), which preserve B − L while destroying B + L. Quantum gravity is expected to be harsher — exact global symmetries are believed to be unrealizable in any theory of gravity, a statement proven within AdS/CFT by Harlow and Ooguri (2021) — and black holes are the standard illustration: matter of any baryon number falls in, and thermal radiation carrying none comes back out. This architecture therefore does not derive baryon and lepton number conservation from boundary information. It predicts that they are approximate, that they fail at the boundary, and that the exactly conserved quantities are those with a no-hair handle. The prediction is shared with the rest of quantum gravity rather than distinctive of this model; what would be distinctive, and wrong, is a horizon that conserved baryon number exactly.

**Three generations: a conjecture from Class 4 self-similarity.** The Standard Model's three generations of fermions — (e, μ, τ), (u, c, t), (d, s, b), and their neutrino counterparts — remain one of the deepest unexplained patterns in particle physics. Each generation replicates the quantum numbers of the previous one at a higher mass scale.

A speculative but structurally motivated hypothesis: Class 4 systems inherently contain Class 3 (self-similar, fractal) behavior as a subprocess (Section 2.5). If the space of stable singularity boundary configurations inherits this self-similar structure, the same boundary type could be stable at multiple energy scales — producing copies of the same particle at different masses. Three generations would then reflect a hierarchical, self-similar structure in the configuration space of Planck-scale singularities.

This is a conjecture, not a derivation. The number three is not predicted by this argument alone. However, the generation structure is otherwise entirely unexplained by the Standard Model itself (which treats the three generations as a brute empirical fact), and the self-similarity of Class 4 dynamics provides a natural — if not yet quantitative — structural motivation for generation replication. If a future formalization of the Planck-scale singularity configurations shows that exactly three hierarchical levels are stable under Class 4 dynamics, this would constitute strong evidence for the computational-atom interpretation.

**Existence proof: automata as fermionic quantum field theories.** The computational-atom picture is not merely a conceptual proposal — it has mathematical backing. Wetterich (2022a, 2022b, 2022c) has demonstrated that large classes of reversible cellular automata on space-lattices are *exactly equivalent* to discretized fermionic quantum field theories, via a proven mapping through Grassmann functional integrals. This is not an approximation but a mathematical identity: the probabilistic description of the automaton (probability distribution over initial bit configurations) is equivalent to quantum mechanics — wave functions, density matrices, and non-commuting operators all arise from the classical automaton structure. Some automata in this class realize *local* gauge symmetries (the structure the Standard Model requires), and Wetterich (2022c) explicitly constructed a cellular automaton representing spinor gravity in four dimensions, with exact local Lorentz symmetry on the discrete level and emergent diffeomorphism symmetry in the continuum limit. By the universality of Class 4 computation, any Class 4 automaton can in principle *simulate* a system that produces SU(3)×SU(2)×U(1) with three generations — Langton's ant could run such a simulation, as could an arbitrarily high-dimensional automaton. But simulation is not physical equivalence: a cellular automaton simulating QCD is no more "producing quarks" than a weather simulation is producing rain. The open problem is not whether a Class 4 automaton can simulate the Standard Model, but which automaton produces the observed gauge group and generation structure as its *natural dynamics* — as the direct consequence of its rule structure rather than as an encoded program running on top of it. This is the question Wetterich's framework now makes precise: his results demonstrate that specific automata are mathematically *identical* to specific fermionic QFTs, not merely simulating them. The meeting point — automata whose native dynamics produce SM-like particle content — is the frontier.

Elze (2022) provides complementary support from the measurement problem: quantum-classical hybrid systems, the dynamics at the interface between quantum and classical descriptions, are shown to be compatible with underlying ontological cellular automata. This extends the CA-QFT correspondence beyond pure quantum systems to the measurement boundary itself. More recently, Elze (2024) demonstrated that classical Ising spins on a cellular automaton lattice relate to the Weyl equation under deformation, with bits becoming qubits in the process. This provides a concrete mechanism for the computational-atom picture: the transition from deterministic CA bits to quantum mechanical qubits to relativistic fermion dynamics (Dirac equation) is a continuous mathematical deformation, not a conceptual gap. Combined with Wetterich's automata-QFT equivalences, the emergence of quantum field theory from classical automaton dynamics is increasingly well-established.

### 5.7 Black Holes, Particles, and the Topology of Spin

The singularity unification thesis connects to an observation that has been in the literature since 1968 but whose implications have not been fully absorbed: black holes and elementary particles share the same characterizing properties. The black-hole uniqueness ("no-hair") theorems establish that a stationary black hole in Einstein–Maxwell theory is fully described by three quantities: mass (M), charge (Q), and angular momentum (J). Israel (1967, 1968) proved uniqueness for the *static* (J = 0) vacuum and electrovac cases; the rotating, charged case rests on the uniqueness results of Carter (1971) and Robinson (1975) together with Hawking's (1972) rigidity theorem. These are precisely the quantum numbers that characterize elementary particles. Carter (1968) deepened this correspondence by showing that the Kerr-Newman solution — the general charged, rotating black hole — produces a gyromagnetic ratio of g = 2, identical to the Dirac electron. This is not imposed; it emerges from the same source-free field equations.

Burinskii (1998, 2008) has pursued this correspondence furthest, arguing that the electron literally *is* a Kerr-Newman geometry: when the Kerr-Newman solution is evaluated with electron parameters (mass, charge, spin), the result is a ring singularity whose ring structure can be modeled as a closed gravitational string. Arcos and Pereira (2004) confirmed that the extreme Kerr-Newman case reproduces all electron quantum numbers.

**An unresolved scale and horizon tension.** Stated this baldly, however, the correspondence collides with Section 5.5 — and the collision should be named rather than passed over. The Kerr-Newman solution with electron parameters is *super-extremal*: the electron's angular momentum exceeds, by more than forty orders of magnitude, the maximum its tiny gravitational mass could dress with a horizon. The classical solution is therefore a *naked* ring singularity — a singularity without a horizon — and its ring radius is of order the electron's Compton scale, ~10⁻¹³ m, more than twenty orders of magnitude larger than the Planck length. Taken at face value, this contradicts Section 5.5 twice over: a naked singularity has no horizon and is therefore not an information-impermeable boundary, and the Compton scale is not the Planck scale.

The framework's response invokes the torsion mechanism developed at the end of this section. In Einstein-Cartan theory, fermion spin sources torsion, and torsion at high density is repulsive: it prevents the formation of the classical point or ring singularity (Poplawski, 2010). On this reading, the naked singularity of the classical Kerr-Newman solution is an artifact of extrapolating torsion-free general relativity into a regime where it does not apply; what replaces it is a bounded, regularized core. The two scales then play different roles: the Compton-scale ring structure is *exterior dressing* — the electromagnetic and gravitational field configuration through which the particle presents its quantum numbers to the rest of the computational domain, the structure in which the g = 2 result lives — while the information-impermeable boundary that Section 5.5 posits is a Planck-scale core within it. This two-scale resolution is a conjecture, not a result: no derivation currently connects a torsion-regularized core to the Kerr-Newman exterior, and the classical solution as it stands has no horizon at all. The black-hole/particle correspondence should therefore be read as a striking correspondence carrying an unresolved scale and horizon tension — not as a structural identity at the level of the field equations. The unification claim does not rest on it; it rests on the impermeability argument of Section 5.2. The Kerr-Newman correspondence is suggestive corroboration whose proper interpretation remains open.

**Spin as topological circumnavigation.** The connection between spin and singularity topology illuminates why the quantum numbers align. For a spin-1/2 particle, a 360° rotation does not return the system to its original state; a full 720° rotation is required. This is not a geometric property but a topological one — it reflects the double-cover relationship between SU(2) and SO(3) (Penrose, 1971). For a singularity, "rotation" cannot be defined as revolutions per unit time; there is no internal reference frame against which to measure orientation. What can be measured is circumnavigation: how many times must one traverse the boundary at its innermost accessible orbit to return to one's origin? For fermions, the answer is two. The spin quantum number, in this reading, is the topological winding number of the singularity boundary — a property of the boundary's topology, not of any mechanism "inside." This interpretation receives support from loop quantum gravity, where Rovelli and Smolin (1995) derived an area spectrum in which the same half-integer spin labels j that characterize particle spin also label area quanta of horizons. Spin is a boundary property on both sides of the correspondence.

**Singularity interiors are not separate universes.** A common framing in the literature (Smolin, 1992; Poplawski, 2010; Easson & Brandenberger, 2001) describes black hole interiors as spawning "baby universes" — new, causally disconnected cosmological regions. The SB-HC4A framework suggests a more parsimonious interpretation. The observable universe's horizon is plainly an artifact of finite signal speed: what lies beyond it is more of the same universe — quarks, protons, stars, galaxies — simply inaccessible from our location. By the singularity unification thesis (Section 5.2), the same applies to every other singularity boundary. The "interior" of a black hole, of a Planck-scale particle, of the cosmological horizon, is not a separate universe. It is the universe — the same computational process — in a region that is causally unconnectable from our reference frame.

What appears from inside as a labyrinth of causally disconnected regions — singularity interiors that seem separate, horizons that seem to enclose distinct worlds — is a feature of the interior perspective, not of the underlying computation. The automaton does not contain separate universes any more than a cellular automaton contains separate "glider universes." It contains one computational process whose internal causal structure, viewed from any single location within it, presents some regions as accessible and others as permanently beyond reach. The boundaries are real in the sense that no information crosses them from within. But they are perspectival in the sense that they partition a single process into apparently separate domains. "Interior causality" — the causal structure we can observe and measure — is the interior observer's representation of a computation whose full causal structure is, by the inexpressibility theorem of Section 6.4, inaccessible from within. The real structure of the automaton is not a knot of disconnected bubbles; it is a single self-referential process that only looks like disconnected bubbles to any observer embedded in it. This is the cosmological expression of Gödel's incompleteness: the system's complete causal structure is a true statement about itself that no internal formal description can capture.

**The Big Rip as didactic bridge.** The Big Rip scenario (Section 5.4) makes this interpretation vivid. As the expansion tears spacetime apart, the causal horizon of every observer shrinks until it contains only that observer. Each resulting fragment is a holographically saturated bounded region — an information boundary enclosing a computational domain. These fragments relate to each other exactly as elementary particles do: never touching, never exchanging information across their boundaries, each carrying properties inherited from the parent universe's local physics. If the fragments are particle-like, then particles are fragment-like — and the proposed unification of all six singularity types becomes intuitive rather than abstract. The Big Rip does not create new universes; it reveals, at a scale accessible to imagination, the structure that already exists at the Planck scale in every elementary particle.

**Torsion and the nature of the boundary.** Einstein-Cartan theory — the torsion mechanism invoked above for the Kerr-Newman case — supports the information-boundary interpretation more generally. When fermion spin couples to spacetime, it generates torsion, and torsion at high density produces a repulsive interaction that prevents the formation of classical point singularities (Poplawski, 2010). The "singularity" is not an infinite-curvature point but a region where torsion-mediated dynamics replace classical collapse with a bounce or a phase transition. The boundary remains real — information cannot cross it — but what lies behind it is not an undefined mathematical pathology. It is more computation, more universe, in a region that is causally sealed from the observer by the information-opacity of the boundary itself.

---

## 6. The Holographic Class 4 Architecture

### 6.1 Three Relationships Between Holograms and Automata

In the book manuscript that preceded this paper (Gruber, 2015), I identified three possible relationships between holographic systems and Class 4 cellular automata:

1. **A holographic substrate produces Class 4 dynamics.** This is what the brain does: locally holographic neural networks (Lashley, 1950; Pribram, 1971) operating at criticality produce Class 4 cortical dynamics.

2. **A Class 4 automaton produces holographic output.** Local rules at the edge of chaos generate non-local, distributed information encoding as emergent behavior. This describes quantum entanglement from an information-theoretic perspective.

3. **A Class 4 automaton whose rule structure is itself holographic.** The rules encode higher-dimensional information in lower-dimensional structure. If such a system exists, it does what the holographic principle says the universe does — not by analogy, but by construction.

I proposed (Gruber, 2015) that if all three relationships could coexist in a single system — holographic rules, Class 4 dynamics, holographic output — the result would be a computational fixed point: a system that encodes itself.

### 6.2 The SB-HC4A Architecture

The Singularity-Bounded Holographic Class 4 Automaton (SB-HC4A) is the system in which all three relationships hold simultaneously, bounded by the singularity structure identified in Section 5.

**Definition.** An SB-HC4A is a dynamical system U = (S, R, B) where:
- S is a state space on a d-dimensional manifold
- R is a holographic rule set: R encodes (d+1)-dimensional information in d-dimensional structure
- B is a singularity boundary: a scale-invariant surface of maximum information density (holographically saturated) that bounds the computational domain at every scale
- U operates within the Class 4 band — the regime of computational irreducibility with universality (Section 2.3). The band is bounded below by order and above by chaos, and Class 4 is an interval rather than a knife-edge point: the defining criterion is irreducibility with universality, not any particular value of a control parameter. Branching ratio σ and maximum Lyapunov exponent λ_max are diagnostics of the regime, not definitions of it, and they reach their critical values at different operating points in the same system — so neither a specific σ nor a specific λ_max is required here
- The output of U is holographic: emergent large-scale structure encodes non-local information

### 6.3 Self-Referential Closure

The SB-HC4A is self-referential: it computes its own structure. This can be stated as a fixed-point condition:

Φ(U) = U

where Φ is the "compute the output" operator. This self-referential closure has a precise formal analogue in the self-referential computation framework (Gruber, 2026b, Section 6.3), where the fixed point of self-representation is: Φ(m*) = m*, where m* is the state at which the model and the modeled coincide.

The self-referential closure condition has a precise operational meaning. The holographic boundary of the universe, at maximum information density, encodes the complete rule set governing the system's evolution. These rules decompress into the observable interior: the three-dimensional physical universe with its fields, particles, and dynamics. That interior, through its ongoing evolution, continuously re-encodes information back onto the boundary. The output of the computation is identical to the system performing the computation. There is no external specification, no blueprint stored in some meta-universe, no initial condition imposed from outside. The rules generate the structure; the structure embodies the rules. To say the universe is a computational fixed point is to say that applying the holographic encoding-decompression process to the universe yields the universe. Nothing is added, nothing is lost, nothing refers beyond itself.

This self-referential closure is not a logical circle. Circularity is a static defect in reasoning, where a conclusion covertly presupposes itself. What is described here is a dynamical process that converges to a stable configuration. A standing wave is sustained not by fiat but by continuous regeneration through the medium it propagates in; similarly, the universe's structure is sustained by the computation it instantiates, moment to moment. The fixed point persists because the dynamics converge to it, not because it was stipulated. Class 4 cellular automata are precisely the systems capable of this behavior: complex enough to support persistent self-organizing structures, yet constrained enough that those structures are stable rather than chaotic. The self-reference is therefore not a philosophical embarrassment but a physical property, as concrete as the resonance condition of a vibrating string.

The holographic architecture receives strong support from Van Raamsdonk's (2010) demonstration that spatial connectivity is built from quantum entanglement: disentangling two subsystems disconnects the spacetime between them. If entanglement constructs spacetime, then the holographically saturated boundary, which encodes entanglement information at maximum density, is literally the substrate from which the observable spatial interior emerges, exactly the relationship the SB-HC4A architecture requires.

### 6.4 Inexpressibility

This stability comes at an epistemic cost, and the cost is fundamental. A self-referential system of sufficient complexity inevitably contains truths that no formal subsystem can derive. This is the content of Gödel's incompleteness theorems (Gödel, 1931), and it applies with full force here. The universe, as a self-referential Class 4 automaton operating at the boundary of computability, cannot be completely described by any formal system that is a proper part of it. The "Weltformel" (world equation) is therefore not an equation in the traditional sense. It is the process itself. The only complete description of the universe is the universe. Every sub-universe description, including every equation a physicist writes down, is necessarily incomplete. Such descriptions capture regularities, approximations, useful compressions of local behavior, but never the whole. This is not a failure of physics; it is a theorem about self-referential systems. The universe is not hiding its equation from us. It is computing it.

A parallel conclusion emerges from constructor theory (Deutsch & Marletto, 2015), which reformulates physics in terms of possible and impossible transformations rather than initial conditions and dynamical laws, a process-over-state ontology that converges with the SB-HC4A's claim that the universe's "equation" is a computation, not a formula.

### 6.5 Entanglement as Holographic Non-Separability

Section 6.1 stated that a Class 4 automaton produces holographic output — non-local, distributed information encoding — and identified this as quantum entanglement from an information-theoretic perspective. That identification was relational: it said *what* entanglement is in SB-HC4A terms. This section confronts the constraint that disciplines every such proposal — Bell's theorem — and states precisely what the architecture explains, what it assumes, and what it still owes.

**One locus, two reflections.** Under the single-surface ontology of Sections 5.2 and 5.7, two entangled particles are not two systems that share a common cause. They are a single configuration — one locus — on the holographic boundary, which appears as two spatially separated particles only in the decompressed interior description. The components of this claim are already in place elsewhere in the paper; they have simply not been connected to entanglement until now. The ER=EPR conjecture (Maldacena & Susskind, 2013; Section 5.2) asserts exactly this: an entangled pair is connected by a Planck-scale Einstein-Rosen bridge — at the substrate level, the two are not separate. Van Raamsdonk's (2010) result (Section 6.3) supplies the complementary half: spatial connectivity itself is built from entanglement, so the three-dimensional distance "between" the particles is an emergent property of the entanglement structure, not a fundamental fact that the entanglement must somehow reach across. The same conclusion follows from the holography-of-information results discussed in Section 8.2 (Raju, 2022): boundary data are not localized in the interior sense at all. What presents itself in the interior as two systems separated by a spacelike gap is, on the boundary, one configuration with no gap to bridge.

**The Bell constraint.** Bell (1964), in the CHSH formulation (Clauser, Horne, Shimony, & Holt, 1969), establishes that any theory satisfying two premises is bounded by S ≤ 2 in the CHSH correlation measure: *measurement independence* (the hidden state λ is uncorrelated with the choice of measurement settings) and *factorizability* (P(a,b|λ) = P(a|λ) P(b|λ): given the common cause λ, the outcomes at the two wings are statistically independent). Quantum mechanics violates the bound, and experiment confirms the violation. Since the SB-HC4A assumes a deterministic substrate (the assumption declared in Section 3; 't Hooft, 2016), it must reject one of the two premises. It rejects factorizability — and it rejects it at the root rather than by tuning the hidden variable. Factorizability presupposes that there are two systems, occupying spacelike-separated regions, whose joint state decomposes into independent local states once λ is given. Under the single-surface ontology that presupposition fails before any λ is specified: there are not two systems, and the spacelike separation across which the factorization is defined is a feature of the emergent interior description, not of the substrate. Interior three-dimensional distance is emergent (Section 6.3); on the boundary there is no spacelike gap across which a "nonlocal influence" would have to propagate. The Bell correlations are not signals passing between distant systems. They are two interior reflections of one boundary configuration.

**Determinism without conspiracy.** Rejecting interior locality while retaining determinism is not an exotic maneuver; it is the oldest consistent position in the foundations literature. Bohmian mechanics (Bohm, 1952) is a fully deterministic, explicitly nonlocal theory that preserves measurement independence and reproduces every prediction of quantum mechanics, including the maximal CHSH violation. It serves here as an existence proof: deterministic, nonlocal, and non-superdeterministic is a coherent corner of theory space. It is the corner the SB-HC4A occupies.

**Why this is not superdeterminism in disguise.** An obvious worry: if observer, apparatus, and particle pair are all reflections of one surface, does the architecture not covertly correlate everything with everything — including measurement settings with hidden states, which is the superdeterministic loophole? It does not, because the one-locus identification is selective rather than global. Which interior systems count as reflections of a *single* boundary locus is determined by the entanglement structure, and entanglement is monogamous: a maximally entangled pair cannot simultaneously be entangled with third systems. The apparatus settings — whether chosen by a random number generator, an experimenter, or the photons of a distant quasar — are not entangled with the pair before the measurement, and therefore do not participate in the locus. Measurement independence is preserved. Superdeterminism remains available as a further option — one I find independently interesting — but nothing in the architecture requires it, and this section does not invoke it.

**No signalling.** Boundary non-separability yields correlations, never signals: the marginal statistics at each wing are independent of the setting chosen at the other, so the architecture respects the no-signalling constraint exactly as quantum mechanics does.

**The James-Stein lens.** A classical result from estimation theory provides an illuminating — though, as stated below, not yet rigorous — description of this non-separability. The James-Stein theorem (Stein, 1956; James & Stein, 1961) shows that when d ≥ 3 parameters are drawn from a shared distribution, estimating them independently is *inadmissible*: it is dominated by a joint "shrinkage" estimator that exploits the shared origin. (Brown, 1971, showed this admissibility boundary at d = 3 coincides with the recurrence/transience boundary of Brownian diffusion; the result is not to be confused with quantum Stein's lemma, which concerns hypothesis testing.) The standard objection to deploying this theorem in physics is that inadmissibility is a property of *estimators* — of descriptions — not of physical states. Under the single-surface ontology the objection loses its force, because interior states *are* descriptions: they are decodings of the one boundary locus (Section 8.2), not independently existing systems that descriptions merely track. Read this way, the theorem says that the independent product-state description of an entangled pair is an inadmissible decoding of the single boundary configuration, and the entangled — jointly shrunk — description is the admissible one. The non-separability of the quantum state is the non-separability of the only accurate description of one locus.

The lens stops at the qualitative claim. The shrinkage coefficient w = (d−2)σ²/‖θ‖² is not read here as a scaling law for multi-partite correlation strength, decoherence, or the semiclassical limit: that quantity is defined for many independently parameterized systems, and for a single boundary locus it has no established interpretation. The classical Stein effect lives on Euclidean parameter spaces; McCormack and Hoff (2022) extend it to Fréchet means in CAT(0) metric spaces; the discrete, combinatorially structured configuration space of holographically saturated boundaries (cf. the Levin-Wen excitations referenced in Section 11.1) is neither, and a discrete Stein-type theorem would have to be built from scratch. Results from quantum estimation theory — the inadmissibility of maximum-likelihood tomography (Ferrie & Blume-Kohout, 2018), James-Stein advantages in entangled Gaussian sensing (Salmon, Strelchuk, & Arvidsson-Shukur, 2024), the equivalence of minimax estimation to a ground-state problem with Fisher information as the potential (Tsang, 2020) — show that shrinkage phenomena are real and consequential in quantum description. They keep the lens credible; they do not certify the mechanism.

The formal home of the claim is more likely holographic quantum error correction than the Stein literature. There, bulk information is encoded redundantly in a boundary state so that it is recoverable from suitable subregions and not from their complements (Almheiri, Dong, & Harlow, 2015; Pastawski, Yoshida, Harlow, & Preskill, 2015), and entanglement-wedge reconstruction makes precise which boundary region suffices to decode a given bulk operator (Dong, Harlow, & Wall, 2016). Joint decoding succeeding where product decoding fails is there a property of the code, not an analogy drawn from estimation — which is the claim this section needs and cannot yet derive. The formalization owed here will more plausibly come from that direction than from a discrete Stein theorem.

**The empirical anchor.** Afik and de Nova (2022) proposed using top-quark pair production at the LHC — the highest-energy regime experimentally accessible — to probe entanglement and Bell-inequality violation, and the ATLAS and CMS collaborations subsequently *observed* entanglement in top–antitop production (ATLAS Collaboration, 2024; CMS Collaboration, 2024). Bell-inequality *violation* in this system has been proposed and analysed but is not yet experimentally established. The observed entanglement functions in the present argument not as support but as a specification of the target: it establishes that entanglement is a substrate-level property — persisting undiminished at the highest energies probed — rather than an artifact of low-energy effective description, and it fixes the empirical correlation strength that any substrate-level mechanism must reproduce.

**What is actually owed: Tsirelson's bound.** Denying factorizability dissolves the Bell constraint, but it dissolves it too well. The full set of no-signalling correlations extends far beyond the quantum set — up to the Popescu-Rohrlich box value S = 4 (Popescu & Rohrlich, 1994) — while quantum mechanics, and nature, stop at Tsirelson's bound S = 2√2 (Cirel'son, 1980). Merely "reproducing the quantum value" is therefore a near-empty achievement: any of countless nonlocal mechanisms can be tuned to emit S = 2√2. The non-trivial obligation — open not just for the SB-HC4A but for every substrate-level reconstruction of quantum mechanics — is to *derive the ceiling*: to explain why boundary non-separability produces correlations up to exactly 2√2 and no further, when no-signalling alone would permit 4. The ceiling is closer to hand than it first appears. *Information causality* (Pawłowski et al., 2009) states that the information a receiver can obtain about a sender's database cannot exceed the capacity of what was sent, Σ_k I(a_k : b | K = k) ≤ m; it recovers Tsirelson's bound through the Uffink inequality exactly where no-signalling alone fails to, and recent work has made it an efficient tool for bounding the quantum set in general Bell scenarios (Jain, Gachechiladze, & Miklin, 2024). The architecture does not have to derive that principle from anything, because under the commitments already made it *is* one of them. The holographic bound makes boundary information finite per unit area, and under the single-surface ontology of Section 5.2 an entangled pair is one boundary locus rather than two systems. The information the two wings can jointly extract is therefore information read off that locus, bounded by its capacity — which is the information-causality inequality with the locus capacity in place of a transmitted-bit count. The quantum ceiling follows.

One step in that argument is asserted rather than proven, and it should be named: that the pair's joint statistics are decodings of a *single* boundary locus whose jointly accessible information is capacity-bounded. Two clauses of that postulate are load-bearing and must be stated with it wherever it is restated, because without them it is not a weaker claim but a refuted one. **Jointness:** the reconstruction is irreducibly joint — the statistics do not factor through any decomposition into per-wing decodings with setting-independent locus content. Read distributively, with each wing separately decoding the locus content and measurement independence retained as this section retains it, the postulate *is* a local hidden-variable model and yields CHSH ≤ 2, which is the bound the section exists to escape; jointness is therefore what makes the postulate compatible with the observed violation in the first place, not an added strengthening of it. Note that "one locus" here means one *connected wedge*, not one connected boundary patch: the locus may be disconnected on the surface while its wedge is connected in the bulk, which is precisely the eternal-black-hole configuration in which two disjoint boundary regions hold one connected wedge (Maldacena & Susskind, 2013). **Minimality:** the locus must be the minimal one meeting that condition. Read as licensing the whole encoding surface, the capacity bound constrains nothing — a cosmological-horizon budget of order 10¹²² bits cuts no correlation set whatever, and the argument would go through for supra-quantum correlations as readily as for quantum ones. This is the single-surface ontology applied to entanglement, which is the same application Section 5.2 already makes and this section already relies on in rejecting factorizability; but applying an ontological postulate is not the same as proving a theorem about accessible information, and turning it into one is a question for entanglement-wedge reconstruction (Dong, Harlow, & Wall, 2016) — the direction the preceding lens also points.

A standing objection to this route deserves a direct answer. Oughton and Timpson (2024) show that information causality recovers Tsirelson's bound only when the information measure is Shannon, failing under Rényi-2, which makes the principle look dependent on an arbitrary choice. Here the choice is not made at the level of the principle. The rigorous forms of the Bekenstein bound are statements about relative entropy at α = 1 (Casini, 2008; Longo, 2024; Kudler-Flam et al., 2025); quantum mutual information is itself a relative entropy, S(ρ_AB ‖ ρ_A ⊗ ρ_B); and on states diagonal in a common basis the von Neumann quantity reduces to the classical one. The registers in the protocol are classical, so the measure is inherited from the physical bound by restriction rather than selected for convenience. Were a Rényi-α analogue of the 2πER inequality established, this reply would weaken accordingly.

What none of this buys, even granted in full, is a reconstruction of quantum theory: information causality does not uniquely single out quantum correlations, since certain supra-quantum "almost quantum" correlation sets satisfy its known consequences (Navascués, Guryanova, Hoban, & Acín, 2015). The claim is the narrower one — that the ceiling is entailed by commitments the architecture makes on independent grounds, modulo the decoding step named above.

**What this section claims.** Three things, in descending order of strength. First, the existence and substrate-level character of nonlocal correlations follow from commitments the paper already makes on independent grounds — a holographic boundary (Section 5.2), entanglement-built spatial connectivity (Section 6.3), and singularity-unified topology (ER=EPR) — with measurement independence and no-signalling preserved; the Bell escape is the denial of fundamental interior locality, and Bohmian mechanics proves the resulting corner of theory space is coherent. Second, the James-Stein inadmissibility theorem supplies a heuristic lens under which the entangled state is the admissible description of a single boundary locus — illuminating, quantitatively uninterpreted, and likelier to be made rigorous through holographic quantum error correction than through a discrete Stein theorem. Third, the Tsirelson ceiling follows from those same commitments by way of information causality, conditional on the single-locus decoding step named above, and with the measure-dependence objection to that route answered from the relative-entropy form of the Bekenstein bound. An explanation of entanglement's existence and character; an interpretive lens on its description; and a conditional derivation of its quantitative ceiling, with the condition stated.

---

## 7. Self-Referential Computation Across Scales

### 7.0 A Note on Terminology

This section maps a cosmological architecture onto a cognitive one, and four words do different work on the two sides. Fixing them here prevents the mapping from appearing to claim more than it does.

**Decompression, not simulation.** The interior is called the *decompressed form* of the boundary throughout, and the word "simulation" is reserved for its ordinary computational senses — running an automaton forward, or one universal system emulating another. The distinction is not cosmetic. Decompression is *syntactic*: the interior is what the boundary's compressed description unfolds into, and nothing in that relation requires the interior to be *about* anything. Representation is *semantic*: a model of X stands for X and can misrepresent it. The cognitive side of the mapping involves representation, because a self-model represents the system that holds it; the cosmological side, as argued here, involves only decompression. Reading the interior as a representation would import a represented-thing the architecture does not posit, and would file the model with proposals it does not resemble.

**Holographic** means dimensional reduction with an area law in the physics literature, and distributed storage with graceful degradation in the Lashley–Pribram sense. Both senses appear in this paper, and Section 6.1 distinguishes them explicitly; where the term is used without qualification the physics sense is meant.

**Observer** means a world-line with a causal past in Section 5.2, and a subject of experience to any reader arriving from the consciousness literature. Only the first sense is used in the cosmological argument. Nothing in Sections 2–6 requires an observer to be conscious, and the cosmological argument stands if no observer ever is.

**Information** is used in three senses that are not the same quantity: thermodynamic entropy, Kolmogorov complexity, and semantic content. The first two are provably distinct and the third is not a formal quantity at all. Where the paper's argument turns on a bound, the quantity is thermodynamic entropy in bits; where it turns on compressibility, it is description length. The semantic sense appears only in the cognitive correspondence of this section, and never in the derivations.

### 7.1 The Structural Mapping

The SB-HC4A architecture is conjectured to map onto the architecture of self-referential computational systems, with the following structural correspondences:

| SB-HC4A (Universe) | Self-Referential Computation (Cognitive Systems) |
|---|---|
| Singularity boundary (information-opaque) | Implicit-explicit boundary (representationally opaque) |
| Observable interior (physics) | Explicit models (decompressed representations) |
| Holographic rule structure | Distributed/holographic implicit knowledge |
| Class 4 dynamics | Critical neural dynamics |
| Self-referential closure: Φ(U) = U | Self-referential closure: Φ(m*) = m* |
| Conservation of energy/information across boundary | Conservation of information across implicit-explicit split |
| Inexpressibility from within (Gödel) | Meta-cognitive limitation: systems cannot fully represent their own substrate |
| Singularity boundary at every scale | Implicit-explicit boundary at every level of the model hierarchy |

### 7.2 Structural Correspondence, Not Mere Analogy

This mapping is proposed as more than metaphorical: the claim is that both systems fall in the same computational class and share the following architectural features. Whether this rises to a strict structural identity — rather than a strong correspondence — is left open, and is the burden of the formalization (Gruber, 2026 formalization, §6).

1. **Both are Class 4 dynamical systems** operating at the edge of chaos. The universe maintains criticality through self-organized criticality (Bak et al., 1987). Neural systems maintain criticality through homeostatic regulation of excitation-inhibition balance (Hengen et al., 2016; Ma et al., 2019).

2. **Both are bounded by information-opaque surfaces.** The universe's singularity boundaries prevent information transfer (event horizons, Planck regime). Self-modeling systems have an implicit-explicit boundary that prevents representational access to substrate operations (Gruber, 2026a, Section 3.6).

3. **Both have holographic structure.** The universe's information content is encoded on boundaries ('t Hooft, 1993; Susskind, 1995). Neural information storage is holographic — distributed across the substrate, degrading gracefully under damage (Lashley, 1950; Pribram, 1971).

4. **Both exhibit self-referential closure.** The universe computes its own structure (the laws of physics are the universe's dynamics applied to itself). Self-modeling systems represent their own modeling processes (self-referential closure: Φ(m*) = m*).

5. **Both are inexpressible from within.** The universe's complete specification exceeds any internal formal system (Gödel). Self-modeling systems cannot fully represent their own substrate (the meta-cognitive limitation; Gruber, 2026a, Section 3.7; compare Chalmers, 2018).

### 7.3 Self-Referential Computation as a Universal Pattern

The claim is not that the universe is "conscious" in any experiential sense. The claim is that the universe and self-modeling cognitive systems are conjectured to instantiate the *same computational pattern* at different scales:

- The **universe** is a Class 4 holographic automaton bounded by singularities, where the interior (observable physics) is the *decompressed form* and the boundary (singularity layer) is the *substrate*.

- **Self-modeling cognitive systems** are Class 4 holographic automata (critical neural dynamics) bounded by the implicit-explicit boundary, where the explicit models are the *decompressed form* and the implicit models are the *substrate*.

Same architecture. Different scale. The pattern is fractal — which is precisely what a Class 4 system predicts, since Class 4 dynamics contain Class 3 (self-similar) behavior as a subprocess.

---

## 8. Energy, Information, and Conservation

### 8.1 The Energy-Information Hypothesis

Landauer's principle (Landauer, 1961) establishes a minimum energy cost for erasing one bit of information: kT ln 2. The Bekenstein bound (Bekenstein, 1981) ties the same two quantities in the opposite direction, and it is the form of the bound stated in Section 5.2 — not the area law — that does so: the entropy of a bounded system is capped by its energy and radius, S ≤ 2πkER/ħc, so a system's information capacity is fixed by an energy budget. Black hole thermodynamics (Bekenstein, 1973; Hawking, 1975) assigns entropy, temperature, and information content to black holes through their surface area.

These results converge on a hypothesis: energy and information are not merely correlated but identical — two descriptions of the same quantity. This is not proven, and I flag it as a weak point (Section 9.1). But if E = I, the conservation laws become information conservation laws, and the SB-HC4A architecture acquires a natural conservation principle.

### 8.2 Conservation Across the Singularity Boundary

If energy/information is conserved, singularities do not destroy information — they *transform* it. This is the resolution of the black hole information paradox that modern physics is converging on (Almheiri et al., 2021; Penington, 2020; Raju, 2022). Information that enters a black hole is not lost; it is encoded on the event horizon (holographic encoding) and eventually re-emitted through Hawking radiation. This is the non-perturbative tier of IB1 (Section 5.2), and it is consistent with impermeability rather than an exception to it: no observer who remains inside the computational domain reads anything from behind the boundary, while the substrate holds the information throughout. Unitarity is the operative word in that resolution: information conservation across a horizon requires that the underlying dynamics be reversible — a requirement Section 8.4 elevates to an explicit architectural commitment.

Black-hole complementarity (Susskind, Thorlacius, & Uglum, 1993; 't Hooft, 1985) gives this conservation an observer-indexed form that the present model generalizes: the exterior description — infalling matter freezing, thermalizing, and scrambling on a stretched horizon before re-emission — and the infalling description — a smooth, markerless crossing followed by ordinary interior physics — are both valid accounts of the same information, and no observer can access both, the horizon's causal structure protecting the no-cloning theorem. These are, respectively, the compressed and decompressed forms defined below: complementarity is the established local instance of the substrate/interior duality, of which the single-surface ontology of Section 5.2 is the proposed generalization. Whether the smooth interior survives unitarity for old black holes remains contested (the firewall argument: Almheiri, Marolf, Polchinski, & Sully, 2013); the entanglement-island results already cited (Penington, 2020; Almheiri et al., 2021) currently favor smoothness, and nothing in this section depends on the outcome.

In the SB-HC4A model, this generalizes: the singularity boundary at every scale conserves total information while transforming it between compressed (boundary) and decompressed (interior) forms:

- **Compressed form** (on the boundary): Maximum information density, holographically saturated, inaccessible from within. This is the "substrate."
- **Decompressed form** (in the interior): Lower density, organized, accessible. This is the **decompressed form** — the observable universe, or the representational content of self-modeling systems.

### 8.3 The Implicit/Explicit Parallel

This is precisely the implicit/explicit split in self-referential computational systems:

- **Implicit knowledge** (substrate): Holds all the information — synaptic weights, structural knowledge, the full learned model. Maximum information density. Not representationally accessible.
- **Explicit models** (the decompressed form): A lower-bandwidth, organized projection of selected information. Accessible to the system's self-representation. This is the representational content of self-modeling systems.

The permeability function in self-referential computation (Gruber, 2026a, Section 3.6; Gruber, 2026b, Section 3) determines how much information transfers from implicit to explicit — how much of the compressed substrate becomes part of the explicit representation. The laws of physics play the analogous role at the cosmological scale: they determine what information from the singularity-layer substrate enters the observable interior.

### 8.4 Reversibility and the Emergent Arrow of Time

The conservation discussion above presupposes a commitment the model should state explicitly. The SB-HC4A's supporting machinery is uniformly reversible: Wetterich's automaton–QFT equivalences (Section 5.6) hold for *reversible* cellular automata; the Page-curve resolution of the information paradox (Section 8.2) is a statement of unitarity; 't Hooft's (2016) deterministic substrate evolves by information-preserving dynamics. Yet the model also leans on entropy increase, heat death, and cyclic renewal (Section 5.4) — apparently irreversible physics. The resolution is a definite architectural commitment: **the microscopic substrate is reversible** — no two distinct substrate states evolve to the same state, and total information is conserved — while **the arrow of time and the apparent randomness of interior physics are emergent**, products of coarse-graining and horizon information-loss, not of the substrate law. An interior observer tracks only the decompressed projection; the information needed to invert the dynamics is precisely the information sequestered behind singularity boundaries. Landauer erasure is real for the interior description and absent at the substrate level. The interior's Rule-30-like irreversibility — one-way, entropy-producing, illegible — is the coarse-grained shadow of a reversible boundary computation satisfying Φ(U) = U. The CPT alternation between cycles (Section 5.4) is the global expression of this same reversibility: what looks from inside like destruction and restart is, at the substrate level, an information-preserving transformation.

Reversible laws do not erase the arrow. The thermodynamic arrow, on the standard analysis, is not a property of the dynamical law at all but of a boundary condition — the low-entropy past, the Past Hypothesis (Albert, 2000) — combined with coarse-graining. The SB-HC4A inherits this structure directly: the substrate law is reversible; the arrow lives in the asymmetry between the highly compressed initial boundary state (the seed of the decompression) and the coarse-grained interior description that cannot see behind horizons.

**Playback reversal: two faces of one trajectory.** "Reversing time" can mean two different things, and the distinction sharpens what the emergent arrow is. *Reversing the dynamics* — running an interior-effective rule like Rule 30 backwards as a local rule — is ill-defined: the rule is many-to-one, and a given row has many possible predecessors. *Watching a realized history backwards* — playback reversal — is perfectly definite: there is exactly one realized past. And for a computationally irreducible automaton the playback-reverse has a striking property: it is **non-local**. Nothing local in row t+1 singles out the actual row t from its many possible predecessors; what singles it out is the entire realized history — equivalently, the full boundary data. Played backwards, Rule 30 looks like globally coordinated dynamics: scattered, disordered cells converge with perfect choreography onto simple structure, as if the whole lattice were conspiring. This is not mysterious — Bennett (1973) showed that a computation run backwards is *uncomputation*, itself a perfectly good computation, but one whose steps are coordinated by the complete record of the forward run.

The same trajectory therefore presents two faces. **Forward** (interior-ward): local, divergent, illegible — decompression from the seed and boundary, entropy increasing, structure proliferating without visible purpose. **Boundary-ward**: non-local, convergent, and legible *as computation* — a process that terminates on the fixed point Φ(U) = U, readable only against the complete boundary data, and therefore apparently teleological. The defensible core of this observation is the asymmetry itself — locality versus non-locality, divergence versus convergence, illegibility versus legibility — which is a crisp restatement of the arrow of time for irreducible computation. The further reading — that the boundary-ward face is *the* computation, that the universe's self-computation is legible only in the direction that terminates on its own fixed point, and that this apparent teleology is the signature of self-referential closure — is an interpretive layer, and I label it as such.

**Relativity as confirmation.** One might expect relativity to constrain this picture; on inspection it confirms it. The CPT theorem (Lüders, 1957; Pauli, 1955) establishes that any Lorentz-invariant, local, unitary quantum field theory is CPT-symmetric — a deep reversibility of the laws is a *theorem* of the continuum physics the substrate must reproduce. And special and general relativity geometrize time as a dimension of a four-dimensional manifold, for which the block universe is the default reading. Both results pin the substrate–continuum pair to exactly the commitment made above: a reversible substrate automaton from which CPT and Lorentz symmetry emerge in the continuum limit (Wetterich, 2022c; 't Hooft, 2016), with the Rule-30-like arrow as the emergent interior face.

**The block universe and the fixed point.** The block universe is not merely compatible with the self-referential closure — it is its natural setting. Φ(U) = U can be read as a *timeless* fixed-point condition on the whole four-dimensional block: the block is the configuration that satisfies its own holographic encoding. Computational irreducibility is then the reason a timeless fixed point nevertheless feels like genuine becoming from inside: Class 4 dynamics admit no predictive shortcut (Wolfram, 2002 — the same point recurs in Wolfram's more recent "ruliad" framing), so an embedded observer cannot apprehend the block except by living through the computation. What the architecture is incompatible with is not the block but the *superdeterminist conspiracy* block — one whose initial data fine-tunes correlations between measurement settings and prepared states. Section 6.5 rejects that route for independent reasons, resolving Bell correlations through holographic nonlocality instead; the present section reinforces that choice: the SB-HC4A's block is reversible and self-consistent, not conspiratorial.

---

## 9. Where This Could Break

A theory that claims no weaknesses is not a theory. Here are the seven places where the SB-HC4A model is most vulnerable.

### 9.1 Weak Point 1: Energy = Information Is Not Proven

The energy-information identity is strongly suggested by Landauer's principle, the Bekenstein bound, and the holographic principle, but it is not established as a fundamental law. Landauer's principle has been experimentally confirmed (Berut et al., 2012), but only for erasure — it does not prove that all energy is information. If energy and information are merely correlated rather than identical, the conservation argument (Section 8) weakens, and the mapping between singularity boundaries and information boundaries becomes looser.

Recent work by Vopson (2025) proposes that gravity itself is evidence of a computational substrate, arguing that gravitational attraction arises from information entropy reduction by massive objects. If correct, this provides empirical support for the energy-information identity and connects a specific fundamental force to the computational ontology the SB-HC4A requires.

**What would resolve it**: A derivation of energy conservation from information conservation (or vice versa) within a well-defined physical framework, or an experimental demonstration that information has gravitational effects proportional to its energy-equivalent.

### 9.2 Weak Point 2: Class 4 Universe Is an Empirical Claim, Not a Theorem

Self-organized criticality is well-documented in sandpiles (Bak et al., 1987), neural networks (Beggs & Plenz, 2003), earthquakes (Gutenberg & Richter, 1956), and other systems. But these are all *subsystems within* the universe. Whether the universe *itself* — at its most fundamental level — operates at Class 4 is a much stronger claim. The universe contains Class 4 subsystems; this does not entail that the universe is itself Class 4. A Class 5 universe could contain Class 4 pockets, just as a Class 4 automaton contains Class 2 substructures.

The elimination argument (Section 3.2) is the strongest available response: Class 4 is the only class consistent with all observations. But the elimination of Class 5 rests on abduction (physics would be impossible), not deduction.

**What would resolve it**: Evidence that the universe's large-scale dynamics exhibit criticality signatures — power-law distributions in the cosmic microwave background, scale-free structure in galaxy distributions, or branching ratio analysis of cosmological dynamics. Some of this evidence exists (e.g., the scale-free distribution of galaxy clusters), but it has not been framed as a criticality argument.

### 9.3 Weak Point 3: Singularity Unification Is Speculative

Whether Planck-scale structure, black hole event horizons, and cosmological horizons are truly "the same thing" at different scales requires a theory of quantum gravity to verify. Loop quantum gravity (Rovelli, 2004) and string theory (Polchinski, 1998) both suggest structures consistent with this claim — in loop quantum gravity, spacetime is discrete at the Planck scale with area quantization that connects to black hole entropy; in string theory, the holographic principle is central (Maldacena, 1998). But neither theory confirms the specific claim that all singularities are instances of the same information boundary.

**What would resolve it**: A derivation, within a quantum gravity framework, showing that the information-theoretic properties of Planck-scale boundaries and macroscopic event horizons are formally identical (same entropy scaling, same information capacity per unit area, same causal disconnection properties).

### 9.4 Weak Point 4: Testability Is Limited

The model predicts:

(a) **Singularity universality**: All singularities across scales share informational properties. The resolution of the black hole information paradox should confirm that event horizons conserve information — and the same conservation principle should apply at the Planck scale and the cosmological horizon. Partially testable through black hole information research.

(b) **Cosmological criticality**: The universe's large-scale dynamics are at the edge of chaos. In principle testable through statistical analysis of the CMB, large-scale structure, or the distribution of galaxy cluster sizes. A preliminary multifractal detrended fluctuation analysis (MFDFA) of the Planck 2018 CMB temperature map (Gruber, 2026c) found no excess multifractality at large angular scales (ℓ < 1500), with observed multifractal spectrum widths fully consistent with Gaussian random fields sharing the observed power spectrum. This null result does not bear directly on the SOC hypothesis, because the CMB is a recombination-era observable separated from the initial conditions by inflationary processing — the appropriate targets are primordial gravitational waves, higher-order non-Gaussianity, or late-time nonlinear structure where criticality signatures may be regenerated.

(c) **Self-referential computation as local instance**: Self-modeling cognitive systems implement the same architecture as the universe. Testable through predictions about critical neural dynamics (Gruber, 2026a, Section 8): nine specific predictions about phenomenology, anesthetic mechanisms, and neural criticality.

But the core claim — that the universe *is* an SB-HC4A — may be unfalsifiable from within, for exactly the Gödelian reason the model itself predicts (Section 6.4). The system cannot be fully specified by any subsystem. This is either a devastating weakness or a structural prediction of the model, depending on one's philosophical commitments.

### 9.5 Weak Point 5: The Cognitive Ceiling Problem

This is the deepest objection, and it was identified during the model's initial formulation.

If we are Class 4 automatons operating at criticality, then the SB-HC4A model may simply be the most complex concept our Class 4 brains can produce. We cannot think in Class 5. We cannot conceive of structures beyond our own computational class. The pattern we see — Class 4 everywhere, self-similar at every scale, holographic and self-referential — might be the *signature of our own cognitive architecture projected onto the cosmos*, not a feature of the cosmos itself.

This objection connects to the evolutionary biology of cognition. The human brain evolved under selection pressure for symmetry detection — faces of predators and prey are the most symmetric, and therefore most survival-relevant, patterns in a hunter-gatherer's environment. We are, at the deepest level, symmetry-detection machines. The SB-HC4A model is fundamentally a symmetry claim (the same architecture at every scale). We might find this symmetry not because it exists in the universe but because our brains are optimized to find symmetry wherever they look.

This is structurally identical to the Meta-Problem at cosmic scale: the ESM cannot see its own substrate, so it cannot distinguish between "the universe has this structure" and "my brain can only model the universe with this structure." The cosmological model predicts its own potential unfalsifiability — which is either the strongest possible confirmation of the cross-scale computational symmetry (the model predicts this exact epistemological limitation) or the strongest possible objection to it (the model is an artifact of the observer, not a feature of the observed).

A Class 4 system can simulate anything up to and including Class 4 complexity. But it cannot verify whether the universe exceeds that. If the universe is Class 5 but locally appears Class 4 to Class 4 observers (because Class 4 is the maximum pattern we can detect), we would construct exactly this model — and be wrong.

I do not know how to resolve this objection from within. I am not sure it can be resolved from within. I include it because intellectual honesty requires it.

### 9.6 Weak Point 6: Cyclic Cosmology Is Underdetermined

The cyclic cosmology of Section 5.4 follows logically from the premises (singularities transform information; heat death is a singularity; therefore heat death triggers transformation), but the specific predictions — Big Bang / Big Crunch alternation, CPT signature flipping, Big Rip branching — go beyond what the framework strictly entails. The information-transformation property of singularities does not by itself determine *what form* the decompressed information takes. A singularity transition could produce a new universe with entirely different physics, the same physics, or the CPT-conjugate physics; and the Big Rip's fragmentation into multiple daughter universes raises additional questions about how total information is partitioned across branches. The model predicts cyclicity (or branching cyclicity) but underdetermines the cycle's character.

The CPT alternation hypothesis is motivated by parsimony (the simplest nontrivial transformation) and by its explanatory payoff (baryon asymmetry), but it is not derived from first principles within the framework. It should be read as a natural possibility within the SB-HC4A architecture, not as a firm prediction.

The underdetermination extends beyond the cycle's character: the axioms also leave the dimensionality of the automaton open (Section 10.2). One might worry that this feeds a fine-tuning objection — that Class 4 dynamics require a delicately chosen rule, so the selection argument of Section 3 demands luck. The cellular automaton literature suggests the opposite trend. In one dimension, Class 4 is razor-thin: of the 256 elementary rules (88 equivalence classes under mirror and complement), essentially one family is clearly complex and computationally universal — Rule 110, proven universal by Cook (2004), with Rule 54 a conjectured second. In two dimensions the picture inverts: complex and universal rules are commonplace. Conway's Game of Life (B3/S23) is proven universal; HighLife (B36/S23) supports a natural self-replicating pattern; Day & Night (B3678/S34678) exhibits complex dynamics under an exact on–off state symmetry — and these sit inside a space of 2⁵¹² binary Moore-neighborhood rules whose classification is formally undecidable (Culik & Yu, 1988). The lesson — an empirical trend in the CA literature, not a theorem — is that complexity and universality become *more* generic as dimension rises. If the trend continues into 3+1 dimensions, the edge-of-chaos regime is presumably more generic still, and the fine-tuning worry softens: the universe need not be delicately tuned to land in Class 4 if Class 4 is generic in high-dimensional rule spaces. Leaving the dimension open is therefore an underdetermination that cuts in the architecture's favor.

**What would resolve it**: Observational evidence of pre-Big-Bang structure. Penrose (2010) has proposed searching for concentric low-variance circles in the CMB as signatures of preceding aeons. However, critical reanalysis by Jow and Scott (2020) found no statistically significant CMB signatures for Penrose's "Hawking points," casting doubt on the specific CCC observational program. This does not directly affect the SB-HC4A's cyclic cosmology, which derives cyclicity from the information-theoretic properties of singularity boundaries rather than from conformal rescaling; the two models predict different observational signatures, and the SB-HC4A's specific signatures remain to be derived (Section 9.4). Boyle, Finn, and Turok (2022) further developed the CPT-symmetric program with a concrete prediction: the right-handed neutrino as dark matter. If the SB-HC4A cyclic model is correct, similar signatures should exist — though their specific form depends on details of the singularity transition that the model does not yet specify.

### 9.7 Weak Point 7: The Saturation Trigger Is a Motivated Conjecture

The cyclic cosmology depends on a specific dynamical claim: that holographic saturation *triggers* decompression — that a boundary at maximum information density cannot be statically sustained and must transform into a new interior. This transition is the engine of every renewal scenario in the framework (heat death, Big Crunch, Big Rip), and it is a motivated conjecture, not a derived result.

The difficulty is concrete. The de Sitter horizon entropy that dominates the late universe (~10¹²² k_B) is essentially constant from early times; nothing obviously *changes* dynamically at the proposed trigger moment. Section 5.4's response is the saddle-point mechanism: maximum boundary information density is an extremum of the computation that is maximally *disordered* rather than dead — unlike the trivial extrema of Class 1 (the all-off or all-on lattice) — and the fixed-point condition Φ(U) = U cannot be statically held there, because no further distinctions are encodable. The dynamics are forced off the extremum, and the fully loaded boundary decompresses into a new ordered interior. This mechanism is plausible, and it has a cousin in the literature: Penrose's (2010) Conformal Cyclic Cosmology, in which the remote saturated future of one aeon becomes the Big Bang of the next — Section 5.4's mechanism is, in effect, its automaton-theoretic form. But it is unproven. The honest state of the evidence is sobering: the best-studied Class 4 automaton, the Game of Life, is too primitive to exhibit anything like it — random high-density soup does not decompress into new order; it decays to sparse "ash." Demonstrating a saturation-to-decompression transition requires assembling, in one construction, the ingredients now known to exist separately — high-density complexity and an exact on/off symmetry (as in the Day & Night rule) together with reversibility (as in reversible block automata) and a boundary channel into which entropy can be exported (Section 5.4); no single rule yet combines them.

**What would resolve it**: A concrete automaton — or any well-defined dynamical system with a holographic bound — in which driving the boundary to maximum information density provably destabilizes the configuration and produces a re-ordered interior phase. Short of that, a formal instability result: a proof that Φ(U) = U admits no static solution at holographic saturation.

---

## 10. The Necessity Argument

### 10.1 The Argument from the Axioms

Notwithstanding the weak points above, the SB-HC4A is the best candidate architecture consistent with all five axioms simultaneously — where "best candidate" is meant precisely: each axiom is necessary for the conclusion (Section 10.2), and the architecture is what their conjunction motivates, even though the axioms do not force every feature of the model.

**Axiom 1** (Ontological Necessity): Something exists. Nothing is not a possible state of affairs — argued in Section 3.1 along two independent lines, ontological and epistemic, with the modal and vacuum-decay counterexamples treated there.

**Axiom 2** (Computational Character): Whatever exists has dynamical behavior classifiable within the five-class hierarchy.

**Axiom 3** (Criticality Selection — conditional on the substrate-determinism assumption of Section 3): Given a deterministic substrate, Class 4 is the only class in the taxonomy that (a) supports universal computation, (b) self-maintains through self-organized criticality, and (c) contains Classes 1–3 as subprocesses.

**Axiom 4** (Information Bound): Information propagation speed is bounded by c. Information density per unit boundary area is bounded by the holographic bound, and the entropy of a bounded system by the Bekenstein bound (Section 5.2). Information is conserved.

**Axiom 5** (Holographic Encoding): The boundary of a d-dimensional region encodes all information in the region's interior on its (d−1)-dimensional surface.

From these:

- A1 + A2 → Something with dynamical behavior exists.
- A3 → Given substrate determinism, that behavior is Class 4 — selected by elimination (Section 3.2), not by fiat.
- A4 → The system is bounded by information horizons at every scale (singularity structure).
- A5 → The boundaries encode the interior (holographic architecture).
- A3 + A5 → The system is a holographic Class 4 automaton.
- A4 + A5 → The boundaries are holographically saturated and scale-invariant.
- Self-referential closure: A holographic Class 4 system with holographic output is a fixed point: Φ(U) = U.

### 10.2 Necessity, Not Uniqueness

Each axiom is necessary for the conclusion. Remove any one and the architecture is no longer motivated:

- Without A1: Nothing is possible — no universe required.
- Without A2: The existent thing need not have computational character — mysterian position.
- Without A3: Any dynamical class is permissible — no prediction about the universe's dynamics.
- Without A4: No information horizons — no singularity structure — no boundaries.
- Without A5: No holographic encoding — no boundary-interior relationship.

This is a necessity claim about the axioms, not a uniqueness claim about the model. The five axioms jointly select an architecture *class* — singularity-bounded, holographic, Class 4, self-referentially closed — but they underdetermine the model within that class. The dimensionality of the automaton, the exact singularity inventory, whether the cosmology is linearly cyclic or branching, and whether CPT signatures alternate across cycles (Section 9.6) are all left open by A1–A5: they are motivated extensions, not consequences. At least one of these underdeterminations works in the architecture's favor — as Section 9.6 notes, the prevalence of complex, universal rules rises with dimension in the CA literature, so leaving the dimension open eases the Class 4 selection rather than threatening it.

The argument is that these axioms are not arbitrary assumptions but well-supported physical and logical principles, and that their conjunction yields a tightly constrained cosmological architecture — constrained in kind, underdetermined in detail.

---

## 11. Discussion

### 11.1 Relationship to Existing Cosmological Proposals

The SB-HC4A model intersects with several existing research programs:

**'t Hooft's Cellular Automaton Interpretation** ('t Hooft, 1993, 2016): The model is a direct extension of 't Hooft's proposal that quantum mechanics emerges from deterministic automaton dynamics at the Planck scale. The SB-HC4A adds the Class 4 classification (specifying which class of automaton), the singularity boundary structure, and the cross-scale symmetry with self-referential computation.

**The Holographic Principle** ('t Hooft, 1993; Susskind, 1995; Bousso, 2002): The model presupposes the holographic principle and extends it by proposing that holographic encoding is not just a property of boundaries but of the automaton's rule structure itself (Relationship 3 of Section 6.1).

**Self-Organized Criticality** (Bak et al., 1987; Bak, 1996): The model relies on SOC as the mechanism by which the universe maintains Class 4 dynamics. The extension is the claim that this self-organization operates at the cosmological level, not just in subsystems.

**Digital Physics** (Fredkin, 2003; Zuse, 1969; Wolfram, 2002, 2021): The model shares the premise that the universe is fundamentally computational but adds specific structure: the five-class hierarchy, the holographic property, the singularity boundary, and the cross-scale symmetry with self-referential computation. The Wolfram Physics Project's more recent results on emergent GR and QM from hypergraph rewriting are discussed separately below.

**Wheeler's "It from Bit"** (Wheeler, 1990): The model is consistent with Wheeler's proposal that information is ontologically fundamental. The E = I hypothesis (Section 8.1) is a strong version of "it from bit."

**Penrose's Conformal Cyclic Cosmology** (Penrose, 2010): CCC proposes that the universe undergoes infinite cycles (aeons), with the conformally rescaled heat death of one aeon becoming the Big Bang of the next. The SB-HC4A model's cyclic cosmology (Section 5.4) shares the cyclic structure and the identification of heat death as a transition rather than a terminus. The key difference is the mechanism: Penrose relies on conformal rescaling and the vanishing of rest mass at late times; the SB-HC4A model relies on information transformation at singularity boundaries. The SB-HC4A mechanism is more general — it derives cyclicity from the information-theoretic properties of singularities rather than from specific geometric operations.

**The Boyle–Turok CPT-Symmetric Universe** (Boyle, Finn, & Turok, 2018; Boyle & Turok, 2024): This proposal places a CPT mirror at the Big Bang, with our universe paired with a CPT-conjugate anti-universe extending backward in time. The SB-HC4A model's CPT signature alternation (Section 5.4) is compatible with this picture but extends it: rather than a single mirror, the model predicts ongoing CPT alternation across cycles, with each singularity transition potentially flipping the matter-antimatter signature. Boyle, Finn, and Turok (2022) further developed this program with a concrete prediction: the CPT-symmetric universe requires a right-handed neutrino as dark matter, providing the model's most specific observational signature — a prediction the SB-HC4A model is agnostic about but does not exclude.

**Phantom Energy and the Big Rip** (Caldwell, 2002; Caldwell, Kamionkowski, & Weinberg, 2003): The Big Rip scenario — in which phantom dark energy (w < −1) drives the expansion rate to divergence at a finite future time, tearing apart all bound structures down to spacetime itself — provides a third cosmological endgame distinct from heat death and Big Crunch. The SB-HC4A model accommodates this scenario naturally (Section 5.4): the Big Rip fragments the computational domain into many holographically saturated boundaries, each of which triggers an independent information transformation and restart. This generalizes the cyclic dynamics from a linear sequence to a branching tree of sub-universes — a structural multiverse arising from the same singularity-as-information-transformer principle that drives the linear cycles. The model's robustness across all three endgames — heat death, Big Crunch, and Big Rip — is a significant strength: the cyclic cosmology does not depend on the equation of state of dark energy taking any particular value.

**Wetterich's Cellular Automata ↔ Fermionic QFT Equivalences** (Wetterich, 2022a, 2022b, 2022c): Wetterich has demonstrated that large classes of reversible cellular automata on space-lattices are exactly equivalent to discretized fermionic quantum field theories — not as an approximation but as a proven mathematical mapping via Grassmann functional integrals. The equivalence class includes interacting fermion theories with both abelian and non-abelian continuous symmetries, and some automata models realize local gauge symmetries — the structure the Standard Model requires. Most remarkably, Wetterich (2022c) constructed a cellular automaton that represents spinor gravity in four dimensions, with exact local Lorentz symmetry on the discrete level and emergent diffeomorphism symmetry in the continuum limit. This is a cellular automaton model of quantum gravity — not a metaphor. For the SB-HC4A, Wetterich's program provides the existence proof that the computational-atom picture (Section 5.6) is mathematically sound: specific automata produce specific fermionic spectra with specific gauge symmetries. The approach is complementary to the SB-HC4A's: Wetterich constructs automata *from* known QFTs (reverse-engineering the automaton from the field theory), while the SB-HC4A constrains the automaton class *from above* (the universality class is determined by axioms). The meeting point — automata that satisfy the SB-HC4A's Class 4 and holographic constraints and are then checked for Standard Model-like particle content — is unexplored territory.

**The Wolfram Physics Project** (Wolfram, Gorard, & Peaslee, 2020; Wolfram, 2021): The Wolfram Physics Project uses hypergraph rewriting rules — not traditional cellular automata on a fixed grid, but rules that dynamically generate spacetime itself. Two results are relevant: (1) the Einstein field equations arise generically from any computationally irreducible hypergraph evolution, given certain observer assumptions; and (2) the Feynman path integral arises in "branchial space" (the space of multiway histories) by the same mechanism that gives Einstein's equations in physical space. Both results are rule-independent — they hold for any sufficiently complex hypergraph rule. Particles are conjectured to be topological obstructions in the hypergraph, but no specific topology has been identified with any known particle, and the SM gauge group has not been derived. The SB-HC4A framework is structurally compatible: Wolfram's approach is bottom-up (pick a rule, see what emerges), while the SB-HC4A is top-down (constrain the universality class by axioms). If Wolfram's topological-obstruction particles turn out to satisfy the computational atom conditions of Section 5.6, the two programs would converge. A key structural difference: the Wolfram framework generates spacetime dynamically from hypergraph rewriting with no pre-existing lattice, whereas the SB-HC4A inherits the fixed-lattice CA tradition. More fundamentally, the Wolfram framework contains no analogue of the Bekenstein-saturation trigger that drives the SB-HC4A's cyclic cosmology, and does not propose the cross-scale singularity identity that is central to this paper's architecture.

**Levin-Wen String-Net Condensation and Quantum Graphity** (Levin & Wen, 2005; Konopka, Markopoulou, & Severini, 2008): Two related programs provide existence proofs for emergent particle physics from discrete substrates. Levin and Wen showed that starting from pure bosonic spin models on a lattice — with no fermions or gauge fields put in by hand — string-net condensed states produce emergent gauge bosons (including U(1) photon-like excitations) and emergent fermions (in 3D and higher) as collective excitations. This provides a mechanism for unifying gauge bosons and fermions from a single bosonic substrate, using the tensor category theory that the SB-HC4A formalization also employs. Quantum Graphity (Konopka et al., 2008) is a background-independent model where spacetime itself is emergent from a complete graph of N vertices. At high energy the graph is fully connected and symmetric; at low energy it undergoes a phase transition to an ordered, low-dimensional, local structure — emergent space. The high-to-low energy transition is a Big Bang analogue: the universe starts as a fully connected graph and "freezes" into spatial structure. This provides a concrete model for the SB-HC4A's holographically saturated initial boundary (the fully connected graph at maximum information density) decompressing into a low-dimensional observable interior — precisely the picture of the Big Bang as a singularity boundary transformation proposed in Section 5.4.

**Quantum Cellular Automata and Causal Set Theory** (Bisio, D'Ariano, & Tosini, 2015; Elze, 2014; Surya, 2019): The QCA/QFT correspondence shows that quantum walks on lattices reproduce the Dirac equation in the long-wavelength limit, and these can be promoted to multi-particle quantum cellular automata yielding the Dirac quantum field theory for free fermions. This is a concrete realization of the SB-HC4A claim that Feynman diagrams are "diagrams of computation." The central obstacle is the fermion doubling problem (Nielsen & Ninomiya, 1981): discretizing space inevitably produces unwanted extra fermion species. Separately, the causal set approach (Surya, 2019) postulates that spacetime is fundamentally a discrete partial order. It preserves local Lorentz invariance despite discreteness — a major advantage over naive lattice approaches — and is naturally compatible with the SB-HC4A's causal-structure-first philosophy. Both programs address specific technical challenges that a future concrete realization of the SB-HC4A would need to solve.

**Steinhardt-Turok Cyclic Model** (Steinhardt & Turok, 2002): Although not automaton-based, the Steinhardt-Turok cyclic model provides the target dynamics for the SB-HC4A's cyclic cosmology: an endless sequence of cosmic epochs, each beginning with a bang and ending in a crunch, with finite temperature and density at transitions. The SB-HC4A framework (Section 5.4) generalizes this to include all three endgames (heat death, crunch, Big Rip) with information conservation across the boundary, and derives the cyclicity from the information-theoretic properties of singularity boundaries rather than from brane collision dynamics.

### 11.2 Relationship to Self-Referential Computation Research

The SB-HC4A model does not require any specific theory of cognition or phenomenology to be correct. The cosmological argument (Sections 2–6) stands independently. However, the structural correspondence with self-referential computational systems suggests:

1. Self-referential computation at criticality is a universal pattern that appears at multiple scales, not a cosmic accident.
2. The emergence of self-modeling systems in a Class 4 universe is not merely possible but structurally guaranteed — any sufficiently complex Class 4 subsystem with self-referential closure will instantiate the pattern.
3. The meta-cognitive limitation (systems cannot fully represent their own substrate) is the local version of the cosmological inexpressibility problem — both arise because self-referential systems cannot fully specify themselves from within (Chalmers, 2018; Gruber, 2026a).

### 11.3 What This Is Not

This paper does not claim:

- That the universe is "conscious" in any experiential sense. The structural identity is architectural, not phenomenal. A building's blueprint is not a building.
- That cognition creates physical reality (idealism). The model is physicalist: the substrate is physical; the decompressed interior is a physical process; the correspondence is structural.
- That quantum mechanics is "explained by" cognitive processes (Penrose, Stapp). The model makes no such claim. Quantum mechanics is an emergent property of the automaton's dynamics — self-referential computation is also emergent, at a higher scale.
- That this is proven. It is an argument. It could be wrong (Section 9).

---

## 12. Conclusion

The SB-HC4A model proposes that the universe is a Class 4 holographic automaton bounded at every scale by singularity surfaces — information-impermeable, holographically saturated boundaries — where the observable interior is a decompressed projection of the boundary-encoded information, and the system is self-referentially closed: it computes its own structure. The substrate dynamics are reversible; the arrow of time is an emergent, interior-perspective property (Section 8.4).

The singularity boundaries are not merely spatial but temporal. The Big Bang and any future Big Crunch are information boundaries of the same kind as event horizons — impermeable to information exchange from within the computational domain, though, unlike event horizons, they terminate world-lines at finite proper time rather than receding from every approach — a distinct mode of unreachability, and one in which nothing arrives anywhere (Section 5.3). If singularities transform rather than destroy information, heat death itself becomes a singularity transition, and the self-referential closure Φ(U) = U extends from spatial self-encoding to temporal self-renewal: the universe computes its own restart. Three cosmological endgames — heat death, Big Crunch, and Big Rip — all leave a holographically saturated boundary, and, conditional on the saturation-instability conjecture of Section 5.4, all trigger renewal: as a single successor (heat death, Big Crunch) or as a branching tree of daughter universes (Big Rip). The resulting cyclic cosmology — potentially alternating CPT signatures across cycles — connects to and extends Penrose's Conformal Cyclic Cosmology, Boyle and Turok's CPT-symmetric universe proposal, and Caldwell's phantom energy analysis.

This architecture structurally corresponds to (and is conjectured to share the computational class of) the architecture of self-referential computational systems: a self-referential computation at criticality, bounded by an information-opaque boundary, with the decompressed interior as the represented world and the substrate as the informationally inaccessible foundation.

The model rests on five axioms (ontological necessity, computational character, criticality selection, information bounds, holographic encoding), proceeds by conditional elimination (given a deterministic substrate, Class 4 is selected by elimination), and yields a self-consistent architecture whose axioms are each necessary for the conclusion — though they do not determine the model uniquely (Section 10.2). The computational-atom picture now has mathematical backing: Wetterich (2022a, 2022b, 2022c) has proven that *large classes* of reversible cellular automata are exactly equivalent to fermionic quantum field theories with gauge symmetries, including a 4D spinor gravity model with exact local Lorentz symmetry. This, combined with emergent GR and QM from hypergraph rewriting (Wolfram, 2021), emergent gauge bosons and fermions from string-net condensation (Levin & Wen, 2005), emergent spacetime from graph phase transitions (Konopka et al., 2008), and an estimation-theoretic reading of entanglement as the non-separable description of a shared substrate (Section 6.5), places the SB-HC4A within a converging landscape of research programs — each addressing different aspects of the same fundamental question. Seven specific weak points have been identified, the deepest being the cognitive ceiling problem: we may find this symmetry because our Class 4 brains are constitutionally incapable of seeing anything else.

Whether the SB-HC4A is a description of the universe or a description of the limits of human cognition is, I believe, the most important open question in the philosophy of science. The model predicts that this question cannot be answered from within — and that prediction is either the model's deepest confirmation or its deepest flaw.

---

## References

Afik, Y., & de Nova, J. R. M. (2022). Quantum information with top quarks in QCD. *Quantum*, 6, 820. arXiv:2203.05582.

Albert, D. Z. (2000). *Time and Chance*. Harvard University Press.

Albert, D. Z. (2012). On the origin of everything. *The New York Times*. [Review of Krauss, 2012.]

Algom, I., & Shriki, O. (2026). The ConCrit framework: Critical brain dynamics as a unifying mechanistic framework for theories of consciousness. *Neuroscience & Biobehavioral Reviews*, 180, 106483.

Almheiri, A., Dong, X., & Harlow, D. (2015). Bulk locality and quantum error correction in AdS/CFT. *Journal of High Energy Physics*, 2015(4), 163.

Almheiri, A., Hartman, T., Maldacena, J., Shaghoulian, E., & Tajdini, A. (2021). The entropy of Hawking radiation. *Reviews of Modern Physics*, 93(3), 035002.

Almheiri, A., Marolf, D., Polchinski, J., & Sully, J. (2013). Black holes: complementarity or firewalls? *Journal of High Energy Physics*, 2013(2), 62.

Arcos, H. I., & Pereira, J. G. (2004). Kerr-Newman solution as a Dirac particle. *General Relativity and Gravitation*, 36, 2441.

ATLAS Collaboration. (2024). Observation of quantum entanglement with top quarks at the ATLAS detector. *Nature*, 633, 542–547.

Bahiru, E., Belin, A., Papadodimas, K., Sárosi, G., & Vardian, N. (2024). Holography and localization of information in quantum gravity. *Journal of High Energy Physics*, 2024(5), 261.

Bak, P. (1996). *How Nature Works: The Science of Self-Organized Criticality*. Springer.

Bak, P., Tang, C., & Wiesenfeld, K. (1987). Self-organized criticality: An explanation of the 1/f noise. *Physical Review Letters*, 59(4), 381–384.

Beggs, J. M., & Plenz, D. (2003). Neuronal avalanches in neocortical circuits. *Journal of Neuroscience*, 23(35), 11167–11177.

Bekenstein, J. D. (1973). Black holes and entropy. *Physical Review D*, 7(8), 2333–2346.

Bekenstein, J. D. (1981). Universal upper bound on the entropy-to-energy ratio for bounded systems. *Physical Review D*, 23(2), 287–298.

Belinskii, V. A., Khalatnikov, I. M., & Lifshitz, E. M. (1970). Oscillatory approach to a singular point in the relativistic cosmology. *Advances in Physics*, 19(80), 525–573.

Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics Physique Fizika*, 1(3), 195–200.

Bennett, C. H. (1973). Logical reversibility of computation. *IBM Journal of Research and Development*, 17(6), 525–532.

Berut, A., Arakelyan, A., Petrosyan, A., Ciliberto, S., Dillenschneider, R., & Lutz, E. (2012). Experimental verification of Landauer's principle linking information and thermodynamics. *Nature*, 483, 187–189.

Bisio, A., D'Ariano, G. M., & Tosini, A. (2015). Quantum field as a quantum cellular automaton: The Dirac free evolution in one dimension. *Annals of Physics*, 354, 244–264.

Black, M. (1952). The identity of indiscernibles. *Mind*, 61(242), 153–164.

Bohm, D. (1952). A suggested interpretation of the quantum theory in terms of "hidden" variables. I. *Physical Review*, 85(2), 166–179.

Borde, A., Guth, A. H., & Vilenkin, A. (2003). Inflationary spacetimes are incomplete in past directions. *Physical Review Letters*, 90(15), 151301.

Bousso, R. (1999). A covariant entropy conjecture. *Journal of High Energy Physics*, 1999(07), 004.

Bousso, R. (2002). The holographic principle. *Reviews of Modern Physics*, 74(3), 825–874.

Boyle, L., Finn, K., & Turok, N. (2018). CPT-symmetric universe. *Physical Review Letters*, 121(25), 251301.

Boyle, L., Finn, K., & Turok, N. (2022). The Big Bang, CPT, and neutrino dark matter. *Annals of Physics*, 438, 168767.

Boyle, L., & Turok, N. (2024). Thermodynamic solution of the homogeneity, isotropy and flatness puzzles (and a clue to the cosmological constant). *Physics Letters B*, 849, 138442.

Brown, A. R., Roberts, D. A., Susskind, L., Swingle, B., & Zhao, Y. (2016). Complexity, action, and black holes. *Physical Review D*, 93(8), 086006.

Brown, L. D. (1971). Admissible estimators, recurrent diffusions, and insoluble boundary value problems. *Annals of Mathematical Statistics*, 42(3), 855–903.

Burinskii, A. (1998). Kerr spinning particle, strings, and superparticle models. *Physical Review D*, 57, 2392.

Burinskii, A. (2008). Dirac-Kerr-Newman electron. *Gravitation and Cosmology*, 14, 109.

Caldwell, R. R. (2002). A phantom menace? Cosmological consequences of a dark energy component with super-negative equation of state. *Physics Letters B*, 545(1-2), 23–29.

Caldwell, R. R., Kamionkowski, M., & Weinberg, N. N. (2003). Phantom energy: Dark energy with w < −1 causes a cosmic doomsday. *Physical Review Letters*, 91(7), 071301.

Carter, B. (1968). Global structure of the Kerr family of gravitational fields. *Physical Review*, 174, 1559.

Carter, B. (1971). Axisymmetric black hole has only two degrees of freedom. *Physical Review Letters*, 26(6), 331–333.

Casini, H. (2008). Relative entropy and the Bekenstein bound. *Classical and Quantum Gravity*, 25(20), 205021.

Chaitin, G. J. (1966). On the length of programs for computing finite binary sequences. *Journal of the ACM*, 13(4), 547–569.

Chalmers, D. J. (2018). The meta-problem of consciousness. *Journal of Consciousness Studies*, 25(9-10), 6–61.

Cirel'son, B. S. (1980). Quantum generalizations of Bell's inequality. *Letters in Mathematical Physics*, 4(2), 93–100.

Clauser, J. F., Horne, M. A., Shimony, A., & Holt, R. A. (1969). Proposed experiment to test local hidden-variable theories. *Physical Review Letters*, 23(15), 880–884.

CMS Collaboration. (2024). Observation of quantum entanglement in top quark pair production in pp collisions at √s = 13 TeV. *Reports on Progress in Physics*, 87, 117801.

Cook, M. (2004). Universality in elementary cellular automata. *Complex Systems*, 15(1), 1–40.

Culik, K., II, & Yu, S. (1988). Undecidability of CA classification schemes. *Complex Systems*, 2(2), 177–190.

DESI Collaboration. (2025). DESI DR2 results II: Measurements of baryon acoustic oscillations and cosmological constraints. *Physical Review D*, 112(8), 083515. arXiv:2503.14738.

Deutsch, D., & Marletto, C. (2015). Constructor theory of information. *Proceedings of the Royal Society A*, 471(2174), 20140540.

Dong, X., Harlow, D., & Wall, A. C. (2016). Reconstruction of bulk operators within the entanglement wedge in gauge-gravity duality. *Physical Review Letters*, 117(2), 021601.

Easson, D. A., & Brandenberger, R. H. (2001). Universe generation from black hole interiors. *Journal of High Energy Physics*, 2001(06), 024. arXiv:hep-th/0103019.

Egan, C. A., & Lineweaver, C. H. (2010). A larger estimate of the entropy of the universe. *The Astrophysical Journal*, 710(2), 1825–1834.

Einstein, A. (1905). Zur Elektrodynamik bewegter Körper. *Annalen der Physik*, 322(10), 891–921.

Elze, H.-T. (2014). Action principle for cellular automata and the linearity of quantum mechanics. *Physical Review A*, 89(1), 012111.

Elze, H.-T. (2022). Are quantum-classical hybrids compatible with ontological cellular automata? *Universe*, 8(4), 207.

Elze, H.-T. (2024). Cellular automaton ontology, bits, qubits and the Dirac equation. *International Journal of Quantum Information*, 22, 2450013. arXiv:2401.08253.

Ferrie, C., & Blume-Kohout, R. (2018). Maximum likelihood quantum state tomography is inadmissible. arXiv:1808.01072.

Fredkin, E. (2003). An introduction to digital philosophy. *International Journal of Theoretical Physics*, 42(2), 189–247.

Garay, L. J. (1995). Quantum gravity and minimum length. *International Journal of Modern Physics A*, 10(2), 145–165.

Geroch, R., Kronheimer, E. H., & Penrose, R. (1972). Ideal points in space-time. *Proceedings of the Royal Society of London A*, 327(1571), 545–567.

Gibbons, G. W., & Hawking, S. W. (1977). Cosmological event horizons, thermodynamics, and particle creation. *Physical Review D*, 15(10), 2738–2751.

Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. *Monatshefte für Mathematik und Physik*, 38, 173–198.

Gruber, B. J. (1968). On locally isomorphic groups and Cartan-Stiefel diagrams. In A. Ramakrishnan (Ed.), *Symposia on Theoretical Physics and Mathematics* (pp. 1–25). Springer.

Gruber, B. J. (1980). Symmetries in science. In *Symmetries in Science* (pp. 1–18). Springer.

Gruber, M. (2015). *Die Emergenz des Bewusstseins*. Self-published. 2016 corrected reprint: new cover, typographical corrections; ISBN 9781326652074.

Gruber, M. (2026a). The Four-Model Theory of Consciousness: A simulation-based framework unifying the Hard Problem, binding, and altered states. *Zenodo* preprint. https://doi.org/10.5281/zenodo.18669891

Gruber, M. (2026b). Toward a mathematical formalization of the Four-Model Theory: A recommended approach. *Zenodo* preprint. https://doi.org/10.5281/zenodo.21843693

Gruber, M. (2026c). Scale-dependent multifractal structure in the Planck 2018 CMB: Evidence from needlet-based detrended fluctuation analysis. *Zenodo* preprint. https://doi.org/10.5281/zenodo.20306785

Gutenberg, B., & Richter, C. F. (1956). Magnitude and energy of earthquakes. *Annali di Geofisica*, 9, 1–15.

Guth, A. H. (2007). Eternal inflation and its implications. *Journal of Physics A: Mathematical and Theoretical*, 40(25), 6811–6826.

Harlow, D., & Ooguri, H. (2021). Symmetries in quantum field theory and quantum gravity. *Communications in Mathematical Physics*, 383(3), 1669–1804.

Hawking, S. W. (1972). Black holes in general relativity. *Communications in Mathematical Physics*, 25(2), 152–166.

Hawking, S. W. (1975). Particle creation by black holes. *Communications in Mathematical Physics*, 43, 199–220.

Hawking, S. W., & Penrose, R. (1970). The singularities of gravitational collapse and cosmology. *Proceedings of the Royal Society of London A*, 314(1519), 529–548.

Hengen, K. B., Torrado Pacheco, A., McGregor, J. N., Van Hooser, S. D., & Turrigiano, G. G. (2016). Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. *Cell*, 165(1), 180–191.

Hossenfelder, S. (2013). Minimal length scale scenarios for quantum gravity. *Living Reviews in Relativity*, 16, 2.

Israel, W. (1967). Event horizons in static vacuum space-times. *Physical Review*, 164, 1776.

Israel, W. (1968). Event horizons in static electrovac space-times. *Communications in Mathematical Physics*, 8, 245.

Jain, P., Gachechiladze, M., & Miklin, N. (2024). Information causality as a tool for bounding the set of quantum correlations. *Physical Review Letters*, 133(16), 160201.

James, W., & Stein, C. (1961). Estimation with quadratic loss. *Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability*, 1, 361–379.

Jow, D. L., & Scott, D. (2020). Re-evaluating evidence for Hawking points in the CMB. *Journal of Cosmology and Astroparticle Physics*, 2020(03), 021. arXiv:1909.09672.

Klinkhamer, F. R., & Manton, N. S. (1984). A saddle-point solution in the Weinberg-Salam theory. *Physical Review D*, 30(10), 2212–2220.

Kolmogorov, A. N. (1965). Three approaches to the quantitative definition of information. *Problems of Information Transmission*, 1(1), 1–7.

Konopka, T., Markopoulou, F., & Severini, S. (2008). Quantum graphity: A model of emergent locality. *Physical Review D*, 77(10), 104029.

Krauss, L. M. (2012). *A Universe from Nothing*. Free Press.

Kudler-Flam, J., Leutheusser, S., Rahman, A. A., Satishchandran, G., & Speranza, A. J. (2025). Covariant regulator for entanglement entropy: Proofs of the Bekenstein bound and the quantum null energy condition. *Physical Review D*, 111(10), 105001.

Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development*, 5(3), 183–191.

Lashley, K. S. (1950). In search of the engram. *Symposia of the Society for Experimental Biology*, 4, 454–482.

Leibniz, G. W. (1686). *Discourse on Metaphysics*.

Levin, M. A., & Wen, X.-G. (2005). String-net condensation: A physical mechanism for topological phases. *Physical Review B*, 71(4), 045110.

Longo, R. (2024). A Bekenstein-type bound in QFT. arXiv:2409.14408.

Lüders, G. (1957). Proof of the TCP theorem. *Annals of Physics*, 2(1), 1–15.

Ma, Z., Turrigiano, G. G., Wessel, R., & Hengen, K. B. (2019). Cortical circuit dynamics are homeostatically tuned to criticality in vivo. *Neuron*, 104(4), 655–664.

Maldacena, J. (1998). The large-N limit of superconformal field theories and supergravity. *Advances in Theoretical and Mathematical Physics*, 2(2), 231–252.

Maldacena, J., & Susskind, L. (2013). Cool horizons for entangled black holes. *Fortschritte der Physik*, 61(9), 781–811.

McCormack, A., & Hoff, P. D. (2022). The Stein effect for Fréchet means. *Annals of Statistics*, 50(6), 3647–3676. https://doi.org/10.1214/22-AOS2245

Metzinger, T. (2003). *Being No One: The Self-Model Theory of Subjectivity*. MIT Press.

Misner, C. W. (1969). Mixmaster universe. *Physical Review Letters*, 22(20), 1071–1074.

Navascués, M., Guryanova, Y., Hoban, M. J., & Acín, A. (2015). Almost quantum correlations. *Nature Communications*, 6, 6288.

Nielsen, H. B., & Ninomiya, M. (1981). Absence of neutrinos on a lattice: (I). Proof by homotopy theory. *Nuclear Physics B*, 185(1), 20–40.

Oughton, N., & Timpson, C. G. (2024). Bounding quantum correlations: The role of the Shannon information in the information causality principle. *Entropy*, 26(7), 562.

Pastawski, F., Yoshida, B., Harlow, D., & Preskill, J. (2015). Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence. *Journal of High Energy Physics*, 2015(6), 149.

Pauli, W. (1955). Exclusion principle, Lorentz group and reflection of space-time and charge. In W. Pauli, L. Rosenfeld, & V. Weisskopf (Eds.), *Niels Bohr and the Development of Physics* (pp. 30–51). Pergamon Press.

Pawłowski, M., Paterek, T., Kaszlikowski, D., Scarani, V., Winter, A., & Żukowski, M. (2009). Information causality as a physical principle. *Nature*, 461(7267), 1101–1104.

Penington, G. (2020). Entanglement wedge reconstruction and the information problem. *Journal of High Energy Physics*, 2020, 2.

Penrose, R. (1971). Angular momentum: An approach to combinatorial space-time. In T. Bastin (Ed.), *Quantum Theory and Beyond* (pp. 151–180). Cambridge University Press.

Penrose, R. (2010). *Cycles of Time: An Extraordinary New View of the Universe*. Bodley Head.

Perlmutter, S., et al. (1999). Measurements of Ω and Λ from 42 high-redshift supernovae. *The Astrophysical Journal*, 517(2), 565–586.

Planck, M. (1899). Über irreversible Strahlungsvorgänge. *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften zu Berlin*, 5, 440–480.

Polchinski, J. (1998). *String Theory* (Vols. 1–2). Cambridge University Press.

Popescu, S., & Rohrlich, D. (1994). Quantum nonlocality as an axiom. *Foundations of Physics*, 24(3), 379–385.

Poplawski, N. J. (2010). Cosmology with torsion: An alternative to cosmic inflation. *Physics Letters B*, 694(3), 181–185.

Pribram, K. H. (1971). *Languages of the Brain*. Prentice-Hall.

Raju, S. (2022). Lessons from the information paradox. *Physics Reports*, 943, 1–80.

Riess, A. G., et al. (1998). Observational evidence from supernovae for an accelerating universe and a cosmological constant. *The Astronomical Journal*, 116(3), 1009–1038.

Robinson, D. C. (1975). Uniqueness of the Kerr black hole. *Physical Review Letters*, 34(14), 905–906.

Rovelli, C. (2004). *Quantum Gravity*. Cambridge University Press.

Rovelli, C., & Smolin, L. (1995). Discreteness of area and volume in quantum gravity. *Nuclear Physics B*, 442, 593.

Rowland, E. S. (2006). Local nested structure in rule 30. *Complex Systems*, 16(3), 239–258. https://doi.org/10.25088/ComplexSystems.16.3.239

Ruggiero, R. (2020). Big Rip: Heating by Hawking radiation and a possible connection to conformal cyclic cosmology. arXiv:2005.12684.

Salmon, W., Strelchuk, S., & Arvidsson-Shukur, D. R. M. (2024). James-Stein estimation in quantum Gaussian sensing. arXiv:2404.02203.

Shew, W. L., & Plenz, D. (2013). The functional benefits of criticality in the cortex. *The Neuroscientist*, 19(1), 88–100.

Smolin, L. (1992). Did the universe evolve? *Classical and Quantum Gravity*, 9, 173.

Stein, C. (1956). Inadmissibility of the usual estimator for the mean of a multivariate normal distribution. *Proceedings of the Third Berkeley Symposium on Mathematical Statistics and Probability*, 1, 197–206.

Steinhardt, P. J., & Turok, N. (2002). A cyclic model of the universe. *Science*, 296(5572), 1436–1439.

Surya, S. (2019). The causal set approach to quantum gravity. *Living Reviews in Relativity*, 22, 5.

Susskind, L. (1995). The world as a hologram. *Journal of Mathematical Physics*, 36(11), 6377–6396.

Susskind, L., Thorlacius, L., & Uglum, J. (1993). The stretched horizon and black hole complementarity. *Physical Review D*, 48(8), 3743–3761.

Tegmark, M. (2008). The Mathematical Universe. *Foundations of Physics*, 38(2), 101–150.

't Hooft, G. (1985). On the quantum structure of a black hole. *Nuclear Physics B*, 256, 727–745.

't Hooft, G. (1993). Dimensional reduction in quantum gravity. In *Salamfestschrift* (pp. 284–296). World Scientific.

't Hooft, G. (2016). *The Cellular Automaton Interpretation of Quantum Mechanics*. Springer.

Toffoli, T., & Margolus, N. (1987). *Cellular Automata Machines: A New Environment for Modeling*. MIT Press.

Tolman, R. C. (1934). *Relativity, Thermodynamics and Cosmology*. Oxford: Clarendon Press.

Tsang, M. (2020). Physics-inspired forms of the Bayesian Cramér-Rao bound. *Physical Review A*, 102(6), 062217.

Uggla, C., van Elst, H., Wainwright, J., & Ellis, G. F. R. (2003). Past attractor in inhomogeneous cosmology. *Physical Review D*, 68(10), 103502.

Van Raamsdonk, M. (2010). Building up spacetime with quantum entanglement. *General Relativity and Gravitation*, 42, 2323–2329.

Vopson, M. M. (2025). Is gravity evidence of a computational universe? *AIP Advances*, 15(4), 045035.

Wetterich, C. (2022a). Fermion picture for cellular automata. *arXiv preprint*, arXiv:2203.14081.

Wetterich, C. (2022b). Fermionic quantum field theories as probabilistic cellular automata. *Physical Review D*, 105(7), 074502.

Wetterich, C. (2022c). Cellular automaton for spinor gravity in four dimensions. *arXiv preprint*, arXiv:2211.09002.

Wheeler, J. A. (1957). On the nature of quantum geometrodynamics. *Annals of Physics*, 2(6), 604–614.

Wheeler, J. A. (1990). Information, physics, quantum: The search for links. In *Complexity, Entropy, and the Physics of Information* (pp. 3–28). Addison-Wesley.

Wilson, K. G. (1971). Renormalization group and critical phenomena. I. *Physical Review B*, 4(9), 3174–3183.

Wolfram, S. (2002). *A New Kind of Science*. Wolfram Media.

Wolfram, S. (2021). The Wolfram Physics Project: A one-year update. *Stephen Wolfram Writings*.

Wolfram, S., Gorard, J., & Peaslee, M. (2020). A class of models with the potential to represent fundamental physics. *Complex Systems*, 29(2), 107–536. arXiv:2004.08210.

Zuse, K. (1969). *Rechnender Raum*. Friedrich Vieweg & Sohn.
