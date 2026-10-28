# AIW-295 — Breuer (1995) premise check against paper 1, draft 3

Date: 2026-10-18 · Target: `drafts/papers-book/paper1-draft.md` (draft 3) · Source: Breuer, T. (1995), "The Impossibility of Accurate State Self-Measurements", *Philosophy of Science* 62(2):197–214, doi:10.1086/289852 (JSTOR stable 188430).

**Result in one line:** the 1995 full text is not legally open anywhere I could reach, so **no page-numbered quote from the body could be taken**. The paper's headline statement of Breuer matches his own abstract word for word. Its more specific claims (the premise, "uses no counting", "sets the dynamics aside") can be checked only against secondary restatements, and one of them ("sets the dynamics aside") looks overstated.

---

## 1. Retrieval log (legal routes only, 16 attempts)

| # | Route | Result |
|---|---|---|
| 1 | Unpaywall `api.unpaywall.org/v2/10.1086/289852` | `is_oa: false`, `oa_status: closed`, no OA locations |
| 2 | OpenAlex `works/doi:10.1086/289852` | closed, `any_repository_has_fulltext: false`. Abstract retrieved (below) |
| 3 | Semantic Scholar Graph API | `isOpenAccess: false`, `openAccessPdf.status: CLOSED` (68 citations) |
| 4 | Cambridge Core direct PDF URL (`…/S0031824800063923a.pdf`) | HTTP 200, but it returns the HTML landing page: "Get access… Content may require purchase". **Article purchase: "Temporarily unavailable".** Abstract and affiliation taken from that page. The HTML was deleted and **no PDF was saved**, so `docs/sources/breuer-1995/` is empty |
| 5 | PhilPapers `rec/BRETIO-3` (WebFetch and curl) | HTTP 403 both ways. No PhilArchive copy is known |
| 6 | OpenAlex list of Breuer's open-access works | 16 OA items, all later finance/statistics or Kochen–Specker papers. None restates the 1995 theorem |
| 7 | arXiv author search `au:Breuer_T` | nothing relevant (only the 2002 Kochen–Specker preprints) |
| 8 | Follow-up: "Ignorance of the Own Past", *Erkenntnis* 48 (1998) 41–48, doi:10.1023/A:1005394214858 | Unpaywall closed. Springer redirects to login. No abstract in OpenAlex |
| 9 | Follow-up: "What theories of everything don't tell", *SHPMP* 28 (1997) 137–143 | Unpaywall closed. ScienceDirect 403 |
| 10 | Follow-up: "Subjective decoherence in quantum measurements", *Synthese* 107 (1996), doi:10.1007/BF00413900 | OpenAlex closed, no repository copy |
| 11 | Follow-up: "John von Neumann met Kurt Gödel" (1999, in *Language, Quantum, Music*, Springer, 159–170) | no open copy found |
| 12 | Author homepage `homepages.fhv.at/tb/cms/` | DNS does not resolve (the site is gone) |
| 13 | JSTOR stable/188430 | page exists, behind a JS challenge. Reading it needs a JSTOR account |
| 14 | scholar.archive.org / CORE | client challenge / redirect, no hit |
| 15 | Secondary restatements on arXiv: Szangolies 1805.10668, Mayburov quant-ph/0205024 and quant-ph/0212099, Jennings 2012.12033, Waaijer & van Neerven 1902.07139, Wolpert 0708.1362 | downloaded and searched. Mayburov gives the most detailed restatement, Szangolies one sentence, Wolpert nothing |
| 16 | SEP "Relational Quantum Mechanics", Fall 2005 archive, §4.2 (Laudisa & Rovelli) | gives a structural description of Breuer's formalism (quoted below) |

**The author cannot be contacted.** Thomas Breuer (b. 10 Aug 1966, Pune) **died on 11 September 2023 in Feldkirch** (de.wikipedia "Thomas Breuer"). He had taught at FH Vorarlberg, Dornbirn, since 1999. Two works of his restate the theorem in book length: his habilitation, *Universalität und Unvollständigkeit – Die Grenzen physikalischer Theorien* (Universität Salzburg, 1996), and his dissertation, *Classical Observables, Measurement, and Quantum Mechanics* (ETH Zürich).

**Ways MG could get the text:**
1. **JSTOR personal account** at jstor.org/stable/188430. A free personal account may allow reading online. I have not checked whether this journal is included.
2. **Library or interlibrary loan:** Vorarlberger Landesbibliothek, ULB Tirol (Innsbruck) or FHV library. Phil. Sci. 1995 is a common holding. The Salzburg habilitation would be at UB Salzburg.
3. **Buying it on Cambridge Core** once the purchase option, now "temporarily unavailable", is back.
4. ResearchGate entry 249081244 might hold an author upload, but it needs a login, and a full-text request cannot reach a deceased author.

---

## 2. What can be quoted from Breuer himself

**Abstract** (Phil. Sci. 62(2), p. 197, from Cambridge Core and OpenAlex):
> "It is shown that it is impossible for an observer to distinguish all present states of a system in which he or she is contained, irrespective of whether this system is a classical or a quantum mechanical one and irrespective of whether the time evolution is deterministic or stochastic. As a corollary, this implies that it is impossible for an observer to measure the EPR-correlations between himself or herself and an outside system. Implications of the main result are discussed for how we have to conceive of universally valid theories."

Affiliation on the article: Department of History and Philosophy of Science, University of Cambridge.

**Secondary restatements** (not Breuer's words, used only as corroboration):

- **SEP, RQM (Fall 2005), §4.2:** "Breuer studies the possibility for an apparatus O to measure its own state. More precisely, of measuring the state of a system containing an apparatus O. He defines a map from the space of all sets of states of the apparatus to the space of all sets of states of the system. Such a map assigns to every set of apparatus states the set of system states that is compatible with the information that — after the measurement interaction — the apparatus is in one of these states. Under reasonable assumptions on this map, Breuer is able to prove a theorem stating that no such map can exist that can distinguish all the states of the system."
- **Mayburov, quant-ph/0212099, §2 (same text in quant-ph/0205024):** "NO is NT subset and O state is S′T state projection on NO called an restricted state RO. From NT mapping properties the principal restrictions for MS states discrimination by O were formulated in Breuer theorem. Namely, if for two arbitrary S′T states ΦS, Φ′S their restricted states RO, R′O coincide, then for O this S′T states are indistinguishable." Mayburov also writes that "Breuer results doesn't permit to derive the restricted states for arbitrary quantum system unambiguously", and that Breuer took the partial trace as a "phenomenological ansatz" for the quantum restricted state.
- **Szangolies, arXiv 1805.10668:** "in 1995 Breuer proved that no observer can distinguish all the states of a system that includes them as a proper part".

---

## 3. Every statement of Breuer in paper 1 draft 3, with verdicts

Breuer is named in §1 (line 19), §4 (line 69), §7 (lines 117 and 119) and the reference list (line 167). §8, §9 and the Notes do not name him.

### S1 — §1, line 19: "the self-prediction results of Popper (1950), MacKay (1960) and, in measurement form, Breuer (1995)"
**Verdict: slightly inaccurate (category).** Breuer's result is about **present** states ("distinguish all present states", abstract). It is a self-*measurement* result, not a self-*prediction* result. Hanging it on "self-prediction results" puts it in the diagonal/prediction family, which §4 and §7 then take it out of.
**Proposed:** "the self-prediction results of Popper (1950) and MacKay (1960), and Breuer's (1995) result on self-measurement;"

### S2 — §7, line 119: "Breuer's (1995) observer that cannot distinguish all present states of a system containing it"
**Verdict: accurate.** This is nearly verbatim from the abstract (p. 197). No change.

### S3 — §7, line 119: "concludes that no state of D distinguishes all states of W"
**Verdict: accurate in substance, can be made more precise.** According to SEP, the theorem concerns the map from (sets of) apparatus states *after the measurement interaction* to the compatible system states: no such map distinguishes all system states. "No state of D" is a fair shorthand, but it skips the measurement step.
**Optional:** "…and concludes that no outcome D can be in after a measurement interaction distinguishes all states of W."

### S4 — §4, line 69 and §7, line 119: the mechanism is "non-injectivity of restriction"; D is "a proper subsystem in the kinematic sense, so that distinct states of W agree on D"
**Verdict: consistent with secondary sources; not verifiable at page level.** Mayburov's restatement is exactly this: distinct states with the same restricted state cannot be told apart by O. **One caveat the paper leaves out:** in the quantum case, the restriction (partial trace) is, according to Mayburov, an *ansatz* Breuer adopts, not something his theorem derives. This does not change the classification, but a referee who knows the literature could raise it.

### S5 — §4, line 69: the premise is "that W's admissible states include, **for each state of D**, distinct states agreeing on D and differing outside it"
**Verdict: probably stronger than Breuer needs, so it understates his result's reach. Unverified.** The conclusion "cannot distinguish **all** states" needs only **one** pair of distinct W-states with the same restriction to D, i.e. a restriction map that is not injective somewhere. "For each state of D" asks for every fibre to have at least two elements. If Breuer's own premise is the existential form, the draft makes his result look more conditional than it is. I could not see how Breuer words it.
**Proposed (safe in either case):** "a kinematic premise for Breuer's (1995) result, that distinct admissible states of W can agree on D, i.e. that restriction to D is not injective;" — and keep the mechanism as stated.

### S6 — §4, line 69: "Breuer's premise holds for infinite W, where a proper part can have as many states as the whole and counting fails"; §7, line 119: "uses no counting"
**Verdict: plausible, not verified at page level.** The abstract's "irrespective of whether this system is a classical or a quantum mechanical one" covers classical phase spaces of continuum cardinality, where a counting argument cannot work. So the claim fits the scope Breuer asserts. Whether Breuer himself remarks on cardinality, I cannot confirm. Note that Mayburov glosses the result as "O has less number of DFs", which is degrees of freedom, not cardinality, and is his gloss, not Breuer's. **No change proposed.** Mark it for a check against the text.

### S7 — §7, line 119: "Breuer's argument is independent of the dynamics" … "Breuer's argument, which sets the dynamics aside"
**Verdict: "independent of the dynamics" is accurate if read as "for any dynamics". "Sets the dynamics aside" is probably overstated.** Breuer's own claim is that the result holds "irrespective of whether the time evolution is deterministic or stochastic" (abstract, p. 197). That is universality *across* dynamics, not absence of dynamics. According to SEP, the time evolution is part of his formalism: the map is defined by what is compatible with the apparatus state "after the measurement interaction", and the theorem holds "under reasonable assumptions on this map". Those assumptions are not visible to me. They may well constrain how the dynamics acts (e.g. that the evolution does not shrink the state space). If so, "sets the dynamics aside" is false and "independent of the dynamics" needs a qualifier.
**Proposed:** "Breuer's argument holds whatever the time evolution, deterministic or stochastic, and uses no counting: …" and, later in the same paragraph, "…which is why capacity needs incompressibility and Breuer's argument, which holds for any time evolution, does not."
⚠ The contrast with capacity ("a description may fix the complement's state by procedures D runs…") depends on how Breuer's measurement map handles dynamics. Check this sentence against pp. 197–214 before submission.

### S8 — §7, line 117: "L1, L2 and Breuer's result use none" (no fixed-point-free operation, i.e. not diagonal)
**Verdict: consistent with every restatement found.** All of them describe a restriction/indistinguishability argument, not a diagonal one. Breuer's 1999 chapter title ("John von Neumann met Kurt Gödel: Undecidable statements in quantum mechanics") shows that he himself draws the Gödel *analogy*, and Szangolies lists Breuer next to the diagonal results. A referee might object here. The paper's claim concerns mechanism, not analogy, so it stands. No change.

### S9 — Reference, line 167
**Verdict: correct.** Volume 62(2), pp. 197–214, 1995, doi:10.1086/289852 all match Cambridge Core and OpenAlex. (Secondary sources misdate it: SEP 2005 and Waaijer & van Neerven give "1993". The draft has it right.)

---

## 4. Summary table

| # | Location | Claim | Verdict | Basis |
|---|---|---|---|---|
| S1 | §1 l.19 | Breuer as a "self-prediction result in measurement form" | slightly inaccurate (category) | abstract, p.197 ("present states") |
| S2 | §7 l.119 | cannot distinguish all present states of a system containing it | **accurate** | abstract, p.197 (verbatim) |
| S3 | §7 l.119 | no state of D distinguishes all states of W | accurate (optional precision) | SEP §4.2 |
| S4 | §4 l.69, §7 l.119 | mechanism = non-injectivity of restriction | consistent; quantum restriction is an ansatz | Mayburov; unverified at page level |
| S5 | §4 l.69 | premise "for each state of D" | probably stronger than needed (understates reach) | logic of the conclusion; unverified |
| S6 | §4 l.69, §7 l.119 | holds for infinite W / uses no counting | plausible | abstract scope; unverified |
| S7 | §7 l.119 | "independent of the dynamics" / "sets the dynamics aside" | first OK as "any dynamics"; **second probably overstated** | abstract p.197; SEP §4.2 |
| S8 | §7 l.117 | not diagonal | consistent | all restatements |
| S9 | refs l.167 | bibliographic data | **correct** | Cambridge Core, OpenAlex |

**Still open:** S4–S7 need the article body (pp. 197–214). Get it through JSTOR or a library (§1). Re-open AIW-295 once it is in hand, save the PDF to `docs/sources/breuer-1995/`, and check S5 and S7 first.
