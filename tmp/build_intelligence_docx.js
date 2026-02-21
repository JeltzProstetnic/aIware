#!/usr/bin/env node
// Build .docx files for NIdP submission of the intelligence paper
// Creates: 1) Title page with author info  2) Anonymized manuscript

const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Header, Footer,
  AlignmentType, HeadingLevel, PageBreak, PageNumber,
  LevelFormat, ExternalHyperlink, BorderStyle
} = require("docx");

// ── Config ──────────────────────────────────────────────────────────────
const FONT = "Times New Roman";
const SIZE = 24; // 12pt in half-points
const LINE_SPACING = 480; // double spacing (240 = single)
const INDENT_FIRST = 720; // 0.5 inch first-line indent
const RUNNING_HEAD = "INTELLIGENCE AND MOTIVATION";

const TITLE = "Why Intelligence Models Must Include Motivation: A Recursive Framework";
const AUTHOR = "Matthias Gruber";
const AFFILIATION = "Independent Researcher";
const EMAIL = "matthias@matthiasgruber.com";
const ORCID = "0009-0005-9697-1665";

const HIGHLIGHTS = [
  "Major intelligence models systematically exclude motivation as a component",
  "Intelligence is a recursive loop of Knowledge, Performance, and Motivation",
  "Operational knowledge functions as the primary multiplier in this loop",
  "AI systems lack motivation, explaining their absence of self-directed growth",
  "The recursive model predicts intelligence is largely learnable",
];

const KEYWORDS = "intelligence, motivation, recursive systems, operational knowledge, artificial intelligence, CHC theory, Cattell investment theory";

// ── Read and parse the markdown ──────────────────────────────────────────
const md = fs.readFileSync("paper/intelligence/paper.md", "utf-8");

// Extract abstract
const absMatch = md.match(/## Abstract\n\n([\s\S]*?)\n\n\*\*Keywords\*\*/);
const abstractText = absMatch ? absMatch[1].trim() : "";

// Extract body (Section 1 through Section 8, before References)
const bodyStart = md.indexOf("## 1. Introduction");
const refsStart = md.indexOf("## References");
const bodyMd = md.substring(bodyStart, refsStart).trim();

// Extract references
const refsMd = md.substring(refsStart + "## References".length).trim();

// ── Anonymize self-citations ─────────────────────────────────────────────
function anonymize(text) {
  // Replace self-citations — catch all patterns: (Gruber, 2015), Gruber (2015), in Gruber, etc.
  text = text.replace(/\(Gruber,\s*(\d{4})\)/g, "([Author], $1)");
  text = text.replace(/Gruber\s*\((\d{4})\)/g, "[Author] ($1)");
  text = text.replace(/Gruber\s*\(submitted\)/g, "[Author] (submitted)");
  text = text.replace(/Gruber,\s*submitted/g, "[Author], submitted");
  text = text.replace(/in Gruber/g, "in [Author]");
  // In references section
  text = text.replace(/^Gruber, M\./gm, "[Author].");
  return text;
}

// ── Parse inline formatting ──────────────────────────────────────────────
function parseInline(text) {
  const runs = [];
  // Split on bold (**...**) and italic (*...* but not **) patterns
  const regex = /(\*\*\*(.+?)\*\*\*|\*\*(.+?)\*\*|\*(.+?)\*)/g;
  let lastIndex = 0;
  let match;

  while ((match = regex.exec(text)) !== null) {
    // Add text before match
    if (match.index > lastIndex) {
      runs.push(new TextRun({
        text: text.substring(lastIndex, match.index),
        font: FONT, size: SIZE
      }));
    }
    if (match[2]) {
      // Bold italic (***...***)
      runs.push(new TextRun({
        text: match[2], font: FONT, size: SIZE, bold: true, italics: true
      }));
    } else if (match[3]) {
      // Bold (**...**)
      runs.push(new TextRun({
        text: match[3], font: FONT, size: SIZE, bold: true
      }));
    } else if (match[4]) {
      // Italic (*...*)
      runs.push(new TextRun({
        text: match[4], font: FONT, size: SIZE, italics: true
      }));
    }
    lastIndex = match.index + match[0].length;
  }
  // Add remaining text
  if (lastIndex < text.length) {
    runs.push(new TextRun({
      text: text.substring(lastIndex),
      font: FONT, size: SIZE
    }));
  }
  if (runs.length === 0) {
    runs.push(new TextRun({ text: text, font: FONT, size: SIZE }));
  }
  return runs;
}

// ── Parse markdown body into paragraphs ──────────────────────────────────
function parseBody(mdText, doAnonymize = false) {
  if (doAnonymize) mdText = anonymize(mdText);

  const lines = mdText.split("\n");
  const paragraphs = [];
  let i = 0;

  while (i < lines.length) {
    const line = lines[i];

    // Skip horizontal rules
    if (line.match(/^---\s*$/)) { i++; continue; }

    // Empty line = skip
    if (line.trim() === "") { i++; continue; }

    // Level 1 heading: ## X. Title (APA Level 1: centered, bold)
    const h1 = line.match(/^## (\d+\.\s+.+)$/);
    if (h1) {
      paragraphs.push(new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 240, after: 0, line: LINE_SPACING },
        children: [new TextRun({
          text: h1[1], font: FONT, size: SIZE, bold: true
        })]
      }));
      i++; continue;
    }

    // Level 2 heading: ### X.Y Title (APA Level 2: flush left, bold)
    const h2 = line.match(/^### (\d+\.\d+\s+.+)$/);
    if (h2) {
      paragraphs.push(new Paragraph({
        spacing: { before: 240, after: 0, line: LINE_SPACING },
        children: [new TextRun({
          text: h2[1], font: FONT, size: SIZE, bold: true
        })]
      }));
      i++; continue;
    }

    // Generic ## heading (for Abstract, References, Conclusion, Discussion)
    const hGen = line.match(/^## (.+)$/);
    if (hGen) {
      paragraphs.push(new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 240, after: 0, line: LINE_SPACING },
        children: [new TextRun({
          text: hGen[1], font: FONT, size: SIZE, bold: true
        })]
      }));
      i++; continue;
    }

    // Generic ### heading
    const hGen2 = line.match(/^### (.+)$/);
    if (hGen2) {
      paragraphs.push(new Paragraph({
        spacing: { before: 240, after: 0, line: LINE_SPACING },
        children: [new TextRun({
          text: hGen2[1], font: FONT, size: SIZE, bold: true
        })]
      }));
      i++; continue;
    }

    // Numbered list items (1. **text**: ...)
    const numItem = line.match(/^(\d+)\.\s+(.+)$/);
    if (numItem) {
      const content = numItem[2];
      paragraphs.push(new Paragraph({
        spacing: { line: LINE_SPACING },
        indent: { left: 720, hanging: 360 },
        children: [
          new TextRun({ text: numItem[1] + ". ", font: FONT, size: SIZE }),
          ...parseInline(content)
        ]
      }));
      i++; continue;
    }

    // Bullet list items (- **text**: ...)
    if (line.match(/^-\s+/)) {
      const content = line.replace(/^-\s+/, "");
      paragraphs.push(new Paragraph({
        spacing: { line: LINE_SPACING },
        indent: { left: 720, hanging: 360 },
        children: [
          new TextRun({ text: "\u2022 ", font: FONT, size: SIZE }),
          ...parseInline(content)
        ]
      }));
      i++; continue;
    }

    // Regular paragraph — collect continuation lines
    let para = line;
    i++;
    // Don't merge with next line (markdown uses single newlines as line breaks in some contexts)

    paragraphs.push(new Paragraph({
      spacing: { line: LINE_SPACING },
      indent: { firstLine: INDENT_FIRST },
      children: parseInline(para)
    }));
  }

  return paragraphs;
}

// ── Parse references ─────────────────────────────────────────────────────
function parseReferences(refText, doAnonymize = false) {
  if (doAnonymize) refText = anonymize(refText);

  const refs = refText.split("\n\n").filter(r => r.trim());
  return refs.map(ref => new Paragraph({
    spacing: { line: LINE_SPACING },
    indent: { left: 720, hanging: 720 }, // APA hanging indent
    children: parseInline(ref.trim())
  }));
}

// ── Running header + page number ─────────────────────────────────────────
function makeHeader(text) {
  return new Header({
    children: [new Paragraph({
      alignment: AlignmentType.LEFT,
      spacing: { line: 240 },
      children: [
        new TextRun({ text: text + "\t", font: FONT, size: SIZE }),
      ],
      tabStops: [{
        type: "right",
        position: 9360 // right margin position
      }],
    })]
  });
}

function makeHeaderWithPage(text) {
  return new Header({
    children: [new Paragraph({
      spacing: { line: 240 },
      tabStops: [{ type: "right", position: 9360 }],
      children: [
        new TextRun({ text: text, font: FONT, size: SIZE }),
        new TextRun({ text: "\t", font: FONT, size: SIZE }),
        new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: SIZE }),
      ]
    })]
  });
}

// ── Build Title Page Document ────────────────────────────────────────────
async function buildTitlePage() {
  const doc = new Document({
    styles: {
      default: {
        document: {
          run: { font: FONT, size: SIZE }
        }
      }
    },
    sections: [{
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
        }
      },
      headers: {
        default: makeHeaderWithPage(RUNNING_HEAD)
      },
      children: [
        // Blank lines for vertical centering
        ...Array(6).fill(null).map(() => new Paragraph({
          spacing: { line: LINE_SPACING },
          children: [new TextRun({ text: "", font: FONT, size: SIZE })]
        })),
        // Title
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { line: LINE_SPACING },
          children: [new TextRun({
            text: TITLE, font: FONT, size: SIZE, bold: true
          })]
        }),
        // Blank line
        new Paragraph({ spacing: { line: LINE_SPACING }, children: [] }),
        // Author
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { line: LINE_SPACING },
          children: [new TextRun({ text: AUTHOR, font: FONT, size: SIZE })]
        }),
        // Affiliation
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { line: LINE_SPACING },
          children: [new TextRun({ text: AFFILIATION, font: FONT, size: SIZE })]
        }),
        // Blank line
        new Paragraph({ spacing: { line: LINE_SPACING }, children: [] }),
        // ORCID
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { line: LINE_SPACING },
          children: [new TextRun({
            text: "ORCID: " + ORCID, font: FONT, size: SIZE
          })]
        }),
        // Email
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { line: LINE_SPACING },
          children: [new TextRun({
            text: "Correspondence: " + EMAIL, font: FONT, size: SIZE
          })]
        }),
        // Author Note - page break
        new Paragraph({ children: [new PageBreak()] }),
        // Author Note
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { line: LINE_SPACING, after: 240 },
          children: [new TextRun({
            text: "Author Note", font: FONT, size: SIZE, bold: true
          })]
        }),
        new Paragraph({
          spacing: { line: LINE_SPACING },
          indent: { firstLine: INDENT_FIRST },
          children: [new TextRun({
            text: "Matthias Gruber has no institutional affiliation. He is an independent researcher and R&D AI Transformation Manager at Ivoclar AG, Schaan, Liechtenstein. He has no conflicts of interest to disclose.",
            font: FONT, size: SIZE
          })]
        }),
        new Paragraph({
          spacing: { line: LINE_SPACING },
          indent: { firstLine: INDENT_FIRST },
          children: [new TextRun({
            text: "Correspondence concerning this article should be addressed to Matthias Gruber, Email: " + EMAIL,
            font: FONT, size: SIZE
          })]
        }),
        // Highlights - page break
        new Paragraph({ children: [new PageBreak()] }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { line: LINE_SPACING, after: 240 },
          children: [new TextRun({
            text: "Article Highlights", font: FONT, size: SIZE, bold: true
          })]
        }),
        ...HIGHLIGHTS.map(h => new Paragraph({
          spacing: { line: LINE_SPACING },
          indent: { left: 720, hanging: 360 },
          children: [
            new TextRun({ text: "\u2022 ", font: FONT, size: SIZE }),
            new TextRun({ text: h, font: FONT, size: SIZE })
          ]
        })),
      ]
    }]
  });

  const buffer = await Packer.toBuffer(doc);
  fs.writeFileSync("paper/intelligence/title-page.docx", buffer);
  console.log("Created: paper/intelligence/title-page.docx");
}

// ── Build Anonymized Manuscript ──────────────────────────────────────────
async function buildManuscript() {
  const bodyParagraphs = parseBody(bodyMd, true);
  const refParagraphs = parseReferences(refsMd, true);
  const anonAbstract = anonymize(abstractText);

  const doc = new Document({
    styles: {
      default: {
        document: {
          run: { font: FONT, size: SIZE }
        }
      }
    },
    sections: [{
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
        }
      },
      headers: {
        default: makeHeaderWithPage(RUNNING_HEAD)
      },
      children: [
        // Title (centered, bold) - no author info
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { line: LINE_SPACING, after: 240 },
          children: [new TextRun({
            text: TITLE, font: FONT, size: SIZE, bold: true
          })]
        }),
        // Abstract heading
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { line: LINE_SPACING, before: 240 },
          children: [new TextRun({
            text: "Abstract", font: FONT, size: SIZE, bold: true
          })]
        }),
        // Abstract text (no first-line indent per APA)
        new Paragraph({
          spacing: { line: LINE_SPACING },
          children: parseInline(anonAbstract)
        }),
        // Keywords
        new Paragraph({
          spacing: { line: LINE_SPACING },
          indent: { firstLine: INDENT_FIRST },
          children: [
            new TextRun({ text: "Keywords: ", font: FONT, size: SIZE, italics: true }),
            new TextRun({ text: KEYWORDS, font: FONT, size: SIZE, italics: true })
          ]
        }),
        // Page break before body
        new Paragraph({ children: [new PageBreak()] }),
        // Re-state title at start of body (APA requirement)
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { line: LINE_SPACING, after: 240 },
          children: [new TextRun({
            text: TITLE, font: FONT, size: SIZE, bold: true
          })]
        }),
        // Body
        ...bodyParagraphs,
        // References - page break
        new Paragraph({ children: [new PageBreak()] }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { line: LINE_SPACING, after: 240 },
          children: [new TextRun({
            text: "References", font: FONT, size: SIZE, bold: true
          })]
        }),
        ...refParagraphs,
      ]
    }]
  });

  const buffer = await Packer.toBuffer(doc);
  fs.writeFileSync("paper/intelligence/manuscript-anonymous.docx", buffer);
  console.log("Created: paper/intelligence/manuscript-anonymous.docx");
}

// ── Run ──────────────────────────────────────────────────────────────────
(async () => {
  try {
    await buildTitlePage();
    await buildManuscript();
    console.log("\nDone. Two files created in paper/intelligence/");
    console.log("- title-page.docx (with author info, highlights)");
    console.log("- manuscript-anonymous.docx (double-blind ready)");
  } catch (err) {
    console.error("Error:", err);
    process.exit(1);
  }
})();
