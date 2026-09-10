<!-- Action: reference -->
<!-- S293: BOTH halves are now executed. RIM was repaired and published S292; the cosmology half —
     all five criticals, all five reference defects, and both referee silences — was repaired S293 and
     the build promoted to canonical. This file is PROVENANCE ONLY: it records what the defects were
     and who found them. It is NOT a work order and nothing in it is outstanding. Current cosmology
     state: docs/pending-s294-cosmology.md. S295 closed the last two steps — the citation gate is
     clean (145/145) and cosmology is published as Zenodo v4 (10.5281/zenodo.21844284). Three FURTHER
     reference defects of this same class were found in S295 while clearing the gate (Boyle2018 missing
     an author, an Elze chimera, an unfindable Gruber1968) — i.e. the S291 sweep did not exhaust the
     class, and the existence gate is what caught the remainder. -->
<!-- Tracked-by: AIW-171 (RIM), AIW-172 (cosmology), AIW-173 (prospective research), AIW-170 (citation gate) -->
# S291 Fable passes — the defect lists that block both publications

Two adversarial Fable passes ran S291 (2026-08-07) on MG's instruction. **Both papers are BLOCKED from
publishing.** MG's suspicion about cosmology ("we havent looked thoroughly") was correct.

**S292 status.** Every finding below has now been independently re-verified — see
`docs/s292-citation-verification.md` for what was checked against what. Two came back different from the
report: C4 is worse than described, and C7 is refuted as stated (the real defect is md↔tex drift). The
**RIM list is repaired**; what still blocks its publication is the whole-paper review, not this list. The
**cosmology list is untouched** and its five confirmed reference defects are recorded as `defective` in
`docs/reference-manifest.json`, so they block the build until repaired.

**Verification status (as written S291):** the citation findings below are the agents'. I independently
re-verified four of them against Crossref/arXiv this session — all four confirmed. The rest are
agent-reported and must each be re-verified as they are fixed, not fixed on trust.

## Correction to the RIM agent's framing

The RIM agent wrote that "the revision itself introduced three chimeric citations." **That is wrong.**
All four flagged RIM items are present at commit `28291ed8`, i.e. before the S291 revision: Gignac ×3,
Huang ×3, Balboni ×2, the McGrew quote ×1. They are long-standing defects the revision failed to catch,
not defects it created. This matters for where the process gap is: the gap is that nothing ever audits
citations the session is not already touching (`AIW-170`).

## RIM — blocking, before any Zenodo version (`AIW-171`)

**Confirmed by me via Crossref:**
- **C1 chimera.** Manuscript: `Gignac & Zajenkowski (2024), Intelligence, 104, 101802`. That title
  ("Inconsistent Flynn effect patterns may be due to a decreasing positive manifold…") is
  **Oberleiter, Fries, Dejardin, Heller, Schaible, Vetter, et al. (2024), *Intelligence* 107, 101867**,
  DOI 10.1016/j.intell.2024.101867. The in-text claim (IQ up, *g* down) may instead match
  **Andrzejewski, Oberleiter, Vetter & Pietschnig (2024), *J. Intelligence* 12(12), 130**. Read the right
  one before re-citing — this citation is used in **§3.3 and §7.3**.
- **C2 chimera.** Manuscript: `Huang, C. (2024), Educational Psychology Review, 36(1)`. That title is
  **Vu, Scharmer, van Triest, van Atteveldt & Meeter (2024), *Educational Psychology* 44, 136–170**,
  DOI 10.1080/01443410.2024.2307960. ⚠ The agent reports the finding is **asymmetric in the direction that
  matters**: achievement→motivation β ≈ .18 vs motivation→achievement β ≈ .10. Cited twice (**§1, §3.4**).
- **C3 chimera.** Manuscript: `Balboni, Ferrandi & Naglieri (2021)`. That article is **single-authored by
  Robert J. Sternberg**, *J. Intelligence* 9(4), 58. Fixing it changes §3.4's dynamic-systems framing.

**Agent-reported, verify before fixing:**
- **C4 fabricated quotation, §2.1.** CHC as the "standard reference point" (McGrew, 2009, p. 1) — agent
  searched the full PDF and the phrase is absent; nearest is "key reference point," referring to Carroll 1993.
- **C5 source contradiction, §3.1 — the most serious.** "NFC correlates primarily with Gf, TIE primarily
  with Gc… (von Stumm & Ackerman, 2013)". Agent reports both correlate more strongly with **Gc**, and that
  the r ≈ .78–.87 figure is Woo et al. (2007). **This is the only concrete empirical illustration of the
  unity-of-motivation claim**, which is a headline abstract claim.
- **C6** Wechsler (1944) quote inexact — p. 3 reads "the **aggregate or** global capacity of **the
  individual**". **C7** Rosenthal (2002) is in the reference list but never cited.

**Internal contradictions introduced or left by the revision:**
- **§3.4 opening** still says "none, to my knowledge, has formalized the full recursive structure" while the
  new text three paragraphs later says "That work is done, it is formalized, and it is two decades old."
- **§8 closing** reinstates the causal absolute §6.3 was calibrated to remove ("measured in children who stop
  trying… a collective future diminished by every mind that was told it was not enough") — and claims
  *measurement* for what §6.3 now calls a prediction. Also the highest manifesto-register risk in the paper,
  positioned where an editor reads last.
- **§6.5** "hard predictions about the dynamics of a formal system" contradicts §7.4 ("not a fully specified
  formal model") and §3.4 (van der Maas et al. "supply functional forms that the present paper does not").
- **§3.4 Sternberg et al. (2021)** — "structurally identical to the recursive loop proposed here" misreports
  meta-intelligence (a control system choosing *among* approaches, not self-improvement) and needlessly
  destroys novelty.

**Surviving AI-tells the agent found in my own new prose** (this is the `prose-register.md` class, third
recurrence): §3.1 "the model should say so rather than let the notation imply otherwise"; §3.4 "the present
proposal must be positioned against them explicitly" (the revision *instruction* leaking into the prose);
§5.1 "and it should not be presented as though it could"; §6.3 "worth stating precisely, because it is easy
to state too strongly"; §7.3 "and both are declared here, before the data are inspected"; §7.4 "it would be
dishonest not to flag it."

**Verified clean** (so clean is distinguishable from unexamined): Flynn & Weiss Table 2 — every §7.3 figure
checked against the PDF, all exact, both quotes verbatim. Also confirmed as cited: van der Maas 2006;
Dickens & Flynn 2001; **Jussim & Harber 2005 (the new §6.3 characterization is a verbatim match)**;
Bratsberg & Rogeberg; Sundet; Wicherts; Pietschnig & Voracek; Hilger 2017/2020 and Schultz & Cole (the §7.1
rewrite reports them correctly); Ackerman & Heggestad (.08/.30); Nusbaum & Silvia; Brose; Schmiedek;
Heckman; Macnamara & Burgoyne; Wechsler 1940/1943; Oudeyer & Kaplan; Friston; Dörner & Güss; Pathak;
Canivez & Youngstrom; Edwards & DeYoung.

## Cosmology — blocking, MG's suspicion confirmed (`AIW-172`)

**CRITICAL:**
1. **IB1 (information impermeability) contradicts §8.2 and contradicts Raju (2022), which the paper cites in
   its own support.** §5.3 calls impermeability "rigorous… the property on which the unification of Section
   5.2 rests," while §8.2 endorses information returning in Hawking radiation. Repair exists in the
   literature (two-tier: semiclassically impermeable, non-perturbatively boundary-available) — see
   Bahiru, Belin, Papadodimas & Sárosi, *JHEP* 05 (2024) 261.
2. **The Bekenstein bound is misattributed throughout.** Bekenstein (1981) PRD 23, 287 gives
   S ≤ 2πkER/ħc — energy × radius, **not area**. The area law is 't Hooft (1993) / Susskind (1995).
   "Bekenstein saturation" is one of the three properties the whole unification rests on (§5.2, §5.6, §8.1,
   abstract).
3. **§5.6's particle-spectrum argument is self-refuting.** It derives an O(1)-bit boundary and then asks it
   to encode the Standard Model (≳60 states, ≥6 bits, area ≳ 25 ℓ_P²). As written the paper's own arithmetic
   predicts a two-particle universe.
4. **§5.6 vs §5.7 no-hair conflict.** §5.6 derives baryon/lepton-number conservation from boundary
   information; §5.7 identifies particles with (M, Q, J) no-hair boundaries — which is the standard argument
   that B and L are *not* fundamental. Nowhere for B, L, colour or weak isospin to live.
5. **The heat-death saturation mechanism is asserted, is wrong by ~12 orders of magnitude, and is
   half-retracted two paragraphs later.** BH entropy ~10¹⁰⁶–10¹¹⁰ vs horizon ~10¹²².

**Five more defective references** (same class as RIM): Rubio & Dunningham 2020 → arXiv:2007.04849 is
**Tsang, sole author**; Bisio/D'Ariano/**Tosini** Ann. Phys. 368 → that volume/pages is Bisio/D'Ariano/
**Perinotti**, "Quantum cellular automaton theory of light" (**I confirmed this one**); Konopka/Markopoulou/
**Smolin** PRD 77 → actually **Severini**; Rowland (2006) title is **invented**; Boyle & Turok PLB 849 is
**2024**, not 2022.

**Two silences a referee will name:** no mention of **DESI DR2** (favours w₀ > −1, wₐ < 0 — the Big Rip
branch is disfavoured though not excluded), and no mention of **Tolman's** entropy-accumulation objection,
which every cyclic cosmology must answer.

**Genuinely good news, and it is strategic:** the sweep found **no work connecting information causality or
Tsirelson's bound to holography or the Bekenstein bound** as of mid-2026. §6.5's proposed route is
**unclaimed territory** — the paper's best novelty claim, and a reason to move.

## Prospective research (`AIW-173`)

a. **Run the saturation-trigger automaton experiment** (§9.7's own resolution criterion) — Day&Night
   self-complementarity + Critters reversibility + a boundary entropy-export channel. Both outcomes are
   informative. Compute exists (the 4090 box). Highest value ÷ effort; converts Weak Point 7 into a result.
b. **Attempt the information-causality-from-bounded-encoding derivation** while the window is open. Push
   Jain/Gachechiladze/Miklin (PRL 133, 160201) polynomial machinery through a finite-capacity boundary
   channel; answer Oughton & Timpson's Shannon-dependence objection from von Neumann relative entropy.
   Success = CHSH ≤ 2√2 from capacity alone; instructive failure is itself publishable as a no-go.

Full cosmology working notes: `tmp/sb-hc4a-review-notes-fable.md` (agent artifact — move somewhere tracked
before `tmp/` is cleaned).
