# 租房申请、入住、报修及交房：事实链

作者 documents；实际查阅日 2026-10-13。正文 `content/book/life/housing/rental-process.md`，完整 written 草稿、draft true，待独立事实审。本文限定普通住宅租赁，四州具体规则和纽约市办理案例；西雅图只采用实际可核的未来新规边界，不冒写不可打开材料。新稿未自行构建、提交或填写审阅元数据。

冻结正文 SHA-256：`6d0058fe202a619f99274b6199e7dbe454fe0ce33756ec71bdffaa3686e44438`，按 `sha256(text.split('---', 2)[2].encode('utf-8'))` 计算。作者自检已确认中文加粗外侧空格、四个站内链接指向现存主题；这些预检不替代异人事实审或主控构建。

## 实际读取方法与冲突

- web search 用于发现地址，随后必须 open 或普通 HTTPS 取得原文。网页若工具 403，用 urllib + BeautifulSoup 获取同一官方网页正文；PDF 在内存用 pypdf 解析，不下载入版本库。表内每项都实际读到了所列部分。
- 加州 DRE 网页 `gb05_lookingfor.html` 的 screening fee 段把 §1950.6(c)(2)(A)/(B) 两套可选程序连成似乎全部必须满足的清单；并保留“2023 年 12 月 $62.02”历史值。以 DRE **2026 法律汇编原法文本**为准：A 或 B，不把所有被拒者都归为无条件退款。本稿未写未经单独核算的 2026 CPI 金额；写实际费用、物价调整法定上限，并给当前法律依据。筛查费规则与加州押金页分工明确。
- 得州旧 `statutes.capitol.texas.gov/Docs/PR/htm/PR.92.htm`、旧 PDF 和 DocViewer 地址，本次仅返回新的 Angular 应用壳，不能算读法条。检查该站公开前端 `chunk-7GRZWKYH.js` 的 `FileServerPath` 后，使用其实际公共法典资源 `https://tcss.legis.texas.gov/resources/PR/htm/PR.92.htm`，正常 HTTPS 成功读完整相关条款。无认证、绕过或私人接口。正文引用可读的官方资源并保留条款锚点。
- 得州 AG 报修指引只举 certified/registered mail，但现行 §92.056(b)(3) 明含 USPS 或私人投递可追踪的其他邮递方式；正文以原法列足。§92.056(d) 的七天是可反驳推定，绝不是所有维修都可统一等七天。另注意 SLL 押金说明对 itemized list 例外有易误读的概括，本稿按 §92.104(c) 的**欠租且金额无争议**双条件写。
- Seattle `seattle.gov` 普通页面、手册 PDF、first-in-time FAQ 及 Municode 直接正文/API 在 web 和普通 HTTPS 均 403 或空正文，translationrequest 子域 TLS 失败。检索摘要不计实际阅读；未采用其中当前 move-in fee 比率、分期和 first-in-time 具体例外。官方 Legistar `127497` FullText 成功取得，§18 将 §§1—17 生效置于 2027-07-01，§§2/3 明写 after July 1, 2027 新签/续订合同。签署件附件返回 410，未声称读到签章扫描；Legistar 通过状态、市长 2026-08-18 签署的履历实际可读。
- CA Courts 驱逐页 web 403，但普通 HTTPS 获得完整正文；NY 旧 `/courthelp/Homes/evictions.shtml` 404，改用当前 `/help/homes-evictions`，实际读到 NYC/市外分流。WA AG 资源页普通 HTTPS 可读，但含历史疫情和旧金额等杂项，正文改引当前 WA Courts 驱逐入口，不采用旧资金/时段/金额。

## 房源、申请、拒绝与合同

| 来源 | 实读范围、支持断言与限制 |
|---|---|
| [DRE：Looking for a Rental Unit](https://www.dre.ca.gov/publications/ResourceGuidebook/gb05_lookingfor.html) | 看房、费用预算、inspection、维修承诺入合同、租赁申请及身份/收入替代、筛查费与 holding 段。材料举例属于加州指南及通用准备方法，不声称每家房源必须采用同一收入倍数。照片和自行看房仍需核对出租主体。指南筛查费冲突按上文处理。 |
| [FTC：Rental Listing Scams](https://consumer.ftc.gov/articles/rental-listing-scams) | 2026 年 6 月页面全文：盗用真广告、自助看房并非出租授权、独立找物业联系方式/房产记录、礼品卡/加密币/指定汇款、保护个人材料。未照抄“签租约前不用任何信用信息”的过宽简化，正文分清真实申请所需授权与未核实联系人。 |
| [DRE 2026 Real Estate Law Excerpts](https://www.dre.ca.gov/files/pdf/relaw/2026/excerpts.pdf) | 实际 PDF 纸页 149—150（零基 148—149）完整 §1950.6，及前文 §1950.1 可重复报告：筛查成本/CPI、知道或应知无房不能收、A/B 两程序、并发误收例外与七天、另一程序 7/30 较早、收据和未用费用、信用报告七天交付/邮寄/email；可重复报告三十天、房东自愿接受且接受后不得收筛查/访问费。未引用 §1950.7 非住宅规则。 |
| [NY RPL §238-a](https://www.nysenate.gov/legislation/laws/RPP/238-A) | most recent revision 2025-10-17，完整 §1(a)/(b) 及末尾不得合同放弃：普通申请处理费禁收、累计 actual 或 $20 较低、申请人过去 30 天背景或信用报告免核查费、须副本+invoice/receipt。co-op 业主/股东申请和特定照护养老设施例外，不把一切 coop 租客都排除。未采用 late fee/退票费数据。 |
| [WA RCW 59.18.257](https://app.leg.wa.gov/rcw/default.aspx?cite=59.18.257) | 正文完整 §1—4：事先书面/张贴告知筛查项目、拒绝标准、报告机构和免费副本/纠错权、是否接受可重复报告；只有告知后可收实际筛查成本，DIY 不超过本地通常服务成本；不利决定**须书面且说明理由**，包括有条件接受，不受联邦允许口头通知的较低形式标准替代。 |
| [TX Property Code §§92.351—92.354](https://tcss.legis.texas.gov/resources/PR/htm/PR.92.htm#92.351) | 实际完整读 definitions、printed criteria、签收与未签推定、未告标准又拒绝须退 fee/deposit、完整申请七天/无表从定金起、co-applicant、电话及邮戳通知、周末假日顺延。未将申请费、申请定金和租约履约押金混为一项。正文未引用罚金/倍数赔偿，避免展开另一个诉讼页。 |
| [NYC DCWP：FARE FAQ](https://www.nyc.gov/site/dca/about/FAQ-Broker-Fees.page) | 页面更新 2026-06-02，全文 1—9：2025-06-11 生效、房东代理及 listing agent 禁转费用、不许强迫租客聘指定或 dual agent、自愿租客中介仍可付费、逐项披露与 DCWP 投诉。FAQ8 生效前形成合同义务可能例外，正文明确谈“现在新订的租赁”，不反推旧合同。 |
| [Seattle Ord 127497 / CB121254 FullText](https://seattle.legistar.com/LegislationDetail.aspx?FullText=1&GUID=8C1A5166-A0FD-495C-A90A-F04339929D7D&ID=8135103) | 立法状态和历史、§§1—4 收费披露/禁止规定及 §18 生效原文实际读到。只用证明未来时点，不用 2026 通过新闻推断当前已可援引全部条款。核心生效日 2027-07-01，正文保留 after 日期新订/续订范围。 |
| [CFPB：Tenant screening report denial](https://www.consumerfinance.gov/ask-cfpb/what-should-i-do-if-my-rental-application-is-denied-because-of-a-tenant-screening-report-en-2105/) | 实际全文，租房拒绝、担保/提高押金租金、adverse notice 口头/电子/书面、报告机构联系方式、60 天免费副本、纠错及协助入口；正文另外加 WA 书面要求。只写材料及纠错行动，不保证重新出租该单元。 |
| [HUD：Report Housing Discrimination](https://www.hud.gov/reporthousingdiscrimination) | 举报信息与入口、FHA protected classes、适用行为和对象、其他资助项目不同规则。正文只举部分理由并提供请求审查入口，不作个案构成歧视结论，也不把该入口写成普通押金退费机关。 |
| [Texas State Law Library：Leases](https://guides.sll.texas.gov/landlord-tenant-law/leases) | 书面/口头、协商、完整租约副本及不可放弃法律保护；正文使用读合同与保留定稿建议，没有援用副本 3 business days 等额外期限。页面 assistance animals 条款实际看到但未扩写分类细则。 |

## 入住房况、维修与退租

| 来源 | 实读范围、支持断言与限制 |
|---|---|
| [WA RCW 59.18.260](https://app.leg.wa.gov/rcw/default.aspx?cite=59.18.260) | 完整 §1—5：收押金必须书面租约和具体房况/清洁/损坏清单，双方签名日期、租客副本及免费替补一次，不扣正常磨损。正文未引用不提供清单的赔偿数额。 |
| [NY GOL §7-108](https://www.nysenate.gov/legislation/laws/GOB/7-108) | 最近版本 2022-03-04；完整 1/1-a 及 4—6 例外：不适用 7-107 单位及列明 rent control/照护等；一个月押金/预付、季节性和合作公寓业主例外；入住检查、搬离前检查、14 天结算。正文明确普通非租金管制，不把 14 天扩到 rent-stabilized/rent-controlled 全部住房。 |
| [DRE：Dealing with Problems](https://www.dre.ca.gov/publications/ResourceGuidebook/gb09_dealingwith.html) | Habitability、双方维修责任、书面通知/急事电话后书面、reasonable time、repair-and-deduct 条件和风险、联系地方 building/health/housing 检查、诉讼与调解入口。普通 30 天并非紧急缺陷统一等待期；不将工单等同于扣租充分条件。没有扩写该页家暴/止赎等未核时效法条。 |
| [NY AG：Residential Tenants’ Rights Guide](https://ag.ny.gov/publications/residential-tenants-rights-guide) | Warranty of Habitability、合理修理时间、房客造成缺陷边界、地方检查与法院路径，以及押金监管住房/非监管住房区别。具体 20 美元和 14 天同时对上列原法，不仅凭通俗指南概括。 |
| [NYC HPD：Report a Quality or Safety Issue](https://www.nyc.gov/site/hpd/services-and-information/report-a-maintenance-issue.page) | 实际全文：先告房东、311/online/mobile、服务编号追踪、HPD 联系/检查、违规分类时限、法院帮助。正文不列细分类罚期，只提示它们与从首次报修起算不同。 |
| [WA RCW 59.18.070](https://app.leg.wa.gov/rcw/default.aspx?cite=59.18.070) | 完整核心条文：书面 premises/owner if known/defect；commence remedial action 24h/72h/10d，超出控制、承包安排等例外，须尽快完成。重要区别：并非固定完工期限。 |
| [TX §§92.052、92.054、92.056](https://tcss.legis.texas.gov/resources/PR/htm/PR.92.htm#92.052) | 完整原文：ordinary tenant 健康安全；通常付租收件人/地点，通知时不欠租；租客原因/insured casualty 例外；后续书面通知与可追踪邮件替代；receipt，七天 rebuttable presumption，补救分别依 §92.0561/0563。正文没有提供自行扣租计算或保证七天即能离开。 |
| [TX AG：Renter’s Rights](https://www.texasattorneygeneral.gov/consumer-protection/home-real-estate-and-travel/renters-rights) | 实际全文，重点 If You Have Problems：通知、合理时间、第二次通知、法律咨询及押金。按原法补全其邮递例子的范围；未抄宽泛“任何驱逐都要 cause”等独立待核概括。 |
| [WA RCW 59.18.280](https://app.leg.wa.gov/rcw/default.aspx?cite=59.18.280) | 完整核心：租约终止且搬离、弃租另起算、30 天 full specific statement/docs/refund、personal delivery 或 first-class mail、wear notdamage；票据估价工时等证明。正文不把寄出期限写成到达期限，未采用倍数赔偿或主张全部自动没收。 |
| [TX §§92.103—92.107](https://tcss.legis.texas.gov/resources/PR/htm/PR.92.htm#92.103) | .103 三十天/强调预先通知条款；.104 合法扣除/ordinary wear/.104(c) 欠租且数额无争议的说明例外；.1041 规定日邮戳推定；.107 书面转寄地址前义务暂停但权利不丧失。另实读 SLL security-deposit 页作为发现入口，最终例外按法条校正。 |

## 收到通知的分流（不展开驱逐诉讼）

实读 [CA Courts tenant eviction](https://selfhelp.courts.ca.gov/eviction-tenant) 全文（普通 HTTPS 成功，web 403）、[NY Courts Homes & Evictions](https://www.nycourts.gov/help/homes-evictions) 全文、[WA Courts Eviction & Housing Issues](https://www.courts.wa.gov/self-help/eviction/) 全文、[Texas SLL Eviction Process](https://guides.sll.texas.gov/landlord-tenant-law/eviction-process) 通知/起诉/答辩/听审及不同程序部分。入口均有法院步骤、表件或法律援助转介。正文只要求辨认文件类型、保留送达信息、核实答辩/出庭及寻求当地帮助，没有写各州完整期限，也不将投诉视为自动暂停诉讼。得州来源含 2026 summary disposition 专门程序，本稿不将其误推广普通租赁。

## 作者自检范围与未核边界

教学英文片段为明确标注的虚构漏水报修，不是引文或法定通知模板。身份证明/收入材料表是可询问方案，不保证房东必须接受每一类。无 SSN 不填写假号，未在本稿承诺全国无身份限制或特定 ITIN 必可替代筛查。

未核 2026 加州筛查费 CPI 精确美元数、Seattle 当前 first-in-time 和 move-in 数值、纽约不同监管住房完整押金时间、各地涨租/just cause/驱逐抗辩/家暴解约全套、住房补助项目及每家房源规则；正文没有据这些未核内容作判断。加州押金细节复用已正式集成页，不复制或覆盖其审阅。所有公共入口、导读、总账和构建留主控处理。

## 独立事实审修订

2026-10-13：按 health 独立审意见，在维修表补明华盛顿州从收到书面通知起算；得州补明租客、合法同住者、家人或访客造成且非正常磨损的损坏，以及保险承保事故的例外。作者另实读 §92.054 全条，保险事故维修期从房东收到保险赔付起算，不将此例外套作普通七天维修。正文未扩写保险事故解除合同或减租救济。最终正文 SHA-256：`6d0058fe202a619f99274b6199e7dbe454fe0ce33756ec71bdffaa3686e44438`。
