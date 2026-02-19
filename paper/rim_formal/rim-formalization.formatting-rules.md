# Formatting Rules for RIM Formalization Paper

Rules for pandoc-based PDF generation with Unicode math support. Extends Paper 4 (FMT) mappings.

## Build Process

- **Build tool**: `pandoc`
- **Command**: `pandoc rim-formalization.md -H unicode-header.tex --pdf-engine=pdflatex -o rim-formalization.pdf`
- **Unicode header**: `unicode-header.tex` provides LaTeX mappings for Unicode math symbols

## Unicode Support (via unicode-header.tex)

### Greek Letters (Uppercase)

- Δ Π Σ Φ Λ Ω

### Greek Letters (Lowercase)

- α β γ δ η θ κ λ μ ν ω π ρ σ τ
- **Additional beyond Paper 4**: β δ ω

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
- Shares most mappings with Paper 4 (FMT) but includes additional Greek letters β δ ω
- If new Unicode symbols are added to the .md, update unicode-header.tex accordingly
