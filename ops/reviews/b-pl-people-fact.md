# People15篇语言拟稿：独立差分事实审

2026-10-14（Asia/Shanghai），修订作者root；独立事实审banking_fact。 **PASS：仅限下列15件冻结proposed的38处语言差分及全文上下文，无必要事实返修。** 本轮本人实际全文读1674行／290763字节拟稿，逐件实读15份真实diff，末轮重新独算60个旧新body／whole摘要。此结论不重做全部旧事实审，不追认原frontmatter的历史reviewed_by为本轮新审，也不代替异人第三审、canonical安装或工程／渲染。

本轮只写本审阅与事前逐具体路径`git check-ignore`的`.cache/b-pl-people-banking-fact/`本人缓存；未改canonical、original、proposed、作者manifest、共享、元数据、其他审阅；没有构建、提交、登录或对外联系。此前first20结论未套到本15件；之前医疗时效只读记录也未充作本批全文读取。

## 最终版本绑定与本人读取

输入根为`.cache/b-pl-people-proposals/{original,proposed}/`，下表路径在两目录下均按完整canonical路径嵌套；manifest本人首轮及末轮SHA均为`aac3eece66481023289c1286941b20d9aeb33910bc7882cc26c9b1df83b98863`。每件均真正从frontmatter读至下表末行，另读其旧新真实diff；旧稿并未另作15件完整事实回源。60个摘要都由实际字节独算，不抄manifest作核验；body采用UTF-8全文`full.split('---',2)[2]`并保留换行。

15件拟稿frontmatter与original逐字节相同（原已集成状态和原审阅字段不变），数字、完整链接文字／URL顺序、行数均相同。本人顺序正验精确得到proposed；在准确新offset处降序撤回38处，精确恢复original全部字节及全部旧body／whole摘要。末轮15件canonical仍与original逐字节相同。上述不变检查只作证据，下面另逐处判语义；不以数字／链接相同代替事实审。

| #、canonical路径 | 拟稿真正全读范围／字节 | 原whole／body SHA-256 | 新whole／body SHA-256 |
|---|---|---|---|
| 1 · content/book/people/health/appointment-network.md | 1—59／6490 | whole `91a9063db2e45001ae86f1250f39de4c98981041e034f9220656aacf875673e5`<br>body `4c8d3b8551eb31ed9778e29a6a5b9724ee1fbe6bbf53f9d409e8e10c85b76de6` | whole `258415ab951f71e0d91a3fe9868f797c1a34b694df6fa68212b361096e45315b`<br>body `7d99bc988b333e482094362f7366994a17a988b9c4db7a222f273fff125c901d` |
| 2 · content/book/people/health/insurance-costs.md | 1—63／6109 | whole `c59989a3ae7fc4f451f8b811679a278c93b7447f1975d491306b00c5e5289e5e`<br>body `c9ffeddbe4ab79912751089ee35114d95e5264fa211a58e9dc3ac7be0a4c5d3b` | whole `8fb6c70c98f6e54bb12d5e77abc26746d102b363b7da4ac10b75e5ee76677520`<br>body `d682854aa03ae2c37081e8df0cac1286b8b973877513c84f5e8d86246ae94e7b` |
| 3 · content/book/people/health/medical-bills.md | 1—71／8785 | whole `89d72e74ec31531fdffa889219c206fdc7b59b263738608d69bd537a3099340f`<br>body `485addc8f652f6ebe777814fa5527e8c43f406519cf50d0d809a74be90304fd0` | whole `682e5fe821e7cd4510a5ad65de77c938db45117e1dd124ce4e7e8d9395597de2`<br>body `b85af8f5bbaf5a130efec97c0c31022e3fcee983273d734ceefe508277cac141` |
| 4 · content/book/people/health/coverage-changes.md | 1—100／19238 | whole `dd093f87de1dad5a266854cec072235b006ef12d2cb04bcc584163d3c2ef79b8`<br>body `54f796e916ab7d1d0cc19fca99e8ffc8919a6bff161674e547ce17cee5da3943` | whole `7945afdad8595406aa7a566f37e665690a0c83c619d7de4909753c4e1e2a2917`<br>body `0027fac51a855511b7301404a4aa38a121d501950a9a6c97109a29482d8848e2` |
| 5 · content/book/people/language/service-conversations.md | 1—127／10697 | whole `83152695e21896beb1b547161334338ebfb781c9d00852b2f07c723fbb4f2c88`<br>body `62b636f6b67ceecfdd3d7f0800b863c39afa29a1bb3370d40b5eb8f8e0a0d41b` | whole `7b15e3d60f47f16b84044bc7020854f7391fb97c0a0f668b2d3065f12a03d76d`<br>body `41a9d3b418c44ad20e39a326fcaa862cce6a16d3408ff7d8abf2aa747a893a6c` |
| 6 · content/book/people/school/school-enrollment.md | 1—114／16904 | whole `7ed5e90f8bdf20e40f51f7701185ea7c9664b3fc81cdbe9eb66cc45a2f4a4a41`<br>body `b8a01b4ae60bdc4441c9ace62002b07b90dc47e629dd06653dea6868b1f03cc0` | whole `802832d9006f3c7f659c66d311a8cd0c557fff48a94288e1e61b64a9d5d69003`<br>body `491fc6eeabdbcf76b869fa450ff3c101cad98ff9766ae54bed45d6f7b79ec1c5` |
| 7 · content/book/people/family/birth-and-first-weeks.md | 1—95／18795 | whole `bf625b6a4897f8b27d0bc955a5095ac5dafc4b3eac8fc883fe964450f46f207f`<br>body `bb51e12f0ed73579c4f86064c2b7963c28c323ea64d7cf6425b3df355ae609b8` | whole `3631f6e4984214ef1ae4314bb99a313b00dd92081e1757fed0aad3977f80a64c`<br>body `0756c0d7424a31a382e3441ac9739e8a7caed57b965e908fc15e0d13b361706b` |
| 8 · content/book/people/accessibility/accommodations.md | 1—134／25337 | whole `11cbbe7d03520624d7ede0987bedc05b672a06f886da70f3e5da8696547fae73`<br>body `1b028fd251ea4f4878076d3cae67fc7aec940ad7e44d7637c269c4362f24db0c` | whole `37cf88df82abde8cef3fa98805a7c6afb8fbcea88ecddd33f6df742b0a82d2d9`<br>body `988d870296bfba09feda32475657ea5542c321765ce5ca29ecf65a6e3f062d59` |
| 9 · content/book/people/accessibility/mental-health.md | 1—117／23301 | whole `071e9a4abb0eff8c7b1cf4bb8be584f9ac5ba272d3fecfd6029f54f65bb8852d`<br>body `575c7d19fa70154da8672ea22f9d942a3c48fd89998f6f41ccb047a13a428917` | whole `636db970ecb8ed665da64258bf009e5bc6f0df53cb4ef329aaa9867d0eaf5366`<br>body `8b52a308ae7a27c57845818ad47800d86a0d89ce89123797893c8eaac45f05d4` |
| 10 · content/book/people/aging/caregiving-plan.md | 1—148／22774 | whole `88bc9cc0ae8e8f3cccd5ed46e9cba708d56094b64ef3b0e93aaeb2d0a3d6f638`<br>body `67cbe66df380938966b619fc692145282321bf43696522a0a682788dafc85c1a` | whole `ff03465d86b05d890acef55cc312a5c0dce16ab4b95c1136af62e240c36b4c93`<br>body `a7667b144d1aec0e555d291269b48f6b4f17879fd92b6caf65ff73b8444c02c7` |
| 11 · content/book/people/aging/advance-planning.md | 1—125／25103 | whole `6c45952220efe69f02213ddc5bd772c0d401749d7114958eff11cf32a4866941`<br>body `48c70ff0af9f63f4b21e9c2f9c85ea5a7c6ff2607d475f5ecd4cdf61312f2be0` | whole `17590e8843412abec245d6cf90985b6f7894371a8d4fb6e526e124398a8315a5`<br>body `581fc7d83f10f9f464bd0ef52c73dc25c1c01075ed186657b22884a1b9ff47f0` |
| 12 · content/book/people/aging/retirement-medicare.md | 1—148／28666 | whole `b91cd2db3b8e4566558014e28fc27b349333930d09086ee59237d4575f412dd0`<br>body `4aa59f4c2edea50131ebea65dfe3457875c5dde0c7db6292147b69f6aa6749d2` | whole `7b82213dec778d4f5fdebb63b535c30a2c9fc563b90482d854a4deb31516ee3a`<br>body `cc54818566e1fce18046f533d7060871b9a0b72c3ae8e1564bf9e5e697b56765` |
| 13 · content/book/people/aging/death-arrangements.md | 1—125／26639 | whole `1b6cd2383b8a099a468dfde0ad64f370373a4db81d913875e41e879f7a02fb92`<br>body `7f527b505e36cdd4ad519ccae92b745a3e48187f69f1e6f63f6f89b7e2244397` | whole `cc7db010c3f3a15126b5719e1adf23a3df294267fd907f65bd32927ae748a7d0`<br>body `51b15e77c5314ef1bf7cab976cb83b0946ba76fd816ba51ce41e7605679cb0dd` |
| 14 · content/book/people/family/childcare.md | 1—115／23931 | whole `5eb4d16268eee7f1f9a051b97c016ff8fe1f7d4299ef913541f403d9e6308a8a`<br>body `b207514914db15706c42fcc8ee12041b07a5fa9460e26a657353fcbf737d413f` | whole `a9f0fa70c908bc1a1a2a6d35a341dbd89422ca524c9dce7ed8c9fbb7ac6eab73`<br>body `1c45c3e7ffaa09652cafe2ec5bb0263d47f87ffa7913727b52568b5c6367672b` |
| 15 · content/book/people/school/school-support.md | 1—133／27994 | whole `61d25f70841824d0a244db43da35e9bcefd7654c383e5649efecff1fa13d3aed`<br>body `04d5ef6d12845b42122e149d02290671845bb1bfe88244470a1ae31b33c53af2` | whole `22c8dc7e343c2bca56baedbb000015f9d6996682ce7d24077848f6a516dbc1b3`<br>body `7b85c2e4a50b0355aa89980186a9103600d66abdb110a9ef90e76a113e584b71` |

## 38处真实差分位置

以下#与上表同一文件；L为本人按新旧完整文件实际定位，两版本行号相同。表列全部38处，不用摘句替代全文读取。准确原offset／新offset、顺序manifest offset、统一diff及正逆验在本人缓存`diff-report.json`／`final-bindings.json`；空串删除仍按准确offset撤回。

| #／L | 唯一原文字 → 拟稿文字 |
|---|---|
| 1／L18 | `member ID、group number（如有）` → `会员号（member ID）、团体编号（group number，如有）` |
| 1／L20 | `计划的 provider directory 开始` → `计划的医疗服务提供者目录（provider directory）开始` |
| 1／L53 | `对 grandfathered plans 另有适用限制` → `对保留旧规则的保险计划（grandfathered plans）另有适用限制` |
| 2／L20 | `与 coverage period。` → `与保障期间（coverage period）。` |
| 2／L42 | `下面是 **教学虚构** ，没有对应真实保险产品：` → `下面是 **教学虚构** ：` |
| 3／L36 | `收费机构的 billing department` → `收费机构的收费账务部门（billing department）` |
| 3／L50 | `**递交 internal appeal。**` → `**递交内部申诉（internal appeal）。**` |
| 3／L51 | `**仍被拒绝时检查 external review。**` → `**仍被拒绝时核查外部审查（external review）。**` |
| 3／L63 | `书面 good faith estimate。` → `书面善意费用估算（good faith estimate）。` |
| 4／L16 | `本页处理失去雇主保险和搬州这两种常见变化。` → 删除为准确空串 |
| 4／L84 | `；这不是所有人都被取消，也不是所有新搬入者都能加入。` → `。` |
| 5／L50 | `这是一个具体机构的服务承诺。` → 删除为准确空串 |
| 5／L127 | `先把一句来意、一个澄清问题和一句确认安排练熟，就有了下次通话能用的起点。` → `先把一句来意、一个澄清问题和一句确认安排练熟。` |
| 6／L53 | `与 counselor 核对` → `与学校辅导员（counselor）核对` |
| 6／L57 | `交给 school nurse 或` → `交给校护士（school nurse）或` |
| 6／L92 | `它不表示健康材料从此无需处理。` → 删除为准确空串 |
| 6／L94 | `**foster care liaison**` → `**寄养学生联络员（foster care liaison）**` |
| 7／L43 | `找 Wage and Hour Division，` → `找工资与工时司（Wage and Hour Division），` |
| 7／L57 | `申请 certified copy，` → `申请认证副本（certified copy），` |
| 7／L65 | `一般的 birth verification 与 certified birth certificate 是` → `一般的出生记录核验（birth verification）与认证出生证明（certified birth certificate）是` |
| 8／L24 | `找招聘负责人、主管或HR；` → `找招聘负责人、主管或人力资源部门（HR）；` |
| 8／L27 | `找Disability Services／Accessibility Office；` → `找残障／无障碍服务办公室（Disability Services／Accessibility Office）；` |
| 8／L72 | `本机构EEO Counselor**` → `本机构平等就业机会辅导员（EEO Counselor）**` |
| 8／L115 | `向EEOC提交charge，` → `向EEOC提交歧视控告（charge），` |
| 9／L30 | `雇主若有Employee Assistance Program（EAP），` → `雇主若有雇员援助项目（Employee Assistance Program，EAP），` |
| 9／L49 | `向计划索取Summary of Benefits and Coverage（SBC）或雇主计划的Summary Plan Description（SPD），` → `向计划索取福利与保障摘要（Summary of Benefits and Coverage，SBC）或雇主计划的计划摘要说明（Summary Plan Description，SPD），` |
| 10／L47 | `使用 Important Message from Medicare（IM）` → `使用Medicare重要通知（Important Message from Medicare，IM）` |
| 10／L47 | `使用 Notice of Medicare Non-Coverage（NOMNC）` → `使用Medicare终止承保通知（Notice of Medicare Non-Coverage，NOMNC）` |
| 10／L47 | `向 BFCC-QIO 提出快速申诉` → `向BFCC-QIO（负责该快速申诉的机构）提出快速申诉` |
| 10／L136 | `**Long-Term Care Ombudsman**` → `**长期照护申诉专员（Long-Term Care Ombudsman）**` |
| 11／L68 | `本页按该表走公证；` → `按该表的公证栏办理；` |
| 12／L44 | `银行routing number。` → `银行路由号码（routing number）。` |
| 12／L87 | `（服务提供者接受assignment时）` → `（服务提供者同意以Medicare核准额作为全额收费，即接受assignment时）` |
| 12／L146 | `机构给的fast appeal通知办` → `机构给的快速申诉（fast appeal）通知办` |
| 13／L119 | `墓地另核Division of Cemeteries。` → `墓地另核墓地管理部门（Division of Cemeteries）。` |
| 14／L63 | `领取Cash Assistance的家庭` → `领取现金援助（Cash Assistance）的家庭` |
| 14／L71 | `Temporary Assistance案件继续` → `临时援助（Temporary Assistance）案件继续` |
| 15／L26 | `下面是 **教学虚构** 的初评请求，不是已经寄出的信：` → `下面是 **教学虚构** 的初评请求：` |

## 差分及会改变行动的上下文判断

1. **预约网络（#1三处）：** 会员号与团体编号只是卡字段对译，group number的“如有”保留；CMS旧手册的字段例子只核术语，不被当2026统一卡格式。provider directory仍从本计划查询、向保险与诊所核具体地点。grandfathered中文说明针对原急诊保护限制；同段911和下段另一套No Surprises保护保留，未变成所有旧计划无保护。本人HealthCare.gov相关主文、CMS卡字段实际支持。
2. **保险费用（#2两处）：** coverage period是保障期间，SBC现官方所链样例首页有此字段；仅核字段，不采用样例2025价格或过期OMB栏作2026规则。删“没有对应真实产品”后仍明标教学虚构，网络内／免赔／20%及600→280算例条件均保留，未变为任何真实计划的待遇。
3. **医疗账单（#3四处）：** billing department仍是收费机构账务部门，不变成保险资格部门。内部申诉向保险方，外部审查按最终通知找独立审查者；Marketplace／其他计划及紧急并行条件仍分开。Good Faith Estimate说明是预期收费估算，单提供者／设施分别核对仍在，400及收到初始账单120日期限字节未变；本轮未重新审全部医保法律及所有旧期限。
4. **保障变化（#4两处）：** 删除开头自述不删scope中的失保／搬州对象或查阅日。L84删否定总结后，同段仍明列部分成人新申请冻结、既有成员符合规则并按时续保、儿童／孕产／原寄养例外和州资金过渡，再要求拿本人身份、原保障及通知核。本人新开DHCS采用段支持，不扩为“所有人取消”或“所有新搬入可加入”。WA法院SSI一组等原段未改，本次不冒充另审全部当期非公民细类。
5. **服务沟通（#5两处）：** 删除机构承诺总结后，免费口译仍明确写“SSA／Social Security”，随后仍要求其他机构另查实际服务，未推广成所有机构免费口译。末句删“有起点”不删练来意、澄清、确认安排三个动作。全部例句教学虚构标记与业务、账户、期限区分仍在；本轮不重新核未变的SSA语言原页。
6. **学校入学（#6四处）：** counselor／school nurse加学校角色中文；得州原法职能、WA校护士记录核验实际支持，不赋予任何人自动批准学分或接种豁免。删健康材料否定句后，紧前仍要求学校／联络员补记录、必要免疫，家长配合；立即入学权及缺件／争议安排不变。foster care liaison为寄养学生联络员，本人OEO真body198—200明确此人，原“不能把别人照顾自动套无家可归”保留。
7. **孕产出生（#7三处）：** WHD名称中文不改变FMLA的雇主／员工条件、无薪／职位与医保分工。认证副本仍由孩子出生地政府记录机构办理，申请人资格、用途和ID继续核；没有把普通复印或公证当认证出生证明。DSHS真页列certified copies与birth verifications为不同产品，中文对译未合并两者。
8. **无障碍（#8四处）：** HR为人力资源部门，大学服务办公室按本校程序而非统一新资格；原Title I人数、基本职责及大学学业要求均保留。联邦EEO Counselor与普通EEOC charge仍是两个场景，45日和180／300不互套；EEOC真主文解释charge为签字歧视陈述并请求救济，中文“歧视控告”未变成刑事起诉或一般客服电话咨询。
9. **心理健康（#9两处）：** EAP仍是“雇主若有”的雇员援助项目，要核费用与保密并另接长期治疗，未作全部雇主必有或全部长期治疗免费承诺。SBC与雇主SPD中文名称分别说明保障摘要和计划说明，仍要向计划／诊所核这次服务；DOL计划信息原文及NIMH真EAP段支持。未把旧DOL手册整套parity推为本轮2026所有规则。
10. **照护（#10四处）：** IM／NOMNC中文都处在“Medicare承保的服务过早结束”及医院／专业护理／居家医护语境，不指整个Medicare参保资格被终止。BFCC-QIO只是负责该快速申诉的机构，Medicare真原文明确独立审查承保服务是否应继续；原当天／前一日中午及自付核对不变。长期照护申诉专员帮助机构住民处理权利／照护／搬离，ACL真职能段支持；虐待另报主管、危急911仍在，不把专员当全部个人法院代理。
11. **预先授权（#11一处）：** “按该表的公证栏办理”仍只约束本文采用的WA财务500模板；紧后法律另允许合格见证、要核接收条件的路线完整保留。本人真PDF财务9—10页及本轮真RCW11.125.050(1)支持这一区分。没有把同包医疗模板生效条款或公证方式变成所有WA POA唯一法定条件；其他CA法条旧失败不被本句补齐。
12. **退休Medicare（#12三处）：** routing number只是银行路由号码、与本人账号和账户类型分开，SSA真2页清单有此字段。assignment新释义与本人Medicare主文定义一致：提供者接受核准额作承保服务的全额收费；紧前免赔额后患者20%仍保留，实际定义还保留患者免赔／共保，不意味着Medicare支付全额。2026的202.90／283及2027未公布全部费用限制均未动。fast appeal为快速申诉，原正在结束的承保医护语境及按通知办理不变，不变成所有SSA复议均有同一快速期。
13. **死亡手续（#13一处）：** Division of Cemeteries的中文仅明确墓地管理部门；NY DOH真FAQ58—66本身区分殡葬书面投诉与该部门，不扩监管类型或代办权限。IFS经办限定、SSA待遇、各法院及材料未变。
14. **托育（#14两处）：** NYC Cash Assistance为现金援助项目、找HRA，Tompkins Temporary Assistance为当地临时援助案件；都保留英文项目名和各自法域。ACS／HRA真段和县真页当前waitlist说明支持。未将普通失业、偶尔一次救急或全部现金收入等同项目资格；SIS300%继续只作续认优先例外，不改普通收入门槛、移民、服务或申诉起算。
15. **学校支持（#15一处）：** 删“不是已寄信”后，初评请求仍明确教学虚构、后续仍须真正交书面请求并保存学校收件、家长知情同意及适用时钟。未使虚构例信获得实际寄出／收件或诊断／IEP资格的证据效力；原两处SPS／CA程序补正完整保留，未重核37个旧源。

## 本轮本人真正独立读到的一级采用范围

查阅／请求日期均为本轮北京时间2026-10-14（普通请求UTC2026-10-13 22:19—22:25），与各源自己的更新日、旧PDF元数据和书稿原查阅日区分。未显示源自有发布／更新日的网页不推定日期，只记本轮查阅日。缓存原件SHA、每次normal／8888状态／DNS失败／最终URL、PDF页数在本人`source-index.json`；本人具体采用段和web等效读取在`source-read-ranges.json`。HTTP200仅说明响应，下面逐项明确实际内容；没有登录、验证码操作、表件递交或后台读取。33个普通定位URL中3个不采用，另真正web开RCW一条，合计31个独立采用URL，**不是31份全报告／整法律通读**。

| 本人源ID／实际URL | 本人实际读范围、版本与采用／失败边界 |
|---|---|
| p01 · [https://www.healthcare.gov/using-marketplace-coverage/getting-medical-care/](https://www.healthcare.gov/using-marketplace-coverage/getting-medical-care/) | 缓存main1–31完整；采用17–21目录定义及保险／诊所核对。 请求：normal:403；proxy-8888:200。 |
| p02 · [https://www.healthcare.gov/health-care-law-protections/doctor-choice-emergency-room-access/](https://www.healthcare.gov/health-care-law-protections/doctor-choice-emergency-room-access/) | 缓存main1–44完整；采用35–39急诊预批准及grandfathered适用限制。 请求：normal:403；proxy-8888:200。 |
| p03 · [https://www.healthcare.gov/health-care-law-protections/grandfathered-plans/](https://www.healthcare.gov/health-care-law-protections/grandfathered-plans/) | 缓存main1–124完整；采用16–36旧计划类别、35–82权利表。另本人web16–55，不以先前作者读源代替。 请求：normal:403；proxy-8888:200。 |
| p04 · [https://www.healthcare.gov/health-care-law-protections/summary-of-benefits-and-coverage/](https://www.healthcare.gov/health-care-law-protections/summary-of-benefits-and-coverage/) | 缓存main1–44完整；采用16–26、28–38摘要及样例链接。 请求：normal:403；proxy-8888:200。 |
| p05 · [https://www.healthcare.gov/appeal-insurance-company-decision/internal-appeals/](https://www.healthcare.gov/appeal-insurance-company-decision/internal-appeals/) | 缓存main1–55完整；采用20–33向保险方内部申诉及46后继续。 请求：normal:403；proxy-8888:200。 |
| p06 · [https://www.healthcare.gov/appeal-insurance-company-decision/external-review/](https://www.healthcare.gov/appeal-insurance-company-decision/external-review/) | 缓存main1–96完整；采用11–33独立外部审查及按通知找主管。未采用已过去10/2专项延期作为现行窗口。 请求：normal:403；proxy-8888:200。 |
| p07 · [https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/get-help/guides-resources/what-good-faith-estimate](https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/get-help/guides-resources/what-good-faith-estimate) | 缓存main1–75完整；采用9–10、32–49预期费用／单机构估算／纸件或邮件；页标Modified10/05/2026。 请求：normal:403；proxy-8888:200。 |
| p08 · [https://www.eeoc.gov/filing-charge-discrimination](https://www.eeoc.gov/filing-charge-discrimination) | 缓存main1–67完整；采用5–15签字歧视控告及25–38联邦雇员另走程序。web初开只给标题，采用的是本人的缓存真主文。 请求：normal:403；proxy-8888:200。 |
| p09 · [https://www.eeoc.gov/federal-sector/overview-federal-sector-eeo-complaint-process](https://www.eeoc.gov/federal-sector/overview-federal-sector-eeo-complaint-process) | 缓存main1–50完整；采用7–14先联系本机构EEO Counselor、一般45日及后续正式投诉不同步骤。 请求：normal:403；proxy-8888:200。 |
| p10 · [https://www.nimh.nih.gov/health/find-help](https://www.nimh.nih.gov/health/find-help) | 缓存main1–102完整分两次读取；采用69–70 human resources及EAP；Last Reviewed April2026。 请求：normal:200。 |
| p11 · [https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/understanding-your-mental-health-and-substance-use-disorder-benefits](https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/understanding-your-mental-health-and-substance-use-disorder-benefits) | 缓存选读1–55、65–135；采用92–107 SPD／SBC及问计划，不将手册全套parity义务当本轮2026实审。 请求：normal:403；proxy-8888:200。 |
| p12 · [https://www.dshs.texas.gov/vital-statistics/birth-records](https://www.dshs.texas.gov/vital-statistics/birth-records) | 缓存main127–178实际；采用139–153certified copies与birth verifications不同产品，非全部资格或费用重核。 请求：normal:200。 |
| p13 · [https://www.dol.gov/agencies/whd/fmla](https://www.dol.gov/agencies/whd/fmla) | 缓存main1行、98–205实际及同一原件Wage and Hour Division导航名称；采用99–101、180–188 WHD帮助与更新日Jan26,2026。 请求：normal:403；proxy-8888:200。 |
| p14 · [https://www.medicare.gov/providers-services/claims-appeals-complaints/appeals/fast-appeals](https://www.medicare.gov/providers-services/claims-appeals-complaints/appeals/fast-appeals) | 缓存main1–82实际完整；采用1–8快速申诉对象／BFCC-QIO独立审查，13–39 IM／NOMNC与原起点。 请求：normal:403；proxy-8888:200。 |
| p15 · [https://www.medicare.gov/basics/costs/medicare-costs/provider-accept-Medicare](https://www.medicare.gov/basics/costs/medicare-costs/provider-accept-Medicare) | 缓存main1–48实际完整及本人web10–46；采用2–4 assignment和11–18患者免赔／共保、提交理赔。 请求：normal:403；proxy-8888:200。 |
| p16 · [https://acl.gov/programs/Protecting-Rights-and-Preventing-Abuse/Long-term-Care-Ombudsman-Program](https://acl.gov/programs/Protecting-Rights-and-Preventing-Abuse/Long-term-Care-Ombudsman-Program) | 普通与8888均403；本人web真开123行，采用2–15、113职能与Last Modified10/21/2024，不称原件二进制取到。 请求：normal:403；proxy-8888:403。 |
| p17 · [https://healthweb-back.health.ny.gov/professionals/funeral_director/faq.htm](https://healthweb-back.health.ny.gov/professionals/funeral_director/faq.htm) | 缓存选读1–75、95–128；采用58–66殡葬书面投诉／Division of Cemeteries分工。 请求：normal:200。 |
| p18 · [https://www.nyc.gov/site/acs/early-care/apply-child-care.page](https://www.nyc.gov/site/acs/early-care/apply-child-care.page) | 普通与8888均403；本人web主文17–63实际；采用30–37及51–58 Cash Assistance／HRA渠道。 请求：normal:403；proxy-8888:403。 |
| p19 · [https://www.tompkinscountyny.gov/All-Departments/Social-Services/Child-Care-Assistance-Program](https://www.tompkinscountyny.gov/All-Departments/Social-Services/Child-Care-Assistance-Program) | 缓存main1–26实际完整及185–218办理段；采用8–25当前waitlist及Temporary Assistance既有案件。公告自Nov1,2025；SIS优先例外未变为普通收入门槛。 请求：normal:403；proxy-8888:200。 |
| p20 · [https://www.oeo.wa.gov/en/education-issues/school-enrollment](https://www.oeo.wa.gov/en/education-issues/school-enrollment) | normal403／8888真200原件；首次抽取main为空0行，后从自己raw严格重抽body270行并实际读191–207，采用198–200 Foster Care Liaison。web另Internal Error，不能写web成功。 请求：normal:403；proxy-8888:200。 |
| p21 · [https://www.dhcs.ca.gov/medi-cal/updates/medi-cal-changes/](https://www.dhcs.ca.gov/medi-cal/updates/medi-cal-changes/) | 普通与8888均403；本人web真原文39–387可见，采用64–89及143–156成人冻结／既有续保、儿童孕产寄养例外／州资金过渡。只差分核L84删句，不重核2027全规则。 请求：normal:403；proxy-8888:403。 |
| p22 · [https://www.ssa.gov/hlp/isba/10/isba-checklist.pdf](https://www.ssa.gov/hlp/isba/10/isba-checklist.pdf) | 普通DNS失败、8888 403；本人web真2页PDF73行，实际物理2页61–72直接入账字段，物理1页36版本Oct2024。只用于routing number，未采用其旧账户资格作为2026账户规则。 请求：normal:请求失败；proxy-8888:403。 |
| p23 · [https://assets.washingtonlawhelp.org/en/print/pdf/node/191](https://assets.washingtonlawhelp.org/en/print/pdf/node/191) | 真PDF10页；实际提取读物理1–2选段（缓存1–35）及9–10（237–315），Last Review May28,2026，财务500表Revised05/2026。仅公证栏／选项采用，未目视或全读10页。 请求：normal:403；proxy-8888:200。 |
| p24 · [https://doh.wa.gov/community-and-environment/schools/immunization](https://doh.wa.gov/community-and-environment/schools/immunization) | 缓存877行，仅实际518–537及定位734–735／815；采用524／530–532校护士核记录。其余表及新法律未全读。 请求：normal:403；proxy-8888:200。 |
| p25 · [https://files.eric.ed.gov/fulltext/ED537242.pdf](https://files.eric.ed.gov/fulltext/ED537242.pdf) | 真PDF7页；实际选页／段缓存1–35、100–117、181–240，采用物理4页107–116和6页193–208残障服务联系人。元数据Creation2011-09-12／Mod2011-09-27，不当2026全部法律依据，未目视全7页。 请求：normal:200。 |
| p26 · [https://www.nyc.gov/site/hra/help/cash-assistance.page](https://www.nyc.gov/site/hra/help/cash-assistance.page) | 普通与8888均403；本人web22–29、128–131实际，采用Cash Assistance项目／HRA及托育衔接，不重核该页所有补助。 请求：normal:403；proxy-8888:403。 |
| p27 · [https://www.cms.gov/marketplace/technical-assistance-resources/summary-benefits-coverage.pdf](https://www.cms.gov/marketplace/technical-assistance-resources/summary-benefits-coverage.pdf) | 猜测定位URL普通403／8888 404，未读、不采用。随后真正从p04现页Sample SBC链接进入p28。 请求：normal:403；proxy-8888:404。 |
| p28 · [https://www.cms.gov/CCIIO/Resources/Forms-Reports-and-Other-Resources/Downloads/Sample-Completed-SBC-Accessible-Format-01-2020.pdf](https://www.cms.gov/CCIIO/Resources/Forms-Reports-and-Other-Resources/Downloads/Sample-Completed-SBC-Accessible-Format-01-2020.pdf) | 真PDF5页；原链接重定向012825文件，实际仅物理1页缓存1–72，采用Coverage Period字段。示例保障年2025，OMB栏到2026-05-31，不作为2026价格或现行模板审批证明。 请求：normal:403；proxy-8888:200。 实际重定向：[2025样例原件](https://www.cms.gov/cciio/resources/forms-reports-and-other-resources/downloads/english-sample-completed-sbc-accessible-format-012825.pdf)。 |
| p29 · [https://tea.texas.gov/curriculum-and-instruction/learning-support-and-programs/school-guidance-and-counseling/school-counseling-general-faqs](https://tea.texas.gov/curriculum-and-instruction/learning-support-and-programs/school-guidance-and-counseling/school-counseling-general-faqs) | TEA FAQ普通／8888／web均403，未读不采用搜索内容；相应角色用实际p33法条核。 请求：normal:403；proxy-8888:403。 |
| p30 · [https://www.dol.gov/general/topic/health-plans/planinformation](https://www.dol.gov/general/topic/health-plans/planinformation) | 本人web87–94及缓存16–19实际；采用SPD说明计划／SBC汇总保障，不全读其全部ERISA要求。 请求：normal:403；proxy-8888:200。 |
| p31 · [https://www.dshs.texas.gov/vital-statistics/birth-records/birth-record-faqs](https://www.dshs.texas.gov/vital-statistics/birth-records/birth-record-faqs) | 定位Birth FAQ普通／8888均404，web不可取，未读不采用。不同产品名称已在真正p12主文列出。 请求：normal:404；proxy-8888:404。 |
| p32 · [https://www.cms.gov/about-cms/agency-information/office-of-minority-health/c2c-roadmap-documents/c2c-roadmap_english.pdf](https://www.cms.gov/about-cms/agency-information/office-of-minority-health/c2c-roadmap-documents/c2c-roadmap_english.pdf) | 真旧CMS手册18物理页；实际仅物理6页（印页8–9，缓存142–198）及封面／元数据，采用Member／Group number字段。PDF元数据Creation2014-03-10／Mod03-14，不采用示例价格、旧保险资格；未目视全18页。 请求：normal:403；proxy-8888:200。 |
| p33 · [https://tcss.legis.texas.gov/resources/ED/htm/ED.33.htm#33.007](https://tcss.legis.texas.gov/resources/ED/htm/ED.33.htm#33.007) | 真当前ED33主文1394行；实际仅47–77、109–127角色段及定位；采用§33.006(a)、33.007(a)—(b) school counselor的学校学业／课程职能，不称整章全读。 请求：normal:200。 |
| w01 · [https://app.leg.wa.gov/RCW/default.aspx?cite=11.125.050](https://app.leg.wa.gov/RCW/default.aspx?cite=11.125.050) | 本人实际130–137法条全文，采用(1)公证或合格见证两路线；条尾2026c101s2／2016c209s105。 |

## 未核边界与结论

这里只独立审38处指定差分和拟稿全文上下文，不重核全部15篇所有旧资格／金额／期限，也未把旧事实审、作者成功或普通200当自己的阅读。原引用的API版本、全部四州法规／表格、院校后台、各家庭和真人个案没有因本审被补成已核。本轮PDF仅选页提取文本或web原文读取，未作图像目视。旧PDF只核本次术语／角色／模板指定字段；其余页、2026／2027全套法律、医疗个案和全部旧parity规则未全审。未打开的TEA FAQ、错误Birth FAQ、猜测CMS PDF仍为失败，相关必要定义已经上述真正一级来源核清，不能将失败页标题或搜索摘文当补证。

38处均没有删掉会改变行动的法域、资格、时间、起算、例外、证明、递交／确认或继续程序。 **最终差分事实结论：PASS，无必要返修。** 仅绑定上表全部60个摘要及manifest；原稿、拟稿或manifest任何后续改变都需重新核相应完整绑定，不能追认旧版本。由root实际接受本记录后，另派异人静态门禁；本记录不表示canonical已经改写、正式集成、构建或渲染通过。

## 真实过程断点保留

2026-10-14（Asia/Shanghai），修订作者root，独立事实审banking_fact。本轮只写本新记录和事前核具体路径忽略的本人缓存，不改canonical／original／proposed、作者包、其他审阅／共享／元数据，不构建提交。first20结果不套本批；本批只审语言差分及全文上下文，不自称重核全部旧来源或工程PASS。

## 初始真实断点

**IN PROGRESS** 。已按正式分派开始读取people manifest，尚未实际全读本批15份proposed、独算旧新全部摘要或完成必要定义回源。root的实读及offset逆验仅是线索，不能代替本人的读取。只对实际完成的项目作结论，未读项不记PASS。

范围为`.cache/b-pl-people-proposals/{original,proposed}/`下manifest列出的15件、38处修订。逐件实读proposed全篇和真实diff、核角色／文件／程序释义及删句后会改变行动的条件；所有数字与链接不变亦须语义审。必要原作者返修只报root，不改其文件；若改稿必须另绑定新完整版本。

## 已完成读取，定义回源尚未完成

本轮已实际全文读15件proposed从frontmatter至末行，合计1674行／290763字节；独立生成并实际读完15份真实统一diff、38处准确差分。学校入学／出生两件首次合读输出截断，随后补读学校完整diff及出生全文，不将截断视为完整读取。初次机器逆验误把manifest offset当原始正文offset而断言失败，没有生成通过记录；实际核清为每次顺序替换时的**完整Unicode文本offset**后，另独立定位原稿唯一旧句及新稿对应offset，顺序正验与降序逆验均精确恢复原始字节。不是在proposed中搜索通用句号来撤回。

manifest本人实算为`aac3eece66481023289c1286941b20d9aeb33910bc7882cc26c9b1df83b98863`；60个旧新body／whole摘要均与输入相符，15件canonical与original逐字节相同，FM、数字序列、完整链接文字及URL序列和行数均不变。机器结果在本人已忽略缓存`.cache/b-pl-people-banking-fact/{bindings-initial,diff-report}.json`，这些一致性检查不代替38处语义判断。必要一级定义尚在本轮独立回源，本节不作最终PASS。
