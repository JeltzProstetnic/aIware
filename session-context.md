# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-20 (Session 85)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Power outage recovery + B&W illustration conversion for POD print

## What Session 85 Did
1. Power outage recovery — verified all git state clean, both remotes up to date
2. Backfilled Session 84 in `docs/conversation-log.md`
3. **B&W figure conversions for print** (all 3 existing + 2 new):
   - `figure1-four-model-architecture-bw.svg/png` — grayscale version of four-model diagram
   - `figure2-real-virtual-split-bw.svg/png` — grayscale version of real/virtual split
   - `figure3-phenomenological-content-bw.svg/png` — grayscale version of phenomenological content
   - `figure-five-layer-stack-bw.svg/png` — **NEW** figure (was placeholder)
   - `figure-penfield-homunculus-bw.svg/png` — **NEW** figure (was placeholder)
4. Updated `book-manuscript.md` to reference B&W figures
5. Fixed figure1 duplication bug in build script (was inserted via both markdown AND FIGURE_INSERTIONS)
6. Rebuilt PDF — 251 pages, 5 figures, all B&W

## Current Stats
- Chapters: 16, ~62,331 words
- Pages: 251 (US Trade 6"x9")
- Figures: 5 (all B&W grayscale)
- Content: PRINT-READY (text-level)

## Remaining Placeholders
- Line ~380: `[FIGURE: SDXL/Flux...]` — AI-generated image of simulation looking at itself. Needs external generation (Flux/SDXL on RTX 4090).

## User-Declared Roadmap (This Session)
1. ~~B&W illustrations~~ **DONE** (this session)
2. **Cover image hi-res**: User will provide later
3. **Table review**: User wants to go over ALL tables — "none are perfect yet"
4. **Full review round**: Over the whole book
5. **Publish**: KDP + IngramSpark + Payhip
6. **German version**: Create after English publication

## Submission Status
- NoC: RESUBMITTED, awaiting feedback
- SSRN: SUBMITTED, awaiting acceptance
- Zenodo cosmology: PUBLISHED (DOI: 10.5281/zenodo.18698606)
- PsyArXiv intelligence: PUBLISHED (https://osf.io/preprints/osf/kctvg)

## Recovery
1. Read this file + MEMORY.md
2. Book: `pop-sci/book-manuscript.md` — content source of truth
3. PDF: `pop-sci/book-manuscript.pdf` — current (251 pages, B&W figures)
4. Next: table review round, then full book review, then publish
