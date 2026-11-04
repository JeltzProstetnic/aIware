# Formatting Rules for Cosmology Formalization Paper (SB-HC4A Formalization)

Rules for pandoc-based PDF generation.

## Build Process

- **Build tool**: `pandoc`
- **Build command**: `pandoc sb-hc4a-formalization.md -H unicode-header.tex --pdf-engine=pdflatex -o sb-hc4a-formalization.pdf`
- **Unicode header**: `unicode-header.tex` — PRESENT (shared with `paper/cosmology/`)

## Unicode Characters Used

The formalization paper uses significantly more mathematical Unicode than Paper 3, including:

**Greek letters**: Φ, Λ, Ω, λ, μ, σ, τ, ρ, ψ, θ, α, β, γ, δ, ε, ζ, η

**Set theory & logic symbols**: ∈, ∉, ⊆, ⊂, ∪, ∩, ∅, ∨, ∧, ¬, ∀, ∃, ⟹, ⟺, →, ↔, ⇒, ⇔

**Mathematical operators**: ×, ÷, ≤, ≥, ≠, ≈, ∝, ∫, ∑, ∏, √, ∞, − (minus)

**Superscripts & subscripts**: ², ³, ⁴, ⁵, ¹, ⁻

**Special characters**: – (en-dash, ×42 approx), — (em-dash, ×171 approx), • (bullet)

All symbols are covered by the shared `unicode-header.tex` file located at `/home/jeltz/aIware/paper/cosmology_formal/unicode-header.tex`.

## Maintenance Notes

- `unicode-header.tex` is shared with `paper/cosmology/`. If new mathematical or logical symbols are added to the formalization paper, verify that `unicode-header.tex` covers them before building.
- The `ö` character (in German terms or references) is handled by `inputenc` utf8, not `newunicodechar`.
- Because the formalization paper is symbol-dense, ensure all Greek letters, set theory operators, and logic symbols used are explicitly defined in the unicode header.
