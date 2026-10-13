# B11 住户服务、婚姻与退休集成验收

2026-10-13，root。三篇完成作者以外的事实审及第三人静态审，主控已实际完整读最终正文、地图、作者证据及两审记录。只安装四项候选frontmatter，隔离构建、桌面／手机、全部新增打印页及本地完整同步通过后，acceptance三项才由candidate改为integrated。全书目标继续active。

| content/book/下正文 | 最终完整正文SHA-256 | 作者／事实审／第三静态 |
|---|---|---|
| life/household/utilities.md | 59d29dec04e22132ab9ec79a8279ab9bb2bc4058e5d28db36a5b74c6e0c5e03c | banking_fact／birth_fact／static_editor；b11-utilities-fact.md、b11-utilities-static.md |
| people/family/marriage-separation.md | 3dca83e2f3ca391bf144a4f6f352086b7577acfbcc58c6152432483d292101d9 | static_editor／root／banking_fact；b10-marriage-separation-fact.md、b10-marriage-separation-static.md |
| people/aging/retirement-medicare.md | 4aa59f4c2edea50131ebea65dfe3457875c5dde0c7db6292147b69f6aa6749d2 | birth_fact／static_editor／root；b11-retirement-medicare-fact.md、b11-retirement-medicare-static.md |

正文摘要以UTF-8全文 `split('---', 2)[2]` 保留前导与结尾换行；三个角色每篇各为不同参与者。安装后整文件：住户服务 `ec608120566cab88280d4ed0f9648ca3d867c9ecc873c695ca9d437e55f15fe7`，婚姻 `95ce11a82c8a7755880678dd8c17f8423a78e10a3cc32514fd2d5fa944375b6b`，退休 `b91cd2db3b8e4566558014e28fc27b349333930d09086ee59237d4575f412dd0`。安装前冻结whole及六份审阅记录SHA，均已从实际文件复算并对照记录。

住户服务最终112行、map78／evidence167／事实89／第三62，主控完整实读。四处唯一作者补正经作者、事实、第三及主控各自逆验恢复旧body／whole；NY家庭特殊保护条件及City Light变化后10工作日通知已改正。City Light七页／206行主文真正成功读取者为birth_fact；作者及第三403边界保留，主控没有承继成功或冒称重新全读该PDF。第三另实读NY两页新原件。本批集成不扩大个人资费、后台申请字段及未读地方条款。

婚姻最终128行、map52／evidence125／事实109／第三65，主控完整实读。原作者唯一修订King County现场帮助一句，主控与第三逆验旧完整两SHA、元数据及94链接顺序。主控事实采用72个一级URL的实际段落及失败／部分阅读界限在事实记录中；第三新增县帮助、共同申请及债务原文抽查分别归属。主控此前“无预约”的概括已纠正为先现场后有限预约，不把主控概括错误写成网站版本变化。

退休最终148行、map29／evidence65／事实102／主控第三25，主控完整实读；唯一SSPA适用者修订的原加粗范围与前导空格经完整逆验恢复旧两SHA。主控另真正打开POMS的适用段及PL119-21 §71201、签署日期；不是整部法律或2027整册通读。作者／事实的2027册采用页及各自访问失败保留原范围，不移作主控阅读。

共享内容更新三章、生活与人生两部分导读，新增住户服务／婚姻／退休三事项，更新抵达、搬家、事项目录、地区总入口与四州、术语及来源说明。18份编辑入口已实际全文读回。术语索引只接已说明的事项。首页、模板、屏幕／打印样式和固定OINK未改。旧40篇整文件、正文与旧40项验收账，安装前后及同步后逐件相同；基线 `.cache/reports/b11-baseline.json` SHA `66c07f59409a0b27185a40769cf604f40eea24156a653c99e726b01737723bbb`。

实际运行 `PATH="$PWD/.cache/checks-venv/bin:$PATH" make check DESTINATION=.cache/production-review`，Hugo 0.166.0 Extended、OINK 1.2.0固定f8f476e660cf053a2645b7b923ae8d08d5448fce。最终生产221页面／35静态文件，109 HTML、43正式主题、3草稿，零警告／错误。最初同批构建时仅2草稿，托育作者随后写出草稿；两次均真实检查未泄漏，没有把草稿计作正式篇。

本批独有预览127.0.0.1:24142、PID47946，完整命令为本项目 `scripts/serve_preview.py --port 24142 --directory .cache/production-review`，cwd实查为本项目。独立无登录headless Chromium的范围 `ops/reviews/b11-browser-scope.json` 共27路径，1440×1000与390×844共54访问、24搜索、8交互零错误。HEFPA／REP、Project Cupid／joint petition、Medigap／工作积分实际命中对应主题；首页键盘卡、明暗、复制EOB5135字符、搜索Escape／Enter、非当前侧栏展开及叶子跳转、打印锚点均实际执行。

初次浏览在手机侧栏失败，报告49932673保留，未算PASS。主控读固定主题的drawer下一帧关闭按钮焦点代码，并新捕获实际focusin／click事件：原步骤六次中四次误按关闭按钮；等菜单焦点与动画完成后六次全部能展开并跳转。仅修改检查脚本等待真实菜单就绪，再完整重跑通过；没有改主题、强制点击或跳过检查。诊断报告完整SHA `de1df416bd48833aee0be7e93b06ca6176905a8a4234ac1074b009f49b66dbb1`。

主控实际目视45幅网页图：三主题两端6幅、八章／事项入口两端16幅、四州新增入口两端8幅、全部7张手机表、首页两端2幅、打印目录1幅、侧栏诊断1幅、检索4幅。两幅主检索图尚在动画中，不作浮层视觉依据；另真正等待动画的HEFPA桌面／Medigap手机两图清晰通过。补充24入口图／7手机表报告零错误，七表宽／scroll／父容器均356px，桌面770px；实际表头、行、近引均可读，无固定页头重叠或页面横向溢出。

打印网页77逻辑单元、43范围框、1583外链、零坏锚点；1583不是本批逐源联网核验数量。最终PDF238物理页、6,094,506字节。主控用NFKC逐页文本定位后，真正目视全部19个新主题物理页：住户69—73、婚姻110—116、退休158—164；另目视改动导读35／63／91／104／151，合计24页。跨页表重复表头且不拆行，正文与近引、结尾未见裁切或孤立引注；未逐页目视全238页。

最终主报告 `.cache/reports/b11-browser.json` 日期2026-10-13T13:52:31.602Z，SHA `598f24ca87d44af06a65b1b1cc87f4ad91fb5f655b1bcecbd7997509bee6b651`；补充 `.cache/reports/b11-extra-browser.json` SHA `a702481c17752b0c36f3c5268db41fc69260176c7a08f970357190dc826fcdba`；PDF `.cache/render/b11-book-review.pdf` SHA `6bec30704998f8047251ae93a74ec085823de49c8ce6477573a4f9e6390d78a5`；范围SHA `80dbe7f558147a377069e239467a81ed79c15a19874f93e18c94fcc1fc00e77a`。失败报告、动画图、诊断及原件保留忽略目录；具体输出生成前逐项实查忽略。

实际完整读同步脚本、复核源与目标所有下层无符号链接，执行make sync，再用独立os.walk／lstat／字节／SHA比较完整269文件、117目录、386路径，全部类型、大小和摘要相同；旧40篇双摘要再次不变。车辆、托育与历史三草稿均无HTML／搜索／打印产物。正式登记后另实跑public站点检查为109／43／3、零错误。只本地提交已完成源和轻记录，进行中的B12作者包不混入。本批预览再次实查完整命令及cwd后已关闭，24142实查无监听；未拥有1317／1318未动，无外部发布或联系。
