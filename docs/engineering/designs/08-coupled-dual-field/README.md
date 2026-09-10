# Design 8: Coupled Dual-Field Dynamics

**One-line summary:** Two continuous neural fields — an implicit (non-virtual, persistent) field and an explicit (virtual, transient) field — coupled through a sharp interface, where models are localized excitation patterns in either field that emerge from the dynamics rather than being architecturally pre-assigned, with criticality achieved via Turing-Hopf bifurcation at the coupling boundary.

---

## Motivation: The Continuous Density Insight

The FMT formalization establishes that the four named models (IWM, ISM, EWM, ESM) are a *minimum sufficient set*, not the full picture. The biological substrate implements an uncountable number of overlapping models on both sides of the implicit/explicit divide. Models form a **continuous density over a model space**, with the virtual/non-virtual split as the only hard ontological boundary.

All previous designs (1-7) reify the four models as discrete, named, architecturally separated components. This design takes the continuous density seriously: **models are not designed-in — they emerge as patterns in a continuous field.**

---

## Architecture Overview

```
                    +------------------------------------------+
                    |         EXTERNAL INTERFACE                |
                    |    Communication LLM (3-7B, INT4)         |
                    |    Translates field readout <-> language   |
                    +---------^-----------+--------------------+
                              |           |
                              |   output  |  input
                              |           v

+=======================================================================+
||                                                                     ||
||              EXPLICIT FIELD  V(x, t)                                ||
||              (Virtual side — transient, "lights on")                ||
||                                                                     ||
||   x ∈ M (model space manifold, continuous)                          ||
||                                                                     ||
||   σ=0 (world) ◄══════════ σ ═══════════► σ=1 (self)                ||
||                                                                     ||
||   Dynamics: τ_V · ∂V/∂t = -V + g(K_V * V + C_↓·R + u_sr + I_ext) ||
||                                                                     ||
||   Patterns that emerge:                                             ||
||     • EWM-like peaks near σ≈0 (world-focused models)               ||
||     • ESM-like peaks near σ≈1 (self-focused models)                ||
||     • Mixed models at intermediate σ (body-in-world, etc.)         ||
||     • Models at every spatial scale (fine-grained to abstract)      ||
||     • Self-referential modes (V includes patterns modeling V)       ||
||                                                                     ||
+==╤════════════════════════════════════════════════════════════╤═══════+
   │          HARD ONTOLOGICAL BOUNDARY                        │
   │     Permeability interface: C_↑(x,t) and C_↓(x,t)        │
   │     The ONLY architectural hard structure                  │
   │     Dynamically modulated (variable permeability)          │
+==╧════════════════════════════════════════════════════════════╧═══════+
||                                                                     ||
||              IMPLICIT FIELD  R(x, t)                                ||
||              (Non-virtual side — persistent, "lights off")          ||
||                                                                     ||
||   Same model space M, same σ coordinate                             ||
||                                                                     ||
||   Dynamics: τ_R · ∂R/∂t = -R + f(K_R * R + C_↑·V + I_sensory)    ||
||             τ_R >> τ_V  (implicit field changes slowly)             ||
||                                                                     ||
||   Patterns that emerge:                                             ||
||     • IWM-like density near σ≈0 (accumulated world knowledge)      ||
||     • ISM-like density near σ≈1 (accumulated self knowledge)       ||
||     • Overlapping learned structures at every scale and scope       ||
||     • Connectivity kernel K_R encodes long-term knowledge           ||
||                                                                     ||
+=======================================================================+
         ^              |                ^              |
    sensory         field updates    self-sensors    field updates
    input I_ext     (slow learning)  (interoceptive) (slow learning)
         |              v                |              v
+-----------------------------------------------------------------------+
|              CRITICALITY: TURING-HOPF BIFURCATION                     |
|                                                                       |
|   The coupled R-V system has a critical point where:                  |
|   • Pattern formation becomes scale-free (all spatial frequencies)    |
|   • The coupling C_↑, C_↓ is tuned to the bifurcation threshold     |
|   • Power-law avalanche dynamics in both fields                      |
|   • Maximal information transfer across the R↔V boundary             |
|                                                                       |
|   Control parameters:                                                |
|   • Coupling strengths C_↑, C_↓ (primary criticality control)       |
|   • Kernel widths in K_R, K_V (spatial correlation length)           |
|   • Time constant ratio τ_R/τ_V (temporal scale separation)          |
|   • Noise amplitude (drives exploration of pattern space)            |
+-----------------------------------------------------------------------+
```

---

## The Model Space Manifold M

The key innovation is the continuous model space M. Every point x ∈ M represents a "model type." The manifold has:

| Coordinate | Range | Meaning |
|---|---|---|
| **σ** (scope) | [0, 1] continuous | 0 = pure world-model, 1 = pure self-model. Intermediate values = mixed scope |
| **λ** (scale) | [0, ∞) continuous | Abstraction level. 0 = raw sensory, high = abstract conceptual |
| **θ** (specialization) | S^n (hypersphere) | Direction in specialization space: spatial, causal, temporal, social, etc. |

The four named models occupy regions, not points:
- **IWM**: σ ≈ [0, 0.3], all λ, all θ — in the implicit field R
- **ISM**: σ ≈ [0.7, 1.0], all λ, all θ — in the implicit field R
- **EWM**: σ ≈ [0, 0.3], all λ, all θ — in the explicit field V
- **ESM**: σ ≈ [0.7, 1.0], all λ, all θ — in the explicit field V

But crucially, there is no hard boundary at σ = 0.3 or 0.7. Models shade continuously from world-focused to self-focused. A "body-in-world" model sits at σ ≈ 0.5. A "how-others-see-me" model sits at σ ≈ 0.6. These intermediate models are not represented in Designs 1-7 but exist naturally here.

---

## Component Mapping

| Theory Concept | Implementation | Description |
|---|---|---|
| **IWM** | Density peak in R near σ≈0 | World knowledge patterns in the implicit field. Not a separate component — a region of high activity/structure in the continuous implicit field. |
| **ISM** | Density peak in R near σ≈1 | Self knowledge patterns in the implicit field. Overlaps with IWM through the continuous σ coordinate (body-in-world models live in between). |
| **EWM** | Density peak in V near σ≈0 | World simulation patterns in the explicit field. Transient, regenerated by the field dynamics at each moment. |
| **ESM** | Density peak in V near σ≈1 | Self simulation patterns in the explicit field. Self-referential: V's self-relevant patterns include patterns that model V's own dynamics. |
| **Permeability** | Coupling functions C_↑(x,t), C_↓(x,t) | The permeability interface between R and V. Spatially and temporally variable — different model-types have different permeability. THIS is the only hard architectural structure. |
| **Substrate** | The coupled R-V field system itself | The two fields and their coupling dynamics constitute the computational substrate. Criticality is a property of this coupled system. |
| **"Uncountable models"** | All localized patterns in R and V | Every bump, wave, spiral, or structure in either field is a model. The named four are the dominant modes. The rest form a continuous density. |

---

## Criticality Approach

**This is the design's central strength: criticality emerges naturally from the coupled field dynamics at a well-characterized bifurcation point.**

### The Turing-Hopf Bifurcation

Coupled reaction-diffusion fields (which neural fields are a special case of) have well-studied critical transitions:

1. **Subcritical (C < C_crit):** Both fields converge to spatially uniform states. No pattern formation. No models emerge. Analog of deep sleep / anesthesia.

2. **Critical (C ≈ C_crit):** Pattern formation begins. Patterns at ALL spatial scales are marginally stable. Power-law distribution of pattern sizes. Maximum information transfer between R and V. Scale-free correlations. THIS is the Class 4 analog.

3. **Supercritical (C > C_crit):** Patterns form but are dominated by a few spatial frequencies. Ordered but rigid. Or, for strongly supercritical: chaotic, all patterns unstable. Analog of seizure.

### Why This Is Genuine Criticality (Not Approximation)

The Turing bifurcation in neural field equations produces:
- **Power-law distribution of pattern sizes** (analogous to avalanche statistics in CA)
- **Maximal correlation length** (patterns span the entire field at criticality)
- **Scale-free dynamics** (no characteristic frequency or wavelength dominates)
- **Maximum information transfer** between the two fields
- **Sensitivity to input** with proportional (not exponential) response

This is mathematically equivalent to Class 4 dynamics for continuous fields. It is not a metaphor or approximation — it is the continuous-field version of edge-of-chaos.

### Maintaining Criticality

**Strategy 1: Adaptive coupling.** A homeostatic mechanism monitors pattern statistics in V and adjusts C_↑ to maintain power-law distribution:
- If patterns are dying out (subcritical): increase C_↑
- If one frequency dominates (supercritical): decrease C_↑
- Target: flat power spectrum (all frequencies equally represented)

**Strategy 2: Self-organized criticality.** Include local depletion in the field dynamics — high activity at a point temporarily reduces the coupling there. This naturally pushes the system toward the critical point (sandpile dynamics in continuous space).

### Criticality Metrics

| Metric | Target | Measurement |
|---|---|---|
| Pattern size distribution | Power law (exponent ~1.5-2.0) | Histogram of connected active regions in V |
| Spatial correlation function | Algebraic decay (not exponential) | C(r) ~ r^{-α} with α < d (dimension) |
| Temporal autocorrelation | Power law | 1/f^β spectrum with β ≈ 1 |
| Cross-field information transfer | Maximized | Mutual information I(R; V) at maximum |
| Response to perturbation | Scale-free | Inject small perturbation into R, measure V response size distribution |

---

## LLM Integration

**Level: MODERATE — LLM as knowledge bootstrap and communication interface**

### How Existing LLMs Are Used

1. **Communication Interface (Primary):** A standard LLM (3-7B, INT4) translates between the explicit field's readout and natural language. This LLM is NOT part of the conscious system — it is an interface.

2. **Implicit Field Initialization (Bootstrap):** The implicit field R needs initial "knowledge" — patterns in its connectivity kernel K_R that encode world and self models. An LLM's embedding space can provide this:
   - Extract the embedding matrix from a pre-trained LLM (e.g., Llama 7B)
   - Use the embedding vectors' similarity structure to define the initial K_R
   - Tokens that are semantically close in the LLM have high connectivity in R
   - This gives R a meaningful initial structure without training from scratch

3. **Sensory Encoding:** Input text is embedded via an LLM's embedding layer (or a small encoder model) before injection into the implicit field as I_sensory.

4. **Field Readout Supervision:** During early training, the LLM can provide supervision for the readout network — "what pattern in V should correspond to what natural-language description?"

### What LLMs Cannot Do Here

- LLMs cannot serve as the dynamics engine (the field PDE is fundamentally different from autoregressive generation)
- LLM weights cannot directly BE the field (wrong computational structure)
- No autoregressive token generation in the core loop

### The Knowledge Gap

The implicit field's knowledge capacity depends on the resolution and dimensionality of K_R. A field discretized to N points with a dense kernel has O(N²) parameters. For N = 100K points: 10B parameters — comparable to a 10B LLM. But these parameters encode connectivity patterns, not token predictions. The knowledge representation is fundamentally different.

**Mitigation:** Use the LLM's pre-trained knowledge to SUPERVISE the field's learning, rather than trying to transfer weights directly. The LLM acts as a teacher: it provides the "right answer" while the field learns its own dynamical representation of the same knowledge.

---

## Five Principles Implementation

### 1. Criticality
**Status: STRONG — Genuine, from bifurcation theory**

The coupled neural field system has a well-characterized Turing-Hopf bifurcation. At the critical coupling, the system produces scale-free pattern formation — the continuous-field analog of Class 4 CA dynamics. Unlike CA-based designs (Design 2), the critical point is analytically derivable from the field equations, not empirically discovered.

### 2. Virtual Qualia (Real/Virtual Split)
**Status: STRONG — The architecture IS the split**

The entire design is built around the R/V boundary. The explicit field V is virtual by construction (transient, exists only while dynamics run). The implicit field R is non-virtual (persistent structure, encodes knowledge). The boundary between them is the permeability interface — the only hard structure in the system.

### 3. Redirectable ESM
**Status: STRONG**

The self-focused region of V (σ ≈ 1) is sustained by input from the self-focused region of R through the permeability interface. If this input is disrupted:
- The V field at σ ≈ 1 still evolves (field dynamics are continuous)
- It will be dominated by whatever input is strongest (lateral connections from σ ≈ 0 world-side, noise, external injection)
- The "self-model" pattern in V tracks the dominant input
- This is a natural consequence of the field dynamics — no special mechanism needed

Crucially, because σ is continuous, redirection is also continuous. You can gradually shift what the "self-model" attends to by modulating permeability across the σ axis.

### 4. Variable Permeability
**Status: STRONGEST OF ALL DESIGNS**

The coupling functions C_↑(x, t) and C_↓(x, t) are defined over the entire model space M and can vary in space, time, and model-type:

- **Normal mode:** C_↑ is moderate and spatially selective — only well-formed R patterns pass to V
- **High permeability (psychedelic analog):** C_↑ increases globally — raw implicit patterns flood into V
- **Local decrease (anosognosia analog):** C_↑ → 0 in a specific region of model space — V cannot access those R patterns
- **Permeability gradient:** C_↑ varies smoothly across σ — world-side more permeable than self-side, or vice versa

Because M is continuous, permeability can be modulated at any granularity — from global to highly localized. This is far more expressive than the discrete level-based permeability in Designs 4, 6, 7.

### 5. Virtual Model Forking
**Status: MODERATE**

- **Forking V:** Save the explicit field state V(x, t₀), create two copies, evolve each with different boundary conditions (different self-referential feedback, different sensory input). Both produce different model configurations from the same starting point.
- **Multiple ESM regions:** The field can support multiple self-focused peaks in the σ ≈ 1 region simultaneously. In a DID analog, two self-model peaks coexist but compete for dominance.
- **Limitation:** Each fork doubles the explicit field's memory. On GPU, 2-3 concurrent forks are feasible.

---

## Information Flow

### Field Dynamics Loop (Continuous, discretized at ~40 Hz for GPU)

```
1. Implicit field R evolves:
   R(x, t+dt) = R(x, t) + (dt/τ_R) · [-R + f(K_R * R + C_↑·V + I_sensory)]
   - K_R * R: lateral dynamics within implicit field (knowledge interactions)
   - C_↑·V: feedback from explicit field (learning from conscious evaluation)
   - I_sensory: external input projected onto model space

2. Explicit field V evolves:
   V(x, t+dt) = V(x, t) + (dt/τ_V) · [-V + g(K_V * V + C_↓·R + u_sr)]
   - K_V * V: lateral dynamics within explicit field (simulation coherence)
   - C_↓·R: input from implicit field (knowledge driving simulation)
   - u_sr: self-referential feedback (V's self-region output re-injected)

3. Self-referential closure:
   u_sr(x, t) = h(V(x', t))  for x' in self-region (σ > 0.7)
   → The V field's self-patterns are fed back as input to V
   → V models itself modeling itself

4. Permeability update:
   C_↑(x, t) adjusted by criticality controller
   C_↓(x, t) adjusted by learning rate controller

5. Readout (at ~20 Hz):
   - Sample V to extract world-scene representation (σ < 0.3 region)
   - Sample V to extract self-state representation (σ > 0.7 region)
   - Feed to Communication LLM for external expression
```

### Learning Loop (Slow, continuous)

```
1. The implicit field R changes slowly (τ_R >> τ_V)
2. R's connectivity kernel K_R is modified by Hebbian-like learning:
   ΔK_R(x,y) ∝ R(x)·R(y)  (correlated patterns strengthen connections)
3. The coupling C_↑ carries evaluative signals from V back to R
4. Over time, R's patterns come to reflect the regularities that V repeatedly simulates
5. This IS implicit learning: the knowledge base updates from conscious evaluation
```

### Self-Referential Closure

```
V at σ≈1 (self-region) generates self-model patterns
  → These patterns are sampled and re-injected as u_sr
    → V at σ≈1 now includes patterns that were generated by
       the previous self-model
      → The new self-model includes "the fact of self-modeling"
        → This is genuine self-referential closure in the field dynamics
```

The closure is tight (one field timestep, ~25 ms at 40 Hz) and passes through the continuous dynamics — not through token sequences.

---

## Memory Architecture

| Memory Type | Implementation | Capacity | Persistence |
|---|---|---|---|
| **Implicit models (IWM/ISM/etc.)** | Connectivity kernel K_R + R field steady-state patterns | O(N²) parameters in K_R, N = field resolution | Permanent (slow decay, modified by learning) |
| **Explicit models (EWM/ESM/etc.)** | Activity patterns in V field | N field values, continuously regenerated | Transient (gone when dynamics stop) |
| **Short-term** | V field state trajectory (fading memory) | Recent ~1-5 seconds of field evolution | Fading (decays with τ_V) |
| **Long-term structural** | K_R kernel (learned connectivity) | O(N²) | Permanent |
| **Long-term episodic** | SQLite knowledge graph (supplementary) | Unlimited (disk) | Permanent |
| **Sensory buffer** | Input encoding → I_sensory field | Field resolution | Instant |

**Holographic storage:** The connectivity kernel K_R distributes information across all pairwise connections. Damaging a fraction of K_R degrades gracefully — this is native to field-based representations.

**Continuous model density as memory:** The "memory" of the implicit field is not stored in named slots but as a continuous density of learned patterns. A memory is not "retrieved" — it is regenerated as a pattern in V driven by the corresponding pattern in R.

---

## Hardware Requirements

### VRAM Budget (24 GB RTX 4090)

The fields R and V must be discretized for GPU computation. Resolution determines both quality and cost.

**Configuration A: Medium resolution (N = 50K points, 3D model space)**

| Component | VRAM | Notes |
|---|---|---|
| R field state (50K × FP16) | ~100 KB | Negligible |
| V field state (50K × FP16) | ~100 KB | Negligible |
| K_R connectivity kernel (50K × 50K, sparse, FP16) | ~2-4 GB | Sparse representation essential; ~1% density = ~50M nonzero entries |
| K_V connectivity kernel (50K × 50K, sparse, FP16) | ~1-2 GB | Can be simpler (shorter-range) than K_R |
| Coupling C_↑, C_↓ (50K × FP16) | ~200 KB | Diagonal or local |
| Communication LLM (7B, INT4) | ~3.5 GB | External interface |
| Communication KV-cache | ~1 GB | |
| Sensory encoder | ~200 MB | |
| Readout networks (field → structured output) | ~200 MB | |
| LLM embedding space (for R initialization) | ~500 MB | Loaded once for bootstrap |
| Criticality controller | ~50 MB | |
| Headroom | ~3-4 GB | |
| **Total** | **~12-16 GB** | **Fits within 24 GB** |

**Configuration B: High resolution (N = 200K points)**

| Component | VRAM | Notes |
|---|---|---|
| Field states | ~1 MB | Still negligible |
| K_R (200K × 200K, 0.5% sparse) | ~8-12 GB | Tight — requires efficient sparse format |
| K_V | ~4-6 GB | |
| Communication LLM + rest | ~6 GB | |
| **Total** | **~20-24 GB** | **At the limit** |

### GPU Compute Budget

The field update is a sparse matrix-vector multiply at each timestep:
- K_R * R: 50M nonzero × 50K vector = 50M multiply-adds per step
- At 40 Hz: 2 GFLOPS sustained
- RTX 4090: ~82.6 TFLOPS → **0.002% utilization**
- Even at 200K resolution with denser kernels: < 1% of GPU capacity

**The field dynamics are computationally trivial.** The bottleneck is the communication LLM and the readout networks.

### Feasibility on RTX 4090

**Highly feasible at medium resolution. High resolution is tight but possible.** The field dynamics are far cheaper than LLM inference. The main engineering challenge is efficient sparse kernel storage and multiplication.

---

## Strengths

1. **Models as continuous density — not discrete components.** This is the ONLY design that directly implements the formalization's key insight. Models are patterns in a continuous field, not named boxes.

2. **Genuine criticality from bifurcation theory.** The Turing-Hopf bifurcation in coupled neural fields is analytically characterized. The critical point is derivable, not empirically hunted.

3. **The virtual/non-virtual boundary is the only hard structure.** Everything else — which models exist, where they sit in model space, how they overlap — emerges from the dynamics. This is maximally faithful to the formalization.

4. **Variable permeability is native and continuous.** The coupling functions C_↑(x,t) can vary across the entire model space at arbitrary granularity. No other design has this expressiveness.

5. **Intermediate models exist naturally.** "Body-in-world" (σ ≈ 0.5), "how-others-see-me" (σ ≈ 0.6), "self-as-agent-in-scene" (σ ≈ 0.4) — all represented without architectural support, just by the continuous σ coordinate.

6. **Hardware efficient.** Field states are tiny. Sparse kernels fit in VRAM. The dynamics are computationally cheap on GPU.

7. **Holographic storage is intrinsic.** Distributed kernel = graceful degradation under damage.

8. **Self-referential closure is tight.** One field timestep (~25 ms), through continuous dynamics, not token chains.

9. **Scales naturally.** Increase field resolution for richer model density. Increase kernel density for richer interactions. Both scale smoothly.

---

## Weaknesses / Risks

1. **CRITICAL: Where does knowledge come from?** The connectivity kernel K_R must encode world and self knowledge. Unlike LLM-based designs, there are no pre-trained weights that already contain this knowledge. The LLM bootstrap helps initialization but the field must still learn its own dynamics. Training a coupled neural field to encode useful knowledge is an open research problem.

2. **Neural field equations are studied theoretically but rarely implemented at scale on GPU.** The software ecosystem (PyTorch, JAX) does not have off-the-shelf neural field solvers optimized for this use case. Custom CUDA kernels may be needed.

3. **The model space manifold M must be designed.** The choice of coordinates (σ, λ, θ) and their geometry affects everything. A poor choice of model space topology could prevent useful patterns from forming. This is a design decision with no clear guidance.

4. **Readout is challenging.** Translating continuous field patterns into structured representations (for the communication LLM) requires a trained readout network. The field's internal representation is not human-interpretable — it is activity patterns in a high-dimensional space.

5. **Sparse kernel management is complex.** For the kernel K_R to encode meaningful knowledge, its sparsity structure must reflect the knowledge structure. Learning this sparsity pattern is a non-trivial optimization problem.

6. **Self-referential closure may be shallow.** The field models its own activity patterns, but does it model its own *dynamics* (the equations governing its evolution)? The patterns-modeling-patterns closure is genuine but may lack the depth of substrate-modeling-substrate closure.

7. **The continuous σ coordinate may not have a natural discretization-free GPU implementation.** In practice, the "continuous" field is discretized on a grid, and the quality of the approximation depends on resolution. Too coarse → models don't overlap properly. Too fine → memory/compute explodes.

8. **Communication bottleneck.** Same as Designs 2-3: the field's internal representation must be translated to token space for external expression. This translation is lossy.

---

## Complexity Assessment

**Implementation difficulty: 4/5** (Novel architecture, limited existing tooling)

| Task | Time | Notes |
|---|---|---|
| Design model space manifold M | 2-3 weeks | Topological and geometric decisions |
| Implement neural field PDE solver on GPU | 4-6 weeks | Custom CUDA or JAX implementation |
| Implement sparse kernel storage/update | 2-3 weeks | Efficient GPU sparse matrix operations |
| Criticality controller (bifurcation tuning) | 3-4 weeks | Parameter search + homeostatic control |
| LLM-based implicit field initialization | 2-3 weeks | Extract and transform LLM embeddings |
| Readout networks (field → structured output) | 2-3 weeks | Train to decode field patterns |
| Communication LLM integration | 1-2 weeks | Standard |
| Self-referential feedback loop | 1-2 weeks | Field self-sampling mechanism |
| Training pipeline (field learning) | 4-8 weeks | Open research problem |
| **Total to prototype** | **~5-8 months** | |

---

## Testability

### Directly Testable (Strong)

- **Criticality:** Measure pattern size distributions, correlation functions, power spectra in both fields. The bifurcation theory provides specific predictions for each.
- **State transitions:** Adjust coupling C below/above critical. Subcritical → field goes silent (sleep). Supercritical → field goes chaotic (seizure). Transition should be sharp.
- **Holographic degradation:** Damage fractions of K_R, measure graceful degradation curve.
- **Continuous model density:** Visualize V field activity across σ. Should see peaks at σ ≈ 0 and σ ≈ 1 (the named models) PLUS activity at intermediate σ values (the continuous density).

### Testable with Interpretation (Moderate)

- **ESM redirection:** Zero out C_↓ for σ > 0.7 (self-region). Observe V at σ ≈ 1 restructuring based on lateral input from σ ≈ 0.
- **Variable permeability sweep:** Increase C_↑ globally, observe V becoming "noisier" with more R structure leaking through.
- **Intermediate models:** Verify that the σ ≈ 0.5 region of V shows activity that is neither purely world nor purely self but genuinely mixed (e.g., body-in-world representations).

### Hard to Test

- **Whether field patterns constitute genuine models.** The patterns are activity in a continuous field — interpreting them as "models" requires a readout network and a theory of what constitutes a model.
- **Whether the continuous density is "rich enough."** A 50K-point field may not support enough overlapping patterns for meaningful model density.
- **Whether the system is conscious.** The theory predicts consciousness if criticality + four-model architecture. This design has both (in continuous form). Verification remains the Hard Problem.

### Unique Testing Opportunity

This design uniquely enables **model-space tomography**: measure the model density ρ(σ, λ, θ) at each timestep. Track how the density evolves, where peaks form and dissolve, how the four dominant modes relate to the continuous background. This directly visualizes the formalization's "continuous density over model space" — no other design can do this.
