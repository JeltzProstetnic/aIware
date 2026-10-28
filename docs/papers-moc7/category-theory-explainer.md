# Why category theory for FMT? An honest explainer

*For MG, after the MoC7 question from a machine-learning computer scientist: "Why formalise FMT with category theory when the brain is a continuous physical thing?" Written 2026-10-16. Sources: `paper/fmt_formal/fmt-formalization.md` (the roadmap, cited below as "roadmap §x"), `paper/full/four-model-theory-full.md` §9, `docs/moc7-field-guide.md`, `docs/fable-fmt-formal-extraction-S245.md`, `docs/aiw269-lit-formal.md`, `docs/aiw94-two-dials-formalization.md`, `paper/rim_formal/rim-formalization.md`, `docs/moc7/booklet.txt`. External references were checked against Crossref, arXiv and publisher pages on 2026-10-16. Status notes are in the reference list.*

**Verdict in one sentence.** Category theory is a sound choice of *language* for one thing FMT needs, which is to say exactly when a fast, virtual level of description "closes" over a substrate and when part of that level models the system that produces it. It is the wrong choice of *primary tool*: the predictions FMT can actually test come from stochastic dynamics and information theory, and today the categorical part of the roadmap is four short subsections of definitions with no theorem in them.

---

## 0. The short answer to the questioner

The questioner's premise is that category theory is a mathematics of discrete things, so it cannot fit a continuous organ. That premise is wrong twice over.

1. **Category theory does not care whether things are discrete.** Smooth manifolds, measurable spaces, metric spaces and Markov kernels all form categories. Continuous-time dynamical systems compose categorically. The machine-learning community already uses the idea, with backpropagation described as a functor, equivariant networks and categorical deep learning (§3).
2. **FMT's relevant level is not the substrate anyway.** The theory places phenomenality on a virtual, computational level. Whether the substrate is continuous, discrete or hybrid is a question about the *domain* of a map. The theory's claim is about the map, and about what is true on its *codomain*.

The honest add-on: what we have is a specification. Nothing has been proven yet.

---

## 1. What the formalisation actually is right now

### 1.1 The roadmap as a whole: six modules, and category theory is one of them

The roadmap (Gruber, 2026b, *Toward a Mathematical Formalization of the Four-Model Theory: A Recommended Approach*) is mostly **not** category theory. Its abstract lists six modules:

| Module (roadmap §) | Mathematics used | Status |
|---|---|---|
| Continuous model space, §2 | A density ρ(s, ν, t) over scope × mode, with a threshold ν_crit for the virtual/real split | Defined. Not estimated from any data |
| Permeability, §3 | Transfer entropy T_{A_s→B_s}, a gating family g_c, and a density PDE (called "Fokker-Planck"; the S245 review notes it is really reaction–advection–diffusion) | Defined. The signed-predictions table is the most testable part. Phase 1 |
| Criticality, §4 | σ, λ_max, DFA α, Fisher information; the two dials E = P∞ (percolation) and K = on-cluster LZ | Signature hypothesis. Lemmas L1 and L2 explicitly **open** |
| ESM redirection, §5 | An input-dependent attractor, with mutual information I(e; i_self) vs I(e; i_ext) | Defined, with predictions |
| Self-referential closure, §6 | O_ESM ⊆ S_EWM; recursion depth μ_n; self-prediction R; a fixed point Ψ(m*) = m*; an RG-fixed-point analogy | Proposed. Phase 3, "hardest" |
| **Category-theoretic architecture, §7** | Two categories Sub and Sim, a functor F, a natural transformation η, a coproduct | **Proposed only.** Phase 2 |

The roadmap's own scope statement (§1.3) governs everything here: *"It does not verify the mathematical apparatus — the author is not a mathematician … The equations presented here are intended as precise specifications of what needs to be formalized … not as proven theorems."*

### 1.2 The categorical part, construct by construct

| FMT construct | Categorical object in roadmap §7 | Done or proposed |
|---|---|---|
| Substrate (real side): W, x(t) | Category **Sub**: objects are substrate states; morphisms are physical state transitions | Stated in one sentence. No construction or example |
| Virtual models (EWM, ESM, the part of ρ above ν_crit) | Category **Sim**: objects are virtual-model states; morphisms are "experiential transitions" | Stated in one sentence |
| Real/virtual split; "consciousness" | Functor **F: Sub → Sim** that preserves composition | Asserted ("Consciousness is a functor"). No proof that F exists for any system |
| Variable permeability | Natural transformation **η: F_normal ⇒ F_altered** | Asserted, with a link to Smithe's (2024) structured active inference |
| Forking of the self-model (DID) | **Coproduct** ESM_1 ⊔ … ⊔ ESM_n in Sim | Asserted. The S245 Fable review judged this "decoration" |
| Self-referential closure | Ψ(m*) = m*, related to Lawvere's fixed-point theorem. This is in §6.4, **not** in §7 | Proposed. Phase 3 |

Phase 2 of the build order (§8) moved Module 7 up from Phase 3. The roadmap's argument is that emergence in physics is formalised categorically (Levin–Wen string-nets use tensor categories; Wetterich's automaton–QFT equivalences are functorial), so the categorical frame "should inform the construction of Modules 2 and 5, not be retrofitted". It recommends collaborating with a category theorist (Tsuchiya, Smithe). **That is an argument from analogy, not a demonstration.**

### 1.3 What the project's own documents say about the status

- **Main paper, §9 Open Question 2:** *"The theory's computational-regime requirement is specified qualitatively, not quantitatively. A full mathematical treatment — defining the four models formally, specifying the free-modeling condition, deriving predictions as formal consequences — remains to be developed."* §7 of the same paper lists the absence of formalisation as *"The theory's primary disadvantage"*.
- **MoC7 field guide:** the booklet abstract says *"Category-theoretic formalization in development"*. The field guide sets that against *"Open question 2: no quantitative formalism yet"* and adds *"AMCS is a mathematics society; promise only what you can show."*
- **S245 Fable review (cleanliness note c):** *"§7's functor/natural-transformation apparatus does no computational work the plainer dynamical statements don't already do."* It recommended keeping category theory out of the extractable paper altogether.
- **AIW-269 literature sweep (Sep 2026):** found no category-theoretic model of consciousness that pre-empts or settles anything in §7. The closest result was Dehghani (2026, arXiv:2608.30231, not re-verified here), an algebraic result that structure exists only in a composite.
- **The RIM formalisation**, the sibling roadmap, uses no category theory at all. It is built on SDEs, stochastic bifurcation and Kramers escape, and it is the more concrete of the two documents.

**A discrepancy you should know about.** The MoC7 abstract describes a *different* construction from the roadmap: *"mapping model types as objects with natural transformations between implicit-to-explicit transitions … criteria for substrate-independent consciousness detection."* In the roadmap, the objects are *states* rather than model types, the implicit-to-explicit relation is the functor F rather than a natural transformation, and no detection criterion appears anywhere. If someone at MoC7 read the abstract and then the roadmap, they saw two different things.

### 1.4 Technical problems with §7 as written

These are worth knowing before you defend it.

1. **"Consciousness is a functor" proves too much.** Any faithful simulation, such as a weather model, has a structure-preserving map from substrate dynamics to simulated dynamics. F therefore captures FMT's *two-level ontology*, the existence of a virtual level, but not consciousness. What makes FMT a theory of consciousness is self-referential closure, and that sits in §6, not in §7. The categorical section never touches it.
2. **Functoriality is not free, and the roadmap does not say so.** A coarse-graining Π of a dynamical system (roadmap §4.1 already has Π_EWM and Π_ESM) is functorial only if the projected dynamics are self-contained, that is, Π ∘ f = g ∘ Π for some macro-dynamics g. In Markov-chain language this is lumpability (Kemeny & Snell, 1960). Most coarse-grainings fail it. **This is good news and should be said loudly:** it means F is a *substantive, testable claim*, and it is precisely FMT's second principle, that recurrent dynamics "host a second computational level". See §4, deliverable D1.
3. **Objects as states versus objects as state spaces.** If the objects of Sim are individual states, then "F(x(t)) = ESM_1 ⊔ … ⊔ ESM_n" does not parse: a functor sends one object to one object, and a coproduct of *states* is not a state. The standard choice in systems theory is the reverse: objects are *systems* (state spaces with dynamics) and morphisms are structure-preserving maps between systems. With that choice, the coproduct becomes "the virtual system decomposes into a sum of self-model regimes, and at any time the state is in exactly one summand". That *is* meaningful and does fit the one-alter-at-a-time claim. It still needs the coproduct's universal property to do some work, or it remains notation.
4. **The direction of η.** If "more substrate structure maps into the simulation" under psychedelics, then F_altered is a *finer* coarse-graining than F_normal. The canonical natural map then runs from the finer to the coarser (F_altered ⇒ F_normal), not the other way. Nor does naturality "ensure" that content arrives in hierarchical order (V1 → V2/V3 → higher). That is an empirical claim, and naturality is silent on it. A cleaner version is to give coarse-grainings a refinement order and treat permeability as movement in that order, with transfer entropy (roadmap §3) as its measure.
5. **The Hard Problem step is restated, not derived.** "Phenomenal properties exist in Sim, not in Sub" is a choice about where to put them. The functor does not force that choice. The roadmap's §9.2 concedes this in general (*"The formalization does not derive phenomenality from mathematics"*). §7.2 should say the same in place.

---

## 2. Why category theory, of all things?

Here are the real reasons, each with an honest statement of what it does and does not buy.

### 2.1 Compositionality

Category theory is the mathematics of *how things compose*. A theory with levels (substrate → implicit models → explicit models) and with parts that plug together (four model kinds, gating channels, self-model inside world-model) needs two things stated precisely: what composes with what, and which properties survive composition. Phillips and Wilson (2010) used exactly this to explain the systematicity of cognition. Fong and Spivak (2019) is the standard introduction to the applied programme.
*What it buys:* it forces each "level" to be specified as a system with an interface, so "the ESM is part of the EWM" stops being a picture.
*What it does not buy:* any number.

### 2.2 Structure-preserving maps between levels

The core of FMT is a claim about *levels*. Qualia are real at the computational level and incoherent at the substrate level, the way a spreadsheet value is incoherent at the transistor level. The natural mathematical statement of "a level" is a map from fine to coarse description that commutes with the dynamics:

```
        f (substrate dynamics)
   X ───────────────────────────▶ X
   │                              │
 Π │                              │ Π        Π = coarse-graining (roadmap §4.1)
   ▼                              ▼
   Z ───────────────────────────▶ Z
        g (virtual-level dynamics)
```

If this square commutes, at least approximately, then the virtual level is a system in its own right. You can run it without looking at X, and its properties are not properties of X. That is the categorical content of "two-level ontology". In the language of coalgebras (Rutten, 2000; Jacobs, 2017), a dynamical system is a coalgebra X → G(X), and Π is a coalgebra homomorphism. For stochastic dynamics, G is the Giry probability monad, so X can be any measurable (continuous) space.

**Bridge for the ML person.** A learned latent world model is good exactly when *encode-then-step ≈ step-then-encode*. This is the same commuting square. Bisimulation metrics in reinforcement learning (Ferns, Panangaden, & Precup, 2004; Zhang et al., 2021) measure how far an encoder is from a homomorphism, and they come directly out of coalgebraic bisimulation for *continuous-state* Markov processes (Desharnais, Edalat, & Panangaden, 2002). On this reading, FMT says the brain contains a world model *and a self model* in that sense, and that phenomenality is a property of the latent side.

### 2.3 The self-model as a model of the modelling system

This is FMT's distinctive claim, and the place where category theory has the most to offer. It is also the place where it currently offers the least that is concrete.

- **Fixed points.** Roadmap §6.4 states closure as Ψ(m*) = m*. Lawvere's (1969) fixed-point theorem is the categorical root of every diagonal argument: Cantor, Gödel, Tarski, Turing (Yanofsky, 2003). **Note that Lawvere cuts both ways.** It produces fixed points, and it also proves that a system cannot represent all of its own maps on itself. The second half fits FMT's *observability constraint* (O_ESM ⊆ S_EWM, the self-model's blind spot) better than it fits closure. That is an opportunity: the observability constraint may be derivable, rather than merely posited (D2).
- **Guarded recursion.** At MoC7, Kawakami (*Guarded Reflection*, Aud 2) argued that self-reference has unique, constructible fixed points when every self-occurrence is guarded by a one-step delay ▷ (Löb induction, modelled in the topos of trees; Birkedal et al., 2012). He also said this meets the discreteness objection "structurally (the guard is a zero-width cut)". This fits FMT unusually well. The ESM models the system's *previous* frame, which is the temporal-echo mechanism of the main paper (§3.4.4). The continuous-math version is Banach's contraction fixed point. The topos-of-trees version generalises it. This is the most promising formal home for closure.
- **Coalgebras and final coalgebras.** A system's behaviour up to observational equivalence is its image in the final coalgebra. Non-well-founded "hypersets", presented at MoC7 by Williford (Aud 2), are the final coalgebra of the powerset functor. That is a principled way to say "the self is a circular object" without paradox.
- **What this does *not* yet give:** a criterion that separates a self-model from mere recurrence. Feedback alone (a trace in a traced monoidal category; Joyal, Street, & Verity, 1996) is recurrence. Every RNN has it. The criterion has to say that the fed-back content is a *model of the loop*. See D2.

### 2.4 Comparing theories through functors

Tsuchiya, Taguchi and Saigo (2016) proposed using functors to test whether IIT's integrated-information structures correspond to the structure of experience. Kleiner and Tull (2021) recast IIT itself in categorical terms, and Kleiner (2020) and Kleiner and Ludwig (2024) frame "mathematical structure of experience" more generally. Prentner (2024) argues that category theory lets consciousness science go beyond a list of correlations. The real value for FMT is that IIT, GNW and FMT can be set in **one frame**. Each picks out a *privileged coarse-graining* of the same substrate:

- **IIT:** the grain that maximises Φ (its exclusion postulate).
- **GNW:** the grain at which ignition and broadcast occur. Fougea (MoC7, Aud 5) formalised GNW with timed automata and a *refinement* relation, which is itself an order/categorical notion.
- **FMT:** the grain whose dynamics close (D1) *and* contain a self-model (D2).

When computed on the *same* simulated substrate, these either coincide or they do not. Where they diverge, you have a discriminating experiment.

### 2.5 Yoneda: "an object is its relations"

The Yoneda lemma implies that an object is determined, up to isomorphism, by the pattern of maps into it from every other object. Tsuchiya and Saigo use this as the formal core of a *relational* account of experience: a quale is fixed by its similarity relations to all other qualia (Tsuchiya & Saigo, 2021; Northoff, Tsuchiya, & Saigo, 2019). Enriching the hom-sets with graded similarity (Tsuchiya, Phillips, & Saigo, 2022) and an adjunction between qualia and reports (Tsuchiya, Saigo, & Phillips, 2023) extend the idea. An enriched category with distances as hom-values *is* a generalised metric space (Lawvere, 1973), so this is continuous mathematics.
*FMT fit:* if qualia are properties of a computational level, they are structural and relational properties. FMT therefore sides naturally with the structural turn. The empirical handle already exists and needs no category theory to run: unsupervised Gromov–Wasserstein alignment of similarity structures across individuals (Kawakita et al., 2025). That is the field guide's "structure-vs-absolute" benchmark.
*Caveat:* Yoneda gives identity *up to isomorphism*. It eliminates the inverted-spectrum residue by construction, so it cannot be used as an argument *against* that residue.

---

## 3. The continuous-brain objection, answered properly

### 3.1 Category theory is not about discreteness

| Continuous structure | Categorical home | Reference |
|---|---|---|
| Probability and noise on continuous spaces | Category of Markov kernels; the Giry monad | Giry (1982) |
| Conditioning, sufficiency and Bayes, abstractly | Markov categories | Fritz (2020); Cho & Jacobs (2019) |
| Metric and similarity spaces | Categories enriched over [0, ∞] | Lawvere (1973) |
| Dynamical systems, continuous or not | Coalgebras | Rutten (2000); Jacobs (2017) |
| ODE systems wired together | Algebras on the operad of wiring diagrams | Vagner, Spivak, & Lerman (2015); Myers, *Categorical Systems Theory* (book draft) |
| Bisimulation of continuous-state stochastic systems | Labelled Markov processes | Desharnais, Edalat, & Panangaden (2002) |
| Bayesian inference / active inference, compositionally | Bayesian lenses, "Bayesian updates compose optically", polynomial systems | Smithe (2020, 2022, 2023, 2024); Capucci et al. (2022) |
| Gradient-based learning | Backprop as a functor; categorical deep learning | Fong, Spivak, & Tuyéras (2019); Gavranović et al. (2024); Shiebler, Gavranović, & Wilson (2021) |
| Sheaves, contextuality | Sheaf-theoretic contextuality | Abramsky & Brandenburger (2011); Prakash at MoC7 (Aud 5) |

**For the ML person specifically:** an equivariant network is a natural transformation between functors out of a group, viewed as a one-object category. Geometric deep learning (Bronstein et al., 2021) is in effect applied category theory restricted to groups. So the ML field already relies on structure-preserving maps on continuous data. Category theory is that idea with the restriction to groups removed.

### 3.2 Your premise point: the brain is not simply continuous anyway

The questioner treats the brain as a smooth continuum. At the relevant grain it is hybrid:
- Spikes are all-or-none events, and vesicle release is quantal.
- Attractor states and perceptual cycles are discrete in time.
- The roadmap itself (§4.1) calls the cortical automaton *"a discrete system on a high-dimensional lattice"*.

At the same time, the roadmap insists that the *model space* is continuous: a density ρ, *"statistical, not enumerative"* (§1.2). Mathematically, FMT is a hybrid continuous–discrete system. That is an argument *for* a framework that is agnostic between the two, which category theory is.

### 3.3 The relevant level is computational, so substrate continuity is beside the point

FMT's ontology puts phenomenality on the virtual level, and the theory is substrate-neutral (roadmap §4.1: *"any dynamical system satisfying the criticality and architectural constraints qualifies"*). Whether X is ℝ^N with an ODE, a spiking lattice, or a reservoir on a GPU, the claim is about whether a coarse-graining Π with closed dynamics on Z exists, and what Z contains. **Continuity of X is a property of the domain of Π. FMT's claims are about Π and Z.** Mason's MoC7 talk on abstraction layers and substrate independence makes the same move from the AMCS side.

### 3.4 What the questioner may really be worried about, and where they are right

The likely real worry is that category theory produces no numbers, while neuroscience runs on continuous, quantitative, statistical models. **That worry is largely correct about the roadmap.** Every measurable quantity in it (transfer entropy, σ, λ_max, P∞, LZ, mutual information, R) is non-categorical, and the RIM roadmap gets a long way with SDEs alone. Category theory's honest role is a specification and integration language, not a measurement tool.

---

## 4. What it should lead to: concrete deliverables

These are ranked by value per effort. **D1 and D2 are my proposals, not existing results.** They are what would make §7 earn its place.

**D1. Make "the virtual level exists" a measurable commuting square.** Recast Sub and Sim as stochastic systems (coalgebras for the Giry monad). Define F as an *approximate* homomorphism Π with a **closure defect** δ(Π). This measures how far "step-then-coarse-grain" differs from "coarse-grain-then-step", using a KL or Wasserstein distance, or the information-theoretic closure measures of Rosas et al. (2024) and Bertschinger et al. (2006). The real/virtual split then becomes a question with a numerical answer: *is there a low-dimensional Π with small δ?* This can be computed now on the in-silico reservoirs (Gruber, 2026d) and on fitted latent-dynamics models of neural data. Prediction: δ rises (closure breaks) under propofol and in generalised seizure, and changes but stays finite under psychedelics. **Cheapest real win; ties §4.1 to §7.**

**D2. A criterion that separates a self-model from mere recurrence, plus a derivation of the blind spot.** A system X contains a self-model E when three conditions hold:
- E is a component of X.
- There is a *lossy* approximate homomorphism h: X → E that tracks the dynamics of the parts of X *including E itself*, so E predicts its own next state and not only the world's.
- E has strictly lower capacity than X.

Mere recurrence, such as a thermostat or a generic RNN, has feedback but no such h beyond the trivial identity. The capacity condition excludes the trivial self-model E = X. A Lawvere/Cantor-type argument then suggests that a lossy self-model cannot be complete. That would turn the observability constraint O_ESM ⊆ S_EWM from a posit into a consequence. The measurable proxy is the self-prediction score R of roadmap §6.3, reported against matched ablations. *Risk:* the counting half of the argument does not need category theory.

**D3. Closure as a guarded fixed point.** Replace the free-floating Ψ(m*) = m* with a self-model update that takes the system's previous frame as input. Its unique fixed point exists by Banach's theorem (metric version) or Löb induction in the topos of trees (Birkedal et al., 2012; Kawakami at MoC7). This gives existence and uniqueness for "the self", links closure to the temporal-echo frame rate, and replaces the RG-fixed-point analogy of §6.6 as the primary target. The RG analogy can stay as a long shot. *Do not* use a trace in a traced monoidal category as the closure criterion: a trace formalises feedback, which every recurrent network has.

**D4. A theory-comparison testbed.** On one simulated substrate, compute each theory's privileged grain: IIT's max-Φ grain (Kleiner & Tull's formal IIT), GNW's ignition grain (Fougea's automata), and FMT's grain from D1 plus D2. Report where they agree and where they diverge. This is where "a functor to IIT's or GNW's formal structure" becomes a test rather than a diagram.

**D5. Permeability as movement in the refinement order of coarse-grainings,** measured by the transfer entropy of roadmap §3. This fixes the direction problem of §7.3 and connects the categorical module to the Phase-1 empirical one.

**D6. A structural (Yoneda-style) qualia test.** Run the field guide's Gromov–Wasserstein structure-vs-absolute benchmark, with the relational reading of FMT stated as a prediction: cross-subject *structure* aligns where *absolute* decoding fails.

**Housekeeping.** Downgrade or drop §7.4 (coproduct) unless the universal property is used. Fix "Consciousness is a functor" to "the virtual level is (approximately) a functor image". Reconcile the MoC7-abstract wording with the roadmap. Stop advertising a "category-theoretic formalization in development" until D1 exists.

### 4.1 Honest risks

- **Decoration.** This is the S245 verdict, and it is currently correct. A diagram that says nothing the dynamical equations do not already say is a cost to the reader and a credibility risk with mathematicians (AMCS).
- **No quantitative predictions from category theory itself.** All numbers come from the measures inside the objects and maps. The categorical layer can at best make sure that the right numbers are being compared.
- **The hard parts are statistical, not categorical.** Estimating Π, ρ and E from data, and separating real modes from decomposition artefacts (roadmap §2.6), are inference problems.
- **Dependence on collaborators.** Category theorists who know consciousness science are few (Tsuchiya/Saigo/Phillips, Kleiner/Tull, Smithe, Signorelli/Coecke). Without one, §7 will stay a sketch.
- **Audience cost.** Neuroscientists find it opaque, and mathematicians will check it. Overpromising to either costs more than saying nothing.
- **Better tools for several parts:**
  - Stochastic dynamical systems and bifurcation theory for ESM redirection (§5) and ignition (as RIM shows).
  - Information theory for permeability and closure (transfer entropy; Rosas et al., 2020, 2024; information closure in Chang et al., 2020; causal emergence in Hoel et al., 2013).
  - Information geometry for criticality and qualia geometry (Amari, 2016; Oizumi et al. 2025, already in the roadmap).
  - Percolation and statistical mechanics for the two dials.
  - Probabilistic graphical models and state-space models for estimation (Koller & Friedman, 2009). Markov categories host these, but you do not need the host in order to fit them.

### 4.2 Frank recommendation

**Category theory should not be FMT's primary formal tool.** The primary tools should be **stochastic dynamical systems plus information theory**. That is where the roadmap's testable content already lives (§3–§5, the two dials), and it is the language the ML questioner, neuroscientists and the RIM roadmap share.

Keep category theory in a **small, load-bearing role**: the commuting-square definition of a virtual level (D1), the self-model criterion and the blind-spot derivation (D2), and the guarded-fixed-point account of closure (D3). Those three are the only places where it states something the dynamics alone do not. If D1 and D2 cannot be made to yield a theorem or a computed δ within one collaboration cycle, demote §7 to an appendix.

Publicly, describe it as *"a categorical specification of the two-level architecture, with the measurable modules first"*, never as *"a category-theoretic formalization in development."*

---

## 5. Answer card (~150 words, ready to send)

> Thanks for the sharp question. Two answers.
>
> First, category theory isn't about discreteness. Smooth manifolds, measurable spaces and Markov kernels all form categories, and continuous dynamical systems compose categorically. ML already uses this: equivariant networks are structure-preserving maps, and backprop has been described as a functor. A learned world model is good exactly when "encode, then step" equals "step, then encode". That commuting square is the core of our formalisation. FMT claims that brain dynamics admit a coarse-graining whose dynamics close on themselves (the "virtual" level), and that part of that level models the very system producing it. Whether the substrate is continuous or spiking only affects the domain of that map.
>
> Second, honestly: the categorical part is a specification, not yet a result. The quantitative work (transfer entropy, criticality, attractor dynamics) is ordinary stochastic dynamics and information theory, and that comes first.

---

## References

Status key: **[V]** = checked on 2026-10-16 against Crossref, arXiv, a publisher page or DBLP. **[V-roadmap]** = taken from the roadmap's own reference list, which went through the project's reference gate. **[MoC7]** = MoC7 booklet abstract, `docs/moc7/booklet.txt`. **UNVERIFIED** = not checked.

- Abramsky, S., & Brandenburger, A. (2011). The sheaf-theoretic structure of non-locality and contextuality. *New Journal of Physics*, 13(11), 113036. https://doi.org/10.1088/1367-2630/13/11/113036 [V]
- Amari, S. (2016). *Information geometry and its applications*. Springer Japan. https://doi.org/10.1007/978-4-431-55978-8 [V]
- Bertschinger, N., Olbrich, E., Ay, N., & Jost, J. (2006). Information and closure in systems theory. In *Explorations in the Complexity of Possible Life* (pp. 9–19 or 9–21; sources disagree). IOS Press. [V: authors, year, title; pages and publisher UNVERIFIED]
- Birkedal, L., Møgelberg, R. E., Schwinghammer, J., & Støvring, K. (2012). First steps in synthetic guarded domain theory: Step-indexing in the topos of trees. *Logical Methods in Computer Science*, 8(4:1). https://doi.org/10.2168/LMCS-8(4:1)2012 [V]
- Bronstein, M. M., Bruna, J., Cohen, T., & Veličković, P. (2021). Geometric deep learning: Grids, groups, graphs, geodesics, and gauges. arXiv:2104.13478 [V]
- Capucci, M., Gavranović, B., Hedges, J., & Rischel, E. F. (2022). Towards foundations of categorical cybernetics. *EPTCS*, 372, 235–248. https://doi.org/10.4204/EPTCS.372.17 [V]
- Chang, A. Y. C., Biehl, M., Yu, Y., & Kanai, R. (2020). Information closure theory of consciousness. *Frontiers in Psychology*, 11, 1504. https://doi.org/10.3389/fpsyg.2020.01504 [V]
- Cho, K., & Jacobs, B. (2019). Disintegration and Bayesian inversion via string diagrams. *Mathematical Structures in Computer Science*, 29(7), 938–971. https://doi.org/10.1017/S0960129518000488 [V]
- Dehghani, N. (2026). "More is different" in neural circuits: Algebraic emergence of effective theories in canonical recurrent motifs. arXiv:2608.30231 [taken from `docs/aiw269-lit-formal.md`, where it was checked 2026-09-28; not re-checked]
- Desharnais, J., Edalat, A., & Panangaden, P. (2002). Bisimulation for labelled Markov processes. *Information and Computation*, 179(2), 163–193. https://doi.org/10.1006/inco.2001.2962 [V]
- Ferns, N., Panangaden, P., & Precup, D. (2004). Metrics for finite Markov decision processes. *Proceedings of UAI 2004*, 162–169. arXiv:1207.4114 [V]
- Fong, B., & Spivak, D. I. (2019). *An invitation to applied category theory: Seven sketches in compositionality*. Cambridge University Press. https://doi.org/10.1017/9781108668804 [V]
- Fong, B., Spivak, D. I., & Tuyéras, R. (2019). Backprop as functor: A compositional perspective on supervised learning. *LICS 2019*. arXiv:1711.10455 [V]
- Fougea, G. (2026). A computational framework for the global neuronal workspace hypothesis. MoC7 talk, Aud 5. [MoC7]
- Fritz, T. (2020). A synthetic approach to Markov kernels, conditional independence and theorems on sufficient statistics. *Advances in Mathematics*, 370, 107239. https://doi.org/10.1016/j.aim.2020.107239 [V]
- Gavranović, B., Lessard, P., Dudzik, A. J., von Glehn, T., Araújo, J. G. M., & Veličković, P. (2024). Position: Categorical deep learning is an algebraic theory of all architectures. *Proceedings of ICML 2024*, PMLR 235, 15209–15241. arXiv:2402.15332 [V]
- Giry, M. (1982). A categorical approach to probability theory. In *Categorical Aspects of Topology and Analysis* (Lecture Notes in Mathematics 915, pp. 68–85). Springer. https://doi.org/10.1007/BFb0092872 [V]
- Gruber, M. (2026b). Toward a mathematical formalization of the Four-Model Theory: A recommended approach. *Zenodo*. https://doi.org/10.5281/zenodo.21843693 [own work]
- Gruber, M. (2026d). In-silico tests of the four-model architecture. *Zenodo*. https://doi.org/10.5281/zenodo.21610993 [own work]
- Hoel, E. P., Albantakis, L., & Tononi, G. (2013). Quantifying causal emergence shows that macro can beat micro. *PNAS*, 110(49), 19790–19795. https://doi.org/10.1073/pnas.1314922110 [V]
- Jacobs, B. (2017). *Introduction to coalgebra: Towards mathematics of states and observation*. Cambridge University Press. https://doi.org/10.1017/9781316823187 [V]
- Joyal, A., Street, R., & Verity, D. (1996). Traced monoidal categories. *Mathematical Proceedings of the Cambridge Philosophical Society*, 119(3), 447–468. https://doi.org/10.1017/S0305004100074338 [V]
- Kawakami, W. (2026). Guarded reflection: How retention dissolves the regress problem of self-consciousness. MoC7 talk, Aud 2. [MoC7]
- Kawakita, G., Zeleznikow-Johnston, A., Takeda, K., Tsuchiya, N., & Oizumi, M. (2025). Is my "red" your "red"? *iScience*, 28(3), 112029. https://doi.org/10.1016/j.isci.2025.112029 [V]
- Kemeny, J. G., & Snell, J. L. (1960). *Finite Markov chains*. Van Nostrand. [UNVERIFIED — standard text, not web-checked]
- Kleiner, J. (2020). Mathematical models of consciousness. *Entropy*, 22(6), 609. https://doi.org/10.3390/e22060609 [V]
- Kleiner, J., & Ludwig, T. (2024). What is a mathematical structure of conscious experience? *Synthese*, 203(3), 89. https://doi.org/10.1007/s11229-024-04503-4 [V]
- Kleiner, J., & Tull, S. (2021). The mathematical structure of integrated information theory. *Frontiers in Applied Mathematics and Statistics*, 6, 602973. https://doi.org/10.3389/fams.2020.602973 [V]
- Koller, D., & Friedman, N. (2009). *Probabilistic graphical models: Principles and techniques*. MIT Press. [V]
- Lawvere, F. W. (1969). Diagonal arguments and cartesian closed categories. In *Category Theory, Homology Theory and their Applications II* (Lecture Notes in Mathematics 92, pp. 134–145). Springer. https://doi.org/10.1007/BFb0080769 [V]
- Lawvere, F. W. (1973). Metric spaces, generalized logic, and closed categories. *Rendiconti del Seminario Matematico e Fisico di Milano*, 43, 135–166. Reprinted in *Reprints in Theory and Applications of Categories*, 1 (2002), 1–37. [V]
- Mac Lane, S. (1998). *Categories for the working mathematician* (2nd ed.). Springer. https://doi.org/10.1007/978-1-4757-4721-8 [V]
- Mason, J. (2026). The Mathematical Consciousness Hypothesis (MCH) … MoC7 talk, Aud 5. [MoC7]
- Myers, D. J. (n.d.). *Categorical systems theory* [Book draft, unpublished]. https://www.davidjaz.com/Papers/DynamicalBook.pdf (retrieved 2026-10-16) [V: exists as a draft]
- Northoff, G., Tsuchiya, N., & Saigo, H. (2019). Mathematics and the brain: A category theoretical approach to go beyond the neural correlates of consciousness. *Entropy*, 21(12), 1234. https://doi.org/10.3390/e21121234 [V]
- Oizumi, M., Lim, C., & Kanai, R. (2025). Principal bundle geometry of qualia. *PsyArXiv*. [V-roadmap]
- Phillips, S., & Wilson, W. H. (2010). Categorial compositionality: A category theory explanation for the systematicity of human cognition. *PLoS Computational Biology*, 6(7), e1000858. https://doi.org/10.1371/journal.pcbi.1000858 [V]
- Prakash, C. (2026). Contextuality in models of consciousness: Trace logics of observation and belief. MoC7 talk, Aud 5. [MoC7]
- Prentner, R. (2024). Category theory in consciousness science: Going beyond the correlational project. *Synthese*, 204(2), 69. https://doi.org/10.1007/s11229-024-04718-5 [V]
- Rosas, F. E., Mediano, P. A. M., Jensen, H. J., Seth, A. K., Barrett, A. B., Carhart-Harris, R. L., & Bor, D. (2020). Reconciling emergences: An information-theoretic approach to identify causal emergence in multivariate data. *PLOS Computational Biology*, 16(12), e1008289. https://doi.org/10.1371/journal.pcbi.1008289 [V]
- Rosas, F. E., Geiger, B. C., Luppi, A. I., Seth, A. K., Polani, D., Gastpar, M., & Mediano, P. A. M. (2024). Software in the natural world: A computational approach to hierarchical emergence. arXiv:2402.09090 [V]
- Rutten, J. J. M. M. (2000). Universal coalgebra: A theory of systems. *Theoretical Computer Science*, 249(1), 3–80. https://doi.org/10.1016/S0304-3975(00)00056-6 [V]
- Shiebler, D., Gavranović, B., & Wilson, P. (2021). Category theory in machine learning. arXiv:2106.07032 [V]
- Signorelli, C. M., Wang, Q., & Coecke, B. (2021). Reasoning about conscious experience with axiomatic and graphical mathematics. *Consciousness and Cognition*, 95, 103168. https://doi.org/10.1016/j.concog.2021.103168 [V]
- Smithe, T. St. C. (2020). Bayesian updates compose optically. arXiv:2006.01631 [V]
- Smithe, T. St. C. (2022). Polynomial life: The structure of adaptive systems. *EPTCS*, 372, 133–148. https://doi.org/10.4204/EPTCS.372.10 [V]
- Smithe, T. St. C. (2023). *Mathematical foundations for a compositional account of the Bayesian brain* [DPhil thesis, University of Oxford]. arXiv:2212.12538 [V]
- Smithe, T. St. C. (2024). Structured active inference (extended abstract). arXiv:2406.07577 [V]
- Tsuchiya, N., Phillips, S., & Saigo, H. (2022). Enriched category as a model of qualia structure based on similarity judgements. *Consciousness and Cognition*, 101, 103319. https://doi.org/10.1016/j.concog.2022.103319 [V]
- Tsuchiya, N., & Saigo, H. (2021). A relational approach to consciousness: Categories of level and contents of consciousness. *Neuroscience of Consciousness*, 2021(2), niab034. https://doi.org/10.1093/nc/niab034 [V]
- Tsuchiya, N., Saigo, H., & Phillips, S. (2023). An adjunction hypothesis between qualia and reports. *Frontiers in Psychology*, 13, 1053977. https://doi.org/10.3389/fpsyg.2022.1053977 [V]
- Tsuchiya, N., Taguchi, S., & Saigo, H. (2016). Using category theory to assess the relationship between consciousness and integrated information theory. *Neuroscience Research*, 107, 1–7. https://doi.org/10.1016/j.neures.2015.12.007 [V]
- Vagner, D., Spivak, D. I., & Lerman, E. (2015). Algebras of open dynamical systems on the operad of wiring diagrams. *Theory and Applications of Categories*, 30(51), 1793–1822. arXiv:1408.1598 [V]
- Williford, K. (2026). Circularity, hypersets, and the structure of consciousness. MoC7 talk, Aud 2. [MoC7]
- Yanofsky, N. S. (2003). A universal approach to self-referential paradoxes, incompleteness and fixed points. *Bulletin of Symbolic Logic*, 9(3), 362–386. https://doi.org/10.2178/bsl/1058448677 [V]
- Zhang, A., McAllister, R., Calandra, R., Gal, Y., & Levine, S. (2021). Learning invariant representations for reinforcement learning without reconstruction. *ICLR 2021*. arXiv:2006.10742 [V]
