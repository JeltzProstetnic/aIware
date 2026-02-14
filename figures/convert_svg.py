#!/usr/bin/env python3
"""
Convert SVG to PNG using available Python libraries.
Fallback approach if dedicated SVG converters aren't available.
"""

import subprocess
import sys
import os

svg_file = '/home/jeltz/aIware/figures/figure1-four-model-architecture.svg'
png_file = '/home/jeltz/aIware/figures/figure1-four-model-architecture.png'

# Try different conversion methods in order of preference

# Method 1: rsvg-convert (if available)
try:
    result = subprocess.run(['rsvg-convert', svg_file, '-o', png_file],
                          capture_output=True, check=True)
    print(f"Converted using rsvg-convert: {png_file}")
    sys.exit(0)
except (subprocess.CalledProcessError, FileNotFoundError):
    pass

# Method 2: inkscape (if available)
try:
    result = subprocess.run(['inkscape', '--export-type=png',
                           '--export-filename=' + png_file, svg_file],
                          capture_output=True, check=True)
    print(f"Converted using inkscape: {png_file}")
    sys.exit(0)
except (subprocess.CalledProcessError, FileNotFoundError):
    pass

# Method 3: ImageMagick convert (if available)
try:
    result = subprocess.run(['convert', svg_file, png_file],
                          capture_output=True, check=True)
    print(f"Converted using ImageMagick: {png_file}")
    sys.exit(0)
except (subprocess.CalledProcessError, FileNotFoundError):
    pass

# Method 4: cairosvg (if available)
try:
    import cairosvg
    cairosvg.svg2png(url=svg_file, write_to=png_file)
    print(f"Converted using cairosvg: {png_file}")
    sys.exit(0)
except (ImportError, Exception) as e:
    pass

# Method 5: svglib + reportlab (if available)
try:
    from svglib.svglib import svg2rlg
    from reportlab.graphics import renderPM
    drawing = svg2rlg(svg_file)
    renderPM.drawToFile(drawing, png_file, fmt='PNG')
    print(f"Converted using svglib: {png_file}")
    sys.exit(0)
except (ImportError, Exception) as e:
    pass

print("ERROR: No SVG conversion tool found. Tried:", file=sys.stderr)
print("  - rsvg-convert (librsvg2-bin)", file=sys.stderr)
print("  - inkscape", file=sys.stderr)
print("  - convert (ImageMagick)", file=sys.stderr)
print("  - cairosvg (Python)", file=sys.stderr)
print("  - svglib (Python)", file=sys.stderr)
print("\nPlease install one of these tools.", file=sys.stderr)
sys.exit(1)
