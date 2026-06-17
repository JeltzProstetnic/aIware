# Literature Research: Motivation and Intelligence Models

**Generated**: 2026-02-14 (Session 27)
**Source**: Research analyst agent, 31 tool uses, 25+ web searches

## Key Finding

**No major scholarly paper explicitly argues that the systematic exclusion of motivation from intelligence models is a fundamental theoretical blind spot.** This confirms the novelty of our paper.

## Summary Table

| Theory | Acknowledges Motivation? | Includes in Model? | Why Not? |
|--------|--------------------------|-------------------|----------|
| Binet (1905) | Yes (affects test performance) | No | Designed tests to minimize motivational variance |
| Spearman (1904) | Implicit (g as "mental energy") | No | Factor analysis strips out motivational variance |
| Wechsler (1940) | **Yes (essential for life success)** | **No (called for it, ignored)** | Psychometric tradition prevailed |
| Cattell (1943-1987) | Yes (investment traits motivate Gf->Gc) | No | Treats motivation as external catalyst |
| CHC Theory (dominant) | Yes (acknowledged as confound) | No | Pure cognitive model, 16 abilities, zero motivational |
| Sternberg (1985) | Implicit (practical intelligence) | No | Not theorized as distinct component |
| Gardner (1983) | **Yes (intrapersonal intelligence)** | **Yes** | Rejected by field, lacks psychometric validation |
| Ackerman PPIK (1996) | Yes (personality & interests drive development) | No | Kept outside intelligence construct |
| Dweck (2006) | Yes (growth mindset drives development) | No | Treated as educational psychology, not intelligence |
| Stanovich (2016) | **Yes (motivation to engage System 2)** | **No (part of RQ, not IQ)** | Preserves traditional IQ construct |
| Duckworth (2007) | Yes (grit = perseverance + passion) | No | Personality trait, orthogonal to IQ |

## Closest Predecessors

1. **Wechsler (1943)**: "We cannot expect to measure total intelligence until our tests also include some measures of the non-intellective factors." — Ignored.
2. **Snow (1996)**: Proposed SRL as "overarching conative concept" — stayed in educational psychology.
3. **Stanovich (2016)**: Introduced RQ to capture what IQ misses — kept as separate construct.

## Full research output

See `/tmp/claude-1000/-home-jeltz-aIware/tasks/a1e617d.output` for raw agent transcript with all citations and URLs.

---

## COGITO papers from Schmiedek/Wittmann — relevance evaluation (Session 225, 2026-06-17)

**Provenance.** Werner Wittmann sent the RIM paper to **Florian Schmiedek** (DIPF Frankfurt; core COGITO author). Schmiedek replied endorsing RIM's central thesis ("motivation is underestimated"; for a COGITO 2 he would add *task-specific daily motivation* measurement) and attached these two papers; Wittmann forwarded them 2026-06-16 (correspondence `wittmann-werner.md` Msg 28). Full texts: `literature/fulltext/Brose2010.pdf`, `Schmiedek2020.pdf` (CC-BY). Both read in full this session.

### Brose, Schmiedek, Lövdén, Molenaar & Lindenberger (2010) — *Research in Human Development* 7(1), 61–78
**What it is.** COGITO (101 younger 20–31, 103 older 65–80; ~100 daily sessions). Daily motivation measured with the Intrinsic Motivation Inventory (effort, 2 items; enjoyment, 3 items); WM = spatial 3-back. R-technique (between-person) vs P-technique (within-person) factor analyses of the motivation↔WM link, explicitly testing the **ergodicity** assumption.
**Findings.** (1) In younger adults, motivation (both effort and enjoyment) is **positively coupled with WM performance day-to-day** — higher-motivation days are better-performance days — at both levels. (2) In older adults the coupling is near-zero/weak (reduced motivation variability; more routinized lives; many older participants showed *no* motivation variance and were excluded). (3) **Within-person structures differ reliably across individuals → ergodicity is violated**; the average between-person correlation *underestimates* the average within-person coupling.
**Relevance to RIM — HIGH / direct (this is the M-factor evidence).**
- It is the cleanest published demonstration that **motivation is not noise but a systematic, measurable determinant of cognitive performance within a person over time** — the empirical anchor for treating M as constitutive in K×P×M, not an external catalyst.
- Maps onto RIM **Prediction 8** (§7.2): "motivation should predict *consistency* of intellectual engagement... intraindividual SD... testable with experience-sampling." Brose's P-technique daily design is exactly that methodology; the heterogeneity it finds is what RIM predicts.
- Non-ergodicity directly reinforces RIM's **Brunswik-symmetry / temporal-reliability** argument (§3.1, Prediction 7): single-occasion motivation snapshots mechanically attenuate the motivation–intelligence correlation. Brose shows motivation *fluctuates* and that the fluctuation carries real performance variance.
- **Honest-framing caveat:** the coupling is robust in the young but weak/absent in older adults, and heterogeneous across individuals — cite as "motivation systematically co-varies with cognitive performance within persons (in those who vary)," NOT "motivation universally drives cognition."

### Schmiedek, Lövdén, von Oertzen & Lindenberger (2020) — *PeerJ* 8:e9290 (CC-BY)
**What it is.** COGITO young-adult daily data (101 adults × 9 cognitive tasks — 3 WM, 3 episodic memory, 3 perceptual speed — × ~100 days). Compares **within-person** vs **between-person** correlation structures via symmetrical Kullback–Leibler divergence + MDS + hierarchical (g) factor models.
**Findings.** (1) Within-person structures diverge greatly from the modal between-person structure AND from each other (avg KL ≈ 5.90, p<.001; non-ergodic). (2) WM carries the largest common variance at both levels, but **the g factor is far less prominent within than between persons** (de-trended within-person g loading of perceptual speed ≈ 0). (3) **Between-person structure cannot serve as a surrogate for within-person structure**; "the hierarchical model of intelligence is not necessarily the best template for capturing the organization of intelligence within individuals." Calls for person-oriented study (cf. Schork 2015 "Time for one-person trials"; Finn 2015 connectome fingerprinting; conditional ergodicity, Voelkle 2014).
**Relevance to RIM — HIGH / structural + methodological (not motivation-specific).**
- Independent, rigorous **empirical undercutting of g-as-the-essence-of-intelligence** — the IQ/psychometric tradition RIM argues against. RIM critiques g on theoretical grounds (motivation omitted); Schmiedek shows g is largely a *between-person* artifact that doesn't even describe within-person cognitive organization. Strong convergent ammunition for RIM §3.4 / §7.1.
- Establishes the **methodological warrant** for RIM's whole within-person prediction program: to study how intelligence is actually organized and develops, you must measure individuals intensively over time — exactly the design RIM's recursive-loop and variance/consistency predictions assume.
- **Honest-framing caveat:** this paper does **not** test motivation; it is about the (non-ergodic) structure of *cognitive* performance and the weakness of within-person g. Use it for the g-critique + the within-person methodology, and pair it with Brose 2010 (and Schmiedek's own email) for the motivation link. Do not cite it as direct evidence for the M factor.

### Use recommendations
1. **RIM paper (`paper/intelligence/paper.md`) — add both to References and cite where the argument already exists:**
   - §3.4 *Relation to Existing Work* + §7.1 — Schmiedek 2020 as independent evidence the between-person g structure is not the within-person reality (strengthens the case against g-centric intelligence theory).
   - §7.2 *Predictions 7 & 8* (Brunswik symmetry / temporal reliability; consistency = intraindividual SD via experience sampling) — Brose 2010 as existing P-technique evidence that motivation fluctuates and co-varies with performance within persons; both papers as the methodological precedent (COGITO, KL-divergence, P-technique) for operationalizing RIM's within-person predictions.
   - §3.1/§3.3 (motivation as constitutive, not "motivation matters") — Brose 2010 as the within-person empirical instantiation.
   - These are **content edits to the manuscript** → do on the next RIM revision pass (AIW-81 / RIM resubmission), with user sign-off on framing; storage + this evaluation are done now.
2. **Classification:** primary = **RIM sources** (not mere "related work"). Stored in `literature/fulltext/` + master list `docs/references.md` §5 (new "Intraindividual Variability & Within-Person Structure" subsection).
3. **FMT relevance — peripheral only.** No motivation/consciousness content; the one transferable idea is the **non-ergodicity / within-person measurement philosophy** (relevant to how FMT's empirical self-model predictions — e.g. the AIW-47 meta-d′ work — should be tested within individuals over time). Do NOT shoehorn either paper into the FMT papers; the FMT-empirical thread is the ketamine meta-d′/d′ work, a separate strand. (This is why they live in the RIM literature file and are only *noted* — not listed as FMT refs — in `literature/INDEX.md`.)
4. **Strategic (convergence-and-differentiation, mirrors the Bach prior-art task):** Schmiedek is a senior COGITO author **independently** converging on RIM's core claim. Frame any citation/outreach as *independent convergence + what RIM adds* (the multiplicative K×P×M formalization; motivation as constitutive component, not moderator) — credit, don't concede priority.
5. **Owed correspondence:** the substantive RIM reply to Wittmann (+Schmiedek), due after mid-July, must engage both papers concretely — esp. that RIM predicts exactly the *task-specific daily motivation* measure Schmiedek says COGITO lacks. (Tracking: `correspondence/wittmann-werner.md` Msg 23/28.)
