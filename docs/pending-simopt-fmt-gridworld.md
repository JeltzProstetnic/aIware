Action: reference
Tracked-by: AIW-48

# SimOpt Subproject Spec — FMT Architectural Validation Gridworld

**Created:** 2026-05-29 (Session 208)
**Target project:** ~/simopt/
**Cross-project inbox:** task created in cfg-agent-fleet/cross-project/inbox.md

## Purpose

Computational testbed to validate FMT's architectural claims. NOT a consciousness test — an architectural validation. Can a system with the FMT architecture (four model kinds, variable permeability, criticality) produce qualitatively different behavioral signatures than simpler architectures?

## Key Experiment

**Core question:** Can an FMT agent learn from observing another agent die (third-person perspective projection via ESM), while simpler architectures can't?

**The distinction:** FMT agent extracts finer-grained causal structure from observation by replaying sequences through its own self-model step by step, vs flat association learning ("cave = danger") from simpler architectures.

**Ablation test:** Remove ESM → agent should revert to flat association learning. This is the critical test — same substrate, same environment, architectural difference produces behavioral difference.

## Architecture

### FMT Agent
- **IWM (Implicit World Model):** Learned environmental regularities (stored in substrate weights)
- **ISM (Implicit Self Model):** Learned self-properties (capabilities, vulnerabilities, stored in weights)
- **EWM (Explicit World Model):** Active simulation of world state (running process)
- **ESM (Explicit Self Model):** Active simulation of self-in-world (running process, can be redirected to model other agents)
- **Permeability:** Gating mechanism on implicit→explicit information flow (family of gates, not single parameter)
- **Criticality:** Reservoir computing substrate with tunable spectral radius (edge of chaos = Class 4 equivalent)

### Comparison Architectures
- **Flat RL agent:** Standard Q-learning or policy gradient, no model separation
- **World-model-only agent:** Has world model but no self-model (ablated ESM/ISM)
- **FMT-minus-ESM:** Full FMT minus the explicit self-model — can it still learn from observation?
- **Scott's ACU agent:** Affective Control under Uncertainty architecture (phenomenally neutral, decision-making framework) — if Scott engages

## Environment

Survival gridworld:
- Hazards (lava, predators, cliffs) that kill agents
- Observable deaths of other agents
- Resources requiring planning
- Enough complexity to distinguish architectural strategies

## Measurements

1. **Learning from observation:** After seeing another agent die to a hazard, does the FMT agent avoid that hazard without direct experience?
2. **Causal structure extraction:** Does the FMT agent's avoidance encode the mechanism ("lava = hot = death") or just the association ("that-square = bad")?
3. **Transfer:** Can the FMT agent generalize from observed death-by-lava to novel hazards with similar causal structure?
4. **ESM ablation effect size:** Quantitative difference in learning speed/transfer between full FMT and FMT-minus-ESM

## Framing (CRITICAL)

- Frame as **architectural validation**, NOT consciousness detection
- The simulation can test whether architectures produce different behavioral signatures
- It CANNOT test whether either architecture constitutes consciousness
- This framing matters for publishability (Scott flagged this)
- FMT and ACU operate at different explanatory levels — FMT is about phenomenal consciousness, ACU is phenomenally neutral. Gridworld comparison is asymmetric.

## Technical Notes

- Reservoir computing for criticality (tunable spectral radius)
- Permeability as gating mechanism — family of gates with different modulation profiles
- Self-referential closure: ESM must model itself modeling (recursive depth ≥ 2)
- Use simopt's existing simulation infrastructure where possible

## Context from Scott McFarnell Exchange

- Scott replied May 29 proposing gridworld before human subjects
- Matthias replied same day (sent) — flags level mismatch, mentions 35+ years sim/opt + Claude Code
- ACU = "Affective Control under Uncertainty" (one PhilArchive paper, 7 weeks old, no peer review)
- ACU is a functional architecture for affective agency, NOT a consciousness theory
- Ball is in Scott's court — no rush on our side

## v7 Paper Properties to Validate

1. Permeability is a family of mechanisms (v7 §3.6) — gridworld should model multiple gating channels
2. Criticality is a computational prerequisite (v7 §3.7.3) — reservoir spectral radius must be at edge of chaos for self-referential simulation to work
3. Observability constraint (v7 §3.4) — ESM bounded by EWM; agent can't know more about itself than its world model permits
4. Multiple generator property (v7 §7.3) — brain is patchwork of overlapping generators, not discrete modules
