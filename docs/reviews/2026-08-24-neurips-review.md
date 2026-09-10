# Adversarial review — NeurIPS 2026 workshop submission (AIW-212)

Reviewed 2026-08-24, against the revision deadline 24 Aug 23:59 AoE (25 Aug 13:59 Austrian).
Sources checked: `drafts/neurips-ai-and-the-self-2026.md`, `tmp/neurips-submission/PAPER-anonymous.pdf`,
`scripts/build_neurips_workshop_pdf.py`, all seven references verified against primary sources
(arXiv full text, Crossref DOI records, Zenodo, Nature).

## Verdict

**No defect requires a re-upload.** Every factual claim and number in the paper checks out against
primary sources, every citation is real and accurately attributed, the PDF is anonymous including
metadata, and all internal cross-references resolve. One *optional* strengthening is available and is
deadline-sensitive: the handover's Hoque-ownership argument is now **verified against the primary
source** (it IS a single 7-point "comfortable publishing under your own name" item), and adding one
sentence to §2 would close the paper's only undefended flank — a reviewer reading Hoque as a felt-
ownership result can present it as a counterexample to the sign prediction. That is an argument
upgrade, not a repair; the decision whether it justifies re-uploading before the deadline is MG's.
Everything currently in the paper is true as written.

---

## Findings (most consequential first)

### 1. Hoque ownership measure — hazard CONFIRMED against primary source; paper's current use is defensible; a verified strengthening is available

- **Status: CONFIRMED (primary source: arXiv 2311.13057v3 full text).**
- Hoque et al.'s "ownership" measure is exactly what the handover suspected — a single 7-point item:
  *"On a scale of 1 (not at all comfortable) to 7 (very comfortable), how comfortable would you be in
  publishing the short story under your name?"* (baseline 3.39 vs HaLLMark 4.92, d = 0.46).
  By the submission's own §5/Appendix taxonomy ("willingness to sign sole-authored"), that is
  **declared authorship, not felt ownership**.
- **What the paper currently says** (md:21): *"Hoque et al. (2024) built a tool that visualizes the
  provenance of each text segment and report, from a study with thirteen creative writers, that it
  helped them retain a sense of control and ownership."* This is accurate reported speech — it is
  precisely what Hoque et al. claim in their own abstract — so it satisfies the project's "state what
  the cited paper actually argues" rule. **Not a defect.**
- **The exposure:** taken at face value, Hoque's result (provenance marking → *higher* "ownership")
  is a prima facie counterexample to the paper's central sign prediction (marking → *lower* felt
  authorship, md:43). The paper never confronts this. The now-verified fact that Hoque's item measures
  comfort-signing — the construct the paper itself says moves *independently* of felt ownership —
  converts the apparent counterexample into support for the paper's own felt/declared distinction.
  One sentence in §2 (after the 14%→3% sentence, md:23) would do it. Optional; MG's call; last chance
  is the deadline.

### 2. Anonymity — clean, with one inherent residual noted

- **Status: CONFIRMED clean** (md grep, PDF full-text grep, PDF metadata).
- PDF metadata: `title`, `author`, `subject`, `keywords` all empty; producer is pdfTeX. No leak.
- Full text: no "Matthias", no ORCID, no matthiasgruber.com, no aIware, no Ivoclar, no
  acknowledgements section, no first-person self-citation. The only "Gruber" hits are third-person
  citations "(Gruber, 2026)" — the form double-blind convention requires and the build gate
  deliberately permits.
- `tmp/neurips-submission/PAPER-anonymous.pdf` is **byte-identical** (md5 7ba5224c…) to
  `tmp/build-neurips/neurips-ai-and-the-self-2026.pdf`, timestamp 2026-08-23 22:44:29 — the kit holds
  the current version containing both late changes (§6 disclosure sentence and the Hoque 14%→3%
  figure both present on PDF pp. 2 and 4).
- **Residual, unavoidable:** a paper whose entire theoretical base is one single-author Zenodo
  preprint lets a motivated reviewer infer the author. That is a property of the paper's design, not
  a fixable leak; NeurIPS policy is satisfied.
- **Not verifiable from here:** whether the PDF *on OpenReview* is this 22:44 version. The handover's
  check stands: open the submitted PDF, §6 final paragraph, look for "drafted with AI assistance
  under the marked condition of §5". I did not touch OpenReview (constraint).

### 3. Every number recomputed — all correct

- **Status: CONFIRMED.**
- "n = 30 and n = 96" (md:11) — matches Draxler et al. Study 1/Study 2 exactly.
- "verbatim-AI share … fell from 14% to 3%" (md:23) — primary source says 13.66% (baseline) vs
  3.48% (HaLLMark). Standard rounding; fair. (Note the study's own term is "text written by the AI";
  "verbatim-AI share" is a faithful paraphrase.)
- "thirteen creative writers" (md:21) — matches (13 participants).
- Appendix power claim (md:91): d = 0.3, α = .05 two-tailed, power .90 → normal approximation gives
  n ≈ 116.7, exact paired-t ≈ 119. "approximately 120" is correct.
- No ratio/quantifier claims of the §8.9 type exist in this paper (checked every comparative
  sentence).

### 4. All seven references verified against primary records — all correct

- **Status: CONFIRMED** (Crossref, arXiv, Zenodo, Nature, publisher pages).
- **Draxler et al. 2024** — title, all seven authors in order, TOCHI 31(2), DOI 10.1145/3637875: all
  exact per Crossref. The three findings attributed to it (ownership/authorship dissociation across
  two studies; influence raises ownership while personalization has no effect; larger discrepancy for
  supposed *human* ghostwriters) are all in the paper's abstract/results.
- **Hoque et al. 2024** — title, all seven authors, CHI 2024, DOI 10.1145/3613904.3641895: exact.
- **Joshi & Vogel 2025** — title, authors, CUI '25, DOI 10.1145/3719160.3736608: exact per Crossref.
  Both attributed findings confirmed from the paper: an unassisted-writing condition existed and AI
  writing lowered psychological ownership; longer prompts → higher ownership.
- **Joshi & Vogel 2026** — arXiv:2507.03670, Graphics Interface 2026: exact. The load-carrying claim
  (md:25) is confirmed verbatim from the abstract: interface techniques raised prompt length AND
  ownership; adding AI-generated suggestions "further increased prompt length, but did not lead to
  improvements in psychological ownership." The paper's cautious framing ("not designed to test this,
  so we do not lean on it") is accurate.
- **Wegner & Wheatley 1999** — Am. Psychologist 54(7), 480–492, DOI 10.1037/0003-066X.54.7.480: exact
  per Crossref. Priority/consistency/exclusivity is the correct trio.
- **Dijkstra & Fleming 2023** — Nat. Communications 14, 1627, DOI 10.1038/s41467-023-37322-1: exact.
  Abstract states verbatim that "imagined and perceived signals are in fact intermixed, with
  judgments of reality being determined by whether this intermixed signal is strong enough to cross a
  reality threshold."
- **Gruber 2026** — DOI 10.5281/zenodo.18669891 resolves (concept DOI → latest version, currently
  v14 "The Four-Model Theory of Consciousness: A Simulation-Based Framework…"). Cited work exists,
  author/year correct.

### 5. SUSPECTED (minor, judgment): the Dijkstra & Fleming gloss slightly extends the finding

- md:37: *"…with judgments of reality turning on whether the combined signal strength crosses a
  threshold: **no single factor unambiguously marks a signal's source**."* The clause after the colon
  is an interpretation, presented in the same breath as the finding. It is well supported — their
  result specifically rejects the "intention-as-source-tag" alternative — so I judge it defensible,
  but a hostile reviewer could note the paper words it as if quoted. Minimal repair if desired:
  "…crosses a threshold — that is, no single factor unambiguously marks a signal's source." Cosmetic.

### 6. Minor reference-style notes (no action needed)

- Gruber reference gives the short title only; the Zenodo record carries a subtitle. Common practice
  for preprints; not a defect.
- In the built PDF, "References" renders as numbered section "7" and the appendix heading reads
  "A Appendix: Experimental design detail" (the word Appendix doubled by the `\appendix` + heading
  text). Both cosmetic, both artifacts of the pandoc path; neither violates the CFP.

---

## Internal consistency — all cross-references resolve

- §1 "We return to this last finding in §6" → §6 first limit discusses exactly that finding. ✓
- §6 "The human-ghostwriter finding of §1" → present in §1. ✓
- §6 disclosure "the marked condition of §5" → §5 defines a marked condition (staged, visually
  attributed, confirm/dismiss), and the disclosure's description ("every contribution staged and
  attributed before it entered the draft") matches the representation property, which is what the
  sentence claims. Coherent. ✓
- §5 "detailed in Appendix A" → exactly one appendix, labeled A. ✓
- Footer "40th Conference … (NeurIPS 2026)" — 2026 is the 40th. ✓
- Falsification block (md:59) is internally coherent: three outcomes map to three rival readings
  without overlap.

## Prose-register notes (LOW priority, reported last per brief)

1. §6 final sentence *"We record it because a paper on the phenomenology of assisted writing that
   concealed its own production would be a poor instrument"* brushes the banned S276 class
   ("advertises its own honesty"). The disclosure itself is content MG explicitly wanted; the
   justification sentence is the optional part. Flagged, not urged.
2. §4 *"which is exactly the point"* — mild cadence tic. Leave unless retouching anyway.
3. No hits on the named bans: no "load-bearing", no "bite", no "worth noting", no "Importantly/
   Crucially", no revision-history narration, no reviewer-addressing.
4. Prediction framing complies with `prediction-framing.md`: single operationalized prediction with
   sample size, effect size, falsification criteria, and explicit competitor comparison; §6 cleanly
   separates the dissociation result from confirmation of the source theory.

## Nothing found in these areas (explicitly checked)

- Arithmetic/quantifier errors of the §8.9 type — none (every number recomputed, item 3).
- Fabricated or misattributed citations — none (all seven verified to primary records, item 4).
- Anonymity leaks in md, PDF text, or PDF metadata — none (item 2).
- Acknowledgements, funding statements, ORCID, personal domains — absent.
- Dangling section references, phantom appendix, abstract/body mismatch — none.
- Kit-vs-build divergence — none (byte-identical PDFs).
- Claims cited as "tests" that are only "consistent with" — none found; the paper's own hedging
  (Joshi & Vogel 2026 "we do not lean on it"; Draxler "consistent with both") is accurate.
- One thing NOT checkable from here: which version is on OpenReview (live-service constraint) —
  the handover's §6-sentence check remains the test.
