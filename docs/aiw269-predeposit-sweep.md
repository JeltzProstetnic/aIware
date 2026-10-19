<!-- Action: await-user-decision -->
<!-- Tracked-by: AIW-269 -->
# AIW-269 — pre-deposit sweep: FMT v16 + formalization v4 (S323, 2026-09-28)

MG, verbatim: *"first we need to make sure we are aligned with most recvent literature and open todos"*.
Literature window: **pass 1 = 2026-08-26 → 09-28** (done). ⚠ MG S323 corrected the scope: no general sweep of the master had ever been run, which I failed to say when offering "since v15". **Final scope = since the first FMT deposit, 2026-02-17** → pass 2 covers 2026-02-17 → 2026-08-25.

Sources (subagent outputs, tracked):
`docs/aiw269-open-todos.md` · `docs/aiw269-lit-theories.md` · `docs/aiw269-lit-criticality.md` ·
`docs/aiw269-lit-ai.md` · `docs/aiw269-lit-formal.md`.

**Verification status.** Every MUST-ANSWER item plus the key MUST-CITEs was re-resolved by the main
loop (arXiv abstract page / Crossref / DataCite): titles, publishers and dates match. The remaining
NICE-TO-HAVEs are still subagent-verified only.

**Coverage caveat.** arXiv's API returned errors (429/406/empty responses) and OpenAlex rate-limited
the agents, so the arXiv sweep is partial, above all for the qualia/sentient/self-model/AI-welfare
keywords. A re-run of those keywords is owed before calling the sweep complete.

## Pass 2 (2026-02-17 → 08-25) — DONE S323

Slices in `docs/aiw269-p2/` (theories, criticality, ai, formal). New must-answers, all drafted in
`drafts/aiw269-must-answer-drafts.md`: **A7** Sipling/Zhang/Di Ventra (criticality premise), **A8** propofol
"Absent" (Sikka 2026, Bajwa 2025), **A9** Corcoran 2026 (PP as a contender), **F1** Roig/Muñoz/Morales (L2),
**G1** Gurnee J-space (folds into AIW-253, plus l.382/l.646), plus Goldstein & Kirk-Giannini (l.646) and two
more rival blueprints for §8.7 (CTM-AI, ReCoN-Ipsundrum). A4 strengthened by Selte 2026.
**Coverage gap, both passes:** OpenAlex daily quota exhausted; bioRxiv 7,020/7,656 and PsyArXiv 5,100/7,303
records pulled; math.DS/cs.IT title-screened. A top-up run after the quota resets (midnight UTC) is owed
before the deposit.

## A. MUST-ANSWER — literature that bears against a claim in the text

| # | Item (verified) | Hits | Proposed response |
|---|---|---|---|
| A1 | **Skipper et al., "What is it like to be a blob?"** bioRxiv/openRxiv 2026-09-09, `10.64898/2026.09.02.745341` — 579-study meta-analysis: no invariant core, and theory-nominated regions add no predictive power | FMT master l.767 (posterior hot zone = world model), l.957 (default-mode network = self model) | Reframe the region mappings as *candidate substrates of a functional architecture*, not as localisations; FMT's claims are functional, so this is a concession of wording, not of theory |
| A2 | **Basri, BarAvi & Hemmo**, *Conscious Cogn* online 2026-09-08, `10.1016/j.concog.2026.104121` — the unfolding argument is unsound; physics underdetermines function | §7.2 (unfolding), §4.4 (functionalism / substrate neutrality) | One paragraph: take the unfolding half as a gift, answer the indeterminacy half. ⚠ An SSRN version with a different title existed Dec 2025, so it is borderline for the window |
| A3 | **Nakamura, Michel & Lau, "Hitting and missing on consciousness"**, *Psychiatry Clin Neurosci* 2026-09-17, `10.1111/pcn.70136` — no-report paradigms do not remove hit/miss confounds | Table 1 l.196 (no-report as the empirical handle for closure) | Hedge the Table 1 cell; cite |
| A4 | **Wu, OSF replication registration** 2026-09-23, `10.17605/osf.io/vgehz` — Siclari 2017 posterior hot-zone dream decoding did not replicate on open 9–32-channel data (not peer-reviewed; the author scopes the null to coarse resolution) | §6.3 l.767 "with high accuracy" | Soften to "reported … (a low-density replication failed, Wu 2026)" |
| A5 | **Grinberg et al., S3Q → machine-qualia architecture**, arXiv:2609.30743 | §8.7 "Unique? … no specific architectural blueprint" | Soften §8.7 or add S3Q to §7.3 with the differences (no separate self-model, no closure/Class-4 requirement) |
| A6 | **Khadangi, "We Built a Mirror and Mistook It for a Mind"**, arXiv:2609.06715 — liability-based "closure" criterion | §3.4.3 closure | One sentence separating the two senses of "closure" |

## B. MUST-CITE — additions that support existing claims

| Item | Where |
|---|---|
| Nikolič et al. 2026, *J Psychopharmacol*, `10.1177/02698811261473445` (psilocybin raises gamma signal diversity; tracks acute effects, r = 0.71) | master l.415, Table 4 l.689 |
| Sahakian et al. (PsyArXiv 2026-08-28) — children's imagination/reality confusion | master l.718–720 |
| Bates et al. (bioRxiv 2026-08-27) — focal TPJ stimulation (tDCS) impairs perceived-vs-imagined discrimination | master l.1027 |
| Watanabe et al. (bioRxiv 2026-09-21) — colour-similarity alignment, toddler → adult | Prediction 5, caveat l.973 stands |
| Bassler & Pennartz (PsyArXiv 2026-09) — judge theories by the regularities they predict | §1.2 / §7.1 scoring |
| **Bieberich RIFT → published version**, *Brain Sci* 2026-09-16, `10.3390/brainsci16090983` | reference l.1170 (currently the bioRxiv version) — mechanical |
| Šekrst; Maczan; Zeng et al. (LLM self-report is trained, and self-prediction ≠ introspection) | master l.646, l.342 |
| van Rooyen (arXiv:2609.22300); Solms et al. (arXiv:2609.03883) | l.640; §4.2.2 |
| Fontenele…Shew 2026 *Commun Phys* (criticality hidden from power-law fits) — conditional: its preprint dates from 2025 | l.478 (DFA α choice) |
| **Formalization:** Du et al. arXiv:2609.07624 (Fisher information as criticality proximity); Carcamo & Lynn arXiv:2609.09438 (fitted models drift to criticality); Vock & Meisel arXiv:2608.28431 (local rule → criticality in deep networks) | roadmap §4.2, §2.6/§4.3/§4.7, §4.4 |

## C. Outside pass-1 window — ALL THREE INCLUDED by MG S323

- Dijkstra, Fleming & Shea, "Why do we need imagination–reality monitoring?", *Neurosci Conscious* niag048, online 2026-08-20 — directly on l.718–720.
- "A Critical Assessment of the Brain Criticality Hypothesis", arXiv 2604.21071 (Apr 2026, unverified) — a direct attack on the criticality premise; v15 does not cite it.
- Anthropic, "A global workspace in language models" (2026-07-06) — bears on l.646.

## D. Open to-dos (from `docs/aiw269-open-todos.md`)

- **Ready for v16:** AIW-240 (reference-list sort); AIW-253 (J-space paragraph, placement open).
- **Ready for v4:** AIW-251 surrogate caveat beside the E-dial (3–4 sentences).
- **Needs an MG ruling:** AIW-243 (hedges; add Mashour 2020 + Lau PRM; defer the style pass), AIW-201, AIW-265, AIW-266 (Culik & Yu sentence), AIW-219 (cite Friedlander 2015), AIW-75 (Gruber 2015 self-citations), AIW-77 ("sentience"), AIW-251 (master sentence).
- **Close as already in source** (to be spot-checked before closing): AIW-222, 202, 193, 110, 53.
- **Structural:** v16 has no epic (AIW-210 is closed) → AIW-269 serves as the v16/v4 umbrella.
