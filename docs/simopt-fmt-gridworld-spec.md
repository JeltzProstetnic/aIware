# FMT Architectural Validation Gridworld — Spec Reference

**Canonical spec location:** `~/simopt/docs/plans/2026-05-29-fmt-gridworld.md`
**SimOpt backlog items:** SIM-47 through SIM-52
**Ingested:** 2026-05-29 (simopt WSL session, inbox task closed)

## Source Documents (aIware)

- **Formalization paper:** `paper/fmt_formal/fmt-formalization.md` (9200 words, v7-aligned)
  - Phase 4 (§8) describes the gridworld as computational validation — results to be incorporated before publication
  - Key sections: §3.3 (gating family), §4.4 (criticality prerequisite), §5 (ESM redirection), §6.2 (observability constraint)
- **Design rationale:** `docs/decisions.md` — "Gridworld vs Cellular Automaton — Instrument Choice (2026-05-29)"
- **Original pending file:** `docs/pending-simopt-fmt-gridworld.md` (Session 208 context, now reference-only)

## Three Predictions (summary)

1. **ESM ablation → categorical behavioral difference** (causal-structure extraction vs flat association)
2. **Sub-critical dynamics → categorical collapse of self-referential processing** (phase transition, not gradual)
3. **EWM coverage ablation → proportional ESM degradation** (observability constraint)

## Key Design Insight (Session 209)

Gridworld and cellular automaton are mathematically the same object. The agent/environment split is semantic, not structural. We use the gridworld because it communicates to non-mathematicians — we're demonstrating what a self-model buys, not how the agent/world boundary emerges. Hazard families (thermal, fall, movement-based) are required to discriminate architectures via causal-structure transfer.
