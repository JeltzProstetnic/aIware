# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-07-28T17:05Z — WSL
**Goal:** Update the fmt.matthiasgruber.com wiki (AIW-27) — written 2026-03 at FMT v1–3; social wants to link it as the "consciousness standard model candidate".
**Completed:**
- Investigated: wiki = `wiki/` in repo (127 md, MkDocs/Material, LIVE, frozen since 2026-03-20). Deploy owned by infrastructure project.
- Diagnosed: wiki ~70% framing-aligned already — NOT a from-scratch rewrite. Real defect = criticality-as-requirement (registry #3) + registry #2/#4/#5/#6 + 15mo missing currency + stale links.
- PART 1 (10 load-bearing files) corrected + committed (`0b8c4240`): free-compute reframe + "leading candidate" SMoC framing + registry #6 on engineering-spec + glossary Free-Compute entry.
- Authored lean long-tail workflow (19 fix→verify batches + currency draft).
- AIW-27 rescoped ([>]); handoff `docs/pending-wiki-refresh.md`; inbox notes (infrastructure redeploy, social linkable, cfg workflow-gotcha).
**Key Decisions:**
- **Wiki content = aIware's; deployment (mkdocs.yml/DNS/build) = infrastructure project.** This session edits only `wiki/*.md`.
- **Scope = targeted correction + currency pass, NOT a from-scratch rewrite** — because inspection showed the wiki is ~70% aligned with current FMT framing (four-model-theory.md already has "floor not ceiling", "kinds", constitution-not-transfer). A full rewrite would discard sound structure + AIW-27 post-production.
- **Public framing = FMT as the "leading candidate for a standard model of consciousness"** (pre-paradigm, invitation-not-verdict) — not "assert as THE standard model" (overclaim risk with academics) and not "drop the SMoC brand" (loses social's hook). MG-chosen.
- **Canonical correction: criticality → free compute.** Requirement = Class-4 capability actually deployed for open-ended self-modeling; criticality (σ≈1/λ≈0) = the measured dynamical signature, not the requirement (paper §3.7.3/§8.9; registry #3).
- **Workflow burst rate-limit**: ~14–20 concurrent Workflow agents trips a transient server-side limit that fails the whole batch fast; throttle into waves on retry.
**Pending at shutdown:** PART 2 workflow **rate-limited twice (server-side burst limit, 0 files edited, wiki/ clean)** — retry throttled into waves when limits clear.
**Recovery/Next session:**
- Resume PART 2 from `docs/pending-wiki-refresh.md` (has the workflow scriptPath, retry command, canonical language, known-broken-links list, and currency topics). Retry the workflow when server rate limits clear — throttle into 2–3 waves. Do NOT redo the 10 committed files. Wiki source = `wiki/`; never touch deployment (infra project).

### 2026-07-28T15:55Z — WSL (home PC)
**Goal:** S275 continuation after first (voided) shutdown — process 4 Bartl-queue link-mails MG sent to bartl@matthiasgruber.com; flag crucible relevance; ingest + queue.
**Completed:**
- Read the 4 Bartl-queue mails (they were on the Bartl label, not the general inbox).
- Crucible-relevance answered: only #1 (Kanai ICCR) is crucible-adjacent — already DONE (S274, tonight's JAIC anchor). #2 = cosmology (SB-HC4A), #3/#4 = RIM.
- Read #3 (IQ↔happiness) + #4 (Edwards & DeYoung "More Than General Intelligence") → RIM material. #2 (Cosmic Compiler) = RG-403, no local PDF; classified cosmology from title.
- Ingested → `docs/bartl-intake-2026-07-28.md`; trashed all 4 Bartl mails (8 msg copies, reversible 30d).
- Created AIW-132 (RIM sift/cite, P1) + AIW-133 (cosmology Cosmic-Compiler↔SB-HC4A, P1, blocked on RG PDF) — MG-set P1.
**Key Decisions:**
- Bartl mails are read-tasks (link + instruction). Of the 4: #1 Kanai already done (JAIC anchor); #2 cosmology (needs RG PDF); #3/#4 RIM (#4 = strong anti-monolithic-g citation, verify DOI). MG set both new items P1.
- Earlier this session (pre-void): NoC single-blind correction, NoC/JAIC/JCS three-paper reframe, Wolfram+Metzinger name-drop advisory — all committed (cc26f9cc) + pushed. See `docs/decisions.md` S275.
**Pending at shutdown:** 23:00 gate (AIW-130 Fable run). cfg-agent-fleet repo still dirty (inbox social task + dashboard) — a cfg session must commit+push.
**Recovery/Next session:**
- Intake detail: `docs/bartl-intake-2026-07-28.md`. AIW-132 needs the Edwards & DeYoung citation verified before use. AIW-133 blocked until MG pulls the RG "Cosmic Compiler" PDF.
- AIW-130 (23:00) spec + all S275 reframes: `docs/pending-fmt-two-slice-drafts.md`.

### 2026-07-28T14:16Z — WSL (home PC)
**Goal:** Startup + hold for the 23:00 time-gate on AIW-130 (FMT two-slice Fable drafting). Planned work is NOT yet due (started 14:16, gate is 23:00). Do productive interim work per MG.
**Completed:**
- Startup protocol: git-sync (global + private remote, both up to date), additionalContext surfaced
- Read handoff `docs/pending-fmt-two-slice-drafts.md` — confirmed TIME-GATED to 23:00 today, do NOT launch Fable workflow before then
- Interim task (a) Safron ingest — ALREADY DONE by S259 (Safron2020/2022a/2022b in corpus, INDEX.md addendum). Inbox item stale.
- Interim task (b) NoC SI CFP fetched + verified → `docs/noc-si-cfp-2026.md` (deadline Dec 31 2026, guest editors Pinto/Doerig/Dołęga, Research Article ≤9k, APC $3,625)
- FOUND CONFLICT: NoC is SINGLE-blind (verified OUP author guidelines) — AIW-130 handoff + AIW-103 said "double-blind-friendly" (FALSE); AIW-106 said single-blind (CORRECT).
- MG approved reconciliation → NoC corrected to single-blind everywhere.
- MG framing corrections (2026-07-28) baked into handoff + AIW-103:
- Wolfram/Metzinger **name-drop advisory** persisted → `.claude/knowledge/neuroscience-communication.md` (two-tier: CREDIT in FMT base paper + books, OMIT in external slices/outreach/blogs). Carried into handoff + social task.
- Filed social cross-project inbox task: **3 FMT blog posts** (one simple point per slice — NoC/JAIC/JCS).
**Key Decisions:**
- AIW-130 Fable two-slice drafting is time-gated to 23:00 local 2026-07-28 (MG instruction S274). Session started 14:16 → not due. Must not launch the Workflow before 23:00.
**Pending at shutdown:** 23:00 gate (AIW-130, 2 slices tonight; JCS deferred). aIware edits committed at shutdown. cfg-agent-fleet inbox + dashboard-cache edits UNCOMMITTED (cross-project boundary — a cfg session must commit+push, else the social blog task won't reach other machines).
**Recovery/Next session:**
- The scheduled work spec is in `docs/pending-fmt-two-slice-drafts.md` (Tracked-by AIW-130). Only run it if local time ≥ 23:00 on 2026-07-28 (or later date).
- If resuming interim work: cross-project inbox has aIware items (Safron papers ingest, Bildstein working group, Birch commentary, strategy-doc refresh, crucible data-integrity loop-close AIW-124/§8.9).

