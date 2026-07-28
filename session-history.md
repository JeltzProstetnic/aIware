# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-07-28T09:24Z — WSL (home PC)
**Goal:** Report open items for the Dutch (nl) book edition + assess whether remaining work fits ~20% model-limit / ~9% Fable budget until 23:00.
**Completed:**
- Startup: private pull (up to date), persona Bartl, WSL.
- Established authoritative NL state (was stranded on unmerged worktree branch `s268-translations-zh-print`).
- **Merged `s268-translations-zh-print` → main** (merge commit `efb09267`; session-context conflict resolved in favor of this session). NL publish-candidate now on main: pb+hc interiors 288pp margin-clean, epub, 3 covers AIW-60-QA'd, KDP metadata, Kalk 349+ fixes.
- **Pushed both remotes** (private full `5791fbc1..efb09267`; origin filtered `fa419c2c..46ee2de8`, 7 LFS objects; manuscripts excluded from public per push filter).
- Cleanup: worktree removed, local branch deleted, `docs/pending-nl-publish-handoff.md` updated to record merge.
**Key Decisions:**
- NL final Fable pass is DEFERRED to Wednesday (Fable tokens back); Fable budget reserved for FMT v13 (AIW-127). Do NOT spend the ~9% Fable on NL today.
- NL publish is gated on MG human-native Dutch review (locked gate) + the deferred Fable pass — neither is unblocked by today's token budget.
- main's `docs/pending-translations-nl-el-ko.md` is STALE (Kalk/coherence/build listed as remaining were done on s268); superseded by `docs/pending-nl-publish-handoff.md`.
**Pending at shutdown:** NL publish gates (MG human review; Wednesday Fable pass; MG KDP upload) — see Next Session Task.
**Recovery/Next session:**
- Authoritative NL "what's left": `docs/pending-nl-publish-handoff.md` (now on main).
- NL merged via commit `efb09267`; branch `s268-translations-zh-print` + worktree removed. Nothing stranded off-main anymore.

### 2026-07-27T15:20Z — WSL (home PC)
**Goal:** Improve + SEND the Safron/IWMT convergence note (AIW-119). DONE — verified against Safron's primary papers, 6 fixes applied, MG-approved, SENT.
**Completed:**
- Startup + corrected false STALE_PENDING flag (note was not sent)
- Primary-source verification: 3 parallel agents vs Safron2020/2022a/2022b → 6 accuracy fixes to the note
- ICT thread grounded (Chang/Biehl/Yu/Kanai, arXiv 1909.13045); Kanai = JAIC EiC verified
- AIW-129 filed (P2, proposed) — FMT = Φ-free ICT patch / JAIC door-opener; contacts.md row 14 + social inbox updated
- Note rebuilt (PDF clean, 0 overfull); cover MG-rewritten to terse 2-liner
- SENT from matthias@ (msg 19fa4ad6ea8b6929); stale S267 draft trashed; pending-safron-send.md deleted
- Atomic tracking: contacts.md row 37, correspondence/safron-adam.md, backlog AIW-119, conversation-log S272
**Key Decisions:**
- STALE_PENDING flag on pending-safron-send.md was a FALSE POSITIVE — note was polished S271, deliberately not sent.
- 6 accuracy fixes are all tightenings toward Safron's own wording (no argument change) — required because a domain expert reads the note.
- Cover email: MG rewrote to a deliberately terse 2-liner + FMT DOI; sent standalone (self-labeling subject, easier for a swamped Safron to find in Sept).
**Pending at shutdown:** (a) MG to confirm AIW-129 priority (proposed P2). (b) Commit + filtered-push this session's changes. (c) Await Safron reaction ~Sep — do NOT nudge; on reply, gauge him then weigh the Kanai/JAIC angle.
**Recovery/Next session:**
- Send complete: Gmail msg 19fa4ad6ea8b6929, to asafron@gmail.com, from matthias@matthiasgruber.com. Corrected note: drafts/aiw119-iwmt-fmt-convergence-note.md.
- Uncommitted work this session: the 6 note edits, backlog AIW-129, contacts.md (rows 14+37), inbox social item, correspondence/safron-adam.md, conversation-log. NEEDS commit + filtered-push (dual remote).

### 2026-07-26T22:10Z — WSL
**Goal:** MG's S271 order — (1) publish FMT v13 (AIW-121 epic), (2) write to Safron, (3) review the anti-AI-tell mechanism. Night mode (Sun 22:07), persona Bartl.
**Completed:**
- Startup: private ff-merge (up to date), read handoff `docs/pending-next-fmt-v13-safron.md`
- Verified AIW-94 fmt_formal §4.7 EXISTS (ground truth) → handoff item 1(a) is STALE, fmt_formal done S268
- Companion DOI added to refs — Gruber2026d now `@article` Zenodo `10.5281/zenodo.21610993` in both `.bib` (was @unpublished/in-prep) and `.md` reference line 1183. NOTE: current `paper.bbl` predates this cite → v13 build MUST re-run bibtex.
- Task-2 Safron PDFs ALREADY INGESTED (prior session Jul 13): `literature/fulltext/Safron2020.pdf` (IWMT), `Safron2022a.pdf` (AIXI-FEP-AI, byte-exact to handoff source), `Safron2022b.pdf` (G-SLAM, byte-exact). Windows Documents sources now gone (volatile). references.md lacks a Safron entry (minor).
- MG chose FULL PASS + tracked-changes PDF + "use fable freely" (S271)
- `.bib`: removed Wolpert orphan; added verified Yaron2022 (ConTraSt, Nat Hum Behav 6(4):593-604, doi 10.1038/s41562-021-01284-5) + NYDeclaration2024 (Andrews/Birch/Sebo)
- `.tex` full pass applied: 6 tell-opener removals, 3 defensive-tag trims, empty-sentence + hedge cuts, 150-word sentence split, antithesis reword, cross-ref repoint (§8.7→§3.4.3;§8.7), frame-rate reconcile (→20 Hz, drop "alpha"), dataset-count →$\sim$140 (7 sites; caught+fixed a double-tilde comgarra bug), +cites Yaron/NYDecl/Tegmark(Q3)/Gilmore(anosognosia)
- BUILD CLEAN: `tmp/build-full-v13/paper.pdf` 123pp, 0 undefined cites, 0 overfull>2pt, 0 errors; Gruber2026d renders w/ DOI 10.5281/zenodo.21610993
- Tracked-changes PDF: `tmp/build-diff-v13/diff.pdf` 123pp (latexdiff CFONT, baseline=HEAD paper.tex `tmp/paper-v13-baseline.tex`)
- Both staged: `tmp/v13-review/FMT-v13-CLEAN.pdf` + `FMT-v13-TRACKED-CHANGES.pdf`
**Key Decisions:**
- Publish is outward/irreversible → do all reversible prep + build + verify, present built PDF, get explicit go before running zenodo-upload.sh.
- fmt_formal §4.x treated as DONE (S268) — ground-truth §4.7 present; handoff line was stale.
**Recovery/Next session:**
- Handoff: `docs/pending-next-fmt-v13-safron.md` (Action: act). Backlog: AIW-121 (v13 epic), AIW-124 (companion, DONE/published).
- Remaining v13 members per AIW-121 [S267]: (1) fmt_formal §4.x = DONE; (2) final Fable pass; (3) publish.
- DOIs: master concept `10.5281/zenodo.18669891`; companion concept `10.5281/zenodo.21610993`.

