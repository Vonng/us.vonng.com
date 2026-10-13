# B02 税务居民独立事实审

- 审阅人：`/root/civic`；作者：`/root/health`，为不同参与者。
- 实际回源与落记录日期：2026-10-13。
- 审阅正文：`content/book/work/tax/tax-residency.md`。
- 正文 SHA-256：`93d49d8669b588696e7b89b7d48e1dd9e6647f1068a58834adb446a829eff457`。
- 算法：读取实际文件后，对 `split('---', 2)[2]` 字符串按 UTF-8 编码计算 SHA-256，不含 front matter。冻结通知后重新完整阅读文件并复算，结果一致。
- 结论：在正文声明的联邦个人所得税范围内，**事实审通过** ，无待作者修改的阻断项。此记录不代替第三人静态审、主控候选元数据安装、隔离构建和实际渲染验收。

审阅者独立打开并阅读下列 IRS 网页、表件和加州 FTB 原文；作者的来源清单和审稿提示不代替这些实际阅读。表中以章节、表件页码和少量原文短语定位；读到页面或表格，不代表已为任何真实个人判定资格。

## 居民测试、计日与学生排除

| 实际阅读的原文与定位 | 独立核验结果 |
|---|---|
| [IRS：Determining an individual's tax residency status](https://www.irs.gov/individuals/international-taxpayers/determining-an-individuals-tax-residency-status)，正文两项测试、例外与 dual-status 段；`calendar year` | 非公民的绿卡／实质居留测试、按日历年核对、年中身份变化和选举入口有依据。正文未用签证、号码或单年半年直接代替测试。 |
| [IRS：U.S. tax residency — Green card test](https://www.irs.gov/individuals/international-taxpayers/us-tax-residency-green-card-test)，正文及终止身份列项；`at any time` | 日历年中任何时候具备 LPR 身份与起始日另判的区分正确；正式放弃、行政和司法终止路径有依据。 |
| [IRS Publication 519（2025）](https://www.irs.gov/publications/p519)，第 1 章 `Green Card Test`、`Resident status abandoned` 及紧接的 Caution；`more than 10 years old` | 原文明确长期离美或绿卡年代过久不自动结束税务居民状态，须核对正式决定及证据。稿件没有把卡片有效期当成税务居民结束日，也保留了协定与长期居民边界。 |
| [IRS：Substantial presence test](https://www.irs.gov/individuals/international-taxpayers/substantial-presence-test)，两项门槛、`Days of presence in the United States`、`Exempt individual` | 当前年 31 天与三年加权 183 天须同时满足；权重为 1、1/3、1/6。一天中部分时间、美国地域范围、属地与领空排除、过境不足 24 小时及特殊身份条目均与稿件一致。exempt 指计日排除，而非所有收入免税。 |
| [IRS：Exempt individual who is a student](https://www.irs.gov/individuals/international-taxpayers/exempt-individual-who-is-a-student)，正文身份、五年及表件段；`5 calendar years` | 学习目的、F/J/M/Q、实质遵守身份条件、历次学生／教师／受训者等年份和部分日历年计入都有依据。稿件未把五年写成连续 60 个月，未保证每个学位重置。 |
| [2025 Form 8843](https://www.irs.gov/pub/irs-pdf/f8843.pdf)，第 3 页 `Who Must File`、`When and Where To File`；第 4 页 `Part III—Students` | 学生需要报告计日排除；有 1040-NR 随表附交、没有所得税申报义务时仍单独提交，期限随相应说明核对。原文支持排除年份及五年后事实证明路径，正文没有把漏表补救说成统一规则。 |
| [2025 Form 8843](https://www.irs.gov/pub/irs-pdf/f8843.pdf)，第 2 页 Part V 第 17—18 项；第 4 页 `Part V—Individuals With a Medical Condition or Medical Problem` | 医疗问题须在美期间发生并阻止原定离境；原来已知病况、来美治疗及已能离境后继续留下不能无条件排除。表上包含预定／实际离境日期、医生或其他医疗人员证明。稿件使用“不能直接套用”，没有把所有旧病一概排除。 |
| [IRS：外国学生较密切联系例外](https://www.irs.gov/individuals/international-taxpayers/the-closer-connection-exception-to-the-substantial-presence-test-for-foreign-students)，四条件及举证责任段；`all four` | 五年后学生分支与一般 8840 分支不同。无永久居美意图、持续守身份条件、未采取取得绿卡步骤、境外较密切联系四项与正文一致。没有写成第六年自动成居民，也没有把学生例外等同收入豁免。 |

两个标明教学虚构的例子已独立复算：`150 + 120 / 3 + 120 / 6 = 210`；2021、2022、2023、2024、2025 为五个日历年，2021 年只在 12 月符合条件仍占一年。正文保留“所有天数均可计入、尚待例外审查”和此前无适用排除年份的条件。

## 较密切联系、协定与居民期间

| 实际阅读的原文与定位 | 独立核验结果 |
|---|---|
| [IRS：一般较密切联系例外](https://www.irs.gov/individuals/international-taxpayers/closer-connection-exception-to-the-substantial-presence-test)，`Establishing a closer connection`、两外国条件、绿卡步骤与 `Requirement to file Form 8840` | 当前年少于 183 天、全年境外 tax home、较密切联系、绿卡申请限制和及时提交表件共同构成判断，不能以国籍或家乡取代事实。两国分支与迟交的严格举证例外有依据。 |
| [2025 Form 8840](https://www.irs.gov/pub/irs-pdf/f8840.pdf)，第 3 页 `Tax Home`、`Can You Claim the Closer Connection Exception?`；第 4 页两国条件、`When and Where To File`、逾期说明 | tax home 通常为主要工作或营业地区，不简单等同家庭住址。核对了境外全年要求、两国五条件、无须所得税申报时仍须单交、延期及逾期举证规定。正文没有把补交表件写成自动恢复资格。 |
| [IRS：Tax treaties](https://www.irs.gov/individuals/international-taxpayers/tax-treaties)，`Overview`、`The effect of tax treaties`；`residents (not necessarily citizens)` | 国籍不自动决定待遇；居民冲突条款与单项收入减免不同；计算所得税的非居民待遇不自动消除其他目的下的居民身份。各州是否承认联邦协定须另查，不能直接外推。 |
| [Form 8833，Rev. December 2022](https://www.irs.gov/pub/irs-pdf/f8833.pdf)，第 1 页双重居民勾选与长期居民提示；第 4 页 `Dual-resident taxpayer`、`Termination of U.S. Residency` | 双重居民按协定主张另一国居民，计算所得税按相应非居民规则、交 1040-NR 并附 8833 有原文支持。长期绿卡居民可能涉及 Form 8854 及终止居民特殊规定；稿件没有替具体协定作结论，也没有保证所有申报义务消失。 |
| [IRS：Residency starting and ending dates](https://www.irs.gov/individuals/international-taxpayers/residency-starting-and-ending-dates)，绿卡／SPT 起始、exempt 注释、结束及 `Statement required to establish your residency termination date` | 起点一般不是满足加权门槛的当天；两测试取适用的较早起点，前后年度居民期间可产生连续年度影响。提前结束须核对境外 tax home、联系与声明，单纯离境不够。稿件没有遗漏下一年度的约束，也未把 exempt 日当成起算日在美日。 |

## 所得、申报路径、选举与州税

| 实际阅读的原文与定位 | 独立核验结果 |
|---|---|
| [IRS：Taxation of U.S. residents](https://www.irs.gov/individuals/international-taxpayers/taxation-of-us-residents)，全球所得及报表段；`worldwide income` | 居民通常按类似公民规则处理全球所得、使用 1040／1040-SR 路径有依据；稿件把是否必须报表及具体抵免留给相应条件，没有声称全球所得必被重复全额课税。 |
| [IRS：Taxation of nonresident aliens](https://www.irs.gov/individuals/international-taxpayers/taxation-of-nonresident-aliens)，`Who must file`、应税所得和报表段 | 非居民仍可能负有 1040-NR 申报义务；ECI 与其他应税美国来源所得需区分。学生有工资、奖学金或其他收入应另判，不能以计日排除代替所得性质判断。 |
| [IRS：Alien taxation — Certain essential concepts](https://www.irs.gov/individuals/international-taxpayers/alien-taxation-certain-essential-concepts)，居民、非居民、dual-status 三段 | 非居民在有限情形下也可能对境外来源收入纳税。稿件采用“通常／一般／有限情形”，没有将美国来源表述为绝对唯一边界。 |
| [IRS：Taxation of dual-status individuals](https://www.irs.gov/individuals/international-taxpayers/taxation-of-dual-status-individuals)，定义、所得时段及 `Forms to file` | dual-status 是同一年居民与非居民期间，不指双重国籍；年末身份决定主表和另一时段说明。正文未把 dual-status 与两国同时居民混淆，且提醒扣除限制另核。 |
| [IRS：Nonresident aliens — Sourcing of income](https://www.irs.gov/individuals/international-taxpayers/nonresident-aliens-sourcing-of-income)，`Summary of source rules` 表；`Where services performed`、`Location of property` | 工资一般看实际工作地点、租金看不动产所在地。由此支持海外雇主和海外收款账户不能单独证明境外工资来源；这是对原表的直接应用，未外推复杂跨国分配细节。 |
| [IRS：Tax residency status — First-year choice](https://www.irs.gov/individuals/international-taxpayers/tax-residency-status-first-year-choice)，开头条件与 `Filing Form 1040`；`31 days in a row`、`75%` | 本年及前一年未满足测试、前一年未作该选择、下一年满足 SPT、连续 31 天和对应期间 75% 条件与稿件一致。须待下一年实际满足测试再提交声明，缺席日有限计入，均有依据。正文所用旧路径会正确重定向至该页。 |
| [IRS：Nonresident spouse](https://www.irs.gov/individuals/international-taxpayers/nonresident-spouse)，`Election to file joint return`、`How to make the choice`、`Suspending the choice`、`Ending the choice` | 选择当年联合申报、双方全年全球所得、双方签署、以后年度延续以及终止限制有依据。稿件只写“符合条件”，未承诺任何婚姻或配偶情形均适用，也未误称以后每年只能联合申报。 |
| [California FTB：Residents](https://www.ftb.ca.gov/file/personal/residency-status/index.html)，`Am I a resident?` 两项；`temporary or transitory purpose` | 在加州非临时目的居住，或加州 domicile 者因临时目的离州的两条基础条件准确。稿件只用来说明州判定另有规则，没有以此替任何个人完成加州居民综合判断。 |

## 来源差异与本次边界

- 本次实际读到的是 2025 年 Form 8843、8840，及 Rev. December 2022 的 Form 8833。稿件准确声明采用查阅时已发布版本，没有冒称已核实 2026 税年的最终表件，也没有写死年度截止日、收入门槛或扣除额。未来实际申报应重新获取对应税年的表件与说明。
- IRS 的 SPT 概述页对 8843 逾期后果措辞较宽；2025 Form 8843 第 3 页的该项处罚说明具体点名专业运动员与医疗情形。已分别实际阅读，不以概述覆盖表件细节。正文只说明学生申报义务，不断言学生漏表就必然失去全部计日排除资格，故无需以未经核实的统一处罚补稿。
- IRS Tax treaties 概述页仍出现 1040-NR-EZ 的旧名称。稿件使用实际 Form 8833 指向的 1040-NR，未沿用这个过时入口。
- 本次未审查任何具体双边协定的完整待遇、saving clause、个别奖学金或工资减免、FICA、遗产赠与税、移民身份处分、FBAR／FATCA、退出税计算或既往错报补救方案；正文亦未给出这些个案结论。
- 本次只用 FTB 概述核实州税边界，未核实四重点州的完整居民判定与跨州收入分配。不能将本页联邦测试改写为全国州税标准。
- 未登录真实税务账户、提交表件、采集个人记录或联系机构。准备证据、列出差异及寻求国际个人税专业核对是稿件的行动建议，并非对真实申报结果的保证。
- 本结论仅绑定上述正文 SHA。正文若修改，须重新计算 SHA；实质事实、行动或范围变化须复核受影响断言，再交第三名参与者静态审。
