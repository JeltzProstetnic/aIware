<!-- AIW-343 study kit index. PRIVATE (drafts/ is excluded from the public mirror) until data collection closes. -->
# AIW-343 — "Perception and beliefs about the mind" study kit

| File | What |
|---|---|
| `protocol.md` | Design, hypotheses, exclusions, analysis, power, falsifier, ethics — doubles as the OSF pre-registration draft |
| `questionnaire-part1.md` | Full Part 1 instrument (EN master) with item IDs = CSV column names |
| `consent-and-info.md` | Participant information + GDPR consent |
| `recruitment-message.md` | Invitation + one reminder |
| `hosting-spec.md` | Requirements for institute (host) + infrastructure (deployment) |
| `research-instruments-umit.md` | Licences/item texts of the published scales, DOIs, SGIC method, UMIT ethics route and contacts |
| `../../scripts/aiw343_analysis.py` | Pre-registered analysis code; tests `scripts/test_aiw343_analysis.py` |
| `../../docs/research/cheap-discriminating-prediction-s358.md` | Derivation (Fable S358): Part 1 = Candidate 1; Part 2 = Prediction 6 leak arm + Candidate 2 |
| `expose-rcseq.md` | Two-page exposé for Michael Netzer (co-investigator ask) and the RCSEQ application |

## MG decisions (S358)
- D1 language: **English first**; DE, IT, FR later.
- D2 recruitment: **MG recruits personally** and obtains employer clearance himself (no Ivoclar routing).
- D3 controller: **MG personally**, now; the Institute hosts as processor.
- ~~D4 UMIT co-investigator: Ass.-Prof. Michael Netzer~~ — **dropped**: no ethics review and no Netzer ask (D-S364-7); UMIT mention removed from the consent text (D-S365-A, 2026-10-28).
- D6 dualism = Riekki 6 + Navarro-Peña 5 → **S361-5: Riekki full 12-item reflective-dualism factor** (Stanovich granted permission 2026-10-25) + Navarro-Peña 5; D7 Stanovich courtesy mail (answered: yes); D8 DABBS now + ask T&F for Templer.
- D5 **no linking code** → Part 1 fully anonymous → RCSEQ shortened procedure; demographics cut to 3 age bands + gender.

## Open before go-live
1. ~~Dualism instrument~~ — DONE S358 (MG D6): Riekki 2013 own 6 items (CC BY) + Navarro-Peña 2026 5 position statements (CC BY 4.0), verbatim in the questionnaire. Stanovich courtesy permission mail = Gmail draft for MG to send (D7). Research: `research-dualism-das.md`.
2. ~~Death anxiety~~ — DONE S364 (D-S363-10): DAP-R Fear of Death subscale, 7 items, 7-point, in master + builder + analysis; `.lss` rebuilt (question IDs after `das` renumbered — re-import if an older build is already on the server). German arm: DAP-GR (CC BY 4.0). Replaces DABBS 1–4 (ND licence blocks German) and Templer DAS (T&F fees).
3. ~~RPBS items~~ — DONE S358: 26 items verbatim in questionnaire-part1.md (source PDF in `sources/`).
4. ~~BFI-10~~ verified S361 (GESIS ZIS 76). O-LIFE UnEx: all 12 verified — `une_11` wording + permission confirmed by Oliver Mason 2026-10-26 (S362).
5. ~~Netzer / RCSEQ ethics application~~ — NOT REQUIRED per MG 2026-10-28 (D-S364-7): anonymous, no intervention, so no ethics-committee review under Austrian law; consent text and closing page say so.
6. ~~Employer clearance~~ — DONE per MG 2026-10-28.
7. ~~Blind-spot SVG for the platform~~ — DONE S361: `blindspot-demo.svg` is inlined by the builder (no external asset); geometry checked (desktop: dot vanishes at ~41 cm; dot 1.6°, gap 2.0°, both inside the ~5°×7° blind spot); a phone hint ("turn it sideways") was added because a portrait phone would need ~11 cm; PNG fallback `blindspot-demo.png` (1600 px).
8. Pilot n ≈ 10 → replaced by a 3-response smoke test on the live server (MG 2026-10-28), then OSF pre-registration with the frozen analysis code.

Sequence: smoke test on the live server → OSF pre-registration → recruitment (Arm C link carries `?src=ppx`; survey closes 15 December 2026) → Part 2 protocol.
