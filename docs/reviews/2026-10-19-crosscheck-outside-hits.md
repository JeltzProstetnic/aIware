# AIW-303 known findings — hits outside aIware (read-only scan, S342)

**Places outside aIware where the known findings apply (read-only scan, nothing edited)**

Verdict: most live hits come from text written before S329/S341, mainly criticality treated as a requirement. They sit in the published book, the crucible/mirror-box spec, older blog posts, the live Bluesky bio and twitter-strategy.md. The websites themselves are deployed exactly as the repo has them: the live and local copies are byte-identical, apart from one local copy that is older than the live one.

## 1. crucible — /home/jeltz/crucible/papers/fmt-implementation-spec.md
The report places all of these in the crucible spec. The text is unchanged, so the line numbers still match. Route through the crucible inbox.
- :11 "four nested models on a substrate operating at the edge of chaos … (implicit/structural vs. explicit/phenomenal)". Findings: SUFFICIENCY-17, ARCHITECTURE-1, ARCHITECTURE-7, ARCHITECTURE-15, PHENOMENAL-2, PREDICTIONS-5. Replace with: "real-time self-simulation across four model kinds along two axes (mode, an orthogonal contrast; scope, a nesting) on a substrate running free modelling … (implicit/structural vs. explicit; phenomenal in the closed loop)".
- :42 "IS the conscious perception of the world", :44 "This IS what it's like…", :49 "IS the conscious experience of being a self". Finding: PHENOMENAL-2. Add "where its content enters the self-model's closed loop".
- :73 ρ(s,ν,t) and :241–244 ρ₀–ρ₃. Finding: PHENOMENAL-13. Rename the depth labels ρₙ → μₙ.
- :80 "ν > ν_crit is conscious, ν < ν_crit is not". Finding: PHENOMENAL-2. Replace with: "ν > ν_crit is explicit; it is conscious where it also enters the closed loop".
- :87 "## 3. The Five Principles" and :89 "derives from five principles". Finding: ARCHITECTURE-1. Change to three principles, with redirection, permeability and forking listed as consequences.
- :92 "must operate at the **edge of chaos**". Findings: SUFFICIENCY-17, ARCHITECTURE-1. Replace with: "The substrate must support open-ended (Class 4-capable) computation and recruit it for self-modelling (free modelling); near-criticality (σ≈1, λ≈0, α) is a signature to monitor, not a setpoint to enforce."
- :100 "DFA exponent α ≈ 1". Finding: PREDICTIONS-14. Replace with: "α in 0.6–0.9 (Hardstone et al., 2012) indexes long-range temporal correlations".
- :102 "must be tunable to criticality". Findings: SUFFICIENCY-17, PREDICTIONS-5. Replace with the measured demand-gated peak in the ordered regime, with σ and λ reported beside rate-matched surrogates.
- :182 "### 4.2 Criticality Requirement". Finding: SUFFICIENCY-17. Retitle: "Free-modelling capability (criticality as readout)".
- :206–209 "Consciousness ⟺ [σ ∈ …] ∧ …" and :423 "σ ∈ [σ_low,σ_high] ∧ ρ near all 4 corners ∧ Φ(m*)=m*". Findings: SUFFICIENCY-17, ARCHITECTURE-1. Replace the σ conjunct with free modelling, and replace ⟺ with ⟸ (jointly with embodiment and at least one pain-pleasure axis).
- :215 "Self-model + no criticality = … simulation can't run". Findings: SUFFICIENCY-17, PREDICTIONS-5. Replace with: "Self-model + no free modelling = correct architecture, simulation can't run (anesthetized brain; in cortex the loss usually shows as subcriticality)".
- :227, :229, :265, :382, :421, :446 "Φ(m*) = m*". Findings: SUFFICIENCY-15, PHENOMENAL-13. Change Φ → Ψ.
- :233 "This IS phenomenal experience". Finding: PHENOMENAL-2. Add: "in the closed loop".
- :239–244 depth table. Findings: PHENOMENAL-11, ARCHITECTURE-18. Add a "Minimal consciousness" row above Basic (same μ₀, differs on richness).
- :261 "at least ρ₁ … for any meaningful consciousness". Finding: PHENOMENAL-11. Replace with: "The base case is depth μ₀: minimal and basic consciousness. Depth ≥ μ₁ is required for reportable, extended consciousness, not for consciousness as such."
- :346 "should peak near σ ≈ 1", :356 "by disrupting criticality", :358 "Sustained operation at criticality". Finding: PREDICTIONS-5. Restate in terms of free modelling: abolition happens by abolishing free modelling, and the coherence peak was measured at λ≈−0.68 in the ordered regime.
- Not cited in the report, but the same defects in the same file:
  - :66 "This is why the Hard Problem dissolves". Finding: PHENOMENAL-7. Replace "dissolves" with "is transformed".
  - :110 "self-referential, at criticality". Finding: SUFFICIENCY-17. Replace with "with free modelling".
  - :303 and :419 "C(t) = ∫∫_{ν_crit} ρ" labelled "Total conscious content", and the :440 glossary entry "explicit (conscious)". Findings: PREDICTIONS-6, PHENOMENAL-2. Restrict C(t) to the closed loop's support with χ_loop, and gloss ν_crit as the explicit/implicit boundary only.

## 2. simbook
**pop-sci/book-manuscript.md (EN)** is before S329 throughout. All nine translations other than DE (es, fr, it, nl, pt, ja, ko, zh, el) have the same 2524 lines, so these line numbers carry over to them. In the DE manuscript the matching lines are :448, :464, :520, :912, :1385, :1845 and :2409.
- :463 "must operate at what mathematicians and physicists call the **edge of chaos**". Finding: SUFFICIENCY-17/18 family, ruling 3. Replace with: "must have free modelling: open-ended (Class 4) computation recruited for its own modelling; in cortex this usually shows as dynamics at the edge of chaos".
- :471 "This is where consciousness lives. Only edge-of-chaos dynamics have both properties". Finding: SUFFICIENCY-24. Replace with: "The edge of chaos is one place a medium supports open-ended computation, not the only one; in cortex the capability usually shows as near-critical dynamics."
- :479 "the physical one (the substrate must operate at criticality) … Both thresholds must be met. Together, they are sufficient." Findings: SUFFICIENCY-13, SUFFICIENCY-12, ruling 3. Replace the threshold with free modelling, and replace "Together, they are sufficient" with: "Neither is sufficient alone or together; what suffices is the four model kinds under closure, with free modelling, embodiment and at least one pain-pleasure axis."
- :535 "meta-analysis of 140 datasets … Their conclusion: consciousness tracks criticality". Finding: CITATIONS-2. Change 140 → 143, and attribute "tracks criticality" to ConCrit as a proposal.
- :745 "Propofol … Thalamocortical connectivity is disrupted … push below criticality". Findings: CITATIONS-1, ruling 3. Replace with: "frontal-to-parietal (corticocortical) feedback connectivity fails while thalamocortical connectivity is preserved; free modelling is abolished and the substrate turns subcritical with it".
- :759–769 state table and "determined by two factors: whether your substrate is at criticality". Finding: SUFFICIENCY-4. Order the states by whether free modelling and the explicit models are running, and keep the criticality column as the usual signature.
- :807 and :809 vegetative "subcritical substrate" / covert "The substrate is critical". Finding: SUFFICIENCY-4. Reword in terms of free modelling. Criticality was not measured in Owen 2006.
- :933 "Commitment 3: Criticality is the physical threshold … may not reach criticality and thus would not be conscious". Finding: SUFFICIENCY-17 family. Replace with: "Free modelling is the computational threshold; near-criticality is its usual cortical signature."
- :385, :931, :1077, :1125, :1181, :1223, :1237, :1407 ("The theory requires criticality"), :2476 ("Build the Four Models at Criticality"), :2480 ("four nested models … at criticality"). Findings: SUFFICIENCY-17, ARCHITECTURE-15. Change "at criticality" → "with free modelling", "four nested models" → "four model kinds", and :1407 "requires criticality" → "requires free modelling".
- :1529, :1697, :1839 Class 4 defined by self-organized criticality ("the only known way…"). Finding: SUFFICIENCY-18. Replace with: "self-maintaining, in physical substrates typically through self-organized criticality".
- :1873 "a self-referential simulation running at the edge of chaos … Qualia … dissolved". Findings: PHENOMENAL-7, ruling 3. Change "running at the edge of chaos" → "running free modelling", and "dissolved" → "transformed".
- :413 "The question dissolves". Finding: PHENOMENAL-7. Replace with "is transformed".
- explicit = phenomenal with no loop. Findings: PHENOMENAL-1, ARCHITECTURE-7, ruling 4.
  - :167 "virtual side … conscious" → "conscious where its content enters the self-model's closed loop".
  - :211 "it is *all* of experience". Keep the line, and add that explicit content outside the self-model's loop is preconscious.
  - :339 and :457 "explicit models … are where experience lives" → "the closed loop of the explicit models".
  - :609 caption "explicit models generate phenomenal experience" → add "in the closed loop".
  - :2355 "fully explicit (…, phenomenal)" → "phenomenal in the closed loop".
- "four models" read as modules (ARCHITECTURE-16). :2420 "If the four models are genuinely distinct processes, we should be able to see them in brain scans" → "four model kinds".

**pop-sci/blurb.txt, no-outside/listing.md, no-outside/kdp-form-fields.txt:** none.

## 3. Websites
Live and local are identical (md5) for matthiasgruber.com /, book.html and publications.html, for research …/consciousness/, and for the fmt pages and llms-full.txt. The fmt site matches the aIware wiki build as of today, so its hits are in the aIware `wiki/` sources.

**Exception:** the local copy `sites/matthiasgruber.com/fmt-map/fmt-prediction-map.json` is older than the live file. The live file equals the research-site copy, with 52 differing fields.

- matthiasgruber.com/book.html:258 (also -staging) "A book that dissolves the Hard Problem". Finding: PHENOMENAL-7. Replace with "transforms the Hard Problem".
- book.html:263 "self-referential computation at criticality". Finding: ruling 3. Replace with "self-referential computation with free modelling (open-ended computation recruited for self-modelling)".
- research-site/build.py:51 (rendered on research …/consciousness/ and /publications/) "treating the four models as a minimum sufficient set". Findings: SUFFICIENCY-12, ARCHITECTURE-8. Replace with "minimum set of model kinds the architecture forces, not an exhaustive enumeration".
- Live fmt-map (matthiasgruber.com and research …/fmt-map/fmt-prediction-map.json):
  - Node E8 "Thalamocortical effective connectivity breaks down at propofol-induced loss of consciousness, with structural connectivity preserved", refs [2, 5 = Boly 2012]. Finding: CITATIONS-1/PREDICTIONS-1. Replace with "Frontal-to-parietal backward corticocortical effective connectivity fails at propofol LOC while thalamocortical connectivity is preserved (Boly et al., 2012)".
  - Edges D1→D2 "Thalamocortical breakdown is the expected form of channel failure" and D1→E8 depend on E8 and need revisiting with it.
  - Source of these nodes and edges: aIware drafts/papers-moc7/fmt-prediction-map.json.
- fmt.matthiasgruber.com, from aIware `wiki/`:
  - core-architecture/four-model-theory.md:34 and open-questions/minimum-configuration.md:13 "*minimum sufficient set*". Finding: SUFFICIENCY-12. Replace as above.
  - four-model-theory.md:5, :11, index.md:16, ai-consciousness/ai-welfare.md:33, engineering-specification.md:24 and :98, physical-foundations/wolfram-classes.md:29 "four nested models". Finding: ARCHITECTURE-15. Replace with "four model kinds along two axes (mode, an orthogonal contrast; scope, a nesting)".
  - four-model-theory.md:26 and :61 "explicit (generated, phenomenal)", philosophical/not-illusionism.md:19 "Within the EWM/ESM, experience has genuine phenomenal character", hard-problem/virtual-qualia.md:19 "virtual, phenomenal side". Findings: PHENOMENAL-1, ARCHITECTURE-7. Add "in the self-model's closed loop".
  - foundations/historical-context.md:74 "a two-level ontology that dissolves the Hard Problem". Finding: PHENOMENAL-7. Replace with "transforms".
  - physical-foundations/two-thresholds.md:21, quoting master, "Propofol disrupts thalamocortical connectivity". Finding: CITATIONS-1. Follow the master fix.
  - reference/key-figures.md:149 "~140 datasets". Finding: CITATIONS-2. Change to 143.
  - limitations/other-minds.md:35 "would be qualitatively distinguishable". Finding: SUFFICIENCY-7. Replace with "may become apparent".
- Blog (infrastructure/blog/content/posts, all live):
  - four-model-theory-introduction.md:74 "140 neural datasets confirming… The signature … tracks consciousness". Findings: CITATIONS-2, PREDICTIONS-3. Change to 143, and say it supports the near-critical cortical signature, not the requirement.
  - four-model-theory-introduction.md:100 "consciousness requires edge-of-chaos criticality … confirmed". Findings: ruling 3, PREDICTIONS-3. Replace with "consciousness requires free modelling, whose cortical signature is near-criticality; that signature was predicted in 2015".
  - four-model-theory-introduction.md:108 "doesn't operate at criticality … at the right dynamical regime". Replace with "doesn't recruit open-ended computation for modelling itself".
  - can-ai-be-conscious.md:38 "must operate in … edge-of-chaos criticality" and :73. Finding: ruling 3. Replace with free modelling, with criticality as its usual signature.
  - one-theory-all-the-phenomena.md:14 "Four functional models — world, body, self, and a meta-model integrating them — operating at a critical dynamical regime". Finding: ARCHITECTURE-16 (wrong taxonomy and modules) plus ruling 3. Replace with "Four model kinds (implicit/explicit × world/self) under self-referential closure, with free modelling".
  - one-theory-all-the-phenomena.md:67 "When criticality is exceeded, the meta-model destabilizes" and :99 "Insects possibly lacking a meta-model". Same issue: rephrase onto the ESM.
  - beautiful-loop-two-languages.md:38 "FMT commits explicitly to criticality: the loop has to run at the edge of chaos". Replace with "FMT commits to free modelling (Class-4 capability recruited for self-modelling); near-criticality is its usual signature".
  - same-loop-from-both-ends.md:18 "self-referential updating held at criticality … poised at the edge". Replace with "self-referential updating with free modelling".
  - self-referential-simulation-commentary-seth.md:24 "self-referential simulation at criticality … hold itself at criticality". Same replacement.
  - the-ai-interviews-the-consciousness-guy.md:68 "has to operate at the edge of chaos", :70 "140 datasets", :102 "no criticality", :138 "running at criticality has phenomenal experience". Findings: ruling 3, CITATIONS-2. Same replacements, plus 143.
  - how-ai-misreads-fmt.md and what-the-loop-carries.md are already correct.

## 4. social (evergreen documents only)
- **Live Bluesky bio (@matthiasgruber.bsky.social, confirmed via public API)**, also in drafts/bluesky-profile-setup-2026-08-12.txt:38: "a system that models its world and models itself, held at criticality". Finding: ruling 3. Replace with "…models itself, with open-ended computation turned on itself" (238 chars → recheck the 256-char limit).
- drafts/bluesky-profile-setup-2026-08-12.txt:53, the pinned first post: "self-referential modelling at criticality". Replace with "self-referential modelling with free modelling (open-ended computation)". This is only needed if the post is still pinned or reused.
- twitter-strategy.md:
  - :75, :123, :263, :324, :466 "predicted edge-of-chaos criticality as necessary … confirmed by 140 datasets". Findings: ruling 3, PREDICTIONS-3, CITATIONS-2. Replace with "predicted in 2015 that cortex would show a near-critical signature of free modelling; Hengen & Shew's 143-dataset meta-analysis (2025) found the near-critical setpoint".
  - :91, :209, :257, :262 "dissolves the hard problem". Finding: PHENOMENAL-7. Replace with "transforms".
  - :107 "why explicit models = consciousness", :259 "explicit world/self (= consciousness)", :485 "The explicit self-modeling process IS your subjective experience". Finding: ruling 4. Add "in the closed self-model loop".
  - :260 "Class 4 criticality". Replace with "Class 4 capability (free modelling)".
- docs/fmt-theory-bridge-map.md:15, :18, :20 "the loop at criticality" / "closure + criticality dynamics". Finding: ruling 3. Replace with "the closed loop with free modelling".
- docs/amazon-bios.txt, docs/amazon-author-note.txt, social CLAUDE.md: none.

## 5. mirror-box
- papers/fmt-implementation-spec.md is a copy of the crucible spec, the same 450 lines and identical apart from whitespace. Every crucible hit in section 1 applies at the same line numbers. Fix both copies, or replace the mirror-box copy with a pointer to the crucible one.
- docs/design-spec.md:535 "NOT a dynamical system at criticality". Finding: ruling 3, a weak hit. Replace with "NOT free modelling (no open-ended computation recruited for self-modelling)". :18 is exploratory wording and fine.