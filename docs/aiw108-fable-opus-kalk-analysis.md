# AIW-108 — Fable→Opus Kalk-scan downgrade analysis + Opus-only recipe for the open languages

**Session 252, 2026-07-08.** Question (MG): after the Fable→Opus downgrade, can we reach Fable-quality Kalk
coverage on the OPEN languages (IT/JA/ZH) using **Opus only**, and if so with what recipe / how many rounds?
Method: use **ES (Fable, 1 pass) as the control/reference**, and the **PT-vs-FR pair (both Opus, 2 primed passes)**
as the reproducibility check.

## 1. Data (category-A "objective" findings — the recall metric)

| Lang | Model | Passes | A pass-1 | A pass-2 (primed) | A total found | applied | **vs Fable control** |
|------|-------|--------|---------:|------------------:|--------------:|--------:|:--------------------:|
| **ES** | Fable | 1 (36×68ln) | 245 | — | **245** | 242 | **100% (control)** |
| **FR** | Opus | 2 (36×68 + 54×46ln) | 84 | 141 | **225** | 215 | **92%** |
| **PT** | Opus | 2 (36×68 + 54×46ln) | 83 | 144 | **227** | 218 | **93%** |

(B/voice: ES 85, FR 166, PT 167. C/motifs: ES 21, FR 26, PT 21.)

## 2. Findings

1. **The recipe is reproducible.** FR and PT — two different Romance targets, same Opus×2-primed recipe — landed at
   **225 vs 227 A-findings (Δ 0.9%)** and **166 vs 167 B**. Near-identical. So the numbers below are a *stable process
   signature*, not a per-language fluke. This is what lets us extrapolate.

2. **One plain Opus pass ≈ 1/3 of Fable.** Opus pass-1 alone caught **34%** of Fable's A-findings (FR 84, PT 83 vs
   245). A single conservative Opus pass is NOT a substitute for Fable — this is the whole recall gap MG spotted.

3. **The checklist priming is the lever that closes the gap — it transfers Fable's recall to Opus.** Pass-2
   (checklist-primed with the shared EN/DE source-calques *extracted from the ES-Fable findings* + finer 46-line
   segments) contributed **63%** of Opus's total A. Priming roughly **tripled** first-pass recall (34%→92%). The
   mechanism: the calques are **source-driven** (same EN/DE original → same trap in every target), so a checklist
   mined from the Fable pass on ONE sibling is a high-recall probe for the others. Opus is a good *executor* of a
   known checklist; it is a weaker *discoverer* from scratch. Fable discovers; Opus, once told what to look for, nearly
   matches.

4. **~8% residual is Fable-exclusive** (245 vs ~226). Composition is **confounded** — we cannot cleanly split
   "Opus deficit" from "Spanish genuinely has ~18 more calque sites than PT/FR" without a Fable pass on FR/PT. The
   residual is most likely **language-specific** issues an EN/DE source-checklist can't carry (e.g. ES conciencia vs
   consciencia; PT gender fosfenas→fosfenos) plus borderline A/B calls.

## 3. Opus-only recipe to reach Fable-quality on the open languages

**IT (Romance sibling, same EN+DE source):** the checklist transfers almost fully. Expect the FR/PT result (~92%).
  1. Translate (see caveat §5).
  2. Opus pass-1: general native-editor Kalk scan (36×~68-line segments).
  3. Opus pass-2: **checklist-primed**, finer (54×~46-line) segments. Prime with the **master checklist** =
     `tmp/shared-calque-checklist.txt` **enriched** with the source idioms FR/PT surfaced beyond ES (cheap to rebuild
     from the three findings sets). Same A/B/C/D schema + validation gate (quarantine "orig → proposed" malformed fixes).
  4. Optional pass-3 (native-grammar): a focused pass on the ~8% the source-checklist can't carry — language-specific
     grammar/gender/register — to push past 92%. Diminishing returns; the human native gate covers this otherwise.

**JA/ZH (typologically distant):** the **source-side** of the checklist still transfers (an EN idiom calqued literally
  is detectable in any language), but (a) the *target renderings* can't be reused, and (b) CJK add issue classes the
  Romance checklist doesn't cover — measure words, honorific/register level, topic-comment word order, and quote glyphs
  (JA「」, ZH "" — NOT guillemets). Expect Opus×2-primed to reach a **lower %** of Fable here, so the gap is largest
  exactly where the language is hardest. **Reserve returning Fable tokens for JA/ZH** (both translation and, ideally,
  at least a calibration scan) rather than IT.

## 4. Is another round needed, and where?

- **ES:** done (Fable). Not worth a re-scan.
- **FR / PT:** at 92–93% + the human native gate — **good enough for publish-candidate.** An optional pass-3
  (native-grammar focus, master checklist) would recover part of the residual 8%; low priority.
- **Highest-value next spend is CALIBRATION, not coverage** — see §5.

## 5. Recommended use of the incoming Fable tokens (MG: "expecting another round soon")

1. **Calibration first (cheap, removes the confound).** Spend Fable on a **small matched sample** — e.g. the same
   ~8–10 FR *or* PT segments Opus already scanned — and diff Fable-vs-Opus on identical text. That gives the **true
   per-language Opus:Fable recall ratio** (removing the ES-vs-PT language confound) and validates the 92% before we
   commit the Opus-only recipe to IT/JA/ZH. ~10 segments of Fable ≈ trivial cost, high information.
2. **Translations, not scans, are the Fable-worthy bulk.** The **translation** step is the hard-to-fix part
   (a weak translation can't be fully rescued by a calque scan — scans catch calques, not deep register/flow/voice).
   So: do IT/JA/ZH **translation on Fable** when tokens return; run the **Kalk scans on Opus** with the master
   checklist. This is why the open-language translations are postponed rather than done on Opus now.

## 6. One-line takeaway
**Opus ≈ Fable for Kalk *scanning* IF primed with a Fable-mined source-calque checklist (2 passes → ~92%, reproducible
across FR/PT to 0.9%). Keep Fable for the two things priming can't fix: the initial discovery pass on the FIRST
sibling, and the translations themselves — especially the distant JA/ZH.**
