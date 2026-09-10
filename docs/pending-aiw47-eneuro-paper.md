<!-- Action: reference -->
<!-- Tracked-by: AIW-47 (eNeuro short report), AIW-75 (FMT v11 ketamine fold-in) -->
# Next session: AIW-47 is SUBMISSION-GRADE — remaining = MG logistics, gated outreach send, FMT v11

> ## 🛑 Session 229 (2026-06-18) — eNeuro STANDALONE ABANDONED (MG decision)
> - **Correction email SENT** by MG Jun 17 16:52 (thread `19ed60eaf7da503d`; confirmed in Gmail Sent + `correspondence/wittmann-werner.md` Msg 25). Bonn/Wittmann no longer hold the overclaimed p≈0.018 — this supersedes every "unsent draft" note below.
> - **Ettinger replied Jun 18** with a data-use/consent objection (didn't realise the data would feed a standalone publication; would have wanted to be consulted first). MG replied same day, de-escalating (publication not a priority; manuscript a by-product; eNeuro was contemplated only for RIM, which cites their *published* results).
> - **MG DECISION (Jun 18): drop the standalone eNeuro paper + deprioritize Bonn.** Rationale (see `docs/decisions.md`): the corrected result is NULL → near-zero door-opening value for RIM, let alone FMT (MG's only real interest); Bonn uncooperative (data-use friction + no reply to the design question) and unlikely to hold further useful data; not worth the ~$1,945 APC or the relationship cost. Do NOT chase co-authorship — reopen ONLY if Bonn proactively offers within-subject / free-d′ data.
> - **AIW-75 (FMT v11 ketamine fold-in)** left to MG — folding a NULL/trend into FMT as "preliminary evidence" is weak; decide separately whether to include at all.
>
> --- everything below predates the Jun-18 decision; kept for history ---
>
> **⏱ Session 225 update (2026-06-17):**
> - **Outreach correction email is STILL AN UNSENT DRAFT** (Gmail id `19ebd4d9cedcb80e`) — verified against Sent: only Msg 24 (the OLD significant p≈0.018, Jun 11) + a Jun-16 courtesy reply ever went out. **Bonn/Wittmann still hold the overclaimed p≈0.018.** MG has shortened the draft from the Opus original (dropped co-author solicitation + benchmark framing).
> - **Before sending: refresh the attached PDF** — the draft carries `Gruber_eNeuro_Entwurf.pdf` (predates the Session 224 round-2 fixes); swap to current `drafts/aiw47-eneuro/aiw47-eneuro-opinion-DRAFT.pdf`. Draft is user state — do not edit/send without MG.
> - **Wittmann replied Jun 16** (collegial; did NOT engage the ketamine content; away until mid-July) → no new input for the eNeuro manuscript. **Lehmann/Ettinger silent** — within-subject design question + the between-subjects PS unanswered; not a blocker (between-subjects confirmed from OSF).
> - **eNeuro manuscript itself needs NO change** from the new psychologist info (their only new input was RIM-side, via Schmiedek). The ~06-16 send-gate has elapsed.

> ## ⭐ AUTHORITATIVE STATE — end of Session 224 (2026-06-12)
>
> **The paper is done.** `paper/aiw47/aiw47-eneuro-opinion.md` carries the STANDARD response-conditional
> numbers throughout, the certified hierarchical Bayesian HMeta-d (95% HDI [−0.86,+0.14]), and every
> round-2 Fable review fix. PDF rebuilt clean (`tmp/build-aiw47/`, 0 overflow, 9 pp), draft refreshed
> (`drafts/aiw47-eneuro/aiw47-eneuro-opinion-DRAFT.pdf`). Committed + pushed to private (01e2ee7, 2330b77).
> Do NOT re-do the rewrite. Numbers are primary-source-verified against the authors' OWN OSF scripts.
>
> ### What Session 224 closed (don't repeat)
> - Standard-method rewrite (evidence/methods/Fig 2 caption) + hierarchical Bayesian fold-in.
> - Round-2 Fable review → 3 High items all RESOLVED via the authors' OSF scripts: their sig meta-d′ =
>   t-test on Bayesian per-subject estimates + ANCOVA w/ Staircase_SD covariate, NO interaction tested;
>   Lehmann 2022 BBR citation confirmed correct+complete. (Record: `docs/aiw47-fable-review.md` Round 2,
>   `docs/aiw47-hmetad-reanalysis.md`.)
> - MG checklist: GNW demoted to near-neighbour (clean scalar foil = criticality/complexity); figure files
>   renamed so file#=label# (Fig1=2×2 schematic, Fig2=ketamine); code repo staged.
> - **Code repo:** `JeltzProstetnic/metad-ketamine-reanalysis` (PRIVATE, double-blind-scrubbed, tests green).
> - **Outreach email REFRAMED** (standard-method correction) → Gmail DRAFT created (id `r-6929866618130868089`),
>   PDF attached, from matthias@, standalone. Tracked: `drafts/aiw47-eneuro/outreach-email-DRAFT.md`.
>
> ### REMAINING — in order
> 1. **Outreach send is GATED:** do NOT send until Lehmann replies to the design question OR the ~2026-06-16
>    timeout (decisions.md "AIW-47 Authorship & Venue"). The Gmail draft is ready; MG reviews/edits/sends.
>    After send → update `correspondence/wittmann-werner.md` (Msg 25) + `contacts.md` (#33/#34) per the
>    outreach workflow. NOTE: Msg 24 (sent 06-11) told them the OLD significant numbers; this draft corrects
>    that to the trend — that correction is the email's first substantive beat.
> 2. **MG submission logistics (when ready to submit eNeuro):** separate title page (author/ORCID + the real
>    repo URL); generate an ANONYMIZED code mirror for double-blind review (anonymous.4open.science / OSF
>    view-only) — the repo is PRIVATE, flip it PUBLIC at acceptance; pay ~$1,945 APC. AI-use sentence already
>    in Acknowledgments. (M-4 residual: an Opinion carrying original analysis MAY be queried by a desk editor —
>    defensible; body ~3k words < 4k cap.)
> 3. **TASK 2 — FMT v11 (AIW-75):** fold the corrected standard-method ketamine finding into the full FMT
>    paper as ONE preliminary-evidence point (honest framing identical to the eNeuro paper: direction-consistent
>    trend, NOT reproduced significance). v10 already on Zenodo (10.5281/zenodo.20631497). Update .md AND .tex.
>
> ### Separate carry-forward (NOT part of AIW-47) — promote to backlog when picked up:
> - **Bach prior-art citations** for FMT + RIM (convergence-and-differentiation framing) — in the cross-project inbox (social, 2026-06-12); **propose P2** (priority-protective, not urgent; social owns the Bach relationship). Not yet in `backlog.md`.
> - **Temporal-smearing / "now"-fabrication argument → pop-sci book** next revision — in the cross-project inbox, already tagged **P1** by social. Not yet in `backlog.md`.
> - **Owed: dedicated Wittmann RIM/COGITO reply** — his Jun-3 COGITO message (Msg 23 in `correspondence/wittmann-werner.md`, "Reply pending" since S211). Separate from the AIW-47 group outreach (he's only cc'd there for the consciousness update); the RIM/COGITO thread still owes him a real reply.
