# Red-team review — §4.2.2 "The unrepresentable apparatus" and §4.2.3 "Readout and causal power"

Reviewed against: didactic-patterns.md (#13, #35, #36, #37 + scope guards + MG S299/S300 rulings),
prose-register.md (phrase list + register hunt + antithesis measurement), and §3.4.1–§3.8, §4.2.1–§4.2.5,
§10.3 of the paper. Passages as committed in 35f5e34d (identical in .md and .tex — mirror verified
paragraph-by-paragraph after markup normalization).

## Verdicts

- **§4.2.2 block ("The unrepresentable apparatus"): SHIP WITH EDITS.** Two severe findings (A1, A2), one
  high (A3), the rest medium/minor. Nothing requires pulling; the scope guard itself is implemented
  faithfully and there is no positioning leakage.
- **§4.2.3 block ("Readout and causal power are different relations"): SHIP WITH EDITS.** One severe
  finding (B1 — a genuine theory contradiction, one clause), one high (B2), the rest medium/minor.
  No positioning leakage.

## Positioning check (attack 5 — the decisive one): NO LEAK in either passage

- **Model-based vs model-free RL.** Closest approach is §4.2.3's "where a stored hedonic value is
  re-instantiated and run against candidate courses of action." Evaluation-of-candidate-actions is
  MB-RL vocabulary, but the sentence makes **no arbitration, override, habit, or recency claim** — the
  parts of pattern 35 that actually collide with Daw/Dolan territory (explicit route defeating a
  recency-weighted habit; implicit compliance) are all absent. What the sentence states is MG's settled
  S299 ruling (causal power = the quale issuing in further simulation, via *re-instantiation* — which is
  itself the FMT-vs-MB-RL differentiator the knowledge file names), i.e. theory content, not positioning.
  Nothing here can be contradicted by whatever the blocked positioning decision later decides. It may
  attract a one-line "this is model-based control" reviewer remark that the eventual positioning section
  will answer; it does not require that section to exist first.
- **Predictive processing.** No prediction, precision, generative-inference, or error vocabulary in either
  passage. Pattern 36 (weather simulation) is *not* used in these passages at all — no PP contact.
- **Revonsuo threat-simulation.** Nothing about dream function or threat. Clean.
- **Domhoff & Fox continuum.** §4.2.3 conspicuously avoids "dreaming"/"daydreaming"/"mind-wandering" —
  it says "recall or prospection" and "further simulation." The avoidance held. Clean.

## Findings — §4.2.2 block (ranked)

### A1 — SEVERE: the outside-level sentence asserts determinism the passage elsewhere declines
- **Current:** "From outside, the organism does what its substrate and its history determine it will do
  given its input."
- **Problem:** "determine it will do" asserts organism-level determinism as fact. Paragraph 3 of the same
  block says "The account is therefore neutral between them," and the paper's standing line (same section,
  two paragraphs up) declines the determinism question as "a question for physics, not consciousness
  theory." A reviewer quotes the two sentences side by side; and this is precisely the composition MG's
  scope guard demands (#37: the physics question is *declined*, not answered in passing). MG's spoken
  version ("doing exactly what its brain and genes are dictating") is fine as speech; in the paper it
  quietly answers the declined question. It is also the one sentence that lets the block be read as
  arguing *there is no free will* — the inference the knowledge file says is not FMT's to make.
- **Replacement:** "From outside, there is no missing cause: the choice issues from the organism's
  substrate and history given its input." (Neutral between deterministic and stochastic issuance; keeps
  the inside/outside parallelism.)

### A2 — SEVERE: "presents as a choice without one" collides with the block's own paragraph 2
- **Current (para 1):** "A decision consequently enters the simulation with its cause absent from every
  position the simulation can survey, and a choice whose cause is unrepresentable presents as a choice
  without one."
- **Current (para 2):** "the path actually taken is fully explained by reasons the moment one looks for
  them."
- **Problem:** A choice that is "fully explained by reasons" from the inside does not "present as a
  choice without [a cause]" — reasons are in-scene causes. The two sentences are quotably inconsistent.
  Additionally, the mechanism as stated overshoots phenomenologically: an event with no represented cause
  should present as *arbitrary* (things that happen to me), not as *free* (things I do). The
  phenomenology of volition is self-origination, not causelessness.
- **Minimal repair (keeps MG's "feels uncaused" at the level of production):** append to the para-1
  sentence: "— without one, that is, at the level of production: reasons appear in the scene as contents
  weighed, not as anything that produces the weighing's outcome, and the producing is the part with no
  representative in the scene."
- **Stronger repair (route through the self-model — resolves A3 as well, but touches #37's verbatim
  "feels uncaused," so needs MG's sign-off):** "A decision consequently enters the simulation with its
  generating cause absent from every position the simulation can survey. The simulation assigns it, as it
  assigns every event it must place, to the self — and behind the self-model the regress ends, because
  what stands behind it is the apparatus, which cannot appear. The choice therefore presents not as
  uncaused but as originating in the self, with nothing behind the self: felt freedom is what an origin
  feels like."

### A3 — HIGH: the digestion-class objection is unanswered
- **The objection a skeptic gets for free:** most causes go unrepresented without their effects feeling
  uncaused — nobody represents their gastric physiology, yet hunger does not feel uncaused. What
  distinguishes the apparatus case?
- **What the passage has:** only the in-fact/in-principle distinction ("not concealed somewhere within
  that scene, but of a kind that cannot appear in it at all"). That is necessary but not sufficient: the
  *mechanism* of hunger is also never represented by any actual subject, yet hunger presents as caused —
  because the body-model supplies an in-scene stand-in cause ("I haven't eaten"). Decisions also get
  stand-ins (reasons — para 2 concedes it). So unrepresentability of the true cause cannot by itself be
  what makes decisions special; the passage must say what is.
- **The answer available inside the theory:** bodily states are referred to the body-model, which always
  has a stand-in; decisions are referred to the *self*, and the self is the one locus behind which no
  stand-in exists, because what stands behind it is the apparatus. (This is the stronger A2 repair; if
  the minimal A2 repair is taken instead, add one sentence:) **Proposed insertion after the "cannot
  appear in it at all" sentence:** "This is not the ordinary incompleteness of any model. Most causes go
  unrepresented without their effects presenting as uncaused, because the simulation supplies a stand-in
  from the world- or body-model — hunger is referred to an empty stomach with no representation of its
  physiology. A decision is referred to the self, and the self is the one locus for which no stand-in is
  available: what stands behind it is the apparatus."

### A4 — MEDIUM: the §3.4.1 anchor runs in the wrong direction, and §3.6/§3.8 undercut the flat "cannot appear at all"
- **Current:** "not concealed somewhere within that scene, but of a kind that cannot appear in it at all,
  for the same reason that 'sum of column B' does not appear in a transistor-level description
  (Section 3.4.1)."
- **Problem (direction):** §3.4.1 establishes *upward* incoherence — the computational property is absent
  from substrate-level vocabulary. The claim here needs the *reverse* — substrate operation absent from
  the computational-level scene — which §3.4.1 does not establish and which is false in general: a
  simulation can describe substrates (this paper, written by a conscious system about its own apparatus,
  is such a description; the neuroscientist who knows Libet's result still feels free). "For the same
  reason" borrows a symmetry the cited section does not contain.
- **Problem (flatness):** §3.6 states in the paper's own voice that "processing-level activity becomes
  visible within the simulation" (blind-spot filling, phosphenes) — quotable against "cannot appear in
  it at all." And §3.8 already states the correct, scoped version of the present claim nearly verbatim:
  "the implicit models that generate the simulation are not themselves part of the simulation" /
  "principled opacity." Not citing §3.8 both loses the block's best in-house support and looks like
  unacknowledged repetition.
- **Replacement:** "not concealed somewhere within that scene, but structurally excluded from it: the
  implicit models that generate the simulation are not themselves part of the simulation (Section 3.8).
  The simulation can contain descriptions of brains, and substrate activity can intrude as anomalous
  content (Section 3.6); what it cannot contain is its own current generation, represented as the cause
  of what it is generating." (Drop the Section 3.4.1 clause here; the level ontology is re-cited two
  sentences later anyway via "Sections 3.4.1, 3.4.6".)

### A5 — MEDIUM: "an otherwise comprehensive model" is false by the paper's own account
- **Current:** "it is what the single gap in an otherwise comprehensive model looks like from inside the
  model."
- **Problem:** the paper elsewhere insists the simulation is drastically bandwidth-limited (20 Hz frame
  rate, selective permeability, most physiology unmodeled). The model is full of gaps; a reviewer lists
  three. The intended claim is that this is the one *in-principle* gap among many contingent omissions.
- **Replacement:** "it is what the model's one in-principle gap — as opposed to its many contingent
  omissions — looks like from inside the model."

### A6 — MINOR: register — "The account is deliberately narrow."
"Deliberately" narrates the authors' own move (prose-register: strategy-narration class). Flat bounding
is allowed; the adverb is not. **Replacement:** "The claim is narrow."

### A7 — MINOR: mis-anchored cross-reference
- **Current:** "the epistemic asymmetry at the implicit/explicit boundary (Section 3.4.3)".
- **Problem:** the implicit/explicit boundary is §3.6; the ESM-cannot-observe-ISM asymmetry is §3.8.
  §3.4.3's asymmetry is inside/outside *description* of a closed system — related but not the one named.
- **Replacement:** "the epistemic asymmetry at the implicit/explicit boundary (Sections 3.6, 3.8)".

### A8 — MINOR: "so the option is a real one" flirts with alternative possibilities
- **Current:** "others have taken it, so the option is a real one".
- **Problem:** read modally, this asserts genuine alternative possibilities for *this* organism — a
  libertarian-flavored claim para 3 declines. What others' having taken it establishes is only that the
  option is realizable in kind (not fantasy), which is all the undecidability argument needs.
- **Replacement:** "others have taken it, so it is no fantasy".

### §4.2.2 conformance to pattern #37 (both directions)
- Required and present: composition with the existing widening-of-will line (block opens by building on
  it, not replacing it); the explicit division of labour (physics declined / phenomenology answered); the
  deterministic-and-indeterministic invariance; "carries no evidential weight in either direction"; the
  Shaolin-monk undecidability rendered abstractly. All faithfully implemented.
- Forbidden and absent: presenting the account as evidence about determinism; the "therefore no free
  will" inference — **except** via A1's sentence, which is the one breach.
- Not included, not required here: the AC prediction (felt-freedom report in artificial systems) — the
  pattern flags it as unusual value but does not bind it to §4.2.2.

## Findings — §4.2.3 block (ranked)

### B1 — SEVERE: "available to systems well short of closure" grants qualia below closure
- **Current:** "A quale is read continuously: the implicit models generate a frame and use the resulting
  value as a live readout of the organism's state — the cheapest and most constant thing the architecture
  provides, and available to systems well short of closure."
- **Problem:** the sentence's subject is a *quale*; as written it says quale-readout is available short
  of closure. The paper's core architecture says otherwise: §3.4.2 makes qualia constitutive properties
  of the running self-simulation, §3.4.3/§4.2.5 tie phenomenal character to self-referential closure,
  §3.5 puts the entry level of phenomenal experience at EWM + rudimentary ESM. A system well short of
  closure has a value-readout (pattern #13's dashboard, tier-(i)) — but nothing it reads is a quale.
  MG's S299 ruling says the same: "live quale reading is just the self model doing its thing **via its
  closure recurrence**." The sub-closure availability belongs to the readout *function* (#13), and the
  compression of #13 into the quale sentence moved it onto the quale itself. A careful reviewer quotes
  §3.4.3 against this clause directly. This is the both-directions conformance failure: #13's content
  imported, but attached to the wrong subject.
- **Replacement:** "— the cheapest and most constant thing the architecture provides. The readout
  function itself is available to systems well short of closure; only at closure is the value read a
  quale (Section 3.4.3)." (Or, minimally: delete ", and available to systems well short of closure".)

### B2 — HIGH: "Being read is not a causal power." — unrelativized, and quotable against §4.2.1
- **Current:** "Being read is not a causal power. The value is a component of a system that has one, in
  the way an instrument's dial is part of a control loop without being the control."
- **Problem (the dial objection):** a dial in a closed loop is causally efficacious *precisely by being
  read* — intervene on the reading and behaviour changes. Under any interventionist reading, the flat
  denial is false. **Problem (internal):** §4.2.1 says "Qualia are not causally inert: as the self-model's
  evaluative representations they do genuine causal work" — and §4.2.1's worked example of that claim is
  the thermostat *display*, i.e. the readout, granted constitutive status in the feedback loop. §4.2.1's
  own spreadsheet-sum analogy makes "component of the computation" and "causally efficacious"
  compatible; the new block makes them exclusive. Same relation, opposite classification, two pages
  apart. The distinction that survives is not causal/non-causal but *power over simulation content*
  versus *input to implicit control* — and the block's own closing sentence already has the right
  relativization ("determines the content of what gets simulated next").
- **Replacement:** "Being read gives the quale no causal power over what is simulated next. The value is
  causally efficacious the way Section 4.2.1 already grants — as a constitutive component of the loop
  that reads it — in the way an instrument's dial is part of a control loop without being the control."

### B3 — MEDIUM: "actually requires" corrects §4.2.1 and misstates its ground
- **Current:** "which is what the theory's rejection of epiphenomenalism (Section 4.2.1) actually
  requires."
- **Problem:** "actually" reads as an in-text correction of §4.2.1 (register: the manuscript arguing with
  itself), and the substance is off: §4.2.1 rejects epiphenomenalism on the feedback/evaluation-loop
  ground, not on quale-initiated simulation. Two different grounds for the same rejection invites "the
  paper cannot decide why it is not epiphenomenalist."
- **Replacement:** "which is where the theory's rejection of epiphenomenalism (Section 4.2.1) cashes out
  at the level of the individual quale."

### B4 — MINOR: "the two collapse together easily" — ambiguous antecedent
- **Current:** "Both modes describe what the running self-simulation does; neither is by itself a claim
  about what a quale does, and the two collapse together easily."
- **Problem:** "the two" reads as *the two modes* — but the collapse being warned against (per AIW-202)
  is between simulation-capacity claims and quale-power claims.
- **Replacement:** "…what a quale does, and the two kinds of claim collapse together easily."

### §4.2.3 conformance to patterns #13/#35 and the S299 ruling
- The readout/issuing split is MG's resolved ruling rendered accurately (dashboard = component of a
  causal-power system; causal power begins where the value issues in associated simulation). The
  "re-instantiated" wording preserves the differentiator pattern 35's positioning note demands. The
  AIW-202 correction (inward mode ≠ quale causal power) is implemented by the closing sentence. Apart
  from B1's subject error and B2's unrelativized denial, the block is faithful to the source material.

## Prose register (both passages)

- Phrase list: clean — no throat-clearing, no "importantly/crucially", no strategy narration beyond A6,
  no revision-history narration.
- Measured antithesis rate: new prose 1.5 "rather than" per 1,000 words vs 3.1/1,000 document baseline —
  **below** baseline; no scrub needed. The not-X-but-Y constructions present all carry real contrast
  (location vs kind; absence vs misrepresentation) — keep.
- One flag: A6 ("deliberately").

## What was checked and found sound (do not edit)

- The scope-guard paragraph (para 3 of §4.2.2 block) implements MG's #37 guard fully and is the strongest
  paragraph in either insertion — apart from A6's one adverb, leave it alone.
- "which is a different thing from misrepresenting a fact the model contains" — genuine and defensible
  distinction (structural absence vs misrepresentation); it is what blocks the "illusion of free will"
  misreading. Keep.
- The .tex mirror is verbatim (markup-normalized comparison, all paragraphs match).
- No claim in either passage lands in RL/PP/Revonsuo/Domhoff territory (see positioning check above);
  neither passage needs the blocked positioning decision to ship.
