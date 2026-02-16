# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-16 (Session 60)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Repo reorganization, paper audit, implementation folder setup

## Current State
- **Active Task**: Session 60 in progress
- **Progress**:
  - Moved root scripts to `scripts/` subfolder
  - Created `scripts/push.sh` for dual-push (private=all, public=filtered)
  - Wrote NoC highlights file (5 bullet points)
  - Full audit of trimmed paper completed — 12 critical issues found
  - Created `/home/jeltz/aIware.implementation/` with cc-mirror setup, 7 agents, papers copied
  - Implementation project: git initialized, private remote only, pushes to `implementation` branch

## Repo Reorganization
- **Public (origin)**: Excludes `tmp/`, `scripts/`, `session-context.md`, `docs/`
- **Private**: Gets everything
- **Push script**: `scripts/push.sh` handles the split automatically

## Paper Audit Key Findings
- Body: ~12,157 words (need 9-10k) — cut ~2-3k
- Abstract: 317 words (need ≤250) — cut ~70
- Missing: Conflict of Interest, Author Contributions (CRediT)
- 4 citation gaps, 2 duplicates, unsorted references, no DOIs
- Figures need explicit cross-references in text

## Implementation Folder
- Path: `/home/jeltz/aIware.implementation/`
- Git: private remote → `implementation` branch on aIware-private
- Agents: research-analyst, knowledge-synthesizer, ai-engineer, llm-architect, python-pro, data-scientist, documentation-engineer
- Papers copied as read-only reference

## Recovery Instructions
1. Read this file
2. PsyArXiv preprints still awaiting moderation (24-72h from 2026-02-16)
3. Next: Fix audit issues in trimmed paper, then .docx conversion
4. Implementation folder ready for Phase 1 work (concept extraction)
