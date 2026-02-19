#!/usr/bin/env python3
"""
Render the tracked-changes paper as HTML with proposed insertions highlighted.
Uses subprocess to call uvx markdown for conversion.
Two-pass: first highlight insertion markers, then convert full markdown to HTML.
"""

import re
import subprocess
import tempfile
import os

INPUT = '/home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md'
OUTPUT = '/home/jeltz/aIware/tmp/tracked-paper-review.html'

with open(INPUT, 'r') as f:
    text = f.read()

# Step 1: Extract proposed insertions, replace with placeholder tokens
insertions = []

def extract_insertion(m):
    idx = len(insertions)
    source = m.group(1).strip()
    rationale = m.group(2).strip() if m.group(2) else ""
    content = m.group(3).strip()
    insertions.append((source, rationale, content))
    return f'\n\n%%INSERTION_{idx}%%\n\n'

pattern = re.compile(
    r'<!-- \[PROPOSED INSERTION — ([^\]]+)\] -->\s*'
    r'(?:<!-- Rationale: ([^>]+?) -->\s*)?'
    r'(.*?)'
    r'<!-- \[END INSERTION\] -->',
    re.DOTALL
)

text = pattern.sub(extract_insertion, text)

# Step 2: Convert markdown to HTML via uvx
with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as tmp:
    tmp.write(text)
    tmp_path = tmp.name

try:
    result = subprocess.run(
        ['uvx', '--from', 'markdown', 'markdown_py',
         '-x', 'tables', '-x', 'footnotes', '-x', 'smarty',
         tmp_path],
        capture_output=True, text=True, check=True
    )
    html_body = result.stdout
finally:
    os.unlink(tmp_path)

# Step 3: Replace placeholder tokens with highlighted HTML blocks
for idx, (source, rationale, content) in enumerate(insertions):
    # Convert the insertion content markdown to HTML too
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            ['uvx', '--from', 'markdown', 'markdown_py',
             '-x', 'tables', '-x', 'footnotes', '-x', 'smarty',
             tmp_path],
            capture_output=True, text=True, check=True
        )
        content_html = result.stdout
    finally:
        os.unlink(tmp_path)

    meta_html = f'<div class="insertion-meta"><strong>PROPOSED INSERTION</strong> &mdash; {source}'
    if rationale:
        meta_html += f'<br><em>Rationale: {rationale}</em>'
    meta_html += '</div>'

    block = f'<div class="proposed-insertion">{meta_html}{content_html}</div>'
    html_body = html_body.replace(f'<p>%%INSERTION_{idx}%%</p>', block)
    # Fallback if it wasn't wrapped in <p>
    html_body = html_body.replace(f'%%INSERTION_{idx}%%', block)

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Four-Model Theory &mdash; Tracked Changes Review</title>
<style>
  body {{
    max-width: 820px;
    margin: 40px auto;
    padding: 0 24px;
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 16px;
    line-height: 1.75;
    color: #222;
    background: #fafafa;
  }}
  h1 {{ font-size: 1.8em; margin-top: 1.5em; }}
  h2 {{ font-size: 1.4em; margin-top: 2em; border-bottom: 1px solid #ccc; padding-bottom: 0.3em; }}
  h3 {{ font-size: 1.15em; margin-top: 1.5em; }}
  p {{ margin: 0.8em 0; text-align: justify; }}
  blockquote {{ border-left: 3px solid #999; margin: 1em 0; padding: 0.5em 1em; color: #555; }}
  table {{ border-collapse: collapse; margin: 1em 0; font-size: 0.9em; }}
  th, td {{ border: 1px solid #ccc; padding: 6px 10px; text-align: left; }}
  th {{ background: #eee; }}
  hr {{ border: none; border-top: 1px solid #ccc; margin: 2em 0; }}
  sup {{ font-size: 0.75em; }}
  ol, ul {{ margin: 0.5em 0; }}
  li {{ margin: 0.3em 0; }}

  /* Tracked changes highlighting */
  .proposed-insertion {{
    background: #e8f5e9;
    border-left: 5px solid #2e7d32;
    padding: 16px 20px;
    margin: 1.5em 0;
    border-radius: 6px;
    position: relative;
    box-shadow: 0 1px 4px rgba(0,0,0,0.08);
  }}
  .proposed-insertion::before {{
    content: "NEW";
    position: absolute;
    top: -11px;
    right: 14px;
    background: #2e7d32;
    color: white;
    font-size: 0.7em;
    font-weight: bold;
    padding: 2px 10px;
    border-radius: 3px;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    letter-spacing: 0.5px;
  }}
  .insertion-meta {{
    background: #c8e6c9;
    padding: 10px 14px;
    margin: -16px -20px 14px -20px;
    border-radius: 6px 6px 0 0;
    font-size: 0.82em;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    color: #1b5e20;
    border-bottom: 1px solid #a5d6a7;
  }}
  .insertion-meta em {{ color: #2e7d32; }}

  /* Navigation */
  .nav-bar {{
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: #2e7d32;
    color: white;
    padding: 8px 20px;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.85em;
    z-index: 100;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  }}
  .nav-bar a {{
    color: white;
    text-decoration: none;
    background: rgba(255,255,255,0.15);
    padding: 4px 12px;
    border-radius: 4px;
    font-weight: 500;
  }}
  .nav-bar a:hover {{ background: rgba(255,255,255,0.3); }}
  .nav-bar .title {{ font-weight: bold; margin-right: auto; }}

  body {{ padding-top: 50px; }}

  /* Print styles */
  @media print {{
    body {{ max-width: none; margin: 0; padding: 20px; }}
    .proposed-insertion {{ break-inside: avoid; }}
    .nav-bar {{ display: none; }}
  }}
</style>
</head>
<body>

<div class="nav-bar">
  <span class="title">Tracked Changes Review</span>
  <a href="#insertion-0">1: Identity/H&#x2082;O</a>
  <a href="#insertion-1">2: Must Feel</a>
  <a href="#insertion-2">3: Digital Twin</a>
  <a href="#insertion-3">4: Developmental</a>
</div>

{html_body}

</body>
</html>
'''

# Add anchor IDs to insertion blocks
for idx in range(len(insertions)):
    html = html.replace(
        f'<div class="proposed-insertion">',
        f'<div class="proposed-insertion" id="insertion-{idx}">',
        1  # only first occurrence each time
    )

with open(OUTPUT, 'w') as f:
    f.write(html)

print(f"Written to: {OUTPUT}")
print(f"Size: {len(html):,} bytes")
print(f"Insertions highlighted: {len(insertions)}")
