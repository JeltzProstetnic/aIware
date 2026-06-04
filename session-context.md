# Session Context

## Session Info
- **Last Updated**: 2026-06-04T14:00+0200
- **Machine**: Steam Deck 2
- **Working Directory**: /home/deck/aIware
- **Session Goal**: Read Wittmann Gmail → escalated into full RIM/COGITO publication strategy + Davos Tech Summit preparation

## Current State
- **Active Task**: End-of-session wrap, ready for `cls` when user returns from bouldering
- **Progress** (use `- [x]` checkbox for each completed item):
  - [x] aIware repo synced + reset to private/main (978374d → Session 210 shutdown)
  - [x] social repo synced from origin (hard reset, was 25 days stale; no separate private remote)
  - [x] ivoclar repo cloned to Deck 2 (first time)
  - [x] private remote added to aIware (was missing — HTTPS configured)
  - [x] Gmail auth via /mcp (claude.ai Gmail; google-workspace not deployed on Deck 2)
  - [x] Wittmann latest read: thread 19e8f57ea48f2918 "COGITO" — pivot from BIS to COGITO data offer via Schmiedek (DIPF) + Völkle (Freiburg, ctsem author)
  - [x] Wittmann reply (Message 24) drafted in German, sent by user with code-help offer addition
  - [x] Three lit-scan subagents returned: Schmiedek COGITO portfolio + Völkle ctsem + broader COGITO landscape with gap analysis
  - [x] COGITO Antragsskizze drafted (`drafts/cogito-antragsskizze.md`, German, 10 sections)
  - [x] RIM v2 preprint upload prepared (AIW-18 elevated P2→P1, pending file in place)
  - [x] R-vs-Python-vs-Both subagent returned: recommendation R-primary + Python satellite; AIW-69 added
  - [x] Davos Tech Summit Gmail read (thread 19e92f516e118677) — Sacha Ghiglione's CHF 6k partner package
  - [x] Ivoclar took the Special Partner Package (CHF 6k) — Lark negotiated, Hirt approved
  - [x] Davos target-list subagent returned — 24 Tier 1 + 15+ Tier 2 + 3 categories Tier 3
  - [x] Davos target list persisted to `drafts/davos-target-list.md` (with Variant C signing booth, direct-VIP-approach recalibration, Pascal Kaufmann re-encounter playbook)
  - [x] Pascal Kaufmann added to canonical contacts (cross-project/contacts.md #32) — book given LAAX May 28
  - [x] Wittmann + Schmiedek + Völkle added to canonical contacts (#29-31)
  - [x] Stefan Riegler added to Ivoclar Colleagues (#9, CPO, fresh Konzernleitung, Davos attendance pending Hirt-Matthias-Riegler chain)
  - [x] AIW-22 elevated P2→P1 (book reviews gating Amazon Ads + book-fame channel)
  - [x] AIW-70 (Davos prep) added with full sub-tasks
  - [x] AIW-71 (Wittmann Amazon.de review ask) added
  - [x] lrn findings 1, 2, 3, 5 inbox-routed to cfg-agent-fleet (sponge rule failures); 6 dropped per user
  - [x] RCA subagent on sync-before-lookup failure → inbox item with proposed global rule
  - [x] Persona switched Bartl→Elsa→Bartl after frustration over lookup-chain failure

## Key Decisions
- **Two-track RIM publication**: Track A = RIM v2 preprint on PhilSci-Archive (citable anchor before Schmiedek/Völkle see framework); Track B = empirical paper on COGITO with Schmiedek/Völkle/Wittmann co-authors. Targets: Psychology and Aging or MBR or Intelligence.
- **R-primary pipeline**: Stop the Python port as primary (Schmiedek already converted SAS→R; Völkle is ctsem author; psychometric ecosystem is R). Python kept as private sanity-check.
- **Davos signing strategy = Variant C** (Ivoclar partner space, no permissions needed — Matthias has full authority over Ivoclar's branded footprint). 100-150 book copies (24 Tier 1 + ~100 signing buffer). User affords, transports by car.
- **VIP approach = direct**. Matthias self-handles approaches (no playbook need for Lark-mediation). Pascal Kaufmann re-encounter at Davos is natural; ball is still in his court but conversation is fine.
- **McFarnell collab deprioritized as breakthrough vehicle** (he's a noname like Matthias; co-authorship doesn't supply credibility signal). Kept as parallel attempt. Schmiedek/Völkle/Wittmann is the credentialed path.
- **Breakthrough triple**: (1) RIM via COGITO with credentialed co-authors, (2) Book fame via Davos giveaway + Wittmann endorsement + Goodreads-first strategy, (3) Real-life conference contacts. Davos = AC implementation + book + AI-policy channel, NOT FMT-publication channel.
- **lrn outcomes**: Person Lookup Chain rule needs canonical-path naming (Finding 2 inboxed); sync-before-lookup clause needs adding (RCA inboxed). Both global CLAUDE.md edits routed via cfg-agent-fleet inbox.

## Recovery Instructions
- Next session: load AIW-18 handoff (`docs/pending-rim-v2-preprint-upload.md`) for RIM v2 preprint upload.
- All Davos prep in `drafts/davos-target-list.md` + `AIW-70` sub-tasks.
- Antragsskizze in `drafts/cogito-antragsskizze.md` — pending user review before Wittmann forwards to Schmiedek/Völkle (gated on Wittmann's reply to current draft + RIM v2 preprint being live).
- Wittmann thread state: Message 23 (his COGITO offer) → Message 24 (Matthias's R-acceptance + code-help offer) sent. Wait for his next reply before next move.
- Ivoclar repo now cloned on Deck 2 (62M).

## Carry-Over Items
- AIW-18 → next-session-task (already set in Next Session Task section below)
- AIW-70 sub-tasks (a-j) — Davos prep over next 3 weeks
- AIW-71 — Wittmann Amazon.de review ask paired with future Wittmann message
- Stefan Riegler full row needed in `~/ivoclar/knowledge/people.md` (cross-project inbox item)
- 4 prior inbox tasks (GAN/cortex, McFarnell gridworld pivot, BBS closed, Laukkonen/Bieberich pitches) — NOT actioned, deferred
- PROJECT SETUP INCOMPLETE: Roster + Reference missing — deferred
- Benjamin Zeller invitation to Schatzalp Gala — Matthias to discuss with Lark (Lark closer to Zeller family); Hirt may want to avoid political exposure of owner family
- Stefan Riegler invitation to Davos — Hirt asked Matthias to invite; Riegler's calendar may not allow

## Next Session Task
task: true
file: docs/pending-rim-v2-preprint-upload.md
backlog: AIW-18
description: Upload RIM v2 preprint to PhilSci-Archive (Track A of two-track RIM publication strategy). Pre-upload PDF rebuild + content checks, then archive submission, then update references + correspondence files. ~1.5-2h focused work. Strategic gating: RIM v2 must be citable BEFORE Schmiedek/Völkle see the framework via Wittmann brokerage, so the empirical Track B paper (COGITO collaboration) has a stable theory citation.
