---
name: numbered-action-items
description: End-of-response action/decision items for the user must be NUMBERED so MG can reference them by number
metadata: 
  node_type: memory
  type: feedback
  originSessionId: afdcc699-ca64-42aa-9318-9e00ec6d0900
---

When a response ends with items the user needs to act on, choose among, or reply to (a "For you" / "next steps" / "choices" block), NUMBER them (1., 2., 3.) — never dashes or bullets. MG replies by number ("do 1 and 3"); unnumbered items can't be cited, which forces him to re-quote them.

**Why:** MG steers fast by referencing items by index. Bullets break that workflow and irritate him (corrected S241 2026-07-05, sharply).

**How to apply:** any closing action/decision list gets numbers. Plain bullets are fine only for non-referenceable FYI. Likely a fleet-wide interaction preference, not aIware-specific — promote to a global rule if it recurs elsewhere. Nuance vs [[list-enumeration]] (avoid two same-scheme numbered lists back-to-back): satisfy both by numbering the *action* list and using prose/sub-bullets for any preceding enumerated content.
