<!-- Tracked-by: AIW-298 (Z2), AIW-130. Changelog for the JAIC detector draft, session Z2, 2026-10-19 (WSL, subagent). -->
# JAIC draft, Z2 changelog: v19/v20 consistency pass

**Files changed:** `drafts/aiw130-jaic-draft.md` (D1–D25), `drafts/aiw130-jaic-cover-letter.md` (C1–C3).
**Rules checked against:** FMT master v20 (`paper/full/four-model-theory-full.md`, doi:10.5281/zenodo.23477765):
§3.5 (one criterion, graded levels above it), §3.4.6 (accessible vs accessed), §3.7.3 (four-part sufficient
conjunction); `docs/aiw288-master-fix-proposals.md` (groups A–F); `.claude/knowledge/neuroscience-communication.md`
(no "gate/gating"); `.claude/knowledge/prediction-framing.md` (S329: criticality is a signature, not a requirement);
MG 2026-08-02 on `aiw130-PROPOSE.md` decision 3 (drop the "completes Kanai's ICF" framing from the body).
Baseline copies for diffing: `tmp/z2-jaic/baseline-draft.md`, `tmp/z2-jaic/baseline-cover.md`.

## Draft: changes

| ID | Where | Old | New | Reason |
|---|---|---|---|---|
| D1 | Abstract | "a system's self-model gates its own world-model's update" | "a system's self-model enters the update of its own world-model" | Gate wording (aiw288 E6: "closure-gated updating" → "closed-loop"); "enters the update rule" is the draft's own §4 term |
| D2 | Abstract | "yielding a graded verdict plus a unit-individuation edge case" | "yielding a verdict with graded confidence plus …" | One criterion (§3.5): the verdict is yes/no, the confidence is graded. Abstract now 147/150 words |
| D3 | §1 ¶4 | "explicit self-model gates the update of its own world-model"; "yielding a graded verdict" | "enters the update of"; "a verdict with graded confidence" | As D1, D2 |
| D4 | §1 ¶5 | "The relationship to ICCR is one of *completion*, not competition: check 2 is … so the detector supplies the tier-III structure their §9.2 invites rather than proposing a rival measure." | "Check 2 is a concrete instance of … methodology, and the detector offers a candidate for the tier-III structure their §9.2 invites; it is not a rival measure." | MG 2026-08-02: no "complete" framing toward others' work; also a not-X-but-Y pair |
| D5 | §3 ¶1 | "a system is conscious to the degree that it builds a model of itself …" | "a system is conscious when it builds a model of itself …" + "A system has phenomenology or it has none; above that single criterion, how conscious it is varies with the richness and recursive depth of its self-model (Gruber, 2026a, Section 3.5)." | "to the degree that" makes consciousness itself graded (aiw288 B); §3.5 wording |
| D6 | §3 levels ¶ | "a self-model that gates its own world-modelling" | "a self-model that enters its own world-modelling" | Gate wording |
| D7 | §3 last ¶ | (dual threshold only) | added: "The two thresholds are each necessary and are not jointly sufficient. FMT's sufficient condition is a conjunction of four parts: the four models under closure, free compute, embodiment, and at least one pain-pleasure axis, which may be engineered (Gruber, 2026a, Section 3.7.3). The checks test the first two by intervention; Section 4 states how a verdict handles the other two." | Two-part sufficiency (aiw288 A): the draft read as if closure + open-ended computation suffice |
| D8 | §4 ¶1 | "returns a graded verdict" | "returns a verdict with graded confidence" | As D2 |
| D9 | Check 2 heading | "Check 2 — closure gates the world-model's own update." | "Check 2 — the self-model enters the world-model's own update." | Gate wording |
| D10 | §4 Output | "The detector returns a graded conscious-or-not verdict with an explicit confidence, set by … and capped by the weakest of checks 2 and 3." | "… returns a yes-or-no verdict on whether the tested conditions hold, with an explicit confidence set by … and capped by the weaker of checks 2 and 3. A positive verdict supports attributing consciousness only together with the two parts of FMT's sufficient conjunction that the checks do not establish by intervention: embodiment, which check 1 presupposes, and at least one pain-pleasure axis, which the tester establishes from the system's architecture (Gruber, 2026a, Section 3.7.3)." | One criterion + four-part conjunction; "weakest of two" → "weaker" |
| D11 | Box 1 | "through the world-model it gates" | "through the world-model whose update it enters" | Gate wording |
| D12 | Box 1 | bare "κ" ×4 in prose | `$\kappa$` | Build fix: pdflatex stopped on U+03BA outside math |
| D13 | §5 ¶4 | "one self-attractor gating one world-model" | "one self-attractor entering the update of one world-model" | Gate wording |
| D14 | §6(a) | "whether that self-basin gates the world-model's own update" | "… enters …" | Gate wording |
| D15 | §6(c) | "If a limb's self-model gates how that limb's world-model updates" | "If a limb's self-model enters the update of that limb's world-model" | Gate wording |
| D16 | §6(c) | "the verdict is positive with a confidence set by the graded values, *and* …" | "…, read together with the architecture's pain-pleasure axis as Section 4 requires, *and* …" | Four-part conjunction in the worked example |
| D17 | §7 ICCR | heading "— the primary integration, instantiation not rivalry."; "The detector *completes* ICCR at its three explicit openings."; closing "This is the substantive theory ICF's §9.2 and §9.4 call for, not a claim that ICF is incomplete or inferior." | heading "**ICCR (Kanai & Ma, 2026b).**"; "The detector answers ICCR at its three explicit openings."; closing sentence deleted | MG 2026-08-02 directive; the deleted sentence pre-answers a critic (prose register) |
| D18 | §8 ¶1 | "which is why the verdict is graded and grain-annotated rather than absolute." | "which is why every verdict carries a confidence and names the grain it was reached at." | One criterion; not-X-but-Y |
| D19 | §8 dual threshold | "a decodable self-model that does not gate its own world-modelling"; "The verdict is a conjunction across a substrate property and an architectural relation, and …" | "… does not enter …"; "…, read together with embodiment and a pain-pleasure axis (Section 4), and …" | Gate wording; four-part conjunction |
| D20 | §8 necessity | heading "Necessity, not claimed sufficiency — and the self-monitor boundary."; "We advance the three checks as *necessary* conditions on a conscious realizer, not a demonstrated jointly sufficient set."; "We name the class explicitly so that no reader mistakes the conjunction of closed-loop readouts for the target." | heading "Necessity, and the self-monitor boundary."; "The three checks test *necessary* conditions on a conscious realizer. FMT's sufficient condition is the four-part conjunction of Section 3 (…; Gruber, 2026a, Section 3.7.3), and the checks establish its first two parts by intervention."; "Passing the closed-loop readouts alone does not meet the target." | Four-part conjunction; the last sentence was self-narration (prose register) |
| D21 | §9 | "the self-model gating its own world-model's update"; "yielding a graded verdict" | "the self-model entering the update of its own world-model"; "a verdict with graded confidence" | As D1, D2 |
| D22 | References | Gruber 2026a: "*Zenodo.* Concept DOI 10.5281/zenodo.18669891." | "(Version 20). *Zenodo.* doi:10.5281/zenodo.23477765. Concept DOI 10.5281/zenodo.18669891." | v20 citation. Verified by DataCite: title matches, version "v20", issued 2026-10-19, author Gruber; Zenodo API: record 23477765 has concept DOI 18669891 |
| D23 | References | Gruber 2026b: "*Zenodo.* DOI 10.5281/zenodo.21610993." | "(Version 4). *Zenodo.* doi:10.5281/zenodo.23216263. Concept DOI 10.5281/zenodo.21610993." | 21610993 is the concept DOI, not a version DOI. Verified by Zenodo API: latest version v4 = record 23216263; DataCite title matches |
| D24 | Fig. 1 caption + alt text | "graded decision flow feeding a graded verdict"; node 2 "Closure gates world-model update?"; box "Graded verdict plus confidence" | "decision flow with graded readouts, feeding a verdict with graded confidence"; "Self-model enters the world-model's update?"; "Verdict plus graded confidence" | Gate wording; one criterion |
| D25 | Fig. 2 alt text | "closure: self-model gates the world-model's own update." | "closure: the self-model enters the world-model's own update." | Gate wording |

## Cover letter: changes

| ID | Old | New | Reason |
|---|---|---|---|
| C1 | "self-referential closure that gates the world-model's own update"; "yielding a graded verdict"; "a buildable minimal critical spiking substrate" | "closure in which the self-model enters the world-model's own update"; "a verdict with graded confidence"; "a buildable minimal open-ended spiking substrate" | Gate wording; one criterion; S329 (the draft already says "open-ended", the letter still said "critical") |
| C2 | "positioned as **completing Intrinsic Computational Functionalism** (Kanai & Ma, 2026) … I have taken care that the contribution **stands independently of that framing** — … does not depend on the reader accepting the completion narrative." | "The paper answers the three questions that Intrinsic Computational Functionalism (Kanai & Ma, 2026b) leaves open: … The three checks and their grounding are motivated on their own dynamical-systems terms." | MG 2026-08-02 directive; "I have taken care" advertised the text's own care (prose register); year suffix matched to the reference list |
| C3 | "(concept DOI 10.5281/zenodo.18669891)"; "the companion a biological-brain criticality-necessity claim on neural evidence"; "coherent on what is necessary (one enabling condition …)" | "(version 20, doi:10.5281/zenodo.23477765; concept DOI 10.5281/zenodo.18669891)"; "the companion an account of near-critical cortical dynamics on neural evidence"; "agree on what is necessary (free modelling, stated substrate-neutrally here and through its neural-tissue signature there)" | v20 DOI; "criticality-necessity" contradicts S329 |

## Figures (review build only)

The tracked figures `figures/aiw130/jaic-fig1.*` and `jaic-fig2.*` and their generator `scripts/gen-aiw130-figures.py` are
outside this session's write scope and still carry the old labels. The review PDF uses copies rendered by
`tmp/z2-jaic/render_jaic_figs_z2.py`, which applies three string changes to the generator in memory:

| ID | Figure | Old label | New label |
|---|---|---|---|
| F1 | Fig. 1 | "Check 2 — closure gates the world-model's own update (the crux)" | "Check 2 — the self-model enters the world-model's update (the crux)" |
| F2 | Fig. 1 | "Graded conscious-or-not verdict / + explicit confidence" | "Verdict on the tested conditions / + graded confidence" |
| F3 | Fig. 2 | "closure: the self-model gates the world-model's own update" | "closure: the self-model enters the world-model's own update" |

**Before deposit:** apply F1–F3 to `scripts/gen-aiw130-figures.py` and re-run it (it also re-renders the NoC figures).

## Checked and left unchanged

| Item | Count | Why it stays |
|---|---|---|
| "self-model-gated planner" (§6b, §8), "demand- and scale-gated" (§6b) | 3 | In-silico program vocabulary, kept in master v20 §8.11 (aiw288 "fine as is", md 1029) |
| "binary" | 3 | All about the binary loop-cut test, not about whether a system is conscious |
| Criticality as requirement | 0 | The draft already follows S329: criticality is a contingent signature; check 3 passes a subcritical system |
| "accessible / access" (v19 sense) | 0 | No hits |
| Redirectable / forkable ESM credit | 0 | No hits ("the architecture forks" in §6c is generic) |
| Alen Frey in byline / CRediT | 0 | Removed S337; byline and CRediT are single-author |
| FMT section numbers §8.7–§8.9 | 0 | The draft cites no master §8 section; the two new pointers (§3.5, §3.7.3) use v20 numbering |

## Gates run (2026-10-19)

- Build: `scripts/build-md-pdf.sh` → `tmp/z2-jaic/aiw130-jaic-z2-review.pdf`, 23 pages, **0 overfull boxes (worst 0.00pt)**, no `??`, all 3 figures embedded.
- Citations: every in-text author-year pair matches a reference entry and every entry is cited (script check).
- Prose register: `~/simbook/scripts/check_prose_register.py` → draft 0 hits, 0 dense windows; cover letter 0/0.
  `scripts/register_gate.py` problem classes (incl. self-narration) → 0 on both files. Antithesis density in the
  changed paragraphs 3.8 per 1k words against a 7.1 baseline.
- Body length: 9,721 words (§1–§9); abstract 147/150; keywords 6/6.
