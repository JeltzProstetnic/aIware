# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-19 (Session 73)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Cosmology paper update (new literature from Perplexity analysis), then restart for book review

## Current State
- **Active Task**: Updating FMT formalization paper with literature implications
- **Cosmology paper**: DONE — integrated, rebuilt PDF, committed, pushed
- **Formalization analysis**: DONE — `tmp/formalization-literature-implications.md`
- **Formalization paper edits**: IN PROGRESS — adding RG fixed point to Module 6, elevating Module 7 in build order, adding ν_crit graph transition, doubling caution, bridge-to-physics note
- **All infrastructure TODOs from Session 71**: DONE (Session 72)
- **Skills installed**: Restart required to load (docx, pdf, doc-coauthoring + 6 global skills)

## What Session 73 Did
1. Integrated Perplexity literature findings into SB-HC4A cosmology paper
2. Added 6 new research programs to Section 11.1: Wetterich (CA↔QFT equivalences), Wolfram Physics Project (emergent GR/QM), Levin-Wen (string-net condensation), Quantum Graphity (emergent spacetime), QCA/Causal Sets, Steinhardt-Turok (cyclic cosmology)
3. Strengthened Section 5.6 (computational atoms) with Wetterich existence proof
4. Updated Conclusion (Section 12) with converging research landscape
5. Added ~12 new references (Wetterich 2022a-d, Wolfram 2021, Levin & Wen 2005, Konopka et al. 2008, Bisio et al. 2015, Elze 2014, Surya 2019, Nielsen & Ninomiya 1981, Steinhardt & Turok 2002)
6. Fixed cosmology paper unicode-header.tex (was MISSING, now copied from fmt_formal)
7. Rebuilt sb-hc4a.pdf (264KB)
8. Committed Perplexity source files (perplexity-review.md, perplexity literature findings.md)

## NEXT SESSION — Book Pipeline
- **Take into account**: `pop-sci/perplexity-review.md` (Perplexity's readability review)
- Perplexity's 5 main issues: em-dash addiction (1,178), Ch 4 defensive loop, Ch 15-16 wall, concept repetition, Ch 7 undercooked

### Phase 1: Deep Review
- Read `pop-sci/book-manuscript.md` (~31,000 words) end-to-end
- Cross-reference with Perplexity review findings
- Assess: flow, consistency, accuracy, readability, narrative arc
- Flag: repetition, gaps, unclear passages, tonal shifts
- Generate review HTML for author to scan

### Phase 2: Editing
- Apply review findings
- Ensure chapter transitions are smooth
- Verify all theory references are consistent with papers
- **Ch 15-16**: Consider restructuring with new cosmology literature (Wetterich, Quantum Graphity, etc.)
- Check that pop-sci tone is maintained (not too academic, not too casual)

### Phase 3: Illustration
- Identify passages that need figures/diagrams
- Design illustrations for key concepts (four models, real/virtual split, qualia)
- Create or commission visuals

### Phase 4: Publishing
- Final proofread
- Format for target platform (self-publishing? publisher submission?)
- Cover design, metadata, ISBN

## Parked TODOs (not next session)

### Publications
- Intelligence paper: trim ~358 words, highlights, .docx, submit to *New Ideas in Psychology*
- NoC resubmission (trimmed paper .docx ready)
- Outreach emails (3 ready to send: Priesemann, Metzinger, Carhart-Harris)
- **Wetterich contacted** — waiting for reply
- Computational atoms insight — separate short paper?

### Research
- **Perplexity findings → FMT formalization**: What do Wetterich, Levin-Wen, and QCA/QFT results mean for the mathematical formalization of the four-model theory?

### Infrastructure (low priority)
- ~~Cosmology paper missing unicode-header.tex~~ DONE (Session 73)
- Papers 1 and 3 need build scripts (.tex currently hand-maintained)
- Update Claude Code 2.1.37 → 2.1.47
- Deploy on other machines (NUC, Steam Decks, etc.)

## Recovery Instructions
1. Read this file. Next step: deep book review (take into account Perplexity review).
2. Book manuscript: `pop-sci/book-manuscript.md`
3. Book formatting rules: `pop-sci/book-manuscript.formatting-rules.md`
4. Perplexity review: `pop-sci/perplexity-review.md`
5. Build script: `tmp/build_book_pdf.py`
6. Review tool: `tmp/review_changes.py` (symlink to `~/claude-config/tools/`)
7. Skills need restart to load.
