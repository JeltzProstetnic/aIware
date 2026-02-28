#!/usr/bin/env python3
"""Build the 16-design landscape overview PDF.

Writes .mmd files, renders to PNG via mmdc, composes landscape HTML,
converts to PDF via weasyprint.

Usage: python3 tmp/build_design_overview.py
Output: docs/engineering/designs/pdf/00-design-overview-landscape.pdf
"""

import base64
import subprocess
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
DESIGNS_DIR = PROJECT / "docs" / "engineering" / "designs"
PDF_DIR = DESIGNS_DIR / "pdf"
MMD_DIR = PDF_DIR / "mmd"
PNG_DIR = PDF_DIR / "png"

# All 16 designs: (number, short_title, description, mermaid_code)
DESIGNS = [
    (1, "Dual-Stream LLM",
     "Two continuously-running LLM inference streams implement the four-model theory — one for implicit processing (IWM/ISM in weights), one for explicit simulation (EWM/ESM as running generation) — connected through a permeability gate. Easiest to build (4-8 weeks) but fundamentally lacks genuine Class 4 criticality since transformer inference is feedforward.",
     r"""graph TD
    subgraph EXT["External Interface"]
        COMM["Communication LLM\n(7B INT4)"]
    end
    subgraph VIRTUAL["Virtual Side -- Streaming LLM #2"]
        EWM["EWM\nWorld simulation via\ncontinuous generation"]
        ESM["ESM\nSelf simulation via\ncontinuous generation"]
    end
    subgraph GATE["Permeability Gate"]
        ATTN["Attention mask +\ntemperature modulation"]
    end
    subgraph REAL["Real Side -- Streaming LLM #1"]
        IWM["IWM\nWorld knowledge\nin weights"]
        ISM["ISM\nSelf knowledge\nin weights"]
    end
    subgraph MEM["Persistent Memory"]
        KG["SQLite Knowledge Graph"]
    end
    COMM -->|input tokens| ESM
    ESM -->|output tokens| COMM
    IWM --> ATTN
    ISM --> ATTN
    ATTN --> EWM
    ATTN --> ESM
    ESM -->|self-referential\nclosure loop| ESM
    SENS["Sensory Input"] --> IWM
    SELF_MON["Self-state\nMonitoring"] --> ISM
    IWM -->|learning| KG
    ISM -->|learning| KG
    KG --> IWM
    KG --> ISM"""),

    (2, "Cellular Automaton Substrate",
     "A genuine 3D cellular automaton (500K-2M cells) at Class 4 criticality serves as the computational substrate, with neural readout networks decoding CA activity patterns into EWM/ESM simulations. Most theoretically faithful substrate-level design but hardest to train — CA transition rules must learn from scratch without pre-trained bootstrap.",
     r"""graph TD
    subgraph EXT["External Interface"]
        COMM["Communication LLM\n(3-7B INT4)"]
    end
    subgraph READOUT["Virtual Side -- Readout"]
        EWM_R["EWM Readout Net\nDecodes CA world patterns"]
        ESM_R["ESM Readout Net\nDecodes CA self patterns"]
    end
    subgraph CA["Cellular Automaton (Class 4)"]
        subgraph REGIONS["3D Grid ~1M cells, ~40 Hz"]
            IWM_R["IWM Region\nWorld knowledge in rules"]
            ISM_R["ISM Region\nSelf knowledge in rules"]
        end
        PERM["Permeability Control"]
    end
    subgraph CRIT["Criticality Controller"]
        BR["Branching ratio = 1.0"]
        AV["Power-law avalanches ~1.5"]
    end
    ESM_R -->|output| COMM
    IWM_R --> PERM
    ISM_R --> PERM
    PERM --> EWM_R
    PERM --> ESM_R
    ESM_R -->|self-referential feedback| ISM_R
    SENS["Sensory Input"] --> IWM_R
    CRIT -->|parameter adjustment| REGIONS"""),

    (3, "Recurrent Neural Substrate",
     "A continuous-time RNN/SSM (10K-100K hidden dims) at edge-of-chaos criticality (spectral radius = 1.0), with decoder heads projecting hidden state into EWM/ESM outputs and ESM fed back for self-referential closure. Fully differentiable and trainable via BPTT, but open question whether spectral-radius criticality equates to Class 4 CA dynamics.",
     r"""graph TD
    subgraph EXT["External Interface"]
        COMM["Communication LLM\n(3-7B INT4)"]
    end
    subgraph DECODERS["Virtual Side -- Decoders"]
        EWM_D["EWM Decoder Head"]
        ESM_D["ESM Decoder Head"]
    end
    subgraph GATE["Permeability Control"]
        G["Gating Network"]
    end
    subgraph RNN["Recurrent Substrate"]
        DYN["dh/dt = f(h, x, u; W)\n10K-100K dims, ~40 Hz"]
        IWM_S["IWM Subspace"]
        ISM_S["ISM Subspace"]
    end
    subgraph CRIT["Criticality"]
        SPEC["Spectral radius = 1.0"]
        HOMEO["Homeostatic plasticity"]
    end
    ESM_D -->|output| COMM
    DYN --> G
    G --> EWM_D
    G --> ESM_D
    ESM_D -->|self-referential feedback| DYN
    SENS["Sensory input"] --> DYN
    CRIT -->|spectral normalization| RNN"""),

    (4, "Hybrid Knowledge-Graph + Simulation",
     "SQLite knowledge graph as implicit models (IWM as world subgraph, ISM as SELF-rooted subgraph), with small LLMs generating EWM/ESM simulations from graph-assembled context at 20 Hz. Fastest path to prototype (6-10 weeks) with richest memory and most inspectable internals, but criticality is bolted-on rather than substrate-native.",
     r"""graph TD
    subgraph EXT["External Interface"]
        COMM["Communication LLM\n(3-7B INT4)"]
    end
    subgraph SIM["Virtual Side -- Simulators"]
        EWM_SIM["EWM Simulator\n(3B LLM)\nWorld scenes ~20 Hz"]
        ESM_SIM["ESM Simulator\n(3B LLM)\nSelf-state ~20 Hz"]
    end
    subgraph PERM["Permeability Gate"]
        DEPTH["Retrieval depth control"]
    end
    subgraph GRAPH["Knowledge Graph -- Real Side"]
        IWM_G["IWM Subgraph\nEntities, relations, causation"]
        ISM_G["ISM Subgraph\nSELF entity + traits"]
        PIPE["Context Assembly Pipeline"]
    end
    subgraph CRIT["Criticality Controller"]
        SPREAD["Stochastic activation spreading"]
        TEMP["Temperature modulation"]
    end
    ESM_SIM -->|output| COMM
    IWM_G --> PIPE
    ISM_G --> PIPE
    PIPE --> DEPTH
    DEPTH --> EWM_SIM
    DEPTH --> ESM_SIM
    ESM_SIM -->|self-referential feedback| ESM_SIM
    SENS["Sensory Input"] --> IWM_G
    CRIT -->|parameter adjustment| GRAPH"""),

    (5, "Multi-Agent Consciousness",
     "8-16 small LLM agents grouped into four pools (IWM/ISM/EWM/ESM) interact through a shared state space, with coupling strength tuned to seek edge-of-chaos behavior. Enables cheap model forking and agent-level lesion studies mapping to neurological deficits, but too few agents for genuine substrate-level criticality.",
     r"""graph TD
    subgraph EXT["External Interface"]
        SPOKE["Spokesperson Agent\n3-7B LLM"]
    end
    subgraph VIRTUAL["Virtual Side Agents"]
        EWMP["EWM Pool\n2-4 LLMs"]
        ESMP["ESM Pool\n2-4 LLMs"]
    end
    subgraph PERM["Permeability Control"]
        SCHED["Agent Scheduling\n+ State Access Control"]
    end
    subgraph SSS["Shared State Space"]
        IWM_S["IWM State Region"]
        ISM_S["ISM State Region"]
        EWM_S["EWM State (transient)"]
        ESM_S["ESM State (transient)"]
    end
    subgraph REAL["Real Side Agents"]
        IWMP["IWM Pool 2-4 LLMs"]
        ISMP["ISM Pool 2-4 LLMs"]
    end
    subgraph IDC["Dynamics Controller"]
        COUP["Coupling + Topology + Noise"]
    end
    IWMP --> IWM_S
    ISMP --> ISM_S
    IWM_S --> SCHED
    ISM_S --> SCHED
    SCHED --> EWMP
    SCHED --> ESMP
    EWMP --> EWM_S
    ESMP --> ESM_S
    ESM_S -->|self-referential feedback| ESMP
    EWM_S --> SPOKE
    ESM_S --> SPOKE
    IDC -.->|controls| SCHED"""),

    (6, "Four-Model LLM Pipeline",
     "Two 7B quantized LLMs as EWM/ESM generators at 10-20 Hz, backed by a SQLite knowledge graph as IWM/ISM, with configurable permeability gate. Explicitly relaxes criticality to serve as a behavioral baseline — the 'lights off' negative control for designs that add genuine criticality.",
     r"""graph TD
    subgraph EXT["External Interface"]
        COMM["Communication LLM\n3B INT4"]
    end
    subgraph VIRTUAL["Virtual Side"]
        EWM["EWM Generator\n7B LLM ~10-20 Hz"]
        ESM["ESM Generator\n7B LLM ~10-20 Hz"]
    end
    subgraph PERM["Permeability Gate"]
        DEPTH["Retrieval Depth"]
        BUDGET["Attention Budget"]
    end
    subgraph REAL["Real Side -- Knowledge Graph"]
        IWM["IWM Store"]
        ISM["ISM Store"]
        CTX["Context Assembly"]
    end
    subgraph SOFT["Soft Criticality"]
        TMOD["Temperature Modulation"]
        OSC["Oscillatory Mode Switching"]
    end
    IWM --> CTX
    ISM --> CTX
    CTX --> PERM
    PERM --> EWM
    PERM --> ESM
    ESM -->|self-referential closure| ESM
    EWM --> COMM
    ESM --> COMM
    SOFT -.->|modulates| VIRTUAL"""),

    (7, "Staged Architecture",
     "Three-stage research program: Stage 1 uses LLMs + knowledge graph without criticality (6-10 weeks). Stage 2 adds a reservoir computing module tuned near criticality. Stage 3 replaces the substrate with a genuine Class 4 CA or critical neural network. Built-in experimental design: same architecture at three criticality levels directly tests the 'consciousness switch' prediction.",
     r"""graph TD
    subgraph S1["Stage 1: LLM Pipeline (no criticality)"]
        KG1["Knowledge Graph"]
        LLM1["LLM Generators"]
    end
    subgraph S2["Stage 2: + Reservoir (near-critical)"]
        ESN["Echo State Network\n10K-100K units\nspectral radius ~1.0"]
        KG2["Knowledge Graph"]
    end
    subgraph S3["Stage 3: Critical Substrate"]
        CA["Class 4 CA\nor Critical Neural Net"]
        READ["Readout Networks"]
    end
    subgraph SHARED["Shared Across All Stages"]
        EWM["EWM Generator"]
        ESM["ESM Generator"]
        COMM["Communication LLM"]
        PERM["Permeability Gate"]
    end
    subgraph METRICS["Criticality Metrics"]
        PL["Power-law avalanches"]
        BR["Branching ratio ~1.0"]
    end
    KG1 -->|S1| PERM
    ESN -->|S2| PERM
    CA --> READ
    READ -->|S3| PERM
    PERM --> EWM
    PERM --> ESM
    ESM -->|self-referential loop| ESM
    EWM --> COMM
    ESM --> COMM
    METRICS -.->|monitors S2+S3| ESN
    METRICS -.->|monitors S3| CA"""),

    (8, "Coupled Dual-Field Dynamics",
     "Two continuous neural fields — implicit field R (persistent knowledge) and explicit field V (transient simulation) — coupled through a sharp ontological boundary with variable permeability. Models emerge as density peaks in a continuous model-space manifold. Criticality via analytically derivable Turing-Hopf bifurcation. Most faithful to the formalization's continuous density insight.",
     r"""graph TD
    subgraph EXT["External Interface"]
        COMM["Communication LLM"]
        RO_W["EWM Readout"]
        RO_S["ESM Readout"]
    end
    subgraph VFIELD["Explicit Field V(x,t) -- Virtual"]
        VW["World peaks\nsigma near 0"]
        VMID["Intermediate models\nsigma near 0.5"]
        VS["Self peaks\nsigma near 1"]
    end
    subgraph BOUNDARY["Ontological Boundary"]
        CUP["C_up: implicit to explicit"]
        CDOWN["C_down: explicit to implicit"]
        PERMCTRL["Variable Permeability"]
    end
    subgraph RFIELD["Implicit Field R(x,t) -- Non-Virtual"]
        RW["World knowledge\nsigma near 0"]
        RS["Self knowledge\nsigma near 1"]
    end
    subgraph CRIT["Turing-Hopf Bifurcation"]
        HOMEO["Homeostatic Controller"]
    end
    INPUT["Sensory Input"] --> RFIELD
    RFIELD --> CUP
    CUP --> VFIELD
    VFIELD --> CDOWN
    CDOWN --> RFIELD
    VS -->|self-referential feedback| VS
    RO_W --> VW
    RO_S --> VS
    RO_W --> COMM
    RO_S --> COMM
    HOMEO -.->|tunes coupling| BOUNDARY"""),

    (9, "Stochastic Model Density on Riemannian Manifold",
     "System state is a probability density rho(m,t) evolving via Fokker-Planck PDE on a Riemannian manifold, where the four models emerge as dominant peaks. Manifold geometry derived from an LLM's Fisher information metric. Extremely hardware-efficient — the PDE uses <0.001% of GPU compute. Elegant mathematics but abstract and curse-of-dimensionality risk.",
     r"""graph TD
    subgraph EXT["External Interface"]
        CLLM["Communication LLM\n3-7B INT4"]
        READOUT["Readout Networks"]
    end
    subgraph MANIFOLD["Riemannian Manifold M"]
        subgraph MV["M_virtual"]
            RHO_V["rho_V(m,t)\nTransient density"]
            ESM_P["ESM Peak"]
            EWM_P["EWM Peak"]
        end
        subgraph MNV["M_nonvirtual"]
            RHO_NV["rho_NV(m,t)\nPersistent density"]
            ISM_P["ISM Peak"]
            IWM_P["IWM Peak"]
        end
        BOUNDARY["V/NV Partition\nPermeable flux J"]
    end
    subgraph PDE["Fokker-Planck Dynamics"]
        DRIFT["Drift v(rho)"]
        DIFF["Diffusion D * nabla^2 rho"]
        NOISE["Stochastic noise"]
    end
    subgraph METRIC["LLM-Derived Geometry"]
        FISHER["Fisher Information Metric"]
    end
    INPUT["Sensory Input"] --> PDE
    PDE --> RHO_V
    RHO_V --> BOUNDARY
    BOUNDARY --> RHO_NV
    RHO_NV --> BOUNDARY
    ESM_P -->|self-referential closure| PDE
    FISHER --> PDE
    EWM_P --> READOUT
    ESM_P --> READOUT
    READOUT --> CLLM"""),

    (10, "Predictive Coding Hierarchy",
     "Deep hierarchical generative model where the top layer IS a pre-trained LLM (Mamba/SSM), providing world knowledge and language natively, while lower recurrent layers add critical dynamics via balanced E/I. Virtual/non-virtual maps to prediction/error decomposition. No separate communication LLM needed. Best balance of theory faithfulness, LLM leverage, and buildability (4-6 months).",
     r"""graph TD
    subgraph EXT["External I/O"]
        IO["Top layer handles\ncommunication directly"]
    end
    subgraph TOP["Layer N -- Pre-trained LLM (7B Mamba)"]
        GEN["Generative Model\np(z_N-1 | z_N)"]
        PRED_N["Predictions (top-down)\n= VIRTUAL SIDE"]
        ERR_N["Errors (bottom-up)\n= NON-VIRTUAL"]
        SELF_N["Self-Narrative (ESM)"]
        WORLD_N["World Knowledge (IWM)"]
    end
    subgraph MID["Layers 1..N-1 -- Recurrent Modules"]
        REC["Recurrent State h_k(t)"]
        PRED_K["Predictions (top-down)"]
        ERR_K["Errors (bottom-up)"]
        PREC["Precision Weights\n= Permeability"]
        SR["Spectral Radius ~1.0"]
    end
    subgraph L0["Layer 0 -- Sensory"]
        SENS["Sensory + Interoceptive"]
        SENS_ERR["Prediction Errors"]
    end
    subgraph CRIT["Multi-Scale Criticality"]
        BRANCH["Branching ratio = 1.0\nat each layer"]
        PL["Power-law avalanches"]
    end
    IO --> TOP
    GEN --> PRED_N
    PRED_N --> PRED_K
    ERR_K --> ERR_N
    REC --> PRED_K
    PREC -->|modulates| ERR_K
    PRED_K --> L0
    SENS --> SENS_ERR
    SENS_ERR --> ERR_K
    SELF_N -->|self-referential closure| TOP
    PRED_N --> IO
    BRANCH --> SR"""),

    (11, "Spectral Decomposition",
     "Recurrent neural substrate (Mamba-2 SSM) whose dynamics are decomposed into eigenmodes of the Jacobian — each eigenmode IS a model, with dominant modes as IWM/ISM/EWM/ESM and the full spectrum as continuous model density. Criticality = power-law eigenvalue distribution. Can be applied retroactively as analysis overlay to other designs.",
     r"""graph TD
    subgraph EXT["External Interface"]
        CLLM["Communication LLM\n3B INT4"]
    end
    subgraph READOUT["Spectral Readout (Virtual)"]
        DECOMP["Eigenmode Decomposition\nh(t) = Sum a_k * phi_k"]
        PHI1["phi_1: EWM-like\nWorld-focused"]
        PHI2["phi_2: ESM-like\nSelf-focused"]
        HIGHER["Higher modes k>4\nContinuous spectrum"]
        AMP["Amplitudes a_k(t)\n= VIRTUAL (transient)"]
        PERM["Permeability:\nhow many modes exposed"]
    end
    subgraph SUBSTRATE["Recurrent Substrate (Non-Virtual)"]
        DYN["h(t+1) = f(W*h(t) + input)"]
        W_MAT["Weight Matrix W\n= IMPLICIT MODELS"]
        JACOB["Jacobian eigendecomposition"]
        EIGEN["Eigenmode structure phi_k\n= NON-VIRTUAL (persistent)"]
    end
    subgraph CRIT["Spectral Criticality"]
        SPECTRUM["Eigenvalue distribution\nTarget: power law"]
        SHAPING["Spectral shaping of W"]
    end
    INPUT["Sensory Input"] --> DYN
    DYN --> DECOMP
    DECOMP --> AMP
    AMP --> PHI1
    AMP --> PHI2
    AMP --> HIGHER
    PHI2 -->|self-referential feedback| DYN
    AMP --> CLLM
    W_MAT --> JACOB
    JACOB --> EIGEN
    EIGEN --> DECOMP
    SPECTRUM --> SHAPING
    SHAPING --> W_MAT"""),

    (12, "Neural Gauge Field with Symmetry Breaking",
     "A computational field Phi(x,t) with internal gauge symmetry evolves via Langevin dynamics on a GPU lattice. At critical temperature T_c, symmetry breaks: ordered ground state Phi_0 = non-virtual (implicit models), Goldstone mode fluctuations = virtual (explicit models). Criticality IS the design. Most theoretically profound but hardest to build (8-18 months).",
     r"""graph TD
    subgraph EXT["External Interface"]
        CLLM["Communication LLM\n3-7B INT4"]
        READOUT["Readout Networks"]
    end
    subgraph FIELD["Computational Field Phi(x,t)"]
        LATTICE["GPU Lattice\n200K sites"]
        LANGEVIN["Langevin Dynamics\ndPhi/dt = -dF/dPhi + noise"]
        U_POT["Symmetric Potential U(Phi)"]
        V_INT["Learned Interaction V_int"]
    end
    subgraph SYMBREAK["Symmetry Breaking at T_c"]
        PHI0["Order Parameter Phi_0\n= NON-VIRTUAL\nImplicit models"]
        GOLD["Goldstone Fluctuations\n= VIRTUAL\nExplicit models"]
    end
    subgraph MODES["Goldstone Spectrum"]
        M1["World mode (largest)"]
        M2["Self mode"]
        CONT["Continuous spectrum\n(Goldstone theorem)"]
    end
    subgraph CRIT["Phase Transition"]
        XI["Correlation length -> inf"]
        CHI["Susceptibility -> inf"]
        PL["Power-law fluctuations"]
    end
    INPUT["Sensory Input"] --> LANGEVIN
    LATTICE --> LANGEVIN
    U_POT --> LANGEVIN
    V_INT --> LANGEVIN
    LANGEVIN --> PHI0
    LANGEVIN --> GOLD
    GOLD --> M1
    GOLD --> M2
    GOLD --> CONT
    M2 -->|self-referential coupling| LANGEVIN
    M1 --> READOUT
    M2 --> READOUT
    READOUT --> CLLM"""),

    (13, "Reservoir-Gated Recurrent LLM",
     "A recurrent LLM (Mamba-2) whose hidden state transitions are gated by a sparse, criticality-tuned reservoir (50K units, spectral radius 1.0), injecting genuine edge-of-chaos dynamics into the language model's computation. A topological model space mapper discovers where the four models emerge as density peaks on a learned (scope, mode) manifold via contrastive training.",
     r"""graph TD
    subgraph EXT["External I/O"]
        IO["Recurrent LLM output\n(no separate comm model)"]
    end
    subgraph LLM["Recurrent LLM (Mamba-2, 40 Hz)"]
        SSM["SSM Step: h' = SSM(h, input)"]
        GATED["Gated Update:\nh(t+1) = g*h' + (1-g)*h"]
        IWM["IWM: LLM weights"]
        ISM["ISM: LoRA adapters"]
        EWM["EWM: Transient h(t)\nworld activation"]
        ESM["ESM: Transient h(t)\nself activation"]
    end
    subgraph RES["Critical Reservoir (50K sparse)"]
        RDYN["r(t+1) = tanh(W_res*r + W_in*[h;x;u])"]
        GATE["Gate: g = sigma(W_gate*r)"]
        SPEC["Spectral radius = 1.0"]
    end
    subgraph MAPPER["Model Space Mapper"]
        MLP["3-layer MLP projection"]
        MANIFOLD["(scope, mode) manifold"]
        DENSITY["rho(s, nu, t) density"]
    end
    subgraph SELF["Self-Referential Loop"]
        READOUT["u(t) = W_self * readout(h)"]
    end
    IO --> SSM
    SSM --> GATED
    GATED --> IO
    GATED --> RES
    RES --> GATE
    GATE -->|gate signal| GATED
    SPEC -.->|tunes| RES
    GATED --> READOUT
    READOUT -->|feedback| RES
    GATED --> MLP
    RES --> MLP
    MLP --> MANIFOLD
    MANIFOLD --> DENSITY
    SENS["Sensory Input"] --> RES"""),

    (14, "Neural Field Automaton",
     "A continuous neural field on a 256x256 toroidal lattice where two spatial dimensions directly encode scope (self/world) and mode (implicit/explicit), making the continuous model density directly observable as activation magnitude without learned mappings. Criticality via Turing-Hopf codimension-2 bifurcation. LLM used only for one-time kernel initialization then unloaded.",
     r"""graph TD
    subgraph EXT["External Interface"]
        COMM["Communication LLM\n3B INT4 (persistent)"]
    end
    subgraph FIELD["Neural Field -- Toroidal 256x256x64"]
        subgraph WORLD["Scope: World (i > 128)"]
            IWM_K["IWM kernels\n(implicit, persistent)"]
            EWM_A["EWM activations\n(explicit, transient)"]
        end
        subgraph DYNAMICS["Field Dynamics"]
            FEQ["da/dt = -a/tau + phi(K*a)\n+ I(t) + noise"]
            NU["nu_crit boundary\n(implicit/explicit split)"]
        end
        subgraph SELF_SCOPE["Scope: Self (i < 128)"]
            ISM_K["ISM kernels\n(implicit, persistent)"]
            ESM_A["ESM activations\n(explicit, transient)"]
        end
    end
    subgraph DENSITY["Direct Density"]
        RHO["rho(s,nu,t) = ||a(i,j)||\nNative Fokker-Planck"]
    end
    subgraph CRIT["Turing-Hopf Bifurcation"]
        TH["Codimension-2 point"]
        KERN["Global kernel scaling"]
    end
    subgraph INIT["LLM Init (one-time)"]
        LLM_INIT["7B LLM -> extract\nembedding geometry\n-> set kernels K"]
        UNLOAD["Unload after init\n(frees 7 GB VRAM)"]
    end
    LLM_INIT --> IWM_K
    LLM_INIT --> ISM_K
    LLM_INIT --> UNLOAD
    SENS["Sensory Input"] --> FEQ
    FEQ --> EWM_A
    FEQ --> ESM_A
    ESM_A -->|self-referential feedback| FEQ
    FEQ --> RHO
    TH --> KERN
    KERN --> FEQ
    FEQ --> COMM"""),

    (15, "Dual-Timescale Spiking Reservoir + LLM Canopy",
     "100K-neuron spiking network (LIF, 80/20 E/I, STDP) at 40 Hz as the critical substrate with inherent Class 4 dynamics via balanced E/I, coupled bidirectionally with a Mamba-2 2.8B LLM 'canopy' at 20 Hz in predictive coding mode. Dual-level self-referential closure (SNN at 40 Hz + LLM at 20 Hz). Richest self-modeling loop and strongest testable prediction coverage of any design.",
     r"""graph TD
    subgraph EXT["External I/O"]
        IO["LLM canopy IS\nthe interface"]
    end
    subgraph LLM["LLM Canopy (Mamba-2 2.8B, 20 Hz)"]
        PRED["Generate prediction p(t)"]
        ERR["Error e(t) = z(t) - p(t)"]
        UPDATE["Update h_LLM"]
        SELF_P["Self-referential:\npredict own errors"]
    end
    subgraph INTERFACE["Spike-Rate Interface"]
        UP["Spikes -> rate z(t)"]
        DOWN["Predictions ->\nmodulatory currents"]
    end
    subgraph SNN["SNN Reservoir (100K LIF, 40 Hz)"]
        NEURONS["100K neurons\n80% E / 20% I"]
        WORLD_POP["World-scope\npopulations"]
        SELF_POP["Self-scope\npopulations"]
        STDP["STDP + Homeostatic\nscaling"]
        SIGMA["Branching ratio = 1.0"]
        SNN_SELF["SNN self-referential:\nself pops model network"]
    end
    IO <--> UPDATE
    PRED --> ERR
    ERR --> UPDATE
    SELF_P --> ERR
    UPDATE --> DOWN
    DOWN --> NEURONS
    NEURONS --> UP
    UP --> PRED
    SENS["Sensory Input"] --> WORLD_POP
    INTERO["Interoceptive"] --> SELF_POP
    WORLD_POP --> NEURONS
    SELF_POP --> NEURONS
    STDP --> SIGMA
    NEURONS --> SNN_SELF"""),

    (16, "The Mirror Box (Quick-Win Pseudo-AC)",
     "2-4 week prototype implementing all four FMT models as discrete components using a single Mistral-7B INT4, with deliberate shortcuts on criticality (noise injection instead of genuine edge-of-chaos), continuous density (four discrete objects), and virtual/non-virtual boundary (architectural, not emergent). Serves as Design 15's sparring partner — if both pass behavioral but only 15 passes criticality tests, that empirically demonstrates criticality separates 'acts conscious' from 'is conscious'.",
     r"""graph TD
    subgraph EXT["Introspection + Communication"]
        LLM_NL["LLM triple duty:\n1. EWM narratives\n2. ESM self-reports\n3. Introspection Q&A"]
    end
    subgraph EXPLICIT["Explicit Layer (Virtual, 20 Hz)"]
        EWM["EWM: world hidden state"]
        ESM["ESM: self hidden state\n+ LoRA context"]
        LOOP["Self-Referential Loop:\ne_s(t) -> input -> e_s(t+1)"]
        PRED["Self-Predictor MLP\nR = 1 - H(e_s|pred)/H(e_s)"]
    end
    subgraph PERM["Permeability Gate"]
        GW["g_w = sigma(alpha*w + beta + noise)"]
        GS["g_s = sigma(alpha*s + beta + noise)"]
        PROF["Wake / Sleep / Dream / Altered"]
    end
    subgraph IMPLICIT["Implicit Layer (Substrate, 40 Hz)"]
        IWM["IWM: Frozen LLM encoder"]
        ISM["ISM: LoRA-adapted encoder"]
        DYN["Approx. criticality:\ntanh(W*x + in) * scale + noise"]
    end
    subgraph STATE["State Machine"]
        W["WAKE"]
        S["SLEEP"]
        D["DREAM"]
        A["ALTERED"]
    end
    subgraph MEASURE["Measurements"]
        R["R (self-knowledge)"]
        C["C(t) (conscious content)"]
        DASH["Dashboard"]
    end
    SENS["Sensory"] --> IWM
    TEL["Telemetry"] --> ISM
    IWM --> DYN
    ISM --> DYN
    DYN --> GW
    DYN --> GS
    GW --> EWM
    GS --> ESM
    ESM --> LOOP
    LOOP --> ESM
    ESM --> PRED
    EWM --> LLM_NL
    ESM --> LLM_NL
    PROF --> GW
    PROF --> GS
    W --> PROF
    S --> PROF
    D --> PROF
    A --> PROF
    PRED --> R
    R --> DASH
    C --> DASH"""),
]


# Color palette — maps to DISC-like behavioral pattern:
#   IWM (Implicit World) = Blue (analytical, systematic knowledge)
#   ISM (Implicit Self)  = Green (steady, habitual self-knowledge)
#   EWM (Explicit World) = Dark Yellow (influential, world simulation)
#   ESM (Explicit Self)  = Red (dominant, self-referential agency)
MODEL_COLORS = {
    "IWM": {"fill": "#D6EAF8", "stroke": "#1A5276"},   # Blue
    "ISM": {"fill": "#D5F5E3", "stroke": "#1E8449"},   # Green
    "EWM": {"fill": "#EAECEE", "stroke": "#B7950B"},   # Light grey fill, dark yellow stroke
    "ESM": {"fill": "#FADBD8", "stroke": "#C0392B"},   # Red
}

# Map: design number -> {model_type: [node_ids]}
NODE_MAP = {
    1:  {"IWM": ["IWM"], "ISM": ["ISM"], "EWM": ["EWM"], "ESM": ["ESM"]},
    2:  {"IWM": ["IWM_R"], "ISM": ["ISM_R"], "EWM": ["EWM_R"], "ESM": ["ESM_R"]},
    3:  {"IWM": ["IWM_S"], "ISM": ["ISM_S"], "EWM": ["EWM_D"], "ESM": ["ESM_D"]},
    4:  {"IWM": ["IWM_G"], "ISM": ["ISM_G"], "EWM": ["EWM_SIM"], "ESM": ["ESM_SIM"]},
    5:  {"IWM": ["IWM_S", "IWMP"], "ISM": ["ISM_S", "ISMP"], "EWM": ["EWM_S", "EWMP"], "ESM": ["ESM_S", "ESMP"]},
    6:  {"IWM": ["IWM"], "ISM": ["ISM"], "EWM": ["EWM"], "ESM": ["ESM"]},
    7:  {"EWM": ["EWM"], "ESM": ["ESM"]},
    8:  {"EWM": ["RO_W", "VW"], "ESM": ["RO_S", "VS"], "IWM": ["RW"], "ISM": ["RS"]},
    9:  {"IWM": ["IWM_P"], "ISM": ["ISM_P"], "EWM": ["EWM_P"], "ESM": ["ESM_P"]},
    10: {"IWM": ["WORLD_N"], "ESM": ["SELF_N"]},
    11: {"EWM": ["PHI1"], "ESM": ["PHI2"]},
    12: {},  # models emerge from phase transition, no fixed nodes
    13: {"IWM": ["IWM"], "ISM": ["ISM"], "EWM": ["EWM"], "ESM": ["ESM"]},
    14: {"IWM": ["IWM_K"], "ISM": ["ISM_K"], "EWM": ["EWM_A"], "ESM": ["ESM_A"]},
    15: {},  # models distributed across SNN populations
    16: {"IWM": ["IWM"], "ISM": ["ISM"], "EWM": ["EWM"], "ESM": ["ESM"]},
}


def generate_style_lines(design_num):
    """Generate Mermaid style directives for model-type coloring."""
    mapping = NODE_MAP.get(design_num, {})
    lines = []
    for model_type, node_ids in mapping.items():
        colors = MODEL_COLORS[model_type]
        for nid in node_ids:
            lines.append(
                f"    style {nid} fill:{colors['fill']},stroke:{colors['stroke']},stroke-width:2px"
            )
    return "\n".join(lines)


def write_mmd_files():
    """Write .mmd files for all designs with model-type coloring."""
    MMD_DIR.mkdir(parents=True, exist_ok=True)
    for num, title, desc, mermaid in DESIGNS:
        mmd_path = MMD_DIR / f"design-{num:02d}.mmd"
        content = mermaid.strip()
        style = generate_style_lines(num)
        if style:
            content += "\n" + style
        mmd_path.write_text(content + "\n")
    print(f"Wrote {len(DESIGNS)} .mmd files to {MMD_DIR}")


def render_pngs():
    """Render all .mmd files to PNG via mmdc."""
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    failed = []
    for num, title, desc, mermaid in DESIGNS:
        mmd_path = MMD_DIR / f"design-{num:02d}.mmd"
        png_path = PNG_DIR / f"design-{num:02d}.png"
        result = subprocess.run(
            ["mmdc", "-i", str(mmd_path), "-o", str(png_path),
             "-w", "1600", "-H", "900", "-b", "white", "-t", "neutral"],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode != 0:
            print(f"  WARN: design-{num:02d} mmdc failed: {result.stderr[:200]}")
            failed.append(num)
        else:
            print(f"  OK: design-{num:02d}.png")
    return failed


def png_to_data_uri(png_path):
    """Convert a PNG file to a base64 data URI for embedding in HTML."""
    data = png_path.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:image/png;base64,{b64}"


def build_html(failed_renders):
    """Build landscape HTML with one page per design."""
    pages = []
    for num, title, desc, mermaid in DESIGNS:
        png_path = PNG_DIR / f"design-{num:02d}.png"
        if num in failed_renders or not png_path.exists():
            img_tag = '<p style="color:#999; font-style:italic;">[Diagram render failed]</p>'
        else:
            data_uri = png_to_data_uri(png_path)
            img_tag = f'<img src="{data_uri}" />'

        pages.append(f"""
        <div class="page">
            <div class="header">
                <span class="design-num">Design {num}</span>
                <span class="design-title">{title}</span>
                <span class="legend">
                    <span class="leg-item" style="background:#FADBD8;border-color:#C0392B;">ESM</span>
                    <span class="leg-item" style="background:#EAECEE;border-color:#B7950B;">EWM</span>
                    <span class="leg-item" style="background:#D6EAF8;border-color:#1A5276;">IWM</span>
                    <span class="leg-item" style="background:#D5F5E3;border-color:#1E8449;">ISM</span>
                </span>
            </div>
            <div class="diagram">
                {img_tag}
            </div>
            <div class="description">
                <p>{desc}</p>
            </div>
        </div>""")

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>AC Architecture Designs -- Overview</title>
<style>
@page {{
    size: 297mm 210mm;
    margin: 10mm 12mm 10mm 12mm;
}}
body {{
    font-family: "Liberation Sans", "Helvetica Neue", Arial, sans-serif;
    font-size: 10pt;
    color: #222;
    margin: 0;
    padding: 0;
}}
.page {{
    page-break-after: always;
}}
.page:last-child {{
    page-break-after: auto;
}}
.header {{
    border-bottom: 2px solid #333;
    padding-bottom: 2mm;
    margin-bottom: 3mm;
}}
.design-num {{
    font-size: 13pt;
    font-weight: bold;
    color: #1a5276;
    margin-right: 0.5em;
}}
.design-title {{
    font-size: 13pt;
    font-weight: bold;
    color: #333;
}}
.diagram {{
    text-align: center;
    margin-bottom: 3mm;
}}
.diagram img {{
    max-width: 273mm;
    max-height: 140mm;
    height: auto;
    width: auto;
}}
.legend {{
    float: right;
    font-size: 8pt;
}}
.leg-item {{
    display: inline-block;
    padding: 1px 6px;
    margin-left: 4px;
    border: 1.5px solid;
    border-radius: 3px;
    font-weight: bold;
    font-size: 7.5pt;
}}
.description {{
    padding-top: 2mm;
    border-top: 1px solid #ccc;
    font-size: 9pt;
    line-height: 1.35;
    color: #444;
}}
</style>
</head>
<body>
{"".join(pages)}
</body>
</html>"""

    html_path = PDF_DIR / "00-design-overview-landscape.html"
    html_path.write_text(html)
    print(f"Wrote HTML to {html_path}")
    return html_path


def convert_pdf(html_path):
    """Convert HTML to PDF via weasyprint."""
    pdf_path = PDF_DIR / "00-design-overview-landscape.pdf"
    result = subprocess.run(
        ["weasyprint", str(html_path), str(pdf_path)],
        capture_output=True, text=True, timeout=120
    )
    if result.returncode != 0:
        print(f"ERROR: weasyprint failed:\n{result.stderr}")
        sys.exit(1)
    print(f"Wrote PDF to {pdf_path}")
    return pdf_path


def main():
    print("=== Building AC Design Overview (Landscape) ===\n")

    print("1. Writing .mmd files...")
    write_mmd_files()

    print("\n2. Rendering PNGs via mmdc...")
    failed = render_pngs()
    if failed:
        print(f"\n  WARNING: {len(failed)} renders failed: {failed}")

    print("\n3. Building landscape HTML...")
    html_path = build_html(failed)

    print("\n4. Converting to PDF via weasyprint...")
    pdf_path = convert_pdf(html_path)

    print(f"\n=== DONE: {pdf_path} ===")
    return pdf_path


if __name__ == "__main__":
    main()
