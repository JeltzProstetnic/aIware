<!-- Action: reference -->
<!-- Tracked-by: AIW-192, AIW-190 -->
# Can MG's sleep claim be tested on public data? — feasibility check

**Status:** feasibility note, S297 (2026-08-08). Tracks `AIW-192`, serves `AIW-190` and didactic pattern
**#14**. Answers MG's question of 2026-08-08: *"can we do that reanalysis with public data?"*

**Answer: yes for the dissociation, with a substitution for the depth axis, and the deepest-sleep regime
— the one the claim is actually about — is where the data is thinnest.**

---

## 1. The dataset exists and it is better suited than expected

**DREAM — a dream EEG and mentation database.** *Nature Communications* 16(1), 7495 (13 Aug 2025),
`10.1038/s41467-025-61945-1`. Repository: `monash.edu/dream-database`, `10.26180/22133105`.
**CC-BY-4.0.** Most constituent datasets download freely; a minority require a request to the original
corresponding author.

Initial release: **20 datasets, 505 participants, 2,643 awakenings**, of which **1,550 carry a
standardized report classification**. Minimum per awakening: ≥20 s of sleep M/EEG at ≥100 Hz on ≥2
electrodes up to the moment of waking, plus manually scored sleep stage.

**The decisive feature is that its three report categories are exactly the distinction the claim turns
on**, standardized across all 20 contributing studies:

| Category | Database's own definition |
|---|---|
| **Experience (E)** | reports experiences during sleep **and can recall specific content** |
| **Experience without recall (EWR)** | reports having had experiences **but no recall of specific content** — the database's own term is *"white dream"* |
| **No experience (NE)** | no recall of experiences **and no impression that there would have been any** |

**EWR is awareness-without-consolidation as a measured category.** It is not a proxy for it and not an
inference from it — the participant asserts experience occurred and cannot report its content. That is
didactic pattern **#14**'s dissociation, already collected, already standardized, already public.

## 2. The gap: no arousal threshold anywhere in it

**The database records no arousal threshold, no awakening-stimulus intensity, no latency to wake, and
no sleep-depth index.** MG's operational handle — *"the one where it is really hard for people even to
wake you"* — is therefore not directly available, and this is the one real obstacle.

**Two substitutions, in increasing order of quality.**

- **Sleep stage**, which the database does carry. Crude, three or four discrete levels, and confounded
  with everything else that differs between stages.
- **Slow-wave activity computed from the supplied EEG** — 0.5–4 Hz power in the ≥20 s preceding each
  awakening. SWA is the standard continuous correlate of arousal threshold, it is derivable from data
  the database guarantees is present, and critically it permits testing **within** stage, which is what
  separates a depth effect from a stage effect. **This is the analysis to run.**

## 3. The published stage table already points the right way — and is not enough

From the paper's own breakdown (n = 1,550):

| Stage | E | EWR | NE |
|---|---|---|---|
| N1 | 97 (88%) | 1 (1%) | 12 (11%) |
| N2 | 485 (56%) | 68 (8%) | 308 (36%) |
| N3 | 31 (48%) | **7 (11%)** | 26 (41%) |
| REM | 416 (81%) | 12 (2%) | 87 (17%) |

Two things are visible and neither is conclusive.

**NE rises with depth** — 11% → 36% → 41% across N1→N2→N3 — in the order arousal threshold rises. That
is the coarse version of the prediction, and it is unsurprising enough that on its own it discriminates
nothing: every account predicts fewer reports from deeper sleep.

**EWR also rises with depth** — 1% → 8% → **11%**, peaking in N3, and collapsing to 2% in REM. *That*
is the interesting number, because the two accounts differ on it:

- If experience **stops** below a floor, EWR should **vanish** at the greatest depth: there is nothing
  to have an impression of.
- If experience **persists and consolidation fails** (MG's account, pattern #14), EWR should **survive
  or grow** into the deepest sleep, with NE overtaking it only at the extreme.

**EWR is at its maximum in N3.** The sign favours the consolidation account. **But n = 64 classified N3
awakenings total, 7 of them EWR** — that is far too little to carry a claim, and N3 is precisely the
regime the claim is about.

## 4. What the reanalysis would actually be

1. Pull the openly-downloadable DREAM subsets; record which required author request and exclude or
   report them separately.
2. Compute SWA (0.5–4 Hz relative power) over the pre-awakening window, per awakening, per subject.
3. Model report category against SWA **within stage**, with subject and source-study as random effects
   — the 20 studies used different awakening methods and different native categorization schemes mapped
   onto the three, so study is a mandatory random effect, not an optional one.
4. **The discriminating test is the shape of the EWR curve, not the NE curve.** Pre-register that
   distinction before looking, because NE-rises-with-depth is confirmable under every account and is
   exactly the "confirmation you cannot fail" that crucible's pattern 39 warns about.
5. Report the N3 cell size prominently whatever the result.

## 5. Limits to state up front

- **Substituted axis.** SWA is a proxy for arousal threshold, well-established but a proxy; the claim
  MG stated is about wakeability, and no public dream dataset appears to measure it.
- **The deepest sleep is the thinnest data.** 64 classified N3 awakenings against 863 in N2. The
  regime the claim is about is the one the corpus barely samples.
- **NE is interpretively unsafe on its own.** A "no experience" report cannot distinguish absence of
  experience from total failure to retain it — which is *why* EWR carries the argument.
- **Narcosis is untestable here.** The other half of MG's exception, anaesthesia, is absent from this
  corpus entirely and would need a different literature.
- **This tests Half 1 only.** The claim that one can be aware *most of the time* during sleep with fine
  senses is not addressed by awakening-based data at all.

## 6. Why it is worth doing anyway

It converts a claim MG himself called *"a lot of unprovable claims"* into a pre-registerable analysis on
open CC-BY data with an established instrument, at zero data-collection cost. And the target is not the
obvious one: **the result that would matter is the behaviour of the white-dream category at depth**,
which is a number nobody appears to have looked at with this question in mind, and which the two
accounts genuinely split on.
