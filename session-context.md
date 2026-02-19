# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-19 (Session 78)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Backfill + SSRN + Class 4 self-containment fix + Big Rip conjecture + NoC status fix

## What Session 78 Did
1. **Conversation log backfill**: Reconstructed Sessions 75-77 from git history (lost to auto-compaction).
2. **SSRN submission**: Updated guide with correct title/keywords. User submitted manually. Awaiting SSRN acceptance. Note: Zenodo DOIs (DataCite) don't resolve in SSRN's Crossref-only DOI lookup — use plain URL instead.
3. **Class 4 self-containment fix**: All three documents (Paper 3, Paper 6, book) claimed "Class 4 contains all lower classes" but omitted Class 4 containing itself. Fixed Section 2.5 (Paper 3), Section 2.6 + Axiom A3 + Section 6 (Paper 6), and 6 passages in book (Ch 14, Ch 15, Appendix C). The cross-scale identity is computational self-containment (Class 4 nests Class 4), not geometric self-similarity (Class 3 fractal).
4. **Big Rip conjecture**: Created `CONJECTURE-BIG-RIP.md` — Class 4 self-containment structurally favors the Big Rip. Linked from README.
5. **NoC status correction**: Fixed all persistent files — NoC is RESUBMITTED and awaiting reviewer feedback. Was incorrectly listed as a pending TODO in session-context, MEMORY.md, README line 23, and publications-inventory.

## Submission Status
- **NoC (trimmed consciousness paper)**: RESUBMITTED. Awaiting reviewer feedback. NOT a TODO.
- **SSRN (cosmology paper)**: SUBMITTED. Awaiting acceptance.
- **Zenodo (cosmology paper)**: PUBLISHED. DOI: 10.5281/zenodo.18698606
- **PsyArXiv (intelligence paper)**: PUBLISHED. https://osf.io/preprints/osf/kctvg
- **Wetterich**: Contacted, awaiting reply.

## NEXT SESSION — Priorities
1. **Book edits**: Ch 7 expand (USER INPUT NEEDED on what to add), Ch 14-15 restructure, em-dash pass
2. Intelligence paper trim (~358 words) + highlights + .docx + submit to NIdP
3. Outreach emails (3 ready: Priesemann, Metzinger, Carhart-Harris)

## Parked TODOs

### Publications
- Intelligence paper: trim ~358 words, highlights, .docx, submit to *New Ideas in Psychology*
- Outreach emails (3 ready to send)
- Computational atoms insight — separate short paper?
- Big Rip conjecture — may integrate into Paper 3 Section 10 later

### Research
- **Perplexity findings → FMT formalization**: Wetterich, Levin-Wen, QCA/QFT → what do they mean for FMT math?

### Infrastructure (low priority)
- Paper 1 (full consciousness paper) still needs build script
- Update Claude Code
- Deploy on other machines

## Recovery Instructions
1. Read this file + MEMORY.md
2. Build scripts: `tmp/build_book_pdf.py` (book), `tmp/build_cosmology_pdf.py` (Papers 3 & 6)
3. Next session starts with book edits — ask user about Ch 7 content
