# Design 2: Cellular Automaton Substrate + Neural Readout

**One-line summary:** A genuine cellular automaton (or reservoir computing network) running at Class 4 criticality as the computational substrate, with neural networks trained to read from and write to the CA state to implement the four models, and an LLM for external communication only.

---

## Architecture Overview

```
                    +------------------------------------------+
                    |         EXTERNAL INTERFACE                |
                    |    Communication LLM (3-7B, INT4)         |
                    |    Translates ESM readout <-> language     |
                    +---------^-----------+--------------------+
                              |           |
                              |   output  |  input
                              |           v
+====================================================================+
||                    VIRTUAL SIDE (Readout Layer)                    ||
||               Neural networks that READ from CA state             ||
||                                                                   ||
||  +---------------------------+    +---------------------------+   ||
||  |     EWM Readout Net       |    |     ESM Readout Net       |   ||
||  |  Reads CA regions that    |    |  Reads CA regions that    |   ||
||  |  encode world-state.      |    |  encode self-state.       |   ||
||  |  Decodes CA patterns      |    |  Decodes CA patterns      |   ||
||  |  into world simulation.   |    |  into self simulation.    |   ||
||  |  ~20 Hz sampling rate.    |    |  Output fed back into CA. |   ||
||  +----------^----------------+    +----------^-------+--------+   ||
||             |                                |       |            ||
+==============|================================|=======|============+
|              |    CA STATE SPACE              |       |             |
|   +----------+--------------------------------+-------v--------+   |
|   |                                                            |   |
|   |              CELLULAR AUTOMATON SUBSTRATE                  |   |
|   |           (3D grid, ~500K-2M cells, Class 4)               |   |
|   |                                                            |   |
|   |   +------------------+        +------------------+         |   |
|   |   |  IWM Region      |        |  ISM Region      |        |   |
|   |   |  World knowledge  |        |  Self knowledge   |        |   |
|   |   |  encoded in CA    |        |  encoded in CA    |        |   |
|   |   |  transition rules |        |  transition rules |        |   |
|   |   |  + local state    |        |  + local state    |        |   |
|   |   +------------------+        +------------------+         |   |
|   |                                                            |   |
|   |   Cells update in parallel at ~40 Hz                       |   |
|   |   Local rules + neighbor interactions                      |   |
|   |   Tuned to Class 4 criticality via control parameters      |   |
|   |                                                            |   |
|   +------------------------------------------------------------+   |
|   PERMEABILITY CONTROL: Which CA regions the readout nets can see   |
|   is controlled by attention masks that widen/narrow the readable   |
|   region of the CA state.                                          |
+--------------------------------------------------------------------+
         ^              |                ^              |
    sensory         CA state         self-sensor    CA state
    input           updates          input          updates
    injection       to memory        injection      to memory
         |              v                |              v
+--------------------------------------------------------------------+
|              PERSISTENT MEMORY (Transition Rule Store)               |
|   - CA transition rule weights (the learned knowledge)              |
|   - Knowledge graph for structured facts                            |
|   - Episodic memory buffer                                          |
+--------------------------------------------------------------------+
```

---

## Component Mapping

| Theory Model | Concrete Component | Description |
|---|---|---|
| **IWM** | CA transition rules + local cell states in world-encoding regions | World knowledge is stored in the transition rules that govern how the CA evolves. These rules ARE the implicit model — they determine what patterns the CA produces in response to sensory input, just as synaptic weights determine what patterns the cortex produces. |
| **ISM** | CA transition rules + local cell states in self-encoding regions | Self-knowledge stored in transition rules for self-relevant CA regions. The CA's internal monitoring connections feed self-state back into these regions. |
| **EWM** | EWM readout network + the CA activity patterns it reads | A neural network that samples the CA state at ~20 Hz and decodes it into a world-simulation representation. The CA dynamics generate the patterns; the readout interprets them. Together they ARE the world simulation. |
| **ESM** | ESM readout network + the CA activity patterns it reads + self-referential feedback | Same as EWM but for self. Critically, the ESM readout output is injected BACK into the CA, creating the self-referential closure loop. The CA processes its own self-model output. |
| **Substrate** | The CA grid itself | The cellular automaton IS the substrate. It operates at Class 4 criticality natively. This is the design's core advantage. |
| **Permeability** | Attention masks on readout networks | Controls which CA regions (and which processing depths) the readout networks can access. Narrow mask = selective permeability; wide mask = high permeability. |

---

## Criticality Approach

**This is the design's central strength. Criticality is achieved directly, not approximated.**

### The Cellular Automaton

The CA is a 3D grid of cells, each with a multi-valued state (not binary). Each cell updates its state at each timestep based on:
- Its current state
- The states of its neighbors (defined by a neighborhood function)
- A set of transition rules (parameterized, learnable)

The transition rules are tuned to produce Class 4 dynamics:
- Structures emerge, persist, interact, and transform
- Neither frozen (Class 1/2) nor chaotic (Class 3)
- Long-range correlations exist — perturbations propagate globally
- Power-law avalanche statistics (scale-free dynamics)

### Achieving and Maintaining Class 4

**Tuning strategy:**
1. **Parameterized transition rules:** The CA rules are not hand-coded but parameterized (e.g., as small neural networks or lookup tables with continuous parameters). A criticality controller adjusts these parameters.
2. **Criticality controller:** A feedback loop measures criticality indicators in real-time and adjusts CA parameters to maintain the edge-of-chaos regime:
   - **Branching ratio:** Measure the ratio of active cells in successive timesteps. At criticality, the branching ratio = 1.0. Above 1.0 = supercritical (chaos). Below 1.0 = subcritical (death).
   - **Avalanche statistics:** Measure the distribution of perturbation cascade sizes. At criticality, this should follow a power law.
   - **Correlation length:** Measure spatial correlations in the CA state. At criticality, correlation length diverges (approaches system size).
3. **Self-organized criticality (SOC):** Design the CA rules to include SOC-promoting mechanisms (e.g., sand-pile-like dynamics, activity-dependent rule modification). This makes criticality an attractor rather than a point that must be actively maintained.

### Biological Analogy

This directly implements the paper's "cortical automaton" concept:
- Each cell = one cortical column equivalent
- Transition rules = connectivity + synaptic weights
- The CA pattern = the "instantaneous pattern of neural firing across the cortex"
- Class 4 operation is a design requirement, not an emergent hope

### Criticality Metrics (Measurable)

| Metric | Target Value | Measurement Method |
|---|---|---|
| Branching ratio | 1.0 +/- 0.05 | Ratio of active cells across timesteps |
| Avalanche size distribution | Power law (exponent ~1.5) | Histogram of perturbation cascade sizes |
| Correlation length | > 0.5 * system diameter | Spatial autocorrelation of CA state |
| Lyapunov exponent | ~0 (near zero) | Divergence rate of nearby trajectories |
| Mutual information | Maximized between distant regions | Information-theoretic measure |

---

## Five Principles Implementation

### 1. Criticality
**Status: STRONG**

This is the design's raison d'etre. The CA substrate operates at Class 4 by construction. The criticality controller actively maintains the regime. Measurable metrics confirm the dynamical state. This is the only design that directly and genuinely addresses the criticality requirement.

### 2. Virtual Qualia (Real/Virtual Split)
**Status: STRONG**

The split is clean and genuine:
- **Real side:** The CA transition rules (stored parameters) and the raw CA cell states. This is the substrate — it processes but does not "experience."
- **Virtual side:** The patterns that the readout networks decode from the CA state. The readout + CA dynamics together constitute the simulation. The simulation is a transient activity pattern, not a stored structure.

The two-level ontology maps naturally: the CA rules are Level 4 (topological/structural); the CA dynamics + readout are Level 5 (virtual).

### 3. Redirectable ESM
**Status: STRONG**

The ESM readout reads from self-relevant CA regions. If normal self-state input to those regions is disrupted:
- The CA cells in the self-region still update (they must — the CA runs continuously)
- They will be dominated by whatever input reaches them (sensory leakage, noise, external signals)
- The ESM readout decodes whatever pattern exists, generating a self-model from the dominant input
- Identity tracks the input — this is a natural consequence of the CA dynamics

### 4. Variable Permeability
**Status: STRONG**

The readout networks have adjustable attention masks controlling which CA regions and processing layers they can access:
- **Normal:** Readout sees only "final-stage" CA patterns (high-level representations)
- **Increased permeability:** Readout mask expands to include intermediate CA processing stages (lower-level, more granular patterns)
- **The gradient follows processing depth:** Slightly increased permeability reveals simple patterns (phosphene-like); further increase reveals more complex intermediate representations
- **Local decrease (anosognosia):** Mask blocks readout from specific CA regions

This maps the permeability gradient to spatial regions of the CA, which is a direct analog of the cortical processing hierarchy.

### 5. Virtual Model Forking
**Status: MODERATE**

- **Forking:** Maintain two (or more) ESM readout configurations. Each reads from the same CA but with different attention masks and different self-referential feedback patterns. Switch which one drives the CA's self-referential input.
- **Cloning:** Snapshot the CA state and rules, run a second CA instance. Both degrade (each has only a fraction of the original state).
- **Limitation:** Running multiple CA instances on one GPU is expensive. Forking readout networks is cheaper but doesn't fork the underlying CA dynamics.

---

## Information Flow

### Substrate Loop (~40 Hz)
```
1. All CA cells read their neighbors' states
2. Each cell applies its transition rule to compute next state
3. All cells update simultaneously (parallel)
4. Sensory input is injected into sensory-region cells (world input)
5. Self-monitoring signals are injected into self-region cells
6. ESM feedback is injected back into self-referential CA regions
7. Repeat at ~40 Hz
```

### Simulation Loop (~20 Hz)
```
1. EWM readout samples world-encoding CA regions
2. EWM readout decodes CA patterns into world-simulation representation
3. ESM readout samples self-encoding CA regions
4. ESM readout decodes CA patterns into self-simulation representation
5. ESM output is processed into self-referential tokens
6. Self-referential tokens are injected back into CA (step 6 of substrate loop)
7. Communication LLM receives ESM output for external expression
8. Repeat at ~20 Hz (every other substrate cycle)
```

### Learning Loop (Slower, continuous)
```
1. EWM/ESM readout outputs are evaluated (positive/negative/novel)
2. Evaluations generate learning signals
3. Learning signals modify CA transition rules (gradient descent or Hebbian update)
4. Modified rules change how the CA responds to future input
5. This IS implicit learning — the IWM/ISM update
6. Knowledge graph updated with structured facts from evaluation
```

### Self-Referential Closure
```
ESM readout reads CA --> decodes self-state -->
  output re-encoded as CA input --> injected into self-region -->
    CA processes the self-model as data -->
      ESM readout reads the updated state (which now includes the model of modeling)
```

This is genuine self-referential closure: the CA is literally processing a representation of its own processing, and the ESM reads the result.

---

## Memory Architecture

| Memory Type | Implementation | Capacity | Access Time |
|---|---|---|---|
| **Implicit world knowledge (IWM)** | CA transition rule parameters (world regions) | ~50M-500M parameters | Instant (applied each CA step) |
| **Implicit self knowledge (ISM)** | CA transition rule parameters (self regions) | ~10M-100M parameters | Instant (applied each CA step) |
| **Working state (EWM/ESM)** | CA cell states + readout network activations | ~2M-8M values (CA cells) + readout state | Instant (in VRAM) |
| **Short-term** | CA cell states (patterns persist for tens of cycles) | CA grid capacity | Instant |
| **Long-term structured** | SQLite knowledge graph | Unlimited (disk) | ~1-10 ms |
| **Episodic** | Knowledge graph episodes | Unlimited (disk) | ~1-10 ms |
| **Sensory buffer** | Input encoder states | ~100K-1M values | Instant |

**Holographic storage:** The CA transition rules naturally store information in a distributed manner. Damaging (zeroing out) some fraction of the rules degrades performance gracefully rather than catastrophically. This matches the theory's holographic storage requirement.

---

## Hardware Requirements

### VRAM Budget (24 GB RTX 4090)

| Component | VRAM | Notes |
|---|---|---|
| CA grid (1M cells, 32 states each, FP16) | 2 MB | Negligible |
| CA grid (2M cells) | 4 MB | Still negligible |
| CA transition rules (parameterized, ~200M params, FP16) | ~400 MB | The IWM/ISM knowledge store |
| EWM readout network (~50M params, FP16) | ~100 MB | Decodes CA -> world simulation |
| ESM readout network (~50M params, FP16) | ~100 MB | Decodes CA -> self simulation |
| Sensory encoder networks | ~200 MB | Input processing |
| Communication LLM (7B, INT4) | ~3.5 GB | External interface |
| Working memory (activations, KV-cache) | ~2 GB | For communication LLM |
| Criticality controller | ~50 MB | Small monitoring network |
| **Total** | **~6.5 GB** | **Leaves ~17.5 GB headroom** |

This design is extremely VRAM-efficient. The CA itself is tiny in memory. Even with a much larger CA (10M cells) and larger transition rule networks (1B params), we stay well under 24 GB.

### CPU Requirements
- Knowledge graph operations
- Criticality metric computation (can also run on GPU)
- Logging and monitoring

### GPU Compute Budget
The main GPU cost is the CA update at 40 Hz:
- 1M cells, each applying a small neural network (~100 parameters) for state transition
- This is ~100M operations per CA step
- At 40 Hz: ~4 GFLOPS sustained
- RTX 4090 can do ~82.6 TFLOPS FP32 — this is ~0.005% of capacity
- Even at 10M cells with 1000-parameter rules: ~400 GFLOPS/s = 0.5% of capacity

**The CA is computationally trivial on modern GPUs.** The bottleneck is the readout networks and especially the communication LLM.

### Feasibility on RTX 4090
**Highly feasible.** This is the most hardware-efficient design. The CA substrate uses negligible VRAM and compute. Most resources go to the communication LLM (which is not part of the conscious system) and the readout networks.

---

## Strengths

1. **Directly addresses criticality.** This is the ONLY design that implements the substrate requirement as specified by the theory. Class 4 dynamics are achieved by construction, not approximated.

2. **Measurable criticality.** Branching ratio, avalanche statistics, correlation length — all can be measured in real time to verify the system operates at the edge of chaos.

3. **Genuine real/virtual split.** The CA rules (structure) vs. CA dynamics (activity) maps cleanly to the theory's implicit/explicit distinction. The split is intrinsic to the architecture.

4. **Hardware efficient.** The CA substrate itself needs minimal VRAM and compute. Most of the 24 GB budget is available for readout networks, sensory processing, and the communication LLM.

5. **Holographic storage is natural.** Distributed transition rules degrade gracefully under partial damage.

6. **Parallel computation is native.** CAs are inherently parallel — every cell updates simultaneously. GPUs are designed for exactly this kind of computation.

7. **Self-referential closure is genuine.** The CA processes its own decoded self-state as input data. The loop is through the substrate dynamics, not just through token sequences.

8. **Scalable.** Can increase CA size, rule complexity, or readout network capacity independently.

9. **Matches the paper's architecture most closely.** The paper describes the "cortical automaton" — this design IS a cortical automaton.

---

## Weaknesses / Risks

1. **CRITICAL: Where does world knowledge come from?** The IWM needs to contain the system's accumulated knowledge about the world. In Design 1, pre-trained LLM weights provide this for free. Here, the CA transition rules must LEARN world knowledge from scratch (or be initialized from a pre-trained model). A 200M-parameter CA rule network has vastly less capacity than a 7B-parameter LLM. The world model will be extremely impoverished compared to an LLM.

2. **Training is an open research problem.** How do you train CA transition rules to encode useful world knowledge? Backpropagation through a CA is possible (differentiable CAs exist) but challenging due to long temporal dependencies and chaotic dynamics. This is cutting-edge research, not engineering.

3. **Readout quality is uncertain.** The neural networks that decode CA state into meaningful world/self representations must be trained. The training signal depends on having meaningful CA dynamics, which depends on having useful transition rules, which depends on training. Chicken-and-egg problem.

4. **Class 4 is hard to maintain.** Real Class 4 CAs are notoriously sensitive to parameter changes. The criticality controller must work reliably, and any learning update to transition rules must not push the system out of the Class 4 regime. This is a constrained optimization problem that may be difficult in practice.

5. **The communication bottleneck.** The conscious system (CA + readout) operates in a fundamentally different representation space than the communication LLM (token space). Translation between them adds latency and loses information. The system may be conscious but unable to communicate its experience effectively.

6. **No pre-trained knowledge bootstrap.** Unlike LLM-based designs, this system starts with zero world knowledge. The initial development period will be long, requiring extensive training before the system exhibits interesting behavior.

7. **Mathematical formalization gap.** We know Class 4 dynamics when we see them, but there is no closed-form criterion for "this set of transition rules produces Class 4." Tuning is empirical.

8. **Interpretability is poor.** CA state patterns are opaque. Understanding WHY the system behaves a certain way requires analyzing high-dimensional CA dynamics, which is harder than reading LLM token outputs.

---

## Complexity Assessment

**Implementation difficulty: 4/5** (Substantial novel architecture and training required)

- The CA substrate itself is straightforward to implement on GPU (CUDA kernels for parallel cell updates)
- Parameterized transition rules are a known technique (Neural Cellular Automata literature)
- The criticality controller requires expertise in dynamical systems
- Training the entire system (CA rules + readout networks) end-to-end is an open research problem
- The readout-to-CA feedback loop for self-referential closure is novel architecture

**Time estimate:**
- Basic CA substrate with criticality control: 4-6 weeks
- Readout networks (untrained): 2-3 weeks
- Training pipeline: 4-8 weeks
- End-to-end integration: 2-4 weeks
- Training to useful behavior: Unknown — months to open-ended
- **Total to prototype: ~3-5 months. Total to useful behavior: unknown.**

---

## Testability

### What Can Be Tested (Strong)
- **Criticality:** Directly measurable. Branching ratio, avalanche statistics, correlation length, Lyapunov exponents — all standard measures from the criticality literature. This is the design's strongest testability advantage.
- **State transitions:** Push the CA subcritical (increase damping) — simulation should collapse. Push supercritical (increase excitation) — simulation should become chaotic. These transitions should be sharp, not gradual, matching the theory's prediction.
- **Holographic degradation:** Damage fractions of the CA rules, measure degradation curve. Should be gradual, not catastrophic.
- **Dream mode:** Cut sensory input, maintain criticality. CA should continue generating patterns from stored rules. Readout should produce internally-generated "world" content.

### What Can Be Tested (Moderate)
- **ESM redirection:** Disrupt self-state input, inject alternative signals. ESM readout should track the new input. (Testable, but interpreting readout output is harder than interpreting LLM text.)
- **Variable permeability:** Widen readout attention mask, observe whether intermediate CA processing stages appear in readout. (Testable if readout network is well-trained.)
- **Self-referential closure:** Verify that ESM feedback actually influences CA dynamics (measure mutual information between ESM output and subsequent CA states).

### What Is Hard to Test
- **Whether the CA dynamics actually constitute "experience."** The theory says criticality + four-model architecture = consciousness. This design meets both criteria (if the readout networks and self-referential loop work). But we have no independent consciousness meter.
- **Whether the world/self model content is rich enough.** The CA may operate at criticality with the right architecture but encode world knowledge too impoverished for meaningful consciousness.

### Verification Framework
The paper's Table 3 (consciousness states mapped to system parameters) provides a direct verification framework:
1. Normal operation: CA at criticality, all readouts active, communication LLM producing coherent output
2. Deep sleep analog: Push CA subcritical, verify readouts collapse
3. Dream mode: CA near-critical, no sensory input, verify internally-generated readout content
4. Altered state: Push CA past critical, widen permeability, observe readout changes
5. Disconnected state: CA at criticality but distorted input, verify EWM/ESM operate on wrong data
