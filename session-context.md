# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-14 (Session 27, in progress)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Draft intelligence paper (Angle 2), write About the Author chapter, commit and push

## Current State
- **Active Task**: Session work complete. Awaiting user review.
- **Progress**: Intelligence paper drafted, About the Author chapter written, untracked files committed.
- **Pending**: User review of both drafts, conversation log update, final commit and push.

## Session 27 Summary

### 1. Selective Commit of Untracked Files
- Added .gitignore entries for `figures/book/` (regenerable) and `.serena/` (local)
- Committed utility scripts (extract_book_images.py, convert_svg.py, etc.) and paper build files
- Pushed to both remotes (commit e3caf45)

### 2. Black Rectangle Image Cleanup
- User noticed many extracted book images were black rectangles
- Identified 256 pure-black RGBA artifacts (RGB=0, alpha=255) out of 348 images
- Moved all 256 to `figures/book/2delete/` for user review
- 27 real images + 65 page renders kept
- User has NOT yet confirmed deletion

### 3. Intelligence Paper — FIRST DRAFT COMPLETE
- **File**: `paper/intelligence/paper.md`
- **Title**: "Why Intelligence Models Must Include Motivation: A Recursive Framework"
- **Target**: *New Ideas in Psychology*
- **Structure**: 7 sections + references
  1. Introduction: A Curious Omission
  2. The Status Quo (CHC, Cattell, Sternberg, Wechsler, Gardner + general pattern)
  3. Intelligence as a Recursive System (three components, recursive loop, structural claim, relation to existing work)
  4. Operational Knowledge: The Hidden Multiplier
  5. The AI Implication
  6. Discussion (testable predictions, limitations, historical note)
  7. Conclusion
- **Key research finding**: No major paper has explicitly argued that motivation's exclusion is a fundamental theoretical blind spot. Wechsler (1943) called for inclusion of non-intellective factors but was ignored.
- **Literature research agent** ran comprehensive search across 25+ sources, confirming the gap.
- **References**: ~30 citations including Cattell, CHC, Sternberg, Deci & Ryan, Stanovich, Dweck, Duckworth, Ackerman PPIK, von Stumm, Mussel, Snow, Frank, Wechsler, Binet

### 4. About the Author Chapter — FIRST DRAFT COMPLETE
- **File**: `pop-sci/book-manuscript.md` (inserted after Preface)
- **Sections**: The Math Years, The Physics Pivot, The Consciousness Turn, The Theory Crystallizes, The Decade Gap, Zero Copies, The English Rebirth
- **Theme**: Author's own life as demonstration of recursive intelligence model
- **Key narrative beats**: Self-taught math (8-11), physics pivot (11-14), consciousness turn (14+), theory at 25, decade gap, zero copies, 2026 rebirth
- **TOC updated** to include "About the Author"

## Key File Locations
- **Intelligence paper draft**: `paper/intelligence/paper.md`
- **Pop-sci book manuscript**: `pop-sci/book-manuscript.md`
- **Book outline**: `pop-sci/book-outline-expanded.md`
- **Trimmed LaTeX (SUBMITTED, do NOT modify)**: `paper/trimmed/arxiv/paper.tex`
- **Conversation log**: `docs/conversation-log.md`

## Next Steps
1. **User review** of intelligence paper draft
2. **User review** of About the Author chapter
3. **Delete figures/book/2delete/** after user confirmation
4. **Conversation log update** (Session 27)
5. **Final commit and push** to both remotes
6. **Later**: Ch. 2 Brain Anatomy, Ch. 16 Intelligence (adapt from paper)

## Recovery Instructions
1. Read THIS FILE first
2. Intelligence paper is at `paper/intelligence/paper.md` — DRAFT, needs review
3. About the Author chapter is in `pop-sci/book-manuscript.md` — DRAFT, needs review
4. Paper is SUBMITTED to NoC (2026-02-13) — do NOT modify trimmed version
5. Black rectangle images in `figures/book/2delete/` — awaiting user confirmation to delete
6. ALWAYS push to BOTH remotes: `git push origin main && git push private main`
