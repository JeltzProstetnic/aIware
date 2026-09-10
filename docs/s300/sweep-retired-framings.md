# S300 Sweep — Retired Framings Still Live in the FMT Master

**Scope:** `paper/full/four-model-theory-full.md`, audited in full (all 1545 lines of body prose read; references skimmed) against `didactic-patterns.md`, `fmt-misconception-registry.md`, `awareness-consciousness-terminology.md`, `fmt-2015-definitions.md`, `prediction-framing.md`, and `docs/decisions.md` (S277–S299 entries). Defect class per the S299 handover: places where the paper still says something the project has since decided it no longer says.

**⚠ State audited:** the WORKING TREE as of 2026-08-10 ~22:55, NOT HEAD. The master was edited by the live S300 session *during* this audit (uncommitted +8 lines: the pattern-37 "unrepresentable apparatus" upgrade to §4.2.2 and the readout-vs-causal-power paragraph in §4.2.3). All line numbers below are working-tree numbers at 22:55 and will drift as v15 editing continues — **locate targets by the quoted text, not the line number.**

---

## Summary table

| # | Line(s) | What it says now | What the project has since decided | Decision source | Severity | Confidence |
|---|---|---|---|---|---|---|
| 1 | 578 (§4.2.3) | "…the simulation-forking and variable-permeability operations of **Principles 4–5**" | FMT is THREE principles; forking and permeability are demoted to consequences (derived in §6.0) | `didactic-patterns.md` lines 763–769 (AIW-138, MG-settled 2026-08-03); `docs/decisions.md` S282 (line 627) + S286 v14 application (line 994); the paper's own lines 134–140 and §6.0 | **Severe** (internal contradiction; a structure the theory no longer has) | **High** |
| 2 | 590 (§4.2.4, first sentence) | "…confers a specific adaptive advantage **that no simpler system can replicate**" | Capability language must be PRICE, never BARRIER; "the theory claims no operation that unconscious processing is barred from" — stated by the paper itself two paragraphs later (line 592) | `didactic-patterns.md` lines 738–758 (MG S299, AIW-193: two instances "found live in the FMT master… on 2026-08-10" and repaired — this is a surviving sibling) | **Severe** (a claim the theory no longer makes, contradicted within its own subsection) | **High** |
| 2b | 590 (§4.2.4, last clause) | "…a capacity that **requires an explicit world model** capable of categorical abstraction" | Axis (A) of the same S299 discipline: no capability barrier may be asserted between implicit/unconscious and explicit/conscious processing | Same source as #2 | Moderate | **Medium** (see intent note below) |
| 3 | 509, 512 (§3.7.3) | Bullet headlined "**Computational prerequisite: Criticality**"; "Both thresholds must be met. **Criticality is necessary** but not sufficient" — stated substrate-neutrally | The requirement is Class-4 capability / free compute; criticality is its signature *in neural tissue*, "in SOME systems, maybe not all" (MG S271). Don't headline "criticality requirement" unqualified. | `fmt-misconception-registry.md` misread #3 + lesson (b) ("Rule stands for all other prose"); the paper's own Table 1 Criticality entry (line 174), §3.7 opening (line 437), §8.9 (line 965) | Minor (labeling residue; content beneath the label is correct) | **Medium** |

No other instances of the S299 known-dead framings exist in the master — see "Confirmed clean" below.

---

## Finding 1 — "Principles 4–5" (line 578) — SEVERE, HIGH CONFIDENCE

**Paper text (exact):**
> "In the *inward* mode the running self-simulation is the necessary medium for reality-decoupled processing: attentional redirection, mental imagery, counterfactual simulation, and the simulation-forking and variable-permeability operations of Principles 4–5."

**The decision that retires it (exact):** `didactic-patterns.md` (Cautions section):
> "**FMT is THREE principles, not five (`AIW-138`, MG-settled 2026-08-03):** … The four model kinds, redirection onto the non-self, variable permeability and simulation forking all demote to **consequences with explanatory power**."

The restructure was applied to the paper in v14 (decisions.md, S286 2026-08-05: "FMT v14 three-principle restructure applied"). The paper itself now states three principles at lines 17, 70, 134–140, and §6.0 (line 692) explicitly derives forking and permeability as consequences, not principles. There are no Principles 4–5 anywhere else in the paper — this is the single surviving reference to the retired five-principle numbering, and a reviewer who follows it finds nothing.

**Proposed replacement (direct substitution):**
> "…attentional redirection, mental imagery, counterfactual simulation, and the simulation-forking and variable-permeability mechanisms derived in Section 6.0."

Simple substitution; no re-cut needed.

---

## Finding 2 — "no simpler system can replicate" (line 590) — SEVERE, HIGH CONFIDENCE

**Paper text (exact, §4.2.4 opening sentence):**
> "The four-model architecture confers a specific adaptive advantage that no simpler system can replicate: it enables **cognitive learning** — the induction of general theories from particular observations…"

**The decision that retires it (exact):** `didactic-patterns.md`, MG verbatim 2026-08-10 (S299):
> "we have to be careful about capability necessity stuff concerning self model and consciousness because there is probably nothing the self model can do that the world model cant… a capability unconscious processing cannot replicate should not be possible i think."
> "**The licensed form on every axis is PRICE, never BARRIER**."

The same registry entry records: "**Found live in the FMT master twice on 2026-08-10** — §4.2.4 asserted a capability *'unconscious processing — however sophisticated — cannot replicate'* … repaired to cost framing." The repair rewrote the paragraph at line 592 — which now says, in the paper's own voice: *"the advantage is one of cost, not of possibility. The theory claims no operation that unconscious processing is barred from"* and *"not that it unlocks the otherwise impossible."* But the **topic sentence of the subsection at line 590 still asserts the barrier** ("no simpler system can replicate"), so §4.2.4 currently contradicts itself between its first and second paragraphs. This is precisely the "sibling" the S299 handover predicted.

**Proposed replacement (direct substitution for the opening clause):**
> "The four-model architecture confers a specific adaptive advantage — one of cost rather than of possibility, in a sense made precise below: it supports **cognitive learning** — the induction of general theories from particular observations…"

**Finding 2b (same paragraph, last clause), MEDIUM confidence.** The paragraph ends: "…a capacity that requires an explicit world model capable of categorical abstraction." Read literally, "requires" is a barrier claim on axis (A) (implicit vs. explicit) of the same S299 discipline. It is *defensible* as an internal-architecture statement (within FMT, categorical abstraction over novel instances is an explicit-model operation by definition), which is why this is flagged rather than asserted — I am partly guessing at intent. If edited, the price form would be:
> "…a capacity the explicit world model's categorical abstraction supplies cheaply, where a system without one must pay for each instance separately."

Recommend MG (or the v15 session applying member (h)'s logic) rules on 2b rather than auto-applying.

---

## Finding 3 — §3.7.3 headlines "Criticality" as the prerequisite (lines 509, 512) — MINOR, MEDIUM CONFIDENCE

**Paper text (exact):**
> "- **Computational prerequisite**: Criticality. The virtual system must exhibit Class 4 dynamics…"
> "Both thresholds must be met. Criticality is necessary but not sufficient; the four-model architecture is necessary but not sufficient. Together they are sufficient."

**The decision it lags:** `fmt-misconception-registry.md` misread #3 (MG S271: "criticality is a symptom of free computation in certain systems. FMT requires FREE COMPUTE, not necessarily criticality") and lesson (b): "Lead with 'free compute / Class-4 capability,' criticality as its symptom. Don't headline 'criticality requirement' unqualified. (**APPLIED in v14**… Rule stands for all other prose.)"

The v14 fix retitled §3.7 and rewrote Table 1's Criticality entry ("The signature, in neural tissue, of the computational regime the theory requires"), and §3.7's own opening (line 437) says "the commitment is then better stated as Class 4 *capability*." §3.7.3 is the one remaining place that uses bare "Criticality" as the substrate-neutral *name* of the prerequisite. The content directly under the label is correct (it immediately unpacks as open-ended computation / Class 4), so this is a labeling residue, not a wrong claim — hence minor. It is nonetheless the exact headline pattern lesson (b) bans, and Table 1's definition makes the paper's own vocabulary inconsistent with it (by Table 1, "criticality" cannot be the substrate-neutral prerequisite, because Table 1 defines it as the *biological* signature).

**Proposed replacement:**
> "- **Computational prerequisite**: Class 4 capability. The virtual system must be able to compute open-endedly — the regime whose signature in neural tissue is criticality (Section 3.7)…"
> and at line 512: "Both thresholds must be met. The Class 4 regime is necessary but not sufficient; the four-model architecture is necessary but not sufficient. Together they are sufficient."

Confidence is medium, not high: the shorthand may be deliberate (the section already carries the capability-first trichotomy two paragraphs down), and §3.7.3 is heavily cross-referenced (§8.9 line 973 cites "the trichotomy of Section 3.7.3"). If edited, keep the trichotomy text untouched — only the two labels move.

---

## ⚠ NOT findings — deferred or already-applied items the next session must not mistake for defects

**a. §4.2.3's two-causal-roles structure is PENDING A RE-CUT, deliberately deferred — DO NOT "fix" it now, and DO NOT attempt a rename.** The S299 decision (decisions.md, "the two causal pathways are named"): the settled names are **DREAMING** (short-term) and **MATURING** (long-term), and *"these are a re-cut of the two causal roles, not a rename of them. §4.2.3's outward role is self-model → substrate → behaviour → environment over developmental time; the carving is substrate plasticity driven by usage. The two overlap but are not the same division, so §4.2.3 requires restructuring rather than a terminology pass — and that work is deliberately not started, because MG's dreaming hypothesis may change the shape again."* The conceptual difference, stated so nobody find-and-replaces: §4.2.3's outward/inward axis divides by **where the causal chain terminates** (environment vs. own simulation); DREAMING/MATURING divides by **timescale of effect** (offline replay-and-recombine that reads stored quale-values into plans, vs. usage-driven long-term plasticity — the groove). Both new routes go *outward first*, so mapping outward→MATURING / inward→DREAMING is wrong on both ends. Tracked: AIW-202. Additional traps recorded in `didactic-patterns.md` (pattern 35/36 block): timescale must be stated explicitly; path length runs opposite to timescale; both names need first-use glosses (dreaming covers daydreaming — one kind, two regimes; maturing ≠ biological maturation).

**b. Pattern 37 and the readout/causal-power distinction were applied to the working tree DURING this audit** (uncommitted at time of writing): §4.2.2 gained the "unrepresentable apparatus" account (scope-guarded to phenomenology, physics question declined — matches the S299 scope guard) and §4.2.3 gained "Readout and causal power are different relations" (the AIW-202 dashboard-vs-dreaming line). Both insertions are consistent with the S299 rulings as recorded. Do not re-add them.

**c. Pattern 36 (the weather-simulation discriminator vs. PP) is a pending v15 ADDITION to §7.2's PP entry, not a retired framing.** The current PP entry (line ~835) is the scope-limited/complementary account the registry calls "correct but defensive." Note for the applying session: §3.4.3 Stage 1 already uses the weather simulation, so the discriminator has a natural in-paper anchor.

**d. The capability-null / "zero compute" / "self-relational increment" vocabulary does not appear in the master at all** — it is S299 v15-drafting vocabulary. Nothing stale to remove; the correction ("the null sits on the self-relational increment, not at the closure locus") constrains only *future* member drafting.

---

## Fact-class disagreements (paper vs. knowledge file on a fact, not a framing)

**F1. Which ictal route is dominant — LOW-MODERATE CONFIDENCE, flag for verification, not for editing.**
- Paper §10.3 (line 1044): generalized tonic-clonic seizures exit Class 4 "**typically by pathological hypersynchrony** and, **in some recordings**, by supercritical avalanche dynamics at onset and spread… (Meisel et al., 2012)."
- `didactic-patterns.md` (Cautions, pattern-4 correction): "the dynamical mechanism is **supercritical + complexity-collapse**, NOT 'ordered/synchronous Class-2.' Hypersynchrony is the *correlate*… Reconcile route-independently: 'exit from Class-4 (**dominant route supercritical**)…'"

The two agree on the theory-level invariant (route-independent Class-4 exit — the paper states this explicitly, so the theory claim is safe either way) but **disagree on which empirical route dominates**: the paper makes hypersynchrony typical and supercriticality occasional; the knowledge file makes supercriticality dominant and hypersynchrony a correlate. One of the two should be corrected against Meisel et al. 2012 (and the wider ictal-criticality literature) — and it is genuinely possible the *knowledge file's* shorthand is the wrong one, since the paper's hedged wording reads like it was written against the primary source. Do not edit the paper on the knowledge file's authority alone.

**F2. Checked and consistent (no action):** PCI threshold 0.31 and Casarotto et al. (2016) sensitivity figures (100% benchmark, 94.7% MCS) are identical in Table 1, §3.7, and §8.1 and match the knowledge base. The §3.6 regress argument matches the S285/S288 ruling exactly (knowledge requires a reference system, not consciousness — the paper states "the regress is consciousness-free throughout"). The 2015 consciousness definition (line 144/160) matches the verbatim 2015 rendering. "Originally yielded nine predictions (Gruber, 2015)" (line 875) is not contradicted by `prediction-framing.md` (whose 8→9→4 history describes the *paper's* revisions; the book's own count is unrecorded in the KB) — not reportable.

---

## Confirmed clean — every other S299 handover item, checked and negative

| Checked for | Result |
|---|---|
| "the reading" / "the carving" as pathway names | **Absent.** Never entered the paper (grep, whole file). DREAMING/MATURING also absent — the §4.2.3 re-cut has not been started, per (a) above. |
| "zero compute" / "zero compute residue" / "capability-null at the closure locus" | **Absent** (grep: "zero.compute", "null", "residue", "increment", "closure locus" — only unrelated hits, e.g. "accumulated residue of the system's history" line 227, a different sense). |
| Spontaneous-"I" gate | **Corrected form live** at line 338 (§3.4.3): the theory *declines* the spontaneity criterion, two reasons given, replaced by naturalistic label acquisition under ablation control (member (g)). No sibling instance of a spontaneity gate elsewhere; all other "spontaneous" hits are retinal firing / spontaneous behavior literature. |
| Absolute capability claims (member (h) siblings) | **Two residues found** — Findings 2 and 2b. The repaired instances at lines 580 and 592 are confirmed live and correct ("emphatically NOT the claim that some capability is barred…"; "no operation that unconscious processing is barred from"). §4.4's scoping rule (line 624), §4.2.5's "Generality" + budget paragraphs (598–608 region), and §8.9's NFL discipline (line 971: "closure necessity… has been falsified five times in this program") are all in the licensed price/budget form. |
| ESM/EWM usage vs. the S299 axis discipline | Line 592 carries the no-difference point in the paper's own voice ("no operation that the self-model performs and the world-model could not"). No contrary assertion found anywhere else. |
| "Closure enables what feedforward cannot" (withdrawn crucible framing) | **Absent.** §8.9 line 963 states the NFL concession explicitly. |
| Advantage scaling on recursion depth (withdrawn, axis-corrected to richness) | **Absent.** Recursion depth appears only as the access/presence mechanism (line 380) and the §3.5 ladder — both legitimate, distinct uses. Advantage claims run on redeployment/cost. |
| Mirror neurons as support (pattern #30 discipline) | **Absent.** No mirror-neuron citation in the paper. |
| One-directional criticality (S277 banned constructions: only/iff/selectively deployed/tracks) | **Compliant.** Lines 174, 437 state "one way only… never the converse"; Table 1b says "Necessary, not sufficient; one-directional"; the near-critical-but-unconscious sleep case is accommodated (line 437). No banned construction found. |
| Misread #2 (transfer-across-boundary) | **v14 fix confirmed live**: §3.6 (line 400) and Table 1 "Becomes conscious" (line 176) carry generated-from + transfer-as-shorthand-for-permeability. |
| Pattern 32 (holography misattribution) | **Clean**, re-confirmed: §5.2 attributes distributed storage to the implicit models and states the explicit models are processes, not stored structures (matches the S297 check recorded in the registry). |
| "Four modules" modularism / fixed model counts | **Clean**: "four model kinds rather than four modules" (abstract), "four is the floor, not the ceiling" (lines 17, 225), nesting-not-orthogonal stated (line 206). |
| "Awareness" as felt-floor (pattern 33 terminology trap) | **No violation**: "awareness" appears only in defensible senses (covert awareness — clinical term of art; self-awareness; lucid awareness). The optional folding-in of "sentience" for the felt floor (terminology file's recommendation) has not been done — that is pending optional work, not a defect. |
| Five-principles structure | One residue — Finding 1. All other statements (lines 17, 70, 134–140, 686–694) are three-principle form. |
| S269 dropped banked positive #1 (closure-maintenance) | **Confirmed dropped**: §8.9's banked list starts with the planner result; the closure-maintenance recursion-specific result is not claimed. |

---

*Audited by the S300 sweep subagent (Fable), 2026-08-10 late evening. Method: full body read of the working-tree master + targeted greps for each dead framing + cross-read of all six named knowledge/decision files. Adversarial-false-positive policy applied: candidate hits on "both at their maxima" (line 646 — qualified by "ordinarily"/"rarely" and the C_N convergence-credit paragraph satisfies the pattern-5 caution), seizure Class-2/3 phrasing in §3.7 (line 482 — route-independent commitment stated in the same paragraph), and the §8 numbered-prediction structure (survived multiple MG-reviewed published revisions; the prediction-framing lessons are already embodied in §8's illustration/convergence split) were examined and NOT reported as findings.*
