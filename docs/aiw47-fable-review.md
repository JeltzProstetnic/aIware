<!-- Action: reference -->
<!-- Tracked-by: AIW-47 -->
# AIW-47 eNeuro Opinion — Fable 5 critical review ROUND 2 (2026-06-12, Session 224)

Reviewer: Claude Fable 5 (read-only), of the standard-numbers rewrite. Verdict: **Major, near-minor.**
Round-1 High set (H1/H2/H3) confirmed resolved; corrected numbers internally airtight; double-blind /
two-kinds / no-overclaim compliance clean. Three NEW High items — **all resolved this session:**

- **H-1 (well-powered-vs-underpowered asserted, mechanism absent)** → RESOLVED. Read the authors' own OSF
  scripts: their sig meta-d′ = independent-groups t-test on Bayesian per-subject estimates + ANCOVA with
  `Staircase_SD` covariate; the gap to our trend is the **estimator + covariate**, not pooling. Added the
  mechanism to §"Preliminary evidence" + noted our hierarchical efficiency estimate matches their *marginal*
  M-ratio. (Primary source: `tmp/aiw47-data/gucm2/Material_Behavioral_Data_Syntax.sps`, `Script_Hmetadprime.m`.)
- **H-2 (citation: is the behavioral deficit really in the connectivity-titled 2022 paper?)** → RESOLVED.
  Verified (search + the paper's own abstract): the 2022 BBR paper reports "ketamine-induced deterioration in
  metacognitive performance, whereas no significant effects... for perceptual performance, RTs and bias." The
  2021 *Neurosci. Consc.* episodic-memory paper is a DIFFERENT dataset (N=53). Citation correct + complete.
- **H-3 (selectivity laundered through the original = same Gelman-Stern fallacy)** → RESOLVED. The authors did
  NOT run a drug×measure interaction (sig meta-d′ + n.s. d′ only). Softened to: a fall in one index with the
  other spared is *consistent with* selectivity; establishing it needs the interaction in a free-d′ design.

Also applied: L-1 (94% ArviZ-default HDI → recomputed true **95% HDI [−0.86,+0.14]** from the same seed),
L-3 (first-person "I" → third person), interaction relabel (permutation→Welch p≈0.37, the standard value).

**Still OPEN (presented to MG as a pre-submission checklist, mostly MG/logistics):** M-2 (whether GNW belongs
in the "scalar→covariation" foil or should be softened to a near-neighbour like HOT — positioning call);
M-3 (deposit analysis code publicly; eNeuro increasingly rejects "available on request"); L-2 (figure FILE
names are swapped vs their text LABELS → rename before portal upload); L-5 (title "is necessary" vs body hedge);
M-4 residual (Opinion-type may be queried for carrying original analysis — defensible; word count ~3k OK).

---

# AIW-47 eNeuro Opinion — Fable 5 critical review (2026-06-12, Session 223)

Reviewer: Claude Fable 5 (read-only). Target: `paper/aiw47/aiw47-eneuro-opinion.md`.
Verdict: **MAJOR REVISION.** Writing/hedging/comms = submission-grade; the *discriminating power* of the argument is not yet what the paper claims.

## The three High-severity issues (all judged real on review)

**H1 — The "battery" doesn't discriminate; one leg hands IIT its own weapon.**
The paper concedes meta-d′/d′ doesn't beat HOT, then promises a battery (meta-d′ selectivity + PCI + preserved implicit processing) that does. It doesn't: (a) meta-d′ selectivity = shared with HOT (conceded); (b) **PCI (Casali 2013) is Tononi-co-authored, an IIT-camp complexity measure** → using it to discriminate FMT *from* IIT is self-defeating; (c) preserved implicit processing under anaesthesia is predicted by GNW/RPT/IIT alike → discriminates nothing. Novelty rests entirely on discrimination, so this is the central hole.

**H2 — The staircase clamps d′, so "d′ preserved while meta-d′ falls" is partly by construction.**
If accuracy is held by an online staircase, d′-flat is engineered, and a *scalar account + staircase* predicts the same meta-d′↓/d′-flat pattern → voids this dataset's power to separate covariation from dissociation. Also the manuscript is internally contradictory: "difficulty constant" (stimulus fixed, d′ free) vs "accuracy held by staircase" (d′ clamped) = opposite designs, opposite evidential value. The proposed decisive test inherits the same flaw. MUST disambiguate the actual Lehmann design.

**H3 — "Selective" rests on significant-vs-nonsignificant, not an interaction; stats asymmetrically reported.**
Comparing meta-d′ (p≈0.018, sig) vs d′ (p≈0.11, ns) is NOT a test of difference (Gelman & Stern). Proper test = drug×measure interaction (not run/reported). Worse: results.md §7c gives d′ **Hedges g = −0.49 (medium)** and **MWU p = 0.093 (marginal)** — the manuscript reports only d′'s favourable Welch p (0.11) and OMITS d′'s g and MWU, while meta-d′ gets both tests. → d′ is not cleanly "preserved"; both measures trend down (g −0.49 vs −0.75), overlapping magnitudes. Asymmetric reporting flatters "preserved" and is an honesty-constraint problem, not just presentation.

## Medium / Low (selected)
- **M1** Table 1 likely strawmans IIT: Φ is decoupled from behavioural report → IIT makes no clean SDT covariation prediction; honest entry = "no clean behavioural SDT prediction," not "covariation." (GNW row also contestable — Dehaene links confidence to broadcast.)
- **M2** self-model fidelity ≡ meta-d′ asserted by fiat (meta-d′ = perceptual metacognition, one slice of the self-model).
- **M3** closure-as-level-setter stipulated, imported from Gruber 2026, not argued here.
- **M4** within-vs-between design presented as settled but unresolved → confirm with Lehmann (paired reanalysis may recover M-ratio).
- **M5** reproducing the authors' own effect on the same dataset = estimator-robustness, not new/discriminating evidence; "independently reproduced" (used ~3×) overstates → prefer "reanalysis of the same dataset with an independent estimator."
- **L1** no 2×2 schematic (Session-189 review flagged "zero figures for a 2×2 theory" as a desk-reject signal). **L5** title ("are necessary") firmer than body ("increasingly look like").

## Constraint compliance
Honest hedging PASS-with-caveat (H3 asymmetry tightens it); double-blind PASS-with-residual-risk (sole self-citation + privately shared data narrows authorship); no-four-modules PASS (strong); zero phil-of-mind PASS; citations PASS-with-gaps (add ketamine-psychophysics ref; Brown/Lau/LeDoux 2019 for HOT; Gelman&Stern/Nieuwenhuis for H3; an edge-of-chaos ref).

## Prioritised fixes (Fable's order)
1. Repair or honestly downgrade the discrimination claim (drop PCI as FMT-vs-IIT discriminator → shared level-axis instrument; locate discrimination in a contrast IIT/HOT genuinely can't make — e.g. a predicted coupling between the level axis and the *self*-model axis / an implicit-*self*-model effect — or reframe contribution as "sharper falsification handle for scalar-vs-architecture," not "discriminates among theories").
2. Resolve the staircase confound (state free vs clamped d′; if clamped, concede d′ channel uninformative for this dataset; redesign the decisive test without accuracy-clamping).
3. Report the drug×measure interaction + symmetric stats (d′'s g=−0.49 and MWU=0.093 alongside meta-d′'s); let "selective" rest on the interaction.
4. Fix Table 1 IIT/GNW rows (de-strawman).
5. Concede the two definitional leaps (M2/M3).
6. Confirm within/between design with the authors (M4).
7. Add a 2×2 schematic; relabel "reanalysis, same dataset, independent estimator"; align title; (figure path codename is internal-only, not in the rendered PDF).

Full review text preserved in session transcript (Session 223).
