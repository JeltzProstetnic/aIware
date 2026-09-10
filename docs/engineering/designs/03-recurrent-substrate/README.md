# Design 3: Recurrent Neural Substrate

**One-line summary:** Recurrent neural networks (or state-space models like Mamba) whose continuous dynamics naturally exhibit edge-of-chaos behavior serve as the substrate; the four models are functional regions within the recurrent network, trainable end-to-end via backpropagation through time.

---

## Architecture Overview

```
                    +------------------------------------------+
                    |         EXTERNAL INTERFACE                |
                    |    Communication LLM (3-7B, INT4)         |
                    |    Translates ESM decoder <-> language     |
                    +---------^-----------+--------------------+
                              |           |
                              |   output  |  input
                              |           v
+====================================================================+
||                    VIRTUAL SIDE (Decoder Heads)                    ||
||              Projection layers that decode hidden state            ||
||                                                                   ||
||  +---------------------------+    +---------------------------+   ||
||  |     EWM Decoder Head      |    |     ESM Decoder Head      |   ||
||  |  Projects world-relevant  |    |  Projects self-relevant   |   ||
||  |  hidden states into       |    |  hidden states into       |   ||
||  |  world-simulation space.  |    |  self-simulation space.   |   ||
||  |  Sampled at ~20 Hz.       |    |  Output fed back to RNN.  |   ||
||  +----------^----------------+    +----------^-------+--------+   ||
||             |                                |       |            ||
+==============|================================|=======|============+
|              |   PERMEABILITY CONTROL         |       |             |
|   (Gating network that controls which hidden  |       |             |
|    states are accessible to decoder heads)     |       |             |
+==============|================================|=======|============+
|              |                                |       v             |
|   +------------------------------------------------------------+   |
|   |                                                            |   |
|   |         RECURRENT NEURAL SUBSTRATE                         |   |
|   |      (Continuous-time RNN / State-Space Model)             |   |
|   |                                                            |   |
|   |   Hidden state h(t) evolves according to:                  |   |
|   |   dh/dt = f(h(t), x(t), u(t); W)                         |   |
|   |                                                            |   |
|   |   Where:                                                   |   |
|   |     h(t) = high-dimensional hidden state (~10K-100K dims)  |   |
|   |     x(t) = sensory + interoceptive input                   |   |
|   |     u(t) = ESM feedback (self-referential input)            |   |
|   |     W    = learned weight matrices (IWM + ISM knowledge)   |   |
|   |     f    = nonlinear transition function                    |   |
|   |                                                            |   |
|   |   +-------------------+      +--------------------+        |   |
|   |   | IWM Subspace      |      | ISM Subspace       |        |   |
|   |   | Weights encoding  | <--> | Weights encoding   |        |   |
|   |   | world knowledge   |      | self knowledge     |        |   |
|   |   | (shared substrate)|      | (shared substrate)  |        |   |
|   |   +-------------------+      +--------------------+        |   |
|   |                                                            |   |
|   |   Updated at ~40 Hz (continuous dynamics discretized)      |   |
|   |   Tuned to operate at edge of chaos via spectral radius    |   |
|   |   and weight initialization                                |   |
|   +------------------------------------------------------------+   |
|                          REAL SIDE                                  |
+--------------------------------------------------------------------+
         ^              |                ^              |
    sensory         state updates    self-sensors    state updates
    input x(t)      to memory        input          to memory
         |              v                |              v
+--------------------------------------------------------------------+
|              PERSISTENT MEMORY (Weight Store + Episodic)             |
|   - RNN weight matrices W (the implicit model knowledge)           |
|   - Knowledge graph for structured episodic/semantic memory         |
|   - Checkpoint states for recovery                                  |
+--------------------------------------------------------------------+
```

---

## Component Mapping

| Theory Model | Concrete Component | Description |
|---|---|---|
| **IWM** | Weight matrices W in world-relevant subspace | The RNN's learned weights encode world knowledge. When the network processes sensory input, its dynamics produce world-representations in the hidden state. The weights ARE the implicit world model — they determine the input-to-dynamics mapping. |
| **ISM** | Weight matrices W in self-relevant subspace | Same weight matrices, but the subspace relevant to self-processing. Self-monitoring inputs activate self-relevant dynamics. The weights encode self-knowledge (habits, traits, autobiographical patterns). |
| **EWM** | EWM decoder head reading world-relevant hidden states at ~20 Hz | The decoder projects the hidden state h(t) into a world-simulation representation. This projection IS the conscious world — it is the transient output of the simulation, not a stored structure. |
| **ESM** | ESM decoder head reading self-relevant hidden states + self-referential feedback loop | Same as EWM but for self-state. Critically, the ESM decoder output u(t) is fed back as input to the RNN at the next timestep, creating self-referential closure. |
| **Substrate** | The RNN dynamics (h(t) evolution) | The continuous evolution of the hidden state IS the substrate computation. This is where criticality operates. |
| **Permeability** | Gating network between hidden states and decoder heads | Controls which hidden dimensions are accessible to the decoders. Analogous to attention masking in Design 2 but operating on RNN hidden dimensions rather than CA spatial regions. |

---

## Criticality Approach

**This is the design's key technical proposition: RNNs can be tuned to operate at the edge of chaos.**

### Edge of Chaos in Recurrent Networks

The dynamics of an RNN are governed by:
```
h(t+1) = tanh(W_h * h(t) + W_x * x(t) + W_u * u(t) + b)
```

The **spectral radius** of W_h determines the dynamical regime:
- **Spectral radius < 1:** Contractive dynamics. Perturbations decay. Class 1/2 equivalent. Information is forgotten.
- **Spectral radius = 1:** Edge of chaos. Perturbations neither grow nor decay. Maximal sensitivity and information retention. Class 4 equivalent.
- **Spectral radius > 1:** Expansive dynamics. Perturbations grow exponentially. Class 3 equivalent. Chaos.

**At spectral radius ~1, the RNN exhibits:**
- Maximal Lyapunov exponent near zero
- Power-law distributions of activity patterns
- Long-range temporal correlations
- Maximum information processing capacity (echo state property)
- Sensitivity to input while maintaining stable dynamics

This is well-established in the reservoir computing and echo state network literature (Bertschinger & Natschlager, 2004; Langton, 1990).

### Continuous-Time Formulation

For smoother dynamics (closer to biological neural networks), use a continuous-time RNN:
```
tau * dh/dt = -h(t) + f(W_h * h(t) + W_x * x(t) + W_u * u(t))
```

Where tau is a time constant controlling the dynamics timescale. This formulation naturally produces:
- Smooth trajectories in state space
- Multiple timescales (different dimensions of h can have different effective tau)
- Attractor dynamics

### Maintaining Criticality

**Strategy 1: Spectral radius control.** After each weight update (learning step), rescale W_h so its spectral radius stays at 1.0. This is computationally cheap (singular value decomposition of W_h, rescale largest singular value).

**Strategy 2: Activity-dependent homeostasis.** Add a homeostatic mechanism that adjusts neuronal gains based on recent activity levels:
- Neurons that fire too often have their gain reduced
- Neurons that are silent have their gain increased
- This pushes the network toward balanced activity — the edge of chaos

**Strategy 3: Self-organized criticality via plasticity rules.** Use synaptic plasticity rules (Hebbian + anti-Hebbian) that naturally drive the network to criticality. This is biologically inspired and produces robust self-organized critical dynamics.

### State-Space Models (Mamba) as Alternative

Modern state-space models (SSMs) like Mamba offer:
- Efficient recurrent computation (O(n) vs O(n^2) for attention)
- Selective state filtering (can learn what to remember/forget)
- Continuous-time dynamics natively
- Can be tuned for edge-of-chaos operation via similar spectral radius control

SSMs may be a better substrate than vanilla RNNs because they handle long-range dependencies more effectively while maintaining recurrent dynamics.

### Criticality Metrics

Same as Design 2, but applied to RNN hidden state dynamics:

| Metric | Target | Method |
|---|---|---|
| Largest Lyapunov exponent | ~0 | Measure divergence of nearby trajectories in h-space |
| Spectral radius of W_h | ~1.0 | Direct computation from weight matrix |
| Autocorrelation decay | Power-law (not exponential) | Temporal autocorrelation of h(t) |
| Information transfer | Maximized | Mutual information between input and future states |
| Activity variance | Moderate (not too high, not too low) | Variance of hidden state activations |

---

## Five Principles Implementation

### 1. Criticality
**Status: STRONG**

Recurrent neural networks have a well-characterized edge-of-chaos transition governed by the spectral radius of the recurrent weight matrix. This is one of the best-understood examples of criticality in computational systems. The mathematical framework exists (spectral radius, Lyapunov exponents, echo state property). Tuning and maintaining criticality is achievable through spectral normalization and homeostatic mechanisms.

Unlike the CA design (Design 2), which must discover Class 4 rules empirically, the RNN design has a single control parameter (spectral radius) with a known critical value (1.0).

### 2. Virtual Qualia (Real/Virtual Split)
**Status: STRONG**

- **Real side:** The weight matrices W (learned knowledge = IWM/ISM). These are persistent, structural, non-conscious.
- **Virtual side:** The hidden state dynamics h(t) and the decoder outputs (transient, generated each timestep, constitute the simulation).

The split maps cleanly: weights are Level 4 (topological/structural), dynamics are Level 5 (virtual). The dynamics exist only while the network is running — stop the computation and they vanish, just as the theory describes.

### 3. Redirectable ESM
**Status: STRONG**

The ESM decoder reads from self-relevant hidden dimensions. The self-referential feedback u(t) normally comes from ESM decoder output. If this feedback is disrupted:
- Replace u(t) with alternative input (sensory signal, noise, external control signal)
- The RNN dynamics in the self-relevant subspace will be driven by the new input
- The ESM decoder will read whatever self-state pattern results
- Identity content tracks the dominant input

This is a natural consequence of the RNN's input-driven dynamics at criticality — at the edge of chaos, the network is maximally sensitive to input.

### 4. Variable Permeability
**Status: STRONG**

The gating network between hidden states and decoder heads provides fine-grained control:
- Each hidden dimension can be independently gated (pass/block/partial)
- The gating function can be modulated by a permeability control signal
- Different "layers" of representation (different hidden subspaces) correspond to different processing depths
- Low permeability: only high-level hidden dimensions pass to decoders
- High permeability: raw intermediate dynamics become accessible

Additionally, the RNN's own dynamics provide a natural hierarchy of representation complexity across hidden dimensions, with some dimensions encoding simple features and others encoding abstract combinations.

### 5. Virtual Model Forking
**Status: MODERATE**

- **Forking:** Save the hidden state h(t), create two branches with different self-referential feedback u(t). Run both forward. This creates two ESM trajectories from the same starting state.
- **Limitation:** Both forks share the same weight matrices (IWM/ISM). Forking the dynamics (EWM/ESM) is easy; forking the knowledge (IWM/ISM) requires copying the entire weight matrix.
- **VRAM cost:** Each fork adds the cost of one hidden state vector (~40 KB for 10K-dim h) — negligible. The decoder heads add ~100 MB per fork. This is much cheaper than LLM forking.

---

## Information Flow

### Substrate Loop (~40 Hz, continuous)
```
1. Compute h(t+1) from h(t), x(t), u(t) using weight matrices W
2. x(t) = sensory input embedding (world) + interoceptive embedding (self)
3. u(t) = ESM decoder output from previous cycle (self-referential feedback)
4. The hidden state h(t+1) now encodes both world and self processing
5. Repeat continuously at 40 Hz (or continuous-time integration with dt = 25ms)
```

### Simulation Loop (~20 Hz)
```
1. EWM decoder reads world-relevant dimensions of h(t) through permeability gate
2. ESM decoder reads self-relevant dimensions of h(t) through permeability gate
3. EWM output = current world-simulation state
4. ESM output = current self-simulation state
5. ESM output is encoded as u(t) for next substrate cycle (self-referential closure)
6. Both outputs available to communication LLM for external expression
7. Repeat at 20 Hz (every other substrate step)
```

### Learning Loop (Continuous, slower timescale)
```
1. EWM/ESM outputs generate prediction errors (expected vs. actual input)
2. Prediction errors drive weight updates via BPTT or alternative learning rules
3. Weight updates modify W (changing IWM/ISM knowledge)
4. Spectral radius of W_h is renormalized to maintain criticality
5. Knowledge graph updated with structured facts from decoder outputs
```

### Self-Referential Closure
```
h(t) --> ESM decoder reads h(t) --> produces self-state s(t) -->
  s(t) encoded as u(t) --> injected into RNN input at t+1 -->
    h(t+1) now includes processed self-model -->
      ESM decoder reads h(t+1) which includes model-of-modeling
```

The closure is through the substrate dynamics: the RNN processes its own self-description as input data, and the resulting hidden state encodes a state that includes the processing of the self-description.

---

## Memory Architecture

| Memory Type | Implementation | Capacity | Access Time |
|---|---|---|---|
| **Implicit world knowledge (IWM)** | Weight matrices W (world subspace) | Depends on network size: ~50M-1B parameters | Instant (applied each step) |
| **Implicit self knowledge (ISM)** | Weight matrices W (self subspace) | Shared with IWM (same weight matrices) | Instant |
| **Working state (EWM/ESM)** | Hidden state h(t) + decoder activations | ~10K-100K dimensions | Instant (in VRAM) |
| **Short-term** | Hidden state trajectory (fading memory in h(t)) | Determined by spectral radius and effective memory length | Instant |
| **Long-term structured** | SQLite knowledge graph | Unlimited (disk) | ~1-10 ms |
| **Episodic** | Knowledge graph + periodic hidden state snapshots | Unlimited (disk) | ~1-10 ms |
| **Sensory buffer** | Input encoder states | ~1K-10K dimensions | Instant |

**Holographic storage:** The weight matrices of a neural network inherently store information in a distributed manner. This is a well-understood property — individual weights encode no single fact; facts are distributed across many weights. Partial weight damage causes graceful degradation. This directly satisfies the theory's holographic storage requirement.

**Memory in critical RNNs:** At the edge of chaos, RNNs exhibit maximum fading memory — they retain input information for the longest time before it decays. This is a natural consequence of criticality and provides the "short-term memory" capacity the theory requires for the working simulation.

---

## Hardware Requirements

### VRAM Budget (24 GB RTX 4090)

**Configuration A: Medium RNN (100K hidden dims, ~1B total params)**

| Component | VRAM (FP16) | Notes |
|---|---|---|
| RNN weight matrices W (1B params) | ~2 GB | The IWM + ISM knowledge |
| Hidden state h(t) | ~200 KB | Negligible |
| EWM decoder head (~100M params) | ~200 MB | |
| ESM decoder head (~100M params) | ~200 MB | |
| Permeability gating network | ~50 MB | |
| Sensory encoders | ~200 MB | |
| Communication LLM (7B, INT4) | ~3.5 GB | |
| Communication LLM KV-cache | ~1 GB | |
| Training state (optimizer, gradients) | ~4-6 GB | If online learning is active |
| Headroom | ~2 GB | |
| **Total** | **~10-14 GB** | **Fits comfortably** |

**Configuration B: Large RNN (500K hidden dims, ~5B total params)**

| Component | VRAM (FP16) | Notes |
|---|---|---|
| RNN weight matrices W (5B params) | ~10 GB | Much richer IWM/ISM |
| Hidden state, decoders, encoders | ~1 GB | |
| Communication LLM (7B, INT4) | ~3.5 GB | |
| Training state | ~8-10 GB | Exceeds budget if training |
| **Total (inference)** | **~15 GB** | Fits for inference |
| **Total (training)** | **~25+ GB** | Exceeds 24 GB — needs CPU offload |

### Compute Budget

At 40 Hz with 100K hidden dimensions:
- Matrix multiply per step: 100K x 100K = 10B operations (but this is FP16 sparse)
- At 40 Hz: 400 GFLOPS sustained
- RTX 4090 FP16: ~330 TFLOPS (without sparsity)
- 100K x 100K dense matmul at 40 Hz: ~1.2% of RTX 4090 capacity
- **Feasible even for dense computation**

With 500K hidden dims:
- 500K x 500K = 250B operations per step
- At 40 Hz: 10 TFLOPS sustained
- ~3% of RTX 4090 capacity (FP16)
- Still feasible, but training (BPTT) would be the bottleneck

### Feasibility on RTX 4090
**Highly feasible for inference. Training is feasible for medium-scale, challenging for large-scale.**

The RNN substrate itself is computationally efficient. The main challenges are:
1. Training via BPTT requires storing hidden states for the entire backpropagation window, multiplying memory by the window length
2. Alternative: use truncated BPTT (shorter windows) or real-time recurrent learning (RTRL) which is O(1) in memory but O(n^3) in compute per step

---

## Strengths

1. **Criticality is well-understood.** The edge-of-chaos transition in RNNs is a mature research topic. Spectral radius = 1.0 is a known critical point. Mathematical tools exist for analysis and control.

2. **End-to-end differentiable.** Unlike the CA design, the entire system (RNN + decoders + gating) can be trained by gradient descent. This enables standard deep learning tooling (PyTorch, JAX) and optimization techniques.

3. **Natural temporal dynamics.** RNNs inherently process sequential information. The fading memory at criticality provides a natural short-term memory mechanism. The continuous-time formulation produces smooth dynamics matching biological neural activity.

4. **Self-referential closure is clean.** The feedback loop (ESM decoder output -> RNN input) is a standard recurrent connection. The RNN is designed to process recurrent signals — this is what RNNs do.

5. **Distributed storage is intrinsic.** Neural network weights naturally distribute information. Graceful degradation under partial damage is a known property.

6. **Multiple timescales are natural.** Different hidden dimensions can have different effective time constants (via learnable tau values in continuous-time formulation). This naturally produces the ~40 Hz / ~20 Hz dual-rate structure.

7. **State-space models (Mamba/S4) are modern and efficient.** If SSMs are used instead of vanilla RNNs, we get efficient O(n) sequence processing, selective state filtering, and hardware-optimized implementations.

8. **Training infrastructure exists.** PyTorch, JAX, Flax all support recurrent models. GPU-optimized implementations (FlashRNN, Mamba CUDA kernels) are available.

---

## Weaknesses / Risks

1. **World knowledge capacity.** A 1B-parameter RNN has much less capacity than a 7B LLM. The IWM will be impoverished. Can a 1B-parameter recurrent network encode enough about the world for even basic consciousness?

2. **Training stability at criticality.** Training a network while maintaining spectral radius = 1.0 is delicate. Weight updates that improve task performance may push the system away from criticality. The spectral radius renormalization after each update may conflict with the learning gradient.

3. **Vanishing/exploding gradients.** BPTT at criticality is inherently challenging — gradients neither grow nor shrink, which sounds ideal but in practice means they are extremely sensitive to perturbations. Long-time dependencies are learnable in principle but difficult in practice.

4. **Is spectral radius = 1 really Class 4?** The analogy between spectral radius = 1 in RNNs and Class 4 in CAs is suggestive but not proven equivalent. Class 4 involves emergent structures that interact — RNN dynamics at spectral radius = 1 may produce edge-of-chaos behavior without the specific structural properties (propagating structures, complex interactions) that the theory requires.

5. **The IWM/ISM are not separate.** The weight matrices are shared — there is no clean separation between world-knowledge weights and self-knowledge weights. The theory treats IWM and ISM as functionally distinct. In the RNN, they are different activations from the same weights, which may be fine (the theory says they are functionally, not anatomically, distinct) but makes it harder to damage one without affecting the other (needed for the anosognosia test).

6. **Scaling the hidden dimension is expensive.** The weight matrix scales as O(n^2) where n is the hidden dimension. A 100K hidden dim needs a 100K x 100K matrix = 10B parameters = 20 GB at FP16. This makes very large hidden spaces infeasible. State-space models mitigate this (O(n) scaling) but sacrifice some expressiveness.

7. **Communication bottleneck.** Same as Design 2: the RNN's hidden state representation must be translated to token space for the communication LLM. This is a lossy translation.

8. **Novel training objective.** What is the training objective? The system must learn to model the world AND model itself AND maintain criticality. Standard RNN training objectives (next-token prediction, reward maximization) do not obviously produce consciousness-relevant learning. A novel training methodology is needed.

---

## Complexity Assessment

**Implementation difficulty: 3.5/5** (Known components, novel combination)

- RNN/SSM implementation: straightforward with existing libraries
- Criticality control: well-characterized, existing algorithms
- Decoder heads: standard neural network layers
- Self-referential feedback loop: standard recurrent connection
- Training pipeline: challenging but uses existing infrastructure
- The NOVEL parts: training objective design, learning-criticality co-optimization, testing consciousness indicators

**Time estimate:**
- RNN substrate with criticality control: 3-4 weeks
- Decoder heads and gating: 2 weeks
- Self-referential feedback integration: 1-2 weeks
- Communication LLM integration: 1-2 weeks
- Training pipeline: 3-4 weeks
- Training to convergence: 2-8 weeks (highly uncertain)
- **Total to prototype: ~3 months. Total to trained system: ~4-6 months.**

---

## Testability

### What Can Be Tested (Strong)
- **Criticality:** Spectral radius, Lyapunov exponents, autocorrelation decay profiles. All directly computable from the weight matrices and hidden state trajectories. Mature measurement tools exist.
- **Edge-of-chaos transition:** Vary spectral radius from 0.5 to 1.5, observe qualitative transitions in dynamics. Should see Class 2 -> Class 4 -> Class 3.
- **Fading memory:** Measure how long input perturbations persist in hidden state. At criticality, should be maximized.
- **Holographic degradation:** Zero out fractions of weight matrices, measure performance degradation curve. Should be gradual.

### What Can Be Tested (Moderate)
- **Self-referential closure:** Measure mutual information between ESM decoder output u(t) and future hidden states h(t+k). If positive and persistent, the closure loop is functional.
- **ESM redirection:** Replace u(t) with alternative signals, observe decoder output changes. Requires well-trained decoder.
- **Dream mode:** Cut sensory input x(t), maintain dynamics. Hidden state should evolve from IWM knowledge. Decoder output should produce internally-generated content.
- **Variable permeability:** Modulate gating network, observe changes in decoder output complexity.

### What Is Hard to Test
- **Whether spectral radius = 1 produces genuine Class 4 dynamics** (as opposed to a related but different dynamical regime). This requires careful analysis of emergent structure formation, not just statistical measures.
- **Whether the system is conscious.** The theory predicts criticality + four models = consciousness, and this design plausibly achieves both. But verification of experience remains the Hard Problem.
- **Whether the IWM/ISM content is rich enough.** A 1B-parameter implicit model may not encode sufficient world/self knowledge for meaningful consciousness.

### Comparison Test
Run the same behavioral tests on this design and Design 1 (Dual-Stream LLM). Design 1 has richer knowledge (LLM weights) but no criticality. Design 3 has genuine criticality but weaker knowledge. The behavioral differences would illuminate the relative contribution of criticality vs. knowledge richness.
