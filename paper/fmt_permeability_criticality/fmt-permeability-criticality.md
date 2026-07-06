# Permeability as Directed Information Flow: A Transfer-Entropy Operationalization of the Implicit–Explicit Boundary in Consciousness, with Signed Predictions Across Pharmacological and Sleep States

**Matthias Gruber**

*Independent researcher*

*ORCID: 0009-0005-9697-1665*

*Correspondence: matthias@matthiasgruber.com*

---

## Abstract

A recurring informal claim across theories of consciousness is that altered states — psychedelics, anesthesia, sleep, meditation — reflect changes in how much normally-unconscious ("implicit") information reaches conscious access ("explicit"). This "permeability" language is explanatorily productive but has lacked a measurable definition, leaving it unfalsifiable. Here I give permeability a precise operational definition as the **transfer entropy** (Schreiber, 2000) from substrate/implicit-processing signals to explicit/conscious-access signals, decomposed into a **channel-indexed gating family** that maps onto distinct neuromodulatory systems (serotonergic, GABAergic, dopaminergic, noradrenergic). I then define three complementary, already-standard **criticality observables** — the neuronal-avalanche branching ratio σ, the maximum Lyapunov exponent λ_max, and the detrended-fluctuation-analysis exponent α — as a joint operating-regime constraint, and I note that avalanche criticality and edge-of-chaos criticality are dissociable (Kanders et al., 2017) and must be measured separately. The core deliverable is a table of **signed, state-specific predictions**: each state (normal waking, psilocybin/LSD, high-dose *Salvia divinorum*, right-hemisphere-stroke anosognosia, NREM, REM, meditation, hypnagogia) is assigned a predicted direction of change in global transfer entropy, in channel-specific gating, and in the criticality observables, with divergence points that discriminate this account from an "entropy simply goes up" null. Finally I specify a concrete **Phase-1 analysis plan** on existing open psychedelic and anesthesia datasets — which recordings, which TE estimator (JIDT/IDTxl with Kraskov–Stögbauer–Grassberger estimation and Ragwitz embedding), which source/target ROIs, how effect signs are read off, and the confound controls (spectral, volume-conduction, and stationarity). The framework is deliberately theory-light: it operationalizes one mechanism and stakes it on directional predictions, so that it can be *clearly right or clearly wrong* on data that already exist.

**Keywords**: transfer entropy; consciousness; directed information flow; neuronal avalanches; branching ratio; criticality; psychedelics; anesthesia; effective connectivity

---

## 1. Introduction

### 1.1 The Problem: "Permeability" Is Productive but Unmeasured

Across several frameworks, a shared intuition recurs: conscious states differ in how much information that is normally processed *outside* awareness becomes available *to* awareness. Psychedelics are described as "loosening" a filter; deep anesthesia as "closing" one; dreaming as awareness driven from within rather than from the senses. This intuition is explanatorily productive — it organizes an otherwise disparate phenomenology — but as usually stated it is a metaphor. "The boundary becomes more permeable" predicts nothing quantitative and can absorb almost any result post hoc. That flexibility is precisely what makes such claims scientifically weak.

The claim I make here is narrow and testable: **permeability is directed information flow from implicit-processing signals to explicit/conscious-access signals, and it is measurable, right now, as transfer entropy on existing neural recordings.** I am not proposing a new theory of consciousness. I am taking one mechanism that many theories invoke informally and giving it (i) a formal definition, (ii) a decomposition that respects known neuromodulatory pharmacology, and (iii) a table of signed predictions that a single re-analysis of open data could falsify.

### 1.2 Why Transfer Entropy

Transfer entropy (TE; Schreiber, 2000) measures the reduction in uncertainty about the future of a target time series *Y* given the past of a source *X*, beyond what *Y*'s own past already provides. It is model-free (no assumed functional form), directional (T_{X→Y} ≠ T_{Y→X} in general), and captures nonlinear dependencies — three properties that linear Granger causality lacks and that matter for neural data. TE is now a mature tool in neuroscience with validated estimators and confound controls (Vicente et al., 2011; Wibral et al., 2014; Lizier, 2014, JIDT; Wollstadt et al., 2019, IDTxl). This maturity is the point: the operationalization proposed here requires **no new mathematics**, only a disciplined application of established estimators to a specific source→target contrast, read with a specific sign convention.

### 1.3 What This Paper Delivers

Section 2 defines permeability as TE and decomposes it into a channel-indexed gating family aligned to neuromodulatory systems. Section 3 defines the three criticality observables and the dissociation problem. Section 4 is the signed-prediction table and the divergence points that separate this account from a generic "complexity tracks consciousness" claim. Section 5 is the Phase-1 analysis plan on named open datasets, including estimator choice, ROI selection, sign read-out, and confound controls. Section 6 states the limits honestly: this is a measurement framework for one mechanism, not a theory of phenomenality, and the "implicit/explicit" partition is an operational stipulation to be validated, not a claim that the brain contains two boxes.

---

## 2. Permeability as Transfer Entropy

### 2.1 Definition

Let the neural state be observed as a set of time series. Partition channels (or sources) into two operational classes by an *a priori*, preregistered criterion (§5.2): an **implicit set** I — signals from processing stages that do not, in the baseline state, correlate with report/conscious access — and an **explicit set** E — signals from stages that do. Define permeability as the transfer entropy from I to E:

> **P ≡ T_{I→E} = Σ p(e_{t+1}, e_t^{(k)}, i_t^{(l)}) · log [ p(e_{t+1} | e_t^{(k)}, i_t^{(l)}) / p(e_{t+1} | e_t^{(k)}) ]**

where e_t^{(k)} and i_t^{(l)} are the k- and l-dimensional delay embeddings of the explicit and implicit signals (Takens embedding; dimension and lag set by the Ragwitz criterion, §5.3). P has units of bits (or nats) per sample and is intrinsically directional: it is the extra predictability of the *explicit* future contributed by the *implicit* past.

This is the entire formal core. Everything downstream is (a) how to decompose P, (b) what regime the substrate must be in for P to be meaningful, and (c) which direction P and its components should move in each state.

### 2.2 Global vs. Local Permeability

P can be computed globally (pooled or averaged over all I→E pairs) or locally (for a specific implicit source region → explicit target region). This distinction is load-bearing:

- **Global P** captures whole-brain shifts — the account of psychedelics (uniform increase) and deep anesthesia (uniform collapse).
- **Local P** captures domain-specific deficits — the account of anosognosia, where transfer from a specific damaged domain fails while the rest of the brain is normal.

The same quantity, at two spatial scales, distinguishes a global pharmacological effect from a focal lesion effect. This is a genuine, non-trivial consequence of the definition.

### 2.3 The Gating Family: One Knob Is Wrong

Permeability is not a single scalar. In biological brains, the implicit→explicit boundary is modulated independently by several neuromodulatory systems, across channels, regions, and cortical layers. Collapsing them into one "permeability knob" would predict that all state changes look alike, which is false. I therefore define a **gating family**

> **G = { g_c : c ∈ C },  g(t) = ∏_{c∈C} g_c(t)**

indexed by modulatory channel c ∈ C = {5-HT, GABA, DA, NA, …}, where each g_c ∈ [0,1]^{N_c} is a spatially resolved gate (N_c = region/column/voxel count at the analysis scale) and the composite gate is the element-wise product. A scalar "permeability" is recovered as a summary statistic (e.g., the spatial mean of g), but the *fundamental* quantity is the channel-indexed family. Empirically, G is not directly observed; it is inferred from the pharmacology of the manipulation (which receptor system the drug targets) crossed with the spatial pattern of the measured TE change.

The decomposition earns its keep by making **channel-specific signed predictions** (§4): serotonergic agonism should raise TE broadband and globally; GABAergic agonism should suppress TE globally; dopaminergic modulation should change *which* implicit content crosses (the spatial/scope pattern) without necessarily changing the *total*; focal lesions should knock out TE in a specific pathway only. These four signatures are distinguishable in data, which is the whole point of refusing the single-knob model.

### 2.4 Total Conscious Content (Auxiliary Scalar)

For convenience I define a single scalar summarizing the "amount" of explicit processing available to be driven, C(t), as the total explicit-side activity above the conscious-access criterion. C(t) is offered only as the quantity expected to co-track existing whole-brain complexity indices — the Perturbational Complexity Index (PCI; Casali et al., 2013) and Lempel–Ziv complexity — providing an external convergent-validity check. It is not part of the core TE claim and carries no independent theoretical weight here.

---

## 3. Criticality Observables

Permeability is only interpretable if the substrate is in a dynamical regime that *can* transmit information over distance without either dying out or exploding into noise. That regime is criticality. I do not here argue *why* consciousness should require criticality (that is a separate, and contested, theoretical claim). I take the weaker, purely operational position: **report the operating regime alongside the permeability measurement, using three already-standard observables, and treat their relationship as an empirical question.**

### 3.1 Three Measures

- **Branching ratio σ** — mean number of descendant activations per ancestor across neuronal avalanches (Beggs & Plenz, 2003; Shew & Plenz, 2013; MR-estimator, Wilting & Priesemann, 2018). σ < 1 subcritical, σ = 1 critical, σ > 1 supercritical. The empirical consciousness-criticality literature (ConCrit; Priesemann et al., 2013, 2014) centers on σ, with the awake brain slightly subcritical (σ ≈ 0.95–0.99).
- **Maximum Lyapunov exponent λ_max** — separation rate of nearby trajectories (Bertschinger & Natschläger, 2004; Boedecker et al., 2012). λ_max < 0 ordered, λ_max ≈ 0 edge of chaos, λ_max > 0 chaotic. This is the measure most directly tied to the "edge of chaos" intuition.
- **DFA exponent α** — long-range temporal autocorrelation / scale-free structure of oscillation amplitude envelopes (Hardstone et al., 2012). α ≈ 0.5 uncorrelated, α ≈ 1 critical, long-range correlated.

### 3.2 The Dissociation Problem — Measure Them Separately

Kanders et al. (2017) showed that avalanche criticality (σ ≈ 1) and edge-of-chaos criticality (λ_max ≈ 0) do **not** necessarily co-occur: they index different phase transitions. This is a methodological warning, not a theoretical thesis. The operational consequence is concrete: **do not assume one measure stands in for the others.** Compute σ, λ_max, and α independently, and report states where they diverge as the most informative cases — a state that is avalanche-critical but not edge-of-chaos (or vice versa) is exactly where competing theoretical readings make different bets. In this paper I make no claim about which measure is "primary"; I claim only that reporting all three, and their divergences, is the honest way to characterize regime.

### 3.3 The Regime Constraint (Operational, Not Derived)

For the permeability predictions below to be interpretable, I assume only that a conscious, responsive baseline sits in the empirically observed near-critical band (σ roughly in [0.95, 1.1]; λ_max near 0; α near 1). This is an *observed regularity* imported from the criticality literature, used here as a covariate / inclusion criterion — not a derived necessity. The stronger claim that self-referential architecture *entails* criticality is explicitly excluded from this paper: that chain is a conjecture, not a deduction, and nothing here depends on it.

---

## 4. Signed Predictions

The framework's empirical content is a set of **signed, state-specific predictions**. Each state is assigned (i) a direction for global P = T_{I→E}, (ii) the channel(s) of G expected to drive it, (iii) any local/domain anomaly, and (iv) the expected criticality-observable movement. Signs, not magnitudes, are the primary commitment — magnitudes are dataset-dependent and calibrated in Phase 1.

**Table 1. Predicted signed changes relative to normal waking baseline.**

| State | Global P (T_{I→E}) | Driving channel(s) in G | Local anomaly | Criticality observable |
|---|---|---|---|---|
| Normal waking | baseline | selective gating | none | σ ≈ 0.95–0.99; λ_max ≈ 0; α ≈ 1 |
| Psilocybin / LSD | ↑↑ (broadband) | g_{5-HT} ↑ globally | none (global) | σ → 1 (toward/just past critical); α ↑ |
| *Salvia divinorum* (high dose, κ-opioid) | ↑ but ESM-selective collapse | g_{κ} disrupts self-scope gating | T_{I→E} to self-referential targets → 0; T_{I→E} to exteroceptive targets ↑ | regime near-critical but reorganized |
| Anosognosia (R-hemisphere stroke) | ≈ normal (most domains) | structural loss of g_c in one pathway | domain-specific T_{I→E} deficit | global σ near baseline |
| NREM (deep sleep) | ↓↓ (near zero) | uniform gate suppression | uniform | σ < 1 (subcritical); PCI ↓ |
| REM dreaming | medium, **internally sourced** | endogenous drive | T from stored parameters ↑; T *from sensory input* → 0 | σ near waking; PCI near waking |
| Meditation (trained) | selectively ↑ | domain-specific g_c control | trained target domains only | α ↑ in trained bands |
| Hypnagogia / sleep onset | gradually ↑ then variable | rising baseline gate noise | bottom-up onset (low→high level) | drift toward subcritical |

### 4.1 The Divergence Points (What Makes This Falsifiable, Not Vacuous)

A skeptic will say "entropy/complexity just goes up in psychedelics and down in anesthesia — you've relabeled a known result." The framework's non-trivial, discriminating predictions are the ones a generic complexity account does **not** make:

1. **Direction, not just level.** P is *directed* (I→E). REM is the sharp test: undirected complexity in REM is near-waking, but this account predicts a specific dissociation — high transfer *from stored/internal parameters* to explicit signals, near-**zero** transfer *from sensory input* to explicit signals. A symmetric or sensory-driven TE pattern in REM would falsify it.
2. **Channel-specific spatial signature.** Serotonergic (psilocybin) vs. GABAergic (propofol) manipulations should differ not only in sign of global P but in *which* g_c and which spatial pattern drives it. If propofol and psilocybin produced mirror-image *identical* spatial TE patterns, the gating-family decomposition would be wrong.
3. **Content-vs-amount split for dopamine.** Dopaminergic modulation is predicted to change the *scope/spatial pattern* of what crosses without necessarily changing total P. A finding that DA manipulation only scales total P uniformly would falsify the family decomposition.
4. **Local-without-global in anosognosia.** A focal deficit in T_{I→E} for one domain with normal global P is predicted. Finding either global collapse or no local deficit would falsify the local/global distinction.
5. **Salvia's self-selectivity.** κ-opioid ego dissolution is predicted to collapse transfer specifically to *self-referential* explicit targets while sparing/raising transfer to *exteroceptive* targets — a signed, region-selective prediction distinct from a uniform increase.

These five are where the account earns falsifiability. Each names a result that, if observed, kills a specific structural claim.

---

## 5. Phase-1 Analysis Plan (Existing Data)

Phase 1 requires no new data collection and no new mathematics. It is a preregisterable re-analysis of open recordings.

### 5.1 Datasets

- **Psychedelics.** Open psilocybin and LSD resting-state datasets with simultaneous or matched EEG/MEG and/or fMRI (e.g., the Imperial College / Carhart-Harris LSD MEG–fMRI corpus and psilocybin resting-state releases; open psilocybin EEG sets on OpenNeuro). MEG/EEG is primary because TE needs adequate temporal resolution; fMRI supports the spatial/scope pattern and the PCI-convergence check.
- **Anesthesia.** Propofol datasets with graded sedation levels (e.g., the Cambridge propofol EEG/fMRI sets; open ECoG anesthesia recordings where available). Graded dosing is essential to test dose-monotonic sign predictions.
- **Sleep.** Open polysomnography EEG with staged NREM/REM (e.g., Sleep-EDF, or higher-density research PSG) for the REM directed-source dissociation and NREM collapse.
- **Meditation** (secondary/exploratory): open long-term-practitioner EEG sets, used only for the trained-domain-specificity prediction, which is weaker and exploratory.

Anosognosia and *Salvia* predictions are flagged as **prospective** (requiring targeted acquisition) and are not part of the immediate re-analysis; they are stated so the framework is complete and the later experiments are pre-committed.

### 5.2 Defining the Implicit (I) and Explicit (E) Sets — Preregistered

The I/E partition must be fixed *a priori* to avoid circularity. Two acceptable operationalizations, both preregistered before touching state data:

- **Report-based (preferred where available):** E = signals from regions/stages whose activity, in an independent baseline task, predicts report/detection (e.g., late positivity / global-access nodes, higher-order association cortex); I = early/perceptual and subcortical-proxy stages that do not predict report at baseline.
- **Hierarchy-based (fallback):** E = higher-order association ROIs; I = primary sensory and low-level ROIs. Coarser but fully a priori.

The partition is a stipulation to be validated by whether it yields the signed pattern, not a claim that these regions "are" the implicit/explicit models.

### 5.3 Estimator and Pipeline

- **Toolbox:** IDTxl (Wollstadt et al., 2019) or JIDT (Lizier, 2014).
- **Estimator:** Kraskov–Stögbauer–Grassberger (KSG) nearest-neighbour estimator for continuous signals (bias-controlled, no binning). Discrete/symbolic TE as a robustness check.
- **Embedding:** non-uniform state-space embedding with Ragwitz optimization of embedding dimension and delay per target; maximum lag scanned and reported.
- **Significance:** permutation/surrogate testing with time-shifted and phase-randomized surrogates; multiple-comparison control (FDR) across source–target pairs.
- **Direction read-out:** compute both T_{I→E} and T_{E→I}; report net and each direction. The signed predictions in Table 1 refer to T_{I→E}. For REM, additionally split I into "sensory-input–driven" vs. "internally/parameter-driven" sources and test the predicted dissociation.
- **Criticality observables computed on the same epochs:** σ via the multi-timescale MR-estimator (Wilting & Priesemann, 2018) to avoid subsampling bias; λ_max via standard trajectory-divergence methods on reconstructed state space; α via DFA on amplitude envelopes. Report all three and their divergences (§3.2).

### 5.4 Confound Controls (Mandatory)

TE on neural data is vulnerable to well-known confounds; each is pre-committed to a control:

- **Volume conduction / field spread (EEG/MEG):** work in source space where possible; use TE variants and lags robust to instantaneous mixing; report both sensor and source results.
- **Spectral / SNR changes masquerading as information transfer:** psychedelics and anesthesia change broadband power. Control by (i) KSG (amplitude-invariant to monotonic transforms), (ii) matching/covarying SNR, (iii) reporting that the *directed* asymmetry (I→E vs E→I), not raw level, carries the prediction.
- **Non-stationarity:** epoch into quasi-stationary windows; test stationarity; use ensemble TE across trials/epochs rather than single long segments.
- **Sampling rate / downsampling artifacts:** report at native rate and one downsampled rate.
- **Reverse causation / common drive:** conditional/multivariate TE conditioning on other sources to reduce spurious pairwise links.

### 5.5 Success and Failure Criteria (Pre-committed)

- **Support:** the *signs* in Table 1 hold for global P (psilocybin ↑, propofol ↓ monotone with dose, NREM ↓), AND at least the REM directed-source dissociation (§4.1 #1) holds. Magnitude calibration is secondary.
- **Partial:** global signs hold but the discriminating divergence predictions (§4.1) fail — indicates the *permeability-as-TE* core survives but the gating-family decomposition is wrong.
- **Falsification:** global signs fail (e.g., propofol does not monotonically reduce T_{I→E}; REM shows sensory-driven I→E), OR the directed asymmetry vanishes once SNR is controlled (i.e., the "effect" was spectral power all along).

---

## 6. What This Buys, and What It Cannot

**Buys.** A metaphor becomes a number: "the boundary is more permeable under psychedelics" becomes "directed transfer entropy from implicit to explicit sources rises, driven by the serotonergic gate, monotonically with dose, with this spatial signature." That is falsifiable on data that already exist. It also makes the framework interoperable — TE connects to predictive-processing information measures, σ connects to the criticality literature, PCI provides convergent validity.

**Cannot.** This paper does not explain phenomenality, does not derive why criticality should matter, and does not claim the brain literally contains an "implicit model" and an "explicit model." The I/E partition is an operational instrument. Decomposition methods can manufacture apparent structure; the confound controls (§5.4) and the a-priori partition (§5.2) are there precisely because the honest failure mode — "the directed effect was spectral power" — must be given a fair chance to win. The value here is not truth about consciousness but *decidability* about one mechanism.

---

## References

Beggs, J. M., & Plenz, D. (2003). Neuronal avalanches in neocortical circuits. *Journal of Neuroscience*, 23(35), 11167–11177.

Bertschinger, N., & Natschläger, T. (2004). Real-time computation at the edge of chaos in recurrent neural networks. *Neural Computation*, 16(7), 1413–1436.

Boedecker, J., Obst, O., Lizier, J. T., Mayer, N. M., & Asada, M. (2012). Information processing in echo state networks at the edge of chaos. *Theory in Biosciences*, 131(3), 205–213.

Carhart-Harris, R. L., et al. (2014). The entropic brain: a theory of conscious states informed by neuroimaging research with psychedelic drugs. *Frontiers in Human Neuroscience*, 8, 20.

Casali, A. G., et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. *Science Translational Medicine*, 5(198), 198ra105.

Hardstone, R., et al. (2012). Detrended fluctuation analysis: a scale-free view on neuronal oscillations. *Frontiers in Physiology*, 3, 450.

Kanders, K., Lorimer, T., & Stoop, R. (2017). Avalanche and edge-of-chaos criticality do not necessarily co-occur in neural networks. *Chaos*, 27(4), 047408.

Lizier, J. T. (2014). JIDT: An information-theoretic toolkit for studying the dynamics of complex systems. *Frontiers in Robotics and AI*, 1, 11.

Priesemann, V., et al. (2013). Neuronal avalanches differ from wakefulness to deep sleep — evidence from intracranial depth recordings in humans. *PLOS Computational Biology*, 9(3), e1002985.

Priesemann, V., et al. (2014). Spike avalanches in vivo suggest a driven, slightly subcritical brain state. *Frontiers in Systems Neuroscience*, 8, 108.

Schreiber, T. (2000). Measuring information transfer. *Physical Review Letters*, 85(2), 461–464.

Shew, W. L., & Plenz, D. (2013). The functional benefits of criticality in the cortex. *The Neuroscientist*, 19(1), 88–100.

Vicente, R., Wibral, M., Lindner, M., & Pipa, G. (2011). Transfer entropy — a model-free measure of effective connectivity for the neurosciences. *Journal of Computational Neuroscience*, 30(1), 45–67.

Wibral, M., et al. (2014). *Directed Information Measures in Neuroscience*. Springer.

Wilting, J., & Priesemann, V. (2018). Inferring collective dynamical states from widely unobserved systems. *Nature Communications*, 9, 2325.

Wollstadt, P., et al. (2019). IDTxl: The Information Dynamics Toolkit xl. *Journal of Open Source Software*, 4(34), 1081.
