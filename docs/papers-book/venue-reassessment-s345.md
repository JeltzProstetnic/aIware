<!-- Action: await-user-decision -->
<!-- Tracked-by: AIW-292 -->
# Venue re-assessment of all papers (AIW-292, S345, 2026-10-20)

**Verdict:** six papers can go to a no-fee journal now or after one prep session. Three papers wait for JAIC.
One sits at JCS. The rest are blocked, are not journal papers, or should stay preprints.

**MG's criteria applied, in order:**
1. **Effort for MG.** Email or an OJS upload of one PDF is low. A Springer or Elsevier Editorial Manager
   submission (title page, declarations, .docx/.tex) is medium. Medium plus reviewer nominations, highlights and
   many forms is high.
2. **No journal that rejected us.** Rejected so far: NoC ×2, PLREV, NBSR and C&C (FMT); Philosophical Psychology,
   Theory & Psychology and New Ideas in Psychology (RIM); the BBS commentary call. Peer commentaries are exempt
   (S325). The S324 pause was lifted in S337, so the NoC special issue is technically open again. It is still a
   rejecting venue, so it goes to MG as decision D3.
3. **APC.** No APC for RIM (MG 2026-08-10). Every other APC is flagged below, and venues without one are preferred.
4. **Preprints.** Every paper is or will be on Zenodo, so the venue has to accept a public preprint.
5. **Blinding.** We are an independent author, so double-blind beats single-blind. A Zenodo preprint stays
   findable by reviewers. Every double-blind venue below allows preprints anyway.
6. **One paper at a time.** JCS is taken by `AIW-46` (submitted 2026-10-19). A journal gets a second paper from
   us only when nothing else fits.

**Verification:** "live 2026-10-20" means fetched today from the journal's own page with curl or the
r.jina.ai reader. "2026-10-18" means verbatim from `venues-paper1.md`. "2026-10-19" means the backlog record
(JAIC: `AIW-290`; JCS: `AIW-46`). Anything else is marked UNVERIFIED. These pages blocked every method today:
OUP (Philosophia Mathematica), SAGE (Review of General Psychology), APS (Phys Rev D) and Elsevier *Intelligence*.

---

## 1. JAIC candidates (wait for the Suzuki/Kanai reply, `AIW-290`)

The enquiry went out 2026-10-19 17:21 to Suzuki, cc Kanai. It asks which paper JAIC wants first.

**JAIC facts (verified 2026-10-19):**
- Hybrid journal; no fee unless open access (APC US$2,200).
- No word limit stated. Abstract ≤150 words, ≤6 keywords.
- Submission via Editorial Manager (wspc-jaic), so medium effort.
- Blind type and preprint policy are **UNVERIFIED**. Ask in the reply thread.

| Paper | Status | Words (md, incl. refs) | Fallback if JAIC declines | Blockers |
|---|---|---|---|---|
| **An Operational Detector for Machine Consciousness** (`AIW-130` Lane B) | draft, not on Zenodo | 11,278 | *Minds and Machines* (facts in §2 row 5). That collides with the NoC slice, so the slice moves if both need it. | 4 open MG decisions; §6 in-silico grounding has no owner; no `.tex`/figure build |
| **Silent suffering** (robot plea) | Zenodo `10.5281/zenodo.23479963` | 6,052 | *Nature Machine Intelligence* Perspective via presubmission enquiry (S334 brief). Limits and APC **UNVERIFIED** | none for JAIC |
| **The Worm on the Disk** | Zenodo `10.5281/zenodo.23474833` | 8,949 | **→ *Minds and Machines* (MG S348 2026-10-21; Synthese now holds the Hard Problem paper). Scope fits (philosophy of computer science; computational approaches); double-blind; abstract 150–250 words; no article word cap found on the guidelines page; hybrid (subscription route free).** ~~*Synthese*~~. No word cap; double-blind; free subscription route (APC £2,390 only for OA); Springer preprint policy OK (2026-10-18) | none |

The eNeuro opinion is filed under `AIW-290`, but it was **not** offered to JAIC. It is handled as a non-JAIC
paper in §2.

---

## 2. Non-JAIC papers: one selected venue each, plus a fallback

### 2a. Ready, or one prep session away

| # | Paper | Status | Words | Selected venue: verified facts | Fallback | MG effort | Blockers / prep |
|---|---|---|---|---|---|---|---|
| 1 | **What a Rejection Cost** (falsity gradient) | Zenodo `10.5281/zenodo.23478568` | 6,908 | ***Studies in History and Philosophy of Science*** (Elsevier; MG named it in S339). ≤12,000 words incl. abstract, footnotes and refs. **Double-anonymized**; separate title page. Elsevier icon "Supports open access" = hybrid, with a free subscription route. Preprints *"will not count as prior publication"*. Portal: submit.elsevier.com/SHPS (Editorial Manager). Highlights are an optional separate file. *Live 2026-10-20*, sciencedirect.com/journal/studies-in-history-and-philosophy-of-science/publish/guide-for-authors | *Journal for General Philosophy of Science* (Springer). ~10k soft cap; free route (OA APC €2,790); Springer AI and preprint policy (2026-10-18) | med | anonymised .docx/.tex; title page; AI statement. None blocking |
| 2 | **Limits Without an Outside** (paper 1) | Zenodo `10.5281/zenodo.23494694` | 9,350 | ***Logique et Analyse*** (Peeters / CNRL). Scope: *"Logic and Philosophy of Logic / Philosophy of Mathematics / Philosophy of Language / Formal Philosophy"*. ~15–20 pages; **single PDF upload via OJS** (logiqueetanalyse.be/ojs). Double-blind when the PDF is anonymised. Subscription journal; no author fee found. Postprint deposit with no embargo. Preprint policy: the checklist says *"not previously published … (or an explanation has been provided in Comments to the Editor)"*, so declare the Zenodo DOI there. *Live 2026-10-20*, logiqueetanalyse.be/submissions.html + about.html | *Philosophia Mathematica* (OUP). Double-blind; no word cap; abstract ≤100 words; author's original version may be public; APC UNVERIFIED. 2026-10-18; Cloudflare-blocked today | **low** | anonymise the PDF (fn 1 and the No Outside self-citation); AI statement. Whether LeA's AI policy and acceptance of preprints hold: **UNVERIFIED** (a one-line Comments note covers it) |
| 3 | **Too Late to Report** (minimal self) | Zenodo `10.5281/zenodo.23495402` | 10,058 | ***Phenomenology and the Cognitive Sciences*** (Springer). *"average submission is approximately 9,000 words (including references), and submissions larger than 10,000 words are discouraged"*. **Double-blind**; separate title page. Hybrid with a subscription route; APC only for OA (amount UNVERIFIED). Springer preprint policy. Editorial Manager. *Live 2026-10-20*, link.springer.com/journal/11097/submission-guidelines + how-to-publish-with-us | *Review of Philosophy and Psychology* (row 4 facts). If row 4 goes there, use PhiMiSci after D4 | med | trim ~200–700 words to stay ≤10k incl. refs; anonymise; Allen/MoC7 citation consent (decision #5) |
| 4 | **Where the Theories Sit** (theory map) | Zenodo `10.5281/zenodo.23496102` | 11,181 | ***Review of Philosophy and Psychology*** (Springer). *"The general length of our papers are 8000-10,000 words (including references, footnotes, tables and figures)"*. **Double-blind**. Hybrid with a subscription route; APC only for OA. Editorial Manager. *Live 2026-10-20*, link.springer.com/journal/13164/submission-guidelines | *Philosophy and the Mind Sciences* (PhiMiSci). No word limit (≤20k); **double-blind**; **free for authors** (*"not-for-profit open-access journal that is free for authors and readers"*); single PDF upload via OJS (low effort); a preprint is noted in "Comments for the Editor". AI: *"extensive use … strongly discouraged"*, disclosure required. *Live 2026-10-20*. **Blocked by S325 until the JAIC slice is out (D4)** | med | **cut ~1,200 words** to fit 10k; independent coder for Table 1 (`AIW-313`, D9) |
| 5 | **More Than Computation, Made of Computation** (NoC slice, `AIW-103`) | draft, **not on Zenodo** | 9,175 | ***Minds and Machines*** (Springer). *"Journal for Artificial Intelligence, Philosophy and Cognitive Science"*; computational approaches to philosophical issues. **Double-blind**. Hybrid with a subscription route. Editorial Manager; *"The author should suggest up to six reviewers"*. Word limit **not stated**. *Live 2026-10-20*, link.springer.com/journal/11023/submission-guidelines + aims-and-scope | NoC special issue (deadline 2026-12-31). **Rejecting venue ×2, single-anonymized, fully OA with APC US$3,625 and no free route** (verified 2026-07-28, stale). Only on MG's explicit go (D3) | high (reviewer list) | reframe away from the CFP wording; re-check the thesis against S329 (criticality not required); Zenodo deposit first (AIW-298 Z8) |
| 6 | **Near-criticality does not set the level of consciousness** (eNeuro opinion, `AIW-290`) | manuscript, **not on Zenodo**; 3 register hits | 3,971 | ***Cortex*, Viewpoint** (Elsevier). *"mini-review, position papers on relevant topics which do not report new experimental data. They can be submitted spontaneously"*. No limit stated for Viewpoints. **Single-anonymized** (affiliation visible). Hybrid with a subscription route. Preprints allowed. Elsevier portal; highlights *"encouraged"*. *Live 2026-10-20*, sciencedirect.com/journal/cortex/publish/guide-for-authors | *eNeuro* Opinion. ≤4,000 words, **≤10 references** (draft has 18), 2 figures; double-blind; posting a preprint *"is not considered prior publication"*. **APC US$1,945 for non-members**. *Live 2026-10-20*, eneuro.org/content/information-authors | med | Zenodo deposit; register hits; de-anonymise for Cortex; D5 (Cortex vs eNeuro) |

### 2b. Blocked, or not ready for a journal yet

| # | Paper | Status | Words | Selected venue | Fallback | Effort | Blockers |
|---|---|---|---|---|---|---|---|
| 7 | **Pointing Is Not Defining** (Def A, `AIW-278`) | draft, PDF built, not on Zenodo | 8,997 | **PhiMiSci** (facts in row 4) | **JCS** once `AIW-46` is decided (9k incl. refs, email, no APC, double-blind; S342) | low | **waiting for Signorelli** (co-authorship); D4 |
| 8 | **Deriving a Definition…** (Def B, `AIW-279`) | draft | 8,848 | **Synthese** (facts in §1, worm row; 2026-10-18) | *Review of Philosophy and Psychology* | med | cites Def A, so it follows Def A; AI statement missing; "connectome" ×2 (AIW-206) |
| 9 | **Permeability as Directed Information Flow** (`AIW-291`) | manuscript; PDF stale; no review | 3,738 | ***Cognitive Neurodynamics*** (Springer). Abstract 150–250 words; Editorial Manager; hybrid with a subscription route. **Blind type and length UNVERIFIED** (live 2026-10-20, link.springer.com/journal/11571/submission-guidelines) | *Minds and Machines* | med | AIW-288 wording (8 hits); 3 register hits; AI statement; first review; Zenodo |
| 10 | **Privacy of Qualia as a Decompilation Problem** (`AIW-105`) | first draft, July | 4,397 | **PhiMiSci** (UNVERIFIED for fit until rewritten) | *Synthese* | low | predates v15–v23; 9 VERIFY; AIW-206 frozen terms (21 hits) |
| 11 | **CMB multifractal** (`AIW-63`) | Zenodo `10.5281/zenodo.20306785` | 6,717 | ***Physical Review D*** (backlog target). **All facts UNVERIFIED**: APS blocked every fetch today | *JCAP* (UNVERIFIED) | med | **positive control `AIW-163` first** |
| 12 | **RIM**: Motivation as Allocation Policy… (`AIW-36`) | Zenodo `10.5281/zenodo.20125095` | ~7,900 body | ***Review of General Psychology*** (APA/SAGE). Theory journal; *"5,000 to 10,000 words … as long as 15,000 … inclusive of references"* (**search-index snippet only**; SAGE page 403 today). Blind type, APC route and preprint policy **UNVERIFIED** | *Intelligence* (Elsevier, hybrid; page unreachable today, **UNVERIFIED**) | med | **APC must be €0** (MG 2026-08-10); AIW-227 rulings (Prediction 5) still open; D6 |

### 2c. Already placed, closed, or not journal papers

| Paper | Status | Venue |
|---|---|---|
| **Why the Hard Problem Looks Unbridgeable from Inside** (JCS carve, `AIW-46`) | Zenodo `10.5281/zenodo.23480985` | **Under consideration at JCS** since 2026-10-19. Fallback if JCS rejects: PhiMiSci |
| **What the loop carries** (PLR "Loops" commentary, `AIW-228`) | Zenodo `10.5281/zenodo.23478413` | Zheng: the commentary window is closed. Blog + preprint, **no journal** |
| Seth BBS commentary | Zenodo | BBS call closed (2026-05-29). **No journal** |
| Skeptic response (`AIW-294`) | pitch sent | Magazine, not a journal. Waiting for the reply |
| Two Roads to Recursive Closure (Olinyk, `AIW-120`) | draft | Zenodo/blog by MG's pivot; **no journal** |
| **FMT master** (v23) | Zenodo `10.5281/zenodo.18669891` | ~38k+ words; no journal can take it (S244). Stays a preprint; PhilSci-Archive optional |
| Companion (in-silico tests) | Zenodo, v5 | Counts as published (MG S342); no journal planned |
| SB-HC4A cosmology | Zenodo | "Cosmology rests" (S316); SSRN upload only (`AIW-03`) |
| Formalization roadmaps ×3 | Zenodo | Not journal papers |
| *No Outside* (book) | Zenodo `10.5281/zenodo.23473517` | Book; KDP via simbook |
| McFarnell registered report (`AIW-48`) | idea | *Cortex* RR, now submitted via Peer Community in Registered Reports (Cortex page, live 2026-10-20) |
| Span rule (`AIW-219`), COGITATE commentary (`AIW-14`) | not drafted / parked | none |

---

## 3. Proposed submission order (non-JAIC)

The order puts ready preprints first and then MG's lowest effort. It puts at most one paper in any journal.
**Recommended pace: one submission per session.**

1. **Limits Without an Outside → Logique et Analyse.** Lowest effort (one anonymised PDF, OJS) and ready now.
2. **What a Rejection Cost → SHPS.** Ready now; MG chose the venue in S339.
3. **Too Late to Report → Phenomenology and the Cognitive Sciences**, after a small trim to ≤10k.
4. **Where the Theories Sit → Review of Philosophy and Psychology**, after the ~1.2k cut (and the coder, if D9 says
   wait).
5. **eNeuro opinion → Cortex Viewpoint**, after Zenodo deposit and the register fix.
6. **NoC slice → Minds and Machines**, after the S329 thesis check and Zenodo deposit.
7. Later, once unblocked: Def A → PhiMiSci (Signorelli), Def B → Synthese, RIM → RGP (D6), CMB → PRD (AIW-163),
   permeability, qualia.

Two prep steps apply to every submission:
- an anonymised copy, built in `tmp/` and never from a canonical PDF;
- the inline AI statement worded per the S334 ruling. The ruled wording discloses prose drafting. JCS's policy
  conflicts with that wording (AIW-46), so check each venue's AI wording when its kit is built.

---

## 4. Decisions for MG (recommended option first)

- **D1:** Order in §3. **(a) Accept, one submission per session (Rec.)** / (b) submit everything ready in one batch.
- **D2:** Venue for paper 1. **(a) Logique et Analyse: lowest effort, best scope (Rec.)** / (b) Philosophia
  Mathematica / (c) Kriterion (6–8-week decision, but gold OA ~€1,500 with a waiver on request).
- **D3:** NoC special issue (deadline 2026-12-31). **(a) Skip it: NoC rejected us twice, review is single-blind,
  and there is no free route, APC US$3,625 (Rec.)** / (b) submit the slice there anyway.
- **D4:** PhiMiSci deferral (S325: none until the JAIC slice is out). **(a) Keep it; PhiMiSci stays a fallback
  only, because its AI policy "strongly discourages" extensive AI use (Rec.)** / (b) lift it now and move the theory
  map there (lower effort, free).
- **D5:** eNeuro opinion. **(a) Cortex Viewpoint, no fee (Rec.)** / (b) eNeuro Opinion: double-blind, but US$1,945,
  and the refs must be cut to 10.
- **D6:** RIM. **(a) Keep the preprint as the publication until AIW-227 closes, then RGP if it verifies at no fee
  (Rec.)** / (b) send it to RGP now.
- **D7:** JAIC reply handling. **(a) Wait up to 3 weeks after 2026-10-19, then send the detector via Editorial
  Manager unasked (Rec.)** / (b) wait indefinitely.
- **D8:** Preprint disclosure at double-blind venues. **(a) Name the Zenodo DOI only where the venue asks (LeA,
  PhiMiSci) and in the cover letter, never in the manuscript (Rec.)** / (b) disclose everywhere.
- **D9:** Theory map and the independent coder (`AIW-313`). **(a) Submit without the coder and add the coding in
  revision (Rec.)** / (b) wait for the coder first.
