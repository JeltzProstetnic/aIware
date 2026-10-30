# Fable — Citation-Integrity Audit + Edit Plan: SB-HC4A cosmology paper + formalization (S245)

**Scope:** author-level, web-verified audit of every load-bearing reference in
- Parent: `paper/cosmology/sb-hc4a.md` (+ `.tex`)
- Formalization: `paper/cosmology_formal/sb-hc4a-formalization.md` (+ `.tex`)

**Method:** WebSearch/WebFetch verification of authors, title, venue, year, DOI/arXiv id. No claim rests on memory.

**Headline:** All 6 S244-flagged items **CONFIRMED**. 4 additional citation errors found. Two structural physics fixes specified. Formalization contains one **FALSE proposition** (conformal-time / "Universal Temporal Unreachability") that contradicts the corrected parent and must be deleted or restated.

**Count: 6 confirmed disqualifying-tier fabrications/misattributions + 4 additional citation errors = 10 distinct problems.** The McCane/Dryden fabrication and the electron-scale mismatch appear in BOTH manuscripts.

---

## PART 1 — CONFIRMED DISQUALIFYING ITEMS (S244 flags, all verified)

### 1.1 Afik & de Nova (2022) — WRONG VENUE + FACTUAL OVERCLAIM ★ most serious
- **As cited (parent ref, line 673):** "Afik, Y., & de Nova, J. M. R. (2022). Quantum information with top quarks in QCD. *Physical Review D*, 106(3), 034032."
- **As claimed in text (parent §6.5, line 397):** "Afik and de Nova (2022) **demonstrated Bell-inequality-violating entanglement** in top-quark pair production at the LHC…"
- **Verified truth:**
  - The paper IS real but the venue is wrong: **Quantum 6, 820 (2022)**, arXiv:2203.05582 — NOT *Phys. Rev. D* 106, 034032.
  - It is a **theoretical proposal** ("proposed measuring…"), not a demonstration.
  - **Entanglement** in top–antitop was later **observed** by **ATLAS (Nature 633, 542–547, 2024)** and **CMS (Rep. Prog. Phys. 87, 117801, 2024)**. **Bell-inequality violation is NOT experimentally established** — still at the proposal/analysis stage.
  - (Author initials also off: paper is by J. R. M. de Nova; cited "J. M. R.")
- **Sources:** https://arxiv.org/abs/2203.05582 · https://www.nature.com/articles/s41586-024-07824-z · https://link.springer.com/article/10.1007/JHEP07(2024)192
- **Appears:** parent only (§6.5 + ref). Triple error (venue + proposal-vs-demonstration + Bell overclaim).

### 1.2 "McCane & Dryden (2022)" → McCormack & Hoff (2022) — FABRICATED AUTHOR NAMES (both papers)
- **As cited:** "McCane, B., & Dryden, I. L. (2022). The Stein effect for Fréchet means. *Annals of Statistics*, 50(6), 3647–3676."
- **Verified truth:** Correct paper, journal, volume, issue, pages — but **BOTH author surnames are fabricated.** Real authors: **Andrew McCormack & Peter Hoff**, *Ann. Statist.* 50(6), 3647–3676 (2022), **DOI 10.1214/22-AOS2245** (arXiv:2009.09101).
- **Source:** https://projecteuclid.org/journals/annals-of-statistics/volume-50/issue-6/The-Stein-effect-for-Fréchet-means/10.1214/22-AOS2245.full
- **Appears in BOTH papers:** parent §6.5 (line 395) + ref (821); formalization §4.6/JS2 (line 362), §10 Module 4.6 (line 791), + ref (939). Same fabrication in both.

### 1.3 Ma et al. (2019, Neuron) — 2 FABRICATED AUTHORS
- **As cited (parent, line 819):** "Ma, Z., Turrigiano, G. G., **Bhatt, D. H., & Bhatt, W. B.** (2019). Cortical circuit dynamics are homeostatically tuned to criticality in vivo. *Neuron*, 104(4), 655–664."
- **Verified truth:** Real authors: **Ma Z, Turrigiano GG, Wessel R, Hengen KB.** Journal/volume/pages correct (Neuron 104, 655–664). "Bhatt, D. H." and "Bhatt, W. B." are **both invented** — they replace Wessel R. and Hengen K.B.
- **Source:** https://www.sciencedirect.com/science/article/pii/S0896627319307378 · https://pmc.ncbi.nlm.nih.gov/articles/PMC6934140/
- **Appears:** parent §7.2 (line 426) + ref.

### 1.4 Hengen et al. (2016, Cell) — 1 FABRICATED FINAL AUTHOR
- **As cited (parent, line 791):** "Hengen, K. B., Torrado Pacheco, A., McGregor, J. N., Van Hooser, S. D., **& Bhatt, D. H.** (2016). Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. *Cell*, 165(1), 180–191."
- **Verified truth:** Real final author is **Gina G. Turrigiano**, not "Bhatt, D. H." Full author list: Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, **Turrigiano GG**. Journal/vol/pages correct.
- **Source:** https://www.cell.com/cell/fulltext/S0092-8674(16)30060-5 · https://pubmed.ncbi.nlm.nih.gov/26997481/
- **Appears:** parent §7.2 (line 426) + ref. (Note: the same fictitious "Bhatt" surname is spliced into 1.3 and 1.4 — a coupled fabrication.)

### 1.5 "Jow, Scott & Sievers (2022) arXiv:2208.06021" — INVENTED AUTHOR + WRONG-PAPER FUSION
- **As cited (parent, line 801):** "Jow, D. L., Scott, D., **& Sievers, J. L.** (2022). Re-evaluating evidence for Hawking points in the CMB. *JCAP*. **arXiv:2208.06021**."
- **Verified truth — three-way conflation:**
  - The **title** "Re-evaluating evidence for Hawking points in the CMB" is the real **Jow & Scott (2020)** paper — **arXiv:1909.09672**, JCAP 2020(03):021. **Two authors only** (D. L. Jow, D. Scott).
  - **arXiv:2208.06021** is a **different paper**: "The quest for CMB signatures of Conformal Cyclic Cosmology" by **Bodnia, Isenbaev, Colburn, Swearngin & Bouwmeester (2022)**.
  - **"Sievers, J. L." is an invented author** — on neither paper.
- **Sources:** https://arxiv.org/abs/1909.09672 · https://iopscience.iop.org/article/10.1088/1475-7516/2020/03/021/pdf · https://arxiv.org/abs/2208.06021
- **Fix:** cite **Jow, D. L., & Scott, D. (2020). Re-evaluating evidence for Hawking points in the CMB. *JCAP*, 2020(03), 021. arXiv:1909.09672.** Drop Sievers; drop 2208.06021 (or cite Bodnia et al. 2022 separately if that paper's null result is wanted).
- **Appears:** parent §9.6 (line 552) + ref.

### 1.6 No-hair theorem mis-attributed to "Israel (1967, 1968)" alone — MISATTRIBUTION
- **As cited (parent §5.7, line 314):** "The no-hair theorem (Israel, 1967, 1968) establishes that a black hole is fully described by three quantities: mass (M), charge (Q), and angular momentum (J)."
- **Verified truth:** Israel (1967, *Phys. Rev.* 164, 1776) covers **static vacuum** (Schwarzschild uniqueness); Israel (1968, *Comm. Math. Phys.* 8, 245) covers **static electrovac** (Reissner–Nordström). **Neither covers rotation (J).** The full stationary M,Q,J uniqueness rests on **Carter (1971)** + **Hawking rigidity (1972)** + **Robinson (1975)**.
- **Source:** https://en.wikipedia.org/wiki/No-hair_theorem (uniqueness-theorem lineage) · standard result.
- **Fix:** see Part 4b.
- **Appears:** parent §5.7 only.

---

## PART 2 — ADDITIONAL ERRORS FOUND (not in S244 list)

### 2.1 Ruggiero (2020) — MISATTRIBUTION TO WRONG PERSON
- **As cited (parent, line 869):** "**Ruggiero, M. L.** (2020). Big Rip: Heating by Hawking radiation and a possible connection to conformal cyclic cosmology. arXiv:2005.12684."
- **Verified truth:** arXiv id + title correct, but the author is **Rafael Ruggiero** → initial **"R."**, not "M. L." **M. L. Ruggiero (Matteo Luca Ruggiero)** is a *different* relativist; the initials misattribute the paper to the wrong physicist.
- **Source:** https://arxiv.org/abs/2005.12684 · https://ruggiero.github.io/
- **Appears:** parent §5.4 (line 262) + ref.

### 2.2 Elze (2024) — WRONG VOLUME + WRONG ARTICLE NUMBER
- **As cited (parent, line 757):** "Elze, H.-T. (2024). Cellular automaton ontology, bits, qubits and the Dirac equation. *International Journal of Quantum Information*, **24(7), 2450138**."
- **Verified truth:** Real: *Int. J. Quantum Inf.* **vol. 22, article 2450013** (2024), arXiv:2401.08253. Cited volume (24) and article number (2450138 — digits transposed from 2450013) are both wrong. Authors/title/journal/year OK.
- **Source:** https://www.worldscientific.com/doi/10.1142/S0219749924500138 · https://arxiv.org/abs/2401.08253
- **Appears:** parent §5.6 (line 310) + ref.

### 2.3 Almheiri et al. — WRONG YEAR (minor)
- **As cited (parent, line 681):** "Almheiri, A., Hartman, T., Maldacena, J., Shaghoulian, E., & Tajdini, A. **(2020)**. The entropy of Hawking radiation. *Reviews of Modern Physics*, 93(3), 035002."
- **Verified truth:** Published **2021** (Rev. Mod. Phys. 93, 035002, 21 Jul 2021; arXiv:2006.06872 is 2020). In-text also cites "2020."
- **Source:** https://link.aps.org/doi/10.1103/RevModPhys.93.035002
- **Fix:** change year to 2021 (or cite arXiv:2006.06872 if the 2020 date is intended).

### 2.4 Algom & Shriki (2026) — WRONG FIRST-AUTHOR INITIAL (minor)
- **As cited (parent, line 679):** "**Algom, S.**, & Shriki, O. (2026). The ConCrit framework: Critical brain dynamics as a unifying mechanism for consciousness theories. *Neuroscience & Biobehavioral Reviews*."
- **Verified truth:** First author is **Inbal Algom → "Algom, I."** Real title: "The ConCrit framework: Critical brain dynamics as a unifying **mechanistic framework for theories of consciousness**," *Neurosci. Biobehav. Rev.* **vol. 180, art. 106483 (2026)**. Add vol/article; fix initial; align title.
- **Source:** https://www.sciencedirect.com/science/article/pii/S0149763425004841

### 2.5 Boyle & Turok (2022b) — RECOMMEND VERIFYING (unresolved)
- **As cited (parent, line 719):** "Boyle, L., & Turok, N. (2022b). Thermodynamic solution of the homogeneity, isotropy and flatness puzzles… *Physics Letters B*, 849, 138442."
- **Status:** title matches a real Boyle–Turok paper, but *Phys. Lett. B* **vol. 849 corresponds to ~2024**, so the year/volume pairing looks inconsistent. Not verified this pass — flag for a targeted check before submission.

**Verified CORRECT (spot-checked, no change needed):** Vopson (2025, AIP Advances 15, 045035) · Boyle, Finn & Turok (2022a, Ann. Phys. 438, 168767) · Wetterich 2022b (PRD 105, 074502) · Wetterich 2022d (Phil. Trans. R. Soc. A 380(2216), 20210066) · Carter (1968, Phys. Rev. 174, 1559 — g=2 attribution correct) · Ruggiero arXiv id · Jow&Scott arXiv id.

---

## PART 3 — CORRECTED CITATION TABLE (as-cited → corrected → source)

| # | As cited | Corrected | Verifying source |
|---|----------|-----------|------------------|
| 1 | Afik & de Nova (2022), *Phys. Rev. D* 106(3) 034032; "demonstrated Bell-violating entanglement" | Afik & de Nova (2022), **Quantum 6, 820**, arXiv:2203.05582 — a **proposal**; entanglement **observed** ATLAS 2024 / CMS 2024; **Bell violation not established** | arxiv.org/abs/2203.05582 ; nature.com/articles/s41586-024-07824-z |
| 2 | McCane, B., & Dryden, I. L. (2022) | **McCormack, A., & Hoff, P. D. (2022)**, *Ann. Statist.* 50(6), 3647–3676, DOI 10.1214/22-AOS2245 | projecteuclid.org …/10.1214/22-AOS2245 |
| 3 | Ma, Z., Turrigiano, Bhatt D.H., Bhatt W.B. (2019) | **Ma, Z., Turrigiano, G. G., Wessel, R., & Hengen, K. B. (2019)**, *Neuron* 104(4), 655–664 | sciencedirect.com/…/S0896627319307378 |
| 4 | Hengen, Torrado Pacheco, McGregor, Van Hooser, **Bhatt D.H.** (2016) | Hengen, Torrado Pacheco, McGregor, Van Hooser, **Turrigiano, G. G.** (2016), *Cell* 165(1), 180–191 | cell.com/cell/fulltext/S0092-8674(16)30060-5 |
| 5 | Jow, Scott & **Sievers** (2022), arXiv:2208.06021 | **Jow, D. L., & Scott, D. (2020)**, *JCAP* 2020(03), 021, **arXiv:1909.09672** | arxiv.org/abs/1909.09672 |
| 6 | No-hair theorem (Israel 1967, 1968) [M,Q,J] | Israel (1967,1968) = **static only**; add **Carter (1971) + Hawking (1972) + Robinson (1975)** for M,Q,J | en.wikipedia.org/wiki/No-hair_theorem |
| 7 | Ruggiero, **M. L.** (2020) | Ruggiero, **R.** (2020), arXiv:2005.12684 | ruggiero.github.io ; arxiv.org/abs/2005.12684 |
| 8 | Elze (2024), *IJQI* **24(7), 2450138** | Elze (2024), *IJQI* **22, 2450013**, arXiv:2401.08253 | worldscientific.com/…/S0219749924500138 |
| 9 | Almheiri et al. (**2020**), RMP 93 035002 | Almheiri et al. (**2021**), RMP 93, 035002 | link.aps.org/doi/10.1103/RevModPhys.93.035002 |
| 10 | **Algom, S.**, & Shriki (2026) | **Algom, I.**, & Shriki, O. (2026), *NBR* 180, 106483 | sciencedirect.com/…/S0149763425004841 |

---

## PART 4 — IN-TEXT CLAIM REWORDINGS

### 4a. Afik / Bell overclaim — exact corrected wording (parent §6.5, "The empirical anchor", line 397)

**REPLACE the paragraph:**
> **The empirical anchor.** Afik and de Nova (2022) demonstrated Bell-inequality-violating entanglement in top-quark pair production at the LHC — the highest-energy regime experimentally accessible. This result functions in the present argument not as support but as a specification of the target. It fixes the empirical correlation strength that any substrate-level mechanism must reproduce, and it establishes that entanglement is a substrate-level property — persisting undiminished at the highest energies probed — rather than an artifact of low-energy effective description.

**WITH:**
> **The empirical anchor.** Afik and de Nova (2022) proposed using top-quark pair production at the LHC — the highest-energy regime experimentally accessible — to probe entanglement and Bell-inequality violation, and the ATLAS and CMS collaborations subsequently *observed* entanglement in top–antitop production (ATLAS Collaboration, 2024; CMS Collaboration, 2024). Bell-inequality *violation* in this system has been proposed and analysed but is not yet experimentally established. The observed entanglement functions in the present argument not as support but as a specification of the target: it establishes that entanglement is a substrate-level property — persisting undiminished at the highest energies probed — rather than an artifact of low-energy effective description, and it fixes the empirical correlation strength that any substrate-level mechanism must reproduce.

*(Also update the abstract's "highest-energy regime" gloss only if it repeats the Bell claim — it does not, so no abstract change needed here.)*

### 4b. No-hair theorem — corrected sentence + refs (parent §5.7, line 314)

**REPLACE:**
> The no-hair theorem (Israel, 1967, 1968) establishes that a black hole is fully described by three quantities: mass (M), charge (Q), and angular momentum (J).

**WITH:**
> The black-hole uniqueness ("no-hair") theorems establish that a stationary black hole in Einstein–Maxwell theory is fully described by three quantities: mass (M), charge (Q), and angular momentum (J). Israel (1967, 1968) proved uniqueness for the *static* (J = 0) vacuum and electrovac cases; the rotating, charged case rests on the uniqueness results of Carter (1971) and Robinson (1975) together with Hawking's (1972) rigidity theorem.

**Add to reference list:**
- Carter, B. (1971). Axisymmetric black hole has only two degrees of freedom. *Physical Review Letters*, 26(6), 331–333.
- Hawking, S. W. (1972). Black holes in general relativity. *Communications in Mathematical Physics*, 25(2), 152–166.
- Robinson, D. C. (1975). Uniqueness of the Kerr black hole. *Physical Review Letters*, 34(14), 905–906.

---

## PART 5 — STRUCTURAL FIX 3a: §7 "Not Analogy but Structural Identity" → "Structural Correspondence"

**Rationale:** brain = universe is an analogy/conjecture (a proposed cross-scale correspondence), **not** an established identity. The single-surface *singularity* identity of §5.2 is a separately-postulated claim and is out of scope here; only the *cross-scale* (brain↔universe) identity is downgraded.

Find→replace, parent:

1. **Heading (line 422):**
   `### 7.2 Not Analogy but Structural Identity`
   → `### 7.2 Structural Correspondence, Not Mere Analogy`

2. **Line 409 (§7.1 opener):**
   `The SB-HC4A architecture maps onto the architecture of self-referential computational systems with exact structural correspondence:`
   → `The SB-HC4A architecture is conjectured to map onto the architecture of self-referential computational systems, with the following structural correspondences:`

3. **Line 424 (§7.2 opener):**
   `This mapping is not metaphorical. Both systems implement the same formal architecture:`
   → `This mapping is proposed as more than metaphorical: the claim is that both systems fall in the same computational class and share the following architectural features. Whether this rises to a strict structural identity — rather than a strong correspondence — is left open, and is the burden of the formalization (Gruber, 2026 formalization, §6).`

4. **§7.3 line 438:**
   `instantiate the *same computational pattern* at different scales`
   → keep, but prepend hedge: `are conjectured to instantiate the *same computational pattern* at different scales` (verb already appropriately weak; optional).

5. **Abstract (line 15):**
   `This architecture is structurally identical to self-referential computational systems that operate at criticality`
   → `This architecture structurally corresponds to self-referential computational systems that operate at criticality`
   and
   `Self-modeling cognitive systems are thus local, scale-reduced instances of the same computational pattern`
   → `Self-modeling cognitive systems are thus argued to be local, scale-reduced instances of the same computational pattern`

6. **Conclusion (line 663):**
   `This architecture is structurally identical to the architecture of self-referential computational systems`
   → `This architecture structurally corresponds to (and is conjectured to share the computational class of) the architecture of self-referential computational systems`

*(The `.tex` sibling carries the same strings — apply the identical replacements in `paper/cosmology/sb-hc4a.tex`.)*

---

## PART 6 — TASK 4: FORMALIZATION SYNCS-TO-PARENT (stronger/retracted physics)

The formalization asserts physics the corrected parent has already walked back. Two hard fixes + one framing fix.

### 6.1 §3.3 "Universal Temporal Unreachability" Proposition — **FALSE; DELETE or RESTATE** ★
- **The error (lines 178, 180, 184):**
  - Line 178: "a radiation-dominated universe gives **η → −∞ as t → 0⁺**. The Big Bang maps to the infinite past in conformal time — it is asymptotically unreachable." **FALSE.** For radiation, a(t) ∝ t^½ ⇒ η = ∫dt/a ∝ ∫t^(−½)dt = 2t^½ → **0 (finite)** as t→0. Conformal time is **finite** at the Big Bang — which is exactly the **horizon problem**. (The parent §5.3, line 224, states this correctly.)
  - Line 180: crunch "η → +∞ as t → t_crunch" — **FALSE** for the same reason (finite conformal time to the crunch).
  - Line 184, **Proposition (Universal Temporal Unreachability):** "All information boundaries … are temporally asymptotically unreachable … a *consequence* of IB1–IB3." **FALSE as stated** — the temporal termini are reached at finite proper *and* finite conformal time (geodesic incompleteness: world-lines *terminate*, they do not asymptote).
- **Corrected replacement (mirror the parent's three-mode taxonomy, §5.3):**
  - Fix line 178: "In conformal time η, a radiation-dominated universe gives η ∝ 2t^½ → **0** (a finite value) as t → 0⁺: the Big Bang lies at **finite** conformal — and finite proper — depth. This finiteness is the horizon problem. Only under past-eternal continuations (eternal inflation; Penrose's CCC; the Boyle–Turok CPT-symmetric universe) does the conformal coordinate extend to η → −∞."
  - Fix line 180 correspondingly: the crunch is reached at **finite** conformal and proper time; geodesics are incomplete there.
  - **Replace the Proposition** with a **No-Arrival (three-mode)** statement matching the parent §5.3 "What survives" ladder:
    > **Proposition (No-Arrival, three modes).** No member of the singularity inventory is ever an event in its computational domain, but for three distinct geometric reasons: horizons **recede** (arrival forbidden; asymptotic in the interior parameter), the scale floor is **shielded** (arrival regenerated at larger scale; heuristic), and the temporal termini **terminate without arrival** (world-lines are geodesically incomplete at finite proper time; arrival *undefined*, not merely forbidden). Information impermeability (IB1–IB3) is shared by all three; asymptotic-approach geometry is **not** — it holds for horizons, heuristically for the scale floor, and for the termini only under past-eternal continuations. Temporal *asymptotic* unreachability is therefore **not** a consequence of IB1–IB3.
  - Update the §3.3 closing sentence (line 186) that calls unreachability "not a contingent physical fact but a structural feature" — restrict it to horizons/scale-floor; the termini are the exception.
  - Cascade: abstract (line 15, "temporal asymptotic structure") and §10 Module 3 (line 777, "verify temporal unreachability as a consequence of IB1–IB3") must drop the "consequence of IB1–IB3" phrasing — the corrected claim is a three-mode *taxonomy*, not a derived universal.

### 6.2 Electron Kerr-Newman = super-extremal — sync the particle-boundary claim ★
- **The gap:** §3.7 (Definition, line 238) and the inventory table (line 158, "Particle interiors … Claimed: Planck-scale Bekenstein saturation") assert particles are stable **Planck-scale** singularity boundaries of area ~ℓ_P² with horizon-like IB1–IB3 — with no mention of the scale/horizon tension the parent §5.7 now concedes.
- **Parent's corrected position (§5.7, line 318):** the Kerr–Newman electron is **super-extremal** (J exceeds the horizon bound by >40 orders of magnitude) ⇒ a **naked, horizonless ring singularity** at the **Compton scale ~10⁻¹³ m**, **not** the Planck scale. The Planck-scale, information-impermeable core is a **conjectured** torsion-regularized object (Einstein–Cartan / Popławski 2010), not an established Kerr–Newman horizon.
- **Required edit:** add a caveat to §3.7 (after the Definition / around line 250) and to the inventory table's "Particle interiors" row:
  > *Caveat (scale/horizon tension).* The classical Kerr–Newman solution with electron parameters is super-extremal: it has **no horizon** (a naked ring singularity) and its ring radius is of order the **Compton** scale, ~10⁻¹³ m, ~20 orders of magnitude above the Planck length. The identification of a particle with a **Planck-scale, horizon-bounded** Bekenstein-saturated surface (CA1–CA3) is therefore a **model posit requiring a torsion-regularized core** (Poplawski, 2010), not a consequence of the classical field equations. This is the weakest entry in the inventory (cf. Gruber 2026a, §5.7).
- The formalization already flags the particle-interior row as "the weakest" (line 166) — but must **name** the super-extremality / naked-singularity / Compton-vs-Planck problem explicitly to match the parent, rather than presenting Planck-scale saturation as merely "claimed."

### 6.3 "Structural identity functor" → "structural correspondence functor" (framing sync with 3a)
- §6 title (line 532), §6.2 (line 546), abstract (line 15, "cross-scale structural identity as a functor"), §10 Module 6 (line 789), §11.1 (line 807) all assert a "structural identity functor." To stay consistent with the parent's §7 downgrade (correspondence, not identity):
  - Retitle §6 → "The Cross-Scale **Structural Correspondence** Functor (Proposed)."
  - In §6.2/§11.1 present the functor as **conjectured/proposed** (the text at line 789 already hedges "Demonstrating that this functor exists…" — extend that hedge to the section headings and the abstract).
  - This is a wording/consistency fix, not a physics error — but leaving "identity" in the formalization while the parent says "correspondence" is an internal contradiction reviewers will catch.

---

## PART 7 — NEW REFERENCES TO ADD (net)

Parent:
- Carter, B. (1971). Axisymmetric black hole has only two degrees of freedom. *Physical Review Letters*, 26(6), 331–333.
- Hawking, S. W. (1972). Black holes in general relativity. *Communications in Mathematical Physics*, 25(2), 152–166.
- Robinson, D. C. (1975). Uniqueness of the Kerr black hole. *Physical Review Letters*, 34(14), 905–906.
- ATLAS Collaboration. (2024). Observation of quantum entanglement with top quarks at the ATLAS detector. *Nature*, 633, 542–547.
- CMS Collaboration. (2024). Observation of quantum entanglement in top quark pair production in pp collisions at √s = 13 TeV. *Reports on Progress in Physics*, 87, 117801.

(Optionally, if the Bodnia et al. null result is wanted alongside Jow & Scott: Bodnia, E., Isenbaev, V., Colburn, K., Swearngin, J., & Bouwmeester, D. (2022). The quest for CMB signatures of Conformal Cyclic Cosmology. arXiv:2208.06021.)

Both papers: replace every "McCane, B., & Dryden, I. L. (2022)" with "McCormack, A., & Hoff, P. D. (2022)."

---

## PART 8 — WHERE EACH FIX LANDS (file/line map)

Parent `paper/cosmology/sb-hc4a.md` (+ `.tex`): §3.2 line 122 (Algom initial) · §5.4 line 262 (Ruggiero initial) · §5.6 line 310 (Elze vol/art) · §5.7 line 314 (no-hair) + line 318 (already-correct super-extremal discussion — keep) · §6.5 line 397 (Afik reword) · §7.1–7.3 lines 409/422/424/438 (identity→correspondence) · §8.2 line 460/681 (Almheiri year) · §9.6 line 552 (Jow/Scott/Sievers) · abstract line 15 + conclusion line 663 (identity→correspondence) · ref list lines 673, 679, 681, 757, 801, 819, 821, 869.

Formalization `paper/cosmology_formal/sb-hc4a-formalization.md` (+ `.tex`): §3.2 table line 158 (particle-interior caveat) · §3.3 lines 178/180/184/186 (conformal-time Proposition — DELETE/RESTATE) · §3.7 ~line 250 (super-extremal caveat) · §4.6/JS2 line 362 + §10 line 791 + ref line 939 (McCane→McCormack&Hoff) · §6 lines 532/546 + §10 line 789 + §11.1 line 807 + abstract line 15 (identity→correspondence) · §10 Module 3 line 777 (drop "consequence of IB1–IB3").

**Remember:** edit `.md` first (source of truth), then mirror into `.tex`; run `pytest scripts/test_content_integrity.py` before any `.tex` commit; bibtex needs `dangerouslyDisableSandbox`.
