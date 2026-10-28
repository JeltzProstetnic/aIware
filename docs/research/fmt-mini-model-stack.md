# FMT mini-model: simulator, reference models, dynamical-object instrument, 2-day plan

Research and feasibility check, 2026-10-27 (S362), WSL box (RTX 4090, 48 GB, Python 3.12).
Spec: `docs/sources/mg-2026-10-27-fmt-substrate-spec.md`. MG's two corrections given during this
task are built in: **(a)** the body representation is not one area or one column. It takes a large
share of the cortical surface, spread over several areas (somatosensory, motor, parietal, insular),
with free area left over. **(b)** "Areas" means functional differentiation across one continuous
surface, not copies of microcircuit tiles. Core principle (MG): *"the secret is in defining, finding
and analyzing spiking activity AS MODELS"*. That is why §3 is the centre of this document.

Probes ran in a throwaway venv, `/tmp/claude-1000/fmtenv`. Scripts are in `/tmp/claude-1000/*.py`.
A claim with a URL was checked against that fetched page. A claim marked **UNVERIFIED** was not.
A claim marked **MEASURED** was run on this box.

**Verdict:** use **NEST 3**. It installed with one pip command, ran a 44k-neuron STDP network at
4 s per biological second, and JSC already builds it with MPI. Build the surface from scratch in
NEST, using the thalamocortical models below as references. Do not fork one of them.

---

## 1. Simulator choice

### Install results on this box (MEASURED)

| Package | Result | Notes |
|---|---|---|
| `pip install nest-simulator` | **OK**, NEST 3.10.0 | Wheel built with OpenMP, GSL and Boost, **without MPI** (`build_info: have_mpi False`). Smoke test: 10k LIF neurons, about 10M synapses, 1 s simulated in **0.9 s** wall time at 4 Hz on 8 threads. |
| NEST at mini-model size | **OK** | 44k `iaf_psc_exp` neurons, 35.3M synapses, Poisson background, 16 threads. **Static synapses: 2.4 s per biological second, 7.0 Hz, 2.9 GB RSS. STDP on E→E: 4.0 s per biological second, 6.0 Hz, 4.3 GB RSS.** The same network built from `aeif_cond_exp` (adaptive GSL solver) took about 20 s per biological second. That run was untuned and silent, so treat the number as a cost warning only. |
| `pip install brian2` | **OK**, 2.10.1 | Brian2 2.11.0 needs Python ≥3.13 ([PyPI](https://pypi.org/project/Brian2/)), so pip chose 2.10.1. Cython target: 10k LIF neurons, 5M synapses, 1 s simulated in **3.1 s** including compilation, at 14 Hz. |
| `pip install pygenn` | **FAILS** | Not on PyPI. Installing from the GitHub tag 5.3.0 fails for lack of the system **`libffi` dev package**. GeNN docs: install "directly from github using pip"; libffi dev and a CUDA toolkit with `CUDA_PATH` are needed ([GeNN install](https://genn-team.github.io/genn/documentation/5/installation.html)). Fixing it needs root (apt). |
| Brian2CUDA / GeNN / NEST GPU on the 4090 | **Blocked for now** | The box has **no `nvcc`** (no CUDA toolkit; torch ships its own runtime). Every GPU code generator needs one. Installing `cuda-toolkit` and `libffi-dev` is a root apt step and needs MG's go-ahead. |
| Analysis: `elephant` 1.2.1, `scikit-learn`, `ripser` 0.6.15, `rsatoolbox` 0.3.2 | **OK** | **SPADE** recovered an injected 5-neuron synchronous pattern among 20 Poisson trains. **CAD** at default settings did *not* recover it (not tuned; check `max_lag`, bin size and alpha before using it). ripser found the ring in noisy circle data (H1 bar 1.64). |
| `seqnmf` 0.1.2 (PyPI) | **Installs but import fails** | It imports `pkg_resources`, which the current setuptools (84) no longer ships. Pin an older setuptools or vendor the code. |
| CEBRA | not tried | Pulls in torch, several GB. |

### Comparison

| | NEST 3 | Brian2 (+Brian2CUDA, Brian2GeNN) | GeNN / PyGeNN | Arbor | NetPyNE / NEURON |
|---|---|---|---|---|---|
| Install here | pip, works | pip, works; GPU back-ends need nvcc | blocked (libffi, CUDA) | pip ([docs](https://docs.arbor-sim.org/en/latest/)), not tried | not tried |
| LIF with refractory period, AdEx, Izhikevich | all built in (`iaf_psc_exp`, `aeif_*`, `izhikevich`, `ht_neuron`, `gif_*`; MEASURED from model list) | any equation, user-written | built in plus custom | multi-compartment cells | Hodgkin–Huxley-type cells |
| Resting rate from Poisson background | `poisson_generator`, `inhomogeneous_poisson_generator`, `sinusoidal_poisson_generator` (MEASURED) | `PoissonInput`, `PoissonGroup` | yes | yes | yes |
| Plasticity | `stdp_synapse`, `stdp_triplet`, `stdp_dopamine_synapse` (reward), `clopath`, `vogels_sprekeler` (inhibitory homeostasis), `tsodyks2` (short-term), `eprop_synapse`, structural plasticity (MEASURED from model list) | any rule, user-written | custom rules | limited | yes |
| Custom models | NESTML: generates code for NEST and NEST GPU, GPL-2.0+ ([nestml](https://github.com/nest/nestml)) | native | native | NMODL | NMODL |
| Scaling | MPI plus OpenMP; "Use NEST on your laptop or the largest supercomputers" ([repo](https://github.com/nest/nest-simulator)) | single node; Brian2CUDA is single GPU (multi-GPU support **UNVERIFIED**) | single GPU (**UNVERIFIED** for multi-GPU) | MPI plus GPU | MPI |
| GPU | **NEST GPU**: MPI multi-GPU, about 1M neurons and 1B synapses at about 70 s per biological second on one RTX 2080 Ti ([nest-gpu](https://github.com/nest/nest-gpu)); PD14 microcircuit at 1.055 s per biological second on an RTX 2080 Ti against 62.7 s for NEST on an i9-9900K ([Golosio et al. 2021](https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2021.627620/full)) | Brian2CUDA ([docs](https://brian2cuda.readthedocs.io/en/latest/introduction/index.html)); Brian2GeNN is "beta status" ([repo](https://github.com/brian-team/brian2genn)) | yes | yes | CoreNEURON (**UNVERIFIED**) |
| At JSC | **JSC builds nest-simulator 3.8** (toolchain gpsmpi 2024a, `-Dwith-mpi=ON -Dwith-openmp=ON`, SIONlib, HDF5) in its public EasyBuild repo ([easyconfig](https://github.com/easybuilders/JSC/blob/2025/Golden_Repo/n/nest-simulator/nest-simulator-3.8-gpsmpi-2024a.eb)). NEURON and nest-desktop are there too. | **No Brian2 easyconfig** in the 2025 Golden_Repo `b/` folder (checked); a user venv would work | **UNVERIFIED** | **UNVERIFIED** | NEURON module present (same repo, `n/NEURON`) |
| Fit with Michiel | **Best.** TVB–NEST co-simulation exists ([tvb-multiscale](https://github.com/the-virtual-brain/tvb-multiscale) interfaces TVB with NEST, ANNarchy and NetPyNE). Elephant analysis, NEST GPU and the JSC module all belong to the same Jülich ecosystem. His public work is TVB neural masses on GPU with CUDA kernels (`docs/research/aiw351-vandervlag-jsc-research.md`, which cites [TVB-Reservoir](https://github.com/DeLaVlag/TVB-Reservoir)). | weak | GPU code generation, close to his CUDA side, but a different ecosystem | weak (morphology) | via tvb-multiscale |
| Licence | GPL-2.0+ | CeCILL-2.1 ([PyPI](https://pypi.org/project/Brian2/)) | **UNVERIFIED** | **UNVERIFIED** | **UNVERIFIED** |

**Recommendation: NEST 3 (PyNEST) for the mini-model. Scale path: (1) JSC's MPI NEST module on CPU
nodes; (2) NEST GPU on JUWELS Booster or JURECA-DC GPUs; (3) a TVB–NEST co-simulation, with the
spiking surface embedded in a TVB whole-brain context.** Step 3 is where Michiel's toolchain comes
in. The network code is the same at every step. Only `nest.local_num_threads` and the MPI launch
change. NESTML keeps any custom neuron portable to NEST GPU.

**Brian2 is the fallback** if an unusual equation is needed fast. It has no JSC module, so it is a
detour on the scale path.

Two caveats:

- **NEST GPU's model and plasticity coverage is narrower than CPU NEST.** Before relying on the GPU
  step, check that every neuron and synapse model chosen in §4 exists in NEST GPU (**UNVERIFIED**).
- **On this box the CPU is the fast path for now.** The GPU needs a CUDA toolkit install first.

---

## 2. Reference models to reuse

| Model | What it gives FMT | Size and run time | Licence and link |
|---|---|---|---|
| **Potjans & Diesmann 2014 cortical microcircuit (PD14)** | Layer-specific connection probabilities, E/I balance, Poisson background, realistic resting rates. Use it as a **parameter source for each local patch of the surface**, not as a tile to copy (correction b). | 77k neurons, about 3×10⁸ synapses; 62.7 s per biological second for NEST on an i9-9900K, 1.055 s on an RTX 2080 Ti with NEST GPU ([Golosio 2021](https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2021.627620/full)) | Non-code material CC BY-NC-SA 4.0, PyNEST code GPL-2.0+ ([repo](https://github.com/INM-6/microcircuit-PD14-model)); [docs](https://microcircuit-pd14-model.readthedocs.io/en/latest/) |
| **Multi-area model (Schmidt, van Albada et al. 2018)** | Template for **areas joined by long-range connections** with heterogeneous within-area parameters. That is the scale-up target, too big for the mini-model. | 4.13M neurons, 24.2B synapses, 32 areas (macaque visual cortex); "a large amount of resources" needed; downscaling supported | CC BY-NC-SA 4.0, NEST 2.14 or 3.0 ([repo](https://github.com/INM-6/multi-area-model)) |
| **Hill–Tononi early visual pathway (NEST topology tutorial)** | **The closest match to the I/O topology:** retina (an input "ganglion") → thalamic relay plus reticular nucleus → layered cortex, on spatial grids. | 40×40 grid per layer; `iaf_cond_alpha`; written for NEST 2.20.1 ([tutorial](https://nest-simulator.readthedocs.io/en/v2.20.1/tutorials/topology/hill_tononi_Vp.html)). **Not in NEST 3's `pynest/examples`** (checked via the GitHub API: only `spatial/` grid examples remain), so it needs porting. | GPL-2.0+ (NEST) |
| **Multiarea Hill–Tononi thalamocortical model (R. Murphy)** | Toy brain with two hemispheres, three cortical areas each, and their thalamic nuclei, built in NEST **to study consciousness mechanisms**. Outputs LFP. | Size not stated on the page (**UNVERIFIED**); last pushed 2021-02; ships custom `ht_neuron` models for NEST 2.20.0 | **Apache-2.0** ([repo](https://github.com/ricardomurphy/Multiarea-Hill-Tononi-thalamocortical-network-model)) |
| **Destexhe 2009, AdEx thalamic, cortical and thalamocortical networks** | Parameters for regular-spiking, fast-spiking, low-threshold-spiking, thalamocortical relay and reticular cells that give **self-sustained asynchronous irregular activity**, the resting-rate regime MG asks for. | Demos with N=500 and N=2000+500 networks; NEURON plus PyNN 0.7/0.8 with a NEST back-end ([ModelDB mirror](https://github.com/ModelDBRepository/126466)); J. Comput. Neurosci. 27:493 ([arXiv](https://arxiv.org/pdf/0809.0654)) | ModelDB terms (**UNVERIFIED**) |
| **Izhikevich & Edelman 2008, large-scale thalamocortical model** | Proof of concept that a thalamocortical spiking system with STDP shows spontaneous activity and waves "without explicit programming". Too detailed to reuse; cite as a precedent. | 1M multicompartment neurons, about 0.5B synapses, 22 cell types, thalamic nuclei, white matter from diffusion tensor imaging ([OpenAlex abstract](https://api.openalex.org/works/doi:10.1073/pnas.0712231105)). Run time **UNVERIFIED**. | no public code (**UNVERIFIED**) |
| **NEST `pong` example (R-STDP, Wunderlich 2019, Gille 2022)** | **The closed-loop template:** simulate a step, read the output layer, update the environment, set input rates, repeat, with dopamine-modulated STDP. | small two-layer networks ([source](https://github.com/nest/nest-simulator/tree/master/pynest/examples/pong)) | GPL-2.0+ |
| **Spinal pathways plus muscle spindles coupled to an arm (Chacon et al. 2025)** | A NEST ↔ body-simulator loop: motoneuron spikes go out, spindle afferent rates come back, exchanged every 0.1 s through a Cython interface. | 36 spinal neurons, 6 muscle–tendon units ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12417497/)) | code "freely available" per the paper; licence **UNVERIFIED** |
| **Spiking arm control, premotor + M1 + cerebellum (DeWolf et al.)** | Spiking motor-cortex arm model | REACH code on GitHub (**UNVERIFIED** beyond the search snippet; [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5136600/) not fetched) | **UNVERIFIED** |

No published spiking model of a **cortical body schema spread over several areas behind a thalamic
bottleneck** turned up. The pieces exist separately: thalamocortical networks, cortical surfaces,
body-in-the-loop spinal and cerebellar control. Putting them together is the novel part.

**Single best reference to start from:** the **Hill–Tononi retina → thalamus/reticular → cortex
architecture**. Read Murphy's Apache-2.0 multi-area version for the area wiring and the NEST 2.20
tutorial for the spatial code. Re-implement both in NEST 3 with `nest.spatial`, using **Destexhe 2009
AdEx parameters** for thalamic and cortical cells. Take local connectivity statistics from PD14.
`ht_neuron` and `ht_synapse` are present in NEST 3.10 (MEASURED), so the Hill–Tononi cell model
itself needs no port.

---

## 3. The instrument: finding spiking activity and testing it AS A MODEL

This is the core of the project. Finding a recurring pattern is step one. FMT's claim is stronger:
some patterns **are models of something**, the body or the world. So the instrument has three tiers:
find candidates, test whether a candidate models a referent, then classify it as robust or dynamical.

### 3.1 Tier 1: find candidate objects

| Method | Tool | Finds |
|---|---|---|
| SPADE: frequent synchronous or lagged spike patterns, with surrogate statistics | `elephant.spade` (MEASURED working) | precise repeated patterns |
| CAD (Russo & Durstewitz 2017): assemblies at several time scales with arbitrary lags | `elephant.cell_assembly_detection` ([docs](https://elephant.readthedocs.io/en/latest/reference/cell_assembly_detection.html)); untuned defaults missed a planted pattern (MEASURED) | assemblies from synchrony up to rate co-modulation |
| ASSET (sequences of synchronous events), Unitary Events, GPFA latent trajectories | `elephant` ([modules](https://elephant.readthedocs.io/en/latest/modules.html)); BSD-3 ([repo](https://github.com/NeuralEnsemble/elephant)) | sequences, excess synchrony, smooth low-dimensional trajectories |
| Assemblies from ICA or NMF on binned rates | `scikit-learn` (PCA, then FastICA or NMF) | weighted ensembles, cheap and scales to the whole surface |
| seqNMF: repeated sequences with no stimulus reference | Python port `seqnmf` (MIT, [ContextLab](https://github.com/ContextLab/seqnmf)); original in MATLAB ([FeeLab](https://github.com/FeeLab/seqNMF)), [eLife 2019](https://elifesciences.org/articles/38471) (the last two not fetched, **UNVERIFIED**) | sequences, including candidate replay |

### 3.2 Tier 2: does this pattern model a referent?

The referent is known exactly in simulation: joint angles, velocities, motor commands, target
position. That is the big advantage of an in-silico body. Five tests:

1. **Decoding (does the pattern carry the referent?).** Cross-validated ridge or logistic decoders
   from the candidate's activity to body state (`scikit-learn`). Report R² against shuffles that
   keep firing rates. Decode separately from each area and from the thalamus. The thalamus sets the
   information ceiling of the bottleneck, so a cortical pattern that beats it must be integrating
   over time.
2. **Encoding (is the pattern driven by the referent?).** Fit a GLM or Poisson regression from body
   state to each neuron's spike counts. A model-like pattern explains variance that the raw input
   ganglia do not, for example position integrated from velocity.
3. **Structure preservation (is the map faithful?).**
   - **RSA:** build a neural representational dissimilarity matrix (RDM) over a set of body
     configurations and correlate it with the RDM in body space (`rsatoolbox`,
     [docs](https://rsatoolbox.readthedocs.io/en/latest/)).
   - **Topology:** persistent homology of the population point cloud (`ripser`, MIT,
     [PyPI](https://pypi.org/project/ripser/)). A 1-DOF rotating joint should give a ring (one
     long H1 bar); two joints should give a torus (two H1 bars).
   - **Learned embeddings:** CEBRA (Apache-2.0 from v0.4.0, [docs](https://cebra.ai/docs/)) with
     body state as the auxiliary variable, plus its cross-run consistency score.
4. **Prediction (does the pattern anticipate the referent?).** Decode body state at t+Δ from
   activity at t, for Δ from 0 to 300 ms. A model shows a decoding peak at Δ > 0 that beats both
   the input ganglia and a decoder that extrapolates from current state alone.
5. **Offline and prospective reactivation (does the pattern run without its input?).** Cut or
   clamp the input ganglia, or freeze the arm, and test whether the referent-specific patterns found
   in tests 1–3 recur: template matching, decoder applied to the offline activity, and seqNMF
   sequences matched to movement sequences. Recurrence with time compression counts as
   replay-like.

**Controls (required for any claim that a pattern is a model):** (i) a degree-preserving shuffle of
cortical weights; (ii) the same network without plasticity; (iii) an area map with the body
assignment permuted. A pattern counts as a model only if it beats all three.

### 3.3 Tier 3: robust or dynamical

| Criterion | Robust object (what the body does and senses) | Dynamical object (planning, simulating the future) |
|---|---|---|
| Coupling to current input | high decoding of the current referent; reliable across trials | low decoding of the current state |
| Perturb-and-return (brief current pulse into an assembly with `step_current_generator`) | returns to the stimulus-locked trajectory; measure the return time constant | diverges or switches |
| Persistence | outlasts the input autocorrelation time (attractor-like) | transient sequence |
| Input ablated | collapses, or persists as a stable state | **still occurs**: replay or preplay |
| Prediction profile (test 4) | peak at Δ ≈ 0 | peak at Δ > 0, or decodes *alternative* states |
| Where it occurs | expected mostly in the body areas | expected to recruit the free areas |

### 3.4 The three most practical tools

1. **Elephant**: SPADE for patterns and GPFA for trajectories. It reads NEST output through Neo.
2. **scikit-learn decoders and encoders plus `rsatoolbox`**: the test of whether a pattern is a model
   of something, run against the exactly known simulated referent.
3. **`ripser`** for manifold topology, plus the **perturb-and-return and input-ablation protocols**
   run inside NEST. Add CEBRA once torch is installed.

---

## 4. Two-day build plan (NEST 3, CPU, runs in minutes)

### Architecture: about 44k neurons, the size MEASURED at 4 s per biological second with STDP

```
 simulated arm (numpy, 2 joints)                    proprio ganglion (DRG-like) 300
   ^ torques                  joint angle/velocity ─> visual ganglion (target) 200
 motor ganglion (spinal-like) 200  <─ M1-like region  interoceptive ganglion 100
                                           |                  |
                                           v                  v
                        ONE THALAMUS: relay 2,000 + reticular 500 (about 1:16 of cortex)
                                 ^ corticothalamic feedback        |
                                 |                                  v
          CORTICAL SURFACE: one continuous 2-D sheet, 40,000 neurons (32k E / 8k I)
```

**The surface is one sheet, not tiles.** Neurons get random positions on a 2-D sheet. Connections
are distance-dependent (Gaussian kernel via `nest.spatial`) plus sparse long-range links. Areas are
**functional differentiation**: regions of the same sheet that differ in (1) which thalamic relay
group projects into them, (2) graded parameters such as recurrent strength, adaptation and E/I
ratio, and (3) their long-range partners. Boundaries are soft gradients, not walls.

**Share of the surface by function (correction a):**

| Region of the sheet | Share | Thalamic input | Role |
|---|---|---|---|
| S1-like (proprioceptive, somatotopic) | 12% | proprio relay | body state |
| M1-like (motor, somatotopic) | 10% | motor-thalamus loop | output to the motor ganglion |
| Parietal body-schema-like | 12% | weak; mostly cortical input from S1, M1 and visual | integrates body and target |
| Insula-like (interoceptive) | 6% | interoceptive relay | internal body state |
| **Body total** | **≈40%, over four regions** | | |
| Visual-like (target or world) | 15% | visual relay | world input |
| **Free association surface** | **≈45%** | none direct | spare capacity; expected home of dynamical objects |

The percentages are design choices, not anatomy. Adjacency follows the human layout: S1 next to M1,
parietal between S1 and visual, insula at the edge.

**Neurons and resting rates.**

- Cortex: LIF `iaf_psc_exp` with `t_ref` 2 ms (E) and 1 ms (I) for day 1; switch to `aeif_cond_exp`
  with Destexhe RS/FS parameters on day 2 if time allows. It costs about 5–8× (MEASURED, untuned).
- Thalamus: AdEx with low-threshold-spiking or TC-like parameters, or `ht_neuron`.
- Every population gets independent Poisson background, tuned to **resting rates of 1–5 Hz (E) and
  5–15 Hz (I)** with irregular firing (CV of inter-spike intervals about 1).

**Simulated body.** A two-joint planar arm with damping in numpy, coupled to NEST in 10 ms steps
using the pong-example loop: `nest.Prepare()`, then repeat `nest.Run(10.)`, read the motor
ganglion's spikes, convert agonist/antagonist rates to torques, step the arm, set the input ganglia
rates (Gaussian population code over angle and velocity), then `nest.Cleanup()`.

**Engineered (the evolution part):**

- the routing: ganglia → thalamus → cortex, and M1 → motor ganglion
- topographic (somatotopic) projections
- the area map and its parameter gradients
- E/I balance
- reticular gating of the relay

**Trained (the experience part):**

- ~~`stdp_synapse` on E→E/thalamocortical + motor babbling, dopamine STDP later~~ **SUPERSEDED
  2026-10-28 (MG rulings via crucible, CRU-227 v1 post-mortem).** v1 failed in measurement: the
  imbalanced rule erased 61–67 % of body input to parietal/insula within 10 min, and cortex decoded
  only ~7 % of joint-angle variance (thalamus 79 %). The regime now is:
  - **Balanced plasticity.** MG: *"strengthening and weakening must be balanced, evolution made brains
    that are more or less stable in their overall mapping."* Potentiation and depression must cancel
    in aggregate; `vogels_sprekeler_synapse` on I→E stays for rate homeostasis.
  - **Innate priors, not random babbling.** Behaviour starts from priors hardwired **below cortex**
    (food seen → crude reach, pain → withdrawal): clumsy, never random.
  - **Reward-gated from the start** (eating +, pain −; e.g. `stdp_dopamine_synapse`), refining the
    innate priors into automatisms. MG chose both (priors and reward gating).
  - Design draft with open questions Q1–Q4: `~/crucible/docs/design/cru227-v2-creature.md`.

### Schedule

| When | Work | Done when |
|---|---|---|
| **Day 1 morning** | Sheet, area map, ganglia, thalamus; background tuning | Resting state: rate, CV and Fano factor per region; no runaway; non-zero rest everywhere. 10 s simulated ≈ 30 s wall. |
| **Day 1 afternoon** | Arm plus closed loop, passive moves | Decode joint angles from the proprio ganglion, the thalamus, S1-like and parietal-like regions (test 1); measure the thalamic information ceiling. |
| **Day 2 morning** | STDP babbling, 2–5 min simulated (≈8–20 min wall at 4 s per biological second; **plastic thalamocortical synapses not yet measured**) | Before/after comparison: decoding, RSA and H1 topology of the S1/parietal manifold (tests 1–3), each against the three nulls. |
| **Day 2 afternoon** | First robust vs dynamical measurement | Perturb-and-return on assemblies found by SPADE or ICA (robust). Input ablation with the arm frozen: search the free and parietal regions for replay of babbling sequences (test 5), and run prediction profiles (test 4). |

**Main risks:**

- STDP in a closed loop destabilises (mitigation: inhibitory plasticity, weight bounds, short runs).
- No dynamical objects appear in two days. That would be a result, not a failure; report it with the
  nulls.
- Day 1 tuning of the background overruns.

**Scale-up path.** Same code, (1) more neurons per unit area, then (2) more surface. Run on JSC NEST
3.8 MPI, then NEST GPU, then embed in TVB through tvb-multiscale. Ask Michiel about NEST GPU's
coverage of the chosen models, and whether his GPU pipelines can run parameter sweeps of the area
gradients.

---

## Probes and artefacts

- Venv: `/tmp/claude-1000/fmtenv`: nest-simulator 3.10.0, brian2 2.10.1, elephant 1.2.1,
  scikit-learn 1.9.1, ripser 0.6.15, rsatoolbox 0.3.2, seqnmf 0.1.2 (broken import).
- Scripts: `/tmp/claude-1000/smoke_nest.py`, `smoke_brian.py`, `size_nest.py`, `smoke_ana.py`.
- Blocked, root needed: `cuda-toolkit` (nvcc) and `libffi-dev`, for GeNN, Brian2CUDA and NEST GPU on
  the 4090.
