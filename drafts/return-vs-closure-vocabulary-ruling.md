# The closure-language package for the FMT master — three decisions that have to be made together

> ## ⚠ STATUS UPDATED S309 (2026-08-24) — most of this file is now APPLIED. Read this box first.
>
> The line below once read *"nothing in this file has been changed in the paper."* That is no longer
> true, and the file is kept for its reasoning, not as a to-do list.
>
> | part | state |
> |---|---|
> | **B** — the false claim at `:338` | **APPLIED S307** (`f6cf1a82`). Now reads *"can sever from the rest of the system"*. |
> | **C** — the rename at `:340` | **APPLIED S307** (`f6cf1a82`). The non-equivalent *"or ablation of the explicit self-model"* alternative is gone. |
> | **A, Group B** (4 places) | **APPLIED S309** (`aa92e7c4`), both `.md` and `.tex`. |
> | **A, Group D** (option (a)) | **APPLIED S309** (`aa92e7c4`). ⚠ **Three occurrences, not the two counted below** — the near-ceiling condition is stated twice in §8.9's eighth banked result, once in the headline list and once in the elaboration. |
> | **A, Groups A and C** | **DELIBERATELY UNTOUCHED**, for the reason given in the Group C section. |
>
> **Two things still need MG and nothing else does:**
> 1. **Group C** — leave the graph-theory terms of art as they are (the recommendation), or replace them
>    with *"acyclic"* / *"acyclicity"*. **Not** with "closure": that collapses the 5.3× / 6.0× distinction
>    the sixth banked result is priced on.
> 2. **The erratum question** — does v15 carry an erratum for this package and for the two §8.9 repairs
>    already made, or do they simply ride in v16? **None of the numbers change.**
>
> Also for the record: **crucible must be told Group C is deliberate**, so their side does not sweep it
> and re-open the divergence they stopped at.

> **Why one package and not three.** Crucible confirmed on 2026-08-23 that these interact. A
> mechanical "use closure everywhere" pass would erase the very distinction that item C below
> introduces, on the day it is introduced — and it would make "closure" name two different objects
> across §8.7 and §8.9. Ruling on one without the others produces a paper that contradicts itself.

**Contents:** **A** — the ten "return" places · **B** — a false claim at `:338` · **C** — a rename at `:340`.

---

# A. "Return" vs "closure" — the ten places
Raised by crucible 2026-08-11, who swept their own prose and deliberately stopped at the paper's
edge: *"changing it here while the paper says something else would create a divergence — the call
is yours."*

Your ruling, as they recorded it: *"i explicitly said use closure, not return. if return is
closure, use closure."* Where a sentence needs the mechanism rather than the property, the agreed
phrasing is *"feeding back into the same population"*. `bottleneck` stays.

**They were right that it reached the published paper.** A#9's fourth measured condition reads
*"and reads back over a short return"* in FMT v15, in both the `.md` and the `.tex`.

---

## The finding: ten occurrences, and they are not one thing

A blanket find-and-replace would damage the paper. The word does three different jobs.

### Group A — ordinary English verb. Leave alone. (3)

`:338` *"returns a negative verdict"* · `:626` *"tend to return two closed systems"* ·
`:753` *"the substrate returns to a subcritical state"*

Nothing to do with the FMT term.

### Group B — the retired noun, and your ruling applies cleanly. (4)

| # | Line | Now | Proposed |
|---|---|---|---|
| 1 | `:419` | "what **the return** of its output into the world-model's update rule buys is self-consistency" | "what its output, **fed back into** the world-model's update rule, buys is self-consistency" |
| 2 | `:427` | "closure is **the return** *over* what the channel holds" | "closure is the **pass back** *over* what the channel holds" |
| 3 | `:981` | "the cycle that carries **the return**" | "the cycle that **closes**" |
| 4 | `:981` | "observing the disturbance would require reading the driven subsystem, which *is* **the return**" | "…which *is* **the closure**" |

Item 1 is the §3.6.1 decomposition sentence. Its own next clause already says *"only the second is
closure"* — so the retired word is not even carrying the meaning there; it is redundant with the
sentence that follows it.

### Group C — ⚠ graph-theoretic terms of art. Substituting "closure" here would make the paper wrong. (3)

`:626` *"cannot be made **return-free**"* · `:626` *"which of its subsets sit inside a **returning
component**"* · `:981` *"region-level acyclicity implies neuron-level **non-return**"* ·
`:981` *"Buying **return-freedom** — no closed walk anywhere"*

The sixth banked result turns on a distinction between two *different* prices: opening the global
loop costs 14.0% / 12.0%, and **return-freedom** — no closed walk anywhere — costs 74.0% / 71.5%.
The paragraph's whole argument is that the cheap operation **relocates** closure and only the
expensive one abolishes any path back. Call both of them "closure" and the 5.3× / 6.0× multiplier
stops meaning anything.

**Recommendation: keep these, and if the word still bothers you, the honest replacement is the
graph-theory term itself — "acyclic" / "acyclicity" — not "closure".**

### Group D — the two A#9 phrases crucible specifically flagged. (2, and these are the awkward ones)

`:981` *"must be delivered near the ceiling of what the architecture can achieve, and **reads back
over a short return**"*
`:981` *"survives to an exchange rate of roughly 1732 when **the return is a single stage** and only
210 when it is eight"*

Here "return" is doing quantitative work: it is the thing being **measured in stages** (one stage
vs eight). "A short closure" and "the closure is a single stage" both read wrong. Options:

- **(a)** *"reads back over a short path"* / *"when the path back is a single stage"* — cheapest, keeps the measurement legible.
- **(b)** *"closes over a short path"* / *"when the closing path is a single stage"* — keeps your word visible, slightly heavier.
- **(c)** leave both, on the grounds that a measured stage-count is a mechanism and not the property.

**My recommendation is (a).** It removes the retired noun without pretending a stage-count is a
property, and "path" is already the paper's own word two sentences earlier ("through a path of far
lower rank").

---

## A — what I'd do, in one line

Apply **Group B (4 edits)** and **Group D option (a) (2 edits)**. Leave Group A and Group C alone,
and tell crucible that Group C is deliberate so they don't sweep it on their side and re-open the
divergence.

---

# B. ⚠ A claim at `:338` that the measurement says is false

**Current text, verbatim** (`paper/full/four-model-theory-full.md:338`, mirrored at
`paper/full/latex/paper.tex:453`):

> "The self at issue is the explicit self-model, a closure-dependent state that **efferent
> disconnection of the self region can remove**;"

**It does not remove it.** Crucible measured the two cuts separately and they are not even nested
(`~/crucible/docs/decisions.md`, 2026-08-12 night ruling; you were asked and said *"no idea,
crucible is ground truth"*):

| cut | cost | what is left |
|---|---|---|
| efferent disconnection of the self region | **14.03%** of synapses | **two** closed systems — the self region keeps its own returning structure entirely intact |
| cutting the self region's own recurrence | **6.23%** | **one** closed system |

So the sentence names the cut that **leaves the self-model closed on itself** and claims it removes
it. The cut that actually removes the self region's closure is the cheaper one nobody had separated
until this ruling.

⚠ **This is where the interaction bites.** Crucible's suggested repair is *"a closure-dependent
state that opening the self region's closure removes"* — and **I do not recommend applying that
string**, because it uses "closure" for the *region-level* self-loop. If your use-closure-never-return
ruling also rewrites the global-loop language in §8.9, "closure" then names two different objects a
few pages apart, which is exactly the distinction the sixth banked result prices at **5.3× / 6.0×**.
Crucible agrees and declined to sign their own wording for that reason.

**What I'd propose instead:** *"a state that the self region's own recurrence sustains, and that
cutting that recurrence removes"* — names the mechanism, avoids the overloaded word, and is true of
the 6.23% cut. **Your call.**

*Scope on all of the above: structural, region granularity, one synthetic connectome family.
Dynamical survival is unmeasured — crucible filed CRU-99 and has not run it.*

---

# C. A rename at `:340`, and a second mechanism the sentence doesn't defend

**Current text, verbatim** (`:340`, mirrored at `paper.tex:455`) — the dolphin
signature-whistle criterion:

> "under an identical language bridge, efferent disconnection of the self region **— or ablation of
> the explicit self-model —** should abolish self-recognition while leaving the taught label intact
> and still producible."

**The interpolated clause is a category error on your own death-boundary axis** — "the explicit
self-model" is the process, and what a wiring cut removes is structure. Crucible's proposed
replacement, which they sign:

> **"— or removal of the self region's self-recurrence —"**

**Plus one thing they raised unprompted and I think they're right about:** as written, the sentence
asserts **one** mechanism for **two structurally different cuts**. Both plausibly abolish
self-recognition, but for different reasons — disconnection cuts the route out, de-recurrence
removes the referent. The sentence should not assert a single mechanism it never defends. Cheapest
honest fix is to name both and claim only the shared prediction.

---

# Cost if you say yes to all three

Eight to ten edits across `paper/full/four-model-theory-full.md` and `paper/full/latex/paper.tex`,
one rebuild, and one decision that covers this whole package: **does v15 get an erratum, or do these
fixes simply ride in v16?**

**None of the numbers change.** The same erratum question applies to the two §8.9 repairs already
made this session — the false "order of magnitude per subsystem" quantifier (now stated as the
elevenfold-then-under-threefold steps it actually is) and the scope clause that under-claimed a
four-condition result as one.
