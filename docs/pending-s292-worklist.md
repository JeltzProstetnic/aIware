<!-- Action: reference -->
<!-- SUPERSEDED 2026-08-07 (S292 close). AIW-170 and AIW-171 are DONE and RIM is published
     as Zenodo v3. AIW-172 and AIW-174 carry forward into docs/pending-s293-cosmology.md, which is
     the actionable brief. Kept for the constraints and MG's verbatim work order. -->
<!-- Tracked-by: AIW-171, AIW-172, AIW-174, AIW-170 -->
# S292 work order — MG-set, 2026-08-07

**Both papers are BLOCKED from publishing until their defect lists close.** MG cleared both to publish
during S291 — that clearance was given *before* the Fable passes returned and does **not** carry over.
Do not publish either paper on the strength of the earlier "publish cosmology" / "then publish" instruction.

Full defect lists: `docs/pending-s291-fable-defects.md`. Cosmology notes: `docs/s291-cosmology-review-notes-fable.md`.

## The four items MG assigned to this session, in his words

> "next session, 171 and 172 and 170" … "yes P0 next session together with 172" (on the
> information-causality / Tsirelson route)

1. **`AIW-171` (P0) — RIM defect repair, then publish.**
2. **`AIW-172` (P1) — cosmology defect repair, then publish.**
3. **`AIW-174` (P0) — the Tsirelson-from-Bekenstein derivation**, run *together with* `AIW-172`.
4. **`AIW-170` (P1) — close the citation-gate gap** that let all of this through.

## Order of operations — do it in this sequence

**`AIW-174` depends on `AIW-172` error 2.** The Bekenstein bound is currently misattributed as
area-proportional throughout SB-HC4A; the derivation needs it stated correctly (it is energy × radius; the
area law is 't Hooft/Susskind, and the rigorous modern forms are *relative-entropy* statements). Repair
first, derive second — or at minimum fix the statement of the bound before building on it.

Suggested order: `AIW-170` (cheap, and it protects everything after it) → `AIW-171` → `AIW-172` → `AIW-174`.

## Hard constraints — do not skip these

- **Re-verify every citation claim as you fix it.** Four of the agents' claims were independently confirmed
  against Crossref/arXiv in S291 (Gignac→Oberleiter, Huang→Vu, Balboni→Sternberg, Bisio/Tosini→Perinotti).
  **The rest are agent-reported only.** An agent's citation finding is a hypothesis until checked — that is
  the whole lesson of this session, and re-fixing on trust would repeat it one level up.
- **RIM has no md→tex generator.** Every content change goes into BOTH `paper.md` and `paper.tex` or they
  drift. Cosmology is the opposite: `sb-hc4a.md` is the single source and `sb-hc4a.tex` is a stale pandoc
  artifact — do not edit it.
- **Load `.claude/knowledge/prose-register.md` before writing any prose** (new S291, triggered from
  CLAUDE.md). The register sweep is step 4 of its workflow and gates any draft shown to MG. Six tells
  survived into the S291 prose; they are listed in the defect file and must go in the same pass.
- **Run the whole-paper review before publishing** (new rule in `publication-build.md`), not a
  backlog-scoped one. Scoping the S291 cosmology pass from two open items is what produced a tiny diff and
  a false sense of health.
- **Do not follow `james-flynn.net`** — it 301s to a squatted domain.
- **Never build the canonical cosmology PDF in place**; build to `tmp/` and copy on approval. RIM's
  `build_rim_pdf.py` DOES write the canonical in place, which is correct only when a canonical rebuild is
  intended.
- **Review diffs: use `latexdiff --type=CCHANGEBAR`**, not `UNDERLINE`. Underline suppresses hyphenation and
  put 11 overfull boxes into the S291 review PDF; MG saw text past the margin. And compile diffs through the
  gated wrapper, not raw pdflatex.

## The single judgement call waiting for MG

**RIM C5, §3.1.** The NFC→Gf / TIE→Gc dissociation is reported opposite to von Stumm & Ackerman (2013)
according to the Fable pass (agent-reported, NOT yet independently verified — verify first). If it holds,
the unity-of-motivation claim loses its only concrete empirical illustration, and that claim is in the
abstract. Options are (a) find a correct illustration, (b) soften the abstract to what §7.2 actually stakes,
(c) let prediction 9's matched-*k* contrast carry it alone. **Do not choose for MG.**

## Also open, not assigned to S292

- `AIW-173` (P2) — the saturation-trigger automaton experiment. Compute is on the WSL box.
- Optional, MG's call: one sentence in cosmology §10.1 conceding Axiom 1 is arguable rather than axiomatic.
- Optional, offered and not done: file the Schultz & Cole redeployment observation (higher intelligence →
  *less* task-related network reconfiguration, a candidate neural signature for didactic patterns #20/#26)
  into `.claude/knowledge/didactic-patterns.md`.
- Nothing has been pushed. The public remote is untouched.
