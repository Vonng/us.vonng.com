# 信用卡、个人借款与催收：B15作者证据

2026-10-14，原作者banking_fact。主题地图已先落盘，正文已完整成稿并冻结为末节版本。只拥有`content/book/work/finance/debt.md`与同slug地图、本证据及事前核忽略的自有缓存；拟birth_fact事实／root第三，待主控另派。本记录不是作者自审。下文暂停时的“尚无正文”等均为当时真实历史。

## 恢复与范围

本人本轮实际读上级及项目AGENTS，完整PROMPT408行（首次输出截断160—201另读）、说人话99行，再依次BOOKMAP40、TASKS60、CHECKPOINT61。实际Git和文件检索确认debt正文及两包原不存在，地图先建；已有banking-payments／credit-records等只读参考，未修改。B14 death三件保持原冻结，公共参与最终两审收到，无待作者项。

## 实际来源

以下均为banking_fact本轮10/14实际开读；正常HTTPS／8888失败和web真主文成功分开。`.cache/debt-banking/fetch.py`、索引及逐件原件／提取路径均先实际核git忽略；首轮40请求完成不代表40来源已读。source-index.json只记录请求，不承载事实通过结论。

| 来源／版本 | 本人真实采用范围与边界 |
|---|---|
| [CFPB个人分期借款](https://www.consumerfinance.gov/ask-cfpb/what-is-a-personal-installment-loan-en-2114/)，review2024-08-30／modified2025-01-29 | web真56行全文读，23—40：一次资金、定期偿付、固定或可调整利率、费用和困难可问安排；并不保证放款或获延期。普通及8888为403。 |
| [CFPB费用](https://www.consumerfinance.gov/ask-cfpb/do-personal-installment-loans-have-fees-en-2120/)，review2024-08-30／modified09-04 | web真50行全文读，23—34采用发起／文件／通常可选保险／担保登记与逾期等费用、比较披露；普通／8888均403。 |
| [CFPB信用卡APR](https://www.consumerfinance.gov/ask-cfpb/what-is-a-credit-card-interest-rate-what-does-apr-mean-en-44/)，review2023-08-28／modified08-30 | web真42行全文读，23—28信用卡APR年化利率；不是所有费用总额。初猜what-is-apr-en-44路径本轮失败且不采用。 |
| [CFPB宽限](https://www.consumerfinance.gov/ask-cfpb/what-is-a-grace-period-for-a-credit-card-en-47/)，review2024-09-23／modified09-25 | web真44行全文读，23—30：通常购物、无强制必有宽限、全额按期条件、余额／新购物／现金预支区别；普通／8888均403。尚不决定在正文采用21日账单发送细则。 |
| [CFPB还款困难](https://www.consumerfinance.gov/ask-cfpb/what-should-i-do-if-i-cant-pay-my-credit-card-bills-en-1697/)，review及modified2026-09-02 | web真64行全文读，23—50：立即联系、列收支、说明可付／恢复／拟付款期、核咨询费及减债骗局；不承诺谈成。普通／8888均403。 |
| [FTC共同签署](https://consumer.ftc.gov/articles/cosigning-loan-faqs)，April2024 | web79行全文读，14、30—58责任／费用／信用／无产权／担保物／文件与解除须同意；不同州及贷款类别条件保留，不把notice规则泛化。普通／8888404。 |
| [FTC贷款预付费诈骗](https://consumer.ftc.gov/articles/what-know-about-advance-fee-loans)，July2022 | web73行全文读，2—39：保证获贷与先付费／特殊收款风险；真实申请费可能存在，不称一切预付费违法。普通／8888404。 |
| [FTC催收起诉](https://consumer.ftc.gov/articles/what-do-if-debt-collector-sues-you)，November2023 | web59行全文读，9—25及31—44回应、文件、法院期限、帮助与违规不消债。未采用旧主文的民事判决进入信用报告概括，也不泛化扣薪到四州。普通／8888404。 |
| [RegF1006.2](https://www.consumerfinance.gov/rules-policy/regulations/1006/2/)，页面CurrentVersion | web164行全文读，68—110个人家庭债及collector／originalcreditor／债务购买者定义、例外；并非所有原债权人均受FDCPA。普通／8888403。 |
| [RegF1006.34](https://www.consumerfinance.gov/rules-policy/regulations/1006/34/)，CurrentVersion | web365行中实际只读0—252，48—79初次或5日通知／付清例外及诉状不算初次，115—123验证期收到／推定收到、137—229明细／期限／电子地址。253—364未读，不称全文；30日不是从首次电话自动计算。原记“252—365”有索引边界笔误，本次更正，不增加读取范围。 |
| [RegF1006.38](https://www.consumerfinance.gov/rules-policy/regulations/1006/38/)，CurrentVersion | web116行全文读，49—58本人书面或催收人接受的有效电子方式；85—106及时请求／争议收到后的暂停、重复争议与未争议不等法律承认。不把30日写成催收人统一答复期。普通／8888403。 |
| [RegZ1026.18](https://www.consumerfinance.gov/rules-policy/regulations/1026/18/)，CurrentVersion | web738行只真正读0—242及304—353；首次和续读合并输出截断243—303，尚未补读。采用贷款人、amountfinanced净信用、financecharge、APR／明细和340—348总付款定义线索；付款表(g)核心需补读，后部也未全读。普通／8888403。 |
| [CAAG催收](https://oag.ca.gov/consumers/general/debt-collectors) | 新普通TLS200原件提取133行全文实读，6—11、31—51、77—88、124：核债／法院／费用／信用争议／投诉并非个人律师。34的30日首次联系简写不采用；州时效数字及重启规则未核现法，留地图。 |
| [CA法院债务诉讼](https://selfhelp.courts.ca.gov/debt-lawsuits) | 普通403、8888真200原件52行全文读，35—46主文；已有真实summons／complaint与程序／资源链接，未打开其余子页，不写全州答复日数。 |
| [NYDFS信用消费者](https://www.dfs.ny.gov/credit) | 普通403、8888真200提取373行只实际读231—281；235—244已核销债务substantiation与60日／暂停、诈骗核原债权人。联邦30日firstcontact概括不采用；其余信用／debit旧概括非本文已核。 |
| [NYDFS债务FAQ](https://www.dfs.ny.gov/faqs/industry_faqs/debt) | 普通403、8888真200，71行全文实读，初次截断29—35已补读29—39。引言adopted2014-11-14不是2026新法；原债权人／未default服务等豁免、部分已核销债务60日及待诉／判决安排豁免可用。旧时效重启说法须回现行法后才可能采用。 |
| [WAAG催收](https://www.atg.wa.gov/collection-agencies) | 普通403、8888真200，43行全文读；1—25覆盖／身份／明细／书面停止与争议、费用，37—39执行例外。threecontacts简写不写绝对上限，州RCW另有回应例外。 |
| [WADOL催收执照](https://dol.wa.gov/professional-licenses/collection-agencies) | 普通403、8888真200，64行全文读；许可对象、实际主管与complaint链接，只查到链接未开投诉／lookup子页，不冒称已查真实个人。 |
| [RCW19.16.250](https://app.leg.wa.gov/rcw/default.aspx?cite=19.16.250) | 普通超时、8888真200；提取183行只实际读20—74，书面明细／债权人信息／合理努力／次数回应例外／伪法院文件／时效外起诉。75以后被输出截断且未读，医疗债等不采用。 |

内部依赖本轮真读：credit-records完整76行；finding-help1—40；reading-contracts1—45。均只读，前两部分明确报告纠错／法律帮助准备；banking-payments及语言页尚未本轮开读，不把旧任务记忆冒作此次读取。

## 真失败、壳页面与尚未开读

索引f01—f25多数CFPB／DFPI普通及8888为403、FTC为404；只有上表另由web真主文取得的采用范围算成功，不能把同批其他相邻URL推成已读。RegZ6／7、RegF6／26／42、FTCgetoutdebt／collectionFAQ／FDCPAtext、CFPB331／1403／1411、CA DFPI两入口目前只下载失败或搜索定位，不算主文。

NYCourtHelp旧路径403、猜NYAGcredit-lending404；WA法院目录f35普通DNS失败后8888真200但82行尚未实际读。Texas f36多一层debt-collection猜路径404、旧OCCC域路径404、Harris猜answers404、SOSdebtcollectors403均未核主文。f39Finance392普通200只JS导航壳，实际1—24及原件检索没有392.001／法条，不冒称法条成功；已发现官方392.pdf、SOS2901.pdf及新OCCC域候选，但尚未开读。NYC新催收规则与NYCPLR现行时效也只定位，未核生效不写。

## 10/14优先任务暂停点

主控正式分派B14学校支持独立事实；保存以上真实研究后暂停本作者，无正文、无冻结／自审。恢复时补RegZ缺段、RegF停止联系、四州许可查人和得州真实源，按地图完成行动链再写正文；不重新把40下载算40采用，不采用搜索摘文和没有读到的法条。

## 当前未知与不采用范围

按地图保留个人产品合同条件、催收覆盖与收到／电子争议、四州许可／保证金／豁免、陈旧债务与具体法院程序。未核期限和数字不进入正文。破产、学生／商业／抵押贷款、欠税／抚养和全部跨境规则不展开，只在有实际一级入口时作明确转介。

## 10/14门禁完成后恢复本作者

本人已完成公交第三及学校独立事实并交主控，恢复本作者研究。真正完整重读自己的地图与本证据、查看首轮40请求日志；尚无debt正文。下续研究以本人的实际新读为准，不重置前述失败、截断或未读范围，也不把学校／公交记录当本主题证据。

## 10/14新增实际读取与再次保存断点

- [RegZ1026.18](https://www.consumerfinance.gov/rules-policy/regulations/1026/18/)此次web真201—320，缺口243—303已真正补读；298—315付款次数／金额／频率、首期与一般封闭式非房地产信用，未把房贷披露概括用于本页。仍未全读738行。
- [RegF1006.6](https://www.consumerfinance.gov/rules-policy/regulations/1006/6/)web真143—194、248—365：154—179停止联系、催收人收到才完成、其接受的有效电子方式及三种例外；344—355电子地址退订，不等于停止所有联系。没有称366行全读。
- [RegF1006.26](https://www.consumerfinance.gov/rules-policy/regulations/1006/26/)web63行全文实际读，48—53时效及禁止起诉／威胁、破产proof-of-claim例外；[RegF1006.42](https://www.consumerfinance.gov/rules-policy/regulations/1006/42/)web73行全文读，47—63通知可保存／真实通知与部分电子E-SIGN条件。首个合并输出截断后另真正重开这两件，不把截断算已读。均页面CurrentVersion，普通／8888既有403保留。
- [FTC催收FAQ](https://consumer.ftc.gov/articles/debt-collection-faqs)，March2023，web真167行全文读：43—54停止／核验、89诉讼独立回应、110—141陈旧债务及部分州付款／承认风险、签字结清协议及付款记录。电话次数、扣薪／福利完整细则及私人诉讼金额未采用，须依实际制度另核。普通／8888既有404。
- [TXAG权利](https://www.texasattorneygeneral.gov/consumer-protection/financial-and-insurance-scams/debt-collection-and-relief/your-debt-collection-rights)web真177行全文读，91联系真实债权人、94—126州禁止及州书面争议；不能把州30日答复推为联邦验证统一30日。后normal403／普通8888真200缓存f46仅已取得，尚未另全文读其117行提取件；不混为web读取。
- [TXAG减债](https://www.texasattorneygeneral.gov/consumer-protection/financial-and-insurance-scams/debt-collection-and-relief/debt-relief-and-debt-relief-scams)web真149行全文读，90—116核咨询费用／新贷款总成本／settlement风险，未采用一切前期收费非法的过宽表述。其父页web129行也实际读，只作导航。
- [NYC Civil Court应诉](https://www.nycourts.gov/new-york-city-civil-court/answering-debt-collection-case-nyc-civil-court)web149行全文真读，84—110本人／书面答复及留副本、139帮助、145—148不应诉与寻求撤销缺席判决。126—128混有3年与旧6年／4年、部分付款重启概括，不用于本稿现行时效。20／30日不拟作全州或送达通用算法。普通／8888f45均403。
- [WA法院目录](https://www.courts.wa.gov/court_dir/)f35已真正全文82行读，按县／城市／法院名及翻译／远程入口只作定位，不是本案答复规程。银行页正文14—130此次实际完整读；首个输出截断1—9尚待补读元数据；语言页尚未补读。

具体忽略检查后生成fetch2.py，新f41—f53各html／pdf／txt／json及source-index-2.json均由脚本事前git check-ignore逐路径核对；普通TLS保留。f41CA1788.2、f42DFPI、f45NYC、f53CFPB投诉两途403；f43WA lookup38行、f44WA complaint138、f47OCCC20、f48SOS72、f51CA和解90、f52CA诉状49虽真200，但本次尚未读其主文。f49大写Docs/FI/pdf/FI.392.pdf真200仅text/html导航，与小写web155行壳相同，未取得PDF／法条；f50猜StateLawLibrary子页404。TXSOSdebtcollectors和新occc.state域web不能访问／502，DFPI两原URLweb403；搜索结果仅作正确OCCC域／法院及州主管入口定位，CFPB账单61及FTCgetoutdebt未实际开读，不采用其搜索摘文。

现在按主控正式分派先暂停本作者，转B14职场第三静态；无debt正文／冻结／自审。恢复时继续读新原件和未核采用段，不能以40＋13下载数代替真正读源。

## 10/14最终恢复后的本人实际阅读

root正式接受职场新版第三和死亡新版两审后，恢复debt原作者；本人真全读本地图57行及本证据68行，旧暂停、失败和未读范围保留历史。以下是这次恢复后新实际读到的采用段；不是先前下载时已读，也不是另外两主题的来源继承。

| 本人真实来源与范围 | 版本、采用及未核边界 |
|---|---|
| f43 [WA DOL执照查询说明](https://dol.wa.gov/professional-licenses/look-status-business-or-professional-license)，全38行；f44 [DOL投诉](https://dol.wa.gov/professional-licenses/file-complaint)，全138行 | 原普通403、正常8888 TLS200原件本次真读；按姓名／执照号／类型查有效和到期；投诉交文件、日期及已尝试办法，线上／电邮／邮寄。74—94明确中立调查、结果通知、不能替消费者追回钱／赔偿或作法律裁判；不声称已进入查询后台或查过真人，无页内更新日。 |
| f47 [OCCC投诉分流](https://occc.texas.gov/consumers/file-a-complaint/complaint-portal/)，全20行；f48 [TX SOS其他服务](https://www.sos.state.tx.us/other/index.shtml)，全72行 | 本人已取普通TLS200原件此次真读；OCCC按城市和部分街址查受管非银行消费者贷款机构，没找到仍可报其资料投诉；SOS主文35仅提供Debt Collector Bonds Search。原HTML相关href本人另真读，未进入真实投诉／执照／保证金后台，不由目录推所有人须有保证金、金额或资格，未采用其选举条。 |
| f51现重定向[CA法院诉前协商](https://selfhelp.courts.ca.gov/debt-lawsuits/resolve-before-lawsuit)，全90行；f52现重定向[Summons与Complaint](https://selfhelp.courts.ca.gov/debt-lawsuits/summons-complaint)，全49行 | 普通403／8888 TLS200的本人原件本次全读；采用40—67的州书面停止联系、仍可起诉，f52的42—48付款后须核撤诉、书面协商与法院回应。f51“约一半”及72—79统一四年／重启概括不采用，不当2026现法或个案折扣保证；无页内修订日。f26 CAAG133行及f28 DFS231—281又真实重读，原30日首次联系简写不采用。 |
| [NYC DCWP Check License](https://www.nyc.gov/site/dca/consumers/check-license.page)，web全38行；[催收许可范围](https://www.nyc.gov/site/dca/businesses/license-checklist-debt-collection-agency.page)，web全118行 | 真正0—37及0—117全部显示读；查询无需登录只作入口，15—24主要业务定期收NYC居民个人／家庭债者、部分催收律师与debt buyers；不推广全纽约州或声称全部业务必须许可。101明列SHIELD 2027-01-01生效，仅留地图，不提前套用；许可费用与申请后台虽主文可见，本文不采用。页尾2025版权不当修订日。 |
| [Harris County Justice Court目录](https://www.jp.hctx.net/suits/default.htm)，web全65行；从真实18链接进入[Debt Claim说明](https://www.jp.hctx.net/suits/filingDC.htm)，web全75行 | 目录62—64不提供个人法律意见／有当前性提示；Debt Claim36—61显示债权人类型、借款／账户／转让明细，63—69不及时答辩的缺席判决与债权证明。本文只给该县该法院类别的应诉及查案／表件入口，不采用金额管辖上限、答复天数或推所有得州法院程序；未打开法院表件／查案后台，旧猜/5-1/answers404不冒作恢复。 |
| [RegZ1026.13](https://www.consumerfinance.gov/rules-policy/regulations/1026/13/)，web323行中实际0—241 | 首次87—121输出被截，另真正open100返回37—241完整补读，故截至241无采用缺口，242—322未读。Current regulation，112—137书面异议／接受的电子方式、首次问题账单传送后60日内收件、姓名账户／日期金额原因；147—190收到后30日确认及例外、2个完整账单周期不超90日、争议／非争议付款与自动扣款。200—237更正通知或理由和请求依据；不当银行RegE、催收验证或所有商品质量争议。 |
| [RegZ1026.7](https://www.consumerfinance.gov/rules-policy/regulations/1026/7/)，web find真正390—440、467—519 | 全520行并未通读，441—466输出截断不认已读；采用417—423仅付最低的时间／成本警告和不再新增余额的估算假设，491—501可见例外。本文让读者读自己的账单，不承诺所有账单都有36月例子，也不采用催收次数或统一最低付款比例。 |
| [RegF1006.38](https://www.consumerfinance.gov/rules-policy/regulations/1006/38/)本次web全116行重读 | Current regulation；49—58书面／其接受的电子地址，85—106“在验证期内递交的书面请求／争议”收到后暂停到规定核验或重复争议回应。不把规则改成消费者一定须在期内送达，不写催收人统一30日答复。原普通403未变；原件本次未重新下载。 |
| [CFPB投诉](https://www.consumerfinance.gov/complaint/)，web全161行；[联系](https://www.consumerfinance.gov/about-us/contact-us/)，web全124行 | 分别page modified2026-10-05／10-01；产品、关键日期／金额／联系／证据、代办授权、转公司或主管、跟进答复；联系31—37的855-411-2372及TTY855-729-2372。未进入门户，未采用15／60日为诉讼暂停或保证解决，未从contact推全部电话有免费中文口译；投诉f53普通／8888 403保持，不混为本地200。 |
| [FTC How To Get Out of Debt](https://consumer.ftc.gov/articles/how-get-out-debt)，web全224行，页内December2025 | 15—26预算／早协商及部分州旧债风险；47—108书面安排、咨询不因nonprofit即免费、管理计划与settlement分开；134—150停付加费／信用／仍会起诉／不能保证减债。42—44学生贷款实际servicer分流、160—180破产转介只作地图方向，不采用其完整破产门槛／税公式／时效或“所有前收费违法”概括；准确历史删除期限不扩成本稿的新规则。 |

本轮真实失败：DFPI新how-to-get-help web403，原lookup／CIV1788.2各普通及8888 403仍保持；TX SOS原debtcollectors web不可访问，正文若给查询只采用真读other目录；CFPB猜en61路径web不可访问，没有读账单消费者FAQ，不继承搜索摘文。首次四查询合批搜索结果有截断且有非一级项，只用可见的主管URL定位，不把搜索当实读。以上新web没有新增下载，既有f43—52原件具体忽略检查记录在前节。

内部本次真补银行页1—13元数据，至此原正文14—130与元数据读取缺口完成，仍不核其全部外源；语言页service-conversations1—70真读，采用46—52请求具体语言和核机构安排，不声称已全读该页或全国免费口译。其余依赖仍按前节真实范围，只读不改。

## 10/14成稿前后的最后核对

本人已完整读初稿111行，随后按既有真实采用段改用共同签署者而不外推所有保证人；贷款办理费、社会安全号码及四州主管名称就近释义。重新真读本人已取得的f28原件230—282及f29全71行，只是原件复读，不冒称再次HTTP回源；纽约表按240—244及FAQ3—11、18—25明确charged-off含义、收到适用请求后暂停／60日提供、原债权人／非违约服务及法院事项例外。未采用该页30日first contact或旧时效重启概括。

语言页service-conversations71—125现已全部真读，结合此前1—70此次全文完成；采用80—93查账单／核等待期间付款和正式渠道、101—125跟进并保留确认。本人另实际读五个内部目标当前元数据与标题，全部integrated／draft false；只作现有内容承接，不继承其全部外源或重新作事实审。

最后逐链接检查曾发现正文WA法院目录有已读记录但证据未写URL，现仅为真实既有f35记录补入官方URL；没有新增源读取。教学虚构算例用算术独立核3000−300＝2700、24×150＝3600、36×110＝3960、150−110＝40及3960−3600＝360，不计算或虚构真实产品APR。

## 10/14作者中间全文读取与摘要（已由末节替代）

正文最终111行／21915bytes已本人实际分1—55／56—111全读，含元数据、三表与所有引注。最终补CFPB中文机构名及两地法院中文类别，URL、数值与来源采用范围未增加；银行扣款／信用记录／合同／法援／语言五个正式目标均只读，7个绝对链接有效。原件及web的全读／部分、版本与真实失败逐件见上文，39不同正文一级URL仅采用已记明主文段，不把53请求或HTTP状态当全读。此主题没有采用真PDF主文；TX假PDF的HTML壳失败保留。

中间正文SHA-256为`a70875181ee469809118c5080fa5d4e3463fa70e000e44f2adba6dddb36cf1e8`，严格UTF-8 `full.split('---',2)[2]`保留首尾换行；中间整文件SHA-256为`0ab83b7f7a1727011455faaab0066eaadbd98e818199876dd3690104e753c869`。written／draft true，verified和reviewed_by均为空；以下末节最终法律文字校准已替代此摘要，不以它送审。

格式与算例检查：8H2／0H1、3个两列表、18处加粗外侧空白、64普通链接（57外链／39URL；7内链／5目标），所有正文外链都有本人实际范围的证据入口。未执行共享构建、提交、元数据安装、真实开户／借款／查询／投诉或联系机构。完成本记录后作者实际全文读回最终地图、证据，再重新实算四摘要交root；独立FACT和第三审须另派，作者不预判通过。

## 10/14法律文字最后校准与最终送审冻结

本人最后又真web打开[当前RegF1006.34](https://www.consumerfinance.gov/rules-policy/regulations/1006/34/)采用段，实际返回0—254全部读（共365行，255—364仍未读，不称整法全读）；41标This version is the current regulation。69—72的(b)(2)排除正式民事诉状作为初次催收联系；115—123的(b)(5)验证期起于提供信息，止于收到或法定推定收到后30天，通知可按推定日列截止，须核通知和送达记录。前述旧0—252记录不增加其当时已读范围；此次是实际再次回源，未新下载或把普通403改称200。

因此只替换正文L67一个完整段落，将原“验证期从收到起算／诉状不是验证通知”按上项精确表述；其他正文、元数据及64链接顺序不动。内存逆换该唯一段精确恢复中间body`a70875181ee469809118c5080fa5d4e3463fa70e000e44f2adba6dddb36cf1e8`／whole`0ab83b7f7a1727011455faaab0066eaadbd98e818199876dd3690104e753c869`，中间版本未报异人审。最终111行／21972bytes已本人再次分1—55／56—111全部实际读回。

当前最终正文SHA-256：`4aa3f76757320f1f00023c73c3c92eb9544cfdf2a05ba8dab4406a2882f15e3f`（UTF-8 `full.split('---',2)[2]`，不裁首尾换行）；整文件SHA-256：`7a16f07bc8edd4967e139f79d8e4d9bf6d1fb788292b297c77abc4e02ad42734`。written／draft true／verified与reviewed_by空。最后实际完整读回两包、重新实算四摘要后交root正式安排异人事实与第三，作者记录不是独立PASS；既有失败、部分／未读、复杂案件和后台边界保持。
