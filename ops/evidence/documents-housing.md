# B01 documents / housing 事实链

作者 documents；实际研究日期 2026-10-13。以下来源实际打开正文或官方PDF；搜索仅用于发现。Python `urllib.request`、BeautifulSoup及pypdf只在内存读取，未保留大型下载物、未进入私人账户。独立事实审由 health 另行进行。

## 签证、I-94、I-797和EAD

对应 `content/book/life/documents/status-documents.md`。

| 来源 | 实读位置、采用断言 | 时期、边界与访问 |
|---|---|---|
| [State visa expiration](https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/visa-expiration-date.html) | What the Visa Expiration Date Means；Admission/Duration；Extension：签证用于申请入境，口岸决定准入和停留，I-94具体日期与D/S，签证到期不能直接替代停留日期 | 联邦非移民；网页未显示内容修订日；web打开完整核心正文 |
| [USCIS I-797 types](https://www.uscis.gov/forms/filing-guidance/form-i-797-types-and-functions) | 完整表格，I-797A替代I-94；B工作者petition批准；C收件/退件/约见；E补件 | Last Reviewed/Updated 2025-01-24；web错误，urllib直连200正文 |
| [USCIS I-797C](https://www.uscis.gov/forms/all-forms/form-i-797c-notice-of-action) | What is / Benefits：C本身为收件通知，不授予身份或移民利益 | Last Reviewed/Updated 2021-01-25；urllib实读；另一个 filing-guidance 旧路径404，未引用 |
| [USCIS EAD](https://www.uscis.gov/green-card/green-card-processes-and-procedures/employment-authorization-document) | 前三节：EAD证明工作授权；授权本身与资格证明差异；永久居民不需EAD；H/L等特定雇主身份；续期180天；更正USCIS错误与申请人错误不同 | Last Reviewed/Updated 2025-10-30；urllib直连200；未采用邮寄具体地址和处理时间，避免没有必要的维护负担 |
| [USCIS官方GovDelivery通知](https://content.govdelivery.com/accounts/USDHSCIS/bulletins/3f927da) | 全文，2025-10-30及以后特定EAD续期取消自动延长；此前已经延长不撤销；法律及TPS Federal Register例外 | USCIS发布2025-10-29 09:42 EDT；未采用发布者政治措辞 |
| [USCIS Policy Manual vol10 A ch4](https://www.uscis.gov/policy-manual/volume-10-part-a-chapter-4) | I. Automatic Extensions：明确only timely filed before 2025-10-30；脚注86 | 2026-10-13实读现行正文，未把2025新闻单独视为当前执行证据 |
| [Federal Register 2025-19702](https://www.federalregister.gov/documents/2025/10/30/2025-19702/removal-of-the-automatic-extension-of-employment-authorization-documents) | 标题、规则概述、生效与法规引用，90 FR48799 | interim final rule，发布日期2025-10-30；现行执行再以政策手册互核 |

CBP `https://www.cbp.gov/travel/international-visitors/i-94` 和自动化旧PDF直连/工具403；指定正常代理也未解决。`https://i94.cbp.dhs.gov/help` 可达但web无脚本正文，故仅作为公开查询/求助入口，未写未经实读的“30天内更正”或操作按钮。未把2015旧PDF搜索摘要当证据。申请个人记录的实际结果未测试。

EAD具体国别TPS、学生OPT和诉讼当事人的延长期限不在本稿概念页内作一刀切判断；检索发现2026个案诉讼线索，但没有读取相应法院命令，不声称全国推翻、暂停或完整法院动态核验。正文明确需核对适用于本人的专项通知或法院命令。

## SSN和ITIN

对应 `content/book/life/documents/numbers.md`。

| 来源 | 实读位置与采用断言 | 版本与边界 |
|---|---|---|
| [SSA首次申请](https://www.ssa.gov/number-card/request-number-first-time) | 全文：免费；online开始/办公室交材料；批准后5—10工作日邮寄；公民及合格非公民 | web可读；直接urllib部分403；页面未给修订日 |
| [SSA材料选择器](https://www.ssa.gov/ssnumber/ss5doc.htm) | Original Card for Noncitizen Adult；citizen adult；corrected card：至少两份不同材料、原件/发证机关认证副本；F/J文件及工作证明；更正仍原号码 | web正文可读，未登录表单；不把所有身份套同一文件组合 |
| [SSA卡类型](https://www.ssa.gov/ssnumber/cards.htm) | 全文三种限制文字 | 文本未显示修订日；号码不代表当前工作授权 |
| [SSA POMS RM10211.600](https://secure.ssa.gov/poms.nsf/lnx/0110211600) | A1–A3：非工作理由仅联邦出资福利法定需要、或合法居留且已具其余资格的州地方公共救助；机构原信及其他身份材料 | Rev 2023-02-07，页面batch run2026-07-23；health独立审指出初稿概括过宽，已精确改写 |
| [IRS ITIN主说明](https://www.irs.gov/tin/itin/individual-taxpayer-identification-number-itin) | What used for；Who needs；When apply；After apply；Get SSN：税务用途与不具SSN资格，工作/身份边界，等待、原件、转SSN合并记录 | 2026-10-13实际全文；未采用该页过度简写的183天税务居民句子，税年抵免金额未进入本稿 |
| [IRS how to apply](https://www.irs.gov/tin/itin/how-to-apply-for-an-itin) | What need；Apply in person对照；After：W7/税表/证件，TAC/VITA/CAA/AA差异，CP565/566/567，7周/9–11周/60天 | 当前页面全文urllib200；SSA申请批准与IRS等待起算点分开写 |
| [IRS W7 instructions](https://www.irs.gov/instructions/iw7) | Supporting Documentation；How/When apply；Where apply；Exceptions：原件/发证机关副本，护照及被扶养人居住证明边界，附税表例外 | 12/2024说明与W7修订；未复述税收抵免年度规则 |
| [IRS renew](https://www.irs.gov/tin/itin/how-to-renew-an-itin) | 全文：三连续税年未使用则第三年底失效；信息申报可继续用；Renew既有号码；取得SSN不再续ITIN | 当前官方网页，不把ITIN过期写成移民身份过期 |

SSA ss5doc与旧POMS EBE页面仍叙述I-765/I-485自动制卡；发现停止/变动的外部线索但未获取足够官方当前实施证据。因此稿件只保留已申请联办者向SSA说明与查询、直接SSA申请可行路径；未承诺填写移民表格即可收到卡，也未宣称联办已全面恢复或终止。

## 加州押金

对应 `content/book/life/housing/ca-deposit.md`。

| 来源 | 实读位置与支持断言 | 版本与边界 |
|---|---|---|
| [DRE 2026 Real Estate Law excerpts](https://www.dre.ca.gov/files/pdf/relaw/2026/excerpts.pdf) | 印刷p143–149（PDF索引142–148）§1950.5(a)–(r)逐段实读；(c)1月/小房东/军人/家庭信托/预付/旧押金；(f)预检；(g)照片；(h)21天、2026电子与多人退款、125含等号及14天；(m)恶意赔偿 | 2026官方法典摘录，实际urllib下载到内存+pypdf读取；本次未由Leginfo直接读成文法。当前法源优先于部分旧摘要 |
| [DRE When You Have Decided to Rent](https://www.dre.ca.gov/publications/ResourceGuidebook/gb07_when.html) | Security Deposits；Service Members；Inventory Checklist：2024-07-01金额、2025-07-01入住照片，留证及押金不能自当末月租金 | 官方在线指南含2025更新；其筛查费例子明确2023，不采用其金额 |
| [DRE Moving Out](https://www.dre.ca.gov/publications/ResourceGuidebook/gb10_movingout.html) | Refund of Security Deposits至Initial/Final Inspection；清洁/正常损耗；2025-04-01退租前后照片；21天/14天/48小时/最后两周；善意估价 | 正文与脚注均实际读；指南部分用“less than125”而法典为“do not exceed125”，采用法典≤125；指南未完整反映2026电子/多人退押规则，以法典补足 |
| [CA Courts deposit guide](https://selfhelp.courts.ca.gov/guide-security-deposits-california) | 全文：允许扣款、21天、书面请求、small claims自然人12500、恶意最高额外2倍 | web工具403但urllib直连200+BeautifulSoup实读；不是根据搜索摘要 |
| [CA DOJ押金提示PDF](https://oag.ca.gov/system/files/media/Know-Your-Rights-Security-Deposits-English.pdf) | 两页实读：1月/小房东、州地方、军人入口、恶意赔偿 | 2024资料；PDF有“少于125无明细”的易误解概括，不采用；法典h1和h4明确明细与凭据分别处理 |
| [CA DOJ 2024-02-06公告](https://oag.ca.gov/news/press-releases/attorney-general-bonta-issues-consumer-alerts-guidance-protect-california) | Security Deposits段：地方规则可能增加利息等要求 | 原始公告日期2024-02-06；仅采地方边界，不据旧公告证明2026细节 |

Leginfo §1950.5通过web、urllib和指定正常代理均403，停止重试；找到DRE官方2026法典摘录后已读原法，不再构成重要断言缺口。SF页面返回JS挑战，未绕过，未采用其利率；本稿不承诺某市利息比例或全湾区通用规则。第三人若需核对法典，可直接读取上述DRE PDF的相应页。

初稿在 health 审核时已按建议把“21 天收到”改成期限内按适用方式交付/寄出，避免邮寄到达日错配；预检告知同时覆盖任一方结束租赁通知及固定租期届满前合理时间。退款 2026 变化与照片/125 例外在稿中明确。其余两稿补准非工作 SSN 的联邦资助待遇/其余资格条件，以及旧 EAD 自动延长只适用特定合格类别。最终三稿已获独立事实审通过，正文绑定见 `ops/reviews/b01-documents-fact.md`，主控负责后续静态审与集成。

## 复核触发

USCIS续期规则、政策手册或适用专项判令有变化时，重核status；SSA申请/联办政策或IRS W7版本变化时重核numbers；§1950.5修改、州法院small claims金额调整或新增地方利息案例时重核housing。网页页脚和抓取日期不能代替生效日期。证据不是独立审核通过记录。
