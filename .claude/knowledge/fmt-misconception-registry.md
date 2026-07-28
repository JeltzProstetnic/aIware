<!-- consumed-by: neuroscience-communication.md (comms rules), didactic-patterns.md (teaching devices), CLAUDE.md (Communication Rules) -->
<!-- updates: none -->
# FMT Misconception Registry — how FMT gets misread, and the preemptions

**Origin (S271, 2026-07-26):** A frontier LLM (Gemini) asked to compare FMT to GWT/GNWT, IIT, HOT produced a recurring cluster of misreadings — each corrected by MG in his own words. The strategic point: **if a capable model defaults to these, so will reviewers, journalists, funders, and other AIs.** FMT prose must preempt them. Grounded against `paper/full/four-model-theory-full.md` (§3.1–3.7, §4.4, §5.1, §8.7–8.9) + MG's verbatim corrections. Feeds AIW-95 (didactic-pattern sweep), the paper's own reviewer-proofing, and v14 framing (AIW-126).

Companion rule already in force: `neuroscience-communication.md` ("two kinds of models, not four modules"). The six misreads below are that same modularism error metastasizing — fix the framing at the source (2×2 of *kinds*) and most of the downstream demands die.

## The six misreadings

### 1. Naïve modularism ("four boxes")
- **Wrong:** four discrete modules / systems / "pillars" — separate boxes in the brain.
- **Correct:** a 2×2 *taxonomy of two model KINDS* across Scope (World/Self) × Mode (Implicit/Explicit) — the *minimum sufficient set*, not the count. Substrate implements "an effectively uncountable number of overlapping models"; the four are "extremal points in a continuous space." The axes aren't symmetric: mode is an orthogonal contrast, scope is a *nesting* (ESM⊆EWM, ISM⊆IWM) — so "four independent boxes" is wrong twice. "A conceptual taxonomy, not a claim about spatial organization" (§3.2).
- **Why seductive:** a 2×2 table *looks* like four cells; LLMs/reviewers pattern-match to Fodorian box-and-arrow cognitive architectures.
- **Preemption:** *"FMT names two KINDS of model along two axes — four extremal poles of one continuous, overlapping modeling ecology — not four modules; four is the floor, not the ceiling."*

### 2. The "data-transfer / information-routing" misframe
- **Wrong:** you need math for "how data transforms from an implicit state (latent weights) into an explicit state (rendering)" — a pipe across a boundary.
- **Correct:** the explicit models are *generated from / constituted by* the substrate — "distinct from that substrate the way any computation is distinct from the hardware that executes it" (§3.1–3.3). MG: *"the implicit state is the machine, the explicit state is the software… the software is MADE FROM the machine data, not the data transferred from the machine into the software."* Constitution, not routing — no transfer step to formalize.
- **Why seductive:** "boundary" + arrows reads as a channel. **FMT's own vocabulary seeds this:** §3.6/Table 1 describe *permeability* as "information transfer across the implicit-explicit boundary" — a legitimately *different* relation (which stored content surfaces into the running sim), but the shared word "transfer" invites collapsing constitution into it.
- **Preemption:** *"The explicit simulation is MADE OF the substrate the way software is constituted by hardware — not fed data across a pipe. Reserve 'transfer' strictly for which implicit content surfaces into the running simulation (permeability), never for how the simulation is generated."*

### 3. Criticality as requirement vs. symptom  → see v14 framing flag below
- **Wrong:** "criticality / edge of chaos / the criticality threshold" is *the* foundational requirement to define and measure.
- **Correct:** the deep requirement is *free compute* — Class-4 (universal-computation) *capability* actually deployed for open-ended, autonomous self-modeling. MG: *"criticality is a symptom of free computation in certain systems. FMT requires FREE COMPUTE, not necessarily criticality."* §3.7.3 already makes it a trichotomy (capability + free instantiation + evolutionary forcing — a Turing-universal laptop is excluded because "nothing drives it to criticality"); §8.9: "the manipulated quantity is Class-4 *capability*… not any single dynamical marker." Criticality is the downstream dynamical *signature* — **and per MG (S271): what free compute looks like in SOME systems, maybe not all.**
- **Why seductive:** the section is *titled* "The Criticality Requirement"; Principle-1/Table-1b lead with "Criticality"; readers reach for the most measurable quantity (σ, DFA-α, avalanche exponents).
- **Preemption:** *"The requirement is FREE COMPUTE — Class-4 capability turned on itself for autonomous self-modeling; criticality (σ≈1) is the observable symptom some substrates show while doing it, not the thing itself."*

### 4. The binding problem, misapplied
- **Wrong:** FMT needs "a formal calculus to verify the four models are bound into a singular loop rather than four separate programs talking."
- **Correct:** the four are poles of *one* shared high-dimensional substrate — no separate things to bind. MG: *"all is taking place in the same neural net, how can four abstract corners of a high-dimensional vector space NOT be bound."* §5.1: binding is "an emergent property of a substrate operating at criticality" — maximal correlation length delivers "binding into a single experiential field… not consistency of that field's contents." FMT *dissolves* binding, doesn't solve it.
- **Why seductive:** binding is a canonical open problem; every theory is expected to post a mechanism — and Misread #1 (boxes) directly generates the demand (separate boxes *would* need binding).
- **Preemption:** *"Binding isn't a problem FMT solves — it's one dissolved: the four poles are corners of a single space, already bound by construction; criticality binds them into one FIELD, not one consistent story."*

### 5. Over-localization (a region-box per model)
- **Wrong:** map all four to discrete regions (EWM=posterior hot zone, ESM=PFC…).
- **Correct:** asymmetric. MG: *"for the implicit two axes [localization is fine], the explicit ones are NOT localizable."* Implicit (IWM/ISM) = *structural*, stored in connectivity (DTI/synaptic-density PET; §3.1.1, Level-4 topological system). Explicit (EWM/ESM) = Level-5 *virtual*: distributed, transient phase-synchronization that "collapse[s] under anesthesia while structural connectivity is preserved"; DMN co-activation is "a neural correlate, not a localization claim" (fn 3). Asking "which region is the EWM?" is a level error.
- **Why seductive:** fMRI culture equates "real" with "localizable"; the IIT-posterior vs GNWT-prefrontal debate primes the same demand of FMT.
- **Preemption:** *"Implicit models localize to structural substrate (image with DTI/PET); explicit models are non-localizable transient dynamics across the whole network — 'which region is the EWM?' is a level error."*

### 6. FMT as an implementation spec (not a theory of what consciousness IS)
- **Wrong:** FMT is an AC engineering blueprint; the natural next move is "implement it in code."
- **Correct:** FMT is a theory of *what consciousness is* — substrate-independent necessary+sufficient architecture (criticality/free-compute + four-model closure). Building a conscious machine is a downstream *implication* (§8.7–8.8), "not currently testable — the engineering does not yet exist"; §8.9 tests component *mechanisms* and "does not attempt to build consciousness." Scaffolded LLM/agent loops are "architectural mimicry, not self-referential closure" (§4.4).
- **Why seductive:** FMT is unusually architectural for a consciousness theory, so it *reads* like a spec; an LLM's competence gradient runs toward "code it." MG had to redirect: *authoring the paper, not implementing AC.*
- **Preemption:** *"FMT states what consciousness IS and what any substrate must satisfy to have it; building one is an unrealized implication, not the theory — and an agent loop with memory is mimicry, not the self-referential closure the theory requires."*

## Communication lessons (durable rules — extend `neuroscience-communication.md`)

a. **Never let "implicit→explicit" read as data transfer.** Say *generated from / constituted by*. Reserve "transfer/surfacing" only for permeability. *(NEW — flags an in-paper hazard: §3.6/Table 1 "information transfer across the boundary" seeds Misread #2; candidate future-edition disambiguation.)*
b. **Lead with "free compute / Class-4 capability," criticality as its symptom.** Don't headline "criticality requirement" unqualified. *(NEW — sharpens §3.7/§8.9 hedge into a default.)*
c. **Binding is dissolved, not solved — say so preemptively** when comparing to IIT/GNWT. *(NEW; pairs with anti-modularism.)*
d. **State the localization asymmetry explicitly** whenever regions come up (implicit=structural/localizable; explicit=distributed/non-localizable). *(NEW.)*
e. **Frame FMT as a theory of what consciousness IS, not a build spec** — especially with AI-literate audiences and other LLMs; put AC in the "implication, not yet buildable" bucket; call scaffolded loops mimicry. *(NEW — this is where LLM interlocutors specifically drift; matters most in AI/tech-press and funder contexts.)*
f. **Reinforce/generalize "two kinds of models, not four modules"** — "four is the floor, not the ceiling" and "extremal poles of one continuous ecology" are the positive replacements. *(REINFORCES the Session-100 rule.)*
g. **When a capable interlocutor "demands the math," first check whether the demand encodes a misread.** Gemini's "transfer calculus" (#2), "criticality threshold" (#3), "binding calculus" (#4) were all artifacts of misreadings — formalizing them would formalize the error. *(NEW — directly relevant to the formalization paper Gruber 2026b: don't let reviewer/AI-generated "missing math" set the agenda uncritically.)*
