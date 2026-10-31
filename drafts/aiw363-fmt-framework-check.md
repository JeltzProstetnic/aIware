# AIW-363 — FMT master checked against MG's framework rulings of 2026-10-30

**Paper:** `paper/full/four-model-theory-full.md` (line numbers below refer to this file; every edit target was
also found once in `paper/full/latex/paper.tex`, so each accepted edit lands in both).
**Rulings:** `~/crucible/docs/decisions.md` 2026-10-30 entries (~08:50 to ~11:50, incl. D10); aIware record
`docs/decisions.md` D-S366-A, D-S366-D. D10 (~11:50) settles the earlier provisional D7: an integrated,
lower-dimensional copy of body signals IS a first simple explicit self model. It is treated here as part of ruling (2).
**Status:** research only. Nothing in the paper was changed. Every replacement below is PROPOSED, for MG's approval.

## Verdict

The paper already agrees with most of the framework. It puts phenomenality in the mutual updating of the explicit self and
world models (Principle 3, §3.5 floor, Table 1b). It holds explicit content outside the loop to be unconscious
("preconscious", §3.3, §3.4.6, Table 1 "Becomes conscious"). It already states ruling (1) in §3.1 and Table 1. Three
things conflict. **First, the scope axis:** the paper nests the explicit self model inside the explicit world model
(ESM ⊆ EWM, §3.1, §3.2, Table 2, Fig. 1, §3.4.3 Stage 3). Ruling (3) makes the world model all explicit modelling
*outside* the self model. This is the largest conflict and needs MG's decision (T1). **Second, two sentences
describe the ESM as if all of it were conscious** (§3.2 l.226, Fig. 3 caption). Rulings (5) and D10 need an ESM part that
is not active. **Third, two passages misstate closure:** l.297 puts consciousness in the relation between explicit
models and the implicit substrate, and l.893 has closure run one way. Smaller items: the write criterion at l.152 is
defined through an evaluation error, which presupposes a read. The paper never names "active" parts, and it uses
"active" to mean "running" (Table 4). It never uses "subconscious". Its 2015 source defines *Unterbewusstsein* so that it
includes implicit knowledge, and that collides with ruling (5).

Conflicts per ruling: (1) 1 · (2)+D10 0 direct, 1 if Principle 2 is read literally (T5), plus 2 missing statements ·
(3) 5, all one nesting issue, plus a term collision on "active" · (4) 2 · (5) 2, plus the subconscious/preconscious term.

---

## Ruling (1) — a model is recurring activity that writes (follows) its target and is readable; actual reading only for consciousness

| Line | Quote (verbatim, ≤ 30 words) | Status | Why |
|---|---|---|---|
| 152 | "A model must be readable; that it is actually read is required only for consciousness (Section 3.4.3). A structure the system cannot evaluate is a data structure, not a model." | agrees | Ruling (1) as applied in S366. |
| 152 | "such that *M* can be evaluated: operating on *M* yields states that *h* relates to consequences in *T*" | agrees | "can be evaluated" is readability. "State or structure" also covers the stored implicit models, which the ruling (about activity) does not address. |
| 152 | "*T* fixes the model's boundary; updating *M* from that error is the write access of Table 1" | **conflicts** | "That error" is the error of an evaluation, so write access as defined here presupposes that *M* was read. Under (1), write = following the target, with no reading required. Table 1 (l.164) already says "updates from new input". Edit E1. |
| 164 | "(1) write access (updates from new input), (2) read access (its representations can be evaluated by the system; being read is required only for consciousness)" | agrees | Matches (1). |
| 164 | "(3) boundary recognition (differential response inside vs. outside the target domain; Gruber, 2015)" | ambiguous | Ruling (1) names two criteria. Crucible ~08:50: MG chose "Write is enough"; for the explicit-model claim the boundary becomes extra characterisation. Whether Table 1 keeps three criteria is T7. |
| 164 | "the Bereitschaftspotential is consistent with read access, though preparatory motor activity alone does not establish that the system interprets its own representations" | ambiguous | The caveat concerns actual interpretation, which the definition no longer requires for a model. No edit needed. The caveat can go if MG wants Table 1 shorter. |
| 137, 240 | "persistent activity patterns that survive their own inputs, interact, and compute over one another, individuated by their mutual effects" | ambiguous | (1) says *recurring*; MG on 10-28 ruled that a pattern may recur every *n* steps and need not be continuous. Read literally, "survive their own inputs" also excludes D10's input-locked copy. Decision T5. |
| 172 | "Content-specific neural activity (fMRI BOLD, EEG/MEG source-localized) that tracks reportable experience and collapses under anesthesia" | ambiguous | The observable catches only the active, in-loop part. Non-active explicit models (ruling 5) follow their target without tracking reportable experience. It is a detection handle, not the definition, so no edit is required. |
| 609 | "The readout function itself is available to systems well short of closure …; only at closure is the value read a quale" | agrees | Reading alone is not consciousness; consciousness includes reading. Consistent with (1) and (4). |

## Ruling (2) + D10 — a realistic explicit self model is a lower-dimensional, integrated copy of the actual self; strong explicit/implicit differences only in imagination and complex cases

| Line | Quote (verbatim, ≤ 30 words) | Status | Why |
|---|---|---|---|
| 226 | "The ESM is generated from the ISM (which provides the self-knowledge) and current interoceptive and proprioceptive input" | agrees | Body signals through stored wiring. The crucible session cited this passage too. |
| 226 | "the brain's continuous generation of a unified self-narrative that constitutes self-experience" | ambiguous | "Narrative" is compatible with "copy" for a human ESM that includes history, but the paper never says that the realistic ESM is a reduced copy of the actual self. Insertion E9. |
| 236 | "it needs stored self-knowledge … to construct the ongoing self-narrative … Without an ISM, the ESM has no source material" | agrees | Same source as (2): the wiring supplies the copy. "Construct" is compatible. |
| 150 | "constructed on the fly, revised where it fails, and filled with interpolations, simplifications, and outright confabulations" | ambiguous | "Simplifications" fits "lower-dimensional". "Outright confabulations" as normal content strains "departs strongly only in imagination". The crucible session read the passage as consistent. No edit proposed: the passage concerns self-simulation of world and self together. |
| 178, 417 | "The explicit models are *generated from* the substrate rather than filled by a copy of it" | ambiguous | Word collision only. The paper denies that explicit models copy *stored content*, and (2) affirms that the realistic ESM copies *the actual self* (its target). Decision T8. |
| 325 | "a realistic representation of the organism — its states, its geometry, its capabilities — in proportion to what the system has. A position estimate alone is not one." | ambiguous | "Realistic" agrees with (2). D10's model carries states only (hunger, pain, danger proximity). If the list is a conjunction, D10's model fails it. Decision T6; insertion E10. |
| 401 | "The self model at the floor is still a model of the system itself, however simple" | agrees | Compatible with D10's simplest case. |
| 531 | "the first stable attractor such a network forms is expected to model it … the first representations brains formed would then have been simple representations of the body" | agrees | D10 is an instance of this expectation. |
| 593 | "it maintains continuity through **confabulation** … reconstructs a continuous self-narrative from whatever the ISM contains" | ambiguous | About continuity across interruptions, not the present self-image. Compatible. |
| 663 | "Interoceptive-style regulation of a body-model is one route to the ESM" | agrees | |
| 734 | "The explicit self-model is a process that requires input to run (Section 3.2); it does not carry its own content independently of what feeds it." | agrees | A copy needs its body input. |
| 767 | "experiences of "becoming" objects or entities in their immediate environment: becoming a piece of furniture, becoming a wall" | agrees | The strong-departure case, MG's "being a horse or a chair". |
| 803 | ""self-model" means a model of the organism itself, however simple, in proportion to what the organism has (Section 3.4.3), not narrative autobiography" | agrees | |
| 137, 240 | "persistent activity patterns that survive their own inputs" | conflicts if read literally | D10 counts an input-locked integrated copy as an explicit self model, and whether it survives an input cut is untested (CRU-238). T5. |
| — | (no passage) | **silent** | The paper never states MG's flat ruling that only complex tasks, worlds and selves show a strong explicit/implicit difference, i.e. that in a simple system the two are hard to tell apart. Insertion E9. |

## Ruling (3) — world model = all explicit modelling outside the self model; active world model = the part that reaches the self model; active self model = the part of the self model that acts on the world model

| Line | Quote (verbatim, ≤ 30 words) | Status | Why |
|---|---|---|---|
| 152 | "The four kinds differ in two respects: scope of the target (everything, or the self as a proper part of it)" | **conflicts** | For the explicit kinds, (3) makes the world model's scope the complement of the self model. E2 (depends on T1). |
| 209 | "scope is a nesting: the self-model's content is a proper part of the world-model's (ESM ⊆ EWM, ISM ⊆ IWM)" | **conflicts** | ESM ⊆ EWM against "outside the self model". (3) covers explicit modelling only and says nothing about ISM ⊆ IWM, which is 2015-native (Gruber 2015, p.266, *"Das Selbstmodell ist ein Teil des Metamodells"*). E3, T1. |
| 213 | "\| \| Everything (world) \| Self only \|" (Table 2 header) | **conflicts** | Same issue in the explicit row. The Fig. 1 SVG carries the same header ("Everything (world)", "Self only"). E4. |
| 218 | "scope (world vs. self), a nesting (ESM ⊆ EWM, ISM ⊆ IWM)" (Fig. 1 caption) | **conflicts** | Same. E5. |
| 319 | "the world-model includes the self-model as part of its modeled reality" | **conflicts** | Containment. Under (3)/(4) the self enters the world model through mutual updating, not by being a part of it. E6. |
| 224 | "the brain's dynamic construction of a unified scene from sensory and stored data that constitutes perceptual experience" | ambiguous | Narrower than (3): "all explicit modelling outside the self model" also includes models of other agents (l.807) and non-active parts. Insertion E7. |
| 228 | "Real neural models do not respect the world/self boundary — they blend across it." | ambiguous | (3) needs a self-model boundary to define the world model as everything outside it. Compatible if a blended model is split by its parts. No edit proposed. |
| 561 | "patterns of activity within the simulation that constitute the ESM's self-perception within the EWM" | ambiguous | Containment wording. Follows T1. |
| 615 | "the self-model's manipulation of the explicit world-model (ESM-on-EWM)" | agrees | This is the active self model in (3)'s sense. |
| 621 | "the two are models in the same format, differing in what they are pointed at" | agrees | A partition by target, with no capability difference between self and world model (didactic-patterns caution B). |
| 807 | "modeling another agent is a *world-model* operation: the explicit world model is a general-purpose modeler" | agrees | Other agents lie outside the self model. |
| 201 | "test whether it reaches a self-model component that enters the world model's update rule and is entered by it" | agrees | "Component" = the active self model. Matches the crucible instrument (lagged prediction both ways). |
| 1093 | "linear decoding … from self-model units versus world-model units" | agrees | Disjoint units. |
| 1109 | "the explicit self-model (ESM) and explicit world model (EWM) should be *independently disruptable*" | agrees | Fits a partition more easily than containment. |
| 707, 713 | "All four active" · "All active, ↑ permeability" (Table 4) | term collision | "Active" here means running, and it includes the implicit models. Under (3) a running explicit model can be non-active. T3, E14. |
| 793 | "consistent with the EWM generating structured experiential content whenever it is active" | term collision | Same. |
| — | (no passage) | **silent** | The paper never names the active world model or active self model. It speaks of content "in the closed loop" and "outside the loop". E8 adds the definitions. |

## Ruling (4) — closure = mutual updating of the active explicit self model and the active explicit world model → phenomenality, "the sense of being here and now"

| Line | Quote (verbatim, ≤ 30 words) | Status | Why |
|---|---|---|---|
| 17, 138, 275 | "the self-model and the world-model each entering the other's update rule, as they must when both are activity patterns in one reciprocally wired recurrent substrate" | agrees | Mutual, between activity patterns (explicit). The parts that enter each other's update rule are, by (3), the active parts. |
| 401 | "The explicit world and self models close on each other, and their content is the present moment together with a primordial pain or a nothingness." | agrees | Explicit–explicit; "present moment" = "now". The paper says nothing about "here". Optional E15. |
| 357, 359 | "nothing in it models the carrying: the accumulated state is never represented as the recent past *of a perspective*, so no "now" is constructed" | agrees | Closure gives the "now". |
| 297 | "Consciousness arises from the interplay between this cortical automaton and the substrate that generates the automaton — from the dynamic relation between the explicit models the automaton carries and the structural knowledge base" | **conflicts** | Puts consciousness in the explicit–implicit relation. (4) and Principle 3 put it in the explicit self–world mutual update. E11. |
| 521 | "Consciousness arises from the interplay between the automaton's dynamics and the models it carries — the implicit models (IWM, ISM) … and the explicit models (EWM, ESM)" | ambiguous | Lists what the process needs and does not state closure. Readable as compatible. No edit. |
| 319 | "The system models the world, models itself within that world, and models the fact that it is the thing doing the modeling." | ambiguous | Representational framing of Stage 3. Mutual updating is stated at 138/275, not here. E6 adds it. |
| 436 | "its output, fed back into the world-model's update rule, yields self-consistency (Section 3.4). The two are separable, and only the second is closure." | ambiguous | Here closure is the channel's output fed into the world model, which is one direction and passes through the implicit–explicit channel. T4. |
| 444, 446 | "Attention is selection *into* the channel; closure is the pass back *over* what the channel holds." · "If experience is the closure of the self-model over the channel's occupancy" | ambiguous | Consistent with (4) only if the channel occupancy (*Arbeitsmodell*) is the active world and self models. T4. |
| 893 | "closure counts only where the self-model enters the world model's update rule (Section 3.4.3)" | **conflicts** | Stated one way. (4) and l.201 are mutual. E12. |

## Ruling (5) — the non-active parts of the explicit world and self models = the psychologists' "subconscious"

| Line | Quote (verbatim, ≤ 30 words) | Status | Why |
|---|---|---|---|
| 15 | "the explicit models are virtual and transient, and are phenomenal when they enter the self-model's closed loop" | agrees | Implies explicit content outside the loop. |
| 172 | "Virtual, transient, phenomenal in the self-model's closed loop (Section 3.4.6)" | agrees | |
| 178 | "Content entering the closed loop of self-model and world-model: … or taken up from an explicit model held outside the loop (Section 3.4.6)." | agrees | "Explicit model held outside the loop" = a non-active part. Crucible D8 cites this passage as consistent. |
| 224 | "conscious where its content enters the self-model's closed loop" | agrees | EWM sentence already allows a non-active part. |
| 226 | "The Explicit Self Model (ESM) is the conscious self in the closed loop" | **conflicts** | Leaves no room for a non-active ESM part, which (5) requires. D10 records an ESM with no closure at all. The Fig. 1 SVG labels the ESM "The conscious self — "I"" in the same way. E9. |
| 256 | "These are generated, transient, and phenomenal." | ambiguous | Flat claim, qualified two sentences later. E8 removes the tension. |
| 256 | "explicit content outside that loop is preconscious (Section 3.4.6)" | agrees in substance; **term collision** | Same set as (5), different name. T2. |
| 387 | "The boundary between implicit and explicit determines what reaches conscious awareness." (Fig. 3 caption) | **conflicts** | Under (5) explicit content can be subconscious, so the loop decides what becomes conscious. The implicit/explicit boundary only decides what can. The caption also uses "awareness", which §3.5 reserves for access. E13. |
| 391 | "It may be stored on the implicit side, or held in an explicit model without entering the self-model's closed loop." | agrees in substance | Block's "accessible" content covers the implicit side and the non-active explicit models. (5)'s subconscious covers only the explicit half. "Preconscious" is used here as Dehaene et al.'s (2006) term, which can stay. |
| 417 | "Implicit content becomes conscious when it enters the closed loop of self-model and world-model within what the running simulation currently represents." | agrees | The loop is a subset of the running simulation. |
| 442 | "content that passes through it is by construction content the running simulation currently represents" (with "changes to the *Arbeitsmodell* are conscious") | ambiguous | Read together, everything the running simulation represents would be conscious, which (5) contradicts unless the channel holds only the active parts. T4. |
| 170, 254 | "Substrate-level, learned, non-conscious knowledge" · "physical, structural, learned, and non-conscious" | agrees | The implicit level is "non-conscious", not "subconscious". 2015 drew the line differently (T2b). |
| 595 | "an unconscious processing loop at approximately 40 Hz … corresponds to substrate-level computation" | ambiguous | "Unconscious" for implicit-level processing. No conflict, but it is a third term in the same family. |
| — | (no passage) | **silent** | "Subconscious" occurs nowhere in the paper, and the paper never maps a psychological term onto the non-active explicit models. E8 adds the mapping. |

---

## Proposed minimal edits (all PROPOSED, for MG's approval; mirror each in `latex/paper.tex`)

Edits E2–E6 apply only if T1 = A or C. E8 and E14 depend on T2 and T3. The bracketed choices show where.

**E1 — l.152, ruling (1).**
Current: "*T* fixes the model's boundary; updating *M* from that error is the write access of Table 1, and the capacity to evaluate it is the read access."
PROPOSED: "*T* fixes the model's boundary; updating *M* so that it follows *T* is the write access of Table 1, and the capacity to evaluate it is the read access."

**E2 — l.152, ruling (3), if T1 = A/C.**
Current: "The four kinds differ in two respects: scope of the target (everything, or the self as a proper part of it) and mode (…)."
PROPOSED: "The four kinds differ in two respects: scope of the target (the world, or the self) and mode (…)."

**E3 — l.209, ruling (3).**
Current: "The two dimensions differ in kind — mode is a genuine orthogonal contrast, while scope is a nesting: the self-model's content is a proper part of the world-model's (ESM ⊆ EWM, ISM ⊆ IWM)."
PROPOSED (T1 = A): "The two dimensions differ in kind. Mode is a genuine orthogonal contrast. Scope divides the explicit models, the explicit world model being all explicit modeling outside the explicit self model, and nests the implicit ones, stored self-knowledge being a part of stored world-knowledge (ISM ⊆ IWM)."
PROPOSED (T1 = B, sentence kept, one added after it): "The part of the EWM outside the ESM, all explicit modeling of what is not the self, is the world model with which the self model closes."
(T1 = C: as A, with "and divides the implicit ones in the same way" in place of the nesting clause.)

**E4 — l.213 (Table 2 header), ruling (3), if T1 = A/C.**
Current: "| | Everything (world) | Self only |"
PROPOSED: "| | World | Self |" — and the same two labels in `figures/figure1-four-model-architecture.svg` (+ PNG and the translated BW variants).

**E5 — l.218 (Fig. 1 caption), ruling (3), if T1 = A.**
Current: "The two dimensions — mode (implicit vs. explicit), an orthogonal contrast, and scope (world vs. self), a nesting (ESM ⊆ EWM, ISM ⊆ IWM) — define four functionally distinct models."
PROPOSED: "The two dimensions — mode (implicit vs. explicit), an orthogonal contrast, and scope (world vs. self), which divides the explicit models and nests the implicit ones (ISM ⊆ IWM) — define four functionally distinct models."

**E6 — l.319, rulings (3) and (4), if T1 = A/C.**
Current: "The system's self-model (ESM) represents the system that is generating the world-model (EWM); the world-model includes the self-model as part of its modeled reality."
PROPOSED: "The system's self-model (ESM) represents the system that is generating the world-model (EWM), and each enters the other's update rule, so the self is modeled within the world it models."

**E7 — l.224, ruling (3); insertion after the first sentence of the EWM paragraph (all T1 options).**
PROPOSED insertion: "It comprises all explicit modeling outside the self model, including the models of other agents (Section 6.4)."

**E8 — l.256, rulings (3), (4), (5).**
Current: "Their content *is* experience when it enters the closed loop of self-model and world-model; explicit content outside that loop is preconscious (Section 3.4.6)."
PROPOSED (written for T2 = c, T3 = A): "The part of the explicit world model that reaches the self model is the *active* world model, and the part of the self model that acts on the world model is the *active* self model. Their mutual updating is the closed loop, which gives the sense of being here and now, and content in it *is* experience. The non-active parts of both models are what psychology calls the subconscious [source to choose and verify, T2]; the part of it that can enter the loop at any moment is preconscious (Section 3.4.6)."
(T2 = a: last sentence "The non-active parts of both models are subconscious (Section 3.4.6)." · T2 = b: "…are preconscious, what psychology calls the subconscious (Section 3.4.6)." · T3 = B: replace "*active* world model / *active* self model" with "the part in the loop".)

**E9 — l.226, rulings (2) and (5).**
Current: "**The Explicit Self Model (ESM)** is the conscious self in the closed loop — the brain's continuous generation of a unified self-narrative that constitutes self-experience."
PROPOSED: "**The Explicit Self Model (ESM)** is the generated self, conscious where it enters the closed loop — the brain's continuous generation of a unified self-narrative that constitutes self-experience."
PROPOSED insertion at the end of the same paragraph (after "…rather than stored in the substrate."): "When the system represents itself realistically, the ESM is a lower-dimensional, integrated copy of the actual self, produced through the stored wiring from current body signals. It departs strongly from the implicit self models only in imagination, as in imagining being a horse or a chair. Only complex tasks, worlds and selves show a strong difference between explicit and implicit models, so in a simple system the two are hard to tell apart."
(Optional: the Fig. 1 ESM label "The conscious self — "I"" → "The generated self — "I"".)

**E10 — l.325, ruling (2)/D10; insertion before "A position estimate alone is not one." (depends on T6).**
PROPOSED insertion: "An integrated, lower-dimensional copy of several body signals, such as hunger, pain and the nearness of danger, is one, of the simplest kind."

**E11 — l.297, ruling (4).**
Current: "Consciousness arises from the interplay between this cortical automaton and the substrate that generates the automaton — from the dynamic relation between the explicit models the automaton carries and the structural knowledge base that sustains them."
PROPOSED: "Consciousness arises within the explicit models this automaton carries, where the explicit self and world models update each other, while the structural knowledge base generates and sustains those models."

**E12 — l.893, ruling (4).**
Current: "…on the Four-Model Theory, closure counts only where the self-model enters the world model's update rule (Section 3.4.3)."
PROPOSED: "…on the Four-Model Theory, closure counts only where the self-model and the world model enter each other's update rules (Section 3.4.3)."

**E13 — l.387 (Fig. 3 caption), ruling (5).**
Current: "The boundary between implicit and explicit determines what reaches conscious awareness."
PROPOSED: "The boundary between implicit and explicit sets what can become conscious, and the closed loop of the explicit self and world models sets what does."

**E14 — l.707, l.713, l.793, ruling (3), if T3 = A.**
Current: "All four active" · "All active, ↑ permeability" · "whenever it is active"
PROPOSED: "All four running" · "All running, ↑ permeability" · "whenever it is running"

**E15 (optional) — l.401, ruling (4).**
Current: "…and their content is the present moment together with a primordial pain or a nothingness."
PROPOSED: "…and their content is being here, in the present moment, together with a primordial pain or a nothingness."
(Only if MG wants "here" at the floor. "Here" must not be read as a position estimate, which the same paragraph excludes.)

---

## Terms to decide

**T1. Scope: nesting or partition for the explicit models?** The paper nests the ESM in the EWM (l.152, 209, 213, 218, 319).
Project memory traces the explicit nesting to Gruber 2015 ("Ich-Modell eingebettet" in the Weltmodell; p.61 in the
2016 PDF, p.62 as cited per AIW-325). Ruling (3)
puts the world model outside the self model.
- A. Partition the explicit models (world model = all explicit modelling outside the self model). Keep the implicit nesting
  ISM ⊆ IWM, which is 2015-native (p.266). Edits E2–E7.
- B. Keep ESM ⊆ EWM as a nesting of targets. Name the part of the EWM outside the ESM as the world model that closure pairs
  with. Only E3-B and E7.
- C. Partition both rows (also ISM vs IWM). This departs from the 2015 p.266 sentence.

**T2. "Subconscious" vs "preconscious" for the non-active explicit content.** The paper says "preconscious" (l.256, l.391 via
Dehaene). Gruber 2015 (p.69) defines *Unterbewusstsein* as "sämtliches Wissen einer Entität, welches Auswirkung auf deren
Bewusstsein, Wahrnehmung oder Verhalten haben kann", which includes implicit knowledge. It defines *Vorbewusstes* as the
subconscious content "welches jederzeit bewusst werden kann".
- a. Replace "preconscious" with "subconscious" at l.256, and keep Dehaene's term only where it is cited (l.391).
- b. Keep "preconscious" and add that psychology calls this the subconscious.
- c. Use both, as in 2015, with the scope narrowed by ruling (5): subconscious = the non-active explicit models; preconscious
  = the part of them that can enter the loop at any moment.
- Sub-question: is implicit knowledge also "subconscious" (2015) or only "non-conscious" (current paper, l.170/254)? And
  which psychologists does the paper name? Janet used "subconscious". Freud used "preconscious/unconscious" and rejected
  "subconscious". Kihlstrom's (1987) "cognitive unconscious" is mostly implicit processing and would collide with (5).
  Any source has to be read and verified before it enters the paper.

**T3. "Active" in the paper.** The paper uses "active" for running (Table 4 l.707/713, l.793) and never in (3)'s sense.
- A. Adopt "active world model / active self model" in the paper (E8) and change the paper's other uses to "running" (E14).
- B. Keep the paper's "in the closed loop / outside the loop" and use "active" only in the crucible instrument.

**T4. Is the *Arbeitsmodell* (channel occupancy, §3.6.1) the active part of the explicit models?** l.436, 442, 444 and 446
describe closure as the self model's pass over the channel's content. They also suggest that all content the running
simulation represents is conscious.
- a. Yes: the channel holds the active world and self models, and closure is their mutual update. §3.6.1 then agrees with
  (4) and (5) as written, and one clause at l.444 could say so.
- b. No: the channel carries content on its way into the loop, and active parts can lie elsewhere. Then l.442 needs
  narrowing.
- c. Leave §3.6.1 as it is for now.

**T5. Principle 2's "persistent activity patterns that survive their own inputs" (l.137, l.240).** It conflicts with
"recurring" (ruling 1; MG 10-28: recurrence after gaps counts) and, if read literally, with D10's input-locked copy.
- a. Keep it as a description of the second level as a whole, with simple input-locked models as its limiting case.
- b. PROPOSED text: "recurring activity patterns, regenerated by the wiring from current input, that interact and compute
  over one another, individuated by their mutual effects rather than by which cells carry them."
- c. Wait for the CRU-238 input-cut result before touching a principle.

**T6. §3.4.3 "What counts as a self model" (l.325): is "its states, its geometry, its capabilities" a conjunction or a list
of examples?** D10's copy carries states only.
- a. Examples: add E10.
- b. Loosen to "its states and, where it has them, its geometry and capabilities".
- c. Keep l.325 as the criterion for the self model that closes at the floor, and count D10's copy as an explicit self
  model below that criterion.

**T7. Boundary recognition as model criterion (3) in Table 1 (l.164).** Ruling (1) names write and readability. In the
crucible instrument MG chose "Write is enough".
- a. Keep three criteria in the theory and drop the boundary test only in the instrument.
- b. Demote it: l.152 already says "*T* fixes the model's boundary", so Table 1 lists boundary recognition as a consequence
  of the target.
- c. Drop it from Table 1.

**T8. "Copy".** l.178 and l.417: explicit models are "generated from the substrate rather than filled by a copy of it".
Ruling (2) and E9: the realistic ESM is "a copy of the actual self".
- a. Keep both. The first denies a copy of stored content, the second affirms a copy of the target, and E9 names the target.
- b. Change l.178/417 to "…rather than filled by a transfer of stored content".
- c. Use another word in E9 (e.g. "a reduced, integrated image of the actual self").

**H1 (hedged hypothesis, no edit proposed): "basic awareness may already arise from non active explicit models without
active closure".** The crucible session found no conflict if awareness means access. The paper, however, says at l.162 and
l.399 that without phenomenology "every term of the family (consciousness, awareness, sentience, self-awareness) is
negative". At l.391 it also says accessible content "is not conscious". So the hypothesis conflicts under either reading
unless MG redefines the term.
- a. Awareness = access inside closure. The paper stays as it is, and the hypothesis is about access only.
- b. Awareness = accessibility outside closure. Then l.162/399 would drop "awareness" from the family.
- c. Awareness = a phenomenal floor without closure. This conflicts with §3.5 (floor = "a rudimentary closure") and
  Principle 3.

**H2 (hedged hypothesis, no edit proposed): "explicit closure might already give rise to a basic reflective self".** §3.5:
the floor has "no reflection" (l.401); at basic consciousness "the self-model is in the loop but does not take itself as an
object" (l.403); reflection appears at the doubly extended rung (l.407).
- a. "Reflective" = the self mirrored in the world model it closes with. No conflict, and one clause at l.401 could say so.
- b. Reflection proper at the floor. This conflicts with l.401, 403 and 407.
- c. Test first and leave §3.5 unchanged until a result exists.
