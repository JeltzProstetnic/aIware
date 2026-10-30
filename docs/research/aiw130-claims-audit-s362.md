# AIW-130 JAIC draft: claims audit against crucible withdrawals (S362, 2026-10-27)

Audited file: `drafts/aiw130-jaic-draft.md` (303 lines, last edited 2026-10-21). Audit only; the manuscript was not touched.

**Verdict: the theory sections hold. Section 6(b), the Section 8 "corroborated" paragraph and the Conclusion claim in-silico results the published companion v6 does not report. Fix those before submission.**

**Counts: 10 BLOCKER, 11 MAJOR, 15 MINOR.**

## Yardsticks used

| Yardstick | Path |
|---|---|
| Must-NOT-claim list | `~/crucible/docs/cru226-juelich-substance.md` §4 (lines 278–313) |
| Published companion v6 (concept 10.5281/zenodo.21610993, v6 10.5281/zenodo.23702509) | `drafts/companion-computational-paper-draft.md` |
| Theory rulings | `.claude/knowledge/fmt-misconception-registry.md`; `docs/decisions.md` (S329 l.655–659, S281 l.365–367, S342 l.677–687, S359 l.759/764); `.claude/knowledge/prediction-framing.md` l.32–44 |
| Crucible primaries | `~/crucible/docs/results/p1-causal-transfer.md`; `cru201-six-confirmations-audit-2026-09-30.md`; `~/crucible/docs/model-explainer/index.html` l.243–246 (P2 = interaction, status "NEXT", never confirmed) |
| Kanai & Ma (2026b) | local full text `literature/fulltext/Kanai2026.pdf` (arXiv:2606.15348v1, 13 Jun 2026, 27 pp), extracted with PyMuPDF |

What the draft does **not** do, checked against the CRU-226 §4 list: it quotes no FlowBody result (route A/B, CRU-206, CRU-210), says nowhere that our systems "operate at criticality" or sit at σ≈1, cites no CRU-108 energy figure, does not use A#1 ("closure maintains a model"), A#6, CRU-69/74/139, makes no 1M-neuron or scale claim, and does not repeat the "wired bottleneck has not run" sentence. The draft's problems are elsewhere: it describes companion results that do not exist in v6, and it calls a *predicted* interaction *banked*.

---

## BLOCKERS (false, or cites something the source does not contain)

### B1 — l.152, first sentence
> "In simulation we can already show that the checks separate systems that differ in the target structure."

**Wrong:** none of the three checks has ever been run. The companion measures task capability (transfer, planning depth, survival, parity accuracy). It reports no clamp sweep, no κ, no $L_W$ and no check-3 signature. Companion §4 (l.109–159) and §8 (l.242): "mechanism demonstrations … they do not establish the scaled dependency"; grep of the companion for `clamp|κ|L_W|attractor|novelty rate` returns nothing.
**Replace:** "In simulation the companion reports capability dissociations that bear on the structures the checks target; none of them runs the checks themselves."

### B2 — l.152
> "And open-ended computation does real, demand- and scale-gated work: the compute advantage of the generative regime appears only for tasks of intermediate difficulty and sharpens as the system grows, so open-ended computation contributes measurably to task performance."

**Wrong:** this is the old CRU-40 Part A edge-peak reading. Companion §4.4 (l.135–141) now says the peak "lies in the ordered regime", 0 of 30 seeds near λ=0, it "coincides with the peak of linear recall … so the gating is a memory-horizon effect", and "it is not evidence that the edge pays". §7 (l.234): "Whether operating at the edge pays remains untested." CRU-201 audit: one of the "six confirmations" shows the peak; two are nulls and two run *against* an edge peak.
**Replace:** "In a rate reservoir an accuracy peak appears only for tasks of intermediate difficulty. It replicates on 30 of 30 fresh reservoirs, but it lies in the ordered regime and moves with the task's memory horizon, so it is not evidence that operating at the edge of chaos pays (Gruber, 2026b, §4.4)."

### B3 — l.154
> "The banked positive results are the ones where open-ended computation and closure are present *together* on a differentiated substrate; closure alone and the generative regime alone are null or weak."

**Wrong:** no banked result manipulates the regime and closure together. The closure × criticality interaction is crucible prediction **P2**, status "NEXT — CRU-40" (`~/crucible/docs/model-explainer/index.html` l.243–246) and was never confirmed. `prediction-framing.md` l.74 lists it as *the discriminating prediction*, not a result. The companion's positive capability results (§4.1–4.3) were obtained on a gridworld planner, a toy survival room and an ESN fixed at spectral radius 0.95, with no regime manipulation. So "closure alone … null" is contradicted by the companion's own positives. CRU-226 §4 item 3 also bans any closure-necessity claim.
**Replace:** "The companion does not test closure and the open-ended regime together. Its positive results were obtained with no regime manipulation, and the closure × regime interaction FMT predicts is untested. One toggle of re-entry on an undifferentiated spiking reservoir gave no advantage on a task the passive reservoir already solved (Gruber, 2026b, §6), which the framework expects: a loop between two things needs two things."

### B4 — l.156, last two sentences
> "…on the spiking side, a branching ratio counts toward that comparison only when it departs from the value a rate-matched surrogate produces. These ablations are the experimental content of the claim that the checks discriminate: each check has a manipulation that should, and in the toy systems does, move the readout it is responsible for while leaving the others fixed."

**Wrong:** "and in the toy systems does" is false. No regime ablation with closure, and no rate-reservoir versus self-organizing spiking-pool baseline, appears in the companion. Companion §4.4 l.139: the spiking pool "could not test location". CRU-201: the one spiking "confirmation" (CRU-40 B0) was a null whose band came from a rate-meter σ.
**Replace (last sentence):** "These ablations are the experiments the checks call for. Each specifies a manipulation that should move the readout its check is responsible for while leaving the others fixed. None has yet been run as specified."

### B5 — l.124 (Box 1)
> "That $L_W$ (obtained by structural, capacity-matched suppression) tracks the clamp-defined $\kappa$ is an empirical assumption, validated in the companion (Gruber, 2026b), not an identity."

**Wrong:** the companion contains no κ, no $L_W$ and no clamp sweep. The sentence cites a validation that does not exist.
**Replace:** "That $L_W$ (obtained by structural, capacity-matched suppression) tracks the clamp-defined $\kappa$ is an empirical assumption, not an identity, and it has not yet been tested."

### B6 — l.150
> "…every branching ratio is reported beside a rate-matched surrogate, and the capability itself is established by task performance and a closed-loop perturbation test (Gruber, 2026b). … The design and its instantiation choices are given in the in-silico companion (Gruber, 2026b)."

**Wrong:** companion v6 has no minimal open-ended spiking substrate design, no homeostatic/STDP pool, no self-basin and no closed-loop perturbation test (grep `homeostatic|STDP|self-basin|closed-loop perturbation`: no hits). The present tense ("is reported", "is established") also reads as done work for a design the same paragraph calls "not yet instantiated". The rate-meter fact itself is in the companion (§3.2 l.105) and may be cited.
**Replace:** "A branching ratio near unity would not count as evidence of the regime: a subsampled branching estimate reaches unity on firing rate alone (Gruber, 2026b, §3.2). Every branching ratio would therefore be reported beside a rate-matched surrogate, and the capability would be established by task performance." Delete the last sentence ("The design and its instantiation choices are given in the in-silico companion"), or point it at a document that actually contains the design.

### B7 — l.158
> "The **decisive test is open**: a scaled, spiking, closure-driven open-ended modeller whose capability *dies* when the loop is cut has not yet been built."

**Wrong:** this states the decisive test in exactly the form the published companion rejects. Companion §8 l.244: "It is tempting to state the open test as whether a scaled, closure-driven modeller *loses its modelling capability* when the loop is cut. That test cannot come out positive … **The claim is instead about cost at matched function on an open-ended workload**." See also §7 l.234 ("No result here licenses 'closure enables what feedforward cannot'") and CRU-226 §4 item 3 (five kills plus the stationary-closure theorem).
**Replace:** "The decisive test is open, and it is not a loop-cut. On a deterministic, stationary task a finite closed loop unrolled over a finite horizon is feedforward plus memory, so a test of whether capability dies when the loop is cut cannot come out positive (Gruber, 2026b, §8). The test the theory commits to is cost at matched function on an open-ended workload: how much more a cut system pays to reach the same behaviour, and whether that gap grows with the openness of the task."

### B8 — l.162
> "It licenses the claim that the checks are *implementable* and *discriminating* at toy scale: one can build systems that differ in the target structure and show that the readouts move as the theory says. … Reported this way, the evidence is a proof that the detector is runnable and a set of dissociations consistent with the mechanism — no more, and no less."

**Wrong:** the readouts (κ, $L_W$, the check-3 signature) were never measured, so "show that the readouts move" and "a proof that the detector is runnable" are false. Same sources as B1.
**Replace:** "It licenses the claim that the checks are specified precisely enough to implement, and that toy systems built with and without the target components differ in capability as the theory expects. It does not license the claim that the checks have been run, that any built system is conscious, or that the mechanism has been shown at the capacity FMT holds consciousness requires. … Reported this way, the evidence is a specification of a runnable detector plus a set of capability dissociations consistent with the mechanism."

### B9 — l.196
> "On the corroborated side sit the in-silico dissociations of Section 6: that a self-model carries a capability its ablation cannot, that a self-model-gated planner scales where reactive policies plateau, and that the closure advantage is an interaction with the open-ended regime rather than a main effect."

**Wrong:** the third item is a prediction (see B3), not a corroboration. The first overstates the transfer result (see M3): the ablation removes the generating projection, and the companion "pre-concedes" that the result is not unique to FMT (§4.3 l.131, §8 l.246).
**Replace:** "On the corroborated side sit the companion's toy-scale capability results reported in Section 6. Removing the projection that generates a self/other model abolishes a transfer capability, a result shared with causal-representation learning and not unique to FMT. A self-model-gated planner scales with depth where reactive policies fail at a fixed sample budget. The predicted interaction between closure and the open-ended regime is untested."

### B10 — l.200 (Conclusion)
> "The procedure is grounded by a buildable minimal open-ended spiking substrate and by in-silico dissociations whose discriminating result is an interaction, with the decisive scaled test stated as open."

**Wrong:** same as B3/B9: no interaction result exists.
**Replace:** "The procedure is specified down to a buildable minimal open-ended spiking substrate and is motivated by toy-scale capability dissociations; the checks themselves, and the decisive scaled test, have not yet been run."

---

## MAJOR (over-claims)

### M1 — l.10 (Abstract)
> "…in-silico dissociations show they discriminate; a worked embodied example illustrates…"

**Over-claim:** the checks were never run (B1). The abstract is 149 words against JAIC's 150 limit, so the replacement keeps the length.
**Replace:** "…toy-scale in-silico dissociations motivate them; a worked embodied example illustrates…"

### M2 — l.24, also l.198
> "This paper supplies all three. … and with in-silico dissociations that show they discriminate."

**Over-claim:** "supplies all three" is stronger than the draft's own §5 ("a candidate answer, not a settled criterion") and §4 ("to the extent the extraction is not yet fully automated at scale"). It also runs against MG S281 (`decisions.md` l.366): *"there was no need whatsoever to mention that we 'complete' or anything their work."* The last clause repeats M1.
**Replace (l.24):** "This paper proposes an answer to each. … and with toy-scale in-silico dissociations that bear on the structures the checks target." **(l.198):** "This paper proposes an answer to each."

### M3 — l.152
> "An explicit self/other model causally carries a capability its ablation cannot: in a survival task requiring transfer of a learned avoidance to previously unobserved situations, agents equipped with an explicit self-model transferred the avoidance where matched controls did not — an ability that vanished under a capacity- and recurrence-matched ablation of the self-model, with a large reported effect (Cohen's $d \approx 2.4$…)."

**Over-claim, and factually off:**
- It is an observational-to-outcome transfer task in a 9×7 gridworld, not a survival task.
- The ablation removes the self/other *projection*; the model itself cannot be cut (companion §4.3 l.129).
- Neither the companion nor `p1-causal-transfer.md` describes the ablation as "capacity- and recurrence-matched".
- One "matched control", Q-learning, scored 0.94 through a tie-break artefact (`p1-causal-transfer.md`).
- The required non-uniqueness concession is missing (companion §4.3 l.131; `prediction-framing.md` l.70 "pre-concede").

**Replace:** "In an observational-to-outcome transfer task, an agent whose explicit self/other model is generated by a dedicated projection avoids a novel hazard that shares a witnessed mechanism (0.98). The same agent with that projection removed stays at chance (0.78; Cohen's $d$ = 2.44, 40 seeds; Gruber, 2026b, §4.3). The result is shared with causal-representation learning and is not evidence for FMT over its rivals."

### M4 — l.152
> "A self-model-gated planner scales with problem depth where a full bracket of competent reactive policies — tabular Q-learning, ensemble fitted-Q, behavioural cloning, and hand-built heuristics — plateaus."

**Over-claim:** the fixed-budget qualifier is missing. Companion §4.1 l.117: "Nothing here claims a reactive architecture could not reach the same behaviour with more; the comparison is what each buys per sample." The bracket scores 0.00–0.33; it fails rather than plateaus.
**Replace:** "A self-model-gated planner scales with problem depth where a bracket of reactive policies (tabular Q-learning, ensemble fitted-Q, behavioural cloning and hand-built heuristics) scores 0.00–0.33 at the same sample budget (Gruber, 2026b, §4.1); nothing shows the reactive policies could not reach the behaviour with more samples."

### M5 — l.22
> "Section 9.2 states that their framework operationalizes the *search* for consciousness-relevant structure but needs a substantive theory to fix the target — the tier-III, dynamics-internal structure itself."

**Misrepresents Kanai & Ma:** §9.2 says theories "can guide the search for the tier-III target", while the target is fixed by the system itself. §4.5: "A theory may help us discover or approximate an intrinsic partition, but it does not constitute the partition as intrinsic." §9.2: the definitions "do not say that a theory of consciousness creates the relevant structure". Kanai is JAIC's EiC.
**Replace:** "Section 9.2 places the consciousness-relevant structure in 'a tier-III, dynamics-internal feature of the system itself' and assigns theories the job of guiding the search for it, by proposing which interventions and readouts may reveal it."

### M6 — l.38
> "Recurrent realizers pass; tables and unfolded nets fail."

**Over-claim of the cited paper:** in Kanai & Ma §4.7 the unfolded net fails ICCR only *if* the persistent recurrent component belongs to the target: "Whether the persistent component is in fact consciousness-relevant is a tier-II/III question the framework deliberately leaves open."
**Replace:** "If the persistent recurrent component belongs to the relevant intrinsic organization, the unfolded net fails ICCR although it passes every boundary test; whether that component is consciousness-relevant, Kanai and Ma leave open (§4.7)."

### M7 — l.74 (and the same claim at l.78)
> "In an embodied agent the body is the highest-mutual-information, most-persistent, and most-controllable regularity in the sensory stream, so any world-model that forms attractors at all is driven to carve a stable basin for the agent's own body. The self-attractor thus falls out of embodiment…"

**Over-claim:** this untested hypothesis is stated as a necessity. In crucible the self/world differentiation is hardcoded: "construction, not emergence" (CRU-226 §4 item 3). Companion §2 l.85 says each structural prior "stipulates what development would otherwise have to discover". The closest support is companion §5.3 (self-inclusion selected by wiring cost), which is an optimality result on a numpy substrate.
**Replace (l.74):** "In an embodied agent the body is plausibly the highest-mutual-information, most-persistent and most-controllable regularity in the sensory stream, so we expect a world-model that forms attractors to carve a stable basin for the agent's own body. This is a hypothesis: in the model systems built so far the self/world split was built in, and a wiring-cost argument makes self-inclusion cheapest without showing it forms unaided (Gruber, 2026b, §5.3)." **(l.78):** "…so a world-model that carves attractors is expected to carve a basin for 'the body/self.'"

### M8 — l.174
> "…recurrence is *necessary* on this account but not sufficient — a merely recurrent system need not exhibit the closure pattern (i)$\wedge$(ii), which is the specific structure the detector adds."

**Over-claims what (i)∧(ii) adds.** Companion §5.1/§7 (l.169–177, l.236): on the model connectome "closure … is what recurrence already gives you, cheap to move and prohibitive to remove". Mutual dependence between coupled recurrent sub-partitions is therefore generic. A reviewer will press this.
**Replace:** "…recurrence is necessary on this account but not sufficient. Mutual dependence between two coupled recurrent sub-partitions is common; on the companion's model connectome, closure is what recurrence already gives (Gruber, 2026b, §5.1). Conditions (i)∧(ii) alone therefore discriminate little, and the discriminating content sits in the representational condition (iii) and the off-line sub-clause."

### M9 — l.176
> "…it therefore cannot predict a closure-*caused*, level-graded collapse of the self-circuit when the self-model's contribution to its own update is removed at matched recurrence."

**Over-claim:** the differentiating prediction is a capability-collapse prediction. The companion says such a prediction "cannot come out positive" and is "refutable by construction" (§8 l.244, §7 l.234).
**Replace:** "…it therefore makes no prediction about how much more a system without the self-model's contribution to its own update must pay, at matched recurrence, to reach the same world-modelling performance on an open-ended workload. FMT predicts that this cost gap exists and grows with the openness of the task."

### M10 — l.196, second forecast
> "…and that cutting the self-model's contribution to its own update should degrade world-modelling in proportion to the novelty of the workload."

**Over-claim:** this is the capability-loss form again; the companion's DV is cost at matched function (§8 l.244).
**Replace:** "…and that, at matched function, a system with the self-model's contribution to its own update cut should need more capacity or samples to reach the same world-modelling performance, with the gap growing with the novelty of the workload."

### M11 — l.160 (with l.80, Check 2 graded pass)
> "A null in that regime then counts as a disconfirmation of closure, not of workload adequacy…"

**Inconsistent with the published DV.** Check 2 scores excess $L_W$ at fixed capacity; the companion commits to cost at matched function (§8 l.244). The draft never relates the two, so the pre-registration commitment sits on a quantity the companion does not use. CRU-226 §4 item 3 records that route A came out closed ≈ capacity-matched open; that result is not quotable (CRU-222), but it is why this commitment needs the companion's framing.
**Replace (append to l.160):** "The companion states the decisive test as cost at matched function (Gruber, 2026b, §8). The excess-loss criterion here is its fixed-capacity reading, and a pass requires both readings to agree in sign. A null in that regime counts against closure, not against the adequacy of the workload."

---

## MINOR (wording, scope, citation hygiene)

| # | Line | Verbatim | Issue | Replacement |
|---|---|---|---|---|
| m1 | 20 | "…its realization relation, which we abbreviate ICCR" | ICCR is Kanai & Ma's own abbreviation (Def. 11). | "…its realization relation, ICCR" |
| m2 | 46 | "…but which structure that is requires a substantive theory ICF does not provide." | Softer form of M5. | "…and which structure that is, ICF leaves to theory-guided empirical search." |
| m3 | 52 | "First, Kanai and Ma hold that these openings do not weaken their *conditional* claims…" | Kanai says this only of the grain problem (§9.3: "our main results are not affected by the grain selection problem"). | "First, Kanai and Ma hold that the grain opening does not weaken their *conditional* claims…" |
| m4 | 64 | "…in rate reservoirs the computational optimum sits in the driven-stable, ordered regime (Gruber, 2026b)." | One task family; the companion's own scope is narrower. | "…in the rate reservoirs tested so far the accuracy optimum sat in the driven-stable, ordered regime (Gruber, 2026b, §4.4)." |
| m5 | 84 | "…uses the criticality signatures only as the best-validated readout for that property in a self-organizing physical medium." | The companion records that the subsampled branching ratio "has already failed as a stand-alone certificate" (§8 l.250). | "…uses the criticality signatures only as a corroborating readout for that property in self-organizing tissue, each reported beside a rate-matched surrogate." |
| m6 | 152 | "Prospective self-in-simulation yields a behavioural survival advantage over a matched reactive agent." | Companion: "small … a toy … an existence result, not a large effect" (§4.2). | "Prospective self-modelling gives a small survival advantage in a toy task (0.29–0.33 against 0.17–0.25; Gruber, 2026b, §4.2)." |
| m7 | 152 | "The dissociations below were run on toy rate- and spiking-network models in the companion" | The cited results are gridworld and rate-ESN models; none is spiking. | "…were run on toy gridworld and rate-reservoir models in the companion" |
| m8 | 154 | "Closure imposed on an *undifferentiated* substrate … yields no advantage, and the framework predicts exactly this" | The CRU-36 null is AT RISK (unbounded-membrane audit, CRU-226 §4 item 6). The companion gives a second reason (the task was not memory-limited, §6 l.224) that the draft drops. | Already folded into the B3 replacement; add "on a task the passive reservoir already solved". |
| m9 | 186 | "A companion treatment of consciousness in biological brains … abolish free modelling, and the substrate usually turns subcritical with it." | (a) The NoC slice is uncited and unpublished, so reviewers cannot check it. (b) The master says this of propofol only (`paper/full` / `noc` l.346); generalised with "usually", it reads as the reverse form criticality ⇒ free modelling that `prediction-framing.md` l.41 bans. | "A companion treatment of consciousness in biological brains (in preparation) tracks the same necessity in neural tissue, where free modelling often shows as near-critical dynamics; propofol, which abolishes free modelling, also turns the substrate subcritical." |
| m10 | 190 | "…the homeostatic self-regulating controller, which passes the *closed-loop* forms of all three checks…" | A homeostatic controller passing check 3 (open-ended computation deployed for self-modelling) contradicts §3/§4. | "…which can pass the closed-loop forms of checks 1 and 2…" |
| m11 | 170 | "…the detector supplies the tier-III structure ICF's own relation leaves unspecified." | Over-strong, and runs against S281 (see M2). | "…the detector proposes a candidate for the tier-III structure ICF's own relation leaves unspecified." |
| m12 | 210 | AI-use disclosure ("…prototyping of the analysis code used for the in-silico checks reported in the companion preprint…") | Not the S342 wording, which MG chose at D-S359-2 (`decisions.md` l.759, l.687: German origin, names "Claude (Anthropic)", reviewed-and-responsible clause). "In-silico checks reported in the companion" also repeats the B1 error. | Use the S342 text; say "analysis code for the in-silico experiments reported in the companion". MG must check the text before entry (S345 rule). |
| m13 | 222 | "Baltieri, M., & Kanai, R. (2026). Steam-engine naturalism. *Behavioral and Brain Sciences*, 49. doi:10.1017/S0140525X25103531." | **UNVERIFIED.** The citation ledger (`drafts/aiw130-verified-citations.md` l.11) and Kanai & Ma's own reference list give PsyArXiv 2025, doi 10.31234/osf.io/m4gk3. A BBS version may exist, but it was not verified here (offline). | Verify the BBS DOI live, or cite the PsyArXiv form from the ledger. |
| m14 | 286–302 | Figures 2 and 3 | Only Figure 1 is referenced in the body (l.72). Figures 2 and 3 have captions but no in-text callout. | Add "(Figure 2)" at l.58/l.62 and "(Figure 3)" at l.52 or l.170. |
| m15 | 164 | "…the system is terrifyingly competent and not a candidate." | Register: "terrifyingly" is editorialising. | "…the system may be highly competent and is not a candidate." |

---

## Kanai & Ma (2026b) citation check — local full text, all verified

| Draft line | Claim / quote | Kanai & Ma location | Status |
|---|---|---|---|
| 22, 46 | §9.2 tier-III target; "disciplined hypotheses about which interventions and readouts may help reveal" | §9.2 | quote ✓; paraphrase ✗ → M5/m2 |
| 22, 48 | §9.4 "should therefore not be presented as a rival measure of consciousness"; "a realization constraint"; "the next step"; "develop methods for extracting effective intrinsic structures from complex systems"; "IIT, for example, is more developed in this respect" | §9.4 | ✓ verbatim |
| 22, 50 | §9.3 "where the present framework is least settled"; "has no such maximization principle"; "could play that role" | §9.3 | ✓ verbatim |
| 30 | C1/C2 from Ma & Kanai (2026); universal theory, Kanai & Fujisawa (2024) | §1–2 | ✓ |
| 32 | Definition 9, five conditions, (5) = lumpability | §4.5 | ✓ |
| 34–36 | Definition 10 tuple $(S_P,\Omega,\mathcal A,\mathcal J,\Delta_P,\Lambda_P)$, $\Delta_P^{a,\omega}(\Pi_P(x))=\Pi_P(\Phi^{a,\omega}(x))$ | §4.6 | ✓ |
| 38 | lookup table / unfolded net / sustained clamp, Doerig et al. 2019; "unfolding argument loses its grip" | §4.7 | ✓; "Recurrent realizers pass" ✗ → M6 |
| 40 | computational mechanics, Shalizi & Crutchfield 2001 | §4.4 | ✓ |
| 42 | Definition 11; Theorem 1 with $F_Q$; "must identify a missing consciousness-relevant structure … and explain why that structure is required" | §5, §6, §8 | ✓ verbatim |
| 142 | §7.4 duplication/branching; extended mind (Clark & Chalmers 1998) | §7.4 | ✓ |
| 232 | Butlin et al. (2026) TiCS 30(6), 488–501 | Kanai reflist matches | ✓ |
| 222 | Baltieri & Kanai (2026) BBS | Kanai reflist has PsyArXiv 2025 | UNVERIFIED → m13 |

## Clean sections

- **§1** apart from l.24 (M2).
- **§2** apart from l.22/38/46/52 (M5, M6, m2, m3). The formal content (Defs 9–11, theorem, burden quote) matches the source.
- **§3** is clean on every theory ruling:
  - "four is not four modules … 2×2 taxonomy of computational kinds" (l.60);
  - free modelling necessary, not sufficient, with criticality "its usual signature in cortex and … neither" (l.64), matching S329 and the registry;
  - the sufficient conjunction (l.68) matches master §3.7.3 verbatim in substance.
  - Only m4 at l.64.
- **§4** checks 1–3 and Box 1 are clean as specifications, except l.74/78 (M7), l.84 (m5) and l.124 (B5). The criticality guardrail (l.84–86) is fully consistent with S329.
- **§5 (grain)** is clean: hedged, "candidate answer", the shared intractability with Φ admitted.
- **§6(a)** design paragraph: clean except B6. **§6(c)** worked example: clean except m15. The near-unity window there is paired with a rate-matched surrogate and is hypothetical, so it is allowed.
- **§7**: IIT, GWT/indicator and substrate paragraphs are clean. The issues are at l.170 (m11), l.174 (M8) and l.176 (M9).
- **§8**:
  - "Scope" (l.184), "dual threshold" (l.188) and "Falsification" (l.194) are clean.
  - Hard problem (l.192): "transforms rather than solves" complies with PHENOMENAL-7 / D-S359-7 (never "dissolves").
  - Issues are at l.186 (m9), l.190 (m10) and l.196 (B9, M10).

## Manuscript facts

- **Word count:**
  - 11,281 words total (`wc -w`);
  - 9,873 in §§1–9;
  - abstract 149 (JAIC limit 150);
  - 6 keywords (JAIC limit 6);
  - 34 reference entries.
- **Figures:** three are referenced as files: `figures/aiw130/jaic-fig1.pdf`, `jaic-fig2.pdf` and `jaic-fig3.pdf` (all present, with svg/png). Only Figure 1 is cited in the body (m14). JAIC wants EPS at ≥300 dpi; there is no EPS yet.
- **Anonymisation:** the draft is **not** anonymised: author name, ORCID and email are on l.3–4, and the AI disclosure plus self-citations carry DOIs. **That is correct for JAIC:** the review is single-blind and "do NOT anonymize" (`paper/jaic/journal-guidelines-jaic.md` l.6, l.13). S345 D8 ("preprint DOI … never in the anonymised manuscript") applies only to double-blind venues. The byline is sole-author, consistent with Frey out (S302) and Sousouri dropped (S356).
- **Other, not counted:**
  - `decisions.md` l.371 (S277) records the JAIC title as "…a Self-Model That Takes Itself for Its Bearer", while the draft uses "An Operational Detector for Machine Consciousness: …". The NoC lane now carries that subtitle, so S277 is probably superseded; confirm with MG.
  - Root cause for B3/B9: `.claude/knowledge/prediction-framing.md` l.70 still lists "(1) maintain a model recursion-specifically" (A#1, now WITHDRAWN) among the banked positives. Its l.74 interaction line is easy to misread as a result. That file needs its own update.
