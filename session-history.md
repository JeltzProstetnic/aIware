# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-07-05T23:22Z — WSL (home PC)
**Goal:** Implement the "simplest possible AC as planned" = AIW-91 minimal critical spiking substrate (closure-at-criticality kernel). MG wants to use Fable as the build model.
**Completed:**
- Startup: private remote ff-merged (clean), context surfaced
- Confirmed Fable 5 is reachable from this fleet (roster geo-block note is stale as of tonight)
- Located "the plan": `docs/aiw91-minimal-critical-substrate.md` (+ S230 crystallised decisions)
- Integrated Davos §9 (Zhuo Zou accidental-consciousness thesis) into the architecture
- Full architecture pass with MG → persisted as the "Session 242" crystallization block
**Key Decisions:**
- MG redirected tonight's work from the FMT v12 handoff to AC implementation (AIW-91).
- **Design locked** (details in the AIW-91 doc): genuine spiking LIF (Norse, NOT reservoir/ESN, NOT
  abstract units) · self-model EMERGES from embodiment · closure = the single experimental switch ·
  minimal-embodied first · **home = crucible** (its Python/Norse/PyTorch/Mamba-2 stack already fits;
  AIW-91 kernel = crucible Phase-1) · `Embodiment` seam = Gymnasium API (SimBody→CheapRobot→ProRobot) ·
  simopt: **fork** the FMT domain logic to Python (peer-review repro), keep ESN as a rate baseline ·
  cheap robot = sim→real dress rehearsal, match the pro's stack (ROS2/LeRobot).
- aIware owns the DESIGN; crucible will own the CODE.
- **Robot ORDERED 2026-07-06: Waveshare WAVEGO *Pro* Pi4 kit (direct Waveshare, ships AT, ~$415).**
  Feedback servos (position/speed/voltage) + 9-axis IMU → proprioception exposed. CAUGHT: the standard
  EX/PI4 kit (SKU 21745) = PWM/no-feedback — avoided; got the Pro. Pi4 fine (onboard compute irrelevant
  — ESM on PC per Libet split). Maps onto the Libet timescale-split (ESP32 fast onboard loop + Pi/PC
  slow ESM loop over WiFi).
- **Prior work exists:** AIW-91 has an S231 scaffold at `~/aIware/aiw91/` (5/5 tests, EWM decodable,
  closure dissociation; Fork A/B resolved; key finding = need balanced-E/I inhibition-stabilised
  substrate, NOT mere branching-criticality). Slice 1 EXTENDS this, not from scratch.
- **Fable finding corroborates an existing inbox item** (infrastructure filed 2026-07-05: "Fable NOT
  permanently geo-blocked → mark INTERMITTENT"). No new inbox item needed — already tracked.
**Recovery/Next session:**
- The plan: `docs/aiw91-minimal-critical-substrate.md`. AC repos: `~/mirror-box/` (Design 16, built) + `~/crucible/` (Design 15, scaffolded). Criticality machinery to reuse: AIW-90 Track 2 (`tmp/connectome-analysis/_track2_worker3.py` patterns, Brian2).

### 2026-07-05 (Session 241, evening, WSL) — WSL (home PC)
**Goal:** FMT paper v12 — land all content in the `.md` source of truth (Opus-4.8 + Fable-5 convergent-review fixes + original v12 items), commit; defer the `.tex` LaTeX port + build + Zenodo publish to next session (MG decision). Plus a Fable-5 content-gate re-test (gate is intermittent — banked).
**Completed:**
- Startup (git sync clean; private up to date)
- Fable-5 gate re-test: 4/4 fresh agents PASSED (S239's 6/6-refuse reversed → gate is intermittent). Persisted `docs/fable-content-gate/gate-retest-2026-07-05-S241.md`; decisions.md S241 entry added; cfg inbox content-gate item amended.
- Citation verification (2 background agents) — `docs/fmt-v12-citation-verification-S241.md`. Katlowitz→654(8119):714–723; 140-datasets→Hengen&Shew not ConCrit; Chowdhury single 19–45 Hz; 4 new refs verified.
- All review-driven fixes applied to `.md`: citations, Chowdhury retrofit, Table 5 FMT ●→◐ + footnote, abstract/conclusion reframe, close→narrow verb, priority trim, cosmology quarantine.
- Original v12 items in `.md`: AIW-89 olfaction §4.4, AIW-75 Passos-Ferreira §6.4 (+ citation-breadth grep-check, editor-fix decisions), AIW-96 already done.
- `references.bib`: Katlowitz vol/pages fixed + 4 new refs added.
- `paper.tex` REVERTED to clean S236 (so next session does one atomic port from the finished `.md`).
- Backlog AIW-89 / AIW-75 status notes; handoff `docs/pending-fmt-v12-zenodo.md` updated with the `.tex`-sync gap + port spec.
- Commit `.md` + `.bib` + docs + backlog (private remote).
- Logged Natalie K de Alma in `contacts.md` (Researcher #36, honest provenance note) — committed + pushed.
- Fixed cfg-agent-fleet uncommitted state from here (no cfg session needed): 2 commits pushed (`b58af81..486f1ed`) — verified push-tooling security hardening (tests 17/17) + all pending cross-project/session state from today's infra/social/aIware sessions. Working tree clean.
**Key Decisions:**
- **The `.tex` is 2 sessions behind the `.md`** (last touched S236; S239+S240 were `.md`-only). `build_full_pdf.py` compiles the hand-maintained `.tex`, so v12 CANNOT be built until the port is done. Casarotto 91.2% fabrication is still live in `.tex`. Reverted `.tex` to clean → atomic port next session. Full spec in `docs/pending-fmt-v12-zenodo.md`.
- Fable-5 gate is INTERMITTENT (headline for MG's LinkedIn "Will report"): S239 6/6 refuse → S241 4/4 pass, same day, same files. Explained partly by the cfg inbox note that Fable was temporarily re-enabled for EU 2026-07-05. Criticality-as-trigger: plausible CBRN secondary signal, not primary. Serving-model not cryptographically confirmed.
- Hard-Problem: Table 5 FMT ●→◐ + footnote notes IIT rests on the same primitive (MG-approved). v12 scope = all quick fixes; deep reframes deferred.
**Pending at shutdown:** New backlog item for DEFERRED deep reframes (type-B lineage resolution, ESM/EWM→primary pre-registered prediction, "solves→reframes" full abstract rewrite, 25–30% length cut) — surfaced by both reviews, out of scope for v12.
**Recovery/Next session:**
`.md` is the complete v12 source of truth (committed). Next session: port to `.tex` per `docs/pending-fmt-v12-zenodo.md` (§ "S241 UPDATE"), verified facts in `docs/fmt-v12-citation-verification-S241.md`. Never recompile canonical `paper/full/paper.pdf`; build into `tmp/build-full/paper-v12.pdf`. bibtex needs dangerouslyDisableSandbox.

### 2026-07-05T17:37Z — Steam Deck 2 (steamdeck2)
**Goal:** FMT paper v11 Opus review triage — bibliography audit BLOCKER first, then 8 MAJORs, then 7 MINOR/NIT. Per handoff `docs/pending-fmt-opus-review-triage.md`.
**Completed:**
- Startup: private-remote sync (up to date), config-repo dirty state noted, handoff read
- Add AIW-101 (P1) to backlog for this triage work
- Bibliography audit — 12 ref-list entries added (Fiser 2004, Fleming & Lau 2014, Koenig-Robert & Pearson 2019, Meisel 2012, Rahnev 2013, Rahnev 2020, Raichle 2010, Rouault 2018, Soon 2013, Stringer 2019, Tononi & Edelman 1998, Zheng & Meister 2025); metadata sourced from `paper/full/latex/references.bib` (all 12 already present in .bib — .md ref list was out of sync)
- Casarotto 2016 specificity fix — .md said 91.2% (not in paper); corrected to 100% benchmark + 94.7% MCS-sensitivity per WebSearch verification of Wiley abstract
- BLOCKER slice committed + dual-pushed (30ef1e5)
- 8 MAJOR revisions applied: #1 §3.7.1 scale hedge, #2 §7.2 scale-agnostic rewrite, #3 §4.4 Seth biological-naturalism engagement (~155w NEW paragraph), #4 §7.2 Doerig unfolding full paragraph, #5 §3.4.3 Chalmers metaphysical hygiene refinement, #6 §8.5 mPFC → ESM-network fix, #7 §8.5 Prediction 4 Statement functional-network framing, #8 §5.1 Alnagger "consistent with...show" reframe
- MG voice-approved drafting MAJORs (#3, #4, #5, #7); MAJOR slice committed (5ef44e8) + dual-pushed
- 7 MINOR/NIT revisions applied: #1 §3.7 preamble "Take neurons as..." stylistic; #2 §3.4.6 phenomenal-overflow FMT-response expansion (~110w); #3 §4.2.5 weak-illusionism consolidated to cross-reference of §3.4.5 (250w → 95w); #4 §3.7.3 "why not laptops" trichotomy signpost added at section start; #5 §8.4 cosine-distance illustrative-caveat; #6 abstract "no competing theory generates" softened per handoff (concedes PP/REBUS on Prediction 2); #7 §4.2.3 dense involuntary-extreme sentence split into 3
**Key Decisions:**
- Resume-as-planned per user directive after startup. Bibliography audit executes first because it is the submission BLOCKER identified in the Opus subagent triage.
- Fable-5 diagnostics NOT re-run this session (MG standing directive, per handoff §"Do-not-do").
- Tracked-changes.md variant left as-is until MG picks sync/delete/leave (per handoff §"Other pending items").
**Pending at shutdown:** shutdown. AIW-102 (conference/salon + book-signing + Vorarlberg lit-clubs) is next-up; MG to supply the Feldkirch literature-club contact name.
**Recovery/Next session:**
Read `docs/pending-fmt-opus-review-triage.md` for the full triage plan. Current step = bibliography audit. Session-history + `docs/conversation-log.md` note: log lags by 26 sessions (log at S213, HEAD at S239) — backfill needed at shutdown, not blocking this work.

