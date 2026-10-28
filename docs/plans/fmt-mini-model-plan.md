# FMT mini-model — experiment plan to Fri 2026-10-30 and the scale-up with JSC

aIware S362, written 2026-10-27 ~23:30. Owner: MG. Build: crucible (CRU-227). Binding spec:
`docs/sources/mg-2026-10-27-fmt-substrate-spec.md`. Requirements with line refs to the master:
`docs/research/fmt-mini-model-requirements.md` (AM-x = activity-model criteria, C-x = commitments, P-x =
predictions). Working definition of "pattern P models X": crucible `docs/fmt-substrate-assets-2026-10-27.md` §3,
**pending MG's ruling**.

## What we are building, in one paragraph

A biologically plausible spiking network: NEST-equivalent `iaf_psc_exp` cells with refractory periods and
calibrated non-zero resting rates. Peripheral ganglia connect it to a simulated two-joint arm and a simple visual
scene. Everything passes through ONE thalamus, which is both the I/O relay and the low-rank channel of the
thalamocortical loop. A basal-ganglia selector gates the relays. Behind the thalamus is one continuous cortical
sheet with soft area gradients: body representation ~40% (motor, somatosensory, insular, parietal), vision 15%,
45% free. The **implicit models are the wiring and the weights**. The **explicit models are not built**. They
are what we look for: activity objects that the detector finds without labels, then tests as models (write, read,
boundary, generated) and places on the scope (self↔world), kind (robust↔dynamical) and loop axes.

**Status at writing (crucible e90c341, measured):** 43,700 neurons, 6.77M synapses, ~1.0 s wall per model-second
on the 4090, resting rates calibrated (cortex E 2.7 Hz, I 8.5 Hz, relays ~5 Hz). The FIND step of the detector
recovers planted assemblies and finds none in rate-matched noise.

## Conformance table (every substrate change must keep these true)

| Check | Must hold |
|---|---|
| Explicit models | appear only as detected activity; no population, area or mask is named EWM/ESM or another model kind (sheet.py already refuses such names) |
| Body model | spread over a large fraction of the surface, never one area |
| Thalamus | one; relay and loop channel; its loop rank = size of `rel_assoc` |
| Biology | refractory period on; resting rates non-zero and calibrated; E/I separate |
| Criticality | reported only beside a rate-matched null, never a target |
| Evidence | no result ranking or ablating named regions counts as FMT evidence |

## Milestones

**M1 — Wed 28 Oct: the body in the loop.**
- Couple the two-joint arm: proprioception and motor ganglia, 10 ms body step. Run motor babbling (random motor
  commands with proprioceptive feedback).
- Switch on STDP plus inhibitory plasticity, so the implicit models form from the body's regularities.
- Measures: rates stay physiological, no runaway; the ISI CV, which is 0.61–0.70 today; at what CV the irregular
  regime holds.
- **Gate:** 10 model-minutes of babbling without instability.

**M2 — Wed/Thu: the ANALYSE steps of the detector.** In order, on the found objects:
1. WRITE: fit a map from the object to the arm state. It must beat the rate-matched null and an
   input-filter/delay-line null.
2. READ: replace the object with a frozen tape or a scramble. Does downstream activity or motor output change in
   the direction that anticipates the arm's consequences?
3. BOUNDARY: respond to perturbations inside versus outside the arm's domain.
4. GENERATED: suppress activity globally, restore it, and check the object reconstitutes with W unchanged.

Then place each object: scope from the reafferent versus external share of its content; kind from its coupling
to current input against its information about future arm states with internal onset; loop membership from a
white-box trace.
- Object tracking across cells (identity by causal signature, AM-5) is in scope only if M2 finishes early.

**M3 — Thu 29 Oct: the first FMT test, P1.**
- *The first stable activity object a body-coupled network forms models the body* (master l.531, which says this
  "has not yet been measured in spiking networks").
- Protocol: track object emergence over babbling time. Record the first object that passes all four model
  criteria, and its scope.
- Controls: the same network with (a) the arm replaced by rate-matched input of no structure, and (b) the
  thalamic loop rank set to minimum.
- Pre-register the readouts before the run.
- **What would count against P1:** the first model-passing object is world-scoped, or appears no earlier with
  the body than with structureless input.

**M4 — Thu night: package for Michiel.**
- A one-command run and the result files.
- A NEST port plan. The cell is already NEST-exact, so the port is the wiring builder plus the plasticity rules.
- The two scale experiments below.

## What we bring Michiel on Friday (the ask)

Not a brief. A running model with a first measurement, and two experiments that need his hardware and his skills:

- **S1 — size and areas.** The same architecture at 10^5 → 10^6 neurons in NEST (MPI on JSC CPU nodes, later
  NEST GPU). Question: as the surface grows and the free area grows with it, do dynamical (prospective) objects
  appear that the small model cannot hold? This tests the claim that free compute area carries simulation of
  the non-present.
- **S2 — his connectome as the long-range scaffold.** His TVB 96-region connectome supplies long-range
  structure; spiking areas are embedded via TVB–NEST co-simulation, his specialty. The body representation spans
  the somatomotor and parietal regions. Question: does the activity-model detector find the same object classes
  in a connectome-shaped cortex?
- **His instruments** (Lyapunov, DFA once fixed, PCI) run on our objects, our detector runs on his reservoirs,
  and the DFA fix goes to him as a gift (MG decides timing, S362-8).

## Risks, stated

- **Thursday buys a working instrument and substrate, maybe one P1 measurement — not a confirmed FMT result.**
- STDP with babbling can run away or go silent. M1's gate is there to catch that before M2/M3 build on it.
- The definition of "models X" is pending MG's ruling. If he changes it, M2 changes with it.
- Cortex-informed training, a robot in the loop and plasticity at scale are out of scope before Friday.

## Decisions for MG (numbered)
- **P-1:** approve crucible's "pattern P models X" definition as the working definition (crucible assets §3).
- **P-2:** approve P1 as the first test (vs another prediction from requirements §3).
- **P-3:** visual input in the mini-model now (a moving dot) or body only until after the call?
