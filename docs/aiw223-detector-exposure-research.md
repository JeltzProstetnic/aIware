<!-- Action: reference -->
<!-- Tracked-by: AIW-223, AIW-212 -->
# AI-detector exposure — the research behind `AIW-223`

**S306, 2026-08-23.** Defensive measurement: what would a detector say about MG's own writing, so
submission decisions can be made case by case. Two Fable research passes, no text sent anywhere.

---

## 1. MG's hypothesis is BACKWARDS — for one detector family, and that family is not the one that matters most

MG's guess: *"the more rigorous a text the less alternate word choices the less detectable."*

**Wrong for the perplexity/burstiness family**, and the causal direction has been tested rather than
assumed. **Liang et al. 2023** (*Patterns* 4:100779) found 7 commercial detectors averaged **>61%
false positives on human-written TOEFL essays** (~97% flagged by at least one) while scoring native
US 8th-grade essays near-perfectly. Then they ran the manipulation both ways: using a model to
**enrich** the word choice of human essays **reduced** flagging; **simplifying** native essays'
vocabulary **increased** it. Constrained word choice raises detection, it does not lower it.

Corroborating: 14,400 genuine oncology abstracts (1980–2023, most written before LLMs existed) were
falsely flagged at **up to 8.7%**, 5.1% scoring ">90% AI", the *NEJM* subset **10.2%**. And the
canonical embarrassment — ZeroGPT scores the US Constitution ~92–98% "AI". That is exactly "rigorous
text with few alternate word choices."

**⚠ But the inversion does not carry to trained classifiers.** Pangram is a different animal:
vendor-reported 0.01% overall FPR and **0.004% on academic essays**; an independent Chicago Booth
study (Jabarian & Imas, WP 2025-116) found ~0 FPR on long passages and named it the only detector of
four meeting a 0.5% FPR cap and the only one robust to "humanizers".

⇒ **Two separate exposures, and they must not be merged.** Against GPTZero-style tools MG's most
careful papers are his *highest*-risk artifacts. Against Pangram, false positives are rare — so the
exposure there is not false positives at all, it is **text a model actually wrote**, which is a true
positive.

## 2. ✅ Anthropic text watermarking is REAL, announced 2026-08-11

Under the EU AI Act Transparency Code (effective 2 Aug), Anthropic embeds a SynthID-style
imperceptible watermark in generated text.

- **Scope:** models launched **on or after 2026-08-02**; older models "in transition". Covers **API,
  Claude, Claude Code**, Cowork, cloud partners.
- **No public detection tool yet** — "forthcoming technical documentation".
- Anthropic's own framing: it shows content **"may have been *processed* by Claude"**, explicitly
  **not** authorship.
- Survives "some editing"; lost under heavy edit, paraphrase or translation.

**⚠ The consequence that bites a submission decision made today:** text generated now may become
**retroactively attributable** once detection ships. A submission cannot be un-made.

**Unknown, and the help centre is silent:** whether current Claude Code / Fable output is already
marked. Do not assume either way.

**For comparison** — **Google** SynthID-Text has been in production since 2024-10-23 (~20M responses,
*Nature*); generator open-sourced, **detection needs Google's key**. **OpenAI** built a watermark
(~99.9% effective internally) and **never shipped it**; ChatGPT text carries none.

⇒ **No journal or third party can watermark-check anything today.** Watermark detection and AI-text
classification are different problems and any deliverable must keep them apart.

## 3. ⚠⚠ What NeurIPS actually did, and what it means for `AIW-212`

**The NeurIPS 2026 Position Paper Track ran Pangram over every submission and desk-rejected 178 —
18.4%.** Primary source `blog.neurips.cc/2026/06/02`. Thresholds:

| condition | outcome | n |
|---|---|---|
| score ≥ 0.9 | reject, no appeal | 77 |
| score ≥ 0.8 + corroborating patterns | reject | 79 |
| **score ≥ 0.5 where the author denied or failed to declare AI use** | reject | 22 |
| score 0.8–0.9 | conditional — produce documented **pre-AI / post-AI / final version history** by 15 June or be rejected | 123 |

**✅ That trap does not exist for the "AI and the Self" workshop, checked 2026-08-23.** The CFP is
**silent** on AI use, and the OpenReview submission form has **no AI-use field** (fields are exactly
`title, authors, keywords, TLDR, abstract, pdf, email_sharing, data_release`). The ≥0.5 rule needs a
*solicited* declaration to deny; none is solicited. The Position Track's policy is **explicitly
scoped to that track**; the Main Program's policy is permissive ("authors are welcome to use any tool
they wish"). **The workshop adopted neither.**

⇒ **Do not add an unrequested AI-use statement to an anonymous PDF.** It satisfies no requirement and
adds deanonymization surface. If a disclosure is requested later, that is the hook.

**Deadline:** CFP says **24 Aug 23:59 AoE** and that is binding. The OpenReview invitation's technical
duedate is 29 Aug 12:15 UTC (+30 min grace) — a safety net, **not** an extension.

## 4. ▸▸ The strongest defence is not a detector score

**The remedy NeurIPS actually accepted was documented version history.** aIware's git log — markdown
sources, commit-by-commit, session logs, per-paper build provenance — *is* that artifact, and it
already exists for every paper in this repo. **It is worth more than any score this project can
produce**, because it is evidence about process rather than a probability about prose.

## 5. Venues and publishers — disclosure, not detection

Elsevier, Springer Nature, Wiley, IEEE, ACM, T&F and PLOS are uniformly **disclosure-based**; AI
cannot be an author (COPE, Feb 2023). Screening infrastructure exists — Springer Nature's **Geppetto**,
Elsevier's **Check Integrity** (~2,000 journals) — but targets fabricated content and tortured
phrases, not AI assistance. **A hit triggers an editorial query, not automatic misconduct**, and COPE
guidance says detector inconsistency makes them unsuitable as a sole basis for accusation.
Universities default to Turnitin; Vanderbilt (2023) and MSU disabled it over false positives.
**arXiv** does not screen; its 1-year ban needs "incontrovertible evidence" (hallucinated references,
leftover model meta-comments) and it blocks AI-generated survey papers.

## 6. Local detectors — ranked for the 4090

All viable open options are **perplexity-family**, which answers "would a GPTZero-style tool flag
this". ⚠ **None emulates Pangram (proprietary), so NeurIPS-style exposure can be bounded locally but
never measured.**

1. **Binoculars** (ICML 2024) — **implement first.** Two-model observer/performer (Falcon-7B +
   Falcon-7B-Instruct); score is a perplexity ÷ cross-perplexity ratio. ~90% TPR at 0.01% FPR,
   zero-shot. BSD-3 code, Apache-2.0 weights. **bf16 needs ~28 GB — over budget on a 24 GB card**;
   run 8-bit (~15 GB) or sequential per-model passes with logit caching (shared tokenizer allows it).
   English-tuned, so it shifts on German.
2. **Fast-DetectGPT** (ICLR 2024, MIT) — cheap cross-check, single model, fits trivially.
3. **RADAR** (NeurIPS 2023) — the only open *trained-classifier* counterpoint, <2 GB. 2023-era;
   expect drift against 2026 models.
4. **Skip:** DetectGPT (superseded), OpenAI's RoBERTa detector (deprecated, authors warn against it),
   SynthID-Text OSS (detects only watermarks made with your own key).

## 7. Calibration design — the part that decides whether any number means anything

- **Score prose chunks of ≥250–300 tokens**, after stripping LaTeX, maths, citations and bibliography.
  Below that every detector is noise (OpenAI drew its line at 1,000 characters).
- **▸ The control corpus is the whole game.** MG's **2015 German monograph** and any pre-2022 prose
  are certainly-human text *by the same author* — the only way to turn a score into a decision.
  ⚠ Binoculars is English-tuned, so the German monograph shifts the distribution: prefer pre-LLM
  **English** prose where it exists and calibrate German separately.
- Verify AUROC on the controls **before** trusting any score on a paper.
- **The output may claim:** "Detector X at threshold t flags k% of MG's known-human text and j% of
  paper Y's sections." That k is a *personal* false-positive rate — the paper-independent prior that
  his style trips detector X.
- ⛔ **The output may NOT claim "this paper is Y% AI."** Vendor percentages are thresholded scores
  mapped through the *vendor's* calibration corpus. Not a probability, and not comparable across
  detectors.

## 8. Known failure modes with direct relevance here

**Translated text** (Weber-Wulff et al. 2023, *Int J Educ Integrity*: 6 of 14 tools produce false
positives on machine-translated human text; all tools <80% accurate; obfuscation drops accuracy to
~26%) — relevant to the German→English pipeline. **Non-native register**, by the low-lexical-variability
mechanism rather than nationality. **Formulaic academic prose.** **Short texts.** **LaTeX/maths-heavy
text** — practitioner consensus, no measured study found; treat as unverified.

## 9. Not established

- Whether the NeurIPS **main track** or any workshop screens (only the Position Track is documented).
- Whether Elsevier/Wiley run general AI-*writing* detectors on all submissions.
- **Anthropic's transition coverage** — whether pre-Aug-2026 models, including current sessions,
  already watermark, and when detection ships.
- Which detector the oncology study used; Turnitin's current FPR (vendor claims only); Pangram's FPR
  on non-native *academic* authors specifically.
