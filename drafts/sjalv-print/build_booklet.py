"""SJÄLV — saddle-stitch booklet imposition for A4 duplex laser printing.

Physical object
--------------
3 × A4 portrait sheets, nested and folded once across the middle, stapled in
the fold.  That gives a 12-page A5-LANDSCAPE booklet with the spine along the
TOP edge, which is what "two slides on each A4 page" forces: the slides are
16:9, so the fold has to be horizontal.  Opened, it reads as a vertical spread
— one page above the fold, one below, both upright.

Page plan (12 pages, so the outer sheet carries slides 1 and 10):
    1  slide 01 (front cover)      7  slide 06
    2  blank (inside front)        8  slide 07
    3  slide 02                    9  slide 08
    4  slide 03                   10  slide 09
    5  slide 04                   11  slide 10 (inside back)
    6  slide 05                   12  blurb + QR (outer back)

Imposition (duplex flipping on the LONG edge):
    sheet i FRONT: lower = page(2i-1) upright ; upper = page(P-2i+2) upright
    sheet i BACK : lower = page(2i)   rot180  ; upper = page(P-2i+1) rot180

CORRECTED 2026-08-05 against a real print.  The two faces of the SAME half-leaf
must carry OPPOSITE rotations, because flipping a leaf about a top spine turns
it through 180 degrees.  The first version had front-upper and back-upper both
at 180, which put pages 8, 10 and 12 upside down.  Front side upright, back
side rotated: the standard pattern for a top-bound duplex booklet.

Print settings: plain duplex, flip on LONG edge, 100 % / actual size,
NO "booklet" or "N-up" mode — the imposition is already done here.
"""
import argparse
import glob
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas

SRC = glob.glob('/mnt/c/Users/Matthias/Pictures/SJ*LV')[0]
HERE = os.path.dirname(os.path.abspath(__file__))
COVER_ART = os.path.join(HERE, "cover-content.png")   # 01.png with the
# original border box and the two part numbers cropped away — both are
# redrawn as vector below, so the cover can fill a turned portrait page
# instead of sitting in it as a narrow 16:9 strip.
SHEET_W, SHEET_H = A4                      # 210 × 297 mm in points
HALF_H = SHEET_H / 2                       # a booklet page is 210 × 148.5 mm

# page-local layout, origin bottom-left of the A5-landscape page, spine on top
M_SIDE, M_SPINE, M_FOOT = 10 * mm, 15 * mm, 11 * mm

QR_URL = "https://doi.org/10.5281/zenodo.18669891"
SITE = "matthiasgruber.com"

BLURB = [
    "Contents:  1 × substrate sheet · 1 × virtual layer · 1 × body",
    "1 × energy supply · 1 × Allen key · 1 × sealed bag",
    "Weights not included.",
    "",
    "Three parts remain on backorder.",
]


# --------------------------------------------------------------------------
# page painters — each draws into a 210 × 148.5 mm frame at the current origin
# --------------------------------------------------------------------------
def paint_slide(c, path, w=None, h=None):
    w = SHEET_W if w is None else w
    h = HALF_H if h is None else h
    box_w = w - 2 * M_SIDE
    box_h = h - M_SPINE - M_FOOT
    img = ImageReader(path)
    iw, ih = img.getSize()
    iw_w = box_w
    ih_h = iw_w * ih / iw
    if ih_h > box_h:                       # never crop a page
        ih_h = box_h
        iw_w = ih_h * iw / ih
    x = (w - iw_w) / 2
    y = M_FOOT + (box_h - ih_h) / 2
    c.drawImage(img, x, y, width=iw_w, height=ih_h, mask=None)


def paint_blank(c):
    pass


def paint_cover(c, w, h):
    """Turned front cover: fresh border box, content flush to the top."""
    bx0, by0 = M_SIDE, M_FOOT
    bx1, by1 = w - M_SIDE, h - M_SPINE
    c.setLineWidth(1.6)
    c.setStrokeGray(0)
    c.rect(bx0, by0, bx1 - bx0, by1 - by0)

    pad = 8 * mm
    img = ImageReader(COVER_ART)
    iw, ih = img.getSize()
    aw = (bx1 - bx0) - 2 * pad
    ah = aw * ih / iw
    c.drawImage(img, bx0 + pad, by1 - pad - ah, width=aw, height=ah, mask=None)

    c.setFillGray(0)
    c.setFont("Helvetica", 11)
    c.drawString(bx0 + pad, by0 + pad + 13, "45")
    c.drawString(bx0 + pad, by0 + pad, "22000")


def paint_backcover(c, w=None, h=None):
    w = SHEET_W if w is None else w
    h = HALF_H if h is None else h
    cx = w / 2
    top = h - M_SPINE

    c.setFillGray(0)
    c.setFont("Helvetica-Bold", 34)
    c.drawCentredString(cx, top - 26, "SJÄLV")
    c.setFont("Helvetica", 11.5)
    c.drawCentredString(cx, top - 42, "AC — Assembly Instructions")

    c.setLineWidth(1.1)
    c.line(cx - 0.4 * w, top - 52, cx + 0.4 * w, top - 52)

    y = top - 70
    for ln in BLURB:
        if ln:
            c.setFont("Helvetica-Bold" if ln.startswith("Three") else "Helvetica", 9.5)
            c.drawCentredString(cx, y, ln)
        y -= 13

    side = 26 * mm
    w = qr.QrCodeWidget(QR_URL, barLevel='M')
    b = w.getBounds()
    d = Drawing(side, side, transform=[side / (b[2] - b[0]), 0, 0,
                                       side / (b[3] - b[1]), 0, 0])
    d.add(w)
    renderPDF.draw(d, c, cx - side / 2, M_FOOT + 15)

    c.setFont("Helvetica", 8)
    c.drawCentredString(cx, M_FOOT + 6, "Four-Model Theory · M. Gruber · " + SITE)
    c.setFont("Helvetica", 6.5)
    c.setFillGray(0.45)
    c.drawCentredString(cx, M_FOOT - 3,
                        "Models of Consciousness 7 · Copenhagen · October 2026")
    c.setFillGray(0)


# --------------------------------------------------------------------------
def build_pages():
    s = lambda n: os.path.join(SRC, f"{n:02d}.png")
    order = [("ROT90", "COVER"), s(1), s(2), s(3), s(4), s(5), s(6), s(7),
             s(8), s(9), s(10), ("ROT90", "BACKCOVER")]
    for p in order:
        q = p[1] if isinstance(p, tuple) else p
        if q not in (None, "BACKCOVER", "COVER") and not os.path.exists(q):
            raise SystemExit(f"missing source: {q}")
    return order


def turned(c, cw=True):
    """Set up a portrait 148.5 x 210 frame on the landscape page."""
    if cw:
        c.translate(SHEET_W, 0)
        c.rotate(90)
    else:
        c.translate(0, HALF_H)
        c.rotate(-90)


def paint(c, page, cover_cw=True):
    if isinstance(page, tuple):                      # ("ROT90", what)
        _, what = page
        c.saveState()
        turned(c, cover_cw)
        if what == "BACKCOVER":
            paint_backcover(c, w=HALF_H, h=SHEET_W)
        elif what == "COVER":
            paint_cover(c, w=HALF_H, h=SHEET_W)
        else:
            paint_slide(c, what, w=HALF_H, h=SHEET_W)
        c.restoreState()
    elif page is None:
        paint_blank(c)
    elif page == "BACKCOVER":
        paint_backcover(c)
    else:
        paint_slide(c, page)


def place(c, page, half, rot, label, marks, cover_cw=True):
    """half: 'lower'|'upper'; rot: 0|180. Sets up the page-local frame."""
    c.saveState()
    if rot == 180:
        c.translate(SHEET_W, SHEET_H if half == 'upper' else HALF_H)
        c.rotate(180)
    elif half == 'upper':
        c.translate(0, HALF_H)
    paint(c, page, cover_cw)
    if marks:
        c.setFont("Helvetica", 6)
        c.setFillGray(0.6)
        c.drawString(6 * mm, 4 * mm, label)
        c.setFillGray(0)
    c.restoreState()


def impose(out, marks=True, cover_cw=True):
    pages = build_pages()
    P = len(pages)
    n_sheets = P // 4
    c = canvas.Canvas(out, pagesize=A4)
    c.setTitle("SJÄLV — AC Assembly Instructions")

    for i in range(1, n_sheets + 1):
        front = [(2 * i - 1, 'lower', 0), (P - 2 * i + 2, 'upper', 0)]
        back = [(2 * i, 'lower', 180), (P - 2 * i + 1, 'upper', 180)]
        for side, slots in (("front", front), ("back", back)):
            for pno, half, rot in slots:
                place(c, pages[pno - 1], half, rot,
                      f"p.{pno}  ·  sheet {i} {side} {half}", marks, cover_cw)
            if marks:
                c.saveState()
                c.setDash(4, 4)
                c.setLineWidth(0.5)
                c.setStrokeGray(0.65)
                c.line(0, HALF_H, SHEET_W, HALF_H)
                c.setFont("Helvetica", 6)
                c.setFillGray(0.55)
                c.drawCentredString(SHEET_W / 2, HALF_H + 3, "F O L D")
                c.restoreState()
            c.showPage()
    c.save()
    print("wrote", out, f"({n_sheets} sheets / {n_sheets * 2} PDF pages)")


BLEED = 3 * mm


def print_shop(out, cover_cw=True):
    """Twelve single A5-landscape pages with 3 mm bleed, in reading order.

    This is the file a commercial printer wants: they run their own imposition,
    so they must NOT be sent the A4 duplex file.  Trim is 210x148 mm inside a
    216x154 mm media box; nothing in the artwork bleeds off (the ground is
    white), so the bleed is simply white margin, and every element already sits
    well inside the 4 mm safety line.
    """
    pages = build_pages()
    c = canvas.Canvas(out, pagesize=(SHEET_W + 2 * BLEED, HALF_H + 2 * BLEED))
    c.setTitle("SJÄLV — AC Assembly Instructions (print, 3mm bleed)")
    for p in pages:
        c.saveState()
        c.translate(BLEED, BLEED)
        paint(c, p, cover_cw)
        c.restoreState()
        c.showPage()
    c.save()
    print("wrote", out, f"({len(pages)} pages, {SHEET_W/mm:.0f}x{HALF_H/mm:.0f}mm "
          f"trim + {BLEED/mm:.0f}mm bleed)")


def reading_order(out, cover_cw=True):
    """12 A5-landscape pages in reading order — for proofing, or for a
    printer's own booklet mode."""
    pages = build_pages()
    c = canvas.Canvas(out, pagesize=(SHEET_W, HALF_H))
    c.setTitle("SJÄLV — reading order")
    for p in pages:
        paint(c, p, cover_cw)
        c.showPage()
    c.save()
    print("wrote", out, f"({len(pages)} pages)")


def outline_fonts(path):
    """Convert all text to vector paths — MANDATORY for the print-shop file.

    ReportLab draws with the PDF base-14 fonts (Helvetica, Helvetica-Bold,
    Times-Roman) and, by design, never embeds them. Print shops reject that:
    WIRmachenDRUCK held Auftrag 12831205-1 on 2026-08-05 with "in Ihrem
    PDF-Dokument sind einige Schriften nicht eingebettet ... alternativ koennen
    Sie die Schriften gerne in Pfade umwandeln". This is that second option,
    which is the safer one here because it preserves the approved appearance
    exactly instead of swapping in a different embedded typeface.

    Verified 2026-08-05: 12 pages, MediaBox unchanged at 216 x 154.5 mm, all
    raster art bit-identical at full resolution, QR still decodes to the Zenodo
    concept DOI, and every page pixel-identical except sub-pixel glyph
    rendering on the all-text back cover.
    """
    import shutil
    import subprocess
    if shutil.which("gs") is None:
        print(f"!! ghostscript not found — {path} STILL HAS UNEMBEDDED FONTS, "
              f"do not send it to a print shop")
        return
    tmp = path + ".outlined"
    subprocess.run([
        "gs", "-q", "-dNOPAUSE", "-dBATCH", "-sDEVICE=pdfwrite",
        "-dNoOutputFonts",
        # never let ghostscript touch the artwork: the sources are already at
        # 222 dpi, which MG ruled sufficient, and there is nothing to spare.
        "-dDownsampleColorImages=false", "-dDownsampleGrayImages=false",
        "-dDownsampleMonoImages=false",
        "-dAutoFilterColorImages=false", "-dAutoFilterGrayImages=false",
        "-dColorImageFilter=/FlateEncode", "-dGrayImageFilter=/FlateEncode",
        "-dColorConversionStrategy=/LeaveColorUnchanged",
        "-dCompatibilityLevel=1.4",
        "-o", tmp, path,
    ], check=True)
    os.replace(tmp, path)

    # Fail loudly rather than shipping a file a shop will bounce again.
    try:
        import fitz
    except ImportError:
        print(f"outlined {path} (install PyMuPDF to auto-verify)")
        return
    doc = fitz.open(path)
    leftover = {f[3] for page in doc for f in page.get_fonts(full=True)}
    doc.close()
    if leftover:
        raise SystemExit(f"FONT OUTLINING FAILED for {path}: still present {leftover}")
    print(f"outlined {path} — 0 fonts remain, safe for the print shop")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-marks", action="store_true",
                    help="drop the fold line and p.N test marks")
    ap.add_argument("--cover-ccw", action="store_true",
                    help="turn the cover and back cover the other way")
    a = ap.parse_args()
    cw = not a.cover_ccw
    impose("sjalv-booklet-A4-duplex.pdf", marks=not a.no_marks, cover_cw=cw)
    impose("sjalv-booklet-A4-duplex-clean.pdf", marks=False, cover_cw=cw)
    reading_order("sjalv-reading-order-A5.pdf", cover_cw=cw)
    shop_file = "sjalv-printshop-A5-bleed.pdf"
    print_shop(shop_file, cover_cw=cw)
    # The print-shop file is the only one that leaves the house — outline it.
    # The A4 duplex and reading-order files are for the home printer, where
    # base-14 substitution is fine.
    outline_fonts(shop_file)
