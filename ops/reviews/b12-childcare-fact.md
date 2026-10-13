# B12 托育：独立事实审

2026-10-13，独立事实审 `root`；作者 `birth_fact`，第三静态 `banking_fact` 尚待正式派发。本记录只给当前冻结稿事实 PASS，不能代替第三审、候选元数据、隔离构建、真实渲染或正式集成。

审阅路径 `content/book/people/family/childcare.md`，115行、23,829字节；正文 SHA-256 `b207514914db15706c42fcc8ee12041b07a5fa9460e26a657353fcbf737d413f`，整文件 `4493b2ec5bd93876ff53965baec42d6ebda505b47251e1435f4e4ee50adc3076`。正文算法为UTF-8全文 `split('---', 2)[2]`，保留前导换行。对应地图44行 SHA `bd8d8cde442cdb2e03cf6b4af85a5ad9f0d8d03ecd2232491e884a7aa95e2faa`，作者证据96行 SHA `3fbd1396a12a4f85c5256a8b6ed16974d5d673c4b00434287dda8a84a922c184`。本人完整读正文、地图及证据；长输出曾截断，正文按1–58／59–115、证据按1–48／49–96补读。收口再次完整读正文115行并复算上述四摘要，元数据仍为written／draft true、verified及reviewed_by空。

## 独立取得与真实阅读

本人从正文抽出50个不同外部URL重新请求，下载前逐一验证151个缓存路径均忽略。默认Python缺requests的首次脚本在请求前失败；改用现有checks虚拟环境。正常TLS直接及正常8888代理请求，38份200（34HTML、4PDF），12份失败；200只证明取得，不证明读过。随后本人打开下表采用段，失败网页分别经网页工具回源。没有绕证书、挑战、登录真实门户、提交申请或联系机构。

原件及每次渠道成败存忽略缓存 `.cache/evidence/b12-childcare-root-fact/`；下表00–49与本人脚本索引一致，行号是本人的提取或网页工具行号，不借作者行号充作阅读。最终49个正文原URL有本人实际采用段；24原about-us仍超时／网页错误，以本人真读的县主管板页及同机构现计划页交叉核服务区。另实际读到六月得州被无改采纳文本，共52个不同来源URL有实际采用段。地方资金、表格和页面存在时间边界，未以搜索摘文作资格证明。

| 索引、一级来源 | 本人实际读到与采用边界 |
| --- | --- |
| 00 [托育类型](https://www.childcare.gov/consumer-education/what-are-my-child-care-options) | 正常TLS主文50行全读；类型、时段和参加补助的机构分开，不作具体名额证明。 |
| 01 [合同与家庭责任](https://www.childcare.gov/consumer-education/find-and-choose-quality-child-care/your-responsibilities-once-you-find-care) | 40行全读，报价、政策、病假、关门、取消及留合同；不推全州统一退费。 |
| 02 [寻找并选择](https://www.childcare.gov/consumer-education/find-and-choose-quality-child-care/simple-steps-for-finding-and-choosing-child-care) | 50行全读，查许可与整改、问实际名额和现场／远程访问。 |
| 03 [加州R&R网络](https://rrnetwork.org/family-services/find-child-care?zip=) | 本轮主文17行全读；ZIP、本地顾问、MyChildCarePlan及人工支持，未实际查询某ZIP。 |
| 04 [CDSS许可查询](https://www.cdss.ca.gov/inforesources/community-care-licensing/facility-search-welcome) | 36行全读；五年记录、更旧区域办公室、仍须访托；无具体机构结论。 |
| 05 [OCFS搜索](https://hs.ocfs.ny.gov/dcfs) | 817行中实际1–75、730–817；当前类型／状态、查询及NYC中心转接；中间县校选项未全读，不称查遍机构。 |
| 06 [NYC Child Care Connect](https://access.nyc.gov/programs/nyc-child-care-connect/) | 正常失败，本人网页工具142行全读；中心检查及不安全／不卫生／违法经营311报告。 |
| 07 [NYC监管类别](https://www.nyc.gov/site/doh/business/permits-and-licenses/children-and-adolescents-childcare.page) | 正常失败，网页68行全读；DOH中心与州家庭等类别不同。 |
| 08 [WA Child Care Check](https://www.dcyf.wa.gov/services/earlylearning-childcare/child-care-check) | 17行全读；许可、成立投诉及检查；未把供应人名额字段当实时保证。 |
| 09 [Child Care Aware家庭服务](https://childcareawarewa.org/family-services/) | 本人正常TLS成功主文24行全读；家庭转介及800-446-1114。 |
| 10 [TX HHS托育入口](https://www.hhs.texas.gov/services/family-safety-resources/child-care) | 39行全读；Search Texas Child Care、许可投诉与虐待分流。 |
| 11 [TX照护类别](https://www.hhs.texas.gov/services/family-safety-resources/child-care/frequently-asked-questions-about-texas-child-care/what-are-types-child-care-operations) | 130行中1–80实际读；licensed、registered、listed家庭照护及listed无常规检查；后续residential未用。 |
| 12 [监测和检查](https://childcare.gov/consumer-education/regulated-child-care/monitoring-and-inspections) | 11行全读；日期、违规、整改和成立投诉，不推没投诉即安全。 |
| 13 [TX检查报告](https://www.hhs.texas.gov/services/safety/child-care/frequently-asked-questions-about-texas-child-care/what-are-ccr-reports-inspections-enforcement-actions) | 50行全读；重复违规、纠正与不同监管动作，不给真实机构评分。 |
| 14 [许可及豁免](https://childcare.gov/consumer-education/regulated-child-care/child-care-licensing) | 63行全读；最低要求、依法豁免／违法无证及补助额外要求。 |
| 15 [访托问表PDF](https://www.childcare.gov/sites/default/files/2017-12/ChildCare_govFull%20checklist-EN-Final.pdf) | 真6物理页、327行全读；首次尾部截断另补300–327。页内2018；只用于监督、接送、应急、过敏、用药、语言、沟通等问项，旧比率和临床细则未当2026统一法律。 |
| 16 [NICHD安全睡眠](https://safetosleep.nichd.nih.gov/reduce-risk/safe-sleep-environment) | 84行全读，长输出另独立补全；坚实平坦、软物、成人床与沙发风险，未扩为完整临床方案。 |
| 17 [DOJ托育ADA](https://www.ada.gov/resources/child-care-centers/) | 190行中本人实际1–102；Q1–6、9、13已读，政府／私营／直接宗教经营、个别评估、修改与例外及不能另收ADA必需服务费；未把余问题当已读。 |
| 18 [CDSS家长路线](https://www.cdss.ca.gov/inforesources/calworks-child-care/parent-information-and-resources) | 本人119行全读；县CalWORKs、APP及原个案停止日期；未采用错位旧热线或未核所有项目身份条件。 |
| 19 [OCFS正式申请路线](https://hs.ocfs.ny.gov/CCAPeligibility/Home/SurveyQuestions?answer=false&questionNumber=3) | 80行全读；筛查仍可接正式申请、线上／LDSS，不把示例化条件结果作真实家庭资格。 |
| 20 [ACS申请](https://www.nyc.gov/site/acs/early-care/apply-child-care.page) | 正常失败，网页71行全读；10小时等理由、residency／收入、非现金新券资金等候、已有券及时续认、线上不重复寄纸及HRA分支。 |
| 21 [WCCC主文](https://www.dcyf.wa.gov/services/earlylearning-childcare/getting-help/wccc) | 295行中1–30、210–295实际读；申请844-626-8687、多语言、可先申请后选机构、材料。网页旧自付例子未采用，按31新表；FFN照顾者身份未移给孩子。 |
| 22 [WCCC权利与责任](https://dcyf.wa.gov/services/earlylearning-childcare/getting-help/wccc/rights-responsibilities) | 67行全读；免费语言、复核／听证、每日获准签到签退、换机构五日、授权及可另收的特定费用。通知旧简写未套现法。 |
| 23 [TX3C申请步骤](https://www.childcare.texas.gov/for-families/child-care-scholarships/ccs-application-steps-for-families) | 正常失败，网页49行全读；waitlist→邀请Standard Application、每90日确认及按实际通知补件；未把通常两周写统一邀请截止。 |
| 24 [Gulf Coast服务区原页](https://www.wrksolutions.com/about-us) | 本人正常、正常代理及网页多次超时／internal error，尾斜线及搜索ref重开仍失败。未继承作者150行实读；采用下列两个一级替代材料核Houston-Galveston地方范围，不声称本页恢复。 |
| 25 [Gulf Coast托育补助](https://www.wrksolutions.com/childcare-financial-assistance) | 正常超时，本人网页236行中55–155实际读；713-334-5980、2026-10-01—2027-09-30收入资料、当前waitlist及换托两周。后续重开失败保留；13周与34清单12周不同，不写统一收入取样期。 |
| 26 [CA资格事实单PDF](https://www.cdss.ca.gov/Portals/9/CCDD/FactSheets/CDSS-Child-Care-Eligibility-Fact-Sheet.pdf) | 真2物理页、88行全读，标2/12/26；资格路线加need、CalWORKs县／APP分工，不从缺身份字段推出全部非公民资格。 |
| 27 [ACS表格](https://www.nyc.gov/site/acs/early-care/forms.page) | 正常失败；初网页只有元信息，另本人重开真正读15–102；中文、工资／自雇／学习／求职证明，不声称每个附件都读。 |
| 28 [MOIA家庭服务](https://www.nyc.gov/site/immigrants/city-services/family-services.page) | 正常失败，网页237行中130–177实际读，137–144只对所申孩子要求移民材料；未据Head Start／PromiseNYC概述给当前完整资格。 |
| 29 [Tompkins县CCAP](https://www.tompkinscountyny.gov/All-Departments/Social-Services/Child-Care-Assistance-Program) | 正常280行中1–145、215–251、250–280实读；35–145另补防截断。50–63当前资金等候、完整合格才列入、TA继续及续认homeless／低于300%SIS／特殊需要；230–256纸表607-274-5612和递交／email／邮寄。67旧普通300%FPL与79–144现85%SMI表冲突，正文未采用旧线，SIS优先非普通门槛。 |
| 30 [WAC110-15-0005](https://app.leg.wa.gov/wac/default.aspx?cite=110-15-0005) | 107行全读；初次≤60%SMI、重申≤65%、资产／欠自付处理、学徒／托育从业／高中路线及首资格日年龄与WA居住。 |
| 31 [WA新自付表PDF](https://www.dcyf.wa.gov/sites/default/files/pdf/copay_calculation_table.pdf) | 真1物理页、38行全读；Effective10/1/26、Revised9/8/26，收入与自付档不抄旧网页65／90例子。正文要求经办人核，不复制家庭金额。 |
| 32 [DCYF实施更新](https://dcyf.wa.gov/services/early-learning-providers/subsidy/legislative-updates) | 80行全读；普通扩到75／85%计划取消，新表10/1生效；未来供应人变化未提前施行。 |
| 33 [DCYF会议PDF](https://dcyf.wa.gov/sites/default/files/pdf/032525_EOTaskForce_Minutes.pdf) | 真5物理页、196行中90–155实际读，物理3页124–139州资金服务未满足联邦孩子身份条件的说明。明确2025-03-25并要求核当期安排；未称整5页读完或2026所有家庭必合格。 |
| 34 [TX当前材料PDF](https://www.childcare.texas.gov/sites/default/files/CCS/Docs/ccs-eligibility-documentation-log.pdf) | 正常及直接网页失败；本人从家庭表格真实链接点击取得网页工具真15页／599行，先读0–150，本轮再从同一实际返回原件读145–330，实际到物理8页开头，非整15页。标10/2026；108–114美国国民独立证明、176–265住址／收入／照护理由、302起成人身份；无工资单的核验形式。后续ref／重新点击403或错误保留，没有本人二进制SHA。 |
| 35 [TX CCS条件](https://www.childcare.texas.gov/for-families/child-care-scholarships) | 正常失败，网页118行全读；25单亲／50双亲合计活动、年龄、家庭费用、换托至少两周，宽泛eligible表述结合现规则及34，不把任一条件当足够。 |
| 36 [TX最终采纳](https://www.sos.state.tx.us/texreg/archive/September182026/Adopted%20Rules/40.SOCIAL%20SERVICES%20AND%20ASSISTANCE.html) | 正常359行中1–50、245–256、300–314实际读并补截断；22–24无改采纳六月资格文本，A–E自10/1、G自11/1；资格子章10/1已生效，未来G未当今天生效。 |
| 37 [TX家庭表格](https://www.childcare.texas.gov/child-care-services/ccs-forms-families) | 正常失败，网页54行全读；Inclusion Assistance父母先填、当地接续和家长出勤要求，未打开真实账户。 |
| 38 [CA家长申诉](https://www.cdss.ca.gov/inforesources/child-care-and-development/parent-resources/parent-appeals) | 96行全读，28／34当地14日从收到NOA起及及时请求继续最后服务；54后续复审须CDSS收到、从当地决定书印日期起14日，不混起算、不套全部现金补助。 |
| 39 [ACS券服务／申诉](https://www.nyc.gov/site/acs/early-care/support-families-vouchers.page) | 正常失败，网页64行全读；共同签CFWB049回交→正式入托、换券、HRA／过渡个案另办、拒绝notice date起60日听证且可不等conference，虐待800-342-3720／急险911。 |
| 40 [WAC110-15-0280](https://app.leg.wa.gov/wac/default.aspx?cite=110-15-0280) | 89行中1–50实际读；家庭90个日历日从收到决定起，good cause例外；供应人追偿程序未移家庭。 |
| 41 [WAC110-15-0025](https://app.leg.wa.gov/wac/default.aspx?cite=110-15-0025) | 79行中1–56实际读；语言／复核、授权费率差额、缺席／自选休假关门限制，无理由／无须预告托育方终止但5日告知DCYF；实际现法与2022效期，不把普通合同条款套WCCC。 |
| 42 [WAC110-15-0034](https://app.leg.wa.gov/wac/default.aspx?cite=110-15-0034) | 93行中1–70实际读；授权时段、许可托育收费与补助账务／材料／争议禁费，允许额外时段另核，不写全部费用皆禁。 |
| 43 [CA家长安全权利](https://www.cdss.ca.gov/inforesources/child-care-and-development/parent-resources/parental-rights) | 本人正常主文10行全读；怀疑虐待先移开孩子、核记录／可匿名，不复制旧错位电话。 |
| 44 [DFPS报告](https://www.dfps.texas.gov/Contact_Us/report_abuse.asp) | 本人93行全读；800-252-5400、9/1/23起儿童报告姓名及电话、911急险、儿童托育涉嫌虐待；ICF成人机构不同受理未移此页。 |
| 45 [CA许可投诉](https://www.cdss.ca.gov/inforesources/ccld-complaint-hotline) | 133行全读；托育中心／家庭844-538-8766、匿名／留联系人及免费口译翻译；调查十日访问不当办结保证。 |
| 46 [OCFS投诉及监管](https://hs.ocfs.ny.gov/DCFS/Search/GetProblematicProviders) | 266行中1–28、183–266实际读；218为800-732-5207，成立／pending与吊销不同；未查完动态名单或对真实机构下结论。 |
| 47 [WA托育投诉](https://www.dcyf.wa.gov/safety/child-care-complaints) | 36行全读；安全／虐待及疑无证866-363-4276，不把工作日调查期限当孩子应等待。 |
| 48 [TX CCR所在地办公室](https://www.hhs.texas.gov/services/family-safety-resources/child-care/contact-child-care-regulation) | 203行中1–85实际读；日间地区及intake／general联系、休斯敦，正文只指所在地目录。未称全部办公室读完或24小时可现场受理。 |
| 49 [TX CCR／DFPS手册](https://fhb.hhs.texas.gov/handbooks/child-care-regulation-handbook/6200-receiving-assessing-processing-intake-reports) | 807行中1–139实际读；6210 Revision25-3／8/15/25、6220普通日间标准与虐待／忽视／儿童死亡转SWI，匿名CCR与DFPS法定实名要求分开。未称全807行读完。 |

三份额外实际一级采用来源：[得州六月文本](https://www.sos.state.tx.us/texreg/archive/June52026/Proposed%20Rules/40.SOCIAL%20SERVICES%20AND%20ASSISTANCE.html)，本人网页1357行中683–711、785–808、823–838及先前850–1050实际读；§809.41本地、年龄、身份、收入／资产与§809.52等专门路线结合36采纳，非仅凭提案写现法。[Harris County主管板说明](https://harriscountytx.granicus.com/boards/w/b97df4edf6fda4d2/boards/42972)，本人网页285行实际返回全读，9–11说明Workforce Solutions与Houston-Galveston服务区；只采用机构关系和区域，不采用董事／名额／任期信息。[Gulf Coast现计划页](https://wrksolutions.com/about-us/plans)，本人网页129行全读，72、83–85核地区及机构关系；不把计划当家庭资格。TWC目录搜索后直接打开仅3行网页壳，未当PDF成功或完整目录阅读。

本人实际取得四件PDF二进制SHA：15 `9ba323a240d66f95f0e46753d3aaa71e48ac3d623154b7772705284caa44f35c`；26 `4837cc4fe1f0f0dc4fd226e9be4aa51d8ab9677326f00277fb53c350ac33752e`；31 `13c4a63acf09fae6af3a2a6b2aa84c8a2a689f0a9456700e6a38a11f7efc66da`；33 `1467445a1310cdc9c5e5086041da8e5491afffcf5230107d622fcf9e6572668b`。其中33只读采用页，二进制下载摘要不等于全件已读；34只有真网页PDF采用段，不能编原件摘要。

## 结论与未核边界

事实 PASS，无必要作者返修。正文按地区和项目放资格、文件、起算点与例外；许可和实际质量、申请／资金等候／发券、孩子身份／成人身份证明、补助授权／机构合同、投诉／申诉都能分别继续。两张四州表与临近普通链接可追到实际采用段。SIS续认优先不冒称纽约普通资格；WA新表和取消扩大政策有当前版本；TX美国国民和10月已生效资格规则保留精确边界。未凭13周／12周冲突统一收入样本，未给新券或真实名额保证。

没有核真实家庭资格、个案收入资产计算、当日是否发券、机构实时质量与名额、后台申请或儿童材料；CA全子项目移民资格、Head Start／PromiseNYC完整现资格、所有县资金优先、全部照护类别比例、雇佣税、医疗／监护法律和所有听证司法程序不在本稿断言范围。2025州资金说明只作为问DCYF当期路线的依据。24原入口独立未读边界已明确，地域事实由两个实际一级替代来源交叉核，不继承他人阅读。第三审需重新核当前路径与摘要；任何正文改动均使本PASS失效，必须重新事实审。
