<!-- Action: reference -->
<!-- Tracked-by: AIW-137 -->
<!-- Source of truth for the MoC7 A0 poster. Edit here, then rebuild the PDF. -->

# MoC7 poster — content draft v1

**Format:** A0 portrait (841 × 1189 mm), three columns. Answered: the organisers confirmed A0
portrait on 2026-08-20.

**Built proof:** `drafts/moc7-poster-A0-proof.pdf` — 1 page, 841 × 1189 mm, verified.
**Rebuild:** `bash scripts/build-moc7-poster.sh` (asserts 1 page + A0; writes into
`tmp/build-moc7-poster/` only). Add `--promote` to copy the two proof PDFs into `drafts/` — it never
writes a figure there, because doing so silently reverted an approved closure-symbol fix at S303.
**Build sources (tracked):** `scripts/assets/moc7-poster/` — `poster.html` plus the figure SVGs.
**Figures — both purpose-built for the poster; neither canonical file was modified.**
`drafts/moc7-poster-fig-2x2.svg` (grid) — the paper's `figures/figure1-four-model-architecture.svg`
renders at ~7 pt on A0 with unreadable bullet lists, so this is a simplified large-type variant.
`drafts/moc7-poster-fig-bubble.svg` — `figures/figure2-real-virtual-split-simple.svg` adapted: internal
title dropped, model boxes widened, abbreviations enlarged to anchor at 2 m, and **a two-headed
closure arrow ESM↔EWM**, because the original bubble has no closure loop and closure is now P3.
**S321 (MF6, MG D2 = mutual):** both figures draw closure as two-headed ESM↔EWM — in the grid a
dashed arc joining the two explicit boxes replaces the ESM-only ring, which never touched the EWM its
caption named. Every arrowhead is an explicit polygon (cairosvg renders SVG markers reversed), and
every label is ≥ 18 pt at print size (grid ≥ 26 viewBox units, bubble ≥ 20). The bubble's "sensory
input" label now sits beside its path instead of on it. The build sources in
`scripts/assets/moc7-poster/` carry these changes; the two `drafts/moc7-poster-fig-*.svg` copies do
not yet.

**Header layout (MG 2026-08-03):** the lede is a **block-quote in the left header column, beside the
QR** — not a full-width band beneath the title block. The first build had it full-width, which left an
odd horizontal gap between the title block and the lede; MG called it out and directed the vertical
space into the dense column area below instead. Header padding was tightened and the gain spent on
leading (1.46) and section gaps (15 mm). **S321 freeze pass:** the must-fix swaps added more lines
than the free space held, so that gain was handed back — leading 1.40, section gaps 12 mm, table-cell
and list-item padding trimmed, header padding trimmed. No type size changed.

**Subtitle is one line on purpose:** "with converging empirical support" (MG D1, S321). The previous
wording is the one v15's own §8.1 caveat makes hardest to defend: some corroborating work predates the
2015 publication, and the ledger names the independent groups two feet below anyway.

**FIGURE = BUBBLE. Settled by MG (S321, re-stated S327: "bubble and i told you that a million times").** The grid
variant is retired and no longer builds; the one proof is `drafts/moc7-poster-A0-proof-bubble.pdf`. Do not ask again.

**Type sizes as built:** title 76 pt · subtitle 52 pt · block heads 44 pt · lede 34 pt · body 30 pt ·
tables 24 pt · sources 22 pt. Body is well above the 24 pt floor for 1.5–2 m reading; when content
stopped fitting, copy was cut rather than type shrunk.
**Word count:** ≈ 780, inside the 600–800 target.

**Sourcing note.** Content is taken from the current paper (`paper/full/four-model-theory-full.md`
§3.1, §3.7, §8) and the sharper closure formulation in `drafts/aiw130-jaic-draft.md` §3–4 + Box 1 —
*not* from the June abstract, which predates both. The accepted title is kept verbatim so the poster
matches the conference booklet.

---

## Block 1 — Header

**The Four-Model Theory — A structural taxonomy of consciousness, with converging empirical support**

Matthias Gruber · Independent researcher · ORCID 0009-0005-9697-1665
`matthias@matthiasgruber.com`

**[QR CODE]** → full preprint, https://doi.org/10.5281/zenodo.18669891

> Consciousness is the capacity of a system to build a model of itself, to relate to that model, and
> to interact with it. What distinguishes a conscious system is not that it carries a self-model, but
> that self-model and world-model each enter the other's *update rule* — a relation stated as an
> intervention, so it can be clamped and swept in any system one can intervene on.

<!-- MG 2026-08-03: the previous lede ("...sharp enough to be applied to a candidate system — and
     sharp enough to fail") was cut. It advertised good scientific practice to an audience of
     scientists instead of stating the theory — the AI-tell / meta-science register banned by
     memory/feedback_ai_tells_meta_science.md. Two more instances of the same class were cut in the
     same pass: "Read the corroborated column honestly" → "Most of the corroboration is shared", and
     "the poster makes no attempt to read it" → "is not what the criterion measures". Keep sweeping
     for this class in every revision. -->

<!-- KEPT deliberately: the "What would falsify it" block. It lists five specific disconfirmers with
     thresholds — that is content, not a lecture about falsifiability. The banned register is
     *talking about* method; naming what would kill the theory is method. -->

<!-- RESOLVED (AIW-138, MG 2026-08-03). The five-principles question is moot: FMT now has THREE
     principles, and they are on the poster as Block 2b. Criticality demoted to a signature; the old
     "virtual qualia" renamed and MERGED with self-referential closure into P3; redirection,
     permeability and forking demoted to consequences. §6's explanatory range — the other contender
     for the space — went in as Block 2c. Both fit because the Level block was cut. -->

---

## Block 2 — Two axes, four kinds

**[FIGURE: the 2×2 grid — scope (world / self) × mode (implicit / explicit), large]**

A 2×2 taxonomy of computational **kinds** — not four modules, four boxes in a wiring diagram, or four
anatomical regions. In any substrate the kinds are realized as graded, overlapping, plastic partitions
with shifting boundaries.

**And they are not posited.** They are the minimum the architecture forces: anything conscious must
model world and self, at both the structural and the simulation level. Four is the floor, not the
ceiling.

<!-- This is §3.2's "principled minimum" + "Why four, not three?", promoted from p.12 of the paper to
     the poster. MG 2026-08-03: cleanest kill for the "four modules" misread, and it turns the
     taxonomy from a stipulation into a consequence. The two paragraphs that used to sit here were cut
     in the same pass — the three principles now say what they said, more fundamentally. -->

---

## Block 3 — The criterion: self-referential closure

A rich, decodable self-model can sit in a system as a read-only object that a downstream controller
consults. That is not enough. **Closure** is the stronger condition that the explicit self-model
and world-model each enter the other's *update rule* — the system models the world *through* a model
of itself, and itself through its model of the world.

Stated as an intervention rather than a description: clamp the self-variables, do(σ := c), and sweep
the clamp value. Closure holds when the world-model's induced transition differs across clamp values

  Δ_W^{do(σ:=c), ω}  ≠  Δ_W^{do(σ:=c′), ω}

on a non-negligible set of admissible contexts, **and** symmetrically when the self-transition depends
on the world-cell. A one-way arrow σ → Δ_W is ordinary causal coupling, satisfiable by any
feed-forward self-input; the mutual dependence closes the cycle.

*Formal statement: in preparation.* (small note directly under the formal box — MG D15 = tag)

**Off-line sub-clause.** The dependence must survive decoupling from current sensory input. This is
what separates a self-*model* from a self-*monitor*, and it excludes a homeostatic controller whose
body-state estimator merely feeds adaptive gain into its world-model.

Closure is graded: κ = min(κ_W, κ_S), with

  κ_W = sup_{c,c′,ω} d(Δ_W^{do(σ:=c), ω}, Δ_W^{do(σ:=c′), ω})

and κ_S likewise for Δ_S under a clamp of the world-cell, do(w := u).

<!-- MG D2 = mutual (S321): the symmetric clause stays, so the graded strength is the weaker of the
     two directions. The κ_W line is its own non-breaking .eq div on the poster (MF11); the same
     formula is on the handout. -->

The criterion is **intrinsic and substrate-neutral**: invariant under structure-preserving
relabelling. An unfolded feed-forward chain matches the closed system's behaviour only with unbounded
resources; under a resource bound the two come apart, and that efficiency gap is the empirical
handle.

---

## Block 4 — The ledger

**Corroborated — derived from the architecture in 2015; independent work consistent with it:**

| Expectation | Independent work |
|---|---|
| Consciousness-abolishing agents all push the substrate below criticality, whatever the receptor mechanism | Maschke 2024 (ketamine); Toker 2026; Algom & Shriki 2026; PCI, consistent, predates: Casali 2013, Casarotto 2016 |
| Waking degrades criticality; sleep restores it | Meisel 2013 (predates); Xu 2024 (10–14 d continuous) |
| Sleep onset is a bifurcation, not a dimming | Li 2025 (n > 1,000; critical slowing ≈ 4.5 min ahead) |
| Rising permeability exposes processing stages in hierarchical order | Carhart-Harris & Friston 2019; Timmermann 2023 — *shared with predictive processing* |
| Callosotomy degrades bilaterally rather than splitting cleanly | Pinto 2017 — *FMT's reading of their data; observable not unique to FMT* |

**Open — novel; four untested, one partly tested:**

| Prediction | Status |
|---|---|
| Psychedelics alleviate anosognosia, dose-dependently, in disconnection-type cases | untested; coarse form also follows from REBUS — FMT adds sub-ego-dose dependence, lesion-side complexity, disconnection vs destruction |
| Ego-dissolution identity content tracks the dominant sensory input, modality-specifically | untested |
| DID alter switches show a self-referential → sensorimotor dissimilarity gradient | untested |
| Lucid-dream onset is a phase transition in the self-model's criticality state, not a ramp | untested; awaits real-time criticality tracking in sleep |
| Qualia structure aligns across individuals; absolute encoding does not | group-level structural alignment shown (Kawakita 2025); individual-level arm and the paired decoding failure untested |

**Most of the corroboration is shared.** It concerns criticality — the neural signature of
Principle 1 — which FMT holds in common with ConCrit, REBUS and the entropic-brain program. Setpoint
premise: Hengen & Shew 2025 (~140 datasets). What is distinctive is the *derivation path*: Principle 1
was motivated by computational universality, independently of the empirical criticality literature. And free modelling is **necessary, not sufficient**. No free modelling → no consciousness, never the converse.

---

## Block 2b — Three principles

*Settled with MG 2026-08-03 (AIW-138). Replaces the "Level = depth of closure" block, which the
principles supersede. Sits at the foot of column 1, under the grid.*

1. **Open-ended computation allows free modelling.** Near-criticality is what this looks like in
   neural tissue — the signature the property leaves in a substrate, not the principle itself.
2. **Recurrent non-linear dynamics of sufficient complexity host a second computational level:**
   persistent activity patterns that survive their own inputs, interact, and compute over one another
   — individuated by their mutual effects rather than by which cells carry them. This level is the
   explicit, virtual side.
3. **Phenomenology is a real, physical effect on that level, and arises exactly where the modelling
   closes on itself** — the theory's one bridging commitment, argued for rather than derived.

Everything else follows: the four kinds, the redirection of the modelling resource onto the non-self
that builds the world-model, variable permeability, and the forking of the self-model.

<!-- P3 merges the old "virtual qualia" principle with self-referential closure (MG: "yes principle 3
     and 4 are one"). Its biconditional IS FMT's constitutive claim (§3.4) and remains asserted-not-
     derived (§3.4.3). It does NOT license any criticality claim — S331: criticality is a signature, not a requirement (S329 ruling). -->
<!-- "Standing wave" is deliberately absent from the print wording: cortex shows travelling waves too,
     and the claim is persistence, not geometry. Keep the standing-wave image for speech only. -->

---

## Block 2c — What the architecture accounts for

*§6's explanatory range, absent from the first draft. MG 2026-08-03: "definitely a very strong
contender". Named phenomena only — never a boast about deriving much from little, which is the banned
register.*

| Phenomenon | Via |
|---|---|
| Psychedelic phenomenology | raised permeability exposes intermediate processing stages |
| Anaesthesia | substrate pushed out of the open-ended regime |
| Dreams, lucid dreaming | permeability; lucid onset = basic → simply extended consciousness |
| Split-brain | each hemisphere keeps a degraded but complete copy — halved in resolution, not in content |
| Dissociative identity disorder | forking of the explicit self-model |
| Animal consciousness | graded depth of recursive self-modelling |

---

## Block 5 — What would falsify it

- **Free modelling** — robust consciousness where a fixed lookup reproduces the system's behaviour on novel input.
- **Closure** — disrupting the loop degrades *report* but leaves phenomenology intact under no-report
  paradigms.
- **Dissociation** — no manipulation suppresses one level without proportionally affecting the other.
- **Permeability** — psychedelics raise complexity without improving explicit awareness in
  disconnection-type anosognosia.
- **Qualia** — absolute-state decoding generalizes across individuals as well as unsupervised
  structural alignment does.

---

## Block 6 — In progress, and what I am here for

A **category-theoretic formalization** is in development: model kinds as objects, implicit→explicit
transitions as natural transformations, compositional semantics for inter-model relations. Roadmap:
https://doi.org/10.5281/zenodo.21843693

The criterion is being written up as a **three-check detector** (paper in preparation): self-attractor
present; closure enters the world-model update; open-ended computation actually deployed. Toy-scale
closure mechanism results: https://doi.org/10.5281/zenodo.21610993

The open predictions need people with clinical and imaging access, which is why I am here — please
come and argue with me.

<!-- All three DOIs on the poster are CONCEPT DOIs (MG: never version DOIs), verified 2026-09-23:
     18669891 → FMT preprint (14 versions), 21610993 → in-silico companion (2 versions),
     21843693 → "Toward a Mathematical Formalization of the Four-Model Theory" (3 versions).
     A#9 ("self-inclusion falls out of wiring", v15 §8.9 Eighth result; MG D6 = yes if it fits) was
     NOT printed: column 3 has 7.7 mm left after the must-fixes, less than one body line.
     Robot box (D7): NOT on the poster — S327 2026-09-30 MG chose an off-poster TENT CARD instead
     (the box measured 89.5 mm; the poster has ~36 mm spare, all in column 3). Caption, MG-chosen:
     "By this poster's own criterion, the robot beside it is not conscious: a spiking network with a
     camera, a learned choice among seven moves, a reflex and a fear of backing onto unknown ground, but
     no self-model entering a world-model. It is the baseline a closure architecture must beat."
     It describes crucible's MoC7 demo brain as ruled 2026-09-30 (the Q-table brain). Source
     scripts/assets/moc7-poster/robot-card.html -> drafts/moc7-robot-card.pdf (A5 landscape, fold).
     The honest box keeps its two sentences. Handout: robot left out. -->


---

## Not on the poster — answers to have ready

From the three AICE-26 peer reviews (`tmp/aice-review-mapping.md`); better-informed people will raise
the same at the board.

| Objection | Short answer |
|---|---|
| Operationalization gap (R7-1) | Block 3 *is* the answer — an intervention algebra, not a description. Offer to send the detector paper when it is out. |
| Spreadsheet analogy is flawed (R7-3) | Drop the analogy in conversation; go straight to level-constitutive properties. |
| Implicit/explicit linkage unjustified (Rc-1) | Rameson 2010 ran the 2×2 factorial; Dehaene & Naccache 2001 and Doyon 2003 establish the axes independently. |
| Animal evidence missing (R7-8) | §6.4. Concede it is the thinnest part. |
| Novelty unclear (Rm-2) | The derivation path, plus closure as a *counterfactual* rather than a possession claim. |
| "Four modules" misread | Never say it. Point at the grid — the visual form does the work. |
| "Isn't the modelling level just Turing complete?" | **Yes — and that is the point against using it.** Under unbounded memory the brain, a PC and Rule 110 are all in the same class, so the predicate cannot separate a conscious system from a spreadsheet with a loop. Conceding it hands away the §3.4 Stage-1 distinction. Say instead: the claim is (a) the modelling is **not amortizable** — no fixed lookup reproduces it on novel input — and (b) **architectural** — the self-model enters the world-model's update rule. Neither is a complexity-class claim. If pressed on neural nets specifically: Siegelmann & Sontag showed rational-weight RNNs are Turing universal, but that construction needs unbounded activation precision — the same infinity, through a different door. |

**Print:** local paper print in Wolfurt, a few days before the flight (MG D11, S321).
**Bring:** the A4 handout (`drafts/moc7-handout-a4.pdf`); 2–3 copies of the book.
