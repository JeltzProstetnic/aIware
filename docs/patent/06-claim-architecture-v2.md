# Claim Architecture v2 — Post-Red-Team Restructuring

**Preparatory drafting for briefing a patent attorney. Not legal advice.** No author of this
document is a patent attorney; nothing here may be filed as-is. This is the redraft responding to
`05-red-team.md` (2026-08-11); it supersedes the *claim set* of `03-claim-architecture.md` but not
that document's vocabulary map (§1), disclosure analysis, or continuation posture, which are
incorporated by reference. Companion documents: `01-patentability-strategy.md` (filing strategy —
its conclusions stand, including **priority filing before MoC7, Oct 12–16 2026**) and
`02-prior-art-landscape.md` plus the red-team's R1–R13 (which now form the working art record).

**The inventor's brief is unchanged:** a claim set as painful as possible to circumvent, fencing the
implementation recipe rather than the theory, with publication freedom secured by filing first.

---

## 0. Decisions made in this redraft — summary

| # | Decision | Red-team finding it answers |
|---|---|---|
| D-1 | **The routed-credit training method (v1 claim 23) is promoted to lead independent claim (new claim 1)** and carries the portfolio. It is the only fully-measured, art-clean, structural claim in the set, and its evidence base (Gate A, CRU-83) is *independent of the fold defect* — it involves no return loop. | Finding 6 (§6.2 of the red team) |
| D-2 | **The system independent is redrafted in Markush form over all three fold-breakers** (distinct return filter state / delay / interposed nonlinearity), closing the two free doors. | Finding 3 (§2.2) |
| D-3 | **The heterogeneous-τ dilemma is resolved by a state-distinctness redraft, not a constant-value redraft** — and partially *dissolved*: on the fold algebra itself, the performance-positive published variant (per-neuron heterogeneity, Perez-Nieves) does **not** break the fold and lands in the self-defeating bin; the variant that does break it (per-edge kinetics) is **caught** by the redrafted branch (i). One contested variant remains (dedicated-kinetics return), where validity rests on the problem-discovery story alone. Full analysis §3. | Findings 1–2 (§2.1) |
| D-4 | **v1 claim 16 (redeployment) is pulled from the priority independents.** Rebuilt in narrow form as a *conditional* family, filed only if the forward-direction / control-loop / spiking-substrate runs (E8) complete before the priority date; otherwise spec-disclosed for continuation. | Finding 5 (§1.3, §3.3, §4) |
| D-5 | **v1 claim 21 as drafted is dead and is not refiled.** Its salvageable elements become dependents of new claim 1. The margin gate leaves every independent (unmeasured conjunct = escape surface) pending E6. "Exactly one scalar trace" becomes "a number of trace values per connection independent of network size" in the independent, "exactly one" as a dependent. | Finding 5 (§1.4, §2.5) |
| D-6 | **v1 claim 31 (neuromorphic device family) is killed as an independent.** Loihi (R7) discloses the capability level; a configuration-novelty device claim is prophetic *and* obvious *and* enforcement-broken. One neuromorphic-implementation *dependent* of the system claim survives at near-zero cost; the hardware embodiment stays in the spec for continuation rights. | Finding 5 (§1.5, §3.4) |
| D-7 | **Every measurement is re-attributed** (§4): which limitations rest on loop-independent evidence, which on folded-arm evidence (needing re-runs), which are prophetic. The 7.9× technical-effect hook is withdrawn from the system claim's support until re-measured on the unfolded loop (E4). | Finding 4 (§3.1) |
| D-8 | **A work order for crucible (E1–E10, §6)** converts the prophetic and folded-arm-supported limitations into enabled ones. E1 (build and run the non-foldable loop) gates the entire system family; the family should not be filed without it. | Finding 4; red-team §7.4 |

Filing consequence: the priority application leads with the **training-method family** (claims 1–14),
carries the **system family** (claims 15–30) contingent on E1 (+E4 strongly recommended), holds the
**redeployment family** (claims 31–33) contingent on E8, and files **no device family**. CRM/medium
claims mirroring claim 1 are routine US adjuncts. The continuation posture of v1 §2.6 (rate-network
generalization, decompilation pipeline, certification method, emergence-protocol controls) is
unchanged: disclose in the spec, claim nothing now.

---

## 1. Family A — training method with routed masked credit (claims 1–14) — THE LEAD

### Why this family leads

The red team's most important line: claim 23 "survived every front" — no close art after genuine
search, fully measured, pre-registered, structural. Its evidence (CRU-83 Gate A: local three-factor
rule fits the frame at 92.4% of the hand-wired ceiling, +0.891 vs floor −0.003, permutation
p = 0.0001, 8 seeds, pre-registered before the script existed) was taken on the real spiking
substrate **with no return loop in the rig at all** — so it is untouched by the CRU-69 folded-arm
wound that undermines the system family's numbers. It is the one part of the portfolio whose
technical effect is measured *at its point of novelty* today.

Promotion changes the claim's scope: as v1's claim 23 it carried all of claim 21's limitations; as
an independent it must stand on its own novelty. The point of novelty is therefore drafted as the
**routing structure itself** — mask-confined plasticity into an interposed alignment region, with
the downstream structure held fixed — on top of an admitted-art three-factor skeleton (Izhikevich
R1 is cited in the spec as the skeleton's source; the claim does not pretend eligibility traces are
new). The red team searched the three-factor literature specifically and found no art on spatially
routed, mask-confined credit through an interposed region. That search must be repeated
professionally (CPC G06N 3/049 × "eligibility trace" × "third factor", per red-team §7.8) before
filing.

> **Claim 1 (independent — training method).**
> A computer-implemented method of training a recurrent network of spiking neurons of a control
> system of an embodied agent, the network comprising a designated region and an alignment region,
> the alignment region being interposed between a sensory input of the network and the designated
> region, the method comprising:
> maintaining, for each of a plurality of plastic synaptic connections, at least one eligibility
> trace updated locally from pre-synaptic and post-synaptic spike activity of that connection and
> decaying with an eligibility time constant, wherein the number of trace values maintained per
> connection is independent of the number of neurons of the network;
> computing a modulatory credit signal;
> confining synaptic plasticity, by a connection mask, to connections into the alignment region,
> wherein connections from the alignment region to the designated region and connections within the
> designated region are held fixed during the training; and
> updating weights of the connections into the alignment region as a function of the product of the
> respective eligibility trace and the credit signal.

*Drafting notes.* (a) The Gate-A structure verbatim: OBS→FRAME plastic under `plastic_mask`,
FRAME→SELF and SELF→SELF fixed. Every limitation is measured in exactly this configuration. (b) The
independent deliberately does **not** recite: the margin gate (unmeasured — §2.5(a) of the red team;
pending E6), the fixed readout (eroded by RM-SORN; implied anyway by mask confinement; explicit in
dependent 6), homeostasis (SORN art makes it non-distinguishing; dependent 2), or derived credit
(prophetic on the spiking substrate — Gate A's own scope note: "nothing here separates supplied
credit from derived credit"; dependent 9). Each omitted conjunct was escape surface that bought no
novelty. (c) "Independent of the number of neurons" adopts v1's B.3.5 instruction and closes the
two-traces-per-synapse escape (red-team §2.5(c)). (d) Validity posture against R1+R6: Izhikevich
supplies traces × global credit; SORN supplies homeostasis-in-reservoir; **neither routes credit
through a masked interposed region with the downstream path frozen** — that structure has no
counterpart in the three-factor, SORN, or e-prop literature searched, and it is what the shuffled
floor (−0.003) shows to be load-bearing. (e) Known weakness, stated: the Gate-A floor separates the
*rule* from the wiring, not the *routing* from unrouted plasticity — an examiner or opponent may ask
"what does the mask buy over plasticity everywhere?" That comparison is unmeasured. E7 exists to
close it before filing.

> **Claim 2.** The method of claim 1, further comprising concurrently adapting, for each neuron of
> at least the alignment region, a firing threshold by negative feedback from a running average of
> that neuron's firing rate toward a target rate.

> **Claim 3.** The method of claim 2, further comprising pinning the adapted firing thresholds to
> fixed values during any evaluation of network outputs used to assess training progress.

*(θ-pinning, v1 claim 26 — measured failure mode it prevents: free-running homeostasis inverts the
carried code, corr +0.968 → −0.937. The red team found no art on it. Chained after 2 because pinning
presupposes adaptation. If the examiner presses claim 1, the first fallback merge is 1+2+3 — the
red-team's own recommended merged form.)*

> **Claim 4.** The method of claim 1, wherein plastic connections are initialized with connection
> signs determined by a per-source-neuron sign assignment and with random magnitudes, and wherein
> connections whose stored sign contradicts the sign assignment of their source neuron are rejected
> at construction.

*(Dale-sign construction guard, v1 claim 24 — survived the red team "cheap"; flagged for
professional search on sign-constrained E/I initialization art. Gate A §5 documents the concrete
defect it prevents: 576 mis-signed edges would have silently untrained the inhibitory half.)*

> **Claim 5.** The method of claim 1, wherein each scalar dimension of the sensory input is
> connected to the alignment region through at least one excitatory and at least one inhibitory
> population pair, whereby coefficients of either sign are realizable under the sign assignment.

> **Claim 6.** The method of claim 1, wherein weights of a readout of the network are fixed before
> the training and held fixed throughout the training.

> **Claim 7.** The method of claim 1, wherein exactly one scalar eligibility trace is maintained per
> plastic synaptic connection.

> **Claim 8.** The method of claim 1, wherein the updating is applied only when an error measure
> exceeds a margin. *(Retained as a dependent only; delete if E6 shows the gate is not
> load-bearing.)*

> **Claim 9.** The method of claim 1, wherein the credit signal is derived by the network itself as
> a reafference prediction error between predicted and actual subsequent sensory input, computed
> over all sensory channels without selection of a subspace of channels. *(Prophetic on the spiking
> substrate — flagged; rate-analogue demonstrated. E-gap named in §4.)*

> **Claim 10.** The method of claim 9, wherein no training signal, reward definition, or input
> labelling identifies any subset of sensory channels as pertaining to the embodied agent's own
> body.

> **Claim 11.** The method of claim 1, comprising a first stage in which the network is trained on
> sensorimotor experience of the embodied agent's own body to form a forward model, and a second
> stage in which, with parameters of the forward model held fixed, only an alignment transform is
> trained to adapt the forward model to a changed body or to an external dynamical entity.
> *(Bridge to family C.)*

> **Claim 12.** The method of claim 1, wherein the plastic synaptic connections are stored in a
> compressed edge-indexed representation, whereby memory required for training scales with the
> number of stored connections rather than with the square of the number of neurons.

*(The O(E) effect moves out of the independent — the red team is right that a whereby reciting an
inherent property of sparse storage adds no patentable weight (§1.4), and it created the
eligibility/validity tension of §4 ("Eligibility and validity cannot both be saved by the
whereby-clause"). As a dependent it still anchors the EPO route-(ii) technical-character story with
its measured numbers: 0.06 GB vs ~2.5 GB/step at 25k neurons.)*

> **Claim 13.** The method of claim 1, wherein the training is conducted while, for each region of a
> plurality of regions of the network, a branching parameter estimated from spike activity of a
> fixed-size subsample of that region lies within a predetermined band around unity. *(Eroded by
> Wilting & Priesemann 2018 + Zierenberg 2018 — acceptable as a dependent, per red-team rank 6. The
> band needs E9/E10.)*

> **Claim 14.** The method of claim 1, wherein the recurrent network is the recurrent network of a
> control system according to claim 15. *(Unity-of-invention anchor.)*

---

## 2. Family B — system with a non-foldable return, Markush form (claims 15–30)

> **Claim 15 (independent — system).**
> A control system for an embodied agent, comprising:
> a sensor interface arranged to receive sensory signals from at least one sensor of the embodied
> agent;
> an actuator interface arranged to issue motor commands to at least one actuator of the embodied
> agent;
> a recurrent network of spiking neurons partitioned into a plurality of regions, the plurality of
> regions comprising at least a first region coupled to receive the sensory signals and a second
> region coupled to receive a copy of the motor commands, wherein neurons of at least two different
> regions are assigned different membrane time constants;
> recurrent synaptic connections among the neurons, wherein synaptic transmission over the
> recurrent synaptic connections is low-pass filtered by one or more synaptic filter states;
> a readout arranged to derive from spike activity of the second region a signal of dimensionality
> lower than the number of neurons of the second region; and
> a return path arranged to re-inject the derived signal as input to neurons of at least the first
> region,
> **wherein the return path comprises at least one of:**
> **(i) a return filter state that low-pass filters the derived signal and that is distinct from
> every synaptic filter state filtering synaptic transmission of recurrent synaptic connections onto
> the neurons receiving the re-injected signal;**
> **(ii) a delay element imposing on the derived signal a transmission delay exceeding the
> transmission delay of every recurrent synaptic connection onto the neurons receiving the
> re-injected signal; and**
> **(iii) a nonlinear transformation interposed between the readout and the re-injection;**
> **such that the input contributed by the return path is not expressible as an additive
> modification of weights of the recurrent synaptic connections acting on the one or more synaptic
> filter states**;
> and wherein the motor commands are derived at least in part from spike activity of the recurrent
> network.

*Drafting notes — every change from v1 claim 1 is deliberate:*

1. **"a shared synaptic filter state having a first filter time constant" → "one or more synaptic
   filter states."** This is the repair of the red team's §2.1. The v1 element recited crucible's
   implementation accident (one scalar `a`, one buffer `_g`); any heterogeneous-kinetics
   implementation simply lacked the element. The generic form covers uniform, per-neuron, per-pathway
   and per-edge filtering, so the wherein-clause always has a referent.
2. **Branch (i) is state-distinctness, not constant-value difference.** "A second, different time
   constant" (v1) is escaped by drawing constants from a distribution. "Distinct from every filter
   state filtering recurrent input *onto the same target neurons*" tracks the actual mathematical
   boundary of the fold theorem (see §3): the fold holds exactly when the return's contribution
   passes through filter states shared with recurrent transmission; it breaks exactly when the
   return has states of its own. Crucible's `g_ret` construction infringes; a per-edge-τ
   implementation infringes (its return edges necessarily carry their own states); a per-neuron-τ
   implementation does not infringe — and, by the theorem, has built an open network (§3.2).
3. **Markush over all three breakers, in the independent.** Non-negotiable per red-team §2.2: v1's
   claims 3/4 as dependents caught nothing their parent did not catch, leaving delay-only and
   nonlinearity-only returns — both certified functional fold-breakers by CRU-69 §4 — free. As
   Markush alternatives each is an independent infringement route. EPO practice will want each
   alternative enabled: E5 exists for that (a task run through a delay-return arm and a
   nonlinearity-return arm; the differential-τ arm is E1).
4. **The functional wherein is kept as the common consequence, with a definitional test in the
   spec.** The spec must define the decomposition test operationally (simulate the system;
   separately simulate with the return path's weights removed and, superposed, the return
   contribution computed as a weight-modification acting on the existing filter states; the system
   is non-foldable iff the superposition fails to reproduce the total — the exact form of crucible's
   `test_a_shared_filter_leaves_the_matrix_decomposition_exact`, inverted). This gives the
   functional clause an Art. 84/§112(b) answer. Counsel must decide whether the functional clause
   survives as a wherein or should demote to the spec; the Markush structure does not depend on it.
5. **How this survives Nicola & Clopath (R4) and the multi-kinetics art (R12, R5), stated
   exactly:** R4's feedback shares the network's synaptic filter — it is the foldable configuration
   (their own effective-weight formulation *is* the fold), so it fails branch (i) structurally and
   the functional wherein by algebra; it has no distinguishing delay (ii) or interposed nonlinearity
   (iii). R12's dual-kinetics networks (AMPA/NMDA everywhere) have no low-rank readout-return at
   all; where a return re-enters through receptor kinetics also used by recurrent transmission onto
   the same targets, branch (i) is not met — and the configuration folds pathway-wise (§3.2), which
   is consistent, not embarrassing. R5 is per-neuron heterogeneity with no readout-return
   architecture. **No single reference discloses the combination** (red-team §6.1 conceded this
   after genuine search). The obviousness fight over R4+R12 ("make the feedback slow-NMDA") is real
   and cannot be drafted away; the counter is the problem-discovery story — nobody had published
   that a shared-filter return is algebraically an open network — and the spec must teach the fold
   theorem as the technical problem, accepting that this also teaches the breakers (which is
   precisely why all three are in the independent).
6. **Filing condition:** this family does not go into the priority filing unless E1 has run
   (claimed machine demonstrated end-to-end), and it goes in weak unless E4 has produced a measured
   effect attributable to the distinguishing feature (G 2/21). §4 has the ledger.

> **Claim 16.** The system of claim 15, wherein the return path comprises the return filter state of
> alternative (i), the return filter state having a filter time constant differing by at least a
> factor of two from every filter time constant applied to recurrent synaptic connections onto the
> neurons receiving the re-injected signal. *(Factor pending E9 sweep; measured working point is
> factor ten, τ 2 vs 20.)*

> **Claim 17.** The system of claim 15, wherein the plurality of regions further comprises a third
> region coupled to receive proprioceptive signals of the embodied agent, and wherein the return
> path re-injects the derived signal into neurons of both the first region and the third region.
> *(Span law — support currently folded-arm-only; needs E2.)*

> **Claim 18.** The system of claim 17, wherein the dimensionality of the derived signal is smaller
> than one tenth of the number of neurons spanned by the re-injection. *(Needs E2 + E9.)*

> **Claim 19.** The system of claim 15, wherein the return path comprises at most one intermediate
> relay stage between the readout and the re-injection. *(Short-return — needs E3.)*

> **Claim 20.** The system of claim 15, wherein the readout comprises a projection of the spike
> activity of the second region through a relay population of spiking neurons, the relay population
> having fewer neurons than the second region, and wherein the re-injection comprises synaptic
> projections from the relay population. *(Express relay-population dependent — closes red-team
> §2.3's construction escape as a matter of claim scope; the spec must additionally define
> "readout" and "derived signal" to include dimension-reducing projection through a neuron
> population, and "return filter state" to include the relay's membrane and synaptic states, per
> v1 B.1.7's off-substrate instruction which is retained.)*

> **Claim 21.** The system of claim 15, wherein at least part of the return path is implemented
> outside the recurrent network, the derived signal being computed and re-injected by a processing
> element external to the network. *(Off-substrate return.)*

> **Claim 22.** The system of claim 15, wherein the return filter state of alternative (i) is
> implemented as a distinct dendritic or compartmental state of the neurons receiving the
> re-injected signal, the compartment having its own filter time constant.

> **Claim 23.** The system of claim 15, further comprising a firing-threshold regulator arranged to
> adapt, for each neuron, a firing threshold by negative feedback from a running average of that
> neuron's firing rate toward a target rate.

> **Claim 24.** The system of claim 23, wherein a gain of the recurrent synaptic connections is set
> such that, for each region of the plurality of regions, a branching parameter estimated from
> spike activity of a fixed-size subsample of that region lies within a predetermined band around
> unity. *(Criticality — Cramer-clearing structure retained from v1 claim 9; eroded by R9/R10 but
> acceptable as a dependent; band needs E9/E10.)*

> **Claim 25.** The system of claim 15, wherein the recurrent synaptic connections are stored in a
> compressed edge-indexed representation with a fixed per-neuron fan-in.

> **Claim 26.** The system of claim 15, wherein weights of the readout are fixed during operation
> and during training of the recurrent synaptic connections, and wherein synaptic plasticity is
> confined to the recurrent synaptic connections.

> **Claim 27.** The system of claim 15, wherein the copy of the motor commands is delivered to the
> second region by a fixed, non-plastic projection.

> **Claim 28.** The system of claim 15, wherein the neurons receiving the re-injected signal
> include neurons whose activity is also driven by the sensory signals, whereby the derived signal
> and the sensory signals share a common state space.

> **Claim 29.** The system of claim 15, wherein membrane time constants are assigned per region and
> differ between the first region and the second region by at least 25%. *(Percentage pending E9;
> contributes nothing against obviousness per red-team §1.2 preamble-erosion note — keep only if
> cheap.)*

> **Claim 30.** The system of claim 15, implemented on a neuromorphic processing device in which
> the one or more synaptic filter states and the return filter state of alternative (i) are
> realized as configurable filter circuits or per-compartment filters, and in which synaptic
> connections are stored in synapse memory comprising, per stored connection, a weight field and a
> number of eligibility-trace fields independent of the number of neuron circuits. *(The residue of
> the killed device family — a system-claim dependent costs nothing, keeps a neuromorphic hook, and
> avoids the configured-chip enforcement trap of a standalone device claim. The spec keeps the full
> hardware embodiment at data-structure level for continuation rights and expressly distinguishes
> Loihi's capability-level disclosure (R7).)*

---

## 3. The heterogeneous-τ dilemma — resolution, and where the red team overreached

### 3.1 What the red team got right

The v1 claim element "a shared synaptic filter state having a first filter time constant" fenced the
implementation accident. Any implementation without a single global filter state escaped the entire
family, dependents included, at modest-to-zero cost. That finding stands and drove change 1 of §2.

### 3.2 Where the red team overreached — the fold algebra does not say what §2.1 says

The red team asserts (§2.1, third bullet): *"With heterogeneous τ, any return pathway automatically
has 'its own' time constants — the competitor gets a non-foldable, dynamically real loop without
ever building the claimed second-filter-state construction."* **This is wrong for the variant the
cited art actually supports, and the error matters.** From CRU-69 §3, the fold identity is

```
I(t) = gain·((W_bulk + W_ret)·g(t)) = gain·(W_bulk·g(t)) + gain·(W_ret·g(t))
```

and it holds because `g(t)` is a function of the spike train alone, never of `W`. That remains true
for **any neuron-indexed filter state**: replace scalar `a` by a per-neuron vector `a_j`
(source-indexed, Perez-Nieves-style presynaptic heterogeneity) or filter each neuron's summed input
post-synaptically with its own `τ_i` — in both cases the return contribution `W_ret·g(t)` passes
through exactly the same states as the recurrent contribution, matrix additivity is untouched, and
**the loop still folds**. Only **edge-classified kinetics** — per-edge filter states, or per-pathway
states in which the return edges use states not shared by recurrent edges onto the same targets —
break the decomposition. Consequences:

- **Per-neuron heterogeneous τ (the variant R5 measured and the field's published best practice):**
  escapes claim 15 under branch (i) — correctly, because it *is* a foldable, open-network
  configuration. It lands in v1's B.1.2 bin: the competitor gets R5's learning benefits and has, by
  the theorem, declined to build the invention. The escape is real but it is no longer an escape
  *with the invention included free*.
- **Per-edge heterogeneous τ (the genuinely fold-breaking variant):** is **caught** by redrafted
  branch (i) — its return edges necessarily carry filter states distinct from every recurrent state.
  And it is not free: a shared or per-neuron filter costs O(N) dynamic state; per-edge filtering
  costs O(E) state and per-edge updates (at fan-in ~100, roughly two orders of magnitude more
  dynamic memory) — modest on Loihi-class hardware whose per-synapse traces are already paid for,
  real on the memory-constrained software and edge substrates that are this route's commercial
  case. Also, R5's measured benefit attaches to per-neuron, not per-edge, heterogeneity — the
  "published best practice that improves learning" support and the "total escape" mechanism belong
  to *different variants*.
- **Per-pathway dual kinetics everywhere (Brunel & Wang habit):** a return re-entering through
  receptor kinetics also used by recurrent transmission onto the same targets folds pathway-wise —
  escapes branch (i), open network, B.1.2 bin. A return through kinetics *not* used by the
  recurrence onto those targets meets branch (i) and infringes.

### 3.3 The residual dilemma, stated honestly

The redraft closes the per-edge door and converts the per-neuron door into a self-defeating escape.
What remains contested is the **dedicated-kinetics return**: a competitor who gives the return path
receptor kinetics distinct from the recurrence (slow-NMDA feedback onto fast-AMPA recurrence)
infringes branch (i) — and will argue obviousness from R4+R12 exactly as the red team scripts it.
That fight cannot be won by drafting; it is won or lost on the problem-discovery story (the fold
theorem as the previously-unrecognized technical problem), which the red team itself scores as "a
real argument" and the EPO's problem-solution approach favors. **Cost of this resolution:** the
system family's validity now rests on one argument, and a tribunal unpersuaded by problem-discovery
invalidates branch (i) while (ii) and (iii) stand on their own art-free structure. That is an
acceptable posture for a *secondary* family — which is what D-1 makes it.

Two further honesty notes carried into the spec: (a) per CRU-67 §10, the spec must **never** claim
or imply that a non-foldable return produces input-output behavior an open architecture cannot —
the inventor's own record proves the opposite ("ties exactly, term for term"; "what survives is a
cost gap, not an indistinguishability gap"). The invention's technical character is resource
economy and trainability structure, not behavioral distinctness. E4 is designed accordingly
(cost-at-matched-performance, not performance-at-matched-cost). (b) The crucible record is assumed
discoverable (red-team §7.9); every claim above is drafted to be consistent with CRU-67/69/83 being
read aloud.

---

## 4. Evidence ledger — where each technical effect is measured (Part B)

Categories: **CLEAN** = measured on evidence independent of the fold defect (loop-independent rigs
or the substrate without the return); **FOLDED** = supported today only by folded-arm measurements —
must be re-run on the unfolded loop before the supported limitation is asserted with numbers;
**PROPHETIC** = constructive disclosure only.

| Claim(s) | Limitation / effect | Status | Evidence today | Repair |
|---|---|---|---|---|
| 1 | Routed masked credit reaches 92.4% of hand-wired ceiling; decorrelated-credit floor −0.003; p = 0.0001 | **CLEAN** | CRU-83 Gate A, 8 seeds, pre-registered, spiking substrate, no loop in rig | — (E7 strengthens: prices routing vs unrouted plasticity, currently unmeasured) |
| 2 | Homeostasis required for stable plastic learning | **CLEAN** | R0b-2, reproduced on sparse substrate (OFF → drift and collapse) | — |
| 3 | θ-pinning prevents code inversion (+0.968 → −0.937 unpinned) | **CLEAN** | Recorded failure mode + Gate A run with θ pinned during scoring | — |
| 4, 5 | Dale guard; antagonist-complete support | **CLEAN** (as working-configuration findings) | Gate A §5 (576 mis-signed edges refused); Stage 0b realizability | — |
| 6 | Fixed readout / plasticity-confinement attributability | **CLEAN** | CRU-57 s1e: plastic recurrence 0.966 vs frozen-recurrence best-fit readout near chance, 25k neurons | — |
| 7, 12 | One trace per edge; O(E) memory (0.06 GB vs ~2.5 GB/step) | **CLEAN** | CRU-57 s1e | — |
| 8 | Margin gate load-bearing | **UNMEASURED** | none — flagged by red team §2.5(a) | E6; delete claim 8 if null |
| 9, 10 | Derived credit (reafference PE, all channels); no-self-label | **PROPHETIC** (spiking) | rate-analogue demonstration only; Gate A supplied credit externally | E-gap = crucible M1s2/M1s3 build item (outside this work order's minimum set; pre-existing build requirement) |
| 13 | In-band training (per-region σ) | **CLEAN** for the estimator finding (CRU-40 step 7: per-region dispersion vs pinned whole-pool σ) | — | E9/E10 for the band value |
| 15 wherein | Non-foldability of the constructed return | **PROPHETIC** as a running machine | exact algebra (3.2×10⁻¹⁵); unit-test current separation τ 2 vs 20; specified construction. No end-to-end run | **E1 — gating** |
| 15 (ii), (iii) | Delay / nonlinearity branches enabled | **PROPHETIC** | CRU-69 §4 taxonomy only | E5 |
| 16 | Factor-two constant separation | **UNSWEPT** | one working point (factor ten) | E9 |
| 17, 18 | Span = support argmin; rank/support < 0.1 | **FOLDED** | CRU-75 (72 architectures, 8/8 seeds) — folded arms | E2 |
| 19, 20 | Monotone relay-count fidelity cost; relay dynamics | **FOLDED** | CRU-70 (Spearman −1.000, 8/8); CRU-67 | E3 |
| — (spec technical-effect hook) | 7.9× synapse economy of the bottleneck return; 5.3–6.0× / 71.5–74% unroll cost | **FOLDED** | CRU-70 §3; CRU-58 | **E4 — the G 2/21 repair; without it the system family's effect-at-point-of-novelty is unsupported** |
| 23, 24 | Homeostatic regulation; per-region band in configured system | **CLEAN** (substrate) / **PROPHETIC** (with return active) | CRU-40 step 7; R0a | E10 |
| 25–29 | Storage, readout-fixing, efference, containment, τ ranges | **CLEAN** (structural, substrate-level) / ranges **UNSWEPT** | build record | E9 |
| 31–33 (family C) | Forward-direction redeployment; closed control loop; spiking substrate | **PROPHETIC** in the claimed direction | CRU-57 GO measured *inverse* direction, idealized learners, no control step; flat 0.000 by construction | **E8 — gating for family C** |

The one-line summary the attorney needs: **family A is filable on today's evidence; family B is
filable only after E1 (and credibly only after E4); family C is not filable on today's evidence.**

---

## 5. Design-around table v2 (Part C)

Every verdict below has been checked against the dependency structure: "caught" is asserted only
where an *independent* claim (or a Markush alternative of one) is infringed; a dependent is cited
only as narrowing an already-infringed independent. Escapes are named as escapes.

### 5.1 Against claim 1 (routed-credit training)

| # | Attempt | Verdict |
|---|---|---|
| A.1 | Plasticity everywhere / no alignment region (unrouted three-factor learning) | **ESCAPE — deliberately.** Unrouted three-factor learning is R1's own territory; fencing it is impossible and claiming it would be suicide. Cost to competitor: unmeasured today (Gate A's floor is decorrelated, not unrouted, credit) — E7 prices it. If E7 shows routing is load-bearing, the escape forfeits the measured benefit; if it shows routing is dispensable, family A's *commercial* scope is narrower than hoped and we should know before spending grant fees. |
| A.2 | Two or more trace values per synapse | **Caught** — claim 1 recites "independent of the number of neurons," not "exactly one." |
| A.3 | Externally supplied credit (supervised) | **Caught** — the independent does not require derived credit (claim 9 is the dependent). |
| A.4 | Omit the margin gate | **Caught** — the gate is not in the independent (claim 8 is the dependent). v1's §2.5(a) escape closed by demotion. |
| A.5 | Train the readout too (e-prop style) | **Caught by claim 1 as drafted** if plasticity into the alignment region is mask-confined and the FRAME→designated-region path is held fixed — claim 1 does not recite a fixed readout. A competitor who *also* frees the alignment→designated connections escapes — and has abandoned the routing structure entirely (= A.1). |
| A.6 | Train offline with surrogate gradients / BPTT, ship frozen | **ESCAPE for training-time infringement** (unchanged from v1 B.3.1, and unchangeable — training claims are practiced in private). Mitigations: the deployed system may still read on claim 15; any product that continues learning in the field re-enters claim 1. Named to counsel as the reason family A leads on validity but family B leads on enforcement — the portfolio needs both. |
| A.7 | Rate-based (non-spiking) implementation of the same routing | **ESCAPE from the priority claims** (claim 1 recites spiking; eligibility traces are drafted on spike activity). Continuation posture per v1 §2.6 — spec discloses the rate analogue (which is where the routed-credit idea was first demonstrated), preserving the chase. |
| A.8 | Route credit through a *different* interposed structure (e.g., multiplicative gating instead of masked plasticity) | Construction fight. The spec should define "connection mask" functionally (any mechanism restricting which connections receive weight updates) — drafting instruction to counsel. |

### 5.2 Against claim 15 (system, Markush)

| # | Attempt | Verdict |
|---|---|---|
| B.1 | Delay-only return | **Caught — Markush branch (ii) of the independent.** v1's dependent-claim fallacy repaired; verified: (ii) is an alternative *within* claim 15, not a narrowing of another branch. |
| B.2 | Nonlinearity-only return | **Caught — branch (iii).** Same repair. |
| B.3 | Per-edge heterogeneous synaptic τ | **Caught — branch (i)** (return edges necessarily carry states distinct from every recurrent state onto the re-injection targets), plus the functional wherein is satisfied. Scope-checked in §3.2. Residual risk: validity fight over obviousness of per-synapse kinetics + R4 feedback; defended on problem-discovery plus the combination's absence from the art. |
| B.4 | Per-neuron heterogeneous τ (Perez-Nieves style) | **ESCAPE — and self-defeating by the fold theorem** (§3.2: neuron-indexed states leave matrix additivity intact; the loop folds; the competitor ships an open network). The spec states the theorem and this consequence, converting the escape into a teaching (v1 B.1.2's logic, now correctly scoped). Honesty caveat carried from CRU-67: an open network may still be *functionally* competitive — this escape is only self-defeating for competitors who need a dynamically real loop. Competitors who don't were never inside the fence of any drafting. |
| B.5 | Dual kinetics everywhere, return on a shared receptor type | **ESCAPE — folds pathway-wise, same bin as B.4.** A return on kinetics *not* shared with recurrence onto the same targets is caught by (i). |
| B.6 | Relay-population return | **Caught-or-construction-fight, materially improved:** claim 20 recites it expressly; the spec defines readout/derived-signal/return-filter-state to cover relay projections (spec-definition instruction, §2 note to claim 20). A relay of k ≪ region-size neurons meets the low-dimensionality element; its membrane/synaptic states are distinct states in the (i) sense, its spiking is an interposed nonlinearity in the (iii) sense, and its integration imposes delay in the (ii) sense — the competitor must argue out of all three branches simultaneously. Residual: a relay population as large as the region evades the bottleneck element — and forfeits the bottleneck economics (E3/E4 price it). |
| B.7 | Unroll into feedforward-with-memory | **GENUINE ESCAPE — the expensive one** (unchanged from v1 B.1.4), with the honesty note that its price tags (5.3–6.0×, 7.9×) are folded-arm measurements until E4 re-runs them. |
| B.8 | Same-timestep / shared-filter linear re-entry ("we have a loop but not your construction") | **ESCAPE — self-defeating by theorem** (v1 B.1.2, retained; the exact algebra is in the spec). |
| B.9 | Off-substrate return (external processor re-injects) | **Caught** — claim 15's return path is not located inside the network; claim 21 makes it express. |
| B.10 | Dendritic/compartmental second constant | **Caught** — branch (i) as drafted does not say "synaptic"; claim 22 makes it express. |
| B.11 | Rate-based implementation | **ESCAPE from priority claims**; continuation posture (v1 B.1.6 unchanged). |

### 5.3 Against claims 31–33 (conditional redeployment family)

| # | Attempt | Verdict |
|---|---|---|
| C.1 | Relearn from scratch per entity | Escape by abstention; forfeits the measured sample-cost advantage (numbers to be re-cut forward-direction under E8 before being cited). |
| C.2 | Dedicated other-model (ToMnet route) | **GENUINE ESCAPE** — published art, unfenceable (v1 B.2.2 unchanged). |
| C.3 | Adapter at 12–15% of model parameters | **Closed by redraft:** the rebuilt independent (claim 31) rests on the *concurrent dual-use* limitation and the verification step, not on a bare parameter-ratio bound; the ratio is demoted to a dependent (claim 32). The red team's B.2.3 refutation (freezing preserves fidelity regardless of adapter size) is accepted — the ratio was never load-bearing and is no longer asked to be. |
| C.4 | Nonlinear adapter | Caught — independent leaves the transform unqualified. |

---

## 6. Work order for crucible — the minimum experiment set (Part D)

Each item names: what to run, on what arm, and what number supports what limitation. Ordering is by
gating power, not effort. Items E1–E5 are the system family's filing condition; E6–E7 harden the
lead family; E8 gates family C; E9–E10 harden numerical dependents. All are software runs on the
existing substrate; per CRU-69 the differential-τ construction is "a code change, not a research
program."

| # | Run | Arm / substrate | Deliverable number → supported limitation |
|---|---|---|---|
| **E1** | Implement the differential-τ return (`g_ret`, `a_ret ≠ a`, second spMV) on `RegionalLifPool`, wired ESM→(EWM,ISM); flip `test_a_shared_filter_leaves_the_matrix_decomposition_exact` to assert the decomposition **fails** (the record's own acceptance signal); run the banked cued-recall task end-to-end. | The unfolded loop — the claimed machine, first existence | A completed task run with the decomposition test failing → claim 15's wherein moves PROPHETIC → demonstrated. **Gates family B.** |
| **E2** | Re-run the span-law argmin (CRU-75 protocol; the 72-architecture grid or a justified reduction) with the E1 return in place of the folded rank-k term. | Unfolded loop | Argmin at span = support, ≥6/8 seeds → claims 17–18. If the span law does *not* survive unfolding, claims 17–18 are dropped — better to know now. |
| **E3** | Re-run the relay-count cost curve (CRU-70 protocol) through the unfolded loop, k = 1…8. | Unfolded loop | Monotone fidelity decline with k → claim 19; prices escapes B.6/B.7. |
| **E4** | Re-measure the synapse-economy figure: unfolded k=1 bottleneck return vs its best open/folded approximation **at matched task performance**, reporting synapse and memory cost. Design constraint from CRU-67 §10: expect the open rival to *tie on behavior*; the claimed effect is the cost gap, so the DV is resource cost at matched performance, never behavioral distinctness. | Unfolded loop vs open control | X× cost figure attributable to the distinguishing feature → the G 2/21 technical-effect hook for family B. **Without E4 the family files with no measured effect at its point of novelty.** |
| **E5** | Run the same banked task through (a) a delay-element return arm and (b) an interposed-nonlinearity return arm (the other two CRU-69 §4 breakers). | Two new arms | One completed run each → enablement of Markush branches (ii) and (iii) (each alternative must be supported, not just taxonomized). |
| **E6** | Margin-gate ablation on the Gate-A rig: learned arm with and without `hinge_margin`, same seeds. | Gate-A rig (loop-free) | If gate-OFF degrades: number → claim 8 gains support. If null: delete claim 8 and the gate leaves the spec's recipe emphasis. Either way the unmeasured conjunct stops being escape surface. |
| **E7** | Unrouted-plasticity control on the Gate-A rig: identical substrate and credit, `plastic_mask` removed (plasticity everywhere), vs the routed learned arm. | Gate-A rig | The routing premium (Δcorr routed vs unrouted) → claim 1's effect measured *at its point of novelty* (the current floor separates rule-from-wiring, not routed-from-unrouted). Also prices escape A.1. |
| **E8** | Redeployment in the committed **forward** direction: (a) forward-direction frame refit with the banked protocol; (b) close the loop — derive and execute control outputs through the redeployed model on any body, however simple; (c) the same refit hosted on the spiking substrate (`ClosureBrain`), reduced scale acceptable. | s1-successor protocol / spiking substrate | (a) forward held-out error vs relearn-from-scratch at matched budget; (b) any completed closed-loop episode; (c) any completed spiking-hosted refit → together they gate family C. Partial completion = family C stays out of the priority filing. |
| **E9** | Cheap CPU sensitivity sweeps for every claimed numeral: τ-ratio factor (claim 16), rank/support boundary (18), membrane-τ percentage (29), τ_elig range (spec), σ band width (13/24), target rate and margin (spec). | Existing rigs | Swept boundaries → each numerical dependent survives Art. 84/§112; anything unswept demotes to spec-example. |
| **E10** | Per-region σ estimation with the E1 return **active**: confirm the per-region subsampled estimator still resolves dispersion and pick the committed band. | Unfolded loop | Band value + in-band configuration record → claims 13/24 in the configured system. |

Sequencing note for the sibling project: E1 is a prerequisite of E2, E3, E4, E5(a-b share its
harness) and E10. E6/E7 are independent CPU-minutes items on the Gate-A rig and can run first.
E8 is independent of everything else. The binding calendar constraint is the priority filing before
MoC7 (Oct 12–16, 2026): if the E1-chain cannot complete in time, file family A alone on priority
and add family B in the PCT year — counsel to confirm that added claims at PCT keep the later
effective date only for the new matter (standard, but it must be a decision, not a drift).

---

## 7. Where this redraft disagrees with the red team

Stated per the standing instruction that an attacker overreaches sometimes; everything else in
`05-red-team.md` is accepted and acted on above.

1. **The §2.1 "free, performance-positive, total" characterization conflates two variants.** The
   published, performance-positive, R5-supported design-around (per-neuron heterogeneity) does not
   break the fold — neuron-indexed filter states leave `g(t)` independent of `W` and matrix
   additivity intact (CRU-69 §3's own algebra). The variant that does break the fold (per-edge
   kinetics) is not what R5 measured, costs O(E) rather than O(N) dynamic state, and is caught by
   the state-distinctness redraft. The dilemma is real (§3.3 names the surviving horn) but it is
   one contested variant wide, not the whole heterogeneity spectrum. The red team's *drafting*
   conclusion (the narrow claim is broken) was nonetheless correct and is adopted.
2. **"Negative cost" is overstated for the fold-breaking variant.** On Loihi-class hardware with
   per-synapse trace memory already provisioned, near-free; on the memory-constrained software and
   edge substrates that are this route's actual commercial case, per-edge filtering is a real
   constant-factor memory/compute cost. Minor, but it changes who would actually take the escape.
3. **The relay-population escape (§2.3) is priced too cheaply.** With claim 20 express, the spec
   definitions instructed in §2, and the relay simultaneously implicating all three Markush
   branches, the competitor's "excellent non-infringement narrative" becomes a three-front
   construction fight. It remains a risk, not a free door.
4. **Claim 23's survival was tested at dependent scope.** The red team's finding 6 attaches to the
   routed-credit *feature*; promoting it necessarily broadens the claim beyond what was attacked
   (the v1-claim-21 limitations no longer narrow it). The promotion is still right — but the
   professional pre-filing search on the promoted scope (§1 drafting note, red-team §7.8's CPC
   sweep) is mandatory, not optional, and this document says so rather than treating survival as
   transferable.

---

## 8. What was killed, plainly

- **v1 claim 16 and its family, as drafted:** dead on Bocsi 2013 + Houlsby 2019 + *Recentive*/G 1/19
  + inverse-direction-only evidence. Not refiled. Rebuilt narrowly as conditional claims 31–33
  (spiking-substrate-embedded forward model per claim 14/11 bridge; **concurrent dual-use** — the
  same model instance serving own-body control and entity prediction, the one candidate limitation
  in neither R2 nor R3; the claim-17 verification step folded into the independent; **actuation
  recited**, not "deriving outputs"; parameter ratio demoted to a dependent). Filed **only** if E8
  completes; otherwise spec-disclosed, continuation-chased. Draft text for 31–33 is held in this
  posture deliberately — writing polished claim language for an unfileable family spends attorney
  money in the wrong order; the structural decisions above are what counsel needs.
- **v1 claim 21, as drafted:** dead on Izhikevich 2007 + SORN/RM-SORN under KSR/Comvik. Not
  refiled. Elements redistributed into claims 1–13 as recorded in §1.
- **v1 claim 31 and the device family:** dead as an independent on Davies 2018 capability-level
  disclosure + wholly-prophetic status + configuration-enforcement posture. Replaced by system
  dependent claim 30 and spec-level hardware disclosure. No device independent is filed at
  priority; revisit at national phase only if silicon plans materialize.
- **The 7.9×/5.3–6.0× numbers as claim-support:** withdrawn from every validity argument until E4
  re-measures them on the claimed machine. They may still appear in the spec as measurements *of
  the folded comparator* (i.e., of the escape's cost), clearly labelled as such — that labelling is
  what makes CRU-69's discoverability survivable.

*End of claim architecture v2. Preparatory work product for patent counsel; not legal advice; no
filing decision should rest on this document alone.*
