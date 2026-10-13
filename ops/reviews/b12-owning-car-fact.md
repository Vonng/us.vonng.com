# B12 自用车辆独立事实审

2026-10-13；独立参与者 banking_fact，原作者 static_editor，拟第三人 birth_fact。本记录只审 `content/book/life/transport/owning-car.md`，不修改作者正文、地图、证据、元数据或共享文件，不构建、提交或联系机构。历史作者任务已冻结交主控另派异人，不能把其作者身份混同本审阅。

## 当前结论与版本：重量范围必要补正后

**当前独立事实结论 PASS，仅绑定本节新冻结稿。** 第三人实际发现L54“以下”可能包含本数，原作者已按root正式授权改为“低于”；首轮事实审未识别这一中文端点歧义。旧版本的事实PASS不承载新稿，本人本次完整重读新正文、两包及自己的旧审阅，核摘要、唯一逆换和自己的DMV原件后重新作结论。

- 完整正文 SHA-256：`a3a6c544a0acacc76bbdf6ef475d4072fac7c61ed863ce9c667141a4f8ba209f`，UTF-8 `full.split('---', 2)[2]` 保留所有换行。
- 整文件 SHA-256：`0a84ca4685ef8ddcef05a14d2c6fc5f189f662f84ab1603600ad9c45fc02320b`，152行、28,300字节，本人独立实算。
- 地图 SHA-256：`59ee02187e41047ee9e1afcc23e2a2748ff320157febaa1ffbde05e5f9c33c69`，62行、12,108字节。
- 作者证据 SHA-256：`71e67a30f6e317b666575187b62d4015db9ecffe85bc8654b1a15c311d508226`，162行、42,890字节。
- 实际元数据仍written／draft true、verified与reviewed_by空；作者static_editor／事实banking_fact／第三birth_fact，三人不同。第三新版本、候选与工程仍由主控继续，不表示已集成。

以下首轮64源的逐件实际读取与失败原样保留为前阶段历史；本轮只重新读自己的DMV OLIN2026–10原件，没有重新请求或读遍64源。新全文阅读、实际采用段和逆换证据见末节。原审阅在本次修改前为112行／27,495字节、SHA `5bbc81cb009ba1b8fdedc5658193d21b511b74080934448711e2ca5fcd3bc9a2`，仅作旧记录历史定位。

## 首轮结论与版本（历史，已不承载当前新稿）

**首轮旧版本曾独立事实 PASS，仅绑定下列旧冻结版；该门禁不能移给顶部新稿。** 本人完整实际读152行正文（初读1—50、51—100、101—152，收口另完整1—78／79—152）、56行地图和156行作者证据（1—35、36—70、71—105、106—140、141—156）。作者记录只用于定位，以下回源均为本人新请求后真正读到的主文／物理页，未继承作者成功、旧缓存或其补读状态。首次保存为核验进行中，只有下述实际回源和最终重算完成后才改此结论。

- 完整正文 SHA-256：`876ac70b0b27d1c7e25ad088fed0a842b5abdafc648be881b5243537b69beba7`，UTF-8 `full.split('---', 2)[2]` 保留所有换行。
- 整文件 SHA-256：`ee5811a1d070378000aa615f1ba57c720b0f890b5d131ab0646b431cd3371568`，152行、28,297字节，本人独立实算与正式送审一致。
- 地图 SHA-256：`65f85b6192cbc7ca0f0b0398210dca95551333c0cac2fe034a43b7e76b90222e`；证据 SHA-256：`887b1b6c583b86bfc37bb85213bd4f778b238ebf85e8419532bacf5cdb187185`。
- 实际元数据 written／draft true、verified 与 reviewed_by 空；本审阅不安装候选。

## 首轮本人读取方法与保存点

已新取正文64个不同外引URL；下载前对 `.cache/car-fact-banking/source-index.json`、`fetch.py`及 f01—f64 各 `.raw/.txt/.json/.pdf` 258个具体路径逐一 `git check-ignore -v` 成功。普通HTTPS保留TLS校验，失败仅试正常127.0.0.1:8888代理；没有绕挑战、账号或VIN查询。索引／HTTP只记录取得，不证明阅读。下表“缓存行”均指本轮自己新取得的文本；网页工具行从0起，PDF页为物理页。读取日期均2026-10-13，页内版本与查阅日期分开。

| 独立一级来源 | 本人真正读到的范围、支持的采用项及边界 |
|---|---|
| [CFPB预算，f05](https://www.consumerfinance.gov/ask-cfpb/how-much-can-i-afford-to-borrow-for-a-car-or-auto-loan-en-751/) | 普通及代理403；web原页真实全文82行读到，主文20—72。Last reviewed2023-09-12／modified2025-10-28；车辆、附加品、税费、首付及持续保险油电维修、家庭收支合算，不采用示例作报价。 |
| [CFPB车贷比较，f06](https://www.consumerfinance.gov/ask-cfpb/how-do-i-compare-auto-loan-offers-what-should-i-look-at-besides-the-monthly-payment-en-753/) | 普通及代理403；web全文69行实读，核心20—59；2024-01-30。APR、融资总额、期限、利息及负资产风险；其示例利率与“建议五年”未作为本文规则。 |
| [CFPB买车／租赁，f07](https://www.consumerfinance.gov/ask-cfpb/what-should-i-know-about-leasing-versus-buying-a-car-en-815/) | 普通及代理403；web全文89行实读，核心20—79；review2023-09-12／modified2023-09-14。使用权、期限里程、磨损、提前结束及买断条件；未采用典型里程为所有合同。 |
| [FTC融资与租赁，f08](https://consumer.ftc.gov/articles/financing-or-leasing-car) | 本人普通及代理404（与作者403不同）；web原页全文101行真实读到，主文11—73，July2022。落地价、共同签约、negative equity、银行／dealer比较、最终批准、完整合同副本及叫回改约继续；不承诺贷款。 |
| [FTC二手dealer，f14](https://consumer.ftc.gov/articles/buying-used-car-dealer) | 普通及代理404；web原页全文146行真实实读，核心13—123，April2024。Buyers Guide／as-is／书面保修、独立检查与历史／安全检查区别、联邦无普遍三日退车、州及合同取消。私人交易未被套同一Guide义务。 |
| [CA实施备忘录，f16](https://www.dmv.ca.gov/portal/file/26olin10-pdf/) | web真3物理页／107行全部读到；本轮普通200取得179,667字节真PDF，后来另完整逐页读本地117行。OLIN2026-10，Implementation Date2026-09-22；P1范围／2026-10-01／替代付费二日／≤50,000美元二手自动三日，P2—3执法与参考。未把memo的business days自行补成完整法条算法。 |
| [CA现行生效说明，f17](https://sd24.senate.ca.gov/news/press-release/california-car-shoppers-set-benefit-strongest-consumer-protections-nation) | 本人web真全文56行，正文3—25实读；日期2026-09-30。400英里及可合理restocking fee与三日；立法作者官方说明不是完整法条。CIV1784.43 web及后续本人普通／正常代理均403，尚未读到最后法条、截止算法、退款公式，不据搜索或旧二日费用表填空。 |
| [TX买卖，f09](https://www.txdmv.gov/motorists/buying-or-selling-a-vehicle) | 普通200，本人实际缓存1—25／270—310／550—610，非877行全文。2025-07-01金属牌、买方30日、卖方通知30日、130-U／lien／title-only、Harris等17排放县、登记保险、卖家身份VIN、dealer代办收据与牌照保留／转用／销毁。县下拉及特殊赠与未全读。 |
| [TX新居民，f32](https://www.txdmv.gov/motorists/new-to-texas) | 普通200，实际1—70及300—323，非323行全文；30日登记、county tax office、原州title或registration／130-U、title非统一强制、排放县先检；27行精确支持US军队现役及在TX高校的非居民全日制学生例外。未采用费用数额或全部county表。 |
| [TCEQ现行检查，f33](https://www.tceq.texas.gov/airquality/mobilesource/im.html) | 普通200，实际1—80／139；背景及2025-09-24 adopted正文明确普通非商用2025-01-01免安全检查、受影响县汽油2—24年车仍年度排放。2026租赁修订附件未开；不把目录标题当新条文或本页普通车新规则。 |
| [WA买车登记，f10](https://dol.wa.gov/vehicles-and-boats/vehicles/buying-and-selling-vehicle/buy-and-register-vehicle) | 普通200，完整171行按1—95／96—171实读。15日、全owner title、agent／notary前签申请、按年款里程文件、私人无牌先trip permit、dealer代办及未过期WA驾照／法定豁免；未展开低频全部费用或具体人物资格。 |
| [WA迁入，f29](https://dol.wa.gov/moving-washington/vehicle-registration-and-plates) | 普通200全文70行；30日、先WA驾照、driver／vehicle office分开、银行持title传真、地址／续期与toll，未操作申请。 |
| [WA Clean Car Law，f31](https://dol.wa.gov/vehicles-and-boats/vehicles/buying-and-selling-vehicle/clean-car-law-emission-requirements) | 普通200全文80行；2009+新车及条件适用<7,500英里二手、WA居民／豁免、VECI标签，不能修成新certification。未把停止定期检测读成任车皆能入州。 |
| [WA停止排放检测，f30](https://ecology.wa.gov/air-climate/air-quality/vehicle-emissions/emissions-check-ends) | 本人普通200全文36行（与作者403不同）；2020-01-01停止续期检测，改装／冒烟仍违法；未采用动态空气指标。 |
| [CA私人购买，f22](https://www.dmv.ca.gov/portal/vehicle-registration/new-registration/registering-a-vehicle-purchased-from-a-private-party/) | 普通200全文32行；10日买方／5日卖方、签字title／REG227／bill of sale／smog和税费入口。网页旧10年里程未作为本文规则。 |
| [CA登记手册，f23](https://www.dmv.ca.gov/portal/handbook/california-driver-handbook/vehicle-registration-requirements/) | 普通200全文36行；购车10日、成为居民或工作20日、CA排放资格；未读全部手册各语种。 |
| [CA外州登记，f34](https://www.dmv.ca.gov/portal/how-to-9-register-a-vehicle-from-out-of-state-nonresident-vehicle/) | 普通200真实重定向官方HTVR9，真2页完整89行逐页读，REV3/2020。REG343全owner／lessor、title／登记／VIN核验／CA smog、材料不全先交申请费用、发行州补title；旧10年里程与特殊低里程细目未在本文扩用。 |

以上为首批真实保存点：其余采用URL当时尚待读取，未以获取成功或局部核完认整体通过。下节记录随后本人真正完成的回源，不倒写当时阅读状态。

## 后续本人实际一级阅读（2026-10-13）

| 独立一级来源 | 本人实际读段／版本、核对结果与边界 |
|---|---|
| [LA Metro，f01](https://www.metro.net/riding/) | 普通200，缓存1—35／88，核心5—17为Los Angeles County行程／站点／实时／地图及提醒；不以目录存在声称实际算过行程、票价或减免。 |
| [MTA，f02](https://www.mta.info/) | 普通及代理403，第一次混合web仅标题未算阅读；后来本人单独真实web全文62行，0—14及33—44站点／实时／无障碍入口。未实际执行行程或读取全部子计划。 |
| [King Metro，f03](https://kingcounty.gov/en/dept/metro/rider-tools/) | 本人普通200完整41行（与作者403不同）；route／Trip Planner／Next Departures、停车及客服电话口译，采用只为真实本地工具。 |
| [RideMETRO，f04](https://www.ridemetro.org/riding-metro/apps/ridemetro-app) | 普通200，1—81／166真实读到，行程时间／起终点／路线站点、无账号也可用、实时需网络、服务提醒及视觉辅助；未读82—166使用条款，不宣称账号／合同或现场行程测试。 |
| [DOJ消费者NMVTIS，f11](https://vehiclehistory.bja.ojp.gov/nmvtis_consumers) | 普通200全文90行；title／brand／里程／保险total loss／junk与salvage，州标记差异、可能漏项／false negative及取州完整产权。旧87%覆盖与2008统计没有采用为2026数据。 |
| [DOJ报告说明，f12](https://vehiclehistory.bja.ojp.gov/nmvtis_understandingvhr) | 普通200全文51行；五类指标、严重受损salvage及独立检查，维修／召回不属简报完整内容；未购买或验证某个VIN。 |
| [NHTSA召回，f13](https://www.nhtsa.gov/recalls) | 普通及代理403，本人真web原页199行中的45—190实际读到，采用58／63—75／168—179。VIN、未修记录、已修／近期未列、厂家安全指示及免费补救；未读全部品牌及手册，不以查询0断言无历史问题。 |
| [NHTSA里程，f15](https://www.nhtsa.gov/vehicle-safety/odometer-fraud) | 普通及代理403，真web165行中的45—164实读，核心125—145；title／保养记录核对、里程披露及2010或以前／20年例外。正文没有套CA／NY旧材料的10年概括；页面轮胎与历史统计未扩用。 |
| [TDI保险指南，f18](https://www.tdi.texas.gov/pubs/consumer/cb020.html) | 普通200，真实1—110及158—283／283。Last updated12/11/2025。责任／碰撞／其他损失、deductible、loan额外保障、保单司机／用途、新／借／租车确认；195—283事故留证、保单及时通知、估价／拒赔、全损与未偿贷款、代步及争议。111—157未读，不宣称全篇；TX约20日自动覆盖／prompt-pay／退保退款日数没推广全国。 |
| [NY保险，f19](https://dmv.ny.gov/insurance/insurance-requirements) | 普通200全文74行；NY责任保单、登记与保单同名、双registrant材料、ID卡及电子报告都要、180日自卡生效起，有效登记持续保险；没有把owner／registrant混同。 |
| [CA保险／停用，f20](https://www.dmv.ca.gov/portal/vehicle-registration/insurance-requirements/) | 普通200全文56行；公路行驶／停放财务责任、证明、取消前通知、ANU与登记续期PNO不同。现30／60／15已读但正文未加四州金额表或自保全部条件。 |
| [WA财务责任，f21](https://dol.wa.gov/driver-licenses-and-permits/mandatory-insurance) | 普通200全文114行；责任险或合法替代、随车证明及州外车按登记州规则。金额／自保／保证金例外已读，未扩成普通申请统一资格。 |
| [CA BAR smog，f24](https://www.bar.ca.gov/smog-check) | 普通200全文194行按1—110／111—194实读；私人过户90日、certificate有效90日、年款／燃料／转让vs续期／外州初次不同、STAR及失败／修复／referee；只用条件与继续入口，不采用动态价格或把smog当机械检查。 |
| [NY登记，f25](https://dmv.ny.gov/registration/register-and-title-a-vehicle) | 普通200全文108行；私人登记／title、实际office及材料guide、卡生效180日、登记10日检查扩展／前车主检查无效、文书核错。未承诺全部收件日期或费用。 |
| [NY车辆章，f26](https://dmv.ny.gov/book/export/html/1566) | 普通200全文84行；9—24迁入30日、MV82／姓名6分／出生、所有权／lien／税单；注册与title区别、卖方拆牌和保险、10日私人检查。页中旧10年里程／个别旧邮寄地址未作本文新规则。 |
| [NY ID82，f27](https://dmv.ny.gov/forms/id82.pdf) | 普通200真2物理页，全123行逐页实读；页内ID82(10/25)、PDF Mod2026-03-17分别记。P1证明姓名6分／生日、原件或发证认证、至少一项签名；两页各证件条件。本文只引实际认可文件入口，不保证外国证件或无SSN人人同一清单。 |
| [NY安全／排放，f28](https://dmv.ny.gov/new-york-state-vehicle-safetyemissions-inspection-program) | 普通200全150行按1—80／81—150实读；21每12个月／换registrant，93—110排放按年款／燃料／重量及真实纽约都会县；许可修理、失败继续、维修投诉90日／3,000英里。机械明细已读但本文未代车检结论。 |
| [Harris实际办理，f35](https://www.hctax.net/Auto/Appointments/Appointment?v=1) | 本人普通200（作者403）真实1—38及159—178／178；首次title／new resident到场或预约、dealer／lender邮件先713-274-8000核收到、hold-file另须record。没有采用可能旧检查通用句／费用，未预约。 |
| [NHTSA轮胎，f36](https://www.nhtsa.gov/vehicle-safety/tires) | 普通及代理403，本人真正web原页342行完整输出实读，采用188—241冷态压力／门边标签非胎侧最大值及厂家换位／不同尺寸例外。没有采用统计、具体寿命或低频爆胎操作／PDF。 |
| [FTC维修，f37](https://consumer.ftc.gov/articles/0211-auto-repair-basics) | 普通及代理404；首次混合web只0—32、后续原URL和ref两次Timeout、find无匹配均不充全文。后来本人真开 `/articles/auto-repair-basics` 重定向现引用页，实际0—76及178—196；August2012。诊断费／第二意见／书面估价及超金额再许可、完成工单及进出里程、厂家维护、保修和向manager继续。77—177机械排故未读／未采用。 |
| [WSDOT toll，f38](https://wsdot.wa.gov/travel/roads-bridges/toll-roads-bridges-tunnels/good-go-accounts-passes) | 普通200，真实1—88及134—185／349；登记地址纸账／866-936-8246／无账单查号，卖出或被盗举证、州登记责任与帐号不同。89—133及186以后未全读，不写全部费率、期限或保证移除账户即免责任。 |
| [NYC311停车，f39](https://portal.311.nyc.gov/article/?kanumber=KA-02275) | 普通200真实1—77／511；40行30日从summons／NOL开出、10位号码／证据／邮件确认、57—58任一语言书面材料／中立认证翻译／英语决定。未读全部申诉、实体抗辩和后台，也没提交。 |
| [CA SR1，f40](https://www.dmv.ca.gov/portal/dmv-virtual-office/accident-reporting/) | 本人普通200全文20行；DL／ID、VIN或plate、双方保险、10日与伤亡或>1,000、另于警察／保险报告。没点击Start或另填表。 |
| [CA事故／财务责任，f41](https://www.dmv.ca.gov/portal/driver-education-and-safety/dmv-safety-guidelines-actions/financial-responsibility-insurance/) | 普通200实读1—35／109；18—28准确支持任何伤亡／任一方>1,000、10日，以及私人场地仅自己财物且无人伤亡免报。未读余听证停牌程序、不认证全页。 |
| [NY驾驶人事故入口，f42](https://dmv.ny.gov/records/file-a-motorist-crash-accident-report) | 普通200全文65行；伤亡／任一人>1,000，伤亡立即警方、本人报告另办，online或邮寄MV104、副本入口。未登入NY.gov／提交。 |
| [NY MV104，f43](https://dmv.ny.gov/document/mv-104) | 普通200真实重定向mv104.pdf，2页、5/25；pypdf提示旋转文字不完整，没有称其抽取全文。另用pdftotext布局真读P1全部126行、P2全部94行，并真正本地渲染／view_image目视P2。P2顶部10日／>1,000／NY发生、签名及原件寄送；不产生可提交表件。 |
| [WA事故入口，f44](https://dol.wa.gov/driver-licenses-and-permits/driver-safety/reporting-collision-damage) | 普通200全文58行；调查警员报／未调查本人4日、真实WSP／本地警察与sheriff入口；报告阈值另以以下原法及WAC核，不把驾驶记录段独自当法。 |
| [WA RCW46.52.030，f45](https://app.leg.wa.gov/RCW/default.aspx?cite=46.52.030) | 普通200全文86行；(1)伤亡或任一人表面损失≥WSP现阈值、4日，调查警员(3)代报；(5)1987旧500非现阈值。原法沿革已读，未冒称2026新修。 |
| [WA WAC446-85-010，f46](https://app.leg.wa.gov/WAC/default.aspx?cite=446-85-010) | 普通200全文24行；正文2015-01-01阈值1,000，filing12/3/14、effective1/3/15各如原页，不自行改其日期差异；只采用当前≥1,000。 |
| [TX现行550章，f47](https://tcss.legis.texas.gov/resources/TN/htm/TN.550.htm) | 普通200是真法条；本人1—150／366，§550.001真实道路／公私地点边界，.021—.023停车安全与身份保险救助，.026伤亡／不能安全正常驾驶时立即按所在地通知，.062警员电子10日报告。151以后未全读，不用旧导航200或CR2替法条。 |
| [TxDOT事故与副本，f48](https://www.txdot.gov/data-maps/crash-reports-records.html) | 普通200真实1—75／124；警員CR3／10日、本人获取副本、2017后不保管CR2／提交将销毁。76以后与全部披露规则未读，不承诺公众任意查看。 |
| [CA全损／不可修复，f49](https://www.dmv.ca.gov/portal/vehicle-registration/new-registration/total-loss-salvage-non-repairable-vehicles/) | 普通200全文60行；不可修复证书不准重登、保险赔结与无赔结申请职责分开、发行州补title。金额／bond细目不在本稿扩用。 |
| [NHTSA失窃，f50](https://www.nhtsa.gov/vehicle-safety/vehicle-theft-prevention) | 普通及代理403；第一次混合web只有标题没算读，后来本人独立真web原页130—157／158实读，139—145立即警方／case号／VIN牌照车型色／保险／找回先通知。24小时为页面建议未写成全国法律或全部保单统一截止。 |
| [WA卖车，f51](https://dol.wa.gov/vehicles-and-boats/vehicles/buying-and-selling-vehicle/sell-vehicle) | 普通200全文120行；title／bill of sale双方副本、先收款、拆牌、5日卖方报告含trade-in／处置／保险，代办要自己确认、转移完成后移账户。日期算法由f56实核。 |
| [CA title，f52](https://www.dmv.ca.gov/portal/vehicle-registration/titles/title-transfers-and-changes/) | 普通200全文100行；seller／lienholder签、title／REG227／REG166等、外州title丢失向发行州，NRL与过户不同；队列旧日期／处理预估未当现时保证。 |
| [CA NRL，f53](https://www.dmv.ca.gov/portal/vehicle-registration/titles/title-transfers-and-changes/notice-of-transfer-and-release-of-liability-nrl/) | 普通200全文83行；5calendar days、买家姓名地址／VIN／里程／日期、保存确认、NRL不转title也不删名，责任免除与法院判断有边界。未提交。 |
| [NY交牌，f54](https://dmv.ny.gov/registration/surrender-return-or-turn-in-your-vehicle-plates-and-registration) | 普通200全文105行；交plates和registration后停责任保单、迁州旧牌、FS6T收据／PD7，邮戳与receipt不同。其他车辆和退费全部例外未推广自用车。 |
| [NY保险断档，f55](https://dmv.ny.gov/insurance/insurance-lapses) | 普通200全文124行；有效登记持续保、卖车／转牌／交牌及证明、被盗／扣押另分支；私下交车不结束州记录。没有用停保代表已注销。 |
| [WA卖方日期，f56](https://dol.wa.gov/vehicles-and-boats/vehicles/renew-or-replace-vehicle-tabs/affidavit-lossrelease-interest) | 普通200本人1—45／143实读；all legal／registered owner签、buyer15日、seller5日排除周末州假日。其“20年或新”里程简写和继承／trust等余段未扩用。 |
| [CA个人报废，f57](https://www.dmv.ca.gov/portal/handbook/vehicle-industry-registration-procedures-manual-2/salvage-nonrepairable-junk-vehicles/junking-a-vehicle-individual/) | 普通200全文37行；自己拆解前向DMV记Junk、所有权链、交牌及smog报废豁免。普通停用／salvage／不可修复有别；未扩写commercial税清／bond。 |
| [CA投诉，f58](https://www.dmv.ca.gov/portal/file/dmv-complaints-ffinv-1-pdf/) | 普通200真PDF2页，全99行逐页实读；FFINV1 NEW9/2019。dealer合同／登记、调查division、INV172A／相关副本及实际office渠道；P2“不能强迫退车”旧概括未覆盖2026取消权或作为本稿否定。没另填INV172A。 |
| [BAR投诉，f59](https://www.bar.ca.gov/complaint) | 普通200全文69行；CA维修／smog／售车仅涉及修理、受理编号／补件、调解与执法分开；非一定赔付或保证7—10日。 |
| [NY商家投诉，f60](https://dmv.ny.gov/a-guide-for-consumers-what-to-expect-if-you-file-a-complaint-against-a-dmv-regulated-automotive) | 普通200全文83行；VS35及附件、Business Regulation Unit、维修90日／3,000英里先到，行政无法强制赔款。未套全部购车纠纷或保证处理时间。 |
| [WA商家投诉，f61](https://dol.wa.gov/professional-licenses/file-complaint) | 普通200全文138行；vehicle business选择、时间线／所有相关副本，title申请／合同／付款、360-664-6484；非对私人seller的统一受理或赔偿决定。 |
| [TX dealer投诉，f62](https://www.txdmv.gov/complaints) | 普通200全文71行；Auto Dealer／现online入口、销售合同／广告、888-368-4689；行政罚款不代私人赔款请求，未扩用Lemon Law或表后台。 |
| [TDI投诉，f63](https://www.tdi.texas.gov/consumer/get-help-with-an-insurance-complaint.html) | 普通200全文55行；updated7/8/2026、company／agent／adjuster、Auto选择、800-252-3439；未登录门户／上传。 |
| [NAIC州主管，f64](https://content.naic.org/state-insurance-departments) | 普通及代理403挑战；第一次混合web只标题未算读，后来本人独立真web全文44行，11—33按州目录及complaint实际主文。未执行动态筛选、读全部目录PDF或验证某真人受理。 |

### 真PDF原件与读取界限

本人的5件正式采用PDF均由本轮正常TLS实际取得并核真实页数，不沿作者哈希认读：f16三页／179,667字节／SHA `c5b1366b796bf4bdc8c681bad3995ffd782b0728c23c34fe99a0dc4e8b5f47d6`；f27两页／132,558字节／`3b7a612c92a5344437fbf8e432dae7927cad4e6929f50d6a23654b9d14e53a0b`；f34两页／299,137字节／`7d929c7a1c321e879b21171b5066cc9f884633c3703445183bab6792321df8db`；f43两页／284,531字节／`85702177c18598a039cbe6494277fd18c6591306e116de3a9097e934b564fda8`；f58两页／245,978字节／`90492bb893d5313305399c187b666a39751596cd196e79974fabe90ee95e091b`。f43两页实际pdftotext、P2另真PNG目视；其他PDF为逐页文本读，未冒称所有原页目视或交互表字段测试。PDF文件元数据日期与页内版本分开，上表以页内日期为采用版本。

新增ca-law `.raw/.json`及f43-layout.txt、f43-page2.png在请求／生成前四个具体路径也逐一核忽略。CIV1784.43正常HTTPS及正常代理各403（5,735字节挑战），web403，完整现行法条未读；不反复挑战、不自行计算三工作日／周末、退款公式或补旧二日金额。正文L54采用本人真实9/22主管实施备忘录及9/30官方生效说明，所写三日／50,000／400／可能合理扣费与这两来源一致；它明确要求本次书面截止和通知／返车／退款条件，没有把未核细则当全国或全部车辆规则。

## 首轮内链与采用断言交叉核对

本人重新读取8个内链的实际当前文件／元数据，均integrated、draft false；只采用本文承接所需段，不继承它们全部外引为本轮新研究。实际读取：credit-records16—42／54—66；reading-contracts16—55；banking-payments61—77／116—128；new-resident-license14—38／86—102；address-changes81—105（采用95—105日常账户）；service-conversations46—53／80—106；emergency-help14—40；finding-help16—41。目标与申请前查本人信用、完整签约文件、付款、驾驶许可／车辆登记分开、改址、书面沟通、紧急911及私人索赔法援相符。

本人再次完整实际重读送审正文1—78／79—152，无截断；先后读到的数值在正文步骤与表格同一对象：虚构450＋170＋120＋110＋90＋30＝970、CA买10／迁入20／NRL5calendar／事故10及>1,000；NY迁入30与保险卡180分开／私人登记后检查10／通常每12月安全检查／事故10及>1,000／维修投诉90或3,000；WA买15／迁入30／卖5排周末州假日／未调查事故4及≥1,000；TX买title30／迁入登记30／卖方通知30／警员CR3期限未作本人表期限；NYC听证30只为该市。起保、逾期、全损贷款、牌照及退出没有新增未读统一承诺。

## 首轮未核实边界与门禁待办历史

未进入真人账户、输入VIN或买报告／贷保申请、预约、实车检测、提交DMV／法院／投诉表；未读完整CA CARS最后法条与截止／扣费公式、全部低频身份和车辆例外、全部县费率／每张表字段、所有保单条款／跨境保险／诉讼期限、动态行程或预约后台。旧2012维修／2019投诉／2020外州材料只采用持续可读流程，未充2026新实体法。普通或代理失败与web真正成功分别保留，混合输出只标题／截断、PDF不完整提示及补读链未抹掉。

64个正文不同外引URL的实际采用段均已本人读到，必要金额／期限／法域与文件已逐项对照；目前无事实返修请求。最后还需重新独立算全文／整文件摘要，读回本审阅完整记录后落最终结论；在此节保存时尚不凭来源数量认PASS。第三静态及工程另由正式不同参与者完成。

## 首轮最终独立事实结论（2026-10-13，旧版本历史）

本人完成上述实际回源、当前8个内链采用段、再次152行正文完整阅读及本记录1—35／36—70／71—108完整实际读回；独立重算正文仍 `876ac70b0b27d1c7e25ad088fed0a842b5abdafc648be881b5243537b69beba7`，整文件仍 `ee5811a1d070378000aa615f1ba57c720b0f890b5d131ab0646b431cd3371568`，地图／证据摘要仍与首轮送审值一致，没有作者修订或待返修项。采用的资格、材料、金额、期限与法域分支有本人真正读取的对应一级主文，未读细则保持上节边界，没有认证这些空白为已核。结论 **PASS**；仅移交主控正式派 birth_fact 第三静态，作者／事实／第三角色分别为 static_editor／banking_fact／birth_fact，不表示已集成、工程通过或个案资格确认。本人只写此审阅和已忽略研究缓存。

## 2026-10-13 单句补正后的实际全文重读与新事实重绑

root正式指派后，本人先独立实算新正文、地图和证据四摘要，均与顶部新值一致，再完整读新正文152行（1—50／51—100／101—152）、地图62行、证据162行（1—40／41—80／81—120／121—162）。另完整读修改前自己的112行事实审（1—32／33—64／65—96／97—112），保留当时真正逐件回源、部分范围、补读、失败和未核细目的归属，没有把原作者这次重读或第三审消息当自己的来源阅读。

正文唯一修订为L54的 `10,000磅以下轻型车` → `低于10,000磅的轻型车`。本人实查新短语只出现一次、旧短语不再出现；在内存将新短语唯一逆换为旧短语，得到正文 `876ac70b0b27d1c7e25ad088fed0a842b5abdafc648be881b5243537b69beba7`、整文件 `ee5811a1d070378000aa615f1ba57c720b0f890b5d131ab0646b431cd3371568`，精确恢复旧28,297字节文件。UTF-8字符串逆换与原始字节逆换结果相同；frontmatter逐字相同，96个链接及顺序完全一致（88外引／64不同URL、8内部目标）。其余金额、日期、期限、适用对象、正文和全部引注未改变。没有生成或覆盖旧稿文件。

本轮真正重新打开的是本人首轮独立取得的[DMV OLIN2026–10实施备忘录](https://www.dmv.ca.gov/portal/file/26olin10-pdf/)：`.cache/car-fact-banking/f16.txt`全部117行、物理第1—3页实际读到；`.raw`与`.pdf`均为179,667字节、二进制SHA `c5b1366b796bf4bdc8c681bad3995ffd782b0728c23c34fe99a0dc4e8b5f47d6`，本人重算两者相同并用PDFReader再次核真3页。页内Implementation Date2026-09-22；物理第1页NOTE、提取17—19明确持牌加州dealer零售或lease的轻型车范围为 **under 10,000 lbs.** ，所以中文改为“低于10,000磅”准确排除本数。此次是自己的既有原件重读，不是新网络请求、原作者缓存或继承birth_fact阅读；没有声称新取得现行完整法条。

第1页41—46自动三日、≤50,000二手及business days简写，原已实际读的9月30日官方说明400英里／可能合理扣费，与没有改变的L54采用范围继续对应。重量计算的完整法定定义、最后CIV法条、三日算法／周末和退款扣费公式仍未核；原普通／8888／web403及旧网页／标题／截断的阅读界限全部保持，没有再次探测挑战或以旧两日条件补空白。此次没有新扩大其它州、保险或事故规则的核验日期与范围。

新正文两包的完整阅读、摘要和唯一逆换均满足，重量端点必要修订有本人实际原件采用段支持；结论 **新版本独立事实 PASS**，准确绑定正文 `a3a6c544a0acacc76bbdf6ef475d4072fac7c61ed863ce9c667141a4f8ba209f`／整文件 `0a84ca4685ef8ddcef05a14d2c6fc5f189f662f84ab1603600ad9c45fc02320b` 及本记录顶部新map／evidence。无待作者事实项。全部首轮未核边界不变，第三人须完整读新稿后重新绑定自己的门禁；本人只修改本事实审文件，没有改作者、他人、metadata或共享，没有构建、提交或对外联系。
