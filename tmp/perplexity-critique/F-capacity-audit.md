# F — Capacity Audit (May–Sep 2026)

**Author:** wave-1 agent F
**Date:** 2026-05-01
**Purpose:** Brutally realistic FMT-hours/week budget for the 5-month dissemination plan.

---

## 1. Empirical baseline — aIware sessions per month

Counted from `docs/conversation-log.md` session headers (191 logged sessions since project inception 2026-02-12). The conversation log's session IDs run 1–190 with several gaps; counts below are headed sessions per calendar month, deduplicated:

| Month | aIware sessions | social sessions | Notes |
|------:|----------------:|----------------:|-------|
| Feb 2026 (12-28) | ~103 | 15 | Project launch — burst, 7+ sessions/day at peak. Not a sustainable rate. |
| Mar 2026 | ~30 | 46 | Steady cadence. Twitter sprint dominant. |
| Apr 2026 | ~9 | 7 | **Activity collapsed.** Easter holidays + spring weather + the desk-rejection demoralization curve. |
| Apr 13–30 | 8 (out of 191 total → 184–191) | 4 | Trough. Three desk rejections, paper-strategy pivot. |

**Inferred typical session length:** 30–90 min (median ~45 min) for aIware writing/orchestration sessions; 15–30 min for social engagement sessions. Many April sessions were inbox/triage, not substantive FMT work.

**Trend signal:** aIware monthly sessions dropped 70% Feb→Apr. The April collapse is the most honest predictor of summer behavior — and April was *cool, indoor* weather. May–Sep will be worse.

---

## 2. Constraints feeding into the budget

- **Ivoclar full-time:** 5 days/week, ~40h. Reports to CTO Hirt. Workday FMT time = essentially zero (only inbox triage at lunch).
- **Family + Vorarlberg life:** wife and children, Alpine region, summer = mountains/lake/garden.
- **Steam Deck-in-bed mode:** primary FMT terminal after night-mode (17:00 wkdy / 20:00 wkend). Summer evenings stay light to ~21:30 in Vorarlberg → less bed time, more terrace time.
- **Public holidays / school holidays:**
  - May 14 Ascension (Thu, often bridged to Fri)
  - May 24–25 Pentecost / Whit Mon
  - Jun 4 Corpus Christi (Thu, bridged)
  - Aug 15 Assumption
  - Vorarlberg school summer break: ~Jul 11 – Sep 6 (9 weeks, family time)
- **Travel commitments:**
  - **Bochum** Jun 18–19 (travel Jun 17 + Jun 20 = 4 days off-grid)
  - **AICE-26 Brighton** Jul 2 (travel Jul 1–3 = 3 days off-grid)
- **Competing projects in active rotation:** cfg-agent-fleet (1,472 commits, P1 daily), social (P1, FMT-supportive but separate context), ivoclar (P2 corp), muse, infrastructure, mirror-box, and the long P2–P5 tail (25 active projects in registry). Cross-project inbox has ~70 pending items (27 >7 days, 26 >14 days) — every aIware session pays an inbox-triage tax.
- **Documented user preference:** "Summer is coming, this means good weather periods will significantly hold us up." Take literally.

---

## 3. Monthly hours budget (Matthias-hours, FMT-only)

"Matthias-hours" = high-cognitive-load time where Matthias is at the keyboard reviewing/writing/deciding. Subagents extend this but every output needs review.

| Month | Realistic FMT h/wk | Total FMT h | Major events | Notes |
|------:|-------------------:|------------:|--------------|-------|
| **May 2026** | **5–7 h/wk** | ~24 h | Bochum reg deadline May 30; SAGE deadline May 1 (today) | Pentecost long weekend lost. Two bridge weekends. Best of the five months. |
| **Jun 2026** | **3–5 h/wk** | ~16 h | BBS commentary deadline Jun 12 (4 days lost to Bochum + travel) | BBS sprint gates everything. After Jun 12 → recovery + Bochum follow-up. |
| **Jul 2026** | **2–3 h/wk** | ~10 h | AICE-26 Jul 2 (3 days off-grid); school break starts Jul 11 | First half = AICE, second half = vacation mode. Worst single month. |
| **Aug 2026** | **1–3 h/wk** | ~8 h | School break full month; Wendland re-contact window opens late Aug | Family vacation block. Maybe 1 hard week mid-month. |
| **Sep 2026** | **4–6 h/wk** | ~20 h | School break ends Sep 6; weather shifts | Back-to-routine. Ramp window for Q4 push. |

**Five-month total: ~78 Matthias-hours of FMT work.** That is *less than two full work-weeks* spread across five months.

### Activity breakdown (% of available FMT hours)

| Activity | Matthias-h share | Subagent leverage | Notes |
|----------|-----------------:|-------------------|-------|
| Writing (paper revisions, BBS, Nautilus) | ~40% | High (drafts) — but every paragraph needs author review | The §3.4 rewrite alone = 4–6 Matthias-h |
| Outreach correspondence | ~20% | Medium (drafts) — sending requires Matthias send | Each substantive reply = 30–60 min |
| Reading (citations, peer papers) | ~10% | High (subagent summaries) | Subagents can pre-digest; final synthesis = Matthias |
| Planning / strategy / triage | ~15% | Low — judgment work | Inbox + backlog grooming |
| Book promo / marketing | ~10% | High | Most can be delegated end-to-end if user pre-approves templates |
| Conference logistics | ~5% | Low | Registration, travel, slide prep |

---

## 4. Matthias-hours vs. subagent-hours

**Subagents multiply throughput on parallelizable, draft-able work:** literature scans, paper-section first drafts, reply boilerplate, code refactors, test-suite generation. They do **not** reduce review load — every output needs Matthias's eyes before it ships.

**Realistic multiplier:** 1 Matthias-hour of orchestration → 3–5 subagent-hours of parallel work + 1–2 Matthias-hours of review. Net: a 5h Matthias-week can produce maybe 15–20h of *work product* if well-orchestrated, but only ~3h of that is "shipped" (review-cleared) per session.

**Anti-pattern to avoid:** queueing more drafts than Matthias has review capacity for. Every unreviewed draft is technical debt — and there are already ~17 stale `pending-*.md` files in `docs/` (see retrospective-2026-04-24).

---

## 5. Hard ceilings — concurrent FMT initiatives

Given ~78 Matthias-hours over May–Sep:

- **Maximum 2 active "primary" FMT initiatives at any time.** Examples of primaries: AIW-49 BBS commentary, AIW-46 JCS submission, AIW-51 paper v5 deep revision, AIW-48 McFarnell registered report.
- **Maximum 1 active outreach campaign at a time.** Wave-2 researcher outreach (AIW-05) cannot run concurrently with BBS sprint.
- **Book promo runs as background only** until September. Subagents handle, Matthias approves in batches.
- **At most 1 conference per month with attendance.** May=none, Jun=Bochum, Jul=AICE, Aug=none, Sep=none.
- **No new salami-slice paper (AIW-47) before September.** The §3.4 rewrite must land first or it competes for the same writing-h.

**Triage rule:** when more than 2 primaries are "active" in the backlog, the youngest one demotes to P2/Waiting until one of the active two ships or is parked.

---

## 6. Concrete recommendation when capacity is exceeded

**Apply the "BBS-first, single-track May–June" rule:**

1. **May:** finish §3.4 rewrite + BBS commentary draft. Park everything else (JCS, McFarnell, Nautilus, Wave-2 outreach).
2. **Jun 1–12:** finalize and submit BBS commentary. Nothing else lands.
3. **Jun 13–30:** Bochum prep + post-conf follow-up. Optional JCS work if BBS came in clean.
4. **Jul:** AICE-26 + recovery. No new submissions.
5. **Aug:** read-only month. Reading queue + Wendland follow-up email (1 outbound).
6. **Sep:** McFarnell registered-report co-design + JCS submission.

If a new opportunity arrives mid-cycle (e.g., a researcher invites collaboration, a journal CFP appears with a tight deadline), apply the rule explicitly: **you cannot accept it without dropping one of the two current primaries.** Force the trade-off into the backlog before saying yes.

---

## 7. What this means for any plan derived from Perplexity's package

Any plan that assumes >7 FMT-hours/week sustained May–Sep is fiction. Any plan that schedules >2 paper revisions + outreach + book promo concurrently is fiction. The realistic dissemination plan must:

- Single-thread May (BBS) and Jun (Bochum + BBS submit).
- Treat July–August as a **maintenance-only** window (replies to incoming, no outbound campaigns).
- Hold all "nice to have" items (Nautilus, salami-slice, Bielefeld, Wave-2 outreach) for September or Q4.
- Build a Q4 ramp plan, not a Q3 ramp plan.

The user's own correction ("good weather periods will significantly hold us up") plus the empirical April collapse are the strongest signals. Plan around them, don't fight them.
