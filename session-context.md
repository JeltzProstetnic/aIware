# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-13 (Session 20)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: PDF review formatting fixes + prepare for literature review

## Current State
- **Tables 3 & 4**: Abbreviated in ALL three paper versions (noc, trimmed, full)
- **Figures**: Embedded in NoC markdown with HTML img tags
- **PDF generation**: `uvx --from "md2pdf[cli]" md2pdf -i <file> -o <out> -e tables -e toc -c paper.css`
- **Abstract**: Opens with "This paper presents" (not "I present")

## What's Ready for NoC Submission
1. LaTeX manuscript + references.bib + 3 figures (`paper/trimmed/arxiv/`)
2. Cover letter with AI disclosure (`correspondence/cover-letter-noc.md`)
3. Submission checklist (`paper/trimmed/noc/SUBMISSION-CHECKLIST.md`)
4. Review PDF (`paper/trimmed/noc/four-model-theory-noc.pdf`)

## Emails Status
- **Wave 1 SENT**: Shriki + Hengen (arXiv endorsement) — NO RESPONSES YET
- **Wave 2 PENDING**: Metzinger, Carhart-Harris, Priesemann

## Next Session Task: Literature & Claims Review
Thorough review of the paper checking:
- Are all cited references real and accurately described?
- Are claims about competing theories (IIT, GNW, HOT, PP, AST, RPT) fair and accurate?
- Are dates, authors, and findings correctly attributed?
- Are any important recent references missing?
- Focus on the NoC version (`paper/trimmed/noc/four-model-theory-noc.md`)

## Key File Locations
- NoC markdown: `paper/trimmed/noc/four-model-theory-noc.md`
- NoC PDF: `paper/trimmed/noc/four-model-theory-noc.pdf`
- PDF stylesheet: `paper/trimmed/noc/paper.css`
- Trimmed markdown: `paper/trimmed/four-model-theory-trimmed.md`
- Full paper: `paper/full/four-model-theory-full.md`
- LaTeX: `paper/trimmed/arxiv/paper.tex`
- Cover letter: `correspondence/cover-letter-noc.md`
- Figures: `paper/trimmed/noc/figure{1,2,3}-*.png`

## Recovery Instructions
1. Read THIS FILE first
2. Next task: thorough literature/claims review of the NoC paper
3. Use web search to verify references, dates, claims about competing theories
4. ALWAYS push to BOTH remotes: `git push origin main && git push private main`
