#!/usr/bin/env python3
"""Generate index of extracted book images."""

import time
from pathlib import Path

output_dir = Path("/home/jeltz/aIware/figures/book")
pdf_path = "/mnt/c/Users/Matthias/Documents/_Eigene/Die Emergenz des Bewusstseins 6x9 lit.pdf"

# Collect all image files
image_files = sorted(output_dir.glob("book_page_*_img_*.png"))
render_files = sorted(output_dir.glob("book_page_*_render.png"))

# Parse image info
images_by_page = {}
for img_path in image_files:
    # Parse filename: book_page_064_img_2.png
    parts = img_path.stem.split('_')
    page_num = int(parts[2])
    img_num = int(parts[4])

    if page_num not in images_by_page:
        images_by_page[page_num] = []

    images_by_page[page_num].append({
        'img_num': img_num,
        'filename': img_path.name,
        'path': str(img_path)
    })

# Sort images within each page
for page in images_by_page:
    images_by_page[page].sort(key=lambda x: x['img_num'])

total_images = len(image_files)
key_pages = [64, 65, 262, 264]

# Write index
summary_path = output_dir / "IMAGE_INDEX.md"
with open(summary_path, "w") as f:
    f.write("# Book Image Extraction Index\n\n")
    f.write(f"**Source PDF**: `{pdf_path}`\n")
    f.write(f"**Total Pages**: 299\n")
    f.write(f"**Total Images Extracted**: {total_images}\n")
    f.write(f"**Extraction Date**: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

    f.write("## Summary\n\n")
    f.write(f"- {len(images_by_page)} pages contain embedded images\n")
    f.write(f"- {len(render_files)} pages rendered (including key pages)\n")
    f.write(f"- Output directory: `/home/jeltz/aIware/figures/book/`\n\n")

    f.write("## Key Theory Pages\n\n")
    f.write("Pages known to contain key theory figures:\n\n")
    for kp in key_pages:
        render_file = f"book_page_{kp:03d}_render.png"
        img_count = len(images_by_page.get(kp, []))
        if (output_dir / render_file).exists():
            f.write(f"- **Page {kp}**: {img_count} images extracted, full page render available\n")
            f.write(f"  - Render: `{render_file}`\n")
            if img_count > 0:
                f.write(f"  - Images: `book_page_{kp:03d}_img_{{1..{img_count}}}.png`\n")
        else:
            f.write(f"- **Page {kp}**: No render found\n")
        f.write("\n")

    f.write("## All Extracted Images by Page\n\n")

    for page_num in sorted(images_by_page.keys()):
        images = images_by_page[page_num]
        f.write(f"### Page {page_num}\n\n")
        f.write(f"- **Image count**: {len(images)}\n")
        f.write(f"- **Page render**: `book_page_{page_num:03d}_render.png`\n")
        f.write(f"- **Images**:\n")

        for img in images:
            f.write(f"  - `{img['filename']}`\n")

        f.write("\n")

print(f"Index generated: {summary_path}")
print(f"Total images cataloged: {total_images}")
