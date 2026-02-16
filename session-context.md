# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-16 (Session 62)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Fix bioRxiv→PsyArXiv references, add intelligence paper DOI, generate .docx, clean refs

## Current State
- **Active Task**: Session 62 COMPLETE.
- **Progress**:
  - Intelligence paper on PsyArXiv — DOI: 10.31234/osf.io/kctvg
  - Consciousness paper still awaiting PsyArXiv moderation
  - Fixed intelligence paper ref to consciousness paper: bioRxiv → PsyArXiv
  - Updated all consciousness paper copies: "forthcoming" → "Gruber, 2026" + PsyArXiv DOI (versionless)
  - Added DOI to README in 3 places (summary, detail, roadmap) with local PDF links preserved
  - Removed 4 orphaned references from trimmed paper (Block 2007, Butlin 2025, Priesemann 2014, Tagliazucchi 2016)
  - Generated .docx with 3 embedded figures: `paper/trimmed/noc/four-model-theory-noc.docx`
  - Refs now: 73 (trimmed), all verified cited

## Known Issues
- **Footnote rendering in Office 365 Online**: The `[^quantum]` footnote (von Neumann 1932, Wigner 1961, Zurek 2003 — rejecting observer-dependent QM) is correctly encoded in the .docx (word/footnotes.xml, id=53) but Office 365 Online doesn't display it / can't jump to it. Desktop Word should be fine. If NoC reviewers flag "uncited references" for von Neumann/Wigner/Zurek, this is why — convert the footnote to inline text or remove it.

## Recovery Instructions
1. Read this file
2. Consciousness paper still awaiting PsyArXiv moderation — check status, get DOI when live
3. **NEXT SESSION**:
   - When consciousness paper gets DOI: update intelligence paper ref + README
   - Add DOIs to references (time permitting)
   - Wait for PsyArXiv preprints to go live before resubmitting to NoC
   - .docx is READY at `paper/trimmed/noc/four-model-theory-noc.docx`
   - Implementation folder ready for Phase 1 work (concept extraction)
4. Do NOT resubmit to NoC until PsyArXiv preprints are confirmed live
