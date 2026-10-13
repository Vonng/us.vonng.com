# B07 集成验收

2026-10-13，root。世界、成年亲人照护、求职入职与个人消费合同均完成作者冻结、独立事实审、第三人静态审、主控候选构建及实际渲染，现正式登记。B01—B06的26篇正文摘要未变，全书仍未完成。

| content/book/下正文 | 最终正文 SHA-256 | 作者 | 独立事实审 | 第三人静态审 |
|---|---|---|---|---|
| foundations/world/world-connections.md | 8466c6b243b057c16f914cce3c5bc3381da5c4ac3c469dc4ef0154c77c6b5375 | root | banking_fact，b07-world-fact.md | static_editor，b07-world-static.md |
| people/aging/caregiving-plan.md | 67cbe66df380938966b619fc692145282321bf43696522a0a682788dafc85c1a | birth_fact | banking_fact，b07-caregiving-fact.md | root，b07-static.md |
| work/career/job-search-onboarding.md | f5c8738b3677bb8dca0c3ba73dcdf2d9c01f668360ff18de15ba570c618e42bc | banking_fact | static_editor，b07-career-fact.md | root，b07-static.md |
| rights/contracts/reading-contracts.md | a456a8907378760c2b1736dc3b429457f602340975e1b36a869eb5c6f1031f08 | static_editor | birth_fact，b07-contracts-fact.md | root，b07-static.md |

各稿作者、事实审与第三审为不同参与者；root没有改三名作者正文。世界稿Census调查范围、求职稿SSN与银行资料用途、照护稿TX投诉号码适用对象及加粗空格、合同稿WA旧网页替代，均由相应作者处理并经最终摘要复核。世界事实审原分派两轮容量异常未完成、不计PASS；现役审者实际回源及替代UN当前一级资料，旧1945人数未用于当前结论。所有实际读取、失败入口与未核细则保留各事实审记录，不能将本次静态或联网状态当新一轮全书事实审。

只安装frontmatter后的整文件 SHA-256：世界 `595191ad369254aaa382d4c6b0bc57017563e1634b9e9b0e10d5a4bdd5eec46a`；照护 `88bc9cc0ae8e8f3cccd5ed46e9cba708d56094b64ef3b0e93aaeb2d0a3d6f638`；求职 `2d06153510d94a027c2ccc9ec5420682dcd0b8227c2cc9d89f293622fc5a1eca`；合同 `60a507a7d3b0600c0be833fb69095b3815a0a7ce6bdd6fa548135cf6289450ea`。正文SHA未变；作者证据中的整文件为候选元数据前冻结值。

新增四章实际导读及求职／照护事项，更新四部分导读、四州入口、术语、来源说明和首页8张事项卡。正式内容为30主题、21章、5部分；未写领域仍只在地图，B08草稿不接入正式导航。

实际执行 `PATH="$PWD/.cache/checks-venv/bin:$PATH" make check DESTINATION=.cache/production-review`。Hugo 0.166.0 Extended，OINK实际HEAD仍固定 `f8f476e660cf053a2645b7b923ae8d08d5448fce`。79 HTML、30候选主题、1当时草稿，生产零警告；内部目标／锚点、元数据、正文摘要、三人角色、搜索与打印零错误。电话草稿及空数字章节实际没有HTML，未泄漏。没有改共享渲染代码，B06已通过的隔离过滤fixture不重复运行；新草稿另查实际产物。

本会话创建127.0.0.1:24138的预览，独立无登录Chrome profile。`US_REVIEW_CONFIG=ops/reviews/b07-browser-scope.json`涵盖24路径，两端1440／390共48次页面访问、20检索及8项交互记录，实际报告时间2026-10-13T06:38:16.179Z，零错误。首页键盘卡、明暗切换、复制、搜索Escape／Enter及非当前侧栏展开均实际运行。各新增主题的表格两端分别770／356px，页面无横溢出。打印57内容单元、30范围元数据、787外链与零坏锚点；787不是本轮逐一联网核验数。

root实际查看四新主题两端首屏与范围框、世界机构表两端、照护四州申请手机版与NY／TX支持表及TX限定Intake行、I-9两端表、WA现行和未来招聘分支、合同取消段桌面与WA法院手机行。另看求职／照护导读两端、两份事项手机首屏和两端新首页卡片。补充截图的WA法院选择器首轮文字不匹配，已按实际“华盛顿”重取；一轮州段定位仍在平滑滚动时截图，未计通过，改为即时定位并实际核72px位置再重取。长表元素截图有固定栏时，另以实际视口检查表头与行。没有把这些采集问题记成页面故障或未经目视算通过。

154物理页PDF实际看第10／31／32／95／96／98／103／105／125／148／150页：旧地区算例与州税表，跨页国际机构表及民意分母，四州照护与完整收尾，背景报告、I-9，取消资格与法院／后续收款。未发现文字／表格裁切、表行拆散或新增结尾孤行；并非逐页目视154页。PDF实际SHA `26fdbc9227da2d893481b537622fe35195fa5c3478d4bc3bba9bcf215da889e7`，归档 `.cache/render/b07-book-review.pdf`；报告归档 `.cache/reports/b07-browser.json`，SHA `e363e7f1647d1a3174efed2929221cce6d15cfcef8f4e2f4eb581a5fab67007f`，均事前确认忽略。截图和PDF不入Git。

正式登记后实际执行 `PATH="$PWD/.cache/checks-venv/bin:$PATH" make sync`，209文件路径、大小和SHA一致。root随后独立比较完整两棵目录，209文件与87目录共296路径相同；三篇B08草稿及空章均不在产物中。public为本批本地产物，依赖、原始资料、截图、PDF与生成目录均忽略。没有外部推送、部署、DNS或联系机构。普通研究、后续审阅和本地提交继续，全书目标保持active。
