# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-19 (Session 76)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Wetterich integration across cosmology papers

## Current State
- **Active Task**: Session complete — restart ready
- **Wetterich integration**: Added Wetterich's CA↔QFT equivalences across Paper 3 (Section 1.2), Paper 6 (abstract, Section 3.7, Section 4.5, Phase 1 roadmap, Section 11.1, conclusion, references), and README
- **PDFs**: Paper 3 and Paper 6 rebuilt via pandoc
- **MEMORY.md**: Updated with complete 6-paper inventory table (was missing Papers 5-6)
- **NoC**: Submitted, awaiting reviewer feedback (no action needed)

## What Session 76 Did
1. Analyzed Wetterich vs 't Hooft prominence across all cosmology papers
2. **Paper 3 (Section 1.2)**: Added Wetterich sentence under 't Hooft — proven CA↔QFT equivalences, spinor gravity in 4D
3. **README**: Added "with mathematical grounding from Wetterich's CA↔fermionic QFT equivalences" to Paper 3 description
4. **Paper 6 — major integration** (6 locations):
   - Abstract: Wetterich alongside 't Hooft
   - Section 3.7 (Computational Atoms): Full existence-proof paragraph with 4 results + Grassmann mapping as formalization tool
   - Section 4.5 (Holographic Automata): Wetterich as concrete holographic rule set examples (HR1-HR2), HR3 as open question
   - Phase 1 roadmap (Module 3): Wetterich's Grassmann mapping as existing formal machinery
   - Section 11.1: Added to "Interoperability with physics"
   - Conclusion: Formalization builds on existing results, not starting from zero
   - References: Added Wetterich 2022a-d (were completely missing)
5. Rebuilt both PDFs via pandoc
6. Updated MEMORY.md with complete 6-paper inventory table

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
