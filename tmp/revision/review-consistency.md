# Internal Consistency Review: paper.tex (build-highlighted)

Review performed on the full 1180-line paper. Findings organized by severity.

---

## Critical Issues (fix before publication)

### C1. Dangling reference: "Section 6.5" (reconfiguration)
**Line 353:** `(see Section 6.5)` -- Section 6.5 (Clinical Dissociations) was removed. The revision comment on line 853 confirms: "§6.5 Clinical Dissociations removed." The current Section 6 only has subsections 6.1-6.4. The reconfiguration bullet now has no valid target.

**Fix:** Remove the cross-reference or redirect to the appropriate location (the CBT/reconfiguration content was cut entirely per the revision comment; the bullet should either reference a surviving passage or be self-contained).

### C2. Dangling reference: "Section 6.3 on split-brain" (two locations)
**Line 351:** `(see Section 6.3 on split-brain)` -- Section 6.3 is now "Dreams and Lucid Dreaming." Split-brain content was explicitly moved to Section 5.2 (Holographic Storage and the Patchwork Principle), as confirmed by the revision comment on line 806: "Split-brain content moved to §5.2."

**Line 698:** `This property is critical for understanding split-brain phenomena (Section 6.3)` -- Same issue.

**Fix:** Change both references from "Section 6.3" to "Section 5.2" (or wherever split-brain is now discussed in the body text). However, note that Section 5.2 does not contain the split-brain discussion in the active text either -- the split-brain content appears only in comments (lines 806-809). The split-brain discussion now appears primarily in Section 8.1 (empirical convergence, line 978) and in the animal consciousness table (line 840). If the split-brain argument is supposed to anchor the "cloning" software-like property, it needs a home in the body text, not just in comments and convergence evidence.

### C3. Misdirected reference: "the anesthesia discussion of Section 6.2"
**Line 328:** `(as in the anesthesia discussion of Section 6.2)` -- Section 6.2 is now "Self-Model Disruptions: Anosognosia and DID." The section does mention propofol briefly via Katlowitz (2026), but its primary content is anosognosia and DID, not anesthesia. The main anesthesia discussion is in Section 5.3 (Table 4: Consciousness States and Criticality), which covers propofol, ketamine, and anesthetic convergence.

**Fix:** Change "Section 6.2" to "Section 5.3" or remove the parenthetical.

### C4. Table numbering mismatch: "Table 5" vs actual LaTeX numbering
**Lines 871, 873:** Text refers to "Table 5" for the Theory Comparison scoring matrix. However, LaTeX auto-numbers tables by `\caption{}` order:
- Table 1 = "Empirical Handles for FMT-Specific Constructs (Table 1b)" (line 252)
- Table 2 = "The Four-Model Architecture" (line 281)
- Table 3 = "Independent Convergence on Criticality" (line 507)
- Table 4 = "Consciousness States and Criticality" (line 711)
- Table 5 = "Empirical status of software-like operations across species" (line 845)
- Table 6 = "Theory Comparison Across Eight Requirements" (line 880)

The scoring matrix will be numbered Table 6, not Table 5.

Additionally, "Table 1" (Operational Definitions) is rendered as manually bolded text (line 209: `\noindent\textbf{Table 1. ...}`) outside any `\begin{table}` environment, so LaTeX does not count it. This means the first auto-numbered table is "Table 1b," which LaTeX calls "Table 1" -- creating a naming collision: both the manual "Table 1" and the auto-numbered "Table 1" (which is actually Table 1b) will appear to readers as "Table 1."

**Fix:** Either put the Operational Definitions table inside a proper `\begin{table}` with `\caption{}`, or use `\label`/`\ref` throughout, or manually hard-code all table numbers. The current hybrid approach (some manual, some auto-numbered) guarantees mismatches.

---

## Minor Issues (should fix)

### M1. Bare-text citations (no `\cite` command)
Five author-year citations are typed as plain text instead of using natbib commands:

- **Line 125:** `Chalmers (1995, 1996) formulated...` -- should be `\citet{Chalmers1995,Chalmers1996}`
- **Line 133:** `Block (1995, 2007) further refined...` -- should be `\citet{Block1995,Block2007}`
- **Line 504:** `Tagliazucchi et al. (2012, 2016) showed...` -- should be `\citet{Tagliazucchi2012,Tagliazucchi2016}`
- **Line 504:** `Priesemann et al. (2013, 2014) characterized...` -- should be `\citet{Priesemann2013,Priesemann2014}`
- **Line 528:** `Priesemann et al. (2013, 2014) measured...` -- should be `\citet{Priesemann2013,Priesemann2014}`

These will not be hyperlinked, will not appear in the reference list's back-references (if enabled), and may format inconsistently with natbib-generated citations. Note: `Priesemann2013` exists in the bib file but is otherwise uncited -- the bare-text citations are the only references to it, so bibtex will not include it in the compiled bibliography.

### M2. Grammatical error in `\citet` usage
**Line 447:** `A note on \citet{Block1995} distinction` renders as "A note on Block (1995) distinction" -- missing the possessive. Should be `\citeauthor{Block1995}'s (\citeyear{Block1995}) distinction` or `\citet{Block1995}'s distinction` or a rephrasing like "A note on the distinction drawn by \citet{Block1995}."

### M3. Conclusion's open questions list doesn't match Section 9
**Line 1150:** "Open questions remain: the status of the implicit models (real or also virtual?), the need for mathematical formalization, the specific physical mechanism supporting criticality, and the minimum configuration for consciousness."

This lists 4 items. Section 9 contains 6 open questions:
1. Are all four models virtual?
2. Mathematical formalization
3. Physical implementation
4. ESM/EWM double dissociation (new, added in revision)
5. Multi-level substrate architecture
6. Decoding the virtual side

The conclusion omits OQ4, OQ5, and OQ6, and includes "the minimum configuration for consciousness," which does not correspond to any current OQ. This was likely an older OQ that was replaced or merged.

**Fix:** Update the conclusion's open questions list to match the actual Section 9 content.

### M4. 22 unused bibliography entries
The following bib keys are never cited in the paper:
`Aldrich1987`, `Alkire2000`, `Anton1899`, `Bola2020`, `Cybenko1989`, `DehaeneNaccache2011`, `Gazzaniga1962`, `Gazzaniga1965`, `Gilmore1992`, `Hornik1989`, `Lu1997`, `Monti2010`, `NatNeuro2025IIT`, `Nir2010`, `Phillips2021`, `Priesemann2013`, `Tegmark2000`, `Wada1949`, `Weiskrantz1986`, `Wigner1961`, `Zurek2003`, `vonNeumann1932`.

Most of these correspond to content that was removed in revisions (Clinical Dissociations section, split-brain discussion). `Priesemann2013` is referenced in bare-text citations (M1 above) but never via `\cite`, so bibtex will not find it.

Bibtex will silently ignore these, so they won't cause compilation errors, but they inflate the `.bib` file. If the paper is submitted to a journal that checks references, the mismatch will be flagged.

### M5. Split-brain discussion has no home in the body text
The revision comments (lines 806-809) confirm that split-brain content was "moved to §5.2." But Section 5.2 (Holographic Storage and the Patchwork Principle) discusses holographic storage in general -- the actual split-brain clinical discussion (Gazzaniga 2000, Pinto 2017, Wada test, left-hemisphere confabulation) exists only in:
- Revision comments (lines 806-809) -- not rendered
- Section 8.1 (line 978) -- empirical convergence evidence
- Section 6.4 animal consciousness table (line 840) -- as cloning evidence
- Section 4.2.2 (line 623) -- brief mention of confabulation

The abstract (line 44) and the software-like properties list (line 351) both promise a split-brain discussion, but the main clinical account was removed and not fully relocated. This leaves the "cloning" property asserted but not demonstrated in the body text.

### M6. Abstract mentions phenomena not fully treated in body
The abstract lists phenomena the theory "unifies": "psychedelic phenomenology, anesthetic mechanisms, dream states, split-brain phenomena, dissociative identity disorder, and animal consciousness." After revisions:
- Split-brain phenomena: no dedicated section (see M5)
- Anesthetic mechanisms: covered in Section 5.3 (Table 4) and Section 6.2 (Katlowitz), but the revision comment on line 773 says "propofol/ketamine trimmed to architecture reference"

This is borderline -- the coverage exists but is distributed and reduced.

---

## Cosmetic Issues (optional)

### O1. Inconsistent section reference formatting
The paper uses multiple formats for section references:
- `Section 3.4` (most common)
- `Section~3.7` (with non-breaking space, line 222, 230)
- `\S3.4` (line 547)
- `§6.2` (used only in revision comments/notes, lines 773, 794, etc.)

Within the rendered text, `Section X.Y`, `Section~X.Y`, and `\SX.Y` all appear. This is cosmetically inconsistent. The `~` prevents line breaks (good practice); `\S` produces the section symbol. Pick one convention.

### O2. Table 1 (Operational Definitions) formatting is inconsistent with other tables
Table 1 uses a `\begin{description}` environment with manual bold header ("Table 1. Operational Definitions...") and footnotes via `\textsuperscript{1/2/3}`. All other tables use proper `\begin{table}` + `\caption{}` environments. This means Table 1 won't appear in a List of Tables, can't be referenced with `\ref`, and its numbering collides with auto-numbered Table 1 (which is actually Table 1b).

### O3. Revision comment markers in comments
Lines 773, 794, 806, 853, 930, 976, 1081, 1129, 1133 contain `% [REVISION: ...]` comments. These are editorial notes that should be removed before final submission. They are invisible to readers in the PDF but visible in the source if shared.

### O4. Double-dash vs em-dash
The paper consistently uses `---` for em-dashes throughout (correct LaTeX convention). No issues found.

### O5. Keyword consistency
**Line 47:** Keywords include `\rev{self-referential closure}` (highlighted as revised). This is fine if intended -- it flags the keyword as newly added.

---

## Summary

| Severity | Count |
|----------|-------|
| Critical | 4 |
| Minor | 6 |
| Cosmetic | 5 |

The four critical issues all stem from the same root cause: section restructuring during revision left cross-references pointing to old section numbers. The most impactful is C4 (table numbering), which affects the scoring matrix -- one of the paper's most prominent elements. C1, C2, and C3 are straightforward find-and-replace fixes once the intended targets are confirmed.
