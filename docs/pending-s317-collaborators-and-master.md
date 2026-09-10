<!-- Action: await-user-decision -->
<!-- Tracked-by: AIW-10, AIW-253, AIW-210, AIW-182, AIW-254 -->
# S317 — one decision that is MG's, then the master's v16 queue

S316 closed `AIW-250` and `AIW-218`, published the companion as v2, first-deposited both remaining
formalization roadmaps, and ruled `AIW-253`. What is left divides cleanly into one thing only MG can
answer and a queue that does not need him.

---

## ⚠ THE DECISION — `AIW-10`, and it has been the open half all along

**All three formalization roadmaps are now citable preprints.** FMT `10.5281/zenodo.21843693`, RIM
`10.5281/zenodo.22133501`, SB-HC4A `10.5281/zenodo.22133504`. That removes the excuse the item had been
sitting behind; it does not close it. **No collaborator has been approached, and each roadmap explicitly
defers verification of its formal apparatus to domain experts**, so the ask is concrete and unusually
easy to state — which makes the missing input *who*, not *what*.

**MG's call, and a session should not invent the answer:**

1. **Does this go out at all right now**, or does it wait for MoC7 (Oct 12–16), where face-to-face is a
   better first contact than cold email and the poster is already accepted?
2. **Which roadmap leads?** They want different people. FMT formalization → information geometry,
   dynamical systems. RIM → stochastic differential equations, bifurcation theory, psychometrics
   (Wittmann is already an active correspondent and the obvious first read on this one). SB-HC4A →
   mathematical physics, category theory, cellular automata — Wetterich is cited heavily and is the
   nearest thing to a natural recipient the corpus has.
3. **Named targets.** The person lookup chain applies before any drafting:
   `~/cfg-agent-fleet/cross-project/contacts.md` is canonical, and
   `~/cfg-agent-fleet/cross-project/fmt-visibility-strategy.md` is the single source of truth for
   outreach status. Check both before proposing anyone, and check the communications log for what has
   already been said to them.

⚠ **Do not draft researcher email without MG naming targets.** The outreach workflow is atomic and its
first two steps are contacts + communications-log checks; skipping to a draft inverts it.

---

## The queue that does NOT need him

1. **`AIW-253`'s master text.** The ruling is made (forward direction derived, reverse asserted; pattern
   **#40** written). What is open is *placement*: §7's comparison entries are the natural home given the
   Gurnee J-space contrast, and it rides `AIW-210`'s v16 rather than a bump of its own. Also unwritten:
   the cheap falsifier — train a comparable model on a corpus no workspace-bearing mind produced
   (proof libraries, genomic sequence, simulation traces, game records) and ask whether J-space-like
   structure appears at all.
2. **`AIW-210` — the FMT master's v16.** The `.md` and `.tex` now carry S313–S316 edits the published
   v15 does not, including this session's three category-error repairs and the condensation-graph→block-search
   correction. That queue only grows; at some point it is a version.
3. **`AIW-182`'s remaining third.** The nature/nurture rationale paragraph MG ruled into the companion at
   S299, with its non-optional scope sentence. It needs the rationale section `AIW-141`(b) rules in, which
   the paper does not have — a section to write, not a paragraph to paste.
4. **`AIW-254`'s remaining parts.** The venue column is fixed; the EN-book "available next week" text, the
   German-translation-in-preparation line, the 8-live/4-forthcoming reality and the ASIN matrix are not.
   `ABOUT.md` row 1 also still says *"Preprint (v8)"* against a published v15.

---

## State to carry

- **Three deposits this session, all verified by reading them back:** RIM roadmap concept
  `10.5281/zenodo.22133501`, SB-HC4A roadmap concept `10.5281/zenodo.22133504`, companion v2
  `10.5281/zenodo.22133843` (concept `…21610993`). All md5-match their repo canonicals.
- **New tooling, and the incidents behind it.** `scripts/zenodo_first_deposit.py` mints new records — the
  old script could only add versions, which nobody had noticed because nothing had needed a first deposit.
  `scripts/zenodo_metadata.py` carries a `ZENODO_TITLE` override — without it a retitle ruling was
  unexecutable, and the companion's v2 briefly went live with the new title in the PDF and the old one on
  the record. `build-md-pdf.sh` can now render a lower-case sigma, which it could not before.
- **The publish gate now distinguishes a roadmap from its parent paper.** `paper/cosmology_formal/` used to
  be a cosmology-paper token, so nine unrelated items blocked the roadmap. Tokens are filename-scoped;
  note `sb-hc4a` is a prefix of `sb-hc4a-formalization` and would re-merge them if anyone "tidies" it.
- **Gates at close:** suite 549 passed / 6 skipped, reference gate OK at 743 references, backlog
  done-but-open gate clean.
- **The fleet inbox is refusing filings.** 156 open against a ceiling of 25 — `[work]` and `[rule]` items to
  cfg-agent-fleet are currently rejected outright; only `[fact]` gets through.
