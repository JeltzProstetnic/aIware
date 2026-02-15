# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-15 (Session 36, in progress)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Manuscript fixes from flow review

## Current State
- **Active Task**: Manuscript fixes — all 8 edits applied
- **Progress**: All flow-review fixes applied to `pop-sci/book-manuscript.md`
- **Pending**: Commit + push, conversation log entry

## Session 36 — What Happened

### Manuscript Fixes from Flow Review — COMPLETE

Applied 8 fixes to `pop-sci/book-manuscript.md` based on `tmp/manuscript-flow-review.md`:

**Critical fixes:**
1. **Five-level hierarchy in Ch 6** (fix #3): Added paragraph after permeability gradient section explicitly mapping psychedelic mechanisms to all five levels (Electrochemical → Proteomic → Topological → Virtual), fulfilling Ch 2's promise.
2. **Six-layer bridge in Ch 9** (fix #2): Added callback to Ch 2's six-layer argument when discussing corvids, making the substrate-independence point explicit.

**Important fixes:**
3. **Sufficiency clarification in Ch 11** (fix #8): Added clause connecting the engineering specification back to Ch 5's "necessary but not sufficient" framing.
4. **Ch 4→5 transition** (fix #13): Added bridging paragraph asking what makes the architecture *run*, easing the gear shift from identity questions to computational dynamics.
5. **Preface/About overlap** (fix #6/#10): Replaced duplicate "zero copies" retelling in About the Author with a reference to the Preface ("You already know from the Preface how that went").
6. **ESM triple-coverage** (fix #7): Trimmed Ch 7 Cotard's section to reference Ch 6's mechanism ("By now, you should recognize the mechanism") rather than re-explaining from scratch.
7. **nSAI/nSU reuse** (fix #12): Added callback in Ch 11 using both abbreviations when discussing AI skepticism, so they're no longer introduced-then-abandoned.

**Minor fixes:**
8. **Notes + structure**: Fixed "random letter sequence" → "random number sequence" in Notes. Added "## Coda" heading to the concluding paragraphs.

**Already fixed in prior sessions (skipped):**
- Ch 16 dangling reference — already removed
- Tarski/Gödel error — already corrected to "Gödel's"

**Not addressed (structural/expansion work for future sessions):**
- #9: Chapter length imbalance (expanding Ch 8, 10, 11) — requires substantial new content
- #16: Ch 7 clinical section voice — cosmetic, low priority
- #18: Ch 12 overloaded — major structural change (splitting into 3 chapters)

## Open Tasks for Next Session
1. **bioRxiv submission** — follow guide in `tmp/preprint-submission-guide.md`
2. **Full LaTeX parity** — LaTeX `paper.tex` is missing substantial Markdown content
3. **Chapter expansion** — Ch 8 (split brain), Ch 10 (predictions), Ch 11 (building AC) are short
4. **Ch 12 split consideration** — could become 3 chapters (implications, free will, open questions)
5. Ongoing: arXiv endorsement, outreach emails, NoC review wait (~6 weeks from Feb 13)

## Key File Locations
- **Pop-sci book manuscript (UPDATED)**: `pop-sci/book-manuscript.md`
- **Flow review**: `tmp/manuscript-flow-review.md`
- **Full paper LaTeX**: `paper/full/arxiv/paper.tex`
- **Intelligence paper**: `paper/intelligence/paper.md`
- **Trimmed LaTeX (SUBMITTED, do NOT modify)**: `paper/trimmed/arxiv/paper.tex`

## Recovery Instructions
1. All 8 manuscript fixes are applied — verify with grep for key phrases
2. Next: commit + push, then bioRxiv submission or chapter expansion
