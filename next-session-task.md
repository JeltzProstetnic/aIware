<!-- task: true -->
- **task**: true
- **file**: docs/pending-aiw92-paper-integration.md
- **backlog**: AIW-92
- **description**: Execute the AIW-92 PAPER integration (final Tier A target). Books are DONE+committed (08d3416). Follow the spec in docs/pending-aiw92-paper-integration.md: add 4 bib entries (Meisel2012, TononiEdelman1998, KoenigRobertPearson2019, Soon2013), DROP Schindler 2008, make 6 edits in BOTH four-model-theory-full.md AND latex/paper.tex (§3.7 un-numbered two-dimensions block + seizure worked-example; route-indep seizure at lines 410+885; §3.4.6 presence/access; §4.2.3 two-causal-roles NEW subsection w/ manual renumber of 4.2.3→4.2.4→4.2.5; §5.1 energy governor). NO Prediction 5, NO Table 4 row. Build into tmp/ (pdflatex×3 + bibtex w/ dangerouslyDisableSandbox), grep for ??? citations + broken Section refs, update references.md, commit. Then AIW-93 (AI-tell/voice pass, esp. DE).
