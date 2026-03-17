const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, AlignmentType, HeadingLevel,
        Header, Footer, PageNumber, PageBreak } = require("docx");

const doc = new Document({
  styles: {
    default: {
      document: {
        run: { font: "Times New Roman", size: 24 } // 12pt
      }
    },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: "Times New Roman" },
        paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 0 }
      },
      {
        id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, font: "Times New Roman" },
        paragraph: { spacing: { before: 200, after: 100 }, outlineLevel: 1 }
      },
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 }, // US Letter
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.RIGHT,
          children: [new TextRun({ text: "Review Proposal \u2014 Gruber", italics: true, size: 20, font: "Times New Roman" })]
        })]
      })
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [new TextRun({ children: [PageNumber.CURRENT], size: 20, font: "Times New Roman" })]
        })]
      })
    },
    children: [
      // Title
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 120 },
        children: [new TextRun({
          text: "Review Proposal: The Four-Model Theory of Consciousness \u2014 A Criticality-Based Framework with Independent Empirical Confirmation",
          bold: true, size: 28, font: "Times New Roman"
        })]
      }),
      // Author
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 60 },
        children: [new TextRun({ text: "Matthias Gruber", size: 24, font: "Times New Roman" })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 60 },
        children: [new TextRun({ text: "Independent researcher", italics: true, size: 22, font: "Times New Roman" })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 60 },
        children: [new TextRun({ text: "ORCID: 0009-0005-9697-1665", size: 22, font: "Times New Roman" })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 240 },
        children: [new TextRun({ text: "matthias@matthiasgruber.com", size: 22, font: "Times New Roman" })]
      }),

      // Proposed review
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun("Proposed Review")]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun(
          "This proposal concerns a review article presenting the Four-Model Theory of Consciousness (FMT), " +
          "a framework that derives consciousness from self-simulation at criticality. The theory, originally " +
          "published in 2015 (Gruber, 2015), proposes that consciousness is constituted by ongoing self-simulation " +
          "across four nested models arranged along two orthogonal axes \u2014 scope (world vs. self) and mode " +
          "(implicit/substrate-level vs. explicit/phenomenal) \u2014 operating on a substrate at the edge of chaos. " +
          "The review presents the theory, demonstrates its explanatory range across psychopharmacology, sleep science, " +
          "clinical neurology, and comparative cognition, and documents its empirical track record."
        )]
      }),

      // Why PLREV
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun("Suitability for Physics of Life Reviews")]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun(
          "The Four-Model Theory is grounded in the physics of complex systems. Its central physical commitment " +
          "\u2014 that consciousness requires the substrate to operate at the edge of chaos (Wolfram Class 4 dynamics) " +
          "\u2014 was derived from Wolfram\u2019s computational universality framework (Wolfram, 2002), independently of " +
          "the neuroscience criticality program that was already underway (Beggs & Plenz, 2003). The theory treats the " +
          "cortex as a high-dimensional cellular automaton whose criticality regime determines whether consciousness " +
          "is possible, and frames qualia as constitutive properties of the computational level \u2014 dissolving the " +
          "Hard Problem through a level distinction analogous to the relationship between a program and its hardware. " +
          "This physics-of-computation approach places the work squarely within the journal\u2019s scope of " +
          "\u201cphysics of living systems\u201d and \u201ccomplex phenomena in biological systems.\u201d"
        )]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun(
          "The review\u2019s interdisciplinary reach \u2014 spanning dynamical systems theory, computational neuroscience, " +
          "psychopharmacology, sleep physiology, clinical neurology, and philosophy of mind \u2014 aligns with the " +
          "journal\u2019s mission as \u201ca unifying force going across barriers between disciplines.\u201d"
        )]
      }),

      // Empirical grounding
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun("Empirical Grounding")]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun(
          "Unusually for a consciousness theory, the framework has substantial independent empirical confirmation. " +
          "Five claims that follow from the theory\u2019s core axioms \u2014 established in 2015 \u2014 have since been " +
          "independently confirmed by research groups with no connection to the theory:"
        )]
      }),
      new Paragraph({
        spacing: { after: 100 },
        children: [
          new TextRun({ text: "Anesthetic-criticality convergence. ", bold: true }),
          new TextRun(
            "The theory predicts that all agents abolishing consciousness push the substrate below the criticality " +
            "threshold, regardless of receptor mechanism. This has been confirmed by the PCI threshold of 0.31 " +
            "(Casali et al., 2013), the ConCrit framework (Algom & Shriki, 2026), and Hengen and Shew\u2019s (2025) " +
            "meta-analysis of 140 datasets."
          )
        ]
      }),
      new Paragraph({
        spacing: { after: 100 },
        children: [
          new TextRun({ text: "Sleep-dependent criticality restoration. ", bold: true }),
          new TextRun(
            "The theory predicts that waking degrades criticality and sleep restores it. Bhatt et al. (2024, " +
            "Nature Neuroscience) confirmed this in continuous multi-day recordings."
          )
        ]
      }),
      new Paragraph({
        spacing: { after: 100 },
        children: [
          new TextRun({ text: "Sleep onset as bifurcation. ", bold: true }),
          new TextRun(
            "The theory predicts sleep onset is a radical transition, not gradual dimming. Li et al. (2025, " +
            "Nature Neuroscience) demonstrated a predictable bifurcation tipping point in over 1,000 participants."
          )
        ]
      }),
      new Paragraph({
        spacing: { after: 100 },
        children: [
          new TextRun({ text: "Psychedelic content maps the processing hierarchy. ", bold: true }),
          new TextRun(
            "The theory\u2019s permeability principle predicts hierarchical content emergence under psychedelics, " +
            "consistent with Carhart-Harris and Friston\u2019s (2019) REBUS model and dose-dependent visual cortex " +
            "effects (Timmermann et al., 2023)."
          )
        ]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [
          new TextRun({ text: "Split-brain holographic degradation. ", bold: true }),
          new TextRun(
            "The theory predicts bilateral degradation rather than clean hemispheric specialization after " +
            "callosotomy, consistent with Pinto et al.\u2019s (2017) finding of unified consciousness with split perception."
          )
        ]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun(
          "This track record \u2014 axioms established a decade before the confirming data, confirmed by independent " +
          "groups \u2014 is rare among consciousness theories. Most empirical work in consciousness science involves " +
          "post-hoc correlation of neural measures with existing theories, not consequences derived from first " +
          "principles and subsequently confirmed by unrelated research programs."
        )]
      }),

      // Core theoretical contribution
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun("Core Theoretical Contribution")]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun(
          "The review\u2019s central theoretical contribution is a dissolution of the Hard Problem of consciousness " +
          "(Chalmers, 1995) through a two-level ontology. The theory distinguishes between a real level (the physical " +
          "substrate and its implicit models \u2014 synaptic weights encoding world-knowledge and self-knowledge) and " +
          "a virtual level (the explicit models \u2014 the ongoing simulation that constitutes experience). Qualia are " +
          "constitutive properties of the virtual level: they exist at the level of the running computation but are " +
          "incoherent at the substrate level, just as a spreadsheet cell\u2019s value is incoherent at the transistor " +
          "level. The Hard Problem dissolves because it rests on a category error \u2014 seeking phenomenal properties " +
          "at the substrate level where they categorically do not exist. Self-referential closure (the system\u2019s " +
          "model includes a model of itself) explains why this specific computation has experience when a weather " +
          "simulation does not."
        )]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun(
          "The theory belongs to the self-modeling tradition in consciousness studies (Metzinger, 2003; Damasio, " +
          "1999; Seth, 2021; Graziano, 2013; Hofstadter, 2007) but extends it in three ways: it specifies the " +
          "minimal architecture (four model kinds along two axes \u2014 a 2\u00D72 taxonomy that defines the floor, " +
          "not the ceiling, for consciousness), adds a physical prerequisite (criticality), and develops the " +
          "two-level ontology that dissolves the Hard Problem. The review systematically compares the theory against " +
          "seven competing frameworks (IIT, GNW, HOT, PP, AST, RPT, ConCrit) across all eight requirements."
        )]
      }),

      // Novel predictions
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun("Novel Predictions")]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun(
          "Beyond the confirmed claims, the review presents four novel, currently untested predictions with " +
          "clear falsification criteria: (1) that psychedelics should alleviate anosognosia by globally increasing " +
          "implicit-explicit permeability, compensating for the local block that causes deficit unawareness \u2014 " +
          "a cross-domain surprise prediction connecting psychopharmacology and clinical neurology through a single " +
          "mechanism; (2) that ego dissolution content during psychedelic experiences tracks the dominant sensory " +
          "input, allowing identity content to be predicted and directed; (3) that DID alter switches produce " +
          "neural reconfigurations concentrated in self-model (default mode) networks rather than diffusely " +
          "distributed; and (4) that lucid dream onset corresponds to a step-like criticality threshold crossing " +
          "originating in self-model cortical regions. No competing consciousness theory generates predictions " +
          "1 or 2."
        )]
      }),

      // Structure
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun("Review Structure")]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun(
          "The proposed review (~17,000 words, 3 figures, ~85 references) is structured as follows. " +
          "It establishes eight core requirements for a theory of consciousness, then presents the Four-Model Theory " +
          "and its philosophical commitments (process physicalism, weak emergence, substrate independence). " +
          "It develops the criticality and binding framework, demonstrates explanatory range across six domains " +
          "(psychedelic phenomenology, anesthesia, dreams, split-brain, animal consciousness, clinical disorders), " +
          "provides a systematic comparison against seven competing theories (IIT, GNW, HOT, PP, AST, RPT, ConCrit), " +
          "presents the empirical convergence evidence and four novel predictions, and addresses open questions " +
          "including the need for mathematical formalization. A preprint is available on Zenodo " +
          "(DOI: 10.5281/zenodo.19064950)."
        )]
      }),

      // Significance
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun("Significance")]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun(
          "The consciousness field is at an impasse. The COGITATE adversarial collaboration (2025) produced " +
          "equivocal results for both IIT and GNW. Over 100 researchers have declared IIT pseudoscientific. " +
          "No theory commands broad assent. The Four-Model Theory offers a way forward by grounding consciousness " +
          "in the physics of critical phenomena \u2014 connecting the philosophical questions (why is there experience?) " +
          "to the empirical program (criticality as a measurable, manipulable property) through a specific " +
          "architectural specification (four models at criticality). The theory\u2019s demonstrated empirical " +
          "grounding and its implications for artificial consciousness make it directly relevant to current debates " +
          "about machine consciousness and AI welfare (Butlin et al., 2023, 2025; Long et al., 2024)."
        )]
      }),

      // Keywords
      new Paragraph({
        spacing: { before: 200, after: 400 },
        children: [
          new TextRun({ text: "Keywords: ", bold: true }),
          new TextRun("consciousness, criticality, self-model, cellular automaton, hard problem, " +
            "qualia, binding problem, psychedelics, substrate independence, artificial consciousness")
        ]
      }),

      // AI declaration
      new Paragraph({
        spacing: { after: 120 },
        children: [new TextRun({
          text: "Declaration of generative AI and AI-assisted technologies in the manuscript preparation process",
          bold: true, italics: true, size: 24
        })]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun(
          "During the preparation of this work the author used Claude (Anthropic) in order to conduct " +
          "structured adversarial challenges against the theory, assist with literature search and citation " +
          "verification, and refine editorial presentation. The underlying theory was developed in 2015 " +
          "without AI assistance, predating current generative AI capabilities. After using this tool, the " +
          "author reviewed and edited the content as needed and takes full responsibility for the content " +
          "of the published article."
        )]
      }),
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/home/jeltz/aIware/tmp/plrev-proposal/plrev-review-proposal.docx", buffer);
  console.log("Done: plrev-review-proposal.docx");
});
