# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-16 (Session 60)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Repo reorganization, paper audit, implementation folder setup

## Current State
- **Active Task**: Session 60 COMPLETE. Next: fix 12 trimmed paper audit issues.
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
3. **NEXT SESSION**: Fix 12 audit issues in trimmed paper (`paper/trimmed/noc/four-model-theory-noc.md`):
   - Cut ~2-3k body words (12,157 → 9-10k)
   - Cut abstract to ≤250 words (currently 317)
   - Add Conflict of Interest + Author Contributions (CRediT) sections
   - Fix 4 citation gaps (Gazzaniga 1965, Treisman & Gelade 1980, Algom/Shriki year, Anthropic year)
   - Remove 2 duplicate refs (Gazzaniga 2000, Graziano 2024)
   - Sort references alphabetically
   - Add figure cross-references in text
   - Fix Friston no-year, Van Rullen → Van Rullen & Koch
   - Remove orphaned Dehaene ref
   - Add DOIs (time permitting)
4. After fixes: .docx conversion (last step before NoC resubmission)
5. Implementation folder ready for Phase 1 work (concept extraction)
