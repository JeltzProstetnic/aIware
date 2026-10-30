# AIW-130 JAIC draft — independent re-check of the S363 fix pass (D-S363-5)

Manuscript: `drafts/aiw130-jaic-draft.md` at 9d5d6e59 (unchanged at HEAD af361d26), diffed against 9d5d6e59~1.
Checked against: companion v6 `drafts/companion-computational-paper-draft.md` (§3.2, §4.1–4.6, §5.1, §6, §7, §8);
FMT master `paper/full/four-model-theory-full.md` (l.17, l.54, l.176); Kanai & Ma full text
`literature/fulltext/Kanai2026.pdf` (fitz); `figures/aiw130/jaic-fig1.svg`/`.png`; Crossref for Baltieri & Kanai.
Line numbers are the current draft's.

**Verdict: the pass resolves every finding it claims to, and none of its edits strengthens a claim against its source.
One new defect is MAJOR: the new figure callouts cite Figure 3 first, then Figure 2, then Figure 1. Nine MINOR items
remain, each a one-clause fix.**

Measured: abstract 148 words (≤150). `structural_slop.py --profile paper` on the whole file: PASS, matching the
changelog (9,996 words; denial 1.00, ordinal 0.80, callbacks 1.70, fences 0.40, contrast 0.10, undecided 0.00,
pet words 0.00). The AI-use statement (l.210) claims no in-silico checks were run. It says nothing about in-silico
work at all. Baltieri & Kanai: Crossref confirms "Steam-engine naturalism", *BBS* 49, e318.

---

## 1. Per-finding verification

| finding | lines | resolved? | note |
|---|---|---|---|
| F6 | 152 | yes | Companion §4.4: medium task only at N = 300; the hard task lifts with N. |
| F7 | 154 | yes | The "whose main effect" ambiguity is gone. |
| F8/m5 | 82, 84 | partly | See N3 below: "reported beside" does not say the value must differ from the surrogate's. |
| F9 | 156 | yes | Companion §3.2/§4.6: ρ = 1 is ordered (λ ≈ −0.12), the edge is measured. |
| F10/m4 | 64, 156 | partly | See N4 below: two of the rate reservoirs tested returned nulls. |
| F11 | 162 | yes | The cut is clean (judgement b, §3). |
| F12 | 78, 150, 164 | yes | |
| F13 | 174 vs Box 1 l.120 | yes | Box 1 (i) already contains the off-line clause, so "closed-loop form of (i)∧(ii)" and "off-line clause of (i)" both type-check against Box 1. |
| F3 residue | 174 | yes, with a residue | See N5 below (judgement c). |
| F14 | 196 | yes | |
| F15 | 116, 164, 188, 194, alt text l.290 | yes | The alt text quote matches the figure verbatim. See N6 below (falsifier vs pass condition) and §3(d). |
| F16 | 80, 124 | yes | |
| F17/m11 | 170 | yes | See N8 below for one sentence in the same paragraph that is still strong. |
| F18 | 26 | yes | |
| F19/m1 | 20 | yes | Kanai & Ma abstract: "Intrinsic Causal-Computational Realization (ICCR)". |
| F20/m3 | 52 | yes | Kanai & Ma: "leaving it open does not weaken them". |
| F21/m12 | 210 | yes | MG's wording, no in-silico claim. |
| m2 | 46, Box 1 l.126 | yes | Kanai & Ma §9.2: "The mechanism-enriched canonical framework offers a way to operationalize this search"; "theory … must help to adjudicate empirically". |
| m6 | 152 | yes | Companion §4.2 wording and numbers. |
| m9 | 186 | yes, with a residue | See N7 below (judgement a). |
| m13 | 222 | yes | Crossref-verified. |
| m14 | 52, 58 | **introduced N1** | |
| m15 | 164 | yes | |
| For-MG 4 | 184, 192, 196 | yes, with a residue | See N9 below. |
| R1 | whole file | yes | Callbacks 1.70/1k. See N2 below for two pins a reader needs. |
| R2 | 152, 156, 162 | yes | "Not run" now appears once in §6 (l.162) and once in §9 (l.200). |
| R3 | 154 | yes | The ambiguity in the touched sentence remains (N2b). |

---

## 2. New or residual findings

### N1 — MAJOR — l.52, l.58, l.72: figures are cited out of order
The m14 callouts put the first in-text citation of Figure 3 at l.52 and of Figure 2 at l.58. Figure 1 is first cited
at l.72. World Scientific, like nearly all journals, numbers figures in order of first citation, and the LaTeX
template floats them by first reference. So the build would place Fig. 3 first.
**Fix.** Renumber the figures to match first citation. The ICCR-openings table becomes Fig. 1, the 2×2 grid stays
Fig. 2, and the decision flow becomes Fig. 3. Update captions, file references and "Figure 1 renders the procedure"
(l.72) to match. The alternative is to drop the l.52 callout and cite Figure 3 from §7 l.170, but the Figure 2
callout (l.58) would still precede the Figure 1 callout (l.72), so renumbering is needed either way.

### N2 — MINOR — two pins removed under R1 that a reader needs
(a) **Quote locators in §2 (l.46–50) and §5 (l.134).** The §9.2/§9.4/§9.3 pins on the italic headers served as the
only locators for the direct quotations under them ("disciplined hypotheses …", "IIT, for example, is more developed
in this respect", "has no such maximization principle", "could play that role"). APA requires a locator for a direct
quotation. §1 l.22 maps the openings to sections, so a reader can reconstruct the locators, but should not have to.
**Fix.** Restore one pin per italic header (`*Which structure (§9.2).*` etc.). That is +3 callbacks, which keeps the
rate near 2.0/1k, under the 2.5 ceiling.
(b) **l.154 re-entry null.** The §6 pin was cut, and l.152 now ends "Data and protocols for all four results are in
the companion (Gruber, 2026b, §4)". A reader looking for the null in §4 will not find it, because it is companion §6.
**Fix.** "(Gruber, 2026b, §6)". In the same sentence, "the framework expects it either way" can be read as "the
framework expects either outcome of the re-analysis", which sounds unfalsifiable. **Fix:** "the framework predicts
a null here, since the reservoir had no distinct self- and world-models for a loop to close between."

### N3 — MINOR — l.82: the surrogate condition is weaker in check 3 than everywhere else
l.82 has "a branching ratio near unity reported beside a rate-matched surrogate". l.156 counts the ratio "only when it
departs from the value a rate-matched surrogate produces", and l.164 has "a rate-matched surrogate that fails to
reproduce them". "Reported beside" does not require the value to differ, and companion §3.2 says a σ "establishes a
firing rate unless" it is reported beside its surrogate. The check-3 wording is the one a tester would follow.
**Fix.** l.82: "…a branching ratio near unity that a rate-matched surrogate does not reproduce…".

### N4 — MINOR — l.64 (and l.156): "in the rate reservoirs tested so far the computational optimum sits in the … ordered regime"
Companion §4.4 Methods lists five further scans. In two rate reservoirs capability was best on the ordered side. A
third rate reservoir returned a null, and a fourth returned a null inside the band. So not every rate reservoir tested
showed an optimum at all. The F10 wording (taken from the S362 recheck's own fix) still generalises over the nulls.
**Fix.** l.64: "…in the rate reservoirs tested so far, where a capability optimum appeared, it sat in the
driven-stable, ordered regime (Gruber, 2026b, §4.4)". l.156 can keep the shorter form, because it only locates where
the capability sits.

### N5 — MINOR — l.174: the hedged premise yields an unhedged conclusion (judgement c)
"Mutual dependence … plausibly comes as cheaply, so the closed-loop form of (i)∧(ii) discriminates little". The
scoping is right: §5.1 is a graph result, and companion §7 says only that closure "is what recurrence already gives
you" on that connectome. So the dynamical claim can only be conjecture, and "plausibly" marks it as one. The
conclusion then drops the hedge. "Comes as cheaply" is also a cost metaphor carried over from §5.1, which priced
removal of closure, not the presence of dependence.
**Fix.** "Mutual dependence between two coupled recurrent sub-partitions is plausibly as common, so the closed-loop
form of (i)∧(ii) would discriminate little; the discriminating content sits in the off-line clause of (i) and in the
representational condition (iii)."

### N6 — MINOR — l.194 vs l.80/l.160: the falsifier and the pass condition now use different readouts
F15 moved check 2's falsifier from $L_W$ to κ ("world-transition … invariant under swept clamps … (κ ≈ 0)"). That
matches Box 1, but check 2's graded pass (l.80) is excess $L_W$ against a sham, and l.160 requires both readings to
agree in sign. Box 1 l.124 says the $L_W$–κ link is untested. A system with κ > 0 and no excess $L_W$ fails check 2
by l.80/l.160 but is not named as a failure in the falsification list.
**Fix.** Append to l.194's check-2 sentence: "…or whose closure-specific excess $L_W$ does not exceed the
capacity-matched sham".

### N7 — MINOR — l.186: the m9 citation is supported, but it drops the hedge (judgement a)
The master supports the attribution. l.17: "Open-ended computation allows free modeling, and near-criticality is the
signature that property leaves in neural tissue rather than the requirement itself". l.176: "criticality is how that
requirement usually shows in a biological substrate. The relation runs from free modeling to the signature and not
back". Two small departures:
1. The master's l.17 subject is open-ended computation, not free modelling. The draft itself treats the two as one
   at l.64, so this is tolerable.
2. The draft says "is the signature" where l.64 of the draft and master l.54/l.176 say "usual".

The sentence's own last clause (l.186, "of which criticality is one contingent physical signature") is also weaker
than its opening.
**Fix.** "…where near-criticality is the usual signature free modelling leaves, not the requirement itself
(Gruber, 2026a, §3.7)". In the same paragraph, the closing "The two describe one condition at two grains" (touched:
"treatments" was cut) is a cadence-tic ending, and "grain" is this paper's technical term for scale (§5).
**Fix.** Cut the sentence, or write "at two levels of description".

### N8 — MINOR — l.170: the paragraph F17 fixed still contains "are the … method"
"The three checks are the structure-*extraction* method they name as the next step" (pin edited in this pass).
Kanai & Ma §9.4 say an ICF-based theory "should develop methods for extracting effective intrinsic structures". They
name a class, not this method.
**Fix.** "The three checks are a structure-*extraction* method of the kind they name as the next step."

### N9 — MINOR — l.196: "differentiating predictions" now heads a list whose first item is pre-conceded as non-differentiating
The For-MG-4 rewrite turned the sentence into "The architecture also makes differentiating predictions, some
corroborated post hoc and some untested". The first corroborated item is "shared with causal-representation learning
and not unique to FMT", and companion §8 calls it non-unique. The paragraph's closing sentence uses "differentiating"
correctly, for the PP-contrast forecasts.
**Fix.** "The architecture also makes predictions, some corroborated post hoc and some untested."

### N10 — MINOR — l.154: "obtained at one fixed regime"
F1 replaced "§4.1–4.3 involve no regime manipulation" with "were obtained at one fixed regime". The planner (§4.1)
and survival (§4.2) results are gridworld controllers with no dynamical regime to fix. Only §4.3 sits on a reservoir
(ρ = 0.95).
**Fix.** "The closure-side results above were obtained without varying the substrate's regime, and the reservoir
sweep manipulates no closure, so no experiment varies the two together."

---

## 3. The four judgement calls

**(a) m9 → Gruber 2026a for criticality as free modelling's signature.** Supported by master l.17 and l.176 (see N7
above). Add "usual" and the §3.7 pin.

**(b) F11 cut rather than replaced.** Right call. "Capacity band" is undefined anywhere; it is most likely a garble of
companion §3.2's "capability band", which means something else. Replacing it would have invented a threshold. The
surviving point (toy systems are not evidence at scale) is carried by "or that the mechanism has been shown at scale".
Small redundancy: "shown at scale; the scaled, spiking, closure-driven demonstration remains to be built". This can
stand.

**(c) F3 "plausibly comes as cheaply".** The scoping is acceptable: it keeps the graph/dynamics line §5.1 draws
itself, and "plausibly" marks a conjecture. The inference that follows needs the hedge too (N5 above).

**(d) F15 Fig. 1 alt text.** The changed readout is now verbatim from the figure ("a self-state maintained across the
perturbation and re-established after it"). The rest of the alt text was untouched and still describes a different
figure than the one rendered:
- The alt text describes "decision nodes" with question labels ("Self-attractor present?"). The figure has boxes
  titled "Check 1 — a self-attractor is present", and its check-2 title is "closure gates the world-model's own
  update (the crux)".
- The check-2 readout in the figure is "graded excess loss Lᵂ … capacity-matched sham". The alt text has "graded
  world-model predictive loss L_W … capacity-matched control".
- The alt text omits check 3's intervention, the side note "decisive failure at check 2 or 3 caps the verdict", and
  "resolved by the two dials".
- The verdict box in the figure reads "Graded conscious-or-not verdict + explicit confidence", but the alt text says
  "Verdict plus graded confidence".

The last point is also a consistency issue that sits outside this pass. The figure says "conscious-or-not", while
§4's Output rule (l.88) returns a verdict on "whether the tested conditions hold" that supports attribution only
together with embodiment and a pain-pleasure axis. **Fix (not caused by this pass, but it blocks a clean figure
build):**
- Change the figure's verdict box to "Verdict on the tested conditions + explicit confidence".
- Regenerate the alt text from the SVG's text strings, box by box.

---

## 4. Prose register (changed text only)

No new phrase-list hits, throat-clearing, self-narration, revision-history narration or pet words in the changed
sentences. The whole-file gate passes. Two items in changed text:
- the paragraph-final aphorism at l.186 (N7);
- the "either way" ambiguity at l.154 (N2b).

"This section fixes the ICCR machinery the checks instantiate" (l.30) is plain signposting, which the register
allows. One clunk: l.124 says "on the workload fixed in Section 6 — the world-model predictive loss $L_W$ on an
open-ended workload", so "workload" appears twice. Optional fix: "in Section 6 — the world-model predictive loss
$L_W$ on the open-ended workload fixed there".

---

## Counts

- BLOCKER 0
- MAJOR 1 (N1)
- MINOR 9 (N2–N10)
- The Fig. 1 verdict box and alt text (§3d) are flagged but were not introduced by this pass.

## Verdict

Needs fixes before the template build:
- N1, figure renumbering (MAJOR);
- the Fig. 1 verdict box and alt text (§3d), because the build embeds the figure;
- then the one-clause MINORs N2–N10, which can go in a single pass after N1.
