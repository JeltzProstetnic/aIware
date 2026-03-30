<!-- session-context.md — updated by Claude, parsed by rotate-session.sh -->

**Last Updated:** 2026-03-30 20:45 CET
**Machine:** Steam Deck
**Working Directory:** /home/deck/aIware
**Session Goal:** Gmail check, git divergence fix, pending file promotion, lrn audit

## Completed Items

- [x] Gmail check — 2 unread ResearchGate (Marko Vitas follower, Moritz Breit RIM read), plus McFarnell Mar 29 reply (experiment co-design proposal) found via broader search
- [x] Git divergence fixed — local was 16 sessions behind private/main (sessions 162-177). Reset to private/main, restored 3 unique local files (build_rim_pdf.py, test_build_rim.py, dual-engine build_noc_pdf.py) from backup branch
- [x] Promoted Session 160 pending items to backlog: AIW-41 (McFarnell experiment co-design), AIW-42 (Alnagger citation in .md), AIW-43 (Marie Kaiser outreach). German figure paths confirmed done.
- [x] Updated McFarnell Waiting row with Mar 29 experiment proposal
- [x] `lrn` audit: Gmail `is:unread` failure (2nd occurrence after Session 165). Deployed PreToolUse hook `gmail-search-guard.sh` — blocks `is:unread` in Gmail searches fleet-wide. Committed to cfg-agent-fleet.
- [x] Drafted McFarnell reply (Gmail draft r8253899360831767773) — accepts experiment co-design, proposes registered report, floats lab collaborator recruitment
- [x] Created `docs/pending-mcfarnell-reply.md` (Action: present) for tomorrow's review-and-send

## Key Decisions

- Gmail guard hook deployed as fleet-wide PreToolUse (0 tokens) rather than project-level rule — prevents recurrence across all projects
- McFarnell experiment strategy: co-design paradigm, then jointly recruit lab-based collaborator (Peters, Luppi, or Mediano) for execution. Registered report as vehicle.

## Carry-Over Items

- `docs/pending-mcfarnell-reply.md` (present) — review and send McFarnell reply draft
- `docs/pending-german-book-review.md` (present) — German book review resume at ch5
- `docs/pending-word-editing-protocol.md` (reference) — tracked by cfg-agent-fleet, done
