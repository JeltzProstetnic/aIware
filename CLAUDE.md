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
| `~/cfg-agent-fleet/cross-project/fmt-visibility-strategy.md` | Shared FMT visibility strategy (aIware + social). Targets, calendar, engagement coordination rules. **Single source of truth** for researcher outreach status, conference deadlines, media targets. |
| `~/cfg-agent-fleet/cross-project/inbox.md` | One-off cross-project tasks |

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

- **Two remotes**: `origin` (public, filtered) + `private` (full, `git@github.com:JeltzProstetnic/aIware-private.git`)
- **NEVER merge or pull from origin into local.** Origin is a one-way filtered mirror. Merging it treats "not on public" as "should be deleted" — Session 120 lost scripts/, docs/references.md, pop-sci/ barcodes this way. Only `git fetch origin` (to check state) and `git push origin` (via push.sh) are safe. If origin diverges, force-push it — never merge it in.
- **Session startup — MANDATORY**: Fetch and pull from **private only** before reading any project files. Run `git fetch private && git merge --ff-only private/main` (or handle divergence). The global `git-sync-check.sh` handles `origin` fetch (NOT merge). Private remote carries `session-context.md`, `scripts/`, `tmp/`, `docs/` — without it, operational files are missing.
- **If `private` remote is not configured**: Add it: `git remote add private git@github.com:JeltzProstetnic/aIware-private.git`
- **Push command**: `bash scripts/push.sh` (handles both + filtering)
- **Never push**: `tmp/`, `scripts/`, `session-context.md`, `docs/` to public
- **Divergence recovery**: If origin diverges (same content, different SHAs from multi-machine commits), check that local is the superset (has all content from both remotes), then force-push origin: `git push origin main --force-with-lease`. This is safe because origin is the public filtered mirror — private is the source of truth.
- **Session context protection**: `session-context.md` lives only on private remote. If it appears blank/template after pulling, the likely cause is a stale push from another machine that overwrote it. Recovery: `git log --all --oneline -- session-context.md` to find the last real version, then `git checkout <sha> -- session-context.md`. Prevention: ALWAYS read conversation-log.md if session-context.md is blank — it has the ground truth of what happened.

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

**pandoc .docx builds**: ALWAYS use `--csl=apa.csl` (or equivalent non-Chicago CSL). Without it, citeproc uses Chicago style which replaces repeated author names with "———" dashes — rendering references unreadable. The CSL file is stored at `paper/trimmed/noc/apa.csl` and copied to build dirs by the build script.

## Delivery Rules

- **Manual process kits**: When the user needs multiple artifacts for a manual process (journal submission, conference upload, email attachments, etc.), ALWAYS create a dedicated `tmp/<process-name>/` folder, copy all needed files there with clear names, and open the folder in Explorer. Never make the user sift through `tmp/`.
- **Paper PDFs — LaTeX only**: When the user asks to see a paper, ALWAYS open the LaTeX build output (`tmp/build-full/paper.pdf`, `tmp/build-noc/paper.pdf`), never intermediate weasyprint/pandoc markdown renders. Clean up intermediate `fmt-*` artifacts after review sessions to prevent confusion.

## Submission Rules

- **Read journal guidelines first**: Before advising on any submission or resubmission, read the stored journal guidelines file (e.g., `paper/trimmed/noc/journal-guidelines-noc.md`). Check ALL requirements (word count, abstract limits, figure alt text placement, required sections) BEFORE building submission artifacts.
- **Desk rejection = new submission**: "Immediate Reject" on ScholarOne means no revision option. Must "Start New Submission." Cover letter should reference the prior manuscript ID and detail what was revised. Don't assume a revision workflow without checking the decision type.
- **Alt text IN the manuscript**: NoC (and many OUP journals) requires alt text directly in the manuscript under each figure legend, preceded by "Alt text:". A separate alt-text file is NOT sufficient — it must be in the `.tex` source within `\caption{}`.
- **Verify .docx before submission**: Always open and spot-check the `.docx` output (references, figures, formatting) before declaring it submission-ready. pandoc conversions from LaTeX are lossy.

## Communication Rules

- **Neuroscience outreach**: Never say "four models" — say "two kinds of models" or "model kinds/classes". Frame FMT as computational taxonomy, not circuit diagram. See MEMORY.md for full rule.
- **Console output**: Never paste >10 words for copy/paste. Write to `tmp/` file and open in Notepad.
- **Canonical PDFs**: Never recompile `paper/*/paper.pdf` for comparison. Always compile into `tmp/`.
- **Email**: This project uses Gmail EXCLUSIVELY (`jeltz.prostetnic@gmail.com` via `mcp__google-workspace`). NEVER use `mcp__pst-search` — that is for Ivoclar work only.
- **Email drafts → Gmail drafts, ALWAYS**: When composing email responses or outreach, ALWAYS create the draft via `mcp__google-workspace__draft_gmail_message`. NEVER write email content to text files in `tmp/`. Text files break the review/edit/send workflow — Gmail drafts let the user review, edit inline, and send with one click. This applies to ALL email composition across ALL projects. **Before recreating a "missing" draft, check Sent folder first** — if the draft is gone from Drafts, the user probably sent it.
- **Check communications log before drafting**: Before drafting any email, check the communications log for prior exchanges with that recipient. Never repeat content already communicated (e.g., congratulating someone twice).
- **Hedge presumptions about recipients**: Never state as fact what you can't verify about the recipient's circumstances, workload, or situation. Use "probably," "I imagine," or restructure to avoid the presumption.
- **Don't re-explain what the recipient told you**: When responding to a point the recipient made, acknowledge agreement in one sentence. Only elaborate when adding something new — don't lecture them on their own argument.
- **Outreach email workflow (atomic — no step may be skipped):**
  1. Check contacts.md for current relationship status + prior exchanges
  2. Check communications log for content already communicated
  3. Draft email in Gmail via MCP
  4. After user confirms sent → update contacts.md (status + date + pitch angle) AND conversation log BEFORE doing anything else. The send is not complete until tracking reflects it.
