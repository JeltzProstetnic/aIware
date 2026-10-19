<!-- Action: reference — ✅ DONE 2026-07-06 (S245): FMT v12 PUBLISHED to Zenodo. Version DOI 10.5281/zenodo.21226262 (https://zenodo.org/record/21226262); concept DOI 10.5281/zenodo.18669891 auto-resolves to v12. Social + infrastructure DOI briefs filed to cross-project inbox. Remaining content below = the DEFERRED other-paper work (canonical: docs/fable-complex-reviews-S244.md + backlog). -->
<!-- Backlog: AIW-13/AIW-105 done S244. -->

# [DONE 2026-07-06] Publish FMT v12 to Zenodo — PUBLISHED, DOI 10.5281/zenodo.21226262

**State at S244 shutdown:** FMT full v12 is COMPLETE, reviewed (9-reviewer adversarial pass + 5 fix passes), and builds clean. MG was **reviewing the PDF and said "so far all fine"** but had NOT given final sign-off when the session ended. **Do NOT publish until MG confirms the PDF.** The DOI is irreversible.

## Current built artifact
- Clean PDF: `tmp/build-full/paper-v12.pdf` (**117 pp, 0 undefined cites, 0 undefined ctrl-seq, 0 overfull >2pt, 0 LaTeX errors**).
- Red-diff (changes since S243 in red): `tmp/build-diff2/paper-v12-reddiff.pdf`.
- Source of truth `.md` + build `.tex` are IN SYNC (full parity sweep done S244).
- Rebuild if needed: `python3 scripts/build_full_pdf.py` (bibtex needs `dangerouslyDisableSandbox`).

## Publish procedure (once MG signs off)
1. **Prepend the v12 entry to `tmp/zenodo-changelog.md`** (the upload script appends this file to the deposit description — skipping = empty release note). Ready-to-prepend HTML block:

```html
<p><strong>v12 changes (2026-07-06): independent adversarial-review pass, Hard-Problem rewrite, qualia-structure prediction</strong> (substantial revision; the core architecture is unchanged).</p>
<ul>
<li><strong>Hard Problem (§3.4.3) rewritten:</strong> conditional dissolution — the level-confusion holds on a constitutive reading of self-referential closure the theory motivates but does not derive (rated partial, ◐); the closure→phenomenality link is made empirically approachable via spontaneous first-person report under a training control, with an explicit confabulation caveat (necessary but not sufficient).</li>
<li><strong>IIT engagement (§7.2):</strong> honest-convergence paragraph — grant IIT's diagnosis (experience as an irreducible, integrated, causally-structured whole) while rejecting substrate-boundness; consciousness located in substrate-neutral self-referential updating at criticality, not intrinsic &Phi;. Barrett &amp; Mediano (2019) &Phi;-undefined-for-non-Markovian critique added with IIT's reply conceded; exclusion postulate stated correctly.</li>
<li><strong>New Prediction 5 (§8.6):</strong> qualia structure is cross-individually shareable (unsupervised Gromov&ndash;Wasserstein alignment of similarity structures; Kawakita et al. 2025) while absolute per-brain encoding is not — a falsifiable dissociation; new qualia-structure paragraph (§3.4.2) anchored to the phenomenal-concept strategy.</li>
<li><strong>Substrate independence:</strong> olfaction (thalamus-bypassing) anchor (Li &amp; Gottfried 2010, Sela 2009); Seth biological-naturalism engagement; Bayne et al. 2024 cross-system testing; Milinkovic &amp; Aru biological-computationalism engaged.</li>
<li><strong>Corrections &amp; honesty:</strong> Casarotto (2016) PCI benchmark comparison corrected; 40/20&nbsp;Hz reframed as a posit; No-Free-Lunch replaced by multiple-realizability; §1 automaton-identity aligned (consciousness = the self-simulation running on the Class-4 automaton, not the automaton itself); Passos-Ferreira &amp; Chalmers 2026 infant-consciousness field-context; citation-breadth 2024&ndash;26.</li>
<li><strong>References:</strong> new verified citations added (Barrett &amp; Mediano 2019, Kawakita 2025, Kriegeskorte 2008, Bayne 2024, Storm 2024, olfaction set); all DOIs web-verified.</li>
</ul>
```

2. **Rebuild** into `tmp/build-full/` (do NOT touch canonical `paper/full/paper.pdf`).
3. **Show MG the built PDF one more time** (irreversible DOI) — only proceed on explicit go.
4. **Upload:** `bash scripts/zenodo-upload.sh tmp/build-full/paper-v12.pdf`. Auto-bumps v11→v12 (v11 = `10.5281/zenodo.20631497`; FMT concept DOI `10.5281/zenodo.18669891`). Override if auto-bump misfires: `ZENODO_VERSION=v12 bash scripts/zenodo-upload.sh …`. Uses `.env.zenodo` (gitignored, non-interactive).
5. **Cross-project briefs after publish:** append to `~/cfg-agent-fleet/cross-project/inbox.md` — (a) **social**: new v12 DOI (the tweet-candidate item filed S244 is waiting on exactly this — "do NOT announce a DOI until aIware confirms publish" → now confirmed); (b) **infrastructure**: homepage/blog → v12 DOI.

## THEN (deferred from S244 — the other-paper work)
The 6 Fable reviews of the rest of the complex are in **`docs/fable-complex-reviews-S244.md`** with prioritized per-paper proposals. Suggested order (see that doc's Synthesis):
1. Cosmology + cosmology-formal **citation-integrity fixes** (fabricated authors — HIGH, disqualifying).
2. Cosmology-formal **sync to corrected parent** (it regressed — asserts retracted physics as Propositions).
3. **RIM inversion** (unity thesis + predictions 7/8 headline; cite mutualism/Dickens-Flynn/Chollet; toy M-node sim) — the path off 3 desk-rejects.
4. Decouple RIM from FMT + disambiguate "recursion" vs "self-reference" across the complex.
5. FMT-formal: extract the §3+§4 transfer-entropy+criticality module as a standalone paper.
6. AIW-106 venue strategy (`docs/fmt-venue-assessment-S244.md`): full FMT = 38k words = monograph → preprint (PhilSci-Archive) + JCS 9k carve (double-blind) + co-author.

## What NOT to do
- Do NOT publish before MG's explicit PDF sign-off.
- Do NOT recompile canonical `paper/full/paper.pdf` (build into `tmp/`).
- Do NOT skip the changelog prepend before `zenodo-upload.sh`.
- Do NOT bundle the theory complex as a "theory of everything" — sequence FMT → RIM → cosmology at arm's length (Fable complex-review directive).
