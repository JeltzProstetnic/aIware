# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-03-04 ~13:00 — WSL
**Goal:** NoC resubmission prep + cleanup + rule codification
**Completed:**
- Deleted misleading tmp/ artifacts (weasyprint renders, revision intermediates, stale builds)
- Updated Zenodo DOI from 18669891 to 18861613 (v3) across all 10 files + MEMORY.md
- Updated cover letter for new submission (references NCONSC-2026-051, details 3 revisions)
- Prepared submission folder: `tmp/noc-resubmission/` with manuscript.docx, 3 figures, cover letter, alt text, highlights
- Fixed paper.tex: removed [^quantum] footnote, added alt text under all 3 figure captions
- Fixed pandoc .docx build: added APA CSL to prevent "———" author substitution dashes
- Rebuilt noc-paper.docx with all fixes
- Stored NoC journal guidelines as ACA-009 in DMS + `paper/trimmed/noc/journal-guidelines-noc.md`
- Added 6 new rules to CLAUDE.md (delivery, build, submission)
- Dropped 2 inbox tasks for cfg-agent-fleet (DMS discoverability + architecture)
**Key Decisions:**
- Desk rejection = new submission (no revision workflow on ScholarOne for "Immediate Reject")
- APA CSL chosen for pandoc .docx builds to avoid Chicago-style author dashes
- Journal guidelines stored in both project dir and DMS catalog (ACA-009)
- Rules go in CLAUDE.md, NOT MEMORY.md — user corrected this explicitly
**Pending at shutdown:** User is uploading to ScholarOne. Verify after submission that new manuscript ID is assigned.
**Recovery/Next session:**
- Submission folder: `tmp/noc-resubmission/` has everything needed
- If .docx needs rebuild: `python3 tmp/build_noc_pdf.py --docx` (now includes APA CSL automatically)
- Cover letter: `correspondence/cover-letter-noc.md` (plain text copy in submission folder)
- Editor reply: `tmp/editor-reply-andrillon-draft.txt` (not needed for new submission — integrated into cover letter)

### 2026-03-04 12:10 — WSL
**Goal:** Deep review of both submission artifacts (full + NoC), fix all issues, then proceed to preprint update + NoC resubmission + editor email
**Completed:**
- Built full paper PDF (tmp/build-full/paper.pdf, 61pp, ~13,900 words)
- Built NoC .docx + PDF (tmp/noc-paper.docx, tmp/noc-paper.pdf, 40pp, ~9,029 words)
- Deep review by 3 parallel agents: full paper, NoC, cross-comparison
- Fixed .docx figure embedding (added --resource-path + cwd to pandoc in build_noc_pdf.py)
- Fixed Aldrich1987 wrong authors in NoC references.bib (corrected to 4-author version)
- Fixed Gazzaniga1965 wrong paper in NoC references.bib (Neurology→Brain)
- Fixed dangling "Section 3.7.1" ref in NoC paper.tex (replaced with inline hierarchy description)
- Backported 3 citation fixes from NoC to full paper (Friston2010, COGITATE artifact, TononiAlbantakis2025)
- Fixed section numbering in full paper (subsection→subsubsection for 3.7.1-3.7.3, added labels+refs)
- Added pdflatex/bibtex/pandoc/weasyprint/pytest/etc to global permissions
- Rebuilt both artifacts — all fixes verified clean
**Key Decisions:**
- Aldrich1987: Full paper version (4 authors) is correct per PubMed; NoC had wrong 5-author variant
- Gazzaniga1965: Full paper version (Brain, "Disconnexion") is the canonical split-brain paper; NoC had the earlier Neurology paper
- Section 3.7.1 ref in NoC: Replaced with inline enumeration rather than removing entirely (preserves context for reader)
- Full paper intro: Removed uncited inline text refs (Frontiers in Psychology 2025, Acta Analytica 2024) — not in .bib, no clean citation possible
**Pending at shutdown:** 1. Update Zenodo preprint, 2. NoC resubmission, 3. Email to editor
**Recovery/Next session:**
- All source fixes are in: paper/full/biorxiv/paper.tex, paper/trimmed/noc/paper.tex, paper/trimmed/noc/references.bib, tmp/build_noc_pdf.py
- Built artifacts in tmp/ are ready for review but NOT yet committed
- Next steps: 1. Update Zenodo preprint (full paper), 2. Resubmit to NoC, 3. Email editor
- Rebuild commands: full → copy biorxiv/ to tmp/build-full/, pdflatex×3 + bibtex; NoC → python3 tmp/build_noc_pdf.py --docx

### 2026-03-04 — WSL
**Goal:** Build LaTeX pipeline for NoC paper (replacing inferior markdown→docx pipeline)
**Completed:**
- Diagnosed Table 3 overflow: markdown pipe table → pandoc .docx has no width constraint; full paper uses tabularx
- Created `paper/trimmed/noc/paper.tex` — full LaTeX conversion of NoC paper, matching full paper quality
- Created `paper/trimmed/noc/references.bib` — 104 BibTeX entries (all NoC refs + Block2007, Tagliazucchi2016 fixes)
- Created `tmp/build_noc_pdf.py` — build script with --docx and --highlight flags
- Test build successful: 40 pages, 726KB, 0 undefined citations, 8 minor hbox warnings
- Table 3 now uses tabularx with controlled column widths — overflow fixed
**Key Decisions:**
- NoC paper now has a proper LaTeX pipeline matching the full paper's quality. The old markdown→pandoc→docx pipeline is superseded for review/authoring; .docx submission copy is generated from .tex via pandoc.
- Title "Simulation-Based Framework" kept — Session 131 clarified the term, didn't retreat from it.
- Resubmit first, email editor second (so manuscript is in system when editor reads the reply).
**Recovery/Next session:**
- NoC .tex source: `paper/trimmed/noc/paper.tex`
- NoC .bib: `paper/trimmed/noc/references.bib`
- Build: `python3 tmp/build_noc_pdf.py` (PDF) or `python3 tmp/build_noc_pdf.py --docx` (PDF + .docx)
- Review PDF: `tmp/noc-paper.pdf`
- Full paper canonical PDF: `paper/full/biorxiv/paper.pdf` (do NOT recompile — use as-is)

