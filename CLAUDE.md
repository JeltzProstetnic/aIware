# aIware — Consciousness Theory, Publications & AC Implementation

Consciousness research project: theory → papers → pop-sci book → artificial consciousness.

## Knowledge Loading

| Domain | Files | Load when... |
|--------|-------|-------------|
| Publications | `~/.claude/domains/publications/publication-workflow.md` | Authoring, editing, or building any paper/book |
| Publications (TDA) | `~/.claude/domains/publications/test-driven-authoring.md` | Modifying build scripts or .md→.tex pipeline |
| Software Development | `~/.claude/domains/software-development/tdd-protocol.md` | Writing or modifying code (future AC implementation) |

## Key Files

| File | Purpose |
|------|---------|
| `session-context.md` | Current session state — **read first** |
| `backlog.md` | Full prioritized backlog — read when active TODOs are done |
| `docs/conversation-log.md` | Session history — **append every session** |
| `references.md` | Master reference list for all papers |
| `ABOUT.md` | Project overview / README for humans |

## Cross-Project

| File | Purpose |
|------|---------|
| `~/claude-config/cross-project/fmt-visibility-strategy.md` | Shared FMT visibility strategy (aIware + social). Targets, calendar, engagement coordination rules. **Single source of truth** for researcher outreach status, conference deadlines, media targets. |
| `~/claude-config/cross-project/inbox.md` | One-off cross-project tasks |

## Project Structure

| Directory | Contents |
|-----------|----------|
| `paper/full/` | Consciousness paper (FMT) — full version |
| `paper/trimmed/noc/` | Consciousness paper — trimmed for NoC |
| `paper/intelligence/` | Intelligence paper (RIM) |
| `paper/cosmology/` | Cosmology paper (SB-HC4A) |
| `paper/cosmology_formal/` | Cosmology formalization |
| `paper/fmt_formal/` | FMT formalization roadmap |
| `paper/rim_formal/` | RIM formalization roadmap |
| `pop-sci/` | Book manuscript (EN + DE), covers, KDP assets |
| `figures/` | Diagrams, bubble diagrams, page renders |
| `correspondence/` | Academic correspondence |
| `tmp/` | Build scripts, test files, drafts, generated PDFs |
| `scripts/` | Push script, SVG conversion, image tools |
| `docs/` | Conversation log, outreach plans, theory notes |

## Publication Pipeline

**Strict direction: `.md` → `.formatting-rules.md` → `.tex` → `.pdf`**

- NEVER edit `.tex` directly — all content in `.md`
- Build scripts in `tmp/build_*.py`
- Tests: `pytest tmp/test_content_integrity.py -v` (before every .tex commit)
- Full domain rules: see Knowledge Loading table above

## Git & Push

- **Two remotes**: `origin` (public, filtered) + `private` (full)
- **Push command**: `bash scripts/push.sh` (handles both + filtering)
- **Never push**: `tmp/`, `scripts/`, `session-context.md`, `docs/` to public

## Build Infrastructure

| What | Command |
|------|---------|
| Book PDF | `python3 tmp/build_book_pdf.py` |
| Cosmology PDF | `python3 tmp/build_cosmology_pdf.py` |
| Content tests (Tier 1-3) | `pytest tmp/test_content_integrity.py -v` |
| PDF tests (Tier 4) | `pytest tmp/test_pdf_verification.py -v -m slow` |
| Build script tests | `pytest tmp/test_build_scripts.py -v -m "not slow"` |
| Baseline calibration | `python3 tmp/update_test_baselines.py` |

**bibtex** must run with `dangerouslyDisableSandbox` (sandbox blocks .bbl writes).

## Communication Rules

- **Neuroscience outreach**: Never say "four models" — say "two kinds of models" or "model kinds/classes". Frame FMT as computational taxonomy, not circuit diagram. See MEMORY.md for full rule.
- **Console output**: Never paste >10 words for copy/paste. Write to `tmp/` file and open in Notepad.
- **Canonical PDFs**: Never recompile `paper/*/paper.pdf` for comparison. Always compile into `tmp/`.
