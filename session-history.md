# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-07-06T16:50Z — WSL (home PC)
**Goal:** FMT v12 — run a significant adversarial-review team over the S243 philosophy block, consolidate, fix anything real, then (only after MG PDF sign-off) publish v12 to Zenodo. MG directive S243 said "Fable team"; Fable is geo-blocked to this fleet → substituting Opus 4.8 reviewers (sanctioned red-team substitute).
**Completed:**
- Startup + read handoff/pending; pulled S243 v12 diff (620c6524)
- 9-reviewer adversarial pass (4 Opus + 5 Fable — Fable AVAILABLE, gate down, ran clean on consciousness content)
- Consolidated findings → docs/fmt-v12-review-consolidated-S244.md (committed 96092349)
- MG chose Targeted humility scope; applied Tier 1 + Tier 2 + key Tier 3 to .md+.tex (committed 760bd610)
- Build clean: 116pp, 0 undefined cites, 0 undefined ctrl-seq, 0 overfull>2pt, 0 errors
- Opened paper-v12.pdf (clean) + paper-v12-reddiff.pdf (changes red) for MG
- Social notified (inbox — tweet candidate, wait for DOI)
- AIW-105 (qualia paragraph §3.4.2 + Prediction 5 §8.6, renumber, counts, 2 cites) — committed 46e0891c
- AIW-13 objection-defense briefing → docs/fmt-objection-defense-S244.md
- Full .md↔.tex parity sweep (subagent, MINOR-DRIFT) → all 4 fixed (Bayne/Storm sentences propagated, 2 xrefs 3.4.4→3.4.5); Table 1b float-number + Mago2026 key = deferred cosmetic
- Rebuilt clean 117pp (0/0/0/0) + red-diff vs S243 base (46 blocks); both reopened for MG
- Fable autonomous venue review → docs/fmt-venue-assessment-S244.md (paper=38k words=monograph; JCS double-blind = #1 solo; split+preprint+co-author path)
**Key Decisions:**
- **Fable IS available** (global since 2026-07-01, subscription-included through 2026-07-07; content-gate down) — the injected roster "geo-blocked/UNAVAILABLE" text is STALE (cfg inbox P1 tracks the fix). 11 Fable subagents ran clean this session on consciousness + cosmology content, no refusals. Corrected my mid-session mistake of trusting the stale roster.
- **Humility-propagation scope = TARGETED** (MG choice): abstract keeps its "category error" punch (+ one hedge "argued not derived, §3.4.3"); zombie §4.2.5 made conditional-on-constitutive-reading; §3.4.2/§4.3/§11 left confident. (AIW-13 briefing flags this as the #1 residual referee exposure — accepted tradeoff.)
- **v12 fix scope**: Tier1+2+key-Tier3 (9-reviewer consolidated) + AIW-105 (qualia paragraph + Prediction 5) + 5-item polish; full .md↔.tex parity restored (Bayne/Storm sentences propagated, Toker2022 drift removed, 2 xrefs fixed).
- **Publish GATED on MG's explicit PDF sign-off** — MG was reviewing ("so far all fine"), no final go. Deferred to next session.
- **Theory complex: keep at arm's length** (Fable complex-review directive) — FMT first standalone, RIM decoupled from FMT, cosmology last in a speculation-tolerant venue; disambiguate "recursion" (RIM feedback) vs "self-reference" (FMT/cosmology fixed point).
- **Full FMT = ~38k words / 117pp = monograph** (grew from 12.7k C&C version) — no journal takes it whole; JCS 9k carve (double-blind) is the #1 solo shot (AIW-106).
**Pending at shutdown:** Do NOT publish before MG sign-off (irreversible DOI). Changelog prepend still needed before upload.
**Recovery/Next session:**
Handoff: docs/pending-fmt-v12-fable-review.md (guardrails, remaining steps). Publish procedure: docs/pending-fmt-v12-zenodo.md §"Build v12 + publish". v11 DOI 10.5281/zenodo.20631497; concept DOI 10.5281/zenodo.18669891.

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

