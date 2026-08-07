<!-- agent-fleet-managed -->
# aIware — Consciousness Theory, Publications & AC Implementation

Consciousness research project: theory → papers → pop-sci book → artificial consciousness.

## Knowledge Loading

### Always loaded — read at session start, no trigger needed

| File | Why unconditional |
|------|-------------------|
| `.claude/knowledge/didactic-patterns.md` | The durable catalog of FMT teaching devices + the corrections not to re-introduce. **MG-directed 2026-07-31: "aIware and all its subprojects must be aware of this knowledge file, not only when I mention it explicitly."** Carrying it every session is what makes patterns get reused and gaps (`AIW-95`) visible. Co-owned with crucible (`~/crucible/docs/didactic-patterns.md`). |

### Triggered — load only when the trigger fires

| Domain | Files | Load when... |
|--------|-------|-------------|
| Publications | `~/.claude/domains/publications/publication-workflow.md` | Authoring, editing, or building any paper/book |
| Publications (TDA) | `~/.claude/domains/publications/test-driven-authoring.md` | Modifying build scripts or .md→.tex pipeline |
| Software Development | `~/.claude/domains/software-development/tdd-protocol.md` | Writing or modifying code (future AC implementation) |
| Prediction Framing | `.claude/knowledge/prediction-framing.md` | Writing or revising predictions in any FMT publication or submission |
| Prose register | `.claude/knowledge/prose-register.md` | Writing or revising any FMT paper, book or outreach prose |
| Neuroscience comms | `.claude/knowledge/neuroscience-communication.md` | Writing to neuroscientists (emails, papers, outreach) — the "two kinds of models" rule |
| Publication build/review | `.claude/knowledge/publication-build.md` | Building/reviewing any paper PDF — canonical-PDF protection, pipelines, yellow-highlight reviews, parallel-chunk limits |
| 2015 definitions | `.claude/knowledge/fmt-2015-definitions.md` | Defining or revising any FMT term (data/information/knowledge/meaning, consciousness, intelligence, the *erweitert* ladder) — the verbatim 2015 German definitions, the Bezugssystem architecture, and the flagged discrepancies vs current FMT |
| Project reference | `.claude/knowledge/project-reference.md` | Cold-start orientation — theory one-pager, bubble diagram, author facts, key paths |

## Key Files

| File | Purpose |
|------|---------|
| `session-context.md` | Current session state — **read first** |
| `backlog.md` | Full prioritized backlog — read when active TODOs are done |
| `docs/conversation-log.md` | Session history — **append every session** |
| `docs/references.md` | Master reference list for all papers |
| `ABOUT.md` | Project overview / README for humans |

## Reference (load on demand, not at start)

- MCP catalog: `~/.claude/reference/mcp-catalog.md`
- Output rules: `~/.claude/reference/output-rules.md`
- Project-specific protocols: Knowledge Loading table above + `.claude/knowledge/`

## Active Roster

- **Agents:** built-in only — **Explore** (search/fan-out), **Plan** (implementation planning), **general-purpose** (multi-step research/edit), **Opus writer subagent** for final creative prose. No custom `.claude/agents/`.
- **Skills:** `deep-research`, `code-review`, publication build scripts (see Build Infrastructure). Workflow tool for multi-phase paper passes (opt-in).

## Cross-Project

| File | Purpose |
|------|---------|
| `~/cfg-agent-fleet/cross-project/fmt-visibility-strategy.md` | Shared FMT visibility strategy (aIware + social). Targets, calendar, engagement coordination rules. **Single source of truth** for researcher outreach status, conference deadlines, media targets. |
| `~/cfg-agent-fleet/cross-project/contacts.md` | Canonical people catalog (researchers, media, Ivoclar). Append-allowed from aIware. Check before any person work — deep per-person history lives in `correspondence/<surname>-<firstname>.md`. |
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
| `figures/` | Diagrams, bubble diagrams, page renders (shared with the book — stays public) |
| **`~/simbook` (separate private repo)** | **The pop-sci book** (EN + DE + translations, covers, KDP, book build infra) was extracted here 2026-07-31 (AIW-125 / CFG-478). Book manuscripts do NOT live in aIware — they're the paid product. Public-history purge of old book blobs = deferred CFG-479. |
| `correspondence/` | Academic correspondence |
| `drafts/` | Content awaiting user review (pitches, submissions, letters) |
| `tmp/` | Test files, generated PDFs, throwaway build intermediaries only |
| `scripts/` | Build scripts (`build_*.py`), push script, SVG conversion, image tools |
| `docs/` | Conversation log, outreach plans, theory notes |

## Publication Pipeline

**Strict direction: `.md` → `.formatting-rules.md` → `.tex` → `.pdf`**

- NEVER edit `.tex` directly — all content in `.md`
- Build scripts in `scripts/build_*.py` — tracked; never `tmp/`
- Tests: `pytest scripts/test_content_integrity.py -v` (before every .tex commit)
- Full domain rules: see Knowledge Loading table above

## Git & Push

- **Two remotes**: `origin` (public, filtered) + `private` (full, `git@github.com:JeltzProstetnic/aIware-private.git`)
- **NEVER merge or pull from origin into local.** Origin is a one-way filtered mirror. Merging it treats "not on public" as "should be deleted" — Session 120 lost scripts/, docs/references.md, pop-sci/ barcodes this way. Only `git fetch origin` (to check state) and `git push origin` (via push.sh) are safe. If origin diverges, force-push it — never merge it in.
- **Session startup — MANDATORY**: Fetch and pull from **private only** before reading any project files. Run `git fetch private && git merge --ff-only private/main` (or handle divergence). The global `git-sync-check.sh` handles `origin` fetch (NOT merge). Private remote carries `session-context.md`, `scripts/`, `tmp/`, `docs/` — without it, operational files are missing.
- **If `private` remote is not configured**: Add it: `git remote add private git@github.com:JeltzProstetnic/aIware-private.git`
- **Push command**: `bash ~/cfg-agent-fleet/setup/scripts/filtered-push.sh` (centralized dual-remote filtered push; reads `.push-filter.conf`). Requires clean worktree — stash unrelated `tmp/` leftovers before running. The old `scripts/push.sh` was retired in commit 4baa0af.
- **Never push**: `tmp/`, `scripts/`, `session-context.md`, `docs/` to public
- **Divergence recovery**: If origin diverges (same content, different SHAs from multi-machine commits), check that local is the superset (has all content from both remotes), then force-push origin: `git push origin main --force-with-lease`. This is safe because origin is the public filtered mirror — private is the source of truth.
- **Session context protection**: `session-context.md` lives only on private remote. If it appears blank/template after pulling, the likely cause is a stale push from another machine that overwrote it. Recovery: `git log --all --oneline -- session-context.md` to find the last real version, then `git checkout <sha> -- session-context.md`. Prevention: ALWAYS read conversation-log.md if session-context.md is blank — it has the ground truth of what happened.

## Build Infrastructure

| What | Command |
|------|---------|
| Consciousness paper (NoC, trimmed) | `python3 scripts/build_noc_pdf.py` |
| Intelligence paper (RIM) | `python3 scripts/build_rim_pdf.py` |
| Review PDF (changed passages highlighted) | `python3 scripts/build_review_pdf.py` |
| AC design PDFs | `python3 scripts/build_individual_pdfs.py` · `build_design_overview.py` · `build_design_pdfs_13_16.py` |
| SMoC figures | `python3 scripts/build_smoc_marks.py` · `scripts/build_philosophy_map.py` |
| Markdown → PDF (overflow-safe) | `bash scripts/build-md-pdf.sh <in.md> <out.pdf>` — gated: shared preamble, fails on Overfull \hbox >2pt. Use for ALL md→PDF; never hand-roll bare pandoc. |
| Reference-existence gate | `python3 scripts/verify_references.py --check` — offline; `--update` needs network (run under tmux). Blocks publish. |
| md vs built PDF drift | `python3 scripts/check_md_pdf_drift.py --paper rim` — prose drift + reference-list ordering |
| All script tests | `pytest scripts/ -v` |
| Content tests (Tier 1-3) | `pytest scripts/test_content_integrity.py -v` |
| RIM build/citation tests | `pytest scripts/test_build_rim.py -v` |
| PDF tests (Tier 4) | `pytest scripts/test_pdf_verification.py -v -m slow` — recovered S289, **not re-validated against current PDFs** (`AIW-156`) |
| Baseline calibration | `python3 scripts/update_test_baselines.py` — recovered S289, same caveat |
| Cosmology PDF | `python3 scripts/build_cosmology_pdf.py` — recovered S289, same caveat |
| ~~Build script tests~~ | **QUARANTINED** — `scripts/test_build_scripts.py` tests a superseded pipeline API; `collect_ignore`d in `scripts/conftest.py` until rewritten (`AIW-156`) |

**bibtex** must run with `dangerouslyDisableSandbox` (sandbox blocks .bbl writes).

**pandoc .docx builds**: ALWAYS use `--csl=apa.csl` (or equivalent non-Chicago CSL). Without it, citeproc uses Chicago style which replaces repeated author names with "———" dashes — rendering references unreadable. The CSL file is stored at `paper/trimmed/noc/apa.csl` and copied to build dirs by the build script.

## Delivery Rules

- **Manual process kits**: When the user needs multiple artifacts for a manual process (journal submission, conference upload, email attachments, etc.), ALWAYS create a dedicated `tmp/<process-name>/` folder, copy all needed files there with clear names, and open the folder in Explorer. Never make the user sift through `tmp/`.
- **Paper PDFs — LaTeX only**: When the user asks to see a paper, ALWAYS open the LaTeX build output (`tmp/build-full/paper.pdf`, `tmp/build-noc/paper.pdf`), never intermediate weasyprint/pandoc markdown renders. Clean up intermediate `fmt-*` artifacts after review sessions to prevent confusion.
- **Pitches, submission materials, and content awaiting user review → `drafts/`, never `tmp/`.** `tmp/` is for build artifacts and throwaway intermediaries only. Anything the user needs to review, edit, or act on goes to `drafts/` (tracked in git, persists across machines).

## Submission Rules

- **Read journal guidelines first**: Before advising on any submission or resubmission, read the stored journal guidelines file (e.g., `paper/trimmed/noc/journal-guidelines-noc.md`). Check ALL requirements (word count, abstract limits, figure alt text placement, required sections) BEFORE building submission artifacts.
- **Desk rejection = new submission**: "Immediate Reject" on ScholarOne means no revision option. Must "Start New Submission." Cover letter should reference the prior manuscript ID and detail what was revised. Don't assume a revision workflow without checking the decision type.
- **Alt text IN the manuscript**: NoC (and many OUP journals) requires alt text directly in the manuscript under each figure legend, preceded by "Alt text:". A separate alt-text file is NOT sufficient — it must be in the `.tex` source within `\caption{}`.
- **Verify .docx before submission**: Always open and spot-check the `.docx` output (references, figures, formatting) before declaring it submission-ready. pandoc conversions from LaTeX are lossy.
- **Read the target before responding**: Before writing any commentary, review, or letter responding to a published article, read the article or verify its claims via research agents — never write from assumptions about what the author argues.
- **Verify every citation**: Every citation in a submission draft must be verified (title, authors, journal, DOI) via search agent before presenting the draft to the user.
- **Honest convergence framing**: When citing external work as supporting a claim, state what the cited paper actually argues and use "consistent with" unless the paper tests the claim directly.

## Communication Rules

- **Neuroscience outreach**: Never say "four models" — say "two kinds of models" or "model kinds/classes". Frame FMT as computational taxonomy, not circuit diagram. Full rule: `.claude/knowledge/neuroscience-communication.md`.
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
