# B08 手机与家庭网络：独立事实审

当前摘要：**PASS**。2026-10-13，独立参与者 `banking_fact` 已完整读最终正文、实际独立回源并复核作者两处 FTC 引注修订。正文路径 `content/book/life/digital/phone-internet.md`；最终完整正文 SHA-256 `2fec99dbc2e0eeba297f76fd9f4241d25d3f37dc7f7c9d4cc382644f4cd0abe7`（UTF-8 `split('---', 2)[2]`），实际整文件 SHA-256 `6b528875904d08db88191089eca6312d09ed504e185cb937b6c30250baf79bd7`。没有剩余事实修改项，可由 `birth_fact` 进入第三静态；本结论不代替第三静态、主控元数据安装、构建／渲染或正式集成。

## 分派、实读与边界

作者 `root` → 独立事实审 `banking_fact` → 拟第三静态 `birth_fact`，三名不同参与者。本人只写本 review；正文问题返作者，不改正文、作者 map/evidence、共享账本、元数据，不构建、提交、发布或外部联系，不启动／探测 Claude。

本轮实际重读上级／项目 AGENTS、当前 BOOKMAP → TASKS → CHECKPOINT，检查实际 Git，完整读正文及同 slug map/evidence。既有 PROMPT、说人话规则、deep-research researcher 与 PDF 方法继续适用。作者读取记录只作来源定位，不能继承为本人已读。此 review 接手时不存在，没有旧 PASS 可追认。初读正文 SHA 为 `9b6c79e30cc91d7897bd3d605f373bdbb375779f8428c68229cccc76749a05a8`，整文件为 `1f4803033652fba8a1c159066bbf60750903c1d0930142a7d7137a0f1ce211a4`；当时独立回源尚在进行、未 PASS，旧摘要只保留断点历史。

下载前已实际确认 `.cache/evidence/b08-phone-fact/source-index.json`、拟用 `fcc-guide.pdf`、`current-part8.xml` 均命中 `.gitignore:2:.cache/`；后续逐具体写入路径另核忽略。普通 HTTPS 保留 TLS 校验，必要时仅用既有普通 `127.0.0.1:8888` 代理。请求成功不是核验通过，采用段实际开读后另补范围、日期、失败及结论。

## 本轮独立取源与实际阅读

本人新取原件，缓存为 `.cache/evidence/b08-phone-fact/`，没有使用作者缓存作为本人的一级回源。`source-index.json` 记录正文 24 个唯一外链及 5 个必要补充入口，共 29 个入口、47 次直连／普通代理请求（2026-10-13 UTC 06:36:22—06:37:01）。取得文件后另实际打开采用主文；失败的 FCC／FTC HTML 通过网页工具实际开读，不把普通 403 当主文。独立原件校验值列于下文。额外最新日期 API、FTC 普通头请求和 PDF 请求分别保留在自己的忽略索引，不混成原 47 次请求。

下表既记采用内容，也明确只读采用段或全主文、以及未采用内部资料的边界；行号为本轮网页工具或本人缓存文本的位置，不是永久出版页码。日期均来自本人实际看到的主文／元数据，未见页面更新日的资料不推定发布日期。

| 来源 | 本人实际请求、阅读位置和版本 | 采用断言及核验边界 |
|---|---|---|
| [FCC 消费者投诉中心](https://consumercomplaints.fcc.gov/hc/en-us) | 普通直连／8888 均 403；网页工具实际读完整主文 0—91 行，采用 20—28、48—66 行；未见明确页面更新日。 | Phone／Internet 分类包括收费、设备、覆盖、保号和网络可用性；解锁后仅“可能”使用其他网络；File a complaint 与 Tell your story 不同，后者不转交公司或回复。未打开该页全部 fcc.gov 指南，不宣称自己实际递交投诉或保号。 |
| [Apple：解锁 iPhone](https://support.apple.com/en-us/109316) | 普通 HTTPS 200，实际读全主文；缓存 83 行含 **2026-01-22** Published Date。 | 设置→通用→关于本机→Carrier Lock／No SIM restrictions；只有现运营商能解锁，Apple 不能代解。只用于 iPhone 例子，不扩成 Android 界面、统一解锁天数，也未采用抹除手机分支或执行任何设备操作。 |
| [T-Mobile：BYOD](https://www.t-mobile.com/support/devices/not-sold-by-t-mobile/bring-your-own-device-byod-guide) | 直连 403、普通代理 200；实际读全主文 77 行／约 3,977 字符，未见明确更新日。 | 解锁与兼容分开；IMEI checker、频段／VoLTE、No match 找厂家、部分兼容可能影响覆盖和速度。采用公司自有检查方法，不保证海外手机或其他公司设备可用；未输入真实 IMEI 或做套餐购买。 |
| [FCC 国家宽带地图操作](https://help.bdc.fcc.gov/hc/en-us/articles/10467446103579-How-to-Use-the-FCC-s-National-Broadband-Map) | 直连／代理 403；网页工具 111 行，实际读完整采用主文 1—57 行。Updated **2025-05-15 16:59**。 | 地址／无街道地址按城镇州定位，固定服务按提供者上报；移动覆盖为室外／移动中的车内，明确不显示室内。最大广告速度不是实测；建筑点不是每一单元安装保证。未实际查询个人地址、下载全国数据、测速或提交 challenge。 |
| [eCFR：47 CFR part 8，截至 2026-10-08](https://www.ecfr.gov/api/versioner/v1/full/2026-10-08/title-47.xml?part=8) | 普通 HTTPS 200 **真 XML**；本人实际完整读 §8.1(a)—(c)，不是验证码页。另独立请求 2026-10-13 日期返回 404，错误原文明确 latest issue date **2026-10-08**。 | (a)(1) 每个正在出售的独立宽带套餐、售点含网页／门店／电话、门户及残障可及、(a)(4) 英语及美国营销语言。当前 (a)(3)、(5)、(7) 仍存在；未把延期的新 (a) 当生效。XML 标签图像未显示，具体字段另用 2024 指南文字核。普通 eCFR HTML 挑战是作者记录，本人不继承为法条已读，也未操作验证码。 |
| [FCC：2024 标签指南 DA 24-459](https://docs.fcc.gov/public/attachments/DA-24-459A1_Rcd.pdf) | 普通 HTTPS 200，真实 PDF **11 个物理页**；本人实际读物理 **p1—3、p5—7**，p1 为 **2024-05-14**。另实际读元数据 `/CreationDate`、`/ModDate` 均 `D:20250108211439Z`，不是政策发布时间。 | 采用 p5—7 的月费／优惠及期限、附加／一次／退出费、数据额度和典型上下行／延迟。税费可能按位置变化，不能保证广告价就是总价。p4 标签图像、p8—11 未读，不称 11 页全读；以当前 XML 核对，指南不能取代现行规则。 |
| [USAC：About Lifeline](https://www.lifelinesupport.org/about-lifeline/) | 普通 HTTPS 200；网页工具全文 33 行实际读，核心 11—30 行；未见明确更新日。 | 合格家庭最高 **$9.25／月**、合格 Tribal 地区最高 **$34.25／月**；同住共享收入／费用为一户、一份。变化 **30 日**通知，未每月自付服务须每 **30 日**用、随后 **15 日**继续使用通知；被要求续认则 **60 日**。此为联邦维持条款，未套入 CA 州项目续认表的期限。 |
| [USAC：How to Qualify](https://www.lifelinesupport.org/how-to-qualify/) | 普通 HTTPS 200；网页工具全文 67 行实际读，采用 16—55 行含 **2026 年**收入表。 | 收入不超过 **135% FPG** 或本人／家庭成员／子女／受扶养人参加列出的福利；Medicaid、SNAP、SSI、FPHA、Veterans Pension／Survivors Benefit 逐项实读。特殊 Tribal 与犯罪受害者临时分支已看到但不替普通读者统一扩大资格，不复制各户人数金额或保证个案获批。 |
| [USAC：Supporting Documents](https://www.lifelinesupport.org/supporting-documents/) | 普通 HTTPS 200；网页工具 179 行，实际读全部主文 7—175 行，含 **135% of 2026 FPG**。 | 收入／福利函、身份／SSN 末四位／Tribal ID、地址和同址 household worksheet；通知会说明补什么及如何交。收入与福利文件的有效日期条件实际读到但正文只要求按补件通知。未打开附 Guide PDF／Worksheet 原表，不承诺任何无 SSN 人都可用外国护照替代；商业账户和福利核验分开。 |
| [USAC：How to Apply](https://www.lifelinesupport.org/how-to-apply/) | 普通 HTTPS 200；网页工具全文 44 行实际读，核心 8—32 行。 | 网上、参加公司或邮寄；**Oregon／Texas** 转州网站；残障申请协助 **800-234-9473**，可邮寄申请，获资格后仍需找参加公司登记。当前该页没有 CA 一律排除 National Verifier 的说法。没有操作申请／登录，未把残障号码承诺成必有任何语言服务。 |
| [CPUC：California LifeLine Eligibility](https://www.cpuc.ca.gov/consumer-support/financial-assistance-savings-and-discounts/lifeline/california-lifeline-eligibility/) | 直连 DNS 失败，普通代理 200；实际读全主文 122 行／约 11,920 字符，含福利、收入、申请／年度续认和拒绝。收入表实际有效期 **2026-06-01—2027-05-31**。 | 州有自己的福利／收入标准，年度表格按表中 due date、不是统一联邦 60 天。主文一户电话优惠、TTY／DDTP 例外及 SSN 末四位缺失拒绝均读到；正文没有保证任意替代资料必然通过。未采用州电话 $19、补回公式、冻结或拒绝细节为统一商业手机规则。 |
| [CPUC：Home Broadband Pilot](https://www.cpuc.ca.gov/consumer-support/financial-assistance-savings-and-discounts/lifeline/pilots-and-government-partnerships/california-lifeline-home-broadband-pilot-program) | 直连 DNS 失败，普通代理 200；实际读全主文 45 行／约 2,686 字符，无统一消费者起始日。 | 已推出 **三年**试点，宽带最高 **$20**、同公司宽带＋wireline／wireless voice 最高 **$30**。页面最低服务标准／例外和资格转 GO153-A 看到但正文只要核合格套餐。How to Participate 是**服务公司**授权／advice letter，非个人消费者表；不造消费者表或全国统一起日。每月频率另由下方 Program 页直接核实。 |
| [NY DPS：Affordable Broadband Act](https://dps.ny.gov/node/10381) | 普通 HTTPS 200；网页工具 254 行，本人实际读 ABA 完整采用段 **32—57 行**，未见明确页面更新日。 | 服务 **超过 20,000** 客户公司；合格家庭 **$15／月至少 25 Mbps，或 $20／月至少 200 Mbps**；NSLP 免费／减价午餐、SNAP、Medicaid 等所列福利；小 ISP 临时豁免。正文未写所有公司都必须提供两档、不写永久零涨价，也未核某地址供应商／实际套餐；该页其他电力／区号事项不算采用阅读。 |
| [WA UTC：Telephone Assistance Programs](https://www.utc.wa.gov/ur/node/129) | 直连 403，普通代理 200；实际读全主文 17 行／1,149 字符，未见明确更新日。 | **WTAP 2015 年 8 月已结束**，现向联邦 Lifeline，部分无线公司参加，Tribal 按当地公司核。没有把 2022 年新闻的语音金额或旧 WTAP 当 2026 项目，也未核个人 Tribal 资格。 |
| [FCC：ACP 假广告警示](https://consumercomplaints.fcc.gov/hc/en-us/articles/32636130998420-CONSUMER-ADVISORY-FEDERAL-COMMUNICATIONS-COMMISSION-WARNS-CONSUMERS-ABOUT-WEBSITES-ADVERTISING-THE-AFFORDABLE-CONNECTIVITY-PROGRAM) | 直连／代理 403；网页工具全文 31 行实际读，核心 5—8 行；页面未显示明确发布日。 | **ACP 2024-06-01 结束**；虚假招生和取资料风险，给敏感资料后走身份盗用处理。未把 ACP 与 Lifeline／CA 试点混合；附 advisory PDF 未开读，不宣称现可申请 ACP。 |
| [T-Mobile：Transfer Your Phone Number](https://www.t-mobile.com/support/account/transfer-your-phone-number) | 直连 403，普通代理 200；实际读全主文 **305 行／约 12,171 字符**，含 port-in、port-out、个人 TPOP、PAH 权限／保护和故障段，未见明确更新日。 | 旧账户保持 active 到完成、新设备／SIM 准备、号码／账号／账单地址／转号密码、联系人短信语音备份，转后其他线可能仍须取消。个人账户 TPOP 由 **Primary Account Holder** 生成，先解除 Port Out Protection。只是该公司规则；不推广其优惠、免费或全国转号时间，不把设备尾款等同转号本身已免除。 |
| [Xfinity：Returning Your Equipment](https://www.xfinity.com/support/articles/returning-your-equipment) | 普通 HTTPS 200；实际读全主文 160 行／约 4,540 字符，未见明确更新日。 | 断开账户后仍能进 Digital Return Center（需 ID／密码）；门店回执；线上核序列号、UPS 预付标签，保留含 tracking 的上部作收据。按公司具体设备／渠道核对，不把两周显示、配件范围或商店规定扩成所有公司，未实际登录／寄件。 |
| [FTC：停用手机前处理资料](https://consumer.ftc.gov/articles/how-remove-your-personal-information-you-get-rid-your-phone) | 普通直连／代理 403；网页工具全文 39 行实际读，核心 2—28 行，**2022 年 7 月**。 | 备份、移 SIM／SD、抹除以及不保留号码时更新各账户登记号码；认证器可能需重新激活。正文只采用联系／验证衔接、按各手机／账号步骤继续，不给统一擦除流程或恢复保证。 |
| [FTC：Protect Your Phone](https://consumer.ftc.gov/articles/how-protect-your-phone-hackers) | 普通直连／代理 403；网页工具全文 46 行实际读，核心 2—30 行，**2022 年 7 月**。 | 屏幕锁、系统和 app 更新、备份、丢失查找／锁定／擦除功能。没有把这些设置保证成必能找回或绝对安全，也未进入其内链手机设置。 |
| [FTC：2019 SIM-swap 原入口](https://consumer.ftc.gov/consumer-alerts/2019/10/sim-swap-scams-how-protect-yourself) | **本轮未读到原页主文。** 普通直连／代理均 403；普通浏览器 User-Agent 请求均 404；网页工具原 URL 两次、搜索 ref 一次、从 FTC 两步认证原文真实点击一次均超时／400；公开分页 `?page=0` 也不可取。 | 搜索确实返回完整长摘文，但本人没有将其算作实际开读该原页。已用下表两步认证主文及真实官方诈骗应对 PDF 独立核相应行动；原引用访问边界保留，具体补引注建议已返作者。普通请求 404 不推定此文永久撤销／所列建议失效。 |
| [FCC：Filing a Complaint Q&A](https://consumercomplaints.fcc.gov/hc/en-us/articles/205082880-Filing-a-Complaint-Questions-and-Answers?from=button) | 直连／代理 403；网页工具全文 **106 行**实际读，采用 21—39、57—78 行。 | informal 免费、确认和 tracking；FCC 或提供教育材料或转商家，**提供者自收到转交投诉起 30 日书面回复**，并给消费者和 FCC 副本。回复同邮件补件／异议，并非每个投诉都转交或保证退款；正式申诉费用／六个月虽读到但正文未采用。 |
| [CPUC：CAB Complaint FAQs](https://www.cpuc.ca.gov/consumer-support/file-a-complaint/utility-complaint/cab-faqs) | 直连 DNS 失败，普通代理 200；实际读全主文 62 行／8,625 字符（包括未采用能源问题），采用未授权电话费和 Cable／Internet／VoIP 末段；未见明确更新日。 | 未授权电话费争议同时付无争议额；CPUC 通常不管视频和互联网，可向 FCC；VoIP 有有限帮助可向 CAB 陈述。未把电气押款、19 日／15 日等期限、911 或室内电话线路义务套成本文所有无线服务规则。 |
| [NY DPS：Complaint Entrance](https://www3.dps.ny.gov/ocs/itxgate.nsf/) | 普通 HTTPS 200；实际读全主文与表单说明 43 行／1,532 字符，无明确更新日。 | 先找提供者；传统电话等 DPS 范围，**Cellular／Internet／Satellite TV 转 NYAG**，州外长途 FCC；原案补信息／查状态入口确实有。未提交或查案；电气 72 小时紧急停供分支不套手机。 |
| [WA UTC：Telecommunications](https://www.utc.wa.gov/regulated-industries/utilities/telecommunications) | 直连 403，普通代理 200；实际读全主文 38 行／1,205 字符，无明确更新日。 | 州内电话公司的 rates／services；**通常不管 cable、internet、wireless**，正文按服务类型转 FCC／消费合同主题。未用注册公司清单直接推定任何个案法定管辖。 |

## 必要补充一级资料

| 来源 | 本人实际读取范围／版本 | 对当前正文的核验作用与限制 |
|---|---|---|
| [GovInfo：2026-16503 最终规则](https://www.govinfo.gov/content/pkg/FR-2026-08-13/html/2026-16503.htm) | 普通 HTTPS 200；本人实际读主文 **1—72 行**的发布信息／Summary／DATES及 **1090—1235 行** Final Rules 到结尾。**2026-08-13**，91 FR **52251—52261**。未读中间全部政策论证，不称全篇通读。 | DATES 为 **2026-09-14 生效，但指令 3（§8.1(a)）无限期延后、须另公布生效日**；Final Rules 第 2 项改 (b)、第 3 项改 (a)(1)/(2) 并去掉 (3)/(5)/(7)。据此不能把新口头摘要、链接／图标、费汇总、取消 CSV／归档全当已生效。与当前真 XML 逐项一致，本稿没有宣称延期的新 (a) 已生效。 |
| [FCC：Phone Complaint Issues](https://consumercomplaints.fcc.gov/hc/en-us/articles/360001201223-Phone-Form-Descriptions-of-Complaint-Issues) | 直连／代理 403；网页工具全文 **75 行**实际读，核心 4—53 行。 | billing、cramming、equipment／unlocking、number portability、coverage；slamming 只限 wireline，不套 wireless／VoIP。正文只用相应分类，未把单个商家问题预先判违法。 |
| [FCC：Internet Complaint Issues](https://consumercomplaints.fcc.gov/hc/en-us/articles/115002206106-Internet-Form-Descriptions-of-Complaint-Issues) | 直连／代理 403；网页工具全文 **57 行**实际读，核心 4—34 行。 | availability、billing、modem／router、speed／latency 等分类；未用遗留 ACP 入口为已结束项目制造资格。 |
| [CPUC：California LifeLine Program](https://www.cpuc.ca.gov/consumer-support/financial-assistance-savings-and-discounts/lifeline) | 直连 DNS 失败，普通代理 200；本人实际读全主文 **55 行／约 3,850 字符**，Overview、Pilot Update、Contacts 和资源入口。 | 参加电话公司启动州申请；Provider Search 是官方入口，但本人未实际查询公司；试点明确 **$20／月、$30／月**，与 Pilot 页配对。州资格／续认不等同联邦 60 天。没有把服务公司 advice letter 当消费者表或采用任何电话时间／号码作为正文新增事实。 |
| [eCFR 最新日期 API](https://www.ecfr.gov/api/versioner/v1/full/2026-10-13/title-47.xml?part=8) | 初独立直连／代理均 404；后另实际读 160 字节错误原文，记录在 `latest-api-response.json`，UTC **06:39:00**。 | 错误明确 2026-10-13 已超过 Title 47 最新 issue **2026-10-08**。依这个日期独立读到 05.xml 的真实 §8.1，而不是把 404、挑战 HTML 或未生效 Final Rules 当现行规则。 |
| [FTC：Use Two-Factor Authentication](https://consumer.ftc.gov/articles/use-two-factor-authentication-protect-your-accounts) | 网页工具全文 **78 行**实际读，核心 31—63 行，**2022 年 9 月**。 | 明确 SIM-swap 可夺号码收短信验证码，认证器／安全密钥相对短信更安全（若账号可选），敏感账户先开并按本账号设置继续。未把它们承诺成绝对安全；该页实际内链去 2019 SIM 文本仍超时，不能凭此算旧页已读。 |
| [FTC：What To Do if You Were Scammed，官方 PDF](https://consumer.ftc.gov/system/files/consumer_ftc_gov/pdf/What%20to%20do%20is%20you%20were%20scammed_EN.pdf) | 网页工具实际识别为 **application/pdf，2 个物理页**，文字共 105 行；本人实际读到两页文字，采用物理 **p2 的 89—98 行**；日期 **2022 年 10 月**。 | “号码和账户被夺”分支：联系提供者夺回号码，之后改账户密码，核信用卡／银行／其他账户未授权变化并报告。普通直连／代理下载均 403、无本地 PDF／哈希；网页截图尝试仅返回来源标识未返回可视图像，所以只声明 PDF 原文文字实读，不声明像素／图像审完。未采用资金追回电话／金额／法律保证。 |
| [FTC：What To Do if You Were Scammed，当前 HTML](https://consumer.ftc.gov/articles/what-do-if-you-were-scammed) | 网页工具全文 **163 行**实际读，**2026 年 6 月**；采用个人资料／账号部分 91—119 行作交叉比对。 | 当前 HTML 给账号改强密码／开启两步认证及恢复路径；不是原 2019 SIM 页，不能用当前标题代替旧 URL 已读。未把其他付款方式的追回说明套为本稿退款权利；手机专门步骤仍以上述 PDF 的明确分支为准。 |

## 本人原件版本辨认

- 当前 eCFR `05.xml` SHA-256：`f13bad017d852a1fdb6064153b98d98716d5aa3e961d5dd5d700a30a36beb507`。本人新取并实际读，与作者哈希相同只用于辨认，不据此继承阅读。
- DA24-459 `06.pdf` SHA-256：`73370b5511b1f47e28662a18e4ff30dda85542b0c7402a7ac55566fbc8fab8e4`，11 物理页，实际读取范围在上表。
- GovInfo `25.html` 本人实际响应字节 SHA-256：`e137f586117c64f4004170debc2b22a00f1b58e367e02ae7e6790d5b647b3493`。记录本人字节值，未直接抄作者原件哈希；采用 DATES／Final Rules 在本轮原文实际读到。
- FTC 2022 应对 PDF 已由网页工具识别并读到原文；普通下载没有获得 `%PDF` 原件，不编造本地哈希或宣称完成图像阅读。

## 失败、未采用及受阻边界

- 普通消费者 FCC 子站 HTML、地图帮助页多 403，但网页工具实际取得主文，按上表逐项记实际采用范围。没有继承作者 fcc.gov 主域的失败／成功，也没把未打开的内链指南算已读。
- CPUC 四个原入口直连均 DNS 失败，普通 8888 代理成功并实际读主文。WA 两入口本轮直连 403、代理 200，与作者原方法不同，按本人记录。
- FTC 停用前／保护手机两页直连和代理 403，但网页工具主文可读。2019 SIM 原入口截至本断点未读，失败细节与代核一级资料已单列，不靠搜索摘文通过旧页。
- 从本人实际读到的 USAC Apply 点击 `https://www.texaslifeline.org/`，网页工具返回 **403**；没有继续登录、绕过或制造州表格。仅采用已实际读 USAC 的州分流及参加公司协助，不宣称自己核完 Texas 门户、Solix、州金额／资料／自动资格或所有州投诉管辖。
- 作者记录的普通 eCFR 验证码页没有被本人操作或作为法条。本人采用的是公开 API 真 XML 和实际 DATES／Final Rules，依独立错误响应确认版本最新日期。
- 未核具体个人地址、IMEI、账单、套餐报价、余额、个案身份／福利、订约、楼宇进入许可、取消期限、自动扣款结果或投诉结果。正文相应位置要求读者向自己的公司核订单／通知，不给全国一致资格、时限或退款承诺。
- 一般准备、首账核对、安装要求和归还记录属于办事问题清单，不虚构个人办理结果，也不把 Apple／T-Mobile／Xfinity 自家办法推广成全部商家的相同条件。内部链接只作为已有主题继续路径，不代审全部内链内容或以候选合同页当前状态冒称正式集成。

## 返作者的意见及返修前断点（历史）

截至当时，未发现资格、金额、日期、法域或流程方面须改的事实项。联邦 Lifeline 的 30／15／60 日与 CA 州续认已经分开，FCC 30 日从提供者收到转交投诉起算、纽约 >20,000 门槛及两档选择、WA WTAP 结束、得州分流和 ACP 结束均有本人实际一级主文支持。当前标签采用旧 (a) 的处理正确。

本人向作者 `root` 报告 2019 FTC 原页本轮不可独立开读，并提供已实际开读的 FTC 两步认证主文和 2022 真 PDF p2，建议为日常防护／号码被夺后的步骤就近补可读官方引注，不新增事实。root 接返修，表示会独立打开两项后补引注、重算正文 SHA。**该断点当时暂不冻结最终 PASS**；等待作者实际修订后完整读新正文／差异，复核新 SHA。旧正文 `9b6c79e3…` 不预先承载新稿结论，第三静态不可据这个历史断点开始。

## 作者返修后的实际全文与摘要复核

root 独立读取两项 FTC 资料后，在“手机突然不能通话或收短信”段仅作两处引注变化：短信风险／认证器或安全密钥句后补 [FTC 两步认证主文](https://consumer.ftc.gov/articles/use-two-factor-authentication-protect-your-accounts)；该段最终夺回号码、改密码、核金融账户并报告的步骤改引 [FTC 2022 官方 PDF 物理第 2 页](https://consumer.ftc.gov/system/files/consumer_ftc_gov/pdf/What%20to%20do%20is%20you%20were%20scammed_EN.pdf)。两项均是本人此前已实际开读的一级内容，不是继承作者新声明。

本人随后**再次完整读当前全文**，实际读作者 map、evidence 顶部及新增返修链，核对引用确在对应行动旁；正文动作、限定和 frontmatter 未变。原 2019 FTC 入口仍在前段作为历史引注，本审仍不宣称原页已读；该原页本轮的 403／404／超时保留。另保留 2022 PDF 截图未获得像素的边界，核心 SMS 风险及号码恢复已有本人实际读到的官方原文文字依据。运营商 PIN／权限与转出保护另有本人实际读到的 T-Mobile 自家账户说明，正文要求按所选公司自己的设置继续，不承诺统一安全机制或保证恢复。

本人用内存精确逆向比较：移除新增两步认证链接及其后一个空格，将末尾 PDF 引注恢复为原“FTC：号码被夺后的步骤”2019 URL。逆换正文 SHA 精确恢复 `9b6c79e30cc91d7897bd3d605f373bdbb375779f8428c68229cccc76749a05a8`，整文件恢复 `1f4803033652fba8a1c159066bbf60750903c1d0930142a7d7137a0f1ce211a4`。证明只有上述两处引用变化，元数据和其余正文未变；没有写回正文。

当前实际重新计算：正文 SHA-256 **`2fec99dbc2e0eeba297f76fd9f4241d25d3f37dc7f7c9d4cc382644f4cd0abe7`**，整文件 **`6b528875904d08db88191089eca6312d09ed504e185cb937b6c30250baf79bd7`**。旧送审摘要不承载最终 PASS。作者 map/evidence 的旧冻结叙述作为历史保留，顶部及追加记录均指向该新摘要；本审明确只绑定新稿。

## 最终结论

**PASS — 独立事实审通过，绑定当前正文。** 正文采用的具体资格、金额、日期、期限、州分支和操作流程已由本人实际一级资料核验；标签新 (a) 延期、Lifeline 联邦与州续认、纽约 ABA 门槛／价格／例外、WA 项目结束、Texas 仅已核分流、公司办法边界、FCC 30 日起算及 ACP 结束均准确。FTC 核心风险／恢复动作现有本人实读的可读官方引注；未把 2019 不可读原页、搜索摘文或作者记录当成本人的阅读。没有剩余返修项。

作者 `root` → 独立事实审 `banking_fact` → 第三静态 `birth_fact`，三人不同，可以进入第三静态。本人仅写本 review 和忽略研究缓存，未改正文、作者 map/evidence、共享文件或元数据，未构建、提交、发布或外部联系；生产门禁由第三静态和主控另行完成。
