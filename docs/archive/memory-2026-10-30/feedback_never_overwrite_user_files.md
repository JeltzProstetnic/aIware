---
name: Never overwrite user-edited files
description: When user is editing a file inline (Word, etc.), NEVER write to the same path — always use a new filename. Session 176 destroyed 30min of user work.
type: feedback
---

When the user opens a file for inline editing (Word .docx, any editor), NEVER overwrite that file path — even if the user reports a problem with the file. Always write rebuilt/fixed versions to a NEW filename.

**Why:** Session 176 — user opened .docx for inline review, reported rendering issue in the second half. I rebuilt the .docx to the same path while Word still had it open with 30 minutes of edits (highlights, strikethroughs, comments). The rebuild overwrote the user's work. No recovery possible.

**How to apply:** When rebuilding/regenerating any file the user has open for editing: (1) ALWAYS use a different filename (append -v2, -fixed, timestamp, etc.), (2) NEVER assume the original file is disposable, (3) Ask the user to close and save the edited file first if you need to reuse the same path.
