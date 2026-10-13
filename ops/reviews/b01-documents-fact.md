# B01 证件与加州押金：独立事实审

- 审阅人：`/root/health`；作者：`/root/documents`，为不同参与者。
- 实际查阅与复核日期：2026-10-13。
- 结论：下列三篇在注明的范围内 **事实审通过** 。作者已处理四项事实或行动边界修订，审阅者重读最终正文并核对修订依据；没有剩余阻断项。
- 本记录只完成独立事实审，不代替第三人静态审、构建、实际渲染与主控正式集成。

## 绑定版本

从实际文件读取 UTF-8 字符串，对 `split('---', 2)[2]` 的正文重新编码并计算 SHA-256；不含 YAML 元数据。

| 正文路径 | 最终正文 SHA-256 | 结论 |
|---|---|---|
| `content/book/life/documents/status-documents.md` | `16e535093fd8b475a697b10581a6e99d920b8424a71d5d80929c786a924c4721` | 通过 |
| `content/book/life/documents/numbers.md` | `b19d8a3a61087b71ff259ee2164b2f967e475398fa84436f5fa12207f1d1c32a` | 通过 |
| `content/book/life/housing/ca-deposit.md` | `57553e2b832b8157cd4a7144cf9bcf2bbb32afbb1ace82fde529d2b7a0463c8d` | 通过 |

## 实际阅读的官方原文

审阅者完整阅读三篇正文，再独立打开下列官方资料。网页浏览工具无法取得正文时，使用正常 TLS 的 Python HTTP 请求读取官方网页，或在内存解析官方 PDF；没有把搜索摘要、作者记录或其他人的结论当成实际查阅。

| 来源与原文定位 | 核验内容及边界 |
|---|---|
| [国务院：签证有效期](https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/visa-expiration-date.html)，What the Visa Expiration Date Means、Admission / Duration of Stay | 签证是申请入境的凭据，口岸决定准入与停留；I-94 日期与 D/S 不等于签证贴纸期限。 |
| [USCIS：I-797 类型](https://www.uscis.gov/forms/filing-guidance/form-i-797-types-and-functions)，完整类型表 | A 附替代 I-94；B 为工作者 petition 批准；C 的多种通知用途；E 补件。正文要求读完整通知，没有用表号取代具体决定。该页经 Python 读取。 |
| [USCIS：EAD](https://www.uscis.gov/green-card/green-card-processes-and-procedures/employment-authorization-document)，适用对象、Renewing、Incorrect Information | 永久居民及部分依身份就业者无需另有 EAD；证明已有工作权和申请工作权的区别；续期一般鼓励到期前 180 天内；USCIS 错误与申请人资料错误更正程序不同。经正常代理 HTTP 读取完整正文。 |
| [USCIS：2025-10-29 通知](https://content.govdelivery.com/accounts/USDHSCIS/bulletins/3f927da)，effective date / exceptions 段；[现行政策手册](https://www.uscis.gov/policy-manual/volume-10-part-a-chapter-4)，I. Automatic Extensions | 独立核对 2025-10-30 起相关续期不再自动延长、此前已获延长不受该变更影响、法律与 TPS 专项例外；现行手册仍限定此前特定合格类别的及时续期。没有把通知概括为全部类别一律停止工作。 |
| [USCIS：永久居民卡手册](https://www.uscis.gov/policy-manual/volume-11-part-b-chapter-1)，Purpose、Background、条件居民脚注 | 卡片是身份及证明文件；卡片期限不能机械代替个案身份判断。正文未提供放弃永久居民身份或条件身份解除的完整操作程序。 |
| [SSA：首次申请](https://www.ssa.gov/number-card/request-number-first-time)，申请步骤、费用与送达；[SSA：卡片类型](https://www.ssa.gov/ssnumber/cards.htm)，三种卡；[非公民资格 FAQ](https://www.ssa.gov/faqs/en/questions/KA-02178.html) | 免费、在线开始与办公室出示材料、官方电话号码、批准后 5—10 工作日；限制文字不等于不受条件的工作权。 |
| [SSA：材料选择器](https://www.ssa.gov/ssnumber/ss5doc.htm)，Original / Noncitizen Adult 及对应身份、学生材料段 | 原件或发证机关认证副本、首次至少两份不同文件、F-1 的 I-20 与校内工作证明或 CPT / EAD、J 类材料；不同类别没有被写成统一一套文件。网页包含多个展开状态，审阅读取相应原文，而非仅首页标题。 |
| [SSA POMS RM 10211.600](https://secure.ssa.gov/poms.nsf/lnx/0110211600)，A.1—A.3 | 非工作 SSN 要求法定福利用途、其余资格及主管机构证明；州和地方公共救助还要求合法居留。正文已按原文收窄，不把驾照或一般生活便利列作资格。 |
| [IRS：ITIN](https://www.irs.gov/tin/itin/individual-taxpayer-identification-number-itin)，资格、处理时间、取得 SSN、未取得 ITIN 的延期及付款 | ITIN 与 SSN 资格分流、无工作或福利授权、7 周及报税季 / 海外 9—11 周、原件 60 天查询、SSN 后停用 ITIN 并合并记录。 |
| [IRS：申请 ITIN](https://www.irs.gov/tin/itin/how-to-apply-for-an-itin)，W-7、各递交渠道、通知；[W-7 说明](https://www.irs.gov/instructions/iw7)，Supporting Documentation Requirements | 通常与税表同递交及免附税表例外；TAC、指定 VITA、CAA 与 AA 区别；护照、被扶养人在美居住证明、认证范围；CP565 / CP566 / CP567 下一步。W-7 支持文件段另以 HTTP 完整读取。 |
| [IRS：ITIN 续期](https://www.irs.gov/tin/itin/how-to-renew-an-itin)，When to renew；[W-7 说明](https://www.irs.gov/instructions/iw7)，Reminders / Expired ITINs | 三个连续税年未用于联邦所得税申报的失效、仅信息申报用途例外；W-7 明写第三个税年 12 月 31 日，正文与之相符。 |
| [DRE：入住指南](https://www.dre.ca.gov/publications/ResourceGuidebook/gb07_when.html)，Security Deposits、Service Members、Inventory Checklist | 2024-07-01 一个月押金上限、小房东两项条件及军人例外、押金各种名称加总、不退条款、2025-07-01 新租约入住照片。 |
| [DRE：搬出指南](https://www.dre.ca.gov/publications/ResourceGuidebook/gb10_movingout.html)，Initial Inspection Before Tenant Moves Out、Refund of Security Deposits | 预检通知包括固定租约到期，申请后最后两周及 48 小时书面通知、违约情形例外；扣款与后续凭据的细节另与下项法条独立对照。 |
| [DRE《2026 Real Estate Law》官方法典摘录](https://www.dre.ca.gov/files/pdf/relaw/2026/excerpts.pdf)，Civil Code §1950.5，印刷第 143—149 页，PDF 索引 142—148 | 实际读取完整条文相关段：(b)(e) 扣款范围、正常损耗、专业清洁；(c) 旧押金、预付、改造、自然人 / 家庭信托及军人边界；(f) 预检；(g) 入住及搬出维修前后照片；(h)(1) 21 个日历日、电子及合租退款；(h)(2)—(5) 明细 / 照片 / 收据、≤125 美元例外、估价及两个 14 日期限；(m) 恶意法定赔偿。PDF 在内存解析，没有把指南简写替代条文例外。 |
| [加州法院：押金指南](https://selfhelp.courts.ca.gov/guide-security-deposits-california)，全部主要行动段 | 可扣项目、书面索偿、小额诉讼自然人 12,500 美元及恶意最高两倍押金另加实际损失；经 Python 读取正文，未把网页浏览工具的 403 记为成功。 |
| [加州检察长：租客保护提示](https://oag.ca.gov/news/press-releases/attorney-general-bonta-issues-consumer-alerts-guidance-protect-california)，地方保护、押金与求助段 | 地方可能另有押金利息与更强保护；正文要求按实际地址查城市 / 县，没有编造湾区统一规定。 |

## 已修订并复核的事项

1. 非工作 SSN：原表述可能扩展到一般公共服务；现明确联邦出资福利、其余资格，以及州 / 地方公共救助的合法居留条件，与 POMS 相符。
2. EAD 旧自动延长：现明确特定合格类别和及时续期，不再造成过去所有续期一概自动延长的印象。
3. 押金 21 天：现说明允许邮寄时按期限寄出，不把租客实际收件日当作唯一判断标准。
4. 预检触发：现补任一方结束租赁意向通知及固定租期届满前合理时间，不漏无须另发解约通知的到期情形。最后一次修订后重新计算住房 SHA。

作者补入的 2026 年电子 / 合租退款、125 美元包含等号、照片交付例外与旧押金边界，均另回 §1950.5 实际条文复核。教学英语索偿例句明确虚构，不假冒真实来信或个案。

## 未核实边界与复核触发

- CBP I-94 在线工具是动态页面；本次帮助页未返回可读正文，CBP 静态资料另受 403 限制。未登录或查询任何真实 I-94，也未验证个案更正结果。正文只链接官方入口并要求核对、询问，没有编造特定处理时限；文件用途另由国务院及 USCIS 正文交叉支持。
- Leginfo 直连与正常代理均遇 403；未宣称读到该站。加州法条依据是 DRE 官方 2026 年法典摘录。未穷尽地方条例、补助住房、机构破产或特殊终止租约规则，正文已有对应边界与求助分流。
- 没有测试 SSA / IRS / USCIS 的真实申请或电话服务，没有确认任何个人的资格、等待时间、移民诉讼适用范围或合同争议结果。处理时间保留为官方一般预期。
- 增加具体身份类别、移民专项延期、地方押金利息、税年申报细节或改动行动期限时，须重新查原文并复核。正文任何变更均需重算 SHA；实质变更不能仅更新日期沿用本结论。
