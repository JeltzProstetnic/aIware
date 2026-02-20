# Formatting Rules for Book Manuscript

Rules collected during editing sessions. Consumed by `tmp/build_book_pdf.py`.
All rules listed here are already implemented in the build script.

## Trim Size & Margins (POD)

- Trim: 6" × 9" (US Trade paperback)
- Inner margin (gutter): 0.875" — sized for ~250-page binding
- Outer margin: 0.75"
- Top margin: 0.75"
- Bottom margin: 0.75"
- Text block: ~4.375" × 7.5"
- Two-sided printing (`twoside`), chapters start on recto (`openright`)

## Typography

- Font: Palatino 11pt
- Line spacing: `\setstretch{1.15}` (standard book leading)
- Paragraph style: indented first line, no inter-paragraph space (LaTeX default)
- Microtype enabled for better justification

## Front Matter (Roman Numerals)

Order:
1. Half-title page (recto) — title only, no subtitle, `\pagestyle{empty}`
2. Blank verso
3. Full title page (recto) — title, subtitle, author, `\pagestyle{empty}`
4. Copyright page (verso) — © 2026 Matthias Gruber, ARR, ISBN [TBD]
5. Dedication page (recto) — italic, centered, `\pagestyle{empty}`
6. Blank verso
7. Table of contents — `\pagestyle{plain}` (page numbers only)
8. Preface — `\chapter*`, `\pagestyle{plain}`
9. About the Author — `\chapter*`, `\pagestyle{plain}`

## Main Matter (Arabic, Starting at Page 1)

- `\mainmatter` inserted before Chapter 1
- `\pagestyle{fancy}` with running headers
- Chapters 1–16 as numbered `\chapter{}`
- Coda as `\chapter*` (unnumbered, with TOC entry)

## Back Matter

- `\backmatter` inserted before Acknowledgments
- Acknowledgments, Notes and References as `\chapter*`
- Appendices A–E as `\chapter*` (with "Appendix X:" in title)
- All with TOC entries via `\addcontentsline`
- `\markboth` set for correct running headers

## Title Page

- Main title: `\Huge\bfseries`, line break after "Simulation" → `The Simulation\\[0.3cm] You Call "I"`
- Subtitle: `\Large`, line break after "Architecture of" → `The Architecture of\\[0.2cm] Consciousness, Computation, and the Cosmos`
- Author: `\large Matthias Gruber` (not italic on full title page)
- Half-title: title only, `\vspace*{3in}` before
- Full title: `\vspace*{2in}` before, `\vspace{0.8cm}` title→subtitle, `\vspace{2cm}` subtitle→author

## Headers / Running Heads

- Left-even (verso): `\small\itshape The Simulation You Call "I"`
- Right-odd (recto): `\small\itshape\leftmark` (current chapter name)
- Header rule: 0.4pt
- Front matter: `\pagestyle{plain}` (no running heads, just page numbers)
- Main matter: `\pagestyle{fancy}` (running heads + page numbers)
- Chapter start pages: `\pagestyle{plain}` (automatic)

## Blank Pages

- Blank pages from `\cleardoublepage` are truly blank (no headers, no page numbers)
- Custom `\cleardoublepage` redefinition ensures `\thispagestyle{empty}`

## Chapter Formatting

- Chapter title: `\huge\bfseries` for number line, `\Huge` for chapter name
- Unnumbered chapters: same size, no number prefix
- Chapter spacing: 50pt before, 40pt after (more generous than draft)

## Block Quotes

- Indented 1.5em left and right
- Italic body text (`\itshape`)

## Epigraphs (> blockquotes at chapter start)

- `\vspace*{2cm}` before epigraph
- `\vspace{1cm}` after epigraph (before chapter body)

## Tables

- Standard LaTeX tabularx with `\\` row separators
- Header row converted from markdown `|` syntax
- All tables use `\small` font size (consistent across all tables)
- 4pt extra vertical spacing between data rows for readability

## Section Title Line Breaks

- "Why Your Brain Has the Capacity for Self-Modeling" → line break after "Capacity" to avoid right-margin overflow

### Visual Processing Hierarchy Table (Appendix A) — Two-Page Spread

The 5-column Brodmann area table is too dense for a single page (even landscape).
Split across two facing portrait pages:
- **Left page (verso)**: Area, Brodmann area, Receptive field, Normal function
- **Right page (recto)**: Area, Psychedelic signature
- Area column repeated on both pages for easy cross-reference
- Both pages use `\footnotesize` for comfortable fit
- Force onto even page first (verso/left), so the spread is visible when the book is open
- Notes follow after the right-page table

## Links

- All links hidden for print (`hidelinks`) — no colored text, no boxes
- URLs remain clickable in digital PDF but invisible in print

## Copyright Page

- © 2026 Matthias Gruber. All rights reserved.
- ISBN: [TBD]
- First edition, 2026
- www.matthiasgruber.com
