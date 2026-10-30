# Japanese interior — Fable native-editor review (S259, 2026-07-13)

Full JA manuscript reviewed by 9 Fable agents against the aligned EN source.
Severity: **High** = fix before publish · **Med** = should fix · **Low** = polish.
Source review files: tmp/interior-review/ja-*.md. Fixes not yet applied — MG triage.

---

# ja-01 — Japanese editor review: teaser「そこにない点」+「著者について」+ 第1〜2章 (JA lines 48–249 vs EN 48–249)

| line | severity | issue | suggested fix |
|------|----------|-------|----------------|
| 62 | Med | 「開いた、正常に機能している目がまっすぐそこに向いているというのに、である。目はまっすぐそこに向いている。」— 「目がまっすぐそこに向いている」を二文連続でほぼ逐語反復しており、くどい。EN は前半が位置説明 "in front of your open, functioning eye"、後半が別文 "Your eye is aimed right at it." | 前半を位置句に戻す：例「太い黒の点が印刷されているまさにその位置で、開いた、正常に機能している目のまん前で、ページはただ継ぎ目なく白い。目はまっすぐそこに向いている。それなのに見えない。」— 反復を一回に。 |
| 166 / 190 / 206 | Med | "synaptic weights" の訳語が不統一。166・190＝「シナプス荷重」、206＝「シナプスの重み」。同一原語なのに揺れている（さらに 荷重＝load の含みがあり、NN 文脈では 重み が標準）。※176「シナプス結合の強度」は EN "strengths of synaptic connections" の訳で別物、これは可。 | 三箇所を一語に統一。ML 隣接の文脈なら「シナプスの重み」に統一するのが自然。荷重を採るなら 206 も「シナプス荷重」に合わせる。 |
| 226 / 236 | Med | 層の序数表記が章内で不統一。226＝「第一層／第二層／第三層」（漢数字）、236＝「第4層／第5層」（算用数字）。層の"数"(三層・六層)は漢数字で統一されているのに序数だけ混在。 | 236 を「第四層／第五層」に直し、漢数字に統一。 |
| 238 | Low | 「アーキテクチャ上の能力は、現象学と歩調を合わせている。」EN "tracks the phenomenology" は直前に列挙した自己意識の"現れ・徴候"（鏡像認知・計画・悲嘆）を指すが、「現象学」はフッサール的な学問分野と読まれやすく、語と主語(アーキテクチャ上の能力)の噛み合わせも弱い。 | 「現象面／現れ方」もしくは「現象学的な特徴」に。例「アーキテクチャ上の能力は、その現象面と歩調を合わせている。」 |
| 206 | Low | 「比較的に固い（学習によってゆっくり変わっていく）」— 構造的な rigid には 硬い が適切（固い＝堅固・きつい寄り）。また「比較的に」は「比較的」の方が自然。 | 「比較的硬い（学習によってゆっくり変わっていく）」。 |

Notes: 常体（だ・である）は全域で一貫、敬体の混入なし。数値・固有名は全て EN と一致（九つ／1.5キロ／25歳／2015／300ページ／120人／2023／2025／30年／15センチ／三層・六層／4000万／八本）。FMT 用語は一貫（四つのモデル／四モデル理論・自己モデル・世界モデル・ハード・プロブレム、glossは終始「難しい問題」）。カタカナ用語（デジタルツイン、ニューラルネットワーク、コネクトーム、パラログ 等）は定訳で過剰な translationese なし。カオスの縁・臨界は本セクション対象外。

---

# ja-02 — 第3〜4章 (Ch3 The Virtual Side / Ch4 Why It Feels Like Something) — native-JA editor review

Overall: high-quality literary translation. 常体（だ・である）consistent throughout; no です／ます leaks. FMT terminology (世界モデル／自己モデル／明示的・暗黙的／臨界性／カオスの縁／自己言及的閉包／クオリア) consistent and correct. Abbreviations (EWM/ESM/ISM) introduced properly. Typography (「」、。——、H₂O、2×2) clean. Only minor issues below.

| line | severity (High/Med/Low) | issue | suggested fix |
|------|-------------------------|-------|---------------|
| 378 | Med | Dropped internal cross-reference. EN: "Recall the digital twin **from Chapter 2**." JA: 「デジタルツイン（ジェットエンジンの工学シミュレーション）を考えてみよう。」 — the 第2章 back-reference (the "you've seen this before" signal) is deleted and replaced by an inline gloss. Gloss content is faithful (Ch2 line 178 lists a jet engine as an example), but the callback is lost. | 「第2章で見たデジタルツイン（ジェットエンジンの工学シミュレーション）を思い出してほしい。」 |
| 272 | Low | First in-section gloss 「ハード・プロブレム（難しい問題）」: 難しい問題 is a loose descriptive phrase; the idiomatic noun 難問 reads better and matches the project's canonical term. | 「意識のハード・プロブレム（難問）」 |
| 272, 328, 334, 340, 342, 366, 424, 438 | Low | "ハード・プロブレム" is set with a nakaguro (・). Internally consistent within this section, but the terminology spec lists ハードプロブレム／難問 — confirm this matches the rest of the book so the form doesn't drift between chapters. | Harmonize to whichever form the other sections use (e.g. ハードプロブレム). |
| 336 vs 396 | Low | Inconsistent の-insertion in the same parallel "virtual self perceives the virtual world" formula: 336「仮想の自己が仮想の世界を…」 vs 396「仮想自己が仮想世界を…」. | Pick one form for the paired phrase (e.g. 仮想自己／仮想世界 or 仮想の自己／仮想の世界) and apply to both. |

---

# ja-03 — Ch5–6 (第5〜6章) native-JA editor review

Section is high-fidelity and complete: all EN paragraphs map 1:1, the Ch6 病態失認 (anosognosia) subsection is present and intact (JA 672–688), all numbers/dates/citations match EN, FMT terminology is consistent (カオスの縁, 自己モデル/世界モデル, 明示的/暗黙的, 臨界性, 普遍計算, 皮質オートマトン), and 常体（だ・である）is uniform throughout. Only minor issues below.

| line | severity | issue | suggested fix |
|---|---|---|---|
| 470 | Med | Doubled adjective: 「ゆるやかなゆるやかなデルタ波」 — 「ゆるやかな」is repeated (EN: "slow delta waves"). Reads as a duplication typo. | 「ゆるやかなデルタ波」 |
| 670 | Med | Mixed parenthesis width in one sentence: opens full-width（ but closes half-width ) twice — 「…にちがいない」)、…生成するEWM)、」 — while the third pair closes full-width（…ESM）. Orthographic inconsistency. | Use full-width closing ）for all three: 「…にちがいない」）、…生成するEWM）、…ESM） |
| 468 / 624 | Low | "global integration" rendered inconsistently: 468「グローバルな統合」vs 624「全体的統合」(same concept). | Standardize (e.g. 全体的統合 both places, or add グローバルな gloss once). |
| 628 / 632 | Low | Heading 「転向可能な自己」and body 「転向する」for "redirect(able)": 転向 strongly connotes ideological/political conversion (転向者=apostate), off-register for an ESM re-latching onto dominant input. | Consider 向きを変えられる自己／向け先を変える, or リダイレクト. |
| 650 / 670 | Low | "Cotard's delusion" → 「コタール症候群」(= syndrome). Consistent internally and コタール症候群 is the standard JP term, but EN deliberately says "delusion" (妄想). Slight term-broadening drift. | Optional: 「コタール妄想（症候群）」or keep, note EN uses 妄想. |

---

# ja-04 — 第7〜9章 (Ch7–9) native-JA editor review

| line | severity | issue | suggested fix |
|------|----------|-------|---------------|
| 704 | Med | Section heading 「夢——省エネモード」 renders "Dreams: Degraded Mode" as *energy-saving mode*. 省エネ implies efficiency/optimization — the opposite spin of "degraded/impaired," and it contradicts the section's own body, which uses 「劣化したシミュレーション」(708) and 「劣化モードで走る」(710). High-visibility heading, so treat with care (borderline High). | 「夢——劣化モード」 (match the body's 劣化 wording). |
| 802 | Med | "subcritical" rendered as 「臨界未満（サブクリティカル）」, but the term was established as 亜臨界 in the same span (698, 740, and table rows 758/759). A technical book should keep one term for a defined concept; two spellings for one thing can read as two different states. | Use 亜臨界 here too (drop the サブクリティカル gloss, or gloss 亜臨界 once at first use in 698). |
| 757–758 vs 698/706 | Low | Orthography inconsistency: the map table writes 「REM睡眠」「深いNREM」(roman), while the body writes 「レム睡眠」(706) and 「ノンレム睡眠」(698) (katakana). Same book, two conventions. | Unify — prefer katakana 「レム／ノンレム」 in the table to match running text (or roman in both). |
| 808 / 812 | Low | "Cotard's **delusion**" (heading + body) rendered 「コタール**症候群**」 (Cotard's *syndrome*). 症候群 is standard JA usage and reads well, but the author deliberately wrote "delusion" (妄想). Borderline/optional. | If fidelity to "delusion" matters, 「コタール妄想」; otherwise accept 症候群 as idiomatic localization. |
| 906 | Low | "into the nest, into the hive" → 「巣のなかへ、群れのなかへ」. "hive" (superorganism / bee colony, setting up Ch10's animal imagery) is softened to 群れ (swarm/herd), losing the collective-colony nuance that pairs with 巣 (nest). Defensible literary choice. | Consider 「巣のなかへ、コロニーのなかへ」 or 「蜂の巣のなかへ」 to preserve the nest/hive pairing. |

Notes: No mistranslations, omissions, factual/number errors, or 常体(だ・である) leaks found in the narration. All FMT terminology is consistent and correct — 四つのモデル/四モデル(理論), 自己モデル, 世界モデル, 明示的/暗黙的 (EWM/ESM/IWM/ISM), カオスの縁-family dynamics as クラス2/3/4, 臨界/臨界性/臨界近傍, ハードプロブレム-adjacent framing, 作話, 分岐（フォーク）/クローン化. Proper names, dates (2006, 1971, 2017, Reinders 2003, ages 7–12, 30 years, Prediction 9→予測9), and the consciousness-map table are all accurate. Katakana technical terms (アーキテクチャ, マルチエージェント, ホログラフィック) are appropriate; quoted patient/dialogue ます-forms are correct direct speech, not register breaks.

---

# ja-05 — 第10〜12章 (Ch10-12: The Animal Question / Nine Predictions / From Machines to Minds)

Fidelity is strong overall: JA and EN are line-aligned 1:1 with no dropped or added paragraphs, numbers are accurate (85,000 / 302 / 140,000 / 86 billion / 100 trillion / 90% / 7–10 yrs / 200 m / six hours), chapter and appendix cross-references all match (第1/2/5/6/8/9章, 付録B/H), FMT terminology is consistent (四つのモデル・四モデル理論, 自己モデル, 世界モデル, カオスの縁（ふち）, 臨界/臨界性, IWM/ISM/EWM/ESM), 常体（である調・〜のだ）is consistent throughout with no です・ます leaks, and idiom rendering is excellent (合わせ鏡 for "hall of mirrors", 蝋燭と水晶／錠前師の不気味さ, ヤドカリが新しい貝殻, その場しのぎ for "kludge"). Issues below are typography/consistency polish plus a few minor fidelity nuances.

| line | severity | issue | suggested fix |
|------|----------|-------|----------------|
| 960 | Med | Half-width parentheses used around a Japanese clause: 「覚えているだろうか(哺乳類は三層で足りる…というものだ)。」 — inconsistent with the full-width （） used everywhere else in the book (e.g. lines 924, 926, 1000). Visibly jarring in-line. | Change to full-width: 「覚えているだろうか（哺乳類は…というものだ）。」 |
| 1116 / 1118 / 1138 / 1176 | Med | Five-level hierarchy names are inconsistent (same referents, different renderings). "proteomic" = 「プロテオミクスのレベル」(1116) vs 「プロテオーム的（構造）」(1138) / 「プロテオーム的レベル」(1176); "topological" = 「トポロジカルなレベル」(1118) vs 「トポロジー的レベル」(1176); "virtual" = 「仮想のレベル」(1120) vs 「仮想レベル」(1162,1168). Also, 「プロテオミクスの」names the *discipline* (proteomics), not the level — a mild mistranslation of the adjective "proteomic". | Unify: 「プロテオーム的レベル」and 「トポロジー的レベル」(and one of 仮想レベル／仮想のレベル) throughout; drop 「プロテオミクスのレベル」. |
| 944 / 1008 | Low | Question-mark width inconsistent: line 944 「うちの犬に意識はあるの?」uses half-width `?`, but line 1008 「突然の大きな音は？涙だ。」uses full-width `？`. | Use full-width 「…あるの？」for consistency. |
| 912 / 1044 / 944 vs 1198 / 1126 | Low | Number orthography mixes kanji and Arabic for comparable quantities: 三十メートル (912), 四十分 (1044), 午前三時 (944) vs 200メートル (1198), 302個/14万/860億/100兆 (1126). 三十メートル vs 200メートル is a direct same-unit clash in parallel first-person anecdotes. | Pick one convention (Arabic for measured quantities is cleanest here) and at minimum align 三十メートル ↔ 200メートル. |
| 922 / 924 / 926 / 928 | Low | "Commitment 1/2/3" (a stance the theory is committed to) is rendered 「前提1/2/3」(premise). Function is preserved (predictions are derived from them), but 前提 = premise/assumption, not commitment. | Consider 「基本前提」or 「コミットメント」for the labels; leave body wording as is if 前提 is kept. |
| 928 | Low | "Simpler nervous systems (insects, worms)" → 「昆虫や線虫」narrows generic "worms" to nematodes specifically. Defensible given the later C. elegans (線虫) reference, but the EN here is generic. | Optional: 「昆虫やミミズなど」or keep 線虫 if the nematode reading is intended. |

---

# ja-06 — 第13〜15章（JA 1224–1519 vs EN Ch13–15）native-JA editor review

| line | severity (High/Med/Low) | issue | suggested fix |
|------|-------------------------|-------|---------------|
| 1250 | Med | 「クーン（Kühn）」— Simone Kühn の慣用カタカナは「キューン」。「クーン」は本書98行目のトマス・クーン（Thomas Kuhn）と同一表記になり、別人と混同される。 | 「キューン（Kühn）」に変更 |
| 1252 | Med | 「サリア・ウェットリー（Thalia Wheatley）」— 人名転写誤り。Thalia は「タリア／ターリア」（Th は t 音）、Wheatley は「ウィートリー」が定訳。 | 「タリア・ウィートリー（Thalia Wheatley）」 |
| 1336 | Med | 「目の前にあるものから切り離れ」——「切り離れる」は非標準の動詞形（標準は他動詞「切り離す」／受身「切り離される」）。 | 「目の前にあるものから切り離され」または「〜を切り離し」 |
| 1452 | Med | 脱落：EN「self-organized criticality — **which we first met in Chapter 5**」の第5章への参照が訳出されていない（読者への既出リマインダーが消失）。 | 「**自己組織化臨界性**——第5章で最初に出会ったあの仕組み——である。」等で参照を復元 |
| 1438–1466 | Med | 一人称複数の表記ゆれ：計算クラス節では「われわれ」（1438, 1442, 1444, 1446, 1448, 1450, 1466）、直後の地平線節では「私たち」（1466後半, 1470, 1496）。同一章内で交替しており、本書全体では「私たち」が優勢（65 vs 19）。 | 章内（できれば全巻）で「私たち」に統一 |
| 1230 | Low | 「襟を正させられる話」— EN "humbling"。「襟を正す」は「気を引き締める・敬意を抱く」であり「謙虚にさせられる」とは意味がずれる。 | 「謙虚にならざるをえない話」等 |
| 1232 / 1308 | Low | 「四モデル・アーキテクチャ」（1232）と「四モデルのアーキテクチャ」（1308）が混在（全巻でも12対11で拮抗）。 | どちらか一方に統一（推奨：「四モデル・アーキテクチャ」） |
| 1328 / 1336 | Low | EN は "superpower" を第13章末（1328）と第14章冒頭（1336）で意図的に反復するが、訳は「超能力」（1328）と「並外れた力」（1336）に割れて呼応が消えている。 | 両方「超能力」に揃えて反復を再現 |
| 1372 | Low | 見出し「私にわからないこと」— 係助詞が抜けてやや不自然。 | 「私にはわからないこと」 |
| 1480 | Low | 「眩暈」— 74行目・1416行目では同じモチーフを「めまい」と平仮名表記。同一章内の呼応語で漢字・かなが揺れている。 | 「めまい」に統一 |

数値・固有名詞（Hz、ミリ秒、光年、10^-35 m、60桁、1987/1998/2009年、パー・バック、トホーフト、サスキンド、ホッセンフェルダー等）はすべて EN と一致。常体（だ・である）は全域で維持。FMT用語（自己モデル／世界モデル／カオスの縁／臨界性）は既定訳に一致。省略・追加は1452の一件のみ。

---

# ja-07 — 第16〜17章（万物のアーキテクチャ／最も深い鏡）, JA lines 1520–1843 vs EN Ch16–17

| line | severity | issue | suggested fix |
|------|----------|-------|---------------|
| 1832 | High | **Title self-citation mismatch** (same bug class as FR edition). Text reads 本書の題名は『あなたが「私」と呼ぶシミュレーション』である — but the real title (line 1 of the manuscript) is 「私」という名のシミュレーション. | 本書の題名は『「私」という名のシミュレーション』である。 |
| 1580 (also 1582, 1584, 1624, 1730, 1778, 1784) | Med | Terminology flip mid-chapter: Ch16 opens with 事象の地平線 (1532, 1538, 1540), then switches to 事象の地平面 from 1580 onward. Book-wide split is 9× 地平線 vs 8× 地平面 — genuinely inconsistent. | Unify to 事象の地平線 (standard pop-sci term) throughout the book, or at minimum within Ch16–17. |
| 1582, 1624, 1730 | Med | 宇宙論的地平面 (1582, 1624) and bare 宇宙論的地平 (1730, twice) vs the book-dominant 宇宙論的地平線 (9×, incl. 1538, 1558 in this section). | Unify to 宇宙論的地平線. |
| 1630, 1736–1746, 1782–1808 | Med | EN "decompress(ed)" rendered four different ways within this section alone: 展開 (Ch16: 1546, 1548, 1550), 解凍 (1630), 伸張 (1736, 1740, 1742, 1746), 伸長 (1782, 1784, 1808). The 伸張→伸長 flip happens inside Ch17's own mapping argument, where the compressed/decompressed pair is the load-bearing concept. All 伸張/伸長/解凍 hits in the book are in this section. | Pick one term for the technical pair (圧縮／伸張 is standard data-compression Japanese) and use it consistently; 展開 acceptable as the Ch16 narrative verb, but 1736–1808 must be internally uniform. |
| 1620, 1748, 1796 | Med | "subprocess(es)" = 部分プロセス (1620) / 下位プロセス (1748) / 部分過程 (1796) — three variants for the same technical term, in deliberately parallel passages (1620 and 1748 restate the same claim). Book-wide also mixed (4/3/4). | Unify to 部分プロセス. |
| 1734 | Low | 暗黙的・明示的境界 — sole nakaguro variant; everywhere else (8×, incl. 1693, 1784) the term is 暗黙的-明示的境界. | 暗黙的-明示的境界 |
| 1712 | Low | Lost deliberate callback: EN repeats "sit down" (1680 "made me sit down" → 1712 "make you want to sit down"). JA has 座り込んでしまった (1680) but 立ち止まらされる (1712), breaking the echo. | e.g. そして、これを読んで思わず座り込みたくならないなら、まだ理解できていないのだ。 |
| 1610 | Low | Numeral style mix: 二つでも、四つでも、17でもなく — Arabic 17 amid kanji numerals. | 二つでも、四つでも、十七でもなく |
| 1774 | Low | ロルフ・ランダウア missing the long vowel — the same paragraph (and 1780) uses ランダウアー. | ロルフ・ランダウアー（Rolf Landauer） |
| 1830 | Low | Title-echo phrase あなたが「私」と呼ぶシミュレーション renders EN "the simulation you call 'I'" literally but no longer echoes the JA title wording (「私」という名の…), weakening the setup for the title reveal at 1832. The 「宇宙」と呼ぶ parallel constrains the phrasing, so this is optional. | Optional: 「私」という名のシミュレーションは、われわれが「宇宙」と呼ぶシミュレーションと、同じパターンの上で走っている。 (or leave as is once 1832 is fixed). |

Notes (not defects): ハード・プロブレム (1828) matches the book-wide convention (21×, zero ハードプロブレム); 四モデル理論／四モデル・アーキテクチャ (1690, 1724, 1802) match book convention (45×/12×). All numbers/facts check out (13.8 billion yr, 12 fermions, 4 bosons + Higgs, Bak/Chen/Creutz 1989, Gödel 1931 age 25, Landauer 1961/2012, three generations, five axioms/correspondences, Appendix F/G references). 常体 is consistent; prose register is natural and idiomatic throughout.

---

# ja-08 — Coda + Acknowledgments + Notes/References + 付録A (Neurology) + 付録B (Intelligence Model)

Fidelity vs EN is strong throughout: no omissions, no dropped paragraphs, all citations/author-years/journal numbers (Research in Human Development 7(1), 61–78; PeerJ 8:e9290; 204 people / 100 sessions; 14 nearly swallowed; Brodmann area 17; receptive-field degrees; 2011 Nobel; Nature 2025; 12 June 2026; github URL) intact and untouched. 常体（だ・である）is consistent — no です・ます leaks. Neurology glossary technical terms are accurate. Only issues below are terminology-consistency drifts.

| line | severity | issue | suggested fix |
|---|---|---|---|
| 1930 | Med | "Performance" in the canonical multiplicative formula rendered 遂行 — 「知識×遂行×動機づけ」 — but the Appendix B body defines and writes the component as 性能 everywhere (esp. the identical formula at line 2091: 「知識×性能×動機づけ」). A reader seeing both formulas will read two different middle terms. The Wittmann/COGITO glosses on the same line also use 遂行 for "performance" where the body (2087) uses 性能. | Change 遂行→性能 in the formula and in the two citation glosses on line 1930, matching the body. |
| 2077, 2083 | Med | "operational knowledge" rendered 運用的知識, but every definitional/core occurrence uses 操作的知識 (2005, 2025, 2027 header, 2029, 2031, 2033). Two competing terms for one concept risks reading as two different things. | Unify to 操作的知識 at 2077 and 2083. |
| 1846 | Low | "cosmology" rendered as katakana コスモロジー (「よりにもよってコスモロジーだった」), but the Notes section uses the kanji term 宇宙論 (e.g. 1924 宇宙論的地平線／宇宙論的論証). Katakana-English where an established kanji term exists and is used elsewhere. | Consider 宇宙論 for consistency (colloquial punch survives). |
| 1898, 1904 | Low | "hard problem" rendered ハード・プロブレム with nakaguro; project glossary term is ハードプロブレム／難問. Internally consistent within this section but verify against the rest of the book. | Drop the nakaguro → ハードプロブレム (or confirm book-wide convention). |
| 1858 | Low | proprioception rendered 固有感覚 in the Coda (「その動きが私の固有感覚と食い違っていた」), but 付録A defines Proprioception as 固有受容感覚 (1954). Cross-reference mismatch. | Align to 固有受容感覚, or note 固有感覚 as accepted shorthand. |
| 2013–2063 | Low | "(recursive) loop" alternates between 循環 (1991, 2013, 2019, 2025) and ループ (2055, 2063, 2069, 2087...). Stylistically tolerable but a careful editor would unify. | Pick one rendering for "loop" across Appendix B. |

---

# ja-09 — 付録C〜H (Appendix C–H): native-JA editor review vs EN

| line | severity | issue | suggested fix |
|---|---|---|---|
| 2357 | High | Omission vs EN. EN opens weak-point Four with an authorial-voice sentence: "This is the one that ties my stomach in knots." The JA drops it entirely — jumps from the bold heading 「…それ自身の予測によって。」straight to 「自己言及的閉包のゲーデル的帰結は…」. This line pairs rhetorically with 2349「答えられない唯一のもの」; losing it weakens the passage's voice. | Restore a rendering, e.g. 「これは、考えるたびに胃が締めつけられる一点だ。」directly after the heading. |
| 2355 | Med | Typography: mismatched parenthesis widths. 「特異点（プランクスケール、ブラックホール、宇宙論的なもの)が」— opening is full-width（but closing is half-width ). Every other JA-content paren in these appendices is full-width（）. | Change the closing ) to full-width ）. |
| 2445, 2447, 2455, 2457 (vs 2257, 2281) | Med | Orthography inconsistency for REM/non-REM. Appendix D writes it in Latin — 「REM睡眠」(2257)、「REMの豊富な睡眠後半」(2281). Appendix H writes it in katakana — 「レム睡眠」「ノンレム睡眠」「レムとノンレム」(2445, 2447, 2455, 2457). Same term, two orthographies within the reviewed span. | Standardize book-wide (e.g. レム睡眠／ノンレム睡眠 throughout, or REM/NREM throughout). |
| 2265, 2289 (vs 2331, 2373) | Low | Question-mark width inconsistent. Half-width ? at 「…夢を見ているのか?」(2265) and 「…まさかあるまい?」(2289); full-width ？ at 「なぜか？」(2331) and 「…人間だろうか？」(2373). | Standardize to full-width ？ (or whichever the book uses elsewhere). |
| 2222/2238 (App C) vs 2343/2355/2357/2473 (App F–H) | Low | Register consistency: first-person plural alternates. Appendix C uses われわれ (2222「われわれは現在」, 2238「われわれの宇宙」); Appendices F/G/H use 私たち (2343「私たちの観測」, 2355「私たちはそれをもっていない」, 2473「私たちの理解と治療」). Singular 私 is consistent; plural is not. | Pick one plural form book-wide. |
| 2421 | Low | Kanji choice. 「繊維の一部だけを切る」uses 繊維 (textile/general fiber) for corpus-callosum nerve fibers; anatomical Japanese standard is 線維 (cf. 神経線維). | Change 繊維 → 線維. |
| 2447 | Low | Flow: 「90分のウルトラディアンリズム（一晩を通じたレムとノンレムのリズム）」repeats リズム（…リズム）. EN is "cycle (the rhythm…)". | Use ウルトラディアン周期（…のリズム）to break the repetition. |

Notes (verified clean): all nine prediction headings and bodies match EN exactly; class names/numbers (Wolfram 1–4, five-class 1–5, Class 4.5, three generations, 十七/十七, 2002/2006/1990/2009/2019/2017/2026, 2–6週間, 5時間, 20–60分, 90分, PCI/LZ, V1/V2/V3/V4) all correct; FMT terms consistent (四つのモデル/四モデル理論, 自己モデル/世界モデル, IWM/ISM/EWM/ESM, カオスの縁, 臨界性/臨界状態, 神経的シグネチャ vs 神経的指紋 distinction preserved); 常体 (だ・である) uniform throughout, no です・ます leakage; clinical terms accurate (病態失認, 作話, 脳梁, 脳梁離断術, 解離性同一性障害, 交代人格, 内側前頭前皮質).

