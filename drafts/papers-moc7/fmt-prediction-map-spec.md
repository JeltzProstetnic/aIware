<!-- Action: reference -->
<!-- Tracked-by: AIW-276 -->
# FMT prediction map, in the format of Negro et al. (2026)

**Backlog:** `AIW-276`. **Prepared:** 2026-10-16 (Steam Deck 2, subagent). **Status:** draft for MG review. Nothing has been uploaded, submitted or sent anywhere.
**Machine-readable map:** `drafts/papers-moc7/fmt-prediction-map.json` (64 nodes, 101 edges). All tables below are generated from that file.

**Verdict in one sentence:** the programme's format is fully specified in the preprint and FMT fits it cleanly. The JSON follows the paper's ontology; the platform's own file format (React Flow JSON) is now documented in `mudrik-platform-schema.md`, and `scripts/convert_prediction_map.py` generates the upload file `fmt-prediction-map.platform.json` from it.

**v19 audit (2026-10-18):** node texts re-checked against FMT v19 (the master in `paper/full/`); ten node texts, eight edge justifications and two cross-theory notes were updated. Audit table: `fmt-prediction-map-v19-audit.md`.

**v19 additions (2026-10-19, MG-approved):** the three v19 items the audit (§3) found missing were added as four nodes and twelve edges: C15 the self-model criterion (§3.4.3), E10 the white-box trace (Table 1b), E11 and F10 the refuters of the bridge (§4.4). Two existing low-PageRank falsifiers gained the further parents the master states (B7 → E1, A1 → F6). Every centrality value in §4 was recomputed with `scripts/prediction_map_centrality.py`.

**S339 additions (2026-10-19, MG-approved):** E14 (C9-1, misbinding and field unity have separate causes; also approved for the next FMT version) and E15 (C9-2, synchrony as signature; map only), both from C9 (`docs/c9-binding-evidence.md`). C9 is no longer idle. **S338 additions (2026-10-19, MG-approved; not yet in the FMT master):** three proposed predictions for two claims that had none, from `docs/proposed-predictions-c5-c8-c9.md`: E12 frame-like experience tracking a shorter neural autocorrelation window (C5-1), E13 the in-silico echo cut (C5-2), F11 the simulated generation display with its uninterpretable fourth arm (C8-1). Three edges: C5 → E12, C5 → E13, C8 → F11. They carry the status `proposed`, a `proposed` field and the text tag "Proposed S338, not yet in the FMT master". C9 (binding) is deferred and stays a leaf. The collicular route is not a node; it is falsifier (c) of E12. All values in §4 were recomputed.

---

## 1. The programme's format: what was established, and from where

Source: `docs/moc7/negro-2026-prediction-maps.txt`, the text extraction of Negro, Elbaz, Fischer, Schreiber & Mudrik (2026), *Prediction maps as a gateway to better understand and test scientific theories*, PsyArXiv, doi 10.31234/osf.io/kqr87_v1. Page numbers are the preprint's own.

### 1.1 Map ontology

| Element | What the paper specifies | Where |
|---|---|---|
| Underlying model | A theory is a Lakatosian network of beliefs: a core plus levels of auxiliary hypotheses. The auxiliaries make the core testable and also shield it from falsification. | pp. 2–3 |
| Core | "We structured each map around a core claim, representing the principal idea of the theory." A core may hold more than one box: IIT's core is A1 (axioms) = A2 (postulates). | pp. 6, 17 |
| Levels | Five levels of auxiliary hypotheses (L1–L5), each further specifying the previous one. L1 unpacks the core, L2 develops L1, and so on. | pp. 6–7, Fig. 1c |
| Level layout by theory type | **Cognitive-core theories** (GNWT, RPT, PRM): L3 = cognitive predictions, L4 = neural implementation, L5 = neuroscientific predictions. **Substrate-general-core theories** (IIT): L3 = brain-specific claims, L4 = neuroscientific predictions, L5 = cognitive predictions. | p. 7 |
| Claim classes (colours) | cognitive (cyan); substrate-general (green, a "physical substrate" not assumed to be a brain); brain-specific (pink); extrapolation (yellow: consciousness beyond healthy adult humans, e.g. animals, AI). RPT's L1 also carries "hybrid" cognitive+neural claims. | p. 7, Fig. 1a; p. 24 |
| Node labels | Letter = level (A core, B = L1, C = L2 …); number runs clockwise from the top-left box of each level. Labels carry **no** logical information; only the arrows do. Each claim carries numbered references to a per-theory bibliography (Table 1). | p. 13 |
| Edges | One relation type: a generic **"in virtue of"** dependence, logical but not necessarily deductive. **Solid arrow** = between levels; **dashed arrow** = within a level. Direction: from the claim that grounds to the claim that follows ("C4 can lead to C3, in which case an arrow will go from the former to the latter"). | p. 8, Fig. 1b; p. 13 |
| Mutually exclusive paths | HOROR's map uses different-coloured arrows from one box to mark mutually exclusive paths. This is a supplement-only convention. | Fig. S3.2 |
| "Prediction" | Any empirical statement logically derived from upstream claims. The maps do not separate prediction from accommodation; the authors list this as a limitation. | p. 31 |
| Completeness | Hidden background auxiliaries are left out (e.g. "the brain is the organ that sustains the cognitive function"). | p. 13 |
| Validation | Maps built by several modellers, iterated to consensus, then revised over several rounds with the theory's proponents. | pp. 4–6, 8, 27 |

### 1.2 How centrality is computed

Four node-level measures (pp. 8–12, Fig. 2), all on the directed graph:

- **Local Reaching Centrality (LRC)** = the share of the other nodes reachable from the node (Mones et al. 2012). Downstream breadth.
- **Harmonic Centrality (HC)** = the sum of 1/shortest-path-length to every reachable node, normalised by the maximum possible number of reachable nodes. Downstream breadth weighted by closeness.
- **Betweenness Centrality (BC)** = the share of shortest paths between other pairs that pass through the node (Freeman 1977). The node as a "logical bridge".
- **PageRank (PR)** with damping d = 0.85 (Brin & Page 1998). Importance inherited from parents. The paper uses it as the "high-stakes prediction" measure: "challenging predictions with high PR reverberates directly to other highly influential upstream claims."

Reporting convention: per theory, the 90th percentile, median and 10th percentile of each measure (Table S1.17), and node values quoted against them. Example on p. 28: "LRC 0.241; 90th percentile 0.248; median 0.017". The analysis code "is available and added as supplemental resource" (p. 13).

### 1.3 Shared versus unique predictions

**The paper does not weight shared against unique predictions.** Every measure is within-network. Shared ground between theories is handled in two ways:

1. **Convergence points.** One claim is mapped in each theory, and its centrality is compared across the two theories. The worked example is NMDA receptors: a hub for RPT (E1), around the median for GNWT (F6) (p. 28).
2. **Evaluating tests.** The PageRank of the nodes an adversarial collaboration actually tested tells you whether the test was central to each theory. Cogitate: IIT's E10 had the highest PR on the IIT map, while the GNWT predictions tested were medium (pp. 29–30; S2 does the same for INTREPID and ETHOS).

Novelty, boldness and precision are named as further dimensions of informativeness, but are explicitly **outside** the method (p. 30, Fig. 7). Shared/unique is therefore **extra information** in this spec, not part of the programme's format. It is what an FMT map adds when it is compared with the published maps.

### 1.4 The platform's file format

**Resolved 2026-10-18.** The format is documented in `drafts/papers-moc7/mudrik-platform-schema.md`, read from the app's own source (`src/App.tsx`, `exportNetwork`/`importNetwork`) in a headless browser and confirmed with a live Download. In short: a map file is React Flow JSON with the top-level keys `theory`, `nodes`, `edges`, `exportDate`, `version`; a node carries its claim in `data.label` and its colour(s) in `data.colors`; an edge is an untyped `source` → `target` arrow. The app has no fields for level, claim class, references or solid/dashed, so those survive only as column position, colour, the label's "(refs)" suffix and an SVG dash style (losses listed in the schema note, §3).

`fmt-prediction-map.json` stays the source file. `python3 scripts/convert_prediction_map.py` writes `fmt-prediction-map.platform.json`, which loaded in the app with all 55 nodes and 84 edges of the pre-addition map and survived a Download round trip (the 59-node version: §4, end). Rerun it after any change to the map; `scripts/test_convert_prediction_map.py::test_output_file_is_current` fails while the output is stale.

The earlier attempts, kept for the record (Steam Deck 2, 2026-10-16):

| Source | Attempt | Result |
|---|---|---|
| OSF supplement `osf.io/9xug8` | `api.osf.io/v2/nodes/9xug8/files/osfstorage/` via curl (IPv4 and default) and WebFetch; `osf.io/9xug8/files` via WebFetch | curl timed out; WebFetch got HTTP 500 and connection refused. **Nothing downloaded**; `scratchpad/osf9xug8/` is empty. |
| CodeSandbox source `xk29y8` | `codesandbox.io/api/v1/sandboxes/xk29y8` (+ `/sandpack`), `codesandbox.io/s/xk29y8` | HTTP 403 (Cloudflare "Just a moment…" challenge). |
| The app `xk29y8.csb.app` | GET `/`, `/package.json`, `/src/App.js` | 200, but every path returns the same 3 KB Create-React-App shell. The app is bundled client-side by CodeSandbox's `sandbox-startup.js`, which fetches the sources from the blocked API. |
| Headless browser | Playwright MCP | No Chromium installed on Steam Deck 2 (known quirk). |

The CodeSandbox API that returned 403 to curl was later reached as a network response of the running app in a headless browser; that is how the schema above was read.

---

## 2. The FMT map: design decisions

1. **Layout = the substrate-general (IIT-type) layout.** FMT's three principles are about a computational substrate, not about the brain, which puts it with IIT and not with GNWT/RPT/PRM. Accordingly: L1–L2 mostly substrate-general; L3 brain-specific implementation claims and the extrapolations; L4 neuroscientific predictions; L5 cognitive/behavioural predictions. Some L2 claims are already brain-specific (C12 criticality signature, C13 localisation asymmetry). The paper allows this: class and level are independent axes.
2. **Three core boxes, A1 → A2 → A3, joined by dashed same-level arrows.** This follows IIT's two-box precedent and the master's own statement that the theory "rests on three principles" (§3), each grounding the next. **MG option:** collapse them into one A1 ("consciousness is the closure of a self-model with a world-model on a second computational level of a freely-modelling substrate"). Centrality would barely change, because the core reaches everything either way.
3. **Only the master's derivations become edges.** Every edge cites the section where the master derives it (§6.0 and the "Derivation:" lines of §8.2–8.6 supply most of them). No edge was invented to raise a node's centrality.
4. **Constraints applied (misconception registry, prediction framing):**
   - **Two kinds of models, not four modules** (B1).
   - **Constitution, not transfer** (B2; "transfer" is used only for permeability, B7).
   - **Criticality is a signature, never a requirement.** It sits at L2 (C12), *downstream* of free modelling, and every criticality prediction is marked "cannot disconfirm A1".
   - **Closure is an efficiency advantage in a cost window, not a capability necessity** (C11, F7).
   - **Binding is dissolved** (C9).
   - **Explicit models are not localisable** (C13, D6).
   - **Corroborations are kept apart from novel predictions** (`status` field).
   - The sleep-criticality convergences (Xu 2024, Li 2025) are **left out**. They test the signature only and would add criticality nodes that cannot bear on the core.
5. **Things deliberately not mapped:** §4 philosophy (free will, process physicalism), cosmology, RIM, the five-system hierarchy beyond C13/D2, the illusionism contrast (an ontological dispute with no empirical test, per brief C6). These are not "predictions" in the programme's sense.

### 2.1 Bibliography (per-theory numbered list, as in the paper's Table 1)

1. Gruber (2015), *Die Emergenz des Bewusstseins*.
2. Gruber (2026), FMT master, Zenodo concept DOI 10.5281/zenodo.18669891.
3. Gruber (2026d), in-silico companion, doi 10.5281/zenodo.21610993.
4. Katlowitz et al. (2026), *Nature*.
5. Boly et al. (2012), *J Neurosci*.
6. Rouault et al. (2018); Rahnev et al. (2020).
7. Kawakita et al. (2025), *iScience*.
8. Tzioridou et al. (2026), PsyArXiv.
9. Mago et al. (2025), arXiv.
10. Tsuchiya et al. (2015); Nakamura, Michel & Lau (2026).

All of these are already in the master reference list. Full citations are in the JSON.

### 2.2 Nodes (64)

Kinds: 3 core, 35 auxiliary (incl. 4 extrapolations), 26 predictions. Prediction status: 8 novel-untested, 5 corroborated, 4 partially supported, 3 candidate tests, 5 proposed (S338/S339, not yet in the master), 1 candidate (OQ7).

| ID | Level | Class | Kind | Status | Claim | FMT § | Refs |
|---|---|---|---|---|---|---|---|
| **A1** | core | substrate-general | core | principle | Free modelling: open-ended (Class 4-capable) computation, recruited by an autonomous system for its own modelling, is necessary for consciousness. Near-criticality is the signature it leaves in neural tissue, not the principle. | §3 Principle 1; §3.7; §3.7.3 | 1, 2 |
| **A2** | core | substrate-general | core | principle | Recurrent non-linear dynamics of sufficient complexity host a second computational level: persistent activity patterns that interact and compute over one another, individuated by their mutual effects rather than by the units that carry them. | §3 Principle 2; §3.3 | 1, 2 |
| **A3** | core | substrate-general | core | principle | Phenomenology is real and physical, and it is that second level's modelling closed on itself: the self-model and the world-model each entering the other's update rule (self-referential closure). An identity, not a law: phenomenality is closure. Argued for, not derived. | §3 Principle 3; §3.4.3 | 1, 2 |
| **B1** | L1 | substrate-general | auxiliary | derived | Any conscious system must model world and self, each at a stored (implicit) and a generated (explicit) level: two kinds of model on two axes (IWM, ISM, EWM, ESM). Scope is a nesting (ESM within EWM); four is the minimum, not the count, and the four are not modules. | §3.2 | 1, 2 |
| **B2** | L1 | substrate-general | auxiliary | derived | Real/virtual split: the implicit models are stored in substrate connectivity and are never directly conscious; the explicit models are generated from (constituted by) them plus current input. Constitution, not data transfer. | §3.3 | 1, 2 |
| **B3** | L1 | substrate-general | auxiliary | derived | Qualia are level-constitutive properties of the running explicit models: real at the computational level, absent from the substrate-level description. | §3.4.1-3.4.2 | 1, 2 |
| **B4** | L1 | substrate-general | auxiliary | derived | Self-referential closure is what distinguishes conscious from non-conscious computation: a simulation that is merely monitored or broadcast, without closure, has no inside. | §3.4.3 | 2 |
| **B5** | L1 | substrate-general | auxiliary | derived | Each necessary, neither sufficient: free modelling (capability, free instantiation, autonomous recruitment) and the four-model architecture. Sufficient: four models under closure + free compute + embodiment + at least one pain-pleasure axis. | §3.7.3; §4.4 | 2 |
| **B6** | L1 | substrate-general | auxiliary | derived | A system has phenomenology or none. Above that, consciousness is graded on two axes, richness of content and depth of recursive self-modelling: minimal (the floor), basic, simply, doubly, triply extended. Points on a continuum, not discrete stages. | §3.5 | 1, 2 |
| **B7** | L1 | substrate-general | auxiliary | derived | Some implicit-to-explicit permeability is forced (zero permeability = no explicit models) and its variability is the default: permeability is a family of modulable boundary properties with local and global modes. | §3.6; §6.0 | 1, 2 |
| **B8** | L1 | substrate-general | auxiliary | derived | Forking: because the explicit level is computationally open-ended, several self-model configurations (and offline runs such as recall or modelling another agent) can run on one substrate. | §6.0 | 2 |
| **B9** | L1 | substrate-general | auxiliary | derived | Redirection: the explicit self-model is an input-driven generator; when its normal self-referential input is disrupted it latches onto whatever input dominates. | §6.0 | 2 |
| **C1** | L2 | substrate-general | auxiliary | derived | The explicit models read and write the high-dimensional implicit models through a low-rank channel. The channel's current occupancy is the working model (Arbeitsmodell) = working-memory content = the global workspace; it is not what constitutes experience. | §3.6.1 | 1, 2 |
| **C2** | L2 | cognitive | auxiliary | derived | Arousal sets the channel's capacity, attention selects its occupancy, working memory is that occupancy. Attention is selection into the channel; closure is the pass back over what it holds, so the two dissociate. | §3.6.1 | 2 |
| **C3** | L2 | cognitive | auxiliary | derived | For accessed content (in the self-model's closed loop), access and phenomenality are two level-descriptions of one process; accessible content, implicit or explicit, is preconscious until it enters that loop. Recursion depth, not a broadcast stage, turns presence into reportability; nothing overflows. | §3.4.6; §3.6.1 | 2 |
| **C4** | L2 | cognitive | auxiliary | derived | Minimal and basic consciousness: closure at the lowest recursion depth (minimal: the present moment, no discernible qualia; basic: discernible content). Phenomenal without global broadcast; reportable only via a rung above. | §3.5; §3.4.6 | 1, 2 |
| **C5** | L2 | substrate-general | auxiliary | derived | Temporal echo: recursion under closure smears content over time, and this smearing constitutes experienced temporal flow. | §3.4.4 | 1, 2 |
| **C6** | L2 | substrate-general | auxiliary | derived | Substrate independence: any physical system meeting the sufficient conjunction (B5) is conscious, whatever its material; an engineered pain-pleasure axis is compatible. | §4.4 | 2 |
| **C7** | L2 | cognitive | auxiliary | derived | Source distinguishability: composing the explicit models must not destroy the distinguishability between live and offline (forked) runs that the source pathways carry. No reality tag is posited; source attribution is the fragile term. | §6.0 | 2 |
| **C8** | L2 | cognitive | auxiliary | derived | Meta-problem: the explicit self-model cannot model its own generating substrate, which produces the intuition that consciousness is mysterious (a triply-extended operation). | §3.8 | 2 |
| **C9** | L2 | substrate-general | auxiliary | derived | Binding is dissolved, not solved: the model kinds are poles of one shared substrate and its dynamics, so no separate binding mechanism is needed (one field, not necessarily consistent contents). | §5.1 | 2 |
| **C10** | L2 | substrate-general | auxiliary | derived | The relational structure of a qualia space is a relational invariant shareable across individuals; the absolute substrate state realizing a quale is idiosyncratic and is transferred only by instantiation, never by description. | §3.4.2; §8.6 | 2 |
| **C11** | L2 | substrate-general | auxiliary | derived | Closure is an efficiency advantage inside a cost window, not a capability necessity: it pays where a system must model many model-bearing agents and itself in an open-ended environment, and ample compute can replace it on bounded problems. | §4.2.4; §8.10; §8.11 | 2, 3 |
| **C12** | L2 | brain-specific | auxiliary | derived | In neural tissue free modelling usually shows as a near-critical signature (sigma ~ 1, DFA alpha 0.6-0.9, power-law avalanches). The signature is contingent: neither necessary nor sufficient for consciousness, so criticality data cannot disconfirm A1 in either direction. | §3.7; Table 1 | 2 |
| **C13** | L2 | brain-specific | auxiliary | derived | Localization asymmetry: implicit models localize to structural connectivity; explicit models are distributed, transient dynamics that are not localizable to a region. | §3.1.1; Table 1 fn 3 | 2 |
| **C14** | L2 | substrate-general | auxiliary | derived | The explicit self-model and the explicit world model are architecturally separable model kinds and should be independently disruptable (functional selectivity, not focal modules). | §9 OQ4 | 2 |
| **C15** | L2 | substrate-general | auxiliary | derived | What counts as a self model: a model of the system itself, however simple, representing its states, geometry and capabilities in proportion to what the system has. A position estimate alone is not one: a SLAM robot vacuum fails (its 'self' is a position, no implicit/explicit split, a fixed algorithm, no free compute recruited). | §3.4.3 (what counts as a self model); §3.5 | 2 |
| **D1** | L3 | brain-specific | auxiliary | candidate | In cortex the thalamocortical relay is the leading realizer candidate for the low-rank channel; it is not the only one (olfaction reaches cortex without a thalamic relay and is conscious). | §3.6.1 | 2 |
| **D2** | L3 | brain-specific | auxiliary | derived | General anaesthesia abolishes experience by channel failure while the wired (implicit) layer stays intact. | §3.6.1; §3.3 | 2 |
| **D3** | L3 | brain-specific | auxiliary | derived | In brains, permeability is set by neuromodulatory systems (serotonergic, GABAergic, dopaminergic and others), varying independently across sensory channels, regions and histology. | §3.6 | 2 |
| **D4** | L3 | brain-specific | auxiliary | derived | Psychedelics raise permeability globally (intermediate processing stages become explicit); anosognosia is a local permeability block (the ISM holds the deficit, the ESM does not receive it). | §3.6; §6.1; §6.2 | 1, 2 |
| **D5** | L3 | brain-specific | auxiliary | candidate | Candidate mechanism: cortico-basal ganglia-thalamo-cortical loops evaluate candidate model updates against dopaminergic prediction error before they enter the explicit simulation. | §9 OQ7 | 2 |
| **D6** | L3 | brain-specific | auxiliary | derived | Self-model differences concentrate along a self-referential-to-sensorimotor gradient of cortical processing; default-mode co-activation is a correlate, not a localization of the ESM. | §8.1; §8.4; Table 1 fn 3 | 2 |
| **D7** | L3 | brain-specific | auxiliary | derived | In REM sleep the substrate approaches but does not reach waking criticality; lucid onset is the ESM crossing from basic to simply extended consciousness. | §8.5 | 2 |
| **D8** | L3 | extrapolation | auxiliary | derived | A synthetic system meeting the sufficient conjunction of B5 (its pain-pleasure axis may be engineered) would be conscious. Not currently testable. | §8.9; §8.10 | 2 |
| **D9** | L3 | extrapolation | auxiliary | derived | Current LLMs, including scaffolded agent loops with memory, are not conscious: they lack self-referential closure, self-produced update of their implicit models and autonomous recruitment of open-ended computation (a globally available, reportable workspace without closure is mimicry). | §4.4; §7.2 | 2 |
| **D10** | L3 | extrapolation | auxiliary | derived | A Turing-universal but heteronomous system (externally clocked and programmed, e.g. a laptop) is not conscious: nothing recruits its universality for autonomous self-modelling. | §3.7.3 | 2 |
| **D11** | L3 | extrapolation | auxiliary | derived | Animal consciousness forms a gradient set by whether an organism sustains self-referential simulation through free modelling, not by phylogeny or behaviour (corvids qualify without a neocortex). Floor candidates: fish, amphibians, possibly insects; below closure, no experience. | §6.4 | 2 |
| **E1** | L4 | brain-specific | prediction | novel-untested | Psychedelics at sub-ego-dissolution doses improve explicit awareness of deficits in anosognosia, dose-dependently and temporarily, correlated with complexity increases over the lesioned hemisphere; strongest in disconnection-type, absent in destruction-type cases. | §8.2 (Prediction 1) | 2 |
| **E2** | L4 | brain-specific | prediction | novel-untested | In dissociative identity disorder, representational dissimilarity between alter states is greater in self-referential than in sensorimotor processing (a gradient), alter-specific, reproducible, and distinct from role-play controls. | §8.4 (Prediction 3) | 2 |
| **E3** | L4 | brain-specific | prediction | novel-untested | Verified lucid-dream onset shows phase-transition dynamics (critical slowing, discontinuous onset) originating in self-model networks before spreading. A signature prediction: its failure falsifies D7/C12, not A1. | §8.5 (Prediction 4) | 2 |
| **E4** | L4 | brain-specific | prediction | corroborated | Processing guided by the implicit models (e.g. hippocampal semantic parsing, word prediction, representational plasticity) continues under consciousness-abolishing anaesthesia while the explicit models are suppressed. Disconfirmer: implicit learning abolished at BIS 40-60. | Table 1b (implicit integrity) | 2, 4 |
| **E5** | L4 | brain-specific | prediction | candidate-test | Disrupting the self-modelling loop itself (targeted disruption beyond metacognitive read-out, decision criteria held fixed, no-report designs; in silico closure-on/off ablation) degrades experience, not merely report or confidence. Falsifier: loop disruption leaves no-report markers of experience intact. Metacognitive disruption alone does not test closure (FMT predicts experience survives it; report may fail via long-term memory transfer). | Table 1b (self-referential closure) | 2, 10 |
| **E6** | L4 | brain-specific | prediction | novel-untested | A causal perturbation can degrade the explicit self-model while sparing the explicit world model, and the converse (selective ESM disruption ~ depersonalization; selective EWM disruption ~ fragmented world with intact self). | §9 OQ4 | 2 |
| **E7** | L4 | brain-specific | prediction | novel-untested | Permeability rises monotonically with 5-HT2A agonism (3+ dose levels; Lempel-Ziv complexity, 5D-ASC, content transfer), and global (psychedelic) and local (anosognosia) permeability changes have distinguishable neural signatures. | §3.6 (falsifiability constraints); Table 1b | 2 |
| **E8** | L4 | brain-specific | prediction | corroborated | Thalamocortical effective connectivity breaks down at propofol-induced loss of consciousness, with structural connectivity preserved. | §3.6.1 | 2, 5 |
| **E9** | L4 | brain-specific | prediction | corroborated | States intensifying phenomenal self-modelling (meditative absorption, jhana) shift cortical dynamics toward the near-critical signature. Signature-level: cannot disconfirm A1. | §3.7.3 | 2, 9 |
| **E10** | L4 | substrate-general | prediction | candidate-test | White-box trace: in inspectable systems (connectome, weights, running dynamics), an input traced to a self-model component that enters the world model's update rule and is entered by it marks consciousness, reportable or not (the non-report signature of minimal consciousness). Falsifier, where such systems also report: a traced signal reaching the closed self and world models without no-report markers of experience of it, or such markers for a signal never reaching the self model. | Table 1b (consciousness in non-reporting systems); §3.5 | 2 |
| **E11** | L4 | brain-specific | prediction | novel-untested | Human refuters of the bridge (phenomenality is closure): content traced into the closed self and world models while every no-report marker and the later report show no experience of it; or robust no-report markers of experience where closure is absent. The second is hard to establish in vivo: opening the loop in one place relocates it. | §4.4 (refuters of the bridge) | 2 |
| **E12** | L4 | brain-specific | prediction | proposed | Shortening the temporal echo makes experience frame-like ('single frames, single thoughts, step by step') in every modality and in thought together, and the size of the frame-like report covaries with the shortening of the neural autocorrelation window (ACW, resting and task EEG/MEG). Test: placebo-controlled THC, two doses, crossover, eye tracking; TMS over V5 as a vision-only control with no global ACW change. Falsifier: frame-like reports without ACW shortening; ACW shortening without frame-like reports; or reports confined to vision or locked to saccades (the collicular route). Discrete-perception accounts tie frames to a slower perceptual cycle (alpha peak frequency down); FMT predicts alpha frequency need not move. Proposed S338, not yet in the FMT master. | §3.4.4 (temporal echo); proposal C5-1 in docs/proposed-predictions-c5-c8-c9.md | 2 |
| **E13** | L4 | substrate-general | prediction | proposed | In-silico echo cut: in a closed architecture whose self-model no longer receives its own state from the previous frame (within-frame closure kept), the self-model loses its representation of its own elapsed time and of the order of its own past states, while the world model's representation of external time survives. Three arms: closure + echo, closure + echo cut, recurrence without closure; linear decoding from self-model versus world-model units, plus a report of own elapsed time. Falsifier: the echo-cut arm decodes its own elapsed time from self-model units as well as the full arm does. Tests representation, not experience. Proposed S338, not yet in the FMT master. | §3.4.4 (temporal echo); proposal C5-2 in docs/proposed-predictions-c5-c8-c9.md | 2 |
| **E14** | L4 | brain-specific | prediction | proposed | Misbinding and field unity have separate causes: a focal manipulation of feature binding (right intraparietal rTMS, attention load) shifts guessing-corrected conjunction errors without changing the unity of each object and scene or global complexity markers; graded propofol sedation degrades the whole field without raising conjunction errors at matched feature accuracy, and never yields features experienced outside one field. Proposed S339, not yet in the FMT master. | §5.1 (binding); proposal C9-1 in docs/proposed-predictions-c5-c8-c9.md | 2 |
| **E15** | L4 | brain-specific | prediction | proposed | Synchrony is a signature, not the pairing mechanism: in-phase versus anti-phase gamma stimulation (tACS) between colour- and form-coding cortex at matched arousal changes detection and clarity, not which features are paired; refuted if anti-phase raises conjunction errors at matched feature accuracy. Proposed S339, not yet in the FMT master. | §5.1 (binding); proposal C9-2 in docs/proposed-predictions-c5-c8-c9.md | 2 |
| **F1** | L5 | cognitive | prediction | novel-untested | During ego dissolution under salvinorin A, the reported identity content ('what I became') tracks the most salient content in the environment, even content with no contingency with the subject's heartbeat, breathing or movement; controlling what is salient predicts and directs it. | §8.3 (Prediction 2) | 2 |
| **F2** | L5 | cognitive | prediction | partially-supported | Within a modality, unsupervised label-free alignment of qualia-similarity structures generalizes across individuals, while a decoder of one brain's absolute realizing state fails on another's. The committed claim is the dissociation. | §8.6 (Prediction 5) | 2, 7 |
| **F3** | L5 | cognitive | prediction | novel-untested | Working-memory capacity co-varies with the rank of the read/write channel and not with neuron count or brain volume; capacity scaling with brain volume across species would falsify the derivation. | §3.6.1 | 1, 2 |
| **F4** | L5 | cognitive | prediction | corroborated | Metacognitive efficiency (M-ratio, read-out by the self-model) is largely decoupled from first-order sensitivity (d', world-model discrimination). No priority claimed for the regularity. | §9 OQ4 | 2, 6 |
| **F5** | L5 | cognitive | prediction | partially-supported | Under perturbation of the substrate or of communication between levels, source attribution degrades before phenomenal experience does: dreaming is experience without source attribution, and dream recall frequency predicts dream-reality confusion. | §6.0 | 2, 8 |
| **F6** | L5 | cognitive | prediction | candidate-test | Novel-input probe: a fixed lookup fitted to a system's past input-output behaviour fails on novel input wherever the system is conscious. Disconfirmer of A1: robust consciousness where a fixed lookup reproduces behaviour on novel input. | Table 1b (free modelling) | 2 |
| **F7** | L5 | substrate-general | prediction | partially-supported | In model systems, the advantage conferred by explicit self-modelling is small on simple individual tasks and grows steeply with task sociality and compositional depth (efficiency at matched budget, not capability necessity). | §8.11 | 2, 3 |
| **F8** | L5 | cognitive | prediction | candidate | If that selection mechanism is miscalibrated: too permissive gives positive symptoms, too conservative negative symptoms, noisy cognitive symptoms; 5-HT2A agonists should disrupt salience filtering, measurable as reward-valence violations in ratings of psychedelic imagery across doses. | §9 OQ7 | 2 |
| **F9** | L5 | cognitive | prediction | corroborated | Rising permeability exposes intermediate processing stages in hierarchical order: phosphenes and form constants, then complex imagery, then dream-like scenes (psychedelics, hypnagogia). | §8.1; §3.6 | 1, 2 |
| **F10** | L5 | substrate-general | prediction | partially-supported | Functional-twin refuter of the bridge, tested in silico: no return-free system reproduces every function attributed to phenomenality (reports of presence, opacity about its own processing, reports of ineffability, flexible behaviour guided by valence) within the same resource bound as the closed system. Measured so far: return-freedom costs 71.5-74.0% of a model connectome, five to six times what relocating closure costs. | §4.4 (primary refuter); §8.11 (fifth result) | 2, 3 |
| **F11** | L5 | cognitive | prediction | proposed | Simulated generation display: a display of a plausible build-up of 'your processing', contingent on and preceding the participant's own percept or decision, lowers reported mystery about that experience, whether or not the display is veridical. A fourth arm, a contingent and preceding but uninterpretable display (a leak analogue), leaves mystery unchanged or raises it. Arms: preceding display; the same display mistimed or uncorrelated; no display; uninterpretable display; a veridical sub-arm uses a real-time readiness-potential BCI. Falsifier: no drop relative to the mistimed display at matched belief in it; the veridical display beats the fake one; or the leak arm lowers mystery as much as the coherent display. Proposed S338, not yet in the FMT master. | §3.8 (meta-problem); §3.4.3; proposal C8-1 in docs/proposed-predictions-c5-c8-c9.md | 2 |

**Placement of the v19 additions.** C15 is a theoretical claim, so it sits at L2 with C4 and the other developments of L1; it is the criterion, not a test. E10 is a prediction about traced internal dynamics, so L4; its class is substrate-general because the master applies it "now to artificial systems, and to nervous systems as they become inspectable". The bridge refuters split by where they can be run: the two human refuters are one brain-specific L4 node (E11); the functional twin is an in-silico, behavioural-functional prediction, so L5 next to F7, which rests on the same §8.11 programme.

**Placement of the S338 additions.** The proposal document ranks C8-1 as one candidate, so the simulated display, its mistimed control, the veridical sub-arm and the fourth (uninterpretable, leak-analogue) arm are one node, F11: a cognitive/behavioural prediction measured by report, L5. E12 is a neuroscientific prediction (the ACW is its committed measure), brain-specific, L4. The proposal placed E13 at "L2/L3 substrate-general"; the method puts predictions at L4/L5 in this layout (§1.1, p. 7), so E13 sits at L4, substrate-general, next to E10, the other prediction read off inspected internal dynamics. Uniqueness follows the proposal: E12 contested (discrete perception predicts a slower alpha cycle; FMT predicts a shorter ACW with alpha unmoved), E13 unique (rivals silent), F11 shared in part (AST shares the explanation, not the predicted effect of the manipulation).

### 2.3 Edges (101, all of type "in virtue of")

| # | From | To | Style | Justification |
|---|---|---|---|---|
| 1 | A1 | A2 | dashed | Principle 2's 'sufficient complexity' is defined as sufficient to be in the regime named by Principle 1 (§3). |
| 2 | A2 | A3 | dashed | Principle 3 locates phenomenology 'on that level', the second level of Principle 2 (§3). |
| 3 | A2 | B1 | solid | The four model kinds are the minimum that Principles 2 and 3 jointly force (§3, §3.2). |
| 4 | A3 | B1 | solid | Closure needs a self-model and a world-model that enter each other's update rule (§3.2). |
| 5 | A2 | B2 | solid | The second level is generated by the substrate, as software is constituted by hardware (§3.3). |
| 6 | B1 | B2 | dashed | The implicit/explicit axis of the 2x2 is the stored/generated distinction (§3.2-3.3). |
| 7 | A3 | B3 | solid | Qualia are the phenomenology of Principle 3, located at the computational level (§3.4.1-3.4.2). |
| 8 | B2 | B3 | dashed | Level-constitutive properties presuppose the real/virtual level distinction (§3.4.1). |
| 9 | A3 | B4 | solid | Closure is the bridging commitment itself, unpacked as the conscious/non-conscious criterion (§3.4.3). |
| 10 | A1 | B5 | solid | First threshold = free modelling (§3.7.3). |
| 11 | B1 | B5 | dashed | Second threshold = the four-model architecture (§3.7.3). |
| 12 | A3 | B6 | solid | Levels are added layers of recursion of the closing self-model (§3.5). |
| 13 | B1 | B6 | dashed | The ladder is defined over the explicit self-model (§3.5). |
| 14 | A2 | B7 | solid | A second level generated from the substrate forces some transfer across the boundary (§6.0). |
| 15 | B2 | B7 | dashed | Permeability is how readily implicit content is drawn into generating the explicit models (§3.6). |
| 16 | A1 | B8 | solid | Forking follows from Principle 1 directly: an open-ended level can host several self-model configurations (§6.0). |
| 17 | A3 | B9 | solid | Redirection follows from Principles 2 and 3 with the ESM's generative character (§6.0). |
| 18 | B2 | B9 | dashed | The ESM is generated from input, not stored, so it requires input to run (§3.2, §6.0). |
| 19 | B2 | C1 | solid | The explicit models read and write the implicit ones; the dimensional mismatch makes the path low-rank (§3.6.1). |
| 20 | B4 | C1 | solid | Closure is the self-model's pass over the channel's occupancy; occupancy itself is not constitutive (§3.6.1). |
| 21 | C1 | C2 | dashed | Arousal, attention and working memory resolve into capacity, selection and occupancy of the one channel (§3.6.1). |
| 22 | B6 | C3 | solid | Reportable content is produced by added recursive depth (§3.4.6). |
| 23 | C1 | C3 | dashed | The channel sets breadth, not reportability; this is why overflow is rejected (§3.6.1 'What the channel is not'). |
| 24 | B6 | C4 | solid | Minimal and basic consciousness share the lowest recursion depth of the ladder (§3.5). |
| 25 | B4 | C5 | solid | Temporal echo is recursion under closure (§3.4.4). |
| 26 | B5 | C6 | solid | If the sufficient conjunction names no material, nothing in the material is required (§4.4). |
| 27 | B8 | C7 | solid | Forked and live runs use the same models in the same format, so something must keep them distinguishable (§6.0). |
| 28 | B2 | C8 | solid | The ESM is generated from a substrate it cannot model (§3.8). |
| 29 | B6 | C8 | solid | Asking what consciousness is is a triply extended operation (§3.5, §3.8). |
| 30 | B1 | C9 | solid | The model kinds are poles of one continuous space, not separate modules (§3.2, §5.1). |
| 31 | A2 | C9 | solid | One shared substrate and its dynamics bind by construction (§5.1). |
| 32 | B3 | C10 | solid | Structure = relational organization of the explicit models; encoding = substrate realization (§8.6 derivation). |
| 33 | B4 | C11 | solid | What closure buys is self-consistency at a cost, paying only inside a cost window (§4.2.4, §8.10-8.11). |
| 34 | A1 | C12 | solid | Principle 1: near-criticality is what free modelling looks like in neural tissue (§3, §3.7). |
| 35 | B5 | C12 | solid | Recruitment in cortex plausibly shows as near-critical dynamics; the operating point is a signature (§3.7.3). |
| 36 | B2 | C13 | solid | Implicit = structural (stored in connectivity); explicit = Level-5 virtual dynamics (§3.1.1, §3.7.1). |
| 37 | B1 | C14 | solid | ESM and EWM are distinct model kinds on the scope axis (§9 OQ4). |
| 38 | C1 | D1 | solid | Thalamocortical relay as one realizer of a low-rank read/write path (§3.6.1). |
| 39 | C1 | D2 | solid | Abolishing experience with structure intact requires exactly channel failure (§3.6.1, 'Fourth'). |
| 40 | B2 | D2 | solid | The wired implicit layer is distinct from the running explicit models (§3.3). |
| 41 | D1 | D2 | dashed | Thalamocortical breakdown is the expected form of channel failure in cortex (§3.6.1). |
| 42 | B7 | D3 | solid | Permeability as a family of mechanisms, implemented neuromodulatorily in brains (§3.6). |
| 43 | D3 | D4 | dashed | Psychedelics act on 5-HT2A (global mode); lesion-related disconnection is local (§3.6, §6.1-6.2). |
| 44 | B7 | D4 | solid | Global and local modes of permeability (§6.0). |
| 45 | B7 | D5 | solid | OQ7 asks for the moment-to-moment mechanism that sets permeability (§9). |
| 46 | C1 | D5 | solid | A selection mechanism on a narrow path is the tractable form of the question (§3.6.1). |
| 47 | C13 | D6 | solid | Explicit models are not localizable, so the signature is a gradient, not a region (§8.4). |
| 48 | C14 | D6 | solid | Self-model operations should concentrate where the ESM is computed (§8.4). |
| 49 | C12 | D7 | solid | ESM activation depth indexed by position relative to the critical point (§8.5 derivation). |
| 50 | B6 | D7 | solid | Lucid onset = basic to simply extended (§8.5). |
| 51 | C4 | D7 | solid | Non-lucid dreaming = basic consciousness with thin self-model (§8.5). |
| 52 | C6 | D8 | solid | Substrate independence (§8.9 mechanism). |
| 53 | B5 | D8 | solid | The sufficient conjunction met in silico (§3.7.3, §8.9). |
| 54 | C6 | D9 | solid | Substrate is not the reason: the architecture is (§4.4). |
| 55 | B4 | D9 | solid | Broadcast/workspace without closure is not consciousness (§4.4, §7.2). |
| 56 | B5 | D9 | solid | No autonomous recruitment, no self-produced implicit-model update (§4.4). |
| 57 | B5 | D10 | solid | The autonomous-recruitment leg of the trichotomy excludes the laptop (§3.7.3). |
| 58 | B6 | D11 | solid | Continuum of self-modelling depth across organisms (§6.4). |
| 59 | C6 | D11 | solid | Criterion is functional, so no laminar cortex is required (corvids, §6.4). |
| 60 | B4 | D11 | solid | Systems below self-referential closure lack phenomenal experience (§6.4, insects). |
| 61 | D4 | E1 | solid | A global permeability increase should compensate a local block (§8.2 derivation). |
| 62 | B8 | E2 | solid | Each alter is a forked ESM configuration (§8.4 derivation). |
| 63 | D6 | E2 | solid | Differences concentrate along the self-referential gradient (§8.4). |
| 64 | D7 | E3 | solid | Threshold crossing in the ESM with a phase-transition signature (§8.5). |
| 65 | D2 | E4 | solid | Wired layer intact under anaesthesia, so implicit-model processing continues (Table 1b). |
| 66 | B4 | E5 | solid | If closure constitutes experience, disrupting the loop must degrade experience (Table 1b). |
| 67 | C3 | E5 | solid | Report is one read-out; the prediction targets experience, not report (Table 1b). |
| 68 | C14 | E6 | solid | Separable model kinds should be independently disruptable (§9 OQ4). |
| 69 | D6 | E6 | solid | Candidate TMS targets on the self-referential vs world-directed axis (§9 OQ4 (i)). |
| 70 | D3 | E7 | solid | Monotonic serotonergic modulation of permeability (§3.6 constraint 1). |
| 71 | D4 | E7 | solid | Global and local changes must have distinguishable signatures (§3.6 constraint 2). |
| 72 | D2 | E8 | solid | Expected signature of channel failure (§3.6.1). |
| 73 | D1 | E8 | solid | Thalamocortical relay as channel realizer (§3.6.1). |
| 74 | C12 | E9 | solid | Intensified self-modelling should push dynamics toward the signature (§3.7.3). |
| 75 | B9 | F1 | solid | A deprived ESM takes up the most salient content in the explicit world-model (§8.3 derivation). |
| 76 | D4 | F1 | solid | Ego dissolution = permeability raised beyond the point where self-referential input is disrupted (§8.3). |
| 77 | C10 | F2 | solid | Runs directly off Principle 3 via level-constitutive qualia (§8.6). |
| 78 | C2 | F3 | solid | Working memory is the channel's occupancy, so its span is the channel's rank (§3.6.1 'First'). |
| 79 | C14 | F4 | solid | d' indexes EWM discrimination, M-ratio the ESM's read-out (§9 OQ4). |
| 80 | C7 | F5 | solid | Source attribution is the fragile term and degrades first (§6.0). |
| 81 | B5 | F6 | solid | Free modelling is necessary; a lookup is its absence (Table 1b). |
| 82 | C11 | F7 | solid | Fit-window advantage scales with sociality and complexity (§8.11). |
| 83 | D5 | F8 | solid | Miscalibration mapping (§9 OQ7). |
| 84 | D4 | F9 | solid | Global permeability increase exposes intermediate stages in hierarchical order (§3.6, §8.1). |
| 85 | B4 | C15 | solid | Closure is between a self model and the world model, so §3.4.3 fixes what counts as a self model before closure can be judged ('What counts as a self model', §3.4.3). |
| 86 | B1 | C15 | solid | The SLAM vacuum fails in part because 'it has no implicit/explicit split' (§3.4.3). |
| 87 | B5 | C15 | solid | The vacuum also fails because 'its algorithm is fixed, and it recruits no free compute for its own modeling (Section 3.7.3)' (§3.4.3). |
| 88 | C15 | C4 | dashed | 'The self model at the floor is still a model of the system itself, however simple (Section 3.4.3); a mutual update between a position estimate and a map does not qualify' (§3.5). |
| 89 | B4 | E10 | solid | The trace tests whether a signal reaches a self-model component 'that enters the world model's update rule and is entered by it (Section 3.4.3)' (Table 1b). |
| 90 | C15 | E10 | solid | The trace counts only a component that models the system itself; a position estimate does not qualify (Table 1b, §3.4.3, §3.5). |
| 91 | C4 | E10 | solid | Minimal consciousness is unreportable by definition; 'its non-report signature, in systems that can be inspected, is a signal traced to the closed self and world models' (§3.5, Table 1b). |
| 92 | B4 | E11 | solid | Refuters of the premise that closure constitutes phenomenality, stated separately from the markers (§4.4). |
| 93 | B4 | F10 | solid | If a return-free twin did everything, 'closure would then do no explanatory work, and the identity would be idle' (§4.4). |
| 94 | C11 | F10 | solid | The theory's claims are economic (§4.2.4), so the twin must match 'within the same resource bound'; closed and unfolded systems agree only with unbounded resources (§4.4, §7.2, §8.11). |
| 95 | B7 | E1 | solid | 'Derivation: Principle 2 → variable implicit-explicit permeability (Section 6.0) → prediction': one mechanism with local and global modes, so a global increase should compensate a local block (§8.2). |
| 96 | A1 | F6 | solid | Table 1b's free-modelling row states Principle 1 as the construct ('Consciousness requires free modeling … Necessary, not sufficient') and the novel-input probe as its test (§3, Table 1b). |
| 97 | C5 | E12 | solid | C5 says flow is the smearing, so less smearing means less flow; because the echo runs through the explicit simulation as a whole, the loss is not tied to one sensory pathway (§3.4.4; proposal C5-1, docs/proposed-predictions-c5-c8-c9.md). |
| 98 | C5 | E13 | solid | What makes a 'now' is that the carried state is modelled 'as the recent past of a perspective' (§3.4.4); remove the carrying into the self-model and that representation should go (proposal C5-2, docs/proposed-predictions-c5-c8-c9.md). |
| 99 | C8 | F11 | solid | Mystery comes from the self-model representing experience without its generation (§3.8); anything that lets the simulation contain a generation account removes the absence, and since the ESM receives substrate information only as content inside the simulation (§3.4.3), a fake display and a real one reach it by the same route. The leak arm follows from §3.8's second mechanism, uninterpreted leaks of substrate processing (proposal C8-1, docs/proposed-predictions-c5-c8-c9.md). |
| 100 | C9 | E14 | solid | §5.1: the dynamics deliver binding into one experiential field, not consistency of its contents; feature assignment is content, so disturbing content leaves the field and disturbing the dynamics takes the field, contents included (proposal C9-1; evidence in docs/c9-binding-evidence.md). |
| 101 | C9 | E15 | solid | §5.1 (master L671): gamma synchrony is a signature of the integrating regime, not a dedicated binding mechanism, so phase manipulation should not change which features pair (proposal C9-2). |

**Edges considered and not added** (no derivation stated in the master): C6 → F10 (§4.4 says multiple realizability constrains *where* the premise can be tested, not what the twin claim follows from); C8 → F10 (opacity is on the twin's list of functions, but §4.4 does not cite §3.8); B9 → E1 (§7 l.917 credits "the redirectable ESM" with Prediction 1, but §8.2's own derivation runs through permeability only; logged as a master inconsistency, not mapped); B2/C13 → E1 (the disconnection-versus-destruction boundary condition is argued inline, without a derivation line); D9 → E10 (§4.4 names the trace as how D9 is *measured*, which is not an "in virtue of" relation). For the S338 nodes the proposal's derivations name only the claim each was proposed for: F11 also uses the §3.4.3 observational horizon, which already grounds C8 (B2 → C8) and has no node of its own, and E13 uses the §3.4.4 echo alone, so no further parents were added.

---

## 3. Unique vs shared predictions

"Shared with" names the theories on the published maps (GNWT, IIT, PRM, RPT; supplement: Active Inference, HOROR, HOSS, NREP, SOMA) wherever the master's distinguishing-power text supports it. Rival node labels are quoted from the preprint text. Supplement-map node labels are not available in the text extraction (the figures are images).

| FMT node | Prediction (short) | Verdict | Shared with / contested by | FMT's differential content |
|---|---|---|---|---|
| **E2** (P3) | DID alter dissimilarity follows a self-referential > sensorimotor gradient | **Unique** | IIT predicts posterior-integration differences, GNWT prefrontal-ignition differences, PP distributed prediction-error differences (§8.4) | The gradient itself |
| **F2** (P5) | Qualia structure aligns across individuals; absolute decoding does not | **Unique** (as a dissociation) | The structural arm overlaps with the Tsuchiya/Oizumi qualia-structure programme and is partly supported at group level (Kawakita 2025). Closest map node: IIT C2 (experience type depends on substrate architecture). Strong privacy predicts no alignment; standard functionalism predicts the encoding transfers too | The paired failure of absolute decoding |
| **F6** | Fixed-lookup novel-input probe (disconfirmer of free modelling) | **Unique** | — | It is FMT's own falsifier of A1 |
| **F7** | Advantage of self-modelling scales with task sociality/compositional depth (in silico) | **Unique** (as the scaling claim) | Sample-efficiency gains from world models are generic ML; only the scaling shape is FMT's | Small on simple tasks, steep on social ones |
| **E10** | White-box trace: a traced input reaching closed self and world models decides consciousness without report | **Unique** (as the procedure) | IIT also claims a report-free verdict from the substrate, but by a different quantity (Φ over the cause-effect structure), not by tracing a signal to a self model | Self-model criterion (C15) plus the two-way update; reaches minimal consciousness, which no report can |
| **F10** | Functional-twin refuter: no return-free system matches every phenomenality function within the same resource bound | **Unique** (as the resource-bounded claim) | The unfolding argument (Doerig et al. 2019, master §7.2) grants feedforward equivalents without a resource bound; FMT's reply is that they agree only with unbounded resources | The resource bound, and its in-silico pricing (§8.11) |
| **E13** (proposed S338) | In-silico echo cut removes the self-model's sense of its own elapsed time | **Unique** | Rivals silent: recurrence-based theories predict time coding wherever there is memory and do not separate self-located from world-located coding | The self-located/world-located interaction; tests representation, not experience |
| **E1** (P1) | Sub-ego-dissolution psychedelics improve anosognosia | **Shared in part** | Active Inference / REBUS: the coarse version follows from prior relaxation + aberrant predictive coding (Fotopoulou 2014). GNWT, IIT, PRM, RPT are silent | Dose below ego dissolution; lesioned-hemisphere complexity; disconnection vs destruction |
| **F1** (P2) | Ego-dissolution identity content (salvinorin A) tracks the most salient content | **Shared in part** | Active Inference / REBUS: input tracking as such is shared (relaxed self-priors plus per-channel precision; Apps & Tsakiris 2014). PP accounts of bodily self-attribution weight heartbeat contingency (Suzuki 2013; Aspell 2013). GNWT, IIT, HOT, AST are silent | Identity follows the salient unsynchronised stream over a faint heartbeat-synchronised one (2 × 2 salience × synchrony, with an under-drug contingency manipulation check) |
| **E3** (P4) | Lucid onset = phase transition originating in self-model networks | **Shared in part** | GNWT (prefrontal ignition overlaps); PP (precision on self-model, compatible). IIT predicts a posterior Φ increase instead | The combination of phase-transition dynamics, self-model-network origin and criticality markers. Signature-level: failure does not refute A1 |
| **F3** | WM capacity = channel rank, not brain volume | **Shared in part** | GNWT B1/C6/C10 (gated bottleneck; GW items = WM items) | Capacity derived from channel rank, plus the cross-species non-scaling test |
| **E7** | Monotonic 5-HT2A dose → permeability; global vs local signatures distinguishable | **Shared in part** | Entropic brain / REBUS predict entropy rising with dose | The global-vs-local signature split |
| **F5** | Source attribution degrades before experience; dreaming as the everyday case | **Shared in part** | PRM (A1/B5 reality monitoring; F3 hallucination when prefrontal function is disrupted) | The ordering; and no tag (FMT's requirement is negative) |
| **F8** | Selection-mechanism miscalibration → three schizophrenia symptom clusters; 5-HT2A → reward-valence violations | **Shared in part** | Dopamine hypothesis (Howes & Kapur 2009); PP aberrant salience | The architectural grounding. Candidate only (OQ7) |
| **E4** | Implicit-model processing continues under anaesthesia | **Shared in part** | GNWT (C4: unconscious modular processing) and RPT (B3: feedforward functions without consciousness) both accept rich unconscious processing | The claim that it survives at consciousness-abolishing doses, with plasticity (Katlowitz 2026). The prediction-framing note's "IIT/GNW predict no sophisticated processing" is **too strong** for GNWT; do not use it with Mudrik's group |
| **F11** (proposed S338) | A simulated generation display lowers felt mystery; an uninterpretable one does not | **Shared in part** | AST (Graziano & Webb 2015) shares the explanation (a self-model omitting mechanism) but places it in an automatic attention schema an external display does not alter, so on our reading it predicts no or a weaker effect; illusionism reads the same way. Neither is a published prediction. Explanatory-gap views (cf. Chalmers 2018) predict no effect | Veridical = fake; the leak arm moves mystery the other way |
| **E5** | Disrupting the self-modelling loop degrades experience, not just report | **Contested** | PRM D2 and HOT/HOSS (a higher-order change alone should change experience); GNWT (experience follows ignition/P3b) | — see §3.1 |
| **E11** | Human refuters of the bridge: closed-loop content with no experience, or experience markers without closure | **Contested** | RPT (local recurrence is sufficient; see the C4 ↔ RPT C5 link) and IIT (integrated cause-effect structure) require no self model, so they allow the outcome FMT names as its second refuter | Closure, not recurrence or integration, as what must be absent |
| **E6** | ESM/EWM double dissociation | **Contested** | Strict PP / Active Inference predicts covariation. Seth's interoceptive inference softens the contrast (§9 OQ4) | Orthogonal disruption |
| **E12** (proposed S338) | Supramodal frame-like experience tracks a shorter autocorrelation window (THC) | **Contested** (mechanism); shared in part (phenomenon) | Discrete-perception accounts (VanRullen 2016; Herzog et al. 2020) also predict stroboscopic experience, but tie it to a slower perceptual cycle (alpha peak frequency down) | ACW shortening with alpha unmoved; all modalities and thought together, not vision alone |
| **D8 / D9** (extrapolation) | Synthetic system meeting the sufficient conjunction (B5) conscious; LLMs/agent loops not | **Contested** | GNWT D11 (functional GW suffices) and RPT D2 (recurrent learning systems are conscious) are more liberal; IIT's artificial-systems extrapolation (F3) is more restrictive about digital hardware | Closure + autonomous recruitment as the criterion |
| **E8** | Thalamocortical breakdown under propofol | **Shared** | GNWT, IIT, RPT and DIT all accommodate it | Only that FMT derives it from channel failure (D2) |
| **F4** | Metacognitive efficiency decoupled from d′ | **Shared** | Well established (Fleming & Lau 2014); HOSS/PRM model it too | None claimed |
| **F9** | Psychedelic imagery follows the processing hierarchy | **Shared** | REBUS / Entropic brain | None claimed (master §8.1 says so) |
| **E9** | Jhāna shifts dynamics toward the near-critical signature | **Shared** | Criticality frameworks (ConCrit); IIT E8 makes a different meditation prediction (decreased posterior gamma in "pure presence") | None; signature-level |

**Where FMT disagrees with the theories already mapped (rival node labels, for the convergence analysis of §1.3):**
- GNWT D6 (failed ignition = not conscious) vs FMT C4 (minimal and basic consciousness without broadcast).
- GNWT D11 vs FMT D8/D9.
- IIT D5 (inactive neurons contribute) vs FMT B2.
- IIT's artificial-systems extrapolation vs FMT D8.
- PRM A1 (the tag constitutes consciousness) vs FMT C7 (no tag; a function only).
- RPT D2 vs FMT D8.

Agreements are listed in the JSON `cross_theory_links`. The best convergence point for a Negro-style comparison is **GNWT C6 "Items in GW are items in Working Memory" ↔ FMT C1/C2**: both maps hold it, and it is central on FMT's map (C1 has the 4th-highest BC) while GNWT's C6 is a mid-level hub. That is exactly the kind of "same claim, different weight" result the paper shows with NMDA.

### 3.1 Table 1b closure falsifier (E5) — resolved S334

Master Table 1b used to state the closure falsifier as *"Metacognitive disruption leaves phenomenology intact."* That is the outcome FMT predicts (F4: metacognitive read-out decouples from first-order discrimination; §3.5: basic experience needs no higher-order layer), so it read as the HOT position. MG ruled (S334) to reword the master: the falsifier is now *disrupting the self-modelling loop itself leaves no-report markers of experience intact*. Metacognitive disruption alone does not test closure, and report may fail with it because transfer to long-term memory can fail as well. E5 carries the new wording.

---

## 4. Centrality: the expected high-centrality nodes (computed)

The four measures were computed exactly as described in §1.2: outgoing LRC and HC normalised by n−1, directed Brandes BC normalised by (n−1)(n−2), and PageRank with d = 0.85 and dangling mass spread uniformly. A stdlib re-implementation was used because networkx is not installed here. The authors' code should reproduce these values to rounding, **if** their HC uses outgoing distances as the text says. **Script (tracked since 2026-10-19):** `python3 scripts/prediction_map_centrality.py` prints the distribution and the full table below; `scripts/test_prediction_map_centrality.py` checks the measures on hand-computable graphs and fails while this section's table is stale. Before the v19 additions it reproduced all 220 values of the 55-node table to the printed precision. Percentiles use the nearest-rank convention (median = value at index ⌊n/2⌋, 90th = index ⌊0.9(n−1)⌋ of the sorted values).

**Distribution (FMT map, 62 nodes, 99 edges):**

| Measure | median | 90th pct |
|---|---|---|
| LRC | 0.016 | 0.156 |
| HC | 0.016 | 0.117 |
| BC | 0.000 | 0.007 |
| PR | 0.014 | 0.022 |

These are comparable to the published maps; GNWT's core HC is 0.440, FMT's is 0.39–0.40. Earlier values: 64 nodes (before E16, S343) LRC 0.016 / 0.159, HC 0.016 / 0.119, BC 0.001 / 0.007, PR 0.014 / 0.022; 59 nodes (v19 additions, before S338) LRC 0.017 / 0.224, HC 0.017 / 0.170, BC 0.000 / 0.008, PR 0.015 / 0.024; 55 nodes LRC 0.019 / 0.185, HC 0.019 / 0.145, BC 0.000 / 0.008, PR 0.016 / 0.026. The 90th percentiles of LRC and HC fell with S338 because three leaves joined the bottom of the sorted list while the nearest-rank index moved up only two places: the LRC 90th percentile is now C1 (0.164) instead of B5 (0.224). No hub lost reach.

**Reading:**
- **Hubs (LRC/HC), excluding the core:**
  - B1, the two-kinds-of-model architecture (LRC 0.770, HC 0.373), stands far above every other L1 claim.
  - Next come B2, the real/virtual split (0.459 / 0.265), and B4, closure (0.410 / 0.269). B4 gained most from the additions (from 0.296 / 0.191 at 55 nodes): the self-model criterion, the white-box trace and both bridge refuters derive from it, and with S338 so do the two echo predictions through C5. Closure now edges past the real/virtual split on HC, though not on LRC.
  - Then B5 (necessary thresholds, sufficient conjunction; LRC 0.213) and C1 (the channel; 0.164).

  The architecture is still FMT's most productive claim, ahead of closure. That parallels the GNWT finding that the bottleneck claim is less far-reaching than its prominence suggests.
- **Bridges (BC):**
  - B2 (0.0156) is the top bridge, ahead of B1 (0.0117), A2 (0.0115), B4 (0.0098), C1 (0.0088) and B7 (0.0087).
  - The real/virtual split is the logical connector between the principles and both the anaesthesia/channel cluster and the permeability cluster.
  - Evidence against the implicit/explicit dissociation (E4, E6, F4) is therefore the most structurally damaging kind for FMT.
  - The new C15 is a minor bridge (0.0026, about D7's level): it links B1, B4 and B5 to the minimal-consciousness cluster (C4 → D7, E10). With S338, C5 (0.0022) and C8 (0.0016) became minor bridges too.
- **High-stakes predictions (PR):**
  - E3 lucid onset (0.031), then F2 qualia-structure dissociation (0.028), F1 ego-dissolution content (0.025), **E10 white-box trace (0.025, 5th of 62)**, E2 DID gradient (0.024), and E5 closure handle, E6 and E8 (0.023).
  - D7 (0.025) and D6 (0.023) are the high-PR intermediate claims.
  - E10 ranks high because it has three parents (B4, C15, C4), and C4 itself gained a parent (C15; C4's PR rose from 0.013 to 0.019 at 59 nodes, 0.018 now).
- **Where the v19 additions land (PR rank of 62):** E10 5th; F10 functional twin 24th (0.015); C15 32nd (0.014); E11 human refuters 61st (0.011). E11 hangs off B4 alone, and B4 has ten children, so each receives a small share. A reader will rank the human refuters as low-stakes, as the master's own derivation (closure only) implies. Adding F10 also halved F7's inheritance from C11: F7 fell from 0.022 (15th of 55) to 0.015 (28th of 59), 0.014 (31st of 62) now.
- **Where the S338 proposed predictions land (PR rank of 62):** F11 simulated generation display 13th (0.021), because C8 has two parents (B2, B6) and passes everything to its one child; E12 and E13 29th and 30th (0.014 each), because C5 hangs off B4 alone and splits its share over two children. Their quality profile (computed by `scripts/prediction_map_quality.py`): one parent and one path from the core each; exposure 15% of the theoretical claims for E12 and E13, 21% for F11. They are single-parent predictions, so a failure lands on C5 or C8 first.
- **Two findings MG should see before sending:**
  1. **E3 still tops PageRank (0.031, ahead of F2 at 0.028), but on FMT's own terms it is a signature prediction whose failure cannot refute A1.** PR is high because E3 rests on D7, which has three parents including C12 (criticality). This is where the method and FMT's framing collide. Either accept that Negro-style PR will flag E3 as high-stakes (and say in the cover note why its failure would hit C12/D7, not the core), or check whether §8.5's derivation should route D7 through B6/C4 alone.
  2. **F6 and E1 moved up but F6 stays low.** The master states one further parent for each: B7 → E1 (§8.2's derivation line names permeability directly) and A1 → F6 (Table 1b's free-modelling row states Principle 1 as the construct F6 tests). E1 rose from 0.015 (30th of 55) to 0.017 (20th of 59); it is 0.016 (21st of 62) after S338. F6 rose only from 0.013 (50th of 55) to 0.014 (43rd of 59), and is 0.013 (46th of 62) now: A1 is a root, so it carries only the base PageRank mass and splits it over five children. PageRank by construction ranks a falsifier that hangs directly off the core as low-stakes; no textually supported edge changes that. The cover note should say that F6 disconfirms A1 itself.
- **Unproductive claims (the paper's "weak links"):**
  - C9 (binding dissolved) is a leaf: a theoretical claim with no empirical consequence on the map (its predictions are deferred to a later session). C6 (substrate independence) leads only to the extrapolations D8, D9 and D11, so it too reaches no prediction. These two are the map's idle claims (reach 32 of 34 theoretical claims, 94%).
  - C5 (temporal echo) and C8 (meta-problem) were leaves until S338. They now reach E12/E13 and F11, but only through proposed predictions not yet in the master; until the master carries them, the honest reading is that the theory states these claims without a test of its own.
  - B3 (virtual qualia) reaches only C10 → F2.
  - The paper flags exactly this pattern (IIT's B3/B4). Expect it to be noticed.

Full table:

| ID | Level | LRC | HC | BC | PR |
|---|---|---|---|---|---|
| A1 | core | 1.000 | 0.385 | 0.0000 | 0.009 |
| A2 | core | 0.938 | 0.398 | 0.0112 | 0.011 |
| A3 | core | 0.922 | 0.398 | 0.0070 | 0.011 |
| B1 | L1 | 0.781 | 0.376 | 0.0112 | 0.013 |
| B2 | L1 | 0.453 | 0.260 | 0.0147 | 0.013 |
| B3 | L1 | 0.047 | 0.039 | 0.0037 | 0.013 |
| B4 | L1 | 0.391 | 0.257 | 0.0089 | 0.011 |
| B5 | L1 | 0.203 | 0.154 | 0.0068 | 0.013 |
| B6 | L1 | 0.141 | 0.109 | 0.0044 | 0.013 |
| B7 | L1 | 0.125 | 0.094 | 0.0079 | 0.013 |
| B8 | L1 | 0.047 | 0.039 | 0.0007 | 0.011 |
| B9 | L1 | 0.016 | 0.016 | 0.0011 | 0.013 |
| C1 | L2 | 0.156 | 0.117 | 0.0080 | 0.012 |
| C2 | L2 | 0.016 | 0.016 | 0.0017 | 0.011 |
| C3 | L2 | 0.016 | 0.016 | 0.0010 | 0.014 |
| C4 | L2 | 0.047 | 0.039 | 0.0012 | 0.018 |
| C5 | L2 | 0.031 | 0.031 | 0.0020 | 0.010 |
| C6 | L2 | 0.047 | 0.047 | 0.0005 | 0.011 |
| C7 | L2 | 0.016 | 0.016 | 0.0005 | 0.014 |
| C8 | L2 | 0.016 | 0.016 | 0.0015 | 0.013 |
| C9 | L2 | 0.031 | 0.031 | 0.0020 | 0.013 |
| C10 | L2 | 0.016 | 0.016 | 0.0015 | 0.015 |
| C11 | L2 | 0.031 | 0.031 | 0.0010 | 0.010 |
| C12 | L2 | 0.047 | 0.039 | 0.0022 | 0.013 |
| C13 | L2 | 0.047 | 0.031 | 0.0011 | 0.011 |
| C14 | L2 | 0.062 | 0.055 | 0.0033 | 0.011 |
| C15 | L2 | 0.062 | 0.044 | 0.0023 | 0.014 |
| D1 | L3 | 0.047 | 0.039 | 0.0003 | 0.011 |
| D2 | L3 | 0.031 | 0.031 | 0.0034 | 0.018 |
| D3 | L3 | 0.078 | 0.055 | 0.0007 | 0.012 |
| D4 | L3 | 0.062 | 0.062 | 0.0034 | 0.017 |
| D5 | L3 | 0.016 | 0.016 | 0.0020 | 0.014 |
| D6 | L3 | 0.031 | 0.031 | 0.0020 | 0.022 |
| D7 | L3 | 0.016 | 0.016 | 0.0025 | 0.024 |
| D8 | L3 | 0.000 | 0.000 | 0.0000 | 0.014 |
| D9 | L3 | 0.000 | 0.000 | 0.0000 | 0.015 |
| D10 | L3 | 0.000 | 0.000 | 0.0000 | 0.011 |
| D11 | L3 | 0.000 | 0.000 | 0.0000 | 0.016 |
| E1 | L4 | 0.000 | 0.000 | 0.0000 | 0.016 |
| E2 | L4 | 0.000 | 0.000 | 0.0000 | 0.023 |
| E3 | L4 | 0.000 | 0.000 | 0.0000 | 0.030 |
| E4 | L4 | 0.000 | 0.000 | 0.0000 | 0.017 |
| E5 | L4 | 0.000 | 0.000 | 0.0000 | 0.022 |
| E6 | L4 | 0.000 | 0.000 | 0.0000 | 0.022 |
| E7 | L4 | 0.000 | 0.000 | 0.0000 | 0.018 |
| E8 | L4 | 0.000 | 0.000 | 0.0000 | 0.022 |
| E9 | L4 | 0.000 | 0.000 | 0.0000 | 0.015 |
| E10 | L4 | 0.000 | 0.000 | 0.0000 | 0.024 |
| E11 | L4 | 0.000 | 0.000 | 0.0000 | 0.010 |
| E12 | L4 | 0.000 | 0.000 | 0.0000 | 0.014 |
| E13 | L4 | 0.000 | 0.000 | 0.0000 | 0.014 |
| F1 | L5 | 0.000 | 0.000 | 0.0000 | 0.024 |
| F2 | L5 | 0.000 | 0.000 | 0.0000 | 0.022 |
| F3 | L5 | 0.000 | 0.000 | 0.0000 | 0.019 |
| F4 | L5 | 0.000 | 0.000 | 0.0000 | 0.013 |
| F5 | L5 | 0.000 | 0.000 | 0.0000 | 0.021 |
| F6 | L5 | 0.000 | 0.000 | 0.0000 | 0.013 |
| F7 | L5 | 0.000 | 0.000 | 0.0000 | 0.014 |
| F8 | L5 | 0.000 | 0.000 | 0.0000 | 0.021 |
| F9 | L5 | 0.000 | 0.000 | 0.0000 | 0.013 |
| F10 | L5 | 0.000 | 0.000 | 0.0000 | 0.015 |
| F11 | L5 | 0.000 | 0.000 | 0.0000 | 0.021 |
| E14 | L4 | 0.000 | 0.000 | 0.0000 | 0.015 |
| E15 | L4 | 0.000 | 0.000 | 0.0000 | 0.015 |
| E16 | L4 | 0.000 | 0.000 | 0.0000 | 0.015 |

**Platform check (2026-10-19, headless Chromium, local file load only, nothing saved to a server).** The regenerated `fmt-prediction-map.platform.json` loads in https://xk29y8.csb.app with no alert: 59 nodes, 96 edges, 13 of them dashed. The app's **Analyze** button opens a "Network Metrics" panel with a metric selector (None, LRC, Harmonic Centrality, Betweenness Centrality, PageRank) and the counts "Nodes: 59, Edges: 96"; choosing a metric puts a two-decimal badge on every node. With PageRank selected, all 59 badges agree with the table above to the displayed precision, and the six nodes showing 0.03 are this table's top six (E3, F2, D7, F1, E10, E2). The app's own centrality code therefore ranks the map as this section does; at two decimals it cannot separate the top six. That check was run on the 59-node map; the 62-node file with the S338 additions was regenerated by the same script and passes `test_convert_prediction_map.py`, but has not been loaded in the app again.

---

## 5. How MG could upload it (plain language)

The format is now known (§1.4, `mudrik-platform-schema.md`), and the converted file has been loaded and round-tripped in the app headlessly.

1. **Regenerate the upload file** if the map changed: `python3 scripts/convert_prediction_map.py` → `drafts/papers-moc7/fmt-prediction-map.platform.json`.
2. **Open https://xk29y8.csb.app/ in a desktop browser**, choose **Load Map** and select that file. The theory slot reads `other` (the dropdown has no FMT entry).
3. **The app stores maps only in the browser** (`localStorage`, no server-side save), and the `other` slot does not survive a page reload. Download the map again before closing the tab if anything was changed by hand.
4. **What the app cannot show:** levels (shown as columns, not rings), references (only the numbers in each label), the solid/dashed distinction as a native feature (it renders via an SVG dash style), and the cross-theory links. The rendered PDF or this spec carries those.
5. **Getting into the programme is a conversation, not an upload.** The paper's maps were built by the authors and then iterated with the proponents (pp. 5–8). Its additional maps (Active Inference, HOROR, HOSS, NREP, SOMA) are all theories under adversarial collaborations. The realistic route is to send **Niccolò Negro (corresponding author)**, cc Liad Mudrik, the JSON plus a rendered PDF of the map, offering it as a proponent-built draft for their own iteration. That message is a Gmail draft for MG, per the outreach workflow, and is not part of this deliverable.
6. Before sending, run the reference check on the ten bibliography items: `python3 scripts/verify_references.py --check`. Items 4–10 are taken from the master reference list.

---

## 6. Decisions for MG

1. ~~E5 / Table 1b closure falsifier wording~~ — resolved S334 (§3.1).
2. **E3 at the top of PageRank** (§4). Accept it and explain, or revisit the derivation in §8.5.
3. **Core:** three boxes (A1–A3) or one merged A1?
4. **Scope:** add the candidate (OQ7) nodes D5/F8? They raise PR but are not commitments. Keeping them is honest only if they stay labelled "candidate".
5. **Rival-node mapping:** the supplement maps (Active Inference, HOSS, NREP …) are figures; their node labels need the PDF figures or the OSF files to cite exactly. Is it worth fetching from another machine?
6. **Send route:** Negro first (corresponding author, who builds the maps), or Mudrik first (an existing correspondent who replied 2026-10-08)?
