---
title: "美国税务居民怎样判断：绿卡、居留天数与学生例外"
description: "按税年核对联邦税务身份，算清三年居留天数，分辨学生排除、境外较密切联系、税收协定和州税规则。"
page_id: work.tax.tax-residency
content_kind: task
scope: "美国联邦个人所得税；主要面向非美国公民，州税另判；规则查阅至 2026-10-13，表件说明使用查阅时已发布版本"
status: integrated
draft: false
verified: '2026-10-14'
reviewed_by: banking_fact（差分事实审）；birth_fact（第三静态审）
weight: 10
---

先确定报哪一个税年，再判断这一年哪些时段属于美国税务居民。税表中的 **resident alien / nonresident alien** 是税务分类，不能直接从国籍、签证名称、SSN，或“今年住了半年”推出来。一个持临时工作身份的人可能已经是税务居民；符合学生计日排除条件的人，即使全年在美国，也可能仍是非居民。[IRS：个人税务居民判定](https://www.irs.gov/individuals/international-taxpayers/determining-an-individuals-tax-residency-status)

这里讨论联邦个人所得税。美国公民通常按公民规则处理全球所得，不走下文非公民的两项测试；遗产赠与税、Social Security / Medicare 工资税和州税各有自己的适用规则，不能拿本页结论一概代替。移民文件本身的用途见 [签证、I-94、身份与工作授权](/book/life/documents/status-documents/)。

## 先把税年与证据放在一起

多数个人按 **1 月 1 日至 12 月 31 日** 的日历年判断。先建一张记录表：

| 要整理的资料 | 用来判断什么 |
|---|---|
| 本年及前两年的每次入境、离境日期，护照、I-94、机票等记录 | 实际在美天数，以及三年加权计算 |
| 绿卡身份生效、放弃或终止文件；身份变更批准文件 | 是否满足绿卡测试、居民起止日期 |
| 历次 F / J / M / Q 身份与项目记录、I-20 / DS-2019、以前的 Form 8843 | 哪些天可以排除；学生等身份过去已经使用了多少日历年 |
| 境内外工作地点、住房、家庭、税务申报与身份申请记录 | tax home、较密切联系及协定居民的事实依据 |
| 各类收入、收款日期、W-2 / 1042-S / 1099 和以往税表 | 确定身份后选择申报路径、划分时段并核对以前的处理 |

旅行记录可能有遗漏，身份也可能在境内改变。发现两个来源对不上，先列出差异再补证，不要为了得到某个税务结论删改日期。号码申请另见 [SSN 与 ITIN](/book/life/documents/numbers/)。

## 第一步：本年是否满足绿卡测试

非公民在日历年中任何时候具有美国合法永久居民身份，通常就满足 **green card test** 。这回答的是是否触发居民规则；居民期从哪天开始，还要另判，不能直接把取得绿卡的一年都填成全年居民。[IRS：绿卡测试](https://www.irs.gov/individuals/international-taxpayers/us-tax-residency-green-card-test)

绿卡到期、长期在海外或没有在美国领工资，都不自动结束这项税务居民认定。IRS 要求结合正式放弃、行政或司法终止等依据判断；若准备依税收协定主张其他国家居民，也应先看下文的协定和长期居民边界。不要先停报居民税表，再把身份终止手续留到以后。[IRS Publication 519：Green Card Test、Resident status abandoned](https://www.irs.gov/publications/p519)

没有满足绿卡测试，继续算居留天数。已满足的人也应算：两项测试可能产生不同的居民起始日。

## 第二步：先排除合格天数，再算三年加权

**Substantial presence test（实质居留测试）** 必须同时满足两个条件：本年可计入天数至少 31 天；本年全部可计入天数，加上上一年可计入天数的三分之一、上上年的六分之一，合计至少 183 天。[IRS：实质居留测试](https://www.irs.gov/individuals/international-taxpayers/substantial-presence-test)

```text
加权天数 = 本年天数 + 上一年天数 ÷ 3 + 上上年天数 ÷ 6
```

下面是 **教学虚构例子** ，假设所有列出的天数都可计入，且尚未检查较密切联系或协定例外：

| 用于判断的税年 | 本年 | 上一年 | 上上年 | 加权结果 |
|---|---:|---:|---:|---:|
| 2025 年 | 150 天 | 120 天 | 120 天 | 150 + 40 + 20 = 210 天 |

这个人本年不足 183 天，却同时满足 31 天和三年加权 183 天门槛。接下来仍要检查例外；210 天也不是其实际在美国生活的天数。

一般一天中任何时间实际身在美国，就算一天，入境和离境日也应检查。这里的美国范围包括 50 州、华盛顿特区等法定地域，不包括美国属地和美国领空；经停、跨境通勤、特定船员及医疗情况另有计日条件，不能只用手机定位总天数。[IRS：Days of presence、美国范围](https://www.irs.gov/individuals/international-taxpayers/substantial-presence-test)

最常遇到的排除分支是：

- **符合条件的学生、教师或受训者等 exempt individual。** 这里的 exempt 指居留测试中排除天数，不表示其收入全部免税。不同类别有不同年限，不能把学生规则套给所有 J 类访问学者。
- **在两个美国境外地点之间转机，在美不足 24 小时。** 这是有特定目的和时长条件的过境排除，不是“待不足一天都不算”。
- **在美期间发生医疗问题，导致原本打算离境却无法离境。** 已知旧病、来美就医，或已经能够离境却继续留下等情况不能直接套用。需要按 Form 8843 Part V 核对，并由医生等医疗人员完成相应证明。

每个排除日都应记下理由及支持文件；跨加拿大 / 墨西哥经常通勤、船员、外交及其他特殊身份，按对应条目另核。[Form 8843 说明，第 3—4 页](https://www.irs.gov/pub/irs-pdf/f8843.pdf)

## 学生的五个日历年怎样数

以学习为主要目的、暂时持 F、J、M 或 Q 类身份在美且实质遵守身份条件的学生，可能排除相应天数。通常所说的 **五年是五个日历年** ，不是 60 个月，也不是每个学位重新获得五年。核对历次已作为学生、教师或受训者等适用类别排除天数的年份；某年只符合一部分时间，也会占一个日历年。[IRS：Exempt individual — Student](https://www.irs.gov/individuals/international-taxpayers/exempt-individual-who-is-a-student)、[Form 8843：Part III — Students](https://www.irs.gov/pub/irs-pdf/f8843.pdf)

**教学虚构例子：** 某学生此前没有相关排除年份，2021 年 12 月首次以 F-1 身份来美，此后每年都符合学生排除条件。2021 年已经算第一个日历年，通常的五年到 2025 年用完。2026 年应重新判断能否继续排除；若不行，把可计入天数放回实质居留测试。第六年不是仅凭日历翻页就必然成为居民，还要看实际天数及其他适用规则。

超过通常五年后，学生仍可能以事实证明没有永久居美意图、持续遵守学生身份要求、没有采取取得永久居民身份的步骤，并与境外国家保持更密切联系。举证责任在学生本人；这项学生规则与下一节使用 Form 8840 的一般较密切联系例外不同，不能混用。[IRS：专供外国学生的例外及四项条件](https://www.irs.gov/individuals/international-taxpayers/the-closer-connection-exception-to-the-substantial-presence-test-for-foreign-students)

符合学生排除条件时仍须提交 **Form 8843** ：需要报 1040-NR 的，随税表附上；无需提交所得税表的，也要按该税年说明单独寄送 8843，并核对适用申报期限。没有收入不等于没有这项表格义务。反过来，有工资、奖学金或其他收入时，应另判收入性质、免税依据和 1040-NR 申报要求；“五年学生例外”本身不免除这些收入的税。[Form 8843：Who Must File、When and Where To File](https://www.irs.gov/pub/irs-pdf/f8843.pdf)、[IRS：非居民申报要求](https://www.irs.gov/individuals/international-taxpayers/taxation-of-nonresident-aliens)

## 第三步：满足加权测试，是否仍有例外

### 一般的境外较密切联系

**Closer connection exception** 可能使已经满足实质居留测试的人仍按非居民处理，但不能只说“我的家在中国”。通常须同时核对：

1. 本年在美天数少于 183 天。这一项看本年，不看三年加权合计。
2. 全年在境外维持 tax home，并与该国保持比美国更密切的联系。
3. 没有绿卡身份，也没有申请、采取取得绿卡的步骤或待审的身份调整申请等情形。
4. 按要求及时提交 **Form 8840** ，随所得税表附上；无需报所得税表的，也须单独提交。

tax home 通常指主要工作、营业或任职地点所在地区，不简单等于户籍、房产所在地或家人住处。需要结合长期住房、家庭、物品、社会活动及官方文件等事实证明联系。年中从一个外国转到另一个外国，也有专门的两国条件，不能把“全年同一外国”的通常路径硬套过去。[IRS：较密切联系例外及申报](https://www.irs.gov/individuals/international-taxpayers/closer-connection-exception-to-the-substantial-presence-test)、[Form 8840 说明，第 3—4 页](https://www.irs.gov/pub/irs-pdf/f8840.pdf)

未按时提交 8840，通常不能主张这项例外；IRS 对有明确且令人信服证据证明已合理了解并采取重大合规步骤的情形另设例外。已经漏报时，应整理往年天数、材料和具体原因，让熟悉国际个人税的专业人员核对补救条件，不能只在下一年补勾一个选项。[IRS：Requirement to file Form 8840](https://www.irs.gov/individuals/international-taxpayers/closer-connection-exception-to-the-substantial-presence-test)

### 两国都认定为居民时，查具体协定

如果两国国内法都认定你为居民，适用的所得税协定可能有解决居民冲突的条款。应查该协定的居民条款、具体事实和披露要求；持某国护照，不代表自动获得该国所有协定待遇。协定对某项收入减免，与协定把你判为另一国居民，也不是同一个判断。[IRS：Tax treaties](https://www.irs.gov/individuals/international-taxpayers/tax-treaties)

符合条件并主张按协定成为另一国居民的 dual-resident taxpayer，计算美国所得税时按非居民规则处理，须提交 **Form 1040-NR 并附 Form 8833** 披露。不能因此推断其他所有美国申报义务也消失。长期绿卡居民这样主张还可能触发终止税务居民的特殊规则及 Form 8854；作选择之前应一起核对，不能把它当作普通软件选项。[Form 8833：Dual-resident taxpayer、Termination of U.S. Residency](https://www.irs.gov/pub/irs-pdf/f8833.pdf)

## 第四步：划清居民期，再选申报路径

触发居民测试的日期，不一定是居民期起点。实质居留测试下，一般从本年第一次可计入的在美日开始；不是从加权累计够 183 天的那一天才开始。只满足绿卡测试时，一般从本年第一次以永久居民身份在美之日开始；两项都满足时，核对较早的适用起点。上一年已有居民期间、学生排除结束等情况还会影响起点。[IRS：Residency starting dates](https://www.irs.gov/individuals/international-taxpayers/residency-starting-and-ending-dates)

离境也不自动从当天起结束居民期。一般结束日及提前结束的条件，要结合剩余年度的境外 tax home、较密切联系、下一年是否又成为居民，以及须提交的签名声明判断。准备离美或终止绿卡身份时，把本年和下一年的安排一起核对。[IRS：Residency ending dates、所需声明](https://www.irs.gov/individuals/international-taxpayers/residency-starting-and-ending-dates)

一年内先后既是居民又是非居民，称为 **dual-status** ，不是双重国籍，也不同于同时被两国认定为居民的 dual-resident。[IRS：Dual-status individuals](https://www.irs.gov/individuals/international-taxpayers/taxation-of-dual-status-individuals)

| 判定结果 | 接下来核对的联邦所得税路径 |
|---|---|
| 全年居民 | 一般以 1040 / 1040-SR 路径处理全球所得，包括境外工资、利息和租金；具体是否须报、抵免与排除另按规则判断 |
| 全年非居民 | 有申报义务时使用 1040-NR；区分与美国经营有效关联的所得，以及其他应税美国来源所得，不能把非居民理解成无需报税 |
| dual-status | 分开居民和非居民时段；年末为居民通常以 1040 作主表并附非居民期说明，年末为非居民通常以 1040-NR 作主表并附居民期说明，按要求标注 |

居民通常涉及全球所得；非居民一般以美国来源所得为主，但有限情形下境外来源所得也可纳税。dual-status 的主表、说明及扣除限制须按当年说明处理。[IRS：居民所得](https://www.irs.gov/individuals/international-taxpayers/taxation-of-us-residents)、[IRS：居民、非居民及 dual-status 基本规则](https://www.irs.gov/individuals/international-taxpayers/alien-taxation-certain-essential-concepts)

所得来源也不能仅由收款银行所在地决定。例如工资通常看实际提供服务的地点，房租看房屋所在地；海外雇主往海外账户付款，不足以单独证明是境外来源工资。[IRS：所得来源分类](https://www.irs.gov/individuals/international-taxpayers/nonresident-aliens-sourcing-of-income)

还有两种可能改变结果的选择，不能只为了套用一款报税软件而作：

- **First-year choice。** 在本年与前一年均未满足两项居民测试、前一年也未作这项选择，而下一年满足实质居留测试等条件下，可能选择把本年的一部分作为居民期。还要满足本年连续 31 天及相应期间至少 75% 居留要求，并等到下一年实际满足测试后按程序提交声明；部分缺席日另有有限计入规则。[IRS：First-year choice](https://www.irs.gov/individuals/international-taxpayers/alien-tax-status-first-year-choice)
- **与公民或税务居民配偶共同选择。** 符合条件的夫妻可以选择把非居民配偶按全年居民处理并联合申报，但随之要处理双方全年全球所得，且选择可能延续至以后年度，停止也有限制。先比较完整后果，再按要求由双方签署声明。[IRS：Nonresident spouse](https://www.irs.gov/individuals/international-taxpayers/nonresident-spouse)

## 州税再单独判断

联邦非居民不保证是所在州的非居民。以加州为例，FTB 关注是否为了非临时目的在州内居住，以及以加州为 domicile、只因临时目的离州等事实；它不是照抄上述三年计日公式。联邦协定待遇也不保证各州承认。[加州 FTB：居民判定](https://www.ftb.ca.gov/file/personal/residency-status/index.html)、[IRS：协定与州税](https://www.irs.gov/individuals/international-taxpayers/tax-treaties)

到实际居住、工作及有收入来源的州税务机关分别查 resident、part-year resident 和 nonresident 要求。跨州搬家、远程工作或夫妻分居两州，应保存各州入住、离开及工作地点记录。

办理前应能写出一份简短结论：报哪个税年；两项测试的结果；排除哪些天及理由；是否主张例外、协定或选举；居民期起止日期；需提交哪些税表、附表和声明。将结论与支持文件一起保存，再进行收入计算和申报。以前用错居民类型、漏交声明或存在两国冲突时，把完整资料交给处理国际个人税的专业人员核对，不要只更换本年的表格而忽略以前年度。
