# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-24T21:00:00+01:00 (Session 110)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Color bubble diagram, Bochum abstract PDF + submission, session wrap-up

## Current State
- **Active Task**: None — session complete
- **Progress (this session)**:
  - Created canonical color bubble diagram: `figures/figure2-real-virtual-split-simple.{svg,png}` (color, no insight box)
  - Recorded in MEMORY.md: "bubble diagram" = this file for all future references
  - Updated `tmp/bochum-abstract.tex` to use color figure, recompiled PDF (3 pages)
  - Created Gmail draft for Bochum submission → USER SENT to franziska.klasen@rub.de
  - Updated outreach master list: Bochum abstract marked SUBMITTED Feb 24
- **Pending**:
  - **Bochum registration by May 30** — register at RUB external site
  - Intelligence paper waiting for PsyArXiv moderator
  - Trim COGITATE commentary to 1,500 words (NoC Spotlight Commentary limit)
  - Commentary submission to NoC via ScholarOne
  - Cosmology → SSRN PhysicsRN

## Recovery Instructions
1. Bochum abstract SUBMITTED — track registration deadline May 30
2. COGITATE commentary draft at `tmp/cogitate-commentary-draft.md` needs 1,500-word trim
3. Intelligence paper awaiting PsyArXiv moderator (no action needed)
4. bibtex MUST run with dangerouslyDisableSandbox (sandbox blocks .bbl writes)
5. After ANY PDF build, run: `pytest tmp/test_content_integrity.py tmp/test_pdf_verification.py -v`
