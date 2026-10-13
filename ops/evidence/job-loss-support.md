# B06 失业与工时减少支持：作者证据

原作者 civic；恢复修订者 birth_fact；实际查阅 2026-10-13。对应 `content/book/work/employment/job-loss-support.md`。新稿仍 written／draft true，verified 与 reviewed_by 空，本文不是独立审阅结论。独立事实审为 root，第三人静态审为 static_editor；birth_fact 本次只承担作者修订。

当前正文 SHA-256：`160a39b1cdd003a0528be0396f50330ddda787cc1e43b11491f630372bf3f7d7`，按 UTF-8 `split('---', 2)[2]` 实际计算。原作者冻结稿 `e33e6d6c6fb35c66b551da0406a29ab6a86c88c31506ec681ed3744bdbf46ace` 留作历史。本次只改变下述两段 TX 来源／文件名／术语说明，其他规则、金额、期限、身份条件及元数据未改；未构建或提交。

## 2026-10-13 恢复修订：替换 TX 两处旧资料包引用

birth_fact 先全文读正文、地图和下方 civic 作者证据，再独立实际打开以下三份一手材料。不是仅采用 root 已读回执：前两页 web 本次超时，随后普通 TLS 请求均返回 200 并实读页面；第三页 web 已实际读到主文。

| 本轮实际读到的来源与定位 | 修订采用范围 |
|---|---|
| [TWC：About Your Unemployment Benefits Application](https://content.govdelivery.com/accounts/TXWC/bulletins/3cf852d)，页面署名 Texas Workforce Commission，发送时间 2025-01-29 08:52 AM CST；实读英语 Claim Processing、Correspondence and Documents、Request Payment、Maintaining Eligibility 等主文 | Claim Processing 给准确文件名 Statement of Wages and Potential Benefit Amounts，并说明它不是资格全面批准；Request Payment 要按所寄说明的 date/day 请求支付，不能等资格通知，UBS 或 800-558-8321，每两周继续。本文两处旧包引用改为此明确日期的 TWC 公告。未采用同页处理天数、雇主回复期、身份核验等待时间、延长福利或其他未改写条件。 |
| [TWC：CC Contact Us](https://cs.twc.texas.gov/TWC-CC-Contact-Us/)，实读 Unemployment Benefit Claims Services | 明列 Unemployment Telecenter 800-939-6631 与 Automated System, Tele-Serv 800-558-8321。本文电话申请处增加正式联系引用；没有使用在线表单、提交个人信息或保证接通时间。页面的离线／只读提示不影响公开电话说明的实际读取，本轮不声称已验证表单功能。 |
| [Workforce Solutions of West Central Texas：Filing for Unemployment Benefits](https://www.wfswct.org/394/Filing-for-Benefits)，首段第 19 行，并读后续申请／文件／支付段以辨边界 | 首段明确可在线或拨 800-939-6631 申请，作为电话申请用途的地方 workforce 主管互核。其后最低每周三次、waiting week 和其他时间概括未用于正文；本次不以该页替代完整 2026 资格研究。 |

root 独立审本轮对原 [Coastal Bend Rapid Response Packet](https://www.workforcesolutionscb.org/wp-content/uploads/2025/02/Rapid-Response-Packet.pdf) 的复取记录为普通直连 503、web 超时及正常 8888 代理 503；该失败由 root 实际执行，本修订者不声称亲自重读成功。下方来源 19 的 civic 历史实读保留，但不把它写成本轮可达或当期全部条件已核。本次用已经实际读到的 TWC 署名公告和正式联系入口支持 TX 核心申请／支付断言，不反复尝试无关附件。

具体修订：原 Statement of Potential Benefits 改为上表准确名称并加中文；原未重新读到的 Work Search Notification 标题改为“查看机构寄来的求职要求，按通知安排每周活动”；支付表 filing day 加“申报日”解释。没有新增求职次数、注册期限、等候周、给付上限或任何身份判断。改稿后交 root 对最终版本完成独立事实审，再交 static_editor 第三人静态审。

## 原作者核验方法及已知来源冲突（历史）

以下链接均实际读到正文或 PDF 所述页面。web 无正文或返回错误时，用普通 HTTPS requests／BeautifulSoup 读取公共页面；PDF 以 web 文本或 requests 内存 pypdf 阅读。没有登录、提交申请、联系机构或触碰账户。没有写入下载文件。

- TWC 主站 `www.twc.texas.gov` 的 eligibility、handbook、request-benefit-payments 等本轮 web 返回机器人页，普通 HTTPS 返回 CloudFront 地区 403；旧 `twc.state.tx.us` 重定向同处，test 子站也无法读取。未将其搜索摘要标作实读。基本资格改用同机构 efte 教材和现行州法；支付请求与申请电话采用地方 Workforce Solutions 发布资料包中实际署名 TWC 的原件，并以可读 UBS 登录页互核入口。未借测试站或第三方计算器推导现行资格。
- Texas 法典旧域名 `statutes.capitol.texas.gov/GetStatute.aspx` 本轮返回首页，`tcss.legis.texas.gov/Docs/...` 大写路径 web 不可读；普通 HTTPS 的小写 `/docs/LA/htm/LA.201.htm` 与 `.212.htm` 实际 200 且有法条。正文使用后者。
- EDD 的 DE 8714AB 为 Rev. 5 (9-18)，当前资格页仍链接该原件；只用于现行页面援引的基期与金额测试。2018 年 PDF 中电话营业时间未采用，电话及申请方式另读当前 Step 2 页面。
- WA Information You Need 页把 regular base year 笼统写作 18 months，与同机构专门 Estimate Your Benefit 的四个季度定义不一致。正文将 18 个月仅用于准备就业经历；基期采用专门计算页明确的 first 4 of last 5 completed quarters，没有把 18 个月写成计入工资的普通基期。
- NY P832 当前下载实读为 2/26，2026 年 3,500／19,118／9,559 与当前 FAQs 一致。正文不采用其他旧版 3,400 门槛，不写每周最高给付金额，避免把旧年度数字带入。

## 文件、工资和申请州

1. [WA ESD Information You Need](https://esd.wa.gov/get-financial-help/unemployment-benefits/applying-unemployment-benefits/how-apply-unemployment-benefits/information-you-need-when-you-apply)，普通 HTTPS 200，实际读 Basic information、Your work history from the last 18 months、employer contact／dates：所有兼职临时雇主、日期、身份及授权信息；州证件是 if you have one；完成后有 how to apply 入口。仅作资料准备，不复用该页错误的 18 个月基期句。
2. [CA DIR Paydays](https://www.dir.ca.gov/dlse/FAQ_Paydays.htm)，web 完整相关主文：discharged immediate（含 accrued vacation）；无固定期限书面合同的辞职者 72 小时及事先通知差别；电影、油井、季节产品等例外；无争议工资不可因其他争议扣住。正文只概括普通已赚取工资和必要边界。
3. [NY Wages and Hours FAQ](https://dol.ny.gov/wages-and-hours-frequently-asked-questions)，web 实读离职工资问答：regular payday for pay period worked；if requested, mail final wages。未采用此页其他行业的旧年度工时概述。
4. [WA L&I Getting Paid](https://www.lni.wa.gov/workers-rights/wages/getting-paid/)，web 全文：quit／fired final paycheck on or before next regularly scheduled payday；不得为钥匙设备扣住；severance／vacation 等福利另有约定问题。
5. [TWC Final Pay](https://efte.twc.texas.gov/final_pay.html)，普通 HTTPS 200 全文：involuntary six calendar days；voluntary next regularly scheduled payday；commission／bonus agreement 可另定支付进度，不能一律把所有补偿并入六日。
6. [DOL State UI](https://www.dol.gov/general/topic/unemployment-insurance)，web 403 后普通 HTTPS 200 实读 How Do I Apply：尽快联系工作州；住在外州或多州工作时可向现居州机构问跨州手续；准确提供前雇主地址与日期。未引用同页 COVID 特别宽免或一般预计处理天数。

## 四州申请与工资资格

7. [EDD Eligibility](https://edd.ca.gov/en/unemployment/Eligibility)，web 全文：足够基期工资、全部或部分失业、无自身过错、能且可工作、寻找工作；错误分类的 contractor 可申请由 EDD 判定；每两周认证；CalJOBS 等要求按通知。本页未写 21 天具体登记期限，避免不交代通知起算点。
8. [EDD Eligibility FAQ](https://edd.ca.gov/en/unemployment/FAQ_-_Eligibility/)，web 全文相关问答：主动辞职可能有 good cause，维持就业的努力及具体事实；无法工作时转 DI／照护转 PFL，未概括为所有州照护必无资格；非公民合法身份和授权覆盖赚取工资时与每个申请周，EDD 经 DHS 核验。
9. [DE 8714AB](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de8714ab.pdf)，web 实读 2 页；第 1 页完整 monetary tests：1,300 high quarter 或 900 且 total 1.25 倍；standard first 4 of last 5 completed quarters；不够时自动 ABP last 4，已有标准资格不能为更高金额任选。第 2 页旧电话时间未用。
10. [EDD Step 2 Apply](https://edd.ca.gov/en/unemployment/step-2-apply/)，web 完整申请段：myEDD／UI Online、电话／fax／mail，普通话 1-866-303-0706，AJCC 帮助完成纸件，language resources。未把所有 EDD 电话功能写成相同。
11. [NY P832](https://dol.ny.gov/how-your-weekly-unemployment-insurance-benefit-payment-calculated-p832)，由 [How Much Will My Benefit Be](https://dol.ny.gov/node/32526) 点击下载，web 实读 2 页，版号 2/26。第 1 页普通／替代基期和使用过的工资不得再次用于下一申请；第 2 页 2026 两季、3,500、1.5 倍及 19,118／9,559 例外。每周金额算法与 maximum/minimum 未移入正文。
12. [NY Before You File FAQs](https://dol.ny.gov/you-file-claim-unemployment-faqs)，web 实读主文：2026 门槛互核；标准已合格但替代可更高时需 request within 10 days of date on initial Monetary Determination；首次完全或部分失业周申请；跨州工资可由一个实际工作州处理；非公民失业时合法工作、能合法接受新工作；severance／partial eligibility 按具体条件。未写边界不同的小于／小于等于最高金额，亦未硬编码每周最高福利。
13. [NY Claimant Benefit Process](https://dol.ny.gov/unemployment-claimant-benefit-process-0)，web 实读申请与电话段：新申请链接到 `unemployment.labor.ny.gov`，电话 1-888-209-8124；普通话、粤语等选项；回复问卷、消息与调查。本页未保证两到三周到账。
14. [WA ESD Basic Eligibility](https://esd.wa.gov/get-financial-help/unemployment-benefits/basic-eligibility-requirements)，web 不稳定，普通 HTTPS 200 主文：680 小时；通常最近 18 个月 WA 部分工资；近期军人／联邦分支；每周能且可工作及求职；part-time 可能扣减；UI 与 paid family medical leave 不可同领的具体提醒未外推成一切照护都不合格。
15. [WA Estimate Your Benefit](https://esd.wa.gov/get-financial-help/unemployment-benefits/estimate-your-benefit)，普通 HTTPS 200，实读 Your base year 与 Alternate base year：first 4 of last 5 completed quarters；普通不足 680 小时可查 last 4，替代仍 680。未采网页计算器输出，未算个案金额。
16. [TWC Eligibility Issues](https://efte.twc.texas.gov/ui_law_eligibility_issues.html)，web 主文和普通 HTTPS 互核 Monetary Eligibility、Continuing Eligibility、Partial Unemployment：first 4 of last 5；至少两季 wages；总额 37 × WBA；之前有申请者另有后续 6 × WBA 工资要求；当前工作授权、能工作、可接受工作、工作登记等。missing wages 可由 SSN 误配／漏报／分类造成。本稿不计算 WBA 或固定 125% 公式，不泛化为所有低于 40 小时可领。
17. [Texas Labor Code §201.011(1)](https://tcss.legis.texas.gov/docs/LA/htm/LA.201.htm)，普通 HTTPS 全章并定位：特殊医学可验证疾病／伤害影响 major part of quarter，可用受伤／患病季度之前的五季前四季，须发生起 24 个月内 initial claim。正文仅说明不同于其他州 last 4，不另抄 seven weeks（这是机构口径，未读当期解释故不采用）。
18. [UBS Logon](https://apps.twc.texas.gov/UBS/security/logon.do)，web 正文：旧用户应使用既有账号和恢复功能，勿新建。公开页可访问不等于账户内申请已验证，本轮没有登录。
19. [Workforce Solutions Coastal Bend Rapid Response Packet](https://www.workforcesolutionscb.org/wp-content/uploads/2025/02/Rapid-Response-Packet.pdf)，web 实读 7 页中的物理第 1—2 页；第 2 页为署名 TEXAS WORKFORCE COMMISSION 的 Unemployment Benefits Claim Help & Resources 原件：UBS、Tele-Center 800-939-6631、Tele-Serv 800-558-8321；Statement of Potential Benefits／Work Search Notification；每两周 filing day 申请支付，do not wait for TWC to determine eligibility。资料包路径为 2025/02，内部其他社区清单为 2023，故只采用 TWC 署名页稳定的流程与电话，不把整个包声称为 2026 新版手册，不引用人员私人联系方式、过时职位名单或固定处理天数。主站当期搜索定位与原件规则相符，但搜索摘要只作查找，不作为主要证据。

## 非公民与工作授权

20. [NY Labor Law §590(9)](https://www.nysenate.gov/legislation/laws/LAB/590)，web 实读 283—303 行对应第 9 项：过去 remuneration 的非公民身份条件，包括 lawful permanent residence、lawfully present for performing services、PRUCOL；保留法条与当期 FAQs 双来源，未把仅有 EAD／SSN 写成充分条件。
21. [WA ESD Citizenship and Legal Rights](https://esd.wa.gov/get-financial-help/unemployment-benefits/applying-unemployment-benefits/how-apply-unemployment-benefits/citizenship-and-legal-rights)，普通 HTTPS 主文实读：询问最近 24 个月合法工作情况、most recent immigration document、补资料信、SAVE 工作授权核验；未把举例文件当成一律自动具有工作授权。
22. [RCW 50.20.098](https://app.leg.wa.gov/RCW/default.aspx?cite=50.20.098)，web 实读 Services performed by alien (1)—(3)：过去服务作为给付依据的法定类别；正文概括并保留原法，没有逐项推导 asylum／parole 等个案。
23. [TWC Coverage Issues](https://efte.twc.texas.gov/ui_law_coverage_issues.html)，普通 HTTPS 实读 Non-Citizens／§207.043 引文以及分类段，配合来源 16 当前工作授权：工资须报告不等于可计入给付。法定过去身份类别原文已读，未用雇主指南中的过时 INS 名称概括当前主管机关。
24. [USCIS Legal Services](https://www.uscis.gov/scams-fraud-and-misconduct/avoid-scams/legal-services)，旧 find-legal-services 入口 web 不可读，普通 HTTPS 重定向现址 200；主文 Who Can Represent、What Representatives Can Do：合格律师、DOJ recognized organization accredited representative、可咨询表件和移民选择。正文只转介，不采用网上已归档的离职后宽限期说明作当前期限承诺。

## 持续申报、受阻与初次申诉

25. [EDD Step 5 Certify](https://edd.ca.gov/en/unemployment/step-5-certify-for-benefits/)，web 全文：every two weeks；工资未发也要报；电话 Tele-Cert 若需报告工作工资或地址等不可用，应在线／邮寄。未把“在线 Work Search Record 屏可跳过”误写成不用求职。
26. [NY Certify Weekly Benefits](https://dol.ny.gov/unemployment/certify-weekly-unemployment-insurance-benefits)，web 实读 Overview、When to Certify、在线与电话：收到可以认证的通知后每周；Monday–Sunday，一周最后 Sunday 至 following Saturday 申报该周；没有照搬 WA 的 Sunday–Saturday 周界。
27. [WA How to File Weekly Claims](https://esd.wa.gov/get-financial-help/unemployment-benefits/weekly-unemployment-claims/how-file-your-weekly-claims)，普通 HTTPS 实读：Sunday–Saturday 结束后；等待资格、工资工时加入、申诉时均继续；claims center 800-318-6022；cash-out vacation 不对应申领日期与该周 vacation pay 区别；离职款项按种类处理。未写所有 severance 一定扣减或一定不影响。
28. [WA Decision Letter](https://esd.wa.gov/get-financial-help/unemployment-benefits/applying-unemployment-benefits/understand-your-benefits-decision-letter)，普通 HTTPS 实读：逐季工资／工时；0 元可能是漏报；带工资单、W-2、雇主联系及日期更正；combined wages 等还没加完时可能非最终决定。
29. [EDD Step 4 Documents](https://edd.ca.gov/en/unemployment/step-4-review-benefit-documents/)，普通 HTTPS 全文：DE 1101CLMT、DE 5614、DE 429Z、DE 4581、DE 1326C；核对错工资日期雇主并按通知更正。未把过往“10 天纠错”记忆写为当前统一期限。
30. [EDD Appeals](https://edd.ca.gov/en/unemployment/appeals/)，web 完整主文：DE 1080CZ／DE 1444CT 寄发日起 30 天书面；DE 1000M 或 letter，通知首部地址；逾期 good cause；继续认证，only weeks certified and otherwise eligible 可支付；口译／accommodation 请求。
31. [NY Hearing Process FAQ](https://dol.ny.gov/hearing-process-frequently-asked-questions)，web 完整相关主文＋普通 HTTPS复核：最初 request hearing 须 mailed／personal delivery 后 30 天内，邮戳或其他证据；online／mail／fax；继续每周申报以保全权利；后续 ALJ appeal 另有 20 天，本页不把初次 30 天套到第二级。
32. [WA Appeal Decision](https://esd.wa.gov/get-financial-help/unemployment-benefits/appeal-unemployment-benefits-decision)，普通 HTTPS 全文：from date ESD sends decision 30 days；eServices／mail／fax，非所有决定可online、不能phone／email；多个决定各列或分别提交；继续weekly，未claim不支付；逾期说明理由。
33. [Texas Labor Code §212.053](https://tcss.legis.texas.gov/docs/LA/htm/LA.212.htm)，普通 HTTPS实读，另取同路径 PDF 在内存 pypdf 互核：claimant 最迟 copy mailed 后第14 calendar day；[TWC Claim and Appeal Process](https://efte.twc.texas.gov/ui_law_the_claim_and_appeal_process.html)，普通 HTTPS 实读 initial determination／appeal tribunal：writing、fax／mail／delivery／portal，按具体决定，保留证据。正文未把 employer 原始答复期限错误当成 claimant 期限，主时限采用法条直接支持。

## 医疗与紧急支持

34. 已有医保页 `content/book/people/health/coverage-changes.md`：只复用既有完整稿的衔接入口，不重写资格、窗口或未来法规数字；工资页、身份文件页、租房页同理。
35. [USAGov Emergency Food](https://www.usa.gov/emergency-food-assistance)，web 全文：food pantry／food bank、211 与机构资源；原文 updated 2025-12-23。正文未承诺211一定代办，也未将 pantry 目录等同食品资格批准。
36. [USAGov Emergency Housing](https://www.usa.gov/emergency-housing-assistance)，web 全文：短期住房及州紧急租金帮助分别有入口；正文提醒通知与法院程序另行处理，租房既有稿承接。未引用疫情时期的统一租金项目。
37. [USAGov SNAP](https://www.usa.gov/food-stamps)，web 实读申请与州／地方办公室，收入与资金等州要求；[TANF](https://www.usa.gov/welfare-benefits)，web 实读 What is／Eligibility／local office，后者 updated 2026-01-13。仅作项目分流，不声明具体移民类别可领；家庭谁申请、所需资料让对应项目分别判断。2026 FNS QC 手册搜索曾提示 non-applicant，但未完整核验该规则的当期变更，故未将该材料变成正文资格断言。

## 作者自检与未核实边界

无真实申请人数据、无账户登录或提交；未验证电话接通时长、账号内每屏或当天项目资金。四州基期门槛、初次申诉、最后工资、身份边界均有实际一手来源；金额信不是资格全通过、UI 不是劳动分类或 SSN 判断已在正文分开。三张比较表均两列。站内目标存在；中文加粗边界在收稿前扫描。没有自行构建或提交。特殊工种、第二福利年度、等候周完整比较、给付金额计算、追回与多级上诉、SNAP／TANF 细则留地图。

## B06 主控集成记录

civic原作者／birth_fact修订；root独立事实审、static_editor第三人静态审均PASS。当前正文160a39b1；B06正式integrated／draft false，2026-10-13，见b06-integration.md。 本段仅登记实际完成的审阅与集成，不新增来源实读或个案核实声明；实际读到的范围与失败边界见对应事实审记录。
