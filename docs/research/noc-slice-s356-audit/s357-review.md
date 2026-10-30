<!-- Action: reference -->
<!-- Tracked-by: AIW-292, AIW-340 -->
# S357 red-team of the NoC-slice spine repair (Fable 5.1, 2026-10-23)

Target: `drafts/aiw130-noc-draft.md` after repair session 1 (commit f0e68aa7). Read-only review; the orchestrator verified the Toker finding against the full text (Europe PMC, PMC8851554) before applying anything.

## Findings applied (S357)
- **Toker et al. 2022 was cited inverted** in §3.2, §3.4 and the Fig 1 caption/alt text (inherited from the pre-S357 draft and from the S356 replacement drafts). The source: waking low-frequency electrodynamics lie on the **chaotic** side of the edge; GABAergic anaesthesia (propofol) goes **deeper into the chaotic** phase; LSD reduces chaoticity (closer to the edge); generalised seizures (2 ECoG + 1 MEG) go into the **periodic/stable** phase. Toker has no ketamine and no sleep data. Toker is on the suggested-reviewer list, so this would have been read by its author.
- Seizure route: direct evidence for both seizure types (Meisel 2012 focal; Toker 2022 generalised → periodic), so it is no longer "unsettled".
- §4 splice corruption (orchestrator's own script error) repaired.
- §5 human behavioural form of the probe dropped: a behaviour predictor cannot be matched on exposure, so the falsifier could never be met.
- Free modelling's third part: "recruitment sustained by its own operation whatever first installed it" (master §3.7.3, engineered recruitment allowed); signature attributed to free modelling, not to capability.
- Universality proofs carry no operating-point condition (not "a broad range").
- Accommodation vs prediction (§3.2), "near-critical by its avalanche statistics" (sleep), hedge consistency on the energy-management mechanism, §8 companion claim narrowed to what the companion reports, §9 "usually present", Ma 2019 "about two days", register fixes (advertised honesty, self-narration, §9 repeating the abstract).
- Optional items taken: §3.2 heading, Langton attribution ("storage and transmission"), salvia dropped from Fig 3, the two banned phrases in the cover-letter block.

## Citations checked as used
Metzinger 2003, Dennett 1991, Siegelmann & Sontag 1995, Maass 1996, Meisel 2012, Meisel 2013, Priesemann 2013. Gruber 2026b echo-state claim supported (companion §4.6, worded "on the ordered side of the measured edge of chaos").

## Gates after
structural (paper) PASS: denial 0.37, ordinal 0.00, callbacks 2.04, scope fences 0.74; 0 register hits, 0 dense windows.
