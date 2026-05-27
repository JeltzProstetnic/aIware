# Final Pre-Zenodo Review — paper.tex (build-highlighted)

Review date: 2026-05-27

## 1. Dangling References

**All section references verified correct.** Every `Section~N`, `Section N.N`, and `\S N.N` points to an existing section. Specific checks:

- Section~7.4 (line 100) -> Summary of Comparative Advantages (line 916) -- EXISTS
- Section~5.2 (line 340) -> Holographic Storage (line 697) -- EXISTS
- Section~6.1 (line 341) -> Psychedelic Phenomenology (line 750) -- EXISTS
- Section 6.2 (line 339) -> Anesthesia and Clinical Disorders (line 777), DID discussed at line 792 -- EXISTS
- Section~8.4 (lines 1049, 1082) -> Prediction 3: DID (line 985) -- EXISTS
- Section~4.4 (line 1051) -> Substrate Independence (line 662) -- EXISTS
- \S7.2 (lines 878, 909) -> Theory-by-Theory Comparison (line 885) -- EXISTS
- \S3.4 (line 551) -> Virtual Qualia (line 346) -- EXISTS
- \S2 (line 880) -> Eight Requirements (line 115) -- EXISTS
- `\ref{tab:theory-comparison}` (lines 849, 1119) -> label at line 857 -- EXISTS
- `\ref{tab:empirical-handles}` -> label at line 251 -- EXISTS
- Table 5 (line 847) -> Theory Comparison table (5th table in document) -- EXISTS

**FIXED: Missing spaces after section numbers.** Five instances of `Section~Ntext` (no space between number and following word) would render as "Section 2develops" in PDF output:
- Line 84: `Section~2develops` -> `Section~2 develops`
- Line 110: `Section~2establishes`, `Section~3presents`, `Section~6demonstrates`, `Section~7provides`, `Section~8presents` -> spaces added
- Line 485: `Section~8but` -> `Section~8 but`
- Line 847: `Section~2are` -> `Section~2 are`
- Line 1108: `Section~8are` -> `Section~8 are`

## 2. Citation Integrity

**All 160 unique citation keys verified present in references.bib.** No missing keys. No orphan `\cite` commands. No risk of `[?]` output.

## 3. Abstract Accuracy

The abstract accurately describes the paper's current contents:
- Eight requirements: listed correctly
- Five principles: listed correctly (criticality, virtual qualia, redirectable ESM, variable permeability, simulation forking)
- Phenomena unified: correctly listed (psychedelics, anesthetics, dreams, split-brain, DID, animal consciousness)
- Four novel predictions: correctly described (two named explicitly)
- Convergence evidence: correctly enumerated with citations

**FIXED: "digital constructs"** (abstract line 44). The body consistently uses "computational-level properties" or "virtual constructs" -- never "digital." Changed to "virtual constructs" for terminological consistency. "Digital" could invite misreadings about discrete vs. continuous computation.

## 4. Conclusion Accuracy

The conclusion accurately matches the body:
- Open questions list (line 1125): all 6 items match the numbered items in Section 9
- Prediction descriptions (line 1121): all 4 predictions correctly summarized with correct Prediction numbers
- Convergence evidence summary: correctly identifies shared territory with other criticality-based frameworks
- Evidential status caveat (line 1127): correctly notes the 2015 self-published provenance

## 5. Internal Contradictions

### FIXED: "dissolution" vs "transformed"

**The issue:** Line 369 used "The dissolution:" as a subheading for the Hard Problem treatment. But line 411 explicitly states "The Hard Problem is not dissolved; it is transformed." The scoring footnote (line 877) says "a reframing rather than a dissolution." The abstract and conclusion both use "addresses" and "revealing a category error" -- consistent with reframing, not dissolution.

**The fixes:**
- Line 369: "The dissolution:" -> "The reframing:"
- Line 584: "broader dissolution of the Hard Problem" -> "broader treatment of the Hard Problem"

Now consistent throughout: the paper addresses/transforms/reframes the Hard Problem, never claims to dissolve it.

### FIXED: "single parameter" vs "family of boundary properties"

**The issue:** Table 1b (line 266) explicitly states permeability is "a family of boundary properties, not a single parameter." But line 927 said "variable implicit-explicit permeability as a single-parameter mechanism" and line 96 said "under one parameter." These directly contradict the Table 1b revision.

**The fixes:**
- Line 927: "single-parameter mechanism" -> "unified mechanism"
- Line 96: "under one parameter" -> "under one principle"

Now consistent: permeability is described as a single *principle* (correct -- one theoretical mechanism) but not a single *parameter* (which would be wrong -- it varies by channel, region, and histology).

### No contradiction found: "four discrete models" vs "continuous model space"

The paper already handles this correctly. Section 3.2 (line 302) explicitly explains the "principled minimum" framing: "four is the floor, not the ceiling" and "extremal points in a continuous space." No other passage contradicts this framing.

## Items Requiring Author Decision

None found. All issues identified were clear-cut inconsistencies (terminology drift, missing spaces) that I fixed directly. No ambiguous cases requiring judgment calls.

## Summary

| Category | Issues Found | Fixed | Needs Author |
|----------|-------------|-------|-------------|
| Missing spaces | 5 instances (8 individual fixes) | 8 | 0 |
| Citation integrity | 0 | -- | 0 |
| Abstract accuracy | 1 ("digital") | 1 | 0 |
| Conclusion accuracy | 0 | -- | 0 |
| Internal contradictions | 2 (dissolution/transformed, single-parameter/family) | 4 | 0 |
| **Total** | **8** | **13 edits** | **0** |
