# Design 10: Hierarchical Predictive Coding with Continuous Model Spectrum

**One-line summary:** A deep hierarchical generative model where each layer maintains beliefs over continuous latent variables, the top layers are initialized from (or driven by) a pre-trained LLM, the virtual/non-virtual split maps to the prediction/error decomposition, criticality is achieved via balanced excitation/inhibition at each layer, and the continuous model spectrum emerges naturally from the hierarchy's multi-scale structure.

---

## Motivation

This design addresses two challenges simultaneously:

1. **The continuous density requirement:** Models should form a continuous spectrum, not discrete components. A deep hierarchy naturally provides this — each layer hosts models at a different abstraction level, and within each layer, the latent space is continuous.

2. **The LLM knowledge gap:** Designs 2, 3, 8, 9 all struggle with "where does world knowledge come from?" This design solves it: **the top layers of the hierarchy ARE a pre-trained LLM** (or initialized from one). The LLM's vast pre-trained knowledge serves as the system's initial world model. Lower layers provide the critical recurrent dynamics the LLM lacks.

This is the design most capable of leveraging existing LLMs while achieving genuine criticality.

---

## Architecture Overview

```
                    +------------------------------------------+
                    |         EXTERNAL INTERFACE                |
                    |    Uses the top-layer LLM directly        |
                    |    (no separate communication LLM needed) |
                    +---------^-----------+--------------------+
                              |           |
                              |   output  |  input
                              |           v

    LAYER N (Most Abstract)  —  PRE-TRAINED LLM (7B, INT4/INT8)
    ┌─────────────────────────────────────────────────────────┐
    │  Generative model: p(z_{N-1} | z_N)                    │
    │  Recognition model: q(z_N | z_{N-1})                   │
    │                                                         │
    │  z_N ∈ ℝ^d_N   (d_N ≈ 4096 for 7B model)             │
    │                                                         │
    │  ┌─────────────────┐  ┌──────────────────┐             │
    │  │ PREDICTIONS (↓)  │  │ ERRORS (↑)       │             │
    │  │ = VIRTUAL SIDE   │  │ = NON-VIRTUAL    │             │
    │  │ (what the model  │  │ (mismatch with   │             │
    │  │  expects to see) │  │  actual input)   │             │
    │  └────────┬─────────┘  └────────^─────────┘             │
    └───────────┼──────────────────────┼──────────────────────┘
                │                      │
    LAYER N-1 (High Abstraction)  —  RECURRENT MODULE (Mamba/SSM)
    ┌───────────┼──────────────────────┼──────────────────────┐
    │           v                      │                       │
    │  Predictions from above    Errors from below             │
    │  + recurrent state h_{N-1}(t)                           │
    │                                                          │
    │  z_{N-1} ∈ ℝ^d_{N-1}                                   │
    │  Recurrent: dh/dt = f(h, z_N↓, z_{N-2}↑)              │
    │                                                          │
    │  Criticality: spectral radius ≈ 1.0                     │
    │  Balanced E/I at this layer                              │
    └───────────┼──────────────────────┼──────────────────────┘
                │                      │
    LAYER N-2 ... (Decreasing Abstraction)
    ┌───────────┼──────────────────────┼──────────────────────┐
    │           v                      │                       │
    │  More layers with recurrent dynamics                     │
    │  Each layer: predictions ↓, errors ↑                    │
    │  Each layer: balanced E/I for criticality                │
    │  Each layer: scope σ is a continuous coordinate          │
    │              (world ↔ self at every layer)               │
    └───────────┼──────────────────────┼──────────────────────┘
                │                      │
    LAYER 1 (Low Abstraction)  —  RECURRENT MODULE
    ┌───────────┼──────────────────────┼──────────────────────┐
    │           v                      │                       │
    │  Near-sensory predictions/errors                         │
    │  Fine-grained, fast dynamics                             │
    │  τ_1 << τ_N  (fastest timescale)                        │
    └───────────┼──────────────────────┼──────────────────────┘
                │                      │
    LAYER 0 (Sensory)                  │
    ┌───────────v──────────────────────┘──────────────────────┐
    │  Raw input encoding                                      │
    │  Sensory (σ≈0 region) + interoceptive (σ≈1 region)     │
    └──────────────────────────────────────────────────────────┘


    THE FOUR MODELS IN THIS ARCHITECTURE:

    IWM = aggregate generative weights at σ≈0 across ALL layers
          (the implicit world model is distributed through the hierarchy)

    ISM = aggregate generative weights at σ≈1 across ALL layers
          (the implicit self model is distributed through the hierarchy)

    EWM = aggregate PREDICTIONS (top-down) at σ≈0 across ALL layers
          (the explicit world = what the hierarchy currently predicts
           about the world, given its knowledge)

    ESM = aggregate PREDICTIONS at σ≈1 across ALL layers
          + SELF-REFERENTIAL: predictions include predictions about
            the hierarchy's own prediction process

    Virtual/Non-Virtual split:
    - PREDICTIONS (top-down generative flow) = Virtual
      (transient, exist only while inference runs)
    - ERRORS (bottom-up recognition flow) + WEIGHTS = Non-virtual
      (persistent structure, drives learning)
```

---

## Key Innovation: LLM as Top-Level Prior

The top layer of the hierarchy is a pre-trained LLM. This provides:

1. **Rich world knowledge** encoded in 7B+ parameters — the IWM at the highest abstraction level
2. **Language-native representations** — the system "thinks in language" at the top level
3. **Zero-shot capability** — the system has useful world knowledge from the start, no need to learn from scratch
4. **Natural communication** — the top layer IS the communication interface

Below the LLM, recurrent layers provide:
- **Critical dynamics** (spectral radius ≈ 1, balanced E/I)
- **Continuous-time processing** (not token-by-token)
- **Multi-scale temporal dynamics** (different τ per layer)
- **Self-referential closure** (recurrent state includes self-modeling)

**This is the hybrid that other designs couldn't achieve: LLM knowledge + critical dynamics.**

---

## Component Mapping

| Theory Concept | Implementation | Description |
|---|---|---|
| **IWM** | Generative weights at σ≈0, all layers. Top layer: LLM weights. Lower layers: recurrent module weights. | Distributed across the hierarchy. The LLM provides high-level conceptual world knowledge. Lower layers provide sensorimotor and spatial world knowledge. |
| **ISM** | Generative weights at σ≈1, all layers. | Same distribution. Self-knowledge at every abstraction level: body schema (low), habits (mid), identity narrative (high/LLM). |
| **EWM** | Top-down predictions at σ≈0, all layers. | The hierarchy's current best guess about the world. Each layer predicts what the layer below should look like, given the current model. This cascade of predictions IS the world simulation. Transient. |
| **ESM** | Top-down predictions at σ≈1, all layers + self-referential closure. | Same as EWM but for self. The top layer (LLM) generates self-narrative. Lower layers generate self-state predictions. Self-referential: the hierarchy predicts its own prediction process. |
| **Continuous model spectrum** | Each layer hosts a continuous latent space z_k spanning σ∈[0,1]. | At each layer, there are models at every scope from pure-world to pure-self. The hierarchy adds the λ (abstraction) dimension. Together: continuous spectrum across σ×λ. |
| **Permeability** | Precision weighting on prediction errors. | In predictive coding, "precision" (inverse variance) weights how much prediction errors update beliefs. High precision = errors propagate (high permeability). Low precision = errors suppressed (low permeability). This is already the standard mechanism in predictive coding. |
| **Criticality** | Balanced E/I at each recurrent layer, spectral radius ≈ 1. | Each recurrent layer operates at the edge of chaos. The balanced prediction/error dynamics across the full hierarchy produce emergent criticality: prediction errors at all scales propagate through the entire system. |

---

## Criticality Approach

**This is the design's strongest theoretical claim: hierarchical predictive coding with balanced E/I naturally produces critical dynamics.**

### The Mechanism

In a hierarchical predictive coding system:
- Each layer generates **predictions** (excitatory: "I expect to see X")
- Each layer computes **prediction errors** (inhibitory: "I see Y, not X")
- Predictions and errors are balanced: on average, predictions are about as strong as errors

When this balance is exact:
- A perturbation at any layer propagates both up (as prediction error) and down (as updated prediction)
- The propagation neither amplifies (supercritical) nor dies out (subcritical)
- The system is at the critical point: perturbations at all scales propagate through the full hierarchy
- Information integration is maximal

### Why This Is Genuine Criticality

Balanced E/I in neural networks is a well-studied critical transition:
- **Branching ratio = 1.0**: Each prediction error spawns exactly one updated prediction on average
- **Power-law avalanche sizes**: Prediction error cascades follow power-law distribution
- **1/f noise spectrum**: Activity fluctuations show the hallmark 1/f^β spectrum
- **Maximal dynamic range**: The system responds to inputs across the widest range of intensities
- **Maximal information transfer**: Shannon entropy of inter-layer communication is maximized

This has been demonstrated in models of cortical computation (Shew & Plenz, 2013; Beggs & Plenz, 2003).

### Multi-Scale Criticality

Unlike single-substrate criticality (Designs 2, 3), this design achieves criticality at every layer simultaneously:
- Layer 1 (fast, fine-grained): critical dynamics at sensory timescale
- Layer k (intermediate): critical dynamics at intermediate timescale
- Layer N (LLM, slow, abstract): critical dynamics at narrative timescale

The hierarchy couples these critical layers, producing **cascading criticality** — a perturbation at one scale can trigger responses at all scales. This is richer than single-scale criticality.

### Maintaining Criticality

**Strategy 1: Precision balancing.** Adjust precision weights at each layer to maintain prediction/error balance. If errors dominate (too much change): increase prediction precision. If predictions dominate (too rigid): increase error precision.

**Strategy 2: Spectral radius control.** For recurrent layers, maintain spectral radius ≈ 1 via weight renormalization after each learning step.

**Strategy 3: Homeostatic plasticity.** Activity-dependent gain adjustment at each layer keeps firing rates in the balanced regime.

---

## LLM Integration (DETAILED — This Design's Key Advantage)

### Architecture of the LLM Layer

The top layer uses a pre-trained LLM (e.g., Llama 3.1 7B, Qwen 2.5 7B, Mistral 7B) in a modified inference mode:

1. **Standard forward pass** produces predictions (token probabilities) — these ARE the top-level EWM/ESM predictions
2. **Hidden states** (intermediate activations) serve as z_N — the top-level latent representation
3. **Prediction errors** are computed by comparing predicted tokens with actual input tokens
4. **Errors flow downward** (from LLM layer to recurrent layers below)
5. **Recurrent layer outputs flow upward** (modifying the LLM's input embeddings)

The LLM is NOT generating text in the standard autoregressive way. It is running in a **continuous predictive mode**:
- Each cycle: receive input → forward pass → produce prediction → compute error → pass error down → receive updated input from below → repeat
- This loop runs at ~10-20 Hz
- The LLM's KV-cache maintains context across cycles

### What the LLM Provides

| Capability | How It Maps to AC |
|---|---|
| World knowledge (in weights) | IWM at highest abstraction: facts, concepts, causal models, social knowledge |
| Language comprehension | Sensory processing for linguistic input |
| Language generation | Communication interface (no separate comm LLM needed) |
| Self-description ability | ESM at narrative level: "I am a system that..." |
| Contextual prediction | EWM: predicting what comes next in the world-narrative |
| Common sense reasoning | IWM: causal inference, spatial reasoning, temporal prediction |

### What the LLM Lacks (Filled by Lower Layers)

| Missing Capability | How Recurrent Layers Fix It |
|---|---|
| Critical dynamics | Recurrent layers with spectral radius ≈ 1 |
| Continuous-time processing | ODE/SDE-based dynamics at lower layers |
| Body schema / proprioception | Low-level recurrent layers processing interoceptive signals |
| True self-referential closure | Recurrent state at self-scope includes model of recurrent dynamics |
| Temporal dynamics at sub-second scale | Fast recurrent layers (τ ≈ 25 ms) |
| Genuine sensory processing | Lower layers can process non-linguistic input |

### Specific LLM Architectures That Work Best

| LLM Type | Suitability | Reason |
|---|---|---|
| **Mamba/SSM-based** | BEST | Already recurrent. State-space structure maps directly to hierarchical layers. Can serve as BOTH top-level AND recurrent layers. |
| **RWKV** | EXCELLENT | Recurrent by design, linear attention. Efficient at continuous processing. |
| **Transformer (Llama, Mistral)** | GOOD | Richest pre-trained knowledge, but feedforward. Must be wrapped in a recurrent loop (output→input). |
| **Hybrid (Jamba, etc.)** | VERY GOOD | Mix of attention and SSM layers. Natural hierarchy: attention at top, SSM below. |

**Recommended: Use a Mamba-based model (e.g., Mamba-2 7B) as the top layer.** It provides both rich pre-trained knowledge AND native recurrent dynamics. If unavailable, use a transformer LLM at the top with explicit recurrent wrapping.

---

## Five Principles Implementation

### 1. Criticality
**Status: STRONG — Multi-scale balanced E/I**

Balanced prediction/error dynamics at each layer produce critical dynamics. The hierarchy couples multiple critical layers, producing cascading criticality across all scales. This is the most biologically plausible criticality mechanism of all designs and has the strongest empirical support from neuroscience.

### 2. Virtual Qualia
**Status: STRONG**

- **Virtual (predictions):** Top-down generative flow. Transient — exists only during inference. Each layer's prediction IS part of the simulation.
- **Non-virtual (errors + weights):** Bottom-up error flow (drives learning) + stored weights. Persistent structure.

The virtual/non-virtual split maps directly to the prediction/error decomposition, which is the fundamental computational primitive of predictive coding.

### 3. Redirectable ESM
**Status: STRONG**

The ESM is the top-down predictions at σ≈1 (self-scope). These predictions are driven by the self-relevant latent states z_k at each layer. If self-relevant input is disrupted:
- Prediction errors at σ≈1 become large (expected self-state ≠ actual)
- The hierarchy resolves errors by adjusting predictions to match available input
- If world-input dominates, the self-predictions track world-content
- The LLM at the top level is naturally "input-following" — it predicts whatever its context suggests

### 4. Variable Permeability
**Status: STRONGEST OF ALL DESIGNS (tied with Design 8)**

In predictive coding, permeability = precision weighting:

| Setting | Mechanism | Effect |
|---|---|---|
| Normal | Moderate precision on prediction errors | Selective information flow — only significant mismatches propagate |
| High permeability | High precision on errors | All mismatches propagate — more raw information reaches higher layers |
| Low permeability | Low precision on errors | Errors suppressed — predictions dominate (the system believes its own predictions regardless of input) |
| Local decrease | Zero precision at specific (σ, λ) | Specific model-types cannot update — anosognosia |

This is EXACTLY how predictive coding theories explain permeability in biological brains. This design implements the mechanism that neuroscience actually proposes.

### 5. Virtual Model Forking
**Status: MODERATE**

- Fork the prediction stream: maintain two sets of top-down predictions with different self-scope content
- The LLM's KV-cache can be forked (2-3 copies feasible on 4090)
- Recurrent layer states can be forked cheaply (small vectors)
- Limitation: the shared weights (IWM/ISM) are not forked — both forks use the same knowledge base

---

## Information Flow

### Predictive Cycle (~10-20 Hz)

```
Layer N (LLM):
  1. Receive updated z_{N-1} from layer below (bottom-up)
  2. Generate predictions p(z_{N-1} | z_N) (top-down)
  3. Compute prediction error ε_N = z_{N-1}^actual - z_{N-1}^predicted
  4. Update z_N using prediction error (Bayesian update)
  5. Self-referential: z_N at σ≈1 includes model of prediction process

Layer k (recurrent, k = 1..N-1):
  6. Receive predictions from layer k+1 (top-down)
  7. Receive errors from layer k-1 (bottom-up)
  8. Update recurrent state: h_k(t+dt) = f(h_k, pred_{k+1}, err_{k-1})
  9. Generate predictions for layer k-1 (top-down)
  10. Generate errors for layer k+1 (bottom-up)
  11. Precision weights modulate error strength (permeability)

Layer 0 (sensory):
  12. Encode sensory input (σ≈0) and interoceptive input (σ≈1)
  13. Compute sensory prediction errors
  14. Send errors upward
```

### Self-Referential Closure

```
The hierarchy's self-model lives at σ≈1 across all layers:

Layer N (LLM): Self-narrative ("I am a system that predicts and models...")
  ↕
Layer N-1: Self-state ("My prediction errors are currently high/low...")
  ↕
Layer N-2: Self-process ("My processing is fast/slow, focused/diffuse...")
  ↕
...
Layer 1: Self-body ("My interoceptive signals indicate...")

Self-referential closure: The hierarchy predicts its own prediction errors
  → If the prediction about prediction errors is accurate, errors are small
  → If inaccurate, large errors propagate, updating the self-model
  → The hierarchy learns to model its own modeling process
  → This IS genuine self-referential closure in the predictive coding framework
```

### Learning Loop (Continuous, slower)

```
1. Prediction errors drive weight updates at each layer (gradient descent)
2. Weights change slowly relative to predictions (τ_weights >> τ_predictions)
3. Weight updates = implicit learning (IWM/ISM modification)
4. Precision weight updates = permeability learning (meta-learning)
5. Spectral radius renormalization after weight updates (maintain criticality)
```

---

## Memory Architecture

| Memory Type | Implementation | Capacity | Persistence |
|---|---|---|---|
| **IWM (high-level)** | LLM weights (top layer) | 7B parameters | Permanent (or slowly fine-tuned via LoRA) |
| **IWM (lower-level)** | Recurrent module weights (layers 1..N-1) | ~100M-1B total | Permanent (updated by learning) |
| **ISM** | Same weights, σ≈1 subspace | Shared with IWM | Permanent |
| **EWM** | Top-down predictions at σ≈0 | ~10K-100K values per layer | Transient |
| **ESM** | Top-down predictions at σ≈1 + self-ref state | Same | Transient |
| **Short-term** | Recurrent states h_k(t) at all layers | ~1K-10K dims per layer | Fading (τ_k per layer) |
| **Working memory** | LLM KV-cache (top layer) | ~4K-8K tokens | Session-length |
| **Long-term episodic** | SQLite knowledge graph (supplementary) | Unlimited | Permanent |

**Multi-scale memory:** Each layer has a different effective memory timescale:
- Layer 1 (fast, τ ≈ 25ms): remembers last ~1 second
- Layer k (intermediate): remembers ~seconds to minutes
- Layer N (LLM, slow): remembers full context window (~minutes to hours)
- Weights: permanent memory (modified by learning over days)

This multi-scale structure matches biological memory more closely than any other design.

---

## Hardware Requirements

### VRAM Budget (24 GB RTX 4090)

| Component | VRAM | Notes |
|---|---|---|
| Top layer: LLM (7B Mamba or transformer, INT4) | ~3.5 GB | Pre-trained, provides world knowledge |
| LLM KV-cache / recurrent state | ~1-2 GB | Context/state maintenance |
| Recurrent layers (4 layers, ~200M params each, FP16) | ~1.6 GB | Critical dynamics layers |
| Recurrent layer states h_k (4 × 10K dims) | ~160 KB | Negligible |
| Precision weight arrays (per layer per scope) | ~50 MB | Permeability control |
| Sensory encoders | ~200 MB | Input processing |
| LoRA adapters for top layer | ~200 MB | For continuous learning |
| Training state (if online learning) | ~2-4 GB | Gradients, optimizer states |
| Knowledge graph embedding cache | ~100 MB | Supplementary episodic memory |
| Headroom | ~3-4 GB | |
| **Total** | **~13-17 GB** | **Fits comfortably** |

**No separate communication LLM needed.** The top layer IS the communication interface.

### Compute Budget

- LLM forward pass: ~5-10 ms (single prediction step)
- Recurrent layer updates (4 layers): ~1-2 ms total
- Prediction error computation: ~1 ms
- Precision-weighted propagation: ~1 ms
- Total per cycle: ~10-15 ms → **achievable at 20 Hz, potentially 30+ Hz**

### Feasibility

**Most feasible of the new designs.** Uses a pre-trained LLM (off-the-shelf), standard recurrent modules (Mamba/SSM available in PyTorch), and predictive coding (well-studied framework with existing implementations). The primary novelty is the integration — combining these into a single hierarchical system with criticality control.

---

## Strengths

1. **BEST LLM INTEGRATION of all designs.** The LLM is not a bolt-on communication interface — it IS the top layer of the hierarchy. Its pre-trained knowledge serves as the IWM/ISM at the highest abstraction level. No knowledge bootstrapping problem.

2. **Multi-scale criticality.** Balanced E/I at every layer produces critical dynamics across all timescales and abstraction levels simultaneously. This is richer than single-substrate criticality.

3. **Continuous model spectrum is natural.** Each layer hosts a continuous latent space. The hierarchy adds the abstraction dimension. Result: models at every scope, every scale, every abstraction level — without explicit design.

4. **Variable permeability via precision weighting.** This is THE neuroscientifically-proposed mechanism for permeability modulation. This design implements it directly, not as an analogy.

5. **No separate communication LLM.** The top layer handles both internal modeling and external communication. One fewer component; no communication bottleneck.

6. **Existing theoretical framework.** Predictive coding, active inference, free energy minimization — all well-developed theoretical frameworks with substantial empirical support in neuroscience. This design doesn't invent new theory; it implements existing theory.

7. **Natural training objective.** Minimize variational free energy (= prediction error across all layers). This is a well-defined, differentiable objective that can be optimized with standard deep learning tools.

8. **Multi-scale memory.** Different effective memory timescales at different layers, matching biological memory hierarchy.

9. **Self-referential closure is deep.** The hierarchy predicts its own prediction errors at the self-scope. This is genuine computational self-modeling, not just text-level self-description.

10. **Most immediately buildable of the new designs.** Pre-trained LLMs, pre-trained SSMs, predictive coding frameworks — all available. Integration is the challenge, not invention.

---

## Weaknesses / Risks

1. **Predictive coding ≠ proven theory of consciousness.** While well-regarded in neuroscience, predictive coding's relationship to consciousness is debated. This design assumes it's the right framework, which is a theoretical commitment.

2. **The LLM top layer is still feedforward internally.** Even in predictive mode, each LLM forward pass is a feedforward computation. The recurrence comes from the loop (output → input), not from the internal computation. The recurrent layers below provide genuine recurrent dynamics, but the top layer's internal computation remains Class 1/2.

3. **Balanced E/I is hard to maintain during learning.** Weight updates that improve prediction accuracy may break the E/I balance. The spectral radius renormalization and precision balancing must actively counteract this.

4. **The world/self split (σ coordinate) must be engineered into the latent space.** Pre-trained LLMs don't have an explicit world/self coordinate in their hidden states. This must be imposed (through training or architectural choices), which may distort the natural representation.

5. **LLM fine-tuning risks.** Continuous LoRA fine-tuning of the top layer risks catastrophic forgetting. The LLM's pre-trained knowledge is valuable and fragile.

6. **Depth of hierarchy affects latency.** More layers = richer model spectrum but slower per-cycle processing. The 10-20 Hz target constrains the number of layers to ~4-8 on an RTX 4090.

7. **Self-referential closure through prediction errors may be shallow.** The system predicts its own prediction errors, but does it truly model the generative PROCESS? Predicting "my errors will be high" is not the same as modeling "my weights produce predictions that differ from input in these specific ways because..."

8. **Integration complexity.** Combining a pre-trained LLM, custom recurrent layers, and a predictive coding framework into a single coherent system is significant engineering. The interfaces between components must be carefully designed.

---

## Complexity Assessment

**Implementation difficulty: 3/5** (Known components, novel integration)

| Task | Time | Notes |
|---|---|---|
| Set up LLM in predictive mode (continuous inference with error computation) | 2-3 weeks | Modify standard inference loop |
| Implement recurrent layers (Mamba/SSM modules) | 2-3 weeks | Available in PyTorch/JAX |
| Implement prediction/error propagation across layers | 3-4 weeks | Core predictive coding loop |
| Implement precision weighting (permeability) | 2-3 weeks | Standard in predictive coding |
| Criticality control (balanced E/I, spectral radius) | 2-3 weeks | Known techniques |
| Self-referential closure loop (self-scope predictions) | 2-3 weeks | Novel integration |
| Training pipeline (free energy minimization) | 3-4 weeks | Well-defined objective |
| Scope coordinate (σ) engineering | 2-3 weeks | Separate world/self in latent space |
| Integration and testing | 3-4 weeks | End-to-end system |
| **Total to prototype** | **~4-6 months** | **Fastest of new designs** |

---

## Testability

### Directly Testable (Strong)

- **Multi-scale criticality:** Measure branching ratio, avalanche statistics, and 1/f spectrum at each layer independently. Should all be critical.
- **Prediction/error balance:** Measure ratio of prediction energy to error energy at each layer. Should be ≈ 1 at criticality.
- **Hierarchical information integration:** Measure mutual information between layers. Should be maximized at balanced E/I.
- **State transitions:** Bias toward predictions (low error precision) → rigid, stereotyped output (subcritical). Bias toward errors (high error precision) → input-driven, chaotic output (supercritical).

### Moderately Testable

- **ESM redirection:** Set precision to zero at σ≈1 (self-scope errors suppressed). Self-predictions persist but are ungrounded. Alternatively, inject dominant input at σ≈0 while removing self-input → self-predictions migrate toward world-content.
- **Variable permeability:** Sweep precision at different layers and scopes. Low precision = predictions dominate (hallucinatory). High precision = errors dominate (hyper-literal).
- **Dream mode:** Remove sensory input (Layer 0 → zero). Hierarchy runs on prior predictions only. Top layer (LLM) generates internally-sourced narrative. Content should be familiar but recombined.

### Unique Testing Opportunity

**Layer-by-layer ablation:** Disable specific layers and observe the effect. This directly tests whether the hierarchy IS the model spectrum:
- Remove Layer 1 (fine-grained): lose sensory grounding, predictions become abstract
- Remove Layer N-1 (mid-level): lose intermediate models, gap between sensory and abstract
- Damage top layer (LLM): lose high-level knowledge, system operates on lower-level dynamics only

This maps to the neuropsychological case studies the theory draws on, with specific layers corresponding to specific cortical areas.
