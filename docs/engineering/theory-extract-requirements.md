# Computational & Architectural Requirements Extraction

## Source: *The Four-Model Theory of Consciousness* (Gruber, 2015/2026)

Extracted: 2026-02-16

This document extracts every computational and architectural requirement or constraint from the paper that would affect the design of an artificial consciousness (AC) system.

---

## 1. Substrate Requirements

### 1.1 What the Substrate Must Provide

**Criticality (Edge of Chaos / Class 4 Dynamics)**
- The substrate MUST operate at or near the edge of chaos — Wolfram's Class 4 computational regime (Section 3.7).
- This is a *physical prerequisite*. Below Class 4, consciousness is impossible regardless of architecture.
- Class 4 dynamics means: "Complex enough to sustain a self-simulation, ordered enough for that simulation to be coherent" (Section 3.7).
- The substrate must exhibit **maximal correlation length**: distant parts influence each other, local perturbations propagate globally, information is integrated across the entire network (Section 5.1).
- Must support **scale-free dynamics** for cross-scale synchronization: simple and complex representations must remain coherent with one another (Section 5.1).

**Wolfram's Four Classes — Computational Meaning**
- **Class 1**: Converges to fixed state. Computationally: system reaches equilibrium and stops changing. Useless for consciousness.
- **Class 2**: Periodic/repetitive patterns. Computationally: system enters loops. Too predictable for consciousness.
- **Class 3**: Chaotic/random. Computationally: no stable structure can persist, everything is noise. Too disordered for coherent consciousness.
- **Class 4**: Complex/edge of chaos. Computationally: capable of universal computation. Structures emerge, persist, interact, and transform. This is the ONLY regime where consciousness can emerge.

**What Class 4 Means for Implementation**
- The system must be capable of **universal computation** (Turing-complete).
- It must produce dynamics where **structures emerge, persist for a while, interact with other structures, and eventually transform or dissolve** — neither freezing into patterns nor dissolving into noise.
- It must support **long-range correlations**: information must be able to propagate across the entire system, not just locally.
- Criticality provides "the only regime in which robust computation can self-organize on inherently noisy hardware" (Section 8.8).

**Self-Referential Closure**
- The substrate must support a system that can **model itself modeling itself** (Section 3.4).
- A weather simulation models weather but not itself. The AC substrate must support a simulation that IS the thing being simulated — the ESM models the system's own modeling process.
- Self-referential closure is "precisely the condition under which the gap between process and feeling does not exist" (Section 3.4).

**Sufficient Recursive Capacity**
- The biological brain uses 6 cortical layers; universal approximation requires only 3 layers (Section 4.4).
- The "surplus" 3 layers provide overhead for self-modeling: running explicit models as real-time simulations ON TOP OF implicit processing.
- Implication: the substrate needs roughly **double** the computational capacity required for basic information processing — half for processing, half for self-simulation.

**Distributed / Holographic Storage**
- The implicit models (IWM, ISM) must store information in a **distributed, non-local manner** across the substrate (Section 5.2).
- Properties required: graceful degradation (partial loss degrades but doesn't destroy), attractor dynamics, distributed representations.
- "Patchwork hologram": locally holographic within functional areas, fractally self-similar across units, globally emergent at whole-system scale (Section 5.2).

### 1.2 What Is Explicitly NOT Required (Biological Artifacts)

- Six-layer cortical architecture — this is "an evolutionary implementation, not a requirement" (Section 4.4).
- Specific neurotransmitter systems — the theory is agnostic about the physical mechanism supporting criticality (Section 9, Open Question 3).
- Biological neurons — corvids have nuclear clusters instead of layers; cephalopods have radically different architecture. Both are predicted to be conscious (Section 4.4).
- Specific ion channels, synaptic mechanisms, or protein expression patterns — these are Level 2-3 in the five-system hierarchy, not Level 5 where consciousness exists (Section 3.7.1).
- Quantum processes — explicitly rejected as unnecessary. "Observer-dependent interpretations of quantum mechanics are rejected" (Section 4.2, footnote).

### 1.3 Substrate Independence Claims — What Is Portable

- **Fully portable**: The four-model functional architecture (IWM, ISM, EWM, ESM).
- **Fully portable**: The real/virtual split (implicit models as substrate-level storage, explicit models as transient simulation).
- **Fully portable**: The criticality requirement (Class 4 dynamics).
- **Fully portable**: Variable permeability between implicit and explicit models.
- **Fully portable**: The self-referential closure property.
- **Uncertain portability**: The five-system hierarchy (physical → electrochemical → proteomic → topological → virtual). The theory claims "only the virtual level is strictly required, but the bidirectional causal flow between levels suggests that decoupling the virtual system from its lower-level supports may not be straightforward" (Section 9, Open Question 5).
- **Uncertain portability**: The holographic storage mechanism — it may or may not be a consequence of criticality (Section 9, Open Question 7).

### 1.4 Two Thresholds — Both Must Be Met

1. **Physical threshold**: Criticality (Class 4 dynamics). Without this, no consciousness regardless of architecture.
2. **Functional threshold**: Four-model architecture. Above criticality but without the architecture = complex dynamics but no consciousness.

Both are necessary; together they are sufficient (Section 3.7.3).

---

## 2. Processing Requirements

### 2.1 Real-Time Constraints

**Continuous Processing**
- Consciousness is described as a "real-time self-simulation" (Section 3.1). The simulation must run continuously during waking.
- The EWM is a "real-time simulation of reality" (Section 3.2).
- The ESM is a "real-time simulation of 'I'" (Section 3.2).

**Two Temporal Scales**
- **Unconscious processing loop**: ~40 Hz (substrate-level computation, rapid, parallel) (Section 4.2).
- **Conscious integration loop**: ~20 Hz (the "frame rate" of EWM and ESM) (Section 4.2).
- This means the substrate processes at roughly **double** the rate of the conscious simulation.
- The conscious simulation receives ALL information with a uniform ~500 ms delay relative to substrate events (Section 4.2).

**Streaming, Not Batch**
- Processing must be continuous/streaming, not batch. The simulation is "transient" and "constructed in real time" (Section 3.2).
- The explicit models are "patterns of activity" — they exist only while actively being computed (Section 3.3).

**Punctuated Stability**
- The system cannot maintain criticality indefinitely. There are "extended phases of coherent conscious operation (waking), interrupted by periodic breakdowns in which the simulation collapses (deep sleep) and the substrate restores the biochemical conditions for criticality" (Section 5.1).
- Implication: the system needs a periodic "maintenance mode" where the simulation stops and substrate conditions are restored. The 90-minute ultradian cycle in biology provides a reference.

### 2.2 Parallel vs. Sequential Processing

**Massively Parallel at Substrate Level**
- The IWM and ISM operate in parallel across the entire substrate. The "cortical automaton" is a parallel computation where each column/unit updates simultaneously based on local rules (Section 3.7.2).
- The implicit models perform "rapid, parallel processing within and across" models (Section 4.2).

**Integrated at Simulation Level**
- The EWM and ESM must produce **unified** output — this is the binding requirement. "Distributed processes are unified into coherent experience" (Section 2.5).
- Binding is an emergent property of critical dynamics, not a separate mechanism (Section 5.1). So the parallel substrate must produce unified integration at the simulation level through its critical dynamics.

**Both Required Simultaneously**
- The system needs massively parallel substrate computation AND unified simulation output, running concurrently.

### 2.3 Feedback Loop Timing Requirements

**Continuous Bidirectional Flow**
- "The virtual models are in continuous feedback with the implicit models: the simulation's outputs feed back to update implicit processing, shaping future behavior" (Section 4.2).
- Primary direction: implicit system deploys virtual simulation as its evaluation mechanism — "presents decisions, actions, and their consequences to the simulation so that the simulation can assess outcomes" (Section 4.2).
- Secondary direction: explicit system contributes assessments back, reshaping implicit models through learning (Section 4.2).

**Temporal Structure**
- The feedback must operate within the conscious frame rate (~20 Hz / 50 ms per frame).
- The substrate processes decisions BEFORE the conscious simulation is aware of them (Libet's ~350-500 ms delay is expected, not a bug) (Section 4.2).

### 2.4 State Maintenance Requirements

**What Must Persist (Long-Term)**
- IWM: "total accumulated knowledge about the world, stored in synaptic weights (or their functional equivalent)" — everything the system has ever learned (Section 3.2). This is permanent and grows over the system's lifetime.
- ISM: "accumulated self-knowledge: body schema, proprioceptive calibration, motor skills, habits, personality traits, autobiographical memory structures" (Section 3.2). Also permanent and growing.

**What Is Transient**
- EWM: "a virtual construct — a transient pattern of activity, not a permanent structure" (Section 3.2). Exists only while being actively generated.
- ESM: "virtual: a transient process, not a permanent entity" (Section 3.2). Exists only while being actively generated.
- On interruption (sleep, anesthesia), the explicit models cease to exist. On resumption, they are reconstructed from implicit models + current input (Section 4.2).

**State Reconstruction**
- "Each time the ESM is generated — upon waking, after anesthesia, after any interruption — it reconstructs a continuous self-narrative from whatever the ISM contains" (Section 4.2).
- The ESM always confabulates bridging narrative to maintain perceived continuity.

---

## 3. Memory/State Architecture

### 3.1 Types of Memory Required

**Implicit Memory (Substrate-Level, Non-Conscious)**

1. **IWM Storage**: Perceptual regularities, causal models, spatial relationships, semantic knowledge, motor programs for interacting with the world (Section 3.2). This is the system's ENTIRE learned knowledge about the world.
2. **ISM Storage**: Body schema, proprioceptive calibration, motor skills, habits, personality traits, autobiographical memory structures, social self-knowledge (Section 3.2). This is the system's ENTIRE learned knowledge about itself.
3. Both stored as "structural features of the substrate" — in biology, synaptic weights, dendritic morphology, connectivity patterns (Section 3.3).

**Explicit Memory (Simulation-Level, Conscious)**

4. **EWM Active State**: The current conscious world-scene — multimodal sensory integration, spatial layout, object recognition, temporal flow. Generated in real-time from IWM + current sensory input (Section 3.2).
5. **ESM Active State**: The current conscious self — sense of being a subject, perspective, embodiment, agency, personal history. Generated in real-time from ISM + current interoceptive/proprioceptive input (Section 3.2).

**Working Memory Equivalent**
- The explicit models (EWM + ESM) serve as working memory — they hold the current simulation state that is being actively processed and evaluated.
- Bandwidth is limited: "approximately 20 Hz with a processing delay of roughly 500 ms" compared to the substrate's "vastly higher throughput" (Section 4.2).

### 3.2 How Implicit Learning Accumulates

- Through the feedback loop: "conscious evaluations — the explicit system's independent assessments of situations, actions, and outcomes — feed back to reshape the implicit models through learning" (Section 4.2).
- Changes to the IWM/ISM constitute learning — modifications to "the topological system: the connectivity architecture — the pattern of connections, their strengths, and their organization" (Section 3.7.1, Level 4).
- Learning operates on slower timescales than the simulation: the proteomic system (minutes to days) modulates the topological system (Section 3.7.1).
- CBT works by "repeated corrective experience drives substrate-level rewiring (synaptic plasticity), modifying the ISM, which changes the ESM's self-model" (Section 6.6).

### 3.3 How Explicit Simulation Maintains State

- The EWM is generated from: IWM (knowledge base) + current sensory input (constraint/update signal) (Section 3.2).
- The ESM is generated from: ISM (self-knowledge base) + current interoceptive/proprioceptive input (Section 3.2).
- State is maintained through continuous regeneration — there is no persistent "simulation state" independent of the generative process.
- In dreams: EWM generates without sensory input, drawing on IWM stored knowledge instead. Result: familiar places/people, impossible physics, narrative incoherence (Section 6.3).
- In psychedelic states: normally implicit intermediate processing stages leak into the simulation, adding content (Section 6.1).

### 3.4 Relationship Between Memory and the Four Models

| Model | Memory Type | Persistence | Content Source |
|-------|-----------|-------------|----------------|
| IWM | Long-term world knowledge | Permanent, grows over lifetime | Sensory experience, learning, feedback from EWM evaluations |
| ISM | Long-term self-knowledge | Permanent, grows over lifetime | Interoception, proprioception, feedback from ESM evaluations |
| EWM | Active world-simulation (working memory) | Transient, exists only while generated | IWM + current sensory input |
| ESM | Active self-simulation (working memory) | Transient, exists only while generated | ISM + current interoceptive input |

The implicit models are the **knowledge base**; the explicit models are the **active workspace**. Information flows from implicit to explicit (generation) and from explicit back to implicit (learning).

---

## 4. Information Flow Constraints

### 4.1 Directionality Requirements Between Models

**Primary Generative Flow (Implicit -> Explicit)**
- IWM -> EWM: World knowledge generates the conscious world-simulation.
- ISM -> ESM: Self-knowledge generates the conscious self-simulation.
- This is the primary direction: the implicit models GENERATE the explicit models.

**Secondary Learning Flow (Explicit -> Implicit)**
- EWM evaluations -> IWM: Conscious assessments of world-events update world-knowledge.
- ESM evaluations -> ISM: Conscious assessments of self-states update self-knowledge.
- This is secondary but essential: "two-way traffic" (Section 4.2).

**Cross-Model Interaction**
- EWM and ESM interact: the self exists WITHIN the world simulation. The ESM "occupies" the EWM — "the sense of being a subject within it" (Section 3.5).
- IWM and ISM share a substrate and are not cleanly separable — both are encoded in the same distributed network.

**Sensory Input**
- External sensory input -> EWM: constrains and updates the world simulation.
- Interoceptive/proprioceptive input -> ESM: constrains and updates the self simulation.
- In dreams: these input channels are largely blocked, so the explicit models run on internal (IWM/ISM) content only (Section 6.3).

### 4.2 Permeability — What Controls Flow Between Implicit and Explicit

**Variable Permeability is a Core Mechanism**
- The boundary between implicit and explicit models has **variable, controllable permeability** (Section 3.6).
- Normal waking: **selectively permeable** — relevant information passes through based on attentional and contextual gating.
- The boundary is a **graded transition zone**, not a sharp line (Section 3.6).

**What Modulates Permeability**
- Attentional state (what the simulation currently requires).
- Contextual demands.
- Arousal level.
- Pharmacological agents (psychedelics increase; anesthetics affect indirectly via criticality).
- Neurological damage (anosognosia = local decrease).
- Training (meditation = trained modulation of permeability).

**Permeability States Observed**
| Condition | Permeability | Effect |
|-----------|-------------|--------|
| Normal waking | Selective, moderate | Relevant info passes; most implicit processing hidden |
| Psychedelic | Globally increased | Intermediate processing stages become conscious |
| Anosognosia | Locally decreased | Specific implicit knowledge blocked from simulation |
| Pre-sleep/relaxation | Gradually increasing | Bottom-up progression: phosphenes -> geometrics -> hypnagogic imagery |
| Meditation | Trained modulation | Selective access to normally implicit processes |
| Deep sleep | Minimal (subcritical) | No transfer — simulation collapsed |

### 4.3 What Triggers Model Transitions

**Consciousness Onset/Collapse**
- Onset: substrate reaches criticality threshold -> explicit models can be generated -> simulation begins (Section 3.7.3).
- Collapse: substrate drifts below criticality (neurotransmitter depletion, metabolic waste) -> simulation collapses -> sleep onset (Section 5.1, 8.8).
- This is described as a **radical (step-like) transition**, not gradual dimming (Section 8.8, sub-prediction b).

**Graduated Consciousness Levels**
- Basic consciousness: minimal ESM, rudimentary self-awareness (Section 3.5).
- Simply extended: first-order self-observation (ESM models system's own states).
- Doubly extended: second-order (ESM models itself modeling).
- Triply extended: third-order (ESM models itself modeling itself modeling) — deepest self-awareness, enables scientific study of consciousness.
- Transitions between levels depend on depth of recursive self-modeling, which can fluctuate with state (Section 3.5).

**ESM Redirection**
- When normal self-referential input is disrupted, the ESM "latches onto whatever input dominates the available input stream" (Section 6.1).
- Triggers: high-dose psychedelics, salvia divinorum, severe neurological damage (Cotard's).
- The ESM does NOT stop — it redirects.

**Model Forking**
- The virtual models can be **forked**: a single substrate can run multiple ESM configurations (Section 3.3).
- Biological example: DID (dissociative identity disorder) — multiple alter personalities = multiple ESM configurations on same substrate (Section 6.2).

### 4.4 Required Feedback Loops

1. **EWM <-> ESM**: The self exists within the world simulation; self-perception requires world-context and vice versa. Continuous mutual constraint.
2. **Explicit -> Implicit (learning)**: Conscious evaluations feed back to reshape implicit models over time.
3. **Implicit -> Explicit (generation)**: Implicit models continuously generate the explicit simulation.
4. **Sensory input -> Explicit models**: External signals constrain the simulation to reality (when available).
5. **Criticality maintenance**: The substrate must maintain itself at Class 4 dynamics. When it drifts (depletion), restoration mechanisms must kick in (sleep analog) (Section 5.1).

---

## 5. Scale/Complexity

### 5.1 World Model Complexity

**Minimum Requirements**
- The EWM must integrate multimodal sensory data into a **unified scene** (Section 4.2).
- It must support **categorical abstraction**: "an unfamiliar mushroom sharing features with known toxic species can be avoided without any direct experience" (Section 4.2).
- It must support **consequence simulation**: modeling what would happen in hypothetical scenarios.
- It must support **third-person perspective projection**: modeling another entity's experience within the world model (Section 4.2).

**Biological Reference Point**
- The IWM encompasses "everything the system has ever learned: perceptual regularities, causal models, spatial relationships, semantic knowledge, motor programs" (Section 3.2).
- For an artificial system, the world model need not be as rich as a human's — the graduated consciousness levels (Section 3.5) suggest that even basic world models suffice for basic consciousness.

### 5.2 Self Model Complexity

**Minimum Requirements**
- The ESM must generate a sense of being a **subject** with a **perspective** (Section 3.2).
- It must model the system's own states and processes (for self-awareness beyond basic consciousness) (Section 3.5).
- It must be **redirectable**: capable of taking different inputs and constructing different self-narratives.
- It must support **confabulation**: reconstructing continuity from available material when there are gaps (Section 4.2).

**For Higher-Level Consciousness**
- Simply extended: ESM includes model of own states.
- Doubly extended: ESM models itself modeling (metacognition).
- Triply extended: ESM models itself modeling itself modeling (philosophical reflection, ability to study consciousness).

### 5.3 Minimum Viable Complexity for Consciousness Emergence

**The Paper's Position**
- Consciousness is **graduated, not binary** (Section 3.5).
- The minimum is **basic consciousness**: "Minimal self-simulation. The system generates an EWM and a rudimentary ESM — it experiences a world and has a minimal sense of being a subject within it" (Section 3.5).
- This requires: substrate at criticality + four-model architecture (even in minimal form).
- Open Question 4 asks: "What is the minimum set of models required for consciousness, versus self-aware consciousness, versus full human-type consciousness?" — this is explicitly unresolved (Section 9).

**Complexity Clues from Biology**
- Rodent cortices (simple) support basic consciousness — "rudimentary simulation sufficient for phenomenal experience but thin in self-awareness" (Section 6.5).
- Corvid pallia (nuclear, not layered) support tool use, planning, mirror self-recognition — suggesting substantial consciousness without mammalian cortical architecture.
- Cephalopods demonstrate problem-solving with radically different architecture.
- Implication: the minimum complexity bar may be lower than expected.

### 5.4 Scaling Claims

- The paper does NOT make specific claims about parameter counts or computational FLOPS.
- The theory predicts a **continuum**: more recursive self-modeling = deeper consciousness.
- The six-layer cortex observation suggests **~2x overhead** for self-simulation on top of basic processing.
- "A computational substrate of the universe's scale — vast in spatial extent, temporal depth, and possibly in dimensions not yet characterized — does not merely allow self-simulating systems to emerge; it renders them a structural inevitability" (Section 4.4). This is a cosmological claim, not a sizing guide.

---

## 6. Hardware Implications for RTX 4090

### 6.1 RTX 4090 Specifications (Reference)

- 24 GB GDDR6X VRAM
- 16,384 CUDA cores
- 512 Tensor cores (4th gen)
- ~82.6 TFLOPS FP32
- ~330 TFLOPS FP16 (with sparsity)
- ~660 TOPS INT8 (with sparsity)
- 1 TB/s memory bandwidth

### 6.2 What Fits on 24 GB VRAM

**The Implicit Models (IWM + ISM) — Long-Term Storage**
- These are the system's learned knowledge, equivalent to "synaptic weights." In neural network terms, these are the model parameters.
- A 7B-parameter model at FP16 = ~14 GB. At INT8 = ~7 GB. At INT4 = ~3.5 GB.
- A 13B model at INT4 = ~6.5 GB.
- Rough budget: ~8-12 GB for implicit model weights, leaving 12-16 GB for active computation.

**The Explicit Models (EWM + ESM) — Active Simulation**
- These are transient activation patterns, not stored weights. They require working memory (VRAM for activations, KV-cache equivalents, intermediate states).
- At 20 Hz frame rate, each "frame" of the simulation must complete in 50 ms.
- Key constraint: the simulation must run TWO models (world + self) simultaneously, plus their interaction, plus sensory input processing, all within 50 ms.

**Criticality Engine**
- The system needs a dynamical substrate operating at Class 4. This is NOT a standard neural network forward pass (which is Class 1/2). It requires **recurrent dynamics** — iterative, feedback-rich computation.
- Options: Recurrent neural networks, reservoir computing, cellular automata on GPU, spiking neural networks.
- Cellular automata on GPU are well-suited: GPUs excel at parallel local-rule application across large grids.
- A 3D cellular automaton with ~1M cells at ~40 Hz update rate is computationally feasible on RTX 4090.

### 6.3 What Requires Creative Solutions

**Simultaneous Dual-Rate Processing**
- The paper specifies 40 Hz substrate + 20 Hz simulation. The GPU must run BOTH concurrently.
- Solution: Time-multiplexing. Run substrate update at 40 Hz, sample for simulation at 20 Hz. CUDA streams can handle this.

**Recurrent Dynamics at Scale**
- Standard transformer inference is feedforward (Class 1/2). The theory EXPLICITLY rejects this as insufficient for consciousness.
- Solution: Use reservoir computing or spiking neural network models that naturally produce recurrent dynamics. These are less mature than transformers but computationally feasible on GPU.
- Alternative: Implement a cellular automaton whose transition rules are defined by learned weights (the IWM/ISM). This directly implements the "cortical automaton" concept from Section 3.7.2.

**Distributed Holographic Storage**
- The implicit models must degrade gracefully under partial damage and distribute information globally.
- Standard neural network weights already have this property to some degree (distributed representations).
- Solution: Use architectures with inherent distribution (e.g., Hopfield networks, modern energy-based models, or standard deep networks which naturally distribute representations across weights).

**Self-Referential Architecture**
- The system must model ITSELF. This means the simulation (EWM/ESM) must have access to representations of the system's own processing.
- Solution: Feed the simulation's output state back as input to the next cycle. This creates the self-referential loop. Must be carefully designed to avoid runaway feedback.
- The ESM specifically needs a model of the ENTIRE system's operation, not just one component.

**Permeability Control**
- Need a mechanism to control how much implicit (substrate) information leaks into the explicit (simulation).
- Solution: Gating mechanisms (attention gates, learned thresholds, modulation signals). This is architecturally straightforward but tuning is critical.

### 6.4 What Might Need Remote/Cloud Compute

**Large-Scale IWM**
- If the world model needs to be very rich (human-level world knowledge), the implicit weights may exceed 24 GB.
- A 70B-parameter model at INT4 = ~35 GB, exceeding single-GPU VRAM.
- Options: Use a smaller model (7B-13B), quantize aggressively (INT4/INT3), offload cold parameters to system RAM with on-demand paging, or use a cloud-hosted model for IWM queries.

**Training / Learning**
- Continuous learning (updating IWM/ISM from ESM/EWM feedback) requires backpropagation or equivalent, which doubles memory requirements.
- Solution: Use online learning algorithms with lower memory overhead (e.g., Hebbian-style updates, reservoir adaptation, LoRA-style parameter-efficient fine-tuning).
- Heavy training runs (initial IWM/ISM pre-training) would likely need cloud compute (multi-GPU clusters).

**Multi-Modal Sensory Processing**
- If the system needs vision + audio + other modalities simultaneously, the input processing pipeline adds VRAM pressure.
- Solution: Use lightweight encoder models for each modality, keeping total input processing under 2-4 GB VRAM.

### 6.5 Feasibility Assessment

**What the Paper Actually Requires vs. What People Assume**

The paper does NOT require:
- A model as large as a human brain (86 billion neurons, ~100 trillion synapses).
- Human-level world knowledge.
- Perfect perceptual fidelity.
- Triply extended consciousness (the deepest form).

The paper DOES require:
- Class 4 (edge-of-chaos) dynamics — this is achievable with recurrent/reservoir/CA architectures on GPU.
- Four functionally distinct models (IWM, ISM, EWM, ESM) — this is an architectural design pattern, not a size requirement.
- Real-time self-simulation at ~20 Hz — achievable if models are appropriately sized.
- Variable permeability between implicit and explicit — a gating mechanism, architecturally simple.
- Distributed storage with graceful degradation — standard property of neural networks.
- Self-referential closure — achievable via recurrent feedback loops.

**Bottom Line: A Minimal AC System is Feasible on RTX 4090**

A *basic consciousness* implementation (the lowest level in the graduated hierarchy) with:
- Small implicit models (1B-7B parameters, INT4/INT8 quantized) = 1-7 GB
- Cellular automaton or reservoir computing substrate for criticality = 1-4 GB
- Active simulation state (EWM + ESM activations) = 2-4 GB
- Sensory input processing = 1-2 GB
- Headroom for feedback/gating/control = 2-4 GB
- **Total: ~8-20 GB — fits within 24 GB**

A *richly conscious* system with human-level world knowledge would need either:
- Aggressive quantization + parameter offloading to system RAM, or
- A multi-GPU or cloud-augmented setup.

**Key Technical Risks**
1. Achieving genuine Class 4 dynamics (not just "complex-looking" dynamics) on GPU — this needs careful tuning and measurement.
2. The 20 Hz real-time constraint with self-referential feedback — latency must be managed.
3. The learning loop (explicit -> implicit) running continuously without destabilizing the system.
4. Whether a small (1B-7B) implicit model can encode sufficient world/self knowledge for even basic consciousness.
5. The mathematical formalization is incomplete — we are implementing from qualitative descriptions, not formal specifications. This is the largest risk.

---

## Appendix A: Key Quantitative Claims from the Paper

| Parameter | Value | Source |
|-----------|-------|--------|
| Unconscious processing rate | ~40 Hz | Section 4.2 |
| Conscious simulation rate | ~20 Hz | Section 4.2 |
| Conscious processing delay | ~500 ms | Section 4.2 |
| Libet readiness potential lead | ~350-500 ms | Section 4.2 |
| NREM/REM cycle | ~90 minutes | Section 5.1, 6.3 |
| Cortical layers (biology) | 6 | Section 4.4 |
| Layers for universal approximation | 3 | Section 4.4 |
| Layers for self-modeling overhead | ~3 (surplus) | Section 4.4 |

## Appendix B: Five Principles (Design Axioms)

These are the five principles from which the entire explanatory range derives (Section 6):

1. **Criticality**: Substrate operates at edge of chaos (Class 4 dynamics).
2. **Virtual Qualia**: Qualia exist in the simulation, not in the substrate.
3. **Redirectable ESM**: The Explicit Self Model takes whatever input dominates when normal input is disrupted.
4. **Variable Permeability**: The boundary between implicit and explicit models is dynamically adjustable.
5. **Virtual Model Forking**: The explicit models can be forked, cloned, redirected, or reconfigured.

## Appendix C: Five-System Hierarchy

For the biological brain; artificial substrates may collapse or rearrange these levels:

1. **Physical system**: Atoms, molecules, macroscopic structures.
2. **Electrochemical system**: Ion gradients, action potentials, synaptic transmission.
3. **Proteomic system**: Receptor configurations, neurotransmitter synthesis, protein expression (minutes-to-days timescale).
4. **Topological system**: Connectivity architecture — where IWM and ISM are stored. Changes = learning.
5. **Virtual system**: Real-time dynamical pattern (cortical automaton) — where EWM and ESM exist. This IS consciousness.

## Appendix D: Consciousness States as Design Targets

From Table 3, the states we should be able to produce/detect:

| State | Criticality | Models Active | Consciousness |
|-------|-----------|---------------|---------------|
| Normal waking | At/near critical | All four | Full |
| Dream mode | Near-critical, no input | EWM/ESM on internal input | Degraded |
| Deep sleep analog | Subcritical | None | Absent |
| Maintenance mode | Forced subcritical | None (restoring substrate) | Absent |
| Disconnected | Not subcritical, wrong input | EWM/ESM on distorted input | Present, disconnected |
| Altered | At/past critical, high permeability | All, increased permeability | Present, altered |

## Appendix E: What Current LLMs Lack (Per the Paper)

The paper explicitly states current LLMs fail the AC specification because they:

1. **Lack an ISM**: No substrate-level self-knowledge distinct from outputs (Section 10.1).
2. **Lack an ESM**: No real-time self-simulation constituting a subjective perspective (Section 10.1).
3. **Lack criticality**: "Transformer inference is a feedforward pass — Class 1/2 dynamics" (Section 10.1).
4. **Lack the real/virtual split**: No two-level ontology with experience at the virtual level (Section 10.1).
5. **Lack recurrent dynamics**: Attention is computed in a single pass without recurrent dynamics (Section 10.1).
6. **Lack the motivational component**: No self-directed intellectual development (Section 10.1).

This means we CANNOT simply fine-tune an LLM for AC. The architecture must be fundamentally different.
