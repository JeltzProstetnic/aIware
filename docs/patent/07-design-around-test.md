# 07 — The design-around test (S302, 2026-08-12)

**Not legal advice.** An in-house adversarial engineering test, run because MG correctly observed that
**this question is ours and not counsel's**: a patent attorney rules on validity, but whether a claim set
*forces a competitor to negotiate* needs someone who knows spiking substrates, the fold theorem and
multi-kinetics synapses.

**MG's decision rule, verbatim (2026-08-12):** *"one fable pass for now. if a fable pass finds a way around
its done. if not we consider."*

**RESULT: ESCAPE FOUND. The lane closes.**

**Method:** one Fable agent briefed as a competitor's principal engineer, tasked to ship the capability
without infringing, and **deliberately blinded to `05-red-team.md`** so that agreement would be independent
confirmation rather than restatement.

⚠ **Independence caveat, self-reported and worth keeping:** `06-claim-architecture-v2.md` embeds the
drafter's own design-around table in its §5, so a reader of the claims cannot be fully blind. The agent
labelled which findings were absent from that table. **The load-bearing findings below are the new ones**
— the FORCE costing, the branch-(ii) drafting gap, the modulatory return, and the black-box
unprovability. That is what makes this a test rather than an echo.

---

## 1. The verdict, in the form that answers the €15k question

> **Advising my own CEO: do not take a licence; route around.** … As it stands, this claim set, filed as
> drafted, does not force a competitor to the table.

Multiple independent **literal** escapes exist for every family; several cost approximately nothing *on the
patentee's own evidence record*; and the central structural limitation is unprovable from outside a product.

## 2. Claim 1 (family A, the best claim) — escapable through its own admitted prior art

Novelty lives entirely in **L2 + L5** (the routing: an alignment region interposed between sensory input
and the designated region, with plasticity confined by a connection mask). L3/L4/L6 are the admitted
Izhikevich skeleton. Infringement requires *every* limitation, so escaping through an admitted-art element
is legally clean — and the claim **cannot be broadened to cover published rules without ensnaring the art**.

- **The cheapest escape breaks L3 with a pre-synaptic-only trace.** Train the alignment stage with a
  delta-rule / feedback-alignment scheme: traces filtered from *pre-synaptic* activity only, maintained
  **per source neuron** rather than per connection. Two literal misses at once — the trace is not updated
  from "pre-synaptic **and post-synaptic** spike activity of that connection", and it is not maintained
  "for each … connection". Both the delta rule and feedback alignment (Lillicrap) are pre-priority
  published art, so **equivalents cannot reach them**.
  **Cost: 0–15 % sample efficiency, worst only on long-delayed-credit tasks; ≈ 0 for the alignment-refit
  use case that matters. Trace memory drops from O(E) to O(N) — an outright improvement.** Budget 2–4
  engineer-weeks to benchmark. **Ship: yes.**
- **Backup: e-prop-style traces** (Bellec 2020, verified unpatented in `02`) build the trace from the
  post-synaptic *membrane-potential pseudo-derivative* — arguably not "spike activity", and with better
  measured performance than plain three-factor rules.
- **Break L2 with output-side alignment** — put the adaptable transform on the prediction side of the
  frozen region instead of between sensor and region. Literally unmet. ≈ 0 cost when modalities match.
- **Break L5 with soft-freezing** — EWC-style regularisation toward stored values instead of a mask.
  Downstream weights measurably change, so they are not "held fixed". (⚠ The sham version — epsilon
  learning rates — invites an equivalents finding. The honest version is a real functional difference.)
- **Venue and substrate** (already conceded in `06` §5): factory training by surrogate-gradient BPTT
  practised in private, in a chosen jurisdiction; or a rate-based alignment stage escaping L1 entirely.

⇒ **Four independent outs on the strongest claim, two resting on published art**, with the few-shot
capability fully intact.

## 3. Claim 15 (family B) — the drafter's "self-defeating" escape is not self-defeating

**The finding that matters most, and it inverts an assumption in `05` §5.** The folded factored return —
low-rank readout re-injected through the *shared* synaptic filter — is behaviourally identical to the
claimed machine by **MG's own fold algebra** (*"ties exactly, term for term"*). `06` §5 dismisses this as
self-defeating for a competitor. **That label is unearned on today's evidence:**

1. **Kept in factored form** (never materialising `W_fb·W_out` into a dense matrix), it has the **same
   synapse and memory economy** as the claimed non-foldable return — and the 7.9× economy figure was
   itself measured on folded arms.
2. **The claimed advantage of the non-foldable loop over this configuration is PROPHETIC.** Per the
   project's own ledger, **E1 and E4 have never been run.** There is no measured benefit being forfeited.
3. **This configuration is FORCE** (Sussillo & Abbott 2009), confirmed in `02`. A competitor practising it
   is practising 2009 prior art, which no drafting, amendment or equivalents theory can reach.

**Cost of this escape: zero measurable, today.**

Two further escapes, both new:

- **The modulatory return — currently unclaimed entirely.** The capability spec says the self-model must
  influence the world-model's *update rule*, "not merely feed it as an input" — yet an additive re-injected
  current, foldable or not, is exactly feeding it as an input. The natural engineering realisation is a
  **gain / threshold / time-constant modulation** return. It meets **none** of branches (i)–(iii), sits
  outside the "re-inject as input" preamble, and trivially satisfies non-foldability because a
  multiplicative interaction is not an additive weight modification. Since the "such that" clause is drafted
  as a *consequence* of the Markush rather than as a free-standing limitation, failing all three branches
  ends the inquiry. Cost: 2–3 engineer-months of stability tuning, in exchange for arguably a **better**
  match to the stated capability.
- **⚠ A genuine drafting hole in branch (ii).** It requires the return delay to **exceed** the delay of
  *every* recurrent connection onto the target neurons. Give the recurrence one functional sparse
  long-delay pathway — return at 5 ms, recurrent delays {1 ms, 10 ms} — and no recurrent channel exists at
  5 ms, so **the loop genuinely does not fold**, yet (ii) is literally unmet because 5 < 10. A non-foldable
  return that escapes all three branches, at near-zero cost. **The fix is one word: "differing from",
  not "exceeding".**

Agreed with the drafter on one point: the relay-population escape *is* materially harder after claim 20
plus the spec definitions, and would not be attempted.

## 4. Family C — no claim text exists, and the intended core is escaped by weight-sharing

Run entity-prediction on a **weight-sharing clone** of the frozen self-model: shared read-only parameters,
separate dynamical state. Whether that is "the same instance serving both concurrently" is a construction
fight the accused party starts ahead in. Cost ≈ duplicate state memory only. Any prediction-only or
advisory product escapes an actuation recital outright.

## 5. ⚠ The structural irony — the fold theorem makes infringement unprovable

**Because the folded and unfolded machines are I/O-identical by MG's own record, no external behavioural
test can ever distinguish an infringing return from a FORCE-style one.** Enforcement requires white-box
access: weights files, or silicon reverse-engineering. **A competitor shipping opaque configured hardware
is effectively unauditable.**

Method claims fare no better — training happens in private and the venue is selectable. Only on-device
learners expose the rule, via firmware and synapse-memory layout.

## 6. What would make it bite — on file if crucible ever changes the evidence

Kept because the family is **not yet filed**, so all of it remains fixable. In the agent's priority order:

1. **Broaden every admitted-art element of claim 1.** *"At least one locally maintained eligibility
   variable computed from activity of at least the pre-synaptic neuron"* — drop "and post-synaptic", drop
   "spike", drop per-connection maintenance; demote the pre×post trace to a dependent. Validity survives
   because novelty is carried by L2+L5. **As drafted, L3 is the single biggest hole in the portfolio's
   best claim.**
2. **Capture output-side alignment** — recast functionally as adapting parameters *outside* the designated
   region while the designated region is held fixed.
3. **Close the soft-freeze door** — define "held fixed" to include confinement by learning-rate reduction
   or weight-change penalty, with a quantitative floor.
4. **Fix branch (ii)** — "differing from", not "exceeding every".
5. **Claim the modulatory return** — a fourth Markush branch or sibling independent covering modulation of
   gain, threshold, time constant or plasticity parameter. (Check art first: gain modulation is old, but
   *a low-rank self-summary modulating a recurrent world-model* may still be clean.)
6. **Run E4 before spending anything on family B.** Until a measured gap over the folded factored
   comparator exists, family B fences a construction nobody is forced to build. If the gap turns out to be
   in *trainability through the loop* rather than synapse count, redraft the wherein around the trained
   system rather than the static architecture.
7. **Add externally observable claims**, or the set stays white-box-only: promote the synapse-memory
   data-structure dependent; add a method-of-use claim keyed to measurable few-shot adaptation behaviour;
   for family C, recite "a second instance **sharing parameters** with the first" to kill the clone escape.

## 7. Conclusion

**The lane closes on MG's stated rule.** The escape was found — several of them, two on published art, at
a cost bounded by one internal benchmark rather than the 40 % threshold that would have made the patent
commercially real.

**The single condition that would reopen it:** E4 demonstrating a large, real cost-or-trainability gap
attributable specifically to the non-foldable return — **and** a refile with the seven gaps above closed.
That is a software experiment, not a purchase, which is the encouraging part: the cheapest route to a
stronger patent position was never the €15k.
