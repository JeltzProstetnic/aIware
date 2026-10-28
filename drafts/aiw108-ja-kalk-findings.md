# AIW-108 — JA Kalk-scan findings (native-Japanese calque/naturalness sweep)

Session 254, 2026-07-10. Method: parallel **Opus 4.8** native-Japanese editors over `pop-sci/book-manuscript-ja.md` (36 general @70ln + 54 aggressive checklist-primed @46ln = 90 agents). **439 findings: A=320, B=103, C=2, D=14.**

Per MG policy: **A + B applied, D softened (reserved register), C kept.** **323 applied** via verified match-once (`tmp/kalk_apply.py`). Plus two systematic mechanical fixes: **96 stray `―` (U+2015) → `——` (U+2014)** em-dash normalization, and **3 dropped chapter separators** restored (Ch.9/10, App-A → JA now 45, matches EN). Half-width `(`→`（`-paren normalization DEFERRED to native reviewer (context-dependent: `（IWM）` gloss vs Latin `(2015)` citation cannot be auto-distinguished).

**Not applied (70):** 0 were overlap-duplicates (70ln & 46ln passes cover the same text; the twin fix already applied — spot-verified fixed). 69 genuine miss + 1 ambiguous listed below.

## D — grandeur softenings (reserved register) — APPLIED (14) — reviewer tone-check
- **[seg 6·grandeur]** «打てる最強の一手であり» → «打てる最も強い一手であり» — 最強 carries a popular/gaming-flavored superlative tone; JA nonfiction reserve prefers the sober 最も強い while keeping the full claim.
- **[seg 20·grandeur]** «加減した量で手を伸ばすなら、それは超能力といっていい» → «加減した量で手を伸ばすなら、それは並外れた力を発揮する» — 「超能力といっていい」は米国的な誇張（superpower）。日本の抑制的ノンフィクション調では控えめな断定に寄せ、意味は保つ。
- **[seg 25·grandeur]** «これを読んで思わず座り込みたくならないなら、まだ理解できていないのだ» → «これを読んで思わず立ち止まらされる思いがしないなら、まだ理解できていないのだ» — 「座り込みたくなる」はTEDトーク調のアプルーズ・ライン的身振り。日本語ノンフィクションの抑制に合わせ、意味を保ったまま落ち着いた表現に。
- **[seg 35·anglicism]** «それは病態失認に対する医学的ブレイクスルーであるだけではない» → «それは病態失認に対する医学上の突破口であるだけではない» — 「医学的ブレイクスルー」はUS的な宣伝調カタカナ。日本のノンフィクションはより抑制的に「突破口」で足りる。
- **[seg 35·grandeur]** «それがうまくいくなら、それこそが究極の裏づけとなる» → «それがうまくいくなら、それが何よりの裏づけとなる» — 「究極の」はTEDトーク的な誇張。抑制の効いた「何よりの」に寄せて驚きは残し宣伝色を落とす。
- **[seg 2·grandeur]** «いかなる対抗理論も及ばない予測を立て» → «他のどの理論も立てていない予測を立て» — 'no rival theory can match' is a superlative competitive sales-claim; understate to a sober factual statement (predictions no other theory has made) per the reserved grandeur policy.
- **[seg 6·grandeur]** «息をのむようなグラフィック、リアルな物理挙動、引き込まれるストーリーを備えた、没入感のあるオープンワールドゲームだ» → «美しいグラフィック、リアルな物理挙動、先を追いたくなるストーリーを備えた、没入感のあるオープンワールドゲームだ» — Ad-copy adjective stack ('breathtaking / immersive / gripping') reads like marketing; Japanese nonfiction resolves toward sober description while keeping the vividness — softens 息をのむよう and 引き込まれる to reserved equivalents.
- **[seg 9·grandeur]** «内部で打てる最強の一手であり» → «内部で打てる有力な一手であり» — 「最強の一手」はUS流の最上級ハイプ。日本の抑制されたノンフィクション文体では主張を残しつつ「有力な一手」と控えめに述べる方が説得的。
- **[seg 11·grandeur]** «電気的活動の壮大なパターン» → «電気的活動の広大なパターン» — grand を「壮大な」と訳すと装飾的で誇張的。日本語ノンフィクションの抑制された調子に合わせ、規模を述べる「広大な」へ落とす。
- **[seg 18·grandeur]** «神経科学全体でも最も驚嘆すべき実演の一つだ» → «神経科学のなかでもとりわけ驚くべき実演だ» — US-style superlative hype ('in all of neuroscience, one of the most astonishing'); Japanese nonfiction persuades through understatement — keep the wonder, drop the salesmanship.
- **[seg 22·grandeur]** «進化上の利点は計り知れない。» → «進化上の利点は大きい。» — 計り知れない is a superlative applause-line; Japanese nonfiction persuades through understatement — soften to a sober statement while keeping the claim.
- **[seg 30·grandeur]** «それは、決してキャンセルされない唯一の約束である» → «それは、決して取り消されることのない、自分との約束である» — 英語の appointment that never gets cancelled を「キャンセル」で受けた広告的な締め。抑制した言い回しに寄せる。
- **[seg 38·grandeur]** «そして、これを読んで思わず座り込みたくならないなら、まだ理解できていないのだ。» → «そして、これを読んで思わず立ち止まらずにいられないとすれば、それはまだ十分に腑に落ちていないということなのかもしれない。» — TED的な聴衆へのアプラウズ・ライン。日本のノンフィクションは自己顕示的な断定を避けるため、驚きは残しつつ断定を控えめに和らげる。
- **[seg 53·grandeur]** «それこそが究極の裏づけとなる» → «それこそが何よりの裏づけとなる» — 「究極の」は英語 the ultimate vindication のセールス的な最上級。日本語ノンフィクションの抑制トーンでは誇張気味。驚きは残しつつ穏当な表現へ。

## C — deliberate motifs KEPT as-is (2)
- **[seg 5·motif]** «実在の側では灯りが消えている。» — 「灯りが消えている／ついている」は意識の不在・現前を示す本章の対比モチーフ（nobody-home系）。意図的反復として保持。
- **[seg 30·motif]** «はたして戻ってこられるのか、戻ってくるのが何人の自分なのか、誰にもわからない» — 第14章の危険ラインの固定モチーフ。KEEP（変更不可）。

## Genuine miss — quote not verbatim (69) — reviewer may apply manually
- **[seg 3·collocation]** «同じ欠けた中心のまわりを包んでいるにすぎない» → «同じ欠けた中心を取り囲んでいるにすぎない» — 「まわりを包む」はcircling/wrapping aroundの不自然な直訳。中心を取り巻く意味の自然な連語は『取り囲む』。
- **[seg 4·collocation]** «工場のフロア» → «工場の生産ライン» — "factory floor" calqued as 工場のフロア reads as an English loanword transfer; in a list of physical systems for a digital twin (ジェットエンジン、送電網、…) the idiomatic Japanese is 生産ライン/生産現場.
- **[seg 5·collocation]** «そして、あなたはそれを直接に意識することは、決して、絶対にない。» → «そして、それを直接に意識することは、決して、断じてない。» — 「あなたは……ことは……ない」は主題の二重ハ＋英語の主語直訳で不自然。あなたを外し、「決して、絶対にない」の英語式副詞重ね（never, absolutely never）を「決して、断じてない」に整える。
- **[seg 5·fluency]** «あなたは生涯をそのただ中で過ごし、決してその外へ出ることはない。» → «人は生涯をそのただ中で過ごし、決してその外へ出ることはない。» — ここのyouは一般的な「人」を指し、あなたを立てる必要がない。含意主語ないし「人は」のほうが常体の地の文になじむ。
- **[seg 6·collocation]** «それは過大なほど大きく、再帰的に構成されたネットワークであり» → «それは過剰なほど大きく、再帰的に構成されたネットワークであり» — 過大なほど大きい is a redundant/awkward collocation (過大 already means 'too large'); 過剰なほど大きい ('overbuilt to excess') is the natural rendering of the EN 'overbuilt'.
- **[seg 6·grandeur]** «息をのむようなグラフィック、リアルな物理挙動、引き込まれるストーリーを備えた、没入感のあるオープンワールドゲームだ» → «美しいグラフィック、リアルな物理挙動、先を追いたくなるストーリーを備えた、没入感のあるオープンワールドゲームだ» — Ad-copy adjective stack ('breathtaking / immersive / gripping') reads like marketing; Japanese nonfiction resolves toward sober description while keeping the vividness — softens 息をのむよう and 引き込まれる to reserved equivalents.
- **[seg 7·register]** «ホログラフィックの原理があなたを守る» → «ホログラフィックの原理が働いて損傷を食い止める» — ここの「あなた」は読者に議論の重みを負わせる payload ではなく、一般的な臨床事実の記述。文化ガイドの読者呼称規則に反する付随的なあなた——暗黙主語化すべき。
- **[seg 7·fluency]** «隠したあなたの本物の手» → «隠した本物の手» — 実演パラグラフでの直接呼称は許容範囲だが、「隠した」で既に文脈が確定しており「あなたの」は冗長。落とすとより自然な日本語の実演文になる。
- **[seg 8·typography]** «（ISM)——眠りが» → «（ISM）——眠りが» — 開き括弧が全角（で閉じ括弧が半角)の不整合。日本語本文では全角）に統一。
- **[seg 8·collocation]** «継ぎ目もなく、その繋ぎ目に気づく» → «継ぎ目もなく、その継ぎ目に気づく» — 同一文内で「seam」を継ぎ目と繋ぎ目に表記ゆれ。継ぎ目に統一。
- **[seg 9·grandeur]** «内部で打てる最強の一手であり» → «内部で打てる有力な一手であり» — 「最強の一手」はUS流の最上級ハイプ。日本の抑制されたノンフィクション文体では主張を残しつつ「有力な一手」と控えめに述べる方が説得的。
- **[seg 11·collocation]** «海全体を嵐へと叩き立てる» → «海全体を嵐へと煽り立てる» — 英語 whip the ocean into a storm の直訳。「叩き立てる」は自然な日本語コロケーションではない。
- **[seg 17·glossary]** «EWMが活動、ESMが完全に関与 | 自己認識の亢進» → «EWMが活動、ESMが完全に関与 | 自覚の亢進» — Glossary §2 FORBIDS 認識 as a rendering of awareness; lucid-dream heightened self-awareness (everyday sense) takes the permitted 自覚, not 自己認識.
- **[seg 18·glossary]** «**潜在的な気づき——内側に閉じ込められて**» → «**内に秘められた気づき——内側に閉じ込められて**» — 潜在的 is the glossary-FORBIDDEN pair (潜在的/顕在的 belongs to memory research and is locked out for implicit/explicit). For 'latent awareness' avoid 潜在的; 内に秘められた preserves the sense without importing the wrong literature.
- **[seg 18·glossary]** «だが、潜在的に意識のある患者は、まったく別のものだ。» → «だが、内に意識を保つ患者は、まったく別のものだ。» — Same forbidden 潜在的; the theory's implicit/explicit lock reserves 潜在的 for memory research. Rephrase to avoid it while keeping 'covertly conscious' meaning.
- **[seg 19·false-friend]** «受動的な受信機ではない» → «受動的な受け手ではない» — 受信機 is a radio/TV appliance (a receiver set); as a calque of EN "passive receiver" contrasting with a generative model it reads as hardware. 受け手 keeps the sense without the device connotation.
- **[seg 21·fluency]** «あなたはベッドに横たわり» → «ベッドに横たわり» — 「あなたが〜する」型の場面描写は日本語では暗黙主語が自然。ここは議論を担う二人称ではないので落とせる。
- **[seg 22·fluency]** «隣人を殺したあのキノコに、どこか怪しいほど似ている。あなたはそれを食べない。» → «隣人を殺したあのキノコに、どこか怪しいほど似ている。それを食べはしない。» — Incidental 'you' → あなた; subjectless Japanese is the default per reader-address rule, and あなた is over-used across this passage.
- **[seg 22·fluency]** «話はさらに良くなる。» → «しかも話はこれで終わらない。» — Calque of colloquial EN 'It gets better' — 話が良くなる is 翻訳調 as a paragraph opener; a native connective reads more naturally.
- **[seg 24·calque]** «地獄が凍りつくまで繰り返す» → «いつまでも延々と繰り返す» — 英語イディオム until hell freezes over の直訳。日本語に対応する慣用句がなく翻訳調。皮肉の色を残しつつ自然な「延々と繰り返す」に。
- **[seg 25·calque]** «私を夜も眠らせないものだ» → «私が夜も眠れなくなるほど気にかけている問題だ» — 英語イディオム「what keeps me up at night」の直訳。日本語としては使役の「眠らせない」が翻訳調で、自然な言い回しに直す。
- **[seg 26·calque]** «完全に戻ったときに私を打ったのは» → «完全に戻ったときに痛切に感じたのは» — 英語 "what struck/hit me" の直訳。「私を打った」は物理的打撃を連想させる翻訳調で、内面の実感には「痛切に感じた」が自然。
- **[seg 27·false-friend]** «はるかに悪いのではないかと私は疑っている» → «はるかに悪いのではないかと私はにらんでいる» — 英語suspectの偽の友。日本語の「疑う」は「悪いこと自体を疑う」意に読め逆転する。ここは推量なので「にらんでいる／見ている」が自然。
- **[seg 30·fluency]** «鷹のように目を光らせておくべき食い違いが三つある» → «厳しく目を光らせておくべき食い違いが三つある» — 「鷹のように」は英語 watch like a hawk の直訳。日本語では「目を光らせる」だけで十分自然。
- **[seg 30·collocation]** «これをスポーツに仕立て上げた» → «これを一種の遊びにしてしまった» — 英語 made a sport of it の直訳。日本語で「スポーツに仕立て上げる」は競技化の意にとられ、原意（面白半分の慣習）とずれる。
- **[seg 31·glossary]** «その最小限で成立するversion までは特定していない» → «その最小限で成立する形態までは特定していない» — Untranslated English word "version" plus a Latin-token inter-word space left in Japanese prose; render as 形態 (or 形) with no space.
- **[seg 31·register]** «夜も眠れなくさせると君に告げた、あの問いだ» → «夜も眠れなくさせると告げた、あの問いだ» — 君 is explicitly forbidden as reader-address; here the second person is not the argument's payload, so drop to implicit subject.
- **[seg 35·collocation]** «精確な意味において» → «厳密な意味で» — 「精確な意味において」は英語 in a precise sense の直訳的で硬い翻訳調。日本語では「厳密な意味で」が自然な定着表現。
- **[seg 35·calque]** «体系的に地図化したかどうか» → «体系的に調べ上げたかどうか» — 「地図化した」は英語 mapped out の直訳的カルク。ここでは全体像を系統的に把握する意なので「調べ上げた／整理した」が自然。
- **[seg 37·calque]** «初めてそれを見たとき、私を思わず座り込ませたものがここにある» → «初めてそれを見たとき、私は思わず座り込んでしまった。それがこれだ» — EN "what made me sit down" object-causative calqued as 私を…座り込ませたもの; natural JA prefers the author as subject reacting, then pointing at the thing.
- **[seg 38·grandeur]** «そして、これを読んで思わず座り込みたくならないなら、まだ理解できていないのだ。» → «そして、これを読んで思わず立ち止まらずにいられないとすれば、それはまだ十分に腑に落ちていないということなのかもしれない。» — TED的な聴衆へのアプラウズ・ライン。日本のノンフィクションは自己顕示的な断定を避けるため、驚きは残しつつ断定を控えめに和らげる。
- **[seg 39·fluency]** «ディナーパーティーで交わす興味深い会話の種になる» → «食事の席での気の利いた話の種になる» — EN "dinner-party conversation"の慣用句カルク。ディナーパーティーは日本語で自然な社交枠でなく、名詞前の連体修飾も重い。意味を残して自然化。
- **[seg 40·calque]** «以来その握力はゆるんでいない» → «以来その手応えは少しも弱まっていない» — 英語 "its grip hasn't loosened" の直訳。反論に「握力（=手を握る力）」を当てるのは翻訳調で、日本語では不自然。
- **[seg 41·typography]** «のなら(宇宙が本当に自己相似的» → «のなら（宇宙が本当に自己相似的» — Half-width ( ) wraps a Japanese-text parenthetical; JA prose requires full-width （）. The closing paren later in the same sentence must be switched to ） too.
- **[seg 41·collocation]** «ほぼ無限のクラス4系であるのなら)、もう一手ある» → «ほぼ無限のクラス4系であるのなら）、もう一手ある» — Closing half-width ) of the same parenthetical; convert to full-width ） to match the opening fix.
- **[seg 42·fluency]** «そこでFrancis CrickとKochは、意識の神経相関を求めて視覚系を段階を追って体系的に踏破した» → «そこではフランシス・クリック（Crick）とコッホ（Koch）が、意識の神経相関を求めて、視覚系を段階を追って体系的に踏破した» — 英語の "in which" 型の後置修飾を「そこで」で受けており、走り文のなかで研究者名がラテン表記のまま。用語集§4に従い初出はカタカナ＋（原綴）が自然。
- **[seg 45·collocation]** «まさにこの故障の型を示す» → «まさにこの種の機能不全を示す» — 「failure mode」を「故障の型」と機械翻訳的に直訳している。認知システムの体系的欠陥には「この種の機能不全」が自然。
- **[seg 47·false-friend]** «最も無秩序なものへと、清潔な単調勾配として並べる» → «最も無秩序なものへと、きれいな単調勾配として並べる» — 「clean（=整然とした）monotonic gradient」の誤訳。清潔は衛生的な清らかさを指す false-friend。同じ概念を後段（line 40）は正しく「きれいな単調勾配」と訳しており、そちらに揃える。
- **[seg 47·calque]** «独自の分類の枠組みに値する、とは独立に論じた» → «独自の分類の枠組みに値すると、独立に論じている» — 「Rowland independently argued that …」の語順カレ。読点＋「とは独立に論じた」が翻訳調で、引用節と副詞「独立に」の係りが不自然。「値すると、独立に論じている」で自然な日本語の流れにする。
- **[seg 48·collocation]** «多くのランダムさの統計検定を通過する» → «ランダムさの統計検定の多くを通過する» — English noun-stacking calque of "passes many statistical tests of randomness"; 「多くのランダムさの統計検定」 misreads as "tests of much randomness" — 多く should quantify the tests, not modify randomness.
- **[seg 49·anglicism]** «そこへ至るための最も easy な方法である» → «そこへ至るための最も簡単な方法である» — Untranslated English word "easy" left inline in Japanese prose; must be rendered as 簡単な.
- **[seg 50·glossary]** «一つのシミュレーションなのだという静かな認識が» → «一つのシミュレーションなのだという静かな気づきが» — 「認識」is on the forbidden list for rendering awareness; this is the awareness-of-a-content moment (aware that the world is a simulation), which the glossary locks to 気づき.
- **[seg 50·typography]** «世界の幾何学(カップがどこにあるか、その周囲にどんな障害物があるか)» → «世界の幾何学（カップがどこにあるか、その周囲にどんな障害物があるか）» — Half-width ( ) wrapping Japanese prose; the typography rule mandates full-width （） for parentheticals inside Japanese text.
- **[seg 50·typography]** «自己の運動学(腕がどう構えられているか、握るために指をどう形づくるべきか)» → «自己の運動学（腕がどう構えられているか、握るために指をどう形づくるべきか）» — Half-width ( ) around Japanese prose must be full-width （）.
- **[seg 50·typography]** «知識(世界)と、その中での自分の評価(自己)» → «知識（世界）と、その中での自分の評価（自己）» — Two half-width paren pairs wrapping Japanese words; must be full-width （） in Japanese prose.
- **[seg 50·typography]** «正典的モデル(IWM、ISM、EWM、ESM)» → «正典的モデル（IWM、ISM、EWM、ESM）» — Parenthetical is Japanese-punctuated (full-width 、 inside), so the enclosing parens must be full-width （）, not half-width.
- **[seg 50·typography]** «完全に暗黙的(構造的、貯蔵された、無意識的)» → «完全に暗黙的（構造的、貯蔵された、無意識的）» — Half-width ( ) around Japanese prose must be full-width （）.
- **[seg 50·typography]** «完全に明示的(シミュレートされた、一過性の、現象的)» → «完全に明示的（シミュレートされた、一過性の、現象的）» — Half-width ( ) around Japanese prose must be full-width （）.
- **[seg 51·typography]** «元がない(学習された知識がない)» → «元がない（学習された知識がない）» — Half-width ASCII parentheses in Japanese prose; culture guide locks full-width （） for JA-text parentheticals.
- **[seg 51·typography]** «まったくない(体験がない)» → «まったくない（体験がない）» — Half-width parens in JA prose parenthetical; must be full-width （）.
- **[seg 51·typography]** «重い複製(ミュー粒子)と» → «重い複製（ミュー粒子）と» — Half-width parens around a JA-prose gloss; must be full-width （）.
- **[seg 51·typography]** «らに重い複製(タウ粒子)が» → «らに重い複製（タウ粒子）が» — Half-width parens around a JA-prose gloss; must be full-width （）.
- **[seg 51·typography]** «クラス3(フラクタル)の» → «クラス3（フラクタル）の» — Half-width parens around a JA-prose gloss; must be full-width （）.
- **[seg 51·typography]** «粒子(タウ粒子、トップクォーク)» → «粒子（タウ粒子、トップクォーク）» — Half-width parens around a JA-prose parenthetical; must be full-width （）.
- **[seg 51·typography]** «なお成り立つだろう(五つの対応はE=Iに依存していない)» → «なお成り立つだろう（五つの対応はE=Iに依存していない）» — Half-width parens around a JA-prose aside; must be full-width （） (E=I stays as-is inside).
- **[seg 51·typography]** «すべての特異点(プランクスケール、ブラックホール、宇宙論的なもの)» → «すべての特異点（プランクスケール、ブラックホール、宇宙論的なもの）» — Half-width parens around a JA-prose list gloss; must be full-width （）.
- **[seg 51·typography]** «これほどまでに絶対なのか?» → «これほどまでに絶対なのか？» — Half-width ASCII question mark in JA prose; use full-width ？ (heading question).
- **[seg 51·typography]** «観測されていない。なぜか?» → «観測されていない。なぜか？» — Half-width ASCII question mark in JA prose; use full-width ？.
- **[seg 52·collocation]** «理論の足元を火にあぶってみたい読者» → «理論を容赦なく吟味してみたい読者» — 「hold feet to the fire」の直訳。足元を火にあぶるは日本語に定着した言い回しではなく翻訳調——native表現に。
- **[seg 52·calque]** «あなたを深く疑わせるはずのやり方で自らを批判から免疫化している» → «あなたを深く疑わせるはずのやり方で自らを批判の届かないところに置いている» — 「immunize itself against criticism」の直訳。免疫化は不自然——native の「批判の届かないところに置く」へ。
- **[seg 52·typography]** «正直なところ?私にはどちらなのか» → «正直なところ？私にはどちらなのか» — 日本語地の文で半角?を使用。全角？に統一すべき。
- **[seg 52·typography]** «そんなことをするような人間だろうか?」» → «そんなことをするような人間だろうか？」» — 「」内の反語疑問文で半角?を使用。日本語では全角？が正。
- **[seg 53·typography]** «何時間も(あなたが目覚めている一日じゅう)» → «何時間も（あなたが目覚めている一日じゅう）» — 日本語内容の傍注に半角( )。全角（）に統一。
- **[seg 53·grandeur]** «それこそが究極の裏づけとなる» → «それこそが何よりの裏づけとなる» — 「究極の」は英語 the ultimate vindication のセールス的な最上級。日本語ノンフィクションの抑制トーンでは誇張気味。驚きは残しつつ穏当な表現へ。
- **[seg 54·typography]** «解離性同一性障害(一人の人間のなかに複数の異なる同一性» → «解離性同一性障害（一人の人間のなかに複数の異なる同一性» — Half-width ( on a Japanese-prose parenthetical; culture guide locks full-width （） for asides in JA text.
- **[seg 54·typography]** «現れているあいだの脳活動(fMRIまたはEEG)を記録する» → «現れているあいだの脳活動（fMRIまたはEEG）を記録する» — Japanese-prose parenthetical (contains JA 「または」) must use full-width （）; half-width only for pure verbatim Latin spans.
- **[seg 54·fluency]** «明示的自己モデルが活性化し、あなたは明晰になる» → «明示的自己モデルが活性化し、明晰な状態になる» — あなた here is an incidental EN 'you' calque, not an argument-carrying second person; JA default is implicit subject.
- **[seg 54·fluency]** «睡眠不足は、あなたを臨界下へと追いやる» → «睡眠不足は、脳を臨界下へと追いやる» — Incidental あなた from EN 'you'; the referent is the brain — implicit/脳 subject reads more naturally in JA nonfiction.
- **[seg 54·fluency]** «十分に長く起きていれば、あなたの脳の臨界性は» → «十分に長く起きていれば、脳の臨界性は» — あなたの is a redundant EN-possessive calque; dropping it keeps the implicit-subject JA register.

## Ambiguous — quote appears >1×, skipped (1)
- **[seg 28·calque]** «シナリオを走らせ» → «シナリオを試し» — "run scenarios" — 走らせる has some currency for シミュレーション in tech JA, but "シナリオを走らせる" is calque-y in polished nonfiction; 試す/検討する reads more native.

## Whole-book coherence pass (S254, 1 Opus read) — 13 findings

**8 ja-only APPLIED** (verified match-once):
- **Salvia katakana unified** ×3: サルビア・ディビノ**ラ**ム → サルビア・ディビノ**ル**ム (第6章 l.636/650/670, matching glossary/初出).
- **TOC↔heading alignment** ×3: 第3章 見出し「仮想の側面」→「仮想の側」(term-consistent); 目次 第8章「臨床の鏡」→「臨床という鏡」; 目次 第10章「動物という問い」→「動物の問い」.
- **HIGH — stutter/dup bug fixed** (第16章 l.1682): 「初めてそれを見たとき、私は初めてそれを見たとき」→ 「初めてそれを見たとき、私は」(a real Fable duplication error at the book's climactic reveal).
- **register-drift**: section heading 「### オチ」(punchline/gag slang, wrong register for the reveal) → 「### 明かされるもの」. **Reviewer: confirm the replacement heading.**

**5 structural → logged to AIW-109** (NOT patched per-language — cross-confirm the IT pass): Ch.12 neuron contradiction (百万 vs 8万5000/日), Ch.10 loop-close off-by-one (前章→第8章), Coda re-narration (雪崩/ノックアウト), Ch.15 self-org criticality re-intro, + NEW item G "ドイツ語版の分析" authorial self-reference (faithful to EN "the German book's analysis"). See `docs/aiw109-shipped-ed2-temporal-report.md`.

**Status:** JA = **publish-candidate** (323 Kalk + em-dash normalization + 3 separators + 8 coherence fixes). Gate: human native Japanese reviewer before any KDP upload. Reviewer priorities: the deferred half-width→full-width paren normalization, the オチ→明かされるもの heading, and the B-category voice calls in the git diff.