<!-- Action: reference. Tracked-by: AIW-125 (done), CFG-479 (deferred). Source: aIware WSL 2026-07-31 S279. -->
# simbook extraction — post-extraction follow-ups

**The P0 (CFG-478 Option 3) is DONE + verified. Forward exposure CLOSED.** This file tracks the
remaining NON-exposure-critical follow-ups only.

**S279 end status:** backlog migration DONE (8 items → `~/simbook/backlog.md`), simbook/backlog.md created,
pop-sci untracked leftovers DELETED (316 MB), dup AIW-127 RENUMBERED → AIW-134. **REMAINING = only the minor
README stale row (item 4 below) + the cfg-side items (already routed to the cross-project inbox: registry row,
CFG-479 history purge, F2 all-machine pull, Gmail-marker bump).** Nothing exposure-critical or urgent.

## Done (2026-07-31, S279)
- Private-only repo `JeltzProstetnic/simbook` created (init `3d5b7d0`, provenance `aIware@a05daaf0`).
  248 files: 160 pop-sci + 56 figure copies + render pipeline + 16 build scripts + typography_fixes + kdp-specs.
- Standalone build verified: EN interior 269pp + paperback cover, both exit 0.
- aIware `git rm`'d the book (189 files) + hardened `.push-filter.conf` (added the leaked root paths).
- aIware private `75ee90f3`; **public tip `5a78102b` VERIFIED clean** (0 book/isbn/private//session-*/kdp-specs; figures 101 + paper 79 stayed public).

## Remaining aIware-side (NONE exposure-critical)
1. **Backlog migration — PENDING MG REVIEW** (per "new backlog entries need user priority review").
   Book-specific items to move → `~/simbook/backlog.md`, MG confirms the split + priorities:
   - Clear book: AIW-24 (DE figures), AIW-60 (cover QA), AIW-87 (book revision), AIW-88 (send copies),
     AIW-98 (ed.3 refinements), AIW-113 (manuscript substring guard), AIW-115 (TOC folio glue),
     AIW-127 (translation KDP release sequence). AIW-114 (relocate book toolchain) = now MOOT (done via extraction).
   - Ambiguous (marketing, tied to social/outreach): AIW-22, AIW-70 (Davos giveaway), AIW-71 (Amazon review ask).
   - Theory/paper items that only MENTION the book STAY in aIware.
2. **Create `~/simbook/backlog.md`** with the confirmed migrated items.
3. **Untracked `~/aIware/pop-sci/` leftovers (~569 MB)** — regenerable + backed up in simbook. Delete or keep? (runbook step I, optional; respect backup-before-wipe — backup EXISTS in simbook.)
4. **Minor:** README.md ~line 196 still has a table row for `pop-sci/magazine-article.md` (now in simbook) — trim or leave.

## cfg-side (already routed to cross-project inbox 2026-07-31)
- ~~Register simbook in `registry.md` (Parent: aIware, PRIVATE-only).~~ **DONE 2026-08-02 (S280, MG-directed): simbook added to `registry.md` (P1, Parent aIware, PRIVATE-only) + `dashboard-cache.md` row → now shows in the `af` picker nested under aIware. simopt also bumped P4→P2 per MG.**
- Create **CFG-479** = deferred purge of book blobs from aIware's PUBLIC history (method = MG's call). *(STILL OPEN — MG-gated.)*
- **F2:** every other machine must `git -C ~/cfg-agent-fleet pull` (fixed filtered-push) + `git -C ~/aIware` pull private (gets extraction) before its next aIware push.

## Honest framing (carry into any report)
Manuscripts were world-readable ~5.5 months (2026-02-13 → 2026-07-31). Old public commits STILL carry
the blobs (deferred CFG-479). This closed FORWARD exposure only — "no new exposure; historical cleanup
pending", never "leak gone". Assume copies exist (Software Heritage etc.).
