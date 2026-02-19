# Complete Publications of Matthias Gruber

## Overview

This report catalogs all known publications by Matthias Gruber (b. 1978, Feldkirch, Austria) — biomedical informatics researcher (UMIT), software professional, and author. Distinguishing this Matthias Gruber from namesakes (notably the Cardiff University neuroscientist MJ Gruber and the EPFL entrepreneurship professor Marc Gruber) required cross-referencing institutional affiliations (UMIT, Profactor, V-Research, BlueLogic) and co-author networks.[^1][^2]

***

## I. Academic Theses

### 1. Master Thesis: *Modulare Delta Algorithmen für das praktische Versionsmanagement von Dokumenten* (2007)

- **Author:** Matthias Gruber
- **Institution:** UMIT – Private Universität für Gesundheitswissenschaften, Medizinische Informatik und Technik, Hall in Tirol
- **Institute:** Institut für Informationssysteme des Gesundheitswesens
- **Supervisor:** Hon. Prof. Dr. Roland Blömer
- **Degree:** Master of Science, Biomedizinische Informatik
- **Year submitted:** 2007 (Innsbruck, 11.06.2007)
- **Language:** German (with English summary)
- **Software:** SDelta (Secure Delta) — a managed (.NET/C#) framework for binary and text delta algorithms implementing Myers (1986) and Tridgell/rsync (1999) with swappable cryptographic hash functions (addressing known weaknesses in MD5/SHA-1)[^3][^4]
- **Acknowledgments:** Credits Bernhard Glück (business partner at BlueLogic Software Solutions) for contributions, and mentions the software was to be deployed in BlueLogic's commercial document management system[^3]

**Predatory journal republication:** The thesis was republished in 2010 by **VDM Verlag Dr. Müller** (Riga, Latvia) as a book under the title *"Modulare Delta Algorithmen für das praktische Versionsmanagement: Verwendung von sicheren Hashfunktionen bei der Erstellung von Concurrent Versioning Systems (CVS) und Online Update Systemen"*, ISBN 978-3-639-22928-8, 84 pages. VDM Verlag Dr. Müller is a well-known predatory/vanity publisher that systematically contacted thesis authors and republished their work with minimal editorial oversight — essentially a print-on-demand repackaging of the original thesis.[^5][^6]

### 2. Dissertation: *A Generic Framework for Discrete Simulation Based Optimization* (completed ~2010–2016, never defended)

- **Author:** Matthias Gruber
- **Topic:** A generic, high-performance object-oriented software framework for simulation-based optimization, consisting of two main libraries: (1) a discrete event simulation engine with advanced event concept (event/event-instance/handler separation), reproducible stochastics with seed indexing, and entity templates; (2) a metaheuristic optimization framework with generic interfaces supporting random strategy, simulated annealing, and evolutionary algorithms — designed for hyper-heuristic scenarios[^7]
- **Languages:** Implemented in both C# (.NET) and Java
- **Supervisor:** Ao. Univ. Prof. Dipl.-Ing. Dr. techn. Felix Breitenecker (TU Wien)
- **Co-supervision/support:** Dr. techn. Thomas Löscher
- **Affiliations referenced:** Profactor GmbH, HEAL Group (HeuristicLab), POM Institute (Universität Wien), AREC Automatisierungstechnik GmbH[^7]
- **Status:** The dissertation was completed, accepted by the institute as finished, and self-published via Lulu.com in 2016 (ISBN 978-3-838-15223-3). However, **it was never formally defended** — the institute required Matthias to teach for free for 3 years as a condition for allowing the defense, which he declined. As a result, no doctoral degree was awarded despite the work being academically complete.[^8]

***

## II. Peer-Reviewed Conference Papers

### 3. IEEE CIG 2006: *Using Wearable Sensors for Real-Time Recognition Tasks in Games of Martial Arts — An Initial Experiment*

- **Authors:** Ernst A. Heinz, Kai S. Kunze, **Matthias Gruber**, David Bannach, Paul Lukowicz
- **Conference:** 2006 IEEE Symposium on Computational Intelligence and Games (CIG'06), Reno/Lake Tahoe, NV, USA, May 22–24, 2006
- **Published in:** Proceedings of the 2006 IEEE Symposium on Computational Intelligence and Games, pp. 98–102
- **Publisher:** IEEE (Institute of Electrical and Electronics Engineers)
- **ISBN:** 1-4244-0464-9 / 978-1-4244-0464-3
- **Affiliation:** Institute for Computer Systems and Networks (CSN), UMIT, Hall in Tyrol, Austria[^9][^10]
- **Summary:** Describes an initial experiment using inexpensive body-worn gyroscopes and accelerometers to capture Wing Tsun Chum Kiu movements. Matthias Gruber served as the Wing Tsun expert test subject. The paper demonstrates feasibility of real-time motion recognition for martial arts games using frequency range power (FRP), thresholding, and machine learning (C4.5, KNN, Naive Bayes). Results showed clear distinction between expert and amateur execution.[^9]
- **Note:** Matthias is credited in the paper as the Wing Tsun expert whose movements were recorded and compared against an amateur (co-author Kai Kunze).[^9]

### 4. IEEE LINDI 2011: *Practical Token Retrieval and Indexing from Binary Data: An Application in Computer Aided Design*

- **Authors:** M. Gruber, R. Geschray, C. Hillbrand
- **Conference:** 2011 IEEE 3rd International Symposium on Logistics and Industrial Informatics (LINDI)
- **Publisher:** IEEE
- **Affiliation:** V-Research GmbH, 6850 Dornbirn, Austria
- **DOI reference:** IEEE Xplore document 6031132[^11][^12]
- **Summary:** Proposes a method to retrieve textual data from proprietary binary CAD files (specifically MegaCAD PRT files) by parsing binary streams with a sliding window, then filtering noise using phonetic, phonotactic, and casing criteria. The paper introduces a characteristic value formula combining phonetic measure, casing measure, and umlaut fraction with ROC-optimized thresholds. Results: 930 distinct tokens retrieved vs. 348 from official export, with promising sensitivity/specificity demonstrated on 39,005 German dictionary words vs. randomly generated strings.[^11]
- **Financed by:** Austrian COMET scheme within the K-Project "Integrated Decision Support Systems for Industrial Processes" (ProDSS).[^11]

### 5. ASIM 2009: *Evaluierung und Analyse integrationsfähiger Simulations Engines für die Entwicklung komplexer und detaillierter Simulationsmodelle*

- **Authors:** Markus Speckle, **Matthias Gruber**, Martin Saler
- **Conference:** ASIM 2009 (Arbeitsgemeinschaft Simulation) Workshop, Dresden
- **Affiliation:** V-Research GmbH – Industrielle Forschung und Entwicklung, Technische Logistik, Stadtstraße 33, A-6850 Dornbirn[^13]
- **Summary:** Evaluates 52 simulation tools and 16 simulation libraries against defined exclusion and evaluation criteria for integration into the V-Research AWPS (Anwendungsplattform Simulation) environment. Identifies 4 qualifying tools (Micro Saint Sharp, ExtendSim AT, Arena, Witness) and 3 libraries (SiRO, Delsi, CSIM19). The paper compares differences in modeling paradigms, programming languages, interface capabilities, development environments, and verification/validation support between simulation tools and libraries.[^13]
- **Note:** This paper is a direct companion to Speckle's thesis (referenced as  in the paper) and laid groundwork for the dissertation's simulation library design.[^14][^7]

***

## III. Books (Self-Published via Lulu.com)

### 6. *Emergenz des Bewusstseins* (2015)

- **Author:** Matthias Gruber
- **Publisher:** Lulu.com
- **Date:** January 20, 2015
- **Format:** Hardcover, 302 pages
- **ISBN-13:** 978-1-326-65207-4
- **ISBN-10:** 1326652079
- **Language:** German[^15][^16]
- **Description:** A non-fiction treatise on the emergence of consciousness and intelligence, leading the reader from philosophy and semantics through information-theoretic and neurobiological foundations. The author claims to have deciphered human consciousness at age 25 and presents his theoretical framework across disciplines.[^15]
- **Lulu profile:** Published under the spotlight "WingChun" with the bio: "Matthias Gruber is a software professional and former researcher, specialized in biomedical informatics and artificial intelligence".[^17]

### 7. *The Billion Year Countdown* (2018)

- **Author:** Matthias Gruber
- **Publisher:** Lulu.com
- **Date:** August 5, 2018
- **Format:** Paperback, 190 pages
- **ISBN-13:** 978-0-244-10547-1
- **Language:** English[^18][^19]
- **Genre:** Science Fiction
- **Description:** A student, just months from completing his final thesis, encounters a mysterious being, triggering a chain of events linked to a strange plague and a rogue secret agent. The narrative evolves into an intergalactic odyssey where the boundaries between good and evil blur.[^18]

### 8. *Ringe des Lebens — Die Geschichte der X* (2017)

- **Author:** Matthias Gruber
- **Publisher:** Lulu.com
- **Date:** December 24, 2017
- **Format:** Paperback, 484 pages
- **ISBN-13:** 978-0-244-95623-3
- **Language:** German
- **Genre:** Science Fiction[^20]

### 9. *Ringe des Lebens — Das Erbe der X* (2018)

- **Author:** Matthias Gruber
- **Publisher:** Lulu.com
- **Date:** January 13, 2018
- **Format:** Paperback, 506 pages
- **ISBN-13:** 978-0-244-65624-9
- **Language:** German
- **Genre:** Science Fiction[^21]

### 10. *Ringe des Lebens — Die Zukunft der X* (2018)

- **Author:** Matthias Gruber
- **Publisher:** Lulu.com
- **Date:** March 5, 2018
- **Format:** Paperback, 444 pages
- **ISBN-13:** 978-0-244-95624-0
- **Language:** German
- **Genre:** Science Fiction[^22]

### 11. *A Generic Framework for Discrete Simulation Based Optimization* (2016)

- **Author:** Matthias Gruber
- **Publisher:** Lulu.com (self-published version of the undefended dissertation)
- **Date:** April 4, 2016
- **ISBN-13:** 978-3-838-15223-3
- **Language:** English[^23][^8]

***

## IV. Other Notable Citations & Work-in-Progress

### 12. Expert Interview Citation in Georg Knabl's Diploma Thesis (2008)

- **Cited as:** "Gruber, Matthias. 2008. private communication. 6. Mai 2008."
- **Context:** Georg Knabl's diploma thesis *"Semantic Web in Unternehmen: Effizienter Einsatz der Semantic Web-Technologie in Unternehmen"* (FH JOANNEUM, September 2008) lists Matthias Gruber as one of six interviewed Semantic Web experts, identified as "Dipl.-Ing. Matthias Gruber, wissenschaftlicher Mitarbeiter bei Profactor GmbH im Bereich Artificial Intelligence".[^24]
- **Significance:** This places Matthias at Profactor in the AI department as of mid-2008 and confirms his expertise was recognized in the semantic web / knowledge management space.

### 13. *Sustainable Leadership in an Agile Environment* (Work in Progress)

- **Author:** Matthias Gruber
- **Status:** Early draft / notes only
- **Content:** Brief outline for a planned book on leadership, with notes on leading upwards vs. downwards, humor in management, and the tension between doing the best for the customer vs. the company. Originally intended to be titled "Sustainable Leadership in a Volatile Environment".[^25]

***

## Summary Table

| # | Type | Title | Year | Venue / Publisher | Co-Authors |
|---|------|-------|------|-------------------|------------|
| 1 | Master Thesis | Modulare Delta Algorithmen für das praktische Versionsmanagement | 2007 | UMIT | — |
| 1b | Predatory Reprint | (same as above) | 2010 | VDM Verlag Dr. Müller | — |
| 2 | Dissertation (undefended) | A Generic Framework for Discrete Simulation Based Optimization | ~2010–2016 | (TU Wien / Lulu.com) | — |
| 3 | IEEE Conference Paper | Using Wearable Sensors for Real-Time Recognition Tasks in Games of Martial Arts | 2006 | IEEE CIG'06 | Heinz, Kunze, Bannach, Lukowicz |
| 4 | IEEE Conference Paper | Practical Token Retrieval and Indexing from Binary Data | 2011 | IEEE LINDI | Geschray, Hillbrand |
| 5 | Conference Paper | Evaluierung und Analyse integrationsfähiger Simulations Engines | 2009 | ASIM 2009 | Speckle, Saler |
| 6 | Book (Non-fiction) | Emergenz des Bewusstseins | 2015 | Lulu.com | — |
| 7 | Book (Fiction) | The Billion Year Countdown | 2018 | Lulu.com | — |
| 8 | Book (Fiction) | Ringe des Lebens — Die Geschichte der X | 2017 | Lulu.com | — |
| 9 | Book (Fiction) | Ringe des Lebens — Das Erbe der X | 2018 | Lulu.com | — |
| 10 | Book (Fiction) | Ringe des Lebens — Die Zukunft der X | 2018 | Lulu.com | — |
| 11 | Book (Technical) | A Generic Framework for Discrete Simulation Based Optimization | 2016 | Lulu.com | — |
| 12 | Expert Citation | Private communication in Knabl's Diplomarbeit | 2008 | FH JOANNEUM | — |
| 13 | Work in Progress | Sustainable Leadership in an Agile Environment | — | — | — |

***

## Notes on Disambiguation

The name "Matthias Gruber" is extremely common in German-speaking academia. The Cardiff University neuroscientist Matthias J. Gruber (curiosity/memory research, ~3,300 citations) and EPFL's Marc Gruber (entrepreneurship, ~14,700 citations) are entirely different researchers. This Matthias Gruber's academic footprint is modest in citation counts but distinctive in its interdisciplinary breadth — spanning Wing Tsun biomechanics, cryptographic hash functions, CAD data mining, discrete simulation engineering, consciousness theory, and science fiction.[^26][^2]

---

## References

1. [Matthias Gruber](https://scholar.google.com/citations?hl=en&user=nPA2jxgAAAAJ) - Sir Henry Dale Fellow, CUBRIC, School of Psychology, Cardiff University, UK - Cited by 2,817 - Curio...

2. [‪Matthias Gruber‬ - ‪Google Scholar‬](https://scholar.google.com/citations?user=nPA2jxgAAAAJ&hl=en) - Matthias Gruber. Reader (Associate Professor), CUBRIC, School of Psychology, Cardiff University, UK....

3. [Gruber-2007.pdf](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/56150879/cc7b69d6-7c4c-446a-803d-09931f923aec/Gruber-2007.pdf?AWSAccessKeyId=ASIA2F3EMEYEY5YNTQ6K&Signature=VlGQc%2FbKFFHxRDp6xhLEXKFlshg%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIGmLFD7yX4odn5LL5gl%2BoE77qmltj8iYq%2Blnb7NUza73AiBnVyrte2N9mWvFuZhLwbqsYPpRG6XXOS7G4ZIaQJ%2FAmyr8BAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4oQlPjyES%2B0bzdHYKtAE%2FcB%2BtzKKwQ0sO7sbwWnPovCPhEhTspXrGDe%2BkeXz65UQqqGOVZKkef0509Q0I9xzE1WfG8HKsdnucsbK%2B7ZEaG4Y%2FheBxAKx%2B%2FJb5Bq%2BjJqHWqyDEsPzhnMAlAXjyf0AqGp9ubyrV%2F1IULG9jMO%2BxveXbVuVy2SN689LZFz0zGMg5TkDQBV9rRlwpgTbFbYb9sfHIMOLliGpKxTnZWgdQg48cmzSO9kLbEzaPgFUHZL6rx60e2Dtpoej48qhqWXGsC6UqbvK9lPUA88yll6eji%2BBzF7M6mOsI381Pd3%2BA2%2FoLPGyv08M%2FQPzBwKUub1DWdLcbLf6J4WxSL1GHkqLUZlBwhHm0QsDRq6T7S8uVL9x3d3BaVKOExFSkbX%2B1%2BGn6RhLrWfUrADEoL3kTjKqnLxj%2F%2F88wbEQEyZhikua4CEdVw%2F4oxS5dIhhvR3Q8ktOKKTUumYu%2BYJvp0ek3G5C5DfsMsqJw6UOQ0bRhIsFgWyG6VufHwfTBpVRZzmWDRXWMHQQscwwAJCSvj8lL%2BkhUkE4gvmxt%2FWwTZ2Iz%2FezvC%2FQ8ItTEmY8fEWBR6ct%2B3MFJCrfO8JdGzsW%2FmfYdFB0%2FpHl9%2Brk%2FoRvSpDRDT6lXfyEM1Un%2FabWJTdFixNDRQl7MeOJmV1ODtym4J%2Bba7VixXxuO%2FfnGvyJXnsW0Tt5UurBGB7IjxB%2BzYZnfyHHg0G25m2DJvGOzaALx0IOaLTzcRHplKYj0GzfkeotZ%2BdchUAwcJAg9Vhdx7qKLqtm5dpzr7bMHFYL%2FeBagyIyDfzEqjDAvtzMBjqZAREeOIkWQIiZ33IWoGLrVRz1QwRKKSw2ARlRoZarkEGoCQKmGcJ6Gv9VE08bMZr%2F0jkp6yEMp%2FkqtX1smbiBdYKvNctn%2Bv%2F1Z05EYustD2m6GKYy6UfmI1KdbK4D883oBS2BJao26v6MFRHlj%2FqJd%2BqVvxv2K6yCdZ7%2FqWBg7%2Ft%2BDSuBMdsxlaN%2F0Mn5THOrSHy%2Fyt0mJFxAiw%3D%3D&Expires=1771516473) - Microsoft Word - Gruber 2007 FNIAL.doc Aus dem Institut fr Informationssysteme des Gesundheitswesens...

4. [Gruber-2007-FNIAL.doc](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/56150879/9a4e1380-135f-445e-b482-f49b68cd94dd/Gruber-2007-FNIAL.doc?AWSAccessKeyId=ASIA2F3EMEYEY5YNTQ6K&Signature=MqCPfIJqoUJ3ESNFF4jwIh2hJlo%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIGmLFD7yX4odn5LL5gl%2BoE77qmltj8iYq%2Blnb7NUza73AiBnVyrte2N9mWvFuZhLwbqsYPpRG6XXOS7G4ZIaQJ%2FAmyr8BAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4oQlPjyES%2B0bzdHYKtAE%2FcB%2BtzKKwQ0sO7sbwWnPovCPhEhTspXrGDe%2BkeXz65UQqqGOVZKkef0509Q0I9xzE1WfG8HKsdnucsbK%2B7ZEaG4Y%2FheBxAKx%2B%2FJb5Bq%2BjJqHWqyDEsPzhnMAlAXjyf0AqGp9ubyrV%2F1IULG9jMO%2BxveXbVuVy2SN689LZFz0zGMg5TkDQBV9rRlwpgTbFbYb9sfHIMOLliGpKxTnZWgdQg48cmzSO9kLbEzaPgFUHZL6rx60e2Dtpoej48qhqWXGsC6UqbvK9lPUA88yll6eji%2BBzF7M6mOsI381Pd3%2BA2%2FoLPGyv08M%2FQPzBwKUub1DWdLcbLf6J4WxSL1GHkqLUZlBwhHm0QsDRq6T7S8uVL9x3d3BaVKOExFSkbX%2B1%2BGn6RhLrWfUrADEoL3kTjKqnLxj%2F%2F88wbEQEyZhikua4CEdVw%2F4oxS5dIhhvR3Q8ktOKKTUumYu%2BYJvp0ek3G5C5DfsMsqJw6UOQ0bRhIsFgWyG6VufHwfTBpVRZzmWDRXWMHQQscwwAJCSvj8lL%2BkhUkE4gvmxt%2FWwTZ2Iz%2FezvC%2FQ8ItTEmY8fEWBR6ct%2B3MFJCrfO8JdGzsW%2FmfYdFB0%2FpHl9%2Brk%2FoRvSpDRDT6lXfyEM1Un%2FabWJTdFixNDRQl7MeOJmV1ODtym4J%2Bba7VixXxuO%2FfnGvyJXnsW0Tt5UurBGB7IjxB%2BzYZnfyHHg0G25m2DJvGOzaALx0IOaLTzcRHplKYj0GzfkeotZ%2BdchUAwcJAg9Vhdx7qKLqtm5dpzr7bMHFYL%2FeBagyIyDfzEqjDAvtzMBjqZAREeOIkWQIiZ33IWoGLrVRz1QwRKKSw2ARlRoZarkEGoCQKmGcJ6Gv9VE08bMZr%2F0jkp6yEMp%2FkqtX1smbiBdYKvNctn%2Bv%2F1Z05EYustD2m6GKYy6UfmI1KdbK4D883oBS2BJao26v6MFRHlj%2FqJd%2BqVvxv2K6yCdZ7%2FqWBg7%2Ft%2BDSuBMdsxlaN%2F0Mn5THOrSHy%2Fyt0mJFxAiw%3D%3D&Expires=1771516473) - Aus dem Institut fr Informationssysteme des Gesundheitswesens Betreuer Hon. Prof. Dr. Roland Blomer ...

5. [VDM Modulare Delta Algorithmen für das praktische ... - Galaxus](https://www.galaxus.de/en/s12/product/modulare-delta-algorithmen-fuer-das-praktische-versionsmanagement-german-matthias-gruber-2010-refere-55234144) - This paper discusses modular delta algorithms ... SDelta (for Secure Delta) by the author ... Modula...

6. [Modulare Delta Algorithmen für das praktische ...](https://buecherinsel.buchkatalog.at/modulare-delta-algorithmen-fuer-das-praktische-versionsmanagement-9783639229288) - Modulare Delta Algorithmen für das praktische Versionsmanagement ... Zu dies ... Mehr anzeigen. Matt...

7. [Dissertation.Full.Update2016.pdf](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/56150879/ab6c24ec-e672-4747-8568-6c35f2a9a9d7/Dissertation.Full.Update2016.pdf?AWSAccessKeyId=ASIA2F3EMEYEY5YNTQ6K&Signature=Pg%2BjTDVG51iTDd76gohmWISVkeA%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIGmLFD7yX4odn5LL5gl%2BoE77qmltj8iYq%2Blnb7NUza73AiBnVyrte2N9mWvFuZhLwbqsYPpRG6XXOS7G4ZIaQJ%2FAmyr8BAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4oQlPjyES%2B0bzdHYKtAE%2FcB%2BtzKKwQ0sO7sbwWnPovCPhEhTspXrGDe%2BkeXz65UQqqGOVZKkef0509Q0I9xzE1WfG8HKsdnucsbK%2B7ZEaG4Y%2FheBxAKx%2B%2FJb5Bq%2BjJqHWqyDEsPzhnMAlAXjyf0AqGp9ubyrV%2F1IULG9jMO%2BxveXbVuVy2SN689LZFz0zGMg5TkDQBV9rRlwpgTbFbYb9sfHIMOLliGpKxTnZWgdQg48cmzSO9kLbEzaPgFUHZL6rx60e2Dtpoej48qhqWXGsC6UqbvK9lPUA88yll6eji%2BBzF7M6mOsI381Pd3%2BA2%2FoLPGyv08M%2FQPzBwKUub1DWdLcbLf6J4WxSL1GHkqLUZlBwhHm0QsDRq6T7S8uVL9x3d3BaVKOExFSkbX%2B1%2BGn6RhLrWfUrADEoL3kTjKqnLxj%2F%2F88wbEQEyZhikua4CEdVw%2F4oxS5dIhhvR3Q8ktOKKTUumYu%2BYJvp0ek3G5C5DfsMsqJw6UOQ0bRhIsFgWyG6VufHwfTBpVRZzmWDRXWMHQQscwwAJCSvj8lL%2BkhUkE4gvmxt%2FWwTZ2Iz%2FezvC%2FQ8ItTEmY8fEWBR6ct%2B3MFJCrfO8JdGzsW%2FmfYdFB0%2FpHl9%2Brk%2FoRvSpDRDT6lXfyEM1Un%2FabWJTdFixNDRQl7MeOJmV1ODtym4J%2Bba7VixXxuO%2FfnGvyJXnsW0Tt5UurBGB7IjxB%2BzYZnfyHHg0G25m2DJvGOzaALx0IOaLTzcRHplKYj0GzfkeotZ%2BdchUAwcJAg9Vhdx7qKLqtm5dpzr7bMHFYL%2FeBagyIyDfzEqjDAvtzMBjqZAREeOIkWQIiZ33IWoGLrVRz1QwRKKSw2ARlRoZarkEGoCQKmGcJ6Gv9VE08bMZr%2F0jkp6yEMp%2FkqtX1smbiBdYKvNctn%2Bv%2F1Z05EYustD2m6GKYy6UfmI1KdbK4D883oBS2BJao26v6MFRHlj%2FqJd%2BqVvxv2K6yCdZ7%2FqWBg7%2Ft%2BDSuBMdsxlaN%2F0Mn5THOrSHy%2Fyt0mJFxAiw%3D%3D&Expires=1771516473) - 1

8. [Matthias Gruber | A Generic Framework For Dis - DeutschlandCard](https://www.deutschlandcard.de/preisvergleich/p/9783838152233-matthias-gruber-a-generic-framework-for-discrete-simulation-based) - Finden Sie Matthias Gruber | A Generic Framework For Discrete Simulation Based bei eBay in der Kateg...

9. [cig06.pdf](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/56150879/1fc9e9d3-4579-47d8-8961-6dc55c4eadbf/cig06.pdf?AWSAccessKeyId=ASIA2F3EMEYEY5YNTQ6K&Signature=O0LkQSoGFwA7qGhRFX3FQCyO0SM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIGmLFD7yX4odn5LL5gl%2BoE77qmltj8iYq%2Blnb7NUza73AiBnVyrte2N9mWvFuZhLwbqsYPpRG6XXOS7G4ZIaQJ%2FAmyr8BAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4oQlPjyES%2B0bzdHYKtAE%2FcB%2BtzKKwQ0sO7sbwWnPovCPhEhTspXrGDe%2BkeXz65UQqqGOVZKkef0509Q0I9xzE1WfG8HKsdnucsbK%2B7ZEaG4Y%2FheBxAKx%2B%2FJb5Bq%2BjJqHWqyDEsPzhnMAlAXjyf0AqGp9ubyrV%2F1IULG9jMO%2BxveXbVuVy2SN689LZFz0zGMg5TkDQBV9rRlwpgTbFbYb9sfHIMOLliGpKxTnZWgdQg48cmzSO9kLbEzaPgFUHZL6rx60e2Dtpoej48qhqWXGsC6UqbvK9lPUA88yll6eji%2BBzF7M6mOsI381Pd3%2BA2%2FoLPGyv08M%2FQPzBwKUub1DWdLcbLf6J4WxSL1GHkqLUZlBwhHm0QsDRq6T7S8uVL9x3d3BaVKOExFSkbX%2B1%2BGn6RhLrWfUrADEoL3kTjKqnLxj%2F%2F88wbEQEyZhikua4CEdVw%2F4oxS5dIhhvR3Q8ktOKKTUumYu%2BYJvp0ek3G5C5DfsMsqJw6UOQ0bRhIsFgWyG6VufHwfTBpVRZzmWDRXWMHQQscwwAJCSvj8lL%2BkhUkE4gvmxt%2FWwTZ2Iz%2FezvC%2FQ8ItTEmY8fEWBR6ct%2B3MFJCrfO8JdGzsW%2FmfYdFB0%2FpHl9%2Brk%2FoRvSpDRDT6lXfyEM1Un%2FabWJTdFixNDRQl7MeOJmV1ODtym4J%2Bba7VixXxuO%2FfnGvyJXnsW0Tt5UurBGB7IjxB%2BzYZnfyHHg0G25m2DJvGOzaALx0IOaLTzcRHplKYj0GzfkeotZ%2BdchUAwcJAg9Vhdx7qKLqtm5dpzr7bMHFYL%2FeBagyIyDfzEqjDAvtzMBjqZAREeOIkWQIiZ33IWoGLrVRz1QwRKKSw2ARlRoZarkEGoCQKmGcJ6Gv9VE08bMZr%2F0jkp6yEMp%2FkqtX1smbiBdYKvNctn%2Bv%2F1Z05EYustD2m6GKYy6UfmI1KdbK4D883oBS2BJao26v6MFRHlj%2FqJd%2BqVvxv2K6yCdZ7%2FqWBg7%2Ft%2BDSuBMdsxlaN%2F0Mn5THOrSHy%2Fyt0mJFxAiw%3D%3D&Expires=1771516473) - Using Wearable Sensors for Real-time Recognition Tasks

10. [Using wearable sensors for real-time recognition ... - Keio University](https://keio.elsevierpure.com/ja/publications/using-wearable-sensors-for-real-time-recognition-tasks-in-games-o/) - Using wearable sensors for real-time recognition tasks in games of martial arts - An initial experim...

11. [LINDI-2011.pdf](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/56150879/be9966c7-009f-4df1-ad2e-0ad93ff1f829/LINDI-2011.pdf?AWSAccessKeyId=ASIA2F3EMEYEY5YNTQ6K&Signature=IAdU%2FImxvhFSxXqVmuQ7Bg2Q%2FIc%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIGmLFD7yX4odn5LL5gl%2BoE77qmltj8iYq%2Blnb7NUza73AiBnVyrte2N9mWvFuZhLwbqsYPpRG6XXOS7G4ZIaQJ%2FAmyr8BAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4oQlPjyES%2B0bzdHYKtAE%2FcB%2BtzKKwQ0sO7sbwWnPovCPhEhTspXrGDe%2BkeXz65UQqqGOVZKkef0509Q0I9xzE1WfG8HKsdnucsbK%2B7ZEaG4Y%2FheBxAKx%2B%2FJb5Bq%2BjJqHWqyDEsPzhnMAlAXjyf0AqGp9ubyrV%2F1IULG9jMO%2BxveXbVuVy2SN689LZFz0zGMg5TkDQBV9rRlwpgTbFbYb9sfHIMOLliGpKxTnZWgdQg48cmzSO9kLbEzaPgFUHZL6rx60e2Dtpoej48qhqWXGsC6UqbvK9lPUA88yll6eji%2BBzF7M6mOsI381Pd3%2BA2%2FoLPGyv08M%2FQPzBwKUub1DWdLcbLf6J4WxSL1GHkqLUZlBwhHm0QsDRq6T7S8uVL9x3d3BaVKOExFSkbX%2B1%2BGn6RhLrWfUrADEoL3kTjKqnLxj%2F%2F88wbEQEyZhikua4CEdVw%2F4oxS5dIhhvR3Q8ktOKKTUumYu%2BYJvp0ek3G5C5DfsMsqJw6UOQ0bRhIsFgWyG6VufHwfTBpVRZzmWDRXWMHQQscwwAJCSvj8lL%2BkhUkE4gvmxt%2FWwTZ2Iz%2FezvC%2FQ8ItTEmY8fEWBR6ct%2B3MFJCrfO8JdGzsW%2FmfYdFB0%2FpHl9%2Brk%2FoRvSpDRDT6lXfyEM1Un%2FabWJTdFixNDRQl7MeOJmV1ODtym4J%2Bba7VixXxuO%2FfnGvyJXnsW0Tt5UurBGB7IjxB%2BzYZnfyHHg0G25m2DJvGOzaALx0IOaLTzcRHplKYj0GzfkeotZ%2BdchUAwcJAg9Vhdx7qKLqtm5dpzr7bMHFYL%2FeBagyIyDfzEqjDAvtzMBjqZAREeOIkWQIiZ33IWoGLrVRz1QwRKKSw2ARlRoZarkEGoCQKmGcJ6Gv9VE08bMZr%2F0jkp6yEMp%2FkqtX1smbiBdYKvNctn%2Bv%2F1Z05EYustD2m6GKYy6UfmI1KdbK4D883oBS2BJao26v6MFRHlj%2FqJd%2BqVvxv2K6yCdZ7%2FqWBg7%2Ft%2BDSuBMdsxlaN%2F0Mn5THOrSHy%2Fyt0mJFxAiw%3D%3D&Expires=1771516473) - untitled

12. [Practical token retrieval and indexing from binary data ... - IEEE Xplore](https://ieeexplore.ieee.org/iel5/6026102/6031122/06031132.pdf) - Gruber et al. • Practical Token Retrieval and Indexing from Binary Data: An Application in Computer ...

13. [Langfassung_ASIM2009.pdf](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/56150879/023cc5ad-50d8-4406-b177-244e64824799/Langfassung_ASIM2009.pdf?AWSAccessKeyId=ASIA2F3EMEYEY5YNTQ6K&Signature=CyYyYScTpuz0VakAFGc%2Fko%2FDcx4%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIGmLFD7yX4odn5LL5gl%2BoE77qmltj8iYq%2Blnb7NUza73AiBnVyrte2N9mWvFuZhLwbqsYPpRG6XXOS7G4ZIaQJ%2FAmyr8BAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4oQlPjyES%2B0bzdHYKtAE%2FcB%2BtzKKwQ0sO7sbwWnPovCPhEhTspXrGDe%2BkeXz65UQqqGOVZKkef0509Q0I9xzE1WfG8HKsdnucsbK%2B7ZEaG4Y%2FheBxAKx%2B%2FJb5Bq%2BjJqHWqyDEsPzhnMAlAXjyf0AqGp9ubyrV%2F1IULG9jMO%2BxveXbVuVy2SN689LZFz0zGMg5TkDQBV9rRlwpgTbFbYb9sfHIMOLliGpKxTnZWgdQg48cmzSO9kLbEzaPgFUHZL6rx60e2Dtpoej48qhqWXGsC6UqbvK9lPUA88yll6eji%2BBzF7M6mOsI381Pd3%2BA2%2FoLPGyv08M%2FQPzBwKUub1DWdLcbLf6J4WxSL1GHkqLUZlBwhHm0QsDRq6T7S8uVL9x3d3BaVKOExFSkbX%2B1%2BGn6RhLrWfUrADEoL3kTjKqnLxj%2F%2F88wbEQEyZhikua4CEdVw%2F4oxS5dIhhvR3Q8ktOKKTUumYu%2BYJvp0ek3G5C5DfsMsqJw6UOQ0bRhIsFgWyG6VufHwfTBpVRZzmWDRXWMHQQscwwAJCSvj8lL%2BkhUkE4gvmxt%2FWwTZ2Iz%2FezvC%2FQ8ItTEmY8fEWBR6ct%2B3MFJCrfO8JdGzsW%2FmfYdFB0%2FpHl9%2Brk%2FoRvSpDRDT6lXfyEM1Un%2FabWJTdFixNDRQl7MeOJmV1ODtym4J%2Bba7VixXxuO%2FfnGvyJXnsW0Tt5UurBGB7IjxB%2BzYZnfyHHg0G25m2DJvGOzaALx0IOaLTzcRHplKYj0GzfkeotZ%2BdchUAwcJAg9Vhdx7qKLqtm5dpzr7bMHFYL%2FeBagyIyDfzEqjDAvtzMBjqZAREeOIkWQIiZ33IWoGLrVRz1QwRKKSw2ARlRoZarkEGoCQKmGcJ6Gv9VE08bMZr%2F0jkp6yEMp%2FkqtX1smbiBdYKvNctn%2Bv%2F1Z05EYustD2m6GKYy6UfmI1KdbK4D883oBS2BJao26v6MFRHlj%2FqJd%2BqVvxv2K6yCdZ7%2FqWBg7%2Ft%2BDSuBMdsxlaN%2F0Mn5THOrSHy%2Fyt0mJFxAiw%3D%3D&Expires=1771516473) - Beitrag ASIM 2001

14. [MatthiasGruber3036090.pdf](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_a2bd7b13-2402-4fdf-9ae0-3fe78c707391/0534a057-8e32-45bd-813c-e150a760416b/MatthiasGruber3036090.pdf?AWSAccessKeyId=ASIA2F3EMEYEY5YNTQ6K&Signature=EDaWRoRtuSbWFv1OEvGWGiIo%2BFo%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIGmLFD7yX4odn5LL5gl%2BoE77qmltj8iYq%2Blnb7NUza73AiBnVyrte2N9mWvFuZhLwbqsYPpRG6XXOS7G4ZIaQJ%2FAmyr8BAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4oQlPjyES%2B0bzdHYKtAE%2FcB%2BtzKKwQ0sO7sbwWnPovCPhEhTspXrGDe%2BkeXz65UQqqGOVZKkef0509Q0I9xzE1WfG8HKsdnucsbK%2B7ZEaG4Y%2FheBxAKx%2B%2FJb5Bq%2BjJqHWqyDEsPzhnMAlAXjyf0AqGp9ubyrV%2F1IULG9jMO%2BxveXbVuVy2SN689LZFz0zGMg5TkDQBV9rRlwpgTbFbYb9sfHIMOLliGpKxTnZWgdQg48cmzSO9kLbEzaPgFUHZL6rx60e2Dtpoej48qhqWXGsC6UqbvK9lPUA88yll6eji%2BBzF7M6mOsI381Pd3%2BA2%2FoLPGyv08M%2FQPzBwKUub1DWdLcbLf6J4WxSL1GHkqLUZlBwhHm0QsDRq6T7S8uVL9x3d3BaVKOExFSkbX%2B1%2BGn6RhLrWfUrADEoL3kTjKqnLxj%2F%2F88wbEQEyZhikua4CEdVw%2F4oxS5dIhhvR3Q8ktOKKTUumYu%2BYJvp0ek3G5C5DfsMsqJw6UOQ0bRhIsFgWyG6VufHwfTBpVRZzmWDRXWMHQQscwwAJCSvj8lL%2BkhUkE4gvmxt%2FWwTZ2Iz%2FezvC%2FQ8ItTEmY8fEWBR6ct%2B3MFJCrfO8JdGzsW%2FmfYdFB0%2FpHl9%2Brk%2FoRvSpDRDT6lXfyEM1Un%2FabWJTdFixNDRQl7MeOJmV1ODtym4J%2Bba7VixXxuO%2FfnGvyJXnsW0Tt5UurBGB7IjxB%2BzYZnfyHHg0G25m2DJvGOzaALx0IOaLTzcRHplKYj0GzfkeotZ%2BdchUAwcJAg9Vhdx7qKLqtm5dpzr7bMHFYL%2FeBagyIyDfzEqjDAvtzMBjqZAREeOIkWQIiZ33IWoGLrVRz1QwRKKSw2ARlRoZarkEGoCQKmGcJ6Gv9VE08bMZr%2F0jkp6yEMp%2FkqtX1smbiBdYKvNctn%2Bv%2F1Z05EYustD2m6GKYy6UfmI1KdbK4D883oBS2BJao26v6MFRHlj%2FqJd%2BqVvxv2K6yCdZ7%2FqWBg7%2Ft%2BDSuBMdsxlaN%2F0Mn5THOrSHy%2Fyt0mJFxAiw%3D%3D&Expires=1771516473)

15. [Emergenz Des Bewusstseins book by Matthias Gruber - ThriftBooks](https://www.thriftbooks.com/w/emergenz-des-bewusstseins_matthias-gruber/24985026/) - Emergenz des Bewusstseins [German]. By Matthias Gruber. $32.54. Format: Hardcover. Condition: New.

16. [ISBN 9781326652074 - Emergenz des Bewusstseins](https://isbnsearch.org/isbn/9781326652074) - Emergenz des Bewusstseins. ISBN-13: 9781326652074. ISBN-10: 1326652079. Author: Matthias Gruber. Bin...

17. [Matthias Gruber - Books and Publications Spotlight | Lulu](https://www.lulu.com/spotlight/WingChun) - ByMatthias Gruber. Published 8/5/2018. Paperback. 12.94 USD. product thumbnail · Ringe des Lebens - ...

18. [The Billion Year Countdown - Gruber, Matthias - morawa.at](https://www.morawa.at/detail/ISBN-9780244105471/Gruber-Matthias/The-Billion-Year-Countdown) - The Billion Year Countdown von Gruber, Matthias ✓ Gratisversand mit Kundenkarte ✓ Blitzschnelle Lief...

19. [The Billion Year Countdown - Gruber, Matthias - Hugendubel ...](https://www.hugendubel.info/detail/ISBN-9780244105471/Gruber-Matthias/The-Billion-Year-Countdown) - The Billion Year Countdown ; TaschenbuchKartoniert, Paperback ; EUR15,80 ; Beschreibung. Just a few ...

20. [Ringe des Lebens - Die Geschichte der X - Lulu](https://www.lulu.com/shop/matthias-gruber/ringe-des-lebens-die-geschichte-der-x/paperback/product-1g294gqk.html) - Matthias Gruber is a software professional and former researcher, specialized in biomedical informat...

21. [Ringe des Lebens - Das Erbe der X by Matthias Gruber ... - Dymocks](https://www.dymocks.com.au/ringe-des-lebens-das-erbe-der-x-by-matthias-gruber-9780244656249) - Ringe des Lebens - Das Erbe der X. Home Ringe des ... Lulu.com. Publication Date, 13 Jan 2018. Autho...

22. [Ringe des Lebens - Die Zukunft der X book by Matthias Gruber](https://www.thriftbooks.com/w/ringe-des-lebens---die-zukunft-der-x_matthias-gruber/36701215/) - Ringe des Lebens - Die Zukunft der X [German]... By Matthias Gruber. $30.15. Format: Paperback. Cond...

23. [Simulation Based Optimization Parametric Optimiza .pdf](https://proyectoisi.frc.utn.edu.ar/book/scholarship/fetch.php/simulation_based_optimization_parametric_optimiza.pdf)

24. [Diplomarbeit_Knabl.pdf](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/56150879/b414a8a1-0b22-436f-9937-6a4dc6cd488f/Diplomarbeit_Knabl.pdf?AWSAccessKeyId=ASIA2F3EMEYEY5YNTQ6K&Signature=0WFqn0Yi06meLayjLKIoIoEQrOo%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIGmLFD7yX4odn5LL5gl%2BoE77qmltj8iYq%2Blnb7NUza73AiBnVyrte2N9mWvFuZhLwbqsYPpRG6XXOS7G4ZIaQJ%2FAmyr8BAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4oQlPjyES%2B0bzdHYKtAE%2FcB%2BtzKKwQ0sO7sbwWnPovCPhEhTspXrGDe%2BkeXz65UQqqGOVZKkef0509Q0I9xzE1WfG8HKsdnucsbK%2B7ZEaG4Y%2FheBxAKx%2B%2FJb5Bq%2BjJqHWqyDEsPzhnMAlAXjyf0AqGp9ubyrV%2F1IULG9jMO%2BxveXbVuVy2SN689LZFz0zGMg5TkDQBV9rRlwpgTbFbYb9sfHIMOLliGpKxTnZWgdQg48cmzSO9kLbEzaPgFUHZL6rx60e2Dtpoej48qhqWXGsC6UqbvK9lPUA88yll6eji%2BBzF7M6mOsI381Pd3%2BA2%2FoLPGyv08M%2FQPzBwKUub1DWdLcbLf6J4WxSL1GHkqLUZlBwhHm0QsDRq6T7S8uVL9x3d3BaVKOExFSkbX%2B1%2BGn6RhLrWfUrADEoL3kTjKqnLxj%2F%2F88wbEQEyZhikua4CEdVw%2F4oxS5dIhhvR3Q8ktOKKTUumYu%2BYJvp0ek3G5C5DfsMsqJw6UOQ0bRhIsFgWyG6VufHwfTBpVRZzmWDRXWMHQQscwwAJCSvj8lL%2BkhUkE4gvmxt%2FWwTZ2Iz%2FezvC%2FQ8ItTEmY8fEWBR6ct%2B3MFJCrfO8JdGzsW%2FmfYdFB0%2FpHl9%2Brk%2FoRvSpDRDT6lXfyEM1Un%2FabWJTdFixNDRQl7MeOJmV1ODtym4J%2Bba7VixXxuO%2FfnGvyJXnsW0Tt5UurBGB7IjxB%2BzYZnfyHHg0G25m2DJvGOzaALx0IOaLTzcRHplKYj0GzfkeotZ%2BdchUAwcJAg9Vhdx7qKLqtm5dpzr7bMHFYL%2FeBagyIyDfzEqjDAvtzMBjqZAREeOIkWQIiZ33IWoGLrVRz1QwRKKSw2ARlRoZarkEGoCQKmGcJ6Gv9VE08bMZr%2F0jkp6yEMp%2FkqtX1smbiBdYKvNctn%2Bv%2F1Z05EYustD2m6GKYy6UfmI1KdbK4D883oBS2BJao26v6MFRHlj%2FqJd%2BqVvxv2K6yCdZ7%2FqWBg7%2Ft%2BDSuBMdsxlaN%2F0Mn5THOrSHy%2Fyt0mJFxAiw%3D%3D&Expires=1771516473) - Diplomarbeit Fachhochschule FH JOANNEUM Gesellschaft mbH Semantic Web in Unternehmen Effizienter Ein...

25. [sustainable-leadership-in-an-agile-environment.docx](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/56150879/8e69941c-e30b-47bc-a05d-c599129cb9b1/sustainable-leadership-in-an-agile-environment.docx?AWSAccessKeyId=ASIA2F3EMEYEY5YNTQ6K&Signature=pyo5vpM%2BJLKWSNnuvPkcFlviqp4%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIGmLFD7yX4odn5LL5gl%2BoE77qmltj8iYq%2Blnb7NUza73AiBnVyrte2N9mWvFuZhLwbqsYPpRG6XXOS7G4ZIaQJ%2FAmyr8BAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4oQlPjyES%2B0bzdHYKtAE%2FcB%2BtzKKwQ0sO7sbwWnPovCPhEhTspXrGDe%2BkeXz65UQqqGOVZKkef0509Q0I9xzE1WfG8HKsdnucsbK%2B7ZEaG4Y%2FheBxAKx%2B%2FJb5Bq%2BjJqHWqyDEsPzhnMAlAXjyf0AqGp9ubyrV%2F1IULG9jMO%2BxveXbVuVy2SN689LZFz0zGMg5TkDQBV9rRlwpgTbFbYb9sfHIMOLliGpKxTnZWgdQg48cmzSO9kLbEzaPgFUHZL6rx60e2Dtpoej48qhqWXGsC6UqbvK9lPUA88yll6eji%2BBzF7M6mOsI381Pd3%2BA2%2FoLPGyv08M%2FQPzBwKUub1DWdLcbLf6J4WxSL1GHkqLUZlBwhHm0QsDRq6T7S8uVL9x3d3BaVKOExFSkbX%2B1%2BGn6RhLrWfUrADEoL3kTjKqnLxj%2F%2F88wbEQEyZhikua4CEdVw%2F4oxS5dIhhvR3Q8ktOKKTUumYu%2BYJvp0ek3G5C5DfsMsqJw6UOQ0bRhIsFgWyG6VufHwfTBpVRZzmWDRXWMHQQscwwAJCSvj8lL%2BkhUkE4gvmxt%2FWwTZ2Iz%2FezvC%2FQ8ItTEmY8fEWBR6ct%2B3MFJCrfO8JdGzsW%2FmfYdFB0%2FpHl9%2Brk%2FoRvSpDRDT6lXfyEM1Un%2FabWJTdFixNDRQl7MeOJmV1ODtym4J%2Bba7VixXxuO%2FfnGvyJXnsW0Tt5UurBGB7IjxB%2BzYZnfyHHg0G25m2DJvGOzaALx0IOaLTzcRHplKYj0GzfkeotZ%2BdchUAwcJAg9Vhdx7qKLqtm5dpzr7bMHFYL%2FeBagyIyDfzEqjDAvtzMBjqZAREeOIkWQIiZ33IWoGLrVRz1QwRKKSw2ARlRoZarkEGoCQKmGcJ6Gv9VE08bMZr%2F0jkp6yEMp%2FkqtX1smbiBdYKvNctn%2Bv%2F1Z05EYustD2m6GKYy6UfmI1KdbK4D883oBS2BJao26v6MFRHlj%2FqJd%2BqVvxv2K6yCdZ7%2FqWBg7%2Ft%2BDSuBMdsxlaN%2F0Mn5THOrSHy%2Fyt0mJFxAiw%3D%3D&Expires=1771516473) - Actually i wanted to call this book SUSTAINABLE LEADERSHIP in a volatile environment, but i didnt wa...

26. [Marc Gruber](https://scholar.google.com/citations?user=_iOa_HAAAAAJ&hl=en) - Prof. of Entrepreneurship & Technology Commercialization - Cited by 14,774 - entrepreneurship - stra...

