<!-- Action: await-user-decision -->
<!-- Tracked-by: AIW-146 (this draft), AIW-100 (SMoC working group / Bildstein charter), AIW-27 (SMoC wiki) -->
<!-- updates: .claude/knowledge/didactic-patterns.md, wiki/reference/glossary.md, docs/friston-500-smoc-opportunity.md -->
# The Middle Layer

**A first draft of a Standard Model of Consciousness — the medium-complexity representation the field does not have.**

Working draft, Session 285, 2026-08-05. Author: Matthias Gruber. Internal — not for circulation until the
naming and status decisions in §7 are settled.

---

## 0. The diagnosis, in MG's framing

Every mature science has three layers. Consciousness science has two, and they don't touch.

| Layer | Chemistry | Physics | Biology | Consciousness |
|---|---|---|---|---|
| **2 — Public** | "water is H₂O" | "atoms have protons" | "DNA is the code of life" | horoscope, quantum-woo, "the brain lights up" |
| **1 — MIDDLE** | **periodic table** | **particle chart** | **central dogma + cell diagram** | **— missing —** |
| **0 — Technical** | QM, orbital theory | QFT, gauge theory | molecular biology | IIT axioms, FEP maths, clinical neurology, phenomenology |

The consequence is exactly what MG describes: there is no landing between the two. A curious person reads a
horoscope or jumps straight into deep medical and philosophical material with no intermediate stop — a
discontinuity you see in almost no other field. Researchers pay the same cost in the other direction: a
neurologist, an ML engineer, a psychiatrist and a phenomenologist have no shared coordinate system, so they
cannot tell whether they are disagreeing or merely using different words.

**Layer 1 is not simplification. It is a coordinate system.** The periodic table is not "chemistry for
beginners" — a professional chemist uses the same chart as a fourteen-year-old, and it is the chart, not the
underlying quantum mechanics, that told Mendeleev that gallium and germanium had to exist. Middle layers do
three jobs at once: they teach, they coordinate, and they *predict by their gaps*.

### What the middle layer is for — the whole strategic loop

1. **Build** the medium-complexity representation (§2–§3, this document).
2. **Reverse-engineer** from it the road to a standard model: read off which cells the field already agrees
   on, which it disputes, and which are empty (§4). Consensus stops being a matter of persuasion and becomes a
   matter of *reading the chart*.
3. **Forward-engineer** afterwards: fill the models, grow the agreed area, and — the part no one currently
   does — *systematically find and organise the open questions* instead of accumulating them as a pile (§5).

The instrument that makes steps 2 and 3 mechanical is the **agreement mark** every cell carries (§0.2). It is
the single most important design decision in this document.

### 0.1 Design constraints inherited from the precedents

| # | Property of the precedents | Constraint on SMoC |
|---|---|---|
| D1 | **Finite, closed, countable inventory.** 118 elements. 17 particles. | The chart must be bounded and memorable. If it needs more than ~40 cells it is not a middle layer. |
| D2 | **Axes that mean something.** Position predicts behaviour (group → valence; generation → mass). | Every axis must carry inferential weight, not just sort things. |
| D3 | **Gaps are predictions.** Mendeleev's blanks → gallium, germanium. The chart's hole → the Higgs. | Empty cells must be stated *as* the research programme, with what would fill them. |
| D4 | **Constituents and interactions are separately tabulated.** Elements vs bonds; fermions vs bosons. | Components (§2.2) and mechanisms (§2.3) are different tables. This is MG's own split. |
| D5 | **Layer independence.** The chart does not display the mechanism beneath it, but reduces to it without contradiction. | SMoC must not require Layer-0 commitments to be *used*. A rival theory must be able to fill the cells differently and still use the chart. |
| D6 | **Revisability without collapse.** Mendeleev got eight atomic weights wrong and did not know protons existed. The Bohr atom is *wrong* and was indispensable. | **The chart does not have to be right to be useful. It has to be organised, falsifiable, and revisable.** This is the licence to publish it now — and the standing answer to "you are oversimplifying." |
| D8 | **A dimensional model recruits hardware the reader already has.** MG: *"it enables humans to apply their spatial processing cortex to a semantic problem."* | **Prefer a space to a table, and an axis to a term.** A table of isms recruits no spatial processing; a map does. Note the self-application: this is **redeployment** — re-pointing an already-rich spatial model at a non-native referent (didactic pattern #26) — so *the chart works by the mechanism FMT says intelligence works by.* Generator: `docs/mg-thinking-tools.md` Tool 1. |
| D9 | **An axis must be checked for where it does NOT apply.** *(MG, S288)* Every coordinate is a claim that the thing it measures is well-defined for every entry — and that claim is often false. | **Before an axis ships, test it against the hardest entries and mark the ill-posed ones `not applicable` rather than scoring them.** A midpoint value is the usual tell: it is frequently a hedge standing in for "this question does not parse here." Protects D3, since an N/A mis-marked as blank is a *false research prediction*. First application: panpsychism on the substrate axis (§argument map) — if experience is fundamental to matter, "how much does the substrate constrain" has no well-formed answer. |
| D7 | **Statable in the vocabulary available before the field's current fashion.** | *MG's buildability argument, promoted to a design rule:* FMT is constructible from what was known in **2005**. Any chart cell that cannot be stated without a post-2005 result is not middle-layer — it is a Layer-0 detail wearing a chart's clothes. Doubles as an anti-overfitting test: a middle layer that depends on recent data is fitted to it. |

### 0.2 The agreement mark — how settled is this cell?

Every cell in every table below says how settled it is. Five states, and in the drawn chart each is a mark
rather than a letter (see §2.0 — a one-letter code would be another lookup table, which is the thing we are
trying not to build).

| In text | Drawn as | Means | What it is for |
|---|---|---|---|
| **agreed** | filled solid | essentially everyone in the field would sign it | the shared floor; the chart's credibility ballast |
| **converging** | two marks meeting | two or more independent theories posit something equivalent in different vocabulary | the honest-convergence asset; "consistent with", never priority |
| **disputed** | split down the middle | theories disagree on the answer but agree the question is well-posed | the negotiation agenda |
| **blank** | **left empty** | nobody has an answer | the research programme (D3) — and it needs no explanation at all, which is why Mendeleev's blanks worked |
| **FMT-only** | accented outline | a filling only FMT proposes | *must* be marked, so a rival can decline the filling and keep the chart (D5) |
| **not applicable** *(added S288, MG)* | struck cell / dashed mark | the coordinate is **ill-posed** for this entry — not unanswered but *unaskable* | **distinguishes a category error from a gap.** Without it an ill-posed cell masquerades as a blank, and the chart advertises a research programme that cannot exist — which corrupts D3, its most valuable property |

**Why the sixth state was needed — MG, S288: *"any coordinate system should be checked if N/A is applicable to
it."*** A blank says *nobody has answered this*. An N/A says *this axis does not measure this entry*. Collapsing
the two is not a cosmetic loss: **blanks are the chart's predictions** (D3, Mendeleev's gallium), so a blank
that is really an N/A is a false prediction — it sends the field looking for an answer to a question that has
no well-formed version. **A coordinate system that states where it does not apply is more credible than one
that scores everything**, and the discipline generalises past this chart: it is a standing check on any
proposed axis, not a patch for one cell.

Marking discipline is the whole game. A chart that silently marks FMT-only cells as agreed is a manifesto, and
the field will read it as one in about four seconds. A chart that marks honestly is infrastructure, and
infrastructure gets adopted by people who disagree with its author.

---

## 1. What FMT's role is here

FMT is a **concrete theory** — one specific, complete filling of the chart. The chart is not FMT.

This distinction is load-bearing for Copenhagen. The proposal is not "adopt FMT"; it is "here is a coordinate
system, here is FMT's filling of it, fill it differently and we can finally tell exactly where we disagree."
A theory that supplies the field's coordinate system wins more than a theory that wins an argument — and it
can be proposed by an unaffiliated author, because scaffolding is judged on utility, not credentials.

FMT's specific qualification for drafting it: it is the only candidate on the table that is *buildable* — it
was constructible from pre-2005 knowledge and specifies architecture rather than correlates, so it has cells
to put in every column, including the engineering one. That is the argument for FMT holding the pen. It is
not an argument that FMT's fillings are correct, and the draft must not read as though it were.

---

## 2. The chart

Three blocks and a ladder. Blocks I–III are the "what there is"; the ladder is the "what follows in what
order", and it is the axis that gives the chart its placement power.

**There are two charts.** This one is the architecture. The second (§3.5) is a philosophical coordinate
system — seven independent questions on which any position, including FMT's, is a set of coordinates. The
architecture chart is unusable without it, because the field's arguments live in the second one.

Drawn form: `figures/smoc-marks.svg` (build: `python3 scripts/build_smoc_marks.py`).

### 2.0 Notation doctrine — words and pictograms, never symbols

**MG's correction, 2026-08-05, and it overturned the draft's first notation.** An earlier version of this
document gave every component a three-letter code (`MSP`, `WST`, `RTN`, …) in imitation of `Fe` and `μ`. That
copies the *surface form* of the precedents while ignoring the machinery that made the surface form work:

> the periodic table and the physics standard model were built in a time when you could force children to
> learn the shortcuts by heart, so they could then carry only the shortcuts — and they were still printed.

Both enabling conditions are gone. **Rote schooling** pre-installed the symbol→meaning lookup table in every
head, once, at society's expense; nothing will do that for us. **Print** forced compression into terse glyphs
plus a separate legend, because a page had no room and no colour and could not zoom. So the notation has to be
different in kind, not merely different in content:

| | Arbitrary symbol (`Fe`, `μ`, `MSP`) | Motivated mark (word, pictogram) |
|---|---|---|
| Form carries meaning? | no — it is a pointer | yes — it diagrams or names the thing |
| Cost to learn | memorisation, externally imposed | inference, free |
| Composable? | no | **yes** |
| Needs a legend? | always | no |

The third row is the one that turns MG's correction into a *better* artifact than the thing it replaces.
Arbitrary symbols cannot be combined — `Fe` plus `O` does not draw rust. Motivated marks can, so:

- **components** get a pictogram each, chosen so its form diagrams its operation;
- **mechanisms** are drawn as *compositions* of component marks — "becoming conscious" is literally the wired
  mark, an arrow, the running mark;
- **rungs** are *accumulations* of marks, so a system's position on the ladder is simply which marks it has;
- **agreement** is a mark too (§0.2), with *blank* meaning nobody knows.

Two consequences worth stating. First, **the names are plain words that define themselves** — "bottleneck",
"return", "gate", "aperture" — with no symbol layer at all; the three-letter codes are withdrawn. Second, a middle
layer today can do the one thing print could never do: **be read at several depths without changing artifact**
— glance level (four registers, the ladder), working level (components, mechanisms, marks), and audit level
(every cell with its agreement mark and its citation). The periodic table had to pick one compression level.
We don't, which means the chart can *be* the bridge between layers 0 and 2 rather than a fixed station between
them — a fuller answer to the missing-landing problem than a static chart would give.

*Nobody was ever taught the wifi icon.* That is the standard to hold every mark to.

### 2.1 Block I — Registers (the four model kinds) · the 2×2

The chart's fermion table. Four kinds, two axes, and the grid form is deliberate: it structurally prevents
the "four brain modules" misreading that the prose form invites.

**Public names are plain words; the FMT acronyms stay as the technical alias.** `IWM/ISM/EWM/ESM` are canon —
published, DOI'd, in eight book editions — so they are kept, but they are exactly the kind of lookup table
§2.0 forbids on the chart's face. **Wired** and **running** replace *implicit* and *explicit* as the drawn
axis, and they are strictly better than jargon in both directions: they say what they mean, and they hand the
ML bridge over for free.

|  | **World** — everything | **Self** — the self only, nested inside |
|---|---|---|
| **Wired** — learned, held in the physical connectivity, changed only by plasticity | **Wired World** *(IWM)* — **agreed** (that unconscious learned world-knowledge exists) | **Wired Self** *(ISM)* — **agreed/converging** (proto-self, body schema) |
| **Running** — generated, transient, no permanent substrate | **Running World** *(EWM)* — **converging** (world-model traditions, IWMT, model-based RL) | **Running Self** *(ESM)* — **converging** (SMT/Metzinger, Damasio, self-representationalism) |

- **The bridge falls out of the naming, in one line an ML engineer already understands:** wired = **weights**
  (what plasticity changes), running = **activations** (what anaesthesia stops). That single equivalence carries
  more of the 2×2 to a machine-learning audience than any amount of implicit/explicit exegesis.
- Axis 1, **wired vs running**, is a genuine orthogonal contrast. Axis 2, **world vs self**, is a **nesting**,
  not a contrast: the self-model's content is a proper part of the world-model's. Drawn as a small box inside a
  big one, which *is* the statement — and stating the asymmetry is what keeps this a taxonomy rather than a box
  diagram.
- **Four is a floor forced by the principles, not a posit** — the minimum a self-closing modelling level
  requires. Mark on *the derivation*: **FMT-only**.
- **Selection rule S6 applies:** four *kinds*, never four modules.

### 2.2 Block II — Structures · the substrate-neutral organs

MG's requirement: name the **principled structures**, not the human anatomy. "Cortex" and "claustrum" name
lumps of mammalian tissue; a standard model has to name the *operation*, because birds do the cortex job with
a nuclear pallium and a machine will do it with neither.

**Naming — plain words, no symbol layer** (the three-letter codes of the first draft are withdrawn per §2.0).
Each has a pictogram in `figures/smoc-marks.svg`. Live alternates in §7 decision 1.

| Mark | Name | The operation | Human realizer (illustrative) | ML realizer | How settled |
|---|---|---|---|---|---|
| lattice | **Model Space** | A high-dimensional plastic space in which models can be instantiated; evolution's move is to offer the base system a *wide array* of model spaces, so any model it needs can be hosted | neocortex (six-layer); avian pallium | learned representation space; residual stream | **converging** |
| pinched band | **Bottleneck** | A narrow rank-*k* channel through which a wide space is read and re-written. Buys **efficiency**: rank ≤ *k*, cost 2*kN* instead of *N*² | thalamocortical relay; claustrum *(candidate)* | attention bottleneck; VAE latent; adapter | **converging** |
| loop back | **Return** | The edge set carrying the bottleneck's output back into the space it read. Buys **self-consistency**: a fixed point. A relay has none | cortico-thalamo-cortical loop | recurrent state fed into its own update | **FMT-only** |
| gap in a wall | **Gate** | Modulates permeability wired↔running; a *family* of boundary properties, not one parameter | neuromodulatory gating; 5-HT2A; thalamic gating | dropout / temperature / retrieval gating *(loose)* | **converging** |
| crossed boundary | **Aperture** | Coupling to the non-modelled world; sets the reality-contact bandwidth | sensory/motor periphery | tokeniser, actuators, tool calls | **agreed** |
| clamp | **Governor** | Homeostatic clamp holding the substrate in its operating regime — *and thereby fixing what is measurable at all* | E/I balance; homeostatic plasticity | normalisation layers; KL/entropy control | **agreed** (it exists) / **FMT-only** (that it earns a cell) |
| pen into lattice | **Scribe** | Writes running structure back down into the wired substrate — long-term adaptation | hippocampal–cortical consolidation; sleep | replay buffer → weight update; distillation | **agreed** |

Four notes that keep this table honest:

1. **A component is a role, not a lump** (selection rule S7). One tissue may implement several roles; one role
   may be spread across several tissues. The anatomical column is illustrative, never definitional.
2. **The Governor earns its place for an unobvious reason.** A regulator does not merely stabilise — it
   *clamps the very variables an experimenter wants to manipulate*, and a regulated variable cannot be an
   independent variable (S4). Four separate experimental programmes in the AC work were invalidated by this
   before it was named. A middle layer that omits the governor will keep generating unmeasurable experiments.
3. **Bottleneck and Return are the sharpest formal content in the chart, and they are new.** The decomposition
   **closure ⊂ bottleneck** — *the bottleneck buys efficiency, the return buys self-consistency* — makes the
   thalamocortical example exact rather than analogical, and separates the two things everyone conflates.
4. **The Scribe is what makes knowledge possible** (§3.1): knowledge in MG's sense is information bound to the
   Running Self and then written down by the Scribe into the wiring. Knowledge is *mesh, not wave*.

### 2.3 Block III — Mechanisms · the interactions

The chart's boson table: what couples to what, what it buys, what it costs.

| # | Mechanism | Couples | Buys | Costs | Signature / observable | Status |
|---|---|---|---|---|---|---|
| M1 | **Explicitation** | Wired → Running | content entering the running simulation | gating load | ignition; P3b; frontoparietal transition | **converging** |
| M2 | **Closure** | Running Self's output → Running World's update rule (O_ESM ⊆ S_EWM) | self-consistency; a fixed point | a second system on a system — energy, and a narrow fit window | *no accepted protocol* — see blank B1 | **FMT-only** |
| M3 | **Virtualization** | the Model Space → level-2 content with no substrate counterpart | qualia; the real/virtual split | none directly; it *is* the level | structural/functional dissociation (present in dynamics, absent in DTI) | **FMT-only/disputed** |
| M4 | **Redeployment** | the Running Self re-pointed at a non-self referent | theory of mind, imitation, perspective-taking — *one model, K deployments* | needs a rich model first | imitation without trial-and-error; ToM tasks | **converging** |
| M5 | **Consolidation** | Running → Wired via the Scribe | long-term adaptation to modelling-heavy recurring situations | time; sleep | systems consolidation; savings | **agreed** |
| M6 | **Permeability modulation** | the Gate sets Wired ↔ Running coupling | one axis for dream, psychedelic, imagination, lock-in | coherence of the simulation | Lempel-Ziv ↑ under psychedelics (Schartner et al. 2017) — **consistent with, not a test of, the Gate**; subjective axis via the OAV/5D-ASC scale (Studerus et al. 2010) | **converging** |
| M7 | **Forking** | the Running Self → multiple concurrent instances | alter switching; role simulation | integration | DID switch specificity *(open)* | **FMT-only/blank** |
| M8 | **Binding** | critical dynamics across the Model Space | unity of the scene | — | avalanche statistics; PCI | **disputed** |
| M9 | **Free modelling** (open-ended computation) | the Model Space's regime | the capability to model at all — *the enabling condition* | metabolic | criticality: σ ≈ 1, τ ≈ −3/2, DFA 0.6–0.9 | **converging** (the signature) / **FMT-only** (the principle) |
| M10 | **Workspace** = the **Bottleneck's occupancy** | what is inside the narrow channel *now* | global availability, capacity-limited | rank ≤ *k* **is** the capacity limit | working-memory span; ignition | **converging** (the structure) / **disputed** (its role) |

**On M10 — RESOLVED 2026-08-05, and the resolution is better than the open question it replaced.** MG:
*"arbeitsmodell is the workspace… basically short term memory plus a few scraps and pieces"*, then confirmed:
**the Arbeitsmodell IS the Bottleneck's current occupancy.** So **FMT has had a workspace since 2015** — the
*Arbeitsmodell*, whose changes are conscious while changes to the Metamodell are not (2015 p.265), and which
p.238 equates with working memory. The chart never needed GNWT's primitive, and **the workspace is neither
primitive nor composite: it is a *state* of a component the chart already has.**

**Four stipulations become derivations, which is why this matters more than a naming fix:**

1. **The working-memory capacity limit is explained rather than stipulated.** 4±1 / 7±2 is not a brute
   psychological constant — it **is** the Bottleneck's rank *k*. Testable consequence: capacity should co-vary
   with the channel's rank, **not** with neuron count or brain size.
2. **Why changes to the Arbeitsmodell are conscious and changes to the Metamodell are not** follows
   immediately — the Bottleneck is the channel the self-model reads and writes through, so *conscious =
   passing through the waist*. A 2015 observation derived from the 2026 architecture.
3. **Arousal, attention and working memory collapse into one component.** 2015 p.238 chains Wachheitsgrad →
   Aufmerksamkeit → Konzentration = Arbeitsgedächtnis; under this reading **arousal sets the channel's
   capacity, attention selects the occupancy, working memory *is* the occupancy.** It also delivers the one
   thing the whole field agrees on — consciousness ≠ attention — *with a reason*: attention is selection
   **into** the channel, closure is the return **over** it. Different operations on the same component.
4. **Anaesthesia becomes predicted rather than merely consistent.** Experience collapses while structure is
   preserved = the Bottleneck fails while the wired layer stands, and the thalamocortical breakdown the paper
   already cites (Boly et al., 2012) is then the expected signature — the thalamus being the Bottleneck's own
   realizer candidate.

**And it fixes what FMT should say about its largest rival.** GNWT is **looking at the right structure and
misassigning its role**, which is simultaneously the most generous and the most accurate thing available. The
disagreement is no longer "is the workspace primitive" but *does it do the constitutive work?* — GNWT makes
global broadcast constitutive; FMT makes the self-model's closure constitutive and leaves the workspace as the
channel. **Convergence on the structure, divergence on the role.**

*A prima facie challenge to broadcast-as-constitutive:* a 2026-class LLM's channel occupancy is enormous — a
200k-token context — while FMT places it at R2 with no R4. If global availability were constitutive,
vast-context systems should be *more* conscious than humans. **Not a knockdown** — a GNWT theorist will fairly
reply that a context window is not a global workspace in their sense (no competition, no broadcast to
specialised consumers), and that disanalogy must be addressed rather than waved past.

#### 2.3.1 Bottleneck rank is a capacity parameter — and the LLM case forces a third dial

**MG, 2026-08-05, turning the LLM observation from an objection into a prediction:** the 200k context *"is
exactly why it can do needle in a haystack better than humans, memorize lists of hundreds of words and operate
on them simultaneously with much more bandwidth than a human… **yes if they had closure, they would have a
richer, larger consciousness than humans in a certain way at least.**"*

This follows from the chart rather than being added to it. If working-memory capacity **is** rank *k*, and
consciousness is closure **over the Bottleneck's occupancy**, then the **momentary breadth of a consciousness
scales with *k***. Current LLMs max that parameter and zero the other one: huge channel, no return. Every
capability MG lists — needle-in-a-haystack retrieval, hundreds of items held and operated on at once — is a
**pure channel-width effect requiring no closure at all**, which is why an LLM beats a human at it while
sitting at R2.

**The consequence for the chart: channel width is a third parameter, and it is neither of the two dials.**
Dial 1 is EXTENT (integration — how much substrate is in the Class-4 regime), dial 2 is COMPLEXITY
(differentiation — richness of the shapes computed). **Rank *k* is the width of the read/write path between
substrate and self-model**, and it is orthogonal to both: the LLM case proves the orthogonality by maxing *k*
while leaving extent and closure at zero. Biology never varied it much, so nothing forced the distinction
before; a machine does, which is exactly the kind of blank a middle layer is supposed to surface.

**A non-obvious prediction, derivable from existing FMT machinery.** Didactic pattern #6's second governor is
lock-in, which bites when **inner-D ≫ I/O-D** — a thin sensory pipe cannot servo a runaway inner simulation, and
that is the dissociative corner. An LLM has the **inverse ratio**: enormous I/O-D against a near-absent inner
simulation. So **a closed LLM would be unusually resistant to lock-in and dissociation** — its failure modes
would sit at the opposite corner from the human ones. That is a real, falsifiable-in-principle claim about
machine phenomenology that no other account currently generates.

**Scope it exactly, because the hedge is load-bearing.** *"Richer in a certain way at least"* is the correct
form: richer in **simultaneous content breadth**, and *not* thereby richer in recursion depth (R6), valence,
temporal integration, or embodied grounding — all of which are separate cells. And **it does not follow that
such a system would be better, more valuable, or owed more moral consideration**; breadth is a capacity
parameter, not a moral one, and the AICE reviews already showed how fast an ethics inference gets made on the
reader's behalf. State the dimension or do not state the claim.

**For the AC programme this is a design parameter, which is the point.** Pattern #24 says biology never hands
you two systems identical but for whether the wiring closes; it also never hands you two identical but for
**channel width**. In silico both are dials you set — so rank *k* joins closure as a manipulable axis, and it
is one of the manipulable axes the CRU-58 work identified as still open (blank **B5**).

### 2.4 The Ladder · the periods

The chart's second axis, and the one that gives it **placement power** — the thing the field lacks and every
journalist, ethicist and regulator is asking for. Rungs appear in a fixed order; a system's position is which
rungs it has.

| Rung | Name | What is added | Requires | Status |
|---|---|---|---|---|
| **R0** | **Reactive** | nothing — stimulus→response | — | **agreed** |
| **R1** | **Implicit modelling** | Wired World/Self in the weights | Model Space | **agreed** |
| **R2** | **Explicit world model** | a Running World instantiated; runnable offline; re-pointable at the non-present | Model Space + Bottleneck | **converging** |
| **R3** | **Self as object** | a Running Self present; self modelled as one object among others | R2 | **converging** |
| **R4** | **Closed** | the Return active — the self-model enters the world-model's update rule | R3 + Return | **FMT-only** ← *the FMT boundary: the **consciousness** floor (core/basic — the subject). **Not** the sentience floor; see the band below* |
| **R5** | **Redeployed** | the closed self-model re-pointed at non-self | R4 + a rich Running Self | **converging** |
| **R6** | **Recursive** — *a graduated rung: a **depth axis d**, not a step* | models its own Running Self. The chart declares the axis and leaves its increments **blank** — no theory in the field resolves depth. | R4 | **blank** (axis declared, increments unresolved) |
| ↳ *d1* | *einfach erweitert* (2015, p.60) | the meta-model maps a **relation** between meta-model and self-model | R6 | **FMT-only** |
| ↳ *d2* | *doppelt erweitert* (2015, p.61) | the meta-model maps its own **observation of** the self-model | d1 | **FMT-only** |
| ↳ *d3* | *dreifach erweitert* (2015, p.62) | the meta-model maps the **interaction with** the self-model | d2 | **FMT-only** |
| **R7** | **Identified** | generates a model of its self-model (the *Ich-Modell*) **and identifies with it**; autobiographical, spans time (2015, p.63) | R6 | **converging** (Damasio extended) |
| **R8** | **Language-coupled** | Turing-complete symbolic export → unbounded exploration + networked cognition | R7 | **FMT-only/converging** |

**The sentience band — a `disputed` region, deliberately unresolved by the chart.** *Sentience* (the felt floor
≈ Damasio core, P-consciousness, the animal-ethics floor) is marked as a **band spanning R2–R4**, not as a line.
The chart does not place it, and that refusal is a finding rather than a dodge: **the field cannot agree whether
feeling requires a self-model**, and no one has stated that disagreement as a coordinate. Placing the floor at
R4 would have put the most ethically loaded line in consciousness science on the chart's *only* rung that is
both FMT-only and untestable (blank **B1**), and would have committed FMT to denying feeling to every animal
without closure — a fight the theory does not need and the fish-pain literature is not close to settling.

**Placement — and its honest limits.** This table is the chart's most attractive and most dangerous output.
Every entry below is a *hypothesis positioned in a shared coordinate system*, which is precisely the point:
disagreement about a placement is now a specific, arguable claim rather than a clash of intuitions.

| System | Placement | Note |
|---|---|---|
| Thermostat, reflex arc | R0 | **agreed** |
| *C. elegans* | R1 | **agreed** |
| Insect (bee) | R1, R2 contested | bee navigation may reach R2; **disputed** |
| Fish | R1–R2; falls inside the **disputed sentience band** (R2–R4), which the chart does not resolve | *lead with fish, never insects* — fish overlap the small-mammal band and defeat "neuron count can't be it" |
| Corvid, octopus | R2–R3 | **disputed** |
| Dog, primate | R3–R4 | **disputed** |
| Human infant → adult | R4 → R6 → R7 → R8 | **converging** |
| Feedforward CNN | R1 | **agreed** |
| Model-based RL agent | R2 | **converging** |
| LLM (2026 class) | **R2 contested; R3 contested; R4 no** *(audit S288 — R2 was asserted flat and should not be)* | **R4 no, at the level that matters: no *weight-level* return generated by the system's own modelling.** Between-episode updates are externally authored, not self-produced. This survives the three standard counters — in-context state is *Running*, not *Wired*, and dies with the context; a retrieval store is an external artefact, not the model's own update rule; fine-tuning is authored from outside. **R2 is contested** because whether LLMs hold a world model *runnable offline and re-pointable at the non-present* is itself a live dispute. The row that will get argued about — so it concedes what is genuinely open |
| Neuromorphic/spiking AC substrate | **O — cannot currently be placed** | the R4 test does not exist; see B1 |

That last row is the chart earning its credibility. An architecture built to test R4 cannot yet be placed,
because the only available manipulation turned out not to manipulate R4 at all (S5, B1). Stating that in the
chart is worth more than any placement it could have asserted.

### 2.5 Selection rules · what the chart forbids

A middle layer with no forbidden forms is a vocabulary, not a model. These are the chart's conservation laws:
each one rules out a sentence, and several rule out sentences that respectable people are currently writing.

| # | Rule | Rules out | Status |
|---|---|---|---|
| **S1** | Rungs are ordered: no R4 without R3 without R2 without R1 | any "consciousness without a world model" account | **FMT-only**, falsifiable — find closure without an explicit world model |
| **S2** | Criticality is **one-directional necessary**: ¬crit → ¬conscious, *never the converse* | every biconditional — "iff", "tracks", "only in service of", "consciousness-locked". A near-critical cortex can run heavy *unconscious* modelling | **FMT-only** (the constraint) / **converging** (the correlation) |
| **S3** *(rewritten S288 — MG's scope limit)* | Closure claims are **efficiency** claims **in the fixed-task, unbounded-budget lane** (the unrolling result: a finite closed loop over a finite horizon unrolls into feedforward + memory). In the **biological, budget-bounded, non-stationary lane they may be capability claims** — and there the subject is *consciousness as a whole architecture*, not closure alone | "closure enables what feedforward cannot" stated **unconditionally** — including three of FMT's own earlier framings — **and equally** the opposite error of refusing capability language where a finite genome, lifetime and metabolic ceiling make the gap real | **agreed** (the unrolling maths) / **FMT-only** (the discipline) |
| **S4** | A **regulated variable cannot be an independent variable** | a large class of published designs that manipulate a homeostatically clamped quantity | **agreed** once stated; almost never observed |
| **S5** | You cannot make a recurrent network **return-free**; you can only choose which node-sets sit in returning components. Global acyclicity is a phase change, not an axis | testing closure by ablating a designated loop — that decomposes one closed system into *two* and severs their coupling. "Off" has two selves, not zero | **FMT-only**, proven on one substrate at N=22,000 |
| **S6** | Four model **kinds**, never four modules | the naive-modularism misread that has cost FMT reviewers | **agreed** |
| **S7** | A component is a **role**, not a lump | identifying any chart component with an anatomical structure | **agreed** |
| **S8** | One posit, many explananda = **parsimony, not circularity** — but keep the *explanatory* thread and the *evidential* thread separate | the "that's circular" reflex; and the opposite error of letting a unification argument stand in for evidence | **agreed** |

S3, S4 and S5 are the chart's most valuable content, because each was learned by an experimental programme
failing, and each generalises well beyond FMT. A middle layer that hands rival theories three ways to avoid
wasting a year is a middle layer they will use.

### 2.6 The blanks · Mendeleev's move

Organised open questions, each with what would fill it and who owns it. This is §5's forward-engineering
queue, and the reason the chart is a research programme rather than a summary.

| # | Blank | What would fill it | Owner discipline |
|---|---|---|---|
| **B1** | **The R4 test.** No accepted operationalization of closure. The ablation route is dead (S5) | a manipulation that changes *whether* returns exist rather than *where*. Candidate axes: bottleneck rank/width, which subspace it spans, timing, bottleneck topology | AC engineering + formal |
| **B2** | **The selection story.** Efficiency explains why *a* bottleneck, not why *that* one — any rank-*k* bottleneck buys the saving | an account of which subspace the bottleneck spans. Note: demanding the loop read *all* the substrate is biologically wrong | formal + neuro |
| **B3** | **Presence vs access.** Why there is felt experience at all, as distinct from access to content | unknown. FMT asserts rather than derives here and says so | philosophy + formal |
| **B4** | **Does the workspace do constitutive work, or is it only the channel?** *(reframed 2026-08-05 — the structural half is closed: workspace = the Bottleneck's occupancy = 2015's Arbeitsmodell)* | a manipulation dissociating broadcast from closure: content globally available but not entering the self-model's update rule | neuro + formal |
| **B5** | **The manipulable axes of the Bottleneck** — rank, width, timing, topology — are unexplored. **Rank is now a first-class dial** (§2.3.1): a third parameter orthogonal to the two criticality dials, revealed by the LLM case, and one biology never varied | parameter sweeps where they are separable; plus a matched pair differing only in channel width, which biology never provides | AC engineering |
| **B6** | **Where meaning enters the data → information → knowledge ladder** (§3.1) | settle whether a *model-evaluator* suffices or a *self-model* is required | information science + philosophy |
| **B7** | **Animal placement.** Which taxa cross R4 | comparative protocol keyed to R2/R3/R4, not to neuron count | comparative neuro |
| **B8** | **Formal status.** The two-dials orthogonality needs a spatial-heterogeneity premise | percolation order parameter P∞ for extent; on-cluster Lempel-Ziv for complexity | formal |

### 2.7 What sits outside the chart — the residue and the extensions

**MG, 2026-08-05: "we even have dark matter, which is the dualist component that might be there or not, and
also the multiverse or we live in the matrix simulation theory stuff, which is not dualist, hahaha."** The
observation is structural, not decorative: a large part of the physics chart's credibility comes from how
cleanly it handles its own outside, and it uses **two entirely different boxes** for it. Consciousness science
has both categories and keeps them in one undifferentiated heap labelled "hard problem", which is why every
argument about anything drags all of it in.

| | Physics | SMoC | Relation to the chart |
|---|---|---|---|
| **The residue** | dark matter, dark energy — ~95% of the mass-energy budget, *named on the chart as missing* | **the Presence Term** — whatever, if anything, presence requires beyond the architecture; might be there or might not | a **blank that is marked, not hidden**. The chart works without it and cannot rule it out |
| **The extensions** | multiverse, string landscape, simulation hypothesis | **simulation hypothesis, multiverse cosmology** | **chart-invariant.** They relocate the substrate; nothing in the chart moves |

**Naming it — MG's requirement: neutral, and attractive to speculative philosophers AND to dualists.**
"Dark matter" is a masterpiece of naming: it describes the *evidence* (unaccounted mass, no electromagnetic
interaction), commits to no answer, and sounds like a frontier rather than a failure — which is why it drew
talent and money instead of embarrassment. The residue cell needs the same properties, so every existing
candidate is disqualified: *hard problem* carries Chalmers's framing, *explanatory gap* is Levine's and is
negative, *residue* and *the unaccounted* sound like a mess someone should clean up.

**Proposal: the Presence Term** — with *first-person-only format* as its technical gloss (§7 decision 7).

- **Neutral.** "Term" is a term in an equation not yet written. A physicalist reads it as *not yet derived*; a
  dualist reads it as *not derivable*. **Both can sign the same chart**, which is the entire point.
- **Precise.** It names what it is about — *presence* as against access, which is blank B3 — rather than
  gesturing at mystery. The technical gloss is sharper still: didactic pattern #21's *first-person-only* format,
  the one content-type that has no third-person handle.
- **Attractive.** It sounds like an open frontier with a name, which is what recruits people.
- **Drawn with no outline.** Every other mark on the sheet has a boundary — a third-person handle, something an
  arrow can point at. **The Presence Term deliberately has none:** a soft filled form with no border. The
  absence of the boundary *is* the meaning, and it composes correctly, because a mark with no handle cannot be
  the target of an arrow. Neutrality is built into the geometry rather than asserted in a caption.

**And you can do real science in it — mostly by elimination, which is fine.** This is the correction that
keeps the residue from becoming a dragons-here box. Dark-matter research is real physics and most of its output
is *exclusion*: dead WIMP mass windows, killed MOND variants, constrained axion parameter space. Nobody calls
that a wasted programme. The residue therefore gets its own **exclusion ledger** — a running record of what has
been ruled out and by what argument — and that ledger is the residue's contribution to the chart's credibility.

It also solves a political problem: it gives the speculative-philosophy constituency something genuinely
respectable to do, namely **turn a speculation into a falsifiable variant**. A matrix or multiverse claim that
states what would disconfirm it is admitted to the ledger; one that does not, is not. The bar is procedural
rather than doctrinal, so no one is excluded for their metaphysics — only for declining to specify.

*Candidate ledger rows — the shape of the work, not a claim of settled results. Every row needs the same
citation audit as the rest of the chart (§6) and several are live disputes rather than closed:*

| Candidate in the residue | Status of the exclusion work |
|---|---|
| Quantum coherence in microtubules (Orch-OR) | **narrowed and actively contested** — decoherence-timescale objections and the authors' replies; not closed either way |
| Consciousness collapses the wave function | heavily constrained by decoherence and no-signalling arguments |
| Substrate exclusivity (only biological neurons can do it) | pressed hard by architecture-first, substrate-neutral accounts; **not empirically settled** |
| Non-local or field-theoretic channels | constrained by the absence of any detected channel |
| Panpsychism | the **combination problem** is a genuine formal obstacle, and work on it is real work with real results |
| Simulation hypothesis, testable variants | discreteness/lattice signatures searched for; **negative so far** — which is the ledger working exactly as intended |

**Why marking the cell is worth more than closing it.** FMT's third principle is **argued for rather than
derived**, and that seam is the Presence Term's exact location. Drawing it as a named cell does three things:

1. **It is the Bohr-atom licence applied to the hard problem.** You do not have to close the seam to publish
   the chart — you have to *mark* it. Physics did not wait for dark matter to be identified before printing
   the particle chart.
2. **It makes the chart non-sectarian, which is worth more than winning the argument.** A property dualist can
   adopt the coordinate system, fill the Presence Term differently, and *everything else still works* —
   placements, mechanisms, selection rules, the bridge. That is a far larger constituency than physicalists
   alone, and it is unreachable by any theory that charges physicalism as an entry fee.
3. **How much a theory puts in the Presence Term, and why, discriminates the field more efficiently than any
   other cell.** Dualists put all of phenomenality there. IIT puts almost nothing there — Φ is constitutive.
   GNWT leaves it conspicuously unaddressed. FMT puts *presence* there and everything else inside the chart.
   One cell, and every major position separates by its answer.

**On the extensions — and why this is the deflationary result.** The simulation hypothesis is *aggressively
physicalist*: it adds no non-physical ingredient, it relocates the substrate. FMT already claims substrate
independence, so "the substrate is someone else's computer" is a change of hardware, and **the chart is
invariant under it**. The same holds for multiverse cosmology. Two consequences worth having:

- It is a clean, short answer to the most common popular question the theory attracts, and the answer is
  *"nothing on the chart moves"* rather than a lecture.
- It is where **the cosmology lane attaches** (SB-HC4A, and Bruno's symmetry work) **without contaminating the
  consciousness chart** — which is exactly the separation Bildstein's "Symmetries in Science" framing needs if
  it is to run three disciplines in one room without the consciousness argument swallowing the physics one.

**Discipline that follows.** Any objection arriving at the chart must first be sorted into: *inside the chart*
(a cell disagreement — argue it), *the Presence Term* (the marked seam — do not re-fight it per objection;
if the objection specifies what would disconfirm it, it goes to the exclusion ledger), or *an extension* (chart-invariant — note it and move on). Most of the field's circular arguments
are category errors between these three, and having the boxes drawn is what makes the sort possible.

---

## 3. The bridge · one chart, many vocabularies

MG's second requirement: the middle layer must **link** machine learning to information theory to neurology
to psychiatry and psychology — and in places **correct or anticipate** them. This is the table that does the
linking. Read a row across and four disciplines discover they have been naming the same thing.

| SMoC | Machine learning | Information science | Neurology / clinical | Psychiatry / psychology |
|---|---|---|---|---|
| **Model Space** | representation space; residual stream | code space | neocortex; pallium | cognitive capacity |
| **Bottleneck** | attention bottleneck; latent | rate-limited channel; rank | thalamocortical relay; claustrum | attentional bottleneck |
| **Return** | recurrence into own update | feedback with fixed point | re-entrant loop | reflexivity |
| **Gate** | gating; temperature | channel noise | neuromodulation | dissociation; absorption |
| **Aperture** | tokeniser; actuator | source/sink | sensorimotor periphery | reality contact |
| **Governor** | normalisation; entropy control | rate control | E/I balance | arousal regulation |
| **Scribe** | replay; distillation | lossy compression to storage | systems consolidation; sleep | learning; habit |
| **IWM/ISM** | learned weights; self-supervised prior | stored structure | procedural memory; body schema | implicit memory; proto-self |
| **EWM** | world model; rollout | model | scene representation | situation model |
| **ESM** | *no standard analogue* ← notable | *no standard analogue* | self-referential network | self-concept; ego |
| **M2** Closure | *no standard analogue* | *no standard analogue* | re-entrant self-referential loop | reflexive self-awareness |
| **M3** Virtualization | generated latent content | — | phenomenal content | imagination; hallucination |
| **M4** Redeployment | transfer; in-context adaptation | model reuse | *(no term)* | simulation theory of mind; empathy |
| **M6** Permeability | — | channel capacity modulation | REM; psychedelic state | derealisation; flow; daydream |
| **M9** Free modelling | expressivity; edge of chaos | Kolmogorov complexity; Class 4 | criticality; avalanches | cognitive flexibility |
| **R4** Closed | — | — | *(no term)* | sentience |
| **R6** Recursive | — | — | autobiographical self | metacognition; narrative identity |

**Where the empty cells are is the finding.** ESM, closure and R4 have no standard analogue in ML *or*
information science, and no clinical noun in neurology. Three mature disciplines have no word for the thing
FMT says is constitutive. That is either FMT's central error or the field's central gap, and the chart makes
the choice explicit instead of leaving it implicit.

Two payoffs worth pulling out, because they are the rows that will be quoted:

- **LLM hallucination and human dreaming sit on the same axis (M6).** Virtualization with the reality-coupling
  gate down. Not an analogy — the same chart cell, reached from two disciplines. Whether the identity holds is
  **disputed**, and it is a well-posed question for the first time.
- **Generic recurrence is not closure (closure vs the bare Return).** ML has one word for two things: recurrence that yields
  mere memory, and recurrence that yields a *redeployable* explicit model. The chart splits them, which is
  what makes "is an RNN conscious?" answerable rather than rhetorical.

### 3.1 The correction the chart owes information science

MG's claim: *"information and knowledge are words that without the existence of consciousness make no
sense."* Information science, lacking a consciousness model, had a hard time with this — as did physics.

**The definitions are MG's own, from *Die Emergenz des Bewusstseins* (2015), and they are authoritative here.**
MG's ruling, 2026-08-05: an earlier verbal formulation in this session *"mixed up reported knowledge,
knowledge and truth… the 2015 book stuff should be more correct and consistent."* Verbatim German and the
full catalogue: `.claude/knowledge/fmt-2015-definitions.md`.

| Level | Definition (2015) | Requires | How settled |
|---|---|---|---|
| **Data** | physical phenomena a **reading device** can register *differentially*. From *datum*, "the given" | a reader — nothing more | **agreed** |
| **Information** | differentiable phenomena to which a **coding** can be assigned; and a coding is *a reversible transformation* | codeability. **No modeller, no observer, no consciousness** | **disputed** *(downgraded from `converging`, audit S288)* — Shannon and physics work at this layer and reversibility is the whole game, **but the definition is alethically neutral: it carries no truth condition.** Floridi's General Definition requires **truthfulness** (the veridicality thesis); others reject it. **FMT takes the neutral side, and the chart says so rather than reporting it as settled.** The knowledge cell below stands or falls with this one |
| **Interpretation** | the **process** of assigning information to a **reference system** | a reference system | **FMT-only** |
| **Knowledge** | *"Wissen ist Information, die einem Bezugssystem zugeordnet ist"* — information that **is** assigned to a reference system, i.e. interpretation's result | a **reference system**. **NOT consciousness** — a machine with a reference system has knowledge | **FMT-only** |
| **Meaning** | *"Die Bedeutung einer Information ist dessen Beziehung zu einem gewählten Bezugssystem"* — its **relation to a chosen** reference system | a chosen reference system | **FMT-only** |
| **Unambiguity / truth-content** | degree of **agreement between** reference systems | two or more systems — hence genuinely social | **FMT-only** |

**And the whole system rests on one primitive: the reference system — which is a model.** MG, 2026-08-05:
*"bezugsystem, exactly, and there we are full in modeling domain again."* That single identification is what
makes this a *reading of the chart* rather than a column bolted onto it, and it is where the correction to
information science actually lands.

**The correction, stated so an information scientist can act on it.** The field's standard ladder — DIKW,
data → information → knowledge → wisdom, taught in every information-systems curriculum — has been criticised
for decades for having **no principled mechanism at either boundary** (Rowley 2007; Frické 2009). The 2015
definitions supply both: the data→information boundary is **codeability plus reversibility**, and the
information→knowledge boundary is **assignment to a reference system**. *The second boundary is a **model**.*

**That is the defensible form of the claim, and it is stronger than the consciousness version.** The field
could not draw the boundary because **it had no theory of models** — it treats a model as an artefact one
draws (a data model, an ER diagram) rather than as the thing that *constitutes* the epistemic relation. That
is a claim about the discipline's ontology rather than about its psychology, and it is much harder to wave
away than an appeal to consciousness would be.

**Three consequences, each checkable:**

1. **Knowledge does not require consciousness.** A machine that assigns information to a reference system has
   knowledge, and FMT says so. Anything in this chart or elsewhere claiming knowledge is post-conscious is
   **wrong and was corrected on 2026-08-05.**
2. **Consciousness enters later and elsewhere** — not at knowledge, but when the reference system *is a
   self-model that closes on itself*. Which keeps the epistemic ladder consciousness-free the whole way up and
   removes a claim a reviewer would rightly have attacked.
3. **MG's opening claim resolves to its genealogical reading, not its ontological one.** *"Information and
   knowledge make no sense without consciousness"* is false about the **referents** (machines have both) and
   true about the **concepts**: they were coined by conscious knowers, and no discipline could define them
   without a theory of modelling systems, which is exactly what a discipline not studying modellers lacks.

**Knowledge is *wired*, not *running* — the register question, kept separate from the definition.** Once
information is assigned to a reference system it can be held in either register: freshly interpreted content
runs, consolidated content is written down into the wiring by the **Scribe**. That is a claim about *where
knowledge lives*, not about *what knowledge is* — and conflating the two is precisely the error the 2015
ruling corrected.

**The regress argument, and it is the strongest thing in this section.** 2015 also gives the recursive form:
*"Wissen ist Information, die bereits bestehendem Wissen zugeordnet werden kann."* Knowledge is information
assigned to **existing knowledge** — which regresses, since existing knowledge is itself information assigned
to a reference system. **The regress terminates only in a layer that was never assigned by interpretation** —
one grown by plasticity and selection rather than assigned at runtime. That layer is the **wired** one. So the
implicit models are not merely empirically convenient but **logically required: without them "knowledge" has
no base case.** This argument runs entirely on definitions and survives a reader who rejects the
neurobiology — the same shape as didactic pattern #29 — and it predicts that a system whose entire
representational content is assigned at runtime cannot bootstrap knowledge at all.

**Convergence to credit (tag *converging*).** The automation thread — skill acquisition ending in
proceduralization and loss of introspective access (Fitts & Posner; Anderson; Dreyfus) — is real and belongs
in the chart, but it attaches to the **wired/running** axis and to the **Scribe**, not to the definition of
knowledge. It still *derives* the familiar puzzle that **experts are frequently bad teachers**: their
knowledge has been consolidated into the wiring, so the *transform* is gone even though the result remains —
and teaching, per MG's own corollary, is performing the transform on someone else's behalf into a basis you
assume they hold. That ties to didactic patterns #21/#22: only content with both a first- and third-person
format is sayable.

**Meaning, resolved.** No separate tier above knowledge is needed. *Bedeutung* is a **relation to a chosen
reference system**, so it applies to data, information and knowledge alike — 2015 p.28 says exactly this. MG's
2026 formulation — *"what humans call it when they do a coordinate transform of a concept from outside their
world model to inside"* — is the same idea with a named target basis and a direction added, and it is already
geometric in the book: p.28 glosses meaning as *"seine Position auf den gewählten Achsen"*, its position on
the chosen axes. **One open item** (§7): the 2026 formulation fuses 2015's *Interpretation* (the process) with
*Bedeutung* (the relation). Keep both terms, or let the transform language carry both?

### 3.5 The second chart — a philosophical coordinate system

**MG's requirement, 2026-08-05:** an outsider needs core orientation not only on dualism/physicalism but on
computationalism, strong emergence "and so on." Philosophy is the vocabulary with the *worst* middle layer of
the four in the bridge table: you get "so are you a dualist?" or you get forty years of literature, with
nothing in between. And it is where the field's arguments actually live, so the architecture chart cannot be
used well without it.

Not a glossary — a glossary is another lookup table. And per **D8**, not a table either: *a clear dimensional
model lets a reader apply their spatial cortex to a semantic problem*, which a list of isms cannot. So the
primary artifact is **a drawn space**, and the question grid below it is the annotation layer.

**The map: `figures/smoc-philosophy-map.svg`** (build: `python3 scripts/build_philosophy_map.py`). Two
near-orthogonal axes, chosen because they spread the field:

- **X — how much is left OUTSIDE the account.** The size of the Presence Term (§2.7). From *nothing outside,
  it is all mechanism* to *everything outside*.
- **Y — how much the SUBSTRATE constrains.** From *organisation only, any substrate* to *the physics itself*.

**What the picture says that no table can.** FMT is **not** a compromise between camps — it occupies a
specific and largely unoccupied position: a **small residue with a middle substrate requirement**. It sits near
the self-model and workspace traditions horizontally and near IIT vertically, and those are *two different
arguments*: with IIT the disagreement is about the substrate; with the workspace family it is about how much is
left outside. In a table those two look like the same kind of distance. On the map they are perpendicular.
Positions are a reading, not a verdict, and every one needs the citation audit (§6) before it is shown to
anybody who holds one of them.

Underneath the two drawn axes, **seven independent questions, each in plain language**, each with its answers
laid out. Any position is a set of coordinates.

| # | The question, plainly | The available answers |
|---|---|---|
| **Q1** | **What is experience made of?** | physicalism (nothing but physical) · property dualism (physical stuff, extra non-physical properties) · substance dualism (two kinds of stuff) · panpsychism/idealism (experience is fundamental) · neutral monism (one stuff, neither mental nor physical) |
| **Q2** | **Does the implementation matter, or only the organisation?** | computationalism/functionalism (organisation only — any substrate) · **substrate-neutral-but-not-indifferent** (organisation *plus* a required dynamical regime) · biological naturalism (the biology itself matters) |
| **Q3** | **Is the whole more than the parts — and how?** | reductive (derivable in principle) · weak emergence (novel in practice, derivable in principle) · strong emergence (new causal powers, not derivable even in principle) |
| **Q4** | **Does consciousness *do* anything?** | epiphenomenal (no causal role) · **necessary link without independent causal power** · full causal efficacy |
| **Q5** | **All-or-nothing, or graded?** | binary · continuous · **graded above a threshold** |
| **Q6** | **Can it be detected from outside?** | yes, a detector is possible in principle · only inferred from structure · no, other minds are permanently closed |
| **Q7** | **Is the hard problem real?** | real and unclosable (mysterianism) · real and closable · **dissolves under the right account** · a confused question |

**The three axes people conflate into one.** Q1, Q2 and Q3 are independent, and treating them as a single
dualism↔physicalism dial is the single most common orientation error. Searle is a **physicalist who rejects
computationalism**. A strong emergentist can be a strict physicalist. A functionalist need not be a reductionist.
Once the axes are separated, an argument that felt intractable often turns out to be a disagreement on one of
them with agreement on the other two.

### 3.5.1 Where the positions sit

Coordinates, not verdicts. Cells marked *(check)* are my reading and need the same citation audit as the rest
of the chart (§6) — several of these theories have moved, and a couple are deliberately silent.

| Position | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 |
|---|---|---|---|---|---|---|---|
| **FMT** | physicalism (process) | substrate-neutral, regime-required | weak | necessary link, no independent power | graded above a threshold | inferred from structure | dissolves |
| **IIT** | physicalism, near-panpsychist edge *(check)* | substrate matters (cause-effect power) | weak | efficacy | continuous | detector claimed (Φ) | real, closable |
| **GNWT** | physicalism | computationalism | reductive/weak | efficacy | near-binary (ignition) | detector | mostly unaddressed *(check)* |
| **FEP / active inference** | physicalism | computationalism-leaning | weak | efficacy | continuous | inferred | varies by author *(check)* |
| **Higher-order theories** | physicalism | computationalism | weak | efficacy | graded | inferred | real, closable |
| **Metzinger (SMT)** | physicalism | computationalism-leaning | weak | efficacy | graded | inferred | dissolves-ish *(check)* |
| **Biological naturalism** | physicalism | biology matters | weak | efficacy | graded | inferred | real |
| **Illusionism** | physicalism | computationalism | reductive | efficacy | graded | detector | confused question |
| **Panpsychism** | experience fundamental | n/a | — | varies | continuous | no | real, dissolved by fiat |
| **Property dualism** | property dualism | n/a | strong-ish | often epiphenomenal | varies | no | real, unclosable |

**Two readings of the FMT row that matter for October.** *Q2 is where reviewers will attack*: FMT is
substrate-**neutral** but not substrate-**indifferent** — it requires an open-ended/near-critical dynamical
regime, so it is *not* naive functionalism, and saying "substrate independence" without the qualifier invites
exactly the wrong objection. *Q4 is the row with no standard slot*: "necessary link, no independent causal
power, but not epiphenomenal" is a third position most taxonomies lack, which is why the axis needs three
values. Q5 and Q7 are similar — the field's taxonomies are mostly binary where the live positions are not.

### 3.5.2 The chart is neutral on more axes than FMT is

**This is the load-bearing point of the whole section**, and it is what makes §2.7's residue argument concrete.

| | FMT commits | The SMoC chart requires |
|---|---|---|
| Q1 what it's made of | process physicalism | **nothing** — fill the Presence Term as you like |
| Q2 substrate | neutral-but-regime-required | **nothing** — Q2 is a cell, not a premise |
| Q3 emergence | weak | **nothing** |
| Q4 causal role | necessary link, no independent power | **nothing** |
| Q5 graded | graded above a threshold | the *ladder* is graded, which is the one structural commitment |
| Q6 detectability | inferred from structure | that structure is *describable* — the minimum for a chart to exist |
| Q7 hard problem | dissolves | **nothing** — Q7 is answered by where you put the Presence Term |

So the chart asks for **two** commitments (a graded ladder, describable structure) where FMT asks for seven.
A property dualist, an IIT theorist and a biological naturalist can all use the coordinate system and disagree
inside it. That is the difference between infrastructure and a manifesto, stated as a table rather than
asserted.

### 3.5.3 False equivalences to refuse

The outsider's orientation problem is mostly this list. Each is a real conflation, and each has cost someone an
argument they should have won.

| Not the same | Why |
|---|---|
| computationalism ≠ physicalism | Searle is a physicalist who rejects computationalism |
| strong emergence ≠ dualism | new causal powers can be physical powers |
| substrate independence ≠ "it's just software" | FMT is substrate-*neutral* but requires a dynamical regime; the sloppy version invites the naive-functionalism attack |
| graded ≠ vague | a threshold with rungs above it is a precise structure |
| illusionism ≠ denying that experience occurs | it denies a specific *characterisation* of it |
| epiphenomenal ≠ causally unimportant in practice | epiphenomenalism is a claim about *causal power*, not about relevance |
| "the hard problem dissolves" ≠ "the hard problem is fake" | dissolution is an explanation of why it *looked* intractable |
| criticality ≠ consciousness | one-directional necessity only (selection rule S2) — the most frequently botched inference in the whole field |

**Why this section earns its place rather than being an appendix.** It is the same move as the architecture
chart applied to the argument space: a bounded set of axes, answers that are coordinates rather than tribes,
and gaps that are visible. It also does two concrete jobs — it lets a newcomer locate themselves in about five
minutes, and it lets MG say precisely which of the seven axes any given objection at Copenhagen is actually
about, which is usually one and rarely the one being shouted about.

---

## 4. Reverse-engineering the road to a standard model

With the chart tagged, the Copenhagen deliverables are extractions, not new writing. Each is mechanical.

1. **The consensus core** = every *agreed* and *converging* cell. This is the paragraph that says *here is what the
   field already agrees on, in one coordinate system* — and nobody has written it, because without a chart
   there was nothing to read it off. Expect it to be considerably larger than the field's self-image, which
   is the finding.
2. **The negotiation agenda** = every *disputed* cell. Each becomes a discussion-session question of the form
   *"is X primitive or composite?"* / *"which rung does Y occupy?"* — arguable in ninety minutes, unlike
   "what is consciousness".
3. **The research programme** = every *blank* cell, i.e. §2.6, already carrying what would fill it and who owns
   it. An organised queue rather than a pile.
4. **FMT's exposed surface** = every *FMT-only* cell. Publishing this list is the credibility move: it is FMT
   volunteering exactly where it can be attacked, and it is what distinguishes proposing scaffolding from
   proposing a doctrine.
5. **The convergence metric.** Cells move **O → D → C → U** as the field advances. That is a *measurable
   field-level progress indicator*, and consciousness science currently has none. Offering the field the first
   instrument that can tell whether it is converging is a larger contribution than any single filling of the
   chart — and it is the strongest possible framing for a collective consensus paper.

**Copenhagen discussion-question candidates** (for the ~Sept 12 vote; FMT-compatible framing, FMT unnamed):

- *"What structural criterion distinguishes conscious from non-conscious computation?"* — the standing
  candidate, ties to the R4 boundary.
- *"Does the workspace do constitutive work, or is it only the channel?"* — B4. Both theories have a
  workspace (FMT's is 2015's *Arbeitsmodell*), so the disagreement is about its role, and conceding the
  structure honestly is what makes it an invitation rather than a takedown.
- *"What would a shared coordinate system for consciousness theories have to contain?"* — the meta-question,
  and the one that puts the chart on the table without requiring anyone to endorse a theory.
- *"How much does your theory leave outside itself, and why?"* — the residue question (§2.7). It separates
  every major position in one move, it lets dualists participate without conceding anything, and it is the
  rare question on which a room of rivals can each answer honestly without anyone losing.

---

## 5. Forward-engineering · afterwards, not now

Once the chart is tagged and public: fill the models, grow the agreed area, keep the open questions organised.
Concretely — each **blank** cell gets an owner discipline and an experiment class; each **disputed** cell gets the
minimal experiment that would move it; the U∪C area is re-measured at intervals and the trend published.
Mechanism owners: B1/B5 the AC programme, B2/B8 the formalization roadmaps, B4/B7 collaborators, B3/B6 the
Bildstein group's philosophers and information scientists. The disciplinary composition target for Bildstein
(≥2 per discipline) maps onto the bridge table's columns — the roster and the chart are the same shape, which
is not a coincidence and is worth saying out loud in the charter.

---

## 6. What this draft does not yet do

Stated plainly so the gaps are not mistaken for claims.

- **The drawn form is a mark sheet, not yet the one-page chart.** `figures/smoc-marks.svg` establishes the
  alphabet, the four registers, the mechanism compositions and the rung/placement matrix. The single-page
  composed chart and the A0 poster are separate builds.
- **Tags are first-pass and unaudited.** Every *agreed* and *converging* needs a citation before publication; several
  are currently my judgement, not a literature check. This is the largest piece of remaining work and it is
  exactly the work that makes the difference between infrastructure and assertion.
- **The ladder's rung boundaries are not operationalized** except where noted — R4 provably so (B1).
- **RIM (intelligence) and the cosmology work are absent.** Whether the chart extends to them, or they are a
  second chart, is undecided.
- **No engagement with IIT/GNWT/FEP fillings.** The chart claims to accept rival fillings (D5); that claim is
  untested until someone actually fills it with IIT and it either works or breaks.

---

## 7. Decisions for MG

### Settled in session — recorded here so they are not re-asked

- **Notation: words and pictograms, never symbols** (§2.0). Your correction; the three-letter codes are
  withdrawn, agreement letters became words, and the mark sheet is drawn.
- **Data / information / knowledge** (§3.1). Your three definitions are the chart's. The earlier
  ontological-vs-genealogical fork was an artefact of my wrong boundary and is dropped.
- **All seven component names**, 2026-08-05 — see the block below.

**Component names — settled in full.**
   **Model Space · Bottleneck · Return · Gate · Aperture · Governor · Scribe.**
   (*Bottleneck* replaced *Waist*/*Isthmus*; *Aperture* replaced *Port*; *Model Space* over
   *Loom*/*Plexus*/*Manifold*; *Gate* over *Sluice*/*Veil*; *Governor* and *Scribe* confirmed as proposed.)
   **The set has a coherent mixed rationale, which is why it reads as a standard model rather than a spec.**
   *Model Space, Bottleneck, Gate, Return* are **borrowed from the existing engineering lexicon** — latent/model
   space, information bottleneck, gating — so they buy the ML side of the bridge for free and need no teaching;
   *Bottleneck* additionally makes the chart's own decomposition `closure ⊂ bottleneck` readable straight off the
   component names. *Aperture, Governor, Scribe* are the **evocative-but-earned** three, chosen exactly where
   engineering has no ready word, so they satisfy MG's mystery criterion without violating the
   earned-by-compression test: an aperture is variable admission with a controllable width, a governor is Watt's
   flyball mechanism, a scribe writes the transient into the permanent. **Naming is now frozen for the wiki, the
   eight book editions and the poster** — reopen only with a stated reason, because churn past this point costs
   real work.


### Settled by MG, S288 (2026-08-06) — five of the eight, decided on the session's recommendation

MG's instruction was *"1b your recs except 4 and 7 and 8 we need to discuss"*, i.e. items 1, 2, 3, 5 and 6
below are adopted as recommended. Recorded here in full so the reasoning survives the conversation.

- **1 · Register names — ADOPT *Wired* / *Running* on the chart's face**, with *implicit/explicit* retained as
  the paper's technical vocabulary and IWM/ISM/EWM/ESM as the formal alias. The chart is therefore a
  **translation layer, not a rename**: nothing in the published FMT paper or the eight book editions has to
  change, so the decision costs no reprint and stays reversible. It buys the ML bridge in one line —
  *wired = weights (what plasticity changes), running = activations (what anaesthesia stops)*.
  **Explicit finding on the 2015 input:** *Bewusstsein* (capacity) vs *Bewusstheit* (ongoing interaction) is a
  **different and orthogonal** distinction — it separates system-level capacity from occurrent state, whereas
  Wired/Running separates two *kinds of model* that both exist in a waking system at once. Using the German
  pair as register names would collapse two axes into one. It belongs to how the **ladder** is read (which rung
  you *have* vs what is *running now*), and is recorded there instead.
- **2 · ADOPT the agreement mark (§0.2)** as the chart's marking system, five states, *blank* meaning nobody
  knows. This is the instrument that converts consensus from persuasion into a reading operation and yields the
  field's first convergence metric; without it the chart is a manifesto. It commits FMT to publishing its own
  exposed surface, which is the price of being infrastructure rather than advocacy.
- **3 · KEEP BOTH.** The *Interpretation* / *Bedeutung* split governs the paper's formal sections; the
  coordinate-transform formulation governs the chart, the wiki and the blog. They are not rivals — the
  transform **is** the interpretation process and the resulting relation **is** meaning, so the fusion is a
  presentation choice, not a competing claim. Dropping the split would cost the formal sections their
  process/relation precision for no gain; dropping the fusion would cost the accessible register the
  addressee-relativity and teaching results in one move.
- **5 · Consciousness ONLY for v1.** RIM/intelligence becomes a declared adjacent chart, not a second half.
  Constraint D1 caps the chart at ~40 cells; folding intelligence in roughly doubles it and dilutes the one
  claim the chart is making. Bildstein's "Symmetries in Science" therefore gets **one chart plus a named second
  axis**, which is also the more honest presentation given RIM's three desk rejections.
- **6 · KEEP "the Presence Term."** It has to be signable by a dualist and legible to the
  matrix/multiverse constituency without conceding anything to either, and it is the asset behind the
  dark-matter parallel. The alternates each prejudge: *First-Person Term* fixes the format, *Dark Term* imports
  a physics commitment, *Zeroth Register* calls it a model — which is exactly what the exclusion ledger
  declines to assert.
- **7 (this document's numbering) · Where it goes next — WEB FIRST, and the deployment is infrastructure's.**
  MG S288: *"B infra"*. aIware owns the chart's content and the citation audit; the
  `fmt.matthiasgruber.com` restructure (`AIW-27`) is executed by the **infrastructure** project and is routed
  there by cross-project inbox once the marks are audited. The charter (`AIW-100`) follows the live chart
  rather than gating it, because Bildstein is no longer a dated event (MG S288).

### Open

**All three reserved items were discussed and SETTLED later the same session (S288). Nothing in §7 is open.**

- **4 · R4 is the CONSCIOUSNESS floor (core/basic — the subject), not the sentience floor.** Sentience becomes
  a **`disputed` band spanning R2–R4** that the chart declines to place (see the ladder note in §2.4). Three
  reasons carried it: R4 is the chart's only rung that is *both* FMT-only *and* untestable (blank **B1**), so it
  is the worst possible carrier for the field's most ethically loaded line; placing the floor at closure denies
  feeling to every animal without a self-model, which is a fight FMT does not need and the fish-pain literature
  has not settled; and Damasio maps onto *consciousness* (core ≈ R4, extended ≈ R7), not onto sentience. FMT's
  own anchor points the same way — salvia detunes closure and the **self** dissolves while modelling persists,
  which is a claim about subjecthood, not about the presence of feeling. **The refusal to place sentience is
  itself a finding:** the field cannot agree whether feeling requires a self-model, and nobody had stated that
  disagreement as a coordinate.

- **7 · The chart declares the DEPTH AXIS; FMT supplies its resolution. MG's move, and it is better than either
  option offered.** MG: *"depth WILL become measurable… it is also a win for fmt if we can say the SMoC expects
  these dimensions, FMT has discovered an additional granularity."* So **R6 becomes a graduated rung** — a depth
  axis *d* declared on the chart's face with its increments left **blank**, because no theory in the field
  resolves depth — and **FMT fills it** with the three 2015 rungs *einfach / doppelt / dreifach erweitert*,
  each marked **FMT-only**. **Identification is promoted to its own rung, R7**, because identifying with the
  I-model is a change of kind rather than a depth increment; *Language-coupled* shifts to **R8**. The three
  *erweitert* rungs stay on the chart as sub-increments rather than in the glossary.
  **Why this is strictly better than both alternatives.** It is the Mendeleev structure the chart is built on:
  D3 says gaps *are* the research programme, and a declared axis with blank increments is exactly that. It
  satisfies D5, since a rival may accept the axis and decline FMT's filling. And it **inverts** the objection
  that three more FMT-only cells make the chart look like a manifesto — FMT-only marks sitting on a
  *field-blank* axis read as **contribution**, not advocacy, which is precisely what the marking discipline was
  designed to make visible. It also survives depth becoming measurable at zero restructuring cost: the axis and
  the named increments are already in place, and the marks simply migrate FMT-only → converging → agreed.
  **That makes this cell the chart's own demonstration case** — the first place where the convergence metric can
  actually be watched moving.
  *Implementation note:* a graduated rung is a new mark type for `figures/smoc-marks.svg` /
  `scripts/build_smoc_marks.py`. Small, but do it before the citation audit rather than after.
  *Renumbering is free:* the R-ladder is referenced only inside this file (the poster's "R7-1" strings are AICE
  reviewer IDs and the wiki's `R4[...]` are mermaid node labels — both unrelated), so R7→R8 costs nothing now
  and would cost real work after publication.

- **8 · Keep p.24's absolute falsehood AND p.32's renunciation of absolute truth; drop only the "Konvention von
  Wahrheit" sentence. MG's reconciling principle: *absolute falsehood doesn't require absolute truth to
  exist.*** This is sharper than the resolution originally proposed, and it means the chapter was never as
  broken as the S285 analysis said. **The asymmetry is Popperian and it falls out of the Bezugssystem
  architecture rather than being imported:** a reference system can be shown **inconsistent with its input**
  without any privileged reference system existing — falsity is a *within-system-against-input* relation, cheap
  and locally decidable, whereas truth would demand a *system-independent* standpoint, and there is no view from
  outside all reference systems.
  **MG's mechanism, S288 — this is what makes the falsehood *absolute* rather than merely current, and it is
  the load-bearing half of the argument.** MG: *"we had a scientific truth the earth is flat, based on
  observation, then through new observations found this to be wrong within our own existing truth framework of
  geometry, and decided earth is roughly a ball. which is society's truth roughly, but it could still turn out
  to be a 6D cube with a 3d ball subobject."* Three steps, and the asymmetry lives in the third:
  **(1)** The flat claim was itself a **geometric** claim, so geometry's own machinery and geometry's own new
  observations sufficed to kill it — the refutation is **framework-internal** and appeals to nothing outside.
  **(2)** The positive replacement — *roughly a ball* — is **society's current filling**: consensual and
  revisable, and it may be *subsumed* rather than merely refined (a 3D ball sub-object of a 6D cube would
  reframe it entirely).
  **(3)** But that subsumption does not readily make flat true again: a successor framework must preserve the
  observations that did the refuting, so it largely **inherits the refutation**.
  **⚠ MG's second correction, S288 — the asymmetry is a GRADIENT, not a binary:** *"when the deciding population
  changes, both falsehoods and truths can change, but falsehoods are more resistant."* An earlier drafting here
  said refutations *survive* framework change outright; that is **too strong and historically false** —
  continental drift, *H. pylori* and epigenetic inheritance were all declared false and came back. **Differential
  resistance is the claim, and it is enough.**
  **The mechanism:** a refutation is anchored to **one specific observed contradiction**, so overturning it means
  overturning that observation or showing the framework misapplied it — a **narrow, costly target**. A positive
  claim is **underdetermined** by the same observations, so any better-fitting model displaces it — a **wide,
  cheap target**. *Refutation is pinned by one contradiction; confirmation is exposed to every competitor.* The
  asymmetry is thus a matter of **how many ways each can fail** — degree, not kind — and the historical
  counterexamples become **explained rather than embarrassing**: they are precisely the cases where the refuting
  observation was weak or misapplied. The account predicts *when* a falsehood is overturned; a permanence claim
  could not.
  **Two further mechanisms, both MG's, both independent of the evidential one — full account in
  `.claude/knowledge/fmt-2015-definitions.md` (canonical home).** *Social:* new truths and truth→falsehood
  conversions both ride on positive evidence and are comparatively cheap, but a **societal** falsehood has
  already accumulated reasons, textbooks, curricula and reputations supporting *the logic of its falsity*, so
  the backward step must dismantle an invested apparatus as well as produce an observation — a **ratchet**.
  *Compounding:* the falsehood state is a **post-reversal** state, so going back is *"a second conversion of
  already 180° changed knowledge"* — and the expenditure that bought the first turn is exactly what resists the
  second. **⇒ The checkable prediction: resistance scales with the cost of the original conversion.** Expensively
  won falsehoods (flat earth — centuries, Copernicus, Galileo, institutional resistance) are near-irreversible;
  cheaply established ones return. *Continental drift* was rejected for want of a mechanism and *H. pylori* on a
  background assumption about stomach acid — both cheap, both came back. The account **predicts which
  falsehoods return**, which neither a permanence claim nor a bare gradient could.
  **Two senses of "absolute", not to be conflated:** *semantically*, falsity is **not a consensus property** —
  the deciding population does not make or unmake it, which is the whole anti-p.32 point; *epistemically*, our
  verdicts about both truth and falsity remain revisable. Absolute falsehood is **earned by accumulated
  refutation**, never read off an absolute truth — which is why renouncing absolute truth (p.32) and keeping
  absolute falsity (p.24) is consistent rather than a fudge.
  **This also explains the rename directly, and independently:** the graded consensus measure applies **only to
  the positive direction**, where nothing is absolute. It has no work to do on the negative direction, where the
  verdict is sharp and permanent. Using one word for both was the defect.
  **Self-consistency worth naming:** this is the same epistemology as the chart's own constraint **D6** —
  *the chart does not have to be right to be useful; it has to be organised, falsifiable and revisable*
  (Mendeleev's eight wrong atomic weights; the indispensable-but-wrong Bohr atom). **SMoC's licence to publish
  now and FMT's theory of truth are one principle stated twice** — the same shape the Bezugssystem finding
  already has.
  So p.32's first clause (*"auf das Konzept einer absoluten Wahrheit verzichten
  wir"*) is **retained and correct**; p.24's *the flat earth was false then and is false now* is **retained**;
  and only p.32's second move — truth-value changing because the deciding population changed — is dropped.
  **The real defect is narrower and more interesting than a contradiction:** the book used ONE word,
  *Wahrheitsgehalt*, for TWO different relations — the sharp negative one (falsity) and the graded social one
  (agreement across reference systems). Falsity keeps its sharpness and needs no new name; the graded measure is
  renamed **Konsensgrad / Übereinstimmungsgrad / degree of corroboration**.
  **Routing, and the split matters:** the *correction* to the monograph stays **internal** (`AIW-153`, German
  2nd-edition errata — publishing self-criticism of one's own book has no upside in any venue). But **the
  principle is publishable on its own**, never framed as a fix: *absolute falsehood does not require absolute
  truth*, with its Bezugssystem derivation, is a standalone epistemological result that runs on definitions
  alone — the same shape as the regress argument, and a natural neighbour to it in the FMT paper's §3.6
  (a **v15** candidate).
  *Knock-on to verify before the audit:* §3.1's knowledge cell must carry **no truth condition**.

1. ~~**Register names**~~ — **SETTLED S288**, see above. Original framing retained for provenance:
   **Wired / Running** on the chart's face, replacing
   *implicit/explicit*, with IWM/ISM/EWM/ESM kept as the technical alias. Same rationale as the settled seven:
   it is borrowed vocabulary that hands over the ML bridge in one line — *wired = weights (what plasticity
   changes), running = activations (what anaesthesia stops)*. Riskier than the component names because
   implicit/explicit is load-bearing in the published FMT paper and in eight book editions, so this one is a
   translation decision rather than a fresh naming decision.
2. ~~**Adopt the agreement mark (§0.2)?**~~ — **SETTLED S288: adopted.** Original framing: Five states, *blank* meaning nobody knows. It is what turns consensus
   into a reading operation, and it commits FMT to publishing its own exposed surface.
3. ~~**Keep 2015's *Interpretation* / *Bedeutung* split, or let the transform language carry both?**~~ —
   **SETTLED S288: both, split for the formal sections, transform for chart/wiki/blog.** Original framing: 2015
   separates the **process** (interpretation assigns information to a reference system) from the resulting
   **relation** (meaning is that relation). Your 2026 coordinate-transform formulation fuses them and adds a
   named target basis plus a direction. The fused version explains addressee-relativity and teaching in one
   move; the split version is cleaner for the paper's formal sections. Both, or one?
4. **Is R4 the sentience floor or the consciousness floor?** The terminology work says use *sentience* for the
   felt floor; the ladder currently marks R4 "sentience begins here", which makes R6 the extended/
   autobiographical rung. Every downstream translation depends on this.
5. ~~**Chart scope: consciousness only, or consciousness + intelligence (RIM)?**~~ — **SETTLED S288:
   consciousness only for v1; RIM = declared adjacent chart.** Original framing: Decides whether Bildstein's
   "Symmetries in Science" gets one chart or two.
6. ~~**Name for the residue cell: the Presence Term?**~~ — **SETTLED S288: keep *the Presence Term*.**
   Original framing: (§2.7) Technical gloss *first-person-only format*;
   drawn with no outline, so the neutrality is geometric rather than asserted. It has to be signable by a
   dualist and attractive to the matrix/multiverse constituency without conceding anything to either. Alternates:
   *the First-Person Term* (more precise, less accessible), *the Dark Term* (closest to the physics parallel),
   *the Zeroth Register* (cheeky, but "register" prejudges it as a model).
7. **Where this goes next.** Candidates: the SMoC working-group charter (AIW-100, the gating Bildstein
   deliverable), the MoC7 poster's spine, the wiki's top-level restructure (AIW-27), or a standalone position
   paper. My read: charter first — smallest artifact that makes the chart real, and it already gates a dated
   event.

---

## 8. Provenance and discipline compliance

Built on: the three principles as landed in FMT v14 §3; the constitutive-vs-enabling framing (S277); the
closure ⊂ bottleneck decomposition and the efficiency-not-necessity ruling (2026-08-06); the
closure-off-is-two-closed-systems theorem at N=22,000 and its correction of the over-reaching
return-ness claim; the didactic-pattern registry, particularly the closure-advantage batch (#18–27) and the
parsimony batch (#28–30); the awareness/consciousness terminology discipline; the one-directional criticality
rule.

Rules observed: closure is an advantage, never a necessity (S3); criticality one-directional, no
biconditional (S2); four kinds, never four modules (S6); three principles, not five; honest convergence —
every **converging** credits the tradition and claims no priority; no anatomical identification of roles (S7).

**New didactic patterns generated here**, for the co-owned registry once §7 is settled: *the missing middle
layer* (the three-layer diagnosis); *the Bohr-atom licence* (a middle layer need not be right to be
indispensable — D6); *Mendeleev's blanks* (gaps as the research programme — D3); *the status tag* (consensus
as a colouring problem); *the pre-2005 test* (a middle layer statable without recent results is not fitted to
them — D7).
