# 日常购物与退货：作者研究记录

2026-10-13，B08 作者 `birth_fact`。开工先建立地图，再实际读取一级来源；现已写成完整正文并完成作者自读。仅作者正文、同 slug map／evidence 属本次所有权；共享文件、构建与提交由 root 负责。本文是作者研究记录，不是独立事实审通过结论。

当前完整正文 SHA-256：`b8541cd63e9eab39a42b8d26a2a1803e45121cb4affc91c3ab789d1a9355631f`；整文件 SHA-256：`88660e08ea83d3c90a0aafc2bb3d411d9b085b9189b885ed9cb675702b98b8f1`。算法为UTF-8全文 `split('---', 2)[2]`，保留起始换行。原作者／本轮返修者birth_fact；独立事实审root、拟第三静态static_editor。written／draft true／verified空／reviewed_by空未改，待root绑定最终全文复核。

## 本轮已经实际读取的一级来源

以下阅读均发生于 2026-10-13；采纳范围以当前完整稿及末尾冻结摘要为准。普通 HTTPS 抽取行号来自本人的新取源文本，网页工具行号来自实际返回的主文。没有把仅标题／状态或作者之外的缓存计为已读。实际新取源索引留在已确认忽略的 `.cache/evidence/shopping-returns/source-index.json`；失败条目的challenge／错误页不计主文，网页工具实读则按本表记录。

| 来源、版本与实际读段 | 可采用事实及边界 |
|---|---|
| [NIST 单位价格消费者工具](https://www.nist.gov/programs-projects/uniform-unit-pricing-tools-consumers-fight-shrinkflation)，普通 HTTPS200 全主文19—156行；updated2025-09-15 | unit price 是每一计量单位的价格；可按净含量自行算，线下／网购都可比较。NIST 的最佳实践／模型规则不能直接当全国所有店必须标单位价。州数量、调查比例、立法提案不采用 |
| [NIST SP1181e2025 HTML](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/1181e2025/NIST.SP.1181e2025.html)，普通HTTPS200；版本审批2025-06-23，实际读Publication History／Executive Summary及Section3的754—828行 | 同产品类别用同一计量单位比较；包装数量、重量／容量／数量与组合声明的区别。未下载PDF；未把最佳实践的店方建议写成全国强制法 |
| [FDA Nutrition Facts](https://www.fda.gov/food/nutrition-facts-label/how-understand-and-use-nutrition-facts-label)，web77—237行完整；无本文采用版次 | serving size、servings per container、每份营养和热量、双列、%DV每份5%或以下低／20%或以上高、Added Sugars已经计入Total Sugars。未采用各类疾病风险／个人热量目标或临床营养建议。普通HTTPS同URL404，web实读成功 |
| [FDA Food Allergies](https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/food-allergies)，web65—134行；顶部2025-01指导更新、2026-02公开会议并非个人治疗依据 | 九大主要过敏原；配料名／括号或Contains两种标法；may contain等属自愿，现点现包的餐食不适用相同要求；FDA管辖与肉禽蛋、酒、原农产品、高精炼油等边界及非九类物质另看Ingredients。未写阈值、患者诊断或急救操作。普通HTTPS404，web成功 |
| [FDA 食品浪费与安全](https://www.fda.gov/food/consumers/how-cut-food-waste-and-maintain-food-safety)，web85—118行完整；无采用版次 | Best if Used By是质量标记，储存／包装说明与日期一起看；实际买能用完的数量。州新法见下行，未将全国一般说明当加州2026规则；未采用苹果储存时长、疾病统计或个人安全判断 |
| [FDA Infant Formula Safety](https://www.fda.gov/consumers/consumer-updates/infant-formula-safety-dos-and-donts)，web74—103行；实际采用87—88 | 婴儿配方奶Use By之后不喂给婴儿；保存和开封指示在包装上。未采用配制时数、临床喂养或产品推荐 |
| [CDFA 日期标签](https://www.cdfa.ca.gov/is/foodrecovery/fooddatelabeling/)，web49—76及普通HTTPS200完整主文 | 2026-07-01起相关标签区分质量与安全、禁止消费者可见Sell by，鸡蛋／婴儿配方奶例外。BEST if Used by与USE by两项含义已实读。未从页面推断每种食品必须有日期；AB660原文访问失败的边界如下 |
| [FTC Online Shopping](https://consumer.ftc.gov/articles/online-shopping)，web2—68完整；May2023 | 比较总价／运费／处理费／税等、促销条件、退货费用／期限及记录。该页将defective商品与账单争议并写；正文按下行专门指南及RegZ分清质量争议。普通HTTPS403 |
| [FTC 未到货／账单](https://consumer.ftc.gov/articles/what-do-if-youre-billed-things-you-never-got-or-you-get-unordered-products)，web2—53完整；August2022 | 发货承诺、取消及全额退款，信用卡账单错误与已接受商品质量争议分开；书面60日／收信30日／两完整周期最多90日、无争议款继续付、借记卡不同、未来到货超60日时机构可能另给保护。原文未订购商品段已读，但正文不扩展误投包裹／试用订阅。普通HTTPS403 |
| [eCFR 16CFR435](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-435)，web标题版本69行、§435.1全部及§435.2／3全部116—226行；title16截至2026-10-08 | 完整订单定义、30日及向卖方新申请信贷的50日例外、实际交承运人算发货、首次短延期可默示同意／再次延期、取消和退款动作、大多数付款7工作日与卖方自己信贷1周期、种子／生长植物／COD及其他排除。普通HTTPS虽200却是Request Access页，未计法条成功 |
| [CFPB 信用卡争议](https://www.consumerfinance.gov/ask-cfpb/how-do-i-dispute-a-charge-on-my-credit-card-bill-en-61/)，普通HTTPS200全部问答1—16行；reviewed2024-04-15 | 及时联系、书面60日、保存资料、已付款可争议、决定书面说明；质量缺陷可能用不同程序 |
| [CFPB 购买退款](https://www.consumerfinance.gov/ask-cfpb/how-can-i-get-a-refund-on-a-product-or-service-i-purchased-with-my-credit-card-en-1969/)，普通HTTPS200问答1—25行；reviewed2024-05-15、modified2024-09-06 | 商家处理／发卡争议与账单错误的区别。后半段$50／100英里／未付余额属于另一路 claims and defenses，不套到未到货的billing-error程序，正文不写这些金额距离条件；非发卡BNPL也不混写 |
| [CFPB RegZ§1026.13](https://www.consumerfinance.gov/rules-policy/regulations/1026/13/)，普通HTTPS200；标为current。实际读a／b／c及相关官方解释，d(1)原文；抽取1—148行 | 未接受／未按约送达、错误贷记、通知须送达指定地址，60日从首错账单发送起，漏记credit从应显示贷记账单发送起；电子书面方式仅在机构billing-rights声明指定时成立；无需先等商家答复；30日确认、两完整周期≤90日；调查期争议额相关费用与无争议账款分别处理。未采用尚未完整读取的d后续／e—g细则或自动扣款3工作日规则 |
| [CA OAG退货政策](https://oag.ca.gov/consumers/general/refunds)，普通HTTPS200全部主文7—18行 | receipt7日全额退款／credit／等额换货等选择不足时须显著展示限制；未依法展示时购后30日有凭据全额退；生鲜、标注final sale、使用／损坏、定制、缺原包装、卫生原因等例外。缺陷另看warranty；原法1723本轮403，未声称读到法条 |
| [CA OAG SB478 FAQ](https://oag.ca.gov/hiddenfees)，普通HTTPS200主文1—18、17—59及其余正文曾读到；生效2024-07-01、SB1524例外 | 适用个人商品／服务全额价格含强制费用，政府税费／合理实寄运费可另列、handling须含；可避免的信用卡费与只有信用卡可付不同；餐厅／酒吧／杂货店单项食品饮料等例外须按要求显著显示。未扩大到所有食品与所有交易、未给信用卡费统一比例 |
| [NY GBL218-a现行法](https://www.nysenate.gov/legislation/laws/GBS/218-A)，web52—91全部；most recent revision2025-08-08 | 实体及online retailer展示方式、退款形式／时间／无凭据／折扣货／费用披露及索取书面政策；违反规定时30日、未被买方使用损坏、凭据验证，cash／credit由买方选。普通HTTPS403。DCP一般页的简述不足以消掉这些条件 |
| [NY Refunds/Rebates/Rainchecks](https://dos.ny.gov/refunds-rebates-and-rainchecks)，web50—65及普通HTTPS200完整主文；无明确采用日期 | 普通policy事先看、索取书面、退货费用及地方保护；具体30日恢复条件以已实际读到的GBL218-a为准。未采用返利与raincheck等旁支 |
| [NY GBL518](https://www.nysenate.gov/legislation/laws/GBS/518)，web55—77全部；most recent revision2024-02-16 | 信用卡含附加费总价显著展示、费不超卡公司向商家收取的费用、可双价。罚金及地方执法条款已读但正文不列500美元等无关金额 |
| [NY信用卡附加费一页指南](https://dos.ny.gov/credit-card-surcharge-guidance)，普通HTTPS200实际下载后pypdf完整读1页；实际转址2024/04/2024-04-10…PDF，页脚1/24，内容生效2024-02-11 | 信用卡／现金双价或高总价加现金折扣，单贴百分比或只在收据另加不足。二进制SHA `9582703bf5fb8d0d204d69f285e704ee6e8ccc0a98cb1c15902c6b02f9e0ddeb`。初次误把该PDF当HTML的乱码不算阅读，纠正下载解析后才采用 |
| [WA退款换货](https://www.atg.wa.gov/store-refunds-exchanges)，普通HTTPS200主文3—16全读 | 普通非缺陷／未误导商品看商家policy，保存包装价签凭据、gift receipt、折扣货期限及运费；特殊电话／上门取消另看合同页 |
| [TX州法律图书馆退款FAQ](https://sll.texas.gov/faqs/refunds-returns/)，web21—26全读及39更新时间2025-08-26 | 不存在该馆所知的统一3日购物取消，通常看合同与店方政策，未发现州统一展示要求。不把该馆“未找到”写成对全部特定交易的绝对法律结论；引用的私人律师文章未回源、不采用 |
| [CDFA Quantity Control](https://www.cdfa.ca.gov/dms/programs/qc/qc.html)，普通HTTPS200完整主文及链接 | 核净含量、付款价与包装；由县weights and measures执法，投诉向相应县。Consumer旧猜路径200错误页不采用；未实际下载消费者PDF或查询县个案 |
| [NY Weights and Measures](https://agriculture.ny.gov/weights-measures)，普通HTTPS200完整核心页及地方目录链接 | 称重／包装核查及县市部门投诉入口；未把此页当个人已经调解成功，未采用单位价强制条文 |
| [WA WSDA计量](https://agr.wa.gov/services/inspections-and-investigations/inspections/weights-and-measures)，普通HTTPS200 What We Do及Questions主文 | 核价／秤／包装与投诉，当前电话360-902-2035，邮箱wtsmeasures@agr.wa.gov。未采用设备旧页360-902-1822，不用许可标签推断店方价格正确 |
| [TX TDA Scanners](https://texasagriculture.gov/Regulatory-Programs/Weights-and-Measures/Scanners)，普通HTTPS200134—154行全部；无明确版次 | scanner店方负责价格，错误价须改以最低价收费；未写虚构自动赔款或免费商品规则 |
| [TX TDA计量投诉](https://texasagriculture.gov/Regulatory-Programs/Weights-and-Measures/Weights-and-Measures-Complaint-Process)，普通HTTPS200123—139行全部 | 误价、秤、包装投诉；512-463-7698，需店名地址与事实，调查与执法范围。罚款是州款，不自动变个人退款；未联系主管 |
| [NY DCP投诉](https://dos.ny.gov/file-consumer-complaint)，普通HTTPS200全部主文1—39 | 先向商家解决，DCP自愿调解不能强制；已进入诉讼／法律行动的不受理，中文表格链接及8006971220。未下载中文附件或提交表单 |
| [CA OAG投诉表](https://oag.ca.gov/contact/consumer-complaint-against-business-or-company)，普通HTTPS200公开表头1—95及591—684尾段 | 中文资料链接、附件敏感信息遮盖、AG不能当私人律师／可转主管；没有填入个人信息、点击提交或用本页推断返款承诺 |
| [WA AGO投诉](https://www.atg.wa.gov/file-complaint)，普通HTTPS200全部主文3—71 | WA居民／对WA企业投诉、非正式解决、拒答时不能强制、可继续法院、case number跟进；不把部门请求商家30日回复当消费者诉讼或银行争议延期 |
| [TX OAG投诉](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint)，普通HTTPS20063—118行实际全部读取 | 店名地址／日期金额／联系材料、普通虚假商业／退款等投诉；公开记录、不得含敏感账号等、confirmation留存，caseid不等调查，主要收集市场线索。未写个人代理／催退款保证 |
| [CFPB金融投诉](https://www.consumerfinance.gov/complaint/)，普通HTTPS2001—105行主文实际读 | 发卡／银行等金融产品受理，普通商家购买分流、日期金额与材料、取得回应和跟踪。未采用一般15日／60日回应周期替代RegZ期限，未采用debanking政治评述／保留25年等旁支 |

## 访问差异、冲突与未核边界

- 保存前实际 `git check-ignore` 已确认 `.cache/evidence/shopping-returns/source-index.json`、notes.txt、拟用unit-pricing.pdf均忽略；另在下载前确认ny-credit-card-guide.pdf忽略。只下载NY这一页指南，其余原文经正常HTTPS文本或web读取；未改忽略规则或安装依赖。pypdf提示缺fontTools但一页文字完整可读，未把字体警告当来源失败，也未改共享环境。
- FDA两基本HTML普通404，web实际返回正确主文；FTC普通403，web实际成功；eCFR普通200 Request Access不算法条读取，web当前主文成功。NY法条普通403但web成功。均如实区分渠道，没有关闭TLS／绕验证码／登录或联系机构。
- USDA/FSIS Food Product Dating：网页工具搜索曾返回官方整篇原文，包含日期字样、infant formula及储存段，确实读过；直接web打开（含普通尾斜杠）、普通HTTPS及普通8888代理均403。2019-0022指南页web403；askFSIS婴儿食品页timeout，猜测SellBy FAQ路径不可访问。最终正文优先FDA可实际打开主文及CDFA2026当前页；不把搜索摘要或2019全国一般Use-By解释替代当前州安全日期含义。
- CA1723法条普通HTTPS与web403。AB660导航／正文页web与普通HTTPS403；CDFA当前公开说明经两个渠道200并实际读到质量／安全、日期与例外。只采用该说明能支撑的标签含义，不推断原法全部制造日期／旧库存／产品特例，也不称每项食品必须有日期。
- NY DCP一般页面把未展示policy的30日权益写得简略，并说普通退款形式不统一；GBL218-a现行原文明确违法展示时未使用／未损坏／可验证购买日期的cash或credit选择权，最终按原文条件表述，不能混成所有购物无条件30日退款。2025修订明确online retailer也受展示要求，旧页不能消掉这一分支。
- CA SB478一般全额价格FAQ同时列SB1524对餐饮／杂货店食品等的例外；最终必须保留这些范围，不将普通日用品总价规则无条件套食品菜单。NY信用卡费规则不推广到银行卡或其他州；TX信用卡收费诉讼／禁令效力未完成核验，不给其统一禁令结论。
- 未核各州完整单位价义务／店面积和品类例外、所有税费／card network附加费上限、商业或跨境买卖、COD等排除交易详细退款、商品质量的完整warranty／claims-and-defenses诉讼、BNPL、个别平台保证和真实送达风险分配。SNAP/WIC等福利资格、个人营养／过敏诊疗、完整食品储存时数与召回个案另留专题，不补写资格或临床建议。

## 最终采用、作者自查与冻结

- 正文 `content/book/life/household/shopping-returns.md`。初稿全文实际自读，历史正文 SHA-256 `f37769cce6dcd94c287b1e1bb97b68c11f03da5334186b979f911b8ff07761be`；历史整文件 SHA-256 `b6bfc4225b74a011a2852a77fabe405850dd004063162be4b0b2c56f3937dba4`。算法为UTF-8完整文件分离frontmatter后的 `split('---', 2)[2]`，包含分隔符后的原有换行。已由下述两处返修取代，不承载最终审阅结论。
- 采用规则与数字的位置：正文21行教学单位价；25行每份与5%／20%；33行CA2026-07-01食品日期与蛋／配方奶例外、35行配方奶UseBy；43—44行CA2024-07-01全额报价／食品例外及NY信用卡总价；61—64行四州退货条件；70—74行FTC发货30／卖方新信贷50日、首短延期默示同意及退款动作7工作日／卖方信贷一周期；82—88行RegZ60日送达、漏贷记起算、指定书面／电子方式与30日／两完整周期90日、借记卡；96—99行四州计量与消费主管。具体行号以冻结文件为准，来源靠近相关断言。
- CA原1723与AB660原法访问失败如前述，正文采用主管可实读说明而不声称已全文核法；NY218-a／518和联邦435／RegZ已实际读主文及适用官方解释。全国“Use-By一般质量”的旧说法未写入，避免覆盖CA当前安全日期；退款文件发出与银行到账、普通质量争议与billing error、信用卡与debit明确分开。
- 完整覆盖购买前单位价／标签／报价／政策、收据与订单核对、普通退货／瑕疵继续路径、迟发及未到货、取消退款、退款缺失／扣款争议、四州投诉分流与最终到账核对。少英语用实际问句与食材名记录，远地址网购用下单前核配送地址及退邮费用。两例均明示教学虚构，不使用真实商家推荐。
- 实际作者检查：YAML字段written／draft true／verified空／reviewed_by空；105行、49个普通链接（45 HTTPS＋4绝对站内）、站内目标源文件存在；无正文H1、加粗内外空格符合要求；虚构单位价数学核对；逐句过“删后会错什么”语言判定。未做构建／渲染／提交，未申请外部联系或操作投诉表。
- 站内合同稿B07须由root正式集成后再发布本稿；银行和法律帮助已有正文。SNAP／WIC等食品支持另留地图，不设资格、金额或申请承诺；其余未核范围保留上节。由另两名参与者分别独立事实审、第三静态；作者不为自己的正文安装审阅元数据或写PASS。

## 独立事实审返修：全额credit与退款期限引注

2026-10-13 08:06—08:08 UTC，root作为独立事实审反馈两处最小文字问题。本人作为原作者重新实际打开以下一级原件，作者新读取不借用root的记录：

- [CA OAG Refund Policies](https://oag.ca.gov/consumers/general/refunds)，网页工具本轮真正open，实际读151—161行完整政策主文；159行将full修饰refund或credit，并允许equal exchange及组合；160—161为例外及违法展示后的30日条件。故只将加州表的“额度”明确为“全额商店额度”。页面未明示政策更新日，仍不声称已打开本轮失败的Civil Code §1723。
- [eCFR 16 CFR Part435](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-435)，本轮真正open，69行标title16截至2026-10-08／最近修改2026-10-01；实际重读116—149行。§435.1(b)(1)、(2)定义七工作日及一个账单周期，§435.1(d)定义不同付款的退款动作。故仅把引注标签补为“§435.1(b)、(d)：退款动作与期限”，URL与原段期限／动作完全不变；不把发出退款当实际到账。

实际正文仅上述两处差异；frontmatter、其他断言、金额、期限、例外、引用URL和链接数量不变。按最终全文复算的完整摘要在顶部。本人在内存逆向撤回两处，恰恢复历史正文 `f37769cce6dcd94c287b1e1bb97b68c11f03da5334186b979f911b8ff07761be`、整文件 `b6bfc4225b74a011a2852a77fabe405850dd004063162be4b0b2c56f3937dba4`。原作者／修订者birth_fact，独立事实审root，拟第三静态static_editor；不混淆本人随后承担的其他稿件事实审角色。重新交root复审最终全文，不由作者写事实PASS或安装元数据。未构建、提交或外部联系。
