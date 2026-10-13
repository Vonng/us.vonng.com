# B04 跨州税务：独立事实审

审查人 documents；作者 civic，彼此独立。查阅日期 2026-10-13。对象 `content/book/work/tax/state-residency.md`。已完整阅读正文与作者证据，以下来源均由审阅者独立实际取得正文。结论：事实审通过。作者已按意见补入纽约住所期间的现行审计口径，审阅者对照第 49—51 页原文复核新增段；四州三列表格也重新核对，未改变适用范围。最终正文 SHA-256：`05d6c6adeefc9b4c4c3cd1fa1e7263d5101f60367b07baf589c038f77c180017`。计算方法 `sha256(text.split('---', 2)[2].encode('utf-8'))`，不含 frontmatter。后续第三人静态审、元数据、构建与集成由主控完成。

## 独立回源范围

通过 web open 或普通 HTTPS 请求取得官方网页，BeautifulSoup 提取主文；PDF 在内存解析。不把搜索摘要当原文，不用作者记录替代实读。长表件只核与正文有关的部分，不声称读完全部税务表册。

| 来源 | 实际阅读位置、核对结果 |
|---|---|
| [FTB Residents](https://www.ftb.ca.gov/file/personal/residency-status/index.html)；[Part-year and nonresident](https://www.ftb.ca.gov/file/personal/residency-status/part-year-and-nonresident.html) | 两页主体与后者 Leaving California 四种场景：居民全球所得、非居民来源所得、部分年度划分、雇员与承包服务区别、申报入口。具体申报收入门槛仍属 2025，正文没有冒充 2026 门槛。普通雇员工资依据服务所在地，不能只因雇主在加州而全部归加州来源。 |
| [FTB 2025 Publication 1031](https://www.ftb.ca.gov/forms/2025/2025-1031-publication.pdf) | 实读纸页 4、5、6、10、11 的定义、联系强弱、迁居、工资来源、domicile 与共同财产；相邻安全港条件读到但稿件未借其推定所有搬家。没有以证件或 183 天单独判定 CA 身份；配偶、住所、目的与实际迁移仍重要。 |
| [FTB Publication 1100](https://www.ftb.ca.gov/forms/misc/1100.html) | 实读 B Tax Computation Method，以及 D Individual Retirement Accounts, Employer-Sponsored Retirement Plans, and Compensation 的相关工资段、例 9—12，兼读 E 股票期权边界。有效税率公式与迁走后收到旧 CA 服务工资的处理支持正文；未把旧算例金额当新税年税额。正文引用标签 Compensation for Services 是主题描述，实际段题为上述 D。 |
| [NY Nonresident FAQ](https://www.tax.ny.gov/pit/file/nonresident-faqs.htm)；[Income tax definitions](https://www.tax.ny.gov/pit/file/pit_definitions.htm) | 主文实际读到 domicile、住所与 184 天双条件、两组 domicile 例外、NY 来源、全年口径再分配、主要办公室与居家办公、NYC 非居民。居留日与工作日分开，少于 184 天不排除 domicile 路径。定义页仍直接链接下列 2021 审计指南。 |
| [NY Nonresident Audit Guidelines, December 2021](https://www.tax.ny.gov/pdf/2021/misc/nonresident-audit-guidelines-2021.pdf) | 实读第 49—51 页 D、E 与第 52—54 页相关计日原文；自 2022 税年开始一般超过十个月，适用于当年取得或处置住所，短暂出租既有住宅不能机械扣月，州内住所可接续；不是绝对安全港。这一实际期间是本次要求作者补进正文的修订。 |
| [TSB-M-06(5)I](https://www.tax.ny.gov/pdf/memos/income/m06_5i.pdf)；[2025 IT-203 instructions](https://www.tax.ny.gov/forms/current-forms/it/it203i.htm) | Memo 第 1—4 页实际读到，IT-203 实读居民定义、Line 1、Schedule A 工作日与主要办公室条件、Schedule B 居留日。NY 主要办公室与外州主要办公室不能混为“纽约总部”；home office 有多因素条件。W-2 州工资不必等于分配后的 NY 来源额，工作日不等于所有居留日。 |
| [NY NYC, Yonkers and MCTMT](https://www.tax.ny.gov/pit/file/nyc_yonkers_residents.htm) | 主文全部阅读。NYC 五区、IT-360.1 随 IT-201 或 IT-203、Yonkers 非居民 earnings 另表，与正文分层一致；自雇 MCTMT 数值不在稿件普通雇员范围。 |
| [FTB Other State Tax Credit](https://www.ftb.ca.gov/file/personal/credits/other-state-tax-credit.html)；[2025 IT-112-R instructions](https://www.tax.ny.gov/forms/current-forms/it/it112ri.htm) | FTB 全部主文；NY General instructions、part-year、dual residency 与 Line 24 相关说明实际读到。CA Schedule S 附另州税表、另一州给予抵免时的限制；NY 居民期且来源于另一辖区并被征税的限制；Line 24 明确不是工资扣缴或预缴额。正文未保证抵免全部双重税。 |
| [WA Income Tax FAQ](https://dor.wa.gov/taxes-rates/income-tax/frequently-asked-questions-about-income-tax) | 普通 HTTPS 成功取得并完整阅读 main：2026 没有一般个人所得税；已公布新税从 2028-01-01 开始、首批申报 2029。正文将当前与未来分开，不以旧常识推定永久无税，不代判特定读者资格。 |
| [WA Capital gains FAQ](https://dor.wa.gov/taxes-rates/other-taxes/capital-gains-tax/frequently-asked-questions-about-washingtons-capital-gains-tax) | 实读股票债券等无形资产分配、出售时 domicile、不动产与退休账户豁免、扣除及申报区别。正文没有未经税年核验的税率或扣除额。 |
| [Texas Constitution VIII §24-a](https://tcss.legis.texas.gov/Docs/CN/htm/CN.8.htm)；[Comptroller Taxes](https://comptroller.texas.gov/taxes/) | 宪法 §24-a 全条实际阅读；目录实读销售税、车辆税及其他税种。普通个人工资不交 TX PIT 与仍存在其他税种的区分成立，没有把实体 franchise tax 扩张给雇员。 |
| [IRS 2026 W-2](https://www.irs.gov/pub/irs-pdf/fw2.pdf) | 实读 Copy 1 表格 15—20 及联邦 Box 1，并读员工更正说明；州与地方工资/扣缴/辖区字段对应正确。正文是在州工资金额分配语境要求雇主更正，不授权自行更改金额。 |
| [FTB estimated payments](https://www.ftb.ca.gov/pay/estimated-tax-payments.html)；[NY estimated tax](https://www.tax.ny.gov/pit/estimated_tax/) | 两页实际主文；只用于支持扣缴不足时应核对本州当年预缴。FTB 网页仍混入 2024 金额说明与 2026 日期，正文没有采用这些旧额或声称四期相等。 |
| [FTB Letters](https://www.ftb.ca.gov/help/letters/index.html)；[NY Letters](https://www.tax.ny.gov/pit/letters/)；[NY refund adjustments](https://www.tax.ny.gov/pit/file/more_info_refunds.htm) | FTB 实读 PIT4044、4600；NY 实读 RFI 与居住/工作/分配材料、AU-262.3/262.55、按通知回应；refund 页主文实读 DTF-160/161、比较 Explanation 并提供支持文件。正文不凭一个通知的期限推广所有来信，也不把再交原始表当回应通知。 |

## 边界与判断方法

以普通 W-2 跨州搬家和远程工作为界，未审核个案 domicile、所有联邦身份/协定、夫妻共同财产分配公式、复杂股权/递延、自雇、军人、运输人员或全部地方税。纽约例外和工作日规则仅核正文使用范围；没有完整审计 107 页指南全部案例。WA 未来新税未独立作全部法案及诉讼状态分析，正文仅引用主管机构当日公布的实施时点，并要求临近税年复核。

教学例子明确假设 CA 居民身份已经结束、普通工资全在州外、没有夫妻分配与股权复杂问题；结论没有越过这些前提。完成标志属于保存税表、接受回执与付款记录的实务建议，不是对所有申报系统内部状态的事实保证。
