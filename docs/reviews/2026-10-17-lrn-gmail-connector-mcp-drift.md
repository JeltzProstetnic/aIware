<!-- Action: reference -->
<!-- lrn analysis S334 2026-10-17 (steamdeck2): Gmail connector bypasses point-of-action hook; google-workspace MCP drift. MG approved A + B + communication-policy line fix. Implementation routed to cfg-agent-fleet inbox. -->

**Verdict: both failures are real mechanism gaps, and neither is an agent that "should have followed the rule better". The fleet already has the right hook for Failure 1, but it only knows the tool names of the google-workspace MCP. The claude.ai Gmail connector tools slip past it unmapped. For Failure 2, no check anywhere compares the MCP servers a machine file declares with the ones actually configured.**

I edited nothing and ran no git. I measured these on this machine:
- `~/.cc-mirror/mclaude/config/.mcp.json` lists serena, playwright, memory and diagram. User-scope `mcpServers` in both `.claude.json` files is empty, and `~/.workspace-mcp` does not exist.
- `~/cfg-agent-fleet/global/hooks/point-of-action-knowledge.sh` exists and is registered with matcher `mcp__.*|WebSearch|WebFetch` through safe-run.
- `gmail-search-guard.sh` is registered with the exact matcher `mcp__google-workspace__search_gmail_messages`.

---

## Failure 1: Gmail draft created without the Gmail knowledge

**Root cause.** The fleet already handles this with a hook instead of prose. `point-of-action-knowledge.sh` injects a `gmail-compose` payload on the first compose call of a session. That payload covers the attachment staging route, draft dedup and standalone-only drafts. But its tool map has only two keys: `mcp__google-workspace__draft_gmail_message` and `send_gmail_message`. Its settings.json matcher (`mcp__.*`) already lets connector calls through to the hook. The hook's own fast-exit then drops them, because `mcp__claude_ai_Gmail__create_draft` and `update_draft` are not in the map. So the agent got nothing at the point of action. The only remaining trigger was the vague CLAUDE.md table row ("email"), which loses to the drafting task itself (Pattern 3).

**Related gaps:**
- **Wrong payload for the connector anyway.** The current text tells the agent to stage files into `~/.workspace-mcp/attachments/`, which is impossible on a connector-only machine.
- **The bigger connector hazard is missing.** `gmail-management.md` l.41 records that the connector silently rewrites every URL in a draft into a `google.com/url?q=` redirect (measured 2026-09-23), and the payload never mentions it.
- **This was already known.** `ivbook.md` l.107 recorded on 2026-08-11 that machines without google-workspace use the connector, whose tool names differ from the fleet docs. That finding was written into a machine file and never turned into a mechanism.
- **Same blind spot in the search guard.** `gmail-search-guard.sh` does not cover `mcp__claude_ai_Gmail__search_threads`, so the `is:unread` block can be bypassed through the connector.

**Classification:**
- Pattern 3: the pre-step lost to the drafting itself.
- Pattern 5(b)/(c): loading and enforcement already exist, but the enforcement's scope (its tool map) was incomplete. The fix belongs there, not in the prose.
- Pattern 11: every test in `test-point-of-action-knowledge.sh` feeds only google-workspace tool names, so they are green while the live connector path never fires.

**Proposal (hook behaviour spec).** Extend `point-of-action-knowledge.sh`:
1. **Map 1** (tool → group): add `mcp__claude_ai_Gmail__{create_draft,update_draft,send_message,reply,forward}`, all mapped to a new group `gmail-connector`.
2. **Map 2** (group → payload): add a `gmail-connector` entry. One part of it is computed at hook time: is `google-workspace` present in `$CLAUDE_CONFIG_DIR/.mcp.json` (or user-scope `mcpServers`)? The payload text:
   - (a) "This connector rewrites every URL in the body into a google.com redirect, silently."
   - (b) "It takes no file-path attachments."
   - (c) If google-workspace is present: "Use `mcp__google-workspace__draft_gmail_message` instead. Stage attachments in `~/.workspace-mcp/attachments/`."
   - (c) If absent: "google-workspace MCP is NOT configured on this machine. Path attachments and byte-exact URLs are unavailable. Tell MG that once, and do not suggest manual attach as if it were normal."
   - (d) Dedup, as in the existing payload.
   - (e) "Draft only after MG has signalled ready to draft." This mirrors the pending [rule] already in the cfg inbox.
3. **New mode: deny once instead of inform.** Only for `gmail-connector`, add `POAK_MODE[gmail-connector]=deny-once`. On the first call, emit `permissionDecision:"deny"` with the payload as the reason and set the marker; the agent's retry then passes. This matters because inform-only lets the first draft run with corrupted URLs before the agent ever reads the warning. Leave the existing `gmail-compose` group inform-only.
4. **Search guard.** Add `|mcp__claude_ai_Gmail__search_threads` to the gmail-search-guard matcher and make its substring test match `search_threads`.

**Placement:**
- `~/cfg-agent-fleet/global/hooks/point-of-action-knowledge.sh`
- the gmail-search-guard matcher in the settings template, and `gmail-search-guard.sh`
- tests in `~/cfg-agent-fleet/setup/tests/test-point-of-action-knowledge.sh`

**Token cost.** About 250 tokens once per session, only in sessions that compose mail through the connector, plus one extra tool round-trip from the deny. Every other tool call costs zero. No CLAUDE.md growth.

**Tests (write these first and watch them fail):**
1. A connector `create_draft` payload produces a deny on the first call and passes on the second, keyed by session.
2. A fixture `.mcp.json` without google-workspace makes the payload contain "NOT configured"; one with google-workspace makes it name `draft_gmail_message`.
3. Pattern 11 guard: at least one test feeds a PreToolUse payload captured from a real connector call (copied out of a session transcript), not a hand-written one.
4. The registered matcher regex matches `mcp__claude_ai_Gmail__create_draft`, extending the existing test 146.
5. gmail-search-guard blocks `is:unread` on `search_threads`.
6. Everything already in the suite stays green.

**Tier.** T2 (hooks plus the settings template), so `setup/tests/run.sh` and Podman E2E are required.

**Conflicts and fixes:**
- `communication-policy.md` l.59 says "All email drafts MUST use `draft_gmail_message`", which is false on connector-only machines. Change it to: "Drafts use `mcp__google-workspace__draft_gmail_message` where configured. Otherwise the claude.ai Gmail connector, whose limits the point-of-action hook injects."
- The pending [rule] "draft only after MG signal" (cfg inbox l.18) should go in together, so payload (e) matches the CLAUDE.md wording.
- The ivbook.md l.107 note about tool-name differences should move into the connector payload or into gmail-management.md as a "Connector tool names" subsection.

**Pattern check.** This is enforcement, not prose (fixes 5c). The trigger is action-specific: named tools (fixes 2). It arrives at the point of action (fixes 3 and 4). The test plan includes a real artifact (fixes 11). No CLAUDE.md rule is added, so 8 and 9 do not apply.

---

## Failure 2: google-workspace MCP missing on Deck 2, machine file says Active

**Root cause.** The Auth State row in `steamdeck-2.md` (l.44) is free prose, and nothing ever reads it against reality. The SessionStart checks I found that touch MCP:
- `04-auto-fix.sh` 4.8b only repairs a broken `~/.mcp.json` symlink.
- `07b` only lists MCP reference docs.
- `22-fleet-drift` covers git and installation drift, not MCP.

So nothing checks which servers are actually configured, and a stale machine file reads as truth. The same gap already showed on ivbook (no google-workspace, recorded only as prose).

**Classification:**
- Pattern 5(f): no rule was broken. The fault is an unverified environment claim.
- Pattern 1 flavour: the machine file was written once at onboarding (2026-05-10) and never re-checked against the live config.
- Pattern 11 risk for any fix that parses the prose table, so use a machine-readable declaration instead.

**Proposal (check spec).**
1. **Declaration.** Each machine file gets one machine-readable header line, for example `<!-- mcp-expected: serena, playwright, memory, diagram, google-workspace -->`. On Deck 2 it would declare google-workspace only if MG wants it here; that decision is also the fix in the inbox [work] item.
2. **New module `global/hooks/checks/28-mcp-declared-drift.sh`.** It runs at SessionStart and reads `mcp-expected` from the machine file that `~/CLAUDE.local.md` imports. It compares that list with the union of the `mcpServers` keys in `$CLAUDE_CONFIG_DIR/.mcp.json` and the user-scope `.claude.json`.
   - **Declared but not configured:** append to WARNINGS, e.g. `MCP_DRIFT: machine file declares google-workspace but it is not configured (.mcp.json has: serena, playwright, memory, diagram).` It cannot auto-fix, because deployment needs the vault passphrase.
   - **Configured but not declared:** a NOTE that the machine file is stale.
   - **Missing header:** a NOTE "machine file declares no mcp-expected". Keep it until every machine file carries one, so the gap stays visible instead of silent.
   - **Scope:** configured vs declared only, not connection health. A server that fails to connect (serena and diagram did this session) is a different check.
3. **Prose change.** Machine-file Auth State rows for MCP-backed services should point at the header instead of asserting "Active".
4. **Immediate fix.** Correct `steamdeck-2.md` l.44, which the inbox [work] item already covers.

**Placement:**
- the new check module
- `setup/tests/test-check-mcp-declared-drift.sh` (required, because every check needs a test)
- the header line in all 8 machine files plus `machines/_template.md`

**Token cost.** Zero tokens when the lists match. About 40 tokens per drifted server per session. Shell cost is one python or jq parse per SessionStart.

**Tests (write these first):**
1. A fixture machine file declaring google-workspace, with a fixture `.mcp.json` lacking it, emits `MCP_DRIFT`; matching lists emit nothing.
2. A missing header emits the NOTE.
3. User-scope `mcpServers` count toward "configured".
4. Real artifact: one test runs against the real `steamdeck-2.md` and a copy of this machine's real `.mcp.json`, and must report the drift that exists today.
5. Silence check: a malformed `.mcp.json` produces a degradation WARNING, not silence (same contract as 22).

**Tier.** The check module is T2 and needs E2E. The machine-file headers are T3 (template-push dry-run). Actually deploying google-workspace into `.mcp.json` is T1 and needs risk-gate clearance; that belongs to the existing [work] item.

**Conflicts and fixes:**
- Stay within the SessionStart `additionalContext` budget of about 10k chars (`hook-behavior.md` l.3): one line per drift, no file dumps.
- Add a "Machine file must carry `mcp-expected`" line to the onboarding steps in `machines/_template.md` and `foundation/project-setup.md`.

**Pattern check.** Automation, not prose (fixes 5f). Atomic: it detects at every session start rather than at a deferred audit (fixes 1). The declaration is machine-readable and the test plan uses real artifacts (fixes 11). No new behavioural rule.

---

## What the cfg inbox items should contain

The existing [work] item (cfg inbox l.20) already covers deploying the MCP and correcting the machine file, so do not duplicate it. File a new **[work]** item (P2, Tier 2) for the cfg session:

> aIware S334 lrn (2026-10-17, steamdeck2): (A) `point-of-action-knowledge.sh` misses `mcp__claude_ai_Gmail__*`. Add the 5 connector compose tools as group `gmail-connector` with deny-once mode and a payload covering URL rewriting, no path attachments, a live google-workspace presence check with the right route, dedup and draft-after-signal. Extend the gmail-search-guard matcher to `search_threads`. Tests: deny then pass, presence branch, captured real connector payload, matcher regex. Fix `communication-policy.md` l.59 and move the ivbook.md l.107 tool-name note into gmail-management.md. (B) New check `28-mcp-declared-drift.sh`, plus an `<!-- mcp-expected: … -->` header in all machine files and `_template.md`. Warn when a declared server is not configured, note when a configured one is undeclared or the header is missing. Tests include the real `steamdeck-2.md`. Run E2E in Podman. Coordinate with the pending [rule] "draft only after MG signal" (cfg inbox l.18).

This is enforcement code, not a CLAUDE.md rule, so it is [work] rather than [rule]. If MG wants a written rule to go with it, the only one worth having is the `communication-policy.md` l.59 rewording. That one needs Meta-Rules consent.

## Recommendation

Do both, A first:
- **A** is a small, data-driven extension of a hook that already exists and fails exactly on the path that bit this session. It costs nothing outside connector sessions.
- **The deny-once mode is what matters.** The connector's damage (rewritten URLs, impossible attachments) happens on the first call, so a note delivered after that call arrives too late. The live presence check means the hook tells the truth on Deck 2 and ivbook even before google-workspace is deployed there.
- **B** closes the deeper drift class: a prose "Active" in a machine file with nothing checking it, now seen on two machines.

Neither needs a new CLAUDE.md sentence. Adding one would repeat the "follow the rule better" non-fix (Pattern 5) that this failure has already disproved.
