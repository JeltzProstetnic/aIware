# Formatting Rules for Book Manuscript

Rules collected during editing sessions. Consumed by `tmp/build_book_pdf.py`.
All rules listed here are already implemented in the build script.

## Title Page

- Main title: `\Huge\bfseries`, line break after "Simulation" → `The Simulation\\[0.3cm] You Call "I"`
- Subtitle: `\Large`, line break after "Architecture of" → `The Architecture of\\[0.2cm] Consciousness, Computation, and the Cosmos`
- Author: `\large\itshape Matthias Gruber`
- Date line: `\small Draft manuscript --- \today`
- Spacing: `\vspace*{3cm}` before title, `\vspace{1cm}` between title and subtitle, `\vspace{2cm}` between subtitle and author

## Headers / Running Heads

- Left-even: `\small\itshape The Simulation You Call "I"`
- Right-odd: `\small\itshape\leftmark` (current chapter name)

## Chapter Formatting

- Chapter title: `\huge\bfseries` for numbered, `\Huge` for chapter name
- Unnumbered chapters: same size, no number prefix

## Block Quotes

- Indented 1.5em left and right
- Italic body text (`\itshape`)

## Epigraphs (> blockquotes at chapter start)

- `\vspace*{2cm}` before epigraph
- `\vspace{1cm}` after epigraph (before chapter body)

## Tables

- Standard LaTeX tabular with `\\` row separators
- Header row converted from markdown `|` syntax
