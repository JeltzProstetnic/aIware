# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-15 (Session 44, complete)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Paper directory cleanup + reorganization

## What Was Done (Session 44)
- Renamed `paper/full/arxiv/` → `paper/full/biorxiv/` (git mv, preserves history)
- Deleted 17 git-tracked stale files: duplicate figures, old PDF builds, withdrawn arXiv trimmed version, consumed tmp artifacts, one-time scripts
- Deleted 3 untracked one-time scripts from tmp/
- Total: 20 files removed, 1 directory renamed, 1 directory deleted

## Canonical File Paths (IMPORTANT — changed this session)
- **Full paper LaTeX**: `paper/full/biorxiv/paper.tex` (was `paper/full/arxiv/paper.tex`)
- **Full paper PDF**: `paper/full/biorxiv/paper.pdf` (canonical, bioRxiv submission)
- **Full paper Markdown**: `paper/full/four-model-theory-full.md`
- **Full paper refs**: `paper/full/biorxiv/references.bib`
- **Trimmed paper (NoC)**: `paper/trimmed/noc/` (FROZEN — submitted 2026-02-13)
- **Intelligence paper**: `paper/intelligence/paper.md` (canonical, 7,400 words, NIP-ready)
- **Intelligence paper LaTeX**: `paper/intelligence/paper.tex` (STALE — needs regeneration from .md)
- **Intelligence paper PDF**: `paper/intelligence/paper.pdf` (STALE — needs regeneration)
- **Book manuscript**: `pop-sci/book-manuscript.md` (~33,000 words)

## Next Steps (Prioritized)

### 1. Appendix B (intelligence model)
- Condense intelligence paper into ~2,000-3,000 word appendix for book
- Intelligence paper now finalized, so this is unblocked

### 2. Intelligence paper → LaTeX + NIP submission
- Regenerate `paper/intelligence/paper.tex` from polished .md (the current .tex predates Session 43 edits)
- NIP accepts LaTeX (elsarticle class) — no need for .docx
- Compile PDF
- AI tools declaration for cover letter
- Submit to New Ideas in Psychology

### 3. Computation classes discussion
- 5-class vs 4-class Wolfram
- Scope: book-only or feed back into paper?

### 4. Structural book decisions
- Split Chapter 7 at Clinical Mirror?
- Expand Chapter 8 (split-brain)?
- Two illustrations needed (inside simulation, Game of Life five-class)

### 5. Check bioRxiv upload status

## Recovery Instructions
1. Read this file
2. Note the new canonical paths (biorxiv/ not arxiv/)
3. Next action: Write Appendix B from intelligence paper + regenerate intelligence paper.tex
4. Intelligence paper at paper/intelligence/paper.md (7,400 words, polished)
5. Intelligence paper.tex is STALE — must be regenerated before submission
6. Review reports at tmp/paper-vs-book-reconciliation.md and tmp/book-flow-review.md
