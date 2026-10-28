<!-- Action: await-user-decision -->
# RIM Platinum (v5) — final adversarial review before DOI deposit

Reviewed 2026-08-27 (WSL, Fable subagent). Target: `paper/intelligence/paper.md` at HEAD
(Platinum edition, post commits 0837bbf2 / 7e3d6fad / 4c3fd77a). Read in full (697 lines), diffed
against `de6d43f3` (the v4 published state), read against `.claude/knowledge/prose-register.md`,
and cross-checked against the four prior review records (`2026-08-24-rim-review.md`,
`2026-08-24-rim-repairs.md`, `2026-08-24-rim-rulings.md`, `2026-08-26-rim-fable-review.md`,
`2026-08-26-platinum-verification.md`) so that already-litigated findings are not re-raised.

**What was independently verified this pass (primary or full-text sources reached):**

- **Ritchie & Tucker-Drob (2018)** — full PDF read (utexas lab copy). Confirmed: 1.197 IQ pts/yr
  (control-prior design), 2.056 (policy change), 5.229 (cutoff); mean outcome age 63.48 for the
  control-prior design; outcome-age moderation −0.026 pts/yr (2.154 at age 18 → 0.485 at 83).
  **New fact the paper does not carry:** within the control-prior design the fluid-test effect is
  0.836 pts/yr with **p = .152 — not significant**; the significant signal is on composite tests
  (1.876). The policy-change design's fluid effect IS significant (2.272, p = .003, mean outcome
  age 47.9).
- **Melby-Lervåg et al. (2016)** — PMC full text. Nonverbal far transfer: 0.20 [0.11, 0.28]
  untreated / 0.05 [−0.02, 0.13] treated / −0.05 [−0.21, 0.11] delayed-treated. All three of the
  paper's numbers exact.
- **Ackerman & Heggestad (1997)** — Openness–Gf r = .08 vs Gc .30: confirmed (secondary
  full-text descriptions; consistent with the 08-26 review's independent confirmation).
- **Wicherts et al. (2004)** — five datasets (Dutch WAIS, DAT, RAKIT + reanalyses of Must et al.
  and Teasdale & Owen) = "five intelligence batteries from three countries": confirmed.
- Register density on the *new* prose measured per the register file's own prescription (added
  lines vs pre-rewrite baseline): see S7.

Everything else numeric rests on the S312/S313 verification records (Flynn & Weiss Table 2 read
from `literature/fulltext/FlynnWeiss2007.pdf`; Schweitzer, Oberleiter, Heckman, Macnamara,
Edwards & DeYoung, Vu, Ackerman 2018 all previously confirmed verbatim) — not re-derived here.

---

## BLOCKERS

### B1. Motivation is still typed as a component of the loop in the paper's own mouth — including inside the Abstract

The title thesis is "not a component but the allocation policy over the loop" (L111, L117:
"Motivation is not a component of the loop at all"). The surviving text contradicts it repeatedly,
and twice fatally:

- **L135:** "The recursive model therefore treats Motivation as a single component with two
  functional expressions" — four paragraphs after L117 denies it is a component at all. Same
  subsection.
- **Abstract, final sentence (L23):** "one of the three things being reciprocally caused has been
  the wrong kind of thing all along" — but the same abstract says "motivation is not a
  constituent of the loop at all." If it is reciprocally caused, it is a loop node.
- **§3.2 (L143–151):** the loop's four bullets give Motivation in-edges and out-edges as a peer
  node ("Motivation enhances both Knowledge and Performance"; "Knowledge and Performance enhance
  Motivation"). This is the unrevised v4 loop; a referee holds it against the title.
- Residue elsewhere: L43 "recursive three-component model"; L137 "The three components"; L157
  "recursive interaction of three components"; L273/275/289/402 "the M component"; L328 "an
  intervention on the Motivation component"; L371 "the Motivation component that drives"; L410
  "The Motivation component's primary contribution".

The theory itself does not need "not in the loop" — it needs "not a capacity." The model's own
dynamics (Matthew effect, self-efficacy, L151) require M to be causally updated by K and P, i.e.
to be a node. The claim that survives everything else in the paper is: *M is in the loop, but it
is not a magnitude — it is the policy that allocates the loop's time, and it is itself re-pointed
by the loop's outcomes.* One reconciliation passage saying exactly that (and a sweep of
"component" → "constituent" where M is meant, or an explicit licence for the loose usage) closes
the whole class. Without it, the paper's sharpest sentence ("not a component of the loop at all")
is contradicted by its own Abstract, its own model section, and ~10 other passages.

Related quantity-talk that the re-typing declares a category error (L117: "asking how much of it
someone has is close to a category error") but the paper goes on committing: L330 "A poor grade
reduces M", L345 "an intervention that boosts M", L398 "when motivation is low", predictions 1
and 6. Prediction 8 contains the translation (level → consistency/frequency of allocation); it is
never applied to these passages. One sentence stating the translation inoculates them all.

### B2. §3.4.1's separation from Kanfer & Ackerman is carried by the one thing the paper elsewhere lets the reader reject

**L193:** "The present proposal allocates something else: **offline simulation time in an explicit
self-model, across developmental time.**"

Two problems, each sufficient:

1. **It imports the disavowed architecture.** §3.4.2's closer (L219: "A reader who rejects it, or
   prefers another, can accept everything the recursive model claims and predicts"), §5.3
   (L283–287) and §7.4 (L451) all quarantine the Gruber-2026 explicit-self-model account as an
   optional conjecture. But L193 makes that architecture the *content of the separation* from the
   three occupants. A reader who exercises the offered rejection is left holding exactly the
   referee's sentence: "this is Kanfer & Ackerman's distal allocation, extended in timescale —
   i.e., PPIK," which the paper itself concedes is "closest" (L207).
2. **It misdescribes the paper's own construct.** Everywhere else, what the policy allocates is
   loop-engagement time, not offline simulation: the observatory schedule allocates *observation*
   nights (L119); Handlungsdrang allocates "action and exploration" (L121); schooling "points the
   allocation policy at material the learner would not have chosen" for "hours a day" (L309) —
   classroom hours are not offline simulation. Either the resource is the loop's time (and L193
   is wrong) or it is offline simulation (and §3.3's education derivation and the paper's central
   metaphor describe a different construct).

The verification record already contains the licensed fix: the S313 verification batch (Agent A)
established that the durable separations from K&A are (i) the developmental timescale, (ii)
re-typing the intelligence construct itself, and (iii) consequences for the measurement of the
allocated disposition — all three of which §3.4.1 *also* states (L195). Strike "offline simulation
time in an explicit self-model" and state the resource as the loop's iterations across
developmental time; the subsection then stands on ground the paper has actually secured.

### B3. "Knowledge is two things" is given two partitions that do not coincide — and the running process is claimed by three constituents

- **Abstract (L23) and §3.1 (L115)** announce the split as the *physical* structure/process
  boundary ("what is stored in structure and what runs as process"; the dead-brain criterion).
- **§4 (L229–231)**, which L115 promises as the payoff ("the reason to separate them appears in
  Section 4, where the two sides turn out to behave differently under intervention"), actually
  divides **factual vs operational** knowledge — and L115 itself places operational knowledge "on
  the first side" (stored in structure, running only when it works). So both of §4's knowledges
  sit on the structural side; §4 never shows "the two sides" (stored vs running) behaving
  differently under anything. The promised earning does not occur.
- Worse, the *running* side is claimed elsewhere by the other two constituents: L137 assigns "the
  capacity to construct a model and run it detached from present input" to **Performance and
  Motivation**; §6.1 (L305) scores model-construction inside measured **Gf**; §7.3 (L425) maps
  simulation-loaded subtests onto the generative process. If the explicit running process is
  Knowledge's second half AND Performance's construction skill AND what Motivation draws on, the
  typology has one process claimed three times, and a referee will ask which constituent owns it.

Fix direction: say explicitly that Knowledge divides along *content* (factual vs operational) and
that the structure/process boundary is a *mode* distinction that cross-cuts all three
constituents (stored disposition vs running exercise), with §7.3's subtest partition anchored on
the mode distinction — which is how §7.3 actually uses it. As written, the Abstract's second
headline claim ("Knowledge is not one constituent but two, divided by the physical boundary") is
not the claim the body defends.

### B4. The Abstract and §8 assert a "durable effect of schooling on fluid ability" that the cited design does not show

Verified against the R&TD primary this pass: in the control-prior-intelligence design — the one
the body quotes (1.197/yr, adult outcomes, L165) — the **fluid-test effect is 0.836 pts/yr,
p = .152, not statistically significant**; the design's significant signal is on composite tests
(1.876), and outcome-age moderation runs the effect down from 2.154 at age 18 to 0.485 at 83.
The body hedges ("at the lower end of that range" L165; "diminishes with age" L307) but never
discloses the non-significance; the **Abstract (L23: "the durable effect of schooling on fluid
ability") and §8 (L465: "Schooling moves fluid ability durably")** flatten the hedge into a claim
the quoted table contradicts at one lookup. This is the paper's own named failure mode (front and
back matter flattening what the body scoped).

Salvage exists: the **policy-change design** shows a significant fluid effect (2.272, p = .003)
at adult mean outcome age 47.9, with no age moderation. Either re-anchor the fluid claim there
(and say so), or restate the contrast the way §3.3 actually argues it — durable effect on
*measured intelligence* (composite) vs a WM-training far-transfer estimate that is nil against
treated controls and negative at follow-up — and keep "fluid" out of the abstract's version.
Also, small scoping error at L165: "designs that control prior intelligence … one to two points
per year" — the 1–2 range spans two designs, only one of which controls prior intelligence, and
1.197 is that design's overall estimate (mean outcome age 63.5), not an adult-subset estimate.

---

## SHOULD-FIX

- **S1 (L131 vs L408).** The unity claim's stated risk-bearer is "the aggregation contrast of
  prediction 9" — but prediction 9 (L412) as written contains no motivation instrument at all
  (imagery, absorption, matrices); prediction 7 (L408) self-describes as the unity claim's
  "principal support". Flagged in the 08-26 review, not repaired. Either add the motivation
  version of the matched-k modality contrast to prediction 7's design, or repoint L131 at 7.
- **S2 (Abstract L23, sentence 1).** "Every major model of intelligence leaves motivation out of
  its formal structure" — §3.4.2 (L207) concedes PPIK "explicitly models how personality traits
  and interests direct the Gf-to-Gc investment process". §1 (L35) carries the PPIK hedge; the
  Abstract does not. Ackerman is the chief interlocutor and a plausible J. Intelligence referee.
- **S3 ("century-long resistance to trait measurement" — Abstract L23, L161, L465).** Asserted,
  never documented: the cited instrument record starts 1982 (NFC), and the field's own
  self-description is "genuinely distinct constructs" (the paper says so at L123), not "failed
  trait measurement". Either temper to what §3.1 actually shows (a family of moderately
  correlated, differently-loading instruments) or cite a historical source for the century.
- **S4 (Wittmann & Hattrup mediation, L121 and L207).** Still unverified after three passes
  (primary unreachable; re-attempted this pass, still unreachable — secondaries confirm the
  intelligence→DDM paths but not risk-taking *mediation*). Also L207 says the finding "provid[es]
  empirical evidence for the exploration-exploitation dynamic that the recursive loop predicts" —
  past "consistent with". Wittmann reads this paper; one email settles it, or soften both
  passages to what the secondaries support.
- **S5 (§8 factive "because", L461–465).** The four payoff sentences state the model's
  explanations as established fact ("Motivation resisted trait measurement for a century because
  there was no trait there to find"; "Schooling moves fluid ability durably … because one
  re-points the schedule") where the body offers them as the policy reading's predictions with
  stated defeaters. Convert to the body's conditional register — §8's next paragraph (the
  defeaters) already shows the paper knows how.
- **S6 (Abstract length).** 403 words, single paragraph; MDPI *Journal of Intelligence* asks
  ~200 max. It was 348 at v4 and flagged then; Platinum grew it. For a Zenodo deposit it is
  merely heavy; for the named target journal it is a desk-level irritant.
- **S7 (register — new prose).** Measured per the register file's own prescription (added lines
  vs the v4 baseline, same regex both sides): the Platinum additions run **7.3 antithesis
  constructions per 1,000 words against the 5.25 baseline they join** ("rather than" 30× in
  ~6,750 added words). Many carry real oppositions (type contrasts are the argument) — but the
  file's rule is that new-denser-than-joined is doing rhythm. Named instances to cut or recast:
  - L191 "Ackerman is this paper's chief interlocutor throughout" — self-narration of the
    document's own moves, the exact class MG struck twice this session.
  - L195 "The vacancy this paper fills is narrower than 'psychometrics'." — the paper staging
    its own contribution.
  - L163 "stops being an excuse and becomes a theorem" — "theorem" overclaims in a paper that
    states it has no formal model (L441); "a consequence of the re-typing" is the honest word.
  - L159 "one consequence seen four times" / L465 "The re-typing pays four times over" — cadence
    pair; keep at most one.
- **S8 (register — old prose now in a deposit-final).** L265 "This is where the comparison
  becomes interesting." (narrating the reader's route); L332 "two constraints have to be carried,
  not passed over" (advertising the paper's own care — the banned class by name); L217 "the
  combination this paper assembles"; L322 "A caveat is necessary here:"; L207 sentence-initial
  "Notably,". All pre-date Platinum; all are one-line fixes.

## OPTIONAL

- L71 "As early as 1943" while §7.5 and the references credit Wechsler (1940) as the earlier
  statement — say 1940 at L71 or drop "as early as".
- L37 "It is an impressive edifice." — empty-praise copula (has a rhetorical function; author's
  call).
- L320 "compound interest machine" paragraph — pop-sci register in a journal paper; effective,
  but it is the passage a hostile referee quotes to call the paper popular.
- Heavy mid-paragraph bolding in §3 (six+ bold clauses, e.g. L119, L125, L169, L193) — reads as
  staging; MDPI copyediting may strip it anyway.
- L177 "incompatible with models that treat intelligence as a primarily biological trait" —
  "difficult to reconcile with" is the defensible strength.
- L265 "a striking resemblance" — cliché intensifier.
- Carried-over unverified anchors (known, listed in the 08-26 review, still open): Wittmann
  (1988) E/N demonstration (prediction 8's methodological model); von Stumm & Ackerman (2013)
  r ≈ .30 / range 0–.58 (prediction 7's disconfirmation anchor); Dignath & Büttner (2008)
  follow-up claim (prediction 4); Woo et al. (2007) .87 endpoint. Note also that the
  M→K→Performance anchor now rests on **Wittmann (2002)**, an unpublished conference paper — 
  legitimate, but referee-unverifiable except through Wittmann himself; make sure MG holds the
  document.

---

## CLEAN — checked and found sound (negative results)

- **Ruling compliance is clean across the board.** Price-not-barrier holds everywhere including
  the two previously-flagged §5.3/§6.1 sentences (now cost-form, L285, L303); no mirror neurons;
  the g-sense/author-sense split is explicit (L109); convergences are "consistent with"
  throughout §7.1 and §3.4.2 (sole drift: the Hattrup sentence, S4); recursion appears as
  fit-window advantage with stated defeaters, never necessity.
- **§2.7 handles all four rulings-sensitive sources exactly as ruled**: Meehl is cited for
  non-cumulativeness only, with the open-concepts defense stated in the same paragraph (L95);
  van der Maas is "could predict while referring to nothing of the kind its name suggests" with
  the pp. 855–856 quote and the explicit "alternative, not a refutation" (L99); Eronen &
  Bringmann is "unknown validity, never known invalidity" with their own anti-hopelessness
  sentence quoted (L97); the Salthouse exchange keeps Schaie's and the Betula rebuttals separate
  (L101).
- **The §3.3 education/WM-training contrast does what it was ordered to do**: the confound is
  argued, not asserted — the untreated-control g = 0.20 that "would beat a year of schooling" is
  stated, the no-shared-ruler point is made, and the comparison is rebuilt on the two things that
  survive (treated-control isolation; durability) (L165–169). The 1.197 adult figure is quoted.
  All effect sizes verified exact against both primaries this pass. The residual defect is the
  fluid-specific flattening in Abstract/§8 (B4), not the body's argument.
- **§6.3–6.4 is honest against its own interest**: Jussim & Harber's anti-compounding conclusion
  is stated at full strength and explicitly flagged as "in direct tension with the compounding
  prediction" (L332), with the grading pathway separated rather than borrowing expectancy
  support (L334). No straw-manning found anywhere in §7.
- **§7.3's disconfirmation discipline held**: the American record is declared incapable of
  testing limb 1 because the partition was read off it (L425, L437); Coding's exclusion is
  stated with its cost (L418); the invariance constraint is carried (L435).
- **Prediction 7's defeater is real and quantified** (r ≥ .50 required; r ≈ .30 disconfirms,
  L408), prediction 5 is operationalized with a positive disconfirmer (L402), and the Abstract's
  two defeaters match the body's exactly.
- **Citation hygiene**: every number I could independently reach was exact (R&TD, Melby-Lervåg
  ×3, A&H, Wicherts), consistent with the S312/S313 verification records for the rest.

---

## Verdict

**Do not deposit as-is.** The empirical spine, the rulings compliance, and the disconfirmation
apparatus are in genuinely good shape — but the re-typing that gives the Platinum edition its
title is contradicted by the paper's own Abstract, model section, and a dozen surviving
"component" passages (B1); the paper's defense against its nearest neighbours rests on a phrase
its own separability clauses disown (B2); the second headline re-typing (Knowledge-as-two) does
not survive its own Section 4 (B3); and the Abstract asserts a fluid-ability result its cited
design fails to show at p = .152 (B4). All four are wording-level repairs — none requires new
evidence or new structure — but all four sit in the sentences a referee reads first.
