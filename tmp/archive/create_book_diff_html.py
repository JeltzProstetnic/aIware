#!/usr/bin/env python3
"""
Generate an HTML file showing inline diffs between the original and edited book manuscript.
Uses git to get the original, difflib for computing word-level diffs.
"""

import subprocess
import difflib
import re
import html as html_escape
from datetime import datetime

INPUT_FILE = 'pop-sci/book-manuscript.md'
OUTPUT_FILE = '/home/jeltz/aIware/tmp/book-review-applied-changes.html'

# Get original content from git
print("Fetching original from git...")
result = subprocess.run(
    ['git', 'show', f'HEAD:{INPUT_FILE}'],
    capture_output=True,
    text=True,
    cwd='/home/jeltz/aIware'
)

if result.returncode != 0:
    print(f"Error: Could not get original file from git: {result.stderr}")
    exit(1)

original = result.stdout

# Get current content
print("Reading current file...")
with open(f'/home/jeltz/aIware/{INPUT_FILE}', 'r') as f:
    current = f.read()

# Split into lines for processing
original_lines = original.splitlines()
current_lines = current.splitlines()

# Compute line-level diff
print("Computing diff...")
matcher = difflib.SequenceMatcher(None, original_lines, current_lines)

def render_line(line, idx=0):
    """Render a single line with basic markdown formatting."""
    if not line.strip():
        return '<p>&nbsp;</p>'

    # Chapter headings
    if line.startswith('## '):
        anchor = f'chapter-{idx}'
        return f'<h2 id="{anchor}">{html_escape.escape(line[3:])}</h2>'

    # Other headings
    if line.startswith('### '):
        return f'<h3>{html_escape.escape(line[4:])}</h3>'
    if line.startswith('#### '):
        return f'<h4>{html_escape.escape(line[5:])}</h4>'
    if line.startswith('# '):
        return f'<h1>{html_escape.escape(line[2:])}</h1>'

    # Regular paragraph
    formatted = format_markdown_line(line)
    return f'<p>{formatted}</p>'

def format_markdown_line(line):
    """Apply basic markdown formatting (bold, italic, code)."""
    text = html_escape.escape(line)

    # Bold: **text** or __text__
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', text)

    # Italic: *text* or _text_
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'_(.+?)_', r'<em>\1</em>', text)

    # Code: `text`
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)

    return text

# Extract chapter headings for navigation
chapter_pattern = re.compile(r'^##\s+(.+)$')
chapters = []
for i, line in enumerate(current_lines):
    match = chapter_pattern.match(line)
    if match:
        chapters.append((i, match.group(1).strip()))

# Build the HTML with diff highlighting
html_parts = []
change_count = 0

for tag, i1, i2, j1, j2 in matcher.get_opcodes():
    if tag == 'equal':
        for idx, line in enumerate(current_lines[j1:j2]):
            html_parts.append(render_line(line, j1 + idx))

    elif tag == 'replace':
        change_count += 1
        html_parts.append(f'<div class="change-block" id="change-{change_count}">')

        old_text = ' '.join(original_lines[i1:i2])
        new_text = ' '.join(current_lines[j1:j2])

        old_words = old_text.split()
        new_words = new_text.split()

        word_matcher = difflib.SequenceMatcher(None, old_words, new_words)
        diff_html = []

        for wtag, wi1, wi2, wj1, wj2 in word_matcher.get_opcodes():
            if wtag == 'equal':
                diff_html.append(html_escape.escape(' '.join(new_words[wj1:wj2])))
            elif wtag == 'delete':
                deleted = html_escape.escape(' '.join(old_words[wi1:wi2]))
                diff_html.append(f'<span class="deletion">{deleted}</span>')
            elif wtag == 'insert':
                inserted = html_escape.escape(' '.join(new_words[wj1:wj2]))
                diff_html.append(f'<span class="insertion">{inserted}</span>')
            elif wtag == 'replace':
                deleted = html_escape.escape(' '.join(old_words[wi1:wi2]))
                inserted = html_escape.escape(' '.join(new_words[wj1:wj2]))
                diff_html.append(f'<span class="deletion">{deleted}</span> <span class="insertion">{inserted}</span>')

            if wtag != 'equal':
                diff_html.append(' ')

        html_parts.append('<p class="diff-para">' + ''.join(diff_html).strip() + '</p>')
        html_parts.append('</div>')

    elif tag == 'delete':
        change_count += 1
        html_parts.append(f'<div class="change-block" id="change-{change_count}">')
        deleted_lines = [format_markdown_line(l) for l in original_lines[i1:i2]]
        html_parts.append(f'<p class="diff-para"><span class="deletion">{" ".join(deleted_lines)}</span></p>')
        html_parts.append('</div>')

    elif tag == 'insert':
        change_count += 1
        html_parts.append(f'<div class="change-block" id="change-{change_count}">')
        for line in current_lines[j1:j2]:
            formatted = format_markdown_line(line)
            html_parts.append(f'<p class="diff-para"><span class="insertion">{formatted}</span></p>')
        html_parts.append('</div>')

# Build chapter navigation links
chapter_nav = []
for idx, title in chapters[:15]:  # Limit to first 15 chapters for nav bar
    short_title = title[:25] + '...' if len(title) > 25 else title
    chapter_nav.append(f'<a href="#chapter-{idx}">{html_escape.escape(short_title)}</a>')

# Generate final HTML
now = datetime.now().strftime('%Y-%m-%d %H:%M')

html_output = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Book Manuscript — Applied Changes Review</title>
<style>
  body {{
    max-width: 900px;
    margin: 40px auto;
    padding: 0 24px;
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 16px;
    line-height: 1.75;
    color: #222;
    background: white;
  }}

  h1 {{ font-size: 2em; margin-top: 1.5em; }}
  h2 {{ font-size: 1.6em; margin-top: 2em; border-bottom: 2px solid #ddd; padding-bottom: 0.3em; }}
  h3 {{ font-size: 1.3em; margin-top: 1.5em; }}
  h4 {{ font-size: 1.1em; margin-top: 1.2em; }}

  p {{ margin: 0.8em 0; text-align: justify; }}

  code {{ background: #f5f5f5; padding: 2px 5px; border-radius: 3px; font-family: monospace; }}

  /* Navigation bar */
  .nav-bar {{
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: #1565c0;
    color: white;
    padding: 10px 20px;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.85em;
    z-index: 100;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  }}

  .nav-bar .title {{
    font-weight: bold;
    font-size: 1.1em;
    margin-bottom: 6px;
    display: block;
  }}

  .nav-bar .subtitle {{
    font-size: 0.9em;
    opacity: 0.9;
    margin-bottom: 10px;
    display: block;
  }}

  .nav-controls {{
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 8px;
  }}

  .nav-bar button {{
    color: white;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.3);
    padding: 5px 14px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.95em;
    font-weight: 500;
  }}

  .nav-bar button:hover {{
    background: rgba(255,255,255,0.3);
  }}

  .nav-bar a {{
    color: white;
    text-decoration: none;
    background: rgba(255,255,255,0.15);
    padding: 4px 10px;
    border-radius: 4px;
    font-size: 0.9em;
  }}

  .nav-bar a:hover {{
    background: rgba(255,255,255,0.3);
  }}

  body {{ padding-top: 160px; }}

  /* Change highlighting */
  .change-block {{
    margin: 1.2em 0;
    padding: 12px 16px;
    border-left: 4px solid #ff9800;
    background: #fff8e1;
    border-radius: 4px;
  }}

  .diff-para {{
    margin: 0.5em 0;
  }}

  .deletion {{
    background: #ffcccc;
    text-decoration: line-through;
    padding: 2px 4px;
    border-radius: 3px;
    color: #c62828;
  }}

  .insertion {{
    background: #ccffcc;
    padding: 2px 4px;
    border-radius: 3px;
    color: #2e7d32;
    font-weight: 500;
  }}

  /* Print styles */
  @media print {{
    body {{ max-width: none; margin: 0; padding: 20px; padding-top: 20px; }}
    .nav-bar {{ display: none; }}
    .change-block {{ break-inside: avoid; }}
  }}
</style>
</head>
<body>

<div class="nav-bar">
  <span class="title">Book Manuscript — Applied Changes Review</span>
  <span class="subtitle">Generated: {now} | Total changes: {change_count}</span>

  <div class="nav-controls">
    <button onclick="jumpToChange(-1)">← Previous Change</button>
    <button onclick="jumpToChange(1)">Next Change →</button>
    <span style="margin: 0 10px;">|</span>
    {' '.join(chapter_nav[:8])}
  </div>
</div>

{''.join(html_parts)}

<script>
let currentChangeIndex = 0;
const totalChanges = {change_count};

function jumpToChange(direction) {{
  currentChangeIndex += direction;

  if (currentChangeIndex < 1) currentChangeIndex = 1;
  if (currentChangeIndex > totalChanges) currentChangeIndex = totalChanges;

  const target = document.getElementById('change-' + currentChangeIndex);
  if (target) {{
    target.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
    target.style.boxShadow = '0 0 10px rgba(255, 152, 0, 0.5)';
    setTimeout(() => {{
      target.style.boxShadow = '';
    }}, 1500);
  }}
}}

// Keyboard navigation
document.addEventListener('keydown', (e) => {{
  if (e.key === 'n' || e.key === 'ArrowDown') {{
    jumpToChange(1);
    e.preventDefault();
  }} else if (e.key === 'p' || e.key === 'ArrowUp') {{
    jumpToChange(-1);
    e.preventDefault();
  }}
}});
</script>

</body>
</html>
'''

# Write output
print("Writing HTML...")
with open(OUTPUT_FILE, 'w') as f:
    f.write(html_output)

print(f"\nSuccess!")
print(f"Output: {OUTPUT_FILE}")
print(f"Size: {len(html_output):,} bytes")
print(f"Changes detected: {change_count}")
print(f"Chapters found: {len(chapters)}")
print(f"\nKeyboard shortcuts: 'n' or Down arrow for next change, 'p' or Up arrow for previous")
