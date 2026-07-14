# Session History

Rolling window of the last 3 sessions. Newest first.

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

### 2026-07-13T22:05Z — WSL (home PC)
**Goal:** AIW-109 — apply Fable interior-review fixes across all 6 translations → rebuild → re-upload eBooks as ed.2 corr.2
**Completed:**
- Startup: private ff-merge (up to date), session-context populated, config-dirty on cfg-agent-fleet flagged
- Read EN source anchors (378 callback intact, 674 anosognosia ¶ present, 678 EWM/ESM, 1674/1726 distinct)
- Applied ALL High-severity fixes via 6 parallel Fable subagents (one per manuscript file, no collision):
- FR: title self-citation «Je»(+echo), anosognosia ¶ restore, Class-4 bullet close, Ch2 callback, Ch5 xref
- JA: title self-citation (+echo), weak-point-4 authorial line, Ch2 callback, Ch5 xref
- ES: meaning-inversion 1324 →«en tu lugar», Ch2 callback, 1674/1726 made distinct (678 NOT touched)
- IT: broken impersonal-si grammar 330–340 (4 edits, «si prova» consistent), Ch2 callback, 1674/1726 distinct (678 NOT touched)
- PT: 1550 truncation restored, Ch2 callback
- ZH: meaning-inversion 1750 →推出第四类之外, term-collision 1298 →通透性, Chalmers name 1308, Ch2 callback, Ch5 xref, 1674/1726 distinct
- Med pass (~127) applied via 6 Fable per-language agents (Low ~222 deferred per MG)
- Line 678 EWM→ESM across all 8 editions (MG: info that arm isn't behaving as predicted never reaches ESM)
- Build-checklist §5 verified: PT quotes auto-curled by pandoc `smart`; FR EPUB NBSP + CJK emphasis deferred (build-level)
- Committed 52db8226; work-order updated with build&ship handoff
**Key Decisions:**
- Model routing: Fable for risky/challenging native-language fixes, Opus for mechanical (per MG directive + work-order §Model policy; Fable cost-free as of S259).
- Line 678 anosognosia deficit = Explicit Self Model (ESM), not World Model (MG, author decision).
- Edition marker "Second edition" = PRINT copyright page ONLY (MG S260); eBooks keep just © 2026.
- Another review round on the corrected manuscripts BEFORE any rebuild (MG S260) — reduces churn after ~800 edits.
- EN source (book-manuscript.md) deliberately NOT edited: 378 callback is intact (per-translation restore only); 678 EWM/ESM deferred to MG; 1674/1726 EN is already the canonical distinct pair (translations propagate FROM it).
- All 6 translation manuscripts are line-aligned ±2, so shared clusters (378, 1674/1726) fixed per-file.
**Pending at shutdown:** build & ship deferred to next session behind another review round (MG S260).
**Recovery/Next session:**
- High-fix diffs are on disk (uncommitted): `git -C ~/aIware diff --stat pop-sci/book-manuscript-*.md`.
- To continue: get MG answers to the 3 gate questions (Med/Low scope, line 678, edition label), then Med/Low pass → build-checklist → rebuild → re-upload.
- Flagged-but-out-of-scope (next pass): FR ~2248 «(voir Chapitre 6)» capital-C vs lowercase convention; IT chapter-title/TOC «ci si sente qualcosa» (grammatically valid, but body now uses «si prova» — consider harmonizing the heading).

