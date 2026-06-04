# Pending: RIM v2 Preprint Upload (AIW-18)

Action: act

**Tracked-by**: AIW-18 (P1, Session 211)
**Decision date**: 2026-06-04 (Session 211)
**Strategic context**: Track A of the two-track RIM publication plan. Track B = COGITO empirical paper with Schmiedek/Völkle/Wittmann (post data-application). RIM v2 must exist as a citable preprint BEFORE Schmiedek/Völkle see the framework via Wittmann's brokerage intro, so the empirical paper has a stable theory citation.

---

## Goal

Upload **RIM v2** (current state, as it exists in `paper/intelligence/`) to **PhilSci-Archive** as the primary archive, with **Zenodo** as fallback. Outcome: a permanent, citable preprint DOI/handle for the RIM theory anchor.

## Why PhilSci-Archive primary

- Open access, free.
- Philosophy of science scope — RIM's theoretical framing fits.
- PsyArXiv already rejected v2 ("outside scope") — that route is closed.
- Zenodo is fine as fallback but is generalist; PhilSci-Archive signals to academic readers that it is intended for philosophy-of-science discourse.

## Pre-upload checklist

- [ ] Confirm current state of `paper/intelligence/paper.md` and corresponding `.tex`/`.pdf` — is v2 the latest, or has it been touched since v2 preprint attempt?
- [ ] Run `pytest tmp/test_content_integrity.py -v` if test infrastructure for RIM exists (otherwise spot-check).
- [ ] Rebuild PDF: `python3 tmp/build_intelligence_pdf.py` if such a script exists; otherwise from current `.tex` via `pdflatex` + `bibtex` (use `dangerouslyDisableSandbox` if needed).
- [ ] Verify PDF compiles cleanly without `???` citations.
- [ ] Visual spot-check: title page, abstract present, references render, figures (if any) intact.
- [ ] Confirm Zenodo concept DOI for RIM still valid (10.5281/zenodo.20125096 from Session 198) — PhilSci-Archive entry should link to it.

## PhilSci-Archive upload procedure

1. **Account**: confirm or create at https://philsci-archive.pitt.edu/. User may already have an account from prior philosophy-of-science engagement; check `passwords/` vault or prior browser logins. If no account: create with `matthias@matthiasgruber.com`.
2. **Submission form**: Title, Author(s), Abstract (~250 words), Keywords (4-6: recursive intelligence model, four-model theory, cognitive variability, evaluation function, computational psychometrics), Subject classification (likely "Specific Sciences > Psychology > Cognitive Psychology" and "General Issues > Philosophy of Mind"), Date.
3. **License**: CC-BY 4.0 (matches Zenodo deposits, matches book licensing convention).
4. **File**: upload the PDF from `paper/intelligence/paper.pdf`.
5. **Conference / journal field**: leave blank (preprint, no venue commitment).
6. **Notes**: mention "Companion paper: Four-Model Theory of Consciousness, Zenodo DOI 10.5281/zenodo.20415804". Mention this is v2 (revised from the version that received 3 desk rejections at Phil Psych / Theory & Psychology / NIdP).

## Zenodo fallback procedure (if PhilSci-Archive blocked or down)

1. Token at `~/aIware/.env.zenodo` (this machine: verify exists post-clone — may need to vault-restore).
2. Use existing `scripts/zenodo-upload.sh` if available.
3. Reuse RIM concept DOI 10.5281/zenodo.20125096 — this is a version update, not a new deposit.

## Post-upload actions

- [ ] Update `references.md` with the PhilSci-Archive handle.
- [ ] Update `paper/intelligence/paper.md` / `.tex` with the new self-citation handle (so subsequent copies reference correctly).
- [ ] Update aIware `backlog.md` — mark AIW-18 done.
- [ ] Update `~/cfg-agent-fleet/cross-project/contacts.md` Wittmann row — note RIM v2 preprint is now live and citable (so the COGITO collaboration brokerage can cite a stable preprint).
- [ ] Update `correspondence/wittmann-werner.md` — add Message 24 (Gruber → Wittmann) mentioning the RIM v2 preprint handle, paired with the COGITO Antragsskizze.
- [ ] Notify Wittmann of the preprint via the same reply that includes the Antragsskizze (`drafts/cogito-antragsskizze.md`) — gives him a citable theory anchor to forward to Schmiedek/Völkle.

## Estimated effort

- Pre-upload checks: 30 min
- PDF rebuild (if needed): 30-60 min
- PhilSci-Archive form: 20 min
- Post-upload tracking updates: 15 min

**Total: 1.5-2 hours focused work, single session.**

## Risks

- PhilSci-Archive may take days to approve the submission (editorial check). Account for this in Wittmann brokerage timing — don't promise the citable handle to Wittmann before the archive approves.
- If `.env.zenodo` is missing on Deck 2, Zenodo fallback fails until the vault is updated (cfg-agent-fleet inbox already tracks Zenodo token vault completeness).
- If the RIM v2 PDF needs build-system fixes (no test infrastructure exists per backlog `tmp/test_content_integrity.py` reference for RIM specifically), allocate an extra session for that work first.

## Notes

- RIM has been **desk-rejected 3 times** (Phil Psych Feb 25, T&P Mar 4, NIdP). PhilSci-Archive is not peer reviewed — it is a moderated preprint server. The point of this action is **citability**, not peer review.
- Future RIM peer-reviewed publication target is now Track B (RIM-on-COGITO empirical paper with Schmiedek/Völkle co-authors).
