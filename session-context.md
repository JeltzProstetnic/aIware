# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-19 (Session 75)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Abstracts check, Zenodo submission, README refresh

## Current State
- **Active Task**: Session complete — restart requested
- **Abstracts**: Checked all 7 papers. Fixed cosmology paper abstract ("I propose" → "This paper proposes"). Updated preprint submission guide with current physics-framed abstract.
- **Zenodo**: Cosmology paper submitted. DOI: 10.5281/zenodo.18698606
- **README**: Fully refreshed (cosmology Zenodo DOI, NoC resubmitted status, session count 74, removed "First Draft" label from Paper 3)
- **NoC**: Submitted, awaiting reviewer feedback (no action needed)

## What Session 74 Did

### Track 1: Cosmology Preprint
1. Researched 10+ preprint servers — ranked SSRN PhysicsRN #1, Zenodo #2, Preprints.org #3
2. Prepared submission guide: `tmp/preprint-submission-guide.md` (metadata, keywords, step-by-step for both platforms)
3. **RETITLED cosmology paper**: "Emergent Spacetime from Self-Referential Computation: A Hierarchical Cellular Automaton Framework" (removed "consciousness" — physicist repellent)
4. Rebranded entire paper: 19 changes replacing "consciousness" framing with "self-referential computation" — physics content untouched
5. Rebuilt cosmology PDF (261KB)

### Track 2: Book Pipeline
6. **Deep editorial review** (opus): `tmp/book-review-session74.md` (403 lines). Verdict: "First half is among the best pop-sci writing on consciousness I have encountered." Weaknesses are structural, not substantive.
7. All 5 Perplexity issues verified (em-dashes, Ch 4 defensive loop, Ch 15-16 wall, repetition, Ch 7 undercooked)
8. **Merged Ch 12+13** into "Chapter 12: From Machines to Minds" (~5,600 words combined). Book now 15 chapters.
9. Renumbered all subsequent chapters + updated cross-references + Notes section
10. **Removed parenthetical re-glossing** after Ch 5 (2 instances found — manuscript was already clean)
11. **New Coda** (~800 words): Identity argument with personal experiences (avalanche, knockout, 4D fractal, age argument, quantum immortality). Ends: "Be nice to everyone. They might all be you."
12. Rebuilt book PDF (0.9 MB), copied to Desktop
13. Updated README.md (new paper title, 15 chapters, submission status)

## NEXT SESSION — Priorities

### 1. SSRN PhysicsRN Submission
- Submission guide at `tmp/preprint-submission-guide.md`
- Abstract is finalized (physics-framed, no "I" start)
- Zenodo already done (DOI: 10.5281/zenodo.18698606)

### 2. Book Edits (from Session 74 review)
1. **Expand Ch 7** (Sleep/Anesthesia) — needs ~1,500 words: personal anecdote, falling-asleep phenomenology, hypnagogia. USER INPUT NEEDED for personal stories.
2. **Restructure Ch 14-15** (old 15-16, cosmology chapters) — split Ch 14 in two, move particles-as-atoms to appendix, add analogies. MAJOR effort.
3. **Em-dash pass** — reduce ~40% (from 19.5/1k to 10-12/1k). Systematic, mechanical.
4. **Reframe Ch 4** objection-rebuttal structure — from defensive to constructive
5. **Add analogies/anecdotes** to back half (review says front half has 1 per 1,000-1,500 words; back half drops to 1 per 3,000+)

### Also pending (book)
- Review HTML for author to scan highlighted changes
- Verify chapter transitions at act breaks (especially Ch 12→13, Ch 13→14)
- Address jargon gaps (supervenience, computationally irreducible, Bekenstein bound, CPT flip, AdS/CFT)

### 3. Intelligence Paper
- Trim ~358 words, highlights, .docx, submit to *New Ideas in Psychology*

## Parked TODOs

### Publications
- Intelligence paper: trim ~358 words, highlights, .docx, submit to *New Ideas in Psychology*
- NoC resubmission (trimmed paper .docx ready)
- Outreach emails (3 ready to send: Priesemann, Metzinger, Carhart-Harris)
- **Wetterich contacted** — waiting for reply
- Computational atoms insight — separate short paper?

### Research
- **Perplexity findings → FMT formalization**: What do Wetterich, Levin-Wen, and QCA/QFT results mean for the mathematical formalization of the four-model theory?

### Infrastructure (low priority)
- Papers 1 and 3 need build scripts (.tex currently hand-maintained)
- Update Claude Code
- Deploy on other machines

## Recovery Instructions
1. Read this file. Next priorities: expand Ch 7, restructure Ch 14-15, em-dash pass.
2. Book manuscript: `pop-sci/book-manuscript.md`
3. Book review: `tmp/book-review-session74.md`
4. Ending drafts: `tmp/book-ending-draft.md` (variants), `tmp/book-ending-v2.md` (final)
5. Preprint guide: `tmp/preprint-submission-guide.md`
6. Build script: `tmp/build_book_pdf.py`
