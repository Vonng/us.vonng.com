# B06 出生与最初几周：独立事实审中断记录

- 正文：`content/book/people/family/birth-and-first-weeks.md`
- 作者：`/root/health`；独立事实审：`/root/documents`
- 当前正文 SHA-256：`3e2583c2e8925395e6e44991df2705a3fa0e3ea9438493ad705810a736c5631f`（仅 `split('---', 2)[2]` 的 UTF-8 字节）。
- 核查日期：2026-10-13。
- 状态：**未完成，用户暂停后保存现场；不是 PASS，不能据此安装已核验元数据。**
- 已全文阅读正文及作者证据；未修改正文。以下为本轮亲自打开原文所得，并非以作者记录代核查。迄今未发现需要作者返修的实质问题。暂停后只保存本记录，没有继续研究、构建或提交。

## 已实际完成的来源核对

1. [HealthCare.gov 怀孕与保障](https://www.healthcare.gov/what-if-im-pregnant-or-plan-to-get-pregnant/)：web 实读正文。孕产服务、Medicaid 全年申请、联邦市场怀孕本身不构成 SEP、出生后 60 天及出生日起保障、已有成人计划选择受限、分娩时母亲有 Medicaid 时新生儿至少一年保障，均与稿内对应范围相符。
2. [DOL 出生后特别加入](https://webapps.dol.gov/elaws/ebsa/health/72.asp)：web 实读正文。出生后 30 天请求、出生日起生效、员工及计划提供的家属类别条件，稿件已保留。
3. [NY DFS 个人市场说明](https://www.dfs.ny.gov/apps_and_licensing/health_insurers/guidance/market_rules_guaranteed_availability_renewability)及[现行 Insurance Law §4328](https://www.nysenate.gov/legislation/laws/ISC/4328)：均 web 实读。DFS 页面修订于 2017 年，已另读现行法 (b)(4)(B)，核实经有资格医疗人员确认后孕期可申请、确认所在月首或本人选择下月首生效；未扩展至所有雇主计划。
4. [NY DOH 2026 孕产标准](https://healthweb-back.health.ny.gov/health_care/medicaid/standards/perinatal_care/)：普通 HTTPS 200，BeautifulSoup 实读开头生效与适用范围及包含 immigration / 12 months 的完整相关段落。2026-02-01 标准明确 pregnant Medicaid members 不论移民身份在妊娠结束后延续 12 个月；正文未把此写成不看其他资格。
5. [Washington Healthplanfinder 孕期页面](https://www.wahealthplanfinder.org/us/en/my-account/life-events/pregnancy-and-post-partum.html)：web 实读；[HCA noncitizens](https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/noncitizens)及[WAC 182-505-0115](https://www.hca.wa.gov/free-or-low-cost-health-care/i-help-others-apply-and-access-apple-health/wac-182-505-0115-washington-apple-health-eligibility-pregnancy-and-after-pregnancy-coverage)：普通 HTTPS 200 实读相关正文及全部规则条款。核实 2026-10 非公民资格变化仍保留孕产例外；规则第 (4)、(6) 款区分孕期最后一天已覆盖者及产后申请者，补申请仅到原定 12 个月期间末。
6. [TX HHS Medicaid/CHIP Perinatal](https://www.hhs.texas.gov/services/health/medicaid-chip/medicaid-chip-programs-services/medicaid-pregnant-women-chip-perinatal)及[产后延续 FAQ](https://www.hhs.texas.gov/sites/default/files/documents/postpartum-medicaid-chip-faq.pdf)：普通 HTTPS 200；HTML main 与两页 PDF 经 pypdf 实读。核实居住、收入、Medicaid 公民/合格非公民、CHIP-P 无其他保险且不合格 Medicaid；CHIP-P 不享完整 12 月延续、妊娠结束后 60 天内两次产后就诊。FAQ 2024-06 修订，载明 2024-03-01 起完整 Medicaid/CHIP 延续，未把旧过渡恢复日期当一般现行开始日。
7. [Covered California 家庭变化](https://www.coveredca.com/enrollment/major-life-changes/)：web 实读实际申请、家庭变化及生育入口。原引 DHCS MCAP 长 URL 与 immigrant eligibility FAQs 本轮 web / 普通 HTTPS / 正常代理均 403；作者表示其本轮 web 曾成功，审阅不把这个说法计作自己读到原文。
8. 对上一项，已另独立 web 实读同主管机关 [DHCS Immigration Status and Changes](https://www.dhcs.ca.gov/immigration-status-and-changes-to-medi-cal-eligibility/) 表格及 Important Notes；其 2026 年孕期及结束后一年不论移民身份可申请例外支持稿内短断言。另实读 [LA DPSS MCAP](https://dpss.lacounty.gov/en/health/pregnant/mcap.html) 全部相关资格段落：加州居住、收入、其他项目与保险、maternity-only deductible/copayment 大于 $500，支持稿内例子。该县页其他未在正文使用的 renewal 表述未作采纳。[DHCS Help Center](https://www.dhcs.ca.gov/medi-cal/help/) 已打开但仅返回前部，**尚未直接读到其 MCAP 小节**；不能把搜索结果中该小节作为已实读。
9. [HRSA 健康中心](https://bphc.hrsa.gov/about-health-center-program/what-health-center)：web 实读全文。按收入及家庭人数调费、服务无力支付者与查询入口支持稿内受阻路径，未宣称所有诊所免费或均有相同产前服务。
10. [DOL FMLA](https://www.dol.gov/agencies/whd/fmla)：普通 HTTPS 200，实读 main 中无薪职位保护、团体保险延续、雇主与员工资格、州法可能额外保障及沟通申请段。稿件仅作入口性说明，没有承诺普遍带薪期限。
11. [NYC 出生记录](https://www.nyc.gov/site/doh/services/birth-death-records-birth.page)：web 实读 New and Expectant Parents、五区管辖、认证证明及更正段。核实医院 worksheet、多语参考、列名父母约四周免费副本，非全国做法；[WA DSHS 亲子关系](https://www.dshs.wa.gov/family-food-and-housing-services/child-support/establishing-parentage) 实读主文，婚姻/承认书/法院命令途径与稿件有限例子相符。
12. [LA DPH 出生记录](https://publichealth.lacounty.gov/dca/dcabirth.htm)：普通请求依本站自然跳转 HTTP 200，实读全部正文。确认本年/前一年，排除 Pasadena、Long Beach，较早记录 RR/CC；[LA RR/CC 网上申请](https://www.lavote.gov/home/records/birth-records/birth-records-request/online-request)：web 实读主文，身份声明及 informational copy 不用于建立身份属实。
13. [NY DOH 出生证明](https://healthweb-back.health.ny.gov/vital_records/birth.htm)：普通 HTTPS 200 实读正文；核实州 DOH 排除 NYC 五区、地方 registrar、列名父母与身份证明。 [WA DOH 出生记录](https://doh.wa.gov/licenses-permits-and-certificates/vital-records/ordering-vital-record/birth-record)：普通 HTTPS 200 实读正文；核实医院登记不构成副本订单、身份与关系材料、首份不自动免费及多种订购方式。
14. [TX DSHS 出生记录](https://www.dshs.texas.gov/vital-statistics/birth-records)：web 实读 Birth Records 主文及 Other Ways / Corrections；核实 verification 与 certified copy 不同、网上/邮件/地方及 Austin 现场入口，未展开未核定价或承诺全国交付时间。
15. [SSA EAB FAQ](https://www.ssa.gov/faqs/en/questions/KA-10041.html)及[儿童 SSN 手册](https://www.ssa.gov/pubs/EN-05-10023.pdf)：web 实读，手册 2026-04 版。核实医院/分娩中心/执业助产士 EAB、不知道双方 SSN 仍可申请、后续线上启动并办公室完成、年龄身份及申请人关系证明不同；稿内未把出生证明当全部材料。
16. [AAP 新生儿首次检查](https://www.healthychildren.org/English/ages-stages/Your-Childs-Checkups/Pages/Your-Checkup-Checklist-Newborn-Visit-2-to-5-days-old.aspx)：web 实读 2026-09-18 更新正文。实际标题/当前内容为出生后 3–5 天，URL 旧字样 2-to-5 未当规则；医院资料、喂养体重筛查及预约受阻联系途径与稿件相符。[CDC 紧急孕产警讯](https://www.cdc.gov/hearher/maternal-warning-signs/index.html)：web 实读警讯与末段。孕期/分娩后一年、稿内列举症状、立即求医及报告孕产史有支持；正文已说明不是全部警讯。

## 恢复时尚须处理

- 完成最终逐段断言与上述核验范围的对照、确认没有遗漏的资格/期限，以及正式结论；目前没有给出 PASS。
- 直接链接 [HealthCare.gov SEP](https://www.healthcare.gov/coverage-outside-open-enrollment/special-enrollment-period/) 尚未单独打开；同机构怀孕页已经实际支持文中出生后 60 天及出生日起算，但记录不能称两页都已读。SSA number-card 门户亦未在本轮另开；2026 手册已明确该申请入口与办公室完成路径。
- DHCS 原引两页本轮持续 403，现有独立实读同机构/地方项目主管资料已支持正文涉及的 CA 短断言；恢复时判断是否需要额外补读或为引用可达性建议作者换链接。没有发现必须删改的事实冲突，不因本轮访问失败单独认定作者未读。
- 正文不包含医疗诊断、所有州精确收入表、复杂亲子诉讼、公民身份争议或所有出生记录收费；这些未作全面核验，不得从本审延伸为全流程法律/医疗认证。
- 仅正文 SHA 如变化，须先检查变化内容再重绑，不可只抄旧通过结论。

## 同一执行者银行作者稿交接

`content/book/work/finance/banking-payments.md` 已完成并交 civic 独立事实审。root 预检要求的四处粗体闭合前空格已修正，事实文字未变，全文粗体内外空格已检查。当前正文 SHA：`3fce0fead028faf8a294ed6cf8ab3de590a2b51af13678e5c0ccb6db77b3fabd`。作者地图/证据为 `ops/maps/banking-payments.md`、`ops/evidence/banking-payments.md`。未自行构建或提交；等待独立审意见，用户暂停期间不继续工作。
