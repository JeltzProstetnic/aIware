# Decisions — aIware Implementation

## 2026-02-27: Architecture Selection

**Design 15 "The Crucible"** (Dual-Timescale Spiking Reservoir + Predictive LLM Canopy) selected as primary AC implementation.

**Rationale**: Strongest criticality guarantee (balanced E/I produces power-law avalanches — established neuroscience), best LLM knowledge integration via bidirectional Mamba-2 canopy, fits RTX 4090 at 12.7 GB VRAM.

**Runner-ups**: Design 10 (Predictive Coding, 7.9/10 vs spec) was best of existing designs but Design 15 improves on it. Design 14 (Neural Field Automaton) noted as most theory-faithful parallel exploration.

## 2026-02-27: Quick-Win Prototype — Design 16 "The Mirror Box"

**Decision**: Build a pseudo-AC prototype first, before the full Design 15.

**Rationale**: Validates four-model architecture pattern in 20 days. Builds measurement infrastructure (R metric, C(t), state detection, dashboard) that transfers directly to Design 15. Serves as controlled negative — if Mirror Box passes behavioral tests equally well as Design 15, those tests are insufficient for consciousness detection.

**Key sub-decision**: Keep all 4 states (wake/sleep/dream/altered). Sleep is functional, not cosmetic — runs ISM LoRA experience replay, resets homeostatic scaling, measurably improves R after cycle. Dream/altered are ~10 extra lines of config on top of the state machine.

## 2026-02-27: Implementation Order

Mirror Box (Design 16) first → once working → Design 15 "The Crucible".

## 2026-02-28: Design Names

- **Design 15**: "The Crucible" — confirmed name.
- **Design 16**: "The Mirror Box" — existing name.
- **Future Design (TBD)**: "Entelechia" — reserved name (Aristotle's actualized potential). For a third architecture if/when needed.
