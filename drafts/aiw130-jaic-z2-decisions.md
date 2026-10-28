<!-- Tracked-by: AIW-298 (Z2), AIW-130. Decision list for MG, JAIC detector draft. 2026-10-19. -->
# JAIC detector paper: decisions for MG (Z2)

Review PDF: `tmp/z2-jaic/aiw130-jaic-z2-review.pdf` (23 pp). Changes: `drafts/aiw130-jaic-z2-changelog.md`.

**Length vs JAIC limits:** body 9,721 words; JAIC sets no word or page cap. Abstract 147 of 150 words, keywords 6 of 6.
Single-blind, up to 4 suggested reviewers, figures EPS at 300 dpi or more (`paper/jaic/journal-guidelines-jaic.md`).

**Tracking conflict, not reconciled:** the readiness plan (row #3) lists four decisions as open. `aiw130-PROPOSE.md`
and backlog `AIW-130` record answers for all four. Two of the four (article type, time dilation) were NoC questions.
The status below is taken from those records; please confirm which is right.

---

**J1. Article type.** Recorded: JAIC built as a Research Article, section "Assessing AI Consciousness". MG's confirmation
(2026-07-30) was for the NoC paper; no JAIC-specific confirmation is on file.
- **(a) Research Article (recommended).** No length cap, so nothing pushes toward a shorter type; the section remit names "tests" and "formal frameworks".
- (b) A shorter type. Would need cuts to §5–§6 for no gain.

**J2. Time dilation, keep or cut.** Recorded: a NoC item; MG confirmed "keep" for NoC on 2026-07-30. The JAIC draft
contains no time-dilation passage.
- **(a) Close as not applicable to JAIC (recommended).**
- (b) Add it to JAIC. It has no role in the detector.

**J3. Reviewer slate.** Recorded: Kleiner, Wiese, Mediano approved by MG 2026-08-02, no fourth; Suzuki dropped (co-authored with Kanai). Kleiner and Wiese both sit on the MoC7 organising committee; Kleiner is also on the JAIC board.
- **(a) Keep the three; re-run the COI check at submission (recommended).**
- (b) Add a fourth (candidates on file: Aru, Schneider, Graziano), after the same COI check.

**J4. Named vs generic neuromorphic examples.** Recorded: MG chose named examples (2026-08-02); slate confirmed S299:
Sandamirskaya (DNFT/attractors), Zou (SpikingMCU), plus one more not yet chosen. **The draft still has the generic
example in §6(c); the named text was never written.**
- **(a) Write §6(c) with the two named architectures now, report where each fails, and leave the third slot open until MG picks it (recommended).** A heads-up to Sandamirskaya goes through social before the Zenodo deposit, since the deposit makes the analysis public.
- (b) Deposit with the generic example and add the named ones for the journal version.
- (c) Name a third now (no candidate is on file; I have not proposed one).

**J5. §6 in-silico grounding has no owner** (Frey left the paper, S302). §6(a) already calls the spiking substrate
"a specified but not-yet-instantiated design"; §6(b) reports only companion results (Gruber, 2026b, v4) and states the
scaled test as open.
- **(a) Deposit with §6 as written, grounded on the published companion (recommended).** Nothing in it claims an unbuilt result.
- (b) MG owns building the minimal spiking substrate (§6a) before deposit.
- (c) Hand the build to crucible as a separate item and cite it later.

**J6. Editor-in-chief: Kanai or Suzuki.** Stored guidelines (S216) say Kanai, with the homepage's "Chella" called stale;
Suzuki described himself as chief editor (contacts #64). Not reconciled. The WS editorial-board page returned 403 to a script today. Matters for the cover letter and COI, not for Zenodo; the S339 route is a presubmission enquiry to Suzuki.
- **(a) Keep the cover letter addressed to "the Editor-in-Chief and Editors", and ask Suzuki in the presubmission enquiry (recommended).**
- (b) MG checks the editorial-board page in a browser before the enquiry.

**J7. New from v20: embodiment and the pain-pleasure axis.** The v20 sufficient condition has four parts (§3.7.3).
The three checks establish closure and free compute; embodiment is presupposed by check 1 and the valence axis is
tested by nothing. Z2 states this in §3, §4 Output, §6(c) and §8 and makes a positive verdict conditional on both.
- **(a) Keep it as now written: the two are preconditions read from the architecture (recommended).**
- (b) Add a fourth check for a pain-pleasure axis (needs an intervention and a readout; a new §4 subsection).
- (c) Narrow the paper's claim to "necessary conditions only" and drop the verdict-to-attribution step.

**J8. Figure labels.** Tracked `figures/aiw130/jaic-fig1/2` still say "gates" and "Graded conscious-or-not verdict";
the review PDF uses corrected copies. Fig. 2 also draws closure as one arrow (self → world), while Box 1 and v20 §3.5
need the two models to close on each other.
- **(a) Apply F1–F3 to `scripts/gen-aiw130-figures.py` and add the return arrow world → self in Fig. 2 (recommended).**
- (b) Labels only.
