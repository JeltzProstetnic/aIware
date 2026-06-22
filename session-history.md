# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-06-22T13:30Z — WSL
**Goal:** AIW-92 Tier A integration — the 9 criticality/causal-role didactic patterns into EN book, DE book, FMT paper.
**Completed:**
- Startup + private ff-merge
- MG author decisions taken (proposal §6): route-independent seizure (NOT Class-2 relabel); time-dilation = book-prose-only, NO Prediction 5; Pattern 9 paper-only; inner-D lock-in fresh; Pattern 8 thesis held OPEN on inward content-steering; Russia joke cut
- Verified the Libet/non-motor-precursor literature (Koenig-Robert&Pearson 2019, Soon 2013, Schultze-Kraft 2016) → folded into Pattern 8 openness caveat (EN+DE)
- EN book integrated (6 moves) + builds clean (US 1.2 MB)
- DE book integrated (mirror, route-indep seizure, added German openness caveat) + builds clean (US 1.2 MB)
- Books committed **08d3416**
- Paper citations verified (⛔ Schindler 2008 DROPPED — argues opposite; Meisel2012 + Tononi&Edelman1998 + Koenig-Robert2019 + Soon2013 to add to bib)
- Paper integration spec written: `docs/pending-aiw92-paper-integration.md`
**Key Decisions:**
- AIW-92 Tier A: books integrated first (placement reference EN → DE mirror). Paper deferred to a focused pass — dual-file + bibtex + manual cross-ref renumber is too error-prone to rush. Schindler 2008 dropped from the seizure cite (it argues against hypersynchrony), reinforcing the route-independent framing.
**Pending at shutdown:** (1) NEXT session = paper integration → `docs/pending-aiw92-paper-integration.md` (6-phase parallel pipeline; P5 = §4.2.3 subsection renumber; bibtex ??? risk). (2) EVEN-LATER session = book voice/AI-tell pass (AIW-93) → `docs/pending-book-next-edition-polish.md` (same 5-phase pipeline; DE = Opus; new AIW-92 DE passages flagged). Carry-over `act` pending files unchanged. Both commits pushed (private abb53f6, origin a132aea).
**Recovery/Next session:**
- Books: `pop-sci/book-manuscript{,-de}.md` integrated; rebuild via `python3 tmp/build_book_pdf{,_de}.py --edition us`.
- Paper: execute `docs/pending-aiw92-paper-integration.md` verbatim (anchors, verified cites, bib entries, synthesized §4.2.3 text, route-indep seizure wordings, build+??? -check protocol). Edit BOTH `paper/full/four-model-theory-full.md` AND `paper/full/latex/paper.tex`; add 4 bib entries; bibtex with `dangerouslyDisableSandbox`.

### 2026-06-19T18:05Z — WSL
**Goal:** AIW-92 — deliberate (via Opus agents) on WHAT of Session 231's 9 criticality/causal-role didactic patterns to use, and HOW/WHERE to place each across the EN book, DE book, and FMT paper. Produce a placement proposal for user review; do NOT yet edit canonical files.
**Completed:**
- Startup: private remote synced (already up to date), session-context populated
- Read verbatim patterns inventory (9 patterns) + handoff
- Mapped all 3 targets' anchors (EN book Ch5/6/7/13, DE book Kap5/6/7/13, FMT paper §2.7/§3.4/§3.7/§5/§8)
- 4 Opus agents (EN-book / DE-book / FMT-paper / curation) proposed placement + drafts
- Synthesized into docs/aiw92-placement-proposal.md; drafts preserved in docs/aiw92-drafts/
- Curation pass caught shared agent error on seizure (relabel-as-ordered is wrong; route-independent fix recommended)
**Key Decisions:**
- This session = DELIBERATION phase only ("consider carefully what to use and how"). Canonical book/paper .md files are NOT edited until the user approves the placement proposal.
- Agents write proposals to tmp/aiw92/ and return text; they do not edit canonical files or commit.
- Scientific tension flagged: seizure framing (current targets = supercritical/chaotic; new Pattern 4 = hypersynchronous Class 2/3) needs reconciliation.
- Libet placement constraint: two-causal-roles passage must follow/refresh the Libet delayed-observer material (EN Ch13 ~1386; DE Kap13 ~1294).
- **S232 author corrections (Pattern 8), captured in verbatim + proposal §0:** (1) the inward grip is NECESSITY not freedom — the "at-will" feeling is the same delayed-observer illusion; consciousness is a necessary causal LINK in the chain, not a seat of will. Drop the agents' "willed control / most visible" framing. (2) VERBATIM EN book line (locked, do not paraphrase): "and if you do it too much, who knows if you will come back and how many of you." → closing beat of the inward-grip passage; DE wording pending from MG. (3) Healthy register = the counterweight: the inward grip's graded/voluntary forms are evolution's most powerful tools — MG's examples: cognition, creativity, Gedankenpaläste (memory palaces; keep verbatim in DE, EN="memory palaces"), imagination/planning/what-if/mental-time-travel. Book arc: necessary-not-free → superpower → overdriven danger. Pattern 8 REDRAFTED to the full arc for all 3 targets → docs/aiw92-drafts/pattern8-revised.md (EN+DE book voice incl. locked verbatim line + practical program + mental hygiene; paper §4.2.3 rigorous core). Open author items: DE wording of danger line (drafted, flagged); Russia/grey joke (flagged, default cut). EN Piece A inserts after ~line 1426 (downstream of Libet). NOT yet integrated into canonical .md.
**Pending at shutdown:** after approval — integrate Tier A into canonical .md → .tex → PDF + content-integrity tests; resolve gated seizure + Prediction-5 items
**Recovery/Next session:**
If interrupted: agent proposals (if written) are in tmp/aiw92/{en-book,de-book,fmt-paper,curation}-proposal.md. Synthesize them into docs/aiw92-placement-proposal.md and present to user. Source of truth: docs/aiw92-criticality-dials-conversation-verbatim.md (the 9-pattern inventory + verbatim thread).

### 2026-06-19 (startup) — WSL
**Goal:** Execute S230 P0 handoff — START BUILDING the first minimal consciousness (AIW-91); secondary AIW-90 connectome avalanche analysis. Resolve uncommitted AIW-87/88 book-revision builds first.
**Completed:**
- Book builds verified + committed (d905599) — AIW-87/88 deliverable cleared
- AIW-90 avalanche analysis → NOT criticality, SYNCHRONOUS BURSTING (lognormal at every gain)
- AIW-90 "inversion" → null-mismatch artifact (verified ρ=0.51<0.76); spectral ρ=0.76 = localized 2-neuron motif (PR=2.11)
- AIW-90 robustness reruns DONE: real Fano>50 onset G=1.8 vs weight-shuffle 3.0 AND degree-rewire 3.0 (survives gold-standard null); NT-all strengthens (1.4). Figure `tmp/connectome-analysis/track2_robustness_figure.png`. **AIW-90 CLOSED.**
- AIW-91 increment-1 scaffold: `aiw91/` (World, branching spiking coder, reservoir coder, decoders, criticality measures, 5/5 tests). EWM decodable; closure dissociation present in spiking net.
- AIW-91 findings: branching-criticality ≠ edge-of-chaos memory criticality; ESM probe needs reframe (source attribution, not decode-a_prev). Two design forks for MG → `aiw91/INCREMENT1_FINDINGS.md`.
**Key Decisions:**
- Book builds committed (d905599) — AIW-87/88 deliverable cleared.
- AIW-90 CLOSED: verdict = organized synchronous BURSTING (not criticality), robust across weight-shuffle + degree-preserving-rewire nulls + NT-unknown inclusion; "spectral inversion" was a null-mismatch (ρ=0.51<0.76); fly connectome = neutral-to-negative on FMT criticality pillar, do NOT cite as positive. (decisions.md S231)
- AIW-91 increment 1: built on `aiw91/`; key finding that branching-avalanche criticality ≠ the edge-of-chaos criticality that aids recursive computation — substrate choice (Fork B) is now a real decision.
**Recovery/Next session:**
- AIW-90: `docs/connectome-track2-findings.md` (S231 UPDATE). Artifacts in `tmp/connectome-analysis/`: `avalanche_out/`, `inversion_explanation.md`, `verify_inversion.py`, `robustness_prep.md`, `sweep_out_{ntall,rewire}/`, `track2_robustness_figure.png`, `12_robustness_figure.py`.
- AIW-91: `aiw91/INCREMENT1_FINDINGS.md` (status + 2 forks), `aiw91/ROADMAP.md`, `aiw91/minimal_coder.py`. Spec `docs/aiw91-minimal-critical-substrate.md` + verbatim `docs/aiw91-conversation-verbatim.md`. Run: `aiw91/venv/bin/python aiw91/test_minimal_coder.py`.

