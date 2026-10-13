# 恢复断点

更新：2026-10-13。目标 **active**，继续完成全书。恢复顺序 BOOKMAP → TASKS → 本账 → 实际文件与Git；408行PROMPT、历史交接及说人话规则已完整实读。历史暂停现场见 [HANDOFF-2026-10-13.md](HANDOFF-2026-10-13.md)。

## 已正式集成

- 本项目main，无remote，未外部推送或发布。B01—B05共22篇保留，B05本地2b293c7、暂停现场559caf8。B06本地49b0bd3，出生bb51e12f、银行2b427531、失业160a39b1、法律帮助98b56bc4，见 [B06验收](reviews/b06-integration.md)。旧未完成审没有追认为通过。
- B07本地cd9af3f，世界8466c6b2、照护67cbe66d、求职f5c8738b、合同a456a890。79 HTML、30主题／21章，两端48访问／20检索／8交互；154物理页PDF实际11页，209文件／87目录同步，见 [B07验收](reviews/b07-integration.md)。旧世界事实分派容量异常不计PASS，最终采用现役banking_fact事实及static_editor第三的实际记录。
- B08本地58bba22，手机2fec99db（root→banking_fact事实→birth_fact第三），购物b8541cd6（birth_fact→root事实→static_editor第三），社区01cae4dd（static_editor→birth_fact事实→banking_fact第三），两审及主控实际渲染均PASS，正式集成。完整SHA与三人记录见 [验收账](reviews/acceptance.json) 和 [B08验收](reviews/b08-integration.md)。root实际完整读最终正文及审阅，只安装frontmatter；旧30篇整文件与正文摘要均不变。
- B08电话原2019 FTC引注受阻后实际换2022主文／两页PDF；购物全额credit及退款(b)/(d)由作者改并逆验；社区NYC优惠、SPL现名、当期课程关闭及未核BPL细则已处理，最后单处空话删句经事实及第三全文重绑。作者BPL Languages成功、事实403与本人已读Contact等效依据分开保留，不承继他人回源。
- B08新增生活三章实际导读及抵达后安顿事项，搬家增通信与社区，四州、术语、事项及来源索引已接入。B08结束时33正式主题、24有内容章节、5部分、86 HTML；其余地图条目没有占位页。
- B08隔离生产零警告／错误，22路径两端44访问、28检索、8交互零错误。三新主题表格宽／scroll均770／356；打印63内容单元、33范围框、917外链、零坏锚点。root实际目视关键桌面／手机表、导读、事项与四州；172物理页PDF实际55／57／58／59／66／68／70／72／74／76，未见裁切或结尾孤行，并非逐页检查。
- public与隔离目录已独立比较完整223文件、94目录、317路径，类型／大小／SHA一致。报告、截图、打印稿、原件及依赖忽略，只保存源文、轻量证据与记录。B08实际本地提交37明确文件，B09／B10进行中稿件未混入；提交号58bba22已实际核Git。
- B09创业3733354f、继续教育d99c8bc5、户外5e190a77各自三名不同参与者的两审及主控完整读取、候选、实际生产／网页／打印均PASS，已正式登记integrated；完整SHA及范围见 [B09验收](reviews/b09-integration.md)。旧33篇整文件和正文摘要仍逐件一致；正式36主题、27章、5部分、95 HTML。
- B09两端25路径共50访问、24检索、8交互零错误；实际看38幅网页图。初次193页打印发现孤立引注，主控只扩展Book打印段落保持规则，再构建及两端检查通过；最终194页实际目视17页（57／70／76／83／101—107／147／151／152／187／188／190），引注已同段，表行／正文／结尾无裁切。最终报告ebccdad2、PDF a9fe5064，两种完整SHA及初版／试排界限在验收记录。
- 实际make sync及随后独立目录比较为241文件、103目录、344路径，类型／大小／SHA全部相同。无障碍、购房及新婚姻作者草稿不进入public。本批本地提交尚待实际Git登记，不冒记号码；外部发布未授权。

## 工程与所有权

实际Hugo 0.166.0 Extended，OINK 1.2.0固定f8f476e660cf053a2645b7b923ae8d08d5448fce；检查依赖使用.cache/checks-venv。本批实际运行make check DESTINATION=.cache/production-review，再做网页／打印并make sync，命令与限制见 [ENGINEERING.md](ENGINEERING.md)。本会话24139预览PID46399和24140预览PID11953均按实际完整命令／项目cwd核所有权后关闭，24140已实查无监听；既有未拥有1317／1318不动。

root拥有共享配置、模板、首页、导读、入口、账本、构建及本地提交。三名现役birth_fact、banking_fact、static_editor只拥有分派主题正文及同slug地图／证据，独立审只写指定记录；不得改他人文件或自行构建提交。新稿written／draft true、verified和reviewed_by空；冻结完整摘要后异人事实，再第三静态，root候选及实际渲染后集成。正文修订均重新绑定最终摘要。

## 当前研究与审阅

B09三主题已正式集成；三章／三事项及部分、四州、术语／来源入口已接入，public为已验收B09。旧33正式主题整文件／正文基线`.cache/reports/b09-baseline.json`已实算保存且最终逐件不变。安装后整文件：business2d6aaf442dc7b13451b724d97eaf5ea639b148e92d089588741ed1a35e33c96f、education5fc71898d9c5b1e0dc65ecf82271c66ca8981d0b863f6d02f577cd1fcfe107af、outdoor92fbdce39b355c44042e79271726f7b10ce4b2574b222668b141b6bc727c796f；完整正文摘要均不变。继续无障碍的独立事实及B10三稿；单批通过不结束全书目标。

| 主题 | 实际断点与下一步 |
|---|---|
| B09 start-business | banking_fact作者→birth_fact事实→root第三，最终完整正文3733354f29b41084479b4b99e3cba5f81d15d9ea56841b3ef0f387d59b6529e7，冻结整文件cda9a588c9e0088dda793d82e8417233878eb55bacb4dbe59b3323cd95c36bf8。DE／EIN、短期I-9、TX年化收入补正后，最后仅改停业关银行一句；两异人分别完整复读145行／逆验重绑PASS。root完整作者／审阅包及工程门禁通过，已正式集成。 |
| B09 continuing-education | static_editor作者144行，body d99c8bc5766a56450668a7a053d39c9a55813cb824bce54fa943081cc7952106，冻结whole4014e377fa4c2c717ec1f020e4059cc33114e80c4894118d49fa3784587281a9。banking_fact独立49源实际采用段事实PASS，FTC失败后官方入口实际跳回主文成功，原失败保留；birth_fact全文第三PASS，新增抽查四源与其余45异人记录明确分开。root完整144行、map40／evidence138、事实89／第三37及工程门禁通过，已正式集成。 |
| B09 accommodations | birth_fact原作者134行初冻结af3be0e5；banking_fact已独立事实审，并要求TEA在线副本只对multiple students自发的范围补正。作者实际新取主文并唯一改句、全文重读／逆验，现实算body1b028fd251ea4f4878076d3cae67fc7aec940ad7e44d7637c269c4362f24db0c／wholecb28fac4910f23fc3c433b5c299e46ca34a18e3918febc2013061aa120ccdeb7。事实审继续／待最终全文重绑，root第三未开始，无集成结论。 |
| B09 outdoor-planning | root作者最终95行，body5e190a7790971ce0d39769e7edf962a19ff04277569e405fcc96f3572a2330ac，冻结wholeb883efee071954ef238b72edc2b5b5edfd7c843df64866efd60b8cbe5608f2b1，map17／evidence56。原2c2b3ded独立20源事实PASS后第三要求删两句，root唯一删句并新全文实读；birth_fact和static_editor各自新全文／逆验恢复旧两SHA，重绑最终两审PASS。root最终审阅及网页／打印通过，已正式集成。USFS403、PDF未读、实时名额等边界保留。 |
| B10 buying-home | banking_fact原作者123行已冻结，root当前实算bodyb89f8256d17904b9fb9e22f6da5ef6033a7530a1b0d36f0b1032ac540299683b／whole1abc9857ea4d1008fbb99b1567711c7cb3e40e9411bbbf40d1da313e5d69023a；written／draft true／核验空。作者现先做无障碍独立事实；root购房事实待开始，static_editor第三待，未集成。 |
| B10 marriage-separation | static_editor四县及法院一级研究已保存，CA洛县／NYC／WA King／TX Harris，King County3／60日矛盾按实际RCW与执照起止日期处理。服务流断开后从实际map36／evidence99恢复，无失败轮PASS；written作者草稿现已创建128行，仍在成稿未冻结。未来root事实、banking_fact第三。 |
| B10 filing | root合并普通年度申报／付款／延期／更正、海外收入及FBAR／8938核心链，2025已出版税年／2026办理日与当前已过期限分开。50官方网页／PDF原件正常TLS与SHA存忽略缓存；联邦及四州采用段、4868物理1／2及FinCEN1／2／4—6已实读，长1040NR／8938／NY2025说明只核采用段；VITA不采用旧69000，IRS旧60—120日分期说明不替代当前180日。当前无正文或审阅，准备成稿，未来static_editor事实、birth_fact第三。 |
| B11 mental-health | birth_fact已正式接普通成人心理支持全国／四州作者任务，研究中；同slug正文／地图／证据，必要无障碍作者返修优先。暂定banking_fact独立事实、root第三，冻结后再送审。 |

第一轮核心路径和收口条件见 [FOCUS.md](FOCUS.md)。继续历史与公共参与、生命周期、通勤／车辆、住户服务、年度报税、经济困难及灾害等缺口；不能凭36篇或单批通过代替全书完成。PL-6两份共享页已实际通读无需删改，其他既有正文校对另排；新稿直接执行说人话标准，不能绕过摘要与异人门禁。

普通研究、修订、核验、构建及本地提交继续自主推进。加拿大只读参考；不启动／探测Claude，不联系外部，不推送、部署或改DNS。记录与文件冲突时以实际文件、完整摘要和来源核对，任何记录不能替代实际核验。
