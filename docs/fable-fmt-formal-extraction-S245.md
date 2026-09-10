# S245 — FMT Formalization: Standalone Paper Extraction + Roadmap Demotion Fix

*Fable, S245. Deliverable for AIW backlog (roadmap over-claim fix + extractable paper).*
*Source: `paper/fmt_formal/fmt-formalization.md`. This file contains three parts:*
*(1) a standalone paper draft extracting §3 + §4.1–4.3, (2) the demotion rewrite for the parent roadmap's §4.4–4.5, (3) cleanliness notes on the other S244-flagged weaknesses.*
*Nothing here is committed to the source; this is a draft for MG review.*

---

# PART 1 — STANDALONE PAPER DRAFT

**Target venue (plausible):** *Entropy*, Special Issue "Models of Consciousness" (or the "Information Theory and Consciousness" track). Methods-and-predictions genre — an operationalization/registered-analysis proposal, not a claim of results. Estimated length ~5,200 words in this skeleton.

---

## Title

**Permeability as Directed Information Flow: A Transfer-Entropy Operationalization of the Implicit–Explicit Boundary in Consciousness, with Signed Predictions Across Pharmacological and Sleep States**

**Matthias Gruber**
*Independent researcher · ORCID 0009-0005-9697-1665 · matthias@matthiasgruber.com*

---

## Abstract

A recurring informal claim across theories of consciousness is that altered states — psychedelics, anesthesia, sleep, meditation — reflect changes in how much normally-unconscious ("implicit") information reaches conscious access ("explicit"). This "permeability" language is explanatorily productive but has lacked a measurable definition, leaving it unfalsifiable. Here I give permeability a precise operational definition as the **transfer entropy** (Schreiber, 2000) from substrate/implicit-processing signals to explicit/conscious-access signals, decomposed into a **channel-indexed gating family** that maps onto distinct neuromodulatory systems (serotonergic, GABAergic, dopaminergic, noradrenergic). I then define three complementary, already-standard **criticality observables** — the neuronal-avalanche branching ratio σ, the maximum Lyapunov exponent λ_max, and the detrended-fluctuation-analysis exponent α — as a joint operating-regime constraint, and I note that avalanche criticality and edge-of-chaos criticality are dissociable (Kanders et al., 2017) and must be measured separately. The core deliverable is a table of **signed, state-specific predictions**: each state (normal waking, psilocybin/LSD, high-dose *Salvia divinorum*, right-hemisphere-stroke anosognosia, NREM, REM, meditation, hypnagogia) is assigned a predicted direction of change in global transfer entropy, in channel-specific gating, and in the criticality observables, with divergence points that discriminate this account from an "entropy simply goes up" null. Finally I specify a concrete **Phase-1 analysis plan** on existing open psychedelic and anesthesia datasets — which recordings, which TE estimator (JIDT/IDTxl with Kraskov–Stögbauer–Grassberger estimation and Ragwitz embedding), which source/target ROIs, how effect signs are read off, and the confound controls (spectral, volume-conduction, and stationarity). The framework is deliberately theory-light: it operationalizes one mechanism and stakes it on directional predictions, so that it can be *clearly right or clearly wrong* on data that already exist.

**Keywords:** transfer entropy; consciousness; directed information flow; neuronal avalanches; branching ratio; criticality; psychedelics; anesthesia; effective connectivity

---

## 1. Introduction

### 1.1 The problem: "permeability" is productive but unmeasured

Across several frameworks, a shared intuition recurs: conscious states differ in how much information that is normally processed *outside* awareness becomes available *to* awareness. Psychedelics are described as "loosening" a filter; deep anesthesia as "closing" one; dreaming as awareness driven from within rather than from the senses. This intuition is explanatorily productive — it organizes an otherwise disparate phenomenology — but as usually stated it is a metaphor. "The boundary becomes more permeable" predicts nothing quantitative and can absorb almost any result post hoc. That flexibility is precisely what makes such claims scientifically weak.

The claim I make here is narrow and testable: **permeability is directed information flow from implicit-processing signals to explicit/conscious-access signals, and it is measurable, right now, as transfer entropy on existing neural recordings.** I am not proposing a new theory of consciousness. I am taking one mechanism that many theories invoke informally and giving it (i) a formal definition, (ii) a decomposition that respects known neuromodulatory pharmacology, and (iii) a table of signed predictions that a single re-analysis of open data could falsify.

### 1.2 Why transfer entropy

Transfer entropy (TE; Schreiber, 2000) measures the reduction in uncertainty about the future of a target time series *Y* given the past of a source *X*, beyond what *Y*'s own past already provides. It is model-free (no assumed functional form), directional (T_{X→Y} ≠ T_{Y→X} in general), and captures nonlinear dependencies — three properties that linear Granger causality lacks and that matter for neural data. TE is now a mature tool in neuroscience with validated estimators and confound controls (Vicente et al., 2011; Wibral et al., 2014; Lizier, 2014, JIDT; Wollstadt et al., 2019, IDTxl). This maturity is the point: the operationalization proposed here requires **no new mathematics**, only a disciplined application of established estimators to a specific source→target contrast, read with a specific sign convention.

### 1.3 What this paper delivers

Section 2 defines permeability as TE and decomposes it into a channel-indexed gating family aligned to neuromodulatory systems. Section 3 defines the three criticality observables and the dissociation problem. Section 4 is the signed-prediction table and the divergence points that separate this account from a generic "complexity tracks consciousness" claim. Section 5 is the Phase-1 analysis plan on named open datasets, including estimator choice, ROI selection, sign read-out, and confound controls. Section 6 states the limits honestly: this is a measurement framework for one mechanism, not a theory of phenomenality, and the "implicit/explicit" partition is an operational stipulation to be validated, not a claim that the brain contains two boxes.

---

## 2. Permeability as Transfer Entropy

### 2.1 Definition

Let the neural state be observed as a set of time series. Partition channels (or sources) into two operational classes by an *a priori*, preregistered criterion (§5.2): an **implicit set** I — signals from processing stages that do not, in the baseline state, correlate with report/conscious access — and an **explicit set** E — signals from stages that do. Define permeability as the transfer entropy from I to E:

> **P ≡ T_{I→E} = Σ p(e_{t+1}, e_t^{(k)}, i_t^{(l)}) · log [ p(e_{t+1} | e_t^{(k)}, i_t^{(l)}) / p(e_{t+1} | e_t^{(k)}) ]**

where e_t^{(k)} and i_t^{(l)} are the k- and l-dimensional delay embeddings of the explicit and implicit signals (Takens embedding; dimension and lag set by the Ragwitz criterion, §5.3). P has units of bits (or nats) per sample and is intrinsically directional: it is the extra predictability of the *explicit* future contributed by the *implicit* past.

This is the entire formal core. Everything downstream is (a) how to decompose P, (b) what regime the substrate must be in for P to be meaningful, and (c) which direction P and its components should move in each state.

### 2.2 Global vs. local permeability

P can be computed globally (pooled or averaged over all I→E pairs) or locally (for a specific implicit source region → explicit target region). This distinction is load-bearing:

- **Global P** captures whole-brain shifts — the account of psychedelics (uniform increase) and deep anesthesia (uniform collapse).
- **Local P** captures domain-specific deficits — the account of anosognosia, where transfer from a specific damaged domain fails while the rest of the brain is normal.

The same quantity, at two spatial scales, distinguishes a global pharmacological effect from a focal lesion effect. This is a genuine, non-trivial consequence of the definition.

### 2.3 The gating family: one knob is wrong

Permeability is not a single scalar. In biological brains, the implicit→explicit boundary is modulated independently by several neuromodulatory systems, across channels, regions, and cortical layers. Collapsing them into one "permeability knob" would predict that all state changes look alike, which is false. I therefore define a **gating family**

> **G = { g_c : c ∈ C },  g(t) = ∏_{c∈C} g_c(t)**

indexed by modulatory channel c ∈ C = {5-HT, GABA, DA, NA, …}, where each g_c ∈ [0,1]^{N_c} is a spatially resolved gate (N_c = region/column/voxel count at the analysis scale) and the composite gate is the element-wise product. A scalar "permeability" is recovered as a summary statistic (e.g., the spatial mean of g), but the *fundamental* quantity is the channel-indexed family. Empirically, G is not directly observed; it is inferred from the pharmacology of the manipulation (which receptor system the drug targets) crossed with the spatial pattern of the measured TE change.

The decomposition earns its keep by making **channel-specific signed predictions** (§4): serotonergic agonism should raise TE broadband and globally; GABAergic agonism should suppress TE globally; dopaminergic modulation should change *which* implicit content crosses (the spatial/scope pattern) without necessarily changing the *total*; focal lesions should knock out TE in a specific pathway only. These four signatures are distinguishable in data, which is the whole point of refusing the single-knob model.

### 2.4 Total conscious content (auxiliary scalar)

For convenience I define a single scalar summarizing the "amount" of explicit processing available to be driven, C(t), as the total explicit-side activity above the conscious-access criterion. C(t) is offered only as the quantity expected to co-track existing whole-brain complexity indices — the Perturbational Complexity Index (PCI; Casali et al., 2013) and Lempel–Ziv complexity — providing an external convergent-validity check. It is not part of the core TE claim and carries no independent theoretical weight here.

---

## 3. Criticality Observables

Permeability is only interpretable if the substrate is in a dynamical regime that *can* transmit information over distance without either dying out or exploding into noise. That regime is criticality. I do not here argue *why* consciousness should require criticality (that is a separate, and contested, theoretical claim — see Part 2 of this document and §6). I take the weaker, purely operational position: **report the operating regime alongside the permeability measurement, using three already-standard observables, and treat their relationship as an empirical question.**

### 3.1 Three measures

- **Branching ratio σ** — mean number of descendant activations per ancestor across neuronal avalanches (Beggs & Plenz, 2003; Shew & Plenz, 2013; MR-estimator, Wilting & Priesemann, 2018). σ<1 subcritical, σ=1 critical, σ>1 supercritical. The empirical consciousness-criticality literature (ConCrit; and Priesemann et al., 2013, 2014) centers on σ, with the awake brain slightly subcritical (σ ≈ 0.95–0.99).
- **Maximum Lyapunov exponent λ_max** — separation rate of nearby trajectories (Bertschinger & Natschläger, 2004; Boedecker et al., 2012). λ_max<0 ordered, λ_max≈0 edge of chaos, λ_max>0 chaotic. This is the measure most directly tied to the "edge of chaos" intuition.
- **DFA exponent α** — long-range temporal autocorrelation / scale-free structure of oscillation amplitude envelopes (Hardstone et al., 2012). α≈0.5 uncorrelated, α≈1 critical, long-range correlated.

### 3.2 The dissociation problem — measure them separately

Kanders et al. (2017) showed that avalanche criticality (σ≈1) and edge-of-chaos criticality (λ_max≈0) do **not** necessarily co-occur: they index different phase transitions. This is a methodological warning, not a theoretical thesis. The operational consequence is concrete: **do not assume one measure stands in for the others.** Compute σ, λ_max, and α independently, and report states where they diverge as the most informative cases — a state that is avalanche-critical but not edge-of-chaos (or vice versa) is exactly where competing theoretical readings make different bets. In this paper I make no claim about which measure is "primary"; I claim only that reporting all three, and their divergences, is the honest way to characterize regime.

### 3.3 The regime constraint (operational, not derived)

For the permeability predictions below to be interpretable, I assume only that a conscious, responsive baseline sits in the empirically observed near-critical band (σ roughly in [0.95, 1.1]; λ_max near 0; α near 1). This is an *observed regularity* imported from the criticality literature, used here as a covariate/inclusion criterion — not a derived necessity. The stronger claim that self-referential architecture *entails* criticality is explicitly excluded from this paper (see Part 2 for why that chain is a conjecture, not a deduction).

---

## 4. Signed Predictions

The framework's empirical content is a set of **signed, state-specific predictions**. Each state is assigned (i) a direction for global P = T_{I→E}, (ii) the channel(s) of G expected to drive it, (iii) any local/domain anomaly, and (iv) the expected criticality-observable movement. Signs, not magnitudes, are the primary commitment — magnitudes are dataset-dependent and calibrated in Phase 1.

**Table 1. Predicted signed changes relative to normal waking baseline.**

| State | Global P (T_{I→E}) | Driving channel(s) in G | Local anomaly | Criticality observable |
|---|---|---|---|---|
| Normal waking | baseline | selective gating | none | σ≈0.95–0.99; λ_max≈0; α≈1 |
| Psilocybin / LSD | ↑↑ (broadband) | g_{5-HT} ↑ globally | none (global) | σ → 1 (toward/just past critical); α ↑ |
| *Salvia divinorum* (high dose, κ-opioid) | ↑ but ESM-selective collapse | g_{κ} disrupts self-scope gating | T_{I→E} to self-referential targets → 0; T_{I→E} to exteroceptive targets ↑ | regime near-critical but reorganized |
| Anosognosia (R-hemisphere stroke) | ≈ normal (most domains) | structural loss of g_c in one pathway | domain-specific T_{I→E} deficit | global σ near baseline |
| NREM (deep sleep) | ↓↓ (near zero) | uniform gate suppression | uniform | σ < 1 (subcritical); PCI ↓ |
| REM dreaming | medium, **internally sourced** | endogenous drive | T from stored parameters ↑; T *from sensory input* → 0 | σ near waking; PCI near waking |
| Meditation (trained) | selectively ↑ | domain-specific g_c control | trained target domains only | α ↑ in trained bands |
| Hypnagogia / sleep onset | gradually ↑ then variable | rising baseline gate noise | bottom-up onset (low→high level) | drift toward subcritical |

### 4.1 The divergence points (what makes this falsifiable, not vacuous)

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

### 5.2 Defining the implicit (I) and explicit (E) sets — preregistered

The I/E partition must be fixed *a priori* to avoid circularity. Two acceptable operationalizations, both preregistered before touching state data:

- **Report-based (preferred where available):** E = signals from regions/stages whose activity, in an independent baseline task, predicts report/detection (e.g., late positivity / global-access nodes, higher-order association cortex); I = early/perceptual and subcortical-proxy stages that do not predict report at baseline.
- **Hierarchy-based (fallback):** E = higher-order association ROIs; I = primary sensory and low-level ROIs. Coarser but fully a priori.

The partition is a stipulation to be validated by whether it yields the signed pattern, not a claim that these regions "are" the implicit/explicit models.

### 5.3 Estimator and pipeline

- **Toolbox:** IDTxl (Wollstadt et al., 2019) or JIDT (Lizier, 2014).
- **Estimator:** Kraskov–Stögbauer–Grassberger (KSG) nearest-neighbour estimator for continuous signals (bias-controlled, no binning). Discrete/symbolic TE as a robustness check.
- **Embedding:** non-uniform state-space embedding with Ragwitz optimization of embedding dimension and delay per target; maximum lag scanned and reported.
- **Significance:** permutation/surrogate testing with time-shifted and phase-randomized surrogates; multiple-comparison control (FDR) across source–target pairs.
- **Direction read-out:** compute both T_{I→E} and T_{E→I}; report net and each direction. The signed predictions in Table 1 refer to T_{I→E}. For REM, additionally split I into "sensory-input–driven" vs. "internally/parameter-driven" sources and test the predicted dissociation.
- **Criticality observables computed on the same epochs:** σ via the multi-timescale MR-estimator (Wilting & Priesemann, 2018) to avoid subsampling bias; λ_max via standard trajectory-divergence methods on reconstructed state space; α via DFA on amplitude envelopes. Report all three and their divergences (§3.2).

### 5.4 Confound controls (mandatory)

TE on neural data is vulnerable to well-known confounds; each is pre-committed to a control:

- **Volume conduction / field spread (EEG/MEG):** work in source space where possible; use TE variants and lags robust to instantaneous mixing; report both sensor and source results.
- **Spectral/SNR changes masquerading as information transfer:** psychedelics and anesthesia change broadband power. Control by (i) KSG (amplitude-invariant to monotonic transforms), (ii) matching/covarying SNR, (iii) reporting that the *directed* asymmetry (I→E vs E→I), not raw level, carries the prediction.
- **Non-stationarity:** epoch into quasi-stationary windows; test stationarity; use ensemble TE across trials/epochs rather than single long segments.
- **Sampling rate / downsampling artifacts:** report at native rate and one downsampled rate.
- **Reverse causation / common drive:** conditional/multivariate TE conditioning on other sources to reduce spurious pairwise links.

### 5.5 Success and failure criteria (pre-committed)

- **Support:** the *signs* in Table 1 hold for global P (psilocybin ↑, propofol ↓ monotone with dose, NREM ↓), AND at least the REM directed-source dissociation (§4.1 #1) holds. Magnitude calibration is secondary.
- **Partial:** global signs hold but the discriminating divergence predictions (§4.1) fail — indicates the *permeability-as-TE* core survives but the gating-family decomposition is wrong.
- **Falsification:** global signs fail (e.g., propofol does not monotonically reduce T_{I→E}; REM shows sensory-driven I→E), OR the directed asymmetry vanishes once SNR is controlled (i.e., the "effect" was spectral power all along).

---

## 6. What This Buys, and What It Cannot

**Buys.** A metaphor becomes a number: "the boundary is more permeable under psychedelics" becomes "directed transfer entropy from implicit to explicit sources rises, driven by the serotonergic gate, monotonically with dose, with this spatial signature." That is falsifiable on data that already exist. It also makes the framework interoperable — TE connects to predictive-processing information measures, σ connects to the criticality literature, PCI provides convergent validity.

**Cannot.** This paper does not explain phenomenality, does not derive why criticality should matter, and does not claim the brain literally contains an "implicit model" and an "explicit model." The I/E partition is an operational instrument. Decomposition methods can manufacture apparent structure; the confound controls (§5.4) and the a-priori partition (§5.2) are there precisely because the honest failure mode — "the directed effect was spectral power" — must be given a fair chance to win. The value here is not truth about consciousness but *decidability* about one mechanism.

---

## References (paper subset — inherited from source, plus additions)

Beggs & Plenz (2003) *J. Neurosci.* 23:11167. · Bertschinger & Natschläger (2004) *Neural Comput.* 16:1413. · Boedecker et al. (2012) *Theory Biosci.* 131:205. · Carhart-Harris et al. (2014) *Front. Hum. Neurosci.* 8:20. · Casali et al. (2013) *Sci. Transl. Med.* 5:198ra105. · Hardstone et al. (2012) *Front. Physiol.* 3:450. · Kanders, Lorimer & Stoop (2017) *Chaos* 27:047408. · Lizier (2014) *Front. Robot. AI* 1:11 (JIDT). · Priesemann et al. (2013) *PLoS Comput. Biol.* 9:e1002985; (2014) *Front. Syst. Neurosci.* 8:108. · Schreiber (2000) *Phys. Rev. Lett.* 85:461. · Shew & Plenz (2013) *Neuroscientist* 19:88. · Vicente et al. (2011) *J. Comput. Neurosci.* 30:45. · Wibral et al. (2014) *Directed Information Measures in Neuroscience*, Springer. · Wilting & Priesemann (2018) *Nat. Commun.* 9:2325 (MR-estimator). · Wollstadt et al. (2019) *JOSS* 4:1081 (IDTxl).
*(All present in or consistent with the source reference list; JIDT/IDTxl/MR-estimator/Wilting–Priesemann added as they are required to specify the Phase-1 estimator honestly.)*

---
---

# PART 2 — DEMOTION FIX FOR THE PARENT ROADMAP (§4.4–4.5)

**Problem (S244 finding).** §4.4 presents a two-step chain — *self-referential closure ⇒ universal computation ⇒ Class 4 ⇒ criticality* — as a **deduction** ("not as an empirical observation but as a deductive consequence"). This is the ONLY thing the roadmap claims to have derived, and both bridges fail:

- **Bridge 1 fails:** self-modeling does **not** imply Turing-universality. A system can represent aspects of its own dynamics without being able to compute every computable function. "Models the process that generates it" is not equivalent to "can simulate an arbitrary program." No proof connects them; it is asserted.
- **Bridge 2 fails:** Wolfram's "PCE / Class-4-universality" is a *conjecture*, and even as conjectured it runs the other way from what the text needs. Rule 110 (and Life) are *proven* universal; but (a) universality has been *proven* for only specific Class-4 rules, not the class, (b) Class 4 is **not necessary** for universality (universal systems exist that aren't naturally classed as Class 4), and (c) "universal computation ⇒ operates at/near criticality" is not established — universality is about what a system *can* compute, not the dynamical regime it *sits in* during operation.

So the chain must be relabeled from *deduction* to *conjecture with two explicitly-open lemmas*. Replacement prose below.

---

### Replacement for §4.4 — "Criticality as a Conjectured Prerequisite (Two Open Lemmas)"

> **§4.4 Criticality: a conjectured, not derived, prerequisite**
>
> The parent theory treats operation near criticality (Wolfram Class 4 / edge of chaos) as a requirement for consciousness. It is tempting to try to *derive* this requirement from the theory's commitment to self-referential closure, via the chain
>
> > self-referential closure ⇒ universal computation ⇒ Class-4 dynamics ⇒ criticality.
>
> **I state plainly that this chain is a conjecture, not a proof.** It is offered as a research target — a structure that *would*, if established, upgrade criticality from an empirical correlate to a consequence — and it rests on two lemmas that are, at present, **open**:
>
> - **Lemma L1 (closure ⇒ universality) — OPEN.** *Does self-referential closure (a system whose explicit self-model represents the dynamics that generate that very self-model) entail computational universality (the capacity to simulate an arbitrary program)?* This is **not** established. Self-representation of one's own dynamics is not known to be equivalent to Turing-universality; a system may faithfully model salient aspects of its own operation while being computationally weaker than a universal machine. No proof is known to the author, and the implication may well be false as stated. What can be said rigorously is only that deeper recursive self-modeling requires *more* computational resource (a monotonicity claim), not that it requires *universal* resource.
>
> - **Lemma L2 (universality ⇒ criticality) — OPEN.** *Does computational universality require, or even imply, operation at or near a critical dynamical regime (Class 4 / edge of chaos)?* This is **not** established, and the standard results point the other way. (i) Wolfram's principle relating Class 4 to universality is itself a **conjecture** (the Principle of Computational Equivalence), not a theorem. (ii) Universality has been **proven only for specific rules** (Rule 110, Conway's Life), not for Class 4 as a class. (iii) Class-4 behavior is **not necessary** for universality — universal computation is realized by systems that are not naturally described as edge-of-chaos. (iv) Most importantly, universality is a statement about what a system *can compute in principle*, whereas criticality is a statement about the *dynamical regime it occupies during operation*; the two are logically distinct, and one does not obviously entail the other.
>
> Accordingly, the criticality requirement in this theory should be read as an **empirically motivated operating-regime hypothesis** — well supported as a *correlation* by the consciousness-criticality literature (§4.2–4.3) — and the "deductive" chain above should be pursued as an open program: *if* L1 and L2 can each be proven (or given a precise restricted form under which they hold), *then* criticality follows; until then, it does not. Nothing else in the formalization depends on the derivation succeeding. The transfer-entropy permeability formalism (§3) and the criticality *observables* (§4.2–4.3) stand entirely on their own as empirical instruments, independent of whether L1 and L2 are ever closed.

---

### Replacement for §4.5 — "The Two-Threshold Formalization (as conjunction, not entailment)"

> **§4.5 The two thresholds as a conjunction**
>
> The theory posits two thresholds — a criticality regime and a self-simulation architecture. Formally these combine as a **conjunction of independently-stated requirements**:
>
> > Consciousness (of the human type) ⟹ [ criticality-observables in the near-critical band ] ∧ [ self-simulation architecture: significant modeling mass on both self and world, at both implicit and explicit levels ].
>
> Both conditions are asserted to hold together, and each is independently motivated: a critical substrate without self-modeling (e.g., a sandpile at its critical point) has complex dynamics but no self-simulation; an architecture with the right model profile but driven below criticality (e.g., deep propofol anesthesia) retains the structural capacity but cannot instantiate the simulation.
>
> **I explicitly do *not* claim that the first condition entails the second, nor the reverse.** The earlier draft asserted that the architectural threshold *entails* the criticality threshold "via the universal-computation bridge." That entailment is exactly the conjectured chain of §4.4, resting on the open lemmas L1 and L2. Until those lemmas are proven, the two thresholds are stated as **co-required but logically independent** — an empirically-motivated conjunction, not a derived implication. If L1 and L2 are later established, this conjunction can be strengthened to an entailment; that strengthening is a stated goal of the formalization program, not a present result.

---
---

# PART 3 — CLEANLINESS NOTES (keep the extracted paper free of these S244-flagged weaknesses)

These are the other over-reaches in the roadmap. The Part-1 paper was written to **exclude** all of them. Notes for MG and for the roadmap's own hygiene:

**(a) The "Fokker–Planck" misnomer (roadmap §3.4).** The equation `∂ρ/∂t = −∇·(vρ) + D∇²ρ + S` is called a Fokker–Planck equation, but it is not one: it has a **source/sink term S** and its ρ is not a conserved probability density, so it is properly a **reaction–advection–diffusion (RAD) equation**. A Fokker–Planck equation conserves probability and has no source term. Worse, ρ is **overloaded three ways** in the source document: (i) the model *density* ρ(s,ν,t) in §2; (ii) the group-representation ρ(g) in the Oizumi principal-bundle passage §2.5 (`f(g·x)=ρ(g)·f(x)`); (iii) the recursive representation map ρ_n in §6.3. Three distinct objects, one symbol. **Fix for roadmap:** rename the dynamics "reaction–advection–diffusion" (drop "Fokker–Planck"); rename the symbols (e.g., density → μ or ρ_M; keep ρ(g) as the group rep; recursion map → R_n). **Extracted paper:** omitted entirely — Part 1 uses TE and the criticality observables, never the density PDE, so the misnomer cannot leak in.

**(b) Cybenko / universal-approximation misapplication (roadmap §6.5).** The text claims the six-layer neocortex "exceeds the three-layer minimum for universal function approximation (Cybenko, 1989)." This misreads the Universal Approximation Theorem: Cybenko's result is about **width** (a single hidden layer of *unbounded width* suffices), not about **depth** — there is no "three-layer minimum," and "layers" in the UAT sense (input/hidden/output of an MLP) are **not** the histological laminae of cortex. Equating cortical laminae with ANN layers is a category error. **Fix for roadmap:** delete the Cybenko sentence or replace with an honest statement (cortical depth may provide representational/recurrent capacity; the UAT is not the relevant theorem and does not license a "minimum layer" claim). **Extracted paper:** not present — §6 is out of scope for Part 1.

**(c) Category-theory "forking as coproduct" (roadmap §7.4).** Presenting virtual-model forking (DID) as a categorical **coproduct** `F(x)=ESM_1 ⊔ … ⊔ ESM_n` is decoration: nothing in the account uses the universal property of the coproduct (no maps out, no proof the construction is a coproduct rather than merely a disjoint union of states), and §7's functor/natural-transformation apparatus does no computational work the plainer dynamical statements don't already do. **Recommendation:** keep category theory out of the extracted paper entirely; in the roadmap, either drop §7.4 or reduce it to **one honest paragraph** flagged as suggestive analogy ("the disjoint, mutually-exclusive coexistence of multiple self-models is *suggestive* of a coproduct-like structure; making this precise — identifying the relevant universal property — is deferred"). **Extracted paper:** contains no category theory. Clean.

**Net effect:** Part 1 stands on Schreiber-2000 TE (used correctly), the three standard criticality observables (used as observables, with the dissociation caveat), and signed directional predictions on existing data. It inherits none of (a)–(c), and it drops the §4.4–4.5 over-claim that Part 2 demotes.
