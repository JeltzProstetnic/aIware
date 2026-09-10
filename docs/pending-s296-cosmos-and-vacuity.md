<!-- Action: reference -->
<!-- Tracked-by: AIW-186, AIW-184, AIW-182, AIW-181, AIW-162 -->

> **⚠ SUPERSEDED S297 (2026-08-08) — do not act on this file. Demoted `act` → `reference`.**
> Everything it asked for was executed or explicitly resolved:
> **`AIW-186`** — the discussion MG asked for is `drafts/aiw186-vacuity-regime.md`; the vacuity objection
> **fails** (it equivocates *containment* for *closure*) and the regime branch is discharged. Spun out:
> `AIW-187` (allocation — worked to a number, the concrete version is excluded) and `AIW-188` (done).
> **`AIW-184`** ✅ done · **`AIW-181`** ✅ done · **`AIW-162`** ✅ done ·
> **`AIW-182`** left open **deliberately** — bundle-blocked into the `AIW-124` reopening pass.
> The live handover is **`docs/pending-s297-inbox-remainder.md`**. Keep this file only as the S296
> record; delete it when `AIW-186` and `AIW-182` close.
# S296 handover — the vacuity regime, and what else is unblocked

**MG asked for one thing by name: a deeper discussion of the vacuity regime (`AIW-186`).** Everything
else here is context or secondary work.

**Read first:** `drafts/aiw166-cosmos-transfer.md`. It is the whole cosmos thread in one place — the
Occam/span-law interlock (§4), the nesting-trichotomy falsifier (§5), ESM = EWM as the degenerate-limit
answer to `AIW-167` (§6), MG's inversion (§6a), the binding discipline rules (§7), and what is still
open (§8). Do not reconstruct the thread from this file; this file only says where to start.

## The discussion MG asked for

The vacuity hazard, stated at full strength: if a universe with no outside is one strongly-connected
component, it is **closure-ON by construction**, no OFF arm exists, and *if everything is closure,
closure discriminates nothing.* CRU-58 warning (D) is the precedent — a genericity claim confirmed "by a
mundane and total mechanism", true and near-vacuous. CRU-36 bites from the other side: a homogeneous
reservoir re-entered into itself collapses into one undifferentiated pool, and **a pool can be critical
and self-connected and still model nothing.**

**Then MG inverted it the same evening, and the inversion is the reason this is worth a session:**
*"this might explain entropy and the enormous homogeneity of the universe."* If the cosmos is that
structure, homogeneity is **predicted** rather than accommodated, and the horizon problem gets a rival
answer to inflation.

### Carry these four verbatim into the discussion

1. **⚠ In gravitating systems homogeneity is LOW entropy, not high** — Penrose's Weyl-curvature
   hypothesis: smooth is low-entropy, clumped is high. So this is **not** an explanation of entropy
   *increase*, and stated that way it runs against the second law. **Aim at the smooth low-entropy
   INITIAL condition** — the Past Hypothesis, ~1/10^10^123 — which **inflation presupposes rather than
   derives** (Penrose's standing objection: inflation needs a low-entropy start to begin). That target
   is unoccupied and far more valuable.
2. **Accommodation is not prediction.** Inflation is quantitative (`n_s ≈ 0.965`, acoustic peak
   positions, near-scale-invariance). A qualitative "the architecture forces smoothness" accommodates a
   known fact, which is exactly the post-hoc vulnerability the formalization paper names as the theory's
   largest liability. Numbers, or it does not compete.
3. **The universe is homogeneous but NOT homogeneous** — 1 part in 10⁵, and the anisotropies are where
   all structure comes from, observers included. A pure pool-collapse predicts *complete* homogeneity,
   which is falsified. The explanandum is near-but-bounded-away-from uniformity, so the architecture
   must deliver the **departure** too. Best place to look: the span law's **near-ceiling** condition,
   which is exactly a "not all the way" constraint, and which the minimality thesis needed anyway.
4. **It must FORBID one outcome.** Compatible with both a smooth and a clumpy universe = explains
   nothing. This is `AIW-186`'s regime requirement arriving from the other direction.

**A legitimate outcome of this discussion is "true and vacuous, concede it."** That is far better than
shipping the vacuous version, and it should be on the table from the start.

## Also open and unblocked — no dependencies, take in any order

- **`AIW-184` (P2)** — the single-locus postulate must carry **jointness** and **minimality** explicitly
  wherever it is restated. Read distributively it is a local hidden-variable model yielding CHSH ≤ 2 —
  refutation-shaped, not merely weaker. Correct wording is in
  `drafts/aiw174-entanglement-wedge-postulate.md` §4 (L1/L2/L3).
- **`AIW-182` (P2)** — the companion's §7 still frames the central dependency as capability-*loss*,
  which is the pre-2026-08-06 necessity framing. Revise to cost-at-matched-function. **Bundle with
  `AIW-140`** (the "Enabling Conditions" title) and with crucible's incoming A#7/A#8/A#9 companion
  drafts — one revision pass, not three.
- **`AIW-181` (P1)** — the ablation-validity audit binds any future Phase-4 run *now*, not at the next
  Zenodo version: SCC decomposition, enrichment-corrected dominant-loop-mode, and verification that the
  removed mechanism has not reconstituted, all **before** results are read.
- **`AIW-162` (P2)** — purge "simulation" from the cosmology body where avoidable (MG: *"everyone will
  think another matrix theory"*). **Title is already clean**; 31 body instances need triage, not a
  blanket replace. Scoped to cosmology only — the book's title is deliberate, do not touch it.

## Waiting on others

- **Crucible** owes the companion-side A#7/A#8/A#9 explanation drafts (requested S296, no deadline
  pressure — that side rides the AIW-124 `[[CRUCIBLE:]]` fill at MoC7 weeks 6.5–8).
- **Infrastructure** owes the `fmt.matthiasgruber.com` rebuild (deploy is 11 versions stale) and the
  `matthiasgruber.com` publications-index repair.
- **cfg-agent-fleet** owes the `filtered-push.sh` fail-closed non-determinism fix — it fired a second
  time on 2026-08-08, on `.claude`, with `git ls-files --cached -- .claude` returning 88 files while the
  guard's warning claimed zero. **Operational note for the next session: if the push refuses with that
  impossible pair of messages, re-run it — it succeeds.** Verify the public mirror afterwards.

## Standing discipline from this session — do not re-derive, do not relax

- **Never publish the "we are the universe's qualia" wording** (MG-directed 2026-08-08).
- **Cite the generator-vs-output distinction** (`K(rule) ≪ K(orbit)`, uncontested), **never Wolfram's
  Physics Project** — contested, and it hands a hostile reviewer their opening move.
- **Cosmology and FMT stay decoupled in public** until the cost question closes.
- **Accumulate into ONE cosmology rewrite** — never a version per finding.
