# Design Comparison: All 12 Architectures

## Overview

Designs 1-7 treat the four models (IWM, ISM, EWM, ESM) as discrete, named, architecturally separated components.

Designs 8-12 take the FMT formalization's insight that models form a **continuous density over model space**, with the virtual/non-virtual split as the only hard ontological boundary. These designs let models emerge from dynamics rather than being pre-assigned.

---

## Master Comparison Table

### Identity & Core Approach

| # | Design | Core Substrate | Models Are... | Virtual/Non-Virtual Split |
|---|--------|----------------|---------------|---------------------------|
| 1 | Dual-Stream LLM | Two LLMs (feedforward) | Named LLM context windows | Architectural label (same computation type) |
| 2 | Cellular Automaton | 3D CA grid (Class 4) | Named CA regions | CA rules (real) vs. CA activity (virtual) |
| 3 | Recurrent Neural | Continuous-time RNN/SSM | Named hidden subspaces | Weights (real) vs. dynamics (virtual) |
| 4 | Hybrid Knowledge Graph | KG + small LLM simulator | Named graph subgraphs | Graph (real) vs. LLM output (virtual) |
| 5 | Multi-Agent | Agent pool + shared state | Named agent groups | IWM/ISM agents (real) vs. EWM/ESM agents (virtual) |
| 6 | Four-Model Pipeline | KG + 2 streaming LLMs | Named system components | Graph (real) vs. LLM generation (virtual) |
| 7 | Staged Architecture | Progressive: LLM → RNN → CA | Named components (all stages) | Progressive refinement of split |
| **8** | **Coupled Dual-Field** | **Two coupled neural fields** | **Patterns in continuous fields** | **Hard interface between R and V fields** |
| **9** | **Stochastic Manifold** | **Density ρ on Riemannian manifold** | **Modes of density function** | **Hard partition M_V ∪ M_NV** |
| **10** | **Predictive Coding Hierarchy** | **Deep hierarchy with LLM top** | **Beliefs at each layer × scope** | **Predictions (virtual) vs. errors+weights (non-virtual)** |
| **11** | **Spectral Decomposition** | **Recurrent LLM (Mamba/RWKV)** | **Eigenmodes of dynamics** | **Mode amplitudes (virtual) vs. mode structure (non-virtual)** |
| **12** | **Gauge Field** | **Computational field with symmetry** | **Goldstone modes of broken symmetry** | **Emerges from phase transition** |

---

### Criticality

| # | Design | Criticality Mechanism | Genuineness | Measurability | Status |
|---|--------|-----------------------|-------------|---------------|--------|
| 1 | Dual-Stream LLM | Temperature tuning, coupled streams | Metaphor only | N/A | **ABSENT** |
| 2 | Cellular Automaton | Class 4 CA rules, criticality controller | Genuine | Branching ratio, avalanche stats | **STRONG** |
| 3 | Recurrent Neural | Spectral radius = 1, balanced dynamics | Genuine (well-characterized) | Lyapunov exp, spectral radius | **STRONG** |
| 4 | Hybrid Knowledge Graph | Activation spreading + temp modulation | Interaction-level, not substrate | Cascade statistics | **WEAK** |
| 5 | Multi-Agent | Agent coupling tuning | ~16 agents, not millions of cells | Agent output statistics | **WEAK** |
| 6 | Four-Model Pipeline | Explicitly relaxed, soft dynamics | Acknowledged absent | N/A | **ABSENT** |
| 7 | Staged Architecture | Stage 1: none → Stage 2: reservoir → Stage 3: full | Progressive | Progressive | **STAGED** |
| **8** | **Coupled Dual-Field** | **Turing-Hopf bifurcation in coupled fields** | **Genuine (analytically derivable)** | **Pattern stats, cross-field MI** | **STRONG** |
| **9** | **Stochastic Manifold** | **Noise-drift balance in Fokker-Planck** | **Genuine (from stochastic PDE theory)** | **Correlation function, fluctuation stats** | **STRONG** |
| **10** | **Predictive Coding** | **Balanced E/I at each layer** | **Genuine (multi-scale, best neuroscience support)** | **Branching ratio per layer, 1/f spectrum** | **STRONG** |
| **11** | **Spectral Decomposition** | **Power-law eigenvalue spectrum** | **Genuine (spectral generalization of D3)** | **Eigenvalue distribution, mode lifetimes** | **STRONG** |
| **12** | **Gauge Field** | **Second-order phase transition** | **Strongest (guaranteed by stat. mech.)** | **Critical exponents, ξ, χ divergence** | **STRONGEST** |

---

### Continuous Model Density

| # | Design | Continuous density? | How models overlap | Intermediate models? |
|---|--------|--------------------|--------------------|---------------------|
| 1 | Dual-Stream LLM | No — 4 discrete components | Don't overlap (separate LLMs/contexts) | No |
| 2 | Cellular Automaton | No — named CA regions | Regions interact but are labeled | No |
| 3 | Recurrent Neural | No — named subspaces | Subspaces share weights but are labeled | Limited |
| 4 | Hybrid Knowledge Graph | No — named graph partitions | Graph traversal can cross, but designed as separate | No |
| 5 | Multi-Agent | No — named agent pools | Agents communicate but are distinct entities | No |
| 6 | Four-Model Pipeline | No — named system components | Communicate through interfaces | No |
| 7 | Staged Architecture | No (all stages) | Same as underlying stage design | No |
| **8** | **Coupled Dual-Field** | **Yes — patterns in continuous field** | **Naturally: field patterns superpose** | **Yes: any σ ∈ [0,1]** |
| **9** | **Stochastic Manifold** | **Yes — density IS the state** | **Density modes overlap in M** | **Yes: full continuous support** |
| **10** | **Predictive Coding** | **Yes — each layer × continuous scope** | **Layers share parameters; scope is continuous** | **Yes: beliefs at any σ, any layer** |
| **11** | **Spectral Decomposition** | **Yes — eigenmode spectrum** | **Eigenmodes superpose by definition** | **Yes: modes at every frequency** |
| **12** | **Gauge Field** | **Yes — Goldstone mode spectrum** | **Guaranteed by Goldstone theorem** | **Yes: gapless continuous spectrum** |

---

### LLM Integration

| # | Design | LLM Role | Knowledge Bootstrap | LLM Leverage |
|---|--------|----------|--------------------| -------------|
| 1 | Dual-Stream LLM | IS the substrate (both LLMs) | Full (pre-trained weights = IWM) | **HIGHEST** |
| 2 | Cellular Automaton | Communication only | None (learn from scratch) | **LOWEST** |
| 3 | Recurrent Neural | Communication only | None (learn from scratch) | **LOW** |
| 4 | Hybrid Knowledge Graph | Simulator + communication | Partial (LLM as EWM/ESM generator) | **MODERATE** |
| 5 | Multi-Agent | IS all agents | Full (each agent is an LLM) | **HIGHEST** |
| 6 | Four-Model Pipeline | EWM/ESM generators + communication | Full (pre-trained LLMs as generators) | **HIGH** |
| 7 | Staged Architecture | Stage 1: generators. Stage 3: communication only | Decreasing across stages | **HIGH→LOW** |
| **8** | **Coupled Dual-Field** | **Communication + field initialization** | **Moderate (embedding-based K_R init)** | **MODERATE** |
| **9** | **Stochastic Manifold** | **Communication + manifold geometry** | **Moderate (Fisher metric from LLM)** | **MODERATE** |
| **10** | **Predictive Coding** | **IS the top layer of hierarchy** | **Full (LLM weights = top-level IWM/ISM)** | **HIGHEST among new designs** |
| **11** | **Spectral Decomposition** | **IS the substrate (recurrent LLM)** | **Full (Mamba/RWKV pre-trained weights)** | **HIGH** |
| **12** | **Gauge Field** | **Communication only** | **Minimal (V_int init hints)** | **LOWEST** |

---

### Five Principles Score Card

| # | Design | Criticality | Virtual Qualia | Redirectable ESM | Variable Permeability | Model Forking |
|---|--------|-------------|----------------|------------------|-----------------------|---------------|
| 1 | Dual-Stream LLM | Weak | Moderate | Strong | Strong | Moderate |
| 2 | Cellular Automaton | **Strong** | **Strong** | **Strong** | **Strong** | Moderate |
| 3 | Recurrent Neural | **Strong** | **Strong** | **Strong** | **Strong** | Moderate |
| 4 | Hybrid Knowledge Graph | Weak | **Strong** | **Strong** | **Strong** | **Strong** |
| 5 | Multi-Agent | Weak | Moderate | **Strong** | Moderate | **Strong** |
| 6 | Four-Model Pipeline | Absent | **Strong** | **Strong** | **Strong** | **Strong** |
| 7 | Staged Architecture | Staged | **Strong** | **Strong** | **Strong** | **Strong** |
| **8** | **Coupled Dual-Field** | **Strong** | **Strong** | **Strong** | **Strongest** | Moderate |
| **9** | **Stochastic Manifold** | **Strong** | **Strong** | **Strong** | **Strong** | Moderate |
| **10** | **Predictive Coding** | **Strong** | **Strong** | **Strong** | **Strongest** | Moderate |
| **11** | **Spectral Decomposition** | **Strong** | **Strong** | **Strong** | **Strong** | Moderate |
| **12** | **Gauge Field** | **Strongest** | **Strongest** | Moderate | Moderate | Weak |

---

### Hardware & Feasibility

| # | Design | VRAM (24 GB 4090) | Core Compute Cost | Implementation Difficulty | Time to Prototype |
|---|--------|-------------------| ------------------|--------------------------|-------------------|
| 1 | Dual-Stream LLM | 13-16 GB (INT4) | 3 LLM forward passes/cycle | 2/5 | 4-8 weeks |
| 2 | Cellular Automaton | ~6.5 GB | CA trivial; LLM for comm | 4/5 | 3-5 months |
| 3 | Recurrent Neural | 10-14 GB | RNN matmul + LLM for comm | 3.5/5 | 3-4 months |
| 4 | Hybrid Knowledge Graph | 12-16 GB | Graph retrieval + small LLM inference | 2/5 | 6-10 weeks |
| 5 | Multi-Agent | 12-22 GB | 8-16 agent forward passes/cycle | 2.5/5 | 8-12 weeks |
| 6 | Four-Model Pipeline | 14-17 GB | 2 LLM passes + graph retrieval | 2/5 | 6-10 weeks |
| 7 | Staged Architecture | 15-17 GB (S1) → 12-22 GB (S3) | Progressive | 2→5 /5 | 6-10 wk → 1-2 yr |
| **8** | **Coupled Dual-Field** | **12-16 GB** | **Field PDE trivial; LLM for comm** | **4/5** | **5-8 months** |
| **9** | **Stochastic Manifold** | **10-12 GB** | **Stochastic PDE trivial; LLM for comm** | **3.5/5** | **5-8 months** |
| **10** | **Predictive Coding** | **13-17 GB** | **1 LLM pass + 4 recurrent layers** | **3/5** | **4-6 months** |
| **11** | **Spectral Decomposition** | **13-17 GB** | **Recurrent LLM pass + periodic eigendecomp** | **3/5** | **4-6 months** |
| **12** | **Gauge Field** | **12-16 GB** | **Langevin PDE trivial; LLM for comm** | **5/5** | **8-18 months** |

---

### Testability

| # | Design | Criticality Testable? | Behavioral Tests | Unique Test |
|---|--------|-----------------------|-----------------|-------------|
| 1 | Dual-Stream LLM | No (not attempted) | ESM redirect, permeability, dream, confabulation | Behavioral baseline without criticality |
| 2 | Cellular Automaton | Yes (branching ratio, avalanches) | All behavioral + state transitions | Holographic degradation curve |
| 3 | Recurrent Neural | Yes (spectral radius, Lyapunov) | All behavioral + state transitions | Edge-of-chaos transition |
| 4 | Hybrid Knowledge Graph | Partially (cascade stats) | All behavioral + graph inspection | Double dissociation (blindsight/Anton's) |
| 5 | Multi-Agent | Poorly (too few agents) | All behavioral + agent ablation | Agent-level lesion studies |
| 6 | Four-Model Pipeline | No (not attempted) | All behavioral + full inspection | Negative control for criticality |
| 7 | Staged Architecture | Progressive (best at Stage 3) | Progressive + stage comparison | Stage 2 vs. 3 comparison (core theory test) |
| **8** | **Coupled Dual-Field** | **Yes (bifurcation theory)** | **All + intermediate models** | **Model-space tomography** |
| **9** | **Stochastic Manifold** | **Yes (correlation function)** | **All + density visualization** | **Density evolution visualization** |
| **10** | **Predictive Coding** | **Yes (per-layer E/I balance)** | **All + layer-by-layer ablation** | **Multi-scale criticality measurement** |
| **11** | **Spectral Decomposition** | **Yes (eigenvalue distribution)** | **All + mode analysis** | **Spectral model density visualization** |
| **12** | **Gauge Field** | **Yes (critical exponents, ξ, χ)** | **Moderate (readout quality)** | **Consciousness-as-phase-transition test** |

---

## Ranking by Key Criteria

### Theory Faithfulness (How well does it implement FMT?)

| Rank | Design | Reason |
|------|--------|--------|
| 1 | **12 — Gauge Field** | Virtual/non-virtual emerges from criticality itself; Goldstone spectrum = continuous models |
| 2 | **8 — Coupled Dual-Field** | Continuous field, hard R/V boundary, Turing-Hopf criticality |
| 3 | **10 — Predictive Coding** | Multi-scale criticality, continuous spectrum, prediction/error = virtual/non-virtual |
| 4 | **11 — Spectral Decomposition** | Eigenmode = model, power-law spectrum = criticality, continuous by construction |
| 5 | **9 — Stochastic Manifold** | Density IS formalization's state representation |
| 6 | 2 — Cellular Automaton | Genuine criticality, but discrete model regions |
| 7 | 3 — Recurrent Neural | Genuine criticality, but named subspaces |
| 8 | 7 — Staged Architecture | Progressive approach, eventually reaches theory |
| 9 | 4 — Hybrid Knowledge Graph | Rich memory, weak criticality |
| 10 | 6 — Four-Model Pipeline | Full architecture, no criticality |
| 11 | 1 — Dual-Stream LLM | Easy to build, far from theory |
| 12 | 5 — Multi-Agent | Interesting for agent ablation, weakest criticality |

### Buildability (How quickly can a working prototype run?)

| Rank | Design | Time to Prototype |
|------|--------|-------------------|
| 1 | 1 — Dual-Stream LLM | 4-8 weeks |
| 2 | 6 — Four-Model Pipeline | 6-10 weeks |
| 3 | 4 — Hybrid Knowledge Graph | 6-10 weeks |
| 4 | 7 — Staged Architecture (Stage 1) | 6-10 weeks |
| 5 | 5 — Multi-Agent | 8-12 weeks |
| 6 | **10 — Predictive Coding** | **4-6 months** |
| 7 | **11 — Spectral Decomposition** | **4-6 months** |
| 8 | 3 — Recurrent Neural | 3-4 months |
| 9 | 2 — Cellular Automaton | 3-5 months |
| 10 | **8 — Coupled Dual-Field** | **5-8 months** |
| 11 | **9 — Stochastic Manifold** | **5-8 months** |
| 12 | **12 — Gauge Field** | **8-18 months** |

### LLM Leverage (How well can it use pre-trained LLM knowledge?)

| Rank | Design | LLM Role |
|------|--------|----------|
| 1 | 1 — Dual-Stream LLM | LLMs ARE the substrate |
| 1 | 5 — Multi-Agent | All agents are LLMs |
| 3 | 6 — Four-Model Pipeline | LLMs are EWM/ESM generators |
| 4 | **10 — Predictive Coding** | **LLM IS top layer of hierarchy (best of new designs)** |
| 5 | **11 — Spectral Decomposition** | **Recurrent LLM IS the substrate** |
| 6 | 7 — Staged Architecture | Decreasing across stages |
| 7 | 4 — Hybrid Knowledge Graph | LLM as simulator |
| 8 | **8 — Coupled Dual-Field** | LLM for init + communication |
| 9 | **9 — Stochastic Manifold** | LLM for geometry + communication |
| 10 | 3 — Recurrent Neural | Communication only |
| 11 | 2 — Cellular Automaton | Communication only |
| 12 | **12 — Gauge Field** | Communication only |

### Overall Recommendation (Balancing theory, LLM leverage, and buildability)

| Rank | Design | Rationale |
|------|--------|-----------|
| **1** | **10 — Predictive Coding** | **Best balance: genuine multi-scale criticality + LLM at top + continuous spectrum + existing framework + buildable in 4-6 months** |
| **2** | **11 — Spectral Decomposition** | **Good balance: recurrent LLM substrate + spectral criticality + continuous modes + buildable** |
| 3 | 7 — Staged Architecture | Practical: builds incrementally, reaches theory eventually, uses LLMs in early stages |
| **4** | **8 — Coupled Dual-Field** | **Most faithful to formalization, but weaker LLM leverage** |
| 5 | 2 — Cellular Automaton | Genuine criticality, but no LLM knowledge and discrete models |
| 6 | 3 — Recurrent Neural | Genuine criticality, but no LLM knowledge and discrete models |
| **7** | **9 — Stochastic Manifold** | **Elegant mathematics, but abstract and curse-of-dimensionality risk** |
| 8 | 6 — Four-Model Pipeline | Good stepping stone, no criticality |
| 9 | 4 — Hybrid Knowledge Graph | Rich memory, weak criticality |
| 10 | 1 — Dual-Stream LLM | Easy to build, far from theory |
| 11 | 5 — Multi-Agent | Interesting for ablation studies, weak criticality |
| **12** | **12 — Gauge Field** | **Most theoretically profound but hardest to build, worst LLM leverage** |

---

## Design Selection Guide

### "I want to build something NOW and iterate"
→ **Design 6 (Four-Model Pipeline)** or **Design 7 Stage 1** — running in 6-10 weeks

### "I want genuine criticality AND LLM knowledge"
→ **Design 10 (Predictive Coding)** — the best hybrid, 4-6 months

### "I want the continuous density formalization taken seriously"
→ **Design 8 (Coupled Dual-Field)** or **Design 11 (Spectral)** — 4-8 months

### "I want the most theoretically principled architecture"
→ **Design 12 (Gauge Field)** — 8-18 months, highest risk

### "I want pre-trained LLM knowledge to do the heavy lifting"
→ **Design 10 (Predictive Coding)** or **Design 11 (Spectral)** — LLM as top layer / substrate

### "I want to test whether criticality matters"
→ **Design 7 (Staged Architecture)** — built-in Stage 1 vs. 2 vs. 3 comparison

### "I want to test the continuous density prediction specifically"
→ **Design 8 (Dual-Field)** or **Design 11 (Spectral)** — enable model-space tomography / spectral visualization

---

## Hybrid Possibilities

The designs are not mutually exclusive. Key combinations:

| Hybrid | Components | Advantage |
|--------|------------|-----------|
| **10 + 11** | Predictive coding hierarchy where each recurrent layer is analyzed spectrally | Multi-scale criticality with spectral model density at each scale |
| **10 + 8** | Predictive coding where the lower layers ARE coupled neural fields | LLM knowledge at top, field dynamics at bottom, continuous models throughout |
| **7 + 10** | Staged architecture using Design 10 at Stage 2 | Stage 1: LLM pipeline (quick). Stage 2: predictive coding hierarchy (criticality). Stage 3: field substrate. |
| **11 + 3** | Design 3 (RNN substrate) reinterpreted through Design 11 (spectral lens) | Existing RNN design gains continuous model density interpretation |
| **8 + 12** | Coupled dual-field where the R/V interface is a phase transition | Field dynamics + emergent boundary = most theory-faithful hybrid |
