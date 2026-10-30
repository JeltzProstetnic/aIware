<!-- Action: reference -->
<!-- Tracked-by: AIW-276 -->
# FMT prediction map: v19 audit of the node texts

**Date:** 2026-10-18 (S338, WSL, subagent). **Map:** `drafts/papers-moc7/fmt-prediction-map.json` (55 nodes, 84 edges).
**Reference:** the FMT v19 master, `paper/full/four-model-theory-full.md` (line numbers below are that file's).
**Checklist used:** `docs/aiw296-wiki-supplement-plan.md` (W01–W37), `.claude/knowledge/fmt-misconception-registry.md`, `.claude/knowledge/neuroscience-communication.md`.

**Verdict:** 45 nodes state v19 correctly, 7 were stale and 3 were wrong; all 10 have been rewritten from the master's wording. The three wrong nodes all carried the retired claim that free modelling plus the architecture suffice for consciousness.

| Count | Nodes |
|---|---|
| **OK** 45 | A1, A2, B1, B2, B3, B4, B7, B8, B9, C1, C2, C5, C7, C8, C9, C10, C11, C12, C13, C14, D1, D2, D3, D4, D6, D7, D9, D10, E1–E9, F1–F7, F9 |
| **STALE** 7 | A3, B6, C3, C4, D11, D5, F8 |
| **WRONG** 3 | B5, C6, D8 |

Key: **WRONG** = the node states something v19 explicitly retracts. **STALE** = the node uses wording v19 replaced, leaves out a v19 change that bears on it directly, or uses banned register. **OK** = consistent with v19, no edit.

## 1. Changed nodes

| ID | Verdict | Old text (short) | Master (v19) | New text |
|---|---|---|---|---|
| **B5** | WRONG (W11) | "…are each necessary and together sufficient for consciousness." | §3.7.3 l.525: "Free modeling is necessary but not sufficient; the four-model architecture is necessary but not sufficient. What is sufficient is a conjunction: a system that implements the four models under closure, with free compute, embodiment and at least one pain-pleasure axis, is conscious." §4.4 l.639 repeats it. | "Each necessary, neither sufficient: free modelling (capability, free instantiation, autonomous recruitment) and the four-model architecture. Sufficient: four models under closure + free compute + embodiment + at least one pain-pleasure axis." `fmt_section` → "§3.7.3; §4.4". |
| **C6** | WRONG (W11) | "given the four-model architecture and free modelling, the material of the substrate is irrelevant…" | §4.4 l.639: "any physical system that meets the sufficient conditions of Section 3.7.3 — the four models under closure, free compute in the Class 4 regime, embodiment, and at least one pain-pleasure axis — is conscious." §3.7.3: "an engineered axis is compatible with substrate independence". | "Substrate independence: any physical system meeting the sufficient conjunction (B5) is conscious, whatever its material; an engineered pain-pleasure axis is compatible." |
| **D8** | WRONG (W11, W12) | "A synthetic system implementing the four-model architecture with free modelling would be conscious." | §3.7.3 l.525 (conjunction; "The pain-pleasure axis may be engineered"). | "A synthetic system meeting the sufficient conjunction of B5 (its pain-pleasure axis may be engineered) would be conscious. Not currently testable." ⚠ The master's own §8.7 l.1009 and §4.4 l.657 still carry the old two-part form (see §3). |
| **A3** | STALE (W15) | "…a real, physical effect on that second level, and it arises exactly where the modelling closes on itself…" | §3 l.138: "Phenomenology is real and physical, and it is that level's modeling closed on itself … The principle is an identity, not a law connecting two things: phenomenality is closure." | "Phenomenology is real and physical, and it is that second level's modelling closed on itself: the self-model and the world-model each entering the other's update rule (self-referential closure). An identity, not a law: phenomenality is closure. Argued for, not derived." |
| **B6** | STALE (W01, W02, W03) | "Consciousness is graded by the depth of recursive self-modelling: basic, simply extended, doubly, triply…" | §3.5 l.393: "A system has phenomenology or it has none … Above that gate, consciousness … is graduated along two axes: richness of content … and depth of recursion … The floor of both axes is called *minimal consciousness*." | "A system has phenomenology or none. Above that, consciousness is graded on two axes, richness of content and depth of recursive self-modelling: minimal (the floor), basic, simply, doubly, triply extended. Points on a continuum, not discrete stages." |
| **C3** | STALE (W08, W09) | "Access and phenomenal consciousness are two level-descriptions of one running process. Present content becomes accessed content by added recursive depth…" | §3.4.6 l.387: "*Accessible* content … is stored on the implicit side, it is not conscious, and it becomes conscious only when a permeability event draws it into the running simulation … For accessed content, access and phenomenal consciousness are two descriptions of the same running process." l.389: "Added recursive depth converts presence into reportability, with no separate broadcasting stage." | "For accessed content (in the running simulation), access and phenomenality are two level-descriptions of one process; accessible content is preconscious until a permeability event. Recursion depth, not a broadcast stage, turns presence into reportability; nothing overflows." |
| **C4** | STALE (W02, W04) | "Basic consciousness: phenomenal experience with only a rudimentary self-model, before first-order self-observation and without global broadcast." | §3.5 l.395–397: minimal = "a rudimentary closure … the present moment together with a primordial pain or a nothingness … no discernible qualia … unreportable by definition"; basic = "above minimal consciousness on the content axis and at the same depth of recursion … reportable only where a recursive rung above it takes that content as an object". §3.4.6: "minimal and basic consciousness … can exist without global broadcasting". | "Minimal and basic consciousness: closure at the lowest recursion depth (minimal: the present moment, no discernible qualia; basic: discernible content). Phenomenal without global broadcast; reportable only via a rung above." |
| **D11** | STALE (W06) | "…systems below closure lack experience regardless of behavioural sophistication." (no floor placement) | §6.4 l.791: "The theory's candidates for this level are fish, amphibians, and possibly insects." l.799: "An insect brain that sustains even a rudimentary closure has at least minimal consciousness." | "…(corvids qualify without a neocortex). Floor candidates: fish, amphibians, possibly insects; below closure, no experience." |
| **D5** | STALE (register) | "Candidate gate: cortico-basal ganglia-thalamo-cortical loops…" | Content matches §9 OQ7 l.1061. `neuroscience-communication.md`: "Never 'gated by' / 'a gate' / 'gating' … Nothing stops any signal from reaching consciousness." | "Candidate mechanism: cortico-basal ganglia-…" (rest unchanged). |
| **F8** | STALE (register) | "If the permeability gate is miscalibrated: …" | Content matches §9 OQ7; same register rule. | "If that selection mechanism is miscalibrated: …" (rest unchanged). |

Lengths (characters, old → new): A3 251 → 269, B5 183 → 241, B6 198 → 248, C3 233 → 274, C4 144 → 223, C6 157 → 168, D5 174 → 179, D8 123 → 146, D11 274 → 278, F8 283 → 286. Six stay within +25. B5, B6, C3 and C4 grew by 40–80 because the v19 content (the four-part conjunction, the gate plus two axes, the accessible/accessed split, the minimal floor) does not fit the old length. All remain below the map's longest node (E5, 444).

### Edge justifications and cross-theory notes changed with them

IDs, endpoints, styles and the edge set are unchanged (verified by script against `HEAD`). Only these text fields changed:

| Edge # | Edge | Old | New |
|---|---|---|---|
| 22 | B6 → C3 | "Interrogable (accessed) content is produced by added recursive depth" | "Reportable content is produced by added recursive depth" (v19: depth gives reportability, not access) |
| 23 | C1 → C3 | "The channel sets breadth, not access" | "…breadth, not reportability" |
| 24 | B6 → C4 | "Basic consciousness is the lowest rung of the ladder" | "Minimal and basic consciousness share the lowest recursion depth of the ladder" |
| 26 | B5 → C6 | "If architecture plus free modelling suffice, nothing in the material is required" | "If the sufficient conjunction names no material, nothing in the material is required" |
| 45 | B7 → D5 | "…the moment-to-moment gating mechanism of permeability" | "…the moment-to-moment mechanism that sets permeability" |
| 46 | C1 → D5 | "A gate on a narrow path is the tractable form of the question" | "A selection mechanism on a narrow path…" |
| 53 | B5 → D8 | "Both thresholds met in silico = sufficient" | "The sufficient conjunction met in silico" |
| 83 | D5 → F8 | "Gate miscalibration mapping" | "Miscalibration mapping" |

Cross-theory links: C4 ↔ GNWT D6 note now reads "minimal and basic consciousness without global broadcast"; D8 ↔ IIT F3 note now reads "a digital implementation meeting the sufficient conjunction (B5) is conscious". Rival node labels quoted from the preprint (e.g. GNWT B1 "entry is gated") were left verbatim.

## 2. Nodes checked and left unchanged

| ID | Master section and quote | Note |
|---|---|---|
| A1 | §3 l.136 "Open-ended computation allows free modeling … Near-criticality is what this looks like in neural tissue"; §3.7 l.448 "Free modeling is necessary and not sufficient" | Says "necessary" and does not claim sufficiency. |
| A2 | §3 l.137 / §3.3 l.240, Principle 2 | Verbatim in substance. |
| B1 | §3.2 l.207–209, 228 "four is the floor, not the ceiling"; scope "is a nesting" | Registry #1 preemption already carried ("not modules"). |
| B2 | §3.2 l.220–226; §3.3 | Constitution, not transfer (registry #2). The S335 "didactic cut" (W31) is not in the master yet, so no change. |
| B3 | §3.4.2 l.289 "qualia are constitutive properties of the computational level" | "absent from the substrate-level description" ≈ master "incoherent at the substrate level". AIW-285 items are on hold (W34). |
| B4 | §3.4.3 l.311–319 (Stages 1–3) | Consistent with the identity reading. |
| B7 | §6.0 l.722 "zero permeability would mean no explicit models … its variability is the default" | — |
| B8 | §6.0 l.724 | — |
| B9 | §6.0 l.720 | — |
| C1 | §3.6.1 l.430–438; §7.2 l.865 "The workspace GNW takes as a primitive is … the occupancy of the low-rank path" | — |
| C2 | §3.6.1 l.438 (Third) | — |
| C5 | §3.4.4 l.355 | — |
| C7 | §6.0 l.726–728 | — |
| C8 | §3.8; §3.5 l.403 | — |
| C9 | §5.1 l.665–669 "binding into a single experiential field … not consistency of that field's contents" | Registry #4. |
| C10 | §3.4.2 l.301; §8.6 | — |
| C11 | §4.2.4; §8.8 l.1021 "closure pays only inside a fit window … ample compute can replace it" | — |
| C12 | §3.7 l.448 "Criticality is neither … Criticality data therefore cannot disconfirm the theory in either direction"; Table 1 Criticality | Matches W23 (signature, not requirement); registry #3. |
| C13 | Table 1 fn c; §3.1.1; registry #5 | Section ref "Table 1 fn 3" kept (the LaTeX build numbers the footnote). |
| C14 | §9 OQ4 l.1049, 1053 "functional selectivity, not the focal excision of a localized module" | — |
| D1 | §3.6.1 l.440 | — |
| D2 | §3.6.1 l.440 (Fourth) | — |
| D3 | §3.6 l.411 | — |
| D4 | §3.6 l.417–418; §6.1–6.2 | Map says "become explicit"; the master's own l.417 still says "become accessible", which collides with the v19 accessible/accessed split (see §3). |
| D6 | §8.4 l.977; Table 1 fn c | — |
| D7 | §8.5 l.987 "the substrate approaches but does not fully reach waking criticality; lucid onset corresponds to the ESM crossing from basic to simply extended consciousness" | Descriptive use of criticality, as the master's. |
| D9 | §4.4 l.657 "What they lack is closure over it, persistence, and the Class 4 regime … architectural mimicry, not self-referential closure" | Registry #6. |
| D10 | §3.7.3 l.527, 531 | — |
| E1 | §8.2 | — |
| E2 | §8.4 | — |
| E3 | §8.5 l.991 "It is a prediction about the signature, so its failure would not by itself disconfirm free modeling." | — |
| E4 | Table 1b "Implicit integrity" | — |
| E5 | Table 1b "Self-ref. closure" (S334 wording, W18) | — |
| E6 | §9 OQ4 | — |
| E7 | §3.6 l.424; Table 1b "Permeability" | — |
| E8 | §3.6.1 l.440 | — |
| E9 | §3.7.3 l.533 | — |
| F1 | §8.3 | — |
| F2 | §8.6 | — |
| F3 | §3.6.1 l.434 | — |
| F4 | §9 OQ4 l.1053 "I claim no priority" | — |
| F5 | §6.0 l.732 | — |
| F6 | Table 1b "Free modeling": "Robust consciousness where a fixed lookup reproduces the system's behavior on novel input" | Matches W22. |
| F7 | §8.9 l.1033 | — |
| F9 | §8.1 l.945; §3.6 l.417 | — |

Also checked: no node defines consciousness as an ability (W10), denies panpsychism (W17), places dreaming in deep NREM (W07), enumerates "four modules", or says "samples".

## 3. Not fixed in the text audit: for MG

**v19 content with no node — RESOLVED 2026-10-19 (MG approved adding all three).** The map now has 59 nodes and 96 edges:
- ~~**White-box trace** (Table 1b row "Consciousness in non-reporting systems", l.201)~~ → **E10** (L4, substrate-general, candidate-test), parents B4, C15, C4.
- ~~**Bridge refuters** (§4.4 l.645)~~ → **F10** functional twin (L5, substrate-general, partially-supported; parents B4, C11) and **E11** the two human refuters (L4, brain-specific, novel-untested; parent B4).
- ~~**What counts as a self model** (§3.4.3 l.325, the SLAM vacuum)~~ → **C15** (L2 auxiliary; parents B4, B1, B5; child C4 via §3.5's floor sentence, and E10).

Two further edges give existing low-PageRank falsifiers the parents the master states: B7 → E1 (§8.2 derivation line) and A1 → F6 (Table 1b free-modelling row). Every centrality value in spec §4 was recomputed with `scripts/prediction_map_centrality.py` (now tracked, with a test that fails while §4 is stale). E3 still tops PageRank (0.033); E10 enters 5th of 59; F6 moves from 50th of 55 to 43rd of 59 and E1 from 30th to 20th. Edges considered and rejected for lack of a stated derivation are listed under spec §2.3.

**One further master inconsistency found while doing this (candidate for AIW-288):** §7 l.917 credits "the redirectable ESM" with the mechanism for Prediction 1 (psychedelics and anosognosia), while §8.2's derivation line runs Principle 2 → permeability → prediction with no redirection step. The map follows §8.2.

**Places where the master contradicts its own v19 changes** (candidates for AIW-288, not edited):
- §8.7 l.1009 and l.1011, §8.8 l.1019, §4.4 l.657: a synthetic four-model system with Class 4 capability "will exhibit consciousness" / "should produce genuine consciousness", the two-part form §3.7.3 retired. D8 now follows §3.7.3, so the map is stricter than §8.7.
- §6.4 l.787 "continuum (not binary)", §1.3 l.62 "graded rather than binary criteria", §6.5 l.818 "a gradient, not a binary": against the one-gate rule of §3.5 l.393 (W01).
- §3.6 l.417 "intermediate processing stages … become accessible to the explicit models" and §8.2 l.955 "psychedelics make the implicit accessible": "accessible" now means preconscious (§3.4.6), the collision W08 flags in the wiki.
- §9 OQ7 l.1061 and §3.6.1 l.440 use "gating" / "a gate on a narrow path", which `neuroscience-communication.md` bans. The map now avoids the word; the master does not.

## 4. Verification

- JSON structure: 55 nodes, 84 edges; node IDs, edge endpoints and styles identical to `HEAD`; top-level keys unchanged.
- Spec `fmt-prediction-map-spec.md` §2.2/§2.3 tables re-synced with the JSON: 0 mismatches across 55 node texts and 84 edge rows.
- Platform file regenerated: `python3 scripts/convert_prediction_map.py` → `fmt-prediction-map.platform.json` (theory=other, 55 nodes, 84 edges).
- `python3 -m pytest scripts/test_convert_prediction_map.py -q`: **18 passed** (same as the baseline before the edits).
- Centrality recomputed with an independent stdlib script (LRC, HC, BC, PR as in spec §1.2): all 220 values match spec §4 to the printed precision. PageRank order unchanged (E3 0.037, then D7 and F2 0.031). Only the node names in the spec's §4 reading were updated.
