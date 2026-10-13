# 失业或搬州后怎样接上医疗保险：作者证据

- 正文：`content/book/people/health/coverage-changes.md`
- 作者：`/root/health`；实际查阅日期：2026-10-13；初稿 written / draft true，审阅字段空。
- 方法：下列采用来源均实际读取官方网页正文或 PDF 原文。web.open 成功后阅读相应完整规则段；因 web 403 而改用普通 HTTPS `urllib.request.urlopen` 的来源单列。TLS 校验保留，未登录个人账户、提交申请或联系第三方；PDF 内存读取，未将下载文件保存进仓库。
- 搜索结果仅发现入口；无正文成功读取的来源没有作为证据。冻结正文 SHA-256：`54f796e916ab7d1d0cc19fca99e8ffc8919a6bff161674e547ce17cee5da3943`（`split('---', 2)[2]`，UTF-8）。本记录不是独立事实审。

## 联邦行动链

| 来源与实际定位 | 实际读到的内容 / 采用范围 | 适用条件与复核触发 |
|---|---|---|
| [DOL：Protecting Retirement and Health Benefits after Job Loss](https://www.dol.gov/agencies/ebsa/workers-and-families/protecting-retirement-and-health-benefits-after-job-loss)，Health Benefits / Special Enrollment in Another Group Health Plan / COBRA 全段；web 403，普通 HTTPS 200，BeautifulSoup 读正文 | 别的雇主团体计划失保后通常 30 天请求特别加入、下月第一天前生效；合格 COBRA 事件、20 人计划、60 天较晚起点、追溯衔接、总保费加管理费；EBSA 1-866-444-3272 | 不是所有就业计划都受同一法；正文把普通失去工作保险与 Medicaid 失保、Medicare 分开。联系方式或程序变化重查 |
| [DOL：A Worker’s Guide to Health Benefits Under COBRA](https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/an-employees-guide-to-health-benefits-under-cobra)，web 实读 Coverage / Qualifying Events / Notice and Election / Paying / Duration / Alternatives（正文约 L137–472） | 上一历年一半以上通常营业日 20 人、兼职折算；私营与大部分州地方计划，联邦 / 部分教会不同；严重不当行为排除；合格受益人独立选择；保障与同类在职成员相同并随其调整；18 个月及延期、提前结束；普通 102%、残障延期可 150%；选保至少 60 天从 notice provided 或原保障终止较晚者；首次付款至少 45 天；先 waive 后撤回可能不完全追溯 | 正文不承诺所有人有 18 个月、不假定通知收到日等于提供日，不把 102% 适用于残障延期。未穷举 29 / 36 个月条件和州 mini-COBRA，不用其期限安排读者行动。计划年度累计额要求核查，未断言跨计划自动继承 |
| [HealthCare.gov：失去工作保险](https://www.healthcare.gov/have-job-based-coverage/if-you-lose-job-based-coverage/)，web 实读 Options 1/2 与所有 FAQ（L17–87） | 辞职 / 被解雇造成实际失保均可能 SEP；60 天；月初生效与 March 7→April 1 原例；年内离职前收入须计；配偶雇主邀请与补助、新工作等待期 | 原页 FAQ“下月”不能误写为过了一个月才选也追溯；用 CMS 生效表补足。正文小林 10 月例为作者教学虚构，无真实个人与金额 |
| [HealthCare.gov：Special Enrollment Period](https://www.healthcare.gov/coverage-outside-open-enrollment/special-enrollment-period/)，web 实读 Loss / Moving / Other circumstances / Documents（L16–156） | 合格失保前后 60 天；失去 Medicaid / CHIP 后 90 天；自愿取消、未付保费排除；不合格保险不生成同样失保窗口；搬迁而非旅游治疗；部分 Medicaid 迟拒可触发 | 正文一般 60 天明确普通失去工作保险；90 天不是所有 SEP 通则。未来年度 SEP、诉讼、各州补件不同须复核 |
| [HealthCare.gov：Unemployed coverage](https://www.healthcare.gov/unemployed/coverage/)，web 实读全文 | 家庭和全年预计收入决定补助而非是否工作；市场申请可转州项目；新的 affordable / minimum value 雇主 offer 影响 PTC | 正文没有填年度 affordable 比率，也不暗示所有收入 / 身份类别都可得补助；新工作与保障可用日期分开 |
| [HealthCare.gov：收入](https://www.healthcare.gov/income-and-household-information/income/)，web 实读全文，尤 L18–26、55–102、106–113 | 问当前月收入和预计全年；工资 / 失业金等纳入、受抚养人收入有报税义务条件；应更新，可能退还多领补助 | 正文不枚举 MAGI 表格行号或跨年度税率；没有将当年月收入与全年概念混合。全年与 Medicaid 各项目期间不能互推 |
| [HealthCare.gov：COBRA 转市场](https://www.healthcare.gov/unemployed/cobra-coverage/)，web 实读全部条件表与 FAQ | 正常耗尽 COBRA、雇主贡献或政府补助结束、仍在原失保 60 天期内等可有 SEP；自愿取消 / 停缴一般没有新 SEP；开放投保另论；等确认新保障日期再停 | 正文未让读者通过停缴制造事件，也未告诉读者错过期限后必能延长 |
| [CMS：Special Enrollment Periods, SEP Verification, and Complex Case Scenarios Webinar](https://www.cms.gov/marketplace/technical-assistance-resources/sep-overview-complex-case-scenarios.pdf)，封面 September 2026；web 实读 PDF 第 6–11、15、17、37–42 页（PDF 索引减 1） | 第 7 页：past loss 为选保次月初，future loss 为旧保结束月后月初；第 15 页自 2025 各州常规 SEP 生效日期一致；搬家新主要住址获得不同计划，之前 60 天至少 1 天保障；境外 / 领地、特定部落 / ANCSA、原服务区无计划三组例外；搬后 60 天；非旅游医疗临停；旧市场终止可安排日期 | 第 9–11 页附诉讼暂缓：不能仅摘“新增各类 SEP 入保前核验”而漏脚注。正文只要求按具体资格通知补件，未推断所有 SEP 均需同样核验。截图/图表未用作证据，采用可解析文字条款。若法庭或新年度政策变化复核 |
| [HealthCare.gov：搬家](https://www.healthcare.gov/reporting-changes/when-you-move/)，web 实读全文 | 跨州不能保留旧市场计划，去新州建申请并选；同州地址更新；首保费完成 | 同保险公司不等于同计划；不是 Medicare 全国保障迁移规则。没有要求州 Medicaid 申请等到原案关闭后才提交 |
| [HealthCare.gov：Medicaid / CHIP](https://www.healthcare.gov/medicaid-chip/getting-medicaid-chip/)，web 实读 L18–131 | 逐州规则、全年申请、家庭分流、市场转州、州决定通知；移民联邦资助范围和州儿童孕妇差异；某些有限保障与 PTC 情形不同；拒后可查其他市场选择 | 正文不把申请等同批准、不保证追溯，也不承诺 Medicaid 拒绝本身永远触发 SEP；没有写“有 Medicaid 字样必不得任何补助”的过宽规则。网页一般三个月追溯未采用，2027 时限已有变化 |
| [Medicare：COBRA coverage](https://www.medicare.gov/basics/get-started-with-medicare/medicare-basics/working-past-65/cobra-coverage)，web 实读 L10–37 | COBRA 不延长工作相关 Part B 特殊加入期限；Medicare eligible 未投保时 COBRA 可只付少部分；SHIP；政府 / 私营不同联系人 | 正文未给个人决定、未展开 8 个月算日、Medigap / Medicare Advantage / ESRD 特例；须另页完整研究 |
| [HealthCare.gov：完成投保](https://www.healthcare.gov/apply-and-enroll/complete-your-enrollment/)，web 实读 L17–58 | 首保费直接付保险公司、按其说明期限；账户查看起保、保险公司核验；没卡问保险公司 | 正文限有保费计划，未说 $0 保费须凭空交钱。支付时间、有效期等由保险公司确认 |
| [HealthCare.gov：What can I appeal?](https://www.healthcare.gov/marketplace-appeals/)，web 实读全文，L18–22、24–58、64–84 | 一般资格通知日期起 90 天；资格、SEP、起保日可诉；州自办市场有自己的入口；要求补件先补；保险公司理赔不走同一资格申诉 | 正文限定 HealthCare.gov，一般期限不套所有州 / Medicaid / 保险理赔；没有断言客服咨询中止期限 |

## 四州实际入口与 2026 年会改变行动的差异

| 来源与实际定位 | 实读与采用 | 边界 / 更新触发 |
|---|---|---|
| [Covered California：Major life changes](https://www.coveredca.com/enrollment/major-life-changes)，web 实读 event table、Help / FAQ 标题（L41–135） | 失工作保险前后 60 天；失 Medi-Cal 后 90 天；搬迁 60 天并可联系提前报告；Certified Enrollers 实际入口 | 折叠 FAQ 答案未全部呈现，没有以未读答案推断特殊细则。未采用下一年度开放投保日期 |
| [DHCS：Help](https://www.dhcs.ca.gov/medi-cal/help/)，web 实读资格、搬家 / Reporting changes（L461–615）、冻结问答（L675–686） | 跨州申请新州，跨县 ICT；某些成人 2026-01-01 新申请冻结、原有成员续保不同；儿童孕产规则 | 正文没有将 90 天续保补件宽限写成任何断保均能恢复。帮助手册其他资产 / 牙科 / 工作残障保费段未采用，存在版本混杂须另核 |
| [DHCS：Immigration Status and Changes to Medi-Cal Eligibility](https://www.dhcs.ca.gov/immigration-status-and-changes-to-medi-cal-eligibility/)，web 实读整个表和 Important Notes（L42–106）；正文自注 August 2026、有效至 2027-06-30 | 身份各行、LPR 等待期、PRUCOL 等并非一律冻结；未列成人原有保留；未满 19 儿童、孕期及产后一年、18 岁寄养且未满 26 等继续入口 | 正文不把“undocumented”与所有无 SIS 类别随意画等号，写“某些成人”，让读者以表逐人核对。未采用 2027 牙科、保费金额与 FFS 细节 |
| [DHCS：Tracking Federal Impact—Medi-Cal Eligibility](https://www.dhcs.ca.gov/tracking-federal-impact-medi-cal-eligibility/)，web 实读正文；标明 last updated September 21, 2026，L55–56 | 2026-10-01 联邦资金资格收窄，受影响已有成员州资助 full-scope 至 2027-06-30 | 较年初 proposed budget PDF 更新；不能把联邦资金终止写成 CA 立即全面失保。页面公共负担 / 数据诉讼虽实际读到，正文不据此写移民法律结论；2027 续保、工作规则另需完整实施研究 |
| [NY State of Health：Special Enrollment](https://nystateofhealth.ny.gov/specialenrollment)，首轮 web 实读全文，尤 L84–101 和页尾申请提示 L169–178 | 特殊事件、非事件、电话 / 当地助手；Medicaid / Essential Plan / 儿童可全年申请；一般 60 天前或后按类型 | 页首仍有 2016 年日期，不能当当前开放投保安排；只采用现行事件和页尾项目说明。复查时 web / urllib 403，首轮确实取得正文且有定位。无登录/填表 |
| [NY OAG：Attorney General James Issues Guidance…](https://ag.ny.gov/press-release/2026/attorney-general-james-issues-guidance-new-yorkers-facing-health-insurance)，web 实读 June 22, 2026 公告 L24–53 | 7 月起高于 200% FPL 不能继续 EP；200%—250% 组退出，转市场与助手 | 未使用公告中的已经过去的 September 1 过渡节点作为当前办理日；该页金属层级粗略说明未采用 |
| [NYC311：Health Insurance](https://portal.311.nyc.gov/article/?kanumber=KA-02767)，web 实读 Changes to Essential Plan L62–66 / 申请帮助 L69–85 | 明确“as of July 1, 2026”原收入组已不再由 EP 覆盖，独立确认六月公告已实施；免费申请帮助入口 | 正文不填单人美元收入金额，避免家庭规模误用；2027 工作规则未据此展开 |
| [WA Healthplanfinder：Health insurance after a job loss](https://www.wahealthplanfinder.org/us/en/my-account/life-events/health-insurance-after-a-job-loss.html)，web 实读 L57–165 | 用旧雇主计划最后一天；前后 60 天、在结束月办；Apple Health 合格者全年；COBRA 到期 / 补贴停；免费助手及多语言 | 不把失去工作直接等于失去保障，不把可全年申请等于自动资格 |
| [HCA：What the changes to Apple Health mean for you](https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/what-changes-apple-health-mean-you)，web 403，HTTPS 200 全文实读 | 2026-10-01 非公民资格变化、9 月 30 日 SSI 法院例外；当前联系方式、19–64 / 65+ 分流；2027 / 2028 变化明列生效年 | 未来规则未误写成 2026 条件，正文年龄 / Medicare / LTSS 另行分流。2027-01-01 和后续判令为复核触发 |
| [HCA：H.R.1 noncitizen fact sheet](https://www.hca.wa.gov/assets/free-or-low-cost/hr1-noncitizen-fact-sheet.pdf)，web 403，HTTPS PDF 内存 pypdf 实读 3 页，June 2026 | p1 非公民变化、儿童孕期及产后保留；p2 LPR 调整与五年豁免；p3 更新情况、其他项目、年龄 / 残障 / Medicare 分流 | 六月单本没有九月法院保护，必须与下条一起读；正文未断言所有难民一定失保，也未给 RMA 4 个月等未展开的资格行动 |
| [HCA：Court order protects Apple Health coverage…](https://www.hca.wa.gov/about-hca/news/announcements/court-order-protects-apple-health-coverage-more-800-washingtonians)，web 403，HTTPS 200 实读全篇；2026-10-01 | 9 月 30 日 WA 西区法院初步禁令，保护领取 SSI 且原本此次失保者；州机构保存覆盖、通知 | 正文不扩大为所有非公民或所有残障人士受到保护；新判令、撤销或范围变化立即复核 |
| [HCA：Apple Health Expansion](https://www.hca.wa.gov/about-hca/programs-and-initiatives/apple-health-medicaid/apple-health-expansion)，web 403，HTTPS 200 全文实读；另初期实读 [enrollment cap 公告](https://www.hca.wa.gov/about-hca/news/announcements/apple-health-expansion-enrollment-cap) | 当前 cap met、扩展针对不能按其他身份规则获 Apple Health 成人；其他项目与市场另核；2027-01-01 FFS 未来变化 | 旧 cap 公告谈预算 proposal，未当已实施法律；用当前项目主页确认名额。主页有倒置 OE 日期“Nov 1, 2026–Jan 15, 2026”和隐私 / public charge 简化语不一致，均未采用。不能写成所有 Apple Health 均关闭 |
| [Texas HHS：Health](https://hhs.texas.gov/services/health)，web 403、普通 HTTPS 200 全文；[Your Texas Benefits](https://yourtexasbenefits.com/Apply/GettingStartedApp?lang=en_US) web 200 重定向 /Learn/Home 实读公开入口文字 | HHS 将福利申请引至 Your Texas Benefits；老人 / 残障 / 地方贫困医疗等路线；YTB 先判断本系统或 HealthCare.gov | 仅公开入口可用性，不做真实申请。本文未穷举 TX 资格美元门槛或时限 |
| [Texas Works Handbook A-240](https://fhb.hhs.texas.gov/handbooks/texas-works-handbook/a-240-medical-programs)，web 实读 A-240 全章和 A-242 Certified Group | 家庭 MAGI 类别：儿童、孕妇、父母 / caretaker；parent 必须与 dependent child 同住、TP08 child receives Medicaid 等；类别和收入必须同时符合 | 章内修订年 2012–2022 混合，采用当前官方承载的类别结构，未把整章说成 2026 新法，也不采用移民旧段替代 2026 变化 |
| [Texas Department of Insurance：2026 Texas Health Coverage Guide](https://www.tdi.texas.gov/healthguide/2026-texas-health-coverage-guide.pdf)，web 实读封面 2026–28 edition / first posting Dec 2025；印刷 p9–10（PDF 物理第 11–12 页，零基索引 10–11） | HealthCare.gov 个人市场、YourTexasBenefits 政府项目入口；儿童、孕妇、原寄养、残障、65+；跨州 Medicaid 服务与资格不同 | 正文结合 HHS 补上 parents/caretakers，未将 TDI 简介当完整排他资格。文件别处约10% affordability、共付案例等未采用 |

## 未采用来源、不能据此作出的结论

- DHCS `/medi-cal/updates/medi-cal-changes/`、2026-01-05 新闻页多次 403；改用实际可读 Help、身份表和 2026-09-21 联邦影响页，未把搜索摘要当主文。年初 H.R.1 Implementation Plan 搜索显示的是提案阶段，未以它否定后来的州过渡资金。
- NY DOH 2026-03-23 批准公告、NYSOH EssentialPlan 页及首页部分请求 403；收入组退出采用 OAG 原文加 NYC311 事后确认。没有假装读到被拒页面。
- HealthCare.gov 移动 screener 页 web 正文 0 行，未采用；2026-09 CMS PDF 充分给出条件与例外。CMS PDF 有诉讼脚注，本文未省略脚注后将暂缓的核验制度写成现行要求。
- Texas HHS 旧父母照顾者路径 404；实际新 fhb 官方手册及 HHS / YTB 入口可读。没借第三方网页给出得州收入或新移民资格结论。
- HCA 非公民事实页是六月，不能单读；SSI 禁令是九月底，Expansion 名额为查阅时状态，未来公告改变须更新。
- 没有测私人账户、个人案例资格、实际药房或特定网络；这类结果由计划文件及申请通知决定。正文中的建议电话 / 问题列表为作者操作整理，不是逐字法规。
- 本页未声称完整覆盖所有小雇主延续法、Medicare、军人 / VA、学生保险、长期照护、特殊医疗项目、移民公共负担与数据共享诉讼；所写边界均在相关行动处可见，不以此省略普通失保可执行流程。

## 复核与验收

1. 独立审须回到所采用正文，尤其选保与付款分开、较晚起点、移动先前保障例外、SSI 法院保护、新申请冻结与旧保续保不同。异人通过后由第三参与者静态审，主控方可安装正式元数据。
2. 2027 年度入口、收入 / 补助规则、CA / WA 2027-01-01 项目转换、CA 2027-06-30 过渡末日、NY Essential Plan 再调整、WA 名额及判令变化是重新研究触发；不以本文 2026 快照指导后续年度而不回源。
3. 本文虚构教学例只有小林 10 月 15 日终止、20 日选保、11 月 1 日生效，未编造真实投诉、资格批准或医疗记录。
4. 作者仅完成局部格式 / 链接路径 / 正文 SHA 核验，不构建、不提交、不把作者记录当事实审通过。
