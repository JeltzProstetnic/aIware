# Decisions Log — aIware

Curated record of strategic decisions and rationale. Topic-organized, not chronological.

---

## Zenodo v5 Blocked on Deep Revision (2026-04-16, Session 189)

**Decision:** Do NOT upload Zenodo v5 until AIW-51 sub-tasks complete (1-2 weeks of focused revision).

**Why:** Session 189 ran 5 parallel Opus reviews (editor, neuroscience, philosophy-of-mind, structural, clarity) on the current full FMT paper. All 5 independently converged on the same desk-reject signals: §3.4 self-referential closure stipulated-not-argued, "virtual" used in 3 incompatible senses, criticality never operationalized to a concrete neural signature, §9 OQ2 paragraph lectures editors, abstract buries thesis 70 words deep, zero figures for a 2×2 theory, REM phenomenology still wrong after Andrillon's NoC flag. Uploading v5 with these unfixed would cement the sixth-rejection trajectory into the public record.

**Highest-leverage edit:** §3.4 rewrite as centerpiece (~1500 words, weather-sim contrast example). All 5 reviewers named this as the load-bearing move.

**Full consolidated review:** `docs/pre-zenodo-v5-review-2026-04-16.md`. Sub-task checklist: AIW-51 in `backlog.md`.

**Follow-up:** After v5 upload, reassess whether to continue AIW-07 (journal submissions) or commit fully to the Session 184 pivot (AIW-46 JCS + AIW-47 salami-slice + AIW-48 McFarnell + AIW-49 BBS).

---

## STRATEGIC DIRECTION — Two Paths to Breakthrough (2026-03-16)

**Decision:** The primary long-term goal across aIware AND scifi is achieving a breakthrough in ONE of two domains — either as a recognized consciousness researcher OR as a successful sci-fi author. Either path unlocks the other:

- **Sci-fi success → research credibility:** A best-selling author writing about consciousness gets invited to conferences, gets media coverage, gets taken seriously by academics who otherwise desk-reject outsiders. (Precedent: Hofstadter, Watts, Egan — fiction writers who became intellectual forces.)
- **Research breakthrough → author platform:** A validated consciousness theory makes the pop-sci book and any fiction instantly compelling. "The scientist who solved consciousness writes novels" is a story that sells itself.

**Why:** 8+ books written, zero fame, zero newspaper coverage, 5+ desk rejections with zero peer reviews, 13+ unanswered outreach emails. The bottleneck is not quality — it's distribution and credibility. An outsider without institutional affiliation faces a catch-22: need fame to publish, need publication to get famous. Breaking through on EITHER front shatters this loop.

**Implication:** Both projects (aIware, scifi) should be evaluated against this goal. Tactics that increase visibility, create external validation, or build platform in EITHER domain are high priority. Pure craft improvements without distribution impact are lower priority.

**Shared with:** scifi project (via cross-project inbox).

---

## Co-Author Strategy (2026-03-16)

**Decision:** Actively pursue a co-author with academic institutional affiliation for the consciousness paper (FMT). This is the single highest-leverage move for the research path.

**Why:** An institutional co-author solves: (1) desk-rejection filtering by affiliation, (2) adds empirical credibility, (3) provides access to journal networks and reviewer pools, (4) enables grant applications.

**Candidates (ranked by co-author fit — research Mar 16):**

| Rank | Candidate | Institution | Why | Status |
|------|-----------|-------------|-----|--------|
| 1 | **Andrea Luppi** | Cambridge/Oxford | Wellcome Early Career Fellow, "Rising Star 2025", PNAS taxonomy paper parallel to FMT, building independent identity — needs frameworks. Best career stage. | PITCHED 2026-03-16 |
| 2 | **Megan Peters** | UC Irvine → UCL 2026 | Research question = "how does the brain build representations of world and self" (verbatim FMT). Moving to UCL = fresh start. Adversarial collab leader, community builder. | PITCHED 2026-03-16 |
| 3 | **Pedro Mediano** | Imperial College | Lecturer (= Asst. Prof.), information theory, PID. One exchange Mar 2 — replied positively, asked about datasets, then silence. | LUKEWARM — needs re-engagement hook |
| 4 | **Michael Pitts** | Reed College | COGITATE, replied positively Mar 12. Plans to read paper. | WARM — awaiting his read |
| 5 | **Tomas Marvan** | Czech Academy of Sciences | CC'd by Kob. Philosophical angle — good for BBS commentary, not empirical co-authorship. | ONE EXCHANGE |
| 6 | **Viola Priesemann** | MPI Göttingen | Criticality/neural dynamics = FMT C4CA substrate layer. Moderate overlap. German-speaking. | NOT YET CONTACTED |

**Excluded:**
- **McFarnell** — independent, no affiliation. Two outsiders ≠ one insider.
- **Northoff** — too senior (350+ papers, 28k citations, Canada RC Tier 1). Would absorb FMT into his TTC brand.
- **Blanke** — too senior (EPFL founding director, commercial interests). Wrong collaboration mode entirely.
- **Shriki** — pitched Feb 13, no reply. Keep as citation target.

**Approach:** Don't ask "will you co-author?" — ask "what would you add/change?" Collaboration proposals emerge from intellectual engagement, not cold asks. Bochum (May 30) is the single best opportunity — conferences convert email ghosts into real relationships. Bring a one-pager (bubble diagram + 3 predictions). Target mid-career researchers at poster session, not headliners.

**Next actions:**
1. Email Luppi — pitch FMT taxonomy as complement to his information decomposition taxonomy
2. Email Peters — time for late 2025/early 2026 UCL transition window (or Bochum if she attends)
3. Re-engage Mediano with Bochum attendance question or new result

---

## German Book Publication on KDP (2026-04-15)

**Decision:** Publish "Die Simulation namens Ich" on KDP in all three formats (Kindle eBook, paperback, hardcover) using KDP-free ISBNs, with KDP Select + 70% royalty for the Kindle edition.

**Why:**
- KDP-free ISBNs: zero cost, Amazon-exclusive, fastest path — matches the English edition approach.
- KDP Select for Kindle: Kindle Unlimited inclusion is the main discovery channel for niche German philosophy/consciousness titles (Tolino/Kobo market share <10% in DE for this category). Low-regret: opt out after 90 days if needed.
- 70% royalty at €6.99 list price: ~€4.58 net per sale vs €2.45 at 35%. Standard tier for German pop-sci.
- Translation metadata flagged during setup: Amazon auto-links the German and English editions on product pages within 2-14 days via the "This is a translation" fields.

**ISBNs:**
- Paperback: 9798257520600 (KDP-free)
- Hardcover: 9798257524424 (KDP-free)
- Kindle: ASIN assigned by Amazon

**Technical decisions baked into `tmp/build_book_pdf_de.py`:**
- `\rotatebox{90}{\begin{minipage}{7.25in}}` for landscape tables (NOT `pdflscape`) — pdflscape stores content at `/Rotate 90` coordinates that KDP's preflight reads without applying the rotation, causing false "insufficient gutter" errors with content appearing 2"+ past page bounds. Rotatebox embeds the rotated table inside the portrait text frame, all content stays in the page rectangle.
- `\footnotesize` default for German tables (vs `\small` for English) — German compounds require smaller font.
- `ragged2e` Y/Z column types with `\hspace{0pt}` trick + explicit `\hyphenpenalty=0` to force hyphenation of long compounds in tabularx cells.
- Soft-hyphen dict in `convert_table_cell()` for 15+ stubborn compounds (Selbstbewusstsein, Bewegungsverarbeitung, etc.) where hyphenation patterns don't fire inside tables.
- Pandoc EPUB reader: `-simple_tables-multiline_tables` to prevent pandoc from interpreting `---` horizontal rules as table delimiters (bug that wrapped Der Autor → Kapitel 3 content in a 6%-wide phantom table).

**Coda fractal-dream reframe:** The original "Die Umstände lasse ich aus" (circumstances I'll leave out) in the Coda made it obvious the fractal experience was a drug reference. Rewritten as "Und dann gab es den wiederkehrenden Traum aus meiner Kindheit — nur war ich dieses Mal selbst ein animiertes vierdimensionales Fraktal." Hooks back to the Chapter 7 recurring childhood fractal landscape dream — narrative coherence preserved, no drug hint.
