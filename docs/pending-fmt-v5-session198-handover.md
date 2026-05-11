Action: present
Tracked-by: AIW-51

# FMT v5 Revision — Session 198 Handover

**From:** Session 197 (2026-05-11, WSL)
**Paper state:** `paper/full/four-model-theory-full.md` at 29,126 words (up from 28,079)
**Commits:** Session 197 commit (pending — commit at shutdown)
**Decision:** 28k Zenodo version stays as-is; no aggressive word count cuts. Journal versions (JCS, etc.) are separate manuscripts.

## What Was Done in Session 197

### Phase B — Section-Level Fixes (ALL COMPLETE)
1. **Frankish weak illusionism engagement** (§3.4.4): Named weak illusionism, argued specific distance, acknowledged empirical indistinguishability, framed as ethical consequence (artificial consciousness moral patienthood)
2. **Criticality concrete signatures** (§3.7): New paragraph anchoring DFA α, branching ratio σ, avalanche exponents as THE operational signatures, with testability commitment
3. **Animal consciousness expanded** (§6.5): Nieder 2020 corvids (single-neuron correlate), Barron & Klein 2016 insects (boundary question), Birch 2020 dimensions, Godfrey-Smith 2016 cephalopods, methodological cautions
4. **Prediction 3 de-reified** (§8.4): "DMN = ESM network" replaced with cosine-distance formulation (d ≥ 0.5 self-referential vs d < 0.2 sensorimotor)
5. **§4.2 subsection structure**: Split into 4.2.1 Dual Evaluation, 4.2.2 Free Will/Identity, 4.2.3 Cognitive Learning, 4.2.4 Standard Objections

### Phase C — Structural/Editorial (ALL COMPLETE)
6. **§6 cut 8→3**: Dreams + split-brain condensed to one section; clinical psych compressed; kept psychedelics, anosognosia, DID as the three prediction-connected phenomena
7. **8 citations added**: Seth & Bayne 2022, Aru/Suzuki/Larkum 2020, Beautiful Loop (Laukkonen/Friston/Chandaria 2025), Metzinger 2024, Dehaene 2021, Kleiner 2024, Barron & Klein 2016, Birch et al. 2020, Nieder et al. 2020, Godfrey-Smith 2016
8. **Self-citations pruned**: 21 → ~8 Gruber refs (kept first mention, derivation claim, convergence section, companion papers)

### 6-Angle Adversarial Re-Review (ALL FINDINGS TRIAGED)
19 findings identified, all resolved:
- 11 reference [VERIFY] markers cleared (web-verified)
- 2 journal-level placeholders replaced (Acta Analytica → Wagner-Altendorf 2024, Frontiers → Kirkeby-Hinrup 2025b)
- NFL theorem reframed (optimization → implementation independence argument)
- COGITATE phrasing softened
- Convergence timeline made honest (pre-2015 = consistency, post-2015 = convergence; theory developed ~2005, published 2015)
- Tone: "dissolves" → "addresses" outside §3.4; "pre-paradigm state" → "has not converged"; "crisis" → "difficulty"
- Holographic analogy fixed for explicit models (processes, not stored structures)
- Prediction 4 qualified (measurement protocol premature; criticality markers ≠ gamma; Voss 2014 acknowledged)
- Derivation chains added to all 4 predictions (principle → mechanism → prediction)
- Permeability quantified (LZc ~15-20% increase, formalization gap acknowledged)
- Power-law counterargument cited (Touboul & Destexhe 2017)
- Blindsight residual phenomenology acknowledged (Phillips 2021)
- Closure: foundational commitment made explicit (parallels IIT axioms, GNW broadcasting thesis)
- Table 5: rubric fairness sentence added
- Frankish: honest philosophical divide + ethical consequence framing
- Orphaned reference removed (Alkire/Haier/Fallon 2000)
- Unverifiable references removed (Frankish 2023, Lau/Michel/LeDoux 2024, Tsuchiya & Saigo 2024)

## What Remains — Session 198 Must-Do

### FIRST: Flow check + formal/technical review (3-4 subagents)
The paper has had ~190 lines changed across 20+ edits. Before building, run:
1. **Flow/coherence reviewer**: Read full paper start to finish, flag any jarring transitions, orphaned cross-references, or sections that no longer connect after the §6 cuts
2. **Internal consistency reviewer**: Check that claims in §3 match claims in §7/§8/§11; check Table 2 operational definitions still match body text; check Table 4 consciousness states still match §6
3. **Reference integrity**: Final pass — every body citation has a reference entry, every reference is cited, no duplicates, alphabetical order correct
4. **Copy editor**: Typos, grammar, formatting consistency (heading levels, bold/italic patterns, footnote style)

### THEN: Phase D — Build/Verify/Upload
- [ ] Sync .md → .tex (update paper/full/biorxiv/paper.tex from paper/full/four-model-theory-full.md)
- [ ] Rebuild LaTeX PDF into tmp/build-full/
- [ ] Run `pytest tmp/test_content_integrity.py -v`
- [ ] Run `pytest tmp/test_pdf_verification.py -v -m slow`
- [ ] Upload Zenodo v5 with changelog (document all Session 196 + 197 changes)
- [ ] Cascading impact check (cosmology paper terminology, formalization roadmaps, books)

## Key Files
- `paper/full/four-model-theory-full.md` — THE source of truth (29,126 words)
- `docs/pending-fmt-v5-revision-plan.md` — execution plan (reference, tracked by AIW-51)
- `docs/pending-fmt-v5-session197-handover.md` — previous handover (superseded by this file)

## Strategic Context
- AIW-49 BBS Seth commentary (Jun 12 deadline) — top priority after v5 upload
- AIW-62 Kanai JAIC inquiry — awaiting reply
- AIW-38 Nautilus pitch — awaiting reply
- Plan G operating envelope: May FMT budget ~24 Matthias-hours
