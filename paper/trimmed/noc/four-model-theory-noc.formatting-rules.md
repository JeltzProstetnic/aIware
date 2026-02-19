# Formatting Rules for Trimmed Paper (Neuroscience of Consciousness)

Rules for .docx conversion. No LaTeX output for this paper.

## Target Journal Requirements

- **Journal**: Neuroscience of Consciousness
- **Format**: .docx (Microsoft Word) required
- **Body word limit**: 9,500 words
- **Abstract word limit**: 250 words

## Build Process

- **Build tool**: `pandoc`
- **Command**: `pandoc four-model-theory-noc.md -o four-model-theory-noc.docx`
- **Output**: Direct .md to .docx conversion (no intermediate .tex)

## HTML Preview Styling

- CSS file: `paper.css` (for browser preview during editing)
- Table styling:
  - Width: `100%`
  - Font size: `0.85em`
  - Cell padding: `6px 12px`

## Highlights

- Article highlights stored in separate file: `highlights.md`
- Highlights are required by journal (3-5 bullet points, ~85 chars each)

## Maintenance Notes

- **No .tex output** — this paper goes directly from .md to .docx
- HTML preview is for editing convenience only (not submitted)
- Build script not needed — simple pandoc command suffices
- **Known issue**: Footnote `[^quantum]` (von Neumann, Wigner, Zurek) renders in desktop Word but NOT in Office 365 Online. May need conversion to inline citation if reviewers flag it.
