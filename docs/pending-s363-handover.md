<!-- Action: reference -->
<!-- Tracked-by: AIW-357, AIW-356, AIW-351, AIW-355, AIW-130, AIW-353, AIW-312, AIW-343 -->
# S362 → S363 handover (written 2026-10-28 ~00:20, WSL)

## 1. NEXT TASKS (MG orders at shutdown), both while crucible runs
MG: *"next session can continue beginners guide on thinking work while we wait for cru"* and *"and prepare jaic submissions of course"*.

**1a. Prepare the JAIC submissions (AIW-130 Detector, AIW-355 Worm), promised to Suzuki, fleet calendar Mon 2026-11-02 09:00.** See §4 for the state of both. Concretely: get S362-3..7 answered; apply the detector minors fix pass; build both manuscripts in the JAIC template (Word `jaic-doc.zip` or LaTeX `jaic-2e.zip`, downloaded via MG's browser if Cloudflare blocks agents); write the cover letters (`drafts/aiw130-jaic-cover-letter.md` exists for the detector); prepare a kit folder per paper (`drafts/submissions/2026-10-28-jaic-*`); MG submits via editorialmanager.com/wspc-jaic (ORCID registration).

**1b. The Beginner's Guide to Thinking (AIW-357).** aIware owns the theory and research questions; the book moves to simbook once those are settled (MG S362).

**Where it stopped.** The audit of Perplexity's dossier is complete: `docs/research/aiw357-perplexity-dossier-audit.md`, with three detail reports beside it in `docs/research/aiw357-*.md`. Verdict: no thesis was contradicted by evidence. The dossier weakened them by inflating claims, by grading novelty as weakness, and by citing MG's books without engaging their arguments. Part of this our own brief induced. Its section "Revised brief for any next research pass" has six points.

**Next concrete action.** Write the **revised research brief v2** in `drafts/aiw357-thinking-guide-brief-v2.md`. The current brief and package are at `~/simbook/thinking-guide/perplexity-package/00-BRIEF.md`. v2 should:
- grade each thesis on two axes: literature (confirmed / contradicted / silent / not empirical) × argument (valid / premise contested / invalid);
- allow weakening only on contradiction;
- give each thesis a canonical sentence plus a "what I do not claim" line (drafts for theses 2 and 5 are in `docs/research/aiw357-logic-truth-misreadings.md`);
- split theses 3 and 8, which the old wording merged;
- fix the package glosses (monocausality: "almost all", not "every brain"; emergence is indirectly multi-causal);
- carry the 2026 truth definition (*No Outside* §6.2);
- supply full *No Outside* chapters 1, 2, 4, 6 and 8.

**New material to fold in from S362:**
- Perelman (`docs/research/aiw357-theses-4-6-7-9-suppression.md`). Role (a): great work outside institutional academia; accuracy guard: he was employed at Steklov, so the claim is "outside the incentive machinery". Role (b): the mushroom quote, as reported, for living in the now.
- MG's now-only rationale for indifference to success markers (`docs/sources/bartl-2026-10-27-super-hard-problem.md`, addenda).
- Then ask MG what to do with v2: rerun Perplexity, or have us draft entries.

## 2. AIW-356 discussion owed to MG (deferred by MG to "not today", S362)
Super-hard problem, the now, recurrence and Boltzmann brains as indiscernible from the worm on the disk, and Hawking's time reversal. Verbatim notes and the open checks (the Hawking retraction scope; Nobel cases to be named or dropped) are in `docs/sources/bartl-2026-10-27-super-hard-problem.md`.

## 3. Waiting on crucible: FMT mini-model (CRU-227; aIware plan AIW-351 successor)
- **Binding spec:** `docs/sources/mg-2026-10-27-fmt-substrate-spec.md`. It records MG's verbatim corrections and decisions: body ≈ a large fraction of cortex; activity AS models is the core; thalamus = I/O relay AND loop channel; peripheral ganglia plus a basal-ganglia selector; torch first; all four model criteria measured, none a gate; body-first test; vision ON.
- **Plan:** `docs/plans/fmt-mini-model-plan.md`. **Requirements:** `docs/research/fmt-mini-model-requirements.md`. **Stack:** `docs/research/fmt-mini-model-stack.md` (NEST 3.10 works via pip in `/tmp/claude-1000/fmtenv`). **RCA:** `docs/research/fmt-crucible-misread-rca.md`.
- **Crucible state (S362 end):** biosheet built (43.7k neurons, ~real time without plasticity); P1 pre-registration v2 after a Fable red-team (`~/crucible/docs/design/cru227-p1-prereg-2026-10-28.md`); vision being switched on with the red-team re-run. The FROZEN/BODY/REPLAY/MIN-RANK runs take ~8–10 GPU-hours. Readout is expected Thursday or Friday morning, red-teamed before any interpretation.
- **Jülich call: Fri 2026-10-30 10:00** (Michiel's FZJ Zoom, ID 659 3774 0772; fleet calendar). MG: "no more briefs; we need an experiment he can scale". The plan's M4 package (one-command run, NEST port plan, scale asks S1/S2) is what goes to the call. The one-page brief and the explainer exist but are superseded in purpose.
- **Michiel's code:** the DFA bugs are confirmed and the Lyapunov notes run-verified (`~/crucible/docs/cru226-vdvlag-code-verification.md`).

## 4. JAIC submissions — promised to Suzuki 2026-10-27, fleet calendar Mon 2026-11-02 09:00
- **Detector (AIW-130):** `drafts/aiw130-jaic-draft.md` is cleaned. The audit plus an independent re-check fixed 31 claims; the in-silico content is now quotable as stated. Changelog: `drafts/aiw130-jaic-s362-changelog.md`. 21 minor items are open (S362-7).
- **Worm (AIW-355):** package started in `drafts/submissions/2026-10-28-jaic-worm/`, with a 150-word abstract proposal (S362-4). Its format depends on S362-3.
- **JAIC guidelines** (partial; the publisher site is Cloudflare-gated): `docs/research/jaic-author-guidelines.md`.

## 5. Other carry-overs
- **ResearchGate edit window (AIW-312):** the S361 list, plus swapping the In-Silico Tests file (RG 416595850) for companion v6 (`tmp/zen-companion-v6/companion.pdf`, 10.5281/zenodo.23702509, published S362).
- **Emergenz re-deposit (AIW-353):** the cover-page PDF from simbook, uploaded under the existing filename `emergenz-de-2-pb.pdf` (D-S362-6).
- **AIW-343 survey:** Templer DAS is dropped (no paid permissions, D-S362-3). Choose: drop it, or replace it with a free death-anxiety measure.
- **Springer Transfer Desk:** complaint sent (D-S362-7). The notification pages need a Springer account to decline, so there is nothing further unless MG wants to log in.
- **cfg inbox items filed S362:** AIW-359 (lrn: the gmail-compose hook should match `update_draft`; one sentence for gmail-management) and the Bartl-folder rule (move handled mail to Bartl/ subfolders; `Bartl/Research` created).

## 6. Decisions for MG (ask with AskUserQuestion, re-verify each premise first)
- **S362-3 JAIC facts behind Cloudflare.** Premise: `docs/research/jaic-author-guidelines.md` §2–4 are UNVERIFIED. Needed: single- or double-blind, word limit, reference style, template. Options: (a) MG opens worldscientific.com/worldscinet/jaic → submission guidelines (recommended); (b) ask Suzuki; (c) submit and follow the EM instructions.
- **S362-4 Worm abstract.** Premise: `drafts/submissions/2026-10-28-jaic-worm/abstract-150-proposal.md` (150 words; the M&M version was 245). Options: (a) approve (recommended); (b) edit.
- **S362-5 Detector title.** Premise: decisions S277 records "…a Self-Model That Takes Itself for Its Bearer"; the draft carries "An Operational Detector for Machine Consciousness: …". Options: (a) keep the current title (recommended); (b) the S277 one.
- **S362-6 Detector AI-use disclosure.** Premise: it is not MG's S342 wording and still says the checks were "reported in the companion" (false; recheck `docs/research/aiw130-recheck-s362.md`). Options: (a) S342 wording without the false clause (recommended); (b) only drop the clause.
- **S362-7 Detector minors.** Premise: 21 open items in the changelog and the re-check, including m2 (§9.2 contradiction at l.46 and in Box 1) and section-reference density 5.24 against a 2.5 ceiling. Options: (a) a fix pass applying all (recommended); (b) MG reviews them.
- **S362-8 Michiel's code bugs.** Options: (a) offer once the instrument exchange is agreed (recommended); (b) mention briefly on the call; (c) send afterwards in writing with the repro.
- **S362-9 Michiel's chapter PDF.** The bot wall blocks the agents. Options: (a) MG downloads https://juser.fz-juelich.de/record/1046968 into Downloads (recommended); (b) skip.
- **AIW-343 DAS replacement.** Options: (a) drop the DAS (recommended); (b) find a freely licensed death-anxiety scale.
