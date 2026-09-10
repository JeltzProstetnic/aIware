# Bottleneck-arm over-claim audit (crucible 2026-08-14 finding) — aIware prose

**Audited 2026-08-24 by a Fable subagent.** Finding audited against: every banked loop arm ran as the
materialised dense product `A @ Vt` (billed 125,888 connections, actually 323,424,256, off 2,569×);
the span rule's STORAGE claim is untouched; every DYNAMICAL or METABOLIC statement about a
"bottleneck arm" describes a dense matrix. Plus: closure itself costs ×1.03 rest / ×1.01 load (the
8.72× was the wiring); the energy negative is withdrawn and the spandrel-on-energy-grounds claim may
not be drafted in either direction.

Ground truth cross-checked read-only in crucible: `~/crucible/docs/results/cru108-closure-vs-wiring.md`
(§2–§3), `~/crucible/docs/results/cru108-instantiated-bottleneck.md` (:39–45),
`~/crucible/docs/decisions.md` (2026-08-14 afternoon entry, "Consequence for every banked loop
result. They were all run on the materialised product."), and
`~/crucible/docs/results/fmt-evidence-ledger.md` (row 8 = A#8 = CRU-74 tier B; rows A#7/A#9).

---

## ANSWERS TO THE TWO GOVERNING QUESTIONS

### (a) Does the published master (v15) contain a DYNAMICAL or METABOLIC bottleneck-arm claim?

**YES — exactly one, DYNAMICAL, and it is in both the .md and the published .tex.** The Seventh
banked result of §8.9 (ledger A#8, CRU-74 tier B, a spiking experiment) is described as
*"a spiking architecture whose bottleneck writes to a subsystem and never reads it"* — a dynamical
result attributed to a narrow-waist architecture whose dynamics were never run. See D-1 below.
There is **no METABOLIC bottleneck-arm claim** in v15: no energy, run-cost, or spiking-cost figure is
anywhere attributed to a bottleneck arm (the only "energy" token in the Seventh is the control
statement "per-unit injected energy fixed", which is a statement about injected drive, not about the
arm's cost profile).

The S306 repairs (commit `3ec61acb`, AIW-216 order-of-magnitude wording + AIW-217 scope clause)
**did not touch this class** — they repaired the Eighth result's paragraph only. So the
materialised-dense re-description is a **third §8.9 repair candidate** for the open erratum-on-v15
vs wait-for-v16 decision. It is the smallest of the three in surface area: one architecture clause,
one rival-readout name, and (optionally) the ordinal's headline wording — which is MG's banked
verbatim formulation (ledger row 8), so the wording change **needs MG's ruling, not a silent swap**.
The measured content of the Seventh (the R² contrast) survives; this is an erratum-level descriptor
fix, not a retraction.

### (b) Does any aIware text state or imply the withdrawn energy negative, in either direction?

**NO.** "Spandrel"/energy-negative language occurs only inside the two warning documents themselves
(`docs/crucible-status-2026-08-23.md` §1(c) and `docs/pending-s306-detector-and-submission.md:150–155`),
both quoting the withdrawal *as a prohibition* — correct usage. The master's "metabolically
expensive" (line 983), didactic patterns #6/#11, and SMoC M2's "energy" cell are biological-lane
theory claims that predate and never cite the crucible energy runs; they neither assert nor deny the
spandrel question about the model system. One **watch item**: backlog `AIW-201` ("structurally
present, metabolically paid for, and capability-idle") would cross the line if drafted as written —
see W-2.

---

## DEFECTS

### D-1 — Master §8.9, Seventh result: dynamical result attributed to a bottleneck architecture
- **File:line:** `/home/jeltz/aIware/paper/full/four-model-theory-full.md:981` (same text in
  `/home/jeltz/aIware/paper/full/latex/paper.tex:1232` — the published build source; verified
  `grep -c "whose bottleneck writes"` = 1 in the .tex).
- **Quoted:** *"**Seventh, closure earns its keep exactly to the extent that the driven subsystem
  carries change the bottleneck cannot work out from what it already reads:** in a spiking
  architecture whose bottleneck writes to a subsystem and never reads it — no return path at any
  point — holding connectome, carriers, and per-unit injected energy fixed, and flipping only
  whether the carrier waveform carries information about the disturbance driving that subsystem,
  moves downstream R² from −0.001 to 0.640 …"* — plus, later in the same result, the rival readout
  named *"bottleneck-only"*.
- **CLASSIFICATION: DYNAMICAL.**
- **Why wrong as written:** this is CRU-74 tier B (ledger A#8), a spiking experiment. Per crucible's
  2026-08-14 ruling, every banked loop arm — including this one — was simulated as the materialised
  dense product of its rank-k factors; *"this substrate has never simulated a bottleneck. It
  simulates the materialised product of one, which is the opposite of a bottleneck in the currency
  energy is charged in — dense where the architecture claims to be sparse"* (cru108-closure-vs-wiring
  §3). The sentence attributes a spiking dynamical result to a narrow-waist architecture; the object
  that ran has ~2,569× more connections than the factored bill implies. **What survives:** the R²
  contrast itself is within-arm with the (dense) realization held fixed on both sides, so
  −0.001→0.640, the four-readout tie, and the matched-condition advantages (0.398/0.209/0.089) stand
  as facts about the arm that ran; the write operator's rank is genuinely ≤ k as a linear map. What
  does not survive is the implication that a wired narrow waist produced them — a wired bottleneck
  applies the operator in two timesteps through a spiking nonlinearity, and cru108-instantiated
  measured that this costs ~4 points of ceiling, i.e. the dynamics are *not* a free
  reparameterisation.
- **Minimal correct restatement:** *"…in a spiking architecture whose rank-k write operator —
  realized in simulation as the materialised dense product of its factors — writes to a subsystem
  and never reads it…"*, and rename or footnote the *"bottleneck-only"* readout (e.g.
  "write-operator-only"). The ordinal's headline clause ("…the bottleneck cannot work out from what
  it already reads") is MG's banked verbatim formulation — flag to MG rather than editing.
- **Confidence: HIGH.** Checked: ledger row 8 attributes the result to CRU-74 tier B spiking;
  crucible decisions.md 2026-08-14 states the consequence applies to *every* banked loop result;
  cru108-instantiated:39 states "Every banked loop arm is billed 2·|span|·k … and simulated as the
  materialised product"; the .tex carries the identical sentence.

### D-2 — Master §8.9, paragraph opener: "a currency" joint framing
- **File:line:** `/home/jeltz/aIware/paper/full/four-model-theory-full.md:981` (first sentence).
- **Quoted:** *"Three further banked results concern what the architecture costs rather than what it
  does; they share a substrate, a currency, and a form of argument…"*
- **CLASSIFICATION: AMBIGUOUS (low severity).**
- **Why flagged:** the Sixth's percentages (14.0%/74.0% etc.) are *measured nonzero counts* of the
  connectome; the Eighth's synapse advantages (241→6288 etc.) are *factored storage bills*.
  Presenting them as one "currency" is exactly the accounting-bill-against-a-measurement conflation
  cru108 diagnosed as the root of the 2,569× error. Nothing asserted of either result individually
  is false; the joint framing invites the wrong equation.
- **Minimal fix:** drop "a currency", or qualify: "a cost currency — measured connection counts in
  the sixth, stored-parameter bills in the eighth."
- **Confidence: MEDIUM-HIGH** (the defect is a framing risk, not a false statement; the conflation
  mechanism is documented verbatim in cru108-closure-vs-wiring §2).

### D-3 — Master §8.9, closing paragraph: "metabolically expensive" inside the results-reading frame
- **File:line:** `/home/jeltz/aIware/paper/full/four-model-theory-full.md:983`.
- **Quoted:** *"…which is why non-conscious animals compete successfully against conscious ones
  across most of the biosphere, and why the capacity is rare and metabolically expensive rather than
  universal."*
- **CLASSIFICATION: AMBIGUOUS (adjacency, no text change strictly required).**
- **Why flagged:** this is a biological-lane theory claim, unsourced to the program, and it predates
  crucible's energy runs — so it does not state the withdrawn negative. But it sits inside the
  paragraph that governs *"how these results should be read"*, and post-08-14 there is no program
  energy result that could support it (closure itself measured ×1.03/×1.01 — nearly free; the
  metabolic question about bottleneck architecture is open). It must never acquire a crucible
  citation, and a v16 pass could add a lane marker ("a claim about biological self-modelling, not
  measured in the model systems above").
- **Confidence: HIGH** that it is currently unsourced and biological-lane; MEDIUM that a reader
  would misattribute it.

### D-4 — aiw133 cosmology analysis: relay neurons that never ran
- **File:line:** `/home/jeltz/aIware/docs/aiw133-schoff-cru-cosmology-analysis.md:362–366` (§B.3).
- **Quoted:** *"Content partitioned across CE | EWM | ISM; a loop closes over a span;
  **cost = 2·|span|·k synapses + k relay neurons**; DV = pattern completion on the half never cued."*
- **CLASSIFICATION: DYNAMICAL-mislabel in a cost description (moderate, doc-level).**
- **Why wrong as written:** describes the simulated arm as containing k relay neurons. Per cru108:
  *"There are no relay cells."* The `2·|span|·k` bill is the right storage quantity; the "+ k relay
  neurons" term describes an idealised wired realization that was never simulated — the arm ran as
  the materialised dense product. The three numbered claims that follow (span ceiling, super-span
  waste, subsystem-coupling condition) are function-and-bill claims and stand (function was computed
  with the exact operator; bills are bills).
- **Minimal restatement:** *"billed cost = 2·|span|·k stored entries (the idealised wired form would
  add k relay units; the simulated arms materialised the product — no relay cells ran)."*
- **Confidence: HIGH.** This file is `Action: reference` companion-analysis material for the
  cosmology lane (A5/Bekenstein argument) and would propagate the wired-realization fiction into a
  second paper if inherited verbatim.

---

## WATCH ITEMS (not defects in current prose; will become defects if drafted)

- **W-1 — Companion paper (AIW-124/AIW-218) methods:** per crucible CRU-94 routing, the
  `[[CRUCIBLE:]]` method sections *must* describe the banked loop arms as materialised dense
  products and import the cru69 §11.6 scope sentence verbatim. No companion methods prose exists in
  aIware yet (checked `drafts/` and `docs/aiw92-drafts/` — nothing drafted), so the exposure is
  currently zero, but every future draft inherits D-1's fix.
- **W-2 — backlog.md `AIW-201`:** the matched-recurrence argument describes its predicted null as
  proof the self-relational property is *"structurally present, metabolically paid for, and
  capability-idle."* "Metabolically paid for" presumes closure is metabolically costly; the only
  clean number says closure itself is nearly free (×1.03 rest, ×1.01 load) and the bottleneck-
  architecture energy question is open/withdrawn. If drafted as-is this states an energy premise in
  the withdrawn zone. Planning prose, not paper text — but the eventual draft must move the cost to
  the redeployment axis or drop the metabolic clause.
- **W-3 — "waist buys efficiency" occurrences** (`drafts/aiw-operationalization-review.md:55`,
  `docs/decisions.md:836`, `docs/smoc-middle-layer-draft.md:195,210–211`,
  `docs/aiw133-…-analysis.md:394–398`): the decomposition *"the waist buys efficiency (rank ≤ k,
  wiring 2·k·N instead of N²), the return buys self-consistency"* is safe **as long as "efficiency"
  stays a wiring/storage count** — that reading is now independently validated on the wired
  follow-up (575,488 vs 22,744,284 connections, 39.5× fewer at matched performance). It must never
  be glossed metabolically: at rest the wired bottleneck's energy is a wash (×0.930, 2 of 8
  individuals above 1.0), and the load-regime ×0.532 supports no spandrel claim in either direction.
- **W-4 — SMoC M2 row** (`docs/smoc-middle-layer-draft.md:223`): closure's "why it costs" cell reads
  "energy, and a narrow fit window" (pattern #11). Biological-lane; must not be footnoted to
  crucible energy numbers for the same reason as D-3.

---

## CLEAN LIST — checked and genuinely safe (bounds the repair)

1. **Master Sixth result** (`four-model-theory-full.md:981`): 14.0%/12.0% closure-opening cost,
   74.0%/71.5% return-freedom, 5.3×/6.0× — self-declares *"a claim about graph structure and not
   about dynamics"*; matches crucible's safe list verbatim. STORAGE/structural. Checked against
   crucible-status §4.
2. **Master Eighth result** (`:981`, span rule / A#9): all synapse figures (241→6288,
   −2428…−7324, 195/2159/6048, 48/48 unbounded at 126 units, exchange rates ~1732/210),
   span=support in 8/8 seeds × four content conditions, the four selection conditions, and the
   self-description *"a wiring-cost result on a numpy substrate."* Every cost figure is the factored
   bill, which crucible rules is *"the right quantity"* for the storage claim (*"To the span rule:
   no impact"*); performance figures were computed with the exact operator (numpy — the dense
   product implements the identical linear map, so function claims are realization-independent
   there). The post-S306 wording ("an elevenfold step and then a further factor of under three")
   matches the AIW-216 repair and avoids the banned "order of magnitude per subsystem". STORAGE —
   CLEAN.
3. **Master Fifth result** (`:979`): "a re-entrant loop holds decodable content… 0.63–0.77" — makes
   no bottleneck/waist/rank claim; the return genuinely existed whatever the arm's realization, and
   decodability was measured on what ran. CLEAN.
4. **Master channel prose** (`:378, :380, :429, :431, :737, :835` — §3.4.2, §3.6.x, §6.2, §7.2):
   "low-rank read/write path", "narrow path", "rank sets how much the simulation holds", the
   thalamocortical-realizer candidacy, the anesthesia signature. Theory-lane claims about brains and
   architecture; none attributes dynamical or metabolic evidence to the program's bottleneck arms.
   CLEAN.
5. **Master `:484`** (third dial): "in an artificial substrate rank and closure are both settable" —
   true at operator level (rank of A@Vt is k). CLEAN.
6. **NoC trimmed paper, fmt_formal, rim_formal** — zero occurrences of
   bottleneck/waist/loop-arm/span-rule/rank-k content (verified with narrow and broad greps,
   including channel/energy/spiking/wiring sweeps; all fmt_formal matches are the unrelated
   permeability-channel formalism). **The exposure does not extend to any of these surfaces.**
7. **`docs/aiw219-span-rule-novelty-check.md`** (S306, post-correction): storage-framed throughout
   ("self-inclusion from connection-count minimization"); the proposed claim sentence is cost/span
   only. CLEAN — but the standalone paper's methods must carry the materialised-dense disclosure
   when drafted (W-1 applies).
8. **`drafts/return-vs-closure-vocabulary-ruling.md`** — naming ruling only ("`bottleneck` stays");
   no dynamical claim. CLEAN.
9. **`drafts/aiw186-vacuity-regime.md:47`** — correctly characterizes CRU-58 as "a wiring diagram
   whose edges were physically cut" (structural). CLEAN.
10. **`docs/decisions.md:627–628`** (channel-not-bottleneck naming rationale) and `:836`
    (decomposition record) — conceptual; CLEAN (subject to W-3's efficiency-reading note).
11. **`docs/patent/*`** — the folded/open-arm exposure is already self-flagged and mitigated:
    `05-red-team.md:34` marks the span/bottleneck/short-return dependents **WOUNDED** as "supported
    exclusively by measurements taken on folded (open-network) arms"; `06-claim-architecture-v2.md`
    marks the 7.9× synapse-economy figure **FOLDED** with remediation experiments (E1–E4: wire a
    real relay return, re-run the argmin, re-measure economy at matched performance). No unflagged
    over-claim found. CLEAN (already-aware).
12. **`paper/intelligence/paper.md` ("Performance Is Not the Bottleneck"),
    `paper/seth-commentary/seth-commentary.md` ("specification problem is the bottleneck"),
    `paper/cosmology/sb-hc4a.md`** — "bottleneck" only in unrelated metaphorical senses. CLEAN.
13. **`.claude/knowledge/didactic-patterns.md`** — no span-rule dynamical claims; #6/#11 energy
    items are biological-lane and pre-crucible (W-4 note applies). Pattern #24 (same-N matched pair)
    is a motivation claim, untouched. CLEAN.
14. **Session/conversation logs** — no bottleneck+energy/metabolic claim statements found
    (proximity grep over both logs). CLEAN.
15. **`docs/aiw91-minimal-critical-substrate.md:232`** — "not the bottleneck" = VRAM sense. CLEAN.
16. **Engineering designs (`docs/engineering/designs/*`)** — "bottleneck" in the
    VAE/autoencoder/pipeline senses, pre-dating and independent of the span-rule program. CLEAN.

---

## VERDICT (one sentence)

The published v15 master carries exactly one defect in the audited class — the Seventh result's
"spiking architecture whose bottleneck writes…" descriptor (dynamical, dense-arm, erratum-sized) —
plus two low-severity framing ambiguities in the same section; the Sixth and Eighth results, the
whole channel construct, the NoC paper, both formalization roadmaps, and the withdrawn energy
negative are all clean, and the companion paper's exposure is entirely prospective.
