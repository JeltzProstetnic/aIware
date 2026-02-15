# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-15 (Session 37)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Open todos review, book PDF generation, preprint strategy

## Current State
- **Active Task**: User handling arXiv withdrawal + bioRxiv submission
- **Progress**:
  - Reviewed all open todos
  - Clarified bioRxiv vs arXiv strategy (bioRxiv chosen — no endorsement wall)
  - Built book manuscript PDF converter (`tmp/build_book_pdf.py`)
  - Generated 124-page A5 book PDF with 3 figures at `pop-sci/book-manuscript.pdf`
  - Copied to Windows desktop for review
- **Pending**: User reviewing book PDF, user doing arXiv withdrawal + bioRxiv submission

## Session 37 — What Happened

### Open Todos Reviewed
1. bioRxiv preprint submission — USER DOING NOW
2. Full paper → journal — BLOCKED (wait for NoC, ~late March). Target: Physics of Life Reviews
3. Intelligence paper — DRAFT COMPLETE (7,858 words), could submit independently
4. Book manuscript — PDF GENERATED for review
5. LaTeX parity — full paper LaTeX behind markdown
6. Chapter expansion — future (Ch 8, 10, 11 short; Ch 12 could split)

### Preprint Strategy Decision
- User had already sent outreach emails to Hengen (WashU) and Shriki (BGU) with arXiv endorsement link
- Decided: withdraw arXiv submission, submit to bioRxiv instead (no endorsement wall, 24-72hr turnaround)
- Endorsement contacts still useful for future papers (endorses account, not specific paper)

### Book PDF Generated
- Script: `tmp/build_book_pdf.py` (markdown→LaTeX→PDF)
- Output: `pop-sci/book-manuscript.pdf` (124 pages, A5, Palatino, 3 figures)
- Figure placement: p.28 (four-model architecture), p.30 (real/virtual split), p.33 (phenomenological content)
- Also generated: `pop-sci/book-manuscript.tex` (intermediate LaTeX)

### Book Feedback (DO NOT APPLY YET — noted for future session)
- "About the Author" section: "I'd ask you to wait a few pages" → too defensive/pleading
- User's authentic voice: more like "I don't mind" / unbothered / genuinely doesn't care about credentials
- Need to find the right register: direct, confident, not crude

## Key File Locations
- **Book PDF**: `pop-sci/book-manuscript.pdf` + `C:\Users\Matthias\Desktop\book-manuscript.pdf`
- **Book LaTeX**: `pop-sci/book-manuscript.tex`
- **PDF converter**: `tmp/build_book_pdf.py`
- **Sent emails**: `correspondence/sent/email-hengen.txt`, `correspondence/sent/email-shriki.txt`
- **Preprint guide**: `tmp/preprint-submission-guide.md`

## Recovery Instructions
1. User is handling arXiv withdrawal + bioRxiv submission manually
2. Book PDF is generated and on desktop — awaiting more feedback
3. Do NOT edit book manuscript yet — just collect feedback notes
4. Next technical work: apply book feedback (future session), LaTeX parity, chapter expansion
