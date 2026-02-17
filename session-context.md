# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-17 (Session 67, pre-push)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Write SB-HC4A cosmology formalization paper — DONE

## Current State
- **Active Task**: Ready for commit + push
- **Progress**:
  - Cosmology formalization paper written: `paper/cosmology_formal/sb-hc4a-formalization.md` (~9,200 words)
  - PDF generated: `paper/cosmology_formal/sb-hc4a-formalization.pdf`
  - Bruno Gruber death year REMOVED from cosmology paper (HE IS ALIVE!)
  - Cosmology PDF regenerated with fix
  - README restructured: papers 1-3 (content), papers 4-6 (formalizations)
  - Conversation log updated with Session 67
  - MEMORY.md updated with Bruno alive note
- **Pending**: Commit and push

## TOP TODO (Next Session)
1. **DECIDE: Cosmology as final book chapter vs. separate book** — user leans toward chapter. Once reader understands consciousness, cosmology is ~1 chapter.
2. **DECIDE: Five-class taxonomy as separate paper or part of cosmology paper** — currently only in book. If separate: short supplemental paper. If integrated: expand Section 2 of cosmology paper.
3. Pop-sci book chapter on cosmology (if going book-chapter route)
4. Intelligence paper: trim ~358 words, highlights, .docx, submit to *New Ideas in Psychology*
5. NoC resubmission (trimmed paper .docx ready)
6. Outreach emails (3 ready to send)

## Key Files
- `paper/cosmology_formal/sb-hc4a-formalization.md` — cosmology formalization paper (CANONICAL SOURCE)
- `paper/cosmology_formal/sb-hc4a-formalization.pdf` — generated PDF
- `paper/cosmology_formal/unicode-header.tex` — LaTeX Unicode mapping for PDF generation
- `paper/cosmology/sb-hc4a.md` — cosmology paper (CANONICAL SOURCE, Bruno fixed)

## Recovery Instructions
1. Commit and push (if not yet done)
2. The two open decisions need user input (book structure, five-class taxonomy)
3. For PDF regeneration: `pandoc paper/cosmology_formal/sb-hc4a-formalization.md -o paper/cosmology_formal/sb-hc4a-formalization.pdf --pdf-engine=pdflatex -V geometry:margin=1in -V fontsize=11pt -V documentclass=article -H paper/cosmology_formal/unicode-header.tex`

## Conversation Summary
Session 67. Wrote the SB-HC4A cosmology formalization paper (third in the "Toward..." series). 8 modules, ~9,200 words. Fixed Bruno (alive, not dead!). Restructured README with new paper ordering. Three open discussion points deferred: book chapter vs separate book, five-class taxonomy placement, TOC question (no TOC found in markdown — may have been in a previous PDF build).
