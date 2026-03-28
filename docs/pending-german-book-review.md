Action: present

# German Book Review — Resume at Chapter 5

**Review position:** Chapters 1–4 complete. Resume at **Kapitel 5: Am Rand des Chaos**.

**Workflow:**
1. Build fresh .docx: `python3 tmp/build_book_docx.py`
2. Copy to review file: `cp tmp/book-manuscript-de.docx tmp/book-review-de-vN.docx`
3. Open for user review
4. User edits inline (strikethrough=delete, yellow=rewrite, green=pattern to apply book-wide, direct text=accept)
5. Extract: formatting marks + full text diff against source .md
6. Apply edits, rebuild, open next version

**Extraction protocol:** See `~/cfg-agent-fleet/cross-project/inbox.md` → pending knowledge file `word-editing-extraction.md`. Three mark types: strikethrough, yellow highlight, direct text changes (diff-only, no formatting marks).

**Patterns already applied book-wide:**
- "erfährt/erfahren" (phenomenal experience) → "erlebt/erleben" or "spürt"
- `--` → `–` (en dash)
- nSKI → nAGI
- VMT → FMT
- Figures: German versions (.de.png)

**Build script:** `tmp/build_book_docx.py` — preprocesses `---` to `\newpage`, resolves figures from `pop-sci/` resource path.
