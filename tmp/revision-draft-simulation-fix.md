# Revision Draft: Sharpening "Simulation" and Hard Problem Dissolution

Addresses Andrillon's NCONSC-2026-051 feedback:
- "simulation" needs sharper definition
- unclear how it dissolves the hard problem

Based on Matthias's clarifications:
1. "Simulation" is pedagogical shorthand — brain generates unified narrative, not a digital twin
2. Hard problem dissolves via category error (qualia = digital constructs at different computing level), NOT via calling things "simulation"
3. Substrate vs. computation distinction is universal (every ML system has it) — "simulation" doesn't establish it

---

## EDIT 1: New paragraph after line 120 (after Core Definition)

INSERT after "What it requires is a system capable of constructing and maintaining a self-referential simulation in real time."

> A clarification on terminology is warranted. "Self-simulation" is a pedagogical shorthand, not a claim that the brain operates like a digital twin replicating reality in a continuous, deterministic loop. What the brain generates is something more like a unified narrative: a more or less linear, relatively contradiction-free story of the organism's current situation — past, present, and anticipated future — assembled from fragmentary substrate-level knowledge and current sensory input. This narrative is neither continuously updated nor strictly linear; it is constructed on the fly, revised where it fails, and filled with interpolations, simplifications, and outright confabulations. The term "simulation" is retained because it captures the essential architectural feature: the explicit models are *generated processes* running on a structural substrate, distinct from that substrate in the way any computation is distinct from the hardware that executes it. This substrate-computation distinction is not a philosophical claim unique to consciousness — it holds for every computing system, from spreadsheets to neural networks. What is unique to consciousness is not the distinction itself but what happens at the computational level: *self-referential closure*, the fact that the system's generated model includes a model of the system generating the model (see Section 3.4).

---

## EDIT 2: Restructured Section 3.4 (replaces lines 160-178)

### 3.4 Virtual Qualia: Dissolving the Hard Problem

Every computing system — from a laptop running a spreadsheet to a neural network training on data — inherently distinguishes between a physical substrate and the computational processes running on it. This is not a philosophical claim; it is an engineering truism. The substrate (transistors, synaptic weights, connectivity patterns) supports and constrains the computation, but the computational level has properties that are incoherent at the substrate level: a spreadsheet cell "contains a sum," but no transistor contains a sum. This level distinction is universal and uncontroversial.

The central claim of the Four-Model Theory is that **qualia are constitutive properties of the computational level**. They are the way the generated self-model (ESM) registers its own states and the generated world-model (EWM). Qualia are, in this precise sense, digital constructs — patterns that exist at the level of the running computation and that are incoherent at the substrate level, just as "cell A1 contains the sum of column B" is incoherent at the level of transistor states.

This dissolves the Hard Problem by revealing a **category error** — specifically, a **level confusion** — in its formulation:

**The standard formulation**: "Why does physical processing (neuronal firing, synaptic transmission) feel like something?"

**The dissolution**: It does not. The IWM and ISM — the substrate-level implicit models — operate without any phenomenal character whatsoever. There is nothing it is like to be a synaptic weight. Qualia are not missing from the substrate; they are the wrong kind of property to seek there. They exist at the computational level — at Level 5 of the five-system hierarchy (Section 3.7.1) — where they are not mysterious but constitutive. Asking why neuronal firing feels like something is analogous to asking why transistor switching "is" a spreadsheet. The transistors are not the spreadsheet; they generate and sustain it. The neurons are not the experience; they generate and sustain the computational process in which experience is constitutive. Within the explicit models, "redness" is simply the ESM's mode of registering a particular class of EWM content — no more mysterious than "cell A1 contains 42" is mysterious to a spreadsheet user, despite being nowhere in the transistors.

**Why self-referential computation specifically?** A critic might object: spreadsheets and weather simulations also run at a higher computational level than their substrates — why don't they have qualia? The answer lies in **self-referential closure**. A weather simulation models weather; it does not model *itself modeling weather*. The four-model architecture creates a closed loop: the ESM is the system modeling its own modeling process. In this loop, the distinction between the model and the modeled collapses — the computation *is* the thing being computed. Qualia are not an *addition* to the self-modeling; they are the self-modeling as encountered from the inside of the loop. A non-self-referential computation has an outside from which it can be described without remainder; a self-referential computation at criticality has no such outside. The computation *is* its own observer, and observation-from-inside is what we call experience.

This is not a proof that self-referential computation must be conscious — it is an argument that self-referential computation is the *kind* of process for which the Hard Problem's assumptions break down. Self-referential closure is precisely the condition under which the gap between process and feeling does not exist.

This is **not** illusionism in the sense of Dennett (1991) or Frankish (2016); nor is it compatible with deflationary accounts (Graziano, 2024). Illusionism holds that qualia as traditionally conceived are illusions — there is nothing it is like, and our sense that there is something it is like is itself a misrepresentation. The Four-Model Theory holds that qualia are *real at the computational level*. Within the EWM/ESM, experience has genuine phenomenal character. What is illusory is the assumption that this phenomenal character must be a property of the physical substrate. It is not. It is a property of the computational process that the substrate runs.

This constitutes a **two-level ontology**: the substrate level (real side) has no experience, and the computational level (virtual side) has genuine experience. Both levels are physical — the computation is a physical process, not a supernatural one — but they have different ontological properties. The category error in the Hard Problem consists in conflating the two levels: seeking phenomenal properties at the substrate level where they do not exist.

The Explanatory Gap closes simultaneously. The gap between "neurons fire in pattern X" and "I experience red" is not a gap in our knowledge but a reflection of the level distinction. The neural firing pattern generates and sustains the computation in which redness is experienced, but the firing pattern itself is not red and does not experience redness, just as a CPU's electrical states are not "a spreadsheet" even though they generate and sustain one.

---

## EDIT 3: Terminology changes (mechanical, apply after approval of 1+2)

| Line | Current | Proposed |
|------|---------|----------|
| 1 (title) | "A Simulation-Based Framework" | Keep or change to "A Computational-Level Framework"? |
| 124 | "explicit/simulated" | "explicit/generated" |
| 131 | "Explicit (simulated, phenomenal)" | "Explicit (generated, phenomenal)" |
| 137 | "real-time simulation of reality" | "real-time construction of a unified scene from sensory and stored data" |
| 139 | "real-time simulation of 'I'" | "real-time generation of a unified self-narrative" |
| 149 | "simulated, transient, generated" | "generated, transient" (drop "simulated" — redundant with "generated") |
| 153 | "nature as simulations rather than structures" | "nature as generated processes rather than stored structures" |
| 631 | "simulate consciousness" | "imitate consciousness" (different sense of "simulate" — clarify) |

Downstream uses of "simulation" (dreams, propofol, permeability, etc.) should read correctly once the definition in 3.1 and the restructured 3.4 are in place. No changes needed there.

---

## What changed structurally in Section 3.4

OLD order: (1) qualia are virtual → (2) category error asserted → (3) simulation doesn't feel, simulation does → (4) self-referential closure as anticipated objection → (5) not illusionism → (6) two-level ontology → (7) explanatory gap

NEW order: (1) substrate/computation distinction is universal and trivial → (2) qualia are constitutive of computational level (digital constructs) → (3) category error = level confusion → (4) self-referential closure as PRIMARY argument for why THIS computation has experience → (5) not a proof → (6) not illusionism → (7) two-level ontology → (8) explanatory gap

Key moves:
- "Every computing system has this distinction" → defuses "you're just inventing a distinction by calling it simulation"
- "Digital constructs at a different computing level" → actual dissolution mechanism, not the word "simulation"
- Self-referential closure promoted from "anticipated objection" to primary argument
- "simulation" replaced with "computation" throughout 3.4 where it refers to the level distinction
