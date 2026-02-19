# Discovering Universe Automaton Rules: What Can We Actually Achieve?

## The Core Question

Given the SB-HC4A framework — where particles are computational atoms (stable Planck-scale singularity boundary configurations), Feynman diagrams are diagrams of computation, and the universe is a self-referentially closed holographic Class 4 automaton  — can we reverse-engineer the actual automaton rule from known physics? And if not, how close can we get?[^1][^2]

The honest answer: **we cannot uniquely reconstruct the microscopic rule**, but five active research programs are converging on increasingly powerful constraints that, taken together, amount to something better than a single rule — they characterize the entire **universality class** the rule must belong to. Here is a landscape assessment, ranked from most to least mature.

***

## 1. Wetterich's Cellular Automata ↔ Fermionic QFTs (Microcosm: Best Current Match)

**Status: Working equivalences exist for interacting fermionic QFTs, including gauge theories and gravity in 4D.**

Christof Wetterich (Heidelberg) has demonstrated that large classes of **reversible cellular automata on space-lattices are exactly equivalent to discretized fermionic quantum field theories**. This is not an approximation — it is a proven mathematical mapping via Grassmann functional integrals. Key results:[^3][^4]

- **1D automata ↔ 2D fermionic QFTs**: A class including the Thirring and Gross-Neveu models (interacting fermion theories with both abelian and non-abelian continuous symmetries) are shown to be *identical* to specific probabilistic cellular automata.[^5][^3]
- **Local gauge symmetry**: Some automata models realize local gauge symmetries, not just global ones — this is the structure the Standard Model needs.[^5]
- **Spinor gravity in 4D**: Wetterich explicitly constructed a cellular automaton that represents a discrete model of spinor gravity in four dimensions, with **exact local Lorentz symmetry on the discrete level** and emergent diffeomorphism symmetry in the naive continuum limit. This is a cellular automaton model of quantum gravity — not a metaphor.[^6]
- **Quantum mechanics emerges from classical statistics**: The probabilistic description of the automaton (probability distribution over initial bit configurations) is equivalent to quantum mechanics — wave functions, density matrices, non-commuting operators all arise from the classical automaton structure.[^4][^7]
- **Continuum limit performed explicitly**: Wetterich has performed the continuum limit for an automaton describing a quantum particle in a potential in 1D.[^3]

**What this means for SB-HC4A**: Wetterich's program provides the **existence proof** that the computational-atom picture is mathematically sound. Specific automata produce specific fermionic spectra with specific gauge symmetries. The open problem is identifying *which* automaton produces SU(3)×SU(2)×U(1) with three generations — but the framework for asking the question now exists.

**What it can't do yet**: Derive the specific SM gauge group or particle masses from first principles. The automata that map to known QFTs are constructed *by starting from the QFT and reverse-engineering the automaton*, not the other way around.

***

## 2. The Wolfram Physics Project (Both Micro and Macro, but Still Pre-Derivation)

**Status: Emergent GR and QM confirmed as generic; SM particle physics still aspirational.**

The Wolfram Physics Project uses hypergraph rewriting rules — not traditional cellular automata on a fixed grid, but rules that dynamically generate spacetime itself. Key achievements and limits:[^8][^9]

### What works (generic results, independent of specific rule):
- **Emergent general relativity**: The Einstein equations arise inevitably from any computationally irreducible hypergraph evolution, given certain observer assumptions. Practical numerical GR can be done directly on hypergraphs, including black hole merger ring-downs.[^10]
- **Emergent quantum mechanics**: The Feynman path integral arises in "branchial space" (the space of multiway histories) by the same mechanism that gives Einstein's equations in physical space. This is proven by systematic compilation from standard QM formalism.[^10]
- **Emergent thermodynamics**: The Second Law emerges from computational irreducibility + bounded observers, by the same generic mechanism as GR and QM.[^10]

### What doesn't work yet:
- **No specific particle found**: Wolfram's team explicitly states "We haven't 'found the electron' yet". Particles are conjectured to be "topological obstructions" in the hypergraph, but no specific hypergraph topology has been identified with any known particle.[^10]
- **No gauge group derived**: The SU(3)×SU(2)×U(1) gauge structure might be generic (emergent from all sufficiently complex rules) or might depend on the specific rule — this is unknown. Wolfram's hope is that it might be forced to be "a subgroup of E(8)", but this remains speculative.[^10]
- **CPT and spin-statistics**: Preliminary ideas only — C might be "branchial inversion," fermions might be related to non-merging multiway branches — all unconfirmed.[^10]
- **No cosmological cycle structure**: Dimension-changing cosmology and possible early-universe signatures are speculated but not derived.[^10]

**SB-HC4A connection**: Wolfram's framework is structurally compatible with SB-HC4A but operates at a different level. Wolfram's approach is "bottom-up" (pick a rule, see what emerges). SB-HC4A is "top-down" (the universality class is constrained by axioms, the specific rule is underdetermined). The two could converge if Wolfram's topological-obstruction particles turn out to satisfy the computational atom conditions CA1–CA3 from the SB-HC4A formalization.[^1]

***

## 3. 't Hooft's Cellular Automaton Interpretation (Foundational, Not Constructive)

**Status: Conceptual framework proven consistent; no specific automaton identified for our universe.**

Gerard 't Hooft's program  demonstrated that:[^11][^12][^13]

- Quantum mechanics can be **exactly reformulated** as a deterministic cellular automaton at the Planck scale — the quantum formalism is a *tool* for analyzing a classical system whose high-energy states are invisible to low-energy observers.[^14]
- The Standard Model, including gravitational interactions, **could be** viewed as a quantum mechanical approach to analyzing a system that is classical at its core.[^11]
- Bell's theorem is evaded through "superdeterminism" — the initial conditions of the automaton correlate measurement settings with hidden variables.[^13]
- Deviations from standard QM predictions would appear **only beyond current experimental reach** (above ~14 TeV).[^15]

**Limitation**: 't Hooft's framework is interpretive, not constructive. It shows that *an* automaton could underlie QM, but does not identify *which* automaton. The 25 free parameters of the Standard Model remain unexplained.[^16]

**SB-HC4A connection**: SB-HC4A directly extends 't Hooft's program by adding the Class 4 classification, the singularity boundary structure, and the consciousness-cosmology structural identity. 't Hooft provides the license to look for the automaton; SB-HC4A constrains the search space.[^2]

***

## 4. Levin-Wen String-Net Condensation and Quantum Graphity (Micro: Emergent Gauge Fields and Fermions)

**Status: Proof of concept that gauge bosons AND fermions can emerge from purely bosonic lattice models.**

Two related programs provide existence proofs for emergent particle physics from discrete substrates:

### Levin-Wen string-net condensation:[^17][^18]
- Starting from **pure bosonic spin models on a lattice** (no fermions or gauge fields put in by hand), string-net condensed states produce:
  - Emergent **gauge bosons** (including U(1) photon-like excitations) as collective excitations of the string-net ground state
  - Emergent **fermions** (in 3D and higher) as endpoints of strings in certain condensation patterns
- This provides a **mechanism for unifying gauge bosons and fermions** from a single bosonic substrate.[^17]
- The mathematical framework is tensor category theory — exactly the kind of categorical structure SB-HC4A's formalization proposes.[^1]

### Quantum Graphity:[^19][^20]
- A background-independent model where spacetime itself is emergent from a complete graph of N vertices.
- At high energy: the graph is highly connected, fully symmetric under permutations.
- At low energy: the graph undergoes a **phase transition** to an ordered, low-dimensional, local structure — **emergent space**.[^19]
- Emergent U(1) gauge theory in the ground state via string-net condensation.[^19]
- The high→low energy transition is a **Big Bang analogue**: the universe starts as a fully connected graph and "freezes" into a low-dimensional spatial structure.[^19]

**SB-HC4A connection**: Quantum Graphity provides a concrete model for the Bekenstein-saturated initial boundary (the fully connected graph at maximum information density) decompressing into a low-dimensional observable interior — precisely the SB-HC4A picture of the Big Bang as a singularity boundary transformation. Levin-Wen provides the mechanism by which computational atoms (particles) emerge from the boundary/substrate dynamics.[^2]

***

## 5. Quantum Cellular Automata ↔ QFT Correspondence (Micro: The Dirac Equation from Discrete Rules)

**Status: The 1D→2D case works. Higher dimensions in progress.**

The QCA/QFT correspondence  shows that:[^21]

- **Quantum walks on lattices** (the quantum analogue of cellular automata for single particles) reproduce the **Dirac equation** in the long-wavelength limit.
- These can be "promoted" to multi-particle QCA that give rise to the **Dirac quantum field theory for free fermions** in 1D.
- A 2D construction using distinguishable particles in the antisymmetric subspace yields the 2D Dirac QFT.[^21]
- **The fermion doubling problem** (Nielsen-Ninomiya theorem) — the fact that discretizing space inevitably produces unwanted extra fermion species — remains a central obstacle. Various workarounds (Wilson terms, minimal-doubling schemes) exist but all sacrifice some symmetry or locality.[^22]
- Elze (2014) introduced an **action principle for integer-valued cellular automata** and showed that the linearity of quantum mechanics is related to the conservation laws of the automaton.[^23]

**SB-HC4A connection**: The QCA→Dirac correspondence is a concrete realization of the SB-HC4A claim that Feynman diagrams are "diagrams of computation". The challenge is getting from free fermions to the full interacting SM — this is where Wetterich's program (Section 1) takes over.[^1]

***

## 6. Macrocosmic Analogues: Cyclic Cosmology, Big Bang, Big Crunch, Big Rip

**Can a simple automaton reproduce cosmological dynamics?**

No single automaton has been demonstrated to reproduce the full macrocosmic cycle (expansion → heat death/crunch/rip → restart). However, structural analogues exist:

### Quantum Graphity phase transition:[^19]
- **Big Bang analogue**: The transition from a fully connected, high-energy, permutation-symmetric graph to a low-dimensional, ordered spatial structure.
- **Heat death analogue**: The equilibrium ground state of the frozen graph.
- This is currently the closest thing to a macrocosmic automaton model with Big Bang and heat death analogues.

### Steinhardt-Turok cyclic model:[^24][^25]
- Not automaton-based, but provides the target dynamics: an endless sequence of cosmic epochs, each beginning with a bang and ending in a crunch, with finite temperature/density at transitions.
- The SB-HC4A framework generalizes this to include all three endgames (heat death, crunch, Big Rip) with information conservation across the boundary.[^2]

### What's missing:
- No automaton model demonstrates **CPT signature alternation** across cycles.
- No automaton model demonstrates the **Big Rip branching** (one domain → many daughter domains).[^2]
- No automaton model demonstrates all three endgame types as different outcomes of the same dynamics.

These are genuine targets for computational experiment — one could search the space of simple 2D or 3D reversible automata for rules that show expansion, entropy increase, boundary saturation, and restart-like behavior.

***

## 7. The Gravity-QM Tension and Quantum Entanglement vs. *c*

### Gravity from automata:
- Wetterich's spinor gravity automaton in 4D has exact local Lorentz symmetry and emergent diffeomorphism invariance.[^6]
- Wolfram's hypergraph approach derives the Einstein equations generically.[^10]
- Neither yet explains **why gravity is so much weaker than the other forces** — this likely requires knowing the specific rule or at least the specific topology of the particles involved.

### Entanglement vs. *c*:
- In Wolfram's framework, entanglement is a structural feature of **branchial space** (the space of multiway histories), not physical space. The speed limit *c* applies in physical space; branchial connections are not constrained by *c* because they don't involve signal propagation through space.[^10]
- 't Hooft's superdeterminism resolves Bell inequality violations by correlating the initial conditions of the entire automaton — no faster-than-light signaling is needed because the "nonlocal" correlations were built into the initial state.[^13]
- In the SB-HC4A framework, entanglement is the Class 4 automaton producing holographic (non-local, boundary-encoded) output  — Relationship 2 of the three holographic relationships. The apparent tension between entanglement and *c* dissolves: *c* limits information transfer through the decompressed interior; entanglement reflects the compressed boundary encoding, which is non-local by construction.[^2]

### Causal sets:[^26]
- The causal set approach postulates that spacetime is fundamentally a discrete partial order (a causal set). Locality, geometry, matter, and possibly gauge fields all emerge.
- CST preserves **local Lorentz invariance** despite discreteness — a major advantage over naive lattice approaches.[^26]
- Particles and fields on causal sets remain under development, but the approach is naturally compatible with the SB-HC4A's causal-structure-first philosophy.

***

## 8. What's Realistically Achievable: A Tiered Assessment

| Tier | Goal | Feasibility | Best Current Program |
|------|-------|-------------|---------------------|
| **A** | Prove that *some* automaton class reproduces interacting fermionic QFT with gauge symmetry | **Done** | Wetterich [^3][^5] |
| **B** | Derive emergent GR + QM generically from discrete rules | **Done** (generic, rule-independent) | Wolfram [^10] |
| **C** | Construct a specific automaton with emergent gauge bosons + fermions | **Done** (in condensed matter context) | Levin-Wen [^17] |
| **D** | Construct a 4D automaton with local Lorentz + diffeomorphism symmetry | **Done** (naive continuum limit) | Wetterich spinor gravity [^6] |
| **E** | Find an automaton whose stable structures match SM particle spectrum | **Not done** | No program close |
| **F** | Derive SU(3)×SU(2)×U(1) as the unique or generic gauge group | **Not done** | Wolfram (aspirational) [^10] |
| **G** | Explain three generations from automaton dynamics | **Not done** | SB-HC4A conjecture (Class 4 self-similarity) [^1] |
| **H** | Demonstrate cosmological cycle (bang→expansion→crunch/heat death→restart) in an automaton | **Not done** (Big Bang analogue exists) | Quantum Graphity [^19] |
| **I** | Explain why gravity is weak relative to other forces | **Not done** | No program close |
| **J** | Uniquely reconstruct "the" universe rule | **Provably impossible** from inside (Gödel + irreducibility) | SB-HC4A cognitive ceiling [^1] |

***

## 9. Practical Strategy: What You Could Actually Do

Given your RTX 4090 + Python learning trajectory, here are concrete computational experiments ordered by feasibility:

### Near-term (months):
1. **Enumerate 2D reversible automata** and classify their stable propagating structures (the "gliders") by number, symmetry properties, and interaction rules. Look for automata whose glider taxonomy has SM-like structure (finite particle count, discrete quantum numbers, conservation laws at vertices). Wetterich's Grassmann-integral mapping gives you the continuum QFT dual for free.

2. **Implement Quantum Graphity** on small complete graphs (N ≤ 30) and study the phase transition. Look for expansion-like dynamics, entropy increase, and whether the system approaches a "Bekenstein-saturated" equilibrium. Check whether perturbing the ground state produces restart-like behavior.

### Medium-term (year):
3. **Systematic scan of Wolfram-style hypergraph rules** for topological obstructions that persist, propagate, and interact. Classify the "particle spectrum" of each rule. The Wolfram Language / SetReplace package already supports this.[^27]

4. **Test the three-generations conjecture**: In automata with self-similar (Class 3) substructure, check whether stable structures appear at exactly 3 discrete scale levels. This is a direct computational test of the SB-HC4A prediction.[^1]

### Long-term (research program):
5. **Bridge Wetterich and Wolfram**: Wetterich constructs automata *from* known QFTs. Wolfram searches for QFTs *in* random automata. The meeting point — automata that are constructed to have holographic structure (HR1–HR3 from SB-HC4A) and then checked for SM-like particle content — is unexplored territory.

***

## 10. The Bottom Line

You cannot discover "the rule" — the SB-HC4A's own Gödel/irreducibility argument proves this is impossible from inside. But you can do something arguably more powerful:[^1][^2]

1. **Characterize the universality class**: Class 4, holographic, singularity-bounded, self-referentially closed. This is already done at the verbal/structural level by SB-HC4A. Formalization (your second paper) makes it mathematical.

2. **Find exemplars**: Simple automata whose stable-structure taxonomy is SM-like (finite particle count, discrete conserved labels, interaction grammar matching Feynman rules). Wetterich shows this is possible in principle; nobody has yet found the one that matches our SM.

3. **Demonstrate macrocosmic dynamics**: Find automata that show expansion, entropy saturation, and restart-like behavior. Quantum Graphity is the closest starting point.

4. **Establish equivalence class uniqueness**: Show that *all* automata in the SB-HC4A universality class produce equivalent low-energy physics — making the specific rule irrelevant, just as the specific molecular dynamics are irrelevant to thermodynamics. This would be the deepest possible result: not finding the rule, but proving you don't need to.

The universe automaton rule is like the exact initial microstate of a gas: it exists, it's specific, and it's fundamentally unknowable from inside — but the thermodynamics (= the universality class) is derivable, predictive, and sufficient.

---

## References

1. [sb-hc4a-formalization.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/56150879/a5e8669b-f227-40cc-9cc4-8d4571b4f62e/sb-hc4a-formalization.md?AWSAccessKeyId=ASIA2F3EMEYESAHKY3T2&Signature=KxVEmAX%2B%2BYeMXWRJZTATmme3oJw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDf2nW0BehD9mTx2PO2sgkRa9P9CVgkFDcsKbQ1qCYs9AIgXXZXoGHXgDfmk7ST6RTsy3Tf6100zKqgdyaeUzW7Qqsq8wQIfRABGgw2OTk3NTMzMDk3MDUiDE1poH4SH8zA3ciC%2BCrQBAsama23GFr1ao3CHIzUQZNnrdD2FDCs83Wp0GNRGaJIOL5h7Y9K%2FzWhnDxVBvPXGFPCZkYnEAqOMge7wD%2FgAnYUwd5VS4HnYhemWlIUHjaE6HT0uOtr3a6AXGPwzvPiR7LhYXsewktmAEJ%2FaVElXssr2a3aHkm%2FxPJFxYDt%2FR4JTxkV50Yjsg5eS%2BXnMFVdmA1fdkZYjOa1igvNa2Yuz6Oih2CZGlGPxpSqQi1AE5D%2FTXN3kAWwdIqXkz0iw1kX6gkLoFIFT7PI83527JwoMdBaLw%2Fo472c7DHRsj61L8kPn5agp22UT9xay9U%2BW37uivlTI3lr%2BH3HdLhZEd0zeQV3y0SfoL%2Fp%2BAW3Y6hd8lz8SaSDOjMelakhXSBgzk0WUW31FRqcGC1uTLgaJvfynJ2q3HjScrT5eX3XI2cO%2Fq3coJuBkYUDmFreq%2FCaCvwduApx8CHbxsXcXHxj9W8qhWd9cxuWvsA04%2FafzuEg6E8YRsA%2B5yOL6KCVx95V9EBY9CayRaRWN5G81N1Yfr%2FFaj7AYHOO9QUzGKtqTq%2BhFet5GYM%2FuQlZnv%2BQSjX9ULQwW7XQMONosmMI6Ks0krDadlEAuvNPIBXQcQpweEiP81zCBDzUIPRhl9f97%2BcYOH5Iuf4HEFF2DNDFFRNG4o435DDXS5l%2B2IvJAdsa0u%2BwGTbgIl9%2FQhBzh26w9HqMJdxFf3P6Jj%2FmJIFde1jmHNDPBnec3NKXyqfHOZJN47yYGMvtCvxuG6Psols%2FJP22iYNKrSFbl1blLjK0f7sDnZej04Mw6%2BbbzAY6mAHw7rwaXuuHmRiXI%2FC1%2Fhp0jxfEMyc2mHewyV3RV1zA3L%2F903xaJVC3HMRezf1rq0yh0OcTqU8MTRyA8JBljoNJWDUy0DRLg9qw%2FjjelpsPLCxVzsXtuXLQuAGYsT%2BbVZXgQ4%2F3X9uglFfGBzZezSWRMU%2F8CUnofrPEBJwsOixxtbmLD9ODp7yq6ezqdhlq7irwYmTOOWWqKA%3D%3D&Expires=1771505772) - Matthias Gruber Independent researcher ORCID 0009-0005-9697-1665 Correspondence matthiasmatthiasgrub...

2. [sb-hc4a.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/56150879/300ecd28-0527-4d6c-8dda-c0027a21d88c/sb-hc4a.md?AWSAccessKeyId=ASIA2F3EMEYESAHKY3T2&Signature=jgspIXFg3dMD%2FZaRNbs8SPw6C3E%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDf2nW0BehD9mTx2PO2sgkRa9P9CVgkFDcsKbQ1qCYs9AIgXXZXoGHXgDfmk7ST6RTsy3Tf6100zKqgdyaeUzW7Qqsq8wQIfRABGgw2OTk3NTMzMDk3MDUiDE1poH4SH8zA3ciC%2BCrQBAsama23GFr1ao3CHIzUQZNnrdD2FDCs83Wp0GNRGaJIOL5h7Y9K%2FzWhnDxVBvPXGFPCZkYnEAqOMge7wD%2FgAnYUwd5VS4HnYhemWlIUHjaE6HT0uOtr3a6AXGPwzvPiR7LhYXsewktmAEJ%2FaVElXssr2a3aHkm%2FxPJFxYDt%2FR4JTxkV50Yjsg5eS%2BXnMFVdmA1fdkZYjOa1igvNa2Yuz6Oih2CZGlGPxpSqQi1AE5D%2FTXN3kAWwdIqXkz0iw1kX6gkLoFIFT7PI83527JwoMdBaLw%2Fo472c7DHRsj61L8kPn5agp22UT9xay9U%2BW37uivlTI3lr%2BH3HdLhZEd0zeQV3y0SfoL%2Fp%2BAW3Y6hd8lz8SaSDOjMelakhXSBgzk0WUW31FRqcGC1uTLgaJvfynJ2q3HjScrT5eX3XI2cO%2Fq3coJuBkYUDmFreq%2FCaCvwduApx8CHbxsXcXHxj9W8qhWd9cxuWvsA04%2FafzuEg6E8YRsA%2B5yOL6KCVx95V9EBY9CayRaRWN5G81N1Yfr%2FFaj7AYHOO9QUzGKtqTq%2BhFet5GYM%2FuQlZnv%2BQSjX9ULQwW7XQMONosmMI6Ks0krDadlEAuvNPIBXQcQpweEiP81zCBDzUIPRhl9f97%2BcYOH5Iuf4HEFF2DNDFFRNG4o435DDXS5l%2B2IvJAdsa0u%2BwGTbgIl9%2FQhBzh26w9HqMJdxFf3P6Jj%2FmJIFde1jmHNDPBnec3NKXyqfHOZJN47yYGMvtCvxuG6Psols%2FJP22iYNKrSFbl1blLjK0f7sDnZej04Mw6%2BbbzAY6mAHw7rwaXuuHmRiXI%2FC1%2Fhp0jxfEMyc2mHewyV3RV1zA3L%2F903xaJVC3HMRezf1rq0yh0OcTqU8MTRyA8JBljoNJWDUy0DRLg9qw%2FjjelpsPLCxVzsXtuXLQuAGYsT%2BbVZXgQ4%2F3X9uglFfGBzZezSWRMU%2F8CUnofrPEBJwsOixxtbmLD9ODp7yq6ezqdhlq7irwYmTOOWWqKA%3D%3D&Expires=1771505772) - Matthias Gruber Independent researcher ORCID 0009-0005-9697-1665 Correspondence matthiasmatthiasgrub...

3. [[2203.14081] Fermion picture for cellular automata](https://arxiv.org/abs/2203.14081) - by C Wetterich · 2022 · Cited by 10 — We discuss large classes of automata that are equivalent to di...

4. [Fermionic quantum field theories as probabilistic cellular ...](https://link.aps.org/doi/10.1103/PhysRevD.105.074502) - by C Wetterich · 2022 · Cited by 14 — A class of fermionic quantum field theories with interactions ...

5. [Fermion picture for cellular automata](https://arxiv.org/pdf/2203.14081.pdf) - by C Wetterich · 2022 · Cited by 10 — We discuss large classes of automata that are equivalent to di...

6. [Cellular automaton for spinor gravity in four dimensions](https://arxiv.org/abs/2211.09002) - by C Wetterich · 2022 · Cited by 7 — We construct an automaton that represents a discrete model of s...

7. [Quantum fermions from classical bits - The Royal Society](https://royalsocietypublishing.org/rsta/article/380/2216/20210066/112024/Quantum-fermions-from-classical-bitsQuantum) - by C Wetterich · 2022 · Cited by 13 — A simple probabilistic cellular automaton is shown to be equiv...

8. [Wolfram Physics Project](https://wolframinstitute.org/research/wolfram-physics-project) - The Wolfram Physics Project seeks to redefine our understanding of the universe through the developm...

9. [Are you saying that the universe is a cellular automaton?](https://www.wolframphysics.org/questions/scientific-general-interest/are-you-saying-that-the-universe-is-a-cellular-automaton/) - No. Cellular automata are very useful models for many things, and provided the intuition that led to...

10. [The Wolfram Physics Project: A One-Year Update](https://writings.stephenwolfram.com/2021/04/the-wolfram-physics-project-a-one-year-update/) - An update from Stephen Wolfram on the Physics Project. Exploration of models, connections to existin...

11. [The Cellular Automaton Interpretation of Quantum Mechanics](https://books.google.com/books/about/The_Cellular_Automaton_Interpretation_of.html?id=ctlCDwAAQBAJ) - This book presents the deterministic view of quantum mechanics developed by Nobel Laureate Gerard 't...

12. [The Cellular Automaton Interpretation of Quantum Mechanics](https://arxiv.org/abs/1405.1548) - by G Hooft · 2014 · Cited by 19 — This book is an overview of older material, but also contains many...

13. ['t Hooft on Cellular Automata and String Theory](https://www.math.columbia.edu/~woit/wordpress/?p=5022) - One of 't Hooft's motivations is a very common one, discomfort with the non-determinism of the conve...

14. [Gerard 't Hooft - The Cellular Automaton Interpretation of ...](https://phlconnect.ched.gov.ph/admin/uploads/add217938e07bb1fd8796e0315b88c10/2016BookTheCellularAutomatonInterpreta.pdf) - by G Hooft · Cited by 295 — This book is an overview of older material, but also contains many new o...

15. [The Cellular Automaton Interpretation of Quantum Mechanics](https://www.youtube.com/watch?v=a7xw0p4WfDs) - A cellular automaton is basically what the word says you divide space into a grid.

16. [The Cellular Automaton Interpretation of Quantum Mechanics](https://arxiv.org/pdf/1405.1548.pdf) - by G Hooft · 2014 · Cited by 28 — This book is an overview of older material, but also contains many...

17. [[cond-mat/0404617] String-net condensation: A physical ...](https://arxiv.org/abs/cond-mat/0404617) - by MA Levin · 2004 · Cited by 1830 — Thus, string-net condensation provides a mechanism for unifying...

18. [Topological order and long range entanglement](https://indico.ph.ed.ac.uk/event/5/attachments/491/543/Wen.pdf) - → string-net condensation Levin-Wen 05 (string-net liquid). → |Φstringi has long-range entanglement ...

19. [[0801.0861] Quantum Graphity: a model of emergent locality](https://arxiv.org/abs/0801.0861) - by T Konopka · 2008 · Cited by 256 — Quantum graphity is a background independent model for emergent...

20. [Quantum graphity: A model of emergent locality](https://link.aps.org/doi/10.1103/PhysRevD.77.104029) - by T Konopka · 2008 · Cited by 257 — Quantum graphity is a background-independent model for emergent...

21. [Quantum cellular automata and quantum field theory in two spatial ...](https://discovery.researcher.life/article/quantum-cellular-automata-and-quantum-field-theory-in-two-spatial-dimensions/36b56239dc7e33e3be3b85e614055b6a) - This QCA/QFT correspondence has both theoretical and practical applications, but there are obstacles...

22. [Fermion Doubling in Lattice Field Theory](https://www.emergentmind.com/topics/fermion-doubling) - Fermion doubling is the emergence of extra chiral fermion modes from discretizing space, as mandated...

23. [Action principle for cellular automata and the linearity of ...](https://link.aps.org/doi/10.1103/PhysRevA.89.012111) - by HT Elze · 2014 · Cited by 56 — We introduce an action principle for a class of integer-valued cel...

24. [A Cyclic Model of the Universe](http://ui.adsabs.harvard.edu/abs/2002Sci...296.1436S/abstract) - by PJ Steinhardt · 2002 · Cited by 972 — We propose a cosmological model in which the universe under...

25. [A Cyclic Model of the Universe](https://arxiv.org/abs/hep-th/0111030) - by PJ Steinhardt · 2001 · Cited by 966 — We propose a cosmological model in which the universe under...

26. [[1903.11544] The causal set approach to quantum gravity](https://arxiv.org/abs/1903.11544) - by S Surya · 2019 · Cited by 393 — The causal set theory (CST) approach to quantum gravity postulate...

27. [Hypergraph Rewriting](https://wolframinstitute.org/research/hypergraph-rewriting) - This project aims to uncover the behaviour of such mysterious objects. Project Overview.

