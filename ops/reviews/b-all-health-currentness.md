# 全书医疗当期条件：只读事实缺口核查

2026-10-14（Asia/Shanghai），核查者banking_fact，root正式分派READONLY。本任务只写本新记录及事前核具体路径忽略的本人研究缓存，不改任何正文、章导读、作者包、验收、共享或B-PL记录，不构建提交。本轮以既有54篇集成基线中的五件为对象，六篇新候选另由主控处理；本记录不承载最终新稿FACT／THIRD或工程PASS。

## 首次落盘断点（历史）

首次落盘时为 **IN PROGRESS** 。当时尚未完成本轮四医疗正文的完整读取、退休稿相关段读取或任何外部采用段独立回源。root所给DSHS HR1页仅为定位线索，不继承其200或阅读。稍后逐件从实际文件算body／whole SHA，并记真正读到的范围；下载、目录、搜索摘文及旧审阅不能替代本轮实读。

范围：insurance-costs、coverage-changes、appointment-network、medical-bills完整正文，另选retirement-medicare涉及Medicaid及当期2026条件的段。重点现行非公民类别、2026-10-01后执行与法院保护范围、续期／终止／改买保障、混合家庭／儿童与语言人工入口。2027未来规则不作当前条件；其他金额／窗口仅在出现明确新变更线索时核关键断言，不扩全部医疗法律。

所有结论必须标具体正文路径／实际行、原文日期与本人采用段、失败及未核边界；必要修订只给唯一最小替换或补句，由root另行安装并派异人重绑。未核项目不写“无需改”或PASS。

## 本轮读取与版本绑定

2026-10-14实际完成本次限定范围的只读核查。四医疗文件从frontmatter至末行均由本人完整实读；退休稿只实读1—12、18—24、30—38、48—148行，不把未读的13—17、25—29、39—47行或全部退休法律计入本轮。首次关键词搜索输出截断只作定位；其相关段均另实际读取。此次又实读项目AGENTS及PROMPT的元数据／7.2／7.3段，并按BOOKMAP→TASKS→CHECKPOINT恢复；共享记录不代替本次正文和来源核查。

body按原UTF-8文本`full.split('---', 2)[2]`计算，保留全部换行；whole按实际文件原字节计算。以下均为已集成的当前文件，末轮重新算五件全部10摘要与最初读取值一致；没有改正文或核验日期。

| 实际文件 | 行数／字节 | 本轮正文SHA-256 | 本轮整文件SHA-256 |
| --- | --- | --- | --- |
| `content/book/people/health/insurance-costs.md` | 63／6125，全读 | `c9ffeddbe4ab79912751089ee35114d95e5264fa211a58e9dc3ac7be0a4c5d3b` | `c59989a3ae7fc4f451f8b811679a278c93b7447f1975d491306b00c5e5289e5e` |
| `content/book/people/health/coverage-changes.md` | 100／19376，全读 | `54f796e916ab7d1d0cc19fca99e8ffc8919a6bff161674e547ce17cee5da3943` | `dd093f87de1dad5a266854cec072235b006ef12d2cb04bcc584163d3c2ef79b8` |
| `content/book/people/health/appointment-network.md` | 59／6395，全读 | `4c8d3b8551eb31ed9778e29a6a5b9724ee1fbe6bbf53f9d409e8e10c85b76de6` | `91a9063db2e45001ae86f1250f39de4c98981041e034f9220656aacf875673e5` |
| `content/book/people/health/medical-bills.md` | 71／8705，全读 | `485addc8f652f6ebe777814fa5527e8c43f406519cf50d0d809a74be90304fd0` | `89d72e74ec31531fdffa889219c206fdc7b59b263738608d69bd537a3099340f` |
| `content/book/people/aging/retirement-medicare.md` | 全件148／28580；读取限上述范围 | `4aa59f4c2edea50131ebea65dfe3457875c5dde0c7db6292147b69f6aa6749d2` | `b91cd2db3b8e4566558014e28fc27b349333930d09086ee59237d4575f412dd0` |

## 本人实际一级回源

以下19个不同URL均为本轮本人实际新请求并读取相应主文或选页，没有继承root、作者证据或旧审阅的成功。查阅日均为北京时间2026-10-14，缓存UTC记录相应为2026-10-13晚间；原件发布／更新日另列，不将查阅日写成更新日。`hNN`指本人编号抽取件，web行号指本轮实际返回的原文；只对明列的段落作采用。检索摘文不计入这些采用范围。

| 一级来源 | 原件日期／版本；本人实际读取和采用范围 | 独立取得与失败边界 |
| --- | --- | --- |
| [DSHS：benefits and H.R.1](https://www.dshs.wa.gov/family-food-and-housing-services/dshs-benefits-and-hr-1) | 页首Updated October 2026；h01主文208行全读，医疗采用1—30：10/1变化、法院保护、LTSS请case manager更新身份。后续SNAP不采用于本医疗结论 | 真web初开超时；普通HTTPS DNS解析失败；正常8888、TLS校验开启取得200真实主文，不把两次失败删去 |
| [HCA：changes mean for you](https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/what-changes-apple-health-mean-you) | 未明列全页更新日；h02主文104行全读，6—24法院／非公民、25—61未来规则时间、65—96通知与人工分流 | 普通403；正常8888真200主文 |
| [HCA非公民事实表PDF](https://www.hca.wa.gov/assets/free-or-low-cost/hr1-noncitizen-fact-sheet.pdf) | 页内June 2026，共3物理页；113行全文提取实读，并逐张目视全部3页。采用1页类别与儿童／孕产例外、2页LPR五年期及豁免、3页更新资料／其他项目／办理分流；2页旧全体失保概括须与后来的SSI法院公告合读 | 普通403；正常8888真PDF200。原件SHA `02b9eb82d588c2588a71e465dc6f6b10de03ecbede02e6c2eb586f29125648f3`；不把June原件说成10月新版 |
| [HCA：法院保护800余人公告](https://www.hca.wa.gov/about-hca/news/announcements/court-order-protects-apple-health-coverage-more-800-washingtonians) | Thu,10/01/2026；h04主文15行全读，采用3—6：9/30西区联邦法院临时禁令，华州同时领取SSI且原本因此次新限制在10/1失保的人，HCA／DSHS保留保障并通知 | 普通403；正常8888真200。实际读州主管执行公告，未打开法院裁定全文，不外推所有非公民／全国或最终胜诉 |
| [HCA：Apple Health Expansion](https://www.hca.wa.gov/about-hca/programs-and-initiatives/apple-health-medicaid/apple-health-expansion) | 未明列更新日；h05主文126行全读，采用18—34目前满额与其他项目、109人工助手；1/1/2027转FFS只识别为未来 | 普通403；正常8888真200。其市场开放期结尾年份及若干隐私概括未采用，详见末节 |
| [Public Law119-21原法](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) | July4,2025；h06真读1—55首页、13475—13521的完整§71109、14840—14885的完整§71201。采用联邦资助限制10/1/2026及例外引用、Medicare新申请类别／既有成员18个月／通知义务 | 普通TLS真200全文原件已保存；全件19691行只读上述段落，非全法通读 |
| [CMS SHO26-001 PDF](https://www.medicaid.gov/federal-policy-guidance/downloads/sho26001.pdf) | April8,2026，共34物理页；只提取并实际全读物理1—10、428行，另目视5、8、9、10页。采用3—6页FFP和五年期／儿童孕妇州选项区别、7—8页dual eligible及不同Medicare起点、8—10页重核、材料、其他资格基础及终止前通知／听证 | 普通403；正常8888真PDF200，SHA `2c9e7ac1139c991b160912434b2d5990fe216a8691313dd39142299c09380e3b`。11—34页系统细则及附录未读；April指导早于September华州禁令，不能覆盖后者 |
| [HCA：Noncitizens当前主文](https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/noncitizens) | 未明列更新日；h08主文143行全读，1—21当前规则与SSI保护、32—68儿童／孕产／Expansion、73—127其他项目和五年期、128—138市场办理。1—7旧概括不能脱离17—21法院保护段 | 普通403；正常8888真200；未进入具体个人申请或所有下游资格表 |
| [HCA：Medicare Savings Program](https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/medicare-savings-program) | 未明列更新日；h09主文35行全读，9—11MSP是Medicaid费用帮助、无资产测试；27—32Washington Connection或纸件入口 | 普通403；正常8888真200；未打开本轮收入flyer、申请表或账户，不把无资产测试扩成没有身份／收入条件 |
| [Medicare当前费用](https://www.medicare.gov/basics/costs/medicare-costs) | 费用表明确2026；真web主文10—140实际读取，重点51—57；另h10独立主文89—116实读202.90／283／常见20%及assignment。未以本页推定2027价格 | 普通403；正常8888真200，另真web成功；不把248行抽取件全部称为通读 |
| [Medicare：provider accept Medicare](https://www.medicare.gov/basics/costs/medicare-costs/provider-accept-Medicare) | 未明列更新日；真web主文10—46及h11主文48行全部实读，重点定义和本人仍有免赔／共保 | 普通403；正常8888真200，另真web点击费用页真实链接成功；未打开个人provider查询或提交索赔 |
| [Washington Healthplanfinder：job loss](https://www.wahealthplanfinder.org/us/en/my-account/life-events/health-insurance-after-a-job-loss.html) | 未明列更新日；真web57—101实读：雇主保障前后60日、填写旧保障最后一天、申请帮助；不是从最后工作日起算 | 普通／正常8888均403；真web200有上述真实主文；账号、提交按钮与个人后台未操作 |
| [DHCS：身份类别表](https://www.dhcs.ca.gov/immigration-status-and-changes-to-medi-cal-eligibility/) | 页内chart准确截至August2026并注明至6/30/2027；真web39—106主文实读，采用既有成员／儿童孕产原寄养例外；2027列不作当前待遇 | 普通／正常8888均403；本人真web成功表行与说明，未读所有下游RMA／法律资料 |
| [DHCS：federal impact eligibility](https://www.dhcs.ca.gov/tracking-federal-impact-medi-cal-eligibility/) | Page last updatedSeptember21,2026；真web39—110主文实读，重点55—56：受10/1联邦变化影响的成员由州全范围维持至6/30/2027；57—72只辨未来时间 | 普通／正常8888均403；本人真web成功。74—98披露／公共负担新变化只作为不提供旧保证的界限，未打开判令或新规则全文，不新增具体移民结论 |
| [纽约AG：Essential Plan调整](https://ag.ny.gov/press-release/2026/attorney-general-james-issues-guidance-new-yorkers-facing-health-insurance) | June22,2026；h15主文45行全读，3—11的200%—250%收入组7/1退出及38—42免费办理入口。其9/1转换期限已过，不写成今天仍可用 | 普通TLS真200；本轮没有以新闻引出的所有保险金属等级、补助金额作新事实 |
| [NYC311：Health Insurance](https://portal.311.nyc.gov/article/?kanumber=KA-02767) | 未明列更新日；h16实际读1—85，采用50—72的已生效7/1退出、继续核其他保障、人工帮助。25—49的2027规则只辨未来 | 普通TLS真200；284行抽取件未全读，账户／请求回电／投诉功能未操作；不把单人金额范围套全家庭 |
| [DHCS：Medi-Cal Changes](https://www.dhcs.ca.gov/medi-cal/updates/medi-cal-changes/) | 未明列更新日；真web实读64—89的1/1/2026新申请冻结、保留／续保与例外，143—156的10月州过渡，183—213的当期与未来资产分界、381—387继续续办。采用仅这些段落 | 本轮本人真web从身份表链接进入；426行非全页通读，聚合输出162附近截断不计实读，未来低频服务未展开 |
| [Healthplanfinder：language support](https://www.wahealthplanfinder.org/us/en/tools-and-resources/how-to/language-support.html) | 未明列更新日；本人真web57—137主文英文段实读，95—112电话1-855-923-4633、多语言／TTY／线上或面谈助手，119—123资格异议可用首选语言 | 本轮本人真web从job-loss页点击真正入口；1303行语言总页只读该段，未把所有翻译PDF、申诉申请或其他语言正文计已读 |
| [DHCS：California MSP](https://www.dhcs.ca.gov/individuals/medicare-savings-programs-in-california/) | 当期表明确2026；本人真web39—86主文／表实读，采用46—47的A buy-in条件、1/1/2026恢复130000个人＋每人65000／最多10人，55—60县及MC14A申请入口 | 本轮真web成功；未下载新MC14A或县表，不把2027将来资产变化提前作用于2026 |

本人的原件／请求和失败日志只放已核忽略的`.cache/b-all-health-currentness-banking-fact/`，首次六源与后十源分`source-index.json`／`extra-index.json`；各保存件均再核具体路径`git check-ignore`，补充十源脚本还在每次请求前逐一核该次原件／抽取件／日志路径。普通TLS与正常127.0.0.1:8888均保留证书校验。PDF图片亦先逐路径核忽略再生成和实际查看。日志内“download_is_not_reading”或尚空读取栏是下载阶段记录；真正读取范围以上表为准，取得200本身不算读过。

## 逐项当期结论及最小建议

**本次发现：上述当前版本中，已核的10/1医疗资格／法院范围、华州／加州／纽约相关2026变化与2026费用没有需要事实补正的差异；仅退休L87的assignment需要一个有一级定义依据的中文释义建议。** 这是限定当期缺口核查完成，不是五篇最终FACT／THIRD PASS、全书医疗验收或工程通过。

1. `coverage-changes.md` L88（并结合L79、L90、L98）：无需事实补正。当前原文已列10/1受影响的非公民成人、转LPR／儿童／孕产分别核查、9/30同时领取SSI的一组保护、Expansion满额及继续查有限服务／市场。HCA六月PDF、当前noncit主文与10/1执行公告须结合使用；旧PDF“9/30以后失保”不能独占结论。当前书稿没有把该临时法院保护扩成所有非公民或保证Expansion接上，食品页线索不构成此稿遗漏。[HCA公告](https://www.hca.wa.gov/about-hca/news/announcements/court-order-protects-apple-health-coverage-more-800-washingtonians)

2. `coverage-changes.md` L14、L24、L55、L69、L82—90、L98：在本次变化范围无需补句。书稿已逐成员核结果，不把普通成人拒绝推广到孩子／孕产者；L90已分老人／Medicare／LTSS／残障负责单位，L98要求保存通知、补件和递交记录。HCA实际人工入口和Healthplanfinder首选语言帮助足以让读者继续核具体类别；本轮没有操作真实申请或承诺所有家庭成员同批获准。CMS SHO8—10页亦要求评估其他基础并给终止／复核通知，不能把单一身份变化当“自行停保”的依据。[CMS当前指导](https://www.medicaid.gov/federal-policy-guidance/downloads/sho26001.pdf)、[语言帮助](https://www.wahealthplanfinder.org/us/en/tools-and-resources/how-to/language-support.html)

3. `coverage-changes.md` L79、L88及`retirement-medicare.md` L72、L114、L117：本次核到的分流和无资产测试仍成立，无需事实替换。HCA给19—64与65岁／Medicare／残障／LTSS不同办理路线，MSP当前主文明确无资产测试但须满足项目资格。CMS SHO4页脚注14、7—8页明确Medicaid资助限制涉及MSP，不能把既有Medicare的18个月保护期推到MSP；书稿没有这种推断，L117已要求身份／居住及适用项目审核，L72已链接保障接续。本轮不新增一个未经逐州核实的统一MSP终止日期。[HCA MSP](https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/medicare-savings-program)

4. `coverage-changes.md` L84：无需事实补正。本人独立真读DHCS的新申请冻结主文及身份表，1/1/2026冻结、既有成员按时续保／仍符合条件、儿童／孕产／原寄养例外，与书稿相符；9/21联邦影响页和当前Changes页均支持受10月变化影响成员的州全范围过渡至6/30/2027。2027FFS／牙科／资产后续变化没有被书稿说成当前已经执行。[DHCS现行变化](https://www.dhcs.ca.gov/medi-cal/updates/medi-cal-changes/)

5. `coverage-changes.md` L78、L86：无需事实补正。纽约AG的6/22主文与当前NYC311明确7/1/2026退出原200%—250%组；正文已让收入高于200%的家庭重查，不重复已经过去的9/1专项转换截止日。没有把当前NYC311的2027工作／续期规则说成今天生效。[NYC311当前说明](https://portal.311.nyc.gov/article/?kanumber=KA-02767)

6. `retirement-medicare.md` L52：无需事实补正。本人实读原法§71201全段，7/4/2025现有成员18个月后适用、通知义务与当前书稿的1/4/2027未来日期相符；§71109及CMS当期指导中的10/1 Medicaid日期是另一制度起点。此稿没有提前终止既有Medicare或把一种身份直接当完成全部年龄／缴费／居住条件。[原法§71201](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)

7. `retirement-medicare.md` L87、L112：本人实际当前费用页支持B部标准月费202.90、年免赔283、接受assignment时常见20%个人分担；当前DHCS MSP页支持加州2026恢复的资产数值及县办理路线。无需改数字、年份、条件或既有链接。L87原句唯一片段`（服务提供者接受assignment时）`建议最小替换为`（服务提供者接受assignment（同意以Medicare核准额作为全额收费）时）`。理由：现行Medicare定义页面明确以承保服务的核准额为全额收费，同时患者仍付适用免赔／共保；补中文可让首次遇术语的读者理解20%算在哪个金额上，不能改成“全额报销”。原费用链接已就近支持定义，不需要新增未经实读的规则。[2026费用](https://www.medicare.gov/basics/costs/medicare-costs)、[assignment定义及本人分担](https://www.medicare.gov/basics/costs/medicare-costs/provider-accept-Medicare)

8. `insurance-costs.md`、`appointment-network.md`、`medical-bills.md`：各已完整读，当前scope分别限定普通个人／雇主成本、预约网络核查和以Marketplace申诉为例；未看到把旧的华州非公民资格、SSI保护或Medicaid变化错误推广为通用保险条件。它们分别保留计划具体SBC／确认、逐人资格去保障接续、Medicare／Medicaid另按本通知办理的路径。针对此次明确变化线索无需事实补正；不由此推称本轮重新验证了全部网络／No Surprises／GFE／理赔申诉／医院援助规则。尤其`medical-bills.md` L55本已禁止套用前述180日／4个月到Medicaid，而本轮没有重新开其全部申诉原法。

## 未核实与不能扩大之处

- 没有打开September30法院裁定全文、后续案卷或独立核全部诉讼，结论只采10/1HCA及当前HCA／DSHS执行公告里华州SSI受影响组；不是全国临时禁令解释。CMS April信的旧一般处理不能抹去这个后来的实际州执行分支。
- HCA六月事实表与当前主文给儿童／孕产、调整成LPR、五年期豁免等具体范围，本轮只用其支撑正文的“分别核查”；没有写新的全国儿童无身份限制承诺，没有完整核所有签证、RMA、MCS、AEM、移民表件、个案终止或每州资金细目。未把全国FFP条件与所有州自费资格混成同一条件。
- HCA当前变化页65+电话列`1-800-501-4633`，其June PDF和当前Noncitizens的DSHS路由列`1-877-501-2233`，来源内容和对象不同；本轮都真实读到，没有拨号或断定一个号码错误。正文目前用具名单位／助手分流，没有硬写这两个号码，故无须以未实拨的判断改稿。
- Expansion页面已真读且满额核实，但其开放期句把终止年写作“January15,2026”且若干隐私表述不宜独占结论；本轮不采用这些句子，不自行生成正确的2027窗口。Healthplanfinder语言页“人人可买”只用于其具名州市场入口，不扩成人人可获免费Apple Health或联邦补助。
- DHCS9/21页出现近期公共负担及资料分享变化，HCA也有法院／数据分享说明；没有全读相关新联邦规则或裁定，故不新增私人资料永不分享、福利绝无移民影响或个案必然不利的结论。当前`coverage-changes.md` L90本已要求当前官方说明与合格法律帮助，五件此次读取的段落没有旧版全体保证需要删除。
- 2027工作／续期／追溯／FFS、2028共付或2027费用只识别为未来；没有为变化本身往当前正文塞新条件。其全部实施例外、法定更新和未来名单未作本轮完整事实审。纽约下一年度投保窗口、得州全部类别、COBRA、SSA福利金额、GFE争议及雇主各窗口也不冒称新审通过。

## 交回状态

本次限定范围只读缺口核查 **完成** ：已核的当期变化没有必须事实修正文句；有上列L87单处中文释义建议，由root与原作者门禁另办。本轮没有修改正文、作者包或任何核验字段，未改B-PL记录、共享账本或他人审阅，没有构建、提交、账户操作或联系机构。五件末轮10摘要与本轮初读相同；本记录不能用于追认任何未来修改后的正文FACT／THIRD／工程PASS。
