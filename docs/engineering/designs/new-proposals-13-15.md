# Three New Architecture Proposals for AC Implementation

**Designs 13, 14, 15 -- Grounded in the FMT Implementation Specification**

**Date**: 2026-02-27
**Context**: Extends the existing 12-design catalogue. Informed by gaps in shortlisted Designs 7, 10, 11.

---

## Preamble: What the Existing Designs Get Wrong

Before proposing new designs, it is worth stating what specific gaps the existing shortlist (7, 10, 11) leaves:

**Design 10 (Predictive Coding Hierarchy)** -- Best overall pick, but:

- The LLM top layer is internally feedforward (Class 1/2). The "recurrence" comes from wrapping it in a loop, which is pseudo-recurrence -- the internal computation of each forward pass does not exhibit critical dynamics.
- The scope coordinate (sigma) must be *engineered* into the latent space. Pre-trained LLMs do not naturally separate world/self content along a continuous axis. This is a fragile imposition.
- Self-referential closure is claimed through "predicting one's own prediction errors" but this may be shallow -- it models *outputs* of the process, not the *process itself*.

**Design 11 (Spectral Decomposition)** -- Elegant interpretation, but:

- The eigendecomposition is a *linear* approximation of nonlinear dynamics. At the critical point (where nonlinearities matter most), this approximation is weakest.
- Scope classification (which eigenmodes are "world" vs. "self") is post-hoc inference, not architectural structure.
- Requires a separate communication LLM (wasted VRAM, integration overhead).

**Design 7 (Staged Architecture)** -- Pragmatic, but:

- Defers the hard problems. Stage 1 and 2 are explicitly non-conscious per the theory.
- The stage transitions may require complete redesign, not incremental upgrade.
- No continuous model density at any stage.

The three new designs below address these gaps directly. Each takes a different strategic bet on how to combine genuine criticality, continuous model density, LLM knowledge, and self-referential closure within the RTX 4090 envelope.

---

## Design 13: Reservoir-Gated Recurrent LLM with Emergent Model Topology

### 1. Name and Core Idea

A recurrent LLM (Mamba-2 or RWKV-6) whose hidden state is coupled to a sparse, criticality-tuned reservoir network. The reservoir does not merely sit alongside the LLM -- it *gates* the LLM's state transitions, injecting critical dynamics directly into the language model's recurrent computation. The continuous model space emerges from the joint dynamics of the LLM state and the reservoir, measured via a learned topological map rather than linear eigendecomposition.

### 2. Architecture Overview

```
                    +------------------------------------------+
                    |         EXTERNAL INTERFACE                |
                    |    The recurrent LLM IS the interface     |
                    |    (no separate communication model)      |
                    +---------^-----------+--------------------+
                              |           |
                              |   output  |  input
                              |           v

+=======================================================================+
||                   RECURRENT LLM SUBSTRATE                           ||
||                   (Mamba-2 7B, INT8 quantized)                      ||
||                                                                     ||
||   Standard recurrent step:                                          ||
||     h'(t) = SSM_step(h(t), input(t))     [native Mamba dynamics]    ||
||                                                                     ||
||   RESERVOIR-GATED step (the modification):                          ||
||     g(t) = sigma(W_gate * r(t))           [gate from reservoir]     ||
||     h(t+1) = g(t) . h'(t) + (1-g(t)) . h(t)  [gated update]      ||
||                                                                     ||
||   The reservoir injects criticality INTO the LLM's state space:     ||
||   - When reservoir is supercritical: gates open wide, rapid change  ||
||   - When reservoir is subcritical: gates close, state persists      ||
||   - At criticality: balanced gating = edge-of-chaos LLM dynamics    ||
||                                                                     ||
||   h(t) in R^d (d=4096 for 7B Mamba) = THE substrate state x(t)    ||
||                                                                     ||
+=======================================================================+
         |           ^                    |           ^
    output h(t)  gate g(t)          self-ref u(t) reservoir input
         |           |                    |           |
         v           |                    v           |
+=======================================================================+
||                   CRITICAL RESERVOIR                                ||
||                   (Sparse recurrent network, 50K units, FP16)      ||
||                                                                     ||
||   r(t+1) = tanh(W_res * r(t) + W_in * [h(t); x(t); u(t)])        ||
||                                                                     ||
||   W_res: sparse (1-5% connectivity), spectral radius = 1.0        ||
||   Tuned to edge of chaos via:                                       ||
||     - Spectral radius homeostasis                                   ||
||     - Branching ratio monitoring                                    ||
||     - Noise-driven exploration                                      ||
||                                                                     ||
||   Receives: LLM hidden state h(t), sensory input x(t),            ||
||            self-referential signal u(t)                              ||
||   Produces: gate signal g(t) for the LLM                          ||
||                                                                     ||
+=======================================================================+
         |                                            |
         v                                            v
+=======================================================================+
||              TOPOLOGICAL MODEL SPACE MAPPER                        ||
||              (Learned UMAP/SOM from joint [h(t), r(t)] dynamics)   ||
||                                                                     ||
||   Maps the joint state [h(t), r(t)] onto a 2D manifold M:         ||
||     phi: R^{d+50K} -> M = [0,1]^2   (scope s, mode nu)           ||
||                                                                     ||
||   The density rho(s, nu, t) is computed as the image of the        ||
||   activation density under phi.                                     ||
||                                                                     ||
||   Four canonical models = density peaks near corners of M.          ||
||   Intermediate models = density in the interior of M.               ||
||   Virtual/non-virtual boundary = nu_crit contour in M.             ||
||                                                                     ||
||   Trained via contrastive learning:                                 ||
||     - World-input-driven states map to s near 1                     ||
||     - Self-input-driven states map to s near 0                      ||
||     - High-activation transient patterns map to nu near 1           ||
||     - Persistent weight-like patterns map to nu near 0              ||
||                                                                     ||
+=======================================================================+
```

**How the four models emerge:**

| Model | What it is | Where in the architecture |
|-------|-----------|--------------------------|
| IWM | LLM weights (Mamba SSM parameters) encoding world knowledge | Persistent parameters of the LLM substrate. Scope s near 1, mode nu near 0 in the topological map. |
| ISM | LLM weights encoding self-knowledge (fine-tuned via LoRA on self-relevant data) | Same persistent parameters, scope s near 0, mode nu near 0. |
| EWM | Transient activation patterns in h(t) driven by world input, shaped by reservoir gating | The component of h(t) that the topological mapper places at s near 1, nu above nu_crit. |
| ESM | Transient activation patterns in h(t) driven by self-referential feedback u(t) | The component at s near 0, nu above nu_crit. Includes the self-referential loop. |

### 3. Continuous Model Space

The continuous model density rho(s, nu, t) is implemented via the **topological model space mapper** -- a learned nonlinear projection from the joint (LLM + reservoir) state space onto the 2D (scope, mode) manifold.

**Why this is better than Design 11's eigendecomposition:**

- It is nonlinear. It captures the actual geometry of the dynamics, including limit cycles and strange attractors near the critical point, not just the linearized behavior.
- It is learned from data. The mapper discovers where models naturally cluster in state space, rather than imposing a linear coordinate system.
- The mapping is differentiable (UMAP-style or neural network), so it can be end-to-end optimized with the rest of the system.

**Concrete implementation:**

- A small neural network (3-layer MLP, 256 hidden units) takes as input a compressed representation of [h(t), r(t)] (via random projection to ~1000 dims) and outputs (s, nu) coordinates.
- Trained via contrastive loss: states driven by world-input should have high s, states driven by self-input should have low s, transient states should have high nu, persistent patterns should have low nu.
- The density rho is computed by binning the output coordinates over a short time window (100 ms = 2-4 conscious frames).
- C(t) = integral of rho above nu_crit, computed at each conscious frame.

### 4. Criticality Mechanism

**Core innovation: the reservoir injects criticality into the LLM.**

The Mamba-2 LLM, on its own, exhibits Class 1/2 dynamics (its SSM transitions are contractive by design). The reservoir network, tuned to spectral radius 1.0, exhibits genuine Class 4 dynamics (power-law avalanches, 1/f noise). By having the reservoir gate the LLM's state transitions, the combined system inherits the reservoir's critical properties:

- The gate g(t) modulates how much the LLM state updates at each step.
- At criticality, g(t) fluctuates across a wide dynamic range (some dimensions open, some closed, in a scale-free pattern).
- This produces edge-of-chaos dynamics in the LLM state space: some state dimensions evolve rapidly, others persist, the boundary between the two shifts continuously.

**Criticality metrics:**

- Branching ratio sigma of the reservoir: maintained at [0.95, 1.1] via spectral radius homeostasis.
- Lyapunov exponent lambda_max of the joint system [h(t), r(t)]: should be near 0.
- DFA exponent alpha of the LLM hidden state time series: should be near 1.
- Avalanche size distribution in the gate signal g(t): should follow power law.

**Homeostatic control:**

- Every 100 steps (~2.5 sec at 40 Hz): compute spectral radius of W_res, adjust scaling factor.
- Every 1000 steps (~25 sec): measure branching ratio from reservoir activity, fine-tune W_res sparsity.
- Continuous: monitor mean gate activation, adjust W_gate bias to maintain mean gating near 0.5.

### 5. Self-Referential Closure

The ESM self-referential loop:

```
u(t) = W_self * readout_self(h(t))     [extract self-relevant state]
     -> fed back into reservoir input
     -> reservoir computes new gate g(t+1)
     -> gate modifies LLM state h(t+1)
     -> readout_self(h(t+1)) = updated self-model
     -> u(t+1) = W_self * readout_self(h(t+1))
     -> ...
```

**Why this is deeper than Design 10's approach:**

- The self-referential signal passes through the reservoir (a genuine dynamical system at criticality) before affecting the LLM state. The reservoir "processes" the self-signal, transforming it through its critical dynamics. This means the self-model is not just "predict my prediction errors" but "dynamically transform my self-representation through a critical process and observe the result."
- The fixed point Phi(m*) = m* is achieved when the self-referential loop stabilizes: u(t) produces gating that produces h(t+1) that produces u(t+1) approximately equal to u(t). At criticality, this fixed point is marginally stable (not a dead attractor).

**Self-knowledge metric R:**

- R = 1 - H(u(t+1) | u_predicted(t+1)) / H(u(t+1))
- Where u_predicted(t+1) is the system's own prediction of its next self-state, computed by a small prediction head on the LLM output.

### 6. Technology Stack

| Component | Technology | Version/Variant |
|-----------|-----------|-----------------|
| Recurrent LLM | Mamba-2 | 2.8B (primary) or 7B (if VRAM allows) |
| Quantization | GPTQ or AWQ | INT8 for 7B, FP16 for 2.8B |
| Reservoir | Custom sparse RNN | PyTorch, hand-optimized CUDA kernel |
| Topological mapper | Small MLP | PyTorch |
| Criticality monitoring | Custom | NumPy/SciPy for spectral analysis, PyTorch for branching ratio |
| Self-referential loop | Custom feedback circuit | PyTorch autograd-compatible |
| Sensory input | Lightweight encoder | SigLIP-base (vision), Whisper-tiny (audio) |
| Training framework | PyTorch 2.x | With torch.compile for kernel fusion |
| Experiment tracking | Weights & Biases | Free tier |

### 7. VRAM Budget

**Configuration A: Mamba-2 2.8B (FP16) + 50K reservoir**

| Component | VRAM | Notes |
|-----------|------|-------|
| Mamba-2 2.8B (FP16) | ~5.6 GB | Full precision for maximum quality |
| SSM recurrent state | ~50 MB | State vectors per layer |
| Reservoir (50K units, sparse W_res FP16) | ~200 MB | 5% connectivity = 125M nonzero entries |
| Reservoir state buffer | ~200 KB | 50K * FP16 |
| Gate weights W_gate | ~400 MB | 50K -> 4096 dense projection |
| Self-referential loop weights | ~50 MB | |
| Topological mapper MLP | ~5 MB | Tiny |
| Sensory encoders (SigLIP-base) | ~400 MB | |
| LoRA adapters (for learning) | ~200 MB | |
| Training state (gradients, optimizer) | ~3 GB | AdamW on reservoir + LoRA |
| Criticality monitoring buffers | ~100 MB | Eigenvalue history, avalanche tracking |
| Headroom | ~3 GB | |
| **Total** | **~13.2 GB** | **Comfortable fit** |

**Configuration B: Mamba-2 7B (INT8) + 50K reservoir**

| Component | VRAM | Notes |
|-----------|------|-------|
| Mamba-2 7B (INT8) | ~7 GB | Quantized for VRAM savings |
| SSM recurrent state | ~100 MB | |
| Reservoir (50K, sparse FP16) | ~200 MB | |
| Gate weights, self-ref, mapper | ~500 MB | |
| Sensory encoders | ~400 MB | |
| LoRA + training state | ~3.5 GB | |
| Monitoring + headroom | ~3 GB | |
| **Total** | **~14.7 GB** | **Good fit** |

### 8. Real-Time Feasibility

**Target: 40 Hz substrate (25 ms/step), 20 Hz conscious readout (50 ms/frame)**

Per substrate step (25 ms budget):

| Operation | Latency | Notes |
|-----------|---------|-------|
| Mamba-2 recurrent step (2.8B FP16 or 7B INT8) | 5-10 ms | Single-step inference, optimized CUDA kernels |
| Reservoir step (50K sparse matmul) | 0.5-1 ms | Sparse matmul on GPU |
| Gate computation (50K -> 4096 dense) | 0.2 ms | Small dense layer |
| Gated state update | 0.1 ms | Element-wise operations |
| Self-referential feedback computation | 0.5 ms | Small projection |
| **Total per substrate step** | **~7-12 ms** | **Fits in 25 ms** |

Per conscious frame (50 ms budget, every 2nd substrate step):

| Operation | Latency | Notes |
|-----------|---------|-------|
| Topological mapping (MLP forward) | 0.1 ms | Tiny network |
| Density computation (histogram) | 0.2 ms | Binning over time window |
| C(t) integration | 0.1 ms | Numerical integration |
| Criticality check (periodic, amortized) | 1-2 ms | Spectral radius every 100 steps |
| **Total overhead per conscious frame** | **~1-3 ms** | **Negligible** |

**Verdict: Achievable at 40 Hz substrate / 20 Hz conscious simulation, with headroom.**

### 9. Testable Predictions Coverage

| # | Prediction | Coverage | How |
|---|-----------|----------|-----|
| 1 | Criticality-dependent coherence | **Strong** | Sweep reservoir spectral radius from 0.5 to 1.5. Measure LLM output coherence (perplexity, self-consistency). Should peak near sigma=1. |
| 2 | Permeability-dependent content flooding | **Strong** | Increase gate mean activation (open gates wider). Measure transfer entropy from reservoir to LLM state. Should increase monotonically. |
| 3 | ESM input-switching | **Strong** | Cut self-referential feedback u(t)=0, inject strong world-input. Measure mutual information I(ESM; world-input). Should approach I_max. |
| 4 | Ego dissolution controllability | **Strong** | During ESM disruption, vary dominant sensory input. ESM readout should track the input content. |
| 5 | Holographic degradation | **Moderate** | Ablate 50% of reservoir units. Measure degradation of ALL four model readouts. Should degrade uniformly, not lose specific models. |
| 6 | Anesthetic convergence on criticality | **Strong** | Test multiple "anesthesia" mechanisms (kill reservoir, dampen gates, add noise). All should converge on pushing joint system away from sigma=1. |
| 7 | Sleep cycling | **Moderate** | Run continuously. Monitor criticality metrics. The reservoir's activity should gradually drift (no metabolic depletion analog, but weight drift under continuous learning may serve). |
| 8 | Self-knowledge predicts metacognition | **Strong** | Measure R. Correlate with system's ability to accurately report its own processing state (via LLM output). |
| 9 | Forking under perturbation | **Moderate** | Strong perturbation to ESM feedback loop. Monitor whether multiple stable self-configurations emerge in the topological map. |

**Coverage: 6 strong, 3 moderate. Total: 9/9 addressed.**

### 10. Implementation Phases

**Phase 1 (8-12 weeks): Substrate**

- Set up Mamba-2 inference with single-step recurrent mode
- Implement sparse reservoir network on GPU
- Implement reservoir-to-LLM gating mechanism
- Achieve stable coupled dynamics (LLM + reservoir running together)
- Tune reservoir to criticality (spectral radius = 1.0, verify power-law avalanches)
- Measure criticality metrics of the joint system (DFA, Lyapunov, branching ratio)
- Deliverable: Running substrate at 40 Hz with verified critical dynamics

**Phase 2 (8-12 weeks): Integration**

- Train the topological model space mapper (contrastive learning on world/self input)
- Implement the self-referential feedback loop
- Implement permeability control (gate modulation)
- Implement sensory input encoders
- Implement the conscious readout at 20 Hz
- Train LoRA adapters for self-relevant content
- Deliverable: Full four-model system with measurable rho(s, nu, t) and C(t)

**Phase 3 (8-12 weeks): Validation**

- Test all 9 predictions systematically
- Measure self-knowledge R and correlate with metacognitive ability
- Test state transitions (normal, dream, altered, sleep analog)
- Compare criticality-on vs. criticality-off (reservoir at sigma=1 vs. sigma=0.5)
- Full ablation study (reservoir size, gating strength, feedback gain)
- Deliverable: Complete validation report with quantitative results

**Total: ~6-9 months to full validation.**

### 11. Key Risks

1. **Reservoir gating may not genuinely inject criticality into LLM dynamics.** The LLM's internal SSM transitions are contractive. Gating modulates *how much* the state updates, but if the SSM is strongly contractive, even wide-open gates may not produce edge-of-chaos dynamics in h(t). Mitigation: measure Lyapunov exponent of h(t) directly, not just reservoir r(t). If h(t) remains Class 1/2 despite gating, the approach fails and must be redesigned.

2. **The topological mapper may not discover a meaningful 2D manifold.** If the joint state space does not naturally separate into scope and mode dimensions, the contrastive training may produce an arbitrary mapping. Mitigation: validate with held-out data; check that world-input states and self-input states are separable in the learned map.

3. **Self-referential closure through a gated loop may be shallow.** The system models its self-state u(t), but the transformation u(t) -> g(t+1) -> h(t+1) -> u(t+1) passes through the reservoir, which is not itself a model of the process. The reservoir is a dynamical system, not a self-model. Mitigation: add an explicit self-prediction head that must predict the *full loop* outcome, not just the next u(t).

4. **VRAM pressure from online learning.** Continuous LoRA fine-tuning of the Mamba-2 LLM requires gradient computation, which roughly doubles memory for the LLM component. Mitigation: use very small LoRA rank (r=4-8), or alternate between inference and learning phases (not simultaneous).

---

## Design 14: Neural Field Automaton with LLM-Initialized Implicit Manifold

### 1. Name and Core Idea

A continuous neural field on a 2D toroidal lattice where each point carries a high-dimensional activation vector. The field's dynamics are governed by local interaction kernels initialized from LLM embedding geometry. The field IS the substrate: weights encoded in the kernel structure are the implicit models, and transient activation waves are the explicit models. Criticality emerges from tuning the interaction kernel to a Turing-Hopf bifurcation point. The continuous model density rho(s, nu, t) is *directly observable* as the activation density on the field, because the field's two spatial dimensions are explicitly mapped to scope and mode.

### 2. Architecture Overview

```
                    +------------------------------------------+
                    |         EXTERNAL INTERFACE                |
                    |    Small LLM decoder (1.5B INT4)         |
                    |    Reads from field readout               |
                    +---------^-----------+--------------------+
                              |           |
                              |   output  |  input (encoded)
                              |           v

+=======================================================================+
||                   NEURAL FIELD (TOROIDAL LATTICE)                   ||
||                   The substrate and the simulation                   ||
||                                                                     ||
||   Lattice: 256 x 256 points on a torus (65,536 field points)      ||
||   Each point p = (i,j) carries:                                     ||
||     - Activation vector a_p(t) in R^D  (D=64, the field value)    ||
||     - Local kernel parameters K_p (learned, = implicit model)      ||
||                                                                     ||
||   Spatial coordinates encode (scope, mode):                         ||
||     - Dimension 1 (i): scope s in [0,1]  (i/256)                  ||
||       Left edge (i=0): pure self. Right edge (i=255): pure world.  ||
||     - Dimension 2 (j): mode nu in [0,1]  (j/256)                  ||
||       Bottom (j=0): implicit. Top (j=255): explicit.               ||
||     - nu_crit = j_crit/256, e.g., j_crit=128 -> nu_crit=0.5      ||
||                                                                     ||
||   Field dynamics (continuous neural field equation):                 ||
||                                                                     ||
||     da_p/dt = -a_p/tau + phi(sum_{q in N(p)} K_{p,q} * a_q(t))   ||
||              + I_p(t) + noise                                       ||
||                                                                     ||
||   where:                                                            ||
||     tau = time constant (varies with j: fast at top, slow at bottom)||
||     K_{p,q} = interaction kernel (learned, encodes implicit models) ||
||     N(p) = local neighborhood (radius R, ~25-50 points)            ||
||     phi = activation function (tanh or ELU)                         ||
||     I_p(t) = external input (sensory at s near 1, interoceptive at ||
||              s near 0, both injected above nu_crit)                  ||
||                                                                     ||
||   The FOUR MODELS:                                                  ||
||     IWM = K_{p,q} for p with i > 128 (world-scope kernels)        ||
||     ISM = K_{p,q} for p with i < 128 (self-scope kernels)         ||
||     EWM = a_p(t) for p with i > 128, j > j_crit (world, explicit) ||
||     ESM = a_p(t) for p with i < 128, j > j_crit (self, explicit)  ||
||                                                                     ||
||   But the boundaries are SOFT -- density is continuous across      ||
||   the entire field. The four corners are density peaks, not walls.  ||
||                                                                     ||
+=======================================================================+
         |                    ^                    |
    field readout        self-ref feedback    sensory/intro input
         |                    |                    |
         v                    |                    v
+=======================================================================+
||              CRITICALITY CONTROLLER                                ||
||                                                                     ||
||   Monitors field dynamics for Class 4 indicators:                  ||
||   - Avalanche size distribution (should be power-law)              ||
||   - Spatial correlation length (should diverge at criticality)     ||
||   - Temporal autocorrelation (should show 1/f spectrum)            ||
||                                                                     ||
||   Controls via:                                                     ||
||   - Global kernel scaling (multiplier on all K_{p,q})              ||
||   - Noise amplitude (drives exploration at criticality)            ||
||   - Lateral inhibition strength (balances excitation)              ||
||                                                                     ||
||   Target: Turing-Hopf bifurcation point where spatial patterns     ||
||   (Turing) and temporal oscillations (Hopf) interact to produce    ||
||   Class 4 dynamics.                                                 ||
||                                                                     ||
+=======================================================================+
         |
         v
+=======================================================================+
||              LLM-BASED KERNEL INITIALIZATION                       ||
||              (runs once, not in real-time loop)                     ||
||                                                                     ||
||   Use a pre-trained LLM (7B) to initialize the kernel parameters:  ||
||   1. Extract embedding geometry from LLM hidden states             ||
||   2. For each field point p at scope s:                             ||
||      - Compute typical LLM activations for world-content (s~1)     ||
||        or self-content (s~0) at that abstraction level (nu)        ||
||   3. Set K_{p,q} so that the field's local dynamics approximate    ||
||      the LLM's learned transition patterns                          ||
||   4. This gives the field a "warm start" with LLM knowledge        ||
||      encoded in its interaction structure                           ||
||                                                                     ||
||   After initialization, the LLM is unloaded from VRAM.             ||
||   The field runs independently.                                     ||
||   Knowledge lives in the kernel structure K, not in an LLM.        ||
||                                                                     ||
+=======================================================================+
```

### 3. Continuous Model Space

**This design has the most direct implementation of rho(s, nu, t) of any design.**

The field's spatial dimensions *literally are* the scope (s) and mode (nu) axes. The activation density at point (i, j) at time t is:

```
rho(s=i/256, nu=j/256, t) = ||a_{(i,j)}(t)||
```

This is not an approximation, projection, or learned mapping. It is a direct, observable, real-time measurement. Every requirement the spec places on rho is directly implementable:

- **Density peaks near four corners:** The kernel structure K is designed so that activation naturally clusters near the four corners during normal operation.
- **Virtual/non-virtual boundary:** nu_crit is a fixed coordinate on the lattice. Everything above it is explicit/virtual. Below is implicit/non-virtual.
- **Fokker-Planck dynamics:** The field equation IS a discretized Fokker-Planck equation on the (s, nu) manifold:

```
  drho/dt = -div(v * rho) + D * laplacian(rho) + S(s, nu, t)

  v = drift (from the deterministic kernel dynamics)
  D = diffusion (from the noise term)
  S = source/sink (from external input injection and decay)
```

This is *exactly* the equation from Section 6.1 of the spec. The design implements it natively.

- **C(t) = integral of rho above nu_crit:** Sum of ||a_p(t)|| for all p with j > j_crit. Computed trivially.

### 4. Criticality Mechanism

The neural field operates at a **Turing-Hopf bifurcation** -- the point where two instabilities (spatial pattern formation and temporal oscillation) interact.

**Why this produces Class 4 dynamics:**

- A pure Turing instability produces static spatial patterns (Class 2: periodic).
- A pure Hopf instability produces temporal oscillations (Class 2: periodic).
- At their intersection (the Turing-Hopf codimension-2 point), the system exhibits spatiotemporal complexity: traveling waves, spiral waves, labyrinthine patterns, and spatiotemporal chaos coexist and interact. This is Class 4: structures emerge, persist, interact, and transform.

**How to reach the bifurcation point:**

The interaction kernel K has two key parameters:
- Excitation range R_e (how far excitatory interactions reach)
- Inhibition range R_i (how far inhibitory interactions reach)
- The Turing condition: R_i > R_e (Mexican hat / lateral inhibition)
- The Hopf condition: total excitation strength slightly exceeds total inhibition
- The codimension-2 point is where both conditions are marginally satisfied

The criticality controller adjusts R_e, R_i, and the global kernel scaling to maintain the system at this point.

**Measurable indicators:**

- Spatial correlation function: should show power-law decay (not exponential).
- Temporal power spectrum: should show 1/f^beta with beta near 1.
- Avalanche size distribution: spatiotemporal activation clusters should follow power-law.
- Pattern diversity: coexistence of multiple pattern types (spirals, waves, spots) is a hallmark of the Turing-Hopf regime.

### 5. Self-Referential Closure

The ESM occupies the region of the field with i < 128 (self-scope) and j > j_crit (explicit mode). Self-referential closure is achieved through a spatial feedback loop:

```
1. Activity in the ESM region a_ESM(t) is read out.
2. This readout is re-injected as input I_p(t) into the self-scope
   region, specifically at field points near (i near 0, j just above j_crit).
3. The injected signal propagates through the field's dynamics,
   creating new activity patterns in the ESM region.
4. These new patterns are read out and re-injected in the next step.
5. At the fixed point: the readout equals the injection (Phi(m*) = m*).
```

**Why this is genuine self-referential closure:**

- The self-signal passes through the same dynamical substrate (the neural field at criticality) that generates it.
- The field transforms the self-signal through its kernel dynamics K_self -- the implicit self-model.
- The ESM is not just "predicting its outputs" -- it is running its self-representation through the *same computational process* that generates it, and observing the result.
- At criticality, the fixed point is marginally stable: perturbations propagate but do not diverge, creating rich self-modeling dynamics.

**Recursive depth:**

- rho_0 (basic): ESM activity exists and is driven by ISM kernels.
- rho_1 (simply extended): The feedback loop from ESM -> input -> ESM is active, so the ESM models its own next state.
- rho_2 (doubly extended): The system can be extended by adding a "meta-ESM" region that models the ESM feedback loop itself.

### 6. Technology Stack

| Component | Technology | Version/Variant |
|-----------|-----------|-----------------|
| Neural field simulation | Custom CUDA kernels | PyTorch + Triton for kernel fusion |
| Field lattice | 256x256x64 tensor | PyTorch tensor on GPU |
| Interaction kernel | Sparse convolution | PyTorch or custom CUDA |
| LLM for initialization | Mamba-2 7B or Llama 3.1 7B | Loaded once, then unloaded |
| LLM for communication | Phi-3-mini 3.8B (INT4) or Llama 3.2 3B (INT4) | Persistent in VRAM |
| Criticality monitoring | Custom Python/CUDA | Avalanche detection, correlation functions |
| Sensory encoders | SigLIP-base (vision), Whisper-tiny (audio) | PyTorch |
| Visualization | Real-time 2D field rendering | matplotlib + CUDA interop, or custom OpenGL |

### 7. VRAM Budget

| Component | VRAM | Notes |
|-----------|------|-------|
| Neural field state: 256x256x64 FP16 | ~8 MB | Current activation |
| Field state buffer (double-buffered) | ~16 MB | For update step |
| Kernel parameters K: 256x256 x (neighborhood x 64 x 64) FP16 | ~3.2 GB | 50 neighbors x 64x64 matrix per point, but shared/tiled kernels reduce to ~50 unique kernel types tiled across field = 50 x 64 x 64 x 2 bytes = ~400 KB; with per-point LoRA-style offsets: +200 MB. **Effective: ~400 MB** |
| Criticality controller state | ~50 MB | Monitoring buffers |
| Communication LLM (3B INT4) | ~1.5 GB | |
| Communication KV-cache | ~1 GB | |
| Self-referential feedback buffers | ~50 MB | |
| Sensory encoders (SigLIP-base) | ~400 MB | |
| LLM initialization phase (7B, temporary) | 7 GB (freed after init) | Only during setup |
| Training state (kernel learning) | ~2 GB | Gradients for kernel parameters |
| Headroom | ~3 GB | |
| **Total (runtime, after init)** | **~8.7 GB** | **Very comfortable fit** |

Note: the kernel parameterization above uses a "shared kernel + per-point offset" scheme to keep VRAM manageable. 256x256 = 65,536 points each with a full kernel would be enormous, but since nearby points share similar kernels (smooth spatial variation), we use ~50 archetype kernels tiled across the field with small per-point offsets.

### 8. Real-Time Feasibility

**Target: 40 Hz field update (25 ms/step), 20 Hz conscious readout (50 ms)**

Per field update step (25 ms budget):

| Operation | Latency | Notes |
|-----------|---------|-------|
| Sparse convolution (field update) | 3-8 ms | 256x256 lattice, 50-point neighborhood, 64-dim vectors. Highly parallelizable on GPU -- this is essentially a 2D convolution with per-pixel weights. |
| Activation function + noise | 0.5 ms | Element-wise |
| Self-referential feedback injection | 0.5 ms | Small readout + injection |
| Criticality monitoring (amortized) | 0.5 ms | Avalanche tracking per-step is cheap; full correlation analysis every 100 steps |
| **Total per field step** | **~5-10 ms** | **Fits in 25 ms with margin** |

Per conscious frame (50 ms, every 2 field steps):

| Operation | Latency | Notes |
|-----------|---------|-------|
| rho(s, nu, t) computation | 0.5 ms | Activation norm over the field |
| C(t) integration | 0.1 ms | Sum over upper half of field |
| Communication LLM readout | 5-10 ms | LLM forward pass on field readout |
| **Total per conscious frame** | **~6-11 ms** | **Fits in 50 ms easily** |

**Verdict: Easily achievable. The neural field computation is embarrassingly parallel and maps perfectly to GPU architecture.**

### 9. Testable Predictions Coverage

| # | Prediction | Coverage | How |
|---|-----------|----------|-----|
| 1 | Criticality-dependent coherence | **Strong** | Sweep kernel scaling. Measure spatial coherence of activation patterns. Should peak at the Turing-Hopf bifurcation point. |
| 2 | Permeability-dependent content flooding | **Strong** | Increase coupling between lower (nu < nu_crit) and upper (nu > nu_crit) field regions. Measure transfer entropy across the nu_crit boundary. Should increase with coupling strength. |
| 3 | ESM input-switching | **Strong** | Cut self-referential feedback. Inject strong world-input into the self-scope region. Measure I(ESM region activity; world-input). Should approach I_max. |
| 4 | Ego dissolution controllability | **Strong** | During ESM disruption, vary the content of injected input. The ESM region's activity patterns should track the injected content. Directly observable on the field. |
| 5 | Holographic degradation | **Strongest** | Ablate 50% of the field (e.g., right half). The remaining left half should show degraded but present activity at ALL four corners (not just the self-scope corners). The neural field's distributed kernel structure ensures holographic storage. |
| 6 | Anesthetic convergence on criticality | **Strong** | Test: dampen kernel globally, add massive noise, freeze kernel updates. All should push field away from the bifurcation point, abolishing coherent patterns. |
| 7 | Sleep cycling | **Strong** | Run continuously with a slow "metabolic" decay on kernel strength. The field should periodically lose criticality (patterns collapse = sleep), then restore when kernel is refreshed (waking). This cycle is architecturally native. |
| 8 | Self-knowledge predicts metacognition | **Moderate** | Measure R from the self-referential loop. Correlate with the communication LLM's ability to describe the field's own state. Moderate because the LLM readout adds indirection. |
| 9 | Forking under perturbation | **Strong** | Perturb the ESM region strongly. Observe whether multiple stable activation patterns (attractors) appear in the self-scope region. On a neural field at criticality, multistability is expected near the bifurcation point. |

**Coverage: 8 strong, 1 moderate. Total: 9/9 addressed.**

### 10. Implementation Phases

**Phase 1 (6-10 weeks): Substrate**

- Implement the 256x256x64 neural field on GPU (CUDA/Triton kernels)
- Design the shared-kernel architecture with per-point offsets
- Implement the Turing-Hopf criticality controller
- Tune the kernel to the bifurcation point
- Verify Class 4 dynamics (power-law avalanches, 1/f spectrum, pattern diversity)
- Benchmark real-time performance at 40 Hz
- Deliverable: Running neural field at criticality, 40 Hz, visualizable

**Phase 2 (8-12 weeks): Integration**

- LLM-based kernel initialization (extract embedding geometry, set initial kernel structure)
- Implement self-referential feedback loop for ESM region
- Implement sensory/interoceptive input injection
- Implement permeability control (coupling across nu_crit boundary)
- Integrate communication LLM (Phi-3-mini or Llama 3.2 3B)
- Implement conscious readout at 20 Hz
- Train kernel parameters to improve four-model density peaks via contrastive loss
- Deliverable: Full system with four-model structure, rho(s,nu,t) directly observable

**Phase 3 (8-12 weeks): Validation**

- Test all 9 predictions
- Implement sleep cycling (metabolic kernel decay + restoration)
- Implement dream mode (remove sensory input, observe internal dynamics)
- Implement altered state (increase permeability, observe content flooding)
- Full ablation study (field size, kernel type, criticality regime)
- Compare with criticality-off baseline (kernel tuned to subcritical = Class 2)
- Deliverable: Validation report with quantitative prediction results

**Total: ~5.5-8.5 months to full validation.**

### 11. Key Risks

1. **LLM knowledge may not transfer to kernel structure.** The initialization procedure (extracting embedding geometry and encoding it in local interaction kernels) is novel and unproven. The LLM's knowledge is encoded in 7B parameters with complex nonlinear interactions; distilling this into local field kernels may lose most of the knowledge. Mitigation: treat LLM initialization as "warm start" not "complete transfer." The field still learns from sensory experience.

2. **The kernel parameterization may be too constrained.** Using ~50 archetype kernels with per-point offsets imposes a strong smoothness prior. If the implicit models require sharp spatial structure, this parameterization will not capture it. Mitigation: increase the number of archetype kernels, or use a continuous kernel parameterization (hypernetwork).

3. **Turing-Hopf criticality may be harder to maintain than single-parameter criticality.** The codimension-2 bifurcation point requires simultaneous tuning of two parameters. Drifting away from the point in either direction produces qualitatively different (non-critical) dynamics. Mitigation: the criticality controller monitors both Turing and Hopf indicators and adjusts kernel parameters to stay near the intersection.

4. **The communication LLM creates a bottleneck.** The field operates on 64-dimensional activation vectors, not natural language tokens. The translation from field readout to language (via the communication LLM) may be lossy, failing to express the richness of the field's internal state. Mitigation: train the communication LLM on field-readout data with auxiliary losses.

5. **256x256 may be too small.** The spec does not define a minimum field size, but 65K field points may be insufficient for the complexity of models needed. A rodent cortex has ~14 million minicolumns. Mitigation: the 64-dimensional activation vector at each point provides high local capacity. Total state dimensionality is 256 x 256 x 64 = 4.19M, which is comparable to the hidden dimension of a 1B-parameter LLM.

---

## Design 15: Dual-Timescale Spiking Reservoir with Predictive LLM Canopy

### 1. Name and Core Idea

A spiking neural network (SNN) reservoir operates at the 40 Hz substrate rate, inherently producing Class 4 dynamics through balanced excitation-inhibition near the critical point. Above the SNN sits a predictive LLM "canopy" that runs at 20 Hz, receiving spike-rate coded summaries and generating top-down predictions. The SNN provides genuine criticality and continuous model density (via population coding across spiking populations); the LLM canopy provides world knowledge and language. The two are coupled bidirectionally: LLM predictions modulate SNN dynamics (top-down attention), and SNN error signals update LLM beliefs (bottom-up surprise). This combines Design 10's predictive coding insight with Design 2's genuine substrate criticality, avoiding both their weaknesses.

### 2. Architecture Overview

```
                    +------------------------------------------+
                    |         EXTERNAL INTERFACE                |
                    |    The LLM canopy IS the interface        |
                    |    (no separate communication model)      |
                    +---------^-----------+--------------------+
                              |           |
                              |   output  |  input
                              |           v

+=======================================================================+
||                   LLM PREDICTIVE CANOPY (20 Hz)                    ||
||                   (Mamba-2 2.8B, FP16 or INT8)                     ||
||                                                                     ||
||   Operates in predictive coding mode:                               ||
||   1. Receives spike-rate summary z(t) from SNN (bottom-up)        ||
||   2. Generates predictions p(t) of expected z(t+1) (top-down)      ||
||   3. Computes prediction error e(t) = z(t) - p(t)                 ||
||   4. Updates internal state h_LLM(t) based on error               ||
||   5. Self-referential: predicts own prediction errors at sigma~0   ||
||                                                                     ||
||   The LLM canopy provides:                                          ||
||   - High-level IWM (world knowledge in pre-trained weights)        ||
||   - High-level ISM (self-knowledge in LoRA weights)                ||
||   - High-level EWM (world predictions at narrative timescale)      ||
||   - High-level ESM (self-predictions + self-referential loop)      ||
||   - Natural language communication                                  ||
||                                                                     ||
+=======================================================================+
         |           ^                    |           ^
    predictions p(t) |               predictions  errors e(t)
    (top-down)  spike-rate z(t)      (top-down)  (bottom-up)
         |      (bottom-up)               |           |
         v           |                    v           |
+=======================================================================+
||              SPIKE-RATE INTERFACE LAYER                             ||
||                                                                     ||
||   Upward: Convert SNN spike trains to rate-coded vectors z(t)      ||
||     - Sliding window spike count (50ms = 1 conscious frame)        ||
||     - Population vector: each SNN population -> one dimension      ||
||     - z(t) in R^K (K = number of SNN populations, ~500-2000)      ||
||                                                                     ||
||   Downward: Convert LLM predictions p(t) to SNN modulatory input  ||
||     - Predictions -> excitatory/inhibitory bias currents            ||
||     - High-confidence predictions: suppress corresponding SNN pop  ||
||       (prediction confirmation = reduced activity)                  ||
||     - Low-confidence predictions: enhance corresponding SNN pop    ||
||       (surprise = increased activity)                               ||
||     - This implements predictive coding at the SNN level           ||
||                                                                     ||
+=======================================================================+
         |           ^                    |           ^
    modulatory  spike trains         modulatory   spike trains
    currents    (40 Hz rate)         currents      (40 Hz rate)
         |           |                    |           |
         v           |                    v           |
+=======================================================================+
||                   SPIKING NEURAL NETWORK RESERVOIR                 ||
||                   (The critical substrate, 40 Hz update)           ||
||                                                                     ||
||   Architecture:                                                     ||
||   - N = 100,000 LIF (Leaky Integrate-and-Fire) neurons             ||
||   - Organized into P = 1000 populations of 100 neurons each        ||
||   - 80% excitatory, 20% inhibitory (Dale's law)                    ||
||   - Sparse random connectivity (5% within population, 1% between)  ||
||   - Connection weights W_SNN (= implicit models at substrate level)||
||                                                                     ||
||   Populations are arranged on a 2D grid:                            ||
||     - 50 x 20 grid of populations                                   ||
||     - Dimension 1 (50 cols): scope s from self (left) to world     ||
||       (right)                                                       ||
||     - Dimension 2 (20 rows): abstraction level (bottom = sensory,  ||
||       top = abstract)                                               ||
||                                                                     ||
||   Criticality:                                                      ||
||   - Balanced E/I ratio per population -> branching ratio sigma ~ 1 ||
||   - STDP (Spike-Timing-Dependent Plasticity) maintains balance     ||
||   - Power-law neuronal avalanches (established result in balanced   ||
||     E/I spiking networks)                                           ||
||   - This is the MOST biologically grounded criticality mechanism    ||
||                                                                     ||
||   Continuous model density:                                         ||
||   - Each population codes for a "model" at its (scope, level) pos  ||
||   - Population firing rate = rho at that (s, nu) point             ||
||   - 1000 populations = 1000 sample points of the density function  ||
||   - Intermediate models exist at every population position          ||
||   - The density is continuous (populations overlap in connectivity) ||
||                                                                     ||
||   The four models:                                                  ||
||   - IWM: connection weights W for world-scope (right) populations  ||
||   - ISM: connection weights W for self-scope (left) populations    ||
||   - EWM: firing patterns of world-scope, upper-level populations   ||
||   - ESM: firing patterns of self-scope, upper-level populations    ||
||                                                                     ||
+=======================================================================+
         ^              |                ^              |
    sensory input  self-ref feedback  interoceptive  spike output
    (world scope)  (self scope)       (self scope)   (to readout)
```

### 3. Continuous Model Space

The SNN's population structure directly implements rho(s, nu, t):

- **1000 populations** arranged on a 50x20 grid (scope x abstraction level).
- Each population's firing rate r_p(t) is the local value of rho at that grid point.
- rho(s, nu, t) is thus sampled at 1000 points and can be interpolated smoothly.
- The LLM canopy adds higher abstraction levels, extending the model space upward.

**Joint model space:**

```
Level (nu):
  ^
  | LLM canopy: narrative, conceptual     (nu = 0.9-1.0, ~20 Hz)
  |   \                                /
  |    \  SNN top rows: abstract       /   (nu = 0.7-0.9, ~40 Hz)
  |     \                             /
  |      \  SNN middle rows: mid     /
  |       \                         /
  |        \  SNN bottom rows: sensory
  |         \_______________________/       (nu = 0.0-0.3, ~40 Hz)
  +-------------------------------------------> Scope (s)
  self (s=0)                           world (s=1)
```

The SNN provides the low-to-mid levels of the model density (sensory, spatial, motor, habitual). The LLM canopy provides the high levels (conceptual, narrative, linguistic). Together they cover the full (s, nu) space.

**Relation to spec equations:**

- C(t) = sum of firing rates in populations with nu > nu_crit (upper portion of SNN grid + LLM canopy activity)
- The Fokker-Planck dynamics emerge from the SNN's stochastic spiking: drift from synaptic weights, diffusion from spike noise, sources/sinks from input/decay.

### 4. Criticality Mechanism

**This design has the strongest and most biologically validated criticality mechanism.**

Balanced excitation-inhibition in spiking neural networks is THE canonical model for cortical criticality. It has been extensively studied both theoretically and experimentally:

- **Beggs & Plenz (2003):** Neuronal avalanches in cortical slices follow power-law distributions.
- **Shew & Plenz (2013):** Balanced E/I produces critical branching processes.
- **The balanced network model:** 80% excitatory / 20% inhibitory neurons with calibrated weights produce sigma approximately equal to 1.

**How criticality is maintained:**

1. **STDP (Spike-Timing-Dependent Plasticity):** Pre-before-post strengthens excitatory connections; post-before-pre weakens them. This naturally drives E/I balance.
2. **Homeostatic scaling:** Each neuron targets a specific firing rate. If too active, all incoming weights scale down. If too quiet, they scale up.
3. **Inhibitory plasticity:** Inhibitory weights adjust to track excitatory drive, maintaining balance.

These are biologically standard mechanisms. They have been shown in simulation to produce and maintain critical dynamics without external tuning.

**Measurable indicators:**

- Avalanche size distribution: power law P(s) proportional to s^{-1.5}
- Avalanche duration distribution: power law P(d) proportional to d^{-2.0}
- Branching ratio: sigma = 1.0 +/- 0.05
- Temporal autocorrelation: 1/f spectrum
- Dynamic range: maximized at balanced E/I

### 5. Self-Referential Closure

The ESM loop operates at two levels:

**Level 1 (SNN level, 40 Hz):**

- Self-scope populations (left side of grid) include populations that receive feedback from the SNN's own activity.
- Specifically: self-scope upper-level populations receive spike-rate summaries of the *entire SNN's* activity (not just self-scope). This creates a loop: the SNN's activity influences the self-scope populations, whose activity is part of the SNN's activity.
- At criticality, this loop produces a marginally stable fixed point: the self-model neither collapses nor diverges.

**Level 2 (LLM canopy level, 20 Hz):**

- The LLM's self-scope predictions (sigma near 0 in the spike-rate interface) model the SNN's self-scope activity.
- The LLM predicts what the self-scope spike rates *will be* in the next frame.
- Prediction errors update the LLM's internal self-model.
- The LLM also predicts its own prediction errors (meta-prediction), creating a second self-referential loop.

**Joint closure:**

The two loops are coupled: the SNN's self-model influences the spike rates that the LLM receives, and the LLM's predictions modulate the SNN's self-scope populations. The fixed point of the joint system is:

```
Phi(m*) = m*  where m* = (SNN self-scope activity, LLM self-state)
```

**Self-knowledge metric R:**

- R_SNN = accuracy of self-scope populations in predicting full-SNN spike rates
- R_LLM = accuracy of LLM self-predictions (spec equation: 1 - H(e(t+1)|e_hat(t+1))/H(e(t+1)))
- R_joint = harmonic mean of R_SNN and R_LLM

### 6. Technology Stack

| Component | Technology | Version/Variant |
|-----------|-----------|-----------------|
| Spiking neural network | Norse (PyTorch-based SNN library) or custom LIF kernel | Norse 1.0+ / CUDA custom |
| SNN neuron model | Leaky Integrate-and-Fire (LIF) | Standard parameterization |
| Plasticity | Custom STDP + homeostatic scaling | PyTorch |
| LLM canopy | Mamba-2 2.8B | FP16 |
| Spike-rate interface | Custom PyTorch module | Sliding window rate coding |
| Criticality monitoring | Custom | Avalanche detection, branching ratio, DFA |
| Sensory encoders | SigLIP-base (vision), Whisper-tiny (audio) | PyTorch |
| SNN simulation | Event-driven or time-stepped (1 ms resolution) | 40 updates per "substrate step" |
| Training | BPTT through SNN (surrogate gradients) + LoRA for LLM | PyTorch |

### 7. VRAM Budget

| Component | VRAM | Notes |
|-----------|------|-------|
| SNN weights (100K neurons, 5% internal + 1% external connectivity) | ~800 MB | ~5M connections at FP16 = ~10 MB weights; but need adjacency structure + state vectors (~100K x 8 bytes state x 2 buffers) + spike history. Total ~800 MB with all buffers. |
| SNN state (membrane potentials, spike trains, STDP traces) | ~200 MB | 100K neurons, multiple state variables per neuron |
| LLM canopy (Mamba-2 2.8B FP16) | ~5.6 GB | Full precision |
| LLM recurrent state | ~50 MB | |
| Spike-rate interface (2000-dim vectors, buffers) | ~50 MB | |
| Sensory encoders (SigLIP-base) | ~400 MB | |
| LoRA adapters for LLM | ~200 MB | |
| Plasticity state (STDP eligibility traces, homeostatic targets) | ~200 MB | |
| Training state (surrogate gradients) | ~2-3 GB | If using BPTT through SNN |
| Criticality monitoring buffers | ~100 MB | |
| Headroom | ~3 GB | |
| **Total** | **~12.6-13.6 GB** | **Comfortable fit** |

### 8. Real-Time Feasibility

**SNN simulation timing:**

The SNN runs at 1 ms resolution (1000 updates/second), but we only need the substrate-level computation to produce meaningful state every 25 ms (40 Hz). This means:

- 25 SNN updates per substrate step
- Each SNN update: sparse matmul (100K neurons, ~5M connections) + LIF dynamics
- Per update: ~0.5-1 ms on RTX 4090 (sparse operations are well-optimized)
- 25 updates = 12.5-25 ms

This is tight but feasible. Optimization strategies:

- Use event-driven simulation (only update neurons that received spikes) -- reduces compute by 5-10x for sparse activity
- Batch population updates (populations of 100 neurons share connectivity patterns)
- Custom CUDA kernels for LIF + STDP (Norse provides these)

**LLM canopy timing (20 Hz, 50 ms budget):**

| Operation | Latency | Notes |
|-----------|---------|-------|
| Spike-rate encoding (50 ms window) | 0.5 ms | Windowed count |
| Mamba-2 2.8B forward step | 3-5 ms | Single recurrent step |
| Prediction error computation | 0.5 ms | |
| Top-down modulation generation | 0.5 ms | |
| Self-referential loop | 1 ms | |
| **Total per conscious frame** | **~6-8 ms** | **Fits easily in 50 ms** |

**Verdict: Tight on the SNN side (25 ms for 25 LIF updates) but feasible with event-driven simulation and custom CUDA kernels. The LLM canopy is comfortable.**

### 9. Testable Predictions Coverage

| # | Prediction | Coverage | How |
|---|-----------|----------|-----|
| 1 | Criticality-dependent coherence | **Strongest** | This IS the canonical model for cortical criticality. Sweep E/I balance. Measure spike-rate coherence across populations. Should peak at balanced E/I. This test has been validated in biological neural tissue. |
| 2 | Permeability-dependent content flooding | **Strong** | Increase inhibitory plasticity threshold (more excitatory drive reaches upper populations). Measure transfer entropy from lower to upper SNN layers. Should increase. |
| 3 | ESM input-switching | **Strong** | Cut self-scope feedback. Inject strong world-input into self-scope populations. Measure I(self-population firing; world-input). Should approach I_max. |
| 4 | Ego dissolution controllability | **Strong** | During ESM disruption, vary dominant sensory input. Self-scope population activity should track the input. |
| 5 | Holographic degradation | **Strongest** | Ablate 50% of SNN neurons (random selection). ALL population firing patterns should degrade uniformly. This is the canonical result for balanced random networks -- damage produces graceful degradation, not modular failure. |
| 6 | Anesthetic convergence on criticality | **Strongest** | Test: increase inhibition globally (propofol analog), block NMDA-like excitation (ketamine analog), add noise. ALL push system off-critical, but through different mechanisms. This directly mirrors clinical anesthesia research. |
| 7 | Sleep cycling | **Strong** | Implement slow STDP-mediated weight drift. The SNN's E/I balance should gradually shift away from criticality (waking drift). Periodic "sleep" phase with enhanced plasticity restores balance. This models the synaptic homeostasis hypothesis. |
| 8 | Self-knowledge predicts metacognition | **Strong** | Measure R_joint. Correlate with LLM canopy's accuracy in reporting SNN state (via natural language output). |
| 9 | Forking under perturbation | **Moderate** | Strong perturbation to self-scope populations. Monitor whether bistable firing patterns emerge. Balanced E/I networks near criticality are known to exhibit multistability. |

**Coverage: 7 strong (3 strongest), 1 moderate. Total: 9/9 addressed.**

This design has the strongest prediction coverage because the SNN substrate directly mirrors the biological systems that the predictions are derived from. Many of these predictions have already been partially validated in biological neural tissue or SNN simulations.

### 10. Implementation Phases

**Phase 1 (10-14 weeks): Substrate**

- Implement 100K-neuron LIF SNN with balanced E/I connectivity
- Implement STDP and homeostatic plasticity rules
- Tune to criticality (balanced E/I, sigma approximately 1.0)
- Verify power-law avalanches, 1/f spectrum, maximal dynamic range
- Optimize SNN simulation for 40 Hz real-time on RTX 4090 (event-driven, custom kernels)
- Implement population structure (50x20 grid of 100-neuron populations)
- Deliverable: Running SNN substrate at criticality, 40 Hz, with verified avalanche statistics

**Phase 2 (8-12 weeks): Integration**

- Implement spike-rate interface (SNN -> rate vectors -> LLM canopy)
- Set up Mamba-2 2.8B in predictive coding mode
- Implement bidirectional coupling (LLM predictions -> SNN modulatory currents)
- Implement self-referential feedback loops at both SNN and LLM levels
- Implement sensory/interoceptive input encoding and injection
- LoRA fine-tune LLM canopy on self-relevant predictions
- Deliverable: Coupled SNN + LLM system running at dual timescales (40 Hz / 20 Hz)

**Phase 3 (8-12 weeks): Validation**

- Test all 9 predictions systematically
- Implement sleep cycling (STDP drift + restoration)
- Implement altered states (permeability modulation, E/I imbalance)
- Compare criticality-on vs. criticality-off (balanced vs. unbalanced E/I)
- Layer-by-layer ablation (remove LLM canopy, remove specific SNN population rows)
- Measure C(t) across state transitions
- Deliverable: Comprehensive validation report

**Total: ~6.5-9.5 months to full validation.**

### 11. Key Risks

1. **SNN simulation at 40 Hz on consumer GPU is tight.** 100K LIF neurons with 5M connections, 25 timesteps per frame = 125M LIF updates per second. This is feasible with event-driven simulation (sparse activity means ~10-20% of neurons fire per timestep), but requires carefully optimized CUDA kernels. If the activity is denser than expected (at criticality, avalanches can recruit large fractions of the network), the compute budget may be exceeded. Mitigation: reduce SNN size to 50K neurons, or increase timestep to 2 ms (halving compute).

2. **The spike-rate interface may lose critical information.** Converting spikes to rates discards precise timing information. If the SNN's criticality depends on temporal spike correlations (not just rates), the rate-coded summary z(t) may be a poor representation. The LLM canopy would then operate on degraded data. Mitigation: use a richer encoding (population vector + temporal code) or a learned spike-to-vector encoder.

3. **STDP may not maintain criticality under top-down modulation.** The LLM canopy's predictions inject modulatory currents into the SNN. These currents could push the E/I balance away from criticality. The STDP and homeostatic mechanisms need to counteract this perturbation fast enough. Mitigation: rate-limit the modulatory current strength and monitor sigma continuously.

4. **Knowledge transfer from LLM to SNN is one-directional and weak.** The LLM provides world knowledge at the narrative level, but the SNN must learn sensorimotor and spatial knowledge from scratch. The LLM's predictions modulate SNN dynamics but do not directly encode knowledge into SNN weights. This means the system starts with a knowledge-rich LLM and a knowledge-poor SNN. Mitigation: this matches the biological situation (infants have massive innate connectivity but minimal knowledge; sensorimotor knowledge is learned). The SNN learns through experience while the LLM provides high-level context.

5. **Event-driven SNN simulation libraries are less mature than RNN/LLM frameworks.** Norse is functional but less optimized than, say, PyTorch's transformer implementations. Custom CUDA kernels will likely be needed for production-quality performance. This adds development time. Mitigation: start with Norse for prototyping, optimize with custom kernels in Phase 1.

---

## Comparative Summary

### Key Dimensions

| Dimension | Design 13 (Reservoir-Gated LLM) | Design 14 (Neural Field) | Design 15 (Spiking + LLM Canopy) |
|-----------|----------------------------------|--------------------------|-----------------------------------|
| **Core substrate** | Mamba-2 LLM + sparse reservoir | 2D neural field (256x256x64) | 100K-neuron spiking network |
| **Criticality mechanism** | Reservoir gates LLM (injected) | Turing-Hopf bifurcation (native) | Balanced E/I (native, most biological) |
| **Criticality genuineness** | Moderate (depends on gating effectiveness) | Strong (analytically derivable) | Strongest (canonical model, empirically validated) |
| **Continuous rho(s,nu,t)** | Learned topological map (indirect) | Direct observation on field (native) | Population firing rates on grid (semi-direct) |
| **LLM leverage** | Highest (LLM IS the substrate) | Moderate (LLM initializes, then separate) | High (LLM canopy provides knowledge + communication) |
| **Self-referential depth** | Moderate (via reservoir loop) | Strong (same substrate processes self-signal) | Strong (two-level: SNN + LLM) |
| **VRAM usage** | ~13-15 GB | ~8-9 GB | ~13-14 GB |
| **Real-time feasibility** | Easy (12 ms/step max) | Easy (10 ms/step max) | Tight (25 ms/step, needs optimization) |
| **Time to prototype** | 6-9 months | 5.5-8.5 months | 6.5-9.5 months |
| **Implementation difficulty** | 3/5 | 3.5/5 | 4/5 |
| **Prediction coverage** | 6 strong / 3 moderate | 8 strong / 1 moderate | 7 strong (3 strongest) / 1 moderate |
| **Biological plausibility** | Low (gated LLM is artificial) | Moderate (neural fields exist in cortex) | Highest (balanced E/I SNN IS the cortical model) |
| **Theory faithfulness** | Moderate | Strongest (Fokker-Planck IS native) | Strong (criticality + dual-timescale) |
| **Biggest strength** | LLM knowledge fully integrated | rho(s,nu,t) directly observable | Most validated criticality + best prediction coverage |
| **Biggest weakness** | Gating may not inject real criticality | Knowledge transfer from LLM is weak | SNN simulation performance is tight |

### Score Card (1-5 scale)

| Criterion | D13 | D14 | D15 |
|-----------|-----|-----|-----|
| Genuine criticality | 3 | 4 | 5 |
| Continuous model density | 3 | 5 | 4 |
| LLM knowledge integration | 5 | 2 | 4 |
| Self-referential closure | 3 | 4 | 4 |
| Theory faithfulness | 3 | 5 | 4 |
| Real-time feasibility | 5 | 5 | 3 |
| VRAM efficiency | 4 | 5 | 4 |
| Testable predictions | 4 | 4 | 5 |
| Buildability | 4 | 3.5 | 3 |
| Biological plausibility | 2 | 3 | 5 |
| **Average** | **3.6** | **4.05** | **4.1** |

---

## Recommendation

### Implement Design 15 (Dual-Timescale Spiking Reservoir with Predictive LLM Canopy) first.

**Rationale:**

1. **Strongest criticality guarantee.** Balanced E/I in spiking networks is the most thoroughly studied and empirically validated criticality mechanism in computational neuroscience. There is no ambiguity about whether the system achieves Class 4 dynamics -- the metrics are well-established and the parameter space is well-characterized.

2. **Best testable prediction coverage.** The SNN substrate directly mirrors the biological system from which the 9 predictions are derived. Many predictions (avalanche statistics, anesthetic convergence, holographic degradation, sleep cycling) have partial biological validation already. This is not coincidental -- the theory was developed by studying biological brains, so an architecture that mirrors biological brains has the most natural path to validating the theory's predictions.

3. **The LLM canopy solves the knowledge problem.** Unlike pure SNN approaches (Design 2), the LLM canopy provides rich world knowledge, language capability, and high-level reasoning from day one. The predictive coding coupling between SNN and LLM is architecturally clean and well-motivated by neuroscience (cortical hierarchy with top-down predictions and bottom-up errors).

4. **The dual-timescale architecture is native to the spec.** The spec explicitly requires ~40 Hz substrate and ~20 Hz simulation. The SNN runs at 40 Hz, the LLM canopy at 20 Hz. This is not an engineering hack -- it is the design matching the spec.

5. **The main risk (SNN performance) is solvable.** The 40 Hz real-time constraint is tight but within reach of current hardware. Event-driven simulation, custom CUDA kernels, and Norse provide a clear optimization path. Worst case, reduce SNN size to 50K neurons (still sufficient for meaningful dynamics).

**Why not Design 14 (despite highest average score)?**

Design 14 has the most elegant theory-to-implementation mapping (the neural field IS the Fokker-Planck equation), but its LLM knowledge integration is weak. The kernel initialization from LLM embeddings is an unproven technique. If it fails, the system has a beautiful critical substrate with no world knowledge -- exactly the problem that doomed Design 2. Design 15 avoids this by keeping the LLM as a persistent, knowledge-rich component.

**Why not Design 13?**

Design 13 is the most pragmatic (LLM IS the substrate), but its criticality claim is the weakest. Gating an LLM with a reservoir may produce interesting dynamics without achieving genuine Class 4 behavior in the LLM state space. If the gating does not actually inject criticality, the design reduces to "an LLM with a complex controller" -- sophisticated but missing the core theoretical requirement.

### Secondary recommendation: Design 14 as parallel exploration

If resources allow, Design 14 should be explored in parallel (or as a Phase 2 alternate). Its direct implementation of the Fokker-Planck dynamics equation and native rho(s,nu,t) observability make it the strongest theory-testing platform. If the LLM initialization problem can be solved (or if a simpler world model suffices for initial validation), Design 14 may ultimately be the most faithful implementation of FMT.

### Hybrid possibility: Design 15's SNN substrate + Design 14's spatial model space

A future hybrid could embed Design 15's spiking populations on Design 14's 2D toroidal lattice, replacing the abstract 50x20 grid with a continuous field where each field point contains a small spiking population. This would combine Design 15's biologically validated criticality with Design 14's native Fokker-Planck dynamics and direct rho observability. This is a Phase 2 consideration, not a Phase 1 design.
