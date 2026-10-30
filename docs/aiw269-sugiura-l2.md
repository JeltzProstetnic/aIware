# AIW-269 — Sugiura et al. (2025) vs Lemma L2 item (v)

Source read in full: Sugiura, Ariizumi, Asai, Azuma (2025), *Necessary and Sufficient Reservoir
Condition for Universal Reservoir Computing*, Mathematics 13(21) 3440, doi 10.3390/math13213440,
13 pp., CC BY. `www.mdpi.com` returns 403 (Akamai "Access Denied") to curl and to headless Chromium;
the PDF is reachable on MDPI's CDN:
`https://mdpi-res.com/d_attachment/mathematics/mathematics-13-03440/article_deploy/mathematics-13-03440.pdf`
(HTTP 200, 484,573 bytes, text extracted with PyMuPDF on 2026-09-28).

Roadmap passage checked: `paper/fmt_formal/fmt-formalization.md` line 309, Lemma L2 item (v).

## Setting of the paper (what the theorems are about)

- Continuous-time reservoir treated as a functional `f : V_res → R^m` from finite-length input
  functions (Lipschitz-bounded by K, values in compact convex A) to the state at time 0, started from a
  **fixed** initial state `x_init` at time −t (§2, Eq. 4). There is no echo-state / initial-condition
  independence assumption; the fixed start side-steps it.
- Readout: polynomial `p ∈ P_m`. Targets: uniformly continuous functionals. Error: uniform (sup).
  Universality = Definition 1, Eq. (5).
- Metric on inputs (Eq. 8): a fading-weight sup norm on the common domain plus `|θ(t1) − θ(t2)|` for
  the lengths. `V_res ∪ V` is compact under it (Proposition 1).
- Deterministic and noiseless only (§1: "we focus on the deterministic and noiseless case").

## (1) The property "only achieved or approached by chaotic reservoirs"

It is **Theorem 3 (§4, "Pathological Property of Universal Reservoir")**:

> "Theorem 3. Let F* be the set of uniformly continuous functionals from V_res to R. Let f : V_res → R^m
> be a functional that is bounded and universal for uniform approximations in F*. Then, the set of
> points v ∈ V_res at which f is discontinuous is dense in V_res."

Gloss (§4): "Theorem 3 says that a universal reservoir has a discontinuous point on an arbitrary
neighborhood of an arbitrary point and is very sensitive to input change."

It follows from **Theorem 1 (§3)** — universality (Eq. 5) ⇔ NSP (Condition 1) ⇔ uniformly continuous
left inverse (Condition 2), for bounded f — proved as a corollary of the general **Theorem 2** on any
compactifiable metric input space. Proof of Theorem 3: if f were continuous on some neighbourhood
N_δ(v), f with its continuous inverse would embed that neighbourhood in R^m; **Lemma 2** embeds
[0,1]^{m+1} into every N_δ(v); small inductive dimension then gives m+1 ≤ m (Eq. 31), a contradiction.
§1 states the same thing informally: "if there is a continuous and universal reservoir, it is a
homeomorphism. However, the infinite-dimensional space of input functions and the finite-dimensional
space of output values cannot be homeomorphic."

So the "pathological property" is **dense discontinuity of the input→state map**, equivalently
"infinite resolution" (§5: "The NSP can be seen as an infinite resolution that distinguishes two input
functions, regardless of how similar they are.").

## (2) What "chaotic" means in the paper

It is **never defined**. No Lyapunov exponent, no autonomous-vs-driven distinction, no echo-state
property, no edge-of-chaos or criticality language appears anywhere in the text. The link to chaos is
an interpretive remark, supported only by citations [19, 22–24] (chaotic spin-wave, chaotic circuit,
quenched chaos, chaotic neural-network reservoirs):

- §1: "This result suggests that a universal reservoir is highly sensitive to inputs, and chaotic
  reservoirs, such as those described in [19,22–24], are necessary to achieve universality."
- §5: "The behavior of a universal reservoir, as shown in this study, indicates that chaotic systems are
  necessary to achieve or approach universality. The difference between two inputs remains in a
  state-space system as the difference between states. Hence, a system sensitive to inputs is also
  sensitive to the initial state. As we showed, a universal reservoir has dense discontinuous points and
  is very sensitive to inputs. Therefore, the universality can be related to chaotic systems."

Reading: "chaotic" = sensitivity of the **driven** input→state map to its input, which the authors
transfer by analogy to sensitivity to initial state. It is a heuristic, not a theorem. On ESP status:
the framework fixes x_init, so the ESP is not addressed; their earlier paper (ref [20], IEEE TNNLS 2023)
is titled "Nonessentiality of Reservoir's Fading Memory for Universality". My inference, not stated by
them: fading memory is continuity in exactly the weighted-sup metric of Eq. (8), so a universal
reservoir in this sense violates fading memory on a dense set of inputs.

A further inference of mine (standard ODE theory, not in the paper): a finite-dimensional state-space
reservoir with Lipschitz ϕ and fixed x_init depends continuously on its input over any finite horizon,
so it has no discontinuities at finite-length inputs and **cannot** meet Theorem 3. Positive-Lyapunov
chaos makes the sensitivity grow like e^{λt} without ever becoming a discontinuity at finite t. That is
why the abstract hedges "achieved **or approached**": real chaotic systems approach the ideal, none
reaches it. The authors note that "the discontinuity of f … does not mean the discontinuity of the time
derivative ϕ", but they do not show how a well-posed system produces it.

Their own verdict on attainability (§5): "Our results indicate that universality, discussed since [3],
is an ideal approximation ability difficult to achieve in practice." And their proposed practical route:
"We can also consider reservoirs with finite resolution, and it may be possible to guarantee
approximation abilities for them according to their resolution. Such reservoirs behave more gently and
are easier to implement than those with the NSP."

## (3) Bearing on L2 and on the current roadmap sentence

**Current sentence is accurate** as far as it goes: NSP ⇔ universal approximation with polynomial readouts
(Theorem 1), for bounded continuous-time reservoirs, uniformly continuous targets, uniform error. Two
caveats:

- It omits the paper's main consequence (Theorem 3). A reader of L2 would infer NSP is a benign
  condition compatible with a stable, fading-memory reservoir. The paper says the opposite.
- Minor: Sugiura et al. already state that Theorem 2 covers any compactifiable input space, "Hence, our
  result may be applied to various types of RC not discussed in this paper, such as discrete-time ones"
  (§1). "Roig et al. extend the result to driven discrete-time reservoirs" is still fine if Roig give an
  explicit proof, but the extension is anticipated in Sugiura. (Roig et al. not re-read here.)

**Effect on the edge-of-stability conjecture: refines it, and points away from λ_max ≈ 0 for the exact
notion.**

- Exact approximation universality requires unbounded input sensitivity (dense discontinuity). That lies
  beyond the chaotic side of the edge, and beyond anything a well-posed finite-dimensional system does.
  It gives no support for "universality forces λ_max = 0"; if anything it says the exact limit is not a
  marginal regime at all.
- Nothing in the paper separates autonomous chaos from driven stability, so it neither supports nor
  refutes "chaotic when undriven, marginally stable under drive". Its object is the driven map only, and
  it asks that map to be maximally sensitive, which is the opposite of driven stability.
- The two results fit together if one separates the ideal from the finite-resolution case. Sugiura's
  theorem is about infinite resolution in a noiseless setting; Roig et al.'s marginal-driven-stability
  optimum is numerical, with linear readouts and finite resolution (and, typically, noise). A peak at the
  edge is plausible as the trade-off between resolution (wants sensitivity) and noise robustness/memory
  (wants contraction) once resolution is finite. That trade-off is not proven by either paper.
- It adds weight to L2's own conclusion that "No theorem yet forces the maximal Lyapunov exponent to
  zero": the one exact characterisation available drives the optimum to the pathological end, and any
  edge-of-stability result will have to come from a finite-resolution or noisy formulation.

## (4) Proposed addition to L2 item (v) — one sentence

Insert after the Roig, Muñoz, and Morales (2026) sentence, before the Du and Wang sentence:

> Sugiura et al. also prove that such a reservoir is discontinuous on a dense set of inputs (their
> Theorem 3), which they read as requiring chaotic dynamics; exact approximation universality thus lies
> beyond the edge of stability, and the marginal window found by Roig et al. belongs to the
> finite-resolution regime that Sugiura et al. describe as easier to implement.

Reason for adding rather than leaving it: the existing sentence cites Sugiura only for the equivalence,
and a reader would take NSP as compatible with a stable reservoir. Theorem 3 is the paper's headline and
it bears directly on L2's direction. The sentence reports their theorem, attributes the chaos reading to
them, and keeps the reconciliation with Roig to what both papers state (ideal vs finite resolution). The
Lipschitz/fading-memory inferences above are mine and are kept out of the roadmap.

Register check: no not-X-but-Y construction, no self-narration, no throat-clearing, no banned words.
The "thus" claim ("lies beyond the edge of stability") is the one interpretive step; if MG wants the
roadmap to state only what the source states, drop that clause and keep "…which they read as requiring
chaotic dynamics."
