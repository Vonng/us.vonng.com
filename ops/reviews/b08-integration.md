# B08 集成验收

2026-10-13，root。手机与家庭网络、日常购物与退货、图书馆与社区服务的独立事实审及第三静态均完成，root实际完整读取最终正文与相应审阅；候选安装、隔离生产、桌面／手机和打印检查已通过，现正式登记。B01—B07的30篇整文件与正文摘要均未变。全书仍active，不以本批替代第一轮核心路径收口。

| content/book/下正文 | 最终完整正文 SHA-256 | 作者 | 独立事实审 | 第三静态 |
|---|---|---|---|---|
| life/digital/phone-internet.md | 2fec99dbc2e0eeba297f76fd9f4241d25d3f37dc7f7c9d4cc382644f4cd0abe7 | root | banking_fact，b08-phone-fact.md | birth_fact，b08-phone-static.md |
| life/household/shopping-returns.md | b8541cd63e9eab39a42b8d26a2a1803e45121cb4affc91c3ab789d1a9355631f | birth_fact | root，b08-shopping-fact.md | static_editor，b08-shopping-static.md |
| life/community/local-support.md | 01cae4dda1ce86d14d2dadf448184cf1415b09c949ad90523f6db6aafead751e | static_editor | birth_fact，b08-community-fact.md | banking_fact，b08-community-static.md |

算法为UTF-8全文 `split('---', 2)[2]`，保留正文起始换行。三稿作者、事实与静态均为三名不同参与者。root只改候选frontmatter，安装后整文件：手机 `be9c82921ce94711936d2d2e48a4366f77988d69988fab3912a168727a9d1658`；购物 `620ecfb6c42b0606f121103b98f9176b6b4eb1b4647304373fdac16754cf4224`；社区 `4e3a56607d278f3b4995d2743936c4a8e8f7041dda0c4c4a14bd7d919138261d`。冻结时作者记录的整文件仍是元数据前版本，不混作现文件摘要。

手机2019 FTC原页受阻后，由root作者实际读2022当前说明和两页PDF、仅换近处引注，独立事实重核后通过。购物的“全额商店额度”与退款§435.1(b)、(d)由原作者修订，root逆验两处差异并实际全文复读，第三静态重新实算。社区NYC优惠类别、SPL现名与Literacy Source当期关闭已由原作者改；独立无法读取的BPL Welcome／设备／正式ESOL细节退地图。作者实际读Languages与事实审403、事实审本人已读Contact等效原页分别保留；第三静态未冒记新回源。最后单处空话删句由原作者完成，事实及第三各自全文复读、逆算旧两SHA后绑定最终01cae4dd。具体采用段、版本、访问失败与未核边界以各独立审阅为准，不能把本批渲染当新事实审。

root新增三个实际章导读与“抵达后安顿”事项，更新生活部分、跨州搬家、事项索引、四州入口、术语及来源说明；导读仅引用已有主题。首页8卡及共享渲染代码没有修改。正式33主题、24有内容章节、5部分；B09创业仍为written草稿，教育、无障碍和户外研究不接入正式导航。

实际执行 `PATH="$PWD/.cache/checks-venv/bin:$PATH" make check DESTINATION=.cache/production-review`，Hugo 0.166.0 Extended；实际 `git -C themes/oink rev-parse HEAD` 仍为固定 `f8f476e660cf053a2645b7b923ae8d08d5448fce`。86 HTML、33主题、1当时草稿；生产零警告，metadata／SHA／三人角色／内部目标与锚点／搜索与打印零错误，创业草稿没有HTML。无共享过滤代码改动，已验收的隔离过滤fixture不重复运行。

本会话创建127.0.0.1:24139预览，PID46399实际命令核为本项目scripts/serve_preview.py及对应目录／端口；无登录独立Chrome profile。实际范围 `ops/reviews/b08-browser-scope.json`，22路径在1440／390两端共44访问、28检索、8交互记录，报告时间 `2026-10-13T08:29:50.074Z`，零错误。首页键盘卡、明暗、复制、搜索Escape／Enter与非当前侧栏展开实际运行。三新主题全部表格两端宽／scroll均770／356px，无页面横溢出；打印63内容单元、33范围元数据、917外链与零坏锚点，917不是本轮逐一联网核验数。

root实际目视三新主题两端首屏，电话四州补助表两端及手机版FCC回复起算，购物四州退货／三列投诉手机表及桌面账单纠错段，社区系统手机表与NYC桌面办理段。另实际看三章桌面导读、抵达事项两端首屏与手机完成段、四州新增入口手机段。额外36幅采集只算上述真正目视的图，不将未看的截图自动视为通过；页面末段即时定位受底部滚动边界限制时，截图仍涵盖完整收尾。

172物理页PDF实际目视55／57／58／59／66／68／70／72／74／76页：购物标签、四州政策、跨页主管表及完整结尾，电话范围与四州补助、投诉与收尾，社区系统、NYC优惠及SPL材料、当前课程与无障碍继续。未见文字裁切、表行拆散或结尾孤行；跨页主管表重复表头。并非逐页目视172页。PDF `.cache/render/b08-book-review.pdf` SHA `79e462b405d6986f14492fbbe976890b0140d3455149af0b3e217eda53d4faaa`；报告 `.cache/reports/b08-browser.json` SHA `410761b52eac7a5a9bf9deb90a2e0511d843b66626da21c347b6149fceda3f62`。原件、截图、PDF和报告均在已确认忽略的缓存，只保存本轻量记录与范围。

正式登记后实际执行 `PATH="$PWD/.cache/checks-venv/bin:$PATH" make sync`，223文件路径、大小和SHA一致。root随后独立比较完整目录：223文件与94目录共317路径，类型、大小和每件SHA相同；旧30主题整文件仍逐件相同。创业草稿没有产物。所有生成目录继续忽略；本地提交另见实际Git，不写待执行提交号。没有外部推送、部署、DNS或联系机构。B09创业已独立事实PASS，root第三静态另续；教育、无障碍、户外与B10购房继续研究。

继续教育作者在渲染期间新增written草稿。root随后实际再运行内容与产物检查，86 HTML、33正式主题、2当前草稿仍零错误，教育和创业均无产物／搜索泄漏。24139预览已再次核PID46399完整命令与参数后关闭，原本未拥有的1317／1318不动。没有因新草稿重跑无改动的全部交互或逐源研究。
