# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-16 (Session 51, complete)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Full paper .tex/.md reconciliation + book enhancements

## What Was Done (Session 51)

### Full Paper Reconciliation (Completed — CRITICAL)
- 12 items ported from .tex into .md (canonical source)
- Key items: dual evaluation architecture rewrite, expanded Prediction 8 (5 sleep sub-predictions), permeability graded-filter evidence, identity/confabulation, 2 new open questions, 4 new limitations, substrate independence cosmological grounding
- Body word count: ~14,400 → ~16,744 words
- .tex is now STALE — needs regeneration from reconciled .md
- No automated build script exists for full paper .tex generation
- bioRxiv submission (PDF) was NOT touched — only the .md source was updated

### Book Enhancements (Completed — Background)
1. **Three Guiding Principles** added to Ch1 (~500 words): Occam's Razor, Copernican Principle, Leibniz's Law — cross-checked with website content
2. **Chapter 11 expanded** from ~24 lines to ~2,600 words: all nine predictions with pop-sci descriptions, including Prediction 8's 5 sleep sub-predictions

### AC Architecture Brainstorm (Noted)
- First architectural question for Step 8 (AC Architecture Design) documented
- Core idea: LLMs as four-model components, context windows as dynamic state
- Key open question: does frozen-weight architecture satisfy criticality, or create a "never-aging mind"?
- See docs/ac-architecture-brainstorm.md for full brainstorm

### Other
- README.md updated to reflect current project state (papers, book, roadmap)
- Highlighted review HTML created at tmp/book-review-highlighted.html
- Class 5 description corrected in book (randomness doesn't preclude computation — infinite sequences contain everything)

## Canonical File Paths
- **Full paper Markdown**: `paper/full/four-model-theory-full.md` (RECONCILED — single source of truth, ~16,744 body words)
- **Full paper LaTeX**: `paper/full/biorxiv/paper.tex` (STALE — needs regeneration from .md)
- **Full paper PDF**: `paper/full/biorxiv/paper.pdf` (bioRxiv version — NOT modified)
- **Full paper refs**: `paper/full/biorxiv/references.bib`
- **Trimmed paper (NoC)**: `paper/trimmed/noc/` (FROZEN — submitted 2026-02-13)
- **Intelligence paper**: `paper/intelligence/paper.md` (canonical, ~8,757 words)
- **Book manuscript**: `pop-sci/book-manuscript.md` (~29,000+ words, 14 chapters + 3 appendices)
- **Book .tex**: `pop-sci/book-manuscript.tex` (STALE — needs regeneration from .md)

## User TODOs (Carried Forward + New)
1. **Full paper .tex regeneration**: Regenerate from reconciled .md (no build script exists — manual or create one)
2. **Book .tex regeneration**: Regenerate from canonical .md (build script exists: tmp/build_book_pdf.py)
3. **Review highlighted book changes**: tmp/book-review-highlighted.html open in browser
4. **Full paper word count review**: Body grew from ~14,400 to ~16,744 — may need trimming for journal targets
5. **Future publications brainstorm**: See tmp/website-cross-check.md Section 4
6. **Confirm bioRxiv DOI**
7. **Intelligence paper → NIP submission**

## Next Steps
- Review highlighted book changes
- Full paper .tex regeneration (priority — currently stale)
- Book .tex regeneration + PDF rebuild
- Consider trimming full paper for Physics of Life Reviews submission
- Intelligence paper submission
- AC architecture exploration (Step 8 begins) — see docs/ac-architecture-brainstorm.md

## Recovery Instructions
1. Read this file
2. Session 51 work is COMMITTED and PUSHED
3. Full paper .md is reconciled — .tex needs regeneration
4. Book has new content in Ch1 (principles) and Ch11 (predictions) — review via tmp/book-review-highlighted.html
5. README is updated
