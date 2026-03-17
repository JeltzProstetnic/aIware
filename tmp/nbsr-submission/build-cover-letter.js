const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, AlignmentType } = require("docx");

const today = "March 17, 2026";

const doc = new Document({
  styles: {
    default: {
      document: { run: { font: "Times New Roman", size: 24 } }
    }
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    children: [
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun(today)]
      }),
      new Paragraph({
        spacing: { after: 100 },
        children: [new TextRun("Editor-in-Chief")]
      }),
      new Paragraph({
        spacing: { after: 100 },
        children: [new TextRun({ text: "Neuroscience & Biobehavioral Reviews", italics: true })]
      }),
      new Paragraph({
        spacing: { after: 400 },
        children: []
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun("Dear Editor,")]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun(
          "Please consider the enclosed manuscript, \u201CThe Four-Model Theory of Consciousness: " +
          "A Simulation-Based Framework Unifying the Hard Problem, Binding, and Altered States,\u201D " +
          "for publication as a theoretical review in Neuroscience & Biobehavioral Reviews."
        )]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun(
          "The paper presents a comprehensive theory of consciousness grounded in self-simulation at " +
          "criticality. It proposes that consciousness is constituted by ongoing self-simulation across " +
          "four nested models (implicit/explicit \u00D7 world/self) operating on a substrate at the edge " +
          "of chaos. The theory dissolves the Hard Problem through a two-level ontology in which qualia " +
          "are constitutive properties of the computational level, and derives diverse phenomena \u2014 " +
          "psychedelic states, anesthesia, dreams, split-brain, dissociative identity disorder, and animal " +
          "consciousness \u2014 from five principles."
        )]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun(
          "The manuscript is particularly suited to your journal for two reasons. First, its criticality " +
          "framework directly engages with work recently published in Neuroscience & Biobehavioral Reviews, " +
          "including the ConCrit framework (Algom & Shriki, 2026). The theory\u2019s criticality requirement " +
          "was derived independently from Wolfram\u2019s computational framework in 2015, and the subsequent " +
          "empirical consolidation \u2014 including Hengen and Shew\u2019s (2025) meta-analysis of 140 datasets " +
          "and Bhatt et al.\u2019s (2024) sleep-criticality work in Nature Neuroscience \u2014 confirms its core " +
          "commitment. Second, the paper functions as a systematic theoretical review: it surveys eight " +
          "requirements for a theory of consciousness, compares seven competing frameworks, and proposes " +
          "a unifying synthesis."
        )]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun(
          "Unusually for a consciousness theory, the framework has substantial independent empirical " +
          "grounding: five claims that follow from its core axioms \u2014 established in 2015 \u2014 have " +
          "since been independently confirmed by research groups with no connection to the theory, including " +
          "the anesthetic-criticality convergence, sleep-dependent criticality restoration, sleep onset as " +
          "bifurcation (Li et al., 2025, Nature Neuroscience), and split-brain holographic degradation. " +
          "Four novel predictions remain untested, including that psychedelics should alleviate anosognosia " +
          "and that ego dissolution content tracks dominant sensory input \u2014 predictions no competing " +
          "theory generates."
        )]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun(
          "A preprint is available on Zenodo (DOI: 10.5281/zenodo.19064950). The manuscript has not been " +
          "published and is not under consideration for publication at any other journal. AI tools (Claude, Anthropic) were " +
          "used for adversarial challenge, editorial refinement, and literature search; the theory itself " +
          "was developed without AI assistance (2015, pre-dating current AI capabilities)."
        )]
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun("Thank you for your consideration.")]
      }),
      new Paragraph({
        spacing: { after: 100 },
        children: [new TextRun("Sincerely,")]
      }),
      new Paragraph({
        spacing: { after: 100 },
        children: [new TextRun({ text: "Matthias Gruber", bold: true })]
      }),
      new Paragraph({
        spacing: { after: 50 },
        children: [new TextRun("Independent researcher")]
      }),
      new Paragraph({
        spacing: { after: 50 },
        children: [new TextRun("ORCID: 0009-0005-9697-1665")]
      }),
      new Paragraph({
        children: [new TextRun("matthias@matthiasgruber.com")]
      }),
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/home/jeltz/aIware/tmp/nbsr-submission/cover-letter-nbsr.docx", buffer);
  console.log("Done: cover-letter-nbsr.docx");
});
