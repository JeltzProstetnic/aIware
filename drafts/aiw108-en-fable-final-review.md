# AIW-108 — EN edition: final QA pass (S255, 2026-07-11)

**Purpose (MG, S255):** LAST-LINE quality sweep of the PUBLISHED ed.2 EN manuscript for **defects that have hidden well** — factual errors, contradictions, broken cross-refs, coherence breaks, prose tells that survived prior passes. **NOT a theory revision.** Reviewers: 5× `claude-fable-5` over disjoint ranges (all self-ID confirmed, gate open). FLAG-ONLY — nothing rewritten. Crucible model results are optional upside only ("could footnote 'confirmed in a model'"), never a reason to touch published claims. **Nothing is falsified → "none has been falsified" stands.**

Coverage: front+Ch1–4 (R1), Ch5–8 (R2), Ch9–12 (R3), Ch11+App H (probe), Ch13–17 (R4), Coda+App A–G (R5).

---

## HIGH — fix before any reprint

| Location | Issue | Fix |
|---|---|---|
| Ch.13 ~L1248 "Libet **proved this in 1979**" | **Wrong date.** The described readiness-potential study (RP 550 ms before movement, awareness ~200 ms before) is Libet, Gleason, Wright & Pearl **1983** (*Brain* 106). 1979 is Libet's *separate* sensory-timing/backward-referral paper. Hid well because 1979 is a real Libet year. | → **1983**. |

## MED — verify / qualify

| Location | Issue | Action |
|---|---|---|
| Ch.13 ~L1254 "a computer with **two mice**… the confederate moved it" | Doesn't match Wegner's canonical **"I Spy" (Wegner & Wheatley 1999)** — shared planchette + auditory priming + forced stops, not two mice with one hidden. Named researcher + study = a psychologist will catch it. | Verify vs Wegner & Wheatley 1999; correct the setup. |
| Ch.5 ~L534 citations | Two load-bearing 2025–26 criticality cites unverifiable: **Hengen/Shew "140 datasets, *Neuron* 2025"** and **Algom/Shriki "ConCrit, *N&BR* 2026"**. The "empirical dam broke" beat rests on them. | Verify journal/year/authors/dataset-count. |
| Ch.4 ~L418 | **Joscha Bach direct quotes** ("a virtual reality projected into a virtual observer"; "uploaded into a monkey…") — accuracy load-bearing (named living person). | Verify verbatim vs source. |
| Ch.6 ~L650 "**strongest psychedelic substance on Earth**" | Drops the load-bearing qualifier. Salvinorin A = most potent *naturally occurring* hallucinogen; LSD is stronger by mass. | → "most potent *naturally occurring*…". |
| Ch.12 ~L1128 "fruit fly **partial** connectomes" | Dated for a 2026 book — the **complete** adult *Drosophila* connectome (FlyWire, ~140k neurons) was published 2024. | → "full fruit-fly connectomes". |
| Notes ~L1924 | Notes jump **Ch.13 → Ch.15** — no Chapter 14 note. | Confirm Ch.14 needs none, else the entry is dropped. |

## LOW — factual precision / robustness

| Location | Issue |
|---|---|
| Coda ~L1854 "**I'm fifty**" | **MG: any exact age is correct for <1 year → self-dates the book.** Reword to an age-robust construction (drop the hard number). Note: 50 is also factually off (born 1978 → 47/48 in 2026). |
| Ch.5 ~L626 "cocaine, meth, and alcohol **physically destroy neurons**" | Overstated for cocaine (its harm is chiefly ischemic/cardiovascular); meth + chronic alcohol support it. Qualify or drop cocaine from the trio. |
| Ch.3 ~L286 salvia "**proprioceptive input overwhelms** the system" | Interpretive/dubious mechanism (salvinorin = κ-opioid dissociative). Soften if reprinted. |
| Ch.3 ~L322 "you'd expect to occasionally lose one… **never happens**" | Absolute overstates — focal retrograde amnesia / category-specific deficits exist in pathology. Optional hedge. |
| Ch.13 L1246 "**20 Hz**" vs L1276 "**5 Hz**" conscious rate | Two unreconciled figures for "conscious" rate. Add one clause: simulation-update (20 Hz) vs decision (5 Hz). |
| Ch.16/App F Bekenstein bound "surface area, not volume" (L1778) + "unitarity is a consequence of the Bekenstein bound" (App F ~L2335) | Pure Bekenstein bound = entropy↔energy; strict area-scaling is the holographic/BH-entropy result. Consistent pop-sci simplification (author's call); App F's unitarity-from-Bekenstein is stated flatly where the same appendix hedges its 3-generations claim → add a matching hedge. |
| Ch.5 ~L466 Game of Life "**three rules**" (×3) | Canonically 3–4 rules (birth/survive/die). Defensible compression; consider "a handful". |
| App H / Ch.11 ketamine vs Pred 5 "should not drop below criticality" | Anesthetic-dose ketamine tends to *preserve/raise* LZ/PCI complexity → the empirically weakest link in the "converges on criticality" battery. Robustness flag; a one-line hedge helps. |

## Cross-reference & coherence

| Location | Issue |
|---|---|
| Ch.14 L1380 "**In Chapter 5**… three possible relationships" vs Ch.15 L1422 "**In the last chapter**…" | Same "three relationships" attributed to two chapters. Harmonize + confirm Ch.5 actually contains them. |
| Ch.5 ~L516 "**the** permeability leak" | Definite article before "permeability gradient" is formally introduced (Ch.6 ~L566). Forward-dependency. |
| Ch.9 ~L892 "the clinical chapter" / L906 "the appendix at the back" | Vague vs the book's precise cross-refs elsewhere → name Chapter 8 / Appendix H. |
| Ch.9 ~L908 "into the nest, into **the hive**" | Foreshadows collective/hive minds; Ch.10 treats insects only as an individual-criticality boundary case → payoff never lands. |
| Ch.13 L1238 (Leibniz's Law) + L1310 (clock analogy) | Zombies fully argued twice without back-reference — reads as re-settling. Add "as I flagged earlier" at the second. |
| Ch.16/17 weak points **#4** (L1820) + **#5** (L1822) | Both reduce to "Gödel from within" — sharpen so #4 = model-unfalsifiability, #5 = observer-projection. |
| Ch.2 ~L140 "one principle for animals… one for zombies and free will" | Verify the two promised principles actually pay off where animals / zombies are treated (the animals one looks exposed in Ch.2). |
| Appendix refs (A/C/E/F/G) across the book | Integrity-check they exist and contain the cited content (unverifiable from within individual ranges). |

## Structural — ed.3 (already logged; confirmed in place)

- **Coda ~L1856–1862:** re-narrates the avalanche / knockout / 4D-fractal episodes **at full length** → compress to callbacks; keep only the fresh "bootstrap from nothing / be nice to everyone" move.
- **Ch.15 ~L1454:** a callback phrase ("which we first met in Chapter 5") was inserted, **but Per Bak's 1987 sandpile is then re-taught in full** → trim the re-teaching to one line. (Per Bak 1987 date is correct.)
- **"German book" self-ref:** located at Ch.17 ~L1838, phrased **"the 2015 book"** — already de-germanized. **Resolved** (author's call whether to keep).

## Prose consistency / tells

| Location | Issue |
|---|---|
| L1374 / L1676 / L1728 | "a theory that claims to have no open questions **isn't a theory — it's a religion / sales pitch**" — same aphorism **3×**; keep one (the "sales pitch" variant). |
| L1668 "Class 4 **automatons**" | Book uses **"automata"** everywhere else (L1452/1514/1622/1708) → fix for consistency. |
| Ch.16–17 (L1708/1764/1766/1832…) | Anti-metaphor hammer ("not a metaphor / not an analogy / structural identity") **5–6×** → thin one or two. |
| Ch.5 L552 ≈ L554 | Near-verbatim "beauty→reality has been rightly/legitimately criticized" hedge in adjacent paragraphs → state once. Also two "this stunned me" beats (L542/L554) → keep the stronger. |
| Throughout (R1) | High-density "not X — it's Y" antithesis cadence + heavy em-dash clustering — style, but a final pass could vary a handful. |

## Artifacts

- **Ch.4 ~L272:** leftover `<!-- FUTURE: Color edition figure … SDXL prompt preserved in git history -->` editorial comment still in the published source → remove.
- **Ch.16 L1476 `$10^{-35}$`** (raw inline LaTeX) vs L1636 glyph-avoidance ("the Greek letter Phi") → verify KDP/PDF renders the inline math and align the convention.

## Optional "confirmed in a model" enrichment (secondary, MG's call)
- Reviewers surfaced no claim requiring this. The only *opportunity* (not a defect): where Ch.12 discusses building a conscious machine, an ed.3 could footnote that closure's model-maintenance and criticality's compute role have **preliminary positive support in a computational model** — additive, positive-framed, only if MG wants it.

**Bottom line:** No BLOCKER, nothing reprint-*blocking* for the existing ed.2 run. The two that genuinely hid well and should be fixed before ed.3 are the **Libet 1983 date** (HIGH) and the **Wegner "I Spy" setup** (MED) — both named-source factual claims a specialist will catch. Everything else is verify/qualify/polish.
