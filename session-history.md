# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-07-14T23:05Z — WSL (home PC, DESKTOP-32ILURB)
**Goal:** Resume AIW-109 BUILD & SHIP (ed.2). Manuscripts are TEXT-FINAL (6 translations @ 2475 lines). Remaining = build-level typography → edition-marker flip → rebuild interiors+eBooks → hand MG the KDP upload kit.
**Completed:**
- Startup: private ff-merge clean; surfaced additionalContext (config-repo-dirty in cfg sibling noted, not touched; 11 aIware inbox items parked as outreach/theory lane)
- Verified manuscripts: ES/FR/IT/JA/PT/ZH all 2475 lines; DE 2367 (own structure); EN 2475 — matches handoff
- Read §5 build-checklist (drafts/aiw109-combined-cross-language-findings-S259.md)
- Step 1: build-level typography — new tested `tmp/typography_fixes.py` (14-pass pytest). FR EPUB narrow-NBSP U+202F (apostrophe already curled by pandoc smart); JA+ZH `*CJK*`→bold, Latin titles kept italic. Wired into epub + CJK print builders.
- Step 2: edition marker First→Second on PRINT copyright page, all 8 langs (verified; 0 stale first-markers). eBooks keep © 2026.
- Step 3: rebuilt 8 eBooks + 18 print interiors fresh; ZH docx rebuilt + PublishDrive kit refreshed. Source .md untouched, 6 translations still 2475 ln.
- Step 4: KDP re-upload kit `drafts/aiw109-ed2-reupload-2026-07-14/` (7 eBooks + README) ready for MG-manual upload.
**Key Decisions:**
- Text is FINAL — NO more text editing (S262 judgment round + MG decisions applied, commits 172dcdc9→8e6e5717).
- Edition marker: "Second" only, drop "corr." — PRINT copyright page ONLY; eBooks keep just `© 2026` (MG S260).
- Build-level typography lives in `scripts/typography_fixes.py` (moved out of tmp/ per MG "move non-throwaway out of tmp"; imports fixed + verified). Rest of book-build toolchain stays in tmp/ pending AIW-114.
- MG S263: next session re-does all cover art IF necessary, then RE-UPLOADS EVERYTHING (print + covers + eBooks). Spine check done — all covers' baked page counts match built interiors → no cover redo needed unless the final Fable review flags a defect.
- MG S263: next session must run a LAST Fable review (3–5 agents, overall checks + samples, INCLUDING sampling the built print-interior PDFs, not just source text) → then close AIW-109.
**Recovery/Next session:**
- Handoff: docs/pending-aiw109-multilang-fix-and-reupload.md (§ "NEXT SESSION (S263)")
- Build-checklist: drafts/aiw109-combined-cross-language-findings-S259.md §5
- Build scripts: tmp/build_translation_interior.py (ES/FR/IT/PT), tmp/build_translation_interior_cjk.py (JA/ZH), tmp/build_book_pdf.py (EN/DE), tmp/build_book_epub_lang.py (eBooks)
- comgarra-guard rule in .claude/knowledge/publication-build.md — applies to ANY global/substring swap

### 2026-07-14T13:10Z — WSL (home PC, DESKTOP-32ILURB)
**Goal:** Continue AIW-109 (multilang book corrections) to publication — resolve Fable cost-hold conflict with MG, then run the judgment review round on corrected manuscripts, then build-level typography → build & ship.
**Completed:**
- Startup: private remote ff-merged (already up to date), session-context populated
- Read HANDOFF file `docs/pending-aiw109-multilang-fix-and-reupload.md`
- Fable cost-hold conflict RESOLVED — MG cleared Fable cost-free; propagated to cfg inbox + decisions.md
- Judgment review round DONE — 6 Fable agents, all 6 manuscripts still 2475 lines; results in `docs/pending-aiw109-judgment-round-S262.md`
- Crash-safe checkpoint: committed + pushed to private
- MG ruled on all needs_MG_decision items ("a + go with recs"); applied via 4 Fable agents (ES/ZH/JA/PT); all 6 manuscripts still 2475 lines → text-FINAL for ed.2
- Root-cause guard for the comgarra bug: knowledge entry + AIW-113 + cfg inbox escalation (MG-approved)
**Key Decisions:**
- Fable cost-hold RESOLVED (S262) — MG confirmed cost-free; used Fable for the judgment round. Fleet-config clearance propagated via cfg inbox.
- comgarra guard (S262, MG-approved) — blind substring/`replace_all` swaps banned without a grep pre-check + post-check; recorded in `.claude/knowledge/publication-build.md` + AIW-113 + cfg global-rule inbox proposal.
- Edition marker: print copyright page only (eBooks keep `© 2026`, no edition line) — S260.
- Line 678 anosognosia = ESM in all 8 editions — S260.
**Pending at shutdown:** Steps 1–4 (build & ship) deferred to next session per MG. 11 cross-project inbox tasks still un-triaged → backlog.
**Recovery/Next session:**
- Handoff/work-order: `docs/pending-aiw109-multilang-fix-and-reupload.md` (AIW-109).
- Primary findings: `drafts/aiw109-combined-cross-language-findings-S259.md` (§4 = judgment-round worklist, §5 = FMT term decisions + build checklist).
- Low-risk mechanical pass committed `fcf82704`; do NOT assume every §4 row is still open — re-verify against current text.

### 2026-07-13T23:40Z — WSL
**Goal:** AIW-109 — resume the translation review round; deliver Low-items overview, then fix the low-risk (mechanical) subset across all 6 translations; prepare handover to publication.
**Completed:**
- Startup (WSL); private remote synced; handoff read
- Delivered overview of the ~222 Low items (7 thematic buckets + scope recommendation)
- Low-risk mechanical pass DONE across all 6 translations — 34 in-line edits, 2475-line invariant preserved, committed `fcf82704`
- Both must-fix integrity items done (IT Ch4 title/TOC; ZH L1898 EN-absent detail removed); both S260 flagged extras done (FR 2248 cap-C; IT idiom)
- Handover updated (`docs/pending-aiw109-multilang-fix-and-reupload.md` — S261 status block)
**Key Decisions:**
- "Fix the low-risk stuff first" (MG) → conservative mechanical-only pass (typography/accents/decimals/numerals/punctuation-width/cross-ref-caps/hyphenation + 2 integrity must-fixes). Everything needing a term/lexical/name/grammar judgment was DEFERRED to the next review round.
- **Fable cost-hold conflict UNRESOLVED (must resolve before the judgment round):** S259 handoff says Fable cost-free; live agent config says Fable ON COST HOLD since MG directive 2026-07-07. This mechanical pass used Opus (no cost risk). MG must decide Fable-vs-Opus for the native-judgment round.
- Do NOT rebuild before the review round completes (carried from S260). Edition marker First→Second on PRINT copyright page ONLY; eBooks stay `© 2026` (carried from S260).
**Pending at shutdown:** judgment round (buckets 1–3: terminology/lexical/name/grammar) → build-level typography → build&ship → human-native gate.
**Recovery/Next session:**
- Handover / work-order: `docs/pending-aiw109-multilang-fix-and-reupload.md` (S261 block = the ordered path to publish).
- Judgment-round worklist: `drafts/aiw109-combined-cross-language-findings-S259.md` §4 (term/lexical/name/grammar rows) + §5 (FMT term-reconciliation decisions) + §3 (cross-language clusters).
- This session's low-risk scope spec: `tmp/aiw109-lowrisk-scope.md`.
- Build scripts: `tmp/build_translation_interior.py` (ES/FR/IT/PT), `_cjk.py` (JA/ZH), `build_book_epub_lang.py`; EN/DE own scripts. Do NOT build until the judgment round is done.
- Invariant: all 7 editions (EN + 6 translations) are exactly 2475 lines and line-aligned (±2). Any edit must preserve 2475 lines per file.

