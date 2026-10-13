# 活动队列

更新：2026-10-13。用户已明确恢复全书目标，当前 active。保留 B01—B07，B08审阅、正式集成、构建、实际渲染与本地同步已通过；历史暂停现场保留在 HANDOFF-2026-10-13.md。

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
| B08-shared | root：三章导读、抵达后安顿、搬家增量、四州与索引 | 86 HTML、33主题／24章；44页面／28检索／8交互零错误，172页PDF实际10页抽查通过；223文件／94目录完整同步一致 |
| B09-business | banking_fact作者：work/business/start-business → birth_fact事实审 → root第三静态 | 最终76c4cc7f，独立事实PASS；root第三静态尚待实际完整审，仍written／draft true |
| B09-education | static_editor作者：people/education/continuing-education及同slug地图／证据 | 作者继续实际回源及成稿；成人继续学习／资助／注册链，未获独立事实或静态PASS |
| B09-accessibility | birth_fact作者：people/accessibility/accommodations及同slug地图／证据 → banking_fact事实审 → root第三静态 | 已分派先地图后研究；公共服务、工作、住房、学校分别核法律／材料／实施／受阻；尚无审阅PASS |
| B09-outdoors | root作者：rights/outdoors/outdoor-planning及同slug地图／证据 | 地图已建立，实际一级研究开始；普通日游与入门营地、四州许可／闭园／通信／返回；无正文或审阅PASS |
| B10-home | banking_fact作者：life/housing/buying-home及同slug地图／证据 → root事实审 → static_editor第三静态 | 已分派先地图后研究；自住贷款、合同、验屋／估价、产权／交割及持续成本；不提前视为成稿或审阅通过 |

root拥有配置、模板、首页、章导读、公共入口、总账、共享构建及本地提交。作者只改分派主题正文与同slug地图、证据；事实审只改分派审阅记录。新稿 written／draft true，核验字段空，冻结摘要后异人事实审，再由第三名参与者静态审；元数据、构建与正式登记由root完成。

后续须覆盖尚无正文的无障碍、高等教育、创业、户外，并继续历史与公共参与、退休／死亡、家庭与托育、车辆、住户服务、购房、年度报税等重要完整行动链。四州、非公民、不同家庭、城乡、语言与无障碍条件逐项走查；领域地图条目可按同一行动链合并，不能以章节数或占位页满足目标。局部来源失败只限制相应断言，继续可核实工作。外部推送与发布未授权。

B07三位作者只改上述正文及同slug的ops/maps、ops/evidence，不改章导读、共享账本、其他正文或已集成版本。冻结后另下发事实审任务，不能自审。工作区新增语言校对规则已实读；新稿直接执行其判定标准，既有正文的B-PL另排批次，所有正文修订仍须符合用户AGENTS的摘要及异人审阅门禁。

第一轮核心路径和收口条件已具体化于FOCUS.md；后续批次先补缺章，再补重要行动断点。PL-6两份共享入口实际通读、无需语言删改，记录验收；其余既有正文校对仍待分派。
