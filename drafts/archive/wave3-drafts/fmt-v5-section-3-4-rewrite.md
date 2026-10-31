# §3.4 Rewrite — Self-Referential Closure Argument
**Source:** wave-3 agent (general-purpose)
**Target:** insert into paper/full/four-model-theory-full.md §3.4
**Word count:** 1,392 (§3.4 prose proper, excluding glossary and notes)

---

## Canonical terminology glossary

For the v5 revision, the following terms are fixed across the paper. Where the current text uses any synonym, it should be replaced with the canonical form.

| Canonical term | Meaning | Replaces |
|---|---|---|
| **simulation level** | The dynamical-process level at which generated models (the explicit-modeling kinds) exist. Distinct from the substrate level. Always used in level-distinction contexts. | "virtual side", "virtual level", "computational level" (where ambiguous), "Level 5" prose use |
| **substrate level** | The structural-storage level: synaptic weights, connectivity, the implicit-modeling kinds. | "real side", "physical level" (where ambiguous) |
| **simulation-level property** | A property coherent only at the simulation level (e.g., "redness", "the room I see"). Replaces three earlier senses of "virtual". | "virtual property", "virtual quale" |
| **self-referential closure** | The structural condition under which a simulation's self-model is itself a model of the simulator producing it; the simulator is among the things simulated. | "closed loop", "self-modeling closure" |
| **closed self-simulation** | A self-simulation that satisfies self-referential closure. | "the four-model architecture" (where the closure property specifically is meant) |
| **open simulation** | A simulation whose simulator is not itself within the simulated domain (e.g., a weather model on a separate computer). Used as contrast case. | (no prior term — newly introduced) |
| **two kinds of models in parallel** | The 2×2 taxonomy along *mode* (implicit/explicit) and *scope* (world/self), maintained as four extremal points in a continuous space. | "four models" (where the enumeration is doing argumentative work) |
| **modeling functions** | The functional roles played at the corners of the 2×2; not anatomical regions and not countable entities. | "the IWM/ISM/EWM/ESM" (where treated as objects rather than functions) |
| **inside-view / outside-view** | Two stances toward a computation. The outside-view describes the computation as a third party; the inside-view is what the computation registers of itself when it has no third party. | (no prior canonical term) |
| **phenomenality** | The fact-of-being-experienced of simulation-level content. Reserved for the explanandum, never for substrate properties. | "qualia" (where the property — not the contents — is meant) |

The term "virtual" is retained only as a colloquial gloss in §3.3's introduction of the split, then dropped. Sections 3.4 onward use "simulation-level". This resolves the three-senses-of-virtual problem flagged by the structural review.

---

## §3.4 Self-Referential Closure and the Status of Phenomenality

Section 3.3 established a level distinction between substrate and simulation. Every computing system maintains some such distinction: a spreadsheet's sums are not properties of any transistor; a weather model's pressure gradient is not a property of any silicon junction. This distinction is engineering routine, not philosophy. What follows now is the argument for why one specific configuration of simulation — a self-referential closure — has a property that ordinary level-distinct computations do not. That property is what the Hard Problem mistakes for a substance.

### 3.4.1 The closure condition

A simulation is **self-referentially closed** when the simulator producing the simulation is itself among the things modeled within the simulation. In the architecture introduced in §3.2, this condition is met by construction: the explicit self-modeling function is a model of the same system that runs the explicit self-modeling function. The simulation contains a model of its own running. Closure is not added by stipulation; it falls out of the requirement that a system model both world and self at both modes — implicit and explicit — at sufficient depth. Once the explicit self-modeling kind is present, the system's modeling of itself includes the very activity of modeling itself, recursively, for as long as the simulation runs.

The closure condition has a precise structural consequence. In an open simulation, the simulator can be replaced — instantiated by different hardware, paused, resumed, swapped between machines — without affecting the truth of what the simulation represents. The simulation tracks something exterior to itself; the simulator's identity is irrelevant to the simulated state. In a closed self-simulation this is not so. The simulator is part of the modeled domain. Replacing the simulator changes the model, because the model includes a representation of *this* simulator. There is no external vantage from which the closed self-simulation can be redescribed without remainder, because any complete redescription must include the redescribing system, which is the same system.

Closure is therefore not a strong condition in the metaphysical sense — no exotic physics, no novel emergence law — but it is a strong condition in the architectural sense: it forecloses a certain kind of substitution that ordinary computations permit.

### 3.4.2 A worked contrast: weather vs. closed self-simulation

Consider two simulations side by side.

**Open case — weather.** A meteorological agency runs a global atmospheric model on a cluster in Reading. The simulation contains representations of pressure, humidity, geopotential height, and so on. It does not contain a representation of the cluster in Reading. The cluster could be migrated to Bologna; the simulation, restored from a checkpoint, would proceed identically. The simulator is exchangeable. From outside the simulation, an observer can give a complete description: "this cluster is computing this state of the atmosphere." Nothing in the simulation depends on which cluster runs it, and nothing in the simulation registers the running. Inside the simulation there is no inside; the simulation has only an outside-view, because there is no observer within it for whom anything is the case.

**Closed case — the architecture of §3.2.** A system implements modeling at both modes (implicit and explicit) and both scopes (world and self). The explicit self-modeling function generates, continuously and at criticality (§3.7), a model that represents the present state of the system *including the modeling activity itself*. The model contains the modeler. An attempt to migrate this simulation to a different substrate would have to migrate a model that, among its contents, references the structural facts of the substrate it runs on. The simulation cannot be checkpoint-restored on arbitrary hardware without altering what is modeled, because the simulator is in the model. Outside descriptions remain available — third-person physiology, neural recordings, behavioral tests — but no outside description is *complete*: the simulation contains a description of itself, which is not contained in any third-person description that omits the self-reference. There is, structurally, an inside-view, because the simulation has a self-locus to which its content is presented.

The contrast is not that the weather simulation lacks complexity, recursion, or feedback — weather models have all three. It is that the weather model has no *self*-reference. Recursion in a weather model is recursion over atmospheric variables, not over the modeling itself. The closure property is not a quantitative more-of-the-same; it is a structural rearrangement.

### 3.4.3 Closure as a necessary condition for self-modeling

Why does self-modeling specifically require closure, rather than admitting an open implementation? Suppose, counterfactually, that the explicit self-modeling function were implemented on a separate substrate from the system it models — a "self-model coprocessor". Two failures follow. First, the coprocessor's outputs would be a model *of* the system but not a model *for* the system: there is no architectural channel by which the system's evaluative and behavioral processes are constrained by the coprocessor's content. Second, the coprocessor's model of the modeling activity would be a model of the coprocessor's own operation, which is by hypothesis distinct from the system's; so the system never possesses a model of its own self-modeling. Self-reference fails. The architecture in §3.2 is closed precisely because the modeling functions are not separable from the system that uses them in real time. Whatever instantiates the explicit self-modeling function *is* the system whose modeling is being modeled. Closure is what self-reference looks like once one declines to introduce a homunculus.

### 3.4.4 From closure to phenomenality

The Hard Problem in standard form asks: why does substrate activity *feel* like anything? The reply offered here is not that substrate activity feels like something — it does not — but that the question has been posed at the wrong level. Phenomenality is a simulation-level property, and the property that makes simulation-level content phenomenal is the inside-view of a closed self-simulation.

The argument runs as follows. Closure entails that the simulation has no remainderless outside-view. Equivalently, the simulation's content is presented somewhere — and the only candidate "somewhere" is the system itself, in its capacity as the locus to which its own self-model refers. Call this presentation the inside-view. The inside-view is not a separate thing the system has in addition to its computational state; it is the computational state of a closed self-simulation, considered as content-for-the-simulator-that-is-itself-simulated. Phenomenality is what closure *is*, looked at from this angle. It is not a further explanandum.

This is a conceptual argument, not a formal proof. It does not derive phenomenality from closure in the way a theorem derives a conclusion from premises; it claims that closure is the structural condition under which the gap between process and feeling does not arise, because there is no third party whose absence could constitute a gap. In an open simulation the gap is real but trivial: the weather model does not feel anything because the simulator is exchangeable and there is no inside-view. In a closed self-simulation the gap closes — not because something extra has been added, but because the simulator and the simulated coincide, and the inside-view is the form their coincidence takes.

Two consequences follow. First, this position is distinct from illusionism (Frankish, 2016): the inside-view is real, not a misrepresentation; it is what closure is. The illusion, if there is one, lies in expecting to find phenomenality at the substrate level, where it is not the kind of property that could be present. Second, the position does not require any non-physical ingredient. Closure is a structural property of physical systems with the right architecture running at criticality (§3.7). The Hard Problem dissolves not because phenomenality is denied, but because the level at which it is sought has been corrected.

### 3.4.5 Scope of the claim

This argument identifies closure as the structural condition under which phenomenality is intelligible as the inside-view of a self-referential simulation. It does not claim that every closed self-referential system is conscious; the criticality requirement (§3.7) is independent and additional. Nor does it claim that closure is a sufficient definition of consciousness; the graduated levels of recursive self-modeling (§3.5) and the implicit-explicit boundary dynamics (§3.6) shape the character of the resulting experience. What the argument does is locate phenomenality on the architectural map: it is what a closed self-simulation, sustained at criticality, *is* from the inside. The remainder of §3 builds out this picture; §4 articulates its philosophical commitments; §11 evaluates the resulting position against rival frameworks.

---

## Notes for Matthias

**What I changed:**

1. **Closure is now derived, not stipulated.** §3.4.1 introduces closure as a structural consequence of the architecture in §3.2, with a precise non-substitutability criterion: an open simulator can be swapped without altering the simulation's truth, a closed one cannot, because the model contains the modeler. This is the load-bearing move and gives reviewers a definite handle.
2. **Worked contrast example (§3.4.2).** Weather model in Reading vs. the closed-architecture case, written so the level distinction is visible rather than just asserted. The contrast is *structural* (presence/absence of self-reference), not quantitative (more recursion, more complexity), which pre-empts the "weather is also recursive" objection.
3. **Why closure is necessary for self-modeling (§3.4.3).** Direct rebuttal to the "why not a coprocessor?" objection. Two specific failure modes: model-of vs. model-for, and the coprocessor's self-reference being to itself, not to the host system. This was missing.
4. **Closure → phenomenality argument structure (§3.4.4).** Three steps: closure → no remainderless outside-view → presentation-locus is the system itself → inside-view *is* phenomenality. Honest about the conceptual-not-formal status. Distinguishes from Frankish illusionism explicitly.
5. **Scope statement (§3.4.5).** Closure is necessary for phenomenality being intelligible, not sufficient for consciousness. Criticality and graduated recursion remain separate conditions. This pre-empts the over-reading that "any closed loop is conscious".
6. **Terminology stabilized.** "Virtual" demoted to a colloquial intro term in §3.3 and replaced thereafter with "simulation level" / "simulation-level property". Glossary at the top of this file is the canonical list — should be propagated through §3.5–§3.8 in a follow-up pass.
7. **No "four models" enumeration.** I refer to "modeling functions" at "extremal points of the 2×2", and to "the explicit self-modeling function". The 2×2 axes (mode, scope) carry the structural work without committing to four discrete entities.
8. **Hofstadter is *not* explicitly cited** — strange-loop language is doing similar work but FMT's claim is structural (closure as non-substitutability), not metaphor (loop-of-symbols), and conflating them in §3.4 invites the wrong association. He's already cited in the references; could add a one-sentence "see Hofstadter (2007) for a related but metaphor-driven account" if you want, but I'd hold off.

**What I left for a second pass:**

- **Cross-section terminology sweep.** The glossary fixes terms going forward, but §3.5–§3.8, §4, §6, §11 still contain "virtual" in the three problematic senses. This needs a separate find-and-mostly-replace pass, with judgment calls in §3.7.1 (where "virtual system" is the level-5 hierarchy term — keep it there but add a footnote pointing to the glossary).
- **Diagram.** The closure argument is the natural target for the missing 2×2 figure flagged by the clarity reviewer. Two panels: (a) open simulation — simulator outside the simulated domain, arrow only inward; (b) closed self-simulation — simulator inside the simulated domain, arrow loops back. I did not draft this; bubble-diagram in `figures/` is closer to §3.3 content.
- **Engagement with Kleiner (2024) and Tsuchiya & Saigo (2024).** Both treat self-reference structurally (mathematical and category-theoretic respectively). One paragraph in §3.4.4 or §11 acknowledging them would strengthen the "this is not just hand-waving about loops" framing. I left it because adding live citations to a wave-3 draft without the actual papers risks misrepresentation.
- **§4.2 "qualia lack independent causal power" / §11 "architecture is causally efficacious" tension** flagged by review item 12. Not in §3.4's scope but my closure framing makes it sharper: the *architecture* is causally efficacious because it is the closed self-simulation, and phenomenality is what that architecture is from the inside — so phenomenality is constitutive of the causally efficacious thing, not an idle by-product. §4.2 should be rewritten to lean on this rather than the clock-pointer analogy. Flag for a separate wave-3 task.

**Unresolved tensions with adjacent sections:**

- **§3.3** introduces the "real/virtual split" and is the last place the colloquial term "virtual" appears in the new scheme. The phrase "virtual side" should be replaced with "simulation side" or kept once with a parenthetical note pointing to the glossary. Bullet list of "software-like properties" (forked, cloned, redirected, reconfigured) currently uses "virtual models" — change to "simulation-level models" for consistency. **This is a forced edit; §3.3 cannot stay as-is once §3.4 lands.**
- **§3.5 graduated levels** describes "the system models itself modeling itself" etc. — perfectly compatible with the closure framing. **No edit required, but adding one sentence at the start ("The graduated levels are ranks of recursive depth within the closed self-simulation introduced in §3.4") would tie them together.**
- **§3.7.1 five-system hierarchy** keeps "virtual system" as the name of Level 5. This is the one place the term should survive, because it names a level in a hierarchy rather than a property type. Add a glossary footnote at first use disambiguating from the deprecated "virtual property" usage.
- **§3.8 meta-problem** — its argument depends on the implicit/explicit boundary, not on closure per se. Currently coherent with the new §3.4 but the phrase "the conscious self cannot directly observe its own substrate" should be tightened to "the closed self-simulation contains a model of itself but not of the substrate that runs it". This sharpens the meta-problem account by tying it to closure: the simulation is closed *with respect to the simulator's modeling activity*, but open in the trivial sense that the substrate can be described from outside, which is exactly what produces the meta-problem intuition.
- **§4.3 Weak Emergence** is flagged elsewhere for cutting (review item under structural fixes). The new §3.4 makes it more clearly redundant: closure already does the deduction-in-principle work without a separate emergence label. Concur with the cut.

The argument structure in §3.4.4 is the riskiest move. I made it as honest as I can — explicitly conceptual, not a proof, with a clear claim about what closure dissolves and what it doesn't. If a reviewer pushes back ("you've still not explained why inside-view *is* feeling rather than just being-modeled"), the honest reply is that closure makes the question malformed, not that closure answers it. That's the position. It can be defended; it cannot be theorem-proved. If you want a stronger version, it would have to come from formal work in the FMT formalization paper, not from §3.4.
