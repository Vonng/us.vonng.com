# 全书公共页：只读语言与导航语义走查

结论： **READONLY WALK COMPLETE** 。static_editor，2026-10-14（Asia/Shanghai）。当前78件公共源全部实际全文读到，未读公共源0件。 **8页8处必要语言／导航语义建议待实施，70页无进一步修改建议** ；另1处地区总入口遗漏已报告并由root单独补正，本人新全文读取和逆验后绑定最终版。只读完成不等于建议已实施、PL账本已验收、新主题FACT／THIRD或正式工程／集成PASS。

本次只写本记录及事前逐具体路径核忽略的本人缓存`.cache/all-public-static-editor/`；没有改公共源、主题、作者包、元数据、他人审阅或共享PL进度，没有构建、提交、部署、外部联系或探测Claude。

## 实际集合、规则与阅读批次

真实集合为首页1件、全书入口1件、5个部分和28个章节导读、docs43件（总入口、阅读来源说明、术语各1；地区总入口和4州共5；事项总入口和34事项共35），总计78件／2170行／178768源文件字节。未凭新改26入口把其余17个docs或34件书内入口排除；不把主题正文混算为公共源。所有body摘要均按原UTF-8全文`split('---',2)[2]`保留首换行，whole为完整源字节。

本轮再次真正读项目AGENTS全部20行、PROMPT§7的165—215、说人话细则全部99行、实际路径`ops/reviews/speak-plainly-progress.md`全部126行、FOCUS全部32行；此前已读humanizer技能继续应用，不冒称本轮重读。最初试`ops/speak-plainly-progress.md`不存在，随即用rg找到上列真实路径并全文读。旧67件账本与当前78公共源／60主题不是同一集合；本次不领取或更新PL共享行。

先逐件列路径与双摘要，再保存83个已核具体ignore路径中的78份源快照和索引；本文新增缓存均另核具体路径后写。实际依次读：首页／全书／foundations9件、life7件、people8件、rights与work11件；docs总入口／about／事项总入口／地区总入口4件和glossary1件；当前4州各全文；34事项分6／6／6／6／6／4件读。全部从1至末行，工具各批均完整显示，未以命中／200／提取行数替代全文。地区总入口后又真读root新全文1—40，其他77件末轮双摘要无变。

## 待主控实施的精确最小建议

以下8处原句在实际行均唯一；只在内存模拟建议，自查完整frontmatter、数字、链接文字与URL顺序、标题、表格行均保留，没有在源上试改。P06／P07只把对应福利资格说清，创业／入职页真正的工作授权条件保留。P08明确既有保险／不用保险及资料未齐分支，不新增金额、天数或保险权益；root已接受此必要定位，明确与公共语言阶段一起实施，B15／B16本批未改该入口。

### P01 `content/book/foundations/culture/_index.md` L15

原：从具体谈话出发，比给整个国家归纳一种性格更能帮助日常交往。

建议：删除这整句，其余段落保留。

依据与保留：前句已给双方关系与眼前安排，后续链接给虚构场景；这句国家性格比较不增加具体沟通动作。保留关系场景与虚构说明。

### P02 `content/book/people/_index.md` L16

原：家庭、学校与照护中的安排也需要这样逐项确认。

建议：删除这整句，其余段落保留。

依据与保留：把医疗核账的方法泛接到三个领域，没有给新人员、材料或时点；下文已分别给孩子、照护与学习的具体入口。

### P03 `content/book/work/employment/_index.md` L19

原：休假和其他保障仍须按各项目条件分别判断。

建议：删除这整句，其余段落保留。

依据与保留：紧邻L21已明确实际工作关系、适用资格、收件人与分项提交。删此泛尾不删任何具体资格，休假与UI分流仍在。

### P04 `content/book/people/education/_index.md` L17

原：录取后继续顾问计划、注册、付款和第一次上课。

建议：录取后与顾问确认学习计划，完成注册、付款并开始上课。

依据与保留：原句把顾问计划和办理动作都作继续的宾语，读者不易知道怎样继续。补足动作，仍是现有顾问计划／注册／付款／上课，不增全国顾问审批条件。

### P05 `content/docs/routes/food-cash-support.md` L26

原：，不把一项食品申请当成全部生活支持已经接上。

建议：。

依据与保留：同段已经逐项列失业医保、债务、住房通知、住户服务和医疗账单的继续动作。尾句仅再否定全部接上，删后所有具体分流保留。

### P06 `content/docs/routes/_index.md` L34

原：核工作资格和收件人

建议：核相应项目资格和收件人

依据与保留：该项是休假／工伤／歧视办理，工作资格易混读成工作授权。与目标正文的适用制度资格对齐，保留资格核对，不改任何具体条件。

### P07 `content/docs/routes/caregiving.md` L28

原：工作资格

建议：相应休假或收入支持资格

依据与保留：这里已明确接休假与州收入支持，改称对应项目资格，避免与开业／入职页所说工作授权混读；家庭关系、通知和收件均保留。

### P08 `content/docs/routes/medical-care.md` L21

原：保存收据，等保险处理说明与收费机构账单到齐后，按[医疗账单核对页](/book/people/health/medical-bills/)逐项匹配。

建议：保存收据，按[医疗账单核对页](/book/people/health/medical-bills/)核对账单与已付记录；使用保险时对照EOB，没有使用保险时对照书面估算。资料未齐时联系收费机构或保险方，并继续核付款或申诉期限。

依据与保留：同入口L20已含不用保险者；当前医疗账单正文L63有账单与书面估算分支，L36／43要求查询缺失处理与保全原期限。原句让所有人等EOB到齐才核，可能让不用保险者无法继续或迟办。root已接受必要定位，明确与其他公共建议一起另批实施，当前未改；本轮仅源内对照，不作新外源事实结论。

P08本人另实际全文读`content/book/people/health/medical-bills.md`1—71：body `485addc8f652f6ebe777814fa5527e8c43f406519cf50d0d809a74be90304fd0`／whole `89d72e74ec31531fdffa889219c206fdc7b59b263738608d69bd537a3099340f`。实际L36／43为缺失处理查询和原付款／申诉期限，L63为不用保险时账单与事前书面估算分支；未重开CMS／HealthCare.gov，也未对其400美元／120日等作新事实结论。P06／P07还实际读当前workplace-rights13—33，L20—27的实际工作关系、各计划雇员条件和分别申请是源内依据，不把签证工作授权当本入口的所有福利资格。

## N01已由root单独补正：地区总页账户直链

本人初读`content/docs/regions/_index.md`全部40行，末L40只有食品／债务／通知／灾害／枪支五项直接入口，账户仍可经州页两步到达，不是坏链。报告遗漏后root亲自读L40，单独在句首加入与四州相同的“安排储蓄或教育供款时，沿[储蓄与专项账户](/book/work/finance/accounts-investing/)核供款、实际资产和取用条件。”本人随即真正新全文1—40读回，完整whole `6d2268135c62859b29b2761b2763f296ade92691a91e42e6853d416a911ec9ca`／body `fd112c8f5bfff9ffc62ca7bcab5e3bec2d1a28b8ac88e668c35cae00c4e5e4f5`。

本人唯一内存撤回该141字节前缀，精确恢复旧whole `3246f87046aed1ee9bbe8fae31b6afd9ac7945ba3e5b87e47f93e0ca78ba8267`／body `18de533755ab02ab4f908132a1e018308fc3ecb845b2445ec57432051448a081`；40行、全部数字和frontmatter不变，原五链接保留，仅新增账户直链。旧版确已全文读，历史不能套为最终版；当前该页无进一步修改建议。

本轮root还给4州末段加同一账户句。本人此前只取得这4份旧摘要快照、尚未读旧全文，收到修订后直接实际全文读59／55／57／55行最终版；不将旧取得说成旧实读。下表保存旧双摘要，当前各州绑定在总表。

| 旧4州取得历史（非旧全文阅读） | 旧whole SHA-256 | 旧body SHA-256 |
|---|---|---|
| `content/docs/regions/california.md` | `0872cdddb6d1c7e344bb8c63cdf13c70af7450ca371f1bdb9487aa5bfa3d4550` | `62dd0fe44572ddc6ebc43d151982419d04090716e56371dea390e40ed3519a85` |
| `content/docs/regions/new-york.md` | `d0ee3becb122de31e9b01cd4195935f0d2800ffecd5c2f7d9b4cfe653a141d44` | `2f6d23a52084dc2e7fa893e987800e1b1e41434ff735c89b9ad0a48ecf97560c` |
| `content/docs/regions/texas.md` | `6a3b57752e4661c69166426d5288db514414b97d9ffe616f29708a84e0023c3e` | `5118ac9fcac41e71f65bd0f650ed8a9ffaf6e1b16dce9467dd92943db58f5dd0` |
| `content/docs/regions/washington.md` | `6c47ba5387d5d59428ef6cee8ff55695c77a0a8c66675041bc640e088835cbdf` | `1c34b0739b1dbf3e7ea74ac95feb7afd3b06d8a7fc4fb97f561327a4517e0970` |

## 导航、公开状态和保留边界

最终78源中712次普通Markdown链接全为绝对站内路径，115个不同URL（包含6个段落片段和生成打印页），映射108个不同真实content源。源目标实际字段均integrated／draft:false，没有失踪源或draft:true目标；6个school／tax片段另从既有public HTML实际h2／h3 id核到。它是静态DOM与源核对，不是本人新视觉渲染或构建。`/_print/book/`是生成路由：实际book源outputs有print、已有public及production-review打印文件存在，另读print partial全35行；不以没有同名content文件判坏链，也不称本轮阅读全文／渲染整书打印。

本人另真读book-directory shortcode1行与project partial5行，确认目录按页面／章节递归生成；首页15行源使用landing，首页卡片／搜索／移动侧栏等实际布局和交互没有在本次源语言走查重新操作。正文源、路径与公开字段不能替代用户浏览器和手机测试。

检查时（UTC2026-10-13 21:59左右，对应本地10/14），6新主题和6新事项源已装候选公开字段，但其12个对应public HTML尚未同步；root亦明确六篇仍candidate。故不能由FM写integrated推断它们已经工程／正式集成或部署完成。其余已存public与生成文件的存在也不算本人的完整视觉验收。新六篇在相关work／rights部分、finance／legal／safety章、事项总表、about和glossary均有实际入口；4州及最终地区总页已补齐6主题。没有文字仍称新六篇未写，所见尚未寄到／尚未完成等说的是读者自己的材料或事项。

14个传统检测词定位结果为0，但P01—P08来自真正上下文而非零命中推PASS。保留真实条件、时效、责任、例外和教学虚构：服务区／学区不同、非公民发言与投票资格、SSA代领／生前POA与身后权限、已获无障碍资格还须订车、递交截图还须确认生效、来访与长期生活、各程序起算／收件／送达以及名额与提供者接案。没有为了语言删数字、资格、来源、标题或表格。

## 第一轮场景与当期核查的关联

本轮先读家庭场景12行、医疗当期11行当时IN PROGRESS断点；收口发现两记录已由各自执行者增补，随后本人分别真正完整读家庭1—64／65—126／127—182及医疗1—44／45—86，而不是把更新SHA冒作全文。当前家庭记录whole `fd73097105e68f124561de42d14e11b08f11c64ff2d4c76226ba7593b09beb7c`、医疗记录whole `18adf84443985b2ea750e50323961bef332226a5de552ab30449e59d890f98a0`。

birth_fact的家庭场景结论是三条普通入学／在校支持、长期照护、亲人去世链的READONLY COMPLETE，无必须新增主题的核心断点；它的21件全文、具名地方与失败范围属于birth，非本人重新查完家庭事实。本公共走查保留事项school／caregiving／bereavement及四州相应入口，学校请求与同意／服务实施、本人意愿权限／人员接案、身后处置／通知与正式申请均未被概括成一种办理。其Seattle HCS具体办公地址未核、ADRC导航不替代批准、低频专家案件和个案付款／名额未核边界继续保留；不借目录存在宣告个案可办完。

banking_fact当期医疗核查在实际范围无必须事实补正，有退休assignment中文释义建议，属于它的19源与选页范围；本记录没有继承那些新回源为本人，也未实施该正文建议。P08是本人公共源与医疗账单正文的独立导航分支发现，不冲销两人的有界结论，也不转为全书医疗、全部家庭情境或60主题新FACT／THIRD PASS。

## 当前逐件双摘要、完整实际范围与判断

每行均为本人从当前源字节复算，范围1—末行含全部frontmatter、正文、表格和链接旁文；无需改理由按该页实际任务记录。78件之后再次实算均同本表，没有未读的公共源。其余主题正文只核内链目标与字段，除上列71行医疗账单和workplace选段，未在本轮全文重新阅读或回全部外源。

| 实际公共源路径 | 实读行／bytes | whole SHA-256 | body SHA-256 | 判断／具体理由 |
|---|---|---|---|---|
| `content/_index.md` | 1—15／405 | `657a3a00089fd1b575d8fa3bcc82af799049005b051875f8aaab65dc72aee361` | `79633853cc6599ff9901367d0777440eafa18eb95ca0b2c48e918c6b10f89bc1` | 一句说明连续阅读与按问题查找；没有免责声明或虚构事实。这里只审15行首页源，landing布局的视觉表现另由root核。 |
| `content/book/_index.md` | 1—36／1167 | `6c665b4e42351fe43b9b090b947478ce68b1344df3f2f84813896d3666a9595f` | `00e7935b06f154ae27342e959ec59f52d590986f6d7335dba77b41176fa47ae7` | 事项、地区、术语与打印的用途具体；目录由shortcode生成，不把源码中的一个标签算全文目录已渲染。 |
| `content/book/foundations/_index.md` | 1—22／1358 | `0d5daf3d2795e9c172ee826219d0eb19b42b646fc8f4ea70bbe7ac65c171630c` | `91bea13ca0cf7b7b6846f8231196b03d1fdf059e0afbc156a1c9f48853480804` | 各章与迁移／公共参与有用途分工；按个人资格投票的限定保留。 |
| `content/book/foundations/communities/_index.md` | 1—17／837 | `44a76acafdf3fc09caec624bfcb415af9f525c310ab2d363741514633fa1491c` | `64543c7be3ab898a96815bd03924a16d10cc11b89ff97553228c6ad3b06ca4e0` | 具体Nation、成员与土地制度及时间地点提示防止跨共同体误用；没有空泛文化训诫。 |
| `content/book/foundations/culture/_index.md` | 1—17／742 | `467d3f8ee977b45c0b9e26d6ffc6bea3ba65a838e7575c2ace0ee9f79c9fe145` | `3ade9ec9a7d42d100d985cac545ee4fd5ef8b1c951413a59472451ca867b6f8c` | P01；首句的双方关系和眼前安排、后句的虚构对话说明均保留。 |
| `content/book/foundations/geography/_index.md` | 1—17／826 | `c588c7e407edb6a8f8cbedd75a3524e2cdd77f6c966f447bb41bf476ace66ba6` | `3b420436ff8a046d005f1d215a2318842508689055a9d184cb501acbdccf76ba` | 州／都会区／地址口径关系到选址和主管，虚构算例标记保留。 |
| `content/book/foundations/government/_index.md` | 1—19／1014 | `ba5eeea2637bdae5e270a6dde61fedd305ea95c983b4cca3d584b3a9ffce7ac4` | `c0609c0af4aa3b5c922d138857e90985a6056d3ad4b15c0fe55328d0db590c35` | 先看签发与主管，再分公共意见和个人投票资格；程序编号与期限分开有防错价值。 |
| `content/book/foundations/history/_index.md` | 1—21／1468 | `058029b29d7133a7cd3d2c00b5c0e0de47e4f07c139601342d3269a783a81042` | `5f4ee1ba1398e8febaf075bb195b52f65e4a60be90f69e910bb50a8ae1a54fd0` | 建国、隔离和迁移各有时间／权利／资料口径，未把历史身份限制当当前办理条件。 |
| `content/book/foundations/world/_index.md` | 1—17／928 | `03a91b83136778a23ba7092619eb18b17da415d0303e3f1ed1f3e741c87c9944` | `17437369e796c1ac129eb5d091683e84d83f4a0a43760f120e65b86330b135df` | 新闻的日期、对象与单位及统计／机构主题写清，实际跨境需要按个人文件而非概览办理。 |
| `content/book/life/_index.md` | 1—26／1813 | `74681b4581112347c65485b0014f76e84ae335dae08fb91858a2b2f51754b727` | `c918e09156e26398b9f030e0261d6e0d74bd53bdbeb6200d2e0f7784aead9f40` | 文件、租住、驾照、通信、消费、社区、购房、住户与公交各有入口，未重复具体规则。 |
| `content/book/life/community/_index.md` | 1—17／1034 | `2b5eed4f6944b0ef542fb27e7c41ffe85790aeb3ef7ebd4975281818b6026b36` | `c50408612a46e5b3d335d1010fe0519c72359decabf8efaaf36730149334d521` | 市／县服务区、卡种和设备权限影响去哪办；沟通与开放活动有实际转接。 |
| `content/book/life/digital/_index.md` | 1—17／1007 | `b48f4fc45b884cf128bf1bfd117dc29a62a6d4e7e0626e942278d9a2a9e56ea0` | `5f9a7e026da613b613ebbed4d5f2bbc35ba74dd56ae2b16fe2707f6873a96350` | 设备、地址、报价、号码、扣款和归还分别接到办理结果，合同／银行／信用转接明确。 |
| `content/book/life/documents/_index.md` | 1—19／1285 | `facf5f0a736ed29ac6bbfa141df4b7fcff0615e7093bcb465e3c938ff610634e` | `704aaaa379cbeb88607481597ffcc86e5829158a4680c09917c077a8493a1ade` | 文件用途、号码、逐案改址与返美记录分开；安顿事项不是旅行资格替代。 |
| `content/book/life/household/_index.md` | 1—19／1202 | `b257fac27250cd99da6c46ac5824585b57c17eabf0e1b21f50546026a8ac231f` | `071e36bdd181d8683e617ee39fc622892f75ed316c6ad3ec1ffa080b1282bbca` | 开通／核账／搬离与购买／争议各按事件分流，不把退款或自动付款混成同一路。 |
| `content/book/life/housing/_index.md` | 1—19／1262 | `ed77723bb3dd57ce3a825ef2a48ecd98c632bca7d6ac7c10168484229de434d8` | `43907e8ad92ffeb0e19f5435a853a44937cf7f7f7bfded97542d4a5524d07f49` | 租住与买来自住的材料、付款和持续账单分开，产权／估价／保险的区分有用。 |
| `content/book/life/transport/_index.md` | 1—21／1318 | `ea7a4fb69e5a45bec8765ce58e5f19fb11fc6a893b29821d06d3616819879004` | `f384fdc389acee3cfad21be16d1cb248f1328c73f946315fded20d6551b0ab87` | 实际去回程、驾驶许可和车辆文件分开，不把交出车辆或办驾照当所有手续完成。 |
| `content/book/people/_index.md` | 1—28／2155 | `a425ed92bc512a5ea368594e2e3e96fe2364a351b54f214110a4da5fa94f9ae8` | `681ba7a18dc62f311a105c9ab57863c318046b75486f1cb06e473f42810d07b1` | P02；医疗、出生、学校、照护、学习、便利与退休具体入口仍保留。 |
| `content/book/people/accessibility/_index.md` | 1—19／1181 | `2400358f5f73a61508ff3c9553180fc825707ac5149a1f8795a88943ac82c7f6` | `93d75d6e85d78ac117986cee7f5d8759eef17c78c68bda73a427dcc2a21a3740` | 接诊与便利按场所／服务／法域分开，日期、联系人与拒绝后的续办具体。 |
| `content/book/people/aging/_index.md` | 1—23／1811 | `aa49e094e90fe97820d7e4fede7a5acdf798da90b0650d18647ebad2e9de850a` | `cf5afe0758a1dec2c03d1b19f4618b52120d8888aa7a0029cbd3d13abd5a6f21` | 退休、照护、授权和死亡四链齐，信息权限／临床医嘱／身后手续的分流保留。 |
| `content/book/people/education/_index.md` | 1—19／1141 | `ced47e0de84b34b9673369773659b78ea4336c57e8873141ba6e3d7695c89b0e` | `2c5f5a5cebac1e616aed06065a910c8824a5f6bf2179b8796dbe268ec81f4625` | P04；认可、执照、学分、工作照护与费用的真实选择条件保留。 |
| `content/book/people/family/_index.md` | 1—21／1337 | `c4104d2fa7fc7024521edaedb8d3155fd6798228900a2c0e43e959e20098815a` | `f6ee28f5ed3acb447f33fe6f36d130c259118e7efcc12d27460fe0d4588ebc67` | 按涉及的人、授权、现有婚姻和实际照顾核文件，执照／法院／托育名额均有继续路径。 |
| `content/book/people/health/_index.md` | 1—19／858 | `bd9ab8e45a51f43da952efa20ccc4f587c6cb26458f61bd592bca3daa246e18c` | `44a9c41c324e5b46154fc2a79474556db298dcb1243e4ea3b9a1f87e46ee125f` | 保险分担、网络手续与账单连接同一次服务，失保／迁州另核旧新生效和持续用药。 |
| `content/book/people/language/_index.md` | 1—17／847 | `ffcfe5fa74332340997fb8629b750999a7fd936ed4cc3192da9cd8110f1b4a66` | `ee7aed076428f489e5d01f44678f0a498c989141ae8ce915ac887ad0b70ce35b` | 日期金额编号、澄清与复述是实际沟通；例句与正式办理期限分开有防错价值。 |
| `content/book/people/school/_index.md` | 1—19／1135 | `733ee1a0e8d12d912e74b047fef97c3cae184f2b39d915bc36726debeee0fe93` | `0b05977b1d3e6dfa10d8117045c1e057c62a8111e9011c200762b032b9f2b079` | 入学缺件和人工协助之后接语言、IEP／504与安全，获准和实际实施分别检查。 |
| `content/book/rights/_index.md` | 1—24／1683 | `54c12c00b60e2ae90bcfe990fe02bdb7b899f4311dc7aa212cc64da49cc56bdf` | `0d2f2522e347f5245498fb669c142b9c6b0a365befefbef1469e126ecbabaae2` | 真实通知、法院回应、合同、户外、灾害与枪支各有入口，新三篇没有仍称未写。 |
| `content/book/rights/contracts/_index.md` | 1—17／992 | `ccc413e6fe77ceb715584470e9108ec1941a248cc5abf0468a9920fa9c6b181b` | `89b2b44b1e93e29402479fc56fd8fc3bbe9703225029b011d9f9dba4ef50b654` | 交付、总成本、退出与具体场所取消有对象，租约／工资／医疗另接已有正文。 |
| `content/book/rights/legal/_index.md` | 1—19／1108 | `71ec5e3b0dedaf563d200d147ac8123731c0ac9895e994b3cb76b2ffed2d5e9c` | `42ff8db81fac91d17e34843943bad2ceab1160e2d3f662eec2885cd3b5e76712` | 解释／个人分析／出庭代理不同，通知期限、递交和到庭有实际承接。 |
| `content/book/rights/outdoors/_index.md` | 1—19／1060 | `d0bda805e38026d1845c0bd466939f7066e37f3caf2e21511812ef24dc4cd9f0` | `588863415728f67e423e2e5c64c98a53d8a9d8184a6c9a9201005d30c02cdaea` | 管理者、凭证、当天关闭及可信联系人／返回结果具体，不扩大普通日行露营范围。 |
| `content/book/rights/safety/_index.md` | 1—21／1033 | `732ef02bb6631ca70ea65f56b971ca3f30793804155209c226525477d990febe` | `5570f100af63872e13fbcfaf02a931711c2b9cbb307c423bb643efaede9cadcf` | 危险程度三渠道之后接灾害与已有枪支；儿童／危机、合法接触和主管凭据保留。 |
| `content/book/work/_index.md` | 1—26／2031 | `657b69b1ef0e26c0bd06804ecf462eccc1835d61bb0e52527ee75ea172f3c66a` | `60cb9e89cff212f4a6258459ba609a8c2eb928690a6981e12fc657e9c7c0793e` | 求职、工资、经营、申报与三篇新金融支持入口齐，不把现金供款与账户资产混读。 |
| `content/book/work/business/_index.md` | 1—19／1151 | `c81188cf59b83e0eac49f07c221b81eff87985c5a164c6933574f2167ed3a2e9` | `16cb02c9ea898e546231b7654baeb2cdd85643f7aa9e51552cf4340511bd800a` | 本人工作授权、企业主体、场地许可和雇主／停业手续分开，工作资格在此是真条件。 |
| `content/book/work/career/_index.md` | 1—17／944 | `5b716bc24f726709e1953a1a856c0fcfb8cd08ea2fe42675f274c16a4aa3d0c7` | `45096563aeef13e6ebaa01dabae56ca310d365c0c06663c4201d89b0455c35c0` | 招聘核验至第一笔工资连续，背景材料和I-9有用途，不把offer当入职手续完结。 |
| `content/book/work/employment/_index.md` | 1—21／1359 | `7a6a5967899f196775c5999e3e0aa62a7183c1cea5507bdf74b0dfb7b677bce3` | `2d203079ebaadfc913a1f9e02298114b9383028343ef638c826a0f4f76e75909` | P03；L21适用资格及雇主、收入、工伤、投诉的实际分流保留。 |
| `content/book/work/finance/_index.md` | 1—21／1389 | `ba7a0b1b5614b6f080e98a5279f8ec0ad84a8177a2be587aec985568c1e519ee` | `aba94642c606b6f4af5479084040caa5a15de2c202cba3ad8315d8d2a11f0acc` | 银行、信用、专项账户、债务和食品现金五篇各给实际用途，新三篇均可直达。 |
| `content/book/work/tax/_index.md` | 1—21／1237 | `dfa1fedf4dbf550f1138493d43a1ecc6933e7be90c1f6e82f238965ea5c66576` | `a5faf17a0c4f3c1f5d7d635706d7b3b4fd1e4e7f852804744ed983966a0afb5a` | 税年、居民期间、州来源与申报付款不同，号码／签证不能代替税务身份的提醒有用。 |
| `content/docs/_index.md` | 1—19／608 | `ca9fe1e9086036653d02091c3bc9f7e59121e26b67a3f486e3b277ef0767ac66` | `91fdc6be08b603cc3455b9d05915d2cdfb6e6c8f729f5ed83566dbe8fae854e3` | 事项／地区／术语和连续阅读四种需求对应真实入口，没有重复免责。 |
| `content/docs/about/_index.md` | 1—48／5707 | `33c08d3927a8c8baae28686dcf8a2e385fc250b0f8358909c6a6e38409ac683f` | `02cf1103ab148f823a90b6fc0a8341a36e5681e885ef7e5f7086a7dcb3670150` | 核验日期时效与虚构标记必须保留；当前覆盖已含新六篇，维护单一正文及主管核执行方式有实际用途。 |
| `content/docs/glossary/_index.md` | 1—76／9547 | `57ca7738a46d17fcf83585470479c4449da3f27a8f4524fb20fe46c827b45fb5` | `db419067a098ebd151f153eb709a93fa520e7381d2d2c618e9e0fa6e22d87218` | 陌生英文／缩写到解释页的导航明确；L71—76新六篇均有行，不删除真实术语或定义适用提醒。 |
| `content/docs/regions/_index.md` | 1—40／4669 | `6d2268135c62859b29b2761b2763f296ade92691a91e42e6853d416a911ec9ca` | `fd112c8f5bfff9ffc62ca7bcab5e3bec2d1a28b8ac88e668c35cae00c4e5e4f5` | N01已由root补正后本人全文重读；六新主题现在并列可达，市县／学区／服务区边界保留。 |
| `content/docs/regions/california.md` | 1—59／7787 | `5baab8679086e3f5768591ed8aee804959657596913ebcf43d932778542627d1` | `8d78e0e732f372f694a057be6e7876ddf14d769f6e7447af63ece3f5573eec54` | 已全文读加入账户直链的最终版；LA市县、Pasadena／Long Beach、SFUSD及具体服务区条件保留。 |
| `content/docs/regions/new-york.md` | 1—55／7510 | `40c8c46c24d01e27c873cc80f344b9ea8e5eca4bd706f6488a68a50627eed3c2` | `739fc3c01e1b0ffc6e6f8b60ae96873a104e5b62c7f57bbd9b287a433f974bd5` | 已全文读加入账户直链的最终版；NYC与其他州内机关、四区／Staten Island、Tompkins场次分开。 |
| `content/docs/regions/texas.md` | 1—55／7648 | `6db3219269021c492f82f543e05fb8c5821ecd9095c9b919a5b4dd193e8fb6fd` | `d2c2471e1c312f154ac0d99e0fb2b0e8b2433859fe4510c790f81eecb1acd975` | 已全文读加入账户直链的最终版；Houston市界、Harris经办、Austin学区与Workforce服务区分开。 |
| `content/docs/regions/washington.md` | 1—57／7609 | `a21abd8c99b409f6d26bcb3eb6842b8b8bd43ef352e36880424cb7790ad2e8db` | `a54d9e7034615f6a00ef0930d8334c861677e7ad15f0f0a899b9f4653c098eab` | 已全文读加入账户直链的最终版；Seattle／King／其他县与工作日／日历日起算不混用。 |
| `content/docs/routes/_index.md` | 1—51／5733 | `6ebfaba6090a162c412d3e4fc0a662a55be11d6fe1d34537cb685d142a9a4b08` | `6fffc57d86d0be4cc426dcb6a708d932965034e748382303fed7d09f7d544d91` | P06；34条事项均能到真实对应源，新六事项已全部在列表。 |
| `content/docs/routes/accommodations.md` | 1—26／1786 | `07c8b55618f937623797d60d1ec0fc14f0bec90388d0089808f77339269e9af8` | `b5ef96a50ae121772bf7b3d542f7d7e3600b8a606df9382997a24b0d1331e476` | 具体请求、指定收件、辅助实施、拒绝续办及原事项期限都在，不用咨询代替正式递交。 |
| `content/docs/routes/accounts-investing.md` | 1—26／1635 | `d5cc3fcd0fd88864ebeaa0f64ea2b0460907caab26da92469c4919cf0c19619e` | `4f2724a7d5334a560aac0a83972ef98a3a1d9e458f41b6d21da02f1ef190c5cb` | 现金、保管方、资产、保障、雇主计划、年度供款与取用各有用途和完成记录。 |
| `content/docs/routes/advance-planning.md` | 1—29／2246 | `bde1ac6fea76bd1ced30eb4a24c533404534a95cce011b91f59536165c48495e` | `097640e9b346a3d519c7af267e81f370223d2b75d79d6f9c60e39970cb460e8f` | 本人能力、医疗／财务／信息、签署、交付、撤销与死亡后的权限重新核对，条件不能删。 |
| `content/docs/routes/arrival.md` | 1—40／4452 | `ce73b428dc3853ba91e1ee4e5872228ec0fcc7c9410aa1be56609a466723d008` | `0938540809472e2d3075839caf93c367f4bacbe0ac217766c44bd9fce0e5bfc0` | 短访／长期生活、逐人文件及并行安顿到实际使用齐，不以申请截图作生效证明。 |
| `content/docs/routes/bereavement.md` | 1—28／2142 | `8e0dd4a53e1a0a3778091fc608df296d6453736508c4e109f7855789dd45eaa7` | `1d1bcae9278fafe373d9d025e2dd030af10046cec93382a23605b96a29c428cc` | 交接／处置／合同付款、发生地证明、遗属正式申请与遗产各有机构，生前权限不能通用。 |
| `content/docs/routes/buy-home.md` | 1—32／2466 | `eddb02fe2e87ffa2793fe5f8c9f5b465018dea85306b3f8e95300d7afe5b4138` | `b437f149da8502f5a8b147fd7949e1cb532986223e4c395e695033fae9e12ae9` | 预算、购买资格、贷款、合同、资金和成交后登记／税单有实际文件与原期限。 |
| `content/docs/routes/caregiving.md` | 1—36／3147 | `33cef9f9c26438a18cc719d8ddb7a106ce8942a1ac93c01068a1599f21e74c98` | `41f62afcb8520649bd438b802d9b0da97f91ce312e71e59946c7c2cd3037998c` | P07；本人意愿／沟通权限、出院、付款、提供者开始日与备用人都保留。 |
| `content/docs/routes/childcare.md` | 1—27／2089 | `2b092fc741d4a7d29cfa764f1dc127377b17ecf2970d9974823090ba62dce1b5` | `525f89c8dcae5e7767ca98b6c565eb7701ab99e9d482a702d15348dd03b17bdd` | 许可／现场、家庭申请、名额批准与提供者接案各有确认，安全报告和退出分开。 |
| `content/docs/routes/continuing-education.md` | 1—30／2080 | `71b1bf4006bd0ee413fbc983a2c822710e172ce0d9bcea266711995b1f8a8523` | `2998c7d9721b4d5f5a0791344a2ebc2ac5880587c2882b31801c26dc240feb3b` | 课程结果、海外认定、学年资助、注册付款出席和退出账目齐，不套统一学费／身份。 |
| `content/docs/routes/debt.md` | 1—26／1654 | `5f4585e3c8e034e070bb26458e20fe76e9ab20d500f404a7128d4f9eeec22a7f` | `cd112388c5413c2b039bfb3504f291ef5330e0c75068553004adb89f36d35576` | 催收身份／明细、付款安排、停止联系与法院回应分开，结清记录具体。 |
| `content/docs/routes/disaster-preparation.md` | 1—26／1732 | `2e2dccf2f868bc7213f7bec81d13485a3ab6919d9fea51673da445b7abff2b44` | `4645172706d5494b92212a0b225de16d405b92352e33e34e7ab8cb8a10d024ce` | 实际命令、家庭电药交通、允许返回、保险及灾害援助分开，有补件和后续服务。 |
| `content/docs/routes/emergency.md` | 1—24／1215 | `b4c4eb445d9466f88d8786a2d2bec81ce79c95b138ab9fa4754345a1b0697257` | `016c586b2e592177688a7b82469d5fa75ec1f948e449bcb6cd8a06014593cfcc` | 危险、危机及非紧急三渠道有选路，灾害和枪支继续分别到对应主题。 |
| `content/docs/routes/entry-return.md` | 1—28／2195 | `d3c8873d8634e5c5a6996a75e95c2ecd3aefa2158559a2f3a9aa957fd7908ca6` | `e841888ee40aba8856fe79815621bec9442ef160a650ba316d8aa888d3189cc2` | 逐人文件／日期、当期执行、海关机场、I-94记录和安顿分开，缺件有继续动作。 |
| `content/docs/routes/firearms.md` | 1—26／1687 | `7e15c6c8a66eecd0d4860635d33da6a3f5f7ece6ca2a864c8b7bf823614cdcfa` | `8a64a13cb597e73a72da81961121eec8baac19967c8a2b294f4c090258448e4e` | 已有枪支范围明确，资格、儿童危机、合法接收、报失与法院交出不简化成统一行动。 |
| `content/docs/routes/food-cash-support.md` | 1—26／1654 | `88ce98b0539e7b3ccaaf7cac799f805bbec7fef8f1191cb5fa203fba637d7302` | `7350135258949000e78a9d97bc15bd5865fea6a5527e0e7b95adf3e74b59a415` | P05；当天帮助、谁申请、人工语言、面谈／决定和独立生活支持分流保留。 |
| `content/docs/routes/house-services.md` | 1—34／2703 | `1d5ea50c5d5f9b996ad2108b4e92cb466cb1e8ff1eaffc7b898e3beb2bd45858` | `e4ad823b526a6fd481692efa883f0fbd68b36fb478fa3c4b69725e33ae87f74c` | 实际提供者与服务区、材料／开通、争议／停供、搬离结清及灾害用品具体。 |
| `content/docs/routes/identity-theft.md` | 1—25／1435 | `b3faf75b8fa158546da15cd3c182eeb96173660bc79594180a253a1fd7f281a8` | `890af7642d48adc1650b3ec1f0751819edadf42317e1a84b26007417e6189b72` | 资料错误和盗用不同，账户／征信两方、证件号码、催收和法院各有继续路径。 |
| `content/docs/routes/job-loss.md` | 1—30／2790 | `217c2c22fd967876230fd2a72fa708c58230dba87915ff08668a3b550ee293f5` | `fe119da17550a20df5a51bf29ab3f1350deaae28e74d9228a5ad3680ee1a02e7` | 三种结束日期、工作州UI、工资争议、其他劳动程序、医保和紧急支持分开。 |
| `content/docs/routes/marriage-separation.md` | 1—32／2586 | `9322f626df81b3fdbb18cf67e671545a81d2c0dc10061417fcf9c86552c23843` | `880e9ac75c3cea82e261e11413f624c7eed220ab54c6be31fa8531755c3cb69a` | 现有关系、县执照与有权法院、送达及判令后的账户分别核，不以办证地认离婚法院。 |
| `content/docs/routes/medical-care.md` | 1—24／1936 | `43988a8533c57c176a15d845edf35404390a7b0675dc74a5cc28b9ee6c679924` | `185b18d96404cc4c262d3e117ac873718fc98c307423fd487a74b968ae1411d4` | P08；本轮真读71行医疗账单源内依据，保险／不用保险与资料未齐的行动需区分。 |
| `content/docs/routes/mental-health.md` | 1—30／2174 | `6bf56b411513deae08852d858889f32ed4c3f024ff93d55296f67084d5e99210` | `440dcebbb5cd654f285c2962a40f6b4677f3d2c216f122c2bc8dcb3540011b35` | 即时帮助与普通预约、接诊费用／资格、语言辅助、随访和候诊拒付均有接收方。 |
| `content/docs/routes/moving.md` | 1—39／5316 | `cbe10a659f5359db81bde13288ae5708f3e54ccaa95affc43ed6653c77b48f69` | `dc53c91d02b9de941b3f0773b73358737e00accf6088aa2b4fd2e4c7bff34c2a` | 逐人逐案改址、住房／服务、医疗学校、车辆、税务、授权及危机准备可并行，期限不能等搬完。 |
| `content/docs/routes/notices-deadlines.md` | 1—26／1617 | `18f85daa3ea5ad59bf8ab130fe78b5c6efa546e233215eec32b7b4718dc4f791` | `c40138bc0f993072459056b49c518159bb5fbbfef160404d9daf0270525deb87` | 案号角色和每个起算、指定收件／送达／到庭、漏期和后续书面决定具体。 |
| `content/docs/routes/outdoor-trip.md` | 1—30／1925 | `32bc36cecd64b08301e3294b1e2296b93702274207e77519d6b502a86c19cbe8` | `b6375218861a714503cc4c9dc925e801e612cf17daec8dd20c8339677af0a942` | 具体入口、同伴／辅助、凭证、当天路线、定位求助、返回及取消订单齐。 |
| `content/docs/routes/owning-car.md` | 1—27／2150 | `582456784cbeb679b068e5cafb424a8a013e6d9e172791512b343e625d63d798` | `152df334fd02fec44746bed14bc53f39180e7b70471b2b6a373f07c13cdb8b6c` | 车辆与驾照分别核；保险开始、产权登记、事故索赔和卖方退出均有完成记录。 |
| `content/docs/routes/parenthood.md` | 1—34／3213 | `63911b563a6137d2d97fbd452fb2137a179015137659faed2552c3599837469b` | `f66863da26a0f842a92d06d5416e9202286e76aa7774029f25f0e03fe75ebafe` | 孕产者与孩子、出生四项、未齐先申报、随访及托育接案有时间和权限，不能删真限定。 |
| `content/docs/routes/public-participation.md` | 1—30／2249 | `a0589baa959e0038321e3a5f242775a5dc4e6e08e81cd1ae5163b862d8cd65c2` | `f5bae95540b4e7ebebbe1abe1628f6f06e77bcd4ddb0954cf9dac5605301f89a` | 公共意见、个案申诉与投票三程序分开，公民资格／场次／申请邮戳收到补正必要。 |
| `content/docs/routes/public-transit.md` | 1—30／2139 | `cf7094434b843d3114f92062ea6b413ecf11c7cbd73dcb842644b3fe91cef751` | `9236711e34bce846489f28e4b9a35b06785fbe1e703ec7b6d0303ae72b156e26` | 去回程、付款、优惠和无障碍申请／每次预约分开，获批不等已订车防实际漏办。 |
| `content/docs/routes/retirement.md` | 1—38／3250 | `18dacc4adff2de22f6788769dded3e7202e67bcc6a7d1bb6dc82ddd11e4b880b` | `1537f4acd39965c8e2722e187e9d16bdf797319411fdff3c95e584d06dc41d13` | SSA现金与医疗、卡／费用、SSA代领、死亡与账户取用各有正确分流。 |
| `content/docs/routes/school.md` | 1—27／2710 | `4dc8aaf4cea3f05b9bf1df80574c6f721ef3e725cbb09ee2e1770afc51c6cfbc` | `78d89dd081cf38b1c2574a211d00df233a111eae0f661fa6940492193b7ed007` | 住址学年、缺件／无SSN／不稳住房、五个锚点、真实上课与IEP／504实施可继续。 |
| `content/docs/routes/start-business.md` | 1—28／1874 | `01bc3eb25ce3f93ff43a94cdb81531b888b91fb4d3154be261ed5ae9c8c2009e` | `d0518a218817c099078b5377a90283aab92144496bdaf82010c77a9915b3eebb` | 本人工作资格在此指实际经营工作权限，与主体／许可／税号／账户分别核，是必要条件。 |
| `content/docs/routes/start-work.md` | 1—34／2881 | `d07dc037c764a639ef82d4e2f1ea54b0f3c5156f82bbdead897a9f1baac73250` | `43586f538cfee75604096a17486696924c9dc564a322cebcfb24e894efb821a6` | 工作授权与I-9真资格保留；工资福利、报到和账户扣款／实际到账有确认。 |
| `content/docs/routes/tax-preparation.md` | 1—25／2633 | `63fcaef73d90a5c4d010fe0326180e6b3796678d60fea427665f56af7de3a756` | `b1fec06d367ff37c382794f911ed6c652df67f659be18023ae2fe7e68b184fb7` | 税年居民期间、联邦州与海外表件、申报付款、更正和收件各分开，未编统一期限。 |
| `content/docs/routes/workplace-rights.md` | 1—28／2071 | `b79a4058d897f49dc8d24fbfd0ee38ff90923a62e9f596ef3ef0842369eed90e` | `38db7fcfd778fccd17907d709f487ea43741ee1f92d8bae6ee53a944bf8f6683` | 实际工作关系、适用制度、雇主请求／州收入／工伤／歧视立件分别递交，获准后核落实。 |

当前待实施为P01—P08共8处／8页，70页无进一步修改建议；N01由root独立补正并已在本记录绑定最终版。本次仍是只读建议，未标旧PL账本processed／verified，未追认任何主题、工程或第一轮全部目标完成。记录落盘后整件分批真正读回，另报完整行数／字节及SHA；后续主控安装语言修订时，本人须对实际新完整入口重新读取和绑定，不能拿本表旧摘要套新文件。
