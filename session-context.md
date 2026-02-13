# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-13 (Session 13, end)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Prediction reorder, figure polish, consolidation, figure integration

## Current State
- **Active Task**: Session complete, ready for restart
- **Progress**: All tasks completed, committed, pushed
- **Next**: Frontiers LaTeX/Word formatting, arXiv, magazine submissions, LinkedIn posting

## What Changed This Session

### Prediction Reorder
- Prediction 9 (fMRI model signatures) promoted to Prediction 1 — most direct test of the four-model architecture
- All predictions renumbered (old P1-P8 → new P2-P9)
- 12 cross-references updated in paper.md
- All 10 supporting docs updated for consistency

### Figure Polish
- **Figure 1** (four-model architecture): Green arrow shifted right 24px, blue arrow shifted left for symmetry, sensory input arrow extended to 95px from left edge. v2 promoted to canonical name, old deleted.
- **Figure 2** (real/virtual split): Ovals expanded ry 130→138, all content shifted down 30px to clear subtitle headers, "lights on/off" text split into two lines. v2 promoted, old deleted.
- **Figure 3** (phenomenological content): Declared perfect, untouched.

### Consolidation Audit
- 10 files checked, all fixed for:
  - Prediction count (8→9 everywhere)
  - Prediction numbering (new P1=fMRI order)
  - "2x2 grid" language → "two orthogonal axes"
  - Stale references

### Figure Integration
- **README.md**: All three SVG figures embedded with captions
- **pop-sci/magazine-article.html**: NEW — HTML version of magazine article with embedded figures
- **PNG versions**: All three figures converted to PNG (1720px wide, retina) for LinkedIn
- **LinkedIn post notes**: Updated with specific figure file paths

### Decision: Keep 9 Predictions
- Considered merging P2+P4 (both test permeability). Decided against — P4's standalone cross-domain impact outweighs the benefit of a round number.

## Files Modified/Created
| File | Change |
|------|--------|
| `paper.md` | Prediction reorder, all cross-refs updated |
| `README.md` | Three SVG figures embedded with captions |
| `theory.md` | Prediction count/numbering updated |
| `paper-outline.md` | Prediction count/numbering, grid language fixed |
| `cover-letter.md` | Prediction number refs updated |
| `pop-sci/magazine-article.md` | Grid language, prediction count fixed |
| `pop-sci/magazine-article.html` | NEW — HTML with embedded figures |
| `pop-sci/linkedin-post.md` | Prediction count, figure attachment notes |
| `pop-sci/book-manuscript.md` | Prediction count/numbering, grid language |
| `pop-sci/podcast-script.md` | Prediction count |
| `pop-sci/video-script.md` | Prediction count, grid language |
| `figures/figure1-four-model-architecture.svg` | Arrows repositioned (final) |
| `figures/figure2-real-virtual-split.svg` | Ovals expanded, content shifted (final) |
| `figures/*.png` | NEW — PNG versions for LinkedIn |
| `figures/figure1-four-model-architecture.md` | Grid language fixed |

## Remote Config
- `origin` → `JeltzProstetnic/aIware` (public) — ONLY push target
- All changes committed and pushed

## Open TODOs

### Immediate
- [ ] **Sync private repo** — `aIware-private` on GitHub not updated since Session 12. Push paper.md, figures, PNGs, HTML article via GitHub API (no local remote configured)
- [ ] Format paper for Frontiers LaTeX/Word template
- [ ] Check word count after Prediction 1 (fMRI) repositioning
- [ ] LinkedIn posting with PNG figures
- [ ] Render SVGs to PDF for journal submission

### Near-term
- [ ] arXiv posting (check q-bio.NC endorsement requirements)
- [ ] Self-review paper with fresh eyes
- [ ] Magazine submissions
- [ ] Submit to Frontiers in Computational Neuroscience

### Ongoing
- [ ] Book manuscript review
- [ ] Video recording
- [ ] Podcast outreach

## Recovery Instructions
1. Read THIS FILE first
2. Everything is committed and pushed
3. Paper has 9 predictions with P1=fMRI signatures (the reorder from this session)
4. All three figures are finalized SVGs, also available as PNGs
5. HTML version of magazine article exists at pop-sci/magazine-article.html
6. Cover letter at `cover-letter.md` targets Frontiers in Computational Neuroscience
