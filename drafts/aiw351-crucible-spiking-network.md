---
title: "Crucible's spiking network: cell, sheet and connectome"
author: "Matthias Gruber, 30 October 2026"
---

The v2 creature as run in October 2026, with an 8,000-cell cortex.

## Cell

Every neuron is NEST's `iaf_psc_exp`: a leaky integrate-and-fire cell with exponential current synapses, separate for excitation and inhibition. It runs on PyTorch with sparse CSR weights on one RTX 4090, in float64, with NEST's exact propagators and NEST's update order.

| E_L | V_th | V_reset | C_m | τ_m |
|---|---|---|---|---|
| −70 mV | −55 mV | −70 mV | 250 pF | 10 ms |

| τ_syn ex / in | t_ref | dt | delay |
|---|---|---|---|
| 2 ms / 2 ms | 2 ms | 0.1 ms | 1 step |

Each cell receives independent Poisson background (8 kHz at 20 pA, a placeholder before per-population calibration). Signs follow Dale's law.

## Cortical sheet

- **8,000 cells, 80 % excitatory**, at random positions in a unit square (runs of 40,000 use the same code).
- **Seven areas, strips along one axis**, with blurred borders (σ = 0.02): free frontal 25 %, M1 10 %, S1 12 %, insula 6 %, parietal 12 %, visual 15 %, free temporal 20 %. The body areas (M1, S1, insula, parietal) take 40 % of the sheet. The two free areas (45 %) receive no direct sensory input.
- **Recurrent wiring, fixed in-degree 60 per cell:** 90 % drawn from a 2-D Gaussian distance kernel (σ = 0.1), 10 % uniform over the sheet. Excitatory weight 30 pA, inhibitory −150 pA (g = 5). This is NEST's `spatial` + `fixed_indegree` pattern.
- **Area names label implicit structure only.** The code refuses an area named after a model kind: explicit models are activity patterns, never regions.

## Connectome

![The v2 creature's populations and projections. Numbers on arrows are synapse counts implied by the fixed in-degrees. Bars mark inhibitory projections.](/home/jeltz/aIware/figures/crucible-v2-connectome.png){width=92%}

| Population | Cells | Role |
|---|---:|---|
| sensory ganglia: proprio, visual, intero, pain | 300, 392, 100, 100 | joint angles; a retina with a food and a danger channel; hunger; pain |
| motor ganglion | 200 | four groups (two joints × two directions) driving the arm |
| thalamic relays: proprio, visual, intero, pain | 600, 500, 200, 100 | the only route from the senses into the cortex |
| motor relay (efference copy) | 200 | motor ganglion → M1: the cortex sees its own motor command |
| higher-order relay `rel_assoc` | 500 | cortex → thalamus → cortex loop; its size is the rank of that channel |
| reticular nucleus (inhibitory) | 500 | every relay excites it; it inhibits every relay |
| striatum → GPi (inhibitory) | 300 → 100 | cortex → striatum inhibits GPi, which inhibits the relays: a selector that gates by disinhibition |
| cortical sheet | 8,000 | as above |

**Projections** (k = inputs per target cell):

- Ganglion → its relay: topographic, k = 10, 40 pA.
- Relay → its target areas: somatotopic, k = 20 per cell of the area. Proprio → S1 and parietal (half weight); visual → visual; intero → insula; pain → insula and S1 (half weight); motor → M1.
- Target areas → their relay: excitatory feedback, k = 20.
- M1 (excitatory cells) → motor ganglion: k = 20. This is the cortex's only output to the body.
- All excitatory cortex → `rel_assoc`: k = 50. `rel_assoc` → every cortical cell: k = 5.
- Relays to and from reticular: k = 1 in, k = 10 back at −60 pA. Cortex → striatum k = 20; striatum → GPi k = 20; GPi → every relay k = 5, at −60 pA.

**Below the cortex, a hardwired reflex arc** (not spiking, not learned) maps what the ganglia sense onto motor-ganglion current: a hunger-gated reach towards food, withdrawal on pain, a weaker push away from a looming danger, a push back from joint limits, and small motor noise. The cortex adds its own drive on top through M1.

**Body and world:** a planar two-joint arm (0.35 m + 0.25 m) in a small world with food items, a danger that causes pain on contact, and a hunger signal that rises over time.

## The three bottlenecks

1. **All sensing enters the 8,000-cell cortex through 1,400 relay cells.**
2. **The free areas (3,600 cells, 45 %) get no relay input.** They are reached only through the cortex itself and through the 500-cell `rel_assoc` loop, at 5 inputs per cell.
3. **The cortex acts on the body only through M1's excitatory cells → 200 motor-ganglion cells**, alongside the reflex arc.

## Plasticity

None in the frozen runs. In the learning runs: reward-gated STDP on cortical excitatory synapses from cortex and relays, and on M1 → motor ganglion; inhibitory STDP on inhibitory → excitatory synapses, with a 3 Hz target rate.

## Mapping to NEST

The cell is `iaf_psc_exp` with NEST's defaults, and the sheet is a NEST spatial layer with distance-dependent `fixed_indegree` connections. The circuit can therefore be ported to NEST for scaling without changing the model.
