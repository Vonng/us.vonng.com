# 活动队列

更新：2026-10-14。用户已明确恢复全书目标，当前active。保留B01—B14；B15四篇与B16两篇已完成独立事实、第三静态、正式集成、构建、实际渲染和完整本地同步。本地白名单提交由root收口，全书语言及情境验收继续；历史暂停现场保留在HANDOFF-2026-10-13.md。

| 批次 | 所有者与范围 | 状态／下一步 |
|---|---|---|
| INIT | root：28领域、地区、事项地图，Hugo／OINK、导航与验证 | 工程基线通过，地图不是成稿 |
| B01 | health医疗3；documents文件号码2／加州押金1；civic政府／信用／应急3 | 本地c292949；33 HTML，渲染／同步通过 |
| B02 | civic历史；health税务居民；documents服务英语 | 本地44d1094；40 HTML，58页面／12搜索通过 |
| B03 | health入学；documents驾驶；civic工资 | 本地a81085f；50 HTML，78页面／18搜索及地区增量通过 |
| B04 | documents租房；health医保衔接；civic跨州税 | 本地34ad9e4；53 HTML，32页面／18搜索，实际手机／PDF通过 |
| B05 | health地理→civic事实；documents文化→health事实；civic原住民族→documents事实；root第三静态 | 三稿通过；61 HTML、32页面／20搜索，实际手机／PDF通过，本地2b293c7 |
| B05-address | root作者→documents事实审→civic第三静态 | 最终0c4c7def；三人审阅与本批集成通过，搬家事项已接入 |
| B06-birth | health原作者／static_editor修订→birth_fact事实审→root第三静态 | 最终bb51e12f，三人审阅及B06集成PASS |
| B06-banking | documents原作者／static_editor修订→banking_fact事实审→root第三静态 | 最终2b427531，三人审阅及B06集成PASS |
| B06-job-loss | civic原作者／birth_fact修订→root事实审→static_editor第三静态 | 最终160a39b1，三人审阅及B06集成PASS |
| B06-legal | root作者→health事实审→civic第三静态 | 最终98b56bc4，历史PASS摘要一致，恢复核对及B06集成PASS |
| B06-shared | root：家庭／法律导读、出生／失业事项、四州与首页、打印样式 | 69 HTML、26主题；46页面／20搜索／8交互；129页PDF实际抽查；189路径同步一致；本地49b0bd3 |
| B07-caregiving | birth_fact作者：people/aging/caregiving-plan → banking_fact事实审 → root第三静态 | 最终67cbe66d，两审及实际生产／渲染PASS，正式集成 |
| B07-career | banking_fact作者：work/career/job-search-onboarding → static_editor事实审 → root第三静态 | 最终f5c8738b，两审及实际生产／渲染PASS，正式集成 |
| B07-world | root作者：foundations/world/world-connections → banking_fact事实审 → static_editor第三静态 | 最终8466c6b2，两审及实际生产／渲染PASS，正式集成 |
| B07-contracts | static_editor作者：rights/contracts/reading-contracts → birth_fact事实审 → root第三静态 | 最终a456a890，两审及实际生产／渲染PASS，正式集成 |
| B07-shared | root：四章导读、求职／照护事项、四州入口与索引 | 79 HTML、30主题／21章；48页面／20检索／8交互零错误，154页PDF实际11页抽查通过；209文件／87目录同步一致 |
| B08-digital | root作者：life/digital/phone-internet → banking_fact事实审 → birth_fact第三静态 | 最终2fec99db，两审及主控实际网页／打印PASS，正式集成 |
| B08-community | static_editor作者：life/community/local-support → birth_fact事实审 → banking_fact第三静态 | 最终01cae4dd，事实修改与最后单处删句分别重绑，两审及主控网页／打印PASS，正式集成 |
| B08-household | birth_fact作者：life/household/shopping-returns → root事实审 → static_editor第三静态 | 最终b8541cd6，两处最小补正后两审及主控网页／打印PASS，正式集成；食品支持资格另留地图 |
| B08-shared | root：三章导读、抵达后安顿、搬家增量、四州与索引 | 本地58bba22；86 HTML、33主题／24章；44页面／28检索／8交互零错误，172页PDF实际10页抽查通过；223文件／94目录完整同步一致 |
| B09-business | banking_fact作者：work/business/start-business → birth_fact事实审 → root第三静态 | 最终3733354f两审及主控实际网页／打印PASS，正式集成 |
| B09-education | static_editor作者：people/education/continuing-education → banking_fact事实审 → birth_fact第三静态 | d99c8bc5两审、root完整正文／证据／审阅实读及工程门禁PASS，正式集成 |
| B09-accessibility | birth_fact作者：people/accessibility/accommodations及同slug地图／证据 → banking_fact事实审 → root第三静态 | 最终134行1b028fd2，两审及B10实际网页／全部新增打印页PASS，正式集成 |
| B09-outdoors | root作者：rights/outdoors/outdoor-planning → birth_fact事实审 → static_editor第三静态 | 最终5e190a77：作者仅删两句后两异人新95行全文／逆验重绑PASS，主控实际网页／打印通过，正式集成 |
| B10-home | banking_fact作者：life/housing/buying-home及同slug地图／证据 → root事实审 → static_editor第三静态 | 作者唯一补L39 LE例外后最终123行1232cdbd；新全文／逆验及两审重绑PASS，B10实际网页／全部新增打印页通过，正式集成 |
| B10-family | static_editor作者：people/family/marriage-separation及同slug地图／证据 → root事实审 → banking_fact第三静态 | L108现场服务唯一作者补正，最终128行body3dca83e2；root事实109行及banking_fact第三65行完整绑定PASS，B11工程／实际网页／全部新增打印页通过，正式集成 |
| B10-filing | root作者：work/tax/filing及同slug地图／证据 → static_editor事实审 → birth_fact第三静态 | 最终136行6ca184bc，两canonical链接唯一修订逆验、完整两审及B10工程／实际网页／全部新增打印页PASS，正式集成 |
| B09-shared | root：三章导读、开业／继续学习／户外事项、三部分与四州／索引 | 本地e260625；95 HTML、36主题／27章，50访问／24搜索／8交互零错误；打印孤立引注修正后194页实际17页通过，241文件／103目录同步一致；39明确源文件，进行中草稿未混入 |
| B11-mental | birth_fact作者：people/accessibility/mental-health及同slug地图／证据 → banking_fact事实审 → root第三静态 | 最终117行575c7d19，完整两审及root独立五源抽查、B10工程／实际网页／全部新增打印页PASS，正式集成 |
| B11-utilities | banking_fact作者：life/household/utilities及同slug地图／证据 → birth_fact事实审 → static_editor第三静态 | 最终112行59d29dec、map78／evidence167；四处作者补正、异人事实89行／第三62行及root完整实读与逆验PASS，B11工程／实际网页／全部新增打印页通过，正式集成。City Light PDF参与者访问边界保留 |
| B11-retirement | birth_fact作者：people/aging/retirement-medicare及同slug地图／证据 → static_editor事实审 → root第三静态 | 最终148行body4aa59f4c、map29／evidence65；事实102行及root第三25行、完整包与唯一修订逆验PASS，B11工程／实际网页／全部新增打印页通过，正式集成。2027册与新法只采用已读范围 |
| B12-car | static_editor作者：life/transport/owning-car及同slug地图／证据 → banking_fact事实审 → birth_fact第三静态 | 最终152行bodya3a6c544／whole0a84ca46、map62／evidence162已root全部实读和唯一逆验；bank事实136行PASS SHAb331cf54、birth最终第三62行PASS SHA5212eefa均已root完整实读／重算绑定。各自来源与CA算法／公式未读边界保留；已由root仅改四个集成元数据字段；隔离生产118 HTML／48正式主题通过，70访问／32检索／8交互及补充44入口／13手机表零错误；root实际目视58幅网页图、全部27新增正文及5导读打印页通过，287文件／126目录完整同步后正式登记integrated，见B12验收 |
| B10-shared | root：无障碍章、购房／心理／便利事项、报税／四州／术语与导读 | 本地2411984，46明确源文件；103 HTML、40主题／28章，54访问／28检索／8交互零错误，补充18入口／13手机表；219页PDF全部新增23物理页目视通过，257文件／111目录完整同步一致 |
| B11-shared | root：住户服务、婚姻与退休三篇及相关导读／事项／四州 | 本地668a9c7，43明确文件；109 HTML、43主题／28章；54访问／24检索／8交互零错误，补充24入口／7手机表，实际45网页图及全部19新增打印页加5导读页通过；269文件／117目录386路径独立同步相同。旧40正式主题双摘要与验收条目均不变，见b11-integration.md；全书继续 |
| B12-childcare | birth_fact作者：people/family/childcare及同slug地图／证据 → root事实审 → banking_fact第三静态 | 作者115行bodyb2075149／whole4493b2ec、map44／evidence96冻结不变；root事实74行PASS及bank第三76行PASS均完整实读绑定，第三SHA62a7345a。root49原URL＋3补充实际来源、bank15个独立采用URL与失败各自保留；已由root仅改四个集成元数据字段；隔离生产118 HTML／48正式主题通过，70访问／32检索／8交互及补充44入口／13手机表零错误；root实际目视58幅网页图、全部27新增正文及5导读打印页通过，287文件／126目录完整同步后正式登记integrated，见B12验收 |
| B12-history | banking_fact作者：foundations/history/historical-landscape及同slug地图／证据 → birth_fact事实审 → root第三静态 | 作者90行body3979b801／whole17e3fcc0、map51／evidence78冻结不变；birth事实80行及root第三30行PASS已完整实读，第三SHA31f803ff；root8个来源实际抽核及三张原件图已读。已由root仅改四个集成元数据字段；隔离生产118 HTML／48正式主题通过，70访问／32检索／8交互及补充44入口／13手机表零错误；root实际目视58幅网页图、全部27新增正文及5导读打印页通过，287文件／126目录完整同步后正式登记integrated，见B12验收 |
| B12-entry | root作者：life/documents/entry-return及同slug地图／证据 → birth_fact事实审 → banking_fact第三静态 | L31唯一URL补正后最终114行body8293f921／whole615f3462、map35／evidence97已全读／重算和逆验。birth最终事实115行PASS SHAd7c8fb2c已root完整实读／复算；bank第三65行PASS SHA2ebe8ce9已root全文实读绑定。40采用＋2门户实际边界保留，已由root仅改四个集成元数据字段；隔离生产118 HTML／48正式主题通过，70访问／32检索／8交互及补充44入口／13手机表零错误；root实际目视58幅网页图、全部27新增正文及5导读打印页通过，287文件／126目录完整同步后正式登记integrated，见B12验收 |
| B12-planning | static_editor作者：people/aging/advance-planning及同slug地图／证据 → root事实审 → banking_fact第三静态 | 最终125行body48c70ff0／whole3b3ccb27、map36／evidence83；root事实72行PASS SHA7ac01e30及bank最终第三61行PASS SHAdc0a380c均已root完整实读／重算绑定。第三12URL有界抽查、不同NJP原件及CA法条失败分别保留；已由root仅改四个集成元数据字段；隔离生产118 HTML／48正式主题通过，70访问／32检索／8交互及补充44入口／13手机表零错误；root实际目视58幅网页图、全部27新增正文及5导读打印页通过，287文件／126目录完整同步后正式登记integrated，见B12验收 |
| B12-shared | root：五主题、五章导读、四新事项／五现有事项增量、四州与索引 | 48正式主题／28章／5部分、118 HTML；70访问／32搜索／8交互及44补充入口／13手机表零错误，实际58幅网页图与全部27新增正文／5导读打印页通过；287文件／126目录413路径完整独立同步一致。旧43篇双摘要及验收条目不变，见b12-integration.md；本地42e9fca，56明确文件；全书继续 |
| B13-participation | banking_fact作者：government/public-participation → static_editor事实 → root第三 | 两句三处原作者必要补正后最终body86f99832／作者whole5dca3119、map68 SHA935ced9b／evidence132 SHAd46af342；static事实79行PASS SHA3ea03c61、root第三35行PASS SHAa08a9a91及全部包均已root实读／复算、唯一逆验和本人三源抽核。仅安装四个元数据字段，实际隔离生产123 HTML／51正式主题通过；60访问／24搜索／8交互及补充32入口／38链接点击／7手机表零错误，root实际目视47幅最终网页图、全部16新增正文和3导读及1目录打印页；297文件／131目录428路径独立同步一致后登记integrated，见B13验收。旧48篇双摘要及验收条目不变 |
| B13-migration | static_editor作者：history/migration-society → birth_fact事实 → root第三 | 唯一L67改“签署成法”后bodyc414a204／作者whole74dbb24a、map36 SHA45237d99／evidence69 SHA06447e2f；birth事实85行PASS SHAd18ccece、root第三37行PASS SHA0f655200及全部包均root实读／复算、唯一逆验和本人三源抽核。25来源各自边界保留；仅安装四个元数据字段，实际隔离生产123 HTML／51正式主题通过；60访问／24搜索／8交互及补充32入口／38链接点击／7手机表零错误，root实际目视47幅最终网页图、全部16新增正文和3导读及1目录打印页；297文件／131目录428路径独立同步一致后登记integrated，见B13验收。旧48篇双摘要及验收条目不变 |
| B13-transit | root作者：life/transport/public-transit及同slug地图／证据 → birth_fact事实审 → banking_fact第三静态 | 原作者仅删King County“书面”，120行body2d29516b／作者whole5d99b59a、map26 SHA15fed97b／evidence92 SHA635f87df；birth事实103行PASS SHA7cea4729、bank第三53行PASS SHA152eca45及全部包已root实读／复算与唯一逆验。混合CR与cp1252→UTF-8记录补正各归原记录所有者实际核验；仅安装四个元数据字段，实际隔离生产123 HTML／51正式主题通过；60访问／24搜索／8交互及补充32入口／38链接点击／7手机表零错误，root实际目视47幅最终网页图、全部16新增正文和3导读及1目录打印页；297文件／131目录428路径独立同步一致后登记integrated，见B13验收。旧48篇双摘要及验收条目不变 |
| B13-shared | root：三主题、五导读、两新事项／抵达搬家与四州索引 | 实际隔离生产123 HTML／51正式主题通过；60访问／24搜索／8交互及补充32入口／38链接点击／7手机表零错误，root实际目视47幅最终网页图、全部16新增正文和3导读及1目录打印页；297文件／131目录428路径独立同步一致后登记integrated，见B13验收。旧48篇双摘要及验收条目不变；本地79928c6，40明确完成源和轻记录已实核入提交，B14／B15进行中稿不混入，全书继续 |
| B14-school | static_editor作者：people/school/school-support及同slug地图／证据 → banking_fact事实审 → birth_fact第三静态 | 原作者仅补SPS一年HIB两类例外、收窄未独核CA复议数字；最终133行body04d5ef6d／wholebc4fc553、map42 SHA6af170ab／evi119 SHA51edaf28，bankFACT116行PASS SHA872b54f9、birthTHIRD69行PASS SHA65abafa4均root真正完整实读并六摘要从实际文件复算接受；两处唯一逆验通过。37来源各自段页／失败、旧件/OCR表/SPS504冲突保留，仅安装四项元数据；B14实际生产128 HTML／54正式主题，66访问／24搜索／8交互及36补充入口／50点击／8手机表零错误，另12搜索点击通过；root实际看58有效网页图和全部18新正文／3导读／1目录打印页，307文件／136目录443路径独立同步一致后正式登记integrated，见B14验收 |
| B14-death | banking_fact作者：aging/death-arrangements → birth_fact事实 → static_editor第三 | 原作者仅在实际L61补IFS经办案件限定，125行body7f527b50／whole0ec2260e、map67 SHAa795abe6／最终evi105 SHAe9bb7506；root已新正文／两包全部实读、唯一句及证据定位一字符完整逆验。birth新FACT126行PASS SHAfe779632、static新THIRD82行PASS SHAff2561bc均root真正完整实读并六摘要从实际文件复算接受；75链接／元数据不变。旧104行事实与56行待修第三只留历史，不作新稿结论；49来源各自段页／失败保留，仅安装四项元数据；B14实际生产128 HTML／54正式主题，66访问／24搜索／8交互及36补充入口／50点击／8手机表零错误，另12搜索点击通过；root实际看58有效网页图和全部18新正文／3导读／1目录打印页，307文件／136目录443路径独立同步一致后正式登记integrated，见B14验收 |
| B14-workplace | birth_fact作者：employment/workplace-rights → static_editor事实 → banking_fact第三 | 第三必要中文释义唯一修订后137行body049c4ece／whole0017e303、map49 SHA372f0775／evi85 SHA468bb400；static新FACT96行PASS SHAabe8dc32、bank新THIRD72行PASS SHAcc6afc83均root真正完整实读并六摘要从实际文件复算接受。root已新作者包全部实读、两处历史唯一逆验通过，77链接／元数据不变；旧待修54行abe59270仅留历史。PTO历史及55URL各自段页／失败保留，仅安装四项元数据；B14实际生产128 HTML／54正式主题，66访问／24搜索／8交互及36补充入口／50点击／8手机表零错误，另12搜索点击通过；root实际看58有效网页图和全部18新正文／3导读／1目录打印页，307文件／136目录443路径独立同步一致后正式登记integrated，见B14验收 |
| B14-shared | root：三篇、三章导读、两新事项／七现有事项与四州、索引 | 54正式主题／28章／5部分、128 HTML；主66访问／24检索／8交互、补充36入口／50点击／8手机表及12搜索点击零错误；实际看58有效网页图、全部18新增正文及3导读／1目录打印页，307文件／136目录443路径独立同步相同。旧51篇双摘要与账本不变；见B14验收，本地6ad9cd2，42明确完成文件与白名单逐件摘要实核一致，B15／B16进行中包未混入 |
| B15-accounts | root作者：finance/accounts-investing及同slug地图／证据 → static_editor事实 → birth_fact第三 | 最终bodyfdc758f7，root作者→static_editor事实→birth_fact第三；两异人审及root最终包实际全读／复算通过；仅四项候选元数据，真实生产／两端网页／全部新增打印页／完整同步通过后正式登记integrated；详见 [B15／B16验收](reviews/b15-b16-integration.md) |
| B15-debt | banking_fact作者：finance/debt及同slug地图／证据 → birth_fact事实 → root第三 | 最终body4aa3f767，banking_fact作者→birth_fact事实→root第三；两异人审及root最终包实际全读／复算通过；仅四项候选元数据，真实生产／两端网页／全部新增打印页／完整同步通过后正式登记integrated；详见 [B15／B16验收](reviews/b15-b16-integration.md) |
| B15-notices | static_editor作者：legal/notices-deadlines及同slug地图／证据 → birth_fact事实 → banking_fact第三 | 最终body511bed06，static_editor作者→birth_fact事实→banking_fact第三；两异人审及root最终包实际全读／复算通过；仅四项候选元数据，真实生产／两端网页／全部新增打印页／完整同步通过后正式登记integrated；详见 [B15／B16验收](reviews/b15-b16-integration.md) |
| B15-support | birth_fact作者：finance/food-cash-support及同slug地图／证据 → root事实 → static_editor第三 | 最终body4d2a18b7，birth_fact作者→root事实→static_editor第三；两异人审及root最终包实际全读／复算通过；仅四项候选元数据，真实生产／两端网页／全部新增打印页／完整同步通过后正式登记integrated；详见 [B15／B16验收](reviews/b15-b16-integration.md) |
| B16-disaster | banking_fact作者：safety/disaster-preparation及同slug地图／证据 → static_editor事实 → birth_fact第三 | 最终bodya0687e6b，banking_fact作者→static_editor事实→birth_fact第三；两异人审及root最终包实际全读／复算通过；仅四项候选元数据，真实生产／两端网页／全部新增打印页／完整同步通过后正式登记integrated；详见 [B15／B16验收](reviews/b15-b16-integration.md) |
| B-PL-foundations | banking_fact只读九基础正文；root修订／异人审阅 | 九篇实际全文读取、18摘要绑定；83行走查记录SHA5a7ced52已root完整接受。四篇八建议已冻结拟稿并纳入前20差分事实PASS／第三静态进行，五篇无需改待全书逐件登记；canonical尚未实施。其余三组只读已完整接受，旧67件进度映射仍待，不表示全书语言完成 |
| B16-firearms | root作者：safety/firearms及同slug地图／证据 → banking_fact事实 → static_editor第三 | 最终body757a4e70，root作者→banking_fact事实→static_editor第三；两异人审及root最终包实际全读／复算通过；仅四项候选元数据，真实生产／两端网页／全部新增打印页／完整同步通过后正式登记integrated；详见 [B15／B16验收](reviews/b15-b16-integration.md) |
| B15／B16-shared | root：六主题、26公共入口与打印段间距 | 60正式／28章／5部分、140 HTML；主74访问／24检索／8交互，补充52入口／134点击／18手机表零错误；实际72最终网页图及全部30新增正文／7入口打印页通过，331文件／148目录479路径独立同步一致；旧54双摘要及账条目不变，正式集成，见B15／B16验收 |

root拥有配置、模板、首页、章导读、公共入口、总账、共享构建及本地提交。作者只改分派主题正文与同slug地图、证据；事实审只改分派审阅记录。新稿 written／draft true，核验字段空，冻结摘要后异人事实审，再由第三名参与者静态审；元数据、构建与正式登记由root完成。

后续按FOCUS完成全书语言修订、公共入口建议和情境贯通。移民社会、公共参与、交通、学校、死亡、劳动、专项账户、经济困难、通知及灾害核心已实际承接，仍逐项核四州、非公民、不同家庭、城乡、语言与无障碍条件。地图细目可在同一行动链内合并，低频专家程序保留确切边界，不凭篇数或占位页满足目标。外部推送与发布未授权。

B07三位作者只改上述正文及同slug的ops/maps、ops/evidence，不改章导读、共享账本、其他正文或已集成版本。冻结后另下发事实审任务，不能自审。工作区新增语言校对规则已实读；新稿直接执行其判定标准，既有正文的B-PL另排批次，所有正文修订仍须符合用户AGENTS的摘要及异人审阅门禁。

第一轮核心路径和收口条件见FOCUS.md；现60篇和78公共页仍须全书收口。旧54四组语言只读记录已root完整接受；35拟稿64处修订冻结，前20差分FACT实际接受后第三静态进行，people15差分FACT进行，canonical旧54及原账条目仍同B15基线。进行中下一批作者／审阅记录不混入本批提交，不能以只读记录登记语言已实施。
