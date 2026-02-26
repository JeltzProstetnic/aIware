#!/usr/bin/env python3
"""Generate side-by-side HTML comparison of original vs generated .tex files."""

import html
import os
import difflib

REPO_ROOT = "/home/jeltz/aIware"

PAIRS = [
    {
        "name": "FMT Full Paper",
        "original": os.path.join(REPO_ROOT, "tmp/fmt-paper-ORIGINAL.tex"),
        "generated": os.path.join(REPO_ROOT, "tmp/fmt-paper-GENERATED.tex"),
        "output": os.path.join(REPO_ROOT, "tmp/comparison-fmt.html"),
    },
    {
        "name": "Intelligence Paper",
        "original": os.path.join(REPO_ROOT, "tmp/intel-paper-ORIGINAL.tex"),
        "generated": os.path.join(REPO_ROOT, "tmp/intel-paper-GENERATED.tex"),
        "output": os.path.join(REPO_ROOT, "tmp/comparison-intel.html"),
    },
]


def generate_side_by_side_html(name, orig_path, gen_path):
    """Generate HTML with side-by-side diff of two files."""
    with open(orig_path) as f:
        orig_lines = f.readlines()
    with open(gen_path) as f:
        gen_lines = f.readlines()

    # Generate diff
    differ = difflib.unified_diff(orig_lines, gen_lines,
                                   fromfile="ORIGINAL (hand-maintained)",
                                   tofile="GENERATED (build script)",
                                   lineterm="")

    # Also generate side-by-side
    matcher = difflib.SequenceMatcher(None, orig_lines, gen_lines)

    # Stats
    total_orig = len(orig_lines)
    total_gen = len(gen_lines)
    matching = sum(b[2] for b in matcher.get_matching_blocks())
    similarity = matcher.ratio() * 100

    # Build HTML
    rows = []
    row_num = 0

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                row_num += 1
                line = html.escape(orig_lines[i1 + k].rstrip())
                rows.append(f'''<tr class="equal">
                    <td class="linenum">{i1+k+1}</td>
                    <td class="code">{line}</td>
                    <td class="linenum">{j1+k+1}</td>
                    <td class="code">{line}</td>
                </tr>''')
        elif tag == "replace":
            max_len = max(i2 - i1, j2 - j1)
            for k in range(max_len):
                row_num += 1
                if i1 + k < i2:
                    left_num = i1 + k + 1
                    left = html.escape(orig_lines[i1 + k].rstrip())
                else:
                    left_num = ""
                    left = ""
                if j1 + k < j2:
                    right_num = j1 + k + 1
                    right = html.escape(gen_lines[j1 + k].rstrip())
                else:
                    right_num = ""
                    right = ""
                rows.append(f'''<tr class="changed">
                    <td class="linenum">{left_num}</td>
                    <td class="code left-changed">{left}</td>
                    <td class="linenum">{right_num}</td>
                    <td class="code right-changed">{right}</td>
                </tr>''')
        elif tag == "delete":
            for k in range(i2 - i1):
                row_num += 1
                left = html.escape(orig_lines[i1 + k].rstrip())
                rows.append(f'''<tr class="deleted">
                    <td class="linenum">{i1+k+1}</td>
                    <td class="code left-deleted">{left}</td>
                    <td class="linenum"></td>
                    <td class="code"></td>
                </tr>''')
        elif tag == "insert":
            for k in range(j2 - j1):
                row_num += 1
                right = html.escape(gen_lines[j1 + k].rstrip())
                rows.append(f'''<tr class="inserted">
                    <td class="linenum"></td>
                    <td class="code"></td>
                    <td class="linenum">{j1+k+1}</td>
                    <td class="code right-inserted">{right}</td>
                </tr>''')

    table_html = "\n".join(rows)

    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Comparison: {html.escape(name)}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Consolas', 'Monaco', monospace; font-size: 12px; background: #1e1e1e; color: #d4d4d4; }}
        .header {{ background: #252526; padding: 12px 20px; border-bottom: 1px solid #404040; position: sticky; top: 0; z-index: 10; }}
        .header h1 {{ font-size: 16px; color: #cccccc; margin-bottom: 6px; }}
        .stats {{ color: #808080; font-size: 13px; }}
        .stats .good {{ color: #4ec9b0; }}
        .stats .warn {{ color: #dcdcaa; }}
        .stats .bad {{ color: #f44747; }}
        table {{ width: 100%; border-collapse: collapse; table-layout: fixed; }}
        td {{ padding: 1px 8px; vertical-align: top; white-space: pre-wrap; word-break: break-all; }}
        td.linenum {{ width: 40px; min-width: 40px; max-width: 40px; text-align: right; color: #606060; padding-right: 8px; border-right: 1px solid #333; user-select: none; }}
        td.code {{ width: calc(50% - 40px); overflow: hidden; }}
        tr.equal td.code {{ color: #d4d4d4; }}
        tr.changed td.left-changed {{ background: #5d1f1f; color: #f8d7da; }}
        tr.changed td.right-changed {{ background: #1f3d1f; color: #d4edda; }}
        tr.deleted td.left-deleted {{ background: #5d1f1f; color: #f8d7da; }}
        tr.inserted td.right-inserted {{ background: #1f3d1f; color: #d4edda; }}
        .col-header {{ background: #2d2d2d; padding: 6px 8px; font-weight: bold; color: #9cdcfe; border-bottom: 2px solid #404040; position: sticky; top: 50px; z-index: 5; }}
        /* Navigation: jump between diffs */
        .nav {{ display: inline-block; margin-left: 20px; }}
        .nav button {{ background: #0e639c; color: white; border: none; padding: 4px 12px; margin: 0 4px; cursor: pointer; border-radius: 3px; }}
        .nav button:hover {{ background: #1177bb; }}
        /* Filter controls */
        .filter {{ display: inline-block; margin-left: 20px; }}
        .filter label {{ color: #808080; margin-right: 10px; cursor: pointer; }}
        .filter input {{ margin-right: 4px; }}
        body.hide-equal tr.equal {{ display: none; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{html.escape(name)} — Build Script Comparison</h1>
        <div class="stats">
            Original: {total_orig} lines | Generated: {total_gen} lines |
            Similarity: <span class="{'good' if similarity > 80 else 'warn' if similarity > 50 else 'bad'}">{similarity:.1f}%</span> |
            Matching lines: {matching}/{max(total_orig, total_gen)}
            <div class="nav">
                <button onclick="jumpDiff(-1)">← Prev Diff</button>
                <button onclick="jumpDiff(1)">Next Diff →</button>
            </div>
            <div class="filter">
                <label><input type="checkbox" id="hideEqual" onchange="toggleEqual()"> Show only differences</label>
            </div>
        </div>
    </div>
    <table>
        <tr>
            <td class="col-header" style="width:40px"></td>
            <td class="col-header">ORIGINAL (hand-maintained .tex)</td>
            <td class="col-header" style="width:40px"></td>
            <td class="col-header">GENERATED (build script .tex)</td>
        </tr>
        {table_html}
    </table>
    <script>
        let currentDiff = -1;
        function getDiffRows() {{
            return document.querySelectorAll('tr.changed, tr.deleted, tr.inserted');
        }}
        function jumpDiff(dir) {{
            const rows = getDiffRows();
            if (!rows.length) return;
            currentDiff += dir;
            if (currentDiff < 0) currentDiff = rows.length - 1;
            if (currentDiff >= rows.length) currentDiff = 0;
            rows[currentDiff].scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            // Flash highlight
            rows[currentDiff].style.outline = '2px solid #569cd6';
            setTimeout(() => rows[currentDiff].style.outline = '', 1500);
        }}
        function toggleEqual() {{
            document.body.classList.toggle('hide-equal', document.getElementById('hideEqual').checked);
        }}
    </script>
</body>
</html>"""


def main():
    for pair in PAIRS:
        print(f"Generating comparison: {pair['name']}...")
        html_content = generate_side_by_side_html(pair["name"], pair["original"], pair["generated"])
        with open(pair["output"], "w") as f:
            f.write(html_content)
        print(f"  Written: {pair['output']}")

    print("\nDone. Open both files for side-by-side review.")


if __name__ == "__main__":
    main()
