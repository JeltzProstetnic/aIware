<!-- Action: act -->
<!-- Tracked-by: AIW-241 -->
# RIM — Fable review, S312 (2026-08-26)

**Four Fable agents: §1–3, §4–6, §7–8 + Abstract, and a whole-paper cross-section + citation audit.**
Each was handed the non-litigable rulings (price-never-barrier on both axes; closure/recursion is an advantage
in a fit window, never a necessity, with the budget-relative exception; the *g*-loaded sense is not the
author's sense; convergence is "consistent with"; no mirror neurons), the prose-register ban list, and the
S311 verification discipline — *seven of nine deep findings in the FMT review were refuted on adversarial
check, the failure mode being a verbatim-accurate, context-false quotation.* Every agent was required to
state what it checked before a finding counted.

**Why this paper is being reviewed now:** the published Zenodo v3 (`10.5281/zenodo.21841307`, 2026-08-07) is
44 pp / 16,900 words. The committed source and PDF are 45 pp / 17,836 words as of `b86e0a50` (2026-08-24).
**The publication is one revision behind the repository.** `check_md_pdf_drift.py --paper rim` is clean, so
`.md`, `.tex` and PDF agree with each other — only the deposit is stale.

---

## ⭐ THE HEADLINE: nine findings were reached INDEPENDENTLY by two agents each

Convergence between agents that could not see each other's work is the strongest signal this review
produced, and it is what separates these from the single-agent findings below. **Every item in this table
was found twice.**

| what | found by | status |
|---|---|---|
| **von Stumm et al. (2011) "develop … over time"** at `:153` — the paper's own `:333` says the source is "drawn largely from concurrent student samples" and "carries no childhood-to-adult design" | §1–3 **and** cross-section | **BLOCKER** — the refutation is in the paper's own prediction section |
| **`:317` "early IQ (which primarily captures Performance) is a poor predictor of adult intellectual achievement"** — uncited, contrary to the longitudinal record, and in tension with Prediction 1's own "beyond what childhood IQ predicts" | §7–8 **and** cross-section | **BLOCKER** — named by both as the likeliest desk-rejection trigger |
| **`:195` "What remains uniquely human … is the combination of intrinsic motivation and operational knowledge"** — §5.1 `:217` states that "the usual form of the claim, that artificial systems have no motivation at all, **is false**" | §4–6 **and** cross-section | **BLOCKER** — a barrier claim the paper retracts six paragraphs later |
| **Wittmann & Süß (1999) cited for a motivational pathway** at `:157` | §1–3 **and** cross-section | **BLOCKER, unverified — needs MG.** See below. |
| **Abstract `:23` "static trait"** — the body only ever claims "relatively stable" (`:137`) and "primarily stable" (`:139`); §2.2 credits investment theory as "dynamic, developmental" | §1–3 **and** §7–8 | SHOULD-FIX — the Abstract strawmans a position the body states carefully |
| **`:109` hangs the unity claim on Prediction 9; `:347` hangs it on Prediction 7** — and Prediction 9 as written contains no motivation instrument at all | §1–3 **and** cross-section | SHOULD-FIX |
| **`:151` Dweck "shows … actual cognitive development"** — §6.1 `:253` reports *d* = 0.05, non-significant after publication-bias correction | §1–3 **and** cross-section | SHOULD-FIX |
| **`:61` "what he called 'investment traits'"** — the label is Ackerman's (1996), not Cattell's; Cattell supplied the investment *theory* | §1–3 **and** cross-section | SHOULD-FIX — misquoting the field's founder on his own vocabulary |
| **`:213` "7 ± 2 chunks (Miller, 1956)"** — modern working-memory consensus is ~4 (Cowan, 2001); Miller's figure is immediate memory span | §4–6 **and** cross-section | SHOULD-FIX — a free hit for a *Journal of Intelligence* referee |

---

## 🔴 THE ONE THAT NEEDS MG, AND IT CANNOT BE SETTLED FROM THIS MACHINE

**`:157` — Wittmann & Süß (1999).** The paper says the chapter "demonstrated empirically that **motivation's
effect** on complex performance is largely indirect — mediated through knowledge", with "motivational
variables contributing primarily via knowledge acquisition", and calls this "precisely the M → K →
Performance pathway that the recursive model formalizes." **It is the flagship empirical anchor for the
paper's central claim.**

Both agents tried to reach the primary and neither could — it is a paywalled APA book chapter. What they
established between them:

- The **~50% variance figure is corroborated** (a secondary reports 51% of variance in the complex planning aggregate).
- **Knowledge-as-strongest-direct-predictor is corroborated** by every reachable description.
- ⛔ **No reachable source mentions motivational variables in the path model.** The chapter's own title names
  working memory, intelligence, knowledge and complex problem solving. Stadler et al. (2019, *J. Intelligence*)
  and Süß & Kretzschmar (2018, *Frontiers*) both discuss the chapter in detail; neither mentions motivation.

⇒ **The suspicion is that an ability → knowledge → performance result has been recast as motivation →
knowledge → performance** — the exact "toward more support" direction every defect in the FMT audit failed in.
**Neither agent claims this as confirmed, and it must not be written up as confirmed.**

**MG has direct contact with Wittmann** (he is credited in the Acknowledgments for the measurement-asymmetry
insight). **One email settles it.** If the motivational pathway is not in the chapter, the fallback is either
the rescoped ability-mediation form or, if the claim actually rests on Wittmann's unpublished materials,
a personal-communication citation. ⚠ **Wittmann will read this paper**, which raises the cost of getting it
wrong well above the usual.

---

## 🔴 REMAINING BLOCKERS (single-agent, but checked)

**`:235` (§5.3) — "the conjecture is that motivation of the kind the loop needs *cannot* be supplied as a
module bolted to a system that lacks one."** A capability-barrier claim in the prohibited form. The section
is otherwise well-disciplined — explicitly quarantined, with a refutation condition at `:237` and "the rest
of this paper does not require it" — and `:225` shows the paper knows the licensed form ("not a claim about
what machines can never do"). Hedging as *conjecture* changes the claim's status, not its form.
**Repair:** "…is not economically supplied as a module bolted to a system that lacks one — the expectation
is that any bolt-on route pays a cost the self-model route does not, not that no such route exists."

**`:397` (Conclusion) — "one that cannot explain the self-reinforcing dynamics of intellectual development."**
§3.4 concedes the opposite in its most careful passage: van der Maas mutualism and Dickens–Flynn *are*
motivation-free positive-feedback accounts, `:165` says "That work is done, it is formalized, and it is two
decades old", and `:167` says the Matthew effect and Gf–Gc divergence "are accommodated by the mutualism and
multiplier accounts as well; they are not what distinguishes it." §3.3 `:137` hedges to "have difficulty
explaining." **The Conclusion flattens the concession the body worked hardest to earn.**

---

## The pattern worth naming: the Abstract and Conclusion flatten what the body scoped

Three separate findings are the same defect. `:397` on explanatory impossibility (above); `:397`/`:23` on AI
("leaves the field unable to account for" / "without an account of", where §5.2 `:225` concedes a purely
architectural account "predicts it equally well" and `:385` calls the paper's own position "a bet and not a
result"); `:23` "static trait". **In each case the body is honest and the front and back matter are not.**
This is the same class that shipped in FMT v14 and was repaired in v15 — worth a standing pre-publish check:
*for every substantive claim in the Abstract and Conclusion, name the section that earns it.*

---

## SHOULD-FIX, by area

**Claims about current AI that a 2026 reader falsifies from experience** (§5.1, all three flagged by the §4–6 agent):
- `:213` "LLMs process millions of tokens per second" — true of aggregate fleet or training throughput, not of
  one instance against one human, which is the comparison the sentence sets up. The sentence opens with the
  defensible "orders of magnitude faster", so the number does no necessary work. **Cut it.**
- `:215` "chain-of-thought prompting and verification loops … externally imposed scaffolds" — names only
  prompt-time mechanisms, while for the o1/o3-class systems named in the same paragraph self-verification is
  trained into the policy and fires unprompted. The paper's considered position (`:227`) is about *origin of
  the drive*, not mechanism, and is rescuable in its own terms.
- `:219`/`:223` "Between queries they do nothing" / "capability is static across sessions" — falsified at
  product level by cross-session memory and scheduled agents. `:229` already accommodates these as
  scaffolding, but the qualifier arrives two paragraphs after the categorical claims, and the categorical
  sentences are what gets quoted. **Sequencing defect, not a substantive error.**

**Internal-consistency items:**
- `:185` "Factual knowledge is additive: learning a new fact adds one fact to the store" — the paper's own
  chess example at `:267` has a store of positions multiplying effective processing. Repair by scoping
  factual knowledge to within-domain scaffolding rather than denying it.
- `:253` vs `:287` — §6.1 prices a willingness-change at near-zero to reconcile the mindset null, while §6.4
  and Prediction 6 have motivation-side changes compounding. The paper has the discriminator material at
  `:279` (a "repeated, explicit, institutionally sanctioned signal" vs one-shot) but never applies it here.
  **A reviewer will run Prediction 6 backwards into Macnamara.**
- `:105` calls Motivation "the recursive loop's multiplier" while `:23`/`:43`/`:185`/`:251` reserve
  *multiplier* for operational knowledge, and `:315` calls operational knowledge "the rate-limiting factor" —
  three labels, two components, one definite article. A multiplier is a gain term; a rate limiter is a
  bottleneck. **Pick one vocabulary.**
- `:391` dates Wechsler's call to 1940 while §2.4 `:71` says "As early as 1943" and never cites the 1940
  paper. Both entries are correct in the reference list; the prose disagrees with itself. The better repair
  fixes §2.4 upward, since the 1940 abstract is real and strengthens the point.
- `:391` "has not been systematically examined **until now**" — contradicted by the paper's own §2.6, which
  cites Ackerman (2018) making the suppression-of-motivational-variance argument and says the circularity is
  "rarely noted". **"Until now" invites the referee to name the counterexample the paper itself cited.**
- `:401` extends the compounding-cost claim to "hiring practices, and social institutions" — earned by no
  section; §6 and §7's measurements are exclusively educational, and §6.5 `:299` explicitly refuses this kind
  of extension even for ability tracking.
- `:407` Acknowledgments — "All theoretical content, arguments, and conclusions are solely the author's own"
  is contradicted two sentences earlier, where a specific theoretical insight carrying Prediction 7 and an
  Abstract clause is credited to Wittmann. ⚠ The AI-use declaration ("editorial assistance and manuscript
  formatting") may also understate what the project's own records show; **MG's call, and it must match
  whatever the target venue requires.**
- `:263` "should dominate real-world outcomes, and it does" — flat and uncited, sitting in the blast radius of
  the Schmidt–Hunter tradition. The paper already has citable support at `:157` and `:267`; only the
  flatness is the defect.
- `:339` Prediction 4's compounding claim cites Dignath & Büttner (2008), a meta of post-test SRL-training
  effects. **Unverified** — no indication it compared long vs short follow-up, and "this" refers to the
  compounding claim.

**Prose register** — the paper is clean on the phrase list (zero hits for "load-bearing", "bite", "worth
noting", "importantly", "crucially", empty superlatives). The residue is throat-clearing and
self-narration: `:205` "remarkably clean test case"; `:249` "This is not a feel-good platitude."; `:253`
"This claim requires more argument, but the evidence is strong." (asserts strength before showing evidence);
`:259` "This claim deserves elaboration, because…"; `:265` "To put it bluntly:"; `:157` "Notably,". One
register defect is more serious: **`:345` "A reviewer might reasonably ask:"** — addressing peer review from
inside the manuscript, the flagged class. Repair: "The obvious objection:".

---

## ✅ CONFIRMED CLEAN AGAINST PRIMARIES — do not re-litigate

The cross-section agent reached primaries for fifteen characterizations and **twelve confirmed exactly**.
This paper's citation hygiene is materially better than FMT's was at the same stage, and that is worth
recording so a future review does not redo the work:

**Heckman (2006)** — read from the Science PDF, p. 1901, verbatim: "the Perry treatment children had higher
achievement test scores than the control children **because they were more motivated to learn**"; IQ "no
higher than the control group by age 10"; the age-40 outcome list matches item for item.
**Macnamara & Burgoyne (2023)** — *d̄* = 0.05, CI [0.02, 0.09], non-significant after publication-bias
correction, financial-incentive moderator: all verbatim.
**Schweitzer et al. (2025)** — NFC–TIE *r* = .78–.87; NFC-Gf .19 vs TIE-Gf .12 (*p* = .045); NFC-Gc .24 vs
TIE-Gc .35 (*p* = .006): exact, including the significance claims.
**Ackerman (2018)** — the `:157` quotation is verbatim in the PMC full text.
**Vu et al. (2024)** — β achievement→motivation .176 vs motivation→achievement .096; "about twice" matches.
**Oberleiter et al. (2024)** — N = 1267, six measurement-invariant subscales, ΔR² −.037 to −.066, *d* 0.18–1.24: exact.
**Ackerman & Heggestad (1997)** — Openness–Gf *r* = .08 vs Gc .30: confirmed.
**Edwards & DeYoung (2026)** — NLSY79/97, sibling within-family controls, "30–57% of *g*'s importance": confirmed.
Also confirmed: **Wechsler (1943)** quotation; **Wicherts et al. (2004)**; **Brose et al. (2010)**;
**Flynn & Weiss (2007)**; **Chase & Simon** ("all but disappears" correctly hedges the Gobet–Simon residual);
**Bratsberg & Rogeberg (2018)**, **Sundet et al. (2004)**, **Pietschnig & Voracek (2015)** rates.

**Ruling compliance is clean.** §5 is consistently price-not-barrier at `:225`; the recursion-necessity
conjecture is firewalled and declared refutable in §5.3; convergence is "consistent with" throughout
(`:145`, `:153`, `:321`, `:323`); no mirror neurons anywhere; the *g*-sense/author-sense distinction is
managed everywhere except the two blockers above. §7's objections are stated at full strength — **no
straw-manned objection was found**, which is the check that matters most in a Discussion.

**Arithmetic re-run and correct:** §7.3's 1947–48 to 2001.75 = 54.25 years; five Performance subtests;
18.00/15.90/21.50 internally consistent; Coding's exclusion stated with its cost. All nine §7.2 predictions
cross-reference their body sections consistently; the six-vs-two source count in Prediction 7 enumerates
correctly; the Abstract's "symmetric aggregation … would refute it" matches Prediction 7's *r* ≥ .50 / *r* ≈
.30 disconfirmation criterion exactly.

---

## Still unverified — worth closing before deposit

| claim | where | why it matters |
|---|---|---|
| Wittmann & Süß (1999) motivational pathway | `:157` | **the flagship empirical anchor** — MG can settle by email |
| von Stumm & Ackerman (2013) *r* ≈ .30, range 0–.58 | `:345`/`:347` | Prediction 7's disconfirmation criterion is anchored on it |
| Wittmann (1988) Extraversion/Neuroticism demonstration | `:349` | Handbook chapter unreachable |
| Dignath & Büttner (2008) long- vs short-follow-up | `:339` | Prediction 4's compounding support |
| Edwards & DeYoung "did not replicate cleanly across cohorts" | `:319` | not in the reconstructed abstract; low risk |

---

## What this review did NOT cover

No agent was scoped to the `.tex` mirror or to a rebuild. `check_md_pdf_drift.py --paper rim` reports
`OK — paper.md and rim-paper.pdf agree on prose`, and a test build reproduces the committed PDF exactly
(45 pp / 17,836 words, zero `???`), so the mirror is currently sound — **but every repair folded in from this
review has to be made twice**, in `paper/intelligence/paper.md` and in the hand-maintained
`paper/intelligence/paper.tex`, or it never reaches the PDF.
