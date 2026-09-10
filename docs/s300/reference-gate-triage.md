<!-- Action: await-user-decision -->
<!-- Tracked-by: AIW-204 -->
# FMT reference gate — the 65 needs-review rows, triaged (S300)

The FMT master entered `verify_references.py`'s corpus for the first time this session (`AIW-204`).
Of its 229 references, **164 verified clean and 65 came back needs-review**. None were auto-resolved:
each is an editorial call on a citation in the paper. They fall into three buckets, and only bucket C
needs real thought.

## A — Crossref matched a DIFFERENT WORK (8). Almost certainly not our error.

These have a low title similarity **and** a different first author, which is the signature of a fuzzy
match against a work that has nothing to do with ours — typically because the reference is a **book,
chapter, blog post or preprint that Crossref does not index**. Example: `fmt:Aaronson2014` is a
Shtetl-Optimized blog post and Crossref returned *Jane Austen, Game Theorist*.
**Recommended disposition: mark verified-by-hand with a note, or teach the gate to skip DOI-less
non-journal references rather than fuzzy-matching them** — the second is the real fix, since this
bucket will regenerate on every run.

| key | our first author / year | what Crossref returned | title score |
|---|---|---|---|
| `fmt:Aaronson2014` | Aaronson 2014 | Chwe — Jane Austen, Game Theorist | 0.417 |
| `fmt:Anthropic2025` | Anthropic 2025 | Campiranon — Conclusion: Exploring New Frontiers: Research Priorities for | 0.389 |
| `fmt:Bach2026` | Bach 2026 | Percy — Machine Consciousness and Mind Uploading | 0.508 |
| `fmt:Butlin2023` | Butlin 2023 |  — The Computer Representation of an Artificial Consciousness | 0.468 |
| `fmt:Heitmann2022` | Heitmann 2022 | Grüsser — Migraine phosphenes and the retino-cortical magnification fa | 0.549 |
| `fmt:Milner1962` | Milner 1962 | Arzimanoglou — Rôle des troubles de l’attention dans les difficultés d’appr | 0.492 |
| `fmt:Nemirow1990` | Nemirow 1990 | Hallett — Physicalism, Reductionism &amp; Hilbert | 0.488 |
| `fmt:Siclari2021` | Siclari 2021 | Betta — Cortical and subcortical hemodynamic changes during sleep sl | 0.329 |

## B — same work, metadata nuance (50). Low risk.

Title similarity is high or the first author agrees, so Crossref found *our* work and differs on a
detail — a subtitle, an `et al.` expansion, a preprint-vs-published year, a volume for an online-first
article. **Recommended: spot-check the year/volume ones, accept the rest.**

| key | disagreement |
|---|---|
| `fmt:Alnagger2026` | authors not on the record: Timmermann, Iotzov, Selen, Mediano, Friston |
| `fmt:Baars1988` | first author, year |
| `fmt:Barrett2019` | title, volume, authors not on the record: Mediano |
| `fmt:Brodmann1909` | first author, authors not on the record: Brodmann |
| `fmt:COGITATEConsortium2025` | first author, authors not on the record: COGITATE Consortium |
| `fmt:Chalmers1996` | first author |
| `fmt:Chalmers2018` | title |
| `fmt:Coleman2014` | title |
| `fmt:Damasio1999` | first author, authors not on the record: Damasio |
| `fmt:Damasio2010` | first author, year, authors not on the record: Damasio |
| `fmt:Dehaene2001` | authors not on the record: Naccache |
| `fmt:Dehaene2021` | first author, authors not on the record: Dehaene |
| `fmt:Dennett1991` | first author, year |
| `fmt:Dresler2012` | title |
| `fmt:Frankish2016` | first author, year |
| `fmt:Friston2010` | title |
| `fmt:GodfreySmith2016` | first author, year, authors not on the record: Godfrey-Smith |
| `fmt:Goff2019` | first author, year, authors not on the record: Goff |
| `fmt:Gruber2026b` | title, year |
| `fmt:Gruber2026d` | title |
| `fmt:Hengen2025` | title |
| `fmt:Hinton1986` | title, year, authors not on the record: McClelland, Rumelhart |
| `fmt:Hofstadter2007` | first author |
| `fmt:Huxley1874` | year |
| `fmt:Kleiner2024` | title |
| `fmt:Klver1966` | first author, year, authors not on the record: Klüver |
| `fmt:Kriegel2006` | first author |
| `fmt:Kriegeskorte2008` | authors not on the record: Mur, Bandettini |
| `fmt:LaBerge1985` | first author, year |
| `fmt:Lashley1950` | year |
| `fmt:Lewis1988` | first author, year |
| `fmt:Llins1998` | first author |
| `fmt:Loar1997` | year |
| `fmt:Long2024` | title, year |
| `fmt:Lynn2012` | title |
| `fmt:Metzinger2003` | title, year |
| `fmt:Metzinger2009` | first author |
| `fmt:Mukhametov1977` | authors not on the record: A.Ya |
| `fmt:Myers1958` | authors not on the record: Sperry |
| `fmt:Nagel1974` | title |
| `fmt:Northoff2020` | title, year |
| `fmt:Penrose1994` | first author, year, volume, authors not on the record: Penrose |
| `fmt:Pribram1991` | first author |
| `fmt:Safron2020` | title |
| `fmt:Seth2021` | title, first author, authors not on the record: Seth |
| `fmt:Strawson2006` | year |
| `fmt:Toker2026` | authors not on the record: Pappas, Lendner, Sichani, Schwartz, D'Agostino, Bhatt, Bhatt, Suthana |
| `fmt:Tononi1998` | authors not on the record: Edelman |
| `fmt:Weiskrantz1986` | title, year |
| `fmt:Zheng2025` | title |

## C — ambiguous, needs a human eye (7). This is the real work.

Neither clearly a mismatch nor clearly the same record. **Check these against the actual source.**

| key | our first author / year | Crossref | title score | disagreement |
|---|---|---|---|---|
| `fmt:Andrews2024` | Andrews 2024 | Levy — About time: science and a declaration of animal co | 0.759 | title, first author, year, authors not on the record: Andrews, Birch, Sebo |
| `fmt:Barrett2026` | Barrett 2026 | Marlowe — Drug Courts: The Good, the Bad, and the Misunderst | 0.678 | title, first author, year, authors not on the record: Barrett, Milinkovic, Mediano, Rosas, Bor, Barnett, Seth |
| `fmt:Fitz2025` | Fitz 2025 | Pagel — Testing for Machine Consciousness | 0.779 | title, first author, year, authors not on the record: Fitz |
| `fmt:Graziano2013` | Graziano 2013 | Catenaccio — Consciousness and the Social Brain by Michael S. A | 0.687 | title, first author, year, authors not on the record: Graziano |
| `fmt:Gruber2015` | Gruber 2015 | Pesso — Die Bühnen des Bewusstseins | 0.821 | title, first author, year, authors not on the record: Gruber |
| `fmt:IITConcerned2025` | IIT-Concerned 2025 |  — What makes a theory of consciousness unscientific? | 0.766 | title, first author |
| `fmt:VanRullen2003` | Van Rullen 2003 | VanRullen — Is perception discrete or continuous? | 0.649 | title |

## The durable fix worth considering

Bucket A regenerates on every `--update` because the gate fuzzy-matches references that have no
business being in Crossref. A `type: book|chapter|blog|preprint` marker, or simply skipping
DOI-less references whose title score falls below a floor, would keep the gate's red state meaningful.
As it stands, a permanently-red gate is one nobody reads — which is how the original omission
survived.


## Assessment of bucket C — read from the Crossref metadata, S300

I went through all seven. **None of them looks like an error in the paper's reference list**, and five are
really bucket-A cases that the low-title-score heuristic put here because Crossref returned something
*topically adjacent* rather than something random:

| key | what Crossref actually returned | assessment |
|---|---|---|
| `fmt:Andrews2024` | Levy, *About time: science and a declaration of animal co…* | A **commentary on** the New York Declaration on Animal Consciousness, not the Declaration itself. Our reference (Andrews, Birch, Sebo) is the Declaration. Crossref match is wrong. |
| `fmt:Barrett2026` | Marlowe, *Drug Courts: The Good, the Bad…* | Unrelated. Our reference (Barrett, Milinkovic, Mediano, Rosas, Bor, Barnett, Seth) is a consciousness paper. Crossref match is wrong. |
| `fmt:Fitz2025` | Pagel, *Testing for Machine Consciousness* | A **different paper on the same topic**. Ours is Fitz. Worth one look, but the author mismatch says wrong record. |
| `fmt:Graziano2013` | Catenaccio, *Consciousness and the Social Brain by Michael S. A…* | A **book review of** Graziano's book. Ours is the book. Crossref indexes the review, not the monograph. |
| `fmt:Gruber2015` | Pesso, *Die Bühnen des Bewusstseins* | **MG's own 2015 German monograph is not in Crossref.** A different German-titled book matched. Definitively a non-error. |
| `fmt:IITConcerned2025` | *What makes a theory of consciousness unscientific?* | **This is the right paper.** The disagreement is that it has a consortium author, so Crossref carries no single first author against our `IIT-Concerned` key. Benign. |
| `fmt:VanRullen2003` | VanRullen, *Is perception discrete or continuous?* | **Right paper, right author** — `VanRullen` vs our `Van Rullen` spacing, plus a stored-title difference. Benign; worth aligning the stored title string. |

⚠ **Confidence and its limit:** this is read off the Crossref metadata the gate stored, **not** from
re-opening each source. The pattern is unambiguous in five cases (review-of, commentary-on, wrong-work) and
the two benign ones are self-evident. `fmt:Fitz2025` is the only one I would actually re-check against the
source before signing it off.

⇒ **So the honest summary is: the gate found no bad references in the FMT master, and 65 rows of noise.**
That does not make the exercise worthless — it establishes a clean baseline for the paper for the first
time, and the noise is a fixable property of the gate rather than of the paper. But it does mean the
durable fix below matters more than adjudicating the 65: a gate that is red for structural reasons teaches
people to ignore it, which is the failure mode that let the FMT master go unchecked in the first place.
