# B12 医疗意愿和代理授权：独立事实审

2026-10-13，独立事实审阅者root；原作者static_editor，第三人静态审拟由banking_fact承担，须root接受本记录后正式分派。本记录仅审`content/book/people/aging/advance-planning.md`及对应作者包，不是第三人审、构建、实际渲染或集成结果。

结论：**PASS，限下面实际稿件采用的成人、四州和HIPAA办理范围。** 先独立逐项核查原冻结，再将唯一必要补正退回原作者；收到新稿后完整重读、独立实算新摘要及唯一逆向恢复，结论只绑定补正后的当前版本。没有给作者自审或补正前稿追认PASS。

## 对准的实际文件

| 文件 | 本人真正阅读与独立实算的SHA-256 |
|---|---|
| `content/book/people/aging/advance-planning.md` | 全125行，先原稿1—44／45—87／88—125，原作者补正后再完整读相同三个区间。当前正文`48c70ff0af9f63f4b21e9c2f9c85ea5a7c6ff2607d475f5ecd4cdf61312f2be0`；整文件`3b3ccb2768533fa23ae82be8a7688e2a4ceca46e187227dd2c194bdc74680f52`。正文用UTF-8 `split('---',2)[2]`，保留首换行；整文件用原字节。 |
| `ops/maps/advance-planning.md` | 补正前全30行、当前全36行；当前摘要`a18a154fabfdd60771e643efd47f194cf413b43d8f4be10d80d87d59c597ae31`。 |
| `ops/evidence/advance-planning.md` | 补正前68行分段完整读取，先前被截尾段后来补齐；当前1—44／45—83全83行真实读完。当前摘要`ccc3b705b5ebda697b416c5e2196a20019d45e74608f90a6a675ac1965d0f8f3`。作者记录只帮助定位，不继承其原件阅读结论。 |

## 本人的独立回源与实际阅读

本人新建`.cache/evidence/b12-planning-root-fact/`，实际先核108个具体源缓存／索引／脚本路径的忽略，再正常TLS新请求；工具脚本使用独立requests session，不读取作者缓存、登录、关闭TLS或绕过挑战。首轮31个正文URL中24个普通直连或正常8888取得真正材料，7个普通请求失败后由本人web工具打开真原页并有界读取；另外四条CA财务法条均失败。索引标retrieved-only，不凭200计已读；长输出截断的CA财务表45—94、TX166的1073—1078、NY1513后段及其他采用区间后来单独补齐才计以下范围。

以下31行对应原稿全部31个不同正文URL，末尾新增确认页对应当前第32个。行号属于本人这次提取或web返回，不借作者行号；PDF已实际读完整提取内容及对应全部物理页文本，不声明已填表、核互动字段或逐页视觉审。

| 一级来源／本人缓存 | 真正读到、版本及采用范围 |
|---|---|
| [NY advance-care FAQ](https://healthweb-back.health.ny.gov/community/advance_care_planning/faq.htm)，p01 | 201行全读；采用67—135的医疗文件分别作用、18岁、见证、无统一living-will表、clear-and-convincing意愿和保存。RevisedJanuary2020；未把旧出版时间改称2026新规则。 |
| [TX Health and Safety166](https://tcss.legis.texas.gov/resources/HS/htm/HS.166.htm)，p02 | 实读1—140、157—220、290—301、469—477、925—1134。见证资格、directive完整采用段、医疗POA及披露、两见证或公证、代签、生效医生书面证明／入病历、本人异议、特定事项排除、撤销、怀孕限制均在这些实读段；1074—1077曾截断，后1073—1078实际补齐。未称读完1353行全章。 |
| [NY1430 Health Care Proxy](https://healthweb-back.health.ny.gov/publications/1430.pdf)，p03 | 真PDF全8物理页／332提取行，1—166／167—332完整读。表尾8/22；本人／代理通常18岁、两成年见证、代理和替补不得见证、不需公证、医生认定才启用、人工营养水分、撤销和保存。raw325983字节，SHA`33555be572b3f4273ee82d6372593a19dce050f60f507f9491489ea58d1d7bad`。 |
| [NY financial statutory form§5-1513](https://www.nysenate.gov/legislation/laws/GOB/5-1513)，p04失败后真web | 普通两路403，另实际web读44—165和166—287的完整法定正文，含签署、代理接受、旧POA不自动撤销、权限initial、特殊赠与及代理职责；不称普通请求成功。页列current revision2021-06-18。 |
| [HHS consent／authorization](https://www.hhs.gov/hipaa/for-professionals/faq/what-is-the-difference-between-consent-and-authorization/index.html)，p05失败后真web | 普通两路403，真web全100行；采用84—92的指定信息、披露方、接收人、到期与用途。Last reviewed2022-12-28；不扩成医疗决定授权。 |
| [HHS personal representatives](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/personal-representatives/index.html)，p06失败后真web | 普通两路403，真web全117行；采用58、62—76的适用法律、成人医疗权限与病历范围，以及98—100虐待／危险例外。Last reviewed2024-01-05；未采用未成年人全规则。 |
| [WSMA WA POLST程序](https://wsma.org/resources/advance-care-planning-and-serious-illness/polst/)，p07 | 151行以88—151／1—87真正全读；副本／图像／传真、翻译仅教育、临床和本人／合法代表签署、随人转移及搬州复核。网页某些旧字段说明不压过当前正式表p26，不照抄为全部治疗栏位。 |
| [NY MOLST程序](https://healthweb-back.health.ny.gov/professionals/patients/patient_rights/molst/)，p08 | 实读59—140、145—163；严重病情适用、翻译仅教育、MD／NP／PA签署和复核，页面真实列RevisedOctober2026。未另实际下载DOH5003表，不称其所有字段已核。 |
| [WA11.125.100](https://app.leg.wa.gov/RCW/default.aspx?cite=11.125.100)，p09 | 全41行；本人／代理终止、配偶或州注册伴侣关系解除／分居等申请提出时点、第三方实际知情和新POA不自动撤旧。末列2016法。 |
| [CA Courts准备法律文件](https://selfhelp.courts.ca.gov/wills-estates-probate/legal-documents)，p10 | 主提取全48行；识别其财务／医疗accordion遗漏后，本人从自己新取原HTML实际单独读取这两块完整文本，财务权限／期间／立即或失能与律师复核、医疗副本交接。不把页面most-forms概括用于财务统一见证规则。 |
| [CA AG预先照护安排](https://oag.ca.gov/consumers/general/care/)，p11 | 实读1—84；采用讨论治疗目标、选代理及替补、副本和紧急可取得的安排。不采用旧比例统计或后半hospice支付。 |
| [NY选择医疗代理／多语材料](https://healthweb-back.health.ny.gov/professionals/patients/health_care_proxy/)，p12 | 实读57—116，March2023；讨论、代理及中文入口、医生和代理副本。只核材料入口存在，未冒称逐语言中文PDF全读。 |
| [CA AG正式医疗directive](https://oag.ca.gov/system/files/media/ProbateCodeAdvanceHealthCareDirectiveForm-fillable.pdf)，p13 | 真PDF全7物理页／370行，以1—125／126—255／256—370全读；代理资格／限制／默认与立即生效、两个合格见证或公证、至少一个无相应亲属／遗产利益者、SNF另外指定advocate／ombudsman、副本效力和公证声明。表记2018修法、2019-01-01生效，非2026新表。raw775507字节，SHA`27b318dd63fb1ec3eca2f4dc762adac63908735c7debcd8707c50d637be4a94f`。 |
| [WA DSHS当前本人／家庭材料](https://dshs.wa.gov/adult-and-aging-services/supportive-services/dementia-and-alzheimers-resources/resources-individuals-and-families)，p14 | 全43行；28—40实际医疗／财务POA、多语包括中文、NJP及协助入口；不承诺服务一定接案。 |
| [WA11.125.050](https://app.leg.wa.gov/RCW/default.aspx?cite=11.125.050)，p15 | 全34行；签和日期、公证或两合格见证、双方亲属／注册伴侣及照护人员排除、不能签或mark的分支。末列2026c101s2。车辆转移特定例外未采用。 |
| [DSHS所链NJP医疗／财务包](https://assets.washingtonlawhelp.org/en/print/pdf/node/191)，p16 | 真PDF全10物理页／380行，1—125／126—250／251—380全读；FAQlast review2026-05-28，医疗501及联系页Revised09/2024、财务500 Revised05/2026。医疗立即生效仍保留本人决定权；财务可选立即或失能、逐项特殊权限、模板只列公证。其提到SSA的模板字样不能代替SSA任命p24。raw393177字节，SHA`90ea0025f0c45053a1f4dcec399d8b1038bf51875e9d3a08f9b1492f255433e7`。 |
| [WA70.122.030](https://app.leg.wa.gov/RCW/default.aspx?cite=70.122.030)，p17 | 全47行；Health Care Directive与医疗POA分开、公证或两 qualified witnesses及相应排除、terminal／permanent unconscious法定条件。末列2025c56s1；不扩成任何普通诊疗的统一表。 |
| [WA11.125.040](https://app.leg.wa.gov/RCW/default.aspx?cite=11.125.040)，p18 | 全25行；durable须相应文字，持续效力与起始时点分开。 |
| [WA11.125.090](https://app.leg.wa.gov/RCW/default.aspx?cite=11.125.090)，p19 | 全36行；默认执行即生效或本人约定事件、相应书面能力证明。没有套给所有四州医疗代理。 |
| [Sacramento公共法库财务模板说明](https://saclaw.org/resource_library/power-of-attorney-california-uniform-statutory/)，p20 | 全17行；确实发布Prob4401模板及修改风险。发布者是公共法库，不称为州立法机关或所有现行执行法条。 |
| [SacLaw财务模板](https://saclaw.org/wp-content/uploads/2023/04/form-uniform-form-power-of-attorney.pdf)，p21 | 真PDF全2物理页／94行真实读完，45—94截断处后重新补全；权限initial、立即及durable、共同代理、第三方撤销和签字。该两页没有certificate of acknowledgment，触发下节必要补正。PDF未标当前修订日期，metadata修改2024-11-26不能改称规则有效日。raw404000字节，SHA`265f053228f70f931206aad3c934d3dfa6eb145e6e0fb69a7d156d09c730a5a3`。 |
| [NY§5-1501B](https://www.nysenate.gov/legislation/laws/GOB/5-1501B)，p22失败后真web | 普通两路403，真web全128行；revision2023-10-27，本人理解／签或initial／日期、公证ack加两非agent／gift-recipient见证，公证人可兼一见证，代理另签公证接受、共同代理／附条件生效。 |
| [TX Estates752](https://tcss.legis.texas.gov/resources/ES/htm/ES.752.htm)，p23 | 实读1—185，包含§752.004、.051完整采用表及.052；本人签和acknowledgment、home-equity-loan特定办公室签署、权限initial、立即或失能及证明、代理职责和特定赠与权限。不称512行全章已读。 |
| [SSA本人／福利代领FAQ](https://www.ssa.gov/payee/faqbene.htm)，p24失败后真web | 直连DNS失败／8888 403，真web实际读91—105；101明确POA／joint account不等于SSA representative payee，须另申请及任命。185行其余FAQ未完整读、不扩成所有SSA个案规则。 |
| [WA11.125.060](https://app.leg.wa.gov/RCW/default.aspx?cite=11.125.060)，p25 | 全34行；执行时点与外州法律适用、副本效力及其他法律例外。 |
| [WA POLST当前正式表](https://wsma.org/wp-content/uploads/polst-2021-form-fnl.pdf)，p26 | 真PDF全2物理页／141行全读，REV04/2021；DNR仍可其他治疗、规定的临床及本人／合法决策人签署、电子／传真／副本、不是指定代理文件、改变时新表及VOID旧表。raw114590字节，SHA`17a9297b2a0de273772d8eb9f43e4cda4b64d5bfd0ecead57b943a750abe4650`。 |
| [TX DSHS OOH-DNR程序](https://www.dshs.texas.gov/dshs-ems-trauma-systems/out-hospital-do-not-resuscitate-program)，p27 | 实读130—188、199—212；适用院外复苏措施、完整表／背面要求及部门继续入口。189—198供应商部分输出截断且未采用，不能称全212行主文已读。 |
| [TX当前OOH-DNR正式表](https://www.dshs.texas.gov/sites/default/files/CP-EMSTraumaSystems/dnr/docs/dnr_form.pdf)，p28 | 真PDF全2物理页／162行全读，RevisedOctober12,2023；成人本人／合法代表各执行分支、临床签署与counter-sign、copy随转运、其他适当紧急／舒适照护继续、撤销和怀孕／可疑死亡特殊条件。未成年人分支虽读不采用为本稿完整指南。raw1284950字节，SHA`395c1d18abeb174259d21462fae2a0c2f085d3b4fa976082d958b62b40bb5a1c`。 |
| [HHS撤销信息授权](https://www.hhs.gov/hipaa/for-professionals/faq/can-an-individual-revoke-his-or-her-authorization/index.html)，p29失败后真web | 普通两路403，真web全102行；84—94书面并由covered entity收到、已依法依赖的披露不能收回。Last reviewed2022-12-28。 |
| [NY患者及家属指南](https://healthweb-back.health.ny.gov/publications/1503/index.htm)，p30 | 实读58—205，先90—205、后58—89补齐；成人能力、proxy、医院／护理院／hospice的surrogate、营养水分、伦理及机构政策冲突／转接。出版物December2017、网页January2020；未采用全部未成年人／特殊发展障碍分支，亦未读206—255。 |
| [HHS OCR健康信息投诉](https://www.hhs.gov/hipaa/filing-a-complaint/index.html)，p31失败后真web | 普通两路403，真web全48行；11—35的HIPAA／Part2投诉分流。Last reviewed2026-02-13；不是银行／临床决定／法院的统一救济。 |
| [CA州务卿正式签字确认页](https://notary.cdn.sos.ca.gov/forms/notary-ack.pdf)，本人从真SOS页点击 | 真PDF全1物理页／web21行完整实际读；州／县、到场、身份和签字确认、官员签／seal及只确认身份的声明。未标修订日期，不称2026新表；本人的web阅读没有本地raw摘要，不借作者下载摘要冒充。 |

本人还真实读了两项补充原件：[CA州务卿Acknowledgments说明](https://www.sos.ca.gov/notary/acknowledgments)全44行（Civil1189、顶部声明框及确实链到上述唯一PDF），以及[SacLaw财务POA一般介绍](https://saclaw.org/resource_library/power-of-attorney/)全113行（发布者材料定位与模板性质；其banks／CalPERS／IRS概括不采用为全部机构都可强制自用表的规则）。故当前32个不同正文URL均有本人独立真实采用阅读，另两URL为补充材料；不是34个全部官方法条或全部网页全文核验。

## 必要返修、重新绑定与实际断言结论

CA财务行原本选择公证办理，但所用两页模板缺确认页，读者可能只带两页而漏完成公证证明。本人把唯一必要改动明确退给原作者static_editor，其本人独立取读SOS说明及一页PDF后，仅在实际L66原“采用公证确认本人签字的路径”后加“，请公证人按[州务卿的签字确认页](https://notary.cdn.sos.ca.gov/forms/notary-ack.pdf)完成所需证明”，仍要求律师核权限／签署安排并保留医疗见证不得照搬。本人再全读当前125行、两作者包并独立确认唯一删回此短句精确恢复原正文`38d531b9e982d05782c585056026c289b06b875ce9060788de99f31702876afc`、原整文件`73f70d83281df20b4ed1a223f618120eaeb36475158f0d341ee163068ce36884`；frontmatter字节不变，原75个外链序列完全不变，仅新增PDF一次。此处必须由原作者修改，root没有代写正文。

实际稿件保持医疗意愿、医疗决定、财务权限、HIPAA信息和临床POLST／MOLST各自用途，durable与何时启动、本人能力与不能握笔、亲属协助与合法代理分别放在会改变行动处。NY人工营养水分、CA SNF特别见证、NY财务公证加两见证和代理接受、WA2026财务表公证路径与法定见证分支、TX完整POA披露／home-equity-loan地点、SSA另任payee、TX本人异议及怀孕限制、NY／WA新POA不自动撤旧、WA关系解除申请时点均由本人的上述采用原文支持。

当前CA财务只给“公共法库所发模板→律师核权限及签署→按SOS完成公证确认”的明确路径，不声称已核Prob4402全部有效性，不写所有POA可任选医疗见证规则。真实CA Courts财务accordion、所用模板和SOS材料支持该路径；其余复杂授予、效力争议仍交合格律师。交付要求完整版本、可找原件和副本、确认接收与缺件，受阻区分医疗团队／患者代表／伦理、银行POA人员／法援与HHS信息投诉；这些继续路径未编造后台字段、费用或全国统一期限。

## 未成功及不覆盖的边界

本人p32—35的现行CA Probate4401／4402／4121／4122原页正常直连和8888均403；本人web4402不可达、4121及2025—2026 AB2199原bill403，搜索中未来变更线索未当实际法源采用。旧CLRC／CalPERS专项材料及secondary摘要未拿来替一般当前规则。CA完整POLST、全部监护诉讼、遗嘱／trust／probate与身后手续不在本文结论内。后续CA法改、模板和主管指引变更须重核，不从本次访问失败推断法律没有变化。

TX166未读141—156／221—289／302—468／478—924／1135—1353，TX752未读186—512；NY指南／MOLST及SSA只认表中实际区间。全部译表正文、个案能力认定／临床选择、真实见证或公证人资格、互动PDF、签署／机构后台、境外效力均未核。七个普通失败后真web读取和四CA法条失败均保留，不能被PASS抹去。

当前仍是written／draft true／verified和reviewed_by空。第三人须另检查实际版本、语言／元数据／结构／内链和必要返修落实；root候选安装、隔离make check、实际网页／打印渲染与本地同步尚未发生。本文事实PASS不替代这些后续步骤。
