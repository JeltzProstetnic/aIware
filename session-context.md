# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-13 (Session 20, pre-autocompact)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: PDF formatting fixes completed; next = literature review

## Current State
- **LaTeX installed**: `pdflatex` available locally (texlive via apt)
- **Both paper versions compile**: trimmed (38pp) + full (45pp)
- **Tables 3 & 4**: Abbreviated with symbols in ALL versions (md, tex)
- **Abstract**: "This paper presents..." in all versions, single-spaced in LaTeX
- **ORCID**: In both LaTeX versions
- **Keywords**: Page 1 (trimmed), page 2 (full — long abstract, acceptable)

## PDF Files on Windows (`C:\Users\Matthias\Documents\`)
| File | Style | Version |
|---|---|---|
| `four-model-theory-trimmed-classic.pdf` | Classic (md2pdf) | Trimmed |
| `four-model-theory-full-classic.pdf` | Classic (md2pdf) | Full |
| `four-model-theory-trimmed-modern.pdf` | Modern (LaTeX) | Trimmed, 38pp |
| `four-model-theory-full-modern.pdf` | Modern (LaTeX) | Full, 45pp |

## Compile Commands
- **LaTeX trimmed**: `cd paper/trimmed/arxiv && pdflatex -interaction=nonstopmode paper.tex`
- **LaTeX full**: `cd paper/full/arxiv && pdflatex -interaction=nonstopmode paper.tex`
- **Classic trimmed**: `cd paper/trimmed/noc && uvx --from "md2pdf[cli]" md2pdf -i four-model-theory-noc.md -o four-model-theory-noc.pdf -e tables -e toc -c paper.css`

## Emails Status
- **Wave 1 SENT**: Shriki + Hengen (arXiv endorsement) — NO RESPONSES YET
- **Wave 2 PENDING**: Metzinger, Carhart-Harris, Priesemann

## Next Session Tasks

### 1. Fix Figure 1 arrows
The two upper gray arrows (SCOPE axis) point left→right but should point **downward**. Need to regenerate the SVG/PNG.

### 2. Fix Tables 2 & 3 in LaTeX — tables missing
In the compiled LaTeX PDFs, Tables 2 (Criticality Convergence) and 3 (Consciousness States) show only the caption text ("Table 2: ..." / "Table 3: ...") but the actual table content is gone. Likely a `tabularx` / `\end{tabularx}` mismatch introduced during the width fixes. Check the .tex files.

### 3. Consistent, nice glyphs for Table 4 in LaTeX
The current mix of `\bullet`, `\circ`, `\textcircled`, and `---` looks inconsistent. Spike first: create a minimal .tex file to test a **coherent symbol set** (e.g., `wasysym` filled/half/empty circles, or `tikz`-based, or another package) where all four rating levels look like they belong together. Then apply the winner to both paper.tex files.

### 4. Literature & Claims Review
Thorough review of the paper checking:
- Are all cited references real and accurately described?
- Are claims about competing theories (IIT, GNW, HOT, PP, AST, RPT) fair and accurate?
- Are dates, authors, and findings correctly attributed?
- Are any important recent references missing?
- Focus on the NoC version (`paper/trimmed/noc/four-model-theory-noc.md`)

## Key File Locations
- NoC markdown: `paper/trimmed/noc/four-model-theory-noc.md`
- Trimmed LaTeX: `paper/trimmed/arxiv/paper.tex`
- Full LaTeX: `paper/full/arxiv/paper.tex`
- Full markdown: `paper/full/four-model-theory-full.md`
- Cover letter: `correspondence/cover-letter-noc.md`
- Submission checklist: `paper/trimmed/noc/SUBMISSION-CHECKLIST.md`

## Recovery Instructions
1. Read THIS FILE first
2. Next task: thorough literature/claims review of the NoC paper
3. Use web search to verify references, dates, claims
4. ALWAYS push to BOTH remotes: `git push origin main && git push private main`
