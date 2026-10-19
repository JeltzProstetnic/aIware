<!-- Action: reference -->
<!-- Tracked-by: AIW-242, AIW-244 -->
# Cosmology and RIM — S312 handover. High pressure, max parallelization.

> **⚠ SUPERSEDED S313 2026-08-26 — every decision this file was blocking on has been answered.** MG chose
> **route (A)** and RIM **v4 is published** (`10.5281/zenodo.22118300`), so §0's fork is closed and `AIW-241`
> is done. He **deferred** the RIM `:407` AI-use declaration and **delegated all twelve cosmology rulings**
> to the session (*"cosmology: go by your own instinct"*), so §2 is no longer blocked either.
> **The live handover is `docs/pending-s313-cosmology.md`.** This file is kept for §3's deposit mechanics and
> §5's process facts, which are still true and still worth reading before any deposit.

**MG's direction, verbatim in substance:** continue work on both papers with high pressure and maximum
parallelization; **they should go out today if possible.**

> ⚠ **READ THE FORK IN §0 FIRST.** "Today" is achievable for cosmology and is **not** achievable for RIM as
> MG has now scoped it, and the next session should not discover that halfway through.

---

## 0. THE FORK — RIM cannot both ship today and become Platinum

In the same session MG asked for both papers out today **and** commissioned a Platinum Edition of RIM that
is a partial rewrite: a new title, a re-typed §3.1, a mandatory new §3.4, a new §2.7, and +1,500–2,500 words
net across an 18k-word paper (`drafts/rim-platinum-proposal-2026-08-26.md`). **Those are not compatible in
one day.** The two coherent routes:

**(A) Ship RIM v4 now, Platinum as v5.** The paper is currently green, repaired, and materially better than
the published v3 — 18 review repairs plus the Wittmann reattribution are already in. Publishing v4 costs
nothing and removes the stale-publication problem immediately. Platinum then lands as v5 with the retitle,
which is a cleaner story anyway (a retitle mid-version is less odd than a retitle on a stale record).

**(B) Hold RIM entirely and publish only Platinum.** One deposit, one story, no intermediate version — but
the published v3 stays stale for however long the rewrite takes, and v3 is the version carrying `:317`'s
"early IQ is a poor predictor", which two agents independently named the likeliest desk-rejection trigger.

**Recommendation: (A).** It is strictly dominant unless MG specifically wants no intermediate version. **Ask
him before doing either** — this is a publication-strategy call, not a session call.

**Cosmology has no such fork.** It can go out today once the held rulings in §2 are answered.

---

## 1. STATE — what is done, and it is a lot

### Both papers
| | done |
|---|---|
| Reviews | **Nine Fable agents** — 5 cosmology, 4 RIM. Records: `docs/reviews/2026-08-26-cosmology-fable-review.md`, `docs/reviews/2026-08-26-rim-fable-review.md` |
| Fold-in | **Unambiguous half applied to both**, per MG's ruling "unambiguous now, hold the rest" |
| Gates | Suite **444 passed / 6 skipped**; reference gate **OK — 731 references (554 verified, 177 verified-manual), 352 bibtex citations matched**; RIM drift **OK** |
| Everything committed and pushed to `private` | yes |

### RIM (`paper/intelligence/`) — green, and ahead of its own publication
- 18 review repairs applied to `.md` **and** the hand-maintained `.tex` in one asserted pass.
- **The Wittmann blocker is RESOLVED and it did not need an email.** `docs/wittmann-materials-summary.md`
  (2026-03-26) already documented it: the M→K→P path model, the ~50% variance figure,
  intelligence-as-knowledge as strongest direct predictor and motivation-via-knowledge are **all four the
  Singapore 2002 ICAP paper**, which Wittmann emailed MG on 18 March. Wittmann & Süß (1999) is the
  Brunswik-symmetry paper. Both are now cited for what each reports. **MG ruled S312 that the unpublished
  conference paper is to be cited** — *"it is our strongest formal academic signal and without that RIM has
  zero chance."*
- Built: **46 pp / ~17,900 words**, zero `??`. Published v3 is 44 pp / 16,900.
- Publish gate `10.5281/zenodo.20125095`: **re-derive**, last seen `AIW-229,AIW-200,AIW-10`.

### Cosmology (`paper/cosmology/sb-hc4a.md`) — folded in, NOT yet rebuilt
- **41 repairs** across two asserted batches, `.md` only (its `.tex` is pandoc-generated — **editing the
  `.tex` is a pipeline violation and will be overwritten**).
- `AIW-229` is confirmed by measurement: a fresh build is **68 pp / 29,142 words with `simulation`×9**
  against the published **66 pp / 27,985 with ×22**. The `cosmology_formal` companion regenerates
  identically and **needs no republish**.
- ⛔ **The canonical PDF has NOT been rebuilt since the fold-in.** That is step 1 of §3.
- Publish gate `10.5281/zenodo.18698605`: **twelve** items, of which `AIW-164`, `AIW-166`, `AIW-167`,
  `AIW-174` are content rulings rather than acks.

---

## 2. 🔴 BLOCKED ON MG — nothing below can be decided by a session

### Cosmology, held from the fold-in (all have concrete proposed repairs in the review record)
1. **`:707` "structurally guaranteed"** — this is `AIW-164`, filed 2026-08-06, independently rediscovered by
   this review 20 days later, **and it shipped in v4**. No section argues guaranteed emergence.
2. **The Class 4 defining criterion is stated two incompatible ways** — `:76`/`:138` say irreducibility is
   the criterion and universality is only evidence for it; `:394` says "irreducibility **with** universality".
   ⚠ Under `:394`'s version **Rule 30's Class 4 membership becomes doubly conjectural**, which unravels the
   §2.2 re-filing the whole taxonomy is built on. Consequential — this is the one to put to him first.
3. **§10's title "The Necessity Argument"** — the section's *substance* is compliant (it argues
   axiom-non-redundancy, and §10.2 disclaims model-uniqueness); only the title over-promises.
4. **§9.2's resolution criteria cannot discriminate** and contradict §9.4(b). MG scoped §9 fixes OUT when he
   chose "repair with honest scoping" over the option that included them — **do not apply without asking.**
5. **§9.7's missing symmetric falsifier** — same scope exclusion.
6. **`:482` §7.1's conservation row** — asserted nowhere else and contradicted by §8.3/§8.4; §7.2's defended
   feature list silently omits it.
7. **IB2 grading at `:210`/`:260`** — a unification premise partly supplied by the model's own conjectures,
   then labelled "rigorous… shared by every member".
8. Five further cross-section contradictions: `:328`/`:336` (quantum numbers as boundary labels),
   `:362` (horizon artifact vs ontological boundary), `:366` (particles exchanging information),
   `:552` (timeless fixed point vs ongoing process), `:445` (the information-causality substitution).

### MG-approved but NOT yet applied — the three physics repairs
He chose **"repair with honest scoping"**, which covers exactly these three and no more:
- separate the asymptotic heat-death limit from the finite-time trigger configuration (`:274`/`:282`);
- state E = I's missing exchange rate as an open gap (`:518` — Landauer's rate is temperature-dependent,
  Bekenstein's radius-dependent, so no universal conversion factor exists);
- locate conservation where GR defines it, i.e. locally (`:518` — FRW has no global energy conservation).

### RIM
- **The `:407` AI-use declaration.** "All theoretical content… solely the author's own" is contradicted two
  sentences earlier where a specific insight is credited to Wittmann, and the declared AI scope may
  understate what the project's records show. **It is MG's declaration; only he can word it.**
- **The §6.1-vs-§6.4 mindset/compounding discriminator** — §6.1 prices a willingness-change near zero to
  reconcile the mindset null while §6.4 has motivation-side changes compounding. The paper has the
  discriminator material at `:279` but never applies it here.
- **Route (A) or (B) from §0.**

---

## 3. EXECUTION PLAN — max parallelization

**Serial first, because everything downstream depends on it:**
1. Put §2's cosmology rulings to MG **as one batch**, ordered with the Class 4 criterion first.
2. Apply his rulings + the three approved physics repairs to `sb-hc4a.md`.
3. `python3 scripts/build_cosmology_pdf.py` → verify in `tmp/build-cosmology/paper3/` → **only then**
   promote. ⚠ A bare invocation with no arguments rebuilds **both** canonical papers; `paper6` is in sync
   and must not be disturbed.

**Then parallel — these do not touch the same files:**
- **Track C:** cosmology gates (suite, reference gate, drift), re-derive the 12-item ack list from scratch,
  write the v5 changelog, dry-run, publish.
- **Track R:** RIM per route (A) — re-derive its ack list, write the v4 changelog, dry-run, publish.
- **Track P (only if route A):** start Platinum step 2 — the verification agent batch from the proposal
  (Kanfer & Ackerman 1989 primary, Meehl 1978, Borsboom et al. 2004, Melby-Lervåg nulls, Ritchie &
  Tucker-Drob, the Schaie rebuttal, plus the open debts: von Stumm & Ackerman *r* ≈ .30, Dignath & Büttner,
  Wittmann 1988). **Nothing reaches the Platinum draft unverified.**

**⚠ Deposit mechanics that cost this session time — do not rediscover them:**
- `ZENODO_CHANGELOG` **must** be passed explicitly. The script's default `tmp/zenodo-changelog.md` holds a
  **stale v3 changelog for a different paper**. The guard catches it, but do not rely on that.
- **Re-derive the ack list, never paste it.** It changed once already this session when a new backlog item
  named `paper/full/` — which was the gate working, not failing.
- **Diff the changelog against the git log before depositing.** S311's handover said the deposit was the only
  step left; the changelog was in fact stale by a whole review, and **no gate in the chain can see that.**

---

## 4. The Platinum proposal in one paragraph

`drafts/rim-platinum-proposal-2026-08-26.md`. **Thesis:** the field did not omit a component, it *mis-typed*
the components — P is the only capacity in the psychometric sense, K splits along the structure/process
boundary, **M is not a component but the allocation policy over the loop** — and that one re-typing *derives*
four standing embarrassments the field only reports. **New title committed:** *"A Schedule, Not a Substance."*
**⚠ The finding that changes an obligation:** motivation-as-allocation is **occupied three times over**, and
one occupant is **Kanfer & Ackerman (1989)** — inside the ability literature, by the paper's own chief
interlocutor. What stays separable is that all three allocate *momentary attention within a task* while none
allocates *offline simulation time in an explicit self-model across developmental time*, and none derives the
measurement consequences. **A mandatory §3.4 must name all three before a referee does; unearned novelty here
sinks the paper.** New didactic device proposed: **the observatory** (optics = P, plate archive = K,
telescope-time schedule = M) — needs MG's sign-off before it enters `didactic-patterns.md`.

---

## 5. Two process facts worth keeping

**The changelog is not covered by any gate.** The reference gate proves citations resolve, the drift checker
proves the PDF matches its source, the publish gate proves no open item names the artifact — and a deposit
can still ship release notes that under-report it by an entire review. **Add "diff the changelog against the
git log" to the pre-deposit checklist.**

**`build_review_pdf.py` is retired and `build_changes_highlighted_pdf.py` replaces it** — latexdiff against
any git ref, 12 tests. Its baseline must be *verified*, not assumed: confirm the ref by downloading the
published PDF and comparing marker counts before trusting any diff. A diff against a guessed baseline is a
confident picture of the wrong thing.
