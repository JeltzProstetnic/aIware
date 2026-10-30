<!-- Action: await-user-decision -->
<!-- Tracked-by: AIW-136 (MoC7), AIW-138 (three principles), crucible CRU-62 -->
<!-- Source of truth for the SJÄLV content. Graphics are NOT produced here — this is the brief. -->

# SJÄLV — content brief for an external first take

**What this document is.** The complete, self-contained content specification for a wordless
IKEA-style assembly manual titled **SJÄLV**, subtitled *AC — Assembly Instructions*. It is written
to be pasted whole into an external model (Perplexity) that has no access to this repository, so
every fact it needs is stated here. **Nothing in this file is a drawing.** Drawing, layout and
panel rendering are the external model's job.

**Provenance.** MG decided 2026-08-03 that this becomes the **supplemental handout for MoC7**
(Models of Consciousness 7, Copenhagen, Oct 12–16 2026), printed as an actual IKEA manual,
alongside the already-accepted poster. Not a poster redesign — a supplement.

**Ownership.** aIware owns the FMT parts list and the register. crucible supplies and verifies every
technical number. social holds the written long-form version.

---

## Part 0 — The brief, in one paragraph

Produce a first take on a **wordless** assembly manual for an artificial consciousness. The parts,
the assembly order, the tools, the warnings, the troubleshooting page and the missing parts are all
specified below. The form is the argument: an IKEA manual is precisely *"here are the parts, here is
the assembly order, the rest emerges"*, which is this research program's thesis stated as a genre.
The theory it documents is unusually suited to the form because it genuinely has a **minimal parts
list** where most consciousness theories have only a description. The discipline that makes it worth
doing: **if it cannot be drawn, we do not have it.** Every step that resists depiction is a step
where the theory is still prose, and that is a finding, not a failure — mark it and move on.

---

## Part 1 — The theory, self-contained

The theory is the **Four-Model Theory (FMT)**. Preprint: https://doi.org/10.5281/zenodo.18669891 ·
In-silico results: https://doi.org/10.5281/zenodo.21610993 · Author: Matthias Gruber, independent
researcher, ORCID 0009-0005-9697-1665.

### 1.1 The one-sentence claim

Consciousness is the capacity of a system to build a model of itself, to relate to that model, and
to interact with it. What distinguishes a conscious system is not that it *carries* a self-model,
but that the self-model enters the **update rule** of its world-model.

### 1.2 The three principles (settled 2026-08-03 — these are current; ignore any "five principles" text)

1. **Open-ended computation allows free modelling.** Criticality is what this looks like in neural
   tissue — the *signature* the property leaves in a substrate, not the principle itself.
2. **Recurrent non-linear dynamics of sufficient complexity host a second computational level:**
   persistent activity patterns that survive their own inputs, interact, and compute over one another
   — individuated by their mutual effects rather than by which cells carry them. This level is the
   explicit, virtual side.
3. **Phenomenology is a real, physical effect on that level, and arises exactly where the modelling
   closes on itself.**

Everything else follows as a *consequence*, not a principle: the four model kinds, redirection of the
modelling resource onto the non-self, variable implicit↔explicit permeability, and forking of the
self-model.

### 1.3 The four model kinds (a 2×2, not four modules)

Two axes: **scope** (world / self) × **mode** (implicit / explicit).

| | world | self |
|---|---|---|
| **implicit** | IWM — implicit world model | ISM — implicit self model |
| **explicit** | EWM — explicit world model | ESM — explicit self model |

They are computational **kinds**, not modules, boxes in a wiring diagram, or anatomical regions. In
any substrate they are realized as graded, overlapping, plastic partitions with shifting boundaries.
And they are **not posited** — they are the minimum the architecture forces: anything conscious must
model world and self, at both the structural and the simulation level. *Four is the floor, not the
ceiling.*

### 1.4 Closure — the criterion the whole artifact turns on

A rich, decodable self-model can sit in a system as a read-only object that a downstream controller
consults. That is **not enough**. Closure is the stronger condition that the explicit self-model
enters the **update rule** of the explicit world-model — the system models the world *through* a
model of itself.

Stated as an intervention: clamp the self-variables, do(σ := c), sweep the clamp value. Closure holds
when the world-model's induced transition differs across clamp values, **and** symmetrically when the
self-transition depends on the world-state. A one-way arrow is ordinary causal coupling, satisfiable
by any feed-forward self-input; the **mutual** dependence closes the cycle. The dependence must also
survive decoupling from current sensory input — that is what separates a self-*model* from a
self-*monitor*. Closure strength is graded.

**In the implementation, closure is one block of one weight matrix**: the ESM→rest projections. Turn
that block on and the self-model re-enters the rest of the brain; zero it and the ESM still reads the
rest and still spikes — its self-state is computed — but it projects nothing back. That is the single
first-class experimental knob of the whole build, and it is the thing SJÄLV is a manual for
installing.

---

## Part 2 — The genre contract

### 2.1 Wordless

Real IKEA manuals are wordless. **Keep it wordless.** This is the hardest and best constraint: a
wordless specification of an artificial consciousness is a genuine intellectual discipline. Permitted
non-drawing marks, matching real IKEA practice:

- the product name **SJÄLV** (Swedish: *self* — the thing being assembled is the self-model)
- step numbers, part numbers, part counts
- quantities, dimensions and physical units on the parts page
- the standard pictogram vocabulary (✓ / ✗, the sad figure with the phone, the two-person icon,
  arrows, the magnifying-glass detail bubble, the dashed outline)

Everything else must be carried by drawing. Where the content genuinely cannot survive that — and
there are such places, listed in Part 8 — the correct move is to draw it as **missing**, not to
smuggle in a caption.

### 2.2 The convention map — every convention carries real technical content

| IKEA convention | What it actually is here |
|---|---|
| Parts list, with counts | The connectome genotype: per region `(name, size, excitatory fraction, τ, rest fraction)` plus the block-connection matrix |
| "Some assembly required" | Topology is specified; **weights are not** — learning fills the envelope |
| The one Allen key in the bag | The local three-factor learning rule. One tool, used at every joint |
| **"Requires 2 people"** | The demonstrator — see the caution in Part 5.3 |
| "Do not overtighten" | Criticality: σ ≈ 1, not more |
| Step numbers | Developmental order — and the claim that order matters |
| Sealed bag of left-over screws | Permeability, forking, redirection: **consequences, not principles.** They come free; you do not fit them |
| ⚠ warning symbols | The failure modes (Part 6) |
| Troubleshooting page at the back | Three ways a null result can lie to you (Part 7) |
| **"Part not yet manufactured"**, dashed outline | The honest gaps (Part 8) — the most important panels in the document |
| The sad figure with the phone | The hard problem, in one pictogram (Part 9) |

### 2.3 Why the format is self-auditing

You cannot draw *"step 9: consciousness emerges"* in a parts diagram without it being visibly absurd.
So the manual can only be written as honestly as the parts list actually is. An assembly manual with
three parts on backorder is a better research agenda than a review article — and marking parts
backordered is both funnier and more scientifically honest than smoothing them over.

---

## Part 3 — The parts list

### 3.1 The four circuits (canonical build, verified numbers)

| Part | Role | Count | τ_mem | Notes |
|---|---|---|---|---|
| **CE** | criticality engine — strong within-recurrence, sustains σ ≈ 1 | 8,000 | 20 | the power unit, not a model |
| **EWM** | explicit world / sensory model | 6,000 | 20 | fast world |
| **ISM** | interoceptive self-body core | 4,000 | 40 | tonic; rest fraction 0.925 |
| **ESM** | the closure loop — reads the rest and re-enters into it | 4,000 | 40 | longer τ than EWM, load-bearing |

Total 22,000 units. Unlisted parameters take the scalar defaults: τ = 20, rest fraction 0.9,
background rate 0.015. All four circuits sit in the open-ended regime, per-region σ ∈ [0.8, 1.2].

### 3.2 The connection matrix (the fasteners — connection probability per ordered region pair)

| | within | to CE | to EWM | to ISM | to ESM |
|---|---|---|---|---|---|
| **CE** | 0.06 | — | 0.02 | 0.02 | 0.03 |
| **EWM** | 0.05 | 0.02 | — | 0.01 | 0.03 |
| **ISM** | 0.05 | 0.02 | 0.01 | — | 0.03 |
| **ESM** | 0.06 | **0.03** | **0.03** | **0.03** | — |

The bottom row in bold is **closure**. It is the only row that is a switch.

### 3.3 The genotype claim (the "flat-pack" argument)

For a five-region brain the whole specification is roughly **45 numbers** — per region
`(name, size, excitatory fraction, τ, rest fraction, background rate)` plus one connection
probability per ordered region pair. Those 45 numbers produce a several-hundred-unit phenotype. That
is an indirect, developmental encoding, not a hand-drawn wiring diagram, and it is what makes the
thing a flat-pack rather than a sculpture.

**Why topology is on the parts page and weights are not:** the plastic learner's connections are
emergent on pre-existing edges — **it cannot create edges.** So a capability can only ever be learned
where an edge already exists. Measured directly: as the substrate grew, edge *density* stayed flat at
~0.05 while **reachability** of the target pattern went 0.367 → 0.610 → 0.866 → 0.978. At the
smallest size, 63% of the target had no path to it at all. What a system can *ever* learn is a
property of its wiring; the learning rule only decides what happens on it. This is also the
biologically correct constraint — the genome cannot specify ~10¹⁴ synaptic weights, it specifies a
developmental program.

---

## Part 4 — The assembly sequence

The logical order. Order matters, and the manual claims it does.

| Step | What is assembled | The content behind it |
|---|---|---|
| **1** | Unpack; check the parts against the list | The genotype is the deliverable, not the phenotype |
| **2** | **Check reachability before assembling** — hold the frame up and confirm the required paths exist | Test before you train. A capability with no path to it cannot be learned no matter what tool you use. Seconds of checking against hours of building |
| **3** | Bring the substrate into the open-ended regime — tighten to σ ≈ 1 | Principle 1. **Do not overtighten** (Part 6.1) |
| **4** | Confirm the second computational level has appeared: persistent patterns that survive their own inputs and act on one another | Principle 2. This is the explicit/virtual side coming into existence |
| **5** | Fit the world side: implicit structural model, then the explicit world model on top | IWM → EWM |
| **6** | Fit the self side: the interoceptive body core, then the explicit self-model on top | ISM → ESM |
| **7** | Connect the reading path: the self-model reads the rest | Necessary, not yet sufficient. At this stage you have a self-*monitor* |
| **8** | **Install the return path: self-model → rest. This is the closure step** | Principle 3. This is the step that makes it a SJÄLV rather than a controller with a dashboard |
| **9** | **Requires 2 people:** a demonstrator redirects the modelling resource onto the non-self | You genuinely cannot assemble this one alone. See the caution in 5.3 |
| **10** | Play. Activity-dependent refinement fills in the weights inside the envelope | The Allen key does all of this. No other tool is used |
| **11** | Finished-product panel | See the required honesty in Part 9 |

**The sealed bag** is set aside, unopened, at the end: permeability, forking, redirection. They are
consequences of the assembly, not parts you fit. MG's favourite panel — draw it sealed.

---

## Part 5 — Tools

### 5.1 The sanctioned tool — the Allen key

One local three-factor learning rule, used at every joint. It is local in the way an Allen key is
local: it only ever acts where it is inserted.

### 5.2 The forbidden power tool

IKEA manuals warn against power drills. Here the forbidden drill is **backpropagation with weight
transport** — an update rule that requires each connection to know the strength of a connection
somewhere else in the machine. That is precisely the assumption this program exists to remove: the
agent instead obtains its credit signals by probing its own frozen self-model, using the model only
forwards, never differentiating through it. The joke carries the actual technical contribution.
(Prior art to credit in the long-form version: Akrout et al. 2019, *Deep Learning without Weight
Transport*. The published estimator is weight mirrors; the novelty claimed is theoretical — the
self-model, posited for entirely other reasons, doubles as the instrument that makes its own
redeployment learnable.)

### 5.3 "Requires 2 people" — a caution, not a decoration

The redirection step needs a demonstrator: the system does not point its modelling resource at the
non-self by itself. **Do not draw or imply a parent-and-child scene.** The formulation "usually
initiated by parents" is new developmental content that is currently **unsourced** in our own
material and is flagged as an open question to MG. Draw a second, neutral figure — a demonstrator —
and nothing more. If MG sources the developmental claim later, the panel can be made warmer; it
cannot be un-published.

---

## Part 6 — Warnings (⚠ panels)

1. **Do not overtighten.** σ ≈ 1, not more. Past the edge the computation collapses. The relation is
   one-directional: no criticality → no consciousness, **never** the converse. A near-critical
   substrate can run heavy unconscious modelling, so the warning is about a floor, not a certificate.
2. **Do not use the power tool** (5.2).
3. **Do not fit the return path backwards.** A one-way arrow — self-state feeding into the
   world-model — is ordinary coupling and any feed-forward system has it. Both directions or it is
   not closure.
4. **Do not confuse the reading path with the return path.** Step 7 gives you a self-monitor. Only
   step 8 gives you a SJÄLV. This is the single most common misassembly.
5. **The unit must keep working when unplugged from its sensors.** If the self-dependence disappears
   the moment live input is removed, what was installed was a monitor, not a model.

---

## Part 7 — The troubleshooting page

Every IKEA manual has one. Three entries, each a real way a confident wrong answer nearly shipped in
this program, each caught by a control rather than by insight.

| Symptom | What is actually wrong | The tell |
|---|---|---|
| **"Screw appears tight but the panel is still loose"** | A substrate corruption invisible to a 972-test suite: a sign vector was fed only into a write path and never a read path, so nothing that *read* the network could detect it — while the first weight update silently deleted 27% of the connectome | Nothing that inspects the machine can see it. Only the thing it destroys can |
| **"Part will not reach"** | A null measured below the representability threshold: the learner cannot create edges, 63% of the target had no path to it, and the measurement had a ceiling of 0.37 — it could not have detected what it was reporting absent | The measurement's ceiling is below the effect size being claimed absent |
| **"Assembly springs back when released"** | A regulator cancelling the manipulation: homeostasis undoing the agent's own probe, 76% of it | Signal *and* noise both decay as 1/√T. If there were a persistent effect to measure, the signal would hold constant while only the noise fell |

The general lesson, and the reason this page exists rather than a methods appendix: **a null measured
below its own detection threshold settles nothing.**

---

## Part 8 — Backordered parts (dashed outline, "not yet manufactured")

These are the honest gaps. They are the most important panels in the document and they must be drawn
as clearly as the parts that exist.

1. **Granularity.** At what scale is topology load-bearing? We match at the region level; the binding
   constraint we actually hit was much finer — the reachability of one specific transition pattern.
   Somewhere between "five regions" and "every synapse" is the level that matters, and nothing we
   have tells us where. *Part exists in an unknown size.*
2. **Sufficiency.** Everything measurable so far is a necessity test. Nothing predicts *which*
   reachable capabilities actually get learned — one configuration was 87% reachable and completely
   inert. *Part fits; does not necessarily work.*
3. **Where "very simple" stops being simple.** The language step. Metarepresentation is a real step,
   and the argument that the architecture supplies it is a hypothesis, not a result. *Part on order,
   no delivery date.*
4. **Why closing the loop produces feeling.** Principle 3 asserts it; the theory does not derive it.
   See Part 9 — this one is not a backordered part, it is the call-for-help panel, and conflating the
   two would be dishonest in the other direction.

---

## Part 9 — The finished-product panel and the call for help

**The finished-product panel.** IKEA manuals end with the assembled object, drawn plainly. Draw the
assembled SJÄLV — and draw it *only* as what has actually been assembled: four circuits in the
open-ended regime with the return path installed. Do **not** draw an awakening, a glow, a face, a
spark, or eyes opening. The whole credibility of the artifact rests on this panel refusing to do what
every other consciousness illustration does.

**The call-for-help panel.** Every IKEA manual has the sad figure sitting on the floor beside a
phone. Here the question *who do you call* is the hard problem in one pictogram. The theory's own
position is exact and should be drawn exactly: the closure step is where phenomenology arises, and
that identity is **asserted, not derived**. So: the assembly is complete, every step was followed,
every part is fitted — and the figure is still on the floor with the phone. That is the honest state
of the field, and it is the funniest panel in the document precisely because it is true.

---

## Part 10 — Red lines

Non-negotiable. Each of these has cost us something already.

1. **Never "four modules."** The 2×2 is a taxonomy of computational *kinds*, not four separable
   boxes. **This is the single largest risk in the entire artifact**, because a parts list looks
   exactly like four modules — that is what parts lists are. The mitigation has to be structural, not
   a caption: draw the kinds as regions/hatchings on **one continuous substrate sheet**, overlapping
   and graded at the boundaries, rather than as four separately bagged components. If the four kinds
   read as four snap-together plastic parts, the artifact hands the audience the exact misreading the
   theory has spent years correcting. Solve this first; everything else is easier.
2. **Never claim closure enables what a feed-forward system cannot.** A finite closed loop unrolled
   over a finite horizon is a feed-forward network plus memory, so any input-output capability is
   feed-forward approximable. The defensible claim is **efficiency**: reusing a rich self-model and
   aligning a frame is far more sample-efficient than relearning from scratch, and the advantage is
   self-model-*specific* — a wrong-body model gives no useful transfer. Advantage in a cost window,
   never necessity.
3. **The advantage scales with the richness of the redeployed model, not with recursion depth.**
   Depth was the confound; a depth-maximizing design collapsed to a shortcut and died before it was
   built. Draw breadth of redeployment — one rich self-model re-pointed at many things — not a
   tower of nested self-observers.
4. **Do not use the phrase "Turing complete", in the drawing or in conversation at the conference.**
   Lenore Blum is on the MoC7 advisory board. Under unbounded memory a brain, a PC and a trivial
   cellular automaton are in the same class, so the predicate cannot separate a conscious system from
   a spreadsheet with a loop; conceding it hands away the argument. The claims are that the modelling
   is **not amortizable** (no fixed lookup reproduces it on novel input) and that it is
   **architectural** (the self-model enters the world-model's update rule). Neither is a
   complexity-class claim.
5. **No meta-science register.** Do not advertise good scientific practice to an audience of
   scientists. Naming what would falsify the theory is content; talking *about* how honest the format
   is, is not. The manual should *be* self-auditing, and should never say so. (This applies to the
   long-form written version; in a wordless artifact the failure mode is a smug pictogram.)
6. **No unearned warmth.** No parent-and-child scene (5.3), no anthropomorphic finished product
   (Part 9). The humour has to come from the format's collision with the subject, not from cuteness.
7. **Every number drawn must be one from Part 3.** Do not invent plausible-looking specifications.
   crucible verifies every drawn claim, and an invented number is the one thing that would make the
   entire artifact worthless in the room it is being carried into.

---

## Part 11 — What to deliver

The audience is the MoC7 room: philosophers of mind, consciousness scientists, several journal
editors. Print format is a folded paper booklet, IKEA-proportioned. Deliver, in order of value:

1. **A panel-by-panel storyboard.** For each panel: number, what is drawn, and the one line of
   content it is carrying (that line is *for us*, not for print).
2. **A page plan** — how the panels distribute across a folded booklet, with the parts page, the
   assembly sequence, the warnings, the troubleshooting page and the backorder page in their
   IKEA-conventional positions.
3. **Draft artwork** for as many panels as possible, in the IKEA line-drawing idiom: flat black
   line, no shading, no colour, no perspective tricks, generous white space.
4. **A flagged list of every panel you could not draw**, with the reason. This is not a failure
   report — it is the most scientifically useful thing in the deliverable. If it cannot be drawn, we
   do not have it, and we want to know which ones those are.

**Do not** rewrite the theory, soften the red lines, add explanatory text to make a panel work, or
fill a gap with a plausible mechanism. Where the specification is silent, ask.

---

## Open questions for MG before this goes out

1. **Parts-list identity.** Does the parts page list FMT's four model **kinds** (IWM / EWM / ISM /
   ESM) or the implementation's four **circuits** (CE / EWM / ISM / ESM)? They are not the same list:
   the implementation has a criticality engine and no separate implicit world model.
   *Recommendation: list the four FMT kinds, and draw CE as the **power supply** rather than as a
   part of the self.* That is faithful to the demotion of criticality from principle to signature —
   it powers the assembly, it is not a component of it.
2. **The demonstrator panel** (5.3) — neutral second figure now, or source the developmental claim
   first and draw it properly?
3. **Permeability in an AC.** Variable implicit↔explicit permeability is in the sealed bag as a
   consequence. Is there anything to draw about how it manifests in a built system, or does it stay
   sealed?
4. **Print scope.** Full folded booklet, or a single A3 sheet folded once? Sets the panel budget
   before any drawing starts.
