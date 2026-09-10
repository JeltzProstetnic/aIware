# Temporal/coherence issues in the SHIPPED ed.2 — report for the author-copy decision

**Session 252, 2026-07-08.** Method: one Opus native-editor read each of the **shipped** EN and DE ed.2 manuscripts
(`pop-sci/book-manuscript.md`, `-de.md`) cover-to-cover, in order, flagging restructure fallout (wrong cross-refs,
term re-explanations, result-before-question, re-narrated anecdotes). Severity + how visible to a printed-book reader.
Data: `tmp/en-de-coherence.json`. This feeds AIW-109 (ed.3 + re-propagation).

## BOTTOM LINE (for the copies you ordered)
The **EN author copies are safe to use and gift.** **5 issues, ZERO "obvious", none is a content/argument error** —
the book reads correctly cover-to-cover. The only reader-noticeable ones are **3 wrong chapter-reference numbers**,
each a single wrong digit, invisible to a casual reader and **fixable with a pen in ~30 seconds per copy**. 2 more are
editor-only (a term re-introduced as if new) and invisible in normal reading.

**Recommendation by recipient:**
- **You / friends / family / general readers / signings:** use them as-is. No one reading for pleasure will notice.
- **High-stakes academics & the researchers you're courting** (people who might *follow* a chapter reference): either
  **pen-correct the 3 refs** in those specific copies (exact edits below) or give them the corrected **ed.3** once built.
- **Do NOT bin them.** Nothing here is embarrassing enough to justify that. The worst case is "an attentive academic
  spots a stale chapter number," which the pen fix fully removes.

## EN — 5 issues (0 obvious · 3 attentive · 2 editor-only)

| # | Sev | Visible | What | Pen-fix in a printed copy |
|---|-----|---------|------|---------------------------|
| EN-1 | med | attentive | **Ch.13** says the anosognosia mechanism is "(Chapter 8)". It's actually in **Ch.6** ("Anosognosia: The Inverse", the two-handed-clap story). Ch.8 is Anton's syndrome. The Appendix-A glossary itself says "(See Chapter 6.)" — so the book contradicts itself. | In Ch.13, change **"(Chapter 8)" → "(Chapter 6)"** at "the same mechanism behind anosognosia". |
| EN-2 | med | attentive | **Ch.17** says "Leibniz's Identity of Indiscernibles, which we met in **Chapter 1**." Ch.1 never names it; it's introduced in **Ch.13**. | In Ch.17, change **"which we met in Chapter 1" → "which we met in Chapter 13"**. |
| EN-3 | med | attentive | **Ch.10** (conversion disorder) says "closes the loop back to **the last chapter**: the blindsight from Chapter 8." The last chapter is Ch.9 (split-brain); blindsight is Ch.8 — the clause points at two chapters at once. | In Ch.10, change **"the last chapter" → "Chapter 8"** (keep the rest). |
| EN-4 | low | editor-only | **Ch.15** re-introduces "self-organized criticality" + Per Bak + the sandpile as if new; first used in **Ch.5**. | (not pen-worthy) |
| EN-5 | low | editor-only | **Ch.4** re-glosses "digital twin (a jet engine…)"; fully defined in **Ch.2**. | (not pen-worthy) |

## DE — 13 issues (1 obvious · 7 attentive · 5 editor-only)
The DE ed.2 carried the larger wave-1 restructure, so more fallout. Highlights:
- **DE-8 (medium, OBVIOUS):** the **Coda re-tells the avalanche anecdote in full** (military, reckless officer, life
  flashing by) though it was already told fully in **Ch.13** — a reader notices the same story twice. (DE-9: the two
  tellings even differ slightly — Ch.13 adds "later disciplined", the Coda drops it.) → the one issue a normal DE
  reader *will* clock.
- **DE-2 (high, attentive):** the **same anosognosia "(Kapitel 8)" → should be "(Kapitel 6)"** as EN-1 — and **DE-3**
  notes the DE glossary already says Ch.6, so the DE book also contradicts itself. This is the clearest **structural**
  (both-editions) error.
- **DE-11/DE-13 (medium, attentive):** cognitive-ceiling objection re-explained Ch.16→Ch.17; an imprecise "am Ende
  dieses Buches" forward-ref that's actually paid off in Ch.13.
- 8 low ones: hologram re-explained (Ch.9 vs Ch.3), Wolfram classes framed as if Appendix-C-native (vs Ch.5),
  real/virtual line stated as "the foundation" then relativised in Ch.14, etc.

## Shared / structural vs edition-specific
- **Structural (in BOTH shipped editions → also in ES/FR/PT translations):** the **anosognosia Ch.8→Ch.6** wrong ref
  (EN-1 = DE-2, and the FR pass flagged it too); the **hologram re-explanation** (DE-5 ≈ FR); the **Coda avalanche
  re-narration** (DE-8 ≈ FR). These get fixed **upstream in the EN/DE `.md` and re-propagated**, never per-language.
- **Edition-specific:** most DE low items are DE-restructure-only; EN's Leibniz + "last chapter" refs are EN-only.

## Next (AIW-109)
1. **You decide the copies** (pen-fix the 3 EN refs for high-stakes recipients; otherwise use as-is).
2. **ed.3:** apply the fixes upstream in EN + DE `.md` → rebuild → re-upload KDP (all 6 editions).
3. **Re-propagate** the structural fixes to ES/FR/PT (and IT/JA/ZH when translated).
4. Run the same coherence pass on ES/PT (like FR) for edition-specific temporal issues.

---

## ADDENDUM — S254 (2026-07-10): IT whole-book coherence pass surfaced NEW structural items

Method: one Opus native-IT editor read `book-manuscript-it.md` cover-to-cover (AIW-108 IT finish). It-only fixes
(TOC↔heading title drift ×3, «delirio di Salvia»→lowercase, +5 dropped `---` chapter separators) were applied to IT
directly. The **6 structural** items below affect ALL editions (or the shipped EN/DE) and belong to AIW-109's upstream
batch — do NOT patch per-language:

| # | Sev | What | State across editions | Upstream fix |
|---|-----|------|-----------------------|--------------|
| **A** | **HIGH** | **Neuron-loss self-contradiction.** Ch.12 brain-vs-computer list says the brain loses **"a million neurons a day"** (EN l.1090 / IT l.1086); ~90 lines later the persistence passage says **"85,000 neurons per day — about one per second"** (EN l.1182 / IT l.1178). The two flatly contradict; 85,000/day (≈1/s) is the internally consistent one, "a million/day" is off by an order of magnitude. | **EN ed.2 (SHIPPED) HAS the contradiction.** **DE ed.2 is already CONSISTENT** — uses 85.000 in BOTH spots (l.1067, l.1159). ES/FR/PT/IT/JA inherited EN's "million". | Fix **EN** "a million neurons a day" → "85,000 neurons a day" (align to DE + to EN's own l.1182) → re-propagate to ES/FR/PT/IT/JA. **NB: this REVISES the "EN author copies are safe, 0 obvious" verdict above — this is an internal factual contradiction the S252 EN pass missed. Attentive-reader visible. MG decides copy fate + whether to correct EN now.** |
| B | med | **Ch.10 conversion-disorder loop-close** says "back to the previous chapter" then names Chapter 8 (prev chapter is 9). = the report's **EN-3**, already fixed in EN ("closes the loop back to Chapter 8"). | EN fixed; **still pending in ALL translations** (FR "chapitre précédent" l.1030, JA 前章 l.1032, IT "capitolo precedente" l.1032, ES/PT likely too). | Re-propagate the EN-3 fix to ES/FR/PT/IT/JA. |
| C | med | **Coda re-narrates avalanche + knockout anecdotes in full** (already told Ch.13/Ch.12). = report's DE-8 (fixed in DE). | DE fixed; EN + all translations likely still full re-narration. | Compress Coda retellings to allusive callbacks upstream in EN, re-propagate. |
| D | med | **Ch.15 re-introduces self-organized criticality + Per Bak + sandpile as if new** (first used Ch.5). = report's **EN-4** (fixed in EN). | EN fixed; translations still re-introduce. | Re-propagate EN-4 callback rewrite to translations. |
| E | med | **Ch.15→16 dangling bridge:** "…E sono più strane di quanto mi aspettassi" — plural-feminine subject with no antecedent (EN "and they are stranger than I expected"). Restructure seam. | Likely all editions (check EN). | Supply antecedent upstream ("the consequences are stranger…"), re-propagate. |
| F | low | **Chapter-separator `---` dropped before Ch.9/10/16/App-A/App-C in IT only** (assembly gap; EN clean). | **IT-specific** — FIXED in IT this session. Check ES/FR/PT/JA assemblies for the same dropped-separator gap. | none upstream; verify siblings. |

**Sibling-hygiene (from item F) — CONFIRMED (S254):** `^---$` counts: EN 45, DE 45, IT 45 (fixed), JA 45 (fixed) · **ES 41 (−4), FR 42 (−3), PT 40 (−5)** still dropped chapter separators during assembly. Fix ES/FR/PT at their coherence passes — add `---` before every chapter/appendix heading missing it, matching EN's 45.

### JA coherence pass (S254) — CROSS-CONFIRMS items A–D + one new item

The independent JA whole-book coherence read re-found the SAME structural defects as the IT pass — strong cross-edition confirmation they live upstream:
- **Item A** (neuron contradiction 百万 vs 8万5000/日) — confirmed in JA (第12章 l.1090 vs l.1182).
- **Item B** (Ch.10 loop-close off-by-one, 前章 → 第8章) — confirmed in JA (l.1036).
- **Item C** (Coda re-narrates 雪崩/ノックアウト) — confirmed in JA.
- **Item D** (Ch.15 self-org criticality + Per Bak re-intro) — confirmed in JA (第15章 l.1454).

| # | Sev | What | State | Upstream fix |
|---|-----|------|-------|--------------|
| **G** | med | **"the German book's analysis" authorial self-reference** (EN l.828 "The key insight from **the German book's analysis** of these syndromes…" → JA l.828 「ドイツ語版の分析から得られる核心的な洞察」). A reference to MG's 2015 German monograph; reads oddly in the translations (a JA/ES/FR reader has no "German book" frame). Present verbatim in EN. | **EN (SHIPPED) has it**; translations render it faithfully. NOT a translation bug. | MG decides: keep (it's a real book) or make edition-neutral upstream ("my 2015 analysis" / "the original analysis") → re-propagate. |

### ZH coherence pass (S254) — THIRD independent confirmation of A–D + G

The ZH whole-book coherence read re-found **all five** structural items — three independent Opus passes (IT, JA, ZH) now agree, which is as strong as this gets without a human read:
- **A** neuron contradiction (ZH 第12章 l.1092 「一百万」 vs l.1184 「85,000／每秒一个」) — confirmed.
- **B** Ch.10 loop-close off-by-one (ZH 「上一章」→ should be 第8章) — confirmed.
- **C** Coda re-narration (雪崩／击昏／分形) — confirmed.
- **D** Ch.15 Per Bak / sandpile re-intro — confirmed.
- **G** German-original authorial ref (ZH 第8章 l.830 「德语原著在分析这些综合征时」) — confirmed.

No new structural items from ZH. **Bottom line for AIW-109: items A (HIGH, factual) and B (HIGH) are the priority upstream EN/DE fixes; they now have 3-language confirmation.**

### RESOLVED (S254, 2026-07-11) — MG directive "fix everything everywhere" + corrigendum

**The wrong-fact / wrong-reference errors are now fixed in ALL 8 editions' `.md` source:**
- **A neuron contradiction** → 85,000/day in EN/ES/FR/PT/IT/JA/ZH (DE was already consistent).
- **B Ch.10 off-by-one** → Chapter 8 in DE/ES/FR/PT/IT/JA/ZH (EN already fixed), mirroring EN's "…from that chapter" structure.
- **EN-2 Leibniz** cross-ref → Chapter 13 in DE/ES/FR/PT/IT/JA/ZH (EN already fixed).
- **EN-1 anosognosia** = Chapter 6 everywhere (+ZH cross-ref added for parity).
- **Separator parity** restored: all 8 editions = 45 `---` (ES/FR/PT dropped-separator gaps fixed).

**Corrigendum note** for MG's ed.2 print author copies (friends/family giveaways) = `drafts/corrigendum-ed2.pdf` (EN + DE; lists the 4 EN / 3 DE reader-relevant corrections).

**STILL OPEN (style / ed.3 refinements, NOT errors — deferred to the next-session Fable review):** C (Coda re-narration), D (Ch.15 criticality re-intro), G (German-book authorial ref) — these need coordinated EN/DE upstream *rewrites* then re-propagation. Plus the ed.3 interior rebuild + KDP re-upload of all editions.
