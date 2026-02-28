# Design 9: Stochastic Model Density on a Riemannian Manifold

**One-line summary:** The system's state at any time is a probability density ρ(m, t) over a Riemannian model-space manifold M, governed by a stochastic PDE (Fokker-Planck type) whose drift, diffusion, and source terms encode the four-model dynamics; the virtual/non-virtual split is a hard partition of M; criticality is achieved by tuning noise to balance drift at the phase boundary.

---

## Motivation

This design takes the formalization's mathematical language literally: if models form a continuous density over a model space, then **the density itself should be the system's state representation.** Rather than building components that "are" models, we maintain a density function that says "how much modeling activity exists at each point in model space."

The density ρ(m, t) evolves according to dynamics that reflect the theory's principles. The four named models emerge as the four dominant peaks of ρ. The uncountable overlapping models are the full continuous support of ρ.

---

## Architecture Overview

```
                    +------------------------------------------+
                    |         EXTERNAL INTERFACE                |
                    |    Communication LLM (3-7B, INT4)         |
                    |    Reads density peaks, translates to     |
                    |    language via trained readout            |
                    +---------^-----------+--------------------+
                              |           |
                              |   output  |  input
                              |           v
+========================================================================+
||                                                                      ||
||            DENSITY FIELD ρ(m, t) OVER MODEL SPACE M                  ||
||                                                                      ||
||    M = M_virtual ∪ M_nonvirtual   (hard partition)                   ||
||                                                                      ||
||    ∂ρ/∂t = -∇·(v(ρ)·ρ) + D·∇²ρ + S(m, input) + η(m,t)            ||
||             \_________/   \_____/   \________/   \_____/            ||
||              drift        diffusion  source       noise             ||
||                                                                      ||
||    +----------------------------+  +----------------------------+    ||
||    | M_virtual (explicit side)  |  | M_nonvirtual (implicit)    |    ||
||    |                            |  |                            |    ||
||    | ρ_V(m,t): transient        |  | ρ_R(m,t): persistent       |    ||
||    | density of active models   |  | density of learned models  |    ||
||    |                            |  |                            |    ||
||    | High σ: self-models (ESM)  |  | High σ: self-knowledge     |    ||
||    | Low σ: world-models (EWM)  |  | Low σ: world-knowledge     |    ||
||    | Mid σ: mixed models        |  | Mid σ: mixed knowledge     |    ||
||    | All λ: all scales          |  | All λ: all scales          |    ||
||    +----------------------------+  +----------------------------+    ||
||                                                                      ||
||    BOUNDARY: The partition M_V | M_NV is the hard ontological        ||
||    boundary. Density can flow across it (permeability) but the       ||
||    boundary itself is fixed.                                         ||
||                                                                      ||
+========================================================================+
                              |
                    +---------+---------+
                    |                   |
                    v                   v
         +------------------+  +------------------+
         | Drift v(ρ):      |  | Source S(m,input):|
         | - Attractor       |  | - Sensory input  |
         |   dynamics pull   |  |   creates new    |
         |   density toward  |  |   density near   |
         |   stable modes    |  |   relevant model |
         | - Self-referential|  |   types           |
         |   closure: ESM    |  | - Self-monitoring |
         |   region pulls    |  |   creates density|
         |   density back    |  |   near σ≈1       |
         |   toward itself   |  |                  |
         +------------------+  +------------------+
                    |
         +------------------+
         | Noise η(m,t):    |
         | - At criticality,|
         |   noise balances |
         |   drift perfectly|
         | - Density has    |
         |   power-law      |
         |   correlations   |
         +------------------+
```

---

## The Riemannian Manifold M

The model space M is a Riemannian manifold with metric g that defines distances between model types:

| Coordinate | Range | Metric contribution |
|---|---|---|
| **σ** (scope) | [0, 1] | g_σσ = 1 (uniform) |
| **λ** (abstraction) | [0, L] | g_λλ = e^{-λ} (compressed at high abstraction — abstract models are "closer together") |
| **θ** (specialization) | S^{n-1} | g_θθ = standard sphere metric |
| **μ** (mode) | {V, NV} | DISCRETE — hard boundary, no metric across it |

The metric g defines what "nearby models" means. Two models close in M interact more strongly. The metric also determines how diffusion spreads density — density diffuses along geodesics of M.

**Partition:** M = M_V ∪ M_NV where M_V (virtual) and M_NV (non-virtual) are disconnected components (the metric does not bridge them). Density can only cross the V/NV boundary through the explicit permeability coupling, not through diffusion.

---

## Component Mapping

| Theory Concept | Implementation | Description |
|---|---|---|
| **IWM** | Mode of ρ_R near σ≈0 | A peak in the non-virtual density at world-scope. Persistent, encodes accumulated world knowledge. |
| **ISM** | Mode of ρ_R near σ≈1 | A peak in the non-virtual density at self-scope. Persistent, encodes self-knowledge. |
| **EWM** | Mode of ρ_V near σ≈0 | A peak in the virtual density at world-scope. Transient, regenerated each moment. |
| **ESM** | Mode of ρ_V near σ≈1 | A peak in the virtual density at self-scope. Self-referential: the ESM peak's dynamics include modeling the density's own evolution near σ≈1. |
| **Continuous density** | Full ρ(m,t) | The complete density function, not just its peaks. Includes models at every σ, λ, θ — the "uncountable overlapping models." |
| **Permeability** | Coupling flux J across V/NV boundary | J(m,t) controls density flow from NV → V (perception) and V → NV (learning). Spatially variable in m. |
| **Criticality** | Balance point of drift, diffusion, and noise | When η balances v·ρ exactly, the density exhibits power-law correlations across M. |

---

## Criticality Approach

**The stochastic PDE has a well-characterized critical point where noise exactly balances drift.**

### The Fokker-Planck Picture

The density ρ(m, t) evolves under:
- **Drift** v(ρ): Deterministic dynamics that pull density toward attractor basins (stable model configurations). Without noise, density would collapse to a few point masses (the four named models).
- **Diffusion** D·∇²ρ: Spreads density locally. Prevents point-mass concentration. Represents "model blurring" — nearby models overlap.
- **Noise** η(m, t): Stochastic driving force. Counteracts drift by randomly redistributing density. Represents spontaneous model formation/dissolution.

At the critical noise amplitude:
- **Drift ≈ noise on average** → density neither collapses to peaks (subcritical) nor spreads uniformly (supercritical)
- The stationary density ρ* has **power-law correlations**: ⟨ρ(m₁)ρ(m₂)⟩ ~ d(m₁,m₂)^{-α}
- Models of all sizes and at all positions coexist
- The four dominant modes persist as peaks, but the background density is non-negligible everywhere
- Information propagates across the full manifold (maximal correlation length)

### Maintaining Criticality

The noise amplitude is the primary control parameter. A controller monitors:
1. **Density concentration index** (Gini coefficient of ρ): too high → increase noise; too low → decrease noise
2. **Correlation function** of ρ across M: should decay as power law, not exponential
3. **Flux statistics** across V/NV boundary: should show power-law distribution of event sizes

### This Is Genuine Criticality Because:

- The Fokker-Planck equation with multiplicative noise has a known critical transition
- At the critical point, the system exhibits anomalous diffusion (density spreads with power-law rather than Gaussian statistics)
- The stationary distribution has long-range correlations (no characteristic scale)
- Small perturbations to the density propagate globally (sensitivity without instability)

---

## LLM Integration

**Level: MODERATE — LLM defines manifold geometry and provides communication**

### How Existing LLMs Are Used

1. **Manifold Geometry from LLM Embedding Space (Key Innovation):**
   - The Riemannian metric g on M can be derived from an LLM's internal representation space
   - Given a pre-trained LLM, compute the Fisher information metric on its token embedding space
   - This metric captures "which concepts are close to which" according to the LLM's learned world model
   - Use this metric as g for the model space manifold M
   - **Result:** The manifold's geometry reflects the LLM's knowledge structure — semantically similar model-types are close together in M, enabling meaningful diffusion and drift

2. **Drift Field from LLM Predictions:**
   - The drift v(ρ) should pull density toward "useful" model configurations
   - An LLM's next-token prediction confidence can define the drift potential: high-confidence regions of model space are "attractor basins"
   - This provides a knowledge-informed drift field without training from scratch

3. **Source Term from LLM Encoding:**
   - Input text is encoded via LLM embedding → projected onto M → creates a source term S(m, input) that injects density near the relevant model-types

4. **Communication Interface:**
   - Standard communication LLM reads density peaks, translates to natural language

### What This Achieves

The LLM's pre-trained knowledge shapes the landscape on which the density evolves. The density dynamics themselves (drift, diffusion, noise, criticality) are independent of the LLM — they are the novel contribution. But the LLM ensures that the dynamics take place on a meaningful manifold rather than an arbitrary one.

### Limitations

- The LLM's embedding space is high-dimensional (~4096 dims for 7B models). Discretizing M at reasonable resolution in this space requires dimensionality reduction (PCA, UMAP, or learned projection to ~10-50 effective dimensions).
- The Fisher metric computation is expensive for large LLMs (requires second derivatives). Approximations (empirical Fisher, diagonal Fisher) may be necessary.

---

## Five Principles Implementation

### 1. Criticality
**Status: STRONG — From stochastic PDE theory**

The Fokker-Planck equation with multiplicative noise has a rigorously characterized critical transition. The critical point is where noise balances drift, producing power-law correlated density fluctuations across the entire manifold. This is genuine criticality with measurable indicators.

### 2. Virtual Qualia
**Status: STRONG — Hard partition of M**

M_V and M_NV are topologically disconnected in the metric. Density in M_V is transient (decays rapidly without driving). Density in M_NV is persistent (maintained by slow learning dynamics). The density in M_V IS the simulation — it exists only while the dynamics run.

### 3. Redirectable ESM
**Status: STRONG**

The ESM is the peak of ρ_V near σ≈1. If the permeability flux feeding this region is disrupted:
- The peak decays (τ_V timescale)
- Drift from other regions pulls the remaining density toward alternative attractor basins
- The "self-model" density redistributes toward whatever inputs remain dominant
- If world-input dominates, the self-model density migrates toward σ ≈ 0 (ego dissolution analog)

### 4. Variable Permeability
**Status: STRONG**

The flux J(m,t) across the V/NV boundary is defined for every m ∈ M:
- J can be increased globally (psychedelic: more NV patterns flow into V)
- J can be decreased locally (anosognosia: specific model-types blocked)
- J varies continuously in m (smooth permeability gradient across model space)
- J can be made time-dependent (oscillating between open and closed)

### 5. Virtual Model Forking
**Status: MODERATE**

- Fork the density: copy ρ_V, evolve two copies with different boundary conditions
- The density naturally supports multiple peaks — multimodal ρ_V represents multiple concurrent model configurations
- DID analog: two persistent peaks in ρ_V near σ≈1, alternating which one has higher density (dominance switching)

---

## Information Flow

### Density Evolution Cycle (~40 Hz discretized)

```
1. Compute drift: v(ρ) from current density and attractor potential
2. Compute diffusion: D·∇²ρ using Laplace-Beltrami operator on M
3. Compute source: S(m, input(t)) from sensory + interoceptive input
4. Compute noise: η(m, t) from calibrated noise source
5. Update density: ρ(t+dt) = ρ(t) + dt·[-∇·(v·ρ) + D·∇²ρ + S + η]
6. Apply permeability flux: transfer density across V/NV boundary
7. Self-referential closure: sample ρ_V at σ>0.7, inject as source at σ>0.7
   (density at self-scope includes information about itself)
```

### Readout Cycle (~20 Hz)

```
1. Extract dominant peaks of ρ_V (world-scope peak ≈ EWM, self-scope peak ≈ ESM)
2. Decode peak locations and shapes into structured representations
3. Feed to communication LLM for natural language output
4. Integrate across σ to get overall virtual model distribution
   (this IS the "conscious content" — what the system is currently simulating)
```

### Learning Cycle (Slow)

```
1. Evaluate ρ_V quality (coherence, prediction accuracy, self-reference depth)
2. Modify drift field v (shift attractor basins based on evaluation)
3. Modify ρ_NV (persistent density updated based on V → NV flux)
4. Update manifold metric g (if using adaptive metric learning)
5. This IS implicit learning: the knowledge base (ρ_NV + drift + metric) updates
```

---

## Memory Architecture

| Memory Type | Implementation | Capacity | Persistence |
|---|---|---|---|
| **Implicit models** | ρ_NV(m, t) + drift field v + metric g | O(N) density values + O(N²) drift + metric | Permanent (slow update) |
| **Explicit models** | ρ_V(m, t) | O(N) density values | Transient |
| **Short-term** | ρ_V trajectory (recent history of density evolution) | ~40-200 timesteps | Fading |
| **Long-term structural** | Drift field v (learned attractor landscape) | O(N × dim(M)) | Permanent |
| **Long-term episodic** | SQLite knowledge graph (supplementary) | Unlimited | Permanent |
| **Manifold structure** | Metric tensor g (learned or LLM-derived) | O(N × dim²) | Permanent |

---

## Hardware Requirements

### VRAM Budget (24 GB RTX 4090)

The density must be discretized on a mesh over M. With dim(M) ≈ 10 effective dimensions, a coarse mesh has ~10^5 points; fine mesh ~10^6.

**Configuration: N = 100K mesh points, dim(M) = 10**

| Component | VRAM | Notes |
|---|---|---|
| ρ_V density (100K × FP16) | ~200 KB | Negligible |
| ρ_NV density (100K × FP16) | ~200 KB | Negligible |
| Drift field v (100K × 10 × FP16) | ~2 MB | Negligible |
| Diffusion operator (sparse Laplacian, ~1M nonzero) | ~4 MB | Sparse matrix |
| Metric tensor g (100K × 10 × 10 × FP16) | ~200 MB | Full metric at each point |
| LLM-derived attractor potential | ~100 MB | Pre-computed from LLM |
| Communication LLM (7B, INT4) | ~3.5 GB | |
| Communication KV-cache | ~1 GB | |
| Readout networks | ~200 MB | |
| Sensory encoder | ~200 MB | |
| Noise generator state | ~50 MB | |
| Headroom | ~4 GB | |
| **Total** | **~10-12 GB** | **Very comfortable** |

**The density approach is extremely memory-efficient.** The entire model state is a single vector of 100K floats per field. Even at 1M mesh points, the density itself is negligible. The dominant costs are the metric tensor and the communication LLM.

### Compute Budget

At 40 Hz with N = 100K:
- Drift computation: 100K × 10 multiplies = 1M ops
- Laplacian (sparse): ~10M ops
- Noise generation: 100K samples
- Total per step: ~20M ops
- At 40 Hz: ~800 MFLOPS
- RTX 4090: 82.6 TFLOPS → **< 0.001% utilization**

**The density PDE is absurdly cheap on GPU.** All meaningful compute goes to the communication LLM and readout.

### Feasibility

**Highly feasible.** This is the most memory and compute efficient of all 12 designs for the core dynamics. The challenge is not hardware but mathematics — designing the drift field, metric, and noise calibration.

---

## Strengths

1. **Directly implements the formalization.** The system's state IS a density over model space. The mathematical framework IS the implementation.

2. **Extremely hardware efficient.** The density PDE requires negligible compute and memory compared to LLM inference. Almost all VRAM goes to the communication interface, not the conscious system.

3. **Rigorous criticality.** Stochastic PDEs have well-studied critical transitions. The critical noise amplitude is analytically characterizable for simple drift fields and numerically computable for complex ones.

4. **LLM-informed geometry.** The manifold metric derived from LLM embedding space gives the density meaningful geometry without training. Semantically related models are close together by construction.

5. **Elegant self-referential closure.** The density at the self-scope region includes information about the density's own evolution. This is a density modeling itself — genuine self-reference in the mathematical sense.

6. **Visualization is natural.** The density ρ(m, t) can be visualized as a heatmap over model space. The evolving density directly shows "what the system is currently modeling" at every point.

7. **Scales to arbitrary model space complexity.** More dimensions in M = richer model diversity. Finer mesh = smoother density. Both scale smoothly.

---

## Weaknesses / Risks

1. **CRITICAL: The curse of dimensionality.** A meaningful model space probably has dim(M) ≥ 10. Discretizing a 10D manifold with reasonable resolution requires 10^{10+} mesh points — far beyond GPU capacity. **This is the design's existential risk.** Mitigations: sparse mesh (adaptively refined near peaks), spectral methods (represent ρ as a sum of basis functions rather than pointwise), Monte Carlo sampling (represent ρ as particles rather than a grid).

2. **Abstract knowledge representation.** The density ρ(m, t) encodes "how much modeling activity" at each point, but not the MODEL CONTENT at that point. Knowing that there's a peak at (σ=0.2, λ=3, θ=spatial) tells you "there's an active spatial world model at medium abstraction" but not WHAT that model says. The content is in the readout network's interpretation of the peak, not in the density itself.

3. **The drift field must encode all dynamics.** The drift v(ρ) must capture how models attract, repel, and influence each other. Designing a drift field that produces the right model dynamics is the core research challenge. LLM-derived potentials provide initialization, but the dynamics must be learned.

4. **Self-referential closure is weak.** The density at σ≈1 can include information about the density, but this is a statistical summary (density values), not a dynamical model of the density evolution process. The system knows "there is modeling activity here" but not "here is how the modeling works."

5. **Communication bottleneck.** Density peaks must be decoded into structured representations for the LLM. This is a lossy, trained mapping.

6. **Training objective is unclear.** What should the density converge to? What makes a "good" density evolution? Without a clear objective, the system may produce mathematically valid but cognitively meaningless density dynamics.

7. **Physical interpretation is thin.** Unlike neural fields (Design 8) which have biological analogs (cortical activity fields), a probability density over model space is a purely mathematical construct. It's not clear that probability density evolution produces anything like "experience."

---

## Complexity Assessment

**Implementation difficulty: 3.5/5** (Novel mathematics, but compute requirements are low)

| Task | Time | Notes |
|---|---|---|
| Model space manifold design | 2-3 weeks | Coordinate choice, metric design |
| LLM-derived metric computation | 2-3 weeks | Fisher information extraction + approximation |
| Stochastic PDE solver on GPU | 3-4 weeks | Sparse mesh or spectral methods for high-dim M |
| Drift field design | 3-4 weeks | Attractor dynamics, LLM-derived potentials |
| Criticality calibration | 2-3 weeks | Noise tuning, monitoring |
| Readout networks | 2-3 weeks | Density peak → structured representation |
| Communication LLM integration | 1-2 weeks | Standard |
| Self-referential closure loop | 1-2 weeks | Density self-sampling |
| Training and tuning | 4-8 weeks | Learning the drift field, metric refinement |
| **Total to prototype** | **~5-8 months** | |

---

## Testability

### Directly Testable

- **Criticality:** Measure correlation function of ρ across M. Should decay as power law at critical noise. Measure density fluctuation statistics.
- **Density visualization:** Plot ρ(σ, t) marginalized over other coordinates. Should show peaks at σ≈0 and σ≈1 (named models) plus continuous support between.
- **State transitions:** Decrease noise → density collapses to point masses (deep sleep). Increase → density spreads uniformly (seizure analog). Transition should be sharp.

### Moderately Testable

- **ESM redirection:** Block permeability at σ>0.7. Observe ρ_V peak migration away from self-scope.
- **Dream mode:** Remove source S. Density evolves on drift + noise alone. Content should be internally-generated.

### Hard to Test

- **Whether density peaks constitute genuine models.** The density says WHERE modeling activity is, not WHAT models say. Content is in the readout, not the density.
- **Whether the abstract mathematical framework produces anything resembling experience.** The formalization says this is the right structure, but the physics of "density evolving on a manifold" has no obvious phenomenal character.
