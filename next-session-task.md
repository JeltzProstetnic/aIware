task: true
backlog: AIW-74
file: backlog.md
description: Verify the conversation-log drift guard hook actually fires. New project SessionStart hook in `.claude/settings.json` → `scripts/check-convlog-sync.sh` needs one-time approval. Confirm Claude Code prompted/approved it (approve if asked); confirm no spurious WARN (silent when conversation-log max heading == git max "Session NNN"). Re-run `bash scripts/test-check-convlog-sync.sh` if in doubt (expect 8/8). Close AIW-74 once confirmed live.
