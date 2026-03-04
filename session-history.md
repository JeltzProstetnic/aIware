# Session History

Rolling window of the last 3 sessions. Newest first.

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

