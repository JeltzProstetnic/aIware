# Independent coding of FMT's theory map — instructions

Thank you for coding. You are the second coder for Table 1 of *Where the Theories Sit*
(Gruber, 2026; https://doi.org/10.5281/zenodo.23496102). The published verdicts are a single coder's (the
author's); your coding is the agreement check the paper names as missing (§2.6, §7).

**Please code blind: do not read Table 1, Sections 4-5 or Figures 1-3 of the paper before you
have finished.** Everything you need is in this kit and in the FMT master
(https://doi.org/10.5281/zenodo.18669891, latest version) and the claim file `fmt-claims.json`.

## What to fill in (`coding-sheet.csv`)

One row per rival claim. For each row:

- `component` — the FMT component code(s) the claim is about (table below; §2.2 rule).
- `verdict` — exactly one of A, C, N, X (rules below).
- `containing_fmt_claim` — for A only: the `fmt-claims.json` id(s) that contain the claim.
- `note` — optional; anything that made the call hard, or a disagreement with the claim's wording.

The `claim` column states the rival theory's claim in one line; the `source` column gives
the works it was taken from. If you think a claim misstates its theory, say so in `note`
and code the claim as the theory states it.

## Coding rules (from §2 of the paper)

### 2.1 Atomic claims

An atomic claim is a single subject–predicate–object statement that a theory's proponents assert and that can be true or false independently of the theory's other claims. "A state is conscious if and only if it is the target of a suitable higher-order representation" is one atomic claim; "an empty higher-order representation suffices for experience" is a second. Each claim is assigned a type: definition, principle, bridging commitment, consequence, mechanism, prediction, or falsifier. Two theories can share a mechanism and disagree on whether it is constitutive of experience; separating claims by type keeps the agreement and the disagreement both visible.

### 2.2 Placement

Each claim is placed on the component of the reference architecture that it is about: a claim about global broadcast on the component that carries content between the stored and running levels, a claim identifying experience with a cause-effect structure at the level of phenomenal ontology. Placement depends on subject matter, not on whether the reference theory agrees.

### 2.3 Verdicts

Each placed claim receives one of four verdicts relative to the reference theory's own claim about the same component.

- **A — absorbed.** The reference theory contains the claim, as a component, a mechanism, or an implementation of one of its components.
- **C — compatible.** The reference theory does not contain the claim, and the claim does not conflict with anything the reference theory asserts.
- **N — neutral.** The reference theory takes no position on the claim.
- **X — contradicts.** The claim and the reference theory's claim about that component cannot both be true.

A theory usually receives several verdicts, one per claim. An A verdict names the reference-theory claim that contains the rival claim, so that the containment can be checked against the supplementary file. A claim that the reference theory restates in its own vocabulary without containing it is not absorbed. The verdicts in this paper are a single coder's, the author's; no second coder has yet coded Table 1.

## The reference frame (§3 of the paper)

## 3. The Reference Frame

FMT rests on three principles (Gruber, 2026a, §3).

1. **Open-ended computation allows free modelling.** The system must be able to compute in the regime capable of universal computation (Wolfram's Class 4) and must recruit that capability for its own modelling. Free modelling is necessary and not sufficient for consciousness. In neural tissue it usually shows as near-critical dynamics. Near-criticality is a signature of free modelling in some substrates, at some task sizes. It is neither necessary nor sufficient for consciousness, and a conscious system may run subcritically (§3.7, Table 1).
2. **Recurrent non-linear dynamics of sufficient complexity host a second computational level**: persistent activity patterns that interact and compute over one another, individuated by their mutual effects (§3.3).
3. **Phenomenology is real and physical, and it is that level's modelling closed on itself**: the self-model and the world-model each enter the other's update rule (§3.4). The principle is an identity: phenomenality is closure. This is the theory's single bridging commitment. It is argued for and not derived (§3.4.3).

From these follows a minimum architecture of two kinds of model along two axes (§3.2). Mode separates implicit models, stored in substrate connectivity, from explicit models, generated as running processes. Scope separates the world from the self, and is a nesting: the self-model's content is part of the world-model's. The four extremal poles are the implicit world model (IWM), implicit self model (ISM), explicit world model (EWM) and explicit self model (ESM). Four is the floor; the substrate implements an effectively uncountable number of overlapping models around these poles. The explicit models are generated from the implicit models and current input. They are not filled by a copy of stored content (§3.6). Free modelling and the architecture are each necessary and neither is sufficient. What suffices is a conjunction: the four model kinds under closure, with free compute, embodiment and at least one pain-pleasure axis, which may be engineered (§3.7.3, §4.4).

The components used as coordinates below are:

| Code | Component | Source |
|---|---|---|
| RV | Real/virtual split: implicit models are stored structure and never directly conscious; explicit models are running processes | §3.3 |
| VQ | Virtual qualia: phenomenal properties are real at the computational level and incoherent at the substrate level | §3.4.1–3.4.2 |
| CL | Self-referential closure: the self-model and world-model enter each other's update rule | §3.4.3 |
| TE | Temporal echo: recursion under closure produces experienced temporal flow | §3.4.4 |
| LAD | Graded ladder: minimal, basic, simply, doubly and triply extended consciousness by richness and depth of recursive self-modelling | §3.5 |
| PERM | Permeability: how readily stored content is drawn into the running models, a family of local and global boundary properties | §3.6 |
| CH | Channel: the low-rank path through which explicit models read and write implicit ones; its occupancy is working memory (*Arbeitsmodell*) | §3.6.1 |
| FM | Free modelling: Class-4 capability, free instantiation and autonomous recruitment; criticality as its signature in some brains | §3.7, §3.7.3 |
| L1–L5 | Five-system hierarchy: physical, electrochemical, proteomic, topological (implicit models), virtual (explicit models) | §3.7.1 |
| MP | Meta-problem: the ESM cannot model its own generating substrate | §3.8 |
| SI | Substrate independence: the sufficient conjunction (four model kinds under closure, free compute, embodiment, at least one pain-pleasure axis) suffices on any substrate | §3.7.3, §4.4 |

Three features of the frame govern the verdicts. First, for content in the running simulation, access and phenomenality are two level-descriptions of one process; content that is only accessible, poised for report without being in use, is preconscious: it is stored on the implicit side or held in an explicit model outside the self-model's closed loop, and it becomes conscious on entering that loop (§3.4.6; Dehaene et al., 2006). Added recursive depth converts content that is present into content that is reportable, with no separate broadcast stage (§3.4.6). Second, the ladder starts below basic consciousness. Minimal consciousness is a rudimentary closure of the explicit world and self models whose content is the present moment, with no reflection and no discernible qualia; basic consciousness adds discernible content at the same depth of recursion. Both are phenomenal without first-order self-observation, and awareness that one experiences arrives at the first extended rung (§3.5). Third, FMT's claims about what closure buys a system are claims about one architecture's closure and its efficiency under a resource bound, not claims about what is barred to systems without it (§4.4). Opening a closed loop in a recurrent system tends to relocate closure, leaving two or more smaller closed systems where one stood (§4.4, §8.12).
