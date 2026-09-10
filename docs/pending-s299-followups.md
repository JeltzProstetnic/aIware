<!-- Action: reference -->
<!-- Demoted act → reference on 2026-08-11 (S301). §1 no longer holds a live decision queue: item 2 was
     ruled at S300, items 3 and 4 were resolved at S301 (the Revonsuo mail is drafted, the OSF letter is
     sent), and the one item still open — AIW-203's priority — is carried forward in
     docs/pending-s301-followups.md §3, which is the file the next session presents. Keeping two files
     asking for the same ruling is how a decision gets presented twice and answered once. -->
<!-- Tracked-by: AIW-193, AIW-199, AIW-200, AIW-201, AIW-202, AIW-203 -->
# S299 handover — a theory session that outran the paper, plus four decisions and two queued jobs

> **▸ S300 STATUS (2026-08-10 late).** This file stays `act` because **§1 is untouched — all four
> items still await MG.** Everything else has moved:
> - **§2(a) restructure — two of three parts LANDED.** Pattern #37 is in §4.2.2 with the scope
>   guard; the dashboard/causal-power line is in §4.2.3 with the conflation correction. **The
>   DREAMING/MATURING re-cut is NOT started and stays blocked on §1 item 2 (`AIW-202`)** — both
>   landed passages were deliberately written clear of all four `AIW-202` literatures so they could
>   ship ahead of the ruling.
> - **§2(b) v15 member (a) — needed no work.** The λ crossover landed in S297 (`30f80c56`), before
>   the epic existed. Verified in `.md` and `.tex`; the confounded fidelity half has zero hits.
> - **§3 verification debt — REM atonia/RBD/Jouvet CLEARED** → `docs/s300/verification-rem-atonia.md`.
>   It returned two corrections, both recorded below. The remaining four items were researched in
>   the same session; see the S300 handover for their state.
> - **§5 sweep — DONE**, and it paid exactly as predicted → `docs/s300/sweep-retired-framings.md`.
>   Two severe hits applied ("Principles 4–5"; "no simpler system can replicate"); two
>   medium-confidence findings and one paper-vs-knowledge-file fact conflict left for MG.
> - **A §6.3 factual error was found while checking the REM material**: atonia was credited with
>   suppressing sensory input. It gates motor output. Fixed.
>
> ⚠ **The SessionStart hook flagged this file as already-shipped (`STALE_PENDING`). It was wrong** —
> the "completion evidence" is the commit that *created* the file. Do not demote it on that basis.

## 0. Read this first: what happened, in one paragraph

S299 started as a v15 push and turned into MG's most productive theory session in a while. **Five v15 members
landed** — (b), (c), (g), (h), (j) — and along the way **three retired framings were found still shipping in
the master paper**. Then MG developed a substantial new body of theory in conversation: the capability-null
inversion, the quale as read value, the two freedoms, and the free-will singularity. **All of it is captured**
in `.claude/knowledge/didactic-patterns.md` (patterns #35, #36, #37 plus extensive additions) and in
`AIW-201`/`AIW-202`/`AIW-203`. **Do not re-derive any of it from the conversation log — the knowledge file is
the record and it is more precise than the transcript**, because MG corrected himself four times and only the
final forms are written.

## 1. Awaiting MG — nothing below proceeds without an answer

| # | Item | What is needed |
|---|------|----------------|
| 1 | **`AIW-203` priority** | Proposed **P2**. The S299 book chapter (seven-to-eight pieces, routed to simbook). |
| 2 | ~~**`AIW-202` positioning ×4**~~ **✅ RULED BY MG 2026-08-10 (S300)** — on corrected evidence: the RL differentiator is dead and the Domhoff & Fox continuum is not in their paper. Position against the field's unsettledness (priority inversion = the unclaimed signature); *dreaming* stands on FMT's own architecture. **This unblocked the §4.2.3 re-cut, which has landed.** Details in `AIW-202`. Original text follows: | The four literatures the new theory must be positioned against before a word is drafted: **model-based vs model-free RL** (the recency/priority override *is* their arbitration), **predictive processing** (measurement-against-default is their home turf), **Revonsuo's threat-simulation theory** (the ancestral-function-of-dreaming move is his), **Domhoff & Fox's continuum** (dreaming/mind-wandering/daydreaming sharing the default network is theirs). In each case FMT has a real differentiator — see `AIW-202` — but MG should confirm the framing. |
| 3 | ~~**`AIW-199` Revonsuo outreach**~~ **✅ FIRED S301 2026-08-11 — MG said draft it; Gmail draft `r-6374301162047284797` → `revonsuo@utu.fi`, awaiting his send. Two things this surfaced: the trigger had ALREADY fired on 2026-02-13 (he has been cited on the public mirror for six months, so "before he is cited publicly" was never in front of the horse), and the master cites Revonsuo 1999 + Noreika et al. 2009 — NOT the 1995 or 2000 papers. Original text follows:** | Recommended to **fire now**, on the convergence rather than the original errand. MG's dream material is adjacent to Revonsuo's threat-simulation theory, and the technical question in `AIW-199` (did any element in his 1995 taxonomy ever code modality misattribution?) is a genuine first contact. Trigger is still formally "before he is cited publicly". |
| 4 | ~~**OSF deletion letter**~~ **✅ SENT BY MG HIMSELF 2026-08-11 17:57 — thread `19fece36b5059917` → `support@osf.io`. Both open questions are settled: he took the LESS-candid option (the letter cites "errors" generically and names neither the McGrew quotation nor the reversed NFC/TIE dissociation), and the address question is moot because the OSF account is registered to `matthias@matthiasgruber.com` — verified against the 2026-02-16 submission confirmation — so the Art. 17 request cannot be refused on identity. Only the help-desk auto-ack has arrived. `AIW-200` stays blocked, now on a live request. Original text follows:** | **Deferred by MG.** Draft sits in Gmail, unsent. Two open questions when he returns to it: how candid to be about the defects in the hosted v1 (naming the unverifiable McGrew quotation and the reversed NFC/TIE dissociation is what makes the case undeniable, but it puts them on record), and **which address to send from** — an Art. 17 erasure request gets refused on identity grounds unless it comes from the address registered to the OSF account. |

## 2. Queued work, both unblocked and both deliberately not started

**(a) The §4.2.2 / §4.2.3 restructure.** This is now genuinely ready and it is the highest-value writing job
open. Three things this session established are exactly what those sections lack:
- **The dashboard/causal-power line** — live quale-reading is *not* a route; it is the self-model via closure
  recurrence, with the implicit model using the quale as a dashboard, which is a **component of** a
  causal-power system. Causal power begins only where the quale **results in associated simulation**. This
  joins pattern #13 to #35 and the paper draws the line nowhere.
- **Pattern #37** — §4.2.2 currently answers free will by *widening the definition of will* and never explains
  the phenomenology. #37 explains it structurally: the apparatus is the one thing the simulation cannot model,
  so a choice whose cause is unrepresentable feels uncaused.
- **The two pathways are a RE-CUT, not a rename** — MG's *maturing* is substrate plasticity driven by usage,
  whereas §4.2.3's *outward* is self-model → behaviour → environment. Overlapping, not identical. **Do not
  attempt a find-and-replace.**

⚠ **Names are settled: DREAMING (short-term) and MATURING (long-term), MG's "two freedoms".** Both need a
first-use gloss — see the registry. *The reading* / *the carving* is **dead**; do not reintroduce it.

**(b) v15 member (a)** — the CRU-70 λ crossover. ⚠ **Carry the λ crossover ONLY.** CRU-70's fidelity half is
confounded (a size-matched null attributed 60% to growing state dimension, only 40% to return length), and the
raw 0.909→0.543 decline must never be quoted as a latency effect — it is wrong by 2.5×.

## 3. Verification debt created this session — clear before any of it is published

Every one of these is flagged in place, but they are easy to lose:
- ~~**Domhoff & Fox 2015 / Domhoff 2019** — the dreaming/mind-wandering continuum.~~ **✅ CLEARED S300 — and
  the continuum is NOT THERE. Withdraw the claim.** They say *"dreaming as intensified mind-wandering"*; the
  word "continuum" appears once in the paper and not about these phenomena. The shared-DMN half is
  overstated (default network *plus* secondary visual and sensorimotor cortices; Fox concedes on p.346 that
  the neural basis "involves more than just default network activity"). **The book is 2017, not 2019.**
  **Kirberg & Windt 2026** (*Conscious Cogn* 137:103965, 379 within-subject reports) tests the thesis and
  concludes against it; **Christoff, Fox et al. 2016** call it a *"family of spontaneous-thought phenomena"*.
  ⇒ ***Dreaming*-for-the-whole-kind can no longer be justified as "the field already groups these" — it must
  stand on FMT's own architecture.** That is the stronger position anyway, since Kirberg & Windt cuts against
  *intensification*, which FMT never claimed. **Feed this into the `AIW-202` ruling.**
- ~~**Revonsuo's threat-simulation theory**~~ — **✅ CLEARED S300.** Attribution holds; the 2000 BBS target
  article was read in full. **The modality question is a confirmed gap** — `misattribut*`, `cross-modal` and
  `synaesth*` all return **zero hits** across the article, so `AIW-199`'s opening is genuine. ⚠ Two
  corrections: he credits **Snyder 1966** and **Ullman 1959** with prior evolutionary theories, so do not
  over-attribute the ancestral-function move; and the **2015 Social Simulation Theory is a *competing*
  theory, not an extension** — he sets it against TST for empirical discrimination. ⚠ The BBS peer
  commentary is paywalled and unread; that is where the strongest objections live.
- ~~**Model-based vs model-free RL** (Daw, Dolan, Doll, Gläscher)~~ — **✅ CLEARED S300, and it cost us the
  proposed differentiator.** All four names verify, but **Dayan & Berridge 2014** already say a model-based
  system may need to *"retaste or re-experience"* the outcome — the exact re-instantiation step FMT was going
  to claim. *"Model-based RL is agnostic there; FMT is not"* is **false**; corrected in
  `didactic-patterns.md` and `backlog.md`. Two more steps are occupied (Gershman/Markman/Otto 2014;
  Bornstein et al. 2017). **The defensible ground is the field's unsettledness** — 16 accounts, 9
  incompatible arbitrating variables, 21 years, and recency never referees between systems — **with the
  reordering / priority-inversion signature the least-occupied claim.** Input to `AIW-202`, not a ruling.
- ~~**REM atonia / RBD / Jouvet's pontine lesions**~~ — **✅ CLEARED S300**, citations pulled and
  DOI-checked → `docs/s300/verification-rem-atonia.md`. **Two corrections came back with them.**
  **(i) Do not write "glycinergic."** Brooks & Peever 2012 (*J Neurosci* 32:9785) shows atonia needs
  GABA_B *and* GABA_A *and* glycine; glycine alone is insufficient. **(ii) The separability claim
  must soften.** Whether losing atonia alters dream *content* or only its expression splits by
  sampling method — retrospective studies find large differences (Fantini 2005: 66% vs 15%
  aggressive dreams), prospective lab studies find none (D'Agostino 2012; Valli 2015, which is the
  best citation because its PD-with vs PD-without-RBD design controls for degeneration). Defensible:
  *"no consistent evidence content differs; differences appear retrospectively and largely vanish
  under lab sampling."* Not defensible: *"content is unchanged."* ⚠ **And the deeper caveat, which
  is the one a reviewer would raise:** RBD patients are prodromal synucleinopathy and Jouvet's cats
  were lesioned, so **neither is a clean "atonia removed, simulation intact" preparation** —
  mechanism separability is solid, but mechanism-from-content separability is supported by no single
  preparation. ⚠ Also: "acting out dreams" is interpretation, not observation — the cats showed
  species-typical motor patterns with eyes closed, and Hendricks et al. 1982 found released
  behaviour tracks lesion site. Cite it alongside Jouvet or a reviewer will. ⚠ Both French originals
  remain **UNVERIFIED** (not directly inspected); 12 items are listed as such in the file's §(d).
- **Anticipatory analgesia** — MG softened the claim to *relative pain down-weighting under excitement, possibly
  just salience competition on signal strength*, which needs no opioid literature. **Use the softened form.**

## 4. Do NOT redo

- **The whole S299 theory thread.** It is in `.claude/knowledge/didactic-patterns.md`. MG corrected himself
  repeatedly; the file holds the final forms and marks the superseded ones. Re-reading the transcript will
  surface withdrawn versions.
- **Superseded and explicitly dead:** *the reading* / *the carving* as names; "zero compute" and "zero compute
  residue" as framings of the null; "capability-null **at the closure locus**" (the null sits on the
  **self-relational increment**, because closure has capability like any recurrence).
- **The OSF citation sweep is COMPLETE** — 23 files repointed to the Zenodo concept DOI
  `10.5281/zenodo.20125095`, and both Zenodo RIM records cleaned of the OSF link *and* the erroneous
  `isPartOf` FMT link. Zero `kctvg` references remain in papers, wiki or front matter. `AIW-200` (the OSF
  republish) is **moot if the deletion request succeeds — do not action it until OSF replies.**
- **`AIW-193` members (b), (c), (g), (h), (j) are done and verified** against the built PDF. (c) is
  verification-only and its finding — crucible's ledger stale on three rows — is already routed to them.

## 5. One thing worth knowing about how this session went

Three retired framings were found still live in the master paper in a single session: the spontaneous-"I" gate
(member g), an absolute capability claim (found while placing member h), and MG's ESM/EWM correction arriving
the same day. **All three are the same defect class** — a correction made in conversation or in an inbox item
that never reached the artifact. The standing caution now lives in `didactic-patterns.md` under the
three-axes rule. If a future session is looking for cheap high-value work, **sweeping the master for other
instances of that class is likely to pay.**
