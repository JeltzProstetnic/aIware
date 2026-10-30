# Mallavarapu & Percy (2026) — "A No-Go Theorem for Process Theories of Consciousness" — reading notes

Read in full 2026-10-23 (all 20 pages of the OSF PDF, file `6a7a167e703583e36412d3e8`, "Preprint V1.pdf", 468,445 B, fetched via `https://osf.io/download/6a7a167e703583e36412d3e8/` and extracted with PyMuPDF).

## Bibliographic facts (verified)

- **Authors:** Aneil Mallavarapu (Independent Researcher, Austin, Texas; corresponding) and Chris Percy ("Fundamental Consciousness Lead, The Consciousness Foundation", ORCID 0000-0003-0574-9160). Percy funded in part by the Langer Consortium. Contributions: Mallavarapu conceived the argument and led the formalization; Percy co-formalized and wrote.
- **Title:** "A No-Go Theorem for Process Theories of Consciousness". PsyArXiv, version 1, posted 2026-08-10 (OSF API `date_published`). It is the only version and is flagged `is_latest_version`. CC-BY 4.0.
- **DOI:** 10.31234/osf.io/w3n6v_v1. Resolves (302 → osf.io/w3n6v_v1) and is registered in Crossref as "posted 2026-08-10". OpenAlex W7202139329 lists `cited_by_count = 0`.
- **Talk version:** "Mind as structured matter: a no-go theorem for process theories of consciousness", Aneil Mallavarapu, TSC 2026, concurrent session, Monday 12 Oct, 6:40–7:05 pm (tsc2026.org/concurrent.html, verified).

## (a) The theorem

**Setup (§4.1–4.3, pp. 5–7).** S is "a bounded physical system to which a theory assigns consciousness". X_t = ρ_t^R(Γ_t) is the "complete local physical state", a spatial restriction of the global state that "retains the complete micro-state … and discards only degrees of freedom outside it", so it acquires no memory kernel (p. 5). I is the boundary input. A consciousness attribution has the form C_t = f(X_≤t), rewritten as C_t = f(X_t, X_<t) (eq. 14). A **state-based** attribution is C_t = f(X_t) (eq. 15). "Attributed to present state" means eq. 15.

**What counts as a process theory.** Introduction (p. 2): theories holding that "undergoing a diachronic process, such as recurrence, predictive updating, or sensorimotor interaction, is required for or constitutive of consciousness". Formally (§4.4): a theory that is "irreducibly history-dependent".

**Premises.**
- **P1, irreducible history-dependence:** (i) X_t^α = X_t^β ∧ (ii) I^α = I^β ∧ (iii) f(X_t^α, X_<t^α) ≠ f(X_t^β, X_<t^β).
- **P2, local state sufficiency:** X_t^α = X_t^β ∧ I_>t^α = I_>t^β ⇒ X_>t^α = X_>t^β. They describe it as approximating "the principle of experimental replicability" (p. 7).
- **P3, causal efficacy:** C_t^α ≠ C_t^β ⇒ X_>t^α ≠ X_>t^β (p. 8).

**Theorem (T):** ¬∃α,β [P1 ∧ P2 ∧ P3]. **Proof (§4.8)** by contradiction: P1 together with P2 gives X_>t^α = X_>t^β (18), while P1(iii) together with P3 gives ≠ (19). Hence ¬P1 given P2 ∧ P3. **Corollary (§4.9):** "The history argument in the general attribution function (14) is therefore eliminable", so C_t = f(X_t).

**Extensions.** A stochastic version (§4.10) states P2 as the Markov condition Pr(X_t+Δ | X_≤t, I) = Pr(X_t+Δ | X_t, I). A realizability version (§4.11) says the paired states need only be possible in principle. The premises can also be restated over a coarse-grained state g(X_t) with its own evolution law, which lets "digital computers satisfy this condition at the logical level by design" (p. 10). The illustrative case (§3) is a gear computer with a sufficient 1000-step algorithm: β is assembled directly into α's final state.

**Caveat they state themselves (p. 2):** the theorem "does not assume that consciousness itself is instantaneous or deny that experience may be temporally extended".

## (b) Theories hit, theories that escape, escape routes

**Named as process theories (p. 1):** recurrent processing (Lamme 2010, 2018), sensorimotor (O'Regan & Noë 2001), higher-order (Lau & Rosenthal 2011), active-inference and diachronic accounts (Kirchhoff & Kiverstein 2020; Deane 2021; Whyte & Smith 2021), GWT language agents (Goldstein & Kirk-Giannini 2026), and AI indicators (Butlin et al. 2026). Computational theories are discussed in §5.3: LIDA/GWT (Baars & Franklin 2009), Chalmers 2011 and 2023, and the Conscious Turing Machine (Blum & Blum 2022).

**Not targeted:** "biological system accounts", meaning neural correlates and causal generators such as neurobiological GWT ignition (p. 2).

**Causal-structure theories, IIT included (§5.2):** these escape only if the structure is "unique and physically grounded" in X_t. If the structure is "an actually occurring sequence — such as broadcasting, recurrent propagation, or feedback returning to its source", it "depends on X_<t, and therefore is subject to the theorem". They argue that IIT's grain and boundary choices are not yet shown to be fixed by X_t.

**Escape routes considered (Discussion, p. 11):**
1. Deny P2. This would require new physics that explains "how the historical information is carried".
2. Deny P3, accepting epiphenomenalism, which leaves the theory "observationally indistinguishable".
3. Accept the corollary: "history matters only through the present physical state it produces". X_t may contain "traces of memories, persistent activation, synaptic modifications".

**Favoured outcome (§5.4):** direct physical-state theories, namely EM-field theories (John, Pockett, McFadden, Gómez-Emilsson & Percy) and present-state quantum proposals.

**Challenge to computationalism (§5.3):** they demand "an observer-independent present physical invariant shared across" silicon, tubes and gears.

## (c) MY ASSESSMENT — FMT

**Is FMT hit as defined?** Only on a strict "constituted by the loop having run over [t−w, t]" reading. On that reading β, assembled mid-loop, would lack experience for the first w ms. That reading satisfies P1 and is hit.

FMT does not need that reading. All of its constituents are present-state variables in X_t:
- implicit models in synaptic weights;
- explicit models in current activation;
- the "closed loop" in in-flight recurrent signals, membrane potentials and the self-model currently representing itself.

The authors themselves count "persistent activation" as part of X_t. "The loop is closed now" is then a present-state fact in the same way that momentum is: X_t together with the evolution law M fixes it. So FMT can **reject P1 and accept the corollary at low cost**. Process language becomes an account of how the state is produced and maintained, which the authors explicitly allow (p. 11). The cost is to restate the criterion as C_t = f(g(X_t)), where g is a functional coarse-graining, and to stop calling consciousness "the running" in any sense the present state cannot settle.

**Temporal echo.** This is FMT's strongest asset here. If the experienced "now" is constructed content, then the felt duration and recency are what X_t represents, not a real past interval that must actually have elapsed. β at t would have exactly α's experience, including an apparent past that never happened, like a constructed memory. That is state-based (f(X_t)), so FMT **escapes**. It also handles the specious-present worry the authors raise through Zhou (2023) on p. 1. FMT should not concede that the window w is constitutive. It should say the window is the processing latency that produces the present content.

**Real residual cost.** It does not come from P1–P3. It comes from §5.3's extra demand for an observer-independent physical invariant across substrates. That demand is not derived from the theorem: §4.11 accepts coarse-grained states with their own evolution law. FMT's substrate neutrality (Class 4 computation) therefore faces the implementation problem (Chalmers 1996), not the no-go theorem. A reply would point out that the theorem licenses f(g(X_t)) and that the further invariance demand is an independent premise. FMT is still left owing a grounding of g that is not observer-relative.

**Minor weakness in their premises.** P3 is stated as "attribution differs ⇒ futures differ". A process theorist could hold that consciousness is causally efficacious through its realizer, with only the counterfactual β case staying inert. P3 as stated rules this out by definition, so the "epiphenomenal" horn is partly built into the formalization.

## (d) Responses and citations

As of 2026-10-23 there are none. OpenAlex shows `cited_by_count` 0, and a web search found only the preprint and the TSC 2026 talk.

## Citations used here (verification)

- Mallavarapu & Percy 2026: verified via OSF API, Crossref and the PDF.
- Zhou 2023, JCS 30(3):155–180; Chalmers 1996, Synthese 108(3):309–333, doi:10.1007/BF00413692; Maudlin 1989, J Phil 86(8):407–432: taken from the preprint's reference list. **UNVERIFIED independently.**
