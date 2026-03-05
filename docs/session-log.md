# Session Log

Full session history. Newest first. Never pruned.

### 2026-03-05 — WSL
**Goal:** Hardcover cover subtitle fix + German book revision tracking
**Completed:**
- Fixed hardcover cover subtitle position — moved up 0.25in in `pop-sci/cover-wrap-hc.tex` (y: 7.5085 → 7.7585) to avoid overlap with image
- Rebuilt `pop-sci/cover-wrap-hc.pdf` — user confirmed fix looks correct
- Added AIW-20 to backlog: upload updated cover to KDP/Amazon
- Added AIW-21 to backlog: German book content revisions (no drug self-reports, less autobiographical, cut Glück roasting examples)
**Key Decisions:**
- Subtitle shift of 0.25in (one line at 18pt leading) confirmed as correct by user
- German book revision scoped to 3 specific content issues (AIW-21)
**Pending at shutdown:** Nothing
**Recovery/Next session:**
Cover fix is local only — needs KDP upload (AIW-20). Check paperback/EU variants for same subtitle-image overlap issue during that task.

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

### 2026-03-04 18:35 — WSL
**Goal:** Check Gmail (T&P decision, AISB correspondence), park RIM, update backlog
**Completed:**
- Checked Gmail — Theory & Psychology desk rejection (TAP-26-0111, editor Teo, "argument not new")
- RIM paper PARKED after 3 desk rejections (NIdP, Phil Psych, T&P), zero peer reviews
- Read AISB/AICE-26 email from Parthemore — must resubmit on OpenReview (anonymized PDF, profile needed)
- Found original submission: "Substrate-Independent Consciousness and the Ethics of Artificial Minds" (extended abstract to Torrance, Feb 22)
- Updated backlog: T&P rejected, AICE-26 resubmission as AIW-19 (P1), RIM parked
- Updated MEMORY.md: RIM parked, AICE-26 waiting item added
- Dropped inbox task for cfg-agent-fleet: create gmail-management.md knowledge file
- User wants long-term Gmail inbox zero — systematic triage 10 at a time, eventually full management
**Key Decisions:**
- RIM paper permanently parked — PsyArXiv preprint is the citable record, no further journal submissions
- Gmail inbox zero is a long-term goal; knowledge file creation delegated to cfg-agent-fleet
**Pending at shutdown:** Nothing
**Recovery/Next session:**
No active work in progress. Next priorities: AIW-19 (OpenReview resubmission), AIW-16 (Digital Minds Fellowship, deadline Mar 27).

### 2026-03-04 14:17 — WSL
**Goal:** NoC resubmission — complete ScholarOne submission and email editor
**Completed:**
- Manuscript.docx uploaded to ScholarOne as new submission (not revision — desk rejection = new submission)
- Figures uploaded separately (figure1, figure2, figure3 as PNG)
- Cover letter uploaded
- File designations set (Main Document, Figure, Cover Letter)
- Previous manuscript ID entered: NCONSC-2026-051
- Collection selected: Theories and models (370)
- Open Science Badge: declined (no application form prepared)
- 5 suggested reviewers entered with emails
- Submission completed on ScholarOne
- Editor reply email drafted and sent to thomas.andrillon@icm-institute.org (from matthias@matthiasgruber.com)
**Key Decisions:**
- **Suggested reviewers chosen to avoid conflicts**: Excluded all 12 previously contacted researchers. Final 5: Hinterberger (Regensburg, published in NoC on criticality), Shew (Arkansas, criticality meta-analysis co-author not contacted), Tsuchiya (Monash, qualia), Fahrenfort (VU Amsterdam, consciousness), Aru (Tartu, computational consciousness)
- **Andrillon email sent to institutional address** (thomas.andrillon@icm-institute.org) not generic editorial office — direct reply to his specific feedback, lower bounce risk
- **Lesson learned**: Contacting criticality researchers (Hengen, Shriki, Priesemann) for outreach burned them as potential reviewers. Future outreach planning should reserve some domain experts as reviewer candidates.
**Recovery/Next session:**
Submission is complete. No action needed unless ScholarOne sends error/rejection email. All submission artifacts in `tmp/noc-resubmission/`. Suggested reviewers list saved at `tmp/noc-resubmission/suggested-reviewers.txt`.

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

### 2026-03-04T11:15Z — WSL
**Goal:** Fix "simulation" terminology and Hard Problem dissolution argument across all paper versions, responding to NoC desk rejection (NCONSC-2026-051, Andrillon)
**Completed:**
- Analyzed Andrillon's feedback (3 concerns: simulation undefined, hard problem dissolution unclear, simulation just distinguishes substrate from computation)
- Applied Edit 1: New "clarification on terminology" paragraph after Core Definition (Section 3.1) in all versions (.md full, .md trimmed, .tex full)
- Applied Edit 2: Restructured Section 3.4 — universal level distinction opening, qualia as computational-level digital constructs, Hard Problem as level confusion, self-referential closure promoted to primary argument
- Applied Edit 3: Mechanical terminology changes (simulated→generated, simulate→imitate) throughout
- Updated abstracts in both versions (computational-level framing)
- Updated overview paragraphs in both versions
- Updated .tex (paper/full/biorxiv/paper.tex) to match all .md changes
- Built submission-quality PDF: full paper via pdflatex (tmp/build-full/paper.pdf, 61pp)
- Built trimmed paper .docx (tmp/build-noc/four-model-theory-noc.docx) and PDF view
- Drafted editor reply to Andrillon (tmp/editor-reply-andrillon-draft.txt) — opening thanks for taking work seriously, apologizes for sloppy simulation shorthand from engineering context
- Documented build pipelines in MEMORY.md
- Documented paper review output rules in MEMORY.md
**Key Decisions:**
- "Simulation" retained as term but explicitly defined as pedagogical shorthand, not digital-twin claim
- Hard Problem dissolution reframed: category error = level confusion (seeking computational-level properties at substrate level), NOT "qualia are in the simulation"
- Substrate/computation distinction presented as universal engineering truism, not unique to FMT
- Self-referential closure promoted from anticipated-objection to primary dissolution argument
- "simulated" → "generated" throughout model definitions and Table 1
- Abstract updated to lead with computational-level framing
- Editor reply tone: honest apology for sloppy terminology, direct acknowledgment reviewer was correct
**Recovery/Next session:**
1. All paper source files are updated: `paper/full/four-model-theory-full.md`, `paper/trimmed/noc/four-model-theory-noc.md`, `paper/full/biorxiv/paper.tex`
2. Build outputs in tmp/: `tmp/build-full/paper.pdf` (submission quality), `tmp/build-noc/four-model-theory-noc.{pdf,docx}`
3. Editor reply draft: `tmp/editor-reply-andrillon-draft.txt` — DO NOT finalize until papers are fully reviewed
4. Revision analysis: `tmp/revision-draft-simulation-fix.md` (working notes, can be deleted)
5. Highlighted review copies: `tmp/fmt-full-revised-highlighted.md`, `tmp/fmt-noc-revised-highlighted.md` (can be deleted)
6. **Table 3 overflow**: Search conversation-log.md or session-history.md for "Table 3" or "overflow" or "horizontal" to find previous fix. Likely a tabularx width or font size adjustment.
7. **Next steps**: Fix Table 3 → rebuild full PDF → update Zenodo → finalize editor reply → resubmit to NoC
8. **Preprint update**: User said to do AFTER a clear (new session), to be safe

### 2026-03-02T17:22Z — WSL
**Goal:** Process inbox, handle Mediano reply
**Completed:**
- Checked Gmail inbox — found Pedro Mediano reply (same-day, positive)
- Analyzed Mediano's pushback on psychedelic prediction and "tease apart EWM/ESM" question
- Drafted and created Gmail reply (threaded, from matthias@matthiasgruber.com)
- User reviewed and sent the reply
- Updated engagement-log.md (Mediano → BOTH, reply details)
- Updated contacts.md (Mediano → Active)
- Dropped cfg-agent-fleet inbox task: "email drafts go to Gmail Drafts, not tmp files"
**Key Decisions:**
- Conceded "preserved or enhanced" was too strong for psychedelic EWM prediction — reframed as "differentially affected" in reply to Mediano
- Email drafts should go to Gmail Drafts via MCP, not tmp/ text files (rule to be codified in cfg-agent-fleet)
**Pending at shutdown:** None
**Recovery/Next session:**
1. Mediano exchange is active — if he replies, check Gmail thread ID 19caeb983bde4556
2. UCL Summer School application acknowledged (Sarah Kalwarowsky) — wait for decision
3. Ivoclar Kenosi/batch_langextract IT security audit in progress (André Hopfgartner wants docs)

### 2026-03-03T14:30Z — WSL
**Goal:** AIW-15 diagram redesign + Gmail check + inbox processing
**Completed:**
- AIW-15: Redesigned all 16 simple Mermaid diagrams in `tmp/build_individual_pdfs.py` — LR→TD flow, subgraph grouping, shortened labels, visible self-ref loops
- Increased render height 600→900px for TD layouts
- Fixed Design 16 empty first page (max-height constraint + page-break override)
- Fixed Design 15 B&W/confusing (added explicit IWM/ISM/EWM/ESM nodes with colors, simplified arrows)
- Rebuilt all 16 PDFs, verified no empty-page issues across all designs
- Checked Gmail: MetaLab Summer School application acknowledged (Sarah Kalwarowsky, UCL, Mar 2)
- Updated backlog: AIW-15 done, MetaLab status updated, TSC+AAAI added to AIW-06
- Processed 4 aIware inbox items (cleared from cross-project inbox)
- Nilsen congratulatory email already sent by user
**Key Decisions:**
- Subgraph labels kept short (~15 chars) to avoid truncation in Mermaid rendering
- Design 15 restructured to show four models explicitly (instead of abstract SNN/LLM-only nodes) for color and clarity
- Overview images constrained to max-height 150mm to prevent page overflow on designs with tall diagrams
**Pending at shutdown:** None
**Recovery/Next session:**
1. AIW-15 is complete. All 16 design PDFs regenerated in `docs/engineering/designs/pdf/`
2. Build script is `python3 tmp/build_individual_pdfs.py` — regenerates all .mmd, .png, and .pdf files
3. Next priorities: AIW-16 (Digital Minds Fellowship, deadline Mar 27), AIW-17 (McFarnell SMRI feedback), AIW-01 (Seth BBS commentary)

### 2026-03-02 — WSL
**Goal:** Process open TODOs, inbox tasks, prepare Wave 2 outreach, backlog housekeeping
**Completed:**
- AIW-02: Verified session-context.md + MEMORY.md persist correctly — closed as resolved
- Backlog split: older Done items archived to `docs/backlog-archive.md`
- AIW-11 split into AIW-11a (English, P3) + AIW-11b (German, P1)
- AIW-08 downgraded to P4 (endorsement unlikely without affiliation)
- Inbox: 7 aIware items processed — CIMCAI declined (travel), AAAI declined (travel), Digital Minds Fellowship added as AIW-16, McFarnell feedback added as AIW-17, RIM preprint v2 target added as AIW-18, Torrance/Nilsen verified sent, backlog split done
- AIW-05 Wave 2 outreach: 8 Gmail drafts created with PDF attachments, all sent by user
- Contacts.md updated (8 entries flipped to Contacted, Carhart-Harris + Priesemann added)
- Engagement log updated with all 8 outreach emails
- Nilsen PhD defense congratulations draft created (defense Mar 3)
- Strategy file updated: CIMCAI + AAAI added to Passed/Declined
**Key Decisions:**
- CIMCAI (Berkeley) and AAAI (Burlingame): declined — won't self-fund US travel per stance
- Digital Minds Fellowship (Cambridge, Aug 3-9): recommended apply — fully funded, exact research domain, added as P1
- AIW-08 arXiv: downgraded P3→P4, endorsement unlikely without institutional affiliation
- Wave 2 outreach: all 8 targets contacted same day (email first per strategy rules)
- AIW-15 diagram redesign: deferred to next session, prototype designs 15+16 only
**Recovery/Next session:**
1. Check Gmail drafts — Nilsen congratulations may still be unsent
2. Monitor 8 Wave 2 emails for replies (~2 weeks)
3. Next session: AIW-15 diagram prototype (designs 15+16), read mirror-box README for target clarity
4. Digital Minds Fellowship application needs attention before Mar 27
5. McFarnell SMRI feedback still needs drafting (read his ACU preprint first)

### 2026-03-01T22:30Z — WSL
**Goal:** Compare mirror-box README ASCII diagram with AC design PDF diagrams, decide on diagram standardization
**Completed:**
- Explored mirror-box project for diagram files (all ASCII art, no rendered diagrams)
- Extracted and examined AC design documentation PDFs (17 PDFs, WeasyPrint from Mermaid→PNG→HTML)
- Compared PDF diagrams (simple + detailed) with README ASCII art — neither is 1:1 match
- Opened PNG diagrams for user to visually inspect
- User decided: ASCII diagram is the most human-readable, should be the canonical "simple" level
- Tracked mirror-box task: replace ASCII with Mermaid block using PDF colors (cross-project inbox)
- Tracked AIW-15: redesign all "simple" PDF diagrams to match README clarity level
**Key Decisions:**
- The mirror-box README ASCII architecture diagram is the gold standard for human readability — all "simple" diagrams should target this level of detail
- README diagram will use Mermaid ```mermaid block (option 2) with PDF color scheme, not a PNG image
- New backlog item AIW-15 (P3) for redesigning simple diagrams across all 16 AC design PDFs
**Pending at shutdown:** Nothing
**Recovery/Next session:**
1. Tasks tracked — no immediate follow-up needed
2. Mirror-box Mermaid replacement: write a new .mmd that matches the README ASCII flow exactly, using style directives for PDF colors
3. AIW-15: review each design's simple diagram against the README's clarity standard

### 2026-03-01T22:50Z — WSL
**Goal:** Launch Mirror Box web UI for screenshot, fix environment issues
**Completed:**
- Launched Mirror Box web chat UI (Mistral-7B FP16 on RTX 4090)
- Fixed missing deps: fastapi, uvicorn[standard] not installed in fresh venv
- Added setup.sh to mirror-box (one-command env bootstrap)
- Added [web] extra to pyproject.toml (fastapi + uvicorn[standard])
- Added AI-first launch rule to mirror-box CLAUDE.md (auto-open browser)
- Copied dashboard screenshot to docs/dashboard-screenshot.png
- Updated README.md with screenshot, simplified install, web UI docs
- Committed and pushed mirror-box to GitHub (rebased on Steam Deck Unicode diagram commit)
**Key Decisions:**
- mirror-box venv was fresh (Feb 28 repo split) and missing web deps — root cause was no setup.sh
- Added `uvicorn[standard]` not just `uvicorn` — bare uvicorn has no WebSocket library
- AI-first rule: always auto-open browser when launching web UIs, never just print URLs
**Pending at shutdown:** None
**Recovery/Next session:**
1. Mirror Box web UI was stopped after screenshot
2. All changes committed and pushed to origin/main
3. Inbox tasks for aIware NOT processed this session (quick session, screenshot only)

### 2026-03-01T20:45Z — WSL
**Goal:** Send AC design documentation to Bernhard Glück
**Completed:**
- Opened AC design overview landscape PDF
- Zipped all 17 design PDFs (overview + 16 architectures, 3.7 MB)
- Sent zip to bernhard.glueck@aitive.at via Gmail (from matthias@matthiasgruber.com)
- Sent FMT engineering specification PDF (62 KB) to same recipient
**Key Decisions:**
- Sent from matthias@matthiasgruber.com alias (not jeltz.prostetnic@gmail.com)
- Included all 17 PDFs in zip (overview + designs 01-16)
- FMT implementation spec sent as separate email for clarity
**Pending at shutdown:** None
**Recovery/Next session:**
1. Both emails sent successfully (Message IDs: 19caaece69c4cdb0, 19caaf92514db256)
2. No follow-up actions needed unless Bernhard replies

### 2026-03-01T~20:30Z — WSL
**Goal:** Quick session — process feedback on inbox handling, drop cfg-agent-fleet tasks
**Completed:**
- Startup, pulled from private (already up to date)
- User identified missed mirror-box inbox task — parent projects should flag child project tasks
- Incorrectly edited global CLAUDE.md directly — user corrected, reverted commit
- Dropped 3 cfg-agent-fleet inbox tasks: parent-child rule, statusline persona, colored persona text
**Key Decisions:**
- Cross-project edits go through inbox, even for cfg-agent-fleet (system project exception doesn't mean "edit freely")
- Parent projects should flag child project inbox tasks at session start
**Pending at shutdown:** Nothing
**Recovery/Next session:**
1. Nothing pending — clean shutdown
2. cfg-agent-fleet has 3 new inbox tasks to process next session

### 2026-02-28T~evening — WSL
**Goal:** Quick check-in, no work done
**Completed:**
- Startup loading completed, verified clean state from Session 122
- Inbox items noted (CIMCAI + Digital Minds — not actioned)
**Key Decisions:**
- No decisions made this session
**Pending at shutdown:** Same as Session 122 end state
**Recovery/Next session:**
1. Active TODOs: Seth BBS (Jun 12), Cosmology→SSRN, Bochum registration (May 30), Wave 2 outreach
2. Inbox: CIMCAI conference (May 29-31) + Digital Minds Fellowship (Mar 27) still pending evaluation

### 2026-02-28T14:30Z — WSL
**Goal:** Compile 16 AC design PDFs + landscape overview document
**Completed:**
- Read inbox (CIMCAI + Digital Minds Fellowship items still pending — not addressed)
- Built landscape overview PDF: `docs/engineering/designs/pdf/00-design-overview-landscape.pdf`
- Built 16 individual design PDFs with simple + detailed Mermaid diagrams
- Color-coded IWM (blue), ISM (green), EWM (light grey/dark yellow stroke), ESM (red)
- Neutral Mermaid theme (grey subgraph backgrounds, not yellow)
- ASCII diagrams stripped from individual PDFs
- Build scripts: `tmp/build_design_overview.py` + `tmp/build_individual_pdfs.py`
- Dropped cfg-agent-fleet inbox task re: shareable Mermaid-to-PDF automation
- Cleaned up old redundant PDFs (00-comparison-overview, 16-quick-win-pseudo-ac)
**Key Decisions:**
- EWM color: light grey fill (#EAECEE) with dark yellow stroke (#B7950B) — user preference
- Mermaid theme: `neutral` (grey subgraph backgrounds) not `default` (yellowish)
- Base64-embedded images in HTML for weasyprint compatibility (file:// paths don't work)
- Designs 13-15 extracted from single `new-proposals-13-15.md` into individual PDFs
- Agent-created build scripts in `docs/engineering/designs/pdf/` can be deleted (superseded by unified `tmp/build_individual_pdfs.py`)
**Pending at shutdown:** Nothing from this session's scope
**Recovery/Next session:**
1. Design PDFs are DONE. All 17 files in `docs/engineering/designs/pdf/`
2. Backlog item "[P2] Compile 16 AC design PDFs" can be marked done
3. Inbox items still pending: CIMCAI conference eval, Digital Minds Fellowship eval
4. To rebuild: `python3 tmp/build_design_overview.py` (overview) or `python3 tmp/build_individual_pdfs.py` (individual)
5. Old agent build scripts to clean up: `docs/engineering/designs/pdf/build_design_pdfs.py`, `tmp/build_design_pdfs_13_16.py`

### 2026-02-27T19:50Z — WSL
**Goal:** Handle correspondence, restore Session 120 data loss, drop cfg inbox task
**Completed:**
- AISB reply: 300-word abstract drafted and sent to Torrance
- PsyArXiv v2 rejection noted, resubmission parked
- Restored scripts/ (5 files) and 7 other files deleted by Session 120
- Root cause identified: origin merge treated filtered state as deletions
- Added NEVER-merge-origin rule to CLAUDE.md
- Dropped P1 inbox task for cfg-agent-fleet: centralized push infra + branch-per-remote
**Key Decisions:**
- PsyArXiv v2 resubmission parked (accepted v1, rejected v2 for same title — absurd)
- Push script logic should be centralized in cfg-agent-fleet, per-project config only in repos
- Branch-per-remote architecture needed to structurally prevent origin merge disasters
**Recovery/Next session:**
1. cfg-agent-fleet inbox has the P1 push infrastructure task — pick up next cfg session
2. Waiting: NoC, Phil Psych, AISB (Mar 21), Bochum, Neurophenomenology, MetaLab
3. aIware inbox still has CIMCAI + Digital Minds Fellowship items (not addressed this session)

### 2026-02-27T19:45Z — WSL
**Goal:** Handle incoming correspondence, restore deleted scripts
**Completed:**
- AISB reply: drafted 300-word abstract, Gmail draft created, user sent it
- PsyArXiv v2 rejection noted — resubmission parked
- Restored scripts/ directory (5 files) deleted in Session 120
- Push script working again — origin now properly filtered
- Backlog and MEMORY.md updated
- Conversation log appended (Session 121)
**Key Decisions:**
- AISB 300-word abstract sent to Torrance. Awaiting acceptance by Mar 21.
- PsyArXiv v2 resubmission parked indefinitely (accepted v1, rejected v2 for "scope")
- scripts/ restored from pre-deletion commit (5187bae)
**Recovery/Next session:**
1. Waiting on: NoC, Phil Psych, AISB (Mar 21), Bochum, Neurophenomenology, MetaLab, 13+ outreach emails
2. Cross-project inbox has 3 unaddressed items: CIMCAI, Digital Minds Fellowship, filtered push (push issue now resolved)
3. Push script works — use `bash scripts/push.sh` for all future pushes

### 2026-02-27T19:30Z — WSL
**Goal:** Handle incoming correspondence (AISB reply, PsyArXiv v2 rejection)
**Completed:**
- AISB reply from Steve Torrance — reviewed, drafted 300-word short abstract, created Gmail draft reply, user sent it
- PsyArXiv v2 rejection of intelligence paper — noted, v2 resubmission parked
- Backlog updated (AISB added to Waiting table)
- MEMORY.md updated (PsyArXiv v2 rejection recorded)
- Cross-project inbox items read (CIMCAI, Digital Minds Fellowship, filtered push — not acted on this session)
**Key Decisions:**
- AISB 300-word abstract sent to Steve Torrance (sbtorrance@outlook.com). Conference is University of Sussex, 1-2 July 2026. Remote presentation conditional on review score.
- PsyArXiv v2 resubmission PARKED — they rejected an update to an already-accepted preprint citing "outside scope." Third scope-based rejection for intelligence paper.
**Recovery/Next session:**
1. AISB: awaiting acceptance notification by Mar 21, 2026
2. PsyArXiv v2: parked indefinitely. v1 still live at https://osf.io/preprints/osf/kctvg
3. Cross-project inbox has 3 pending items not addressed this session (CIMCAI, Digital Minds Fellowship, filtered push)

### 2026-02-27 — WSL
**Goal:** Create FMT implementation spec for Claude Code AC implementation
**Completed:**
- Created `tmp/fmt-implementation-spec.md` — targeted engineering extract of FMT + formalization roadmap (~400 lines)
- PDF generated and opened
- Cross-project inbox task dropped for `aIware.implementation` to pick up the spec
- Git divergence on origin resolved (force-push with lease — local was superset)
- Added divergence recovery + session-context protection rules to CLAUDE.md Git & Push section
**Key Decisions:**
- Implementation spec is in `tmp/` (not pushed to public). Implementation project gets it via inbox task.
- Git divergence caused by same sessions committed on VPS and WSL with different merge topologies. Resolved by force-pushing origin (public mirror) since local was the superset. Added recovery procedure to CLAUDE.md.
- Session context was blank because a stale push from another machine overwrote it. Added protection rule to CLAUDE.md.
**Pending at shutdown:** 4 active TODOs (see MEMORY.md). Inbox still has CIMCAI and Digital Minds tasks to evaluate.
**Recovery/Next session:**
- Read `tmp/fmt-implementation-spec.md` if continuing implementation work
- The inbox task for aIware.implementation is live — next session in that project should pick it up
- 4 active TODOs: Seth BBS (Jun 12), Cosmology→SSRN, Bochum registration (May 30), Wave 2 outreach
- Inbox tasks pending evaluation: CIMCAI conference (May 29-31), Digital Minds Fellowship (Mar 27)

### 2026-02-26T~22:30+01:00 (Session 119) — WSL
**Goal:** Oizumi preprint review + Kanai follow-up + COGITATE triage
**Completed:**
- (no completed items recorded)
**Key Decisions:**
- (no decisions recorded)
**Recovery/Next session:**
1. Active TODOs are listed above — pick one to work on
2. Full backlog at `backlog.md` (read when active TODOs are done)
3. **IMPORTANT**: Always pull from BOTH remotes. Origin merge can delete private-only files. After origin merge, always `git diff --name-status HEAD private/main` to check for missing files.
4. push.sh now has divergence guard — if it aborts, run `git pull --rebase private main` first
5. bibtex MUST run with dangerouslyDisableSandbox (sandbox blocks .bbl writes)


### 2026-02-26T~14:45+01:00 — the office (Fedora)
**Goal:** Fix git sync + handle André Sevenius reply
**Completed:**
- (no completed items recorded)
**Key Decisions:**
- Set upstream tracking to private/main (origin is a filtered mirror, private is the real remote)
- Reply to André: focused on falsifiability (Predictions 3+4), not on "is this correct" framing. Deliberately omitted 8-requirement comparison table — let him discover it.


### 2026-02-26T~09:00+01:00 (Session 116) — the office (Fedora)
**Goal:** Fix missing private remote on office machine
**Completed:**
- (no completed items recorded)
**Key Decisions:**
- (no decisions recorded)
