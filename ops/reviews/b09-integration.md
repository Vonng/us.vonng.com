# B09 三主题集成验收

2026-10-13，root。起办与停业、成人继续教育、普通公园日行与营地露营完成各自独立事实审及第三静态，主控完整读最终正文、地图／证据和两审记录后，仅安装候选frontmatter。隔离生产、两端网页、实际打印抽查及public同步现已通过，正式登记三篇；无障碍申请仍在独立事实审，不纳入本记录。全书目标继续active。

| content/book/下正文 | 最终完整正文 SHA-256 | 作者 | 独立事实审 | 第三静态 |
|---|---|---|---|---|
| work/business/start-business.md | 3733354f29b41084479b4b99e3cba5f81d15d9ea56841b3ef0f387d59b6529e7 | banking_fact | birth_fact，b09-business-fact.md | root，b09-business-static.md |
| people/education/continuing-education.md | d99c8bc5766a56450668a7a053d39c9a55813cb824bce54fa943081cc7952106 | static_editor | banking_fact，b09-education-fact.md | birth_fact，b09-education-static.md |
| rights/outdoors/outdoor-planning.md | 5e190a7790971ce0d39769e7edf962a19ff04277569e405fcc96f3572a2330ac | root | birth_fact，b09-outdoors-fact.md | static_editor，b09-outdoors-static.md |

正文算法为UTF-8全文 `split('---', 2)[2]`，保留起始换行。每篇作者、事实审、第三静态为三名不同参与者。安装后整文件分别为business `2d6aaf442dc7b13451b724d97eaf5ea639b148e92d089588741ed1a35e33c96f`、education `5fc71898d9c5b1e0dc65ecf82271c66ca8981d0b863f6d02f577cd1fcfe107af`、outdoor `92fbdce39b355c44042e79271726f7b10ce4b2574b222668b141b6bc727c796f`。冻结时整文件摘要仍在各作者证据，不误称安装后文件。最终正文与两审摘要相同。

创业在DE／EIN、短期I-9和得州年化收入补正后，最后仅调整停业结清及关闭银行账户的一句；事实与第三各自新全文145行实读、逆验恢复前版后重绑3733354f。继续教育最终144行，作者49个不同一级URL的采用范围及事实审本人49源实际读取分开记录；birth_fact第三全文及四源新抽查PASS。主控完整读map40／evidence138、事实89／第三37；此前工具截断的证据逐段补足后才安装候选。

户外原2c2b3ded已由birth_fact独立20源实际采用段事实通过。第三提出两句必要删改，由root原作者唯一删除并完整读新95行；事实与第三分别新全文读取、逆验补回两句恢复旧两SHA，再绑定最终5e190a77两审PASS。USFS403、未读PDF、实时关闭与名额、个人费用资格和特殊户外活动的未核范围仍在证据和审阅中。上述源数不等于主控本轮重新联网读取数；本批工程门禁不替代事实审。

主控新增创业、继续学习、户外三章实际导读和三项办理入口，更新对应三部分、事项索引、四州、术语和来源说明。正式36主题、27有内容章节、5部分、95 HTML。首页、共享内容过滤及OINK源没有修改；旧33篇整文件和正文摘要逐件与本批安装前实算基线相同。

实际两次运行 `PATH="$PWD/.cache/checks-venv/bin:$PATH" make check DESTINATION=.cache/production-review`：Hugo 0.166.0 Extended，OINK 1.2.0仍固定 `f8f476e660cf053a2645b7b923ae8d08d5448fce`。生产零警告／错误；95 HTML、36主题、当时2草稿，元数据／摘要／三人角色、内部链接与锚点、搜索和打印检查零错误。购房与无障碍written草稿无产物。过滤代码未改，已通过的隔离过滤fixture不重复执行。

本会话独有预览为127.0.0.1:24140，PID11953实际完整命令核为本项目 `scripts/serve_preview.py --directory .cache/production-review --port 24140`。采用临时无登录独立Chrome profile。范围 `ops/reviews/b09-browser-scope.json` 的25路径在1440×1000和390×844共50访问、24检索、8交互记录，两次均零错误；首页键盘卡、明暗、复制、搜索Escape／Enter、非当前侧栏展开实际执行。最终报告日期 `2026-10-13T10:16:11.694Z`。

三篇的全部5张表两端宽／scroll分别770／356px，没有页面横向溢出。打印69内容单元、36范围元数据、1093外链、零坏锚点；1093不是本轮逐源联网核验数。主控实际看38幅网页图：三篇两端首屏，全部5表两端，三篇两端后段及手机版底部，三章桌面导读，三事项手机全页，四州手机新增入口。元素长截图曾把固定页头叠在表上，另用真实390×844视口补看三张表的开头；不把截图生成自动计为目视。

初次193物理页打印实看13页，发现户外居民年票引注末行单独落到次页。实际浏览器计算样式已有widows／orphans=3，仍发生此处拆行。主控仅把原本最后段的 `break-inside:avoid-page` 扩到Book打印的直接子段落；未动正文、网页屏幕样式或主题依赖。临时194页试排实际看187／188后，修改本项目打印样式，重新生产及完整两端交互，生成最终194页打印稿。

最终PDF实际目视17物理页：57购物标签、70电话四州表与开通、76社区纽约及西雅图继续、83出生材料表；101—107成人教育的范围、海外材料、跨页申请表、联邦及四州资助、注册和退款表、完整受阻收尾；147经营主体表、151四州雇主表、152停业与收尾；187户外范围、188居民票段与四州表、190求助及返回收尾。申请表跨页重复表头，表行没有拆散；居民票引注已和所属段落同页，正文及结尾未见裁切或孤立末行。不是逐页检查194页，也不把初版／试排图代替最终抽查。

最终PDF `.cache/render/b09-book-review.pdf` SHA `a9fe50645bf5fcfaa84e4c37ab10f02d95893f859813f1d5628e158c093a76e6`；最终报告 `.cache/reports/b09-browser.json` SHA `ebccdad2c3c2534c12e17ea76545adbb3ba65428c699840d5f0f7142bbdbe41e`。初版保留为带before-pagination后缀的缓存，最终与试排明确区分。原件、截图、打印稿、报告与依赖的具体下载／生成路径事先核Git忽略；只保存本轻量记录与范围。

实际执行 `PATH="$PWD/.cache/checks-venv/bin:$PATH" make sync`，241文件路径、大小及SHA相同。主控随后独立比较完整241文件、103目录共344路径，类型、大小与所有文件SHA一致；再次核旧33正文和整文件不变，并核两草稿无HTML。acceptance三条由candidate改为integrated；本地提交号以实际Git及CHECKPOINT为准，不写待执行号码。外部推送、部署、DNS和外部联系没有执行。

婚姻作者在本批结束时创建written草稿。主控实际再跑public内容／产物检查，仍95 HTML、36正式主题、3当前草稿零错误，新增婚姻草稿无产物或检索泄漏。没有因新草稿重跑无变动的交互。24140预览PID11953再次实际核完整命令和项目cwd后关闭，实查该端口无监听；原本未拥有1317／1318不动。
