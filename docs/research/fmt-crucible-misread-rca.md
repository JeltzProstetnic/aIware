# RCA — how crucible came to build explicit models as regions

**Date:** 2026-10-27 (aIware S362). **Trigger:** MG's spec, `docs/sources/mg-2026-10-27-fmt-substrate-spec.md`.
**Scope:** research only. Paths are absolute under `~/crucible` (C) and `~/aIware` (A).

**In one sentence:** the region reading was not a misunderstanding nobody saw. aIware put it into the first design stub, crucible built it on 2026-07-12 against two written rules that forbade it, and from August onward both projects recorded it as an error in their logs. No check could stop work on that basis, and MG never saw it drawn until the Jülich explainer.

---

## 1. How crucible represents the four model kinds

**The dominant design is "explicit model = region".**

- `C/packages/crucible/src/crucible/spiking/closure_brain.py:1–13`: "assembles the four circuits … as named region-slices in one shared `StructuredConnectome` W". The table there gives CE = recurrence pool, EWM = "world / sensory baseline", ISM = "interoceptive self-body core" and ESM = "the closure loop".
  - `:74` `DEFAULT_SIZES = {"CE": 8000, "EWM": 6000, "ISM": 4000, "ESM": 4000}`.
  - `:79–89` a hand-written table of connection probabilities between the blocks.
  - `:15–25` closure is the ESM→rest block of W, switched on and off.
  - **There is no IWM at all.** A "criticality engine" (CE) takes its place, so the network has three regions on the explicit and self side and none for implicit world knowledge.
- `spiking/structured_connectome.py:3–7`: the circuits "are named contiguous region-slices in a single shared recurrent matrix W". First built in commit `435e980`, 2026-07-12 (CRU-40 Step 6).
- `spiking/self_model.py:1–10` (CRU-196): "the SELF REGION's taught content". The rest→ESM weights are trained to predict the body, and the docstring says "Nothing here emerges." `spiking/world_map.py:1` likewise puts an egocentric map into "the world region (EWM)".
- Track A (`fmt/models/models.py`, from the 2026-07-06 founding plan) ports simopt's FMT agent. In it the four models are four separate objects, and `ExplicitWorldModel` and `ExplicitSelfModel` are readouts (`C/docs/implementation-plan.md:187–209`).
- `C/docs/milestones.md:41–45` admits it: "`DEFAULT_SIZES` fixes CE / EWM / ISM / ESM as four named regions … any text implying we have shown self/world differentiation is wrong."

**Parts that already treat explicit models as activity. These are the salvageable ones.**

- `C/docs/implementation-plan.md:33–38` gets the right definitions:
  - "Explicit (activity x(t) projected)", with the implicit models as W.
  - "Emergent self-attractor (do not hand-wire ESM) … we do not stipulate an 'ESM module'."
- `C/docs/design/biological-substrate-structure.md` (CRU-28, 2026-07-07, commit `8d3eb67`):
  - Thalamic relay → L4/L2-3/L5/L6 laminar column, CBGT loop, peripheral CPG ganglia.
  - "no ESM module is introduced — the self-basin must emerge in the structured spiking pool."
  - A test against smuggling in the self-model: does a self-attractor still form when the body's signals are replaced by noise?
  - This is the closest existing document to MG's spec. **It was never built.**
- `C/docs/milestones.md:21–24`, MG's chain of 2026-08-05: "a self model emerges within the main attractor … we can actually find the explicit models in a spiking substrate". The matching backlog items, both open at P2, are **CRU-72**, the "decompilation pipeline" (`C/backlog.md:231`), and **CRU-61**, an evolved connectome built semi-emergently (`:196`).
- `metrics/stability.py:1–15` has three measures: autocorrelation timescale, basin recovery and persistence across states. They are the right raw material for telling robust activity from dynamical activity. Today they are applied to the labelled regions, not to patterns found in the data.
- MG's 2026-07-12 discriminator ("the self-model = the most stable, longest-living …", `C/docs/decisions.md:1889`) is in substance about robust sustained activity. It was turned into a ranking of the regions.
- The `world_map.py` thermometer of bistable cells is a hand-built sustained pattern: a small, working instance of a robust explicit-content carrier.

## 2. Where the region reading entered

**It came from aIware, and crucible made it concrete.** The chain:

1. **2026-06-18, aIware S230 stub** (`A/docs/aiw91-minimal-critical-substrate.md`, commit `d637bca4`):
   - It inverted the axis. Implicit = "the network's own raw dynamics", corrected later at `:22–27`.
   - Its §"Minimal architecture sketch" (`:47–60`) "functionally partitioned" one pool into a substrate, "**EWM: a readout+recurrent module**" and "**ESM: a module whose 'world' is the system's own state**".
   - **This is the earliest text that maps explicit models to modules.** The correction note in the same file says "crucible's whole region scaffold descends from this file".
2. **2026-07-06, aIware S242, same file `:200–205`, locked decision #2:** "The self-model EMERGES from embodiment … we do not stipulate an 'ESM module'." That is correct. **The design authority stated the right reading two weeks after the wrong one, but left the module sketch above it standing.** crucible's founding commit `7d4a92d` (2026-07-06) cites the file as "Design authority".
3. **2026-07-07, MG directive** (`C/docs/decisions.md:2166–2174`): structure the substrate (basal ganglia, cortex, layers, peripheral ganglia), and "never hand-wire the self-model / ESM". It was designed as CRU-28 the same day and **deferred** by the meta-review (`C/docs/meta-review-2026-07-07.md:41–42`), which called structure "a 2nd-order 'does structure help' question".
4. **2026-07-12, the moment the regions were built.**
   - `C/docs/design/cru40-b1-R1-first-slice-plan.md:44–52`, written by a Plan agent and labelled "provenance", adopts "the minimum four circuits", with "*circuit* = named contiguous region_slice in W".
   - The decision that day (`C/docs/decisions.md:1897`) says "closure/ISM loop **hand-wired**". That directly contradicts S242 #2 and the MG directive of five days earlier.
   - The pressure behind it: five "DEAD" results in a row, the stationary-closure theorem (`:1904–1910`), and a turn to "build-first".
   - MG did see the plan's question "4 enough?" (`first-slice-plan.md:105`) and approved the closure-dependence discriminator. As written down, he approved a test, not a reading of FMT.

**Do the aIware texts invite the region reading?**

- **The FMT master does not.** `A/paper/full/four-model-theory-full.md:170` defines the implicit row as "stored in physical connectivity". `:232` says "The explicit models … are generated processes — dynamic patterns of activity", and `:256` "patterns of activity — … transient electrochemical dynamics". The one weak phrase is the permeability language, "the transfer to the ESM is blocked" (`:424`), which reads like a channel between populations.
- **The formalization does invite it by its wording.** `A/paper/fmt_formal/fmt-formalization.md:41` treats the four models "as four *regions* in a continuous space of modeling activity", and `:92` defines "four regions R_IWM … R_ESM" (since 2026-02-17, `b0ff2f50`). These are regions of an abstract scope/mode space, not of a network. But it is the same word.
- **The companion paper describes crucible's regions without objecting** (`A/drafts/companion-computational-paper-draft.md:147, 171–179`, "two-pool spiking network", "the self region", added in S316, 2026-08-27). The paper's own §77 disclaims "four discrete modules". aIware wrote the framing down; it did not check it against the architecture.
- **The registry already names the error.** `A/.claude/knowledge/fmt-misconception-registry.md:35–39` has Misread #5, "Over-localization (a region-box per model) … 'which region is the EWM?' is a level error", and #1, "four boxes" (`:11`). It was created 2026-07-26 (`b1ddcab2`).
  - **Why it did not stop crucible:** (a) it was written two weeks after the regions were built; (b) it is framed as defence against *reviewers* ("Preemption: …"), not as a check on the build; (c) crucible's `CLAUDE.md` does not reference it (no hit in `C/CLAUDE.md`, `C/docs`, `C/.claude`).

**After that, the error was recorded and not acted on:**

- **2026-08-12** `C/docs/decisions.md:3318`: "calling a circuit 'the implicit self-model' is wrong (audit filed; **region names encode the error**)." aIware AIW-221 (`A/backlog.md:221`, closed S306 2026-08-23) fixed aiw91 and noted "**Still open on crucible's side** … their substrate's region names encode the same error".
- **2026-08-19**, MG's visualization ruling (`C/docs/decisions.md:503`): "definitely NOT a pre-labeled and pre-defined clustering by ESM EWM etc." It was filed as a rule for the visualization only. The same entry measured the substrate as "a blob" (Newman Q = 0.196) with "no sensory hierarchy, relay nucleus …".
- **2026-10-07** `C/docs/design/book2015-building-blocks-reading-2026-10-07.md:28–32`: "Four labelled recurrent pools … no explicit low-rank constriction … The self pool therefore had nothing to model."

## 3. Had MG stated the biological target before?

**Yes, three times, each time in crucible's own logs.**

| Date | Where | MG's content | What happened to it |
|---|---|---|---|
| 2026-07-07 | `C/docs/decisions.md:2166–2174` | substrate structure: basal ganglia, cortex, cortical layers, per-region counts, **peripheral ganglia**; ESM must emerge | designed as CRU-28 (thalamic relay + laminar cortex + ganglia); **deferred by the meta-review, never built** (`C/backlog.md:171`, still open) |
| 2026-07-11 | `C/docs/decisions.md:1945–1950` | "**CORTEX-VARIETY PRINCIPLE**: … a VARIED landscape of topologies and kinds (**Brodmann areas**) … layered on a complete subcortical (fish-level) brain — *It's that cortex part we must find*" | **dropped the next day.** The 2026-07-12 four-circuit plan does not cite it |
| 2026-08-05 | `C/docs/milestones.md:21–24` | "self model emerges within the main attractor … find the explicit models in a spiking substrate" | became CRU-72 and CRU-61, both P2 and "revisit after MoC7" |

The 2015 book's "constriction" (concave net) and its ganglia, read 2026-10-07 (`book2015-building-blocks-reading…:6–23`), anticipate the "thalamus-like restriction". They were built only as **rate** blocks (`C/packages/crucible/src/crucible/rate/blocks.py`, Routes A/B), which is the "abstracted neural network" MG now rejects.

"Robust" against "dynamical" patterns, and "dynamical object", appear nowhere as MG's words before today. The closest earlier statements are "main attractor" and the 2026-07-12 "most stable, longest-living" discriminator.

**Where the target was dropped:** at the 2026-07-12 fork, when "build-first" turned a deferred structural programme (CRU-28) into a hand-labelled four-block matrix. After that, every later step built on the blocks.

## 4. What is genuinely reusable

1. **The spiking engine, `SparseLifPool`** (`spiking/sparse_lif.py`): CSR on GPU, Dale's law per source, fan-out normalized, plastic masks, a three-factor rule.
   - **Gaps against MG's spec:** the refractory period exists (`configure_bio_cell(t_ref=…)`, `:361`, CRU-205) but is **off by default**. The membrane floor and STP are also off by default (`bio_cell.py:10`). The default background (`rest_frac=0.9, bg_rate=0.015`, `:215–216`) holds cells just below threshold rather than giving a calibrated non-zero resting rate.
   - Turning these on is a configuration change, not a rewrite.
2. **Throughput, measured** (`C/docs/results/cru40-b1-R1-step2-substrate-throughput.md:31–43`): about 20.6 ps per synapse per step, bound by memory bandwidth. That means real time only up to ~4.9e7 synapses (30k neurons ≈ 0.81× real time, 100k ≈ 0.24×, 1M at K = 2000 ≈ 41× slower than real time). This number sizes MG's architecture before anything is built: a ganglia → thalamus → cortex sheet with sparse long-range wiring fits only if the cortex is sparse (K ≲ 500 at 100k neurons).
3. **Instruments that are validated and honest about their limits:**
   - Branching σ always reported beside a **rate-matched surrogate** (CRU-194/198). This retired the claim that σ ≈ 1 shows criticality, which is a real methodological result.
   - **Lyapunov and damage spreading** (`experiments/spiking_twin.py`; fp64 accumulation needed on the 4090).
   - **DFA** and the regime battery (`metrics/regime_battery.py`, `metrics/criticality.py`).
   - Percolation and Class-4 membership with a guard against periodic activity (`metrics/percolation.py`).
   - The stability triplet (`metrics/stability.py`): autocorrelation timescale, basin recovery, persistence across states.
   - Together these are about 80 % of a **dynamical-object detector**. What is missing is the first step: *finding* objects without labels (clustering co-active assemblies, or recurrent states in the space of population activity), and only then scoring each one as robust (long timescale, persistent across states, recovers its basin, locked to body and senses) or dynamical (short-lived, internally driven, predicts ahead). CRU-72 is where that step belongs.
4. **The stationary-closure theorem** (`C/docs/decisions.md:1904–1910`): for a task that is deterministic and stationary within an episode, a pre-compiled table can always replace self-re-entry. It holds whatever the architecture, so it carries over. It tells the new programme to use open-ended or novel tasks, not fixed ablations.
5. **CRU-28's design and the quadruped blueprint** (`docs/design/biological-substrate-structure.md`, `quadruped-connectome-blueprint.md`): neuron counts for thalamus, cortical layers and CBGT loop, the test against a disembodied self, and the mapping of ganglia to the ESP32. This is a ready first draft of MG's topology.
6. **The embodiment seam** (`embodiment/`, the WAVEGO adapter) and the MoC7 body. These are untouched by the misreading.

**Not reusable as FMT evidence:** every result that ranks or ablates *named* regions (Readout A/B, closure ON/OFF of the ESM block, CRU-196 "self-region content"). It may still be valid as dynamics engineering.

## 5. Root cause

The FMT definition was right in the master paper and right in aIware's locked S242 decision. But **no step required the built architecture to be checked against it, and no document showed MG the architecture as a picture before months of work stood on it.**

- The wrong reading arrived as a pragmatic plan written by an agent (2026-07-12), under pressure from repeated nulls.
- It contradicted two written rules: S242 #2 and the 2026-07-07 directive.
- The contradiction was later recorded three times (2026-08-12, 2026-08-19, 2026-10-07) in decision logs. Those logs are append-only narrative that nothing re-reads as a blocking condition.
- The misconception registry was aimed at reviewers, not builders, and crucible does not load it.
- crucible's reporting rule (`C/CLAUDE.md:97`, 2026-08-11) translated "ESM region" into "the self-model circuit" for MG. That keeps jargon out, but it also keeps the architectural claim out of sight.
- The deferral of CRU-28 ("structure is second-order") was never revisited, even after MG restated the cortex principle four days later.

**Cheapest durable fix (proposal only):**

1. **An architecture-conformance gate.** Keep a short `FMT-substrate-spec.md` (today's six points, signed by MG) in aIware, plus a one-page **architecture diagram that MG signs off**.
   - Any crucible design doc that introduces or changes a substrate must include a conformance table against those points.
   - The table must answer "where do the explicit models live: activity or structure?" with a yes or no.
   - A design that labels a population with a model-kind name must cite MG's sign-off of a diagram showing that.
2. **Load the registry in crucible**, and add Misread #5 as a build check.
3. **Turn "error recorded, not acted on" into a blocking backlog item.** When a decision entry says a built component "encodes the error", it must open a P0 item that names the component.

Item 1 is the load-bearing one: one diagram per architecture change, about 10 minutes of MG's time.
