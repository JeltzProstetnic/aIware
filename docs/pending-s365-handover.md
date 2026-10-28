<!-- Action: await-user-decision -->
<!-- Tracked-by: AIW-343, AIW-130, AIW-355, AIW-360, AIW-312, AIW-353, AIW-356 -->
# S364 → S365 handover (written 2026-10-28 ~12:55, WSL)

MG at shutdown: *"after this pass, cls, next session must continue, and check with cru learnings starting from chapter 6 if this is accurate"* and *"make sure survey can start"*.

## 1. FIRST: start the AIW-343 survey (MG order: "make sure survey can start")
Status: everything except the server import is done.
- Decisions: D-S364-7 (no ethics review, launch after pre-registration, employer clearance done, D2 clarified) and D-S364-8 (OSF pre-registration **h4n7f**, registered 2026-10-28 11:40 UTC, embargoed to 2027-01-31; project hk8q6). OSF login works via ORCID (vault `orcid`; OSF user 4npag).
- Builder: launch-ready (`scripts/aiw343_build_survey.py`). It closes 2026-12-15, carries the support line, no ethics placeholder, and a `src` URL parameter captured by a hidden question. E2E is green on LimeSurvey 7.5.1 (image `martialblog/limesurvey:7.5.1-261021-apache`). Files are in `drafts/aiw343-study/limesurvey/`: p1 = 343101, p2 = 343102, pilot = 343103, public = 343104.
- **Remaining steps:**
  1. Import 343101 and 343102 onto https://survey.alpine-institute.eu.
  2. Check the survey settings.
  3. Run a 3-response smoke test, then delete those responses.
  4. Activate 343101 and 343102.
  5. SendMessage `ivoclar-e0` (or file an ivoclar inbox item if no session is live): "AIW-343 Arm C live" with the URL `https://survey.alpine-institute.eu/index.php/343101?lang=en&src=ppx`.
- **Route:** the production LimeSurvey JSON-RPC is OFF. Measured: an SSH tunnel `ssh -L 127.0.0.1:<port>:172.17.0.1:8797 vps` to `index.php/admin/remotecontrol` returns an empty 200. ⚠ Port 18798 is taken by a local `ppx-ls` podman pod; use 18899. The admin UI sits behind the institute Keycloak. MG chose "I sign in now": open https://survey.alpine-institute.eu/admin in the Playwright window, and MG completes the Keycloak sign-in. Then log into LimeSurvey as `aiar-admin`; the password is in vault key `survey_admin_password`, field **`secret`**. To fill it: in one vault cycle, a small Python script reads `survey_admin_password["secret"]` and writes it to `/dev/shm/lsadmin.txt` (umask 077, prints the length only). Fill it through the `/dev/shm` bridge (`knowledge/dev-browser-ops.md`) and shred the file afterwards.
- Open points from the builder agent:
  - (a) The consent text still says "[in cooperation with UMIT TIROL, Hall in Tirol]", and its header comment mentions the UMIT template. There is no UMIT review now, so this is MG's call. **Decision S365-A.**
  - (b) Analysis must treat any src value other than "ppx" as unlabelled.
  - (c) `hosting-spec.md` says LS 6.17.18, and protocol §2 says Arm P has "no URL parameter". Both are stale.
  - (d) The public build (343104) needs its own expiry and closing date before it opens.

## 2. Detector (AIW-130, JAIC) — EM draft submission WSPC-JAIC-S-26-00288 is NOT approved
- MG is reading. MG's fixes this session: 'each is an invitation'; the two-dimensions sentence; Fig. 2 closure loop now two-way (with caption and alt text); '(stated, not derived)'; 'tested rather than asserted'. Register sweep items 1–25 were walked one by one with MG: 23 applied, item 2 kept (L26 "The result is a decision procedure…"), item 15 shortened. List: `drafts/aiw130-register-sweep-s364.md`.
- **Next 1 (MG order):** check §6 onwards against the crucible learnings for accuracy. Crucible sources: `~/crucible/docs/results/`, `~/crucible/docs/decisions.md`, `docs/research/aiw130-recheck-s363.md`, and the companion v6 `drafts/companion-computational-paper-draft.md` §4. List discrepancies for MG.
- **Next 2:** walk the 15 weaker sweep items one by one with MG (end of `drafts/aiw130-register-sweep-s364.md`).
- **Next 3:** rebuild (`python3 scripts/build_jaic.py detector`; the register gate now runs in the build and fails on hits) plus the diff PDF (`python3 scripts/build_jaic_diff.py detector 788d53dc --copy-to …CHANGES-vs-2026-10-19.pdf`). Then rebuild `latex-source.zip` and the EPS figures in `drafts/submissions/2026-10-28-jaic-detector/`.
- **Next 4:** in EM, log in as `matthiasgruber` (vault `jaic`; ORCID now linked). Open "Submissions Waiting for Author's Approval" → S-26-00288 → Edit Submission. Replace the manuscript PDF, the zip and fig1–3.eps, rebuild the approval PDF, download it, and open it for MG. Approve only on MG's OK. The ORCID prompt no longer appears.
- Already filled in EM for the detector: 5 reviewers (Kleiner, Wiese/Bonn, Mediano, Shanahan, Cleeremans; emails in `reviewers.txt`; Kleiner's and Cleeremans' are unconfirmed in plain HTML), the cover letter in the comments field, the questionnaire answers ("borrowed" = own preprints), no OA.

## 3. Worm (AIW-355) — SUBMITTED
WSPC-JAIC-S-26-00287, approved by MG on 2026-10-28. When the confirmation email gives the final manuscript number, record it in the backlog and in contacts #64. The source sentence "which is what makes the bookkeeping close" → "so the bookkeeping closes" is fixed for the revision.

## 4. Jülich call Fri 2026-10-30 10:00 (Michiel, FZJ Zoom 659 3774 0772)
Call notes: `docs/research/vdvlag-2025-reservoir-chapter-notes.md`. Order of moves: ask Q2 (null baselines) first; offer the DFA bugs only after the exchange is agreed (D-S363-6). Before quoting, check the figure readings against the PDF, especially Fig. 2's DFA colourbar going negative.

## 5. Carry-overs
- AIW-360: link ORCID on the Minds and Machines, Synthese, Phenomenology and the Cognitive Sciences, Review of Philosophy and Psychology, Cortex and Elsevier accounts. Cortex has no vault key; file one.
- AIW-312 (ResearchGate edit window plus companion v6 file swap) and AIW-353 (Emergenz cover-page PDF): unchanged.
- The CC update 2.1.280 → 2.1.312 is available; read the changelog before proposing it.
- `crucible/tmp/vdv-venv` is a venv inside crucible's `tmp/`; it belongs to crucible.

## Decisions for MG (ask with AskUserQuestion; re-verify each premise first)
- **S365-A — UMIT mention in the consent text** (`drafts/aiw343-study/consent-and-info.md`, "[in cooperation with UMIT TIROL, Hall in Tirol]"). There is no UMIT review (D-S364-7) and Netzer has not been asked. Options:
  - (a) delete the mention (recommended);
  - (b) keep it only if Netzer agrees to co-investigate;
  - (c) keep it as is.
  
  Must be settled before activation.
- **S365-B — the weaker 15 sweep items:** walk them now (recommended, MG chose "next session"), or skip.
