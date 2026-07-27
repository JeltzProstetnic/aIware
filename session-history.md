# Session History

Rolling window of the last 3 sessions. Newest first.

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

### 2026-07-26T17:35Z — WSL
**Goal:** Finish the companion paper (Gruber 2026d) per the S269 handoff — integrate the 12+ verified method-fills into the [[CRUCIBLE]] slots, rephrase the 5 KEEP-AS-PLACEHOLDER items as prose, insert the 6 verified citations, build the PDF for MG review. **Zenodo publish is HELD by MG** (irreversible + possible pending real crucible maintenance result).
**Completed:**
- §4.1 (planner) CRUCIBLE fill
- §4.2 (survival) CRUCIBLE fill
- §4.3 (transfer) CRUCIBLE fill
- §4.4 (criticality computes) CRUCIBLE fill
- §4.5 (B0 spiking) CRUCIBLE fill
- §4.6 three-way closure CRUCIBLE fill
- §4.6 leaky-ESN CRUCIBLE fill
- §7 (CRU-36 null) CRUCIBLE fill
- §6.3 (design) preregistration-pending prose
- §6.3 (transfer DV redesign) prose
- §8 (biological signatures) proposed-direction prose
- §9.1 (thinking-time) prose "proposed, not implemented"
- §9.2 (taxonomy) prose "demonstrated / under build / proposed"
- References: 5 DOIs + ISBN inserted; Gruber 2026e suffix confirmed
- Burghardt honesty caveat added at §9.2 in-text
- Header comment updated with S269b log
- Draft grep clean: zero live `[[CRUCIBLE]]`/`[[VERIFY]]` markers in body
- **Build PDF — DONE on WSL (S270): exit 0, 0 overfull boxes, 16pp, tmp/companion.pdf. Fixed unicode-header (⁷ superscript + ö/ï) + author-line \hbox overflow. Committed c5820130, pushed private+origin (origin divergence re-resolved via fetch+filtered force-push).**
- **S270 restructure per MG: companion → results-only report.** Cut former §5 (decisive test), §6 (discriminating prediction/prereg), §8 (bio-signatures direction), §9.1 (thinking-time DV) — each gets its own report; full pre-revision text at git c5820130. Removed §9.2 taxonomy (MG: not his, ordering backwards, no tenable linear metric). De-bloat + de-AI. Body 8543→~5100w, PDF 16→10pp. NO number changed (Methods byte-identical). Refs pruned to cited-only. Committed 11f49df3.
- MG review + revisions — results-only restructure, full de-AI/anti-tell sweep (Fable-hunted), meta-science register cut, abstract stripped of CRU codes. MG-approved.
- **Zenodo publish DONE (S270): companion concept DOI 10.5281/zenodo.21610993** (v1 21610994) — CC-BY-4.0, isSupplementTo master FMT **concept** DOI 18669891 (corrected from stale version 18861613). Linked in public README.md + ABOUT.md.
**Key Decisions:**
- **S270 — companion is a RESULTS report, not results+plans (MG).** Future experiments (scaled decisive test, closure×criticality prediction/prereg, biological-signatures direction, thinking-time DV) get their OWN reports; removed from this paper. Seed = git c5820130. Full rationale in docs/decisions.md S270.
- **§9.2 modelling-capability taxonomy REJECTED (MG) — do not reintroduce.** Not his; ordering backwards (tool use simpler than free modelling); and a direct/linear/easy metric of modelling capabilities is not tenable in principle.
- De-AI/de-bloat is a standing expectation for these papers ("blown up", "ai tells / aidioms"): plain scientific prose, no coined flourishes, no not-X-but-Y chains, restrained bold/em-dashes.
- **Companion PUBLISHED to Zenodo S270 (2026-07-26): concept DOI 10.5281/zenodo.21610993 (v1 21610994).** MG lifted the hold and authorized publish. CC-BY-4.0 preprint, isSupplementTo master FMT **concept** DOI 18669891. **MG rule: always cite the generic/concept DOI, never a version DOI** — README/ABOUT + the Zenodo record all corrected S270. Abstract stripped of internal codes (CRU-36) per MG — codes kept in body.
- Fable will be tried for the FINAL FMT review step if we get there; the "unavailable" system reminder is 5+ weeks stale (2026-06-17), user overrides. Not reached this session.
- Opus 5 — no distinct `Agent(model=...)` selector; `opus` selector maps to whichever Opus the harness runs.
- §4.1 dropped in S269 — every fill mapped by CONTENT, not old number.
- PDF build MUST use `-H paper/fmt_formal/unicode-header.tex` — `paper/_shared/latex-preamble.tex` alone doesn't declare σ / λ / ↔ / ≥ / ≤ / ≫ / ∈ / · / α / Δ / ε / τ / Σ.
- Committed 7e28baa; pushed to **private** and origin. Filtered push succeeded (origin 90089e3→1c04d7a) after the initial stale-info rejection resolved on retry with the additional session-context commit (a3266cd).
- **Deck 2 is not a paper-build env — confirmed and reaffirmed 2026-07-25.** Explored installing pandoc + LaTeX on Deck 2 (three disk-space failures on SteamOS's 5 GB `/`; even TinyTeX would have worked but the fundamental risk remained). MG reconsidered: even a working Deck-side build would render a *different* artifact than WSL/Fedora-home's canonical rendering (font-version drift → page-count drift → possible KDP cover-spine breakage) and mixing the two across a review cycle invites "why did the layout change?" incidents. **Reaffirmed rule: aIware paper/book PDFs build ONLY on WSL (canonical) or Fedora-home; the Deck 2 machine-file "LaTeX not installed" note should stay as an active guideline.** Cross-project inbox item filed to strengthen the machine-file wording.
- **Self-critique to log:** I bent on the machine-file guideline too readily on first push-back ("wait can't you install"). When a machine file has an explicit "not for this purpose" note, the correct response is to explain WHY the constraint exists first, then only proceed if the user's reason overrides the stated tradeoff — not to immediately produce install options. Three round-trips through disk-space failures were the cost of that.
**Pending at shutdown:** 20 other aIware `pending-*.md` files untouched — reserved for a later triage sweep.
**Recovery/Next session:**
- Draft: `drafts/companion-computational-paper-draft.md`. Handoff: `docs/pending-companion-2026d-fills.md` (updated with S269b state).
- To resume on WSL/Fedora: `git fetch private && git merge --ff-only private/main`, then run the PDF build command in Next Session Task.
- If PDF has overflow, `check-pdf-overflow.sh` fails exit 3 — read the log at `/tmp/…/*.log` for the exact overfull line.

