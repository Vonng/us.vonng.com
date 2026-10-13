# B06 法律求助：恢复版本只读静态核对

审阅者：`/root/static_editor`；日期：2026-10-13。作者为历史参与者 `/root`，独立事实审为历史参与者 `/root/health`，已完成的第三人静态审为历史参与者 `/root/civic`。本次没有冒用原审阅者身份，也不替代或重新宣称他们的外部回源。

- 正文：`content/book/rights/legal/finding-help.md`
- 本次实际复算正文 SHA-256：`98b56bc44fa152f1a3674528a3ee27c87f6fe75d7785e3489918da4f3f9f639d`
- 方法：UTF-8 `path.read_text().split('---', 2)[2]`；不含 frontmatter。
- 结论：**PASS，恢复版本只读静态检查通过**。当前正文与既有 health 事实 PASS、civic 第三人静态 PASS 的绑定版本一致；两份历史结论可以按其实际边界沿用。本记录不代表新增独立事实核验、构建、渲染或正式集成。

## 实际读取及版本核对

完整读取上级与项目 `AGENTS.md`、`PROMPT.md`、`ops/HANDOFF-2026-10-13.md`、`ops/BOOKMAP.md`、`ops/TASKS.md`、`ops/CHECKPOINT.md`，并采用 `/Users/vonng/.agents/skills/humanizer/SKILL.md` 中的表达检查方法。

本稿完整读取：

- `content/book/rights/legal/finding-help.md`
- `ops/maps/finding-help.md`
- `ops/evidence/finding-help.md`
- `ops/reviews/b06-legal-fact.md`
- `ops/reviews/b06-legal-static.md`

恢复时 Git 为 `main`，最近保存提交是 `559caf8`；读取时本稿相对工作树和 Git HEAD 没有正文差异。当前 SHA 与交接文件、作者证据和两份最终审阅完全相同。health 文件明确记录两次引文定位修正，以及三处空格修正后从 `cfd22957…c124277` 重绑当前 SHA 的过程；civic 文件明确确认该事实审重绑后收口 PASS。三名原参与者互异，作者没有充任事实审或第三人审。

`ops/maps/finding-help.md` 的“拟 health 独立事实审、civic 第三人静态审”，以及作者证据末尾“待事实审重绑与第三人确认”，仍是较早阶段的文字。实际两份审阅文件已经明确收口；应由主控更新这些当前状态措辞。本次没有覆盖作者记录或原审阅文件，这一记录差异不构成正文或已完成审阅的冲突。

## 静态与编辑检查

- 元数据完整：title、description、page_id、content_kind、scope、status、draft、verified、reviewed_by 均存在；当前仍为 `written / draft: true`，两项审阅字段为空，符合安装候选元数据前的状态。
- 开篇先给出文件、日期与求助需要，紧急和刑事／移民程序在会改变行动的位置分流；没有重复一级标题、工具引用编号或占位正文。
- 全文行动链衔接清楚：原始文件与最近日期→适合的服务→具体人员资格和程序权限→服务范围与费用→双方责任→沟通、争议、更换及原案继续处理。未接案、转介、排队和投诉均没有被写成原案期限自动延后。
- 四州服务表与费用表各为两列；CA 有限代理与费用清单、NY 窗口帮助、TX 费用争议都保留实际案例边界，移民认可组织、个人与 partial/full 代理范围分开表达。未发现与已读事实审结论冲突或未落实的修正。
- 两段示例明确标为教学虚构，虚构文件日期没有被当成可计算的真实期限；有限代理样句没有被冒充通用法律合同。
- 逐项读取 8 处 Markdown 加粗片段并检查内外空格，未发现内部首尾空格或与相邻中文紧贴的标记。
- 两个站内链接均采用绝对路径，实际文件存在：`/book/rights/safety/emergency-help/` 对应 `content/book/rights/safety/emergency-help.md`，`/book/people/language/service-conversations/` 对应 `content/book/people/language/service-conversations.md`。另读取两目标的 frontmatter，均为 `integrated / draft: false`。
- 引文紧随相应断言，页码修正和 EOIR 自然标题已落实；语言中的资格限制、禁止和等待状态提醒有实际防错作用，未发现需要为去除模板话而删掉的必要条件。

## 本次未核边界

本次实际读到的来源是上述本地正文、地图、证据及审阅记录；没有重新打开外部法源、名单、PDF 或查询门户。外部回源的已读／未读边界仍以 health 的历史事实审为准，不能把本次静态检查称为新的全页事实核验。

没有查询具体律师或代表，没有验证读者法律援助资格，没有填写表单、联系机构或登录私人账户。站内目标存在的静态检查不代表浏览器跳转、外部链接可达、移动表格或打印呈现已经通过。

本次只新建此文件，未修改正文、frontmatter、作者地图／证据、历史审阅或共享文件，未构建、渲染、提交。下一步由主控接受准确版本、安装候选元数据，完成本批隔离构建与实际渲染后再登记正式集成。
