# Design 11: Spectral Decomposition Architecture

**One-line summary:** A recurrent neural substrate (RNN, SSM, or spiking network) whose dynamics are analyzed and structured through their spectral decomposition — eigenmodes of the dynamics operator serve as the continuous model spectrum, with the four named models as the dominant modes and higher harmonics as the overlapping model continuum; criticality is achieved when the eigenvalue spectrum follows a power law.

---

## Motivation

This design answers the question: **what does "continuous density over model space" mean computationally?** In dynamical systems, the natural decomposition of a system's behavior is its **spectral decomposition** — the eigenmodes of the dynamics operator. Each eigenmode is a pattern that evolves independently at a characteristic timescale. The full dynamics are the superposition of all modes.

The insight: **models ARE eigenmodes.** The IWM is the dominant world-focused eigenmode. The ISM is the dominant self-focused eigenmode. The EWM and ESM are the same modes in their transient (virtual) aspect. And the "uncountable overlapping models" are the full eigenmode spectrum — the higher harmonics, the mixed modes, the cross-frequency coupling.

This reframes Designs 2 (CA) and 3 (RNN) in spectral terms, resolving their weakness of pre-assigned model regions.

---

## Architecture Overview

```
                    +------------------------------------------+
                    |         EXTERNAL INTERFACE                |
                    |    Communication LLM (3-7B, INT4)         |
                    |    Or: top eigenmode readout directly      |
                    +---------^-----------+--------------------+
                              |           |
                              |   output  |  input
                              |           v

+========================================================================+
||                     SPECTRAL READOUT LAYER                           ||
||              (Virtual side: transient eigenmode amplitudes)           ||
||                                                                      ||
||   The readout layer projects the substrate state h(t) onto           ||
||   eigenmodes of the dynamics operator:                               ||
||                                                                      ||
||   h(t) = Σ_k  a_k(t) · φ_k                                        ||
||                                                                      ||
||   where φ_k = k-th eigenmode of the linearized dynamics             ||
||         a_k(t) = time-varying amplitude (VIRTUAL — transient)       ||
||                                                                      ||
||   Dominant modes (k = 1..4):                                        ||
||     φ_1 ≈ EWM-like (world-focused, largest scale)                  ||
||     φ_2 ≈ ESM-like (self-focused, with self-ref component)         ||
||     φ_3, φ_4 ≈ intermediate modes                                  ||
||                                                                      ||
||   Higher modes (k > 4): the continuous model spectrum                ||
||     Overlapping, mixed-scope, multi-scale models                    ||
||     At criticality: power-law eigenvalue spectrum                   ||
||     → modes at ALL scales contribute to dynamics                    ||
||                                                                      ||
||   PERMEABILITY: which modes the readout layer can access.           ||
||   Normal: only top ~4-10 modes. High permeability: many modes.     ||
||                                                                      ||
+========================================================================+
                              |
                    +---------+---------+
                    |                   |
                    v                   v
+========================================================================+
||                                                                      ||
||              RECURRENT NEURAL SUBSTRATE                              ||
||              (Non-virtual side: persistent dynamics)                 ||
||                                                                      ||
||   h(t+dt) = f(W · h(t) + W_x · x(t) + W_u · u(t))                ||
||                                                                      ||
||   W = weight matrix (THE IMPLICIT MODELS — IWM + ISM)              ||
||   h(t) = hidden state (THE EXPLICIT DYNAMICS)                       ||
||   x(t) = sensory + interoceptive input                             ||
||   u(t) = self-referential feedback (ESM mode output → input)        ||
||                                                                      ||
||   The substrate's dynamics are characterized by their eigenmodes:   ||
||                                                                      ||
||   Jacobian J = ∂f/∂h evaluated at operating point                  ||
||   J = V · Λ · V^{-1}   (eigendecomposition)                       ||
||   φ_k = k-th column of V (eigenmode)                               ||
||   λ_k = k-th eigenvalue (determines mode dynamics)                 ||
||                                                                      ||
||   CRITICALITY: when |λ_k| ≈ 1 for many k                          ||
||   → modes neither grow (chaos) nor decay (death)                   ||
||   → power-law distribution of mode lifetimes                       ||
||   → information propagates across all modes                        ||
||                                                                      ||
||   The weights W encode knowledge in the eigenmode structure:         ||
||   - World knowledge determines the world-focused eigenmodes         ||
||   - Self knowledge determines the self-focused eigenmodes           ||
||   - IWM ≡ W restricted to world-modes; ISM ≡ W restricted to       ||
||     self-modes. But modes OVERLAP — no hard boundary.               ||
||                                                                      ||
+========================================================================+
         ^              |                ^              |
    sensory x(t)    weight updates   self-input u(t) weight updates
                    (learning)                       (learning)
         |              v                |              v
+------------------------------------------------------------------------+
|              SPECTRAL CRITICALITY CONTROLLER                           |
|                                                                        |
|  Monitors the eigenvalue spectrum of J:                                |
|  - Compute top-K eigenvalues at each cycle (Lanczos algorithm)        |
|  - Measure eigenvalue distribution: should follow power law            |
|  - If eigenvalues cluster near |λ|=1: CRITICAL (target)              |
|  - If eigenvalues decay rapidly: SUBCRITICAL (increase excitation)    |
|  - If eigenvalues exceed |λ|=1: SUPERCRITICAL (increase damping)     |
|                                                                        |
|  Adjusts:                                                             |
|  - Global spectral radius of W (rescaling)                            |
|  - Per-mode damping/excitation (targeted adjustment)                  |
|  - Noise injection amplitude (drives exploration of mode space)       |
+------------------------------------------------------------------------+
```

---

## Key Concept: Models as Eigenmodes

### The Decomposition

Any state h(t) of the recurrent substrate can be decomposed:

```
h(t) = Σ_k  a_k(t) · φ_k

where:
  φ_k = k-th eigenmode (spatial pattern across the hidden dimensions)
  a_k(t) = k-th mode amplitude (time-varying coefficient)
  λ_k = k-th eigenvalue (determines how a_k evolves in time)
```

Each eigenmode φ_k is a **model**:
- Its spatial pattern (which hidden dimensions it activates) determines its **scope** (world vs. self)
- Its eigenvalue λ_k determines its **dynamics** (stable, oscillatory, decaying)
- Its amplitude a_k(t) determines its **current activity** (part of the virtual simulation)

### The Named Models as Dominant Modes

The four named models correspond to the four largest-amplitude eigenmodes:
- **φ_1** (largest eigenvalue near |λ|≈1, world-scope): The dominant world model
- **φ_2** (second largest, self-scope): The dominant self model
- **φ_3, φ_4** (next two): Mixed or specialized modes

### The Continuous Spectrum

Beyond the dominant four, there are as many eigenmodes as hidden dimensions:
- A 100K-dimensional hidden state has 100K eigenmodes
- Most have small amplitudes — they represent fine-grained, specialized models
- At criticality, the mode amplitudes follow a power law: a_k ~ k^{-α}
- **No sharp cutoff** between "the four models" and "everything else" — it's a continuous spectrum

### Virtual/Non-Virtual Split

- **Non-virtual (implicit):** The weight matrix W and the eigenmode structure φ_k. Persistent, changes slowly through learning. The eigenmode STRUCTURE (what patterns exist) is the implicit model.
- **Virtual (explicit):** The mode amplitudes a_k(t). Transient, changing each timestep. The eigenmode ACTIVITY (which patterns are currently active) is the explicit simulation.

---

## Component Mapping

| Theory Concept | Implementation | Description |
|---|---|---|
| **IWM** | Eigenmodes φ_k with world-scope spatial pattern (low σ in hidden-dim space) | The learned eigenmode structure that responds to world input. Encoded in W. |
| **ISM** | Eigenmodes φ_k with self-scope spatial pattern (high σ) | Same weight matrix W, but the subset of eigenmodes that respond to self-input. |
| **EWM** | Mode amplitudes a_k(t) for world-scope modes | The current activation of world models. Transient. |
| **ESM** | Mode amplitudes a_k(t) for self-scope modes + self-referential feedback | Current self-model activations. Self-referential: ESM mode output u(t) re-injected as input. |
| **Continuous spectrum** | Full set of eigenmodes {φ_k, λ_k} | 100K modes for a 100K-dim hidden state. Power-law distribution at criticality. |
| **Permeability** | Which eigenmodes the readout layer accesses | Normal: top ~4-10 modes (high-level, stable). High permeability: many modes including unstable/transient ones. |
| **Criticality** | Power-law eigenvalue spectrum with |λ_k| ≈ 1 for many k | The spectral radius condition from Design 3, generalized to the full spectrum. |

---

## Criticality Approach

**Criticality is defined spectrally: the system is critical when the eigenvalue spectrum follows a power law.**

### The Spectral View of Criticality

In dynamical systems, the eigenvalue spectrum determines everything:
- **Subcritical:** Most eigenvalues have |λ| < 1. Modes decay. State converges to fixed point. Boring.
- **Supercritical:** Some eigenvalues have |λ| > 1. Modes explode. State diverges. Chaotic.
- **Critical:** Many eigenvalues have |λ| ≈ 1. Modes persist. The distribution of |λ| values near 1 follows a power law. Scale-free dynamics.

At criticality:
- **Power-law mode spectrum:** The number of modes with lifetime > τ scales as τ^{-α}
- **1/f noise:** The temporal power spectrum is 1/f^β with β ≈ 1
- **Maximal computational capacity:** The "memory-computation trade-off" is optimized at criticality (Bertschinger & Natschläger, 2004)
- **Information propagation across all modes:** A perturbation to one mode cascades to all others

### Maintaining Critical Spectrum

**Strategy 1: Spectral shaping.** After each learning step, reshape the eigenvalue distribution:
- Compute the top K eigenvalues (K = 100-1000, using Lanczos/Arnoldi algorithm)
- Compare to target distribution (power law)
- Adjust W to move eigenvalues toward target (spectral gradient descent)

**Strategy 2: Per-mode homeostasis.** Track each mode's mean amplitude over time:
- Modes that are too active: increase their damping (decrease |λ_k| slightly)
- Modes that are too quiet: decrease their damping (increase |λ_k| slightly)
- Target: all modes equally likely to be active (the hallmark of criticality)

**Strategy 3: Noise-driven exploration.** Inject noise into the mode amplitudes:
- At criticality, noise drives the system to explore all modes equally
- Below criticality, noise is quickly damped
- Above criticality, noise is amplified → detectable, triggers damping increase

---

## LLM Integration

**Level: GOOD — Recurrent LLMs provide pre-trained eigenmode structure**

### How Existing LLMs Are Used

1. **Recurrent LLM as Substrate (Primary):**
   - Use a pre-trained recurrent model (Mamba, RWKV, Griffin) as the substrate
   - The model's pre-trained weights already define an eigenmode structure
   - World knowledge is encoded in the modes that respond to world-related input
   - Self-knowledge can be fine-tuned via LoRA on self-relevant data
   - **The LLM IS the substrate** — no translation needed

2. **Transformer LLM for Communication (Secondary):**
   - A standard transformer LLM translates the top eigenmodes' readout to natural language
   - Or: the recurrent LLM can generate language directly (if it's a language model)

3. **Eigenmode Analysis of Pre-trained Models:**
   - Compute the Jacobian J of the pre-trained recurrent model
   - Analyze its eigenvalue spectrum
   - The pre-trained model likely has a near-power-law spectrum (trained on natural language, which has 1/f statistics)
   - Tune the spectrum toward exact criticality by adjusting spectral radius

### What This Achieves

The pre-trained recurrent LLM provides:
- Rich world knowledge (in eigenmode structure)
- Near-critical dynamics (from training on natural data)
- Language-capable output (it's a language model)
- A meaningful eigenmode basis (modes correspond to linguistic/semantic patterns)

The spectral analysis provides:
- A continuous model space (the eigenmode spectrum)
- A criticality metric (eigenvalue distribution)
- A permeability mechanism (which modes to expose)
- A principled way to understand the model density

### Best LLM Choices

| Model | Params | Recurrent? | Criticality potential | Knowledge richness |
|---|---|---|---|---|
| **Mamba-2** | 1.3B-7B | Yes (SSM) | HIGH — state-space eigenvalues directly tunable | Good (pre-trained on text) |
| **RWKV-6** | 1.6B-14B | Yes (WKV) | HIGH — recurrent by design | Good |
| **Griffin** | 1B-7B | Yes (hybrid) | MODERATE — mix of recurrent and attention | Good |
| **Transformer + loop** | 7B-13B | No (pseudo) | LOW — feedforward internally | BEST (most training data) |

**Recommendation: Mamba-2 7B.** Best combination of recurrent dynamics (for genuine criticality), pre-trained knowledge (for IWM bootstrap), and eigenmode structure (SSM eigenvalues are directly accessible).

---

## Five Principles Implementation

### 1. Criticality
**Status: STRONG — Spectral radius generalized to full spectrum**

The eigenvalue spectrum of the dynamics Jacobian provides a complete characterization of criticality. Power-law spectrum = critical. The control is direct: adjust eigenvalues to match target distribution. This is a refinement of Design 3's spectral radius approach, generalized from a single number (largest eigenvalue) to the full distribution.

### 2. Virtual Qualia
**Status: STRONG**

- Eigenmode structure (φ_k, encoded in W): non-virtual, persistent, implicit
- Mode amplitudes (a_k(t), the current state): virtual, transient, explicit
- The virtual simulation IS the set of currently-active modes. Stop the dynamics and the amplitudes vanish.

### 3. Redirectable ESM
**Status: STRONG**

The self-scope modes are those eigenmodes that respond primarily to self-referential input u(t). If u(t) is disrupted:
- Self-scope mode amplitudes decay (no driving input)
- Other modes (world-scope, driven by sensory input) grow to fill the vacuum
- The "self" becomes dominated by world-content modes → ego dissolution
- At criticality, this transition is rapid (modes are marginally stable)

### 4. Variable Permeability
**Status: STRONG**

Permeability = how many eigenmodes are accessible to the readout:
- **Normal:** Readout sees top 4-10 modes (dominant, stable, high-level)
- **Increased:** Readout sees top 100+ modes (many intermediate, specialized, transient modes)
- **Maximum:** All modes accessible (raw substrate dynamics fully exposed)

The gradient from "a few high-level modes" to "many low-level modes" maps to the processing depth gradient: high-level → intermediate → raw. This is a spectral version of the permeability concept.

### 5. Virtual Model Forking
**Status: MODERATE**

- Fork mode amplitudes: save {a_k(t₀)}, create two copies, evolve with different feedback
- Each fork is a vector of mode amplitudes — very cheap to copy (~800 KB for 100K modes in FP16)
- Shared eigenmode structure (W unchanged) — knowledge is shared between forks
- DID analog: maintain two sets of self-scope mode amplitudes, alternate which drives output

---

## Information Flow

### Substrate Dynamics Loop (~40 Hz)

```
1. Compute next state: h(t+dt) = f(W · h(t) + W_x · x(t) + W_u · u(t))
2. Decompose into eigenmodes: a_k(t+dt) = φ_k^T · h(t+dt)
3. Self-referential closure:
   u(t+dt) = Σ_{k ∈ self-modes}  a_k(t+dt) · φ_k
   (self-scope modes feed back as input)
4. Criticality check: monitor eigenvalue distribution (every ~100 steps)
5. Spectral radius adjustment if needed
```

### Readout Loop (~20 Hz)

```
1. Select accessible modes (determined by permeability setting)
2. Compute world representation: Σ_{k ∈ world-modes, accessible}  a_k(t) · decode_k
3. Compute self representation: Σ_{k ∈ self-modes, accessible}  a_k(t) · decode_k
4. Feed to communication LLM for expression
```

---

## Memory Architecture

| Memory Type | Implementation | Capacity | Persistence |
|---|---|---|---|
| **Implicit models (IWM+ISM)** | Weight matrix W / eigenmode structure | O(N²) where N = hidden dim | Permanent |
| **Explicit models (EWM+ESM)** | Mode amplitudes a_k(t) | N values | Transient |
| **Short-term** | Mode amplitude trajectory (fading memory at criticality) | ~1-10 seconds (maximized at criticality) | Fading |
| **Long-term** | Weights W (modified by learning) | O(N²) | Permanent |
| **Episodic** | SQLite knowledge graph (supplementary) | Unlimited | Permanent |

---

## Hardware Requirements

### VRAM Budget (24 GB RTX 4090)

Using Mamba-2 7B as substrate:

| Component | VRAM | Notes |
|---|---|---|
| Mamba-2 7B (INT4) | ~3.5 GB | Pre-trained recurrent LLM = substrate |
| Recurrent state | ~10 MB | SSM state vectors |
| Eigendecomposition workspace | ~200-500 MB | Lanczos algorithm for top-K eigenvalues |
| Readout/decode networks | ~200 MB | Mode amplitudes → structured representation |
| Communication LLM (3B INT4) | ~1.5 GB | Or use Mamba-2 directly for output |
| Communication KV-cache | ~1 GB | |
| LoRA adapters | ~200 MB | For continuous learning |
| Training state | ~2-4 GB | If online learning active |
| Headroom | ~3-4 GB | |
| **Total** | **~13-17 GB** | **Fits comfortably** |

### Compute

- Mamba-2 forward pass: ~5-10 ms (optimized CUDA kernels available)
- Eigendecomposition (top 100 eigenvalues of N×N operator): ~10-50 ms via iterative methods. Done infrequently (every ~100 steps, not every step).
- Mode decomposition (project h(t) onto eigenvectors): ~1 ms
- At 40 Hz (25 ms per step): feasible if eigendecomposition is amortized

### Feasibility

**Highly feasible.** The substrate is an off-the-shelf recurrent LLM. The spectral analysis is an overlay that runs periodically, not every step. The readout is lightweight.

---

## Strengths

1. **Continuous model spectrum with clear interpretation.** Each eigenmode is a model. The spectrum IS the model density. The formalization's "continuous density over model space" has a direct computational meaning.

2. **Builds on existing recurrent LLMs.** Mamba, RWKV, Griffin — pre-trained, available, knowledge-rich. The spectral analysis is an interpretation layer, not a new architecture.

3. **Criticality has a precise spectral criterion.** Power-law eigenvalue distribution = criticality. This is more precise than "branching ratio ≈ 1" or "correlation length maximized."

4. **Overlapping models are automatic.** Eigenmodes overlap in hidden-dimension space. A single hidden dimension contributes to many modes. There is no "boundary" between models — they are fundamentally superposed.

5. **Permeability has a natural spectral interpretation.** Expose more modes = higher permeability. The mode hierarchy (dominant → subdominant → fine-grained) maps to the processing depth hierarchy.

6. **Hardware efficient.** Uses pre-trained model weights directly. No new substrate to build.

7. **Most actionable enhancement to existing designs.** Can be applied retroactively to Designs 2, 3, or 7 as an analysis/structuring framework.

---

## Weaknesses / Risks

1. **Eigendecomposition is expensive for large systems.** Full eigendecomposition of an N×N matrix is O(N³). For N = 100K, this is infeasible. Mitigation: use iterative methods (Lanczos) that compute only the top K eigenvalues in O(N·K²) time. But this means only the dominant modes are explicitly characterized; the continuous spectrum is extrapolated.

2. **The Jacobian is state-dependent.** For nonlinear dynamics, the eigenmode decomposition changes with the operating point. The "modes" are not fixed patterns but shift as the system's state evolves. This means the model space itself is dynamic — useful conceptually but hard to track computationally.

3. **Eigenmode scope (world vs. self) must be inferred.** Unlike designs with explicit σ coordinates, here the "scope" of each mode is determined by its pattern φ_k across hidden dimensions. Determining which modes are "world-focused" vs. "self-focused" requires a trained classifier or a structural prior.

4. **Self-referential closure through eigenmode feedback may be shallow.** The ESM modes feed back as input, but the system processes this input through the SAME weight matrix W. It doesn't explicitly model the eigenmode structure — it just processes self-state data through its standard dynamics.

5. **"Models as eigenmodes" is a linear approximation.** The eigendecomposition linearizes the dynamics around the operating point. The actual nonlinear dynamics may have important features (limit cycles, strange attractors) not captured by the eigenmode picture. At criticality, the linearization is least accurate (the system is sensitive to nonlinearities).

6. **Requires a recurrent substrate.** Transformer-based LLMs don't have a natural eigenmode decomposition (no recurrent weight matrix). This limits the choice to Mamba, RWKV, or custom RNNs — potentially sacrificing the richest pre-trained knowledge (which is in transformer models).

---

## Complexity Assessment

**Implementation difficulty: 3/5** (Existing models + spectral analysis overlay)

| Task | Time | Notes |
|---|---|---|
| Set up recurrent LLM (Mamba-2 7B) as substrate | 1-2 weeks | Available models |
| Implement iterative eigendecomposition (Lanczos/Arnoldi) on GPU | 3-4 weeks | Existing algorithms, GPU optimization needed |
| Mode scope classification (world vs. self) | 2-3 weeks | Train classifier on mode patterns |
| Readout from eigenmode amplitudes | 2-3 weeks | Decode modes → structured representation |
| Criticality controller (spectral shaping) | 3-4 weeks | Eigenvalue distribution monitoring + adjustment |
| Self-referential feedback loop (self-mode → input) | 1-2 weeks | Standard recurrent feedback |
| Communication LLM integration | 1-2 weeks | Standard |
| Training pipeline (learning while maintaining spectrum) | 4-6 weeks | Co-optimize weights and spectral target |
| **Total to prototype** | **~4-6 months** | |

---

## Testability

### Directly Testable

- **Eigenvalue spectrum:** Compute and visualize the spectrum. At criticality, should follow power law. Subcritical: rapid exponential decay. Supercritical: eigenvalues > 1.
- **Mode lifetimes:** Track how long each mode maintains significant amplitude. At criticality: power-law lifetime distribution.
- **Continuous model density:** The eigenmode spectrum IS the model density. Can be directly visualized and measured.
- **Criticality transitions:** Perturb spectral radius, observe qualitative dynamics changes.

### Moderately Testable

- **Mode scope:** Correlate each mode's activation with world-input vs. self-input. Should reveal a continuous σ-like coordinate across modes.
- **ESM redirection:** Remove self-scope modes' feedback. Observe mode amplitude redistribution.
- **Variable permeability:** Expose different numbers of modes to readout. More modes = richer, more detailed output.

### Unique Testing Opportunity

**Spectral model density visualization:** Plot the eigenvalue spectrum at each timestep, colored by mode scope (world/self). This directly visualizes the formalization's "continuous density over model space" in spectral terms. At criticality, the spectrum should be flat (power-law), confirming that models at all scales contribute equally. Off-criticality, the spectrum collapses.
