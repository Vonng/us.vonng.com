# B02 隔离与民权史：独立事实审

审查人：documents；作者 civic，为不同参与者。实际查阅日期：2026-10-13。对象：`content/book/foundations/history/segregation-civil-rights.md`。

结论：事实审通过。作者已完成一项术语修订，审阅者重读两处改文并重新计算最终正文 SHA-256：`0f3d9430be295eccb387b5e85cd3a8af6cdeaa194eeffff0e23773f453a5cf19`。计算方法为 `sha256(text.split('---', 2)[2].encode('utf-8'))`，不含 frontmatter。年代、原始法律范围、地方案例与历史因果解释均已逐项核对；第三人静态审及主控构建另行进行。

## 独立实际阅读

完整读稿与作者证据后，另行打开下列原始文本或官方历史资料。普通 HTTPS 成功时直接读取正文；web 工具只用 open 到的实际内容，不以搜索摘要代读。原法 PDF 独立从 GovInfo 获取到内存并解析，同时查看已缓存的第 83 页扫描图核对 OCR。

| 一手资料、官方历史材料 | 本轮实际位置及核对结论 |
|---|---|
| [NARA 第十三修正案](https://www.archives.gov/milestone-documents/13th-amendment) | 导言与 Transcript §1：1863 宣言的叛乱地区限制、1865 年 12 月批准、美国及其管辖范围、依法定罪者惩罚例外。没有将宣言写成一举全国废奴。 |
| [NARA 第十四修正案](https://www.archives.gov/milestone-documents/14th-amendment)、[第十五修正案](https://www.archives.gov/milestone-documents/15th-amendment) | 两页原文 §1 与导言：1868/1870 年、出生或归化且受管辖、公民与任何人之别、联邦/州不得按种族肤色及曾受奴役限投票、后续识字等障碍。稿件未把平等保护缩成仅保护公民，也未声称 1965 以后所有投票障碍消失。 |
| [NPS Eric Foner：Reconstruction](https://www.nps.gov/articles/reconstruction.htm) | 独立全文阅读；1865—1877 通常分期、黑人参政、妇女权利未同步实现、1865 归还土地、KKK 暴力、1877 联邦支持退却。叙述保留黑人及社区主动建设，不只是总统和法案时间表；分期没有把社会变化定为同一天结束。 |
| [NPS 重建时期学校](https://www.nps.gov/articles/reconstruction-era-african-american-schools-in-the-south.htm) | 实读全文，重点 Tolson’s Chapel：Sharpsburg、1866 教堂、自由民局安排教师后转社区教师、儿童和成人日夜课程。正文没有把教堂落成日误写成确定开学日。 |
| [Smithsonian：Jim Crow Laws](https://americanhistory.si.edu/brown/history/1-segregated/jim-crow.html) | 独立读 Missouri 1929、Tennessee 1891 原条文转录，以及 Arlington 1940 年代契约展品说明；包含被排斥的其他群体。稿件把这些作为历史证据，并未冒称为现行法或亲见完整契约。 |
| [NARA：Brown v. Board](https://www.archives.gov/milestone-documents/brown-v-board-of-education) | 完整导言、Syllabus 与 Opinion 转录：1954-05-17、一致判决、要求/允许隔离的州法、公校领域、设施等有形条件不足以正当化隔离、七词直接引文；1955 Brown II 才进一步讨论实施。1896 Plessy 的交通案件性质也在原文核到。 |
| [NARA：EO 10730](https://www.archives.gov/milestone-documents/executive-order-10730) | 完整历史导言及原命令 §§1—4、落款：九名学生与州卫队阻挡、群众威胁、联邦控制与军队授权。导言写 9 月 23 日而命令落款 9 月 24 日，稿件只用 1957 年，未传递冲突日期；也没有照抄该页把 Brown I 与 II 速度表述混为一谈的写法。 |
| [NARA：1964 Civil Rights Act](https://www.archives.gov/milestone-documents/civil-rights-act) | 导言、法案总说明与 Title VI §§601—605 原文；接受联邦资助项目、race/color/national origin、实施规则及执行方式。正文只作历史转变说明，不把原始雇主门槛等当现行操作要求。 |
| [NPS：底特律历史场所](https://www.nps.gov/articles/000/architecture-and-preservation-in-detroit.htm) | 独立全文，重点开头和 Miller 段：1930 年代中期学校改变、允许白人转往 Eastern、住宅契约、银行拒贷及 1950 年代起搬迁。正文将居住与转学政策结合解释，且明确地方案例，不说所有北方城市同一原因。 |
| [NPS：Shelley House](https://www.nps.gov/places/missouri-the-shelley-house-l.htm) | 独立全文：购房、邻居起诉、1948 裁判禁止法院执行契约，私人排斥并未因此立刻消失。原页 due process/equal protection 用语不够一致；稿件只采用执行结论，未照抄其法理细节。 |
| [GovInfo：Public Law 90-284，82 Stat.73](https://www.govinfo.gov/content/pkg/STATUTE-82/pdf/STATUTE-82-Pg73.pdf) | 独立读取纸页 81—83，即 PDF 第 9—11 页，Title VIII §§801—805：1968-04-11、住宅销售/出租/融资、当年四项保护理由、分阶段适用及例外。§805 OCR 把 1968 误作 1908；实际查看 `.cache/research/civic/history-stat82-p83.png` 对照原扫描。稿件没有倒填后来增加的 sex/disability/familial status，也没有把所有条文说成当天全部生效。 |

## 修订与范围判断

发现并完成修订的一项术语精度问题：两处 `national origin` 原译“原国籍”，可能被理解为先前持有的法律国籍，掩盖本人或家庭来源背景。作者已将两处统一为“原籍背景（national origin）”，审阅者核对通过。为核对该风险，另实际打开 [HUD 2011 年历史说明](https://archives.hud.gov/news/2011/pr11-055.cfm) 的 national origin 段：明确包括 ancestry，也可能涉及美国出生公民的家庭来源。此来源只用于译名精度，不将 2011 年完整现行权利列表倒写进 1968 年历史；作者后续无法打开该页，不影响本轮审阅者已读原文的记录，也没有冒记作者读取。

文章末段是有出处地方案例基础上的历史解释：撤除禁止不能自动重排已有住宅与校址。作者明确指出不能据此认定今日某地所有差异的单一原因，并要求查当代边界、就业、住房价格、迁移及资料年份。未采用未核实的当代隔离率、财富差距或学校评分因果数字；没有用族群比例替代对居民或教育质量的判断。

未审核范围：完整奴隶制与内战史、全部民权运动组织、其他族群历史、当前出生公民权诉讼、现行住房/教育投诉资格与期限、任何具体社区今天的状况。增加这些内容须新增研究和审查，不能沿用本次通过范围。
