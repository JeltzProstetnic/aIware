# .md → .tex citation-repair mirror (FMT master paper)

**Scope:** mirrored the repairs in `paper/full/four-model-theory-full.md` (29 ins / 27 del, 28 hunks)
into `paper/full/latex/paper.tex` and `paper/full/latex/references.bib`.
**Files touched:** `paper/full/latex/paper.tex`, `paper/full/latex/references.bib`. Nothing else.
The `.md` is byte-identical to how I found it (still 29 ins / 27 del vs HEAD).

---

## 1. `paper.tex` edits (22 lines changed)

Original line numbers in parentheses.

### 1.1 (L244) Criticality construct definition
- **Before:** `A $\sim$140-dataset meta-analysis \citep{HengenShew2025} confirms criticality tracks consciousness; the ConCrit framework \citep{AlgomShriki2026} synthesizes this into a unifying account.`
- **After:** `... \citep{HengenShew2025} consolidates the evidence that cortex operates near criticality as a setpoint of brain function; the ConCrit framework \citep{AlgomShriki2026} extends this into an explicit criticality--consciousness account.`
- Note: the `.md` uses an en-dash in `criticality–consciousness` here while using a plain hyphen in the other four occurrences of the compound. I mirrored that split exactly (`--` here, hyphen elsewhere).

### 1.2 (L273) Table 1b, "Implicit integrity" row, Measurement Approach cell
- **Before:** `Implicit learning under propofol \citep{Katlowitz2026}: statistical learning, priming, skill consolidation.`
- **After:** `Hippocampal processing under propofol-based general anesthesia \citep{Katlowitz2026}: semantic and lexical discrimination, word prediction, representational plasticity. Statistical learning, priming and skill consolidation are proposed extensions, not results of that study.`
- Table structure untouched (`tabularx{\textwidth}{p{2.5cm}XXX}`, `&` / `\\` preserved). Cell is ~3× longer; verified in the built PDF that Table 1b still fits page 15 with all five rows intact and no Overfull box.

### 1.3 (L411) Kawakita qualia-structure claim
- **Before:** `recovers stable cross-individual correspondences without shared labels \citep{Kawakita2025}`
- **After:** `recovers stable correspondences between independent groups of observers without shared labels \citep{Kawakita2025}`

### 1.4 (L543) Schartner permeability quantitative grounding — see §3.2
- **Before:** `\citet{Schartner2017} report Lempel-Ziv complexity increases of approximately 15-20\% under psychedelic doses relative to placebo, with dose-response curves that could anchor the permeability parameter to measurable values.`
- **After:** `\citet{Schartner2017} report significantly increased spontaneous MEG signal diversity under single psychoactive doses of ketamine, LSD and psilocybin; dose-response mapping of these measures has not been carried out and would be needed to anchor the permeability parameter to measurable values.`

### 1.5 (L626) Extent dimension / generalized seizure
- **Before:** `... characterizes the waking state \citep{Meisel2012,Truccolo2011}. Hypersynchronous, ...`
- **After:** `... characterizes the waking state. The direct human evidence for that departure comes from focal seizures --- ictal recordings lose the power-law statistics of the critical regime \citep{Meisel2012} and single-neuron activity is heterogeneous at onset \citep{Truccolo2011} --- and the theory extrapolates the same departure-from-criticality reading to generalized seizures. Hypersynchronous, ...`

### 1.6 (L715) Byczynski & D'Angiulli
- **Before:** `\citet{Byczynski2025} demonstrated ... causally primes detection of subliminal visual stimuli, showing that virtual-level properties modulate substrate-level perceptual processing.`
- **After:** `\citet{Byczynski2025} found ... predicts enhanced detection of subliminal visual stimuli; the result is correlational, with vividness self-reported rather than manipulated, so it is consistent with virtual-level properties modulating substrate-level perceptual processing without demonstrating it.`

### 1.7 (L805) Li et al. 2010 anosmia
- **Before:** `complete conscious anosmia instead requires a cortical lesion in right orbitofrontal cortex \citep{Li2010}.`
- **After:** `complete conscious anosmia has instead been reported after a cortical lesion in right orbitofrontal cortex \citep[single-case evidence:][]{Li2010}.`
- Uses the two-optional-arg natbib form already in the file (`\citep[cf.][]{...}` at L733), renders "(single-case evidence: Li et al., 2010)" exactly as the `.md` reads.

### 1.8 (L838) Split-brain / Pinto (mechanism section)
- **Before:** `... graded deficits observed by \citet{Pinto2017}. Partial callosotomy ...`
- **After:** `... graded deficits observed by \citet{Pinto2017} --- data the theory reinterprets as two degraded simulations, against those authors' own conclusion that callosotomy divides perception without creating two independent conscious perceivers. Partial callosotomy ...`

### 1.9 (L930) Katlowitz anesthesia preparation
- **Before:** `recorded from hippocampal neurons in patients undergoing propofol sedation for epilepsy monitoring`
- **After:** `recorded from hippocampal neurons in epilepsy patients undergoing temporal-lobe resection under propofol-based general anesthesia`

### 1.10 (L948) Siclari dream-content sentence — see §3.1
- **Before:** `\citet{Siclari2018} further showed that dream content can be decoded from posterior cortical activity during both REM and NREM sleep, consistent with the EWM generating structured experiential content whenever it is active.`
- **After:** `Within that hot zone, high-frequency activity correlated with the specific contents of dreams in both REM and NREM sleep \citep{Siclari2017}, consistent with the EWM generating structured experiential content whenever it is active.`

### 1.11 (L981) Animal-consciousness table, Criticality row
- **Before:** `Power-law neuronal avalanches in turtle cortex \citep{Shew2009} and cat visual cortex \citep{Beggs2003}, demonstrating that Class~4 dynamics are not mammal-specific \\`
- **After:** `Power-law neuronal avalanches in turtle visual cortex \citep{Shew2015} and in vivo in anesthetized cat visual cortex \citep{Hahn2010}, demonstrating that Class~4 dynamics are neither mammal-specific nor an artifact of slice preparations \\`
- The `.md` spells the Shew author list out in full; the `.tex` uses `\citep{Shew2015}` per the existing key style in that table (the pre-repair `.tex` did the same with `\citep{Shew2009}`). `Beggs2003` remains cited 5× elsewhere, so its bib entry stays.

### 1.12 (L1064) Hohwy & Seth quote
- **Before:** `... the neural correlates of consciousness, ``largely orthogonal'' to the question of what \emph{makes} ...`
- **After:** `... the neural correlates of consciousness while insisting that ``PP is not itself a theory of consciousness'' --- a scope largely orthogonal to the question of what \emph{makes} ...`
- The mis-scoped quotation mark around "largely orthogonal" is gone; the quoted string is now the one the source actually contains.

### 1.13 (L1124) Anesthetic convergence / Hengen & Shew
- **Before:** `and the \citet{HengenShew2025} criticality meta-analysis independently confirmed it through empirical consolidation of $\sim$140 datasets.`
- **After:** `and the \citet{HengenShew2025} meta-analysis consolidates $\sim$140 datasets behind the premise the argument rests on --- that cortex operates near criticality as a setpoint of brain function --- rather than testing the anesthetic claim itself.`

### 1.14 (L1132) Timmermann
- **Before:** `and dose-dependent visual cortex effects demonstrated with psilocybin \citep{Timmermann2023}.`
- **After:** `and visual-system effects demonstrated with DMT \citep{Timmermann2023}.`

### 1.15 (L1134) Split-brain / Pinto (evidence section)
- **Before:** `... \citeauthor{Pinto2017}\textquotesingle s (2017) finding of ``unified consciousness, split perception'' --- each hemisphere retains a degraded but functionally complete conscious agent.`
- **After:** `... \citeauthor{Pinto2017}\textquotesingle s (2017) finding of divided perception alongside preserved unified responding. Those authors read their data as showing that callosotomy does not create two independent conscious perceivers; the theory reinterprets the same data as two degraded but functionally complete simulations, and the reinterpretation is FMT's, not theirs.`

### 1.16 (L1136) 2×2 architecture — Doyon → Squire
- **Before:** `and to the motor learning dissociation between cerebellar-striatal implicit (procedural) learning and hippocampal-prefrontal explicit (declarative) learning \citep{Doyon2003}.`
- **After:** `and to the long-established dissociation between non-declarative (procedural) and declarative memory systems \citep{Squire2004}.`
- `Squire2004` already existed in the bib.

### 1.17 (L1184) Lucid-onset criticality marker — Voss 2014 → 2009
- **Before:** `Existing work on lucid dream onset \citep{Voss2014} reports gradual gamma-power increases rather than step-like transitions, but gamma power is a spectral measure, not a criticality measure; the two may dissociate.`
- **After:** `Existing work reports elevated frontal gamma-band activity during lucid REM sleep \citep{Voss2009}, but gamma power is a spectral measure, not a criticality measure, and the onset dynamics --- gradual versus step-like --- have not been characterized; the two may dissociate.`
- `Voss2014` is still cited (L952, the lucid-dreaming gamma-stimulation claim, unchanged in the `.md`), so its bib entry stays.

### 1.18 (L1197) Prediction 5 testability
- **Before:** `The structural arm is already demonstrated for color similarity across individuals \citep{Kawakita2025}; the novel content is ...`
- **After:** `The structural arm is demonstrated at the group level for color similarity \citep{Kawakita2025}, whose alignment ran between pooled groups of observers rather than between individuals; the individual-level structural arm, like the decoding arm, remains to be tested, and the novel content is ...`

### 1.19 (L1232) §8.9 banked results — two edits on one line
- (a) **Before:** `they share a substrate, a currency, and a form of argument`  **After:** `they share a substrate and a form of argument`
- (b) **Before:** `in a spiking architecture whose bottleneck writes to a subsystem and never reads it --- no return path at any point --- holding connectome, ...`
  **After:** `in a spiking architecture whose rank-\emph{k} write operator --- realized as the materialised dense product of its factors, not as a relayed bottleneck --- writes to a subsystem and never reads it, with no return path at any point, holding connectome, ...`
- `*k*` → `\emph{k}`, matching `\emph{t} = 14.6` in the same paragraph.

### 1.20 (L1257) Metacognition dissociation — two edits on one line
- (a) **Before:** `... decoupled from first-order performance --- only about 22\% of meta-$d'$ variance is explained by $d'$ --- and the same study reports ...`
  **After:** `... decoupled from first-order performance, and the same study reports ...`
- (b) **Before:** `Conversely, a within-subject stimulus-difficulty manipulation ($n = 12$; \citealp{Rahnev2013}) triples $d'$ (1.05 $\rightarrow$ 3.20) while metacognitive efficiency remains invariant (M-ratio $\approx$ 0.96 throughout).`
  **After:** `Conversely, manipulations of stimulus difficulty within subjects raise first-order sensitivity substantially while leaving metacognitive efficiency essentially unchanged --- the near-independence of metacognitive efficiency from performance that \citet{FlemingLau2014} describe as well established.`

### 1.21 (L1265) Basal-ganglia permeability gating — two edits on one line
- (a) **Before:** `generative adversarial networks \citep{Gershman2019}, though ...`
  **After:** `generative adversarial networks (\citealp{Gershman2019}; cf.\ \citealp{BenjaminKording2023}, on cortical interneurons as adversarial discriminators), though ...`
- (b) **Before:** `The massive compression ratio from striatum ($\sim$2.8 million neurons) to basal ganglia output nuclei ($\sim$30,000 neurons) is consistent with an evaluative bottleneck architecture \citep{BenjaminKording2023}.`
  **After:** `The massive compression ratio from striatum to basal ganglia output nuclei --- in the rat, $\sim$2.8 million neurons to $\sim$30,000 \citep{Oorschot1996} --- is consistent with an evaluative bottleneck architecture; the corresponding human ratio has not been established with comparable stereology.`
- Renders "(Gershman, 2019; cf. Benjamin and Kording, 2023, on cortical interneurons as adversarial discriminators)" — verified in the PDF.

### 1.22 (L1312) Seizure objection — two phrases on one line
- `human ictal recordings depart from` → `human ictal recordings in focal epilepsy depart from`
- `heterogeneous rather than hypersynchronous \citep{Truccolo2011}` → `heterogeneous rather than hypersynchronous, again in focal seizures \citep{Truccolo2011}`

---

## 2. `references.bib` changes

### Added (4)
| Key | Entry |
|---|---|
| `Shew2015` | Shew, Clawson, Pobst, Karimipanah, Wright & Wessel (2015). Adaptation to sensory input tunes visual cortex to criticality. *Nature Physics* 11(8), 659–663. doi 10.1038/nphys3370 |
| `Hahn2010` | Hahn, Petermann, Havenith, Yu, Singer, Plenz & Nikolić (2010). Neuronal avalanches in spontaneous activity in vivo. *J. Neurophysiol.* 104(6), 3312–3322. doi 10.1152/jn.00953.2009 |
| `Voss2009` | Voss, Holzmann, Tuin & Hobson (2009). Lucid dreaming… *Sleep* 32(9), 1191–1200. doi 10.1093/sleep/32.9.1191 |
| `Oorschot1996` | Oorschot (1996). Total number of neurons in the neostriatal, pallidal, subthalamic, and substantia nigral nuclei of the rat basal ganglia… *J. Comp. Neurol.* 366(4), 580–599. doi 10.1002/(SICI)1096-9861(19960318)366:4<580::AID-CNE3>3.0.CO;2-0 |

Placement follows the file's thematic (not alphabetical) grouping: `Shew2015`+`Hahn2010` in the
criticality cluster where `Shew2009` sat; `Oorschot1996` next to `BenjaminKording2023`/`Shepherd2011`
in the basal-ganglia cluster; `Voss2009` immediately before `Voss2014`.

**Special characters.** `Nikolić` is written `Nikoli{\'c}` — the file is pure ASCII and uses
brace-escaped accents throughout (`Llin{\'a}s`, `K\"ording`, `N{\'u}{\~n}ez`). The Oorschot DOI's
`<` and `>` were left **literal**: `plainnat.bst` emits `\doi{...}`, and because `hyperref` loads
`url`, `\doi` resolves to `\begingroup\urlstyle{rm}\Url`, which reads its argument verbatim.
Verified in the built PDF — the DOI renders as
`10.1002/(SICI)1096-9861(19960318)366:4<580::AID-CNE3>3.0.CO;2-0`, no escaping needed, no error.

### Removed (3)
| Key | Why |
|---|---|
| `Shew2009` | Replaced by `Shew2015`; zero remaining citations in `paper.tex`. |
| `Doyon2003` | Orphaned by the Squire2004 swap; zero remaining citations. |
| `Rahnev2013` | Orphaned by the Fleming & Lau rewrite; zero remaining citations. |

No divergence found on any of the three — each was cited in exactly the one `.tex` place the `.md`
repair removed. `Rahnev2020` (Confidence Database) is a different key and is still cited.

---

## 3. The two divergence investigations

### 3.1 Siclari — REAL pre-existing md/tex divergence, and the `.tex` was NOT already right

The `.md` carried a **dangling** `Siclari et al. (2021)` — no matching entry in its reference list.
The `.tex` carried the **same sentence** but resolved the citation to `Siclari2018`:

> `\citet{Siclari2018} further showed that dream content can be decoded from posterior cortical
> activity during both REM and NREM sleep, consistent with the EWM generating structured
> experiential content whenever it is active.`

`Siclari2018` = Siclari, Bernardi, Cataldi & Tononi, "Dreaming in NREM sleep: a high-density EEG
study of slow waves and spindles," *J. Neurosci.* 38(43):9175–9185.

So the two representations had **different defects for the same unsupported claim**: the `.md` cited
a year that resolves to nothing, the `.tex` cited a real paper that does not support the sentence —
it is not a decoding study, and it is NREM-only, which directly contradicts the "both REM and NREM"
in the sentence it was attached to. The `.tex` was therefore *more plausible-looking and equally
wrong*; a reader checking the reference list would have found the `.tex` citation and been misled,
whereas the `.md` at least failed loudly.

Both now read the repaired `.md` version: the content correlation is located **within** the hot zone,
in high-frequency activity, across both REM and NREM, attributed to **Siclari et al. (2017)** — which
is what that paper actually reports.

`Siclari2018` is still cited at `paper.tex` L946 (the "dreaming occurs in both REM and NREM sleep"
list), so it remains in the bib and is correctly used there.

**Worth knowing:** this is evidence that the `.md`→`.tex` mirror has drifted before in a way that
*hides* a defect rather than propagating it. A citation-key audit that compares the `.md`'s
`(Author, Year)` strings against the `.tex`'s resolved `\cite*` keys would catch this class; a build
that only checks "no undefined citations" cannot, because `Siclari2018` was perfectly well defined.

### 3.2 Schartner — NO divergence; the string search failed for a mechanical reason

The `.tex` **did** contain the claim, at L543, written as `approximately 15-20\%` — the escaped
percent sign is why a plain search for `15-20%` came back empty. The rest of the sentence matched
the pre-repair `.md` word for word, including "with dose-response curves that could anchor". Mirrored
in full (§1.4). No pre-existing divergence here.

**One related item the `.md` diff did NOT repair, flagged for the orchestrator, not acted on:**
the Permeability *construct definition* — `.md` L166, `.tex` L236 — still reads

> `\emph{Example:} \citet{Schartner2017}: Lempel-Ziv complexity increases significantly under
> psychedelics relative to placebo, consistent with increased implicit-to-explicit permeability.`

The `.md` and `.tex` agree there **exactly**, so it is not a mirror defect and I left it alone. But it
is the same paper making a claim in the vocabulary the repair just replaced two sections later:
§3.6 now says "spontaneous MEG signal diversity … single psychoactive doses of ketamine, LSD and
psilocybin", while §3.1 still says "Lempel-Ziv complexity … under psychedelics relative to placebo".
The repair deliberately dropped both "Lempel-Ziv complexity" and "relative to placebo" from the
§3.6 sentence about this paper; if that was the right call there, the same two phrases in §3.1 look
inconsistent with it. I have **not** verified Schartner et al.'s comparison condition and am not
asserting it — this is a flag, not a finding. It needs deciding in the `.md` first; I did not touch
it in either file.

---

## 4. Build verification

Throwaway build at `/home/jeltz/aIware/tmp/build-mirror-check/` (full copy of `latex/`, canonical
`paper.pdf` / `paper.bbl` never touched). Sequence: `pdflatex` → `bibtex` (sandbox disabled) →
`pdflatex` ×3.

| Check | Result |
|---|---|
| `pdflatex` exit codes | 0 on all four passes |
| `bibtex` | exit 0, **no warnings at all** (no "I didn't find a database entry", no empty fields) |
| Undefined citation warnings | **0** |
| Undefined reference warnings | **0** |
| `???` in extracted PDF text | **0** |
| LaTeX errors (`^!`) | 0 |
| Overfull boxes | **0** |
| Underfull boxes | 42 (baseline 38 — ordinary justification badness on the four lengthened paragraphs) |
| Total warnings | **3, identical to baseline** |
| Pages | 140 (baseline 139) |

The 3 remaining warnings are pre-existing and unrelated:
`microtype: Unable to apply patch 'footnote'`, `Font shape T1/lmr/bx/sc undefined`,
`Some font shapes were not available, defaults substituted`.

**Baseline control.** To be sure I introduced nothing, I also built HEAD's `paper.tex` + `references.bib`
unmodified at `/home/jeltz/aIware/tmp/build-mirror-baseline/`. It produces **the same 3 warnings, 0
undefined citations, 0 `???`, 0 Overfull**. So the delta from my edits is: +1 page, +4 underfull boxes,
**zero new warnings of any kind**.

**Rendering spot-checks in the built PDF (all confirmed present and correct):**
- Criticality definition, p.14, with the en-dash in "criticality–consciousness".
- Table 1b, p.15 — new "Implicit integrity" cell wraps cleanly, all five rows intact, table fits the page.
- `(Shew et al., 2015)` and `(Hahn et al., 2010)` in the animal-consciousness table.
- `(Oorschot, 1996)` inline, and the full Oorschot DOI in the reference list with `<`/`>` literal.
- `(Voss et al., 2009)` at the lucid-onset passage and `(Voss et al., 2014)` still correct at L952.
- Bibliography entries for Hahn (with `Nikolić`), Shew 2015, Voss 2009, Oorschot 1996.

**Cross-check:** 235 distinct cite keys in `paper.tex`, all 235 present in `references.bib`.
253 bib entries, 18 never cited — **identical set of 18 as at HEAD**, so the repair added no new orphans
and left none of its own behind.

---

## 5. Anything in the `.md` diff I could not mirror

Nothing. All 28 hunks are accounted for: 22 became `.tex` prose edits, 6 were reference-list
add/remove operations already covered in §2.

Two deliberate, reported style decisions rather than literal transcriptions:
1. **Author lists.** The `.md` writes `(Shew, Clawson, Pobst, Karimipanah, Wright, & Wessel, 2015)`
   in full; the `.tex` uses `\citep{Shew2015}` and lets `plainnat` render "(Shew et al., 2015)". This
   preserves the existing key style — the pre-repair `.tex` did exactly the same with `Shew2009`
   against the `.md`'s full "Shew, Yang, Petermann, Roy, & Plenz, 2009".
2. **`criticality--consciousness`.** Mirrors the `.md`'s en-dash at that one spot while the other four
   occurrences of the compound stay hyphenated in both files, as they already were.
