# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-23T19:35Z (Session 107)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Update all three preprints (FMT, Intelligence, Cosmology)

## What Was Done This Session

### 1. FMT Full Paper Fixes
- Fixed "Anthropic, 2026" → "Anthropic, 2025" in .md (line 724)
- Fixed "Algom & Shriki, 2025" → "Algom & Shriki, 2026" in .md (line 221)
- Fixed build script (`tmp/build_fmt_full_pdf.py`):
  - `_SURNAME` regex now handles CamelCase names (McClelland, LaBerge)
  - `_AUTHORS_AMP` and possessive patterns handle "and" (not just "&")
  - `_lookup_key` normalizes "and" → "&" for dictionary lookups
  - Added 12 fallback citation key mappings for org-name edge cases
  - Result: 0 bibtex warnings, 0 unresolved refs (was 12 missing keys)
- Rebuilt: 60pp, 18,844 words, 0 `??`

### 2. Intelligence Paper Fixes
- Changed `Gruber (submitted)` → `Gruber (2026)` at lines 147, 303
- Applied same build script fixes (and/&, CamelCase, lookup normalization)
- Rebuilt: 25pp, 8,581 words, 0 `??`
- **Known formatting issue**: paragraph starting "Conversely, the model predicts that motivation-enhancing interventions—environments" extends over blockquote text width. Cosmetic, needs investigation next session.

### 3. Cosmology Paper Fixes
- Added missing Cook (2004) reference (cited line 102, was absent)
- Removed 3 orphan references: Albantakis (2023), Chalmers (1995), Wetterich (2022d)
- Rebuilt: 32pp, 11,630 words, 0 `??`

### 4. Full vs Trimmed FMT Comparison
- Full: ~17,500 body words; Trimmed: ~9,500 — nearly double
- Key content only in full: Libet reinterpretation, cognitive learning argument, cortical automaton, five-system hierarchy, holography-criticality nexus, full sleep architecture prediction
- Trimmed is strict content subset (adds only figure refs, CoI, author contributions)

### 5. Tests
- 144/144 pass (content integrity + build scripts, Tier 1-3)

## Pending — Next Session
1. **Upload preprints**: All 3 papers ready for upload
   - FMT full → Zenodo (new version, DOI: 10.5281/zenodo.18669891)
   - Intelligence → PsyArXiv (new version, DOI: 10.31234/osf.io/kctvg)
   - Cosmology → Zenodo (new version)
2. **Fix intelligence paragraph formatting** — "Conversely..." paragraph width issue
3. **Bochum poster abstract** — 700 words, deadline Apr 1

## Recovery Instructions
1. Read this file
2. All 3 PDFs are built and ready in canonical locations
3. Upload to Zenodo/PsyArXiv using browser or API
4. Investigate intelligence formatting issue (line 264 in paper.tex)
