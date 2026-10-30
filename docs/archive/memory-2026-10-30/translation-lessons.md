# Translation Lessons — Session 90

## Chunk Size Limits for Parallel Agents
- **Max ~300 lines / ~7,000 words per agent** for translation/rewrite tasks. Beyond that, the Write tool call exceeds the 32,000 output token limit.
- The original chunk 09 (626 lines) failed TWICE on token limits. Split into 09a (311 lines) + 09b (313 lines) — both succeeded.
- Same pattern: translation chunk 09 also hit token limits and needed splitting.
- **Rule of thumb**: Keep chunks under 350 lines for tasks that write full file content.
- **NEVER use just 8 chunks for a full manuscript** — the last chunk always ends up too large and gets stuck. Use 10 chunks with chapter-boundary splitting.
- Session 91: Re-split from 8 to 10 chunks for Sie→man pass. Largest chunk: 7,436 words (was 13,516 before split).

## German Translation Workflow
1. **Parallel chunked translation** works well — 10 chunks, shared glossary, consistent results
2. **Terminology glossary is essential** — include in every agent prompt for consistency
3. **Title/style decisions FIRST** — decide title, address form, tone before launching agents
4. **Address form matters hugely in German**:
   - "du" = too informal for published non-fiction
   - "Sie" = formal but still direct address
   - "man"/impersonal = best for German pop-sci (user preference)
   - Decision: use "man" and impersonal constructions, avoid direct address except where essential

## Cover Image Gotcha
- `cover-wrap.jpg` and `cover-front.jpg` are just the **bare artwork** (background image)
- The actual cover with title, author, blurb, ISBN is in the **PDF** (`cover-wrap.pdf`)
- Must render PDF→JPG via PyMuPDF to get the real cover: `fitz.open() → page.get_pixmap(matrix=300/72) → save()`
- Result: `cover-wrap-render.jpg`

## Push Script Glob Patterns
- `git rm --cached` with unquoted glob works for pathspec patterns
- Use separate PRIVATE_GLOBS array with unquoted `$glob` in the loop (no quotes around `$glob`)
- This correctly excludes `pop-sci/book-manuscript*` (all variants: .md, .pdf, .epub, .tex, etc.)
