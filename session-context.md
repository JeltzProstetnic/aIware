# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-19 (Session 72)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Infrastructure TODOs 1-5 from Session 71

## Current State
- **Active Task**: All 5 infrastructure TODOs COMPLETE + bonus task 6
- **Needs**: Commit, push, restart (skills installed require restart)

## What Session 72 Did

### Infrastructure TODO 1: Absorb wsl-claude-setup ✅
- Copied 12 files (2,784 lines, ~90KB) to `~/claude-config/setup/`
- Structure: install scripts, helper scripts, config templates, knowledge base, README
- Updated registry.md: wsl-claude-setup marked "archived → absorbed into claude-config/setup/"
- Original repo preserved (not deleted)

### Infrastructure TODO 2: Evaluate Agent Teams ✅
- TEAM_MODE (cc-mirror) ≠ Agent Teams (Anthropic experimental)
- TEAM_MODE = orchestrator + subagents in 1 session (current setup, works well)
- Agent Teams = multiple independent sessions, peer-to-peer messaging, ~5x token cost
- They don't conflict — can coexist. Keep TEAM_MODE as default.
- Findings documented: `~/claude-config/knowledge/agent-teams-vs-team-mode.md`

### Infrastructure TODO 3: VoltAgent skills ✅
- Cloned: anthropic-skills (16 skills), voltagent-skills (catalog), obra-superpowers, trailofbits-skills, getsentry-skills
- **aIware skills** installed: docx, pdf, doc-coauthoring (in `aIware/.claude/skills/`)
- **Global skills** installed: verification-before-completion, systematic-debugging, test-driven-development, writing-plans, skill-creator, modern-python (in `~/.claude/skills/`)
- VoltAgent is a catalog pointing to external repos — key ones cloned to `~/.local/share/skill-collections/`

### Infrastructure TODO 4: Review script consolidation ✅
- Built `review_changes.py` — single tool replacing 4 overlapping scripts
- Modes: `--mode highlight` (line-level) and `--mode track` (word-level diff)
- Sources: `--against HEAD` (git), `--against markers` (HTML comments), `--against <file>` (file compare)
- Canonical location: `~/claude-config/tools/review_changes.py`
- Symlinked from `aIware/tmp/review_changes.py`
- Old scripts archived to `aIware/tmp/archive/`

### Infrastructure TODO 5: Formatting-rules.md for all papers ✅
- Created 6 new files:
  1. `paper/full/four-model-theory-full.formatting-rules.md`
  2. `paper/trimmed/noc/four-model-theory-noc.formatting-rules.md`
  3. `paper/intelligence/paper.formatting-rules.md`
  4. `paper/fmt_formal/fmt-formalization.formatting-rules.md`
  5. `paper/rim_formal/rim-formalization.formatting-rules.md`
  6. `paper/cosmology/sb-hc4a.formatting-rules.md`
- Book formatting-rules.md already existed from Session 71

### Bonus: Cross-project tools directory ✅
- Created `~/claude-config/tools/` for scripts useful across projects
- review_changes.py is the first tool there
- Future tools go here too (build scripts, etc.)

### Cleanup
- Removed obsolete `paper/cosmology/SB-HC4A_formal.md` (Session 65 working notes, superseded by full formalization in `paper/cosmology_formal/`)

## TOP TODO — PRIORITY FOR NEXT SESSION

### Publications (carried forward)

1. Intelligence paper: trim ~358 words, write highlights, generate .docx, submit to *New Ideas in Psychology*
2. NoC resubmission (trimmed paper .docx ready)
3. Outreach emails (3 ready to send)
4. Review cosmology chapters for flow/consistency
5. Consider whether computational atoms insight warrants a separate short paper

### Infrastructure (new, lower priority)

6. Cosmology paper missing unicode-header.tex — audit sb-hc4a.md for Unicode symbols, copy header from Paper 4/5 if needed
7. Papers 1 and 3 have no build scripts (.tex hand-maintained) — create build scripts to close the .md → .tex pipeline gap
8. Update session-setup.md with actual skill installation status (collections cloned, per-project skills installed)
9. Deploy skills to other projects (aIware.implementation, lockscreen-gen) when working on them
10. Update Claude Code from 2.1.37 → 2.1.47

### Future

- Deploy Claude Code on Fedora/NUC/Steam Decks/Ivoclar machines
- Try Agent Teams for a parallel research task (experimental)
- Explore per-project MCP server configs
- Consider consolidating unicode-header.tex across Papers 4, 5, 6

## Recovery Instructions
1. Read this file. Publications items 1-5 are top priority.
2. All infrastructure from Session 71 TODOs is DONE.
3. Skills installed — restart required to load them.
4. Config repo at `~/claude-config/`. Symlinks active. Hooks registered.
5. Cross-project tools at `~/claude-config/tools/`.
