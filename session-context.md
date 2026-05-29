# Session Context

## Session Info
- **Last Updated**: 2026-05-29T17:55+0200
- **Machine**: WSL
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: AIW-68 — align FMT formalization paper with v7 paper changes

## Current State
- **Active Task**: AIW-68 (FMT formalization v7 alignment)
- **Progress** (use `- [x]` checkbox for each completed item):
  - [x] §3.3 — Permeability gating operator decomposed into channel-specific family (serotonergic, GABAergic, dopaminergic, noradrenergic)
  - [x] §4.1 — Cortical automaton clarified as canonical example, not general requirement (substrate-neutral framing)
  - [x] §4.4 — New section: Criticality as Logical Prerequisite (self-ref → universal computation → Class 4 deductive chain)
  - [x] §4.5 — Two-Threshold Formalization updated with logical-prerequisite framing
  - [x] §6.2 — New section: Observability Constraint (O_ESM ⊆ S_EWM, three formal consequences)
  - [x] §2.2 — Model density ρ connected to multiple-generator architecture claim
  - [x] Abstract, keywords, §1.3 outline, §10 conclusion — all updated with new sections and cross-references
  - [x] All internal cross-references renumbered (§4.5→§4.6, §6.2→§6.3, §6.3→§6.4, §6.4→§6.5, §6.5→§6.6)
- **Pending**: Commit, update backlog

## Key Decisions
- All three AIW-68 gaps addressed: permeability family, observability constraint, criticality prerequisite
- Paper grew from ~6,000 to ~8,925 words (69 insertions, 21 deletions)
- Observability constraint placed in §6 (self-referential closure) rather than §5 (ESM) because it's architecturally about the closure relationship between ESM and EWM

## Recovery Instructions
If session terminates: all edits are in `paper/fmt_formal/fmt-formalization.md`. Not yet committed. Run `git diff` to review, then commit.

## Next Session Task
<!-- Fill this in during shutdown if the next session should continue specific work.
     Required fields: task: true|false, file: <path>, description: <text>
     The file: MUST point to a dedicated file (e.g., docs/pending-*.md), NEVER to session-context.md.
     rotate-session.sh extracts this section to next-session-task.md automatically. -->
