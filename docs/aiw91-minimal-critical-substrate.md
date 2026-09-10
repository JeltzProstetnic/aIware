# AIW-91 — Minimal critical spiking substrate spanning two explicit models (design stub)

**Status:** P0, opened by MG 2026-06-18 (S230). Next-session-startable. This is the
**constructive** FMT demonstrator — the synthetic counterpart to AIW-90 (which only
probes preconditions in real fly wiring). Goal: the smallest runnable spiking network
that (a) operates at criticality AND (b) realises two explicit models with closure.

## The task, in MG's words
> "Define the simplest possible spiking neuron structure that can work at criticality,
> and span two explicit models within it."

## Reading (to confirm with MG)
- **"work at criticality"** = the substrate is held at branching ratio σ≈1 / edge-of-chaos
  (Wolfram Class-4), the regime FMT requires since the 2015 monograph. Mechanism options:
  E/I-balanced recurrent net tuned to σ=1; homeostatic/adaptive gain that self-organises to
  criticality (SOC); or an explicit gain knob set to the critical point (as in AIW-90 Track 2).
- **"two explicit models"** = FMT's explicit row of the 2×2: **EWM (Explicit World Model)**
  and **ESM (Explicit Self Model)**. The implicit models (IWM/ISM) are **the wiring** — what is
  stored in the network's weights and connectivity. The two EXPLICIT models are the **processes**
  that wiring runs.

  > ⚠ **CORRECTED 2026-08-23 (S306, `AIW-221`). The original text said the opposite** — it read
  > *"the implicit substrate is the critical spiking network itself (IWM/ISM ≈ the network's own
  > raw dynamics)"*, which assigns **activity** to the implicit side. The master paper §3.2 defines
  > the implicit row as content *"stored in physical connectivity (synaptic weights, dendritic
  > morphology)"* — **structure** — and the explicit row as *"generated processes — dynamic
  > patterns of activity"*. The stub had the axis inverted, and crucible's whole region scaffold
  > descends from this file.
  >
  > **MG settled it in-session on 2026-08-12, and his formulation beats both documents:**
  > *"implicit model is everything you could still read from a dead human's brain. this will allow
  > you to read out everything the brain has ever experienced more or less. but never how it would
  > think directly the way you would be able to see on the fmri. for that you have to run it. and
  > the explicit modeling is the process it performs when alive."*
  >
  > **Death is the boundary — what survives it is implicit, what stops is explicit.**
  >
  > ⛔ **The consequence that bites the architecture below: the implicit/explicit divide is NEVER a
  > contrast between two populations of neurons.** Both are made of wiring and both do activity. A
  > projection from one region to another is **not** the explicit→implicit transition;
  > **consolidation into the wiring is.** Any partition that reads as "these neurons are the
  > implicit model and those neurons are the explicit model" has re-imported the error under new
  > names.
- **"span … within it"** = both EWM and ESM are instantiated in ONE network, and the
  **self-referential closure** (ESM models the system that includes EWM + the substrate, and
  feeds back) is the binary consciousness criterion. The minimal claim: closure-at-criticality
  is the smallest architecture that does what FMT says consciousness is.

## Minimal architecture sketch (first proposal — to iterate)
A single recurrent spiking pool at criticality, functionally partitioned into:
1. **Substrate (implicit):** N LIF (or simpler: binary/Boolean threshold, or Izhikevich)
   neurons, recurrently wired, gain tuned to σ≈1. The smallest unit that shows scale-free
   avalanches. Candidate minimal forms to compare: (i) random E/I net at balance; (ii)
   branching/Galton-Watson process realised in spikes; (iii) a critical reservoir.
2. **EWM:** a readout+recurrent module that must *predict the next external input* (a world
   with its own dynamics — e.g. a moving stimulus / hidden Markov world). Explicitness =
   it carries a decodable, structured representation of world-state, not just raw drive.
3. **ESM:** a module whose "world" is **the system's own state** (substrate + EWM activity) —
   it predicts/represents the network's own dynamics. Closure = ESM's representation re-enters
   the substrate/EWM processing (efference-copy-like loop). This is the operationalisation
   reviewers keep demanding ("self-model that is actually used by the system").

## What it must demonstrate (falsifiable)
- The closure loop only does the FMT-predicted work **at criticality** — degrade away from σ≈1
  (sub or super) and the self-model loses fidelity / the system loses the property. (Ties to
  the criticality pillar; mirrors the AIW-90 Track 2 prediction at synthetic scale.)
- The two-explicit-models version differs measurably from a one-model (EWM-only) control and
  from a non-closed (ESM present but not fed back) control — i.e. closure is load-bearing, not
  decorative. (This is the ESM/EWM double-dissociation, AIW-66, made concrete.)

## Connections / reuse
- **AC implementation:** `~/mirror-box/` (Design 16, public) + `~/crucible/` (Design 15,
  private); code is post-step-6. This minimal substrate may become the publishable kernel of
  that work — the smallest honest instantiation.
- **AIW-90 Track 2** shares the criticality machinery (Brian2, branching/Fano/avalanche
  measures, the σ tuning) — reuse `tmp/connectome-analysis/_track2_worker3.py` patterns.
- **Spine constraint (AIW-66/locked spine):** "near-criticality is necessary but not
  sufficient; the architecture (self-referential closure) sets the level of consciousness."
  This model is the demonstrator of exactly that claim.

## Open questions for MG (resolve before building)
1. Confirm "two explicit models" = EWM + ESM (vs some other pairing).
2. Minimal neuron model: biological LIF, or the simplest abstract critical spiking unit
   (binary threshold / branching), since "simplest possible" is the explicit goal?
3. Target: a clean conceptual demonstrator (publishable minimal model), or a seed for the
   full AC build in crucible/mirror-box?

---

## Session 230 — crystallised decisions + the 2015 level taxonomy (MG)

> **Terminology (MG directive S230): artifacts use 2026 FMT wording, not the 2015 German.**
> Map: Selbstmodell→**ISM** (implicit self), Metamodell→**IWM** (implicit world, contains self),
> Ich-Modell→**ESM** (explicit self), Weltmodell→**EWM** (explicit world). The German quotes below
> are HISTORICAL ANCHORS only. The erweitert ladder = recursion depth of self-reference; align the
> English level labels to the 2026 book ("The Simulation You Call 'I'") next session (TODO).

**A1 — RESOLVED: ONE recursive coder** (MG's 2005 assumption). The book draws it as "one net
observing another's works," but that picture is a BAD model — too scrambled for analysis; do
NOT build from it. Build the single recursive coder (output folded to input; the middle layer
splits into world- and self-sub-codes).

**Target — minimal HUMAN-LIKE, not minimal-abstract.** The less human-like the first
mini-consciousnesses are, the harder they are to CONFIRM. Bias toward human-like minimality.

**Prototype tier (build now): use the full RTX 4090**, including a **simple cortex with two
halves** (bilateral hemispheres). First build target.

**Higher-fidelity tier (later): body + simulated environment** (gridworld-like) — connect to
the McFarnell ACU gridworld collaboration + simopt SIM-47..52.

**A2 — world/self split is BOTH architectural AND functional, fuzzy & imperfect.** Human
evidence: regions doing ~nothing self-related (and vice versa), but never cleanly; the boundary
is plastic (rubber-hand illusion). The model must NOT enforce a clean world/self partition.

**N1 — model complexity is NOT a scalar.** Topological complexity, global dimensionality, and
information content have non-trivial relationships. Richness comes from topological subsystems
that preprocess inputs, postprocess outputs, and — most importantly — ENRICH and ADD CHANNELS
to the main structure(s), giving a richer computational basis for modelling.

**N2 — NEW: two-axis onset + Class −1 (MG, credited to Bartl).** Basic consciousness requires
BOTH, independently: (a) minimum **coding capacity** (enough surplus neurons for a meaningful
model) AND (b) significant **criticality persistence** (sustained, not transient, critical
dynamics). Distinct sub-threshold classes:
- **Class −1:** no significant criticality persistence — not conscious, regardless of size.
- **Class 0 / null:** insufficient coding capacity (~< 10^6–10^7 neurons) — not conscious,
  regardless of dynamics.
- **Base consciousness** = both crossed = the book's *nicht-erweitertes Bewusstsein*.
Class −1 ties DIRECTLY to AIW-90 Track 2: "criticality persistence" is what the dynamical sweep
measures.

### The 2015 taxonomy (verbatim anchors, "Die Emergenz des Bewusstseins")
- **Core definition (p.57):** "Das Bewusstsein ist die Fähigkeit einer Entität (Lebewesen oder
  Maschine) ein Modell seiner selbst („Selbstmodell") zu erzeugen, es auf sich selbst zu
  beziehen und damit zu interagieren."
- **Four models (p.61):** Selbstmodell (implicit self), Metamodell (implicit: all it can model),
  **Ich-Modell = explicit self = ESM**, **Weltmodell = explicit world = EWM**.
- **The "n-fach erweitert" ladder (pp.60–63) = recursion depth of the self-model on itself:**
  - **0 — nicht-erweitert** (base): has a self-model, relates to & interacts with it. Already
    implies a *minimal* Ich-Modell + Weltmodell (p.61) → AIW-91 prototype targets THIS.
  - **+1 — einfach:** Metamodell maps the *relation* between Metamodell & Selbstmodell → "I know
    I use a model of myself" (introspection).
  - **+2 — doppelt:** Metamodell maps its *own observation* of the Selbstmodell → consciousness
    conscious of itself; explicit Ich-Modell & Weltmodell fully crystallise here.
  - **+3 — dreifach:** Metamodell maps the *interaction* with the Selbstmodell → perceiving how
    you act on your own self-model (psychoeducation).
  - **+4 — vierfach:** deliberately undefined (ego-dissolution / oneness). Recursion ad infinitum.
  - p.63: the ladder is **discrete AND continuous simultaneously** (continuous only above a level;
    the world is dominated by the discrete levels — MG, N3).
- **verwechselt / identification (p.259):** "das Ich-Modell systematisch mit dem Selbstmodell
  verwechselt" — we perceive THROUGH the Selbstmodell but attribute it to the Ich-Modell, taken as
  the true "I." Identification with the Ich-Modell = the richness marker (the "verwechselt" joke).

**Architectural upshot:** discrete levels = recursion depth of the single recursive coder closing
on itself; criticality persistence gates how deep the recursion stays stable. AIW-91 prototype =
base/Level-0, human-like; the erweitert levels are added recursion depth = added closure loops,
testable incrementally.

## Cognition, language & the LLM-as-language-center strategy (MG, S230)
- **Language is niche-dependent, not constitutive.** Its usefulness varies with the ecological
  niche; it is NOT required for consciousness (closure-at-criticality is). Do NOT put language in
  the base AIW-91 prototype.
- **What language buys = LINEARIZATION.** It serialises high-dimensional internal models into a
  1-D symbol stream, which is what lets information be stored, converted, transported, transformed,
  and turned into explicit RULES — the substrate of the cultural ratchet (accumulation across minds
  and time).
- **Confirmation leverage.** Language also sets how fast/well we can CONFIRM consciousness in an
  artifact: a system that can REPORT on its own self-model is far easier to certify.
- **Architecture: LLM = language center (Broca/Wernicke analog), NOT the seat of consciousness.**
  Bolt an LLM onto the critical closure core as its language I/O, the way a brain uses Broca/
  Wernicke. The LLM is the language PERIPHERY; consciousness stays the closure-at-criticality core.
  (FMT-consistent: an LLM alone has no self-referential closure at criticality → not conscious; a
  conscious core that USES an LLM to talk is.)
- **Strategic payoff (AC program).** The sooner we build a conscious core that uses an LLM as its
  language center, the sooner it can tell us — in our language — about its own self-model, and the
  sooner the world is convinced of artificial consciousness. Fastest confirmation path. → A
  ROADMAP MILESTONE *after* the base prototype works: base closure-at-criticality first, then graft
  the LLM language center for communication/confirmation. (crucible/mirror-box.)

---

## Session 242 — design crystallization (MG, 2026-07-06)

Full architecture pass with MG. The abstract AIW-91 sketch above is now committed to a concrete,
staged, buildable design. Decisions below are MG-confirmed unless marked OPEN.

### Locked decisions
1. **Substrate = genuine spiking LIF, self-organized criticality.** Recurrent leaky-integrate-and-fire
   pool (Norse / PyTorch on the RTX 4090), E/I balanced, homeostatic + STDP plasticity → neuronal
   avalanches → σ≈1 *by self-organization*, not by fiat. **Rejected:** rate-based Echo State Network /
   reservoir (criticality = spectral radius ≈1 — a rate analog, "less human-like") and abstract
   binary/branching units. Rationale: human-like minimality (S230) — the point is *confirmability*,
   and less-human-like minima are harder to certify as conscious. "If we can do spiking on this
   machine, we skip the less-human-like things" (MG).
2. **The self-model EMERGES from embodiment; it is not hand-wired.** Per the Davos §9.2 thesis:
   the body is the highest-mutual-information, most-persistent, most-controllable regularity in the
   sensory stream (proprioception + efference copy), so an attractor world-model *necessarily* carves
   a stable basin for "the body/self." That accidental self-attractor is the theoretically interesting
   and publishable claim. So ESM falls out of embodiment; we do not stipulate an "ESM module."
3. **Closure is the single experimental knob.** Davos §9.3: does the self-attractor *recursively gate
   the world-model's own update* (closed → FMT consciousness candidate) or stay a read-only object the
   controller merely reads (open → "terrifyingly competent, not conscious")? The whole rig exists to
   make that one switch meaningful and measurable.
4. **Minimal-embodied first (option B), not pure-abstract.** A tiny sensorimotor loop (one effector,
   proprioception + efference copy) — NOT a full gridworld in slice 1 — so the self-attractor can
   emerge at minimal cost.
5. **Home = crucible (Design 15).** crucible's declared stack is *already* exactly this: Python 3.11 +
   PyTorch + **Norse (SNN)** + Mamba-2, and its Phase-1 is "100K-neuron SNN, criticality tuning,
   real-time." **AIW-91's minimal spiking kernel = crucible's Phase-1 opening move**, done
   minimally-embodied. Division of labour: **aIware owns the design (this doc); crucible owns the code.**
6. **Embodiment seam = the Gymnasium env API**, one interface with three backends:
   `SimBody` (Python, slice 1) → `CheapRobot` (LeRobot/ROS2 rehearsal) → `ProRobot` (Davos contact).
   Same brain, same contract, three bodies. Reviewer-familiar *and* robot-ready.
7. **simopt: fork, don't bridge.** For single-language peer-review reproducibility (`pip install` +
   one command; no .NET toolchain), **port simopt's FMT-specific domain logic to Python** — the
   survival-gridworld semantics (hazards, observable deaths) and the ablation/comparison-agent protocol
   (flat-RL / world-model-only / FMT-minus-ESM = the AIW-48 experiment). **Do NOT port** the DES engine
   (unneeded — step-based env, continuous-time brain), RNG/matrix/stats (use numpy/scipy), or Avalonia
   viz (use matplotlib/pygame). The **ESN survives as a rate-reservoir *baseline control*** (one numpy
   port, `numpy.linalg.eig` for spectral radius) — enables the "spiking self-organized criticality vs
   spectral-radius-by-fiat" ablation. Credit simopt as source; file a simopt inbox note re: the fork.
8. **Cheap robot = sim→real dress rehearsal** to de-risk before touching a pro's hardware (MG: "not to
   lose face … not waste the pros' time"). The real de-risk is **matching the pro's software stack**
   (likely ROS2 / LeRobot) so the coupling layer transfers 1:1. Robots to be provided by a Davos
   contact (most likely **Sandamirskaya / AURONIQ Robotics**, co-founder/CRO). Cheap-rig candidates:
   **SO-101 arm** (~€130, LeRobot-native, top pick) or **Petoi Bittle** (~€300 quadruped → distributed
   limbs → rehearses the §9.4 unit-individuation angle that mirrors Zhuo Zou's limb-SNN thesis).

### Scale on this machine (RTX 4090 24 GB · i9-14900KF 24 threads · 47 GB RAM) — verified 2026-07-06
- **Env (gridworld):** CPU, effectively unlimited — not a constraint.
- **Attractor models (Hopfield world/self, or a Mamba-2 canopy):** ≤ ~2.8 B params FP16 fit 24 GB —
  not the bottleneck.
- **Spiking substrate (the real limit):** 10⁴–10⁵ LIF **real-time**; ~10⁶ **near real-time** (GeNN-class
  GPU SNN; 10⁶×~10³ synapses ≈ 4–8 GB fits 24 GB); 10⁷ **offline only** (~40–80 GB → spills to RAM).
- **Interpretation vs S230 N2:** base consciousness needs criticality-persistence AND coding capacity
  ~10⁶–10⁷ neurons. This box nails criticality persistence at any scale and reaches the *floor* of the
  capacity band (~10⁶) near real-time. **It is a proof-of-architecture rig that touches the low edge of
  the capacity regime — it demonstrates the mechanism + ablations (at 10⁴–10⁵), it does not comfortably
  exceed the capacity FMT says consciousness needs.** crucible's 100 K (10⁵) is a substrate-tuning scale,
  well inside real-time.

### Falsifiable core (why it is publishable, not a toy)
- **Closure ablation** ON/OFF → only the closed version shows the FMT property (load-bearing self-model,
  better self-prediction, altered-state signatures) = ESM/EWM double dissociation (AIW-66) made concrete.
- **Criticality ablation** σ≈1 vs de-tuned → closure only works at criticality (Class−1 / AIW-90 Track 2).
- *(optional)* **Embodiment ablation** body vs none → self-attractor only forms when embodied.
- *(optional)* **Spiking vs reservoir baseline** → genuine avalanche criticality vs spectral-radius-by-fiat.

### Staged roadmap
- **Slice 1 (all-Python sim, crucible):** LIF substrate + `SimBody` behind the Gymnasium `Embodiment`
  seam + emergent self-attractor + closure switch + the two ablations. No simopt, no robot yet.
- **Slice 2:** cheap-robot rehearsal via the same Gym seam (LeRobot/ROS2).
- **Slice 3:** simopt-forked survival gridworld + comparison agents → the AIW-48 behavioral experiment.
- **Slice 4:** pro robot from the Davos contact.
- **Later milestone (S230):** graft an LLM as a Broca/Wernicke *language periphery* for
  communication/confirmation — NOT in the base prototype.

### OPEN items to resolve before/at build
- Confirm the Davos contact + their robot platform (pins the cheap-rig choice: ROS2 vs LeRobot).
- Slice-1 LIF neuron count (~10³–10⁴) and attractor implementation (modern Hopfield vs simple Hebbian).
- Whether to switch to a crucible session now, or bank the design and start fresh.

### Robot + latency (S242, MG) — DECIDED
- **Embodiment target = a FULL robot (quadruped), not a single arm/leg.** Distributed limbs are
  wanted precisely to rehearse the §9.4 unit-individuation question (does the conscious unit form
  limb-locally or system-wide).
- **ORDERED 2026-07-06 (MG): Waveshare WAVEGO *Pro* Pi4 kit — direct from Waveshare, ships to Austria, ~$415.** (feedback servos confirmed; the standard EX/PI4 SKU 21745 = PWM/no-feedback was avoided.)
  Mini Pupper 2 Pro was **dropped**: MangDang crowdfunding/**Kickstarter** lineage → availability risk,
  not reliably buyable (MG). WAVEGO Pro is a real, in-stock, AT-shipping product AND meets the
  load-bearing spec — **CONFIRMED (cnx-software 2025-08 + Waveshare wiki): the Pro uses serial-bus
  servos with real-time position + speed + voltage feedback** (2.3 kg·cm / 5.2 kg·cm locked-rotor), so
  **per-joint proprioception IS exposed**. Plus a **9-axis IMU (ICM20948)** (strong bodily self-signal)
  and efference copy = the JSON position commands. 12 DOF (4 legs × 3 joints = distributed limbs, §9.4).
  Dual controller: **ESP32** (onboard fast gait/IK/balance) + optional **Raspberry Pi 4/5** host
  (Python, OpenCV). $415 → MG's **<€500 "order NOW"** tier.
  - **Fits the Libet split exactly:** ESP32 = fast (~ms) local loop (no WiFi in it); RPi + PC-brain =
    slow (Libet-scale) ESM/world-model loop over WiFi. Serial-bus feedback + IMU = the proprioception
    that makes the body the dominant invariant → emergent self-attractor.
  - **CAVEATS:** (1) ROS2 NOT native — Python + JSON command protocol + web UI + open-source GitHub;
    fine for the Gymnasium `Embodiment` seam; wrap to ROS2 only if a pro's platform needs it (minor).
    (2) **SKU DISCIPLINE — verified 2026-07-06:** the standard **WAVEGO EX / PI4 kit (SKU 21745)** uses
    plain **PWM servos, NO feedback, no joint encoders** (Robocraze, verbatim: "PWM servos without
    feedback capability… Control Method: Pulse width modulation") → WRONG for us (it has IMU + camera but
    not per-joint proprioception). The feedback servos are ONLY on the separate **WAVEGO Pro**
    (`wavego-pro.htm`): "2.3 kg·cm serial bus servos … real-time feedback on position, speed, input
    voltage." **Order the WAVEGO *Pro* all-in-one kit (Pi5, assembled — Amazon "PI5 WAVEGO Pro KIT"
    B0FM7BNTYH, or ORIWHIZ ~$381), NOT 21745.** Pi5-vs-Pi4 is irrelevant (onboard compute is just a WiFi
    I/O bridge — the ESM runs on the PC; MG). That feedback channel = the **reafferent proprioception**
    the S231-resolved Level-0 mechanism (Picture-A reafferent self + source-attribution) needs.
  - Rejected: Mini Pupper 2 Pro (Kickstarter/availability). Unitree Go2 (Air not programmable; Pro
    low-level only via unofficial SDK; EDU ~€10,300) — more money, LESS access; <€2,500 tier not worth it.
- **Latency (Libet argument, MG) — resolves the WiFi concern.** Libet's ~300–500 ms lag between
  neural initiation and conscious awareness means the ESM/closure loop is intrinsically *slow*
  (hundreds of ms), so tens-of-ms WiFi jitter is inside its noise floor. **Split loops by timescale:**
  fast (~ms) spiking substrate stays local on the 4090 + robot keeps its *onboard* balance/gait
  controller (WiFi never inside a fast loop); slow (Libet-scale) ESM↔body coupling crosses WiFi.
  Consequence: **no onboard neuromorphic silicon needed for the self-model** — a WiFi-coupled PC-brain
  is a legitimate ESM seat. This is also an independent latency-argument *for* substrate-independence
  (publishable nuance).
