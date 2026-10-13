# B07 个人消费与服务合同：独立事实审

- 结论：**PASS**，2026-10-13；作者已完成入口修订，本人复核最终全文与实际差异后通过，可交 root 第三人静态审。
- 最终正文 SHA-256：`a456a8907378760c2b1736dc3b429457f602340975e1b36a869eb5c6f1031f08`；整文件 SHA-256：`362c0c1994bf79beccfb6c62593182ccc604cab58dd6015002fa42980e954c41`。
- 核查者：`/root/birth_fact`；作者：`/root/static_editor`；拟第三人静态审：root。三名参与者不同。本人没有参与本稿写作。
- 实际核查日期：2026-10-13；本轮从 05:29 UTC 起独立读取正文和来源。
- 正文：`content/book/rights/contracts/reading-contracts.md`；作者地图、证据分别为 `ops/maps/reading-contracts.md`、`ops/evidence/reading-contracts.md`，三份均完整实际读到。
- 初审正文 SHA-256：`65bab9ce10f82e8bb11a43b4cebc878d0c2041bda789a12f34713b77bee429e4`；整文件 SHA-256：`7b89b8ee4a7e1ec4553a52d6010c35af6be0222f1d9914767ad7deec4e81a18e`。
- 正文摘要算法：UTF-8 文件 `split('---', 2)[2]`，保留分隔线后空行与末尾换行。作者记录只用于定位，下面为本人本轮重新取得并实际读取的资料。

## 初稿逐段对照与返修项（历史，已解决）

签约主体、附件与承诺、总成本、责任与争议条款、签署保存、履行变更、退出及自动扣款、联邦特定销售取消权、具体补救、四州投诉与司法继续路径均逐段对照。两处家具金额、日期和沟通例子明确标为教学虚构；算术 800+120=920、920-200=720 正确，不作为真实交易或法律期限。

核心事实未发现实质冲突，但初稿三处 WA 法院来源入口需要修复。第 139 行法院表中的表格 URL `https://www.courts.wa.gov/forms/?fa=forms.contribute&formID=33`、送达 URL `https://www.courts.wa.gov/newsinfo/resources/?altMenu=smal&fa=newsinfo_jury.display&fileID=notice&folderID=brochure_scc`，以及第 145 行收款 URL（同路径 `fileID=collect`）本轮普通 TLS、正常 `127.0.0.1:8888` 代理均返回 200 后跳 `error.html`；web 直接打开和从官方总页点击也超时。不能把 HTTP 200 或作者过去成功读取视为本人成功打开。

2026-10-13 已向作者与 root 报告上述具体位置。本人从实际可读的 [WA Courts 小额总页](https://www.courts.wa.gov/newsinfo/resources/?altMenu=sma&fa=newsinfo_jury.scc) 找到并读取 [官方小额手册 PDF](https://www.courts.wa.gov/newsinfo/resources/brochure_scc/smallclaims.pdf)，2025-10 更新、共两页。第 1 页解释向法院书记员取得 Notice of Small Claim、所需事实与金额日期、法院填写相应日期、由非原告送达与相应证明；第 2 页明确法院不替当事人收判决款。当时建议只在 WA 表及末段更换这两组入口，以已实际可读的法院 FAQ 查法院、向 clerk 取得表格，并就近引用该手册的送达与收款说明。不增新金额、期限或诉讼细则。初审未登记通过；作者修订及最终复核见末节。

## 本轮独立回源与适用边界

全部日期为本人 2026-10-13 实际取得资料的日期；表内网页行号指本轮 web 提取，未列行号的普通 TLS 资料以原文标题和段落定位。原始大文件仅在已确认忽略的 `.cache/contracts-fact/`，不入 Git。

| 一手来源及本人实际读取范围／版本 | 与正文对应的结论与边界 |
|---|---|
| [eCFR 16 CFR Part 429](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-429)：web 69、115—180 行，§429.0 全部定义及排除、§429.1(a)—(i) 与取消通知范文、§429.2、§429.3 全部原文。页示 Title 16 截至 2026-10-08。 | 当面招揽、卖方营业所以外订立、买方邀请仍可适用；住所至少 25、住所外至少 130 美元，总价含利息与服务费，多份合同合计；教学培训用途例外均相符。第三个工作日午夜，排除周日与联邦假日；紧急情形必须主动联系及独立手写签名日期声明，主动请求修理限必要零件、追加商品另判，房地产／保险／SEC 注册经纪交易商及临时机动车、艺术品展会排除均保持条件。正文列常见例外，不声称穷尽所有信用交易法律。收到有效通知后 10 个工作日退款、返还抵价物与票据、解除担保权益、通知取回，以及住所待取／自愿寄回由卖方承担费用风险都有支持。未把 FTC 简述的 10 days 用作日历日，也未采用 20 日处置商品规则。 |
| [FTC Cooling-Off 消费说明](https://consumer.ftc.gov/articles/buyers-remorse-ftcs-cooling-rule-may-help)：web 8—60 行主文完整，页尾 September 2025。 | 两份取消通知、销售主要语言的合同／收据、卖方名称地址日期、第三个工作日午夜、星期六计入、及时邮戳及认证邮件回执、未获表格可寄取消信、州法可能多给权利均支持正文。精确金额范围、例外和退款期限以已读现行 CFR 约束其简述。 |
| [15 USC 7001，GPO 2024 汇编](https://www.govinfo.gov/content/pkg/USCODE-2024-title15/html/USCODE-2024-title15-chap96-subchapI-sec7001.htm)：web／普通 TLS 成功，实际读本节 (a)—(j) 与附注，尤其 (a)、(b)、(c)、(d)、(e)。另本轮工具检索实际返回 [House prelim 本节全文](https://uscode.house.gov/view.xhtml?req=%28title%3A15+section%3A7001+edition%3Aprelim%29)，页头标法规截至 2026-09-28，实际读到 (a)—(j)，采用段与 GPO 一致；直接打开失败见下。 | 不能仅因电子形式否定州际／对外交易签名和合同效力；依法须保留的记录应准确、可访问、可再现，与正文相符。正文没有声称电子签名使所有条款有效、消费者必须接受电子记录，或任何电子送达都满足法定书面披露；(b)/(c) 限制仍在本人已读范围。未谎称 GPO 2024 为 2026 汇编。 |
| [15 USC 8403，GPO 2024 汇编](https://www.govinfo.gov/content/pkg/USCODE-2024-title15/html/USCODE-2024-title15-chap110-sec8403.htm)：web 6—14 行及普通 TLS 全节三项。另本轮工具检索实际返回 [House prelim 15 USC 8403](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title15-section8403) 全节，标截至 2026-09-28，与已打开 GPO 同文；直接打开失败见下。 | 限通过网络负面选项交易：取得付款信息前清楚醒目告知重要条件、收费前明确知情同意、提供简单停止循环收费机制。正文没有把这三项扩展为所有线下合同、统一按钮或同渠道取消，也未采用已变化的 FTC click-to-cancel 规则。 |
| [FTC 试用与自动续订](https://consumer.ftc.gov/articles/getting-and-out-free-trials-auto-renewals-and-negative-option-subscriptions)：web 7—74 行全文，September 2024。 | 试用结束前取消、价格与折扣期、续订通知、渠道与提交记录、保留沟通及对账、后续收费争议均支持稿内行动建议，不把网站的概括性法律说明外推至所有州所有合同。 |
| [CFPB 撤销银行账户自动扣款](https://www.consumerfinance.gov/ask-cfpb/how-do-i-stop-automatic-payments-from-my-bank-account-en-2023/)：web 20—50 行及普通 TLS 全主文；reviewed 2026-08-28、modified 2026-08-31。 | 联系商家与银行并书面跟进、持续查账，取消扣款不等于合同终止或债务消灭，均相符。stop payment 收费和差错期限未在此稿列数，另由已有银行稿承接。 |
| [FTC 家庭安防签约](https://consumer.ftc.gov/articles/how-avoid-scams-when-you-shop-home-security-system)：本轮 web 检索返回该原页完整主文，实际读取签前安装／监控／维修分包与费用、书面合同包含承诺、冒充原公司时致电核实等完整段落；列表日期 December 2023。该 URL web 打开与普通 TLS 失败，未声称直接打开整页。 | 原公司核实来访销售人员、问实际安装监控维修承办者的限定示例有原文支持。此处采用的是工具返回的完整原页段落，不是链接标题或作者旧缓存；未采用其较简化的冷静期法律描述。 |
| [Texas OAG 修缮签约建议](https://www.texasattorneygeneral.gov/consumer-protection/home-real-estate-and-travel/how-avoid-home-improvement-scams)：普通 TLS 200，完整读签约建议段至承包商 lien 标题前，页面无可见修订日期。 | 空白不签、完整读后签、工作起止与材料费用、口头承诺入书面、变更收费与即时取得副本支持稿内行动建议；未把房屋修缮特别法写成全国普通合同法。 |
| [FTC 贷款联署 FAQ](https://consumer.ftc.gov/articles/cosigning-loan-faqs)：原 URL 打开超时后，普通尾斜杠 URL 经 web 正常重定向成功，实际读 254—310 行全部主文，April 2024。 | 替主借款人承担债务、可能未偿全额及附加费用支持稿内明确的贷款例子。州法可能改变追收顺序、Notice 不等于责任合同、解除需相关方同意亦已读；正文不推定所有服务担保都适用贷款规则。 |
| [加州最高法院 DKN Holdings LLC v. Faerber，S218597](https://www4.courts.ca.gov/opinions/archive/S218597.PDF)：普通 TLS 200 真 PDF；实际用 pypdf 读物理／印刷第 1—5 页。2015-07-13 判决，共 18 页；原件 SHA-256 `111bf194e82a063a7e8c76b0711f5fd5cdf2e3e48e1a772b96bc3bde1a5f9f13`。 | 第 4 页明确共同及分别承担整体义务、每人可被分别追索全损，第 5 页说明相应加州推定。正文将其作为加州判例对术语的解释与风险识别，不声称两人一签全国即自动连带，不采用本案商业租约、诉讼既判力或个案金额。本人未读第 6—18 页，未冒称全文审判例。 |
| [FTC 商家问题与争议解决](https://consumer.ftc.gov/articles/solving-problems-business-returns-refunds-and-other-resolutions)：web 9—52 行主文完整。 | 核退款政策、材料副本与保留原件、找经理升级、记录对话和网页提交、具体补救与自设答复日、政府投诉、调解是促成协议／仲裁员作决定且可能约束，都支持正文。没有给投诉虚构法定延长期或保证退款。 |
| [CFPB 购车合同强制约束性仲裁](https://www.consumerfinance.gov/ask-cfpb/what-is-mandatory-binding-arbitration-in-an-auto-purchase-agreement-en-739/)：普通 TLS 实读完整主文，reviewed 2024-09-24、modified 2024-09-25。 | 以购车条款说明可能替代法院、涉及上诉和集体请求、可在签前提问或要求修改，与正文的可能性及范围一致，不判个别条款必定可执行。 |
| [AAA 当前规则／表格／费用目录](https://www.adr.org/rules-forms-and-fees/consumer/)：web 3—57 行及普通 TLS 对应目录与 FAQ；[AAA 消费仲裁程序](https://www.adr.org/news-and-insights/how-consumer-arbitration-works/)：普通 TLS 全文，并对照 web 21—53 行，October 01, 2026。 | 限 AAA 自己的程序：小额管辖范围内可继续法院、Demand／合同仲裁约定／申请费或减免、材料给商家，均明确支持。没有下载其当前规则、费用表或 Demand PDF，未核具体费额、全部程序、私人条款效力；目录／程序文章足以支持正文实际采用的入口说明。2025 讨论稿等搜索发现未作现行规则采纳。 |
| [CA Courts 合同违约](https://selfhelp.courts.ca.gov/civil-lawsuit/breach-contract)：普通 TLS 实读完整主文及律师讨论事项。 | 双方具体约定、自己履行条件、损失与证据、仲裁／法域／费用条款，与履约记录、变更和带文件求法律帮助一致。没有把该页的加州 4 年／2 年时效或普通民事答辩期限推广到四州。 |
| [CA OAG 消费者保护](https://oag.ca.gov/consumers)：普通 TLS 完整读消费投诉段；[转介表](https://oag.ca.gov/consumers/complaint-referral-table)：完整读电子／家电维修、Contractor 对应行；[商家投诉表](https://oag.ca.gov/contact/consumer-complaint-against-business-or-company)：完整读公开字段、金额日期广告／签约／沟通／补救、机密资料／代理／诉讼及转介说明。 | BHGS、CSLB 转介准确；未受其他机关监管商家向 OAG 投诉用于识别违法与调查，不能提供私人代理；表单材料与去除 SSN／账户号码的提示有支持。没有填写／提交，未采用有冲突的附件大小数字，未认证每种行业监管机关完整管辖。 |
| [NY 投诉分类](https://ag.ny.gov/file-complaint/consumer)：普通 TLS 全主文和实际 href；[消费者欺诈投诉首页](https://formsnym.ag.ny.gov/OAGOnlineSubmissionForm/faces/OAGCFCHome)：公开首页全部原文；[Economic Justice Division](https://ag.ny.gov/about/about-office/economic-justice-division)：消费者欺诈与保护局职能完整段。 | 商品／网购／服务合同类别真实指向表单，跟进真实入口存在；按商家最近办公室、州外商家按本人附近办公室、首页电话，均相符。部门明确调解消费者投诉；未声称保证退款。未点下一步，不认证后续字段、附件或已经成功受理。 |
| [WA AGO 消费投诉](https://www.atg.wa.gov/file-complaint)：普通 TLS 200 主文完整，包括开头管辖、网上／邮寄入口、投诉过程、商家不配合与机关何时起诉。 | 州居民及对 WA 商家投诉可申请非正式解决；向商家转资料求答复、引用编号补件，不能强制调整，不能作私人律师；仍可评估法院路径。正文没有把其商家回复安排写成法定等待或时效中止。 |
| [TX OAG 消费投诉](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint)：普通 TLS 完整读准备、资料、安全／公开性、系统不保存、确认编号、机关后续和 General complaint 分类段。 | 商家名称地址、金额日期合同付款沟通、一次填完、确认邮件编号、编号不等于调查、通常不另联系、投诉供监测及个人另求救济均相符。未采用表单附件数量大小，未进入或提交表。 |
| [CA Courts 要款](https://selfhelp.courts.ca.gov/small-claims/ask-for-money)：普通 TLS 全主文，尤其要求前置、危险／限制令例外、可立即立案与近期截止；[SC-100 填表说明](https://selfhelp.courts.ca.gov/small-claims/start-case/forms/fill-out-forms)：全主文，包括准确被告、原因金额、县理由、本地附表、顾问及提交下一步；[商家名称地址](https://selfhelp.courts.ca.gov/small-claims/before-you-start/find-business-name-address)：全展开主文。 | 与正文加州法院继续步骤相符；商号与实际经营者、县营业名称、州登记、诉讼文件接收代理人支持开头主体核对。没有查询真人／商家，未填写法院表或采用页上特别争议数字；不是对这些内部机构数据库可办理结果的保证。 |
| [NY Courts 小额入口](https://www.nycourts.gov/help/small-claims)：web 26—48 行实际完整主文，TLS 403 后不以挑战页为成功。 | 金钱请求、不能要求对方履行某行为、两类地区指南与具体法院查找，都支持正文。未核地区手册的具体金额／地点公式，正文要求读者进入适当地区查并未列那些结论。 |
| [WA Courts 立案 FAQ](https://info.courts.wa.gov/support/solutions/articles/72000577084-file-a-small-claim-in-washington-state)：普通 TLS 全问答及链接；[小额总页](https://www.courts.wa.gov/newsinfo/resources/?altMenu=sma&fa=newsinfo_jury.scc)：web 9—39 行全部主文与真实 PDF 链接；[官方两页手册](https://www.courts.wa.gov/newsinfo/resources/brochure_scc/smallclaims.pdf)：web 0—220 行两物理页全文，另普通 TLS 200 下载确认真 PDF 与尾页 October 2025 版本。原件 SHA-256 `a2812a5da0b2ff224ebbb94a02c57e87158987a751a0d0f75463823648f5ca19`；[RCW 12.40.040](https://app.leg.wa.gov/rcw/default.aspx?cite=12.40.040)：web 130—140 行完整条文和版本注。 | 州法院 FAQ 提供 district court 与目录；手册第 1 页允许从 clerk 取得 Notice、列事由金额发生时间、法院填日期、非原告送达和证明，第 2 页法院不代收款；精确支持修订建议。原目录表格／送达／收款网页未能独立打开，只在下方记失败，不能以旧作者已读代本人。正文不列小额金额、管辖公式、送达天数或完整执行步骤。 |
| [TX 州法律图书馆立案](https://guides.sll.texas.gov/small-claims/filing-information)：普通 TLS 完整读 venue 县／precinct、商家／DBA／agent、县法院目录、线上 guided interview 原段；[送达](https://guides.sll.texas.gov/small-claims/serving-the-defendant)：完整读 Serving the Citation、合格送达人、送达方式及 Return of Service、替代送达段。两页更新 2026-10-05。 | 向具体 justice court 核县与 precinct、准备实际被告、Texas Small Claims Petition 入口、向 clerk 请求 citation、送达和证明的继续链均支持。未读 Rule 501 全 PDF，未把概述当四州统一规则，也未填写真实诉状。 |

### 访问失败与未核边界

- FTC 安防页直接打开多次 web timeout；普通 TLS 及普通 8888 代理均 403 自动请求拒绝页。本人实际读到了本轮官方原页的工具检索全文中的必要段落，仅据此核实稿内限定示例，不声称直接打开成功或将其冷静期简述用作完整法律。
- FTC 联署页原地址 web timeout／普通 TLS 403，尾斜杠普通 URL 经 web 重定向实际成功；CFR 普通 TLS 则进入 Federal Register 请求访问页，现行完整原文通过 web 正常读取。没有绕过挑战、关闭证书或使用作者旧缓存。
- House prelim §7001／§8403 直接 web／普通 TLS 均为 200 `Page Not Found`，HTML 自述 temporary format；普通官方 CDN 请求超时。GPO 2024 可读全文与本轮工具检索返回的 House 2026-09-28 全文在正文采用段一致，分别记录访问方式与版本，不把检索原文冒称已直接打开 2026 页面。
- WA 旧法院表格、单独 start／notice／collect 网页失败如前。2025-10 官方两页手册已独立实际打开；该手册以外的各个具体表格、法院当地规定和完整执行手续未认证。尝试的 CRLJ 4 PDF web 不可访问，RCW 4.28.080 打开曾只返回菜单范围，不计作已核送达人法条；上述未读规则不承担本文结论。
- FTC 2026 negative option ANPRM 搜索发现／打开超时，未采用其实体规定；AAA 2025 讨论稿、旧规则 PDF 搜索发现亦未当当前规则。正文仅采用实读 ROSCA 法条、FTC 实务建议与 AAA 自己的 2026 程序说明。
- 本轮不认证四州全部自动续约、定金、翻译、服务许可特别法、私人担保或仲裁条款效力、完整诉状／送达／执行、个案时效起算或中止。正文没有把这些未核事项写为全国确定规则。临近法院截止向法律帮助提供完整日期与文件，是合理的编辑行动分流，不是咨询或投诉可代正式提交的承诺。
- PDF 下载前实际 `git check-ignore` 确认 `.cache/contracts-fact/dkn.pdf`、`.cache/contracts-fact/wa-small-claims.pdf` 等具体文件。没有查询真人或公司的数据库记录、联系机构、填写或提交任何表单，没有构建、提交、安装元数据或修改正文／作者证据／共享文件。

## 修订复核与最终结论

2026-10-13，作者 static_editor 报告实际重新读取官方两页手册后完成修订。本人随后完整重读当前 145 行正文并按已独立读到的手册对照：WA 法院表保留可读 FAQ，改为向 clerk 取得 Notice，送达引用第 1 页；末段收款改引第 2 页。两处修订准确，不改变资格、金额、期限、责任或其他规则。

本人对实际当前文件执行反向替换这两个完整位置，恢复所得正文 SHA 恰为初审 `65bab9ce10f82e8bb11a43b4cebc878d0c2041bda789a12f34713b77bee429e4`，整文件 SHA 恰为初审 `7b89b8ee4a7e1ec4553a52d6010c35af6be0222f1d9914767ad7deec4e81a18e`。这证实只有已复核的两处正文变动，frontmatter 及其他内容未改变。实际 YAML 仍为 `written`、`draft: true`、核验与审阅字段空。

最终结论：**PASS**。本稿采用的重要断言和可执行入口已独立核实并逐段对照，返修项已经解决，未发现仍待处理的实质事实错误。源网页直接访问失败、检索取得原文与已打开替代材料的区别，以及未采用／未核范围均保留如上；通过不代表所有个案法律结论、静态审、构建、渲染或集成。

最终绑定正文 SHA-256：`a456a8907378760c2b1736dc3b429457f602340975e1b36a869eb5c6f1031f08`；整文件 SHA-256：`362c0c1994bf79beccfb6c62593182ccc604cab58dd6015002fa42980e954c41`。可交 root 第三人静态审；正文再变须重新复核并绑定摘要，初审旧 SHA 不承担最终 PASS。本人只修改本事实审文件，没有修改正文、作者 map/evidence、共享文件，没有构建、提交或安装元数据。
