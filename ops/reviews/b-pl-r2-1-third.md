# B-PL-R2-1 第三静态审阅记录

- 审阅日期：2026-10-14
- 审阅人：`B-PL-R2-THIRD`（独立第三人静态审，只读不改；唯一写操作为本记录文件）
- 审阅范围：R2-1 批次 1 处语言修订（工作区未提交差分）
- 审阅时基线：HEAD `560a5b50c7a60abbbecd879fc0cec2505619cee5`（父提交 `f6170ac`，即 R2 账本所记基线）；`git status` 显示工作区改动仅为 R2-1／R2-2 的 3 个 content 文件加账本 `ops/reviews/speak-plainly-r2-progress.md`，无其他批次改动混入
- 规则依据：`AGENTS.md`、`ops/PROMPT-SPEAK-PLAINLY-R2.md`（红线一节）

## 审阅对象

| 文件 | 修订前 body SHA-256 | 修订后 body SHA-256 | 差分量 |
|---|---|---|---|
| `content/book/foundations/culture/invitations-boundaries.md` | `56a9c74590f03b0447e5e46859b3ed18efcd44f2cfb1e62e2b1d77966d0297d1` | `b9f0e449db9e1128a7fb39345beb462079cc089a0e617acb40779c06f060abe8` | 1 hunk，1 行 |

两个 SHA 均由本人按账本口径实算：修订前取 `git show HEAD:<文件>`、修订后取工作区文件，各经 `python3 -c "import hashlib,sys; print(hashlib.sha256(open(sys.argv[1]).read().split('---',2)[2].encode()).hexdigest())" <文件>`。修订后值与账本 `ops/reviews/speak-plainly-r2-progress.md` 第 23 行登记值逐字符一致。

## 实际读到的差分

`git diff HEAD` 唯一 hunk 为 `@@ -52,7 +52,7 @@`，改动第 55 行。修订前（308 字符）：

> 表达邀请时，熟人间的 "Do you want to…" 和更留余地的 "Would you like to…" 都可以使用，选择看关系与活动。教学资料把说话者关系和任务类型放在一起分析，而不是规定所有邀请只能用一种句型。[Relationship between Speakers and Task Type，第 1—2、12 页](https://americanenglish.state.gov/files/ae/resource_files/biesenbach_0.pdf)

修订后（269 字符）：

> 表达邀请时，熟人间的 "Do you want to…" 和更留余地的 "Would you like to…" 都可以使用，选择看关系与活动。[Relationship between Speakers and Task Type，第 1—2、12 页](https://americanenglish.state.gov/files/ae/resource_files/biesenbach_0.pdf)

对该行做字符级 SequenceMatcher 比对，opcode 只有一条 `[delete]`，被删字符串为：

> 教学资料把说话者关系和任务类型放在一起分析，而不是规定所有邀请只能用一种句型。

行内其余部分（含引用链接整串）逐字符相同；行长度差 308−269=39，恰等于被删句的长度。此改动即 R2 提示词"判定示例 1"预审通过的原型改法：删元叙述句，引用移挂前句句末。

## 七项逐项核对

1. **只动语言**：通过。差分仅一条纯删除 opcode，无任何插入或替换；被删句内不含金额、期限、日期、数字、法条编号，也不属于任何表格。修订行之外全文无差分。表格 20 行逐字节相同（程序化比对）。
2. **链接完整**：通过。修订前正文链接 8 条，修订后 8 条；对全文 `[文字](URL)` 整串及 URL 单独分别建多重集比对，均完全一致。被移动的链接 `[Relationship between Speakers and Task Type，第 1—2、12 页](https://americanenglish.state.gov/files/ae/resource_files/biesenbach_0.pdf)` 逐字节未变，从被删句后移挂到承接其事实的前句（"……都可以使用，选择看关系与活动"）句末，属规则允许的相邻句移挂，无丢失、无新增、无改写。
3. **frontmatter 逐字节不变**：通过。程序化比较修订前后 `split('---',2)[1]`（frontmatter 段）完全相等；diff 唯一 hunk 落在第 55 行正文区，不触及 `---` 区块。`status: integrated`、`draft: false`、`verified: '2026-10-14'`、`reviewed_by` 均保持原值，符合本轮"语言修订保留原审阅历史"的先例。
4. **事实范围等同**：通过。被删句是替引用来源辩护的元叙述（"教学资料……而不是规定……"），读者无法据其做出任何具体行为；其承载的实质信息——句型选择取决于关系与活动——已由保留的前句"都可以使用，选择看关系与活动"完整表达。修订前后读者可执行的行为一致：两种句型都可用，按关系与活动取舍。断言未被加强（未变成"所有人都这样用"之类）、未被弱化、未扩大。
5. **无新增事实、无编造补齐**：通过。字符级比对显示纯删除，无任何插入文本，不存在补齐或新增断言的通道。
6. **语言质量**：通过。改动删去一处"而不是"式防御性元叙述（甲类检测词命中处的合法清除），结果句以完整陈述句加句末引用收尾，非电报式残句；未引入对冲堆叠、兜底句、防御性插入语或翻译腔。
7. **表格行列结构、标题层级、加粗空格**：通过。标题行（共 6 条）修订前后逐字节相同，层级不变；表格行（共 20 行）逐字节相同，行列结构不变；改动行及被删句内无加粗标记，全文中文加粗内外空格规则未被触碰。

## 结论

**通过。** 唯一差分是 R2 提示词预审示例的原样落地：删除一句无读者行动价值的元叙述并把引用链接完整移挂到承接句，七项红线核对全部有逐字节或程序化证据支撑，账本登记的修订后 SHA 与实算一致。

## 未核实边界

- 本人未访问、未回源任何外部 URL（含 `americanenglish.state.gov` 的 PDF 原文），链接目标内容与该页事实本身未重新核实。
- 本人未重跑事实审；本记录是针对差分与红线的静态审，不替代原事实审结论。
- 未构建、未渲染；构建与渲染检查属主控验收环节。
- 仅覆盖上述 1 处差分及其波及行；未对该文件其余未改动正文做新一轮语言复审，未涉及 R2-2 及其他批次文件。
