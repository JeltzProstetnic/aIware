# Claim Architecture — the Crucible Implementation Route

**Preparatory drafting for briefing a patent attorney. Not legal advice.** No author of this document
is a patent attorney; nothing here may be filed as-is. Every claim below is a working draft whose
purpose is to make the attorney's first drafting pass cheap, targeted, and grounded in what the
crucible record actually supports. The attorney rewrites; this document tells them what to protect,
what art to clear, and where the evidence sits.

Prepared 2026-08-11. Companion to `01-patentability-strategy.md` (filing strategy, disclosure
chronology, employer analysis — its conclusions are taken as given here) and
`02-prior-art-landscape.md` (verified art; its fenced neighbourhoods are designed around below).

**The inventor's brief, verbatim:** *"I would like to patent the actual way to implement it without
extreme pain, which is 'take a spiking neural net with... recurrence... closure...' in a way that
makes it as painful as possible to circumvent while leaving me as much publication freedom as
possible."*

---

## 0. The three constraints, unpacked — and the publication-freedom answer first

**0.1 Publication freedom has a clean answer, and it should reframe the whole plan: file first,
then publish everything.** Once a priority application is on file, the inventor's own *subsequent*
publications cannot invalidate that family — novelty is assessed at the priority date. The quiet
period is therefore **only the interval between today and the priority filing**, not an indefinite
regime of secrecy. Concretely:

- Nothing in the claims below depends on keeping any *theoretical* material secret. All FMT theory is
  already public (2015 monograph → Zenodo v14 → public GitHub mirror) and is treated throughout as
  prior art against ourselves — the claims are drafted to be novel *over our own publications*.
- What must stay unpublished **until the priority date only** is the implementation layer: the
  differential-τ return construction, the local-rule training recipe as a recipe, the emergence
  protocol, the redeployment protocol details, the decompilation pipeline. After filing: publish all
  of it, at full speed — MoC7 poster, v15, OSF preregistration, Show-HN code, everything.
- The binding calendar item is unchanged from `01`: **priority filing before MoC7 (Oct 12–16, 2026)**
  and before any of the autumn disclosure wave.

**0.2 Claim the route, not the theory.** The theory is public and unpatentable everywhere. The asset
is the *practical recipe*: the specific structural and procedural choices that let an engineer get a
working self-referentially-closed spiking system without re-deriving crucible's dead ends — the fold
trap and its repair, the reservoir inversion, the credit-routing rule, the per-region operating-point
discipline, frame-only redeployment. Every claim below is a fence on a piece of that route.

**0.3 Circumvention pain is manufactured in the dependents, and the honest goal is *costly*, not
*impossible*.** FMT's own published No-Free-Lunch passage guarantees a design-around exists (unroll
the loop into feedforward-with-memory). The measured answer is that this escape is expensive —
crucible has *quantified* the cost (§B) — and the claim set is arranged so that every *cheap* escape
lands on a dependent or sibling claim. Genuine escapes are named as such in §B; there are four.

---

## 1. Vocabulary map — the consciousness-free claim lexicon

The word "consciousness" appears nowhere in the claims, nor do "self-model," "world-model,"
"qualia," "closure" or any FMT term of art. The specification's background section may cite the
published theory; the claims use only the left column. This table also fixes internal-name ↔
claim-term correspondence for the attorney.

| Claim term | Internal name (crucible) | What it is |
|---|---|---|
| first region / sensory-processing region | EWM | region driven by exteroceptive input |
| second region / state-summary region | ESM ("self-loop region") | region whose activity summarizes system state and receives the efference copy |
| third region / proprioceptive region | ISM ("body model") | region driven by proprioceptive/body-state input |
| central region | CE ("engine") | main recurrent processing region |
| return path | closure loop / re-entry | readout of the second region re-injected into the network |
| return filter state / second synaptic filter | the differential-τ fix (CRU-69/83) | separate low-pass state with its own time constant on the return path |
| bottleneck / low-dimensional signal | the span-law bottleneck (A#9) | rank-k readout, k ≪ region size |
| span of the return path | span σ | the set of regions the return re-injects into |
| edge-indexed eligibility trace | sparse three-factor rule (CRU-57 s1e) | one scalar trace per stored synapse (CSR edge) |
| third factor / modulatory credit signal | reward / credit | the global-or-routed modulator in the three-factor rule |
| margin gate | hinge gate (`hinge_margin`) | update applied only when error exceeds margin |
| firing-threshold regulator | homeostasis (`_homeostatic_step`) | per-neuron adaptive threshold from rate EMA |
| branching parameter | branching σ | per-region subsampled activity-propagation ratio |
| alignment transform / frame | the frame (CRU-57/83) | small map aligning a trained forward model to a new body/entity |
| forward model of the agent's body | ĝ | learned map (state, action) → next sensory state |
| reafference prediction error | derived credit (§11.1 of the M1s3 prereg) | predicted-vs-actual next sensory input, all channels |
| fixed readout | frozen random readout (reservoir inversion) | readout never trained; plasticity confined to recurrence |

---

## 2. The claim set

### 2.1 Family overview

| Ind. claim | Category | Drawn primarily for | Eligibility hook (one line each) |
|---|---|---|---|
| **1** | System / apparatus | EPO (and US) | EPO Art. 52 / G 1/19: claimed as a *control system of an embodied agent* — direct link to physical reality (sensor in, actuator out), not a simulation as such; plus implementation-internal effect (7.9× synapse economy of the bottleneck return, measured CRU-70 §3). US §101: *Enfish*-style specific architecture improving the machine's own capability. |
| **16** | Computer-implemented method of operating | EPO + US | EPO: method of controlling a technical system (agent interacting with an external physical entity); measured technical effect = sample-efficiency at matched budget (CRU-57 GO). US: specific improvement to the ML method (few-shot transfer by structural reuse), *Recentive*-distinguished. |
| **21** | Training / configuration method | US-led (EP parallel) | EPO route (ii), G-II 3.3.1: architecture/training adapted to the internal functioning of the computer — O(E) vs O(N²) memory (0.06 GB vs ~2.5 GB/step at 25k neurons, measured), locality enabling on-chip learning. US: improvement to the training method itself, squarely inside the *Recentive* safe zone. |
| **31** | Neuromorphic hardware device | EPO strongest; US parallel | Hardware organization claim — memory layout, filter banks, on-chip plasticity engine. Eligibility unproblematic in both offices. |

Computer-readable-medium claims mirroring 16 and 21 are routine adjuncts for the US filing and are
not drafted out here. A rate-network generalization of claim 1 is held as a continuation candidate
(§2.6), not in the priority independents.

---

### 2.2 System family — claims 1–15

> **Claim 1 (independent — system).**
> A control system for an embodied agent, comprising:
> a sensor interface arranged to receive sensory signals from at least one sensor of the embodied
> agent;
> an actuator interface arranged to issue motor commands to at least one actuator of the embodied
> agent;
> a recurrent network of spiking neurons partitioned into a plurality of regions, the plurality of
> regions comprising at least a first region coupled to receive the sensory signals and a second
> region coupled to receive a copy of the motor commands, wherein neurons of at least two different
> regions are assigned different membrane time constants;
> recurrent synaptic connections among the neurons, wherein synaptic transmission over the recurrent
> synaptic connections is low-pass filtered by a shared synaptic filter state having a first filter
> time constant;
> a readout arranged to derive from spike activity of the second region a signal of dimensionality
> lower than the number of neurons of the second region; and
> a return path arranged to re-inject the derived signal as input to neurons of at least the first
> region,
> **wherein the return path comprises a return filter state separate from the shared synaptic filter
> state, the return filter state having a second filter time constant different from the first filter
> time constant, such that the input contributed by the return path is not expressible as an additive
> rank update to a recurrent weight matrix acting on the shared synaptic filter state**;
> and wherein the motor commands are derived at least in part from spike activity of the recurrent
> network.

*Drafting notes on claim 1.* (a) The bolded limitation is the crown jewel and it is **structural**:
two filter states, two time constants, and a mathematically testable consequence (non-foldability —
the additive decomposition `I[W_bulk+W_ret] = I[W_bulk] + I[W_ret]` fails). It encodes the
fold-algebra discovery (CRU-69/CRU-83 §13.1: a same-timestep return, and equally any return sharing
the uniform synaptic filter, folds *exactly* — verified to 3.2×10⁻¹⁵ — into an open network; the
repair is a second filter state with its own constant, demonstrated to separate currents at τ 2 vs
20). A competitor who omits it has, by our own theorem, built a system whose "loop" is algebraically
an open network — see §B row 1.2 for why that is a self-defeating escape. (b) "Copy of the motor
commands" is the efference copy; it is delivered by a fixed projection (dependent 12), which is how
`SENSORY_ROUTING_V3` implements it. (c) The claim never says what the second region *represents* —
no functional self-model language, which is precisely the gap Kadin claims and we avoid.

> **Claim 2.** The system of claim 1, wherein the second filter time constant differs from the first
> filter time constant by at least a factor of two.

*(Measured separation demonstrated at a factor of ten, τ_syn 2 vs 20; factor-two is the retreat
position and must be re-verified before filing — see §D.5.)*

> **Claim 3.** The system of claim 1, wherein the return path further comprises a delay element
> imposing a transmission delay on the derived signal exceeding the transmission delay of the
> recurrent synaptic connections.

> **Claim 4.** The system of claim 1, wherein the return path further comprises a nonlinear
> transformation interposed between the readout and the re-injection.

*(Claims 3–4 place the other two fold-breakers — delay and interposed nonlinearity, the complete set
identified by the fold analysis — inside the family, so a competitor swapping breaker for breaker
stays inside. If counsel prefers, 1's wherein-clause can be drafted Markush-style over all three
breakers with the non-foldability consequence as the common functional wherein; the three-dependent
form is presented because it keeps claim 1's point of novelty singular and structural.)*

> **Claim 5.** The system of claim 1, wherein the plurality of regions further comprises a third
> region coupled to receive proprioceptive signals of the embodied agent, and wherein the return path
> re-injects the derived signal into neurons of both the first region and the third region.

*(The span-law claim: the return spans the support of the content it carries — world plus body
(CRU-75: argmin over 72 enumerated architectures, 8/8 seeds, span = support exactly; less is a hard
ceiling, 0/8 at any rank).)*

> **Claim 6.** The system of claim 5, wherein the dimensionality of the derived signal is smaller
> than one tenth of the number of neurons spanned by the re-injection.

*(The low-rank bottleneck. The measured selection boundary (rank/support ≈ 0.05–0.1 favourable,
≥ 0.19 never selected — CRU-75 §6) supports an order-of-magnitude limitation; the precise scaling
law is open (CRU-82), so the claim uses a conservative ratio and the spec reports the measured
boundary as an example, not a limit.)*

> **Claim 7.** The system of claim 1, wherein the return path comprises at most one intermediate
> relay stage between the readout and the re-injection.

*(The short-return claim. Measured: trajectory-tracking fidelity declines monotonically with relay
count k, 8/8 seeds, Spearman −1.000, with a genuine latency share of 40% after the size-matched
null; the bottleneck's synapse-cost advantage over the folded equivalent erodes ~8× in exchange-rate
headroom from k=1 to k=8 (CRU-70). A competitor lengthening the return to avoid claim 7 pays a
measured fidelity and cost penalty — pain by design.)*

> **Claim 8.** The system of claim 1, further comprising a firing-threshold regulator arranged to
> adapt, for each neuron, a firing threshold by negative feedback from a running average of that
> neuron's firing rate toward a target rate.

> **Claim 9.** The system of claim 8, wherein a gain of the recurrent synaptic connections is set
> such that, for each region of the plurality of regions, a branching parameter estimated from spike
> activity of a fixed-size subsample of that region lies within a predetermined band around unity.

*(The criticality claim, drafted to clear Cramer et al. 2020: Cramer controls distance-to-criticality
of a single undifferentiated population by homeostatic plasticity; claim 9 requires (i) a region
taxonomy, (ii) the *per-region subsampled* estimator — motivated by the measured finding that the
whole-pool estimator is pinned at σ≈1 and uninformative at ≥22k neurons while per-region 256-channel
estimates resolve genuine dispersion (CE 0.978 / ESM 0.972 / ISM 1.119 / EWM 0.342, CRU-40 step 7) —
and (iii) all-regions-in-band as the configuration condition. Deliberately a dependent, not an
independent: criticality alone is the most NPA-crowded of our features.)*

> **Claim 10.** The system of claim 1, wherein the recurrent synaptic connections are stored in a
> compressed edge-indexed representation with a fixed per-neuron fan-in.

> **Claim 11.** The system of claim 1, wherein weights of the readout are fixed during operation and
> during training of the recurrent synaptic connections, and wherein synaptic plasticity is confined
> to the recurrent synaptic connections.

*(The reservoir inversion: plastic recurrence + fixed readout — the exact structural opposite of the
expired ESN/LSM tradition, and distinguished from e-prop, which trains readouts. Measured: plastic
recurrence learns delayed cued-recall to 0.966 while the frozen recurrence's best-fit readout sits
near chance, at 25,000 neurons in 0.06 GB (CRU-57 s1e).)*

> **Claim 12.** The system of claim 1, wherein the copy of the motor commands is delivered to the
> second region by a fixed, non-plastic projection.

> **Claim 13.** The system of claim 1, wherein the neurons receiving the re-injected signal include
> neurons whose activity is also driven by the sensory signals, whereby the derived signal and the
> sensory signals share a common state space.

*(The containment limitation — the structural residue of `O_ESM ⊆ S_EWM`, stated entirely as wiring.)*

> **Claim 14.** The system of claim 1, wherein the return filter state is implemented as a distinct
> dendritic or compartmental state of the re-injection target neurons, the compartment having its own
> filter time constant.

*(Closes the "I put the second time constant in a dendrite, not a synapse" design-around.)*

> **Claim 15.** The system of claim 1, wherein membrane time constants are assigned per region and
> differ between the first region and the second region by at least 25%.

*(Per-region τ heterogeneity as an explicit limitation; supported by `RegionalLifPool` per-neuron
τ vectors and the DEFAULT_REGIONAL re-tune record (EWM τ 10→15–20 vs others ~8–10). The exact
percentage needs a decided configuration before filing — §D.5.)*

---

### 2.3 Operating-method family — claims 16–20

> **Claim 16 (independent — computer-implemented method of operating).**
> A computer-implemented method of controlling interaction of an embodied agent with an external
> dynamical entity, the method comprising:
> providing, within a control system of the embodied agent, a trained forward model that predicts
> sensory consequences of the agent's motor commands, the forward model having been trained on
> sensorimotor experience of the agent's own body;
> holding all parameters of the trained forward model fixed;
> training an alignment transform that maps between an observation space of the external dynamical
> entity and an input-output space of the forward model, the alignment transform having fewer
> trainable parameters than one tenth of the number of parameters of the forward model;
> generating predictions of the external dynamical entity's behaviour by applying the fixed forward
> model through the trained alignment transform; and
> deriving, from the predictions, control outputs of the embodied agent.

*Drafting notes.* This is the redeployment mechanism (CRU-57 kill-first GO, pre-registered, 8
seeds): refitting only a 36-parameter frame through a frozen model reaches held-out error ≈ 0.000
where relearning from scratch costs 0.178–0.883 (growing with model richness) and a wrong-body model
provides no transfer at all. The parameter-ratio limitation (36 vs ≈840 model parameters measured ≈
4%) is what separates redeployment from disguised relearning. No "theory of mind" language, no
self-model language: it is a transfer-learning method with a structural reuse condition. Rabinowitz
ToMnet (trains a *separate* other-model) and Bongard/Lipson (re-uses a self-model after *damage to
the same body*, not to model an external entity) are the art to distinguish in the spec.

> **Claim 17.** The method of claim 16, further comprising verifying, after training the alignment
> transform, that predictions of the forward model for the agent's own body, read through a readout
> whose weights were fixed before the training of the alignment transform, remain within a
> predetermined tolerance of their pre-training accuracy.

*(The absorption guard as a positive method step — frozen-readout fidelity retention. Turns a QA
control into a claim covering any competitor implementing safe redeployment.)*

> **Claim 18.** The method of claim 16, wherein the alignment transform is a linear map.

> **Claim 19.** The method of claim 16, wherein the forward model is embedded in a recurrent network
> of spiking neurons of a control system according to claim 1.

*(Ties the two families; also the anchor for unity-of-invention.)*

> **Claim 20.** The method of claim 16, wherein the predictions are generated at a recursion depth of
> one, the forward model not being applied to a representation of the external dynamical entity's
> model of the embodied agent.

*(The counter-intuitive shallow-recursion bound — everyone else scales depth. Non-obviousness
asset. Support today is design-level (the depth axis was deliberately corrected away in CRU-57);
this claim is prophetic and flagged as such in §C.)*

---

### 2.4 Training-method family — claims 21–30

> **Claim 21 (independent — training method).**
> A computer-implemented method of training a recurrent network of spiking neurons to control an
> embodied agent, the method comprising:
> storing recurrent synaptic connections of the network in a compressed edge-indexed representation;
> fixing weights of a readout of the network prior to training and holding them fixed throughout
> training;
> maintaining, for each stored synaptic connection, exactly one scalar eligibility trace, updated
> locally from pre-synaptic and post-synaptic spike activity of that connection and decaying with an
> eligibility time constant;
> computing a modulatory credit signal;
> updating weights of the recurrent synaptic connections as a function of the product of the
> respective eligibility trace and the credit signal, wherein the update is applied only when an
> error measure exceeds a margin;
> and concurrently adapting, for each neuron, a firing threshold by negative feedback from a running
> average of that neuron's firing rate toward a target rate,
> whereby memory required for training scales with the number of stored connections rather than with
> the square of the number of neurons.

*Drafting notes.* Every element is measured: the edge-indexed trace and the O(E) memory consequence
(0.06 GB at 25k neurons vs ~2.5 GB *per step* for the dense outer-product rule); the hinge gate and
feedback-alignment credit (`apply_reward(target·W_out)`, the locked R0b-2 recipe, transferred to the
sparse substrate with no retuning); homeostasis as a *requirement* for stable plastic learning
(measured: OFF → drift and collapse). Novelty over Bellec e-prop is carried by the **combination**:
e-prop trains readouts and derives its learning signal by broadcasting a loss gradient; claim 21
requires the fixed readout (reservoir inversion), the margin gate, and concurrent homeostatic
threshold adaptation, and its whereby-clause states the internal-functioning effect the EPO route
(ii) rewards. The final whereby also does the *Recentive* work in the US: this is an improvement to
the training method itself, not "apply ML to X."

> **Claim 22.** The method of claim 21, wherein the credit signal is derived by the network itself as
> a reafference prediction error between predicted and actual subsequent sensory input, computed over
> all sensory channels without selection of a subspace of channels.

*(Derived credit, the §11.1 decision. Demonstrated in the rate-based analogue; not yet demonstrated
on the spiking substrate — the current `apply_reward` path lands a harness-computed vector. Partial
prophetic status flagged in §C/§D.)*

> **Claim 23.** The method of claim 21, wherein the credit signal is applied to connections into an
> alignment region interposed between a sensory input and a designated region of the network, and
> wherein plasticity is confined, by a connection mask, to the connections into the alignment region.

*(The credit-routing structure of Gate A: OBS→FRAME plastic under `plastic_mask`, FRAME→SELF and
SELF→SELF fixed. Measured: the local rule reaches 92.4% of the hand-wired ceiling (learned +0.891 vs
oracle +0.965) against a decorrelated-credit floor of −0.003, permutation p = 0.0001, 8 seeds.)*

> **Claim 24.** The method of claim 21, wherein plastic connections are initialized with connection
> signs determined by a per-source-neuron sign assignment and with random magnitudes, and wherein
> connections whose stored sign contradicts the sign assignment of their source neuron are rejected
> at construction.

*(The Dale-sign construction guard — the defect that would otherwise silently untrain the inhibitory
half of the support. A cheap claim that any careful implementer will infringe.)*

> **Claim 25.** The method of claim 23, wherein each scalar dimension of the sensory input is
> connected to the alignment region through at least one excitatory and at least one inhibitory
> population pair, whereby coefficients of either sign are realizable under the sign assignment.

*(Antagonist-complete support — Stage 0b: a randomly drawn support cannot realize negative
coefficients; four populations per input dimension is the recorded working configuration.)*

> **Claim 26.** The method of claim 21, further comprising pinning the adapted firing thresholds to
> fixed values during any evaluation of network outputs used to assess training progress.

*(θ-pinning. Measured failure mode it prevents: free-running homeostasis inverts the carried code,
corr +0.968 → −0.937 over a long scoring window. Another claim every competent implementer will hit.)*

> **Claim 27.** The method of claim 21, comprising a first stage in which the network is trained on
> sensorimotor experience of the embodied agent's own body to form a forward model, and a second
> stage in which, with parameters of the forward model held fixed, only an alignment transform is
> trained to adapt the forward model to a changed body or to an external dynamical entity.

*(The staged protocol; bridges to claim 16.)*

> **Claim 28.** The method of claim 22, wherein no training signal, reward definition, or input
> labelling identifies any subset of sensory channels as pertaining to the embodied agent's own
> body.

*(The no-self-label route — the emergent variant. Deliberately a **dependent**: a negative
limitation narrows, and a commercial competitor would happily hand-wire the self/world partition, so
the independent must catch the labelled route too. Claim 28 exists to cover the scientifically
strong variant and to anchor written description for the emergence protocol.)*

> **Claim 29.** The method of claim 21, wherein the eligibility time constant is between 5 and 100
> update steps.

*(Measured working value 40 (`tau_elig=40`, locked recipe); the range needs a sensitivity sweep
before filing if it is to survive examination — §D.5.)*

> **Claim 30.** The method of claim 21, wherein training is conducted while, for each region of a
> plurality of regions of the network, a branching parameter estimated from a fixed-size subsample of
> that region lies within a predetermined band around unity.

*(Plasticity-at-the-operating-point; pairs with claim 9 and inherits its Cramer-clearing structure.)*

---

### 2.5 Neuromorphic-hardware family — claims 31–35

> **Claim 31 (independent — neuromorphic device).**
> A neuromorphic processing device comprising:
> a plurality of neuron circuits organized into a plurality of regions, each region having a
> configurable membrane-time-constant parameter set, wherein at least two regions are configured
> with different membrane time constants;
> synapse memory storing synaptic connections in a compressed edge-indexed representation, each
> stored connection comprising a weight field and exactly one eligibility-trace field;
> a first synaptic filter circuit, shared by recurrent synaptic connections, having a first filter
> time constant;
> a second synaptic filter circuit, serving connections of a return path from a designated readout
> of one region to neuron circuits of at least one other region, the second synaptic filter circuit
> having a second filter time constant different from the first;
> an on-device plasticity engine configured to update each stored weight as a function of the
> corresponding eligibility-trace field and a broadcast credit value, gated by a margin condition;
> per-neuron threshold-adaptation circuits; and
> a sensor input interface and an actuator output interface.

*Drafting notes.* This is claim 1 + claim 21 recast as memory organization and filter banks — the
level at which the BrainChip estate does *not* sit. BrainChip US 8,250,011 claims the digital STDP
synapse circuit itself (binary "neurotransmitter" registers + temporal integrator); claim 31 claims
the **regional organization, the dual-filter return path, and the one-trace-per-edge memory
layout**, none of which that family recites, and is agnostic as to the synapse circuit style
(digital, analog subthreshold, memristive — dependent claims can enumerate). The local rule is
exactly what neuromorphic hardware can run on-chip; the commercial hook and the Art. 52 argument are
the same fact. Enablement is at the architecture/data-structure level (fully specified and measured
in software); no silicon exists — prophetic hardware examples in the spec, which `01` §2.3 already
flags as acceptable and which counsel must bless.

> **Claim 32.** The device of claim 31, wherein the eligibility-trace fields decay with a
> configurable eligibility time constant and the plasticity engine operates without storing any
> matrix of dimension number-of-neurons by number-of-neurons.

> **Claim 33.** The device of claim 31, wherein the threshold-adaptation circuits adapt each neuron
> circuit's firing threshold by negative feedback from a running average of its firing rate toward a
> configurable target rate.

> **Claim 34.** The device of claim 31, further comprising circuitry configured to estimate, per
> region, a branching parameter from a fixed-size subsample of that region's spike activity and to
> expose the estimate for gain configuration.

> **Claim 35.** The device of claim 31, wherein the second synaptic filter circuit is implemented as
> a per-target-neuron compartmental filter having its own time constant.

---

### 2.6 Held back for continuations / divisionals (not in the priority independents)

- **Rate-network generalization of claim 1.** The fold algebra and all three breakers were derived
  and verified on rate (tanh) networks in tier A, so a generalized independent ("recurrent neural
  network" without "spiking") is *technically* supportable — but it walks toward Kadin's functional
  neighbourhood and Dreamer's world-model estate, and dilutes the spiking-structural novelty story.
  Recommended: keep the priority spec's disclosure broad enough to support it (describe the tier-A
  rate implementation as an embodiment), and let a US continuation chase it once the examiner's
  reaction to claims 1–15 is known. This is the §3-of-`01` continuation posture doing its job.
- **Decompilation / readout cluster (CRU-72, L7).** Not built — design intent only. Filing now would
  be wholly prophetic with real §112/Art. 83 exposure and weak claim language ("locating explicit
  models in a running substrate" is dangerously functional). Recommendation: **describe the pipeline
  in the priority spec at whatever level the design record supports** (so later continuations have
  basis) **but claim nothing on it now.** Revisit at PCT or national phase.
- **Self-model-survival three-DV scheme** (task performance / retained fidelity on the old body /
  frame-approximation quality) as a *certification method* — a method of verifying that an adapted
  control system retained its original model. Small, but a plausible regulatory-compliance hook.
  Continuation material.
- **Emergence-protocol control arms** (delay-line, nonlinear-feedforward, detuned, scrambled,
  foreign-body, AUX) as method-of-validating claims. Same category.

---

## 3. Novelty over the named art — claim by claim

The two patent neighbourhoods and two NPA anchors `02` flags as most dangerous, taken in turn.

**3.1 Kadin US 11,119,483 / 11,906,965 (functional self-in-world-model, active to 2039, US-only).**
Kadin claims *functions*: an ANN that "identifies the self," constructs a "dynamical predictive
model of the environment" containing the self, with "repeated activation of a model of the self."
No spiking substrate, no return-path structure, no filter states, no training mechanics.
— Claim 1 is clear because its point of novelty is the two-filter-state return construction plus the
region taxonomy — pure structure Kadin nowhere recites; claim 1 also never states that anything
"identifies the self."
— Claims 16/21/31 do not overlap Kadin's category at all (he has no training or transfer method and
no hardware organization).
— *Trap avoided in both directions:* we neither infringe his functional language in our claims (no
"model of the self" appears) nor repeat his mistake (every load-bearing limitation here is
structural or procedural, not aspirational).

**3.2 Google US 12,533,800 (Dreamer — latent-imagination world-model planning, active).**
Dreamer claims training a policy on imagined latent trajectories inside a learned world model.
— No claim here contains "planning inside a learned model" as a load-bearing element. Claim 16's
forward model is used for *entity prediction via a fixed model + trained alignment transform* —
Dreamer has no fixed-model/frame split, no transfer to external entities, and no spiking substrate.
— Claim 1's return path re-injects a *low-dimensional readout of a region's spike activity* into a
sibling region of the same recurrent substrate — not a latent rollout, no imagined trajectories, no
policy-gradient training step.

**3.3 DeepMind EWC family (importance-weighted consolidation; number unpinned, survived §101).**
EWC consolidates by penalizing changes to parameters important to a prior task.
— No claim here recites parameter-importance weighting, penalty terms, or task-sequential
consolidation. The nearest concept (consolidation through sustained re-entry, feature F5 of `02`)
is deliberately **not claimed in this set** — the crucible record does not yet contain a banked
train-with-loop/test-loop-removed transfer result on the real substrate, so F5 stays in the spec as
disclosed-but-unclaimed until it is measured (§D.3). Disclosing it in the priority spec preserves
continuation rights while keeping the granted set clean of the EWC neighbourhood.

**3.4 Cramer et al. 2020 (plasticity-controlled criticality on neuromorphic hardware) — NPA.**
Cramer demonstrates homeostatic plasticity tuning distance-to-criticality of a single reservoir
population on BrainScaleS-2, with task performance tracking the operating point.
— Claims 9/30/34 are drafted on what Cramer does not show: a *region taxonomy* with *per-region
subsampled* branching estimation and an *all-regions-in-band* condition, inside an architecture with
a structurally distinct return path. The measured motivation (whole-population σ is pinned and
uninformative at scale; per-region estimates resolve real dispersion) is itself the non-obviousness
story: the skilled person following Cramer measures the whole pool and learns nothing.
— Criticality never appears as an independent claim, because as an isolated feature it is dead on
Cramer.

**3.5 Bellec et al. 2020 (e-prop) — NPA.**
e-prop trains the recurrence of an SNN with local eligibility traces and a learning signal derived
from a broadcast loss.
— Claim 21 is clear of e-prop on four combined limitations e-prop lacks: (i) the readout is fixed
and never trained (e-prop trains readouts); (ii) the margin gate; (iii) concurrent homeostatic
threshold adaptation as a claimed step (measured as *required* for stability here); (iv) exactly one
scalar trace per stored edge in a compressed representation with the O(E) whereby-clause. Claim 22
(reafference-derived credit computed by the network itself) and claim 23 (credit routed through a
masked alignment region) have no e-prop counterpart at all.
— Honest note: e-prop makes a *single-feature* claim on "local eligibility traces in SNN training"
unpatentable. Claim 21 is a combination claim by necessity, and §B.3 names the resulting escape.

**3.6 Reservoir tradition (ESN/LSM/FORCE — expired or NPA).**
Fixed recurrence + trained readout is free art. Claim 11/21's inversion (plastic recurrence + fixed
readout) is the structural opposite, and the measured attributability control (frozen recurrence's
best-fit readout at chance, G-I2) is the evidence that the inversion is doing real work. FORCE
trains a readout with feedback — it does not confine plasticity to the recurrence, and its feedback
shares the network's single filter path (foldable under our own algebra — a nice spec argument).

**3.7 Bongard/Zykov/Lipson 2006, Kwiatkowski & Lipson 2019 (self-modeling robots) — NPA.**
Published, unpatented; a robot induces its own body model and re-uses it after damage.
— Claim 16 is distinguished on: transfer target is an *external dynamical entity* (not the same
robot after damage); the fixed-model/low-parameter-alignment-transform split with the parameter-ratio
bound; the frozen-readout fidelity-retention step (claim 17). Lipson's line refits or re-induces the
model; it does not hold the model fixed and train a bounded alignment transform. The spec should
cite them and make exactly this contrast.

---

## B. The design-around table

For each independent claim: the moves a competent competitor would try, and the honest verdict.
**Genuine escapes are bolded and named — there are four.**

### B.1 Against claim 1 (system with non-foldable return)

| # | Design-around attempt | Verdict |
|---|---|---|
| 1.1 | Replace the differential-τ return filter with a **delay element** or an **interposed nonlinearity** | **Caught** — claims 3, 4. The fold analysis identified exactly three breakers; all three are in the family. |
| 1.2 | Keep the loop but let it share the uniform synaptic filter (or use same-timestep linear re-entry) — "we have a return path but not your filter state" | **Self-defeating, not caught, and that is fine.** By the fold theorem (verified to 3.2×10⁻¹⁵) such a return is *exactly* an additive rank update to the recurrent matrix — an open network. The competitor has not designed around the invention; they have declined to build it. If their product works anyway, closure was never load-bearing for them and they were never in this market. The spec should state the theorem: it converts this escape into a teaching. |
| 1.3 | Implement the second time constant as a **dendritic/compartmental state** instead of a synaptic filter | **Caught** — claim 14 (and claim 35 on hardware). |
| 1.4 | **Unroll the loop** into a deep feedforward network with memory (the design-around FMT's own published No-Free-Lunch passage hands every reader) | **GENUINE ESCAPE — the expensive one, and quantified.** Structural: preventing return outright costs 71.5–74% of the connectome vs 12–14% for merely re-arranging it (5.3–6.0× multiplier, exact, scale-free, CRU-58). Wiring: the folded functional equivalent of the k=1 bottleneck return costs 7.9× the synapses (15,876 vs 2,016, CRU-70 §3). This escape exists, is legal, and is the costly regime — which is the realistic goal. Name it to the attorney as the accepted boundary of the fence. |
| 1.5 | **Lengthen the return** through many relay stages to avoid the short-return dependent | Escapes claim 7 only; still inside claim 1. And pays a measured monotone fidelity penalty (latency share 40% of a 0.909→0.543 decline) and ~8× exchange-rate erosion of the cost advantage. Costly, partially caught. |
| 1.6 | **Rate-based (non-spiking) implementation** of the same return construction | **GENUINE ESCAPE from the priority claims as drafted** (claim 1 recites spiking). Mitigation: the spec discloses the rate embodiment (tier A) so a continuation can chase it (§2.6); and a rate implementation forfeits the O(E)/energy story that makes the route commercially attractive on edge/neuromorphic hardware. Partially mitigated, honestly open. |
| 1.7 | Move the return loop **outside the substrate** — e.g., an external processor or LLM reads the readout and re-injects | Ambiguous under claim 1 (the claim does not require the return path to be internal). Drafting instruction to counsel: keep "return path" free of any limitation locating it inside the network, so an external-loop implementation with its own filter/delay still reads on the claim. If counsel cannot hold that breadth, add a dependent expressly covering an off-substrate return path. |

### B.2 Against claim 16 (redeployment)

| # | Design-around attempt | Verdict |
|---|---|---|
| 2.1 | **Relearn from scratch** per entity (no reuse) | Escape by abstention — and the measured cost is the point: sample cost grows with model richness (0.178→0.883 at matched budget; 5–14× at reference K), i.e., the escape forfeits exactly the efficiency the patent tolls. Acceptable. |
| 2.2 | Train a **dedicated other-model** (ToMnet route) | **GENUINE ESCAPE** — independently published art we neither can nor should fence. It costs full per-target training data, which is the same expensive regime as 2.1. Named. |
| 2.3 | Refit **more than the alignment transform** (partial fine-tuning of the model) to dodge the parameter-ratio bound | The ratio bound (one tenth) catches small adapters; a competitor fine-tuning above the bound is drifting into 2.1's cost regime and loses the retained-fidelity property claim 17 covers (absorption destroys the old model — measured rationale in the DV1 cheat analysis). Caught-or-costly. |
| 2.4 | Use a **nonlinear adapter** instead of a linear frame | Caught — claim 16 does not require linearity (claim 18 is the narrowing dependent). Drafting discipline: keep the independent's transform unqualified. |
| 2.5 | Apply the model at **deep recursion** to avoid claim 20 | Claim 20 is a dependent; depth does not escape claim 16. (And the shallow bound is the *efficient* choice.) |

### B.3 Against claim 21 (training method)

| # | Design-around attempt | Verdict |
|---|---|---|
| 3.1 | Train with **BPTT / surrogate gradients on GPU**, deploy frozen weights | **GENUINE ESCAPE for training-time infringement — and the deeper enforcement problem: training claims are infringed in private.** Mitigations, both structural: (i) the deployed *system* still reads on claim 1 regardless of how it was trained; (ii) the escape forfeits on-chip/continual learning — any product that keeps learning in the field re-enters claim 21. Name this to counsel as the reason the system claim, not the training claim, is the enforcement lead. |
| 3.2 | Use **e-prop** (trained readout, broadcast learning signal) | Escapes claim 21 — deliberately, since e-prop is prior art we must be novel over, not a competitor practice we can fence. The competitor gives up the fixed-readout inversion and its measured attributability, and on-chip they still need trace memory per synapse (claim 32's layout may still catch the hardware). Accepted boundary. |
| 3.3 | Drop the **homeostasis step** | Caught by nothing narrower — but measured to fail: without homeostatic co-regulation the plastic recurrence drifts and the learned measure collapses (R0b-2, reproduced on sparse). A design-around that does not train is not a design-around. Spec states the measurement. |
| 3.4 | Supply credit **externally** (supervised) instead of deriving it | Claim 21's independent does not require derived credit (claim 22 is the dependent). Caught. |
| 3.5 | Store **two or more trace values per synapse** (e.g., e-prop's decomposed traces) to dodge "exactly one scalar" | Real risk: "exactly one" is easy to design around at modest memory cost. Drafting instruction: consider "at most two" or "a number of trace values independent of network size" as the independent's form, keeping "exactly one" as the dependent. Flagged for counsel rather than resolved here. |

### B.4 Against claim 31 (neuromorphic device)

| # | Design-around attempt | Verdict |
|---|---|---|
| 4.1 | **Software/GPU implementation** | Not this claim's job; caught by claims 1/16/21. |
| 4.2 | Different sparse format (COO, hash-based) | Caught — "compressed edge-indexed representation" is drafted format-agnostic; CSR is an embodiment in the spec. |
| 4.3 | Analog/memristive synapse circuits | Caught — claim 31 is circuit-style-agnostic by design (organization level). |
| 4.4 | Single shared filter bank with **time-multiplexed constants** emulating the dual filter | Grey zone: arguably still "a second synaptic filter circuit" functionally. Drafting instruction: define "filter circuit" in the spec to include time-multiplexed realizations of distinct filter states. |
| 4.5 | Off-chip learning, on-chip inference only | Escapes the plasticity-engine element of 31 as drafted. Counsel should add a sibling device claim without the plasticity engine (regions + dual filter + edge memory + interfaces only) so inference-only silicon is still caught — that sibling is supportable and is missing from this draft by oversight of scope, not evidence. **Adopt.** |

---

## C. The enablement / breadth line

For each independent claim: the broadest supportable version, the fallback under examiner pressure,
and which measured result carries which limitation. "Supported" means a written description crucible
can produce today from banked results; "prophetic" means constructive disclosure only.

### C.1 Claim 1 (system)

- **Broadest supportable:** as drafted — *on condition that the differential-τ return is actually
  built and run before filing* (§D.1). Today the non-foldability limitation rests on: the exact fold
  theorem (verified 3.2×10⁻¹⁵; five CPU assertions on the real substrate), the demonstrated current
  separation at differing constants (τ 2 vs 20, unit test), and a fully specified construction (a
  second filter state `g_ret` with `a_ret ≠ a` plus a second sparse matrix-vector product). That is
  a strong constructive disclosure but **no end-to-end system with the non-foldable loop has ever
  run**. US prophetic-example practice tolerates this; EPO Art. 83 is the risk point.
- **Fallback 1:** claim 1 with claims 8+9 merged in (homeostasis + per-region branching band) — every
  element then has a banked measurement behind it except the return filter itself.
- **Fallback 2 (the fully-measured redoubt):** a system claim on the *substrate without the return
  construction*: regional spiking network, per-region τ, homeostasis, per-region branching-band
  configuration, fixed readout, plastic recurrence, edge-indexed storage, embodied I/O — everything
  measured in CRU-40 step 7 + CRU-57 s1e. Weaker novelty (no crown jewel) but bulletproof support.
- **Measured supports:** region taxonomy + per-region τ (`RegionalLifPool`, 22k-neuron runs);
  per-region σ dispersion and the whole-pool-σ pinning finding (CRU-40 step 7c); homeostatic
  regulation to target rate, gain-insensitive (R0a, sparse port test); short-return cost law
  (CRU-70); span=support argmin (CRU-75); 7.9× folded-equivalent synapse cost (CRU-70 §3).

### C.2 Claim 16 (redeployment)

- **Broadest supportable:** as drafted, *at the rate-network/analogue level*: the mechanism is banked
  (pre-registered GO, 8 seeds, fair hyperparameter sweep, foreign-body specificity control). The
  forward model there is an MLP and the learners are idealized (Levenberg–Marquardt, kernel ridge).
- **Not yet supported:** the same method *on the spiking substrate* (claim 19's combination) —
  redeployment has never run through `ClosureBrain`. Claim 19 is prophetic today.
- **Fallback:** limit to "a forward model comprising a fixed nonlinear map trained on the agent's own
  sensorimotor experience" + linear alignment transform (claim 18 merged in) + the parameter-ratio
  bound — every element then traces to the GO run.
- **Measured supports:** closed ≈ 0.000 vs ablated 0.178–0.883 growing with gain 1.0→3.0; foreign
  3.7–4.0 (no transfer); the ablated sample-hunger curve over K = 8…1024; 36-parameter frame vs
  ≈ 840-parameter model (the "one tenth" bound, with ~25× headroom).
- **Caveat carried into the spec:** the closed arm's flat 0.000 is by construction (data generated by
  the exact ĝ); the discriminative work is the ablated richness-slope and the foreign control. The
  spec must present it that way — an examiner's declaration fight is lost if the flat line is
  oversold.

### C.3 Claim 21 (training)

- **Broadest supportable:** as drafted. This is the best-enabled independent in the set. Every
  element is measured on the real substrate at scale: edge-indexed trace + O(E) memory (25k neurons,
  0.06 GB, learns to 0.966 while frozen sits at 0.470; dense equivalent needs ~2.5 GB per step);
  hinge-gated three-factor updates (locked recipe, transferred with no retuning); homeostasis
  required for stability; fixed-readout attributability control (G-I2 near chance).
- **Claim 22 (derived credit):** demonstrated in the rate-based tier-A analogue; on the spiking
  substrate the current implementation still lands harness-computed credit. Partial support —
  file with the tier-A demonstration + constructive spiking disclosure, or close the gap first
  (§D.2).
- **Claim 23 (routed credit):** fully measured (Gate A: 92.4% of ceiling, floor −0.003, p = 0.0001,
  8 seeds, pre-registered before the script existed — the pre-registration discipline is itself
  useful evidence of possession).
- **Fallback:** merge claims 23 + 26 into 21 (routed credit + θ-pinning) — narrower, wholly
  Gate-A-supported.
- **Numerical dependents (2, 15, 29):** working points are measured (τ_syn 2, τ_mem 8/10–20,
  τ_elig 40, target rate 0.1, margin 0.5); *ranges* are not swept. See §D.5.

### C.4 Claim 31 (hardware)

- **Broadest supportable:** the memory-organization and filter-bank architecture, disclosed at
  data-structure level with the measured software profile as the enabling evidence (the O(E) numbers
  are hardware-motivating facts, not silicon measurements). All hardware examples prophetic.
- **Fallback:** drop the plasticity engine (inference-only sibling, §B.4.5) and the branching
  estimator (claim 34), keeping regions + dual filter + edge memory — the organization alone.
- **Filing posture:** include the hardware section in the priority spec even though prophetic
  (`01` §2.3 and §5.1 already recommend this); claims can be pursued or abandoned at national phase
  when the neuromorphic-industry logic is clearer.

---

## D. What is missing before filing — the concrete work list

Ordered by leverage per week. Items 1–2 are the ones that convert the crown-jewel claims from
prophetic to demonstrated; the rest harden dependents.

1. **Build and run the non-foldable return loop.** Implement the differential-τ second filter state
   (`g_ret`, `a_ret ≠ a`, second spMV) on `RegionalLifPool`, wire it as the ESM→(EWM,ISM) return,
   and flip the named acceptance test: `test_a_shared_filter_leaves_the_matrix_decomposition_exact`
   must be updated to assert the decomposition **fails** — the crucible record itself defines this
   as the acceptance signal that the loop became a distinct dynamical kind. Then run *any* banked
   task (the cued-recall discrimination suffices) end-to-end through the non-foldable loop. This
   single run is the difference between claim 1 as a constructive disclosure and claim 1 as a
   demonstrated machine. Estimated cost per the record: a code change, not a research program.
2. **Close the derived-credit gap on the spiking substrate** (supports claim 22): implement
   reafference-prediction-error credit end-to-end where `apply_reward` currently takes a
   harness-computed vector. The M1s3 record already binds this as a build requirement ("no
   harness-computed error may enter training"), so the patent need and the science need coincide.
3. **Run redeployment on the spiking substrate** (supports claim 19 and strengthens 16): the s1
   frame-refit protocol through a `ClosureBrain`-hosted forward model, even at reduced scale. Note
   the M1s3 record's warning that s1's numbers were measured in the *inverse* direction and the
   committed direction is now *forward* — the patent example should be run forward so spec numbers
   match the claimed method.
4. **The consolidation measurement (feature F5) — decide, don't drift.** `02` ranks
   closure-as-consolidation (train-with-loop / test-loop-removed transfer) as the strongest white
   space, but no such transfer result is banked on the real substrate, which is why this document
   claims nothing on it. Either run the measurement before filing (it needs the non-foldable loop
   from item 1 anyway — a folded loop cannot support a loop-removal claim, by our own algebra) or
   accept disclosed-but-unclaimed status with continuation rights. The fold discovery makes the old
   tier-A "loop-removal" framing unusable; the measurement must be designed on the new loop.
5. **Sensitivity sweeps for every numerical dependent** (claims 2, 6, 15, 29, and the branching band
   of 9/30): each claimed range currently has one measured working point, not a swept boundary. An
   examiner will ask why "factor of two," "one tenth," "25%," "5–100 steps," "band around unity" —
   each needs either a cheap sweep (most are CPU-scale in this codebase) or demotion to
   spec-example-only. Also: decide the σ band (the record's in-band judgments imply roughly ±5–10%
   but no band is anywhere committed).
6. **A single written-description document for the return construction.** The fold theorem, the
   three breakers, the unfiltered-injection trap (`input_current` bypasses the filter entirely — the
   "next move someone would make," already pinned in the record), and the differential-τ
   construction are currently spread over results/design/test files. Counsel needs them as one
   coherent enabling narrative with the five assertions cited. Cheap; one session.
7. **Verify the never-published status of every claimed element** against the public mirror, the
   papers, the wiki, and the talks — `01` §1.4's per-item [verify] applied to this claim set
   specifically. In particular confirm that the §8.9 public prose stops short of: the differential-τ
   construction (it does — the fold material postdates and never shipped), the Gate-A recipe, the
   redeployment protocol parameters, and the per-region σ instrument detail.
8. **Freeze the inventorship record for each independent claim** per `01` §5.4: for claims 1, 16,
   21, 31, one paragraph each documenting MG's conception/direction of the claimed mechanism (the
   unfreeze ruling, the axis corrections, the derived-credit selection, the span-law framing
   rulings are already on the record and citable).

---

## E. Notes to counsel — drafting discipline actually applied here

- **No consciousness vocabulary in any claim** — verified by construction; the vocabulary map in §1
  is the audit trail. The specification may present the published theory as background and cite the
  public papers (they are prior art and citing them costs nothing after the priority date).
- **Structure over function at every point of novelty:** two filter states with distinct constants
  (not "a dynamically real loop"); parameter-count ratio (not "efficient transfer"); per-region
  subsampled estimator (not "operating at criticality"); one trace per stored edge (not "memory
  efficient"). Where a functional consequence appears (the non-foldability wherein, the O(E)
  whereby) it is the *testable consequence of a recited structure*, which is the defensible form.
- **Every numeral traces to a measurement** — the trace is inline in §2's notes and §C; the unswept
  ranges are declared in §D.5 rather than papered over.
- **One deviation from the inventor's brief, stated per instruction:** "as painful as possible to
  circumvent" cannot be absolute — the unrolled-feedforward escape is guaranteed by the inventor's
  own published theorem, and training-time claims are structurally hard to enforce. The achievable
  version, drafted above, is: every cheap circumvention lands on a dependent claim; the four genuine
  escapes (B.1.4, B.1.6, B.2.2, B.3.1) are each either quantified as expensive or mitigated by a
  sibling/continuation; and the system claim, not the training claim, carries enforcement.

*End of claim architecture. Preparatory work product for patent counsel; not legal advice; no filing
decision should rest on this document alone.*
