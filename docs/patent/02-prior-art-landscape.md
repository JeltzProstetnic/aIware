# Prior-Art & Patent-Landscape Scan — FMT Spiking Substrate with Self-Referential Closure at Criticality

**Date:** 2026-08-11 · **Scope:** prospective patent portfolio around the crucible/aIware AC substrate
**Author:** research subagent (Fable), aIware session · **Status:** first-pass landscape, NOT a legal FTO opinion

## The five distinguishing features (search targets)

| # | Feature | Shorthand |
|---|---------|-----------|
| F1 | Self-referential closure: explicit self-model outputs contained in explicit world-model state space (`O_ESM ⊆ S_EWM`), self-region inside a returning recurrent component | **closure** |
| F2 | Criticality / edge-of-chaos (Class-4-like) regime maintained as a runtime control target | **criticality control** |
| F3 | Redeployment: one rich self-model re-pointed at non-self targets, shallow (level-1) recursion | **redeployment** |
| F4 | Sparse spiking implementation, plastic recurrence + fixed readout, ~25k neurons / ~0.06 GB, delayed cued-recall task frozen recurrence cannot learn | **plastic-reservoir SNN** |
| F5 | Closure as consolidation channel: explicit→implicit transfer, measured as train-with-loop / test-loop-removed | **consolidation** |

---

## A. Patents — verified hits, closest first

Verification legend: ✅ = fetched from Google Patents this session (assignee/dates/claim-substance/status read directly); ◐ = number seen in search results but record not individually fetched; status fields are Google Patents' status flags and need professional docketing confirmation before any filing decision.

### A1. Kadin "conscious machines" pair — the closest conceptual art ✅

- **US 11,119,483 B2** — "System and method for conscious machines." Inventor/assignee: **Alan M. Kadin (individual)**. Priority **2018-02-22**, granted 2021-09-14. **Active, expires ~2039-12-08.** US-only (no foreign family found).
- **US 11,906,965 B2** — continuation of the above, granted 2024-02-20. **Active, expires ~2039-05-29.** US-only.
- **Claim 1 in substance (both):** a machine comprising sensor inputs; an ANN configured to identify the self, other agents and objects and to recognize spatio-temporal patterns; an automated processor constructing a simplified **dynamical predictive model of the environment** (a "virtual reality" containing the self); control outputs that alter the environment toward goals. The '965 continuation leans harder on **repeated activation of a model of the self** as the mechanism of consciousness.
- **Reach on our features:** F1 — **conceptually overlapping but not claimed as containment/return-path**: Kadin has a self-representation *inside* a predictive world model, which is the same intuition as `O_ESM ⊆ S_EWM`, but claims neither a return path (self-model outputs re-entering the world-model state space) nor any structural/graph condition (self-region inside a returning SCC). F2 — absent (no criticality, verified by fetch). F3 — partially: the spec identifies self and *other agents* in the VR model, but does not claim re-running one's own self-model on another's inputs, and has no recursion-depth structure. F4 — absent (no spiking; conventional ANN language). F5 — absent (no consolidation mechanism; dreams discussed speculatively only).
- **Assessment:** the single most citable patent reference against a broad F1 claim, and the one an examiner will find first (title match on "conscious machines"). It is **US-only and individually held** — no EP/WO family — so it constrains US claims and US FTO only. A claim drafted on the *structural* closure condition (containment + return path + the graph-theoretic "self-region inside a returning component") plus any of F2/F4/F5 clears it comfortably; a bare functional claim ("machine with a self-model inside its world model") likely does not.

### A2. Thaler / Imagination Engines portfolio (fringe-but-granted consciousness art) ✅

- **US 5,659,666** — "Device for the autonomous generation of useful information" (Creativity Machine). Granted 1997. **Expired** (20 y from 1994 filing). Prior art only.
- **US 7,454,388 B2** — "Device for the autonomous bootstrapping of useful information." Priority 2005-05-07, granted 2008-11-18. **Active but expires ~2027-05-25** — dead as a blocker on any realistic product timeline.
- **US 10,423,875 B2** — "Electro-optical device and method for identifying and inducing topological states formed among interconnecting neural modules" (the DABUS patent). Priority 2014-01-07, granted 2019-09-24. **Active, expires ~2036-08-04.** Individual (Thaler).
- **Claim 1 of '875 in substance:** a monitoring system with an input device capturing pattern-based states, a "thalamobot" processor filtering/identifying state changes among interconnected neural modules, and critic components evaluating merit of detected changes.
- **Reach on our features:** F2 — **adjacent, not equivalent**: the spec (verified) describes noise-driven regimes spanning ordered → "useful confabulation" → chaotic zones and uses fractal-dimension analysis, i.e., it *works the same dynamical neighborhood*, but the claims are about detecting/inducing topological states via perturbation, not about **maintaining a criticality set-point as a control target**. F1 — its "self-monitoring" is literal I/O loopback (network output displayed and re-captured by a camera), not a self-model in a world-model. F3/F4/F5 — absent.
- **Assessment:** worth distinguishing explicitly in any spec we file (the confabulation-zone language is close enough that an examiner may cite it against F2); not a credible blocker for the F1+F2 combination as we state it.

### A3. Commons hierarchical-stacked-networks family (growing, watch it) ✅

- **US 9,053,431 B1** — "Intelligent control with hierarchical stacked neural networks." Inventor/holder: **Michael Lamport Commons (individual)**. Priority 2010-10-26, granted 2015-06-09. **Active to ~2031-10-25.** Continuations: **US 10,510,000 B1**, **US 11,868,883 B1**, **US 2024/0220797 A1**, **US 2025/0238673 A1** ◐ — the family is **still being prosecuted as of 2025**, which is the risk: claims can still be re-aimed.
- **Claim 1 in substance:** a plurality of architecturally distinct ordered neural networks arranged in developmental-stage hierarchy, each feeding signals forward and back to other members, higher networks transforming actions of ≥2 lower ones into "nonarbitrary organizations."
- **Reach:** F1 — no (inter-layer feedback, not self-representation closure; verified by fetch). F4 — spec mentions spiking networks as an available substrate (claim scope risk if a continuation picks that up). F2/F3/F5 — no.
- **Assessment:** not blocking on current claims; the live continuation practice makes it the one **individual-held family to monitor** for late claims drafted toward "self-aware hierarchical networks."

### A4. Irvine Sensors machine-consciousness grant — lapsed ✅

- **US 10,242,314 B2** — "Hyper aware logic apparatus…agent of consciousness and intent for devices and machines." Irvine Sensors Corp. Priority 2015-03-09, granted 2019-03-26. **Expired — fee-related, lapsed 2023-05-01.** Prior art only; no FTO constraint. Claims sensor arrays wired to "neuronal logic units" with variable synapses; no self-model, no spiking dynamics, no criticality (verified).

### A5. BrainChip (Akida lineage) — active hardware art on plastic digital SNNs ✅

- **US 8,250,011 B2** — "Autonomous learning dynamic artificial neural computing device and brain inspired system." Van der Made; BrainChip. Priority 2008-09-21, granted 2012-08-21. **Active to ~2030-12-15.** Continuations **US 10,410,117 B2**, **US 11,238,342 B2** ◐; also pending app **US 2020/0143229 A1** ("Spiking neural network") ◐.
- **Claim 1 in substance:** an information-processing system of **digital synapse circuits** (binary registers holding "neurotransmitter" values) plus a temporal integrator combining synaptic outputs over time; STDP where relative spike timing strengthens/weakens the stored value; learning autonomous via soma feedback.
- **Reach:** F4 — **this is the family to clear for a digital-hardware embodiment**: digital STDP synapse circuits with temporal integration is squarely what an Akida-style implementation of our substrate would use. It does **not** reach a software/GPU simulation (claims are circuit-structural), and does not touch F1/F2/F3/F5.
- **Assessment:** irrelevant to the *claims* we would file (our novelty is architectural, not synapse-circuit-level); relevant to **FTO only if we ship dedicated digital neuromorphic silicon** before ~2030 (parent) / later for continuations — check continuation claim scope before any hardware program.

### A6. Brain Corporation portfolio (Izhikevich-era, Qualcomm-adjacent) — the dense SNN-software thicket ✅/◐

- **US 9,275,326 B2** ✅ — "Rate stabilization through plasticity in spiking neuron network." Brain Corp (Piekniewski, Richert, Fisher, Izhikevich). Priority 2012-11-30, granted 2016-03-01. **Active to ~2033-12-03.** Claim 1: logic that strengthens excitatory→inhibitory connections and inhibitory feedback on excitatory response, weakens both on inhibitory response — i.e., a specific **homeostatic E/I plasticity rule stabilizing firing rate**.
- Siblings seen (numbers from USPTO/search results, records not fetched ◐): **US 9,256,215** (generalized state-dependent learning in spiking networks), **US 9,256,823** (efficient updates in spiking networks), **US 9,129,221** (spiking network feedback apparatus), **US 9,224,090** (sensory input processing in SNN), **US 9,218,563** (spiking saliency detection).
- **Reach:** F2 — **the nearest *claimed* mechanism to "maintain an operating regime by plasticity"**, but the target is firing-rate equalization, not a criticality order parameter (branching ratio, avalanche statistics, Lyapunov/Class-4 measures). F4 — the portfolio broadly covers software-implemented SNN plasticity mechanics circa 2012-2015; individual claims are narrow and rule-specific.
- **Assessment:** an examiner's likely 103 source for "plasticity that regulates network dynamics." Distinguish on the **control target** (a criticality statistic, not a rate) and the **purpose** (maintaining Class-4 computation, not input equalization). Many Brain Corp patents were later assigned/abandoned as the company pivoted to robotics — per-asset status check needed before treating any one as live. Parent expiries cluster ~2032-2035.

### A7. Google / DeepMind — world-model and continual-learning art ✅/◐

- **US 12,533,800 B2** ✅ (from US 2021/0158162 A1) — **the Dreamer patent.** Google LLC; Hafner, Norouzi, Lillicrap. Priority 2019-11-27, granted **2026-01-27**. Active. Claim 1: training a policy network from latent state representations by generating imagined latent trajectories, predicting rewards/values, computing target values, updating policy+value parameters — "latent imagination."
- **US 9,679,258 B2** ◐ — "Methods and apparatus for reinforcement learning" (the DQN patent), DeepMind, granted 2017. Model-free; landscape context only.
- **EWC / catastrophic-forgetting application** — a DeepMind US application claiming *determining parameter importance to task 1, then training on task 2 while protecting those parameters* survived §101 on appeal (USPTO Appeals Review Panel, per National Law Review coverage, verified this session). **I could not pin the publication number** — Google Patents full-text search is not reachable through my tooling and Justia robot-blocked (403). Treat as: **an active, prosecution-confirmed DeepMind claim family exists on importance-weighted consolidation.** Flag for professional search.
- **Reach:** F3 — Dreamer claims *planning inside a learned world model*, not *re-pointing a self-model at another agent*; no self-model at all, no recursion structure. F5 — the EWC family is the serious one: our F5 (explicit→implicit transfer through sustained re-entry) is mechanistically different from importance-penalty regularization, but both live under "consolidating learning from one system/phase into another," so claim language for F5 must be drafted around it (spiking substrate, closure-loop-as-channel, train-with-loop/test-without measurement — none of which EWC has).
- **Assessment:** Google's world-model estate (Dreamer + I2A-era filings) fences the *generic* "learn a world model, plan in it" territory. It does not reach self-model closure. Do not draft any claim whose novelty rests on "agent plans using an internal model" alone — that is now Google's granted ground.

### A8. Expired foundational art — FTO-clear and useful *as* prior art ✅/◐

- **US 7,321,882** ◐ (Fraunhofer/Jaeger, priority ~2001, "supervised teaching of a recurrent artificial neural network" — the **Echo State Network patent**): expired ~2021-22. Fraunhofer's international ESN estate is likewise 20-years-out. **Reservoir computing with a fixed random recurrence and a trained readout is free to practice.** Note the structural inversion vs F4: ESN = frozen recurrence + plastic readout; ours = **plastic recurrence + fixed readout** — the exact opposite training locus, which is both an FTO comfort and a novelty argument.
- **US 6,625,588 B1** ✅-adjacent (record seen, not deep-fetched) — Haikonen/Nokia, "Associative neuron in an artificial neural network," priority 1997-03-26. **Expired.** Haikonen's conscious-machine circuit work (Nokia era) is out of protection; his books remain NPA (see B).
- **IBM TrueNorth core patents** ◐ — the 2011-2014 neurosynaptic-core estate (e.g., US 8,812,415 seen in results) begins expiring ~2031-2034; TrueNorth-specific crossbar claims don't reach any of F1-F3/F5 and reach F4 only for that hardware style. Not individually verified — low priority because non-plastic-at-runtime cores are the *opposite* of F4's plastic recurrence.
- **Numenta** ✅-adjacent — **US 9,189,745 B2** "Temporal memory using sparse distributed representation" (priority ~2011, granted 2015; hardware continuation **US 10,452,972**). Claims sparse sequence memory (spatial pooler + temporal pooler). Sparse representations + sequence prediction overlap F4's *vocabulary* but not its mechanism (no spiking dynamics, no plastic recurrent reservoir, no closure). Parent expires ~2031-2032.

### A9. Named players where **no relevant blocking claims were found** (honest nulls)

- **Intel (Loihi):** portfolio exists (microcode-programmable learning-rule engine, on-chip STDP) but no claim found reaching F1/F2/F3/F5; F4 exposure only for Loihi-style silicon, not simulation. Not exhaustively searched — an Intel-assignee claim search is the top item for a professional follow-up.
- **SynSense, Innatera:** young mixed-signal SNN startups; no claims surfaced relevant to the five features. Unverified beyond absence in searches.
- **Meta (JEPA/LeCun):** JEPA is published as papers and position pieces; **no JEPA patent filings surfaced**. LeCun's 2022 position paper is NPA against generic world-model/self-supervised-prediction claims.
- **Verses AI (Friston, active inference):** heavy publications, "patent-pending" marketing language, **no specific application numbers surfaced through my tooling.** A PATENTSCOPE assignee search on VERSES is the second item for professional follow-up — active-inference agent claims, if granted broadly, would sit near F1/F5's "model updates its own generative model" territory.
- **Hod Lipson / Columbia (self-modeling robots):** the entire self-modeling-robot line (Bongard/Zykov/Lipson 2006 → Kwiatkowski & Lipson 2019 → visual self-models 2022) appears **published, not patented**. That is double-edged: nothing blocks us, and nothing blocks anyone else — and it is the strongest *non-patent* prior art against a broad F3 claim (see B).
- **"Criticality as a claimed feature":** repeated targeted searching (edge of chaos / self-organized criticality / branching ratio / neuronal avalanche + patent) surfaced **zero patents claiming maintenance of a criticality regime in a neural system**. Nearest claimed art is Brain Corp's rate homeostasis (A6) and Thaler's confabulation zones (A2). This is the strongest white-space signal of the scan — with the caveat that my patent-database access was search-engine-mediated (see Coverage).

---

## B. Non-patent prior art an examiner would reach for

Verification level: [v] = confirmed via a fetched/search-returned record this session; [c] = canonical, cited from domain knowledge, bibliographic details not independently re-verified today. None are guesses.

**Against F1 (closure / self-in-world-model):**
- Metzinger, *Being No One* (MIT Press, 2003) — self-model theory of subjectivity; the phenomenal self-model embedded in a world-model. [c] The direct conceptual anticipation; not enabling for any technical implementation.
- Schmidhuber, "Making the world differentiable…" (TR FKI-126-90, 1990) and "On Learning to Think" (arXiv:1511.09249, 2015) — recurrent world-model + controller, and the controller *querying* the model; 2015 explicitly discusses the model containing the agent. [c]
- Kadin's own pre-filing publications (IEEE-adjacent essays on "conscious machines", ~2016-2018) would be cited with his patents. [c]
- Holland (ed.), *Machine Consciousness* (2003); Haikonen, *Robot Brains* (Wiley 2007) — internal-simulation architectures. [c/v]

**Against F2 (criticality as operating point):**
- Bertschinger & Natschläger, "Real-time computation at the edge of chaos in recurrent neural networks," *Neural Computation* 16(7), 2004 (+ the NIPS'04 companion "At the edge of chaos", seen in results [v]) — computation maximized at the order-chaos transition in recurrent networks.
- Legenstein & Maass, "Edge of chaos and prediction of computational performance for neural circuit models," *Neural Networks* 20(3), 2007. [c]
- Langton, "Computation at the edge of chaos," *Physica D* 42, 1990 — the Class-4/λ-parameter source. [c]
- Beggs & Plenz, "Neuronal avalanches in neocortical circuits," *J. Neurosci.* 23, 2003. [c]
- **Cramer et al., "Control of criticality and computation in spiking neuromorphic networks with plasticity," *Nature Communications* 11, 2853 (2020)** [v — PMC record returned in search] — homeostatic plasticity tuning distance-to-criticality on BrainScaleS-2, task performance tracking the operating point. **This is the single most dangerous NPA for F2 as an isolated claim**: it demonstrates plasticity-mediated criticality control on neuromorphic hardware, published 2020. F2 alone is not novel; F2 *as a maintained control target inside a closure architecture* is where the drafting must go.
- P-CRITICAL (Ivanov & Rouat lineage, arXiv:2009.05593) — reservoir autoregulation plasticity rule for neuromorphic hardware. [v]

**Against F3 (redeployment / simulate-other-with-own-self-model):**
- **Bongard, Zykov & Lipson, "Resilient machines through continuous self-modeling," *Science* 314, 2006** [c, corroborated by Columbia pages [v]] — a robot inducing its own body model and re-using it after damage.
- Kwiatkowski & Lipson, "Task-agnostic self-modeling machines," *Science Robotics* 4, 2019. [v — returned verbatim in search]
- Rabinowitz et al., "Machine Theory of Mind," ICML 2018 (DeepMind ToMnet). [c] — learns models *of others*; notably does NOT re-use a self-model, which is our discriminator.
- Simulation-theory-of-mind literature (Gordon 1986; Gallese & Goldman 1998) — "re-run your own machinery offline to model others" as *theory*; caution per didactic pattern #30: the mirror-neuron reading is contested, but as prior art an examiner needs only the published idea. [c]
- Graziano & Kastner, "Human consciousness and its relationship to social neuroscience," *Cog. Neurosci.* 2011 / Graziano, *Consciousness and the Social Brain* 2013 — attention schema applied to self AND others with the same machinery. [c] Conceptually the closest published statement of "one model, self and other targets."
- Ha & Schmidhuber, "World Models," NeurIPS 2018 (arXiv:1803.10122). [v — lineage confirmed in multiple returned records]

**Against F4 (plastic-recurrence / fixed-readout sparse SNN):**
- Maass, Natschläger & Markram, "Real-time computing without stable states" (LSM), *Neural Computation* 14, 2002. [c]
- Jaeger & Haas, "Harnessing nonlinearity…," *Science* 304, 2004 (ESN). [c]
- Sussillo & Abbott, "Generating coherent patterns of activity from chaotic neural networks" (FORCE), *Neuron* 63, 2009 — training *with* feedback loops through a chaotic recurrent network. [c]
- **Bellec et al., "A solution to the learning dilemma for recurrent networks of spiking neurons" (e-prop), *Nature Communications* 11, 3625 (2020)** [v] — local plasticity training the recurrence of an SNN itself; the direct methodological anticipation of "a plastic recurrence learns what a frozen one cannot." No patent found for e-prop (searched; Graz/Intel filings not surfaced — professional check advised).
- Laje & Buonomano, "Robust timing and motor patterns by taming chaos in recurrent neural networks," *Nat. Neurosci.* 2013 — plasticity *in* the recurrence ("innate training"). [c]

**Against F5 (closure as consolidation channel):**
- McClelland, McNaughton & O'Reilly, "Why there are complementary learning systems…," *Psych. Review* 102, 1995 — the two-store fast/slow consolidation architecture. [c] The canonical frame an examiner maps F5 onto.
- Kirkpatrick et al., "Overcoming catastrophic forgetting in neural networks" (EWC), *PNAS* 114(13), 2017 (arXiv:1612.00796 [v]).
- Kumaran, Hassabis & McClelland, "What learning systems do intelligent agents need?" *TiCS* 2016; hippocampal-replay/consolidation modeling literature (Wilson & McNaughton 1994). [c]
- Hinton et al., knowledge distillation (arXiv:1503.02531) — transferring an explicit model's competence into another network; F5's "explicit→implicit transfer" must be distinguished from distillation (ours is via sustained re-entry through the closure loop within one substrate, measured by loop-removal). [c]

**General (would be cited against any consciousness-flavored framing):** Tononi IIT (2004, 2014) [c]; Friston free-energy/active inference (*Nat. Rev. Neurosci.* 11, 2010) [c]; Dehaene global-workspace implementations [c]; Chella & Manzotti, *Artificial Consciousness* (2007) [c]; Gamez, *Human and Machine Consciousness* (2018) [c].

---

## C. White space — what appears unclaimed

Single features are individually anticipated or fenced: F1 functionally (Kadin), F2 in NPA (Cramer 2020 — not in any patent), F3 in NPA (Lipson line, Graziano, ToMnet — not in any patent), F4's components (BrainChip circuits, Brain Corp rules, e-prop NPA), F5's neighborhood (EWC family + CLS theory). **No single-feature claim is safely novel. The portfolio value is entirely in combinations and in structural (not functional) claim language.**

Ranked by (novelty over found art) × (technical meaning):

1. **F1+F5 — the closure-as-consolidation claim. Strongest.** *"A neural system in which a self-model's outputs re-enter the world-model's state space through a return path, wherein sustained re-entrant activation transfers explicitly-learned structure into the plastic implicit substrate, verified by train-with-loop/test-loop-removed transfer."* Nothing found claims consolidation *through* a self-referential loop: EWC consolidates via importance penalties (no loop, no self-model), CLS/replay via a second memory store, distillation via a second network. The loop-removal measurement is itself a claimable method (a test protocol as method claim). This is also the feature pair the crucible experiment actually demonstrates — enablement is real, which none of the fringe consciousness grants can say.
2. **F1+F2 — closure maintained at criticality.** No patent claims criticality control at all; no publication combines a maintained distance-to-criticality set-point *with* a structural self-model return path. Cramer 2020 must be cited and distinguished (their control target exists, but on a reservoir with no self-model; ours conditions the closure architecture's operation on the regime). Draft F2 as a *control loop with a criticality order-parameter as set-point* (branching ratio, avalanche exponent, Lyapunov estimate) — never as "operating at the edge of chaos" (anticipated as a property; not as a maintained target inside this architecture).
3. **F3+F1 structural — redeployment with a containment condition.** "Re-point the self-model at another agent" as pure function is heavily NPA-anticipated (Graziano, simulation ToM, Lipson's other-modeling). What is NOT found anywhere: a claim tying redeployment to the *same* model instance whose outputs are contained in the world-model state space, with **recursion depth bounded (level-1)** as a claimed limitation. The shallow-depth bound is counter-intuitive (everyone else scales depth) and is exactly the kind of non-obvious limitation that survives — didactic pattern #26 is, verbatim, an inventive step argument.
4. **F4 inversion — plastic recurrence with fixed readout, closure-gated.** ESN/LSM (expired/NPA) fixed the recurrence and trained the readout; e-prop trains recurrence but with trained readouts and no architectural condition. A claim on *"fixed readout + plasticity confined to the recurrent substrate, wherein the plastic recurrence includes the closure return path"* inverts the reservoir tradition and is not found. Weakest as a standalone (e-prop is close); strong as a dependent claim under 1-3. The ~25k-neuron/0.06 GB demonstration is enablement evidence, not a claim limitation worth taking.
5. **Full-stack claim F1+F2+F3+F4+F5** — the substrate as demonstrated. Trivially novel over everything found; file as the narrow "picture claim" backed by the actual system, beneath the broader combination claims above.

**Drafting warnings from the found art:** (a) avoid functional "machine that models itself in its world model" language — Kadin '483/'965 sit on it until 2039 in the US; claim the containment/return-path structure and the measured transfer instead. (b) Avoid "agent plans using learned world model" as any load-bearing element — Google's Dreamer grant (US 12,533,800, active) and its family own that neighborhood. (c) Avoid generic "consolidating knowledge across tasks by protecting important parameters" — DeepMind's EWC family is alive and just survived §101 review.

---

## D. Freedom-to-operate flags (building & selling, separate from patenting)

| Risk | Asset | Status | Exposure | Action |
|------|-------|--------|----------|--------|
| **Low-moderate** | Kadin US 11,119,483 / 11,906,965 | Active to 2039, US-only | Functional overlap if our system is described as "machine that recognizes itself in its predictive VR model"; individual inventor, litigation unlikely but NPE-sale possible | Claim-chart review before US product launch; EU/other jurisdictions unaffected |
| **Low (hardware only)** | BrainChip US 8,250,011 + continuations | Parent active to ~2030; continuations later | Only if we build digital STDP synapse silicon; simulation/GPU untouched | Re-check continuation claims before any ASIC program |
| **Low** | Brain Corp SNN portfolio (US 9,275,326 et al.) | Mixed; '326 active to ~2033 | Only if we implement their specific E/I homeostasis rule shapes; our criticality-target control differs | Design-around trivially available (different control law and target) |
| **Low** | Thaler US 10,423,875 | Active to 2036 | Claims are perturbation/topological-state detection with critic — different mechanism | Distinguish in spec; no design change needed |
| **Watch** | Commons family (US 9,053,431 + live continuations) | Prosecution ongoing 2025 | Late claims could be aimed at layered self-aware networks | Monitor new publications in the family yearly |
| **Watch (unresolved)** | DeepMind EWC application(s); Verses AI active-inference filings; Intel Loihi learning-engine claims; possible TU Graz e-prop filings | Unknown numbers | F5 claim drafting; F2/F4 hardware paths | Items 1-4 of the professional search brief below |
| **None (expired/lapsed)** | Fraunhofer ESN (US 7,321,882), Haikonen/Nokia (US 6,625,588), Thaler '666, Thaler '388 (dead 2027), Irvine Sensors US 10,242,314 (fee-lapsed 2023) | Expired | — | Usable as prior art in our own prosecution |

Foundational good news: the entire reservoir-computing training paradigm, Haikonen's conscious-machine circuits, and the 1990s recurrent-network estate are out of protection. Nothing found prevents **building and selling a software/GPU implementation** of the substrate in any jurisdiction; the only hardware-path flags are BrainChip (digital STDP circuits) and the unexamined Intel estate.

---

## Coverage — what was actually searched, honestly

**Reached:** Google Patents individual records via direct fetch (9 records fully read: US11119483, US11906965, US10242314, US9053431, US8250011, US10423875, US20210158162/US12533800, US9275326, US7454388); general web search (≈20 queries) surfacing USPTO full-image records, Justia listings, Business Wire/press, PMC/arXiv for NPA.
**Blocked/not reached:** Justia detail pages (HTTP 403 robot-block); Google Patents *search UI* (JS-only — could not run assignee/CPC queries, only fetch known numbers); **Espacenet and WIPO PATENTSCOPE not reached at all** — no EP/CN/JP/KR native-language coverage; USPTO PatFT/PatentsView API not attempted. **Consequence:** the scan is US-centric and keyword-recall-limited. Chinese SNN filings (large volume post-2018) are entirely uncovered.
**Representative queries:** BrainChip/van der Made autonomous learning; Thaler DABUS bootstrapping; "artificial consciousness"/"machine consciousness" patents; edge-of-chaos + criticality + patent (multiple phrasings — consistently zero patent hits); EWC/catastrophic-forgetting + DeepMind; Lipson self-model patents; world-model RL patents; Loihi learning rules; Haikonen; e-prop/eligibility traces; Qualcomm Zeroth; homeostatic plasticity patents; Numenta HTM; theory-of-mind patents; Verses/active-inference filings.
**Known gaps for a professional search brief:** (1) pin the DeepMind EWC publication number(s) and claim scope; (2) VERSES AI assignee sweep on PATENTSCOPE; (3) Intel assignee sweep restricted to learning-engine/homeostasis claims; (4) TU Graz / IMEC / Forschungszentrum Jülich academic-institution SNN filings; (5) CPC-class sweep G06N 3/049 (spiking) × G06N 3/088 crossed with "self-model"/"criticality" full text on Espacenet; (6) CN filings.

**Status caveat:** all "active/expired" statuses are Google Patents status flags as of 2026-08-11, not a docketing report. US 7,454,388's ~2027 expiry and US 10,242,314's fee lapse were read from the records; everything else should be re-confirmed by counsel before reliance.
