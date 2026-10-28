# FMT corpus cross-check (AIW-303) — 2026-10-19

## Summary

Five reader groups checked the FMT corpus against the master source (`paper/full/four-model-theory-full.md`, which is v20 plus the unpublished S341 corrections). A verifier then confirmed 144 findings, 45 of them claim-changing, and rejected 10. Most of the claim-changing findings come from three things. Criticality is still treated as a condition of consciousness in several places (the master itself, both formalizations, the cosmology papers, the crucible spec and two unpublished drafts). Pre-S341 wording still makes explicit content phenomenal without the closed-loop condition. And a few citations misreport their source, most seriously Boly et al. (2012), which the master cites for the opposite of what that paper found.

Reference standard: where a publication contradicts published v20 but matches the master source, that is not counted as an error. The rule for the last column (MG, S342) is that only claim-changing errors in published works get a new Zenodo version immediately. "Published" means: FMT master, the formalizations, RIM, RIM formal, SB-HC4A and its formalization, CMB MFDFA, No Outside, Worm, PLR comment, falsity gradient, Silent suffering/robot plea, and the JCS carve.

## Works and confirmed findings

One finding can touch several works, so it is counted once in each work's row. Totals at the bottom count each finding once.

| Work | File | Published? | Confirmed | Claim-changing |
|---|---|---|---|---|
| FMT master | paper/full/four-model-theory-full.md | yes | 28 | 7 (PREDICTIONS-1 and CITATIONS-1 are the same issue) |
| FMT formalization | paper/fmt_formal/fmt-formalization.md | yes | 21 | 6 |
| RIM (intelligence paper) | paper/intelligence/paper.md | yes | 5 | 0 |
| RIM formalization | paper/rim_formal/rim-formalization.md | yes | 16 | 7 |
| SB-HC4A | paper/cosmology/sb-hc4a.md | yes | 9 | 1 |
| SB-HC4A formalization | paper/cosmology_formal/sb-hc4a-formalization.md | yes | 15 | 5 |
| CMB MFDFA | paper/cmb_mfdfa/cmb-mfdfa.md | yes | 5 | 1 |
| No Outside | drafts/zenodo-ready/nooutside/no-outside-draft-v1.0.md | yes | 7 | 2 |
| Worm on the disk | drafts/papers-s339/worm-on-the-disk.md | yes | 3 | 1 |
| PLR comment | drafts/zenodo-ready/plr/plr-loops-commentary.md | yes | 3 | 0 |
| Falsity gradient | drafts/zenodo-ready/falsity/falsity-gradient.md | yes | 4 | 0 |
| Silent suffering / robot plea | drafts/zenodo-ready/robot/robot-consciousness-plea.md | yes | 6 | 1 |
| JCS carve (both copies) | drafts/zenodo-ready/jcs/jcs-fmt-carve.md, drafts/papers-s339/jcs-fmt-carve.md | yes | 8 | 2 |
| Companion (in-silico tests) | drafts/companion-computational-paper-draft.md | has a Zenodo deposit (concept 21610993) but is not on MG's S342 list | 12 | 5 |
| Crucible implementation spec | /home/jeltz/crucible/papers/fmt-implementation-spec.md | no (crucible-owned) | 12 | 6 |
| NoC draft (AIW-130 Lane A) | drafts/aiw130-noc-draft.md | no | 7 | 4 |
| JAIC draft | drafts/aiw130-jaic-draft.md | no | 10 | 2 |
| Olinyk / CRC convergence | drafts/aiw120-olinyk-crc-fmt-convergence.md | no | 6 | 5 |
| Minimal self | drafts/papers-moc7/minimal-self.md | no | 6 | 3 |
| Deriving the FMT definition | drafts/papers-moc7/deriving-the-fmt-definition.md | no | 3 | 2 |
| Theory map (+ fmt-claims.json) | drafts/papers-moc7/theory-map-paper.md | no | 6 | 1 |
| Qualia privacy | drafts/aiw105-qualia-privacy-paper-draft.md | no | 3 | 2 |
| eNeuro opinion | paper/aiw47/aiw47-eneuro-opinion.md | no | 6 | 1 |
| Permeability/criticality | paper/fmt_permeability_criticality/fmt-permeability-criticality.md | no | 4 | 0 |
| Other (blog, paper1, definitions-not-settled, knowledge files) | see entries | no | 5 | 0 (one claim-changing finding also touches the registry) |
| **Total (distinct findings)** | | | **144** | **45** |

## Published works that need a new Zenodo version now

These are the published works hit by at least one claim-changing finding.

| Work | Findings | Note |
|---|---|---|
| FMT master | SUFFICIENCY-1, SUFFICIENCY-2, PHENOMENAL-1, ARCHITECTURE-7, PREDICTIONS-1 = CITATIONS-1, PREDICTIONS-3 | Fold into v21 (AIW-302). SUFFICIENCY-1/2, PREDICTIONS-1 and PREDICTIONS-3 are already in published v20. |
| FMT formalization | SUFFICIENCY-11, SUFFICIENCY-12, PHENOMENAL-2, ARCHITECTURE-8, PREDICTIONS-6, CITATIONS-2 | PHENOMENAL-2 and PREDICTIONS-6 follow from S341, so they should cite v21 once it is out. |
| RIM formalization | SUFFICIENCY-12, SUFFICIENCY-16, PHENOMENAL-2, ARCHITECTURE-2, ARCHITECTURE-3, ARCHITECTURE-8, PREDICTIONS-8 | Several of these come from summarising an older RIM; the RIM paper itself is fine. |
| SB-HC4A | SUFFICIENCY-18 | |
| SB-HC4A formalization | SUFFICIENCY-18, ARCHITECTURE-4, PREDICTIONS-9, PREDICTIONS-10, PREDICTIONS-11 | The formalization disagrees with the main paper in four places. |
| CMB MFDFA | CITATIONS-4 | Wrong reference, and a misquotation. |
| No Outside | SUFFICIENCY-19, PHENOMENAL-3 | SUFFICIENCY-19 needs an MG decision first (see the entry). |
| Worm on the disk | SUFFICIENCY-19 | Needs the same MG decision. |
| Robot plea | ARCHITECTURE-6 | |
| JCS carve | PHENOMENAL-3, CITATIONS-3 | CITATIONS-3: the pinned v20 DOI shows the opposite of the cited §3.4.6 split. Fix it before submission. |
| Companion (if MG counts it as published) | SUFFICIENCY-12, SUFFICIENCY-13, PHENOMENAL-3, ARCHITECTURE-7, ARCHITECTURE-8 | SUFFICIENCY-13 cites §3.7.3 for the opposite of what §3.7.3 says. |

Overlaps: several IDs describe the same defect from different groups. They are kept separate here so the IDs stay traceable.
- Crucible spec: SUFFICIENCY-17, ARCHITECTURE-1, PREDICTIONS-5, PHENOMENAL-11.
- Explicit = phenomenal: PHENOMENAL-1, PHENOMENAL-2, PHENOMENAL-3, ARCHITECTURE-7, PREDICTIONS-6.
- "Minimum sufficient set": SUFFICIENCY-12, ARCHITECTURE-8.
- Φ vs Ψ: SUFFICIENCY-15, PHENOMENAL-13, ARCHITECTURE-9.
- NoC draft necessity framing: SUFFICIENCY-23, PREDICTIONS-4.
- Boly 2012: PREDICTIONS-1, CITATIONS-1.

## Index of confirmed findings

CC = claim-changing. Last column = published work → needs a new Zenodo version now?

| ID | Title | Kind | Severity | Published work → new version now? |
|---|---|---|---|---|
| SUFFICIENCY-1 | Master makes the criticality signatures satisfy the Class 4 commitment | internal-contradiction | CC | yes (master) |
| SUFFICIENCY-2 | PP comparison names criticality as a determinant of consciousness | internal-contradiction | CC | yes (master) |
| SUFFICIENCY-11 | FMT formalization uses criticality as a qualifying condition | internal-contradiction | CC | yes (FMT formalization) |
| SUFFICIENCY-12 | "Minimum sufficient set" against master's "necessary but not sufficient" | contradicts-master | CC | yes (FMT formalization, RIM formalization) |
| SUFFICIENCY-13 | Companion cites §3.7.3 for "jointly sufficient", which §3.7.3 denies | bad-citation | CC | companion: MG to confirm whether it counts as published |
| SUFFICIENCY-16 | RIM formalization hardens a separable cost conjecture into "cannot" / iff | mutual-contradiction | CC | yes (RIM formalization) |
| SUFFICIENCY-17 | Crucible spec requires criticality, with a σ biconditional | contradicts-master | CC | no (unpublished, crucible) |
| SUFFICIENCY-18 | Cosmology papers define Class 4 with SOC built in | internal-contradiction | CC | yes (SB-HC4A, SB-HC4A formalization) |
| SUFFICIENCY-19 | Record = run argument reduces FMT's conjunction to architecture | contradicts-master | CC | yes (No Outside, Worm), after MG decision |
| SUFFICIENCY-23 | NoC draft thesis "no criticality, no consciousness" | contradicts-master | CC | no (unpublished) |
| SUFFICIENCY-24 | NoC draft confines open-ended computation to the edge of chaos | mutual-contradiction | CC | no (unpublished) |
| SUFFICIENCY-28 | Olinyk draft puts FMT's threshold "at criticality" | contradicts-master | CC | no (unpublished) |
| PHENOMENAL-1 | Master keeps pre-S341 "explicit = phenomenal" wording | internal-contradiction | CC | yes (master, v21) |
| PHENOMENAL-2 | Formalizations and spec equate ν > ν_crit with phenomenal | contradicts-master | CC | yes (FMT formalization, RIM formalization) |
| PHENOMENAL-3 | Drafts say "explicit models are phenomenal" without the loop qualifier | contradicts-master | CC | yes (No Outside, JCS); companion: MG to confirm |
| PHENOMENAL-4 | Deriving draft quotes the sentence S341 retired | bad-citation | CC | no (unpublished) |
| PHENOMENAL-5 | Theory map: accessible content "stays on the implicit side" | contradicts-master | CC | no (unpublished) |
| PHENOMENAL-6 | JAIC: closure is one-way in prose and Check 2, mutual in Box 1 | internal-contradiction | CC | no (unpublished) |
| PHENOMENAL-7 | JAIC/Olinyk: FMT "dissolves" the Hard Problem | contradicts-master | CC | no (unpublished) |
| PHENOMENAL-8 | Olinyk: FMT "deflationary" about qualia | contradicts-master | CC | no (unpublished) |
| PHENOMENAL-9 | Olinyk credits FMT with the spontaneous-report criterion it declines | contradicts-master | CC | no (unpublished) |
| PHENOMENAL-10 | Minimal-self says published FMT has no floor below basic | contradicts-master | CC | no (unpublished) |
| PHENOMENAL-11 | Crucible spec requires depth ≥ ρ₁ for any consciousness | contradicts-master | CC | no (unpublished) |
| ARCHITECTURE-1 | Crucible spec stale: five principles, criticality required | contradicts-master | CC | no (unpublished) |
| ARCHITECTURE-2 | RIM formalization summarises a retired definition of motivation | contradicts-master | CC | yes (RIM formalization) |
| ARCHITECTURE-3 | RIM formalization: gap detection barred to implicit systems | contradicts-master | CC | yes (RIM formalization) |
| ARCHITECTURE-4 | SB-HC4A formalization: a Uniqueness theorem the parent disowns | mutual-contradiction | CC | yes (SB-HC4A formalization) |
| ARCHITECTURE-5 | eNeuro: closure as the level-setting variable | contradicts-master | CC | no (unpublished) |
| ARCHITECTURE-6 | Robot plea defines consciousness as a capacity | contradicts-master | CC | yes (robot plea) |
| ARCHITECTURE-7 | Unqualified "explicit = phenomenal" in Table 1 and three downstream texts | contradicts-master | CC | yes (master, v21); companion: MG to confirm |
| ARCHITECTURE-8 | "Minimum sufficient set for human-level consciousness" | contradicts-master | CC | yes (FMT formalization, RIM formalization) |
| PREDICTIONS-1 | Master cites Boly 2012 for a thalamocortical breakdown it did not find | bad-citation | CC | yes (master); same issue as CITATIONS-1 |
| PREDICTIONS-3 | Criticality convergence counted as support for the requirement | internal-contradiction | CC | yes (master) |
| PREDICTIONS-4 | NoC draft asserts criticality is necessary | contradicts-master | CC | no (unpublished) |
| PREDICTIONS-5 | Crucible spec keeps withdrawn σ≈1 predictions | contradicts-master | CC | no (unpublished) |
| PREDICTIONS-6 | Formalization C(t) counts preconscious explicit content as conscious | contradicts-master | CC | yes (FMT formalization) |
| PREDICTIONS-8 | RIM formalization attributes claims the intelligence paper does not make | mutual-contradiction | CC | yes (RIM formalization) |
| PREDICTIONS-9 | SB-HC4A formalization: James-Stein read as nonlocality law, "admissible" | mutual-contradiction | CC | yes (SB-HC4A formalization) |
| PREDICTIONS-10 | SB-HC4A formalization: heat death = Bekenstein saturation | mutual-contradiction | CC | yes (SB-HC4A formalization) |
| PREDICTIONS-11 | SB-HC4A formalization derives B and L conservation | mutual-contradiction | CC | yes (SB-HC4A formalization) |
| PREDICTIONS-13 | Qualia-privacy draft overstates Kawakita as individual-level alignment | contradicts-master | CC | no (unpublished) |
| CITATIONS-1 | Boly 2012 says the opposite of what the master cites it for | bad-citation | CC | yes (master); same issue as PREDICTIONS-1 |
| CITATIONS-2 | Formalization credits ConCrit with Hengen & Shew's 140-dataset analysis | contradicts-master | CC | yes (FMT formalization) |
| CITATIONS-3 | JCS pins the v20 DOI for a correction made after v20 | bad-citation | CC | yes (JCS, fix before submission) |
| CITATIONS-4 | CMB: Movahed 2011 chimera reference and overstated quote | bad-citation | CC | yes (CMB MFDFA) |
| SUFFICIENCY-3 | Seizure / σ≈0.98 passages lean on criticality as predictor | internal-contradiction | minor | no (minor) |
| SUFFICIENCY-4 | Table 4 orders states by criticality; covert-awareness cell unsupported | internal-contradiction | minor | no (minor) |
| SUFFICIENCY-5 | Criticality called "the neural effect" unhedged | internal-contradiction | minor | no (minor) |
| SUFFICIENCY-6 | Sufficient conjuncts read as necessary (robot plea) | inconsistency | minor | no (minor) |
| SUFFICIENCY-7 | "Qualitatively obvious" beside "no test is conclusive"; broken sentence | internal-contradiction | minor | no (minor) |
| SUFFICIENCY-8 | "Fit window" cited to §4.2.4, which never defines it | bad-citation | minor | no (minor) |
| SUFFICIENCY-9 | Corvid consciousness asserted as fact | internal-contradiction | minor | no (minor) |
| SUFFICIENCY-10 | Convergence paragraph overstates "in the Class 4 regime" | internal-contradiction | minor | no (minor) |
| SUFFICIENCY-15 | Closure fixed point written Φ after rename to Ψ | inconsistency | minor | no (minor) |
| SUFFICIENCY-20 | No Outside: physics dependency "not now stated" | inconsistency | minor | no (minor) |
| SUFFICIENCY-26 | JAIC lists PCI among criticality signatures | contradicts-master | minor | no (minor) |
| SUFFICIENCY-27 | JAIC states "abolish free modelling → subcritical" as a law | inconsistency | minor | no (minor) |
| SUFFICIENCY-29 | Formalization adds "continuous density" as a necessity | inconsistency | minor | no (minor) |
| PHENOMENAL-12 | Formalization defines closure as an ESM self-fixed-point; misquote | inconsistency | minor | no (minor) |
| PHENOMENAL-13 | Symbol, depth label and R(t) disagreements across formal texts | mutual-contradiction | minor | no (minor) |
| PHENOMENAL-14 | Master stale cross-references (§3.4.2, footnote 3) | internal-contradiction | minor | no (minor) |
| PHENOMENAL-15 | Minimal-self uses "access" for reportability | inconsistency | minor | no (minor) |
| PHENOMENAL-16 | Permeability paper glosses explicit as "conscious-access" | inconsistency | minor | no (minor) |
| PHENOMENAL-17 | Qualia-privacy: "fully dissolved" | contradicts-master | minor | no (minor) |
| ARCHITECTURE-9 | Φ(m*)=m* cited at "Section 6.3" | bad-citation | minor | no (minor) |
| ARCHITECTURE-10 | RIM calls R(t) the closure condition | inconsistency | minor | no (minor) |
| ARCHITECTURE-11 | RIM: C=0 does not force M=0 in either equation | internal-contradiction | minor | no (minor) |
| ARCHITECTURE-12 | RIM symbol overloads (ρ, σ) | internal-contradiction | minor | no (minor) |
| ARCHITECTURE-13 | RIM module numbering mismatch | internal-contradiction | minor | no (minor) |
| ARCHITECTURE-14 | FMT formalization module numbering, missing Table 1 / Eq. [1] | internal-contradiction | minor | no (minor) |
| ARCHITECTURE-15 | "Four nested models" | contradicts-master | minor | no (minor) |
| ARCHITECTURE-16 | Master says "four models" beside its own disclaimer | internal-contradiction | minor | no (minor) |
| ARCHITECTURE-17 | "Two kinds of models" names different axes across papers | inconsistency | minor | no (minor) |
| ARCHITECTURE-18 | Depth tables and theory map omit the minimal-consciousness floor | contradicts-master | minor | no (minor) |
| ARCHITECTURE-19 | Encoder relation called "transfer"; binding a "requirement" | contradicts-master | minor | no (minor) |
| ARCHITECTURE-20 | "Gating" vocabulary persists after REV-1 | inconsistency | minor | no (minor) |
| ARCHITECTURE-21 | Master: forking cited to §6.5, consolidation to §3.4.3 | internal-contradiction | minor | no (minor) |
| ARCHITECTURE-22 | Master §8.1/§8.5 localise the explicit models | internal-contradiction | minor | no (minor) |
| ARCHITECTURE-23 | Intelligence paper: "seven steps", six listed | internal-contradiction | minor | no (minor) |
| ARCHITECTURE-24 | Intelligence paper: distinction "formalized" in master | bad-citation | minor | no (minor) |
| ARCHITECTURE-25 | SB-HC4A formalization misdescribes the five-class split | mutual-contradiction | minor | no (minor) |
| ARCHITECTURE-26 | SB-HC4A formalization: Gödel from the fixed point, and not | internal-contradiction | minor | no (minor) |
| ARCHITECTURE-27 | Cosmology papers: explicit models as a "projection of selected information" | contradicts-master | minor | no (minor) |
| ARCHITECTURE-29 | JCS: self-model-free loop called "Stage 2" | internal-contradiction | minor | no (minor) |
| ARCHITECTURE-30 | JAIC/eNeuro: "two orthogonal dimensions" | contradicts-master | minor | no (minor) |
| ARCHITECTURE-31 | JAIC/NoC: implicit models "in the raw dynamics" | contradicts-master | minor | no (minor) |
| ARCHITECTURE-32 | Olinyk: FMT rejects smooth fading | contradicts-master | minor | no (minor) |
| ARCHITECTURE-33 | Companion overloads σ and redefines R | internal-contradiction | minor | no (minor) |
| ARCHITECTURE-35 | 2015-definitions file lacks the p.243 Lernfähigkeit sentence | inconsistency | minor | no (knowledge file) |
| PREDICTIONS-7 | Intelligence paper: Oberleiter pattern both disclaimed and expected | internal-contradiction | minor | no (minor) |
| PREDICTIONS-12 | CMB lensing dismissal contradicted by own results | internal-contradiction | minor | no (minor; fix in next CMB version) |
| PREDICTIONS-14 | DFA α ≈ 1 called critical | inconsistency | minor | no (minor) |
| PREDICTIONS-15 | "Most distinctive prediction" ranked two ways | internal-contradiction | minor | no (minor) |
| PREDICTIONS-16 | Class 4 commitment "predating" a program Table 3 dates earlier | internal-contradiction | minor | no (minor) |
| PREDICTIONS-17 | Prediction 1 observable global vs lesioned hemisphere | internal-contradiction | minor | no (minor) |
| PREDICTIONS-18 | Prediction 2 derivation names Principle 3 alone | internal-contradiction | minor | no (minor) |
| PREDICTIONS-19 | Master credits companion with removed sections | mutual-contradiction | minor | no (minor) |
| PREDICTIONS-20 | Companion ordinals not renumbered | internal-contradiction | minor | no (minor) |
| PREDICTIONS-21 | Companion mislabels delay D as decodability | internal-contradiction | minor | no (minor) |
| PREDICTIONS-22 | Transfer-probe chance level 0.8 unexplained | inconsistency | minor | no (minor) |
| PREDICTIONS-23 | Formalization asserts a semidirect-product prediction absent from master | mutual-contradiction | minor | no (minor) |
| PREDICTIONS-24 | Formalization: validation "will be reported" yet cited | internal-contradiction | minor | no (minor) |
| PREDICTIONS-25 | Stale §8.x references after S341 renumbering | bad-citation | minor | no (minor) |
| PREDICTIONS-26 | Claim graph carries Predictions 1–5 only | inconsistency | minor | no (minor) |
| PREDICTIONS-27 | Theory map: fifteen theories, nineteen rows | inconsistency | minor | no (minor) |
| PREDICTIONS-28 | Theory map: REBUS makes no anosognosia prediction | mutual-contradiction | minor | no (minor) |
| PREDICTIONS-29 | JCS: two consequences announced, three given | internal-contradiction | minor | no (minor) |
| PREDICTIONS-30 | Falsity study powered for HR 0.6, not for its refutation condition | internal-contradiction | minor | no (minor) |
| PREDICTIONS-31 | JAIC: uninstantiated design called an existence proof | internal-contradiction | minor | no (minor) |
| PREDICTIONS-32 | eNeuro: FMT "recently formalised" | inconsistency | minor | no (minor) |
| PREDICTIONS-33 | SB-HC4A: §8 predictions said to target free modelling | bad-citation | minor | no (minor) |
| PREDICTIONS-34 | SB-HC4A: "large angular scales (ℓ < 1500)" | inconsistency | minor | no (minor) |
| PREDICTIONS-35 | SB-HC4A: "no exact replay" on a reversible finite substrate | internal-contradiction | minor | no (minor) |
| PREDICTIONS-36 | SB-HC4A formalization: CPT alternation "strong prediction" | internal-contradiction | minor | no (minor) |
| PREDICTIONS-37 | SB-HC4A formalization: O(1) bits per atom vs 0.36 bits per Planck area | mutual-contradiction | minor | no (minor) |
| PREDICTIONS-38 | SB-HC4A formalization: bit-to-joule arithmetic, BH information | internal-contradiction | minor | no (minor) |
| PREDICTIONS-39 | SB-HC4A formalization: "Theorem" on a false dichotomy | internal-contradiction | minor | no (minor) |
| PREDICTIONS-40 | CMB: e^(−2N) suppression unsourced | bad-citation | minor | no (minor) |
| CITATIONS-5 | CMB self-cites SB-HC4A under a wrong title | bad-citation | minor | no (minor) |
| CITATIONS-6 | Cosmology preprint cited by superseded v2 DOI | bad-citation | minor | no (minor) |
| CITATIONS-7 | Version vs concept DOIs used inconsistently | mutual-contradiction | minor | no (minor) |
| CITATIONS-8 | Stale "v19" labels | inconsistency | minor | no (minor) |
| CITATIONS-9 | Master section numbers stale in drafts | bad-citation | minor | no (minor) |
| CITATIONS-10 | SB-HC4A cites §3.7 for a §3.8 point | bad-citation | minor | no (minor) |
| CITATIONS-11 | SB-HC4A cites a formalization missing from its list | bad-citation | minor | no (minor) |
| CITATIONS-12 | Formalization cites §9 for a §10.3 limitation | bad-citation | minor | no (minor) |
| CITATIONS-13 | Mukhametov 1977 cited for a criticality asymmetry | bad-citation | minor | no (minor) |
| CITATIONS-14 | New York Declaration in-text key without a matching reference | inconsistency | minor | no (minor) |
| CITATIONS-15 | Butlin et al. TiCS entry: year, volume, authors | bad-citation | minor | no (minor) |
| CITATIONS-16 | Toker 2022 cited for sleep and dreaming | bad-citation | minor | no (minor) |
| CITATIONS-17 | CMB: SOC threshold misattributed; Broadbridge as preprint | bad-citation | minor | no (minor) |
| CITATIONS-18 | Companion cites the published master as "Manuscript" | inconsistency | minor | no (minor) |
| CITATIONS-19 | Falsity: Thagard 1998a does not mention Palmer | bad-citation | minor | no (minor) |
| CITATIONS-20 | Falsity: four cases vs three; Wegener and Bradley dates | internal-contradiction | minor | no (minor) |
| CITATIONS-21 | Robot plea: incomplete reference entries | bad-citation | minor | no (minor) |
| CITATIONS-22 | eNeuro: Katlowitz "advance online publication" | bad-citation | minor | no (minor) |
| CITATIONS-23 | JAIC: Baltieri & Kanai via unregistered PsyArXiv DOI | bad-citation | minor | no (minor) |
| CITATIONS-24 | SB-HC4A formalization: wrong Dong 2016; missing references | bad-citation | minor | no (minor) |
| CITATIONS-26 | Formalization: Smithe key mismatch; Wolfram uncited | inconsistency | minor | no (minor) |
| CITATIONS-27 | Intelligence paper: "formalized" in master | contradicts-master | minor | no (minor) |
| CITATIONS-28 | RIM formalization: uncited references; ISBN note | inconsistency | minor | no (minor) |
| CITATIONS-29 | Permeability paper: ConCrit attributed to Priesemann; no FMT reference | bad-citation | minor | no (minor) |
| CITATIONS-30 | JCS: Tononi 2004 cited for the axioms | mutual-contradiction | minor | no (minor) |
| CITATIONS-33 | PLR title escape; SB-HC4A duplicated clause | inconsistency | minor | no (minor) |

## Claim-changing findings

### SUFFICIENCY-1 — Master makes the criticality signatures the thing that satisfies the Class 4 commitment
- **Kind:** internal-contradiction. **Published → new version now:** yes (master, in v20 already).
- **Locations:** paper/full/four-model-theory-full.md:489, :483, :448, :176, :522
- **Evidence:** :489 reads "The theory's Class 4 commitment is satisfied by the convergence of σ, α, and avalanche scaling — not by PCI" and "an artificial system realizing the Class 4 regime would satisfy the theory's computational threshold". :483 says "the requirement translates to three convergent measurable signatures". Against these, :448 says "Criticality is neither ... Criticality data therefore cannot disconfirm the theory in either direction", :522 says "a signature it may leave, not a condition of it", and :176 says "a conscious system may run subcritically". :489 is the banned reverse form (prediction-framing.md:41).
- **Fix:** :489 → "The theory's Class 4 commitment concerns free modeling; in cortex its usual signature is the convergence of σ, α and avalanche scaling, and PCI is not part of that signature." :483: "the requirement translates to" → "the requirement usually shows as"; "The theory's commitment is therefore to the *convergence*" → "The signature claim is therefore the *convergence*".

### SUFFICIENCY-2 — PP comparison names criticality as a determinant of which systems are conscious
- **Kind:** internal-contradiction. **Published → new version now:** yes (master).
- **Locations:** paper/full/four-model-theory-full.md:871, :448, :176
- **Evidence:** :871 says "the explicit self-model, self-referential closure, and criticality that determine *which* inferential systems are conscious". This contradicts :176 and :448 and the ban at prediction-framing.md:41.
- **Fix:** :871: replace "and criticality" with "and free modeling".

### SUFFICIENCY-11 — FMT formalization uses criticality as a qualifying constraint and as a condition of the closure argument
- **Kind:** internal-contradiction. **Published → new version now:** yes (FMT formalization).
- **Locations:** paper/fmt_formal/fmt-formalization.md:261, :437, :303, :277, :315
- **Evidence:** :261 says "any dynamical system satisfying the criticality and architectural constraints qualifies". :437 says "A self-referential simulation at criticality has no such outside". The same file says at :277 "its usual signature in neural tissue, not as a requirement" and at :315 "its signature, not as a requirement for consciousness". The master says the same at :176/:448. :303 is already hedged by :309.
- **Fix:** :261 → "satisfying the free-modeling and architectural constraints"; :437 → "A self-referential simulation has no such outside". :303 is optional: "fall outside the signature band the theory associates with free modeling in cortex".

### SUFFICIENCY-12 — "Minimum sufficient set for human-level consciousness" contradicts the master's "necessary but not sufficient"
- **Kind:** contradicts-master. **Published → new version now:** yes (FMT formalization, RIM formalization); companion: MG to confirm.
- **Locations:** paper/fmt_formal/fmt-formalization.md:15, :98, :626, :331; paper/rim_formal/rim-formalization.md:15; drafts/companion-computational-paper-draft.md:77; .claude/knowledge/fmt-misconception-registry.md:13; paper/full/four-model-theory-full.md:525, :17
- **Evidence:** All six places say "minimum sufficient set" or "minimum sufficient configuration". The master never uses the phrase. :17 says "a minimum the architecture forces", and :525 says "the four-model architecture is necessary but not sufficient. What is sufficient is a conjunction ...". The older master (`.prefold.bak:225`) did have the phrase, so the master retired it and these files kept it. It also survives in frozen submissions: paper/trimmed/noc/four-model-theory-noc.md:131, paper/trimmed/noc/paper.tex:186, paper/cc/four-model-theory-cc.md:129, paper/aice/aice-draft-paper-anon.tex:68.
- **Fix (corrected):** In the six listed places, replace it with "the minimum set of model kinds the architecture forces, not an exhaustive enumeration". The registry line is a cfg knowledge file and needs Meta-Rules consent. After fmt-formalization.md:335 add: "The parent theory's sufficient condition is the conjunction of §3.7.3 — the four models under closure, free modeling, embodiment and at least one pain-pleasure axis; this paper formalizes only the two necessary thresholds." Correct the NoC, CC and AICE copies only in future versions.

### SUFFICIENCY-13 — Published companion cites §3.7.3 for "jointly sufficient", which §3.7.3 denies
- **Kind:** bad-citation. **Published → new version now:** the companion has a Zenodo deposit (concept 10.5281/zenodo.21610993) but is not on MG's S342 list. MG to decide; if it counts as published, yes.
- **Locations:** drafts/companion-computational-paper-draft.md:81; paper/full/four-model-theory-full.md:525
- **Evidence:** Companion :81 says "Free modelling and the four-model architecture are separately necessary and jointly sufficient (Gruber, 2026e, §3.7.3)." Master :525 says each is "necessary but not sufficient", and that sufficiency needs closure, free compute, embodiment and a pain-pleasure axis.
- **Fix:** :81 → "Free modelling and the four-model architecture are separately necessary and not jointly sufficient; FMT's sufficient condition is the conjunction of the four models under closure, free compute, embodiment and at least one pain-pleasure axis (Gruber, 2026e, §3.7.3)."

### SUFFICIENCY-16 — RIM formalization turns the intelligence paper's separable cost conjecture into "cannot self-improve" / "requires" / iff
- **Kind:** mutual-contradiction. **Published → new version now:** yes (RIM formalization).
- **Locations:** paper/rim_formal/rim-formalization.md:323, :147, :343, :15; paper/intelligence/paper.md:279, :289, :291, :455
- **Evidence:** RIM formal :323 says "AI systems without consciousness-grounded motivation cannot self-improve". :147 says "Motivation requires consciousness". :343 says "if and only if". The source paper says at :289 "any bolt-on route pays a cost the self-model route does not, not that no such route exists", at :291 "If a system with no self-model of any kind sustains the loop, this subsection is refuted and the recursive model is untouched", and at :455 that the theory should not depend on it.
- **Fix:** :323 → "The verbal theory conjectures, separably from the recursive model (Gruber 2026a, §5.3), that self-directed compounding is not economically supplied to a system lacking an explicit self-model; FMT's conjunction decomposes that conjecture into three testable failure modes." :147 → "On that separable conjecture, motivation of the loop's kind presupposes an explicit self-model, whose conditions are FMT's conjunction." :343: change "if and only if" to "only if", and append "This is a cost claim about what a self-model-free route must pay, not a claim about what machines can never do (Gruber 2026a, §5.3)."

### SUFFICIENCY-17 — Crucible implementation spec requires criticality and states a σ-conjunct biconditional
- **Kind:** contradicts-master. **Published → new version now:** no (unpublished, crucible-owned; route via the crucible inbox).
- **Locations:** /home/jeltz/crucible/papers/fmt-implementation-spec.md:11, :92, :102, :182, :206–209, :215, :423; paper/full/four-model-theory-full.md:176, :525
- **Evidence:** :11 says "on a substrate operating at the edge of chaos"; :92 "must operate at the **edge of chaos**"; :102 "must be tunable to criticality"; :182 "### 4.2 Criticality Requirement". :206 has "Consciousness ⟺ [σ ∈ ...] ∧ ...", and :215 "Self-model + no criticality = ... simulation can't run". There is no S329 note in the file. This contradicts master :176/:525, prediction-framing.md:41, and the CRU-203 result (:45).
- **Fix:** P1 (:92) → "The substrate must support open-ended (Class 4-capable) computation and recruit it for self-modelling (free modelling); near-criticality (σ≈1, λ≈0, α) is a signature to monitor, not a setpoint to enforce". Retitle §4.2 "Free-modelling capability (criticality as readout)". At :206/:423, replace the σ conjunct with free modelling, and replace ⟺ with ⟸ (jointly with embodiment and ≥1 pain-pleasure axis). :215 → "Self-model + no free modelling = correct architecture, simulation can't run (anesthetized brain; in cortex the loss usually shows as subcriticality)". :11 → "on a substrate running free modelling".

### SUFFICIENCY-18 — Cosmology papers define Class 4 biconditionally with self-organized criticality
- **Kind:** internal-contradiction. **Published → new version now:** yes (SB-HC4A, SB-HC4A formalization).
- **Locations:** paper/cosmology_formal/sb-hc4a-formalization.md:636, :134, :136, :95, :589; paper/cosmology/sb-hc4a.md:659, :144, :402; paper/full/four-model-theory-full.md:529
- **Evidence:** Formalization :636 (Axiom A3) is "∀x [C4(x) ↔ (U(x) ∧ SOC(x) ∧ ∀k≤4 Contains(x, k))]". :134 says "capable of sustaining criticality", and :136 says brains are Class 4 subsystems. sb-hc4a :659 (Axiom 3(b)) and :144 say Class 4 "self-maintains criticality". Against this, sb-hc4a :402 says "neither a specific σ nor a specific λ_max is required", formalization :95 says the signature is "not a value the system must hit", and master :529 says universal computation has no criticality condition. Taken together, these lines would rule out a subcritical conscious system.
- **Fix:** Formalization :636 → "∀x [C4(x) ↔ (U(x) ∧ Irr(x) ∧ ∀k≤4 Contains(x, k))]", with SOC moved to a separate statement "C4(x) → typically SOC(x) in self-organizing physical substrates". :134 → "capable of sustaining open-ended computation". sb-hc4a :659 (b) → "is self-maintaining, in physical substrates typically through self-organized criticality". :144 → "It self-maintains its regime; in self-organizing systems this typically shows as criticality".

### SUFFICIENCY-19 — Record-equals-run argument reduces FMT's sufficient conjunction to architecture
- **Kind:** contradicts-master. **Published → new version now:** yes (No Outside, Worm), once MG has decided.
- **Locations:** drafts/zenodo-ready/nooutside/no-outside-draft-v1.0.md:1046, :1048, :1082; drafts/papers-s339/worm-on-the-disk.md:68, :90, :94, :162, :172; paper/full/four-model-theory-full.md:529, :531
- **Evidence:** Book :1046 says "the architecture is present in the record wherever it is present in the run", and :1048 says "what the architecture names is structure". :1082 says the states "need not have been computed there". Worm :90 lists free modelling, embodiment and the axis but never comes back to them, and :68 says the decoder "never computes one state from another". Master :531 says a substrate "must *actually perform* it ... this is what answers the abstract-universality objection". So the argument that FMT does not decide the split never addresses the one FMT clause that seems to speak to actual unfolding.
- **Fix:** Add one paragraph after worm :90 and after book :1046 that treats the three non-architectural conjuncts as realized relations. Free modelling is the trajectory's internal dependency generated by an open-ended rule; §3.7.3's "must actually perform it" is read as realized trajectory with internal dependency, and that is the leg the two horns divide over. Embodiment is the body content in the world-model. The axis is valence states in the self-model. **MG decision:** if "actually perform" is to stay a process condition in the master, book :1046 must instead read "Everything FMT's architecture names, and all but one leg of its free-modelling condition, is a pattern of states".

### SUFFICIENCY-23 — NoC draft's thesis is "no criticality, no consciousness"
- **Kind:** contradicts-master. **Published → new version now:** no (unpublished; header says "Do not submit").
- **Locations:** drafts/aiw130-noc-draft.md:15, :27, :49, :67, :73, :91, :113, :123, :131, :277, :283; drafts/aiw130-jaic-draft.md:84; paper/full/four-model-theory-full.md:176, :448
- **Evidence:** :27 says "no criticality, no consciousness". :73 says "the cortex must be near-critical". :91 makes off-critical consciousness the disconfirmer. :123 scopes the necessity to biology, which is exactly the S329-retired form (prediction-framing.md:34–41). :277's Figure 1 is titled "Criticality is necessary for consciousness". Its sibling JAIC :84 says criticality "is neither necessary nor sufficient". The draft is v2 (2026-07-30) and predates S329. Backlog AIW-103 (backlog.md:267) already flags it.
- **Fix:** Rewrite the whole thesis before AIW-103 submission. Free modelling is the necessary condition, and near-criticality is its usual cortical signature. Replace the §4 disconfirmer (:91) with the master's Table 1b lookup test plus the one-way prediction "abolish free modelling → usually subcritical". Retitle Fig. 1 "Free modelling is necessary; near-criticality is its usual cortical signature". Drop "requires criticality" from the Fig. 2 caption and drop the biological-scope necessity at :123.

### SUFFICIENCY-24 — NoC draft confines open-ended computation to the edge of chaos
- **Kind:** mutual-contradiction. **Published → new version now:** no (unpublished).
- **Locations:** drafts/aiw130-noc-draft.md:47, :49; paper/full/four-model-theory-full.md:450; drafts/aiw130-jaic-draft.md:64; drafts/companion-computational-paper-draft.md:107
- **Evidence:** NoC :47 says "supported at — and in the relevant limit confined to — the edge of chaos", and :49 says "only near the edge of chaos". Master :450 says "General computation does not need a near-critical operating point ... co-peak in the driven-stable, *ordered* regime". JAIC :64 and companion :107 agree with the master.
- **Fix:** Delete "and in the relevant limit confined to" and "only near the edge of chaos", and state "The edge of chaos is one place a dynamical medium supports open-ended computation, not the only one (Gruber 2026b; §3.7); in cortex the capability usually shows as near-critical dynamics." This belongs to the SUFFICIENCY-23 rewrite.

### SUFFICIENCY-28 — Olinyk/CRC convergence draft places FMT's threshold "at criticality"
- **Kind:** contradicts-master. **Published → new version now:** no (unpublished, pre-S329).
- **Locations:** drafts/aiw120-olinyk-crc-fmt-convergence.md:102, :154, :161, :186, :195; paper/full/four-model-theory-full.md:176, :448
- **Evidence:** :102–104 says "inside a substrate held at **criticality**". :154 says "FMT's criticality is *dynamical*". :186–187 says "implementing the architecture at criticality should produce genuine consciousness". :195–196 says "closure at (or near) criticality as a necessary condition".
- **Fix:** Replace each "at criticality" (:102, :186, :195) with "with free modelling — open-ended computation recruited for self-modelling, whose usual cortical signature is near-criticality". At :154–162, reframe the threshold as computational. :195 → "closure plus open-ended computation as necessary conditions". Add a header note that the draft predates S329.

### PHENOMENAL-1 — Master keeps pre-S341 "explicit = phenomenal" wording in Table 1, §3.2 and §3.6
- **Kind:** internal-contradiction. **Published → new version now:** yes (master; lands in v21, AIW-302).
- **Locations:** paper/full/four-model-theory-full.md:172, :178, :224, :226, :244, :371, :411; against :15, :216, :256, :387; docs/decisions.md:18
- **Evidence:** :172 (Table 1) says "Virtual, transient, phenomenal". :178 defines "becomes conscious" as content "entering what the running simulation currently represents", and :411 repeats that criterion. :224 says "the conscious world", and :371 says "Within the EWM/ESM, experience has genuine phenomenal character". The S341 lines say otherwise: :15 "phenomenal when they enter the self-model's closed loop"; :256 "explicit content outside that loop is preconscious"; :387 accessible content in an explicit model outside the loop "is not conscious". :178 and :411 are definitions.
- **Fix:** :172 → "Virtual, transient, phenomenal when in the self-model's closed loop (Section 3.4.6) — generated electrochemical activity patterns ...". :178 → "Content entering the closed loop of self-model and world-model: drawn from the implicit side by a permeability event (Section 3.6), or taken up from an explicit model held outside the loop (Section 3.4.6)." :224 → "is the simulated world, conscious where its content enters the self-model's closed loop". :226: add "in the closed loop". :411 → "Implicit content becomes conscious when it enters the closed loop within what the running simulation currently represents". :371 → "Within the closed loop of the EWM/ESM, experience has genuine phenomenal character." Fig. 2 caption → "the virtual world, phenomenal in the closed loop". Mirror all of these in the .tex.

### PHENOMENAL-2 — Formalization, RIM formalization and crucible spec equate ν > ν_crit with phenomenal
- **Kind:** contradicts-master. **Published → new version now:** yes (FMT formalization, RIM formalization), citing v21 once it is deposited.
- **Locations:** paper/fmt_formal/fmt-formalization.md:58, :60, :79, :82, :245–247, :459, :527; paper/rim_formal/rim-formalization.md:110, :119; /home/jeltz/crucible/papers/fmt-implementation-spec.md:11, :42, :44, :49, :80, :233; paper/full/four-model-theory-full.md:256, :387
- **Evidence:** Formalization :60 says "a threshold ν_crit above which modeling activity is phenomenal", :79 "Virtual (phenomenal): ν > ν_crit", and :82 "Everything above ν_crit is part of the conscious simulation". RIM :110 and :119 say the same. Spec :80 says "ν > ν_crit is conscious", and :42 says the EWM "IS the conscious perception of the world" (the finding cited :44; the quote is at :42). These lines matched v20 and became wrong with S341 (master :256, :387). They also make the §6.4 fixed point (:484) redundant for phenomenality.
- **Fix (corrected):** :58 → "fully explicit (1)". :60 → "explicit (virtual); it is phenomenal where it also enters the closed loop of §6.4". :79 → "Virtual (explicit)". :82 → "part of the running simulation and is conscious where it enters the self-model's closed loop (§6.4)". At :245–247, define C(t) over the closed-loop component and keep a separate E(t) for total explicit content. :527 → "explicit-model states". Make the same two edits at RIM :110 and :119. For the crucible spec (:11, :42, :44, :49, :80, :233), file an inbox item.

### PHENOMENAL-3 — Drafts state "explicit models are phenomenal" without the S341 closed-loop qualifier
- **Kind:** contradicts-master. **Published → new version now:** yes (No Outside, JCS carve); companion: MG to confirm; the others are unpublished.
- **Locations:** drafts/companion-computational-paper-draft.md:59, :77; drafts/zenodo-ready/nooutside/no-outside-draft-v1.0.md:569 (and :573, which copies master :411); drafts/zenodo-ready/jcs/jcs-fmt-carve.md:46 (vs :110); drafts/aiw130-noc-draft.md:39; drafts/papers-moc7/minimal-self.md:65; drafts/aiw105-qualia-privacy-paper-draft.md:45; drafts/aiw120-olinyk-crc-fmt-convergence.md:101; drafts/papers-moc7/deriving-the-fmt-definition.md:163, :240; paper/full/four-model-theory-full.md:15, :256
- **Evidence:** The strongest cases are No Outside :569 ("on the theory they are what experience is") and deriving :240 ("There is no phenomenal content outside the explicit models"). Both make the explicit models sufficient for experience. JCS :46 is weak, because JCS :110 already has the loop qualifier.
- **Fix:** One-phrase edits:
  - companion :59 → "phenomenal in the self-model's closed loop"; :77 → "phenomenal where they enter the self-model's closed loop".
  - No Outside :569 → "experience is their content where it enters the closed loop of self-model and world-model (§3.4.6)". :573 follows the PHENOMENAL-1 fix.
  - JCS :46 → "(phenomenal character in the closed loop, unity, perspective)".
  - NoC :39, minimal-self :65, aiw105 :45 and aiw120 :101: add "where they enter the self-model's closed loop" or "in the closed loop".
  - deriving :163 → "the explicit models running in the closed loop"; :240 → "There is no phenomenal content outside the explicit models, and none outside the closed loop within them."

### PHENOMENAL-4 — deriving-the-fmt-definition quotes the master with the sentence S341 retired
- **Kind:** bad-citation. **Published → new version now:** no (unpublished).
- **Locations:** drafts/papers-moc7/deriving-the-fmt-definition.md:236; paper/full/four-model-theory-full.md:387; docs/decisions.md:18
- **Evidence:** :236 quotes "the explicit models (EWM, ESM) *are* phenomenal experience". That phrase has 0 hits in the master source. Master :387 now reads "explicit content that enters the closed loop of self-model and world-model *is* phenomenal experience".
- **Fix:** Replace the second quotation with the :387 wording (Sections 3.4.2 and 3.4.6) and cite v21 once it is published.

### PHENOMENAL-5 — Theory-map paper says accessible content "stays on the implicit side"
- **Kind:** contradicts-master. **Published → new version now:** no (unpublished).
- **Locations:** drafts/papers-moc7/theory-map-paper.md:77; paper/full/four-model-theory-full.md:387; docs/decisions.md:175
- **Evidence:** :77 says accessible content "is preconscious and stays on the implicit side". Master :387 says it may also be held in an explicit model outside the loop. decisions.md:175 marks the implicit-only reading as superseded at S341.
- **Fix:** :77 → "is preconscious: it is stored on the implicit side or held in an explicit model outside the self-model's closed loop, and it becomes conscious on entering that loop (§3.4.6; Dehaene et al., 2006)".

### PHENOMENAL-6 — JAIC draft defines closure one-way in prose and Check 2, but Box 1 requires mutual dependence
- **Kind:** internal-contradiction. **Published → new version now:** no (unpublished).
- **Locations:** drafts/aiw130-jaic-draft.md:10, :24, :62, :80, :104, :110, :120, :122, :194, :200; paper/full/four-model-theory-full.md:138, :201
- **Evidence:** In the prose (:10, :24, :62, :200), the self-model enters the world-model's update. Check 2 (:80) intervenes only on σ and reads only Δ_W/L_W. Box 1 (:104, :110) requires the mutual (i)∧(ii) and calls the one-way arrow "ordinary causal coupling". κ (:120–122) is a sup over Δ_W only, yet the draft claims "κ vanishes exactly when closure is absent". On Box 1's own definition that claim is false. Master :138 and :201 require mutual entry.
- **Fix (corrected):** Make the definition mutual at :10, :24, :62 and :200. Add the symmetric intervention do(w:=u) with readout Δ_S/L_S to Check 2. Define κ as the minimum of the two sups, or reword :122 to "κ vanishes when condition (i) fails". Add a failure clause at :194 for self-transitions that do not change under world interventions.

### PHENOMENAL-7 — JAIC and Olinyk drafts say FMT "dissolves" the Hard Problem
- **Kind:** contradicts-master. **Published → new version now:** no (unpublished).
- **Locations:** drafts/aiw130-jaic-draft.md:192; drafts/aiw120-olinyk-crc-fmt-convergence.md:136; paper/full/four-model-theory-full.md:339, :343, :347, :853
- **Evidence:** JAIC :192 says "FMT dissolves rather than solves the hard problem ... no further fact", and Olinyk :136 says "Both dissolve rather than solve". The master says the problem is "not dissolved; it is **transformed**" (:339), that the identity is argued for by inference to the best explanation (:343), and it rates its own account partial (◐, :853).
- **Fix:** JAIC :192 → "FMT transforms rather than solves the hard problem: qualia are level-constitutive properties of the running self-simulation, real at the computational level and absent from the substrate; that closure constitutes phenomenality is the theory's single bridging commitment, argued for by inference to the best explanation and not derived (Gruber, 2026a, §3.4.3)." Olinyk :136 → "Both reframe rather than solve the Hard Problem, FMT rating its own treatment partial (◐)".

### PHENOMENAL-8 — Olinyk draft calls FMT "deflationary" about qualia
- **Kind:** contradicts-master. **Published → new version now:** no (unpublished).
- **Locations:** drafts/aiw120-olinyk-crc-fmt-convergence.md:25, :107–108, :136, :62; paper/full/four-model-theory-full.md:371, :373
- **Evidence:** The draft calls FMT deflationary at :25, :108 and :136. Master :371 says FMT is not compatible with deflationary accounts, and :373 commits to computational-level realism. Draft :62 says CRC itself is deflationary, so this is a divergence, not a convergence.
- **Fix (corrected):** Replace "deflationary" at :25, :108 and :136 with "level-relative realist about qualia (real at the computational level, absent from the substrate)". Turn the :136 convergence heading into a stated divergence from CRC.

### PHENOMENAL-9 — Olinyk draft attributes to FMT a spontaneous-first-person-report criterion the master declines
- **Kind:** contradicts-master. **Published → new version now:** no (unpublished).
- **Locations:** drafts/aiw120-olinyk-crc-fmt-convergence.md:186–188; paper/full/four-model-theory-full.md:343, :345
- **Evidence:** The draft gives spontaneous first-person report as the strongest evidence. Master :343 declines that criterion, and :345 adopts naturalistic label acquisition under a disconnection control instead. The same sentence also uses "at criticality" as a condition.
- **Fix:** :187 → "... and that a naturalistically acquired self-label that stays attached to the self under efferent disconnection of the self region would be the strongest available evidence (Gruber, 2026a, §3.4.3)". Drop "at criticality".

### PHENOMENAL-10 — minimal-self draft claims published FMT has no floor below basic consciousness
- **Kind:** contradicts-master. **Published → new version now:** no (unpublished).
- **Locations:** drafts/papers-moc7/minimal-self.md:73, :67; paper/full/four-model-theory-full.md:393, :395, :869
- **Evidence:** :73 says "The published statement of FMT (Gruber 2026, §3.5) does not yet place such a floor below the basic level, so this layer is the author's proposal", and :67 calls basic consciousness "the entry level". The master has made minimal consciousness the floor since v19 (:393–395). The file was last changed in ed90c0d5 (2026-10-16), before v19 was finalized.
- **Fix (corrected):** :73 → "Beneath the basic ESM, FMT places a floor of minimal consciousness (Gruber 2026, §3.5): a rudimentary closure ...", and delete "so this layer is the author's proposal". :67 → "Above the floor of minimal consciousness, at the basic level, the system generates ...".

### PHENOMENAL-11 — Crucible spec requires recursion depth ≥ ρ₁ "for any meaningful consciousness"
- **Kind:** contradicts-master. **Published → new version now:** no (unpublished, crucible).
- **Locations:** /home/jeltz/crucible/papers/fmt-implementation-spec.md:261, :239–244; paper/full/four-model-theory-full.md:395, :397, :869, :201
- **Evidence:** Spec :261 requires depth ≥ ρ₁ for any meaningful consciousness, and its table has no minimal level. Master :395, :397 and :869 make minimal and basic consciousness phenomenal without recursion.
- **Fix:** File an inbox item to crucible. :261 → "The base case is depth μ₀ (self-model in the loop without taking itself as object): minimal and basic consciousness. Depth ≥ μ₁ is required for reportable, extended consciousness, not for consciousness as such." Add a "minimal consciousness" row above "Basic".

### ARCHITECTURE-1 — Crucible implementation spec is stale: five principles, criticality required, no free modelling
- **Kind:** contradicts-master. **Published → new version now:** no (unpublished, crucible).
- **Locations:** /home/jeltz/crucible/papers/fmt-implementation-spec.md:11, :87, :89, :92, :102, :182, :206, :423; paper/full/four-model-theory-full.md:134, :140, :176
- **Evidence:** :87 has "## 3. The Five Principles", and :89 says "derives from five principles". :92 says "must operate at the edge of chaos". :206–216 and :423 carry a σ-band conjunct in the biconditional. A grep for free model / open-ended returns 0 hits. Master :134 has three principles, and :140 lists redirection, permeability and forking as consequences.
- **Fix:** Regenerate §1, §3, §4.2, §4.4 and Appendix A from master v20. Use three principles, with redirection, permeability and forking as consequences. Replace P1 with "must have Class-4 (open-ended) capability and recruit it for its own modelling; near-criticality is a signature some substrates show, not a tuning target". Remove the σ conjunct at :206–216 and :423. :11 → "substrate capable of open-ended computation" and "explicit/phenomenal in the closed loop". Until then, add a banner: "STALE relative to FMT v20 (three principles; criticality is a signature)."

### ARCHITECTURE-2 — RIM formalization summarises Gruber 2026a with a retired definition of motivation
- **Kind:** contradicts-master. **Published → new version now:** yes (RIM formalization).
- **Locations:** paper/rim_formal/rim-formalization.md:15, :25, :123, :141, :197–199, :487; paper/intelligence/paper.md:119, :121, :382, :455
- **Evidence:** RIM formal :25 says motivation "is the explicit optimization contribution of the conscious self". :15 calls motivation a "black box". :141 makes M(t) a scalar, and :197–199 gives an SDE on M ∈ [0,1]. The cited 2026a (paper.md, DOI 10.5281/zenodo.20125095) says at :119 that motivation is "the **allocation policy over it** ... it has no ceiling to measure", and at :382 "Motivation is not a magnitude at all". "black box" and "explicit optimization" have 0 hits in paper.md.
- **Fix:** Rewrite §1.1 (:15, :25) and §3.2 (:121–143) to summarise motivation as the allocation policy over the Knowledge–Performance loop, and delete "black box". Re-type M(t) as a policy object, or state that the scalar M(t) is a deliberate simplification that departs from 2026a. State that the FMT grounding is a conjecture (2026a §7.4).

### ARCHITECTURE-3 — RIM formalization asserts gap detection is barred to implicit systems
- **Kind:** contradicts-master. **Published → new version now:** yes (RIM formalization).
- **Locations:** paper/rim_formal/rim-formalization.md:131, :125, :127, :133; paper/full/four-model-theory-full.md:615, :631; paper/intelligence/paper.md:125
- **Evidence:** :131 says "An implicit system cannot detect knowledge gaps because gap detection ... requires the explicit layer." Master :615 says "The theory claims no operation that unconscious processing is barred from", and :631 says "Stated as a barrier it is false". The EWM/ESM mapping of Wissensdrang and Handlungsdrang at :125–133 is not in paper.md:125.
- **Fix:** :131 → "Gap detection is cheap for an explicit model that holds a representation of what a complete model would look like; an implicit system reaches it only at the price of a separate model per gap (Gruber 2026b §4.2.4)." Mark the :125–133 mapping as this paper's own proposal.

### ARCHITECTURE-4 — Cosmology formalization states a Uniqueness theorem the parent paper disowns
- **Kind:** mutual-contradiction. **Published → new version now:** yes (SB-HC4A formalization).
- **Locations:** paper/cosmology_formal/sb-hc4a-formalization.md:668, :682, :610, :29; paper/cosmology/sb-hc4a.md:675, :685, :148
- **Evidence:** :668 has "**Theorem (Uniqueness).** The SB-HC4A is the unique (up to isomorphism) structure satisfying all five axioms", and :682 says "any possible physical universe must be SB-HC4A". The parent's §10.2 (:675) is titled "Necessity, Not Uniqueness", and :685 says the axioms "underdetermine the model within that class".
- **Fix:** Replace the theorem with a class-selection statement: the axioms select the architecture class, and dimension, singularity inventory and cyclic vs branching remain open. Correct :29, :610 and :682 to necessity for the class, conditional on substrate determinism (sb-hc4a §3.2), and drop "any possible physical universe must be SB-HC4A".

### ARCHITECTURE-5 — eNeuro opinion attributes to Gruber (2026) that closure is the level-setting variable
- **Kind:** contradicts-master. **Published → new version now:** no (not on the published list).
- **Locations:** paper/aiw47/aiw47-eneuro-opinion.md:22, :47; paper/full/four-model-theory-full.md:138, :393, :405, :913
- **Evidence:** :22 says closure is "the level-setting variable", and describes it as the capacity to model itself as a modeller, which is recursion depth. Master :393 makes closure a binary gate and grades level by richness and recursion depth, and :913 calls closure "a single binary criterion".
- **Fix:** :22 → "Gruber (2026) makes closure the criterion for phenomenality at all and grades the level above it by richness of content and depth of recursive self-modelling". Present metacognitive sensitivity as an index of recursion depth. Table :47 → "recursion depth above closure, given free modelling".

### ARCHITECTURE-6 — Robot plea defines FMT consciousness as a capacity
- **Kind:** contradicts-master. **Published → new version now:** yes (robot plea).
- **Locations:** drafts/zenodo-ready/robot/robot-consciousness-plea.md:26; paper/full/four-model-theory-full.md:144
- **Evidence:** The plea says FMT "defines consciousness as the capacity of a system to create a model of itself, relate to it and interact with it". Master :144 (S334, in v20) defines it as "the ongoing process", names the capacity separately, and gives the deep-sleep counterexample. On the plea's wording, a dormant robot that has the capacity would count as conscious.
- **Fix:** :26 → "The Four-Model Theory defines consciousness as the ongoing process in which a system runs a model of itself, relates that model to itself and interacts with it; the capacity for that process is named separately (Gruber, 2026a, §3.1)."

### ARCHITECTURE-7 — Unqualified "explicit models are phenomenal" survives in master Table 1 and three downstream texts
- **Kind:** contradicts-master. **Published → new version now:** yes (master, v21); companion: MG to confirm.
- **Locations:** paper/full/four-model-theory-full.md:172 (vs :15, :216, :387); drafts/papers-moc7/minimal-self.md:65; drafts/companion-computational-paper-draft.md:77; /home/jeltz/crucible/papers/fmt-implementation-spec.md:11; docs/decisions.md:18
- **Evidence:** Table 1 :172 says "Virtual, transient, phenomenal" without qualification. Commit 37faa8e2 (S341) qualified :15 and :216, and decisions.md:18 says "All copies now". This overlaps PHENOMENAL-1 and PHENOMENAL-3.
- **Fix (corrected):** Master :172 (and its .tex twin) → "Virtual, transient, phenomenal in the self-model's closed loop — ...". minimal-self :65 → "and their content is phenomenal when it enters the self-model's closed loop". Companion :77 → "(generated, transient, phenomenal in the closed loop)". Spec :11 → "explicit/phenomenal in the closed loop". Check that the v21 / AIW-302 batch covers :172.

### ARCHITECTURE-8 — Formalization papers call the four model kinds a "minimum sufficient set for human-level consciousness"
- **Kind:** contradicts-master. **Published → new version now:** yes (FMT formalization, RIM formalization); companion: MG to confirm.
- **Locations:** paper/fmt_formal/fmt-formalization.md:15, :37, :90, :100, :331; paper/rim_formal/rim-formalization.md:15; drafts/companion-computational-paper-draft.md:77; paper/full/four-model-theory-full.md:228, :236, :395, :525
- **Evidence:** fmt-formal :15 says "a *minimum sufficient set* for human-level consciousness", :37 "required for human-level consciousness", and :90 and :331 "of the human type". Master :228 says the four are the floor for any consciousness, :236 says three are not enough, and :525 gives the sufficient conjunction. Minimal consciousness in fish and insects (:395, :789) still has all four.
- **Fix:** Replace "minimum sufficient set" with "minimum necessary set" (sufficiency is the §3.7.3 conjunction) at fmt-formal :15, RIM :15 and companion :77. Drop the human-level restriction at :15, :37, :90, :100 and §4.5 (:331), or state that four-corner mass is required for any consciousness, with the thresholds lowest at the minimal floor. This overlaps SUFFICIENCY-12.

### PREDICTIONS-1 — Master cites Boly et al. (2012) for a thalamocortical breakdown the paper did not find
- **Kind:** bad-citation. **Published → new version now:** yes (master, in v20). Same defect as CITATIONS-1.
- **Locations:** paper/full/four-model-theory-full.md:440, :767, :1258
- **Evidence:** :440 says "The breakdown of thalamocortical effective connectivity under propofol reported by Boly et al. (2012) is then the expected signature". The Boly 2012 abstract (doi 10.1523/JNEUROSCI.3769-11.2012) says: "loss of consciousness per se was accompanied by a decrease in backward corticocortical connectivity from frontal to parietal cortices, while thalamocortical connectivity remained unchanged." The citation carries §3.6.1's "predicted rather than accommodated" claim. The use at :708 (absence of report) is fine.
- **Fix (corrected):** At :440 and :767 (and the .tex), state what Boly 2012 found: frontoparietal backward corticocortical connectivity fails while thalamocortical connectivity is preserved. Then either restate the realizer candidate as frontoparietal recurrence, or keep the thalamocortical-relay candidacy without this citation. Do not search for a replacement source unless one is verified.

### PREDICTIONS-3 — Criticality convergence is counted as support for the requirement
- **Kind:** internal-contradiction. **Published → new version now:** yes (master).
- **Locations:** paper/full/four-model-theory-full.md:448, :1142, :859, :533, :19, :477
- **Evidence:** :448 says "Criticality data therefore cannot disconfirm the theory in either direction". Yet :1142 says "provides support for the Class 4 commitment specifically", :533 "Recent empirical support for the computational prerequisite", :19 "that convergence concerns the computational requirement", and :859 "This is convergent validation". :477 has the careful form. Data that cannot disconfirm the requirement cannot confirm it either.
- **Fix (corrected):** Align :19, :533, :859 and :1142 with :477: the convergence supports the near-critical cortical signature the Class 4 commitment predicts, not the requirement. For example, :1142 → "provides support for the near-critical signature the Class 4 commitment predicts in cortex; the requirement itself is not tested by criticality data (Section 3.7)". :533 → "consistent with". :859 → "its criticality signature, derived ... in 2015". Mirror in the .tex.

### PREDICTIONS-4 — NoC draft still asserts criticality as necessary for consciousness
- **Kind:** contradicts-master. **Published → new version now:** no (unpublished).
- **Locations:** drafts/aiw130-noc-draft.md:1, :3, :53, :57, :85, :93, :105, :172, :277, :279; paper/full/four-model-theory-full.md:176, :448; .claude/knowledge/prediction-framing.md:35
- **Evidence:** :85 says "in biological brains, consciousness requires near-criticality". :93 says "criticality is necessary and not sufficient". Figure 1 (:277) is titled "Criticality is necessary for consciousness". The title at :3 already says free computation, so the title and the body disagree. Last touched at S328 (544e962a). This overlaps SUFFICIENCY-23.
- **Fix:** Rewrite §3–§4 (:53–:93), :105, :172 and the Figure 1 caption and alt text onto free modelling, and reframe the falsification section around Table 1b. Update the header at :1 to say the body is pre-S329 and must be re-based before AIW-130/AIW-103 use.

### PREDICTIONS-5 — Crucible implementation spec keeps withdrawn σ≈1 predictions
- **Kind:** contradicts-master. **Published → new version now:** no (unpublished, crucible; route via `inbox-file.sh --project crucible --type work`).
- **Locations:** /home/jeltz/crucible/papers/fmt-implementation-spec.md:11, :100, :102, :215, :346, :356, :358; paper/full/four-model-theory-full.md:448, :939, :1053; drafts/companion-computational-paper-draft.md:139, :157
- **Evidence:** :346 says coherence "should peak near σ ≈ 1". The companion found the peak at λ ≈ −0.68 and the true edge at σ ≈ 2.6 (:139, :157), and master :1053 agrees. :356 says abolition goes "by disrupting criticality"; master :939 says it goes by abolishing free modeling. :215 contradicts master :448.
- **Fix:** Add a deprecation header, or rewrite §1 :11, P1 :96–102, the table at :213–216 and §8 predictions 1, 6 and 7 onto free modelling, reporting σ and λ beside rate-matched surrogates. P1 should state the measured demand-gated peak in the ordered regime.

### PREDICTIONS-6 — Formalization defines everything above ν_crit as phenomenal, so its C(t) counts preconscious content
- **Kind:** contradicts-master. **Published → new version now:** yes (FMT formalization), after v21.
- **Locations:** paper/fmt_formal/fmt-formalization.md:79, :82, :243–249; paper/full/four-model-theory-full.md:15, :256
- **Evidence:** :79 says "Virtual (phenomenal): ν > ν_crit". :247 integrates all mass above ν_crit, and :249 predicts that this correlates with PCI. After S341, explicit content outside the loop is preconscious. This overlaps PHENOMENAL-2.
- **Fix:** Redefine ν_crit at :77–82 as the explicit/implicit boundary only, and state that phenomenality also needs the closed loop. Restrict C(t) at :243–249 to the loop's support (for example with a closure indicator χ_loop). The PCI prediction then refers to that restricted quantity. Rename or qualify "Total Conscious Content".

### PREDICTIONS-8 — RIM formalization attributes threshold, uniform-growth, no-development and binary-consciousness claims to the verbal theory
- **Kind:** mutual-contradiction. **Published → new version now:** yes (RIM formalization).
- **Locations:** paper/rim_formal/rim-formalization.md:279, :313, :434, :436, :438, :442; paper/intelligence/paper.md:185, :453, :455
- **Evidence:** RIM formal :434 says "The verbal theory predicts only that a threshold exists", :436 "predicts uniform growth", :438 "predicts 'no development'", and :442 "treats consciousness as binary". paper.md has 0 hits for threshold, ignition, binary, tipping or bifurcation. Its actual claims are at :185 (uneven loop), :453 and :455.
- **Fix:** Rewrite §9 (:432–444) and :279/:313. Present the ignition threshold and the consciousness functional as the formalization's own posits. :436 → "the verbal theory does not specify the domain structure of growth". :438 → "the verbal theory claims only that an exploration drive alone does not produce compounding (2026a, §5.2)". :442 → "the verbal theory leaves the consciousness link open (2026a, §7.4)".

### PREDICTIONS-9 — SB-HC4A formalization reads James-Stein shrinkage as a nonlocality/decoherence law and calls it admissible
- **Kind:** mutual-contradiction. **Published → new version now:** yes (SB-HC4A formalization).
- **Locations:** paper/cosmology_formal/sb-hc4a-formalization.md:363, :389, :391, :850; paper/cosmology/sb-hc4a.md:449, :451
- **Evidence:** The formalization calls the estimator "admissible" at :363, :389, :391 and :850, and reads w as quantifying nonlocality (:389) and decoherence (:391). The main paper says at :449 "Dominating, not admissible", and at :451 that w "is not read here as a scaling law for ... decoherence".
- **Fix (corrected):** Change "admissible" to "dominating" at :363, :389, :391 and :850. Recast results 1–2 at :389–391 as what a discrete Stein-type theorem would have to supply before w could be read that way. Trim the :850 summary to the qualitative claim.

### PREDICTIONS-10 — Formalization derives heat-death saturation from the Gibbons-Hawking maximum and calls it the Bekenstein bound
- **Kind:** mutual-contradiction. **Published → new version now:** yes (SB-HC4A formalization).
- **Locations:** paper/cosmology_formal/sb-hc4a-formalization.md:150, :199–203; paper/cosmology/sb-hc4a.md:206, :270, :274
- **Evidence:** Formalization :201 says heat-death entropy approaches its maximum, which "is precisely the Bekenstein bound ... Bekenstein saturation". The main paper separates the two bounds (:206), says at :270 "Heat death, as usually conceived, is not holographic saturation", and at :274 gets saturation from an emptied interior.
- **Fix:** Rename IB2 (:150) "holographic (area-law) saturation" and cite 't Hooft, Susskind and Bousso. Rewrite :199–203 to the main paper's mechanism: the interior entropy carriers vanish, and the de Sitter horizon saturates by construction.

### PREDICTIONS-11 — Formalization derives baryon and lepton number conservation that the main paper says is violated
- **Kind:** mutual-contradiction. **Published → new version now:** yes (SB-HC4A formalization).
- **Locations:** paper/cosmology_formal/sb-hc4a-formalization.md:265, :290, :850; paper/cosmology/sb-hc4a.md:336, :344, :346
- **Evidence:** Formalization :290 says baryon and lepton number conservation are "consequences of information conservation at singularity boundaries". The main paper says at :344 "Baryon and lepton number have no boundary home at all", and at :346 that it "does not derive" them and predicts they are approximate.
- **Fix:** Restrict :265 to charge and spin, and restate the :290 proposition for charge and angular momentum only. Add the main paper's prediction that B and L are approximate and violated at boundaries. Amend the :850 summary.

### PREDICTIONS-13 — Qualia-privacy draft overstates Kawakita et al. as individual-level alignment
- **Kind:** contradicts-master. **Published → new version now:** no (unpublished).
- **Locations:** drafts/aiw105-qualia-privacy-paper-draft.md:33, :80, :82, :84, :88, :96, :161; paper/full/four-model-theory-full.md:1003, :1518
- **Evidence:** :33 and :84 claim alignment "across individuals". Master :1003 and JCS :200 say the alignment was between pooled groups and that the individual-level arm is untested. :161 is a VERIFY stub that omits Takeda; master :1518 has the full reference. The draft's "Prediction 1/2/3" headings collide with the master's numbering.
- **Fix:** :33 and :84 → "between pooled groups of observers (Kawakita et al., 2025; Watanabe et al., 2026); the individual-level structural arm is untested". Complete the reference from master :1518. Rename the predictions (for example 5a/5b/5c) and say which come from §8.6 and which are new.

### CITATIONS-1 — Boly et al. (2012) says the opposite of what the master cites it for
- **Kind:** bad-citation. **Published → new version now:** yes (master, in v20). Same issue as PREDICTIONS-1.
- **Locations:** paper/full/four-model-theory-full.md:166, :440, :767, :1258
- **Evidence:** Table 1 :166 credits Boly 2012 with "breakdown of thalamocortical effective connectivity and collapse of DMN coherence". :440 and :767 say the same. The abstract reports thalamocortical connectivity unchanged and corticocortical backward connectivity reduced. It is a DCM of frontal and parietal sources and has no DMN measure. The text is in v20 (448183ed).
- **Fix (corrected):** Rewrite :166, :440 and :767 (.md and .tex) to the actual finding. At :440, make the predicted signature the loss of recurrent corticocortical (frontal-to-parietal) effective connectivity. Either drop the thalamocortical relay as the Boly-backed candidate or support it with another, verified source. Remove "collapse of DMN coherence" at :166, or give it its own citation (for example Boveroux et al., 2010). Leave :708 as it is.

### CITATIONS-2 — Formalization credits ConCrit with a 140-dataset σ/conscious-state analysis
- **Kind:** contradicts-master. **Published → new version now:** yes (FMT formalization).
- **Locations:** paper/fmt_formal/fmt-formalization.md:285, :644; paper/full/four-model-theory-full.md:474–475, :939, :1186
- **Evidence:** :285 says "The ConCrit framework (Algom & Shriki, 2026) established that σ covaries with conscious state across 140 datasets." ConCrit is a framework proposal. The 143-dataset meta-analysis is Hengen & Shew (2025), and it makes a setpoint claim. Master :939 attributes this correctly. Reference :644 gives the initial "S." (Crossref: Inbal Algom) and has no volume or DOI.
- **Fix:** :285 → "The ConCrit framework (Algom & Shriki, 2026) proposes criticality as a unifying mechanism across theories of consciousness, and Hengen and Shew's (2025) meta-analysis of 143 datasets consolidates the premise that cortex operates near criticality as a setpoint; neither establishes that σ covaries with conscious state." :644 → "Algom, I., & Shriki, O. (2026) ... 180, 106483. https://doi.org/10.1016/j.neubiorev.2025.106483". Align master Table 3 :475 "2025-26" with 2026.

### CITATIONS-3 — JCS carve pins the v20 DOI while citing a §3.4.6 correction made after v20
- **Kind:** bad-citation. **Published → new version now:** yes (JCS carve; fix before submission).
- **Locations:** drafts/zenodo-ready/jcs/jcs-fmt-carve.md:278, :110; drafts/papers-s339/jcs-fmt-carve.md:286, :118; docs/decisions.md:914
- **Evidence:** Both copies pin 10.5281/zenodo.23477765 (v20). The v20 deposit commit 448183ed (16:52) came before the correction commit 59c42324 (19:21). In v20, §3.4.6 says accessible content "is stored on the implicit side", which is the opposite of the split JCS :110 cites. The JCS prose itself matches the master source. decisions.md:914 requires concept DOIs.
- **Fix:** Either deposit v21 first and cite it, or cite the concept DOI 10.5281/zenodo.18669891 without a version in both copies. Do not leave a v20 pin against the corrected wording.

### CITATIONS-4 — CMB paper: Movahed et al. (2011) is a chimera reference and the quote is overstated
- **Kind:** bad-citation. **Published → new version now:** yes (CMB MFDFA).
- **Locations:** paper/cmb_mfdfa/cmb-mfdfa.md:387, :26, :245, :247, :257, :327
- **Evidence:** :387 cites "Movahed, Javanmardi, Kohandel, & Babar (2011) ... JSTAT P03007". The paper with this title is Movahed, Ghasemi, Rahvar & Tabar, Phys. Rev. E 84, 021103 (Crossref). :26 and :247 put "entirely driven by long-range correlations" in quotation marks, but the abstract says "mainly due to the long-range correlations".
- **Fix (corrected):** :387 → "Movahed, M. S., Ghasemi, F., Rahvar, S., & Tabar, M. R. R. (2011). Long-range correlation in cosmic microwave background radiation. *Physical Review E*, 84(2), 021103. https://doi.org/10.1103/PhysRevE.84.021103". Fix the in-text author list at :26 and the §5.1 heading at :245 if it names the authors. Change the quotation at :26 and :247 to "mainly due to the long-range correlations", use "largely attributable" at :327, and check :257. Rebuild and deposit v2.

## Minor findings

### SUFFICIENCY-3 — Seizure and σ≈0.98 passages lean on criticality as the predictor (downgraded to minor)
- **Locations:** paper/full/four-model-theory-full.md:495, :491, :1126, :479, :448
- **Evidence:** :491 defines extent through the criticality criterion, and :495 derives "consciousness is lost, exactly as the theory predicts" from it. The same line also cites the loss of the structured regime. :479 leaves out the S329 answer. :1126 is consistent with the one-way signature reading.
- **Fix (corrected):** :495 → "Hypersynchronous, low-complexity dynamics cannot host free modeling, and consciousness is lost, as the free-modeling requirement predicts; the extent measure records that loss, it does not define it." At :479, prepend "It does not: the requirement is free modeling and σ is its signature, so no value of σ falsifies it (Section 3.7)." The :1126 edit is optional.

### SUFFICIENCY-4 — §5.3 / Table 4 orders states by criticality; covert-awareness cell unsupported
- **Locations:** paper/full/four-model-theory-full.md:691, :693, :705, :448
- **Evidence:** :691 says "ordered by the substrate's position relative to [the critical point]". Table 4 (:693) is titled "Consciousness States and Criticality". The :705 cell "At critical" cites Owen 2006, an fMRI study that measured no criticality. Toker et al. (2026) was not checked.
- **Fix:** :691 → "ordered by whether free modeling and the explicit models are running; the criticality column records the usual cortical signature where it has been measured". :705 → "Not measured (Owen et al., 2006)", unless Toker 2026 reports it.

### SUFFICIENCY-5 — Criticality called "the neural effect" of Class 4 computation
- **Locations:** paper/full/four-model-theory-full.md:54, :66, :176, :448
- **Evidence:** :54 says "of which criticality is the neural effect", and :66 "whose neural effect is near-criticality". Both are unhedged.
- **Fix:** Change both to "usual neural signature".

### SUFFICIENCY-6 — Sufficient conjuncts read as necessary in the robot plea
- **Locations:** drafts/zenodo-ready/robot/robot-consciousness-plea.md:103, :105; paper/full/four-model-theory-full.md:1037, :525
- **Evidence:** Plea :103 says "suffering needs the conditions under which a system is conscious", and :105 says "Each condition is a place where suffering could be blocked". Master :525 says embodiment is not required for consciousness to exist. The master :1037 part is weak.
- **Fix (corrected):** Plea :103 → "On FMT a system meeting a sufficient conjunction is conscious (Gruber, 2026a, §3.7.3): [list]; suffering needs, in addition, that the axis takes aversive values represented in the closed self-model." :105 → "Each condition is a place where the conjunction could be left unmet, and they differ in what that costs". Under *Embodiment*, add "FMT does not make embodiment necessary for consciousness to exist (§3.7.3)." The master :1037 edit is optional.

### SUFFICIENCY-7 — "Qualitatively obvious" beside "no behavioral test is conclusive"; broken analogy
- **Locations:** paper/full/four-model-theory-full.md:1047, :1120, :1035
- **Evidence:** The :1047 analogy compares obviousness with cost, so it does not parse. :1120 says "would be apparent".
- **Fix:** Use the proposed :1047 rewrite: a difference in what the architecture must pay, which may show as the interaction lengthens. :1120: "would be apparent" → "may become apparent".

### SUFFICIENCY-8 — "Fit window" cited to §4.2.4, which never defines it
- **Locations:** paper/full/four-model-theory-full.md:1047, :611–615; drafts/zenodo-ready/robot/robot-consciousness-plea.md:57
- **Evidence:** "fit window" appears only at master :1047.
- **Fix (corrected):** Append to master :615: "Call the range of problem classes and budgets in which closure is the cheaper route the *fit window*." Alternatively, use "the cost window of Section 4.2.4" at :1047 and plea :57.

### SUFFICIENCY-9 — Corvid consciousness asserted as fact
- **Locations:** paper/full/four-model-theory-full.md:903, :643
- **Fix:** :903 → "The evidence for consciousness in corvids, whose brain architecture is non-cortical (nuclear pallium; Güntürkün & Bugnyar, 2016), favors substrate independence."

### SUFFICIENCY-10 — Convergence paragraph overstates "in the Class 4 regime"
- **Locations:** paper/full/four-model-theory-full.md:909, :607
- **Fix:** :909 → "That multiple independent frameworks converge on self-referential closure as constitutive of consciousness — one of them, RIFT, at criticality — strengthens the case ...".

### SUFFICIENCY-15 — Closure fixed point written Φ(m*)=m* after the rename to Ψ
- **Locations:** paper/rim_formal/rim-formalization.md:119; paper/fmt_formal/fmt-formalization.md:488; /home/jeltz/crucible/papers/fmt-implementation-spec.md:227, :229, :265, :382, :421, :423, :446
- **Fix (corrected):** Change Φ to Ψ at RIM :119 and at the crucible lines listed (via a crucible inbox item).

### SUFFICIENCY-20 — No Outside says FMT "does not now state" the physics dependency
- **Locations:** drafts/zenodo-ready/nooutside/no-outside-draft-v1.0.md:1095, :1048; paper/full/four-model-theory-full.md:635
- **Fix:** :1095 → "the theory takes on a dependency it already names as a conditional (Gruber, 2026a, §4.3): its architecture is necessary for experience and no longer sufficient, because it organizes an ingredient it does not describe."

### SUFFICIENCY-26 — JAIC lists PCI among the signatures of criticality
- **Locations:** drafts/aiw130-jaic-draft.md:82; paper/full/four-model-theory-full.md:489
- **Fix:** Remove PCI from the list and add "perturbational complexity (Casali et al., 2013) co-varies with these empirically but is not a criticality measure".

### SUFFICIENCY-27 — "Abolish free modelling → subcritical" stated as a law
- **Locations:** drafts/aiw130-jaic-draft.md:186; paper/full/four-model-theory-full.md:483, :708
- **Fix (corrected):** Only JAIC :186 → "... the substrate usually turns subcritical with it". Master :708 describes the propofol case and stays as written.

### SUFFICIENCY-29 — Formalization adds "continuous density of modeling activity" as a necessity
- **Locations:** paper/fmt_formal/fmt-formalization.md:75; paper/full/four-model-theory-full.md:17, :907, :525
- **Fix:** :75 → "Any biological-type implementation supports a continuous density of modeling activity; the formalization adopts the density representation for generality, not as a further necessity condition."

### PHENOMENAL-12 — Formalization defines closure as an ESM self-fixed-point and misquotes the master
- **Locations:** paper/fmt_formal/fmt-formalization.md:484, :490, :492; paper/full/four-model-theory-full.md:138, :275, :319, :395
- **Evidence:** The quote "the simulation *is* the thing being simulated" at :492 does not appear in the master. Master :319, in §3.4.3, reads "the computation *is* the thing being computed". The master's closure is the mutual EWM–ESM update.
- **Fix:** Define Ψ on the joint state (e, w) as the coupled update, with closure as its fixed point. Correct the quote to "the computation *is* the thing being computed" (§3.4.3).

### PHENOMENAL-13 — Fixed-point symbol, depth labels and the closure measure R(t) disagree across texts
- **Locations:** paper/fmt_formal/fmt-formalization.md:472, :476, :478, :488; paper/rim_formal/rim-formalization.md:119, :155; /home/jeltz/crucible/papers/fmt-implementation-spec.md:73, :227, :241–244, :423, :446
- **Fix (corrected):** RIM :119 Φ → Ψ. RIM :155: call R(t) the "self-prediction (self-knowledge) measure (§6.3), used as a proxy for the closure condition of §6.4". In the crucible spec (via inbox), change Φ to Ψ at :227, :265, :382, :421, :423 and :446, and ρₙ to μₙ at :241–244 and :261.

### PHENOMENAL-14 — Master stale cross-references
- **Locations:** paper/full/four-model-theory-full.md:442, :883, :184, :387, :389
- **Fix:** :442 → "(Sections 3.4.6, 3.5)" and "(Section 3.4.6)". :883 → "(Table 1, footnote c)".

### PHENOMENAL-15 — minimal-self uses "access" for reportability
- **Locations:** drafts/papers-moc7/minimal-self.md:69, :127; paper/full/four-model-theory-full.md:387, :389; docs/decisions.md:176 (D2c)
- **Fix:** Replace "access/accessed" with "reportable/report" at :69 and :127.

### PHENOMENAL-16 — Permeability paper glosses the explicit set as "explicit/conscious-access"
- **Locations:** paper/fmt_permeability_criticality/fmt-permeability-criticality.md:15, :27, :43, :147; paper/full/four-model-theory-full.md:387
- **Fix:** At :15 and :27, use "explicit-side (report-correlated) signals". At :43 add "The report-correlated set operationalizes accessed content, a proper subset of explicit content (Gruber 2026, §3.4.6)."

### PHENOMENAL-17 — Qualia-privacy draft: "fully dissolved"
- **Locations:** drafts/aiw105-qualia-privacy-paper-draft.md:132; paper/full/four-model-theory-full.md:339, :840, :853
- **Fix (corrected):** Change only :132: "● (fully dissolved)" → "● (fully addressed)". The quoted :144 text does not exist in the file.

### ARCHITECTURE-9 — Closure fixed point cited as Φ(m*)=m* at "Section 6.3"
- **Locations:** paper/cosmology/sb-hc4a.md:413, :493; paper/cosmology_formal/sb-hc4a-formalization.md:431, :436, :571; paper/rim_formal/rim-formalization.md:119; paper/fmt_formal/fmt-formalization.md:461, :482, :486, :488
- **Fix (corrected):** Change the citations at sb-hc4a :413 and formalization :431 to "Section 6.4". Use Ψ at sb-hc4a :413 and :493, formalization :431, :436 and :571, and RIM :119. sb-hc4a :507 is an internal reference and stays unchanged.

### ARCHITECTURE-10 — RIM calls R(t) the "self-referential closure condition"
- **Locations:** paper/rim_formal/rim-formalization.md:155; paper/fmt_formal/fmt-formalization.md:476, :478, :486
- **Fix:** :155 → "R(t) is the self-knowledge (self-prediction) measure of Gruber 2026c §6.3, used here as a graded proxy for closure; closure proper is the fixed point Ψ(m*) = m* (§6.4)."

### ARCHITECTURE-11 — RIM says C(t)=0 forces M(t)=0, but neither equation does
- **Locations:** paper/rim_formal/rim-formalization.md:157, :141, :149, :198, :199, :424
- **Fix:** Either define M(t) = C(t)·(ω_W W_d + ω_H H_d), or change :157 to "When C(t) = 0 the motivation dynamics freeze (the drift vanishes)". State that [5] and [9] are alternative definitions to be reconciled in Phase 4.

### ARCHITECTURE-12 — RIM symbol overloads
- **Locations:** paper/rim_formal/rim-formalization.md:153, :154, :164, :191, :198, :234, :246, :249
- **Fix:** Rename age decline (for example δ_age(t)) and the free-modelling proxy (σ_br). At :249, split the slow baseline from the fast perturbations described at :164.

### ARCHITECTURE-13 — RIM module numbering mismatch
- **Locations:** paper/rim_formal/rim-formalization.md:15, :406, :408, :412, :414, :418, :420
- **Fix:** Renumber §8 to match the abstract (knowledge manifold = Module 1).

### ARCHITECTURE-14 — FMT formalization module labels, missing Table 1 and Eq. [1], revision narration
- **Locations:** paper/fmt_formal/fmt-formalization.md:15, :560, :562, :566, :568, :570, :574, :182, :203
- **Fix:** Label the §8 modules (1)–(6) as in the abstract. Caption the §3.2 table "Table 1", label the §4.1 equation [1], and delete "Module 7 was originally placed in Phase 3 ...".

### ARCHITECTURE-15 — "Four nested models"
- **Locations:** paper/fmt_formal/fmt-formalization.md:15; paper/rim_formal/rim-formalization.md:41; /home/jeltz/crucible/papers/fmt-implementation-spec.md:11; paper/full/four-model-theory-full.md:209
- **Fix:** Replace with "across four model kinds along two axes — mode, an orthogonal contrast, and scope, a nesting (ESM ⊆ EWM, ISM ⊆ IWM)".

### ARCHITECTURE-16 — Master says "four models" beside its own disclaimer
- **Locations:** paper/full/four-model-theory-full.md:209, :228, :252, :525, :545, :557, :639, :657, :1035, :1037, :1039, :1045, :1071, :1073, :1097, :1124, :1136; drafts/zenodo-ready/nooutside/no-outside-draft-v1.0.md:588 (and :1179, unconfirmed)
- **Fix (corrected):** Use "four model kinds" wherever the phrase names the taxonomy, including the OQ1 heading at :1071 and the headings at :228 and :252. "The four models under closure" becomes "the four model kinds under closure". No Outside :588 follows the heading in its next version. Re-check :1179 before editing it.

### ARCHITECTURE-17 — "Two kinds of models" names different axes in different papers
- **Locations:** drafts/zenodo-ready/jcs/jcs-fmt-carve.md:24, :34; drafts/papers-s339/worm-on-the-disk.md:90; drafts/zenodo-ready/nooutside/no-outside-draft-v1.0.md:192, :957; paper/intelligence/paper.md:455; drafts/zenodo-ready/plr/plr-loops-commentary.md:40; drafts/blog-plr-loops-commentary.md:40; drafts/zenodo-ready/robot/robot-consciousness-plea.md:26; paper/aiw47/aiw47-eneuro-opinion.md:20; paper/full/four-model-theory-full.md:209, :230
- **Fix:** Use the master's terms: "four model kinds" for the cells, "two model classes (implicit, explicit)" for mode, "two scopes (world, self)" for scope. Change PLR :40, blog :40, robot :26 and No Outside :957 in their next versions.

### ARCHITECTURE-18 — Depth tables and theory map omit the minimal-consciousness floor
- **Locations:** paper/fmt_formal/fmt-formalization.md:471; /home/jeltz/crucible/papers/fmt-implementation-spec.md:241; drafts/papers-moc7/theory-map-paper.md:69; paper/full/four-model-theory-full.md:393, :395, :397
- **Fix:** Add a "Minimal consciousness" row above Basic. It shares μ₀ and differs on richness. Theory map :69 → "minimal, basic, simply, doubly and triply extended consciousness by richness and depth of recursive self-modelling".

### ARCHITECTURE-19 — Encoder relation called "transfer"; binding called a "requirement"
- **Locations:** paper/fmt_formal/fmt-formalization.md:124, :132; paper/full/four-model-theory-full.md:411, :665
- **Fix:** :124 → "maps onto the generation of the explicit model from the implicit one". :132 → "relevant to FMT's account of binding as an emergent property of the dynamics (Section 5.1 of the parent paper)".

### ARCHITECTURE-20 — "Gating" vocabulary persists after REV-1
- **Locations:** paper/fmt_permeability_criticality/fmt-permeability-criticality.md:15, :35, :62, :66; paper/fmt_formal/fmt-formalization.md:15, :184, :195, :199; docs/decisions.md:14; paper/full/four-model-theory-full.md:1089
- **Fix:** Rename gating to selection in the next versions, or record in decisions.md that REV-1 applies to the master only. MG to decide the scope.

### ARCHITECTURE-21 — Master: forking cited to §6.5, consolidation to §3.4.3
- **Locations:** paper/full/four-model-theory-full.md:140, :816, :775, :268, :867, :303, :436, :234
- **Fix:** :140 → "(Section 6.2)". :867 → "(Section 3.6.1)". Mirror in the .tex.

### ARCHITECTURE-22 — Master §8.1/§8.5 drift toward localising the explicit models
- **Locations:** paper/full/four-model-theory-full.md:987, :951, :184, :209
- **Fix (corrected):** At :987, replace "identified with" with "a candidate correlate of (Table 1, note c)", and reword "threshold crossing in the ESM's criticality state" as a signature claim. The :951 change ("functionally distinct model kinds") is optional.

### ARCHITECTURE-23 — Intelligence paper: "seven steps", six listed
- **Locations:** paper/intelligence/paper.md:43
- **Fix:** "six steps", or count §2.7 explicitly.

### ARCHITECTURE-24 — Intelligence paper: cognitive/RL distinction "formalized in Gruber (2026)"
- **Locations:** paper/intelligence/paper.md:145, :561; paper/full/four-model-theory-full.md:611, :615
- **Fix:** :145 → "developed in Gruber (2015) and in Gruber (2026, §4.2.4)". Drop "formalized". This duplicates CITATIONS-27.

### ARCHITECTURE-25 — Cosmology formalization misdescribes the five-class split
- **Locations:** paper/cosmology_formal/sb-hc4a-formalization.md:53, :89; paper/cosmology/sb-hc4a.md:33, :74, :78, :86
- **Fix:** :53 → "splitting Wolfram's Class 3 by reducibility: reducible fractals form the new Class 3, irreducible deterministic rules (Rule 30) join Class 4, and Class 5 is reserved for ontic randomness generated by no expressible rule". :89 → "Class 4 is computationally irreducible; Class 5 is non-algorithmic, a stronger condition than irreducibility".

### ARCHITECTURE-26 — Cosmology formalization derives undecidability from the fixed point in one place and denies it in another
- **Locations:** paper/cosmology_formal/sb-hc4a-formalization.md:762, :446
- **Fix:** :762 → "if U is computationally universal and embeds formal systems that have U as their subject matter (universality plus embedding, Section 5.5; not from the fixed point alone)".

### ARCHITECTURE-27 — Cosmology papers: explicit models as a "projection of selected information"
- **Locations:** paper/cosmology/sb-hc4a.md:553, :555; paper/cosmology_formal/sb-hc4a-formalization.md:572, :776; paper/full/four-model-theory-full.md:178, :411
- **Fix (corrected):** sb-hc4a :553 → "generated from the substrate as a lower-bandwidth running process, not a copy of its content". :555 → "how readily substrate knowledge is drawn into that generation". In the formalization, keep "projection" where it means a projection of the activity state (as in fmt-formalization §4.1), and reword only phrases that imply copying out of a store.

### ARCHITECTURE-29 — JCS carve calls a self-model-free sensory loop "Stage 2"
- **Locations:** drafts/zenodo-ready/jcs/jcs-fmt-carve.md:220, :60, :62; drafts/papers-s339/jcs-fmt-carve.md:228
- **Fix:** In both copies, "is a Stage 1 system: a simulation without an inside" (or "at most a Stage 2 system").

### ARCHITECTURE-30 — JAIC and eNeuro: "two orthogonal dimensions"
- **Locations:** drafts/aiw130-jaic-draft.md:58; paper/aiw47/aiw47-eneuro-opinion.md:20; paper/full/four-model-theory-full.md:209
- **Fix:** "along two dimensions — mode, an orthogonal contrast, and scope, a nesting".

### ARCHITECTURE-31 — JAIC and NoC: implicit models "in the raw dynamics of the substrate"
- **Locations:** drafts/aiw130-jaic-draft.md:58; drafts/aiw130-noc-draft.md:63; paper/full/four-model-theory-full.md:170, :230
- **Fix:** "stored in the substrate's connectivity and evaluated by substrate processing, not itself represented".

### ARCHITECTURE-32 — Olinyk: FMT rejects smooth fading and owes an account of a sharp crossing
- **Locations:** drafts/aiw120-olinyk-crc-fmt-convergence.md:121–124; paper/full/four-model-theory-full.md:393, :405; .claude/knowledge/prediction-framing.md:29
- **Fix:** Use the proposed :121–124 text. FMT shares the binary gate, grades everything above it continuously, and expects the crossing to be practically unmeasurable as a sharp transition.

### ARCHITECTURE-33 — Companion overloads σ and redefines R
- **Locations:** drafts/companion-computational-paper-draft.md:103, :107, :139, :155, :157, :159; paper/fmt_formal/fmt-formalization.md:478
- **Fix:** Use ρ_sr for spectral radius at :107, :139, :157 and :159. Rename the Pearson readout R_ISM and state that it is a correlation proxy.

### ARCHITECTURE-35 — 2015-definitions knowledge file lacks the p.243 Lernfähigkeit sentence
- **Locations:** .claude/knowledge/fmt-2015-definitions.md:153; paper/intelligence/paper.md:109; paper/rim_formal/rim-formalization.md:15
- **Evidence:** Gruber (2015) p.243 says "Und damit schließt sich der Kreis zur Intelligenz, denn diese ist Ausdruck der Lernfähigkeit. Sie wird von Wissen (explizit und implizit), Leistung (Arbeitsgedächtnis), und von Motivation bestimmt." The publications are faithful to 2015. Only the knowledge file is incomplete.
- **Fix:** Add the p.243 sentence next to the p.51 row.

### PREDICTIONS-7 — Intelligence paper both disclaims and claims the Oberleiter pattern (downgraded to minor)
- **Locations:** paper/intelligence/paper.md:185, :439
- **Fix:** :439 → "— a pattern the recursive model can accommodate through a loop engaged unevenly across content (Section 3.3); it was not predicted in advance and is not claimed as support."

### PREDICTIONS-12 — CMB lensing dismissal contradicted by the paper's own results (downgraded to minor)
- **Locations:** paper/cmb_mfdfa/cmb-mfdfa.md:309, :210, :212, :12
- **Evidence:** :309 says the signal is "concentrated at ℓ < 100". The paper's own results put the only detection at Band 6 (ℓ = 1500–2500), where lensing acts (:212).
- **Fix:** Rewrite :309 to say there is no large-scale detection to explain, and that lensing is a candidate contributor to the Band-6 excess, to be tested with lensed vs unlensed simulations. Add lensing to the candidates at :12, §5.6 and the conclusions. Bundle this with the CITATIONS-4 version.

### PREDICTIONS-14 — DFA α ≈ 1 called critical
- **Locations:** paper/fmt_formal/fmt-formalization.md:293; paper/fmt_permeability_criticality/fmt-permeability-criticality.md:84, :92, :104; /home/jeltz/crucible/papers/fmt-implementation-spec.md:100; paper/full/four-model-theory-full.md:176, :196, :483, :487
- **Fix:** Use the master's convention everywhere: "α in 0.6–0.9 (Hardstone et al., 2012) indexes long-range temporal correlations; α ≈ 0.5 uncorrelated; α > 1 non-stationary drift". The crucible spec goes via inbox.

### PREDICTIONS-15 — "Most distinctive prediction" ranked two ways
- **Locations:** paper/full/four-model-theory-full.md:1106, :1140, :973; paper/fmt_formal/fmt-formalization.md:395; .claude/knowledge/prediction-framing.md:57
- **Fix:** :1106 → "the prediction whose fine structure most sharply separates the redirectable ESM from REBUS's general input-driven updating". Formalization :395 → "one of the theory's most specific predictions".

### PREDICTIONS-16 — Class 4 commitment said to predate a program that Table 3 dates earlier
- **Locations:** paper/full/four-model-theory-full.md:941, :469, :470, :477, :58
- **Fix:** :941 → "predating the large-scale consolidation of the consciousness–criticality program (Hengen & Shew, 2025; Algom & Shriki, 2026)". This also keeps clear of the no-priority guardrail.

### PREDICTIONS-17 — Prediction 1 observable: global vs lesioned hemisphere
- **Locations:** paper/full/four-model-theory-full.md:955, :959, :961, :963; drafts/zenodo-ready/jcs/jcs-fmt-carve.md:210, :212
- **Fix:** :955 → "correlating with increases in neural complexity, most strongly over the lesioned hemisphere". At :961, add "or without a lesioned-hemisphere-specific increase". Mirror in JCS :210.

### PREDICTIONS-18 — Prediction 2 derivation names Principle 3 alone
- **Locations:** paper/full/four-model-theory-full.md:969, :722; drafts/papers-moc7/fmt-claims.json (F-FORK1)
- **Fix:** :969 → "Principles 2 and 3 → redirection ...". In fmt-claims.json, split redirection out of F-FORK1, or add F-P2/F-P3 to its depends_on.

### PREDICTIONS-19 — Master credits the companion with sections it removed
- **Locations:** paper/full/four-model-theory-full.md:1063; drafts/companion-computational-paper-draft.md:4, :6, :244
- **Fix:** :1063 → "develops the full program — the banked results, the two-closure taxonomy and the capability-first reading of criticality; the graded scaled test and the interaction prediction are reserved for a separate report".

### PREDICTIONS-20 — Companion ordinals not renumbered
- **Locations:** drafts/companion-computational-paper-draft.md:165, :248, :16; paper/full/four-model-theory-full.md:1057
- **Fix:** :248 → "the fifth result prices the removal of closure ... The seventh result is an optimality result".

### PREDICTIONS-21 — Companion mislabels delay D as "decodability"
- **Locations:** drafts/companion-computational-paper-draft.md:145, :147
- **Fix:** :145 → "holds operands decodable across distractor delays D = 20–45 (decode 0.61–0.76 against chance 0.50)".

### PREDICTIONS-22 — Transfer-probe chance level 0.8 unexplained
- **Locations:** drafts/companion-computational-paper-draft.md:133, :129; paper/full/four-model-theory-full.md:1055
- **Fix:** Define the probe scoring at :133 and say that the ablated arm sits at chance, or correct 0.8 if it is a typo. Mirror at master :1055.

### PREDICTIONS-23 — Formalization asserts a semidirect-product prediction the master lacks
- **Locations:** paper/fmt_formal/fmt-formalization.md:130; paper/full/four-model-theory-full.md:965
- **Fix:** :130 → mark it as "a prediction of the formalization, not one of Gruber (2026, §8)".

### PREDICTIONS-24 — Formalization: validation "will be reported separately" yet already cited
- **Locations:** paper/fmt_formal/fmt-formalization.md:578, :632, :323
- **Fix:** :578 and :632 → "Computational validation is reported in the companion (Gruber, 2026d); the specification below does not depend on those results."

### PREDICTIONS-25 — Stale §8.x references after the S341 renumbering
- **Locations:** drafts/papers-moc7/minimal-self.md:157; drafts/companion-computational-paper-draft.md:46, :240; paper/full/four-model-theory-full.md:1049; .claude/knowledge/prediction-framing.md:67
- **Fix:** minimal-self :157 → §8.11. Companion :240 → "§3.4.3, §8.6". Companion :46 → §8.11. prediction-framing.md:67 → §8.11 when next touched. This overlaps CITATIONS-9.

### PREDICTIONS-26 — Claim graph carries Predictions 1–5 only
- **Locations:** drafts/papers-moc7/theory-map-paper.md:376; drafts/papers-moc7/fmt-claims.json; paper/full/four-model-theory-full.md:1009, :1021
- **Fix:** Add F-PR6 (depends on F-MP1, §8.7) and F-PR7 (depends on F-TE1 and F-CL1, §8.8), and extend :376.

### PREDICTIONS-27 — Theory map: fifteen theories, nineteen rows
- **Locations:** drafts/papers-moc7/theory-map-paper.md:10, :83, :87–105
- **Fix:** State the variant grouping in the Table 1 caption, or change the count.

### PREDICTIONS-28 — Theory map: REBUS makes no anosognosia prediction
- **Locations:** drafts/papers-moc7/theory-map-paper.md:179; paper/full/four-model-theory-full.md:963, :1140; drafts/zenodo-ready/jcs/jcs-fmt-carve.md:216
- **Fix:** :179 → "REBUS with Fotopoulou's (2014) predictive-coding account of anosognosia yields the coarse prediction; the fine structure (dose dependence below ego dissolution, lesioned-hemisphere complexity, the disconnection boundary) carries the discrimination (Gruber, 2026a, §8.2)."

### PREDICTIONS-29 — JCS: two consequences announced, three given
- **Locations:** drafts/zenodo-ready/jcs/jcs-fmt-carve.md:10, :26, :192, :218, :220
- **Fix:** Say "two empirical consequences and a third contrast with recurrent processing theory", or move §7.3 into §6.8.

### PREDICTIONS-30 — Falsity study powered for HR 0.6, not for its own refutation condition
- **Locations:** drafts/zenodo-ready/falsity/falsity-gradient.md:177, :183, :187
- **Evidence:** With 30–40 events and a true HR of 1, R1 (CI entirely above 0.8) fires in only about 20–25% of samples. Powering R1 at 80% needs about 150–160 events.
- **Fix:** Either size §6.4 for R1 (about 160 events), or restate R1/R2 as a point estimate plus interval (estimated HR ≥ 0.8 with the CI excluding 0.6), and say at :183 that at the planned size a null result is usually inconclusive.

### PREDICTIONS-31 — JAIC calls an uninstantiated design an existence proof
- **Locations:** drafts/aiw130-jaic-draft.md:10, :150, :152; paper/full/four-model-theory-full.md:1055; drafts/companion-computational-paper-draft.md:117
- **Fix:** :150 → "a buildable design, not yet instantiated, that specifies closure in the open-ended regime at the level of spikes and synapses". :10 → "specifies how the checks would be built". :152 → "tabular Q-learning".

### PREDICTIONS-32 — eNeuro: FMT "recently formalised"
- **Locations:** paper/aiw47/aiw47-eneuro-opinion.md:16; paper/full/four-model-theory-full.md:925, :1077, :1118
- **Fix:** :16 → "drawn from an architectural account of consciousness (FMT; Gruber, 2026), where this dissociation is stated as the theory's sharpest architectural test (§9, Open Question 4)".

### PREDICTIONS-33 — SB-HC4A: §8 predictions said to target free modelling
- **Locations:** paper/cosmology/sb-hc4a.md:609; paper/full/four-model-theory-full.md:196, :448, :1051
- **Fix:** :609 → "(Gruber, 2026a: §3.7 and Table 1b for the free-modeling disconfirmer; §8.11 for the in-silico program; §8.2–8.8 for the architectural predictions)".

### PREDICTIONS-34 — SB-HC4A: "large angular scales (ℓ < 1500)"
- **Locations:** paper/cosmology/sb-hc4a.md:607; paper/cmb_mfdfa/cmb-mfdfa.md:12, :210
- **Fix:** Use the proposed :607 rewrite (no excess across ℓ = 2–1500, including ℓ < 100; the 9.6σ excess at ℓ = 1500–2500 is tentatively instrumental).

### PREDICTIONS-35 — SB-HC4A: "no exact replay" on a reversible finite substrate
- **Locations:** paper/cosmology/sb-hc4a.md:280, :559; drafts/zenodo-ready/nooutside/no-outside-draft-v1.0.md:827, :839
- **Fix:** Ground the no-replay claim at :280 in the coarse-grained interior description, acknowledge that substrate-level states recur, and qualify "no return to a prior state" as holding at the interior level.

### PREDICTIONS-36 — SB-HC4A formalization: CPT alternation called a "strong prediction"
- **Locations:** paper/cosmology_formal/sb-hc4a-formalization.md:494, :496
- **Fix:** :494 → "If CPT alternation holds, this is a testable consequence: ...".

### PREDICTIONS-37 — Formalization: O(1) bits per atom vs the main paper's 0.36 bits per Planck area
- **Locations:** paper/cosmology_formal/sb-hc4a-formalization.md:257, :259, :375; paper/cosmology/sb-hc4a.md:330
- **Fix:** Replace "O(1) bits" with "I = A/(4ℓ_P² ln 2) ≈ 0.36 bits per Planck area, so a boundary of order 10–20 Planck areas". At :375, note that log₂(17) ≈ 4.1 bits needs about 11 Planck areas or more.

### PREDICTIONS-38 — Energy–information module arithmetic
- **Locations:** paper/cosmology_formal/sb-hc4a-formalization.md:718, :729; paper/cosmology/sb-hc4a.md:531
- **Fix:** :729 → "1 bit = kT ln 2; at T_P this is E_P ln 2 ≈ 1.36 × 10⁹ J — a temperature-dependent rate, not a universal conversion". :718 → "scales with the square of its mass (S = 4πGM²/ℏc)".

### PREDICTIONS-39 — "Theorem" on cycle-sequence irreducibility rests on a false dichotomy
- **Locations:** paper/cosmology_formal/sb-hc4a-formalization.md:470, :472
- **Fix:** Relabel it "Conjecture" and state the missing premise, or drop the proof sketch.

### PREDICTIONS-40 — CMB: e^(−2N) suppression unsourced
- **Locations:** paper/cmb_mfdfa/cmb-mfdfa.md:287 (and :335)
- **Fix:** Cite or derive it, or soften to "suppressed exponentially in the number of e-folds".

### CITATIONS-5 — CMB self-cites SB-HC4A under a wrong title and acronym expansion
- **Locations:** paper/cmb_mfdfa/cmb-mfdfa.md:363; paper/cosmology/sb-hc4a.md:1, :15
- **Fix:** :363 → "Gruber, M. (2026). Emergent spacetime from self-referential computation: A hierarchical cellular automaton framework. *Zenodo* preprint. https://doi.org/10.5281/zenodo.18698605". Expand the acronym as "Singularity-Bounded Holographic Class 4 Automaton".

### CITATIONS-6 — Cosmology preprint cited by the superseded v2 DOI
- **Locations:** paper/full/four-model-theory-full.md:1446; paper/fmt_formal/fmt-formalization.md:686; paper/cosmology_formal/sb-hc4a-formalization.md:930; docs/decisions.md:914
- **Fix:** Replace 10.5281/zenodo.20294692 with the concept DOI 10.5281/zenodo.18698605 in each next version.

### CITATIONS-7 — Version vs concept DOIs used inconsistently in the S342 papers
- **Locations:** drafts/zenodo-ready/robot/robot-consciousness-plea.md:226; drafts/aiw130-jaic-draft.md:250, :252; drafts/zenodo-ready/plr/plr-loops-commentary.md:80; drafts/zenodo-ready/falsity/falsity-gradient.md:246; drafts/papers-book/paper1-draft.md:189, :191; drafts/zenodo-ready/nooutside/no-outside-draft-v1.0.md:1281
- **Fix:** Use concept DOIs (18669891 FMT, 21610993 companion, 18698605 SB-HC4A, 23473517 No Outside). Name a version in the text only where its wording is quoted. paper1 :191: drop "Version 1.0" or use 23473518.

### CITATIONS-8 — Stale "v19" labels
- **Locations:** drafts/papers-s339/worm-on-the-disk.md:238; drafts/papers-moc7/definitions-not-settled.md:287; drafts/zenodo-ready/nooutside/no-outside-draft-v1.0.md:1093, :1279
- **Fix:** Worm :238: drop "v19". definitions-not-settled :287: use the concept DOI. No Outside: unversioned citation in the next version. The quoted wording is unchanged, so no claim is wrong.

### CITATIONS-9 — Master section numbers stale in drafts
- **Locations:** drafts/papers-moc7/deriving-the-fmt-definition.md:196; drafts/papers-moc7/minimal-self.md:157; drafts/companion-computational-paper-draft.md:46, :67, :240
- **Fix (corrected):** Change "§8.9" to "§8.11" at deriving :196, minimal-self :157 and companion :46. At companion :67 and :240, change "(…§3.4.3, §8.8)" to "(…§3.4.3, §7.1 Table 4 note ‡, §8.10)".

### CITATIONS-10 — SB-HC4A cites §3.7 for a §3.8 point
- **Locations:** paper/cosmology/sb-hc4a.md:509; paper/full/four-model-theory-full.md:444, :537, :539
- **Fix:** :509 → "(the structural opacity of the substrate to the explicit self-model; Gruber, 2026a, Section 3.8; compare Chalmers, 2018)".

### CITATIONS-11 — SB-HC4A cites a formalization missing from its reference list
- **Locations:** paper/cosmology/sb-hc4a.md:499, :886–890; paper/cosmology_formal/sb-hc4a-formalization.md:549; ABOUT.md:31
- **Fix:** Add "Gruber, M. (2026d). Toward a mathematical formalization of the SB-HC4A cosmological model. *Zenodo* preprint. https://doi.org/10.5281/zenodo.22133504", and cite it at :499 as "(Gruber, 2026d, §6)".

### CITATIONS-12 — Formalization cites master §9 for a §10.3 limitation
- **Locations:** paper/fmt_formal/fmt-formalization.md:222; paper/full/four-model-theory-full.md:1067, :1128
- **Fix:** :222 → "(Gruber, 2026, Section 10.3)", and call it a limitation.

### CITATIONS-13 — Mukhametov et al. (1977) cited for a criticality asymmetry
- **Locations:** paper/full/four-model-theory-full.md:808
- **Fix:** :808 → "one hemisphere shows waking EEG while the other shows slow-wave sleep (Mukhametov, Supin, & Polyakova, 1977), which on the theory's reading is an asymmetry of criticality rather than of implicit-explicit permeability".

### CITATIONS-14 — New York Declaration in-text key has no matching reference
- **Locations:** paper/full/four-model-theory-full.md:789, :1192
- **Fix:** :789 → "Andrews, Birch, Sebo, & Sims, 2024".

### CITATIONS-15 — Butlin et al. TiCS entry: year, volume and authors
- **Locations:** paper/full/four-model-theory-full.md:1274; drafts/aiw130-noc-draft.md:193; drafts/aiw130-jaic-draft.md:232
- **Fix:** Use one entry everywhere: Butlin, Long, Bayne, Bengio, Birch, Chalmers, Constant, Deane, Elmoznino, Fleming, Ji, Kanai, Klein, Lindsay, Michel, Mudrik, Peters, Schwitzgebel, Simon & VanRullen (2026), *Trends in Cognitive Sciences*, 30(6), 488–501, https://doi.org/10.1016/j.tics.2025.10.011.

### CITATIONS-16 — Toker et al. (2022) cited for sleep and dreaming
- **Locations:** drafts/aiw130-noc-draft.md:55, :277; paper/aiw47/aiw47-eneuro-opinion.md:12
- **Fix:** Restrict Toker 2022 to waking, seizure, anaesthesia, psychedelics and DOC. Use a sleep-criticality source for sleep (for example Priesemann et al., 2013). Drop "dreaming" unless a source is found. This was verified from the abstract only.

### CITATIONS-17 — CMB: SOC threshold misattributed; Broadbridge cited as a preprint
- **Locations:** paper/cmb_mfdfa/cmb-mfdfa.md:106, :377, :349, :28, :261, :263
- **Fix (corrected):** :106: delete the SOC sentence or source it. :349 → "Broadbridge, P., Nanayakkara, T., & Olenko, A. (2022). On multifractionality of spherical random fields with cosmological applications. *ANZIAM Journal*, 64(2), 90-118. https://doi.org/10.1017/S1446181122000104". Update the in-text year at :28, :261 and :263.

### CITATIONS-18 — Companion cites the published master as an unpublished "Manuscript"
- **Locations:** drafts/companion-computational-paper-draft.md:268, :41, :67, :240; paper/full/four-model-theory-full.md:1448
- **Fix:** :268 → the Zenodo preprint with DOI 10.5281/zenodo.18669891. Relabel 2026e as 2026 at :67 and :240. Delete or date-stamp the :41 comment.

### CITATIONS-19 — Falsity: Thagard (1998a) does not mention Palmer (1954)
- **Locations:** drafts/zenodo-ready/falsity/falsity-gradient.md:20, :42, :148, :298
- **Evidence:** The 1997 author preprint (u1.html) and part II (u2.html) have 0 hits for "Palmer". The published 1998 version was not checked, so this is plausible rather than certain.
- **Fix:** Keep Thagard for the sterile-stomach assumption. Cite another source for Palmer's role and the method judgement (for example Marshall's 2005 Nobel lecture, or Kidd & Modlin 1998).

### CITATIONS-20 — Falsity: four returned cases vs three; Wegener 1915 cited to 1912; Bradley date
- **Locations:** drafts/zenodo-ready/falsity/falsity-gradient.md:20, :22, :140, :142, :146, :220, :240, :308
- **Fix:** Code meteorites in §5.6, or say why only three cases are coded. Add "Wegener, A. (1915). Die Entstehung der Kontinente und Ozeane. Braunschweig: Vieweg." and cite it at :146. Write "Bradley (1728/9)", or align :22 to 1728.

### CITATIONS-21 — Robot plea reference entries incomplete
- **Locations:** drafts/zenodo-ready/robot/robot-consciousness-plea.md:232, :238, :248
- **Fix:** Add "7(3), 484-494" to Hu et al. and "72-79" to Kuehn & Haddadin. Decide one year convention (online-first vs issue year) and apply it to Milinkovic & Aru. Crossref was rate-limited during verification, so recheck these details before editing.

### CITATIONS-22 — eNeuro: Katlowitz "advance online publication"
- **Locations:** paper/aiw47/aiw47-eneuro-opinion.md:117
- **Fix:** "Plasticity and language in the anaesthetized human hippocampus. *Nature* 654:714-723."

### CITATIONS-23 — JAIC: Baltieri & Kanai via an unregistered PsyArXiv DOI
- **Locations:** drafts/aiw130-jaic-draft.md:222
- **Fix:** "Baltieri, M., & Kanai, R. (2026). Steam-engine naturalism. *Behavioral and Brain Sciences*, 49. https://doi.org/10.1017/S0140525X25103531".

### CITATIONS-24 — SB-HC4A formalization: wrong Dong 2016, missing references, Finn dropped
- **Locations:** paper/cosmology_formal/sb-hc4a-formalization.md:331, :373, :490, :796, :808, :892, :910
- **Fix:** Add Dong, Harlow & Wall (2016), PRL 117, 021601, and cite it at :331. Add Bourgain (1985) and Diaconis & Holmes reference entries. Write "Boyle, Finn, and Turok (2018)" at :490 and :796.

### CITATIONS-26 — Formalization: Smithe key mismatch; Wolfram never cited by year
- **Locations:** paper/fmt_formal/fmt-formalization.md:542, :570, :610, :738, :764, :277
- **Fix:** Use "St Clere Smithe (2024)" in the text, and add "(Wolfram, 2002)" at :277.

### CITATIONS-27 — Intelligence paper: distinction "formalized" in the master
- **Locations:** paper/intelligence/paper.md:145; paper/full/four-model-theory-full.md:611, :613
- **Fix:** :145 → "developed in Gruber (2015) and restated as a cost argument in Gruber (2026, §4.2.4)". This duplicates ARCHITECTURE-24.

### CITATIONS-28 — RIM formalization: two uncited references; ISBN note
- **Locations:** paper/rim_formal/rim-formalization.md:483, :485, :497; paper/intelligence/paper.md:559; paper/cosmology/sb-hc4a.md:884; drafts/papers-s339/jcs-fmt-carve.md:284
- **Fix:** Cite or drop Driver & Tomasik (2023) and Murayama & Jach (2025). Add "(2016 corrected reprint; ISBN 9781326652074)" at RIM :485 and JCS :284.

### CITATIONS-29 — Permeability paper: ConCrit attributed to Priesemann; no FMT reference
- **Locations:** paper/fmt_permeability_criticality/fmt-permeability-criticality.md:78, :82, :192
- **Fix:** :82 → "(Priesemann et al., 2013, 2014; reviewed under the ConCrit framework, Algom & Shriki, 2026)", and add that entry. Add and cite the FMT reference (10.5281/zenodo.18669891) at :78. Cite or drop Carhart-Harris (2014).

### CITATIONS-30 — JCS: Tononi (2004) cited for the phenomenological axioms
- **Locations:** drafts/zenodo-ready/jcs/jcs-fmt-carve.md:104; drafts/papers-moc7/deriving-the-fmt-definition.md:196
- **Fix:** :104 → "(Tononi, 2004; Oizumi, Albantakis and Tononi, 2014)" or "(Tononi and Koch, 2015)", and add the entry.

### CITATIONS-33 — PLR title escape; SB-HC4A duplicated clause
- **Locations:** drafts/zenodo-ready/plr/plr-loops-commentary.md:1; paper/cosmology/sb-hc4a.md:581
- **Fix:** PLR :1: remove "\-". sb-hc4a :581: end the sentence at "not a test of it." and delete the repeated clause.

## Rejected by verifier

| ID | Title | Reason |
|---|---|---|
| SUFFICIENCY-14 | RIM conjunction omits embodiment and the axis, made an iff | rim-formalization.md:119 is a necessity claim and the master makes neither conjunct necessary; the :343 iff concerns development (covered by SUFFICIENCY-16). |
| SUFFICIENCY-21 | Robot plea grades consciousness by subcriticality | Plea :26 paraphrases the S329 guardrail itself (prediction-framing.md:40) and says criticality is not a requirement. |
| SUFFICIENCY-22 | PLR answers "where closure becomes sufficient" with the self-model alone | A difference of scope: the commentary offers a hedged candidate answer and does not claim FMT's full sufficient condition. |
| SUFFICIENCY-25 | JAIC §8: a positive verdict licenses attribution | JAIC :184 licenses only "the consciousness-relevant property", and :88 and :190 add the further conjuncts. |
| ARCHITECTURE-28 | No Outside calls implicit/explicit a didactic cut | A deliberate epistemic stance, kept "anyway" for its explanatory power; consistent with master OQ1. |
| ARCHITECTURE-34 | PLR body-first passage implies the self-model is older | PLR :38 explicitly says nothing requires the system to represent itself; MG approved it (decisions.md:16). |
| PREDICTIONS-2 | Prediction 4 ties level to criticality, discontinuous onset | Sanctioned by MG rulings (decisions.md:1290, :65). Only prediction-framing.md:29 is stale, and that is a knowledge file. |
| CITATIONS-25 | Wetterich results stated as class-wide equivalence | fmt-formalization :506 paraphrases the Wetterich abstract faithfully; :508 is the paper's own hedged conjecture. |
| CITATIONS-31 | Worm cites an unpublished "in preparation, §2" | The premise is wrong: the worm paper never says the book argues that point, and a section pointer to a work in preparation is normal. |
| CITATIONS-32 | Master's "first submission to peer review" sentence | Defensible as a contrast with the 2015 monograph; any rewording is MG's style call. |

## Coverage

All five requested groups returned results: master, formal-rim, cosmo-books, new-preprints, unpublished.

- **master:** paper/full/four-model-theory-full.md (full), fmt-misconception-registry.md, prediction-framing.md, plus targeted greps of ABOUT.md, README.md, docs/decisions.md (:914) and docs/fmt-citation-audit.md (:52, :82).
- **formal-rim:** paper/fmt_formal/fmt-formalization.md, paper/intelligence/paper.md, paper/rim_formal/rim-formalization.md, /home/jeltz/crucible/papers/fmt-implementation-spec.md, drafts/companion-computational-paper-draft.md, the knowledge files, fmt-2015-definitions.md (:145–175), and the head of docs/zenodo-changelog-companion-v4.md. Master read in part: :132–660, :738–830 and :929–1135, plus greps.
- **cosmo-books:** paper/cosmology/sb-hc4a.md, paper/cosmology_formal/sb-hc4a-formalization.md, paper/cmb_mfdfa/cmb-mfdfa.md, No Outside v1.0, worm-on-the-disk.md, and the fmt-formalization headings and §6.3–6.4. Master read in part: :132–548, :1067–1075 and :1122–1130.
- **new-preprints:** PLR commentary, falsity gradient, robot plea, both JCS carve copies, the PLR blog, drafts/monograph-limits/03-ch06-07.md (grep), u1.html (Thagard), git show 59c42324, the DataCite API for five Zenodo records, and the Crossref API for 50 sampled external DOIs. Master read in part.
- **unpublished:** the JAIC and NoC drafts, definitions-not-settled, deriving-the-fmt-definition, minimal-self, the eNeuro opinion, the permeability/criticality paper, qualia privacy, Olinyk/CRC, the theory map, paper1-draft, docs/decisions.md (:11–20), fmt-2015-definitions.md (grep), and the crucible evidence-ledger digest (grep). External checks: Zenodo API, Crossref, arXiv, the arXiv HTML of Kanai & Ma, and the OpenAlex Toker 2022 abstract.

No group failed. Limits worth knowing:
- Crossref was rate-limited during verification of CITATIONS-13 and CITATIONS-21, so those bibliographic details rest on the finder's lookup.
- Toker et al. (2026) was not checked (SUFFICIENCY-4).
- For Toker et al. (2022), only the abstract was read (CITATIONS-16).
- For Thagard, the published 1998 version was not checked (CITATIONS-19).
- No Outside :1179 is unconfirmed (ARCHITECTURE-16).
- Frozen past submissions (paper/trimmed/noc, paper/cc, paper/aice) were reached only by grep for SUFFICIENCY-12. They were not read in full.
