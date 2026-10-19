<!-- Action: reference -->
<!-- Tracked-by: AIW-193, AIW-194, AIW-197, AIW-198, AIW-199, AIW-200 -->
<!-- S299 2026-08-10: all eight decisions in the former §1 were ANSWERED by MG and recorded in backlog.md + docs/decisions.md. Section removed per the no-duplicate-status-tracking rule. This file is now REFERENCE ONLY — its value is §0 (the siibra feasibility result, never re-run it), §0b (MG on why a human-like connectome is wanted) and §3 (do-not-redo). -->
# S298 handover — the siibra check LANDED (do not re-run), and eleven decisions waiting on MG

## 0. ✅ RESOLVED — the feasibility check completed just after shutdown. **DO NOT RE-RUN IT.**

**Verdict: siibra is a green light onto a road that does not go where we wanted.** Three findings, all
obtained by measurement rather than argument, and two of them are about **crucible's own code**. Working
artefacts (venv, downloaded matrices, analysis scripts) in `tmp/siibra/`.

**(1) Directedness — I was wrong, and in our favour.** siibra *does* expose a genuinely directed human
connectome: **`AnatomoFunctionalConnectivity` = F-TRACT**, cortico-cortical evoked potentials from **613
epilepsy patients**, 314×314 on Julich-Brain 3.0, retrieved and verified working with no credentials. Its own
header states *"a[i][j] means stimulation from i to j"* — direction is experimental design, not statistical
inference. Measured: `max|A − Aᵀ| = 0.929`, **77% of reciprocal pairs differ**. Everything else siibra ships
is **bit-exactly symmetric** (checked all 7 HCP matrix kinds × 200 subjects: `max|A − Aᵀ| = 0`).

**(2) ⚠ THE CRUCIBLE INSTRUMENT CANNOT RUN ON IT — by ~2,800 orders of magnitude.**
`min_prevention_set` in `packages/crucible/src/crucible/metrics/closure_prevention.py` enumerates **every
subset of the block set** (`for size in range(0, len(pool)+1): for subset in combinations(pool, size)`),
with an explicit comment refusing early termination. Θ(2^E) in blocks, no timeout, no cap, no approximation
fallback. Measured: 16 blocks = 0.37 s, 20 blocks = 7.4 s, **25 blocks did not finish in 200 s**. A
314-region connectome at threshold >0.1 has **9,378 blocks → 2^9378 subsets**. Its own justification comment
says the quiet part: *"The region graph has a handful of blocks, so the exact optimum is affordable."*
**The tractability rests on the connectome having four regions.** ⚠ Also flagged: **no code anywhere in
crucible constructs a condensation DAG** — that language exists only in prose.

**(3) ⚠ THE STRUCTURE WE WANTED TO ANALYSE IS NOT THERE IN REAL CORTEX.** SCC decomposition on F-TRACT at
every sensible threshold gives **one giant SCC of 272–284 nodes plus ~30 fully isolated singletons**; the
condensation DAG has **4–11 edges**. There is no rich return structure to search. **This mirrors crucible's
own synthetic result** (1 SCC over 22,000 neurons) — so a real connectome would **not** discharge the
scope caveat by showing something structurally different. It shows the same degeneracy.

**(4) ⚠⚠ THE SENSITIVITY ANALYSIS DESIGNED THIS SESSION PASSES VACUOUSLY — tested on the real connectome.**
Edge-count-preserving random re-orientation: at **50% flips (= full randomisation)** the FAS moves **+6.2%**
and the giant SCC does not move at all. **A test that passes when the orientation data is replaced by coin
flips proves nothing about the orientation.** Three structural reasons, not artefacts: SCC is near-invariant
under reorientation (no edges removed, only in/out degree re-partitioned, and the reciprocal subgraph is
massively supercritical); **FAS is provably 1-Lipschitz under arc reversal**, so "FAS moved less than the
number of flipped edges" restates a theorem; and **84–95% of the FAS is a mandatory digon floor** —
reciprocal pairs are ~35% of edges, so only **~5–7% of edges carry any orientation-derived loop content**.
⇒ **MG's informed-random ensemble would pass vacuously for the same reason.** If a sensitivity analysis is
run at all: define noise only on the orientation-*uncertain* set and report its size, conserve arc count,
report **residual FAS above the digon floor** as the statistic, report a z-score against a degree-preserving
directed-rewiring null, and report **argmin stability** (edge-wise inclusion frequency across optima), which
is where genuine instability lives. Consider dropping SCC entirely — it has no power here.

**(5) The hierarchy-orientation route is self-refuting and must never be used.** Orienting every edge
low→high by a rank scalar (T1w:T2w, principal gradient) produces **a DAG by construction**: every SCC becomes
a singleton and minimum FAS is **exactly zero**. You would be reading back your own sort order. A systematic
search found no peer-reviewed human study doing it — being first here is a warning, not an opportunity.

**(6) ⇒ DROP THE HUMAN REQUIREMENT — the recommendation is now much stronger than the multiple-realizability
argument alone made it.** Invertebrate connectomes are **edge-complete** where human data is 60–70% missing,
**synapse-resolved and genuinely directed** rather than causally inferred, and **small enough that EXACT
minimum-FAS is computable**, which human region-level graphs are not. **Top pick: Winding et al. 2023 larval
*Drosophila*** (*Science*, `10.1126/science.add9330`) — 3,016 neurons, whole brain, zero truncation, four
compartment-specific directed graphs, CC BY. **Decisively, the authors already publish "41% of brain neurons
were recurrent" plus a signal-flow ordering that is functionally a feedback-arc-minimising vertex ordering —
a published baseline to validate our instrument against.** Then Markov G29×29 (the only truly edge-complete
region-level matrix, behind a registration wall), marmoset (easiest ingest anywhere — one 123 KB file, no
auth), and *Ciona* (177, a complete chordate CNS) / *Platynereis* (2,675, whole animal) as exact-FAS controls.
**Keep F-TRACT as the human datapoint in a comparative set, not as the study** — and via the EBRAINS bucket
(HCP-MMP1 or Lausanne2008-60), **not** siibra's Julich-Brain build, which is the worst-covered one.

**(7) The instrument must be replaced regardless of which data is used.** Exhaustive subset or simple-cycle
enumeration is hopeless (sparse graphs routinely have Ω(2ⁿ) simple cycles). Use **Younger's ordering
formulation solved by branch-and-cut on the linear ordering polytope** (Grötschel, Jünger & Reinelt 1984,
`10.1287/opre.32.6.1195`); at n ≤ ~100 this is exact and fast.

**Three ingest traps to encode in any loader:** Allen (anterograde) and Marmoset (retrograde) have **opposite
injection semantics** — get it wrong and every cycle reverses; **unmeasured ≠ zero** (marmoset's 52.6%
unmeasured square would manufacture 61 spurious singleton SCCs); and `netneurotools`' `macaque_markov` is
**not** the canonical G29×29 (measured ρ=0.743 vs published 0.66).

**Licences:** F-TRACT is **CC BY-NC-SA 4.0** (verified in the data file). The HCP-derived connectome licence
**could not be verified** — check before publication.

<details><summary>Original brief, retained for provenance — already executed, do not re-issue</summary>

### The brief as issued

> Read-only feasibility check. Crucible has graph instruments that operate on a **connectivity matrix at
> region granularity**: (i) strongly-connected-component decomposition of a directed connectome, (ii) an
> exhaustive minimum-edge block search over the condensation graph computing the cost of opening all
> returning loops, (iii) a span/argmin search over region subsets. They currently run on a *synthetic*
> connectome family; the published caveat reads "scoped to this connectome family". Question: can
> `siibra-python` (FZJ INM-1, Julich-Brain) deliver a usable connectivity matrix, or does this need
> substantial glue?
>
> 1. **What connectivity does siibra expose**, with real API calls — structural (DWI/tractography) vs
>    functional (resting-state) vs other; returned as a matrix keyed by parcellation regions, in what type?
> 2. **DIRECTEDNESS — the critical one.** SCC decomposition and return-freedom are meaningless on a symmetric
>    matrix. Is any siibra connectivity directed, or is it all symmetric? **If undirected-only, say so
>    prominently** — that is close to fatal for instruments (i) and (ii) as written.
> 3. **Weights and thresholds** — weighted or binary, standard thresholding practice, typical densities.
> 4. **Granularity** — region counts for the main Julich-Brain versions; coarser/finer alternatives.
> 5. **Provenance** — group-average or per-subject; multiple cohorts (having several independent connectomes
>    would let the study report generality *across* connectomes).
> 6. **Practical access** — install, Python constraints, live API + credentials, download sizes, licence.
> 7. **VERDICT** — obtainable with modest glue (<1 day), only with significant work, or not obtainable?
>
> **Section 8 — where else can DIRECTED connectivity be obtained?** The study does **not** have to be human:
> any *real biological* connectome discharges the caveat, and a **phylogenetically diverse set** discharges it
> better — which also speaks to FMT's multiple-realizability claim (corvids and cephalopods).
> (a) Non-human tract-tracing, directed by construction — verify and characterise: CoCoMac; Allen Mouse Brain
> Connectivity Atlas; Markov/Kennedy quantitative retrograde macaque; Marmoset Brain Connectivity Atlas;
> FlyWire / *Drosophila*; *C. elegans*; MICrONS. For each: directed?, weighted?, node count, density, access,
> licence.
> (b) **Directed connectivity in humans** — CCEP (cortico-cortical evoked potentials from intracranial
> stimulation): is there an open probabilistic atlas across many patients? A Grenoble-based project is
> believed to exist; name and status unverified. Also assess DCM / spectral DCM / Granger / transfer entropy
> and state plainly how contested their directionality is.
> (c) **Orienting an undirected matrix** — hierarchy proxies (laminar termination à la Felleman & Van Essen;
> T1w:T2w myelination gradients), or mapping homologous macaque directed data onto human parcels. Primary
> citation, and what assumptions it smuggles in.
> (d) Ranked verdict, and state explicitly whether **dropping the human requirement** is the better path.
>
> **MG's ruling to fold in (2026-08-09):** mapping macaque directions onto a human connectome is an
> **acceptable fallback** — *"not much of a cheat"*. Do not rank it down on purity grounds; rank it below
> genuinely directed data and above not doing the study. Assess where homology holds (primary sensory/motor,
> visual areas, the feedforward/feedback laminar hierarchy) versus **prefrontal and association cortex**,
> which is where the transfer is expected to be weakest **and where FMT locates the explicit models and the
> ESM**. Is there an established cross-species transfer method with a primary citation, or is it improvised?
> **And assess the move that converts the objection into a measurement:** randomly re-orient a fraction of
> edges and measure how far the SCC inventory and the minimum-edge opening cost move. Robust to 10–20% error
> → defensible; fragile → ruled out on measurement rather than argument. **Is that sound for these particular
> statistics, and is there prior work on the robustness of SCC structure or feedback-arc-set size to edge
> orientation noise?**

**MG's design refinement, as proposed before the result landed:** macaque directions where homology holds,
**informed random** elsewhere, run as an ensemble, with the ensemble spread serving as the sensitivity
analysis. ⚠ **SUPERSEDED by finding (4) above — the ensemble spread would pass vacuously**, because full
randomisation of orientation moves the FAS by only 6.2% and the giant SCC not at all. The *ingest* half of
the refinement (macaque where homology holds, informed-random elsewhere) is unaffected and still correct if a
human connectome is used at all; it is only the "spread IS the sensitivity analysis" step that fails.

</details>

## 0b. ⚠ MG's correction on WHY a human-like connectome is wanted — read before re-scoping `AIW-197`

**MG, 2026-08-09 late, after the feasibility result:** *"drosophila yes, but human shape / macaque is more
interesting because we have dedicated language centers we can connect to or replace by an llm"*, and then:
*"which is a stupid experiment knowing the outcome anyways. thats really not the reason i want a human
similar brain."*

**Two things to carry, both corrections to how this session framed it.**

**(1) The generality study is a confirmation that cannot fail, and should probably not be run at all.** Not
merely blocked by the exponential instrument — **unmotivated**. We already know the answer: crucible measured
one giant recurrent mass on synthetic connectomes, the check measured one giant recurrent mass on F-TRACT,
and massive cortical recurrence is uncontroversial neuroscience. Computing the exact cut would produce a
number nobody doubts the sign of. **That is crucible's own pattern 39 — *a confirmation you cannot fail is
not a measurement*.** The session proposed it because "cheap, safe, upgrades a banked row" read as good
judgement; it was risk-aversion, and it displaced the question MG actually asked.

**(2) Fly is NOT a stepping stone to what MG wants, and must not be re-framed as one.** This session's
closing note called it "the instrument-validation step on the way" — wrong. No homology, no language
periphery, different animal; it answers a question that does not need answering.

**⇒ The reason for a human/macaque substrate is FUNCTIONAL, not structural validation:** it is the only
architecture with **dedicated language centres**, so an LLM can be **wired into that periphery or substituted
for it**, and what FMT claims about the explicit layer and the language interface becomes testable. That is
the same thread as crucible's **CRU-37 language-periphery design (Horizon C)** and the taught-vs-spontaneous
`"I"` reframe now sitting in `AIW-193`(g). **Re-scope `AIW-197` around that, not around discharging A#7's
caveat.**

⚠ **What survives from the feasibility check regardless:** F-TRACT is a real directed human connectome and is
free (`AnatomoFunctionalConnectivity`, 613 patients, no credentials) — **cortex, hippocampus and amygdala
only, no thalamus/striatum/brainstem/cerebellum**, which matters for any loop claim. And the exponential
instrument still has to be replaced before *any* cut-cost number is computed on *any* real connectome.

## 2. External inputs awaited

- **Khallieva et al. (2022), *Dreaming* 32(2):206–220** (`10.1037/drm0000190`) — MG requested full text via
  ResearchGate 2026-08-09. The only synaesthete dream cohort study. Three questions to put to it are in
  `AIW-194`. **It may already contain the answer to pattern #34's core question.**
- **Perplexity prompt** at `tmp/perplexity-dream-modality-search.txt` — MG ran a first sweep and the result is
  folded into `.claude/knowledge/didactic-patterns.md` §34. **Do not re-run it**; the remaining gaps are
  physical-copy items (Winget & Kramer 1979's 132-scale compendium; the printed category list of Hunt et al.
  1982, *Percept. Mot. Skills* 54(2):559–633).
- **Crucible's leg-1 verdict** — `~/crucible/docs/results/data/cru69_verdict.json`, due overnight
  2026-08-09→10. Input for the *next* revision of the `AIW-191` ranking, not this one.

## 3. Do NOT redo

- **`AIW-195` is closed as DROPPED**, deliberately. The short-return *anatomical* prediction is unfalsifiable
  as worded — basal-ganglia loops reach prefrontal cortex, everything routes through thalamus, so both sides
  claim the same evidence; the timing intuition inverts (hyperdirect ~12–15 ms vs L6 corticothalamic up to
  42.7 ms); and IIT 4.0 already states path length is irrelevant. **The λ cost crossover is untouched** and
  rides `AIW-193`(a). Do not re-propose the anatomical version.
- **The "empty coding slot" argument for pattern #34 is RETRACTED** — Revonsuo & Salmivalli's "Sensory
  Experiences" class is interoceptive (nausea, tickle) and was dropped for <1% frequency. The surviving
  argued absence is different and better; it is written up in `didactic-patterns.md` §34.
- **Do not write pattern #34's strong form.** Wundt 1874 and van der Heijden 2024 are positive reports, and
  the hedged sentence to defend is in the knowledge file verbatim, with its concessions.
