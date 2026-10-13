# B10 四主题集成验收

2026-10-13，root。自住购房、年度报税、心理健康服务、便利申请各自完成异人事实审和第三静态。主控实际完整读取最终正文、地图、作者证据和两份审阅记录，只安装候选frontmatter；隔离生产、两端网页、新增打印页和本地public完整同步均已通过，现正式登记四篇。全书目标继续active。

| content/book/下正文 | 最终完整正文 SHA-256 | 作者 | 独立事实审 | 第三静态 |
|---|---|---|---|---|
| life/housing/buying-home.md | 1232cdbdd91165c3773efb2bc3a29085cd8d589c396085b437842e79b5092671 | banking_fact | root，b10-buying-home-fact.md | static_editor，b10-buying-home-static.md |
| work/tax/filing.md | 6ca184bce421c07a203b09640178a0da16e31bb5fefcb8ce7397b089e571e70a | root | static_editor，b10-filing-fact.md | birth_fact，b10-filing-static.md |
| people/accessibility/mental-health.md | 575c7d19fa70154da8672ea22f9d942a3c48fd89998f6f41ccb047a13a428917 | birth_fact | banking_fact，b11-mental-health-fact.md | root，b11-mental-health-static.md |
| people/accessibility/accommodations.md | 1b028fd251ea4f4878076d3cae67fc7aec940ad7e44d7637c269c4362f24db0c | birth_fact | banking_fact，b09-accommodations-fact.md | root，b09-accommodations-static.md |

正文摘要算法为UTF-8全文 `split('---', 2)[2]`，保留开始换行。每篇三个角色为三名不同参与者。冻结时整文件摘要保留在作者证据及各审阅；安装后整文件分别为购房 `cbc7bb5e8c46f821e8750ce605a0e439c60c991d970d9dcc611df363a10415be`、报税 `0de7a4c402d6ce85555f1543b1297e25bdf1e274e6873e80ef3e85d59ac9a763`、心理 `071e9a4abb0eff8c7b1cf4bb8be584f9ac5ba272d3fecfd6029f54f65bb8852d`、便利 `11cbbe7d03520624d7ede0987bedc05b672a06f886da70f3e5da8696547fae73`。最终正文与事实和第三审阅绑定一致。

购房原123行在第三静态提出LE三日内拒贷／撤回例外后，由原作者唯一补正L39。主控实际重新读取完整123行、map65、evidence135、事实115与第三73；唯一逆换恢复原完整正文及整文件摘要，事实与第三分别重绑最终1232cdbd。主控另正常TLS读取Regulation Z §1026.19相关正文与官方解释479—512行；没有把原事实57＋4源写成本次全部重新请求。

报税最终136行，两canonical链接由原作者修订，逆验原两SHA。主控完整读map31／evidence93、独立事实99及第三47；事实审49次请求的37 HTML采用主文、长页采用段和两PDF采用页范围，与作者48源实读分别记录，不把采用部分写成整PDF通读。便利最终134行，主控完整读map34／evidence95、事实84及本人第三34；TEA multiple students唯一作者补正及独立法规采用段记录保留。心理最终117行，主控完整读map33／evidence93、事实99及本人第三43；本次五源独立正常TLS抽查不冒称全部45源重读。CMS网页与现行45 CFR个别起算差异按原审阅保留，没有自行扩充期限断言。

共享源新增无障碍章导读和购房、心理、便利三事项；更新生活／住房、人生、工作／税务导读，年度报税事项、事项目录、四州及地区总入口、术语和来源说明。首页、模板、屏幕样式、打印样式、过滤代码和OINK没有改动。正式40主题、28有内容章节、5部分、103 HTML；旧36篇整文件及正文摘要均与安装前实算基线逐件相同。

实际Hugo为0.166.0 Extended，OINK 1.2.0固定 `f8f476e660cf053a2645b7b923ae8d08d5448fce`。初次裸环境make check在Hugo后因Python缺bs4失败；没有当作通过。随后实际运行 `PATH="$PWD/.cache/checks-venv/bin:$PATH" make check DESTINATION=.cache/production-review` 全部成功：生产209页面／35静态文件，103 HTML、40正式主题、当时3草稿，零警告／错误；元数据、摘要、三角色、内链／锚点、目录／搜索／打印零错误。草稿继续研究后再次独立运行产物检查，仍103／40／3、零错误。

独有预览127.0.0.1:24141、PID63144，实际完整命令及cwd为本项目 `.cache/production-review` 的Python http.server。主控使用独立无登录headless Chromium，不操作用户浏览器。范围 `ops/reviews/b10-browser-scope.json` 的27路径在1440×1000与390×844共54访问、28检索、8交互，零错误；首页键盘卡、明暗、复制EOB 5072字符、搜索Escape／Enter、非当前侧栏展开和叶子链接均实际执行。新增Loan Estimate／Cash to Close、FBAR／8938、OBHA／谈话治疗、ADA coordinator／reasonable accommodation检索均实际断言命中对应主题。

主控实际目视45幅网页图：四主题两端首屏8幅，五个章／事项入口两端及四州新增入口两端共18幅，全部13张新增手机表，首页两端2幅、检索图3幅、打印网页目录1幅。Loan Estimate截图因浮层动画只显示底页，检索是否命中依据实际自动断言；检索浮层视觉采用真实FBAR桌面／手机图，不把未显示浮层的图当视觉通过。表格截图初次固定页头重叠，随后仅改忽略目录内补充检查脚本的滚动与视口裁切，最终13张表逐张实际目视，表头／行及近引可读、无重叠；没有为截图修改产品。

购房3张两列表、便利4张两列表、心理3张两列表、报税3张表的手机版宽／scroll／父容器均356px，桌面正文770px；无横向溢出。补充报告18入口图／13手机表、零错误。打印网页含74逻辑单元、40范围框、1360外链、零坏锚点；1360不是本批逐源联网核验数量。

最终打印稿 `.cache/render/b10-book-review.pdf` 为219物理页、5,783,545字节。主控将其逐页文本NFKC规范化定位新主题，然后实际目视全部23张包含新四主题的物理页：购房57—62、便利88—93、心理94—98、报税183—188。跨页表重复表头，表行没有拆散，正文、链接及结尾未见裁切或孤立引注。未逐页目视全219页；旧36篇摘要保持原样，B09最终194页打印另存，不以旧图代替本批新页。

最终报告 `.cache/reports/b10-browser.json` 日期 `2026-10-13T12:11:21.744Z`，SHA `bc6bda602c9082acc6cb6a4b0853325b3be7d537802d98e7af146cf4ec954e6a`；补充 `.cache/reports/b10-extra-browser.json` SHA `e8c58375a9d875e5d76507f085d7a250925925c1cacbe3084736b2c3978d41f4`；最终PDF SHA `324952a13d842ca648b579b7a9724fa59734da1d4b72331b8dc5584332d0fb6f`。范围文件SHA `75208af82e5bb2a18ed17802ee810f912784997b9a482f307af5194b5d8064c6`。失败／重叠图与中间成功版本另存忽略目录，未用它们替代最终结果。

具体原件、缓存、截图、打印稿、脚本和生成目录均在下载／生成前实查Git忽略。主控完整阅读同步脚本及实际校验源／目标路径，无顶层或下层符号链接，执行 `PATH="$PWD/.cache/checks-venv/bin:$PATH" make sync`。257文件路径、大小和SHA相同；随后独立比较完整257文件、111目录、368路径，全部类型、大小和文件SHA一致，再核旧36篇双摘要不变。婚姻、退休和住户服务三个当前草稿均无HTML／搜索／打印产物。

完成上述实际门禁后，acceptance四条从candidate改为integrated。只提交明确的完成源与轻记录，其他作者进行中正文、地图／证据和审阅不混入本批。本地提交号以实际Git及后续CHECKPOINT为准，不预写待执行号码。预览PID63144再次实际核完整命令和项目cwd后已关闭，实查24141无监听；未拥有的1317／1318不动。无外部推送、部署、DNS变更或外部联系。
