# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-13 (Session 21)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Literature review + fix all pending formatting/content issues

## Current State
- **LaTeX installed**: `pdflatex` available locally (texlive via apt)
- **Both paper versions compile**: trimmed (40pp) + full (47pp)
- **All tables render correctly** in both LaTeX versions
- **Table 4 glyphs**: Unified amssymb circle set (● ⊙ ○ ---)
- **Figure 1**: SCOPE arrows fixed (downward), PNG regenerated
- **Literature review**: Complete — 8 factual errors corrected, 3 refs added, claims softened
- **Causal Role clarification**: Clock analogy + "consciousness is being done" paragraph added to Section 4.2

## PDF Files on Windows (`C:\Users\Matthias\Documents\`)
| File | Style | Version |
|---|---|---|
| `four-model-theory-trimmed-classic.pdf` | Classic (md2pdf) | Trimmed (NOT updated this session) |
| `four-model-theory-full-classic.pdf` | Classic (md2pdf) | Full (NOT updated this session) |
| `four-model-theory-trimmed-modern.pdf` | Modern (LaTeX) | Trimmed, 40pp — UPDATED |
| `four-model-theory-full-modern.pdf` | Modern (LaTeX) | Full, 47pp — UPDATED |

## Compile Commands
- **LaTeX trimmed**: `cd paper/trimmed/arxiv && pdflatex -interaction=nonstopmode paper.tex`
- **LaTeX full**: `cd paper/full/arxiv && pdflatex -interaction=nonstopmode paper.tex`
- **Classic trimmed**: `cd paper/trimmed/noc && uvx --from "md2pdf[cli]" md2pdf -i four-model-theory-noc.md -o four-model-theory-noc.pdf -e tables -e toc -c paper.css`

## Emails Status
- **Wave 1 SENT**: Shriki + Hengen (arXiv endorsement) — NO RESPONSES YET
- **Wave 2 PENDING**: Metzinger, Carhart-Harris, Priesemann

## Session 21 Changes (Summary)
1. Figure 1 SCOPE arrows: horizontal → downward (SVG + PNG)
2. LaTeX Table 2: fixed `\end{tabular}` → `\end{tabularx}` mismatch
3. Table 4: unified glyphs with amssymb (●/⊙/○/---)
4. 8 reference errors corrected (Schartner, Corlett, Reinders x2, Konstantinou→Tononi, Frankish→Graziano, Melloni journal, Milinkovic vol)
5. 3 references added (IIT-Concerned, Tononi rebuttal, Gomez-Marin & Seth)
6. 7 uncited refs removed (trimmed), 6 binding/RPT cites added
7. Convergence claim softened (acknowledge pre-2015 empirical work)
8. Prediction 3 uniqueness softened (acknowledge PP could generate related account)
9. Causal Role clarification: clock analogy, distinguish from classical epiphenomenalism

## Next Session Tasks
- Review the updated modern PDFs for any remaining issues
- Regenerate classic (md2pdf) versions if needed
- Check word count on NoC version (was 9,471 — additions may push close to limit)
- Consider adding Siegel et al. (2024) Nature psilocybin paper + NY Declaration on Animal Consciousness (2024)
- arXiv endorsement follow-up (if responses received)
- Wave 2 outreach emails

## Key File Locations
- NoC markdown: `paper/trimmed/noc/four-model-theory-noc.md`
- Trimmed LaTeX: `paper/trimmed/arxiv/paper.tex`
- Full LaTeX: `paper/full/arxiv/paper.tex`
- Full markdown: `paper/full/four-model-theory-full.md`
- Cover letter: `correspondence/cover-letter-noc.md`
- Submission checklist: `paper/trimmed/noc/SUBMISSION-CHECKLIST.md`

## Recovery Instructions
1. Read THIS FILE first
2. Check word count on NoC markdown (limit 10,000)
3. Review PDFs on Windows for visual issues
4. ALWAYS push to BOTH remotes: `git push origin main && git push private main`
