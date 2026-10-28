<!-- AIW-343 Part 1 questionnaire — master text (EN). PRIVATE until data collection closes. Item IDs are the column names the analysis script expects (scripts/aiw343_analysis.py). Scale names are NEVER shown to participants. -->
# Part 1 questionnaire — master text (draft v0.1, S358)

Language: **English first**; DE, IT, FR later (each a separate translation step with licence checks).

Shown title: **Perception and beliefs about the mind — a short survey** (about 25 minutes)

Implementation notes for the survey platform are in `hosting-spec.md`. Every page has a progress bar. Every item has a "prefer not to answer" option unless marked *required*. Response order inside a scale is randomised per participant unless marked *fixed*.

---

## Page 0 — Information and consent
Text: `consent-and-info.md`. Single required checkbox: *"I have read the information, I am 18 or older, and I agree to take part."* No → polite exit page.

## Page 1 — About you (fixed order)
- `age_band` — 18–34 / 35–49 / 50+ *(coarse on purpose: with ~200 colleagues from one employer, finer demographics could identify people)*
- `gender` — woman / man / non-binary / prefer to self-describe / prefer not to say
- `phil1` "How familiar are you with philosophy of mind (e.g. the mind–body problem)?" 1 not at all – 5 very
- `phil2` "Have you ever taken a course or read a book on consciousness or philosophy of mind?" no / one / several
- `phil3` "Before today, had you heard of the 'hard problem of consciousness'?" no / yes, vaguely / yes, well
- `med1` "Do you meditate or practise a similar mental technique?" never / tried it / occasionally / regularly (≥ weekly)
- `med2` "If yes, for how many years in total?" number (0 allowed)
- `sleep1` "Over the past month, how would you rate your sleep quality overall?" 1 very bad – 5 very good

## Block order (randomised per participant, 50/50)
- **Order A:** Page 2 (PLI) → Page 3 (filler) → Page 4 (beliefs) → Page 5 (covariates)
- **Order B:** Page 4 (beliefs) → Page 3 (filler) → Page 2 (PLI) → Page 5 (covariates)
Store `block_order` = A/B.

## Page 2 — Everyday perception (Processing-Leak Inventory, PLI)
**Optional demonstration (30 s), shown first:** *"A quick demonstration before the questions. Close your left eye and look at the cross with your right eye. Move closer to or further from the screen slowly. At some distance the dot disappears — that is your blind spot. Now do the same with the second picture: at that distance the gap in the line disappears too. On a phone, turn it sideways first; the demonstration works best on a computer screen."* [graphic: `blindspot-demo.svg`, upload as survey resource.] *(Wording kept mechanism-free on purpose: in block order A the demo precedes the belief questions, so explaining 'the brain fills in' could prime the hidden-depth items.)* Button: *"Done / skip."* Store `demo_done` (0/1) and `demo_seen` ("Did the dot disappear?" yes / no / didn't try).

Instruction: *"How often have you experienced the following in the past 12 months? There are no right or wrong answers — many of these are common."*
Scale (fixed): 1 never · 2 once or twice · 3 several times · 4 about monthly · 5 weekly or more

| ID | Item |
|---|---|
| `pli01` | With my eyes closed, I see flickering, dots, or patterns of light or colour. |
| `pli02` | Rubbing or pressing on my closed eyes produces lights or patterns. |
| `pli03` | In ordinary daylight I see a fine, flickering "static", like an old TV screen, over everything I look at. |
| `pli04` | After looking at something bright, an afterimage stays in my view or gets in the way of what I am looking at. |
| `pli05` | I notice blurred, missing or "filled-in" patches in what I see that turn out not to match what is really there. |
| `pli06` | While falling asleep, I see images, faces or scenes that I did not intend to imagine. |
| `pli07` | While falling asleep or waking up, I hear sounds, voices or my name when nothing is there. |
| `pli08` | In silence I hear ringing, hissing or faint music that has no outside source. |
| `pli09` | When I stare at one point, parts of what I am looking at fade out or disappear. |
| `pli10` | Words, faces or objects seem to assemble themselves a moment late, as if I could watch them being put together. |
| `pli11` | A word or thought seems to arrive in my mind just before I have "thought" it. |
| `pli12` | When dozing off, my body suddenly jerks or I feel I am falling. |
| `pli13` | In dim light I see shapes or movement at the edge of my vision that turn out to be nothing. |
| `pli14` | A word I repeat or stare at loses its meaning and turns into mere sound or marks. |
| `chk_inf1` | I have seen a person who was five metres tall. *(infrequency item — valid answer: never)* |

**Flags (same page, after the grid, fixed order):** "Has a doctor ever diagnosed you with…" — `flag_aura` migraine with aura · `flag_vss` visual snow syndrome · `flag_tinn` tinnitus — each yes / no / prefer not. `flag_med` "Do you currently take medication that you know affects perception or sleep?" yes / no / prefer not.

## Page 3 — Filler (personality and attitudes)
Purpose: separate predictor and outcome blocks. Contents:
**BFI-10** (Rammstedt & John 2007, doi:10.1016/j.jrp.2006.02.001; free for non-commercial research per GESIS ZIS 76). Instruction: *"How well do the following statements describe your personality? I see myself as someone who …"* Scale (fixed): 1 disagree strongly · 2 disagree a little · 3 neither agree nor disagree · 4 agree a little · 5 agree strongly. ✅ S361: instruction, all 10 items, order, reverse keys (e01, a07, c03, n04, o05) and anchors verified verbatim against the GESIS ZIS 76 documentation (Rammstedt et al. 2014, doi:10.6102/zis76; `sources/bfi10-gesis-zis553.pdf`); free for non-commercial research, cite the documentation. Openness (`bfi_o*`) is the covariate; the other items are filler and are stored unscored.

| ID | Item |
|---|---|
| `bfi_e01_r` | … is reserved |
| `bfi_a02` | … is generally trusting |
| `bfi_c03_r` | … tends to be lazy |
| `bfi_n04_r` | … is relaxed, handles stress well |
| `bfi_o05_r` | … has few artistic interests |
| `bfi_e06` | … is outgoing, sociable |
| `bfi_a07_r` | … tends to find fault with others |
| `bfi_c08` | … does a thorough job |
| `bfi_n09` | … gets nervous easily |
| `bfi_o10` | … has an active imagination |
| `chk_ir` | To show that you are reading, please select "disagree a little" for this line. *(instructed response; valid = 2; placed between items 6 and 7)* |

## Page 4 — Views about the mind
Instruction: *"How much do you agree with each statement?"* Scale (fixed): 1 strongly disagree … 7 strongly agree.

**Hidden Depth (HD, new):**
| ID | Item |
|---|---|
| `hd1` | When I pay close attention to my own mind, I sense that far more is going on than I can ever reach. |
| `hd2` | I have the impression that most of what makes up my mind is hidden from me, yet not entirely out of sight. |
| `hd3` | My experience seems to rest on something vast that operates just beyond the edge of what I can notice. |
| `hd4` | My mind has depths that introspection can hint at but never reach. |
| `hd5_r` | When I look inward, what I find is all there is to my mind. *(reverse)* |
| `hd6` | There is much more to my own mind than I will ever be able to know from the inside. |

**Explanatory Gap (EG, new; Díaz 2021 items NOT used — they sit inside a deceptive vignette):**
| ID | Item |
|---|---|
| `eg1` | Even a complete scientific account of the brain would leave out what it is like to experience something. |
| `eg2_r` | Science will one day fully explain how conscious experience arises from the brain. *(reverse)* |
| `eg3` | What it is like to see red cannot, even in principle, be captured by physical facts. |
| `eg4_r` | Knowing every physical fact about a person's brain would tell you exactly what they are experiencing. *(reverse)* |
| `eg5_r` | Science could one day fully explain the following phenomenon: perceiving colour. *(reverse; stem from Gottlieb & Lombrozo 2018, doi:10.1177/0956797617722609)* |
| `eg6_r` | Science could one day fully explain the following phenomenon: feeling pain. *(reverse; same stem)* |

**Dualism — Riekki, Lindeman & Lipsanen (2013), full 12-item reflective-dualism factor, verbatim (doi:10.5709/acp-0138-5, Appendix A).** Riekki-original items are CC BY; the six items marked ᵃ come from Stanovich's Dualism Scale (1989) and are used with his written permission (email 2026-10-25, Gmail thread `1a16da64d957be6f`; MG S361-5). Original 5-point anchors: 1 strongly disagree … 5 strongly agree. Full factor as published, so scores compare with Riekki's norms; still report α in the sample. Item 6 keeps the source's missing punctuation.

| ID | Item |
|---|---|
| `dua_01` | Minds are in principle independent of bodies, to which they are only temporarily attached.ᵃ |
| `dua_02` | The mind is a special form of energy, currently unknown to man, that is in contact with the brain and affects it.ᵃ |
| `dua_03` | Thought processes cannot be just brain processes.ᵃ |
| `dua_04` | The mind is immaterial and it works with the brain to generate our behavior. |
| `dua_05` | The consciousness of myself does not die with my physical body. |
| `dua_06` | The body belongs to the world of material and natural laws. The mind is a different kind of existence a spiritual way of being. |
| `dua_07` | The body is material and the mind is immaterial. |
| `dua_08` | Some mental processes have no connection to brain processes.ᵃ |
| `dua_09` | The mind is not part of the brain, but it affects the brain.ᵃ |
| `dua_10_r` | Mental states are activities of my nervous system. *(reverse)* |
| `dua_11_r` | The mind as a whole is made up of substance and material processes. *(reverse)* |
| `dua_12` | The mind and the brain are totally different things.ᵃ |

**Mind–brain positions — Navarro-Peña et al. (2026), PNAS, verbatim, CC BY 4.0 (doi:10.1073/pnas.2610776123).** Original 0–4 scale: 0 totally disagree · 1 partially disagree · 2 neither agree nor disagree · 3 partially agree · 4 totally agree. One item per position (not a scale); allows comparison with their 2,657 neuroscientists. `np_dual` is a secondary single-item dualism measure.

| ID | Item |
|---|---|
| `np_red` | All mental activity (thoughts, feelings, etc.) of the human being is reducible to the functioning of the brain |
| `np_dual` | The human being is composed of two realities, one physical (the body) and one mental, which somehow interact |
| `np_nrp` | The human being is a unitary reality, but mental activity is not entirely reducible to the functioning of the nervous system |
| `np_dam` | The human being is a unity with two dimensions, one mental and one biological, which are distinct but inseparable |
| `np_fun` | The human being is a set of functions that could be implemented in different physical substrates |

Stanovich (1989) granted permission by email on 2026-10-25 (Gmail thread `1a16da64d957be6f`). MG S361-5: use the Stanovich-derived items within Riekki's full reflective-dualism factor (above), not the 27-item original. ⚠ Stanovich's permission does not settle the publisher's rights (T&F, *J Psychol* 1989); the items are short and are reprinted in CC BY Riekki 2013, and the permission is on file. **Open: the six new items still have to be added to the LimeSurvey .lss files (both arms).**

and **paranormal belief** (Tobacyk 2004 R-PBS, 26 items verbatim below, CC BY-NC-ND — no shortening, no translation without permission; `par_*`) — interleaved in the same grid. **Religiosity:** `rel1` "How religious or spiritual are you?" 1 not at all – 7 very; `rel2` "How often do you attend religious services or practise religious rituals?" never … weekly (6-point).


**Paranormal belief — Tobacyk (2004) R-PBS, Table 2, verbatim (CC BY-NC-ND 4.0, doi:10.24972/ijts.2004.23.1.94; source PDF `sources/tobacyk-2004-rpbs.pdf`).** Original 7-point anchors: 1 Strongly Disagree · 2 Moderately Disagree · 3 Slightly Disagree · 4 Uncertain · 5 Slightly Agree · 6 Moderately Agree · 7 Strongly Agree — **use these anchors for the R-PBS items** (unchanged instrument). Item 23 reverse-scored. Subscales: Traditional Religious Belief 1, 8, 15, 22; Psi 2, 9, 16, 23; Witchcraft 3, 10, 17, 24; Superstition 4, 11, 18; Spiritualism 5, 12, 19, 25; Extraordinary Life Forms 6, 13, 20; Precognition 7, 14, 21, 26. Item 15 is printed without a full stop in the original; keep it so.

| ID | Item |
|---|---|
| `par_01` | The soul continues to exist though the body may die. |
| `par_02` | Some individuals are able to levitate (lift) objects through mental forces. |
| `par_03` | Black magic really exists. |
| `par_04` | Black cats can bring bad luck. |
| `par_05` | Your mind or soul can leave your body and travel (astral projection). |
| `par_06` | The abominable snowman of Tibet exists. |
| `par_07` | Astrology is a way to accurately predict the future. |
| `par_08` | There is a devil. |
| `par_09` | Psychokinesis, the movement of objects through psychic powers, does exist. |
| `par_10` | Witches do exist. |
| `par_11` | If you break a mirror, you will have bad luck. |
| `par_12` | During altered states, such as sleep or trances, the spirit can leave the body. |
| `par_13` | The Loch Ness monster of Scotland exists. |
| `par_14` | The horoscope accurately tells a person’s future. |
| `par_15` | I believe in God |
| `par_16` | A person’s thoughts can influence the movement of a physical object. |
| `par_17` | Through the use of formulas and incantations, it is possible to cast spells on persons. |
| `par_18` | The number “13” is unlucky. |
| `par_19` | Reincarnation does occur. |
| `par_20` | There is life on other planets. |
| `par_21` | Some psychics can accurately predict the future. |
| `par_22` | There is a heaven and a hell. |
| `par_23_r` | Mind reading is not possible. *(reverse)* |
| `par_24` | There are actual cases of witchcraft. |
| `par_25` | It is possible to communicate with the dead. |
| `par_26` | Some people have an unexplained ability to predict the future. |

Item order within page 4: each instrument keeps its own published response scale, so page 4 is four randomised grids in randomised order — (HD + EG, 1–7), Riekki dualism (1–5), Navarro-Peña positions (0–4), R-PBS (1–7) — with no scale names shown.

`chk_inf2` (embedded): *"I have never in my life used a telephone of any kind."* *(infrequency — valid: disagree 1–3)*

## Page 5 — More about your experiences (covariates)
- **O-LIFE short, Unusual Experiences** (Mason, Linney & Claridge 2005, doi:10.1016/j.schres.2005.06.020), yes = 1 / no = 0. ⚠ Text from PsyToolkit (secondary source). S361 check: the 2005 paper is not open access (Unpaywall, no repository copy) and no verbatim reprint was found; 12 items, yes = 1, no reverse items. **`une_11` VERIFIED 2026-10-27 by Oliver Mason (author, Gmail `1a177a6c65e7f6a7`): published wording is "a sense of vague danger or sudden dread"; our wording was right. ⚠ Correction S362: the S361 claim that PsyToolkit reads "vague dread" was false — psytoolkit.org/survey-library/schizotypy-short-olife.html has the correct text (checked 2026-10-27), and a web search for the "vague dread" phrasing finds no questionnaire source; the variant was our own S361 transcription slip.** Licence: no open licence; **permission granted by Mason 2026-10-26** ("Absolutely fine"), with citation.

| ID | Item |
|---|---|
| `une_01` | When in the dark do you often see shapes and forms even though there is nothing there? |
| `une_02` | Are your thoughts sometimes so strong that you can almost hear them? |
| `une_03` | Have you ever thought that you had special, almost magical powers? |
| `une_04` | Have you sometimes sensed an evil presence around you, even though you could not see it? |
| `une_05` | Do you think that you could learn to read other's minds if you wanted to? |
| `une_06` | When you look in the mirror does your face sometimes seem quite different from usual? |
| `une_07` | Do ideas and insights sometimes come to you so fast that you cannot express them all? |
| `une_08` | Can some people make you aware of them just by thinking about you? |
| `une_09` | Does a passing thought ever seem so real it frightens you? |
| `une_10` | Do you feel that your accidents are caused by mysterious forces? |
| `une_11` | Do you ever have a sense of vague danger or sudden dread for reasons that you do not understand? |
| `une_12` | Does your sense of smell sometimes become unusually strong? |

Note: `une_01` overlaps PLI item `pli13` (shapes in the dark). That is intended: UnEx is the generic anomalous-experience covariate the PLI must outpredict.
- **DES-B** (Dalenberg & Carlson 2010, modified for DSM-5; public domain, attribution required: *"DES-B (Dalenberg C, Carlson E, 2010) modified for DSM-5 by C. Dalenberg and E. Carlson"*). **Adapted for trait use** and reported as such: the time frame is "the past 12 months" instead of "the past seven days", and the response scale is the PLI frequency scale (1 never … 5 weekly or more) instead of the original 0–4 within-week scale. Instruction: *"How often have you had the following experiences in the past 12 months, when you were not under the influence of alcohol or drugs?"*

| ID | Item |
|---|---|
| `dis_1` | I find myself staring into space and thinking of nothing. |
| `dis_2` | People, objects, or the world around me seem strange or unreal. |
| `dis_3` | I find that I did things that I do not remember doing. |
| `dis_4` | When I am alone, I talk out loud to myself. |
| `dis_5` | I feel as though I were looking at the world through a fog so that people and things seem far away or unclear. |
| `dis_6` | I am able to ignore pain. |
| `dis_7` | I act so differently from one situation to another that it is almost as if I were two different people. |
| `dis_8` | I can do things very easily that would usually be hard for me. |
- Death anxiety — **DAP-R Fear of Death subscale, 7 items** (Wong, Reker & Gesser 1994, in Neimeyer (ed.), *Death Anxiety Handbook*, Taylor & Francis, pp. 121–148; author statement: free for research use), DAP-R items 1, 2, 7, 18, 20, 21, 32 verbatim, 1 Strongly Disagree … 7 Strongly Agree (DAP-R anchors: Disagree, Moderately Disagree, Undecided, Moderately Agree, Agree), score = mean: `das_1` "Death is no doubt a grim experience." · `das_2` "The prospect of my own death arouses anxiety in me." · `das_3` "I am disturbed by the finality of death." · `das_4` "I have an intense fear of death." · `das_5` "The subject of life after death troubles me greatly." · `das_6` "The fact that death will mean the end of everything as I know it frightens me." · `das_7` "The uncertainty of not knowing what happens after death worries me." *Deviations:* the original randomises anchor polarity per item; here all grids run disagree → agree, as elsewhere in the survey. *German arm (if run):* DAP-GR, Jansen et al. 2019, *BMC Psychology* 7:61, doi:10.1186/s40359-019-0336-6, CC BY 4.0, Table 3, same item order: Der Tod ist zweifellos eine grauenvolle Erfahrung. · Die Aussicht auf meinen eigenen Tod verursacht mir Angst. · Die Endgültigkeit des Todes verstört mich. · Ich habe große Angst vor dem Tod. · Das Thema Leben nach dem Tod beunruhigt mich sehr. · Die Tatsache, dass der Tod das Ende von allem, wie ich es kenne, bedeuten wird macht mir Angst. · Die Ungewissheit, über das was nach dem Tod passiert, beunruhigt mich. *Caution for H3:* `das_5` and `das_7` carry afterlife content, which overlaps with the dualism measure; report H3 also without them. Replaces DABBS 1–4 (D-S363-10; DABBS is ND-licensed, so no German arm) and Templer DAS (T&F fees only).
- Absorption: **dropped** (Tellegen scale may not be shown online; MODTAS licence unclear). UnEx + DES-B cover anomalous-experience proneness.
- Support note at top: *"Some questions concern unusual experiences or thoughts about death. You can skip any question. If anything here troubles you, the contact at the end of the survey can point you to support."*

## Page 6 — Your impression (funnel debrief, fixed order, free text, optional)
- `deb1` "What do you think this survey was about?"
- `deb2` "Did you have a hypothesis about what the researchers expect? If so, what?"
- `deb3` "Did you notice any connection between different parts of the survey? If so, which?"
- `deb4` "Anything else you'd like to tell us?"

## Page 7 — Part two
*"Thank you — your answers have been saved.*

*We are planning a second, separate part: a session of about 45 minutes (online or on site) with a short perception task and a brief eyes-closed relaxation exercise.*

**May we contact you to invite you to part two?** *Your answers above stay anonymous. If you say yes, a separate form opens that asks only for your email address. That form is stored apart from this survey and cannot be connected to your answers. Saying yes commits you to nothing; you can decline the invitation later."*

- `p2_optin` — **Yes, show me the contact form** → opens separate survey `contact-p2` in a new tab (email field + "I agree to be contacted once about part two; my email will be deleted when recruitment ends, at the latest after 12 months.") · **No, thank you.**

## Page 8 — End
Thanks. No explanation of the hypothesis until data collection closes; the full explanation will be posted on the Institute site afterwards. Request: *"Many of your colleagues may still take part. Please don't discuss the questions with them until the survey has closed (date) — it would distort the results."* Then support contact, PI contact and the ethics committee reference number.

---
**Estimated time:** consent 2 · about you 2 · demo 1 · PLI 4 · filler 2 · beliefs 6 · covariates 7 · debrief 2 · part two 1 → ~27 min. Verify in the pilot.
