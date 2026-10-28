# James-Stein Paradox and Entanglement in SB-HC4A

**Created:** 2026-06-03 (Session 210)
**Status:** Research synthesis — not yet incorporated into paper
**Tracked-by:** (no backlog item yet — create when ready to write section)

## Research Question

Can quantum entanglement be grounded in the James-Stein paradox if elementary particles are Planck-scale singularities on a shared computational substrate (SB-HC4A §5.5-5.6)?

## Core Argument

In SB-HC4A, every particle-singularity is a Bekenstein-saturated information boundary on a shared Class 4 automaton substrate. Their state-descriptions are not elements of a product Hilbert space — they are configurations on a common substrate. This is the ontological condition under which James-Stein applies: independent per-particle estimators are inadmissible when parameters share a common prior (the automaton's global state), and the joint estimator — shrinking toward the global vacuum — is strictly superior.

The entangled state is the admissible estimator; the product state is the inadmissible one.

## Key Literature

### Directly Relevant
- **Salmon, Strelchuk & Arvidsson-Shukur (2024)** — "James-Stein Estimation in Quantum Gaussian Sensing" (arXiv:2404.02203). JS applied to quantum Gaussian states. Entanglement improves estimator but reduces advantage over MLE; noise restores advantage.
- **Ferrie & Blume-Kohout (2018)** — "Maximum likelihood quantum state tomography is inadmissible" (arXiv:1808.01072). MLE dominated under fidelity, MSE, relative entropy. "Hedging" (mixing toward maximally mixed state) = shrinkage toward vacuum.
- **McCane & Dryden (2022)** — "The Stein Effect for Fréchet Means" (Annals of Statistics 50(6)). Stein shrinkage works in CAT(0) / Hadamard spaces. Fails in positively curved spaces.
- **Brown (1971)** — "Admissible Estimators, Recurrent Diffusions, and Insoluble Boundary Value Problems" (Ann. Math. Statist. 42(3):855-903). Admissibility of MLE ↔ recurrence of Brownian diffusion. Recurrent for d ≤ 2, transient for d ≥ 3 → explains the (d-2) threshold rigorously.
- **Rubio & Dunningham (2020)** — "Physics-inspired forms of the Bayesian Cramér-Rao bound" (arXiv:2007.04849). Minimax estimation = finding ground state of Schrödinger equation, Fisher info = potential. Formal identity, not analogy.
- **Sun & Zhang (2019)** — "Bell Inequality in the Holographic EPR Pair" (arXiv:1612.09513, Phys. Lett. B). CHSH correlators computed holographically via Schwinger-Keldysh. Bell violation reproduced from bulk string fluctuations in AdS/CFT.

### Supporting (holographic/boundary)
- **Van Raamsdonk (2010)** — spacetime connectivity from entanglement (arXiv:1005.3035)
- **Maldacena & Susskind (2013)** — ER=EPR (arXiv:1306.0533)
- **Penington (2020)** — island formula, measurement updates entanglement wedge (arXiv:1905.08255)
- **Almheiri et al. (2020)** — Page curve (arXiv:1911.09581)
- **Engelhardt & Wall (2015)** — quantum extremal surfaces

### Disambiguation
- **"Quantum Stein's lemma"** is a DIFFERENT theorem (hypothesis testing error exponents, not shrinkage estimation). Cite carefully.

## Established Connections

1. **Product states are inadmissible estimators** — Novel framing, defensible via Ferrie-Blume-Kohout
2. **Shrinkage toward vacuum** — Partial formal grounding via Rubio-Dunningham (minimax ≡ ground state) and harmonic prior (Green's function of Laplacian)
3. **d ≥ 3 threshold** — Rigorous via Brown 1971 (Brownian recurrence)
4. **σ² → ∞ → thermal equilibrium** — Qualitatively correct, shared limiting behavior
5. **Measurement updates boundary state** — Supported by island formula literature

## Corrections to Initial Analysis

### Entanglement monogamy / (d-2) — DOES NOT WORK
CKW monogamy FAILS for d > 2 (qutrit systems violate it), while JS coefficient GROWS with d. Dimensional scaling goes in OPPOSITE directions. Drop from argument.

Reference: arXiv:2201.00366 (monogamy review); Jin et al. 2022.

### High ||θ||² ≠ "less entangled"
High-energy particles CAN be highly entangled (Bell pairs at LHC, Afik & de Nova 2022, PRD). Correct mapping: high ||θ||² → better SNR → estimation needs no regularization. About estimation quality, not entanglement structure.

### 2D topological threshold — COINCIDENTAL
The d = 2 threshold appears in both JS (Brown's recurrence) and 2D topological physics (anyonic statistics from braid group), but for independent mathematical reasons. Numerical coincidence, not structural identity.

## The Honest Gap — Mathematical Program

The configuration space of Planck-scale singularity boundaries must support a James-Stein-type inadmissibility theorem. Requirements:

1. **Dimension ≥ 3** in parameter space — satisfied (Standard Model: 17 particle types; O(1) bits must mean ≥ 2 bits / 4+ states)
2. **Metric space structure** with non-positive curvature (CAT(0)) for McCane-Dryden, OR discrete Laplacian for Diaconis-Holmes approach
3. **Loss function** with right convexity — QFI-based relative entropy is natural candidate

### Problem: Levin-Wen fusion graphs are NOT CAT(0)
Non-abelian anyon models have positive combinatorial curvature from vertex branching. McCane-Dryden doesn't transfer directly.

### Two routes forward:
(a) Embed configuration space into Hadamard space (possible via Bourgain-type embeddings with O(log n) distortion, but distortion may destroy loss structure)
(b) Build discrete Laplacian-based shrinkage theorem on excitation graph (Diaconis-Holmes framework, Foata-Zeilberger discrete harmonic analysis)

### Minimum structure needed:
- Notion of "gradient" or harmonic function on the space
- Superharmonicity of shrinkage correction
- Possible in weighted graph spaces via discrete Laplacians

## Strongest Formal Chain

Fisher info as potential → minimax estimation as ground-state problem → harmonic prior as Green's function → shrinkage toward vacuum

Combined with Ferrie-Blume-Kohout (quantum MLE inadmissibility) and SB-HC4A ontology (shared substrate → non-product Hilbert space):

> Independent per-particle state estimation is inadmissible. The admissible joint estimator shrinks toward the global vacuum. SB-HC4A provides the ontological reason why: particles are configurations on a shared Bekenstein-saturated substrate, not independent systems in a product Hilbert space. The entangled state IS the admissible estimator.

## What This Adds to SB-HC4A (if formalized)

1. **Why correlations have specific strength** — shrinkage coefficient w = (d-2)σ²/||θ||² gives the quantitative skeleton (not just "correlations exist")
2. **Decoherence mechanism** — high thermal noise (σ² → ∞) caps shrinkage at w=1, everything collapses to vacuum → classical behavior
3. **Statistical mechanics bridge** — connects automaton substrate to measurable quantum statistics via information geometry

## Paper Integration Plan

If this becomes a new section or appendix in SB-HC4A:
- Present as a conjecture with supporting structure, not as a proven result
- Cite Salmon et al. 2024, Ferrie-Blume-Kohout 2018, Brown 1971, McCane-Dryden 2022, Rubio-Dunningham 2020
- Be explicit about the Euclidean/CAT(0) gap
- Do NOT claim monogamy connection (dimensional scaling is opposite)
- Do NOT claim high-energy → less entangled (empirically wrong)
