# B06 失业支持：当前独立事实审

- 结论：**PASS**。2026-10-13，root 独立实际回源并复核最终作者修订；可交 static_editor 第三人静态审。
- 正文：`content/book/work/employment/job-loss-support.md`。
- 当前正文 SHA-256：`160a39b1cdd003a0528be0396f50330ddda787cc1e43b11491f630372bf3f7d7`，实际 UTF-8 `split('---',2)[2]`，不含 frontmatter。
- 原作者 civic；本轮修订者 birth_fact；事实审 root；第三人静态审 static_editor。root 未改本文正文。下方暂停记录原样保留为未完成历史，不能用于最终元数据。
- 本结论只覆盖下列实际读到的来源与正文断言；尚不代表静态审、构建、渲染或正式集成。

## 恢复后的独立阅读与逐项判断

root 完整重读最终正文、实际差异、地图与作者证据；证据仅用于定位。来源通过 web 或普通 TLS 请求实际读取，HTML 抽取正文，PDF 读取原件文字。批量缓存存于已验证忽略的 `.cache/evidence/job-loss-resume/`；下载成功不等于已读，以下仅列已实际显示并阅读的采用段落。实际查阅日期均为 2026-10-13，网页或 PDF 版本另列。

| 实际来源与阅读位置 | 对应断言与边界 |
|---|---|
| [WA 申请所需资料](https://esd.wa.gov/get-financial-help/unemployment-benefits/applying-unemployment-benefits/how-apply-unemployment-benefits/information-you-need-when-you-apply)，主文 Basic information、过去 18 个月工作经历及入口 | 包括所有兼职、临时雇主及联系方式、日期与身份资料。18 个月仅用于准备经历；同页把基期概述为 18 个月的句子未采用，基期另读专门计算页。 |
| [CA DIR Paydays](https://www.dir.ca.gov/dlse/FAQ_Paydays.htm)，最后工资相关完整问答及行业例外 | 解雇当时支付；无固定期限书面合同的辞职者 72 小时、提前通知的差别；电影、季节等例外。表格准确限定普通工资，不把所有补偿合并成同一到期日。 |
| [NY Wages FAQ](https://dol.ny.gov/wages-and-hours-frequently-asked-questions)，离职者最后工资问答 | 对应工作期正常发薪日，员工要求时邮寄。未采用页面其他行业的旧年度数字。 |
| [WA L&I Getting Paid](https://www.lni.wa.gov/workers-rights/wages/getting-paid/)，主文及 final paycheck | 辞职／解雇均最迟下一个正常发薪日；不能以未归还钥匙设备扣住；离职福利与已赚工资分别判断。 |
| [TWC Final Pay](https://efte.twc.texas.gov/final_pay.html)，主文 | 非自愿离职六个日历日、自愿下个正常发薪日，佣金奖金协议安排的例外。没有将 severance 自动写成法定必付工资。 |
| [DOL UI](https://www.dol.gov/general/topic/unemployment-insurance)，How Do I Apply 与项目说明 | web 失败后普通 TLS 200 实读：尽早联系工作州，多州／外州居住须说明情况。未采用 COVID 例外或预计到账天数。 |
| [EDD Eligibility](https://edd.ca.gov/en/unemployment/Eligibility)，主文；[Eligibility FAQ](https://edd.ca.gov/en/unemployment/FAQ_-_Eligibility/)，完整采用问答 | 错分 contractor 可申请由 EDD 判断；离职原因、工作能力、可接受工作及每周条件另核。辞职 good cause 不是自动通过；疾病／照护可另查 DI、PFL。非公民身份和授权须同时覆盖赚工资时与每个申领周。 |
| [EDD DE 8714AB](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de8714ab.pdf)，两物理页文字，Rev. 5 (9-18)，尤其第 1 页 | 最高季 1,300，或 900 且总额 1.25 倍；普通最近五个完整季度前四，标准不够才自动考虑最近四季。现行 Eligibility 页面仍链接该原件；第 2 页旧电话时间未采用。未声称看过原件图像。 |
| [EDD Step 2](https://edd.ca.gov/en/unemployment/step-2-apply/)，当前主文 | myEDD／UI Online、电话／传真／邮寄、普通话 1-866-303-0706、AJCC 纸件协助。未登录、测试账户内每屏或保证电话接通。 |
| [NY P832](https://dol.ny.gov/how-your-weekly-unemployment-insurance-benefit-payment-calculated-p832)，2/26，两物理页文字；[Before You File FAQ](https://dol.ny.gov/you-file-claim-unemployment-faqs)，本轮主文完整阅读 | 2026 至少两季工资、最高季至少 3,500，总额 1.5 倍；高季 19,118 或以上时其余三季至少 9,559。普通／替代基期及已合格时请求重算、初始 Monetary Determination 日期起 10 日、已用工资不复用、首次失业周、跨州及非公民条件均逐项一致。未采用每周最高额或把当前季度纳入普通基期。 |
| [NY Benefit Process](https://dol.ny.gov/unemployment-claimant-benefit-process-0)，新申请与语言、调查通知段 | 1-888-209-8124、普通话和粤语选项；回复通知和问卷。一般流程页的听证摘要不替代下列专门听证问答。 |
| [WA Basic Eligibility](https://esd.wa.gov/get-financial-help/unemployment-benefits/basic-eligibility-requirements)，主文；[Estimate Your Benefit](https://esd.wa.gov/get-financial-help/unemployment-benefits/estimate-your-benefit)，Your base year／Alternate base year | 普通基期至少 680 小时，通常最近 18 个月有 WA 部分工资，军人／联邦雇员另分支。基期前四／最近五；不足时可看最近四，替代仍须 680。部分工作不是统一“少于 40 小时即合格”。未运行计算器估个案金额。 |
| [TWC Eligibility Issues](https://efte.twc.texas.gov/ui_law_eligibility_issues.html)，Monetary Eligibility、Continuing Eligibility、Partial Unemployment | 至少两季工资、总额至少 37 × WBA，前次申请后另有重新工作收入条件；漏报／SSN 误配／错分类可致缺工资。当前工作授权、能且可工作和持续求职另核。不采用旧 INS 称谓、每周最高额或完整计算公式。 |
| [Texas Labor Code §201.011(1)](https://tcss.legis.texas.gov/docs/LA/htm/LA.201.htm)，实际第 (1) 项全文 | 普通基期五季前四；医学可验证疾病伤害影响相关季度大部分时间有特定基期与 24 个月 initial claim 条件。正文仅提醒带记录核对，不错误套用其他州最近四季或追加未核 seven weeks。 |
| [UBS](https://apps.twc.texas.gov/UBS/security/logon.do)，公开登录页主文 | 旧用户用原账号／恢复，不反复新建。只验证公开入口，不称实际申请已提交。 |
| [TWC 官方公告](https://content.govdelivery.com/accounts/TXWC/bulletins/3cf852d)，2025-01-29 08:52 AM CST，英语主文；[TWC 联系页](https://cs.twc.texas.gov/TWC-CC-Contact-Us/)，Unemployment Claims Services；[West Central Texas Workforce](https://www.wfswct.org/394/Filing-for-Benefits)，申请首段 | 准确文件名 Statement of Wages and Potential Benefit Amounts 只为工资金额决定；按所寄说明的日期／申报日开始请求支付，不等资格决定，每两周继续，UBS／800-558-8321。正式联系页列申请电话 800-939-6631，由地方 workforce 首段互核用途。未采用公告处理天数、疫情延长福利、地方页求职次数或 waiting week 概括。 |
| [NY Labor Law §590(9)](https://www.nysenate.gov/legislation/laws/LAB/590)，web 283—303 行对应第 9 项 | 普通直连／代理 403 后 web 实读实际条文：过去劳动工资受永久居民、为提供劳动而合法在美、PRUCOL 等法定条件限制，结合当前申请 FAQ；没有把单张 EAD／SSN 写成充分条件。 |
| [WA Citizenship](https://esd.wa.gov/get-financial-help/unemployment-benefits/applying-unemployment-benefits/how-apply-unemployment-benefits/citizenship-and-legal-rights)，主文；[RCW 50.20.098](https://app.leg.wa.gov/RCW/default.aspx?cite=50.20.098)，全文 (1)—(3) | 过去 24 个月合法工作情况、最近移民文件、SAVE 核验；过去劳动作为给付依据另受法定类别约束。没有把文件举例当完整资格清单。 |
| [TWC Coverage Issues](https://efte.twc.texas.gov/ui_law_coverage_issues.html)，Non-Citizens／§207.043 实际引文，及上方当前资格段 | 工资需报告不等于能计入 UI 给付；既核过去劳动类别，又核当期工作授权。只采用这一部分，不宣称已审整套雇主教材。 |
| [USCIS Legal Services](https://www.uscis.gov/scams-fraud-and-misconduct/avoid-scams/legal-services)，2026-08-04，公开主文 | 合格律师、认可组织的认可代表及服务入口。只转介，不提供离职宽限期、签证延期或身份个案结论。 |
| [EDD Step 5](https://edd.ca.gov/en/unemployment/step-5-certify-for-benefits/)，主文；[NY Weekly](https://dol.ny.gov/unemployment/certify-weekly-unemployment-insurance-benefits)，主文；[WA Weekly](https://esd.wa.gov/get-financial-help/unemployment-benefits/weekly-unemployment-claims/how-file-your-weekly-claims)，主文 | CA 两周并报未发工资，需报工作工资不能用 Tele-Cert；NY 周一至周日、该周周日至下周六申报；WA 周日至周六结束后、资格／补工资／申诉未决仍继续。WA 800-318-6022、vacation cash-out 与对应日期假期工资差异已实读。TX 两周另用 TWC 公告，未互套各州周界。 |
| [WA Decision Letter](https://esd.wa.gov/get-financial-help/unemployment-benefits/applying-unemployment-benefits/understand-your-benefits-decision-letter)，工资、工时与更正段；[EDD Step 4](https://edd.ca.gov/en/unemployment/step-4-review-benefit-documents/)，主文 | 0 元可因漏工时，逐季核对，工资单／W-2／雇主日期用于补正；身份与工资通知按其要求回应。未统一硬编码“十天纠错”。 |
| [EDD Appeals](https://edd.ca.gov/en/unemployment/appeals/)，主文；[NY Hearing FAQ](https://dol.ny.gov/hearing-process-frequently-asked-questions)，初次 hearing 43—76 行；[WA Appeal](https://esd.wa.gov/get-financial-help/unemployment-benefits/appeal-unemployment-benefits-decision)，主文 | CA 寄发起 30 日书面、DE 1000M／信件、逾期解释 good cause；NY 寄发或亲自送达后 30 日、邮戳／提交证据，在线／邮寄／传真；WA 发出决定起 30 日，非全在线，不可只电话／邮件。三州继续申报所要领取各周；后续听证、上诉的新期限未互套。 |
| [Texas Labor Code §212.053](https://tcss.legis.texas.gov/docs/LA/htm/LA.212.htm)，全文该项；[TWC Claim and Appeal Process](https://efte.twc.texas.gov/ui_law_the_claim_and_appeal_process.html)，Initial Claim／Initial Determination／Appeal Tribunal | 初次决定副本寄往记录最新地址后第 14 个日历日最迟提起，书面方式按决定；不是从看到邮件之日，也不是雇主答复期限。 |
| [USAGov Emergency Food](https://www.usa.gov/emergency-food-assistance)，主文，更新 2025-12-23；[Emergency Housing](https://www.usa.gov/emergency-housing-assistance)，主文与资源入口 | pantry／food bank／211，短期住房和州租金帮助分别查询。正文没有库存、项目资金、资格或自动停止驱逐的保证。 |
| [USAGov SNAP](https://www.usa.gov/food-stamps)，主文；[TANF](https://www.usa.gov/welfare-benefits)，主文，更新 2026-01-13 | 各自联系州／地方或 Tribal 项目，另判家庭、收入、居住等。本文只分流，没有统一移民资格、金额或工作要求，没有从 UI 不合格推导全家所有援助不合格。 |

已有站内的医保衔接、工资、身份文件、租房四页均实际核对目标存在、integrated／draft false，并与本稿采用段落对读；B01—B05 当前正文哈希已与正式账本重新核验一致。本稿仅调用其行动路径，没有抄入新的税率、保障窗口或工资底线。最终四条内链、25 组加粗边界的实际扫描均通过。

## 本轮失败、修订及未核边界

- 旧 Coastal Bend `Rapid-Response-Packet.pdf` 本轮 web 超时、普通直连 503、一次正常 8888 代理仍 503，未重新读到原件。原 civic 历史已读保留，但不冒称 root 本轮读到。TWC 主站两个当前 PDF 亦 web 403；没有借搜索摘要放行。已实际读取上表 TWC 署名公告与公开正式联系页，足以支持所用申请电话、文件名与两周支付断言。
- birth_fact 独立实际读替代页后修订 TX 两段：精确通知名、中文释义、求职按机构通知、两个旧包引用换为明确日期的 TWC 公告，并新增联系页。root 实际 `git diff` 对照，未改其他数字、资格、期限、工作授权或元数据；上述修改有本人实际读到的原文支持。新 SHA 已重新计算一致。
- 普通读取保留 TLS 校验，没有登录、提交、测试实际账户、拨号、联系雇主或机构。未核实际接通／支付处理时间、当天 pantry 库存与援助余额。
- 特殊工种、跨州合并工资全部计算、第二福利年度、等候周完整比较、个案给付金额、追回／多级上诉、移民身份或宽限期、SNAP／TANF 细则仍留地图。现金救急的行动整理不等于任何项目批准。
- 最终正文已完整对照，采用范围内无未解决的实质事实错误，结论 **PASS**。正文若变化，必须检查变化后再重绑；不能复制本结论到新版本。下一关为 static_editor 第三人静态审。

# B06 失业支持：事实审暂停断点（历史）

2026-10-13，审阅者root，作者civic。用户暂停目标并要求跨会话保存现场；这是未完成的独立事实审记录，**不是PASS**，不能据此安装正式元数据。

- 正文：`content/book/work/employment/job-loss-support.md`。
- 正文SHA-256：`e33e6d6c6fb35c66b551da0406a29ab6a86c88c31506ec681ed3744bdbf46ace`，算法为UTF-8 `split('---',2)[2]`。
- 已完整读正文；已读作者证据用于定位，作者证据不代替本次独立回源。

## 暂停前独立实际读到

1. [EDD DE8714AB](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de8714ab.pdf)，web实际抽取两物理页，Rev.5 (9-18)。第1页支持最高季1300，或900且基期总额1.25倍；标准五季前四，标准不够时自动考虑最近四季，不能为金额更高任意选替代。第2页旧营业时间未用于正文；当前Step2入口尚须独立读取。未实际看PDF图像，本轮只读文字。
2. [NY P832](https://dol.ny.gov/how-your-weekly-unemployment-insurance-benefit-payment-calculated-p832)，web实际读两页，2/26。确认2026两季工资、单季3500、总额1.5倍、高季19118及其他季9559边界；普通/替代基期、当前季排除、用过工资不重复使用。正文未写每周最高额。未实际看PDF图像。
3. [NY Before You File FAQ](https://dol.ny.gov/you-file-claim-unemployment-faqs)，web本轮实际输出读到第148行附近：2026工资门槛、标准/替代、初始通知10天重算、首次失业周、跨州工资、部分失业入口。后段非公民条款等尚未独立读完，不能声称全文已核。
4. [DOL UI](https://www.dol.gov/general/topic/unemployment-insurance) 本轮web返回Internal Error，**没有读到主文**。尚未执行普通HTTPS后备读取。作者已读的结果不能算本审阅者实读。

上述已读段暂未发现需返修项，但四州全篇审阅远未完成。无需因暂停前未发现错误而提前通过。

## 恢复后优先补核

- 四州最后工资、工作州申请及误分类。
- CA现行Eligibility/FAQ/Step2、NY现行流程电话与FAQ后段、WA680小时和专门基期页、TX efte资格及法典201.011。
- 四州过去工资身份与当前工作授权的分离，NY590(9)、WA50.20.098、TX207.043等实际条文。
- 每周/两周申报、减时、假期和离职相关款项、缺工资更正、首次申诉期限与起算点；尤其TX14日及CA/NY/WA30日不能互套。
- TX主站受阻时作者使用的署名TWC资料包物理第2页：独立打开原件核验支付流程、两个电话及时间边界；不把其他旧社区清单当当前材料。
- 食物/住房/SNAP/TANF分流与受阻路径，现有内链内容；不扩展未经研究的资格承诺。

作者证据列有37组入口及已知源站冲突，可按实际断言逐项核验。尚未生成批量下载缓存，没有在后台运行下载；只验证过`.cache/evidence/job-loss-review/index.json`会被Git忽略，文件尚未创建。未登录、提交、联系机构、改作者正文、构建或发布。

完成独立事实审后，还需由不同于作者和本事实审者的第三名参与者做静态审，原计划documents。新会话需重新分派代理，不继承旧句柄；历史作者与审阅身份仍按本记录保留。
