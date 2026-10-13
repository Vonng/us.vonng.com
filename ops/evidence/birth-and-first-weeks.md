# 生育与最初几周：作者事实链

实际查阅：2026-10-13。原作者 `/root/health`，B06；本轮恢复修订者 `/root/static_editor`；对应 `content/book/people/family/birth-and-first-weeks.md`。以下原始来源阅读由原作者完成，本轮修订另记在末尾；不以搜索摘要作证，本文件不代替独立事实审。正文适用截至查阅日的公开规则，不预测 2027 年实施。

## 采用来源与定位

| 来源／支持的正文 | 本次实际读取、时期、范围与边界 |
|---|---|
| [HealthCare.gov：Pregnancy coverage](https://www.healthcare.gov/what-if-im-pregnant-or-plan-to-get-pregnant/) | `web.open` 完整主文 10—87 行，分别读取计划覆盖、无保孕期、Medicaid 和出生后计划选择。怀孕本身不触发该联邦市场 SEP；Medicaid／CHIP 全年申请；当前 Marketplace 成年人通常不可因出生任意换计划、孩子可另选；分娩时孕产者已有 Medicaid 的新生儿至少一年保障。限定计划／项目，不推广旅行险，也不把此页孕期 SEP 规则覆盖 NY。已有计划先确认新保障，原文特意说明不要在 Medicaid 批准前取消市场保险 |
| [HealthCare.gov：Special Enrollment Periods](https://www.healthcare.gov/coverage-outside-open-enrollment/special-enrollment-period/) | `web.open` 主文 Changes in household，39—43 行；出生后 60 天、可回溯出生日期。正文以 HealthCare.gov 市场限定，州自建市场另查；页面其他失保窗口不移用于出生 |
| [DOL elaws：Special enrollment for a new dependent](https://webapps.dol.gov/elaws/ebsa/health/72.asp) | `web.open` 完整主文，依次读 employee / newborn / spouse，17 行 birth 至少联邦 30 天内请求和 DOB 生效；前提为计划提供相应家属保障、员工符合资格并按规则加入。末段提示州或计划可更宽；没有把所有祖父母计划或所有员工自动列为孩子的可用计划 |
| [Covered California：Major Life Changes](https://www.coveredca.com/enrollment/major-life-changes/) | `web.open` 实读主文 Life Changes／Having a baby／60 日窗口和生效日选择，61—107 行。用为正式入口；Pregnancy FAQ 答案未呈现，所以正文没有断言 CA 单独怀孕一定产生或不产生 SEP。既有医保页的四州入口仍有效 |
| [DHCS：MCAP Who Qualifies](https://www.dhcs.ca.gov/services/medi-cal-resources/medi-cal-eligibility-division/welcome-to-the-medi-cal-access-program-en-espanol/who-qualifies-for-mcap-en-espanol/) | `web.open` 实读 42—88 行。URL 含 en-espanol，但实际为英文资格正文；2026-01-01 收入表已读，正文不转载金额表。必须仍怀孕、CA 居住、现有 Medi-Cal／Medicare 及其他保险限制；其他保险不保 maternity 或 maternity-only deductible/copayment >$500 的例外。没有误写成一般家庭 deductible >$500 即可加入；完整材料收到日期定义已读但正文不加新期限 |
| [DHCS：Medi-Cal immigrant eligibility FAQs](https://www.dhcs.ca.gov/medi-cal-immigrant-eligibility-faqs/) | `web.open` 实读 44—74 行，采用 49—52 行 Jan 1, 2026 成人新申请限制及 pregnant/infant 例外；pregnancy + one year after regardless outcome／immigration，仍须其他资格。其他 dental 时间与较新政策页有潜在版本差，正文不采用；同页 public charge 广泛解释亦未采用 |
| [NY DFS：Market Rules](https://www.dfs.ny.gov/apps_and_licensing/health_insurers/guidance/market_rules_guaranteed_availability_renewability) 与 [NY Insurance Law §4328](https://www.nysenate.gov/legislation/laws/ISC/4328) | 两页 `web.open` 实际主文；DFS 页修订 2017-11-20，因此再回现行法。§4328(b)(4)(B)，108—121 行，医疗人员执业范围内确认、孕期 any time、确认月份首日或本人选次月首日；DFS 支持个人保险市场层次，正文明确不推广雇主计划。没有误套出生后 60 天窗口到怀孕申请 |
| [NY DOH：2026 Medicaid Perinatal Care Standards](https://healthweb-back.health.ny.gov/health_care/medicaid/standards/perinatal_care/) | 标准 2026-02-01 生效；`web.open` 实际 59—126 行，包括尊重多种家庭、团队、产检可及性、Medicaid 申请、120 行移民身份不影响已符合条件成员的 12 月产后完整服务。www.health.ny.gov 同路径 web／普通 HTTPS 403，官方 healthweb-back 等效正文成功。113—114 行已读：2026-01-01 停止旧纸 DOH-5224 路径，MECM 电子新流程原文仍称 Spring 2026 预计；没有把预计上线当事实，也没有错称全部 presumptive eligibility 已停 |
| [NY State of Health](https://nystateofhealth.ny.gov/) | 本日 B04 已实际读取其正式市场申请及 Medicaid／CHP 入口，B06 仅作为办理入口，不从门户推导金额或资格；精确怀孕及产后规则由上两项支撑 |
| [WA Healthplanfinder：Pregnancy and Post-Partum](https://www.wahealthplanfinder.org/us/en/my-account/life-events/pregnancy-and-post-partum.html) | `web.open` 主文 57—82 行，报告怀孕、APC 12 月、申请入口。页面 SEP 段没有明确“单独怀孕”是事件，故不作此推断 |
| [WA HCA：Noncitizens](https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/noncitizens) | web 403；同日普通 HTTPS `urllib` 200，BeautifulSoup 全部 main 实读。当前提示 2026-10-01 非公民变化，同时明确符合其他条件的 children/pregnant 不论移民身份；Pregnant Individuals 与 APC 段均读。正文不把成人旧类别延伸到孕产者，也不采用页面所列完整身份法律判断 |
| [WA HCA 重印 WAC 182-505-0115](https://www.hca.wa.gov/free-or-low-cost-health-care/i-help-others-apply-and-access-apple-health/wac-182-505-0115-washington-apple-health-eligibility-pregnancy-and-after-pregnancy-coverage) | web 403；普通 HTTPS `requests` TLS 校验开启，200，BeautifulSoup main 全文实读。Effective June 24, 2022；(1)—(2) 收入、居住及非公民例外；(4) 最后孕日符合且覆盖后次月起 12 个月；(5) 范围按 CN／MN；(6) 孕期未参保可在产后期间申请到原定第 12 月结束，不能说申请日起再获完整一年。正文不展开 spenddown 个案 |
| [TX HHS：Pregnant Women Medicaid and CHIP Perinatal](https://www.hhs.texas.gov/services/health/medicaid-chip/medicaid-chip-programs-services/medicaid-pregnant-women-chip-perinatal) | web 访问失败，普通 HTTPS 实际 200，BeautifulSoup 主文全文读到 Medicaid full coverage／STAR、CHIP-P 无其他保险及不符合 Medicaid、Texas 居住／income／Medicaid citizenship-qualified noncitizen、两次产后复诊。未使用年度收入表金额，旧 `/health/women-children/medicaid-pregnant-women-chip-perinatal` 为 404，正文为从官方实际导航找出的现路径 |
| [TX HHS：Postpartum Medicaid and CHIP FAQ](https://www.hhs.texas.gov/sites/default/files/documents/postpartum-medicaid-chip-faq.pdf) | web 403；普通 HTTPS 200、内存 BytesIO+pypdf 两页全文阅读。Rev June 2024；印刷／物理第 1 页从 2024-03-01 起 12 月、CHIP Perinatal 明确 excluded，CHIP-P 妊娠结束月止及结束后 60 日内两次访问；第 2 页 pregnancy loss 仍可完整项目延续、迁出等结束条件已读但不列完全规则。并实际读 [Women and Children](https://www.hhs.texas.gov/services/health/women-children) 普通 HTTPS 主文核对，无把 CHIP 和 CHIP-P 混同 |
| [HRSA：What is a Health Center?](https://bphc.hrsa.gov/about-health-center-program/what-health-center) | web 实读 15—46 行；reviewed November 2025；服务、按收入和家庭人数调整收费、serve everyone even if cannot pay；页内真实 Find a Health Center 指向 https://findahealthcenter.hrsa.gov/ 。没有宣称所有中心免费、立即有床位或每个点都有产科；正文要求确认具体服务 |
| [DOL：FMLA](https://www.dol.gov/agencies/whd/fmla) | web 403；同日普通 HTTPS `requests` 200，main 实读开头、Covered Employers and Employee Eligibility、Family Relationships、请求及雇主通知段。正文仅采用有条件的 unpaid/job-protected/continued group benefits 与 HR、WHD、州劳动机构分流；没有列全国统一带薪天数。员工 12 月／1250 小时／50 人75英里及航空例外均读但正文不做完整资格判断 |
| [NYC DOHMH：Birth Certificates](https://www.nyc.gov/site/doh/services/birth-death-records-birth.page) | `web.open` 实读主文 25—92 行，五区归属、certified copy、new/expectant parents、worksheet 翻译、免费约四周自动邮寄、姓名地址检查、已婚同性／异性父母、未婚自愿 AOP 及更正入口。正文仅采用实际所需部分；没有推广 NYC 自动寄送到全 NY 或全国，也未把 AOP 当所有家庭必签 |
| [WA DSHS：Establishing Parentage](https://www.dshs.wa.gov/family-food-and-housing-services/child-support/establishing-parentage) | 旧 `/esa/division-child-support/establishing-parentage` 在 web 正常重定向到此路径；实读主文 1—29 行，法律关系、marriage／AOP／court order、providers 帮填及法院帮助链接。正文为 WA 案例，复杂家庭签前求证属编辑分流；没有声称仅填出生证明即可完成全部亲权或跨州承认 |
| [LA County DPH：Birth Certificates](https://publichealth.lacounty.gov/dca/dcabirth.htm) | web redirect loop；普通 HTTPS `requests` 请求后官方重定向为同域 HTTP，200，BeautifulSoup 全部主文实读。当前及前一年记录、排除 Pasadena／Long Beach、较早记录 RR/CC、两市具体入口、其他县 CDPH。正文不用10天、费用等可变数值；本县案例不冒充全 CA 统一窗口。未提交个人资料 |
| [LA RR/CC：Online Request](https://www.lavote.gov/home/records/birth-records/birth-records-request/online-request) | web 主文 122—152 行，县内范围、唯一外包 VitalChek、notarized Certificate of Identity 可要求、informational copy 不能确立身份。正文未复制费用／处理日；只通过政府页进入订单，不代办 |
| [NY DOH：Birth Certificates](https://healthweb-back.health.ny.gov/vital_records/birth.htm) | web 及普通 HTTPS 主文实际读到 Overview／Requirements／Corrections，67—140 行。2023-01 修订，当前入口；NYC 排除、当地 registrar、列名父母、ID A/B 两途径。正文不写邮寄积压时长及费用，不把有 SSN 一概写成获得孩子记录前提 |
| [WA DOH：Ordering a Birth Record](https://doh.wa.gov/licenses-permits-and-certificates/vital-records/ordering-vital-record/birth-record) | web 403，普通 HTTPS 200，main 全文实读。qualified applicants、ID／alternate ID、relationship proof、certified vs noncertified；newborn FAQs 明确医院 birth filing form 不等于副本订单、第一份不免费、医院不能替申请人订购。各渠道实际列明。不把 heirloom 一概写成非法律纪念纸（本州 heirloom 可为 legal certified） |
| [Texas DSHS：Birth Records](https://www.dshs.texas.gov/vital-statistics/birth-records) | web 主文 257—310 行；certified long／short／heirloom 与 verification 的产品类别、Texas.gov 订单、mail/in-person/local offices、corrections。正文不推断所有其他用途都收某一种版本，未写自动寄送或具体费用 |
| [SSA FAQ：How do I get my baby's SSN?](https://www.ssa.gov/faqs/en/questions/KA-10041.html) | web 主文 50—60 行，updated 2026-07-01；EAB hospital／birth center／licensed midwife，州 birth registration 转送 SSA；平均处理时间及 2026 纪念卡已读但不采入正文，避免平均值变保证 |
| [SSA：Social Security Numbers for Children](https://www.ssa.gov/pubs/EN-05-10023.pdf) | web PDF 10 物理页；实读物理 2—6 页（印刷 1—5）。不知双方 SSN 仍可申请；事后 online start／office complete 或 SS-5；儿童 citizenship／age／identity 与代办人 identity／relationship；原件要求、noncitizen 另见相应手册。正文明确资料类别，未从本页推断当前有争议的出生公民权案件。另实际读 SSA 2021-12-09 官方博客同义说明，最终引用较新 FAQ 与手册 |
| [AAP HealthyChildren：First Week Checkup](https://www.healthychildren.org/English/ages-stages/Your-Childs-Checkups/Pages/Your-Checkup-Checklist-Newborn-Visit-2-to-5-days-old.aspx) | `web.open` 全主文 62—136 行；Last Updated 2026-09-18。3—5 days old、hospital paperwork、growth／feeding／screening、联系诊所即使closed及医生决定多久就诊。正文称日龄阶段，未误写为出院后再等3—5日；特殊情况按医生安排。疫苗／抗体段虽读，不在本页给处方或最新统一接种结论 |
| [CDC：Urgent Maternal Warning Signs](https://www.cdc.gov/hearher/maternal-warning-signs/index.html) | web 全主文 18—168 行；dated 2024-05-15，2026-10-13 当前读取。孕期／分娩后一年、立即就医、所举胸痛／呼吸／头痛／出血／自伤或伤婴念头、列表非穷尽及告诉医生孕产史。正文只用警讯与紧急分流，不对读者诊断。911 为既有应急稿已核联邦常识，本页不设新医疗阈值 |

## 失败、冲突与未核实范围

- CA CDPH `https://www.cdph.ca.gov/Programs/CHSI/Pages/Vital-Records-Obtaining-Certified-Copies-of-Birth-Records.aspx`：web 502；普通 urllib／requests 为证书链验证失败，未关闭 TLS 校验。没有据其摘要编写全州程序，改用实际读到的洛杉矶县官方出生登记入口并准确保留两市例外。其他加州县的具体费用、表件和办理时间不在本页。
- DHCS Full Scope／Affordability 页面实际读到 `https://www.dhcs.ca.gov/services/medi-cal-resources/full-scope-medi-cal-coverage-and-affordability-and-benefit-program-for-low-income-pregnant-women-and-newly-qualified-immigrants/`；其 NQI 部分仍称预计 2017，另有旧 pregnancy-related／full scope 口径，未用这些旧段判断现行范围。MCAP 使用当前独立资格页、孕产移民例外使用现行 FAQ。没有引用私人帖子或搜索摘要的 2026 法案提案。
- NY DOH 标准中预计 Spring 2026 的 MECM 电子预资格操作是否全州上线，本次未确认；不影响现有 NY State of Health 申请分流，正文无上线承诺。
- WIC eligibility 官方页 web 403；本轮不展开 WIC，未声称完成其资格研究。Medicaid.gov `/medicaid/eligibility/children/index.html` 当前工具不可访问；新生儿 Medicaid 段用实际可读的 HealthCare.gov 主管说明，未把失败入口列为采用证据。
- 出生公民权、护照、领事登记、跨国旅行、代孕／收养／法院亲权命令的个案效力未研究；本页没有断言在美出生即解决父母身份，也没有让出生证替代个人移民资格审查。新生儿 SSN 章节按 SSA 当期材料与申请路径写作。
- 医疗团队、预登记、费用估算、照护任务和完成标志属于编辑整理的实际核对清单，不声称每家医院使用同一表格。未联系医院／雇主、未提交真实申请、未模拟私人保险报价。无虚构数字或冒充官方表格。
- SSN 未到先报告出生并询问补件，是保存窗口的行动建议；没有保证每一计划接受某一种临时材料，也没有给未有保险卡的人保证账单免费。

## 复核触发

进入新的计划年度、州 Medicaid／CHIP 资格或产后延续变更、移民相关联邦执行范围或法院命令影响孕产项目时，重读四州资格和 12 月／CHIP-P 边界。Marketplace 新规则或州怀孕事件变化时，重查 NY 与 HealthCare.gov 并置说明；不按日历自动推断政策已生效。

SSA EAB 流程或材料调整、出生记录订单入口与城市归属变更时，重读各相关段；新收入表不要求修改正文未使用的金额，但 MCAP 的 500 美元保险例外须复核。AAP／CDC 更新时，重查首周预约与警讯。具体申请在当日以主管通知和计划书为准。

未构建、未提交、未安装正式元数据；作者校验仅核正文、链接目标和加粗边界，独立审阅由另一参与者执行。

## 2026-10-13 恢复修订

原作者 `/root/health`；本轮修订者 `/root/static_editor`，由主控分派。修订前正文 SHA-256 为 `3e2583c2e8925395e6e44991df2705a3fa0e3ea9438493ad705810a736c5631f`，修订后为 `bb51e12f0ed73579c4f86064c2b7963c28c323ea64d7cf6425b3df355ae609b8`；均按 UTF-8 `split('---', 2)[2]` 计算，不含 frontmatter。

唯一正文差异：“医院账单仍显示孩子未保险时”改为“医院账单仍把孩子记作无保险时”，表达账单仍将孩子记作无保险的状态。规则、期限、资格、生效日期、金额、链接和元数据均未改变。本轮修订者完整读稿、原地图／证据及历史事实审中断记录，没有为这一个措辞变化新增医疗或福利事实、重新声称原作者的外部来源阅读。

当前版本已交 `/root/birth_fact` 对照实际差异复核；其后修订者实际读取 `ops/reviews/b06-birth-fact.md` 的本轮最终结论，确认独立事实 PASS 绑定当前 `bb51e12f…609b8`。该事实结论来自 birth_fact 的独立阅读，未冒用修订者自行检查代替；第三人静态审由 `/root` 执行。修订者不兼任此稿第三人，不安装正式审阅元数据，不构建、不提交。

## B06 主控集成记录

health原作者／static_editor修订；birth_fact独立事实审、root第三人静态审均PASS。当前正文bb51e12f；B06正式integrated／draft false，2026-10-13，见b06-integration.md。 本段仅登记实际完成的审阅与集成，不新增来源实读或个案核实声明；实际读到的范围与失败边界见对应事实审记录。
