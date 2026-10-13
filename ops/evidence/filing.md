# 年度报税、付款与海外账户：作者证据

查阅：2026-10-13；B10作者root。正文为 `content/book/work/tax/filing.md`，年度申报、付款、更正和普通海外收入／账户合并为同一办理链。普通日历年使用已经公布的2025税年及2026办理日历；查阅日10月13日与原到期日、合规延期后的日期分开，未出版的2026税年字段不套旧值。既有tax-residency、state-residency和号码页是继续入口，不继承其他作者的实际回源或审阅结论。

本轮50个不同官方URL均以正常TLS实际取得HTTP200，原件在下载前已经逐个验证忽略的 `.cache/evidence/filing/`。48网页、2 PDF；2026-10-13作者再次逐个从实际原件字节独立计算SHA，50/50与下载索引一致。索引的初始“not yet read”只是下载时状态，本记录的实际读段才是阅读依据。下表列最终URL、网页主文清理后的定位行／PDF实际物理页及原始字节SHA；HTTP200、检索摘要或索引本身不算阅读。

实际阅读为39网页主文全文、9网页所采用段落和2 PDF的明确页段；长说明没有冒认全文。PDF的pypdf提取曾出现字体警告，随后实际使用pdftotext保留版式重读所列完整物理页文本，没有将警告当作来源失败或跳过阅读。两PDF分别为2025 Form4868四物理页中的1／2，以及FinCEN当前入口仍提供的2017 v1.4 FBAR说明二十二物理页中的1／2／4—6；后者不是2025新出版说明，日期／门槛另与当前FinCEN和IRS主文交叉核。

## 采用断言与范围

- 是否须报：普通2025单身未满65岁、非盲人且不能被他人列为受抚养人的15,750美元门槛，保留全部限定；自雇净收入400美元及以上采用当前Self-employed Tax Center，不把一般need-file页的“over $400”当成精确边界。低于门槛的退款可能、信息表之外的收入和材料来自已读对应主文。
- 表件与期限：1040／1040-NR／dual-status及F/J/M/Q例外只采用2025 NR说明列明段落；居民与非居民条件不同。普通4月15日、及时4868后的10月15日、付款不延期、NR有／无须扣缴雇员工资的4月／6月分支、境外公民／居民的居住加工作地点资格及计息均已读。没有在10月13日虚构可以追认原截止日前的新申请。
- 四州：CA540与540NR分支、自动10月15日申报而普通付款仍4月15日；CA原期限在境外生活或旅行的6月15日／12月15日与联邦境外工作资格分开。NY原期限IT370州申请、原付款及当期申请已结束；WA普通2025工资无州所得税但资本利得独立申报，申请延期／已付款即使最终零税仍须报、联邦延期证明与MyDOR州申请、付款原截止；TX宪法Sec24-a个人净所得税禁令。未把州居民身份等同联邦nonresident alien。
- 海外收入：全球所得、合格外国税抵免1116、境外劳动所得排除2555的tax home／身份／居住测试及连续12个月330完整日、自雇税与重复抵免边界；外币收入／费用按收到、支付或应计规则留汇率，不套FBAR年末账户换算。Foreign Earned Income页只给旧2020—2023排除额度，正文没有借用作2025上限。
- FBAR：美国人及7701(b)居民测试同时保留FBAR自己的美国地理范围；外国账户按分行所在地、权益／签字权限、合计任一时点超过10,000美元，非每户免额；Form114独立BSA E-Filing、个人无需注册，4月15日自动10月15日与所得税延期不同。最高外币值按财政部年末汇率等规则、配偶例外114a及保存五年均核真实主文。未操作BSA后台、真实账户或递交。
- 8938：specified individual身份、账户及其他指定资产、签字权限不自动构成资产权益、无需所得税表时不须8938但其他报告仍可能。住美国未婚／MFS年末50,000或年内75,000、MFJ100,000／150,000；符合境外tax home及居住／完整日条件未婚／MFS200,000／300,000、MFJ400,000／600,000，均为“超过”，两种时点分别列明。随年度税表及其合规延期来自实际222—234，不由FBAR自动延期推出。
- 服务及提交：2025 FreeFile AGI89,000、合作商各自条件／州表收费／不同表件支持，Fillable不提供州表、当期服务至2026-10-15；VITA核各站点自身收入／范围而不写统一69,000或70,244门槛，TCE特别60+；付费PTIN、完整版本／签字、空白签字与按退款比例收费等。受理accepted与软件发送、机关付款及独立FBAR确认分别留档；纸质联合表签署与代签依据实际tc301全文56—68，不借通用how-to-file的标题推出。
- 迟报、更正与记录：付不起仍报、当前在线长期50,000以下含等号且全税表已交／短期少于100,000及180日、利息罚款与批准分开；1040X及一般退款三年／两年较晚、自动算术调整。CA联邦更正后通常六个月且影响CA税额、NY联邦更正后递交90日／IRS最终调整确定90日、assessment异议不能用更正代替；WA MyDOR实际709—788完整更正流程。税表通常三年但资产等更长、FBAR从期限起五年；CP/LTR期限及Form9000入口；新年自雇通常还核季度预缴而非等次年。

## 失败、冲突与未核边界

这50个已列原件的最终请求全部正常TLS200，未采用关闭证书校验等办法。没有因任一来源成功而认其他页面可读。主文清理行仅作本次缓存定位，不是官网永久行号；下表URL才是实际主管入口。

IRS通用how-to-file页仍有旧69,000志愿服务介绍，当前VITA主文明确站点自行收入条件并提到EITC重点70,244；正文按站点核，不写全国统一收入线。IRS past-due页仍有60—120日旧短期付款介绍，采用当前payment-agreement明确180日。WA所得税主文还介绍2028起的新税和2029申报，正文只断言2025工资无该普通税，没有写永久不征税；资本利得新税率／年度扣除数字不纳本页一般申报判断。CA自动境外旅行分支不能替代联邦境外工作资格。

未读完整1040-NR4254行、8938994行、CA5402478行、NY2025 IT2034400行、WA MyDOR1495行以及所有PDF剩余物理页；没有认全文核验。CA非居民门槛中段表未采用统一数值。IRS灾害名单只核通用入口，未核具体县、事件和个人资格；FinCEN灾害公告另核。没有核新年度未发布表件、实时站点预约／语言／可接案范围、收费报价、真实本人登录、退款、付款、电子受理／退件后台、任一真实账户价值、所有软件表件支持或海外实体／信托／遗产赠与全套程序。FTC／FEIE个案和所有协定、自雇工资税协定、双身份联合选择等留地图，给专业核验继续路径。

作者全文及静态自查只用于冻结，不是独立事实或第三静态PASS。初次136行实际完整读；69—136的初次输出服务选择处截断后实际另读94—106补齐，不把截断认全文。正文82链接（76外／45不同URL、6内／5不同当前integrated且draft false目标）与三表2／2／3列、9H2、56加粗外空格均实查。新稿保持written／draft true／verified与reviewed_by空；正式送static_editor事实，之后birth_fact第三静态，再由root工程与实际渲染。初冻结正文SHA-256：`12f95928a810ad4e1885b3bb37250c327966c17ac122c49e0699f1cca871d429`；整文件SHA-256：`6c26f667dda0a0b96beb7119edb29901dd0d34f17904d3230eeef6e3a514e698`；此版有两处未实际打开的年份后缀链接，独立事实未PASS，末节修订版才是当前。

## 实际原件与采用页段

下表的“全文”仅指本次去导航后的网页主文行，不包含网页脚本、所有外链或后台；没有由网页可读推出链接目标也已读。

| 来源 | 实际读取／采用范围 | 原始字节 SHA-256 |
|---|---|---|
| [Individual tax filing \| Internal Revenue Service](https://www.irs.gov/individual-tax-filing) | 网页主文1—50全文实读 | 0c4a67a21585a152e14d52d55542ea829be8e28357bad9ed6f118da7a7134e9c |
| [File your tax return \| Internal Revenue Service](https://www.irs.gov/filing/individuals/how-to-file) | 网页主文1—88全文实读 | 09dfb32085fccc0f3e2dc7ecdb42fe8c92a7d0d1119f31695e57e031a82ca8e2 |
| [Topic no. 301, When, how and where to file \| Internal Revenue Service](https://www.irs.gov/taxtopics/tc301) | 网页主文1—85全文实读 | 1d0a035ede8011454fba4025a626dac58312005d90f404aa81f0303953fc2dbe |
| [Instructions for Form 1040-NR (2025) \| Internal Revenue Service](https://www.irs.gov/instructions/i1040nr) | 2025说明4254行中的805—922、984—1160、1177—1230；采用完整段落已分批实读，后补850—886／1026—1054／1154—1160避免输出截断缺段 | 91663592896ec730eb8a350552dfde0bac8cab9b1d6c6b42eed36100ba5078be |
| [About Form 1040-NR, U.S. Nonresident Alien Income Tax Return \| Internal Revenue Service](https://www.irs.gov/forms-pubs/about-form-1040-nr) | 网页主文1—58全文实读 | 3104236d950f81e07b24fd9ea7b5b74d679a1ab5a998b1153c12e974f1b9f09d |
| [E-file: Do your taxes for free \| Internal Revenue Service](https://www.irs.gov/e-file-do-your-taxes-for-free) | 网页主文1—127全文实读 | 5c7eb87c7a5ddd77b76d5c7e2f7ace0d5cce8b14506e3d4f738860066adbe128 |
| [It’s not too late; use IRS Free File today \| Internal Revenue Service](https://www.irs.gov/newsroom/its-not-too-late-use-irs-free-file-today) | 网页主文1—22全文实读 | eabccfce2dd652619c32b3480f8cb8c4251db608741027e0d074336dac4a8b6b |
| [Free tax return preparation for qualifying taxpayers \| Internal Revenue Service](https://www.irs.gov/individuals/free-tax-return-preparation-for-qualifying-taxpayers) | 网页主文1—66全文实读 | ab151ba296228e8b2ce7ea67173cdaacb2bc8573f86f0219759a69638ac74e9b |
| [Choosing a tax professional \| Internal Revenue Service](https://www.irs.gov/tax-professionals/choosing-a-tax-professional) | 网页主文1—31全文实读 | 7f1930f7ca2d91d13e67ad38f85dd0dc09232ad31399ed6ae489db9a99b1706f |
| [Get an extension to file your tax return \| Internal Revenue Service](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return) | 网页主文1—44全文实读 | b140e37dc299aaeacf100fe246532d5e1beb2e455568fe525730e7d427ffa714 |
| [Payments \| Internal Revenue Service](https://www.irs.gov/payments) | 网页主文1—116全文实读 | 10cd0ab1e817a5aada0696efd0f57d929ae115db9d35b01787303efc07ed189b |
| [Online payment agreement application \| Internal Revenue Service](https://www.irs.gov/payments/online-payment-agreement-application) | 网页主文1—136全文实读 | a508360a6dc10c44347791d5039843afecb3b92d7f1d2431665744fe56a71eb1 |
| [File an amended return \| Internal Revenue Service](https://www.irs.gov/filing/file-an-amended-return) | 网页主文1—63全文实读 | fd8aa5c4fc8fd43e12d220465771b8a5c12f13df05164d3d983dc170dff287fa |
| [Topic no. 305, Recordkeeping \| Internal Revenue Service](https://www.irs.gov/taxtopics/tc305) | 网页主文1—30全文实读 | 138c1b0f71ccc63b6b9de734c3406a993b922f86cea79ecc10f4269b4666d7cb |
| [Foreign earned income exclusion \| Internal Revenue Service](https://www.irs.gov/individuals/international-taxpayers/foreign-earned-income-exclusion) | 70行；1—45采用段完整重读；旧年额度不作2025金额 | 6e2c0c5449b27958d06ae445c2fd27b90dc22b304d825dd32a2b9f02852a856b |
| [Foreign Tax Credit \| Internal Revenue Service](https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit) | 网页主文1—51全文实读 | a029bba7785fca8f442c35a00ee8f17972f5f27724bef43257ec73d998edd123 |
| [Instructions for Form 8938 (11/2021) \| Internal Revenue Service](https://www.irs.gov/instructions/i8938) | Rev.11/2021，共994行；209—275、360—400、461—516，申报期限／身份／门槛／资产采用段 | 78e996401221176dc335033ca410563c6d26de1d47fe248ec1f4dcaa3d81985c |
| [Report Foreign Bank and Financial Accounts \| FinCEN.gov](https://www.fincen.gov/report-foreign-bank-and-financial-accounts) | 网页主文1—94全文实读 | 04a6119e18eda91000367657d3f4c5bfd5796f76685466e2151437e6faee5575 |
| [How Do I File the FBAR? \| FinCEN.gov](https://www.fincen.gov/how-do-i-file-fbar) | 网页主文1—9全文实读 | 3b66dd8fe77d7da6b5eb9068f5cb95e72e4a5bf1481355235843b90992185df4 |
| [Report of Foreign Bank and Financial Accounts (FBAR) \| Internal Revenue Service](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar) | 网页主文1—114全文实读 | 5bdea9e3e321c1a8af170260ae09a1dcbaa6f281268144defb165d11306dc290 |
| [2025 Personal Income Tax Booklet \| California Forms & Instructions 540 \| FTB.ca.gov](https://www.ftb.ca.gov/forms/2025/2025-540-booklet.html) | 2025说明2478行；520—606、2055—2068完整实读，另仅定位113／226／243／725，不把定位当周边全文 | 3dd41af0769e97011852289eb9748793f42839c2dc629ce3710d7f1bb65926d2 |
| [When to file \| FTB.ca.gov](https://www.ftb.ca.gov/file/when-to-file/index.html) | 网页主文1—17全文实读 | a78a82445848978325a8e42c176ee00aa2b87db38756f0e80349ee4ada0ded83 |
| [Part-year resident and nonresident \| FTB.ca.gov](https://www.ftb.ca.gov/file/personal/residency-status/part-year-and-nonresident.html) | 217行；1—57、175—217实读，中段门槛表未采用 | f874d062be58b830fca8c0ca1e9a2738bcd93df6d539dbd34b210c2ff109c979 |
| [Correct an income tax return \| FTB.ca.gov](https://www.ftb.ca.gov/file/after-you-file/amend-a-return/index.html) | 网页主文1—126全文实读 | fca25690b9aee3adaed1d3a52f4de678a5629a27738de97e1c9a9cec7f616788 |
| [Filing due dates](https://www.tax.ny.gov/pit/file/income_tax_filing_due_dates.htm) | 网页主文1—28全文实读 | 5e4d329909a6ea1ed90dce7072fcf3b6e21be108d4c37983aa2fc05e52215a31 |
| [Apply for an extension of time to file an income tax return](https://www.tax.ny.gov/pit/file/ext.htm) | 网页主文1—64全文实读 | aa2dbc710a2c06789a6517c1d4418b162bbb1e2bb674b1744a4e39eb67a1a66c |
| [Frequently Asked Questions about Filing Requirements, Residency, and Telecommuting for New York State Personal Income Tax](https://www.tax.ny.gov/pit/file/nonresident-faqs.htm) | 网页主文1—156全文实读 | e612525ebbc9259dee24fd1a4f132036b18cfae48ee6f26a6ff7da0bc98f6dea |
| [Frequently asked questions about income tax \| Washington Department of Revenue](https://dor.wa.gov/taxes-rates/income-tax/frequently-asked-questions-about-income-tax) | 网页主文1—48全文实读 | 14f815c328b345ff4be90fa4cdece6a338e97ec9e03821bccb4a29fc14a55cff |
| [Capital gains tax \| Washington Department of Revenue](https://dor.wa.gov/taxes-rates/other-taxes/capital-gains-tax) | 网页主文1—107全文实读 | 51dd09172f1809a400dde92bbecbc4f7ce0ea28d786d8debc405164db8e1952b |
| [Frequently asked questions about Washington’s capital gains tax \| Washington Department of Revenue](https://dor.wa.gov/taxes-rates/other-taxes/capital-gains-tax/frequently-asked-questions-about-washingtons-capital-gains-tax) | 网页主文1—99全文实读 | 9a60af75cb89cc6412e5d5e20f8e8a1fc440a1835fd9583f41eb99c226a8c85e |
| [THE TEXAS CONSTITUTION  ARTICLE 8. TAXATION AND REVENUE](https://tcss.legis.texas.gov/Docs/CN/htm/CN.8.htm) | 387行；335—336 Sec24-a完整条款实读，其他条款未认全文 | 97a72612a5f813691ddcb94af20e50da7770ab03f092838dfac5624f0581c3a5 |
| [Tax relief in disaster situations \| Internal Revenue Service](https://www.irs.gov/newsroom/tax-relief-in-disaster-situations) | 366行；1—35通用灾害入口实读，具体事件／县资格未核 | 19de5b5d8dd0855e0e27e42066a78ecf5e380bd5ad5984e7cab6e476cb9b4b58 |
| [Check if you need to file a tax return \| Internal Revenue Service](https://www.irs.gov/individuals/check-if-you-need-to-file-a-tax-return) | 网页主文1—145全文实读 | 7a702a1e8eecec8e9bca8da0dddd4b6a7ff68cca2062d80b0afe7b2de321e55b |
| [Gather your documents \| Internal Revenue Service](https://www.irs.gov/filing/gather-your-documents) | 网页主文1—103全文实读 | 5d64370677a42ac292601ee71abec064907303eb7309e65f227773c0fc4e92cf |
| [Topic no. 254, How to choose a tax return preparer \| Internal Revenue Service](https://www.irs.gov/taxtopics/tc254) | 网页主文1—41全文实读 | 69a8ea147906bad4ed26126084820f9fc1126474068679fd80b69cf2d19d7acd |
| [Understanding your IRS notice or letter \| Internal Revenue Service](https://www.irs.gov/individuals/understanding-your-irs-notice-or-letter) | 网页主文1—46全文实读 | 88c4de33f88d048254896ac8ab8da2207e94edaf6004a29a762235ace1466fed |
| [Who Is A United States Person? \| FinCEN.gov](https://www.fincen.gov/who-united-states-person) | 网页主文1—5全文实读 | 2f5fd708ad5c4759e45b1695e6ae5872182e6c6832bd8ccce6a630049a023150 |
| [Reporting Maximum Account Value \| FinCEN.gov](https://www.fincen.gov/reporting-maximum-account-value) | 网页主文1—11全文实读 | 779b2749dd435028abc85f8aea6483093331d9b1053a1dc25bd53568ef1b8eeb |
| [Due dates: personal \| FTB.ca.gov](https://www.ftb.ca.gov/file/when-to-file/due-dates-personal.html) | 网页主文1—137全文实读 | b9c00f9923bc5c99e2e3fd6a7f9383d42784eb17c9017c983b26142d5bbb81c8 |
| [Extension to file \| FTB.ca.gov](https://www.ftb.ca.gov/file/when-to-file/extension-to-file.html) | 网页主文1—52全文实读 | 4d43047618b7eb527f54903f36eca1fb028794cdb386fe18914d2a655d2e09eb |
| [Capital Gains - My DOR help \| Washington Department of Revenue](https://dor.wa.gov/manage-business/my-dor-help/capital-gains-my-dor-help#fileextension) | 1495行；148—216延期、709—788更正完整实读，其余流程没有认全文 | 393d3c23a01dfe2b443d26d4942d0325d56331fc3884571a71d825d18bd82351 |
| [Filing past due tax returns \| Internal Revenue Service](https://www.irs.gov/businesses/small-businesses-self-employed/filing-past-due-tax-returns) | 网页主文1—75全文实读 | 1d56a2943ccf6e03d8a1f2dab768e1061947264c05d3ea8f33424bc39b2801cf |
| [Topic no. 304, Extensions of time to file your tax return \| Internal Revenue Service](https://www.irs.gov/taxtopics/tc304) | 网页主文1—37全文实读 | 85f973cad0b472ecc7d7c339cce9172872f2391d92c2325ac07abb1182065726 |
| [About Form 4868, Application for Automatic Extension of Time to File U.S. Individual Income Tax Return \| Internal Revenue Service](https://www.irs.gov/forms-pubs/about-form-4868) | 网页主文1—23全文实读 | f135ee9e77d1ef7a978654e88ca5c16af17a84ecd76a2c7e5321cd771c6c4e97 |
| [2025 Form 4868](https://www.irs.gov/pub/irs-pdf/f4868.pdf) | 2025 Form4868，2025-10-01创建；4物理页仅1／2完整版式文本实读，3／4未读 | 36c7607db08ff469ed4e5df89e27ca90f29023c7cd6ca77c69343045e8f33d29 |
| [FinCEN FBAR Line Item Filing Instructions，2017 v1.4](https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf) | 当前提供2017 v1.4说明，22物理页；实际完整1／2／4—6，7—22未读，3未读 | 8a92baf0824e117225239aa33cc56b9608f22017fb357c0a8910daea89acb7d4 |
| [Self-employed individuals tax center \| Internal Revenue Service](https://www.irs.gov/businesses/small-businesses-self-employed/self-employed-individuals-tax-center) | 网页主文1—115全文实读 | d7eb498afd9c0feb69a68a689960778ea24a9cc4636994ebdc330ada2480af23 |
| [Foreign currency and currency exchange rates \| Internal Revenue Service](https://www.irs.gov/individuals/international-taxpayers/foreign-currency-and-currency-exchange-rates) | 网页主文1—38全文实读 | 16d4280cfde563ef410768c0855d2c594f844f58ee84972c56d1c647e842808e |
| [Change or amend a filed return](https://www.tax.ny.gov/pit/file/amended_return.htm) | 网页主文1—61全文实读 | 7031c108ddc6b80ecf2cc0db014d945db9811f3fe881fc558a34d63e6e9b14b3 |
| [2025 Instructions for Form IT-203, Nonresident and Part-Year Resident Income Tax Return](https://www.tax.ny.gov/forms/current-forms/it/it203i.htm) | 当前URL实际2025说明4400行；3589—3608更正及90日、表件分支完整实读 | 0ac4472eacc1025d081525864d09e421893e2bd5505eb27726d0f3f032406ca1 |

## 2026-10-13 独立事实返回：两处1040NR引用URL

static_editor独立事实真正取得年份后缀URL404，指出正文两处链接与作者实际研究的canonical不同。原作者root没有据其请求结果或替代200认规则实读；先逐具体路径核git忽略，2026-10-13 10:58:35 UTC正常TLS本人新取 `https://www.irs.gov/instructions/i1040nr2025`，实际404且标题404，原始SHA `b65ad0452c446bac264bab085b37034da9b48de85466f425e6f52a2500475c84`，没有读到该失效路径的2025规则。此前正文的年份后缀并未由本人实际打开，不能当作已核有效链接；初稿两SHA没有独立PASS。

本人同时正常TLS新取 [canonical Form1040NR说明](https://www.irs.gov/instructions/i1040nr)，实际200／标题Instructions for Form1040-NR(2025)，4254行，原始SHA `ff42447ede17ad58282baac072edf020c52ae3add2c8b03409a70aadf7bcb76d`。该新原始字节与首轮原件不同，清理后的完整4254行文本则逐字节精确相同，两者文本SHA均 `b495addb181ab899e16d21bc978a90a30684f86710c399054954d1bf2dac0cb1`；文本一致不是阅读替代，本人又实际完整读805—852、984—1055、1085—1110、1127—1160、1177—1212，确认采用的义务／居民／日期／dual-status段。首轮其他采用段的实际阅读保留，未认新4254行全文或所有表件及外链都重读。

正文唯一操作为两处失效URL替换成上述canonical，其他规则、日期、数字、字词及frontmatter逐字不变。落盘后本人实际完整读新136行1—45／46—90／91—136，无截断；在内存逆换两URL精确恢复旧完整正文 `12f95928a810ad4e1885b3bb37250c327966c17ac122c49e0699f1cca871d429` 与旧整文件 `6c26f667dda0a0b96beb7119edb29901dd0d34f17904d3230eeef6e3a514e698`。当前完整正文SHA `6ca184bce421c07a203b09640178a0da16e31bb5fefcb8ce7397b089e571e70a`／整文件 `046cbfb74f5d5ea65a465f2e95d3733a1537b474f622c139ebf7167d13b3d91d`；作者冻结不作PASS，交回static_editor继续最终独立全文重绑。metadata仍written／draft true／verified及reviewed_by空，没有候选或工程结论。
