# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-14 (Session 23)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Discuss proposed additions to full paper + pop-sci book expansion

## Current State
- **Active Task**: Discussion of 5 proposed additions — DISCUSSION COMPLETE, corrections captured
- **Progress**: All 15 book page renders analyzed, full paper read, all user corrections documented
- **Pending**: Draft actual paper edits (deferred to next session or later this session)

## Session 23 Summary

### What happened:
1. Read full paper (paper/full/arxiv/paper.tex) — all sections including Limitations and Conclusion
2. Analyzed all 15 flagged book page renders (pp. 97, 189, 196, 197, 204, 209, 211, 215, 225, 234, 235, 238, 243, 251, 280)
3. Proposed placement for 5 user-requested additions
4. User provided 4 critical corrections (see below)
5. **All analysis documented in `docs/session-23-paper-expansion-notes.md`** — READ THIS FIRST in next session

### Key User Corrections (MUST PRESERVE):
1. **Criticality ≠ full stability**: Provides stable phases + radical digital breakdowns (sleep). Speculation: criticality = cellular automaton from neural activity, stable short-term, unstable long-term.
2. **Epistemic framing**: NOT "better than competitors." ONE model contributing to collective search, TOGETHER with others, not against.
3. **Page 209**: DEFINITELY in pop-sci book (confirmed, not "maybe").
4. **Pop-sci book = extra-long self-published version**: Same thing.

### Files created this session:
- `docs/session-23-paper-expansion-notes.md` — COMPREHENSIVE notes on all proposed additions, book page analysis, placement decisions, and user corrections

## Next Steps (prioritized)
1. **Draft paper additions**: 4 new Limitations paragraphs + 1 paragraph in Section 5.1 + 1 sentence in Introduction
2. **Discuss intelligence theory** (p.243) — user flagged for separate discussion (Session Context TODO #3)
3. **Pop-sci book outline** incorporating all deferred content
4. **Update conversation log** with Session 23

## Key File Locations
- **Session 23 expansion notes**: `docs/session-23-paper-expansion-notes.md`
- Full LaTeX: `paper/full/arxiv/paper.tex`
- Trimmed LaTeX: `paper/trimmed/arxiv/paper.tex`
- Pop-sci manuscript: `popsci/` (TBD — may need creation)
- Book page renders: `figures/book/book_page_*_render.png`

## Compile Commands
- **LaTeX trimmed**: `cd paper/trimmed/arxiv && pdflatex -interaction=nonstopmode paper.tex`
- **LaTeX full**: `cd paper/full/arxiv && pdflatex -interaction=nonstopmode paper.tex`

## Recovery Instructions
1. Read THIS FILE first
2. Read `docs/session-23-paper-expansion-notes.md` for all expansion analysis
3. Paper is SUBMITTED to NoC (2026-02-13) — do NOT modify trimmed version
4. Full (long) version is the target for these additions
5. ALWAYS push to BOTH remotes: `git push origin main && git push private main`

## Session 24 TODO (in priority order)
1. **Draft paper additions** to `paper/full/arxiv/paper.tex`:
   - Introduction (Section 1.3): Add epistemic humility + collaborative framing sentence
   - Section 5.1: Add paragraph on criticality as punctuated stability + multi-scale synchronization + CA speculation
   - Limitations: Add 4 new items (inside-modeling limits, language linearity, criticality-rhythm not formalized, model-is-just-a-model)
2. **Consider** behavior gradient from book p.235 for Section 3.6
3. **Consider** four-level physical hierarchy from book p.280 for Section 5 / Open Questions
4. **Discuss intelligence theory** (book p.243) — separate from consciousness theory
5. **Pop-sci book outline** incorporating all deferred content (wave interference p.209, three loops p.225, brain anatomy chapter, full philosophical arguments)
6. **Recompile** full paper and verify
7. **arXiv**: Still blocked on endorsement — check email responses
8. **Wave 2 outreach**: Metzinger, Carhart-Harris, Priesemann — drafts ready, NOT SENT
