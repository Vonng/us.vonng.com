# B06 集成验收

2026-10-13，root。恢复后保留 B01—B05 的22篇正文及审阅记录，四篇 B06 均完成独立事实审、第三人静态审、候选构建和实际渲染后正式集成。旧未完成审阅保留为历史，不追认为通过。

| 正文 | 最终正文 SHA-256 | 原作者／修订者 | 独立事实审 | 第三人静态审 |
|---|---|---|---|---|
| people/family/birth-and-first-weeks.md | bb51e12f0ed73579c4f86064c2b7963c28c323ea64d7cf6425b3df355ae609b8 | health／static_editor | birth_fact，b06-birth-fact.md | root，b06-static.md |
| work/finance/banking-payments.md | 2b42753157ed603aebc8b9a9eb4f5182c930d8410435cb6a8a7822f4219207e5 | documents／static_editor | banking_fact，b06-banking-fact.md | root，b06-static.md |
| work/employment/job-loss-support.md | 160a39b1cdd003a0528be0396f50330ddda787cc1e43b11491f630372bf3f7d7 | civic／birth_fact | root，b06-job-loss-fact.md | static_editor，b06-job-loss-static.md |
| rights/legal/finding-help.md | 98b56bc44fa152f1a3674528a3ee27c87f6fe75d7785e3489918da4f3f9f639d | root | health，b06-legal-fact.md | civic，b06-legal-static.md |

路径均在 content/book/ 下，正文摘要不含 frontmatter。作者、事实审与第三人分别为不同参与者；修订者没有承担同稿独立审。法律稿与两份历史 PASS 的摘要一致，恢复后的只读核对另见 b06-resume-static.md。出生、银行和失业恢复修订均经最终差异复核。详细实读来源、失败读取和未核实边界在各事实审记录，不以缓存存在代替阅读。

新增家庭与法律章导读、迎接孩子与失业事项，更新部分导读、财务和劳动章节、四州地区入口、术语、来源说明及首页卡片。正式内容为26主题、17章、5部分；未写内容仍只在地图。

实际执行 `PATH="$PWD/.cache/checks-venv/bin:$PATH" make check DESTINATION=.cache/production-review`，生产模式零警告，69 HTML、26正式主题、0草稿，内部链接、锚点、元数据、正文摘要、异人审阅、搜索与打印检查零错误。检查依赖装在已确认忽略的本项目虚拟环境，未改全局 Python。打印样式修订后重新执行同一检查通过。

本会话创建的预览使用 127.0.0.1:24137，隔离 Chrome profile。`US_REVIEW_CONFIG=ops/reviews/b06-browser-scope.json` 对1440与390两端各23路径，共46次页面访问、20次搜索、8项交互记录；最终报告时间为2026-10-13T04:34:19.883Z，零错误。实际操作首页键盘卡片、明暗模式、复制、搜索 Escape／Enter 跳转及非当前侧栏展开。打印49内容单元、26范围元数据、637外链、零坏锚点；637不是外链联网核验数量。原始报告保存在忽略的 .cache/reports/b06-browser.json。

root实际查看手机孕期表（含单独定位的得州行）、出生记录表、加保窗口表、银行余额算例、四州失业申诉表及法律费用表；桌面孕期全表、银行电子转账两种期限、法律联系示例，以及家庭／法律章导读和两份事项全页。另查看手机家庭导读、失业事项、得州地区全页和两端首页卡片；手机首页长元素截图带有固定工具栏，追加实际视口截图确认各卡片可读。未发现页面横溢出、文字或表格裁切。

初次129页打印稿在出生主题结尾把半行句子独留下一页，未计为排版通过。实际检查既有 widows／orphans 后，新增仅打印生效的 `.td-book-print-page > p:last-child { break-inside: avoid-page; }`，先用临时 CSS 验证，再写入项目样式、重新生产构建和浏览器回归。最终129页 PDF 的完整文本与已验证临时样式版一致；root实际查看最终第10、25、36、58、61、98、118、124页，覆盖旧批次表格／对话、四州孕期保障、完整收尾段、失业申诉、余额与电子转账、法律费用。文字、表格和引用无裁切；没有逐页目视全部129页。

正式登记后 `make sync` 已核对189路径、文件大小与 SHA-256 一致。全部26篇正文与 acceptance.json 摘要一致，B01—B05 无改稿。public 为本批本地产物；截图、PDF、依赖、缓存与生成目录均忽略。没有外部推送、部署、DNS 变更或联系机构。全书尚未完成，继续 B07 照护、求职入职与合同，再补其余领域和完整行动链。
