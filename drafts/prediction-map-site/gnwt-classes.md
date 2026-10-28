# GNWT claim classes, transcribed from the preprint's Figure 3

**Basis: colours transcribed from the preprint's Figure 3.** Not a classification of ours.

The authors' OSF file `JSON MAPS/GNW_network_2026-03-12.json` (sha256 `92233a60…a0c4c`) leaves 43
of its 44 claims uncoloured (`#ffffff`); only the core box is grey (`#ababab`). The preprint's
Figure 3 (p. 14, "GNWT Prediction map") colours every box. This table records the class of each
box as drawn there, read by eye from the figure image embedded in the PDF (1299 x 919 px, cropped
and enlarged), 2026-10-19.

Source: Negro, N., Elbaz, E., Fischer, S., Schreiber, M., & Mudrik, L. (2026). Prediction maps as
a gateway to better understand and test scientific theories. *PsyArXiv*.
https://doi.org/10.31234/osf.io/kqr87_v1, licence CC BY 4.0. PDF: primary file of
`https://api.osf.io/v2/preprints/kqr87/`, download https://osf.io/download/9stmp/
(`Prediction_Maps_FULL_PREPRINT.pdf`, 2,414,545 bytes, sha256
`d4eb67854e8a7404320952622c9bc6f30da8bb3010c8ac2795cb22ca3936ddf7`), saved as
`negro2026-preprint.pdf` in this folder.

## The classes, in the preprint's words

Methods, p. 7: "The maps further distinguish between four classes of claims: cognitive (i.e.,
claims about cognitive/psychological functions; colored in cyan), substrate-general (i.e., claims
about a generally defined “physical substrate”, without assuming that it must be a brain; green),
brain-specific (i.e., claims about the brain and its properties; pink), and extrapolation
(conjectures about the distribution of consciousness in domains beyond that of healthy adult
humans; [...] yellow)." Figure 1a labels the pink class "Neural claims".

Five GNWT boxes are drawn cyan at the top fading to pink at the bottom. The figure legend does
not explain the two-tone boxes; the RPT section (p. 24) names such claims "hybrid claims (i.e.,
including both cognitive and neural aspects)", and the authors' RPT file stores them as two
colours (cyan and pink). They are recorded here as `cognitive+brain-specific`. The core is drawn
black and carries no class.

No GNWT box is green (substrate-general).

## How the page draws them

`scripts/negro2026_maps.py` keeps this table as `GNWT_FIGURE_CLASSES`, writes it into
`negro2026-gnwt.json` under `"added_classes"` (the authors' file under `"map"` stays unchanged)
and records the change in that file's `provenance.changes`. The viewer draws the classes in the
shades of the authors' own IIT and RPT files: cognitive `#84d7cd`, brain-specific `#e7b1d8`,
extrapolation `#e9e0a5`; the core keeps the file's grey. The GNWT title line on the page says
"colours added by us (see sources)". `scripts/test_negro2026_maps.py` checks this table against
the data.

Counts: cognitive 20, cognitive+brain-specific 5, brain-specific 17, extrapolation 1, core 1
(total 44).

## Table

| Claim | Label excerpt (file text) | Class | Basis |
|---|---|---|---|
| A1 | Consciousness is accounted for in functional terms: … | core | Figure 3: black core box |
| B1 | GW operates as information bottleneck: entry is gated (3; 4) | cognitive | Figure 3: cyan |
| B2 | GW is needed to integrate between different modules and … | cognitive | Figure 3: cyan |
| B3 | GW enables maintenance of percepts over time (1) | cognitive | Figure 3: cyan |
| B4 | Attentional processes mobilize information and broadcast … | cognitive | Figure 3: cyan |
| C1 | Attentional gating selects the content of C among … | cognitive | Figure 3: cyan |
| C2 | Information in modules/specialized brain areas outside … | cognitive+brain-specific | Figure 3: cyan over pink |
| C3 | GW can influence UC processes, which are not all fully … | cognitive | Figure 3: cyan |
| C4 | Information outside GW is processed unconsciously by … | cognitive | Figure 3: cyan |
| C5 | UC responses to stimuli are short lived (1) | cognitive+brain-specific | Figure 3: cyan over pink |
| C6 | Items in GW are items in Working Memory (14) | cognitive | Figure 3: cyan |
| C7 | C processes can be long-lived (1) | cognitive+brain-specific | Figure 3: cyan over pink |
| C8 | Mobilization of information into the GW is signalled by … | cognitive+brain-specific | Figure 3: cyan over pink |
| C9 | Top-down selection determines the contents of C (1; 14) | cognitive+brain-specific | Figure 3: cyan over pink |
| C10 | While GW is occupied by competing content X or by … | cognitive | Figure 3: cyan |
| D1 | Inattentional blindness should occur (1) | cognitive | Figure 3: cyan |
| D2 | The GW can integrate only one state (e.g., percept, … | cognitive | Figure 3: cyan |
| D3 | Novel combinations of operations should require C (1) | cognitive | Figure 3: cyan |
| D4 | Top-down attention should be needed for subliminal … | cognitive | Figure 3: cyan |
| D5 | If strong stimuli involving resonant loops within medium … | cognitive | Figure 3: cyan |
| D6 | Incoming information that fails to attain the critical … | cognitive | Figure 3: cyan |
| D7 | No flexible mental chaining without C (7) | cognitive | Figure 3: cyan |
| D8 | No detection of global violations over time without C (6) | cognitive | Figure 3: cyan |
| D9 | No trace conditioning without C (8) | cognitive | Figure 3: cyan |
| D10 | Attention should be able to trigger C perception of a … | cognitive | Figure 3: cyan |
| D11 | Artificial and biological systems that have a … | extrapolation | Figure 3: yellow |
| D12 | Attentional blink should occur (3; 4) | cognitive | Figure 3: cyan |
| E1 | Frontoparietal area, held to be involved in attentional … | brain-specific | Figure 3: pink |
| E2 | Long-axon pyramidal neurons between the GW and the … | brain-specific | Figure 3: pink |
| E3 | Long-range and feedback connections are needed for C … | brain-specific | Figure 3: pink |
| E4 | Neural representations of C percepts should show … | brain-specific | Figure 3: pink |
| E5 | Late activation differentiates between C and UC … | brain-specific | Figure 3: pink |
| E6 | Unless the content of C is actively maintained in WM, … | brain-specific | Figure 3: pink |
| F1 | Decoding of all contents of C should be possible from … | brain-specific | Figure 3: pink |
| F2 | Competing activity in frontal areas prior to stimulus … | brain-specific | Figure 3: pink |
| F3 | UC information should elicit local short-lived neural … | brain-specific | Figure 3: pink |
| F4 | Complexity measures should be higher for C states (14) | brain-specific | Figure 3: pink |
| F5 | C states should be underpinned by prolonged and deeper … | brain-specific | Figure 3: pink |
| F6 | AMPA receptors modulate feedforward connections while … | brain-specific | Figure 3: pink |
| F7 | Activation in sensory areas should include two peaks, … | brain-specific | Figure 3: pink |
| F8 | Critical NCCs should be found during later time window … | brain-specific | Figure 3: pink |
| F9 | Onset/Offset to tag appearance and disappearance of … | brain-specific | Figure 3: pink |
| F10 | T2-induced activation should be limited to a brief … | brain-specific | Figure 3: pink |
| F11 | There should be higher activation (in PFC) and synchrony … | brain-specific | Figure 3: pink |
