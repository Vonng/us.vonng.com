# B04 租赁流程独立事实审

- 审阅人：`/root/health`；作者：`/root/documents`；实际独立查阅：2026-10-13。
- 正文：`content/book/life/housing/rental-process.md`。
- 初审冻结正文 SHA-256：`375e0d1e24757938aa1acfd71d97a51ee3f37c004f82df1925c88d03839ad3f3`，算法为对 UTF-8 `text.split('---', 2)[2]` 求 SHA-256。
- 最终正文 SHA-256：`6d0058fe202a619f99274b6199e7dbe454fe0ce33756ec71bdffaa3686e44438`。
- 当前结论：**PASS，独立事实审通过**。原稿完整，全文回源审查后作者已补维修条件；修订逐句复核通过。没有把未完成稿、作者证据或搜索摘要当成通过依据。
- 所有权：只写本审阅记录；未改作者正文、元数据、地图、证据、公共文件；未构建、未提交。

## 初审问题与修订要求

1. 得州维修表应在健康安全缺陷与七天推定旁明示责任例外：§92.052(b) 的租客、其他合法入住者、家人或访客造成且不属正常磨损的缺陷，以及 §92.054 的保险承保事故损失，不直接适用普通责任或起算规则。§92.056(a) 明确把前两条并入补救条件。作者证据已经知道这些限制，但读者只看正文还看不到；已发作者补充。
2. 华盛顿维修表建议明确“收到上述书面通知后”起算 24 / 72 小时和 10 天；现文已正确区分开始补救与完工，补此短语使起点明确。

## 独立回到原文的结果

下列来源均由本审阅人重新打开正文或以普通 HTTPS 读取，作者查阅不代替本轮。web 获取成功后实际阅读规则段；遇 403 的普通 HTTPS 回退保留 TLS 校验。PDF 在内存用 pypdf 读取，没有保存下载件。

| 独立来源及实际定位 | 对稿核查结果 |
|---|---|
| [DRE：Looking for a Rental Unit](https://www.dre.ca.gov/publications/ResourceGuidebook/gb05_lookingfor.html)，web 实读 Looking / Inspecting before you rent / Rental Application / Other considerations（约 L143–238） | 预算、具体单元检查、修理承诺纳入租约、身份替代文件及加州不询问移民身份与原文相符。稿中把材料表写为准备和询问方案，没有许诺全国必须接受某证明；没有将三倍租金或美国信用分写成全国门槛 |
| [FTC：Rental Listing Scams](https://consumer.ftc.gov/articles/rental-listing-scams)，2026-06 页面，web 全文 | 盗用真实房源、自助看房仍可能诈骗、独立核实管理公司 / 房产记录、指定礼品卡 / 加密货币 / 汇款均有正文支持；稿中区分核实后的合法申请与过早披露，没有复制 FTC 对申请阶段过于概括的一句话 |
| [DRE 2026 Real Estate Law Excerpts](https://www.dre.ca.gov/files/pdf/relaw/2026/excerpts.pdf)，普通 HTTPS 200，PDF 印刷 pp142–143 §1950.1、pp149–150 §1950.6（零基索引141–142、148–149） | 已完整核对 §1950.6(a)–(l)。A/B 是二选一，不能把按序审查程序的被拒者都写成自动退费；A 的并发误收七天返还及申请人自主转其他单元、B 的选定后七天 / 申请后三十天较早者均准确。付费后的信用报告七天交付、收据及未使用款退款支持正文。§1950.1 自愿接受三十天内制作报告、不得访问费 / 筛查费准确。没核定 CPI 美元上限，正文也没编写数额 |
| [NY RPL §238-a](https://www.nysenate.gov/legislation/laws/RPP/238-A)，web 实读完整 §1(a)/(b)、例外及 §3 | 普通处理费禁收、background / credit 合计 actual 或 $20 较低、过去三十天背景或信用报告免核查费、副本加成本凭证正确。co-op 所有者 / 股东及设施例外没有被扩大为所有合作公寓租客 |
| [NY GOL §7-108](https://www.nysenate.gov/legislation/laws/GOB/7-108)，web 实读 §1/1-a 全部及 §4–6 | 标题与范围排除 rent-stabilized 及列明 rent-controlled 等住房，正文限普通非监管住房，十四天未乱扩。一个月押金 / 预付、法定季节性等例外，签约后入住前可要求检查、记录既有缺陷，以及搬离十四天结算均对得上；未将首月正常到期租金混作额外履约押金 |
| [WA RCW 59.18.257](https://app.leg.wa.gov/rcw/default.aspx?cite=59.18.257)，web 实读 §1–4 | 筛查前书面或张贴说明、报告机构及拒绝标准、可重复报告选择、实际成本；若有 adverse action 州法要求书面并列理由。正文在联邦允许口头后紧接州法更高要求，正确 |
| [WA RCW 59.18.260](https://app.leg.wa.gov/rcw/default.aspx?cite=59.18.260)，web 实读 §1–5 | 收押金时书面租约、房况 / 清洁 / 损坏清单、双方签名日期及副本、正常磨损；稿中没有把清单仅写为自愿技巧 |
| [WA RCW 59.18.070](https://app.leg.wa.gov/rcw/default.aspx?cite=59.18.070)，web 实读全文及 reviser note | 原文 after receipt、commence remedial action、失水热电 / 生命危险 24h、冰箱炉灶等 72h、其他10d，超出控制例外及迅速完工。正文不误称完工期限；起算短语已要求补充。2026 关联条款编号重排不改变本段条件，不援用旧编号指导投递 |
| [WA RCW 59.18.280](https://app.leg.wa.gov/rcw/default.aspx?cite=59.18.280)，web 实读 §1–4 | 租赁终止且搬空后30天，弃租另起算；personal delivery 或 first-class 邮寄；statement/docs/refund 和正常磨损正确。没有把邮寄截止写成到达日，未泛用损坏证明到纯欠租扣款 |
| [Texas Property Code Ch92 官方公共法典](https://tcss.legis.texas.gov/resources/PR/htm/PR.92.htm)，普通 HTTPS 200；逐段独立读取 §§92.351–.354、.052–.056、.103–.108 | 申请费 / 申请定金定义、筛选标准打印通知、拒绝且未给标准应退；七天接受通知、电话 / 邮戳、周末假日顺延准确。维修为 ordinary tenant 健康安全、通知时不欠租、可追踪邮件、第二次书面通知和七天反驳推定，须补上述原因例外。押金30天、书面转寄地址前义务暂缓但权利不丧失、欠租且金额无争议的逐项说明例外、邮戳推定均准确。不得自行押金抵最后租金与 .108 相符 |
| [NYC DCWP FARE FAQ](https://www.nyc.gov/site/dca/about/FAQ-Broker-Fees.page)，web 实读 FAQ1–9；last updated 2026-06-02 | 2025-06-11生效、房东代理 / listing agent、禁止强制聘中介、租客自主雇自己中介、逐项披露及投诉材料均准确；稿说“现在新订”保留旧合同义务 FAQ8 边界 |
| [Seattle Ord127497 / CB121254 FullText](https://seattle.legistar.com/LegislationDetail.aspx?FullText=1&GUID=8C1A5166-A0FD-495C-A90A-F04339929D7D&ID=8135103)，web 独立读履历、§§2/3、§18 | 正式 passed、2026-08-18市长签署履历；§18明确§§1–17于2027-07-01生效，§§2/3“after July 1, 2027”新订或续订范围。稿中没有把2026通过当成2026立即施行，未列未审当前Seattle费率 |
| [CFPB：因租客审查报告被拒](https://www.consumerfinance.gov/ask-cfpb/what-should-i-do-if-my-rental-application-is-denied-because-of-a-tenant-screening-report-en-2105/)，web 全文 | 不利决定包括拒租、要求担保、较高押金或租金；通知三种形式、机构资料、免费报告60天、纠错与联系房东支持正文。此页同时明列住房歧视理由及 HUD 举报路径，支持稿中独立分流 |
| [Texas SLL：Leases](https://guides.sll.texas.gov/landlord-tenant-law/leases)，web 实读 Introduction / Changing / Restrictions | 合同可协商、保存签妥全文、法定不可放弃权利不能靠租约消除正确；没有把口头租约说成一概无效，也没复制法规未普遍禁止 / 允许的零散合同规则 |
| [DRE：Dealing with Problems](https://www.dre.ca.gov/publications/ResourceGuidebook/gb09_dealingwith.html)，web 实读 Habitability / tenant responsibilities / Having repairs made / repair-and-deduct / notices / lawsuit段（L142–336） | 书面留存、急事先口头后书面、严重缺陷合理时间、非一律三十天、地方 building / health / housing检查有依据。正文没有给未经条件核查即可扣租的模板，教学漏水邮件只承担报修功能 |
| [NY OAG：Residential tenants’ rights guide](https://ag.ny.gov/publications/residential-tenants-rights-guide)，web 定位实读 Warranty of habitability / Landlord’s duty of repair（L357–390） | 居住适宜性、须知缺陷、随严重程度变化的合理时间与地方住房官员路径支持正文；文章不填暖气温度、铅漆等其他独立待核细则 |
| [NYC HPD：Report a Quality or Safety Issue](https://www.nyc.gov/site/hpd/services-and-information/report-a-maintenance-issue.page)，web 实读 How to file / After filing / inspections | 先找房东、未响应报311、Service Request number、状态与HPD检查；不同违规类别时限不等同首次报修等待，正文正确分开 |
| [Texas AG：Renter’s Rights](https://www.texasattorneygeneral.gov/consumer-protection/home-real-estate-and-travel/renters-rights)，web 实读 Health and Safety / If You Have Problems / Deposit | 作者以更完整原法纠正通俗指南只列certified / registered mail的局限，合理；指南亦写租客造成缺陷例外，支持本审要求在正文显现。无普通扣租保证或“七天必能退租”的误导 |
| [CA Courts：tenant eviction](https://selfhelp.courts.ca.gov/eviction-tenant)，web403后普通 HTTPS200 全文；[NY Courts：Homes & Evictions](https://www.nycourts.gov/help/homes-evictions)，web全文；[WA Courts：Eviction](https://www.courts.wa.gov/self-help/eviction/)，web全文；[Texas SLL：Eviction Process](https://guides.sll.texas.gov/landlord-tenant-law/eviction-process)，web实读 typical steps、notice、answer和summary disposition区别 | 四州入口均真实提供应诉步骤、表件或当地帮助；NY分纽约市 / 市外；CA答辩不可忽略；TX一般可不提交书面答辩但仍须出庭，2026 summary disposition不同。正文仅提示核对本州答辩和出庭，没有把各州压成统一期限，也没误说所有地方必须同样提交答辩 |

## 获取限制与未核范围

- [HUD 举报入口](https://www.hud.gov/reporthousingdiscrimination) 本轮 web、普通 HTTPS 均403；去掉 www、旧 online-complaint 路径亦未稳定读到正文。因此不能在本审中声称独立实读该页。已独立阅读的 CFPB 官方全文明确相同歧视保护理由及 HUD 举报转介；稿中仅引导请求审查，不宣称个案必胜或不适用豁免，故这一获取限制本身不否定该分流事实。
- 没有用作者“Seattle现行网站受阻”的描述冒充本审亲自读到当前市费率；本文只审条例未来边界。没有确认加州2026筛查费CPI精确金额，正文未写，不能以后直接填数而沿用本审。
- 本文范围排除或未展开监管住房细则、住房补助、全部公平住房豁免、just cause、涨租、家暴、完整驱逐应诉、实际房源资格。已读原法不意味着本审批准这些未写的结论。
- 英文漏水片段自然、具体，明确教学虚构，不是法定送达或完整扣租通知模板。站内链接复用已存正文，相关细则不在本稿重复推导。

## 修订复核与收口

2026-10-13，已重新读取作者修订后的两条维修表及法条引用：华盛顿增加收到上述书面通知起算；得州增加租客、合法同住者、家人或访客造成且不属正常磨损的损坏，以及保险承保事故损失的责任 / 起算例外，引用加入 §92.054。与本审独立实际读取的原法相符。逆转这两处文字及新增法条标签后，正文 SHA 严格等于初稿，确认没有混入其他变更。最终 SHA 已重算并绑定，事实审通过。正文任何后续实质变更，须针对变更回源并重绑。2027-07-01 Seattle实施、四州法修订及官方入口迁移是复核触发。通过事实审后仍需主控第三人静态审与构建、渲染验收。
