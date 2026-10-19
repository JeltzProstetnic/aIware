<!-- Action: reference -->
<!-- Tracked-by: AIW-281 -->
# FMT v19 — master edits queued from the S334 rulings

Source of rulings: `docs/decisions.md` S334. Changelog draft: `docs/zenodo-changelog-fmt-v19.md`. Edit the md and the
hand-maintained `paper/full/latex/paper.tex` together. Nothing deposited without MG's go.

Done: Table 1b closure falsifier (D1).

## D2 — minimal consciousness, two axes, sleep (line numbers as of a771607)
1. §3.5 l.388 — terminology sentence ("sentience names…; awareness is not used…"): one-gate rule; "minimal
   consciousness" for the floor, sentience only as cross-reference; two axes (richness of content × depth of recursion).
2. §3.5 l.390 basic consciousness ("entry level"): add a minimal-consciousness entry below it (rudimentary closure;
   the now + primordial pain or nothingness; no reflection, past/future or discernible qualia; unreportable).
3. §3.5 l.398 ("each level … additional layer of recursive self-modeling"): add the richness axis.
4. §3.4.6 l.382 Block note: reportability grows with recursion depth; access (Block, dispositional) = preconscious,
   implicit side (Dehaene et al. 2006), conscious only via a permeability event.
5. §5.3 Table 4 l.690 Deep NREM row: consciousness "probably absent (unconsciousness)"; reconcile up-state NREM
   dreaming (assign to non-deep NREM or justify).
6. §5.3 Table 4: add a non-deep-sleep row (reportable state closest to the floor).
7. §5.3 l.769 "any sleep stage": qualify.
8. §5.3 l.773 NREM dreaming in up-states: say which NREM depth.
9. §6.4 l.783/798/800: the floor as the lowest rung (fish, amphibians, possibly insects); sentience cross-reference here.
10. Glossary l.160 Consciousness: optional note on the one-gate rule; minimal consciousness lies below what PCI and
    report detect.

## D2c — accessible vs accessed (from the wiki agent's master scan)
11. §3.4.6 l.382: restrict "access and phenomenality are two descriptions of the same process" to ACCESSED content;
    add ACCESSIBLE = preconscious, implicit side (Dehaene et al. 2006); felt self-initiated retrieval = agency
    illusion (Libet; Wegner; §6 free will).
12. §3.4.6 "What converts presence into access is … added recursive depth … a degree of conscious access" →
    reportability.
13. §3.4.6 overflow paragraph "a shallower state of both access and phenomenality" → thin self-model with too little
    recursion above it for its content to be reported.
14. §3.5 basic consciousness ("experiences a world and has a minimal sense of being a subject"): reconcile with the
    floor wording (item 2).
15. §7.2 HOT paragraph: HOT's higher-order representation ↔ FMT's extended rungs; minimal consciousness has none.
16. Same fixes in `drafts/papers-moc7/theory-map-paper.md` (frame l.~77 "converts present into accessed"; C4
    "shallower state of both access and phenomenality").

## D3 — RPT
- §7.2 / Table 5: RPT from "compatible" to "recurrence absorbed; local-recurrence sufficiency contradicts Principle 3".

## D4 — short §7.2 paragraphs
- ICT (Kanai), Searle, enactivism (Thompson), PRM (Lau), CTM (Blum & Blum), MPE (Metzinger — answer: the floor is a
  rudimentary closure, so "selfless" MPE still has an implicit self/world boundary). Source: fairness-reviewed records
  in `drafts/papers-moc7/theory-map-paper.md`.

## Status after the v19 drafting pass (S334)
Items 1–16, D3 and D4 are drafted in md + tex (not compiled: no LaTeX on Deck 2). Open before deposit:
- references.bib: add keys for Blum & Blum 2022, Chang et al. 2020, Metzinger 2020, Searle 1980, Searle 1992,
  Thompson 2007, Varela/Thompson/Rosch 1991, and turn the plain-text cites in paper.tex into \citep/\citealp.
- Check the Siclari summaries against the papers: "fewer and smaller slow waves" (2018) and "local posterior
  reduction of low-frequency activity" (2017).
- Check §1.3 supports "transparent" in the MPE paragraph.
- Build at WSL; changes-highlighted PDF against the v18 commit for MG's review.
- MG's judgement calls (listed in the session report): NREM up-states, light NREM only as "closest to the floor",
  MPE reading, basic vs minimal on the same recursion depth, sentience citation (Birch 2024?), MCS clause.
- theory-map-paper.md C3, §4.1, frame "Second": "phenomenality at the basic rung" → "minimal and basic".

## Pass 2 — MG rulings on C1–C9 (S334)
Source: `docs/decisions.md` S334, bullet "FMT definition vs Paper A's C1–C9"; assessment
`docs/reviews/2026-10-17-fmt-definition-vs-C1-C9.md`. All items drafted in md + tex (not compiled: no LaTeX on Deck 2).
17. Process, not capacity — §3.1 opening rewritten (process; capacity for consciousness named separately; 2015
    *Bewusstsein*/*Bewusstheit* p. 57 quoted); Table 1 Consciousness definition = process; one-gate sentence moved into a
    note marked as a consequence of Principle 3. Sweep: §3.1 ¶2 "produces"/"generates" aligned; §3.5 l.388 one-gate
    sentence already gate-shaped, kept; no other consciousness-as-capacity wording found (l.225 "capable of
    consciousness" and l.1028 "the capacity is rare" refer to the capacity, correctly). — drafted.
18. Sufficient conditions + engineered valence + embodiment/locked-in — §3.7.3 ("Together they are sufficient"
    replaced by the conjunction); §4.4 opening sentence restated against it. — drafted.
19. Self-model criterion + SLAM ruling — §3.4.3 new paragraph "What counts as a self model"; §3.5 minimal entry;
    §6.4 anthropomorphic-risk note. — drafted.
20. Non-reporting systems — Table 1b new row; §3.1.1 closing sentence; §3.5 minimal entry (non-report signature);
    §4.4 "measurable on the system itself"; §6.4 "can only be indirect". — drafted.
21. Bridge = identity — Principle 3 in §3 and §3.4; §3.4 constitutive-step sentence; §3.1 ¶2; §7.2 HOT and RPT; §4.4
    in-vivo markers vs in-silico premise test (71.5–74.0%). Left as is: "consciousness arises from the interplay"
    (§3.4.2, §3.7.2: substrate-to-level generation, not the bridge); "closure constitutes phenomenality" (§3.4.4,
    constitutive); "why does closure generate phenomenality" (§3.4.3, the residual question as posed). — drafted.
22. Panpsychism — §4.1, §4.3, §4.2.5 (Russellian), Table 5 ¶ note. IIT criticisms unchanged. — drafted.
23. `scripts/test_content_integrity.py` canaries updated to the identity wording (same strength). — done.
Open: rebuild `wiki/llms-full.txt` (`python3 scripts/build_llms_full.py`; its staleness test fails); build at WSL.
