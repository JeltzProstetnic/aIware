---
title: "Call brief — Michiel van der Vlag (JSC), Fri 30 Oct 2026, 10:00"
---

**Zoom (his):** fz-juelich-de.zoom-x.de/j/65937740772 · ID 659 3774 0772. **Goal:** leave with an instrument exchange agreed now, a joint experiment sketched, and a named compute route.

**Who he is.** Computational scientist, Simulation & Data Lab Neuroscience, Jülich Supercomputing Centre. ICANN 2025 chapter "Complexity and Criticality in Neuro-Inspired Reservoirs". Reservoirs are The Virtual Brain whole-brain models: 96 connectome regions with neural-mass nodes, 4,096-point parameter sweeps on JSC GPUs, Lorenz prediction, and Lyapunov, DFA and PCI measured after the run. Abstract: edge-of-chaos dynamics give better memory and prediction. Code: github.com/DeLaVlag/TVB-Reservoir (MIT). Strengths: GPU code generation, massive HPC sweeps.

**The opening.** His "closed loop" feeds the network's own prediction back in. That is output feedback, not a self-model. His plan, a reservoir that models and regulates its own dynamics, is the step neither side has taken: nothing in our code feeds λ, DFA or σ back online either. We bring self-model and closure arms with the full control set (cut, capacity-matched open, scrambled), tested estimators (exact-Jacobian Lyapunov, DFA recovering Hurst +/-0.06, rate-matched branching nulls), and one honest datum. **Once λ is measured, our rate-reservoir performance peak sits in the ordered regime, not at the edge** (CRU-203, 30/30 seeds). That is a friendly contrast for him to test on his substrate, not a rebuttal.

**Joint experiment (neither side can do it alone).** A self-model reads the reservoir's state, predicts its own near-future regime (λ, DFA, σ) and its task error, and sets the global gain or coupling. The task is non-stationary prediction: drifting Lorenz, or switching to Rössler. Substrates: his TVB reservoir and our spiking pool. Arms: closed, cut, capacity-matched open, scrambled, plain homeostasis, fixed best-gain oracle. The outcome measure is cost at matched function: parameters or synapses each arm needs to reach the closed arm's error as drift grows. Every regime is measured with both instrument sets.

**What JSC buys us.** Size, seeds and plasticity. Rate reservoirs run in CPU minutes; we don't need JSC for them. Our scaled results so far are 22k–30k spiking neurons, which run on one RTX 4090. The real question needs 100k–1M neurons, at least 3 openness levels, 4 arms, 8–10 seeds and synapse-budget sweeps. Estimate (ours, from measured per-step costs): **$10^{2}$–$10^{3}$ GH200 GPU-hours with frozen weights, $10^{3}$–$10^{4}$ with plasticity**. These are single-GPU job arrays with no MPI up to ~1M neurons.

**Asks, in order.**

1. **Instrument exchange now.** We run our estimators on his public reservoir; he runs TVB-Reservoir against our controls.
2. **A JSC test project hosted by him or the SDL** for the joint experiment. These are open all year, run up to 4 months, and can include SDL support. The PI must be employed at a German institution, so we cannot apply alone.
3. **A joint proposal with him as PI:** the next NIC window (Jan–Feb 2027), or EuroHPC Development Access once the Alpine Institute is registered.
4. **A co-authored, pre-registered paper** on the joint experiment.
5. Later: SDL help porting our spiking pool to multi-GPU for >1M neurons. We have no partitioning code.

**Questions for him.**

- Could an online λ estimate drive the reservoir's own regulation?
- How would he control for a self-model whose predictions change what it predicts?
- Do Lyapunov, DFA and PCI peak at the same parameters in his sweeps?
- Can an outside collaborator be added to his existing JSC projects?

**Do not say.** "Our systems operate at criticality" or "σ≈1"; criticality is a signature, not a requirement. That closure is necessary for capability (five results killed that claim). Any result from FlowBody runs (CRU-222). A ready 1M-neuron pipeline: nothing above 30k neurons has had a task or criticality measurement, and the scaled test is a protocol to co-design. Anything about his figures, which we have not read.

**Your call, not raised by default (run-verified by crucible).** His DFA routine does not measure DFA: four confirmed defects make it read about 0.59 whatever the true exponent, and a four-line fix restores the known answers. His Lyapunov core is right but reads 10× too large, and a stable system driven by noise reads positive, so a positive value in his driven reservoir is no proof of chaos. Offer it once the exchange is agreed.
