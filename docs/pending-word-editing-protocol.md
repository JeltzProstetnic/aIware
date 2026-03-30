Action: reference
Tracked-by: cfg-agent-fleet inbox (done S40 2026-03-29)

# Word Inline Editing — Extraction Protocol

Knowledge for authoring projects where the user edits .docx files inline in Word and expects the agent to extract and apply changes.

## Three Mark Types

1. **Strikethrough** = delete this text. Detected via `w:strike`/`w:dstrike` in run properties.

2. **Yellow highlight** (shading `FFFF00` or highlight `yellow`) = poorly written passage, rewrite it. Not a deletion — a rewrite request.

3. **Direct text changes** = user retyped words, fixed phrasing, changed examples. No formatting marks — text simply differs from source. **Must be detected by diffing docx paragraph text against source .md line by line.**

## Extraction Protocol

1. Extract formatting marks (strikes, highlights, shading) from Word XML
2. **Diff full paragraph text** against source .md for the edited region — this catches direct rewrites
3. Check BOTH `w:highlight` AND `w:shd` for yellow (Word uses shading for manually applied yellow, highlight for toolbar yellow)
4. Direct edits may contain typos — apply the intent, fix obvious typos
5. If ambiguous (comment vs. edit), check context or ask
6. **Never overwrite the user's review file** — always write rebuilt .docx to a new filename

## Target

Create as `~/.claude/knowledge/word-editing-extraction.md`. Add to CLAUDE.md conditional loading table:
- Trigger: "Word inline editing, .docx review extraction, author review round"

## Origin

Learned in aIware Session 176. Missed direct text changes (heading rename, example swap, parenthetical reword) and yellow highlights (shading vs highlight distinction) across three review rounds.
