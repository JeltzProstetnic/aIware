#!/usr/bin/env python3
"""Map images in the book .docx to their surrounding text context."""
from docx import Document

DOCX_PATH = "/home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9.docx"
doc = Document(DOCX_PATH)

# Map rIds to image filenames
rid_to_img = {}
idx = 0
for rel in doc.part.rels.values():
    if "image" in rel.reltype:
        idx += 1
        content_type = rel.target_part.content_type
        ext_map = {'image/png': '.png', 'image/jpeg': '.jpg', 'image/gif': '.gif',
                   'image/x-emf': '.emf', 'image/x-wmf': '.wmf'}
        ext = ext_map.get(content_type, '.bin')
        rid_to_img[rel.rId] = f"image_{idx:03d}{ext}"

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
WP = 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'
A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'

body = doc.element.body
paragraphs = list(body.iter(f'{{{W}}}p'))

print("=== Image placement context ===\n")

for i, para in enumerate(paragraphs):
    drawings = list(para.iter(f'{{{WP}}}inline')) + list(para.iter(f'{{{WP}}}anchor'))

    for drawing in drawings:
        blip = drawing.find(f'.//{{{A}}}blip')
        if blip is not None:
            r_embed = blip.get(f'{{{R}}}embed')
            if r_embed and r_embed in rid_to_img:
                img_name = rid_to_img[r_embed]

                docPr = drawing.find(f'.//{{{WP}}}docPr')
                alt_text = ""
                name_attr = ""
                if docPr is not None:
                    alt_text = docPr.get('descr', '')
                    name_attr = docPr.get('name', '')

                prev_text = ""
                for j in range(i-1, max(i-5, -1), -1):
                    t = ''.join(node.text for node in paragraphs[j].iter(f'{{{W}}}t') if node.text)
                    if t.strip():
                        prev_text = t.strip()[:120]
                        break

                next_text = ""
                for j in range(i+1, min(i+5, len(paragraphs))):
                    t = ''.join(node.text for node in paragraphs[j].iter(f'{{{W}}}t') if node.text)
                    if t.strip():
                        next_text = t.strip()[:120]
                        break

                print(f"Image: {img_name}")
                if name_attr:
                    print(f"  Name: {name_attr}")
                if alt_text:
                    print(f"  Alt: {alt_text}")
                print(f"  Before: {prev_text}")
                print(f"  After:  {next_text}")
                print()
