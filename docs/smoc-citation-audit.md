<!-- Action: act -->
<!-- Tracked-by: AIW-146 (the chart), AIW-27 (web deployment, gated on this) -->
<!-- updates: docs/smoc-middle-layer-draft.md, figures/smoc-philosophy-map.svg -->
# SMoC citation audit — every agreement mark, verified or downgraded

**Opened S288 (2026-08-06) on MG's "5. do it".** This is candidate **A** from the S285 handover: the
prerequisite to everything public. Every *agreed* and *converging* mark on the chart is currently the
session's judgement, and several placements are of theories whose authors will be in the room at MoC7.

**Why it gates:** the chart's entire claim to be infrastructure rather than advocacy rests on the marking
being honest (§0.2 — *"a chart that silently marks FMT-only cells as agreed is a manifesto, and the field will
read it as one in about four seconds"*). One over-claimed *agreed* costs more than ten blanks.

**Status after S289 (2026-08-06):** the **argument map is done — 11 of 11 placements sourced** to primary text,
with the sources printed on the figure (§3). One placement moved (`Biological naturalism`, F14). The **rung
chart still has ~11 cells at ⧗ NEEDS PRIMARY** (§1b end) — that is the remaining audit surface.

---

## 0. Scope, counted

| Mark | Count | Audit obligation |
|---|---|---|
| **agreed** | 17 | **Must verify** — the strongest claim on the chart |
| **converging** | 18 | **Must verify** — needs ≥2 *independent* theories positing something equivalent |
| disputed | 6 | Verify the dispute is real and both sides are correctly stated |
| FMT-only | 16 | No external citation needed — but verify nothing else already says it (a missed convergence is as bad as a false one) |
| blank | 3 | Verify nobody has in fact answered it |

Two of the 35 agreed/converging hits are the §0.2 legend rows, not cells → **33 real cells to verify**, plus
every placement in `figures/smoc-philosophy-map.svg`.

**Verification bar, per the project's own citation rule:** title, authors, venue and DOI checked against a
primary source before any mark stands. **Honest-convergence framing is mandatory** — "consistent with", never
priority, and state what the cited work actually argues rather than what it can be read as supporting.

---

## 1. Findings so far

### F1 — `S3` was both mis-marked and out of date. **FIXED S288.**

Marked **agreed**, but it conflated two different things: the *unrolling mathematics* (genuinely agreed) with
*the chart's own discipline rule* about how to phrase closure claims (which is not a field-consensus claim
about consciousness at all). Worse, its content was superseded the same day by MG's scope limit on the
No-Free-Lunch correction — it stated the efficiency framing unconditionally, which over-applies an ML result
to biological intelligence.

**Rewritten** to scope efficiency to the fixed-task/unbounded-budget lane and permit capability claims in the
budget-bounded biological lane, with the subject being the whole architecture rather than closure alone.
Mark split: **agreed** (the unrolling maths) / **FMT-only** (the budget-relative reading).

*Class of error to watch for in the rest of the audit: **a selection rule is not a field claim.** S1–S8 describe
what the chart forbids. Where a rule embeds a mathematical or empirical result, only that result can carry an
`agreed`; the rule itself cannot.*

### ⚠ METHOD CORRECTION (S288) — read this before trusting any finding below

**The first scan reported only the *first* mark on each row, so cells that were already correctly split read as
single-marked.** Two of the five AT-RISK findings were therefore **false positives against a chart that was
already right**, and a third was half wrong. Corrected by re-scanning for multiple marks per row.

**Five cells were already split and need no action:** `Governor` (agreed + FMT-only), `M9` Free modelling
(converging + FMT-only), **`M10`** (converging on structure + disputed on role — *exactly* what F3
"recommended"), **`S2`** (FMT-only for the constraint + converging for **the correlation** — *exactly* what F2
"recommended"), and `S3` (agreed + FMT-only).

**Corrected tally for the AT-RISK pass: 2 real defects, 2 false positives, 1 half-right.**

| Finding | Verdict |
|---|---|
| **F1 `S3`** | **half right.** The *marking* was already split — that half of the finding was wrong. The *content* was genuinely stale after MG's NFL scope limit, and the rewrite stands on that ground alone. |
| **F2 `S2`** | ❌ **FALSE POSITIVE.** Already reads *FMT-only (the constraint) / converging (the correlation)*. No action. |
| **F3 `M10`** | ❌ **FALSE POSITIVE.** Already reads *converging (the structure) / disputed (its role)*. No action. |
| **F5 `§3.1` information** | ✅ **REAL.** Was unqualified `converging`. Downgraded to `disputed`. |
| **F6 LLM row** | ✅ **REAL.** `R2` was asserted flat. Now contested, and the `R4 no` justification tightened. |

**This correction matters more than the findings.** The chart's entire claim is that its marking is honest; an
audit that inflates its own catch rate would be the same failure one level up. The chart was in better shape
than the first pass said — **and the real audit surface is 29 single-marked cells, not 33.**

**Standing method rule for the remaining pass: parse every mark on a row before judging it, and read the
qualifier in parentheses.** The parenthetical is where the honesty already lives.

---

### AT-RISK PASS — verdicts (as corrected above)

Sources used are those already primary-verified for the FMT paper in **S256** (Beggs & Plenz 2003;
Priesemann et al. 2014; Hardstone et al. 2012; Touboul & Destexhe 2017; Algom & Shriki 2026; Hengen & Shew
2025 — the last two were explicitly cleared of the "possibly fabricated" flag in that pass). Claims marked
**⧗ NEEDS PRIMARY** below are ones I did **not** re-verify this session and which must be checked before the
mark ships.

### F2 — `S2` (criticality) almost certainly over-marked. **RECOMMEND SPLIT.**

Marked **FMT-only** (the constraint) / **converging**. The convergence is real for *one* proposition and not
for the other, and the cell currently blurs them:

- *"Cortex operates near a critical regime"* — **converging** is defensible (Beggs & Plenz 2003; Priesemann
  et al. 2014; Hardstone et al. 2012).
- *"Criticality is necessary for consciousness"* — **not converging.** This is contested, and the FMT paper
  itself carries the caveat (Touboul & Destexhe 2017: non-critical processes produce apparent power laws;
  exponents vary by area and method).

**Recommended:** split into two cells, marking the first *converging* and the second **disputed**. Marking the
necessity claim as converging is the single most likely thing to be caught by a hostile reader, because the
literature it would rest on explicitly declines to say it.

### F3 — `M10` (Workspace = the Bottleneck's occupancy) is an FMT identification, not a convergence.

Marked **converging**. But this is precisely the claim `A4` was written to put to the room — GNWT makes global
broadcast *constitutive*; FMT makes it the *channel*. A global-workspace theorist would sign the structure and
reject the role. Marking it converging asserts agreement on the very point under dispute.

**Recommended:** **converging** on the structure, **disputed** on the role — or demote whole to **FMT-only**.
This is the cell where honest marking buys the most credibility, because conceding it is what makes A4 read as
good faith rather than a takedown.

**VERDICT (S288): confirmed — split into structure and role.** GNWT's claim is that global broadcast/ignition
is **constitutive** of conscious access (Baars 1988; Dehaene & Changeux 2011; Mashour et al. 2020 — ⧗ **NEEDS
PRIMARY** for exact wording before quoting). FMT's `M10` says the workspace *is* the Bottleneck's occupancy and
its role is **channel, not constitution**. Those are not the same claim in different vocabulary; they are the
disagreement itself. A single `converging` mark therefore asserts consensus precisely where there is none, and
it would be read as such by the largest camp in the field within seconds.
**Action:** **converging** on the *structure* (both theories posit a low-capacity bottleneck through which
conscious content passes — this really is independent convergence, and FMT has had one since 2015 in the
*Arbeitsmodell*), **disputed** on the *role* (constitutive vs channel). **Do not demote to FMT-only** — that
would throw away a real convergence and make the chart look defensive. The split *is* the honest mark, and it
is also the exact shape of question **A4**, so the chart and the MoC7 question end up saying the same thing,
which is what a coordinate system is supposed to do.

### F4 — `M4` / `R5` (redeployment) — convergence is real but must be sourced correctly.

Simulation theory of mind (Goldman) and the mental-time-travel / self-projection literature (Buckner & Carroll
2007; Suddendorf & Corballis) do converge on *modelling others by re-running one's own model*. **VERIFY as
primaries.** ⚠ **Do not cite mirror neurons** — didactic pattern **#30**, MG-directed: the interpretation is
disputed along the exact axis FMT cares about, so it hands a hostile reviewer the first thing to attack and
buys nothing that pattern #29 does not already give.

**VERDICT (S288): confirmed over-marked — split it.** The corroborating citations support *"cortex operates in
a slightly subcritical regime"* and nothing stronger. The FMT paper's own §8.9 states the damaging fact
outright: in a leaky echo-state network **memory and computation co-peak in the *ordered* regime**, so σ = 1 is
not where general computation lives — which means even the *within-substrate* story is more qualified than a
`converging` mark implies. Marking the necessity claim as converging asserts agreement that its own sources
decline to give.
**Action:** two cells. *"Cortex operates near criticality"* → **converging** (Beggs & Plenz 2003; Priesemann
2014; Hardstone 2012). *"Criticality is necessary for consciousness"* → **disputed**, with Touboul & Destexhe
2017 named on the sceptical side. The one-directional constraint (¬crit → ¬consc) stays **FMT-only**.

### F5 — `§3.1` information cell: FMT takes a side in a live dispute and does not say so. **DOWNGRADE.**

Marked **converging**, glossed *"this is the layer Shannon and physics work in, where reversibility is the
whole game."* The problem is not the gloss — it is what the definition **omits**. FMT defines information as
*differentiable phenomena to which a coding can be assigned*: **alethically neutral**, no truth condition.
Floridi's General Definition of Information runs the other way, requiring **truthfulness** (the *veridicality
thesis*) — and that thesis is contested rather than settled, with Fetzer, Scarantino & Piccinini and others on
the neutral side. ⧗ **NEEDS PRIMARY** for each of those attributions before they are named in print.

So the cell is not *converging on a settled definition*; it is **FMT joining one camp of an open dispute in the
philosophy of information**. Marking that `converging` is exactly the failure mode §0.2 warns about.
**Action:** → **disputed**, with FMT's alethic neutrality stated as a position taken rather than a fact
reported.

**⚠ And this is load-bearing beyond the cell, which is why it is worth the trouble:** FMT's whole ladder
—`Wissen ist Information, die einem Bezugssystem zugeordnet ist`, with **no truth condition** — is only
coherent under alethic neutrality. So the **§3.1 information cell and the knowledge cell stand or fall
together**, and both connect to the S288 truth work: *falsity is a within-system-against-input relation, not a
precondition on what counts as information.* Stating the commitment openly is stronger than letting a reader
discover FMT quietly assumed it. **Also resolves the tension flagged when this cell was opened** — the chart
can call information science deficient *and* cite it honestly, because the deficiency claim is about its
missing theory of **models**, which is a different axis from the veridicality dispute.

### F6 — the LLM row: two separate over-claims. **REWRITE.**

`R2; **R3 contested; R4 no**` — the draft already predicts this is the row that gets argued about, and it is
currently wrong in *both* directions.

**(a) `R2` is asserted flat, but it is contested.** R2 requires an explicit world model *runnable offline and
re-pointable at the non-present*. Whether LLMs have world models at all is a live dispute — probing results on
the one side, stochastic-parrot and shortcut-learning critiques on the other. ⧗ **NEEDS PRIMARY** both ways.
Asserting R2 unqualified concedes to one camp on the chart's face, and it is the concession a hostile reader
will pick up first, because it is the *generous* reading of LLMs sitting right next to a `R4 no`. **→ mark R2
contested as well.**

**(b) The `R4 no` justification is right but too loosely stated.** *"No persistent return into its own update
rule between episodes"* invites three easy counters — in-context learning, retrieval/memory scaffolds, and
fine-tuning loops. The defensible form names the level: **no weight-level return generated by the system's own
modelling; between-episode updates are externally authored, not self-produced.** In-context state is *running*,
not *wired*, and dies with the context; a retrieval store is an external artefact, not the model's own update
rule. Stated that way the claim survives all three counters — and it keeps the row consistent with the
Wired/Running register naming settled this session.

**Action:** `R2 contested; R3 contested; R4 no (weight-level, self-generated)` — and put the three counters in
the note, pre-empted, rather than waiting to be hit with them in Copenhagen.

---

## 1b. NEEDS-PRIMARY PASS (S288) — six citations verified live, all six hold

Each checked this session for title / authors / venue / year / DOI against a primary or publisher record.
**All six survive; no mark in this group needs downgrading.** Four are **new to the project** — absent from
`docs/references.md` — and must be added there before the marks ship.

| Cell | Citation | Verdict | In `references.md`? |
|---|---|---|---|
| **M4 / R5** Redeployment | **Buckner, R.L. & Carroll, D.C. (2007).** "Self-projection and the brain." *Trends in Cognitive Sciences* **11**(2), 49–57. DOI `10.1016/j.tics.2006.11.004` | ✅ **converging CONFIRMED** | ❌ **add** |
| **M4 / R5** Redeployment | **Goldman, A.I. (2006).** *Simulating Minds: The Philosophy, Psychology, and Neuroscience of Mindreading.* Oxford University Press. ISBN 978-0195138924 | ✅ **converging CONFIRMED** | ❌ **add** |
| **M1** Explicitation | **Dehaene, S. & Changeux, J.-P. (2011).** "Experimental and Theoretical Approaches to Conscious Processing." *Neuron* **70**(2), 200–227. DOI `10.1016/j.neuron.2011.03.018` | ✅ **converging CONFIRMED** | ✅ present |
| **M6** Permeability | **Schartner, M.M., Carhart-Harris, R.L., Barrett, A.B., Seth, A.K. & Muthukumaraswamy, S.D. (2017).** "Increased spontaneous MEG signal diversity for psychoactive doses of ketamine, LSD and psilocybin." *Scientific Reports* **7**, 46421. DOI `10.1038/srep46421` | ✅ **converging CONFIRMED** | ✅ present |
| **M6** Permeability (5D-ASC) | **Studerus, E., Gamma, A. & Vollenweider, F.X. (2010).** "Psychometric Evaluation of the Altered States of Consciousness Rating Scale (OAV)." *PLoS ONE* **5**(8), e12412. DOI `10.1371/journal.pone.0012412` | ✅ confirmed — **⚠ with a naming correction, below** | ❌ **add** |
| **R2** Explicit world model | **Safron, A. (2020).** "An Integrated World Modeling Theory (IWMT) of Consciousness…" *Frontiers in Artificial Intelligence* **3**, 30. DOI `10.3389/frai.2020.00030` | ✅ **converging CONFIRMED** | ❌ **add** |

### F7 — `M4`/`R5` redeployment now clears the convergence bar properly. **KEEP the mark.**

The bar is *two or more **independent** theories positing something equivalent in different vocabulary*, and
this now meets it from two directions that do not share a method: **Goldman** from philosophy/psychology
(mindreading by putting oneself in the other's mental shoes) and **Buckner & Carroll** from systems
neuroscience (prospection, autobiographical memory, theory of mind and navigation recruit a **common core
network** — "we mentally project ourselves into that alternative situation"). One theory plus FMT would not
have been convergence; these two are. ✅ And note the constraint held: **neither citation is a mirror-neuron
claim**, so didactic pattern **#30** is satisfied without effort.

### F8 — ⚠ `M6`'s 5D-ASC reference is misnamed. **FIX THE LABEL, KEEP THE MARK.**

The chart cites "5D-ASC". The citable 2010 paper is titled ***Psychometric Evaluation of the Altered States of
Consciousness Rating Scale (**OAV**)*** — OAV and 5D-ASC are the same instrument lineage (APZ → OAV →
5D-ASC), but citing "5D-ASC (Studerus et al. 2010)" misnames the source. **Cite the OAV paper by its actual
title**, and use "5D-ASC" only as the instrument's common name. Small, but it is exactly the class of error the
project's own citation rule exists to catch.

### F9 — `M6`'s evidence is *consistent-with*, not a test. **SCOPE THE CLAIM.**

Schartner et al. show **signal diversity rises** under three psychedelics. That is consistent with permeability
modulation; it does **not** test the Gate, and no measure in that paper is a permeability measure. Per the
honest-convergence rule the cell must say what the paper actually establishes. **`converging` stands — but the
note must read "consistent with", never "confirms".**

### F10 — `R2` picked up a second, unplanned use.

Safron's IWMT is *explicitly* a synthesis of IIT + GNWT under FEP/active inference, which makes it unusually
strong support for a **converging** mark on the explicit-world-model rung — it is itself a convergence claim.
It is also the primary already owed to **`AIW-119`** (the Safron/IWMT convergence note), so verifying it here
discharges part of that item too. Worth noting the overlap rather than verifying it twice.

### Still ⧗ NEEDS PRIMARY after this pass

`R3` Self as object (Metzinger SMT — 2 hits already in `references.md`, verify the specific claim rather than
the author) · `R7` Identified (Damasio core/extended — 1 hit, same) · `M9` Free modelling · the three component
roles `Model Space` / `Bottleneck` / `Gate` · plus the four attributions flagged in F5/F3 (Floridi and the
alethic-neutrality opponents; GNWT's exact constitutive wording if quoted).

## 2. Worklist — the 33 cells

Grouped by risk. **AT RISK** = the mark is probably wrong and the audit's job is to downgrade it.
**NEEDS PRIMARY** = plausible, but no citation is attached yet. **LIKELY SAFE** = verify quickly, expect to keep.

| Group | Cells |
|---|---|
| **AT RISK** | `S2` criticality-necessity · `M10` workspace role · `§3.1` data/information · LLM row · `S3` *(fixed, F1)* |
| **NEEDS PRIMARY** | `M1` Explicitation (ignition/P3b — Dehaene) · `M4`+`R5` Redeployment (Goldman; Buckner & Carroll) · `M6` Permeability (LZ under psychedelics — Schartner 2017; 5D-ASC) · `M9` Free modelling · `R2` Explicit world model (world-model traditions, IWMT, model-based RL) · `R3` Self as object (SMT/Metzinger, Damasio, self-representationalism) · `R7` Identified (Damasio extended) · `Model Space` · `Bottleneck` · `Gate` |
| **LIKELY SAFE** | `M5` Consolidation (systems consolidation) · `Aperture` (sensory gating) · `Governor` (homeostatic regulation) · `Scribe` · `R0` Reactive · `R1` Implicit modelling · `Wired World (IWM)` *(note: correctly scoped already — "agreed **that unconscious learned world-knowledge exists**", a model of how to scope a mark)* · `Running World/Self` · thermostat/R0 · *C. elegans*/R1 · feedforward CNN/R1 · model-based RL/R2 · human infant→adult · `S4` regulated-variable · `S6` kinds-not-modules · `S7` role-not-lump · `S8` parsimony-not-circularity |

## 2b. ARGUMENT-MAP PASS (S288) — one structural fix, three cells flagged, zero citations found

### ⚠ A third scanning false alarm, and now it is a pattern worth naming

The first read of the map judged the placements from the extracted `POS` tuples and **had the two axes
swapped** — assuming `(substrate, residue)` when the source is `(outside-ness, substrate)`. On that reading
half the map looked wrong, including a supposed contradiction between FMT's plotted position and its own
caption. **Reading `scripts/build_philosophy_map.py` dissolved all of it.**

**That is the third time in this session** that judging an artifact from extracted fragments produced a false
finding (mark-scan first-match ×2, now axis orientation). **Standing rule, added to the method: read the
source that generates an artifact before auditing the artifact.** An audit whose own error rate is this high
is worse than none, because its retractions are not visible to the reader of the chart.

### The placements hold up. Six spot-checked against what the positions actually claim:

| Position | Plotted (outside, substrate) | Verdict |
|---|---|---|
| **FMT** | 0.16, 0.58 | ✅ **small residue + middle substrate — exactly what the caption claims.** The suspected caption/position contradiction was the axis error, not a defect. |
| **IIT** | 0.33, 0.78 | ✅ small residue (axioms→postulates purport to explain phenomenality) + high substrate (specific causal structure; excludes feedforward and digital simulation). Consistent with `moc7-questions.md` A3's "IIT almost nothing [outside]". |
| **Property dualism** | 0.91, 0.24 | ✅ **right, and for a non-obvious reason** — high residue with *low* substrate constraint is correct because Chalmers' **organizational invariance** principle explicitly holds that substrate does not matter. A reviewer who expects dualism high on both axes is the one who is wrong. |
| **Illusionism** | 0.05, 0.18 | ✅ residue ≈ 0 by construction; functionalist. |
| **Mysterianism** | 0.96, 0.62 | ✅ maximal residue (cognitive closure). |
| **Biological naturalism** | 0.48, 0.94 | ⚠ substrate maximal ✅ (Searle: caused by and realised in brain biology), but **residue 0.48 is arguable** — Searle holds consciousness is a biological phenomenon, ontologically subjective yet causally explicable, so by his own account he leaves less outside than the midpoint. |

### F11 — **the reading convention was undeclared. This was the map's real defect. FIXED.**

`Global workspace` sits at outside = 0.15 — which is GNWT **as GNWT describes itself**. Block's
access/phenomenal critique would put the same theory at the far right of the same axis. **Without a declared
convention every placement is ambiguous, and any proponent can say "you have misread me" about any point.**

**Fixed on the figure itself:** *"Every position is plotted as the theory describes ITSELF, never as its
critics read it — for the workspace family those readings differ by most of the x-axis."* Applied uniformly,
and stated in the build script's docstring so it survives the next edit.

This is the highest-value change in the map pass. It is the difference between a chart people **argue with**
and one they **dismiss** — and it costs nothing, because declaring the convention is also the most generous
possible reading of every rival on the map.

### F12 — `Panpsychism` (0.86, 0.52) is the weakest cell: the substrate axis may not apply to it.

If experience is a *fundamental* property of matter, then "how much does the substrate constrain" is arguably
**ill-posed** for panpsychism rather than mid-valued — 0.52 reads as a hedge, which is what a midpoint usually
is. Options: keep with an explicit footnote, or introduce an *off-axis* marking for positions the coordinate
system does not cleanly measure. **The second is more interesting** — a coordinate system that says where it
does not apply is more credible than one that scores everything.

### F13 — **zero of eleven positions carries a citation.** This is the remaining work.

Every point is a reading. Before the map is shown to anyone who holds one of these positions, each needs a
source for the *specific* placement claim, not merely for the position existing. Highest priority are the six
whose holders may be in the room at MoC7 per the `AIW-150` Class-B list.

## 3. The argument-space map — SOURCED (S289). 11 of 11.

`figures/smoc-philosophy-map.svg` places named positions in a space. A misplaced position is worse than a
mis-marked cell: it is a claim about what a specific person thinks, made in public, to their face — and the
`AIW-150` B-list names people who will be at MoC7.

**The rule set for this pass was: no position stays on the map unless its placement can be sourced to something
the author actually wrote.** All eleven now clear it. Each carries a numbered source printed on the figure;
the per-axis passage that licenses each coordinate is below. **One placement moved as a result** (F14).

### 3.1 The sourcing table

Read `x` as *how much is left outside the account* and `y` as *how much the substrate constrains*.

| # | Position | (x, y) | What licenses **x** | What licenses **y** |
|---|---|---|---|---|
| 1 | **Illusionism** | 0.05, 0.18 | Frankish 2016: *"the hard problem is replaced by the illusion problem"* — the explanandum is our representation of phenomenality, not phenomenality. Residue ≈ 0 **by construction**. | ⧗ **inferred, not quoted.** The programme is to explain misrepresentation, which is a representational/functional job; nothing in it privileges a substrate. Lowest-confidence coordinate on the map. |
| 2 | **Global workspace** | 0.15, 0.26 | Dehaene, Lau & Kouider 2017: *"consciousness" conflates two different types of information-processing computations* — global availability (C1) and self-monitoring (C2). Both computational ⇒ small residue. | Same paper asks whether **machines** could have it and outlines *"how they may inspire novel machine architectures"* ⇒ substrate permissive. **Both axes from one abstract.** |
| 3 | **Higher-order theories** | 0.21, 0.33 | Lau & Rosenthal 2011: *"conscious awareness crucially depends on higher-order mental representations that represent oneself as being in particular mental states"* — consciousness *is* a representational relation. | Representational relations are multiply realisable; the theory's empirical commitments are to prefrontal function, not to a physics. |
| 4 | **Active inference / FEP** | 0.28, 0.30 | Friston, Wiese & Hobson 2020: the agenda is to **repair** the Cartesian split *"using physics and information theory"* — the mind/matter distinction is put **inside** physics rather than left over. | "Markovian monism" — Markov blankets and information geometry are statistical/organisational notions, indifferent to what implements them. |
| 5 | **Self-model theory** | 0.20, 0.44 | Metzinger 2005 (Précis): the phenomenal self is transparent self-representation, with *"a straightforward ontological interpretation: no such things as selves exist in the world."* Accounted for, not left over. | Middle, and this is why: SMT is built on **four** levels — phenomenological, representationalist, functionalist, **and** neurobiological — but the last only *"points to potential neural correlates in the domain of biological systems"*. Constraints are representational; biology is a correlate layer. Not substrate-free, not substrate-bound. |
| 6 | **FMT** | 0.16, 0.58 | The Presence Term is a **marked** blank with an exclusion ledger — declared small and declared. | The middle position the map exists to show is occupied: closure + criticality constrain the substrate, but no specific physics is required. |
| 7 | **IIT** | 0.33, 0.78 | Axioms→postulates purport to account for phenomenal properties — cf. Albantakis et al. 2023, *"Formulating the properties of phenomenal existence in physical terms."* Small residue, larger than the workspace family's because the postulates are asserted as an identity. | Tononi & Koch 2015, verbatim: *"a simulation of our conscious brain will not have consciousness"*, and *"a feed-forward network does not exist intrinsically—for itself—but is a zombie"*. Substrate constrains hard — but by **cause–effect structure**, not by biology, which is why it sits below Searle. |
| 8 | **Biological naturalism** | **0.28**, 0.94 | **Moved this session — see F14.** Searle 2002: consciousness is *"causally reducible to brain processes"*, it *"does not name a distinct, separate phenomenon, something over and above its neurobiological base"*, and *"the impossibility of an ontological reduction … does not give it any mysterious metaphysical status."* | Same paper: *"so far, we have not found any system that can cause and realize conscious states except brain systems"*; consciousness is *"a biological process like digestion, photosynthesis, or the secretion of bile."* The most substrate-committed position on the map. |
| 9 | **Panpsychism** | 0.86, **N/A** | Strawson 2006: *"you cannot get experiential phenomena out of wholly non-experiential phenomena"*, therefore *"some of the fundamental properties of the physical stuff must be themselves experiential in character."* Experience is **posited, not derived** ⇒ high. See F15 for the objection a panpsychist will raise. | **D9 `not applicable`.** Micro-experience is everywhere, so the axis looks like 0 — but the map's referent is *macro*-consciousness, and which combinations yield a subject is exactly the unsolved **combination problem** (Chalmers 2016). The theory has no answer, rather than a middling one. |
| 10 | **Property dualism** | 0.91, 0.24 | Chalmers 1995 (*Facing Up*): *"Even when we have explained the performance of all the cognitive and behavioral functions … there may still remain a further unanswered question: Why is the performance of these functions accompanied by experience?"* | Chalmers 1995 (*Absent Qualia…*), verbatim: *"given any system that has conscious experiences, then any system that has the same functional organization at a fine enough grain will have qualitatively identical conscious experiences."* **Organizational invariance is the reason dualism sits LOW here** — the placement a reviewer is most likely to think is a mistake, and it is not. |
| 11 | **Mysterianism** | 0.96, 0.62 | McGinn 1989, verbatim: *"I do not believe we can ever specify what it is about the brain that is responsible for consciousness."* Not merely unexplained — **unexplainable-by-us in principle**. | Same sentence's other half: *"naturalistic but not constructive … whatever it is it is not inherently miraculous"*, and property P is a property *of the brain*. The brain does it; no physics is named. Mid-high, and it should not be maximal. |

### F14 — **`Biological naturalism` moved 0.48 → 0.28.** The midpoint was a hedge, and Searle's own text says so.

The S288 pass flagged the residue as *arguable*; reading the primary settles it. In **Searle 2002, "Why I Am Not
a Property Dualist"** (*J. Consciousness Studies* 9(12), 57–64) he states that consciousness *"is causally
reducible to brain processes, because all the features of consciousness are accounted for causally by
neurobiological processes"*, that *"'Consciousness' does not name a distinct, separate phenomenon, something
over and above its neurobiological base, rather it names a state that the neurobiological system can be in"*,
and — decisively for this axis — that *"the impossibility of an ontological reduction in the case of
consciousness does not give it any mysterious metaphysical status."*

**Why not 0, then.** One thing does stay outside, and Searle says it plainly: *"a complete description of the
third person objective features of the brain would not be a description of its first person subjective
features."* That is a permanent, in-principle remainder — but it is a claim about **description format**, not an
unexplained phenomenon. Small and real ⇒ **0.28**.

**What the move reveals, and it is worth more than the correction:** the map's **top-right quadrant is now
empty**. Nobody on it holds *"the substrate is nearly everything AND the account explains nearly none of it."*
That is a substantive fact about the field, not a gap in the sampling — high substrate-commitment goes with
confidence that the mechanism will deliver. An empty region of a coordinate system is information, the same way
a blank in the rung chart is.

### F15 — the panpsychist's objection to **x = 0.86**, pre-empted rather than waited for.

A panpsychist will say the placement misreads them: *nothing* is left outside their account — consciousness is
put **inside** fundamental physics, which is the most integrated treatment on the map, not the least. Under the
S288 reading convention (*plot the theory as it describes itself*) that objection has to be answered, not
brushed off.

**The answer is that the axis measures what the mechanism DELIVERS, not what the ontology CONTAINS.** Its left
pole reads *"nothing outside — it is all mechanism."* Positing experience as a fundamental property is exactly
the move of declining to derive it, and Strawson's argument is explicitly that it *cannot* be derived: *"you
cannot get experiential phenomena out of wholly non-experiential phenomena."* Including something as a
primitive and explaining it are different, and this axis measures the second. **Add the axis gloss to the
figure caption when the map ships** so the answer arrives before the objection.

### F16 — one coordinate on the map is still inferred rather than quoted: **Illusionism's substrate, y = 0.18.**

Frankish's abstract licenses the x-coordinate outright and says nothing about substrate. 0.18 is read off the
shape of the programme — explaining misrepresentation is a representational job — which is an inference from
what illusionism *is*, not from a sentence Frankish wrote. It is almost certainly right and it is the one cell
of the eleven that would not survive the standard applied to the others. **Either source it to a functionalist
commitment Frankish states in print, or mark it inferred.** Left open deliberately rather than quietly rounded.

### F17 — **DECIDED (MG delegated, S289): a point is a POSITION, not a person.** And a second rule follows.

The `AIW-150` B-list names six MoC7 attendees to prioritise — **Kleiner, Zahavi, Atmanspacher, Blum, Kanai,
Peters** — and none of them is on the map. The question was whether the map plots *families* or *people*. It
plots **positions**, and this is now declared on the figure. Three reasons, in order of weight:

1. **The axes are only defined over accounts.** "How much is left outside the account" is a property of an
   account. A person is not an account. Kleiner's mathematical-consciousness-science programme *formalises and
   compares* theories — it sits a level above these axes and has no coordinate. Saying so on the figure is
   accurate and is not a slight; scoring him would be the category error.
2. **The S288 reading convention only parses for theories.** "Plotted as the theory describes ITSELF" has no
   person-level counterpart: a canonical text is fixed and citable, a living researcher's current view is
   neither.
3. **It is what the S289 citation standard can actually enforce.** The bar set above is *source the placement to
   something the author wrote*. That is a text standard. It works for positions and it cannot work for people.

**The second rule, which is the one that will bite:** *a point earns its place by informing, not by existing* —
and there are exactly two ways to inform: **spread the field**, or **contest FMT's own claimed gap.** The second
matters more, and the audit must not duck it. Applied to the three candidates:

| Candidate | Verdict | Why |
|---|---|---|
| **Conscious Turing Machine** — Blum & Blum 2022, *PNAS* 119(21), e2115934119, doi:`10.1073/pnas.2115934119` | **Not placed** | A genuine position, but by its own abstract it is *"influenced by … the global workspace theory (GWT) … originated by Bernard Baars and further developed by him, Stanislas Dehaene, Jean-Pierre Changeux, George Mashour"*. It lands on top of the workspace family, one notch lower on substrate (a TM abstraction rather than a *neuronal* workspace). A point that close adds crowding, not separation. Also — under **F16**'s own standard — its residue coordinate has no quoted source yet; the abstract says phenomena *"are considered"*, not explained. |
| **Dual-aspect monism** — Atmanspacher | **Not placed** | The psychophysically neutral base makes the substrate axis ill-posed in the *same* way panpsychism's is. A second dashed band would turn **D9** from a rare principled refusal into a general escape hatch, which costs more than the point gains. |
| **Information generation** — Kanai et al. 2019, *Neurosci. Consciousness* 2019(1), niz016, doi:`10.1093/nc/niz016` | **PLACE IT — next session, and do not quietly skip it** | *"a core function of consciousness be the ability to internally generate representations of events possibly detached from the current sensory input … constructed by generative models learned through sensory-motor interactions."* That is **FMT's R2 rung in different vocabulary**, and it is the nearest rival to the region FMT calls unoccupied. **Leaving it off would be self-serving in exactly the way §0.2 warns about** — the map's claim that FMT holds "a specific and unoccupied position" is only worth anything if the position most likely to falsify it is on the chart. It needs its **substrate** coordinate sourced before it goes on; the residue coordinate is already quotable from the abstract above. |

## 4. Method for the remaining work

1. Take cells in risk order — AT RISK first, since those change the chart rather than merely annotate it.
2. For each: state the proposition the mark asserts, find the primary, record title/authors/venue/DOI.
3. Apply the convergence bar: **two or more *independent* theories positing something equivalent in different
   vocabulary.** One theory plus FMT is not convergence.
4. Record the verdict inline in `docs/smoc-middle-layer-draft.md` and the citation in `docs/references.md`.
5. Downgrades are wins, not losses — a chart that demotes its own marks is the one the field will trust.
