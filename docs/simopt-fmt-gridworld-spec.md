# FMT Architectural Validation Gridworld — Specification for SimOpt

**Source project:** aIware
**Target project:** ~/simopt/
**Created:** 2026-05-29 (Session 209)
**Formalization reference:** `paper/fmt_formal/fmt-formalization.md` (aIware repo, 9200 words, v7-aligned)

## What This Is

A computational testbed to validate FMT's architectural claims via ablation experiments in a survival gridworld. NOT a consciousness test — an architectural validation. The question: does the FMT architecture produce qualitatively different behavioral signatures than simpler architectures?

This spec is written for the simopt project to consume directly. It provides the mathematical definitions, architectural requirements, and measurement protocol derived from the formalization paper.

## The Three Predictions to Test

These are the sharp, falsifiable predictions from the formalization. Each maps to a specific ablation.

### Prediction 1: ESM ablation produces categorical behavioral difference

**Source:** Formalization §5 (ESM Redirection Dynamics)

**Claim:** An FMT agent with a self-model (ESM) extracts finer-grained causal structure from observing another agent's death than an architecturally identical agent without the ESM. The difference is categorical (causal-structure extraction vs. flat association learning), not merely quantitative (faster learning).

**Test:** FMT agent vs. FMT-minus-ESM agent. After observing another agent die to a hazard:
- FMT agent should encode the *mechanism* ("lava = hot = death") and transfer to novel hazards with similar causal structure
- FMT-minus-ESM agent should encode only the *association* ("that-square = bad") and fail to transfer

**Measurement:** Transfer success rate to novel hazards with same causal structure but different appearance. Effect size between full-FMT and FMT-minus-ESM.

### Prediction 2: Sub-critical dynamics collapse self-referential processing categorically

**Source:** Formalization §4.4 (Criticality as Logical Prerequisite)

**Claim:** Self-referential simulation is a universal computation. Universal computation requires Class 4 dynamics. Therefore, below the criticality threshold, the self-model cannot sustain universal computation and observational learning should fail — regardless of architecture.

**Test:** FMT agent with reservoir spectral radius tuned from subcritical (< 1.0) through critical (~1.0) to supercritical (> 1.0). At each setting, test observational learning.

**Measurement:** Observational learning success as a function of spectral radius. The prediction is a *phase transition* (sharp threshold), not a gradual curve. Plot learning performance vs. spectral radius — the formalization predicts a step function near σ ≈ 1, not a sigmoid.

### Prediction 3: EWM coverage ablation degrades ESM proportionally

**Source:** Formalization §6.2 (Observability Constraint: O_ESM ⊆ S_EWM)

**Claim:** The explicit self-model cannot represent aspects of the system that the explicit world model doesn't cover. If you reduce what the EWM models about the environment, the ESM's self-knowledge should degrade proportionally — because the ESM is bounded by the EWM's observational horizon.

**Test:** Systematically ablate EWM coverage (hide environmental features from the world model). Measure ESM's self-knowledge accuracy (can the agent predict its own behavior in the hidden domains?).

**Measurement:** Correlation between EWM coverage fraction and ESM self-prediction accuracy. The formalization predicts a tight linear or slightly sub-linear relationship — not independence.

## Agent Architecture Specification

### FMT Agent

Implements the four-model architecture with the following components mapped to formalization sections:

#### Implicit World Model (IWM)
- **What:** Learned environmental regularities stored in substrate weights
- **Formalization:** The world-knowledge partition of W (connectivity matrix), §4.1
- **Implementation:** Learned weights in the reservoir/network that encode environment statistics

#### Implicit Self Model (ISM)
- **What:** Learned self-properties (capabilities, vulnerabilities) stored in substrate weights
- **Formalization:** The self-knowledge partition of W, §4.1
- **Implementation:** Learned weights encoding agent's own capabilities, movement constraints, vulnerability profile

#### Explicit World Model (EWM)
- **What:** Active simulation of world state — a running process, not stored data
- **Formalization:** EWM(t) = Π_EWM · x(t), projection of state vector, §4.1
- **Implementation:** Active predictive process generating next-state predictions for the environment

#### Explicit Self Model (ESM)
- **What:** Active simulation of self-in-world — running process, can be redirected to model other agents
- **Formalization:** ESM(t) = Π_ESM · x(t), §4.1. Self-referential closure: Φ(m*) = m*, §6.4
- **Implementation:** Active process that models the agent's own modeling activity. Must achieve recursive depth ≥ 2 (the agent models itself modeling). For observational learning: ESM replays observed sequences through the agent's own self-model step by step.

#### Gating Family G (Permeability)
- **What:** Family of channel-specific gating mechanisms modulating implicit→explicit information flow
- **Formalization:** G = {g_c}, §3.3. Composite: g(W, x(t)) = ∏_{c ∈ C} g_c(W, x(t))
- **Implementation:** At minimum 2-3 distinct gating channels (e.g., "attention," "arousal," "domain-specific"). Each channel independently modulable. The gridworld doesn't need to map these to neurotransmitter systems — the structural property is that permeability is multi-channel, not single-knob.

#### Criticality (Reservoir)
- **What:** Substrate dynamics at edge of chaos
- **Formalization:** σ ∈ [σ_low, σ_high] where σ ≈ 1 (branching ratio), §4.2-4.4
- **Implementation:** Reservoir computing with tunable spectral radius. σ < 1 = subcritical (activity dies), σ ≈ 1 = critical (Class 4), σ > 1 = supercritical (activity explodes).

#### Observability Constraint
- **What:** ESM bounded by EWM — agent can't know more about itself than its world model permits
- **Formalization:** O_ESM ⊆ S_EWM, §6.2
- **Implementation:** ESM receives information only through EWM projections, never directly from substrate. To ablate: restrict EWM's observable features.

### Comparison Architectures

| Agent | Architecture | Purpose |
|-------|-------------|---------|
| Flat RL | Standard Q-learning or policy gradient, no model separation | Baseline — no internal models |
| World-model-only | Has EWM but no ESM/ISM | Tests whether world-modeling alone suffices for observational learning |
| FMT-minus-ESM | Full FMT architecture minus the explicit self-model | Critical ablation — isolates ESM contribution |
| ACU agent (optional) | Affective Control under Uncertainty architecture | If McFarnell engages — phenomenally neutral, decision-making framework |

## Environment Specification

Survival gridworld with:
- **Hazards** (lava, predators, cliffs) that kill agents — must have diverse causal mechanisms to test transfer
- **Observable deaths** of other agents — the FMT agent watches, doesn't experience directly
- **Resources** requiring planning (food, shelter, tools)
- **Novel hazards** that share causal structure with known hazards but differ in appearance — critical for Prediction 1 transfer test
- **Sufficient complexity** to distinguish architectural strategies — avoid toy environments where flat RL matches FMT

## Measurement Protocol

### Primary metrics
1. **Observational learning rate:** Episodes to criterion performance after observing (not experiencing) a hazard type
2. **Causal transfer score:** Performance on novel hazards sharing causal structure with observed hazards
3. **ESM ablation effect size:** Cohen's d between full-FMT and FMT-minus-ESM on metrics 1-2
4. **Criticality phase transition sharpness:** Derivative of learning performance with respect to spectral radius near σ ≈ 1
5. **Observability constraint compliance:** Correlation(EWM coverage fraction, ESM self-prediction accuracy)

### Secondary metrics
- Total reward over episodes (standard RL comparison)
- Survival duration
- Exploration efficiency
- Self-prediction accuracy (can the agent predict its own next action?)

## Framing Constraint (CRITICAL)

This simulation tests **architectural claims**, not **consciousness claims**. The paper will say:

> "The gridworld demonstrates that the FMT architecture produces qualitatively different behavioral signatures from simpler architectures under controlled ablation. It does not and cannot demonstrate that either architecture constitutes consciousness."

This framing is essential for publishability. Do not claim consciousness detection.

## Integration with Formalization Paper

The gridworld results will be incorporated into the formalization paper's Phase 4 section before publication. The formalization paper (currently at `paper/fmt_formal/fmt-formalization.md` in aIware) already references this gridworld as its computational validation component. Results, figures, and statistical analyses from the simulation should be formatted for direct inclusion.

## Technical Recommendations

- **Python + gymnasium** for the gridworld environment (standard RL infrastructure)
- **Reservoir computing** via reservoirpy or custom implementation for criticality-tunable substrate
- **Ablation framework** built in from the start — every component must be independently removable
- **Reproducibility:** Fixed random seeds, configuration files for all hyperparameters, Docker or conda environment spec
- **Logging:** All metrics logged per-episode for statistical analysis. Store raw trajectories for post-hoc analysis of causal structure extraction.

## Open Questions for SimOpt

1. What reservoir computing library? (reservoirpy is mature; custom gives more control)
2. Grid size and hazard density — needs pilot runs to calibrate difficulty
3. How to operationalize "causal structure extraction" vs "flat association" in the agent's internal representations? (Candidate: representational similarity analysis on hidden states)
4. Multi-agent or single-agent-with-replays for observational learning?
5. How many episodes for statistical power on the phase transition test?
