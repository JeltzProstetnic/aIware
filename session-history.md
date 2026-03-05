# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-03-05 19:20 — WSL
**Goal:** Gmail triage, NoC table fix, inbox notifications
**Completed:**
- Gmail inbox triaged (10 messages, 3 days)
- NoC NCONSC-2026-071 unsubmission identified — tables dropped by pandoc
- Fixed build script: tabularx→tabular preprocessing + explicit Table N. captions + .csl copy
- Verified all 4 tables present in rebuilt .docx
- Committed and pushed fix to private remote
- Cross-project inbox: ivoclar notified about ECHA AI support email
- Cross-project inbox: cfg-agent-fleet notified about proposed global Gmail de-duplication rule
- Cross-project inbox: cfg-agent-fleet notified about VPS maintenance Mar 9
- Cross-project inbox: Updated NoC tracking item with unsubmission details
**Key Decisions:**
- Gmail de-duplication rule proposed as GLOBAL (all projects), not aIware-specific — user confirmed "all projects must be able to deal with gmail and other communication channels to a degree"
- Root cause of NoC unsubmission: pandoc silently drops complex tabularx tables. Fix: preprocess .tex before pandoc (tabularx→tabular, add Table N. prefixes)
- Build script also fixed to copy .csl files (APA style was missing from .docx builds)
**Recovery/Next session:**
- NoC resubmission: run `python3 tmp/build_noc_pdf.py --docx` on any machine (fix is committed to private), upload `tmp/noc-paper.docx` to ScholarOne
- André Nilsen email in inbox is ALREADY HANDLED (Sessions 137-138) — do not re-process

### 2026-03-05 13:45 CET — WSL
**Goal:** Learn from user edits to Nilsen + Kanai email drafts, calibrate email drafting rules
**Completed:**
- Retrieved sent Nilsen + Kanai emails from Gmail, compared against draft versions in tmp/
- Identified 7 corrections across both emails
- User corrected my analysis: Nilsen congratulations removal was about not repeating (already congratulated one day early), not a style preference
- User rejected 4 of 7 proposed rules (C, E, F, G), approved 3 (A, B, D)
- Added 3 approved rules to CLAUDE.md Communication Rules section
- Reverted premature rule writes to MEMORY.md and memory/email-drafting-rules.md
- Posted 2 inbox tasks: communications KB (near people management) + meta-rule (rule changes require user consent)
- Inbox task for email learning marked done
**Key Decisions:**
- Email drafting rules: only 3 of 7 proposed rules approved (check comms log, hedge presumptions, don't re-explain)
- Communications log/KB belongs near people management (life-management domain), not in project memory
- Rule changes require user consent before persisting — posted as proposed global rule to cfg-agent-fleet inbox
- Rules do NOT belong in auto-memory (MEMORY.md) — they go in CLAUDE.md or knowledge files
**Pending at shutdown:** None
**Recovery/Next session:**
- No pending work. Two cfg-agent-fleet inbox tasks awaiting pickup by that project.
- Communications KB doesn't exist yet — will be created by cfg-agent-fleet session.

### 2026-03-05 13:05 CET — WSL
**Goal:** Process Nilsen feedback, Oizumi/Kanai preprint analysis, paper improvements, email drafts
**Completed:**
- Deep analysis of André Nilsen's feedback on FMT predictions (Opus subagent → `tmp/nilsen-feedback-analysis.md`)
- Deep analysis of Oizumi/Kanai/Lim preprint on principal bundle geometry of qualia (Opus subagent → `tmp/oizumi-kanai-qualia-analysis.md`)
- Paper improvement: Wada procedure discussion added to Section 6.4 (full paper .md + .tex + .bib)
- Paper improvement: Pred 7 + Ultimate relabeled as "Theoretical Implications" (.md + .tex)
- Paper improvement: Abstract and section intro updated for new prediction/implication count
- Paper improvement: 4 new references added (Wada 1949, Bola 2020, Gilmore 1992, Lu 1997)
- FMT formalization roadmap: new Section 2.5 connecting Oizumi/Kanai principal bundle framework
- FMT formalization: Oizumi et al. (2025) added to references
- Gmail draft: Nilsen response (Draft ID: r2975635198369510387, thread reply)
- Gmail draft: Kanai follow-up re principal bundles (Draft ID: r527621368296242934, new thread)
- README.md updated: prediction count, Paper 2 status (parked)
- ABOUT.md updated: Paper 2 status (parked)
- Full paper PDF rebuilt (3-pass pdflatex + bibtex) → canonical `paper/full/biorxiv/paper.pdf`
- FMT formalization PDF rebuilt → canonical `paper/fmt_formal/fmt-formalization.pdf`
- RIM paper permanently parked in MEMORY.md
- New rule added: email drafts → Gmail drafts ALWAYS (CLAUDE.md Communication Rules)
**Key Decisions:**
- RIM/intelligence paper permanently parked after 3 desk rejections
- Predictions 7 and Ultimate Prediction relabeled as "Theoretical Implications" (André's feedback)
- Wada procedure discussion added proactively to full paper (André's feedback)
- Oizumi/Kanai principal bundle framework identified as most important adjacent work — integrated into formalization roadmap
- Rule established: email drafts must always be created as Gmail drafts, never text files
**Recovery/Next session:**
- Two Gmail drafts pending review: Nilsen response + Kanai follow-up
- Full analysis documents in `tmp/nilsen-feedback-analysis.md` and `tmp/oizumi-kanai-qualia-analysis.md`
- All paper changes are in .md AND .tex (synced), PDFs rebuilt
- 5 inbox tasks remain for aIware (Nilsen + Kanai now handled; Cambridge, NoC tracking, Strømme still pending)

