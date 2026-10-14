# 公共入口八件拟稿：独立差分事实审

- 审阅日期：2026-10-14（Asia/Shanghai）；修订作者 root → 独立差分FACT birth_fact → 后续第三 static_editor，三名不同参与者。
- 结论： **PASS（只绑定当前八件拟稿的有界差分事实审）** 。本人真正完整读八件proposed全文222行／17744 bytes及八份从原／拟真实字节生成的unified diff，逐件判断；无必要原作者返修。
- 本人完整读 `ops/reviews/b-all-public-author.md` 52行／7801 bytes，独算SHA `5f70eb39acba321e35b1cc85884e7b817d1f4fad571d83d039939dc890a60ea7`；该记录的root回源只属于作者，不能当本人的实际来源阅读。
- 本人实际读冻结入口 `.cache/b-all-public-proposals/manifest.json` 8075 bytes，SHA `94e575d3ca6754ab471a879d741aca0797174330b7a40a261da18a91b822eb08`。
- 八canonical目前逐字等于original，未实施拟稿。本人独算32个原／拟body与whole SHA并逐项匹配manifest，按实际character offset正换及逆换精确恢复原／拟；frontmatter、全部数字、普通链接文本／URL序列均未变。body使用UTF-8全文 `split('---', 2)[2]`，保留前导换行；whole使用完整原始字节。
- 本结论不是全部旧主题或78入口的事实重审，不包括people15的第三审，不表示候选／工程／渲染通过。本人只写本记录及事前核忽略的自有缓存；未改canonical、原件、拟稿、作者包、元数据或共享，未构建／提交。

## 真实读取断点与范围

开始时本人全读作者记录、manifest、八拟稿及八diff，核32摘要后保存IN PROGRESS；P04／P06／P07／P08的正文承接和一级采用段尚未读取，不提前PASS。随后实际读下面五个正文／路径件的指定范围，并亲自新请求和实读五个一级URL，最后再核当前冻结与全文读回本记录。

PROMPT第七节及 `ops/PROMPT-SPEAK-PLAINLY.md` 已在本轮前20第三审实际读取，继续按适用对象／法域／期限／文件／例外的位置及具体防错作用判断。引用正文与本人的一级抽核分别列出，不把原件加载、下载或HTTP200直接登记为阅读。

## 八件真实原／拟路径与大小

| 编号／canonical | 实际original_file | 实际proposed_file | 原行／字节 → 拟行／字节 |
|---|---|---|---|
| P01 `content/book/foundations/culture/_index.md` | `.cache/b-all-public-proposals/original/content/book/foundations/culture/_index.md` | `.cache/b-all-public-proposals/proposed/content/book/foundations/culture/_index.md` | 17／742 → 17／655 |
| P02 `content/book/people/_index.md` | `.cache/b-all-public-proposals/original/content/book/people/_index.md` | `.cache/b-all-public-proposals/proposed/content/book/people/_index.md` | 28／2155 → 28／2089 |
| P03 `content/book/work/employment/_index.md` | `.cache/b-all-public-proposals/original/content/book/work/employment/_index.md` | `.cache/b-all-public-proposals/proposed/content/book/work/employment/_index.md` | 21／1359 → 21／1299 |
| P04 `content/book/people/education/_index.md` | `.cache/b-all-public-proposals/original/content/book/people/education/_index.md` | `.cache/b-all-public-proposals/proposed/content/book/people/education/_index.md` | 19／1141 → 19／1153 |
| P05 `content/docs/routes/food-cash-support.md` | `.cache/b-all-public-proposals/original/content/docs/routes/food-cash-support.md` | `.cache/b-all-public-proposals/proposed/content/docs/routes/food-cash-support.md` | 26／1654 → 26／1591 |
| P06 `content/docs/routes/_index.md` | `.cache/b-all-public-proposals/original/content/docs/routes/_index.md` | `.cache/b-all-public-proposals/proposed/content/docs/routes/_index.md` | 51／5733 → 51／5739 |
| P07 `content/docs/routes/caregiving.md` | `.cache/b-all-public-proposals/original/content/docs/routes/caregiving.md` | `.cache/b-all-public-proposals/proposed/content/docs/routes/caregiving.md` | 36／3147 → 36／3168 |
| P08 `content/docs/routes/medical-care.md` | `.cache/b-all-public-proposals/original/content/docs/routes/medical-care.md` | `.cache/b-all-public-proposals/proposed/content/docs/routes/medical-care.md` | 24／1936 → 24／2050 |

## 八个实际差分的判断

| 编号／实际拟稿行 | 已读语境、核验与结论 |
|---|---|
| P01 文化导读L15 | 只删归纳全国性格的比较评语；同句仍要求看双方关系和眼前安排，L17保留虚构对话及愿意做什么／需要确认的条件。没有把礼节当全国统一习惯，也未删办理资格或具体事实；PASS。 |
| P02 people导读L16 | 只删家庭／学校／照护也应逐项确认的泛指；同段保险、诊所和账单的实际分担／预约／核账仍在，L18—28各出生、学校、照护、学习、心理、便利、婚姻和退休承接保留；PASS，不重判这些旧主题全部资格。 |
| P03 employment导读L19 | 只删休假保障按项目分别判断的收尾重复；L21就在请求处核实际工作关系、适用资格和收件人，并分雇主安排／州收入／工伤／EEO正式提交与各自记录。删除后没有统一雇员或默认有薪资格；PASS。 |
| P04 教育导读L17 | 不明白的“继续顾问计划”改为与顾问确认学习计划，再注册、付款、开始上课。继续学习正文L54—59具名学院流程及L113列教育计划／课程登记直接承接；L115—121核资助实际支付、本人缴费截止、首次出席和毕业。导读仍按实际学校／对应学年办理，没有新增全国统一预约、费用或无条件录取；PASS。 |
| P05 食品路径L26 | 只删一项食品申请不等全部生活支持的比较。L14—22仍有当下帮助、成员分别申请、收件／面谈／补件／领取和听证受阻；L26仍分UI／医保、债务、住房、服务中断和医疗账单。无资格、非申请人材料或持续领取动作删除；PASS。 |
| P06 路径总入口L34 | 只改请假／工伤／歧视这一条“工作资格”为“相应项目资格”。当前职场公共路径L18—28及权利正文L20—27、39—49分别核工作关系、FMLA覆盖和本人条件、州付款与投诉收件；不是把一般移民工作授权当所有保护或补收入的门槛。其他入职／开业路径L33／41未改，未由本改字取消其适用工作授权要求；PASS，不判某个非公民的全部项目资格。 |
| P07 照护路径L28 | “工作资格”具体改为“相应休假或收入支持资格”，仍分别核家庭关系、雇主通知和收件，获准休假／现金支付／家人照护各有确认。职场正文L39—47的无薪岗位保护、L62—86四州制度／承保与收入差异仍明确；本人DOL及EDD采用段支持不能用单一工作授权替代这些项目条件；PASS。 |
| P08 医疗路径L21 | 不再等全部EOB和账单到齐；先存收据，对账单与已付记录，保险使用者对EOB、未用保险者对书面估算；缺资料联系收费机构或保险方，继续核实际付款／申诉期限。两版账单正文L36—43有未收理赔／错误资料的联系、是否暂缓催收须确认及电话不暂停期限；L47—55分实际保障，L63分未用保险估算，L69—71接经济困难／完成结果。CMS及HealthCare新实读支持分流；PASS，未增统一期限、自动停付或争议必准。 |

### P08的实际边界

医疗路径L14先分紧急与计划性服务，L18先紧急求助，L20才承接计划性服务和书面估算路径。CMS明示急救不会取得这项估算，某些未预期护理也不在估算；P08没有声称紧急就诊一律有估算、没有承诺拿不到估算也可使用联邦争议。缺少文件应联络和核程序，不靠“等齐”延后事项。

CMS书面估算／争议及HealthCare保险申诉有各自起算；已有拒赔通知时，一边查收费或补资料，一边保住适用申诉期限。电话联系不自动改付款安排，账单部门的暂停／还款安排要取得确认；同段“付款或申诉”按本人适用事项核，不能读成二者有重叠时任意放弃其中一项。当前入口和两版正文未增加一个覆盖所有保障的统一时钟，也未把普通电话等同正式联邦争议中的收款限制。

## 实际读取的正文／路径依赖

下面是本轮本人实际文件摘要，不将过去本人或他人已审的状态代替此次读取。继续学习只读列出的37行；其他四件按所列范围全读。

| 实际路径 | 本人真正读取范围 | 全件行／字节 | 当前body SHA | 当前whole SHA |
|---|---|---|---|---|
| `content/book/people/health/medical-bills.md` | 当前账单正文，完整1—71 | 71／8705 | `485addc8f652f6ebe777814fa5527e8c43f406519cf50d0d809a74be90304fd0` | `89d72e74ec31531fdffa889219c206fdc7b59b263738608d69bd537a3099340f` |
| `.cache/b-pl-people-proposals/proposed/content/book/people/health/medical-bills.md` | people账单拟稿，完整1—71；另实读两版真实diff | 71／8785 | `b85af8f5bbaf5a130efec97c0c31022e3fcee983273d734ceefe508277cac141` | `682e5fe821e7cd4510a5ad65de77c938db45117e1dd124ce4e7e8d9395597de2` |
| `content/book/people/education/continuing-education.md` | 继续学习，实际1—14、50—59、111—123；不是全144行 | 144／28502 | `d99c8bc5766a56450668a7a053d39c9a55813cb824bce54fa943081cc7952106` | `5fc71898d9c5b1e0dc65ecf82271c66ca8981d0b863f6d02f577cd1fcfe107af` |
| `content/book/work/employment/workplace-rights.md` | 职场权利，完整1—137 | 137／26280 | `049c4ecee882f7ad65d2d713568d2e2df999c895b37e0f735b44fe56ee0def05` | `325c2509ab16ecb66e06ce2b94ceab8c61349be0e5ec4a94da7d90c452e17916` |
| `content/docs/routes/workplace-rights.md` | 职场公共路径，完整1—28 | 28／2071 | `38db7fcfd778fccd17907d709f487ea43741ee1f92d8bae6ee53a944bf8f6683` | `b79a4058d897f49dc8d24fbfd0ee38ff90923a62e9f596ef3ef0842369eed90e` |

## 本人一级源：实际请求与采用段

五个采用URL均由本人在2026-10-14新请求并实际读取。CMS和HealthCare不是借用作者返回，EDD和DOL不是借用职场旧作者缓存；没有进入真实账号、申请、提交、付款或联系机构。

| 一级URL | 本人方法、真正采用段／版本 | 支持与限制 |
|---|---|---|
| [DOL Fact Sheet28](https://www.dol.gov/agencies/whd/fact-sheets/28-fmla) | web403；普通verified TLS直连403；正常8888新请求200后保存真HTML并完整读抽取main1—232。页内Revised March2025；重点1—43雇主／本人／关系，103—143无薪及通知／认证，144—194岗位、医保、特别人员和州法，207—232主管／指南性质。 | 支持FMLA的项目资格、无薪岗位保护和雇主通知，不是一般移民工作授权的同义词。不作为各州现金计划、全部2026身份或专家程序的重新资格审。 |
| [EDD PFL资格](https://edd.ca.gov/en/disability/Am_I_Eligible_for_PFL_Benefits/) | 本人trueweb主文159行，实际读4—82；重点13—21收入损失／工作与CASDI工资、公民或移民身份非资格因素，25—37申领及照护证明，79—82特别学校雇员分支。当前公开页未列修订日期。 | 支持相应州收入项目应分别核定、照护申领有自己的材料／收件；没有由CA推定四州或所有非公民项目都相同，不把网页提到的金额／天数新增到八入口。 |
| [CMS未使用保险](https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/know-your-rights/without-insurance) | 本人trueweb857行中的实际主文683—803，最后修改2026-10-05；重点685—735对象／计划性估算及急救例外，740—759单一提供者和书面估算，764—786保存比账及争议时钟。 | 支持未用保险时以已有书面估算核账；没有估算不能当然走这项联邦争议。没有新增入口金额、统一期限或急救取得估算保证，未开PDF例子／争议资格子页或实际启动程序。 |
| [CMS读EOB](https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/get-help/guides-resources/read-explanation-benefits) | 本人trueweb810行中的实际主文683—756，最后修改2026-10-05；重点694—714 EOB用途／服务与理赔信息，721—739支付／余额及EOB可能未反映已付金额。 | 支持保险EOB不是账单，核已付收据与收费余额、向提供者问差额；未开EOB示例PDF、没有对某个真实账单算应付。 |
| [HealthCare内部申诉](https://www.healthcare.gov/appeal-insurance-company-decision/internal-appeals/) | 本人trueweb60行全读；重点18—28拒赔通知与申诉，29—37 EOB／资料／电话记录，48—55书面结果和加急。未列修改日期的当前公开说明。 | 支持保险程序按适用拒赔通知核期限和材料，普通联系不代正式申诉；当前账单正文已限Marketplace说明，并让Medicare、Medicaid和雇主保障另走相应通知，不将其期限扩到所有保障。 |

DOL真实失败／成功边界：本人web和普通直连403均无主文。第一次普通8888虽200，但本人的检查器误期待全大写“ELIGIBLE EMPLOYEES”，实际只有普通大小写；只打印约500字符且未保存主文，故不计已读。本人修正这个检查后以普通8888独立新取真原件，完整打印并实读main232行才采用；没有关闭TLS或绕挑战。采用HTML93890 bytes，SHA `566d579f02eea4e88fd2217b2d591a5b61a9ff0a1b6efa062b5ac86a8e6fd4fe`；提取文本232行／11047 bytes，SHA `f975627262b187909d3c4d09ce2257b0f0b6c5c8cc00a6977c777b8bc2d993eb`。缓存 `.cache/b-all-public-fact-birth/dol28.html`／`dol28.txt`／`dol28-attempts.json` 写前逐件 `git check-ignore -v` 真正确认 `.gitignore:2:.cache/`；失败和两次200的原件摘要保留在本人attempts，首200不冒作全文已读。

作者记录的另一DOL“how-to-talk”失败不是本人的本次尝试，不写成本人失败或成功；本人选择职场正文实际采用的Fact Sheet28支持此有界差分。教育初次rg定位输出曾截断，随后本人真正完整显示并读1—14／50—59／111—123，未将截断段当全文。

## 结构与未核范围

本人真实核32摘要、八个位置正／逆换及全部数字／普通链接，标题层级、列表结构不变；P08只扩同一条步骤，中文加粗外侧空格仍在。八件共71个绝对站内链接／58个不同目标，本人定位实际canonical目标并读取frontmatter，均integrated／draft false；没有将58个目标的存在冒作58全文或旧来源实审，未做本轮渲染。

保留未核：八入口所指全部旧主题、四州所有福利／工伤／EEO资格和数额期限、个人移民工作授权或医疗判断、全部教育学校及资助、实际保险合同／拒赔／付款协议、GFE争议子程序／PDF、后台表件与个人结果均不是本轮全量再审。五一级的采用范围只支持本次改字和分流，没有承诺任何非公民、照顾者、患者或学生一律获批，也不确认个案申请已经生效。

## 八件原／拟冻结32摘要

每行依次原body、原whole、拟body、拟whole，均由本人从实际字节算得；八canonical仍逐字为原件。这八件当前拟稿承载有界FACT PASS，后续第三仍待static_editor真正审阅，people15第三未纳入。

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

最终无必要原作者修改请求。若任一拟稿字节改变，需按新的差分和完整摘要重绑；当前PASS不表示主控已经实施、安装候选、构建、实际渲染或全书验收。本记录最终全文实际读回后交root，后续第三和工程由正式分派处理。
