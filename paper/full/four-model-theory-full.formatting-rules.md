# Formatting Rules for Full Four-Model Theory Paper

Rules for LaTeX output generation. Build script TBD (currently hand-maintained .tex).

## Document Class and Packages

- Document class: `\documentclass[12pt]{article}`
- Font: `lmodern` package
- Margins: 1in on all sides (`geometry` package)
- Line spacing: `onehalfspacing` (`setspace` package)
- Bibliography: `natbib` with `round` option
- Hyperlinks: `blue!60!black` color scheme (`hyperref` package)
- Additional packages: `amsmath`, `amssymb`, `graphicx`, `booktabs`, `tabularx`, `xcolor`, `microtype`, `parskip`

## Title Page

- Title: Line break after colon using `\\`
  - Example: `Four-Model Theory of Consciousness:\\[0.2cm] An Architecturally-Grounded Framework`
- Author block:
  - Name followed by `\textit{Independent researcher}`
  - ORCID: hyperlinked using `\href{https://orcid.org/0009-0005-9697-1665}{ORCID: 0009-0005-9697-1665}`
  - Email: `\texttt{matthias@matthiasgruber.com}` (plain or hyperlinked with `\href{mailto:...}`)
- Date: suppressed with `\date{}`

## Abstract

- Single-spaced (use `singlespacing` environment if document is onehalfspaced)
- Keywords line follows abstract with no page break

## Tables

- Array stretch: `\renewcommand{\arraystretch}{1.4}`
- Float placement: `table[htbp]`
- Font size: `\small` inside table environment
- Rules: `booktabs` package (`\toprule`, `\midrule`, `\bottomrule`)
- Column types: Use `tabularx` for width-controlled tables with `X` columns

## Figures

- Figures located in `biorxiv/` subdirectory relative to .tex file
- Standard `figure[htbp]` float placement
- Include graphics with `\includegraphics[width=...]{biorxiv/filename.png}`

## Maintenance Notes

- **CRITICAL**: No build script exists yet. The .tex file at `paper/full/biorxiv/paper.tex` is currently hand-maintained.
- When build script is created, it must implement ALL rules listed above.
- Any future formatting changes must be documented here AND implemented in the build script in the same session.
