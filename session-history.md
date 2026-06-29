# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-06-29T19:30Z — WSL (home PC)
**Goal:** S236 — execute AIW-92 (FMT paper integration), then MG-reviewed sharpening edits, commit+push, Zenodo v11, ResearchGate prep. COMPLETE.
**Completed:**
- AIW-92 FMT paper integration: P1–P7 in `.md`+`.tex` (two criticality dimensions §3.7; route-independent seizure §3.7/§10.3; presence→access §3.4.6; new §4.2.3 Two Causal Roles + renumber; §5.1 energy governor; §9 metacog double-dissociation) + 8 verified bib entries. 3 Phase-1 prep agents + 2 Phase-4 review agents (all GO).
- MG-reviewed edits: A §3.4.5 two-limits (instantiation vs extraction/legibility); B removed unbacked fighters sentence §3.4.4 (kept in book); C §4.2.3 inner≫I/O cite upgrade (Stringer2019/ZhengMeister2025/Fiser2004/Raichle2010, cf. Gruber2015 — 4 bib); D §9 focal-lesion→selective-dissociation (anti-modular).
- Build clean: 111pp, 0 undefined cites, 0 LaTeX errors, 0 overfull>2pt. 12 new web-verified bib entries total.
- Committed (b4fb3b63) + filtered-push (private full + origin filtered). Fixed WSL `~/.git-credentials` (added missing `JeltzProstetnic` line — covers all personal repos here).
- **Zenodo v11 PUBLISHED**: version DOI `10.5281/zenodo.21041760`, concept `10.5281/zenodo.18669891`. (Script auto-bump mislabeled it v5 from a stale draft field; corrected to v11 via metadata edit→publish API → AIW-99.)
- ResearchGate upload folder prepared + opened: `tmp/researchgate-upload/` (v11 PDF + UPLOAD-NOTES.md). RG has no API — manual upload by MG.
- `docs/references.md` updated (12 refs). Credential RCA + Zenodo-bug footgun filed (cfg inbox + AIW-99).
**Key Decisions:**
- AIW-92 run as manual parallel Agent calls (not Workflow — no opt-in): 3 read-only prep agents → integrator writing → 2 adversarial review agents. Locked S233 scope held (NO Prediction 5, route-indep seizure, §8 untouched/P7 is §9, no Table rows, un-numbered §3.7 block).
- Zenodo published autonomously (routine tested tooling, reviewed content, metadata editable post-publish). **Lesson: always pass `ZENODO_VERSION=vN` — the script's draft-derived auto-bump is unreliable (AIW-99).**
- §3.4.5/§4.2.3/§9 wording sharpenings made the paper anti-modular + convergence-forward (self-cite → mainstream support); book versions deferred to ed. 3 (AIW-98).
- Credential durable fix (JeltzProstetnic line) applied on WSL; systemic auto-fix escalated to cfg (3 same-day hits: furkansim, p0rn, aIware).
**Recovery/Next session:**
- Paper is live: committed (b4fb3b63), pushed both remotes, Zenodo v11 (`10.5281/zenodo.21041760`). Nothing pending on the paper.
- ResearchGate = the one open MANUAL step for MG: upload `tmp/researchgate-upload/Four-Model-Theory-of-Consciousness-v11.pdf` per its UPLOAD-NOTES.md.
- New backlog: AIW-98 (book ed-3 propagation, P3), AIW-99 (fix zenodo-upload.sh auto-bump, P3) — both pending MG priority confirm.

### 2026-06-25T19:55Z — WSL (home PC)
**Goal:** Startup triage + fix repo issues + low-hanging-fruit hygiene, then shutdown (night mode). AIW-92 FMT paper integration left untouched for a fresh focused session.
**Completed:**
- Startup: git-sync (global + private ff-merge) up to date; surfaced all SessionStart intelligence
- **conversation-log.md backfilled** — 6 genuinely-missing entries (226, 227, 228, 229, 231, 232) reconstructed from decisions.md + git (agent, Edit-only). S226 = honest reconstructed stub (no shutdown commit existed).
- **CLAUDE.md manifest completed** — added `## Reference` + `## Active Roster` sections (project-setup hook flagged both missing). Structural only, no behavioral rules.
- **4 stale `reference` pending files deleted** — all their tracked backlog IDs confirmed `[x]` done: pending-fmt-paper-session204-findings (AIW-64/65/66/67), pending-fmt-v9-revision (AIW-73), pending-v7-simopt-handover (AIW-51/01/68), pending-word-editing-protocol (cfg S40). 12 pending files remain.
- **Root-caused the recurring "conversation-log lags 213" false-positive** → it's cfg's `global/hooks/checks/06c-conversation-log-gap.sh:13` (two-hash `## Session` + `-m1` first-not-max). Filed precise fix as cross-project inbox item to cfg-agent-fleet (aIware's own `scripts/check-convlog-sync.sh` is already correct).
**Key Decisions:**
- Did NOT touch cfg-agent-fleet's hook directly (cross-project) — routed the 06c regex fix through the inbox with the exact one-liner.
- Did NOT start AIW-92 — night mode + it wants a focused fresh session; gated on MG anyway.
- Deleted only `reference` pending files whose every tracked ID is `[x]`; kept anything tied to an open/in-progress item.
**Recovery/Next session:**
- AIW-92: cold-load per PHASE 0 of `docs/pending-aiw92-paper-integration.md`; 6 edits P1–P6 + P7 (§8 metacog), each lands in BOTH `paper/full/four-model-theory-full.md` and `paper/full/latex/paper.tex`.
- cfg has pre-existing + newly-appended uncommitted inbox/dashboard-cache changes — a cfg session commits those, not aIware.

### 2026-06-25T08:58Z — WSL
**Goal:** Execute P0 metacog reanalysis (AIW-96) — open-data test of the FMT ESM/EWM double dissociation (d′⊥meta-d′).
**Completed:**
- Startup loading protocol (private ff-merge up to date; persona → Bartl; session-context populated)
- Confirmed P0 ≠ dropped AIW-47 (free-d′ data, not staircased Bonn) via scout handoff
- Reused validated pipeline (`metad_mle.py`, 4 tests pass); pulled Rouault Expt1 (n=498)
- Data integrity: type-1 d′ reproduces author fits EXACTLY (max|diff|=0.0019)
- Structural orthogonality (78% meta-d′ var ⊥ d′; M-ratio⊥d′ r=−0.20)
- EWM-axis: Rahnev contrast d′ 1.05→3.20 (p<1e-4), M-ratio flat (p=0.91)
- ESM-axis: Rouault published symptom result; TMS sets NULL (reported honestly)
- Deliverables → `docs/aiw-metacog-orthogonality/` (results.md w/ drafted §8 paragraph, figure, scripts)
- Backlog AIW-96 added (proposed P1); session-context updated
**Key Decisions:**
- Persona reset Elsa → Bartl (no frustration at neutral morning startup; Bartl is default).
- P0 confirmed NOT stale and NOT a reopening of AIW-47 (eNeuro stays dropped); deliverable = fold into FMT, not a standalone paper.
- Used Rouault authors' peer-reviewed Maniscalco–Lau fits (d′ reproduced exactly) rather than re-fitting; honest-convergence framing throughout (M-ratio⊥d′ is established Fleming&Lau, FMT consistent-with).
- Did NOT touch canonical FMT paper — drafted §8 paragraph for review first.
**Pending at shutdown:** (1) MG: integrate §8 paragraph? (coordinate w/ AIW-92 paper pass). (2) Optional extensions: ds001512 + CDB sweep. (3) Commit deliverables. (4) cfg inbox P0 item removal (needs cfg session — cross-project). (5) Append conversation-log entry.
**Recovery/Next session:**
- Queued next task (from S233): **AIW-92 FMT paper integration** → `docs/pending-aiw92-paper-integration.md` (6-phase pipeline, wants fresh context). Books already DONE/committed (08d3416).
- After AIW-92 paper: AIW-91 minimal-substrate modeling resumes; then AIW-93 book voice pass.

