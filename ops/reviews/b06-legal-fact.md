# B06 法律求助：独立事实审

审阅人：`/root/health`；作者：`/root`。实际查阅与复核日期：2026-10-13。

结论：**PASS，作者修正两处引用定位后通过**。未发现尚待解决的事实、行动条件或英语例句问题。可进入第三人静态审；本记录不代表构建、渲染或正式集成通过。

- 正文：`content/book/rights/legal/finding-help.md`
- 最终正文 SHA-256：`98b56bc44fa152f1a3674528a3ee27c87f6fe75d7785e3489918da4f3f9f639d`
- 方法：对实际文件 `text.split('---', 2)[2]` 的 UTF-8 字节计算 SHA-256；不含 frontmatter。
- 范围：全文、四州表、费用表、两段教学虚构、内部依赖与作者地图／证据。作者记录仅用于定位，本审阅者独立打开以下原文。

## 发现与闭环

1. 初次核验律师资格的加州 Before Hiring PDF 引文原标“第 1 页”，实际 license status／eligibility／public discipline 位于物理第 2 页（PDF P1，抽取 122—124 行）。已通知作者改为第 2 页，终止代理段本来就正确引用第 2 页。
2. EOIR 链接原写“第 75—80 问”，实际是工具抽取的第 75—80 行，同一题“How do I find an Accredited Representative to help me, and what types of Accredited Representatives are there?”。作者已改成“EOIR：认可代表的代理范围”，并在作者证据中准确区分题名与行号。

初稿正文 SHA 为 `d837eaaefe8a232d500270fbd173baa8602931011b19b060cdbce418578e584c`。两处引注修订后的版本为 `cfd22957adcb25ca52a9ef62cc351dd52cbe383e7de8456063e88d3e4c124277`；逆转上述两个链接文字后，哈希严格等于初稿。

第三人静态审后，作者只在“：**partial”“，**full”“例如，**教学虚构**”三处加粗前补一个普通空格。本审阅者重新读取实际文件并逆转这三处空格，哈希严格等于上述 `cfd22957…c124277`。最终绑定 `98b56bc4…f9f639d`，事实结论不变；两处引注修正链完整保留。此项核验与记录于用户暂停前的已完成修订收口，不构成继续新增研究。

## 实际独立回源

| 来源 | 本次读取位置、判断与边界 |
|---|---|
| [USAGov Legal Aid](https://www.usa.gov/legal-aid) | `web.open`，主文 24—61 行，更新 2025-11-17。低收入等项目资格、按地址查找、LSC／LawHelp／法学院及不同民事主题，支持正文的服务发现与接案核对；没有许诺所有人获得免费代理 |
| [LSC I Need Legal Help](https://www.lsc.gov/about-lsc/what-legal-aid/i-need-legal-help) | web 主文 17—49 行；civil legal aid、受资助组织、地址／城市查询及联系下一步。未实际输入地址或将列表等同申请批准，正文用途准确 |
| [CA Before Selecting an Attorney](https://www.calbar.ca.gov/public/legal-resources/selecting-attorney) | web 主文 17—102 行，Finding the right lawyer、Public defenders、Prepaid legal services、initial consultation。支持准备当事人和文件、实际工作人员、费用与初谈；刑事指定辩护仅分流，未展开不完整资格法则 |
| [CA Before Hiring PDF](https://www.calbar.ca.gov/Portals/0/documents/ConsumerInformation/Before-You-Hire-an-Attorney-EN.pdf) | web 实际 PDF 两物理页，February 2020。第 2 页核对资格与公开纪律、保留文件、沟通、费用及解除委托可能涉及法官许可。正文未复述过时律师人数或概括书面合同门槛；实际引用页码现已修正 |
| [CA Fees and Billing](https://www.calbar.ca.gov/public/legal-resources/working-attorney/what-expect-regarding-fees-and-billing) | web 实读主文 17—82 行。fixed／hourly／retainer 的不同含义、contingency 和费用与开支、协议内容、负担困难及账单异议。四行费用表属询问清单，未把 retainer 一概写成不可退，未将无赔偿等同无需承担任何开支；不承诺固定收费覆盖全部程序 |
| [California Courts Limited-Scope Representation](https://selfhelp.courts.ca.gov/limited-scope-representation) | web 403；同日普通 HTTPS `requests` 返回 200，TLS 校验开启；BeautifulSoup main 全文实际读到 Work with a lawyer for part of your case、Benefits、Decide if right for you、Examples。本文准确限定 CA 说明、本人保留责任及先讨论适合性，不推广全国所有程序。未使用作者仅搜索见到的 Rule 3.35 摘要作证据 |
| [CA Attorney Search](https://apps.calbar.ca.gov/attorney/LicenseeSearch/QuickSearch) | web 首次结果被公共菜单截断后，另行 `open` 定位 949 行；实际读查询区 954—983 行，姓名／bar number、specialist 与 self-reported practice area、主管机构不验证自报专业说明。正文区分查资格与评价专长，未查询具体个人 |
| [NY Courts Find a Lawyer](https://www.nycourts.gov/help/representing-yourself-court/find-lawyer) | web 主文 96—116 行；免费项目、资格、法院志愿律师建议而非出庭、付费转介和后续收费。正文未采用该页 NYC“by 2022”的旧概括，也未误写初谈就是正式接案 |
| [NY Courts Legal Professional](https://www.nycourts.gov/legal-professional) | web 15—57 行，Attorney Search、grievance、fee dispute 及免费查询的真实入口。正文只指向主管导航；未声称本次成功提交个人姓名查询、核实任一律师或所有程序权限 |
| [NY Courts Clerk's Office](https://www.nycourts.gov/help/representing-yourself-court/how-clerks-office-can-help) | web 完整主文 94—122 行；程序／表格／记录可帮助、不可选择诉讼步骤／个案分析／预测结果。本文以纽约法院说明阐释窗口与个案建议的边界，没有让法院书记员替读者选主张 |
| [WSBA Find Legal Help](https://wsba.org/for-the-public/find-legal-help) | web 主文 27—100 行；WSBA 不自行给私人律师转介，页面提供各类路径；King County 的 211 与其他地区 CLEAR、低收入民事、志愿服务、有限执照类型。正文是一般入口，没有遮蔽其范围或承诺必获代理 |
| [WSBA Legal Directory](https://www.mywsba.org/PersonifyEbusiness/LegalDirectory.aspx) | web redirect loop；普通 HTTPS `requests` 200，实际读取 Purpose Statement、eligible to practice／license type／license status 及搜索字段。包括 lawyer／LPO／LLLT；目录不等于推荐，非完整历史名册。本文区分执照类型和权限，未将目录中所有人称为律师 |
| [Texas LRIS](https://www.texasbar.com/AM/Template.cfm?Section=LRIS_Online_Referral_Form) | web 主文 227—234 行；付费转介、不是免费／低费法律援助、初谈 up to 30 minutes／no more than $20、后续另商定。正文金额与时长正确，不推广到所有律师初谈 |
| [Texas Find a Lawyer](https://www.texasbar.com/AM/Template.cfm?Find=0&Section=Find_A_Lawyer&Template=/CustomSource/MemberDirectory/Search_Form_Client_Main.cfm) | web 实际读到查询区 233—260 行，事务类型、city／ZIP／州外执业等候选字段；未提交真实检索。正文仅用于筛选候选人，再另核资格，未将事务分类当认证专业 |
| [USCIS Find Legal Services](https://www.uscis.gov/scams-fraud-and-misconduct/avoid-scams/find-legal-services) | web 403；普通 HTTPS `requests` 200，BeautifulSoup main 全文读取，更新 2026-08-04。Who Can Represent You、Other Representatives、Finding a Representative、G-28／G-28I、签字、替换／撤回和投诉均读。本文保留监督学生等例外，notario／consultant 的名称不产生法律权限；美国境内常见律师与认可代表的 G-28 关系、本人同意和收件安排准确。没有把认可组织规则强加于律师 |
| [EOIR R&A Program](https://www.justice.gov/eoir/recognition-and-accreditation-program) | web 主文 50—81 行，当前页面更新 2026-04-29；组织 recognition 与个人 accreditation 分离、非律师代表只能通过认可组织服务、DHS 与 EOIR/BIA。正文不采用培训要求或续期年数作无需解释的新资格规则 |
| [EOIR Roster Reports](https://www.justice.gov/eoir/recognition-accreditation-roster-reports) | web 主文 39—55 行，更新 2025-04-28；实际看到组织、个人、按州合并三类名单。另点开当前 [Accredited Representatives Roster PDF](https://www.justice.gov/media/1193716/dl?inline=)，报告更新 2026-10-04，共 234 页，仅实际读第 1 页的表头、免责声明及标记：个人／组织状态、日期、DHS only、pending renewal。没有核完整名册，也没有对某人出具资格结论 |
| [EOIR R&A FAQs](https://www.justice.gov/eoir/recognition-and-accreditation-program-frequently-asked-questions) | web 主文 53—82 行完整实际读到两类代表；另读 488—511 行续期与多办公室边界，页面更新 2026-02-23。正文 partial／DHS only 与 full／EOIR 法庭和 BIA 区分正确；通过有资格组织提供服务与需要核对人的行动准确。原引用把行号误作问号，已闭环修正；正文不推断任何日期过期即必然失效，避免忽略 pending renewal |
| [Texas Resolving Fee Disagreements](https://www.texasbar.com/Content/NavigationMenu/ForThePublic/ProblemswithanAttorney/ResolvingFeeDisagreements/default.htm) | web 实读 240—337 行；先沟通、CAAP、一般收费金额争议不由纪律过程处理、涉及不支持收费等另可投诉、地方程序通常自愿。正文保留一般争议与职业行为投诉的分流，没有将 TX 模式推广四州 |
| [CA File Complaints & Claims](https://www.calbar.ca.gov/public/file-complaints-claims) | web 主文 15—49 行；行为投诉、UPL 与 CSF discretionary reimbursement 分立。正文的有条件补偿与原案仍需安排准确，没有把提交投诉许诺退款或接手原案 |

## 全文判断与审阅界限

- 读者链条完整：文件与日期→适合服务→资格与管辖→咨询／代理范围→费用→工作责任→沟通、争议与换人。没有把排队、初谈或投诉当成暂停原案日期的依据。
- 两个例子均明确教学虚构；英文自然可用，日期示例没有冒充真实法定期限。有限代理的样句用于说明范围，明确不是可直接提交或适用于所有法域的标准合同。
- 本页不提供诉讼答辩、刑事指定律师资格、法律援助完整收入／身份限制、移民个案建议、四州全部收费仲裁细目或跨州执业许可结论。上述未核范围没有被正文写成保证。
- 本次没有联系机构、提交转介表、查询私人账户或个人案件，也没有为任何具名专业人员核发资格背书。目录与门户证明可用入口及其自述功能；不等于真实申请／检索流程已成功完成。
- 审阅者仅新建本记录，未改作者正文、元数据、证据和共享文件；两处正文修正均由作者完成。未构建、未渲染、未提交。

后续正式集成必须由第三名参与者进行静态审；页面内容或关键来源变动需按变动范围重新回源并重绑正文 SHA。
