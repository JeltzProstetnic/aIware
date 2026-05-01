# I — Cross-Project Coordination Map (May–Sep 2026)

**Author:** wave-2 agent I
**Date:** 2026-05-01
**Scope:** Weekly interlock between `aIware` (FMT authoring + academic submissions) and `social` (X engagement + public visibility), under the hard capacity ceiling from agent F (~78 Matthias-h total over 5 months) and the timing constraints from agents D/E.

---

## Section 1 — aIware ↔ social hand-offs

The coordination surface is small. Most days the two projects don't need to talk. The events below are the ones that DO require a hand-off, and each has a defined owner and trigger.

| Trigger event | Owner project | Hand-off action | Receiving project | Timing |
|---|---|---|---|---|
| BBS commentary submitted (target Jun 12) | aIware | Write a 2-3 line announcement payload + permanent link → push via inbox to social | social | Social posts within 24-48h, NOT same hour. Tweet says "Just submitted a commentary on Seth's BBS target article — argues that [one line]" with link to commentary preprint, not the book. |
| Bach DM channel state change (any reply, any silence >14 days) | social | Append to `engagement-log.md` AND inbox-flag to aIware if Bach proposes anything actionable (collaboration, intro, paper read). Bach DMs are NOT auto-promoted to aIware — only when a concrete ask appears. | aIware (only on actionable change) | Within the social session that observes the change. |
| Kanai (JAIC) — next move | **aIware** owns this. Social already executed the X warm-up (May 1 axis-mapping reply). | aIware drafts JAIC submission email referencing the May 1 X exchange. social does NOT initiate further public replies until aIware has sent. | social (only to flag if Kanai posts something new) | aIware should send within 2 weeks of May 1 (i.e., by May 15) or lose the warmth. |
| Substack post publishes | aIware (writing) | Drop the URL + 2 candidate quote-tweet snippets into inbox | social | social schedules X cross-post within 24h of publish; LinkedIn cross-post within 48h. |
| Podcast acceptance | social (most pitches originate here per F-budget) | inbox to aIware: which paper to send the host, requested format (preprint, book chapter, summary) | aIware | aIware prepares materials within 1 week of acceptance; social handles announcement post-recording, not pre. |
| German edition Wendland follow-up (Aug) | **aIware** initiates the email (academic register), social does the announcement IF a recording date is fixed | aIware | social | aIware sends Aug 10-15 window (post-vacation re-entry). |
| Cortex RR / JCS / new submission | aIware | inbox to social: "submitted X to Y on date Z, public-OK after acknowledgment received". social does NOT pre-announce. | social | After acknowledgment email (typically 3-7 days). |
| New researcher engages publicly on X | social | If they're already in `contacts.md`: handle in social. If they propose collaboration / paper read / podcast: inbox to aIware. | aIware on actionable | Same session social spots it. |
| Wittmann Mannheim (warm German contact) | aIware | German-language follow-up email; social may cross-post if a public artifact emerges | aIware | Late Aug, paired with Wendland. |

**Hand-off carrier:** `~/cfg-agent-fleet/cross-project/inbox.md` for tasks; `contacts.md` and `engagement-log.md` for state. No Slack-style chatter; no duplicated tracking.

---

## Section 2 — Weekly cadence template

The unit of planning is one week, not one day. A "session" below is a 30-90 min Claude Code interaction.

### May (cool, indoor, conference prep) — F-budget: 5-7 FMT-h/wk

```
Mon-Fri (Ivoclar):  no FMT during work hours.
                    Lunch: ≤5 min on phone — like/RT only, no drafting.
Mon evening:        social (30-45 min) — engagement scan, draft 1-2 tweets
Tue evening:        aIware (60-90 min) — primary writing block (BBS / §3.4)
Wed evening:        family/quiet — no FMT (recovery)
Thu evening:        aIware (60 min) — review subagent outputs, ship one item
Fri evening:        social (30 min) — schedule weekend posts, Gmail audit lite
Sat:                family + outdoor. 30 min max if anything urgent.
Sun afternoon/eve:  aIware orchestration window (60-90 min) —
                    launch overnight subagent waves: literature scans,
                    reply drafts, citation chases. Review Mon evening.
```

Gmail audit cadence in May: **weekly** (Fri evening or Sun) — agent D flagged 2-week staleness as outreach data-integrity risk.

### June (BBS sprint + Bochum) — F-budget: 3-5 FMT-h/wk

```
Jun 1-12:    SINGLE-TRACK. All evenings = BBS commentary finalization.
             social = autopilot (1 post/wk, no campaigns).
             No new researcher outreach. Inbox = aIware-only.
Jun 13-16:   Bochum prep (reading, slide tweaks, travel logistics).
             social: pre-conf engagement on Melloni/Chalmers/Seth IF
             they post; otherwise quiet.
Jun 17-20:   OFF-GRID. No sessions. Auto-replies on email.
Jun 21-30:   Recovery + 1-2 Bochum follow-up emails (aIware) +
             1 Bochum-recap tweet/thread (social).
```

Gmail audit: skip Jun 13-22 (Bochum). One catch-up audit Jun 23.

### July (AICE + school break onset) — F-budget: 2-3 FMT-h/wk

```
Jul 1-3:     OFF-GRID (Brighton).
Jul 4-10:    Recovery week. 1-2 sessions max. AICE follow-ups (aIware)
             + 1 conf-recap tweet (social).
Jul 11-31:   School break starts. **MAINTENANCE ONLY.**
             social: 1 post/wk.
             aIware: incoming-only (replies, no outbound).
             Sunday-eve subagent windows: keep running for reading
             queue digests; review when terrace time allows.
```

Gmail audit: every 2 weeks (acceptable lag during maintenance).

### August — F-budget: 1-3 FMT-h/wk

```
Full school holidays + family vacation block.
Default: zero FMT activity.
One designated "1 hard week" mid-month (best guess: Aug 17-23):
  - Wendland follow-up email (aIware)
  - Wittmann follow-up email (aIware)
  - 2-3 Substack-draft sessions IF energy permits
social: 1 post/2 weeks, German-edition focused.
```

Gmail audit: ONE audit at mid-month hard week. Otherwise dark.

### September — F-budget: 4-6 FMT-h/wk

```
Sep 1-6:     Still vacation tail. Light-touch only.
Sep 7+:      Routine resumes. Pattern reverts to May template.
             Q4 ramp begins: McFarnell co-design, JCS submission.
             social: re-energize cadence to 2-3 posts/wk.
             Gmail audit: weekly again.
```

---

## Section 3 — Coordination anti-patterns

What NOT to do. Each is a real risk given how the two projects can collide:

1. **Both projects drafting an X post about the same event.** If aIware is already preparing a BBS-submitted announcement, social doesn't independently draft one. Owner is whichever project's session triggered the event; the other project receives a payload, not a brief.
2. **Social promoting a paper before aIware confirms submission status.** Submitted ≠ acknowledged ≠ accepted. Public posts must reference the actual state ("submitted", "in review", "accepted") and aIware owns the truth.
3. **Two simultaneous outreach campaigns to the same target.** If aIware is mid-email-thread with Person X, social does NOT start cold-engaging X on Twitter. The coordination rule in `fmt-visibility-strategy.md` already covers this; the rule must be CHECKED, not assumed.
4. **Bach DM activity echoing publicly.** Anything in DMs stays in DMs. Even oblique references ("had a good chat with someone about MC0001") burn the channel. Bach exchanges live in `engagement-log.md` only — never in tweets, never in Substack posts.
5. **Promoting the book heavily while peer review is pending.** Per agent E, top-tier podcast hosts gate on peer-review status. Aggressive book pushes during BBS review (Jun) or any C&C/JCS review window (Jul-Aug) signal "self-publishing only" and lower acceptance rates.
6. **Re-pitching a researcher already pitched.** The contacts.md / engagement-log.md cross-check rule exists for this. Skipping it reproduces the Mar 3 data-integrity disaster (15+ unrecorded pitches).
7. **Both projects auto-promoting completed work to backlog without user priority review.** Per global CLAUDE.md: priorities are user-decided. New backlog items in either project must surface to user.
8. **Cross-project inbox items growing >14 days.** Both projects must drain their queue weekly during May; bi-weekly during Jun-Sep. >14d stale = the rule has failed.

---

## Section 4 — Ivoclar workload signal

Hard rule: **other projects do not read Ivoclar content.** What we CAN observe:

**Behavioral signals** (visible without reading Ivoclar files):
- Number of `~/ivoclar/` session-context.md timestamps in a rolling 7-day window
- `additionalContext` mentions of Ivoclar inbox tasks
- User explicitly mentions Ivoclar workload in aIware/social sessions
- `BARTL_MAIL:` injection volume (bartl@ alias = work-context overflow indicator)

**Heuristic rules:**

| Signal | aIware/social action |
|---|---|
| Ivoclar sessions ≥4/week (rolling 7d) | aIware drops to **maintenance only** that week (incoming replies, no outbound campaigns). social drops to 1 post/wk. |
| Ivoclar sessions ≥6/week | Both projects: pause all outreach. Inbox triage only. |
| User explicitly says "swamped at work" | Immediately set both projects to maintenance. Surface the plan back: "this week = no FMT outbound, OK?" |
| BARTL_MAIL volume >5 unread items | Maintenance, AND surface that the bartl queue is backing up. |
| User skips an aIware session for >5 consecutive days during May | Capacity contracting earlier than F-budget assumed — re-baseline. |
| User opens session at unusual late hour (>22:00 weeknight) | Apply night-mode harder: track over execute, no new initiatives proposed. |

The rule is asymmetric: when in doubt, **drop FMT effort, not work effort.** Ivoclar pays the rent.

---

## Section 5 — Summer reality budget

Per agent F's hour budget, restated as a "what's realistic" sentence per window:

- **May (24 FMT-h total):** §3.4 rewrite landed; BBS commentary draft to 80% complete; Substack set up + 1-2 posts; ~6 substantive engagement actions on X (replies/threads); Gmail audit current; ~10 outreach emails sent. **Best month of the five.**
- **Jun 1-12 (~10 FMT-h):** BBS commentary submitted. ONE thing. Everything else is autopilot.
- **Jun 13-19 (Bochum, 0 FMT-h):** off-grid. No coordination. Auto-reply on email.
- **Jun 20-30 (~6 FMT-h):** 2-3 Bochum follow-up emails; 1 conf-recap thread; Substack post 3 if energy left. JCS work begins ONLY if BBS came in clean.
- **Jul 1-7 (~3 FMT-h):** AICE-26 + recovery. 1-2 follow-up emails. 1 conf-recap thread.
- **Jul 8-31 (~7 FMT-h, 24 days):** maintenance. Incoming replies only. Maybe 1 Substack post. Wendland prep work (research, not yet sending).
- **Aug (~8 FMT-h, 31 days):** vacation block. ONE hard week mid-month: Wendland email, Wittmann email, 2-3 Substack drafts. Otherwise dark.
- **Sep 1-6 (~3 FMT-h):** vacation tail. Light-touch resumption.
- **Sep 7-30 (~17 FMT-h):** routine restored. McFarnell registered-report co-design. JCS submission. Q4 ramp.

**What this means for "Matthias + Claude" combined throughput:** the realistic shipped-work output is ~3 hours/Matthias-week of *review-cleared* artifacts (per F-budget multiplier analysis). Times 22 weeks of available calendar = ~66 hours of shipped output across May-Sep. That's enough for: 1 BBS commentary, 1 JCS submission, 1 McFarnell co-design start, 4-6 Substack posts, 2-3 podcast appearances, ~80 X engagement actions, and ~25 outreach emails. **Not enough for** the salami-slice paper, Nautilus essay, Bielefeld outreach, Wave-2 researcher campaign, or any second book project. Those are Q4.

---

## Top 10 coordination rules (the actual operating manual)

1. **One owner per event.** BBS submission, Kanai next move, Wendland follow-up — each has exactly one owning project. No co-ownership.
2. **Submitted ≠ public.** Social does not announce a paper until aIware confirms acknowledgment received.
3. **Bach DMs stay in DMs.** No public references, no Substack mentions, no oblique tweets. Channel = `engagement-log.md` only.
4. **Single-track June 1-12.** BBS commentary is the only outbound. Everything else parks.
5. **Off-grid means off-grid.** Jun 17-20 (Bochum), Jul 1-3 (AICE), Aug vacation block — no sessions, no inbox draining, auto-replies.
6. **Maintenance mode is the default for Jul 11 – Sep 6.** Outbound campaigns suspended. Incoming replies only.
7. **Gmail audit weekly in May, bi-weekly Jun-Sep.** Outreach data integrity is the foundation.
8. **Ivoclar workload trumps FMT.** Drop FMT first when Ivoclar pressure rises. Heuristic table in §4.
9. **Inbox is the carrier.** All cross-project hand-offs go through `~/cfg-agent-fleet/cross-project/inbox.md` + `contacts.md` + `engagement-log.md`. No ad-hoc messaging, no duplicated tracking.
10. **Q4, not Q3.** Anything that doesn't fit in the May-Sep budget is a Q4 plan, not a "we'll squeeze it in" plan. The F-budget is the budget.
