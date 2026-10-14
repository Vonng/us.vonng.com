# B-PL照护页v2留白补正：独立补充差分事实审

2026-10-14（Asia/Shanghai），独立事实审 banking_fact；语言修订作者 root，第三静态审 birth_fact。仅本新补充记录及事前逐具体路径核忽略的本人缓存；未改 canonical、作者记录、已冻结 people15 FACT、其他审阅或共享文件，未构建、提交、安装。

**PASS（差分及完整上下文范围）** 。结论只绑定下表 v2 完整正文。本人本轮真正从frontmatter至末行全读v2照护148行／22,778字节、作者补充16行，以及真实v1→v2四处diff。四个ASCII空格没有改变人员、法域、年龄、项目、机构职责、号码、资格、期限、材料、渠道或继续动作；无必要返修。旧155行FACT的照护结论签的是v1，不能仅把旧摘要套到v2。

## 实际版本与六项摘要

正文算法为UTF-8完整文本`full.split("---",2)[2]`，保留换行；整件直接哈希原始字节。

| 版本与实际文件 | 行／字节 | 完整body SHA-256 | whole SHA-256 |
|---|---|---|---|
| 原始冻结版：`.cache/b-pl-people-proposals/original/content/book/people/aging/caregiving-plan.md` | 148／22660 | `67cbe66df380938966b619fc692145282321bf43696522a0a682788dafc85c1a` | `88bc9cc0ae8e8f3cccd5ed46e9cba708d56094b64ef3b0e93aaeb2d0a3d6f638` |
| 既有已审拟稿v1：`.cache/b-pl-people-proposals/proposed/content/book/people/aging/caregiving-plan.md` | 148／22774 | `a7667b144d1aec0e555d291269b48f6b4f17879fd92b6caf65ff73b8444c02c7` | `ff03465d86b05d890acef55cc312a5c0dce16ab4b95c1136af62e240c36b4c93` |
| 本补充最终拟稿v2：`.cache/b-pl-people-proposals-v2/proposed/content/book/people/aging/caregiving-plan.md` | 148／22778 | `9a5cf557ecbd0ac87bcb7df0831bdac58c0cb324fbef20f5b48c27f769bd3609` | `349a5369aaa00545e6aae4ad89307a50f872003d731fb9fcaedba77418ea27a3` |

## 四处实际差分与逐字逆验

本人从真实v1与v2文本独立比较，只有四次插入`U+0020`，各在逗号后、电话号码加粗前；四处分别增加1 byte，总增加4 bytes。完整新页保留四州表格与上下文。

| 原文行 | 旧片段 → 新片段 | 新全文字符插入位置（0起） | 新字节插入位置（0起） | 判定 |
|---|---|---|---|---|
| 115 | `，**800-342-9871**` → `， **800-342-9871**` | 8493 | 17053 | 只补外侧空格 |
| 116 | `，**1-855-567-0252**` → `， **1-855-567-0252**` | 8654 | 17338 | 只补外侧空格 |
| 117 | `，**855-937-2372**` → `， **855-937-2372**` | 8811 | 17565 | 只补外侧空格 |
| 129 | `，**844-538-8766**` → `， **844-538-8766**` | 9679 | 19073 | 只补外侧空格 |

按上述v2准确位置从后向前删去四个空格，逐字节恢复v1的whole及body。又实际按people15 v2 manifest的八项变更顺序，从original完成正向重建v2，再逆序撤回完整八项，精确恢复original的两摘要。manifest offset属于逐步变更后的完整Unicode文本位置，不能同时套到未经变更的original上。

115行仍是NY Connects的咨询号码和原有对象；116行仍是华州Community Living Connections及无薪照顾者支持；117行仍将ADRC与60岁及以上的AAA分支分开；129行仍区分CCLD管的社区非医疗服务和CDPH医疗机构。没有将排版补正变成号码更新、扩大服务区或新增资格。47行的三项Medicare／快速申诉释义和136行的长期照护申诉专员释义，与本人原v1差分审一致，未增加权限或改期限。

实算v1与v2的frontmatter、全部数字序列、所有45个普通链接文字／URL及次序、全部标题、表结构与148行行数不变。canonical当前仍逐字节等于original；新拟稿没有安装。数字与链接相同只是机器辅助，结论同时基于本人完整新页和四处真实上下文阅读。

## 已签其他页、实际来源和失败边界

本人独立从原people15 manifest及真实文件重算其他14页的original whole、proposed body／whole，与其原已签v1和v2 manifest一致；仅机器检查摘要，本轮没有重新全文阅读那14页。又逐件比较规范35件旧／新manifest和真实proposed body／whole，其他34件原记录及拟稿字节不变。它们仍由既有first20／people15事实记录承载，不被本补充重签为新全文事实审。

本轮没有新增外部网页请求或号码回源，也没有把作者的请求状态、旧来源200或旧PDF记录当作本轮已读。原people15 FACT中本人31不同一级URL的采用段、PDF选页、版本和真实失败原样保留；本补充不扩大为全部照护现行法律／全部旧事实再核。旧四项释义的本人实际来源与此前采用边界仍见冻结`ops/reviews/b-pl-people-fact.md`；该155行记录不改，whole SHA `ceb1065ca3aca0ebd244bed01c58aee9343db331b38a04b769b77f43d62079d4`。

初次机器检查的链接regex过宽，将URL闭括号后同一行的号码／文字误抓入URL，造成链接不等的断言失败；当时未产生PASS。本人逐项定位后限定实际链接边界，匹配数与原文`](`标记逐项对应，再完整执行上述正／逆验及45链接比对全部通过。这是检查脚本误判，未改输入文件或掩盖正文差异。

## 冻结输入与交接

- `ops/reviews/b-pl-care-spacing-author.md`：SHA `0a2e36746a7270bb1e1457c9dd389d28b05b74d20a1159700a883ec5b819c348`。
- `.cache/b-pl-people-proposals/manifest.json`：SHA `aac3eece66481023289c1286941b20d9aeb33910bc7882cc26c9b1df83b98863`。
- `.cache/b-pl-people-proposals-v2/manifest.json`：SHA `c4307d0a3f5b194620d97d98b8941e200ed1fac4a93124d31619bbedace437ea`。
- `.cache/b-pl-all-proposals-v2.json`：SHA `92d27cea74d526b67096e0c059c0520991d0e08556b59ec94bcf964d332a3602`。
- 本人实际正／逆验、六摘要、四准确位置及其他14／34检查记录：`.cache/b-pl-care-spacing-banking-fact/verification.json`，SHA `b1134611744d1adcf4d1711ff71c15c874a484d744020e13a6169acddbf4f9eb`。

最终结论：v2差分FACT PASS，无待作者事项；只签`body9a5cf557ecbd0ac87bcb7df0831bdac58c0cb324fbef20f5b48c27f769bd3609`及`whole349a5369aaa00545e6aae4ad89307a50f872003d731fb9fcaedba77418ea27a3`。需由root实际接受此新记录，birth_fact再全读v2照护并完成第三门禁。本结论不代第三静态、工程或canonical安装；其他14页仍绑定冻结旧155行FACT。
