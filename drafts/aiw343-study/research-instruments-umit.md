# AIW-343 study: instrument licensing and the UMIT TIROL ethics route

Research note, 2026-10-24. Every DOI below was checked against doi.org and resolved (HTTP 302) on 2026-10-24, and its metadata was read from Crossref, DataCite or OpenAlex.
Item texts are quoted only where an official open source publishes them, and each quote names its source. Where the items are copyrighted, or I could not retrieve them, the entry says so and gives no items.

**Four findings that affect the design (read these first)**

1. **The Díaz (2021) problem-intuition items are tied to vignettes that are partly made up, which counts as deception.** Each study opens with a pain/DPI neuroscience story. The debrief then says *"We made up the rest."* That conflicts with the protocol's "no deception beyond a neutral title". Taking the agree/disagree statements without the fabricated vignette means adapting the instrument.
2. **The Tellegen Absorption Scale (TAS) cannot be used in an online survey without a licence.** University of Minnesota Press holds the copyright, and its Test Division does not allow items to be reproduced online. MODTAS is a modification of the TAS, so its free status is unclear.
3. **A CC BY-NC-ND licence forbids derivatives, and a German translation is a derivative.** This applies to the Tobacyk (2004) RPBS paper and to the MVSQ paper. Translating either into German needs the authors' written permission.
4. **Several of the clean options are free and already validated in German:** BFI-10 (GESIS ZIS, free for non-commercial research), LSHS-G (CC BY-SA 4.0, ZPID Open Test Archive) and DES-B (public domain, English only).

---

## Part A — Instruments

### A1. Stanovich (1989) Dualism Scale

- **Citation:** Stanovich, K. E. (1989). Implicit philosophies of mind: The Dualism Scale and its relation to religiosity and belief in extrasensory perception. *The Journal of Psychology, 123*(1), 5–23. https://doi.org/10.1080/00223980.1989.10542958 (PsycTESTS record: https://doi.org/10.1037/t68280-000)
- **Items:** 27, a mix of dualist and physicalist statements scored as one dimension.
- **Response format:** Likert agreement. Anglin (2014) used a 5-point scale, 1 = strongly disagree to 5 = strongly agree, with α = .80 (Anglin, *Consciousness and Cognition 29*, 105–116, https://doi.org/10.1016/j.concog.2014.08.014). I could not read the original 1989 response format.
- **Licence:** I found no explicit licence. The article is © Taylor & Francis, and the items are reachable only through the paywalled paper or PsycTESTS (a subscription service). Treat it as "ask the author or publisher" (Keith Stanovich, University of Toronto, emeritus).
- **Short form:** none found.
- **German version:** none found.
- **Items openly available?** No. One example item is quoted in Anglin (2014): *"Minds are inside brains but are not the same as brains"*. The other items are not reproduced here.

### A2. Díaz (2021), problem intuitions

- **Citation:** Díaz, R. (2021). Do people think consciousness poses a hard problem? Empirical evidence on the meta-problem of consciousness. *Journal of Consciousness Studies, 28*(3–4), 55–75. Publisher page: https://www.ingentaconnect.com/content/imp/jcs/2021/00000028/f0020003/art00002
- **DOI:** **The publisher assigned none.** JCS DOIs (prefix 10.53765) start with volume 28, issue 9 (verified in Crossref). The repository copy has a DOI: **https://doi.org/10.48350/156357** (BORIS, University of Bern). Accepted-manuscript copy: https://philarchive.org/rec/DAZDPT
- **Materials:** OSF project https://osf.io/kqbh7/ (public; **no licence set** on the node, so default copyright applies). It holds the full Qualtrics exports for Studies 1a, 1b, 2a and 2b.
- **Response format:** Studies 1a, 1b and 2a used a 6-point scale: Strongly agree / Agree / Somewhat agree / Somewhat disagree / Disagree / Strongly disagree. Each was followed by a free-text "Please briefly justify your responses to the previous questions". Study 2b used an endpoint-labelled scale from "Strongly disagree" to "Strongly agree".
- **Item texts, verbatim from the OSF Qualtrics exports:**
  - Study 1a/1b/2a, pain vignette (target items): *"The properties of pain are fully explained in terms of neural activity in the DPI."* / *"The feeling of pain is just neural activity in the DPI."*
  - Matched water control: *"The properties of water are fully explained in terms of chemical composition H2O."* / *"The substance water is just chemical composition H20."* [sic]
  - Study 1b, no-vignette condition: *"The properties of pain are fully explained in terms of neural activity in a specific area of the brain."* / *"The feeling of pain is just neural activity in a specific area of the brain."*
  - **Study 2b, the cleanest four-item set:** *"The feeling of pain is just neural activity in the DPI."* / *"The feeling of pain is a different thing than neural activity in the DPI."* / *"The feeling of pain is fully explained in terms of neural activity in the DPI."* / *"Neural activity in the DPI cannot explain what is like to feel pain."* [sic]. Then the science-evaluation items: *"Science can discover much more about the feeling of pain than what is mentioned in the text."* / *"The scientific findings presented in the text are an example of good science."*
  - Manipulation check in 1a, 1b and 2a: *"The scientific findings about pain presented in this survey are real."* (Definitely true … Definitely false)
- **⚠ Deception:** the debrief reads *"Regarding pain, research has associated it with neural activity in the DPI. We made up the rest."* Using these items without that deception means dropping or rewriting the vignette, which is an adaptation (see the heading note).
- **Licence:** no licence is stated. These are short research items published for replication, so citing them is the norm, but there is no explicit grant. A courtesy email to the author (Rodrigo Díaz, now University of Geneva per PhilPeople) is advisable.
- **German version:** none found. A 2026 non-English replication exists: "Polishing the meta-problem of consciousness: empirical evidence for non-English …", *Philosophical Psychology*, https://doi.org/10.1080/09515089.2026.2710862 (Polish sample, so the language may be Polish rather than German).

### A3. Gottlieb & Lombrozo (2018), "science cannot explain"

- **Citation:** Gottlieb, S., & Lombrozo, T. (2018). Can science explain the human mind? Intuitive judgments about the limits of science. *Psychological Science, 29*(1), 121–130. https://doi.org/10.1177/0956797617722609
- **Materials:** OSF https://osf.io/3r96f/ (public; no licence set). `Stimuli.xlsx` lists all 46 items used in Studies 1–3 and the 46 extra items used in Study 3.
- **Response format:** 1 = strongly disagree to 7 = strongly agree. The paper gives the stems verbatim:
  - Studies 1–2: *"Science could one day fully explain ___"* (scientific possibility) and *"I am uncomfortable with the idea that science could one day fully explain ___"* (scientific discomfort, reverse-coded as "comfort").
  - Study 3, standardised: *"Science could one day fully explain the following phenomenon: ___"* and *"I am uncomfortable with the idea that science could one day fully explain the following phenomenon: ___"*.
  - Dimension items (Study 1), for example introspection-phenomenology: *"___ involves a subjective experience (a feeling of what it is like) that only the individual experiencing it can know"*.
- **Example phenomena, verbatim from Stimuli.xlsx:** "Feeling transformed by a spiritual event", "Experiencing "love at first sight"", "Using one's imagination", "Discerning temperature through touch", "Having headaches", "Dreaming", "Having hallucinations", "Perceiving color" (Study 3 only), "Feeling compassion toward those who are suffering". The full list is in the OSF file.
- **Licence:** no licence is stated. Same position as Díaz: cite it, and a courtesy note to Tania Lombrozo (Princeton) is optional.
- **German version:** none found.

### A4. Templer Death Anxiety Scale (DAS)

- **Citation:** Templer, D. I. (1970). The construction and validation of a Death Anxiety Scale. *The Journal of General Psychology, 82*(2), 165–177. https://doi.org/10.1080/00221309.1970.9920634
- **Items:** 15, true/false (9 keyed true, 6 keyed false).
- **Licence:** I found no explicit licence statement. The paper is © Taylor & Francis. Templer died in 2016. Secondary sources describe it as "widely used freely in non-commercial research" but cite no grant. Status: **unclear; no verified free licence.**
- **Short forms:** there is no official short form. Abdel-Khalek's ASDA is a separate instrument, not a short DAS. A 2025 review covers the many adaptations: Srivastava & Ghosh, *BMC Nursing 24*, https://doi.org/10.1186/s12912-025-04045-1 (CC BY). It reports a German translation exists, but I did not find a citable German validation paper.
- **Items openly available?** Not from an official open source. Not reproduced here.

### A5. BFI-10 (English and German)

- **English:** Rammstedt, B., & John, O. P. (2007). Measuring personality in one minute or less: A 10-item short version of the Big Five Inventory in English and German. *Journal of Research in Personality, 41*(1), 203–212. https://doi.org/10.1016/j.jrp.2006.02.001
- **German documentation:** Rammstedt, B., Kemper, C. J., Klein, M. C., Beierlein, C., & Kovaleva, A. (2014). Big Five Inventory (BFI-10). *ZIS*. https://doi.org/10.6102/zis76 (https://access.gesis.org/zis/554). Validation: Rammstedt et al. (2013), *methods, data, analyses 7*(2), 233–249, https://doi.org/10.12758/mda.2013.013 (CC BY 4.0, DataCite).
- **Licence, verbatim from ZIS:** *"Dieses Erhebungsinstrument darf kostenfrei für nichtkommerzielle Forschungszwecke verwendet werden. Bei einem Einsatz für andere Zwecke oder in einer anderen als der hier dokumentierten Form ist das Einverständnis der Autoren bzw. Autorinnen einzuholen."* → **Free for this study.**
- **Format:** 10 items. ZIS gives the German anchors as a 5-point scale, „trifft überhaupt nicht zu" (1) to „trifft voll und ganz zu" (5). The German instruction is *„Inwieweit treffen die folgenden Aussagen auf Sie zu?"*. Reverse-score items 1, 3, 4, 5 and 7, then average the two items per dimension.
- **Items, verbatim from ZIS 76 (German / English):**
  1. Ich bin eher zurückhaltend, reserviert. / I see myself as someone who is reserved. (−, E)
  2. Ich schenke anderen leicht Vertrauen, glaube an das Gute im Menschen. / … is generally trusting. (+, A)
  3. Ich bin bequem, neige zur Faulheit. / … tends to be lazy. (−, C)
  4. Ich bin entspannt, lasse mich durch Stress nicht aus der Ruhe bringen. / … is relaxed, handles stress well. (−, N)
  5. Ich habe nur wenig künstlerisches Interesse. / … has few artistic interests. (−, O)
  6. Ich gehe aus mir heraus, bin gesellig. / … is outgoing, sociable. (+, E)
  7. Ich neige dazu, andere zu kritisieren. / … tends to find fault with others. (−, A)
  8. Ich erledige Aufgaben gründlich. / … does a thorough job. (+, C)
  9. Ich werde leicht nervös und unsicher. / … gets nervous easily. (+, N)
  10. Ich habe eine aktive Vorstellungskraft, bin fantasievoll. / … has an active imagination. (+, O)
  - I did not re-read the English anchors from the 2007 paper. Take them from the paper before use.

### A6. O-LIFE short form, Unusual Experiences (UnEx)

- **Citation:** Mason, O., Linney, Y., & Claridge, G. (2005). Short scales for measuring schizotypy. *Schizophrenia Research, 78*(2–3), 293–296. https://doi.org/10.1016/j.schres.2005.06.020
- **Format:** 12 items, yes/no (yes = 1), range 0–12.
- **Licence:** PsyToolkit's survey library states *"The short O-LIFE can be used for research, but you need to acknowledge the authors and their research paper when writing about it."* (https://psytoolkit.org/survey-library/schizotypy-short-olife.html). That is a secondary source, not an author licence. Status: **free for research by convention; no author licence found.**
- **Items, verbatim as reproduced by PsyToolkit (secondary source; check against the 2005 paper before fielding):**
  1. When in the dark do you often see shapes and forms even though there is nothing there?
  2. Are your thoughts sometimes so strong that you can almost hear them?
  3. Have you ever thought that you had special, almost magical powers?
  4. Have you sometimes sensed an evil presence around you, even though you could not see it?
  5. Do you think that you could learn to read other's minds if you wanted to?
  6. When you look in the mirror does your face sometimes seem quite different from usual?
  7. Do ideas and insights sometimes come to you so fast that you cannot express them all?
  8. Can some people make you aware of them just by thinking about you?
  9. Does a passing thought ever seem so real it frightens you?
  10. Do you feel that your accidents are caused by mysterious forces?
  11. Do you ever have a sense of vague danger or sudden dread for reasons that you do not understand?
  12. Does your sense of smell sometimes become unusually strong?
- **German version:** Grant, P., Kuepper, Y., Mueller, E. A., Wielpuetz, C., Mason, O., & Hennig, J. (2013). Dopaminergic foundations of schizotypy as measured by the German version of the Oxford-Liverpool Inventory of Feelings and Experiences (O-LIFE). *Frontiers in Human Neuroscience, 7*, 1. https://doi.org/10.3389/fnhum.2013.00001 (CC BY; PsycTESTS record https://doi.org/10.1037/t41484-000). I did not check whether the German items are printed openly in that paper.

### A7. Absorption

- **TAS:** Tellegen, A., & Atkinson, G. (1974). *Journal of Abnormal Psychology, 83*(3), 268–277. https://doi.org/10.1037/h0036681. 34 items, true/false. **Licence: commercial and restricted.** The MPQ manual (Pearson) states that the copyright is assigned to University of Minnesota Press, and that no part may be copied or transmitted *"without written permission from the University of Minnesota Press"*. Requests go to testdiv@umn.edu (https://www.upress.umn.edu/test-division/permissions-and-ordering/). The UMP Test Division does not allow items to be reproduced online. Wikipedia (uncited) adds that UMP *"has reasserted its copyright"* over the circulated modified versions. German adaptation: Ritz & Dahme (1995), *Diagnostica* (I did not find its DOI).
- **MODTAS:** Jamieson, G. A. (2005). The Modified Tellegen Absorption Scale: A clearer window on the structure and meaning of absorption. *Australian Journal of Clinical and Experimental Hypnosis, 33*(2), 119–139 (I did not find a DOI; repository record: https://rune.une.edu.au/entities/publication/274580b7-e982-49b2-aa0a-5d5ed88878c8). 34 items, 0 = never to 4 = very often, items printed in Appendix A. **Licence: unclear.** It is a modification of a UMP-copyrighted scale, I found no licence from Jamieson, and the UMP position may extend to it. Ask Jamieson (University of New England) and UMP. It is widely used in research, for example Terhune & Jamieson (2021), *PNAS*, https://doi.org/10.1073/pnas.2108467118.
- **A free short alternative:** I found no validated, explicitly licensed short absorption scale. The practical options are (a) a UMP research permission, (b) leaving absorption out and using O-LIFE UnEx plus DES-B as proxies, or (c) checking the ZPID Open Test Archive (https://testarchiv.eu), which my search did not cover item by item.

### A8. Brief trait dissociation

- **Recommended: DES-B (modified for DSM-5).** Dalenberg, C., & Carlson, E. (2010), modified for DSM-5 by the same authors. APA "emerging measures" PDF: https://www.psychiatry.org/File%20Library/Psychiatrists/Practice/DSM/APA_DSM5_Severity-of-Dissociative-Symptoms-Adult.pdf
- **Licence, verbatim from the APA PDF:** *"This measure is based on measures produced using U.S. federal government resources and is therefore in the public domain and freely available for use without permission so long as authorship is accurately attributed, as follows: DES-B (Dalenberg C, Carlson E, 2010) modified for DSM-5 by C. Dalenberg and E. Carlson."* → **Free.** The APA's instructions and scoring are © APA, but *"can be reproduced without permission by researchers"*.
- **Format:** 8 items; time frame "the past SEVEN (7) DAYS"; 0 = Not at all, 1 = Once or twice, 2 = Almost every day, 3 = About once a day, 4 = More than once a day; total 0–32, average 0–4. **Note:** this is a state/past-week version. For trait use, the time frame would have to change, which is an adaptation to report.
- **Items, verbatim from the APA PDF:** 1. I find myself staring into space and thinking of nothing. 2. People, objects, or the world around me seem strange or unreal. 3. I find that I did things that I do not remember doing. 4. When I am alone, I talk out loud to myself. 5. I feel as though I were looking at the world through a fog so that people and things seem far away or unclear. 6. I am able to ignore pain. 7. I act so differently from one situation to another that it is almost as if I were two different people. 8. I can do things very easily that would usually be hard for me.
- **DES / DES-II (28 items, 0–100 %):** Bernstein & Putnam (1986), *J Nerv Ment Dis 174*(12), 727–735, https://doi.org/10.1097/00005053-198612000-00004. DES-II: Carlson & Putnam (1993), *Dissociation 6*(1), 16–27 (no DOI). Widely circulated free of charge, but I did not find an explicit licence.
- **German:** the German DES is the FDS (Spitzer, Freyberger et al.), which is commercial (Hogrefe/Huber; not verified in detail). I did not find a German DES-B.

### A9. Paranormal belief

- **RPBS:** Tobacyk, J. J. (2004). A revised paranormal belief scale. *International Journal of Transpersonal Studies, 23*(1), 94–98. https://doi.org/10.24972/ijts.2004.23.1.94. 26 items, 7-point, seven subscales. **Licence: CC BY-NC-ND 4.0** (repository page https://digitalcommons.ciis.edu/ijts-transpersonalstudies/vol23/iss1/11/). You may use the items verbatim for non-commercial work, but **a translation or a shortened version is a derivative** and needs the author's permission. The full text is open, but Cloudflare blocked automated download, so the items are not quoted here. Download the PDF by hand. Original PBS: Tobacyk & Milford (1983), *JPSP 44*(5), 1029–1037, https://doi.org/10.1037/0022-3514.44.5.1029.
- **Rasch two-factor version:** Lange, R., Irwin, H. J., & Houran, J. (2000). Top-down purification of Tobacyk's Revised Paranormal Belief Scale. *Personality and Individual Differences, 29*(1), 131–156. https://doi.org/10.1016/s0191-8869(99)00183-x. Two factors: Traditional Paranormal Beliefs (TPB) and New Age Philosophy (NAP), built from RPBS items. Elsevier paywall, so items are not quoted. Using it inherits the RPBS licence position.
- **German:** I found no German RPBS validation. A German short supernatural-belief alternative exists, "Supernatural Belief Scale – German Version (SBS-10)" (ResearchGate record; I did not verify the citation).

### A10. Visual snow, closed-eye visuals and hypnagogia

- **Melbourne Visual Snow Questionnaire (MVSQ):** Thompson, A. C., Goodbourn, P. T., & Forte, J. D. (2024). Visual Snow Syndrome is unstable: A longitudinal investigation of VSS symptoms in a naïve population. *Annals of Clinical and Translational Neurology, 11*(12), 3205–3214. https://doi.org/10.1002/acn3.52228. Built for **naïve general-population screening**, *"for research purposes only"*. Short and long forms are in Appendix S1. **Article licence: CC BY-NC-ND 4.0**, so a German translation needs the authors' permission. Not quoted. It derives from Kondziella, Olsen & Dreier (2020), Prevalence of visual snow syndrome in the UK, *European Journal of Neurology 27*(5), 764–772, https://doi.org/10.1111/ene.14150.
- **Iowa Sleep Experiences Survey (ISES):** Watson, D. (2001). Dissociations of the night. *Journal of Abnormal Psychology, 110*(4), 526–535. https://doi.org/10.1037/0021-843x.110.4.526. Two factors: General Sleep Experiences (15 items, including hypnagogic hallucinations, vivid dreams, dream/reality confusion) and Lucid Dreaming (3). Reported item counts vary (18 or 24). © APA, so not quoted. Further validation: Fassler, Knox & Lynn (2006), *PAID 41*(4), 675–684, https://doi.org/10.1016/j.paid.2006.03.007. I found no explicit licence.
- **Launay-Slade Hallucination Scale, German (LSHS-G): best option.** Lincoln, T. M., Keller, E., & Rief, W. (2009). *Diagnostica, 55*(1), 29–40. https://doi.org/10.1026/0012-1924.55.1.29. Open questionnaire at the ZPID Open Test Archive: https://doi.org/10.23668/psycharchives.14241 (test page https://www.testarchiv.eu/de/test/9006380). **Licence: CC BY-SA 4.0** (DataCite, and the test page: *"Copyright Autor(-Innen); CC-BY-SA 4.0"*). 12 items, 0–4, from "trifft sicher nicht auf mich zu" to "trifft sicher auf mich zu". The items are in the PDF, which I did not open. English lineage: Bentall & Slade (1985), https://doi.org/10.1016/0191-8869(85)90151-5; LSHS-R Morrison, Wells & Nothard (2000), https://doi.org/10.1348/014466500163112; Larøi, Marczewski & Van der Linden (2004), https://doi.org/10.1016/s0924-9338(03)00028-2.
- **Phosphenes / closed-eye visuals:** I found no validated stand-alone scale. Partial coverage comes from O-LIFE UnEx item 1 and the ISES hypnagogic items.

### A11. DOI checks

- Clark, A., Friston, K., & Wilkinson, S. (2019). Bayesing qualia: Consciousness as inference, not raw datum. *Journal of Consciousness Studies, 26*(9–10), 19–33. **No DOI exists** (JCS DOIs start at 28(9), as above). Cite with the Ingenta URL https://www.ingentaconnect.com/contentone/imp/jcs/2019/00000026/f0020009/art00002 or PhilPapers CLABQC.
- Rouault, M., McWilliams, A., Allen, M. G., & Fleming, S. M. (2018). Human metacognition across domains: Insights from individual differences and neuroimaging. *Personality Neuroscience, 1*, e17. **https://doi.org/10.1017/pen.2018.16**. Verified in Crossref (article number e17).

### A12. Self-generated identification codes (SGIC)

- Yurek, L. A., Vasey, J., & Sullivan Havens, D. (2008). The use of self-generated identification codes in longitudinal research. *Evaluation Review, 32*(5), 435–452. https://doi.org/10.1177/0193841x08316676
- Schnell, R., Bachteler, T., & Reiher, J. (2010). Improving the use of self-generated identification codes. *Evaluation Review, 34*(5), 391–418. https://doi.org/10.1177/0193841x10387576. A 7-element code gave 66.9 % exact matches and 91.5 % with off-by-one matching at one month.
- Direnga, J., Timmermann, D., Lund, J., & Kautz, C. (2016). Design and application of self-generated identification codes (SGICs) for matching longitudinal data. *44th SEFI Conference*, Tampere. https://doi.org/10.5281/zenodo.17021045 (CC BY 4.0). It gives item criteria: applies to everyone, known to the respondent but not the researcher, stable over time, unobservable, high variance, simple to state. It also gives an off-1 matching algorithm, with a 76 % match rate at about 3 months and no false positives in a handwriting check.
- **Recommended recipe for this study** (six elements, alternating letters and digits; fill-in fields, with a worked example shown):
  1. 1st letter of your mother's first name
  2. 2nd letter of your mother's first name
  3. Day of the month you were born (01–31, dropdown)
  4. 1st letter of your place of birth
  5. 2nd letter of your place of birth
  6. Last digit of your birth year
  - Example: mother Anna, born on the 7th in Feldkirch in 1978 → `AN07FE8`.
  - Do not use sibling counts. Both Kearney and Schnell report high error rates for them, and the order in which siblings are counted is ambiguous.
  - Do not use father's initial, which is inconsistent across studies.
  - Normalise umlauts (Ä→A or AE, decide once and state it), case and whitespace before matching.
  - Match with off-1 tolerance plus a mutual-nearest rule (Direnga).
  - In a sample of about 200 people, a 6-character code has ample identifying power. **Report the false-match risk**: with ~200 people, off-1 matching can produce a few false pairs. For linking waves, an exact-match analysis plus an off-1 sensitivity analysis is defensible.
  - **Privacy note:** the code combines quasi-identifiers. Store it only in the response database and never next to e-mail addresses.

---

## Part B — UMIT TIROL

### B1. Ethics committee: "RCSEQ – Research Committee for Scientific Ethical Questions" (Freiwillige Ethikkommission RCSEQ)

- **URL:** https://www.umit-tirol.at/rcseq. Contact: rcseq@umit-tirol.at, +43 50 8648 3942, office staff Isolde Enz and Tilane Bouvet.
- **Chair:** Priv.-Doz. Dr. Magdalena Flatscher-Thöni (magdalena.flatscher-thoeni@umit-tirol.at). Deputy: ao. Univ.-Prof. Dr. Martin Welk (IBIA).
- **Remit:** a voluntary institutional committee shared by UMIT TIROL and fh gesundheit, set up in 2011. It reviews non-statutory projects (anything outside AMG, MPG, KAKuG etc.) that involve vulnerable groups and/or GDPR Art. 9 special-category data. It does not review interventional hospital studies; those go to the Ethikkommission of the Medizinische Universität Innsbruck.
- **Who can apply.** Rules of procedure §1(1)(a), verbatim: projects *"welche seitens oder von Mitarbeiterinnen/Mitarbeitern und/oder Studierenden der Partner durchgeführt werden"*. **An external researcher cannot apply alone.** The application has to come from, or be carried by, a UMIT (or fhg) staff member as co-investigator or project lead. The rules do not explicitly address external co-investigators, so confirm with the office. The rules of procedure were adopted at the 37th session on 16 Oct 2018 (PDF: https://www.umit-tirol.at/data.cfm?vpath=ma-wartbare-inhalte/ma-downloadfiles/06c1-rcseq-go&download=yes).
- **Two tracks (from the submission page):**
  - **Shortened procedure:** used when there is no vulnerable group and no special-category data. Submissions can come at any time and are usually finished "innerhalb weniger Werktage". The outcome is an "RCSEQ-Stammblatt" documenting the project.
  - **Full session:** used when a vulnerable group or special-category data are involved. The project goes to the next session, and the signed original application must also be submitted on paper.
  - **⚠ Which track this study falls in:** paranormal and dualism beliefs are arguably *"religiöse oder weltanschauliche Überzeugungen"*, and dissociation, hallucination-proneness and visual-snow symptoms are arguably health data. Both are Art. 9 categories. Full anonymity takes the data outside the GDPR, **but** SGIC wave-linking makes the data pseudonymous rather than anonymous. Expect the **full-session** track, or ask the office first; there is an *"Anfrage"* inquiry route. UMIT also publishes a *"Handreichung anonyme Befragung vulnerabler Personengruppen"*.
- **Documents:**
  - signed RCSEQ-Antragsformular
  - short exposé (a "Muster Exposé Methodenbeschreibung" template is provided)
  - questionnaire
  - participant information and consent (an "Info-EWE für anonyme Online-Befragung" template exists)
  - description of participant-protection and data-protection measures
  - recruitment plan and planned n
  - data-analysis method
  - the RCSEQ-Checkliste (https://www.umit-tirol.at/data.cfm?vpath=ma-rcseq/rcseq-checkliste-2025)
  - Revisions are due within 6 months, or the application counts as withdrawn.
- **Sessions:** Tuesdays at 13:30. The 2026–27 schedule (session / deadline / date):
  - 78: 23 Nov 2026 → 15 Dec 2026
  - 79: 1 Feb 2027 → 23 Feb 2027
  - 80: 30 Mar 2027 → 20 Apr 2027
  - 81: 24 May 2027 → 15 Jun 2027
  - 82: 27 Sep 2027 → 19 Oct 2027
  - 83: 29 Nov 2027 → 14 Dec 2027
  - Source: https://www.umit-tirol.at/data.cfm?vpath=ma-rcseq/sitzungstermine_2026-27_rcseq. Urgent cases can be decided by circulation (Umlaufbeschluss, rules §9).
- **Fees:** none are mentioned on the RCSEQ pages or in the rules of procedure. Presumably there are none for internal applicants; confirm with the office.

### B2. Relevant departments (from https://www.umit-tirol.at/page.cfm?vpath=universitaet/organe/departments)

- **Psychologie und Sportmedizin:** department head Univ.-Prof.in Dr.in Dipl.-Psych.in Maria Agthe. **Institut für Psychologie** head Univ.-Prof.in Dr.in Martina Rieger (martina.rieger@umit-tirol.at). This is the most natural home for a consciousness or cognition questionnaire.
- **Biomedizinische Informatik und Mechatronik:** department head Univ.-Prof. Dipl.-Ing. Dr. Alexander Sutor. **Institut für Medizinische Informatik** head Univ.-Prof. Dr. Elske Ammenwerth. **Institut für Biomedizinische Bildanalyse** under Martin Welk, the RCSEQ deputy chair.
- **Public Health, Versorgungsforschung und HTA:** department head Univ.-Prof. Dr. Harald Stummer. It includes a Zentrum für Statistische Beratung, which could help with power and analysis.
- **Pflegewissenschaft und Gerontologie:** Univ.-Prof. Mag. Dr. Gerhard Müller. Not relevant here.

### B3. Melanie (née Osl) — **not found as current UMIT staff (confidence: moderate)**

- **What the record shows:**
  - Publications as "Melanie Osl" run from 2006 to 2013 (OpenAlex author A5082269139; dblp https://dblp.org/pid/65/5918.html).
  - She was in the Research Group for Clinical Bioinformatics (Christian Baumgartner), Institute of Electrical, Electronic and Bioengineering, UMIT, working with Stephan Dreiseitl.
  - She was a visiting researcher at the UCSD Division of Biomedical Informatics with Lucila Ohno-Machado in 2011–2012.
  - Last UMIT-affiliated paper: Pallua et al. 2013, *J Proteomics*, https://doi.org/10.1016/j.jprot.2013.08.003.
  - Topics: biomarker discovery from MS data, feature selection (the "Redundancy Demoting" algorithm, *J Biomed Inform* 2009, https://doi.org/10.1016/j.jbi.2009.05.006), and classifier calibration (*JAMIA* 2011, https://doi.org/10.1136/amiajnl-2011-000291).
- **Searches that came back empty:**
  - The UMIT department, institute and staff pages (Technik team, IIG, IEBE, Psychology, Public Health) list no Melanie in informatics or psychology.
  - The Melanies on umit-tirol.at are a nursing coordinator, nursing thesis authors and a MedUni sleep-lab co-author.
  - ORCID has no "Melanie Osl". The two ORCID Melanies with a UMIT affiliation are nursing researchers (Breznik, Karrer).
  - OpenAlex shows no Melanie co-author of Netzer, Dreiseitl or Baumgartner after 2013.
- **Conclusion:** there is no public evidence that she works at UMIT now. If she married, the new surname does not surface in any public professional source I could reach. The likely explanation is that she left academic publishing around 2013. Asking MG's network or LinkedIn directly would settle it faster than further searching.

### B3a. "Michael", former co-student, now UMIT staff (**candidates only, not an identification**)

| Candidate | Position / unit | Fit with "medical/biomedical informatics at UMIT ~2002–07" | Source |
|---|---|---|---|
| **Ass.-Prof. Dipl.-Ing. Dr. Michael Netzer** | Universitätsassistent, Institut für Medizinische Informatik (also listed under IEBE); michael.netzer@umit-tirol.at; Ars Docendi 2025 teaching prize | **Strong.** UMIT-affiliated papers from 2008. Co-authored repeatedly with Melanie Osl (2008–2012) in the same clinical-bioinformatics group. Dipl.-Ing. title. Topics: ML, data mining, bioinformatics. | https://www.umit-tirol.at/page.cfm?vpath=departments/technik/iig/team |
| **Dipl.-Ing. Dr. Michael Handler** | Universitätsassistent / Senior Scientist, Institut für Elektrotechnik und Biomedizinische Technik (IEBE); michael.handler@umit-tirol.at | **Good.** Co-authored with Osl and Netzer (2010–11). Dipl.-Ing. PhD on cryoablation simulation (ÖGBMT prize 2014). Teaches biomedical modelling and simulation. | https://www.umit-tirol.at/page.cfm?vpath=departments/technik/iebe/team |
| Dr. Michael Glöggler | Associate Researcher, Institut für Medizinische Informatik | **Weak.** German economist/computer scientist whose doctorate came from UMIT, apparently later. Works on patient-portal taxonomies. | https://www.umit-tirol.at/page.cfm?vpath=departments/technik/team |
| Priv.-Doz. Michael Edlinger | Senior Scientist, Epidemiology, Public Health | **Does not fit.** Demography, MSc Amsterdam, PhD MedUni Innsbruck. | UMIT biosketch (biosketch_edlinger_m) |
| Michael Fischer | Head, Research Unit for Quality and Ethics in Health Care | **Does not fit.** Theology and health-care ethics. | https://www.umit-tirol.at/page.cfm?vpath=departments/public_health/research-unit-for-quality/team |

I did not verify that Netzer or Handler studied at UMIT between 2002 and 2007. That inference rests on the Dipl.-Ing. title, UMIT-only affiliations from 2008, and shared papers with Osl.
