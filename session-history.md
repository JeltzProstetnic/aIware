# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-07-07T16:03Z — WSL (DESKTOP-32ILURB)
**Goal:** Book ed.2 (AIW-107) — receive MG's full inline review of the Desktop DE-ed2-REVIEW-highlighted.docx → apply small fixes → build KDP publishing package (NEVER auto-publish). Secondary: triage 5-6 strategic aIware inbox items.
**Completed:**
- Startup loading protocol — machine ID (WSL/Bartl/day mode), git-sync (private up to date), read HANDOFF
- Extracted MG's inline review (docx-diff vs baseline → `tmp/aiw107-review/`); 26 ops applied to DE `.md`, all grep-verified (line 2371→2369)
- MG picked 3 EN ports → applied to EN `.md` (Hold-that-thought cut, bites→fits ×2, Attack-them cut); Occam bite-motif KEPT both editions (parity)
- MG: orca EN "trip back"→"detour" (match DE Umweg); "unsere Erde" kept as-is
- Committed both manuscripts `ebf5dca6`; updated pending handoff for 3→2→4
**Key Decisions:**
- Book ed.2: DE .md = source of truth. NEVER auto-publish — MG does manual KDP upload.
- DE diverges from EN on grandeur/tone by design (DACH reserved-tone pass) — see docs/decisions.md.
**Recovery/Next session:**
Resume from `docs/pending-book-ed2-implementation.md` (P0, AIW-107). Book restructure DONE; waiting on MG's Desktop review docx. Related: AIW-93 (voice pass), AIW-98 (content refinements).

### 2026-07-07T10:20Z — WSL (home PC)
**Goal:** Book ed.2 DE finish (AIW-107). START = KALK SCAN (native-German de-Anglizismus sweep, Opus — Fable on cost-hold) over ALL new/ported DE prose → then finish DE wave-1 restructure → build DE + cover + editable highlighted .docx for MG inline review → EN rebuild ("with white" fix).
**Completed:**
- Startup: private+origin sync clean; read handoff (next-session-task.md + pending-book-ed2-implementation.md), AIW-93 tell taxonomy, tone feedback.
- Extracted integrated new DE prose (diff 69e5b69b..HEAD) → tmp/de-ed2-new-prose-integrated.txt (71 lines / ~4,573 words). Confirmed AIW-93 tells present (e.g. „der Teil, der…" calque at 2 spots).
- Kalk scan (5 Opus chunks) → structured surgical findings. Verdict: prose already strongly native; ~48 real findings, named tells confirmed at 3 spots.
- Applied 38 objective-correctness fixes (verified script, each matched 1×) to `pop-sci/book-manuscript-de.md` + `drafts/book-ed2-de-new-prose.md`. „umbringen" motif preserved. Findings doc → `drafts/aiw107-kalk-scan-findings.md` (APPLIED / HELD-13 / CULTURAL-11).
- MG DECISION: "Trim DE for DACH" — DE diverges from EN on grandeur (S176 doctrine revalidated for DE). Applied 13-recast reserved-tone pass (Opus writer) to the 11 flagged passages; items 4+11 kept. Recorded in docs/decisions.md. Committed `09c40a65`.
- **DE wave-1 restructure DONE** — Fable-5 cartographer plan (`tmp/aiw107-kalk/de-restructure-plan.md`) applied via 5 verified engine scripts (apply_s1a/s1b/s3/s2/s4.py, every op unique-match). Kap13 split→new Kap14; renumber to 17ch + TOC + notes-index + 3 cross-refs; Anhänge F+G before H (bodies extracted from source, not retyped); banked prose integrated (One-Razor/286/octopus/waking/refrains); relocations (Copernican→Ch10, Leibniz→Ch13, Ch2 dump-split→Ch6/Ch10, age-11→AppB); motif prune 9a/9b/9c (verified vs EN Ch9). MG grandeur-trim already applied pre-restructure.
- DE PDF built clean: **301 pages** (was 273 on old cover → spine recalc needed). `pop-sci/book-manuscript-de.pdf`.
- DE cover rebuilt (spine 273→301pp = 0.678"); AIW-60 subtitle/artwork-overlap visual QA PASSED. `pop-sci/cover-wrap-de.pdf`. Committed `3280644f`.
- EN "with white" PDF rebuild (271pp, no shift) — committed `c99edb83`. EN otherwise unchanged since MG approval `eeaaa7d8`.
- **Review .docx built**: `drafts/book-manuscript-de-ed2-REVIEW-highlighted.docx` (772KB, figures embedded, 279 yellow-highlight runs). Diff vs pre-ed2 baseline `69e5b69b`: 105 new/changed blocks marked, 979 unchanged plain. QA: new=highlighted, unchanged=plain, color=yellow. **This is MG's tracked-changes review artifact.**
- Took over MG's 14 inline edits (tightened cold-open, du→wir in places, „ertappen" logic + „anatomisch", „Apparat"→„Jargon", bridge rewrite w/ Teppich/Puzzle imagery, „Der Autor" tweaks) + tightened the loose Bruno sentence → `theoretischer Physiker (Quantenmechanik und Symmetrien)…tief geprägt`.
- EN port decision: **nothing ported** — his edits are DE-voice/tightening; EN's parallels are already clean+approved (blind-spot „catch you out" is idiomatic; EN Bruno dedication L1888 is richer than DE's). Documented reasoning to MG.
- **`lrn`: fixed the RECURRING "thin table" docx bug** — root cause = bare `---` before a `.mark` heading → pandoc `multiline_tables` swallows chapters into a full-width table. Persisted to `.claude/knowledge/publication-build.md` (both docx traps: use `[…]{.mark}` not `<mark>` for para highlight; normalize `---` to blank-both-sides; verify `<w:tbl>`≈0). Review script `make_review_docx.py` now normalizes HRs. Rebuilt docx: 0 headings-in-tables, 6 genuine content tables only, 332 highlight runs. DE PDF still 301pp (cover unaffected).
**Key Decisions:**
- **Fable 5 RE-ENABLED for today (MG explicit go, 2026-07-07 mid-session: "make use of fable 5, today it is still free").** Cost-hold lifted for today only. Fable 5 → all NEW creative German prose in the wave-1 restructure (welds, reclaim-ending, fresh transitions). Already-done Kalk scan + reserved pass used Opus (edit tasks — fine, committed). Roster cost-hold note is per-day; not modifying cfg-fleet from aIware.
- **MG directive: finish ALL ed.2 tasks before he reviews the tracked-changes version.** No more mid-work review checkpoints. EN passed at `eeaaa7d8`; only post-review EN change = the "with white" opening polish (in committed .md, PDF rebuild pending).
- **Kalk scan = surgical de-Anglizismus only.** Do NOT rewrite good prose; do NOT re-strip the bridge cold-open / first-person (MG-approved ed.2 structure, EN already committed). FLAG (never auto-cut) US-grandeur / culturally-risky passages for MG's own call — that is what the highlighted .docx is for.
- **Data-integrity flag:** memory `feedback_german_book_tone.md` (S176, 100d old: third-person author, no bridge/tears) is SUPERSEDED by MG's S245 ed.2 restructure directive. Scoped to 1st-edition front matter; surfaced to MG, not silently applied.
**Recovery/Next session:**
Resume the Kalk scan: chunk inputs live in `tmp/aiw107-kalk/`. Subagents return structured findings (surgical old→new + rationale + separate cultural-flag list). Integrate clear wins into DE `.md` (and banked drafts file for not-yet-integrated §3/5/6/7/8/9/10). Full task spec: `docs/pending-book-ed2-implementation.md` + `next-session-task.md`. Baseline for "new prose" diff = commit `69e5b69b`.

### 2026-07-07T00:40Z — WSL (home PC)
**Goal:** Finish Book ed.2 (AIW-107) — wave-2 EN restructure (#4/#8/#9 + #12 motif prune + #13 last-lines) using Fable writer-subagents, then DE port (structural moves 1:1 + banked Fable German), build, cover spine check, MG sign-off → KDP publish.
**Completed:**
- Startup: private-remote pull, additionalContext parsed, handoff + review spec + build/didactic knowledge loaded
- Oriented on post-wave-1 manuscript (17 ch, targets: Ch8 771-856, Ch10 921-1041, Ch11 1043-1163)
- #9 Ch10 orca cold open — orca lifted to top + Fable weld into "Is your dog conscious?"; B2 callback at Mammals bullet. Verified.
- #8 Ch8 end-on-mirror (Fable synthesis close, hands to Ch9) + therapy FAQ moved & merged into Ch10 CBT thread (Fable). Verified.
- #4 Ch11 trough → Fable P3 "become the ocean" SCENE + frame (ends "It says you get a mind."); full battery → new **Appendix H: The Nine Predictions**; TOC updated; Ch9 P9 ref + Ch4 ref de-pointed. Verified: 9 Prediction headers all in App H, none in Ch11.
- #12 motif prune — Motif1 (zero-copies) already fixed in wave-1; trimmed hologram/Lashley re-explanations in Ch5+Ch9 to callbacks to Ch3; trimmed the ESM chair/dead/paralyzed re-list in Ch9 to a callback. Cosmology "holographic principle" usages left (legit physics term).
- #13 forward-pulling last lines — Ch2 already fixed in wave-1 ("about to go inside"); added Ch7 closer (→neurology ward/Ch8) + Ch9 closer (→orca/Ch10). **These two closers are MG-draft (not Fable) — flag for voice review.**
- Build EN — SUCCESS, 271pp (was 265). All restructured beats render (orca p103, ocean scene p121, App H p263, Ch7/Ch9 closers p85/p101). PDF on Desktop + pop-sci/book-manuscript.pdf.
- p203/Ch17 "without the cosmology" was FALSE + self-contradictory (Notes p215 say seeds were in Gruber 2015). Verified vs German 2015 book: p80 't Hooft holographic-bound→universe/black-hole/surface; p79 universe-as-cellular-automaton aside. Rewrote the clause to acknowledge the 2015 cosmology hints. **Same claim likely in DE book — fix during DE port.**
- DONE: Coda 4D-fractal drug hint RESTORED (DE had sanitized it to "wiederkehrender Traum aus meiner Kindheit" → now "…als ich ein animiertes vierdimensionales Fraktal war. Auf die Umstände gehe ich lieber nicht ein." = EN's coy "I won't go into the circumstances"). Late-book → cleared by MG.
**Key Decisions:**
- Wave-2 creative prose via **Fable** writer-subagents (MG directive S246); main loop integrates patches sequentially (single manuscript file — collision rule). Text-returning writers → no file edits by subagent.
- Execution order: #9 → #8 (coupled: therapy Ch8→Ch10) → #4 → #12 → #13 → build → DE → cover → publish.
- Protect-list = relocate/stage only, never rewrite: orca, bridge, blindsight/Anton's mirror, etc. (see docs/fable-book-experience-review-S245.md).
- NEVER auto-publish to KDP. MG signs off on both restructured builds first.
**Pending at shutdown:** MG voice review of all new prose (AIW-93); publish only on MG sign-off of BOTH builds.
**Recovery/Next session:**
- Handoff spec: `docs/pending-book-ed2-implementation.md` (wave-2 remaining) + `docs/fable-book-experience-review-S245.md` (15 fixes, exact WHERE/MOVE, protect-list).
- EN source: `pop-sci/book-manuscript.md` · build `python3 tmp/build_book_pdf.py`. DE source: `pop-sci/book-manuscript-de.md`.
- Banked Fable German for wave-1 new prose: `drafts/book-ed2-de-new-prose.md`.
- Content tests before commit: `pytest tmp/test_content_integrity.py -v`.

