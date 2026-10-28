# AIW-351 — Call prep: Michiel van der Vlag (JSC, SDL Neuroscience)

Call: Fri 2026-10-30 10:00 CET (Zoom). Researched 2026-10-27. Every claim below cites a page fetched on that date.
**Limitation:** the free full text on JuSER and the Springer page are behind bot-check walls and could not be read. Section 1 therefore rests on the published abstract (Radboud repository mirror) and on Michiel's public code, not on the chapter body. The "exact quotes" are from the abstract and README.

## 1. The chapter

- **Bibliographic details:** van der Vlag M, Yegenoglu A, Jimenez-Romero C, Morrison A, Diaz S. "Complexity and Criticality in Neuro-Inspired Reservoirs". In *ICANN 2025, Proceedings Part I*, LNCS, Springer Nature, pp. 645–657, DOI 10.1007/978-3-032-04558-4_52. Sources: [RWTH bibliography](https://www.informatik.rwth-aachen.de/cms/informatik/forschung/publikationen/bibliographie-komplett-/~lolj/details/?file=1029432&lidx=1) and [Radboud record](https://repository.ubn.ru.nl/handle/2066/326747). OpenAlex lists it as green OA on JuSER (FZJ-2025-04036) as a submitted version ([OpenAlex](https://api.openalex.org/works/doi:10.1007/978-3-032-04558-4_52)).
- **Substrate:** the reservoirs are The Virtual Brain (TVB) whole-brain models, not ESNs. Each node is a neural-mass model: **Montbrió–Pazó–Roxin** and **Larter–Breakspear**, both with CUDA kernels. The nodes are coupled through a TVB structural connectome (`connectivity_96.zip`, 96 regions), using tract lengths and conduction-speed delays. The weights are normalised and rescaled to a target spectral radius. Sources: [TVB-Reservoir repo](https://github.com/DeLaVlag/TVB-Reservoir) and [driver code](https://raw.githubusercontent.com/DeLaVlag/TVB-Reservoir/main/montbrio-pazo-roxin_reservoir.py).
- **Readout:** GPU ridge regression on the reservoir states (abstract, [Radboud](https://repository.ubn.ru.nl/handle/2066/326747)). The repo's task utilities include sinusoid generators and a Lorenz system (`utils/create_task.py`, `utils/lorentz.py`).
- **Measures:** the largest Lyapunov exponent, DFA, and the Perturbational Complexity Index (PCI), each as a custom CUDA kernel. The LLE is estimated **from the time series by delay embedding** (parameters `emb_dim`, `lag`, `min_tsep`, `trajectory_len`; [gpu_lya.py](https://github.com/DeLaVlag/TVB-Reservoir)). So it is computed after the run, as a measurement. It is not part of the dynamics.
- **Method:** a parameter sweep on HPC over global coupling, weight noise, conduction speed, heterogeneity and similar parameters. The repo's launch scripts use the JSC accounts `slns` (JUSUF `gpus` partition, 16 nodes) and `vbt` (JUWELS `booster`) ([hpc/](https://github.com/DeLaVlag/TVB-Reservoir)).
- **Main result:** "edge-of-chaos dynamics correspond to enhanced memory and prediction accuracy" (abstract).
- **Code:** MIT-licensed. Requirements: pycuda, torch, tvb-library and tvb-data ([repo](https://github.com/DeLaVlag/TVB-Reservoir)).

**Quotes worth using (from the abstract, [Radboud](https://repository.ubn.ru.nl/handle/2066/326747)):**
1. "It remains unknown how complexity affects the performance of simulated biological networks in predicting non-linear dynamics."
2. "…a quantitative framework for characterizing cognitive dynamics."
3. "The results suggest that edge-of-chaos dynamics correspond to enhanced memory and prediction accuracy, supporting the potential of TVB-based reservoirs for brain-inspired machine learning."

## 2. Profile

- **Role:** "Computational scientist at the Forschungszentrum Jülich (FZJ), working in the Meta-optimization for Bio-inspired Networks team". He "develops high-performance computing (HPC) solutions and GPU-accelerated methods for large-scale, whole-brain TVB simulations" ([EBRAINS Student Conference 2026](https://ebrains.eu/news-and-events/events/2026/1st-ebrains-student-conference-on-interdisciplinary-brain-research)). He is listed as SDL Neuroscience, JSC ([CNS*2023 tutorial T12](https://cns2023.sched.com/event/1ND3U/t12-vast-parameter-space-exploration-using-l2l-on-ebrains)).
- **Group:** SDL Neuroscience. Its remit includes "Mentoring computing proposals and projects" and coordinating HPC/cloud access for EBRAINS and EBRAINS Germany. It is part of JARA and of the Helmholtz Joint Lab "Supercomputing and Modeling for the Human Brain" ([SDL page](https://www.fz-juelich.de/en/ias/jsc/about-us/structure/simulation-and-data-labs/sdl-neuroscience)). The SDL page names no head. Sandra Diaz-Pier co-authors his papers and co-taught the CNS tutorial with him. A public lab head was not confirmed on a fetched page, so ask him.
- **Publications** ([ORCID API](https://pub.orcid.org/v3.0/0000-0003-0370-4655/record)):
  - Vast TVB parameter space exploration (*Applied Sciences* 2024; [arXiv 2311.13337](https://arxiv.org/abs/2311.13337); GPU TVB-AdEx, with Destexhe, Jirsa and Goldman)
  - L2L hyper-parameter exploration (*Front. Comput. Neurosci.* 2022)
  - TVB on EBRAINS as a cloud service (*NeuroImage* 2022)
  - **RateML** (*Front. Netw. Physiol.* 2022): XML/LEMS → Python and CUDA code generation for brain network models; JSC with Jirsa's Marseille group ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10013028/))
  - Multi-GPU brain simulation (*ACM TACO* 2019)
- **Tools:** TVB on GPU (RateML, vast-TVB-space), L2L (gradient-free meta-optimisation), and TVB–NEST co-simulation (forks). He is also building **tvbSBI**, a TVB-GPU simulation-based-inference EEG pipeline for an EBRAINS Days workshop that runs on JUSUF (created 2026-09) ([GitHub](https://api.github.com/users/DeLaVlag/repos), [tvbSBI](https://github.com/DeLaVlag/tvbSBI)).

## 3. JSC compute routes for an independent researcher

| Route | Eligibility (verbatim where possible) | Fit |
|---|---|---|
| **GCS/NIC** (JUPITER Booster/Cluster) | "scientists with affiliations of German universities or research facilities… nationality… irrelevant" ([JSC GCS/NIC](https://www.fz-juelich.de/en/ias/jsc/systems/supercomputers/apply-for-computing-time/gcs-nic)). Next large-scale call: 11 Jan–15 Feb 2027; JUPITER regular projects follow the same twice-yearly deadlines ([GCS](https://www.gauss-centre.eu/for-users/hpc-access)) | **Not open to MG as PI.** It would need a German-affiliated PI, e.g. Michiel. That a JSC staffer can be the PI is my inference from the wording; confirm with coordination-office@fz-juelich.de |
| **VSR (internal)** | "PIs with affiliation of Forschungszentrum Jülich" ([JSC routes](https://www.fz-juelich.de/en/ias/jsc/systems/supercomputers/apply-for-computing-time)) | Michiel only |
| **EuroHPC Development Access** | Purpose: "develop, test and optimise their applications". Allocation period one year; monthly cut-offs (1st of the month, 10:00 CET); systems include **JUPITER** ([call](https://eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-development-access_en)). Open to "academia, research institutes, public authorities, and industry established or located in an EU Member State" ([policy](https://eurohpc-ju.europa.eu/access-our-supercomputers/access-policy-and-faq_en)). Free of charge | **Best route MG can apply to himself**, once the Austrian institute exists. Not verified: whether the PI needs an employment contract with the institute (reported second-hand) |
| **EuroHPC Benchmark Access** | Monthly cut-offs, at most 3 months, "limited number of node hours", JUPITER included, access 2–3 weeks after submission ([call](https://eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-benchmark-access_en)) | Scaling tests ahead of Development or Regular access |
| **Fenix (JSC Cloud)** | "PIs with affiliations of European institutions" ([JSC](https://www.fz-juelich.de/en/ias/jsc/systems/supercomputers/apply-for-computing-time)). The 2025 call was "open to all Europe-based researchers"; it closed 13 Feb 2026 and is for cloud services ([Fenix](https://fenix-ri.eu/news/fenix-2025-call-proposals)) | Annual cycle, cloud rather than GPU HPC |
| **EBRAINS HPC** | Free, for "Europe-based neuroscientists, researchers, and developers planning to use or deploy EBRAINS tools"; also helps with EuroHPC proposals (base-infra-resources@ebrains.eu) ([EBRAINS](https://www.ebrains.eu/health-research-platforms/computing-133/high-performance-computing-327/)) | Good fit if the work uses TVB |
| **SDL collaboration** | The SDL mentors proposals and projects ([SDL page](https://www.fz-juelich.de/en/ias/jsc/about-us/structure/simulation-and-data-labs/sdl-neuroscience)). Michiel already runs on JSC allocations (`slns`, `vbt`) | Fastest start. Whether an external person can be added as a project member (JuDoor) was not verified, so ask him |

HAICORE (Helmholtz AI) and JUNIQ (quantum) need Helmholtz or German PIs ([JSC routes](https://www.fz-juelich.de/en/ias/jsc/systems/supercomputers/apply-for-computing-time)).

## 4. Framing hooks (questions for the call)

1. **Measurement to regulation.** "Your LLE is a delay-embedding estimate computed after the run. Could a windowed online version be the input to the self-model, so the reservoir adjusts its own coupling or noise to hold λ near 0? That closed loop is what my companion paper ([10.5281/zenodo.21610993](https://doi.org/10.5281/zenodo.21610993)) treats as the self-model, and your TVB-Reservoir sweep already gives the parameter map it would steer on."
2. **The self-reference problem you named.** "If the self-model predicts the system's dynamics and also acts on them, its prediction changes what it predicts. Did your meta-reservoir poster deal with that loop? What control would separate a real self-model from a regulator matched on the metrics but holding no model of the system?"
3. **Which marker to trust.** "In TVB, do LLE, DFA and PCI peak at the same parameters, or do they come apart, for example with noise or conduction speed? Which one would you use as the variable the self-model controls?" Follow-up on substrate: would a small neural-mass reservoir (fewer than 96 regions) on one GPU be enough for a first joint test before any proposal?

**Verdict:** the fastest way to compute is joint work on Michiel's existing SDL allocations. The best route MG can apply to himself is EuroHPC Development Access (monthly cut-off, one year, JUPITER), which needs the Austrian institute to be registered.
