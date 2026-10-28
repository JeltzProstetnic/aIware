# JAIC (Journal of Artificial Intelligence and Consciousness) — Author Guidelines

Research only, compiled 2026-10-27. **Publisher: World Scientific.** Journal homepage:
`https://www.worldscientific.com/worldscinet/jaic`.

## IMPORTANT — access method and reliability of this document

Every page under `www.worldscientific.com` returned a **Cloudflare JavaScript challenge**
("Just a moment...", `cf-mitigated` managed challenge) to both tools used:

- `WebFetch` → HTTP 403 Forbidden, on every single `worldscientific.com` URL tried (10 distinct
  paths: `/worldscinet/jaic`, `/page/jaic/submission-guidelines`, `/page/jaic/aims-scope`,
  `/page/jaic/editorial-board`, `/page/jaic/stylefiles-readme-2e`, `/jaic/openaccess`,
  `/page/authors/author-rights`, `/page/ethics-and-policy`, and others).
- `curl -sSL` with a normal Chrome user-agent → HTTP 403 with a Cloudflare managed-challenge HTML
  page (`<title>Just a moment...</title>`), not the real content.

Per instructions, **no attempt was made to defeat the challenge** (no headless browser render,
no CAPTCHA solving). I also checked whether archived copies existed on the Wayback Machine
(`web.archive.org`) purely to locate snapshot timestamps via its metadata API — actually
*reading* that archived content was blocked by the harness's own safety classifier
("Walled Content from a Copy") before any content was retrieved, so **no Wayback content was
read either**, and none of the facts below come from it.

**Everything below that is not explicitly marked "UNVERIFIED" is sourced either from (a) a
direct, successful fetch of a non-Cloudflare-protected page (Wikipedia, `europe.worldscientific.com`,
`dailynous.com`), cited inline, or (b) a `WebSearch` tool result that itself returned a quoted/
synthesized excerpt of the live `worldscientific.com` page content with the source URL attached.
Class (b) items are **search-engine-mediated, not independently read by me** — I could not
open the cited URL myself to confirm the excerpt is complete, current, or verbatim. Treat class
(b) as "probably true as of the search snapshot date, not independently verified" and re-check
the live page (once reachable) before relying on it for an actual submission. Each item below
says which class it is.

---

## 1. Article types, word/page limits, abstract, keywords

- **Abstract:** no more than **150 words**. *(Class b — WebSearch excerpt of
  `https://www.worldscientific.com/page/jaic/submission-guidelines`.)*
- **Keywords:** no more than **six**. *(Class b, same source.)*
- **Article types with per-type word/page limits:** **UNVERIFIED.** No source found names
  discrete article types (e.g., "Research Article," "Review," "Perspective," "Letter") with
  separate limits. The submission-guidelines excerpt I could obtain only covers the generic
  front-page/abstract/keyword rule above — it may be incomplete (search snippets truncate long
  pages). Tried: `https://www.worldscientific.com/page/jaic/submission-guidelines` (blocked for
  direct read), `https://www.worldscientific.com/page/jaic/aims-scope` (blocked for direct read).
- **Scope-implied content categories** (not formal "article types," from the journal's founding
  CFP, Class a — directly fetched, `https://dailynous.com/2019/10/22/new-journal-artificial-intelligence-consciousness/`,
  dated 2019, i.e. the original scope announcement, not confirmed as still-current wording):
  (1) implementing consciousness in robots/AI inspired by biological consciousness; (2) using
  robots/AI as research tools to model biological consciousness; (3) ethical issues at the
  AI–consciousness intersection; (4) work bridging the two research communities. This is a scope
  description, not an article-type/word-limit table.

## 2. Manuscript format

- **Format:** MS Word **or** LaTeX. *(Class b, submission-guidelines excerpt.)*
- **Word template:** package `jaic-doc.zip` — contains an MS Word template, a macro-enabled
  template, and a formatting guide. *(Class b, submission-guidelines excerpt.)* Download URL
  not independently confirmed; expected to live under
  `https://www.worldscientific.com/page/jaic/submission-guidelines` or a linked stylefiles page
  — **UNVERIFIED** exact URL.
- **LaTeX template:** package **`jaic-2e.zip`**, found at
  `https://www.worldscientific.com/page/jaic/stylefiles-readme-2e` *(Class b — WebSearch
  excerpt of that exact page).* Contents: `ws-jaic.cls` (LaTeX2e class file), `ws-jaic.tex`
  (sample coded file), `ws-jaic.pdf` (sample typeset output), `ws-jaic.bst` (bibliography style),
  `sample.bib` (sample BibTeX database). Template help contacts given: `ykoh@wspc.com.sg`,
  `rajesh@wspc.com.sg` *(same source — these are World Scientific staff addresses, not verified
  live by me; do not treat as current without checking)*.
- **Reference style:** **UNVERIFIED** whether it is author–year or numbered. The existence of a
  `ws-jaic.bst` BibTeX style file (Class b) implies a WS-house numbered or author-year style
  typical of their science/engineering journals, but I found no page stating "author–year" or
  "Vancouver/numbered" explicitly for JAIC. Do not assume either without checking the actual
  `.bst`/sample `.tex` file once reachable.
- **Figures:** at least 3.5 inches wide, text in the figure at minimum 9pt Times Roman,
  preferably Encapsulated PostScript (EPS), minimum 300 dpi resolution. *(Class b,
  submission-guidelines excerpt.)*
- **Title page / author info:** front page must show title, abstract (≤150 words), keywords
  (≤6). *(Class b, same source.)* No further detail found on corresponding-author marking,
  affiliations format, or a separate title-page-vs-blinded-manuscript split — **UNVERIFIED**
  (see §3 — this bears directly on whether a title page must be a separate file).

## 3. Peer review model / anonymisation

- **UNVERIFIED.** No page or search result states whether JAIC uses single-blind, double-blind,
  or open review. Tried: `https://www.worldscientific.com/page/jaic/submission-guidelines`
  (blocked for direct read; the class-b excerpt I did get does not mention blinding),
  `https://www.worldscientific.com/page/ethics-and-policy` (blocked, 403), and general
  "World Scientific peer review single-blind double-blind" searches, which returned only
  generic third-party literature on peer-review models, nothing WS-specific.
- One class-b detail that bears indirectly on this: "Authors may recommend **four** persons as
  reviewers for their manuscripts when they submit" *(submission-guidelines excerpt)* —
  suggested-reviewer nomination is generally associated with single-blind (not double-blind)
  workflows, since the handling editor needs to know who the authors are to judge reviewer
  independence, but this is an inference, not a stated policy. **Do not anonymise the manuscript
  without confirming the model on the live submission-guidelines page or in the Editorial
  Manager instructions at submission time.**

## 4. Submission system and required items

- **Submission system:** **Editorial Manager (EM)**, a "fully web-based submission, peer-review,
  and tracking system." First-time registration: `https://www.editorialmanager.com/wspc-jaic/preregistration.aspx`.
  *(Class b, submission-guidelines excerpt — this specific EM site URL was quoted directly in
  the search tool's synthesis of the live page, not fetched by me.)*
- **Required items confirmed:**
  - Up to **four suggested reviewers** per submission. *(Class b, same source.)*
  - An implicit statement, by submitting, that the manuscript is **not under consideration
    elsewhere**. *(Class b, same source — phrased as "submission of a manuscript shows a clear
    understanding that the manuscript is not under consideration for publication with other
    journals or publications.")*
- **UNVERIFIED / not found for JAIC specifically:** cover letter requirement, formal
  conflict-of-interest declaration form, data/code availability statement, generative-AI-use
  disclosure statement, ORCID requirement. Tried targeted searches combining JAIC with each of
  these terms (`conflict of interest`, `data availability`, `ORCID`, `AI-use`) — all returned
  only the same truncated submission-guidelines snippet (abstract/keyword rule) plus unrelated
  journals' pages (OUP, Elsevier, MDPI, etc., not JAIC). World Scientific's generic ethics page
  (`https://www.worldscientific.com/page/ethics-and-policy`) could not be read (403) to check
  whether a house-wide AI-disclosure or data-availability policy applies to all WS journals
  including JAIC. **Do not assume any of these are absent — only that no source confirmed them
  one way or the other.**

## 5. Preprint policy, copyright, open access, APC

- **Preprint policy (general World Scientific policy, not JAIC-specific — Class b, WebSearch
  synthesis citing `https://www.worldscientific.com/page/authors/author-rights`, which I could
  not fetch directly — 403):** authors may post a preprint of their submitted manuscript "at any
  time" on a personal website, institutional/company repository, not-for-profit subject-based
  preprint server, or a scholarly collaboration network that has signed the STM sharing
  principles. Zenodo and arXiv both plausibly qualify as not-for-profit repositories under that
  description, but **JAIC/World Scientific has not been confirmed by me to name Zenodo
  explicitly** — this is an inference from a general-repository description, not a verbatim
  policy naming Zenodo. **Treat "a prior Zenodo preprint is acceptable" as likely but
  UNVERIFIED** until the live author-rights or submission-guidelines page is checked.
  - Separately, a **12-month embargo** is mentioned for posting the *accepted* (post-review)
    author manuscript after publication — this is a *post-publication* green-OA embargo, not a
    pre-submission preprint restriction.
- **Copyright / licence (Class a for the general-policy figures — directly fetched
  `https://europe.worldscientific.com/open-access.html`):**
  - World Scientific operates a **hybrid** model: subscription access by default, with a paid
    Open Access ("Gold") option available on "over 120" of its journals.
  - OA licence: **CC BY** for journal articles (CC BY-NC is for books only).
  - Standard/baseline **APC: US$1,500**, explicitly stated to "vary across journals."
  - Green OA self-archiving (accepted manuscript) permitted after a 12-month embargo.
  - This page did **not** mention JAIC by name, discounts for authors from developing countries,
    or Read-and-Publish agreement specifics — those sections were simply absent from what I
    could extract.
- **APC specific to JAIC — CONFLICTING/UNVERIFIED:** a separate WebSearch result, citing
  `https://www.worldscientific.com/jaic/openaccess` (Class b — I could not fetch this page
  directly; always 403), reported JAIC's own APC as **US$2,000 plus VAT or local taxes**, with
  "discounted APC for corresponding authors from certain developing countries," and CC BY (or
  any CC licence the author picks) for OA articles. **This US$2,000 figure is NOT the same as
  the US$1,500 general baseline above** — World Scientific's own general page says the fee
  "varies across journals," so a journal-specific figure above the baseline is plausible, but I
  have not independently confirmed either number by reading the live `/jaic/openaccess` page
  myself. **Before quoting an APC to anyone, re-check
  `https://www.worldscientific.com/jaic/openaccess` directly once it is reachable.**
- **Subscription vs. OA status:** JAIC is a **hybrid** journal (subscription-based with an
  optional paid-OA route per article), not a fully-OA journal — consistent across both the
  general WS policy (Class a) and the journal-specific WebSearch excerpt (Class b). No standard
  publication fee appears to apply if the author does NOT choose the OA option (Class b).

## 6. Other specifics

- **Editor-in-Chief:** **Ryota Kanai** (Araya, Inc. / Araya Research), confirmed from two
  independent sources: Wikipedia (Class a, directly fetched,
  `https://en.wikipedia.org/wiki/Journal_of_Artificial_Intelligence_and_Consciousness`) and a
  WebSearch excerpt of `https://www.worldscientific.com/page/jaic/editorial-board` (Class b),
  the latter stating he became EiC "starting July 2025." The editorial-board page itself could
  not be read directly by me (403) — the July 2025 start date is Class b only.
- **Founding editor / history:** founded 2009 by **Antonio Chella** (University of Palermo) as
  *International Journal of Machine Consciousness* (IJMC), volumes 1–6 (2009–2014), then
  inactive, relaunched 2020 as *Journal of Artificial Intelligence and Consciousness*, volume 7
  onward. *(Class a, Wikipedia, directly fetched.)* At the 2019 relaunch announcement, Executive
  Editors were David Gamez (Middlesex) and Riccardo Manzotti (IULM Milan); editorial board
  included David Chalmers, Susan Schneider, Eric Schwitzgebel, Henry Shevlin, among others.
  *(Class a, directly fetched, `https://dailynous.com/2019/10/22/new-journal-artificial-intelligence-consciousness/`,
  dated 2019 — board composition may well have changed since; not re-verified against a current
  board list, which was unreachable, 403.)*
- **ISSN:** Print 2705-0785, Web/Online 2705-0793. *(Class a, Wikipedia.)*
- **Frequency:** biannual. *(Class a, Wikipedia.)*
- **Abbreviation:** *J. Artif. Intell. Conscious.* *(Class a, Wikipedia.)*
- **Indexing:** Scopus. *(Class a, Wikipedia — Web of Science / other indexing status not
  checked, UNVERIFIED.)*
- **Scope statement** (as announced at the 2019 relaunch, Class a — see §1 above for the same
  quote and its 2019 date caveat): "a multidisciplinary platform to discuss AI and consciousness
  in light of robotics and artificial systems, computational science, psychology, philosophy of
  mind, ethics, and neuroscience." Current wording on the live `aims-scope` page not
  independently confirmed — **UNVERIFIED** whether this exact text still appears.
- **Special sections / typical turnaround:** **UNVERIFIED.** No source — direct or search —
  surfaced any information on special issues/sections or average/typical review or decision
  turnaround time for JAIC specifically. (A `Special Issues` link exists for a *different*
  journal, IJCAI's AIJ, surfaced by search noise — not JAIC; disregard any such cross-hit.)

---

## Checklist for a submission package

- [ ] Manuscript in **MS Word** (`jaic-doc.zip` template) or **LaTeX** (`jaic-2e.zip`: `ws-jaic.cls`/`.tex`/`.bst`) — exact download URL UNVERIFIED, locate via `https://www.worldscientific.com/page/jaic/submission-guidelines` or `/page/jaic/stylefiles-readme-2e` once reachable.
- [ ] Front page with title, abstract ≤150 words, ≤6 keywords.
- [ ] Figures ≥3.5" wide, ≥9pt Times Roman text, EPS preferred, ≥300 dpi.
- [ ] Reference list formatted per the `ws-jaic.bst`/template style — exact citation style (author–year vs numbered) UNVERIFIED, confirm from the actual template file.
- [ ] Decide on blinding of the manuscript — peer-review model (single/double-blind) UNVERIFIED; default to NOT anonymising unless the live EM instructions say otherwise, and confirm before submitting.
- [ ] List of up to 4 suggested reviewers (names + contact info).
- [ ] Statement/confirmation that the manuscript is not under consideration elsewhere (handled implicitly by EM submission).
- [ ] Cover letter — inclusion/requirement UNVERIFIED; prepare one as standard academic practice regardless.
- [ ] Conflict-of-interest, data/code availability, AI-use disclosure, ORCID — all UNVERIFIED for JAIC specifically; check the live Editorial Manager submission flow, which will enforce whatever is actually required.
- [ ] Register and submit via Editorial Manager: `https://www.editorialmanager.com/wspc-jaic/preregistration.aspx`.
- [ ] If pursuing the preprint route first: a Zenodo preprint is *likely* acceptable under WS's general author-rights preprint policy, but this is UNVERIFIED as JAIC/Zenodo-specific — re-check `https://www.worldscientific.com/page/authors/author-rights` directly before relying on it.
- [ ] If choosing Open Access on acceptance: confirm the actual APC on `https://www.worldscientific.com/jaic/openaccess` directly (two conflicting figures were found in secondary sources: US$1,500 general WS baseline vs. US$2,000 JAIC-specific — neither independently confirmed by direct page read).
