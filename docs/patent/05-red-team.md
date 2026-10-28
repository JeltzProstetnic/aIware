# Red Team — Opposing Counsel Attack on the Draft Claim Set

**Role:** opposing counsel / well-funded competitor. Mandate: destroy `03-claim-architecture.md`, not
improve it. **Not legal advice; adversarial work product for the inventor's own use before spending
€50–80k.** Prepared 2026-08-11 against docs 01–03 and the crucible record (read-only). Every
citation below was verified this session against a live record (publisher page, PubMed, arXiv,
Google Patents, or USPTO) unless explicitly flagged otherwise; flagged items are asserted as
*probable* art only.

**Headline verdict up front:** the claim set as drafted has two structural defects that no amount of
dependent-claim craftsmanship repairs — (1) **claim 1's "shared synaptic filter state" limitation
fences the inventor's own implementation quirk, not the invention**, handing every competitor a
free, performance-*positive* escape (heterogeneous synaptic time constants, which are both
biological reality and published best practice); and (2) **the design-around table's row B.1.1 is
legally wrong** — claims 3 and 4 are dependents of claim 1 and therefore cannot catch a competitor
who uses a delay or a nonlinearity *instead of* the differential-τ filter, so two of the three
fold-breakers are unfenced. Separately, **every measured number offered in support of the system
family was collected on the folded architecture** — i.e., on a system that does *not* satisfy claim
1's central limitation — which is an enablement/plausibility wound the crucible record itself
documents. Claim 16 should die on prior art the landscape scan missed entirely (alignment-based
transfer of robot models, 2013; adapter-style frozen-model transfer, 2019). Claim 21 is a
combination claim whose every element is individually published, several in a single 2007 paper.

---

## 0. The ranked kill list

| Rank | Claim | Verdict | Single strongest argument |
|---|---|---|---|
| 1 | **16** (redeployment method) | **DIES** | Obvious (arguably anticipated in substance) over Bocsi/Csató/Peters 2013 — fixed source robot model + learned alignment transform + few target samples + control use — combined with the adapter literature (Houlsby 2019: frozen model, small trained module, explicitly parameter-ratio-bounded in practice). Doc 02 never searched transfer-learning/adapter art. Eligibility (Alice/Recentive) and enablement (measured in the *inverse* direction, with idealized regression learners, control step never performed) are independent second and third bullets. |
| 2 | **21** (training method) | **DIES or survives only as a narrow merge** | Izhikevich 2007 alone discloses: exactly one scalar eligibility trace per synapse, locally updated from pre/post spikes, decaying with a trace constant, weight update = trace × global modulatory credit, in a sparse spiking simulation. SORN/RM-SORN add concurrent homeostatic threshold adaptation in a plastic recurrent reservoir. The O(E) whereby-clause is inherent to sparse storage (every event-driven simulator). What is left of the combination is the margin gate — a hinge condition — and "readout fixed," which RM-SORN-style task readouts erode. §103/Art. 56 kills the drafted breadth. |
| 3 | **31** (neuromorphic device) | **WOUNDED, probably dying** | Davies et al. 2018 (Loihi): programmable microcode learning engine, per-synapse spike traces — including **multiple traces of one spike train filtered at different time constants** — reward/modulatory traces, configurable per-compartment time constants, dendritic compartments, sparse hierarchical synapse memory. Nearly every element of claim 31 is a Loihi datasheet capability; the claim reads on a *configuration* of a 2018 chip. Plus: wholly prophetic (no silicon), conceded. |
| 4 | **1** (system) | **SURVIVES VALIDITY WOUNDED — but commercially broken as drafted** | No anticipation found (conceded in §6 below), and the fold-theorem problem-discovery story is a genuine non-obviousness asset. But: (a) the "shared synaptic filter state" element gives a zero-cost design-around (§2.1); (b) delay-only / nonlinearity-only returns escape the whole family (§2.2); (c) Art. 83/G 2/21: the claimed system has never run and the point of novelty has no measured effect attached to it (§3.1). A patent that is valid, avoidable at negative cost, and unsupported at its point of novelty is not a toll booth. |
| 5 | 5, 6, 7 (span/bottleneck/short-return dependents) | WOUNDED | All three are supported exclusively by measurements taken on folded (open-network) arms — CRU-69 establishes this in the inventor's own hand. No measurement of span law, rank ratio, or relay cost exists on any system satisfying claim 1. Ranges unswept (conceded §D.5). |
| 6 | 9, 30, 34 (criticality) | SURVIVE as dependents, eroded | Cramer 2020 is distinguished, but the *estimator* story is weaker than doc 03 believes: subsampled branching estimation is published (Wilting & Priesemann 2018, subsampling-invariant estimator), and homeostatic-plasticity-shaped distance-to-criticality under input is published (Zierenberg et al. 2018). What remains is "apply the published estimator per region and require all regions in band" — a thin inventive step, acceptable only because these are dependents. |
| 7 | 23 (routed credit through masked alignment region) | **SURVIVES — best claim in the set** | Measured (Gate A, pre-registered, p = 0.0001), no close art found after genuine search, structural not functional. See §6. |
| 8 | 17 (absorption guard) | SURVIVES, narrow | No art found on frozen-readout fidelity-retention verification as a method step. Low standalone value; real value merged into 16's replacement. |
| 9 | 2, 15, 29 (numerical ranges) | WOUNDED | One working point each, no sweeps; classic Art. 84/§112 fodder (conceded §D.5, but the concession does not repair them). |
| 10 | 24, 25, 26 (Dale guard, antagonist pairs, θ-pinning) | SURVIVE, cheap | Implementation-guard claims. Claim 24 resembles standard sign-constrained E/I network construction practice (Dale-constrained initialization is routine in the bio-plausible RNN literature); **no specific anticipating reference verified this session — flagged for professional search, not asserted.** |

---

## 1. Front one — invalidity over prior art

### 1.1 New art this attack found that doc 02 missed

All verified this session. This table is the value-add over doc 02; the point is that the landscape
scan searched *consciousness, criticality, world-models and neuromorphics* — and never searched
**transfer learning, three-factor learning rules as a literature, FORCE-feedback structure, or
heterogeneous time constants**, which is where the accused art actually lives.

| # | Reference | Verified via | Kills / wounds |
|---|---|---|---|
| R1 | **Izhikevich, E.M., "Solving the distal reward problem through linkage of STDP and dopamine signaling," *Cerebral Cortex* 17(10):2443–2452 (2007).** DOI 10.1093/cercor/bhl152 | OUP + PubMed 17220510 | Claim 21: one scalar eligibility trace per synapse ("synaptic tag"), local pre/post update, decay constant, weight change = trace × global dopamine signal, sparse spiking network. The core three-factor machinery, in one 19-year-old paper. |
| R2 | **Bocsi, B., Csató, L., Peters, J., "Alignment-based transfer learning for robot models," IJCNN 2013**, pp. 1–7, DOI 10.1109/IJCNN.2013.6706721 | MPI-IS + TU Darmstadt PDF | Claim 16: transfer a trained robot model to a *different robot architecture* by learning an alignment between the two spaces, using little target data, for model-based control. The fixed-model / trained-alignment split is the paper's method. Doc 03 distinguishes only ToMnet and Bongard/Lipson; this line was never considered. |
| R3 | **Houlsby, N. et al., "Parameter-efficient transfer learning for NLP," ICML 2019** | Semantic Scholar + google-research/adapter-bert | Claim 16's parameter-ratio limitation: frozen model + trained adapter of few parameters is the defining move of an entire literature (adapters → LoRA and descendants). "Fewer than one tenth of the parameters" is squarely inside its teaching. |
| R4 | **Nicola, W., Clopath, C., "Supervised learning in spiking neural networks with FORCE training," *Nature Communications* 8:2208 (2017)** | Nature + PubMed 29263361 | Claim 1's structural skeleton: recurrent spiking network, low-dimensional readout of spike activity, readout re-injected as input to the network (feedback encoder). Everything except the separate return filter constant. |
| R5 | **Perez-Nieves, N. et al., "Neural heterogeneity promotes robust learning," *Nature Communications* 12:5791 (2021)** | Nature + PubMed 34608134 | Two-edged and lethal: (a) obviousness — heterogeneous *membrane and synaptic* time constants in SNNs, shown beneficial, teaches per-pathway/per-neuron τ diversity; kills claim 15's inventive step and motivates giving any pathway "its own" constant; (b) design-around — see §2.1: a heterogeneous-τ implementation contains no "shared synaptic filter state" at all. |
| R6 | **Lazar, A., Pipa, G., Triesch, J., "SORN: a self-organizing recurrent neural network," *Front. Comput. Neurosci.* 3:23 (2009)**; and RM-SORN (reward-modulated variant, *Front. Comput. Neurosci.* 2015, surfaced same search) | Frontiers + PubMed 19893759; PMC4371712 | Claim 21: plastic recurrence + **concurrent intrinsic-plasticity threshold homeostasis** (firing threshold adapted toward target rate) + synaptic normalization, in a reservoir whose recurrence learns the structure. RM-SORN adds reward modulation onto the same substrate. |
| R7 | **Davies, M. et al., "Loihi: a neuromorphic manycore processor with on-chip learning," *IEEE Micro* 38(1):82–99 (2018)** | Multiple records incl. NICE-workshop slides | Claim 31: microcode-programmable learning engine; per-synapse traces; multiple traces per spike train at *different configurable time constants*; reward traces; dendritic compartments; configurable time-constant parameter sets; hierarchical sparse synapse memory; sensor/actuator interfacing. The device family claim reads on configuring a 2018 commercial research chip. |
| R8 | **Logiaco, L., Abbott, L.F., Escola, S., "Thalamic control of cortical dynamics in a model of flexible motor sequencing," *Cell Reports* 35(9):109090 (2021)** | Cell Press + PubMed 34077721 | Claim 1 obviousness: a *low-rank thalamocortical loop* — small thalamic population reading cortical activity and re-entering it, with its own dynamics — controlling a recurrent cortical network for motor output. The "low-dimensional bottleneck return with its own dynamics re-entering a recurrent network" motif, published, in a motor-control context. |
| R9 | **Wilting, J., Priesemann, V., "Inferring collective dynamical states from widely unobserved systems," *Nature Communications* 9:2325 (2018)** | Nature + arXiv 1608.07035 | Claims 9/30/34: the subsampling-invariant branching-parameter estimator. The "fixed-size subsample" element of the criticality claims is the published solution to the published subsampling problem. |
| R10 | **Zierenberg, J., Wilting, J., Priesemann, V., "Homeostatic plasticity and external input shape neural network dynamics," *Phys. Rev. X* 8:031018 (2018)** | APS + arXiv 1807.01479 | Claims 8/9: homeostatic plasticity generating bursting → close-to-critical → irregular states as a function of input; homeostasis-as-regime-control, pre-published. |
| R11 | **Bellec, G. et al., "Long short-term memory and learning-to-learn in networks of spiking neurons," NeurIPS 2018** (ALIF/LSNN) | NeurIPS + arXiv 1803.09574 | Claim 8: adaptive firing thresholds as a standard SNN ingredient; also heterogeneous adaptation time constants per neuron. |
| R12 | **Brunel, N., Wang, X.-J., "Effects of neuromodulation in a cortical network model of object working memory dominated by recurrent inhibition," *J. Comput. Neurosci.* 11:63–85 (2001)** | Springer + PubMed 11524578 | Establishes what every computational neuroscientist knows: recurrent networks routinely carry *multiple synaptic filter time constants concurrently* (AMPA-fast, NMDA-slow, GABA). "Different pathways, different synaptic filter constants" is a quarter-century-old modeling default, not an invention. |
| R13 | Brain Corp **US 9,129,221 B2** (from US 2013/0297541 A1), "Spiking neural network feedback apparatus and methods" — granted 2015, **status: expired fee-related** (adjusted expiry would have been 2033) | Google Patents fetch | Minor: claimed feedback/context connections with plasticity in SNNs. Prior art only (lapsed), citable against feedback-structure novelty. |

### 1.2 Claim 1 — the honest attack, and its limit

**No anticipation found.** After genuine search I could not produce a single reference disclosing,
in combination: spiking recurrent network + regional taxonomy + low-rank readout of one region +
re-injection through a *separate* filter state with a *different* time constant. That specific
unity appears novel. Recorded as a failure in §6.

**The obviousness case is nonetheless strong, and it writes itself from R4 + R5/R12:**

- R4 (Nicola & Clopath) supplies the entire structural skeleton: spiking recurrent network,
  low-dimensional readout, readout fed back as input. Their feedback shares the network's synaptic
  filter — it is precisely the "foldable" configuration (their own effective-weight formulation
  *is* the fold, ω₀ + ηφᵀ).
- R12 (Brunel & Wang, and the whole biophysical modeling tradition) supplies the modification:
  pathways in recurrent networks carry different synaptic filter constants as a matter of course —
  fast AMPA recurrence, slow NMDA feedback is the textbook working-memory architecture, chosen
  *because* the slow pathway contributes qualitatively different dynamics.
- R5 (Perez-Nieves) supplies contemporary motivation: heterogeneous synaptic/membrane time
  constants measurably improve SNN task performance.
- R8 (Logiaco) supplies the bottleneck-loop-with-own-dynamics motif in a control context.

A skilled person building R4's feedback network and asking "should the feedback synapses have the
same kinetics as the recurrent ones?" has a quarter century of literature answering "they need
not, and slow feedback is often better." The combination requires no inventive leap; it requires
reading two adjacent literatures.

**The inventor's best counter — state it so it can be prepared:** the *reason* to give the return
its own filter constant was unknown. Nobody had published that a shared-filter return is
*algebraically an open network* (the fold theorem); the art gives you heterogeneous constants as a
biophysical habit, not as the difference between a real and a fake loop. Problem-discovery is a
recognized non-obviousness route (EPO problem-solution favors it; US KSR less so). This is a real
argument and it is why claim 1 is scored "survives wounded" and not "dies." But note what it
requires: the specification must actually *teach the fold theorem* as the technical problem — and
the moment it does, it also teaches every reader the two other breakers (delay, nonlinearity),
which sharpens the §2.2 escape.

**Preamble erosion:** "at least two regions with different membrane time constants" (also claim 15)
is anticipated as a feature by R5 and R11 and by decades of modeling; it contributes nothing
against obviousness.

### 1.3 Claim 16 — dies three ways

1. **Prior art (§103 / Art. 56, arguably §102 in substance).** R2 (Bocsi 2013) teaches: a robot's
   learned model, held as the source; an alignment transform learned between the source space and a
   *different robot's* space from a small amount of target data; predictions generated by passing
   through the alignment into the fixed source model; used for control. Map to claim 16: "trained
   forward model … trained on sensorimotor experience" ✓ (source robot model); "holding all
   parameters … fixed" ✓ (the source model is reused, not retrained); "training an alignment
   transform that maps between an observation space of the external … entity and an input-output
   space of the forward model" ✓ (that is the method's name); "generating predictions … by applying
   the fixed forward model through the trained alignment transform" ✓; "deriving control outputs" ✓
   (model-based control is the use case). The only limitation left is the parameter-ratio bound —
   supplied by R3 (Houlsby adapters: frozen model, small trained module, the entire point being the
   parameter ratio). The "external dynamical entity" wording does not distinguish: robot B *is* an
   external dynamical entity relative to robot A's model, and the claim nowhere requires the entity
   to be another agent's mind. The doc's §3.7 distinguishes Bongard/Lipson ("same body after
   damage") — Bocsi is the reference that breaks that distinction, and doc 02 never found it.
2. **Eligibility (§4.2).**
3. **Enablement (§3.3).**

Any one of the three suffices; together they make claim 16 the claim I would least want to defend.

### 1.4 Claim 21 — a combination of published elements

Element-by-element against verified art:

| Claim 21 element | Published in |
|---|---|
| Sparse edge-indexed storage of synapses | Every event-driven SNN simulator and neuromorphic memory design (also R7); inherent, not inventive |
| Exactly one scalar eligibility trace per synapse, local pre/post update, decay constant | R1 (Izhikevich 2007), verbatim mechanism |
| Modulatory credit signal, update ∝ trace × credit | R1; the entire R-STDP / three-factor literature after it |
| Concurrent homeostatic threshold adaptation toward a target rate | R6 (SORN's intrinsic plasticity; RM-SORN combines it with reward modulation); R10, R11 |
| Fixed readout / plasticity confined to recurrence | Partially R1 (no trained readout exists at all — behavior read directly from the network); reservoir-inversion *rhetoric* is new, the practice of not training a readout is not |
| Margin gate | Hinge/deadband conditions on updates are ubiquitous in learning theory; no specific SNN citation verified this session (flagged), but as the *sole* surviving delta it cannot carry inventive step for the combination |
| O(E) whereby-clause | Inherent consequence of sparse storage; a whereby-clause reciting an inherent property adds no patentable weight |

The drafters' novelty argument (§3.5 of doc 03) is built against e-prop only. Against
R1 + R6/RM-SORN the "four combined limitations e-prop lacks" collapse to one and a half: the
margin gate, and "fixed readout" as an explicit negative limitation. Under KSR/Comvik that is not a
patentable combination; each element performs its published function with no synergistic surprise
— and the one measured synergy claim ("homeostasis required for stability") is itself the SORN
finding (plasticity destabilizes the reservoir; IP homeostasis is what keeps it in regime — that is
the 2009 paper's stated architecture).

**Survivable core:** merge claims 23 + 26 into the independent (routed credit through a masked
alignment region + θ-pinning during evaluation) — measured, pre-registered, and I found no art on
either. That narrow claim survives this front. The drafted claim 21 does not.

### 1.5 Claim 31 — reads on configuring Loihi

R7 discloses, as shipped silicon capabilities: neuron circuits organized with configurable
time-constant parameter sets; sparse synapse memory; per-synapse trace fields — including
*multiple* traces of the same spike train at *different* configurable time constants (which also
moots the "second synaptic filter circuit" as a hardware element: Loihi's filter bank already
instantiates plural constants); an on-device programmable plasticity engine consuming traces and
reward/modulatory factors; threshold adaptation implementable in the microcode rule engine; sensor
interfaces (event-based I/O). Claim 31's remaining delta is the *specific wiring* (regions + a
designated readout-return with its own filter circuit) — i.e., a network topology loaded onto a
configurable device. A device claim whose novelty is the loaded configuration invites both an
obviousness rejection over R7 + claim-1-architecture and, in litigation, a fight about whether
selling a configurable chip infringes at all (it does not, until configured — enforcement lands on
the customer, which is the worst enforcement posture there is). Combined with the concession that
all hardware examples are prophetic, family 31 is decorative.

---

## 2. Front two — non-infringement design-arounds

Ranked by cost to the competitor. The first two are effectively free, which is the finding that
matters: **the fence's expensive-escape story (unrolling, 7.9× synapses) is real but irrelevant,
because nobody needs the expensive gate while two free gates stand open.**

### 2.1 FREE, PERFORMANCE-POSITIVE — heterogeneous synaptic time constants (kills the system family's commercial value as drafted)

Claim 1 requires: "synaptic transmission over the recurrent synaptic connections is low-pass
filtered by **a shared synaptic filter state having a first filter time constant**," and defines the
crown-jewel non-foldability against *that shared state*. This claims the inventor's implementation
accident (CRU-69 §2: "`_syn_a` is a scalar … τ_syn is global … the single filter site on purpose"),
not the invention.

The design-around: give synapses **individually drawn or per-pathway synaptic time constants**
(τ ~ distribution, or AMPA/NMDA-style dual kinetics everywhere). Consequences, each fatal to a
different part of the story:

- **No infringement:** there is no "shared synaptic filter state," so the element is absent; the
  wherein-clause ("separate from the shared synaptic filter state") has no referent. Every claim
  in the family (2–15) falls with it, dependents included.
- **No performance cost — a performance gain:** R5 measures heterogeneous time constants
  *improving* SNN learning and robustness. The escape is better engineering than the claimed
  system.
- **The invention comes along for free:** the fold theorem only bites when the filter is uniform
  (CRU-69 §3's algebra requires g(t) to be the same vector in both terms). With heterogeneous τ,
  any return pathway automatically has "its own" time constants — the competitor gets a
  non-foldable, dynamically real loop without ever building the claimed second-filter-state
  construction.
- **It is also where the field already is:** biology (R12) and modern SNN practice (R5, R11) both
  use heterogeneous kinetics by default. The claim as drafted may catch *nobody who was ever going
  to exist*.

This is the single most damaging finding in this document. The dilemma it creates is genuine and
should be put to counsel exactly as a dilemma: **redraft broad enough to catch heterogeneous-τ
implementations and the claim collides with R4+R5/R12 obviousness (a heterogeneous-kinetics
feedback network is 2001-vintage art); keep it narrow (shared filter + separate return state) and
it is avoided at negative cost.** I do not see a drafting trick that escapes both horns; the
honest options are in §7.

### 2.2 FREE — delay-only or nonlinearity-only return (the dependent-claim fallacy)

Doc 03 §B.1.1 rates "replace the differential-τ return filter with a delay element or an interposed
nonlinearity" as **"Caught — claims 3, 4."** That verdict is legally wrong. Claims 3 and 4 are
dependents of claim 1; a dependent claim contains *all* limitations of its parent. A competitor
whose return path has the shared filter plus a **delay** (or an interposed nonlinearity) but **no
second filter state with a different constant** does not infringe claim 1 — and therefore cannot
infringe claims 3 or 4, which only *narrow* claim 1. The three fold-breakers are alternatives; only
one of them is in the independent. Two of the three doors are open, at zero cost — CRU-69 §4's own
table certifies that either alternative "makes a return a distinct dynamical kind," i.e., the
escape loses nothing.

Doc 03's own drafting note anticipates the fix ("1's wherein-clause can be drafted Markush-style
over all three breakers") and then declines it for aesthetic reasons ("keeps claim 1's point of
novelty singular"). The red-team verdict: **the Markush form is not a stylistic option, it is the
difference between a fence and a gate.** As drafted, B.1.1's "Caught" should read "FREE ESCAPE ×2."

### 2.3 NEAR-FREE — the relay-population return

Replace the linear readout + return filter with a **small spiking relay population** (thalamus
motif, R8): second region → sparse projection → relay region of k neurons (its own membrane τ,
which claim 1's own preamble already normalizes as per-region variation) → projection back into the
first region, all synapses on the shared filter. The relay's spiking nonlinearity and membrane
integration make the loop non-foldable (delay + nonlinearity + own τ, all three breakers at once),
while arguably: no "readout … arranged to derive a signal" (a synaptic projection into a region is
not naturally a "readout"), no "derived signal … re-injected," and no "return filter state separate
from the shared synaptic filter state." Claim construction fight at best; the accused structure is
also the one the brain uses, giving the competitor an excellent non-infringement narrative.
Crucible's own CRU-67 relay-dynamics work demonstrates the design space is live and functional.
Cost: k relay neurons instead of a rank-k matrix — negligible.

### 2.4 FREE — claim 16's ratio bound

Train an adapter/alignment module at 12–15% of the forward model's parameter count. The model stays
frozen (so the retained-fidelity property is untouched — doc 03 §B.2.3's assertion that exceeding
the bound "loses the retained-fidelity property" is false: absorption requires *changing the
model's parameters*, and the escape changes none of them); the transfer economics are essentially
unchanged (adapter literature spans 0.5–20% ratios freely); the claim's "fewer … than one tenth"
limitation is not met. Numerical-bound limitations at a point the physics does not enforce are
always free escapes. Alternatively: pad the alignment module with inert parameters — even sillier,
equally effective.

### 2.5 FREE-to-CHEAP — claim 21's conjunction

A conjunctive method claim offers one exit per conjunct. In order of comfort: (a) omit the margin
gate (apply small updates always) — **no banked measurement shows the margin gate is necessary**,
so presumptively free; (b) lightly fine-tune the readout at any point (violates "holding them fixed
throughout training") — cheap, possibly beneficial; (c) two trace values per synapse (doc 03
concedes, B.3.5 — and it is Loihi's native mode, R7); (d) train off-line with surrogate gradients,
ship frozen (doc 03 concedes, B.3.1). Four exits, none costing measured performance.

### 2.6 The escapes doc 03 already prices correctly

For completeness: the unroll (B.1.4, 7.9×/5.3–6.0× measured cost — real but see §3.1's caveat that
these costs were measured on folded arms), full relearning per entity (B.2.1), dedicated
other-model (B.2.2), e-prop route (B.3.2), off-chip learning (B.4.5). These verdicts are honest in
the draft. The problem is not that the expensive escapes were mispriced — it is that §2.1–2.5's
free escapes make the expensive ones academic.

---

## 3. Front three — enablement and written description

### 3.1 The system family's evidence base supports a different system than the one claimed

This is documented in the inventor's own record and it is worse than doc 03's §C.1 concession.

- **The claimed system has never run.** Conceded: "no end-to-end system with the non-foldable loop
  has ever run." The differential-τ construction exists as a unit test showing two currents differ
  (τ 2 vs 20) plus a specification of a code change. Under EPO Art. 83 that is a constructive
  disclosure of a machine whose *defining dynamical property* — the whole point of the wherein
  clause is that the dynamics become a "distinct kind" — has never been observed. Under *Amgen*,
  the full scope of "such that the input … is not expressible as an additive rank update" is
  supported by algebra, but the *utility* of the claimed configuration is supported by nothing.
- **Every supporting measurement was taken on the folded architecture.** CRU-69 (2026-08-10)
  establishes: "the tier-B loop arm was already in folded form … at runtime there is one matrix …
  no tier-A run ever contained a structurally closed arm." Therefore the span-law argmin (claim 5,
  CRU-75), the rank/support boundary (claim 6), the short-return monotone cost (claim 7, CRU-70),
  and — critically — **the 7.9× synapse-economy figure that doc 03 offers as claim 1's EPO
  eligibility/technical-effect hook** were all measured on systems that do **not** satisfy claim
  1's central limitation. The dependents' numbers describe the behavior of a folded (open,
  prior-art-shaped) architecture; whether any of them survive on the non-foldable loop is an open
  empirical question the record itself flags (CRU-69 §6 withdraws the premise that the sweep bears
  on "whether tier B has a real loop").
- **G 2/21 / plausibility attack (EPO), and its US cousin:** the technical effect asserted at the
  point of novelty must be at least plausibly attributable to the distinguishing feature. Here the
  distinguishing feature (second filter state, different constant) has *no measured effect at all*
  — the measured effects belong to the bottleneck/span features, which exist in the folded form
  and are therefore not distinguishing. An opponent will put CRU-69's own sentences into the
  proceedings (post-publication, they will be public in some form, and discovery/inspection reaches
  them in litigation regardless).
- **A subtler wound from the same record:** CRU-67 §10 documents that even the *delayed* relay loop
  was exactly reproduced ("ties exactly, at every τ_r, term for term") by a loop-free rival granted
  one synaptic time constant — "what survives is a cost gap, not an indistinguishability gap." The
  spec must therefore not claim or imply that the non-foldable return produces input-output
  behavior an open architecture cannot; the inventor's record proves the opposite, and an opponent
  who reproduces the three-line algebra will use it to reduce the invention's asserted technical
  character to a memory-cost accounting claim — which is defensible, but much smaller than
  "distinct dynamical kind."

**Repair exists and is cheap** (doc 03 §D.1: build it, run it, re-measure). The red-team point:
until D.1 *and a re-run of the claim-5/6/7 measurements on the unfolded loop* are done, the filing
would go in with its evidence pointing at the wrong machine. D.1 alone (run one task through the
loop) does not fix the dependents.

### 3.2 Claim 21 family — solid, one gap

Best-enabled family (conceded and true). Claim 22 (derived credit) is rate-analogue-only —
conceded; prophetic on the spiking substrate. Claim 29's range 5–100 from a single τ_elig = 40
point — Art. 84/§112 target.

### 3.3 Claim 16 — the measurement does not practice the claim

Four separate gaps, all from the GO record (CRU-57):

1. **Direction:** the banked numbers were measured in the *inverse* direction; the committed
   protocol is *forward* (doc 03 §D.3 concedes). The claim's "predicts sensory consequences of the
   agent's motor commands" is the forward direction — the direction with no banked numbers.
2. **Learners:** the "training an alignment transform" step was performed by Levenberg–Marquardt
   restarts and kernel ridge — idealized offline regression, not any mechanism within the claimed
   control system. The claim is on a computer-implemented method, so this is survivable — but the
   spec's headline numbers describe an idealization.
3. **The flat 0.000 is by construction** (data generated by the exact ĝ; conceded in the GO doc
   itself). The discriminative content is the ablated slope and the foreign control — i.e., the
   evidence shows *relearning is expensive*, not that *the claimed method performs well* on any
   real body or entity.
4. **"Deriving, from the predictions, control outputs" has never been performed.** No control loop
   was ever closed through the redeployed model. The final method step is wholly prophetic.
5. ***Amgen* full scope:** "an external dynamical entity" spans other robots, humans, animals,
   markets, weather — enabled for: a synthetic MLP body whose data the model generated. The genus
   is functional at the point of transfer; the disclosure is one point.

### 3.4 Claim 31 — prophetic silicon

Conceded. Organization-level disclosure is a fair filing posture, but combined with §1.5 the family
is prophetic *and* obvious — the worst quadrant.

---

## 4. Front four — subject-matter eligibility

Concentrated where it can win; concessions where it cannot.

- **Claim 1 (system) and claim 31 (device): the attack largely fails — conceded.** A control system
  with sensor and actuator interfaces on an embodied agent is comfortably outside the G 1/19
  simulation trap (direct link with physical reality) and, in the US, an *Enfish/McRO*-style
  specific architecture. The one soft spot: the technical-effect narrative (7.9× economy) is
  borrowed from the folded system (§3.1), so at the EPO the *inventive-step-relevant* technical
  character rests on shakier evidence than the eligibility checkbox — an Art. 56 problem wearing an
  Art. 52 costume, and the opponent will argue it there.
- **Claim 16: strongest eligibility target in the set.** As drafted it is a sequence of
  mathematical operations (provide model, freeze, fit map, predict, derive outputs). Under
  *Recentive Analytics v. Fox* (Fed. Cir. 2025, adopted by doc 01 itself), applying known ML
  techniques (frozen model + small trained transform — R2/R3 show exactly how known) to a new
  environment ("external dynamical entities") without an improvement to the method itself is
  abstract; "deriving control outputs" is insignificant post-solution activity unless the claim
  positively recites actuation, which it does not — it recites *deriving outputs*, not applying
  them. At the EPO, "external dynamical entity" is unbounded — the entity may be non-technical
  (another mind, a market) — and the claimed result is numerical prediction data; under G 1/19 the
  "potential" technical use of predictions does not count. The embodied-agent preamble is the only
  anchor and it is generic wrapping on the method's face.
- **Claim 21: attack probably fails at the EPO, uncomfortable in the US.** Route (ii) (adaptation
  to internal functioning — O(E) memory, locality) is the right frame and *Recentive* explicitly
  safe-harbors improvements to the training method itself. The wrinkle: the recited memory
  improvement is inherent to sparse storage generally (§1.4), so the "specific improvement" the
  eligibility argument needs is the same element the obviousness attack removes. Eligibility and
  validity cannot both be saved by the whereby-clause.

---

## 5. The one attack I would actually run

**As a competitor: none.** I would ship the §2.1 heterogeneous-τ implementation (with a relay
return, §2.3, if I wanted belt and braces), cite R5 in my design docs as the engineering rationale,
and never need a license or a tribunal. The claim set as drafted does not force me to the table —
that is the commercial finding, and it is independent of every validity argument above.

**If forced to a tribunal — EPO opposition against claim 1** (the crown jewel; killing it guts the
family's deterrence): primary ground **Art. 83 + Art. 56 via G 2/21** — the claimed system never
ran; every asserted technical effect was measured on an architecture not satisfying the
distinguishing feature; the distinguishing feature itself (second filter state) is an obvious
transposition of quarter-century-standard multi-kinetics practice (R12, R5) onto a published
feedback structure (R4), with the fold theorem as the only novel content — and the fold theorem is
a *discovery about the applicant's own implementation*, not a technical teaching that survives into
the heterogeneous-τ systems the field actually builds. Secondary ground: added-matter/clarity
pressure on "shared synaptic filter state" and the unswept numerical dependents. I would choose the
EPO over an IPR because the enablement/plausibility grounds are stronger there than §112 is in IPR
(where enablement is unavailable and I would be limited to §§102/103 — still adequate against
claims 16/21 via R1–R3/R6, but weaker against claim 1).

Cheapest kill overall if the goal is precedent: **IPR against claim 16** on R2 + R3 (§103). Clean
two-reference combination, no swearing-behind available (both >10 years old), and its loss
contaminates the family's licensing story.

---

## 6. Where the attack failed — findings in the claims' favor

Reported per the brief; a survived attack is a finding.

1. **No anticipation of claim 1's combination was found.** Genuinely searched (FORCE-feedback,
   reservoir-with-feedback, thalamocortical models, heterogeneous-kinetics SNNs, dendritic/
   compartment art, neuromorphic estates). The specific unity — regional spiking substrate +
   low-rank readout of a designated region + re-injection through a structurally separate filter
   state with a different constant, framed on the non-foldability consequence — did not surface.
   Claim 1's problem-discovery story (the fold theorem) is a real non-obviousness asset if the spec
   teaches it properly.
2. **Claim 23 (credit routed through a masked alignment region) survived every front.** No close
   art found; fully measured (Gate A, pre-registered, 8 seeds, p = 0.0001); structural language.
   It is the strongest claim in the set and is currently buried as a dependent.
3. **Claim 17 (frozen-readout fidelity-retention verification) survived the art search.** Narrow
   but clean.
4. **System/device eligibility (claims 1, 31) resisted the Alice/G 1/19 attack** — as doc 03
   predicted. Concentrating eligibility fire on claim 16 is correct.
5. **The expensive escapes are genuinely expensive** *if* the claim-5/6/7 numbers replicate on the
   unfolded loop: the unroll cost (7.9× synapses; 71.5–74% connectome) is a real deterrence
   quantum. The caveat of §3.1 (measured on folded arms) is the only thing between this and a
   clean finding for the drafters.
6. **The vocabulary discipline held.** No claim uses consciousness/self-model language; I found no
   Kadin-shaped functional hook to hang an anticipation or an indefiniteness attack on. The §1
   vocabulary map does its job.

---

## 7. What the drafter should change (constructive part — deliberately last)

1. **Resolve the §2.1 dilemma before anything else, because it decides whether the system family
   is worth filing.** Options, in descending honesty: (a) redraft the point of novelty as
   *pathway-relative* — e.g., "wherein an effective filter time constant of the return path differs
   from every filter time constant applied to the recurrent synaptic connections by at least a
   factor of N" — accepting that this must then be argued over R4+R12/R5 on the fold-theorem
   problem-discovery story alone; (b) keep the narrow form and accept that the family is a
   publication-with-a-ribbon (defensive value, no exclusionary value); (c) shift the family's
   center of gravity to what actually survived — claim 23's routed-credit training core and the
   claim-17 verification step — and let the return construction be spec-taught, continuation-
   chased material. A candid attorney conversation about (a)-vs-(b) is worth more than the rest of
   the drafting budget combined.
2. **Markush the three fold-breakers into independent claim 1.** Non-negotiable (§2.2). "Return
   path comprising at least one of: (i) a return filter state having a second, different filter
   time constant; (ii) a delay element …; (iii) a nonlinear transformation …, such that [the
   non-foldability consequence]." Keep 2–4 as narrowing dependents.
3. **Define "readout" and "return path" in the spec to cover** factored low-rank projections
   computed as chained products, relay populations (add an express dependent on a relay-population
   return), and off-substrate returns (doc 03 B.1.7's instruction — keep it).
4. **Do not file the system family before D.1-plus:** build the differential-τ loop, run a banked
   task through it, *and re-run the span/short-return/synapse-economy measurements on the unfolded
   loop* so that the numbers in the spec describe the claimed machine (§3.1). D.1 as scoped in
   doc 03 (one task run) is necessary but not sufficient.
5. **Claim 16: rebuild or drop.** If rebuilt: recite the forward direction actually committed;
   fold claim 17's verification step into the independent (it is the only element with no art);
   recite actuation, not "deriving outputs" (eligibility); add Bocsi 2013 and the adapter
   literature to the spec's distinguished art and find a limitation neither teaches — candidates:
   the reafference-trained forward model *embedded in the claim-1 substrate* (i.e., make current
   claim 19 the independent and accept it is prophetic until §D.3's spiking redeployment run), or
   the self/other dual-use condition (same model instance concurrently serving own-body control
   and entity prediction — not in R2/R3, and arguably the actual invention).
6. **Claim 21: file the merged form** (21+23+26: routed masked credit + θ-pinning as positive
   steps) as the independent; demote the drafted 21 to a fallback. Replace "exactly one" per doc
   03 B.3.5 ("a number of trace values per connection independent of network size"). Either bank a
   measurement that the margin gate is load-bearing or remove it from the independent — an
   unmeasured conjunct is pure escape surface (§2.5a).
7. **Claim 31: keep only if the sibling inference-only claim is added AND the family is repositioned
   against Loihi** — the spec must claim the *configured organization* (regions + designated
   return + dual filter as wired), expressly distinguish R7's capability-level disclosure, and
   accept that enforcement lands on configuration, not silicon. Budget accordingly (i.e., little).
8. **Add to the professional search brief:** transfer-learning/adapter patent estates (Google,
   Microsoft, IBM own LoRA/adapter-adjacent filings — none checked this session); TU Graz e-prop
   filings (doc 02's item, still open); sign-constrained E/I training art for claim 24; margin/
   deadband-gated plasticity art for the hinge element; and a CPC sweep on G06N 3/049 crossed with
   "eligibility trace" and "third factor," which doc 02's consciousness-centric queries never ran.
9. **Assume the crucible record is discoverable.** CRU-69's and CRU-67's candid self-corrections
   ("the arm never existed in unfolded form"; "ties exactly … term for term") are exemplary science
   and exactly what an opponent will read aloud. File only claims whose story is consistent with
   that record being on the table — which, after items 1–6, it can be.

---

*Verification note: R1–R13 were each confirmed this session against publisher/PubMed/arXiv/patent
records (URLs in the session log). Items expressly flagged as unverified: Dale-constrained E/I
initialization art (claim 24), margin-gate plasticity art, Makondo et al. local-Procrustes robot
transfer (surfaced in search results but not independently fetched — R2 alone carries the claim-16
argument). No unverified reference is load-bearing anywhere above.*
