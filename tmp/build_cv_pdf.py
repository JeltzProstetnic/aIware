#!/usr/bin/env python3
"""Build academic CV PDF for Matthias Gruber — MetaLab Summer School application.
Generates two versions: with photo and without photo."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image,
    HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
import sys

# Paths
PHOTO = "/mnt/c/Users/Matthias/Pictures/1749406479497.jpg"
OUTPUT_PHOTO = "/home/jeltz/aIware/tmp/cv-gruber-matthias-2026-photo.pdf"
OUTPUT_NOPHOTO = "/home/jeltz/aIware/tmp/cv-gruber-matthias-2026.pdf"

# Colors
DARK = HexColor("#1a1a2e")
ACCENT = HexColor("#16213e")
RULE_COLOR = HexColor("#4a4a6a")

# Page setup
PAGE_W, PAGE_H = A4
LEFT_MARGIN = 20*mm
RIGHT_MARGIN = 20*mm
TOP_MARGIN = 15*mm
BOT_MARGIN = 15*mm
CONTENT_W = PAGE_W - LEFT_MARGIN - RIGHT_MARGIN


def build(include_photo):
    output = OUTPUT_PHOTO if include_photo else OUTPUT_NOPHOTO
    doc = SimpleDocTemplate(
        output, pagesize=A4,
        leftMargin=LEFT_MARGIN, rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN, bottomMargin=BOT_MARGIN,
    )

    styles = getSampleStyleSheet()

    s_name = ParagraphStyle("Name", parent=styles["Normal"],
        fontSize=18, leading=22, textColor=DARK, fontName="Helvetica-Bold")
    s_subtitle = ParagraphStyle("Subtitle", parent=styles["Normal"],
        fontSize=10, leading=13, textColor=HexColor("#555555"), fontName="Helvetica")
    s_contact = ParagraphStyle("Contact", parent=styles["Normal"],
        fontSize=8.5, leading=11, textColor=HexColor("#444444"), fontName="Helvetica")
    s_section = ParagraphStyle("Section", parent=styles["Normal"],
        fontSize=11, leading=14, textColor=ACCENT, fontName="Helvetica-Bold",
        spaceBefore=10, spaceAfter=2)
    s_body = ParagraphStyle("Body", parent=styles["Normal"],
        fontSize=9, leading=12, textColor=DARK, fontName="Helvetica",
        alignment=TA_JUSTIFY)
    s_item = ParagraphStyle("Item", parent=s_body,
        leftIndent=0, spaceBefore=2, spaceAfter=1)
    s_item_title = ParagraphStyle("ItemTitle", parent=s_item,
        fontName="Helvetica-Bold", fontSize=9)
    s_small = ParagraphStyle("Small", parent=styles["Normal"],
        fontSize=8, leading=10, textColor=HexColor("#666666"), fontName="Helvetica")
    s_subsection = ParagraphStyle("Subsection", parent=styles["Normal"],
        fontSize=9, leading=12, textColor=HexColor("#333333"), fontName="Helvetica-BoldOblique",
        spaceBefore=4, spaceAfter=1)

    story = []

    # --- HEADER ---
    header_text = [
        Paragraph("Matthias Gruber", s_name),
        Paragraph("Dipl.-Ing. (Biomedical Informatics) &mdash; Independent Consciousness Researcher", s_subtitle),
        Spacer(1, 3),
        Paragraph(
            '<font color="#444444">'
            'matthias@matthiasgruber.com &nbsp;|&nbsp; matthiasgruber.com &nbsp;|&nbsp; '
            'ORCID: 0009-0005-9697-1665'
            '</font>', s_contact),
        Paragraph(
            '<font color="#444444">Bildstein, Austria</font>', s_contact),
    ]

    if include_photo:
        photo = Image(PHOTO, width=28*mm, height=28*mm)
        photo.hAlign = "RIGHT"
        header_table = Table(
            [[header_text, photo]],
            colWidths=[CONTENT_W - 32*mm, 32*mm],
        )
    else:
        header_table = Table(
            [[header_text]],
            colWidths=[CONTENT_W],
        )
    header_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 2*mm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=RULE_COLOR))
    story.append(Spacer(1, 3*mm))

    # --- RESEARCH PROJECT ---
    story.append(Paragraph("RESEARCH PROJECT", s_section))
    story.append(HRFlowable(width="100%", thickness=0.3, color=RULE_COLOR))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph(
        "<b>The Four-Model Theory of Consciousness (FMT)</b>", s_item_title))
    story.append(Paragraph(
        "A simulation-based architecture proposing that consciousness consists of real-time "
        "self-simulation organized along two dimensions: scope (world vs. self) and mode "
        "(implicit/learned vs. explicit/simulated). Generates nine falsifiable predictions "
        "testable with fMRI, EEG, and psychopharmacological methods. Developed 2003&ndash;2015; "
        "formalized for peer review 2024&ndash;2025.",
        s_item))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph(
        "<b>Keywords:</b> <i>consciousness, self-simulation, metacognition, qualia, criticality</i>",
        s_item))
    story.append(Spacer(1, 4*mm))

    # --- PUBLICATIONS ---
    story.append(Paragraph("PUBLICATIONS", s_section))
    story.append(HRFlowable(width="100%", thickness=0.3, color=RULE_COLOR))
    story.append(Spacer(1, 2*mm))

    # Consciousness research
    story.append(Paragraph("Consciousness &amp; Intelligence", s_subsection))
    pubs_consc = [
        ("Gruber, M. (2025)",
         '"The Four-Model Theory: A Simulation-Based Architecture of Consciousness." '
         'Under review, <i>Neuroscience of Consciousness</i>. '
         'Preprint: doi.org/10.5281/zenodo.18669891'),
        ("Gruber, M. (2025)",
         '"Recursive Iteration: A Model of Human and Artificial Intelligence." '
         'Submitted to <i>New Ideas in Psychology</i>. '
         'Preprint: osf.io/preprints/osf/kctvg'),
        ("Gruber, M. (2015)",
         '<i>Die Emergenz des Bewusstseins</i> [The Emergence of Consciousness]. '
         'Monograph, self-published (German). ISBN 978-3-7345-4765-4.'),
    ]
    for author, title in pubs_consc:
        story.append(Paragraph(f"<b>{author}</b> {title}", s_item))
        story.append(Spacer(1, 1.5*mm))

    story.append(Spacer(1, 1*mm))
    story.append(Paragraph("Simulation, AI &amp; Engineering", s_subsection))
    pubs_other = [
        ("Gruber, M. (2010)",
         '<i>A Generic Framework for Discrete Simulation Based Optimization</i>. '
         'Doctoral research, TU Wien. ISBN 978-3838152233.'),
        ("Gruber, M. et al. (2010)",
         '"Anticipatory Production Control: Simulation Based Heuristic Optimization." '
         'In: M&auml;rz et al. (Eds.), <i>Simulation und Optimierung in Produktion und Logistik</i>, Springer.'),
        ("Heinz, E.A., Kunze, K.S., Gruber, M. et al. (2006)",
         '"Using Wearable Sensors for Real-time Recognition Tasks in Games of Martial Arts." '
         '<i>Proc. 2nd IEEE Symposium on Computational Intelligence and Games</i>, pp. 98&ndash;102.'),
    ]
    for author, title in pubs_other:
        story.append(Paragraph(f"<b>{author}</b> {title}", s_item))
        story.append(Spacer(1, 1.5*mm))

    story.append(Spacer(1, 3*mm))

    # --- EDUCATION ---
    story.append(Paragraph("EDUCATION", s_section))
    story.append(HRFlowable(width="100%", thickness=0.3, color=RULE_COLOR))
    story.append(Spacer(1, 2*mm))

    edu = [
        ("2009 &ndash; 2011", "Doctoral research (ABD)", "TU Wien",
         "Discrete Simulation Based Optimization. Supervisor: Prof. Felix Breitenecker. Research published (Springer, 2010)."),
        ("2005 &ndash; 2007", "Dipl.-Ing. Biomedical Informatics", "UMIT, Hall in Tirol",
         "Specialization in bioinformatics and artificial intelligence. Thesis grade: A (96/100)."),
        ("2002 &ndash; 2005", "BSc Medical Informatics", "UMIT, Hall in Tirol",
         "Research assistant in Wearable Computing (Prof. Paul Lukowicz). Thesis grade: B (90/100)."),
        ("1998 &ndash; 2002", "Medical studies (pre-clinical)", "University of Innsbruck",
         "Physics, chemistry, biochemistry, biology, anatomy."),
    ]
    for years, degree, inst, detail in edu:
        story.append(Paragraph(
            f"<b>{years}</b> &nbsp;&nbsp; <b>{degree}</b> &mdash; {inst}", s_item_title))
        story.append(Paragraph(detail, s_small))
        story.append(Spacer(1, 1.5*mm))

    story.append(Spacer(1, 3*mm))

    # --- CONFERENCE ACTIVITY (2026) ---
    story.append(Paragraph("CONFERENCE ACTIVITY (2026)", s_section))
    story.append(HRFlowable(width="100%", thickness=0.3, color=RULE_COLOR))
    story.append(Spacer(1, 2*mm))
    confs = [
        '&bull; "Formalizing the Real-Virtual Gap" &mdash; Neurophenomenology satellite workshop, abstract submitted.',
        '&bull; "Substrate-Independent Consciousness and the Ethics of Artificial Minds" &mdash; AISB Convention, extended abstract submitted.',
    ]
    for c in confs:
        story.append(Paragraph(c, s_item))
        story.append(Spacer(1, 1*mm))

    story.append(Spacer(1, 3*mm))

    # --- RESEARCH RELEVANCE TO METALAB ---
    story.append(Paragraph("RELEVANCE TO CONSCIOUSNESS &amp; METACOGNITION RESEARCH", s_section))
    story.append(HRFlowable(width="100%", thickness=0.3, color=RULE_COLOR))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph(
        "FMT&rsquo;s architecture directly engages current debates in consciousness science. "
        "The explicit self-model (ESM) component provides a structural account of metacognition "
        "&mdash; the system monitoring and evaluating its own cognitive states &mdash; connecting to "
        "Fleming&rsquo;s quality space framework (2024) and the COGITATE adversarial collaboration methodology. "
        "FMT generates a novel 2&times;2 factorial prediction (scope &times; mode) that discriminates between "
        "GNW, IIT, and HOT &mdash; a prediction no current theory makes. The framework also addresses "
        "conditions where metacognitive monitoring fails (dreaming, psychedelics, anesthesia) through "
        "specific predictions about criticality disruption and simulation decoupling.",
        s_item))

    story.append(Spacer(1, 3*mm))

    # --- PROFESSIONAL EXPERIENCE (compressed) ---
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", s_section))
    story.append(HRFlowable(width="100%", thickness=0.3, color=RULE_COLOR))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph(
        "<b>2018 &ndash; present</b> &nbsp;&nbsp; R&amp;D AI Transformation Manager &amp; AI Officer &mdash; Ivoclar AG, Liechtenstein",
        s_item_title))
    story.append(Paragraph(
        "<b>2011 &ndash; 2018</b> &nbsp;&nbsp; Scrum Master / Process Manager &mdash; OMICRON Electronics, Austria",
        s_item_title))
    story.append(Spacer(1, 1*mm))
    story.append(Paragraph(
        "<b>2009 &ndash; 2011</b> &nbsp;&nbsp; Research Scientist &mdash; V-Research GmbH, Austria",
        s_item_title))
    story.append(Paragraph(
        "Discrete simulation, semantics, text mining. Guest lectures at TU Wien.", s_small))
    story.append(Spacer(1, 1*mm))
    story.append(Paragraph(
        "<b>2007 &ndash; 2009</b> &nbsp;&nbsp; Research Project Manager &mdash; PROFACTOR GmbH, Austria",
        s_item_title))
    story.append(Paragraph(
        "Managed ~&euro;5M in research projects (voestalpine, Novartis, Roche). FFG award.", s_small))

    story.append(Spacer(1, 3*mm))

    # --- ADDITIONAL ---
    story.append(Paragraph("ADDITIONAL", s_section))
    story.append(HRFlowable(width="100%", thickness=0.3, color=RULE_COLOR))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph(
        "<b>Languages:</b> German (native), English (fluent), French (basic)", s_item))
    story.append(Paragraph(
        "<b>Technical:</b> Python, C#/.NET, AI/ML systems, simulation modeling", s_item))
    story.append(Paragraph(
        "<b>Certifications:</b> PPL(A) pilot license, ICAO English Level 6; "
        "Court-approved expert for software development (Austria)", s_item))

    doc.build(story)
    print(f"CV written to {output}")


if __name__ == "__main__":
    build(include_photo=True)
    build(include_photo=False)
