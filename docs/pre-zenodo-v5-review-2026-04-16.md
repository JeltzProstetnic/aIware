# Pre-Zenodo v5 Multi-Angle Review — 2026-04-16

**Paper:** `paper/full/four-model-theory-full.md` (21,867 words, mtime Apr 14)
**Current Zenodo:** v4 (2026-03-17, DOI 10.5281/zenodo.19064950)
**Context:** 5 desk-rejections (TAP, PLREV, NEUBIOREV, NCONSC×2, CONCOG)
**Reviewers:** 5 parallel Opus agents — editor, neuroscience, philosophy-of-mind, structural, clarity

---

## Convergent Verdict

**Do NOT upload v5 as-is.** Five independent reviewers, four explicit frames and one structural/logical, identify the same core weaknesses. A 6th desk-reject is the most probable outcome if this text were submitted to a top-tier venue tomorrow.

Editor recommendation: "Yes after ~10 quick fixes (1-2 days)." Neuroscience and philosophy reviewers recommend deeper revision.

---

## The Five Reviews — Headline Verdicts

| Angle | Verdict | Severity |
|-------|---------|----------|
| **Editor (gatekeeper)** | Top-tier: desk-reject. Mid-tier: borderline. Specialist (JCS/Mind&Matter): survives. | HIGH |
| **Neuroscience** | LOW credibility for NoC/NBSR. "Armchair architecture with decorative citations." | HIGH |
| **Philosophy of mind** | MEDIUM rigor. Load-bearing moves stipulated, not argued. JCS-submittable after revision. | MEDIUM |
| **Structural/logical** | Sharpening §3.4 + resolving three senses of "virtual" buys more than any other edit. | MEDIUM |
| **Clarity/accessibility** | Abstract buries thesis 70 words deep. No figures for a 2×2 theory. | MEDIUM |

---

## Convergent Top Issues (flagged by ≥2 reviewers)

### 1. §3.4 "self-referential closure" is stipulated, not derived — the paper's single most important argument

Every reviewer except clarity called this out explicitly:
- **Philosophy:** "observation-from-inside is what we call experience" is where the argument needs to be; instead it is where the argument ends.
- **Structural:** "This is the load-bearing move of the entire paper and is stated as stipulation. The author concedes: 'This is not a proof.' But then §11 claims the Hard Problem is *dissolved*."
- **Clarity:** "Load-bearing term, never formally defined. Needs a one-paragraph definition with a worked contrast example."
- **Editor:** flagged via the "not operationalized / not empirically grounded" desk-reject category.

**Fix:** Rewrite §3.4 as the paper's centerpiece (~1,500 words). Concrete contrast example: weather simulation (non-closed) vs. a hypothetical closed system. Admit openly this is a conceptual argument, not a proof, but give the reader enough to see *why* it is supposed to work.

### 2. "Virtual" has three incompatible meanings across the paper

- §3.3: transient patterns of activity in the substrate (physical, dynamical)
- §3.4: properties incoherent at substrate level (level-distinct)
- §3.7: fifth level in the hierarchy (emergent)

The paper uses sense-2 to dissolve the Hard Problem and sense-1/3 to stay physicalist. This is a contradiction that editors/reviewers will spot immediately.

**Fix:** Pick one primary sense. Add explicit disclaimer paragraph defining the term. Alternative term suggested by clarity: "simulation-level."

### 3. "Four models" equivocation — taxonomy vs. countable entities

- §3.2 disclaims: "not a claim about spatial organization," "floor not ceiling"
- §6 treats IWM/ISM/EWM/ESM as countable entities (DID = multiple ESMs, split-brain = two degraded copies)
- §8 Prediction 3: "DMN = ESM network" — exactly the naive modularism Andrillon rejects

**Fix:** Drop "Four-Model" from title. Title suggestion: *"Simulation Consciousness: A Criticality-Based Framework for the Implicit/Explicit and World/Self Axes."* Add explicit ¶: "Hereafter, 'four models' refers to four *kinds of modeling* along two axes. Claims about 'an ESM' should be read as claims about the self-modeling *function*."

### 4. Criticality not operationalized with a concrete neural signature

- 15+ invocations of criticality; never commits to branching parameter κ, avalanche exponent τ, DFA α, or LRTC slope.
- PCI conflated with criticality (it is an integration/complexity measure, not a criticality measure).
- §3.7.2 claims the cortical automaton is *literally* visible as phosphenes — will lose every V1 neuroscientist.

**Fix:** Commit to one signature. Example: "If DFA α < X during propofol and > Y during wake, and this dissociates from PCI, the theory is supported. If not, the theory is wrong." Distinguish PCI from criticality explicitly.

### 5. 8-requirement rubric is set by FMT, then used to score rivals

Close to circular: FMT defines the game it wins. Rival theories score lower on requirements FMT added.

**Fix:** Either cite independent source for the requirements list, or explicitly argue that someone who denies requirement N can still accept FMT. Acknowledge that the selection of requirements is itself theory-laden.

### 6. §9 OQ2 paragraph lectures editors — "single most damaging sentence"

> "To expect both the theoretical model and its full mathematical apparatus from a single author — prior to any peer evaluation of the model's conceptual soundness — inverts the usual scientific workflow…"

Reads as wounded, pre-emptive pushback. Editors read pre-emptive defenses as admission of guilt.

**Fix:** Delete entirely. Replace with one sentence: "Formalization is in progress (Gruber, 2026b)."

### 7. Abstract buries the thesis

Current abstract opens with 8-requirement meta-complaint for 70 words before stating the thesis. Editors skim abstracts in 30 seconds.

**Fix:** Rewrite to lead with the thesis and empirical convergence:
1. One-sentence thesis ("Consciousness is a self-referential simulation running on a critical substrate; qualia are properties of that simulation, not of the neurons that run it.")
2. One-sentence mechanism
3. One-sentence hook ("Five predictions from 2015 have since been confirmed.")
4. One-sentence scope
5. Four novel predictions

### 8. No figures at all — only tables

For a paper whose central move is a 2×2 architectural model, this is a severe communication failure.

**Fix:** Add 2×2 architecture diagram (§3.1) and five-system hierarchy diagram (§3.7.1). The bubble diagram already exists at `figures/figure2-real-virtual-split-simple.svg`. An editor who sees a clean diagram in the first 5 pages commits 5× more attention.

### 9. REM phenomenology still wrong (flagged by Andrillon's NoC rejection, not fixed)

§6.3 reads as if "REM = online dreaming, NREM = offline" — empirically dead. No engagement with Siclari's hot-zone posterior dreaming, NREM dreams, Dresler's lucid-dreaming fMRI, or the fact that PCI during REM ≈ wake.

**Fix:** Rewrite §6.3 and §8.5 with Siclari (2017/2021), Nir & Tononi (2010), Dresler, Baird, Voss. Acknowledge NREM dreaming exists.

### 10. Missing 2024-2026 citations (neuroscience credibility)

Critical misses: Shew/Priesemann/Plenz 2024-2025 criticality reviews; Siclari 2017/2021; Toker 2022; Aru-Suzuki-Larkum 2020; Seth & Bayne 2022 (standard reference); Kleiner 2024; Tsuchiya & Saigo 2024; Lau/Michel/LeDoux 2024; Dehaene 2021 workspace updates; Melloni COGITATE 2025 full paper; Frankish 2016/2023 illusionism responses; Metzinger 2024.

### 11. Zombies, Mary, Frankish illusionism dismissed in single sentences

The paper claims to "dissolve" the Hard Problem but does not confront Chalmers' conceivability argument, Jackson's knowledge argument, or Levine's explanatory gap with more than a sentence each. Frankish's specific illusionism formulation is dismissed without engagement; FMT might actually be weak-illusionism in Frankish's sense.

**Fix:** Expand §4.2 zombie and Mary handling from one sentence to one paragraph each. Address conceivability head-on. Name weak-illusionism and argue the specific distance from it.

### 12. Causal role contradiction (§4.2 vs §11)

- §4.2: "Qualia … lack independent causal power over the substrate."
- §11: "the architecture is causally efficacious; qualia lack independent causal power but are constitutive of the simulation the substrate deploys for evaluation."

These are consistent only if "architecture is causally efficacious" = substrate-level — which means the causal-role requirement is satisfied by *the substrate*, not by consciousness. The §2 Requirement 6 score of ● is overgenerous.

---

## Quick-Fix List (Editor's 10, ≤1-2 days)

1. Delete OQ2 "inverts the usual scientific workflow" paragraph (§9).
2. Delete "addresses all eight requirements" triumphalism from abstract and §11.
3. Replace "dissolves the Hard Problem" with "addresses" in abstract and §11 (keep "dissolves" in §3.4 where argued).
4. Prune AI acknowledgment to Elsevier/OUP boilerplate only.
5. Prune self-citations: 27 → at most 5. Collapse Gruber 2026a/b/c to one citation.
6. Add one operationalization sentence per prediction (effect size, n, outcome measure).
7. Drop [^quantum] footnote.
8. Drop "substrate independence" from abstract (keep argument in §4.4).
9. Add Metzinger 2003 and Kriegel 2009 at §3.1 with concrete differentiating claims.
10. Shorten abstract to ≤250 words.

---

## Structural Fixes (deeper revision, not same-day)

- **§3.4 rewrite** as centerpiece (~1,500 words, self-referential closure argued properly)
- **§3.7 rewrite** committing to concrete criticality neural signature
- **§6 cut** from 8 phenomena to 3 (psychedelics + anosognosia + DID)
- **§6.3 rewrite** REM/dreaming with current literature
- **Cut word count** ~22k → ~12-15k
- **Add figures**: 2×2 architecture, 5-system hierarchy, dual-evaluation
- **Cut §4.3 Weak Emergence** (restates §3.4)
- **Merge §3.7.1 + §3.7.2**
- **Move §3.8 (Meta-Problem) to after §3.6**
- **Split §4.2** (too many distinct arguments under one heading)
- **Prediction 3 fix:** Replace "DMN = ESM" with "alter-switch-related reconfiguration shows higher cosine-distance in self-referential networks (DMN, SN, precuneus) than sensorimotor networks, d ≥ 0.5."
- **Kill or qualify §3.7.2** cortical-automaton-as-phosphenes paragraph.
- **Engage Milinković & Aru (2025)** properly — two paragraphs, not a one-line deflection.

---

## Three Options for Zenodo Upload

**Option A — Hold.** Do not upload v5. Current text would draw a 6th rejection. The quick fixes alone (1-2 days) remove the sentences that make a desk editor's decision take 3 minutes instead of 30 but do not solve structural issues.

**Option B — Quick-fix pass, then upload v5 (1-2 days).** Apply the 10 quick fixes. Upload as v5 with a clear changelog. This is the editor's explicit recommendation. Zenodo is not refereed — preprint accumulates citation record. Structural fixes deferred to v6.

**Option C — Deep revision (1-2 weeks), upload v5 only when §3.4 is tight.** More honest to the reader but delays the record update. Reduces risk of looking committed to flawed claims if future critics cite v5.

**Editor note (from first review):** "Do not send to another journal until a senior co-author is on the paper. The sixth rejection will be worse for the record than no submission at all." This supports Option B or C over any near-term journal submission.

---

## Inputs

- `/home/jeltz/aIware/paper/full/four-model-theory-full.md` (unchanged by this review)
- 5 agent outputs archived in conversation. Agent IDs for follow-up:
  - Structural: a691d452307816045
  - Clarity: a37576bf5b280c6ae
  - Editor: a2c62534ed36ed617
  - Neuroscience: ad4fd78fdb87a598e
  - Philosophy: ae97e6f51c54c37ba
