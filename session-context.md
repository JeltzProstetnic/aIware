# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-19 (Session 71)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Infrastructure — publication workflow rules, modular config, config repo, automation

## Current State
- **Active Task**: SHUTDOWN — infrastructure work complete
- **Config repo created**: `~/claude-config/` → `JeltzProstetnic/claude-config` (private)
- **Symlinks active**: `~/.claude/CLAUDE.md` and `~/.claude/rules/*` → config repo
- **Hooks active**: SessionEnd (auto-sync) + SessionStart (failure check)
- **All changes committed and pushed**

## What Session 71 Did
1. Investigated .md/.tex date discrepancy — Session 70 hand-edited .tex (subtitle fix). No content loss, but violated canonical source rule.
2. Created `.claude/publication-workflow.md` — full pipeline rules (.md → .formatting-rules.md → .tex → .pdf). Formatting rules must be built into build scripts immediately.
3. Created `pop-sci/book-manuscript.formatting-rules.md` — documents existing LaTeX formatting decisions in build script.
4. Extracted CLAUDE.md from 492 → 245 lines. Moved TDD, VoltAgent/session-setup, session-context, publication-workflow into `~/.claude/rules/` as conditional modules.
5. Created `~/.claude/rules/session-setup.md` — unified roster management (agents + skills + MCP servers), session-start checks, mid-session adaptation, phase-aware detection.
6. Created `~/claude-config/` repo — tracks all global config, rules, project registry (16 projects, 7 machines), sync tooling.
7. Set up symlinks so edits go directly into config repo. SessionEnd hook auto-commits+pushes. SessionStart hook checks for sync failures.
8. Researched: Agent Teams (complementary to cc-mirror), OpenCode/Crush (archived→successor, compatible), VoltAgent skills (380+ available).

## TOP TODO — PRIORITY FOR NEXT SESSION

### Infrastructure (analyze + implement, prepare for restart)

1. **Absorb wsl-claude-setup into claude-config**
   - Unique value: install scripts (670 lines), 16 key learnings, git-credential-mcp
   - Move to `~/claude-config/setup/` subfolder
   - Archive or deprecate the standalone wsl-claude-setup repo
   - Preserve key learnings in a knowledge file

2. **Evaluate Agent Teams (CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS)**
   - Already have `CLAUDE_CODE_TEAM_MODE=1` in settings — what does this do vs Agent Teams?
   - Try spawning teammates for parallel research tasks
   - Document findings in config repo
   - Does NOT replace cc-mirror (different purpose: collaboration vs isolation)

3. **VoltAgent skills — clone and evaluate**
   - Clone `VoltAgent/awesome-agent-skills` and `anthropics/skills` to `~/.local/share/skill-collections/`
   - Browse catalog, identify skills relevant to aIware (publication, research, authoring)
   - Install selected skills to `~/.claude/skills/` or project `.claude/skills/`
   - Document in session-setup.md

4. **Review script consolidation**
   - 5 overlapping scripts in `tmp/`: render_tracked_paper.py, render_book_changes.py, create_highlighted_book.py, create_book_diff_html.py, create_tracked_paper.py
   - Consolidate into one `tmp/review_changes.py` with `--mode highlight|track`, `--source`, `--against`, `--output`
   - Must support: full text with nav, highlight-new-only mode, track-changes mode

5. **Create formatting-rules.md files for papers**
   - Full paper: `paper/full/four-model-theory-full.formatting-rules.md`
   - Intelligence paper: `paper/intelligence/paper.formatting-rules.md`
   - Audit existing build scripts for hardcoded formatting decisions

### Publications (existing TODO, lower priority this session)

6. Intelligence paper: trim ~358 words, write highlights, generate .docx, submit to *New Ideas in Psychology*
7. NoC resubmission (trimmed paper .docx ready)
8. Outreach emails (3 ready to send)
9. Review cosmology chapters for flow/consistency
10. Consider whether computational atoms insight warrants a separate short paper

### Future (not next session)

- Deploy Claude Code on Fedora/NUC/Steam Decks/Ivoclar machines
- Evaluate Crush (OpenCode successor) for multi-model / cost-optimization use cases
- Explore per-project MCP server configs (currently global only)

## Recovery Instructions
1. Read this file. Infrastructure items 1-5 are top priority.
2. Config repo is at `~/claude-config/`. Symlinks are active. Hooks are registered.
3. All rule modules live in `~/claude-config/global/rules/` (symlinked to `~/.claude/rules/`).
4. Next session needs a restart after any agent/skill/hook changes.
