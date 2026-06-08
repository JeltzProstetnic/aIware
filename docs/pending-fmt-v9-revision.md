Action: reference
Tracked-by: AIW-73

# FMT v9 Revision — Session Handoff

Paper is at v8 (Zenodo DOI: 10.5281/zenodo.20448177). v9 consolidates new citations, inbox additions, and remaining reviewer-flagged items.

## Execution order (suggested)

### Pass 1: New citations + converging evidence (~1 session)
1. **Converging fMRI evidence for Prediction 1 (2×2 dissociation)** — add to §8 or new §8.x:
   - Fox et al. 2005 (PNAS): DMN vs dorsal attention anti-correlation = self/world axis
   - Dehaene et al. 2001 (Neuron): subliminal local vs conscious global ignition = implicit/explicit axis
   - Rameson, Satpute & Lieberman 2010 (NeuroImage): explicit 2×2 fMRI crossing implicit/explicit × self/non-self, partial confirmation
   - Northoff et al. 2006 (NeuroImage): self = cortical midline structures
   - Doyon et al. (motor learning): cerebellum/striatum implicit vs hippocampus/prefrontal explicit
   - Frame: both axes independently well-established, one partial 2×2 exists, but nobody has run all 4 cells in FMT framework
2. **Tucker/Luu/Friston "Criticality of Consciousness"** (Entropy 2025) — direct FMT validation, cite in §3.7 or §8
3. **Toker et al.** (Nat Neurosci 2026) — adversarial AI on 680K recordings, cite in §8
4. **Seth/Mediano IIT critique** (arXiv 2604.11482) — Phi undefined, cite + engage in §7 comparative
5. **Milinkovic & Aru "Biological Computationalism"** (NBSR 2026) — substrate neutrality bar, cite + engage in §7
6. **Bach "Machine Consciousness Hypothesis"** — self-simulation convergence, cite in §7.3

### Pass 2: Prediction refinements (~0.5 session)
7. **Thalamus strengthening**: Chowdhury already at 3 locations — upgrade wording from "consistent" to CONFIRMED prediction, add thalamus-as-negotiation-hub interpretation, evaluate as 6th confirmed prediction
8. **Prediction 4 (anosognosia) permeability caveat**: "psilocybin increases implicit-to-explicit permeability, which COULD restore deficit awareness — but only if the damaged areas remain structurally capable of participating in the permeability increase"

### Pass 3: Reviewer-flagged structural items (~1 session)
9. **Operational definitions table** (AICE R7-1): subsection or table in §3 mapping each term (self-simulation, self-referential closure, implicit model, explicit model, criticality) → measurable observables
10. **Novelty claim** (AICE Rm-2): one paragraph in §1.3 or §7.4 — novel contribution = specific combination + two-level ontology + criticality requirement + 4 unique predictions. Address "just a combination" objection directly.

### Pass 4: Section rewrites (~1-2 sessions)
11. **§6.3 REM rewrite**: Siclari 2017/2021 (hot-zone dreaming), Nir & Tononi 2010, Dresler, Voss. Acknowledge NREM dreaming. Andrillon flagged at NoC — still unfixed.
12. **Criticality neural signature**: commit §3.7 to specific κ/τ/α. Distinguish PCI from criticality.
13. **Prediction 3 de-reify**: drop "DMN = ESM network", replace with cosine-distance formulation (d ≥ 0.5)
14. **§3.7.2 phosphenes**: kill or heavily qualify
15. **Figures**: add 2×2 architecture (use `figures/figure2-real-virtual-split-simple.svg`) + 5-system hierarchy. Paper currently has zero figures.
16. **§6.5 animal consciousness** (AICE R7-8/R7-9): map software-like operations to animal empirical correlates
17. **Zombies/Mary/Frankish**: expand §4.2 from 1 sentence each → 1 paragraph each

### Pass 5: GAN investigation (independent, can parallel)
18. **GAN architecture** (cortex/basal ganglia adversarial dynamics): theoretical investigation from `~/social/tmp/theoretical-notes-thalamus-gan-2026-06-03.txt`. If solid, add as new section. If not, park.

### Pass 6: Polish + build (~0.5 session)
19. Quality cuts: §4.3 redundancy, OQ7 holography (~500w), triple-stated LLM argument
20. Citation pass 2024-26: remaining gaps (Shew, Priesemann, Plenz, Aru-Suzuki-Larkum, Seth & Bayne, Kleiner, Tsuchiya & Saigo, Lau/Michel/LeDoux, Dehaene, Metzinger, Frankish)
21. Editor quick fixes: OQ2 delete, dissolves→addresses, prune self-citations 27→≤5, operationalize predictions, drop [^quantum], abstract ≤250w
22. Rebuild LaTeX PDF, verify no regressions, upload Zenodo v9

## Total estimate
4-5 focused sessions. Passes 1-2 are fastest wins (citations + prediction fixes). Pass 3 adds empirical credibility. Pass 4 is the heavy lift. Pass 6 is mechanical.

## Files
- Paper .md: `paper/full/four-model-theory-full.md`
- Paper .tex: `paper/full/biorxiv/paper.tex`
- Build: copy biorxiv/ to tmp/build-full/, pdflatex ×3 + bibtex (dangerouslyDisableSandbox for bibtex)
- AICE review mapping: `tmp/aice-review-mapping.md`
- Internal review: `docs/pre-zenodo-v5-review-2026-04-16.md`
- GAN notes: `~/social/tmp/theoretical-notes-thalamus-gan-2026-06-03.txt`
- Prediction framing lessons: `.claude/knowledge/prediction-framing.md`
