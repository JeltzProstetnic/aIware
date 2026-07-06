# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-07-06T09:55Z — WSL (DESKTOP-32ILURB)
**Goal:** FMT paper v12 — port the S239+S240+S241 `.md` review-triage delta into the hand-maintained `paper.tex`, build the PDF, then (after MG PDF sign-off) publish v12 to Zenodo. MG directive S243: "paper first, impl later" (AIW-91 crucible build deferred).
**Completed:**
- Startup: private remote up to date, S231 AIW-91 scaffold reviewed, S242 design read
- State verified: `paper.tex` at clean S236 (`b4fb3b63`, still has `91.2` fabrication); `.md` at S241 (`f792d9ce`); port delta = 98 lines (69+/29−)
- Port `.md` → `paper.tex` (45 hunks: 30 prose + 3 insertions + footnote; 16 ref hunks = BibTeX-side, done S241)
- Parity gate: `grep 91.2`→0; Casarotto 100%, Seth/olfaction/Passos/laptops present; Table5 both ◐; all cite keys resolve; no old-phrasing stragglers; no double-insertions
- Build `tmp/build-full/paper-v12.pdf` — 114pp, 0 undefined cites, 0 ctrl-seq, 0 overfull>2pt, 0 errors (content-integrity pytest absent from tree — tmp/ throwaway; verified via greps instead)
- Doerig "requires its own paragraph" FIXED — now its own paragraph, meta-phrase dropped (both .md + .tex)
- Hard-Problem ◐: kept, but ¶424 + footnote ‡ rewritten in .tex — malformed-question move + dropped IIT-leveling, foreground "FMT alone gives a reason" (MG S243). **.md mirror PENDING wording-lock (post-Fable-redteam + MG OK)**
- AIW-94 two-dials formalization — Fable verdict = MODERATE (NOT easy) → integration DEFERRED, banked to docs/aiw94-two-dials-formalization.md (tracked). Key: EXTENT=P∞ percolation genuinely new vs C_N; but seizure does NOT beat C_N (both go low); time-dilation law HARD/undelivered.
**Key Decisions:**
- MG S243 (2026-07-06): paper before implementation. FMT v12 is the resume target; crucible AIW-91 build deferred.
- `paper/full/latex/paper.tex` is HAND-MAINTAINED (exception to the never-edit-.tex rule) — the build compiles it directly; it must be edited to mirror the `.md`.
- Zenodo publish is IRREVERSIBLE (DOI) — hard stop for MG PDF sign-off before upload.
**Pending at shutdown:** AIW-91 crucible Slice-1 build (deferred per MG "impl later")
**Recovery/Next session:**
- Port spec = `git diff b4fb3b63..HEAD -- paper/full/four-model-theory-full.md`. Full checklist + what-NOT-to-do = `docs/pending-fmt-v12-zenodo.md`.
- Build: copy `paper/full/latex/` → `tmp/build-full/`, `pdflatex ×3` + `bibtex` (bibtex needs `dangerouslyDisableSandbox`). NEVER recompile canonical `paper/full/paper.pdf`.
- v11 DOI = `10.5281/zenodo.20631497`; FMT concept DOI = `10.5281/zenodo.18669891`.

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

