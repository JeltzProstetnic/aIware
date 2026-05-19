# Citation Review — sb-hc4a.md

**Date**: 2026-05-19  
**File reviewed**: `/home/jeltz/aIware/paper/cosmology/sb-hc4a.md`  
**References section**: Lines 571–752 (89 entries total)

---

## Summary

- **Missing references** (cited in text, no entry): **0**
- **Uncited references** (entry exists, never cited): **0**
- **Alphabetical order violations**: **14**
- **Disambiguation required**: **2 papers**
- **Citation format issues**: **3 minor**

All 21+ new citations requested for verification are present in both text and references. See Section 5.

---

## Category 1 — Missing References

**None found.** Every in-text citation has a corresponding entry in the References section.

---

## Category 2 — Uncited References

**None found.** Every reference entry is cited at least once in the body text.

---

## Category 3 — Alphabetical Order Violations

The reference list has 14 ordering errors. APA requires strict alphabetical order by first author surname, then by year for the same author.

| Issue | Current position | Problem | Fix |
|-------|-----------------|---------|-----|
| **~L582** | Bak (1996) before Bak (1987) | Same author: earlier year must come first | Swap: Bak 1987 before Bak 1996 |
| **~L588** | Bisio et al. (2015) placed before Bekenstein (1973), Bekenstein (1981), Berut et al. (2012) | Bi > Be; all three Be-entries should precede Bisio | Move Bekenstein 1973, Bekenstein 1981, Berut 2012 to before Bisio 2015 |
| **~L594** | Berut et al. (2012) placed after Bekenstein but still after Bisio | Berut (Be-r) < Bisio (Bi-s) | Berut must precede Bisio |
| **~L600** | Bousso (2002) placed after Burinskii (1998, 2008) | Bousso (Bou) < Burinskii (Bur) | Bousso must precede Burinskii |
| **~L606** | Boyle & Turok (2022) after Boyle, Finn, & Turok (2022) | For same first author, second author determines order: Finn (F) < Turok (T) | Boyle, Finn (2022) must precede Boyle & Turok (2022) |
| **~L612** | Caldwell (2002) after Carter (1968) | Caldwell (Cal) < Carter (Car) | Caldwell must precede Carter |
| **~L620** | Chalmers (2018) after Cook (2004) | Chalmers (Ch) < Cook (Co) | Chalmers must precede Cook |
| **~L632** | Einstein (1905) after Elze (2024) | Einstein (Ein) < Elze (Elz) | Einstein must precede Elze |
| **~L654** | Hawking (1975) after Jow (2022) | H < J | Hawking must precede Jow |
| **~L690** | Penington (2020) after Penrose (1971) | Penington (Peni) < Penrose (Penr) | Penington must precede Penrose 1971 |
| **~L696** | Perlmutter (1999) after Poplawski (2010) | Perlmutter (Perl) < Poplawski (Popl) | Perlmutter must precede Poplawski |
| **~L728** | 't Hooft (1993, 2016) after Tegmark (2008) | 't Hooft is conventionally sorted as "Hooft" (H) or "t Hooft" (T). Currently placed after Tegmark, which is inconsistent either way: if H, should be near ~L654; if T, should appear between Tegmark and Van Raamsdonk | Choose convention and apply consistently. Recommended: sort as H (Hooft), place after Hawking |
| **~L736** | Van Raamsdonk (2010) after Wheeler (1990) | V < W | Van Raamsdonk must precede Wetterich, Wheeler, Wolfram, Zuse |
| **~L750** | Wolfram (2021) after Wolfram, Gorard, & Peaslee (2020) | Same first author: 2020 must precede 2021 | Swap: Wolfram, Gorard & Peaslee (2020) before Wolfram (2021) |

**Correct B-section order** (as a reference for fixing): Albert, Algom, Almheiri, Arcos, Bak 1987, Bak 1996, Beggs, Bekenstein 1973, Bekenstein 1981, Berut, Bisio, Bousso, Boyle (Finn, 2022), Boyle & Turok (2018), Boyle & Turok (2022), Brown, Burinskii 1998, Burinskii 2008.

---

## Category 4 — Year/Author Mismatches

**None found.** Years in all in-text citations match years in the corresponding reference entries.

---

## Category 5 — Disambiguation Issues

### 5.1 Boyle & Turok 2022 — two papers, no a/b labels (Major)

There are **two distinct 2022 papers** by overlapping Boyle & Turok authors, both listed in references without a/b disambiguation:

- **L604**: Boyle, L., Finn, K., & Turok, N. (2022). *The Big Bang, CPT, and neutrino dark matter.* Annals of Physics, 438, 168767.
- **L606**: Boyle, L., & Turok, N. (2022). *Thermodynamic solution of the homogeneity, isotropy and flatness puzzles.* Physics Letters B, 849, 138442.

In the text these are cited differently (three-author vs. two-author forms) so they are not technically ambiguous, but the reference list violates APA disambiguation rules. APA requires suffix letters when the same (first) author has multiple works in the same year.

**Fix**: Assign labels based on alphabetical order of second author name (Finn < Turok):
- Boyle, L., Finn, K., & Turok, N. (2022**a**). The Big Bang...
- Boyle, L., & Turok, N. (2022**b**). Thermodynamic solution...

Then update in-text citations: L604 citations (L232, L462, L524) → `(Boyle, Finn, & Turok, 2022a)`; L524's `(Boyle & Turok, 2018, 2022)` → `(Boyle & Turok, 2018, 2022b)`.

### 5.2 Abstract reference — Boyle & Turok 2022 (minor)

In the abstract (L15), the text mentions "Boyle and Turok's CPT-symmetric universe" but does not provide a parenthetical citation. The body text cites it at L232 and L524, so this is not an error — abstracts commonly omit citations — but worth noting for journals that require abstract citations.

---

## Category 6 — Gödel Citations Without Year

The Gödel (1931) reference entry exists and is correct. However, the year is missing from two in-text uses:

| Line | Text | Issue |
|------|------|-------|
| **L327** | `(Gödel, 1931)` | CORRECT — has year |
| **L347** | `(Gödel)` in table cell | Missing year |
| **L362** | `(Gödel)` in body text | Missing year |
| L278 | "Gödelian" (adjective) | No citation needed — adjective use is fine |
| L440 | "Gödelian reason" (adjective) | No citation needed — adjective use is fine |

**Fix**: Change L347 and L362 from `(Gödel)` to `(Gödel, 1931)`.

---

## Category 7 — Gruber Same-Surname Disambiguation

APA style requires initials in in-text citations when multiple works by different authors share the same surname. The reference list includes both Gruber, B. J. and Gruber, M.

| Line | Current citation | Issue | Fix |
|------|-----------------|-------|-----|
| **L43** | `(Gruber, 1968, 1980)` | Ambiguous: could be B. J. or M. Gruber | `(Gruber, B. J., 1968, 1980)` |

The M. Gruber citations throughout the paper (`Gruber, 2015`, `Gruber, 2026a`, `Gruber, 2026b`) should similarly be `(Gruber, M., 2015)` etc., though in context they are self-citations and the ambiguity is low. For strict APA compliance, all Gruber citations should use initials.

---

## Category 8 — Citation Format Consistency

### 8.1 Bak (1987) — first vs. subsequent citation style

| Line | Format | Assessment |
|------|--------|------------|
| L122 | `(Bak, Tang, & Wiesenfeld, 1987)` | Full 3-author — correct first citation |
| L354 | `(Bak et al., 1987)` | Abbreviated — acceptable for subsequent citations |
| L418 | `(Bak et al., 1987)` | Acceptable |
| L516 | `(Bak et al., 1987)` | Acceptable |

No fix required. The first occurrence (L122) correctly spells out all three authors; subsequent uses of `et al.` are APA-compliant.

### 8.2 "and" in citation context (L116)

```
(supported by empirical criticality research: Beggs & Plenz, 2003; Shew & Plenz, 2013; 
Algom & Shriki, 2026; and theoretical work on self-referential computation: Gruber, 2015, 2026a)
```

The word "and" here is a prose connector between two citation groups inside a single parenthetical, not an author conjunction. This is non-standard. Fix: restructure as two separate parentheticals, or use "see also":

> (Beggs & Plenz, 2003; Shew & Plenz, 2013; Algom & Shriki, 2026; cf. Gruber, 2015, 2026a for theoretical framework)

---

## Section 5 — New Citations Verification

All 21+ new citations listed in the review request are confirmed present in both text and references:

| Citation | In text at line(s) | Reference entry |
|----------|-------------------|-----------------|
| Maldacena & Susskind (2013) | L188 | L682 ✓ |
| Brown et al. (2016) | L188 | L608 ✓ |
| Carter (1968) | L270 | L610 ✓ |
| Burinskii (1998) | L272 | L596 ✓ |
| Burinskii (2008) | L272 | L598 ✓ |
| Arcos & Pereira (2004) | L272 | L580 ✓ |
| Rovelli & Smolin (1995) | L274 | L710 ✓ |
| Israel (1967) | L270 | L660 ✓ |
| Israel (1968) | L270 | L662 ✓ |
| Smolin (1992) | L276 | L718 ✓ |
| Poplawski (2010) | L276, L282 | L694 ✓ |
| Penrose (1971) | L274 | L688 ✓ |
| Easson & Brandenberger (1999) | L276 | L624 ✓ |
| Van Raamsdonk (2010) | L323, L522 | L736 ✓ |
| Deutsch & Marletto (2015) | L329 | L622 ✓ |
| Elze (2020) | L266 | L628 ✓ |
| Elze (2024) | L266 | L630 ✓ |
| Tegmark (2008) | L126 | L726 ✓ |
| Vopson (2025) | L412 | L738 ✓ |
| Jow, Scott, & Sievers (2022) | L462 | L652 ✓ |
| Ruggiero (2020) | L218 | L714 ✓ |
| Boyle, Finn, & Turok (2022) | L232, L462, L524 | L604 ✓ |
| Wolfram, Gorard, & Peaslee (2020) | L530 | L748 ✓ |

**All 23 new citations verified present and correctly matched.**

---

## Priority Fix List

**High priority** (may cause editorial rejection or reader confusion):

1. **Boyle & Turok 2022 disambiguation** — two 2022 papers without a/b labels. Add 2022a/2022b to both reference entries and update in-text citations.
2. **14 alphabetical order violations** — reference list reordering needed.

**Medium priority** (APA compliance):

3. **Gödel missing year** — add `1931` to `(Gödel)` at L347 and L362.
4. **Gruber disambiguation** — add initials `B. J.` to Gruber 1968/1980 in-text citation at L43.

**Low priority** (style preference):

5. **L116 "and" connector** — restructure the mixed prose-citation sentence.
