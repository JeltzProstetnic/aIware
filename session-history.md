# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-07-08T23:30Z — WSL (home PC, DESKTOP-32ILURB)
**Goal:** AIW-108 — IT translation (Opus, in progress) + NEW MG directive (S253 2026-07-08): add JAPANESE (Fable — MG confirmed cost-free, cost-hold lifted for this work) and CHINESE (Opus, process based on JA). All Kalk/coherence scans → Opus.
**Completed:**
- IT Step 1 translate (Opus 60/60) + Step 2 assemble → `pop-sci/book-manuscript-it.md` (committed 94f4a907)
- IT Step 3 Kalk scan run 1 (wuimcsuwt): 329 findings saved `tmp/it-kalk/findings-partial.json` — but 37/89 agents rate-limited (concurrent with JA workflow)
- IT Kalk re-run (wmurksoab, alone) — merged to 491 findings `tmp/it-kalk/findings-all.json` (A=317 B=162 C=6 D=4). Still 7 segs uncovered (session-limit): pass1{21,27,35} pass2{39,44,52,54}.
- IT Kalk APPLIED: 392 fixes (A+B+D) via match-once → book-manuscript-it.md (2467 ln, 0 missing, 304/304«», acronyms ok). 90 not-found+1 quar+6 C → `drafts/aiw108-it-kalk-findings.md` (reviewer).
- JA prep: glossary-ja.md + culture-guide-ja.md built (Fable; である体, 気づき, 自己言及的閉包, 「」)
- JA translate (wxveb1kwc, Fable): 48/60 chunks OK, saved `tmp/ja-pipeline/ja-results.json`. 12 failed (43,44,46,50,51,53,54,56,58,59,60,61) — **Fable OUT OF CREDITS, resets Jul 14 11pm Vienna.**
- JA gap-fill (w2hp7migb, OPUS 12/12, exemplar-primed w/ nearest Fable neighbors) → merged 48+12 → assembled `pop-sci/book-manuscript-ja.md` (2471 ln, 0 missing, 334/334「」, 0 です/ます vs 1094 である, acronyms intact, seams clean). Committing JA Phase-1.
**Key Decisions:**
- **S253 (2026-07-08): MG confirmed Fable IS cost-free right now → cost-hold LIFTED for this session's work.** Plan: JAPANESE full translation on **Fable** (highest-value use of the free window; hardest literary target); CHINESE full translation on **Opus** (process/lessons reuse from JA — NOT text reuse: JA/ZH share no script/typography/register); ALL Kalk + coherence scans on **Opus** for every language.
- Bulk work otherwise → Opus per S252. Fable = high-value small + the one confirmed-free full translation (JA).
- Chunks 7 & 62 excluded (degenerate empty-EN artifacts) → assembly makes NO markers. Source chunks shared across all langs: `tmp/es-pipeline/chunks/` (62).
- MG S252 Kalk apply policy (carries to all langs): auto-apply A + held B + soften grandeur D, KEEP C motifs, quarantine malformed fixes. Register: conservative (farther from US culture = more traditional; JA/ZH = quite reserved).
- Publish stays gated on a human native reviewer PER LANGUAGE (§0.3 lock).
- Precedent: ES/FR/PT = publish-candidates via this exact pipeline (S252). IT = this session.
**Pending at shutdown:** publish blockers PER LANG (ISBNs, build scripts, human native reviewer). **QUOTA STATE: Fable OUT OF CREDITS (resets Jul 14 11pm Vienna); Anthropic SESSION LIMIT hit (resets ~11pm Vienna tonight) — Opus workflows blocked until reset.** LESSONS: (1) never run 2 large workflows concurrently — rate-limits kill agents; (2) local LM Studio (4090) inference now on the table as a free quota-proof fallback — MG wants it as a built-in FLEET capability (→ cfg inbox).
**Recovery/Next session:**
- If translation workflow output exists: `tmp/it-pipeline/*.json` → assemble via `python3 tmp/es-pipeline/assemble_generic.py <it-output.json> pop-sci/book-manuscript-it.md t`.
- Full step recipe: `docs/pending-aiw108-it-translation.md`. Backlog: `AIW-108` (`[>]`).
- If `book-manuscript-it.md` exists but unpolished → resume at Kalk scan (Step 3).

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

