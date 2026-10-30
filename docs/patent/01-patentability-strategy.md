# Patentability & Filing Strategy — FMT and the Crucible Spiking Substrate

**Preparatory analysis for briefing a patent attorney. Not legal advice.** Neither the author of
this document nor any assistant in this project is a lawyer or patent attorney. Every conclusion
below is a working assessment to make the first attorney meeting cheap and productive; the attorney
decides. Items marked **[verify]** are specific points counsel must confirm before reliance.

Prepared 2026-08-11 for Matthias Gruber (MG). Stated goal, verbatim: *"start planning and drafting
patent(s) protecting our spiking brain once we have one. The idea would be to block as many and much
AC attempts within the definition capacity of FMT, which imo would block ALL ac."*

---

## 0. Executive Summary

1. **Self-disclosure (§1): Europe is closed for everything published; the US has salvage windows
   with hard dates.** The EPC has absolute novelty and no grace period. The 2015 monograph, the
   Zenodo master paper (v1 ≈ mid-Feb 2026 → v13 Jul 2026), the computational companion (~Jul 2026),
   the public wiki, the trade books, **and the public GitHub mirror of the working paper (current to
   Aug 2026, §8.9 with all eight banked in-silico results)** are all prior art against any future EP
   filing. What survives, everywhere, is the **crucible engineering layer that has never left the
   private repo**: the concrete spiking substrate, the local three-factor training rule, the
   emergence protocol, the decompilation pipeline, the embodiment/LLM-coupling designs. In the US, a
   §102(b)(1) grace window additionally keeps the *recently* published mechanism results filable
   until roughly **mid-2027** (per-disclosure dates in §1.3).

2. **Employer (§4): real, non-fatal, and currently being made worse by one specific practice.**
   The invention-provenance facts are strong (theory 2003/2015, a decade before the AI Officer role;
   published as "Independent Researcher"; work on private home hardware). The job title "AI Officer /
   R&D AI Transformation Manager" is the single worst fact. The governing law is probably
   **Liechtenstein (Swiss OR 332 mirror), not Austrian PatG §§6–17** — place of work Schaan —
   and under both regimes the case for a *free invention* is good **provided no employer resources
   were used**. That proviso has a live hole: the personal agent fleet runs on the Ivoclar office
   workstation and the Ivoclar corporate notebook. **If aIware/crucible sessions ever ran on those
   machines, that is documentary evidence for the "employer resources" prong.** Audit and cease
   (§4.5). Have counsel read the employment contract before anything else and before any
   communication with Ivoclar.

3. **Blocking all AC (§3): not achievable, for five independent reasons — but the goal is partially
   achieved already, by a different mechanism.** Definitional-level claims die on (i) MG's own prior
   art, (ii) subject-matter eligibility, (iii) enablement/written description, (iv) dense third-party
   art, (v) a design-around that FMT's own published No-Free-Lunch passage hands to every reader.
   However: **those same publications are prior art against everyone else too.** Nobody — not
   OpenAI, not DeepMind — can now patent the four-model / closure / criticality architecture at the
   definitional level. The "nobody owns AC at FMT's level" half of the ambition is done, permanently
   (prior art never expires; patents do). The achievable *exclusive* asset is a **toll-booth on the
   efficient implementations**: 2–3 narrow, real families on the crucible mechanisms (§5).

4. **Eligibility (§2):** claims survive as apparatus/system, training-method, robot-control, and
   neuromorphic-hardware claims framed on measurable technical effects (synapse/energy cost, sample
   efficiency in a control task, on-chip learnability). Claims framed on "consciousness," on the
   theory as such, or as unanchored simulations die at both offices.

5. **Immediate deadline: file the priority application before MoC7 (Copenhagen, Oct 12–16, 2026)**
   and before any OSF preregistration, v15 Zenodo upload, poster, or Show-HN code release. Every one
   of those is a fresh, EP-fatal disclosure of whatever it contains.

---

## 1. The Self-Disclosure Problem

### 1.1 Europe: Art. 54 EPC — absolute novelty, no rescue

Art. 54(2) EPC: the state of the art comprises **everything made available to the public** by written
or oral description, by use, or in any other way, **before the filing date**, anywhere, by anyone —
including the inventor. There is no inventor grace period. A Zenodo preprint, a public GitHub push, a
personal wiki page, a self-published book, a conference poster, and an OSF preregistration are all
full prior art against the discloser's own later EP application.

The Art. 55 exceptions are two, both narrow, both 6-month, and neither applies:

- **Art. 55(1)(a) — evident abuse** in relation to the applicant: covers a third party publishing
  *stolen or breached* information (e.g., an NDA partner leaking). Voluntary self-publication is the
  opposite of abuse. Not applicable.
- **Art. 55(1)(b) — display at an officially recognised international exhibition** under the 1928
  Convention: a tiny closed list of world-expo-class events. Zenodo, GitHub, MoC7 and academic
  conferences generally do not qualify. Not applicable.

Additionally, per G3/98 and G2/99 the 6-month Art. 55 window is computed from the **filing date, not
the priority date** — even the theoretical rescue is tighter than people assume. Conclusion: **in
Europe, everything already published is unpatentable, full stop.** The only EP-relevant question is
what has *not* been published (§1.4).

*(Secondary note: Germany and Austria offer utility models — Gebrauchsmuster — with a genuine
6-month grace period for the applicant's own disclosures. German GM: apparatus only, no method
claims. Austrian GM: 6-month grace, 10-year term, and — unusually — explicit protectability of
**Programmlogik** (program logic) under §1 GMG. **[verify both]** This is a salvage instrument for
subject matter disclosed after ~mid-February 2026 (i.e., within 6 months of a filing made now), and
because MG is Austrian, the Austrian GM is a cheap, fast, unexamined national layer worth asking
counsel about — as a supplement, never a substitute.)*

### 1.2 United States: 35 U.S.C. §102(b)(1) — the one-year inventor grace

Under §102(b)(1)(A), a disclosure made **one year or less** before the effective filing date is not
prior art if made by the inventor (or by someone who obtained it from the inventor). §102(b)(1)(B)
additionally shields against third-party disclosures of the same subject matter after the inventor's
own first disclosure. Consequences:

- Anything MG published **more than 12 months before filing** is prior art against him even in the
  US. The 2015 monograph is long gone. The Zenodo master v1 (~Feb 2026) content becomes prior art
  against a US filing from **~mid-February 2027**.
- Anything published **within the last 12 months** — the companion computational paper (~Jul 2026),
  Zenodo v13 (Jul 2026), and the §8.9 results pushed to the public GitHub mirror (Jul–Aug 2026) —
  is still US-filable, with per-item expiry dates in the table below.
- **Practical caution counsel will repeat:** relying on the grace period is a last resort, not a
  strategy. It buys the US (and a handful of grace jurisdictions: Canada 12 mo, Australia 12 mo,
  Japan 12 mo, Korea 12 mo, Brazil 12 mo **[verify current terms]**) and nothing else, and the
  §102(b)(1)(B) shield against intervening third-party art has sharp edges (the intervening
  disclosure must be the "same subject matter").

### 1.3 Disclosure inventory — what specifically kills what

Exact Zenodo per-version timestamps must be pulled from the records for the attorney's chronology
annex; dates below are reconstructed from the project logs. **[verify all dates against the Zenodo
records and the public git history — the attorney needs a complete, timestamped disclosure
chronology as Annex A]**

| # | Disclosure | Date | What it discloses | Claims it destroys (EP: outright; US: after grace expiry) | US grace runs out ≈ |
|---|---|---|---|---|---|
| D1 | *Die Emergenz des Bewusstseins*, 2015 monograph (ISBN 978-1-326-65207-4) | 2015 | Four-model architecture; self-model embedded in world-model (p. 61 — the 2015-vocabulary form of O_ESM ⊆ S_EWM); self/world boundary via direct-vs-indirect feedback; qualia as virtual | Any claim to the conceptual architecture: "a system comprising world-model and self-model at implicit and explicit levels, the self-model embedded in the world-model." Dead **everywhere including the US** (>1 yr). | expired |
| D2 | FMT master paper, Zenodo concept DOI 10.5281/zenodo.18669891, v1 | ~Feb 2026 | Full modern theory: 2×2 model kinds, self-referential closure criterion, criticality/Class-4 regime condition, substrate independence, "engineering specification for artificial consciousness: implement the four-model architecture on a substrate operating at criticality" | Every architecture-level and criterion-level claim; every "AC = four models + criticality" claim; the operational measures (PCI etc.) as consciousness tests | ~Feb 2027 |
| D3 | Zenodo versions v2–v13 (v13 = version DOI 10.5281/zenodo.21611849) | Feb–Jul 2026 | Progressive refinements: temporal-echo mechanism, ablation-control self-recognition criterion (§3.4.3), Table 1/1b empirical handles, redeployment framing | Test-method claims on the ablation-control self-report protocol; permeability/criticality measurement claims | Jul 2027 (v13 additions) |
| D4 | Companion computational paper, Zenodo 10.5281/zenodo.21610993 (*Closure and Criticality as Enabling Conditions for World-Modelling*) | ~Jul 2026 | The in-silico program: criticality-band capability results, closure results, two-closure taxonomy, capability-first reading | Method-of-use claims on the tested mechanisms at concept level; "operate an SNN at the edge of chaos to obtain modelling capability" | ~Jul 2027 |
| D5 | **Public GitHub mirror** (github.com/JeltzProstetnic/aIware — origin excludes only tmp/, drafts/, scripts/, docs/, .claude; **paper/ is public and current**) | continuous; §8.9 full text public since ~Aug 8, 2026 | Working master v14+ **including §8.9's eight banked results in quantitative detail**: closure-removal cost (14.0%/12.0% vs 74.0%/71.5%, 5.3–6.0×); conditional value of the return (R² −0.001→0.640 etc.); the **72-architecture bottleneck argmin with all four selection conditions** — low-dimensional content, spanning subsystems, near-ceiling delivery, **read-back over a short return** — and the "self-inclusion falls out of wiring cost" derivation; the spiking maintenance result; the No-Free-Lunch unroll passage | EP novelty/inventive step for: the bottleneck-self-model **design rule**; closure-cost-based architecture selection; "short-return re-entrant low-rank bottleneck spanning world+body regions" claimed at the level of the published prose. (The *specific enabling implementation* is not in the prose — see §1.4 — so narrower claims survive.) | ~Aug 2027 |
| D6 | fmt.matthiasgruber.com wiki | 2026, ongoing | Theory-level content, continuously updated | Same bucket as D2/D3 | rolling |
| D7 | Trade books (*The Simulation You Call "I"*, EN; *Die Simulation namens Ich*, DE) | 2026 | Popular articulation of the architecture, closure, criticality, AC implications | Reinforces D1/D2; nothing extra of claim relevance beyond them **[verify: whether the shipped editions carry the consolidation-channel material of pattern 14 — if yes, that mechanism is disclosed too]** | ~mid-2027 |
| D8 | Formalization papers (Zenodo 10.5281/zenodo.21843693; GitHub roadmaps) | 2026 | Formal definitions roadmap | Formalization-level claims | ~2027 |

**The blunt statement requested:** MG has published, openly and repeatedly, the exact definitional
layer he wants the patents to occupy. The closure criterion has been public since **2015**. The
"implement four models at criticality" engineering specification has been public since **early
2026**. The quantitative design rule for a self-including bottleneck architecture has been public
since **August 2026** — pushed to a public GitHub mirror as part of routine paper maintenance,
probably without anyone flagging that each push is a patent-law disclosure event. At the
definitional level there is nothing left to patent in Europe, and by ~mid-2027 nothing left in the
US either. **The blocking-patent-at-FMT-level plan was dead before it was conceived, mostly by MG's
own (entirely reasonable, priority-establishing) publication strategy.**

### 1.4 What is NOT yet published — the patentable surface

This is the valuable output. The crucible repo is private; its results docs, designs and code have
never been pushed to a public remote. The public paper describes *results and design principles* in
prose; it does not disclose the *enabling implementations*. Anticipation requires an enabling
disclosure; the gap between D5's prose and the crucible artifacts is where the claims live. Every
item below must be checked against the actual public git history before filing ("never left the
private repo" is an assumption to verify, not a fact in evidence). **[verify per item]**

**Cluster A — the substrate (apparatus family).**
- The concrete spiking implementation: ~22,000-neuron regional SNN; region taxonomy (engine /
  world-model / body-model / self-loop) with the hand-written inter-region connectivity table;
  heterogeneous membrane/synaptic time constants per region; homeostatic rate regulation;
  the "delivered drive" instrumentation (measuring the current a loop actually injects, replacing
  firing rate as the drive axis).
- The **non-foldable closure loop** designs: the fold algebra showed a naive closure arm is
  algebraically equivalent to an open arm (M = W + W_fb·W_out); the repair — a loop carrying its own
  *differential* time constant (a second filter state), delay, or nonlinearity so that closure is
  dynamically real rather than foldable — is an architecture feature that exists nowhere public.
  This is arguably the most patent-shaped single artifact in the project: a structural feature,
  discovered through failure analysis, that distinguishes a functioning re-entrant self-loop from
  one that is secretly feedforward.
- The modular substrate build (CRU-86) as implemented.

**Cluster B — training and emergence (method family).**
- The **local three-factor plasticity rule** that routes credit through a *learning* self-model
  region (CRU-83 Gate A: 92.4% of the hand-wired ceiling against a −0.003 floor, p = 0.0001) —
  local rules are exactly what neuromorphic hardware can run on-chip, which is both the technical
  effect for eligibility and the commercial hook.
- The **sufficiency/emergence protocol** (M1s3 / CRU-83 design): the staged training regime under
  which the loop *builds* the self-model rather than having it hand-wired; the multi-consumer
  structure; the pre-registered controls (delay-line, nonlinear-feedforward, detuned, scrambled,
  foreign-body arms) as method steps.
- The **self-model-survival controls**: the three-DV scheme distinguishing redeployment from
  relearning (task performance; fidelity retained on the pre-redeployment body; whether the learned
  frame approximates the target frame). Published nowhere; a natural dependent-claim set.

**Cluster C — measurement and readout (method/apparatus family).**
- The **decompilation pipeline** (CRU-72 / L7): locating explicit models inside a running spiking
  substrate and correlating self-model content to behavior — "robot psychology with every synapse
  visible." Early-stage; if filed now it needs prophetic-example drafting and carries enablement
  risk; if it waits for reduction to practice it must not be published first.
- The training-side **label-hygiene protocol** (never-supply-the-self-label) as a concrete
  contamination-control method for self-report evaluation. Note: the *evaluation criterion*
  (ablation-control label test) is already public in §3.4.3 (D3); only the training-side protocol
  machinery retains novelty. Low standalone value; useful dependent claims.

**Cluster D — embodiment and coupling (weakest, youngest).**
- The embodiment seam and staged body plan (B1 simple → B2 realistic virtual → B3 WAVEGO robot);
  the **non-biasing LLM coupling** (M3) design. Mostly at concept stage; enablement thin today.
  Either mature before filing or cover thinly as dependent material in the Cluster A/B application.

**Not patent material (keep for the papers):** the S298–S300 theory batch (two-tags/dream ordering,
quale-as-read-value, dreaming/maturing routes, free-will blind-spot) — new and unpublished, but
theory, and it will be published in v15 anyway. Its only patent relevance is negative: **it must not
carry any of Clusters A–D into v15 with it.**

### 1.5 Disclosure control from today

The project's default motion is *publish everything immediately* (Zenodo versioning, public mirror,
preregistration, "invite the world"). That is a good science strategy and a catastrophic patent
strategy; they can coexist only with a filing-before-disclosure discipline:

1. **Hard deadline: MoC7, Copenhagen, Oct 12–16, 2026.** The handout/poster and any preprint
   timed to it disclose whatever they contain. File the priority application before it.
2. **v15 of the master must not absorb crucible implementation detail** beyond what §8.9 already
   states, until the priority filing is in. The standing rule "all the evidence must reach the
   paper" (master lists, companion explains) is precisely the mechanism by which Clusters A–B would
   leak next.
3. **OSF preregistration of the public robot experiment is a publication.** The post-MoC7 arc
   (build video, OSF prereg, Show-HN SNN code) is three separate disclosure events. The Show-HN
   code release in particular would be a full enabling disclosure of Cluster A. All of it is fine —
   *after* the priority date.
4. **The public GitHub mirror needs a patent-awareness check in the push workflow**: before
   `filtered-push.sh` publishes paper changes, anything describing not-yet-filed implementation
   detail should be flagged. (D5 happened because nobody was watching this boundary.)
5. Journal submission (NoC, Dec 31) is confidential and not itself a disclosure **[verify journal
   policy]**, but the arXiv/Zenodo copy that habitually accompanies it is.

---

## 2. Subject-Matter Eligibility

### 2.1 EPO

**The exclusions.** Art. 52(2)(a)/(c) EPC excludes discoveries, scientific theories, mathematical
methods, and programs for computers "as such" (Art. 52(3)). FMT *as a theory of consciousness* is
excluded twice over (scientific theory; and, in formalized form, mathematical method). Any claim
whose substance is "the insight that consciousness = self-referential closure at criticality" is
unpatentable regardless of novelty.

**The escape, and its limits.** Under settled practice (T 258/03 *Hitachi* and the Comvik approach,
T 641/00), any claim reciting hardware passes Art. 52 — but for **inventive step only the features
contributing to technical character count**. A claim to "a computer configured to run the four-model
architecture" passes Art. 52 trivially and then dies under Art. 56 unless the *specific* features
produce a technical effect.

**Neural networks specifically.** EPO Guidelines G-II 3.3.1: machine-learning models are treated as
mathematical methods; they gain technical character either (i) by application to a technical purpose
(e.g., controlling a robot from sensor data, image processing on measurement data) or (ii) by
adaptation to a specific technical implementation — architecture choices motivated by the internal
functioning of the computer (memory, energy, parallelism). Both routes are open here and both should
be used in the same application:

- Route (i): the substrate **controls an embodied agent / robot** — sensorimotor loop, real sensor
  input, motor output. Frame the independent claims on the control system.
- Route (ii): the whole crucible economics program *is* a technical-implementation argument —
  synapse count as wiring cost, energy per delivered function, a local learning rule that avoids
  global gradient transport (on-chip learnability on neuromorphic hardware). These are exactly the
  "internal functioning" considerations the Guidelines reward. The published cost results (D5) can
  be cited as *advantages* in the description even though they are prior art as *disclosures* —
  what matters is that the claimed *implementation* is new.

**G 1/19 (2021) — directly on point, and it must be designed around, not just cited.** The Enlarged
Board held that computer-implemented simulations are assessed under Comvik like any other CII; a
simulation claimed *as such* — producing only numerical data about a modeled system — generally
cannot base a technical effect on that data's "potential" later technical use. Only effects that are
(a) within the computer (implementation-level) or (b) tied to an actual technical use (e.g., the
output directly controls a machine) count reliably. Application here:

- A claim to "simulating a self-model within a world-model" — the naked crucible experiment — is
  the *pedestrian-simulation fact pattern with a cognitive system in place of pedestrians*. The
  modeled system (an agent's self) is not a technical system in the EPO's sense, and the output
  (decodability scores, R² values) is numerical data. **This claim form dies under G 1/19.**
- The two safe harbors: claim the **trained control system in operation** (robot/agent control —
  direct link with physical reality), and claim the **training method by its implementation
  properties** (local rule, resource profile — effects within the computer). Keep a pure-simulation
  claim only as a fallback dependent claim, if at all.

**"Consciousness" as claimed effect: never.** It is not a technical effect; it is unverifiable and
would also draw clarity objections (Art. 84) and gift every opponent an insufficiency attack
(Art. 83). The claims must be written entirely in the vocabulary of measurable engineering
properties: sample efficiency at matched budget, synapse/energy cost at matched function, retained
model fidelity under redeployment, decodability of maintained content. The word "consciousness"
belongs in the background section at most.

### 2.2 United States

**§101 / Alice-Mayo.** A theory of consciousness is an abstract idea; a claim that amounts to
"apply the four-model definition on a computer" fails step two (generic implementation of an
abstract idea). The favorable line — Enfish (self-referential data structure as an improvement to
computer functionality — an almost poetic fit here), McRO, Bascom — protects claims directed to a
**specific asserted improvement in computer capabilities**. The adverse recent line matters more:
**Recentive Analytics v. Fox (Fed. Cir. 2025)** held that applying generic machine learning to a new
environment is abstract; eligibility requires a specific *improvement to the machine-learning
method itself*. That is survivable here precisely because the crucible assets *are*
architecture-and-training improvements (a specific loop structure that cannot be folded away; a
specific local rule; measured resource advantages), not "use ML for consciousness."

**§112(a) — the real ceiling on breadth.** *O'Reilly v. Morse* (claim 8: all use of
electromagnetism for printing at a distance — void) is the 170-year-old version of MG's goal, and
**Amgen v. Sanofi (2023)** is its modern restatement: a functional genus claim must be enabled
across its full scope, and "invent it yourself within my function" does not count. A claim covering
"any system that implements a self-model within a world-model with re-entrant closure" is a
functional claim at the point of novelty over an unbounded genus. It would be invalidated under
§112 even if it somehow survived §101 and §102. The same economics holds at the EPO via Art. 83
sufficiency and the plausibility line (G 2/21 adjacent). **This is the doctrinal reason the "block
all AC" claim cannot exist, independent of the prior-art reason.**

### 2.3 What survives, what dies

| Claim type | EP | US | Notes |
|---|---|---|---|
| System/apparatus: SNN with region taxonomy + non-foldable short-return low-rank self-loop, controlling an embodied agent | ✅ strong | ✅ strong | Lead independent claim. Tie to sensor/actuator or neuromorphic implementation. |
| Training method: local three-factor rule routing credit through a learning self-model; emergence protocol with control arms | ✅ good (implementation-level effects) | ✅ good (Recentive-proof: improves the ML method itself) | Second independent claim. |
| Method of operating: few-shot modeling of external agents by redeploying the trained self-model (robot control context) | ✅ good | ✅ good | Watch Bongard/Lipson art closely (§3). |
| Neuromorphic hardware embodiment (on-chip local rule, loop wiring) | ✅ strongest | ✅ strongest | Include a hardware section in the spec even if prophetic. |
| Computer-readable medium claims | ✅ (as CII) | ✅ | Routine adjuncts. |
| Readout/decompilation method (locating explicit models in a running substrate) | ◐ (data-analysis framing risk; anchor to a measurement purpose) | ◐ (abstract-idea risk; anchor to specific technical steps) | File when closer to practice, or as a dependent cluster. |
| Pure simulation claim (no physical link, no implementation-level effect) | ❌ G 1/19 | ◐ weak | Fallback dependent at most. |
| "A conscious machine" / "system implementing consciousness per FMT" | ❌❌ (52(2), 84, 83, own art) | ❌❌ (101, 112, own art) | Never draft. |
| Method of testing/certifying consciousness (ablation-control label test) | ❌ (published D3 + non-technical purpose) | ❌ (published + abstract) | Already given away. |

---

## 3. Can This Block "All AC"? — Honest Verdict

**No. Five independent mechanisms each suffice to kill the maximal version; all five apply.**

1. **Own prior art.** §1: the definitional layer has been public since 2015/2026. Any claim broad
   enough to cover "all serious AC attempts within FMT's definitions" reads on MG's own
   publications and is therefore invalid — anticipated by the very documents that establish his
   priority as a scientist.
2. **Eligibility.** §2: the definitional layer is a scientific theory (EPC) / abstract idea (US).
   The claim that survives eligibility is by construction narrower than the ambition.
3. **Enablement / written description.** Morse and Amgen (§2.2): a claim covering every future AC
   implementation is a functional genus claim that no specification can enable. The breadth that
   would make the patent blocking is exactly the breadth that makes it invalid.
4. **Third-party art.** The definitional space is independently crowded: Metzinger's self-model
   theory (2003); Friston's active inference / self-evidencing; Ha & Schmidhuber's *World Models*
   (2018); **Bongard, Zykov & Lipson, "Resilient machines through continuous self-modeling"
   (Science, 2006)** — a physical robot that builds and uses a self-model, uncomfortably close art
   for any "machine with a self-model" claim; Kwiatkowski & Lipson's task-agnostic self-modeling
   (2019); Graziano's attention-schema theory with Webb's implementations; Haikonen's machine-
   consciousness architectures; Thaler's sentience-flavored patents; Dreamer/MuZero world-model
   agents; the Intel/IBM/BrainChip neuromorphic patent estates. A serious FTO/novelty search (a
   deliverable to commission from counsel, ~€3–6k) will find more. Independent invention is no
   *defense* to infringement, true — but this art bounds what can be *claimed* in the first place.
5. **The published design-around.** FMT's own No-Free-Lunch passage — in the public paper, verbatim:
   *"a finite closed loop unrolled over a finite horizon is a feedforward network with memory, so no
   input-output capability is closed to a feedforward architecture"* — is an instruction manual for
   non-infringement. Any closure-loop claim can be avoided, at an efficiency cost, by the unrolled
   architecture the theory itself guarantees to exist. MG published the escape route.

Add the practical layer: patents run 20 years from filing (a 2026 family dies in 2046 — the AC
timeline may or may not fit); infringement inside a competitor's research lab is invisible and
effectively unenforceable; EU member states have experimental-use exemptions (e.g., Austrian PatG
§22 area **[verify scope]**), and while the US research exemption is nearly dead (*Madey v. Duke*),
suing academic consciousness researchers is reputational suicide for someone whose strategy is
"invite the world to see it."

**What the achievable, still-valuable outcome looks like:**

1. **The defensive wall is already built — recognize it as an asset.** Every disclosure in §1.3 is
   prior art against *everyone*. No lab or company can now obtain the FMT-definitional patent MG
   wanted for himself; the field-level freedom he wanted to control, he has instead *guaranteed for
   everyone, forever* (prior art does not expire). If part of the motive was "no one else may own
   AC," that part is complete. Continue it deliberately: publish theory-level material promptly and
   citably (Zenodo, timestamped) as **defensive publication**, precisely so no one else can fence
   the space.
2. **A toll-booth on the efficient path, not a wall across the field.** FMT's own economics says the
   unrolled design-around is *exponentially expensive in the regime that matters* — closure is the
   efficiency optimum in the fit window. So narrow claims on the **efficient mechanism family**
   (Clusters A–B: the non-foldable loop, the local rule, the emergence protocol) capture the
   commercially viable route even though the concept is free. If — a real *if* — the crucible
   mechanisms are the ones that scale, whoever industrializes AC-like architectures needs a license
   for the efficient implementation. That is the honest, defensible remainder of the blocking
   ambition: **you cannot own the idea; you may own the only affordable road for a while.**
3. **A continuation/divisional posture.** File one thick priority application; keep a US
   continuation and an EP divisional pending for years, so claims can be drafted *later* against
   implementations actually observed in the field (within the four corners of the original
   disclosure). This is the standard mechanism by which a narrow-looking family projects broad
   deterrence.
4. **Leverage beyond exclusion.** A modest granted portfolio: anchors licensing conversations,
   forces bigger players to engage rather than ignore, supports any future venture/spin-out
   valuation, and gives standing in the emerging AC-governance discourse. If the underlying motive
   is partly *ethical control* of AC, note that a patent is a weak instrument for it (20 years, few
   jurisdictions, detection problem) — field-of-use / ethics-conditioned licensing of the granted
   claims is the version of that goal a patent can actually carry.

---

## 4. The Employer Problem

### 4.1 Which law governs — probably not the Austrian Patentgesetz

MG is an Austrian resident (Vorarlberg) employed by **Ivoclar AG**, seat Schaan, **Liechtenstein**
(classic Rhine-valley cross-border commute). Employee-invention rights follow the law governing the
**employment contract**; under the Rome I logic (Art. 8: habitual place of work, absent a choice of
law) that is **Liechtenstein law**, unless the contract says otherwise or the employing entity is
actually an Austrian subsidiary. **[verify: the employing legal entity on the contract, and any
choice-of-law clause — this single document determines which analysis below applies]**

The Liechtenstein/Swiss angle noted in the brief: Liechtenstein and Switzerland form a unified
patent-protection territory (Patent Treaty of 1978, Swiss law applies to patents covering both);
more relevantly, Liechtenstein employment law (§1173a ABGB employment provisions) mirrors the Swiss
Code of Obligations, including the employee-invention rule of **OR Art. 332**. **[verify the
§1173a mirror provision]**

### 4.2 The Liechtenstein/Swiss test (OR 332 pattern)

Three categories:
- **Aufgabenerfindungen** — made in the course of work *and* in performance of contractual duties:
  belong to the employer by law, no compensation beyond salary.
- **Gelegenheitserfindungen** — made in the course of the employment activity but *not* in
  performance of duties: the employer may acquire them only if a **written reservation** exists in
  the contract, against special compensation, exercised within ~6 months of notification.
- **Free inventions** — made outside the employment activity: the employee's, entirely.

The crucible substrate is a free invention on these facts *if* three things hold: no work time, no
employer resources, no duty nexus. See §4.4–4.5.

### 4.3 The Austrian test (PatG §§ 6–17), in case Austrian law applies

Austrian law is employee-friendlier than most: under **§7(1)**, even a genuine *Diensterfindung*
belongs to the employee unless a **written agreement** (individual contract or collective
agreement) assigns it to the employer. **§7(2)** defines a Diensterfindung by two cumulative
elements: the invention (a) **falls within the field of activity of the enterprise**
(Geschäftszweig), and (b) at least one of: (i) the activity leading to it belonged to the
employee's duties, (ii) the impetus came from the employer, or (iii) the making was **substantially
facilitated** by the employer's resources or experience. §§8–17 add compensation, notification and
procedure. **[verify section numbering with counsel]**

Applied: Ivoclar's Geschäftszweig is dental materials, equipment and workflows. A spiking-neural
substrate for artificial consciousness is not in that field — prong (a) plausibly already fails,
which under Austrian law ends the employer's claim regardless of the title. The counterargument a
company lawyer would run: "the enterprise's field includes AI, as evidenced by employing an AI
Officer; his duties are AI; the invention is AI." That argument stretches Geschäftszweig from
*what the company sells* to *what the company uses*, which is not the standard reading — but it is
exactly the fight the job title invites.

### 4.4 The risk, stated plainly

- **The bad fact:** the title. "AI Officer / R&D AI Transformation Manager" puts the word "AI" into
  the duties prong of every test. If Ivoclar ever wanted to fight — realistically only after "get
  famous" succeeds and the asset is visibly valuable — the title is their opening exhibit.
- **The good facts, and they are strong:** the theory was conceived ~2003 and published as a
  302-page monograph in **2015**, roughly a decade before the AI-Officer role existed; every paper
  is published as **"Independent Researcher"** under a personal ORCID with zero Ivoclar affiliation;
  the experimental work runs on a **privately owned** RTX-4090 machine at home; the repos are
  personal; the project has an explicit standing firewall rule (Ivoclar content is handled
  exclusively in a separate project); dental products are a different field.
- **The distinguishing line counsel will draw:** MG's duties are applying AI *to Ivoclar's R&D
  processes* (transformation, tooling, governance) — not conducting basic research on spiking
  neural networks or consciousness. Duties define the Aufgaben prong; a title does not.
- **Net assessment: moderate, manageable, and worth actively engineering down now** — because the
  cost of the risk is not "Ivoclar wins," it is *clouded title*: any future licensee, investor, or
  acquirer will diligence inventorship chains, and an unresolved employer question discounts the
  asset even if the merits favor MG.

### 4.5 One live self-inflicted exposure — fix it now

The personal agent fleet runs on the **Ivoclar office workstation** and the **Ivoclar corporate
notebook** ("in-corp full-dev machine running the personal fleet"). If aIware or crucible sessions
have ever run on those machines — or during paid working hours — that is documentary,
timestamped evidence for the "substantial facilitation by employer resources" prong (Austrian) or
the "in the course of work" element (Swiss/FL). Two actions:

1. **Audit:** sweep the git author metadata, session logs and machine records of aIware and
   crucible for commits or sessions originating from the office hostname or corporate notebook.
   One session of work; produces either a clean bill or a known, bounded problem for counsel.
2. **Cease:** from today, aIware and crucible never run on Ivoclar hardware or during working
   hours, without exception. (The *inverse* — personal hardware doing Ivoclar work — is an
   Ivoclar-policy question, not a patent question, and is out of scope here.)

### 4.6 Evidence pack for independent creation (assemble regardless of strategy)

1. The 2015 monograph (physical copy + ISBN record + publication date proof).
2. The ABOUT/bio record of the 2003 conception, corroborated where possible.
3. Zenodo records: every version DOI with timestamp, all "Independent Researcher."
4. Private git histories (aIware-private, crucible): full commit logs with timestamps and
   author/hostname metadata — plus a generated **commit-time histogram** showing
   evenings/weekends/home-machine concentration. Cheap to produce, highly persuasive.
5. Purchase records for the home 4090 machine and related hardware.
6. Employment contract + role description + start date of the AI-Officer role (showing the theory
   and monograph predate it by ~a decade).
7. The fleet's written firewall rule (Ivoclar content segregated to a separate project).

### 4.7 Sequence with the employer

1. **First:** counsel reads the employment contract (IP-assignment clause, side-activity clause,
   choice of law, any invention-reporting clause). Nothing else happens before this.
2. **Second:** file the priority application (the filing itself is confidential; it does not tip
   anyone off, and it fixes the date).
3. **Third, on counsel's advice only:** decide whether to seek a **negative clearance / release
   letter** from Ivoclar (via the CTO) confirming the AC research is private, pre-existing and
   outside the company's field. A clean letter permanently removes the cloud on title and costs a
   conversation; but raising it also *alerts* the employer, and notification duties
   (OR 332a-pattern; Austrian §§ on Meldepflicht) technically attach only to non-free inventions —
   so whether to volunteer anything is a judgment call that belongs to the lawyer, not to this
   document. Do not have this conversation before steps 1 and 2.

---

## 5. Recommended Filing Strategy

### 5.1 What to file

**One thick priority application** (drafted to PCT/EP standard, ~30–60 pages) covering Clusters A–C
as a single disclosure with multiple independent claims; split later via divisionals/continuations
as needed:

- Independent claim 1 (system): embodied-agent control system comprising a spiking substrate with
  region taxonomy and a **non-foldable, short-return, low-rank re-entrant self-model loop**
  (differential time constant / delay / nonlinearity in the loop as the non-foldability feature).
- Independent claim 2 (training method): the **local three-factor rule** routing credit through a
  learning self-model region, plus the staged emergence protocol; dependent claims on the
  redeployment-vs-relearning control scheme.
- Independent claim 3 (method of operating): few-shot modeling of an external agent by
  **redeployment** of the trained self-model at shallow recursion (the pattern-26 design rule as a
  method step), in a control context.
- Dependent/auxiliary: neuromorphic hardware embodiment; readout/decompilation cluster (prophetic);
  CRM claims.
- Drafted entirely in engineering vocabulary (§2.1); "consciousness" absent from the claims.

**Do not file** anything at the definitional/theory level (dead per §§1–3) or on the ablation-test
protocol (published).

### 5.2 Where and in what order

| When | Action | Purpose |
|---|---|---|
| **Now → early Oct 2026** (before MoC7) | Attorney engaged; contract reviewed; **priority application filed** (EP direct or a well-drafted US provisional — counsel's choice; either sets the Paris priority date). Optionally: Austrian utility model in parallel (6-month grace salvage for recently disclosed apparatus/program-logic matter, §1.1). | Fixes the priority date before the autumn disclosure wave (MoC7, v15, OSF, Show-HN). |
| Oct 2026 → Sep 2027 | Publish freely (poster, prereg, code, v15) — everything after the priority date is harmless to the family. Optionally file a second priority application for material invented after the first (e.g., matured Cluster C/D), to be merged at PCT. FTO/novelty search commissioned. | Science proceeds at full speed; the 12-month window is used to decide seriousness. |
| **≤ Sep/Oct 2027** (12 mo) | **PCT application** claiming priority. | Keeps all ~150 states open; defers the big spend. |
| ~Apr 2029 (30/31 mo) | National/regional phase: **EP + US** as the core; add JP/KR/CN only if the neuromorphic-industry logic justifies it then. | The main go/no-go cost gate; by then M2/M3 results will show whether the mechanisms scale. |
| 2029→ | Prosecution; keep one US continuation and one EP divisional pending (the §3 posture). | Claim-shaping against the field as it develops. |

If the pre-MoC7 window is missed, the fallback ordering is: file before the *next* disclosure event,
accept that whatever MoC7 disclosed joins §1.3's table, and lean on the US grace + Austrian/German
utility-model salvage for it. Every week of delay moves material from §1.4 to §1.3.

### 5.3 Cost envelope (rough, EUR, small-entity scale)

| Phase | Item | Cost |
|---|---|---|
| 0 (2026) | Contract review + employer strategy memo | 1–3k |
| 0 (2026) | Priority application, attorney-drafted | 8–15k |
| 0 (2026, optional) | Austrian utility model(s) | 1–2k |
| 0–1 (2026/27, optional) | FTO / novelty search | 3–6k |
| 1 (2027) | PCT filing (fees + attorney) | 5–8k |
| 2 (2029) | EP + US national phase entries | 12–20k |
| 2 (2029, per extra state) | JP / KR / CN each | 5–8k |
| 3 (2029–2033) | Prosecution to grant, EP + US | 15–30k |
| ongoing | Renewals (rising with age) | 1–4k/yr |
| **Total** | **One family, EP+US, filing → grant, ~7 years** | **≈ €50–80k** |
| | Three families, five jurisdictions | ≈ €150–300k |

The committed near-term spend is only Phase 0 (**≈ €10–20k**); the 12-month and 30-month gates are
natural abandon points if crucible results or finances say stop.

### 5.4 Inventorship note (AI-assisted work)

This project is heavily agent-assisted. EPO: an inventor must be a natural person (J 8/20, DABUS).
USPTO (Feb 2024 guidance on AI-assisted inventions): patentable only where a natural person made a
**significant contribution** to each claim (Pannu factors); AI assistance does not disqualify, but
the human contribution must be documentable. Here the load-bearing inventive concepts are
documented as MG-authored in the project records (the theory, the axis corrections, the design
rulings); keep it that way — for anything destined for a claim, ensure the records show MG's
conception/direction of the *claimed* mechanism, not merely approval of agent output. Flag the
working practice to counsel at the first meeting.

---

## 6. Open Points and Who Settles Them

| # | Question | Settles it |
|---|---|---|
| 1 | Employing entity, IP clause, choice of law, side-activity clause in the employment contract | Employment lawyer (FL and/or AT) — **first action** |
| 2 | Exact disclosure chronology (all Zenodo version timestamps; public-git first-appearance dates for each §8.9 passage; book publication dates; wiki history) | Mechanical; any session can compile Annex A |
| 3 | Whether each §1.4 item is truly absent from every public artifact (papers, books, wiki, public git history, talks) | Session audit + attorney review of the draft spec |
| 4 | Office-machine / work-hours contamination audit (§4.5) | Session audit, then counsel assesses |
| 5 | Austrian GM grace + Programmlogik details; German GM salvage scope | Austrian patent attorney |
| 6 | Claim drafting, G 1/19-proofing, Alice-proofing; FTO vs Bongard/Lipson, Haikonen, neuromorphic estates | European patent attorney (epi) with CII/AI practice — Munich or Vienna; ideally one who prosecutes neuromorphic-computing cases |
| 7 | Whether the shipped trade-book editions disclose the consolidation-channel mechanism (pattern 14) | Session check against the frozen book text |
| 8 | Enablement maturity of Cluster C (decompilation) — file prophetic now vs mature first | Attorney + MG, after CRU-72 scoping |
| 9 | Whether MoC7 materials can be scrubbed of §1.4 content if the priority filing slips | MG + attorney, September checkpoint |

---

*End of analysis. This document is preparatory research for a consultation with qualified patent and
employment counsel; it is not legal advice, and filing decisions must not be made on its basis
alone.*
