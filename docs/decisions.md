# Decisions Log — aIware

Curated record of strategic decisions and rationale. Topic-organized, not chronological.

Last reviewed: 2026-10-24

Monthly review S358: superseded and executed entries were moved verbatim to `docs/decisions-archive.md` (see the
Archive Index below); every remaining entry was compressed to decision + rationale, and entries stating the same
decision were merged (all dates kept). The full pre-compression text is in git: `git show HEAD:docs/decisions.md`
(HEAD = `1b133de8` at review time).

## 2026-10-24 (S358) — publication fees; AIW-343 study set-up

- **No publication fees except for first-class journals or the main FMT paper.** MG verbatim: *"i am not going to pay for publishing in an obscure journal, and they will desk reject all the same i fear, i'd only be ready to pay such sums for 1st class journals or for our main fmt paper"*. Consequence: eNeuro Opinion (US$1,945) is out for the near-criticality Viewpoint (AIW-290). Elsevier transfer targets count only if they have a no-fee route. Every venue list from now on marks APCs and flags any fee venue below first class as excluded.
- AIW-343 (cheap drug-free FMT discriminator, P0). MG's decisions: English first, then DE/IT/FR; MG recruits personally and clears it with the employer himself; MG personally is the data controller; Michael Netzer (UMIT) is co-investigator; no linking code, so the data are anonymous and qualify for the RCSEQ fast track; dualism measured with the Riekki 6 + Navarro-Peña 5 items; death anxiety with DABBS, while T&F is asked about the Templer DAS. Kit: `drafts/aiw343-study/README.md`. Rival theories are allowed to retrofit afterwards; a priori pre-registration is the win.

## 2026-10-23 (S355) — falsifier baseline, Kleiner placement, Unterhofer call
- **AIW-320:** Table 1b's free-modelling falsifier compares against an unrolled feedforward model of matched capacity trained on the same history. Why: it differs from the FMT system only in the closed loop; a fitted lookup only tested generalisation.
- **AIW-322:** the reply to Kleiner & Ludwig 2024 is one short §7 paragraph, framed as a reply to the 'dynamical relevance' premise. Why: a subsection hands a NoC editor more surface; a footnote reads as dismissive.
- **No Outside colons:** left as they are (2.7/1k, ordinary explanatory use; density rule).
- **AIW-337 (Mallavarapu & Percy process no-go):** reply only if the preprint is published in a peer-reviewed venue (MG).
- **Theory map → RoPP (AIW-281):** v3 cut to journal length (~9.3k words, verdicts unchanged) published as v3; submitted without the second coder (D9). Supplementary files are part of the anonymised package and get scrubbed like the manuscript.
- **Submission mail (MG):** journal-system mail goes to Gmail label `Bartl/Submissions`, skips the inbox; kept, never part of the Bartl trash loop.
- **Unterhofer (AIW-328):** he proposes the call slot; funding is raised in the call, not by mail (MG cut the no-budget question).

## 2026-10-22 (S353) — No Outside v1.0.2 order; substrate reversibility loosened
- **No Outside v1.0.2: content fixes first, then one de-patterning pass over the whole book, one MG read at the end** (MG). Why: new §10–11 text gets de-patterned with the rest.
- **SB-HC4A §8.4: injective rule → reversibility of the realised dynamics** (MG, AIW-334 Q1). Why: the boundary–interior bookkeeping needs information conservation along the realised trajectory, which a finite beginningless substrate supplies even under a many-to-one rule (only cycle states occur, one predecessor each).
- **SB-HC4A's next version is deposited together with No Outside v1.0.2** (MG). Why: v1.0.2 cites the loosened §8.4.
- **Inverted-GoL cosmology parked as speculation** (MG, AIW-334 Q2). Why: a selection rule adds nothing, count-based branching cannot give Born weights on finite boards (CRU-223), ontic chance contradicts SB-HC4A §3.2.
- **RIM cites the Fig. 11 MOTSKIL coefficient in one sentence** (MG), via Ackerman's personal communication tied to Ackerman, Kanfer & Goff (1995, p. 276), as fluctuation around the level, not as support for Prediction 8.
- **§10.4 keeps "Physics has no office for refunds."** (MG: *"keep its brilliant"*).

## 2026-10-21 (S348) — No Outside release line; Worm venue; MoC7 cites
- **Too Late to Report → *Phenomenology and the Cognitive Sciences*, submitted** (MG; PHEN-S-26-01071 (final PHEN-D-26-00933)); v2 on Zenodo first so reviewers see the same text.
- **MoC7 presentations are cited without asking the presenters** (MG): public talks/posters with programme abstracts.
- **The Worm on the Disk → *Minds and Machines*** (MG). Why: philosophy-of-computation scope; independent of the Hard Problem paper at Synthese. One paper at M&M at a time (the Detector fallback was also M&M; see S356 D9). **[S359: 'one at a time' RETIRED (MG) — the slice goes to M&M while the Worm (MIND-S-26-01918 (final MIND-D-26-01583)) is under review; reviewer lists kept disjoint.]**
- **No Outside release PDF: no version on the title-page line** (`--release` prints the date only, from the next deposit). Why: matches the KDP edition.

## 2026-10-21 (S347) — JCS reject, Synthese, Zenodo v1.0.1, priorities
- **No Outside v1.0.1 → Zenodo** (MG via simbook; 10.5281/zenodo.23514845). Why: v1.0 states the overstated Kleene slogan.
- **Hard Problem paper → *Synthese*** after the JCS desk reject (SYNT-S-26-04632). Why: no word cap, double-blind, free route.
- **JCS: ask Horswell first** whether a computational paper would suit, rather than sending one blind.
- **Priorities:** AIW-317 P1, AIW-319 P1, AIW-320–322 P2. Membership applied for = AMCS. Pace = one submission per session.
- **Synthese keywords:** "meta-problem" dropped (4–6 limit).

## 2026-10-20 (S345) — browser logins: fill from the vault
MG: *"in, next time you do that"*. When a login's credential is in the vault, the agent fills it via the /dev/shm bridge (`~/.claude/knowledge/dev-browser-ops.md`), never via `browser_type` and never by snapshotting the login page.

## 2026-10-20 (S345) — journal submissions: MG checks every new text first
MG: *"halt at every step that would make you enter new text longer than a few words so i can check"*. Any new text longer than a few words for a submission (portal field, cover letter, comments, highlights, title page, AI declaration) is shown to MG and entered only after his check.

## 2026-10-20 (S345) — venue rulings (AIW-292, `docs/papers-book/venue-reassessment-s345.md` §4)
- D1/D2: one non-JAIC submission per session, in order: paper 1 → Logique et Analyse; falsity gradient → SHPS; Too Late to Report → Phenomenology and the Cognitive Sciences; theory map → Review of Philosophy and Psychology; criticality opinion → Cortex Viewpoint; NoC slice → Minds and Machines.
- D3: skip the NoC special issue (rejected us twice, single-blind, US$3,625, no free route). D4: PhiMiSci deferral kept (fallback only). D5: Cortex Viewpoint, not eNeuro.
- D6: RIM preprint stays the publication until AIW-227 closes; then RGP only at no fee.
- D7: **JAIC: wait 10 days from the 2026-10-19 enquiry** (MG: "we wait 10 days") — from 2026-10-29 the detector paper may go to JAIC via Editorial Manager unasked.
- D8: preprint DOI only where the venue asks and in the cover letter, never in the anonymised manuscript.
- D9: theory map submitted without the second coder; coding added in revision.

## 2026-10-20 (S345) — handover decisions (merged with S346 and S350 on the independent coder)
- IIT "digital duplicate" stays folded into IIT-1 (master §3.7.3); no theory-map v2 for it.
- Paper 4 Metzinger citations: trim to one neutral credit in a v2 (`AIW-315`).
- **Independent coder (`AIW-313`):** ask the Blums first, for the CTM rows (S345); the first contact leads with the free website + software offer (`AIW-314`), the coder/co-author ask second (S346, MG); wait for the Blums, no parallel ask (S350, MG).
- Coder kit: claim lines in the rivals' own terms, not FMT's.

## 2026-10-20 (S345) — Def A: hold the preprint until Signorelli reacts (merged with S342)
MG, final: *"hold the definitions preprint until signorelli has reacted after his vacation"* — "Pointing Is Not Defining" is not deposited until Camilo Signorelli reacts (away until 31 Oct); the Gmail draft to him carries revised draft 2, not a DOI. Co-authorship stays open for a journal version. History: S337 and S342 "wait for Signorelli"; earlier in S345 MG ordered *"when done, preprint and update via mail to signorelli (draft only)"*, then revised it the same session.

## 2026-10-19 (MG via infrastructure) — "No Outside" main-site links are paid-only
matthiasgruber.com links "No Outside" only through the sales page `matthiasgruber.com/no-outside.html` (Amazon); no main-site page links the Zenodo DOI 23473517 or research `/no-outside/` (infra test-enforced). The research site keeps the open DOI. Never send infra the DOI for the main site. Rationale: main site = commercial storefront; research site = open-access home.

## 2026-10-19 (S341) — REV-1, SK-1, PP-2
- **SK-1:** Skeptic pitch approved; Gmail draft (from matthias@matthiasgruber.com) to articles@skeptic.com, pitch only; the 1,400-word draft is sent if they ask.
- **REV-1:** all fix proposals in `docs/aiw288-master-fix-proposals.md` approved; "gating" → "selection" throughout (OQ7: "the basal ganglia role in setting permeability").
- **Master review "changes approved"** (34 fixes + Predictions 6/7, C5-2, C9-1; Sewell cited 2013); **FMT v20 published** (10.5281/zenodo.23477765). PP-2: D11 Friston node added (map 46 claims, over the 45 cap, MG).
- **PLR Loops commentary approved. Body-first attractor (MG idea):** the first attractor in a body-coupled spiking network comes from body feedback, so brains started as body representations (after nerve nets that coordinate without representing) → commentary §3; next master §3.4/§4.4; crucible test. Prior art: Keijzer, van Duijn & Lyon 2013. Kept out: any claim that the self-model is older than the world-model (ESM sits inside EWM).
- **Web links for approved drafts (MG):** Zenodo preprint first, then infra links the DOI. Skeptic article and JCS carve stay off the web (magazine pitch; double-blind).
- **Accessible content (MG):** *"explicit models may be subconscious, by not entering the self model"* — accessible (preconscious) content may sit in an explicit model outside the self-model's closed loop and becomes conscious by entering it. §3.4.6: "explicit content that enters the closed loop IS experience". Consistent with 2015 *Vorbewusstes* (p.68).
- **Facts (social Gmail audit):** OSF/PsyArXiv RIM preprint closed 2026-09-23, notice points to Zenodo 10.5281/zenodo.20125095; MoC7 board was P56 (mails conflicted with P60).
- **PP-2:** C2 ("action necessary") and D10 ("life needed") stay. A3 (beast machine): MG leans keep — *"seth is taking too much oxygen and needs attacking by his own peers"*.

## 2026-10-19 (S340) — No Outside published; worm paper gets figures and publishes
- **Figures:** the survey minimum (`drafts/monograph-limits/figures-survey-s339.md`) redrawn in one B/W vector style by `scripts/build_no_outside_figures.py`, plus the Müller-Lyer figure — 8 figures.
- **No Outside v1.0 published** (MG: *"publish now"*), CC BY-NC-ND 4.0.
- **Ownership (MG):** *"no outside: from now on simbook job, unless more theoretical work comes along, it has all the kdp knowledge."* aIware keeps the sources and any theoretical revision.
- **PP map (MG):** *"make our own, let mudrik rot for a while, her last answer didn't show any interest in our work. we can inform her in a few days."* We draw the PP map ourselves, labelled as drawn by us from PP's published sources; Mudrik is told after go-live (MUD-1); their app's unlicensed "AI" claim list is not used.
- **Worm paper (MG):** *"the figures also must go in worm on the disk which can then also be published immediately."* Open points take the recommended defaults; the three unchecked references must still pass the reference gate.

## 2026-10-19 (S339) — undrafted papers, §8 additions, C9 scope, cross-theory links
- **Undrafted papers:** set 1–5 chosen and drafted (PLR commentary, Skeptic response, worm on the disk, falsity gradient, JCS carve; `drafts/papers-s339/`). 6 span rule: MG's write/shelve call. 7 SpikingMCU (AIW-104): absorb into the robot plea. 8 McFarnell RR (AIW-48): low priority; option of our own study (100+ Ivoclar researchers or ~100 people from the street). 9 AIW-142 small replies: to social after drafting.
- **Master §8 (S8-1, MG "Both now"):** C8-1 and C5-1 → Predictions 6 and 7, C5-2 a planned in-silico test, with AIW-288 (`docs/proposed-master-s8-additions.md`); the "after an ACW pilot" recommendation overruled.
- **C9 scope (C9-A): §5.1 binding = field unity only.** Feature-to-object assignment is content computed by implicit spatial models; FMT owes no account of illusory conjunctions (`docs/c9-binding-evidence.md`).
- **Correspondence address** in new drafts: research@matthiasgruber.com (not matthias@).
- **AIW-299, AIW-300: P2** (MG); AIW-300 scope: all theory pairs.
- **No Outside → Zenodo (MG):** *"no outside should go to zenodo right after one last review (NOW)"* — v0.7 = 8 proofread notes + one Opus review pass (NO-1); W8 recommendations accepted (NO-2); licence **CC BY-NC-ND 4.0** (NO-3); KDP paperback/hardcover + a non-Select ebook, accepting possible price-matching (NO-4; Select forbids a free PDF elsewhere).
- **Metzinger advisory relaxed (rule change, MG-approved):** one neutral SMT credit in venue manuscripts; outreach exclusion and no-recruit policy unchanged; Wolfram unchanged (`neuroscience-communication.md`; CLAUDE.md trigger widened to citing/naming figures).
- **No Outside cover (MG):** lattice tunnel, seed 7 (FLUX 3 Klein, typeset by `scripts/compose_cover.py`; *"definitely your rec"*). Front: `drafts/no-outside-cover/final/front-cover-300dpi.png`.
- **Venue route (AIW-292):** presubmission enquiry to Keisuke Suzuki (JAIC, met at MoC7) offering detector + robot plea + worm paper, JAIC picks. JCS ≠ JAIC.
- **Disk vs running (WD-4, worm paper / master §3.4.5):** MG: *"either there is something in the cosmos that lends basic awareness/consciousness to whatever underlies QM, thereby some light form of panpsychism, or the laid out human on a disk IS conscious. FMT then would predict a split for physics to follow up on, not a decision."* State the split (AIW-285); pick no horn. Rationale: identical structure ⇒ any missing ingredient is extra-structural physics; both horns are behaviourally identical, so it is a dependency on physics, not a test.

## 2026-10-18 (S338) — work order
- **W1 (MG):** No Outside v0.7 → paper 1 draft 4 → JAIC detector (AIW-130) → PLR commentary (AIW-228) → Tier 2 drafts → Skeptic exchange (AIW-294) → AIW-288/285 into the next FMT version. W2: proposed priorities on AIW-275..295 accepted. W3: AIW-174 closed. W4: AIW-223 P0 → P2. W5: MG reviews and sends the four MoC7 drafts himself. W6: JCS slot decided inside AIW-292 (`docs/papers-book/s338-decision-triage.md`).
- **No Outside AI use (MG):** *"Ai use declaration inline for papers not for books, For books kdp does that external of book body."* No declaration in the book body or on the subsite; supersedes monograph D22.
- **Landing pack (MG):** sheep teaser best so far; crucible results stay redacted; the SJÄLV PDF goes online; the six working titles may be listed publicly.
- **Telegram routing (until cfg fixes afd):** act only on @aiware-prefixed messages or ones naming an aIware item; ask bare answers back.
- **Wiki (AIW-296):** supplemented with the v19 state; undeposited paper contents, crucible results and No Outside stay out; theory map goes in wiki-first.
- **Lucid onset (Prediction 4 / map E3), MG:** *"null on the lucid thing refutes the signature"* — already worded so (master §8.5, E3, wiki); cover notes keep that scope.
- **Prediction-map site (AIW-276):** host our map plus Negro et al.'s GNWT/IIT/PRM/RPT maps (CC BY 4.0, attributed; GNWT class colours ours if the preprint has none, marked as ours); quality meta-metrics (empirical reach, fruitfulness, exposure, robustness, scope) with two caveats (FMT map author-drawn; metrics measure articulation, not truth); ConTraSt standing LEAST prominent (MG: "make the contrast thing the least prominent"), FMT shown as not yet tested.

## 2026-10-18 (S337) — papers from "No Outside": order, preprint, corrections timing
- **Order:** paper 1 (core article) first; paper 3 (Ch 14, worm) only if separable (Ch 15 depends on Ch 14). Tiers as in `docs/papers-book/paper-priorities-s337.md`.
- **Preprint:** No Outside on Zenodo after MG's proofread, so paper 1 can cite the DOI.
- **AIW-285 corrections:** fold into the next FMT and SB-HC4A versions with AIW-288.
- **S324 journal pause LIFTED.** All venues re-assessed together, weighing MG's manual submission effort → `AIW-292`. MG on Keisuke Suzuki: *"very nice to us and seems open to radical work like ours"*.
- **eNeuro opinion and the permeability paper are live** → `AIW-290`, `AIW-291`.
- **L1 repair = option A** (MG): L1 limits the act *in progress*; the holding at t is not among the completed items held at t. Complete self-description incl. production is possible (Kleene's recursion theorem, quines); Ryle's distinct-act premise is not used. Applies to the book too.
- **Hygiene:** the Definitions B blocker "2015 book pp. 55–57" is resolved by `fmt-2015-derivation-check.md`; Alen Frey removed from the JAIC byline.
- **Paper 1 scope:** falsity gradient out (short paper later); ≤5 self-citations; the argument must run without FMT being true.

## 2026-10-18 (S336) — "No Outside": the seven holes and D1–D3 ruled
All MG's, one by one (details: `session-context.md` S336 / conversation log).
- **The outside-the-universe view is not a perspective.** It draws no distinctions (every string holds every mind), so triviality, observer-measure debts and "space of structures" counts belong to it and fall with it. A third-person view from WITHIN the experienceable universe is legitimate — MG: *"not an outside the universe view, only an outside a brain-like computation device as seen from within the experiencable universe"*.
- **Hole 1:** observer-measure debt applies only to outside-view theories; inside theories are tested by refutation.
- **Hole 2:** description length demoted to in-world bookkeeping; FMT's architecture decides whether a structure has an inside.
- **Hole 3 / D3:** Ch 15 settles self-application; any perspective that distinguishes anything has a frame and is reached.
- **Hole 4:** "the substrate has no experience" argued from closure + D1 (stored structure is potential; the realized trajectory at closure is the inside); inherits P3's asserted status.
- **Hole 5:** unconditional core = absent current generator + no part can certify its description complete; capacity/irreducibility are world-conditional.
- **Hole 6:** substrate reversibility, determinism and measurement independence are undecidable from inside; SB-HC4A keeps them as declared architectural choices (§6.5 MI fix → AIW-285).
- **Hole 7:** felt logical necessity cited as "consistent with" verified literature; stays a proposal.
- **D1** (S335 stands): rule + initial state = potential; the realized, readable trajectory has an inner world.
- **D2:** order is an observer-selection precondition (consciousness needs an order/disorder contrast; locked-in developmental point as conjecture); testable from inside only as the edge-of-order asymmetry.

## 2026-10-18 (S336, later) — Fable v0.4 verification rulings
- **M1:** the observer-measure debt is justified by "the counted space is one no inhabitant samples, so a count over it refutes nothing until a measure is supplied"; the "every bit string contains every mind" gloss only where free readings are at issue (Ch 14).
- **M5:** consciousness requires order ENCODED in the structure, not order actually received — assembled minds count (D1). The developmental conjecture covers built minds only; Boltzmann/assembled minds stay undecided.
- **M6:** the small-random-patch reading forbids nothing, so it is bookkeeping, not a rival hypothesis.
- M2–M4, M7, M8 + 14 minors applied as Fable worded them (M8: the core forces one cut, capacity the rest).

## 2026-10-18 (S335) — monograph "No Outside"; FMT's level distinction is a didactic cut
- **New project:** a monograph on the limits of mathematics and logic from any embedded perspective (sources `docs/sources/perplexity-2026-10-18/`; drafts `drafts/monograph-limits/`).
- **Ruling (MG, verbatim):** *"the level distinction in FMT between implicit and explicit is at its core a didactic pattern, not an attempt at absolute truth. the level distinction imports the semipermeable boundary (thereby contradicting itself) for the explanatory power it lends that would otherwise be inaccessible, not unlike a physical theory needs to separate time and space, or my cosmology theory needs to separate the boundaries from their projections. humans cannot understand absolute truths due to their limited brains that are embedded in what they try to understand."* Consequence: wording presenting the levels as absolute ontology ("two-level ontology") is a candidate correction.
- **Paper corrections from the monograph are applied only after MG approves each one** (`docs/monograph-paper-correction-candidates.md`).
- **D1 (MG, verbatim):** *"it need not be executed, but the results must be available and readable, the rule and initial state alone are only the potential of an inner world. the printed out bits of the executed rule, even if not executed but randomly found would have one."* Supersedes v0.3 Ch 14's "rule + first state suffices".
- **MG's thread position** (*"instantiation is not needed. FMT is a theory on our plane of existence, not fundamental… the static layout on a disk might be all you need"*) is the monograph's Ch 14 thesis; consequences for FMT §3.4.5 are candidates, not changes.

## 2026-10-16 (S334) — post-MoC7 rulings
- **Paper order:** Definitions A (`AIW-278`) first; the rest left to the agent (MG: *"make the order of the other papers as you like"*): theory map (`AIW-281`), robot plea (`AIW-284`), minimal self (`AIW-280`), Definitions B (`AIW-279`). Drafts venue-neutral in `drafts/papers-moc7/`.
- **Minimal self = basic (non-recursive) ESM, with pattern #33's sentience floor beneath it** — not the ISM ("never directly conscious", §3.2 and 2015 book). Reports need the recursive (*erweitert*) rungs.
- **Category theory stays small and must earn its place:** primary tools = stochastic dynamics + information theory; CT only for D1 (closure defect δ), D2 (self-model vs mere recurrence), D3 (closure as guarded fixed point, cf. Kawakami MoC7 #54). No "category-theoretic formalization in development" until D1 has a result (`docs/papers-moc7/category-theory-explainer.md`).
- **The "ETH LLM tool" talk is Vukovic (#120, University of Zurich), not ETH**; `AIW-277` re-targets to her platform.
- **Table 1b closure falsifier (MG: "a obviously"):** disrupting the self-modelling loop itself leaves no-report markers of experience intact; metacognitive disruption alone does not test closure (the old criterion was HOT's falsifier, the outcome FMT predicts). No-report markers because report may fail with long-term-memory transfer (MG). Applied to master, prediction map (E5), `fmt-claims.json` (F-FAL2), theory map.
- **The floor and the terminology (D2/D2b, MG chose (a)):** the floor is phenomenal — a rudimentary closure, consciousness at its minimum. MG: *"either you have phenomenology or not. no phenomenology -> none of the words get a positive."* Floor = the now plus primordial pain or nothingness; unreportable by definition. Above it, two axes: **richness of content** and **depth of recursion**; **reportability** grows with recursion depth. **Access** in Block's dispositional sense is NOT consciousness (MG): preconscious (Dehaene et al. 2006) until a permeability event brings it into the running simulation; the felt "I just decided to recall this" is the delayed-observer agency illusion ("Two grips, neither free"). Colloquial "aware of X" = X is conscious; the label still avoids "awareness".
- **D2c (MG): split accessible/accessed** (Dehaene et al. 2006): §3.4.6's identity "access and phenomenality are two descriptions of the same process" holds for ACCESSED content only; where the master says recursion converts presence into "access", read REPORTABILITY. *(Superseded S341: accessible content may also be explicit but outside the self-model loop — see 2026-10-19 S341.)*
- **FMT definition vs Paper A's C1–C9** (MG, `docs/reviews/2026-10-17-fmt-definition-vs-C1-C9.md`):
  - *Sufficient:* four models under closure + free compute + embodiment + at least one pain-pleasure axis IS conscious.
  - *Valence* may be engineered — presetting it *"only shortcuts what evolution would do by killing all creatures who get it wrong"*.
  - *Embodiment* is required for the natural emergence of consciousness, not its existence (locked-in from birth: at or slightly below the floor).
  - *Decision procedure:* where connectome, weights and running system are inspectable, trace a signal entering and reaching the self model, report optional; otherwise behavioural analysis only (also the floor's non-report signature).
  - *Self model criterion:* a model of the system itself with a "realistic representation of the organism" factor; a position estimate is not one (a SLAM robot vacuum fails this and free compute).
  - *Capacity vs process:* consciousness = the process (Bewusstheit); the capacity (Bewusstsein) is named separately; fix master §3.1 l.144 and Table 1 l.160.
  - *Bridge:* identity (phenomenality IS closure). *Panpsychism:* FMT requires no micro-experience and cannot exclude it; replace the flat denials (§4.2 l.550, l.630). If it holds, one extra physical ingredient is needed and closure forms a subject from it, so FMT answers the combination problem. In-silico closure-off ablation tests the premise; in-vivo disruption tests the markers.
  - *Definitions B:* adopt Paper A's C1–C9 verbatim and score FMT openly.
- **Definitions A route (MG):** hope for Signorelli as co-author (either order, or all consensus participants; MG accepts second author) — goal is MG's name on THE MAP, attention for FMT and book sales, not sole credit. Sequence: fix master, deposit v19, then mail Camilo (MG's go at each outward step).
- **AI disclosure in every paper of this batch (MG):** "claude assisted with grammar and wording and style, I provided all content, ideas and concepts"; do not overstate the AI contribution either. Statement: "The author used an AI system (Claude, Anthropic) to turn the author's notes and directions into prose, for wording and style, and to verify literature and citations. All content, ideas, concepts and structure are the author's." No attempt to make text undetectable as AI-written (declined S334; JCS requires an AI statement). **[S359: the no-undetectable stance stands (MG); the statement text above is RETIRED — use the S342 wording.]**
- **Deep sleep is probably unconsciousness; non-deep sleep is the reportable state closest to the floor** (settles pending item 10).
- **English label: "minimal consciousness"**; "sentience" only as a cross-reference to animal-ethics literature; never "awareness" for the floor. Supersedes the S221 terminology file's "use sentience for the floor".

## 2026-09-29 (S324) — two crucible rulings that belong to FMT (AIW-232 items 3 and 4)
- **Decompilation is a readout pipeline, never a discriminator** (MG 2026-08-05: *"the decompilation argument was never meant as discriminator"*). The master §3 decompiler passage (reconstruction *in principle*, two limits) must never be recast as a conscious/non-conscious test.
- **The energy axis is retired for any cost claim** (MG 2026-08-17: *"we move to redeployment axis"*). Cost claims ride the redeployment axis and matched-function wiring/storage bills, never a joules-per-timestep number.

## 2026-09-28 (S324) — AIW-269 rulings: what goes into FMT v16 / formalization v4
- **v16 contents (MG, item by item, `drafts/aiw269-must-answer-drafts.md`):** A1+A4, A3, A6, A8 as drafted; A8 corrected after verification (Bajwa et al. woke participants from *deep* sedation and PCIst/LZc did **not** separate experience from none, so the closing prediction is dropped and the null reported plainly); A5 §8.7 "Unique?" → "In part"; A2 Basri hedged paragraph; A7 Sipling short text; G1 J-space paragraph in §7 (GWT entry); A9 Corcoran (three-theory review) + Bandara; F1 the theorem is Sugiura et al.'s, Roig et al. extend it to discrete time, Du & Wang as counterweight. Every must-cite that verifies goes in; unverifiable ones are dropped and listed.
- **G1 falsifier (MG):** *"how would you know a genomic sequence doesnt contain the seed of consciousness in some form? … if you had training data that is all sub class 4 or training data that only contains mathematical or physical equations, it will be much more abstract j-space if any."* ⇒ a **gradient over the generating process**: sub-Class-4 → no workspace; equations only → a far more abstract one at most; text from model-running systems → the observed one. Genomes excluded (they encode the builder of a model-running system).
- **Tiehen & Tubert ("Superintelligent Zombies", JCS 2026):** FMT concedes the bounded case (closure pays only inside a fit window; [S359: say "cost window", S342 D5] ample compute replaces it) and names the **problem class**, not the budget, as what sets the window: modelling many model-bearing agents and itself in an open-ended world keeps redeployment cheaper than per-perspective relearning at any budget.
- **Sugiura et al. 2025 and L2:** after MG's *"do literature research on the 'brain's random generator' first"* (`docs/aiw269-brain-random-generator.md`, `docs/aiw269-sugiura-l2.md`): MG's study is most likely Murakami et al. 2017; noise caps input resolution, so infinite resolution is out of reach in any regime; the finite-resolution optimum is driven-stable / undriven-chaotic, so L2's edge-of-stability conjecture survives. L2 (v) gets the source-only Theorem-3 sentence + the noise-caps-resolution sentence (MG); the biology sentence is held for a later §3.7 edit.
- **Batch:** AIW-243(1)/(2), 266, 219, 251 applied; held 243(3), 201, 265, 75, 77.
- **tmp/ untracked (TMP_LINT, MG S324)** — except the 48 files other files read, above all `tmp/zenodo-changelog.md` (read by `scripts/zenodo-upload.sh`).

## 2026-09-28 (S323) — pre-deposit gate, and the literature window
- **Deposits wait for a literature + open-todo gate (`AIW-269`).** MG: *"in a few days maybe, first we need to make sure we are aligned with most recvent literature and open todos"*.
- **The literature window runs from the first FMT deposit (2026-02-17).** MG: *"when i told you to include work from a certain date, you wrongly expected me to know the limit of your previous sweep, if any."* ⇒ When offering a date window, state what earlier coverage actually exists.
- Out-of-window items included by MG: Dijkstra, Fleming & Shea (NC niag048); Sipling, Zhang & Di Ventra (*Trends Open* 2026); Gurnee et al. AIW-137 poster read-through deferred.

## S319 (2026-09-12) — a string blacklist is not a drift check, and four public records proved it
**Zenodo abstracts are generated** from each paper's own `## Abstract` (`scripts/zenodo_abstract.py`), never hand-maintained or inherited; `zenodo-upload.sh` flags an inherited one. Why (`AIW-257`): a blacklist found one bad record, comparing deposits against their source papers found four — *"fix the class, not the one record MG happened to look at."* **Applying an existing ruling is not making one** (RIM's record retitled to the S313 title without asking).

## 2026-09-23 (S320) — free will part (ii), OSF, Platon, RIM
- **Free will (`AIW-263`):** both halves of MG's 2026-09-18 definition proved occupied in the literature; **MG dropped *"abstract success"*; *Zufriedenheit* survives.** FMT keeps the **explanatory inversion**: the self-model's *attribution decision* is the control variable, so a false attribution carries the same plasticity consequence as a true one (falsifier: encoding under illusory agency with contingency at zero; to crucible). Accepted consequence: **the architecture predicts motivated cognition.**
- **RIM deferred** (*"RIM deferred until we are ready for moc7"*); Fig. 11 uncited until Wittmann confirms the polarity (S353 now cites it one sentence).
- **Platon belongs to crucible** (*"platon goes to cru for now, he will run experiments for us no questions asked, and he has at least two robots on top of that and actually works in robotics"*); LinkedIn closed as a channel.
- **OSF:** rectification granted; asks (2) and (3) dropped and the Art. 12(3) window left to expire, so as not to spend the OSF person's goodwill.

## S319 (2026-09-12) — "wider first" resolved against flags, not taste; and three addresses left blank on purpose
- **Outreach (`AIW-10`, MG "wider first"):** the first wave = everyone without a blocking do-not-approach flag; widening means relaxing a named flag, not re-litigating the list. Decisive flags: the MoC7 timing rule (no cold email four weeks before a face-to-face) and whose court the ball is in.
- **A guessed academic address is worse than an empty `To:`.**

## S316 (2026-08-27) — "more meaning than meaning" enters as a CUT, not as one claim
**`AIW-253` (MG holds the veto):** the **forward** direction (a corpus made by model-bearing systems contains recoverable explicit-model structure) is **derived** from existing commitments (2015 S.86; patterns #8/#14); the **reverse** (deposited meanings write back into language) is **asserted** and conceded in our own voice. Didactic pattern **#40** (state the difference from Harris/Firth; referent-vs-referent examples). Gurnee et al. 2026 shows the forward half and cannot do the reverse. Placement: §7 comparison entries.

## S315/S316 (2026-08-27) — the companion is retitled on the COST axis; cosmology rests; first deposits of both roadmaps (merged)
**MG (S316): *"iii, 2. yes, 3. rest"*.**
1. **Companion retitled on the cost axis** (S315 decision, S316 title): *"What Closure Costs and What It Buys: In-Silico Cost and Capability Results for the Four-Model Architecture"*, shipped with the `AIW-218` revision. Reconciles S284's defer with MG's *"'Closure and Criticality' that will have to change in the title probably, and hopefully we can make a stronger statement even."* The retitle is a correctness fix (No-Free-Lunch rules out closure as an "enabling condition"). **⛔ Standing constraint: the title may not claim more than cost** until M1s3 (sufficiency) adjudicates; what may carry a title today is the architectural-cost line (A#7/A#8/A#9: 14.0%/12.0% vs 74.0%/71.5%, 5.3×/6.0×).
2. **Cosmology rests; no v7 scoped** (`AIW-165` as written would insert a withdrawn claim; `AIW-166` is a design).
3. **First-deposit BOTH undeposited roadmaps** (MG "ii"; RIM formalization `10.5281/zenodo.22133501` first, SB-HC4A formalization `10.5281/zenodo.22133504`). **Rule (S303, second instance): before acting on a handover's premise, verify the premise.** `scripts/zenodo_first_deposit.py` refuses anything that already owns a concept DOI.

## S315 (2026-08-27) — a backlog entry that says it is done must not be left saying it is open
**An open backlog entry may record a finished sub-step only if it also states what is still open.** Why: `AIW-159`/`AIW-179` were finished work still marked open, costing a session. Enforced by `scripts/check_backlog_consistency.py` (deliberately narrow scope).

## S315 (2026-08-27) — a checker whose default target is a build artifact reports staleness as drift
**`check_md_pdf_drift.py` defaults to the canonical artifact, and a target older than its source announces itself** (`target_is_stale()`, exit 1) (`AIW-180`, `AIW-239`). Why: `tmp/` defaults compared against stale builds and reported staleness as drift.

## S314 (2026-08-27) — RIM Platinum v5 shipped, and the changelog was stale a second time
- **A changelog written before the last review pass is stale by definition.**
- **RIM theory: motivation is not a *capacity*, not "not in the loop"** — M is a node (the Matthew effect needs K and P to update it), not a magnitude. A claim needing ten edits to be consistent is usually the wrong claim.
- **A dry run that predicts a known defect class is a decision input.**
- **No in-place canonical writes anywhere in the build layer (`AIW-245`)**; gates read the `.log`, never the exit code (`AIW-247`).
- **Measure new prose register against the file's prior rate**, including the session's own prose.
- **MG rulings:** **Abstract stays at 430 words** (cutting to ~200 would drop the disconfirmation criteria); public mirror pushed after the deposit; `:407` AI-use declaration unchanged.

## S312 (2026-08-26) — FMT v15 shipped, and the gate the chain does not have
- **Diff the changelog against the git log before every deposit.**
- **File a real backlog item before the deposit even if it grows the ack list**; rewording to dodge the gate is gaming it.
- **Every fold-in is an all-or-nothing asserted pass.**
- **A diff baseline is verified against the published PDF**; `build_changes_highlighted_pdf.py` replaces `build_review_pdf.py`.
- **Check the repo before writing to a person** (MG: *"check correspondence etc first"*); the Wittmann attribution (M→K→Performance, ~50% variance) is Wittmann's Singapore 2002 ICAP paper (`docs/wittmann-materials-summary.md`).
- **Cite the unpublished ICAP paper** — MG: *"in this special case yes, unfortunately it is our strongest formal academic signal and even more unfortunately without that RIM has zero chance."*
- **Theory: motivation is an allocation policy over the loop, not a component of it** (refined S314); Kanfer & Ackerman (1989), Shenhav and Kurzban must be named in §3.4.

## S310 (2026-08-25, afternoon) — the second review, and why a half-reviewed paper stays unedited
- **Adopting a rule is not applying it:** a fold-in begins with the pattern sweep.
- **Nothing is folded in until a review is complete.**
- **Re-derive publish-gate acks each time; never paste them.** A failed subagent's output is read, not discarded.
- **Report tracking conflicts; do not reconcile them.**
- **Fable is no longer reliably free** — a multi-agent Fable fan-out is a resource decision.

## S309/S310 (2026-08-25) — a mandatory review that the paper failed, and four MG rulings
**A Fable review precedes every publish** (MG standing instruction). **Sweep every finding by pattern across the whole file, never by line number.**
1. **Criticality is an EFFECT** (*"criticality is a effect, fix."*): the requirement is open-ended Class 4 computation; near-criticality is what it leaves in neural tissue.
2. **"Return" is acceptable where not contrary to established subject terms** (the graph-theoretic uses stay).
3. **The unfolding argument is answered on efficiency grounds:** its force is conceded as epistemic; under a resource bound unfolded and looped systems diverge in behaviour.
4. **"We DO address all"** — the Introduction's claim to address all eight requirements stands.
**MG's defer rule:** *"Defer only things that makes our work more efficient if deferred."* An approved clause is approved for its content, not its fit; verify against extracted PDF text.

## S307 (2026-08-24) — the gates check existence, nobody had checked characterization
- **MG's publishing rule:** *"what are you talking about? as always we fix the defects, bundle them with new findings and evidence whenever available, then upload a fixed version."* Repair sources immediately; the version bump is a later bundled step; leave published canonical PDFs alone (exception: RIM's drift gate).
- **Existence is gated; characterization is a human review step** (hence a Fable review before every publish).
- **A fallback that cannot report that it fired is a forgery** (`AIW-234`).
- **Verify against the built artifact, never a mirror.**
- **Disconnection control (MG):** *"disconnection doesn't remove closure, it splits one closed system into two"* — disconnection holds the model constant, so it is the right control; it is not interchangeable with self-model ablation.
- **`AIW-194` recall tag:** write it as requirement-plus-prediction, never a mechanism claim (source-monitoring theory rejected a discrete tag).

## S306 (2026-08-23) — a defect class that only shows across two files, and a measurement tool built with its overclaim disabled in code
- **Two files can each be consistent and jointly wrong** — compare md reference lists against `.bib` (`AIW-204`).
- **"Not required" is not "should not":** AI-use disclosure goes in even where not solicited.
- **An honesty constraint that matters is enforced in code** (the detector may not emit a percent-AI figure, probability framing or bare verdict).
- **Where a paper and its released code disagree, implement the code.**
- **A cross-session bug report is a hypothesis until reproduced locally.** Interacting decisions go to the author as one package (`AIW-220`).

## S303 (2026-08-12) — citation integrity becomes a P0 concern, and a published paper is found to have been published
- **Citation integrity is P0.** MG: *"wrong references can damage reputation."*
- **Before acting on a handover's premise, verify the premise.**
- **Widen a quality gate even though the number gets worse**; overriding a written ratchet is argued in public.
- **Cite what the source proves, not what it nearly proves.** The shipped artifact is the `.tex`+`.bib` build.
- **Publish after the corrections, not between them.** Deployment scripts reading from `tmp/` must assert the version.
- **Separate effort objections from correctness objections** — MG: *"my time is the bottleneck, not yours"*.
- **Eyeballed geometry fails invisibly** — computed generator plus render-and-look.

## S302 (2026-08-12) — the disclosure decision splits in two, and the patent lane is re-scoped to what MG can afford
- **Publishing the THEORY and the IMPLEMENTATION are separate decisions:** freeze lifted for PAPERS; the crucible implementation stays CLOSED (trade secrecy is free and preserves fundraising). OSF preregistration and a Show-HN code release remain open decisions.
- **No patent spend; ▸ THE PATENT LANE IS CLOSED** — no exclusionary value (blind design-around found escapes for every family). Reopen only if E4 shows a large cost/trainability gap from the non-foldable return **and** a refile closes the seven gaps (`docs/patent/07-design-around-test.md`). MG's test rule: *"one fable pass for now. if a fable pass finds a way around its done. if not we consider."*
- **The fold theorem is MG's as a recognition, never patentable, and cannot be unpublished;** scrubbing rejected (same as `AIW-206`).
- **Alen Frey is out of the JAIC paper**; no follow-up drafted; record kept neutral.

## S301 (2026-08-11) — the patent lane opens, and the backlog turns out to be a leak channel
- **Patent scope** (MG) — *lane closed at S302.*
- **`backlog.md` is excluded from the public mirror.** Any claim "X is not public yet" is checked against `git log origin/main`. History rewrite open, with `CFG-479` if at all.
- **Cross-project theory disagreements go to the result's owner.** Do not scrub the employer-exposure record.

## S300 (2026-08-10/11) — the verification session, and what it cost the theory
- **Two claims died under primary sources:** the "re-instantiate the phenomenal value" differentiator vs model-based RL (Dayan & Berridge 2014) and the Domhoff & Fox "continuum".
- **MG: position against the field's UNSETTLEDNESS, not a monolith**; the unclaimed ground is the **reordering / priority-inversion signature**.
- **Ictal route: UNSETTLED** (route-independent invariant suffices).
- **Pattern #37 paper form (MG):** *"not as uncaused but as **originating** in the self."*
- **Checks fail silently by passing**; verify against the built artifact before working it.

## S298 addendum (2026-08-09) + S299 — the connectome study was risk-aversion dressed as strategy (merged)
- **The connectome generality study is killed — dropped, not deferred** (S298; reaffirmed S299 `AIW-197`). MG: *"which is a stupid experiment knowing the outcome anyways."* A confirmation that cannot fail is not a measurement.
- **The reason for a human-like (human/macaque) connectome is FUNCTIONAL:** MG: *"human shape / macaque is more interesting because we have dedicated language centers we can connect to or replace by an llm"*. Fly is not a step toward it.
- **The siibra feasibility check is complete and must never be re-run** (S299; `docs/pending-s298-followups.md` §0). F-TRACT covers cortex, hippocampus and amygdala only (routed to crucible).
- **Relaying is not understanding** — check an agent's framing before passing it to MG.

## S298 (2026-08-09) — `AIW-191` fires: the prioritization output is a queue discipline, not a cut list
- **Nothing is parked. FMT-master work has right of way; everything else fills GPU-wait gaps** (MG: *"don't park until then, use as gap filler during gpu wait"*).
- **Old crucible inbox items are searched, not triaged**; what MG says in conversation gets missed — a routing defect.
- **A priority without a bundling item loses.** An inbox item correcting a published claim is not background work (MG 2026-07-08: *"'I' is TAUGHT, not spontaneous"*).
- **Book/marketing items go to simbook/infrastructure, not re-imported.**

## S291 (2026-08-07) — the RIM Fable pass lands; the Cosmic Compiler is not cited; two fabricated citations found
- **RIM's consciousness dependency is a boundary condition** — FMT stays a named, separable candidate; a reviewer who declines FMT must not take RIM's independent claims with it.
- **RIM's differentiators are scope and the measurement programme with falsifiers, not the K×P×M formalization.**
- **`AIW-133`: *Cosmic Compiler* not cited** (S290 entry). The citation gate checks resolution, not existence or content (→ `AIW-170`).

## S291 late (2026-08-07) — the passes MG demanded found what he predicted; both papers blocked
- **A diff's size measures its scope, never the artifact's health** (MG: *"i find it hard to believe that this paper on which we did the least work is so good that it needs the least changes."*).
- **An agent's finding is a hypothesis until independently checked.**
- **`AIW-174` P0 with `AIW-172` first.** The prose guard lives in `.claude/knowledge/prose-register.md`, not memory.

## S288 (2026-08-06) — the MoC7 work order, five chart decisions, and what stays open
- **Chart web deployment is infrastructure's job**; aIware owns content, method and citation audit. Bildstein unpinned.
- **Chart decisions:** Wired/Running as a **translation layer** (papers/books keep implicit/explicit); residue named **Presence Term**; *Bewusstsein*/*Bewusstheit* maps to the ladder (capacity vs running now). `docs/smoc-middle-layer-draft.md` §7.
- **No-Free-Lunch is not over-applied (MG):** *"no free lunch is about ML not about human intelligence… human intelligence includes social and emotional intelligence and other stuff that is consciousness altogether (not the closure) IS a capability that lifts intelligence from insect to mammal level."* **Efficiency-only in the in-silico/formal lane; budget-relative capability in the biological lane.**
- **R4 is the consciousness floor; sentience is a `disputed` band R2–R4.**
- **Depth axis: the chart declares it, FMT fills it** (MG: *"depth WILL become measurable"*); *einfach/doppelt/dreifach erweitert* as FMT-only sub-increments; Identification = R7; language-coupled = R8.
- **Truth (MG): *absolute falsehood doesn't require absolute truth to exist.*** The asymmetry is a GRADIENT (*"When the deciding population changes, both falsehoods and truths can change, but falsehoods are more resistant."*); prediction: resistance scales with the cost of the original conversion. *Wahrheitsgehalt* → **Konsensgrad / degree of corroboration** (`AIW-153`); truth blog post under `AIW-122`, never mentioning the monograph.
- **Sixth mark `not applicable` + D9:** every coordinate system is checked for N/A before an axis ships.
- **Design matters** (MG: *"the design is among the very few things that can bring simplicity into such a topic."*); accent `#2a78d6`.
- **`AIW-141`:** neither crucible finding is a standalone paper.
- MoC7-only items (poster last, A2/A1 discussion vote) executed.

## S287 (2026-08-06) — FMT v14 shipped early; the paper stops talking about itself
- **The new component is "the channel", not "the bottleneck":** rank sets how much the simulation holds; recursion depth sets whether it can take its own contents as object. The LLM case is scoped to channel width in the master.
- **Crucible's spiking-plausibility argument declined** ("true and near-vacuous") — verify cross-project claims (`AIW-143`).
- **The paper's self-referential register is gated in `scripts/test_content_integrity.py`** (`AIW-128`).
- **ID collision rule:** renumber the closed side.

## S285f (2026-08-05) — The 2015 definitions are canonical; knowledge does not require consciousness
- **The 2015 definitions are canonical** — *"Wissen ist Information, die einem Bezugssystem zugeordnet ist"*. MG ruled against his own spoken definition: it *"mixed up reported knowledge knowledge and truth there. the 2015 book stuff should be more correct and consistent."*
- **Knowledge is not definitionally post-conscious** (S285d.1 archived); it needs only a reference system; machines have it. **Consciousness enters where the reference system IS a self-model closing on itself.**
- **"The boundary is a model":** DIKW lacks principled boundaries because the field has no theory of models.
- **Argument for the paper:** 2015 p.22 makes knowledge regress, so implicit/wired models are logically required as its base case (`.claude/knowledge/fmt-2015-definitions.md`).

## S285e (2026-08-05) — Notation doctrine: the periodic table's symbols were a print-and-rote artifact
- **No arbitrary symbol layer** (MG: *"dont copy the periodic table or the physics stuff… now we need words or something. and also pictograms, seriously."*). Motivated marks only (self-describing words, operation-diagramming pictograms).
- **Names:** implicit/explicit → **wired/running** on the chart face; `Regulator → Governor`, `Consolidator → Scribe`.
- **One artifact, several depths** (glance / working / audit); ladder drawn as a matrix (`figures/smoc-marks.svg`).

## S285d (2026-08-05) — The project's ultimate goal, named: supply the field its missing middle layer
- **Top-line goal (MG): supply consciousness science its missing medium-complexity middle layer** (periodic-table equivalent), then reverse-engineer a standard model and consensus, then forward-engineer (`docs/smoc-middle-layer-draft.md`, `AIW-146`).
- **Positioning:** the chart is not FMT (FMT is one filling); FMT-specific cells marked deliberately. Agreement status gives the field a progress metric.
- **Design rules:** the Bohr-atom licence (organised, falsifiable, revisable, not right); the pre-2005 test.
- **Closure ⊂ bottleneck:** the waist buys efficiency, the return buys self-consistency; closure claims are efficiency claims; a regulated variable cannot be an IV; a recurrent net cannot be made return-free.

## S285b (2026-08-04) — 222 DPI ruled sufficient; Bach replies and raises J-space
- **The quality bar belongs to whoever decided what the object is for** (222 DPI for the SJÄLV handout).
- **J-space is evidence FOR FMT's architecture:** ablating it leaves fluency and recall intact while multi-step reasoning collapses; no recurrent loops = broadcast without closure.
- **Outgoing correspondence must not claim unrolling costs capability** — the defensible claim is efficiency (pattern #18).

## S284 (2026-08-04) — A month of inbox items was invisible; the paper's title outlived its claim
- **A delivery channel that fails silently is worse than one that fails loudly.** Verify before assuming damage.
- **Companion title: DEFER** (*"defer until more results, nobody is reading it yet"*) — *executed via the S315/S316 retitle.*
- **Peer catalogs are split by function** (FMT teaching devices sync to aIware; measurement discipline to the companion's methods).
- **When a project is extracted, sweep the parent's pending files for anything whose code moved.**

## S283 (2026-08-03) — SJÄLV: the MoC7 handout gets a content brief, and the graphics go out of house
- **Red lines for any FMT illustration:** the four kinds are graded regions on one substrate, never four modules; criticality is the power supply, not a component; the finished product does not wake up; no unsourced developmental content.
- **A popular artifact inherits the paper's claim limits in full;** no "Turing". Briefs for external models are self-contained.

## S282 (2026-08-03) — MoC7 GO; FMT's five principles collapse to three
- **FMT has THREE principles (`AIW-138`, MG):** **P1** open-ended computation allows free modelling (criticality its signature in neural tissue); **P2** recurrent non-linear dynamics of sufficient complexity host a second computational level; **P3** phenomenology is a real physical effect on that level, arising where the modelling closes on itself. Redirection, variable permeability and forking are consequences. Closure is NOT identical to the standing-wave computing; the detector keeps three separate checks.
- **"Turing complete" is useless to claim.** §3.7 title: "Criticality: Signature of the Computational Regime".
- **Meta-science register is banned in FMT prose** (MG: *"isn't that explaining science to scientists again and worse advertising good scientific practice instead of contents"*).

## S281 (2026-08-02) — MoC7 Copenhagen poster accepted; AIW-130 decisions 3–5
- **Honest-convergence discipline applies to competitors too** (MG: *"there was no need whatsoever to mention that we 'complete' or anything their work."*): state FMT positively, cite theirs neutrally.
- **AIW-130 #4:** name published architectures and report where each fails; safety from framing, not anonymity. **#5:** JAIC reviewers Kleiner, Wiese, Mediano.

## S277 (2026-07-30) — AIW-130 two-slice papers: reframe, co-authors, pipeline hardening
- **The criticality claim is strictly ONE-DIRECTIONAL** — *biological-scope necessity retired S329; the ban on reverse and biconditional forms stays.*
- **JAIC title:** "…a Self-Model That Takes Itself for Its Bearer".
- **Co-authors are provisional (earned, not gift)** — *Frey out S302; Sousouri dropped S356 D11.*
- **Pipeline:** `register-ai-tell` + `theory-fidelity` reviewer lenses and a re-review NO-GO gate (`scripts/fmt-pipeline/`).

## Archive Index

Older and retired entries were moved verbatim to **`docs/decisions-archive.md`** to keep this file grep-able.

**Batch 1** (2026-03-16 through Session 253 / 2026-07-06):

- **S248 (2026-07-07)** — Book ed.2 DE trimmed for DACH (edition-scoped tone divergence)
- **S246 (2026-07-06/07)** — Book ed.2 experiential restructure (reader-first opening, printed blind-spot demo, Fable-for-creative-prose)
- **S244 (2026-07-06)** — FMT v12 adversarial review, targeted revision, theory-complex assessment
- **S239 (2026-07-05)** — CA identification is scale-agnostic didactic device, not literal biological claim
- **S240 (2026-07-05)** — Inbox triage: AGI-26 declined, Birch deferred, Seth BBS superseded
- **S241 (2026-07-05)** — Fable-5 content-gate is INTERMITTENT (S239 refusals didn't reproduce)
- **S239 (2026-07-05)** — Fable-5 unusable for consciousness/AI-architecture content; Opus is the ceiling
- **S238 (2026-07-04)** — Book voice-pass (AIW-93): parallel-inventory → verified-JSON-apply methodology
- **S232 (2026-06-19)** — Inward causal role is necessity not freedom; seizure dynamics; two-dials not yet formalized
- **S228 (2026-06-17)** — Olfaction-bypasses-thalamus folds into AIW-87
- **S227 (2026-06-17)** — Will/motivation are poles on a gradient, not separate kinds
- **S224 (2026-06-12)** — AIW-47 eNeuro paper finalized + double-blind code handling
- **S223 (2026-06-12)** — AIW-47 authorship & venue (optimize for FMT recognition); meta-d′ standard method
- **S217 (2026-06-10)** — Fable 5 review: FMT stands; fixes are executional
- **S189 (2026-04-16)** — Zenodo v5 blocked on deep revision
- **S208 (2026-05-29)** — FMT v7 architectural clarifications; NBSR desk rejection
- **S209 (2026-05-29)** — Gridworld vs cellular automaton instrument choice
- **S197 (2026-05-11)** — Full paper stays ~29k for Zenodo; Frankish distinction; self-referential closure commitment
- **2026-03-16** — Strategic direction (two paths to breakthrough); co-author strategy
- **2026-04-15** — German book publication on KDP
- **S210 (2026-06-03)** — James-Stein / SB-HC4A entanglement; thalamus evidence for FMT
- **S215 (2026-06-10)** — MEMORY.md is a mirror not a source; conversation-log drift guard
- **S216 (2026-06-10)** — Seth commentary → standalone Zenodo preprint; eNeuro short-report design (AIW-47 spine)
- **S219 (2026-06-10)** — SB-HC4A cosmology argument repairs (locked spec)
- **S225 (2026-06-17)** — RIM unparked + COGITO convergence; book revision (next edition)
- **S229 (2026-06-18)** — AIW-47 eNeuro abandoned + Bonn deprioritized; connectome (BANC) as gatekeeper-free avenue
- **S230 (2026-06-18)** — AIW-90 Track 2 done + AIW-91 (minimal critical substrate) opened
- **S231 (2026-06-19)** — AIW-90 criticality corrected to synchronous bursting; TWO kinds of criticality (extent vs complexity); Fork A/B resolutions
- **S233 (2026-06-22)** — AIW-92 didactic-pattern integration (books-first)
- **S234 (2026-06-25)** — AIW-96 open-data test of ESM/EWM double dissociation
- **S236 (2026-06-29)** — AIW-92 integration + paper sharpening, Zenodo v11
- **S237 (2026-07-01)** — AIW-99 fix + Bach prior-art (RIM) + Friston-500 → SMoC opportunity
- **S242 (2026-07-06)** — AIW-91 "simplest AC" architecture + embodiment

**Batch 2 — monthly review S326 (2026-09-29)**, under "Archived 2026-09-29 (monthly review S326)":

- **S315 (2026-08-27)** — cosmology v6 ships; formalization not redeposited (superseded by S316 first deposits)
- **S285d.1 (2026-08-05)** — Data/information/knowledge carve (superseded by S285f: 2015 definitions canonical)
- **S285c (2026-08-05)** — SJÄLV frozen (executed; booklets printed)
- **S285 (2026-08-04)** — SJÄLV artwork vectorizer route (superseded by S285b's 222 DPI ruling; executed)
- **S280 (2026-08-02)** — simbook made visible in the `af` launcher (executed one-off)
- **S262 (2026-07-14)** — Fable cost-hold cleared (executed; superseded by later Fable-credit status)

**Batch 3 — monthly review S358 (2026-10-24)**, under "Archived 2026-10-24 (monthly review S358)":

- **S325 (2026-09-29)** — FMT v16 + formalization v4 deposit timing (executed; v16 deposited 2026-10-02, S328)
- **S325 (2026-09-29)** — peer commentaries exempt from the rejected-journals pause (superseded by S337: pause lifted)
- **S325 (2026-09-29)** — public push done; PhiMiSci deferred (push executed; deferral superseded by S345 venue ruling D4)
- **S325 (2026-09-29)** — MoC7 organiser mail status (executed logistics; MoC7 over)
- **S324 (2026-09-29)** — no work toward journals that have rejected us (superseded by S337: pause lifted)
- **S327 (2026-09-30)** — MoC7 poster frozen and printed; robot card off-poster (executed print run; incl. AIW-258(b) poster wording and the online-order rule filed to cfg)
- **S351 (2026-10-21)** — Silent Suffering routing (executed: the rule fired, see S352)

Merged in S358 (both dates kept in the surviving entry): BUBBLE poster figure (S321 + S327); companion cost-axis retitle (S315 + S316); connectome study killed (S298 addendum + S299 `AIW-197`); concept DOI only (S270 + S295 → S343); independent coder / Blums (S345 + S346 + S350); Def A hold (S342 → S345).

---

## S275 cont. (2026-07-28) — FMT wiki refresh (AIW-27): scope & framing
- **Wiki content (`wiki/*.md`) is aIware's; deployment is infrastructure's.** Targeted correction + currency, not a rewrite (MG).
- **Public positioning (MG): FMT as the "leading candidate for a standard model of consciousness"** — an invitation, not a verdict.
- **Canonical criticality reframe:** the requirement is **free compute**; criticality is the measured signature (`docs/pending-wiki-refresh.md`).

## S275 (2026-07-28) — FMT two-slice run reframed + de-risked; three-paper plan; NoC single-blind correction; Wolfram/Metzinger advisory
- **NoC is SINGLE-blind** (OUP guidelines, `docs/noc-si-cfp-2026.md`).
- **Three-paper plan (MG):** NoC (brain), JAIC (machine), JCS (philosophy, `AIW-46`) — distinct claim and evidence each. *(Venues re-assessed S337/S345.)*
- **NoC thesis (MG):** "more than computation" = computation on top of computation (the self-model modelling the modelling); anchor = no criticality → no consciousness *(necessity retired S329)*; two-dials demoted to a side-show.
- **JAIC check 3 = "open-ended computation"** (substrate-neutral); cross-paper guardrail on what is "necessary".
- **Wolfram + Metzinger advisory (MG):** CREDIT them in the FMT base paper and books (lineage — "simple as that, dear academia"); refined S276 (audience-scoped), relaxed S339.
- **Blog:** one post per slice point, routed to social.

## S271 (2026-07-26) — FMT v13 PUBLISHED; free-compute-vs-criticality refinement (→v14); Gemini-misreading registry
- **Theory refinement (MG):** *"criticality is what free compute looks like in SOME systems, maybe not all."* The requirement is FREE COMPUTE; criticality its non-universal signature (`AIW-154`).
- **Gemini-misreading registry** (`.claude/knowledge/fmt-misconception-registry.md`). **Rule:** when an interlocutor "demands the math", first check the demand is not encoding a misread.
- v13 published (concept `10.5281/zenodo.18669891`), gated on two Fable passes. TWCF funding lead (`docs/fmt-funding-leads.md`, `AIW-134`).

## S279 (2026-07-31) — pop-sci book extracted to private `~/simbook`; forward leak closed
- **The book lives in private `JeltzProstetnic/simbook`** (CFG-478). Forward exposure only; history purge = `CFG-479`. **Report framing: "no new exposure; historical cleanup pending," never "leak gone."**
- **Asset topology (MG):** `figures/` stay public in aIware (simbook gets copies); shared private knowledge stays in aIware — **simbook references, never forks** (only `kdp-specs.md` moved). New book items = `SIM-`.

## S270 (2026-07-26) — Companion 2026d restructured to results-only; §9.2 taxonomy rejected
- **The companion is a report of results**; forward-looking sections removed (seed text: git `c5820130`).
- **§9.2 modelling-capability taxonomy (self → other → free-play → tool) — REJECTED, do not reintroduce** (MG): not his; ordering wrong; a linear metric of modelling capability is unsound.
- **Plain scientific prose.** Companion concept `10.5281/zenodo.21610993`, `isSupplementTo` FMT concept `10.5281/zenodo.18669891`; internal experiment codes stay out of abstracts. (Concept-DOI rule: see S343.)

## S269b (2026-07-25) — Companion 2026d prose+citations complete; Deck 2 reaffirmed as non-build env
- **aIware paper/book PDFs build ONLY on WSL (canonical) or Fedora-home**, never on the Steam Decks (font drift → page-count drift → spine breakage).
- **When a machine file says "not for this purpose", surface why before offering install options.**

## S267 (2026-07-24) — Crucible in-silico predictions: placement (Fable) + v13 §8.9/§3.7 landed + undersell root-cause
- **Crucible's program sits in the master as a self-contained, droppable section** plus a separate companion paper — MG's **master/subset** model.
- **Draft crucible content from `docs/crucible-evidence-ledger-digest.md`, never the null-forward CRU-36 brief**; verify every banked positive against runnable code (S269).

## S266 (2026-07-24) — AIW-110 CRU-36 prediction decisions ratified (capability-first)
**Capability-first is canon (MG):** P2 IV = **Class-4 capability** (free compute); P2 DV = task-outcome categorical, only with closure ON. Why: CRU-36 nulled on a homogeneous reservoir with no differentiated self/world models. ⚠ "Two instruments (σ≈1, λ≈0) certify one band" retracted by S326 `AIW-271`; "enabling conditions" retracted by S315/S316.

## S266 (2026-07-23) — Book translations nl/el/ko: engine, channels, KDP limits
Translation + native-editor review on Fable; Kalk + coherence on Opus. **Dutch → KDP; Greek + Korean → PublishDrive.** **Fable-failure policy for translations: halt-and-ask, no silent Opus fallback (MG).** (`AIW-123`; book work now in `~/simbook`.)

## S258 (2026-07-12/13) — publishing 8 editions
- **Cover fixes live in the build SCRIPT, never the generated `.tex`.** All Kindle covers from one recipe.
- **MG waived the human-native-reviewer publish gate for translations (2026-07-13).** KDP has no Simplified Chinese.

## S260 (2026-07-13) — AIW-109 correction pass
- **Anosognosia deficit = Explicit *Self* Model** (MG).
- **Edition marker = print copyright page only** (MG: "only second ed"); eBooks carry only ©.
- **Review round on corrected manuscripts before any rebuild;** Fable for risky native-language fixes, Opus for mechanical edits.

## Book translations — IT + JA added; Fable exhausted mid-run; ZH translator deferred + local-Qwen-draft rejected (Session 253, 2026-07-08)
- **REJECTED: local-Qwen-draft → Opus-repair for quality-critical translation** (MG: "slop then repair ≈ direct-Opus quality at best + an extra step + a second error surface"). Local inference = non-quality-critical bulk and quota-outage fallback only.
- **Never run two large Workflow fan-outs concurrently** (`publication-build.md`).

## S243 (2026-07-06) — FMT Hard-Problem stance + core identity (paper v12)
- **Core identity (MG):** consciousness *is* the ongoing transfer/integration of information into the explicit model; *Bewusstsein = Interaktion mit dem Modell* (authoritative wording: S276).
- **Hard-Problem stance = conditional dissolution + narrower gap, not over-concession** (§3.4.3 ¶A–C): the residue is ill-posed *if* the inside/outside asymmetry is constitutive; residual doubt = other minds. `◐` kept. **[S359: SUPERSEDED by PHENOMENAL-7 (S342) — the master claims transformation only, never dissolution, not even conditionally (MG).]**
- **IIT `●` / FMT `◐`** — IIT argues from axioms. **ESM/EWM boundary:** sharp per snapshot, fluid across frames. **Qualia privacy:** structure shareable, absolute encoding refractory (`AIW-105`).
- **Book rulings (S247–S254):** DE cultural redaction — early chapters cautious with drug anecdotes, late fine; do NOT "fix" the Occam bite-motif (asymmetry intentional); content fixes port, pure voice does not; coherence fixes go upstream in EN/DE source; factual errors fixed in all editions, style items are ed.3 refinements; Kalk recipe in `docs/aiw108-fable-opus-kalk-analysis.md`.

## S255 (2026-07-11, WSL) — final Fable QA pass on all 8 editions; review-purpose correction; Fable-null sign-inversion owned
- **A final review of published content is a hidden-defect QA sweep, not a theory revision (MG).**
- **The CRU-36 null is FMT-consistent, not a falsification.** Reproduce cross-session theories against source before briefing subagents.

## S256 (2026-07-11/12, WSL) — AIW-109 fixes applied to all 8 editions; §0 cleared; MG model + review directives
- **Model split (MG):** Fable first on difficult/lower-resource languages, Opus on high-resource ones; DE rewrites on Opus.
- **MG aphorism directive:** "three times the same sales pitch is NOT ok, remove at least 2".
- **Flag commit intent explicitly.** §0 citations (Hengen & Shew 2025; Algom & Shriki 2026) verified real.

## S257 (2026-07-12) — AIW-109 final split review + figure localization
- **German-book self-reference: drop, don't rename.** Insect quip kept alongside the empirical hedge.
- **Only the three original FMT diagrams are localized**; homunculi figure stays English except DE.

## S263 (2026-07-14) — ed.2 build & ship (build-level typography)
- **Per-language typography is applied at BUILD time, never baked into `.md`** (`scripts/typography_fixes.py`).
- **"Second edition" marker is print-only.** Covers rebuilt only if a page count or cover defect changes.
- **Run `scripts/check_pdf_margins.py` before every KDP upload.** Covers carry the baked ISBN barcode (MG S264).

## S265 (2026-07-17, WSL) — triage of accumulated cross-project inbox items + policy record
- **The 8-language book is fully published** (21 SKUs). **ZH print PARKED.**
- **⛔ Metzinger — PERMANENT no-recruit policy (MG):** never pitch, recruit or invite Thomas Metzinger to anything FMT-related; inform only post-hoc. Outreach only — he remains a legitimate citation. Canonical: social `contacts.md`.
- **RIM reframing** — *positioning superseded by S290 (`AIW-126`).*
- **BLOG-FIRST dissemination (MG):** "We can't keep updating the book on every new finding — the next book update may be half a year away." (`AIW-122`).
- **AIW-110 #1 (MG):** the P2 IV = the substrate must be able to do FREE COMPUTE.
- **Before claiming "nothing is published on X", check `docs/web-presence-inventory.md`.**

## S269 (2026-07-25, WSL) — closure-maintenance "banked positive #1" DROPPED from FMT §8.9 + companion (data-integrity)
- **The closure-maintenance "positive" is DROPPED; do not reintroduce** (MG: "remove rather than discuss the null") — a null at crucible's defaults (`scripts/verify_closure_maintenance.py`).
- **Verify every banked positive against runnable code before paper use.**
- **Never label a result an "honest null" / "honest scope" in a manuscript (MG)** — report the result, drop the virtue word.

## S274 (2026-07-28, WSL) — FMT salami-slice strategy: two desk-reject-resistant lanes; Lane B = "completing Kanai's ICCR"
- **Stop submitting the full paper (5 desk rejections, 0 reviews); cut standalone slices and keep the full paper as a cited Zenodo preprint (MG).**
- **Lane B (JAIC) completes Kanai's ICCR** (arXiv:2606.15348) — instantiation, never supersession (`drafts/kanai-iccr-vs-fmt-comparison-2026-07-28.md`).

## S276 (2026-07-30, WSL) — AIW-130 papers drafted; MG author-review correction on FMT framing
1. **FMT framing (AUTHORITATIVE, MG verbatim):** *"consciousness requires free computation and arises when a self model confuses itself with the being it occupies… the integration of information from implicit models to explicit system and feeding them to the self model is what makes conscious experience."* Consciousness is **constituted** by the implicit→explicit→self-model integration. *(Criticality-necessity half retired S329.)*
2. **Names-out advisory is audience-scoped:** Wolfram/Metzinger out of consciousness-science/neuro/philosophy venues and outreach; fine in CS/complexity venues *(relaxed S339)*.
**Process:** refiners need a theory-owner check.

## Greek (el) translation build + review-order (S278, 2026-07-31)
- **Reconcile-before-scan:** apply an existing interior review before fresh passes.
- **Greek interior font = P052 (URW Palatino)** with polyglossia. **Greek number format UNRESOLVED — MG's call.**

## S286 (2026-08-05, WSL) — FMT v14 three-principle restructure applied; review-format directive
- **All three principles stated once, in order, at the head of Section 3**, with back-references; abstract variant B (variant A in `drafts/aiw138-abstract-variants.md`).
- **Demotions are a derivability claim** (§6.0).
- **MG standing directive ("always 2"): change-tracked HTML is the DEFAULT review artifact for paper revisions**; PDFs only for layout review (`scripts/review_changes.py`). **[S359: SUPERSEDED (MG) — default review artefact is the changes-highlighted LaTeX PDF (`scripts/build_changes_highlighted_pdf.py`).]**
- **Never compare against a committed PDF without checking it against a fresh build of its source.**
- **PDFs for a commercial printer are checked for unembedded fonts first.**

## 2026-08-06 (S289) — the SMoC argument map: sourcing, and what earns a point
- **A point on the map is a POSITION, not a person;** meta-level work does not plot.
- **A point earns its place by informing;** Kanai's information-generation theory IS placed. Biological naturalism at 0.28 on Searle's own text.

## 2026-08-06 (S289) — durable build scripts live in `scripts/` (AIW-145, MG-signed-off wording)
- **`tmp/` is throwaway; anything that would be missed belongs in tracked, machine-portable `scripts/`.**
- **A red test that is right stays red.** `git log --all -- <gitignored-path>` before declaring a `tmp/` file lost.

## 2026-08-06 (S290) — Schoff's *Cosmic Compiler* is not cited in SB-HC4A (AIW-133)
**Not cited:** its Paradox of the Rule equivocates; Axiom II contradicts SB-HC4A §3.2; Φ_Ω is precluded by the cyclic fixed point; grey literature. Engage Albert (2012) in §3.1 instead (`docs/aiw133-schoff-cru-cosmology-analysis.md`).

## 2026-08-06 (S290) — RIM stays a psychometrics paper; free modelling is the mechanism, not the pillar (AIW-126)
- **The third component keeps the name Motivation in K × P × M; free modelling is the mechanism under it** (MG) — nobody can measure free modelling.
- **Do not introduce "free modelling" as a novel term to psychologists** — claim the integration of existing constructs.
- **Free modelling is an operation, not a location (MG)** — any single measure is a modality projection; a generic-structure lesion shows a damage profile flat across modality loading.

## S292 (2026-08-07) — RIM published as v3; the citation gate exists; two rulings from MG
- **RIM concept `10.5281/zenodo.20125096`.** Always pass `ZENODO_CONCEPT_DOI` and dry-run first (`zenodo-upload.sh` defaults to FMT).
- **C5:** §3.1 = the between-trait NFC/TIE contrast Schweitzer et al. (2025) test; cite Woo et al. (2007).
- **The achievement→motivation asymmetry is expected** (a recursive loop needs both directions non-zero).
- **Falsification thresholds are content.** The citation gate mechanises existence only; human verdicts outrank machine ones; the whole-paper review is mandatory.

## S293 (2026-08-07) — cosmology repaired; Axiom 1 argued; four MG rulings
- **"Bekenstein saturation" → "holographic saturation" (MG). Do not merge the two again.**
- **When a repair forces a choice between an internal claim and established physics, the internal claim goes.**
- **`AIW-174` is a conditional derivation — do not upgrade §6.5 to unconditional.**
- **Axiom 1 is argued, not conceded — MG's argument is the spine of §3.1. Do not re-open it as "arguable".**
- **`Gruber2015` is 2015** (2016 printing: cover and typos only). Silent state that outlives its justification is the shared tooling defect.

## S295 — 2026-08-08 — publishing cosmology, and what the link audit exposed
- **`Gruber1968`:** the Ramakrishnan (Ed.) 1968 chapter, `10.1007/978-1-4899-5424-4_1` (MG's call).
- **`MAX_UNVERIFIED` may never be raised** except per the ratchet's documented rule (S305).
- **Public surfaces are audited against the paper, not just for dead links.** (Concept-DOI rule: see S343.)
- **MG's Culik→vacuum-instability inference is withdrawn.**
- **Purges go to the Recycle Bin, not hard delete (MG); leave every Desktop book artifact untouched.**

## S296 (2026-08-08) — the CRU-81 package placed; two Fable theory reviews
- **Peer-routed text carries the routing project's confidence, not its verification.**
- **MG's division of labour: the FMT lists it, the companion explains it.**
- **Operationalization:** formalization's value is exposure; an implementation guarantees reliability, not construct validity; FMT's formalism is *earlier* than Φ, not better.
- **AIW-174 postulate must be stated JOINTLY** (`drafts/aiw174-entanglement-wedge-postulate.md`).
- **MG ruling: without an architect and an electricity bill, cost becomes SIMPLICITY, via Occam's razor** — MG: *the razor carries the assumption that the universe is logical in a specific way; if the universe is so logical as to let the razor work this well, it prefers clean code, and that means the universe is as simple as it logically can be.* Must still survive the selection-effect counter and the minimality-vs-compressibility gap.
- **The publish gate exists (`AIW-185`).** `AIW-167`: nesting preserves class membership, not architecture. `AIW-164`: only the efficiency/simplicity lane remains at cosmological scale.
- **Versioning: no version per finding.** **Cosmology and FMT stay decoupled in public until the cost question has an answer.**

## 2026-08-08 (S297) — Submission timing: journals ride the conference, preprints run ahead
MG: *"no because the submission must be around the conference somewhen, to get the papers in review before is risky, desk reject could be too fast, but as preprints of course yes"* and *"a certain quality should be reached."* **Preprints are unconstrained; quality gates submission, not the calendar.**

## 2026-08-08 (S297) — The vacuity objection fails, and CRU-36 was being over-cited
- **The vacuity objection fails on an equivocation** (which graph); on encode/decode graphs the claim is contentful, contested, not decidable — never "vacuous" (`drafts/aiw186-vacuity-regime.md`).
- **CRU-36's pool collapse is a post-hoc diagnosis** — cite the measured saturation result (0.996 → 0.479 at τ=25).
- **Any causally-generated-inside-the-horizon mechanism is in the dead class;** target the initial condition. `AIW-187`: a one-parameter account locks n_s to r.

## 2026-08-10 (S299) — MG's eight rulings on the S298 decision queue
- `AIW-198` MoC7 wording: wait for the official window (passed). `AIW-194` → P1. `AIW-130` JAIC architecture slate confirmed.
- **`AIW-36` RIM venue — no APC money;** every paid-APC venue is out.
- (`AIW-197` connectome and siibra: merged into the S298 addendum entry.)
- **Freeness gradient (MG):** *"freeness gradient: agree, no book fallback though, either v15 or later. Nature/nurture rationale: also agree."* It goes to the FMT master, **never to the book or blog as a consolation home**; nature/nurture to the companion. Whether book/blog carry it after the paper is not ruled.
- **The two causal pathways: THE READING (short-term) and THE CARVING (long-term)** (MG); the timescale is always stated.
- **Naming: DREAMING and MATURING, one vocabulary across paper and book** (MG: "dreaming and daydreaming to me is the same kind"); the continuum claim is not FMT's.

## 2026-08-14 — Theory of mind is a world-model operation, not a rung on the *erweitert* ladder (MG)
MG: *"my theory doesnt have this problem at all, because it has a free universal modeling system and a means to use a rich self model as template, so there is no more need to explain theory of mind."* ⇒ ToM is the EWM's free instancing with the ESM as template (pattern #28); **a listener is an instance, not a posit.** Concede Bennett's structural observation; only §7 wording owed (`AIW-211`).

## 2026-08-21 (S305) — Conference travel: a standing constraint, not a per-event judgement
MG: *"not going to sydney or ANYWHERE outside EU unless being paid flight and hotel."* ⇒ **Any non-EU venue is out by default** unless flight and hotel are covered; the filter runs FIRST. EU travel is fine; a travel-paid invitation is worth pursuing.

## 2026-08-21 (S305) — The reference gate now checks the artifact that ships, not only its source
Each cited `.bib` entry must match, by content (≥0.90 similarity), a verified markdown reference and inherits its verdict. Why: the PDF builds from `references.bib`. **Before excluding anything from a gate, check rather than reason.** An honest red beats a meaningless green.

## 2026-08-26 (S311) — FMT v15: the second Fable review, completed and folded in
- **American English throughout** (dialect sweeps exclude spelling-identical words); **"criticality commitment" → "Class 4 commitment"**; **Prediction 4 stands** (S204 ruling retired for its lucid-dream half); **kind/degree is stated as a price, not a barrier**; **Siegel & Jarvik 1975 dropped** — an unverifiable citation does not ship.
- **⭐ Budget the verification wave from the start; never fold a deep finding in unattacked** (7 of 9 deep findings refuted).
- A regex cannot identify `backlog.md` entries; a quiet subagent transcript is not a stall.

## S313 (2026-08-27) — two papers published, RIM re-typed, and three instrument lessons
- **Widening a narrow decision must be asked for, not assumed** (MG delegated cosmology: *"cosmology: go by your own instinct"*).
- **RIM's thesis: the field MIS-TYPED its components** (Performance a capacity, Knowledge split structure/process, Motivation the allocation policy).
- **Check the PREVIOUS session's repairs.** Measure new prose against the document's prior baseline; ask what input would make a green gate fail.
- **Trust the drift check and citation gate, not a read-through.** Anchor substitutions on strings unique to the target.

## 2026-09-09 (S318) — Gmail triage, and what it turned up
- **Read the OSF API, never the HTML page.** A support desk's claim about state is not evidence of state.
- **Check `in:sent` before believing a tracking file that says an email was never sent.**
- **`llms-full.txt` is the leverage point for what AI systems say about FMT.**
- **BBS gets no further investment (MG):** *"im in consciousness research, RIM is a cheap byproduct, not investing into psychology pseudoscience."*
- **Deferrable work queues behind work in flight** (MG).

## 2026-09-23 (S321) — Emotions are qualia; memory and time are closure prerequisites for human-like consciousness
MG: *"emotions ARE qualia, not base properties, they are the purest kind of qualia probably. memory and experience of passage of time are crucial to human like consciousness or how else could an entity create a model of itself, apply it and confuse it with itself? so the 2015 book may have been sloppy here."* The monograph (p.263) was sloppy; memory and passage-of-time experience are required for human-like consciousness because closure needs them. Discrepancy #6 in `.claude/knowledge/fmt-2015-definitions.md`; `AIW-267`, `AIW-153`.

## 2026-09-23 (S321) + 2026-09-30 (S327) — MoC7 poster figure: BUBBLE (ruled three times; merged)
MG (S321): *"bubbles and that decision was already taken once, i am irritated now."* MG (S327): *"bubble and i told you that a million times now!!!"* The poster uses the real/virtual bubble figure. **A figure/variant choice is a decision and goes to this file the moment it is made — and the fix is mechanical, not a reminder:** the build produces only `moc7-poster-A0-proof-bubble.pdf` and refuses a non-bubble poster; the grid proof is deleted; stale "open" lines corrected.

## 2026-09-26 (S322) — AIW-267: "arguably the purest kind", reason clause kept
MG: *"'and arguably the purest kind' would fit better, we have no probability."* §3.4.4: "Emotions are qualia too, and arguably the purest kind", reason clause kept (MG changed only the hedge word).

## 2026-09-29 (S326) — AIW-271: criticality requirement re-scoped to capability
`aiw91` locked decision #1 (MG, crucible's wording): *"Class 4 capability at the level carrying the self-model, instrument chosen per level, every σ reported beside its rate-matched surrogate."* "σ≈1 by self-organization" is no longer a requirement. Why: crucible CRU-194/198 showed the σ instrument is a rate meter. FMT §8.9 no longer calls σ and λ interchangeable instruments. Audit: `docs/cru198-sigma-audit-2026-09-29.md`.

## 2026-10-01 S328 — RIM retitled; formalization roadmap closings removed; three deposits
- **RIM title (MG):** the first part *"is noninformative and ridiculous and AI slop all at the same time"* → *Motivation as Allocation Policy and the Mis-Typed Components of Intelligence*. Not-X-but-Y titles are blocked by `register_gate.py`.
- **Formalization roadmaps:** "What Formalization Buys — And What It Cannot" → *Scope and Limits*; aphorism closings removed. Raw-markup formulas fixed; `pdf_markup_gate.py` refuses such a PDF in `zenodo-upload.sh`.
- **Edge-peak replication = crucible P0 (MG):** *"these are top prio replication targets, nothing triggers a negative review more than two chapters stating non-replicated results"*.
- **FMT v16 deposited 2026-10-02** (MG: "fmt main paper accepted … deposit fmt"); the single-run edge-peak shipped as single-run.

## 2026-10-02 S329 — Criticality is not required for consciousness, in machines or (probably) in brains
- **MG, verbatim (2026-10-02):** *"artificial systems do not need criticality for universal compute, and the human brain also doesn't need it probably, its probably just an energy management thing that causes criticality to become measurable. in a class 4 cellular automaton, certain areas may not look like criticality in a long time, what i found in 2005-2015 was that criticality should be a signature of cellular universal compute, but not a necessary property throughout. that this signature orccurs in the human brain and is associated with consciousness is a hint at the explicit models "using" cellular automaton computing mechanisms, or more precisely that free modeling seems to cause criticality patterns in human brains, not that criticality is needed. the same kind of processing may be sub critical in other implementations, and may well be subcritical even in human conscious processing part time, just no evidence yet. so it might be that only certain kinds of conscious processing causes criticality patterns only in brains of a certain kind and only when the tasks are of a certain size. a human brain when consciously computing (cognition) recruits probably a lot more than is required for the modeling task alone, and it needs to keep survival work running in parallel. that may not reproduce cleanly in a much smaller brain. this should not stop our robot from being conscious, it just makes his consciousness way more simple. consciousness requires free modeling and four models, not criticality!"*
- **The ruling:** consciousness requires **free modeling + the four models**; criticality is not a requirement. Free modeling **causes** criticality patterns in brains (probably an energy-management side effect), a conditional signature; subcritical dynamics only make the robot's consciousness simpler. CRU-203's driven-stable optimum is consistent.
- **S277's biological-scope necessity retired** (MG chose "retire necessity"); `prediction-framing.md` and `project-reference.md` rewritten. The ban on reverse and biconditional forms stays.

## 2026-10-07 S331 — "Free modelling is necessary", the poster wording; v17 released before MoC7
- **MG:** *"we would need to replace the term criticality with free modeling / free copmutation"* — poster/handout: *"free modelling is necessary, not sufficient. No free modelling → no consciousness, never the converse."*
- **MG hypothesis, unresearched:** *"i believe criticality might be necessary in efficient spiking implementations or biological systems for some reason."* Do not sweep to a blanket "never necessary" first (left OPEN at S332).
- v17 released before MoC7 (MG: *"i want v17 live before tomorrow"*); poster board P56.

## S332 (2026-10-07) — FMT v17 released: free modelling necessary, criticality a signature
- **MG rulings:** A#6 kept with floored numbers (0.61–0.76) + "pending independent re-analysis"; Table 1b falsifier = "robust consciousness where a fixed lookup reproduces the system's behaviour on novel input" (baseline refined S355); MG's criticality-in-efficient-spiking/biology hypothesis left OPEN, no claim (`docs/research/criticality-necessity-spiking-bio-2026-10-07.md`).
- **Sweep by *role* (does the passage make criticality a condition?), not by phrase** — Fable found implied-condition passages a phrase sweep missed.

### S332 (2026-10-07, later) — ruling propagated to all papers; FMT v18, cosmology v7, SB-HC4A-formal v4, RIM-formal v4
- **Out of scope by ruling:** physical/cosmic criticality in SB-HC4A (Axiom 3, cosmic SOC); CMB paper; RIM main paper.
- **One review pass per release is not enough for a ruling that pervades a 160-page text;** the role test lives in `docs/research/v17-propagation-brief.md`. eNeuro opinion retitled (MG): "Near-criticality does not set the level of consciousness: an architectural prediction, and how to falsify it".

### S333 (2026-10-08) — cosmology v8 published; SB-HC4A-formal Module 2 rewritten in source
- **Cosmology v8** (concept `…18698605`): Class 5 via rule *or* initial data; §6.4 capacity / irreducibility / constitutive limits separated from Gödel; **§7.3 correspondence limited to the implicit/explicit axis** (no cosmological world/self axis — FMT's direct/indirect-feedback criterion needs an outside).
- **SB-HC4A formalization v5** (concept `…22133504`): Module 2 κ column → logical depth; false Corollary → Proposition + depth Conjecture; Rule 110 typical-orbit claim dropped (no invariant uniform measure).

## S342 (2026-10-19, WSL) — PLR route closed; submission order; cross-check rules
- **PLR "Loops" commentary:** window closed; publish via blog in addition to the Zenodo preprint (`AIW-228`).
- **AIW-48:** parked, low priority, no study and no outreach for now.
- **Cross-check (AIW-303) runs before the JCS carve.** Published works: a new Zenodo version immediately only for errors that change a claim; the in-silico companion counts as published.
- (Def A "wait for Signorelli": merged into the S345 Def A entry.)
- **SUFFICIENCY-19 (MG):** master §3.7.3 "must actually perform it" = a realized trajectory with internal dependency generated by an open-ended rule (not a process-in-time condition); No Outside + Worm keep the record-equals-run argument.
- **Cross-check rulings (MG):** D1 propofol sentence aligned with Boly 2012; D2 "a discrete Laplacian approach"; D3 "no replay within the recurrence time"; D4 "gating"→"selection" corpus-wide; D5 **"cost window" everywhere (not "fit window")**; D6 Palmer clause cut; D7 misconception-registry edits kept; D8 priority dossier: 2015 derived Class 4/free computation and predicted the near-critical signature; D9 wiki "four models" → "model kinds".
- **JCS AI policy (MG):** *"you did not create my content! You made English wording from my German thoughts and German prior work"* — the AI statement says exactly that (ideas, arguments, conclusions the author's, from his German-language work; AI rendered them into English and improved language; author reviewed and is responsible).
- **No Outside Zenodo v2 DEFERRED (MG):** minimal corrections go out with the next real change or the KDP update; label for that release: v2 (tooling accepts only vN). **[S359: 'v2' RETIRED (MG) — semver v1.0.x as shipped; v2.0 only for a substantive rewrite.]**
- Priorities: AIW-304 P3, AIW-305 P2, AIW-306 P3, AIW-302 P2.

## S343 (2026-10-20, WSL) — AIW-310 framing; new-item priorities
- **AIW-310 claim:** relative form only — the unpleasantness–intensity GAP scales with self-model disruption, dose and expectancy controlled (Gerrans 2020/2024 already argue the coarse version). Implicit-marker sub-prediction dropped for now. First-person basis (THC, martial arts, mental training) is origin, not evidence.
- **AIW-310 approved into the master** as Prediction 8, §8.9; implications and in-silico programme move to §8.10–8.12. FMT v22 published; v23 corrected a Thornton et al. (2024) misreading. **Never cite a meta-analysis result in a master from the abstract alone.**
- **Kleiner framing:** No Outside's reading limit bounds only the strong claim (a formalism certifying that its structure *is* experience); formalising consciousness theories stays legitimate. Answer him by question, not refutation.
- **Handover 5–7 (MG):** re-upload Kindle after simbook's superscript fix; the robot plea's only text is `drafts/zenodo-ready/robot/`; No Outside source of truth = `drafts/zenodo-ready/nooutside/no-outside-draft-v1.0.md` (`scripts/build_monograph_pdf.sh` never writes an md).
- **No manual version pins / concept DOI only (merged: S270, S295, S343):** cite Zenodo works by concept DOI only — README, web properties, ORCID, outreach (S270, S295); direct file links go to a stable URL whose file is replaced each release (FMT: the canonical PDF in the public GitHub repo) (S343). Enforced by `scripts/test_doi_pins.py`; MG approved it fleet-wide.
- Priorities: AIW-307 P2, AIW-309 P3, AIW-310 P2.

## S344 (2026-10-20, WSL) — three preprints; theory map as standard figure
- **Theory map is FMT's standard overview figure** (MG: *"this theory map is gold, it must be prominent on my research page and the standard model figure"*). Source `scripts/build_theory_map_popsci.py` → `figures/theory-map.*`; infrastructure owns the web cuts.
- **Paper 3 shipped with drawn figures, not drawing specs** (Zenodo files are immutable).
- **Paper 3 framing:** every contradiction record states whether its experiment decides it; verdicts declared single-coder; independent coding before journal submission (AIW-313). **[S359: independent-coding requirement RETIRED (MG); single-coder verdicts declared as such suffice.]**
- **AI-use statement** for papers 1, 3, 4 follows MG's S342 wording and names "Claude (Anthropic)".

## S346 (2026-10-20)
- **Kleene correction in No Outside:** the generator can appear whole (quine, Kleene 1938) but only as a finished state; the generating does not appear in its own product. Kleene and Russell/Gödel are the existence and negated readings of Lawvere 1969. Ch.7 retitled "The Apparatus Not Seen at Work" (MG).
- (Blum first contact: merged into the S345 handover entry.)

## S349 (2026-10-21, WSL) — Prediction 2 salience under salvinorin A; v24
- **Prediction 2 follows salience under salvinorin A (MG):** the redirected ESM takes up the most salient content even without bodily contingency; input tracking is conceded to PP; separating test = salience × heartbeat synchrony with an under-drug contingency check. Salvinorin A only (psilocybin may leak too much internal processing). Dose window Maqueda 2015 (`docs/aiw319-prediction2-vs-pp.md`).
- **Theory-map overview is a master figure (MG D5):** §7 Figure 4.
- **Publish-gate deferrals are temporary (MG D7):** undefer ASAP.
- **Outreach rules:** Montoya → institute member/advisor offer; Stewart → informational only (INS-07); O'Keefe → unpaid board seat + keynote with costs paid and per-contribution fee, no amounts; Unterhofer → only "a patient of yours recommended you", never the person.

## S350 (2026-10-21, WSL) — undefer pass, FMT v25, JCS
- **Prediction 8 names both psilocybin and salvinorin A (MG option c).** P8 needs self-model dissolution, not outward migration; the salvinorin arm stays below the external-perception gating dose (Maqueda 2015).
- **Zenodo FMT description carries research.matthiasgruber.com/moc7/** — added with a version, not as a standalone metadata edit (MG).
- **AIW-137 and AIW-283 closed;** /moc7/ keeps ONE robot video (the teaser). DMS TEC-013 was filed for archival, not website changes.
- (Independent coder: merged into the S345 handover entry.)
- **JCS register:** JCS takes neither technical philosophy nor technical/computational papers; fit = non-technical essays (*Silent Suffering*; the SMoC middle-layer essay AIW-146 would also fit).

### 2026-10-21 S351 — Emergenz Zenodo order (AIW-326)
v1 (2015 Lulu original) first; MG then overrode the wait: v2 deposited at once with the "[DOI folgt]" placeholder, the record description carries concept DOI 10.5281/zenodo.23538664, and the preface gets it in v3.

## 2026-10-21 (S351, MG) — "Emergenz" links follow the No Outside rule
matthiasgruber.com links *Die Emergenz des Bewusstseins* only to the paid editions (Lulu, Amazon once live), never the Zenodo DOI; the research site also links Zenodo (concept 10.5281/zenodo.23538664). MG: *"same rule as for no outside: private homepage links to amazon / lulu only, research site links to zenodo as well"*.

## 2026-10-21 (S351, MG) — name: the "readout fallacy" (German: *Auslesefehlschluss*)
Inferring the structure of a capacity from the structure of the data an instrument can read out of it. 2015 source: Emergenz p.45 (Lulu) — the hierarchical IQ factor model only "bedeutet, dass die Leistungsdaten, die ein typischer IQ-Test erheben kann, so strukturiert sind". MG picked the name from four options; fits the 2015 data definition (*Lesevorrichtung*). No established prior use found (S351). Distinguish from reification, the ecological fallacy and the jingle fallacy. Used in AIW-331 and AIW-322.

## 2026-10-22 (S352, MG) — Silent Suffering to JCS; plea §2 reframed; structural-slop rule
- JCS (Horswell) accepted the essay for consideration while JAIC stayed silent, so the S351 routing rule fired: submitted to JCS, withdrawn from the JAIC offer.
- **Plea §2 (MG):** leads with an architectural profile largely independent of current theories, with two handles (identify systems at risk; prevent suffering by design); FMT credited in one clause; criticality off topic.
- **Structural-slop rule (MG-approved):** fencing, verdict template, thesis cadence, coinage stamps with per-profile ceilings; after simbook's SIM-80 calibration, negation-share and thesis-ending ceilings are not gates (human argument negates as much) and denial openers are the gated separator.

## S354 (2026-10-22)
- **AI-slop rules are density limits, not bans** (MG: "absolute bans are not intended, just accumulations and overuse"). The one hard ban is a version number in a live surface.
- **No Outside Chapter 14: the two answers are "unfolding view" and "structure view"**; FMT takes no stance between them (FMT v27 §3.4.5). Why: "first/second horn" lost the reader.
- **A self-funded salvinorin A study is out** (MG: "unaffordable for me forever"); route Prediction 8 to funded psychedelic labs and a drug-free thesis baseline.

## S356 (2026-10-23, MG)
- **D1/D2:** Cortex Viewpoint prep; RG details batch before Emergenz.
- **D3: the Bonn reanalysis is cut from the Cortex Viewpoint.** Ettinger (data controller of Lehmann et al. 2022) objected on 2026-06-18; MG replied he would not publish without consulting them (Gmail 19ed60eaf7da503d). **Never put the Bonn trial-level data, `results_metaketa_standard.csv` or reanalysis numbers into any deposit or submission without Bonn's written consent.**
- **D5:** Viewpoint title as a question. **D6:** affiliation region-only (Vorarlberg, Austria). **D7:** suggested reviewers Rahnev + Shew. **D8:** CORTEX-D-26-00961.
- **AI statement for Elsevier submissions follows S342** (Elsevier names AI agents explicitly; the short line understated the use).
- **D9:** NoC slice goes to *Minds and Machines* first (queue #6); the Worm waits for a later decision on M&M or a second venue. **[S359: conflicted with the record — the Worm was already submitted to M&M on 2026-10-21 (S349). MG ruled: submit both.]** **D10:** AIW-338 P3.
- **Gmail:** the Submissions filter uses a query (`from:(… OR …)`); OR inside the From criterion never matched.
- **D11:** NoC slice sole-authored; Sousouri's provisional co-authorship dropped. **D12:** Fable spine audit of the NoC slice before any rewrite.
- **D13:** MG rewrites Silent Suffering in German; Claude translates it faithfully (no restructuring, no added claims); offered to Graham as an unpolished translation replacing #8090. Why: authored text + language-only AI use is what Imprint's policy permits.
- **D14–D17:** local zero-shot detection is unusable on this material (Falcon inverted AUROC 0.25; Gemma-4 E4B misranks); weights deleted (MG). Pass-detection-plus-full-disclosure rewrites for venues permitting disclosed AI writing agreed in principle; D17 measuring stick = manual GPTZero/Pangram web scans, public texts only (GPTZero voided S357). **[S359: SUPERSEDED — MG ruled S334 stands: no rewriting aimed at passing detection.]**
- **Fable by default (MG):** *"use fable more we are approaching 50% opus usage but only 16% fable usage"* — red-teams, audits and research go to Fable; Opus for consciousness-theory prose drafting (classifier risk) and when Fable returns 429.

## 2026-10-23 S357 — GPTZero is not a measuring stick either
MG: *"ok so gptzero is useless also"* (GPTZero scored his hand-typed German draft 100 % AI). With the S356 local failure, no AI detector counts as evidence for our texts; the JCS defence rests on the accurate AI statement and MG's German original (AIW-284).

## 2026-10-23 S357 — AI detection: workflow unchanged, no commercial detector (AIW-341)
- **D1, MG:** *"we change nothing. the world and especially the publish or perish culture and the old school journals will have to adapt or perish"* — German → Claude translation and polish stays; the defence is disclosure plus provenance.
- **D2, MG:** *"no, either we find sth local or we defer it"* — no commercial detector API on unpublished work; AIW-341 deferred.

## 2026-10-24 S359 — decisions.md contradictions ruled (MG, from the S358 monthly review)
- **D-S359-1 AI detection:** S334 stands — no rewriting aimed at passing detectors; S356 D14–D17 rewrites superseded.
- **D-S359-2 AI statement:** the S342 wording (German origin, names Claude (Anthropic), reviewed-and-responsible clause) is the one; S334's text retired. Chosen side by side.
- **D-S359-3 Independent coding before journal submission:** retired; single-coder verdicts declared as such suffice.
- **D-S359-4 No Outside label:** "v2" retired; semver v1.0.x stays, v2.0 reserved for a substantive rewrite.
- **D-S359-5 Terminology:** "cost window" everywhere (S342 D5); "fit window" retired, didactic-patterns #11/#18 updated.
- **D-S359-6 Review artefact default:** changes-highlighted LaTeX PDF, not HTML.
- **D-S359-7 S243 "conditional dissolution":** superseded by PHENOMENAL-7 — transformation only, never dissolution, not even conditionally; S243 annotated.
- **D-S359-8 M&M clash (MG):** the Worm is under review at M&M (MIND-S-26-01918 (final MIND-D-26-01583), S349) while S356 D9 said the Worm waits; MG: *submit both to M&M*. 'One paper at M&M at a time' retired; the slice's six suggested reviewers share nobody with the Worm's six (`docs/research/noc-slice-s356-audit/s359-reviewers.md`).
- **D-S359-9 Pending files (MG):** `pending-s312-both-papers.md` (physics repairs verified applied, sb-hc4a.md:276/531/533) and `pending-cru36-prediction-revision.md` (§D ratified S266) deleted; §E play-as-free-modelling and §F VM tax filed as AIW-347 for the master.
- **D-S359-10 AI statement in the M&M slice (MG: "ok"):** full S342 wording on the title page; the same text without the German-work clause inside the anonymised manuscript.

## 2026-10-25 (S360) — M&M slice submitted; Fig 1 evidence; triage
- **D-S360-1 Reviewers (S360-2, MG):** all six suggested reviewers kept; the soft flags are co-authorships of contacts, not contacts.
- **D-S360-2 AIW-346 (S360-4, MG):** Zenodo metadata uniqueness keys on (title, version), so versions of one record may share a title.
- **D-S360-3 Fig 1a (S360-6/7, MG):** states drawn as regions, not points; waking reaches across the edge (Toker et al. call the side unsettled); LSD (75 µg) overlaps waking; axis ends "periodic / stable" and "chaotic / unstable" (Toker's own terminology: chaos is the "ordered" phase of edge-of-chaos criticality); the vertical axis is the state of the whole system. Evidence: `docs/research/noc-slice-s356-audit/s360-fig1a-research.md`.
- **D-S360-3a High-dose LSD:** no evidence places it on the axis; overdose coma is toxic, not anaesthetic.
- **D-S360-4 SSRN record on RG (S360-9, MG):** the January SB-HC4A item (DOI 10.2139/ssrn.6269858) is kept; it is the SSRN record, not a stray duplicate.
- **D-S360-5 Springer figure rule (S360-10, MG):** no titles or captions inside artwork; panel letters only; the text lives in the caption.
- **D-S360-6 Slice preprint (S360-11/12, MG):** deposit before submission — published 10.5281/zenodo.23637343.
- **D-S360-7 M&M submission by the agent (MG: "your job"):** submitted 2026-10-25, MIND-D-26-01607. EM's pre-approval "S" number is not the manuscript number; the Worm is MIND-D-26-01583.
- **D-S360-8 Backlog triage (S360-14/15, MG "apply all"):** 9 items to WAIT, 17 demoted (AIW-07 to P2: the preprint stays the publication of record), 9 closed, post-MoC7 block unparked. Record: `docs/backlog-triage-s360.md`.

## S361 (2026-10-26)
- **D-S361-1 FMT v29 published (S361-1):** 10.5281/zenodo.23660780.
- **D-S361-2 Anthropic guest-investigator call (S361-2/3):** skipped this round — no contact channel, no eligible institution yet, scope is biomedicine.
- **D-S361-3 Dualism instrument (S361-5):** full Riekki 12-item reflective-dualism factor, incl. 6 Stanovich-derived items (Stanovich permission 2026-10-25).
- **D-S361-4 AIW-343 data protection (S361-6):** explicit consent (Art. 6(1)(a) + 9(2)(a)) replaces the "not personal data" claim; public file k ≥ 5. Basis: `docs/research/aiw343-ethics-review-impact.md`. No Austrian statute requires ethics review; prior review still matters for journals.
- **D-S361-5 Reminders (MG):** no cloud routines (RemoteTrigger) for date-bound reminders — they leak information to the cloud and cost tokens. Use the fleet's own calendar/reminder system, made to reach both MG and agent sessions (cfg + infrastructure inbox items filed). Until it works, date-bound aIware items live in the backlog with a DUE date and in the handover.

## S362 (2026-10-27)
- **D-S362-1** Worm on the Disk → JAIC via Suzuki after the M&M desk reject (Suzuki 2026-10-26: all three offered papers fit). AIW-355.
- **D-S362-2** Silent Suffering stays at JCS (#8090) despite Graham's strict-AI-policy warning; no reply needed. AIW-284.
- **D-S362-3** (revised same session) Templer DAS: NO PLSclear. MG: *"we do not pay for scientific papers or data in general, except if there is a direct ROI"* (extends the S358 no-APC ruling to permissions/data). Drop or replace the DAS. AIW-343.
- **D-S362-4** No Outside stays typed Preprint (Zenodo + RG); Emergenz remains Book. Handover S362-1.
- **D-S362-5** AIW-349/350 at P2; AIW-355 P1, AIW-356 P3.
- **D-S362-6** Emergenz cover-page PDF goes to Zenodo under the existing filename `emergenz-de-2-pb.pdf`. AIW-353.
- **D-S362-7** We never follow journal transfer or recommendation offers after a desk rejection; we choose venues ourselves. Such offers are trashed and declined at the source. MG: unsolicited automated advertising presented as help, and a desk rejection gives no basis for any recommendation. 2026-10-27: Elsevier PLREV + Cortex offers declined on journalfinder; Springer (M&M MIND-D-26-01583/01607) complaint SENT 23:56 to swetha.murugan@springer.com (Gmail `1a17f93f02bda8ff`, research@, citing § 174 (3)/(4) TKG 2021, verified on RIS). Supersedes the S358 note in AIW-290 to look at the Elsevier transfer suggestions.

## S363 (2026-10-28)
- **D-S363-1 (S362-3)** JAIC format facts: MG opens the World Scientific guidelines page and downloads the templates (`jaic-doc.zip`, `jaic-2e.zip`) into Downloads. AIW-130, AIW-355.
- **D-S363-2 (S362-4)** Worm JAIC abstract: the 150-word proposal is approved as written. AIW-355.
- **D-S363-3 (S362-5)** Detector keeps the title "An Operational Detector for Machine Consciousness: …". AIW-130.
- **D-S363-4 (S362-6)** Detector AI-use statement uses MG's S342 wording, without the false "reported in the companion" clause. AIW-130.
- **D-S363-5 (S362-7)** Detector: one fix pass applies all 21 open minors, followed by an independent re-check. AIW-130.
- **D-S363-6 (S362-8)** Michiel's DFA bugs are offered only once the instrument exchange has been agreed. CRU-226.
- **D-S363-7 (S362-9)** Michiel's chapter: MG downloaded it (`Downloads/Complexity and Criticality in Neuro-Inspired Reservoirs.pdf`).
- **D-S363-8 (AIW-343)** The Templer DAS is replaced, not dropped: find a freely licensed death-anxiety scale. AIW-343.
- **D-S363-9 (AIW-357)** No further Perplexity pass. MG: *"we dont go over perplexity again"*, *"that was just a one time literature sweep"*. Its evidence tables are kept (audit, "What the dossier got right"). The audit's "revised brief" is retired. We do the theory work ourselves: a thesis sheet giving each thesis a canonical sentence, a "do not claim" line and a two-axis verdict, for MG to approve. Once approved, it is the brief that hands the book to simbook (MG: *"a brief for simbook, thats fine of course"*).
- **D-S363-10 (AIW-343)** The Templer DAS is replaced by the DAP-R Fear of Death subscale (7 items; Wong, Reker & Gesser 1994). The German version is DAP-GR (Jansen et al. 2019, CC BY 4.0, Table 3). Basis: `docs/research/aiw343-death-anxiety-scale-options.md`.
- **D-S363-11 (AIW-357)** Before the simbook hand-off, MG and the agent go through the thesis sheet one thesis at a time. The agent shows the doubts and issues with each argument, and MG answers with context, choosing from the agent's suggestions via AskUserQuestion. The sheet is updated after each thesis.
- **D-S363-12 (AIW-357)** Thesis walk-through complete. The book is about building efficient, useful and correct world models, becoming the self you want to be, and defining success as something achievable that won't kill you or drive you mad (MG, verbatim in the sheet). The nine theses are seeds, not chapters. Perelman is not a thesis 9 example; he is a candidate story for defining your own success. MG's own path is not used. The primitives list is a draft. The sheet goes to simbook now.
- **D-S364-1 (AIW-130)** Detector Fig. 2: the explicit-mode axis label drops "(phenomenal)" and reads "implicit (substrate) ←→ explicit". Explicit content is phenomenal only in the closed self-model loop (S341), so the axis must not claim it. Guarded by `test_fig2_explicit_axis_makes_no_phenomenal_claim`.
- **D-S364-2 (AIW-130, AIW-355)** JAIC manuscripts are built in LaTeX with `ws-jaic.cls` (author–year references via `ws-jaic.bst`). The templates are unpacked in `paper/jaic/templates/`. The guidelines PDF is not needed: the template and `paper/jaic/journal-guidelines-jaic.md` cover the format rules.
- **D-S364-3 (AIW-130, AIW-355)** JAIC needs American English. `build_jaic.py` maps British→American spellings in the JAIC output only; the .md sources stay British.
- **D-S364-4 (AIW-130)** Redraw the three detector figures before submitting, so that in-figure text prints at ≥9 pt at JAIC text width.
- **D-S364-5 (lrn)** The agent submits to journals itself and stops before the final click for MG's approval. Every manuscript delivered for review opens as its PDF plus a changes-highlighted PDF, never as a folder. Root cause: the aIware 'Manual process kits' rule named journal submission as a manual process for the user and prescribed opening an Explorer folder; the S363 handover copied it. Both are fixed.
- **D-S364-6 (lrn)** Link MG's ORCID to every account that offers it, at registration or at the first prompt. Root cause: no rule existed, and 'requested, not required' read as optional. Fleet-wide copy routed to cfg (dev-browser-ops.md). Existing accounts: AIW-360.
- **D-S364-7 (AIW-343, MG 2026-10-28, asked directly after ivoclar relayed INST-1/2/3)** (a) No ethics review: no UMIT RCSEQ and no Netzer ask. Consent and landing page state that the study is anonymous and not subject to mandatory ethics review under Austrian law. Venues are limited accordingly (PLOS ONE closed; others need a national-law exemption statement). (b) Launch Arm C (343101) today, after an OSF pre-registration with the analysis code frozen and a 3-response smoke test, which replaces the n≈10 pilot. (c) Employer clearance: done or not needed (MG). (d) D2 clarified: linking from the end page of MG's own Perplexity-survey instance counts as personal recruitment. A constant marker ?src=ppx is captured by a hidden question.
- **D-S364-8 (AIW-343)** OSF pre-registration h4n7f (https://osf.io/h4n7f; project hk8q6, private), registered 2026-10-28 11:40:46 UTC, before any data collection. Open-Ended Registration; subject Psychology; under embargo until 2027-01-31 (pending approval: automatic after 48 h, or immediate via OSF's email link). Contents: protocol.md, questionnaire-part1.md, consent-and-info.md, aiw343_analysis.py (frozen, SHA-256 prefix 497dceed39d3, commit 350df638), aiw343-p1.lss, MANIFEST.txt. OSF login via ORCID (OSF user 4npag).
- **D-S365-A (AIW-343, MG 2026-10-28)** Delete "[in cooperation with UMIT TIROL, Hall in Tirol]" from the participant information. There is no UMIT review (D-S364-7) and no UMIT co-investigator. Applied to `consent-and-info.md`, the rebuilt `.lss` files and the live 343101 (server-side edit by infrastructure, before any invitation). It is a deviation from the consent text registered in OSF h4n7f, logged in protocol §12.
- **D-S365-B (AIW-130, MG 2026-10-28)** The detector §6–9 is aligned with crucible's record (check: `docs/research/aiw130-s6-crucible-check-s365.md`, 0 wrong numbers, 13 status/framing items). The 2026-10-27 activity-not-regions ruling now applies to the paper: explicit models emerge as robust activity on a biologically close substrate, the plasticity is balanced and reward-gated, and the §5.1 graph result is stated without a self region. The gridworld transfer result stays, described as an agent with a hand-built self/other projection (construction, not emergence). The planner gap is capacity-relative (R5′ 0.45, RT-6). A near-unity branching ratio is reported descriptively and never enters a pass (crucible ruling 2026-10-02). Register items W1–W15 are all applied.
- **D-S366-A (FMT model definition, MG 2026-10-30 ~10:00, verbatim)** *"definition of model should say it is readable, not that it is actually read. that is only required for actual consciousness"*. Applied to the FMT master §3.1 and Table 1 (`.md` + `paper.tex`): read access = the representations can be evaluated by the system; actual reading is required only for consciousness (§3.4.3). Refines crucible's relay of MG's 09:10 ruling (WRITE confirmed, READ not required to claim explicit models); crucible told.
- **D-S366-B (CRU-234 follow-up, MG 2026-10-30 ~10:20, S366-C answered "Send now")** MG's hypothesis (verbatim in crucible inbox): the stable free-area structure is basic consciousness tracking the main pain/pleasure axis; it should survive limb change or small lesions, and if rich enough let the creature model its way around a new obstacle that reflexes cannot pass. aIware sent crucible five tests (input cut, anticipation, read test, lesion, detour) plus the untested targets (cortex-to-cortex prediction, own future, nonlinear). Status: hypothesis, not a finding; must-not-say unchanged.
- **D-S366-C (relay of crucible D7, MG 2026-10-30 ~10:00) — PROVISIONAL: MG hedged right after, verbatim *"i'd say probably yes"*; crucible D8: the frontal direction stays a CANDIDATE until an integration test.** A pattern that only re-carries its input area's signal probably counts as a simple robust explicit model; beating an input filter is a KIND question (robust vs dynamical), not a model criterion. Consequence in crucible: the free-frontal rate direction is a simple robust explicit model of hunger (3/3 creatures, 8k, learning off). aIware consequence: any text that treats input-locked patterns as non-models (detector §6–8, companion v7 AIW-361) must be checked against D7 before its next release.
- **D-S366-D (MG's framework for finding explicit models, crucible console 2026-10-30 ~10:00–10:15; verbatim quotes and paper cross-refs in `~/crucible/docs/decisions.md` 2026-10-30, D8/D9)** Recorded here as aIware's theory record. (1) **Model** = recurring activity that writes (follows) its target and is readable; actual reading is needed only for consciousness (= D-S366-A). (2) **Realistic explicit self model** = a lower-dimensional, integrated copy of the actual self; MG: *"for my self model to be significantly [different] to my implicit self models, i have to imagine being a horse or a chair, while i imagine myself realistically, what else than a lower dimensional, integrated copy of my actual self would i have as explicit self model?"* Flat: *"only complexer tasks and worlds and selves can start to show a strong difference between explicit and implicit models"*. (3) **World model** = *"all explicit modeling outside the self model"*; **active world model** = *"the part that reaches the self model"*; **active self model** = *"the part of the self model that acts on the world model"*. (4) **Closure** = the mutual updating between the active explicit self model and the active explicit world model (D9: "implicit" in MG's message was a slip), *"the explicit closure that gives rise to phenomenality, the sense of being here and now"*. (5) The non-active parts of the explicit world and self models = *"the 'subconsciousness' that the famous psychologists are talking about"*. Paper check against (1)–(5): `AIW-363`.
- **D-S366-E (relay of crucible D10, MG 2026-10-30 ~11:50; resolves D-S366-C)** MG chose "Explicit self-model now": the free-frontal weighted area-rate direction is recorded as a **first simple explicit self model**, an integrated, lower-dimensional copy of hunger + pain + danger proximity, 3/3 creatures (8k, learning off), **without closure** (no active world or self model). Two HEDGED hypotheses (to test, not rulings; paper tension noted by crucible against §3.5): *"basic awareness may already arise from non active explicit models without active closure"* (open: awareness as access, which §3.5 allows, or as basic consciousness, which §3.5 puts at a rudimentary closure); *"explicit closure might already give rise to a basic reflective self"* (open: §3.5 has no reflection at the minimal rung and reflection proper at the doubly extended rung). Source: `~/crucible/docs/decisions.md` 2026-10-30 ~11:50.
- **D-S366-F (AIW-363 term T1, MG 2026-10-30, verbatim)** *"the nesting is the normal mode of operation unless you have an out of body experience without body, like on a strong salvinorin dose with nothing for the body model to latch onto maybe, or the self model system being overwhelmed or damaged or sth. maybe cotard does sth like that also. but nested doesnt necessarily mean physically at the same neurla locations at the same time. nested is just saying that a conscious entity usually models itself within the world model, not somewhere else (where else would that be???)"* Nesting (ESM ⊆ EWM) stays; it is representational, not neural co-location, and compatible with D-S366-D (3), which identifies world-model activity as the explicit modelling outside the self model. Applied: one sentence after the nesting statement in §3.2 (`.md` + `paper.tex`), hedged on salvinorin and Cotard as MG was.
- **D-S366-G (AIW-363 terms, MG 2026-10-30, AskUserQuestion answers)** T2: keep **"preconscious"** for non-active explicit content (Dehaene's precise sense) plus one clause that psychology traditionally called it the subconscious; implicit knowledge stays "non-conscious" (MG first unsure: "not really sure what term is scientiffically more corect … or less poisoned by pseudoscience", then chose this after the reasoning). T3: adopt **"active world model / active self model"** in the paper; other uses of "active" become "running". T4: the **working model** (§3.6.1 channel occupancy) **is the active part** of the explicit models. T5: Principle 2's "survive their own inputs" **waits for crucible's CRU-238 input-cut result**. T6: §3.4.3 l.325 loosened to "its states and, where it has them, its geometry and capabilities". T7: boundary recognition **demoted** from a third model criterion to a consequence of the target (§3.1 "T fixes the model's boundary"); MG asked "how is read access different from readable?" — answer: identical since D-S366-A; the distinction that matters is readable vs actually read.
- **D-S366-H (AIW-363 T8 + H2, MG 2026-10-30)** T8, verbatim: *"they are generated by the substrate: correct. they are integrated from several implicit models plus sensory input plus motor feedback etc. as needed for the entity, modulated by salience and memory etc etc. the simplest possible self model would be a low dimensional model (not "copy") of the body or at least a viewpoint projected into the real world from which the senses seem to get their information."* ⇒ **"copy" is withdrawn** from ruling (2) and D10: the realistic ESM is a lower-dimensional, integrated MODEL of the actual self; l.178/l.417 ("generated … rather than filled by a copy") stay. Open sub-question (T9): does a "viewpoint" differ from the position estimate that l.325/l.401 exclude? H2: "reflective" = the self mirrored in the world model it closes with; one clause at l.401. H1 ("basic awareness … without active closure"): MG wants to discuss, no decision.
- **D-S366-I (AIW-363 T9, MG 2026-10-30)** MG chose "Yes, viewpoint ≠ position": a viewpoint is the origin the senses are referred to, the perspective that binds sensory input, not a coordinate on a map. The SLAM/position-estimate exclusion (l.325, l.401) stays; the paper names the viewpoint as the minimal self model and says how it differs from a position estimate.
- **D-S366-J (AIW-363 H1, MG 2026-10-30: "fourth reading is correct")** MG's hedged hypothesis *"basic awareness may already arise from non active explicit models without active closure"* (typed in the crucible console ~11:50, right after the result: integrated explicit self model, no active world/self model, no closure) means: non-active explicit models can close weakly on each other, and that **rudimentary closure** gives basic awareness — the paper's minimal consciousness — below the full **active** closure that gives "the sense of being here and now". Principle 3 holds (no experience without some closure). Applied: one sentence in §3.5 Minimal consciousness (`.md` + `paper.tex`). Status stays a hypothesis to test (MG hedged "may").
- **D-S367-A (AIW-296, MG 2026-10-30 ~18:05)** Next wiki redeploy only after MG has reviewed the S366 FMT changes and the new FMT version is deposited. `wiki/llms-full.txt` (rebuilt S366) carries the undeposited master, so Def A in the bibliography waits too.
- **D-S367-B (AIW-361, MG 2026-10-30)** Companion v7 is P1 and goes out before the detector's EM swap, so the detector cites a companion that matches crucible's record.
- **D-S367-C (AIW-130, MG 2026-10-30)** Re-check the detector's status claims against D-S366-C/E and change text only where a stated status flips; no new crucible citations. MG: *"1 but wait, some results are still coming in today"* — the re-check runs after crucible's results due later on 2026-10-30.
- **D-S367-D (AIW-363, AIW-364, MG 2026-10-30)** Priorities as proposed: AIW-363 P2, AIW-364 P1.
- **D-S367-E (MG 2026-10-30, replaces the proposed artefact-language exception)** No language rule. MG, verbatim: *"sponge mode for persons should have already (do now and lrn if it hasnt) ingested the information concerning kleiner and bickel concerning their preferred email language, writing mails must check with person data always, there could be addditional information like "always use gendering for this person" or "never mention xy to this person"."* ⇒ Mail language, form of address, gendering and never-mention topics are person data, recorded in the person's record and read before drafting. Kleiner's (German, du-form; never name the Erbprinz) written to contacts #39 the same turn; Bickel is an Ivoclar contact and was routed to the ivoclar session. Rule changes: S367 lrn, `docs/pending-lrn-audit-2026-10-30.md`.
- **D-S367-G (AIW-361, MG 2026-10-30)** The 2026-10-27 ruling reaches the gridworld transfer result: the companion says "built self/other module" (abstract, §4.3, §3.1, §4.6) and states that the dissociation is between agents built with and without that module, silent on whether such a model emerges as activity.
- **D-S367-H (AIW-361, MG 2026-10-30)** Hold companion v7 until crucible's results due later on 2026-10-30 are in, then report D10 and CRU-234/238 in v7.
- **D-S367-I (AIW-363, MG 2026-10-30)** Fix the FMT master §8 with AIW-363, in the same undeposited version: the Fifth–Seventh results become wiring results on a synthetic connectome that inform closure-experiment design and are not evidence for the architecture; the Fourth (A#6) takes the red-team scope (slow-reservoir memory, not a closure result).
- **D-S367-J…M (AIW-367, MG via Telegram while AFK, 2026-10-30 ~19:00, verbatim: *"all your recommendations but we will discuss s367-L further when I am back"*)** J: the formalization's §3.4 keeps the generation term (implicit activity generates explicit mass; nothing drifts across ν_crit), matching "generated, not copied". K: rank counts dimensions held as objects (identified, operated on), not items seen; the twelve Sperling letters are all seen but occupy the simulation as one low-dimensional pattern until identified — clause added to master §3.6.1 and §3.7 (md + tex) and to the formalization. L: the "two sorts of explicit model" sentence (robust sustained vs flexible dynamical patterns, MG's 2026-10-27 crucible spec) comes out of the formalization until CRU-238; **MG wants to discuss it when back**. M: formalization v7 deposits at its revised length (47 pp); a trim pass can come later.
- **D-S367-N (MG 2026-10-30)** Restore the CFG-609 sentence *"Label every list the user must answer with each item's stable ID or a short keyword, never a bare ordinal."* into global CLAUDE.md (dropped by cfg 0a26da91), and RCA what else merges dropped — MG: *"restore and rca and find out what else you merged into oblivion!!!!"*. Restore filed to cfg (P0); audit running.
- **D-S367-O (MG 2026-10-30)** *"given our knowledge base, nothing ever should have to rely or come from memory"* — aIware auto-memory emptied (archive `docs/archive/memory-2026-10-30/`).
- **D-S367-P (MG 2026-10-30)** Auto-memory off fleet-wide: migrate the 7 orphan memory rules, then `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` in the template settings, Check 4.7 on the real path, live test. Audit: `docs/reviews/2026-10-30-memory-audit.md`. cfg executes.
- **D-S367-Q (MG 2026-10-30)** AFD_TOKEN value printed into a subagent's local tool output by the memory audit: accepted, no rotation.
- **D-S367-L deferred (MG 2026-10-30)** The S367-L theory discussion moves to next session (*"since you obviously suffer from context rot already"*).
- **D-S367-R…U (MG 2026-10-30, lrn)** R: pre-push secret scan + masked settings.json reader (cfg); the March AFD_TOKEN copy in cfg's private history stays (no purge). S: restore "User actions go LAST" + CFG-609 no-bare-ordinals (and "or number them" → "or list them by stable ID"), subagent no-files guard, parallelization mandatory — MG: *"make sure these rules are checked again before being committed, time has happened in between."* T: rule-removal guard hook on rule-file commits + lrn self-integrity check. U: retire the CFG-24 token-cost table, restore "verified elsewhere ≠ safe to delete locally", leave the lrn roster-gap clause and the tool-call clause out. All filed to cfg; detail `docs/pending-lrn-audit-2026-10-30.md`.
