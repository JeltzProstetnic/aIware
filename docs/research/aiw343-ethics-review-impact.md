# AIW-343: what happens if no ethics committee reviews the study (Fable, S361 2026-10-26)

Question from MG: *"As a private person in Austria I can run any questionnaire with any volunteer, interpret the data and publish it as I want as long as it is anonymous. Only journal publication is affected, and the study would have to be redone at some point."*
Not legal advice. Labels: [V] verified from a source, [I] inference.

## Verdict
MG is right about Austrian law. He is wrong on three points:
1. GDPR applies at the moment of collection, because the survey collects special-category (Art. 9) data.
2. The public dataset from the colleague arm is not yet anonymous.
3. A redo is not the only fallback. A prior exempt determination costs days and €0–900.

## 1. Austrian law: no approval requirement
- [V] UG 2002 §30 requires ethics committees only at universities with a medical faculty, and only for clinical trials, new medical methods and applied medical research on humans.
- [V] KAKuG §8c applies to hospital operators, with the same medical scope. AMG and MPG cover only drugs and medical devices.
- [V] FOG §2d is a data-protection clause and requires no ethics committee.
  - Under §2b Z 12, a "wissenschaftliche Einrichtung" includes natural persons pursuing Art. 89(1) GDPR purposes, so MG qualifies personally.
  - Under §2d(7), compliant processing needs no approval from the data protection authority (DSB).
- [V] DSG §7(2): consent is a sufficient basis.
- [V] Secondary sources: Austria regulates ethics review for biomedical research but not for social-science research (Wien Klin Wochenschr 2024; SATORI Austria report).
- [I] The Psychologengesetz is not triggered, because no individual diagnosis or feedback is given.
- [I] The Verein (ZVR pending) has no legal personality yet, so MG acts personally.

## 2. GDPR/DSG: where MG is actually exposed
- [V/I] Art. 9 is engaged by:
  - religiosity items and the R-PBS religious subscale (religious beliefs);
  - dualism and mind–brain statements (philosophical beliefs);
  - migraine aura, visual snow, tinnitus and medication flags, DES-B and O-LIFE (health data).
- [V] EDPB Guidelines 02/2026 on anonymisation, §38: producing anonymous data is itself processing. It needs a legal basis under Art. 6, and an Art. 9(2) exemption for special-category data. Under the relative "contextual approach" (C-413/23 P, para 82), the stored dataset can still be anonymous for MG once no means of linking remain.
- **Zero-cost fix:** base the collection step on explicit consent, Art. 6(1)(a) + 9(2)(a); the required consent checkbox already is one.
  - In `consent-and-info.md`, replace "they are not personal data under the GDPR" with "we treat your answers as anonymous; where the GDPR applies, the legal basis is your explicit consent".
- Remaining exposure points:
  - (a) IP logging is off in LimeSurvey [V, hosting-spec], but the reverse proxy, Keycloak, the firewall and the VPS provider's logs still need checking.
  - (b) Turn on LimeSurvey "Anonymized responses". It sets submitdate to 1980-01-01 to defeat log matching [V, LimeSurvey manual]. Store per-page durations only.
  - (c) **The genuine defect is re-identification in the colleague arm (Arm C).**
    - 3 age bands × 5 gender options × rare flags, among about 200 colleagues, will produce unique rows.
    - EDPB tests singling-out by someone with background knowledge [V].
    - Fix before the OSF deposit: k ≥ 5 on quasi-identifiers; collapse gender to 3 options and the flags to "any diagnosed"; leave the arm indicator out of the public file. Free text is never published (already the plan).
  - (d) The Part-2 email form collects personal data. It needs consent, an Art. 13 notice and a processor agreement with the VPS host.
  - (e) An invitee list taken from the employer directory is the employer's data (purpose limitation). Cover this in the employer clearance.
  - (f) Do not name Ivoclar in claims about its staff. This is a reputational risk, not a GDPR one.

## 3. Employer (Ivoclar AG, Schaan: Liechtenstein law)
- [V, secondary] Under the Mitwirkungsgesetz, co-determination is required only for mass dismissals, transfers, and health and safety. [V] Austrian ArbVG §96(1) Z 2 covers personnel questionnaires that the employer introduces.
- [I] A private study that the employer neither commissions nor receives data from triggers neither law. What matters:
  - IT acceptable use: permission for company email, intranet or work time;
  - pressure from the dependent relationship (Helsinki 2024);
  - the employer not wanting to be attributed.
- Get written clearance from the line manager or HR, recruit through private channels, and use no company branding.

## 4. Publication, venue by venue [V]
| Venue | Policy | Prior approval needed? |
|---|---|---|
| PLOS ONE | Approval documents at submission; exemptions only by an IRB or equivalent; retrospective approval refused | Effectively yes |
| Elsevier (Consciousness and Cognition) | A national-law exemption statement explaining why is explicitly allowed | No |
| Frontiers | Must state reasons; may request a waiver letter from an ethics committee | Risky without one |
| OUP Neuroscience of Consciousness | State and explain why approval is not required | No, expect queries |
| JCS | No requirement found | No |
| PsyArXiv / OSF / Zenodo | Scope moderation only | No |

Norms:
- ICMJE: seek approval from an independent body.
- Helsinki 2024 §23: review before the study begins.
- COPE: retrospective approval only in exceptional circumstances.
- APA 8.01 binds only "when institutional approval is required".

Alternatives to a redo:
1. UMIT RCSEQ shortened procedure via Netzer: takes days, no fee listed; an external applicant cannot file alone.
2. The DGPs/TransMIT committee: the applicant needs a doctorate in psychology; €953 for non-members. Netzer could carry the application.
3. A US commercial IRB exempt determination: Pearl IRB about $580, Solutions IRB about $925. Whether they accept a non-US independent applicant is unconfirmed; ask by email.
4. Retrospective approval: not a plan.
5. [I] Two-stage fallback: if review fails, demote Arm C to a documented pilot (preprint only) and run Arm P after review as the journal study.

## 5. Least-cost recommendation
1. File the RCSEQ Stammblatt via Netzer before fielding. If he declines, get a commercial exempt determination (~$600–950). Never field first.
2. Fix the consent wording, turn on anonymized responses and check the logs, and apply the k-anonymity rule to the OSF file.
3. Get written employer clearance, recruit through private channels, and leave the employer unnamed.

A lawyer is not needed for the statute question. One hour would be worth it if HR raises the MWG, or if MG wants to keep the "not personal data" claim.
