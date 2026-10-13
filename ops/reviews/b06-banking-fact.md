# B06 银行与支付独立事实审

本次审阅人：`/root/banking_fact`；原作者：`documents`；恢复修订者：`/root/static_editor`。实际查阅日期：2026-10-13。已完整读正文、地图、作者证据与下方原 civic 断点；作者及旧审阅者的已读记录仅作定位，本次所列来源均由 banking_fact 重新实际读取。

- 正文：`content/book/work/finance/banking-payments.md`。
- 本次最初核对的正文 SHA-256：`3fce0fead028faf8a294ed6cf8ab3de590a2b51af13678e5c0ccb6db77b3fabd`。
- 最终复核正文 SHA-256：`2b42753157ed603aebc8b9a9eb4f5182c930d8410435cb6a8a7822f4219207e5`。
- 方法：实际 UTF-8 文件 `split('---', 2)[2]` 的 SHA-256，不含 frontmatter。
- 当前结论：**PASS，BofA 条件精确化及术语补释后通过独立事实审**。已全文重读最终稿，并核对实际差异；未发现尚待解决的关键事实或行动条件问题。可进入第三人静态审，本结论不代表构建、渲染或正式集成通过。本次没有修改正文、元数据、共享账本或构建产物。

## 本次发现与闭环

1. [Bank of America 当前开户页](https://info.bankofamerica.com/en/international/professional-bank-account)对受美国经济或金融制裁国家公民明确要求合法在美居住证明；原稿“还可能被要求”弱于原页条件。修订者已改成“该页还要求提供证明合法在美居住的文件”，继续限定该银行这一开户渠道；本审阅者在实际最终稿中核对落实。
2. 恢复修订者补 NRA／RA、adverse action notice、APY、routing number、hold notice 和临时贷记的首次中文解释，链接既有联邦税务居民正文与 APY 定义。本审阅者另独立实际读取 IRS 税务居民判定及 Regulation DD §1030.2(c)，并以本轮已读的 CFPB 开户拒绝、Chase 和 §1005.11 原文复核其余释义，未新增未核实的具体资格／收费／期限。

最终稿全文已重新实际读取。复算摘要为上列 `2b427531…19207e5`；逐项逆转已知释义、BofA 条件、税务链接、APY 链接及相邻空格后，实际文件与 Git 中原 `3fce0fea…3fabd` 版本逐字一致；frontmatter 本轮未变。事实审不由作者或恢复修订者自批，第三人静态由 root 承接。

## 本次实际独立回源

以下位置均实际显示并读到。网页更新日期与查阅日期分列；未标更新的来源不以页脚年份猜测版本。只核对正文采用的断言及必要上下文，没有把未展开的整部法律或每家银行产品设为本页门槛。

| 来源 | 实际读取、支持内容与边界 |
|---|---|
| [31 CFR 1020.220，美联储文本](https://www.federalreserve.gov/frrs/regulations/section-1020220-customer-identification-program-requirements-for-banks.htm) | web 定位并实读 `(a)(2)(i)—(iii)`：姓名、个人生日、街址及无固定街址的 APO／FPO 或亲属／联系人街址例外；non-U.S. person 税号、护照号码与签发国等；文件／非文件身份核验与无法核实的处理。支持正文所述法规允许的选项，未把它解释成各银行每种产品必须接受的材料清单 |
| [Bank of America 国际专业人士开户](https://info.bankofamerica.com/en/international/professional-bank-account) | 普通 HTTPS 200，BeautifulSoup 实读全部主文及 FAQ。两份未过期证件；NRA 境外实际地址及美国邮寄地址、RA 美国实际地址；适用时税号；SSN 非统一前提；预约网点。制裁国家公民的合法居住文件为明确要求，现已修正，见闭环第 1 项；未读私人账户或实际预约 |
| [IRS 个人税务居民判定](https://www.irs.gov/individuals/international-taxpayers/determining-an-individuals-tax-residency-status) | 本次修订后 web 实读主文：非公民的美国税务居民／非居民分类、绿卡及实质居留测试、起止日期及例外选择、同年双重阶段。支持 NRA／RA 的税务中文释义与转到既有主解释的行为；没有给具体读者定性或从签证名称猜填 |
| [CFPB 开户被拒](https://www.consumerfinance.gov/ask-cfpb/why-was-i-denied-a-checking-account-en-1113/) | web 全部主文；reviewed 2024-12-18、modified 2025-01-02。ChexSystems／Early Warning、传统信用报告也可能使用；消费者报告不利决定通知、免费报告、书面纠错、低风险账户。稿未承诺换机构必然开户 |
| [Chase 存款协议](https://www.chase.com/content/dam/chase-ux/documents/personal/checking/deposit-account-agreement.pdf) | 普通 HTTPS 200，重新下载后用 pypdf 实读物理页 1、5、10、18、19。共 32 物理页（协议页 1—30，另有隐私资料）；首页及引述页均为 Effective 6/14/2026。页 5 的 available balance 与 ACH／direct deposit、页 10 的 pending 与未显示交易责任、页 18—19 的收到日／截止／非营业日／延迟可用／新户及手机存款另条款均与稿相符。未将该行金额或处理日泛化为全国承诺 |
| [Chase 直接存款表](https://www.chase.com/content/dam/chase-ux/documents/digital/45969_directdeposit.pdf) | 普通 HTTPS 200，pypdf 实读唯一物理页：checking 或 savings／MIA／money market 账号、routing number、姓名地址、授权签名与日期、提交雇主 payroll。版权 2022 不是表件更新日；稿未复制可能变化的网银按钮 |
| [Regulation E §1005.17](https://www.consumerfinance.gov/rules-policy/regulations/1005/17/) | web 实读 `(a)`、`(b)(1)—(3)`、`(f)`及相邻正式解释；页面标 current regulation。ATM／一次性 debit 收费须 affirmative opt-in；可未 opt-in 仍出现负余额而不能收该类透支费；check／ACH／recurring 边界与撤销同意。正文“普通透支服务”保留与信用额度、账户间转款的界限 |
| [Regulation DD §1030.2(c)](https://www.consumerfinance.gov/rules-policy/regulations/1030/2/) | 修订后 web 实际读到 `(c)` APY 定义及相邻条文；页面标 current regulation。APY 按利率及复利频率表示一年账户利息收益，支持表格“计入复利的年收益率”。只核这一通用术语，没有声称 credit union 同受 Regulation DD 或提供计算公式 |
| [FDIC 受保产品与类别](https://www.fdic.gov/resources/deposit-insurance/financial-products-insured) | 普通 HTTPS 200，以主文实际读 Deposit Products、各所有权类别及额度；Last Updated 2024-04-01。单人同银行同类别账户加总，联名须条件、信托另有条件及公式；换账号不扩额。未采用未写入正文的退休／业务／政府详细公式 |
| [FDIC Understanding Deposit Insurance](https://www.fdic.gov/resources/deposit-insurance/understanding-deposit-insurance) | 普通 HTTPS 200，完整主文；Last Updated 2024-04-01。明确 per depositor／FDIC-insured bank／ownership category 的 250,000 美元标准、同类别加总、仅保受保银行倒闭时存款；补强正文的标准框架，未把存款保险当一般诈骗赔付 |
| [FDIC 非受保产品](https://www.fdic.gov/resources/deposit-insurance/financial-products-not-insured) | 普通 HTTPS 200，完整主文；Last Updated 2026-05-12。基金、股票、债券等非存款不因由银行销售而受保；盗用可另涉 EFTA。稿仅采用非存款边界，不复制投资建议或其他保险的概括 |
| [NCUA 保障手册网页](https://mycreditunion.gov/brochure-publications/brochure/how-your-accounts-are-federally-insured) | 普通 HTTPS 200，实读个人单人、IRA／KEOGH、联名、revocable／irrevocable trust 与机构核验部分；另由 web 单独完整读 Coverage Limits 与 estimator 段，确认 per share owner／insured credit union／ownership category 250,000 美元。网页 2024-10-29；未把不同类别公式机械相加 |
| [NCUA Share Insurance](https://mycreditunion.gov/protect-your-money/share-insurance) | 普通 HTTPS 200，完整主文；Last Modified 2025-02-04。NCUSIF 管理、联邦与私人保险、州特许未必 NCUA、存款及非存款边界、查询与估算入口。原页明确所述规则截至 2026-11-30，信托变更 2026-12-01 起生效；正文只提示未来复核，不提前套新公式 |
| [FDIC 第三方 App](https://www.fdic.gov/consumer-resource-center/2024-06/banking-third-party-apps) | 普通 HTTPS 200，完整主文；Last Updated 2024-05-31。非银行本身不受保；资金实际入受保银行且满足所有权及每人金额账簿等条件才可能 pass-through；不保 App 破产、技术故障可能中断访问；核对实际银行。稿没有声称特定 App 已满足这些条件 |
| [People Driven Credit Union ACH／wire](https://www.peopledrivencu.org/faqs/what-is-the-difference-between-an-ach-transfer-and-a-wire-transfer/) | 普通 HTTPS 200，完整 FAQ。ACH 工资／外部账户／自动付款，wire 较急较大金额；该社要求专门 wire instructions，不能只依赖标准 routing number。正文是具名例子，没有通用到款时刻或费用承诺 |
| [Zelle 使用与保障 FAQ](https://www.zelle.com/faq/im-unsure-about-using-zelle-pay-someone-i-dont-know-what-should-i-do) | 普通 HTTPS 200，BeautifulSoup 实读主文及 Using Zelle FAQ。无商品未收到／不符描述购物保障，银行可能另有政策；通常分钟内到已注册账户、不能普通取消或 reverse；未注册 pending 可取消；先查状态／联系自己的银行；符合条件 imposter scam 可能赔付。正文没有把网络取消规则当作否定法定盗用调查权 |
| [CFPB 自动付款](https://www.consumerfinance.gov/ask-cfpb/how-do-automatic-payments-from-a-bank-account-work-en-2021/) | web 全文；reviewed 2026-08-28、modified 2026-08-31。银行 bill pay 发款与商户自动拉款的授权对象不同；保留授权副本、频率和金额，监控余额。稿未称所有 bill pay 必须经 ACH |
| [FTC 假支票](https://consumer.ftc.gov/articles/how-spot-avoid-and-report-fake-check-scams) | web 实读全部主文，June 2025。可用资金不证明真支票，数周后可能发现假票并须偿还银行；多付后让转款为典型骗术。正文建议停止转款／联系银行与原文风险相符 |
| [FTC 冒充银行](https://consumer.ftc.gov/consumer-alerts/2024/06/got-call-about-fraud-activity-your-bank-account-it-could-be-scammer) | web 实读机构文章开头完整段落，不采用评论。验证码、安全账户、以对账单号码回拨、及时报告。该文对受骗转款赔付的宽泛否定未写入稿；实际赔付区分以本次读到的 Reg E 与 Zelle 分支为准 |
| [Regulation E §1005.3](https://www.consumerfinance.gov/rules-policy/regulations/1005/3/) | web 实读 `(a)—(b)`相关 EFT 范围及 `(c)(1)—(3)`排除与正式解释。个人账户、ACH／debit／符合定义 P2P 有覆盖；普通纸质支票与 Fedwire／类似系统排除；支票资料转换为 EFT 或 Fedwire 后另一次 ACH 可不同。正文没有一概说所有 wire 无权利，remittance 另分支 |
| [Regulation E §1005.6](https://www.consumerfinance.gov/rules-policy/regulations/1005/6/) | web 实读完整 `(a)—(b)`与解释；页面标 current regulation。接受的 access device／披露条件、得知丢失或被盗起 2 工作日及 50／500 档、账单发送后 60 日与原可阻止的后续损失、无 access device 不套前两档、特殊情形延期、州法／合同更低责任。正文两个时钟、起算与一般责任概括相符 |
| [Regulation E §1005.11](https://www.consumerfinance.gov/rules-policy/regulations/1005/11/) | web 补齐实读 `(a)—(d)`及相关解释，含原断点未读的 `(d)(1)`。错误与一般问余额不同；首次显示错误的账单发送后 60 日须收到；口头启动、10 工作日书面确认及临时贷记条件；10／45 日，首存后 30 日内交易为 20 工作日／90 日，POS 与所列境外交易 90 日；书面无错误／不同错误说明与索取调查文件。稿未把临时贷记当最终退款 |
| [CFPB EFT FAQ](https://www.consumerfinance.gov/compliance/compliance-resources/deposit-accounts-resources/electronic-fund-transfers/electronic-fund-transfers-faqs/) | web 实读 Coverage Transactions、金融机构相关段、Error Resolution 1—4、Unauthorized EFTs 1—11；主文相关项 2021-06／12、全页 modified 2025-01-16。骗得登录／验证码后由骗子发起可构成 unauthorized；交出凭证不等于实际授权、疏忽不加重法定责任；警方报告／先联系商户不得为调查前提；网络 final／irrevocable 不降低法定保护。本人发款分支须如实说明，稿没有将其自动写成盗用 |
| [Regulation E §1005.10(c)](https://www.consumerfinance.gov/rules-policy/regulations/1005/10/) | web 实读 `(b)—(c)`及正式解释。预授权电子扣款至少 3 工作日前口头／书面止付；可要求 14 日内书面确认，须当时说明并给地址；撤授权后阻止该商户后续付款。稿限定支付类型，并提醒确认覆盖哪些付款 |
| [CFPB 停止自动付款](https://www.consumerfinance.gov/ask-cfpb/how-do-i-stop-automatic-payments-from-my-bank-account-en-2023/) | web 全文；reviewed 2026-08-28、modified 2026-08-31。通知商户和银行、书面记录、止付费、继续核账；撤扣款不消灭债务／不取消服务合同。正文的分别动作及受阻路径相符 |
| [CFPB 投诉入口](https://www.consumerfinance.gov/complaint/) | web 实读完整公开主文；modified 2026-10-05。接收 checking／savings、money transfers，写关键日期金额、附账单及沟通，必要时转其他机关。没有进入投诉账户、递交投诉，稿不承诺 15 日退款 |
| [FDIC BankFind](https://banks.data.fdic.gov/bankfind-suite/bankfind) 与 [NCUA 查询](https://mapping.ncua.gov/) | BankFind 普通 HTTPS 200，实际标题 BankFind Suite，返回 JS 应用壳；未运行机构查询。NCUA mapping 直连及一次正常代理均读超时，详见失败边界；可读的 NCUA Share Insurance 原页确认其官方 Find a Credit Union 入口。没有声称查询了任何实际银行或 credit union 的受保状态 |

本次 Chase 下载已先用 `git check-ignore` 确认 `.cache/evidence/banking_fact/chase-agreement.pdf` 与 `chase-directdeposit.pdf` 被忽略，制品仅在本机缓存。合同文件 SHA-256：`31dbc0116d3e25564e054a29b903c98a6b183d5317f5c0a650e8cbe2eade8793`；直接存款表 SHA-256：`b579284b111d332769e5ae4bd8d4576249d6306f4c7da983c23f02dc3e1be0fa`。摘要用于版本识别，不替代以上实际页读取。

教学虚构账目重新计算：1,200 − 120 = 1,080；1,080 − 700 − 100 = 280。120 已计入可用余额，不能再减一次；没有把这个例子当真实银行会计／计费规则。

## 本次失败与未核实边界

- web 首次美联储页面被巨型公共导航占据，未将那次返回当作 CIP 已读；后续定位实际读到具体条文。web 对 FDIC 受保页及 NCUA Share Insurance 首开返回 Internal Error（未返回可据以认定的 HTTP 状态）；普通 HTTPS 同机构原文 200，实际读到主文。
- NCUA mapping 查询服务：普通 HTTPS 读取超时 30 秒，正常 `http://127.0.0.1:8888` 代理仍读取超时 25 秒。没有关闭 TLS、绕过挑战或继续无价值重试；服务完整操作与真实查询结果未核实。正文提供官方入口，没有把门户可读写成已办理或已核实某机构。
- 本机默认及 Homebrew Python 当次缺 requests／BeautifulSoup／pypdf，首次 requests 抽取未运行；主控创建已忽略隔离检查环境后，本次用 `.cache/checks-venv/bin/python3` 读取所列 HTML／PDF，没有把旧交接环境声明当可用性证据。
- 没有查询具体个人、实际开账户、预约、转款、提交投诉或联系机构；没有核验任何特定 App 真实账簿或 pass-through 资格。商业账户、跨境 remittance、州法支票索赔、具体信托配置及未展开产品继续留地图。本页实际采用的关键断言已完成核验及修订闭环；构建、第三人静态与实际渲染由主控另行验收。

## 原 civic 暂停断点（历史记录，保持未完成结论）

下文为订阅切换前原审阅者的工作断点，不能据此冒用其身份或将其未完成结论改作 PASS。

### B06 银行与支付独立事实审：暂停交接

- 独立事实审者 civic；作者 documents；日期 2026-10-13。
- 正文：`content/book/work/finance/banking-payments.md`。
- 待审当前正文 SHA-256：`3fce0fead028faf8a294ed6cf8ab3de590a2b51af13678e5c0ccb6db77b3fabd`。
- 方法：UTF-8 `split('---', 2)[2]`；暂停保存时已实际复算一致。
- 状态：**未完成，不能登记 PASS**。用户暂停目标后停止新增研究，仅保存已阅读范围与未核项。没有发现已确认的实质错误，也没有把尚未查完写成通过。

## 已做工作与实际独立读取

正文已经全文读完。来源均从正文所列链接独立访问，没有以作者证据代替回源。

1. [CFPB §1005.6](https://www.consumerfinance.gov/rules-policy/regulations/1005/6/)，web 实读现行全文相关条款与解释，抽取 42—115 行。核对 accepted access device／disclosure 条件；得知丢失或被盗后两工作日、50／500 分层；机构须证明原可阻止的后续交易；账单发送后 60 天与后续损失；没有 access device 时前两档不适用；特殊延误及州法／合同更低责任。正文把两个起算点分开，没有把 60 天写成交易日起，也没有保证两日内必定零损失。
2. [CFPB §1005.11](https://www.consumerfinance.gov/rules-policy/regulations/1005/11/)，web 实读定义、通知及调查部分，抽取 43—180 行。已核电话可启动、首次显示错误的账单发送后 60 天内须收到、10 工作日书面确认影响临时贷记、不能等书面确认才调查；10 工作日／45 天、首次存款后 30 天内交易的 20 工作日及 90 天、POS 和法规所列州外发起交易的 90 天；更正与报告结果的具体条款均读到。正文概括的时限及条件目前相符。**(d) 最终书面理由及索取文件段还没有完整读到，恢复后须补，不把仅出现标题当作读完。**
3. [CFPB §1005.3](https://www.consumerfinance.gov/rules-policy/regulations/1005/3/)，web 实读 (c)(1)—(3) 与解释，抽取 136—163 行：纸质支票与 Fedwire／类似银行间或企业间系统排除；由支票资料发起 EFT、由 Fedwire 转来的另一次 ACH 可能另有覆盖。正文使用“普通纸质支票”和系统限定，未一概说所有 wire 都无保护。**(a)—(b) 个人账户及具体 EFT 范围未系统读完，待补。**
4. [CFPB Electronic Fund Transfers FAQs](https://www.consumerfinance.gov/compliance/compliance-resources/deposit-accounts-resources/electronic-fund-transfers/electronic-fund-transfers-faqs/)，web 实读 Error Resolution 1—4、Unauthorized EFTs 1—9，以及支付机构责任相关问答，主要抽取 98—215 行；条目更新为 2021-06／12，仍为当前公开 FAQ。核对骗子通过诈骗取得登录／验证码后自行发起属于未经授权 EFT，交出资料不等于授予该骗子实际权限；警局报告、商户联系和补交资料不得设为启动调查的前提。正文没有把本人按骗术指令主动付款一律改称盗用；但该分支引用的 Zelle 特定赔付政策尚未读，仍待核。
5. [Bank of America 国际专业人士开户](https://info.bankofamerica.com/en/international/professional-bank-account)，普通 HTTPS 200、BeautifulSoup 主文完整读到三步骤和 FAQ。核对两份未过期 ID；NRA 境外实际地址＋美国邮寄地址，RA 美国实际地址；税号 if applicable；SSN 不统一要求；受制裁国家公民额外合法美国居住证明；预约网点。稿件将这些明确限于该行该渠道，目前相符。
6. [NCUA Share Insurance](https://mycreditunion.gov/protect-your-money/share-insurance)，普通 HTTPS 200，主文读到联邦／私人保险区别、NCUSIF 概念、covered／not covered，以及信托规则变更段。实际原文明确 **2026-12-01 生效**，而非已在当前 2026-10-13 生效，稿件未来时态正确。此次工具输出中间有截断，**标准按 owner／institution／ownership category 25 万这一完整表达仍要由正文链接的另一份 NCUA brochure 独立确认**，不能据截断片段概括已审全。

## 已发起但不能算已完成阅读

- 美联储版 [31 CFR 1020.220](https://www.federalreserve.gov/frrs/regulations/section-1020220-customer-identification-program-requirements-for-banks.htm)：HTTPS 200，但首次文本抽取落入极长公共导航，未读到具体 CIP 条款。暂停前第二次针对条款定位的请求已结束，但审阅者尚未显示及读其结果；仍作未核项。
- Chase 当前存款协议与 direct-deposit PDF：暂停前已发起普通 HTTPS／内存 pypdf 抽取，进程在保存时已结束。结果仅工具会话暂存，尚未实际读页，不能声称已经核对生效日、页码或条款。恢复后重新打开对应物理页。
- §1005.10、§1005.17 的 web 返回值已在本轮工具会话，但还没显示正文相关条款；不视为实读。这些工具暂存可能不会随订阅切换保留，应重新回源。

## 恢复后继续核对清单

1. CIP 的姓名／出生日期／地址／识别号；non-U.S. person 护照等替代、无固定街址的规则条件；区分法规允许与银行实际产品接受。
2. CFPB 开户拒绝：消费者报告、adverse action、免费报告、纠错及低风险账户；已有信用页链接不能替代独立核验。
3. §1005.17 的 ATM／一次性借记卡 opt-in 与支票、ACH、经常性扣款边界；§1005.10(c) 的三工作日止付及口头后十四天书面确认条件。
4. FDIC 标准限额、所有权合并、BankFind；NCUA brochure 及查询入口；投资产品不受保；第三方 App pass-through 必要记录条件、App 倒闭与取款访问风险。
5. Chase 2026-06-14 生效协议：稿称第 5、10 页 available／pending，第 18—19 页存款与 hold／new account／mobile deposit，需实际页码与内容核对；direct deposit 表中的 routing／account／type。
6. People Driven CU 的 ACH／wire 指令差别；Zelle 注册收款人取消、未注册 pending、无购物保障及符合条件 imposter scam 赔付；不把政策赔付当作普遍法律退款权。
7. FTC 假支票与冒充银行、CFPB 自动付款与停止付款、CFPB 投诉入口；原作者表格虚构算例 1,200−120−700−100=280 初步算术相符，但账户现实规则不得外推。
8. 补读 §1005.11(d) 书面理由和提供调查文件；§1005.3(a)—(b) 完整覆盖。完成全部回源后再决定是否需作者返修；修订由 documents 操作，审阅者复核后重绑最终 SHA。

## 交接边界

没有联系银行或机构、登录账户、查询个人资料、发起付款或真实投诉。没有改正文、frontmatter、作者证据或共享文件，没有构建或提交。当前只能说明以上已读范围内暂未发现阻断，不能据此安装正式审阅元数据。
