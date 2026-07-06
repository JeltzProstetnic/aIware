# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-07-07T00:25Z — WSL
**Goal:** S246 — implement AIW-107 book ed.2 experiential restructure (15 Fable-review fixes) in EN then DE, build, publish ed.2 on MG sign-off. Opening = READER-FIRST. Spec: docs/fable-book-experience-review-S245.md; handover: docs/pending-book-ed2-implementation.md.
**Completed:**
- #1/#2/#3/#5 OPENING (reader-first): cold open "The Dot That Isn't There" (blind-spot demo → whole-field-fabrication bridge (non-sequitur fix, MG) → bridge epiphany → zero-copies), NEW figure `figures/blind-spot-test.png` (KDP-derived: 84.5mm sep, vanishes ~1ft), About-Author gutted 70→15 lines, Ch1 "One Razor" + Current-State compress + blind-spot callback, 286-beat→Ch5, age-11→AppB.
- #7 Ch2 architecture dump broken up (Five Nested→Ch6, How-Conscious ladder→Ch10, detonation staged, octopus forward-hook).
- #11 Ch4 waking-scene promoted to 2nd-person cold open + "The Self That Stitches Itself" close.
- Copernican→Ch10, Leibniz→Ch13 (relocated from Ch1 "One Razor").
- #6 Ch13 SPLIT → Ch13 "The Delayed Observer" + new Ch14 "The Only Freedom on Offer".
- #10/#14/#15 cosmology: spinning-rock refrains threaded; conservation-laws + three-generations compressed → new Appendix F; weak-points pile-up collapsed → new Appendix G + "The One Objection I Can't Answer"; forward last-lines.
- GLOBAL RENUMBER: old Ch14/15/16 → 15/16/17 (headings, Contents, cross-refs at Ch5/Ch16-17, endnotes). Chapters clean 1–17, appendices A–G.
- EN built (`python3 tmp/build_book_pdf.py`) → pop-sci/book-manuscript.pdf 265pp; cold-open page render verified (figure at correct KDP separation).
- FABLE GERMAN BANKED (while available): `drafts/book-ed2-de-new-prose.md` — native German for all 10 new-prose passages. FLAG: Innsbruck-bridge scene + sharp "zero copies" hook do NOT exist in current DE book → Fable wrote fresh German (needs MG eye).
**Key Decisions:**
- Opening = READER-FIRST; blind-spot demo uses a PRINTED figure (not "draw on paper" — MG); figure sized from actual KDP geometry (0.95·textwidth=105.6mm, marks at 10%/90% → 84.5mm sep, 15° blind-spot → vanishes ~1ft). Generator: tmp/make_blind_spot_figure.py.
- Non-sequitur fix (MG): after the demo, one paragraph establishes as mainstream neuroscience that the WHOLE visual field is fabricated (blind spot = where you catch it), THEN "you've never seen reality directly" as a conclusion.
- Fable IS available (roster note stale) — captured German now before subscription window closes 2026-07-07. "Don't be greedy": Fable only for the from-scratch creative prose (opening, German); Opus for relocation/staging.
- Do NOT auto-publish ed.2 — only on MG sign-off of restructured EN+DE builds.
- Do NOT rewrite protect-list passages — relocate/stage only.
**Recovery/Next session:**
- EN source of truth: pop-sci/book-manuscript.md (restructured, committed). Build: python3 tmp/build_book_pdf.py.
- DE source: pop-sci/book-manuscript-de.md (unedited so far). Banked new German: drafts/book-ed2-de-new-prose.md.
- Spec: docs/fable-book-experience-review-S245.md (15 fixes + protect-list). Handover: docs/pending-book-ed2-implementation.md.
- FMT v12 already PUBLISHED S245 (DOI 10.5281/zenodo.21226262) — that handoff is DONE.

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

