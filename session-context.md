# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-16 (Session 54, pre-handoff)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Prepare handoff for manual book manuscript edit pass

## Current Situation

**Matthias is doing a manual read-through + edit of the entire book manuscript.** This will take 1-2 days. When he returns, the `.md` file will have extensive changes.

## Pre-Edit Baseline Snapshot

| Metric | Value |
|--------|-------|
| **File** | `pop-sci/book-manuscript.md` |
| **Word count** | 45,018 |
| **Line count** | 1,760 |
| **MD5** | `75a2537134a24cba94ae6926f684fc2e` |
| **Last commit** | `56a315b` — Session 53: Final documentation before restart |
| **Git state** | Clean (3 untracked tmp/ files, irrelevant) |

### Chapter Structure (line numbers for reference)
```
  1  # The Simulation You Call "I"
  3  ## How Your Brain Creates Consciousness...
 13  ## Contents
 39  ## Preface: The Book That Sold Zero Copies
 57  ## About the Author
135  ## Chapter 1: The Hardest Problem in Science
211  ## Chapter 2: The Four Models
345  ## Chapter 3: The Virtual Side
425  ## Chapter 4: Why It Feels Like Something (And Why That's the Wrong Question)
533  ## Chapter 5: At the Edge of Chaos
619  ## Chapter 6: What Psychedelics Reveal
721  ## Chapter 7: What Happens When the Lights Go Out
781  ## Chapter 8: The Clinical Mirror
869  ## Chapter 9: Two Minds in One Brain
929  ## Chapter 10: The Animal Question
1027 ## Chapter 11: Nine Predictions
1151 ## Chapter 12: Building a Conscious Machine
1179 ## Chapter 13: Human Virtualization
1271 ## Chapter 14: What It Means
1401 ## Coda
1411 ## Acknowledgments
1423 ## Notes and References
1457 ## Appendix A: Basic Neurology — A Reference Guide
1510 ## Appendix B: The Intelligence Model
1610 ## Appendix C: Five Classes of Computation
```

### Session 53 Additions (most recent changes, now baked in)
1. Identity claim + H₂O analogy (Ch.4)
2. "But Couldn't the Simulation Run 'In the Dark'?" (Ch.4)
3. "Real Within the Simulation — What Does That Actually Mean?" (Ch.4)
4. "How Experience Develops: The Social Construction of the Self-Model" (Ch.10)
5. Digital twin analogy updates

### Known Issues in Manuscript Before Edit
1. Two figure placeholders remain: five-layer stack SVG + VR illustration
2. No prior review pass for flow/consistency — this is the first one
3. ~31,000→45,000 words after Session 53 additions (significant growth)

## When Matthias Returns — Recovery Plan

1. **Read this file** for context
2. **Diff the manuscript** against baseline: `git diff pop-sci/book-manuscript.md`
3. **Get word count delta**: compare new `wc -w` against baseline 45,018
4. **Ask Matthias** what he wants help with:
   - Consistency check after edits?
   - Rebuild .tex and PDF?
   - Specific sections he wants reviewed?
   - New content he added that needs polishing?
5. **Rebuild pipeline** when ready: `python3 tmp/build_book_pdf.py` to regenerate .tex and PDF
6. **CANONICAL SOURCE RULE**: The .md he edited IS the source of truth. Regenerate .tex from it, never the reverse.

## Other Project State (Unchanged)

- **Trimmed paper**: SUBMITTED to NoC 2026-02-13. Under review.
- **Full paper**: `paper/full/four-model-theory-full.md` — canonical. Tracked changes version at `paper/full/four-model-theory-full-tracked.md`.
- **Intelligence paper**: `paper/intelligence/paper.md` — draft complete, 7,858 words.
- **Preprints**: PsyArXiv + bioRxiv strategy planned. Not yet posted.

## Conversation Summary
Session 54: Brief session. Matthias announced he's about to manually edit the entire book manuscript over 1-2 days. Prepared handoff documentation with baseline metrics so we can diff and resume cleanly when he returns.
