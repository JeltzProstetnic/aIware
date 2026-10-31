<!-- AIW-343 hosting requirements — for the institute (owner of the study page) and infrastructure (deployment). aIware owns the instrument and analysis; questions about content go back to aIware. -->
# Hosting specification — Part 1 survey + Part 2 contact form (v0.1)

## Ownership
- **aIware:** questionnaire content (`questionnaire-part1.md`), consent text, analysis code, data analysis.
- **institute:** the study is hosted under the Institute's name — study landing page, privacy notice, results page after closing. **Data controller is MG personally** (decision S358). p1 answers are anonymous; the only personal data is the email in `contact-p2`, for which the Institute/host acts as processor → a short processing agreement (AVV) is needed.
- **infrastructure:** deployment and operation of the survey platform.

## Must-haves
1. **Two separate surveys / data stores:** `survey-p1` (answers) and `contact-p2` (email only). No shared respondent ID, no referrer/URL parameter carrying anything from p1 to p2, no timestamps precise enough to join them (store p2 submission date only, or round to the day).
2. **No identifying metadata in p1:** IP address not stored (LimeSurvey: "Save IP address" off; web-server access logs for the survey path disabled or IP-anonymised), no cookies beyond a session cookie, no analytics, no third-party scripts/fonts (self-host everything).
3. **EU hosting**, HTTPS, nightly encrypted backups, admin access 2FA.
4. **Randomisation:** per-participant block order A/B (store `block_order`); item order randomised within grids as marked; response option order fixed.
5. **Blind-spot demonstration:** a static image pair (cross + dot; line through the dot position) with instructions; no JS tracking needed. aIware supplies the SVG.
6. **Quality data:** total completion time and per-page times stored (seconds); no keystroke logging.
7. **Exports:** CSV with the item IDs from `questionnaire-part1.md` as column names, numeric codes, "prefer not" = empty. aIware's analysis script reads that format.
8. **Languages:** EN at launch; DE, IT, FR added later — build with the platform's multi-language support from the start and store `lang`.
9. **Accessibility:** works on phones; no time limits.
10. **Pilot instance** (n ≈ 10) before the live link; pilot data are kept apart and not analysed with the main data.
11. **Deletion:** `contact-p2` purged when Part 2 recruitment closes or after 12 months. p1 is anonymous — no per-person deletion possible or needed.
12. **Closing:** survey closes automatically at the end date; the landing page then shows the results-to-come notice.

## Status
**LIVE 2026-10-24 (infrastructure INF-168):** https://survey.alpine-institute.eu, LimeSurvey CE 6.17.18 at go-live, **7.5.1 since then** (container image `martialblog/limesurvey:7.5.1-261021-apache`, measured 2026-10-28); admin `/admin` behind institute Keycloak (group survey-admins) then LimeSurvey user `aiar-admin` (vault `survey_admin_password`). No client IP reaches LimeSurvey (measured). Survey-level settings (items 1, 4–12) are aIware's job when building p1/p2/pilot — mapping in `~/infrastructure/configs/vps/survey/README.md`. Cookies: PHPSESSID + Yii CSRF (both technical) → disclosed in the consent text.

## Suggested platform (infrastructure decides)
Self-hosted **LimeSurvey Community Edition** (GPL, mature, supports all of the above incl. randomisation groups and IP-off) on the existing EU VPS, under `survey.<institute domain>`. Alternatives: Formbricks (self-hosted), SoSci Survey (free for non-commercial academic use, hosted in Germany — no self-hosting needed, but the "academic" eligibility should be confirmed for an institute in founding).

## Not yet decided (blocks go-live, not setup)
Ethics approval (UMIT), instrument licences (dualism, death anxiety), employer clearance (MG, manual). Go-live only after aIware confirms all of these.
