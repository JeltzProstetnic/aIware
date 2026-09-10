# Decisions Log — aIware

Curated record of strategic decisions and rationale. Topic-organized, not chronological.

## S316 (2026-08-27) — "more meaning than meaning" enters as a CUT, not as one claim

`AIW-253` owed two decisions and both are made, with MG holding the veto.

**Decision 1 — derived or asserted? Both, and separating them is the whole ruling.** Taken as one claim it
would have to inherit the weaker status and enter the master fully conceded. It does not have to. The
**forward** direction — a corpus produced by model-bearing systems contains recoverable explicit-model
structure, which is why LLMs extract more than direct interpretation — is **derived** from commitments FMT
already holds: 2015 (S.86) makes communication a serialization of an explicit model, and patterns #8/#14 give
those models structure worth serializing. No new posit. The **reverse** direction — that the deposited meanings
write back into language and alter it — is **asserted**, being the exact analogue of the consolidation channel
and stated rather than shown for language. It gets §3.4.3's treatment: conceded in our own voice, in the text,
before a reviewer supplies it.

**Decision 2 — yes, it gets a didactic-patterns entry**, as pattern **#40**. It qualifies on the same grounds
as #28–#30: it carries a discipline rule (state the difference from Harris/Firth or lose the contribution to
prior art), a framing trap that must not be re-introduced (the *1.2*-versus-*c* example is **referent**-vs-
referent, never glyph-vs-glyph, or the promiscuity of the glyph `c` answers it in one line), and a named
contrast case.

**⭐ The contrast case turned out to help rather than threaten.** Gurnee et al. 2026 (`arXiv:2607.15495`) is a
global workspace **without** closure — single forward pass, no recurrence, by their own architectural caveat —
and the item flagged it as raising our burden. It raises it and then pays it, along precisely the seam the cut
runs on: J-space *is* the forward direction demonstrated without closure, which costs FMT nothing because the
derived half never needed closure; what that system cannot do is the reverse direction, its weights being
frozen so no sustained pattern is imprinted back. **The two halves are separated empirically by a published
system, which is a better position than arguing for the separation.**

⚠ Not yet written into the master. Placement is a real decision — §7's comparison entries are the natural home
given the Gurnee contrast — and the master is v15-published with v16-bound edits already accumulating under
`AIW-210`, so it goes in with that version and not before.

## S316 (2026-08-27) — the companion is retitled on the cost axis, cosmology rests, and the third question turned out to rest on a premise that is false

**MG answered the three held decisions: *"iii, 2. yes, 3. rest"*.**

**1. The companion is retitled** to *"What Closure Costs and What It Buys: In-Silico Cost and
Capability Results for the Four-Model Architecture"*, applied to the draft the same session.
**What the retitle removes is an over-claim, and that is the reason it was owed.** v1 read
*"Closure and Criticality as **Enabling Conditions** for World-Modelling"*, and nothing in the paper
shows closure enabling anything — the results price it (§5) and condition its payoff (§4, §5.2),
which is a weaker and different claim. The chosen title also covers both halves of what the paper now
is, four capability results and three cost results, where the two rejected candidates each led on one
half. **The constraint MG set at S315 — the title may not claim more than cost — is satisfied by
construction:** *costs* and *buys* are both cost-axis words, and neither asserts necessity.
⚠ The published v1 deposit keeps the old title until republish; the propagation list lives on
`AIW-218` so the switch happens in one pass rather than drifting file by file.

**3. Cosmology rests. No v7 is scoped.** `AIW-165` and `AIW-166` stay open and unscheduled, each with
the ruling and a revive trigger written into its own entry. The reasoning that was put to MG and which
he accepted: neither item is a paragraph — `AIW-165`'s instruction as written would put a **withdrawn**
claim into the paper, and `AIW-166` carries its own design document plus an MG design conversation, so
reopening it reopens a design rather than an edit. `AIW-163` and `AIW-173` are experiments, not text.
v6 shipped the same week; the live path is the companion and the FMT master.

**2. ⚠ MG said yes to a Zenodo bump for the cosmology formalization, and the question he was answering
was built on a false premise. It is going back to him rather than being executed.** The premise, which
came through the S315 handover and the S315 decisions entry below, was that the formalization's
*published* copy states a fixed point the parent's *published* v6 rejects, and that it *"was not
separately republished at v5 either."* Both presuppose a deposit. **Three checks say there is none.**
The live v6 record `10.5281/zenodo.22132325` contains exactly one file, `sb-hc4a.pdf`. A Zenodo title
search for *"Toward a Mathematical Formalization"* returns **one** hit, the FMT roadmap
(`10.5281/zenodo.21909371`); the RIM and SB-HC4A roadmaps are absent. `README.md` and `ABOUT.md` both
carry the SB-HC4A formalization as GitHub-only with no DOI, and the session-log DOI table says *"no
deposit"* outright. **And the contradiction the bump was meant to remove does not exist either:** the
formalization was revised in the v6 pass, §5's line 398 already defines Φ as *"the composition of
holographic encoding with decompression"*, and its canonical PDF was promoted at S315 and is pushed.
⇒ **There is nothing to bump and nothing to fix.** The real question — whether the roadmap should get a
**first** deposit and a **new concept DOI**, which is a larger and irreversible step than a version bump
— was never put, so it is now. **This is the S303 rule earning its keep for the second time on the same
class of object:** *before acting on a handover's premise, verify the premise.* Resolving it cost three
commands; minting a permanent DOI on it could not have been undone.

**✅ RESOLVED THE SAME SESSION — MG chose "ii": deposit BOTH undeposited roadmaps rather than leave a
third inconsistent case.** Executed and verified.

| roadmap | concept DOI | v1 DOI |
|---|---|---|
| RIM formalization | `10.5281/zenodo.22133501` | `10.5281/zenodo.22133502` |
| SB-HC4A formalization | `10.5281/zenodo.22133504` | `10.5281/zenodo.22133505` |

Both files md5-match the repo canonicals byte for byte, checked by reading the deposits back.

**Three things this surfaced that are worth more than the deposits.**

**(i) The publish gate could not tell a roadmap from its parent paper, and it silently over-blocked.**
`paper/cosmology_formal/` was a *cosmology-paper* token, so the first gate run refused the roadmap's
deposit on **nine** open items, none of which was about the roadmap. Tokens are now filename-scoped —
note `sb-hc4a` is a prefix of `sb-hc4a-formalization`, so the bare stem would have re-merged them — and
each of the three roadmaps owns its own registry entry. **The general shape: a gate keyed on
path prefixes will fold a child artifact into its parent, and the failure mode is a refusal that looks
principled.**

**(ii) The order of the two deposits was forced by a citation, and the guard found it rather than a
human.** The SB-HC4A roadmap cited the RIM roadmap as *"Manuscript in preparation"*. Depositing it first
would have put a permanently dangling citation into the record. The new tool blocked on exactly that
line; RIM went first, its DOI was written into the citation, the PDF was rebuilt through the 2.0 pt
overflow gate (0 boxes) and promoted, and only then did SB-HC4A go. **Sequencing was a consequence of
the content, not a preference.**

**(iii) `scripts/zenodo-upload.sh` never could do this, and that was invisible until now.** It resolves
a concept DOI and POSTs `actions/newversion`, so it can only add to something that exists. The new
`scripts/zenodo_first_deposit.py` (23 tests, written first) mints new records, and every guard in it is
a past incident made mechanical: PDF-older-than-source (S303 shipped a stale PDF on the day the session
was about citation accuracy), the `AIW-206` frozen-vocabulary scan (`AIW-208` caught a CRU-58 result in
reconstructable detail one command before deposit, and EPC Art. 54 makes publication permanent), the
dangling-citation scan, and a refusal to first-deposit anything that already owns a concept DOI, which
would fork the record and split its citations across two DOIs with no way to merge them.

## S315 (2026-08-27) — cosmology v6 ships on the P1s alone, and the formalization is revised but not redeposited

**MG: *"ship now"***, given after being told that the two remaining cosmology P2s are not the
paragraph-sized items the S315 brief assumed — `AIW-165` carries a *"read this before acting"*
warning because the instruction as written would put a **withdrawn** claim into the paper, and
`AIW-166` has its own design document. **v6 is therefore a scoped correctness release**: one symbol
was carrying two different claims, and §6.4, §7.1 and §7.2 had not caught up with §6.3's own
definition. `10.5281/zenodo.22132325`; verified by downloading the deposit back and matching md5
against the repo canonical.

**The publish gate raised nine open items naming cosmology and all nine were deferred, each with a
ruling** (`docs/cosmology-rulings-s315.md`). The gate is doing what `AIW-185` built it for: there is
no blanket override, and naming each item is the point.

**Decided: the formalization is revised but NOT separately redeposited, and this is left to MG.**
Its canonical PDF is promoted and current — 47 pp, and clearing the overflow gate at zero boxes for
the first time. The argument for bumping it is that its *published* copy now states a fixed point
the parent's *published* v6 rejects, which is precisely the cross-document divergence v6 exists to
remove. The argument against is that it was not separately republished at v5 either. Minting a
permanent DOI is not a session's call to make unasked.

## S315 (2026-08-27) — a backlog entry that says it is done must not be left saying it is open

**Two entries in one session turned out to be finished work still marked open** — `AIW-159`, fixed
at S313 by a commit that described it while the backlog said nothing, and `AIW-179`, executed at
S300 on MG's go with *"✅ REGENERATED S300 ON MG'S GO"* sitting inside a `- [ ]` line. The second
cost this session real time re-deriving a decision MG had already made. **The same failure, one
level up, is what filled the fleet inbox**: promoting and deleting are one action and only the
promoting half kept happening.

**Built `scripts/check_backlog_consistency.py` (TDD, 15 tests).** ⚠ **Its scope is deliberately
narrow and stated as such: it catches only the class where the file itself carries the tell.**
`AIW-159`'s class needs a cross-check against git history and is not claimed — a check that
overstated its coverage would be worse than one that admits the gap.

**The design decision that matters is the rule, not the keyword list.** A first version flagged
`AIW-219`, whose literature check genuinely is discharged and whose drafting genuinely is not.
Flagging it would be wrong; ignoring every marker would give back the failure. ⇒ **An open entry may
record a finished sub-step provided it also states what is still open** — then a reader who trusts
the checkbox and a reader who trusts the prose land in the same place. `AIW-219` was missing exactly
that, and now says it. The first live run also caught a bug of my own: `NOT DONE S297` matching
`DONE S297`, which is the `comgarra` substring trap in a new costume.

## S315 (2026-08-27) — the computational companion is retitled on the COST axis, riding the AIW-218 revision

**MG ruled, presented with both of his own statements side by side.** The conflict was real and was not
resolved by a session picking one: `AIW-140` records S284's *"defer until more results, nobody is reading
it yet"* plus *"do not spend a DOI on a title-only correction"*, while crucible's inbox item of 2026-08-10
records *"'Closure and Criticality' that will have to change in the title probably, and hopefully we can
make a stronger statement even."*

**The ruling reconciles them rather than overriding either: retitle on the efficiency/cost axis, and ship
the new title as part of the `AIW-218` revision.** No DOI is spent on a title-only bump — which is what
S284 forbade — and the title changes at the moment a substantive revision happens, which is what the 08-10
remark asked for. This is also crucible's own recommendation, offered under the standing division of
labour (they supply substance and scope; aIware writes the text).

**What makes the retitle a correctness fix needing no new evidence.** v1 is titled *"Closure and
Criticality as **Enabling Conditions** for World-Modeling."* Crucible's No-Free-Lunch correction retires
exactly that: a finite closed loop unrolled over a finite horizon **is** feedforward + memory, so any I/O
capability is feedforward-approximable and closure can never be an enabling condition. **The FMT master
already made this correction in v14** — *"enabling conditions for a world-modeling step"* → *"govern how
efficiently a world-modeling step can be had."* The companion therefore carries in its **title** the
framing the master's body has already retracted, which is visible to any reader holding both.

**⛔ What the title may NOT claim, and this is the constraint that survives the ruling.** A *stronger*
statement is not purchasable. The result that would license one is **M1s3 (sufficiency)**: it has run
three times without adjudicating, §5.1 of its pre-registration is **unpopulated**, and the tier-B spiking
build is **gated** — and the blocker is a measurement instrument, not compute. Crucible says so in its own
words: do not write a stronger claim into a title in anticipation of it. **What may carry the title today
is the architectural-cost line** (A#7/A#8/A#9): opening the global loop costs 14.0% of the connectome
(dense) / 12.0% (modular) where return-freedom costs 74.0% / 71.5%, a 5.3× / 6.0× multiplier, exact and
scale-free. That is a *cost* result, and a title built on it is honest today.

**A title shortlist goes to MG before anything ships.**

## S315 (2026-08-27) — a checker whose default target is a build artifact reports staleness as drift

**`AIW-180` and `AIW-239` were the same defect wearing two backlog numbers**, and fixing them together was
cheaper than either alone. All three `--paper` shorthands in `check_md_pdf_drift.py` defaulted into `tmp/`,
so the one instrument that exists to catch silent content damage reported on whichever build happened to be
lying around — cosmology against a five-month-old S293 file (~16 phantom `md-only` segments, all of them
the S293 §3.1 rewrite the comparison file predated), `full` against a pre-S311 build (the S311 *repairs*
rendered as drift).

**The general lesson is worth more than the fix: staleness and drift are reported in the same vocabulary,
and the alarming reading is the wrong one.** A reviewer running the documented command would have concluded
the paper had massive content drift. ⇒ **Defaults point at the canonical artifact, and a target older than
its source announces itself** (`target_is_stale()`, exit 1, mtime-based). `AIW-239` had offered an
alternative — make the `tmp/` path an opt-in `--build` flag — and it was **not** taken: with the staleness
guard in place a stale canonical announces itself, which is the thing the opt-in was meant to protect
against, so the simpler default became the safe one.

## S314 (2026-08-27) — RIM Platinum v5 shipped, and the changelog was stale a second time

**⭐ The finding, and it is S312's finding recurring in a way S312's fix did not prevent.** S312 added
*diff the changelog against the git log* to the pre-deposit checklist. S314 still nearly shipped a stale
one — because the S313 session had written `docs/zenodo-changelog-rim-v5.md` **before** the final Fable
review, so it carried all four claims the review then retracted: motivation *"not a constituent of the loop
at all"*, Knowledge divided by the structure/process boundary, *"offline simulation time in an explicit
self-model"*, and a durable schooling effect on **fluid** ability. The changelog guard passed it, because
the guard checks only that the file declares the right version number. ⇒ **The durable rule is sharper than
S312's: a changelog written before the last review pass is stale by definition.** Recency against the git
log is not enough — what matters is whether it predates the last thing that changed the claims.

**Decided: B1 is settled against the paper's own sharpest sentence.** The paper said *"Motivation is not a
component of the loop at all"*, and its Abstract, its §3.2 loop bullets and ten further passages
contradicted it. The tempting repair was a component→constituent sweep. **The reviewer's diagnosis was
better and was adopted: the theory never needed *not in the loop*, it needed *not a capacity*.** M **is** a
node — the Matthew effect requires Knowledge and Performance to update it, and the loop is closed only if
they do — and what it is not is a **magnitude**. One reconciliation passage stating that, plus the
level→policy translation, **licenses** the surviving passages rather than requiring them to be rewritten.
A theory claim that needs ten edits to be consistent is usually the wrong claim, not ten wrong sentences.

**Decided: the `.tex` mirror tools were not used, on their own evidence.** `mirror_rim_tex.py --dry-run`
planned 20 edits and reported **2 unplaceable inserts and 12 possessive citations that would degrade to
plain text** — defect class 4 from the S313 handover, announced in advance by the tool itself. ~20 matched
`Edit` calls were made instead. **A dry run that predicts a known defect class is a decision input, not a
warning to click through.**

**Decided: no in-place canonical writes, anywhere in the build layer (`AIW-245`).** The S300 guard had made
the *default* safe and left `--canonical` writing in place, which is why S313 had to hand-hold the cosmology
build. The fix removes the mode entirely: `resolve_build_paths()` takes **no** canonical parameter, so the
build location is not a function of the promotion decision and there is nothing to get wrong. **And the exit
code is not trusted** — the gate reads the `.log`, because pdflatex walks past a Unicode error, drops the
glyph, keeps going, and still writes a PDF; the non-zero status arrives after the damage. `AIW-247` records
that `build_rim_pdf.py` has the same shape and was found only because this fix was being written.

**Decided: measure the register against the file, not against a feeling.** The session's own prose first
measured denser than the paper it joined; four constructions were removed until the file-wide rate sat at
**4.55/1k against HEAD's 4.57**. The S313 lesson — *a green whole-file gate is not clearance for a new
draft* — was applied to the session's own output rather than only to the paper's.

**MG rulings:** deposit v5; **Abstract stays at 430 words** against MDPI's ~200, because cutting to 200 means
dropping the disconfirmation criteria the reviewer named as a strength; public mirror pushed **after** the
deposit, not before; the `:407` AI-use declaration ships unchanged. And on the fleet: **the cross-project
inbox ceiling is unacceptable as it stands** — *"where else should other projects write???"* — because the
boundary rule makes the inbox the only sanctioned channel and the ceiling then closes it while naming no
alternative. **A ceiling on an inbox punishes the writer for the reader's backlog.** Reported to cfg.

## S312 (2026-08-26) — FMT v15 shipped, and the gate the chain does not have

**⭐ The finding worth keeping: no gate in the publish chain can see the changelog.** The S311 handover said
the deposit was the only step left. It was wrong — `docs/zenodo-changelog-fmt-v15.md` was last touched
before the third Fable review, so v15's release notes described the paper up to S310 and covered none of the
45-repair fold-in, including two garbled citations that were rendering in the *published* v14 PDF. The
reference gate proves citations resolve; the drift checker proves the PDF matches its source; the publish
gate proves no open backlog item names the artifact. **A deposit can still ship release notes that
under-report it by an entire review.** ⇒ *Diff the changelog against the git log* is now part of the
pre-deposit checklist.

**Decided: file the backlog item before the deposit, even though it joins the ack list.** `AIW-239` was
surfaced by the pre-deposit gate run and names `paper/full/`, so filing it moved the ack list from the four
that had come back identical three times to five. Rewording it to dodge the path token would have been
gaming the mechanism the gate exists to enforce. **An ack list that grows because a real item was found is
the gate working.**

**Decided: every fold-in runs as an all-or-nothing asserted pass.** A repair that cannot be located exactly
once in *each* target file aborts the whole run having written nothing. Three RIM repairs did abort on the
first two attempts — the hand-maintained `.tex` sets em dashes tight and renders citations as `\citep` /
`\citeauthor` — and catching that as an abort rather than a silent partial application is the entire point.
**This is the mechanical answer to the half-applied-repair disease that S309 and S310 both recorded as a
rule and then failed to apply.**

**Decided: a diff baseline is verified, never assumed.** MG asked for a changes-highlighted copy before
approving v15. The baseline commit was confirmed against the *published* v14 PDF pulled from Zenodo by
marker counts — weak illusionism 6/6, criticality commitment 15/15, Tagliazucchi 7/7 — before any diff was
trusted. **A diff against a guessed baseline is a confident picture of the wrong thing.** The tool that
produced it (`build_changes_highlighted_pdf.py`) replaced `build_review_pdf.py`, whose hardcoded highlight
list from an early-2026 session would have silently marked the wrong passages while looking authoritative.

**Decided: check the repo before writing to a person.** MG's instruction on the RIM Wittmann blocker was
*"check correspondence etc first"* — and the answer was already in `docs/wittmann-materials-summary.md`. The
M→K→Performance claim, the ~50% variance figure and intelligence-as-knowledge-as-strongest-predictor all
belong to Wittmann's **Singapore 2002 ICAP** paper, not to Wittmann & Süß (1999), which is the
Brunswik-symmetry paper. Two review agents had independently suspected the misattribution and neither could
reach the paywalled chapter to confirm it. **The evidence was local the whole time.**

**Decided: cite the unpublished conference paper.** MG, on being told the source is an unpublished ICAP
presentation: *"in this special case yes, unfortunately it is our strongest formal academic signal and even
more unfortunately without that RIM has zero chance."* Annotated `verified-manual` in the manifest with its
evidence; Crossref's near-miss confirmed the venue as the XXV congress, Singapore, 7–12 July 2002.

**Decided (theory): motivation is an allocation policy over the loop, not a component of it.** MG's
definition had gone hollow on the motivation axis because RIM types M as a component alongside K and P, and
FMT posits no motivational faculty to be one. As a policy — what gets re-simulated, how often, pointed at
what — it explains why motivation resists trait measurement, *derives* Brunswik attenuation instead of
invoking it, and converts the paper's consistency-over-level prediction from stipulation to consequence.
⚠ **The ground is occupied**: Kanfer & Ackerman (1989) model motivation as attentional-resource allocation
*inside the ability literature*, and Ackerman is RIM's chief interlocutor. What stays separable is that the
allocated resource is offline simulation time in an explicit self-model across developmental time. **§3.4
must name Kanfer & Ackerman, Shenhav and Kurzban before a referee does.**

## S310 (2026-08-25, afternoon) — the second review, and why a half-reviewed paper stays unedited

**⭐ The lesson repeated for a third time, which is itself the finding: the sweep was not done by pattern.**
S309 adopted *"sweep every finding by pattern across the whole file, never by line number"* (below) after
the disease bit twice. MG's criticality-is-an-effect ruling was then applied at twelve sites — **and left
four sites still calling criticality a prerequisite or a commitment** (`:771`, `:877`, `:901`, `:1058`),
three of them mirrored into the `.tex`. **Adopting a rule is not applying it.** The next fold-in must begin
with the pattern sweep, not end with one.

**Decided: nothing gets folded in until the review is complete.** Three of six agents died on Fable credits,
leaving §3 — the theoretical core, a quarter of the paper — and §8–11 entirely unreviewed. Applying the
finished sections' 10 blockers and 39 should-fixes now would mean editing a half-reviewed manuscript
section by section, which is precisely the mechanism that produces half-applied repairs. The whole review
lands as one pass or not at all.

**Decided: re-derive the publish-gate acks rather than paste them.** The S309 handover instructed this and
the reason held — the list had shrunk three times in one session as items were verified closed. It came back
identical this time; the discipline still cost one command and remains the rule.

**Decided: a failed subagent's output is read, not discarded.** The dying cross-section agent returned one
partial lead in its result field. Verified by hand it proved **correct and understated** — a hand grep found
a wider wording family than the agent had named. A run that ends in an API error can still have produced
findings.

**Decided: report tracking conflicts, do not reconcile them.** Three backlog IDs each carry two entries
disagreeing about whether they are done, and three canonical files disagree about whether the cosmology
canonical build has ever been run. Both went to MG untouched. Picking a side by guess is how a real
remainder gets silently erased.

**Operational consequence: Fable is no longer reliably free.** The agent roster still describes it as
available and unmetered within the Max subscription; it exhausted mid-session. A six-agent Fable fan-out is
now a resource decision, not a free one — check credits before commissioning one.

## S309/S310 (2026-08-25) — a mandatory review that the paper failed, and four MG rulings

**The review earned its place in the sequence.** MG's standing instruction puts a Fable review before
every publish. v15 was built, verified, staged and dry-run green — and the review still found **17
blockers**. A green gate is not a reviewed paper.

**⭐ The finding that outranks any single defect: a defect class is not closed when the instances someone
happened to grep are closed.** Three repairs made in earlier sessions had been applied at some of their
sites and not all, and the unrepaired sites were still sitting in the publish candidate — Hengen & Shew
credited with a criticality–consciousness conclusion at four surviving sites, the Kawakita group-level
hedge missing from the Conclusion, and one sentence that said both "general anaesthesia" and "during
sedation" because a previous repair had fixed only its first half. **Adopted: sweep every finding by
pattern across the whole file, never by line number.**

### MG's four rulings

1. **Criticality is an EFFECT** (*"criticality is a effect, fix."*). The requirement is open-ended Class 4
   computation; near-criticality is what that requirement leaves in *neural tissue*. Twelve sites were
   corrected directly — and the correction pass then found the ruling reaches much further than expected:
   the substrate-independence thesis, the multiple-realizability footnote, the artificial-consciousness
   implication, the LLM comparison and the falsifiability condition **all still asked for operation "at
   criticality"**, a test silicon cannot pass because it has no neural signature to show. As written,
   those claims could not be satisfied by the very substrates they quantify over.
2. **"Return" is acceptable where it is not contrary to established subject terms.** The four
   graph-theoretic occurrences (`return-free`, `returning component`, `non-return`, `return-freedom`)
   stay: they are glossed inline and sit beside the paper's own `acyclicity`, and the sixth banked result
   is priced on the distinction they carry — relocating closure costs 14.0%/12.0%, abolishing any closed
   walk costs 74.0%/71.5%. Calling both "closure" would leave the 5.3×/6.0× multipliers describing nothing.
3. **The unfolding argument is answered on efficiency grounds**, MG accepting the commitment explicitly.
   The paper had characterised Doerig's target backwards — IIT denies the I/O identification, which is
   *why* it is a target — so FMT's claimed escape was the same move IIT makes. The passage now concedes
   the argument's force is **epistemic**, and answers it on cost: unfolding trades a reused loop for
   replicated stages, and under a resource bound the two systems do not agree on behaviour after all. It
   states plainly that this **converts an unfalsifiable distinction into an empirical one rather than
   dissolving the argument**, and that on an unbounded substrate the theory has no experiment to offer.
4. **"We DO address all"** — a review finding **rejected**. The Introduction's claim that the theory
   addresses all eight requirements stands, notwithstanding Table 5's partial ratings on three.

### MG's defer rule, and what it changed

*"Defer only things that makes our work more efficient if deferred."* Applied to the publish gate, this
took the list from **nine to four** — five items turned out to be **finished rather than deferrable**,
and two of those were only discovered by testing rather than by reading: `AIW-204` was closed on
`verify_references.py --check` reporting 724 references and 349 citations matched across all papers, and
`AIW-231`'s two remainders were fixed because deferring one of them would have let a fiction ("+ k relay
neurons" — there are no relay cells) propagate into the cosmology A5 argument at step 3, where it costs
more to find. **Clearing a gate is not a reason to defer.**

### Three process lessons banked

- **An approved clause is approved for its content, not for its fit with the paragraph it lands in.** The
  MG-approved τ_syn clause was pasted verbatim as instructed, and the verbatim paste is exactly what
  created an apparent self-contradiction with its own paragraph.
- **Verify against the extracted PDF text, not the `.tex`** — and expect two false-negative classes that
  both fired: typographic apostrophes and page numbers interleaving mid-phrase. Search short fragments.
- **Trust the machinery over your own edit.** The test suite caught a banned phrase a repair had just
  introduced; the build caught two LaTeX defects the mirror script introduced; the drift checker caught an
  md↔tex wording divergence. All three were self-inflicted and all three were caught by a gate.

### Reported, not reconciled

`AIW-231`, `AIW-204` and `AIW-210` each carry **two backlog entries with conflicting states**. Per the
Data Integrity rule this is a bug to report rather than resolve — picking one is how a real remainder gets
erased.


## S307 (2026-08-24) — the gates check existence, nobody had checked characterization

**MG's publishing rule, stated when asked whether the §8.9 repairs needed an erratum on v15 or should
wait for v16:** *"what are you talking about? as always we fix the defects, bundle them with new findings
and evidence whenever available, then upload a fixed version."* ⇒ **There is no erratum-versus-next-version
question.** Defects are repaired in source immediately; the version bump is a separate, later, bundled
step. The practical consequence, adopted this session: repair sources now, and **leave canonical PDFs
alone where they are published artifacts**, recording their blob hashes so provenance stays retrievable.
The one exception is RIM, whose drift gate compares source against a build and therefore forces a rebuild.

**The defect class this exposed, and it is the session's main finding.** Every existing gate checks
whether a cited work *exists*: the works exist, the bibliographic details are right, the keys resolve,
`.md`/`.tex`/PDF agree, `verify_references.py --check` exits 0. **Nothing had ever checked whether the
sentence citing a source says what the source says.** Audits of the FMT master and RIM found **sixteen and
six defects respectively, and every confirmed one failed in the same direction — toward more support than
the source provides.** Among them: a quotation attributed verbatim to authors who never wrote it; a
paper's central conclusion inverted into the opposite of what it argues; percentages and dose-response
curves attributed to a study that used a single dose; both species wrong in an evidence table, leaving
that row's own claim unsupported; and an age comparison that does not occur in the cited work at all.
⇒ **Existence is mechanical and now gated. Characterization is not automatable and stays a human review
step** — which is precisely why MG's standing instruction is that every publish is preceded by a Fable
review.

**A second-order finding worth more than any single repair: a passing gate hid a wrong work.** The
reference gate had `fmt:Hameroff1996` recorded `"status": "verified"` — against an MIT Press book chapter,
not the Elsevier article the paper cites. Cause: a character class in the DOI parser excluded `)`, so an
old Elsevier DOI containing literal parentheses truncated, the lookup failed, and the resolver **silently
fell back to a title query and matched something else**. Six such DOIs are in the corpus. ⇒ **A fallback
that cannot report that it fired is not a fallback, it is a forgery.** The parser is fixed; the silent
substitution is tracked as `AIW-234` and is not.

**Never trust a mirror; verify against the built artifact.** A mirror agent computed its `.tex` diff at
start-up, three further `.md` edits landed while it worked, and one never reached the `.tex`. It was
caught only by extracting the **built PDF's** text and grepping each repaired phrase. Two of those checks
produced false negatives — page numbers interleave into the extracted stream and split phrases — so the
method needs de-hyphenation and short fragments. **This is the S299 defect class again** (corrections
reaching the tracker but not the artifact), running through a different pipe.

**On dependencies that turn out not to exist.** Three items were carried as blocked on the sister project.
Checked individually, **none of them were**: one was pure wording with MG's own formulation already on
record, one needed only published literature, and the "gated" third was gated on a public CC-BY dataset
this project can download. ⇒ **Verify a dependency against the artifact before deferring work to it.**

**MG's ruling on the disconnection control, which settles an operationalization question that had been
open since crucible raised it:** *"disconnection doesn't remove closure, it splits one closed system into
two"* — **correct**. So efferent disconnection and ablation of the explicit self-model are **not**
interchangeable, and the master's "or" was wrong. The repair makes the correction into a strength:
disconnection is the *right* control precisely because it holds the model constant and withdraws only its
availability, so a loss of self-recognition cannot be attributed to the model's absence. Ablation would
remove model and coupling together and could not distinguish them.

**And a claim that did not survive contact with its primaries.** `AIW-194`'s recall tag: the *requirement*
survives and is strengthened, but a **discrete source tag is the position source-monitoring theory
explicitly defined itself against in 1993** (Johnson, Hashtroudi & Lindsay). MG's chemistry intuition is
partly right — acetylcholine does bias circuits by pathway — but it separates **encoding from retrieval**,
not recall from perception, and puts perception and encoding on the same side. ⇒ Write it as
requirement-plus-prediction, never as a mechanism claim.

## S306 (2026-08-23) — a defect class that only shows across two files, and a measurement tool built with its overclaim disabled in code

- **Two files can each be internally consistent and jointly wrong, and no single-file check finds
  it.** The NoC `Gazzaniga 1965` entry carried the *title of a different 1973 paper by different
  authors* over a page range that does not exist — while **both `references.bib` files held the
  correct work all along**, so the printed PDF was never wrong. Nothing could have caught it except
  comparing the two lists, which is precisely what the `AIW-204` `.bib` arm was built for. It caught
  it on its second outing. **The general form: a correct build artifact can mask a wrong source, and
  reviewing either one alone certifies nothing.**
- **"Not required" is not "should not", and conflating them is how a defensible position becomes an
  indefensible one.** The NeurIPS workshop solicits no AI-use declaration, which made silence
  *permissible*. It did not make silence *right* for a paper describing transparency about AI
  contribution as the field's accepted instrument. **MG caught the tension; the procedural reasoning
  had been correct and rhetorically blind.** The disclosure went into §6 — where it stops being a
  confession and becomes an instance of the mechanism the paper proposes — and was paid for inside
  the page cap rather than by pushing past it.
- **An honesty constraint that matters gets enforced in code, not in a convention.** The detector may
  not emit a percent-AI figure, a probability framing, or a bare verdict. That is a guard function
  the builders and the CLI each run, pinned by 20 tests — because a convention would have been broken
  the first time somebody wanted a headline number, and the number would have been meaningless.
  A Binoculars score is a ratio of two cross-entropies calibrated to nothing.
- **Where a published paper and its released code disagree, the code is what the published thresholds
  were measured with.** Hans et al. Eq. (4) attributes the Binoculars numerator to the *observer*;
  the reference implementation uses the *performer*, and the paper's own Table 5 settles it — the US
  Constitution's published 0.7600 only reproduces one way. **Implementing the printed equation would
  have silently invalidated every threshold**, and produced numbers that looked entirely normal.
- **A cross-session bug report is a hypothesis until its exact string is reproduced locally.**
  Crucible flagged a false claim at `:338` of the master; a first grep truncated at 400 characters
  and appeared to refute it. Crucible was right. **The check cost two minutes and would have caught
  the opposite case just as cheaply** — which is the argument for doing it every time, not for
  trusting more.
- **Three decisions that interact must be put to the author together.** `AIW-220` began as a
  vocabulary question and became a three-part package once crucible confirmed that a mechanical
  "closure everywhere" sweep would collapse the 5.3×/6.0× distinction the sixth banked result rests
  on. **Ruling on one part in isolation produces a paper that contradicts itself**, so the package
  goes as one or not at all.

## S303 (2026-08-12) — citation integrity becomes a P0 concern, and a published paper is found to have been published

- **MG raised the citation gate to P0 with a one-line reason that should govern this class of work
  permanently: *"wrong references can damage reputation."*** The instruction that followed —
  *"2 now"* — treated 34 unverified references as more urgent than a conference deadline eight weeks
  out. The judgement is worth recording because it inverts the usual triage: a reference defect is
  cheap to fix and expensive to be caught at, so it outranks work that merely *feels* more pressing.
- **A handover can be confidently wrong about a fact it never checked.** The S302 brief said the
  formalization roadmap was an unpublished manuscript needing a first Zenodo deposit. It had been
  published on 2026-08-07. Nothing in the brief was dishonest; the claim had simply never been tested
  against the live record. ⇒ **Before acting on a handover's premise, verify the premise** — resolving
  the DOI took one command and changed what the session was doing. The same check cleared the
  disclosure worry attached to it: git showed the sensitive text entered the file the day *after*
  the deposit, so it was never public.
- **The right way to widen a quality gate is to accept that the number gets worse.** Registering the
  three formalization roadmaps exposed 129 references that had never been checked, 34 of them
  unresolved, and turned a green gate red. The alternative — leaving the papers outside the corpus to
  protect the number — is the blindness the gate exists to prevent. ⚠ **An exclusion list is only as
  good as the reason attached to each line**: all three roadmaps sat under a comment reading *"Each
  line is a decision, not an oversight,"* and the decision was defensible right up until one of those
  papers was published. Re-read exclusion reasons when circumstances change; the guard cannot do it.
- **A ratchet that says "may never be raised" should be argued with in public, not quietly.** The
  baseline was raised 0→34 with the reasoning written into the file and flagged to MG for veto, then
  returned to 0 the same session once the debt was cleared. Overriding a written instruction is
  sometimes right; doing it silently never is.
- **Cite what the source proves, not what it nearly proves.** The Bayesian Cramér–Rao citation was
  attributed to authors who did not write the paper — and the surrounding claim also overstated it,
  asserting a general result about the estimator where the source establishes a special case about the
  unfavourable *prior*. Both defects were in one sentence, and only reading the actual abstract
  surfaced the second. **A citation check that stops at "does this work exist" catches the first and
  misses the second.**
- **`.md` and `.tex` drift silently, and the gate only watches one of them.** The corrected citation
  survived in `sb-hc4a-formalization.tex` after removal from the `.md`, and was caught only because a
  safety assertion was written into the cleanup script. **The artifact that ships is the `.tex`+`.bib`
  build; the gate parses the `.md`.** Until `references.bib` joins the corpus, every reference claim
  carries this asterisk.
- **Publish after the corrections, not between them.** Zenodo v2 went out hours before two further
  citation fixes to the same paper, so the public record briefly carried incomplete references on the
  day the session was about reference correctness. Fixed by v3, but the sequencing was the error.
- **Deployment scripts that read from `tmp/` will eventually publish the wrong thing.**
  `zenodo-upload.sh` silently appends whatever sits at `tmp/zenodo-changelog.md`; a stale changelog for
  a *different paper* went live and had to be repaired on the published record. The file named the
  wrong version number, so a version-match assertion would have caught it.
- **Effort objections and correctness objections must be separated before a scope decision.** MG
  overrode a "not atomic" verdict on the book chapter with *"my time is the bottleneck, not yours"* —
  correctly, because three of the five objections were about agent effort (renumbering, covers,
  translations) and only two were about content. **Ranking objections by whose time they cost is what
  made the decision obvious.**
- **Geometry that is eyeballed will be wrong in a way markup cannot show.** Six successive hand-drawn
  repairs of one arrowhead each failed differently, and each failure was invisible in the SVG and
  obvious on a rendered crop. **The fix was not a better technique but a computed generator plus a
  render-and-look verification step** — and notably, the intuitive remedy (hand-draw instead of using
  markers) was the thing that had caused the defect.

## S302 (2026-08-12) — the disclosure decision splits in two, and the patent lane is re-scoped to what MG can afford

- **THE SPLIT, and it is the decision that unblocks everything: publishing the THEORY and publishing the
  IMPLEMENTATION are two separate decisions, and only the first has been made.** The freeze conversation had
  been treating "the freeze lifts" as "everything goes public", which is what made it look like an
  all-or-nothing choice between science and exclusivity. It is not. **MG's ruling: lift the freeze for
  PAPERS — v15, the formalization roadmap, MoC7 — and keep the crucible implementation CLOSED.**
  - **Trade secrecy is free.** Patents are what you buy when you want to *publish* an implementation and still
    control it. Keeping crucible closed costs nothing, needs no attorney, and is the single most effective
    available measure against "large labs implement my stuff" — they would have to rebuild from a paper rather
    than clone a repo.
  - ⚠ **Consequently the public OSF preregistration and the Show-HN spiking-code release are NOT unblocked by
    this.** They remain separate, still-open decisions. Note the genuine tension to weigh when they come up:
    the reach strategy (social `SOC-37`) wants the preregistered public experiment precisely *because* it is
    open, while value capture wants it closed. That tension is real and is not resolved here.
  - **The one real cost, stated so nobody rediscovers it as a surprise:** if MG ever wants to raise money on
    this, "it is all public" is a weak position — investors ask what stops someone else. Keeping crucible
    closed preserves that option at zero cost, which is a second reason to keep the two decisions apart.

- **The patent spend is not justified at present, and MG's own red-team is the reason.** `docs/patent/05-red-team.md`
  §5, verbatim: *"As a competitor: none. I would ship the §2.1 heterogeneous-tau implementation… and never need a
  licence or a tribunal. The claim set as drafted does not force me to the table — that is the commercial finding,
  and it is independent of every validity argument above."* §7 names the outcome plainly: the family may be
  *"publication-with-a-ribbon (defensive value, no exclusionary value)"*.
  - **MG has no capital for this**, and the honest comparison is not "publish and be exploited" versus "patent and
    be paid" — it is "publish and be exploited" versus the same, EUR 15k poorer.
  - **A patent would not have prevented any of the three outcomes MG actually fears.** Professors basing grants on
    the work: ideas are unpatentable and research use is not infringement, so no IP instrument touches it. Large
    labs implementing it: the red-team says the claims do not force anyone to the table, infringement inside a
    research lab is invisible, and enforcement on a configurable chip lands on the *customer*. The Ivoclar
    situation: unaffected.
  - **If the goal is DEFENSIVE — nobody else patents this and fences MG out — publication achieves it completely,
    for EUR 0.** A publication is prior art against the world from its date. That goal is already met.

- **The exclusionary-value question belongs to US, not to a lawyer — MG's correction, and it is right.** A patent
  attorney can rule on validity; whether a claim set *forces a competitor to negotiate* requires someone who knows
  spiking substrates, the fold theorem and multi-kinetics synapses. Counsel will not have that. ⇒ **Method adopted:
  run the design-around exercise in-house, briefed BLIND to the existing red-team so a matching result is
  independent confirmation rather than agreement.** MG's decision rule, verbatim: *"one fable pass for now. if a
  fable pass finds a way around its done. if not we consider."*

- **The fold theorem: ours as a recognition, never patentable, and it cannot be unpublished.**
  - **Provenance:** the identity `x' = tanh((W + W_fb·W_out)x + W_in·u)` was derived and numerically verified in
    crucible (to 3.2e-15, 2026-08-10). But `W_fb·W_out` is a rank-k outer product and adding it to the recurrent
    matrix is elementary linear algebra — any control theorist would see it immediately. **What is MG's is the
    recognition** that the naive closure arm collapses, and therefore that the interesting architecture is the one
    that does not. A framing contribution, not a mathematical discovery.
  - **MG's own point settles the loss question: a theorem is not an implementation.** Under EPC Art. 52(2)(a)
    mathematical methods as such are not inventions, so **the fold theorem was never patentable by anyone** and
    publishing it cost no patent right. What it cost is strategic surprise — it shows a competitor where the fence
    is. That is a competitive-intelligence loss, not an IP loss.
  - **It also carries an upside worth keeping:** it establishes the *problem-discovery* story, which is one of the
    better inventive-step arguments available for the non-foldable return. There is no non-obvious solution without
    a recognised problem.
  - **❌ "Remove it and hope nobody saw it" was considered and rejected.** It does not work mechanically — git
    history persists in forks and clones, Zenodo records and DOIs are permanent by design, and Software Heritage
    and the Internet Archive crawl public repos. For novelty, *made available to the public* is a one-way door:
    availability destroys novelty whether or not anyone read it, so deletion restores nothing. **And the attempt
    would be worse than the disclosure** — the US duty of candour (37 CFR 1.56) makes concealing known prior art
    the route to inequitable conduct and an unenforceable patent. **This is the same ruling MG already made in
    `AIW-206`** (*"do not scrub the logs — an accurate record… is better evidence than a sanitised one"*).
  - Mitigating fact: per `docs/patent/04-disclosure-chronology.md`, what is public is the **mechanism name plus a
    one-phrase repair hint**, not an enabling specification.

- **⚠ The thing a patent would fence does not exist yet.** `docs/patent/03-claim-architecture.md` §D.1: no
  end-to-end system with the non-foldable loop has ever been built and run; the limitation rests on the fold
  algebra plus constructive disclosure. Experiment **E1** is what would build it. ⇒ Filing family B today means
  filing on a system that never ran, which is precisely the EPO opposition ground the red-team names
  (Art. 83 sufficiency + Art. 56 via G 2/21). **Family A is filable; family B is not ready, and money does not
  make it ready — a software experiment does.**

- **▸ THE PATENT LANE IS CLOSED — the design-around test found the escape the same session.** Run per MG's
  rule (*"if a fable pass finds a way around its done"*), blinded to the existing red-team so that agreement
  would be independent confirmation. It found **multiple literal escapes for every family, several at zero
  measurable cost**, and advised *"do not take a licence; route around."*
  - **Claim 1's novelty is only the routing (L2+L5); the rest is admitted Izhikevich art** — so it is
    escapable *through its own prior art*, which is legally clean and cannot be drafted around without
    ensnaring the art. A pre-synaptic-only trace kept per neuron misses L3 twice, on published
    delta-rule/feedback-alignment ground, at 0–15 % cost and an O(E)→O(N) memory improvement.
  - **The folded factored return is FORCE (Sussillo & Abbott 2009)** — behaviourally identical by MG's own
    fold algebra, same synapse economy in factored form, and **family B's advantage over it is prophetic
    because E1 and E4 have never run.** `06` §5 called this escape "self-defeating"; on today's evidence that
    label is unearned, and correcting it is what turns the commercial answer negative.
  - **⚠ The fold theorem makes infringement unprovable from outside.** Folded and unfolded machines are
    I/O-identical, so no behavioural test distinguishes them; enforcement needs weights files or a silicon
    teardown, and opaque configured hardware is unauditable. A patent you cannot detect infringement of is
    not a commercial instrument.
  - **Two new drafting holes, worth keeping on file:** branch (ii) recites a delay *exceeding* every
    recurrent delay where it should recite *differing from* (one slow recurrent edge defeats it while the
    loop still genuinely fails to fold); and **the modulatory return — gain/threshold/time-constant
    modulation — is unclaimed entirely**, despite being arguably the better reading of "the self-model
    influences the world-model's update rule".
  - **Reopen condition, and it is a software experiment rather than a purchase:** E4 demonstrating a large
    real cost-or-trainability gap attributable specifically to the non-foldable return, *and* a refile with
    the seven gaps closed. Full report: `docs/patent/07-design-around-test.md`.

- **Alen Frey is out of the JAIC paper.** He wrote *"I'm out"* to MG with no reason and no stated scope. Out of the
  paper is certain; whether he is stepping back from contact or from Ivoclar work generally is unknown, and **MG
  will find out in person rather than chasing it — no follow-up is to be drafted.** The affiliation question
  (Ivoclar vs independent/ETH) is moot and closed; the §6 in-silico grounding he was to co-build is now unowned.
  Georgia Sousouri is unaffected. The record is kept deliberately neutral: no reason was given, so none is
  recorded, and a co-author who steps back in August may be available later.

## S301 (2026-08-11) — the patent lane opens, and the backlog turns out to be a leak channel

- **MG scoped the patent target himself, and the scope resolves the tension in the original goal.** His words:
  *"I would like to patent the actual way to implement it without extreme pain, which is 'take a spiking neural net
  with… recurrence… closure…' in a way that makes it as painful as possible to circumvent while leaving me as much
  publication freedom as possible."* ⇒ **The fence goes around the implementation recipe; the theory stays free.**
  It has to — FMT is published and therefore unpatentable, permanently in Europe. The stated ambition of blocking
  all AC is not achievable (five independent kill mechanisms, including FMT's own published No-Free-Lunch unroll
  passage, which is a printed design-around instruction). **But the other half of the goal is already achieved and
  permanently so: because MG published openly, nobody else can patent the FMT-definitional level either.** What is
  purchasable is a toll-booth on the efficient path.

- **The freeze serves publication freedom rather than fighting it, and it must always be stated that way.**
  Once a priority application is filed, the inventor's own later publications cannot invalidate it. So filing first
  is what *buys* the freedom to publish. The quiet period runs to the filing date, not indefinitely — weeks, not
  years. Stated any other way, the freeze reads as "stop publishing" and gets resisted for the wrong reason.

- **`backlog.md` was excluded from the public mirror after it was found to be the project's dominant
  unintentional-disclosure channel.** The trigger was self-inflicted: the S301 pushes put the `AIW-206` freeze
  entry on the public mirror, and that entry enumerated every still-unpublished item the patent lane depends on —
  **the freeze notice published the freeze list.** The wider pattern is worse than the incident: CRU-57 Stage-0
  hyperparameters went public through the backlog on 2026-08-04, and the closure-cost numbers on 2026-08-07, a day
  before the paper carried them. **The durable rule that follows: any claim of the form "X is not public yet" must
  be checked against `git log origin/main`, never against what has appeared as a paper.** History rewrite remains
  an open decision, to be done in one pass with the deferred `CFG-479` purge if it happens at all.

- **An adversarial review is worth its cost, and the disagreement it produced is the useful artifact.** A red-team
  broke the first claim set on two structural grounds, one of which — that a competitor running heterogeneous
  per-synapse time constants escapes the system claim for free — would have gutted the portfolio. The redraft
  disagreed with algebra: the fold identity holds for any *neuron-indexed* filter state, so the biologically
  supported, performance-positive variant does not break the fold at all. **That disagreement was routed to
  crucible to adjudicate rather than settled internally, because the fold theorem is crucible's result.**
  Neither analysis alone would have produced the answer.

- **Do not scrub the employer-exposure record.** An audit found crucible clean — 74 sessions, all on the private
  machine — while aIware ran on the Ivoclar office machine roughly fourteen times. Since aIware holds only
  already-published material and crucible holds the entire patentable surface, the contemporaneous record is
  *favourable evidence*, and altering it would be the actually damaging act.

## S300 (2026-08-10/11) — the verification session, and what it cost the theory

- **Two claims died under primary-source verification, and both had been load-bearing.** The proposed
  differentiator against model-based RL — that FMT's override works by *re-instantiating the phenomenal
  value* rather than retrieving an abstract state-value — is **already claimed by that literature**:
  Dayan & Berridge (2014) say a model-based system evaluating an outcome "based on memory of its hedonic
  experience may need to **retaste or re-experience** outcome again." Two further steps of the rollercoaster
  mechanism are occupied too (Gershman/Markman/Otto 2014 for *the implicit side complies*; Bornstein et al.
  2017, with a p-value, for the older-positive-beats-recent-negative signature). Separately, **the Domhoff &
  Fox "continuum" is not in their paper** — they claim *dreaming as intensified mind-wandering*, a narrower
  and contested thesis, and the word "continuum" appears once, about something else.
- **MG's ruling on both (2026-08-10): position against the field's UNSETTLEDNESS, not against a monolith**
  — sixteen accounts, nine mutually incompatible arbitrating variables, twenty-one years without
  convergence, and **recency never referees between systems** in any of them. The unclaimed ground is the
  **reordering / priority-inversion signature**. And *dreaming*-for-the-whole-kind now stands on **FMT's own
  architecture**, which is the stronger footing anyway: Kirberg & Windt (2026) cuts against *intensification*,
  a claim FMT never made, so their result threatens the borrowed grouping and not ours.
- **The ictal-route disagreement resolved as UNSETTLED, and neither source was promoted.** The paper said
  hypersynchrony was the typical route out of Class 4; the knowledge file said supercritical was dominant.
  **Both over-read Meisel et al. 2012**, which is a focal-seizure phase-locking study that never uses
  "supercritical" or "hypersynchrony" and does not cover generalized tonic-clonic seizures. Onset is
  heterogeneous (Truccolo 2011), hypersynchrony dominates late (Jiruska 2013; Kramer 2012), and the most
  direct test finds no pre-seizure supercritical drift (Hagemann 2021). **The route-independent invariant was
  always all the theory needed**, and both artifacts now claim less than either did.
- **Pattern #37's paper formulation changed on a red-team objection MG accepted.** The bare blind-spot
  version overshoots: an event with no represented cause should present as *arbitrary*, not as *free*. And it
  could not answer the cheapest objection — most causes go unrepresented without feeling uncaused. The repair
  routes through the self: unrepresented causes normally get an in-scene **stand-in** (hunger → an empty
  stomach), a decision is assigned to the **self**, and the regress ends there because what stands behind the
  self-model is the apparatus. ⇒ *"not as uncaused but as **originating** in the self."* The spoken form stays
  book-usable; the paper form is superseded.
- **A gate that is red for structural reasons is a gate nobody reads.** The FMT master entered
  `verify_references.py`'s corpus for the first time (`AIW-204`) and returned 65 needs-review out of 229 —
  **none of which is a bad reference.** They are Crossref fuzz against books, chapters, blog posts and MG's
  own 2015 monograph, which it does not index. The lesson generalises beyond this gate and was earned twice
  in one session: the Tier-4 PDF suite had been **skipping** six of eleven tests against a dead path,
  reporting green while verifying nothing. **Checks fail silently by passing.**
- **Verify a member against the built artifact before working it, not only against the backlog.** Three items
  this session were defects in the tracker rather than the artifact: v15 member (a) was already shipped,
  the Tier-4 gate was silently skipping, and `AIW-179`'s "which file is authoritative" had a mechanical
  answer nobody had run. S299 named the defect class as *a correction that reaches the tracker and never the
  artifact*; **the inverse is just as common and costs a session's work.**


## S298 addendum (2026-08-09, post-rotation) — the connectome study was risk-aversion dressed as strategy

- **MG killed the generality study on the right grounds, and they were not the ones the session was
  worrying about.** The session proposed running crucible's structural instruments on a real human connectome
  to discharge A#7's *"scoped to this connectome family"* caveat, and spent the evening on whether the data
  was directed enough and the instrument robust enough. MG: *"which is a stupid experiment knowing the
  outcome anyways."* **He is right — it is a confirmation that cannot fail.** We already know cortex is
  massively recurrent; crucible measured one giant closed component on synthetic connectomes and the
  feasibility check measured one on the real one. The number would surprise nobody. **This is crucible's own
  pattern 39 applied to a study aIware proposed**, and the session walked into it because *cheap, safe,
  upgrades a banked row* reads like good judgement. It was risk-aversion, and it displaced the question MG
  had actually asked.

- **The reason for a human-like connectome is FUNCTIONAL, and the session kept substituting a structural
  one.** MG: *"human shape / macaque is more interesting because we have dedicated language centers we can
  connect to or replace by an llm"*, and then, flatly: *"thats really not the reason i want a human similar
  brain."* Even after conceding the point once, the session's closing note re-framed fly as *"the
  instrument-validation step on the way"* — quietly keeping the dead study alive as stage one. **Fly has no
  homology and no language periphery; it is not a step toward anything MG wants.** The target is a substrate
  whose language centres an LLM can be wired into or substituted for, which makes FMT's claims about the
  explicit layer testable. Same programme as crucible's CRU-37 Horizon C and the taught-vs-spontaneous `"I"`
  reframe in `AIW-193`(g) — three threads that were not visible as one while the structural result was being
  chased.

- **What the feasibility check is still worth, stripped of the study it was for.** Three durable facts:
  **F-TRACT** is a real, free, directed human connectome (613 patients) but covers **cortex, hippocampus and
  amygdala only** — no thalamus, striatum, brainstem or cerebellum, which constrains any loop claim built on
  it. **Crucible's `min_prevention_set` is exhaustive over subsets** and cannot run on any real connectome;
  it needs the standard ordering formulation before it produces a number on anything but a toy. And **no code
  in crucible constructs the condensation graph its prose describes**, which matters because A#7's
  upper-bound argument is headed for v15. All three routed to crucible.

- **Relaying is not understanding — twice in one night, from one cause.** The agent's vocabulary reached MG
  untranslated, and its *framing* reached him unchecked: "the real brain shows the same structure" was
  relayed as the finding that ended the study, when it is mildly good news and the actual blocker was the
  algorithm. **This is the same failure this session had already written up hours earlier** about inbox items
  — *a summary that points at its source may not contain it, and the pointer reads like the content.* Writing
  the pattern down did not prevent committing it.

## S298 (2026-08-09) — `AIW-191` fires: the prioritization output is a queue discipline, not a cut list

- **MG rejected parking anything, and that is the substantive ruling of the pass.** The proposal put the
  cosmology theory cluster (`AIW-186`/`AIW-187`/`AIW-166`), cosmology build hygiene (`AIW-179`/`AIW-180`),
  the ~15 older crucible inbox items, and the P2/P3 theory-intake tail into a *deprioritized-until-after-v15*
  tier. MG overruled all four: *"don't park until then, use as gap filler during gpu wait just like today, it
  will happen frequently while cru is at the height of its compute consumption"*, and on the tail *"not after
  Copenhagen, perfect gap fillers with chance of golden needle"*. **⇒ FMT-master work has right of way and is
  what a session opens with; everything else fills the gaps while crucible's GPU jobs run.** Nothing is
  parked, nothing is deferred past Copenhagen. The reasoning is a resource observation the proposal missed:
  crucible is entering its heaviest compute phase, so aIware sessions will *frequently* be waiting on a job
  that aIware must not contend with — and that wait is capacity, not downtime.

- **The old crucible inbox cluster is reclassified from chore to search.** It was proposed as
  "triage by signature, mark done with a pointer — not new work." MG: *"good background work for fable just to
  make sure we dont overlook a gold needle in the haystack."* The point is not to close items, it is to find
  the one that should not be closed. Runs as a Fable background pass with the two live traps stated in
  advance so it cannot resurrect the withdrawn spectral claim or the dead necessity framing.

- **v15 had no tracking home, and that is the structural cause of the S296–S297 imbalance.** v13 was bundled
  under `AIW-121`, v14 under `AIW-138`; the artifact MG named top priority and targeted just before Copenhagen
  had no epic at all. Items with a container get worked; a deadline without a container does not. `AIW-193`
  created. This is the generalizable lesson: **a priority without a bundling item loses to any cluster that
  has one**, regardless of what the ranking says.

- **The golden-needle sweep found a bias, not just needles, and the bias is the durable finding.**
  MG's instinct that the old crucible inbox cluster was worth a Fable pass rather than a triage chore was
  right: 17 items, 6 genuinely missing and valuable. But the *pattern* across them is what matters.
  **Everything crucible's experiments forced was absorbed** — the stationary-closure theorem, the nulls, the
  two-closures distinction, capability-first instrumentation, the gridworld GO — each traceable to a paper
  section. **All four MG-authored theory threads in the cluster were absent**: the model-space repertoire
  framing (line 102), the taught-vs-spontaneous "I" reframe (114), the freeness gradient (327/100), and the
  sufficiency-not-localization two-tier rule (386). ⇒ **What gets absorbed is what an experiment pushes;
  what gets missed is what MG said in conversation.** An experimental result arrives with a result file, a
  ledger row and a paper-placement audit column chasing it; a theory ruling stated in a design conversation
  arrives as one clause inside a long inbox item and has nothing chasing it. This is a routing defect, not
  an attention defect, and it is why the sweep was worth running rather than closing by signature.

- **The most expensive instance: the master paper shipped v13 and v14 with a gate MG had retired.**
  §3.4.3 line 338 still names *spontaneous* first-person report as the strongest available evidence that
  closure yields experience. MG split the referent from the label on 2026-07-08 — *"'I' is TAUGHT, not
  spontaneous"*, feral children have selves without "I" — and the correction sat in an unprocessed inbox
  item for a month while two versions of the paper went out over it. Verified by hand on both sides before
  entry into `AIW-193`(g): the gate is in the shipped master verbatim, and the reframe is in inbox line 114
  as MG-directed. **The lesson for the queue discipline: an inbox item that corrects a claim already in a
  published paper is not P2 background work**, whatever its inbox tag says.

- **The book/marketing inbox items are transferred, not deprioritized.** MG: *"clean up/transfer
  accordingly."* Most were written before the 2026-07-31 book extraction to `~/simbook` (`AIW-125`/`CFG-478`)
  and now belong to simbook or infrastructure. aIware verifies ownership and routes; it does **not** re-import
  book work.

## S291 (2026-08-07) — the RIM Fable pass lands; the Cosmic Compiler is not cited; two fabricated citations found

- **MG's two scope rulings on the RIM revision.** §6.3 (grading) is **calibrated, not cut** — the argument
  and its structure survive; what goes is the absolute causal language and the borrowed support. The
  consciousness dependency is **demoted to a boundary condition**: FMT stays in the paper as the author's
  named candidate answer to "what supplies the capacity to construct and run a model of what is not present,"
  explicitly separable, flagged at each point of use, and required by nothing in Sections 6 or 7. Both were
  the session's recommendation and both were taken. The rationale for the second is not that FMT is doubted —
  it is that a theory of intelligence resting on the author's own untested framework is refutable by a
  reviewer who simply declines the framework, which costs the paper its independent claims for free.

- **The prior-art passage does NOT claim the multiplicative formalization as RIM's differentiator, contrary
  to the standing draft.** `drafts/rim-priorart-citations-verification.md` records RIM's differentiator as
  "the multiplicative recursive formalization K × P × M plus falsifiable predictions." The first half cannot
  be claimed: §7.4 states that formalization is deferred to a later paper, so asserting a formalism the paper
  does not have is exactly the overreach Fable's review identified. As written, the differentiators are
  **scope** (intelligence theory and measurement, not agent architecture) and **the measurement programme
  with stated falsifiers**. The draft's framing note is superseded on this point.

- **`AIW-133` — the Cosmic Compiler is compared and NOT cited.** Schoff's *The Cosmic Compiler* (4 pp,
  self-published, no journal, no DOI) argues that the Null State is self-undermining because the rule
  "nothing may exist" is itself a constraint, hence C_null > 0, hence existence is necessary. **The
  convergence is real but narrow**, and it is with SB-HC4A's Axiom 1 only. Against citing it, four reasons:
  (i) the load-bearing step conflates the *description* of nothingness being non-empty with the described
  *state* containing a constraint, and the paper does not address that objection; (ii) its Axiom II makes
  free will a "load-bearing thermodynamic law" that prevents the void — which presupposes conscious agents
  in order to prove that existence is necessary, and is circular for the stated purpose; (iii) Axioms I–III
  argue that the universe cannot *revert* to nothingness, which is a different claim from why there is
  something rather than nothing, and the paper slides between them; (iv) provenance is grey literature whose
  reference list is substantially the author's own unpublished program. SB-HC4A already asserts A1 and does
  not need a weaker external statement of it. **Verdict: comparison done, no citation, item closable.**
  Left open for MG: §10.1 currently *asserts* A1 without argument, and a one-sentence acknowledgment that A1
  is arguable rather than axiomatic would be honest — but that is a change to the necessity argument and was
  not requested, so it was not made.

- **Two citations in RIM were wrong in ways no reviewer would have missed.** The Hilger reference carried a
  2017 paper's title under a 2020 year with a **fabricated volume and article number** (*Sci Rep* 10, 18187;
  the real entry is 7, 16088), and the claim built on it — intelligence as dynamic network reconfiguration —
  is the **inverse** of what that literature reports (Hilger et al. 2020 find greater temporal *stability*;
  Schultz & Cole 2016 find *less* task-related reconfiguration). Jussim & Harber (2005) was cited as support
  for compounding expectancy damage when its actual conclusion is that such effects are small, do **not**
  accumulate, and largely reflect *accurate* teacher expectations. Neither was caught by the citation gate,
  because the gate checks key↔bibitem resolution and et-al labelling, not whether a reference exists or says
  what the sentence claims. **That is a real gap in the test suite, not a one-off.**

## S291 late (2026-08-07) — the passes MG demanded found what he predicted; both papers blocked

- **MG's scepticism about the cosmology paper was the correct call, and the reasoning generalizes.** He
  refused to accept "small diff" as evidence of health: *"i find it hard to believe that this paper on which
  we did the least work is so good that it needs the least changes."* The adversarial pass returned five
  critical errors — the Bekenstein bound misattributed throughout (it is energy × radius, not area, and
  "Bekenstein saturation" is load-bearing for the unification), IB1 contradicting both §8.2 and Raju (2022)
  which the paper cites in its own support, a self-refuting §5.6 state count, a no-hair conflict, and a
  heat-death mechanism wrong by twelve orders — plus five defective references and silence on DESI DR2 and
  Tolman. **The durable lesson is the one now written into `publication-build.md`: a diff's size measures
  the scope it was drawn from, never the artifact's health.**

- **An agent's finding is a hypothesis until independently checked, including when it is bad news that
  flatters the sceptic.** Four of the passes' citation claims were re-verified against Crossref/arXiv before
  being acted on; all four held (Gignac→Oberleiter, Huang→Vu, Balboni→Sternberg, Bisio/Tosini→Perinotti).
  The rest remain agent-reported and are marked as such in the defect file. The same discipline caught the
  RIM agent's one real error: it asserted that *the S291 revision introduced* the chimeric citations, when
  all four are present at `28291ed8` and predate the session entirely.

- **The citation defects are a three-session failure, not a one-session one, and that reframes `AIW-170`.**
  Three chimeras and a fabricated quotation sat in RIM through S289, S290 and most of S291 while each
  session verified only the citations it happened to touch. The gate checks that keys resolve to bibitems;
  nothing checks that a bibitem describes a real paper. Closing that is `AIW-170`, and it is a precondition
  for trusting any future "verification debt cleared" claim.

- **`AIW-174` created at P0 on MG's ruling, and the reason is a negative result.** The sweep confirmed that
  **no work connects information causality or Tsirelson's bound to holography or the Bekenstein bound as of
  mid-2026**. SB-HC4A §6.5 has already publicly staked that route as its stated open obligation without
  anyone else working it. MG: *"yes P0 next session together with 172."* Ordering constraint recorded: the
  derivation needs the Bekenstein bound stated correctly, so the `AIW-172` repair comes first.

- **The prose guard moved out of auto-memory (`lrn`, MG-approved).** It failed at S270, S276 and S291 because
  memory is *recalled*, not *loaded* — its text was never in context while prose was being written. Now
  `.claude/knowledge/prose-register.md` with a CLAUDE.md trigger row, and the sweep is step 4 of a numbered
  workflow rather than a standalone reminder competing with the main task. A grep-based checker was
  explicitly **rejected** as the guard: the file itself records that the Fable pipeline's own grep check
  missed this class in S276, so a phrase list would be a static test standing in for a behavioural one.

## S288 (2026-08-06) — the MoC7 work order, five chart decisions, and what stays open

- **The poster is deliberately finished LAST, and that is a content decision rather than a scheduling one.**
  MG: *"it is already close to production quality and good BUT we might discover a few gemstones in cru before
  october i want in."* The reclaimed-space question `AIW-137` opened stays open on purpose — it is the slot
  crucible's August–September results go into. Freezing the poster early would spend that slot on the
  five-principles block and leave nothing to receive a late result.

- **Web deployment of the chart is infrastructure's job, not aIware's.** MG: *"B infra."* The split is
  content vs deployment: aIware owns the chart, the method and the citation audit of the marks; the
  `fmt.matthiasgruber.com` restructure is executed by the infrastructure project and routed by inbox once the
  audit is clean. This also removes the objection that `AIW-27` was competing with paper work for the same
  hands — it never needed aIware's hands for the deployment half.

- **Bildstein is unpinned, so the charter stops gating and starts following.** Three live windows (a week after
  Erik's birthday / winter / next year) and low priority now. The consequence worth stating: a charter that
  points at a *live* chart is a much easier thing to send than one pointing at a draft, so the loss of the
  dated gate actually improves the artifact.

- **Five chart decisions settled on the session's recommendation; three explicitly reserved.**
  Wired/Running adopted as a **translation layer** (the paper and the eight book editions keep
  implicit/explicit, so the decision costs no reprint and is reversible). Agreement marks adopted — the
  instrument that makes consensus a reading operation. *Interpretation*/*Bedeutung* split kept **alongside**
  the coordinate-transform formulation, because they describe the same thing at two altitudes rather than
  competing. Chart scope = consciousness only for v1, RIM as a declared adjacent chart, on constraint D1's
  ~40-cell cap. The residue keeps the name **Presence Term**, because every alternate prejudges what the
  exclusion ledger declines to assert. Full reasoning: `docs/smoc-middle-layer-draft.md` §7.

- **A finding that came out of settling the register names.** *Bewusstsein* (capacity) vs *Bewusstheit*
  (ongoing interaction) is **orthogonal** to Wired/Running, not a candidate for it: the German pair separates
  system-level capacity from occurrent state, while Wired/Running separates two kinds of model that coexist in
  one waking system. Naming the registers after the German pair would have collapsed two axes. The pair is
  recorded against the **ladder** instead — which rung you *have* versus what is *running now*.

- **MoC7 discussion vote: buy probability-of-winning (A2), carry A1 into the corridor.** The two axes are *value
  if it runs* and *probability it wins*. A1 ("what is the contribution of consciousness to human intelligence,
  and **how**") is the higher-value question precisely because most of the field has no mechanism to offer —
  which is also why a room of rivals is least likely to vote for it, and why it carries some risk of reading as
  a trap. A2 ("what structural criterion distinguishes conscious from non-conscious computation") is
  answerable by every camp, produces the taxonomy a consensus paper actually needs, and maps onto the chart's
  R4 boundary without naming FMT. The asymmetry that decides it: **the collective paper is the prize, and a
  question that does not win produces nothing at all**, whereas A1 loses almost none of its value when asked
  face-to-face in a corridor. A5 is used as A2's framing sentence rather than as a competing proposal.

- **A1 is submitted as well, if the organisers allow more than one — MG's correction, and it was right.**
  MG: *"a1 shouldnt split much votes if the odds are low."* The vote-splitting objection only bites when voters
  would otherwise have chosen A2, and a low-odds question by construction diverts few of them; the session had
  bundled that arithmetic together with a separate and much smaller cost — the perception of one unaffiliated
  name pushing two substantive items. **And it missed an upside outright: an unvoted proposal is still read by
  every registered participant on the board**, so submitting A1 buys exposure for the strongest thing FMT has
  to say *in the losing case*, which is the case we expect. Operational split: **campaign for A2 in
  conversation, let A1 stand on the board.** If proposals are capped at one, A2 is the one.

- **The No-Free-Lunch correction had been over-applied, and MG stopped it — this is a theory ruling, not a
  wording preference.** MG: *"no free lunch is about ML not about human intelligence… human intelligence
  includes social and emotional intelligence and other stuff that is consciousness altogether (not the closure)
  IS a capability that lifts intelligence from insect to mammal level."* The unrolling result is a claim **in
  function space, at unbounded budget, about an episode-stationary task**. Three of its own preconditions fail
  for biological intelligence: **budget** (the unrolled equivalent must be built inside a genome, a lifetime and
  a metabolic ceiling — where the unroll is exponential in horizon, no organism instantiates it, so a gap
  unbounded in the limit *is* a capability boundary for every real system); **stationarity** (open-ended
  cognition is precisely the non-stationary case the stationary-closure theorem excludes — novelty outruns the
  amortizer); and **referent** (ML "intelligence" is I/O competence on a task distribution, the *g*-loaded
  sense — and `AIW-132`'s psychometrics say that is not what human intelligence is, since specific abilities
  carry 30–57 % of *g*'s predictive weight and social/emotional intelligence, which *is* redeployment, is where
  the payoff sits). **The quantifier that reconciles both claims:** false that ∃ capability no feedforward+memory
  system realizes; true that ∃ capability and ∃ budget *B* such that none realizes it within *B* while a closed
  system does — and biology never leaves *B*. **The subject of the capability claim is consciousness as a whole
  architecture, not closure as a primitive** — MG's explicit distinction. Operational split now recorded in
  `.claude/knowledge/didactic-patterns.md`: **efficiency-only in the in-silico/formal lane; budget-relative
  capability in the biological lane.** Stating the biological case as mere efficiency is weaker than the
  evidence supports and invites *"so it's just an optimization."* **Paper status: v14 is not wrong** — §8.9
  already predicts a small advantage on simple individual tasks and a steeply growing one on social and
  compositionally complex tasks — **but it is under-stated, and sharpening it is a v15 item.**

- **The three reserved chart decisions, settled the same session.** **R4 is the *consciousness* floor (core/
  basic — the subject), not the sentience floor**, and sentience becomes a `disputed` **band spanning R2–R4**
  that the chart declines to place. R4 is the only rung that is both FMT-only and untestable (blank B1), which
  makes it the worst carrier for the field's most ethically loaded line; and Damasio maps onto consciousness
  (core ≈ R4, extended ≈ R7), not sentience. The refusal is itself the finding — *the field cannot agree whether
  feeling requires a self-model*, and nobody had stated that as a coordinate.

- **The depth axis: the chart declares it, FMT fills it — MG's move, and better than either option offered.**
  MG: *"depth WILL become measurable… it is also a win for fmt if we can say the SMoC expects these dimensions,
  FMT has discovered an additional granularity."* R6 becomes a **graduated rung** — a depth axis with **blank**
  increments, because no theory in the field resolves depth — and FMT supplies *einfach/doppelt/dreifach
  erweitert* as **FMT-only** sub-increments. Identification is promoted to its own rung (R7); language-coupled
  shifts to R8. **This inverts the objection it answers:** FMT-only marks sitting on a *field-blank* axis read as
  contribution rather than advocacy, which is exactly what the marking discipline exists to make visible. It is
  the Mendeleev structure (D3: gaps are the research programme), it satisfies D5 since a rival may take the axis
  and decline the filling, and it survives depth becoming measurable at zero restructuring cost — the marks just
  migrate FMT-only → converging → agreed. **That makes this the chart's own demonstration case for its
  convergence metric.** Renumbering was free: the R-ladder is referenced only inside the draft.

- **Truth: keep p.24's absolute falsity AND p.32's renunciation of absolute truth; drop only the "Konvention von
  Wahrheit" sentence.** MG's principle: ***absolute falsehood doesn't require absolute truth to exist.*** So the
  conflict was never p.24-vs-p.32 but p.24 vs **one sentence** of p.32. MG's mechanism: the flat claim was
  itself a *geometric* claim, so geometry's own new observations refuted it **framework-internally**; the
  positive replacement (*roughly a ball*) is society's revisable filling and may be subsumed (a 3D ball
  sub-object of a 6D cube) — but the subsumption does not restore flat.
  **MG's second correction, and it matters: the asymmetry is a GRADIENT.** *"When the deciding population
  changes, both falsehoods and truths can change, but falsehoods are more resistant."* The strong form drafted
  first — refutations *survive* framework change — is historically false (continental drift, *H. pylori*,
  epigenetic inheritance). **The mechanism behind the gradient:** a refutation is pinned to one specific observed
  contradiction (narrow, costly to overturn), while a positive claim is underdetermined by the same observations
  and displaced by any better-fitting rival (wide, cheap). Degree, not kind — and the historical counterexamples
  become *explained*, since they are exactly the cases where the refuting observation was weak or misapplied.
  **Two senses of "absolute" kept apart:** semantically, falsity is not a consensus property (the anti-p.32
  point); epistemically, verdicts on both remain revisable.
  **The real defect is narrower than a contradiction:** one word, *Wahrheitsgehalt*, for two relations — the
  sharp negative (falsity) and the graded social (agreement across reference systems). The consensus measure has
  work only in the positive direction; hence the rename to **Konsensgrad / degree of corroboration**.
  **Two further mechanisms, both MG's and both independent of the evidential one.** *Social:* new truths and
  truth→falsehood conversions both ride on positive evidence and are cheap; a **societal** falsehood has already
  accumulated reasons, textbooks, curricula and reputations supporting the logic of its falsity, so the backward
  step must dismantle an invested apparatus — a **ratchet**. *Compounding:* the falsehood state is a
  *post-reversal* state, so returning is *"a second conversion of already 180° changed knowledge"*, and the
  expenditure that bought the first turn is what resists the second.
  **⇒ The checkable prediction, and the strongest part of the whole argument: resistance scales with the cost of
  the original conversion.** Expensively won falsehoods (flat earth) are near-irreversible; cheaply established
  ones return — *continental drift* was rejected for want of a mechanism, *H. pylori* on a background assumption
  about stomach acid. **The account predicts which falsehoods come back**, which neither a permanence claim nor
  a bare gradient could. There is also an **FMT reading**: a lived-with falsity ruling has been *consolidated*
  into the wired/implicit layer (pattern #14) — *"that was debunked"* becomes reflex, not an inspectable claim —
  while the current best positive model is held explicitly and known to be provisional. Societies consolidate
  their negatives more thoroughly than their positives, so the asymmetry is derivable from the architecture as
  well as from the logic of evidence.
  **Routing:** the monograph correction stays internal (`AIW-153`); **the principle publishes on its own**, never
  as a fix — it runs on definitions alone, same shape as the regress argument, and belongs beside it in §3.6.
  **v15 candidate.** **And MG called a blog post the same session** (*"looks like we need a truth blog post
  soon"*) → added as the new lead post under `AIW-122`, with the hard constraint that it publishes the principle
  and never mentions the monograph, *Wahrheitsgehalt*, p.24 or p.32. Self-consistency worth naming: this is the chart's own constraint **D6** — *does not have
  to be right to be useful, has to be revisable* — so SMoC's licence to publish and FMT's theory of truth are
  one principle stated twice.

- **A sixth mark — `not applicable` — and a new design constraint D9. MG: *"any coordinate system should be
  checked if N/A is applicable to it."*** The chart had five marks and no way to say *this axis does not measure
  this entry*. That is not a cosmetic gap: **blanks are the chart's predictions** (D3, Mendeleev's gallium), so
  a blank that is really an N/A is a **false research prediction** — it sends the field hunting for an answer to
  a question with no well-formed version. A midpoint value is the usual tell, because a midpoint is often a
  hedge standing in for "this does not parse here." **D9 makes the check mandatory before any axis ships.**
  First application: panpsychism on the substrate axis — if experience is fundamental to matter, "how much does
  the substrate constrain" is ill-posed, and the figure now draws it as a dashed band at its determinate x
  rather than scoring the other coordinate. The general form is the valuable part: *a coordinate system that
  states where it stops is more credible than one that scores everything.*

- **The argument map was redesigned to MG's brief** — blue (`#2a78d6`, the validated data-viz slot, not a picked
  hex) replacing the red accent, 3px rounded rules, bigger marks, warm off-white ground with the plot as a white
  card, and margins/leading opened throughout. MG's reason is worth keeping: *"design matters. the design is
  among the very few things that can bring simplicity into such a topic."* Accent↔neutral separation validated
  at ΔE 21.3 deutan / 18.9 tritan, both ≥3:1 on the surface.

- **`AIW-141`: neither crucible finding becomes a standalone paper.** (a) The homeostasis result is a
  methods section of the companion, not a note — one configuration, one seed, one probe amplitude is not
  standalone-grade, and its publishable core is a *diagnostic signature* which belongs next to the method it
  diagnoses. (b) "Select on function, test the unselected consequence" is the one with independent reach and
  is the better standalone, but as a **short methods/position piece**, since its value is a firewall other
  people can adopt rather than a result.

## S287 (2026-08-06) — FMT v14 shipped early; the paper stops talking about itself

- **Early v14 over a late one, MG's call after weighing "either a late v14 or an early v14 and a last minute
  before moc7 v15".** The deciding asymmetry is the poster QR: it resolves to the Zenodo *concept* DOI, which
  always serves the newest version, so every week v14 sat unpublished was a week the MoC7 board would have shown
  a paper contradicting the poster in a room holding two NoC associate editors. Publishing now made the QR
  correct immediately and turned a v15 in early October from a rescue into an upgrade. **v15 is now the
  accumulating bundle** — crucible results, the remaining `AIW-143` paper-bound items, literature findings.

- **New material was folded into v14 *before* MG's review rather than after.** The review was already pending on
  the S286 phases; adding the three MG-routed S285 results to the same bundle meant one review instead of two.

- **The new architectural component is called "the channel", not "the bottleneck".** §3.4.2 explicitly rejects
  the reading on which phenomenality overflows an *access bottleneck*; reusing that word for a new component
  would have read as reinstating what the paper rejects. §3.6.1 carries a guard paragraph stating the seam:
  **rank sets how much the simulation holds, recursion depth sets whether it can take its own contents as an
  object.** A system can be wide and shallow or narrow and deep.

- **The LLM case is scoped to channel width in the main paper.** "A closed LLM would be richer in breadth" stays
  routed to the JAIC slice; §3.7 uses the case only to show rank varying independently of extent and complexity,
  with the caveat that a context window is not a workspace in the global-broadcast sense.

- **An MG-directed addition was declined on the strength of its own source's later evidence.** MG had directed
  crucible's spiking-substrate plausibility argument into the main paper. Crucible's same-day follow-up showed
  the result is "true and near-vacuous" — leak dominance bounds every eigenvalue's argument, so real-positive
  dominance holds by construction. It was not added. **This is what the `AIW-143` verify-before-acting rule is
  for, and it is the second time in one session that acting on a cross-project claim unverified would have put a
  checkable error in front of reviewers.**

- **The paper's self-referential register is now gated, not policed by eye.** MG rejected it three times in one
  sitting — reader-scolding, a version-history paragraph, then "that whole chapter has to be re-checked". Six
  narrow patterns went into `scripts/test_content_integrity.py` (32 tests) banning version-history narration,
  reader-scolding, "should be read as", self-grading, section self-announcement, and philosophy-of-science
  truism openers. **It immediately caught two instances a careful read-through had missed.** This is the real
  implementation of `AIW-128`, which had been open on the grounds that a per-session recalled memo is not a
  root-cause fix. Pattern routed to cfg-agent-fleet for the writing-project template.

- **`AIW-126` collided across two items; the closed one moved.** RIM keeps 126 because it is open, P1, and dated;
  the closed v14-framing item became `AIW-154`. Renumbering the closed side is cheaper — nothing will act on it
  again.

## S285f (2026-08-05) — The 2015 definitions are canonical; knowledge does not require consciousness

- **MG ruled against his own verbal formulation from earlier the same session.** Asked to reconcile the 2015
  book's *"Wissen ist Information, die einem Bezugssystem zugeordnet ist"* with the day's spoken definition
  (*"a psychosocial construct… pulled very close to his explicit self model and commited to automation and
  removal from consciousness"*), he identified the error himself: it *"mixed up reported knowledge knowledge
  and truth there. the 2015 book stuff should be more correct and consistent."* **The 2015 definitions are
  canonical.**

- **Nothing was lost, because the spoken version was pointing at three real 2015 concepts misattached to the
  base term.** *"Pulled close to the explicit self model"* is **subjektives Wissen** (p.35's converse —
  knowledge built firmly into the inner world-model, as against objective knowledge which is deliberately
  *not*). *"Automation and removal from consciousness"* is **implizites Wissen** and the consolidation
  channel. *"Psychosocial"* and the reporting element are **Glaube** (p.34: knowledge a person *claims* has
  maximal truth-content) and **Wahrheitsgehalt** (agreement between reference systems). All four survive,
  correctly located — the 2015 system had already separated them.

- **What this retracts, and it was load-bearing.** The claim that *knowledge is definitionally
  post-conscious* — written into the SMoC draft §3.1 earlier the same session as the thing that "vindicates
  MG's original line" — is **false and withdrawn**. Under the 2015 definition knowledge requires only a
  **reference system**, so a machine that has one has knowledge, and FMT says so.

- **What replaces it is stronger.** The correction owed to information science is not *"the boundary is a
  consciousness mechanism"* but ***"the boundary is a model."*** DIKW has been criticised for decades for
  having no principled mechanism at either boundary; the 2015 definitions supply both — codeability plus
  reversibility for data→information, assignment to a reference system for information→knowledge. **The field
  could not draw the second boundary because it had no theory of *models*** — it treats a model as an artefact
  one draws rather than as the thing that constitutes the epistemic relation. That is a claim about the
  discipline's ontology rather than its psychology, and it is far harder to wave away than an appeal to
  consciousness.

- **And MG's opening claim resolves cleanly after all.** *"Information and knowledge are words that without the
  existence of consciousness make no sense"* is **false of the referents** (machines have both) and **true of
  the concepts** — they were coined by conscious knowers, and no discipline could define them without a theory
  of modelling systems. Earlier in the session I had raised exactly this ontological-vs-genealogical fork and
  then dismissed it as a false dichotomy; **the fork was right and the dismissal was wrong.** Recorded because
  the failure mode — collapsing a real distinction because a later framing seemed to subsume it — is worth
  not repeating.

- **Where consciousness does enter: not at knowledge, but when the reference system IS a self-model that
  closes on itself.** This keeps the whole epistemic ladder consciousness-free and removes a claim a reviewer
  would rightly have attacked.

- **The strongest result to come out of the extraction is an argument the paper should make.** 2015 p.22 gives
  the recursive form — *"Wissen ist Information, die bereits bestehendem Wissen zugeordnet werden kann"* — so
  knowledge regresses, and terminates only in a layer never assigned by interpretation but grown by plasticity
  and selection. **The implicit/wired models are therefore logically required, not merely empirically
  convenient: without them "knowledge" has no base case.** Runs on definitions alone, survives a reader who
  rejects the neurobiology, and predicts that a system whose entire representational content is assigned at
  runtime cannot bootstrap knowledge.

## S285e (2026-08-05) — Notation doctrine: the periodic table's symbols were a print-and-rote artifact

- **MG rejected the symbol layer outright, and the reason is historical rather than aesthetic.** The first
  draft gave every component a three-letter code (`MSP`, `WST`, `RTN`) in imitation of `Fe` and `μ`. MG:
  *"dont copy the periodic table or the physics stuff, these were done in a time when you could force children
  to learn the shortcuts by hard so they could then carry only the shortcuts, they were still printed then. now
  we need words or something. and also pictograms, seriously."* **Both enabling conditions for terse glyphs are
  gone:** rote schooling installed the symbol→meaning lookup table in every head once, at society's expense,
  and print forced compression into glyphs-plus-legend because a page had no room, no colour and no zoom. The
  draft had copied the surface form while ignoring the machinery that made it work.

- **The replacement is a different KIND of mark, not a different symbol set.** An arbitrary symbol's form
  carries zero information, so the mapping must be memorised; a **motivated** mark (a self-describing word, a
  pictogram whose form diagrams the operation) is *inferred* at zero instructional cost. *Nobody was ever
  taught the wifi icon* — that is the standard every mark must meet.

- **Motivated marks compose, and that is what makes the result better than the thing it replaces.** `Fe` plus
  `O` does not draw rust. But the wired mark + an arrow + the running mark **is** "becoming conscious"; the
  running-self mark through a waist and back into itself **is** closure; a rung **is** the set of marks a
  system has. So mechanisms are drawn as compositions and rungs as accumulations, and **the chart needs no
  legend at all.** Consequence applied throughout: the three-letter codes are withdrawn, and the agreement
  letters (`U/C/D/O/F`) became words — MG asked "what is a status-tag spine????", which was itself the proof
  that an invented shorthand fails the doctrine it was written to serve.

- **Two naming wins fell out of it.** `implicit/explicit` become **wired/running** on the chart's face (FMT's
  IWM/ISM/EWM/ESM stay as the technical alias), and that hands over the ML bridge in one line an engineer
  already knows: **wired = weights** (what plasticity changes), **running = activations** (what anaesthesia
  stops). Also `Regulator → Governor` and `Consolidator → Scribe`, both picture-words for the same operations.

- **A capability print never had, now a design rule: one artifact, several depths.** The periodic table had to
  choose a single compression level. A screen-native chart can be read at a glance (four registers, the
  ladder), at working level (components, mechanisms, marks) and at audit level (every cell with its agreement
  mark and citation) — so the chart can *be* the bridge between the technical and public layers rather than a
  fixed station between them. That answers the missing-landing problem more completely than a static chart.

- **Design finding from building it: accumulation by superposition fails past about three marks.** Overlaying
  mesh + wave + nest + return in one 88 px cell produced grey mush at every tint. The fix was to stop drawing
  the ladder as superposition and draw it as a **matrix — rows are rungs, columns are marks** — which is both
  legible and, unplanned, the genuinely periodic-table-shaped object: the same grid then does **placement**,
  and a human's row beside an LLM's row beside a feedforward net's row is the most quotable artifact the
  project has produced. Record: `figures/smoc-marks.svg`, built by `scripts/build_smoc_marks.py`.

## S285d.1 (2026-08-05) — Data / information / knowledge: MG's carve, and why it vindicates his own claim

- **MG supplied the three definitions and they replaced a four-level draft of mine that put the consciousness
  requirement in the wrong place.** Verbatim: *"data is the given. everything is data. information is data that
  is somehow structured, ordered or otherwise relatable/interpretable, so information is data that a code can be
  applied to (which is also information) so information can interact with more information in some
  theoretically reversible way. knowledge is a psychosocial construct, it is information that someone has pulled
  very close to his explicit self model and commited to automation and removal from consciousness."*

- **Information requires no modeller — only codeability, with reversibility as its signature.** That is broader
  than the "difference that makes a difference" tradition my draft used, and it explains why physicists were
  never *wrong* about information: they work entirely in this layer, where reversibility is the whole game. They
  talk past consciousness researchers because they never needed a third level, not because they mislabelled the
  second. The definition is also self-bootstrapping — the code is itself information — which is a feature.

- **Knowledge is definitionally POST-conscious, and that is what vindicates MG's original line.** Knowledge is
  not a competence held *in* consciousness; it is precisely what automation has driven *out* of it. No explicit
  self-model → no closure → no self-indexed consolidation → **no knowledge, only information.** The requirement
  is structural rather than lexical, so **the ontological-versus-genealogical fork I had raised as a decision
  simply dissolves** — it was an artefact of my boundary, not a real choice. Recorded because the instinct to
  present a false dichotomy as a decision is the error worth not repeating.

- **Knowledge is wired, not running — mesh, not wave.** This makes the information ladder a *reading of the
  chart* rather than an extra column bolted on: data → information → knowledge is the **Scribe** mechanism
  (running → wired) plus self-indexing, drawn with marks already on the sheet. Two disciplines, one drawing.

- **The correction to information science is now specific and citable.** DIKW (data → information → knowledge →
  wisdom), taught in every information-systems curriculum, has been criticised for decades for having **no
  principled mechanism at either boundary** (Rowley 2007; Frické 2009). MG's carve supplies both: codeability +
  reversibility for the first, self-model binding + automation for the second. **That the second boundary is a
  consciousness mechanism is exactly why a field without a consciousness model could not draw it** — which is
  the prediction MG made before the boundary was named.

- **A convergence and a derived explanandum arrive free.** The automation clause is the expertise literature
  (Fitts & Posner; Anderson's proceduralization; Dreyfus) — skill acquisition ends in loss of introspective
  access. The chart then *derives* a familiar puzzle: **experts are frequently bad teachers because their
  knowledge is wired rather than running, so it is no longer in a transmissible format** — which ties straight
  to didactic patterns #21/#22, where only content carrying both a first- and third-person format is sayable.

- **Left open for MG:** where *meaning* sits. The natural reading puts it one step before knowledge —
  information bound to the explicit self-model but not yet automated, i.e. "this means something to me right
  now" — making meaning the live phase and knowledge the consolidated phase of one process. Elegant, but not
  what MG said, so it is not in the chart.

## S285d (2026-08-05) — The project's ultimate goal, named: supply the field its missing middle layer

- **MG named the goal of the whole exercise, and it is not "get FMT accepted."** It is to supply consciousness
  science with the **medium-complexity middle layer** it does not have — the periodic-table / particle-chart
  equivalent — and then to *reverse-engineer* from it the road to a standard model and a large scientific
  consensus, and later *forward-engineer*: fill the models, grow the agreed area, and systematically find and
  organise the open questions. Recorded as the project's top-line framing because it reorders everything
  downstream. First draft: `docs/smoc-middle-layer-draft.md` (AIW-146).

- **The diagnosis is a structural gap, not a communication problem.** Every mature science has three layers:
  public, middle, technical. Chemistry has the periodic table between QM and "water is H₂O"; physics has the
  particle chart; biology has the central dogma. **Consciousness has layers 0 and 2 and nothing between them** —
  MG's own words: *"you either read the horoscope, or you have to jump right into deep medical and philosophical
  shit like you see nowhere else almost."* The missing layer is why a neurologist, an ML engineer, a
  psychiatrist and a phenomenologist cannot tell whether they disagree or are merely using different words.
  **A middle layer is a coordinate system, not a simplification** — a professional chemist uses the same chart
  as a fourteen-year-old.

- **This reframes why five desk rejections happened, and what to do instead.** FMT was submitted as a rival
  theory competing for the same slot as IIT and GNWT, which is the most crowded and most credential-gated
  position in the field. **Authoring the field's coordinate system is a different and weaker-defended
  position** — scaffolding is judged on utility rather than on affiliation, and it can be proposed by an
  unaffiliated author. The chart is explicitly *not* FMT: FMT is one filling of it, and rival fillings must be
  possible or the chart is a manifesto. Every cell carries a status tag (uncontested / converged / disputed /
  open / **FMT-specific**), and the F tags are published deliberately — volunteering the exposed surface is
  what distinguishes infrastructure from doctrine.

- **The status tag turns consensus from persuasion into a reading operation, and yields the field's first
  progress metric.** Read the U and C cells → the consensus core, which nobody has written because there was
  nothing to read it off. Read D → the negotiation agenda. Read O → the research programme. Cells move
  O → D → C → U as the field advances, which makes "is consciousness science converging?" measurable for the
  first time. **That instrument is a larger contribution than any single filling of the chart**, and it is the
  strongest available framing for the MoC7 collective consensus paper.

- **Two design rules worth keeping beyond this draft.** (1) *The Bohr-atom licence*: Mendeleev got eight atomic
  weights wrong and did not know protons existed; the Bohr atom is wrong and was indispensable. **A middle
  layer does not have to be right to be useful — it has to be organised, falsifiable and revisable.** That is
  the licence to publish now and the standing answer to "you are oversimplifying." (2) *The pre-2005 test*,
  promoted from MG's buildability argument: FMT is constructible from what was known in 2005, so any chart cell
  that cannot be stated without a post-2005 result is a Layer-0 detail wearing a chart's clothes. It doubles as
  an anti-overfitting criterion — a middle layer that depends on recent data is fitted to it.

- **The sharpest new formal content came from crucible's failures, and it generalises past FMT.** The
  decomposition **closure ⊂ bottleneck** — *the waist buys efficiency (rank ≤ k, cost 2kN vs N²), the return
  buys self-consistency (a fixed point; a relay has none)* — separates the two things the field conflates and
  makes the thalamocortical example exact rather than analogical. Alongside it, three selection rules learned
  the expensive way: closure claims must be efficiency claims (No-Free-Lunch); a regulated variable cannot be
  an independent variable; and you cannot make a recurrent network return-free, only choose which node-sets sit
  in returning components. **A middle layer that hands rival theories three ways to avoid wasting a year is one
  they will adopt.**

## S285c (2026-08-05) — SJÄLV frozen; the booklet toolchain is the durable output

- **MG declared SJÄLV final for print and waived the 7-point red-line review.** Recorded as a decision, not an oversight: he had looked at the artwork himself and was satisfied, and the review's cost was another round-trip against a deadline he is comfortably ahead of. **What it leaves standing is an exposure, not a defect** — red line #1 (does the parts page read as four snap-together modules?) and every drawn number except the cover's 45 and 22000 are *unverified rather than verified*. The distinction is written into `docs/pending-sjalv-manual.md` so a future reader cannot mistake a waiver for a pass.

- **A software simulation of a physical fold verifies nothing.** The first imposition shipped with a checker that reconstructed the folded booklet from the imposed sheets and passed. It passed because it inverted the same model the imposition was built from. A real print found the error in minutes: pages 8, 10 and 12 upside down, because **the two faces of one half-leaf need opposite rotations** — flipping a leaf about a top spine turns it through 180°. **The general form: a verifier derived from the artefact's own model tests self-consistency, never correctness.** When the ground truth is physical, one physical trial beats any amount of simulation, and the honest move at build time is to say so rather than report a green check.

- **The cheap option and the authentic option coincided, and the eco assumption was backwards.** Live quotes: uncoated 90 g Offset/Naturpapier — the correct IKEA stock — costs about two cents a copy more than the cheapest paper in the shop, while **recycled paper is the most expensive of the four options**, not the cheapest. Worth remembering the next time a paper choice is made by intuition.

- **Two build targets, not one, and they are not interchangeable.** The A4 duplex imposition is for a home laser printer and must never be sent to a print shop, which runs its own imposition and wants twelve single A5 pages with bleed. Both are emitted by `drafts/sjalv-print/build_booklet.py`; the reasoning lives in `.claude/knowledge/sjalv-booklet-build.md` so the distinction survives the session that learned it.

## S285b (2026-08-04) — 222 DPI ruled sufficient; Bach replies and raises J-space

- **MG closed the print-resolution question by changing the spec, not the file.** The handout is *"a conference fun handout to be printed on the cheapest paper i can find"*, so 222 DPI is fine and the blocker raised earlier the same session is void. **The lesson is about whose call it was:** the resolution finding was correct as a fact and wrong as a blocker, because the quality bar belongs to the person who decided what the object is for. Print sourcing filed as `AIW-144` (P1) — and the cheap option and the authentic option turn out to be the same one, uncoated 80–100 gsm rather than the coated gloss print shops quote by default.

- **Joscha Bach replied (2026-08-04) and the reply is a lane, not a courtesy.** He suggested Models of Consciousness, Cognitive Science and ICCS as venues — MoC7 is already accepted, which is worth telling him. He raised two substantive threads: motivation as prewired mechanisms for finding one's place in larger systems of agency, transcended by conditional behaviour as world-modelling improves (his convergence with RIM's K×P×M); and whether the J-space capacity limit in LLMs is inherited from imitating human cognition or is a mathematical constraint on implementing intelligence at all.

- **The J-space result is evidence FOR FMT's architecture and the draft reply did not use it.** Anthropic's ablation shows that removing J-space contents leaves fluency and simple factual recall intact while multi-step reasoning collapses to near zero — the implicit layer surviving while the explicit layer fails, which is the IWM/ISM vs EWM/ESM split as a measured dissociation. Anthropic further notes Claude's workspace has **no recurrent loops**. In FMT terms J-space is broadcast without closure: a self-*monitor*, not a self-*model* — SJÄLV's step 7 without step 8. That is the strongest thing to say to Bach and it is stronger than calling the result an artifact.

- **A live contradiction to watch in outgoing correspondence.** The draft tells Bach that recurrent networks *cannot* be unrolled without qualitative loss for certain spiking classes. Didactic pattern #18 / SJÄLV red line #2 retired exactly that shape of claim: a finite closed loop unrolled over a finite horizon is feed-forward plus memory, so the defensible claim is **efficiency**, never capability. The point survives if it is framed as cost — the unroll depth needed for critical spiking dynamics explodes with horizon — but as stated it contradicts the project's own settled position in a letter to a reader sharp enough to notice.

## S285 (2026-08-04) — SJÄLV artwork: hand-authored vector rejected; use a vectorizer

- **MG's verdict on a from-scratch vector rebuild of page 09: "unusable."** The session hand-authored the whole page as SVG — a stroke ladder, Catmull-Rom centrelines with generated tapers for limbs and tails, and the three figures (HAL, Mecha-Godzilla, the Terminator) built as silhouette masses plus interior detail, over six rendered-and-inspected iterations. It reproduced the layout and typography and the Terminator read correctly, but **it does not reach the reference's quality, and MG will not ship a downgrade.** Recorded because the instinct to try again is exactly what should not happen.

- **The chosen route instead: a standard vectorizer, or resize-and-sharpen.** MG: *"ill use a normal vectorizer instead or just resize and sharpen a bit."* The existing artwork is good — its problem is raster fidelity, not drawing. **The general lesson: when the artwork is already right, the job is a fidelity conversion, not a re-authoring. Redrawing throws away the thing that was working.** Reserve from-scratch authoring for pages whose *composition* is broken (page 07, whose panels are copy-pasted at three different scales — a vectorizer cannot fix that).

- **The one finding that survives the rejection, and it is a print blocker: every source page is 1664×928.** At A5 booklet width, 300 DPI wants ~1750 px across, so the sources are **below print resolution before any layout happens**. Whatever tool does the conversion, this has to be resolved before the MoC7 print run — either genuine vectorization, a higher-resolution regeneration from the image model, or a smaller printed panel. Resize-and-sharpen raises pixel count without raising information, so it does not on its own clear the bar.

- **No tooling on WSL for the chosen route.** There is no `potrace`, `inkscape`, `autotrace` or ImageMagick on this box — only `cairosvg` and PIL. Whoever picks this up needs to install a tracer first, or do it on Windows.

## S284 (2026-08-04) — A month of inbox items was invisible; the paper's title outlived its claim

- **The cross-project inbox lost 30 items silently, and the mechanism is worth naming.** The SessionStart extractor matches project tags **case-sensitively**, so everything written `**aiware**` instead of `**aIware**` was never surfaced — 30 items, oldest 2026-07-07, several P1. aIware saw 21 of 51 and had no signal the rest existed: nothing warns, the count simply comes back short. The window is the damaging part — those items accumulated *while* FMT v13 and the companion paper were being finalized and published on Jul 26, so the sessions doing that work were reasoning from two-thirds of their inbox. **The general lesson: a delivery channel that fails silently is worse than one that fails loudly, and "the inbox looked short" is not a signal anyone can act on.** Mitigated by normalizing the tags; the real fix (case-insensitive match plus a warning when a tag matches no registered project *under any casing*) is filed P1 to cfg-agent-fleet. One of the hidden items was a category-error correction to the entire closure method.

- **Verify before assuming damage.** The instinct on discovering a month of missed corrections is to assume the published artifacts are contaminated. They are not: every retracted crucible number was checked against `drafts/companion-computational-paper-draft.md` and FMT master §8.9, and none reached print — §8.9 even correctly omits the withdrawn evidence-ledger row. Reporting "no erratum-grade error exists" was only possible because the check was run rather than the alarm forwarded.

- **The companion paper's title carries a claim the theory has since retired — and MG chose to let it stand.** v1 is *"Closure and Criticality as **Enabling Conditions** for World-Modeling."* No-Free-Lunch (2026-08-01) makes an enabling-condition claim untenable: a finite closed loop unrolled over a finite horizon *is* feed-forward plus memory, so any I/O capability is feed-forward-approximable, and the honest claim is a sample-efficiency advantage inside a fit window. **MG ruled DEFER: "defer until more results, nobody is reading it yet."** The reasoning is sound and worth recording as a pattern — **a correction to a published artifact nobody is reading is not urgent; it rides along with the next substantive revision rather than spending a DOI on a title-only bump.** The corrected language still governs every *new* piece of writing; what was deferred is the artifact, not the framing.

- **Peer catalogs are split by function, not merged by convenience.** Crucible's didactic file had grown to 26 patterns spanning two genuinely different kinds: FMT teaching devices (#1–13) and experimental measurement discipline (#14–26). Only the first set was synced into aIware's registry; the second belongs in the companion paper's methods section, because a registry that mixes "how to explain consciousness to a lay reader" with "a regulator can silently cancel your manipulation" serves neither audience. Co-ownership is now stated explicitly in both files — neither is the sole owner.

- **A repo extraction can strand work that has a live defect behind it.** `pending-el-ko-zh-print-consolidation.md` sat in aIware describing build scripts that moved to `~/simbook/tmp/` on Jul 31 — so for a week nobody owned a **shipped** defect: the live ZH edition renders Simplified Chinese in the *Japanese* Noto face, in both print interior and ebook. **The checklist item this earns: when a project is extracted, sweep the parent's pending files for anything whose code moved with it.** Routed to simbook as P1.

## S283 (2026-08-03) — SJÄLV: the MoC7 handout gets a content brief, and the graphics go out of house

- **The IKEA-manual handout is now `SJÄLV`** (Swedish: *self* — the thing being assembled is the self-model), tracked as **AIW-139**. MG's decision from the crucible session, promoted out of the cross-project inbox into aIware's own backlog because the deliverable has a hard date (MoC7, Oct 12–16) and the inbox is not a tracker.

- **Division of labour set by MG: content here, graphics elsewhere.** *"leave the token heavy graphics work to perplexity / just prepare the content."* Perplexity (Opus 5 via Perplexity Computer) produces the first take on the drawings; its return comes back to an aIware session for review. The brief (`drafts/sjalv-manual-brief-for-perplexity.md`) was therefore written to be **fully self-contained** — every fact, number and prohibition restated inside one file, because the external model has no repository access and a reference it cannot follow is a gap it will fill by inventing.

- **The biggest risk in the artifact is structural, not editorial.** A parts list *looks exactly like four modules* — that is what parts lists are — and "four modules" is the precise misreading FMT has spent years correcting. The mitigation had to be structural rather than a caption: the four kinds are drawn as graded, overlapping regions on **one continuous substrate sheet**, never as separately bagged snap-together parts. Recorded as red line #1, to be checked before anything else in the returned draft.

- **The criticality engine is drawn as the power supply, not a component** (recommendation, MG to confirm). This is AIW-138's demotion made visual: criticality powers the assembly and is not part of the self. It also resolves a real conflict between two four-item lists that are not the same list — FMT's four model *kinds* (IWM/EWM/ISM/ESM) versus the implementation's four *circuits* (CE/EWM/ISM/ESM), which has a criticality engine and no separate implicit world model.

- **The finished product does not wake up.** No glow, no spark, no eyes opening. The credibility of the whole artifact rests on the last panel refusing to do what every other consciousness illustration does; what carries the honesty instead is the **call-for-help panel** — assembly complete, every part fitted, figure still on the floor beside the phone. That is P3 asserted-not-derived (§3.4.3), drawn accurately, and it is funny only because it is true.

- **The demonstrator panel stays cold.** "Requires 2 people" is drawn as a neutral second figure, not a parent-and-child scene: *"usually initiated by parents"* is new developmental content that is still unsourced in our own material (AIW-138's open question 3). A printed handout cannot be un-published, so the warm version waits for a source.

- **Claim discipline carried verbatim into an artifact aimed at a general audience.** Closure is an **advantage in a fit window, never a necessity** (a finite closed loop unrolled over a finite horizon is feed-forward plus memory); the advantage scales with the **richness of the redeployed self-model, not recursion depth** (depth was the confound that killed a design pre-build); the word "Turing" appears nowhere, with Lenore Blum on the MoC7 advisory board. The general principle worth keeping: **a popular artifact inherits the paper's claim limits in full** — the format may be loose, the claims may not be.

- **The format is the audit.** You cannot draw "step 9: consciousness emerges" without it being visibly absurd, so the manual can only be as honest as the parts list actually is. The four backordered parts (granularity, sufficiency, where "very simple language" stops being simple, and why closing the loop produces feeling) are specified as **the most important panels in the document**, and the external model's *"list of every panel you could not draw"* is defined in the brief as the most scientifically useful thing in the deliverable — each entry marks a place the theory is still prose.

## S282 (2026-08-03) — MoC7 GO; FMT's five principles collapse to three

- **MG said GO on MoC7.** Confirmation sent to the organisers; dinner booked; arriving Sun Oct 11 for the informal Carlsberg Museum event, on the reasoning that the MoC series designs day one for one-on-one contact and a museum afternoon is a better first meeting with Kleiner than a poster board. Registration + payment (€514.80) remained MG-owned at session close. MG asked to be reminded about registration and travel **every exchange until each is confirmed** — recorded as a standing instruction in `docs/pending-moc7-copenhagen.md`.

- **FMT now has THREE principles, not five (AIW-138).** MG's restructure, checked against the paper and accepted:
  **P1** open-ended computation allows free modelling — *criticality is demoted to the signature that property leaves in neural tissue, not the principle*; **P2** recurrent non-linear dynamics of sufficient complexity host a second computational level (persistent activity patterns individuated by their mutual effects rather than by which cells carry them); **P3** phenomenology is a real, physical effect on that level, arising exactly where the modelling closes on itself. Redirection, variable permeability and simulation forking demote to **consequences**. MG merged the old P3 (virtual qualia) and P4 (closure) into one.
  - **Two of the demotions were already the paper's own position**, buried: the JAIC slice (§3) had already split open-ended computation from criticality, and §3.2 already derives the four models as an emergent minimum ("four is the floor, not the ceiling"). The restructure largely *surfaces* existing text — and exposes that **master and slice currently disagree**, since the full paper still lists criticality as principle 1.
  - **One correction issued and accepted: closure is NOT identical to the standing-wave computing.** §3.4's three-stage argument requires virtual-level computation to exist *without* closure (Stage 1 weather simulation, Stage 2 self-monitoring); identifying them would make FMT's Hard-Problem move circular, and would cost the JAIC detector its read-only null — the thing that defeats the unfolding argument.
  - **Guards recorded:** P3's biconditional *is* the constitutive claim (§3.4, still asserted-not-derived per §3.4.3) and does **not** license a criticality biconditional — one-directional rule stands. The detector keeps three separate checks; do not collapse them to mirror three principles.
  - **Why this is a stronger structure, not a retreat:** predictions derived from consequences of a smaller axiom set are harder to dismiss than predictions bolted directly to axioms. Cost is real — §8's five prediction derivations cite principles *by number* and each must be re-derived.

- **"Turing complete" is true of the modelling level and therefore useless to claim.** MG challenged the earlier caution and was right: under unbounded memory a brain, a PC and Rule 110 are all Turing complete, so the predicate cannot separate a conscious system from a spreadsheet with a loop — conceding it hands away the §3.4 Stage-1 distinction. FMT's real claims are that the modelling is **not amortizable** and that it is **architectural** (self-model in the world-model's update rule); neither is a complexity-class claim. Trap to know: Siegelmann & Sontag's rational-weight RNN universality needs unbounded weight *precision* — the same infinity by another door.

- **§3.7 keeps the word "criticality" but not the relation.** MG's condition was "keep it if didactically useful without costing too much correction later". The condition fails on a count: **"criticality requirement" occurs 20× in the paper**, and each occurrence restates the relation the restructure exists to fix, so keeping the bare phrase is the *high*-correction-cost option. Settled title (MG's own shorter phrasing): **"Criticality: Signature of the Computational Regime"** — searchable word first, relation stated in the title so the body needs no walk-back.

- **v14 must be online before Oct 12.** The poster QR resolves to the Zenodo *concept* DOI, which always serves the newest version — so v13's five-principle text would contradict the poster at the board, in a room holding two NoC associate editors. Five-phase plan in `docs/pending-fmt-principles-restructure.md`; phases 1–2 are cheap and fix the master/slice inconsistency, phase 3 (re-deriving §8) is the real cost.

- **Poster: built from the current paper, not the accepted June abstract.** The load-bearing block is closure stated as an **intervention** (clamp the self-state, sweep, watch the world-model's induced transition) — the JAIC formulation, chosen because an AMCS room wants a criterion it can apply and attack. The ledger keeps converging evidence and novel untested predictions in separate tables and **pre-concedes in print** that most corroboration rides on the criticality requirement shared with ConCrit/REBUS. Abstract recommendation for v14: **version B** (claim leads, principles as the compression); A is the formal-venue variant.

- **Meta-science register is banned in FMT prose and must be swept every revision.** MG on the first lede ("…sharp enough to be applied to a candidate system — and sharp enough to fail"): *"isn't that explaining science to scientists again and worse advertising good scientific practice instead of contents"*. Two further instances fell in the same sweep. The line that survives the test: **naming what would falsify the theory is content; talking about the virtue of being falsifiable is not.**

## S281 (2026-08-02) — MoC7 Copenhagen poster accepted; AIW-130 decisions 3–5
- **MoC7 acceptance is not a talk-application downgrade.** MG applied for the poster track deliberately (one-on-one networking over 15 minutes of stage time); the acceptance matches the application. Recorded because the MoC7 application page states that failed *talk* applicants "will usually be offered" a poster — a future reader could otherwise misread the outcome.
- **Why a conference is the right spend against a publication problem.** FMT carries 5 desk rejections and 0 peer reviews; AIW-106/AIW-07 already concluded the blocker is format + affiliation, not content. The only substantive peer reviews FMT ever received came from a conference (AICE-26). MoC7 attacks exactly that failure mode — and the mapping done this session shows **Johannes Kleiner is simultaneously MoC7 organiser, Associate Editor at *Neuroscience of Consciousness* (Lane A / AIW-103) and a JAIC editorial board member (Lane B / AIW-62)**; Kanai (JAIC EiC) is also a NoC Associate Editor; Atmanspacher (invited) and Prentner (organiser) co-edit *Mind and Matter*. Conference lands ~10 weeks before the NoC Dec-31 deadline. **The highest-value item is the collective consensus paper** (topics proposed + voted ~Sept 12; ties to AIW-100/AIW-27 SMoC) — not the poster. Decision itself (attend / ~€1,200–1,900, non-refundable) is MG's, deadline Aug 7.
- **AIW-130 #3 — keep Plenz & Shew as NoC reviewers, but delete the comparative framing.** MG: *"there was no need whatsoever to mention that we 'complete' or anything their work. It adds nothing to the paper."* Generalised rule worth carrying: **the honest-convergence discipline applies to competitors, not only to allies** — state FMT's explanation positively, cite theirs neutrally, let the reader draw the comparison. Same sweep owed on the JAIC body re Kanai's ICF.
- **AIW-130 #4 — name the architectures (MG overruled the session's "keep generic" default, correctly).** With *several* named published architectures the consent/appropriation objection largely dissolves: a set demonstrates the detector's range where a single name reads as anointing a candidate, and applying a published criterion to published work requires no permission. "A generic embodied neuromorphic architecture" is also precisely the vagueness that drew "not sufficiently specified or operationalized" from five desk editors. **Safety comes from the framing, not from anonymity: report where each architecture FAILS, not only where it passes.** Slate to include Sandamirskaya's DNFT/attractor work and Zou's SpikingMCU; courtesy heads-up to Sandamirskaya before submission is social-owned.
- **AIW-130 #5 — JAIC reviewers Kleiner, Wiese, Mediano, no 4th** — accepted knowingly after being shown that two of the three sit on the MoC7 organising committee MG may meet in October (board-adjacent nomination is normal; the editor assigns regardless; Kleiner may become handling editor instead).

## S280 (2026-08-02) — simbook made visible in the `af` launcher (registry registration)
- **Root cause:** `~/simbook` (extracted 2026-07-31, AIW-125/CFG-478) was never added to `~/cfg-agent-fleet/registry.md` or `dashboard-cache.md`, so the `af` picker had nothing to render — the "not visible in af menu" symptom was pure missing registration, not a config fault in simbook itself. Mechanism note: the picker filters **P4/P5 out** unless `PICKER_SHOW_ALL=1`, and it reads `dashboard-cache.md` (not `registry.md`) for what it renders.
- **MG-set priorities:** **simbook = P1** (Parent aIware, PRIVATE-only, type writing → nests under aIware as `c`), **simopt = P2** (reactivated from P4 — it's the live public base for furkansim + the crucible gridworld port → standalone `6`).
- **Boundary precedent (deliberate, not a violation):** the fix lives entirely in cfg-agent-fleet (registry + cache), across aIware's hard cross-project write boundary. MG explicitly chose **path B** — make the cfg edit + commit from the aIware session — over routing to a cfg session. Recorded honestly in the cfg commit (71a0603) + the cfg inbox annotation so it reads as authorized, not accidental. cfg's own `CONFIG_REPO_DIRTY` (2 prior-session auto-gen files) was resolved in the same commit. CFG-479 (history purge) + F2 (all-machine pull) left open — MG-gated, out of scope for visibility.

## S277 (2026-07-30) — AIW-130 two-slice papers: reframe, co-authors, pipeline hardening
- **NoC reframe (executed MG's S276 review):** dropped "selective-deployment" as the lead; the criticality claim is now strictly ONE-DIRECTIONAL (no criticality → no consciousness, biological scope; a near-critical cortex can be unconscious — *accommodated*, not a disconfirmer). Lead = necessity of free computation + the constitutive self-model self-conflation (§D). Promoted this framing to durable docs (`project-reference.md`, `prediction-framing.md`) so future FMT writing can't re-introduce the over-claim.
- **JAIC:** math verified by Fable (no wrong formulas; one real Box-1 lumpability contradiction fixed); the same AI-tell register found + swept. Title tamed per MG: "…a Self-Model That Takes Itself for Its Bearer" (chiasmus kept).
- **Co-authors (MG-directed):** Georgia Sousouri → NoC (§5 EEG protocol), Alen Frey → JAIC (§6 in-silico/crucible); listed **provisionally** (earned-not-gift); bounded, domain-scoped ask; invites sent cross-cc'd for peer-pressure. Affiliations (esp. Alen: Ivoclar vs independent/ETH — IP + symmetry) deferred to MG.
- **Pipeline hardening (root cause of the S276 misses):** the AI-tell check was a shallow phrase-grep and no theory-fidelity gate existed → added dedicated `register-ai-tell` + `theory-fidelity` reviewer lenses + a refiner constraint + a RE-REVIEW NO-GO gate (`scripts/fmt-pipeline/`).
- **Crucible ↔ JAIC detector:** checks 1 & 3 pass at toy scale; check-2's decisive scaled test is OPEN = the paper's own stated open test (honest by design). Movers: Target A / AIW-124 + CRU-57 (Slice 1 already shipped, per inbox).

## Archive Index

Older entries (2026-03-16 through Session 253 / 2026-07-06) were moved verbatim to **`docs/decisions-archive.md`** to keep this file grep-able. Archived sessions/topics:

- **S248 (2026-07-07)** — Book ed.2 DE trimmed for DACH (edition-scoped tone divergence)
- **S246 (2026-07-06/07)** — Book ed.2 experiential restructure (reader-first opening, printed blind-spot demo, Fable-for-creative-prose)
- **S244 (2026-07-06)** — FMT v12 adversarial review, targeted revision, theory-complex assessment
- **S239 (2026-07-05)** — CA identification is scale-agnostic didactic device, not literal biological claim
- **S240 (2026-07-05)** — Inbox triage: AGI-26 declined, Birch deferred, Seth BBS superseded
- **S241 (2026-07-05)** — Fable-5 content-gate is INTERMITTENT (S239 refusals didn't reproduce)
- **S239 (2026-07-05)** — Fable-5 unusable for consciousness/AI-architecture content; Opus is the ceiling
- **S238 (2026-07-04)** — Book voice-pass (AIW-93): parallel-inventory → verified-JSON-apply methodology
- **S232 (2026-06-19)** — Inward causal role is necessity not freedom; seizure dynamics; two-dials not yet formalized
- **S228 (2026-06-17)** — Olfaction-bypasses-thalamus folds into AIW-87
- **S227 (2026-06-17)** — Will/motivation are poles on a gradient, not separate kinds
- **S224 (2026-06-12)** — AIW-47 eNeuro paper finalized + double-blind code handling
- **S223 (2026-06-12)** — AIW-47 authorship & venue (optimize for FMT recognition); meta-d′ standard method
- **S217 (2026-06-10)** — Fable 5 review: FMT stands; fixes are executional
- **S189 (2026-04-16)** — Zenodo v5 blocked on deep revision
- **S208 (2026-05-29)** — FMT v7 architectural clarifications; NBSR desk rejection
- **S209 (2026-05-29)** — Gridworld vs cellular automaton instrument choice
- **S197 (2026-05-11)** — Full paper stays ~29k for Zenodo; Frankish distinction; self-referential closure commitment
- **2026-03-16** — Strategic direction (two paths to breakthrough); co-author strategy
- **2026-04-15** — German book publication on KDP
- **S210 (2026-06-03)** — James-Stein / SB-HC4A entanglement; thalamus evidence for FMT
- **S215 (2026-06-10)** — MEMORY.md is a mirror not a source; conversation-log drift guard
- **S216 (2026-06-10)** — Seth commentary → standalone Zenodo preprint; eNeuro short-report design (AIW-47 spine)
- **S219 (2026-06-10)** — SB-HC4A cosmology argument repairs (locked spec)
- **S225 (2026-06-17)** — RIM unparked + COGITO convergence; book revision (next edition)
- **S229 (2026-06-18)** — AIW-47 eNeuro abandoned + Bonn deprioritized; connectome (BANC) as gatekeeper-free avenue
- **S230 (2026-06-18)** — AIW-90 Track 2 done + AIW-91 (minimal critical substrate) opened
- **S231 (2026-06-19)** — AIW-90 criticality corrected to synchronous bursting; TWO kinds of criticality (extent vs complexity); Fork A/B resolutions
- **S233 (2026-06-22)** — AIW-92 didactic-pattern integration (books-first)
- **S234 (2026-06-25)** — AIW-96 open-data test of ESM/EWM double dissociation
- **S236 (2026-06-29)** — AIW-92 integration + paper sharpening, Zenodo v11
- **S237 (2026-07-01)** — AIW-99 fix + Bach prior-art (RIM) + Friston-500 → SMoC opportunity
- **S242 (2026-07-06)** — AIW-91 "simplest AC" architecture + embodiment

Older entries → `docs/decisions-archive.md`.

---

## S275 cont. (2026-07-28) — FMT wiki refresh (AIW-27): scope & framing

- **Content ownership split.** The fmt.matthiasgruber.com wiki content is aIware's (`wiki/*.md`); deployment (mkdocs.yml, DNS, `mkdocs build`) belongs to the **infrastructure** project. aIware never touches deploy.
- **Targeted correction + currency, NOT a from-scratch rewrite.** Inspection showed the March-2026 wiki is ~70% aligned with current FMT framing already (four-model-theory.md has "floor not ceiling", "kinds", constitution-not-transfer). A full 127-article regeneration would discard sound structure + the AIW-27 SEO/DOI/figure post-production. MG chose targeted.
- **Public positioning = FMT as the "leading candidate for a standard model of consciousness"** — pre-paradigm, an invitation/not a verdict. MG chose this over (a) asserting it AS the standard model (overclaim risk with the academics being courted) and (b) dropping the SMoC brand (loses social's linking hook). This is what social links.
- **Canonical criticality reframe.** The requirement is **free compute** = Class-4 (universal-computation) capability *actually deployed* for open-ended self-modeling; criticality (σ≈1 / λ≈0 / edge of chaos) is the **measured dynamical signature**, not the requirement (paper §3.7.3/§8.9; misconception-registry #3). Applied to 10 load-bearing files (commit `0b8c4240`); long-tail sweep pending (AIW-27, `docs/pending-wiki-refresh.md`).

## S275 (2026-07-28) — FMT two-slice run reframed + de-risked; three-paper plan; NoC single-blind correction; Wolfram/Metzinger advisory

**Interim session before the 23:00-gated AIW-130 Fable drafting run** — de-risked + reframed the scheduled run; no drafting (time-gate held).

**NoC is SINGLE-blind, not "double-blind-friendly" (load-bearing correction).** Verified against OUP author guidelines (verbatim quote in `docs/noc-si-cfp-2026.md`). The AIW-130 handoff + AIW-103 had claimed "double-blind-friendly"; AIW-106 had it right. Lane A therefore proceeds on **guest-editor fit** (Pinto/Doerig/Dołęga solicit exactly the computationalism-vs-implementationism material), NOT on blinding. CFP banked: deadline Dec 31 2026; ≤9k words; APC $3,625.

**Three-paper plan (MG-directed).** FMT feeds THREE non-overlapping slices — NoC (brain), JAIC (machine), JCS (philosophy) — distinct central claim + distinct primary evidence each. Tonight drafts TWO (NoC + JAIC); **JCS = deferred third paper (AIW-46)**, the Hard-Problem-dissolution carve (qualia = virtual self-interface) — NOT a swap for NoC.

**NoC thesis reframe (MG).** The "more than computation" = **computation on top of computation** (higher-order; the self-model modelling the modelling). It has sat in fMRI for decades unrecognized (forest/trees); hard to detect because it doesn't raise IQ, costs short-term, optimizes only narrowly (→ why the brain isn't critical everywhere-always). **ANCHOR = no criticality → no consciousness + FMT's unique *why-criticality* explanation** (energy/optimization can't explain selective cortical criticality; FMT: it's the substrate for the higher-order computation that IS consciousness). The two-dials → time-dilation prediction is **demoted to a side-show**. REVIEW must engage the "criticality is optimal" literature (Shew&Plenz/Chialvo/Beggs).

**JAIC check 3 = "open-ended computation"** (was "Class-4 / SOC dynamics"). Substrate-neutral requirement = free compute; criticality is only the biological signature — consistent with the v14 free-compute refinement (S271/AIW-126). A cross-paper guardrail is baked into the handoff so NoC (criticality, brain-scoped) and JAIC (open-ended computation, substrate-neutral) don't read as contradicting on what is "necessary."

**Standing Wolfram + Metzinger name-drop advisory (MG-directed, GENERAL).** Two tiers: CREDIT them in the FMT base paper + books (historical lineage — intellectual honesty over politics, "simple as that, dear academia"); OMIT them everywhere else we control (submission slices, outreach, blog posts) where the association is a net liability. Persisted → `.claude/knowledge/neuroscience-communication.md`.

**Blog delegation.** Each of the three slice points is simple enough to stand alone as a blog post → filed a social cross-project inbox task (3 FMT blog posts, one per point) carrying the same framing constraints.

## S271 (2026-07-26) — FMT v13 PUBLISHED; free-compute-vs-criticality refinement (→v14); Gemini-misreading registry

**v13 published to Zenodo** — version DOI `10.5281/zenodo.21611849`; concept `10.5281/zenodo.18669891`→v13; reciprocal `isSupplementedBy`→companion `10.5281/zenodo.21610993` set. MG-ordered. Gated on TWO independent Fable passes (audit of the full-pass diff + verification) both GREEN before the irreversible push; built clean 123pp + a tracked-changes PDF for review. MG chose "full pass": AI-tell/register cleanup (6 "is warranted" openers, virtue-openers, 3 defensive tags, empty evaluative, hedge), frame-rate reconciled to ~20 Hz, 150-word sentence split, antithesis reword, cross-ref repoint, +4 verified cites (Yaron2022 ConTraSt / NYDeclaration2024 / Tegmark2000 Q3 / Gilmore1992 anosognosia), −Wolpert orphan, companion DOI in refs. `.tex`/`.bib`/`.md` kept in parity (Fable-mirrored the `.md`). Caught+fixed a double-tilde substring bug mid-edit (comgarra class).

**Theory-framing refinement (→v14, `AIW-154`, filed at the time as AIW-126):** MG — *"criticality is what free compute looks like in SOME systems, maybe not all."* The requirement is FREE COMPUTE (Class-4 capability actually deployed for autonomous self-modeling); criticality is its observable, **non-universal** signature. Already licensed by §3.7.3 trichotomy + §8.9 capability-first + Table 1b ("necessary, not sufficient"); v14 should invert the §3.7 emphasis (retitle away from "The Criticality Requirement") and disambiguate §3.6/Table-1 "information transfer" (constitution-of-the-simulation vs permeability). NOT changed in v13.

**Gemini-misreading registry** (`.claude/knowledge/fmt-misconception-registry.md`): a frontier LLM defaulted to 6 characteristic FMT misreadings — naive modularism; implicit→explicit as data-transfer; criticality-as-requirement; binding-problem-misapplied; over-localization; FMT-as-implementation-spec. Banked with per-misread preemptions + comm lessons; predicts reviewer/journalist/AI misreads → feeds AIW-95, v14, and outreach. New rule: when an interlocutor "demands the math," first check the demand isn't encoding a misread (Gemini's "transfer/criticality/binding calculus" asks were all misread-artifacts).

**TWCF funding lead** (`docs/fmt-funding-leads.md`, AIW-134 — renumbered from dup AIW-127 on 2026-07-31): Templeton World Charity Foundation — Accelerating Research on Consciousness / Structured Adversarial Collaboration = best-fit experiment sponsor (funded COGITATE). Warm bridge: Michael Pitts (Reed) is a TWCF grantee AND already on the FMT outreach roster (AIW-05).

**Data-integrity catch:** the S270 handoff listed "fmt_formal §4.x heavy" as remaining v13 work; ground truth showed §4.7 already written S268 → handoff line was stale (flagged to MG, not silently followed).

## S279 (2026-07-31) — pop-sci book extracted to private `~/simbook`; forward leak closed

**Decision (MG-directed, CFG-478 Option 3):** the pop-sci book (manuscripts, covers, KDP, translations, book
build infra) — which had leaked to aIware's **public** mirror via the `filtered-push.sh` glob bug — was extracted
to a new **private-only** repo `JeltzProstetnic/simbook` (init `3d5b7d0`, provenance `aIware@a05daaf0`), `git rm`'d
from aIware, and the public tip re-filtered clean (verified: 0 book/isbn/`private/`/session-state files; `figures/`
101 + `paper/` 79 stayed public). **This closes FORWARD exposure only** — old public commits still carry the blobs;
the history purge is deferred to **CFG-479** (MG picks method later). Report framing: "no new exposure; historical
cleanup pending," never "leak gone."

**Asset-sharing topology (MG, load-bearing for the extraction):** (1) `figures/` are shared with the papers and
**stay public in aIware** — simbook gets self-contained *copies*; book-exclusive figures may be privatized later
with the CFG-479 history purge ("maybe"). (2) Shared *private* knowledge (didactic-patterns, awareness-terminology,
publication-build/workflow, neuroscience-comms, etc.) **stays in aIware; simbook references, never forks** — only
`kdp-specs.md` (book-only) moved. (3) Runbook missed 3 things I caught: figures are `../figures/` refs (needed copies
+ the render pipeline), `typography_fixes.py` was an unlisted book dependency, and `figures/book/homunculi.*` were
untracked-nowhere (now version-controlled in simbook); ABOUT.md was also offering the paid manuscript as a *free*
public download (removed).

**Other decisions this session:** duplicate `AIW-127` bug surfaced during backlog migration → the TWCF theory item
renumbered to **AIW-134** (book KDP item keeps AIW-127, in simbook). 8 clear-book backlog items migrated to
`~/simbook/backlog.md` (AIW- IDs kept for cross-refs; new items = `SIM-`). KDP NL-hardcover barcode-reaching-into-spine
rejection → **simbook SIM-1** (P1, likely a spine-unaware barcode offset in the HC cover build). Bartl-label intake
(50 messages) ingested → `docs/bartl-intake-2026-07-31.md` + cross-project routes; my assessment of the batch
(bible-code razor cuts FMT's own claims; connectome-instancing indicts the crucible minimal-substrate; FMT is 1952-side;
Sandamirskaya DNF = top deliverable) is in that doc.

## S270 (2026-07-26) — Companion 2026d restructured to results-only; §9.2 taxonomy rejected

**Decision (MG-directed):** the companion (Gruber 2026d) is a **report of results**, not a mixture of results and forward plans. The forward-looking sections were **removed from the paper** — they each get their own report:
- former **§5** (open, decisive scaled test),
- former **§6** (discriminating closure × criticality prediction + preregistration),
- former **§8** (biological-signatures / interface-causal-chain research direction),
- former **§9.1** proposed thinking-time / internal-simulation-budget DV.

The paper now runs: architecture (§2) → two framing moves the results forced (§3) → banked results (§4) → CRU-36 null (§5) → discussion (§6) → limitations (§7). The single honest forward note (the scaled dependency is open and cannot be a clean binary) is folded into §7 limitations, not developed as a plan. **Full pre-revision text with all removed sections: git `c5820130`, `drafts/companion-computational-paper-draft.md`** — the seed for the future reports.

**§9.2 modelling-capability taxonomy (self → other → free-play → tool) — REJECTED, do not reintroduce.** MG's ruling: (1) it is not his — an AI invention attributed to the theory; (2) the ordering is wrong — *tool use is simpler than free modelling*, so the given progression is backwards; (3) more fundamentally it is a **false order**: a direct, linear, easy metric of modelling capabilities is not something we can imagine constructing, so ranking modelling "kinds" on one axis is unsound in principle. Burghardt (2005) went with it (was cited only there).

**Also this pass (de-bloat + de-AI, per MG "a bit blown up… many ai tells / aidioms"):** narrative rewritten in plain scientific prose (dropped "not-X-but-Y" chains, coined flourishes — "VM tax", "banked is banked; open is open", "one falsifiable interaction at a time" — triads-for-rhythm, excess bold/em-dashes). Body **8543 → ~5100 words; PDF 16 → 10 pages.** **No quantitative result changed** — every `**Methods.**` paragraph is byte-identical to `c5820130`. References pruned to cited-only: dropped Burghardt (§9.2), Gruber 2026b (former §8), and pre-existing orphan Algom & Shriki; Boedecker 2012 kept and now cited in §3.2 (edge-of-chaos ESNs). **PUBLISHED to Zenodo S270 (2026-07-26): companion concept DOI 10.5281/zenodo.21610993** (v1 = 21610994; cite the concept/generic DOI) — CC-BY-4.0 preprint, `isSupplementTo` the master FMT **concept** DOI 10.5281/zenodo.18669891. MG rule (S270): always use the generic/concept DOI, never a version DOI — DMS ACA-004's 18861613 was a stale version DOI; the Zenodo record's `isSupplementTo` was corrected to the concept DOI 18669891, and README/ABOUT use the companion concept DOI. MG lifted the hold and authorized publish, choosing not to wait for the crucible maintenance result. Abstract stripped of internal experiment codes (CRU-36) per MG — codes kept in the body. Published via `scripts/zenodo-new-record.py` (draft-then-publish; metadata edited from the stale Seth-commentary block first). Metadata is editable post-publish; reciprocal master→companion `isSupplementedBy` link + the companion DOI into the FMT v13 references = next session.

---

## S269b (2026-07-25) — Companion 2026d prose+citations complete; Deck 2 reaffirmed as non-build env

**Executed (Deck 2):** all 8 `[[CRUCIBLE]]` slots (§4.1–§4.6, §7) filled with verified crucible **Methods.** paragraphs sourced from the evidence-ledger digest; all 5 KEEP-AS-PLACEHOLDER items (§6.3 design, §6.3 transfer-DV redesign, §8 biological-signatures, §9.1 thinking-time, §9.2 modelling-capability-taxonomy) rephrased as preregistration-pending / "proposed future work" prose; all 6 `[[VERIFY]]` citations resolved with DOIs / ISBN (Bertschinger 2004, Boedecker 2012, Burghardt 2005 + §9.2 honesty caveat inline, Kanders 2017, Schölkopf 2021, Gruber 2026e master-paper suffix confirmed). Grep confirms zero live markers in body. Draft is prose-complete + citation-complete; PDF build only remains.

**Decision (MG-directed, self-critique inclusive): Deck 2 is not a paper-build env — reaffirmed and strengthened as an active guideline, not a passive fact.** Explored installing pandoc + LaTeX on Deck 2 to build the companion PDF same-session (three disk-space failures on SteamOS's 5 GB `/`; TinyTeX in `$HOME` would have solved the disk issue but the fundamental concern remained). MG reconsidered: even a working Deck-side build renders a *different* artifact than WSL/Fedora-home's canonical rendering — font-version drift → page-count drift → possible KDP cover-spine breakage — and mixing the two builders across a review cycle invites subtle "why did the layout change?" incidents. **Rule (reaffirmed): aIware paper/book PDFs build ONLY on WSL (canonical) or Fedora-home. Deck 2 machine-file "LaTeX not installed" row should be strengthened to an active guideline with the reasoning captured.** Cross-project inbox item filed for cfg-agent-fleet.

**Self-critique (process, not content):** when a machine file has an explicit "not for this purpose" note, the correct first response to a user's "can you install here?" is to surface WHY the constraint exists and let the user weigh it — not to immediately produce install options. Three round-trips through disk-space failures were the cost of my not doing that. Recorded here so a future session sees the pattern.

**Handoff for next session (WSL or Fedora-home):** `bash scripts/build-md-pdf.sh drafts/companion-computational-paper-draft.md tmp/companion.pdf -H paper/fmt_formal/unicode-header.tex` — the `-H` is mandatory (draft uses σ / λ / ↔ / ≥ / ≤ / ≫ / ∈ / · / α / Δ / ε / τ / Σ; shared preamble doesn't declare all of them, fmt_formal header does). MG eyeballs the built PDF; Zenodo publish stays HELD by MG.

---

## S267 (2026-07-24) — Crucible in-silico predictions: placement (Fable) + v13 §8.9/§3.7 landed + undersell root-cause

**Decision (Fable-decided, MG-ratified):** the crucible computational program goes into the master FMT paper as a **self-contained, droppable §8.9 "In-Silico Tests of the Architecture"** (after §8.7/8.8, NOT folded into the clinical five) plus a **separate companion computational paper** (Gruber, 2026d; ALife / Neural-Computation class) that §8.9 references. Rationale: MG's **master/subset** publishing model — the master can be comprehensive because desk-reject risk is managed at the per-journal subset-cut, but only if the material is section-modular (a clinical subset like NoC drops §8.9 in one line). Correction to S266: **§8 has no "P1/P2/P3" to reword** — the crucible computational predictions were never in the paper; the task was INSERTION (§8.9), not rewording (data-integrity fix, independently flagged by Fable).

**Executed (v13, `.md` + `.tex`, build-verified 123pp, 0 undefined cites/errors):** §8.9 (banked-positives-first) + 5 forward-pointers (§8-intro, §3.7.3, §8.7, §9-OQ2, §9-OQ4); AIW-94 §3.7 two-dials **formal layer** (spatial heterogeneity premise; extent = percolation P∞ + regional σ/α estimation; complexity = on-cluster Lempel-Ziv; orthogonality flagged as conjecture; Tononi–Sporns–Edelman C_N 1994 engaged); 3 refs added (Kanders2017, Tononi1994, Gruber2026d). AIW-105 paper-side found **already landed** (v12 §3.4.2/§3.4.5/§8.6) — no edit. AIW-75(3): **keep all 11** Gruber2015 cites (load-bearing priority anchors). Companion paper drafted + upgraded → `drafts/companion-computational-paper-draft.md`.

**Root-cause lesson (undersell):** the first Fable pass drafted §8.9 + companion from the NULL-FORWARD `pending-cru36-prediction-revision.md` brief, which omits the banked positive evidence (closure maintains a model recursion-specifically; a self-model-gated planner beats a full reactive bracket on depth; prospective-survival advantage; P1 d=2.44). MG caught the undersell. Fix: crucible's full evidence ledger is now digested at `docs/crucible-evidence-ledger-digest.md` (complete-data source); the CRU-36 brief carries a warning pointing to it. **Rule (→ prediction-framing.md): draft crucible/paper content from the DIGEST, never the null-forward brief.**

## S266 (2026-07-24) — AIW-110 CRU-36 prediction decisions ratified (capability-first)

**Decision:** MG ratified the three CRU-36 / AIW-110 prediction-revision theory decisions, all **capability-first** (crucible's 2026-07-08 framing → now aIware canon):
1. **P2 independent variable = Class-4 capability** — the substrate must support universal / free computation; avalanche-σ≈1 and Lyapunov λ≈0 are *interchangeable instruments* certifying it, so the σ-detuning arm is dropped.
2. **P2 dependent variable = task-outcome categorical** — de-tuning criticality categorically collapses the observational→causal-transfer modelling task, only with closure ON (XOR / memory-curve retired: no self-model or closure).
3. **Formalization = two instruments, one capability band** — rate-ESN/spectral-radius (abstract Class-4 proof) + spiking/avalanche (biological realism) certify the *same* capability at different substrate levels; not a contradiction (moot-by-#1).

**Rationale:** CRU-36 nulled because it tested closure/criticality on a homogeneous reservoir with no differentiated self/world models — closure and criticality are *enabling conditions for the modelling step*, not effects in themselves (FMT-consistent). Capability-first dissolves the "which criticality" (Root A) ambiguity into a Class-4 requirement, consistent with §3.7's Wolfram grounding. Residual work [**CORRECTED S267:** §8 has no "P1/P2/P3" — the crucible computational predictions were never in the paper; the task was to INSERT a new §8.9, not reword] = new §8.9 + `.claude/knowledge/prediction-framing.md`, folded into the **AIW-121 v13 epic** (executed S267 — see entry above). Brief: `docs/pending-cru36-prediction-revision.md` §D (null-forward — use `docs/crucible-evidence-ledger-digest.md` instead for paper drafting). No experimental-design work remains aIware-side (crucible's, done).

## S266 (2026-07-23) — Book translations nl/el/ko: engine, channels, KDP limits

**Decision:** Add Dutch (`nl`), Greek (`el`), Korean (`ko`) editions of *The Simulation You Call "I"*. Translation + native-editor interior review on **Fable**; Kalk scan + coherence on **Opus** (unchanged division of labor). Channel routing forced by KDP language support: **Dutch → KDP** (print + Kindle, supported), **Greek + Korean → PublishDrive** (neither is KDP-supported in any format — same off-KDP route as the existing `zh` edition).

**Rationale:** English already exists as the base manuscript, so the biggest untapped KDP-native market is Dutch; Greek (strong philosophical-vocabulary affinity for this book) and Korean (consciousness-studies / tech readership, completes East Asia beside ja/zh) are worth doing via PublishDrive. Fable-failure policy = halt-and-ask, no silent Opus fallback (MG). Done under a console-SSO outage in a remote web session, so Fable-heavy stages were front-loaded to bank the expensive work before handing the Opus downstream to a local fleet session. Handoff: `docs/pending-translations-nl-el-ko.md`; tracked as AIW-123; branch `claude/book-translations-nl-el-ko`.


## S258 (2026-07-12/13) — publishing 8 editions

**Hardcover cover fixes live in the build SCRIPT, never the generated .tex.** The S140 subtitle fix was a manual `.tex` edit; the S144 artwork rebuild regenerated from the script and silently reverted it, so it shipped buggy for months. All cover fixes (eye framing, subtitle position, gradient) now live in `build_book_cover*.py` / `build_translation_covers_latex.py`. A `.tex` edit is not durable.

**All 8 Kindle covers from one recipe.** After many PIL approximations failed to match EN/DE, the fix was to reproduce the EN/DE **LaTeX** front cover for the 6 Latin-script editions (identical gradients/positions, only title/subtitle differ) and match it in PIL only for JA/ZH (xelatex absent). Consistency comes from one recipe, not per-cover tuning. Gradient is dark→**white** at opacity (the white end is what makes the soft "gray" look), MG-tuned a touch darker (black!25/black!20 ends).

**Publish gate for translations waived by MG (2026-07-13).** MG directed publishing all AI-translated editions today, overriding his own human-native-reviewer-before-publish rule. 7 eBooks live (EN/DE/ES/FR/IT/PT/JA); ZH parked on a KDP limitation, not the gate.

**KDP has no Simplified Chinese.** Only Chinese (Traditional) beta, requiring .docx + horizontal-only. A Simplified edition must ship as .docx under the Traditional tag or be converted to Traditional. Parked. (Full spec in `.claude/knowledge/kdp-specs.md`.)

## S260 (2026-07-13) — AIW-109 correction pass

**Line 678 — anosognosia deficit is the Explicit *Self* Model, not the World Model.** EN originally read "Explicit World Model"; two independent translators (ES, IT) had already "corrected" it to ESM. MG (author) ruled **ESM**: a paralyzed-arm deficit is a fact about one's own body/self — precisely, the information that the arm isn't behaving as predicted never reaches the ESM. Fixed EN + DE + FR + JA + PT + ZH; ES/IT already correct. All 8 editions now consistent.

**Edition marker = print only.** MG rejected "ed.2 corr.2" ("only second ed"). The "Second edition" marker goes on the **PRINT copyright page only** (flip First→Second in the build scripts); eBooks carry no edition line (just © 2026).

**Review round before rebuild.** After the High+Med correction pass (~800 edits across 6 translations + EN/DE), MG wants **another review round on the corrected manuscripts before any rebuild/re-upload** — reduce churn, catch anything the fixes introduced. Model routing: Fable for risky/challenging native-language fixes (one agent per manuscript file to avoid collision), Opus/main-loop for mechanical spine edits.

## S262 (2026-07-14) — Fable cost-hold cleared

**Fable cost-hold RESOLVED — MG confirms cost-free (2026-07-14).** The S259 handoff said Fable was re-enabled cost-free (S254); the live fleet agent config still carried the 2026-07-07 cost-hold ("do not route until user confirms no metered charges"). Reported the conflict to MG per the Data-Integrity rule; **MG explicitly cleared it** — Fable is cost-free, use it for the AIW-109 judgment round. The fleet-agent-config hold lives in cfg-agent-fleet → clearance propagated via cross-project inbox (aIware cannot write cfg config directly).

---

## Book translations — IT + JA added; Fable exhausted mid-run; ZH translator deferred + local-Qwen-draft rejected (Session 253, 2026-07-08)

**Context (AIW-108):** the multilingual program (ES/FR/PT already publish-candidates) extended to **Italian and Japanese**.

- **IT:** translated on Opus (60/60) → assembled → Kalk-scanned (491 findings from 89 native-Italian Opus editors) → **392 A+B+D fixes applied** → publish-candidate. Owes 7 Kalk segments + a coherence pass. Reviewer draft `drafts/aiw108-it-kalk-findings.md`.
- **JA:** translated on **Fable** (48/60) — **Fable ran OUT OF METERED CREDITS mid-run** (resets Jul 14 11pm Vienna). The 12 lost chunks were re-translated on **Opus, each primed with its nearest Fable-translated neighbors as house-style exemplars** (MG-requested) — seams verified invisible (register consistent: 0 です/ます vs 1094 である endings). Owes Kalk + coherence.
- **Model policy (updated):** Fable is exhausted (metered credit pool, not the subscription) until Jul 14 → all work on **Opus**. Also hit the **Anthropic session usage limit** (rolling window, resets ~11pm Vienna) → Opus workflows blocked temporarily; remaining IT/JA work deferred to next session per MG.
- **ZH decision (MG):** stays **PAUSED until all other languages are final.** Translator deferred — will be **Opus, Fable, or a cloud Chinese LLM (with account).** **REJECTED: the local-Qwen-draft → Opus-repair pipeline.** MG's rationale: "slop then repair ≈ direct-Opus quality at best + an extra step + a second error surface." A live bake-off (`tmp/zh-bakeoff-results.md`) confirmed local Qwen3-30B-A3B on the 4090 is fast/free/private and fluently native BUT fabricates content on ambiguous input — usable only behind a faithfulness gate, which MG judged not worth it over direct Opus or a cloud ZH model.
- **Local inference as a fleet capability:** filed to cfg inbox — positioned as a quota-outage fallback for NON-quality-critical bulk only, NOT as a translation front-end (per the rejection above).
- **Operational lesson** (also in `.claude/knowledge/publication-build.md`): never run two large Workflow fan-outs concurrently — server rate-limiting silently killed 37 of 89 Kalk agents (the `.catch` masked them as empty results). Serialize; re-run failed segments alone.

---

## S243 (2026-07-06) — FMT Hard-Problem stance + core identity (paper v12)

**Core identity (MG's main claim — now foregrounded in §7.2).** Consciousness *is* the ongoing **transfer / integration of information into the explicit model** — the self-referential updating, at criticality, by which the explicit models are continuously rewritten on the implicit substrate. "Confusing the ESM with oneself" = humor-speak for *Bewusstsein = Interaktion mit dem Modell*.

**Hard-Problem stance = conditional dissolution + narrower-gap (NOT over-concession).** §3.4.3 rewritten (¶A/¶B/¶C): (¶A) the residual "why phenomenality not mere data" is **conditional** — ill-posed *if* the inside/outside asymmetry is constitutive, stands *if* merely epistemic; FMT's one bridging commitment = the constitutive reading. (¶B, MG's own argument) it is **motivated not posited**: in a self-referentially closed recurrent system, *at the level of content*, there is no neutral program/data factorization — the faithful reconstruction is irreducibly first-person ("my five fruits…", never "c=a+b"), so "mere data" is not a coherent rival. (¶C) the identity (first-person-format = lived) is **testable** via **spontaneous first-person report under a training control** (an AC describing a phenomenal life it was NOT trained to describe); the residual doubt is the **general problem of other minds** — crediting a human's report while denying a matched artifact's is special pleading. `◐` kept, now *earned*.

**IIT rating = keep IIT `●` / FMT `◐` (Option 1), integrity-framed.** IIT *argues* from phenomenological axioms (not "posits without argument" — that was a straw-man referee-kill). FMT grants IIT's central insight and reinterprets it functionally/temporally/substrate-neutrally/architecture-gated. Deepest seam = intrinsic (IIT) vs functional (FMT); temporal is reconcilable; both require recurrence and reject feedforward functionalism.

**ESM/EWM boundary.** 2015 book: the *explicit* boundary (Ich/Welt) is **sharp**, the *implicit* (Selbst/Meta) fuzzy. Reconciled = sharp **per snapshot**, fluid **across frames**; old German "misleading." Paper genericized to "explicit models on the implicit substrate."

**Qualia-privacy ("reverse-invent the encoding").** v12 = a paragraph + 1 prediction (structure shareable / absolute encoding refractory — NOT pessimism); ALSO spun out as a standalone, more-testable paper (AIW-105). Does NOT move `◐` (explains ineffability-of-report, not existence-of-feeling).

**Fable = live/intermittent** (ran 6 subs this session), contra the roster's "geo-blocked."

**Book ed.2 — creative prose via Fable (S247).** Wave-2 EN + all DE-port creative prose generated by Fable writer-subagents (they return text; main loop integrates sequentially — single manuscript file = collision rule). Fable confirmed live/selectable (money-gated, not geo-blocked).

**Book DE cultural-redaction principle (MG, S247).** The German ed. was sanitized in places; EN/DE gap now small → port toward EN. EARLY in the book = stay cautious with personal drug/psychedelic anecdotes (a skeptic hasn't bought in yet); LATE (Coda, final chapters) = fine, "whoever followed this far is an ally, not an enemy." The Coda 4D-fractal drug hint (DE had sanitized it to a "childhood dream") was restored on that basis. Ask MG on ambiguous redactions.

**Book DE review format (MG, S247).** Deliverable = an EDITABLE highlighted .docx (all new text + transitions marked) for MG's INLINE German redline. The banked/Fable DE prose has Anglizismus-Kalke ("Hier ist, was…"→"Was soeben…", "mit noch mehr Seite"→"mit Weiß") → a dedicated native-German "Kalk scan" (Fable/Opus, AIW-93 tells) runs before/with the review.

**2015-cosmology confession (MG, S247).** MG had BOTH halves (consciousness + cosmology + their structural identity) since ~2002/3 (the age-25 Innsbruck-bridge epiphany), but deliberately kept the cosmology almost entirely out of the 2015 German book — "didn't dare" (a consciousness theory that also claims to be a theory of the universe = filed under crank). EN's "without the cosmology" line was false + self-contradicted the Notes (which credit the seeds to Gruber 2015: 't Hooft holographic-bound p80, universe-as-cellular-automaton p79) → rewritten to the true story. DE received the confession as a parity insertion (flagged new).

**Book ed.2 — MG DE review is targeted, not a blanket motif-prune; EN kept in parity (S249, 2026-07-07).** MG's full inline review of the DE ed.2 (`DE-ed2-REVIEW-highlighted.docx`, 26 edit ops applied) softened the „bite/attack" combat metaphor and cut two „Hold that X" hooks — but ONLY in specific contexts: `zubeißen`→`passen` in the *predictions* spots (Ch11 + Anhang H), while `zubeißt` in the *Occam's-Razor* passage (Kap1, „wo es zubeißt") was deliberately KEPT. It is NOT a blanket removal. Per MG, 3 of these ported to the (approved) EN for cross-edition parity — cut "Hold that thought" + "Attack them", `bites`→`fits` in the two prediction spots — while EN's Occam "where it bites" (L140) was KEPT to mirror the DE. "Hold that example" (both editions) was left; orca `Rückweg`→`Umweg` / "trip back"→"detour" applied to both. **Do NOT "fix" the Occam bite-motif in either edition — the asymmetry is intentional.** Content/pointer fixes port; pure voice does not (per the DACH-tone decision above).

**Spanish edition — dual-source AI pipeline, human-gated (MG, S250 2026-07-07).** A Spanish edition (AIW-108) will be produced by a **Fable-5 team** translating from BOTH the EN and DE ed.2 manuscripts (EN primary for voice, DE cross-check for meaning + native-idiom solutions), because no human native Spanish speaker is on the team. Locked: **neutral/international Spanish** (widest Spain+LatAm reach; ustedes, no vosotros); **Fable-5** engine (MG runs before the 2026-07-08 cost-cliff; Opus 4.8 fallback); **the AI pipeline produces a publish-*candidate* only — publish is HELD until a human native Spanish reviewer signs off** (AI-only literary Spanish for print is a quality risk MG will not ship). Pipeline mirrors the German process: glossary-first → parallel translate (≤65 lines/agent) → integrate → Spanish "Kalk" calque/Anglicism/germanism scan (A–E) → culture pass → native-quality pass → MG highlighted-.docx review → build/amazon.es. Full spec: `docs/pending-spanish-translation.md`.

**Book ed.2 SHIPPED (S250, 2026-07-07).** All 6 editions (EN+DE × paperback/hardcover/Kindle) uploaded to KDP; EN paperback+hardcover LIVE, both Kindles publishing, DE prints in review. Prices: EN pb $19.80 / hc $29 / Kindle $4.50; DE pb €18.50 / hc €28 / Kindle €4.50. eBooks on 70% royalty. The 2015 German monograph that sold zero copies now has a fully-published six-edition sequel.

**Opus-only Kalk-scan recipe + what Fable is reserved for (MG analysis, S252 2026-07-08).** After the Fable→Opus cost downgrade, we measured (full data + reasoning: `docs/aiw108-fable-opus-kalk-analysis.md`): **one plain Opus Kalk pass catches only ~34% of a Fable pass; two Opus passes where the 2nd is PRIMED with a Fable-mined shared-source-calque checklist reach ~92–93%** — and the recipe is **reproducible** (FR vs PT landed 225 vs 227 A-findings, Δ 0.9%). Mechanism: calques are source-driven (same EN/DE original → same trap in every target), so a checklist mined from a Fable pass on ONE sibling transfers as a high-recall probe to the others; Opus is a strong *executor* of a known checklist but a weak *discoverer* from scratch. **Decisions:** (1) Kalk *scanning* of the open languages (IT/JA/ZH) runs **Opus-only** with the enriched master checklist (2 passes; optional 3rd native-grammar pass for the residual ~8%). (2) **Fable is reserved for the two things priming can't fix: the initial discovery pass on the first sibling, and the TRANSLATIONS themselves** (a weak translation can't be rescued by a calque scan) — especially the distant JA/ZH. (3) When Fable tokens return, spend a *small* slice first on **calibration** (Fable on ~8–10 already-Opus-scanned FR/PT segments) to measure the true per-language Opus:Fable ratio and remove the ES-vs-PT language confound before committing the recipe.

**Temporal/coherence issues in the SHIPPED ed.2 (goal set S252, 2026-07-08).** MG's next big goal: **correct temporal/coherence issues (term re-explained as if new, result-before-question, dangling "as we saw" refs — all ed.2-restructure fallout) in ALL languages, then get all editions published.** Trigger: the FR coherence pass (`drafts/aiw108-fr-coherence-findings.md`) found 10 `structural` issues that likely sit in the shipped EN+DE ed.2 too. MG ordered author copies of that ed.2 and needs a detailed severity report to decide their fate → an authoritative coherence pass on the shipped EN (+DE) is the first deliverable (feeds AIW-109 + the author-copy decision). Fixes go UPSTREAM in EN/DE source → rebuild → re-propagate to translations (never per-language patches).

**S254 (2026-07-10/11) — MG directives + outcomes.** (1) **Language priority order** (MG): DE/EN → already-translated → partially-translated → open; MG then chose **skip-to-IT/JA/ZH** (DE/EN coherence + DE voice already shipped; **AIW-93 EN voice pass DEFERRED**). (2) **ZH un-paused, translated on Fable** ("fable is back" — reachability + cost-free probe confirmed). IT/JA/ZH all driven to **publish-candidate** (Kalk + whole-book coherence). Pipeline lesson re-confirmed: the 70ln+46ln Kalk passes overlap-cover the same text → ~15-20% of findings are twin-duplicates (not-applied = already-fixed-by-twin, spot-verify and move on); systematic CJK typography (em-dash `―→——`, half→full commas, straight→curly quotes for CJK content, chapter-numbering unify) is best fixed by targeted mechanical normalization, NOT per-finding Kalk. (3) **"Fix everything everywhere"** (MG): all wrong-fact/wrong-ref errors fixed in ALL 8 editions (neuron→85k, Ch.10→Ch.8, Leibniz→Ch.13, anosognosia=Ch.6, separators=45). **ed.2 print author copies are OK as friends/family giveaways WITH a corrigendum slip** → `drafts/corrigendum-ed2.pdf` (EN+DE). Style items (Coda re-narration, Ch.15 criticality re-intro, German-book ref) are NOT errors → ed.3 refinements. (4) **Next: final Fable review, DE+EN FIRST** (highest multiplier), then token-check → translations; each with current FMT paper + revised crucible predictions (P1/P2/P3, VM-tax) — flag mismatches, don't auto-rewrite published content.

## S255 (2026-07-11, WSL) — final Fable QA pass on all 8 editions; review-purpose correction; Fable-null sign-inversion owned

**Review purpose CORRECTED (MG, S255).** The S254 handoff framed the "final Fable review" around flagging book-vs-crucible *prediction mismatches* (revised P1/P2/P3, VM-tax). MG corrected the intent: this is a **last-line hidden-defect QA sweep** (factual errors, contradictions, broken cross-refs, coherence, prose tells, artifacts) — **NOT a theory revision**. Crucible results are at most optional upside ("could footnote: already confirmed experimentally in a model"), never a reason to touch published claims. Prediction-mismatch axis **dropped**.

**Sign-inversion error OWNED (S255).** I initially propagated a handoff/inbox framing that read the CRU-36 null as a *falsification* ("the book's criticality+closure sufficiency claim is contradicted; 'none has been falsified' is now dishonest") and briefed the first Fable reviewers on it — sharpening a third-hand summary I never verified. **Ground truth** (`crucible/docs/decisions.md` 2026-07-08): the null is **FMT-CONSISTENT, not a refutation** (mis-wired feedback on a homogeneous blob with no distinct self/world models); the **real Closure-1 loop DID real work** (closure ON ≫ OFF; recursion-specific per a read-only control); criticality computes (CRU-27); 2026-07-11 CS/CG PASS + gridworld all-green (preliminary, "no GO/NO-GO"). **Nothing falsified → the book's "none has been falsified" stands.** Lesson: reproduce cross-session theories against source before propagating (esp. before briefing subagents). Removed the inverted-framing `pending-aiw108-fable-final-review.md`.

**Execution.** 41 `claude-fable-5` reviewers (5/edition + an EN Ch.11/App-H probe), **all 8 editions**, disjoint ranges, each briefed with a source-shared cross-check + native-language-quality axis (Anglizismen/Kalke; CJK typography). **Zero content-gate refusals** (Fable handled consciousness-dense text throughout); zero agent failures on the confirmed model (one early ECONNRESET re-ran clean). Strong evidence the Fable content-gate is currently down and Fable is usable for FMT — but the agent roster still lists it "ON COST HOLD" (stale; MG re-enabled S254). Serialized per language (≤5 concurrent) per the S253 rate-limit rule.

**Findings.** Consolidated → `drafts/aiw108-cross-edition-qa-findings.md` (source-shared matrix w/ per-edition line numbers + edition-specific + verify-first). Detail: `drafts/aiw108-{en,de}-fable-final-review.md`. Fix handover → `docs/pending-aiw108-fix-all-editions.md` (AIW-109). **Verify-first:** Ch.5 citations *Hengen/Shew "140 datasets, Neuron 2025"* + *"Inbal Algom" & Shriki "ConCrit", N&BR 2026* flagged by every reviewer as possibly **fabricated** — WebSearch before any fix; if fabricated it's an MG-level issue (made-up citation in a published book). Newly-surfaced cross-edition content errors: **callosotomy misattributed to Sperry/Gazzaniga**; **Anton's syndrome assigned to ESM (should be EWM)**; **Wolfram credited with "five classes" (has four; 5th is MG's own extension)**; **Hawking/Bekenstein "didn't read each other's papers" (false + self-contradicting)**; **Bruno Gruber acknowledgment phrased as a completed life (he is ALIVE)**. BLOCKERs: FR L1088 raw English editor-note, FR L636/L554, PT L518 corrupted paragraph, English-labelled figures in every non-EN/DE edition. MG directive: document + handover + end this session; fixing is next session (AIW-109).

## S256 (2026-07-11/12, WSL) — AIW-109 fixes applied to all 8 editions; §0 cleared; MG model + review directives

**§0 verify-first CLEARED (reverses the S255 fabrication fear).** WebSearch confirmed the two flagged Ch.5 citations are REAL and accurately cited: **Hengen & Shew, "Is criticality a unified setpoint of brain function?", *Neuron* 2025** (a 140-dataset meta-analysis) and **Algom & Shriki, "The ConCrit framework…", *Neuroscience & Biobehavioral Reviews* 180 (2026)** — "Inbal Algom" is a real Ben-Gurion researcher, not a fabrication. No escalation. The IIT-pseudoscience citation WAS wrong (book said *Nature Neuroscience* 2025) → fixed to **PsyArXiv, 15 Sept 2023** in all editions. Kanzi (dance anecdote verified; ice-cream/sister unverifiable) and the Joscha Bach @Plinz quote → **MG confirmed both, KEPT** (Bach's quoted portions are verbatim-exact per MG's source paste; only the closing line is a faithful paraphrase).

**MG model directive:** translation careful-rewrites ran on **Fable** (MG explicit go — clears the roster's standing cost-hold for the session). DE rewrites on Opus (native-German-quality rule). **Final review split (MG): FABLE FIRST on the difficult/lower-resource half (IT/PT/JA/ZH), then Opus on the easy/high-resource half (EN/ES/FR/DE)** — difficulty judged by model language-capacity (CJK + lower-resource Romance = hardest; exact per-model per-language benchmarks unpublished, so estimated from training-resource tiers).

**MG aphorism directive:** the "a theory that claims X isn't a theory — it's a religion / a sales pitch" trope appeared 3×; MG: "three times the same sales pitch is NOT ok, remove at least 2" → **kept 1 (Ch.14), removed 2** (Ch.16 + Ch.17/appendix) in every edition.

**Execution:** EN+DE by Opus (main loop); ES/FR/PT/IT/JA/ZH by 6 Fable per-language agents against `drafts/aiw109-fix-spec.md`. All source-shared factual/artifact fixes + per-edition §2 + BLOCKERs applied and grep-verified; committed `1dd92e1c`. **Figures remain English-labelled** in the 6 translations (needs image-asset work → AIW-24). Final split review deferred to next session per MG (wind down + handover); divergence flags for the review are in `docs/pending-aiw109-final-review.md`. NB: I committed the fixes as a safety checkpoint — MG noted the commit was "unexpected" (global rule is commit-when-asked); for large verified deliverables the project's work-product-commit rule applied, but flag intent explicitly next time.

---

## S257 (2026-07-12) — AIW-109 final split review + figure localization

**Two-decades contradiction → fixed in all 6 translations.** The review found EN/DE correctly said "two years apart in origin" while ES/FR/PT/IT/JA/ZH all still said "two decades" — a flat internal contradiction with the same paragraph's 2003/~2005 dating. Applied under MG's "apply real fixes" scope (was old item #12, dropped from the canonical spec, but a genuine factual self-contradiction, not a stylistic choice).

**German-book self-reference → drop, don't rename (MG chose "reword all 8").** EN said "the German book's analysis of these syndromes"; in translation this rendered as "the German edition/version," ambiguous against the book's own German edition. Decision: follow the **DE precedent** — the DE edition already *drops* the citation ("Diese Syndrome zeigen vor allem eines…") — so deleted the self-citation clause in EN + the 6 translations rather than inject "my 2015 German book". DE unchanged. Cleaner, and it's the author's own established solution.

**Insect passage: aligned IT to the other 7** (restored "just ask any insect"). 7/8 editions deliberately keep the dry quip alongside the later empirical hedge; only IT (S256) had reconciled it away. Not a real contradiction — the quip is rhetorical, the hedge is the careful position. Kept the tension everywhere.

**Homunculi figure: EN-for-all-except-DE.** It's the Penfield & Rasmussen (1950) sensory/motor homunculus — a famous historical reproduction, ~35 dense English body-part labels, raster PNG. Reproductions conventionally run in English in translated science books; the per-language caption carries the explanation. Only the 3 *original* FMT diagrams (figure1/figure2/five-layer, all SVG) were localized.

**CJK figure rendering recipe (WSL).** cairosvg has no automatic per-glyph font fallback. For JA/ZH: copied Windows fonts (Yu Gothic, Microsoft YaHei) from `/mnt/c/Windows/Fonts` into `~/.local/share/fonts` (no sudo), set `font-family` explicitly per language at render time, and gave the ↻ (U+21BB) loop glyph — missing in the CJK fonts — a per-element `DejaVu Sans` fallback. Figure1's longer-translation overflow (right-edge cutoff, closure-label collision) fixed by geometry: right-anchor the edge labels, left-anchor the closure lines. Fonts are machine-local (not in git); committed PNGs are what the book build consumes.

## S263 (2026-07-14) — ed.2 build & ship (build-level typography)

**Build-level typography, not source edits.** The translation manuscripts must stay line-aligned (2475 ln) with EN, so per-language/format typography is applied at BUILD time, never baked into `.md`. Three pure/idempotent transforms in `scripts/typography_fixes.py` (moved out of tmp/ per MG "non-throwaway out of tmp"; tested by `scripts/test_typography_fixes.py`): FR-epub French punctuation spacing (narrow NBSP U+202F inside «» + before ;!?, NBSP before :), and CJK stress-emphasis→bold that is **content-aware** — only spans containing a CJK codepoint flip to bold; pure-Latin emphasis (*Nature*, *C. elegans*, book titles) stays italic. Empirical check first saved a wasted pass: pandoc `smart` ALREADY curls FR apostrophes, so only the guillemet/punctuation spacing was actually missing.

**Edition marker "Second" is PRINT-only; eBooks carry only © 2026 (MG S260, applied S263).** The First→Second flip lives on the print copyright page (`edition_line` in `build_book_pdf{,_de}.py`; `cfg["edition"]` in the two translation-interior scripts); eBooks never get an edition line. The marker is interior text, so it does NOT trigger a cover rebuild.

**Covers need no redo for this ed.2 (S263 spine check).** Spine = pages × 0.002252". Every cover's baked-in `pages` matches the freshly-rebuilt interior (EN 271, DE 299, ES 290, FR 299, IT 288, PT 288, JA 282, ZH 218) and no cover text changed — so cover art is only re-done next session if a review-driven interior change moves a page count or a cover defect is flagged (then AIW-60 QA). MG S263: after covers settle, EVERYTHING re-uploads (print + covers + eBooks).

**KDP margin overflow was the recurring bug, and the book pipeline had no gate (S264).** KDP rejected ES/FR/IT/PT twice: (H) long URLs/DOIs + long Romance words + slash-joined pairs don't line-break → text off the right edge; (V) the Appendix visual-hierarchy table is too tall for one page in translations → off the bottom (its 3+2 "spread" only triggered on the *English* header, so translated copies fell to a non-breaking `tabularx`). `build_book_pdf_de.py` was already immune (loose tolerance) — the fix (`\emergencystretch=4em`, `\tolerance=3000`, `xurl`, break-after-slash in `escape_latex`, and `xltabular` so tall tables split with a repeating header) had simply never been ported to `build_book_pdf.py`. Why the Fable + visual reviews all missed it: they SAMPLE pages; KDP checks every page; the book pipeline (custom LaTeX, not the gated `build-md-pdf.sh`) had no margin gate. Fix: new builder-agnostic gate `scripts/check_pdf_margins.py` (per-page, recto/verso-aware, H+V, CJK-hanging-punctuation-aware) — run before every KDP upload. Lesson generalized to `.claude/knowledge/publication-build.md` and routed fleet-wide via the cross-project inbox (MG: "other projects may also create pdfs").

**Translation covers carry the baked ISBN barcode, not KDP's auto-overlay (MG S264).** Amazon's auto-placed barcode doesn't line up with the reserved white box and looks awkward, so `build_translation_covers_print.py` now takes per-edition `isbn_pb`/`isbn_hc`, generates the EAN-13 barcode, and keeps it in the box (EN/DE already did this). MG fed the KDP-assigned 979-8 ISBNs live (table in `.claude/knowledge/kdp-specs.md`); **JA has no hardcover** (KDP limitation); ZH covers still pending its ISBN. DE eBook subtitle was also corrected to the canonical "Die Architektur von Bewusstsein, Berechnung und Kosmos" (the source line-3 h2 still carried the old evocative subtitle). ZH .docx TOC replaced pandoc's unreadable empty field with a real hyperlinked 目录 (30 anchors).

## S265 (2026-07-17, WSL) — triage of accumulated cross-project inbox items + policy record

**🎉 MILESTONE — the 8-language book is FULLY PUBLISHED (MG confirmed 2026-07-17).** AIW-109 + AIW-108 CLOSED. Live matrix = **21 SKUs**: EN, DE, IT, PT, FR, ES each as eBook + paperback + hardcover (18); JA as eBook + paperback (no hardcover — KDP limitation); ZH as a **Simplified-Chinese eBook listed under Amazon's "Traditional Chinese" category** (Amazon offers no Simplified category), no ZH print. **The per-language human-native reviewer gate — the long-standing "real blocker" — is CLEARED per MG.** End of a multi-month, multi-session translation+build+KDP saga (ed.2 → cross-edition QA → coherence passes → typography → margin/vertical-overflow gates → Fable final reviews → publish). The 2015 German monograph that sold zero copies now has a fully-published sequel in eight languages.

**ZH print PARKED (MG 2026-07-17).** No Chinese print planned at the moment → the ZH cover barcode (AIW-116) and the ZH-ISBN blocker are OFF the active list. AIW-116 marked done for all planned editions (5 langs baked S264). Reopen only if ZH print is scheduled. (ZH eBook/PublishDrive path is unaffected.)

**Metzinger — PERMANENT no-recruit policy (MG directive, social 2026-07-09; recorded in aIware S265).** DO NOT pitch, recruit, or invite **Thomas Metzinger** (metzinge@uni-mainz.de) to anything FMT-related; keep him off every active/planned outreach or pitch list. MG rationale: ignored MG ~3 decades; his only "response" to an outreach call was an automated advertisement; now sells esoteric life-coaching in retirement (no institutional weight). Policy: do what we can to NOT let him profit from FMT's success; if informed at all, inform only when it is too late for him to react (post-hoc). Deliberate personal exception to the "Standard-Model FOMO / recruit-the-theory-owners" play. Canonical: social `contacts.md` (Metzinger → ⛔ DO NOT RECRUIT) + social `docs/decisions.md` 2026-07-09. **Scope note:** this governs OUTREACH only — Metzinger remains a legitimate *citation* (SMT prior-art / lineage) in the paper + book (AIW-89/75/86/21/79 already cite him); do not strip citations. aIware grep confirmed no active Metzinger outreach exists here, so nothing to remove — this is a guardrail against future sessions adding him.

**AGI-26 "Artificial Phenomenology" track — assessed NOT VIABLE (S265).** Main AGI-26 paper deadline was **Apr 20, 2026 (passed)**; conference is in-person at SF State **Jul 27–30** (10 days out); MG cannot travel internationally. The CIMCAI curated-track Google form (t.co/Jf9qCoXe28 → docs.google.com/forms/…) returns 401 to automated checks so open/closed status is unverified, but the surrounding facts settle it: no realistic value in a remote/proceedings-only contribution to a curated in-person lineup MG can't attend. Recommendation: decline / let it moot. Not converted to a backlog item.

**Safron IWMT papers — ingest already DONE (not pending).** The inbox item ("MG downloaded 3 Safron papers, ingest next session") is stale: `literature/fulltext/` already holds `Safron2020.pdf` (IWMT), `Safron2022a.pdf` (274 KB = AIXI/FEP-AI/IWMT), `Safron2022b.pdf` (909 KB = G-SLAM) — sizes match the inbox item's files. Remaining Safron work = the IWMT↔FMT convergence note (→ AIW-119), not ingest.

**RIM REFRAMING — consciousness is the third factor of intelligence (MG directive, S265 2026-07-17).** MG generalized RIM: **motivation is not the third factor of the intelligence triangle — it is one *example* of a broader third factor, which is CONSCIOUSNESS (the effect at the apex).** Motivation becomes a sub-aspect; other consciousness-derived facets — **play inclination** (= AIW-110 free-modelling/play↔consciousness), **risk aversion/taking** (Wittmann & Hattrup 2004), curiosity, effort allocation, "etc etc" — also feed this third factor, unified by their common source (the conscious self-model steering the implicit↔explicit loop). **Effect:** RIM↔FMT unify — consciousness (FMT's subject) is the decisive third factor of human intelligence (MG already told Ettinger this, corr. Msg 30). This is *the* "RIM reframing" that was blocking the Wittmann email (AIW-118 unblocked). Full note + Wittmann/Schmiedek/COGITO-2 implications: `docs/rim-reframing-consciousness-third-factor.md`. Feeds AIW-81 (RIM revision) + AIW-118.

**BLOG-FIRST dissemination policy (MG directive, S265 2026-07-17).** "We can't keep updating the book on every new finding — the next book update may be half a year away." → **New findings go to the blog (matthiasgruber.com) + LinkedIn, not the book.** The book updates on a slow (~6-month) cadence; between editions, blog posts + LinkedIn posts carry new results. aIware writes the blog/technical content; **social owns LinkedIn posting** (route via cross-project inbox). Immediate queue (AIW-122): (1) two-dials/paper findings; (2) modelling-taxonomy (free-modelling = play) + VM-tax (book-ed.3 content, deferred → blog instead). Convergence notes (Safron/Laukkonen/Olinyk) also route here. Web presence catalogued in `docs/web-presence-inventory.md`.

**AIW-110 ratification #1 ANSWERED (MG S265 2026-07-17):** the P2 independent variable = **the substrate must be able to do FREE COMPUTE** — open-ended, general computational capability (the Class-4 / edge-of-chaos "capability" band crucible leans toward), not merely avalanche-σ or an edge-of-chaos statistical signature. Ratifications #2 (P2 dependent variable) and #3 (reconcile the two formalizations) still open — MG asked for plainer phrasing first.

**Web-presence tracking gap FIXED + lesson (S265).** I claimed the FMT paper §4.4 was the only public engagement with Seth, unaware a dedicated **published commentary** exists (Zenodo 10.5281/zenodo.20626675, blog, 2026-06-10) — AIW-117 was already done. Root cause: aIware tracking mirrored the repo, not the live web (matthiasgruber.com/blog has 6 posts; none tracked). Fix: `docs/web-presence-inventory.md`. **Lesson: before claiming "nothing is published on X", check web-presence-inventory.md.** Also corrected a false alarm: the v12 `.tex` port (olfaction §4.4, Passos §6.4, two-dials) IS complete — the earlier "incomplete" reading was a grep-count artifact (.md keeps its ref list inline; .tex uses bibtex).

## S269 (2026-07-25, WSL) — closure-maintenance "banked positive #1" DROPPED from FMT §8.9 + companion (data-integrity)

**A false positive rode from crucible's ledger into the paper — and this session reproduced it away.** The FMT master §8.9 first banked result, the companion §4.1, and `docs/crucible-evidence-ledger-digest.md` line 11 all claimed *"self-referential closure maintains an explicit model; a read-only control with identical decodability but no recursion fails → the maintenance is the recursion itself,"* citing crucible `experiments/closure_maintenance.py`. **Ground truth (ran the code, `scripts/verify_closure_maintenance.py`):** at the module's own research defaults (interference 0.5, delay 40, 5 seeds) closure ON−OFF ≈ **+0.08, 95% CI crosses 0** = null. The large advantage (+0.5–0.72) appears ONLY at near-zero interference (0.05) + long delay (40–80) = a trivial leaky-integrator effect a **linear delay-line matches** (crucible's own B0 gate G9: self-model ≯ delay-line). The crucible red-team (`cru40-design-redteam.md`) already ruled a rate-ESN positive *"triply-measured impossible"* and named this blob result the *correct negative to publish*. The "positive" was stale ledger/digest prose with no runnable code behind it.

**MG ruled: DROP result #1 entirely** (his stated option: "remove rather than discuss the null"). DONE + verified: FMT §8.9 `.md` (line 895) + `.tex` (line 1144) — dropped, four→three renumbered; digest line 11 — retracted with marker + root-cause note; companion — §4.1 dropped, ~25 §4.x cross-refs renumbered + audited (caught the §9.1 perception-mask null pointing at the wrong section); crucible tasked via cross-project inbox (correct its ledger row #1 + `decisions.md` positive, AND design a real *differentiated-substrate* maintenance experiment WITH MG — the red-team's endorsed path). Companion NOT published — method-fills + 6 citation checks + PDF + MG review remain; **Zenodo DOI HELD** (AIW-124).

**Lesson (both directions):** the aIware digest *mirrors* crucible's ledger; a false positive in the ledger propagated straight toward a permanent DOI. **Verify a banked positive against runnable code before any paper use** — the underselling risk (the digest's original reason to exist, S267) and the overselling risk are both real.

**Editorial call (MG):** do NOT label a result an *"honest null"* / *"honest half-result"* / *"honest scope"* in a manuscript. It is internal CRU-39 "banked is banked" jargon; in the paper it reads as editorializing, faintly defensive, and reviewer-bait. Report the result; drop the virtue word. Stripped throughout the companion this session.

## S274 (2026-07-28, WSL) — FMT salami-slice strategy: two desk-reject-resistant lanes; Lane B = "completing Kanai's ICCR"

The full FMT paper has **5 desk rejections / 0 peer reviews** — a gatekeeper signal, not a quality one. **Decision (MG): stop submitting the monster; cut two standalone-valuable slices, each routed to a lane where a single cold-editor "no" is least likely, and let the full paper live permanently as a cited Zenodo preprint.** Lane A = NoC special issue "Is There More to Consciousness Than Computation?" (anchor = the two-dials/time-dilation prediction — the one sharp falsifiable claim desk editors kept demanding). Lane B = JAIC "Assessing AI Consciousness" (an operational substrate-neutral AC detector — the "operationalize the architecture" every reviewer asked for). Rationale: the recurring desk-reject feedback (definition-departs / predictions-too-general / needs-integration) is itself the slicing recipe — each complaint becomes one of a slice's strongest sections. Anti-salami legitimacy: distinct central claim + distinct primary evidence per slice, both cite the preprint (not self-plagiarism).

**Breakthrough framing (MG called it a "breakthrough chance").** The JAIC EiC Kanai just published his own ICF/ICCR framework (arXiv:2606.15348), which explicitly leaves open exactly what FMT supplies: the consciousness-relevant intrinsic structure (§9.2), a structure-extraction method (§9.4), and grain-selection (§9.3). Lane B is therefore written as *completing* ICCR — FMT names the structure (closure-at-criticality), gives the detector, and answers his grain question with the two dials — **NOT** as a rival. Editor-diplomacy invariant: position as instantiation, never supersession. Full analysis + citations to pull: `drafts/kanai-iccr-vs-fmt-comparison-2026-07-28.md`. Drafting scheduled for the first session after 23:00 2026-07-28 via a Fable-agent team (AIW-130 P1).

## S276 (2026-07-30, WSL) — AIW-130 papers drafted; MG author-review correction on FMT framing

The two-slice Fable pipeline ran end-to-end (plan → cite-verify → draft → 8-reviewer adversarial review → refine → cross-paper gate → build). Both papers built to clean PDFs. **MG's author review: JAIC is good and adheres to FMT; NoC needs substantial revision.** Two corrections of lasting import:

1. **FMT framing (AUTHORITATIVE, MG verbatim):** *"consciousness requires free computation and arises when a self model confuses itself with the being it occupies… the integration of information from implicit models to explicit system and feeding them to the self model is what makes conscious experience."* → Criticality/free-compute is the **necessary enabling** condition; consciousness is **constituted** by the implicit→explicit→self-model integration / self-conflation, NOT by criticality-deployment. The NoC draft drifted into an over-claim — *"criticality arises only in service of conscious self-modelling"* / *"near-critical iff conscious"* (introduced by the refine agent) — which MG rejects as unfounded and killable by unconscious heavy modeling in sleep. The defensible claim is **one-directional only**: no criticality → no consciousness (necessary), but criticality does NOT imply consciousness. To be promoted to the theory-framing docs.

2. **Names-out advisory is audience-scoped (not blanket):** keep Wolfram/Metzinger out of consciousness-science/neuro/philosophy venues + outreach, but they are fine in information-sciences/CS/complexity venues (e.g. the computational companion cites "Wolfram Class 4" by design — that readership differentiates it). Ingested to `.claude/knowledge/neuroscience-communication.md`.

**Process lesson:** an 8-agent adversarial Fable review + the orchestrator both MISSED the AI-tell/condescending-meta register (a recurrence) AND the theory over-claim (which a refiner *introduced* while fixing an unfalsifiability blocker, with no theory-owner check). Prevention proposed (next session, MG consent): a theory-fidelity pass + a strengthened AI-tell sweep targeting meta-commentary-about-strategy. Full handover: `docs/pending-aiw130-noc-revision.md`.


## Greek (el) translation build + review-order (S278, 2026-07-31)

- **Reconcile-before-scan order (deviation from the nl/ja SOP Kalk→coherence→reconcile):** when an interior review already exists, apply it FIRST — its line numbers are only valid against the current manuscript, its fixes are quote/term-based (line-shift-immune), and it cleans the text so the fresh Kalk/coherence passes don't re-flag known drifts. Adopted for el; reasonable default for ko.
- **Greek interior font = P052 (URW Palatino), NOT TeX Gyre Pagella.** Pagella (the Latin editions' font) has ZERO Greek coverage — it compiles but renders Greek as tofu. P052 is the same Palatino/Palladio family WITH full Greek, so the Greek edition keeps the series' typographic identity. Build = xelatex + fontspec + polyglossia(greek) for hyphenation; italics KEPT (Greek has them, unlike the CJK editions which convert italic→bold). `tmp/build_translation_interior_el.py`.
- **Verify subagent-produced manuscript edits independently.** The Opus reconciliation subagent returned a self-validated fixes JSON; applied only after an independent recount + substring-collision check (`apply_interior_fixes.py`). Never trust a subagent's own "0 problems" on bulk manuscript edits.
- **Number-format for el is UNRESOLVED (MG call):** the culture guide said "keep numbers as the EN has them," but the native-editor interior review wants Greek convention (period-thousands / comma-decimals). Held, not silently reconciled — flagged to MG (`interior_fixes.json` HOLD entries).

## S286 (2026-08-05, WSL) — FMT v14 three-principle restructure applied; review-format directive

**Phase 0 settled by MG.** §3.7 becomes **"Criticality: Signature of the Computational Regime"** — the compromise that keeps the searchable word first while stating the relation rather than correcting it later. The decisive argument was countable: "criticality requirement" occurred 21 times, so *keeping* the old headline was the high-correction-cost option, not the low one. Abstract takes **variant B** (the claim leads, three principles as the compression in ¶2) — FMT's five desk rejections were format and affiliation (AIW-106), not lack of formalism, so an abstract opening on three abstract principles gives a hostile editor a faster exit than one opening on consciousness. Variant A survives in `drafts/aiw138-abstract-variants.md` as the formal-venue variant.

**Reading-order fix the written plan did not anticipate.** The plan places P1 in §3.7, P2 in §3.3 and P3 in §3.4 — so a reader meets "Principle 2" twenty pages before "Principle 1". Resolved by stating all three **once, in order, at the head of Section 3** with section pointers, which turns the in-section labels into back-references. Each of §3.3/§3.4/§3.7 then opens with its own principle in bold. This is a structural editorial decision, not a mechanical one, and should be preserved through later revisions.

**The demotions are a claim about derivability, not a retreat.** New §6.0 states, once, why redirection, permeability and forking are consequences: redirection is what an input-driven generator does under input substitution; permeability is forced because explicit models are generated *from* implicit ones (zero permeability = no explicit models at all, hence nothing for P3 to apply to), with only its *variability* contingent; forking follows from P1 directly. The corresponding cost is honest and stated — each §8 prediction chain is now one step longer, so the chains are written out explicitly rather than compressed. A theory that derives more from less carries the larger burden and should say so.

**MG standing directive on review format ("always 2"): change-tracked HTML is the DEFAULT review artifact for paper revisions.** Do not offer the PDF-vs-HTML choice again. PDFs are for layout and typography review only. Persisted to `.claude/knowledge/publication-build.md`; generator is `scripts/review_changes.py`.

**Two pre-existing defects surfaced by the build, neither caused by the restructure.** (1) `tmp/test_content_integrity.py` — the Phase 5 gate the v14 plan depends on — **did not exist**, and neither did any of the five review-HTML generators that `publication-workflow.md` §4 tells sessions to *reuse rather than rewrite*. All were lost with a `tmp/` cleanup. Rebuilt into tracked `scripts/`, which now contradicts `CLAUDE.md:73`; filed as `AIW-145` for MG rather than resolved unilaterally, since rule changes need consent. (2) The committed canonical `paper/full/latex/paper.pdf` is **105 pp while its own committed `.tex` builds to 123 pp** — the canonical PDF is ~18 pages behind its source. This nearly produced a false claim that v14 added 21 pages; it adds **3**. **Lesson: never compare against a committed PDF without first checking it against a fresh build of its own source.** The `.bbl` was likewise stale — 35 citations present in `references.bib` had never been bibtex'd in.

**Print-order addendum (same session).** MG ordered **500** SJÄLV booklets, not the 1000 recommended — €136.67 net at the 500-copy uncoated tier, €164.00 gross paid. WirmachenDRUCK then held the order at preflight for **unembedded fonts**: `build_booklet.py` draws with ReportLab's base-14 faces, which ReportLab never embeds, on all 12 pages. Fixed by converting text to vector paths (the shop's own suggested alternative) rather than embedding a substitute typeface, **because the artwork was already signed off and a different embedded face would have changed the glyphs and reopened that approval**. The general lesson is now a standing pre-flight rule: *any PDF going to a commercial printer must be checked for unembedded fonts before it is sent*, and it bites ReportLab/weasyprint/Cairo output specifically — LaTeX embeds by default. Verification that a fix of this kind is safe has to cover appearance, geometry **and** any machine-readable element: the QR was re-decoded at 400 dpi to confirm it still resolves to the Zenodo concept DOI.

## 2026-08-06 (S289) — the SMoC argument map: sourcing, and what earns a point

**A point on the map is a POSITION, not a person.** (MG delegated the call: *"not sure you decide"*.) Three
reasons, in order of weight: the axes — *how much is left outside the account* and *how much the substrate
constrains* — are only defined over **accounts**, and a person is not an account; the S288 reading convention
("plotted as the theory describes ITSELF") has no person-level counterpart, because a canonical text is fixed
and citable while a living researcher's current view is neither; and the citation standard set the same day is
a **text** standard, which works for positions and cannot work for people. Consequence, declared on the figure
so it reads as a design principle rather than an omission: work that *formalises or compares* positions —
Kleiner's programme — sits a level above these axes and does not plot.

**A point earns its place by informing, not by existing**, and there are two ways to inform: spread the field,
or **contest FMT's own claimed gap**. The second matters more and the audit must not duck it. Applied:
Blum & Blum's Conscious Turing Machine is **not placed** (by its own abstract it is built on GWT; it lands on
top of the workspace family and adds crowding, not separation — and its residue coordinate has no quoted
source); Atmanspacher's dual-aspect monism is **not placed** (it would need a second `not applicable` band and
turn D9 from a rare principled refusal into a general escape hatch); **Kanai's information-generation theory
IS to be placed** — *"internally generate representations of events possibly detached from the current sensory
input … constructed by generative models"* is FMT's R2 rung in other words, making it the nearest rival to the
region the map calls unoccupied. **Leaving it off would be self-serving in exactly the way §0.2 warns about:
the "specific and unoccupied position" claim is only worth something if the position most likely to falsify it
is on the chart.**

**`Biological naturalism` moved 0.48 → 0.28** on Searle's own text (*Why I Am Not a Property Dualist*, JCS
9(12)): consciousness is *"causally reducible to brain processes"*, it *"does not name a distinct, separate
phenomenon, something over and above its neurobiological base"*, and *"the impossibility of an ontological
reduction … does not give it any mysterious metaphysical status."* Not 0, because one thing does stay outside
by his own account — *"a complete description of the third person objective features of the brain would not be
a description of its first person subjective features"* — but that is a claim about **description format**, not
an unexplained phenomenon. **Side effect worth more than the correction: the map's top-right quadrant is now
empty.** Nobody holds *"the substrate is nearly everything AND the account explains nearly none of it."* That
is a fact about the field, and an empty region of a coordinate system is information the same way a blank in
the rung chart is.

## 2026-08-06 (S289) — durable build scripts live in `scripts/` (AIW-145, MG-signed-off wording)

`tmp/` is throwaway; anything that would be missed if lost belongs in tracked `scripts/`. MG approved the exact
`CLAUDE.md` replacement text, so the migration ran: 9 scripts moved, the Build Infrastructure table rewritten
against what actually exists, and 11 tracked scripts made machine-portable (hardcoded `/home/jeltz/aIware` →
`Path(__file__).resolve().parent.parent`) — **a tracked script that only runs on WSL is the same defect one
level down.**

**The rule paid for itself immediately, in both directions.** Moving `test_build_rim.py` out of gitignored
`tmp/` ran it for the first time in months and it failed against the real RIM paper: **9 bibitems with 3+
authors carrying a two-author in-text label, in a paper whose preprint is already public.** Left red on
purpose — the test is right and the paper is wrong, and marking it `xfail` would be the exact move the rule
change exists to prevent.

**And a correction to my own claim, kept because the method matters more than the fact:** I recorded four
missing scripts as unrecoverable *because `tmp/` is gitignored*. That reasoning was wrong — they had been
force-added and were deleted in commit `09755595` (2026-02-25), and all four came back from `09755595^`.
**`git log --all -- <gitignored-path>` before declaring a `tmp/` file lost.** The same shape recurred an hour
later with `AIW-133`, recorded as *BLOCKED on the PDF* while the PDF sat in gitignored `literature/fulltext/`,
downloaded but never indexed. **A gitignored file is invisible until something indexes it — so look before
declaring it missing, and index it the moment it arrives.**

## 2026-08-06 (S290) — Schoff's *Cosmic Compiler* is not cited in SB-HC4A (AIW-133)

MG flagged it as *"short, strange, but probably correct."* Half of that holds: its one load-bearing move —
the **Paradox of the Rule**, that a state of absolute nothingness must nonetheless *enforce* a prohibition on
existence, and an enforced prohibition is structure — is a genuinely different route to the thing SB-HC4A
§3.1 currently just concedes (*"I accept it as Axiom 1: something exists"*). But as written it turns on an
equivocation, `(C = 0) = C_null`, sliding between *nothingness enforces a prohibition* (presupposing an
enforcer — the category error) and *it is a modal truth that nothing exists* (needing no constraint at all).

**Three reasons not to cite, any one sufficient:**

1. **Axiom II makes non-deterministic agency a load-bearing law of nature.** That is SB-HC4A's Class 5,
   reinstalled as a premise, in the one place §3.2's declared substrate determinism cannot allow it — and it
   contradicts the consciousness lane's own settled position (didactic Pattern 8: the felt choice is the same
   delayed-observer illusion as *"I chose to move my arm"*). A citation would damage both papers at once.
2. **Its terminal Φ_Ω is a boundary term**, which the formalization's bi-infinite cyclic fixed point
   explicitly precludes. The two cosmologies are incompatible at the level of their fixed points.
3. **Provenance.** Self-published, no journal, no DOI, no peer review; three external references, none cited
   in the body. Next to Bekenstein, 't Hooft, Penrose and Wetterich it reads as a signal about the author's
   filtering rather than about the claim.

**The redirect is worth more than the citation would have been.** Albert (2012) — *already in SB-HC4A's
reference list* — makes the same structural objection to Krauss: the proposed void smuggles in structure.
Strengthening §3.1 by engaging Albert directly buys the argument with real provenance and none of the cost.

**Kept as calibration:** Schoff is a clean instance of SB-HC4A's own Weak Point 5 (§9.5, the cognitive
ceiling) — a cosmos that exists *in order to* build the hardware that proves the theorem is a
symmetry-detecting mind projecting its architecture onto the universe. Congenial-sounding external
convergence is exactly what §9.5 should be pointed at first. Full analysis:
`docs/aiw133-schoff-cru-cosmology-analysis.md`.

## 2026-08-06 (S290) — RIM stays a psychometrics paper; free modelling is the mechanism, not the pillar (AIW-126)

MG's ruling when the third-pillar reframe was put to him as a positioning question rather than an editing
one. The third component keeps the name **Motivation** in K × P × M. Free modelling supplies the *mechanism*
underneath it and does not replace it, because the evidential thread and the explanatory thread are different
threads (didactic Pattern 28): a *Journal of Intelligence* reviewer can measure NFC, TIE, grit and COGITO
daily effort, and nobody has an instrument for free modelling. Making consciousness the pillar would strip
§7.2 of its measurement anchor in the units the target audience uses — after three desk rejections, on a
thesis Wittmann recommended and Schmiedek independently converged on.

**Corollary — do not introduce "free modelling" as a novel term to that audience.** Psychology already names
the phenomena: mental simulation and prospection (Schacter & Addis), mental models (Johnson-Laird),
metacognition (Flavell), self-regulated learning (Zimmerman), scene construction (Hassabis & Maguire),
positive-constructive daydreaming (Singer), Openness vs Intellect (DeYoung). Three of those are *already
cited in the paper*. What is unclaimed is the **integration** — that these are one capacity, that it is what
the Motivation component measures, and that its absence is why current AI systems do not self-develop.

**MG correction, 2026-08-06 — free modelling is an operation, not a location.** It is instantiated per
modality and per domain, in whatever substrate holds the content being modelled. So aphantasia is a single
dissociation of the *visual instantiation*, not a test of the construct, and "amodal" is the wrong repair
because it predicts one dedicated network. The diagnostic case is the converse: **a condition that degrades
several modelling kinds equally would localize the generic modelling structure** (Hassabis & Maguire's
amnesics are the standing candidate; aphantasics' weakened episodic memory complicates it).

The psychometric consequence is what makes the correction load-bearing rather than merely accurate: if the
construct is instantiated per modality, **any single measure of it is a modality projection** — which is the
same argument the paper already makes twice (NFC vs TIE as measurement-context projections in §3.1; Brunswik
bandwidth attenuation in prediction 7). It converts the aggregation prescription from a statistical fix into
a mechanistic one, and hands the prediction a sharper falsifier: aggregating across *modalities* should raise
convergence more than aggregating the same number of occasions *within* one modality.

**MG refinement, same day — the aphantasia/episodic-memory link is expected, not a complication.** Vision is
the dominant sense, so it is also the instantiation most co-recruited by other modelling kinds; knocking it
out degrades episodic reconstruction without any of them being one network. **This sharpens the criterion
recorded above rather than weakening it, because it supplies the discriminator the criterion was missing:**
a deficit that hits several modelling kinds *equally* is ambiguous between (a) damage to the generic
modelling structure and (b) loss of a heavily shared modality. The two are separable by proportionality —
a **shared-modality** lesion degrades each kind *in proportion to* how much that kind recruits the lost
modality, while a **generic-structure** lesion degrades them *independently of* their modality loading. So
the search target is not "a lesion that impairs several kinds" but "a lesion whose damage profile is flat
across modality loading." Relevant to the crucible/FMT lane, not to RIM.

---

## S292 (2026-08-07) — RIM published as v3; the citation gate exists; two rulings from MG

**RIM v3 is public.** Zenodo version DOI `10.5281/zenodo.21841307`, concept `10.5281/zenodo.20125096`.
Published against RIM's own deposit via `ZENODO_CONCEPT_DOI` — `zenodo-upload.sh` defaults to the FMT
concept DOI and would otherwise have appended a RIM PDF as an FMT version. Dry-run first, always.

**MG ruling — RIM C5, the NFC/TIE dissociation.** Route (a): restate §3.1 as the *between-trait* contrast
Schweitzer et al. (2025) actually test, cite Woo et al. (2007) for the intercorrelation, leave the abstract
unchanged. The within-trait claim ("NFC correlates primarily with Gf") was false — both traits load more on
Gc — but the contrast between the traits is real and significantly tested, so the unity-of-motivation claim
keeps a correctly sourced empirical illustration.

**MG ruling — the achievement→motivation asymmetry is expected, not a tension.** Vu et al. find the pooled
effect of achievement on later motivation about twice the reverse. MG: achievement must overcome the
resistance to new behaviour in order to produce repeatable achievement, while motivation is balanced against
overmotivation and energy waste. A recursive loop needs both directions non-zero, not a particular ordering,
so the earlier framing of this as a concession was wrong and was removed. A psychometric reason points the
same way: in a cross-lagged design achievement is the broad, reliable variable and motivation the narrow
one, so the path *from* motivation is attenuated harder than the path *to* it — the paper's own §7.2
Brunswik argument.

**Falsification thresholds are content, not formatting.** Prediction 7's criterion read "at or below the
currently reported range", and the real range (von Stumm & Ackerman, 0 to .58) *includes* the *r* ≥ .50 the
model requires — the criterion cancelled itself. Re-anchored to the reported average of .30. Correcting a
cited number can silently move a falsifier; check what the number is load-bearing for before changing it.

**A citation gate can only mechanise existence, and existence is not the whole defect class.** `AIW-170`
resolves every reference against Crossref/arXiv once and gates offline thereafter. It caught three chimeras
independently. It could not have caught Frank — a real author cited for the *wrong work by the same author*
— and it cannot catch a sentence that misreports what its source says. Claim↔source agreement stays a human
step, by design; the gate exists to spend that human attention where it is needed.

**Verification survives re-verification.** `--update` originally overwrote `verified-manual` rows, silently
discarding hand-checking of every book and chapter Crossref cannot adjudicate. Human verdicts now outrank
machine ones; only a changed fingerprint retires them.

**The whole-paper review earns its rule.** Scoped to the defect list, the RIM pass would have shipped a §3.1
whose *mechanism* paragraph still asserted the mapping the *data* fix had just contradicted, an uncited
Binet claim, two more AI-tells, and a disclosure naming a superseded model version. None of those were on
any list.


---

## S293 (2026-08-07) — cosmology repaired; Axiom 1 argued; four MG rulings

**"Bekenstein saturation" is renamed "holographic saturation" throughout (MG-confirmed).** The property
the model needs is saturation of the *area* bound, which is 't Hooft (1993) / Susskind (1995), covariant
form Bousso (1999) — not the Bekenstein bound, which is S ≤ 2πkER/ħc, energy × radius, whose rigorous
form is a relative-entropy statement (Casini 2008; Longo 2024; Kudler-Flam et al. 2025). §5.2 Step 1 now
separates them and identifies the one place they coincide: the threshold of gravitational collapse, which
is exactly where horizons sit. **Do not merge the two again.** A side benefit: §8.1 now uses the
Bekenstein bound for what it actually says, which strengthens the energy–information section rather than
weakening it.

**Critical 4 was repaired against the paper's own prior claim.** §5.6 had derived baryon and lepton
number conservation from boundary information while §5.7 identified particles with (M, Q, J) no-hair
boundaries — the standard argument that B and L are *not* fundamental. The repair withdraws the
derivation: the model now predicts B and L are approximate, which agrees with electroweak sphalerons
(Klinkhamer & Manton 1984) and with the absence of exact global symmetries in quantum gravity (Harlow &
Ooguri 2021). A framework that produced exact baryon conservation from a horizon would have been in
conflict with black hole physics; this one is not. The rule this instances: when a repair forces a choice
between an internal claim and established physics, the internal claim goes.

**Heat death reaches saturation by the interior emptying, not by its contents climbing.** The old
mechanism had gravitational collapse and mergers drive interior entropy up to the horizon value. The
numbers forbid it — S_obs ≈ 3 × 10¹⁰⁴ k against S_CEH ≈ 2.6 × 10¹²² k (Egan & Lineweaver 2010), eighteen
orders, and collapsing every remaining baryon does not close it. The de Sitter horizon saturates the
holographic bound by construction, and the interior contribution falls to zero. Same conclusion, opposite
direction, and it no longer half-retracts itself two paragraphs later.

**`AIW-174` is a conditional derivation and must stay labelled as one.** Information causality's
inequality and the holographic bound on the shared locus are *the same inequality* once *m* is read as
locus capacity rather than a transmitted-bit count — so nothing needs proving between two principles.
What is owed is one **single-locus decoding postulate**, which is §5.2's single-surface ontology applied
to entanglement, a premise the paper already holds for reasons unrelated to Bell. The Oughton & Timpson
objection (IC's recovery of Tsirelson is Shannon-specific) is answered because the measure is *inherited*
rather than chosen: the rigorous Bekenstein bounds are α = 1 relative-entropy statements, quantum mutual
information is a relative entropy, and on the protocol's classical registers it reduces to Shannon by
restriction. **Do not upgrade §6.5 to an unconditional claim**, and do not re-attempt the
communication-complexity route (van Dam; Brassard et al.) as independent support — it fails at the same
joint, because a capacity bound limits the *density* of nonlocal resources per unit area, not the
strength of one locus.

**Axiom 1 is argued, not conceded — and the argument is MG's.** The session's initial recommendation was
to concede that "nothingness is not a possible state of affairs" is contested and load-free. MG rejected
that and supplied a better argument, which is now the spine of §3.1: any assertion that nothingness is
possible must either locate it or not. **Located** — fixing it relative to what exists implies a
separation, hence a dimension, hence a position, hence a property; vacuum decay and the empty possible
world are instances, and the Cambridge-property objection fails because occupying temporal or spatial
order is a determination of what a thing is. **Unlocated** — the only form that stays true to the name —
and the claim becomes "nothing, everywhere and everywhen", refuted by the existence of whoever asserts
it. There is no third form. An independent epistemic line runs alongside it: observing a state of affairs
requires standing in a spacetime relation to it, so nothingness is unobservable in principle and the
burden falls to whoever claims the exception. **Do not re-open this as "arguable".**

**Publishing SB-HC4A waits for a clean citation gate (MG).** The paper's content is finished; the 17
remaining reference verifications are the blocker, by choice rather than necessity — zero are known
wrong. The reasoning MG accepted: RIM shipped a fabricated citation through three sessions, and
"unverified" is precisely the state those were in.

**Two rulings on the author's own works.** `Gruber2015` is **2015** — the 2016 Lulu printing changed
cover art and typographical errors only, so the priority claim stands; the cosmology entry had drifted
from RIM's, which already recorded this, and both now match. `Gruber2026b` was cited as a bare
"Manuscript." and is now **published** on Zenodo, concept DOI `10.5281/zenodo.21843693`.

**The whole-paper review earned its rule a second time.** Scoped to the artifact rather than the backlog,
it caught five defects no backlog item pointed at — the abstract still asserting the mechanism Critical 5
had removed and claiming cyclic renewal without its conjecture hedge, the conclusion repeating both plus
saying the termini are "reached in finite proper time" when §5.3 exists to correct exactly that, §5.4
claiming §8 "establishes" information conservation while §8.1 flags it as a weak point, and a dropped
"large classes of" qualifier that turned a scoped Wetterich theorem into a universal one. Every one sat
in text that no open item mentioned.

**Three tooling defects, all of the same shape: silent state that outlives its justification.**
`verify_references.py` carried a human `defective` verdict onto *repaired* entries without checking the
fingerprint, so a fixed reference would have blocked the build forever citing evidence about wording no
longer in the paper. `zenodo-new-record.py` carried another paper's title and abstract hardcoded, so
depositing anything else would have minted a permanent public DOI under the wrong identity. And
`build_cosmology_pdf.py` overwrites the canonical PDF *even when it reports FAILED* — while
`git checkout HEAD --` restored only a 131-byte LFS pointer for that path. All three are fixed, the first
two test-first; the third is documented in `publication-build.md` because it is inherent to the script.

## S295 — 2026-08-08 — publishing cosmology, and what the link audit exposed

**`Gruber1968` replaced rather than defended (MG-decided).** The acknowledgment credited Bruno J. Gruber
via *Topics in Mathematical Physics* (Gordon and Breach, 1968), which appears in **no** bibliographic index
— Crossref filtered to 1965–73, OpenLibrary, DBLP, WorldCat, open web. MG chose (option 1 of 3) to swap in
the 1968 chapter that does resolve: *On locally isomorphic groups and Cartan-Stiefel diagrams*, in
Ramakrishnan (Ed.), `10.1007/978-1-4899-5424-4_1`. Rationale: same year, same subject, and it preserves the
career span the sentence implies. MG holds *Symmetries in Science* vols 1–10, but that series begins in
1980 — the 1968 item was never going to be in it, and the rest of the printed works are not retrievable.
**This was MG's call precisely because it is his uncle's bibliography and his own acknowledgment.**

**The existence gate did not exhaust the defect class on its first pass — and that is the point.** S291's
adversarial sweep found five cosmology reference defects; S293 found a sixth; S295 found **three more**
(`Boyle2018` missing its middle author, an `Elze2020` chimera, the unfindable `Gruber1968`) while clearing
the last 17 `needs-review` rows. Two of the three had survived the S293 whole-paper review because the
sentences citing them are *true of the work the entry was confused with*. Conclusion carried forward:
clearing the backlog of unverified references is not bookkeeping — it is where the remaining defects live.
`MAX_UNVERIFIED` is now **0** and may never be raised.

**Standing rule: publish the CONCEPT DOI, never a version DOI.** Every stale link the audit found was a
version DOI that had been correct on the day it was written — the README's RIM link pinned to v2 while v3
was live, its CMB link pinned to v1, and the deployed FMT wiki serving a March version eleven releases
behind. A concept DOI follows new versions automatically and cannot go stale. Applies to the README, both
web properties, ORCID, and any outreach material.

**Public surfaces must be audited against the paper, not just for dead links.** The README carried
"Bekenstein saturation" — the term S293 corrected as a misattribution, appearing **zero** times in the
paper — and claimed the trimmed FMT paper was "awaiting reviewer feedback" five months after it was desk
rejected. The FMT wiki claimed to be "based on two **peer-reviewed** preprints" when neither has ever been
peer reviewed. None of these is a broken link; all three are false statements a hostile reader finds first.

**MG's Culik→vacuum-instability inference was correctly withdrawn.** Undecidability of CA classification
(Culik & Yu 1988) is a property of the *classification problem*, not of any automaton — ¬∃A ∀c, where the
vacuum conclusion needs ∀c ¬quiescent(c). §2.3 already draws the epistemic conclusion and stops, and §3.2
eliminates Classes 1–2 *empirically* rather than algorithmically, which is why the result costs the model
nothing and can pay for nothing. **§3.1's first horn already yields "the vacuum is not nothing" without
needing instability**, and is therefore not hostage to where the electroweak vacuum falls on the stability
boundary. No paper change.

**Purge to the Recycle Bin, not hard delete (MG).** And **leave every Desktop book artifact untouched** —
`SIM-6` is mid-flight at edition 4 of 11, `SIM-1` is an open KDP cover rejection, and the July hardcover
builds are the only hardcover copies on this machine. What a purge *excludes* needs the same scrutiny as
what it removes: two files that pattern-matched as ours were third-party reference papers.

## S296 (2026-08-08) — the CRU-81 package placed; two Fable theory reviews

**All five CRU-81 drafts are placed in the FMT master (`AIW-177` closed).** A#2 and A#6 close the audit
gap crucible found; A#7/A#8/A#9 are new for v15. Crucible's audit was verified independently before any
edit — the master's banked paragraph did name exactly First/Second/Third (A#4/A#5/A#3), A#2 and A#6 were
genuinely absent from the master and genuinely present in the companion (§4.4, §4.5), and withdrawn A#1
leaves no residue. **The gap really was two rows, not six.**

**The seam was taken, and the ordinals were not restarted.** Eight numbered results in one paragraph is
too many for a reader, and crucible's proposed break — mechanism-demonstration (A#4/A#5/A#3/A#2) vs
architectural-cost (A#7/A#8/A#9) — is well motivated: the second group shares a substrate, a currency and
a form of argument. But the ordinals run 1–8 unbroken *across* the paragraph break rather than restarting
at "First", so that a reviewer citing "the seventh banked result" is unambiguous. Two competing
First/Second/Third runs in one section would have been the cheaper edit and the worse paper.

**A routed draft is not a verified draft.** Crucible's Draft 2 stated *"operand decodability of roughly 20
to 45"* — that is the **delay window** presented as the decodability figure. The source has decodability
0.63–0.77 against chance 0.50 across delays D=20–45. Every number in all five drafts was checked against
its source doc before placement, which is the only reason this did not ship into a published master. The
standing lesson: **peer-routed text carries the routing project's confidence, not its verification** — the
receiving project owns the numbers it prints.

**Draft 5's optional date-provenance footnote: declined for the master, routed to the companion.** Not a
judgement about the argument, which is sound. MG's own division of labour — *the FMT lists it, the
companion explains it and goes into detail* — puts pre-registration chronology on the companion's side.
The same reasoning kept the NOT-ADJUDICABLE label out of the master. Applying MG's rule mechanically is
the point: it decides these cases without re-litigating each one.

**The master now lists three results the companion does not yet explain** (A#7/A#8/A#9), which inverts the
usual direction of the gap. Flagged to crucible rather than silently absorbed.

**Fable review — operationalization (MG's question).** MG asked whether operationalization is just saying
precisely what verbal theories say sloppily, and whether an implementation is therefore the best possible
operationalization. Verdicts: the deflationary claim is **right about most of the field and wrong as a
definition** — formalization's value is *exposure*, not expressiveness; words cannot be wrong in a provable
way, and that is their defect. The supremacy claim **over-reaches**: an implementation guarantees
reliability but not **construct validity** (Cronbach & Meehl 1955), and CRU-58 is the in-house
counterexample — `closure_enabled=False` was precise, reproducible and numeric while measuring closure
*location*, not closure *presence*. The surviving superlative: an implementation eliminates procedure-slack
and thereby concentrates all remaining risk into the word-to-variable-name seam, where it becomes
*attackable* — Φ's validity disputes ran 20 years, the knob's ran weeks. **On MG's own criterion FMT's
formalism is not currently better than Φ — it is earlier than Φ**, and the §1.3 deferral complies with the
criterion's purpose but not its letter. Note: `drafts/aiw-operationalization-review.md`.

**Fable review — AIW-174 in entanglement-wedge language, and it found a refutation-shaped defect.** The
single-locus decoding postulate read **distributively** (each wing separately decoding the locus) *is a
local hidden-variable model* and yields CHSH ≤ 2. Jointness is therefore not a nicety of phrasing but
load-bearing, and any future statement of the postulate must carry it explicitly. Second finding: in
established holography a Bell pair's ebit sits in the **S_bulk correction term, not the area term** — so
standard AdS/CFT does not area-meter single-pair correlations at all, which is where the postulate's real
cost sits. EWR does **not** entail the postulate; at pair scale the connectedness condition *is* the
conjecture. Structural result worth keeping: intra-quantum EWR **cannot** non-circularly deliver Tsirelson,
because Hilbert space already contains it — so the entanglement-wedge form is the postulate's *consistency*
home and the device-independent skeleton is its *derivation* home. §6.5's conditional status is unchanged.
Note: `drafts/aiw174-entanglement-wedge-postulate.md`.

**MG's ruling on the cost functional: without an architect and an electricity bill, cost becomes
SIMPLICITY, via Occam's razor.** This is the answer to the gap that blocks the whole cosmos-transfer
thread — crucible's results are cost-*optimality* facts, and cosmology has no designer and no energy
budget, so nothing obviously occupies the cost role. MG's move is stronger than a patch: a connectome's
synapse count is essentially its description length, so wiring cost was always a **proxy** for
description complexity, while in holography `A/4ℓ_P²ln2` **is** a bit count — area *is* entropy *is*
description length. The two cases may have been measuring one quantity in different units.
**The epistemic/physical brake was raised and MG CORRECTED IT — the correction is right and is recorded
as the position. State the correction precisely, because it drifted once already:** what is only
partially true is **that confusing Occam's razor with a physical rule about the universe is a mistake**.
The partiality attaches to the *error-attribution*, not to the statement as a whole — the epistemic→
physical slide is **not simply a category error**, it is a partly warranted inference, because the
razor's working already presupposes a structural fact about the world. (The earlier draft of this entry
recorded it as "the flat version is only partially true", which misplaces what is being qualified.)
MG: *the razor carries the assumption that the universe is logical in a
specific way; if the universe is so logical as to let the razor work this well, it prefers clean code,
and that means the universe is as simple as it logically can be.* This is a legitimate abductive
inference and it has the same form as the no-miracles argument in scientific realism — **the razor's
empirical success is itself a datum requiring explanation**, and a purely epistemic preference with no
worldly correlate has no business working as well as it does. It also has independent physical support
that is observation rather than philosophy: physical law is *unreasonably compressible* — symmetry
principles are literally compression statements (Noether), and renormalisation-group flow says
microscopic detail is irrelevant to macroscopic description, which is compression stated as dynamics.

**Two things the argument must still survive, neither fatal.** (i) **The selection-effect counter:** we
only call something a law where compression succeeded; incompressible domains (turbulence detail,
protein specifics, history) we call complicated rather than lawless, so part of the razor's apparent
success is physics being *defined* as the compressible part. A referee will raise this. (ii) **"As
simple as it logically can be" is a minimality claim, not a compressibility claim** — and that is the
same extremal-vs-minimal gap flagged below. Its natural repair is also its most productive form: pair it
with a lower bound (the universe must be complex enough to contain the structures it does), which makes
the thesis a **constrained minimisation** — minimal *subject to* delivering the function. That is
precisely the span law's shape, and the "near the ceiling" condition is what stops "as simple as
possible" collapsing into "nothing is simplest."

**The residual seam, sharper than the original question:** RT *extremises* area (stationarity from the
gravitational path integral) while the span law *minimises* cost over enumerated alternatives, and
extremal ≠ minimal in general — quantum extremal surfaces can be saddles.

**The publish gate exists (`AIW-185`), and its first run showed the S296 complaint was understated.**
MG's point was that `AIW-174` should have been folded into cosmology before v4 shipped. The gate found
**13 open items naming cosmology**, four of them *content* items open since S290 two days before the
publish: `AIW-162` (§7.0 terminology note — "simulation" is the most dangerous word in the paper and it
is the headline word), `AIW-164` (§11.2's "structurally guaranteed" is the strongest and least supported
sentence), `AIW-166` (the span law as motivation for Axiom A5), `AIW-167` (the missing world/self axis).
The diagnosis stands and deepens: the failure was never one missed item, it was that **nothing connected
open items to the artifact being published**.

**`AIW-166` already held MG's cosmos-transfer thread, filed 2026-08-06 — and named the same gap
independently.** It reads: *"there is no cost functional anywhere in SB-HC4A and inventing one is a
research programme. Mark as analogy until then."* So the S296 conversation re-derived a documented open
question rather than discovering a new one, which is itself the argument for the gate: the item existed
and nothing surfaced it. Its content is the strongest form of the thread — A5 (holographic encoding) is a
bare postulate the formalization concedes "is not proven as a universal principle", and if a
cost-optimality argument of the span law's shape can be built cosmologically, **A5 demotes from postulate
to consequence of an optimisation**, which is the move §10.2 wants and does not have.

**`AIW-167` is the sharpest brake on the transfer and was not raised in the S296 discussion.** FMT's
central structure is a 2×2 (implicit/explicit × world/self); SB-HC4A has boundary/interior and
substrate/simulation — **one axis**. "Same architecture" therefore maps a 1-D structure onto a 2-D one
and silently drops a dimension. CRU-36 makes the silence untenable: re-entering a homogeneous reservoir
into itself collapses the models into one undifferentiated pool, and **a pool can be critical and
self-connected and still model nothing.** Related: §7.3's "same architecture, different scale, the
pattern is fractal" overstates the containment theorem, which licenses *nesting* — and nesting preserves
class membership, not architecture.

**`AIW-164` constrains which lane the transfer may use, and it routes MG's Occam answer for him.** The
S288 budget-relative rescue — *biology never operates outside B* — is **unavailable at cosmological
scale, because nothing in SB-HC4A bounds the universe's compute.** So the capability lane is closed
there and only the efficiency/simplicity lane remains. MG's instinct to reach for Occam is therefore not
a preference among options; it is the only lane the architecture leaves open.

**Versioning strategy, MG-agreed:** do not cut a v5 per finding. Accumulate `AIW-174`, `AIW-184` and the
S290 content items into **one coherent §6.5-and-friends rewrite**. Zenodo concept DOIs auto-resolve, so
deferring costs a version bump, not a correction notice, and dribbling versions makes the paper look
unstable.

**Cosmology and FMT stay decoupled in public until the cost question has an answer** (MG-agreed). The
cosmology paper's credibility is currently independent of FMT and that independence is an asset; coupling
them makes each carry the other's risk. The thread lives in a research note, not in either paper.

## 2026-08-08 (S297) — Submission timing: journals ride the conference, preprints run ahead

**MG, ruling on whether the NoC/JCS/JAIC submission lane should outrank FMT-master v15 work before
MoC7:** *"no because the submission must be around the conference somewhen, to get the papers in review
before is risky, desk reject could be too fast, but as preprints of course yes"* — and, separately,
*"a certain quality should be reached."*

**The decision has three parts and they are not the same rule.**

1. **Journal submissions are timed to land around the conference, not before it.** The risk is not the
   review outcome but its *speed*: FMT has five desk rejections, and a desk reject can return in days.
   Submitting early means a real chance of walking into MoC7 carrying a fresh rejection, which is a
   worse position than walking in with the same paper under no verdict at all.
2. **Preprints are unconstrained and should run ahead.** They establish priority and give the poster,
   the handout and any conversation at MoC7 a citable, resolvable object. Concept DOIs mean a preprint
   improved later does not strand its own links.
3. **Quality gates submission, the calendar does not.** *"A certain quality should be reached"* — so the
   conference window is a *ceiling* on how early to submit, not a deadline that licenses submitting
   something unready. If quality is not there by the window, the window moves.

**Consequence for prioritization (`AIW-191`):** the submission lane does **not** outrank the FMT master's
v15 path before MoC7 — the two are not competing for the same slot, because submission is deliberately
deferred past the conference. What *does* compete is preprint-quality work on the master, which serves
both. This answers the ranking question S297 could not resolve on its own.

## 2026-08-08 (S297) — The vacuity objection fails, and CRU-36 was being over-cited

**`AIW-186`, the deeper discussion MG asked for.** Full argument: `drafts/aiw186-vacuity-regime.md`.

**The objection fails on an equivocation, not on a concession.** *"A universe with no outside is one
strongly-connected component, hence closure-ON by construction"* never says **which graph**. On the
**causal** graph — the natural reading — the absence of closed timelike curves makes the relation a
partial order, so the graph is acyclic and every SCC is a single event: the universe is maximally
closure-**OFF** there. The argument borrows "no outside" from that graph and cashes it on the
encode/decode and rule/state graphs, where it is substantive and contested. **Containment is free; the
return is not.** The regime the item demanded is already in the cosmology paper's §6.3, whose three
denials are respectively the textbook view of physical law, the black-hole information controversy, and
eternal inflation. Replacement wording: *contentful, contested, not currently decidable* — which is a
normal condition for a cosmological claim, and must not inherit the word "vacuous".

**⚠ CRU-36 was being cited for something it does not show, and the correction improves the argument.**
`aiw166-cosmos-transfer.md` §6a rested MG's inversion on the pool-collapse being *"a measured dynamical
outcome"*. It is not: in crucible's record the pool language is a **post-hoc architectural diagnosis of
why the null happened** (the substrate was a homogeneous blob, so no distinct models existed for a loop
to close between). Read as a prediction of cosmic homogeneity it assumes its conclusion. **What was
measured is better** — re-entry above a threshold drives a decodable structure to chance (0.996 → 0.479
at τ=25), by raising pool gain ×2.3 until pattern-specificity washes out, inert below re≈0.5. So the
inversion re-founds on **saturation rather than pooling**, which makes it **native to the paper's own
§5.4** instead of imported from crucible.

**A prior gate the thread did not have, and it decides the target.** Inflation's achievement is
*coherent super-horizon* perturbations; active in-horizon sources give one broad hump rather than the
acoustic peak series, which is what killed the topological-defect models. **Any causally-generated-
inside-the-horizon mechanism is already in the dead class**, so MG's redirect to the *initial condition*
is not merely the more valuable target but the only surviving one — placing the work in the
bouncing/cyclic class beside CCC, where the bar is delivering the tilt without a tuned potential.

**`AIW-187`'s first number is a negative, and that is the useful outcome.** The tilt's *sign* comes out
right from capacity accretion, unfitted. But a tilt sourced by one geometric quantity **locks `n_s` to
`r`**: `n_s = 0.965` forces `r ≈ 0.09` against the observed `r < 0.036` — the excluded `m²φ²` corner.
Unifying diagnosis, to be stated once rather than rediscovered per attempt: **a one-parameter account
cannot independently fit amplitude and tilt.** The deeper problem outranks the number — *"specified at
horizon crossing"* is inflation's apparatus, so an account needing it is a redescription of inflation
rather than a rival. **Next step is to state the allocation rule in bounce language**, not to improve
the estimate.

## 2026-08-10 (S299) — MG's eight rulings on the S298 decision queue

**`AIW-198` MoC7 wording — WAIT.** No wording review and no submission yet, and explicitly no
submitting ahead of the official window. **The Thu 27 Aug hard deadline is unchanged**, and Greece runs
28 Aug–3 Sep, so the item has to be re-raised before then rather than waiting for its own deadline to
surface it. This is the only deadline-bound item in the backlog; a "wait" on it is a scheduling
decision, not a deprioritization, and the difference must survive into the next handover.

**`AIW-194` → P1.** Ratifies the S298 reasoning: the recall tag stopped being an open question once it
had an experimental dissociation behind it, and it is member (i) of the v15 epic.

**`AIW-130` JAIC — yes to both.** The architecture slate (Sandamirskaya DNFT + Zou SpikingMCU + one
more) is confirmed, and the six figures are to be rendered.

**`AIW-36` RIM venue — no APC money.** Journal of Intelligence (~CHF 2000) is out, and with it every
paid-APC venue. RIM either stays a cited preprint or waits for a no-fee/waived venue. **The consequence
matters more than the decision:** if the preprint is the publication rather than a placeholder, then its
currency is load-bearing, and a stale primary artifact is a different class of risk from a stale
secondary mirror. That is why the OSF republish was opened at P1 rather than the P2 it would otherwise
have been — the two rulings interact, and ranking them independently would have got it wrong.

**`AIW-200` opened** for the OSF/PsyArXiv `kctvg` republish, previously untracked.

**Freeness gradient + nature/nurture — proposal delivered, decision still open.** Written up at
`drafts/freeness-gradient-nature-nurture-placement-proposal.txt`. The proposal's substance is that these
are **two different kinds of content and must not share a destination**: the freeness gradient is a
*discriminator* (it answers "isn't CoT already free modelling?", which is the objection MoC7 will
actually raise) and belongs in the FMT master v15 with its falsifier attached; the nature/nurture
material is *experimental justification* and belongs in the companion's rationale section, where
`AIW-141`(b) already provides the home. Putting the latter in the master would import an experimental
constraint into a theory paper — the exact drift `AIW-191` exists to stop. **Named risk:** "escapes the
basin" / "re-authors the model space" are metaphors, not operationalizations; if basin-escape cannot be
defined non-circularly before the v15 cut, it enters as a stated open criterion plus falsifier, or slips
to the book.

**`AIW-197` — re-scope confirmed, and the sequencing with it.** The reason a human/macaque substrate is
wanted is **functional**: it is the only architecture with dedicated language centres, so an LLM can be
wired into that periphery or substituted for it. It is *not* about discharging A#7's scope caveat. The
generality study is **dropped, not deferred** — a confirmation that cannot fail is not a measurement
(crucible pattern 39), and fly must not be re-framed as a stepping stone toward it. Sequencing: stays
behind the modular substrate in crucible's idle-time queue.

**Standing, and re-confirmed at startup:** the siibra feasibility check is complete and must never be
re-run; its result lives in `docs/pending-s298-followups.md` §0.

**Decision 6 answered same session (MG, 2026-08-10):** *"freeness gradient: agree, no book fallback though, either v15 or
later. Nature/nurture rationale: also agree."* Both halves of the placement proposal adopted — **and one term of it
overruled.** The proposal offered the book as the fallback if basin-escape could not be operationalized before the v15
cut; MG rejected the fallback outright. **The freeness gradient goes to the FMT master or to a later version of it, never
to the book or the blog as a consolation home.** The reasoning to carry: a discriminator that has slipped its deadline is
still a discriminator, and demoting it to a venue where it faces no objection would retire the claim while appearing to
publish it. Operationalizing basin-escape non-circularly is therefore the gating work, not a nice-to-have.
**Left open, because it was not asked and was not ruled:** whether the book and blog carry the material *after* the paper
does (proposal item 3). Do not read the fallback ruling as an answer to that.

**2026-08-10 (S299) — the two causal pathways are named: THE READING and THE CARVING.** MG chose *the reading* (short-term)
and *the carving* (long-term), rejecting *sounding* as "too active" — the quale is delivered, not solicited, and the name
must not suggest the system goes looking for it. **The naming took three attempts because two obvious axes are both
wrong**, and the reasons are worth keeping: *direction* fails because **both routes go outward first**, to the substrate;
and *path length* fails because it runs **opposite** to timescale — the short-term-effect route has the longer trajectory
(simulation → substrate → read the quale frame → back → cognitive frame → planning sequence → salience interrupt), while
the long-term route is slow structural change. So the timescale must be stated, never implied.
**These are a re-cut of the two causal roles, not a rename of them.** §4.2.3's outward role is self-model → substrate →
behaviour → environment over developmental time; the carving is substrate plasticity driven by usage. The two overlap but
are not the same division, so §4.2.3 requires restructuring rather than a terminology pass — and that work is deliberately
not started, because MG's dreaming hypothesis may change the shape again.

**2026-08-10 (S299) — naming settled: DREAMING and MATURING, delegated to the session and decided.** MG ruled that
"dreaming and daydreaming to me is the same kind" — which promotes the route from a night phenomenon to one route with two
regimes — and delegated the wording. **Decision: keep both names, one vocabulary across paper and book, each anchored on
first use.** The book/paper vocabulary split proposed earlier is dropped as unnecessary.
The reasoning that decided it: the theory's claim *is* that night dreaming and daydreaming are one kind, so naming them
with one word **enacts** the claim, whereas two words would quietly deny it. The anchoring sentence therefore does
argumentative work instead of apologising for the usage. **And the position is not idiosyncratic** — Domhoff and Fox's
neurocognitive theory already places dreaming, mind-wandering and daydreaming on a continuum sharing the default network,
which is what makes the naming defensible in a paper rather than merely evocative.
**Two obligations follow.** The continuum claim is Domhoff's and must not be presented as FMT's; FMT's contribution is
what the route is *for* (reading the quale value, assigning credit) and the mechanism for the regime difference (salience
competition, motor gating), which predicts the continuum rather than observing it. And *maturing* retains a real collision
with biological maturation, kept deliberately because it carries the two-freedoms claim, but glossed on first use.

## 2026-08-14 — Theory of mind is a world-model operation, not a rung on the *erweitert* ladder (MG)

**The question arose adversarially and from outside.** Michael Timothy Bennett (ANU) wrote that FMT's
hierarchy *"appears to count recursive self-modelling depth, which is a different structure"* from his
second-order self `c^{ba}_a` (a's model of b's model of a). The session first read this as exposing an
internal inconsistency in the paper — §3.5 defines the ladder as pure self-recursion (*"the system models
itself modeling itself"*, no other agent anywhere in the chain) while §7 grades theory of mind on that same
ladder (`:763`, and `:778`'s *"great apes (doubly extended, including theory of mind and metacognition)"*).

**MG rejected the premise, verbatim:** *"my theory doesnt have this problem at all, because it has a free
universal modeling system and a means to use a rich self model as template, so there is no more need to
explain theory of mind."*

**The decision, and why it is the right one.** Theory of mind is **not** a rung and was never meant to be.
It is a **world-model operation**: the EWM is a general-purpose modeller with free instancing, and the ESM
supplies a rich template to instantiate into it. So FMT posits no theory-of-mind mechanism at all — ToM
falls out of two mechanisms already in the architecture. That is didactic pattern **#28** (one posit, many
explananda) applied to the social-cognition family, and it is the same redeployment claim §4.2 already
makes in cost terms: *"one model in many deployments"* against *"a separate model per perspective, and
paying for each."* The ladder counts self-recursion; the other-model was never on it.

**Two consequences worth keeping.** First, **the correct answer to "where is your listener model?" is that
FMT does not have one, and that is the point** — a listener is an instance, not a posit. Bennett specified
a listener model as its own structure, which is a special-purpose posit where a general one plus an
instancing operation suffices. Second, **Bennett's observation is correct and should be conceded outright**;
the concession is what makes the reframe land, because the reason the structures differ is FMT's advantage
rather than its gap.

**What is actually owed:** only the §7 wording, which invites the reading this session made. `AIW-211`, P2.
The theory is not in question and the ladder is not changing.

---

## 2026-08-21 (S305) — Conference travel: a standing constraint, not a per-event judgement

**MG, verbatim:** *"not going to sydney or ANYWHERE outside EU unless being paid flight and hotel."*

**The rule.** Any venue outside the EU is **out by default**. It re-enters consideration only when flight
and hotel are covered by someone else — an invited-speaker arrangement, a sponsorship, an employer trip, a
grant line. There is no threshold of prestige or fit that overrides this; a perfect-fit workshop in a
non-EU city is still out unless the travel is paid.

**What it applies to, immediately.** NeurIPS 2026 splits across three cities: **Sydney, Paris, Atlanta.**
Sydney and Atlanta are out. **Paris is in** — and it happens to hold the best topical fit anyway
(*AI and the Self*, `AIW-212`). Also disposes of the Sydney world-model track that the incoming social
item had recommended, without needing to weigh it on merit.

**Why it is recorded as a rule rather than a decision about NeurIPS.** The same question was going to be
asked again by `AIW-52` (Berkeley), `AIW-55` (Sentient Futures London — post-Brexit, so non-EU and
therefore covered), `AIW-06`'s rolling conference list, and every future CFP scan. Deciding it once and
writing it down converts a recurring judgement into a filter that can be applied before any research
effort is spent. **The filter runs FIRST**, before fit assessment: a scan should not produce a shortlist
of unreachable venues and then discover they are unreachable.

⚠ **Do not read this as "MG will not travel."** MoC7 Copenhagen is booked and paid for by him; the
constraint is specifically about **non-EU** travel on his own budget. And it is not a refusal in
principle — *"unless being paid flight and hotel"* is an open door, so an invitation that covers travel is
worth pursuing rather than pre-declining.

**Scope of the record.** Filed here because conference and submission targeting is aIware's lane, and
routed to the fleet by inbox because `social` (media/conference targeting) and `life` (personal
constraints) both need it. See `AIW-212`.

---

## 2026-08-21 (S305) — The reference gate now checks the artifact that ships, not only its source

**The gap.** `verify_references.py` parsed each paper's markdown reference list. The canonical FMT
PDF does not build from that list — `paper/full/latex/paper.tex` runs `\bibliography{references}`
and bibtex resolves every citation out of `references.bib`. The two drift by construction, and S302
established they can drift into *different works under the same citation key*: the one defect class
where both artifacts look internally consistent and only a cross-check can see it.

**What was rejected, and why it matters for the next person tempted by it.** Re-resolving the `.bib`
against Crossref doubles the corpus and the network cost in order to verify the same works twice,
and leaves a second manifest to keep in sync with the first. Instead each **cited** `.bib` entry must
correspond, **by content**, to a markdown reference the manifest has already verified, and inherits
that verdict. Matching by key is impossible: the two key spaces are derived independently
(`AlkireHudetzTononi2008` in the `.bib` against `Alkire2008` derived from the `.md`) and a key-based
check reports **45 phantom failures** on a corpus that is largely fine.

**The finding that justifies the whole exercise.** The trimmed NoC cut was excluded from the gate as
a *"trimmed derivative of the master"*. The unstated premise — that the master's rows already cover
its references — had never been tested. It is false: six works its PDF prints are absent from the
master, three of them *different* works from the master's same-author entries (Alkire 2000 vs 2008,
Gazzaniga 1962 vs 2000, Penrose & Hameroff 1994 vs 1996). **That is the paper heading for a journal
submission.** ⇒ **"Derivative" described the prose, and nobody had checked that it described the
bibliography. Before excluding anything from a gate, check rather than reason.**

**On adjudication.** 30 rows came back needs-review and 26 cleared the same day — 22 by carrying the
master's own hand verification onto entries stating the same thing, gated by a 0.90 text-similarity
floor so evidence transfers only where the two entries make the same claim, and 4 by repairing the
entry. The last four were **deliberately not guessed**: two are suspected defects and two are pre-DOI
originals whose reissue year is all Crossref confirms. `MAX_UNVERIFIED` went 0 → 4 under the ratchet's
own documented exception rather than writing `verified-manual` notes that concede the field still
unchecked. An honest red beats a green that means nothing.

---

## 2026-08-26 (S311) — FMT v15: the second Fable review, completed and folded in

**Manuscript/wording rulings (all MG):**
- **American English throughout.** 44 genuine dialect tokens converted; reference-list titles preserved, since *Nature Human Behaviour* is a proper name. ⚠ The first counts were contaminated — `characteristic`, `realistic`, `programmed`, `analysis` and `organism` are spelled identically in both dialects and were wrongly counted as British. Any future dialect sweep must exclude them.
- **"criticality commitment" → "Class 4 commitment"** at all 14 sites. The compliant template already existed at `:907`, on the same line as an offending instance.
- **Prediction 4 stands; the S204 ruling is retired for its lucid-dream half.** Li et al. 2025, already cited at `:911`, measured a bifurcation with critical slowing at ordinary sleep onset — i.e. the "practically unmeasurable" objection failing empirically. **The developmental half of the S204 ruling is unaffected.**
- **v15 scope = defects + didactic pattern #36 only.** The six under-sold arguments the rival panel found, and the Mashour/Lau citations, are deliberately OUT of v15 and want their own pass.
- **The kind/degree family is budget-anchored to the price form**, consistent with the paper's own rule at `:616`: stated as a barrier it is false, stated as a price it is true.
- **Siegel & Jarvik 1975 dropped rather than annotated.** An unverifiable citation does not ship in a deposit-bound manuscript; Kometer & Vollenweider carries the substance. This is the standing "a secondary-source confirmation does not count" rule applied to a reference *we* added.

**Data-integrity rulings:**
- **Cosmology three-way conflict: `AIW-179` was the true one.** The canonical run happened at S300 on MG's go. Settled on evidence — 12 James-Stein hits and an abstract reading "Nine" in the committed `.tex`, exactly what AIW-179 recorded the regeneration as producing (`b5efa1c4`). `AIW-156` and `CLAUDE.md` had been stale for sixteen days and now agree.
- **`AIW-27` and `AIW-30` were genuine ID collisions** — two unrelated tasks each sharing one number. Renumbered to `AIW-237`/`AIW-238`, verified by reading both entries.

**⭐ The methodological finding, and it should change how reviews are budgeted here.**
**Seven of the nine "deep" findings this review produced were REFUTED on adversarial verification.** The failure mode was near-identical every time: **a quotation that is verbatim-accurate and context-false** — severed from a gloss in the same sentence, a scoping clause in the same paragraph, or a distinction the paper draws a few lines later. Three proposed repairs would have actively damaged the manuscript: the IIT-exclusion paragraph would have committed FMT to **simultaneous** DID experiencers (§6.2 says alternation); the "by design" gloss for the computational prerequisite would have **re-admitted the laptop**, the exact counterexample that leg exists to exclude; and the §3.7.3 repair would have weakened `:516`, the theory's **only** sufficiency statement, to fix a contradiction that dissolves on the plain syntax of `:518`. ⇒ **Budget the verification wave from the start; never fold a deep finding in unattacked.** On this manuscript a finding with line numbers and a direct quote still has roughly a one-in-three survival rate.

**Two tooling facts worth keeping:**
- **A regex cannot identify entries in `backlog.md`.** Status preambles carry arbitrary bracketed blocks and cross-references, and two different heuristics disagreed with each other on the same lines. Duplicate-ID claims from a script over that file are not trustworthy — an enumeration made this session was wrong and had to be retracted.
- **A subagent's transcript file can sit unchanged for 25 minutes while the agent is actively working.** File quiescence is not evidence of a stall; misreading it cost a premature kill. Recovery is `SendMessage` to the agent ID, which resumes it with context intact — far cheaper than re-running.

---

## S313 (2026-08-27) — two papers published, RIM re-typed, and three instrument lessons

**MG delegated the twelve held cosmology rulings** (*"cosmology: go by your own instinct"*) after being shown
that two of them reopened a §9 scope he had previously closed. All twelve were applied as proposed. The
delegation is recorded because it is the second time this session that a decision MG had made narrowly was
later widened by him deliberately — the pattern to preserve is that the widening was *asked for*, not assumed.

**RIM's thesis changed, and the title with it.** The Platinum edition stops claiming the field OMITTED
motivation and claims instead that it MIS-TYPED the components it has: Performance is a capacity, Knowledge
splits along a structure/process boundary, and Motivation is the allocation policy over the loop. The
omission survives only as the symptom the re-typing explains. MG chose route (A) — ship v4 first so the stale
public record was fixed immediately, Platinum as v5 — which also meant the retitle lands on a current record
rather than a stale one.

**The strongest single lesson: check the PREVIOUS session's repairs, not just your own work.** An adversarial
agent aimed at text S312 had already "fixed" found five defects that would have shipped in cosmology v5,
including a paragraph byte-identical to its pre-repair self that still carried both the defect it was
supposed to fix and a second one. Three further should-fixes had never been applied at all. **A repair
recorded as applied is not evidence that it was applied.**

**A green gate can be structurally incapable of firing.** The prose-register sweep reported `0 register hits,
0 dense windows` on a draft MG then rejected by eye. The gate measures antithesis density *relative to the
file it checks*, so a document whose baseline is already saturated raises its own threshold: the new prose
ran at 6.85 per 1k against the paper's own 5.20 and never came near the 4× factor. ⇒ **Measure new prose
against the document's PRIOR baseline, not against the current file.** Recorded in `prose-register.md` on
MG's approval. The general form is worth more than the instance: before trusting a passing gate, ask what
input would make it fail, and whether this input could ever produce that.

**Mechanising a hand-maintained mirror is worth it, and it will still damage the file.** RIM has no md→tex
generator, so `md_to_tex_rim.py` + `mirror_rim_tex.py` were built for a rewrite too large to mirror by hand.
The converter was validated by reproducing 182 untouched paragraphs before being trusted on new text — and
the mirror still escaped citation commands into `\textbackslash{}citep`, consumed two LaTeX environments,
duplicated three paragraphs, mis-ordered two, and degraded five citations to plain text. **Every one was
caught by an existing gate; none by reading the file.** The build succeeded, the page count was plausible and
the citations resolved throughout. The drift check against the built PDF is the instrument that found the
content damage, and the citation gate's uncited-bibitem half found the rest.

**Anchoring a substitution on a string that appears inside a co-author list splits the entry.** Two reference
entries were cut in half this session — "Andrzejewski, D., Oberleiter, S., …" and "Dickens, W. T., & Flynn,
J. R. …" — because the anchors `Oberleiter, S.` and `Flynn, J. R.` also occur mid-entry. This is the
documented `comgarra` trap in a new costume. The repair that matters is not the fix but the check: an
integrity diff of the reference list against HEAD, which proved zero entries lost.

## 2026-09-09 (S318) — Gmail triage, and what it turned up

**Read the OSF API, never the HTML page.** `osf.io/preprints/osf/kctvg` is a 4 KB JS shell that renders
nothing to `curl`; `api.osf.io/v2/preprints/kctvg/` returns `reviews_state`, `date_withdrawn` and
`withdrawal_justification` directly. Every future tombstone check goes to the API.

**A support desk's claim about state is not evidence of state.** OSF closed the ticket on 4 September
saying the withdrawal had never been submitted — eleven days after their own record shows it withdrawn.
Believe the record.

**Check `in:sent` before believing a tracking file that says an email was never sent.** The Anthropic
privacy complaint had been sent on 24 August and escalated to a human the same evening, while a pending
file kept nudging MG for two weeks to decide whether to send it. Staleness detectors measure age, not
truth.

**The OSF letter leads on GDPR Article 16, not Article 17.** Erasure was already refused under 17(3)(d)
and re-arguing it goes nowhere. Rectification is a separate right, the archiving exemption does not
answer it, and Article 5(1)(d) obliges them to keep the data accurate. The harm is specific: in
publishing, *duplication* names duplicate publication, which is misconduct, and MG is a court-certified
expert whose standing is his livelihood.

**`llms-full.txt` is the leverage point for what AI systems say about FMT** — not the wiki articles. It
is the file built for crawlers, and it carried a 983-line v8-era copy of the paper, a summary asserting
the models operate "at criticality", and a link offering the withdrawn PsyArXiv tombstone as the
intelligence paper. MG's instinct that Google reads our wiki was right; his instinct that the fix
belongs at the source was righter.

**Zenodo deposit descriptions are inherit-and-append, so the abstract never refreshes.**
`zenodo_metadata.py::apply_version_metadata` copies the previous description and appends a changelog.
The FMT record's v15 changelog therefore explains the criticality correction directly beneath an
abstract still asserting the error. Same blind spot the file's own docstring records for `title`.

**BBS gets no further investment (MG, verbatim):** *"im in consciousness research, RIM is a cheap
byproduct, not investing into psychology pseudoscience."* The process verdict is separate and equally
firm — for the Seth commentary, ScholarOne never carried the target article and the proposal was
rejected the same day it was submitted because the window had already closed. Physics of Life Reviews
(`AIW-228`) is a consciousness venue and is explicitly outside this filter.

**Deferrable work queues behind work in flight** (MG-dictated, after `lrn` interrupted the P0 pass):
live bug investigations, `lrn` calls, and anything parallelizable or postponable.
