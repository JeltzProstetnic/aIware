# Fleet auto-memory audit (aIware S367, 2026-10-30, read-only subagent on WSL)

**Trigger.** aIware's numbered-lists rule existed only in Claude Code auto-memory and never fired. MG: *"given our knowledge base, nothing ever should have to rely or come from memory"*, then *"RCA and check if other sessions committed the same stupidity"*. aIware's own memory was emptied the same session (archive `docs/archive/memory-2026-10-30/`, commit b2ea254d).

## Cause
1. **Auto-memory is on.** CC 2.1.280 keeps it on unless env `CLAUDE_CODE_DISABLE_AUTO_MEMORY` is truthy or setting `autoMemoryEnabled` is false; neither is set in the live WSL `settings.json` nor in the repo template `~/cfg-agent-fleet/setup/config/settings.json`.
2. **The March disable never reached the repo.** 2026-03-03 the office session set `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` by hand in that machine's live settings; `cc-install-invariants.sh:202` lists the key as "cc-mirror-managed" and the template omits it.
3. **The detector checks the wrong path.** `04-auto-fix.sh` Check 4.7 looks at `$PROJECT_DIR/MEMORY.md` and `$PROJECT_DIR/memory/`; the real location is `$CLAUDE_CONFIG_DIR/projects/<sanitized-cwd>/memory/`. No PreToolUse hook covers `*/memory/*`.
4. **Point-of-action vendor instruction beats the prose rule** (lrn Known Faulty Pattern 10): the `# auto memory` system-prompt section tells the model to save a "feedback" memory after a correction — the exact shape of the files found (`type: feedback`, written right after an angry correction). Background `memextract`/auto-dream writers exist too.
5. **Writes after the rule landed** (2026-03-17): 19 files in 7 projects, 2026-03-23 … 2026-08-09, plus aIware's MEMORY.md (2026-10-30).

## Orphans (content only in memory — migrate before disabling)
| Project / file | Content | Target |
|---|---|---|
| agent-fleet/feedback_vps_live.md | VPS runs live systems, never propose it for tests | `~/.claude/machines/vps.md` § Identity → Notes (cfg) |
| ivoclar-regulatory/feedback_check_existing_assets.md | search existing legacy/intake/target-state docs before asking MG for examples | `~/ivoclar/regulatory/.claude/CLAUDE.md` (ivoclar) |
| p0rn/feedback_trash_policy_universal.md | 8TB-trash + hard-delete policy applies to every deletion, not only curation | widen `~/p0rn/CLAUDE.md` HARD RULE "Delete-during-curation semantics" (p0rn) |
| p0rn/feedback_no_devtools_debug.md | never ask MG to attach DevTools; build server-side logging | `~/p0rn/CLAUDE.md` (p0rn) |
| batch-langextract/MEMORY.md (part) | Avalonia gotchas | `~/batch_langextract/.claude/knowledge/technical-context.md`. ⚠ CONFLICT to report, not reconcile: memory says Azure header `x-api-key`, CLAUDE.md:69 + technical-context.md:37 say `api-key`. Token-in-.git/config recipe STALE. |
| ff/MEMORY.md (part) | Windows-side tools (VisoMaster, IndexTTS-2, SearXNG :8888, Windows Python + uv); "crush uses the first model in the array" | tools → `~/.claude/machines/wsl.md` (cfg); crush rule → `~/ff/AGENTS.md` |
| tsveta/MEMORY.md (part) | critique own synthesis before presenting; counter-proposals as separate docs; iterate decks in md before pptx | `~/ivoclar/tsveta/CLAUDE.md` (ivoclar) |

Duplicates (already in KB) and stale files: ivoclar-claims, regulatory ×3, p0rn ×4, muse/social/simopt MEMORY.md, claude-config ×2 (cli.js recipe wrong now), -mnt-c-Users-Matthias (model preference superseded), aIware-implementation, aios, ai2do, mails (archived projects). Every memory dir under `~/.claude/projects/`, `config-local`, `config-readonly` is empty.

## Fix — MG-approved S367-P ("Adopt as proposed")
Migrate the 7 orphans; then add `"CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1"` to the `env` block of `setup/config/settings.json` (deployed by `sync.sh deploy` to every machine; move the key out of the "cc-mirror-managed" list); point Check 4.7 at `$CLAUDE_CONFIG_DIR/projects/*/memory`. Live test: after deploy print the env value the live settings hold; `mkdir /tmp/memtest && env -C /tmp/memtest mclaude -p "ok"` must NOT create `$CLAUDE_CONFIG_DIR/projects/-tmp-memtest/memory`; control run with the var =0 in a second fresh dir must create it.

## Incident
The audit agent printed the live settings `env` block, including `AFD_TOKEN`'s value, into its own tool output (local subagent transcript only). MG S367-Q: accept, no rotation.
