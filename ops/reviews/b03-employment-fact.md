# B03 工资单与加班：独立事实审

- 审阅人：`/root/health`；作者：`/root/civic`，为不同参与者。
- 实际查阅日期：2026-10-13。
- 正文：`content/book/work/employment/pay-stub-overtime.md`。
- 审阅绑定正文 SHA-256：`0b21289995a0c69432629ae8231032d132c2593cdf21c3ddf4db029b89f21c0a`。
- 方法：读取实际正文并按 `split('---', 2)[2]`、UTF-8 计算 SHA；收到冻结通知后独立回源，已核对最终正文与冻结值一致。
- 结论：**事实审通过** 。没有需作者修改的实质事实问题。所有采用的金额、时数、算例、期限及重要边界均有本次实读依据；没有修改作者正文、元数据或证据。静态编辑审、构建与渲染另由主控负责。

## 独立回源与判断

| 实读来源与定位 | 核查结论 |
|---|---|
| [DOL FS14](https://www.dol.gov/agencies/whd/fact-sheets/14-flsa-coverage)，Enterprise / Individual Coverage；[FS17A](https://www.dol.gov/agencies/whd/fact-sheets/17a-overtime)，全部主要豁免及 Other Laws | 普通 HTTPS 取得正文并实际阅读，FS17A 的 web 为 403。两种覆盖、小公司不当然排除、684 美元 / 周、工资方式及职责测试、管理两名全职或等量人力与聘免权 / 有分量建议均准确。标题不是测试，体力劳动不因高薪自动白领豁免。州更有利规则须同时检查。FS17A 标 2019 修订；684 当前数值另由本次 WA 2026 问答及 NY 2026 FAQ 交叉支持，不据旧修订年份讲述法院程序。 |
| [DOL FS23](https://www.dol.gov/agencies/whd/fact-sheets/23-flsa-overtime-pay)，Requirements、regular rate、Salary for workweek、May Not Be Waived | 普通 HTTPS 全文。固定 168 小时 / 七天、40 小时以上、跨周不能平均、1.5 倍、周末名称本身无加成、报酬基数与排除、先付 straight time 后加 0.5 premium、有年薪不自动豁免均得到支持。稿件没有套用单一算例处理所有奖金和混合费率。 |
| [DOL FS22](https://www.dol.gov/agencies/whd/fact-sheets/22-flsa-hours-worked)，Suffer / Permit、Rest and Meal、Training | 普通 HTTPS 全文。工作时间以实际及允许工作为准；通常短休计薪、完全解除职责的用餐时间可排除；培训排除另有条件。稿件未把必须给休息与给了休息后计薪混为一谈。 |
| [DOL pay-stub FAQ](https://webapps.dol.gov/elaws/faq/esa/flsa/018.htm)，全文 | web 实读：FLSA 本身保记录但不要求发 pay stub。 |
| [DOL Worker FAQ](https://www.dol.gov/agencies/whd/faq/workers)，全部问答 | 普通 HTTPS 实读。免费、1-866-487-9243、语言帮助、一般两年 / 故意三年、个人同期记录可供调查、保密及本人许可 / 法院命令例外、反报复、无证员工也执行适用工资法、非全部约定工资 / 福利范围，正文逐项准确。稿件没有承诺追回、绝对匿名或投诉自动停止时效。 |
| [CA 工资单样表](https://www.dir.ca.gov/dlse/PayStub.pdf)，2018-05，PDF 全一页；[CFPB 工资单 handout](https://files.consumerfinance.gov/f/documents/cfpb_building_block_activities_how-to-read-pay-stub_handout.pdf)，Summer 2022，全一页 | 独立普通 HTTPS 在内存解析 PDF，读取所有字段。pay period / pay date、gross / deductions / net、YTD 均对应实际样表；作者只用字段，不把旧税率或旧时薪当标准。 |
| [CA 索赔](https://www.dir.ca.gov/dlse/HowToFileWageClaim.htm)，Make sure you file timely、Gather facts、Keep all your pay stubs、How to file；[CA 2026 公告](https://www.dir.ca.gov/DIRNews/2025/2025-118.html)，2025-12-05 主文；[最低工资](https://www.dir.ca.gov/dlse/minimum_wage.htm)，主文 | web / 普通 HTTPS 实读。2026 为 16.90 美元，70,304 年薪是豁免金额部分；地方 / 部分行业另有较高标准。每次工资说明、线上 / 邮件 / 邮寄 / 到办公室、最低工资及加班等三年、其他请求期限不同、移民身份不影响适用保护，正文有准确范围。未独立读到 Labor Code §226 原网页，不假装原法核验；有限工资单断言由 DIR 正文及样表直接支持。 |
| [CA Overtime](https://www.dir.ca.gov/dlse/FAQ_Overtime.htm)，导言、问答 1–9；[Exceptions](https://www.dir.ca.gov/dlse/FAQ_OvertimeExceptions.htm)，alternative workweek 表；[Executive glossary](https://www.dir.ca.gov/dlse/Glossary.asp?Button1=E)，Executive exemption 全段 | 普通 HTTPS / web 实读。每日八 / 十二、同工作周连续第七日及周四十边界、1.5 / 2 倍、获知或应知未授权工作仍付、年薪分类、未实际工作假日不计加班，均准确。有效 alternative workweek 是算例的重要排除，已经明确；不把四天十小时普通算例用于有效替代安排。州职责测试确实独立于联邦。 |
| [NY Labor Law §195(3)](https://www.nysenate.gov/legislation/laws/LAB/195)，全文段；[Wages and Hours FAQ](https://dol.ny.gov/wages-and-hours-frequently-asked-questions)，Deductions / Payroll Records | web 实读。每次发薪、非豁免者普通 / 加班工时及费率、请求书面算法的断言准确；破损、现金短缺及经营损失扣款禁止有直接依据。未将来源陈旧农业信息写入正文。 |
| [NY 2026 公告](https://www.governor.ny.gov/news/money-your-pockets-governor-hochul-reminds-new-yorkers-minimum-wage-increase-january-1)，2025-12-22 主文；[Minimum Wage FAQ](https://dol.ny.gov/minimum-wage-frequently-asked-questions)，地理问答、2026 E/A threshold 段 | web 实读。NYC / Nassau / Suffolk / Westchester 17，其他地区 16；2026 管理 / 行政 1,275 / 1,199.10 周薪，各规模相同。以实际工作地判断，跨区记录支持准确。未扩为所有 professional 或各类豁免统一门槛，未把 2027 预告当 2026 数字。普通 HTTPS 本次对部分 NY 页 403，web 正文读取成功。 |
| [NY Overtime FAQ](https://dol.ny.gov/overtime-faq-1)，四页 PDF，第 1、3、4 页实际正文 | web 读取，普通 HTTPS 403。四十小时、部分联邦豁免仍适用州加班及费率差别、无一般每日八小时加班、夜间 / 周末不自动加成、不可跨周平均均支持。PDF 农业排除和旧例子未采用；稿件开头已排除行业例外。 |
| [NY Unpaid / Withheld Wages](https://dol.ny.gov/unpaidwithheld-wages-and-wage-supplements)，How to File、Unacceptable Claims、File a Claim | web 实读相关全部段落。页面当前明确超过三年、已诉、工会仲裁、特定 EAP 周薪超过 1,300 等不受理；LS223、上传 / 邮寄和 888-525-2267 直接对应。正文表述为这个行政入口的限制，未当成法院统一时效或 E/A 加班豁免标准。 |
| [WA Minimum Wage](https://www.lni.wa.gov/workers-rights/wages/minimum-wage/)，2026 / 2027 主文；[Overtime Q&A](https://www.lni.wa.gov/workers-rights/wages/overtime/changes-to-overtime-rules-q-a)，2026 thresholds 与 three-part test | 普通 HTTPS / web 实读。当前网页并列 2027 17.73 与 2026 17.13，作者正确只用后者；2026 所有雇主 1,541.70 / 周、80,168.40 / 年准确；金额、方式、职责三测试均保留。 |
| [WA Overtime](https://www.lni.wa.gov/workers-rights/wages/overtime/)，Workweek、Calculating、Alternatives | web 全文实读。普通周四十、一般无日八（公共工程例外）、regular rate 可能包含奖金 / 佣金、未工作有薪假排除、私营不得用该 comp time 代替，支持正文限定情形。 |
| [WA ES.D.1](https://www.lni.wa.gov/workers-rights/_docs/esd1.pdf)，2025-09-08 修订，第 1–2 页 | 普通 HTTPS 在内存解析并实际读取：非农业对象；工资说明、实际工时、普通与加班分列、电子提供及直接存款不能替代均准确。未引入未采用的人员档案或所有资料请求期限。 |
| [WA Worker Rights Complaints](https://www.lni.wa.gov/workers-rights/workplace-complaints/worker-rights-complaints)，完整主体 | 普通 HTTPS 实读。三年、报复 180 天、三种递交、向雇主提供姓名及副本、补件联系、不同结果与不保证收回，正文准确。 |
| [TWC Delivery of Wages](https://efte.twc.texas.gov/delivery_of_wages.html)，written statements 段；[Texas Labor Code 62](https://tcss.legis.texas.gov/Docs/LA/htm/LA.62.htm)，§§62.003、62.151 | 独立普通 HTTPS 实读原法及 TWC 说明。FLSA 覆盖者排除出该章，不能把 earnings statement 义务说成全州普遍要求。稿件正确区分 FLSA 覆盖者和其余适用者；仍建议索取明细是实务建议。 |
| [TWC FLSA](https://efte.twc.texas.gov/flsa_does_and_doesnt_do.html)，首段、premium / holiday / weekend | 普通 HTTPS 实读。7.25、周四十、一般 1.5 倍、周末不自动额外费率支持；未采用其陈旧哺乳内容或过度宽泛的其他旁支。 |
| [TWC Wage Claim and Appeal Process](https://efte.twc.texas.gov/wage_claims_in_texas.html)，claim form / filing 段；[Texas Labor Code 61](https://tcss.legis.texas.gov/Docs/LA/htm/LA.61.htm)，§§61.051–.052 | 普通 HTTPS 实读。官方指南有表件、签名、线上 / 当地 TWC / Workforce Solutions / 邮寄等；提醒传真暂不可用，正文未指示传真。原法明确应付日后第 180 日截止、属受理权限及迟交驳回；稿件准确，未挪用联邦两 / 三年。 |

## 算例与行动链

- 独立复算：1,000 − 180 = 820；16.90 × 2 × 40 × 52 = 70,304；17.13 × 2.25 × 40 = 1,541.70，再乘 52 = 80,168.40。
- 四天各十小时共四十小时；普通加州规则 32 × 22 + 8 × 33 = 968，另外三州普通规则 40 × 22 = 880，相差 88。例子明确非豁免成年员工、当地最低标准足够、无额外收入或特殊安排；不误算为普遍四州任何职业结果。
- 例子与英文沟通均明确教学虚构；英文要求 review / explain，未虚构机构承诺、立案或追回结果。
- 流程从保存工时和工资明细、识别差额，到 payroll / HR 书面要求、更正日期和适当索赔机构；保留内部沟通同时核对正式期限的行动。机构受理范围、移民身份与工作授权、匿名及反报复分别说明。

## 边界与复核触发

未进入工资或投诉账户、提交真实申请、联系劳动机构或核验个人分类。没有替读者判断全部职业豁免、跨州工作法选择、每个地方工资标准、全部合法扣款、扣税、集体协议、餐休安排或法院诉讼期限；正文没有给出这些个案结论。

作者证据中另列的 WA Getting Paid、NY Complaint Process 等探索来源没有在稿件独立承担关键断言，本次未把作者研究自动计为审阅者实读。采用的上述关键断言均已独立回源；未扩大为全套劳动法律审核。

工资年度、联邦 / 州豁免执行、地方 / 行业标准、行政受理条件或表件渠道改变时，重新核查相应段落。任何正文变更须重新计算摘要；涉及事实、数字、期限、对象或例外的改动须再事实审。
