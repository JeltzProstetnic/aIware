# AIW-130 JAIC draft §6–9 checked against the crucible record (S365, 2026-10-28)

Manuscript: `drafts/aiw130-jaic-draft.md` l.146–203 at HEAD d6a43433 (clean tree). Companion: `drafts/companion-computational-paper-draft.md`.
Sources, newest measured result first: `~/crucible/docs/decisions.md` (all October entries l.1–125 and l.4555–5322; September and
July entries where a claim depends on them), `~/crucible/docs/results/` (every file touched since 2026-10-01, plus the older results the
claims rest on), crucible `backlog.md`, the running CRU-231 logs in `/tmp/cru231-*.log` (read only), and aIware's S362/S363 rechecks, RCA
and MG's signed substrate spec. Nothing was run and no job was touched.

## Verdict

Every number in §6–9 matches crucible's record: 0.98 against 0.78, where chance is 0.8 because one of five moves enters the hazard; d =
2.44 on 40 seeds; a reactive bracket at 0.00–0.33; survival 0.29–0.33 against 0.17–0.25; 30 of 30 reservoirs peaking in the ordered
regime. All seven "Gruber, 2026b, §N" pointers land on text that says what is attributed to it, and "the decisive test is open" is
correct. The three CRU-231 jobs running now compare a learning creature with a frozen twin. They measure how much body content survives
plasticity, manipulate no closure and test no cost at matched function, so they do not bear on it. The defects are about status and
framing, and none is a number. **(1)** §6(a) and §9 still describe the minimal design as one spiking pool "functionally differentiated
into" an explicit world-model and an explicit self-model. That is the AIW-91 sketch, which aIware marked SUPERSEDED on 2026-10-27 after
MG ruled that explicit models are activity, never regions. **(2)** The closure knob and the closure ablation are described as cleaner
than crucible measured them to be. On a recurrent substrate the cut leaves closed systems standing, and on the spiking substrate the two
arms could not be held at a matched operating point. **(3)** "Under re-analysis" overstates the state of the CRU-36 null. It is flagged
at risk and has not been re-run, and the item that would re-check it is parked. **(4)** The planner caveat names samples where the
record names capacity. **(5)** A parenthesis places open-ended capability in the ordered regime, but only shallow-task optima were
measured there. **(6)** "Self region" and "self-circuit" carry the region reading.

Counts: ACCURATE 32 · OUTDATED 4 · OVERSTATED 6 · UNDERSTATED 2 · UNVERIFIABLE 1 · WRONG 0 (45 claims).

## Claims table

Paths: C = `~/crucible`, A = `~/aIware`, comp = A/drafts/companion-computational-paper-draft.md. Quotes for every non-ACCURATE row follow
the table.

| # | claim (short) | ms line | verdict | source file:line | proposed fix |
|---|---|---|---|---|---|
| 1 | Heading "the detector specified to implementation" | 146 | ACCURATE | A/docs/research/aiw130-recheck-s362.md (F4 "runnable" fixed) | — |
| 2 | "The smallest system … is a single recurrent spiking pool … functionally differentiated into an explicit world-model … and an explicit self-model" | 150 | **OUTDATED — conflicts with MG 2026-10-27** | C/docs/decisions.md:81–85, 88; A/docs/aiw91-minimal-critical-substrate.md:1, 51–60; A/docs/sources/mg-2026-10-27-fmt-substrate-spec.md:5 | see Q2 |
| 3 | "a single experimental knob … makes closure measurable" | 150 | **OVERSTATED** | C/docs/results/cru58-closure-off-is-two-closed-systems.md:4, 10; C/docs/results/cru40-b1-R1-readout-a.md:16–17; C/docs/decisions.md:2377–2378 | see Q3 |
| 4 | Subsampled branching estimate reaches unity on firing rate alone (2026b §3.2) | 150 | ACCURATE | comp:105; C/docs/results/cru194-regime-2026-09-29.md:263–268; cru203…:219 | — |
| 5 | Every branching ratio reported beside a rate-matched surrogate; capability set by task performance | 150 | ACCURATE | C/docs/results/cru203-edgepeak-replication-2026-10-01.md:122–126; C/docs/decisions.md:4766, 4775–4776 | — |
| 6 | "a buildable design, not yet instantiated" | 150 | ACCURATE (status) | No crucible build of this design; CRU-227 builds MG's different topology (C/backlog.md:88) | — (see Q2 for framing) |
| 7 | Run on toy gridworld and rate-reservoir models | 152 | ACCURATE | C/docs/results/artifact-audit-2026-10-07.md:34 (all four "SAFE — not spiking") | — |
| 8 | Transfer 0.98; ablated "stays at chance (0.78; d = 2.44, 40 seeds)" | 152 | ACCURATE | C/docs/results/p1-causal-transfer.md:7, 19 ("Chance = 0.8"), 27, 31, 44 | — |
| 9 | Shared with causal-representation learning, not evidence over rivals | 152 | ACCURATE | comp:131; C/docs/results/fmt-evidence-ledger.md:24 | — |
| 10 | Reactive bracket "scores 0.00–0.33 at the same sample budget; nothing shows … with more samples" | 152 | **OVERSTATED** | C/docs/results/cru40-b1-R1-S0pre2-gridworld-fitted-arms.md:73, 75–78, 87–93 | see Q10 |
| 11 | Survival 0.29–0.33 vs 0.17–0.25, small margin | 152 | ACCURATE | C/docs/results/cru32b-self-preservation.md:28–31 | — |
| 12 | Rate peak for the medium task only, at base size; 30/30; ordered; moves with memory horizon; not evidence the edge pays | 152 | ACCURATE | C/docs/results/cru203-edgepeak-replication-2026-10-01.md:147–151, 170–173, 176–180, 329–331 | — |
| 13 | "Data and protocols for all four results are in the companion (§4)" | 152 | ACCURATE | comp:115–141 (§4.1–4.4) | — |
| 14 | Interaction untested; no experiment varies closure and regime together | 154 | ACCURATE | CRU-203 has no closure arm; CRU-204 leg B swept gain on the closure arm only (C/docs/decisions.md:4779); CRU-36's planned 2×2 was never run (C/backlog.md:48) | — |
| 15 | Re-entry toggle on an undifferentiated spiking reservoir gave no advantage on an already-solved task (2026b §6) | 154 | ACCURATE | C/docs/results/cru36-substrate-closure-null.md:14–35; comp:222 | — |
| 16 | "That null is under re-analysis after a simulator-artefact audit" | 154 | **OVERSTATED** | C/docs/results/artifact-audit-2026-10-07.md:21, 68; C/backlog.md:95; C/docs/cru226-juelich-substance.md:302 | see Q16 |
| 17 | "the framework predicts a null here, since the reservoir had no distinct self- and world-models" | 154 | **UNDERSTATED** | comp:224 | folded into Q16 |
| 18 | Closure ablation at matched recurrence: "only in the closed version should removing the self-model's contribution degrade the world-model" | 156 | **OVERSTATED** | C/docs/results/fmt-evidence-ledger.md:165; ms l.158; C/docs/results/cru40-b1-R1-readout-a.md:16–17 | see Q18 |
| 19 | "(in the rate reservoirs tested so far, in the driven-stable, ordered regime; Gruber, 2026b)" | 156 | **OVERSTATED** | C/docs/decisions.md:4666–4670, 4725–4727; comp:234 | see Q19 |
| 20 | Substrate baseline: rate reservoir at its measured edge (driven λ ≈ 0) | 156 | ACCURATE (proposal) | C/docs/results/cru203…:58–65, 300–308 | — |
| 21 | Branching ratio counts only when it departs from the surrogate's value | 156 | ACCURATE | C/docs/results/cru203…:124–125; cru194…:220–222 | — |
| 22 | "toy-scale mechanism demonstrations and one strong statistical dissociation" | 158 | ACCURATE | C/docs/results/fmt-evidence-ledger.md:156–158 | — |
| 23 | "The decisive test is open" | 158 | ACCURATE | C/docs/cru226-juelich-substance.md:306 ("The scaled matched-function test is undesigned"); CRU-231, see below | — |
| 24 | A loop-cut capability test cannot come out positive on a deterministic stationary task (2026b §8) | 158 | ACCURATE | comp:244; C/docs/results/fmt-evidence-ledger.md:165 | — |
| 25 | The committed test is cost at matched function on an open-ended workload | 158 | ACCURATE | C/docs/decisions.md:1169–1170; comp:244 | — |
| 26 | Check 2 graded, capacity- and novelty-relative, novelty outrunning any amortizer | 158 | ACCURATE | C/docs/results/fmt-evidence-ledger.md:165 | — |
| 27 | "The companion states the decisive test as cost at matched function" | 160 | ACCURATE | comp:244 | — |
| 28 | Toy systems with and without the target components differ in capability as the theory expects | 162 | ACCURATE (scope: the four results) | as rows 8–12; see Q-open 3 | — |
| 29 | "the scaled, spiking, closure-driven demonstration remains to be built" | 162 | ACCURATE | C/docs/results/fmt-evidence-ledger.md:158–159; C/docs/cru226-juelich-substance.md:304–306 | — |
| 30 | Worked-example thresholds "20% relative rise", "m ∈ [0.97, 1.03]" | 164 | **UNVERIFIABLE** (illustrative) | no crucible source; crucible's operational band is MR m ≥ 0.9 (C/docs/results/cru198-remeasure-2026-09-29.md:58); master cites waking cortex σ ≈ 0.98 (A/paper/full/four-model-theory-full.md:489) | none required; optionally say "for illustration" |
| 31 | Near-unity m with scale-free avalanches "corroborating", beside a surrogate that fails to reproduce them | 164 | ACCURATE | consistent with C/docs/decisions.md:4754–4761 (signature) and 4775 (descriptive, never a gate) as long as it never counts toward a pass | — |
| 32 | "a returning path through the self region is what recurrence already gives (2026b, §5.1; a graph result)" | 174 | **OUTDATED — framing conflicts with MG 2026-10-27** | C/docs/decisions.md:88–89; comp:181; A/docs/research/fmt-crucible-misread-rca.md:59, 102 | see Q32 |
| 33 | Recurrence "*necessary* on this account but not sufficient" | 174 | ACCURATE | a measurement-level necessity (a persistent component to clamp), not the capability necessity crucible killed (C/docs/cru226-juelich-substance.md:288) | — |
| 34 | Near-criticality the usual signature, not the requirement; criticality data cannot disconfirm (2026a §3.7) | 186 | ACCURATE | C/docs/decisions.md:4751–4763; A/paper/full/four-model-theory-full.md:17, 176 | — |
| 35 | Check 3 alone never yields a positive verdict; "conscious" on criticality alone misreads the theory | 188 | ACCURATE | C/docs/decisions.md:4763 | — |
| 36 | "The three checks test *necessary* conditions on a conscious realizer" | 190 | ACCURATE | a theory-level claim about consciousness, untested, distinct from the falsified capability necessity (C/docs/cru226-juelich-substance.md:288) | — |
| 37 | Check 3 fails for self-modelling indifferent to detuning of the generative regime | 194 | ACCURATE | targets free modelling, not criticality, as C/docs/decisions.md:4763–4764 requires | — |
| 38 | "some corroborated post hoc" | 196 | **UNDERSTATED** | C/docs/results/cru40-b1-R1-S0pre2-gridworld-fitted-arms.md:5, 9 | see Q38 |
| 39 | Removing the projection abolishes the transfer capability | 196 | ACCURATE | C/docs/results/p1-causal-transfer.md:39–46 | — |
| 40 | Planner "scales with depth where reactive policies fail at a fixed sample budget" | 196 | **OVERSTATED** | as row 10 | see Q40 |
| 41 | Forecast: "a closure-bearing self-circuit should be the most stable and last-collapsing part"; untested | 196 | **OUTDATED — framing** (the status "untested at scale" holds) | A/docs/research/fmt-crucible-misread-rca.md:36; C/docs/decisions.md:4836–4838, 2375–2378 | see Q41 |
| 42 | "The latter is the decisive test, and it is open" | 196 | ACCURATE | as row 23 | — |
| 43 | A fixed-point predictive-processing account makes neither forecast | 196 | ACCURATE | C/docs/results/fmt-evidence-ledger.md:177 (crucible's working copy of the theory claim) | — |
| 44 | "specified down to a buildable minimal open-ended spiking substrate" | 200 | **OUTDATED** | as row 2 | see Q44 |
| 45 | "the checks themselves, and the decisive scaled test, have not yet been run" | 200 | ACCURATE | crucible's self-model-property tests are not these checks: CRU-206 NO MODEL on the write-back path (C/docs/decisions.md:5108–5115); CRU-227 P1 NOT TESTABLE, four criteria never ran (C/docs/results/cru227-p1-2026-10-28.md:19–20, 80–81) | — |

### Quotes and fixes for the non-ACCURATE rows

**Q2 — row 2, l.150 (OUTDATED, conflicts with a crucible decision).**
Manuscript: "The smallest system that instantiates the detector's target is a single recurrent spiking pool whose dynamics have
open-ended computational capability at the level that carries the self-model, functionally differentiated into an explicit world-model
that predicts the next external input and an explicit self-model whose "world" is the system's own state, with the closure loop running
from the second into the update of the first."
Sources:
- A/docs/aiw91-minimal-critical-substrate.md:52, 57, 60, the origin of this sentence: "A single recurrent spiking pool at criticality,
  functionally partitioned into: … **EWM:** a readout+recurrent module that must *predict the next external input* … **ESM:** a module
  whose "world" is **the system's own state**".
- The same file, l.1: "⛔ **SUPERSEDED — DO NOT BUILD FROM THIS FILE (aIware S362, 2026-10-27).** Its "Minimal architecture sketch"
  makes the explicit models (EWM, ESM) **modules of a network**. That is a level error FMT rules out".
- C/docs/decisions.md:81–83: "The explicit models (EWM, ESM) are emergent spiking ACTIVITY … **Never a region, population, slice or
  module.** 3. Substrate: spiking, close to biology — refractory period ON, non-zero resting firing rate."
- C/docs/decisions.md:84–85: "Topology: I/O through a few ganglia-like spiking networks → ONE thalamus-like restriction → a cortex-like
  compute surface with differentiated (Brodmann-like) areas; the body model takes **a good fraction of the total cortical area**".
- MG verbatim, A/docs/sources/mg-2026-10-27-fmt-substrate-spec.md:5: "Explicit models ARE NOT REGIONS IN A NETWORK … it is very far from
  what FMT asks for."

"Functionally differentiated" softens "partitioned". The sentence is still the superseded sketch, with no implicit models in it, and
"smallest" claims a minimality that MG's spec contradicts.
Fix: "A system that instantiates the detector's target is a spiking substrate close to biology (refractory period, non-zero resting
rate) whose connectome and weights carry the implicit models and in whose activity an explicit world-model and an explicit self-model
emerge as robust patterns, not as regions or modules, with the closure loop running from the self-model's activity into the update of
the world-model's."
The "Concretely:" sentence then needs the matching edit ("a cortex-like sheet of leaky-integrate-and-fire cells, reached through
ganglion-like networks and one thalamus-like relay"). Q-open 1 covers the scope of this change.

**Q3 — row 3, l.150 (OVERSTATED).**
Manuscript: "a single experimental knob — whether that self-basin enters the world-model's own update or is merely read out — makes
closure measurable (check 2)."
Sources:
- C/docs/results/cru58-closure-off-is-two-closed-systems.md:4, 10: "`closure_enabled=False` is not an ablation: it makes TWO closed
  systems" and "**ON = one closed system. OFF = two closed systems, uncoupled.** Not closure vs no-closure."
- C/docs/results/cru40-b1-R1-readout-a.md:16–17: "the closure-ON and closure-OFF arms cannot be placed at a matched operating point".
- C/docs/decisions.md:2377–2378: "A matched-operating-point closure-only perturbation does not exist here (two instruments agree)."

Crucible ran this exact knob, a self block that still reads the rest while its write-back is zeroed, and found both problems.
Fix: "…makes closure manipulable (check 2), although on a recurrent substrate the cut leaves smaller closed systems standing rather than
removing closure (Gruber, 2026b, §5.1)."

**Q10 — row 10, l.152 (OVERSTATED).**
Manuscript: "…scores 0.00–0.33 at the same sample budget; nothing shows the reactive policies could not reach the behaviour with more
samples."
Sources, all C/docs/results/cru40-b1-R1-S0pre2-gridworld-fitted-arms.md:
- l.78: "| R5′ | R5 + one-step **ARRIVAL-cell** patroller dodge | **0.45** |".
- l.75–76: the 4×-label and 4×-corpus refits both score "**0.00**".
- l.91–92: "The pre-committed **RT-6** line stands verbatim: a higher-capacity distiller (e.g. a small CNN over the map) would likely
  close HR".

The pinned range is right, but the strongest adversarial variant reached 0.45. More samples did not help. The record's own caveat is
capacity, and it expects a larger reactive learner to close the gap.
Fix: "…scores 0.00–0.33 (0.45 for the strongest adversarial variant) at the capacity tested; the gap is capacity-relative, and a
higher-capacity reactive learner would likely close it."

**Q16 + Q17 — rows 16–17, l.154 (OVERSTATED; UNDERSTATED).**
Manuscript: "That null is under re-analysis after a simulator-artefact audit; the framework predicts a null here, since the reservoir had
no distinct self- and world-models for a loop to close between."
Sources:
- C/docs/results/artifact-audit-2026-10-07.md:21: "**CRU-36** substrate closure null (I_obs 0.5·vth + re-entry 3.0 …) — null, could move
  either way."
- The same file, l.68: "CRU-36 not re-run."
- C/backlog.md:95: CRU-205, the floor re-check vehicle, is "**PARKED — MG 2026-10-07 ~13:05 "Park it"**", and its re-check list does not
  name CRU-36.
- C/docs/cru226-juelich-substance.md:302: "AT RISK: the §6 re-entry null (CRU-36)".
- No CRU-36 run, repro or data has appeared since 2026-10-07 (git log and `docs/results/data` checked).
- The omitted reason, comp:224: "the substrate was not memory-limited for this task ($H_{\mathrm{native}}$ ≈ 100 ≫ τ = 15), so the
  passive reservoir could already solve it cheaply".

The memory-horizon reason does not depend on how the self-model is realized, so it survives the 2026-10-27 activity-not-regions reading
untouched.
Fix: "A later simulator-artefact audit marked that null as possibly affected, and it has not been re-run; the framework predicts a null
here, since the reservoir carried no self-model and the task lay well inside its passive memory horizon."

**Q18 — row 18, l.156 (OVERSTATED).**
Manuscript: "A *closure ablation* — running the same system with the self-model's contribution to its own update switched on versus
off, at matched recurrence and capacity — isolates check 2: only in the closed version should removing the self-model's contribution
degrade the world-model."
Sources:
- C/docs/results/fmt-evidence-ledger.md:165: the stationary-closure theorem "proves the decisive loop-cut **cannot** be a binary
  oracle-level test on any *deterministic, episode-stationary* task".
- The manuscript's own l.158 says the same.
- C/docs/results/cru40-b1-R1-readout-a.md:16–17, as in Q3.

As written, the ablation predicts capability loss on an unspecified workload, which l.158 rules out. It is consistent only as the
fixed-capacity excess-loss reading on the open-ended workload (l.160).
Fix: "…switched on versus off, at matched recurrence and capacity and on check 2's open-ended workload — isolates check 2: only in the
closed version should removing the self-model's contribution raise the world-model's loss."

**Q19 — row 19, l.156 (OVERSTATED).**
Manuscript: "(in the rate reservoirs tested so far, in the driven-stable, ordered regime; Gruber, 2026b)". The parenthesis locates
"where the substrate keeps its open-ended capability".
Sources:
- C/docs/decisions.md:4666–4667: the CRU-204 rate leg is "a static map applied k times".
- l.4669–4670: "Leg A's scoping result (shallow chains do not need the edge, as §3.7 predicts) is recorded, not banked as evidence either
  way."
- l.4725–4726: "close the rate mirror as uninformative".
- comp:234: "Whether operating at the edge pays remains untested, for want of a task deep enough to exercise the explicit-modelling
  mechanism."
- C/docs/results/cru203-edgepeak-replication-2026-10-01.md:330: the peak is "co-located with the lag-6 memory peak".

What was measured is where shallow, memory-bound tasks peak. No open-ended capability was measured in any rate reservoir. This
disagrees with S363 recheck N4, which let l.156 keep the short form. Line 64 (outside this scope) has the same issue in its
"capability optimum" wording.
Fix: "(in the rate reservoirs tested so far, performance on the shallow memory-bound tasks used peaked in the driven-stable, ordered
regime; Gruber, 2026b, §4.4)".

**Q32 — row 32, l.174 (OUTDATED framing; the attribution is correct).**
Manuscript: "On the companion's model connectome, a returning path through the self region is what recurrence already gives (Gruber,
2026b, §5.1; a graph result)."
Sources:
- comp:181 ("The realized 440-neuron connectome is a single strongly connected component", with cuts "leaving CE+EWM+ISM and ESM") and
  comp:236 ("it is what recurrence already gives you").
- C/docs/decisions.md:88–89: "`ClosureBrain` (CE/EWM/ISM/ESM as region-slices) is NOT an FMT architecture. Results that rank or ablate
  the named regions are not FMT evidence (may remain valid as dynamics engineering)."
- A/docs/research/fmt-crucible-misread-rca.md:59: "The companion paper describes crucible's regions without objecting (… "the self
  region", added in S316…)".

The graph fact survives as dynamics engineering, but "the self region" is the label the ruling withdraws.
Fix: "On the companion's model connectome, which forms a single strongly connected component, every part already lies on a returning
path (Gruber, 2026b, §5.1; a graph result)."

**Q38 — row 38, l.196 (UNDERSTATED).**
Manuscript: "The architecture also makes predictions, some corroborated post hoc and some untested."
Sources:
- C/docs/results/cru40-b1-R1-S0pre2-gridworld-fitted-arms.md:5: "fitted arms run **blind** after the freeze".
- The same file, l.9: "**GO** — all six gates green".

The planner passed a pre-registered gate battery, so "post hoc" fits only the transfer result. That one passed after a rebuild that
followed a null (C/docs/results/p1-causal-transfer.md:59).
Fix: "The architecture also makes predictions, some corroborated in toy systems and some untested."

**Q40 — row 40, l.196 (OVERSTATED).**
Manuscript: "A self-model-gated planner scales with depth where reactive policies fail at a fixed sample budget."
Source: as Q10, the gap is capacity-relative.
Fix: "A self-model-gated planner scales with depth where reactive policies of the capacity tested fail."

**Q41 — row 41, l.196 (OUTDATED framing).**
Manuscript: "that a closure-bearing self-circuit should be the most stable and last-collapsing part of the system under graded
suppression of the substrate".
Sources:
- A/docs/research/fmt-crucible-misread-rca.md:36: "MG's 2026-07-12 discriminator ("the self-model = the most stable, longest-living …")
  is in substance about robust sustained activity. It was turned into a ranking of the regions."
- C/docs/decisions.md:4836–4838: "its Readout A came out VOID (apparatus) and S7 NEGATIVE in July".

"Untested" remains right for a scaled system. The only attempt was toy-scale, region-labelled and void.
Fix: "that the self-model's robust activity pattern should be the most stable and last-collapsing part of the system under graded
suppression of the substrate".

**Q44 — row 44, l.200 (OUTDATED).**
Manuscript: "The procedure is specified down to a buildable minimal open-ended spiking substrate".
Source: as Q2.
Fix: "The procedure is specified down to a buildable, biologically close spiking substrate". This depends on Q2 being adopted.

### CRU-231 and "the decisive test is open"

Three tmux jobs are running: `cru231-frozen`, `cru231-learn`, and `cru231-learn-slowinh` (homeostasis 10× slower). Their logs are
`/tmp/cru231-*.log` and their data `C/docs/results/data/cru231/learning-*-s0.json`. All three run the v2 foraging creature (C/backlog.md:90)
for 20 simulated minutes. They log food eaten, pain, hunger, cortex rate and the decode of shoulder angle from S1 and parietal cortex. The
raw rows so far are unchecked: learn S1 0.087 → 0.444 over minutes 1–2, frozen 0.542 → 0.519, slowinh minute 1 0.33. The jobs ask whether
learning keeps body content. No arm cuts closure, and nothing is matched on function. They do not bear on the claim. Crucible's own
must-not-claim list says the scaled matched-function test is "undesigned" (C/docs/cru226-juelich-substance.md:306).

### Where secondary summaries disagree with crucible's record (newest measured result followed)

- **Companion §6.** comp:222 calls CRU-36 "a clean null". The audit lists it AT RISK and not re-run (artifact-audit:21, 68). The companion
  is stale.
- **Companion §4.5, outside this scope.** comp:145 reads A#6 as closure maintenance. The Fable red-team adopted "slow-reservoir memory,
  not evidence for closure" (artifact-audit:88–91; cru226-juelich-substance:303).
- **Companion §5.** It rests on the region-labelled ClosureBrain ("self region", "CE+EWM+ISM and ESM"), which decisions.md:88–89
  withdraws as FMT evidence.
- **Companion §4.3 Methods.** comp:133 says "Training is 5 × 40 episodes". The source says "training 5 episodes × 40 steps"
  (p1-causal-transfer:7).
- **S363 recheck N4.** It let l.156 keep the short form. The CRU-204 entries (decisions.md:4664–4670, 4725) and comp:234 do not support
  locating open-ended capability (Q19).
- **S362 recheck F2.** It offered "under re-analysis" as the keep-option (aiw130-recheck-s362.md:43), although its own source said "not
  re-run" (l.38–40). That is the wording now in the draft (Q16).
- **Crucible's evidence ledger.** Row A#2's heading "Criticality does real work — it COMPUTES" (fmt-evidence-ledger:23) predates CRU-203,
  and its "Honest scope" loop-cut sentence (l.158–159) predates the same file's l.165 update. The manuscript follows the newer record in
  both places.

## Already fixed since the S363 recheck

All ten S363 findings and the §3d item are fixed in the current text.
- **N1:** figures are cited in order (l.52, 58, 72).
- **N2a:** the quote locators are restored (l.46–50).
- **N2b:** the "(Gruber, 2026b, §6)" pin is in and the "framework predicts a null here" wording is used (l.154).
- **N3:** "that a rate-matched surrogate does not reproduce" is in (l.82).
- **N4:** l.64 is fixed. l.156 kept the short form, which Q19 now flags.
- **N5:** "plausibly as common … would discriminate little" (l.174).
- **N6:** the excess-L_W falsifier is appended (l.194).
- **N7:** "usual signature … not the requirement itself (Gruber, 2026a, §3.7)", with the aphorism cut (l.186).
- **N8:** "a structure-extraction method of the kind they name" (l.170).
- **N9:** "The architecture also makes predictions" (l.196).
- **N10:** "obtained without varying the substrate's regime" (l.154).
- **§3d:** the Figure 3 alt text now reads "Verdict on the tested conditions + explicit confidence" (l.302). The SVG itself was not
  re-checked.
- **l.124 clunk:** fixed.
- **S362 items in this range:** F1 and F4 are fixed, and F3 is resolved by the "plausibly" wording. F2 was applied as the "under
  re-analysis" keep-option, which this check finds overstated (Q16).

## Open questions for the author

1. **How far should §6(a) move to MG's 2026-10-27 spec (Q2/Q44)?** The minimal fix above swaps the region reading for activity-emergent
   models and adds refractoriness and a resting rate. A fuller rewrite would also describe the ganglia → one thalamus → cortex-sheet
   topology, with the body representation taking a good fraction of the sheet. Separately, "homeostatic plus spike-timing-dependent
   plasticity" now has a record against it. An inhibitory homeostat about 1,000× faster than biology erased the input-driven modes within
   a minute (C/docs/results/cru227-p1-2026-10-28.md:29–33, 64). MG ruled for balanced, reward-gated plasticity
   (C/docs/decisions.md:37–48).
2. **Does the 2026-10-27 "not FMT evidence" ruling reach the transfer result?** The FmtAgent's ESM is a module object. Track A's four
   model objects are listed under the region reading (A/docs/research/fmt-crucible-misread-rca.md:21), and the ablation replaces a built
   binding with a no-op. Perception supplies the mechanism label, and `mechanism_aversion` binds to it (p1-causal-transfer:62–66).
   Crucible's must-not-claim list says "Self/world differentiation is hardcoded (construction, not emergence)" (cru226:291). MG has not
   ruled on gridworld agents specifically. Should l.152 and l.196 say the dissociation is between agents built with and without a
   self/other module?
3. **Should l.162 note the later ties?** Since 2026-10-01, crucible's closed-against-open comparisons have tied: route A closed ≈
   capacity-matched open (cru226:289; route-a-s2-centre1:255–258; route-b-s0:206–208). The deep-task chain advantage was erased by the
   membrane-floor re-check (artifact-audit:11, 40). These fit "an advantage only inside a cost window", and the FlowBody runs are not
   quotable anyway (cru226:280–281). Is "toy systems … differ in capability as the theory expects" still the selection you want, or
   should it say "in the four toy systems reported"?
4. **Rewrite or delete the CRU-36 sentence (Q16)?** S362 F2's first option was deletion, and the interaction point stands without the
   sentence.
5. **Should the "corroborating" role of a near-unity m at l.164 say outright that it is descriptive and never part of a pass?** MG's
   rulings 2026-10-02/03 (decisions.md:4761, 4775) require that.

No commits were made.
