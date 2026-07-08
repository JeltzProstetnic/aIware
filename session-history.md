# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-07-08T08:07Z — WSL (home PC, DESKTOP-32ILURB)
**Goal:** AIW-108 multilingual book translation — cleanup + resume (per S251 handoff). 6-language Fable-5 program (ES/FR/PT-BR/IT/JA/ZH); Fable free until 2026-07-12.
**Completed:**
- Startup protocol run — private remote synced (up to date), session-context populated
- Handoff read: `docs/pending-aiw108-multilang-handover.md`
- Deleted 5 degenerate-chunk markers (ES 007+062, FR 007+062, PT 062). Verified chunks 007/062 have empty EN source (boundary artifacts).
- **ES manuscript now fully Phase-1 complete (0 markers).**
- Fable re-translated FR 29, FR 60, PT 31 (run wf_b7339153-a53, 3/3 OK). MG confirmed Fable cost-free for THIS task only.
- Spliced all 3 into FR/PT manuscripts; QA passed (para parity 14/14, 28/28, 28/28; headings translated; seams clean).
- **ES/FR/PT all Phase-1 COMPLETE — 0 markers (2469/2469/2467 ln).**
- Updated handover + backlog AIW-108 + committed.
**Key Decisions:**
- **ACTIVE MODEL POLICY (MG directive S252, until further notice): Fable ONLY for high-value SMALL work — Fable tokens running low.** All bulk work (Kalk scans, translation fan-outs) → **Opus 4.8**. FR + PT Kalk scans = Opus. ES scan was launched on Fable pre-directive → let it finish; re-run any Fable-failed segments on Opus.
- Run ONE language workflow at a time (mass-launch blew the session limit last session).
- All publish gates HELD for human native passes (AI pipeline → publish-candidate only).
**Recovery/Next session:**
- Primary task handover: `docs/pending-aiw108-multilang-handover.md` (TODO resume order + key lessons).
- Full pipeline spec + LOCKED decisions: `docs/pending-spanish-translation.md`.
- Backlog: AIW-108 is `[>]` P1. Open P0 = AIW-91 (minimal critical spiking substrate).

### 2026-07-07T23:05Z — WSL
**Goal:** AIW-108 — Spanish edition. Fable-5 team, dual-source (EN+DE ed.2) translation → publish-*candidate* (human native pass held). Resume-as-planned from S250 handoff. Time-critical: Fable free window closes midnight 2026-07-07.
**Completed:**
- Phase 0 artifacts built for ES/FR/PT/IT/JA/ZH: `tmp/{es,fr,pt,it,ja,zh}-pipeline/{glossary,culture-guide}` + shared chunks in `tmp/es-pipeline/chunks/` (62, language-independent EN+DE).
- **Spanish**: 60/62 translated + assembled → `pop-sci/book-manuscript-es.md` (2473 lines). Gaps: chunks 7 & 62 (redo on Fable).
**Key Decisions:**
- LOCKED (do not re-litigate): neutral/intl Spanish · **top-tier model only** (Fable, free till 07-12) · HOLD publish for human native pass per language (AI → candidate only).
- CJK (JA/ZH) = highest translation risk: EN-primary, DE for meaning only (German idiom doesn't transfer); native gate matters most here. JA quotes 「」, ZH quotes "" (NOT guillemets); FR/IT/ES use «».
- Kalk scan mirrors AIW-107 German A–E structure; watch source-language calques (EN + DE, both).
- Reader-address per language: ES=tú, FR=vous, PT-BR=você, IT=tu, JA=です・ます体, ZH=你.
**Recovery/Next session:**
- Full pipeline spec + LOCKED decisions: `docs/pending-spanish-translation.md`. Assembler: `tmp/es-pipeline/assemble.py` (edit OUT_FILE/DEST + field name per language; ES uses "spanish", FR+ use "translation").
- Translate scriptPath (edit constants per language, run ONE at a time): `.../scripts/aiw108-translate-fr-wf_3976fe8c-291.js`.
- Do NOT publish; do NOT recompile canonical EN/DE PDFs; do NOT parallel-write a manuscript file; do NOT mass-launch workflows (session limit).

### 2026-07-07T20:05Z — WSL
**Goal:** Resume Book ed.2 (AIW-107), MG-directed order 3→2→4 — (3) present held-13 Kalk §B + TOC↔heading drift, apply greenlit; (2) rebuild DE+EN "us" PDFs; (4) KDP kit POST sign-off. NEVER auto-publish.
**Completed:**
- Startup: git clean both remotes
- item 3: 11 TOC/heading drift fixes + 11 §B Kalk (B12/B13 kept), verified
- item 2: rebuilt DE us 301pp / EN us 271pp (baseline). MG signed off on both Desktop PDFs.
- item 4: built ALL 6 interiors (EN us/us-hc 271, EN eu 265; DE us/us-hc 301, DE eu 285) + 2 epubs + 5 covers. **Fixed stale cover spine page-counts** (EN 251→271, EN-eu →265, DE-hc 273→301). AIW-60 visual QA PASSED on all covers (no subtitle/artwork overlap). Assembled `tmp/kdp-2026-07-07/` (8 edition folders + README-upload-guide.txt), opened in Explorer.
- Committed `1e8a3bbb` (item 3+2) + this commit (item 4)
**Key Decisions:**
- TOC↔heading drift: EN manuscript is the parity anchor (its TOC and headings already match). Most DE drifts resolve to "make TOC match heading"; a handful are genuine word-choice calls for MG (Ch1 schwerste/schwierigste, Ch6 enthüllen/offenbaren, Ch10 Tierfrage/Frage der Tiere, Ch16 allem/Allem).
- §B B1 („dich zu ertappen") and B12 („jemand zu Hause") both KEEP original — EN confirms forward reading + "someone home" is a load-bearing recurring motif.
- DE .md = source of truth. Reserved-tone §E pass already applied (13 recasts, S249). EN ed.2 keeps its grandeur; DE dialed down for DACH.
**Recovery/Next session:**
- Full task spec + history: `docs/pending-book-ed2-implementation.md`
- Kalk findings (§B held items): `drafts/aiw107-kalk-scan-findings.md`
- DE source: `pop-sci/book-manuscript-de.md` (TOC L13-44) · EN source: `pop-sci/book-manuscript.md`
- Builds: DE `python3 tmp/build_book_pdf_de.py --edition us` · EN `python3 tmp/build_book_pdf.py`

