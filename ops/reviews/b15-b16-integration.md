# B15／B16正式集成验收

2026-10-14（Asia/Shanghai），主控root。六篇最终正文、地图、证据、独立事实和第三静态记录此前已逐件实际完整读取并从实际文件复算绑定；各篇三名参与者不同，事实通过后才做第三静态。候选安装只改status、draft、verified、reviewed_by四字段，六篇正文不变。实际生产、浏览器、目视打印及完整本地同步通过后，本记录将六条candidate正式登记integrated；这不表示全书目标完成。

## 最终正文与三人次序

| 正文路径 | 作者 → 独立事实 → 第三静态 | 安装前whole | 当前body | 安装后whole |
| --- | --- | --- | --- | --- |
| `content/book/work/finance/accounts-investing.md` | root → static_editor → birth_fact | `9c20f7e689b4b9727b2d852914ab6e4ce9369a61edfab25d357e242609ce45ed` | `fdc758f7811bef7896ac5db7279b2646197340bfeaa3f3bfc3e80f41b823af7b` | `27a9e21c015c3837fadc1f249de51b79fdaf0055115608ad56bd3552a173b6a1` |
| `content/book/work/finance/debt.md` | banking_fact → birth_fact → root | `7a16f07bc8edd4967e139f79d8e4d9bf6d1fb788292b297c77abc4e02ad42734` | `4aa3f76757320f1f00023c73c3c92eb9544cfdf2a05ba8dab4406a2882f15e3f` | `91b1df5c1daf403fdc7116009cdebde2d1466ef30e3ca6d1403905a2d92a78af` |
| `content/book/work/finance/food-cash-support.md` | birth_fact → root → static_editor | `17d4032e38fb7aef12e02e8f4ac3b374c62305b03b2c7a9c8cb456f8a129519a` | `4d2a18b7f3999a42d605f0fcaa54dbc20c9ecf75fce34c92228025c647b96b03` | `f6dde24ec7c4435700eada3e036f1c73336fb92d419a1e865a2de419198e7611` |
| `content/book/rights/legal/notices-deadlines.md` | static_editor → birth_fact → banking_fact | `2cdaf601532d5d049f37ba9f37000f89129eb421ffea7b9bb7295e5c58edfbdc` | `511bed06c7a676fac4d03846f0554b1bfcbaa8ec8b7c123a31a664af6063e3e1` | `1ca10388ccc370c8a8daf2cde6480f46b6f349420870685b98901466e6ddba0a` |
| `content/book/rights/safety/disaster-preparation.md` | banking_fact → static_editor → birth_fact | `83829b4fc2657386017e21209791bbf4c23cbf7a2bffe21acbe98a875cea2325` | `a0687e6b6ba5318d2f4a96b2b01cf006b0f5ddb5c3b3404be3db14310957bcb3` | `aa61148ccfe7a8869a83509172024de76398e1cdedf1a12a2ccddce8fcccb744` |
| `content/book/rights/safety/firearms.md` | root → banking_fact → static_editor | `b73917273e772c81ca43501134878466f372f8a81144c4cd9bc791df88400246` | `757a4e709d30fa810d07df5110e787f49ed79b1ee987b304dbb75be1cd985efb` | `74f6b61ec094feb968605de075c9cb44d40e42d2fbc71c5b1906f5e30fab18ab` |

## 最终包与审阅版本

下面各件均由root实际全文读取；长度和摘要重新从当前文件计算。记录中的采用来源、版本、失败请求、只读段／PDF页及未核边界保留；不把某人成功请求或HTTP状态当成他人已读。

| 文件 | 行／字节 | 完整SHA-256 |
| --- | --- | --- |
| `ops/maps/accounts-investing.md` | 33／6075 | `fd40bcfc61eadb306e95353fd8979a43c2e22f307a4f4fe517b8a25ba5d6b00f` |
| `ops/evidence/accounts-investing.md` | 158／27631 | `d0a0e93012502d25d7d0715b66be19f827be74a8b89652ca47b5ceefa23630cf` |
| `ops/reviews/b15-accounts-investing-fact.md` | 89／24290 | `66382931e475a0d0f224bd607d89b8b688cb5740240c892cb15407bee21d6c6d` |
| `ops/reviews/b15-accounts-investing-third.md` | 62／11727 | `ebcf21106b82241b758b7bb876d780044159c04896af5fbecfccd8f3e06e5e97` |
| `ops/maps/debt.md` | 82／13534 | `c086dd82b55f45cec8cdb67aec75d04dd253e6f5b9bce21d5bea1e3cc801f6a8` |
| `ops/evidence/debt.md` | 113／24595 | `d118fac275ba77044c988a090811510cd42c15eea21a2852bd98f37b81d50f0b` |
| `ops/reviews/b15-debt-fact.md` | 77／17891 | `ed47421e446c57c237d54a4cce5d21de981a4b118b6f3078de7104790b14856b` |
| `ops/reviews/b15-debt-third.md` | 44／7764 | `7ed1b7d555019d08b8ac19b52c4d400266b426c18ada9633171e56da7b386792` |
| `ops/maps/food-cash-support.md` | 82／11663 | `740e02abb81167048a51fbcc2ae319d24e4e60d99b76c9726b140803d76b2f0a` |
| `ops/evidence/food-cash-support.md` | 143／34358 | `9e73d5744ef06c2c67d02cbd079010b61e9223cd82e2522d8b939da9a2298aef` |
| `ops/reviews/b15-food-cash-support-fact.md` | 80／23923 | `47d9f1d78b7e4f27c243a5ca3bbb6c20e2d092b47fd7ad48abbb2dcad2061de9` |
| `ops/reviews/b15-food-cash-support-third.md` | 56／11660 | `b739dc8aecac9304dcf47a17fb4883a547c9c94211fdedfe31747e7c82c68ea2` |
| `ops/maps/notices-deadlines.md` | 30／6652 | `676458d839fd3e2c5a4977a66e3d7c5a854b9aebcf7b40fcfdf3a19afcc339f6` |
| `ops/evidence/notices-deadlines.md` | 96／27164 | `b65dc599b5d031a4ed532acf6b4e9e461e94cfbf41429b3bf24df15e4427c7fd` |
| `ops/reviews/b15-notices-deadlines-fact.md` | 77／20422 | `9628a8bfe2a4344a850f14f44b21e1e8ddf2c2191e8bd949d5b72bc0fbb79a80` |
| `ops/reviews/b15-notices-deadlines-third.md` | 57／11827 | `675031f56ae4f1897ef16958fda497c566b4b339d34fe8300076077decdb0afc` |
| `ops/maps/disaster-preparation.md` | 66／12696 | `fcdb096f1a92e484768412b14954a77f41596f15705d3bf93a79542537e5a36d` |
| `ops/evidence/disaster-preparation.md` | 95／25828 | `24f2a0ccae9966ab984067c3f564d6080f6136ac77a445284c85d15e9d706b53` |
| `ops/reviews/b16-disaster-preparation-fact.md` | 97／24392 | `bd953a09665eaff3639ccdfc8639412167950ac563ed4cefaf0feef96915d6b7` |
| `ops/reviews/b16-disaster-preparation-third.md` | 51／11136 | `a85e99e8c33d5a7d0ec87aee9bcd48f3a89eefc51f85295d3e3a5ab7db6d5c93` |
| `ops/maps/firearms.md` | 62／10023 | `59f6bc82cffbbf116e57f8295363dc9dfc7d78222b8c66477fb5963f2ab8e066` |
| `ops/evidence/firearms.md` | 85／23324 | `6773c39b7800436c4ef5bdfeb049afeb1e11a786a79a987442183e6288f0567c` |
| `ops/reviews/b16-firearms-fact.md` | 117／25713 | `5a171c3bfaae41ffbf800718262bf25dbcf6bfe287cc2fb70bdbea2f666274e8` |
| `ops/reviews/b16-firearms-third.md` | 57／9788 | `b5ba033d065edf0feee739ac1e37362a268ab52df6b3c9bac25a1bdb6952f0e1` |

账户最后只补60日从收到款项起算；食品现金最后只把得州继续给付的请求条件改为十三日期间内邮寄，未保留错误的邮戳说法；灾害最后只明确临时住房范围；枪支先补正两件PDF所引用的物理页，再按真正RCW只修未上弹手枪锁车且车外看不见。各次原作者唯一／累计逆验、数字、链接与元数据未改的实核已留在最终审阅；旧版PASS不能套新正文。通知及债务最终包无额外正文修改。

## 公共入口与真实缺陷

主控实际读并安装26件公共源：六新事项、五导读／部分、七已有事项、四州、地区总页、来源说明、事项索引和术语索引（文件清单如下）。初轮补充浏览器真实失败：四州没有账户直链；随后只补同一句行动入口，保留地方资格／法域条件，并对四旧原件做完整逆验。独立公共只读走查又发现地区总页同样漏此链，root实际读旧段后仅补同句，逆验旧全文、frontmatter和数字一致；static_editor实际重新完整读取四州最终59／55／57／55行与地区总页40行。补正后的六目标都做真实点击，初轮失败报告留缓存，不计通过。

| 公共文件 | 当前whole SHA-256 |
| --- | --- |
| `content/docs/routes/accounts-investing.md` | `d5cc3fcd0fd88864ebeaa0f64ea2b0460907caab26da92469c4919cf0c19619e` |
| `content/docs/routes/debt.md` | `5f4585e3c8e034e070bb26458e20fe76e9ab20d500f404a7128d4f9eeec22a7f` |
| `content/docs/routes/food-cash-support.md` | `88ce98b0539e7b3ccaaf7cac799f805bbec7fef8f1191cb5fa203fba637d7302` |
| `content/docs/routes/notices-deadlines.md` | `18f85daa3ea5ad59bf8ab130fe78b5c6efa546e233215eec32b7b4718dc4f791` |
| `content/docs/routes/disaster-preparation.md` | `2e2dccf2f868bc7213f7bec81d13485a3ab6919d9fea51673da445b7abff2b44` |
| `content/docs/routes/firearms.md` | `7e15c6c8a66eecd0d4860635d33da6a3f5f7ece6ca2a864c8b7bf823614cdcfa` |
| `content/book/work/finance/_index.md` | `ba7a0b1b5614b6f080e98a5279f8ec0ad84a8177a2be587aec985568c1e519ee` |
| `content/book/rights/legal/_index.md` | `71ec5e3b0dedaf563d200d147ac8123731c0ac9895e994b3cb76b2ffed2d5e9c` |
| `content/book/rights/safety/_index.md` | `732ef02bb6631ca70ea65f56b971ca3f30793804155209c226525477d990febe` |
| `content/book/work/_index.md` | `657b69b1ef0e26c0bd06804ecf462eccc1835d61bb0e52527ee75ea172f3c66a` |
| `content/book/rights/_index.md` | `54c12c00b60e2ae90bcfe990fe02bdb7b899f4311dc7aa212cc64da49cc56bdf` |
| `content/docs/routes/start-work.md` | `d07dc037c764a639ef82d4e2f1ea54b0f3c5156f82bbdead897a9f1baac73250` |
| `content/docs/routes/retirement.md` | `18dacc4adff2de22f6788769dded3e7202e67bcc6a7d1bb6dc82ddd11e4b880b` |
| `content/docs/routes/identity-theft.md` | `b3faf75b8fa158546da15cd3c182eeb96173660bc79594180a253a1fd7f281a8` |
| `content/docs/routes/emergency.md` | `b4c4eb445d9466f88d8786a2d2bec81ce79c95b138ab9fa4754345a1b0697257` |
| `content/docs/routes/moving.md` | `cbe10a659f5359db81bde13288ae5708f3e54ccaa95affc43ed6653c77b48f69` |
| `content/docs/routes/house-services.md` | `1d5ea50c5d5f9b996ad2108b4e92cb466cb1e8ff1eaffc7b898e3beb2bd45858` |
| `content/docs/regions/_index.md` | `6d2268135c62859b29b2761b2763f296ade92691a91e42e6853d416a911ec9ca` |
| `content/docs/about/_index.md` | `33c08d3927a8c8baae28686dcf8a2e385fc250b0f8358909c6a6e38409ac683f` |
| `content/docs/routes/job-loss.md` | `217c2c22fd967876230fd2a72fa708c58230dba87915ff08668a3b550ee293f5` |
| `content/docs/regions/california.md` | `5baab8679086e3f5768591ed8aee804959657596913ebcf43d932778542627d1` |
| `content/docs/regions/new-york.md` | `40c8c46c24d01e27c873cc80f344b9ea8e5eca4bd706f6488a68a50627eed3c2` |
| `content/docs/regions/washington.md` | `a21abd8c99b409f6d26bcb3eb6842b8b8bd43ef352e36880424cb7790ad2e8db` |
| `content/docs/regions/texas.md` | `6db3219269021c492f82f543e05fb8c5821ecd9095c9b919a5b4dd193e8fb6fd` |
| `content/docs/routes/_index.md` | `6ebfaba6090a162c412d3e4fc0a662a55be11d6fe1d34537cb685d142a9a4b08` |
| `content/docs/glossary/_index.md` | `57ca7738a46d17fcf83585470479c4449da3f27a8f4524fb20fe46c827b45fb5` |

## 工程、浏览器与实际目视

固定Hugo 0.166.0 Extended及OINK `f8f476e660cf053a2645b7b923ae8d08d5448fce`，实际核子模块HEAD和干净状态。最终真正运行 `PATH="$PWD/.cache/checks-venv/bin:$PATH" make check DESTINATION=.cache/production-review`：140 HTML、60正式主题、0草稿，零警告与项目错误。外链不由此脚本核验。

主控自建127.0.0.1:24146预览，隔离Chrome临时profile，两端1440×1000／390×844。最终主检查37路径、74访问、24搜索、8实际交互零错误；键盘首页卡、复制5135字符、非当前侧栏展开并真实点击、深色和搜索已运行。打印94内容单元、60范围元数据、2643外链、零坏锚点。补充52入口、134真实链接点击、18手机表零错误，18表均两列，实际宽／scroll及父宽／scroll皆356，无横向溢出。

root实际逐张显示并看完最终72幅网页图：六正文两端12图、18手机表、六新事项两端12图、五导读两端10图、四州两端8图、术语／地区总入口两端4图、首页／深色账单／HSA／CFARS两端8图；新增术语末六行另放大两件诊断裁图实看。全页缩图只用于整体布局，细字以有效放大图为依据。初次项目venv无Pillow、sips未真正裁切的结果均不计放大检查，使用现有系统Python Pillow得到390×1650与1440×1000有效局部后实际显示查看。

初稿332物理页PDF在枪支末尾留下三行单独占页；打印段间距0.8em版本330页枪支已修但通知末四行仍单独占页。保留两版PDF、实际看过范围、报告、截图与样式，未把仅生成图算看过。root实际读取固定主题的纸张、字号、行距与分页规则，独立试排通知正文；最终仅项目print CSS设段间距0.6em、h2上间距1.1em，保留段内不分页、字号10.5pt与行距1.55。试排仅实际看1和5页，不声称试稿全读。最终重建和两端主／补充浏览器完整重跑均真通过。

最终PDF318物理页、7626910字节；root实际逐张显示并检查全部六篇新正文30页：账户268—273、债务274—278、食品现金279—283、通知290—294、枪支310—313、灾害314—318；另目录3／书目6／work部分210／finance导读259／rights部分284／legal导读285／safety导读307，共37页。跨页表头重复、行和来源可读；通知第五页与枪支第四页尾段完整，无独立尾段页、标题压字或裁切。未逐页目视全318页。

实际 `make sync` 331文件后，root另以os.walk／lstat遍历源与目的完整树，独立比较331文件、148目录、479路径的类型及文件大小／SHA完全相同，拒绝软链接及其他类型。同步前、后及正式登记时旧54篇整文件、正文SHA及原acceptance条目均逐件不变。新六篇body仍匹配两审；依赖、原件、图片、PDF、生成目录均忽略。

## 可复核缓存摘要与边界

| 实际文件 | 完整SHA-256 |
| --- | --- |
| `.cache/reports/b15-baseline.json` | `176eab00d2ccef83b795160b95bb94ec227650f6ab3a18d6171b657ab78c7899` |
| `.cache/reports/b15-b16-install.json` | `72203c1f783e1c7331e62bbfd5a5ad2ea0d8bbc3482534e4820fe55c0138a6fe` |
| `.cache/b15-b16-public-proposals/manifest.json` | `df27ef78197e14c0daf592cb69afb8d83d1d4b8a02594fff362dcfb134d7a83f` |
| `.cache/reports/b15-b16-regional-account-links.json` | `2d10f9d26b5ac1a501860bd7ad19e2191c5f0b218269eb10800d80781646f29a` |
| `.cache/reports/b15-b16-region-index-account-link.json` | `53834986f525134a9fc955a30b5ba62cadbcdedf6f5ca38f2be12731272ebf78` |
| `.cache/b15-b16-browser-report.json` | `7a011b31a319acf80700d76e334648e0b104ff46515bdfb1f5aa1c495ad1b8b2` |
| `.cache/reports/b15-b16-extra-browser.json` | `931a0c458a24e44ea37b01a2ead9c5a75f3e1eb154276f717bfc09ea8f38deae` |
| `.cache/reports/b15-b16-pdf-index.json` | `07031953be191fc7991ab9607807f0e175e05049f997cae2f4f3404436a28acc` |
| `.cache/b15-b16/render/book-review.pdf` | `21f7e2fdce6c2d7243bf25e1cce5e4cb9bdb378f43aeda4446ffd0b15582bff9` |
| `.cache/reports/b15-b16-root-visual-read.json` | `ab2648b20a35c9c12929882ebc0e2b684a2c1a9246a7e78c0da232631f65ff1e` |
| `.cache/reports/b15-b16-independent-sync.json` | `e4aed65036b42ba8800c48b2bf6e5a5bfefcdceda94c39bc971581e38fc6d4c0` |

浏览器具体范围在 [本批scope](b15-b16-browser-scope.json)，来源与审阅是上述Git轻记录，生成大文件不入Git。首轮和0.8em中间版本保留在 `.cache/b15-b16/initial-render/`、`pre-print-fix/`、`paragraph-spacing-08/`；每次查看范围以相应记录为准。

全书旧54语言走查记录已root完整接受，但35拟稿仍等各自差分事实／第三静态／安装与新工程；既有19件无需改亦待逐件全书登记。公共只读建议、剩余情境贯通和最终范围交付继续，不能凭60篇或本批PASS宣告全书完成。不得外部推送、部署、改DNS、联系他人或启动／探测Claude。仅本地提交在明确白名单暂存及逐件摘要核对后由root执行。

暂存检查曾指出people只读审阅记录末尾有多余空行；原作者birth_fact仅删8个LF。root实际核新件241行／28293字节、SHA `32a016295340e7b3e88ca6fae2e933ea03ad137d4acbd296933d3aa3e6dc3de5`；加回8个LF精确恢复已全文读过的旧件SHA `96b58bcacfb231ea836c2f40320445c7ee48288e26109984d1393fafc092ecfe`，末段亦读回。更新共享摘要后重新核72件暂存清单与逐件index摘要；此格式修正不涉及正文、构建或既有审阅结论。
