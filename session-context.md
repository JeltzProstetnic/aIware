# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-15 (Session 40, complete)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Final pre-flight audit of long paper before bioRxiv submission — DONE

## Current State
- **Active Task**: COMPLETE — all 5 audit checks passed, 3 citation fixes applied
- **Paper status**: `paper/full/arxiv/paper.tex` — 53 pages, compiles cleanly, bioRxiv-ready
- **Build**: `cd paper/full/arxiv && bibtex paper && pdflatex paper.tex && pdflatex paper.tex`

## What Was Done
1. Citation audit — all keys match bib entries; fixed 3 plain-text citations (Weiskrantz, Anton, Aldrich)
2. Internal consistency — all Section~/Table~/Prediction~ refs correct
3. Overclaims — 3 mild flags reviewed and accepted by author
4. Abstract — accurate after Session 39 additions
5. bioRxiv requirements — paper ready as-is, no reformatting needed

## bioRxiv Submission (for Matthias to do manually)
- Upload `paper/full/arxiv/paper.pdf` to https://submit.biorxiv.org/
- Category: Neuroscience, Type: New Results
- License: CC-BY-NC-ND recommended
- Confirm arXiv withdrawal first

## Next Session Plan (Session 41)
1. Book manuscript edits (48 feedback items from `tmp/book-feedback-session37.md`)
2. Short/long paper comparison session
3. PsyArXiv submission (if desired)

## Key File Locations
- **Long paper**: `paper/full/arxiv/paper.tex` (the bioRxiv target)
- **References**: `paper/full/arxiv/references.bib`
- **Trimmed paper**: `paper/trimmed/arxiv/paper.tex` (NoC submission, under review)
- **Feedback log**: `tmp/book-feedback-session37.md` (48 items)
- **Book manuscript**: `pop-sci/book-manuscript.md`
- **Intelligence paper**: `paper/intelligence/paper.md`

## Recovery Instructions
1. Read this file for orientation
2. Read `docs/conversation-log.md` Session 40 entry for audit details
3. Paper is in clean, compilable state — no pending edits
4. bioRxiv submission is manual (author does it at submit.biorxiv.org)
5. Next work: book manuscript feedback items
