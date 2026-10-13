# B12 托育：第三人静态与编辑审

2026-10-13，第三审 `banking_fact`；原作者 `birth_fact`，独立事实审 `root`，三名不同参与者。结论 **静态／编辑 PASS**，没有必要作者返修。本记录承接下述准确版本的独立事实审；只给静态门禁结论，工程、手机与打印实看、候选安装及正式集成由主控继续办理。

## 实际版本、读取与职责

- 正文：`content/book/people/family/childcare.md`，115行、23,829字节；完整正文 SHA-256 `b207514914db15706c42fcc8ee12041b07a5fa9460e26a657353fcbf737d413f`，整文件 SHA-256 `4493b2ec5bd93876ff53965baec42d6ebda505b47251e1435f4e4ee50adc3076`。正文按UTF-8全文 `split('---', 2)[2]` 保留全部换行实算。
- 地图：`ops/maps/childcare.md`，44行、8,106字节，SHA-256 `bd8d8cde442cdb2e03cf6b4af85a5ad9f0d8d03ecd2232491e884a7aa95e2faa`。
- 作者证据：`ops/evidence/childcare.md`，96行、30,227字节，SHA-256 `3fbd1396a12a4f85c5256a8b6ed16974d5d673c4b00434287dda8a84a922c184`。
- 独立事实记录：`ops/reviews/b12-childcare-fact.md`，74行、17,871字节，SHA-256 `bfa7483ab9284094bcc3d5509734c25e716fcf9f1fd2f68e5206657fa11a4211`，当前事实PASS绑定相同正文与整文件摘要，无待作者事项。

本人先读上级与项目AGENTS，依序完整读最新BOOKMAP40行、TASKS53行、CHECKPOINT52行，再检查实际文件与Git。完整PROMPT已于前序连续工作实际读过，本轮重读§7.1—7.3、独立审阅门禁及99行说人话标准。本轮正文实际分1—58／59—115完整读，地图44行完整读，作者证据分1—32／33—64／65—96完整读，事实记录分1—38／39—74完整读；不是用摘要、标题、搜索摘文或作者自查代替整稿阅读。本人初读、格式核查和收口分别实算正文摘要，均一致；四份送审文件没有本人修改。

作者地图与证据顶部的“待正式分派／未开始”是作者冻结时状态，后续事实记录有正式不同参与者及完整版本绑定；本审不把作者冻结记录当审阅PASS。root的49个原URL及额外材料实际回源属于root，作者实际成功属于birth_fact，均未登记为本人已读。本人的关键抽查范围见下表，其余事实采用范围承接已完整读到的独立事实记录。

## 结构、行动与适用条件

开头直接说明找实际名额、核照护与合同、获准后再将补助计入预算。六个二级标题按时段／交通／预算→候选与地址许可→访托、特殊需要及合同→费用支持的申请、材料、等候与申诉→付款授权及首日交接→危险、投诉与换托展开。没有只有入口而缺下一步的清单；没有把许可、筛查、等候或收到券概括成已经有名额或可以付款。

全国核问使用ChildCare.gov及必要NICHD、DOJ依据；四州项目与实际地方入口在会改变动作处出现。纽约市中心和OCFS监管类别分开，得州listed家庭照护与许可／登记、普通CCR投诉与DFPS虐待报告分开。偏远家庭有相邻地区、家庭托育和交通继续路径；轮班、双孩子、亲友照护、语言、残障、过敏、监护与接送在选择或交接位置提出实际问题。没有将公立K–12身份规则移给托育补助，也没有将成人身份文件等同孩子项目资格。

申请段明确查阅至2026-10-13。NYC非现金新券资金等候与已有券续认、Tompkins新申请与部分续认等候及SIS优先例外分别限定；普通收入门槛没有套用旧300%FPL或续认300%SIS。WA普通初次60%SMI、重申65%、特殊路线与已取消普通75%／85%扩展并列，新自付表按10月1日版本，2025州资金说明只用于向DCYF核当期路线。TX美国国民独立保留，普通活动25／50小时不移给初次求职、无家可归及保护转介；10月资格规则与11月尚未来到的G子章没有混写。没有采用地方13周／材料12周差异作为统一收入取样期。

四地申诉规则写在拒绝／减额／停止通知之后：CA当地14日从收到NOA起，后续14日须CDSS收到且从地方决定书印日期起；NYC拒绝notice date起60日，不用先等conference；WA家庭从收到决定起90个日历日并保留good cause。取得付款授权和入托确认后才进入交接；ACS共同完成CFWB049并取得正式通知的步骤没有省去。WCCC已授权照护的收费限制与额外允许收费分开，换托段保留无理由／不须预告托育方终止但五日告知DCYF，以及换托育方后五日告知；TX至少提前两周请求转机构有自己的项目限定。

危险先911或移开孩子再接经办人，许可投诉、虐待报告和纯收费争议分别继续。最后记录合同、授权、负责人、时段、费用、续认和待办，具体信息均可用于下次联系，没有空泛收尾。

## 本人实际一级来源抽查与访问边界

查阅日均为2026-10-13，来源所印日期与本次查阅日分开。本人14个原URL新普通TLS请求之前，逐一 `git check-ignore -v` 核 `.cache/childcare-third-banking/index.json` 及s01—s14各raw／txt／json共43个具体路径，均命中 `.gitignore:2:.cache/`。新请求9份200、5份普通与正常127.0.0.1:8888均403；成功后才另开下列采用段。提取宽搜索曾截断，只作定位，下列实际段另行完整显示并阅读。网页工具取得的PDF只记录本人真读页段，没有本人二进制缓存或虚构原件SHA。未绕TLS、挑战或真实账户。

| 本人实际来源与渠道 | 实际读到的段／版本及本审用途 |
| --- | --- |
| [CDSS家长申诉](https://www.cdss.ca.gov/inforesources/child-care-and-development/parent-resources/parent-appeals)，新普通TLS200，s01 | 提取24—95实际读，Title5 §§18118及后续；47／49／53收到NOA起14个日历日及及时请求继续最后同意服务，73／84后续CDSS须收到且地方letter date起14日。没有称124行全读或全部CalWORKs现金听证适用。 |
| [ACS申请](https://www.nyc.gov/site/acs/early-care/apply-child-care.page)，本人普通／8888均403后真网页主文 | 真正读完整71行，20—27不同照护理由和每周至少10小时工作，32—36非现金家庭新券等候、已有券须按期续认及线上勿重复纸件，53 HRA路线。页脚2025没有当规则更新日。 |
| [ACS券服务、申诉与换托](https://www.nyc.gov/site/acs/early-care/support-families-vouchers.page)，本人普通／8888均403后真网页主文 | 完整64行，29—34共同签CFWB049、回交、正式入托通知／transfer voucher及HRA、TCC另办；40—43拒绝notice date起60日及不须先conference。46—52许可投诉／虐待报告及911分流亦实际读。未进入门户、未读所链每份表。 |
| [Tompkins县CCAP](https://www.tompkinscountyny.gov/All-Departments/Social-Services/Child-Care-Assistance-Program)，新普通TLS200，s04 | 708行含大量导航，本人实际443—485、536—549、620—662；449—462当前新申请与续认等候、完整合格才列入、续认三种优先和TA继续；478现表区间2026-06-01—2027-05-31、544 SIS用于优先；629纸表电话及645—655递交／email／邮寄。没有称全708行读完，没有采用466旧普通300%FPL或其他家庭个案金额。 |
| [WAC110-15-0005](https://app.leg.wa.gov/wac/default.aspx?cite=110-15-0005)，新普通TLS200，s05 | 118—165实际读，普通初次≤60%／重申≤65%、资产／欠自付、学徒／从业者／高中路线；孩子第一资格日年龄及居住。当前印WSR24-20-130、2024-11-01生效。未把未列公民字段推免除身份核验。 |
| [WAC110-15-0025](https://app.leg.wa.gov/wac/default.aspx?cite=110-15-0025)，新普通TLS200，s06 | 118—153实际读，133复核不影响听证，134免费语言服务，140无理由／无预告托育方终止但五日告知DCYF，141—148费率差额、缺席和自行休假限制。所印WSR22-05-007、2022-03-06生效。未推所有额外项目都禁收。 |
| [WAC110-15-0280](https://app.leg.wa.gov/wac/default.aspx?cite=110-15-0280)，新普通TLS200，s07 | 118—173实际读，家庭125—137及90 calendar days从received起、good cause；供应人28日追偿是另一类。所印WSR23-12-037、2023-07-01生效，没有移供应人期限给家庭。 |
| [WCCC权利与责任](https://dcyf.wa.gov/services/earlylearning-childcare/getting-help/wccc/rights-responsibilities)，新普通TLS200，s08 | 真读全部67行，16免费语言、23—31已授权收费限制、36换托育方五日、37每日获准签到签退、39—49允许额外照护及可收费项目。网页10日通知简写没有写进正文；末段FFN照顾者身份没有移为孩子资格。 |
| [DCYF2026实施更新](https://dcyf.wa.gov/services/early-learning-providers/subsidy/legislative-updates)，新普通TLS200，s09 | 实际1—4、42—61；当前ordinary eligibility、10月新自付表与51取消75%／85%普通扩展；61未来2027供应人项目未提前采用。没有称80行全读。 |
| [WA新自付表](https://www.dcyf.wa.gov/sites/default/files/pdf/copay_calculation_table.pdf)，本人真网页PDF | 真1物理页、44行全读；Revised2026-09-08、Effective2026-10-01；41—43的85%收入列用于资格期间重定，不是初次申请线。正文没有复制家庭各档金额。无本人下载二进制摘要。 |
| [DCYF2025会议记录](https://dcyf.wa.gov/sites/default/files/pdf/032525_EOTaskForce_Minutes.pdf)，本人真网页PDF | 真5物理页、156行返回，本人核第1页0—5日期、物理第3页101—112 WCCC采用段；记载2025-03-25州资金服务不满足联邦孩子身份条件的路径。没有称整5页全读、没有把旧会议记录视作2026资格保证。 |
| [得州9月18日最终采纳](https://www.sos.state.tx.us/texreg/archive/September182026/Adopted%20Rules/40.SOCIAL%20SERVICES%20AND%20ASSISTANCE.html)，新普通TLS200，s11 | 359行中1—28、245—258、296—315实际读；22—24资格文本无改采纳六月文本，252—256 A—E10月1日／G11月1日分期，300—314资格子章10月1日生效。不是整359行全读。 |
| [被采纳的得州六月文本](https://www.sos.state.tx.us/texreg/archive/June52026/Proposed%20Rules/40.SOCIAL%20SERVICES%20AND%20ASSISTANCE.html)，新普通TLS200，s12 | 1743行中620—689实际读，§809.41孩子未满13／残障未满19、依法核孩子身份／地方服务区、收入资产及照护理由。和上述实际采纳、日期相接，不仅凭提案认现行。没有称全部专门路线、§809.52或整法本次重读。 |
| [MOIA家庭服务](https://www.nyc.gov/site/immigrants/city-services/family-services.page)，本人普通／8888均403后真网页主文 | 237行返回，本人重点实际135—168，137—144所申孩子须项目适用身份且只要求该孩子移民材料，其他家人不用交。没有采用Head Start、Promise NYC或大学概述作为当前全项目资格。 |
| [Harris County主管板说明](https://harriscountytx.granicus.com/boards/w/b97df4edf6fda4d2/boards/42972)，本人新真网页主文 | 286行返回，本人实际3—11；10核Gulf Coast Workforce Board／Workforce Solutions及Houston-Galveston13县服务区。仅用于原地区引注访问边界的抽查，没有采用董事、名额、任期或该页联系作为托育申请电话。 |

本人以上15个不同一级URL有实际采用段。TX CCS主页s10普通与8888均403、直接web403、从官方搜索结果真正重开仍403、无www公开URL亦不可达；搜索摘文不算主文阅读。[TX材料PDF](https://www.childcare.texas.gov/sites/default/files/CCS/Docs/ccs-eligibility-documentation-log.pdf)s13普通与8888均403、web错误，家庭表格原页本轮web403，未取得实际PDF页段或原件SHA。[Gulf Coast托育补助](https://www.wrksolutions.com/childcare-financial-assistance)本轮web错误，[该机构现计划页](https://wrksolutions.com/about-us/plans)本轮web400／timeout，均没有本人阅读。root记录的about-us原页失败仍属root，本人没有假定原页恢复或将作者150行成功继承。

TX美国国民、25／50小时、两周转托和所引材料细节在root事实记录34／35及25有具体实际采用段，第三审检查这些条件、对象和近引已准确留在正文；本人没有新读到它们的主页／材料PDF，不能登记为本人的新事实核验。地域抽查本人只读上述县主管说明，root已有县主管加同机构计划两个实际一级来源交叉核地域，作者about-us成功、root失败和本人计划页失败均保持各自归属。此次部分失败不构成新的事实差异或返修项，也没有消除任何人的失败记录。

## 内链、语言与手机表格检查

正文75个普通链接，69次外引、50个不同HTTPS URL，6次绝对站内引用／5个不同真实目标；没有相对内链、会话引用编号、占位或裸来源清单。引用均跟在对应动作、资格或具体期限处；两表和紧随的州／项目段落共同给出入口及继续路径，所需条件没有藏到地图。50个外URL的独立事实采用范围已由root记录，第三审没有再声称逐一联网验证全部URL。

本人重新打开五个当前站内源文件，实查metadata均integrated／draft false，并读下列实际承接段；下表正文摘要也由本人按同一算法实算。只是核链接当前内容，未冒称本轮重新核它们的全部外部来源。

| 真实绝对路径、当前正文摘要 | 本人实际读取与链接用途 |
| --- | --- |
| `/book/people/school/school-enrollment/`，`b8a01b4ae60bdc4441c9ace62002b07b90dc47e629dd06653dea6868b1f03cc0` | 对应114行文件，本人实际1—47；公立K–12、实际地址学区、材料与监护／替代证明承接本稿学校登记，范围没有移给托育补助。 |
| `/book/people/accessibility/accommodations/`，`1b028fd251ea4f4878076d3cae67fc7aec940ad7e44d7637c269c4362f24db0c` | 134行文件，实际1—48、110—134；私营服务TitleIII与宗教例外、具体请求、未落实／拒绝及DOJ投诉继续，接本稿特殊需要。 |
| `/book/rights/contracts/reading-contracts/`，`a456a8907378760c2b1736dc3b429457f602340975e1b36a869eb5c6f1031f08` | 145行文件，实际1—48、111—145；当事人、服务费用退出通知、留版本、提出请求、投诉和法院／法律帮助，接本稿签前与退费争议两处。 |
| `/book/rights/safety/emergency-help/`，`49a8d07854505ac39f6dc4463b7d8e36d06847089314403c8e507c5c469ee095` | 67行全部真正读；现场911、位置及发生事情、口译和通信困难，接本稿儿童直接危险。没有将988作为儿童现场救援。 |
| `/book/rights/legal/finding-help/`，`98b56bc44fa152f1a3674528a3ee27c87f6fe75d7785e3489918da4f3f9f639d` | 100行文件，实际1—57、88—100；准备文件／期限、服务地区和接案、核律师资格、窗口及未接案时继续，接合同或其他争议。 |

frontmatter独立YAML解析正确，title／description／page_id／content_kind／scope俱全，page_id `people.family.childcare`在正文树唯一；written／draft true、verified／reviewed_by空，weight20。没有正文一级标题，六个H2层级一致。32处Markdown加粗均逐处扫描内无首尾空白、外有空白；普通中文句法和政策限定保留，没有需要删掉的元叙述、训诫、反复免责或空泛对冲。正文没有虚构例子、可提交儿童文件或统一机构质量结论。

两张表均为2列、4个地区数据行，加表头／分隔共6行，无嵌套表格、单元格硬换行或多余管道。去除链接URL后的最长整行206字符；长格集中在四州入口和申请路线，链接显示为普通有意义文字，不会显示原始长URL。源码没有固定位宽或把时间／金额塞入多列，静态可用；实际手机横向滚动、字号、表头和行裁切、打印跨页尚未由本人看过，不写视觉PASS。主控在候选构建后应实际看两张新表和各州申诉／换托段，属于后续正常工程门禁。

## 最终结论及未核边界

静态／编辑 **PASS**，绑定本记录顶部的完整正文与整文件摘要；无必要作者修订，没有修改任何正文、metadata、作者包、事实记录或共享文件，没有构建、提交、真实查询／申请、联系机构或探测Claude。正文若有任何字节变动，须由原作者处理，先重新事实绑定再重做本第三版本核查；本PASS不追认未来版本。

本审没有核真实家庭收入资产／身份与监护个案、当期实际发券、机构当前质量／名额、后台收件、全部原始材料表、CA每个子项目移民资格、Head Start／Promise NYC完整当期资格、所有县资金优先、完整照护人数比、保姆雇佣税、临床与全部听证司法程序。WA2025州资金说明保留旧资料性质；本人TX主文／材料PDF及Gulf Coast现计划未取得的阅读边界留在本记录，不填成成功。可交主控继续候选与实际工程验收，尚未正式集成。
