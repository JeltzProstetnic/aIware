# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-23T17:30Z (Session 106)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: TDA implementation → preprint comparison

## What Was Done This Session

### Test-Driven Authoring Protocol — Implemented
4-tier content integrity test architecture: 144 tests passing (Tier 1-3 + existing build tests). See commit b648a89.

### Publication Workflow Rule Update
Section 5 rewritten: machine review (tests, source diffs) = Claude's job; visual review (PDF, Word) = user's job. Version comparisons always delivered as compiled PDFs, never source diffs.

### Preprint Comparison — In Progress
Preparing side-by-side comparison of three preprints (as published) vs current local versions:
1. FMT paper — Zenodo (DOI: 10.5281/zenodo.18669891)
2. Intelligence paper — PsyArXiv (https://osf.io/preprints/osf/kctvg), DOI is version-specific (_v1)
3. Cosmology paper — Zenodo

## Recovery Instructions
1. Read this file
2. Tests: `pytest tmp/test_build_scripts.py tmp/test_content_integrity.py -v -m "not slow"` → 144 pass
3. Preprint comparison: download preprint PDFs, compile current local PDFs, open all for user
