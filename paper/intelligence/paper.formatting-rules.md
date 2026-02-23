# Formatting Rules for Intelligence Paper

Rules for LaTeX output generation. Build script TBD (currently no .tex output).

## Document Class and Packages

- Document class: `\documentclass[12pt,a4paper]{article}`
- Font: `mathpazo` package (Palatino)
- Margins: 1in on all sides (`geometry` package)
- Line spacing: `onehalfspacing` (`setspace` package)
- Bibliography: `natbib` with default citation style
- Hyperlinks: `blue` color scheme (`hyperref` package)
- Additional packages: `enumitem`, `url`

## Title Page

- Title: Line break after colon using `\\`
  - Example: `Intelligence as Computational Architecture:\\[0.2cm] A Four-Model Framework`
- Author block:
  - Name
  - Affiliations in `\small` font below name
  - ORCID: plain text (not hyperlinked) — `ORCID: 0009-0005-9697-1665`
- Keywords: `\medskip` spacing before keywords line

## Target Journal

- **Journal**: New Ideas in Psychology
- **Word limit**: 7,500 words (body text)
- **Format**: .docx required (double-spaced)
- **Citation style**: APA 7th edition
- **Highlights**: 3-5 article highlights required (~85 characters each)

## Em Dash Line Breaking
- All em dashes (`---`) are followed by `\hspace{0pt}` to allow line breaks after them
- Without this, LaTeX sometimes produces overfull lines (e.g., "interventions---environments" overshot by 18pt)
- Implemented in build script's `_convert_inline()` function

## Maintenance Notes

- **No build script exists yet** — paper.md has not been converted to .tex
- When build script is created, it must implement all rules listed above
- Final submission requires .docx conversion (pandoc .md → .docx or .tex → .docx)
- Any future formatting changes must be documented here AND implemented in the build script in the same session
