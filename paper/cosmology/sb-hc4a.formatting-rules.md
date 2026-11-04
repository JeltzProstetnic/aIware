# Formatting Rules for Cosmology Paper (SB-HC4A)

Rules for pandoc-based PDF generation.

## Build Process

- **Build tool**: `pandoc`
- **Build command**: `pandoc sb-hc4a.md -H unicode-header.tex --pdf-engine=pdflatex -o sb-hc4a.pdf`
- **Unicode header**: `unicode-header.tex` — PRESENT (copied from `paper/fmt_formal/`, Session 73)

## Unicode Characters Used

Audited Session 73. The paper uses: Φ (×10), × (×2), λ, μ, σ, τ, Λ, Ω, ² (×2), ³ (×2), ¹, ⁵ (×3), ⁻ (×3), → (×18), ↔, − (×5), ∞, ö (×6), – (×42), — (×171). All covered by `unicode-header.tex`.

## Maintenance Notes

- `unicode-header.tex` is shared with `paper/fmt_formal/`. If new symbols are added to the paper, check the header covers them.
- The `ö` character (in German titles like "Köper") is handled by `inputenc` utf8, not `newunicodechar`.
