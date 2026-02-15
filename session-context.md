# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-15 (Session 50, complete)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Book review pass + background tasks (website cross-check, #49 content, PDF tables)

## What Was Done (Session 50)

### Book Review Pass (Completed)
1. **Full manuscript read** (~1,580 lines, 14 chapters + 3 appendices)
2. **"epiphenomenalist framework" → "dual evaluation architecture"** (line 811) — Session 43 fix never reached .md
3. **Stale TODO removed** (Appendix A glossary had `[TODO: Populate...]` above populated entries)
4. **Chapter 13: Human Virtualization restored** (background agent) — ~2,200 words recovered from Session 43 .tex + ~700 words new #49 content. Old Ch13 → Ch14. Cross-refs updated.
5. **PDF table rendering fixed** (background agent) — `tmp/build_book_pdf.py` now converts markdown pipe tables to LaTeX `longtable`. All 6 tables render correctly.
6. **Website cross-check completed** (background agent) — `tmp/website-content.md` + `tmp/website-cross-check.md`. Core ideas integrated; 5 new paper proposals identified.

### Orphan Audit (Completed)
- **Book**: CLEAN — .md is canonical and more complete than .tex
- **Full paper**: **~1,640 words orphaned in .tex** (10 items from Sessions 25+39). Needs reconciliation pass. Key orphans: expanded Prediction 8 (5 sleep sub-predictions), dual evaluation architecture rewrite, permeability nuance, identity/confabulation, 2 open questions, 3 limitations. The .md also has ~1,000 words the .tex lacks. Both files drifted in both directions.
- **Intelligence paper**: CLEAN — regenerated from .md in Session 46

### Review Findings (Not Yet Fixed)
- [FIGURE] placeholders at lines ~210, 224, 260, 344
- Ch11 "Nine Predictions" and Ch12 "Building a Conscious Machine" are thin (~24 and ~27 lines)
- Expanded predictions (~200 words each) from Session 43 .tex could bulk up Ch11 — future task
- "clock analogy for epiphenomenalism" in Notes (line 1273) — left as-is, describes the topic not the theory's position

## Canonical File Paths
- **Full paper LaTeX**: `paper/full/biorxiv/paper.tex` (DIVERGED from .md — needs reconciliation)
- **Full paper Markdown**: `paper/full/four-model-theory-full.md` (DIVERGED from .tex — needs reconciliation)
- **Full paper PDF**: `paper/full/biorxiv/paper.pdf` (54pp)
- **Full paper refs**: `paper/full/biorxiv/references.bib`
- **Trimmed paper (NoC)**: `paper/trimmed/noc/` (FROZEN — submitted 2026-02-13)
- **Intelligence paper**: `paper/intelligence/paper.md` (canonical, ~8,757 words)
- **Intelligence paper LaTeX**: `paper/intelligence/paper.tex` (CURRENT, 25pp)
- **Intelligence paper PDF**: `paper/intelligence/paper.pdf` (CURRENT)
- **Book manuscript**: `pop-sci/book-manuscript.md` (~1,580 lines, 14 chapters + 3 appendices)
- **Book .tex**: `pop-sci/book-manuscript.tex` (STALE — missing Ch13, needs regeneration from .md)

## User TODOs (Noted, Not Yet Acted On)
1. **Three guiding principles in book intro**: Occam's Razor, Copernican Principle, Leibniz's Law — add early in book (intro or Ch1). Cross-check with website content.
2. **Future publications brainstorm**: See `tmp/website-cross-check.md` Section 4 for five concrete paper proposals.
3. **Full paper .tex/.md reconciliation**: ~1,640 words in .tex not in .md + ~1,000 words in .md not in .tex. Need to merge both directions.
4. **Book .tex regeneration**: Regenerate from canonical .md (current .tex missing Ch13).
5. **Expanded predictions**: Port ~200-word prediction descriptions from Session 43 .tex to book Ch11.

## Next Steps
- Full paper .tex/.md reconciliation (priority — submitted paper is .tex, canonical is .md)
- Book: add three guiding principles (Occam, Copernicus, Leibniz)
- Book .tex regeneration + PDF rebuild
- Confirm bioRxiv DOI
- Intelligence paper → NIP submission
- Consider new paper proposals from website cross-check

## Recovery Instructions
1. Read this file
2. Session 50 work is COMMITTED and PUSHED
3. Top priority: full paper .tex/.md reconciliation (~1,640 words each way)
4. Book TODOs: three principles in intro, expanded predictions in Ch11
5. Check `tmp/website-cross-check.md` for new paper ideas
