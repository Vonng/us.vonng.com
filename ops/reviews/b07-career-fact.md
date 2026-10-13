# B07 求职、录用与入职：独立事实审

结论：**PASS**。审阅者 static_editor，2026-10-13。审阅正文 `content/book/work/career/job-search-onboarding.md`，page_id `work.career.job-search-onboarding`。

最终正文 SHA-256：`f5c8738b3677bb8dca0c3ba73dcdf2d9c01f668360ff18de15ba570c618e42bc`。算法为 UTF-8 文件 `split('---', 2)[2]`，保留第二道 frontmatter 分隔线后空行和末尾换行。审阅时整文件 SHA-256：`e5410aac4016ac31ac04a8e7ff60ccb747eb6aec70e98ddb87b12597929e3183`。

作者 banking_fact；独立事实审 static_editor；第三人静态审由 root 后续完成。审阅者没有参与本稿正文、地图或作者证据写作，没有修改正文或元数据。本结论只覆盖上述正文版本和下列实际回源范围，不代替静态审、候选元数据安装、构建或渲染验收。

## 实际审阅与修订重绑

已全文读取正文、`ops/maps/job-search-onboarding.md`、`ops/evidence/job-search-onboarding.md`，核对对象为美国普通成年私营雇员，以及联邦手续与四州采用的州分支。作者的来源清单只用于定位，我重新请求原 URL 并读取下列主管机关或原发布者的内容；没有把其缓存、已读身份或 HTTP 200 当成独立核验。

初读正文 SHA 为 `0a697014bc23f2b89ce9e0ed7174030f41abd02880a3ed63e6687171d55bc982`，整文件为 `3f935d9b5c679b86153900515ef3827485dbf3d0cbb2dc13815031868daf895e`。root 通读后要求作者拆清申请段 SSN 与银行账户资料用途。作者实际修改为“SSN 在核实过的背景调查或工资手续中按用途提供；银行账户资料在核实后的工资入账手续中提供。履历里不放这些号码。”我已实际读取新句并重算最终 SHA；将这一句换回已实读旧句后，正文摘要精确回到原冻结 SHA，确认正文只有这处变化。该区别与独立实读的 FTC 隐私段一致；作者地图与证据已改绑新 SHA 并保留历史。旧 SHA 不承载最终 PASS。

## 实际读取的原始来源

下表的日期为页面或文件明确显示的版本日期；未见日期时不推定更新日。web 是本轮工具实际返回的原文，普通 HTTPS 是审阅者本轮重新请求后读取的正文。二者发生差异时各自记录。

| 来源 | 审阅者实际读取、版本和核对范围 |
|---|---|
| [CareerOneStop：履历](https://cloudfront.careeronestop.org/JobSearch/Resumes/resumes.aspx) | 最初普通 HTTPS 超时、web 直接打开失败；后来从面试页的真实 Resumes 链接点击成功，实读主文 L38–97：相关经验、真实内容、岗位用语、按要求提交与检查预览。另实读官方 [Top section](https://cloudfront.careeronestop.org/JobSearch/Resumes/ResumeGuide/top-portion-of-resume.aspx) 的联系信息/技能 L52–83，及 [Work experience](https://cloudfront.careeronestop.org/JobSearch/Resumes/ResumeGuide/work-experience.aspx) 的经历信息 L38–43 和 General tips L61–66。未见正文更新日；不采用扫描秒数、AI 推广或 ATS 成功预测。 |
| [CareerOneStop：American Job Centers 视频逐字稿](https://cloudfront.careeronestop.org/Videos/JobSearchVideos/american-job-centers-video.aspx) | web 实读完整逐字稿 L39–46，DOL 赞助信息 L20/109：免费求职、履历与面试练习、设备、预约及按资格分流。没有认定个人训练资助资格。 |
| [CareerOneStop：面试准备](https://cloudfront.careeronestop.org/JobSearch/Interview/get-ready.aspx?frd=true) | web 实读主文 L41–74 六步：研究、真实例子、职责/训练问题、澄清与跟进。正文模拟表达均明示教学虚构，不用作真实录用结果。 |
| [CA EDD：Job Seeker Information](https://edd.ca.gov/en/Jobs_and_Training/Job_Seeker_Information) | 普通 HTTPS 200，实读主文包括 CalJOBS、AJCC、求职活动、训练与 Access Employment Services；入口、服务和免费协助相符。未采用其资助金额或 TAA/WOTC 特别资格。 |
| [NY DOL：Career Centers](https://dol.ny.gov/career-centers)、[Career Development](https://dol.ny.gov/career-development) | 两页普通 HTTPS 200；实读定位器的 Region/County 筛选与虚拟协助说明，及 Career Development 主文的岗位探索、履历和面试工具。未逐一核全州地址、数量或当日营业安排。 |
| [NY DOL：语言服务 FAQ](https://dol.ny.gov/faq-language-access-non-english-speaking-new-yorkers) | 普通 HTTPS 200，实读完整 FAQ，尤其免费口译覆盖 DOL 与合作机构 Career Centers、语言服务不足的 complaint form。正文没有将公共机关语言协助外推为所有私人面试的外语口译义务。 |
| [WA ESD：WorkSource](https://esd.wa.gov/jobs-and-training/find-job/job-seekers-get-help-worksource) | 普通 HTTPS 200，实读完整主文：免费技能/岗位/履历/申请指导、设备、定位入口及部分站点服务较少。没有采用工作人员可代填申请或可批准个案失业金的说法。 |
| [TWC LMCI 资料页](https://lmi.twc.texas.gov/shared/publications.asp) | 普通 HTTPS 200，实读 Find Locations / Workforce Solutions Offices & Services 的实际链接，指向 `https://twc.texas.gov/directory-workforce-solutions-offices-services`。只核官方目录入口，不冒称读取 TWC 主站目录全部结果。 |
| [Gulf Coast Workforce Solutions：Job Search](https://www.wrksolutions.com/job-seekers/job-search) | 普通 HTTPS 超时，web 实读 L59–84：当地履历、面试、招聘活动及全州 WorkInTexas 数据库。另实读 [主页](https://www.wrksolutions.com/) 的 Career Office / Work in Texas 实际入口及 Houston 地区导航；没有逐一核本地办公室当天安排，未把 Gulf Coast 服务推广为得州所有办公室统一服务。 |
| [FTC：Job Scams](https://consumer.ftc.gov/articles/job-scams) | web 实读完整主文 L2–52；March 2023。付钱换岗位、假支票转出、礼品卡、包裹转寄、核实招聘方及付款后立即找付款机构/ReportFraud 的动作相符。正常 HTTPS 403，不当成已下载正文。 |
| [FTC：Employer Background Checks and Your Rights](https://consumer.ftc.gov/articles/employer-background-checks-and-your-rights) | web 实读主文 L2–45；August 2025。核外部报告的独立告知/书面授权、预决定材料、最终通知、决定后 60 日免费报告、纠错，以及 L39 的 SSN 与录用后银行入账资料区别。 |
| [FTC/EEOC：What Employers Need to Know](https://www.ftc.gov/business-guidance/resources/background-checks-what-employers-need-know) | web 实读主文，重点 L12–54；February 2014。独立书面告知、书面授权、预不利决定的报告和 FCRA 权利摘要、最终通知与 60 日额外免费报告。正文没有将 60 日写成回应期限或岗位保留期。 |
| [CFPB：Background screening reports](https://www.consumerfinance.gov/documents/10037/cfpb_background-screening-report_handout_2021-08.pdf) | web 实际完整解析两张物理页；文件名为 2021-08。独立告知/授权、特定卡车行业例外、预决定与最终通知、书面纠错、副本证明、通知雇主和 CFPB/FTC 求助均实际读到。另普通 HTTPS 跟随到官方 files 主机成功取得真两页 PDF，指纹见后表；正文不写报告调查期就是雇主等候期。 |
| [EEOC/FTC：求职者的背景调查权利](https://www.eeoc.gov/laws/guidance/background-checks-what-job-applicants-and-employees-should-know) | 普通 HTTPS 200，实读主文 Questions / Background Reports / Negative Background / Where to Go；Issue Date 2014-03-11，EEOC-NVTA-0000-37。一般背景提问、外部编制报告与反歧视制度被正确分开；没有使用其旧电话或旧链接替代当前入口。 |
| [CA CRD：Fair Chance Act factsheet](https://calcivilrights.ca.gov/wp-content/uploads/sites/32/2025/07/Fair-Chance-Act-Factsheet_English.pdf) | 普通 HTTPS 200 真 PDF，pypdf 实读全部三张物理页；June 2025。至少 5 人私营雇主、先条件录用、个别评估、书面预撤回/报告、收到后至少 5 个工作日及准确性争议额外安排、最后通知和法定/医疗等例外相符。正文没有推广为全部职位或使用其七年记录说明涵盖全部制度。 |
| [WA AG：Fair Chance Act](https://www.atg.wa.gov/fair-chance-act) | 普通 HTTPS 200，实读完整主文含 Hiring Processes 和脚注例外。2025 修法对 15 人及以上雇主 2026-07-01 生效，15 人以下为 2027-01-01；条件录用/核其他资格的顺序、指出所用记录、至少保留岗位两个工作日及无人监督接触儿童/弱势者、执法与法律背景限制等例外均与正文一致。 |
| [CA DIR：Equal Pay Act / Pay Transparency](https://www.dir.ca.gov/dlse/california_equal_pay_act.htm) | 普通 HTTPS 200；实读合理请求 applicant pay scale、招聘披露、15 人计数/至少一人在州内、职位可在 CA 履行及 pay scale 定义，另读相关 salary-history 与费用说明；页尾 August 24, 2026。正文采用的门槛、地理范围和合理请求相符。 |
| [NY DOL：Pay Transparency](https://dol.ny.gov/pay-transparency)、[FAQ](https://dol.ny.gov/pay-transparency-act-frequently-asked-questions) | 入口 web 实读 Overview / 私营至少 4 人及投诉范围 L66–104；FAQ 普通 HTTPS 实读 When applies、Advertisements、Range of Pay 开头。至少部分州内履行岗位、固定金额及临时派遣替第三方招工例外相符；正文没有外推未写的州外远程报告链。 |
| [WA L&I：Equal Pay & Opportunities Act](https://www.lni.wa.gov/workers-rights/wages/equal-pay-opportunities-act/) | 普通 HTTPS 200，实读 Job Applicant Protections / Job Postings / Required information：至少 15 人、工资范围或固定金额、福利和其他报酬概述。当前页已含 2025 固定额与更正程序，正文没有沿用“只能列区间”的旧说法。未采用损害赔偿或更正等待期。 |
| [EEOC：Job Applicants and ADA](https://www.eeoc.gov/laws/guidance/job-applicants-and-ada) | 普通 HTTPS 200，实读 Introduction 与 Q1–8；Issue Date 2003-10-07。至少 15 人私人雇主、合格残障申请者、面试合理便利、有效替代、重大困难/费用例外及尽早请求，均有原文支持。 |
| [IRS：W-4](https://www.irs.gov/forms-pubs/about-form-w-4)、[Notice 1392](https://www.irs.gov/forms-pubs/about-notice-1392) | 两页普通 HTTPS 200，实读主文与 current revision 入口；页尾分别 2026-09-10、2026-03-30。W-4 给雇主作联邦工资扣缴、非居民外籍雇员有补充说明相符；未逐行读表格 PDF 或为个人计算扣缴。 |
| [USCIS：EAD](https://www.uscis.gov/green-card/green-card-processes-and-procedures/employment-authorization-document) | 普通 HTTPS 200，实读开头工作依据、永久居民与因身份为特定雇主工作者无须另申请 EAD；页尾 2025-10-30。正文没有以 SSN 或在美居住推定获准为某雇主工作。未重核学生或其他身份个案授权。 |
| [USCIS：I-9 官方入口](https://www.uscis.gov/i-9) | 普通 HTTPS 200，实读全文，包括 Edition Date、Where to File、Special Instructions；Last Reviewed 2026-06-03，现行 Edition 01/20/25、expiry 05/31/2027。正文没有写只能用某一个既有版，也没有要求员工将 I-9 交 USCIS。 |
| [USCIS：I-9 说明](https://www.uscis.gov/sites/default/files/document/forms/i-9instr.pdf) | 普通 HTTPS 200 真 8 页 PDF，pypdf 实读物理第 1–6 页全部；01/20/25、expires 05/31/2027。首日 Section 1/先接受录用、其后三个工作日/少于三日首日、周一至周四示例、A 或 B+C 的员工选择、Supplement A、可接受回执/正式延长、合理真实性/退回原件、DHS 替代程序、非 E-Verify SSN 自愿/ITIN 不可填、E-Verify List B 照片和待号仍可工作均相符。第 7–8 页没有作为已读细则登记。 |
| [USCIS：I-9 表格与清单](https://www.uscis.gov/sites/default/files/document/forms/i-9.pdf) | 普通 HTTPS 200 真 4 页 PDF，实际读物理第 2 页完整文件清单；Edition 01/20/25。护照/永久居民卡/EAD、州驾照加无限制 SSN 卡、限制性卡排除、官方延长、组合文件及回执边界相符。未填写个人表件。 |
| [DOJ IER FAQ](https://www.justice.gov/crt/iers-frequently-asked-questions-faqs) | 普通 HTTPS 200，Updated 2025-04-18；实读 General、Filing a Charge、worker hotline/免费语言服务、文件选择、payroll 与 I-9 用途、待 SSN、E-Verify mismatch 期间不得解雇/停职/限制工时及人数/国籍/口音分流相关段。热线 1-800-255-7688、180 日 charge 相符；正文没有保证所有非公民均获相同 citizenship-discrimination 保护。未采用其中旧 TPS/特定入境回执日期写现行资格。 |
| [E-Verify：Mismatch Overview](https://www.e-verify.gov/employees/tentative-nonconfirmation-mismatch-overview) | 普通 HTTPS 200，实读完整主文，Last Updated 2022-09-15。第十个联邦政府工作日前告诉雇主是否采取行动是决定/通知期限；正文正确区别于在该日完成全部资料更正。没有操作实际案件。 |
| [EEOC：Time Limits](https://www.eeoc.gov/time-limits-filing-charge) | 普通 HTTPS 200，实读主文：一般 180 日、同类州/地方执法通常 300 日、年龄例外、联邦申请者区别、内部争议/仲裁等一般不延长及每起事件另计。正文以普通私营雇员和尽早询问本人期限表达，没有承诺咨询或内部回复暂停期限。 |
| [CFPB：投诉入口](https://www.consumerfinance.gov/complaint/) | 普通 HTTPS 200，实读公开首页产品范围（含其他个人消费报告）、先向报告公司争议、材料和后续说明。只核继续入口，没有创建账户、填写或提交。正文已有先书面纠错步骤。 |
| [FTC：ReportFraud](https://reportfraud.ftc.gov/) | 普通 HTTPS 200 的应用壳及 web 空文本；没有读取后续表单。该真实报告入口由本轮实读 FTC Job Scams 主文直接提供，正文只链接继续报告，未声称提交成功或可得个人退款。 |

## 关键结论

1. 工作授权、SSN、I-9 与 E-Verify 分开处理。I-9 的两段期限与首日例外、员工选文件、受限制 SSN 卡、待号入职和暂不确认程序均已独立读到官方依据；一般流程没有被写成个人身份获准工作的判断。
2. FCRA 三步程序按外部背景报告的普通情形书写，包含特殊卡车行业授权例外、预决定材料、最终通知、纠错和 60 日免费报告。CA/WA 州程序的覆盖人数、生效日期、回应机会与例外保留在会改变申请行动的位置。
3. 四州公共就业入口、免费/本地服务边界及三州采用的招聘薪资披露断言，均有实读的一手资料支持。没有写全国统一训练资格、工资周期、福利生效或最低工资金额。
4. 申请、录用核对、入职、第一班/第一笔工资和受阻后的继续路径完整；模拟履历与英文跟进均标为教学虚构。SSN/银行用途修订已复核，不再把银行账户资料与背景报告混写。

## 失败、缓存与未核边界

- 下载前实际运行 `git check-ignore -v .cache/evidence/b07-career-fact/source-index.json .cache/evidence/b07-career-fact/i9-instructions.pdf`，均命中 `.gitignore:2:.cache/`。本轮请求元数据、原 HTML/PDF 和提取文本保存在该忽略目录；不会纳入 Git，缓存存在不等于读到内容。
- 本轮独立逐项请求正文的 32 个外部 URL，保留普通 HTTPS 状态、重定向、内容类型、SHA 和超时；保持 TLS 校验，没有采用作者代理或缓存代替实际请求。普通 HTTPS CareerOneStop 三页及 Gulf Coast 求职页超时；web 逐字稿/面试/求职主文成功。履历总页初次 web 失败，最后从真实面试页链接点击成功，不能把初次失败抹去。官方 Resume Guide 已实际读到，用于补充通用履历建议。
- FTC 三页普通 HTTPS 均 403，web 主文实际可读，所采断言以实际 web 主文为准。TWC LMCI web 打开超时，但普通 HTTPS 实际取得官方目录链接；Gulf Coast Office 定位页 web 超时，没有据此确认任何具体办公室。ReportFraud 的后续表单未读，FTC 主文直接支撑入口。没有绕过挑战、登录账户、查询个人记录、提交表单或联系机构。
- 本轮 CFPB PDF 实际成功重定向至官方 `files.consumerfinance.gov/f/documents/cfpb_background-screening-report_handout_2021-08.pdf` 并下载；这与作者当时失败并不矛盾，审阅者只记录自己的请求结果。实际 PDF 指纹如下，PDF 内容采用范围见上表。

| 本轮 PDF | 页数 | 二进制 SHA-256 |
|---|---:|---|
| CFPB 背景报告 | 2 | `95a277aa241d1486c3c5145503527bde0cb0b821b4bf09a23f10be1d3b74b3f5` |
| CA CRD 事实表 | 3 | `0e7e54a5d99e6f25965b7c8ea931315b4c1f43b2d0a08879ce1a7a063cc30839` |
| USCIS I-9 说明 | 8 | `c66c3818fbecbfb87b5f0560f4dfd4086905daf72ca29dba15ce4c8d49dc4ca3` |
| USCIS I-9 表格 | 4 | `780f348c34df694bb0b4dbbfaf9f22b99b9757b80d16a37ba89aadf069597281` |

- 未核个人移民/工作资格、学生授权、未成年人、独立承包、政府职位、全部职业执照和地方招聘法、犯罪记录底层法院更正、个人申诉期限起算/中止、具体雇主福利条款或当日办公室服务。这些事项正文提示按实际岗位、项目和本人文件确认，没有作统一资格或结果承诺。
- 10 个绝对站内目标真实存在，实际核其 frontmatter 均为已集成 `draft: false` / `verified: 2026-10-13`。本站银行、号码、身份、税务、工资、保险/网络、语言和法律帮助作为详细操作入口；本轮不重新核其全部历史事实，也不冒用其历史审阅身份。
- 最终正文与作者地图/证据的 SHA 已实际核对一致；元数据仍为 `written` / `draft: true`、`verified` 与 `reviewed_by` 空。只新增本审阅文件，没有修改其他代理记录、公共入口、共享账本或工程，没有构建、渲染、同步或提交。
