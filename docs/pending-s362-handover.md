<!-- Action: reference -->
<!-- Superseded by docs/pending-s363-handover.md (S362 shutdown) -->
<!-- Tracked-by: AIW-351, AIW-352, AIW-343, AIW-312, AIW-353, AIW-354, AIW-349, AIW-350 -->
# S361 → S362 handover

S361 closed the S361 handover:
- FMT v29 published (10.5281/zenodo.23660780).
- ResearchGate window used: FMT file swap, slice added, Formalization FMT details, SB-HC4A title and DOI, Emergenz added as a Book.
- AIW-344 Anthropic call skipped.
- AIW-343: Stanovich permission (12-item dualism block), GDPR/ethics fixes, BFI-10 verified, blind-spot demo checked.
Decisions: `docs/decisions.md` D-S361-1..5.

## 1. DUE Thu night 2026-10-29 — MG S362: work on it after 23:00 2026-10-27 (token window) or on 10-28 — AIW-351 (P0): Jülich call prep, with crucible
**S362: Michiel moved the call to Fri 2026-10-30 10:00 CET** (his FZJ Zoom, ID 659 3774 0772; thread `1a1162b7de992656`). On the fleet calendar (call + brief-due Thu 20:00). MG: JSC might volunteer massive free compute.

Deliver a one-page brief covering:
1. What we would run at JSC scale.
2. The overlap with his minimal self-reflexive reservoir (Lyapunov + DFA self-monitoring).
3. The concrete ask.

Inputs: crucible (inbox item filed), and the in-silico paper (concept 10.5281/zenodo.21610993), whose "scaled closure-driven test is not attempted here" is the natural ask. Contacts row 58.

## 1b. After 23:00 2026-10-27 — MG: `lrn` on the alias mistake
The S362 Mason thank-you went out from matthias@ instead of research@: the draft was created with from_email=research@ (google-workspace), then edited with claude_ai Gmail `update_draft`, which has no from field and dropped the alias. Same window: AIW-351 brief, AIW-356 discussion, JAIC submissions (AIW-355 + AIW-130, promised ~2026-11-02).

## 2. From Wed 2026-10-28 (MG's trigger was 'after tuesday'; unchanged by the call move) — AIW-352: run `lrn` (full self-audit). MG: "track for yourself after tuesday to lrn".

## 3. Reminders (MG S361, D-S361-5)
No cloud routines for reminders. Use our own calendar/reminder system, which is to be made to reach both MG and agent sessions. cfg has the rule change and infrastructure has the delivery; both inbox items are filed. Until it works, items 1 and 2 above live only here and in the backlog.

## 4. ResearchGate, next edit window (AIW-312, AIW-354) — ~3 edits per day
1. Emergenz (416881014): description + CC BY-NC-ND 4.0 via Edit. The text recipe is in `.claude/knowledge/researchgate-ops.md` (S361 note).
2. Add *The Simulation You Call "I"* as a Book **without full text** (MG: the book stays commercial).
3. Check FMT/RIM items for version DOIs in the DOI field.
4. **S362:** swap the In-Silico Tests file (RG 416595850) for companion v6 (`tmp/zen-companion-v6/companion.pdf`, Zenodo 10.5281/zenodo.23702509).

## 5. Waiting
- **Oliver Mason** (Surrey): wording of O-LIFE item `une_11` + permission to use the items. Sent 2026-10-26 10:34. Do not field `une_11` before his answer.
- **Netzer / RCSEQ** (AIW-343): next step is the RCSEQ Stammblatt via Netzer before fielding. If he declines, a commercial exempt determination (`docs/research/aiw343-ethics-review-impact.md`).
- **Infrastructure:** survey log/IP check and privacy-page wording; the FMT v29 redeploy; Copenhagen wayfinder retirement; Stephanie passkey.
- **competitor-radar:** the weekly sweep moves to the Ivoclar Azure AI, mail to Stephanie.
- **simbook:** Emergenz cover page (AIW-353).
- Earlier waits unchanged: O'Keefe, institute, ROPP, Logique et Analyse, Graham/JCS, Signorelli (~1 Nov), M&M editor for both manuscripts.

## 6. Decisions for MG (ask with AskUserQuestion)
- **S362-1 RESOLVED S362 (D-S362-4): keep No Outside as Preprint.** ~~No Outside's type on RG.~~ MG asked why Emergenz is a Book and No Outside is not. The reason: Zenodo types No Outside as *Preprint* (record 23473517, v1.0.3) and Emergenz as *Book*, and each was added through the matching RG flow. Options:
  - (a) keep No Outside as Preprint, recommended if it is a monograph-length essay published as a preprint;
  - (b) retype it as Book on Zenodo (new metadata version) and on RG (one edit);
  - (c) Book on RG only.
- **S362-2 RESOLVED S362 (D-S362-5): P2.** ~~AIW-349/350 priorities.~~ Both are cfg pointer clean-ups (prose-register and publication-build now ship fleet-wide). Proposed P2; MG did not confirm. Options: (a) P2 (recommended), (b) P3.

## Notes
- The Gmail compose hook says threaded drafts are invisible. Always create drafts standalone. Agent draft deletion is blocked by the classifier (cfg inbox item filed).
- After any edit to `drafts/aiw343-study/questionnaire-part1.md` or `consent-and-info.md`, rebuild the survey: `python3 scripts/aiw343_build_survey.py --p2-url 'https://survey.alpine-institute.eu/index.php/343102?lang=en'`. Tests: `pytest scripts/test_aiw343_build_survey.py` (25).

## 7. Decisions for MG raised S362 evening (autonomous run after the 22:15 relay)
- **S362-3 JAIC facts behind Cloudflare (you, in a browser, 2 min):** open worldscientific.com/worldscinet/jaic → submission guidelines. We need: (a) single- or double-blind (anonymise or not), (b) word limit per article type, (c) reference style, (d) template download (Word `jaic-doc.zip` or LaTeX `jaic-2e.zip`). What is known: `docs/research/jaic-author-guidelines.md`.
- **S362-4 Worm abstract for JAIC:** approve the cut to 150 words in `drafts/submissions/2026-10-28-jaic-worm/abstract-150-proposal.md` (the M&M version had 245). Options: (a) approve, (b) edit.
- **S362-5 Detector paper title:** the current title is "An Operational Detector for Machine Consciousness: …". decisions S277 records "…a Self-Model That Takes Itself for Its Bearer". Options: (a) keep the current one, (b) the S277 one.
- **S362-6 Detector AI-use disclosure:** it is not your S342 wording, and it still says "in-silico checks reported in the companion", which is false (no check has run). Options: (a) replace with the S342 wording and drop the false clause, (b) only drop the false clause.
- **S362-7 Detector minor findings (14 left, list in `drafts/aiw130-jaic-s362-changelog.md`):** the independent re-check is DONE (`docs/research/aiw130-recheck-s362.md`): 0 blockers; its 4 majors + F5 + m10 are APPLIED; the in-silico content is now quotable as stated. 21 minors remain (incl. m2, a contradiction with §9.2 at l.46 and Box 1, plus section-reference density 5.24 against a 2.5 ceiling). Options: (a) apply all of them in a fix pass, (b) review them yourself.
- **S362-8 Michiel's code bugs (DFA 4 defects confirmed, LE ×10, driven-positive):** (a) offer on the call once the instrument exchange is agreed (brief's default), (b) mention briefly on the call, (c) send afterwards in writing with the repro.
- **S362-9 Michiel's chapter PDF:** download https://juser.fz-juelich.de/record/1046968 in your browser and drop it into Downloads, so we can check which of his figures rest on the broken DFA values.
