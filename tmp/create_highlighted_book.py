#!/usr/bin/env python3
"""
Create an HTML version of the book manuscript with changes from this session highlighted.
"""

import subprocess
import re
import html

def get_diff():
    """Get the git diff without color codes."""
    result = subprocess.run(
        ['git', 'diff', '--no-color', 'HEAD', '--', '/home/jeltz/aIware/pop-sci/book-manuscript.md'],
        capture_output=True,
        text=True,
        cwd='/home/jeltz/aIware'
    )
    return result.stdout

def parse_diff_for_additions(diff_text):
    """
    Parse the diff to extract the specific text that was added.
    Returns a list of added text snippets.
    """
    additions = []
    lines = diff_text.split('\n')

    for line in lines:
        if line.startswith('+') and not line.startswith('+++'):
            # Remove the leading '+' and keep the rest
            added_text = line[1:]
            if added_text.strip():  # Only keep non-empty lines
                additions.append(added_text)

    return additions

def read_manuscript():
    """Read the full manuscript."""
    with open('/home/jeltz/aIware/pop-sci/book-manuscript.md', 'r') as f:
        return f.read()

def markdown_to_html_simple(md_text, additions_set):
    """
    Convert markdown to HTML with simple formatting.
    Highlight any text that appears in the additions_set.
    """
    lines = md_text.split('\n')
    html_lines = []

    for line in lines:
        # Escape HTML in the line first
        escaped_line = html.escape(line)

        # Check if this line should be highlighted (it was added)
        should_highlight = line.strip() in additions_set

        # Convert markdown headings
        if line.startswith('####'):
            content = line[4:].strip()
            if should_highlight:
                html_lines.append(f'<h4><mark style="background-color: yellow">{html.escape(content)}</mark></h4>')
            else:
                html_lines.append(f'<h4>{html.escape(content)}</h4>')
        elif line.startswith('###'):
            content = line[3:].strip()
            if should_highlight:
                html_lines.append(f'<h3><mark style="background-color: yellow">{html.escape(content)}</mark></h3>')
            else:
                html_lines.append(f'<h3>{html.escape(content)}</h3>')
        elif line.startswith('##'):
            content = line[2:].strip()
            if should_highlight:
                html_lines.append(f'<h2><mark style="background-color: yellow">{html.escape(content)}</mark></h2>')
            else:
                html_lines.append(f'<h2>{html.escape(content)}</h2>')
        elif line.startswith('#'):
            content = line[1:].strip()
            if should_highlight:
                html_lines.append(f'<h1><mark style="background-color: yellow">{html.escape(content)}</mark></h1>')
            else:
                html_lines.append(f'<h1>{html.escape(content)}</h1>')
        elif line.strip() == '---':
            html_lines.append('<hr>')
        elif line.strip() == '':
            html_lines.append('<p>&nbsp;</p>')
        else:
            # Regular paragraph - apply bold and italic, then highlight if needed
            processed = escaped_line
            # Bold: **text** -> <strong>text</strong>
            processed = re.sub(r'\*\*([^\*]+)\*\*', r'<strong>\1</strong>', processed)
            # Italic: *text* -> <em>text</em>
            processed = re.sub(r'\*([^\*]+)\*', r'<em>\1</em>', processed)

            if should_highlight:
                html_lines.append(f'<p><mark style="background-color: yellow">{processed}</mark></p>')
            else:
                html_lines.append(f'<p>{processed}</p>')

    return '\n'.join(html_lines)

def create_html(content_html):
    """Create the full HTML document."""
    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Manuscript — Review Copy (changes highlighted)</title>
    <style>
        body {{
            font-family: 'Georgia', 'Times New Roman', serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 40px auto;
            padding: 0 20px;
            color: #333;
            background-color: #fafafa;
        }}
        h1 {{
            font-size: 2.5em;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            color: #222;
        }}
        h2 {{
            font-size: 2em;
            margin-top: 1.3em;
            margin-bottom: 0.4em;
            color: #333;
        }}
        h3 {{
            font-size: 1.5em;
            margin-top: 1.2em;
            margin-bottom: 0.3em;
            color: #444;
        }}
        h4 {{
            font-size: 1.2em;
            margin-top: 1em;
            margin-bottom: 0.3em;
            color: #555;
        }}
        p {{
            margin-bottom: 1em;
            text-align: justify;
        }}
        mark {{
            background-color: yellow;
            padding: 2px 0;
        }}
        hr {{
            border: none;
            border-top: 2px solid #ccc;
            margin: 2em 0;
        }}
        .title {{
            text-align: center;
            color: #c00;
            font-weight: bold;
            font-size: 1.3em;
            margin-bottom: 2em;
            padding: 10px;
            background-color: #ffe;
            border: 2px solid #cc0;
        }}
    </style>
</head>
<body>
    <div class="title">Book Manuscript — Review Copy (changes highlighted in yellow)</div>
    {content_html}
</body>
</html>"""
    return html_doc

def main():
    print("Getting git diff...")
    diff_text = get_diff()

    print("Parsing additions...")
    additions = parse_diff_for_additions(diff_text)
    additions_set = set(line.strip() for line in additions)

    print(f"Found {len(additions)} added lines")

    print("Reading manuscript...")
    manuscript = read_manuscript()

    print("Converting to HTML with highlighting...")
    content_html = markdown_to_html_simple(manuscript, additions_set)

    print("Creating final HTML document...")
    full_html = create_html(content_html)

    output_path = '/home/jeltz/aIware/tmp/book-review-highlighted.html'
    print(f"Writing to {output_path}...")
    with open(output_path, 'w') as f:
        f.write(full_html)

    print(f"✓ Created {output_path}")
    return output_path

if __name__ == '__main__':
    output = main()
    print(f"\nFile created at: {output}")
