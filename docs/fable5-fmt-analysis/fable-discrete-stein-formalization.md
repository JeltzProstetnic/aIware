# Discrete Stein / CAT(0) Formalization Attempt for SB-HC4A §6.5

**Author:** Fable 5 subagent, 2026-06-11
**Status of this document:** RESEARCH SKETCH — not a proof, not a theorem, not a result.
**Honesty contract:** Everything below is labeled one of:
- **[RIGOROUS]** — established mathematics, citable, but citations should still be spot-checked (LLM recall of exact titles/years is fallible).
- **[PLAUSIBLE]** — an argument I can sketch that a competent statistician/geometer would likely accept after filling gaps, but which has NOT been verified.
- **[CONJECTURE]** — a precise statement whose truth is genuinely open; could be false.
- **[SPECULATIVE]** — physics-side identification with no formal backing.

No claim in this file should enter the paper as anything stronger than its label. The deliverable is a map of the problem, the sharpest minimal open question, and a verdict on whether §6.5's promissory note ("pending the discrete/CAT(0) formalization") is redeemable.

---

## 0. TL;DR

1. The configuration space of a Bekenstein-saturated string-net boundary is **median/CAT(0)-cubical in the abelian case and provably NOT median in the non-abelian case** under the natural move set (pentagon ⇒ odd cycles ⇒ non-bipartite ⇒ not median). So "assume CAT(0)" is not free; it selects the abelian sector.
2. There is a sharp, previously-unstated (to my knowledge) **minimal test problem**: is the rounded MLE for an integer-vector mean θ ∈ Zᵈ of a Gaussian admissible for all d, or inadmissible for d ≥ 3? Neither answer is known to me; **the naive "shrink-then-round" candidate probably fails to dominate** (rounding-boundary bias analysis, §3.3), and it is a live possibility that **discretizing the parameter space kills the Stein effect entirely**.
3. The single tool from the Euclidean proof that transfers to discrete spaces essentially intact is **Brown/Eaton's admissibility ⇔ recurrence correspondence**, which converts the d = 3 Brownian threshold into the **Varopoulos polynomial-growth-degree-2 dichotomy** for random walks on the configuration graph. This gives a plausible route to the *easy half* (admissibility in "dimension ≤ 2") and a candidate statement of the hard half.
4. **Bekenstein finiteness is a structural obstruction**: the configuration space of a finite-area boundary is finite, where every walk is recurrent and identity-type estimators are typically unique-Bayes (hence admissible). Any discrete Stein theorem for this application must be a thermodynamic-limit statement. The paper currently does not acknowledge this.
5. **Physics verdict:** the one-locus/two-particles phenomenon, formalized, is *constrained joint decoding beats product decoding* — which is real, but it is the (unmysterious) error-correction phenomenon, already at home in holographic QEC (HaPPY-type codes / entanglement-wedge reconstruction), not the Stein paradox. The Stein paradox proper (domination *without* shared structure, from loss aggregation + noncompactness) is exactly the part most likely to die under discretization. The d ≥ 3 ⇒ "17 SM particle types" anchor finds **no support in any discrete route examined** and should stay demoted (arguably excised).

**One-line verdict (also at end):** Keep §6.5 demoted as written; the honest formalization target is not James–Stein for one locus but (a) holographic-QEC joint-decoding language for the physics, and (b) a standalone pure-math note on the lattice/median-graph Stein dichotomy — a legitimate open problem, entry point θ ∈ Zᵈ — whose outcome could go either way.

---

## 1. The configuration space, made precise

### 1.1 What the paper needs

§6.5 needs a parameter space Θ = "configurations of one boundary locus" with: (i) a metric (for loss and for Fréchet means), (ii) a product/marginal structure (so "independent description of the two particles" is even definable), (iii) a noise/observation model (so "estimator" is definable). The paper supplies none of these; this section proposes candidates.

### 1.2 String-net configuration spaces **[RIGOROUS background, PLAUSIBLE assembly]**

A Levin–Wen model on a trivalent graph Γ embedded in a surface, with input unitary fusion category 𝒞: a *configuration* is a labeling ℓ: E(Γ) → Irr(𝒞) admissible at each vertex (fusion rules, i.e., N_{ab}^c ≠ 0 for the three incident labels). Θ_Γ = the set of admissible labelings. This is a finite combinatorial set. Two natural graph structures on Θ_Γ:

- **Move graph M_Γ:** edges = elementary local moves (plaquette operators B_p in the abelian case; F/recoupling moves on fusion trees in general).
- **Hamming-type metric:** restriction of the per-edge disagreement metric.

**Case A — abelian (toric code, 𝒞 = Vec_{Z₂}):** configurations = closed-loop (cycle-space) elements of F₂^{E(Γ)}. The plaquette moves are commuting involutions generating the cycle space.
- On a **planar/disk** region the independent plaquette flips give a Cayley graph of F₂^P with P independent involutive generators = the **hypercube Q_P**, which **is a median graph, hence the 1-skeleton of a CAT(0) cube complex** (Chepoi 2000: median graphs are exactly the 1-skeleta of CAT(0) cube complexes) **[RIGOROUS]**.
- On a **closed surface** the plaquettes satisfy one relation per component (∏_p B_p = 1) and configurations split into topological sectors; per-sector move graphs are hypercube *quotients* (folded-cube-like), which are **not median in general** (quotients can create odd or short cycles). **[PLAUSIBLE; checkable case-by-case]**

**Case B — non-abelian (e.g., Fibonacci):** the natural move set is F-moves/recoupling. The pentagon identity equates a path of 2 F-moves with a path of 3 F-moves between the same pair of configurations, i.e., the move graph contains **5-cycles**. Median graphs are partial cubes, hence **bipartite**; a graph with an odd cycle is not bipartite; therefore **the non-abelian recoupling move graph is not a median graph and not the 1-skeleton of a CAT(0) cube complex** under this move set. **[RIGOROUS, given the move set]**
- *Caveat:* medianness is move-set-relative. A different generating move set, a barycentric subdivision, or passing to a derived complex might restore nonpositive curvature (CAT(0) need not be *cubical*; one could try Gromov's link condition on some other polyhedral structure). Whether any natural NPC structure exists on non-abelian string-net configuration spaces is **open** and I found no reason to expect it: pentagon cells are pentagons, and pentagonal 2-cells are compatible with CAT(0) only under angle conditions that would have to be engineered. **[CONJECTURE-level doubt]**

**Consequence:** McCane–Dryden's CAT(0) extension, even if its hypotheses were otherwise satisfiable, applies at best to the **abelian/disk sector** of the boundary theory. Since the paper leans on Levin–Wen precisely for *non-abelian* emergent content (fermions, gauge structure), this is a real mismatch, not a technicality.

### 1.3 The stabilizer-code reading **[RIGOROUS background]**

Alternative, cleaner candidate: take Θ = a linear code C ⊆ F₂ⁿ (stabilizer-code state/syndrome space; holographic codes à la HaPPY: Pastawski–Yoshida–Harlow–Preskill 2015 are the relevant physics family). The ambient hypercube F₂ⁿ is median; the code C is a *subset* of it (not an isometric subgraph unless distance 1, which good codes never are). The natural estimation problem is then:

> θ ∈ C (parameter constrained to the code), observe X = θ ⊕ noise ∈ F₂ⁿ (BSC), estimate θ.

This is **decoding**. It is the formally cleanest home for "product description vs joint description of one locus" — see §4.1, where I argue it is also the *honest* home, and that it changes the genus of the claim.

### 1.4 The Fréchet-mean/median structure **[RIGOROUS background]**

Median graphs carry exactly the structure a discrete Stein program wants:
- A **median operation** m(x,y,z) (unique vertex on geodesics between each pair).
- A **hyperplane (Θ-class) coordinatization**: each median graph isometrically embeds in a hypercube via hyperplane orientations (partial-cube structure; Djoković–Winkler relation).
- **Majority rule:** medians of odd profiles exist and are computed coordinatewise by hyperplane majority (Bandelt & Barthélemy, "Medians in median graphs", c. 1984) **[RIGOROUS, exact reference to verify]**. So the "joint shrinkage target" (sample Fréchet median) is well-defined, consistent with the constraint structure, and computable — the discrete analogue of the grand mean in JS.
- In CAT(0) (cube) complexes, Fréchet means exhibit **stickiness** (Hotz, Huckemann, et al., sticky CLTs on open books, c. 2013; Barden–Le–Owen on BHV tree space): means collapse onto lower-dimensional strata and are insensitive to perturbations, with variance collapse / super-fast rates. **[RIGOROUS phenomenon; its use below is PLAUSIBLE at best]** Stickiness is the most natural *mechanism* by which a joint estimator could strictly dominate in the discrete setting: noise components transverse to a stuck stratum are absorbed at zero cost.

### 1.5 Bekenstein finiteness — the structural problem **[RIGOROUS observation]**

A Bekenstein-saturated boundary of finite area has a **finite** configuration space. On a finite graph: every random walk is recurrent (the Brown/Eaton dichotomy is vacuous), and identity-type estimators are typically admissible — e.g., for the BSC on the full hypercube F₂ⁿ with flip probability p < 1/2, the identity decoder is the **unique Bayes rule under the uniform prior with Hamming loss**, hence admissible. **[RIGOROUS: unique-Bayes ⇒ admissible is standard; the bitwise-MAP computation is elementary]**

So: **no finite-space Stein paradox of the classical kind is available.** Any discrete Stein theorem relevant to §6.5 must be (i) a statement about a *sequence* of boundaries with area → ∞ (thermodynamic limit), with domination gaps bounded below uniformly, or (ii) about the infinite limit graph directly. The paper's framing ("a discrete Stein-type theorem would have to be constructed from scratch") is right but understates this: the theorem must first be *re-typed* as asymptotic.

---

## 2. Candidate theorems

Three precise candidate statements, in increasing order of relevance to the paper and decreasing order of tractability.

### Conjecture A — the minimal test problem (lattice parameter, Gaussian noise) **[CONJECTURE — genuinely open either way, to my knowledge]**

> Let X ~ N(θ, σ²I_d) with θ ∈ Zᵈ, estimators constrained to take values in Zᵈ, loss ‖θ̂ − θ‖². Claim (Stein-survival version): the rounded MLE θ̂₀(X) = round(X) is admissible for d ≤ 2 and **in**admissible for d ≥ 3. Claim (Stein-death version): θ̂₀ is admissible for **all** d.

I do not know which version is true, and I could not name a paper resolving it. (Integer-parameter estimation goes back at least to Hammersley, c. 1950, JRSS-B, on estimating an integer normal mean — d = 1; I am not aware of a d ≥ 3 admissibility analysis. **A literature search by a human is mandatory before claiming novelty.**) This is the right *entry point*: Zᵈ is itself a median graph, its SRW reproduces the Pólya d ≤ 2 / d ≥ 3 dichotomy, and the continuum problem sitting above it is exactly classical JS. If Stein-death holds here, the entire discrete program for §6.5 is dead. If Stein-survival holds, the program has a foundation.

Why it is genuinely unclear — see §3.3: the obvious dominating candidate round(JS(X)) probably does **not** dominate, and the risk of θ̂₀ is *uniformly bounded in θ* (unlike the continuum MLE's constant-but-recoupable risk structure, all the classical "recoup (d−2)²σ⁴E‖X‖⁻² everywhere" leverage is gone except near rounding boundaries).

### Conjecture B — median-graph Stein dichotomy **[CONJECTURE]**

> Let M be a locally finite median graph (1-skeleton of a CAT(0) cube complex), θ ∈ V(M), observation X drawn from a lazy SRW kernel K_t(θ, ·) (or independent per-hyperplane-coordinate flips at rate p — a "graph BSC"), loss = d_M(θ̂, θ) or d_M². Then the formal-Bayes estimator under the counting prior (the natural identity/MAP-type rule) is:
> (i) **admissible if SRW on M is recurrent** — by Varopoulos' theorem, for Cayley-like M this means polynomial volume growth of degree ≤ 2; **[the "easy half"; PLAUSIBLE route via Eaton, §3.1]**
> (ii) **inadmissible if SRW on M is transient**, dominated by an estimator that shrinks hyperplane-coordinate decisions toward the sample/posterior Fréchet median, with the dominating gap controlled by the Green's function of the walk. **[the "hard half"; fully open]**

The discrete analogue of "d ≥ 3" in this statement is **transience of the configuration-graph random walk ≡ isoperimetric/growth dimension > 2** — a property of the *configuration space*, not of any particle count. (Sanity check: M = Zᵈ reproduces the classical threshold.)

### Conjecture C — compound/empirical-Bayes version (the physically relevant asymptotics) **[CONJECTURE, but with the strongest rigorous ancestry]**

> Boundary = N loci with configurations θ₁,…,θ_N ∈ M drawn exchangeably (sharing the substrate ensemble); observe each through the same noisy kernel; total loss = Σ d_M(θ̂_i, θ_i). Then the componentwise rule is asymptotically dominated (as N → ∞, uniformly over the empirical measure class) by a compound rule that shrinks toward the empirical Fréchet median of the sample, with savings governed by the mutual information between hyperplane coordinates induced by the shared ensemble.

Ancestry: Robbins' compound decision theory (1951 "asymptotically subminimax solutions…", 1956 empirical Bayes) — and Robbins' original 1951 example is itself a **discrete-parameter** problem (θ_i ∈ {−1, +1}), where the compound rule beats the componentwise minimax rule for large N. **[RIGOROUS ancestry]** Discrete-*data* Stein effects are also established: Clevenson–Zidek 1975 (simultaneous Poisson means, normalized loss, threshold d ≥ 2 — note: the threshold moved, see §4.2), Hwang 1982 (discrete exponential families). **[RIGOROUS]** What is open is the marriage: compound decision theory with a discrete, median-graph-valued *parameter*, loss = graph metric, shrinkage = reweighted hyperplane majority toward the empirical median. This is, in my assessment, the most likely of the three to be both true and provable — because it replaces the fragile pointwise-domination requirement with asymptotic-in-N domination, which is how Robbins-type results evade exactly the finiteness/boundedness obstructions of §1.5 and §3.3.

---

## 3. Proof strategy and obstructions

### 3.1 What transfers: the Brown–Eaton recurrence bridge **[RIGOROUS tool, PLAUSIBLE application]**

The deepest structural fact in the Euclidean story is Brown 1971: admissibility of (generalized Bayes) estimators of a Gaussian mean corresponds to recurrence of an associated diffusion — this is *why* the threshold is d = 3 (Brownian recurrence in d ≤ 2, transience in d ≥ 3). Eaton (c. 1992, Ann. Statist., "A statistical diptych: admissible inferences — recurrence of symmetric Markov chains", and follow-ups) generalized the sufficient direction to abstract state spaces: **if the symmetric Markov chain associated (via the Dirichlet form of the formal posterior) with an improper-prior formal Bayes rule is recurrent, the rule is admissible** — and Eaton's framework does not require continuum structure. **[RIGOROUS; exact statement and regularity conditions must be verified against the paper]**

Application: for the counting (uniform improper) prior on an infinite median graph M, the associated chain is (a variant of) the SRW on M. Recurrence of SRW on M is controlled by volume growth/isoperimetry (Varopoulos: a Cayley graph is recurrent iff the group has polynomial growth of degree ≤ 2; Nash-inequality versions cover bounded-degree graphs with isoperimetric dimension > 2 ⇒ transient). **[RIGOROUS]** This yields a credible proof skeleton for Conjecture B(i) — the d ≤ 2 half. Crucially, **transience does NOT automatically yield inadmissibility** — that converse direction needed separate, Gaussian-specific work even in Brown 1971. The hard half does not come for free from the bridge.

### 3.2 What breaks: the Euclidean toolkit, tool by tool

| Euclidean tool | Role in JS proof | Discrete fate | Replacement candidate |
|---|---|---|---|
| Stein's lemma E[(X−θ)·g(X)] = σ²E[∇·g] | Computes risk difference unbiasedly (SURE) | Gone: no integration by parts against a continuum parameter; discrete Stein operators (Hudson's lemma for Poisson; Stein–Chen) act on the **data** side, not the parameter side | Summation-by-parts on the graph Laplacian for the *kernel* K_t; Dirichlet-form risk identities (Eaton route) |
| Smooth shrinkage path θ̂_λ = (1−λ)X | Risk is differentiable in λ; small shrinkage always helps when d ≥ 3 | Gone: estimates must jump between vertices; "shrink by ε" is not available | Randomized estimators (see below); or shrink the *decision thresholds*, not the estimate |
| Unbounded risk landscape (risk recouped at every θ) | Domination gap integrable everywhere | Gone: rounded-MLE risk is uniformly bounded; gains exist only near decision boundaries / small ‖θ‖ | Asymptotic-in-N compound formulation (Conj. C); or thermodynamic limit in boundary area |
| Convexity of loss (randomization never helps) | Restricts to nonrandomized estimators | **Reversed**: with estimates constrained to a discrete set, the Rao–Blackwell averaging argument exits the parameter space; randomized decoders can be strictly unbeatable by deterministic ones | Work in the randomized-decision framework from the start; a "discrete JS" may be irreducibly randomized — a referee will demand this be confronted |
| Brownian recurrence/transience at d = 3 | Explains the threshold | **Survives** (the one survivor): SRW recurrence/transience, Varopoulos dichotomy | Eaton bridge (§3.1) |

### 3.3 Why the naive candidate fails (obstruction analysis for Conjecture A) **[PLAUSIBLE analysis, not a proof]**

Take θ̂_JS-round = round(JS(X)) in the Zᵈ problem. At θ = 0 it is far better than round(X) (it returns 0 with high probability while round(X) pays ≈ d·P(|N(0,σ)| > 1/2)·(…) — a large saving, growing with d). But at large ‖θ‖: the JS shift vector has magnitude ≈ (d−2)σ²/‖X‖; shifts smaller than 1/2 change the rounding **only when a coordinate sits near a half-integer** — and there the shift biases decisions systematically toward the origin, i.e., the *wrong way on average*, adding a per-coordinate excess error ≈ (Gaussian density at the boundary) × (shift). Summed over d coordinates this is an excess risk ~ c·d²/‖θ‖ > 0 at moderate ‖θ‖, decaying but **positive** — so round(JS) plausibly does *not* dominate round(X); it trades. A genuine dominating estimator, if one exists, needs a data-dependent dead zone (no shrinkage unless ‖X‖² is improbably small under every θ in a lattice neighborhood) and a proof technique that controls **rounding-boundary terms** — the discrete replacement for the boundary terms that vanish in Stein's integration by parts. Nobody has built this, and it may be unbuildable: the Stein-death branch of Conjecture A (admissibility for all d, e.g., via a Blyth-method argument with discrete priors exploiting the uniformly bounded risk) is fully live.

### 3.4 The stickiness route (most promising discrete-geometry mechanism) **[PLAUSIBLE lead]**

In CAT(0) cube complexes / open books, Fréchet means are sticky: the mean of a perturbed sample stays on a lower stratum, with transverse noise absorbed (Hotz et al.; BHV-space literature). A shrinkage estimator whose target is a sticky median inherits variance collapse — the discrete-geometry analogue of "shrinkage reduces variance more than it adds bias". Program: (1) quantify the risk of median-targeted shrinkage on a cube complex via the sticky CLT; (2) show the absorbed-noise saving exceeds the bias cost exactly when the complex branches enough (degree/valence ≥ 3 at hyperplane crossings — a tantalizing but **unproven** discrete echo of d ≥ 3); (3) feed this into the hard half of Conjecture B. Step (2) is pure conjecture; the "valence ≥ 3 ↔ d ≥ 3" echo is exactly the kind of pattern-matching an LLM finds seductive and a referee should distrust until computed.

### 3.5 McCane–Dryden as imported black box **[UNVERIFIED]**

The paper cites McCane & Dryden (2022) for Stein in CAT(0) spaces. I have **not** verified that paper's actual hypotheses (noise model, loss, class of spaces, whether domination is proved or simulated). Before any formalization leans on it, a human must check: does it prove strict domination, for which noise families, and do its hypotheses tolerate atoms/discreteness? If its proof needs smooth densities along geodesics (likely), it does not transfer to vertex-supported measures without new work.

---

## 4. Connecting back to the physics — honestly

### 4.1 What the one-locus claim actually formalizes to

§6.5's claim: the product-state description of an entangled pair is an inadmissible decoding of one boundary locus. Formalize "one locus, two interior reflections" and you get: a parameter θ constrained to a coupled set (a code C, §1.3), observed through two marginal channels; the "independent description" = decode each marginal separately; the "entangled description" = joint decoding using the constraint.

But notice what this is: **the gain of joint over product decoding here comes entirely from the constraint/coupling** — information the product decoder *discards*. That is real, large, and provable in specific models — and it is **not the Stein paradox**. The Stein paradox's scandal is domination *without* any coupling: independent parameters, separable loss, and shrinkage still wins, purely from loss aggregation over a noncompact space. The paradox-grade ingredient is exactly the one that (a) §1.5 and §3.3 show is most endangered by discreteness/finiteness, and (b) the physics doesn't need. What the physics needs — "the joint description of a genuinely coupled substrate strictly beats the product description" — already has a rigorous home: **holographic quantum error correction** (HaPPY codes, entanglement-wedge vs local reconstruction), where joint-decoding advantages are theorems, not analogies. Translating §6.5's promissory note into holographic-QEC decoding language would be *strictly more honest and strictly better-supported* than completing a discrete JS theorem.

A second honest deflation: for ONE locus viewed twice, the statistical content of "the product description is wrong" is just "the joint posterior is not the product of its marginals" — true, important, and **trivial** (it is the definition of correlation). Stein's theorem adds the word "inadmissible" but, for a single coupled parameter, adds no content beyond that triviality. The non-trivial Stein-flavored statement lives only in the **compound** setting (Conjecture C): many loci, borrowing strength — and there the threshold is in N (number of loci) and configuration-graph growth, not in any "3".

### 4.2 The d ≥ 3 / 17-particle-types anchor

Every discrete route examined replaces the d ≥ 3 threshold with something that does not count particle species:
- Conjecture B: **growth/isoperimetric dimension > 2 of the configuration graph** — for Bekenstein-saturated boundaries the configuration graph in the thermodynamic limit has (at least) exponential volume growth, so the transience condition is crossed *trivially and by an enormous margin*; nothing distinguishes 17 from 4 or 10⁶.
- Conjecture C: threshold is asymptotic in the number of loci N.
- Known discrete-data results: the threshold is **loss-dependent** (Clevenson–Zidek get d ≥ 2 under normalized loss) — the "3" is not even stable within classical statistics.

**Conclusion: the 17-particle anchor is unsupported by every candidate formalization, including the ones favorable to the paper. It should remain demoted; I would recommend excising it entirely rather than leaving it as a "pending" item, because no plausible completion of the program restores it.** The paper's current text already demotes it — correctly — but still frames it as awaiting reinterpretation; the analysis here suggests it awaits deletion.

### 4.3 The missing noise model

A deterministic substrate has no sampling noise, so *whose* estimation problem is this? For the Stein/decoding machinery to attach, the paper must specify: the observer's coarse-grained access map (the channel), the ensemble the risk is averaged over (which configurations of the locus count as "the same experiment"), and why the interior decompression map is an *estimator* in the decision-theoretic sense rather than a fixed isomorphism. §8.2's "interior states are decodings" gestures at this but does not construct the channel. Without that construction, even a fully proven Conjecture B would hang in the air: a theorem about a statistical problem nobody has shown the universe to be solving. This is, in my assessment, a **bigger gap than the missing mathematics**, and it is a physics-modeling gap, not one a statistician can close.

---

## 5. Brutally honest status and verdict

**Rigorous (background):** median graphs = CAT(0) cube-complex skeleta; majority/median structure; pentagon ⇒ non-bipartite ⇒ non-median for non-abelian recoupling graphs (move-set-relative); Brown 1971 / Eaton ~1992 admissibility–recurrence bridge; Varopoulos growth dichotomy; Robbins compound decision theory incl. discrete-parameter examples; Clevenson–Zidek / Hwang discrete-data Stein effects; stickiness of Fréchet means in NPC spaces; unique-Bayes admissibility of identity decoding on finite hypercubes. (All citations to be human-verified.)

**Conjectural (the actual deliverables):** Conjectures A, B, C — none proven here, none claimed. Conjecture A could resolve *against* the program. The §3.3 obstruction analysis and the §3.4 stickiness mechanism are sketches.

**Hand-waving in the paper that this analysis confirms as hand-waving:** the d ≥ 3 ↔ 17 species anchor (no candidate formalization supports it); the implicit assumption that a single-locus problem exhibits a Stein effect at all (it exhibits only joint-vs-marginal posterior non-factorization); the unacknowledged finite-configuration-space problem.

**What a referee would demand:** (1) the noise model / channel construction of §4.3 before any theorem is even relevant; (2) resolution of Conjecture A or an explicit reduction showing why it can be bypassed; (3) confrontation of the randomized-estimator issue (§3.2); (4) verification of McCane–Dryden's actual hypotheses; (5) a reason the abelian-sector restriction (§1.2) doesn't gut the Levin–Wen connection; (6) either a thermodynamic-limit formulation or abandonment of pointwise domination.

**Is the direction worth a dedicated formalization paper?** Split answer:
- As *support for §6.5's physics claim*: **no** — the claim's honest formal home is holographic-QEC joint decoding, where the needed statements are already theorems and the Stein vocabulary is rhetorical. Recommend §6.5 keep the lens demoted exactly as it stands (the current text is defensible), with a possible future edit replacing "pending the discrete/CAT(0) formalization" by a pointer to QEC decoding — a *reframing*, not a proof obligation.
- As *standalone mathematics*: **yes, cautiously** — "Does the Stein effect survive discretization of the parameter space?" (Conjecture A, then B/C) is a sharp, apparently open, well-posed question with a credible toolkit (Eaton bridge + Varopoulos + sticky medians + Robbins compound asymptotics), publishable in a statistics/discrete-geometry venue regardless of which way it resolves — but it would be a statistics paper that *mentions* the cosmology, not a cosmology result.

**ONE-LINE VERDICT:** James–Stein is the wrong tool for the one-locus entanglement claim — keep it demoted (the real phenomenon is constrained joint decoding, already rigorous in holographic QEC) — while the discrete Stein question itself is a legitimate standalone open problem whose best lead is the Eaton admissibility-recurrence bridge turning Brown's d = 3 into the Varopoulos growth-degree-2 dichotomy on median graphs, with θ ∈ Zᵈ rounded-MLE admissibility as the decisive minimal test case.
