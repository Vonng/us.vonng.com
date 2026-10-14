# B-PL-R2-2 第三静态审阅记录

- 审阅日期：2026-10-14
- 审阅人：`B-PL-R2-THIRD`（独立第三人静态审，只读不改；唯一写操作为本记录文件）
- 审阅范围：R2-2 批次 2 处语言修订（工作区未提交差分）
- 审阅时基线：HEAD `560a5b50c7a60abbbecd879fc0cec2505619cee5`（父提交 `f6170ac`，即 R2 账本所记基线）；工作区改动仅为 R2-1／R2-2 的 3 个 content 文件加账本，无其他批次改动混入
- 规则依据：`AGENTS.md`、`ops/PROMPT-SPEAK-PLAINLY-R2.md`（红线一节、甲类改写规则）

## 审阅对象

| 文件 | 修订前 body SHA-256 | 修订后 body SHA-256 | 差分量 |
|---|---|---|---|
| `content/book/life/documents/entry-return.md` | `8293f92189a7e8c44708dde97aec1d266f82bd123a860ec0121ce3a9149efd42` | `e0ea3b76c8ebb055f33fdbfbe45c37d80accb1cbd809a12611361b2b9803981f` | 1 hunk，1 行 |
| `content/book/life/documents/status-documents.md` | `16e535093fd8b475a697b10581a6e99d920b8424a71d5d80929c786a924c4721` | `c2897386c6b55d8f727288f241d5b12c3d68eb64b6fbc8486e0d583a15994224` | 1 hunk，1 行 |

四个 SHA 均由本人按账本口径实算：修订前取 `git show HEAD:<文件>`、修订后取工作区文件，各经 `python3 -c "import hashlib,sys; print(hashlib.sha256(open(sys.argv[1]).read().split('---',2)[2].encode()).hexdigest())" <文件>`。两个修订后值分别与账本 `ops/reviews/speak-plainly-r2-progress.md` 第 47、49 行登记值逐字符一致。

## 实际读到的差分

### 文件一 `entry-return.md`

唯一 hunk 为 `@@ -50,7 +50,7 @@`，改动第 53 行。修订前（340 字符）与修订后（338 字符）该行仅一处不同，句段对照：

- 修订前：`……这是诉讼期间救济，不能写成永久撤销。USC 的办理提示也说明 D/S 继续。……`
- 修订后：`……这是诉讼期间救济，不是永久撤销。USC 的办理提示也说明 D/S 继续。……`

字符级 SequenceMatcher 比对，整行仅一条 opcode：`[replace] 能写成 → 是`（"不"为等值锚点），即 `不能写成永久撤销` 改为 `不是永久撤销`。行内其余内容——日期 `2026年9月15日`、`9月14日`，`D/S`，`固定四年`，句末两条引用链接——逐字符未动。

### 文件二 `status-documents.md`

唯一 hunk 为 `@@ -32,7 +32,7 @@`，改动第 35 行。修订前（248 字符）与修订后（246 字符）该行仅两处不同：

- 修订前：`……D/S 并不意味着无需管理毕业、项目终止或授权工作的日期。[国务院：入境与停留](https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/visa-expiration-date.html)`
- 修订后：`……写 D/S 时仍要管理毕业、项目终止或授权工作的日期。[国务院：入境与停留](https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/visa-expiration-date.html)`

字符级比对，整行两条 opcode：行首 `[insert] 写 `（置于原主语 `D/S` 前），`[replace] 并不意味着无需 → 时仍要`。行内其余内容——同句前半的条件句与 `**D/S（Duration of Status）**` 加粗标记及其后空格、三个管理对象 `毕业、项目终止、授权工作`、句末引用链接——逐字符未动。

## 七项逐项核对（两文件分别给证据）

### 1. 只动语言

- `entry-return.md`：通过。整行唯一 opcode 是 `能写成`→`是` 的 3 字符换 1 字符替换；行内两个日期、`D/S`、`四年` 等全部事实 token 在等值段中逐字符保留。全文无第二个 hunk。表格 14 行逐字节相同。
- `status-documents.md`：通过。整行仅 `写 ` 插入与 `并不意味着无需`→`时仍要` 替换；被改句不含金额、期限、日期、数字、法条编号。表格 14 行逐字节相同。

### 2. 链接完整

- `entry-return.md`：通过。修订前 64 条链接，修订后 64 条；`[文字](URL)` 整串与 URL 两种多重集比对均完全一致。改动行上的两条链接 `[实际法院命令，第 44—48 页](https://www.govinfo.gov/content/pkg/USCOURTS-mad-1_26-cv-13799/pdf/USCOURTS-mad-1_26-cv-13799-0.pdf)` 与 `[USC 学校办理提示](https://ois.usc.edu/dhs-final-rule-postponed/)` 位置未动，仍在句末原挂点。
- `status-documents.md`：通过。修订前 13 条，修订后 13 条；两种多重集比对均完全一致。`[国务院：入境与停留](https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/visa-expiration-date.html)` 仍在被改句句末，逐字节未变。

### 3. frontmatter 逐字节不变

- 两文件均通过。程序化比较修订前后 `split('---',2)[1]` 完全相等；各自 diff 的唯一 hunk 分别落在第 53、35 行正文区，不触及 `---` 区块。`entry-return.md` 的 `verified: "2026-10-14"`、`reviewed_by`，`status-documents.md` 的 `verified: '2026-10-13'`、`reviewed_by: health` 等全部字段保持原值，符合"语言修订保留原审阅历史"的先例。

### 4. 事实范围等同（逐义比对）

- `entry-return.md`：通过。原句 `这是诉讼期间救济，不能写成永久撤销` 的命题内容是"暂缓 ≠ 永久撤销"，`不能写成` 是面向写作者的防御性措辞（指导如何表述），不向读者多给任何事实；改后 `不是永久撤销` 把同一命题直接陈述。未加强（未断言规则已失效、将被恢复或诉讼结果）、未弱化、未扩大（"诉讼期间救济"定性原样保留在前半句）。读者可执行行为不变：不把暂缓当作永久撤销，按下一句（未改动）让 DSO／RO 核后续变化、再核实际 I-94。
- `status-documents.md`：通过。原句是双重否定 `D/S 并不意味着无需管理……日期`，逻辑等值于 `D/S ⇒ 需管理`；改后 `写 D/S 时仍要管理……日期` 正是该正面式，命题完全等值。条件限定 `写 D/S 时` 与同句前半已给出的条件 `如果写 **D/S（Duration of Status）**` 同源同范围，未新增适用对象；三个管理对象逐字保留。读者可执行行为不变：I-94 写 D/S 仍要追踪毕业、项目终止、授权工作三个日期。属 R2 提示词甲类"否定改正面、事实范围不变"的标准形态（同示例 2）。

### 5. 无新增事实、无编造补齐

- 两文件均通过。字符级 opcode 显示两处改动均为既有断言的措辞替换，无任何新增文本块；`写 D/S 时` 的条件取自同句既有条件句，非新事实。

### 6. 语言质量

- `entry-return.md`：通过。`不能写成` 这类面向写作者的元措辞换成直接否定 `不是`，削减防御性表达；未引入对冲堆叠、兜底句或翻译腔。
- `status-documents.md`：通过。删去甲类检测词 `并不意味着` 与 `无需` 构成的双重否定，换成读者一遍即懂的正面规则；改后是完整陈述句，非电报式残句，未引入新的 AI 腔。

### 7. 表格行列结构、标题层级、加粗空格

- 两文件均通过。标题行（`entry-return.md` 9 条、`status-documents.md` 5 条）修订前后逐字节相同，层级不变；表格行（各 14 行）逐字节相同，行列结构不变。两处改动行内被触碰的字符段均无加粗标记；`status-documents.md` 改动行前段的 `**D/S（Duration of Status）** ，` 加粗及外侧空格落在等值段，未被触碰。中文加粗内外空格规则全文未被破坏。

## 结论

- `content/book/life/documents/entry-return.md`：**通过。** 唯一改动是 `不能写成永久撤销`→`不是永久撤销` 的措辞级替换，字符级证据显示行内其余内容逐字未动，命题与读者行为不变。
- `content/book/life/documents/status-documents.md`：**通过。** 唯一改动是双重否定改逻辑等值的正面陈述，条件、对象、引用逐字保留，符合甲类改写要求。

两文件账本登记的修订后 SHA 均与本人实算一致，未发现任何红线违规。

## 未核实边界

- 本人未访问、未回源任何外部 URL（`govinfo.gov` 法院命令 PDF、`ois.usc.edu`、`travel.state.gov`、`i94.cbp.dhs.gov` 等），链接目标内容、日期与事实本身未重新核实。
- 本人未重跑事实审；本记录是针对差分与红线的静态审，不替代两文件原有的独立事实审结论。
- 未构建、未渲染；构建与渲染检查属主控验收环节。
- 仅覆盖上述 2 处差分及其波及行；未对两文件其余未改动正文做新一轮语言复审，未涉及 R2-1 及其他批次文件。
