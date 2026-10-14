# 公共入口八件拟稿：第三人静态审

- 审阅者 static_editor；日期2026-10-14（Asia/Shanghai）。root修订作者 → birth_fact独立差分FACT → static_editor第三，三名不同参与者。
- 结论： **PASS（仅绑定下列八件未安装拟稿的完整第三静态审）** 。八拟稿全文、八真实diff及前审记录均已实读，未发现必要原作者返修。
- 本人仅写此新记录和事前逐路径核忽略的自有缓存；未修改八canonical、拟稿、他人记录、元数据或共享，未构建／提交。
- 八canonical目前仍是原件。本结论不表示候选安装、实际网页／打印检查或新场景重绑已完成；旧医疗场景的NEEDS REVISION保持冻结，等待新canonical正式分派。

## 输入、真实读取与版本归属

本人完整实读作者记录1—52、独立FACT1—97及manifest1—143；它们的他人阅读和失败只按原身份保留，不冒作本人的一级回源。已重新读PROMPT第七节及99行说人话规则，按实际防错作用判断，未用机械词命中代替通读。

| 输入 | 行／字节 | 本人实际复算whole SHA-256 |
|---|---|---|
| `ops/reviews/b-all-public-author.md` | 52／7801 | `5f70eb39acba321e35b1cc85884e7b817d1f4fad571d83d039939dc890a60ea7` |
| `ops/reviews/b-all-public-fact.md` | 97／17947 | `2683a86135a2349cabaedde7f1bfaf77be63bc5e6e626090bde4a40138c80efe` |
| `.cache/b-all-public-proposals/manifest.json` | 143／8075 | `94e575d3ca6754ab471a879d741aca0797174330b7a40a261da18a91b822eb08` |

八拟稿均含完整frontmatter实际读到末行，共222行／17744字节，按P01—P04与P05—P08两批读取；八diff从本人读取的原／拟真实字节生成，并逐份完整显示、实读。旧件本轮作完整字节核对和diff语境读取，未把这种比较称为另一次八旧件全文文字审。

## 八件真实路径、全读范围与位置

| 编号／canonical路径 | 本人实际完整读的proposed_file | 原行／字节 → 拟行／字节；修改行／全文字符offset |
|---|---|---|
| P01 `content/book/foundations/culture/_index.md` | `.cache/b-all-public-proposals/proposed/content/book/foundations/culture/_index.md` | 17／742 → 17／655；L15／272 |
| P02 `content/book/people/_index.md` | `.cache/b-all-public-proposals/proposed/content/book/people/_index.md` | 28／2155 → 28／2089；L16／312 |
| P03 `content/book/work/employment/_index.md` | `.cache/b-all-public-proposals/proposed/content/book/work/employment/_index.md` | 21／1359 → 21／1299；L19／507 |
| P04 `content/book/people/education/_index.md` | `.cache/b-all-public-proposals/proposed/content/book/people/education/_index.md` | 19／1141 → 19／1153；L17／412 |
| P05 `content/docs/routes/food-cash-support.md` | `.cache/b-all-public-proposals/proposed/content/docs/routes/food-cash-support.md` | 26／1654 → 26／1591；L26／775 |
| P06 `content/docs/routes/_index.md` | `.cache/b-all-public-proposals/proposed/content/docs/routes/_index.md` | 51／5733 → 51／5739；L34／1632 |
| P07 `content/docs/routes/caregiving.md` | `.cache/b-all-public-proposals/proposed/content/docs/routes/caregiving.md` | 36／3147 → 36／3168；L28／1033 |
| P08 `content/docs/routes/medical-care.md` | `.cache/b-all-public-proposals/proposed/content/docs/routes/medical-care.md` | 24／1936 → 24／2050；L21／722 |

对应original_file均为 `.cache/b-all-public-proposals/original/` 后接表中canonical完整相对路径，逐件与manifest实际路径一致。正文摘要取UTF-8全文 `split('---', 2)[2]`，保留首换行；whole摘要取完整原始字节。

本人独算32个原／拟body和whole SHA，逐项匹配作者／FACT／manifest；按每件实际Unicode字符offset先确认旧片段，再正换精确生成拟件，按同一位置逆换精确生成旧件。删除项以位置插回，未对空串做全局替换；字符位置未当作UTF-8字节位置。当前八canonical逐字等于original。完整frontmatter、全部数字序列、普通链接文字／URL／顺序、标题、行数和列表结构不变；八件没有正文表格，P08仍为原五步列表，只扩第4步同段。

## 逐件原句、改法与防错判断

| 编号／行 | 精确旧 → 新 | 通读后的判断及保留范围 |
|---|---|---|
| P01 L15 | “从具体谈话出发，比给整个国家归纳一种性格更能帮助日常交往。” → （删除） | 删句没有材料、资格或下一步，不能指出删后会漏办的动作；关系与眼前安排仍在L15，L17虚构对话仍接愿意做的事和需要确认的条件。段落完整，无全国统一礼节推论；PASS。 |
| P02 L16 | “家庭、学校与照护中的安排也需要这样逐项确认。” → （删除） | 删除泛指家庭／学校／照护的尾句；L16原医疗核账动作、L18—28出生、学校、照护、教育、心理、便利、婚姻和退休承接保留，未删具名受理或文件；PASS。 |
| P03 L19 | “休假和其他保障仍须按各项目条件分别判断。” → （删除） | 删重复兜底语；L21已在请假／工伤／歧视行动处核工作关系、适用资格、收件人，并分雇主安排／州收入／正式工伤或EEO提交。没有把项目统一或承诺有薪；PASS。 |
| P04 L17 | “录取后继续顾问计划、注册、付款和第一次上课。” → “录取后与顾问确认学习计划，完成注册、付款并开始上课。” | 把动作不清的“继续顾问计划”变成与顾问确认学习计划，再注册、付款、上课。继续学习正文具名学校与L113承接，学年、学费分类、认可及退出账单仍在；未增全国统一校规；PASS。 |
| P05 L26 | “，不把一项食品申请当成全部生活支持已经接上。” → “。” | 删除食品申请与全部支持的比较；L14—22保留当下帮助、按成员申请、材料／口译、收件面谈补件、领取报告与听证，L26继续分UI／医保、债务、住房／住户服务和账单；PASS。 |
| P06 L34 | “核工作资格和收件人” → “核相应项目资格和收件人” | 仅请假／工伤／歧视这一条改为项目资格，避免把一般移民工作授权当所有保护／收入项目门槛。职场路径和正文仍核雇员范围、人数、关系、工时与不同收件人；L33入职／L41开业未改，未取消它们的适用资格；PASS。 |
| P07 L28 | “工作资格” → “相应休假或收入支持资格” | 保留家庭关系、雇主通知、收件及获准休假／现金支付／照护服务各自确认。本人读到职场正文的岗位保护和收入申请分流及四州差异；EDD当前原页支持应核具体计划，不能拿“工作资格”替代。未许诺照顾者一律合格；PASS。 |
| P08 L21 | “保存收据，等保险处理说明与收费机构账单到齐后，按[医疗账单核对页](/book/people/health/medical-bills/)逐项匹配。” → “保存收据，按[医疗账单核对页](/book/people/health/medical-bills/)核对账单与已付记录；使用保险时对照EOB，没有使用保险时对照书面估算。资料未齐时联系收费机构或保险方，并继续核付款或申诉期限。” | 去掉等EOB和账单全部齐才核对的门槛；已有账单／已付记录先核，使用保险对EOB、未用保险对已有书面估算。缺资料就联系并继续看实际付款／申诉期限，未把电话当自动暂停。L14紧急／计划性分流及L20估算入口仍在；PASS。 |

P06和P07改的是项目资格措辞，不给某个非公民作工作授权或具体待遇判断。已读职场正文L39—49保留FMLA覆盖与本人条件、无薪岗位保护和雇主通知；L62—86另列四州现金／休假／承保与回岗。项目申请及雇主请假仍须各自办理，获准其中一项不能替代另一项的结果。

P08两版账单正文L36—43均要求查理赔是否收到、询问收费与已付差异，并取得付款／催收安排确认；L47—55按实际保险程序和拒赔通知分流，L63为未用保险的书面估算，L69—71接困难、文件结果和付款。入口“付款或申诉”按本人实际事项核；同时适用时不能任意漏掉一条。没有新增统一期限、自动停付、补件必获延期或争议必准。

急救和计划性服务仍分开；本人CMS采用段明示急救无此估算、现有估算按具体提供者比较，没有估算不能当然使用该联邦争议。P08没有要求急救取得估算，没有把资料不齐设成等待门槛，也没有把普通电话等同正式争议中的暂停收款；具体受阻仍回账单正文核对应路径。

## 承接正文：本人实际范围及十个摘要

下面行／字节是完整文件大小；本人阅读按第二列真实范围，不把整件SHA核算或先前审阅称为本轮全文。医疗当前正文和people拟稿都完整实读71行及真实diff；people页是此入口的依赖检查，不是另领people15第三。

| 实际路径 | 本轮本人实读 | 全件行／字节 | body SHA-256 | whole SHA-256 |
|---|---|---|---|---|
| `content/book/people/education/continuing-education.md` | 1—14、50—59、111—123，共37行 | 144／28502 | `d99c8bc5766a56450668a7a053d39c9a55813cb824bce54fa943081cc7952106` | `5fc71898d9c5b1e0dc65ecf82271c66ca8981d0b863f6d02f577cd1fcfe107af` |
| `content/book/work/employment/workplace-rights.md` | 1—49、62—86，共74行 | 137／26280 | `049c4ecee882f7ad65d2d713568d2e2df999c895b37e0f735b44fe56ee0def05` | `325c2509ab16ecb66e06ce2b94ceab8c61349be0e5ec4a94da7d90c452e17916` |
| `content/docs/routes/workplace-rights.md` | 完整1—28 | 28／2071 | `38db7fcfd778fccd17907d709f487ea43741ee1f92d8bae6ee53a944bf8f6683` | `b79a4058d897f49dc8d24fbfd0ee38ff90923a62e9f596ef3ef0842369eed90e` |
| `content/book/people/health/medical-bills.md` | 完整1—71 | 71／8705 | `485addc8f652f6ebe777814fa5527e8c43f406519cf50d0d809a74be90304fd0` | `89d72e74ec31531fdffa889219c206fdc7b59b263738608d69bd537a3099340f` |
| `.cache/b-pl-people-proposals/proposed/content/book/people/health/medical-bills.md` | 完整1—71，另读真实四处diff | 71／8785 | `b85af8f5bbaf5a130efec97c0c31022e3fcee983273d734ceefe508277cac141` | `682e5fe821e7cd4510a5ad65de77c938db45117e1dd124ce4e7e8d9395597de2` |

people账单拟稿仅把收费部门、内部申诉、外部审查和善意费用估算写成中文释义；本人四处实际片段逆换严格恢复当前旧正文两个完整SHA，数字、所有来源和frontmatter不变，L43的电话不自动暂停期限保留。初次只逆词项时漏掉billing department前原有ASCII空格，比较为false；随后按真实diff完整片段（含该空格）重算为true。未据首轮失败指称拟稿多改，未修改依赖。

## 本人一级语义抽核与真实边界

| 本人实际一级URL | 方法、日期、实际读段与版本 | 采用与未核 |
|---|---|---|
| [EDD：PFL资格](https://edd.ca.gov/en/disability/Am_I_Eligible_for_PFL_Benefits/) | 2026-10-14 06:56 +0800本人新普通verified TLS直连，取得真HTML后完整读抽取main1—96，重点7—27、32—42、82—90。页未列修订日期；HTML130769字节SHA `5de86f48e95e31990a418c3d2297b26fd5a30298bcbb3563a0191e590330ce0c`，文本SHA `c95c0b9b0fe09065a7a8c6a329846edba2158cd0e6c53f81e039bc5141eb9b35`。 | 该项目另核收入损失、受保工资、照护材料；其公民／移民身份说明支持P06／P07收窄措辞。未打开认证PDF或后台，未把CA推广到四州或个人待遇；取得200后实际读主文才采用。 |
| [CMS：读懂EOB](https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/get-help/guides-resources/read-explanation-benefits) | 本轮本人新trueweb打开原页，实际主文683—756，重点694—739；页最后修改2026-10-05。随后按683附近再开并独立完整显示采用段；未称810行整页全读。 | EOB不是账单，也未必反映已经支付的钱，支持先核已付记录、差额问收费方。未打开EOB示例PDF，未计算真实患者应付。 |
| [CMS：没有使用保险](https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/know-your-rights/without-insurance) | 本次重新完整读本人同日核心场景审独立普通TLS取得的main1—77，重点17—26、39—67；这是本人自己的旧读取原件，未在本第三再次新请求。页最后修改2026-10-05；实际p09.raw SHA `dc22c83d00fb4236b56cdd4f747c292459930b1e5f13adbac131e974d099618e`，p09.txt SHA `595c9d304efb596f14d88fbcbe4ae710b21af03b0cee6db9da0610ad4f2726ca`。 | 采用对象、计划性估算及急救例外、书面保存比账和不得拖延的时钟。未开PDF、争议资格子页或个人程序，未由该局部读取重判账单专题全部法律／时效。 |

首次CMS与其他记录合并打印截了部分非采用导航文本，主文已显示；随后采用段另开完整显示后才收口，没有把菜单或200当采用阅读。本人这三URL没有未解决的主文访问失败；作者DOL how-to-talk的Internal Error、FACT的DOL403／正常8888成功及其其他阅读仍各归他们，本人未在此轮请求DOL或HealthCare，未继承那些成功或失败。

自有缓存 `.cache/b-all-public-third-static-editor/` 的checks、diffs、navigation、dependencies、源HTML／文本／请求记录及source-boundaries写前均按具体路径实际check-ignore，命中 `.gitignore:2:.cache/`。同日CMS旧原件属于本人既有已核忽略的 `.cache/core-scenarios-static-editor/`。新web保存的是实际采用段文本，未称保存了原始HTML。

## 结构、链接与未核范围

八拟稿共有71个普通链接／58个不同站内目标，逐个解析真实canonical路径并读取frontmatter，全部存在且integrated／draft false；没有外部链接或锚点。逐件数量1／7／3／3／5／36／11／5与原件相同，文字、URL和顺序均保持。58个目标的存在和公开字段不是58篇全文或法律事实审，未新增HTTP／浏览器／打印检查。

八件的frontmatter仍是旧editorial入口字段，全部原样保留integrated／draft false、空verified及root编辑入口身份；不能据拟稿继承的这些字节说修订已正式集成。不存在新写正文误装候选、刷新旧verified或更换审阅者的问题。五处中文加粗全在P08，实际外侧空格和内部无首尾空格合格；其余七件无加粗。没有重复一级正文标题，未添术语口号、泛指免责、残缺句或无信息总结。

真实防错信息保留：P01关系与条件、P03实际工作关系和不同受理者、P04学年／学校和退出账单、P05非申请成员及领取／听证、P07本人意愿／权限／实际服务与雇主通知、P08紧急分流／缺资料与各自期限。削减的旁白未删除这些行为，语言判断均依据上下文。

未核：58目标的全量旧事实及来源、四州全部福利／工伤／EEO规则、个人移民或医疗判断、所有院校资助、真实保险合同／付款约定、估算争议表件及后台、具体个人提交和服务结果，不是本次重审。照护carev2四空格及people15其他页不在此范围；本轮只按上述medical-bills两版依赖。

## 八件原／拟完整32摘要

| 编号 | original_body | original_whole | proposed_body | proposed_whole |
|---|---|---|---|---|
| P01 | `3ade9ec9a7d42d100d985cac545ee4fd5ef8b1c951413a59472451ca867b6f8c` | `467d3f8ee977b45c0b9e26d6ffc6bea3ba65a838e7575c2ace0ee9f79c9fe145` | `5827b88118e4662af086d90ded49260fbe9fba134c47fb9ec7288db29cb8010a` | `4853a89546fff6e95699af7fbd9d002b8b6a8562ec4e49d818ed31c50a6803fd` |
| P02 | `681ba7a18dc62f311a105c9ab57863c318046b75486f1cb06e473f42810d07b1` | `a425ed92bc512a5ea368594e2e3e96fe2364a351b54f214110a4da5fa94f9ae8` | `ace9996fed0d24364dbed3d085502f82c44d088bc15547e80e5fe2b5898ed578` | `51bbe41829b53ee62540553029be6a13e1ba48a152f8b5c3638c0fac89664e34` |
| P03 | `2d203079ebaadfc913a1f9e02298114b9383028343ef638c826a0f4f76e75909` | `7a6a5967899f196775c5999e3e0aa62a7183c1cea5507bdf74b0dfb7b677bce3` | `c507ff0c4bc22aa517f86c67bb00f7097ff378b711b80740e2c9a05a1bbf73ec` | `6b4a22db250628a257d90f23644d359896d803332072d31594e91f5edb1fe81a` |
| P04 | `2c5f5a5cebac1e616aed06065a910c8824a5f6bf2179b8796dbe268ec81f4625` | `ced47e0de84b34b9673369773659b78ea4336c57e8873141ba6e3d7695c89b0e` | `35115b431893661bff624459203da0f5156937a9fdd200e76238fed10ac85b63` | `8bf6a2e9bd26c670f6eaa796c67e06e434124635890adeaafdca39558531ffc2` |
| P05 | `7350135258949000e78a9d97bc15bd5865fea6a5527e0e7b95adf3e74b59a415` | `88ce98b0539e7b3ccaaf7cac799f805bbec7fef8f1191cb5fa203fba637d7302` | `bc2f2d2bbf0b8cb4d774b8e68a90f14ea97c22b9a281bb1d6dcbcb4f54b32bc7` | `23beebd7fd83baacc3f764c8b3561f9e6ad579549f424c88ab31d1b0e903e001` |
| P06 | `6fffc57d86d0be4cc426dcb6a708d932965034e748382303fed7d09f7d544d91` | `6ebfaba6090a162c412d3e4fc0a662a55be11d6fe1d34537cb685d142a9a4b08` | `17dcf23a991587046903c91b5a5823807bbe32dccc76e1d4da142f0fe9e43c98` | `84eb7144a7ccde4431dac88d03eff0717edf983ee89a4094a87bbd802b4d4e14` |
| P07 | `41f62afcb8520649bd438b802d9b0da97f91ce312e71e59946c7c2cd3037998c` | `33cef9f9c26438a18cc719d8ddb7a106ce8942a1ac93c01068a1599f21e74c98` | `365a82ad91c0d15642c33d9f2a41b83e0214f9a19763a89875bf2bce88cbff26` | `33185ceff6a8898fa661c739c273e152efa8d8581ab87d892f6542828ba34420` |
| P08 | `185b18d96404cc4c262d3e117ac873718fc98c307423fd487a74b968ae1411d4` | `43988a8533c57c176a15d845edf35404390a7b0675dc74a5cc28b9ee6c679924` | `18c8cdc3ff5292ae6b36db66570fd4beb0843dadfec63eb0970224011d877a1c` | `dda4b27ac397eb4fad97537763a54fba3a482c4edca2f37a62c12dd9ffcb8545` |

交付前再从实际文件复算32摘要、十个依赖摘要和作者／FACT／manifest三摘要，并逐件再核canonical为旧件；旧核心场景记录181行SHA `18e36ca72afafe94f0218edd99d3b76203c5be589c245a64cf8c4e140311e274`保持原字节。不存在把旧HTTP GET200当真实渲染或本第三PASS的依据。

当前无必要原作者返修。root可按当前冻结八拟稿继续自己的候选和工程；新canonical后的医疗情境重绑须另正式分派，本记录不提前关闭旧NEEDS REVISION。本记录完整实际读回后的行数／字节／SHA在交付消息给出，任一拟稿或依赖更改须按实际差分重新绑定。
