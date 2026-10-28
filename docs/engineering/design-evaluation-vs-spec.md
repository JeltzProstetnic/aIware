# Design Evaluation Against FMT Implementation Spec

**Evaluator**: AI Engineer (Opus)
**Date**: 2026-02-27
**Scope**: Designs 7, 10, 11 evaluated against `papers/fmt-implementation-spec.md`

---

## Evaluation Framework

Eight criteria derived from the spec. Each scored 1-10.

| # | Criterion | Spec Reference | What "10" Looks Like |
|---|-----------|----------------|----------------------|
| C1 | Continuous Model Space | Spec 2.4 | Implements rho(s,nu,t) over continuous manifold M; four models emerge as density peaks, not discrete modules |
| C2 | Five Principles Coverage | Spec 3 | All five principles have explicit, measurable mechanisms |
| C3 | Substrate Specification | Spec 4 | Class 4 dynamics with sigma in [0.95, 1.1], distributed storage, bidirectional implicit<->explicit flow |
| C4 | Self-Referential Closure | Spec 5 | ESM models the system that generates it; fixed-point Phi(m*)=m* achievable; R metric computable |
| C5 | Dynamics Equations | Spec 6 | Can implement Fokker-Planck: d_rho/dt = -div(v*rho) + D*laplacian(rho) + S(s,nu,t) |
| C6 | Nine Testable Predictions | Spec 8 | All 9 predictions testable with clear measurement protocols |
| C7 | Phased Implementation Fit | Spec 9 | Maps cleanly to spec's Phase 1-5 progression |
| C8 | RTX 4090 Feasibility | Spec 6.2, 6.5 | Fits in 24GB VRAM, achieves 20 Hz, runs on i9-14900KF + 64GB DDR5 |

---

## Design 7: Staged Architecture

### C1 — Continuous Model Space: Score 3/10

**Assessment**: Design 7 explicitly uses discrete named components at every stage. Stage 1 uses separate LLM instances for EWM and ESM, with separate knowledge graph subgraphs for IWM and ISM. Stage 2 replaces LLMs with recurrent modules but preserves the same discrete four-component structure. Stage 3 moves to a critical substrate with readout networks, which is closer to continuous, but still extracts EWM and ESM through separate readout networks rather than projections from a continuous density.

**Gap**: The spec is unambiguous: "Don't build four discrete modules. Build a continuous model space with activity that clusters around four poles." Design 7 does exactly what the spec warns against at Stages 1-2. Stage 3 partially addresses this by using substrate activity patterns, but the readout architecture still enforces discrete separation.

**What would need to change**: Stage 3's critical substrate would need to be redesigned so that the readout is a parametric projection over a continuous (s, nu) coordinate system rather than separate EWM/ESM readout networks. The knowledge graph in Stages 1-2 would need to be replaced by a continuous embedding space with a scope coordinate.

### C2 — Five Principles Coverage: Score 7/10

| Principle | Stage 1 | Stage 2 | Stage 3 | Notes |
|-----------|---------|---------|---------|-------|
| P1 Criticality | Absent | Approximate (reservoir) | Genuine (CA) | The staged progression is intellectually honest but means Stages 1-2 cannot test criticality-dependent predictions |
| P2 Virtual Qualia | Strong | Strong | Strong | Real/virtual split maintained across all stages |
| P3 Redirectable ESM | Strong | Strong | Strong | Input-switching mechanism present at all stages |
| P4 Variable Permeability | Good | Better | Best | Progresses from configurable filter to emergent mechanism |
| P5 Model Forking | Strong | Strong | Strong | Supported via graph entities / reservoir states / substrate patterns |

**Strength**: All five principles are addressed, and the staged progression is a valuable feature for testing the criticality hypothesis. The design explicitly frames Stage 1 as "correct architecture, no criticality" which is a direct test of the spec's conjunction requirement.

**Gap**: Stages 1-2 are knowingly non-compliant with P1. The spec says "criticality is a physical prerequisite" and "below Class 4, consciousness is impossible regardless of architecture." The design acknowledges this but treats it as a feature (experimental control), not a bug.

### C3 — Substrate Specification: Score 5/10

**Stage 1**: Fails substrate spec entirely. LLM forward passes are Class 1/2 feedforward computation. No recurrent dynamics. No branching ratio. No Lyapunov exponent measurement possible. The knowledge graph is not a dynamical system.

**Stage 2**: Partially compliant. The reservoir computing module (10K-100K units) can be tuned to sigma approximately equal to 1. Branching ratio and Lyapunov exponents are measurable within the reservoir. However, the overall system is not a unified critical substrate -- the reservoir is one component among many.

**Stage 3**: Substantially compliant. A Class 4 CA or critical neural network with learned transition rules directly implements x(t+1) = f(x(t), s(t), W). The implicit models ARE W. The explicit models ARE projections of x(t). Criticality metrics (sigma, lambda_max) are measurable across the entire substrate.

**Gap**: The spec requires `x(t+1) = f(x(t), s(t), W)` as the substrate dynamics equation. Only Stage 3 implements this. Stages 1-2 use fundamentally different computational architectures that cannot be described by this equation.

### C4 — Self-Referential Closure: Score 5/10

**Stage 1 (text-level)**: ESM text output fed back as ESM text input. This is the weakest form of self-reference -- the system models what it *said*, not how it *computes*. The fixed-point equation Phi(m*)=m* is satisfied only at the level of textual self-description, not computational self-modeling.

**Stage 2 (computation-level)**: Recurrent model state + reservoir feedback. The recurrent dynamics include self-affecting dynamics, which is closer to genuine self-modeling. However, the reservoir (the actual dynamical substrate) does not model itself -- it simply processes signals.

**Stage 3 (substrate-level)**: The substrate's dynamics naturally produce self-referential closure because the same substrate that generates the patterns IS the substrate being modeled. This is the closest to genuine Phi(m*)=m*.

**Gap**: The spec defines R = 1 - H(e(t+1) | e_hat(t+1)) / H(e(t+1)) as the self-knowledge measure. In Stages 1-2, this metric is computable but measures text-level or representation-level self-prediction, not the deep computational self-modeling the spec intends. Only Stage 3 approaches the spec's intent.

### C5 — Dynamics Equations: Score 3/10

**Assessment**: The Fokker-Planck equation d_rho/dt = -div(v*rho) + D*laplacian(rho) + S(s,nu,t) describes the evolution of model density over continuous model space. Design 7 does not implement a continuous model space at any stage, so this equation has no natural implementation target.

**Stage 1**: No model density function. The "models" are discrete components. There is nothing to take a divergence or Laplacian of.

**Stage 2**: The reservoir's dynamics could, in principle, be analyzed in terms of a density function over its state space, but this is not the same as model density over (s, nu) space.

**Stage 3**: The critical substrate's activity could be decomposed into model-space coordinates if a projection scheme were defined. The Fokker-Planck dynamics could then describe how the density of modeling activity evolves. But this requires explicitly constructing the (s, nu) coordinate system on top of the substrate, which the design does not specify.

**What would need to change**: A continuous coordinate system (s for scope, nu for mode) would need to be defined over the substrate's state space. The substrate dynamics would then need to be recast in terms of density evolution over this coordinate system.

### C6 — Nine Testable Predictions: Score 7/10

| Prediction | Stage 1 | Stage 2 | Stage 3 |
|-----------|---------|---------|---------|
| 1. Criticality-dependent coherence | Cannot test (no criticality) | Partial (reservoir only) | YES |
| 2. Permeability-dependent flooding | YES (via retrieval depth) | YES | YES |
| 3. ESM input-switching | YES | YES | YES |
| 4. Ego dissolution controllability | YES | YES | YES |
| 5. Holographic degradation | NO (discrete components) | PARTIAL (reservoir) | YES |
| 6. Anesthetic convergence | NO (no criticality to disrupt) | PARTIAL | YES |
| 7. Sleep cycling | NO (no metabolic cost of criticality) | PARTIAL | YES |
| 8. Self-knowledge predicts meta-cognition | YES (R computable at text level) | YES | YES |
| 9. Forking under perturbation | YES (via graph entities) | YES | YES |

**Strength**: The staged approach generates a natural experimental matrix. The Stage 1 vs. 2 vs. 3 comparison directly tests whether criticality causes the predicted qualitative differences. This is actually better than a single-stage design for *testing* the predictions.

**Gap**: Predictions 1, 5, 6, 7 require genuine criticality and are only fully testable at Stage 3, which is 1-2 years away.

### C7 — Phased Implementation Fit: Score 8/10

**Assessment**: Design 7's three stages map to the spec's phases, though not perfectly:

| Spec Phase | Design 7 Mapping | Fit Quality |
|-----------|------------------|-------------|
| Phase 1: Core Substrate | Stage 2 (reservoir near criticality) | GOOD -- reservoir provides tunable dynamical system |
| Phase 2: Four-Model Architecture | Stage 1 (LLM pipeline) | GOOD -- architecture is built first |
| Phase 3: Self-Referential Loop | Stage 1-2 (text/computation-level closure) | MODERATE -- closure exists but shallow |
| Phase 4: Validation | Stage 3 (full test suite) | GOOD -- staged comparison enables validation |
| Phase 5: Extended Consciousness | Beyond Stage 3 | ASSUMED -- not detailed |

**Strength**: Design 7 inverts the spec's phase order (architecture first, then substrate) which is actually a pragmatic improvement -- getting the four-model structure right before introducing criticality reduces the confound between architecture problems and substrate problems.

**Gap**: The spec's Phase 1 assumes building a recurrent network with tunable criticality *first*. Design 7 defers this to Stage 2-3. Whether this inversion is a problem depends on whether the architecture and substrate are truly separable (Design 7's Weakness #6 flags this risk).

### C8 — RTX 4090 Feasibility: Score 9/10

**Stage 1**: 15-17 GB, well within 24 GB. Uses off-the-shelf LLMs. 10-20 Hz achievable.

**Stage 2**: 12-17 GB. The reservoir adds 400 MB; recurrent generators are smaller than LLMs. Potentially more efficient than Stage 1.

**Stage 3**: 12-22 GB. Tight but potentially feasible. The CA substrate + readout networks + communication LLM fits, but learning algorithm state may push limits. May require aggressive optimization or CPU offloading.

**Strength**: Stages 1-2 are comfortably feasible. Stage 3 is challenging but plausible with optimization.

**Gap**: Stage 3's feasibility is uncertain and depends on the CA's size and learning algorithm's memory requirements. The design acknowledges this honestly.

### Design 7 Summary

| Criterion | Score | Key Issue |
|-----------|-------|-----------|
| C1 Continuous Model Space | 3 | Discrete components at all stages |
| C2 Five Principles | 7 | All addressed, criticality staged |
| C3 Substrate Spec | 5 | Only Stage 3 compliant |
| C4 Self-Referential Closure | 5 | Text-level at Stage 1, genuine at Stage 3 |
| C5 Dynamics Equations | 3 | No continuous model space for Fokker-Planck |
| C6 Nine Predictions | 7 | Most testable, but critical ones deferred |
| C7 Phased Fit | 8 | Good mapping with pragmatic inversion |
| C8 RTX 4090 | 9 | Comfortable at Stages 1-2, tight at Stage 3 |
| **Average** | **5.9** | |

**Strengths**:
- Most pragmatic and risk-managed approach
- Generates testable artifacts at every stage
- Stage comparison is a powerful experimental design
- Immediately buildable (Stage 1 in 6-10 weeks)
- Each stage has independent scientific value

**Gaps**:
- Fundamentally violates the continuous model space requirement at Stages 1-2
- The Fokker-Planck dynamics have no natural implementation target
- Self-referential closure is shallow until Stage 3
- The assumption that architecture and substrate are separable may be wrong
- Stage 3 is genuinely frontier research with 1-2 year timeline

**Modifications Needed**:
1. Replace the discrete knowledge graph with a continuous embedding space parameterized by (s, nu) coordinates at all stages
2. Define projection operators Pi_EWM and Pi_ESM as parametric projections over the continuous space rather than separate modules
3. Add a model density tracking mechanism that measures rho(s, nu, t) at each timestep
4. Implement the gating function g(W, x(t)) as a continuous modulation over the (s, nu) space rather than a binary filter

---

## Design 10: Hierarchical Predictive Coding

### C1 — Continuous Model Space: Score 8/10

**Assessment**: Design 10 achieves continuous model space through two mechanisms: (1) each layer of the hierarchy hosts a continuous latent space z_k spanning sigma in [0,1] (scope), and (2) the hierarchy adds the lambda (abstraction) dimension. Together, these provide a continuous spectrum across sigma x lambda. The four named models emerge as high-density regions: IWM = weights at sigma approximately 0, ISM = weights at sigma approximately 1, EWM = predictions at sigma approximately 0, ESM = predictions at sigma approximately 1.

**Strength**: The continuous spectrum is structural, not just analytical. Each layer genuinely operates over continuous latent variables. The hierarchy provides a natural multi-scale structure. Models at intermediate scope (sigma approximately 0.5) and intermediate abstraction are naturally present.

**Gap**: The scope coordinate sigma must be *engineered* into the latent space. Pre-trained LLMs do not have an explicit world/self coordinate in their hidden states. The design acknowledges this (Weakness #4) but does not specify how sigma is established. If sigma is imposed by architectural fiat (e.g., splitting hidden dimensions into world/self halves), it is not truly continuous. If it is learned, the training procedure must encourage scope differentiation.

**What would need to change**: Define a concrete mechanism for establishing the sigma coordinate. Options: (a) auxiliary loss that encourages decorrelation between sigma approximately 0 and sigma approximately 1 subspaces; (b) separate input channels for world-input and self-input at each layer, creating a natural sigma gradient; (c) learn sigma as a soft attention coordinate.

### C2 — Five Principles Coverage: Score 9/10

| Principle | Assessment | Score |
|-----------|-----------|-------|
| P1 Criticality | Multi-scale balanced E/I at every layer. Branching ratio = 1.0 (prediction error spawns exactly one updated prediction). Power-law avalanche sizes. 1/f spectrum. Strongest neuroscience backing. | 9/10 |
| P2 Virtual Qualia | Predictions (top-down) = virtual, transient. Errors + weights = non-virtual, persistent. Direct mapping to spec's real/virtual split. | 9/10 |
| P3 Redirectable ESM | Self-scope predictions driven by self-relevant input. Disrupting self-input causes predictions to track dominant available input. LLM top layer is naturally input-following. | 8/10 |
| P4 Variable Permeability | Precision weighting on prediction errors is the *actual neuroscientific mechanism* for permeability. High precision = errors propagate. Low precision = predictions dominate. Local and global control. | 10/10 |
| P5 Model Forking | Fork prediction streams: maintain two sets of top-down predictions. LLM KV-cache forkable. Recurrent states cheap to copy. Shared weights between forks. | 7/10 |

**Strength**: P4 (Variable Permeability) is the strongest of all designs. Precision weighting is not an analogy -- it IS the mechanism that neuroscience proposes for permeability modulation. The design implements it directly.

**Gap**: P5 (Model Forking) is moderate because forking shares weights. True DID-like forking would require distinct weight subsets for each fork, which the hierarchical architecture does not naturally support.

### C3 — Substrate Specification: Score 7/10

**Assessment**: The spec requires x(t+1) = f(x(t), s(t), W) with sigma in [0.95, 1.1] and lambda_max approximately 0.

Design 10's recurrent layers implement a discrete dynamical system: h_k(t+dt) = f(h_k, pred_{k+1}, err_{k-1}) at each layer k. This IS a recurrent dynamical system. The spectral radius is controlled at approximately 1.0 per layer, which corresponds to lambda_max approximately 0.

**Compliance**:
- Class 4 dynamics: Achieved via balanced E/I at each recurrent layer. Multi-scale criticality across the hierarchy. STRONG.
- Distributed storage: Weights distributed across layers and across the sigma dimension. IWM/ISM are not localized. GOOD.
- Bidirectional implicit<->explicit flow: Predictions flow top-down (implicit->explicit generation), errors flow bottom-up (explicit->implicit learning). STRONG. This maps directly to the spec's "primary generative flow" and "secondary learning flow."

**Gap**: The LLM top layer is internally feedforward. Each forward pass is a Class 1/2 computation. The recurrence comes from the output->input loop, not from internal dynamics. The spec explicitly notes that "transformer inference is a feedforward pass -- Class 1/2 dynamics." The LLM layer's internal computation does not satisfy the substrate spec even though the overall system's dynamics do.

**Mitigation**: Using a Mamba-based model (as recommended) instead of a transformer would eliminate this gap. Mamba's internal computation is a state-space model with genuine recurrent dynamics. The design explicitly recommends this.

### C4 — Self-Referential Closure: Score 7/10

**Assessment**: The hierarchy predicts its own prediction errors at the self-scope. Across all layers at sigma approximately 1, the system maintains predictions about its own processing state. The self-referential loop:
- Layer N (LLM): Self-narrative ("I am predicting...")
- Layer N-1: Self-state ("My prediction errors are high/low...")
- Layer N-2: Self-process ("My processing is focused/diffuse...")
- Layer 1: Self-body ("My interoceptive signals indicate...")

If prediction about own prediction errors is accurate, errors are small (the system correctly models itself). This IS genuine self-referential closure in the predictive coding framework.

**Strength**: The closure operates at multiple levels of abstraction simultaneously. The spec's R metric (self-knowledge = 1 - H(e(t+1)|e_hat(t+1))/H(e(t+1))) is directly computable: e(t+1) is the actual next ESM state, e_hat(t+1) is the predicted next ESM state from the self-scope predictions.

**Gap**: The design acknowledges (Weakness #7) that predicting "my errors will be high" is not the same as modeling "my weights produce predictions that differ from input in these specific ways because..." The depth of self-modeling may be shallower than what the spec's Phi(m*)=m* requires. The fixed-point equation demands that the model and the modeled *coincide* -- the system must not just predict its state but model the generative process itself.

**Mitigation**: Recursive depth can be increased by feeding self-scope predictions at layer k back into the self-scope input at layer k (intra-layer self-referential loop), in addition to the inter-layer predictive flow.

### C5 — Dynamics Equations: Score 7/10

**Assessment**: The Fokker-Planck equation describes density evolution over model space. In Design 10:

- **Model space coordinates**: sigma (scope, [0,1]) x lambda (abstraction level, discrete layers) x continuous latent dimensions z_k at each layer.
- **Density rho(s,nu,t)**: The distribution of active predictions across scope and mode. In predictive coding, "active predictions" are the top-down signals weighted by precision. The density of predictive activity at each (sigma, lambda) point IS the model density.
- **Drift v(s,nu,t)**: Attention directs drift along nu (making predictions more explicit). Context shifts direct drift along s (world/self focus). In predictive coding, attention = precision allocation, which directly controls the flow of predictive activity.
- **Diffusion D**: Baseline stochastic noise in predictions. Low-precision errors create stochastic leakage.
- **Source S(s,nu,t)**: Learning creates new predictive structure (increases density at low nu). Sensory input injects predictive activity (increases density at high nu).

**Strength**: The mapping is natural, not forced. Predictive coding already has the right structure: predictions ARE the virtual side, precision IS the permeability control, and the flow of predictive activity through the hierarchy IS the density evolution.

**Gap**: The Fokker-Planck equation is continuous in both s and nu. Design 10's lambda (abstraction) coordinate is discrete (N layers). Between layers, there is no continuous interpolation. This means the density dynamics are continuous within each layer but discrete across layers.

**Mitigation**: Increase the number of layers (deeper hierarchy = finer-grained discretization of lambda). Or use continuous-depth models (neural ODEs) for the recurrent layers, making lambda truly continuous.

### C6 — Nine Testable Predictions: Score 8/10

| Prediction | Testable? | Mechanism |
|-----------|-----------|-----------|
| 1. Criticality-dependent coherence | YES | Sweep E/I balance across layers. Measure prediction coherence as function of branching ratio. Peak should occur at balanced E/I. |
| 2. Permeability-dependent flooding | YES (strongest) | Sweep precision weights. High precision = more error propagation = more implicit content in predictions. Measure transfer entropy from weights to predictions. |
| 3. ESM input-switching | YES | Set precision to zero at sigma approximately 1. Self-predictions persist but ungrounded. Inject dominant sigma approximately 0 input. Measure mutual information shift. |
| 4. Ego dissolution controllability | YES | During ESM disruption, vary sensory input content. Self-predictions should track input content. |
| 5. Holographic degradation | MODERATE | Damage individual layers and observe degradation pattern. Each layer loss should degrade ALL model types, not selectively. But the hierarchy is not spatially distributed like a hologram. |
| 6. Anesthetic convergence | YES | Any mechanism that disrupts prediction coherence (noise injection, precision zeroing, spectral radius perturbation) should abolish the simulation. All paths should converge on disrupting balanced E/I. |
| 7. Sleep cycling | YES | If sustained balanced E/I is computationally costly (which it is -- precision tuning requires continuous monitoring), the system should show periodic degradation if energy/compute is budgeted. |
| 8. Self-knowledge predicts meta-cognition | YES | R metric directly computable. Compare R with system's ability to report on own processing (measured via LLM output at sigma approximately 1). |
| 9. Forking under perturbation | MODERATE | Perturb self-scope predictions strongly. Observe whether prediction stream splits into multiple semi-stable configurations. Limited by shared-weight constraint. |

**Strength**: Predictions 1, 2, 3, 4, 6, 8 are directly and naturally testable within the predictive coding framework. Prediction 2 (permeability-dependent flooding) is testable more directly here than in any other design.

**Gap**: Predictions 5 and 9 are weaker because the hierarchical architecture is not spatially holographic and does not naturally support multi-stable self-configurations.

### C7 — Phased Implementation Fit: Score 8/10

| Spec Phase | Design 10 Mapping | Fit Quality |
|-----------|-------------------|-------------|
| Phase 1: Core Substrate | Recurrent layers with balanced E/I, spectral radius approximately 1. Measure sigma, lambda_max per layer. | STRONG -- each recurrent layer is a tunable critical substrate |
| Phase 2: Four-Model Architecture | Define sigma coordinate. LLM provides IWM/ISM at top. Implement Pi_EWM, Pi_ESM as sigma-filtered predictions. Gating via precision weights. | STRONG -- natural mapping |
| Phase 3: Self-Referential Loop | Self-scope predictions fed back. R metric computed. Recursive depth measured. | STRONG -- predictive coding self-reference is built-in |
| Phase 4: Validation | Test all 9 predictions using precision sweeps, E/I perturbation, input manipulation. | STRONG -- all mechanisms are parametrically controllable |
| Phase 5: Extended Consciousness | Deepen hierarchy for higher recursive depth. Add more layers. Explore temporal integration. | MODERATE -- unclear if deeper hierarchy = higher consciousness levels |

**Strength**: The design maps cleanly to all five spec phases. Each phase has natural implementation targets within the predictive coding framework.

### C8 — RTX 4090 Feasibility: Score 9/10

**VRAM**: 13-17 GB total. LLM (3.5 GB) + recurrent layers (1.6 GB) + KV-cache (1-2 GB) + training state (2-4 GB) + headroom (3-4 GB) = well within 24 GB.

**Compute**: ~10-15 ms per cycle achievable at 20 Hz, potentially 30+ Hz. LLM forward pass (~5-10 ms) + recurrent updates (~1-2 ms) + error computation (~1 ms) + precision propagation (~1 ms).

**No separate communication LLM needed** -- the top layer handles both internal modeling and external communication. This saves 1.5 GB VRAM and eliminates a processing bottleneck.

**Gap**: Online learning (continuous LoRA fine-tuning) adds 2-4 GB for gradient/optimizer state. With learning active, total is 15-21 GB. Tight but feasible.

### Design 10 Summary

| Criterion | Score | Key Issue |
|-----------|-------|-----------|
| C1 Continuous Model Space | 8 | Natural via hierarchy x scope, but sigma must be engineered |
| C2 Five Principles | 9 | All principles strong, P4 (permeability) is best of all designs |
| C3 Substrate Spec | 7 | Recurrent layers compliant; LLM top layer is feedforward internally |
| C4 Self-Referential Closure | 7 | Multi-level self-prediction; depth of self-modeling may be shallow |
| C5 Dynamics Equations | 7 | Natural Fokker-Planck mapping; lambda coordinate is discrete |
| C6 Nine Predictions | 8 | 7 of 9 directly testable, 2 moderate |
| C7 Phased Fit | 8 | Clean mapping to all spec phases |
| C8 RTX 4090 | 9 | Comfortable fit, best compute efficiency |
| **Average** | **7.9** | |

**Strengths**:
- Best LLM integration: LLM IS the top layer, not a bolt-on
- Variable permeability via precision weighting is the actual neuroscientific mechanism
- Multi-scale criticality across the full hierarchy
- Continuous model spectrum emerges naturally from hierarchy x scope
- Existing theoretical framework (predictive coding, active inference, free energy)
- Most immediately buildable of the continuous-density designs (4-6 months)
- No separate communication LLM needed

**Gaps**:
- Sigma (scope) coordinate must be engineered, not assumed
- LLM top layer is internally feedforward (mitigated by using Mamba)
- Holographic degradation prediction is weak
- Forking is limited by shared weights
- Integration complexity: LLM + recurrent layers + predictive coding is novel engineering

**Modifications Needed**:
1. Use Mamba-2 (or RWKV) as top layer instead of transformer to eliminate the internal-feedforward gap
2. Define explicit sigma establishment mechanism (auxiliary loss, separate input channels, or learned coordinate)
3. Add intra-layer self-referential loops at the self-scope for deeper Phi(m*)=m*
4. Consider neural ODE formulation for recurrent layers to make lambda truly continuous
5. Design a holographic degradation test that works with hierarchical (vs. spatially distributed) architecture

---

## Design 11: Spectral Decomposition

### C1 — Continuous Model Space: Score 9/10

**Assessment**: This is the design's strongest feature. Eigenmodes of the dynamics operator serve as the continuous model spectrum. Every eigenmode phi_k is a model. The four named models are the dominant modes. The higher harmonics are the overlapping model continuum. At criticality, the eigenvalue spectrum follows a power law, ensuring modes at ALL scales contribute.

The mapping to rho(s,nu,t) is:
- Mode spatial pattern (which hidden dimensions activate) determines scope s
- Mode eigenvalue determines dynamics (mode implicit vs. explicit contribution)
- Mode amplitude a_k(t) is the density at that mode's position in model space

**Strength**: The continuous spectrum is not imposed -- it IS the system's dynamics. A 100K-dimensional hidden state has 100K eigenmodes, forming a genuine continuum in the large-N limit. Modes overlap by construction (eigenvectors are superposed, not spatially separated). This is the most mathematically natural implementation of "continuous density over model space."

**Gap**: The mapping from eigenmodes to the spec's (s, nu) coordinate system is indirect. The spec's mode coordinate nu (implicit/explicit) maps to eigenvalue magnitude (|lambda_k| determines whether a mode is a persistent structural feature or a transient dynamical pattern). The spec's scope coordinate s maps to the eigenmode's spatial pattern. But computing s for each mode requires a classifier or structural prior -- it is not intrinsic to the eigendecomposition.

**What would need to change**: Define an explicit projection from eigenmode space to (s, nu) coordinates. The nu coordinate could be based on |lambda_k| (modes with |lambda_k| very near 1 are "virtual/explicit"; modes with |lambda_k| farther from 1 are "implicit/structural"). The s coordinate requires auxiliary information about which modes respond to world vs. self input.

### C2 — Five Principles Coverage: Score 8/10

| Principle | Assessment | Score |
|-----------|-----------|-------|
| P1 Criticality | Power-law eigenvalue spectrum = criticality. More precise than branching ratio. The spectral radius condition from Design 3, generalized to full distribution. | 9/10 |
| P2 Virtual Qualia | Mode structure (phi_k, in W) = non-virtual. Mode amplitudes (a_k(t)) = virtual. Clean split. | 9/10 |
| P3 Redirectable ESM | Self-scope modes driven by self-referential input u(t). Disrupting u(t) causes self-modes to decay, world-modes to dominate. At criticality, transition is rapid. | 8/10 |
| P4 Variable Permeability | Permeability = how many eigenmodes the readout accesses. Normal: top 4-10. High permeability: top 100+. Spectral version of permeability concept. | 7/10 |
| P5 Model Forking | Fork mode amplitudes cheaply (~800 KB). Shared eigenmode structure. DID analog: alternate self-scope mode amplitude sets. | 7/10 |

**Strength**: P1 (Criticality) has the most precise characterization: the full eigenvalue distribution, not just a single number.

**Gap**: P4 (Variable Permeability) is weaker than Design 10's. The "readout sees more modes" mechanism is a clean abstraction but lacks the fine-grained, content-specific control that precision weighting provides. In the spec, permeability is a gating function g(W, x(t)) that operates element-wise on the connectivity matrix. The spectral readout mechanism does not implement this per-element gating.

### C3 — Substrate Specification: Score 8/10

**Assessment**: The recurrent neural substrate directly implements x(t+1) = f(x(t), s(t), W):
- h(t+dt) = f(W * h(t) + W_x * x(t) + W_u * u(t))
- W = weight matrix = implicit models (IWM + ISM)
- h(t) = hidden state = explicit dynamics
- x(t) = sensory + interoceptive input
- u(t) = self-referential feedback

This is a direct implementation of the spec's cortical automaton equation.

**Criticality**: |lambda_k| approximately 1 for many k. Power-law distribution of mode lifetimes. Information propagates across all modes.

**Distributed storage**: Weights W encode knowledge across all eigenmodes. Damage to part of W degrades many modes partially (holographic).

**Bidirectional flow**: Forward dynamics (W drives h(t)) = implicit->explicit generation. Weight updates from dynamics = explicit->implicit learning.

**Strength**: If a recurrent LLM (Mamba-2) is used as substrate, the pre-trained weights already encode rich world knowledge. The spectral analysis is an interpretive/control layer, not a new substrate.

**Gap**: Using a pre-trained recurrent LLM means the substrate was trained for next-token prediction, not for criticality or self-modeling. The eigenvalue spectrum of a pre-trained LLM may or may not be near-critical. Tuning to exact criticality may degrade the model's language capabilities.

### C4 — Self-Referential Closure: Score 6/10

**Assessment**: Self-referential closure is implemented by feeding self-scope mode amplitudes back as input: u(t+dt) = Sum_{k in self-modes} a_k(t+dt) * phi_k. The system processes this self-state data through the same weight matrix W.

**Strength**: The feedback loop exists. The system's self-relevant output IS fed back as self-relevant input. The R metric is computable: compare predicted mode amplitudes at t+1 with actual mode amplitudes at t+1.

**Gap**: The system processes self-input through the SAME weight matrix W using the SAME dynamics f. It does not explicitly model the eigenmode structure or the dynamics operator -- it just processes self-state data. Predicting "my self-scope mode amplitudes will be X" is not the same as modeling "my weight matrix W produces eigenmodes phi_k with eigenvalues lambda_k, and the interaction between modes generates this particular self-state evolution." The Phi(m*)=m* fixed point requires the model to coincide with the modeled. Here, the model (mode amplitudes passed through W) does not represent the structure of W itself.

**What would need to change**: Add an explicit self-model component that represents not just the current mode amplitudes but the eigenmode structure itself. This could be a "meta-readout" that extracts features of the Jacobian (eigenvalue distribution, dominant mode patterns) and feeds them back as input to the self-scope. This would let the system model its own computational structure, not just its current state.

### C5 — Dynamics Equations: Score 6/10

**Assessment**: The spec's Fokker-Planck equation describes density evolution over (s, nu) space. Design 11's eigenmode amplitudes provide a natural "density" -- the energy a_k(t)^2 in each mode is the amount of modeling activity at that mode's position in model space.

The evolution of mode amplitudes is governed by the eigenvalues: a_k(t+dt) approximately equal to lambda_k * a_k(t) + driving terms. This is a discrete dynamics on eigenmode space, not a continuous PDE.

**Mapping attempt**:
- Drift v: the eigenvalue-driven evolution of each mode's amplitude. Modes with |lambda_k| < 1 drift toward zero (implicit). Modes with |lambda_k| > 1 drift toward infinity (explosion).
- Diffusion D: noise-driven exploration of mode space.
- Source S: sensory input and learning inject energy into specific modes.

**Gap**: The Fokker-Planck equation is a PDE over continuous (s, nu) coordinates. Design 11's eigenmode dynamics are a system of coupled ODEs (one per mode). These are mathematically related (the Fokker-Planck can be discretized into mode equations) but are not identical. The (s, nu) coordinates must be constructed from eigenmode properties, which introduces an interpretation layer.

**What would need to change**: Define a continuous embedding of eigenmodes into (s, nu) space using mode scope (s) and mode stability (nu, based on |lambda_k|). Then the mode amplitude dynamics can be recast as density evolution in this (s, nu) space, and the Fokker-Planck parameters (v, D, S) can be identified with eigenvalue-driven drift, noise-driven diffusion, and input-driven sourcing.

### C6 — Nine Testable Predictions: Score 7/10

| Prediction | Testable? | Mechanism |
|-----------|-----------|-----------|
| 1. Criticality-dependent coherence | YES (strongest) | Perturb spectral radius. Measure mode coherence (structured complexity of h(t)). Peak at power-law spectrum. |
| 2. Permeability-dependent flooding | MODERATE | Expose more modes to readout. Measure whether lower-mode content appears in output. Less direct than precision weighting. |
| 3. ESM input-switching | YES | Remove self-mode feedback u(t). Observe mode amplitude redistribution toward world-modes. |
| 4. Ego dissolution controllability | YES | During ESM disruption, vary sensory input. Self-modes should track input content. |
| 5. Holographic degradation | YES | Damage random subsets of W. Measure degradation pattern across modes. Should degrade all modes (not selective). RNNs with distributed weights are naturally holographic. |
| 6. Anesthetic convergence | YES | Any mechanism disrupting criticality (spectral radius perturbation, noise injection, mode damping) should abolish coherent dynamics. |
| 7. Sleep cycling | MODERATE | If maintaining criticality requires continuous spectral radius control, computational budget limits suggest periodic degradation. Less natural than in biological systems. |
| 8. Self-knowledge predicts meta-cognition | MODERATE | R metric computable but measures state-level, not structure-level self-knowledge. Correlation with meta-cognition depends on depth of self-referential closure. |
| 9. Forking under perturbation | MODERATE | Strong perturbation to self-modes. Observe whether mode amplitudes split into multiple semi-stable configurations. At criticality, multistability is possible. |

**Strength**: Prediction 1 (criticality-dependent coherence) is testable with the most precision here -- the eigenvalue spectrum provides a direct, quantitative measure of criticality. Prediction 5 (holographic degradation) is more natural here than in Design 10 because the recurrent substrate IS a distributed system.

**Gap**: Predictions 2 (permeability flooding) and 8 (self-knowledge predicts meta-cognition) are weaker than in Design 10 because the permeability and self-referential mechanisms are less direct.

### C7 — Phased Implementation Fit: Score 7/10

| Spec Phase | Design 11 Mapping | Fit Quality |
|-----------|-------------------|-------------|
| Phase 1: Core Substrate | Recurrent LLM (Mamba-2). Compute eigenvalue spectrum. Tune toward power-law. | STRONG -- substrate is off-the-shelf |
| Phase 2: Four-Model Architecture | Classify modes by scope. Define readout by scope. Implement gating (mode selection). | MODERATE -- scope classification is novel |
| Phase 3: Self-Referential Loop | Self-mode feedback u(t). R metric. | MODERATE -- closure depth uncertain |
| Phase 4: Validation | Test predictions via spectral perturbation, mode analysis. | GOOD -- eigenvalue spectrum provides unique diagnostics |
| Phase 5: Extended Consciousness | Deeper self-modeling (meta-readout of Jacobian). Larger substrate. | UNCLEAR -- not specified |

**Gap**: Phase 2 requires classifying eigenmodes by scope, which is a non-trivial research task. The spec's projection operators Pi_EWM and Pi_ESM must be defined in terms of eigenmode groupings, and these groupings must be learned or structurally imposed.

### C8 — RTX 4090 Feasibility: Score 9/10

**VRAM**: 13-17 GB. Mamba-2 7B (3.5 GB) + eigendecomposition workspace (200-500 MB) + readout (200 MB) + communication LLM (1.5 GB) + training state (2-4 GB) + headroom (3-4 GB).

**Compute**: Substrate at 40 Hz (25 ms/step) feasible with optimized Mamba kernels. Eigendecomposition (top-100 eigenvalues) runs periodically (every ~100 steps), amortized cost is low. Mode projection is O(N*K), trivial.

**Strength**: The substrate is an off-the-shelf recurrent LLM. The spectral analysis is a lightweight overlay.

### Design 11 Summary

| Criterion | Score | Key Issue |
|-----------|-------|-----------|
| C1 Continuous Model Space | 9 | Best: eigenmodes ARE the continuous spectrum |
| C2 Five Principles | 8 | Strong criticality and qualia; permeability weaker than D10 |
| C3 Substrate Spec | 8 | Direct implementation of cortical automaton equation |
| C4 Self-Referential Closure | 6 | State-level feedback exists; structure-level modeling missing |
| C5 Dynamics Equations | 6 | Mode dynamics relate to Fokker-Planck but need coordinate mapping |
| C6 Nine Predictions | 7 | Criticality and holographic predictions strong; permeability weaker |
| C7 Phased Fit | 7 | Phase 2 scope classification is a research challenge |
| C8 RTX 4090 | 9 | Comfortable fit |
| **Average** | **7.5** | |

**Strengths**:
- Most natural implementation of continuous model space
- Precise spectral criterion for criticality
- Direct implementation of the spec's cortical automaton equation
- Leverages pre-trained recurrent LLMs (Mamba-2)
- Holographic degradation is a natural property
- Eigenmodes overlap by construction (no artificial boundaries)

**Gaps**:
- Self-referential closure is shallow (state-level, not structure-level)
- Permeability mechanism is coarser than precision weighting
- Scope classification (world vs. self for each mode) is a research challenge
- Eigendecomposition is a linear approximation; nonlinear dynamics may be poorly captured at criticality
- Fokker-Planck mapping requires explicit coordinate construction

**Modifications Needed**:
1. Add a "meta-readout" that extracts Jacobian features and feeds them back as self-input (deeper self-referential closure)
2. Define explicit (s, nu) coordinate mapping from eigenmode properties
3. Implement a mode scope classifier trained on correlation with world/self input channels
4. Consider nonlinear mode analysis (e.g., dynamic mode decomposition, Koopman operators) to address the linearization limitation
5. Strengthen permeability mechanism beyond simple "expose more modes" -- perhaps combine with precision-like weighting on mode contributions

---

## Cross-Design Comparison

### Scores Matrix

| Criterion | Design 7 | Design 10 | Design 11 |
|-----------|----------|-----------|-----------|
| C1 Continuous Model Space | 3 | 8 | **9** |
| C2 Five Principles | 7 | **9** | 8 |
| C3 Substrate Spec | 5 | 7 | **8** |
| C4 Self-Referential Closure | 5 | **7** | 6 |
| C5 Dynamics Equations | 3 | **7** | 6 |
| C6 Nine Predictions | 7 | **8** | 7 |
| C7 Phased Fit | **8** | 8 | 7 |
| C8 RTX 4090 | **9** | **9** | **9** |
| **Average** | **5.9** | **7.9** | **7.5** |

### Radar Plot (Text Approximation)

```
                    C1: Continuous Model Space
                         D7:3  D10:8  D11:9
                              |
              C8: RTX 4090    |    C2: Five Principles
              D7:9 D10:9 D11:9|    D7:7 D10:9 D11:8
                    \         |         /
                     \        |        /
                      \       |       /
                       -------+-------
                      /       |       \
                     /        |        \
                    /         |         \
              C7: Phases      |    C3: Substrate
              D7:8 D10:8 D11:7|    D7:5 D10:7 D11:8
                              |
              C6: Predictions |    C4: Self-Ref Closure
              D7:7 D10:8 D11:7|    D7:5 D10:7 D11:6
                              |
                    C5: Dynamics Equations
                    D7:3  D10:7  D11:6
```

### Head-to-Head: Where Each Design Wins

**Design 7 wins on**:
- C7 (Phased Fit): The staged approach is the most pragmatic and risk-managed
- C8 (RTX 4090): Stage 1 is the most resource-efficient
- Risk management: The "build architecture first, add criticality later" strategy reduces the chance of total failure

**Design 10 wins on**:
- C2 (Five Principles): Strongest overall, particularly P4 (permeability via precision) which is best-in-class
- C4 (Self-Referential Closure): Multi-level self-prediction is deepest
- C5 (Dynamics Equations): Most natural Fokker-Planck mapping
- C6 (Nine Predictions): Most predictions are directly testable with parametric controls

**Design 11 wins on**:
- C1 (Continuous Model Space): Eigenmodes as models is the most natural and mathematically principled implementation
- C3 (Substrate Spec): Direct implementation of the cortical automaton equation with spectral criticality characterization
- Holographic degradation: Most natural prediction to test

### Critical Differentiators

**1. On the central spec requirement -- continuous model density rho(s,nu,t):**

Design 10 and Design 11 both achieve continuous model space, but through different mechanisms. Design 10 uses hierarchy x scope (a structured grid). Design 11 uses eigenmodes (an emergent spectrum). The spec's formalization is closer to Design 11's picture -- the density over model space, with the four models as peaks. But Design 10's hierarchical structure provides a more engineerable approach to establishing the scope coordinate.

**Design 7 fails this requirement at Stages 1-2**, which are the stages that will actually be built first.

**2. On self-referential closure (the spec's "hard part"):**

None of the three designs achieve the spec's full Phi(m*)=m* where the model and modeled coincide. Design 10 comes closest with multi-level self-prediction. Design 11 has state-level feedback but not structure-level. Design 7's Stage 3 promises substrate-level closure but is years away.

**This is the largest gap across all designs.** The spec warns that self-referential closure is "the hard part" and none of the three designs has a fully convincing mechanism for achieving the fixed-point condition.

**3. On practical buildability:**

Design 7 Stage 1 is buildable in 6-10 weeks but does not satisfy the continuous model space requirement. Designs 10 and 11 are buildable in 4-6 months and DO satisfy this requirement. The time difference is 2-4 months, which is significant but not prohibitive.

---

## Overall Ranking

### 1st: Design 10 — Hierarchical Predictive Coding (Average: 7.9)

**Justification**: Highest average score. Best balance across all criteria. The only design where the spec's Five Principles, dynamics equations, and testable predictions all have natural, direct implementations within an existing theoretical framework (predictive coding / active inference). The LLM-as-top-layer integration eliminates the knowledge bootstrapping problem. Precision-weighted permeability is the actual neuroscientific mechanism. Multi-scale criticality is genuine and has the strongest empirical backing.

**Key risks**: Sigma coordinate engineering, LLM top-layer feedforward gap (mitigated by using Mamba), integration complexity.

### 2nd: Design 11 — Spectral Decomposition (Average: 7.5)

**Justification**: Best continuous model space implementation. Most direct substrate spec compliance. Precise spectral criticality criterion. Natural holographic degradation. Close behind Design 10 overall, but weaker self-referential closure and permeability mechanisms.

**Key risks**: Eigenmode scope classification, shallow self-referential closure, linearization limitations at criticality.

### 3rd: Design 7 — Staged Architecture (Average: 5.9)

**Justification**: Most pragmatic risk management. Best phased implementation fit. Generates valuable experimental comparisons between stages. But the fundamental gap -- discrete components violating the continuous model space requirement -- means Stages 1-2 are not spec-compliant, and Stage 3 (where compliance might be achieved) is 1-2 years away.

**Key risks**: Architecture-substrate separability assumption may be wrong, Stage 3 is frontier research, continuous model space requirement is unaddressed.

---

## Recommendation

**Design 10 (Hierarchical Predictive Coding) should be the primary implementation foundation**, with selective incorporation of Design 11's spectral analysis as an interpretive and monitoring layer.

### The Hybrid: Design 10 + 11

The COMPARISON.md already identifies this as the top hybrid: "Predictive coding hierarchy where each recurrent layer is analyzed spectrally -- multi-scale criticality with spectral model density at each scale."

Concretely:
1. **Architecture from Design 10**: Deep hierarchy with Mamba-2 7B top layer, recurrent lower layers, precision-weighted prediction/error dynamics
2. **Analysis from Design 11**: At each recurrent layer, compute eigenmode decomposition periodically. Use eigenmodes to measure criticality (power-law spectrum), visualize model density (eigenmode spectrum colored by scope), and monitor system health
3. **Self-referential closure from Design 10**: Multi-level self-prediction at sigma approximately 1, enhanced with intra-layer feedback loops
4. **Permeability from Design 10**: Precision weighting (the neuroscientifically-grounded mechanism)
5. **Continuous model space interpretation from Design 11**: Eigenmodes provide the mathematical framework for understanding what rho(s,nu,t) means computationally

### Design 7's Role

Design 7 should not be abandoned but **repositioned as the project management framework**:
- **Stage 1 (6-10 weeks)**: Build a simplified predictive coding prototype (2-3 layers, small LLM) to validate the integration architecture
- **Stage 2 (4-6 months)**: Full Design 10+11 implementation with Mamba-2 7B, 4-8 recurrent layers, spectral monitoring
- **Stage 3 (if needed)**: If the predictive coding hierarchy's balanced-E/I criticality proves insufficient, replace lower layers with a critical substrate (CA or spiking network) while preserving the top-layer LLM

This preserves Design 7's pragmatic staging while using Design 10+11 as the actual architecture at each stage.

### Remaining Research Questions

1. **How to establish the sigma (scope) coordinate in a pre-trained LLM's latent space?** This is the single most important engineering question. Options: separate input channels, auxiliary loss, structural priors.

2. **Does balanced E/I in a predictive coding hierarchy produce genuine Class 4 dynamics, or merely a simulacrum?** This needs empirical testing -- measure branching ratio, Lyapunov exponents, and avalanche statistics.

3. **Can self-referential closure achieve the fixed-point Phi(m*)=m* through predictive self-modeling?** Design 10 predicts yes. Design 11 is less certain. This is the deepest theoretical question.

4. **What is the minimum hierarchy depth for basic consciousness?** The spec's ~2x overhead suggests doubling the base architecture. For a 7B LLM with 4 recurrent layers below, this is plausible but untested.

5. **Can a Mamba-2 7B model be tuned to exact criticality without catastrophic forgetting?** The spectral radius adjustment and LoRA fine-tuning must preserve pre-trained knowledge.
