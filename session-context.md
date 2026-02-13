# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-13 (Session 18, ready for restart)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Paper trimming + email review + repo reorganization

## Current State
- **Paper trimming**: DONE — paper/trimmed/four-model-theory-trimmed.md at 9,471 body words + 236 abstract
- **Original paper**: paper/full/four-model-theory-full.md preserved (12,077 body words)
- **Emails**: All 5 reviewed and fixed. Wave 1 (Shriki + Hengen) SENT. Wave 2 pending.
- **Cover letter**: Drafted (correspondence/cover-letter-noc.md)
- **ORCID**: Registered — 0009-0005-9697-1665 (added to paper headers)
- **Repo**: Reorganized into paper/, docs/, pop-sci/, figures/, correspondence/

## Repo Structure
```
aIware/
├── README.md
├── session-context.md
├── paper/
│   ├── full/        (12k version + PDF + arxiv/)
│   └── trimmed/     (9.5k version + arxiv/ + noc/)
├── docs/            (conversation-log, theory, references, next-steps, etc.)
├── pop-sci/         (magazine, video, podcast, LinkedIn, book manuscript)
├── figures/         (book figure renders)
└── correspondence/  (gitignored — emails, cover letters)
```

## Next Session — Priority Tasks
1. **Create trimmed LaTeX** — paper/trimmed/arxiv/paper.tex (sync with trimmed .md)
2. **Wait for Wave 1 responses** — Shriki + Hengen (arXiv endorsement)
3. **Send Wave 2** — Metzinger, Carhart-Harris, Priesemann (1 week after Wave 1)
4. **Submit to NoC** — can proceed independently of arXiv
5. **Consider ASSC membership** ($99) once positive feedback received (saves $473 on APC)

## Key File Locations
- Trimmed paper: `paper/trimmed/four-model-theory-trimmed.md`
- Full paper: `paper/full/four-model-theory-full.md`
- PDF (emailed): `paper/full/The_Four_Model_Theory_of_Consciousness.pdf`
- Cover letter: `correspondence/cover-letter-noc.md`
- Next steps plan: `docs/next-steps.md`
- Full LaTeX (needs trimmed version): `paper/full/arxiv/paper.tex`
- Wave 2 emails: `correspondence/email-{metzinger,carhart-harris,priesemann}.txt`
- Wave 1 (sent): `correspondence/sent/email-{shriki,hengen}.txt`

## Recovery Instructions
1. Read THIS FILE first
2. Main task: create paper/trimmed/arxiv/paper.tex from trimmed .md
3. Check email responses (Wave 1 sent to Shriki + Hengen)
4. ALWAYS push to BOTH remotes: `git push origin main && git push private main`
