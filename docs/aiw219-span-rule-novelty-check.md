<!-- Action: reference -->
<!-- Tracked-by: AIW-219 -->
# AIW-219 — Span rule: literature and novelty check

**Run S306, 2026-08-23, by a Fable agent.** MG directed the handover from crucible on 2026-08-14 and
was explicit that **the first ask is a literature check, not a draft**. This is that check. No paper,
abstract or outline was written.

Sources read: `~/crucible/docs/design/span-rule-standalone-publication.md`,
`~/crucible/docs/span-rule-explainer.md`, `~/crucible/docs/results/cru75-span-argmin.md`,
`~/crucible/docs/results/cru82-boundary-scaling.md`, `~/crucible/docs/results/cru69-tau-syn-scope.md`
§11.6. Roughly 15 targeted web searches plus full-text reads across communication subspaces, low-rank
RNNs, wiring economy, bow-tie evolution, information bottleneck, multi-area RNNs, global workspace,
self-modeling and multi-task architecture grouping.

---

## VERDICT: **NOVEL BUT NARROWER THAN IT LOOKS**

No publication was found that derives or measures the **span** of a cost-optimal inter-subsystem
bottleneck and shows it equals the content's support with both failure directions measured; nor the
four-condition specificity; nor the non-monotone double-crossing cost boundary; nor self-inclusion
from connection-count minimization.

⚠ **But it sits one step from two published results, and one of them owns the headline.**

---

## 1. ⚠⚠ The paper a referee will cite against us

**Friedlander, Mayo, Tlusty & Alon (2015), "Evolution of Bow-Tie Architectures in Biology,"
*PLoS Comput Biol* 11(3):e1004055, DOI `10.1371/journal.pcbi.1004055`.**

It claims that bow-tie (bottleneck) architectures evolve in layered networks **iff the goal matrix is
rank-deficient**, and that **the waist width equals the rank of the goal**, "never lower than this
rank."

**That is condition 1 of the span rule, published in 2015.** It must be framed as *sharpening*, never
as discovery.

**Where it stops short**, verified by full-text read:
- **No span analysis at all** — only waist *width*, never *which* subsystems the bottleneck connects.
- **No wiring or connection cost anywhere in the fitness function.** Sparsity arises from
  multiplicative mutation drift, not cost minimization.
- No cost-at-matched-function comparison, no near-ceiling condition, no return-path condition, no
  non-monotone boundary, no self-inclusion.

Follow-ups contest the emergence conditions but stay on width/rank: *npj Syst Biol Appl* 2024,
DOI `10.1038/s41540-024-00396-8`; bioRxiv `2023.03.28.534501`.

## 2. The second-closest, and why it does not collide

**Semedo, Zandvakili, Machens, Yu & Kohn (2019), "Cortical Areas Interact through a Communication
Subspace," *Neuron* 102:249–259, DOI `10.1016/j.neuron.2019.01.026`.**

V1→V2 interactions are captured by a low-dimensional subspace of V1 activity, distinct from V1's
largest fluctuations. **Entirely descriptive** — it measures that a low-rank channel *exists* between
two areas. It never derives that the channel is optimal, never varies the span, never counts
synapses, and has no cost model. **The span rule is a normative claim this literature has explicitly
not made** — and the field's own map of proposed communication schemes (Kohn et al. 2020, *Trends
Neurosci* 43:725–737) contains no wiring-cost optimality scheme at all, which is decent evidence of
absence.

## 3. The rest of the field, ranked

| Work | What it has | Where it stops |
|---|---|---|
| Clune, Mouret & Lipson 2013, *Proc R Soc B* 280:20122863 | connection cost in the objective → modularity | no bottleneck-span prediction, no content-rank condition |
| Kleinman, Chandrasekaran & Kao, NeurIPS 2021 | trained multi-area RNNs propagate output-relevant information preferentially | emergent, not an argmin; no synapse cost; span never varied |
| Clark & Beiran 2025, *PNAS* 122(10):e2404039122 | low rank **imposed** between regions, dynamics derived | takes the architecture as given; never asks if it is optimal |
| Achterberg, Akarca et al. 2023, *Nat Mach Intell* 5:1369 | wiring cost during training → brain-like structure | closest in *spirit*; no span claim, no rank condition |
| Goyal et al. ICLR 2022 (arXiv:2103.01197); VanRullen & Kanai 2021 | shared bandwidth-limited workspace among modules | never makes the O(N²)-vs-O(N) wiring argument; no principle for *which* modules connect; measures no cost |
| Premakumar … Graziano 2024 (arXiv:2407.10188) | imposing self-prediction → simpler, more parameter-efficient nets | **runs the causality the other way** — they impose self-modeling and find efficiency; we derive self-inclusion from efficiency. Cite as partner, not rival |
| Gozel & Doiron 2024, *Sci Adv* 10:eadl6120 | sender/receiver dimensionality match aids communication | mechanistic, no cost |
| Tishby et al., information bottleneck | optimal compression under mutual-information constraints | **a different object.** No wiring, no synapse counts, no span. Must be explicitly distinguished or referees will conflate |
| Baldi & Hornik 1989; Eckart–Young | "optimal rank-k code spans the top-k signal subspace" | the single-system activity-space ancestor; says nothing about which *subsystems* to touch |
| Cherniak 1994; Chklovskii et al. 2002 *Neuron* 34:341; Bullmore & Sporns 2012 | wiring economy classics | placement and length, never bottleneck span |

## 4. What is actually new — the one sentence a reviewer would accept

> In an exhaustive cost-at-matched-function comparison over all 72 span×rank wiring architectures of
> a multi-subsystem associative substrate, the cost-optimal low-rank bottleneck spans exactly the
> subsystems on which the stored content is supported — sub-support spans fail at any capacity,
> super-support spans add pure cost — and the bottleneck beats direct wiring only under four
> independently measured conditions (content low-rank relative to substrate, multi-subsystem support,
> near-ceiling performance criterion, short return path), with the bottleneck/direct boundary
> demonstrably non-monotone in substrate size.

**Scope limits that must travel with it:** numpy substrate; one connectome family; 21–126 units per
subsystem; ranks 4/8/16; one content condition for the boundary work; one cost model; **span
enumerated, not proved**; optimality never necessity; the second cost-crossing sits at the edge of
the tested range; τ_syn robustness verified at 2 and 5, adjudicability lost by 10.

The **self-inclusion corollary rides as a structural remark, not a claim.** It is also the part with
reach: no prior claimant was found, and the nearest work runs the causality the other way.

## 5. ⚠ The strongest referee objection, and how well we answer it

> *"Given your cost model — C increasing in |σ| and k, with k lower-bounded by the content's rank on
> the reachable subsystems — span=support is a foregone conclusion: too-small spans are rank-deficient
> (Friedlander 2015 already noted the waist can never be below goal rank), and larger spans buy
> nothing by construction. Your enumeration confirms arithmetic. What did the experiment discover
> that the cost model didn't presuppose?"*

**Partially answered.** Four things are *not* arithmetic:
1. **The near-ceiling condition** — direct wiring beating every bottleneck at a 90% criterion was
   found by failure, not predicted.
2. **The double-crossing non-monotone boundary**, with direct wiring's cost-to-criterion plateau —
   measured, and the mechanism is **explicitly unexplained** (CRU-82 §4).
3. **The return-path erosion factor** (~8× from a 1-stage to an 8-stage return).
4. **Sub-support unreachability is a hard measured ceiling** in a nonlinear Hebbian completion task,
   not a linear-algebra assertion.

⛔ **Answered badly if the paper leads with span=support as the discovery.** The argmin must be the
organizing spine and the four failure-measured conditions plus the boundary structure the empirical
substance — otherwise a referee kills it with the sentence above plus one citation.

## 6. Venue read — crucible's computational-neuroscience guess is supported

1. **PLoS Computational Biology** — best fit. It published the bow-tie paper this result sharpens and
   is comfortable with simulation-based normative claims carrying honest scope.
2. **Network Neuroscience** (MIT Press) — the wiring-economy/architecture-optimality home; would
   value the double-crossing boundary.
3. **eLife** — plausible if the framing leads with the testable prediction (where communication
   subspaces should and should **not** be found). Higher bar for a pure-synthetic result.
4. **Biological Cybernetics** — traditional home for cost-optimality circuit theory; lower impact,
   low desk-rejection risk.

Preprint to **arXiv q-bio.NC** regardless. ML venues correctly ruled out (no learning, no benchmark).
Pure maths ruled out **unless span=support gets proved** — which the circuit-complexity check
suggests is likely tractable for this restricted cost model even though the general minimum-wire
problem is open, and **would upgrade the paper substantially**. That is the single highest-value
follow-on.

## 7. Residual risk, stated honestly

Semedo 2019's 600+ forward citations were not exhaustively walked, and the 2025–26 bioRxiv flood was
sampled rather than swept. Paywalled full texts (*TiNS*, *Neuron* reviews) were read via abstracts and
preprints. A buried theory paper deriving optimal communication-subspace placement from synapse counts
could exist; nothing in five different search framings surfaced one.
