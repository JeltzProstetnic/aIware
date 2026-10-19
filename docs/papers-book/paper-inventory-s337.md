<!-- Action: reference -->
<!-- Tracked-by: AIW-289 -->
# Planned-paper inventory, S337 (2026-10-18)

**What this is:** every paper in aIware that is planned but not yet a journal article, plus planned journal
submissions of existing preprints. It covers the post-MoC7 papers, the papers the "No Outside" book invites, the FMT
slices and submission lanes, commentaries, computational papers, cosmology and RIM. It is the input for the
prioritisation step of AIW-289. **It contains no ranking.**

**Sources read:** `backlog.md` (full text of every open entry that is or plans a paper), `docs/papers-moc7/*-brief.md`,
`drafts/papers-moc7/`, `docs/pending-s335-handover.md`, `docs/pending-s337-papers-from-book.md`, `docs/decisions.md`
(S324–S337), `docs/fmt-venue-assessment-S244.md`, `docs/reviews/2026-08-24-plr-deadline-cost.md`, `ABOUT.md`, the
`paper/` and `drafts/` trees. Word counts are `wc -w` on the `.md` source, measured 2026-10-18. They include markup and
end matter, so they overstate the body slightly.

**Effort key:** S = under one session · M = one to three sessions · L = more than three sessions, or blocked on outside
work (experiments, co-authors, MG design input).

**Two standing rulings that apply to many rows** (quoted, `docs/decisions.md`):
- **S324 (2026-09-29) pause:** *"do not work on journals that have already rejected our submissions for now. especially
  not on anything that is not the FMT main paper."* Venues that rejected us: NCONSC (×2), PLREV, NBSR, C&C. Exception
  (S325): peer commentaries on other people's target articles are exempt (`AIW-228`).
- **S325 (2026-09-29):** PhiMiSci's AI-disclosure risk is decided *"once the JAIC slice is out, and there is no PhiMiSci
  work before then"*.

---

## A. Papers the "No Outside" book invites (AIW-289)

### A1. AIW-289 (1): core journal article from "No Outside"
- **Working title:** none yet.
- **Thesis:** from inside the universe, the known limits of mathematics and logic work as refutations of outside-view
  theories. Two limits hold unconditionally: there is no current generator, and no part can certify that its
  description is complete. The outside-the-universe view is not a perspective (S336 rulings).
- **State:** idea. Nothing drafted. Source material: book Ch 5, 6, 15 plus the Ch 1 rule
  (`drafts/monograph-limits/no-outside-draft-v0.6.md`, ~52k words, v0.6 PDF 107 pp, MG proofreading).
- **Venue / deadline:** none chosen. The S337 handover lists *Synthese*, *Erkenntnis*, *Philosophy of Science* and JCS
  as examples to check; guidelines must be read first (CLAUDE.md Submission Rules). No deadline.
- **Dependencies:** MG's proofread → v0.7 → Zenodo deposit of the book, so the paper can cite its DOI (S337 decision).
  Feedback from the four readers (MG's father, Ian Eisterer, Paul Schmidinger, MG's Kindle copy) is expected.
- **MG's words:** *"1 AND 3 even maybe. 2 is not a paper, its corrections we have to do anyways"* (2026-10-18). Order
  decided S337: *"paper 1 (core journal article) first; paper 3 … only if separable without overlap"*. Backlog tag:
  `[P1 — default, shutdown S336; MG to confirm]`.
- **Effort:** M–L (distil ~15–20k words of book chapters to journal length, venue fit, citation pass).
- **Overlap:** A2 (Ch 15 depends on Ch 14); AIW-285 corrections and AIW-288 (both FMT-side, not part of this paper).

### A2. AIW-289 (3): Ch 14, "the worm on the disk"
- **Thesis:** an inner world needs a realized, readable trajectory (D1). Rule plus initial state is only potential.
  Triviality arguments become in-world bookkeeping. Stored versus running.
- **State:** idea. Source: book Ch 14 (`drafts/monograph-limits/06-ch14-15.md`, 7,653 words for Ch 14+15).
- **Venue / deadline:** none.
- **Dependencies:** must be separable from A1 without overlap (S337 decision). Ch 15 depends on Ch 14.
- **MG's words:** *"3 even maybe"* (2026-10-18).
- **Effort:** M, if it is separable at all.
- **Overlap:** A1 (high). It also touches FMT §3.4.5 ("description and not an instance"), which is a correction
  candidate under AIW-285.

---

## B. Post-MoC7 papers (AIW-279..284, drafted S334)

S334 order (`docs/decisions.md` 2026-10-16): Definitions A first, then *"make the order of the other papers as you
like"* (MG). The agent chose theory map → robot plea → minimal self → Definitions B. All drafts are venue-neutral. The
S324 pause and the PhiMiSci deferral apply, so there is *"no journal-specific formatting until MG rules on venue"*.

### B1. AIW-279: Definitions B, "Deriving a Definition of Consciousness from Reference Systems"
- **Thesis:** a derivation from consciousness-free primitives (data → coding → information → interpretation →
  knowledge → reference systems are models → self-model). Calling the result "consciousness" rests on one identification
  premise, stated openly. Phenomenological definitions unpack into self-model + memory + report.
- **State:** draft, 8,822 words (`drafts/papers-moc7/deriving-the-fmt-definition.md`, 2026-10-17). It scores FMT on
  Paper A's C1–C9. The 2015 derivation was checked against the primary (`fmt-2015-derivation-check.md`, 5,750 words).
  That check resolves the "blocked on pp. 55–57" note in decisions.md S334.
- **Venue:** brief: PhiMiSci first (deferred by S325), then *Synthese*, *Philosophical Psychology*, *Mind and Matter*.
  Length 9–12k. No deadline.
- **Dependencies:** cites Paper A (AIW-278, waiting). Open decision 4 in pending-s335: the insect "only a now, no how"
  wording. FMT master fixes from S334 (capacity vs process, etc.) went out in v19.
- **MG's words:** backlog `[P1 — proposed]`. The brief recommends *"two papers, A first"*; merging is possible only for
  one PhiMiSci slot.
- **Effort:** M (venue choice, register sweep, final citation audit).
- **Overlap:** AIW-278 (merge candidate per brief §6); AIW-288 (definition of "model", now in the master §3.1); AIW-280
  (report dependence).

### B2. AIW-280: minimal self, "Too Late to Report: Why First-Person Methods Cannot Reach the Minimal Self"
- **Thesis:** reports pass through ESM + memory + language, so they reconstruct after reflection. Microphenomenology
  can track content but not minimal-self structure. A differential test ("minimal-self blindness") comes with a
  refutation condition.
- **State:** draft, 8,873 words (`drafts/papers-moc7/minimal-self.md`, 2026-10-16).
- **Venue:** brief recommends JCS (9k including references, double-blind), then *Phenomenology and the Cognitive
  Sciences* (limit UNVERIFIED) and PhiMiSci. Separate empirical companion → NoC Rapid Communication or registered report
  with a co-author. No deadline.
- **Dependencies:** open decision 5 in pending-s335: cite the MoC7 talks (Allen n=49, preliminary) only after asking the
  authors? Name Zahavi? Look for an empirical co-author later? JCS needs anonymisation, a 150-word summary and an AI
  statement.
- **MG's words:** `[P2 — proposed; MG S334: minimal self = basic ESM + sentience floor]`. Deep sleep is probably
  unconsciousness (S334). This supersedes the draft's "floor persists through most of sleep".
- **Effort:** M (check the draft against the S334 sleep ruling, venue fit, trim to 9k including references for JCS).
- **Overlap:** AIW-284 (post-hoc reports mean suffering would be silent); AIW-279; AIW-105 (report ineffability).

### B3. AIW-281: theory map, "Where the Theories Sit: An Architectural Coordinate System for Comparing Theories of Consciousness, with the Four-Model Theory as Reference Frame"
- **Thesis:** IIT, GNW, PP, HOT, RPT, AST, ICT, IWMT and others placed in FMT's architecture as absorbed, compatible or
  contradicted, each with a deciding experiment. Framed as a method, not as FMT promotion.
- **State:** draft, 9,999 words (`drafts/papers-moc7/theory-map-paper.md`), plus a wiki page draft, 1,887 words
  (`theory-map-wiki.md`), both 2026-10-16.
- **Venue:** brief: wiki first, then the paper. Candidates: NoC (paused under S324), Frontiers Psychology –
  Consciousness Research, PhiMiSci (deferred), JCS. Brief length target 6–8k; the draft is ~10k. No deadline.
- **Dependencies:** open decision 7 (PRM verdict, wiki-first order, frame alignment). The brief puts sequencing after MG
  decides AIW-146 §7: the theory map may be a chapter of the SMoC paper.
- **MG's words:** `[P1 — proposed]`. Chosen second in the S334 order by the agent, because *"its claim triples unblock
  AIW-276/AIW-277"*.
- **Effort:** M (cut to venue length, decisions) for the paper; S for the wiki page.
- **Overlap:** AIW-146 SMoC middle layer (merge candidate); AIW-276/277 (shared claim triples, `fmt-claims.json`);
  AIW-119/129 (vs-iwmt, vs-ict pages); AIW-243(2) (Mashour 2020 / Lau PRM missing from the master).

### B4. AIW-284: robot plea, "Silent suffering: a plea to consciousness science and robotics"
- **Thesis:** consciousness science should look at embodied, self-modelling robots, not LLMs, for possible artificial
  consciousness. Roboticists may build it by accident, and its suffering would be silent. Position against Metzinger's
  2021 moratorium: narrower and actionable (block negative valence).
- **State:** draft v1, 5,747 words (`drafts/papers-moc7/robot-consciousness-plea.md`, 2026-10-16). Header: *"Not yet
  register-gated or citation-rechecked by MG."*
- **Venue:** brief recommends a pre-submission enquiry to *Nature Machine Intelligence* (Perspective), with JAIC as
  fallback plus a short *AI & Society* piece. All length limits UNVERIFIED. No deadline.
- **Dependencies:** open decision 6: self-binding for the crucible robot (logging + pre-registered stop rules
  recommended), "servitude" vs "slavery", title. Co-author question (roboticist or animal-sentience researcher). The
  crucible robot disclosure touches AIW-206 (crucible implementation layer still under trade-secret freeze).
- **MG's words:** *"consciousness science should look at embodied robotics, not LLMs, for potential AC; roboticists will
  build it by accident sooner or later, if they haven't already"* (2026-10-16, as paraphrased in the backlog).
  `[P1 — proposed]`.
- **Effort:** M.
- **Overlap:** AIW-280; AIW-104 (SpikingMCU accidental-consciousness note); the JAIC slice (detector); AIW-141(b)
  ("select on function" firewall, cited in the brief).

### B5. Not papers (inputs to the B set, listed so they are not counted twice)
- **AIW-276** (Mudrik claims-as-graphs) and **AIW-277** (Vukovic platform): claim decomposition and a prediction map
  (`fmt-prediction-map-spec.md`, 8,637 words; `fmt-prediction-map.json`; `fmt-claims.json`). These are submissions to
  other people's programmes, not journal papers. MG: *"we want into Mudrik's program"*. Open decision 8: route via
  Negro, cc Mudrik.
- **AIW-282** (category theory explainer + answer card): explainer, not a paper. MG S334: *"CT stays small — D1/D2/D3
  only"*.

---

## C. FMT main paper: slices and submission lanes

The FMT master is a preprint, now v19 (`10.5281/zenodo.23427746`, 167 pp). MG's standing rule (AIW-191, 2026-08-08):
*"fmt main paper will be top priority of course"*. Timing rule (decisions S297): journals ride the conference,
preprints run ahead, *"a certain quality should be reached"*.

### C1. AIW-130 Lane B / AIW-62: JAIC, "An Operational Detector for Machine Consciousness…"
- **Thesis:** a substrate-neutral detector with three checks (self-attractor; closure gates the world-model update;
  open-ended computation), positioned as completing Kanai & Ma's ICCR.
- **State:** draft, 10,971 words (`drafts/aiw130-jaic-draft.md`, last edited S332 2026-10-07 for the criticality
  ruling). Plan, cover letter and verified-citation ledger are in `drafts/aiw130-*`.
- **Venue:** JAIC, Research Article, section "Assessing AI Consciousness", rolling, no APC noted; Kanai is EiC. The
  pre-submission inquiry (AIW-62, sent 2026-05-07) went unanswered. AIW-129 (FMT as the Φ-free patch to Kanai's ICT) is
  the warmer re-approach.
- **Dependencies:** Alen Frey is out (S302), so the §6 in-silico grounding is unowned. Still gated on MG: *"5 decisions
  (article type, time-dilation keep/cut, reviewer slates, name-vs-generic neuromorphic example) + pre-submission
  checklist … + `.tex` build + figure render"* (S276; decisions 3–5 recorded S281). JAIC has not rejected us, so the
  S324 pause does not apply. PhiMiSci decisions wait on this slice going out (S325).
- **MG's words:** AIW-130 `[P1]`; *"YES to both — the architecture slate … is CONFIRMED, and the six figures ARE to be
  rendered"* (2026-08-10). AIW-62 `[P2]`.
- **Effort:** M (author block, open decisions, figures, build).
- **Overlap:** AIW-129, AIW-104, AIW-284, AIW-141(b), AIW-152(b)/(d) (Arbeitsmodell + the closed-LLM breadth claim are
  routed to the JAIC slice).

### C2. AIW-130 Lane A / AIW-103: NoC special issue "Is There More to Consciousness Than Computation?" ("Why Is the Cortex Critical?")
- **Thesis (as drafted):** the "more" is computation on computation; criticality evidence; FMT's why-criticality
  explanation.
- **State:** draft, 8,860 words (`drafts/aiw130-noc-draft.md`, edited S328/S332).
- **Venue / deadline:** NoC special issue, **deadline 2026-12-31** (future: 74 days from today). Single-blind.
- **Dependencies:** **paused by S324** (NoC rejected us twice). ⚠ The thesis was built on criticality evidence. The
  S329/S332 rulings (*"consciousness requires free modeling and four models, not criticality!"*) retire necessity, so the
  draft's spine needs re-checking even though the S332 propagation pass touched it. The AIW-149 "does publishing the
  superset prejudice the subsets" question was meant to go to Kleiner at MoC7. That answer is not recorded.
- **MG's words:** AIW-103: *"high value, lets do that soon"* (2026-07-05). S324 pause quoted above.
- **Effort:** M, if the pause is lifted; the thesis may need rework after S329.
- **Overlap:** AIW-235 (different paper, same journal); eNeuro opinion and permeability paper (C6, C7, same criticality
  theme); theory map (NoC as candidate venue).

### C3. AIW-46 / AIW-106 / AIW-07: JCS 9k philosophy carve of the full FMT paper
- **Thesis:** the real/virtual split plus self-referential closure as a reframing of the Hard Problem. A carve, not the
  whole system.
- **State:** idea/plan. No JCS manuscript (`paper/jcs/` does not exist). The S244 Fable assessment rates JCS *"#1 SOLO
  shot"* (double-blind).
- **Venue:** JCS, 9,000 words including references, submission by email, no APC. No deadline.
- **Dependencies:** none external. JCS is also the first-choice venue for Definitions A (waiting) and the minimal-self
  paper, so these compete for the same journal. AIW-07 also lists AIW-48 (co-author) as a route.
- **MG's words:** AIW-07 `[P1]`, Decision S184: *"one more attempt at JCS as-is (AIW-46), then pivot the strategy
  entirely"*. AIW-46 `[P3]`, *"DEFERRED to rainy week, revisit end of July 2026"* (date passed). AIW-106 `[P2]`.
- **Effort:** M (the 2026-04 estimate of "3–4 hours" predates the master growing to 167 pp).
- **Overlap:** B2, Definitions A, A1 (all JCS candidates); C2.

### C4. AIW-235: NoC trimmed FMT paper, `.md`/`.tex`/`.docx` sync
- **State:** existing trimmed paper (`paper/trimmed/noc/`). The `.md` and `.tex` differ (footnotes, Gazzaniga 1965),
  the `.docx` is stale, and the abstract is 277 words against a 250 maximum. Body ~9,080 words against the Review
  Article limit of 10,000.
- **Venue:** NoC, which rejected this paper twice → **paused by S324** (decisions.md names AIW-235 explicitly).
- **MG's words:** `[P1 — MG-CONFIRMED S326]`, then paused by S324 (both dated 2026-09-29; S326 later re-confirmed P1).
- **Effort:** S–M.
- **Overlap:** C2.

### C5. AIW-48 / AIW-41: McFarnell co-authored registered report (*Cortex*)
- **Thesis:** an adversarial FMT-vs-ACU experiment. Vary uncertainty, affective significance and temporal pressure
  independently. FMT predicts affect loss → agency loss only.
- **State:** idea. The reply confirming the paradigm (AIW-41) has not been sent. Scott's proposal is dated 2026-03-29.
- **Venue:** *Cortex* Stage 1 registered report. No deadline.
- **Dependencies:** AIW-41 reply; a third collaborator with a participant pool.
- **MG's words:** AIW-48 `[P3]`, but its own text says *"this is now the single highest-value avenue for breaking the
  desk-reject pattern"*. AIW-41 `[P1]`.
- **Effort:** L (co-authors, design, data).
- **Overlap:** AIW-201 (pre-stated dissociation); AIW-134 TWCF.

### C6. eNeuro opinion, "Near-criticality does not set the level of consciousness: an architectural prediction, and how to falsify it" (paper/aiw47)
- **State:** manuscript, 3,945 words (`paper/aiw47/aiw47-eneuro-opinion.md`), double-blind, with figures and code.
  Retitled S332 *"by MG approval"* (decisions.md).
- **Venue:** eNeuro Opinion (~$1,945 APC noted earlier).
- **⚠ Tracking conflict:** AIW-47 is `[x]` *"DROPPED (not done) 2026-06-18"* (MG: drop the standalone eNeuro paper;
  the corrected ketamine reanalysis is a null). Yet the manuscript is still maintained and was retitled on 2026-10-07.
  No open backlog entry covers it. MG must say whether it is live.
- **Effort:** S if revived.
- **Overlap:** C2, C7.

### C7. Permeability paper, "Permeability as Directed Information Flow: A Transfer-Entropy Operationalization of the Implicit–Explicit Boundary…" (paper/fmt_permeability_criticality)
- **State:** manuscript, 3,646 words, PDF built. Created S245 (2026-07-06). Edited S332 for the criticality ruling.
- **Venue:** none recorded.
- **⚠ No backlog entry at all.** Status, venue and MG priority are unknown. The S244 assessment named *"permeability →
  anosognosia×psychedelic … → NoC SI/Frontiers"* as the empirical carve; this paper may be that carve.
- **Effort:** unknown.
- **Overlap:** C2, C6; the FMT formalization's permeability module.

---

## D. Commentaries

### D1. AIW-228: Physics of Life Reviews commentary on "Loops all the way up" (PLR 58, 360–381, 2026)
- **Thesis:** recurrency becomes relevant to consciousness when the loop implements modelling that closes on itself.
  Three points: the criterial slip, the UAT repair, the missing self level. Two findings that cut against MG (their
  Box 4 on von Neumann machines; criticality absent) must be handled.
- **State:** assessed (social, `~/social/docs/plr-loops-commentary-assessment-2026-08-21.md`). **No draft exists.**
- **Venue / deadline:** PLR comment, €0 on the subscription route. **No published deadline.** The empirical working
  deadline is **end of January 2027** (median 124 days after the target went online on 2026-07-24; 90% within 188 days;
  `docs/reviews/2026-08-24-plr-deadline-cost.md`). Recommended: a two-paragraph pitch to the handling editor first.
- **Dependencies:** none blocking. Exempt from the S324 pause (S325: MG chose *"Exempt commentaries"*).
- **MG's words:** `[P1 — MG-CONFIRMED S326]`; SOC-49 P1 in social.
- **Effort:** S–M (commentary length).
- **Overlap:** C1 (closure, recurrency).

### D2. AIW-14: COGITATE commentary (NoC Spotlight), PARKED
- **State:** draft, 1,587 words (`tmp/cogitate-commentary-draft.md`, limit 1,500).
- **MG's words:** `[P5]`; *"Not paying to fix their experimental design."* NoC APC €2,144. NoC is also under the S324
  pause.
- **Effort:** S if revived; revive only if fees or affiliation change.

### D3. Smaller reply/commentary targets (not yet papers)
- **AIW-142 (4)** Kirkeby-Hinrup & Stoll 2026: *"a clean convergence-note/reply target"*. **AIW-142 (5)** Birch's
  "Centrist Manifesto": *"Better as a considered blog/Substack comment than a tweet."* Both `[P2]`, no drafts.
- **AIW-214:** Seth's BBS author response is reportedly out (2026-09-17, subagent-reported, not verified). No paper is
  planned; it is input for C1/B4.

---

## E. Computational and theory side papers

### E1. AIW-219: span rule as a standalone paper (no consciousness claim)
- **Thesis:** the cost-minimal architecture at matched function, over a complete architecture space, is the bottleneck
  with span = support. Plus four failure-measured conditions and a self-inclusion corollary. Condition 1 sharpens
  Friedlander et al. 2015 and is not a discovery.
- **State:** literature check done (`docs/aiw219-span-rule-novelty-check.md`, verdict *"NOVEL BUT NARROWER THAN IT
  LOOKS"*). Nothing drafted.
- **Venue:** *PLoS Comput Biol*, then *Network Neuroscience*; arXiv q-bio.NC preprint regardless (but see AIW-08:
  endorsement is hard to get). No deadline.
- **Dependencies:** **"the drafting decision is MG's — write it or shelve it."** The highest-value follow-on is proving
  span = support. The results are crucible's; the AIW-206 freeze on the crucible implementation layer may apply.
- **MG's words:** *"hand this over to aIware"* (2026-08-14). `[P1]`.
- **Effort:** L (the proof upgrade, crucible data, a new field).
- **Overlap:** companion paper (AIW-140); AIW-166 (span law in cosmology).

### E2. AIW-105: qualia privacy, "reverse-invent the encoding"
- **Thesis:** qualia privacy is a decompilation problem. Quality-space structure is shareable across subjects; the
  absolute per-brain encoding stays out of reach. Three predictions, each with a refutation condition.
- **State:** draft, 4,316 words (`drafts/aiw105-qualia-privacy-paper-draft.md`, 2026-07-17). *"Awaiting MG review."*
  Five citations to verify; three inline author notes to resolve.
- **Venue:** none recorded. No deadline.
- **MG's words:** *"endorsed spinning the qualia-privacy point into its own paper with a more testable premise"*
  (S243, 2026-07-06). `[P2]`.
- **Effort:** M. The draft predates v15–v19, so it needs a consistency check against the master.
- **Overlap:** B2 (report), C3.

### E3. AIW-104: SpikingMCU-in-a-body technical note
- **Thesis:** an embodied spiking system plus an attractor world-model could instantiate minimal consciousness by
  accident, and detectably. Assessed against three criteria (self-attractor, closure, Class-4).
- **State:** idea. Analysis is in social (`davos-tech-summit-2026-research.md` §9).
- **MG's words:** *"might be cited if we get it published"*; *"not urgent, contingent — write when there is a clear
  citation path or outreach moment"*. `[P3]`.
- **⚠** Criterion (c), Class-4/criticality, predates the S329 ruling (criticality is a signature, not a requirement).
- **Effort:** S–M.
- **Overlap:** B4 (high, likely absorbed), C1 (the JAIC draft already uses SpikingMCU as its worked example).

### E4. AIW-120: Olinyk CRC ↔ FMT convergence note, "Two Roads to Recursive Closure"
- **State:** draft, 2,397 words (`drafts/aiw120-olinyk-crc-fmt-convergence.md`). Nine VERIFY items; the dossier is
  quarantined because of the Claude co-development circularity. *"Awaiting MG review."*
- **Venue:** Zenodo/blog (MG pivot: *"write a little paper that cites his CRC and hope he finds it"*). No journal.
- **MG's words:** `[P3]`.
- **Effort:** S.
- **Overlap:** B3 (theory map); AIW-119.

### E5. AIW-201: the capability-null inversion
- **Not a standalone paper by its own text.** The placement is *"candidate for the FMT master (it is a prediction, not a
  method) and for the OSF preregistration"*; the experimental half goes to crucible. Listed because it is a planned
  publication item. `[P1]`, confirmed by MG 2026-08-10. Effort L (needs a powered matched-recurrence design).

### E6. AIW-141: two candidates from CRU-57/60
- **Closed as a venue question** by MG S288: *"141a sounds to me like a small chapter in the computational paper, b
  good idea for later as note or also as rationale part in computational companion."* No standalone paper. (b) *"select
  on function, test the unselected consequence"* stays a possible later short note. The entry is still open.

### E7. Companion computational paper (AIW-140, ledger inside the AIW-218 entry)
- A published preprint (v4, `10.5281/zenodo.23216263`). No journal target is recorded. The open part is the claim-state
  ledger for future versions, not a submission. Listed for completeness.

---

## F. Cosmology and physics

All cosmology is under MG's S316 ruling: *"COSMOLOGY RESTS … no v7 is scoped"*. Since then v7 and v8 have been
deposited anyway (2026-10-07/08), for the criticality-ruling propagation and Class 5 work.

### F1. AIW-03: SB-HC4A to SSRN
- An existing preprint (v8 `10.5281/zenodo.23242055`). The action is an SSRN PhysicsRN upload. `[P2]`. Effort S. Not a
  journal submission.

### F2. AIW-63 / AIW-163: CMB multifractal paper
- **State:** published preprint, "Scale-Dependent Multifractal Structure in the Planck 2018 CMB…"
  (`10.5281/zenodo.20306785`, `paper/cmb_mfdfa/cmb-mfdfa.md`, 6,642 words).
- **Venue:** AIW-63: *"Target: Entropy or Phys. Rev. D."* No deadline.
- **Dependencies:** AIW-163: run the MFDFA instrument positive control *"before reporting the CMB null"*; *"[UNVERIFIED
  whether this was already done in Gruber 2026c — check first.]"*
- **MG's words:** AIW-63 `[P1]`, AIW-163 `[P2]`. S332 lists the CMB paper as *"out of scope"* for the criticality sweep.
- **⚠ Stale:** AIW-63's text (venv ready, SMICA URL 404) predates the preprint that exists now.
- **Effort:** M (positive control, then journal formatting).

### F3. AIW-174: Tsirelson bound from boundary capacity
- **State:** conditional derivation done (`drafts/aiw174-tsirelson-from-capacity.md`, 2,566 words). Proposed §6.5
  replacement text was *"NOT applied — awaiting MG"* at the time. `paper/cosmology/sb-hc4a.md` now has 8 matches for
  "information causality"/"Pawłowski"/"single-locus", so it may have been applied since. Verify.
- **Venue:** inside SB-HC4A. The entry notes that an "instructive failure … is itself publishable as a no-go". No
  standalone paper is planned.
- **MG's words:** `[P0]`, *"yes P0 next session together with 172"* (2026-08-07).
- **Effort:** S to confirm the state.

### F4. AIW-173 / AIW-84: saturation-trigger automaton experiment
- An experiment whose outcome is *"a citable result either way"*: an SB-HC4A upgrade, or *"a standalone companion
  note"* (AIW-84). AIW-173 `[P2]` absorbs AIW-84 `[P3]`. Not started. Effort L (compute + analysis).

### F5. AIW-165 / AIW-166 / AIW-186 / AIW-187: cosmology theory items
- Paper material only after their open items close. AIW-166: *"it is not paper material until all four close"*. AIW-165
  and AIW-166 are explicitly *"not scheduled"* (S316). AIW-186/187 `[P2]`. MG's binding discipline: never publish *"we
  are the universe's qualia"* (2026-08-08). Effort L.

---

## G. RIM

### G1. AIW-36 / AIW-227 / AIW-249: RIM to a journal
- **State:** preprint v6, *Motivation as Allocation Policy and the Mis-Typed Components of Intelligence*
  (`10.5281/zenodo.23081697`). Three desk rejections. Two rulings are open in AIW-227: Prediction 5 contradicts §5.2/§5.3
  and is unfalsifiable. One citation in AIW-249 (Dignath & Büttner 2008) has no owner.
- **Venue:** **MG 2026-08-10: *"NO APC MONEY FOR RIM"*.** *"RIM either stays a cited preprint or waits for a no-fee /
  fee-waived venue."* No candidate venue is recorded.
- **MG's words:** AIW-36 `[P1]`, but the outcome is decided: the preprint is the publication.
- **Effort:** S per correction; no submission is planned.

---

## H. Low-priority and parked

- **AIW-79:** FMT death/immortality piece. `[P5]`, *"post-fame"*. Note at `docs/fmt-death-immortality-note.md`.
- **AIW-08:** arXiv. `[P4]`, *"UNLIKELY"* (needs endorsement).
- **AIW-149:** the FMT monograph (the full paper as a book). `[P2]`. A book, not a paper. The recommended order puts it
  after the slices and after *"ask Kleiner in October"*. No outcome of that question is recorded.
- **AIW-146:** the SMoC middle layer. `[>] [P1]`, confirmed by MG S288. A web-first chart; *"optionally a standalone
  SMoC proposal"* (AIW-152). Six MG decisions in §7 are open. Possible parent paper for B3.
- **AIW-112:** Laukkonen note. MG made it a blog post (S265). Not a paper.
- **AIW-119:** Safron note. Sent privately on 2026-07-27; *"Ball in Safron's court ~Sep — do NOT nudge."* Not a planned
  publication.
- **AIW-259:** "Lizard-brain-myth" paper: mine it for numbers, never cite its conclusion. Not our paper.
- **AIW-10:** formalization roadmaps. All three are on Zenodo. What is open is collaborator outreach (MG *"wider
  first"*, six targets), not a paper.
- **AIW-06:** conference abstracts. 6ICPH Porto is still rolling. SAGE Adaptive Behavior (May 1, 2026) and AAAI Spring
  (Apr 7–9, 2026) have **passed**.

---

## Waiting (excluded from ranking)

### AIW-278: Definitions A, "Pointing Is Not Defining: the state of the definition of consciousness"
- **Thesis:** the accepted phenomenological formulations (Nagel, Block, Searle, Chalmers, IIT axioms, Schwitzgebel) are
  reference-fixers, as their own authors concede, not definitions. Plus evidence of non-consensus.
- **State:** draft, 8,999 words (`drafts/papers-moc7/definitions-not-settled.md`), two Fable referee passes, citation
  audit applied, PDF built.
- **Venue:** brief: JCS (9k including references) or PhiMiSci. Route: via Camilo Signorelli and the MoC7 consensus
  project, with MG hoping for co-authorship (S334).
- **Why waiting:** MG 2026-10-18: *"except the pointing is not defining thing, we are waiting for feedback from others on
  this first"*. Signorelli mail: the Gmail draft has been ready since S334. Whether it was sent is unrecorded
  (pending-s335: *"Check Gmail Sent for the Camilo mail"*, still untouched per the S337 handover).
- **MG's words:** `[P0 — MG S334: write first …]`.
- **Relevance to ranking:** B1 cites it and may merge with it; it competes with C3/B2 for JCS.

---

## Stale or contradictory entries found

1. **AIW-47 vs paper/aiw47.** The backlog says DROPPED 2026-06-18 (MG decision). The eNeuro manuscript was still
   retitled on 2026-10-07 *"by MG approval"*. Live or dead? No open entry.
2. **Permeability paper** (`paper/fmt_permeability_criticality/`) is not tracked anywhere in the backlog.
3. **AIW-130 JAIC draft byline** still reads *"Matthias Gruber · Alen Frey (provisional co-author …)"*, against
   *"Out of the paper is certain"* (S302).
4. **AIW-103 / AIW-235 / AIW-130 Lane A** carry P1 tags but are paused under S324. The NoC SI deadline (2026-12-31) is
   still ahead, so the pause and the deadline collide.
5. **AIW-130 Lane A thesis** (why the cortex is critical) needs re-checking against the S329 ruling that criticality is
   not required.
6. **AIW-223** is `[P0]` on a clock that has passed (*"before he leaves for Greece on 28 Aug"*). The harness shipped;
   the open part sits in AIW-233/224.
7. **AIW-63** is `[P1]`, but its text predates the CMB preprint that now exists. AIW-163 asks whether the positive
   control was already done.
8. **AIW-174** is `[>] [P0]` with text "awaiting MG". The cosmology source now contains the IC/Pawłowski material,
   possibly applied. Verify, then close or re-scope.
9. **AIW-141** is open although MG closed it as a venue question (S288).
10. **AIW-119** is open although the note was sent (2026-07-27) and no publication is planned.
11. **AIW-46** still points to *"AIW-49 (BBS commentary, deadline Jun 12)"*, which was rejected on 2026-05-29. Its
    "revisit end of July 2026" has passed. **AIW-07**'s pivot routes name AIW-47 (dropped) and AIW-49 (rejected).
12. **AIW-106** says *"Zenodo v12 (in progress)"*; the master is now v19.
13. **ABOUT.md paper table** is stale (AIW-254): FMT row says *"Preprint (v8)"* against v19; the companion says v2
    against v4; RIM-formal says v1 against v4; SB-HC4A-formal says v1 against v5. The eNeuro, permeability, CC, JAIC and
    NoC-slice manuscripts are not listed.
14. **AIW-36** is `[P1]`, although the venue question is settled (no APC, the preprint is the publication).
15. **S334 Definitions B blocker** ("blocked on checking the 2015 book pp. 55–57") looks resolved by
    `fmt-2015-derivation-check.md` (2026-10-16). The decisions entry was not updated.
16. **paper/cc/four-model-theory-cc.md** (13,344 words, the C&C version) is still edited in propagation passes. C&C
    rejected it, and S324 pauses C&C. It is not a planned submission.

---

## Facts relevant to ranking

**Deadlines (relative to today, 2026-10-18)**
- NoC special issue: **2026-12-31** (74 days), but paused by S324 (AIW-103, AIW-130 Lane A).
- PLR "Loops" commentary: no published deadline; the empirical working deadline is **~end of January 2027**. Exempt from
  the pause (AIW-228).
- Everything else has no deadline. Passed: BBS Jun 12; SAGE May 1; AAAI Apr 7–9; JCS "end of July" revisit; AIW-223
  Aug 28.

**MG-stated priorities (verbatim, dated)**
- *"fmt main paper will be top priority of course"* (2026-08-08, AIW-191).
- *"do not work on journals that have already rejected our submissions for now. especially not on anything that is not
  the FMT main paper."* (2026-09-29, S324). Commentaries exempt (S325).
- PhiMiSci: no work until *"the JAIC slice is out"* (S325).
- Definitions A *"write first"* (S334); now waiting: *"we are waiting for feedback from others on this first"*
  (2026-10-18).
- Other post-MoC7 papers: *"make the order of the other papers as you like"* (S334).
- No Outside papers: *"1 AND 3 even maybe. 2 is not a paper, its corrections we have to do anyways"* (2026-10-18);
  S337: paper 1 first, 3 only if separable.
- *"we want into Mudrik's program"* (AIW-276).
- RIM: *"NO APC MONEY FOR RIM"* (2026-08-10).
- Quality gates submission: *"a certain quality should be reached"* (2026-08-08); journals timed around conferences,
  preprints run ahead.
- Span rule: *"hand this over to aIware"* (2026-08-14); the drafting decision is still MG's.
- AIW-48 calls itself *"the single highest-value avenue for breaking the desk-reject pattern"*, but is tagged P3.

**Blockers**
- MG input: AIW-130 JAIC decisions and figures; S335 open decisions 4–8 (B1–B4); AIW-219 write-or-shelve; AIW-227
  RIM rulings; AIW-146 §7; status of the eNeuro and permeability papers; the S324 pause for any NoC work.
- Outside people: Camilo Signorelli (AIW-278); McFarnell plus a third collaborator (AIW-48); readers' feedback on No
  Outside (A1/A2); MoC7 authors' consent to be cited (B2); co-authors (B4 optional; NoC lane in S244's view).
- Internal sequencing: No Outside v0.7 → Zenodo DOI → A1; AIW-278 → B1 (cites it); AIW-146 decision → B3 format; JAIC
  slice out → PhiMiSci options (B1, B2, B3 alternatives).
- crucible: AIW-219 (span-rule data and proof), AIW-173 (experiment), AIW-201 (powered design). The AIW-206 trade-secret
  freeze on the crucible implementation layer bears on AIW-219 and on B4's robot self-binding disclosure.

**Venue collisions**
- JCS is the first choice for C3 (FMT carve), B2 (minimal self), Definitions A (waiting) and a candidate for A1 and B3.
- NoC is the candidate for C2, C4, the B3 alternative and the B2 empirical companion. All are paused.
- JAIC is the venue for C1 and the B4 fallback.

**Drafts closest to done (by state, not by value)**
- Full drafts exist for B1 (8.8k), B2 (8.9k), B3 (10k), B4 (5.7k), C1 (11k), C2 (8.9k), C6 (3.9k), C7 (3.6k), E2
  (4.3k), E4 (2.4k).
- Ideas only: A1, A2, C3, C5, D1, E1, E3.
