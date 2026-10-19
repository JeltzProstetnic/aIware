<!-- Action: reference -->
<!-- Tracked-by: AIW-271 -->
# CRU-198 σ≈1 audit of aIware texts — S326, 2026-09-29

**Trigger:** crucible CRU-194/CRU-198 (2026-09-29) found that its criticality instrument (subsampled
Beggs-Plenz branching σ + Class-4 membership) is effectively a firing-RATE meter: unwired cells at a matched
rate pass it. So every crucible result stated as "σ≈1", "critical", "in band", "30k σ≈1 basin" reads as
"fires at a matched rate". MG ordered the audit before the Oct 2 poster freeze (S326, handover Q3).
Method: read-only Explore sweep (subagent), findings below are its report. Spot-verify line numbers before editing.
Nothing has been edited on the strength of this file yet.

## Verdict
**MoC7 poster, handout and poster content are CLEAN.** No σ number appears. Criticality mentions are theory
or brain literature; the σ in Block 3 is the self-variable of do(σ:=c). Indirect exposure only: poster.html
:338–341 / handout :132–134 / content.md :241–243 cite the companion (zenodo.21610993) for toy-scale closure
results, and the companion itself carries (A) claims.

## (A) hits — claims resting on the invalidated instrument
**FMT master `paper/full/four-model-theory-full.md`** (same text in `latex/paper.tex`; copies in `wiki/llms-full.txt`)
- **:1003** σ≈1 and λ≈0 as "interchangeable *instruments* certifying the same capability band". σ≈1 certifies
  only a matched rate per CRU-194/198.
- **:1007** "sweeping the branching ratio across a self-preservation task leaves the self-model's own projection
  essentially unchanged" — the swept variable was effectively rate; the depth dissociation drawn from it is unsupported.
- **:1005 (fifth result)** spiking-scale re-entrant loop on crucible LifPool; the finding does not need σ, only
  the implied "critical substrate" framing does.
- **:1005 (fourth result)** band scanned over spectral radius, not branching σ — lower risk; check whether any
  of the "six settings" defined the band by crucible σ.
- **:443 / :1003** "nominal σ = 1 setpoint" in a leaky ESN is spectral radius, probably unaffected; the shared
  symbol invites confusion.
- **:1011** "the capability-first reading of criticality it requires" — (A) by inheritance from the companion.

**Companion `drafts/companion-computational-paper-draft.md`** (public = zenodo 21610993, v3 deposit due Oct 9–10)
- :105, :248 σ≈1 / λ≈0 as interchangeable instruments; :145 LifPool branching-σ 0.44–1.03 measured from raster;
  :220 "homogeneous critical spiking reservoir" (CRU-36); :226 "Gain = 1.0 corresponds to branching-σ ≈ 1"
  (the instrument itself); :137 / :232 spectral-radius band — check as for master :1005.

**JAIC draft `drafts/aiw130-jaic-draft.md`** — :151 LIF pool "self-organizes to a branching ratio near unity"
(design, :153 says not-yet-instantiated, but presents σ≈1 as proof of criticality); :153 "criticality is not
an ornament but a functional resource"; :157 "criticality ablation" — check what it detunes.
`aiw130-jaic-plan.md` :54, :110, :142 repeat "LIF pool at self-organized criticality".

**Wiki** — `physical-foundations/criticality.md:48` (and diagram :40) treats σ≈1 as the quantity experiments
measure — borderline (theory, but σ as capability measure). `formal/formalization.md:23`,
`open-questions/overview.md:51`, `index.md:286` link the companion without quoting σ (inherit only).
`llms-full.txt` duplicates master :1003 (at :2214), :1007 (:2220), §3.7 :443 (:1662).

## (B) — fine
Brain-literature criticality (ConCrit, Kanders, Priesemann σ≈0.98, Beggs & Plenz) across fmt_formal,
trimmed/noc, intelligence, basics/criticality.md, formal/information-theoretic.md, substrate-independence.md.

## Suggested fix order (needs MG — ties to AIW-271's re-scope decision)
master :1003/:1007 (+ llms-full regenerates from master) → companion :105/:145/:220/:226/:248 (before the
Oct 9–10 v3 deposit) → JAIC :151/:153 → wiki criticality.md:48.
