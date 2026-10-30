# AIW-130 JAIC draft — independent re-check after the S362 claims revision

Manuscript: `drafts/aiw130-jaic-draft.md` (HEAD 65265a3a, 302 lines). Read fresh and checked against the
primary sources, not against the audit or change log:

- companion source `drafts/companion-computational-paper-draft.md` (published v6, concept DOI 10.5281/zenodo.21610993);
- `~/crucible/docs/cru226-juelich-substance.md` §4 "Must NOT claim";
- crucible results: `p1-causal-transfer.md`, `cru40-b1-R1-S0pre2-gridworld-fitted-arms.md`, `cru32b-self-preservation.md`
  (via `fmt-evidence-ledger.md`), `artifact-audit-2026-10-07.md`;
- Kanai & Ma full text `literature/fulltext/Kanai2026.pdf` (fitz). All quoted Kanai & Ma strings were found verbatim,
  and the section pins are correct: §9.2, §9.3, §9.4, §4.7 ("deliberately leaves open"), §7.4 (duplication and
  branching), Definitions 9–11.

Line numbers refer to the current draft.

**Verdict: the S362 fixes hold and none went too far. Four in-silico statements are still wrong or not quotable
(l.154 twice, l.174, the §6 heading). Each takes a one-clause fix. No BLOCKER remains.**

---

## 1. In-silico claims, sentence by sentence

### F1 — MAJOR — l.154: the companion's regime result is a positive one
> "the companion's positive results were obtained with no regime manipulation, so none of them manipulates closure and the open-ended regime together."

**Problem.** The second half is true. The first half is false. Companion §4.4 is a positive result produced by a
regime manipulation: a 41-point spectral-radius sweep with a measured driven Lyapunov exponent, replicated on 30 of 30
reservoirs. The manuscript cites that result two sentences earlier (l.152). The audit's B3 text scoped the claim to
"positive capability results (§4.1–4.3)", and the applied text dropped that scope.
**Source.** Companion §4.4 (l.139–141); audit l.40.
**Fix.** "…and it is untested: the companion's closure-side results (§4.1–4.3) were obtained at one fixed regime,
and its regime result (§4.4) manipulates no closure, so no experiment varies the two together."

### F2 — MAJOR — l.154: the re-entry null is AT RISK
> "One toggle of re-entry on an undifferentiated spiking reservoir gave no advantage on a task the passive reservoir already solved (Gruber, 2026b, §6), which the framework expects…"

**Problem.** This is the CRU-36 null. The unbounded-membrane audit lists it as AT RISK ("null, could move either
way"), and it has not been re-run under the membrane floor. CRU-226 §4 item 6 puts it on the must-not-claim list. The
audit noticed this (m8), but the B3 fix only added the "already solved" clause. The result is still stated as settled.
**Source.** `~/crucible/docs/results/artifact-audit-2026-10-07.md` l.21 and l.68 ("CRU-36 not re-run");
CRU-226 §4.6.
**Fix.** Delete the sentence. The interaction point stands without it. To keep it, mark the scope inside the claim:
"…(Gruber, 2026b, §6; under re-analysis for a membrane-model artefact)…".

### F3 — MAJOR — l.174: a graph result is cited for a dynamical claim
> "Mutual dependence between two coupled recurrent sub-partitions is common; on the companion's model connectome, closure is what recurrence already gives (Gruber, 2026b, §5.1). Conditions (i)∧(ii) alone therefore discriminate little…"

**Problem.** Companion §5.1 measures graph closure: minimum-synapse cuts to open the loop or to make the graph acyclic.
It says so explicitly: "This is a claim about graph structure and not about dynamics … dynamical survival of the
residue is unmeasured". Conditions (i)∧(ii) are counterfactual dependence of conditional transitions, which is a
dynamical property. A reviewer who reads §5.1 will find the disclaimer.
**Source.** Companion §5.1 l.177; §8 l.248.
**Fix.** "…on the companion's model connectome, a returning path through the self region is what recurrence already
gives (Gruber, 2026b, §5.1; a graph result). Mutual dependence plausibly comes as cheaply, so the closed-loop form of
(i)∧(ii) discriminates little, and the discriminating content sits in the off-line clause of (i) and in the
representational condition (iii)."

### F4 — MAJOR — l.146 heading and l.162: "runnable"
> "## 6. Constructive grounding — the detector is runnable" · "the evidence is a specification of a runnable detector"

**Problem.** Nobody has implemented the checks. The body says the design is "not yet instantiated" (l.150) and that
"the checks have [not] been run" (l.162). §4 l.76 concedes that "the extraction is not yet fully automated at scale".
So "runnable" claims more than the evidence shows. A heading is the most quotable string in a section. The change log
left this open (For MG, item 3).
**Source.** The draft itself (l.76, l.150, l.162). The companion has no detector implementation.
**Fix.** Heading: "6. Constructive grounding — the detector specified to implementation". l.162: "…the evidence is
a specification precise enough to implement, plus a set of capability dissociations consistent with the mechanism."

### F5 — MINOR — l.152: the survival result has no number and no pin
> "Prospective self-in-simulation yields a behavioural survival advantage over a matched reactive agent."

**Problem.** This is the only result in the paragraph without a number or a section pin. The companion calls it small,
a toy, an existence result (0.29–0.33 vs 0.17–0.25). m6 is confirmed. The result is safe under the artefact audit
(gridworld, A#5) and is not a FlowBody run.
**Source.** Companion §4.2; `cru32b-self-preservation.md`.
**Fix.** "In a toy survival task, an agent acting on its self-model's survival prediction outlives a matched reactive
agent by a small margin (0.29–0.33 against 0.17–0.25; Gruber, 2026b, §4.2)."

### F6 — MINOR — l.152: "only for tasks of intermediate difficulty"
**Problem.** That holds at N = 300. The hard task lifts off chance with size, and at N = 2000 it peaks at λ ≈ −0.38.
**Source.** Companion §4.4 l.139, l.141.
**Fix.** "…an accuracy peak appears only for the medium-difficulty task at the base size…"

### F7 — MINOR — l.154: "an interaction, not a main effect"
**Problem.** The text does not say whose main effect. Two sentences earlier the paragraph cites a regime effect with
no closure (§4.4), and §8 counts closure main effects (planner, survival) as corroborated. Read literally, the
sentence contradicts both.
**Source.** `prediction-framing.md` ("no main effect of criticality absent closure"); companion §4.4.
**Fix.** "The discriminating prediction is an interaction: the closure advantage should depend on the substrate
keeping its open-ended capability."

### F8 — MINOR — l.82 and l.84: check 3's neural readout has no surrogate
**Problem.** After B6, §6(a) l.150 and §6(c) l.164 count a branching ratio only beside a rate-matched surrogate. Check 3's
neural readout (l.82, "a branching ratio near unity") still lists it bare, and l.84 calls the criticality signatures
"the best-validated readout" (m5). The companion records that the subsampled branching ratio "has already failed as
a stand-alone certificate". m5 is confirmed.
**Source.** Companion §3.2 l.105, §8 l.250; CRU-226 §4.2.
**Fix.** l.82: "…a branching ratio near unity reported beside a rate-matched surrogate…". l.84: "…only as a
corroborating readout for that property in self-organizing tissue…".

### F9 — MINOR — l.156: "tuned to a critical spectral radius by fiat"
**Problem.** The companion's own scan shows that the nominal setting ρ = 1 lies in the ordered regime (λ ≈ −0.12) and
that the edge sits near 2.6. "Critical by fiat" reads as ρ = 1, which the companion shows is not critical.
**Source.** Companion §3.2 l.107, §4.6 l.159.
**Fix.** "…a rate reservoir set to its measured edge (driven Lyapunov exponent ≈ 0) versus a self-organizing spiking pool…"

### F10 — MINOR — l.64 and l.156: "in rate reservoirs the … optimum sits in the … ordered regime"
**Problem.** Confirms m4. The evidence is one replicated reservoir family plus two cited literature results, and five
further scans gave nulls or ordered-side results.
**Source.** Companion §4.4.
**Fix.** "in the rate reservoirs tested so far (Gruber, 2026b, §4.4)".

### F11 — MINOR — l.162: "the floor of that capacity band"
**Problem.** "Capacity band" occurs nowhere else in the manuscript, the companion or `paper/full`. The sentence places
the toy systems relative to a threshold no source defines.
**Fix.** "…or that the mechanism has been shown at scale; the toy systems are far smaller than any system FMT
holds conscious…". Alternatively cut the clause.

### F12 — MINOR — l.78, l.150, l.164: self-attractor formation is stated as fact
**Problem.** M7 hedged l.74 ("plausibly … This is a hypothesis … the self/world split was built in"). The same claim is
still stated as fact in three places:
- Check 1 (l.78): "the body is the highest-mutual-information … regularity";
- §6(a) (l.150): "an attractor world-model carves a self-basin", in the present tense, for a design not yet built;
- §6(c) (l.164): "so decodable self-attractors form; pass".

CRU-226 §4.3: self/world differentiation is hardcoded (construction, not emergence).
**Fix.**
- l.78: "the body is plausibly the…";
- l.150: "would carve";
- l.164: "suppose decodable self-attractors form".

---

## 2. Internal consistency

### F13 — MINOR — l.174 vs Box 1 l.110, l.120 and l.80
**Problem.** After M8, §7 says (i)∧(ii) "discriminate little". Box 1 still calls (i)∧(ii) "the primary pass
condition", and check 2 is "the crux". The F3 fix removes the conflict, because (i) already contains the off-line
clause. If F3 is not applied, Box 1 needs one clause saying the discriminating part of (i) is its off-line form.

### F14 — MINOR — l.196: an untested item sits in the corroborated list
> "On the corroborated side sit … The predicted interaction between closure and the open-ended regime is untested."

**Fix.** Move the sentence to the untested side (after "On the untested side sit…"), or cut it. §6 already states it.

### F15 — MINOR — l.194, l.78, Box 1 l.116, Fig. 1 alt text: "decodable" and $L_W$
**Problem 1.** Check 1's readout is an intrinsic invariant "not read out by a supervised decoder", but four places call
the passing state "decodable".
**Problem 2.** Falsification l.194 defines check 2's failure as "$L_W$ … invariant under swept interventions". By Box 1,
the clamp sweep defines κ, and $L_W$ comes from structural suppression.
**Fix.**
- Replace "decodable" with "intrinsically identified" in the four places.
- l.194: "…whose world-transition is invariant under swept clamps of its self-attractor (κ ≈ 0) — including…".

### F16 — MINOR — l.80 and Box 1 l.124: cross-references to Section 6
**Problem.** l.80 says "as Section 6 shows", but §6 now argues the point by citing the companion (§8), so "argues" is
accurate. Box 1 says $L_W$ is "specified in Section 6"; $L_W$ is defined in check 2 (§4), and §6 fixes the workload.
**Fix.** l.80: "as Section 6 argues". Box 1: "The behavioural correlate of check 2 (Section 4), on the workload fixed in
Section 6 —…".

### F17 — MINOR — l.170 and l.26: tier-III strength
**Problem.** Confirms m11 and extends it. l.170 says the named structure "is the substantive tier-III target §9.2 calls
for" and that the detector "supplies the tier-III structure". l.26 and the revised §1 and §9 say "offers a candidate"
and "proposes an answer".
**Fix.** l.170: "is a candidate for the tier-III target §9.2 calls for … the detector proposes the tier-III structure…".

### F18 — MINOR — l.26: the roadmap omits Section 8
> "Sections 2–6 develop the detector; Section 7 sets it against ICCR."

**Problem.** Section 8 is not mentioned, and §7 covers IIT, GWT, PP and indicator programmes as well as ICCR.
**Fix.** "…Section 7 relates it to ICCR and to rival frameworks; Section 8 states scope and falsifiers."

### F19 — MINOR — l.20: the ICCR abbreviation
**Problem.** Confirms m1. "which we abbreviate ICCR" is wrong. ICCR is Kanai & Ma's own abbreviation for *Intrinsic
Causal-Computational Realization* (their abstract), and the manuscript never expands it.
**Fix.** "…and its realization relation, Intrinsic Causal-Computational Realization (ICCR), specify…".

### F20 — MINOR — l.52: what does not weaken their claims
**Problem.** Confirms m3. Kanai & Ma say that leaving the *grain* open "does not weaken them" (§9.3). They say nothing
of the kind about §9.2 or §9.4.
**Fix.** "First, Kanai and Ma hold that the grain opening does not weaken their *conditional* claims…".

### F21 — MINOR — l.210: the AI-use disclosure
**Problem.** Confirms m12. In this paper "checks" means the detector's three checks, none of which was run, so
"analysis code used for the in-silico checks reported in the companion" repeats the B1 error. MG chooses the wording.
**Fix.** If the sentence is kept: "…in-silico tests reported in the companion preprint".

The numbering of the checks (1, 2, 3) is consistent throughout: §4, Box 1, §6(c), §8, the falsification paragraph and
both figure alt texts. The abstract, §1 and §9 agree with one another and with §6 after the revision. Apart from the
§6 heading (F4), no dangling reference to removed content was found. A grep for "closed-loop perturbation",
"validated", "banked", "survival task" and "d ≈" finds no residue.

---

## 3. The two open minor items

### m2 — l.46 — VALID, apply
> "…but which structure that is requires a substantive theory ICF does not provide."

Kanai & Ma §9.2 is conditional: "If ICF is correct, the consciousness-relevant structure should be found in a
tier-III … feature". They assign theories the job of *guiding the search*: "Scientific theories … can guide the search
for the tier-III target"; tier-II constructs are "disciplined hypotheses about which interventions and readouts may
help reveal it". They do not say that ICF lacks a theory that would fix the target. The revised §1 (l.22) states this
correctly, so l.46 now contradicts it. Box 1 l.126 ("§9.2 invites a substantive theory to supply") is the same point,
said more softly.
**Fix.** l.46: "…but which feature that is has to be found empirically, with theories guiding the search." Box 1
l.126: "…an instance of the mechanism-enriched methodology through which §9.2 proposes to operationalize that search."

### m10 — l.190 — VALID, and "checks 1 and 2" is still slightly wrong
> "…the homeostatic self-regulating controller, which passes the *closed-loop* forms of all three checks…"

Only check 2 has an off-line sub-clause, and so only check 2 has a closed-loop form. Check 1 has no closed-loop form.
Check 3 excludes "a fixed-point relaxation" (l.82), and a homeostatic regulator is the textbook fixed-point
relaxation, so it should *fail* check 3. "All three" is therefore wrong in two ways.
**Fix.** "…which passes check 1 and the closed-loop form of check 2 yet is a plausible non-experiencer; it fails
check 2's off-line sub-clause (Section 4)…".

---

## 4. Prose register (revised sentences only)

`~/simbook/scripts/structural_slop.py --profile paper`, HEAD~2 → HEAD:

| measure (per 1k words) | before | after | ceiling |
|---|---|---|---|
| denial openers | 1.30 | 1.19 | 1.20 |
| ordinal openers | 1.00 | 0.99 | 1.00 |
| §/Section callbacks | 4.30 | **5.24** | 2.50 |
| scope fences | 0.30 | 0.30 | 0.80 |
| contrast verdicts | 0.10 | 0.10 | 0.20 |

### R1 — MINOR — the callback count rose
**Problem.** Callbacks rose from 4.30 to 5.24 per 1,000 words. Most of the increase is new companion section pins in
§6(b), §7 and §8. The draft already failed this ceiling before the revision, and the revision moved it further over.
**Fix.** Keep a pin only where the reader needs the subsection. Drop the repeated "(Gruber, 2026b, §x)" in favour of
one source sentence per paragraph, or let all four §6(b) results share one citation at the end.

### R2 — MINOR — §6(b) stacks fences
**Problem.** l.152 holds five fences in one paragraph:
- "none of them runs the checks themselves";
- "no result in this subsection is drawn from a running instance of it";
- "is not evidence for FMT over its rivals";
- "nothing shows the reactive policies could not…";
- "not evidence that operating at the edge of chaos pays".

"The checks have not been run" is stated again at l.156, l.162 and l.200. This is the stacked red-team pattern that
*Structural slop* describes.
**Fix.** Cut l.152's second sentence after "(Gruber, 2026b)". The not-yet-instantiated status is already stated in
(a). Keep the "not run" statement once in §6, at l.162, and once in §9.

### R3 — MINOR — l.154: canned aphorism
> "a loop between two things needs two things"

**Problem.** The sentence was reworded in the revision ("requires" → "needs"), so it counts as touched. It is a
cadence-tic aphorism.
**Fix.** Disappears if F2 is applied. Otherwise: "…which the framework expects, since the reservoir had no distinct
self- and world-models for a loop to close between."

No new throat-clearing, banned superlatives, "load-bearing", pet words or revision-history narration were found in
the revised sentences. The self-narration at l.162 ("Reported this way") and l.196 ("we are careful to separate…",
"we do not claim they do") is pre-existing and was already listed for MG.

---

## Counts

- BLOCKER: 0
- MAJOR: 4 (F1–F4)
- MINOR: 22 (F5–F21; m2 and m10; R1–R3)

## Verdict

Apart from MG's open decisions (title, AI-disclosure wording, the m-list), the manuscript is not yet entirely free of
unquotable in-silico claims, but it is close. The S362 revision did what it set out to do. Every number it cites
matches the companion and the crucible results: 0.98 vs 0.78, d = 2.44, 40 seeds; the reactive bracket at
0.00–0.33; 30/30 reservoirs in the ordered regime. No result is drawn from a FlowBody run. The withdrawn A#1 and §4.5
results are not cited. No fix went too far into under-claiming.

Four statements remain wrong or not quotable:
- l.154 calls the companion's positives regime-free, but §4.4 is a regime result (F1).
- l.154 cites the CRU-36 re-entry null, which the artefact audit lists as AT RISK (F2).
- l.174 cites the graph-only §5.1 result for a dynamical dependence claim (F3).
- The §6 heading calls an unimplemented detector "runnable" (F4).

All four need one-clause fixes. Once they are applied, along with F5 (the uncited survival result) and the m10
correction, the in-silico content is quotable as stated.
