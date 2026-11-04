# Formatting Rules for FMT Formalization Paper

Rules for pandoc-based PDF generation with Unicode math support.

## Build Process

- **Build tool**: `pandoc`
- **Command**: `pandoc -f markdown+autolink_bare_uris fmt-formalization.md -H unicode-header.tex --pdf-engine=pdflatex -o fmt-formalization.pdf` — the `autolink_bare_uris` extension turns the bare DOI URLs into `\url{}` so `xurl` (in the header) can break them; without it three reference-list DOIs overflow by up to 40pt (measured S324).
- **Unicode header**: `unicode-header.tex` provides LaTeX mappings for Unicode math symbols

## Unicode Support (via unicode-header.tex)

### Greek Letters (Uppercase)

- Δ Π Σ Φ Λ Ω

### Greek Letters (Lowercase)

- α γ η θ κ λ μ ν π ρ σ τ

### Math Operators

- ∂ (partial derivative)
- ∈ ∉ (set membership)
- ∀ ∃ (quantifiers)
- ∧ ∨ (logical operators)
- ≈ ≠ ≤ ≥ (comparisons)
- × · (multiplication)

### Arrows

- → ↔ ↦ ⇒

### Subscripts and Superscripts

- Unicode subscripts and superscripts mapped to LaTeX equivalents

## LaTeX Packages (in unicode-header.tex)

- `newunicodechar` — defines Unicode-to-LaTeX mappings
- `amssymb`, `amsmath` — mathematical symbols and environments
- `textcomp` — text companion fonts
- `fontenc[T1]` — font encoding
- `inputenc[utf8]` — input encoding

## Typography

- Typographic dashes configured for proper en-dash and em-dash rendering

## Maintenance Notes

- **unicode-header.tex is required** — build will fail without it
- All Unicode math symbols in the .md must have corresponding mappings in unicode-header.tex
- If new Unicode symbols are added to the .md, update unicode-header.tex accordingly
