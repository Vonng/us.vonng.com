# B04 医保衔接：独立事实审

- 审查正文：`content/book/people/health/coverage-changes.md`
- 作者：health；独立事实审：civic；查阅日期：2026-10-13。
- 结论：**PASS**。在正文所限定的普通失去雇主保险、跨州搬家和四州办理范围内，未发现需正文返修的事实错误。须继续交 root 第三人静态审及集成验证，本记录不代表已发布。
- 绑定最终正文 SHA-256：`54f796e916ab7d1d0cc19fca99e8ffc8919a6bff161674e547ce17cee5da3943`。按 UTF-8 `split('---', 2)[2]` 计算；没有修改正文、作者地图或作者证据。
- 复核过程：初审绑定 `1d44122b3a07b356bea7d94dee233430874512f917955dac32b373c8d1aaeaae`。作者随后依手机渲染建议将四州表合为“居住州／申请入口与需要核对的事”两列，本审重新逐行读取，全部事实、范围、日期和链接保留，结论继续 PASS，并绑定上述最终 SHA。
- 方法：独立打开下列官方网页或 PDF；普通公开 HTTPS requests 与 web 工具互补，TLS 校验保留，PDF 仅在内存由 pypdf 提取。作者证据用于发现入口，没有代替原文阅读；未登录、提交申请或联系第三方。

## 实际回源与定位

| 原文、版本及实际定位 | 独立核验结论 |
|---|---|
| [DOL Job Loss](https://www.dol.gov/agencies/ebsa/workers-and-families/protecting-retirement-and-health-benefits-after-job-loss)，公开 HTTPS 200，主文全部 | 另一雇主计划通常失保后 30 日请求，生效不晚于请求后下一月首日；与 Marketplace 60 日分开正确。EBSA 电话 1-866-444-3272 与正文一致。 |
| [DOL COBRA guide](https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/an-employees-guide-to-health-benefits-under-cobra)，公开 HTTPS 200；What Is COBRA、Covered Plans、Qualifying Events、Election Procedures、Benefits、Duration、Paying 全部相关段 | 上一历年多于一半典型营业日 20 人，含兼职折算；稿件保留“达到规定人数条件”，不把当日人数当测试。私营／州地方与联邦／部分教会边界、gross misconduct、18 个月及提前终止／延长均准确。 |
| 同一 [DOL guide](https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/an-employees-guide-to-health-benefits-under-cobra)，Election Procedures、Individual Election Rights、Maximum Premiums、Initial Payment | 60 日从 notice provided 与原 coverage loss 较晚起，不能改为实际收信日；首次至少 45 日；普通上限 102%，残障延长特殊；先 waiver 后撤回的起保可能不同，稿件已留正确边界。每名受益人独立选择、在职成员计划变化同步均有原文支持。费用段因首次工具输出截断，另行读取完整 Payments 段后才判定。 |
| [HealthCare.gov Job-based loss](https://www.healthcare.gov/have-job-based-coverage/if-you-lose-job-based-coverage/)，HTTPS 200，全部主文与 FAQ | 辞职／被解雇造成合格失保可有 SEP；全年收入含此前工资；配偶 offer 与新雇主等待期需区别；普通月初起保，不能追溯补全部空档。 |
| [HealthCare.gov SEP](https://www.healthcare.gov/coverage-outside-open-enrollment/special-enrollment-period/)，HTTPS 200，全篇 | 普通失保前后 60 日；Medicaid／CHIP 后 90 日；自愿取消／停缴与其他触发条件不同。正文使用“一般”而没有抹掉其他可触发例外，正确。 |
| [CMS September 2026 SEP webinar](https://www.cms.gov/marketplace/technical-assistance-resources/sep-overview-complex-case-scenarios.pdf)，56 页；实际第 6—11、15、17—29、37—42 页 | 第 7 页既往失保为选保次月首日、未来失保为旧保最后日所在月后首日；第 15 页说明各州 regular SEP 日期协调。第 6／37 页既往 60 日至少 1 日保障及外国／领地、联邦承认部落成员／ANCSA、无可用计划区例外；第 42 页搬迁后 60 日、不同新计划、旅游医疗临停不算。稿件与小林算例均准确。 |
| 同一 [CMS PDF](https://www.cms.gov/marketplace/technical-assistance-resources/sep-overview-complex-case-scenarios.pdf)，第 9—11 页正文和诉讼脚注 | 部分新 SEP 全面入保前核验被法院暂缓，失去 MEC 核验仍在。稿件仅要求按通知补件，没有把暂缓条款当全面现行义务。 |
| [HealthCare.gov COBRA switching](https://www.healthcare.gov/unemployed/cobra-coverage/)，HTTPS 200，全篇及条件表 | 普通到期、雇主不再补贴、仍在原 60 日期内等可转；自行嫌贵停缴一般不会产生新 SEP；先核准新起保，正确。 |
| [Medicare COBRA](https://www.medicare.gov/basics/get-started-with-medicare/medicare-basics/working-past-65/cobra-coverage)，HTTPS 200，全篇 | 工作相关 Part B 窗口不会因选 COBRA 延长；COBRA 在 Medicare eligible 但未加入时可能只付少部分；SHIP 指引与稿件保留边界正确。没有用本页替个案计算 Medicare 时间。 |
| [HealthCare.gov Unemployed](https://www.healthcare.gov/unemployed/coverage/)，HTTPS 200，全篇 | 预计全年家庭收入而非是否工作决定补助；affordable／minimum-value offer 可影响，即便不加入；报告新工作与收入。 |
| [HealthCare.gov Income](https://www.healthcare.gov/income-and-household-information/income/)，HTTPS 200，全篇 | 当前月与保障年度全年分别问；工资、州失业金等项目；变化更新、多领补助可能报税退还。正文没有错填年／月或给未核金额。 |
| [HealthCare.gov Moving](https://www.healthcare.gov/reporting-changes/when-you-move/)，HTTPS 200，全篇 | 跨州需新州申请选计划，旧市场计划不能仅改地址保留；州内更新可能换计划。正文没有把 Medicaid 或 Medicare 硬套成市场同一程序。 |
| [HealthCare.gov Medicaid/CHIP](https://www.healthcare.gov/medicaid-chip/getting-medicaid-chip/)，HTTPS 200，全篇 | 全年可申请、州决定资格、家庭可分流、州规则不同；项目与移民边界由州材料补足。正文不保证追溯、不把申请等于批准。 |
| [Covered California life changes](https://www.coveredca.com/enrollment/major-life-changes)，web 实读 L41—145 | 失去工作保险前后 60 日、Medi-Cal 后 90 日、搬迁和当地助手入口真实。正文表格与限定一致。 |
| [DHCS Help](https://www.dhcs.ca.gov/medi-cal/help/)，普通请求 403，web 实读 L313—431、495—501、589—615、675—686 | 跨州需申请新州，与跨县 ICT 不同；新申请冻结、旧有成员按规则续保、儿童孕产例外。没有把 Help 页其他旧段或未来年度细节引入正文。 |
| [DHCS Immigration status chart](https://www.dhcs.ca.gov/immigration-status-and-changes-to-medi-cal-eligibility/)，标 August 2026／valid through 2027-06-30；web 实读表格 L45—95 与尾注 | 身份类别差异、新旧成员不同、儿童／孕产／原寄养入口均吻合。正文“某些成人”合理避免把所有非公民一概冻结；没有宣称仅凭身份即可获批。 |
| [DHCS Federal Impact](https://www.dhcs.ca.gov/tracking-federal-impact-medi-cal-eligibility/)，2026-09-21 更新；web L49—110 | L55—56 明确 2026-10-01 联邦资金资格变化，受影响 members 获州资助 full-scope 至 2027-06-30。稿件限定已有成员，不扩大成所有新申请者；不拿年初方案推翻最新说明。 |
| [NY State of Health 首页](https://nystateofhealth.ny.gov/)，web 实读 L80—109、189—198 | specialenrollment 路径本审 web 和 HTTPS 均 403；使用同一官方机构首页实际正文补核：儿童、符合资格 Medicaid／EP 成人可全年申请，其他普通 QHP 按 OE／SEP；支持稿件这部分同义有限断言。未假装成功读取失败路径。 |
| [NY OAG guidance](https://ag.ny.gov/press-release/2026/attorney-general-james-issues-guidance-new-yorkers-facing-health-insurance)，2026-06-22；web L29—37、49—52 | 2026-07-01 高于 200% FPL 的原 EP 组失去资格，200%—250% 扩展被撤；有 NYSOH 与认证助手路径。稿件没使用已过期 9 月转换日期。 |
| [NYC311 Health Insurance](https://portal.311.nyc.gov/article/?kanumber=KA-02767)，web 失败后 HTTPS 200，Changes to the Essential Plan 及 Get Help 完整段 | 明确 as of July 1, 2026 已发生退出，独立事后确认 OAG 预告；没有把单人美元金额当全家阈值。 |
| [WA Healthplanfinder job loss](https://www.wahealthplanfinder.org/us/en/my-account/life-events/health-insurance-after-a-job-loss.html)，HTTPS 403，web 实读 L57—165 | 旧雇主覆盖最后一天为日期，前后 60 日，Apple Health 合格者全年、COBRA 到期／补贴结束与当地帮助。机构入口与稿件吻合。 |
| [HCA Apple Health changes](https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/what-changes-apple-health-mean-you)，HTTPS 200 全文 | 非公民改变 2026-10-01；SSI 禁令提醒，2027／2028 各后续时间标明；19—64、65+、LTSS 分流。正文没有提前施行未来工作／续保条件。 |
| [HCA noncitizen sheet](https://www.hca.wa.gov/assets/free-or-low-cost/hr1-noncitizen-fact-sheet.pdf)，June 2026；HTTPS 200 后内存实际读 3 页 | 10 月变化、儿童／孕期／产后例外，转 LPR 与五年豁免须分开；其他项目受限、年龄残障 Medicare 分流。须与后来的禁令一起读，稿件已做到。 |
| [HCA Court order announcement](https://www.hca.wa.gov/about-hca/news/announcements/court-order-protects-apple-health-coverage-more-800-washingtonians)，2026-10-01；HTTPS 200 全文 | 9 月 30 日 WA 西区初步禁令，保护收 SSI 且原本因本次规定于 10 月失保者。稿件没有扩大到所有难民／残障居民，正确。 |
| [HCA Apple Health Expansion](https://www.hca.wa.gov/about-hca/programs-and-initiatives/apple-health-medicaid/apple-health-expansion)，HTTPS 200 全文 | Enrollment limited／cap met 当前明确。不是所有 Apple Health 均满额。原页倒置 OE 日期与隐私概述疑似版本混杂，稿件没有采用这些细节。 |
| [TX HHS Health](https://hhs.texas.gov/services/health)，HTTPS 200 主文 | 正式引至 Your Texas Benefits，Medicaid／CHIP、老人残障与其他医疗路径。YTB 公开页一次 web 可识别、后续 web／HTTPS 错误，不能据此宣称实际申请已测试；HHS 与下条 PDF 足以交叉确认官方申请入口。 |
| [Texas Works Handbook A-240](https://fhb.hhs.texas.gov/handbooks/texas-works-handbook/a-240-medical-programs)，web 实读 L13—87、225—274 | 儿童、孕妇、父母／照顾亲属需满足全部条件，亲属与 dependent child 同住等；失业本身不自动成人 Medicaid。正文没有套用手册旧移民段或旧金额。 |
| [TDI 2026 Health Coverage Guide](https://www.tdi.texas.gov/healthguide/2026-texas-health-coverage-guide.pdf)，封面 2026，36 页；web 超时后 HTTPS 200，内存实际读物理第 11—12 页，即印刷第 9—10 页 | Individual insurance 常通过 HealthCare.gov；政府项目 YourTexasBenefits；儿童、孕妇、原寄养、残障与 65+，Medicaid 跨州规则／服务差异。正文“第 10 页”按印刷页正确。作者证据物理页偏移有一处小笔误，已另告作者修记录，不影响正文 SHA。 |
| [HealthCare.gov Complete enrollment](https://www.healthcare.gov/apply-and-enroll/complete-your-enrollment/)，HTTPS 200，全篇 | 首保费直接付 insurer、按其期限；账户核对起保和公司核验；没卡可询问。正文限定有保费计划，正确。 |
| [HealthCare.gov Appeals](https://www.healthcare.gov/marketplace-appeals/)，HTTPS 200，全篇 | 一般资格通知日期 90 日、可申诉 SEP／起保等决定、州自办入口另核；理赔拒付归计划申诉。正文没有把客服询问当正式申诉，也没有把 90 日套到四州全部项目。 |

## 最终范围检查

- 小林教学例：旧保 10 月 15 日结束，20 日选择普通失保 SEP，11 月 1 日起保；16—31 日空档与 CMS 表吻合，COBRA／Medicaid 仅提示核查，不保证追溯批准。
- 法域、人员和时间例外放在相关行动处：COBRA 计划覆盖与 gross misconduct，Marketplace 失保／搬迁不同窗口，NY 既往 EP 扩展终止，CA 新申请与旧成员，WA 非公民／SSI／满额区别。
- 正文提出网络、药物、转诊预授权重新确认，未承诺某具体计划必须接受旧批准；此部分是合理办理建议并依赖已完成的预约／网络页，不构造个案权益。
- 没有独立模拟私人账户、申请资格、计划付费、真实医生网络或诉讼全部案卷；这些不在本文断言范围。法院保护依据州主管 10 月最新实施说明，不把机构说明扩为对全国或全部类别的裁判结论。
- 2027 续保／工作条件、CA 2027-06-30 过渡终点、WA 新判令／名额、下一年度 Marketplace 政策为必须回源的维护触发。不得只更改 verified 日期沿用本次结论。
