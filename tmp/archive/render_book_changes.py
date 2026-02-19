#!/usr/bin/env python3
"""
Generate an HTML review page for book manuscript changes.
Adapted for Session 56 (previously 55). Reusable — just update CHANGES/POSTPONED data.
"""

import html as html_mod

SESSION = 56

# Each change: (id, description, location, old_text, new_text, change_type)
CHANGES = [
    ("C34", "Math harder problems parenthetical",
     "Chapter 1 (~L141)",
     "This isn't an exaggeration. Physicists have the Standard Model.",
     "This isn't an exaggeration. (Though I should note, in fairness, that mathematics has problems I consider even harder — but those don't keep most people awake at night.) Physicists have the Standard Model.",
     "Parenthetical"),

    ("C33", "Metzinger's theory status update",
     "About the Author (~L119)",
     "The COGITATE adversarial collaboration showed that neither IIT nor GNW could fully explain consciousness, exactly as the theory predicts for any framework that lacks the four-model structure.",
     "The COGITATE adversarial collaboration showed that neither IIT nor GNW could fully explain consciousness, exactly as the theory predicts for any framework that lacks the four-model structure. And Metzinger, whose self-model theory had been one of the key ingredients? He had pivoted — first to AI ethics, publishing a striking call for a moratorium on artificial consciousness until 2050, then to the phenomenology of meditation, analyzing hundreds of reports on states where the self-model temporarily dissolves (The Elephant and the Blind, 2024). His framework was still cited but had never become the dominant paradigm. The field remained wide open.",
     "New sentences (3)"),

    ("C38", "Digital twin analogy + figure update",
     "Chapter 2 (~L229-239)",
     "[Old book figure reference + 'I call them the four models, organized along two axes' with dry taxonomy intro]",
     "[Paper figure + digital twin analogy: 'Your brain does exactly this — twice. It builds a digital twin of the world and a digital twin of you.' Then axes explanation as before, but with warmer setup.]",
     "Major rewrite (simplified intro)"),

    ("C42", "'t Hooft holographic universe connection",
     "Chapter 5 (~L611)",
     "[After Relationship 2, text ended with: '...exactly what quantum entanglement looks like.']",
     "[New paragraph on Gerard 't Hooft's CA interpretation of QM. 'If he's right, the principle I've been describing doesn't just apply to consciousness by analogy — it's literally how the universe works, all the way down.' Clearly flagged as speculative, minority view. Closing: 'if a single computational principle turns out to underlie both the universe and the minds that model it, that would be the most beautiful fact ever discovered.']",
     "New paragraph (speculative, flagged)"),

    ("C45", "Split-brain leans toward two persons",
     "Chapter 9 (~L899)",
     "But over time, the models should drift. [...] but measurably.",
     "But over time, the models should drift. [...] but measurably. [NEW] My own view is that the answer leans toward two. If the bandwidth between hemispheres is insufficient for real-time synchronization of the simulation — and without the callosum, it is — then you have two self-models running on two substrates, each generating its own conscious experience. They cooperate well because they share a body, a sensory environment, and a lifetime of common history. But cooperation is not identity. Two people who live together also cooperate well.",
     "New paragraph (author position)"),

    ("C54", "Salvia time dilation rewrite",
     "Chapter 6 (~L693)",
     "[Original: personal experience only, half a second → fifteen minutes, near-death comparison]",
     "[Expanded: includes wings/flying sensation + physical explanation (falling back on bed), NDE dated to ~1998/99, plus external account: 'One well-documented account involves a man who experienced what felt like eight complete years of an alternative life during a salvia episode that lasted roughly forty-five seconds.' Cites Addy et al. 2015.]",
     "Rewrite + new paragraph"),

    ("C56", "Crick/Koch NCC reference",
     "Notes and References — Chapter 11",
     "All nine predictions are developed formally in the scientific paper.",
     "All nine predictions are developed formally in the scientific paper. [NEW] For the most thorough treatment of functional neuroanatomy in the context of consciousness, see Christof Koch, The Quest for Consciousness (2004) — the Crick-Koch program walking step by step through the visual system. 'Their quest was, in my view, looking for consciousness in the wrong place (the substrate rather than the simulation), but the neuroanatomical groundwork they laid is unmatched.'",
     "New sentences (reference + assessment)"),

    ("C44", "Lucid dreaming appendix",
     "New Appendix D",
     "[Did not exist]",
     "[New appendix: Reality Check Method (4 steps), What to Expect, Other Methods (MILD, WILD, WBTB) with references to LaBerge (1990), Voss et al. (2009), Baird et al. (2019). ~450 words. Connected to Ch.6 via new cross-reference.]",
     "New appendix"),
]

POSTPONED = [
    ("C47", "LLM-breaking prompt experiment", "Chapter 11/12", "Prompt designed (Recursive Depth Probe) — needs testing by author on various LLM subscriptions"),
    ("C49", "Virtual-level-only copy theory", "Chapter 13", "Careful treatment needed — deferred to new subsection with C50/C51"),
    ("C50", "Brain 'programming language' decoding", "Chapter 13", "Deferred to new subsection with C49/C51"),
    ("C51", "Major copy problem meditation", "Chapter 13", "Large new subsection — sleep interruption, birth identity, personal experience. Combined with C49/C50"),
]


def diff_texts(old, new):
    """Simple word-level diff highlighting. Returns (old_html, new_html)."""
    old_words = old.split()
    new_words = new.split()

    # Find longest common prefix
    prefix_len = 0
    for i in range(min(len(old_words), len(new_words))):
        if old_words[i] == new_words[i]:
            prefix_len = i + 1
        else:
            break

    # Find longest common suffix (after prefix)
    suffix_len = 0
    for i in range(1, min(len(old_words) - prefix_len, len(new_words) - prefix_len) + 1):
        if old_words[-i] == new_words[-i]:
            suffix_len = i
        else:
            break

    # Build highlighted versions
    old_mid = old_words[prefix_len:len(old_words) - suffix_len if suffix_len else len(old_words)]
    new_mid = new_words[prefix_len:len(new_words) - suffix_len if suffix_len else len(new_words)]
    prefix = old_words[:prefix_len]
    suffix = old_words[len(old_words) - suffix_len:] if suffix_len else []

    def esc(words):
        return html_mod.escape(' '.join(words))

    old_html = ''
    new_html = ''

    if prefix:
        old_html += f'<span class="unchanged">{esc(prefix)} </span>'
        new_html += f'<span class="unchanged">{esc(prefix)} </span>'

    if old_mid:
        old_html += f'<span class="removed-text">{esc(old_mid)}</span>'
    if new_mid:
        new_html += f'<span class="added-text">{esc(new_mid)}</span>'

    if suffix:
        old_html += f' <span class="unchanged">{esc(suffix)}</span>'
        new_html += f' <span class="unchanged">{esc(suffix)}</span>'

    return old_html, new_html


def render_change(cid, desc, location, old_text, new_text, change_type):
    """Render a single change block."""
    old_html, new_html = diff_texts(old_text, new_text)

    return f'''<div class="change-block" id="change-{cid}">
  <div class="change-header">
    <span class="change-id">{cid}</span>
    <span class="change-desc">{html_mod.escape(desc)}</span>
    <span class="change-type">{html_mod.escape(change_type)}</span>
    <span class="change-loc">{html_mod.escape(location)}</span>
  </div>
  <div class="old-block">
    <div class="block-label">OLD</div>
    <div class="text-content">{old_html}</div>
  </div>
  <div class="new-block">
    <div class="block-label">NEW</div>
    <div class="text-content">{new_html}</div>
  </div>
</div>'''


def main():
    nav_links = '\n    '.join(
        f'<a href="#change-{cid}">{cid}</a>' for cid, *_ in CHANGES
    )

    change_blocks = '\n\n'.join(
        render_change(*c) for c in CHANGES
    )

    summary_rows = '\n'.join(
        f'<tr><td>{cid}</td><td>{html_mod.escape(desc)}</td>'
        f'<td>{html_mod.escape(loc)}</td><td>{html_mod.escape(ctype)}</td></tr>'
        for cid, desc, loc, _, _, ctype in CHANGES
    )

    postponed_rows = '\n'.join(
        f'<tr><td>{cid}</td><td>{html_mod.escape(desc)}</td>'
        f'<td>{html_mod.escape(loc)}</td><td>{html_mod.escape(reason)}</td></tr>'
        for cid, desc, loc, reason in POSTPONED
    )

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Book Manuscript — Session {SESSION} Changes Review</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{
    max-width: 920px;
    margin: 40px auto;
    padding: 0 24px 80px;
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 15px;
    line-height: 1.75;
    color: #222;
    background: #fafafa;
  }}
  h1 {{ font-size: 1.6em; margin-top: 1.5em; }}
  h2 {{ font-size: 1.3em; margin-top: 2em; border-bottom: 1px solid #ccc; padding-bottom: 0.3em; }}
  p {{ text-align: justify; }}

  .nav-bar {{
    position: fixed;
    top: 0; left: 0; right: 0;
    background: #1565c0;
    color: white;
    padding: 8px 20px;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.82em;
    z-index: 100;
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  }}
  .nav-bar .title {{ font-weight: bold; margin-right: auto; font-size: 1.1em; white-space: nowrap; }}
  .nav-bar a {{
    color: white;
    text-decoration: none;
    background: rgba(255,255,255,0.15);
    padding: 3px 10px;
    border-radius: 4px;
    font-weight: 500;
    white-space: nowrap;
  }}
  .nav-bar a:hover {{ background: rgba(255,255,255,0.3); }}
  body {{ padding-top: 55px; }}

  .change-block {{
    margin: 2em 0;
    border: 1px solid #bbb;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 1px 6px rgba(0,0,0,0.07);
  }}
  .change-header {{
    background: #1565c0;
    color: white;
    padding: 10px 16px;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.88em;
    display: flex;
    gap: 12px;
    align-items: center;
    flex-wrap: wrap;
  }}
  .change-id {{
    background: rgba(255,255,255,0.25);
    padding: 2px 10px;
    border-radius: 4px;
    font-weight: bold;
  }}
  .change-desc {{ flex: 1; min-width: 200px; }}
  .change-type {{
    background: rgba(255,255,255,0.12);
    padding: 2px 8px;
    border-radius: 3px;
    font-size: 0.9em;
    opacity: 0.9;
  }}
  .change-loc {{
    opacity: 0.8;
    font-style: italic;
    font-size: 0.9em;
  }}

  .old-block, .new-block {{
    padding: 14px 18px;
    position: relative;
  }}
  .old-block {{
    background: #fce4ec;
    border-bottom: 1px solid #e0e0e0;
  }}
  .new-block {{
    background: #e8f5e9;
  }}
  .block-label {{
    position: absolute;
    top: 8px; right: 14px;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.68em;
    font-weight: bold;
    letter-spacing: 0.5px;
    padding: 2px 10px;
    border-radius: 3px;
    color: white;
  }}
  .old-block .block-label {{ background: #c62828; }}
  .new-block .block-label {{ background: #2e7d32; }}

  .text-content {{
    font-size: 0.95em;
    padding-right: 50px;
  }}
  .unchanged {{ color: #666; }}
  .removed-text {{
    color: #b71c1c;
    background: #ffcdd2;
    padding: 1px 3px;
    border-radius: 2px;
    text-decoration: line-through;
    text-decoration-color: #e57373;
  }}
  .added-text {{
    color: #1b5e20;
    background: #c8e6c9;
    padding: 1px 3px;
    border-radius: 2px;
  }}

  table {{
    border-collapse: collapse;
    font-size: 0.88em;
    width: 100%;
    font-family: 'Helvetica Neue', Arial, sans-serif;
  }}
  th, td {{
    border: 1px solid #ccc;
    padding: 8px 12px;
    text-align: left;
    vertical-align: top;
  }}
  .summary th {{ background: #e3f2fd; }}
  .postponed th {{ background: #fff3e0; }}
  tr:nth-child(even) {{ background: #f8f8f8; }}

  .intro-box {{
    background: #e3f2fd;
    border: 1px solid #90caf9;
    border-radius: 6px;
    padding: 14px 18px;
    margin: 1.5em 0;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.92em;
  }}
  .intro-box strong {{ color: #1565c0; }}

  @media print {{
    .nav-bar {{ display: none; }}
    body {{ padding-top: 0; max-width: none; }}
    .change-block {{ break-inside: avoid; }}
  }}
</style>
</head>
<body>

<div class="nav-bar">
  <span class="title">Session {SESSION} — Book Changes</span>
  {nav_links}
</div>

<h1>Book Manuscript — Session {SESSION} Proposed Changes</h1>

<div class="intro-box">
  <strong>{len(CHANGES)} changes</strong> from postponed C items applied to <code>pop-sci/book-manuscript.md</code>.<br>
  Word count: 45,539 &rarr; 46,780 (+1,241 words).<br><br>
  Each change shows old text with <span class="removed-text">red strikethrough</span>
  and new text in <span class="added-text">green highlight</span>.
  Unchanged context appears in <span class="unchanged">grey</span>.<br><br>
  <strong>To revert any change:</strong> note its ID (e.g. C35) and tell me next session.
</div>

<h2>Proposed Changes (13)</h2>

{change_blocks}

<h2>Postponed for Next Session (12 items)</h2>

<p>These require discussion, research, structural decisions, or major new content.</p>

<div class="postponed">
<table>
<tr><th>ID</th><th>Description</th><th>Location</th><th>Why Postponed</th></tr>
{postponed_rows}
</table>
</div>

<h2>Change Summary</h2>

<div class="summary">
<table>
<tr><th>ID</th><th>Description</th><th>Location</th><th>Type</th></tr>
{summary_rows}
</table>
</div>

</body>
</html>'''

    output = '/home/jeltz/aIware/tmp/book-changes-review.html'
    with open(output, 'w') as f:
        f.write(page)
    print(f"Written to: {output}")
    print(f"Size: {len(page):,} bytes")
    print(f"Changes: {len(CHANGES)}")
    print(f"Postponed: {len(POSTPONED)}")


if __name__ == '__main__':
    main()
