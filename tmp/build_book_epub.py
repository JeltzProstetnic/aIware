#!/usr/bin/env python3
"""Convert book-manuscript.md to a Kindle-ready EPUB file.

Uses pandoc to generate EPUB3 from preprocessed markdown.
Parallel to build_book_pdf.py but targets the eBook pipeline.
"""

import os
import re
import shutil
import subprocess
import tempfile

MANUSCRIPT = "/home/jeltz/aIware/pop-sci/book-manuscript.md"
FIGURES_DIR = "/home/jeltz/aIware/figures"
COVER_IMAGE = "/home/jeltz/aIware/pop-sci/cover-kindle.jpg"
OUTPUT_DIR = "/home/jeltz/aIware/pop-sci"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "book-manuscript.epub")

# Image paths used in the manuscript (relative to pop-sci/) -> flat copy name
IMAGE_MAP = {
    "../figures/figure2-real-virtual-split-bw.png": "figure2-real-virtual-split-bw.png",
    "../figures/book/homunculi.en.png": "homunculi-en.png",
    "../figures/figure-five-layer-stack-bw.png": "figure-five-layer-stack-bw.png",
    "../figures/figure1-four-model-architecture-bw.png": "figure1-four-model-architecture-bw.png",
    "../figures/figure3-phenomenological-content-bw.png": "figure3-phenomenological-content-bw.png",
}


def resolve_image_path(rel_path):
    """Resolve a manuscript-relative image path to an absolute path."""
    # Paths in the manuscript are relative to pop-sci/
    return os.path.normpath(os.path.join(OUTPUT_DIR, rel_path))


def preprocess_markdown(md_text, img_dir):
    """Preprocess the manuscript markdown for EPUB conversion.

    - Copies images to img_dir with flat names and rewrites paths
    - Strips [FIGURE: ...] placeholder lines (image generation prompts)
    - Strips the manual TOC section (pandoc generates its own nav)
    - Inserts figure3 after the trigger line (matching PDF build script)
    """
    lines = md_text.split('\n')
    out_lines = []
    i = 0
    skip_toc = False
    figure3_inserted = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # --- Skip the manual TOC section ---
        if stripped == '## Contents':
            # Skip until next ---
            i += 1
            while i < len(lines) and lines[i].strip() != '---':
                i += 1
            i += 1  # skip the ---
            continue

        # --- Skip [FIGURE: ...] placeholder lines ---
        if stripped.startswith('[FIGURE:'):
            i += 1
            continue

        # --- Skip HTML comments ---
        if stripped.startswith('<!--'):
            if '-->' in stripped:
                i += 1
                continue
            i += 1
            while i < len(lines) and '-->' not in lines[i]:
                i += 1
            if i < len(lines):
                i += 1
            continue

        # --- Rewrite image paths ---
        img_match = re.match(r'^(!\[[^\]]*\])\(([^)]+)\)\s*$', stripped)
        if img_match:
            prefix = img_match.group(1)
            img_path = img_match.group(2)
            if img_path in IMAGE_MAP:
                flat_name = IMAGE_MAP[img_path]
                # Copy the image to the temp img directory
                src = resolve_image_path(img_path)
                dst = os.path.join(img_dir, flat_name)
                if os.path.exists(src):
                    shutil.copy2(src, dst)
                else:
                    print(f"  WARNING: Image not found: {src}")
                out_lines.append(f'{prefix}({flat_name})')
            else:
                # Unknown image — try to copy anyway
                src = resolve_image_path(img_path)
                flat_name = os.path.basename(img_path)
                dst = os.path.join(img_dir, flat_name)
                if os.path.exists(src):
                    shutil.copy2(src, dst)
                out_lines.append(f'{prefix}({flat_name})')
            i += 1
            continue

        # --- Insert figure3 after trigger line ---
        if not figure3_inserted and 'consciousness is not a light switch' in stripped.lower():
            out_lines.append(line)
            i += 1
            # Insert figure3 image
            fig3_src = os.path.join(FIGURES_DIR, "figure3-phenomenological-content-bw.png")
            fig3_name = "figure3-phenomenological-content-bw.png"
            fig3_dst = os.path.join(img_dir, fig3_name)
            if os.path.exists(fig3_src):
                shutil.copy2(fig3_src, fig3_dst)
            out_lines.append('')
            out_lines.append(f'![Phenomenological Content Through a Morning]({fig3_name})')
            out_lines.append('')
            out_lines.append('*Phenomenological Content Through a Morning. Routine activities lead to low '
                           'phenomenological content (autopilot). Salient events (threats, social signals) '
                           'produce high phenomenological content. Consciousness tracks what matters, not everything.*')
            out_lines.append('')
            figure3_inserted = True
            continue

        out_lines.append(line)
        i += 1

    return '\n'.join(out_lines)


def generate_metadata_yaml(tmp_dir):
    """Generate EPUB metadata YAML file."""
    yaml_content = """\
---
title: 'The Simulation You Call "I"'
subtitle: "The Architecture of Consciousness, Computation, and the Cosmos"
creator:
  - role: author
    text: Matthias Gruber
language: en
date: "2026"
rights: "© 2026 Matthias Gruber. All rights reserved."
description: >
  A groundbreaking theory of consciousness that dissolves the Hard Problem,
  explains what psychedelics reveal about the brain, and provides a blueprint
  for building a conscious machine.
subject:
  - Consciousness
  - Neuroscience
  - Philosophy of Mind
  - Artificial Intelligence
  - Popular Science
...
"""
    path = os.path.join(tmp_dir, "metadata.yaml")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(yaml_content)
    return path


def generate_css(tmp_dir):
    """Generate Kindle-optimized CSS stylesheet."""
    css_content = """\
/* Kindle-optimized EPUB stylesheet */

body {
  font-family: Palatino, "Palatino Linotype", Georgia, "Book Antiqua", serif;
  line-height: 1.6;
  margin: 1em;
  text-align: justify;
  hyphens: auto;
  -webkit-hyphens: auto;
}

/* Chapter headings */
h1 {
  font-size: 1.8em;
  font-weight: bold;
  margin-top: 2em;
  margin-bottom: 0.8em;
  text-align: left;
  page-break-before: always;
}

h2 {
  font-size: 1.4em;
  font-weight: bold;
  margin-top: 1.5em;
  margin-bottom: 0.5em;
  text-align: left;
}

h3 {
  font-size: 1.2em;
  font-weight: bold;
  margin-top: 1.2em;
  margin-bottom: 0.4em;
  text-align: left;
}

/* Blockquotes — italic, indented */
blockquote {
  font-style: italic;
  margin: 1em 1.5em;
  padding: 0.5em 0;
  border-left: 3px solid #999;
  padding-left: 1em;
}

blockquote p {
  font-style: italic;
  margin: 0.3em 0;
}

/* Tables — responsive, bordered, readable */
table {
  border-collapse: collapse;
  width: 100%;
  margin: 1em 0;
  font-size: 0.85em;
  line-height: 1.4;
}

th, td {
  border: 1px solid #666;
  padding: 0.4em 0.6em;
  text-align: left;
  vertical-align: top;
}

th {
  background-color: #f0f0f0;
  font-weight: bold;
}

tr:nth-child(even) {
  background-color: #fafafa;
}

/* Figures and captions */
figure {
  margin: 1.5em 0;
  text-align: center;
  page-break-inside: avoid;
}

figure img {
  max-width: 100%;
  height: auto;
}

figcaption {
  font-style: italic;
  font-size: 0.9em;
  margin-top: 0.5em;
  text-align: center;
  color: #444;
}

/* Images outside figure elements */
img {
  max-width: 100%;
  height: auto;
}

/* Emphasis caption paragraphs (italic text after images) */
p > em:only-child {
  display: block;
  font-size: 0.9em;
  color: #444;
  margin-top: 0.3em;
}

/* Lists */
ul, ol {
  margin: 0.8em 0;
  padding-left: 1.5em;
}

li {
  margin-bottom: 0.3em;
}

/* Definition-style lists in Appendix A (bold term + dash + definition) */
li > strong:first-child {
  font-weight: bold;
}

/* Horizontal rules */
hr {
  border: none;
  border-top: 1px solid #ccc;
  margin: 2em 0;
}

/* Dedication */
p > em:only-child {
  text-align: center;
  display: block;
}

/* Title page */
.title {
  font-size: 2em;
  text-align: center;
  margin-top: 3em;
}

.subtitle {
  font-size: 1.3em;
  text-align: center;
  font-style: italic;
  margin-top: 0.5em;
}

.author {
  font-size: 1.2em;
  text-align: center;
  margin-top: 2em;
}
"""
    path = os.path.join(tmp_dir, "kindle.css")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    return path


def main():
    print("=" * 60)
    print("Building EPUB: The Simulation You Call \"I\"")
    print("=" * 60)

    # Create temp working directory
    tmp_dir = tempfile.mkdtemp(prefix="epub_build_")
    img_dir = os.path.join(tmp_dir, "images")
    os.makedirs(img_dir)
    print(f"Working dir: {tmp_dir}")

    # Read manuscript
    print("Reading manuscript...")
    with open(MANUSCRIPT, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Preprocess
    print("Preprocessing markdown...")
    processed = preprocess_markdown(md_text, img_dir)

    # Write preprocessed markdown
    md_path = os.path.join(tmp_dir, "book.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(processed)

    # Generate metadata and CSS
    print("Generating metadata and CSS...")
    meta_path = generate_metadata_yaml(tmp_dir)
    css_path = generate_css(tmp_dir)

    # Copy cover image
    cover_dst = os.path.join(tmp_dir, "cover-kindle.jpg")
    shutil.copy2(COVER_IMAGE, cover_dst)
    print(f"Cover image: {COVER_IMAGE}")

    # Count images
    img_files = os.listdir(img_dir)
    print(f"Images copied: {len(img_files)} ({', '.join(sorted(img_files))})")

    # Run pandoc
    print("\nRunning pandoc...")
    epub_path = os.path.join(tmp_dir, "book-manuscript.epub")
    cmd = [
        'pandoc', md_path,
        '-o', epub_path,
        '--metadata-file=' + meta_path,
        '--css=' + css_path,
        '--epub-cover-image=' + cover_dst,
        '--toc',
        '--toc-depth=2',
        '--split-level=2',
        '--mathml',
        '--resource-path=' + img_dir,
    ]
    print(f"  Command: {' '.join(cmd)}")

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

    if result.returncode != 0:
        print(f"\nPandoc FAILED (exit code {result.returncode})")
        if result.stderr:
            print(f"STDERR:\n{result.stderr}")
        if result.stdout:
            print(f"STDOUT:\n{result.stdout}")
        # Clean up
        shutil.rmtree(tmp_dir)
        return False

    if result.stderr:
        # Pandoc often writes warnings to stderr even on success
        warnings = [l for l in result.stderr.strip().split('\n') if l.strip()]
        if warnings:
            print(f"  Pandoc warnings ({len(warnings)}):")
            for w in warnings[:10]:
                print(f"    {w}")
            if len(warnings) > 10:
                print(f"    ... and {len(warnings) - 10} more")

    # Verify output
    if not os.path.exists(epub_path):
        print("\nFAILED: EPUB file not created")
        shutil.rmtree(tmp_dir)
        return False

    size_mb = os.path.getsize(epub_path) / (1024 * 1024)
    print(f"\nEPUB created: {epub_path} ({size_mb:.2f} MB)")

    # Copy to output directory
    shutil.copy2(epub_path, OUTPUT_FILE)
    print(f"Copied to: {OUTPUT_FILE}")

    # Copy to Windows desktop
    win_path = "/mnt/c/Users/Matthias/Desktop/book-manuscript.epub"
    try:
        shutil.copy2(epub_path, win_path)
        print(f"Copied to: {win_path}")
    except Exception as e:
        print(f"Note: Could not copy to Windows desktop: {e}")

    # Basic structure inspection
    print("\nEPUB structure:")
    import zipfile
    with zipfile.ZipFile(OUTPUT_FILE, 'r') as z:
        names = z.namelist()
        for name in sorted(names):
            info = z.getinfo(name)
            if info.file_size > 0:
                print(f"  {name} ({info.file_size:,} bytes)")
            else:
                print(f"  {name}")

    # Clean up temp directory
    shutil.rmtree(tmp_dir)
    print(f"\nCleaned up: {tmp_dir}")

    print(f"\n{'=' * 60}")
    print(f"SUCCESS: {OUTPUT_FILE} ({size_mb:.2f} MB)")
    print(f"{'=' * 60}")
    return True


if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
