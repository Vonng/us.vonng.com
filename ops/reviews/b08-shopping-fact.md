# B08 日常购物与退货：独立事实审

2026-10-13，`root` 独立事实审， **最终事实审 PASS** ，仅绑定正文 SHA-256 `b8541cd63e9eab39a42b8d26a2a1803e45121cb4affc91c3ab789d1a9355631f`、整文件 SHA-256 `88660e08ea83d3c90a0aafc2bb3d411d9b085b9189b885ed9cb675702b98b8f1`。作者为 `birth_fact`，第三人静态审由 `static_editor`另行实际进行，三名不同参与者。本人只写本审阅记录，不代改作者正文或证据；以下初稿断点保留历史，不承载最终PASS。

## 初始送审版本（历史）

- 正文：`content/book/life/household/shopping-returns.md`；已完整实际读105行，包括所有表格与引注。
- 当前待审正文 SHA-256：`f37769cce6dcd94c287b1e1bb97b68c11f03da5334186b979f911b8ff07761be`。
- 当前整文件 SHA-256：`b6bfc4225b74a011a2852a77fabe405850dd004063162be4b0b2c56f3937dba4`。
- 摘要算法：UTF-8完整文本 `split('---', 2)[2]`，保留分隔符后的换行。
- 已完整实读作者地图26行、作者证据60行；两者不是本审阅者的新回源证据。作者的原源读取和失败须与我的本轮独立取源区别记录。
- 新稿当前字段为 written、draft true、verified与reviewed_by空；B07合同依赖现已正式集成。
- 独立核验重点：FDA营养／过敏原／配方奶日期；CA当前食品标签、报价及退款展示例外；NY现行退货与信用卡价；FTC完整订单、发货／延期／退款动作期限；RegZ账单错误与其他争议的范围、通知送达、时钟及调查；四州计量与消费主管、权限及电话。
- 已实际确认 `.cache/evidence/b08-shopping-fact/` 具体拟用索引、HTML及XML路径被Git忽略；该目录仅保存我本轮独立取源原件与文本。实际读到的采用段、访问失败、作者返修与最终结论将在下方补全。本记录尚不声称任何一级来源已读或事实审通过。

## 2026-10-13 本轮独立取源与实读

本人从冻结正文实际提取30个不同HTTPS引用，独立发起普通TLS请求；原件、HTTP／转址／二进制摘要及抽取文本只在本人的忽略目录。没有打开作者缓存作为本次一级证据。下表缓存号对应 `.cache/evidence/b08-shopping-fact/sources.json`；行号来自本人的新抽取文字，标为网页工具的位置来自本轮真正打开的原主文。200只证明取得材料，表中实际采用段均另开读；403挑战、FDA404错误和eCFR的200 Request Access不计成功。

| 号 | 一级来源与本轮实际阅读 | 对照结论与范围 |
|---|---|---|
| 01 | [NIST单位价格](https://www.nist.gov/programs-projects/uniform-unit-pricing-tools-consumers-fight-shrinkflation)，TLS200，176行完整读；updated2025-09-15 | 25—33、49—52支持按同单位比较／自行算价；没有把模型最佳实践写为全国强制义务。教学两例在本人内存重算分别0.50、0.40美元／100克，非真实商家报价。 |
| 02 | [NIST SP1181e2025 HTML](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/1181e2025/NIST.SP.1181e2025.html)，TLS200；1—107、752—830实际读，批准2025-06-23 | 摘要与Section3支持同产品类别同单位；未读完整1578行／未下载其PDF，不采用商家所有法定展示义务。 |
| 03 | [FTC Online Shopping](https://consumer.ftc.gov/articles/online-shopping)，普通403；网页工具真正打开并完整读2—68、84日期May2023 | 优惠条件、全部费用、退货条件及记录支持。它将defective和billing error概括并列，本稿以专门指南／RegZ精确区分；没有按此概括扩大质量争议。 |
| 04 | [FDA Nutrition Facts](https://www.fda.gov/food/nutrition-facts-label/how-understand-and-use-nutrition-facts-label)，普通404错误；网页工具实际77—237主文 | 92—94每份／多份、139—141添加糖包含、160—181 %DV5%／20%及同每份量、226—228双列支持；未采用临床热量、疾病或个体饮食建议。 |
| 05 | [FDA Food Allergies](https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/food-allergies)，普通404；网页工具65—114实际完整采用段 | 九类、FDA管辖范围、配料／Contains、现场按订单包装与自愿May contain支持。没有把未标警示视为无交叉接触，也不采用临床阈值／急救方案。 |
| 06 | [FDA食品日期与储存](https://www.fda.gov/food/consumers/how-cut-food-waste-and-maintain-food-safety)，普通404；网页工具85—113实际读 | Best if Used By质量含义、向厂家询问和不买超用量支持；储存时长／温度等本稿未写，未把全国一般说明覆盖CA现行安全标签。 |
| 07 | [CDFA Food Date Labeling](https://www.cdfa.ca.gov/is/foodrecovery/fooddatelabeling/)，TLS200；网页工具49—76实际读 | 质量／安全完整字样、2026-07-01消费者Sell by限制、鸡蛋／婴儿配方奶例外支持。AB660导航与拟用HSC原法网页本轮均403；只对主管说明能支持的适用标签结论判断，没有核全部制造日、旧库存或每类产品法定日期义务。 |
| 08 | [FDA Infant Formula](https://www.fda.gov/consumers/consumer-updates/infant-formula-safety-dos-and-donts)，普通404；网页工具74—103实读，采用87—88 | Use By过期不喂、包装储存／开封说明支持；不新增配制时间、喂养建议或产品推荐。 |
| 09 | [CA OAG Hidden Fees](https://oag.ca.gov/hiddenfees)，TLS200；78行完整读 | 3—17、22—44支持2024-07-01全额价、税／实际合理运费、handling、可避免卡费与必付卡费、SB1524特定食品例外；没有推出所有食品或各州统一比例。 |
| 10 | [NY GBL518现行主文](https://www.nysenate.gov/legislation/laws/GBS/518)，普通403；网页工具55—77全文及46版本2024-02-16实际读 | 含附加费总价、实际卡费上限和双价支持；不采用罚款金额，未推广到借记卡／其他州。 |
| 11 | [NY信用卡附加费一页指南](https://dos.ny.gov/credit-card-surcharge-guidance)，TLS200转官方PDF | 真PDF219551字节，SHA `9582703bf5fb8d0d204d69f285e704ee6e8ccc0a98cb1c15902c6b02f9e0ddeb`；本人pypdf实际完整读物理1页，并pdftoppm转图后实际查看整页。文字提示缺fontTools，页面像素和文字都可读；税前最高总价／双价／现金折扣及违法百分比／收据单列例子支持，生效2024-02-11与页脚1/24分开。 |
| 12 | [TDA Scanners](https://texasagriculture.gov/Regulatory-Programs/Weights-and-Measures/Scanners)，TLS200 | 首次抽main只有三行非主文；本人重新抽实际body并读132—154，144支持错误价改成最低价，不写自动赔偿／免费商品。 |
| 13 | [WA Store Refunds](https://www.atg.wa.gov/store-refunds-exchanges)，TLS200，14行完整读 | 普通非缺陷／非误导商品按policy、凭据包装、邮寄和期限支持；不推广特定冷静期。 |
| 14 | [CA Refund Policies](https://oag.ca.gov/consumers/general/refunds)，TLS200，38行完整读 | 7—15支持7日全额refund或credit／等额换货、不展示的30日凭据及列举例外；9—11保修另路。须返作者把credit明确写全额，见下节；未冒称读到1723原法。 |
| 15 | [NY GBL218-a现行原文](https://www.nysenate.gov/legislation/laws/GBS/218-A)，普通403；网页工具52—91全文及42版本2025-08-08实际读 | 实体与online展示、政策副本／费用及违规定条件30日cash或credit选项支持，unused／undamaged／验证日期保留；没有给普通购买无条件30日退款。 |
| 16 | [TX州法律图书馆退款FAQ](https://sll.texas.gov/faqs/refunds-returns/)，普通403；网页工具21—26、39更新时间2025-08-26实读 | 普通按合同／商家政策、不用统一三日取消支持；该馆未找到不推为全部特定交易的绝对法结论，私人律师摘文不作新一级来源。 |
| 17 | [eCFR16CFR435当前规则](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-435)，普通200转Request Access不采用；网页工具69版本截至2026-10-08，116—223全部主文实际读 | 完整订单／30与卖方新信贷50日、承运人发货、首次不超过30日延期的合规默示同意、取消／排除项支持。7工作日／卖方creditor一周期是(b)，退款动作是(d)，须修引注标签；实际到账非该动作期限。 |
| 18 | [FTC未到货与账单](https://consumer.ftc.gov/articles/what-do-if-youre-billed-things-you-never-got-or-you-get-unordered-products)，普通403；网页工具2—53全部及69日期August2022实读 | 全额退款不是强制礼卡、未接受／未按约送达与已接受质量区别，60日／30日／两周期≤90、无争议支付、未来交付与debit不同支持。图表像素未读，不采用图表独有细节或误投包裹推断。 |
| 19 | [CFPB购买退款问答](https://www.consumerfinance.gov/ask-cfpb/how-can-i-get-a-refund-on-a-product-or-service-i-purchased-with-my-credit-card-en-1969/)，TLS200，42行完整读 | reviewed2024-05-15／modified2024-09-06；联系商家／发卡争议的继续路径支持。另路$50／100英里／未付余额未套入billing-error，非发卡BNPL也未混用。 |
| 20 | [CFPB RegZ§1026.13当前原文及解释](https://www.consumerfinance.gov/rules-policy/regulations/1026/13/)，TLS200；1—162实际逐段读 | a(3)/(4)、b原文和解释、c、d(1)完整支持不同账单错误、指定地址60日送达／漏credit起算、指定电子方式、无需等商家、30日确认／完整两周期≤90与暂不付争议额。自动扣款解释亦读但本稿未写详细程序；未将后续e—g或所有抗辩程序冒称全文审阅。 |
| 21 | [CFPB信用卡争议](https://www.consumerfinance.gov/ask-cfpb/how-do-i-dispute-a-charge-on-my-credit-card-bill-en-61/)，TLS200，34行完整读 | reviewed2024-04-15；已付也能争议、书面结果与质量另路支持。通知的精确收到／发送时钟采用20号法文，非一般问答的口语时间。 |
| 22 | [CDFA Quantity Control](https://www.cdfa.ca.gov/dms/programs/qc/qc.html)，TLS200，13行完整读 | 实际县计量部门执行与投诉入口支持；未读消费者PDF或县个案。 |
| 23 | [CA消费者投诉入口](https://oag.ca.gov/contact/consumer-complaint-against-business-or-company)，TLS200，1—96、590—689实际读 | 中文入口、附件遮敏、不能私人代理／可转主管支持；未读中间所有表项或填写提交，不称个人获退款。 |
| 24 | [NY计量主管](https://agriculture.ny.gov/weights-measures)，TLS200，39行完整读 | 包装／秤与县市主管入口支持，未核所有单位价强制法。 |
| 25 | [NY DCP投诉](https://dos.ny.gov/file-consumer-complaint)，TLS200，39行完整读 | 先商家、自愿／不能强制、已法律行动不处理、中文表和8006971220支持；没有下载中文附件或提交。 |
| 26 | [WA WSDA计量](https://agr.wa.gov/services/inspections-and-investigations/inspections/weights-and-measures)，TLS200，113行完整读 | 65—68、89—95真实部门3609022035；未把页头一般3609021800误用为计量投诉电话。 |
| 27 | [WA AGO投诉](https://www.atg.wa.gov/file-complaint)，TLS200，56行完整读 | WA居民／WA企业、非正式／无法强制、法院继续及记录支持；不把商家回复请求期当消费者期限延长。 |
| 28 | [TDA计量投诉](https://texasagriculture.gov/Regulatory-Programs/Weights-and-Measures/Weights-and-Measures-Complaint-Process)，TLS200；首次空main三行，经本人重新抽body，123—139完整主文实际读 | 5124637698、店名地址／事实、调查与执法支持，罚款归州不等个人获赔。 |
| 29 | [TX OAG投诉](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint)，TLS200，63—117实际读 | 公开材料／敏感信息、完整事实、confirmation不是立案、一般消费范围支持；不保证个人代理／催款。 |
| 30 | [CFPB金融投诉](https://www.consumerfinance.gov/complaint/)，TLS200，1—125实际读 | 发卡／银行等金融产品、非金融分流、日期金额／附件与跟踪支持；15／60日一般回应或其余政治／保留年限旁支不写入、不替代RegZ时钟。 |

## 精确返作者要求（已完成，保留历史）

已向原作者birth_fact交两项最小修订，本人不代改正文：

1. CA退货表中“全额退款、额度、等额换货”，须把credit也明确写为全额，例如“全额退款、全额商店额度、等额换货”，避免部分额度被读成满足7日分支；14号实际采用13行支持。
2. 退款期限引注现为“§435.1(d)：退款动作与期限”，应标“§435.1(b)、(d)：退款动作与期限”；期限定义在(b)，动作在(d)，17号本轮实际原文支持。URL和其他正文不必改。

作者须重读其采用资料、只在自己三文件修订并提交新完整正文／整文件SHA，保持draft／空核验字段。本人待新冻结版本再次完整核读并独立复算，旧f37769cc摘要不提前给PASS。未核边界仍为食品临床／储存或召回个案、所有单位价法、旧库存／全法特例、其他付款／质量完整抗辩、平台保证及真实银行到账／机构处理结果；已写的具体断言仅按上表实读范围判断。

## 2026-10-13 最终冻结稿实读与结论

08:08—08:10 UTC，收到原作者的两处最小修订后，本人再次完整实际读最终正文105行，包括frontmatter、每段和两表；实际读作者新增map／evidence返修记录。本人按UTF-8完整文本独立计算正文 `split('---', 2)[2]` 摘要和整文件摘要，分别为顶部最终值。当前status written、draft true、verified和reviewed_by均空。没有安装集成元数据。

本人只在内存逆向撤回“全额商店额度”和新增(b)引注两处，均恰出现一次；计算恰恢复初送审全文正文 `f37769cce6dcd94c287b1e1bb97b68c11f03da5334186b979f911b8ff07761be`、整文件 `b6bfc4225b74a011a2852a77fabe405850dd004063162be4b0b2c56f3937dba4`。故frontmatter、其他正文／URL／金额期限／例外不变，两处改字符合本人上表实际读取的CA主管和当前eCFR。作者自己的新增回源与我的独立回源分别记载，没有互相继承。

最终整条购买→标签／总价／政策→收据与货物→普通退货／缺陷→迟发与取消→退款动作及实际入账→合格账单错误通知与调查→主管分流／法律继续→核实际结果均已完整核读。具体食品日期、四州退货／费用与主管、发货30／50、首次短延期条件、退款7工作日／自营信用一周期、通知60日送达／漏贷记起点、确认30日／两个完整周期最多90日均有上表本人真正读到的一级采用段。CA主管说明与未能打开的完整原法范围分开；一般FDA质量说明未覆盖CA安全日期。已接受质量、借记卡、BNPL、到账、政府投诉与个案结果均未混同为同一法定时钟或保证。

**最终结论：事实审 PASS。** 无其他事实返修项；本结论仅绑定最终完整正文SHA和上表采用范围，不追认旧摘要通过。仍保留前述未核边界与来源渠道失败，不声称全部食品法、平台政策、全部贷款争议／个体退款已核。可交static_editor第三人完整静态审；正文作者birth_fact／事实root／第三static_editor须为三名不同参与者。第三静态、候选元数据、隔离生产、实际桌面／手机／打印与public同步尚未完成，本事实PASS不代替这些门禁。
