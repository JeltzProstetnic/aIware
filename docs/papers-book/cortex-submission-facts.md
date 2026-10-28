# Cortex (Elsevier), Viewpoint: submission facts (verified S356, 2026-10-23)

Sources, read live in the Playwright MCP Chrome (headless chrome and curl both get Cloudflare 403/1000):
sciencedirect.com/journal/cortex/publish/guide-for-authors and /publish/open-access-options.

- **System**: Editorial Manager at `https://www.editorialmanager.com/cortex/Default.aspx` (the "Submit your article" link on the guide).
- **Article type**: **Viewpoint**. The guide says Viewpoints "Are mini-review, position papers on relevant topics which do not report new experimental data. They can be submitted spontaneously or invited by editors." **No word or reference limit is stated** for Viewpoints. Reviews and Research reports say "No word or reference limit" explicitly.
- **Review type**: **Single anonymized**: "This journal follows a single anonymized review process." Editors screen first, then usually at least two reviewers. ⇒ **No anonymised kit is needed.** Names and affiliation go on the title page and in the manuscript.
- **Title page (required)**: title; author given and family names; affiliation with full postal address and country; corresponding author with e-mail (**the e-mail is published**); present address if it changed.
- **Abstract**: required, **≤ 250 words**. A cited reference in the abstract must be given in full.
- **Keywords**: required, **1–7**, English, single words preferred, abbreviations only if well established.
- **Highlights**: encouraged, not required. **3–5 bullets, ≤ 85 characters each including spaces**, uploaded as a separate editable file with "highlights" in the file name.
- **Graphical abstract**: encouraged. At least 1328 px wide, readable at 13 cm, separate file.
- **File format**: editable source, **.docx or .tex**. "A PDF is not an acceptable source file." Word files single-column; double-column allowed only for LaTeX. Remove strikethrough and underline.
- **Figures**: separate files, cited in the text, numbered in order. AI tools may be used for explanatory diagrams and data visualisations but not for primary research images (Elsevier GenAI policy).
- **Structure**: numbered sections (1, 1.1, 1.1.1); the abstract sits outside the numbering. Acknowledgements go in their own section **directly before the references**, never on the title page or in a title footnote. **CRediT** author-contribution statement required.
- **References**: "This journal does not set strict requirements on reference formatting at submission": any consistent style with complete data; DOIs where available. Journal style is applied at proof. Every reference must be a real, existing source.
- **Declarations**: competing interests via the Elsevier declaration tool, uploaded as .doc/.docx ("I have nothing to declare" if none). Funding statement required; if none: "This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors."
- **Generative AI**: declare at submission in a new section **before the reference list**, titled *"Declaration of generative AI and AI-assisted technologies in the manuscript preparation process"*, with the statement "During the preparation of this work the author(s) used [NAME OF TOOL/SERVICE] to [REASON]. After using this tool/service, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the published article." The statement is published. The guide continues "The declaration does not apply to…". The exempted uses were not read (UNVERIFIED). Declare in any case.
- **Data**: Option C research-data policy: deposit, cite and link the data, or explain why it can't be shared. **A data statement is required at submission.** The submission checklist adds that **empirical articles** must meet Cortex's transparency standards (data, code, materials, preregistration). ⇒ After S356-D3 the Viewpoint carries no reanalysis, and its data statement reads "No data were used for the research described in the article."
- **Preprints**: "Sharing preprints, such as on a preprint server, will not count as prior publication." The submission declaration allows prior publication "in the form of a preprint". ⇒ A Zenodo deposit first is fine.
- **Fees**: hybrid. **Subscription route: no fee.** Gold OA APC **USD 3,710** (excl. taxes, "All articles"), personalised at submission by the OACS. OA licences CC BY / CC BY-NC / CC BY-NC-ND.
- **Self-archiving (subscription route)**: accepted manuscript after a **12-month embargo**. The published version may not go on ResearchGate etc. The Zenodo preprint stays as it is.
- **Cover letter**: not mentioned in the guide. Write a short one anyway (EM normally has a slot).
- **UNVERIFIED**: whether the editors expect a Viewpoint under any informal length. Check in EM at submission.

**S356 account + EM mechanics (2026-10-23):**
- Login = **"Continue with Elsevier"** with the Elsevier account (vault `elsevier`, e-mail matthias@matthiasgruber.com), then a one-time **journal registration** (Title, Country required; Institution "Independent researcher" triggers an OK-able warning; reviewer availability left at the default No; marketing opt-out ticked).
- Article type list includes **Viewpoint** and open VSIs (Conscious awareness across the senses, deadline 2027-05-31, excludes work "solely with global states of consciousness"; Assumptions in Neuropsychology, 2027-01-15). General Information asks for the VSI or "Cortex journal (standard submission)".
- **Required items: Cover Letter, Title page, Manuscript** (authorship only on the title page). Also offered: Highlights, Figure, Scientific Transparency Statement/Report (mandatory only for revised empirical articles).
- **2 suggested reviewers required** (name, institution, e-mail, reason). Additional Information: transparency acknowledgement, "earlier version peer-reviewed for Cortex?", funding confirmation, Your Paper Your Way vs Standard.
- Manuscript Data: **EM caps keywords at 5** (the guide says 1–7). The extracted abstract must be "reviewed": `CKEDITOR.setData` alone leaves the flag; a real keystroke in the editor (space + Backspace) clears it.
- Publishing options popup (publishingoptions.elsevier.com): for an independent author it offered **Subscription only, "Nothing to pay"** → Save and return → Proceed → "Building PDF".
- EM file chooser: in `browser_run_code_unsafe`, `Promise.all([page.waitForEvent('filechooser'), click Browse])` + `fc.setFiles` works, but the MCP ALSO queues its own chooser per click. Cancel the extras with an empty `browser_file_upload`, then verify the table.
