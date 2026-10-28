<!-- Action: reference -->
<!-- Tracked-by: AIW-359 -->
# lrn 2026-10-27 (S362) — research mail sent from the wrong alias

Incident: the Mason thank-you (Gmail `1a17ddfd9408eeeb`, 15:59) went out from matthias@ instead of research@. The draft was created with `mcp__google-workspace__draft_gmail_message` (from_email=research@), then edited with `mcp__claude_ai_Gmail__update_draft`, which has no From field and re-sends the draft from the account default (matthias@). MG was told the draft was ready without the From being re-checked.

FINDING: Editing a research@ draft with the claude.ai connector silently reset its sender to matthias@.
ROOT CAUSE: The gmail-compose point-of-action hook matches `draft_gmail_message|create_draft` but not `mcp__claude_ai_Gmail__update_draft`, and gmail-management.md documents the connector's URL rewriting but not that it cannot keep a Send-As alias, so nothing fired at the edit.
FIX: Never edit a draft that must leave from a Send-As alias with `mcp__claude_ai_Gmail__update_draft`; recreate it with `draft_gmail_message` and `from_email`, and delete the old draft.
TARGET: ~/.claude/knowledge/gmail-management.md (next to the URL-rewrite warning) + the gmail-compose hook matcher in settings.json gains `mcp__claude_ai_Gmail__update_draft`, with the same one-line message.
TIER: hook + extend-existing (cfg-owned → inbox item to cfg-agent-fleet)

**MG approved 2026-10-27 ~23:40; filed to cfg-agent-fleet inbox as [rule].**
