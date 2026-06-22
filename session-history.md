# Session History

Rolling window of the last 3 sessions. Newest first.

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

### 2026-06-18T23:35Z — WSL (home PC)
**Goal:** AIW-90 Track 2 (fly-connectome criticality — the 4090-feasibility question) + AIW-91 genesis (minimal critical spiking substrate spanning EWM+ESM; deep theory conversation with MG, logged verbatim).
**Completed:**
- **4090-feasibility answered**: spectral criticality on the full 118k-neuron connectome = **28 seconds** (GPU not even needed). Dynamical sweep = 82 min on CPU.
- **AIW-90 Track 2 spectral**: real ρ=0.76 (g*=1.31); E/I placement generic (z=+0.5); **weight arrangement non-generic (z=−50)** — real held near criticality where weight-shuffle blows to ρ=2.15.
- **AIW-90 Track 2 dynamical (68-run Brian2 sweep, DONE)**: REAL connectome reaches high-susceptibility (Fano) regime at **G≈1.8 vs G≈3.0 for weight-shuffled** — critical-like collective dynamics at ~half the gain of its scrambled null. Inverts the linear spectral prediction (topological, not eigenvalue, effect). Honest scope: criticality *precondition* organized signal — NOT fly consciousness, NOT FMT confirmation. Full result + nuances: `docs/connectome-track2-findings.md`.
- **AIW-91 opened (P0) + fully spec'd**: `docs/aiw91-minimal-critical-substrate.md`. Decisions locked (see below). Verbatim theory transcript: `docs/aiw91-conversation-verbatim.md`.
- brian2 2.10.1 installed; GPU setup commands in Notepad (`tmp/cuda-gpu-setup-commands.txt`, optional).
- Fixed dead PDF path in memory (monograph now at `…/Dropbox/DMS-Sync/Academic/book-consciousness-fmt/…`).
**Key Decisions:**
- **AIW-91 architecture (MG, S230)**: ONE recursive coder (MG's 2005 assumption; the book's "net-watching-net" picture is the bad/scrambled one — discarded). Target = **minimal HUMAN-LIKE** (confirmability). Prototype = **full RTX 4090 + simple cortex with two halves**; higher fidelity later needs a **body + simulated gridworld** (→ McFarnell ACU / simopt). Closure is **internal** (book p.281/p.67 + BCI/VR).
- **Two-axis consciousness onset + Class −1 (NEW, MG credited Bartl)**: basic consciousness needs BOTH minimum coding capacity AND significant **criticality persistence**. Class −1 = no criticality persistence; Class 0/null = too few surplus neurons (~<10^6–10^7). Class −1 ties directly to Track 2.
- **Levels = recursion depth** of the self-model (2015 book's "n-fach erweitert" ladder = base → +1 relation → +2 observation → +3 interaction → +4 undefined); discrete AND continuous. Artifacts use **2026 wording** (ISM/IWM/ESM/EWM); German = historical anchors only.
- **Language = niche-dependent linearization, NOT constitutive**; **LLM = language center (Broca/Wernicke analog) bolted onto the critical closure core, NOT the seat of consciousness**. Fastest world-convincing path = a conscious core that reports its self-model via an LLM. Roadmap milestone AFTER the base prototype.
- **Closure-is-generic (Track 1) does NOT undermine FMT**: FMT claims functional self-referential closure, not loop-density; discriminating evidence is criticality + functional self-modelling.
**Recovery/Next session:**
- Track-2 sweep is COMPLETE (`tmp/connectome-analysis/track2_dynamical_results.json` + `track2_dynamical_figure.png` + `sweep_out/*_trace.npz`). Summary: `10_sweep_summary.py`.
- AIW-91 build spec is `docs/aiw91-minimal-critical-substrate.md` (read first); theory rationale in `docs/aiw91-conversation-verbatim.md` (verbatim transcript — historically significant, MG's 2005 Innsbruck insight).
- Reusable criticality machinery: `tmp/connectome-analysis/_track2_worker3.py` (Brian2 LIF + Fano/MR fingerprints).

