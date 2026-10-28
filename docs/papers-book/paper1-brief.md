# Paper 1 brief — the core article distilled from "No Outside" (AIW-289)

**Status:** brief + outline. No paper prose yet. Prepared S337 (2026-10-18, WSL) from `drafts/monograph-limits/no-outside-draft-v0.6.md`
Ch 1, 5, 6, 15 and the architecture (`00-architecture.md` §1). MG rulings this paper must respect: `docs/decisions.md`
2026-10-18 S335/S336/S337 (holes 1–7, D1–D3, M1–M8; the outside-the-universe view is not a perspective; core =
two unconditional limits, capacity/irreducibility/incompleteness world-conditional).
**Companion files:** prior art `docs/papers-book/prior-art-paper1.md`, venues `docs/papers-book/venues-paper1.md`
(both from S337 research agents; read before drafting), paper 3 assessment `docs/papers-book/paper3-assessment.md`.

## 0. Thesis

**One sentence:** the limits on any description held by a proper part of what it describes can be stated without
claiming a view from outside, because they are not positive truths about all perspectives — they are refutations,
and refutations, unlike positive claims, travel between perspectives without one.

**The problem it solves (the paper's hook):** every limitative thesis about thought or description ("no view from
nowhere", "no God's-eye view", "the limits of thought") seems to be stated from the standpoint it denies. Priest
turns this into contradictions at the limits (inclosure) and accepts them; Nagel and Putnam leave it as a tension;
the relativist self-refutation literature uses it as an objection. The book's answer is a third option that keeps
classical consistency: the limit claims are impossibility claims whose support is that their negations contradict
input every claimant already admits (being embedded, being smaller than the whole, having a frame). So the thesis
"there is no outside" splits: as a refutation it travels; as a positive picture it is one more claim held from inside.

## 1. The argument in five steps (source chapters)

1. **Setup (Ch 5.1).** A describer is a proper part of a whole; it holds descriptions as content within a frame and
   admits some input. A description is complete if, with procedures the part can run, it fixes every fact it claims.
2. **Two unconditional limits (Ch 5.1, 15).** (L1) No perspective holds its own current generation, as a whole, as
   content — the holder would need a further holder (regress; Ch 4.5). (L2) No part can certify its own description
   of the whole complete — the check either holds the remainder (impossible) or proves from admitted input, which
   shows agreement with the input and never that no input is missing. Neither uses incompressibility, irreducibility
   or arithmetic; both hold in a small, simple world.
3. **Three conditional limits, conditions attached (Ch 5.2–5.4).** Capacity (Kolmogorov/Chaitin counting; holds where
   the whole is incompressible beyond the part's capacity); irreducibility (Wolfram/Turing; holds where a describer
   does irreducible work; the finite describer hands back to capacity); incompleteness (Gödel; consistent, effectively
   axiomatized, enough arithmetic). Common form: **the generator can appear in what it generates, but not completely**
   (Gödel's arithmetization represents the proof relation exactly; what fails is complete + consistent appearance).
   Short aside: why the Lucas–Penrose move fails on these terms (Ch 5.5) — footnote or one paragraph.
4. **Falsity without truth (Ch 6).** Positive match-to-world needs a comparison of model and world from a position
   that is not a model; none exists (every comparison is model with model). Falsity needs only a system and its own
   admitted input, both inside: one exhibited contradiction, checkable by anyone with access to the claims and the
   input, and inherited by every successor that keeps the input (Russell → every later set theory; Mersenne 2^67−1 →
   Cole). Escape by refusing the input is always available and is itself a checkable fact (the patch move). Condition:
   reaches perspectives that treat contradiction as failure. Relation to Popper: the logical half is his; what is
   added is the location of what is unavailable (truth as match, not positive verdicts as such), the generality to any
   reference system, and inheritance.
5. **The limits as refutations (Ch 15 "The limits as refutations").** Each limit is an impossibility claim; its
   negation, asserted by any perspective, contradicts that perspective's own admitted input (counting for capacity,
   running-behind for irreducibility, the regress for L1, the remainder/proof dilemma for L2). So the limits reach
   every perspective that distinguishes anything (a perspective with no frame distinguishes nothing; the
   outside-the-universe "view" draws no distinctions and is not a perspective — S336 ruling) as a refutation it can
   check for itself. They carry a refutation's resistance, not immunity. Only an empty chair is undefeated.

## 2. What goes in, what stays out

**In:** steps 1–5; the reading limit (no formalism certifies its own ontological reading, Ch 1) as the first worked
example of the pattern, briefly; Priest/Nagel/Putnam/self-refutation positioning; objections.
**Out (deliberately):** Ch 2–3 (number ladder, why mathematics works), Ch 7 felt logical necessity (a proposal, MG hole
7), Ch 8 cuts (one sentence at most), Ch 9–13 physics, Ch 14 worm on the disk (→ paper 3), FMT/SB-HC4A architecture
beyond citations. The paper must not need FMT to be true; the 2015 reference-system account of knowledge is cited as
the source of the framing, and the argument must run on "reference system = model" alone.
**Open choice (Q-A below):** the falsity *gradient* (Ch 6 "A gradient": resistance to reversal scales with conversion
cost; continental drift, H. pylori, geocentrism; stated falsifiers) is a separate, empirical claim about the history
of science. It strengthens nothing in steps 1–5 and costs ~1,500 words.

## 3. Outline (target 8,000–9,000 words incl. references; adjust to venue)

1. Introduction — the self-application problem for limitative theses (~900)
2. Embedded describers: frame, content, admitted input, completeness (~700)
3. Two limits without conditions (~1,200)
4. Three limits with conditions, and their common form (~1,500)
5. Falsity without truth (~1,500)
6. The limits as refutations (~1,300)
7. Neighbours: Priest's inclosure, Nagel/Moore/Putnam, Popper, Wolpert/Breuer/Lawvere–Yanofsky (~900; exact set from
   the prior-art report)
8. Objections and replies (~900): admitted input is chosen (Popper's swamp — shared swamp); a perspective that denies
   being embedded; paraconsistent perspectives; finite describers and Turing; "is this just Popper?"
9. Conclusion (~300)

## 4. Open questions for MG (ask one at a time; recommended first)

- **Q-A gradient — RULED S337 (MG): left out of paper 1; candidate short paper of its own later.**
- **Q-B venue → deferred to the joint re-assessment `AIW-292` (MG S337).** Agent shortlist (`venues-paper1.md`):
  Philosophia Mathematica, Logique et Analyse, Kriterion (8k cap incl. refs, waivable APC). Caveat: after the prior-art
  repositioning the paper is epistemology more than philosophy of mathematics, so Erkenntnis / Philosophy of Science
  (9k cap, explicit preprint clause) deserve a second look there. Draft venue-neutral at ≤9k incl. references.
- **Q-C — RULED S337 (MG): minimal, ≤5 self-citations**, only where the framing comes from them; argument runs without
  FMT being true. Anonymised venues need self-citations in third person.
- **Q-D title:** working options — "Limits Without an Outside: Why the Limits of Embedded Description Travel as
  Refutations" / "Falsity Without Truth and the Limits of Embedded Description" / "No Outside".

## 4b. Prior-art verdict (S337, `prior-art-paper1.md`) — repositions the paper

- **Anticipated:** L1 (Ryle 1949 "systematic elusiveness"; Popper 1950; MacKay 1960; Breuer 1995), L2 (Albert's
  Münchhausen trilemma; Grim 1991; Wolpert 2008), the generator principle (Lawvere 1969 / Yanofsky 2003; Priest's
  inclosure; Szangolies 2018 applies Lawvere to embedded observers), falsity asymmetry core (Popper 1959, Miller 1994),
  description/instance (endophysics: Svozil, Rössler; Nagel 1986).
- **Looks new:** the unconditional/world-conditional two-tier split; **limits that survive self-application by travelling
  as refutations** (neighbours: Bartley 1962 pancritical rationalism, Apel's performative contradiction; opponents Moore
  1997, Priest); the inheritance formulation as an answer to Duhem–Quine.
- ⇒ **Position:** the limits are established; the article is about what they license epistemically: the taxonomy, the
  self-application argument, falsity-without-truth against Duhem–Quine.
- **Fixes the draft must carry:** inconsistency is semi-decidable for first-order theories ("detectable, then
  permanent", not "decidable"); the exemption belongs to dialetheists, not to paraconsistent logics generally; check
  whether L1 has Lawvere form, and say so either way.

## 5. Risks a referee will press

- Prior art: if Wolpert (2008) or Breuer (1995) already prove L1/L2 for physical inference devices, the paper's
  novelty is the refutation reading (step 5), not the limits — the prior-art report decides how to state this.
- "Admitted input" carries the weight in steps 4–5; it must be defined in §2, not borrowed from the book's narrative.
- The regress argument for L1 needs one precise formulation (frame vs content), or it reads as metaphor.
- Paraconsistency: the condition must be stated as a scope condition, not dismissed.
