<!-- Action: reference -->
<!-- Tracked-by: AIW-278, AIW-279 -->
# How the FMT definition fares under Definitions A's C1–C9 (S334, 2026-10-17)

Opus assessment, read-only, at MG's request ("how does the fmt definition fare by this standard?"). Definition
assessed: the 2015 sentence + free modelling (Principle 1) + closure (Principle 3), per Definitions B §4.5; the
master's own wording is scored too. Sources: Definitions A, Definitions B, `fmt-2015-derivation-check.md`, master
§3, §3.1–3.6, §3.8, §4.4, §6.4 (v19 draft), S334 decisions, misconception registry, CT explainer.

**Housekeeping first:** Definitions B §2/§9 uses *different* criteria under the same labels C1–C5 (B: C3 substrate
neutrality, C4 gradedness, C5 report independence; A: C3 operationalisation, C4 substrate neutrality, C5
discrimination of contested cases). B scores FMT on its own easier set and never runs A's C3, C5 or C6–C9.

## Verdicts

| | FMT | PCI (A §7.2) |
|---|---|---|
| C1 non-circularity | **Partly.** 2015 noun clean (p.57–59), regress base stated (p.21; master §3.6). But master Table 1 "Consciousness" cell puts the definiendum in the definition ("has phenomenology or has none…"); §3.1 opens with "the capacity for subjective experience"; §3.5 levels are written in phenomenal vocabulary. By A's own attention-schema parity, "model", "non-trivial", "free" are theory-laden. | premise has no consciousness terms |
| C2 grounding | **Partly.** Data→information→knowledge→interpretation→model chain grounded. Ungrounded: "nicht-trivial", "free/autonomous" deployment (§3.7.3), Class 4 (no decision procedure for a finite physical system), and what makes a component a *self*-model and not mere recurrence (CT explainer: "Every RNN has it"; D2 is a proposal). | well defined |
| C3 operationalisation | **Fails for non-reporters.** Master Table 1 observable is PCI > 0.31 (report-calibrated); closure "deliberately omitted from Table 1" (§3.1.1); free-modelling probe is a weak necessity test any generalising learner passes; §4.4's "measurable on the system itself" contradicts §3.1.1. Unused asset: white-box inspection of the update graph (D1 δ, D2). | met for humans |
| C4 substrate neutrality | **Partly.** Definiens neutral. Machine verdicts rest on unmeasured regime claims (LLMs "not Class 4", autonomous vs heteronomous); markers a machine passes are reclassified as "marker drift" (heads/tails); "persistent implicit models" sits awkwardly with §3.6 (weights are a base layer). | premise neutral, procedure cortex-bound |
| C5 discrimination | **Partly.** Verdicts and deciding fact stated (closure + free modelling; deep sleep probably out, fish/amphibians minimal, insects possibly, LLMs no). No route to establishing the fact in a non-reporter: §6.4 "evidence can only be indirect" with no method; the floor is unreportable by definition, exactly where contested cases live; serial awakening cannot tell floor from absence; Table 4 up-state models vs "probably unconscious". | met for contested humans |
| C6 stated bridge | **Partly — stated, better than most of Table 1.** Principle 3 is "the single bridging commitment… argued for rather than derived". Weak: identity or law? ("arises exactly where" vs "is"); B identifies the *capacity*, Principle 3 the *running closure*; the falsifier runs through report-calibrated markers; §4.4's relocation argument ("opening a loop relocates it") is the PCI defect written into the theory; §3.4.5 concedes nothing empirical separates FMT realism from strong illusionism. Natural answer not yet used: in-silico full closure-off ablation as the test of the premise. | stated; premise falsifier not separated |
| C7 uncontested cases | **Partly/disputed.** Process reading classifies right. Capacity reading puts deep sleep and anaesthesia in (B's own 2×2), and master Table 1 says both "capacity" and "process". Over-inclusion: an EKF-SLAM robot vacuum (pose and map update each other, beats a lookup) passes the stated tests; which closure applies at the floor is unstated. | met by calibration |
| C8 explains the pointer | **Meets — FMT's strongest condition.** Presence-for-someone/privacy (§3.4.3), ineffability (§3.4.2), explanatory gap/meta-problem via ESM–ISM near-opacity (§3.8), reportability with recursion (§3.4.6). Does not discriminate from AST/illusionism (§3.4.5 concedes possible relabelling). | outside scope |
| C9 creature/state/capacity | **Partly.** B splits Bewusstsein/Bewusstheit; D2c gives the state level; two axes give the creature level. Master still merges capacity and process; Paper A footnote advertises "a capacity definition". | one sense only |

## Gaps FMT must close (with where)
1. **Capacity vs process** — master Table 1 cell and §3.1: split Bewusstsein/Bewusstheit; Principle 3 identifies
   phenomenality with the process; say which one "consciousness" names; move the one-gate sentence out of the
   Definition cell into a note (consequence of Principle 3). Fix Paper A's footnote. Closes C7 contradiction, C9.
   (= pending decision 8.)
2. **Self-model criterion and floor closure** — D2 criterion (lossy component tracking the system's dynamics
   including itself, lower capacity than the whole) into §3.4.3 and the §3.5 minimal-consciousness entry; state
   whether the floor needs self-tracking or only mutual update; rule on the SLAM robot; observable for "autonomous
   deployment" (§3.7.3). Closes C2, part of C7, C4.
3. **Procedure for non-reporters** — new Table 1b row: white-box architectural audit (D1 δ + D2) for artificial
   systems; concrete indirect evidence for animals (§6.4); back or delete §4.4's "measurable on the system itself".
   Closes C3, C5.
4. **Bridge falsifier separate from markers** — §3.4.3 and B §6: identity or law; in-silico full closure-off
   ablation as the test of the premise (no relocation possible by construction); concede in §4.4 that in-vivo
   disruption tests markers, not the premise. Closes C6.
5. **Floor vs absence; deep sleep** — non-report signature for the floor (δ finite vs broken; closure in
   up-states); reconcile up-state explicit models with "probably unconscious"; drop or recast serial awakening.
   Closes C5 at the floor.
Housekeeping: Definitions B uses A's C1–C9 and scores FMT openly, fails included.

## Verdict in plain words
FMT beats Nagel, Block and IIT's axioms on two counts: it states its bridge, and it is the only formulation
examined that tries to explain why there seems to be something it is like (C8). But it fails or half-meets the
conditions the paper says matter most: no decision procedure of its own for an unresponsive patient, an insect or
a machine (its operational criterion is PCI); its exclusion terms lack application conditions; its bridge is
shielded by its own relocation argument; its floor is unreportable with no signature; the master calls
consciousness both capacity and process. **FMT names the deciding fact for contested cases but cannot yet measure
it — on this paper's standard: stated, not met.** Sent as is, a reader applying C3 and C5 to FMT will find FMT
failing the paper's own test.

## The FMT footnote in Paper A
Current: "I defend a capacity definition of consciousness elsewhere (Gruber, 2015; Gruber, in preparation)." Honest
as a statement, misleading by implication (capacity vs the master's "process"; implies FMT is the remedy; cited
title does not match B's actual title "Deriving a Definition of Consciousness from Reference Systems").
Suggested replacement (use the middle clause only once the master adopts the split; until then cite B for it):
> The Four-Model Theory (Gruber, 2015; Gruber, in preparation) defines consciousness as a capacity for
> self-modelling, distinguishes that capacity from the ongoing process of running a self-model, and identifies
> phenomenality with the process. By conditions C1 to C9, its definiens uses no consciousness terms and its bridge
> premise is stated; it does not yet give a decision procedure for systems that do not report, so C3 and C5
> remain unmet.
