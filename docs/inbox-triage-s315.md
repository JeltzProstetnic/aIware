<!-- Action: reference -->
<!-- Tracked-by: AIW-250, AIW-251, AIW-252, AIW-253, AIW-254, AIW-143 -->
# S315 inbox triage — all 28 aIware cross-project items dispositioned

Executed 2026-08-27 on MG's "go". Source file: `~/cfg-agent-fleet/cross-project/inbox/aiware.md`
(28 open items, 88 KB, oldest 2026-07-13). Every item below was read in full, checked against
aIware's existing backlog and knowledge files, dispositioned, and then **deleted from the inbox**.
This file is the record of what each payload said and where it went.

## The finding that explains the backlog, and it is not "nobody triaged"

**Most of these items were already absorbed.** Item by item, the majority had a live aIware
backlog entry covering them — in several cases an entry that had already been *worked and closed*.
What never happened was the deletion. An inbox item is a delivery mechanism, and the fleet's own
rule says to promote and then delete in the same session; the promoting half kept happening and the
deleting half did not. That is why the inbox reached 195 items across the fleet and ~100k tokens.

⇒ **Only five of the 28 carried work with no home anywhere in this project.** They are `AIW-250`
through `AIW-254`.

## Dispositions

### Already fully landed — deleted, no action

| item | payload | where it already lives |
|---|---|---|
| "samples"/"gates" banned, emergence all the way + 3 citations (simbook 08-21) | MG: *"sampling as a figure of speech, i never ever anywhere suggested that there was active sampling"*; *"'gated by' is just as stupid a choice of words … its emergence all the way, from the first cell to the last robot brain"* | `.claude/knowledge/neuroscience-communication.md` — the ⛔ section, the 20 Hz reconciliation and all three papers *including* the Lisman/Akam causal-arrow trap are present |
| `prose-register.md` upgrade batch, 3 gaps (consolidated 08-21) | banned tells, length-and-posture, sliding window | all three landed: `prose-register.md:47` ("load-bearing"), `:49` ("bite"), `:69` (length and posture), `:89` (sliding window, 400/100/4.0) |
| companion TITLE ruling (crucible 08-10) | retitle on cost, no stronger statement | **answered by MG this session** — `docs/decisions.md` S315, appended to `AIW-140` |
| §8.9 order-of-magnitude over-claim (crucible 08-14) | already `[x]` in the inbox | fixed at source `3ec61acb`; published-PDF staleness is `AIW-210` |
| precision ceiling on crucible numbers (crucible 08-11) | never quote past 3 dp for kind (c) | `.claude/knowledge/publication-build.md` "Quoting a crucible number" table; the two four-decimal claims remain `AIW-243`(4) |
| span rule standalone publication (crucible 08-14, MG *"hand this over to aIware"*) | literature check first, not a draft | `AIW-219` — **literature check DONE S306** |

### Folded into existing backlog entries — deleted

| item | disposition |
|---|---|
| Bildstein gathering PARKED (social 07-23, MG) | `AIW-100` / `AIW-102` — the symposium/convening dimension is parked; FMT-as-standard-model *theory positioning* stands. Revive trigger = a genuine crucible robot consciousness result. |
| Olinyk CRC↔FMT note → preprint after 2 edits (social 07-23, MG) | `AIW-120`. The two required edits: flag-as-paraphrase the three unverified proprietary labels ("Double-Jump", "structurally redundant middleman", "Seven Books dialogues"), and keep the *"is Olinyk's Objective Data a generative world-model or structured stored facts?"* question explicitly open rather than adjudicated. Primaries now ingested at `~/social/docs/data/olinyk-OLICRC-full.pdf` + `…OLIORC-2-full.pdf`. |
| qualia-privacy paper parked to P3 (social 07-23, MG) | `AIW-105` → P3 "maybe / hand to a student". Content shipped as a blog; the paragraph + prediction is already slated for the master via `AIW-121`. |
| MoC7 poster not printed; organisers replied (social 08-21, MG) | `AIW-137`. MG: *"poster isnt even in final review with ME yet … a poster print is 5 minutes, a mistake or new cru result missed is much more work."* Organisers answered 08-20: **A0 portrait**, poster sessions daily except Wednesday, questions accepted during the conference so the ~12 Sept window is not a single missable gate. MG's vote remains unspent. |
| the July 2026 crucible→aIware consolidated backlog (14 originals) | it **is** `AIW-143`'s own untriaged list; payloads live in the named crucible record files and `cross-project/inbox-archive.md`. |
| companion rewrite P0 + P0 follow-up (crucible 08-06 ×2) | `AIW-124` / `AIW-140`. Theory-side absorption was done at S285 into `docs/smoc-middle-layer-draft.md`; **the companion method and claim text is the open half**, which is exactly what `AIW-218` and the new title ruling now cover. |
| rank settled + `P1…P5` collision (crucible 08-06) | rank → `AIW-124`'s SMoC M10 row. The notation collision gets its own line in `AIW-250` since it bites in a submitted draft. |
| methods finding + `AIW-201` collision answer (crucible 08-10) | `AIW-201`. crucible pre-registered entry conditions for the capability-null inversion (`cru83-m1s3-sufficiency-prereg.md` §12.6) so it cannot be invoked opportunistically after a null. **Do not promise an M1s3 number in any version.** |
| publication state: 4 forthcoming editions + ASIN matrix (infrastructure 07-20 and 07-24) | merged into `AIW-254`. |

### New backlog items — the five with no home

`AIW-250` · `AIW-251` · `AIW-252` · `AIW-253` · `AIW-254`. See `backlog.md`.

## The payloads worth keeping verbatim, because they are corrections to things we may have written

**A control we were told was measured is WITHDRAWN (crucible 08-13).** The renamed-region control
never measured anything. MG killed it with one question — *"are you testing if variable names
influence the result of the addition?"* The arm passes a different self-region label, but the
connectome builder reads that parameter in exactly two branches and the comparison ran in neither,
so both arms built the **identical** connectome from the identical seed; the "tie to three decimals"
was GPU floating-point noise (5e-9 to 1e-5) reported as a result, and the phrase *"inert, measured
rather than assumed"* inverted the truth. ⇒ **Any draft citing it must be corrected.** The claim is
not lost but re-grounded and stronger: the inertness is guaranteed **by construction**, since the
builder never reads the label unless the loop is being cut. General form worth carrying: *before
banking a control, check that the manipulated parameter is read on the path under test — grep the
branch, do not infer it from the signature.*

**Do not cite the targeted-lesion fragility numbers (crucible 08-05).** Red-teamed and cut down the
same day they were produced; v1's headline is retired. Re-source from
`~/crucible/docs/results/cru58-fragility-profile.md` **v2**, and note the whole result is a 126-unit
numpy analogue never run on the real substrate.

**Never cite `g` without its gauge and relay regime (crucible 08-05).** The 0.500-vs-0.389
discrepancy was **not** different lesion seeds — both numbers are right, being two factorization
gauges of the identical operator. `g` is gauge-dependent by 0.111 across realizations of the same
operator and erodes 0.500 → 0.110 under a strongly saturating relay. The separation from the fold
(0.069) is gauge-robust; the value is not.

**Decompilability was never a discriminator (MG, 08-05, verbatim).** *"the decompilation argument was
never meant as discriminator … so iii as discriminator is dead and was never alive."* It is a
**readout pipeline** — connectome → unrolled recurrence → language → correlate against imaging — with
MG's acceptance criterion *"predict from one fmri frame the next, with giving a reason why things
happen"*. ⇒ **If any companion text frames decompilability as separating closure from a closure-free
rival, it needs rewriting**, and **the paper should not promise a forthcoming discriminator at all**:
CRU-67 has no live candidate left.

**"SMALL and CONSISTENT" must travel together (crucible 08-13).** Removing one synapse in seven costs
0.5–0.7 percentage points of completion; moving that same cut to the self region costs a further
0.09–0.18. ⛔ Reporting *"23 of 24 individuals, p = 1.5e-06"* without the magnitude says the opposite
of what was measured.

**What the decomposition re-run buys, and it is more than was asked (crucible 08-13).** *No single
uniform filter constant reproduces the dual system* — refitting the folded pool's own constant across
nine values fails at every one. Without that, a reviewer can call the dedicated return a
re-parameterisation. Scope it exactly: this is a statement about the **construction**, not about
closure; it says nothing about whether the effect exists or is large.

**The "fixed point vs carried content" distinction is dead (MG, 08-11).** crucible's own
pre-registration §13.2 claimed the two readings *"predict opposite signs"* under restored true input.
They do not — persistence followed by reversion **is** slow reversion, and a rate difference is what
the red-team accused the DV of measuring. Only bistability would be a genuine sign difference. ⇒ **If
any companion text unpacks "self-consistency" as content persisting under contradicting evidence,
that reading does not survive.** The seam that does survive is cleaner: (i) does a stable
self-sustaining pattern exist at all, versus (ii) does that pattern track the body. Separately
falsifiable. Also worth having: a differential measurement across circuits defeats a *global gain*
confound but not a **stipulated** one — the self circuit's membrane time constant is 40 against the
world circuit's 20, so *"the self circuit holds longest"* is true by construction; what defeats it is
that a stipulated constant cannot move with exposure duration or change when closure is cut.

**Two crucible didactic patterns offered peer-to-peer (08-05).** *Pattern 45 — a conceptual
correction is not post-hoc fitting, and the agent must not adjudicate the difference alone.* MG:
*"Its not post hoc fitting if you do a wrong experiment on a wrong assumption and i correct you."*
The discriminator is a counterfactual: would this correction have been made if the result had come
out the other way? *Pattern 46 — a control is only as good as the variable it moves.* Two carefully
run controls both varied *rank* while the confound that governed the effect was *redundancy*; both
were real and both blind to it.
