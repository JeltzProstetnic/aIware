#!/usr/bin/env python3
"""Extract all embedded images from the book source .docx and catalog them."""

import os
import sys
from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT

DOCX_PATH = "/home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9.docx"
OUTPUT_DIR = "/home/jeltz/aIware/wiki/assets/book-originals"

def get_image_extension(content_type):
    """Map content type to file extension."""
    mapping = {
        'image/png': '.png',
        'image/jpeg': '.jpg',
        'image/gif': '.gif',
        'image/bmp': '.bmp',
        'image/tiff': '.tiff',
        'image/x-emf': '.emf',
        'image/x-wmf': '.wmf',
        'image/svg+xml': '.svg',
    }
    return mapping.get(content_type, '.bin')

def extract_images():
    """Extract all images from the .docx file."""
    print(f"Opening: {DOCX_PATH}")
    doc = Document(DOCX_PATH)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Method 1: Extract from document relationships (most reliable for all images)
    images = []
    idx = 0

    # Iterate through all parts in the package
    for rel in doc.part.rels.values():
        if "image" in rel.reltype:
            idx += 1
            part = rel.target_part
            content_type = part.content_type
            ext = get_image_extension(content_type)
            filename = f"image_{idx:03d}{ext}"
            filepath = os.path.join(OUTPUT_DIR, filename)

            blob = part.blob
            with open(filepath, 'wb') as f:
                f.write(blob)

            size_bytes = len(blob)
            images.append({
                'filename': filename,
                'filepath': filepath,
                'content_type': content_type,
                'size_bytes': size_bytes,
                'rel_id': rel.rId,
            })
            print(f"  Extracted: {filename} ({content_type}, {size_bytes:,} bytes)")

    # Also check for images in headers and footers
    for section in doc.sections:
        for header_footer in [section.header, section.footer]:
            if header_footer is not None:
                try:
                    for rel in header_footer.part.rels.values():
                        if "image" in rel.reltype:
                            idx += 1
                            part = rel.target_part
                            content_type = part.content_type
                            ext = get_image_extension(content_type)
                            filename = f"image_{idx:03d}{ext}"
                            filepath = os.path.join(OUTPUT_DIR, filename)

                            blob = part.blob
                            with open(filepath, 'wb') as f:
                                f.write(blob)

                            size_bytes = len(blob)
                            images.append({
                                'filename': filename,
                                'filepath': filepath,
                                'content_type': content_type,
                                'size_bytes': size_bytes,
                                'rel_id': rel.rId,
                                'source': 'header/footer',
                            })
                            print(f"  Extracted (header/footer): {filename} ({content_type}, {size_bytes:,} bytes)")
                except Exception as e:
                    print(f"  Warning: Could not process header/footer: {e}")

    print(f"\nTotal images extracted: {len(images)}")
    return images

def get_image_dimensions(filepath):
    """Get image dimensions using PIL if available, otherwise from raw bytes."""
    try:
        from PIL import Image
        with Image.open(filepath) as img:
            return img.size  # (width, height)
    except ImportError:
        # Try to read dimensions from PNG/JPEG headers manually
        return read_dimensions_manual(filepath)
    except Exception:
        return None

def read_dimensions_manual(filepath):
    """Read image dimensions from file headers without PIL."""
    try:
        with open(filepath, 'rb') as f:
            header = f.read(32)

            # PNG
            if header[:8] == b'\x89PNG\r\n\x1a\n':
                import struct
                w = struct.unpack('>I', header[16:20])[0]
                h = struct.unpack('>I', header[20:24])[0]
                return (w, h)

            # JPEG
            if header[:2] == b'\xff\xd8':
                f.seek(0)
                data = f.read()
                i = 2
                while i < len(data) - 9:
                    if data[i] == 0xFF:
                        marker = data[i+1]
                        if marker in (0xC0, 0xC1, 0xC2):
                            import struct
                            h = struct.unpack('>H', data[i+5:i+7])[0]
                            w = struct.unpack('>H', data[i+7:i+9])[0]
                            return (w, h)
                        elif marker == 0xD9:
                            break
                        elif marker == 0xDA:
                            break
                        else:
                            length = struct.unpack('>H', data[i+2:i+4])[0]
                            i += 2 + length
                    else:
                        i += 1
                return None

            # GIF
            if header[:6] in (b'GIF87a', b'GIF89a'):
                import struct
                w = struct.unpack('<H', header[6:8])[0]
                h = struct.unpack('<H', header[8:10])[0]
                return (w, h)

            # EMF/WMF - can't easily read dimensions
            return None
    except Exception:
        return None

def format_size(size_bytes):
    """Format file size in human-readable form."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"

if __name__ == "__main__":
    images = extract_images()

    print("\n--- Image catalog ---")
    for img in images:
        dims = get_image_dimensions(img['filepath'])
        dim_str = f"{dims[0]}x{dims[1]}" if dims else "unknown"
        img['dimensions'] = dim_str
        print(f"{img['filename']}: {dim_str}, {format_size(img['size_bytes'])}, {img['content_type']}")

    # Write summary for later use
    summary_path = os.path.join(OUTPUT_DIR, "_extraction_summary.txt")
    with open(summary_path, 'w') as f:
        for img in images:
            f.write(f"{img['filename']}|{img.get('dimensions', 'unknown')}|{img['size_bytes']}|{img['content_type']}\n")
    print(f"\nSummary written to: {summary_path}")
