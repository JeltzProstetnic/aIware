# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-24T23:30:00+01:00 (Session 111)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Analyze two new consciousness preprints, draft & send outreach emails

## Current State
- **Active Task**: None — session complete
- **Progress (this session)**:
  - Analyzed McFarnell (2026) "Affective Control under Uncertainty" (Zenodo, 32pp) — two-level theory, Level 2 self-model maps to FMT's ESM, missing world-model dimension
  - Analyzed Kob & Marvan (2026) "Pluralism within limits" (PsyArXiv, 25pp) — NCC pluralism desiderata that FMT fulfills perfectly (two-factor, finite kinds, systematic ordering)
  - Full analysis written to `tmp/paper-analysis-mcfarnell-kob-2026.md`
  - Drafted two outreach emails: `tmp/outreach-drafts-mcfarnell-kob.md`
  - User SENT both emails (McFarnell + Kob)
  - Updated outreach master list: both contacts added to ALREADY CONTACTED section
  - PDFs saved: `tmp/mcfarnell-2026.pdf`, `tmp/kob-marvan-2026.pdf`
- **Pending**:
  - **Bochum registration by May 30** — register at RUB external site
  - Trim COGITATE commentary to 1,500 words (NoC Spotlight Commentary limit)
  - Commentary submission to NoC via ScholarOne
  - Cosmology → SSRN PhysicsRN
  - Awaiting responses from: McFarnell, Kob, Phil Psych editorial, NoC reviewers, Melloni, Kanai, Lau, Biyu He, + others

## Recovery Instructions
1. Check for responses to McFarnell and Kob emails
2. COGITATE commentary draft at `tmp/cogitate-commentary-draft.md` needs 1,500-word trim
3. Intelligence paper awaiting Phil Psych editorial decision (~5 months)
4. bibtex MUST run with dangerouslyDisableSandbox (sandbox blocks .bbl writes)
5. After ANY PDF build, run: `pytest tmp/test_content_integrity.py tmp/test_pdf_verification.py -v`
