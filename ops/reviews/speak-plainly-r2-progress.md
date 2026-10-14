# "说人话"全书校对进度账本 · 第二轮（B-PL-R2）

规则与判定标准见 [ops/PROMPT-SPEAK-PLAINLY-R2.md](../PROMPT-SPEAK-PLAINLY-R2.md)。本账本是第二轮唯一进度账本；首轮已收口账 [speak-plainly-progress.md](speak-plainly-progress.md) 为历史记录，不再更新。

生成于 2026-10-14，基线 HEAD `f6170ac`（138 件全部首轮 verified，工作区干净）。SHA 口径：`open(f).read().split('---',2)[2]` 的 SHA-256；动手前先核对当前文件 SHA 与本表一致，修订后重算并更新本表。

状态图例：`pending` 待认领 ｜ `processed` 本轮有修订 ｜ `clean` 扫描后无必要修订（零修订为合法收尾） ｜ `verified` 主控验收通过。零修订文件 SHA 保持基线值。

## 验收记录

| 日期 | 批次 | 结果 | 备注 |
|---|---|---|---|
| 2026-10-14 | R2-1 | 通过 | 1 处修订（invitations-boundaries 元叙述删除＋引用移挂），15 clean；root 差分验收 [b-pl-r2-1-master.md](b-pl-r2-1-master.md)，第三静态审 [b-pl-r2-1-third.md](b-pl-r2-1-third.md) 通过；acceptance 已装条目，构建检查本批无失配 |
| 2026-10-14 | R2-2 | 通过 | 2 处修订（entry-return、status-documents 否定改正面），19 clean；root 差分验收 [b-pl-r2-2-master.md](b-pl-r2-2-master.md)，第三静态审 [b-pl-r2-2-third.md](b-pl-r2-2-third.md) 通过；acceptance 已装条目，构建检查本批无失配 |
| 2026-10-14 | R2-6a | 通过 | 23 件全部 clean、零改动（入口页首轮已收口，甲类 5 处真否定保留）；无 acceptance 条目变更 |
| 2026-10-14 | R2-5 | 通过 | 12 件全部 clean、零改动；账本 12 行与引句抽查核实；执行者标记的营地句（outdoor-planning）主控裁决保留；无 acceptance 条目变更 |
| 2026-10-14 | R2-3 | 通过 | 1 处修订（mental-health 判定示例2，另消"其其"笔误），24 clean；root 差分验收 [b-pl-r2-3-master.md](b-pl-r2-3-master.md)，第三静态审 [b-pl-r2-3-third.md](b-pl-r2-3-third.md) 通过；acceptance 已装条目 |
| 2026-10-14 | R2-4 | 通过 | 1 处修订（tax-residency 删 8840 条件空转定语，root 独立复核 §7701(b)(3)(B) 等价性），18 clean；root 差分验收 [b-pl-r2-4-master.md](b-pl-r2-4-master.md)，第三静态审 [b-pl-r2-4-third.md](b-pl-r2-4-third.md) 通过；acceptance 已装条目 |
| 2026-10-14 | R2-6b | 通过 | 22 件全部 clean、零改动；git diff 核实 content/docs/ 无改动；无 acceptance 条目变更 |
| 2026-10-14 | 全部收口 | 通过 | 138 件全部 verified；全书 5 处修订（4 主题页＋0 公共页，acceptance 5 条目滚动登记）；最终 `make check DESTINATION=.cache/production-review` 零错误零警告（140 HTML／60 主题／0 草稿），`make sync` 331 路径核验同步；遗留问题 0 项 |

## R2-1 认识美国（foundations，16 文件）

| 文件 | 状态 | 处理人 | 完成日期 | 本轮删改处数 | 当前 body SHA-256 | 遗留问题／备注 |
|---|---|---|---|---|---|---|
| `content/book/foundations/_index.md` | verified | B-PL-R2-1 | 2026-10-14 | 0 | `91bea13ca0cf7b7b6846f8231196b03d1fdf059e0afbc156a1c9f48853480804` |  |
| `content/book/foundations/communities/_index.md` | verified | B-PL-R2-1 | 2026-10-14 | 0 | `64543c7be3ab898a96815bd03924a16d10cc11b89ff97553228c6ad3b06ca4e0` |  |
| `content/book/foundations/communities/tribal-nations.md` | verified | B-PL-R2-1 | 2026-10-14 | 0 | `8618e8cd61696005770906179527571b9e1d1fb412a94e4a9ec324de6ec18412` | 存留否定式均承载真范围信息，逐处判定保留 |
| `content/book/foundations/culture/_index.md` | verified | B-PL-R2-1 | 2026-10-14 | 0 | `5827b88118e4662af086d90ded49260fbe9fba134c47fb9ec7288db29cb8010a` |  |
| `content/book/foundations/culture/invitations-boundaries.md` | verified | B-PL-R2-1 | 2026-10-14 | 1 | `b9f0e449db9e1128a7fb39345beb462079cc089a0e617acb40779c06f060abe8` | 删"教学资料把……而不是……"元叙述句，引用移挂前句（甲类·判定示例1）；链接 5+3 前后一致 |
| `content/book/foundations/geography/_index.md` | verified | B-PL-R2-1 | 2026-10-14 | 0 | `3b420436ff8a046d005f1d215a2318842508689055a9d184cb501acbdccf76ba` |  |
| `content/book/foundations/geography/regional-life.md` | verified | B-PL-R2-1 | 2026-10-14 | 0 | `e092179f5412454d3a139cd482ac19c3b955393bd3b6e614ed38e48061ee7b5a` | "并非简单把行政市标为城市"承载定义真范围，保留 |
| `content/book/foundations/government/_index.md` | verified | B-PL-R2-1 | 2026-10-14 | 0 | `c0609c0af4aa3b5c922d138857e90985a6056d3ad4b15c0fe55328d0db590c35` |  |
| `content/book/foundations/government/public-participation.md` | verified | B-PL-R2-1 | 2026-10-14 | 0 | `86f99832c159afb5224625af45da590c02679525bef9474046d50d28b81d3c11` | 否定式均防具体办理错误（登记、临时票、返票），保留 |
| `content/book/foundations/government/which-government.md` | verified | B-PL-R2-1 | 2026-10-14 | 0 | `2bba54971e426152ce774fce4804325aafdf25ed47371495eefaebe48a74dc7c` |  |
| `content/book/foundations/history/_index.md` | verified | B-PL-R2-1 | 2026-10-14 | 0 | `5f4ee1ba1398e8febaf075bb195b52f65e4a60be90f69e910bb50a8ae1a54fd0` |  |
| `content/book/foundations/history/historical-landscape.md` | verified | B-PL-R2-1 | 2026-10-14 | 0 | `3979b801f8c1aa4e0ae5d5f4c77231e11a1503c519305f2b536214cad91a2f9d` | "可以作出选择"等叙事句改写收益不足，保守保留 |
| `content/book/foundations/history/migration-society.md` | verified | B-PL-R2-1 | 2026-10-14 | 0 | `c414a20450719df9af3aef4c81366ad96bdc150fa9929021240e850b125acc30` | 否定式均承载分类/口径真信息（大迁移、波多黎各、foreign-born），保留 |
| `content/book/foundations/history/segregation-civil-rights.md` | verified | B-PL-R2-1 | 2026-10-14 | 0 | `4da2f0997e69ad6a8eebcbb259db48e6a11e9cf9f5663449b711294f24924d81` | "并非一部名称相同的全国法律"承载真分类信息，保留 |
| `content/book/foundations/world/_index.md` | verified | B-PL-R2-1 | 2026-10-14 | 0 | `17437369e796c1ac129eb5d091683e84d83f4a0a43760f120e65b86330b135df` |  |
| `content/book/foundations/world/world-connections.md` | verified | B-PL-R2-1 | 2026-10-14 | 0 | `8466c6b243b057c16f914cce3c5bc3381da5c4ac3c469dc4ef0154c77c6b5375` | "出生时不是美国公民"为 Census 定义本身，保留 |

## R2-2 日常生活（life，21 文件）

| 文件 | 状态 | 处理人 | 完成日期 | 本轮删改处数 | 当前 body SHA-256 | 遗留问题／备注 |
|---|---|---|---|---|---|---|
| `content/book/life/_index.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `c918e09156e26398b9f030e0261d6e0d74bd53bdbeb6200d2e0f7784aead9f40` |  |
| `content/book/life/community/_index.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `c50408612a46e5b3d335d1010fe0519c72359decabf8efaaf36730149334d521` |  |
| `content/book/life/community/local-support.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `7e60ff36fbef135a943c7c0aeda8cbb616773baa72cf8e14f8c14d7dcd15cce2` | 存留否定式均为真范围信息，判定保留 |
| `content/book/life/digital/_index.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `5f9a7e026da613b613ebbed4d5f2bbc35ba74dd56ae2b16fe2707f6873a96350` |  |
| `content/book/life/digital/phone-internet.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `9102337e353ebbec4ff83fb406edf2c5f0b24a30504af8d4ffef9fba9ee6597d` | "移动图不能据此确定室内信号"等否定式判定保留（常见误解，正面指示已在同句） |
| `content/book/life/documents/_index.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `704aaaa379cbeb88607481597ffcc86e5829158a4680c09917c077a8493a1ade` |  |
| `content/book/life/documents/address-changes.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `e71cd8fbbe082765e7a239552f6cfb2ecfb12c6043f59c326e7e34dc3f18925d` | 大量存留否定式均为程序性真否定（"并不等于正式改址"等），判定保留 |
| `content/book/life/documents/entry-return.md` | verified | B-PL-R2-2 | 2026-10-14 | 1 | `e0ea3b76c8ebb055f33fdbfbe45c37d80accb1cbd809a12611361b2b9803981f` | 甲类改写："这是诉讼期间救济，不能写成永久撤销"→"……不是永久撤销"（"写成"为面向写作者的措辞，事实范围不变） |
| `content/book/life/documents/numbers.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `f820a0d7fb9d38d7b6c69321f4b53b482ecf0bd1d51f316402f69f627104a5e0` | "卡上没有到期日，不能据此判断工作许可永远有效"判定保留（常见误解，正面读法已在前句） |
| `content/book/life/documents/status-documents.md` | verified | B-PL-R2-2 | 2026-10-14 | 1 | `c2897386c6b55d8f727288f241d5b12c3d68eb64b6fbc8486e0d583a15994224` | 甲类改写：D/S"并不意味着无需管理……日期"双重否定改正面"写 D/S 时仍要管理……日期"，事实范围不变 |
| `content/book/life/household/_index.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `071e36bdd181d8683e617ee39fc622892f75ed316c6ad3ec1ffa080b1282bbca` |  |
| `content/book/life/household/shopping-returns.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `b8541cd63e9eab39a42b8d26a2a1803e45121cb4affc91c3ab789d1a9355631f` |  |
| `content/book/life/household/utilities.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `fa44d2aae99a7f833556706aff8bd1ae14724c69c3368f384903b2949006221a` | "邮寄地址写着大城市，不代表所有服务都由该市提供"判定保留（指名常见错误，正面做法在后句） |
| `content/book/life/housing/_index.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `43907e8ad92ffeb0e19f5435a853a44937cf7f7f7bfded97542d4a5524d07f49` |  |
| `content/book/life/housing/buying-home.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `1232cdbdd91165c3773efb2bc3a29085cd8d589c396085b437842e79b5092671` | 交割等待期段落三个"通常"各限定一条有法定例外的独立规则，非对冲堆叠，保留 |
| `content/book/life/housing/ca-deposit.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `7485994c01ab02eba4d09e7de101a6551632aabf2b6d3da6c8b31014754a8cbd` |  |
| `content/book/life/housing/rental-process.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `c4eba9734e269439a6cb6fd7664c9335aba7d296d85d3736629f885272427e8b` | 表格内"一般不迟于"等为各州法独立期限分层，非对冲堆叠，保留 |
| `content/book/life/transport/_index.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `f384fdc389acee3cfad21be16d1cb248f1328c73f946315fded20d6551b0ab87` |  |
| `content/book/life/transport/new-resident-license.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `e3ca87c7f5c1d773710f596dc266f7031ecd62551a98e8a8c92b5758ccc9c74b` | "并非必须先住满半年""不等于必须申请 AB 60"等均为真范围信息，判定保留 |
| `content/book/life/transport/owning-car.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `9b18cf798394de12dbc2c4bd9dc017d8704d928c8088adfd4efab06c35f0f402` |  |
| `content/book/life/transport/public-transit.md` | verified | B-PL-R2-2 | 2026-10-14 | 0 | `090d4dcbe57a2096f5dcbff314a7ca21fa37075669d3601528316fe4d8816cd7` |  |

## R2-3 人生与健康（people，25 文件）

| 文件 | 状态 | 处理人 | 完成日期 | 本轮删改处数 | 当前 body SHA-256 | 遗留问题／备注 |
|---|---|---|---|---|---|---|
| `content/book/people/_index.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `ace9996fed0d24364dbed3d085502f82c44d088bc15547e80e5fe2b5898ed578` |  |
| `content/book/people/accessibility/_index.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `93d75d6e85d78ac117986cee7f5d8759eef17c78c68bda73a427dcc2a21a3740` |  |
| `content/book/people/accessibility/accommodations.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `988d870296bfba09feda32475657ea5542c321765ce5ca29ecf65a6e3f062d59` | 存留否定式均为程序性真否定（"并不因此要求提供合理便利""IDEA不适用于大学"等承载法定范围），判定保留 |
| `content/book/people/accessibility/mental-health.md` | verified | B-PL-R2-3 | 2026-10-14 | 1 | `4b81f5793c311b5ef5d933ccf2423c825464bc9050dd7d541a57acaa206c384e` | 甲类改写（判定示例2）："其其他语言口译通过电话提供，不能据此期待中文短信服务"→"其他语言（含中文）的口译只经电话提供；短信服务不含中文口译"，事实范围不变；链接69前后一致 |
| `content/book/people/aging/_index.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `cf5afe0758a1dec2c03d1b19f4618b52120d8888aa7a0029cbd3d13abd5a6f21` |  |
| `content/book/people/aging/advance-planning.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `581fc7d83f10f9f464bd0ef52c73dc25c1c01075ed186657b22884a1b9ff47f0` | 存留否定式均防具体签署/交付/撤销错误（"不等于已成为representative payee"等，正面要求已在同句），判定保留 |
| `content/book/people/aging/caregiving-plan.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `9a5cf557ecbd0ac87bcb7df0831bdac58c0cb324fbef20f5b48c27f769bd3609` | "只有财务事项的POA，不能据此取得医疗决定权"等真法律范围信息，判定保留 |
| `content/book/people/aging/death-arrangements.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `51b15e77c5314ef1bf7cab976cb83b0946ba76fd816ba51ce41e7605679cb0dd` | "按死亡发生地点找记录机关，不是按家属现住地址"等否定式指名常见错误且正面规则在句首，判定保留 |
| `content/book/people/aging/retirement-medicare.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `cc54818566e1fce18046f533d7060871b9a0b72c3ae8e1564bf9e5e697b56765` | "COBRA等不等于当前就业保障""A部免保费不等于所有医护免费"等均防高代价办理错误；各"通常"限定独立法定规则，非对冲堆叠，判定保留 |
| `content/book/people/education/_index.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `35115b431893661bff624459203da0f5156937a9fdd200e76238fed10ac85b63` |  |
| `content/book/people/education/continuing-education.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `d99c8bc5766a56450668a7a053d39c9a55813cb824bce54fa943081cc7952106` | "DACA、F-1等不会仅凭身份取得联邦资助"等真范围信息，正面路线已在句尾，判定保留；"通常需6–8周，可能更久"承载实际排期信息，保留 |
| `content/book/people/family/_index.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `f6ee28f5ed3acb447f33fe6f36d130c259118e7efcc12d27460fe0d4588ebc67` |  |
| `content/book/people/family/birth-and-first-weeks.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `0756c0d7424a31a382e3441ac9739e8a7caed57b965e908fc15e0d13b361706b` | 存留否定式均防错过加保窗口、递错材料的具体错误（"不要等出生证明和SSN寄到才开始加保"等），判定保留 |
| `content/book/people/family/childcare.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `1c45c3e7ffaa09652cafe2ec5bb0263d47f87ffa7913727b52568b5c6367672b` | 存留否定式均为安全与权利信息（"不能只等机构内部答复""不能凭诊断拒绝"），判定保留 |
| `content/book/people/family/marriage-separation.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `3dca83e2f3ca391bf144a4f6f352086b7577acfbcc58c6152432483d292101d9` | 存留否定式均为法定事实与范围（"没有固定同居年限规则""判令分债不约束债权人"），判定保留 |
| `content/book/people/health/_index.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `44a9c41c324e5b46154fc2a79474556db298dcb1243e4ea3b9a1f87e46ee125f` |  |
| `content/book/people/health/appointment-network.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `7d99bc988b333e482094362f7366994a17a988b9c4db7a222f273fff125c901d` | "批准预授权并不是付款承诺""不要等网络电话或授权手续"等防具体就医错误，判定保留 |
| `content/book/people/health/coverage-changes.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `0027fac51a855511b7301404a4aa38a121d501950a9a6c97109a29482d8848e2` | "主动终止COBRA通常不产生新窗口""60天不是随时申请都能追溯"等均防衔接空档错误，判定保留 |
| `content/book/people/health/insurance-costs.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `d682854aa03ae2c37081e8df0cac1286b8b973877513c84f5e8d86246ae94e7b` | "免赔额并非每次就诊重新扣""自付上限不是绝对封顶"等均为关键口径真信息，判定保留 |
| `content/book/people/health/medical-bills.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `b85af8f5bbaf5a130efec97c0c31022e3fcee983273d734ceefe508277cac141` | "EOB不是付款账单""医院减免不代表医生账单一起减免"等真范围信息，判定保留 |
| `content/book/people/language/_index.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `ee7aed076428f489e5d01f44678f0a498c989141ae8ce915ac887ad0b70ce35b` |  |
| `content/book/people/language/service-conversations.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `41a9d3b418c44ad20e39a326fcaa862cce6a16d3408ff7d8abf2aa747a893a6c` | 例句后的复述句为教学旁注（点明范例结构供模仿），判定保留 |
| `content/book/people/school/_index.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `0b05977b1d3e6dfa10d8117045c1e057c62a8111e9011c200762b032b9f2b079` |  |
| `content/book/people/school/school-enrollment.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `491fc6eeabdbcf76b869fa450ff3c101cad98ff9766ae54bed45d6f7b79ec1c5` | "城市名/学区字样不足以确认学校""homeless不只指露宿"等防找错学校、漏用保障，判定保留 |
| `content/book/people/school/school-support.md` | verified | B-PL-R2-3 | 2026-10-14 | 0 | `7b85c2e4a50b0355aa89980186a9103600d66abdb110a9ef90e76a113e584b71` | "请求评估与同意评估是两步""无IEP不代表排除504"等关键程序真信息，判定保留；"作出决定/作出知情同意"改写收益不足，按先例保留 |

## R2-4 工作与财务（work，19 文件）

| 文件 | 状态 | 处理人 | 完成日期 | 本轮删改处数 | 当前 body SHA-256 | 遗留问题／备注 |
|---|---|---|---|---|---|---|
| `content/book/work/_index.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `60cb9e89cff212f4a6258459ba609a8c2eb928690a6981e12fc657e9c7c0793e` |  |
| `content/book/work/business/_index.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `16cb02c9ea898e546231b7654baeb2cdd85643f7aa9e51552cf4340511bd800a` |  |
| `content/book/work/business/start-business.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `3733354f29b41084479b4b99e3cba5f81d15d9ea56841b3ef0f387d59b6529e7` | 存留否定式均防具体错误（登记LLC不加工作授权、"还没卖出东西"不免5472等），逐处保留 |
| `content/book/work/career/_index.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `45096563aeef13e6ebaa01dabae56ca310d365c0c06663c4201d89b0455c35c0` |  |
| `content/book/work/career/job-search-onboarding.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `f5c8738b3677bb8dca0c3ba73dcdf2d9c01f668360ff18de15ba570c618e42bc` | "作出不利决定/没有作出招聘决定"为FCRA通知内容标准表述，改写收益不足，按先例保留 |
| `content/book/work/employment/_index.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `c507ff0c4bc22aa517f86c67bb00f7097ff378b711b80740e2c9a05a1bbf73ec` |  |
| `content/book/work/employment/job-loss-support.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `eff07740f03d91f29d2dd376bc50d9e45268e6dcc884f2b07e1346a88c915160` | 存留否定式均防具体错误（按住址错选州、等UI决定再求助、"打过电话"当已申诉等），含判定示例3原句，逐处保留 |
| `content/book/work/employment/pay-stub-overtime.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `4fd1304b02a81b34fc93b05c3ae5d74f32bc402ccd7eff3541140dd239f2c677` | "并非所有约定工资或福利纠纷都属其范围"等存留否定式均承载真范围信息，保留 |
| `content/book/work/employment/workplace-rights.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `049c4ecee882f7ad65d2d713568d2e2df999c895b37e0f735b44fe56ee0def05` | 存留否定式均为程序真否定（FMLA本身无薪、客服咨询≠已申请听证、问卷不自动保住WSHRC期限等），保留 |
| `content/book/work/finance/_index.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `aba94642c606b6f4af5479084040caa5a15de2c202cba3ad8315d8d2a11f0acc` |  |
| `content/book/work/finance/accounts-investing.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `fdc758f7811bef7896ac5db7279b2646197340bfeaa3f3bfc3e80f41b823af7b` | "没有不允许的其他医疗保障"定语承载HSA允许/禁止保障分层，非空转定语，保留 |
| `content/book/work/finance/banking-payments.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `307522bd4e462d6c4069788e8a0c9152d43cf289c4f77eab53f0a011192535ad` | 存留否定式均防具体错误（可用余额≠支票有效、停止扣款不消灭欠款等），逐处保留 |
| `content/book/work/finance/credit-records.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `6e17c15a7c69fa7f55055f41624f0d15ed206a93bf2ad5f2894d0986c2e71d23` | 存留否定式均承载真范围（冻结不阻止现有账户接管、屏蔽只用于真身份盗用等），保留 |
| `content/book/work/finance/debt.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `4aa3f76757320f1f00023c73c3c92eb9544cfdf2a05ba8dab4406a2882f15e3f` | 存留否定式均防具体错误（停联不取消债务、余额清≠负面历史删除、投诉转送≠法院收件等），逐处保留 |
| `content/book/work/finance/food-cash-support.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `4d2a18b7f3999a42d605f0fcaa54dbc20c9ecf75fce34c92228025c647b96b03` | "请求核验协助，而不是填一个猜测数字"等否定式指名错误做法，正面指示已在句首，保留 |
| `content/book/work/tax/_index.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `a5faf17a0c4f3c1f5d7d635706d7b3b4fd1e4e7f852804744ed983966a0afb5a` |  |
| `content/book/work/tax/filing.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `2b66fb484cf9fc660ff9abc34f09e650acf939a7df68b32a78b4cf6051b616d7` | "付不起不等于可以不报""软件显示已发送不等于机关已接收"等均防具体错误；"替你作出这些判断"改写收益不足，保留 |
| `content/book/work/tax/state-residency.md` | verified | B-PL-R2-4 | 2026-10-14 | 0 | `da21ce25df2c56eb8b41f309db137a77fd51f4acfc0f149f56e5791d3ac05b81` | "而不是等下一年收到W-2才处理"等否定式指名常见错误，正面指示已在句首，保留 |
| `content/book/work/tax/tax-residency.md` | verified | B-PL-R2-4 | 2026-10-14 | 1 | `8e4a97775c002567a72441d5346496ff4e10887f7af57b8a5112db9a509e43f5` | 乙类4改写：8840四条件之3"不具有使该例外不适用的绿卡身份"→"没有绿卡身份"——该例外对任何绿卡身份均不可用，定语空转，删后事实范围等同；链接21+2前后一致 |

## R2-5 法律与环境（rights，12 文件）

| 文件 | 状态 | 处理人 | 完成日期 | 本轮删改处数 | 当前 body SHA-256 | 遗留问题／备注 |
|---|---|---|---|---|---|---|
| `content/book/rights/_index.md` | verified | B-PL-R2-5 | 2026-10-14 | 0 | `0d2f2522e347f5245498fb669c142b9c6b0a365befefbef1469e126ecbabaae2` | "具体行动还取决于事件发生地点和主管机关"点名决定因素，保留 |
| `content/book/rights/contracts/_index.md` | verified | B-PL-R2-5 | 2026-10-14 | 0 | `89b2b44b1e93e29402479fc56fd8fc3bbe9703225029b011d9f9dba4ef50b654` |  |
| `content/book/rights/contracts/reading-contracts.md` | verified | B-PL-R2-5 | 2026-10-14 | 0 | `a456a8907378760c2b1736dc3b429457f602340975e1b36a869eb5c6f1031f08` | 存留否定式均为真范围信息（E-SIGN 法定效力措辞、冷静期排除、OAG 受理分工），逐处判定保留 |
| `content/book/rights/legal/_index.md` | verified | B-PL-R2-5 | 2026-10-14 | 0 | `42ff8db81fac91d17e34843943bad2ceab1160e2d3f662eec2885cd3b5e76712` |  |
| `content/book/rights/legal/finding-help.md` | verified | B-PL-R2-5 | 2026-10-14 | 0 | `4a1ef3b78e05ed734897b889f9d4888affde0f0f656196e3ae795f46154ee2cb` | "列入目录不等于适合""notario 不因此取得移民代理资格"等否定式均防找错人的具体错误，逐处保留 |
| `content/book/rights/legal/notices-deadlines.md` | verified | B-PL-R2-5 | 2026-10-14 | 0 | `511bed06c7a676fac4d03846f0554b1bfcbaa8ec8b7c123a31a664af6063e3e1` | 期限分支的"通常"各限定有例外或分层起算的法定期限；"未收到准许改期仍按原庭期到场"等程序性真否定保留 |
| `content/book/rights/outdoors/_index.md` | verified | B-PL-R2-5 | 2026-10-14 | 0 | `588863415728f67e423e2e5c64c98a53d8a9d8184a6c9a9201005d30c02cdaea` |  |
| `content/book/rights/outdoors/outdoor-planning.md` | verified | B-PL-R2-5 | 2026-10-14 | 0 | `5e190a7790971ce0d39769e7edf962a19ff04277569e405fcc96f3572a2330ac` | "不会因租到一个营位就能在附近另辟帐篷"句式稍绕，改写收益不足保守保留，供主控复核；其余否定式均防具体错误 |
| `content/book/rights/safety/_index.md` | verified | B-PL-R2-5 | 2026-10-14 | 0 | `5570f100af63872e13fbcfaf02a931711c2b9cbb307c423bb643efaede9cadcf` |  |
| `content/book/rights/safety/disaster-preparation.md` | verified | B-PL-R2-5 | 2026-10-14 | 0 | `a0687e6b6ba5318d2f4a96b2b01cf006b0f5ddb5c3b3404be3db14310957bcb3` | 安全与资格类否定（"风扇不能作极端高温唯一降温""合法签证不能替代 FEMA 身份核验"）均为真规则，保留 |
| `content/book/rights/safety/emergency-help.md` | verified | B-PL-R2-5 | 2026-10-14 | 0 | `49a8d07854505ac39f6dc4463b7d8e36d06847089314403c8e507c5c469ee095` | "不能把中文短信当作已获得中文服务""未送达提示不能当作已受理"等否定式防求助失败，保留 |
| `content/book/rights/safety/firearms.md` | verified | B-PL-R2-5 | 2026-10-14 | 0 | `757a4e709d30fa810d07df5110e787f49ed79b1ee987b304dbb75be1cd985efb` | "免签在境者不适用非移民签证禁令""手套箱不算锁存容器"等承载法定分类与安全真范围，逐处保留 |

## R2-6 docs 入口与共享页（45 文件；入口页短小，可分两个会话）

| 文件 | 状态 | 处理人 | 完成日期 | 本轮删改处数 | 当前 body SHA-256 | 遗留问题／备注 |
|---|---|---|---|---|---|---|
| `content/_index.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `79633853cc6599ff9901367d0777440eafa18eb95ca0b2c48e918c6b10f89bc1` |  |
| `content/book/_index.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `00e7935b06f154ae27342e959ec59f52d590986f6d7335dba77b41176fa47ae7` |  |
| `content/docs/_index.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `91fdc6be08b603cc3455b9d05915d2cdfb6e6c8f729f5ed83566dbe8fae854e3` |  |
| `content/docs/about/_index.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `02cf1103ab148f823a90b6fc0a8341a36e5681e885ef7e5f7086a7dcb3670150` | 存留否定式均防误读（核验日期≠时效保证；未列出≠已覆盖），判定保留 |
| `content/docs/glossary/_index.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `db419067a098ebd151f153eb709a93fa520e7381d2d2c618e9e0fa6e22d87218` |  |
| `content/docs/regions/_index.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `fd112c8f5bfff9ffc62ca7bcab5e3bec2d1a28b8ac88e668c35cae00c4e5e4f5` | "城市名不足以替你核对管辖"指名常见错误，正面做法在前句，保留 |
| `content/docs/regions/california.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `8d78e0e732f372f694a057be6e7876ddf14d769f6e7447af63ece3f5573eec54` |  |
| `content/docs/regions/new-york.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `739fc3c01e1b0ffc6e6f8b60ae96873a104e5b62c7f57bbd9b287a433f974bd5` | "不能只凭旧地图安排路线"指名具体错误，正面指示同句，保留 |
| `content/docs/regions/texas.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `d2c2471e1c312f154ac0d99e0fb2b0e8b2433859fe4510c790f81eecb1acd975` | "不要套用其他州的替代基期"指名具体错误，正面规则同句，保留 |
| `content/docs/regions/washington.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `a54d9e7034615f6a00ef0930d8334c861677e7ad15f0f0a899b9f4653c098eab` |  |
| `content/docs/routes/_index.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `17dcf23a991587046903c91b5a5823807bbe32dccc76e1d4da142f0fe9e43c98` |  |
| `content/docs/routes/accommodations.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `b5ef96a50ae121772bf7b3d542f7d7e3600b8a606df9382997a24b0d1331e476` |  |
| `content/docs/routes/accounts-investing.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `4f2724a7d5334a560aac0a83972ef98a3a1d9e458f41b6d21da02f1ef190c5cb` | "投资可能下跌"为真实风险陈述，保留 |
| `content/docs/routes/advance-planning.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `097640e9b346a3d519c7af267e81f370223d2b75d79d6f9c60e39970cb460e8f` |  |
| `content/docs/routes/arrival.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `0938540809472e2d3075839caf93c367f4bacbe0ac217766c44bd9fce0e5bfc0` |  |
| `content/docs/routes/bereavement.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `1d1bcae9278fafe373d9d025e2dd030af10046cec93382a23605b96a29c428cc` | "不能仅凭照顾者身份推断权限"指名常见且有后果的错误，正面做法紧邻在前，保留 |
| `content/docs/routes/buy-home.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `b437f149da8502f5a8b147fd7949e1cb532986223e4c395e695033fae9e12ae9` |  |
| `content/docs/routes/caregiving.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `365a82ad91c0d15642c33d9f2a41b83e0214f9a19763a89875bf2bce88cbff26` |  |
| `content/docs/routes/childcare.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `525f89c8dcae5e7767ca98b6c565eb7701ab99e9d482a702d15348dd03b17bdd` |  |
| `content/docs/routes/continuing-education.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `2998c7d9721b4d5f5a0791344a2ebc2ac5880587c2882b31801c26dc240feb3b` |  |
| `content/docs/routes/debt.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `cd112388c5413c2b039bfb3504f291ef5330e0c75068553004adb89f36d35576` |  |
| `content/docs/routes/disaster-preparation.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `4645172706d5494b92212a0b225de16d405b92352e33e34e7ab8cb8a10d024ce` |  |
| `content/docs/routes/emergency.md` | verified | B-PL-R2-6a | 2026-10-14 | 0 | `016c586b2e592177688a7b82469d5fa75ec1f948e449bcb6cd8a06014593cfcc` |  |
| `content/docs/routes/entry-return.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `e841888ee40aba8856fe79815621bec9442ef160a650ba316d8aa888d3189cc2` |  |
| `content/docs/routes/firearms.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `8a64a13cb597e73a72da81961121eec8baac19967c8a2b294f4c090258448e4e` |  |
| `content/docs/routes/food-cash-support.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `bc2f2d2bbf0b8cb4d774b8e68a90f14ea97c22b9a281bb1d6dcbcb4f54b32bc7` |  |
| `content/docs/routes/house-services.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `e4ad823b526a6fd481692efa883f0fbd68b36fb478fa3c4b69725e33ae87f74c` |  |
| `content/docs/routes/identity-theft.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `890af7642d48adc1650b3ec1f0751819edadf42317e1a84b26007417e6189b72` | 唯一"以……为准"非括号且指名信用主题页查证入口，单处保留 |
| `content/docs/routes/job-loss.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `fe119da17550a20df5a51bf29ab3f1350deaae28e74d9228a5ad3680ee1a02e7` | "不能把申请UI当成这些程序已完成"防漏办各期限，保留；末段逐项核对清单防漏项，保留 |
| `content/docs/routes/marriage-separation.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `880e9ac75c3cea82e261e11413f624c7eed220ab54c6be31fa8531755c3cb69a` | "不要把办证地点当成有权受理离婚的法院"防递错法院，保留 |
| `content/docs/routes/medical-care.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `18c8cdc3ff5292ae6b36db66570fd4beb0843dadfec63eb0970224011d877a1c` | 末句完成核对清单防漏项；"每条程序有自己的通知、条件与期限"四程序已具名并给入口，保留 |
| `content/docs/routes/mental-health.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `440dcebbb5cd654f285c2962a40f6b4677f3d2c216f122c2bc8dcb3540011b35` |  |
| `content/docs/routes/moving.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `dc53c91d02b9de941b3f0773b73358737e00accf6088aa2b4fd2e4c7bff34c2a` | "不要用临时猜测的地址登记""提交截图只能说明当时做过什么"均为真否定，保留 |
| `content/docs/routes/notices-deadlines.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `c40138bc0f993072459056b49c518159bb5fbbfef160404d9daf0270525deb87` |  |
| `content/docs/routes/outdoor-trip.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `b6375218861a714503cc4c9dc925e801e612cf17daec8dd20c8339677af0a942` |  |
| `content/docs/routes/owning-car.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `152df334fd02fec44746bed14bc53f39180e7b70471b2b6a373f07c13cdb8b6c` |  |
| `content/docs/routes/parenthood.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `f66863da26a0f842a92d06d5416e9202286e76aa7774029f25f0e03fe75ebafe` | "各有自己的条件与期限"项目具名且落在并行提示上；完成情况清单防漏项，保留 |
| `content/docs/routes/public-participation.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `f5bae95540b4e7ebebbe1abe1628f6f06e77bcd4ddb0954cf9dac5605301f89a` | "不要等公开会议的回复代替那份文件上的期限"防错过限，保留 |
| `content/docs/routes/public-transit.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `9236711e34bce846489f28e4b9a35b06785fbe1e703ec7b6d0303ae72b156e26` | "申请获批不表示已经订好车"防漏订车，保留 |
| `content/docs/routes/retirement.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `1537f4acd39965c8e2722e187e9d16bdf797319411fdff3c95e584d06dc41d13` | "退休不会自动完成现金申请"防漏申领，保留 |
| `content/docs/routes/school.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `78d89dd081cf38b1c2574a211d00df233a111eae0f661fa6940492193b7ed007` | "不自行决定停止申请"防弃办，保留 |
| `content/docs/routes/start-business.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `d0518a218817c099078b5377a90283aab92144496bdaf82010c77a9915b3eebb` | "不跳过第一班及第一笔工资的安排"真否定，保留 |
| `content/docs/routes/start-work.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `43586f538cfee75604096a17486696924c9dc564a322cebcfb24e894efb821a6` |  |
| `content/docs/routes/tax-preparation.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `b1fec06d367ff37c382794f911ed6c652df67f659be18023ae2fe7e68b184fb7` |  |
| `content/docs/routes/workplace-rights.md` | verified | B-PL-R2-6b | 2026-10-14 | 0 | `38db7fcfd778fccd17907d709f487ea43741ee1f92d8bae6ee53a944bf8f6683` |  |

共 138 件。
