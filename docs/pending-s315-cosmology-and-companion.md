<!-- Action: reference -->
<!-- Tracked-by: AIW-140, AIW-180 -->
# S315 brief — update the cosmology paper and the computational FMT companion

> **⚠ SPENT — S316 (2026-08-27). Do not work from this brief.** Its companion half is done: `AIW-218`
> is closed and the companion is published as **v2**, `10.5281/zenodo.22133843`, retitled *"What Closure
> Costs and What It Buys"* with the three architectural-cost sections in. Its cosmology half is done too
> (v6 shipped at S315) and cosmology now **rests** by MG's S316 ruling — no v7 is scoped. `AIW-159`,
> `AIW-160`, `AIW-179` and `AIW-218` are all closed; only `AIW-140` (the companion's standing claim-state
> ledger) and `AIW-180` remain, and both are tracked in `backlog.md`. Kept only as the record of what the
> S315 brief asked for. Current state: `docs/decisions.md` S316.

> **⏸ EXECUTED S315 2026-08-27 — demoted to reference.** §0(a) `AIW-180` fixed (with `AIW-239`);
> §0(b) confirmed; §0(c) resolved — `paper6` now passes the overflow gate at 0 boxes, and
> `AIW-179` turned out to have been executed at S300 and never ticked. §1 cosmology: `AIW-159`
> was already fixed at S313, `AIW-160` done in **both** papers, **v6 published**
> (`10.5281/zenodo.22132325`). §3 inbox: all 28 items triaged, `AIW-143` closed.
> §2 the companion is the **open half**, and it moved to
> `docs/pending-s316-companion-and-decisions.md`, which also carries the title shortlist MG
> is owed and the formalization-redeposit decision. Kept for the crucible constraints in §2
> and the precision rule; nothing here is actionable on its own.


**MG-directed at S314 shutdown 2026-08-27:** *"prepare next session to update cosmology paper and
computational FMT companion"*. Both are published artifacts with open revision debt. Neither is blocked.

---

## 0. READ FIRST — three things that will bite before any content work

### (a) ⛔ The cosmology drift gate is not checking the canonical, so a green result means nothing
`AIW-180` (P3, and it should be raised): `check_md_pdf_drift.py --paper cosmology` resolves to
`tmp/build-cosmology/sb-hc4a-S293.pdf`, a throwaway build artifact from S293, **not**
`paper/cosmology/sb-hc4a.pdf`. **Fix the `PAPERS` entry before running it, or a drift-clean result is a
statement about a five-month-old temp file.** This is the same defect class as `AIW-239` on the full paper.
The drift checker is the one instrument that catches silent content damage — a mis-aimed one is worse than
none, because it reports success.

### (b) ✅ The cosmology build is now safe, which is why `AIW-245` was P1
Landed S314. `build_cosmology_pdf.py` is **build-then-promote**: every build runs in
`tmp/build-cosmology/<paper_id>/`, and `--canonical` promotes only after two gates pass.

```
python3 scripts/build_cosmology_pdf.py paper3              # build to tmp only
python3 scripts/build_cosmology_pdf.py paper3 --canonical  # promote after gates
```
Naming the paper is now **required**; `--all` builds both to `tmp/` and cannot be combined with
`--canonical`. Promotion `cp`-backs-up the previous canonical to `tmp/build-cosmology/canonical-backups/`.
⚠ **`git checkout` still cannot restore `paper/cosmology/sb-hc4a.pdf`** — raw blob under an LFS-active
`.gitattributes`, so `HEAD:` holds a 131-byte pointer. The script backs up for you; nothing else does.

### (c) ⚠ `paper6` (the cosmology formalization) does NOT pass the overflow gate — measured S314
10 of 12 overfull hboxes exceed 2.0pt, **worst 14.36pt**, four of them over 10pt. `paper3` is clean at zero.
So **`paper6 --canonical` will refuse to promote** until either the boxes are fixed or an explicit
`--overflow-threshold` is passed. That is deliberate: the threshold in the shell history is the
acknowledgement. **Decide which, rather than discovering it mid-run.** Related: `AIW-179` records that the
`cosmology_formal` `.md` is authoritative and the `.tex` was stale from S210 — one open decision that is
MG's, not a session's.

---

## 1. COSMOLOGY (SB-HC4A) — published v5, `10.5281/zenodo.22118645`

Source: `paper/cosmology/sb-hc4a.md` → `.tex` → `.pdf`. Concept DOI `10.5281/zenodo.18698605`.

**Two P1s, both from the S290 Fable sweep, both concretely fixable and neither needing new evidence:**

- **`AIW-159` — §7.1 contradicts §8.3 inside the same section.** The §7.1 correspondence table lists
  information *conservation* across the boundary as a shared property; §8.3's prose calls the explicit model
  *"a lower-bandwidth, organized projection of **selected** information."* Selection is lossy. **The prose is
  the right half — fix the table row.** An internal contradiction a referee reaches in one lookup.
- **`AIW-160` — split Φ_dyn from Φ_rep. This is reviewer attack line 2** (*"your fixed point is either
  trivial or is a physics claim you haven't made"*). Φ(U) = U is **dynamical** closure, which every
  deterministic system satisfies trivially; Φ(m\*) = m\* is **semantic** self-reference, a representation
  whose content is itself. They share one symbol, and §6.4's Gödel argument plus the formalization's Lawvere
  appeal are theorems about the *semantic* sense being used to license conclusions about the *dynamical* one.
  Crucible's stationary-closure impossibility result is the empirical shadow: dynamical return-ness is
  generic and cheap, semantic self-modelling is neither. **State which sense each argument requires.**

**P2s worth folding in the same pass** (each is a paragraph, not a rewrite): `AIW-163` (run the MFDFA
positive control on the instrument *before* reporting the CMB null — crucible Pattern 51); `AIW-165` (add
the CRU-58 genericity result to §6.3, with its caveat in the same paragraph — it turns a defensive argument
into a positive one); `AIW-166` (the span law as candidate motivation for Axiom A5 — no longer an analogy,
not yet a derivation; state is in `drafts/`); `AIW-186` (**the vacuity regime — MG flagged this for a deeper
discussion and it decides whether ESM = EWM is publishable at all**; do not settle it in a session);
`AIW-173` (the saturation-trigger automaton experiment, §9.7's own resolution criterion).

**P3s:** `AIW-167` (the missing world/self axis — SB-HC4A has one axis where FMT has a 2×2), `AIW-168`
(steelman the Class 3 elimination — reviewer attack line 3), `AIW-169` (import the constitutive/practical
two-limit distinction into §6.4).

⚠ **Do not spend a DOI on a small fix.** v5 shipped 2026-08-27. Batch the P1s and whichever P2s land, then
one v6. The publish gate will re-derive its own ack list; it has changed on every single deposit so far.

---

## 2. THE COMPUTATIONAL COMPANION (Gruber 2026d) — v1 published, and the title is the live question

Draft: `drafts/companion-computational-paper-draft.md`. Zenodo concept `10.5281/zenodo.21610993`,
v1 `21610994`, published 2026-07-26.

### ⚠ MG's position on the title CHANGED between S284 and 2026-08-10, and the backlog records only the first
`AIW-140` carries an **MG ruling of S284 2026-08-04: DEFER** — *"defer until more results, nobody is reading
it yet"*, explicitly *"do not spend a DOI on a title-only correction."*

**But crucible's inbox item of 2026-08-10 reports MG saying the opposite in substance:** *"'Closure and
Criticality' that will have to change in the title probably, and hopefully we can make a stronger statement
even."* ⇒ **Surface both to MG and get one ruling; do not pick.** The two are reconcilable — the S284 defer
was about spending a DOI on a title-only bump, and the 08-10 remark is about what the title should say when
a substantive revision happens — but that reconciliation is MG's to confirm, not a session's to assume.

**The substance, which is settled and is not waiting on MG:**
- v1 is titled *"Closure and Criticality as **Enabling Conditions** for World-Modeling."* Crucible's
  No-Free-Lunch correction retires exactly that: a finite closed loop unrolled over a finite horizon **is**
  feedforward + memory, so any I/O capability is feedforward-approximable and closure can never be an
  enabling condition. **The FMT master already made this correction in v14** — *"enabling conditions for a
  world-modeling step"* → *"govern how efficiently a world-modeling step can be had"*. So the companion
  currently carries in its **title** the framing the master's body has already retracted, which is visible
  to any reader holding both. **That is a correctness fix needing no new evidence.**
- ⛔ **A "stronger statement" is NOT currently purchasable, and crucible says so itself.** The result that
  would license one is **M1s3 (sufficiency)**; it ran twice, both non-adjudicating, §5.1 of the
  pre-registration is **unpopulated**, and the tier-B spiking build is **gated**. **Do not write a stronger
  claim into a title in anticipation of it.**
- ✅ **What could carry a title today** is the architectural-cost line — A#7/A#8/A#9: opening the global loop
  costs 14.0% of the connectome (dense) / 12.0% (modular) where return-freedom costs 74.0% / 71.5%, a
  **5.3× / 6.0×** multiplier, exact and scale-free. That is a *cost* result and a title built on it is
  honest today. Retitling on the **efficiency/cost axis** is crucible's own recommendation.

### `AIW-218` (P1) — the companion's largest single debt
**The master banks eight unbroken ordinals including A#7/A#8/A#9; the companion explains none of the three.**
Crucible tracks closing it as **CRU-85** and supplies substance and framing — **aIware writes the prose.**
Two hard constraints from their side, both of which have bitten before:
1. **Cite the ordinal, never the page** — pages moved 104–105 → 107–109 between builds.
2. The `[[CRUCIBLE:]]` method sections must describe the banked loop arms as **materialised dense products**,
   importing the approved scope sentence **verbatim** from `~/crucible/docs/results/cru69-tau-syn-scope.md`
   §11.6.

Full brief: `docs/crucible-status-2026-08-23.md`. Rides `AIW-124` at MoC7 (crucible CRU-94).

### ⚠ The 2026-08-06 crucible item is P0 and is still untriaged in the inbox
It states in MG's own direction that the night's rulings *"will re-write most of the computational companion
paper"*. Two things in it bear directly on any revision: **(1) the claim is EFFICIENCY, not NECESSITY** — the
DV inverts to *cost at matched function*, and all four of crucible's pre-build kills were scored on the wrong
side of that inversion, so they are **not** evidence against FMT; **(2) the closure operationalization itself
is in question** — *"your 'closure off' just is like a stroke with a new self emerging elsewhere"* — with a
candidate theorem that in a connected recurrent network **whether a path returns is not a manipulable
variable**. Read `~/crucible/docs/decisions.md` top entry for 2026-08-06 in full before revising method or
closure claims.

### The precision rule now applies to every crucible number quoted
Recorded S314 in `.claude/knowledge/publication-build.md`. Before quoting any crucible figure, classify it:
**(a)** a within-run comparison on one shared trajectory — safe to full precision; **(b)** an integer/graph
quantity — exact; **(c)** a cross-rerun reproduction of a floating-point dynamical result — **~2.6e-04 is the
floor and four decimals is over-claiming.** Also carried there: the CRU-121 `2*z(accuracy)` fault, which was
checked S314 and touches nothing in aIware — **but the class is live**, so never quote a crucible ceiling,
fraction-of-ceiling or accuracy-derived *d′* without checking `cru121-why-nobody-learns.md` §9–17 first.

---

## 3. THE INBOX IS THE MISSING INPUT
**28 aIware cross-project items are untriaged** (`AIW-143`), and a large share of them are crucible findings
that bear on exactly these two papers — including the P0 above. **Triaging them is arguably the first move
of the companion work, not a separate chore.** The two `[fact]` items were executed at S314 and deleted; the
rest remain. ⚠ The cross-project inbox is over its fleet ceiling (`CFG-515`) and MG ruled at S314 that the
ceiling mechanism itself is unacceptable — a `[work]` item reporting the deadlock is filed with cfg.

## 4. SUGGESTED ORDER
1. Fix `AIW-180` (the mis-aimed cosmology drift target) — otherwise every later gate result is untrustworthy.
2. Triage the 28 inbox items, at least the crucible ones.
3. Put the **title question** to MG with both of his statements side by side, and the cost-axis option.
4. Cosmology: `AIW-159` + `AIW-160`, then whichever P2s are cheap; rebuild via `paper3 --canonical`; one v6.
5. Companion: `AIW-218` prose against crucible's substance, under the two hard constraints.
