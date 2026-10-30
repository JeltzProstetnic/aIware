<!-- Action: reference -->
<!-- Tracked-by: AIW-187 -->
# The allocation question — what does a saturated boundary fail to encode first?

**Status:** research note, S297 (2026-08-08). Tracks `AIW-187`, spun out of `AIW-186`. Continues
`drafts/aiw186-vacuity-regime.md` §7/§7a, which states the question and the candidate answer. Not paper
material.

**Result in one line:** the account gets the **sign of the spectral tilt right from architecture rather
than from fitting**, which is more than it was entitled to expect — and then the first version concrete
enough to carry a number **lands in an observationally excluded corner**, which is more useful than the
promise it replaces.

---

## 1. The account, restated compactly

A saturated boundary is one on which no further distinction can be encoded. Decompressing it writes the
**cheapest specifiable interior**, and in description-length units the cheapest interior is smooth and
thermal — a thermal bath is specified by one number, a uniform density by one more, while clumped
structure requires saying *where* everything is. This dissolves the apparent paradox in Penrose's
asymmetry (matter maxed, gravity minimal, at the same instant): thermal equilibrium is
**thermodynamically maximal and descriptively minimal at once**, and those are different quantities.

The correspondence that follows: **Weyl curvature tracks how much of the boundary's content has been
expressed as interior structure** — zero at the bang, growing monotonically as the orbit runs, maximal
at the clumped end-state where §5.4's saturation instability triggers.

## 2. The departure from uniformity is forced, not tolerated

A finite-capacity boundary **cannot** specify a perfectly uniform interior. Exact uniformity is an
infinite-precision configuration; the budget is finite; so a nonzero residual inhomogeneity is a
consequence of the capacity bound rather than an embarrassment to be explained away. This is the
"not all the way" constraint the span law's near-ceiling condition was expected to supply, arriving
from the encoding side instead — and it answers `AIW-186`'s third survival condition (*the universe is
homogeneous but not homogeneous*) structurally rather than by appeal.

## 3. The sign of the tilt comes out right, and it comes out for a reason

Boundary capacity is area-metered and the horizon area **grows**. A comoving scale is specified when it
was last in causal contact — earlier for larger scales. Therefore:

> **Larger scales were specified when less capacity existed, hence at coarser precision, hence with
> larger amplitude. More power at large scales is a red tilt.** `n_s < 1` follows from the fact that
> capacity is *accreting*, with no parameter chosen to produce it.

That is worth stating plainly because it is the one place the account currently outperforms its own
expectations: **the sign is a consequence of the architecture, not a fit.** Exact scale-invariance
(`n_s = 1`, Harrison–Zel'dovich) is the limiting case of *constant* capacity — equal description budget
per scale octave — and the observed tilt is the correction from capacity growth.

## 4. ⚠ The first number, and it fails

Make the account concrete with the weakest scaling ansatz that lets it be tested: let the amplitude at a
scale go as some negative power of the capacity available when that scale was specified,
`δ_k ∝ C(k)^(−α)`. Then the tilt is set by how fast capacity grows across the specification epoch, and
**nothing else** — there is no free function, which was the whole selling point.

That is exactly the problem. In the standard parameterisation, a tilt sourced by the background's
expansion rate alone, with **no potential-curvature analogue** (`η_V = 0`), gives

- `n_s − 1 = −6ε_V` ⟹ with the observed `n_s = 0.965`, `ε_V ≈ 0.0058`
- `r = 16ε_V ≈ 0.09`

and the observed bound is **`r < 0.036`** (BICEP/Keck, 95% CL). Excluded by roughly a factor of three.
Under a Hubble-flow parameterisation the arithmetic shifts but the conclusion does not; the tightest
version of the ansatz (`n_s − 1 = −4ε`) pushes `r` to ≈ 0.14, which is worse.

**The diagnosis is sharper than the number.** An account in which the tilt is produced by the growth of
a single geometric quantity **locks `n_s` to `r`**. That locked relation is precisely the corner of
parameter space that tensor bounds have been eliminating for a decade — it is where simple large-field
models like `m²φ²` sit (`n_s ≈ 0.967`, `r ≈ 0.13`), and they are excluded. **The capacity account, made
concrete in the obvious way, reproduces the excluded corner.**

**So the requirement on any successful version is now stated, and it is not vague: it must break the
`n_s`–`r` link.** Concretely, it needs a second parameter governing how capacity is *allocated across
scales*, independent of how fast capacity *grows* — an η-analogue that is not a reintroduced free
potential. Whether the architecture contains one is the live question. If it does not, the account
explains the smooth initial condition qualitatively and cannot compete quantitatively, which is
`AIW-186`'s condition 2 (*accommodation is not prediction*) biting on schedule.

**Status of this negative, honestly.** It is a **provisional kill of the concrete version, not of the
programme**, for one specific reason: the account does not yet derive `δ` from `C` at all, so `α` is
stipulated rather than obtained, and the mapping onto slow-roll parameters imports machinery the account
may not be subject to (see §5). What the calculation establishes is the **target**: any version worth
pursuing must land `n_s ≈ 0.965` while keeping `r` below 0.036, and must say why those two are not
locked together.

## 5. ⚠ A structural problem that outranks the number

"A mode is specified when it was last in causal contact" is **inflation's apparatus** — horizon
crossing, freeze-out, and a quasi-de-Sitter background against which "when" is defined. If the capacity
account needs that background to state itself, it is **not a rival to inflation; it is a redescription
of inflation in description-length units.** That would not be worthless, but it is a different and much
smaller claim than the one `AIW-186` §6a is chasing, and it would forfeit the horizon-problem rivalry
entirely.

The bounce framing avoids the problem and is where the account actually belongs (`AIW-186` §5 places it
in the cyclic class beside CCC on independent grounds): the boundary at the end of the previous cycle
saturates, and the initial data of the next is written at decompression. But then **scale allocation has
to be stated without horizon crossing** — how the saturated boundary's bits map onto comoving scales of
the successor interior. Nothing in the thread says how, and until it does, §4's calculation is testing a
hybrid that belongs to neither picture.

**⇒ The next step is not a better estimate. It is to state the allocation rule in bounce language.**
That is the single blocking item, it costs no GPU and no new physics, and §4's number becomes meaningful
only once it exists.

## 6. What this changes upstream

- **`AIW-186` §6a's "most promising thing in the thread" survives but is downgraded from *promising* to
  *constrained***: the qualitative story is intact and the sign result is a genuine, unexpected asset;
  the quantitative route now has a named obstacle rather than an open horizon.
- **The numerology trap flagged in `aiw166-cosmos-transfer.md` §6a is confirmed from the other side.**
  The naive residual-counting argument fails on the spectral shape (`P(k) ∝ k⁴`); this one fails on the
  tensor bound. Both failures are the same underlying fact — **an account with one parameter cannot
  independently fit amplitude and tilt** — and it should be stated once, in that form, rather than
  rediscovered per attempt.
- **Nothing here touches the vacuity verdict.** `AIW-186`'s regime branch stays discharged; §4 is about
  whether the inversion can compete, not about whether the closure claim is contentful.
