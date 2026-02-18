# SB-HC4A Semi-Formal Specification

**Status**: Working notes extracted from Session 65 conversation. Not a paper — a formalization attempt to be developed.

**Source**: `tmp/cosmological-model-conversation-session65.md`

---

## Definition

**Definition (SB-HC4A).** A *Singularity-Bounded Holographic Class 4 Automaton* is a dynamical system U = (S, R, B) where:
- S is a state space on a d-dimensional lattice (or continuous manifold)
- R is a holographic rule set: R encodes (d+1)-dimensional information in d-dimensional structure
- B is a singularity boundary: a scale-invariant surface of maximum information density (Bekenstein-saturated) that bounds the computational domain at every scale
- U operates at Class 4 dynamics (branching ratio σ ~ 1, Lyapunov exponent λ_max ~ 0)
- The output of U is holographic: emergent large-scale structure encodes non-local information

---

## Axioms

**Axiom 1 (Ontological Necessity).** Something exists. Nothing is not a possible state of affairs.

**Axiom 2 (Computational Character).** Whatever exists has dynamical behavior classifiable within the five-class computational hierarchy.

**Axiom 3 (Criticality Stability).** A Class 4 system is the unique computational class that:
(a) supports universal computation,
(b) self-maintains criticality through self-organized criticality, and
(c) contains Classes 1–3 as subprocesses.

**Axiom 4 (Information Bound).** Information propagation speed is bounded by c. Information density is bounded by the Bekenstein bound. Information is conserved (equivalent to energy conservation if E = I).

**Axiom 5 (Holographic Encoding).** The boundary of a d-dimensional region encodes all information in the region's interior on its (d−1)-dimensional surface (the holographic principle).

---

## Propositions

**Proposition 1 (Class 4 Universe).** From A1, A2, A3: The universe operates at Class 4. (Argument: Class 1–3 are insufficient for universal computation/consciousness. Class 5 makes physics impossible and our existence arbitrary. Class 4 is the unique stable attractor for a self-maintaining complex system.)

**Proposition 2 (Quasi-Infinity).** From A4: The universe is effectively bounded for any observer by information horizons. These horizons are singularities — surfaces of maximum information density.

**Proposition 3 (Scale-Invariant Singularity Structure).** From P1 (Class 4 → self-similar) and P2: The singularity structure is self-similar across all scales. The Planck-scale singularity, the particle "point," the event horizon, and the cosmological horizon are all instances of the same Bekenstein-saturated information boundary.

**Proposition 4 (Self-Referential Closure).** From A5 (holographic encoding) and P1 (Class 4): The universe is an SB-HC4A — a holographic Class 4 automaton whose rules are holographic, whose dynamics are Class 4, and whose output is holographic. This is a self-referential fixed point: Φ(U) = U, where Φ is the "compute the output" operator.

**Proposition 5 (Inexpressibility).** From P4 (self-referential closure) and Gödel's incompleteness: The SB-HC4A cannot be fully specified by any formal system that is a proper subsystem of itself. The "Weltformel" is not an equation but the *process* of the automaton — it can only be expressed by running it.

**Proposition 6 (Consciousness-Cosmology Symmetry).** The FMT four-model architecture is a local, scale-reduced instance of the SB-HC4A pattern:

| SB-HC4A property | FMT property |
|---|---|
| Singularity boundary (information-opaque) | Implicit-explicit boundary (phenomenally opaque) |
| Observable interior (the "simulation") | Explicit models (the conscious simulation) |
| Holographic rule structure | Distributed/holographic implicit knowledge |
| Class 4 dynamics | Cortical criticality |
| Self-referential closure (U computes U) | Self-referential closure (ESM models ESM) |
| Conservation of E/I across boundary | Conservation of information across implicit-explicit split |
| Inexpressibility from within | Meta-Problem (consciousness cannot explain its own substrate) |

**Proposition 7 (Necessity).** The SB-HC4A is the unique structure consistent with all axioms simultaneously. It must exist because:
- (A1) something must exist
- (A3) only Class 4 is self-maintaining and universal
- (A5) holographic encoding is the most efficient information storage
- (P4) self-referential closure is the only self-consistent configuration for a system that computes its own existence

---

## Open Formalization Questions

### 1. Making "Class 4" Mathematically Precise
Wolfram's classification is empirical, not axiomatic. For the SB-HC4A to be rigorous, "Class 4" needs a mathematical definition independent of Wolfram's visual classification. Candidates:
- **Branching ratio** σ ∈ [σ_low, σ_high] (from criticality literature)
- **Maximum Lyapunov exponent** λ_max ~ 0 (edge of chaos)
- **Computational universality** (the system can simulate any Turing machine)
- Some combination of these

### 2. Formalizing the Holographic Rule Set
What does it mean for a rule set R to be "holographic"? Candidate definition: R is holographic if it encodes information about (d+1)-dimensional structure in a d-dimensional specification, such that local application of R at each site implicitly computes global (non-local) relationships.

### 3. Scale Invariance of Singularity Structure
The claim that singularities at all scales are "the same" needs a precise equivalence relation. Candidate: two singularity surfaces S₁ and S₂ are equivalent if they have the same information-theoretic properties:
- Both are Bekenstein-saturated
- Both are information-impermeable (no signal crosses)
- Both bound a computational domain
- Their entropy scales with surface area identically

### 4. The Fixed Point
The self-referential closure Φ(U) = U needs a rigorous definition of Φ. In the FMT formalization (Gruber, 2026b), the analogous fixed point is defined via a representation map. At the cosmological level, Φ must be the operator that maps the system state to its computed output. The fixed-point condition then states that the output IS the system — the universe computes itself.

Connection to Lawvere's fixed-point theorem (Lawvere, 1969) should be explored.

### 5. The Necessity Argument
The strongest claim — that the SB-HC4A *must* exist — requires showing that:
(a) the five axioms are not independent but entail each other under reasonable conditions, or
(b) the conjunction of the five axioms is the only self-consistent set of axioms for a physical universe.

Neither is currently demonstrated. This is the hardest formalization challenge.

---

## TODO

- [ ] Review existing work on formalizing "edge of chaos" (Langton, 1990; Bertschinger & Natschlager, 2004)
- [ ] Review Lawvere's fixed-point theorem and its applicability
- [ ] Investigate whether holographic rule structure can be formally defined for cellular automata
- [ ] Connect to AdS/CFT correspondence (Maldacena, 1998) — is the SB-HC4A a generalization?
- [ ] Explore relationship to Wheeler-DeWitt equation and its self-referential structure
- [ ] Define the equivalence relation on singularities precisely
- [ ] Investigate whether the necessity argument can be strengthened via category theory
