<!-- AIW-269 S324 2026-09-28 — apply report, FMT master v16 (subagent). Nothing committed. -->
# AIW-269 apply report: FMT master (v16)

Files edited: `paper/full/four-model-theory-full.md`, `paper/full/latex/paper.tex`, `paper/full/latex/references.bib`.
Not touched: `paper/fmt_formal/*`, the canonical `paper/full/latex/paper.pdf` (a test build was made in the
scratchpad only). Nothing committed or pushed. Line numbers below are the current (post-edit) state.

## Gates: baseline vs after (measured)

| Check | Baseline (HEAD) | After |
|---|---|---|
| `pytest scripts/test_content_integrity.py -q` | `32 passed in 0.11s` | `32 passed in 0.10s` |
| `python3 scripts/verify_references.py --check` | `OK — 751 references (573 verified, 178 verified-manual), all verified and unchanged. 359 printed bibtex citations matched` | `77 reference problem(s) across 827 entries` = **61** `fmt:… is not in the manifest` (the 61 new refs, need `--update`) + **1** `fmt:Chalmers1996 changed since it was verified` (the 1996→1996a relabel) + **15** `fmt_formal:…` (the other agent's roadmap refs, not mine). No "cited but not in references.bib" errors. |
| `check_md_pdf_drift.py --paper full` (option exists) | reference order: **35** misordered (HEAD md) | against canonical `paper.pdf`: STALE TARGET (expected, PDF not rebuilt; 99 md-only / 45 pdf-only segments). Against a scratchpad test build of the new tex: 85 segments, all rendering noise of the pre-existing classes (3-author "A, B, and C" vs "A et al.", figure captions, footnotes, Table 3 flattening). Reference order: **9** misordered, all explained below. |
| Test LaTeX build (scratchpad copy, pdflatex×3 + bibtex) | — | 0 LaTeX errors, 0 undefined citations, 0 Overfull boxes, bibtex 0 warnings, 320 bibitems. `Chalmers1996` renders as 1996a and `Chalmers1996b` as 1996b (plainnat `\natexlab`). |

## Per spec row

| ID | Status | md location | tex location |
|---|---|---|---|
| A1+A4 | applied verbatim (both parts) | §6.3 l.769 "Siclari et al. (2017) identified, in 256-channel EEG…"; §8.1 l.925, appended to "Converging neural evidence for the 2×2 architecture" ("A meta-analysis of 579…") | l.966; l.1162 |
| A3 | applied verbatim | Table 1b "Self-ref. closure" row, l.196 | l.275 |
| A5 | applied; draft text + clause "and CTM-AI (Yu et al., 2026) and ReCoN-Ipsundrum (Sanyal, 2026) are two more" | §8.7 l.991 "**Unique?**: In part…" | l.1238 |
| A6 | applied verbatim as footnote | §3.4.3 l.302, after "**self-referential closure**." | l.417 `\footnote` |
| A2 | applied verbatim (hedged form); §4.4 pointer applied | §7.2 new paragraph l.873 "Basri, BarAvi and Hemmo (2026) reject…"; §4.4 l.632 "For the objection that physics underdetermines…" | l.1099; l.801 |
| A2 Chalmers relabel | done | **5** in-text sites, not 4: l.42 (Nagel; Chalmers 1996a), l.84 "Chalmers (1995, 1996a)", l.282, l.608 Zombies, l.614 property dualism; ref list entry → 1996a; new 1996b entry | bib key `Chalmers1996` kept, `Chalmers1996b` added; bibtex suffixes verified in test build |
| A7 | applied: paragraph + all four accompanying edits | Table 3 2025 row l.467; convergence para l.470; l.472 "On the critical-point reading…"; caveat end l.476 "; the guard assumes…"; new paragraph l.478 "Sipling, Zhang and Di Ventra (2026) extend this caveat…" | l.608, 614, 616, 620, 622 |
| G1(a) | applied; final falsifier sentence replaced by the spec's gradient sentence | §7.2 GNW entry l.853, replaces "No such manipulation currently exists…" | l.1078 |
| G1(b) | applied verbatim ("ignition-like broadcast") | §3.4.6 Block paragraph l.382 "In brains, the operationalizations…" | l.505 |
| G1(c) | applied, both insertions | §4.4 l.648 "Post-trained models do carry…" and "Goldstein and Kirk-Giannini (2026) argue…" | l.817 |
| A8 | applied; cell + sentence exactly per spec; no prediction sentence | Table 4 l.689 "Absent at surgical depth"; §5.3 l.696 "At surgical depth propofol…" | l.871; l.882 |
| A9 | applied, both parts, spec text | §7.2 PP entry l.857 "Its proponents have since entered active inference…"; §1.1 l.31 "A second adversarial review…" | l.1082; l.67 |
| AIW-243(1) | applied, three one-clause hedges | (1) reafference scope, §3.2 l.233: "any system that acts **and models its world** must predict…"; (2) score analogy, §3.4.3 l.326: "(the analogy covers only the gap between description and instance, since a symphony is not closed on itself)"; (3) ceiling criterion, §3.6 l.417: "absent ceiling effects, with the ceiling established independently of the entropy outcome, for instance by 5-HT2A receptor occupancy measured with PET" | l.332; l.441; l.550 |
| AIW-243(2) | citations only | Mashour et al., 2020 in GNW header l.853; Lau (2022) at §6.0 l.720 "Reviewing the candidate cues for perceptual reality monitoring (Lau, 2022), Dijkstra et al. (2022)…" | l.1078; l.909 |
| AIW-266 | applied | §3.7 l.453, end of the Gruber (2015) paragraph after the class list: "Which class a given automaton belongs to is formally undecidable (Culik & Yu, 1988), so the theory's commitment is to the regime's measurable signatures." | l.590 |
| AIW-219 | applied, one clause | §8.9 **eighth** banked result, l.1007 "Second, the selection is confined to low-dimensional content, as in the evolution of bow-tie architectures under rank-deficient goals, whose waist width equals the goal's rank (Friedlander et al., 2015)…" — see flag 1 | l.1258 |
| AIW-251 | applied, one methods sentence | §3.7 extent dimension l.484 "Regional estimates of this kind need a surrogate that preserves each region's temporal structure, such as window jitter, because shuffling columns manufactures spurious local criticality." | l.628 |
| Must-cites | 35 applied, Tiehen & Tubert skipped, Bieberich already present | see list below | same sites |
| AIW-240 | done | ref list sorted: **260 entries before, 321 after** (260 + 61 new, 0 lost, 0 duplicated; verified by exact comparison with a generated target list) | n/a (bibtex sorts) |

**Held, not applied:** AIW-243(3), AIW-201, AIW-265, AIW-75, AIW-77.

### Must-cite placements (all as minimal citations of existing claims)

- Gibbons 2026 — §1.1 l.31, COGITATE parenthetical ("extension to non-human primates and mice")
- Overgaard, Dietz & Waade 2026 — §1.1 l.31, clause after the "Reviews published…" citations
- Bassler & Pennartz 2026 — §7.1 l.818, parenthetical after "strongest empirical apparatus"
- Maczan 2026, Šekrst 2026 — §3.4.3 l.338, clause after "most readily confabulated strings"
- Moses, Doss & Tagliazucchi 2026 — §3.6 l.415, clause after Schartner (2017)
- Fontenele et al. 2026 — §3.7 l.480, after Clauset et al. (DFA α choice)
- Newman et al. 2026 — §3.7 l.482 (PCI paragraph), "criticality features predicted PCI only within subgroups"
- Jeantin et al. 2026 — Table 4 propofol Evidence cell
- Nikolič et al. 2026 — Table 4 psychedelics Evidence cell
- Mallavarapu & Percy 2026 — §4.1 l.550 ("for a no-go argument against process theories, see…")
- Sofroniew et al. 2026, Han, Chalmers & Izmailov 2026 — §4.2.3 l.596, readout available short of closure
- Fleming & Michel 2025, 2026 — §4.2.4 l.604 ("compare the proposal that conscious vision evolved for offline cognition")
- Koch 2026, Pennartz 2026, Butlin et al. 2026, van Rooyen 2026, Solms et al. 2026 (as "case study") — §4.4 l.642 after Beni (2026)
- Seth 2025 — §4.4 l.644 "Seth's (2021, 2025)"; Klatzmann & Doerig 2026 — same paragraph, one clause
- Kanai, Sun & Baltieri 2026 — §4.4 l.648 "(knowledge resets between interactions; …)"
- Macar et al. 2026 — §4.4 l.648 "(Gurnee et al., 2026; see also Macar et al., 2026)"
- Lederman & Mahowald 2026, Singh et al. 2026, Zeng et al. 2026 — §4.4 l.648 "current models' reports about their own internal states are limited"
- Perrier & Bennett 2026 — §4.4 l.648 on "architectural mimicry"; Xie 2026 — "The orchestration is external scaffolding (Xie, 2026)"
- Sahakian et al. 2026 — §6.0 l.720 "replicated down to age five by"
- Dijkstra, Fleming & Shea 2026 — §6.0 l.716 end of source-distinguishability paragraph, cited only for the functional analysis its abstract claims
- Tzioridou et al. 2026 — §6.0 l.722, dream recall predicts dream–reality confusion
- Changeux & Farisco 2026 — §7.2 GNW l.853, after the Dehaene (2021) substrate-independence sentence
- O'Reilly-Shah et al. 2026 — §7.2 l.865, one sentence after the unfolding-argument statement
- Watanabe et al. 2026 — §8.6 l.977 beside Kawakita (2025)
- Bates et al. 2026 — §9 OQ4 l.1031 TMS candidate (i), cited only as a source-memory (spoken vs imagined) result, per the refs-file warning

Skipped: **Tiehen & Tubert 2026** (must-answer not ruled). Already present: **Bieberich 2026**.

## References added (61 keys, md list + references.bib, copied from `docs/aiw269-refs-verified.md`)

Gibbons2026, Corcoran2026, Bandara2026, Overgaard2026, BasslerPennartz2026, Nakamura2026, Moses2026, Khadangi2026,
Maczan2026, Sekrst2026, Gurnee2026, CulikYu1988, Sipling2026, Janbon2026, Munn2026, Fontenele2026, Newman2026,
MallavarapuPercy2026, Sofroniew2026, Han2026, FlemingMichel2025, FlemingMichel2026, Koch2026, Pennartz2026, Butlin2026,
vanRooyen2026, Solms2026, Seth2025, KlatzmannDoerig2026, Kanai2026, Macar2026, LedermanMahowald2026, Singh2026, Zeng2026,
PerrierBennett2026, GoldsteinKirkGiannini2026, Xie2026, Jeantin2026, Nikolic2026, Sikka2026, Bajwa2025, Sahakian2026,
Lau2022, DijkstraFlemingShea2026, Tzioridou2026, Selte2026, Wu2026, Mashour2020, ChangeuxFarisco2026, Harris1954,
Firth1957, OReillyShah2026, Basri2026, Chalmers1996b, Skipper2026, Watanabe2026, Grinberg2026, Yu2026, Sanyal2026,
Friedlander2015, Bates2026.

bib: 278 → 339 entries, no duplicate keys; every new key is cited in paper.tex. The refs-file corrections are carried
(Vanasse, Wu registration date not in citation, Corcoran group author, Grinberg nine authors, Sun **Y.**, van Rooyen v2
title, Guenot spelling, Bajwa "deep sedation"). Relabel: md `Chalmers, D.J. (1996)` → `(1996a)` plus the 5 in-text sites.

## Register check (rule 8), measured

| Text | words | "rather than" | " not " | "—" |
|---|---|---|---|---|
| HEAD md, whole file | 56,552 | 173 (3.06/kw) | 608 (10.75/kw) | 861 (15.22/kw) |
| Added lines, `git diff -U0 \| grep '^+'` (as instructed) | 12,882 | 33 (2.56/kw) | 124 (9.63/kw) | 145 (11.26/kw) |
| Added lines excluding reference entries | 10,236 | 33 (3.22/kw) | 123 (12.02/kw) | 145 (14.17/kw) |
| HEAD body excluding references | 51,006 | 173 (3.39/kw) | 604 (11.84/kw) | 857 (16.80/kw) |
| **Inserted words only** (word-level diff of the body) | 1,684 | 1 (0.59/kw) | 9 (5.34/kw) | 0 (0.00/kw) |

The `^+` measure is dominated by whole pre-existing paragraphs that git reports as changed lines (the md has one
paragraph per line), so the word-level row is the one that measures the new prose. The one "rather than" is in the
ruled A5 text ("rather than positing a separate explicit self-model").

## Flags — things that looked wrong or needed a call

1. **AIW-219 placement.** The spec says "seventh banked result", but the bow-tie ⇔ rank-deficient-goal / waist = rank
   result matches the **eighth** result's low-dimensionality condition (the seventh is the hidden-disturbance result).
   Placed at the eighth. Move it if the seventh was meant.
2. **Reference order: 9 residual checker flags, 0 real ones.** `check_md_pdf_drift.py`'s key (a) turns ", & X" into a
   double space, which sorts two-author "& X" entries before any other co-author (flags Carhart-Harris & Friston,
   Dehaene & Naccache, Northoff & Huang, Tononi & Edelman, which are in APA second-author order); (b) deletes
   non-ASCII letters, so Güntürkün, Näätänen, Öhman and Šekrst sort as "gntrkn", "ntnen", "hman", "ekrst". I sorted
   with diacritics folded (APA). (c) **Kirkeby-Hinrup 2025a/2025b** is kept a-then-b as the spec says ("a/b suffixes
   in order"), which also matches bibtex's a/b assignment. By second author, Fink (2025b) would come first, so the
   checker flags it. Putting b first also swapped the two entries' hashes in the reference manifest
   (`KirkebyHinrup2025` / `KirkebyHinrup2025b` "changed since verified"), because the gate keys duplicate
   surname+year entries by position. With a-then-b those two errors are gone.
3. **Chalmers 1996 had 5 in-text sites**, not 4 (the refs file missed `Chalmers (1995, 1996)` at §2.1).
4. **Reference gate keys for non-ASCII surnames.** The gate records Šekrst as `fmt:ekrst2026`. Harmless for `--update`, but
   the key will look odd in the manifest.
5. **Ruled text that breaks the prose rules** (applied verbatim as instructed, flagged for MG): A9's "and the comparison
   below treats it on those terms" narrates the document; G1(b)'s "They are its signature and not its definition" is a
   not-X-but-Y construction.
6. **tex citation form.** Six compound citations with prefixes/interjections are written as `(\citealp{…}; text \citealp{…})`.
   `\citetext{…}` was tried first and dropped, because `verify_references.py`'s `\cite…{…}` regex mis-reads `\citetext`
   and reported phantom "cited but not in references.bib" keys. As a side effect the COGITATE citation now renders
   "(COGITATE Consortium, 2025; protocol: Melloni et al., 2023; …)". Before, the tex's `\citep[protocol:][]{…}` printed
   "protocol:" ahead of COGITATE, which did not match the md.
7. **Must-cite judgment calls that MG may want to check:** Changeux & Farisco (2026) is cited as *disagreeing* with the
   paper's own "GNW is substrate-independent" sentence. That is what their abstract says, so the clause reports the
   disagreement. Mallavarapu & Percy (2026) is a no-go argument *against* process theories and is cited as such, with
   no reply. Bates et al. (2026) is cited only as a source-memory result. Dijkstra, Fleming & Shea (2026) is cited only
   for its functional analysis, not for "flexible prefrontal metacognitive evaluation".
8. `verify_references.py --update` has not been run (network step, left to you).
