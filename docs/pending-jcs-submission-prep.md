<!-- Action: reference -->
# JCS Submission Prep — Option C Hybrid

**Tracked-by:** AIW-46
**Decision date:** 2026-04-14 (Session 184)
**Strategy:** Fire-and-forget background work. Main attention should go to AIW-49 (BBS commentary, Jun 12 deadline) and AIW-48 (McFarnell registered report). JCS is the last specialist-venue attempt for the full unification paper before pivoting entirely.

## JCS Requirements (verified from imprint.co.uk Apr 14)

- **Word limit: 9,000 words** including abstract, footnotes, references. **HARD.**
- Submission by email (no portal): `graham@imprint.co.uk` + `graham.jcs@gmail.com` (whitelist both)
- Managing Editor: Graham Horswell
- Anonymized mandatory ✓ (already have double-blind from C&C)
- 150-word summary at the front (separate from abstract — write fresh)
- 50-100 word author bio for "about authors" section
- AI policy compliance statement in submission email
- Harvard referencing with DOIs where available
- Style: educated multidisciplinary readership, minimize jargon, math/lab details to footnotes/appendices
- No APC for subscription route; £1,500 for gold OA (decline)
- Format: Word, RTF, or PDF. Figures inside the document.

## Source manuscript

Start from `paper/trimmed/noc/four-model-theory-noc.md` (11,740 words, anonymized version exists).
**NOT** the C&C version (12,715 — too far over).

## Cuts needed: ~2,740 words

**Concrete trim targets:**

1. **References: 73 → ~50** (saves ~600 words)
   - Drop tangential cites (anything cited only once and not load-bearing)
   - Keep all empirical convergence citations (Toker, Tucker/Friston, Bieberich, Beni, Alnagger, Casali, etc.)
   - Keep all theoretical comparators (GWT, IIT, RPT, HOT, AST, PP)

2. **Section 8 (Empirical Convergence) → one tight paragraph** (saves ~800 words)
   - JCS multidisciplinary audience won't reward exhaustive empirical name-dropping
   - Cite Toker + Tucker/Friston + ConCrit as three load-bearing convergence points
   - Drop the per-prediction confirmation table

3. **Section 10 (Discussion) tightening** (saves ~600 words)
   - Drop McFarnell adversarial experiment subsection (preserve elsewhere — this is the seed for AIW-48)
   - Compress "limitations" section to one paragraph
   - Drop the "future work" subsection entirely

4. **Section 5 ↔ Section 7 redundancy removal** (saves ~500 words)
   - Architecture is described twice (once in Section 5 proper, once in the comparative analysis)
   - Pick one canonical description, reference it from the other

5. **General prose tightening across all sections** (saves ~300 words)
   - Pass for hedge phrases, redundant signposting, "as we have seen" filler

**Total estimated savings: ~2,800 words.** Should land at ~8,940. Leave room for the 150-word summary addition.

## Add to the manuscript

- **150-word summary** at the front. Distinct from the abstract — accessible, no jargon. Aim: a literate non-specialist (philosophy grad student, neurophilosophy postdoc) understands the claim, the novelty, and why it matters in 150 words.
- **Author bio (50-100 words)**: Independent researcher, Vorarlberg. 2015 German monograph "Die Emergenz des Bewusstseins" (Lulu Press). 2026 English pop-sci version "The Simulation You Call 'I'" (KDP). ORCID 0009-0005-9697-1665. Background in [TBD — keep it short].

## DOI pass

- Add DOIs to every reference where one exists
- Use crossref.org or Semantic Scholar API
- Harvard format: Author (Year) "Title", *Journal*, vol(issue), pp. xxx-yyy, doi:10.xxxx/...

## Build target

`paper/jcs/` directory:
- `four-model-theory-jcs.md` (source, 9,000 words)
- `four-model-theory-jcs.docx` (submission)
- `four-model-theory-jcs.pdf` (review copy)
- `cover-email.md` (full email body for Graham Horswell)
- `summary-150.md` (the front summary)
- `author-bio.md` (50-100 word bio)
- `ai-compliance-statement.md`
- `submission-checklist.md`

## Cover email — required elements

- Subject: "Submission: The Four-Model Theory of Consciousness — Theoretical Article"
- Greeting to Graham Horswell
- One paragraph: title, brief description, word count, anonymized status
- Statement: not under consideration elsewhere
- AI compliance statement (per JCS policy — TBD what exactly they require, check at submission time)
- Author contact info
- Note that previous related work is on Zenodo (DOI 10.5281/zenodo.19064950) — be honest about the preprint trail

## Effort estimate

3-4 hours focused work. Best executed as one continuous session (cuts need to be coherent, not patched).

## Risks

- **Still gets desk-rejected.** JCS has rejected unaffiliated independents before. The 9k cut alone won't fix the credibility-signal problem. But: JCS standards favor philosophical framing, which FMT actually is, so the probability is materially higher than C&C/NBSR/PLREV.
- **Time spent here is time not spent on BBS/McFarnell.** This is an explicit strategic tradeoff — keep JCS bounded to one focused session, do not let it expand.
- **AI policy compliance statement** — JCS guidelines say "include confirmation of compliance" but don't link the policy. Need to find it before submission. Likely a one-line statement that AI was/wasn't used in writing.

## Decision rule

If the cut takes more than 4 hours of work or starts requiring structural rewrites rather than trimming, **stop and skip JCS**. The strategy already says BBS and McFarnell are higher-leverage. Don't sink-cost into a 6th journal attempt.
