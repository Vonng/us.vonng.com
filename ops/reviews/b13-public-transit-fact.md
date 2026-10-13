# B13 公共交通独立事实审

当前结论：**PASS**。2026-10-14（Asia/Shanghai），独立事实审 birth_fact；作者 root，后续第三静态拟 banking_fact，三名参与者不同。本结论只绑定下面的最终完整正文和作者包，不替代第三静态、候选安装、构建或实际渲染。初审曾为 IN PROGRESS，必要删词与证据定位补记完成后，本人重新完整读最终三件再收口。

## 实际稿件绑定

本人初审实际读取正文1—60／61—120、地图全26行、证据1—41／42—82；作者删词补正后，又实际完整读取 `content/book/life/transport/public-transit.md` 1—60／61—120、`ops/maps/public-transit.md` 全26行、证据1—45／46—90。第三静态反馈原件编码描述后，本人再实际完整读最新 `ops/evidence/public-transit.md` 1—46／47—92，并从最终实际 UTF-8 文件独立复算：

- 正文120行／20739bytes，body SHA-256 `2d29516be45d78fedd5e5ef709f6f5b790c4f7dc570e3d2503bb8cda1b35692c`；whole `5d99b59a9c24dd4b67f013fe44cb4b2d0654d8045aadc00294712fc9c592c409`。body 严格 `full.split('---', 2)[2]`，不 strip。
- 地图26行／4347bytes，SHA `15fed97b03c6bda971a12137641d4a63de35dada1eb3a519fe102a39b9dcecef`。
- 证据92行／24887bytes，SHA `635f87dfab9502b762fb39f8f1a7c2e8a4300dfa3081eff75f3bd36c9001ca72`。
- 实际 frontmatter 为 written／draft true，verified 与 reviewed_by 均空。本人只修改本记录及自己的忽略缓存，不改作者三件、共享文件、候选元数据，不构建／提交／对外联系。

## 本轮独立回源方法

全部新请求和本人的来源阅读均在北京时间2026-10-14；普通批次 UTC 2026-10-13T17:34:19 起，相应本地已10/14。缓存 `.cache/evidence/b13-transit-fact-birth/` 的 fetch.py、source-index.json、sources.json 及 p01—p50 的 raw／txt／json／pdf 共203个具体路径在下载前逐件 `git check-ignore -v`，全部命中 `.gitignore:2:.cache/`；extra.py另先核同一忽略规则。正常 TLS 直接请求、必要正常127.0.0.1:8888，不关闭验证或绕挑战。自动 JSON 的 obtained-only 不代表本人读取。

本文42个不同正文外引均由本人独立新请求，并实际读取有关采用段；普通失败时另独立打开公开网页主文。下表的普通行号是本人 p01—p42 提取件行号，web行号是本人本轮网页工具返回的页面行号；两者不混用。只记录实际读到的范围，余页／余行取得不等于已读。

联邦 §37.123、§37.125、§37.131 与 §27.123 普通 HTTP200 都转到 unblock.federalregister.gov 的31行挑战页，**不采用**。本人独立网页工具实际读到四条主文及版本头；本轮四条页面均显示 up-to-date10/08/2026、Title49 last amended10/05/2026，§27.123本人的新版本与作者此前9/24显示分开，不能冒用为作者刷新。实际核 complete application后21日、appeal process完成后30日、60日可要求资格申诉、拟停服申诉期间暂缓制裁、PCA免费、3/4英里／固定线路时段，以及书面联邦歧视投诉180日及获准延长期限。

MTA普通请求 p02／p16／p20／p30／p35 直接和8888均403；ACCESS NYC p21／p29普通两路径403挑战；FTA p42两路径403。本人另用网页工具独立打开相应采用主文，成功与普通失败分开，不继承作者200。未进私人账户、真实行程／申请或付款后台。

本人普通 TLS 独取 AccessLA 2026英文TXT：p34 raw SHA `86440f1ee19dcb4419aa49230f1272980f1cf9b834863a65a006203352d653b8`。原件实际由本人脚本cp1252严格解码，按splitlines规范为1650行，再将编号提取件保存为UTF-8；此前错记为“UTF-8-sig解码”已按本人真实管道更正，详见末节。已实际读1—40、170—245、465—530、1045—1120及1120—1185；采用1132—1163，特别1153明示 No Show suspension申诉在信件issued后15日，正文L116相符；未读全文或PDF。初审时发现作者原记1045—1115与本人规范行号不一致，发root核编号及必要补读。作者独立查明原件混合CR／CRLF，按LF计数的1103与规范1153为同一句，原规则没有错；其最终证据60、84—90明示计数体系、重新实际读取与旧记录。本人实际读该更正，未将本人读取归给作者。

## 本人实际读取的42个正文来源

| 本人索引／一级URL | 实际读取、采用条件及边界 |
|---|---|
| [p01 Metro线路](https://www.metro.net/riding/schedules/) | 正常直连200，读1—90／374。采用线路和时刻查询入口；没有逐张读时刻PDF或确认个人行程。 |
| [p02 MTA地图](https://www.mta.info/maps) | 普通两路径403；本人web0—58全部读。工作日、深夜、无障碍、各区公交及铁路目录分开；未读每张所链地图。 |
| [p03 King公交](https://kingcounty.gov/en/dept/metro/travel-options/bus) | 直连连接失败、正常8888取得；1—42全文读。查询／提醒／Night Owl入口；未把夏季项目写成10月班次。 |
| [p04 Sound Transit时刻](https://www.soundtransit.org/schedules) | 直连403、正常8888取得；重定向routes-schedules，1—14全文读。只采用运营者时刻入口。 |
| [p05 Houston公交行程](https://www.ridemetro.org/riding-metro/faqs/-in-category/topics/local-bus-trip-planning) | 正常直连200，1—36全文读。工作日／周末、逐站时刻及纸质图；所链PDF时刻未读。 |
| [p06 Metro无障碍](https://www.metro.net/riding/accessibility/) | 正常200，最终accessibility-guide，1—54全文读。电梯状态与故障替代接续；不保证个人当天设备可用。 |
| [p07 TxDOT机构目录](https://www.txdot.gov/discover/texas-transit-agencies.html) | 正常200，实际1—35／935，采用1—17城市／乡村及县目录。2020区域图不作当期班次保证，余目录未全读。 |
| [p08 Metro票价](https://www.metro.net/fares/) | 正常200，1—48全文。当地公交／rail1.75、2小时非往返、日5／滚动7日18；服务范围与现金除外。 |
| [p09 Metro付款](https://www.metro.net/fares/how-to-pay/) | 正常200，1—80全文。TAP通常2、公交现金／轨道TAP或银行感应、转乘及渠道；2027优惠银行卡仅未来。现金售票机另真实读所链p43 PDF。 |
| [p10 Metro封顶](https://www.metro.net/fares/fare-capping/) | 正常200，1—57全文。自然日及首次刷起7日、免费转乘不当付费、LIFE先按免费次数、现金不封顶。 |
| [p11 OMNY票价](https://omny.info/fares) | 直连403、正常8888取得，1—30全文；另本人web0—51全文读。当前单程3、35／67／17.50七日封顶，首次刷起，不用旧12次换算。 |
| [p12 King价格](https://kingcounty.gov/en/dept/metro/fares-and-payment/prices) | 直连失败、正常8888取得，1—164全文。2025-09-01起19—64岁成人3；日／月票与Access等除外，青年固定线路不同。 |
| [p13 Sound Transit票价](https://www.soundtransit.org/ride-with-us/how-to-pay/fares) | 直连403、正常8888取得，1—190／191—377全文。1／2Link3、Sounder按距、T Line另制；当前356—359仅Sounder ON-OFF、Link只ON，旧泛文不采用。银行卡动作又按下方2026 FAQ核。 |
| [p14 Houston票价](https://www.ridemetro.org/fares/all-about-fares) | 正常200，实际1—200、251—405、406—495／705；201—250及496—705未读。采用当地1.25／P&R2—4.50、Day Pass3及2am边界、卡2／虚拟免费、65—69优惠／70+核准免费／残障材料及人工类别、3小时／各人支付；未泛化其未读项目。 |
| [p15 ORCA卡](https://kingcounty.gov/en/dept/metro/fares-and-payment/ways-to-pay/orca-cards) | 直连失败、正常8888取得，1—166全文。零售／机器／客户处／邮购、月票按车资额度及余额补差、各类优惠卡与除外服务；未外推每台机器现金能力。 |
| [p16 Reduced-Fare OMNY](https://www.mta.info/fares-tolls/subway-bus/reduced-fare/omny) | 普通两路径403；本人web0—120全文。实体OMNY／现金、选定支付工具与本人使用、人工支持；22的旧12次不采用。所链PDF未读。 |
| [p17 OMNY操作](https://omny.info/how-omny-works) | 直连403、正常8888取得，1—23全文。绿色GO、同工具转乘；本人加最多3人，只有一次计cap／免费，转乘每人同reader；首次卡交易可能须等银行。 |
| [p18 King感应](https://kingcounty.gov/en/dept/metro/fares-and-payment/ways-to-pay/tap-to-pay) | 直连失败、正常8888取得，1—66全文。成人银行卡、优惠需相应ORCA、2小时信用／更贵补差、每人自己的工具；Access等除外。 |
| [p19 LIFE](https://www.metro.net/fares/life/) | 正常200，最终life-program，1—108全文。公共福利或家庭收入申请、新90日规定16服务、月20乘次或参与机构折扣、纸件／社区／人工2139222378。收入表未标年数字不采用；县居住条件另核主管2025-12-09原文。 |
| [p20 MTA优惠资格](https://www.mta.info/fares-tolls/subway-bus/reduced-fare) | 普通两路径403；本人web0—119全文。65+或规定残障、当地1.50／express与铁路另制、网上新申请暂不可用、现场／邮寄及任意国家有效护照、不同材料；旧12次不采用。残障PDF第5页未读。 |
| [p21 Fair Fares](https://access.nyc.gov/programs/fair-fares/) | 普通两路径403挑战；本人web0—179全文，Last Updated2026-10-13。NYC18—64、不论移民身份、一人年收入23940与其他家庭表、已有支持须核、身份／年龄／住址／收入、ACCESS HRA或办公室311。主管2026表又独立核，不据未来公告推200%FPL。 |
| [p22 ORCA LIFT](https://kingcounty.gov/en/dept/metro/fares-and-payment/reduced-fares/orca-lift) | 直连失败、正常8888取得，1—145／146—281全文。家庭税前收入≤200%FPL、线上／现场／8007565437、各国护照与收入证明、到期重核；旧数字表与旧1040行不采用。 |
| [p23 ORCA参与机构](https://info.myorca.com/contactless/) | 正常200，1—144全文；另本人web0—264全文。银行卡全成人票、2小时、每人工具、优惠仍用ORCA；不是所有交通方式受理。 |
| [p24 Metro乘车](https://www.metro.net/safety-support/rider-guide/) | 正常200，1—120全文。上下车、扶手、辅助需要与安全求助，不把此页当临床指导。 |
| [p25 49CFR37.123](https://www.ecfr.gov/current/title-49/subtitle-A/part-37/subpart-F/section-37.123) | 普通200为挑战，未采用；本人web103—133全部主文及69版本头读。功能资格三类、临时／行程条件、PCA与陪同；年龄／诊断／不便不自动取得。版本10/08、Title49 amended10/05/2026。 |
| [p26 49CFR37.131](https://www.ecfr.gov/current/title-49/subtitle-A/part-37/subpart-F/section-37.131) | 普通挑战；本人web103—156全部主文及69版本头读，首段输出149后未全显示，另重新打开补读至156。3/4英里／时段／辖区、前日预约／前后1小时协商、PCA免费／陪同另价；版本10/08、amended10/05/2026。 |
| [p27 49CFR37.125](https://www.ecfr.gov/current/title-49/subtitle-A/part-37/subpart-F/section-37.125) | 普通挑战；本人web103—132全部主文及69版本头读。完整申请21日、书面理由／可要求60日申诉、流程完成后30日临时服务、No Show不可控／运营者原因不罚及拟停服复核／暂停制裁；版本10/08、amended10/05/2026。 |
| [p28 AccessLA申请](https://accessla.org/riding_access/gaining_eligibility.html) | 本人正常直连200，1—61全文确为主文，不继承作者先前JS壳。先ID8008270829选3，再联系6265321616评估／材料／设备／免费评估接送；评估后21日及通知后60日书面资格申诉。私人ID后台、所链申请PDF未读。 |
| [p29 AAR申请](https://access.nyc.gov/programs/access-a-ride/) | 普通两路径403；本人web0—181全文，Last Updated2026-04-27。功能／医疗评估、移民身份不问、免费评估交通／人工、60日资格申诉；不认初次询问即完整申请。 |
| [p30 AAR联系](https://www.mta.info/accessibility/access-a-ride/contact) | 普通两路径403；本人web0—96全文，Updated2026-04-16。8773372017／其他区域7183934999、先语言再资格4／预约2／当天3全天；没有联系或进入短信／反馈后台。 |
| [p31 King Access](https://kingcounty.gov/en/dept/metro/travel-options/accessible-services/access-transportation) | 直连失败、正常8888取得，1—160／161—329全文。6+功能、医护部分及评估、完整材料21日／60日按决定信申诉、语言格式2062633113、PCA／陪同、1—7日前日17截止／2062055000每日8—17、跨县较早。主页没有只能书面；补查PDF后返作者删该限制。 |
| [p32 METROLift](https://www.ridemetro.org/riding-metro/transit-services/metrolift-paratransit) | 正常200，实际1—75除纯重复外链装饰、324—400、680—760及761—846；首次纯装饰输出截断后重显所有有关文字。医证签字上传或纸件／7132250119／面谈后21日临时、前一日／周五周末周一、人工7132256716工作日8—17／自动7137394690每日5—17／服务区，未读余段或实际后台。 |
| [p33 METROLift资格FAQ](https://www.ridemetro.org/riding-metro/faqs/-in-category/topics/eligibility-metrolift) | 正常200，1—46全文。功能资格、到期前60日续证与拒绝申诉分开，申诉7136524328及信／email／fax。未标起点的30日不推成提出日起，现行法规按完成流程。 |
| [p34 AccessLA2026 TXT](https://accessla.org/sites/default/files/Publications/2026%20Rider%27s%20Guide%20English.txt) | 正常200，Apr1,2026生效、71825bytes，实际所读范围及SHA见上。前日预约8008831295每日6—22／谷区另制／去回程分别、未赴约拟停服从发信15日，与资格60日不同；全1650行和23MB PDF未读。 |
| [p35 AAR预约](https://www.mta.info/accessibility/access-a-ride/book-and-manage-trips) | 普通两路径403；本人web0—51全文。1—2日前、每日7—17／语言后2／不提供当天新订、去回程分别、改程取消重订；没有MY AAR后台。 |
| [p36 AccessLA指南目录](https://accessla.org/riding_access/access_riders_guide.html) | 本人正常200，1—15全文，只是指南目录；实际采用TXT另读，不把目录当指南全读，也不继承作者web的大PDF／TXT失败为本人尝试。 |
| [p37 OMNY支持](https://omny.info/contact) | 直连403、正常8888取得，1—24全文。8777896669全天、不能在普通表填完整卡／账号；未提交。 |
| [p38 Houston付款FAQ](https://www.ridemetro.org/fares/faqs) | 正常200，1—178全文。各人工具、3小时、现金无找零、Day Pass机购立即生效／卡首次使用至次日2am、实体／虚拟卡资金及丢卡关联保护。未进私人账户。 |
| [p39 AccessLA客户服务](https://accessla.org/about_us/contact_us.html) | 正常200，1—90全文。8008270829与ADA协调员、事件／时间／地点／书面回复继续；努力14日不是法定期限，未填字段或外联。 |
| [p40 Houston ADA投诉](https://www.ridemetro.org/about/records-reports/ada-complaint-process) | 正常200，1—38全文。主管公开人工联系；补件须从联系日10工作日回应，免资料不足关闭；确认及调查时间不混成资格决定期限，未提真实投诉。 |
| [p41 49CFR27.123](https://www.ecfr.gov/current/title-49/subtitle-A/part-27/subpart-C/section-27.123) | 普通200挑战；本人web103—113全部主文及69版本头读。书面歧视投诉180日／获准延长例外；本轮本人版本10/08、amended10/05/2026，与作者此前9/24显示明确分开。 |
| [p42 FTA ADA问答](https://www.transit.dot.gov/regulations-and-guidance/civil-rights-ada/frequently-asked-questions) | 普通两路径403；本人web实际107—146、164—246及重开330—367，采用107—125／335—344与352更新2015-08-21。写书面投诉及180日／办公室继续，不推地方投诉自动暂停期限。未全读368行、未打开当前正式投诉表，不继承作者该表timeout为本人尝试。 |

## 本人另实际读取的一级补查

| 真实URL／版本 | 本人实际阅读与用途 |
|---|---|
| [Metro TVM教程PDF](https://cdn.beta.metro.net/wp-content/uploads/2025/07/29160835/25-1433_web_TAP_TVM_tutorials_Buy_Regular_TAP_Card_and_Stored_Value_bg.pdf) | p43正常直连200，原件1793380bytes，SHA `79db0c1de96aca01e4b816de1198484e97750e0c2cc07c67d244b970a054fcda`；2物理页全部实际pypdf读，另本人web两页全部143行读。©2025／25-1433，第2页27—31明确Cash与credit/debit，支持正文48在售票机现金购卡或存值。CFF字体提示不当读取成功，实际字句另web校对；未据旧机器示例推当前其他票价或每台机器能力。 |
| [King Access Ride Guide PDF](https://cdn.kingcounty.gov/-/media/king-county/depts/metro/documents/travel-options/accessible-services/access-ride-guide.pdf?rev=db3ea210b2cf4d7096ac1a813e9a3cdd&hash=4E01317C23493CFA6B2C06F4A602FCF2) | p44正常直连200，原件3927268bytes，SHA `7811e97c33c03d50aa5e13ae14f365522492497df8dffada36ffdf511c37ac77`，68物理页；实际仅物理1、12、13、14、68，非全书。封面Revised May2023；物理14行11—20列发资格信后60日、写信以及email／联系2062633113，听证可现场／书面／电话。与当前主页仅60日及依决定信相互核，不将旧册的票价或纸件路径压过现页。返作者只删“书面”，未向正文补旧册程序。 |
| [LIFE使用指南](https://www.metro.net/fares/life-benefits-guide) | 本人web0—137全页实际读，最终life-program/life-benefits-guide；采用20月乘／其他参与机构票种及说明，未扩写未纳入正文的续核或所有项目互斥细目。 |
| [Sound Transit付款](https://www.soundtransit.org/ride-with-us/how-to-pay) | 本人web0—111全页，27—52当前ORCA Sounder ON-OFF／Link不OFF及银行卡入口。银行卡具体Sounder动作再读下一项。 |
| [ORCA Tap to Pay FAQ](https://support.myorca.com/hc/en-us/articles/43632666090893-Using-Tap-to-Pay-with-ORCA-FAQs) | 本人新web0—182全文，Updated2026-06-11 17:49；61—76明确实体银行卡／手机在Sounder都须前后刷、同一卡及各人自己的工具，Link登车前刷；没有查个人卡号／交易后台。 |
| [OMNY封顶FAQ](https://omny.info/faq/fare-cap) | 本人从公开FAQ目录真正点击，web0—101全文。23—39实体银行卡与同卡手机另累计、各wallet卡另cap；53—56本人加3人但首刷才计cap／免费。70仍写12次，与明确17.50及当前票价主文有旧句冲突，不采用旧次数或算出18。FAQ目录0—46另实读仅定位。 |
| [NYC Fair Fares主管](https://www.nyc.gov/site/fairfares/index.page) | 本人web0—181全文，21—137采用资格／HRA或其他折扣及人工，72明示2026 Income Guidelines一人23940。未用页脚2025改表的适用年，不打开真实筛查／申请。 |
| [TAP LIFE公开申请说明](https://live.taptogo.net/LIFE) | 本人web0—71全文，37—51范围／身份证明及自证说明；未进申请后台。此页58000与Metro未标年表58300不同，均不把未标年数字写正文。 |
| [Metro LIFE县居民原文](https://thesource.metro.net/from-food-lines-to-free-rides-how-the-life-program-stepped-up-for-la-families/) | 本人web0—141实际显示阅读，采用37—43；原文2025-12-09，43明确LA County居民及材料／自证。只用县域范围，不把当时活动、人数或未标年收入当2026现行金额。 |

## 必要补正、最终差异与事实结论

本轮唯一正文修改请求：原88“有60日书面申诉期限”限定了King Access形式；本人当前主页及所链官方指南实际所读支持60日与依决定信继续，但不支持只能书面。已向root原作者交明确来源及最小删词，root自行补读主页后删除“书面”。原body `cee1dc39f757e37d39c2a80d7b519bdc0ed064fc6629ee18ed840eba13b9dce7`／whole `89723b4d5de51920affe797090176317be6da853d197e99854b86c6b1ff31a58`及82行证据 `dc46ce795e2069c36cf809548265edb60edd0317c48a9a9e421eff5627f2e9d1`保留为初审历史，不承载最终PASS。

收到作者冻结后，本人真实再次读完整120行正文、26行地图、90行证据；独立仅将最终唯一“60日申诉期限”插回“60日书面申诉期限”，精确恢复上述旧body与whole。元数据、61外引／42不同URL、5内部链接序列及其余正文没有变；证据的行号体系与真实补读已本人完整读回，不把作者后来读取写成本人新开源，也不把自己的补查写成作者阅读。

全国定义与四地入口能走完地址／日期／回程核对、票价及工具、费用支持、功能资格／完整申请确认、决定／条件／PCA、每次预约及回程、当天受阻、扣费与丢卡、资格申诉、No Show拟停服与ADA投诉。条件明确在改变行动处：21日从完整申请，30日从申诉流程完成，LA未赴约15日从发信、资格60日另制，Houston续证前60日不作拒绝期限，补件10工作日从联系，FTA180日从所称歧视及获准延长。当前2026数及未来2027优惠分开，地方实例不作全州或全县所有地址服务。上述实际采用范围内无待作者必改事实，授予最终正文 **FACT PASS**。

静态附查实际66普通链接、61外引／42不同HTTPS URL、5绝对内链均存在且integrated／draft false；8个H2、4张两列表，正文无一级标题，中文加粗外侧留空白。没有教学虚构数额或伪个人案例需核；未自行构建或把正文draft改为false，第三审仍须独立完成。

未核范围：没有代查个人实时班次／电梯／路线／完整乘车结果、门户账户／实际支付申请、在线表字段或真实提交、所有PDF表件／地图、全国乡村机构和铁路航空长途、个人功能评估／资格或所有设备尺寸；p01／p07／p14／p32／p34／p42余行及p44余63物理页未全读。作者AccessLA web大PDF／TXT及FTA表的失败只作为其记录边界，未冒称本人请求；本人各普通403、连接失败、CAPTCHA与后续成功保留。新功能或个人例外须按真实当次地址、所选支付工具及正式决定确认，研究记录不能替代实际运营或机构决定。

## 第三静态反馈后的本人记录勘误

2026-10-14，banking_fact指出原件有cp1252弯引号。本人独立实际读自己fetch.py、p34.json及p34.raw，并现场严格解码：UTF-8／UTF-8-sig均在position9的0x92失败，cp1252严格成功。脚本的真实路径是UTF-8-sig尝试失败后cp1252 fallback，随后保存编号UTF-8提取件；p34.json原本亦记录fallback。此前97行事实记录SHA `3652c8e9186539958ed83ada1b0b26390dfdfb3244ab87a3324a3f5935575014`错误把保存件编码写成原件解码，此错记透明保留为历史，不再承载当前绑定。

本人实际将原件strict cp1252解码、splitlines编号后再UTF-8编码，逐字节与既存p34.txt完全相同，保存件SHA `197c94ec4f8b261c8a2a54b1edcb9ea755b63ed86b294e7029e654511a057ba2`；又实际读原件规范1—10及1132—1163，15日／发信起点不变。机器比较1650行不等于本人全文语义阅读，实际采用范围仍限上表。作者独立更正自己的证据60并加92，旧90行证据SHA `44967426690f61eaa56206824f041262fd6b67c587f7b937df6fc6c3d70222f8`保留历史；本人真正完整再读其92行，复算新证据SHA并重绑顶部，未继承第三或作者的解码为本人执行。正文、地图、原件和已读提取件字节及全部采用事实均未改变，最终FACT PASS保留在当前完整正文与最新证据包；本事实记录全文再实际读回、新SHA另算交root与第三人。
