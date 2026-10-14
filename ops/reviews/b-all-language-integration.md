# 全书语言修订：正式集成与实际工程验收

2026-10-14，root。当前138源件（60正文主题＋78公共页）的语言验收完成。43件共76处修订已安装并通过实际构建、浏览器检查、指定截图及打印选页检查、生成目录同步；35主题修订正式登记，95源件及另外25主题旧账不变。本记录只对下表实际版本及语言差分负责；全书领域与情境收口另见 [首轮验收](first-round-acceptance.md)。

## 真实版本与三人门禁

修订前HEAD为 `7425c62c905e9de3ea3597568e411569d227222e`；138件基线SHA `db943d71cb4d7607c1b25e4eb4db758c8e10d12f427032ded9e5d69239eb65d5`。旧67件初始队列已原样加归档说明保留于 [历史账](speak-plainly-progress-legacy67.md)，不能用旧pending当当前状态。当前 [138件逐项账](speak-plainly-progress.md) 已由root真正全文1—152读回，逐件当前body与实际源字节核对，verified138／pending0／hold0。

35正文共68处由root修订，banking_fact独立差分FACT通过后birth_fact第三静态审；其中前20共26处、人生15共42处，照护v2包含四个ASCII留白。四留白另有root作者补正、banking_fact新FACT及birth_fact新版第三，原v1FACT按当时范围冻结。8公共页共8处为root→birth_fact FACT→static_editor第三。作者、事实审、第三人为不同参与者；root随后安装元数据并做工程，未把自己的作者身份当独立审阅。

root已真正完整读回作者／事实／第三记录，核各个实读范围和当前摘要，再检查正逆换、数字、普通链接、标题、行数、适用对象及限定上下文。新正文与最终proposed body逐字一致；安装后whole与proposed whole因verified／reviewed_by两字段更新而区分。32主题更改两字段值，三主题只更改reviewed_by值；其余元数据语义不变。8公共页元数据不变。查阅日期更新只表示此次有界差分审阅，不能推出所有旧外引又重新打开。

| 正式审阅／作者输入 | 当前整件SHA-256 |
|---|---|
| [b-pl-revision-author.md](b-pl-revision-author.md) | `353435062a3cb0d35da525ab2ff656b3ebce600daf7c058c7bb05fa898cb2dd8` |
| [b-pl-first20-fact.md](b-pl-first20-fact.md) | `a4a0fb76049aaa770b5a8f49377528a18ea34ed2a065c81528f740855bcc9378` |
| [b-pl-first20-third.md](b-pl-first20-third.md) | `6f9999b22a914d69b861dc31a6b7af52765f9db8b63c445c8c30a20a2125c826` |
| [b-pl-people-fact.md](b-pl-people-fact.md) | `ceb1065ca3aca0ebd244bed01c58aee9343db331b38a04b769b77f43d62079d4` |
| [b-pl-care-spacing-author.md](b-pl-care-spacing-author.md) | `0a2e36746a7270bb1e1457c9dd389d28b05b74d20a1159700a883ec5b819c348` |
| [b-pl-care-spacing-fact.md](b-pl-care-spacing-fact.md) | `6c7facb654bdc399c61a39fb8c899dabb6796e2e2fd2fe5233c7ecae65397937` |
| [b-pl-people-third.md](b-pl-people-third.md) | `2ea801ff29d81d1a1ce7fb3791fa4fcbb56bedb0466fffb01f31844b94856f91` |
| [b-all-public-author.md](b-all-public-author.md) | `5f70eb39acba321e35b1cc85884e7b817d1f4fad571d83d039939dc890a60ea7` |
| [b-all-public-fact.md](b-all-public-fact.md) | `2683a86135a2349cabaedde7f1bfaf77be63bc5e6e626090bde4a40138c80efe` |
| [b-all-public-third.md](b-all-public-third.md) | `5d35930f9f3c86da2f61cdfa597a1fb9e2b8f6666889b13747c4119ffa567855` |

54既有正文全文语言走查的四组记录、78公共页全文走查及未修订新增六篇保留在逐项账的链接中。那是各执行者的真实旧全文／选段范围；root接受这些记录不称自己全读全部138旧源或全量刷新事实。当前每件body见逐项账，25未改正文的原作者及审阅记录保持。

## 实际工程、浏览器与目视

- 实际 `PATH="$PWD/.cache/checks-venv/bin:$PATH" make check DESTINATION=.cache/production-review` 成功：Hugo0.166.0 Extended、OINK固定f8f476e660cf053a2645b7b923ae8d08d5448fce，140 HTML／60正式主题／0草稿／0错误，生产零警告。未改模板、配置、工程脚本或依赖锁。
- `US_PREVIEW_URL=http://127.0.0.1:24146 US_REVIEW_CONFIG=ops/reviews/b-all-browser-scope.json node .cache/scripts/b-all-check-browser.mjs` 实际通过：138 URL桌面／手机共276次访问，32次检索、8项交互、0错误。页面H1、实际范围／日期、正文与元数据、内部承接、表格和溢出分别检查。打印DOM94内容单元、60范围元数据、2643外链、0坏锚点；外链计数不是全部外链访问成功。
- 补充脚本实际通过：76改动手机段＋76桌面段共152次文字定位，8公共页两端16项，84手机表格，0错误。段落定位使用最终V3原文，不把匹配任意句号当读到了改动。
- root实际显示并查看205主／补充网页图：76手机改动段、35改变主题两端70图、8公共页两端16图、43公共／交互图。另补拍并实际查看桌面／手机HSA及信用查询共4图，等待搜索250ms进入动画完全结束；computed opacity=1、白色背景且无活动动画，搜索结果清晰。早期过渡截图保留，但不作为最终不透明面板判断。
- 打印PDF实际318物理页，root逐张实际查看105个指定页，覆盖目录、72处进入打印稿的改动段、39个改变内容单元首尾及特定表格／元数据边界。四个docs入口不进入书本打印，故打印改动72处／改变单元39，并非漏核76处／43源件。表格表头、完整行、引文和中文加粗未见裁切；指定最后段未见孤句。
- 仅查看指定105页，未称逐页目视318页。部分完整章末段后仍留白，包括20、160、197、223、247页；未承诺消除所有页尾空白。长网页缩略图只支持结构观察，具体文字与改变段用独立定位、手机图和实际上下文判断。
- 实际 `PATH="$PWD/.cache/checks-venv/bin:$PATH" make sync` 通过331个文件路径核对；root另独立lstat及全文SHA复核两个完整树：479路径＝331文件＋148目录，0软链接，类型、大小及摘要全部相同。随后实际 `python scripts/check_site.py --public-dir public` 再通过140 HTML／60主题／0草稿／0错误。

附加 `git diff --check` 实际退出2，唯一提示是state-residency第14行末尾的一个ASCII空格：该处语言替换删去自述句后保留中文加粗外侧留白，按正文格式约定接受。没有将这项检查写成零提示，也未为消除该提示改动已审源字节；生产和项目检查的零错误结果如上。

上述命令各按真实已完成结果登记；生成文件、截图、PDF、报告和依赖均存忽略的.cache／public，只有轻量记录和源文件进入Git。浏览器使用自己创建的隔离headless Chrome及项目预览，没有读取个人浏览器或账号。preview进程最终状态见 [当前检查点](../CHECKPOINT.md)，只关闭自己拥有的24146。

## 结果绑定及失败边界

| 实际原始报告／产物 | SHA-256 |
|---|---|
| `.cache/reports/b-all-candidate-install.json` | `4f8640de015b141f49b1e8ed88dec1a2b7a163a734ab8fa977ab9b4716972984` |
| `.cache/b-all-candidate-gates.json` | `dc39f9137e4254d553d934a5beded7aabc32fc376c4791a90ef4f8bc455a0085` |
| `.cache/b-all-language-browser-report.json` | `04920b0d815d948d800a8f33e43537a2dea0f8a532e4ad7a698b8714846da930` |
| `.cache/reports/b-all-extra-browser.json` | `12c7c860f2a8987c1505712303ef00a6611c5eed93fe1f8e3fb8e8a771484e5e` |
| `.cache/b-all-language/render/book-review.pdf` | `51d66e7338af8ea001395eaa3bbd035203bb82695e43407e43b8fb273ad88136` |
| `.cache/reports/b-all-pdf-index.json` | `4c10485a283b193b0b788df682a8ee46b58b2cf514d3563e11649bc3b369bc71` |
| `.cache/reports/b-all-pdf-images.json` | `fef871b5bc80e206705e0078585f33c47ab0d08edfd76e853e60815fe1b45cc0` |
| `.cache/reports/b-all-root-visual-read.json` | `e133830c8bb75a8b1b433e97dc6019cd48ed6a733d85a12a7d4f29a9472ee5be` |
| `.cache/reports/b-all-search-settled-root.json` | `f9319a3b9567234bb5d191ca556a391d1b4b97556b16612a466b411c164f148f` |
| `.cache/reports/b-all-independent-sync.json` | `c644969460d4245a139fc281dd4876c4b3b31125076ae04eac79722ca366a53b` |
| `.cache/reports/b-all-formal-registration.json` | `84912bf291532a51c813775f641f175a43752fafffd1168a181f379748862010` |
| `.cache/reports/b-all-public-post-integration-check.json` | `0928667218a200483390592946385176f4633e51e8da01bdb012c99a0ffc26fc` |
| `.cache/reports/b-all-final-language-progress.json` | `9158a87843690491d1f4156eb166608714dbb8aa4e7c8fb75e746df245beb933` |
| `ops/reviews/speak-plainly-progress.md` | `7873f86bacd4b224256754b9b09c16723b633b29f44afbb3916c24858d0f815d` |
| `ops/reviews/speak-plainly-progress-legacy67.md` | `3f0536cc80d10f5c9409bbe6f19135b762d010bf9fb96b4f4865dae9a5bd33e1` |

raw浏览器／图像生成报告保留generated-only／root未读标志；root真正显示后的205＋105＋4记录单列，不倒改原始报告。最终目视记录绑定真实图像SHA及PDF，而不是将截图存在当已读。同步独立记录还绑定最终目视记录。

失败也按真实历史保留：领域旧表两处摘要错字首先拒收、后逐项修正再实读接受；四个早期句号片段定位已更正为实际原文；PDF首版按标题子串最后命中错把第309页交叉引用当正文第26页，assert失败时未生成图。随后使用PDF真实named destination并核正文页标题，94单元／39改变单元／72段／missing0、105选页才实际生成和查看。修正定位工具不改PDF、正文或浏览器事实。各原始失败与更正详情保留在对应冻结审阅和.cache报告，不能把第一次失败记成通过。

独立来源的403、超时、输出截断、选段及未打开PDF／私人门户边界仍按原审阅保留；本次语义限定审不改旧来源成“全部新事实通过”。公民／非公民、四州及城乡服务范围未合并。医疗P08新版已安装，账单核对不再要求先等资料全部到齐，并保留真实付款／申诉期限。

候选安装报告仍标candidate，准确表示当时安装阶段；新正式登记报告在实际工程／目视／同步通过后只将35账条目的integration_status变为integrated，未改另外25旧条目。candidate ledger SHA为 `d6f1abe408a0030a2bb80389a3c6e9b1ba2f36762cb8c09b28e41f4fa73228f3`；正式ledger SHA为 `3ba0f4232a3d7c92eb39d9338d5f4ce08d48ff326e4da70a7bb9cc927202df00`。正式条目保留previous_acceptance、原整件与各独立差分审记录。

## 43件最终实际版本

下表为安装后的canonical，whole不沿用安装前拟稿。逐项从当前真实源计算，与安装报告、138进度账及35正式主题总账核对一致；另外95源件whole严格等于修订前基线。

| 实际源路径 | 改动处数 | 当前body SHA-256 | 当前whole SHA-256 |
|---|---|---|---|
| `content/book/foundations/communities/tribal-nations.md` | 2 | `8618e8cd61696005770906179527571b9e1d1fb412a94e4a9ec324de6ec18412` | `b23e7ae4b4fcbb827afd8998cd7d4a699c36b6710acd77b00da9941400782143` |
| `content/book/foundations/culture/_index.md` | 1 | `5827b88118e4662af086d90ded49260fbe9fba134c47fb9ec7288db29cb8010a` | `4853a89546fff6e95699af7fbd9d002b8b6a8562ec4e49d818ed31c50a6803fd` |
| `content/book/foundations/culture/invitations-boundaries.md` | 4 | `56a9c74590f03b0447e5e46859b3ed18efcd44f2cfb1e62e2b1d77966d0297d1` | `26ccf5c693c1f2344423199aa169c56fc85ad07f6db0a368c273fbb50bdf3417` |
| `content/book/foundations/geography/regional-life.md` | 1 | `e092179f5412454d3a139cd482ac19c3b955393bd3b6e614ed38e48061ee7b5a` | `3306c6a87bc77c9434ec19b4b878fb0c6b6a3fc0be223b54b02661031e7334ea` |
| `content/book/foundations/history/segregation-civil-rights.md` | 1 | `4da2f0997e69ad6a8eebcbb259db48e6a11e9cf9f5663449b711294f24924d81` | `3ae210e653a5f1eef736eba8c07918ecacee7dfeaac30b15de08f341edc46169` |
| `content/book/life/community/local-support.md` | 1 | `7e60ff36fbef135a943c7c0aeda8cbb616773baa72cf8e14f8c14d7dcd15cce2` | `1ea91a414b9550d6e9603ef22745e513d26f85ffcb411efe591b505e8a3a1276` |
| `content/book/life/digital/phone-internet.md` | 1 | `9102337e353ebbec4ff83fb406edf2c5f0b24a30504af8d4ffef9fba9ee6597d` | `a834e42d0c5aade73db02918091ab682f2092167bd56d54f96029f133804f2f3` |
| `content/book/life/documents/address-changes.md` | 1 | `e71cd8fbbe082765e7a239552f6cfb2ecfb12c6043f59c326e7e34dc3f18925d` | `72b4d0796ecd91ae965f6cc215bbeab3bac4d485d6637f10eb99b0a037b331a4` |
| `content/book/life/documents/numbers.md` | 1 | `f820a0d7fb9d38d7b6c69321f4b53b482ecf0bd1d51f316402f69f627104a5e0` | `c2857253b7e3e968012a1bd581b51a53aa1eddcfeead4b2df0257e1584c4d097` |
| `content/book/life/household/utilities.md` | 1 | `fa44d2aae99a7f833556706aff8bd1ae14724c69c3368f384903b2949006221a` | `8dd4d6a8a6636046c3d484cc41586e353fa13b2a3435cbecba99d6f2eb57cf73` |
| `content/book/life/housing/ca-deposit.md` | 1 | `7485994c01ab02eba4d09e7de101a6551632aabf2b6d3da6c8b31014754a8cbd` | `f6f03d66c585319636373709b30fd6ff9950ae745ac454f422afa79b18f8d796` |
| `content/book/life/housing/rental-process.md` | 2 | `c4eba9734e269439a6cb6fd7664c9335aba7d296d85d3736629f885272427e8b` | `69c2a0e8753bae0bc00986ebe974fa35a60c45eda794a9683152a24f1c17fc7f` |
| `content/book/life/transport/owning-car.md` | 1 | `9b18cf798394de12dbc2c4bd9dc017d8704d928c8088adfd4efab06c35f0f402` | `80fc24c9840ba70dc75f2fd9da34aa685fbef9d3cf9a01a5d9ca80fac9dfc20c` |
| `content/book/life/transport/public-transit.md` | 1 | `090d4dcbe57a2096f5dcbff314a7ca21fa37075669d3601528316fe4d8816cd7` | `22433ad4ddfb5ab0c19aefb084af599b6db80a8ce3beed2cd391578abb53168c` |
| `content/book/people/_index.md` | 1 | `ace9996fed0d24364dbed3d085502f82c44d088bc15547e80e5fe2b5898ed578` | `51bbe41829b53ee62540553029be6a13e1ba48a152f8b5c3638c0fac89664e34` |
| `content/book/people/accessibility/accommodations.md` | 4 | `988d870296bfba09feda32475657ea5542c321765ce5ca29ecf65a6e3f062d59` | `85177df257da56955b3bc895498a8e2dc36e3df2bb98937e7d42b092646ec484` |
| `content/book/people/accessibility/mental-health.md` | 2 | `8b52a308ae7a27c57845818ad47800d86a0d89ce89123797893c8eaac45f05d4` | `91868935b45defdc361648150cfdd0f1e8da919987814cbc6f202286cb0ccd88` |
| `content/book/people/aging/advance-planning.md` | 1 | `581fc7d83f10f9f464bd0ef52c73dc25c1c01075ed186657b22884a1b9ff47f0` | `668ef23eb6596d81a9c011451cbf6c4a19f143e94dc9cfeec124cf6591a06879` |
| `content/book/people/aging/caregiving-plan.md` | 8 | `9a5cf557ecbd0ac87bcb7df0831bdac58c0cb324fbef20f5b48c27f769bd3609` | `97d5ee026ce33a96c2be39aba2d9927828dc3b7b20a89aca078c9a56b15a6d93` |
| `content/book/people/aging/death-arrangements.md` | 1 | `51b15e77c5314ef1bf7cab976cb83b0946ba76fd816ba51ce41e7605679cb0dd` | `8c57542437a9476c8d1804adf0575ba211a8510ea2e08b680f470fcba7af9d4f` |
| `content/book/people/aging/retirement-medicare.md` | 3 | `cc54818566e1fce18046f533d7060871b9a0b72c3ae8e1564bf9e5e697b56765` | `718eb208ebead130567d7c765d447e2081d30585f2c809b1a89a3407c4877e37` |
| `content/book/people/education/_index.md` | 1 | `35115b431893661bff624459203da0f5156937a9fdd200e76238fed10ac85b63` | `8bf6a2e9bd26c670f6eaa796c67e06e434124635890adeaafdca39558531ffc2` |
| `content/book/people/family/birth-and-first-weeks.md` | 3 | `0756c0d7424a31a382e3441ac9739e8a7caed57b965e908fc15e0d13b361706b` | `546ec46a0cadc050970bbcf1b45254c111a15fee624233f81e0fec7f825e4c53` |
| `content/book/people/family/childcare.md` | 2 | `1c45c3e7ffaa09652cafe2ec5bb0263d47f87ffa7913727b52568b5c6367672b` | `5d24c16bb5a37733efae33cdf12a942a09e3321f784f9b5adfb491afba07c588` |
| `content/book/people/health/appointment-network.md` | 3 | `7d99bc988b333e482094362f7366994a17a988b9c4db7a222f273fff125c901d` | `a1ccd540e2b8f078b635e0405eeb2158756395e4b2dc430da33a98042f802b71` |
| `content/book/people/health/coverage-changes.md` | 2 | `0027fac51a855511b7301404a4aa38a121d501950a9a6c97109a29482d8848e2` | `33b6ddc96b7132275ba3b0aa8c8aafa85f174274a9ddce3ce91c2caf9e2797ce` |
| `content/book/people/health/insurance-costs.md` | 2 | `d682854aa03ae2c37081e8df0cac1286b8b973877513c84f5e8d86246ae94e7b` | `f12dc27ebfdf4e0386fcd9fc809bf3c0f9db58cb9125b4c15a4a440269c7560a` |
| `content/book/people/health/medical-bills.md` | 4 | `b85af8f5bbaf5a130efec97c0c31022e3fcee983273d734ceefe508277cac141` | `c8166d650e79a407a0fef67f82408c94d2e8a87812c6ede0e780e351b5f4e699` |
| `content/book/people/language/service-conversations.md` | 2 | `41a9d3b418c44ad20e39a326fcaa862cce6a16d3408ff7d8abf2aa747a893a6c` | `1caf0bcc7538971bb6f2aa57f749f7db789b73f233e41d234f0b5568741fb2e6` |
| `content/book/people/school/school-enrollment.md` | 4 | `491fc6eeabdbcf76b869fa450ff3c101cad98ff9766ae54bed45d6f7b79ec1c5` | `31f3b8ca70d32ce99a0268296caf2d05edd9be500ada5e6d364a832c18299808` |
| `content/book/people/school/school-support.md` | 1 | `7b85c2e4a50b0355aa89980186a9103600d66abdb110a9ef90e76a113e584b71` | `bc20441683ca57af92938d69605bed5f8d643c87755d132939ed75884c2694cb` |
| `content/book/rights/legal/finding-help.md` | 1 | `4a1ef3b78e05ed734897b889f9d4888affde0f0f656196e3ae795f46154ee2cb` | `72b1ccb6f9ea89dbc56e186e730769f5b112069b91232a1e75f2fbca6b28fcac` |
| `content/book/work/employment/_index.md` | 1 | `c507ff0c4bc22aa517f86c67bb00f7097ff378b711b80740e2c9a05a1bbf73ec` | `6b4a22db250628a257d90f23644d359896d803332072d31594e91f5edb1fe81a` |
| `content/book/work/employment/job-loss-support.md` | 1 | `eff07740f03d91f29d2dd376bc50d9e45268e6dcc884f2b07e1346a88c915160` | `af2d3a57bd18c3e3e75e32544d3e964400cd3bf968b4802a5efed73304ac6d38` |
| `content/book/work/employment/pay-stub-overtime.md` | 1 | `4fd1304b02a81b34fc93b05c3ae5d74f32bc402ccd7eff3541140dd239f2c677` | `9edfdcbc722be752251387568ca8de107d4f5577acfe4cce723f9fa9b3373991` |
| `content/book/work/finance/banking-payments.md` | 1 | `307522bd4e462d6c4069788e8a0c9152d43cf289c4f77eab53f0a011192535ad` | `21ee7bf725635c63f25a98c67aa82bdfe58d409ba2537a63e9da827b9b14fb6c` |
| `content/book/work/tax/filing.md` | 1 | `2b66fb484cf9fc660ff9abc34f09e650acf939a7df68b32a78b4cf6051b616d7` | `4a23c9cb70d4e093ad9f0b3a31fb365ebad5c232716dbfc16c1da03e5af7167a` |
| `content/book/work/tax/state-residency.md` | 2 | `da21ce25df2c56eb8b41f309db137a77fd51f4acfc0f149f56e5791d3ac05b81` | `d8173f40ed4600df1b9681460819c500dcff37e704d44def41ce2e1409dc58b7` |
| `content/book/work/tax/tax-residency.md` | 1 | `8ca0163602c1862d68965aa83681f1b6fd46d8818e0b7439ff461b2f027531b0` | `2ee57adc4d694213516b82ee0eb2d104d75f212631db2ac033b698eaf97ba512` |
| `content/docs/routes/_index.md` | 1 | `17dcf23a991587046903c91b5a5823807bbe32dccc76e1d4da142f0fe9e43c98` | `84eb7144a7ccde4431dac88d03eff0717edf983ee89a4094a87bbd802b4d4e14` |
| `content/docs/routes/caregiving.md` | 1 | `365a82ad91c0d15642c33d9f2a41b83e0214f9a19763a89875bf2bce88cbff26` | `33185ceff6a8898fa661c739c273e152efa8d8581ab87d892f6542828ba34420` |
| `content/docs/routes/food-cash-support.md` | 1 | `bc2f2d2bbf0b8cb4d774b8e68a90f14ea97c22b9a281bb1d6dcbcb4f54b32bc7` | `23beebd7fd83baacc3f764c8b3561f9e6ad579549f424c88ab31d1b0e903e001` |
| `content/docs/routes/medical-care.md` | 1 | `18c8cdc3ff5292ae6b36db66570fd4beb0843dadfec63eb0970224011d877a1c` | `dda4b27ac397eb4fad97537763a54fba3a482c4edca2f37a62c12dd9ffcb8545` |

结论：以上实际版本的43件语言修订正式集成，138件语言队列完成，生产、浏览器、指定目视、选定打印页和完整同步均通过。首轮整体范围、独立情境及仍待普通程序按首轮验收另判断，未对地图内全部未来主题或全部318打印页作完成声明。
