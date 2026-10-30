---
name: feedback-response-length
description: "MG stops reading long responses — \"the text wall has lost me\". Lead with the answer, keep it short."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4b03c32c-fcfc-4b15-8c42-d329f665ae90
  modified: 2026-08-23T19:29:03.004Z
---

**MG, 2026-08-23 (S306), verbatim: *"the text wall has lost me."*** He had asked a direct question,
got five paragraphs of argument, and disengaged — the substance was fine and it still failed, because
he did not read it.

**Why:** long responses do not get skimmed, they get abandoned. A correct answer buried in paragraph
four is a wrong answer. This is the same failure the closing-action-items rule already guards against
in one direction ([[feedback-numbered-action-items]]) — this is the general case.

**How to apply:**
- **Answer in the first sentence.** Then stop, or give at most two or three short paragraphs.
- Reserve length for artifacts, not chat. A long argument belongs in a `drafts/` file he can read when
  he chooses — the same rule as form-fill content going to a file, for the same reason.
- Tool output and diffs already cost him hundreds of scrollback lines. Prose competes with that.
- Applies hardest when he is annoyed or time-pressed. At those moments he wants the verdict, not the
  reasoning that produced it. Offer the reasoning; do not deliver it unasked.
- Bartl already specifies "one plain-words verdict sentence a tired person could repeat back". This
  is that rule, enforced on total length rather than on the verdict alone.

Related: [[feedback-numbered-action-items]]
