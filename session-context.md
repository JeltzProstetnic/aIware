# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-24T15:00:00+01:00 (Session 109)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Fix FMT PDF, update DOIs, strengthen TDA tests, draft commentary

## Current State
- **Active Task**: None — session complete
- **Progress (this session)**:
  - Fixed broken FMT PDF (51 `??` instances — bibtex sandbox failure + deleted .bbl)
  - Fixed missing comparison table (Table 4 — stale float injection anchor)
  - Fixed duplicate assessment criteria text in PDF
  - Fixed missed unlettered `Gruber (2026)` → `Gruber (2026a)` on line 673
  - Strengthened TDA tests: exact table count, zero `??` tolerance, new cite-key↔bib test
  - Updated TDA rules: Tier 4 tests mandatory after EVERY PDF build
  - Updated all DOIs to concept DOIs (FMT: 18669891, cosmology: 18698605)
  - COGITATE commentary draft: `tmp/cogitate-commentary-draft.md` (~2,500 words, needs trim to 1,500)
  - Bochum abstract: `tmp/bochum-abstract.txt` (699 words)
  - Sessions 107+108 logged to conversation-log.md
- **Pending**:
  - USER ACTION: Upload FMT v2 to Zenodo (PDF fixed, 104/104 tests pass)
  - Intelligence paper waiting for PsyArXiv moderator
  - Trim COGITATE commentary to 1,500 words (NoC Spotlight Commentary limit)
  - Submit Bochum abstract to franziska.klasen@rub.de (deadline Apr 1)
  - Commentary submission to NoC via ScholarOne
  - Cosmology → SSRN PhysicsRN

## Recovery Instructions
1. FMT PDF is FIXED — upload to Zenodo
2. Commentary draft needs 1,500-word trim for NoC Spotlight Commentary
3. Bochum abstract ready for email submission
4. bibtex MUST run with dangerouslyDisableSandbox (sandbox blocks .bbl writes)
5. After ANY PDF build, run: `pytest tmp/test_content_integrity.py tmp/test_pdf_verification.py -v`
