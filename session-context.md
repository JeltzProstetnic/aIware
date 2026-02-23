# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-23T17:00Z (Session 106)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Implement Test-Driven Authoring (TDA) protocol

## What Was Done This Session

### Test-Driven Authoring Protocol — Full Implementation
Implemented the 4-tier content integrity test architecture:

**Tier 1 — Structural Parity (12 tests)**: Section/subsection counts match .md vs .tex, section titles preserved, table/figure counts match, unnumbered sections present, no empty sections.

**Tier 2 — Content Volume Guards (7 tests)**: Body word counts in calibrated ranges (FMT: 13k-21k, Intel: 5.5k-10.5k), reference counts, citation command minimums, bold/italic ratios.

**Tier 3 — Canary Phrases (73 tests)**: 41 FMT canaries + 32 Intel canaries — hand-picked phrases from every section that must survive .md→.tex conversion. Covers float anchors, special characters (&, umlauts, em dashes), core theoretical terms.

**Tier 4 — PDF Verification (11 tests)**: Page count ranges, text extraction, section headings in PDF text, no unresolved refs (??), images present, no blank pages. FMT PDF currently unreadable by PyMuPDF (0 pages despite 400KB) — tests skip gracefully.

### Infrastructure
- `tmp/conftest.py` — shared fixtures (build modules, .md/.tex readers, generated .tex)
- `tmp/test_content_integrity.py` — 92 Tier 1-3 tests
- `tmp/test_pdf_verification.py` — 11 Tier 4 tests
- `tmp/update_test_baselines.py` — calibration script
- `~/.claude/rules/test-driven-authoring.md` — TDA rule file
- Updated `~/.claude/CLAUDE.md` — TDA in rule loading table
- Updated `~/claude-config/global/rules/publication-workflow.md` — test step in checklist + Section 9

### Test Results
- Existing 52 build script tests: PASS
- New 92 content integrity tests: PASS
- New 5 intel PDF tests: PASS (6 FMT skipped — unreadable PDF)
- Combined 144 tests in 0.26s

### User Request (end of session)
Compare the FMT and intel paper .tex versions before and after build scripting. Existing comparison files may be at `tmp/{fmt,intel}-{ORIGINAL,GENERATED}.{tex,pdf}`.

## Files Modified This Session
- `tmp/conftest.py` (NEW)
- `tmp/test_content_integrity.py` (NEW)
- `tmp/test_pdf_verification.py` (NEW)
- `tmp/update_test_baselines.py` (NEW)
- `tmp/test_build_scripts.py` (fixtures extracted to conftest)
- `~/.claude/rules/test-driven-authoring.md` (NEW)
- `~/.claude/CLAUDE.md` (TDA row added)
- `~/claude-config/global/rules/publication-workflow.md` (checklist + Section 9)

## Recovery Instructions
1. Read this file
2. Tests: `python3 -m pytest tmp/test_build_scripts.py tmp/test_content_integrity.py -v -m "not slow"` → 144 pass
3. Tier 4: `python3 -m pytest tmp/test_pdf_verification.py -v -m slow` → 5 pass, 6 skip
4. Calibration: `python3 tmp/update_test_baselines.py`
5. **Next**: Compare pre/post build script .tex versions (user request)
6. Existing comparison files: `tmp/{fmt,intel}-{ORIGINAL,GENERATED}.{tex,pdf}` and `tmp/comparison-{fmt,intel}.html`
