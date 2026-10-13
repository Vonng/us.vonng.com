# B14 学校支持、丧亲办理与职场权益集成验收

2026-10-14，主控root。三主题作者、独立事实审、第三静态审各为三名不同参与者；root真正完整读取最终正文、地图、证据和两审，复算绑定后只安装四个frontmatter字段。实际生产、网页、打印和同步通过后，三条candidate才登记integrated。全书目标仍active，本批是中间成果。

## 最终文件与审阅绑定

正文摘要为原始UTF-8字节`full.split(b'---',2)[2]`，不裁首尾换行。作者冻结稿保存在忽略缓存，候选安装的四字段逆换逐字节恢复作者整文件；正文不变。

| 路径与三人 | 正文SHA-256 | 作者整文件SHA-256 | 安装后整文件SHA-256 |
|---|---|---|---|
| `content/book/people/school/school-support.md`；static_editor→banking_fact事实→birth_fact第三 | `04d5ef6d12845b42122e149d02290671845bb1bfe88244470a1ae31b33c53af2` | `bc4fc553ea183ee391c0eb24bce97d11be502df6b655aea068f329a3b35fa44a` | `61d25f70841824d0a244db43da35e9bcefd7654c383e5649efecff1fa13d3aed` |
| `content/book/people/aging/death-arrangements.md`；banking_fact→birth_fact事实→static_editor第三 | `7f527b505e36cdd4ad519ccae92b745a3e48187f69f1e6f63f6f89b7e2244397` | `0ec2260e03a9485c9f61ef2e735c1faae2348bff9901825c7b7bdde6c6eacbb9` | `1b6cd2383b8a099a468dfde0ad64f370373a4db81d913875e41e879f7a02fb92` |
| `content/book/work/employment/workplace-rights.md`；birth_fact→static_editor事实→banking_fact第三 | `049c4ecee882f7ad65d2d713568d2e2df999c895b37e0f735b44fe56ee0def05` | `0017e303d9ee5eef2694b6b0fb2b8b59973eede2885fc32d531f34364653d488` | `325c2509ab16ecb66e06ce2b94ceab8c61349be0e5ec4a94da7d90c452e17916` |

| 轻量文件 | 行数 | SHA-256 |
|---|---|---|
| `ops/maps/school-support.md` | 42 | `6af170ab75538411c87c86db2c2bc8d2d2b00175e1b5d155d36b51e97b97b42a` |
| `ops/evidence/school-support.md` | 119 | `51edaf2899a3e9f030c45bad7b45ecf98f8e96359638693ebf0d602fd407c50a` |
| `ops/reviews/b14-school-support-fact.md` | 116 | `872b54f99782b9cd9c1ef564db58f2e872e5a2b760fcf58d0e84c5a72e88644b` |
| `ops/reviews/b14-school-support-third.md` | 69 | `65abafa4158d8183e73d955429ae45bb8e1e68e509ae15c6fa3c32deafd7730b` |
| `ops/maps/death-arrangements.md` | 67 | `a795abe665010d3d5e0bb90f52151e68be73670f036d1785506378194c38c2d7` |
| `ops/evidence/death-arrangements.md` | 105 | `e9bb7506ef4c5ef1890f59a0c9d364f6f27dc214fdaaee2cf9dc66b25636d1ed` |
| `ops/reviews/b14-death-arrangements-fact.md` | 126 | `fe779632325807626d4db3c984fa905936fa03371cec10148b990f0b3d30a26c` |
| `ops/reviews/b14-death-arrangements-third.md` | 82 | `ff2561bceca991810297b5f4b25abd497fad1a31e61399abe497469eda33524b` |
| `ops/maps/workplace-rights.md` | 49 | `372f077528f8845c53e0d05ae7375784066421a60a92bdc79e3ff5416383877c` |
| `ops/evidence/workplace-rights.md` | 85 | `468bb40057236c46ce4138e8c80694ea78e7783f8253d6a55c4e38f6a59a189e` |
| `ops/reviews/b14-workplace-rights-fact.md` | 96 | `abe8dc32cb7383554677eedad0236e0a7b59d956536ce79f3a75ff194b638c03` |
| `ops/reviews/b14-workplace-rights-third.md` | 72 | `cc6afc83b1b0d354b14d1a8945d9a44dda653c98315c7ee10d8f3d4a6e7ed9e1` |

root实读三正文133／125／137行及全部上表文件。学校作者只补SPS一年HIB的两类例外、收窄未经独核的CA复议数字；死亡作者只补IFS经办案件限定，证据行号另改一字符；职场作者只补PTO范围和中文术语释义。每次最终正文都由异人事实及第三重新绑定，root逐次逆验；旧待修结论只留历史。

各参与者实际URL、段页、日期、失败和未核边界在对应证据／审阅。学校旧PDF及OCR、SPS504时钟差异、CDE访问差异；死亡CA指南选页、SSA英语选页及CDC运入／CRODA公民限定；职场DOL受阻替代、TDI不同读取轮次和各计划employee定义均保留。root完整读取作者和审阅包不等于root重开各篇所列的全部原始来源，也不替代各审阅人自己的实际回源。

## 公共入口与实际工程

root修改三个章导读，新增丧亲与职场事项；学校事项接上语言、评估、实施、转学和安全处理，求职／失业／照护／退休／代理／搬家继续接对应正文，四州及事项／地区索引接入。入口没有独立复制金额或期限，具体条件由唯一正文承接。

实际Hugo为0.166.0 Extended，OINK提交`f8f476e660cf053a2645b7b923ae8d08d5448fce`。启用本项目`.cache/checks-venv`后实际运行`make check DESTINATION=.cache/production-review`，Hugo零警告，259 Pages／128 HTML／54候选正式主题／2当时草稿，项目检查errors空。没有修改配置、模板或共享样式。

主浏览器33路径×桌面1440及手机390，共66访问、24搜索、8交互，零错误。真实测试首页卡片Enter、复制Markdown5135字符、深浅色、搜索Enter／Escape及展开非当前侧栏后跳转。补充检查36入口、50次实际新正文链接点击、8张新手机表，零错误；全部表桌面宽／scroll为770／770，手机356／356。

主控实际看58幅有效网页图：三主题首屏两端6、三导读两端6、两新事项两端4、四州新增段两端8、八张新手机表8、学校／失业／求职／照护／退休／代理／搬家／事项索引／地区索引手机9、桌面打印预览1、首页两端2、深色两端2及六新搜索词两端12。原IEP两张动画未完成的图另实际看过，但不计有效58；其余未看的原搜索截图不冒称已视觉验收。

新增IEP／欺凌／殡葬／遗属／FMLA／工伤另等待动画完成、定位真实结果项，12次都实际点击到对应正文，零错误；12幅最终搜索图逐张看过。首次补充检查错误把搜索结果当a元素，实际读OINK渲染代码确认其为role=option的div，保留失败JSON后修正自有缓存检查器；未修改产品或降低期待。

## 打印与同步

打印DOM88逻辑内容单元、54范围框、2274外链，零坏内部锚点。最终PDF299物理页。root逐张目视全部18个新正文页：学校182—187、死亡207—212、职场239—244；另看三个改动导读176／194／228和目录2，共22页。文字、引用及表行没有裁切，职场表跨页重复表头；242末的完整引导段在243接工伤争议列表。没有逐页检查全299页或对2274外链做网络批检。

物理页定位初次把目录中的创业标题误作下一章起点，未据错误范围验收；实际提取239—248开头确认下一章为245并修正页图清单。pdftoppm首次调用的1400参数误为整数，尚未生成图；改成字符串后22页生成并逐张读到，不用生成成功代替视觉检查。

实际`make sync`后另独立以lstat检查全部307文件／136目录／443路径，类型、文件大小及SHA完全一致。随后三条candidate才改integrated，实际`check_site.py --public-dir public`通过128 HTML／54正式／3当前草稿、errors空。草稿数量随作者继续写作增加，不进入已验收HTML／搜索／打印。

同步和正式登记前后，旧51主题整文件、正文摘要及acceptance条目逐项与本批实际基线相同。三新主题六摘要再次逐文件重算、四元数据逆验通过。实际预览为本会话独有127.0.0.1:24145／PID69763，结束按完整命令和项目cwd核所有权后仅关闭该进程，实查无监听；既有1317／1318未触碰。

## 原始报告与过程边界

所有下载、依赖、辅助脚本、截图、PDF、报告与生成路径事前逐一核git忽略；这里只提交源文、轻量证据和审阅。最初145路径检查因Git对中文输出加引号导致集合断言失败，改用NUL输入／输出后145路径全部通过，之后才生成。首次普通shell的python3缺bs4使make检查失败，启用既有检查虚拟环境后的真实make完整通过，两次状态不混记。

| 忽略缓存原始文件 | SHA-256 |
|---|---|
| `.cache/b14-browser-report.json` | `00dce07002eb7ae90531cf9efd72029a3130dfcc7c0592442d51230587793c50` |
| `.cache/reports/b14-extra-browser.json` | `02ef0ded7d7f7b9222c23842825004871a3e7a8b228a6b28f6de05bca5189515` |
| `.cache/reports/b14-settled-search.json` | `24e3cb89d8d5b771ddccaf9789ef5df6f73651306d380a3128a55c46dd296ab4` |
| `.cache/b14/render/book-review.pdf` | `0b295bede41f768d2a78835a128daf2252784f20826a5e21337de816d5f1ed50` |
| `.cache/reports/b14-sync-independent.json` | `e6057f5e481a0ce680a9cecadc1cf8f38231cd696847b7f1feefd6f70d0455be` |

本批本地提交采用明确完成文件白名单；B15账户、债务、文书、食品支持与B16进行中作者包不混入。提交结果另据实际Git写恢复账，不在执行前冒称已提交。第一轮金融／经济困难、法律文书、灾害及枪支安全与全书语言、情境验收继续；没有外部推送、发布、DNS或联系。
