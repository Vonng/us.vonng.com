# 家庭学校／照护／死亡三链：新canonical版本收口

- 日期2026-10-14（Asia/Shanghai），birth_fact；结论 **READONLY SCENARIO REBIND COMPLETE** 。学校、照护、死亡三条普通家庭链已绑定下表当前26依赖，没有新的核心行动缺口或必要修改请求。只写本新记录。旧 `ops/reviews/b-all-family-scenarios.md` 182行／34445 bytes／SHA `fd73097105e68f124561de42d14e11b08f11c64ff2d4c76226ba7593b09beb7c` 冻结，本人本轮完整1—91／92—182读回，未改旧记录。
- 此次是原家庭三链的已安装canonical版本核对，不是重新独立核全26件全部事实。保留旧21件全文与5件只核目标／frontmatter的真实范围，以及原8个一级采用URL和访问失败边界；本轮另核实际新旧diff、受影响段和限定上下文、26件当前body／whole。
- 实际修订前基线 `.cache/reports/b-all-pre-revision-baseline.json` 1423行／64062 bytes／SHA `db943d71cb4d7607c1b25e4eb4db758c8e10d12f427032ded9e5d69239eb65d5`；安装报告 `.cache/reports/b-all-candidate-install.json` 609行／32961 bytes／SHA `4f8640de015b141f49b1e8ed88dec1a2b7a163a734ab8fa977ab9b4716972984`。本人实际解析报告头部及26依赖对应项，不称全文逐行阅读两个大型JSON。
- 本人从旧记录最终两表定位26路径，逐项与真实基线相符：当前17件改变、9件逐字不变。17件包括P06、P07两个公共入口与15主题；当前body／whole均与实际安装报告对应项相符，其余9件仍等于旧基线。首次schema定位误把公共manifest的files字典用数字0索引，KeyError发生在26核验前；随后按实际字典修正，26完整核验才真正通过。

## 实际新读取的起始断点（历史）

已完整读17份original→canonical实际unified diff（各含5行上下文）和P06 `content/docs/routes/_index.md` 当前全文1—51、P07 `content/docs/routes/caregiving.md` 当前全文1—36。这些diff包括root安装的实际元数据变化，不把拟稿whole等同安装后whole；正文body按UTF-8全文 `split('---', 2)[2]` 并保留前导换行。

P06 L34将“工作资格”明确为“相应项目资格”；P07 L28明确“相应休假或收入支持资格”。两处仍链接原职场正文，请假、州付款、家人照护服务各有自己的请求／决定／开始记录；不是要求先统一证明移民工作授权才可以向所有项目提请求。下一步实际复读职场对应适用分支和三链核心限定／交接／受阻段，再核内部承接及完整当前摘要。

原21件全文经历仍只属于旧记录的阅读版本；本轮当前26件没有统一重新全文阅读。旧5个延伸目标中4件有语言修订，本人已实际读它们的真实diff和受影响上下文，不把原只核frontmatter提升成当时已读全文。本轮尚未发外部一级源新请求，原8源只保留本人此前实读，不借其他参与者成功或主控新工程结果。

主控已通知新构建可以GET；若随后执行，将分别记录本人的实际HTTP／DOM范围，不能当目视或全工程通过。本断点尚无本人新GET、截图或渲染。

## 最终实际读取及独立版本检查

上述17个完整diff已全部实际读完，不将JSON或hash当全文阅读。除每个diff的实际受影响上下文外，本人另实际读以下当前canonical范围，确认前提、文件、收件、实施及受阻继续仍在；两入口完整实读，六主题是限定段实读，不把范围扩成全26新全文。

| 当前真实路径 | 本轮另实际读取范围 |
|---|---|
| `content/docs/routes/_index.md` | 完整1—51，家庭定位仍29／37／40，P06在34 |
| `content/docs/routes/caregiving.md` | 完整1—36，P07在28，32—36仍接实际开始／替班／受阻／丧亲 |
| `content/book/people/school/school-enrollment.md` | 14—47、63—114；48—62也在实际diff上下文读到 |
| `content/book/people/school/school-support.md` | 34—68、72—99、103—133；21—31的虚构请求在实际diff中读到 |
| `content/book/people/aging/caregiving-plan.md` | 18—26、30—47、51—66、70—106、110—119、125—148 |
| `content/book/people/aging/advance-planning.md` | 20—29、58—69、75—88、115—125 |
| `content/book/work/employment/workplace-rights.md` | 22—29、39—49、62—86、133—135；该件全文字节与旧版相同 |
| `content/book/people/aging/death-arrangements.md` | 14—36、40—48、52—67、79—110、114—125 |

其余十个改变主题是service-conversations、finding-help、coverage-changes、insurance-costs、appointment-network、mental-health、accommodations、medical-bills、pay-stub-overtime、job-loss-support；它们与前表五个改变的核心主题合计15，workplace属于9个未改依赖之一，完整路径以末表为准。本人实际读各diff及其5行上下文，未把旧5个延伸目标全部重新阅读全文。当前9件未改版本仍精确等于旧已读／限定目标；它们的旧阅读范围保持。

本人独立从17个真实original缓存及9个未变canonical复算26旧body／whole，全部吻合旧182行记录及真实基线；又从当前26件真实字节计算26新body／whole，共104个旧新摘要。15改变主题正文与对应最终proposed body逐字相同，两个公共页也同最终proposed body；当前installed whole逐项与安装报告相符。按17件实际替换顺序正向重建拟稿、按准确位置逆序撤回，全部精确恢复old／new：其中正文主题37处、公共入口2处，共39处。这仅是本三链26依赖内的差分统计，不称覆盖全部43件76处。

正文数字序列、普通链接文字／URL及次序、标题、行数均不变；frontmatter另实际解析，root安装的语义变化限verified／reviewed_by，其余键值不变。此处记录的是差分核验日期和参与者更新，不能从日期更新推出所有旧一级源已于本轮重新阅读；原scope、资料年份及原FACT边界保留。本人的本轮没有元数据写入。16件三事项／核心与帮助正文仍有73次绝对内链、19个不同目标，实际文件及frontmatter全部可定位且integrated／draft false。

## 三链在当前版本的行动收口

沿旧记录三个明确标为教学虚构的普通家庭情境重绑；不会把例信当真实递交，不代办个人家庭事项。下列段号均实际当前canonical，不是旧行号自动沿用。

### 学校：普通入学、在校语言／残障与安全

事项总入口L29→school事项→enrollment／support的承接不变。enrollment L14—47、67—80把完整住址、年龄、照顾关系、免疫／原课程与计划交正确学区，非公民／无SSN或常规材料不齐均有人工替代；L88—94的即时入学与后续补健康资料、寄养另联络仍在。53／57／94的学校辅导员、校护士及寄养联络员中文释义明确找谁。L98—114继续保存收件、缺件与拒绝理由，最终确认学校、年级、第一天、接送及缺件负责人。

support L34—49仍分孩子语言服务和家长口译；L53—68仍分请求收件、家长知情同意、州计日与例外，不能把教学虚构例信当已开始评估时钟。L72—99核计划副本、实际服务、语言与转学衔接；L103—133保留临时安全安排、调查编号、书面决定、SPS一年HIB两类受妨碍例外及首上诉、IDEA／504／民权不同正式程序。未给全家统一资格、无材料一概免办或全国统一校车承诺。

具名地方仍是 **CA／San Francisco SFUSD Enrollment Center及本校协调员；NY／NYC片区学校或Family Welcome Center、CSE／IEP团队；WA／Seattle SPS Admissions／liaison／HIB及OSPI；TX／Austin ISD登记、LPAC／504及TEA** 。各自材料、请求和人工渠道就在enrollment67—70及support40—49、61—66、86—89、107—110、122—125；四州地区页当前字节不变。完成确认仍是能去上课、有实施负责人和当前安全安排，有迟办／拒绝或缺服务时继续找实际收件者与正式投诉渠道，没有新增核心断点。

### 照护：本人选择、服务、付款与照顾者离岗

事项总入口L37→caregiving事项；P06的L34和P07的L28现直接写项目资格。本人另实际读workplace22—29、39—49、62—86及133—135：雇主覆盖、工时／服务期、家庭关系、认证与收件、休假保护及州现金有不同条件；CA／NY的相应付款分支还明示公民／移民身份不是该项目资格因素。不能把一般移民工作授权当全部休假／付款请求的统一前提。请假获准、款项请求与家人服务开始仍各留确认；WA周请求的雇主补充PTO例外仍在。

caregiving18—26、30—47仍分联系人、披露授权、个人代表，交出院药单、书面操作、器材与转介，明确夜间和替班任务。47的IM／NOMNC／BFCC-QIO中文用于Medicare承保服务结束，不把全体参保资格写成终止；医院当天与其他服务前一日中午及自付责任仍分情形。51—66的医护条件与长期非医疗支付分开，70—106按州、年龄／残障、身份、功能与财务核申请、案号、补件及评估。advance68按采用表的公证栏，法定合格见证路线同句仍在；20—29／75—88／115—125的权限、生效、完整版本交付与拒收继续未变。

具名地方仍是 **CA／Los Angeles County DPSS IHSS及县Medi-Cal；NY／Brooklyn HRA或本人计划、NYIA及NY Connects；WA／Seattle／King County HCS人工申请及ADS／CLC；TX／Harris County HHSC／STAR+PLUS协调员和ADRC** 。NY新门槛／Legacy、WA TSOA暂停与州资助人数／预先授权、TX名单／upgrade／转社区及完整Medicaid分支保持。Seattle HCS具体办公地址原未核到，继续用已读intake及地方社区支持；不把CSO／DVR目录冒作HCS地址。偏远服务区、交通、语言、付不起临时服务、批准后无人接案的继续在134／140—142；146—148核实际到场、任务和接班记录。

115、116、117、129的四个ASCII留白在当前canonical真实存在，body为接受的care v2 `9a5cf557ecbd0ac87bcb7df0831bdac58c0cb324fbef20f5b48c27f769bd3609`。只逆撤四空格可精确恢复v1拟稿body `a7667b144d1aec0e555d291269b48f6b4f17879fd92b6caf65ff73b8444c02c7`；号码、州对象与主管不更新成新事实。136长期照护申诉专员仍只助相应住民，安全／虐待另走许可保护机关。没有新的核心断点。

### 死亡：交接、证明、分别申领与继续生活

事项总入口L40→bereavement事项→death；生前授权与身后代表经advance及finding-help继续。death14—36仍先核医护确认、911／已有hospice计划与法医放行，分别确认处置人、合同购买人、支付及遗产权限；40—48取得GPL／项目总价、授权与负担不起时的具体协助。52—67按死亡发生地、用途／关系、ID与正式渠道订证明、留收件和退件原因；不统一套州ID或家庭住址，不等证明调查结束才回应其他通知。

具名地方仍是 **CA／Los Angeles ME、Registrar-Recorder／County Clerk及Superior Probate；NY／Brooklyn的OCME／NYC Health与Kings Surrogate；WA／King County ME／Vital Statistics及Superior Probate；TX／Harris IFS仅其经办案件、Houston城市正式边界的Health或相应登记方及Harris承办Probate庭** 。证明机关按死亡地，遗产法院按其相应程序；NYC pending换件从原证明发出算，IFS不发证明和城市／县边界限定都在59—67。119新增的墓地管理部门中文仍与NY殡葬卫生主管分开，不扩大权限。

79—93仍先核SSA报告、再分别申领月度／255一次性款、保单索赔及家庭保障；缺件先联系，不把报告等同申请，非公民在美／境外及一次性付款另核。97—110核遗产代表、债务责任例外、家属仍用服务及最后款项；114—125按真实收件者处理拒绝／迟办／争议及语言、邮寄、交通和哀伤支持。完成确认保留机关、交接／授权和价格、证明或缺件负责人、每笔正式申请与案号、决定期限及账户结果。复杂继承、跨境许可、全部遗属资格及临床处理仍属明确专家分流，无新的普通链断点。

## 本人原8一级采用范围与原失败（本次未新增外部请求）

以下全部是本人旧家庭批在2026-10-14真实请求与读取，原记录99—114的范围原样保留；不是本次新请求，也不是从作者或其他事实审继承成功。原PDF未新开，学校／死亡全37／49源未重核，私人门户、个人资格、后台字段、到件、收费、名额及真实交通／付款结果没有结论。本轮差分和限定上下文未产生需新增一级回源解决的事实疑点。

| 本人原实际一级URL | 保留的原采用段／真实失败边界 |
|---|---|
| [CDSS IHSS](https://www.cdss.ca.gov/in-home-supportive-services) | 原web34—93，县申请、评估／决定、提供者与中文／语言；SOC873／874及全部法源本轮未开。 |
| [CDSS County IHSS Offices](https://www.cdss.ca.gov/inforesources/county-ihss-offices) | 原web27—67、143—147含Los Angeles；原点击Internal Error，直接目录成功，两次状态分开。 |
| [LA DPSS Seniors and Persons with Disabilities](https://dpss.lacounty.gov/en/senior-and-disabled.html) | 原web14—25、38—40；原普通TLS自取54行全读，采用17—25、32—37；不采同页GR资格。 |
| [NY DOH How to Apply](https://healthweb-back.health.ny.gov/health_care/medicaid/how_do_i_apply.htm) | 原web74—122、376—398、429—454及473版本May2026；保留LTSS／HRA／急需和人工继续，不采旧年金额或全套身份／资产门槛。 |
| [DSHS Medicaid eligibility／application](https://dshs.wa.gov/medicaid-eligibility-and-how-apply) | 原web1—124，申请、财务／任务评估、人工／纸件／语言及TSOA／CLC；无私人账号读取。 |
| [DSHS Who Can Help](https://www.dshs.wa.gov/who-can-help) | 原web1—116，HCS／CLC／AAA／照顾者支持、交通／喘息；未把咨询当批准。 |
| [Seattle & King County ADS／CLC](https://www.agingkingcounty.org/help-information/community-living-connections/) | 原web5—31主文，Seattle／King服务范围及社区导航；未核个案费用、名额或可派交通。 |
| [Texas HHS ADRC目录](https://resources.hhs.texas.gov/directories/adrc) | 原web后续展开Internal Error／timeout；本人原正常TLS取得202行全读，采用92—98 Harris及179—187不同服务县；不假称原web展开成功。 |

原DSHS通用office-locations虽原普通8888可取，但1381行只作定位、未完整读且未核Seattle HCS；`manuals.dshs.wa.gov/location/dshs-hcs-seattle`原真实403和搜索不采用均保留。原ADRC、LA及通用目录的原件／文本SHA仍仅旧记录110—112承载，本轮未重下载／改写或冒称新原件。

## 本人新构建后的9次HTTP／DOM检查

主控明确通知新构建可GET后，本人正常请求 `http://127.0.0.1:24146` 下九个不同路径，均200、无本轮GET失败。BeautifulSoup实际解析article，核P06／P07及五核心主题的新版文字；四个照护电话号码的真实strong前文本以逗号＋ASCII空格结尾。school事项五个片段在新版enrollment HTML中逐项unquote后确有id。请求均在内存处理，没有新下载文件或截图；HTTP／DOM核对不算目视、点击、手机布局、打印或全工程通过。

| 实际GET路径 | HTTP／响应bytes | 实际响应HTML SHA-256 |
|---|---|---|
| `/docs/routes/school/` | 200／60778 | `b80773d2e54ca89074973e3523a86c9960d0c85881023218fe069cfa610a10e0` |
| `/docs/routes/` | 200／70572 | `d705c034a5577ee80e38f8e4a2cadd26c1dd72d60760397507eab8eb0399e755` |
| `/docs/routes/caregiving/` | 200／61196 | `49d6ac9fa2d4e140c582a0e4c3a8629552228383496bb8bdb040ccbf22b6a910` |
| `/docs/routes/bereavement/` | 200／60947 | `1f8ba4ffeb1da57a81a75e4e9e9591247c7ae0c508d0d47e6c242962a4a88e05` |
| `/book/people/school/school-enrollment/` | 200／118922 | `46c1463a5a750d41ac0dd86a6448c60e25ec9b7851778cc9bf9997ba282d0e8c` |
| `/book/people/school/school-support/` | 200／129956 | `70c70ffa49bd81d8c2ff45cb6cd93f1af3050453730888833c8b2d3c82d6570d` |
| `/book/people/aging/caregiving-plan/` | 200／125325 | `7b7451cd50bb29a68b934c62dd15a825280313e1101784a05fbe8c65fbcbac52` |
| `/book/people/aging/advance-planning/` | 200／128137 | `74c8672decbd95bfea653c5915bee501b570c1e73093f54de759ff3101282d44` |
| `/book/people/aging/death-arrangements/` | 200／127765 | `bc4be5e2d6a218db5119f08d5c34aecfdc2da87ea3ccb3e1e75d968da366aaf2` |

学校真实五锚点是`先查学区再查具体学校`、`带哪些材料缺一项时怎么办`、`住房不稳定直接找-mckinneyvento-liaison`、`被拒一直等不到安排怎样推进`、`收到学校安排后还要确认什么`。新版正文所需段和静态承接存在；本人的结论没有采用主控全138两端／76手机段／打印的进行中或最终结果。

## 26件旧／新实际字节绑定

以下26件全部实际旧值与基线相符，当前值独算；旧前21件的全文阅读、后5件的仅目标／FM范围不改。本轮新增范围以上表／17diff为准。26源合计行数与旧版相同；新358653 bytes、旧358080 bytes是hash统计，不是新全文阅读统计。body保留前导换行；whole为完整源字节。当前两个公共页无元数据变化；15主题实际安装的元数据差异限前述两字段，故whole不能沿用proposed whole。

| #／实际路径／旧阅读范围 | 行／旧→新bytes | old body SHA-256 | old whole SHA-256 | current body SHA-256 | current whole SHA-256 |
|---|---|---|---|---|---|
| 01 `content/docs/routes/_index.md`；原全文 | 51／5733→5739 | `6fffc57d86d0be4cc426dcb6a708d932965034e748382303fed7d09f7d544d91` | `6ebfaba6090a162c412d3e4fc0a662a55be11d6fe1d34537cb685d142a9a4b08` | `17dcf23a991587046903c91b5a5823807bbe32dccc76e1d4da142f0fe9e43c98` | `84eb7144a7ccde4431dac88d03eff0717edf983ee89a4094a87bbd802b4d4e14` |
| 02 `content/docs/routes/school.md`；原全文 | 27／2710→2710 | `78d89dd081cf38b1c2574a211d00df233a111eae0f661fa6940492193b7ed007` | `4dc8aaf4cea3f05b9bf1df80574c6f721ef3e725cbb09ee2e1770afc51c6cfbc` | `78d89dd081cf38b1c2574a211d00df233a111eae0f661fa6940492193b7ed007` | `4dc8aaf4cea3f05b9bf1df80574c6f721ef3e725cbb09ee2e1770afc51c6cfbc` |
| 03 `content/docs/routes/caregiving.md`；原全文 | 36／3147→3168 | `41f62afcb8520649bd438b802d9b0da97f91ce312e71e59946c7c2cd3037998c` | `33cef9f9c26438a18cc719d8ddb7a106ce8942a1ac93c01068a1599f21e74c98` | `365a82ad91c0d15642c33d9f2a41b83e0214f9a19763a89875bf2bce88cbff26` | `33185ceff6a8898fa661c739c273e152efa8d8581ab87d892f6542828ba34420` |
| 04 `content/docs/routes/bereavement.md`；原全文 | 28／2142→2142 | `1d1bcae9278fafe373d9d025e2dd030af10046cec93382a23605b96a29c428cc` | `8e0dd4a53e1a0a3778091fc608df296d6453736508c4e109f7855789dd45eaa7` | `1d1bcae9278fafe373d9d025e2dd030af10046cec93382a23605b96a29c428cc` | `8e0dd4a53e1a0a3778091fc608df296d6453736508c4e109f7855789dd45eaa7` |
| 05 `content/docs/regions/california.md`；原全文 | 59／7787→7787 | `8d78e0e732f372f694a057be6e7876ddf14d769f6e7447af63ece3f5573eec54` | `5baab8679086e3f5768591ed8aee804959657596913ebcf43d932778542627d1` | `8d78e0e732f372f694a057be6e7876ddf14d769f6e7447af63ece3f5573eec54` | `5baab8679086e3f5768591ed8aee804959657596913ebcf43d932778542627d1` |
| 06 `content/docs/regions/new-york.md`；原全文 | 55／7510→7510 | `739fc3c01e1b0ffc6e6f8b60ae96873a104e5b62c7f57bbd9b287a433f974bd5` | `40c8c46c24d01e27c873cc80f344b9ea8e5eca4bd706f6488a68a50627eed3c2` | `739fc3c01e1b0ffc6e6f8b60ae96873a104e5b62c7f57bbd9b287a433f974bd5` | `40c8c46c24d01e27c873cc80f344b9ea8e5eca4bd706f6488a68a50627eed3c2` |
| 07 `content/docs/regions/washington.md`；原全文 | 57／7609→7609 | `a54d9e7034615f6a00ef0930d8334c861677e7ad15f0f0a899b9f4653c098eab` | `a21abd8c99b409f6d26bcb3eb6842b8b8bd43ef352e36880424cb7790ad2e8db` | `a54d9e7034615f6a00ef0930d8334c861677e7ad15f0f0a899b9f4653c098eab` | `a21abd8c99b409f6d26bcb3eb6842b8b8bd43ef352e36880424cb7790ad2e8db` |
| 08 `content/docs/regions/texas.md`；原全文 | 55／7648→7648 | `d2c2471e1c312f154ac0d99e0fb2b0e8b2433859fe4510c790f81eecb1acd975` | `6db3219269021c492f82f543e05fb8c5821ecd9095c9b919a5b4dd193e8fb6fd` | `d2c2471e1c312f154ac0d99e0fb2b0e8b2433859fe4510c790f81eecb1acd975` | `6db3219269021c492f82f543e05fb8c5821ecd9095c9b919a5b4dd193e8fb6fd` |
| 09 `content/book/people/school/school-enrollment.md`；原全文 | 114／16890→16917 | `b8a01b4ae60bdc4441c9ace62002b07b90dc47e629dd06653dea6868b1f03cc0` | `7ed5e90f8bdf20e40f51f7701185ea7c9664b3fc81cdbe9eb66cc45a2f4a4a41` | `491fc6eeabdbcf76b869fa450ff3c101cad98ff9766ae54bed45d6f7b79ec1c5` | `31f3b8ca70d32ce99a0268296caf2d05edd9be500ada5e6d364a832c18299808` |
| 10 `content/book/people/school/school-support.md`；原全文 | 133／28021→27992 | `04d5ef6d12845b42122e149d02290671845bb1bfe88244470a1ae31b33c53af2` | `61d25f70841824d0a244db43da35e9bcefd7654c383e5649efecff1fa13d3aed` | `7b85c2e4a50b0355aa89980186a9103600d66abdb110a9ef90e76a113e584b71` | `bc20441683ca57af92938d69605bed5f8d643c87755d132939ed75884c2694cb` |
| 11 `content/book/people/aging/caregiving-plan.md`；原全文 | 148／22660→22788 | `67cbe66df380938966b619fc692145282321bf43696522a0a682788dafc85c1a` | `88bc9cc0ae8e8f3cccd5ed46e9cba708d56094b64ef3b0e93aaeb2d0a3d6f638` | `9a5cf557ecbd0ac87bcb7df0831bdac58c0cb324fbef20f5b48c27f769bd3609` | `97d5ee026ce33a96c2be39aba2d9927828dc3b7b20a89aca078c9a56b15a6d93` |
| 12 `content/book/people/aging/advance-planning.md`；原全文 | 125／25100→25116 | `48c70ff0af9f63f4b21e9c2f9c85ea5a7c6ff2607d475f5ecd4cdf61312f2be0` | `6c45952220efe69f02213ddc5bd772c0d401749d7114958eff11cf32a4866941` | `581fc7d83f10f9f464bd0ef52c73dc25c1c01075ed186657b22884a1b9ff47f0` | `668ef23eb6596d81a9c011451cbf6c4a19f143e94dc9cfeec124cf6591a06879` |
| 13 `content/book/people/aging/death-arrangements.md`；原全文 | 125／26615→26636 | `7f527b505e36cdd4ad519ccae92b745a3e48187f69f1e6f63f6f89b7e2244397` | `1b6cd2383b8a099a468dfde0ad64f370373a4db81d913875e41e879f7a02fb92` | `51b15e77c5314ef1bf7cab976cb83b0946ba76fd816ba51ce41e7605679cb0dd` | `8c57542437a9476c8d1804adf0575ba211a8510ea2e08b680f470fcba7af9d4f` |
| 14 `content/book/people/language/service-conversations.md`；原全文 | 127／10778→10756 | `62b636f6b67ceecfdd3d7f0800b863c39afa29a1bb3370d40b5eb8f8e0a0d41b` | `83152695e21896beb1b547161334338ebfb781c9d00852b2f07c723fbb4f2c88` | `41a9d3b418c44ad20e39a326fcaa862cce6a16d3408ff7d8abf2aa747a893a6c` | `1caf0bcc7538971bb6f2aa57f749f7db789b73f233e41d234f0b5568741fb2e6` |
| 15 `content/book/rights/safety/emergency-help.md`；原全文 | 67／7685→7685 | `49a8d07854505ac39f6dc4463b7d8e36d06847089314403c8e507c5c469ee095` | `69d394a012f96e3e92d9427e80752829a7956f367cb917e75352a7a662001b19` | `49a8d07854505ac39f6dc4463b7d8e36d06847089314403c8e507c5c469ee095` | `69d394a012f96e3e92d9427e80752829a7956f367cb917e75352a7a662001b19` |
| 16 `content/book/rights/legal/finding-help.md`；原全文 | 100／13926→13899 | `98b56bc44fa152f1a3674528a3ee27c87f6fe75d7785e3489918da4f3f9f639d` | `84e4b3cd363c992d51b815601ee9a903b54ca05aaeff9e2bb07a262fb92e13ea` | `4a1ef3b78e05ed734897b889f9d4888affde0f0f656196e3ae795f46154ee2cb` | `72b1ccb6f9ea89dbc56e186e730769f5b112069b91232a1e75f2fbca6b28fcac` |
| 17 `content/book/people/health/coverage-changes.md`；原全文 | 100／19376→19255 | `54f796e916ab7d1d0cc19fca99e8ffc8919a6bff161674e547ce17cee5da3943` | `dd093f87de1dad5a266854cec072235b006ef12d2cb04bcc584163d3c2ef79b8` | `0027fac51a855511b7301404a4aa38a121d501950a9a6c97109a29482d8848e2` | `33b6ddc96b7132275ba3b0aa8c8aafa85f174274a9ddce3ce91c2caf9e2797ce` |
| 18 `content/book/people/health/insurance-costs.md`；原全文 | 63／6125→6171 | `c9ffeddbe4ab79912751089ee35114d95e5264fa211a58e9dc3ac7be0a4c5d3b` | `c59989a3ae7fc4f451f8b811679a278c93b7447f1975d491306b00c5e5289e5e` | `d682854aa03ae2c37081e8df0cac1286b8b973877513c84f5e8d86246ae94e7b` | `f12dc27ebfdf4e0386fcd9fc809bf3c0f9db58cb9125b4c15a4a440269c7560a` |
| 19 `content/book/people/health/appointment-network.md`；原全文 | 59／6395→6552 | `4c8d3b8551eb31ed9778e29a6a5b9724ee1fbe6bbf53f9d409e8e10c85b76de6` | `91a9063db2e45001ae86f1250f39de4c98981041e034f9220656aacf875673e5` | `7d99bc988b333e482094362f7366994a17a988b9c4db7a222f273fff125c901d` | `a1ccd540e2b8f078b635e0405eeb2158756395e4b2dc430da33a98042f802b71` |
| 20 `content/book/people/accessibility/mental-health.md`；原全文 | 117／23235→23309 | `575c7d19fa70154da8672ea22f9d942a3c48fd89998f6f41ccb047a13a428917` | `071e9a4abb0eff8c7b1cf4bb8be584f9ac5ba272d3fecfd6029f54f65bb8852d` | `8b52a308ae7a27c57845818ad47800d86a0d89ce89123797893c8eaac45f05d4` | `91868935b45defdc361648150cfdd0f1e8da919987814cbc6f202286cb0ccd88` |
| 21 `content/book/work/employment/workplace-rights.md`；原全文 | 137／26280→26280 | `049c4ecee882f7ad65d2d713568d2e2df999c895b37e0f735b44fe56ee0def05` | `325c2509ab16ecb66e06ce2b94ceab8c61349be0e5ec4a94da7d90c452e17916` | `049c4ecee882f7ad65d2d713568d2e2df999c895b37e0f735b44fe56ee0def05` | `325c2509ab16ecb66e06ce2b94ceab8c61349be0e5ec4a94da7d90c452e17916` |
| 22 `content/book/foundations/government/which-government.md`；原目标／FM | 82／8914→8914 | `2bba54971e426152ce774fce4804325aafdf25ed47371495eefaebe48a74dc7c` | `5d6f3ef7d123a102ddb306e335ff7c062ec0e1e5d6ef46787ddf241e699411f3` | `2bba54971e426152ce774fce4804325aafdf25ed47371495eefaebe48a74dc7c` | `5d6f3ef7d123a102ddb306e335ff7c062ec0e1e5d6ef46787ddf241e699411f3` |
| 23 `content/book/people/accessibility/accommodations.md`；原目标／FM | 134／25223→25345 | `1b028fd251ea4f4878076d3cae67fc7aec940ad7e44d7637c269c4362f24db0c` | `11cbbe7d03520624d7ede0987bedc05b672a06f886da70f3e5da8696547fae73` | `988d870296bfba09feda32475657ea5542c321765ce5ca29ecf65a6e3f062d59` | `85177df257da56955b3bc895498a8e2dc36e3df2bb98937e7d42b092646ec484` |
| 24 `content/book/people/health/medical-bills.md`；原目标／FM | 71／8705→8847 | `485addc8f652f6ebe777814fa5527e8c43f406519cf50d0d809a74be90304fd0` | `89d72e74ec31531fdffa889219c206fdc7b59b263738608d69bd537a3099340f` | `b85af8f5bbaf5a130efec97c0c31022e3fcee983273d734ceefe508277cac141` | `c8166d650e79a407a0fef67f82408c94d2e8a87812c6ede0e780e351b5f4e699` |
| 25 `content/book/work/employment/pay-stub-overtime.md`；原目标／FM | 117／17434→17456 | `0b21289995a0c69432629ae8231032d132c2593cdf21c3ddf4db029b89f21c0a` | `ab83b0b0af53e6a88864243af5c6a075359b71b7ccec19b14b868e6f3230f38f` | `4fd1304b02a81b34fc93b05c3ae5d74f32bc402ccd7eff3541140dd239f2c677` | `9edfdcbc722be752251387568ca8de107d4f5577acfe4cce723f9fa9b3373991` |
| 26 `content/book/work/employment/job-loss-support.md`；原目标／FM | 120／20432→20422 | `160a39b1cdd003a0528be0396f50330ddda787cc1e43b11491f630372bf3f7d7` | `bbd078da215a4af112ade216f2089dd295d7f17d868aab97a51793f8cc82c561` | `eff07740f03d91f29d2dd376bc50d9e45268e6dcc884f2b07e1346a88c915160` | `af2d3a57bd18c3e3e75e32544d3e964400cd3bf968b4802a5efed73304ac6d38` |

收口：本轮三条普通家庭链的新canonical版本核对完成，无新的必要正文修改请求。26依赖的旧新版本及当前52摘要已独立绑定，原21全文／5目标范围和原8一级采用／失败边界保留。只写本新审阅，原家庭与people第三记录均未改；没有构建、提交、联系机构、个人申请或付款。九次实际GET仅作新版文字、HTML片段与锚点核对；全书工程、目视／手机／打印及最终同步由root独立完成，本记录不提前宣称这些结果或全书事实PASS。
