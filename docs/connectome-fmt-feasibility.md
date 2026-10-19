# BANC fruit-fly connectome — FMT relevance & feasibility (Session 229, 2026-06-18)

Durable record of a research-agent run (2026-06-18) on the June-2026 ScienceDaily fly-connectome release MG self-forwarded (`https://www.sciencedaily.com/releases/2026/06/260610003047.htm`). Every claim sourced; flag uncertainty before reuse.

## What the study actually is
- **Paper:** "Distributed control circuits across a brain-and-cord connectome," *Nature*, 8–10 Jun 2026. DOI `10.1038/s41586-026-10735-w` (paywalled). **Open preprint (use this):** bioRxiv `10.1101/2025.07.31.667571` (v3) / mirror `PMC12324551`.
- **Dataset: BANC** = Brain-And-Nerve-Cord. First whole-CNS connectome (brain + ventral nerve cord + the brain↔body bridge) in any adult animal. ~160k neurons headline; **114,518 proofread** (optic lobes excluded).
- **Consortium:** Bates, Phelps, Kim, Yang (co-first); Wilson, Lee (HMS), Murthy, Seung (Princeton) + FlyWire / Zetta.ai.
- **The brain is NOT the new part.** The 2024 FlyWire FAFB brain connectome (~139k neurons, *Nature* `s41586-024-07558-y`) already mapped the brain. BANC's novelty = the cord + tracing signals across the brain↔body boundary. (Don't conflate with the 2020 hemibrain, ~25k.)

## Real findings (beyond the thin press release)
- Brain↔body bridge quantified: ~1,313 descending neurons, ~1,841 ascending. "Each leg runs itself" rests on a metric: effectors get their strongest input from same-body-part sensors; local sensorimotor loops dominate, long-range supplements.
- ~15 behavior "superclusters" (escape, feeding, reproduction, locomotion…) interacting via a **subsumption hierarchy** (threat overrides walking) — authors frame it as "distributed, parallelized, embodied," Brooks-style robotics, not a central CPU.
- **Recurrence explicitly documented** (the FMT-relevant part): reciprocal sensor↔motor loops; a negative-feedback landing circuit (DNp10 + AN06B002); a reproduction feedback loop (SAG → pC1 → DN → uterine motor neurons); the canonical learning loop MB → MBON → DAN → MB traced through to motor output.
- **Central complex (CX):** path integration (an internal allocentric position estimate ≈ minimal world-model) + receives **efference copies** of descending steering; characterized as **supervisory, low direct effector influence**.
- Neuromodulatory/endocrine channels annotated (insulin-like DILP, corazonin, leukokinin…).

## Data availability — downloadable: yes
- License **CC-BY 4.0**. FlyWire Codex (`codex.flywire.ai/?dataset=banc`, bulk CSV export), Neuroglancer (`ng.banc.community`), CAVE API.
- Python: `navis`, `fafbseg`, `CAVEclient` (R: `bancr` + natverse).
- **Static graph analysis** (modularity, cycle/feedback detection, motifs on the ~115k-node matrix) = laptop-doable (`networkx`/`scipy.sparse`/`igraph`).

## FMT relevance — skeptical assessment
- **A structural connectome cannot test FMT's functional predictions** (fMRI self/world × implicit/explicit; pharmacology dissociating self- vs world-model fidelity). Anatomy = what *could* talk to what, not model-fidelity dynamics. Presenting anatomy as FMT evidence would be overreach.
- **Recurrence is real but ≠ self-model.** CX (path integration + efference copy) is the best world/self-model candidate; MB→MBON→DAN is a closed self-modifying learning loop. But recurrence/efference copy are necessary-not-sufficient; nothing shows "the model models itself." A weak "structural preconditions present" claim only.
- **A fly is a LOW-probability but NOT excluded FMT-consciousness candidate** (MG correction, 2026-06-18 — do not overstate the negative). FMT is graded and substrate-agnostic ("the architecture sets the *level* of consciousness"), so basic/minimal consciousness is not ruled out a priori by being a fly; it hinges on whether **self-referential closure** is actually instantiated — not on human-likeness, and only partly on raw neuron count (scale matters but isn't decisive). The fly clearly has the *implicit* ingredients (implicit-world ≈ CX path integration; implicit-self ≈ proprioception) plus documented recurrence; what's unevidenced is an *explicit* self-model the system relates to. **Verdict: unlikely, not impossible** — which actually makes the connectome useful for a real FMT question: *does a closed self-referential loop exist at all, and how deep?* (a structural-precondition probe, complementary to the criticality angle below).
- **"Distributed local modules" is neutral** for FMT's model-kind taxonomy (FMT disclaims being a circuit diagram). Do not claim it as support.

## The one real opportunity (if pursued)
A **criticality / edge-of-chaos analysis** of a connectome-constrained spiking model. Precedent: Shiu et al. built a whole-FlyWire-brain LIF model in Brian2 (127,400 neurons, `PMC10187186`) but **never analyzed criticality** → the question is open and unclaimed.
- Ask: does the empirically-wired network sit near **branching ratio ≈ 1 / Wolfram Class-4** under biologically plausible gain, where shuffled-weight controls do not?
- A clean positive = a modest, publishable, **FMT-adjacent** result supporting FMT's **criticality pillar only** (NOT the self-model taxonomy, NOT fly consciousness). Scope honestly as "substrate satisfies a necessary dynamical precondition."
- Method: reuse/extend the Shiu Brian2 model toward BANC; long sims + global-gain sweep; measure branching ratio, power-law avalanche size/duration, Lyapunov zero-crossing. Compute: a reduced version fits WSL (48 GB / 24 cores); a full BANC sweep wants a GPU/cluster. Skill: comp-neuro + spiking sims.

## Recommendation — PRIORITY (MG set P0, 2026-06-18; AIW-90)
This is a high-EV, **gatekeeper-free** empirical avenue — pursued, not shelved. Why it could be a jackpot:
- **No gatekeepers / no consent friction.** CC-BY open data; you own the whole pipeline. The opposite of the Bonn/Ettinger route that just collapsed over data-use consent — nobody can desk-reject you out of running an analysis on public data.
- **Gold-standard substrate.** First complete whole-CNS connectome (*Nature*, 2026) — maximal field visibility.
- **Novel + unclaimed.** Nobody ran a criticality analysis on the connectome-constrained spiking model (Shiu et al. built it, never analyzed it). First-mover.
- **Clean, falsifiable FMT-pillar test.** "Real wiring sits at criticality where shuffled controls do not" is a citable empirical anchor for FMT's Class-4 requirement — the peer-reviewable citation lineage the desk-reject loop has denied.
- **Reusable program.** Track 1 (structurally operationalizing self-referential closure) becomes a "does system X have the architecture for consciousness?" probe, scalable to larger connectomes later.

Honest scope still holds: a positive supports the **criticality pillar only** (not the self-model taxonomy, not fly consciousness); a null is still informative (substrate not critical / no clean closure). The asymmetry — low cost/friction, self-owned, high upside — is what makes it P0. Execute via `docs/pending-connectome-analysis.md` (Track 1 first, laptop-doable).

Sources: Nature `10.1038/s41586-026-10735-w` · bioRxiv `10.1101/2025.07.31.667571` · `PMC12324551` · 2024 FlyWire brain `s41586-024-07558-y` · Shiu et al. `PMC10187186` · `codex.flywire.ai` · `navis`/`fafbseg` (github.com/navis-org) · brain-criticality review IOPscience `10.1088/2632-072X/ac2071`.
