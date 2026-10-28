<!-- Action: reference -->
<!-- Tracked-by: AIW-275, AIW-276, AIW-277, AIW-278, AIW-279, AIW-280, AIW-281, AIW-282, AIW-283, AIW-284 -->
# S334 — overall report (MoC7 aftermath), 2026-10-16

One-page view of everything this session produced. Status lives in `backlog.md`; open questions live in
`docs/pending-s334-mg-decisions.md` (31 items). Everything below is committed to private; nothing was pushed
public, sent, or published.

## Verdict
All five papers you asked for are drafted and reviewed, plus the prediction map for Mudrik's programme. Leads are
triaged and four reply drafts are waiting in Gmail. Nothing goes out until you decide the 31 items, starting with
the Table 1b falsifier.

## 1. MoC7 programme analysis (AIW-275)
- Full booklet downloaded: `docs/moc7/moc7-booklet-web-full.pdf` (+ `booklet.txt`).
- Every talk, keynote, workshop and poster scored 0–3 for FMT relevance: `docs/moc7/analysis-part1..6.md`.
- Consolidated, prioritised lead table: `docs/moc7/leads.md` (P0 / P1 / P2, plus the booklet inputs per paper).
- Threat found: **Sandberg #45** — M-ratio heteroscedasticity may make FMT §9's d′/M-ratio decoupling
  (r = −0.03) noise. Re-run with his normalisation before citing it again.

## 2. Leads, contacts, mail
**P0:** van der Vlag (Jülich, self-modelling reservoir — replied unprompted), Mudrik (prediction maps),
Vukovic (#120 UZH — your "last talk"), Eric Platon (promised repo contact).
**P1 (selection):** Negru (call request), Signorelli consensus paper, Kawakami (guarded recursion → answers the
circularity charge formally), van Loo, Yan (FMT as fifth formalised theory), Antonova, Martinez-Saito, Inzunza
(faithful functors), Murphy (lucid-onset caveat), Yu (FBTC, closest formal rival), Ludwig (chip no-go theorem).

- `contacts.md` updated: Yu and van der Vlag → Active, Chen reply recorded, Negru added (cfg 87bb1a6b).
- **Gmail drafts ready (minimal register):** Negru, van der Vlag, Yu, Chen. Check the From address is matthias@.
- Gmail/LinkedIn intake: `docs/moc7/gmail-intake.md`. Zenil DOI "conflict" was a false alarm (concept DOI).
- The SJÄLV QR resolves to the Zenodo FMT concept DOI, not matthiasgruber.com.

## 3. Papers (`drafts/papers-moc7/`, private)
| # | Paper | File | Words | Review state |
|---|---|---|---|---|
| A | Definitions are not settled (vs Kleiner) — **P0** | `definitions-not-settled.md` | 8,900 | 2 Fable referee rounds + 2 revisions; Fable: should pass at JCS |
| B | Deriving the FMT definition (2015 book) | `deriving-the-fmt-definition.md` (+ `fmt-2015-derivation-check.md`) | 7,958 | 1 review; every 2015 quote checked against the PDF |
| C | Minimal self / microphenomenology too late | `minimal-self.md` | 8,799 | 1 review; sharp refutation condition added |
| D | Robot plea (silent suffering) | `robot-consciousness-plea.md` | 5,741 | 1 review; includes substrate-independence deniers + non-human-like sufferers |
| E | Theory map (IIT, GNW, PP, HOT, RPT, AST…) | `theory-map-paper.md`, `theory-map-wiki.md`, `fmt-claims.json` (54 claims) | 9,906 + 1,887 | fairness review against each rival |
| F | Category-theory explainer (ML question) | `docs/papers-moc7/category-theory-explainer.md` | 5,708 | brief + 150-word answer card in §5; per your ruling CT stays small (D1–D3) |

Order used (your ruling): A → theory map → robot plea → minimal self → B.

**Open checks before any submission:**
- Definitions A: Kripke page (p.152, "Lecture III") needs a print copy; Casali 2013 PCI methods characterised from
  the abstract only (paywall). 8,900 words is close to the JCS 9k ceiling.
- The S324 journal pause still applies — drafts are venue-neutral until you lift it (decision 6).

## 4. Prediction map for Mudrik (AIW-276)
- `fmt-prediction-map-spec.md` + `fmt-prediction-map.json` (55 nodes, 84 edges) + centrality script.
- Platform identified: Negro, Elbaz, Fischer, Schreiber & Mudrik 2026; app at xk29y8.csb.app.
- Blocked on (a) your Table 1b ruling and (b) one demo-map export from a desktop browser (no browser on this Deck,
  CodeSandbox returns 403) to match their import schema.
- Caveat: centrality ranks E3 (lucid onset) highest, which is a signature prediction, not a principle.

## 5. Vukovic (AIW-277)
Retargeted from ETH to Vukovic (UZH LiRI, Multimodal Technology Group, LCP, CAPIRE, MOSAIC). Needs your answer on
what input she asked theories for (decision 25).

## 6. Cru, social, landing page
- **Crucible inbox ×3:** open-sourcing prep; registered-experiment primer with mandatory registration; the
  implementation-plan "necessary" wording + primer review.
- **CS-student primer** drafted: `drafts/contribute-primer/wiki-contribute-index.md`. Held private because it
  quotes unpublished CRU-70/CRU-78 results (disclosure freeze); gap list in `docs/moc7/contribute-primer-gaps.md`.
- **Infrastructure inbox:** `/moc7/` landing page to gain SJÄLV + contribute sections.
- **Social inbox:** all new persons + the Thompson post (needs your list of his CS errors and the forgotten
  speaker's name).
- **Ivoclar inbox (fyi):** LinkedIn messages from Anton Grones (DPO) and Simon — not touched here.

## 7. Knowledge fixes
- `fmt-2015-definitions.md`: recursive knowledge form introduced p.21, re-quoted p.22.
- `prediction-framing.md`: GNW allows sophisticated unconscious processing — "consistent with" only; don't use
  that line with the Mudrik group.
- `decisions.md`: S334 rulings (paper order, minimal self = basic ESM + sentience floor, CT small, Vukovic).

## 8. Details from the transcript check
Caught by re-reading the pre-compaction transcript; not all of these were in the first version of this report.
- **Category theory, public framing.** The CT brief found roadmap §7 to be decoration: two categories and a
  functor, no construction, no theorem. "Consciousness is a functor" proves too much, since a weather model has
  one too. Your MoC7 booklet abstract describes a different construction from the roadmap and promises a
  consciousness-detection criterion that exists nowhere. The brief recommended stochastic dynamical systems plus
  information theory as the main tool, and no more advertising of "category-theoretic formalisation in
  development" until δ gives a result. Your ruling covers the first part (CT small, D1–D3). You also ruled
  to stop advertising it until D1 has a result (decisions.md).
- **Venues proposed by the briefs, all on hold under the S324 pause:**
  - Definitions A: JCS (Fable: should pass) or PhiMiSci (deferred until JAIC). Synthese is borderline unless the
    criteria are shown to discriminate between existing work. NoC is out because Kleiner is an associate editor there.
  - Definitions B: PhiMiSci or Synthese.
  - Minimal self: JCS, then *Phenomenology and the Cognitive Sciences*. A possible empirical companion at NoC,
    with a co-author.
  - Robot plea: a pre-submission enquiry to *Nature Machine Intelligence*, with JAIC or *AI & Society* as fallbacks.
- **Honest limits the reviews left standing:**
  - Definitions B: the phenomenal claim rests on Principle 3 (closure), which the master paper calls "argued for
    rather than derived". Against Kleiner that leaves a standoff, not a win. Nothing in the derivation forces the
    *self* in self-modelling; Metzinger's selfless pure awareness is the counter-case.
  - Robot plea: "cheap" and "low-cost" in the asks have no cost evidence behind them. The drift toward closure
    rests on toy-scale FMT results, which the paper says.
  - Prediction map: your own fixed-lookup falsifier F6 and P1 rank low on centrality.
  - Robot plea conflict of interest: the crucible robot already has hand-set hunger, fear and pain, and closure is
    planned. The paper therefore discloses it (decision 14).
- **Sleep and the sentience floor.** Your sleep claim ("not unconscious while sleeping") contradicts the master's
  deep-NREM row ("mostly absent"). It works only through the capacity/process split. The minimal-self paper states
  "the floor persists through most of sleep" as your own view; decision 10 covers both papers.
- **Minimal-self paper:** Zahavi sits on the MoC7 advisory board, which matters for decision 12.
- **Housekeeping:**
  - The social repo had an old stash-pop conflict on a July terminal log that origin has since deleted. The log
    is backed up, social is fast-forwarded, and the stash still holds it.
  - aIware has a leftover stash from an earlier session; dropping it is your call (decision 31).

## 9. What I need from you
The 31 items in `docs/pending-s334-mg-decisions.md`, one at a time. Top five:
1. Table 1b closure falsifier (blocks the prediction map).
2. Sentience floor without an explicit self-model — stated position.
3. Lift the journal pause for Definitions A (JCS)?
4. Send the four Gmail drafts.
5. Primer disclosure of CRU-70/78.
