#!/usr/bin/env python3
"""Extract all images and page renders from the German book PDF."""

import fitz  # PyMuPDF
import os
import time
from pathlib import Path

# Paths
pdf_path = "/mnt/c/Users/Matthias/Documents/_Eigene/Die Emergenz des Bewusstseins 6x9 lit.pdf"
output_dir = Path("/home/jeltz/aIware/figures/book")
output_dir.mkdir(parents=True, exist_ok=True)

# Key pages to render
key_pages = [64, 65, 262, 264]

print(f"Opening PDF: {pdf_path}")
doc = fitz.open(pdf_path)
total_pages = len(doc)
print(f"Total pages: {total_pages}")

image_count = 0
image_index = []

# Process each page
for page_num in range(total_pages):
    page = doc[page_num]
    page_index = page_num + 1  # 1-indexed for readability

    # Extract images from this page
    image_list = page.get_images()

    if image_list:
        print(f"\nPage {page_index}: Found {len(image_list)} image(s)")

        # Render the page for context
        render_path = output_dir / f"book_page_{page_index:03d}_render.png"
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x zoom for better quality
        pix.save(render_path)
        print(f"  Rendered page to: {render_path}")

        # Extract each image
        for img_index, img in enumerate(image_list):
            xref = img[0]
            img_num = img_index + 1

            try:
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]

                # Save as PNG regardless of original format
                img_path = output_dir / f"book_page_{page_index:03d}_img_{img_num}.png"

                if image_ext != "png":
                    # Convert to PNG using fitz
                    import io
                    from PIL import Image
                    img_pil = Image.open(io.BytesIO(image_bytes))
                    img_pil.save(img_path, "PNG")
                else:
                    with open(img_path, "wb") as f:
                        f.write(image_bytes)

                # Get image dimensions
                width = base_image.get("width", "unknown")
                height = base_image.get("height", "unknown")

                print(f"  Image {img_num}: {width}x{height} -> {img_path.name}")

                image_index.append({
                    "page": page_index,
                    "img_num": img_num,
                    "path": str(img_path),
                    "width": width,
                    "height": height,
                    "format": image_ext
                })

                image_count += 1

            except Exception as e:
                print(f"  Error extracting image {img_num}: {e}")

    # Also render key pages even if they have no embedded images
    elif page_index in key_pages:
        print(f"\nPage {page_index}: Key page (rendering even without embedded images)")
        render_path = output_dir / f"book_page_{page_index:03d}_render.png"
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        pix.save(render_path)
        print(f"  Rendered page to: {render_path}")

doc.close()

print(f"\n{'='*60}")
print(f"EXTRACTION COMPLETE")
print(f"Total images extracted: {image_count}")
print(f"Total pages processed: {total_pages}")
print(f"{'='*60}")

# Write summary
summary_path = output_dir / "IMAGE_INDEX.md"
with open(summary_path, "w") as f:
    f.write("# Book Image Extraction Index\n\n")
    f.write(f"**Source PDF**: `{pdf_path}`\n")
    f.write(f"**Total Pages**: {total_pages}\n")
    f.write(f"**Total Images Extracted**: {image_count}\n")
    f.write(f"**Extraction Date**: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

    f.write("## Extracted Images\n\n")

    if image_index:
        current_page = None
        for img in image_index:
            if img["page"] != current_page:
                current_page = img["page"]
                f.write(f"\n### Page {current_page}\n\n")

            f.write(f"- **Image {img['img_num']}**: `{Path(img['path']).name}`\n")
            f.write(f"  - Dimensions: {img['width']} x {img['height']} pixels\n")
            f.write(f"  - Original format: {img['format']}\n")
            f.write(f"  - Full path: `{img['path']}`\n")
            f.write(f"  - Page render: `book_page_{current_page:03d}_render.png`\n\n")
    else:
        f.write("No images found in PDF.\n")

    f.write("\n## Key Theory Pages\n\n")
    f.write("Pages known to contain key theory figures:\n")
    for kp in key_pages:
        render_file = f"book_page_{kp:03d}_render.png"
        if (output_dir / render_file).exists():
            f.write(f"- Page {kp}: `{render_file}` ✓\n")
        else:
            f.write(f"- Page {kp}: (not rendered)\n")

print(f"\nIndex saved to: {summary_path}")
