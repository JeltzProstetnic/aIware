<!-- Action: reference -->
<!-- Tracked-by: AIW-366 -->
# lrn S367 (2026-10-30) — person comms preferences were not captured

**Trigger.** MG, answering S367-E, verbatim: *"sponge mode for persons should have already (do now and lrn if it hasnt) ingested the information concerning kleiner and bickel concerning their preferred email language, writing mails must check with person data always, there could be addditional information like "always use gendering for this person" or "never mention xy to this person"."*

**Done the same turn.** Kleiner: contacts #39 now opens with `**Comms:** mail in German, du-form; never name the Erbprinz` (cfg 40c62844, pushed). Bickel: an Ivoclar contact; the ivoclar session wrote `Comms: German only — he reads no English, Swiss orthography` into `~/ivoclar/knowledge/people.md`.

**Root cause.** Nothing reads or writes how MG wants a person written to. Capture routes people only to `relationships.md`/`family.md` (global CLAUDE.md "Proactive information capture" and `reference/communication-policy.md`) and never names `contacts.md` or address preferences. aIware's outreach workflow step 1 reads status and prior exchanges, and step 4 writes status, date and pitch angle. So an instruction MG gave mid-draft ("German", "don't name the Erbprinz") was treated as an edit to one mail, not as a fact about the person. Rule analysis by subagent (Meta-Rules step 1), S367.

## Findings (cheapest tier first)

1. **Hook (cfg, Tier 2).** Extend `global/hooks/sent-recently.sh` (same tool_input parse and matcher as SENT_RECENTLY; add the send/reply tools) to inject `RECIPIENT_COMMS: <name>: <Comms segment>` or `<addr>: no Comms recorded`, plus "write any language, address-form or never-mention instruction MG gives for this person into that row's leading `**Comms:**` segment before you draft". Lookup by exact address in `contacts.md` and `relationships.md`, fallback surname (≥4 chars, umlauts folded) in the local part. Never blocks (exit 0). Never reads `~/ivoclar/` outside an ivoclar cwd; for `@ivoclar` addresses or Ivoclar-table rows emit only "Ivoclar recipient: ivoclar project" (filter by domain or row shape, not heading — researcher rows #65–78 sit after the Ivoclar table). Tests use the real row #39 and the real `tool_input.to` shape (Pattern 11). 0 tokens per session, ~30–60 per draft call. Ivoclar mail goes through Outlook, so the hook does not cover Bickel.
2. **contacts.md rules block (extend-existing).** "Start Notes with `**Comms:**` for how MG writes to the person (language, address form, gendering, never-mention), and record the address with it."
3. **aIware CLAUDE.md, Outreach email workflow (project-rule, extends existing steps).** Step 1: "…status, prior exchanges and its `Comms:` segment". Step 3 appended: "Write any instruction MG gives about the recipient (language, address form, topics to avoid) into the contact's `Comms:` segment before redrafting." ~30 tokens per aIware session.
4. **communication-policy.md People bullet + global CLAUDE.md capture parenthesis (extend-existing).** Policy: "People → `cross-project/contacts.md` (external) or `relationships.md`/`family.md` (personal circle), with how MG wants them addressed as the row's `**Comms:**` segment." CLAUDE.md: "(people → `contacts.md`/`relationships.md`/`family.md`, incl. how to address them …)". Also fixes the omission of the canonical `contacts.md` from the capture routing.
5. **ivoclar** — recorded Bickel already; its drafting step reading `Comms:` is ivoclar's to adopt.

Targets 1, 2 and 4 are cfg-owned → inbox `[rule]`/`[work]` to cfg after MG approves; target 3 is aIware's.

## Outcome (MG, S367 S367-F)

Approved 1, 2, 4 → filed to cfg inbox (`[work]` hook, `[rule]` contacts.md + communication-policy/CLAUDE.md text). Option 3 changed by MG: *"outreach knowledge should be read only on demand, in most sessions we do no outreach whatsoever"* → the whole outreach/email block moved from `CLAUDE.md` to `.claude/knowledge/outreach-email.md` (trigger row in Knowledge Loading), with the step 1 + step 3 `Comms:` additions there.

## lrn 2 (S367, MG: "lrn from the token mishap and if possible make sure it never gets pushed to a repo, or at least not to a public one")

**What happened.** The read-only fleet memory audit (subagent) printed the live `settings.json` env block, including `AFD_TOKEN`'s value, into its tool output (local transcript only). MG S367-Q: accepted, no rotation.

**Measured (no value printed):** no tracked file in aIware, cfg-agent-fleet, agent-fleet, crucible, life, p0rn, simbook, social, infrastructure or ivoclar holds the value; public mirrors (agent-fleet, aIware origin) have it in no commit. **cfg-agent-fleet (private) has it in history since 2026-03-06** — commits 0070f129, 93d2345f, bebb0abb, 442a16d9, file `docs/pending-lrn-fixes.md` (added, later removed). `secret-commit-guard.sh` (PreToolUse on Bash `git commit`, SHAPE + salted VALUE fingerprints; `CC_SECRET_FINGERPRINTS`/`CC_SECRET_SALT` set in the live env) fingerprints AFD_TOKEN and **blocks** a commit carrying it in a non-cfg scratch repo (exit 2, tested S367).

**Gaps.** (a) The guard binds to Claude's Bash `git commit` only — scripts (auto-sync, sync.sh), MG's manual commits and any non-Bash path are unscanned, and nothing re-checks at push time. (b) Nothing stops a session or subagent from printing the env block of `settings.json` (the file is a credential store that looks like config). (c) The March leak sits in private history.

FINDING: A credential can reach a remote through any commit path the Bash-bound guard does not see.
ROOT CAUSE: The only scan is bound to the PreToolUse event of Claude's Bash tool, not to the push.
FIX: A fleet-installed git pre-push hook runs the same SHAPE + VALUE scan over every commit being pushed and refuses the push on a hit (chained with the LFS pre-push hook).
TARGET: cfg — global hooks / setup (installed per repo or via core.hooksPath)
TIER: hook

FINDING: A subagent printed `settings.json`'s env block, secrets included, into its tool output.
ROOT CAUSE: `settings.json` carries live credentials in `env` but nothing marks or guards it as a secret store, so "read the settings" reads them.
FIX: `vault-read-guard.sh` blocks raw reads of `$CLAUDE_CONFIG_DIR/settings.json` (cat/jq/python/sed) and points to a reader that prints env values masked.
TARGET: cfg — global/hooks/vault-read-guard.sh + a masked settings reader script
TIER: hook

FINDING: AFD_TOKEN has been in cfg-agent-fleet's private GitHub history since 2026-03-06.
ROOT CAUSE: Leaked before the value-fingerprint guard existed (CFG-652, 2026-09-21); never purged.
FIX: MG decides: history purge of the four commits, or record acceptance (repo private).
TARGET: cfg backlog
TIER: backlog

## Rules merged into oblivion — read-only Fable audit (S367), summary

Full history of global CLAUDE.md (286 commits), global foundation/reference/knowledge, aIware + crucible CLAUDE.md. Lost or weakened without recorded MG approval of the drop:
1. "User actions go LAST" (196fd78b, lrn 2026-03-12) and CFG-609 "never a bare ordinal" — dropped by 0a26da91 (2026-09-27); ab5e7127 (2026-10-23) then added "or number them when they cannot be asked yet", which inverts CFG-609. cfg decisions.md:235 still lists CFG-609 as live (tracking conflict).
2. "Feature self-integrity" (lrn audits verify MCP servers answer, hooks exist at deployed paths, env vars injected) — dropped 61765dd3 (2026-03-12); lrn SKILL.md has no such check.
3. "Subagent file creation guardrail" (subagents create no files unless the prompt names them) — dropped 3d8cb52c (auto-sync, 2026-03-12); only the `sub` row carries it.
4. "Parallelization is mandatory" (independent tasks as parallel subagents; lrn flags serialized work) — dropped 1e6c6741 (CFG-200, 2026-04-08); survives only in roster-management.md (loaded on roster changes).
5. "MEMORY.md is NEVER the answer … ALWAYS wrong" weakened to "NOT … usually wrong" — 00e963b8 (2026-03-20, sync from agent-fleet, no body).
6. "Plans must include a per-session token cost analysis table before approval" (CFG-24) — dropped 61765dd3; cfg decisions.md:621 still mandates it (tracking conflict).
7. Low: lrn roster-gap check clause (9f941bcf); "verified elsewhere ≠ safe to delete locally" (d8b78bbb, auto-sync); "never claim a file updated without a tool call" moved to conditional output-rules.md (ba588ac5).
**Root cause:** replacements are written fresh from a new finding and executed as "replace bullet"; Meta-Rules step 1 checks the new text, nothing checks that each removed sentence is moved, merged or retired by MG; auto-sync commits remove rules with no review. **Proposed mechanism:** PreToolUse hook `rule-removal-guard.sh` on `git commit` touching rule files: every removed bullet/sentence needs a `Rule-removed: "<text>" moved-to <path> | merged-into "<title>" | retired-by MG <date>` trailer, targets grep-verified; tests listed in the audit; config-auto-sync refuses what the guard would block.

## Outcome lrn 2 + oblivion audit (MG, S367-R…U)

R: pre-push scan + masked settings read → cfg (no history purge). S: actions-last + no-ordinals, subagent no-files guard, parallelization restored → cfg, re-checked against today's rules before commit (MG condition). T: rule-removal guard + lrn self-integrity → cfg. U: CFG-24 table retired, "verified elsewhere ≠ safe to delete locally" restored, two low items left out. Tracked: AIW-366 (aIware side), cfg inbox items 2026-10-30.
