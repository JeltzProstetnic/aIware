<!-- Action: reference -->
<!-- Tracked-by: AIW-121, AIW-106 -->
# FMT v13 pre-publication fixes — Fable final review (S268, 2026-07-24)

**Fable verdict: READY-WITH-BLOCKING-FIXES.** Theory content, peer-engagement fairness, and comms-rule compliance are at publication standard. Blockers are v13-merge consistency/citation artifacts, not conceptual defects — all mechanically fixable in one editing pass.
**Pipeline:** edit `paper/full/four-model-theory-full.md` (source) → hand-port to `paper/full/latex/paper.tex` → `references.bib` → rebuild into `tmp/`. Line numbers are v13 .md approximate.

## BLOCKERS
1. **Four-vs-five prediction count** (Prediction 5 / §8.6 added in v13, count not updated everywhere). Reconcile globally to FIVE: abstract (~L15 "Four novel predictions remain untested"), §1.3 (~L60 "these four predictions", ~L70 "four predictions"). **§7.4 (~L787 "four empirically testable claims") — READ CONTEXT FIRST**: this is a per-combination distinctiveness count, may legitimately be about that combination, not the global set. §1.3 L66 + §8 intro L795 + Conclusion L980 already say "five".
2. **Conclusion §11 (~L980) "All five are distinctive to the Four-Model Theory"** — over-claims + contradicts the abstract's own hedge (P2 partly REBUS-derivable, L15; P5 structural arm already demonstrated, Kawakita 2025, §8.6 L863). Replace with §8-intro framing: *four distinctive; P2 partly shared w/ REBUS; P5's structural arm already demonstrated, the paired dissociation is the novel content*. (Also closes the honest-convergence violation.)
3. **Bieberich RIFT DOI malformed** (~L1055): `10.64898/...` is NOT a bioRxiv DOI (bioRxiv = `10.1101/`). Verify the record exists; correct DOI/server, or cut the RIFT engagement (§7.3 ~L773 — not load-bearing).

## SHOULD-FIX
4. **§3.7 (~L422) vs §8.9 (~L893) criticality tension.** §3.7 commits to "convergence of all three signatures (branching ratio, DFA, avalanche)"; §8.9 uses Kanders 2017 that avalanche & edge-of-chaos need NOT co-occur. Add one reconciling sentence in §3.7: the three biological signatures are a false-positive guard *within one substrate*; the capability-first reading (§8.9) governs *cross-substrate* certification — cross-ref §8.9.
5. **Hengen & Shew (2025) "meta-analysis of ~140 datasets"** (asserted 6×: L54/401/413/416/803/982). Title "Is criticality a unified setpoint of brain function?" (Neuron) reads like a review/perspective. VERIFY; if review, change "meta-analysis" → "review synthesizing".
6. **§8.9 quantitative results unverifiable** (survival .29–.33 vs .17–.25; Cohen's d=2.44; transfer .98 vs .78) sourced only to Gruber 2026d "in prep"; §3.7's order-parameter treatment to Gruber 2026b "manuscript". **DECISION NEEDED:** deposit 2026d (+2026b roadmap) as Zenodo/arXiv/OSF preprint before submission and cite that, OR soften §8.9 to "preliminary (in preparation)" and drop the precise effect sizes. [AIW-124 = 2026d companion draft already exists; the fmt_formal §4.7 = 2026b now written.]
7. **Bach & Sorensen (2026)** is a Substack essay (~L1036) engaged as a peer framework in §7.3 (~L775). Frame explicitly as an informal/online essay in-text, or anchor the self-simulation-convergence point to Bach's peer-reviewed work.
8. **ConCrit citation** (Algom & Shriki 2026, Neurosci & Biobehav Rev 180:106483) cited ~8×, load-bearing — VERIFY authors/title/vol/pages independently. (Trivial: ref reads lowercase "concrit"; body "ConCrit".)
9. **§5.1 (~L578) IWMT jab** — "must treat these states as degraded or borderline" is a mild strawman vs the fair §7.3 IWMT treatment + the live Safron outreach. Soften → "reduced-coherence limiting cases, where FMT predicts them as core."
10. **§3.4.4 "Temporal Echo Mechanism"** — evocative metaphor (information-singularity / event-horizon / temporal-smearing) presented as "mechanism" ("This section proposes a mechanism"). Softest target in a rigorous paper. Relabel heuristic/illustrative, or foreground the "gap not closed" hedge (L332) at the section head.

## OPTIONAL
- Hengen & Shew dataset count varies "over 140"/"~140"/"140" — pick one.
- "IIT-Concerned et al., 2025" (L27) informal author string → proper reference.
- Van Rullen & Koch 2003 "20 Hz / ~500 ms" figures (L502) — verify (their discrete-perception work centers ~7–13 Hz).

**Highest-value single change (Fable):** fix #1 count globally + #2 conclusion hedge — closes both A-blockers + the honest-convergence violation, and removes the top hostile-reviewer attack ("no distinctive confirmed evidence").

**Non-blocking strengths Fable confirmed:** modularism compliance (no "four modules" phrasing survives), IIT/GNW/IWMT engagement fair + non-strawmanned, §8.9 crucible-framing exemplary per prediction-framing.md, cross-references clean.

## Artifacts
- Tracked-changes PDF (baseline = last v12 build S244/374b05f0 → v13): `tmp/v13-trackedchanges/paper.pdf` + `C:\Users\Matthias\Downloads\fmt-v13-tracked-changes.pdf` (123pp; 166 add / 27 del blocks).
- fmt_formal §4.7 (Gruber 2026b, roadmap): DONE this session, build-clean `tmp/build-fmt-formal/fmt-formalization.pdf` 31pp.
