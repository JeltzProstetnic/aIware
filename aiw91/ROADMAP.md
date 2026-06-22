# AIW-91 — minimal critical recursive coder: build roadmap

Constructive FMT demonstrator (the synthetic twin of AIW-90). Goal: the smallest runnable
spiking network that operates at criticality AND realises two explicit models (EWM+ESM) with
internal self-referential closure — and show the closure is **load-bearing only at criticality**.

Design source of truth: `../docs/aiw91-minimal-critical-substrate.md` (+ verbatim rationale
`../docs/aiw91-conversation-verbatim.md`). 2026 wording: ISM/IWM/ESM/EWM.

## Architecture (settled, S230)
One recursive 3-layer coder: input → **critical middle (branching σ≈1)** → output, output folded
back to input (**internal** closure / efference, not through-world). At σ≈1 the middle layer
splits into a world-code (external-driven) and a self-code (self-caused), with the self nested
in the world: **O_ESM ⊆ S_EWM** (the 2005-Innsbruck insight; 2015 book p.61/p.260/p.265).
Base/Level-0 ("nicht-erweitert"): minimal ESM+EWM, both onset axes crossed.

## Onset (two axes, S230)
- coding capacity: enough surplus neurons (~10^6–10^7 floor for "a consciousness").
- criticality **persistence**: sustained (not transient) critical dynamics. **Class −1** = no
  persistence → not conscious regardless of size.

## Increments
- **[1] Mechanism proof (small, numpy) — IN PROGRESS.** Two-hemisphere branching/threshold
  spiking net, gain knob G (critical at G·λ_max=1, same machinery as AIW-90 in discrete spikes),
  a 1-D world to track, action folded back internally. Measure EWM-decode, ESM-decode, nesting
  (ESM⊆EWM), and the **criticality × closure dissociation**: both decodes peak at σ≈1 and the
  self-model collapses when criticality is detuned OR the loop is cut. Class-0 by the taxonomy
  (too few neurons to BE a consciousness) — proves the *mechanism*. Files: `minimal_coder.py`,
  `experiment_mechanism.py`, `test_minimal_coder.py`.
- **[1b]** Trained sensorimotor readout (action = report/track the world) + the AIW-66
  double-dissociation vs EWM-only and non-closed controls, quantified.
- **[2] Human-like scale-up.** Brian2 LIF, two real hemispheres, RTX 4090, cross the ~10^6 coding
  floor + measure criticality persistence → the actual minimal-consciousness claim. Reuse
  `../tmp/connectome-analysis/_track2_worker3.py` LIF + criticality machinery.
- **[3] Levels ladder.** Added recursion depth = added closure loops (2015 erweitert ladder:
  +1 introspection … +2 explicit-model crystallisation …). Testable incrementally.
- **[later] LLM language center** (Broca/Wernicke analog) bolted on the closure core for
  report/confirmation. Body + gridworld (McFarnell ACU / simopt) for higher fidelity.

## Env
`venv/` (numpy, scipy; gitignored). Run: `venv/bin/python <script>`.
