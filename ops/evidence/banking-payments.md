# 银行与支付证据

原作者 documents；本轮恢复修订者 static_editor；实际查阅日期 2026-10-13。对应 `content/book/work/finance/banking-payments.md`，个人日常账户与境内支付。下列原始材料阅读由原作者完成，本轮新增阅读与修订另记在末尾；均实际打开正文或 PDF，搜索仅用于发现入口。新稿保持 written / draft true，等待独立事实审。

## 开户与账户使用

1. [31 CFR 1020.220，美联储法规文本](https://www.federalreserve.gov/frrs/regulations/section-1020220-customer-identification-program-requirements-for-banks.htm)：web 可开但导航很长，普通 HTTPS requests + BeautifulSoup 成功实际读 `(a)(1)—(2)`，并查阅其后相关段落。姓名、生日、地址、号码；non-U.S. person 可用护照号码及签发国等；无住宅/营业街址的联系地址例外；证件及非证件验证、无法确认身份时的程序。未把 CIP 号码选择等同于各银行所有产品必须接受，更未把号码条件写成移民身份许可。
2. [Bank of America 国际专业人士](https://info.bankofamerica.com/en/international/professional-bank-account)：web 完整主文实际读到；未标单独更新日期。两份未过期证件；SSN 非统一必需；NRA 境外实际地址及美国 mailing address，RA 美国实际地址，tax ID if applicable；护照等主要与辅助证件；受美国经济/金融制裁国家公民额外合法美国居住证明；预约 financial center。正文限具名渠道，不承诺获批。
3. [CFPB 开户被拒](https://www.consumerfinance.gov/ask-cfpb/why-was-i-denied-a-checking-account-en-1113/)：web 全文，last reviewed 2024-12-18、modified 2025-01-02。ChexSystems/Early Warning、负余额关户等；基于消费者报告的不利决定通知、免费报告、纠错与低风险账户。本文没有复述所有 FCRA 年限或传统信用页面。
4. [Chase 存款协议](https://www.chase.com/content/dam/chase-ux/documents/personal/checking/deposit-account-agreement.pdf)：普通 HTTPS 200，内存 pypdf 实读 PDF；现件首页 **Effective 6/14/2026**，32 PDF 页（协议 30 页加隐私资料）。实际读协议页 1、5、10、18—19，并查看 12—14、16 中与卡、付款及余额相邻的片段。重点：合同另包括费用文件；available / present / pending 解释、direct deposit 为 ACH；未显示为 pending 的交易仍须负责；截止日、营业日、存款延迟、新客户首 30 天、手机存款另有条款。正文只作有限实例，没有将具体 hold 金额和期间泛化成联邦统一承诺。
5. [Regulation E §1005.17](https://www.consumerfinance.gov/rules-policy/regulations/1005/17/)：web 实读 `(b)(1)—(3)`、`(f)` 和相邻正式解释。普通 overdraft 服务为 ATM/一次性 debit 收费的 affirmative opt-in；checks/ACH/recurring 边界、可撤回选择。搜索中的 2024-05 circular 未作为现行法源，正文引用法规本身；未采用已撤销或新提议的通用透支费上限。

6. [Chase 直接存款请求表](https://www.chase.com/content/dam/chase-ux/documents/digital/45969_directdeposit.pdf)：普通 HTTPS 200，pypdf 实读单页，版权 2022，不把版权当更新日期。Checking/Savings account number、routing number、姓名地址、授权签名日期及给雇主 payroll 的用途。正文只教读者按实际银行表件使用号码，未照抄旧界面按钮。

## 存款保障

7. [FDIC 受保金融产品与所有权类别](https://www.fdic.gov/resources/deposit-insurance/financial-products-insured)：web 403，普通 HTTPS 200 + BeautifulSoup 实际完整主文，页示 2024-04-01。存款自动受保、single accounts 同人同银行加总 250,000 美元；joint/trust 等另有资格及计算。正文仅写标准框架，不教读者仅靠添受益人机械扩额。
8. [FDIC 非受保产品](https://www.fdic.gov/resources/deposit-insurance/financial-products-not-insured)：普通 HTTPS 实读主文；基金等非存款产品即使在受保银行销售仍不受 FDIC 保障。正文相应句子不把投资、欺诈、操作故障写成银行倒闭赔付。
9. [NCUA 保障手册网页](https://mycreditunion.gov/brochure-publications/brochure/how-your-accounts-are-federally-insured)：普通 HTTPS 200，实际读 Coverage Limits 与相邻机构核验和 estimator 段。标准 250,000 美元 per share owner / per insured credit union / ownership category。
10. [NCUA Share Insurance](https://mycreditunion.gov/protect-your-money/share-insurance)：web 实读完整主文，last modified 2025-02-04。联邦与私人保险、州特许未必 NCUA；存款与非存款、查机构/估算入口；现说明截至 2026-11-30，已公布信托规则 2026-12-01 起调整。正文给未来变化提示，不提前应用新公式。
11. [FDIC Banking With Third-Party Apps](https://www.fdic.gov/consumer-resource-center/2024-06/banking-third-party-apps)：web 403，普通 HTTPS 200 后完整主文，last updated 2024-05-31。非银行本身不受保；钱实际进入银行且符合所有权/账簿等条件才可能 pass-through；不保非银行自身破产；访问中断联系客服；通过 BankFind 核对实际银行。正文不承诺某 App 满足该条件。

## 付款、余额与骗局

12. [People Driven Credit Union ACH 与 wire FAQ](https://www.peopledrivencu.org/faqs/what-is-the-difference-between-an-ach-transfer-and-a-wire-transfer/)：web 可开，普通 HTTPS + BeautifulSoup 实读正文。ACH 用于工资/外部账户/自动付费，wire 用于较大较急资金；该社特别要求专门 wire instructions。本文把它写成具名例子，未采用其他银行的速度、费用或收款号码。
13. [Zelle 使用与保障 FAQ](https://www.zelle.com/faq/im-unsure-about-using-zelle-pay-someone-i-dont-know-what-should-i-do)：原 zellepay.com URL 由 web 正常重定向至 zelle.com；实际完整读 Using Zelle、purchase protection、pending/completed、取消、imposter scam 相关段。当前页含 Q1 2026 调查脚注，正文不使用调查数字。没有一般购物保护；已注册收款人付款不能取消；未注册 pending 可取消；qualifying imposter scams 可能赔付。未把“不能取消”写成否定未经授权 EFT 的法定调查权。
14. [CFPB 自动付款怎样运作](https://www.consumerfinance.gov/ask-cfpb/how-do-automatic-payments-from-a-bank-account-work-en-2021/)：web 实读全文，reviewed 2026-08-28，modified 2026-08-31。商户拉款与银行 bill pay 发款、授权副本、金额日期及余额不足费用。正文保留这个行动区别，没有称所有 bill pay 都必走 ACH。
15. [FTC 假支票](https://consumer.ftc.gov/articles/how-spot-avoid-and-report-fake-check-scams)：web 先部分返回，随后定位第 27 行实际返回并读完主文，标示 2025-06；普通代理 requests 403 如实记录。支票可用不等于真实有效、识别可能需数周、多付后要求转差额、银行收回资金与举报。无引用搜索摘要代替正文。
16. [FTC 冒充银行诈骗](https://consumer.ftc.gov/consumer-alerts/2024/06/got-call-about-fraud-activity-your-bank-account-it-could-be-scammer)：web 实读开头完整文章段（不使用用户评论）；2024-06 URL。只用其转安全账户/索验证码、用对账单号码回拨和立即报告的提示。文章“受骗转出不会受保护”过度简括的句子未复制为一般赔付结论；实际处理区分发起人，并以现行法规和 Zelle 特定政策核对。

## 错误与盗用、停止扣款

17. [Regulation E §1005.3](https://www.consumerfinance.gov/rules-policy/regulations/1005/3/)：web 实读 `(c)(1)—(3)` 及 Fedwire/ACH 正式解释。普通支票与电子支票转换区别、Fedwire 或类似系统例外。正文提示纸质支票、wire、跨境 remittance 不能套整套国内个人 EFT 流程，没有展开未审完整个案权利。
18. [§1005.6](https://www.consumerfinance.gov/rules-policy/regulations/1005/6/)：web 实读全 `(a)—(b)` 及相关正式解释。2 个工作日从知悉 access device 丢失/被盗起，50 或实际损失较低；晚报 500 档及银行证明要求；账单寄出后 60 天的后续交易责任；非 access device 不套 50/500；特殊情况合理延长；州法或合同较低责任。正文以“一般、适用条件下”概括，不承诺最低必须负担 50 美元。
19. [§1005.11](https://www.consumerfinance.gov/rules-policy/regulations/1005/11/)：web 实读 `(a)—(d)` 与关键解释。首次显示错误的账单送出后 60 天内机构收到；口头可报告；请求书面确认的 10 工作日与临时贷记边界；一般 10 工作日/45 天；首次存款后 30 天内交易的 20 工作日、新账户/POS/境外的 90 天；无错误决定书面说明与取据权。没有把 temporary credit 写成最终退款。
20. [CFPB EFT FAQ](https://www.consumerfinance.gov/compliance/compliance-resources/deposit-accounts-resources/electronic-fund-transfers/electronic-fund-transfers-faqs/)：web 实读个人账户定义、P2P 覆盖、Error Resolution Q4、Unauthorized EFT Q4—7 及相关段；项目更新 2021-06-04/2021-12-13，当前公开页未标 withdrawn。骗得凭证后由骗子发起仍可能 unauthorized；不能以提供警方报告作为启动调查前提；私人网络 final/irrevocable 不消灭 EFTA 条件。普通 requests/正常代理被 403，不记作其正文来源。
21. [§1005.10(c)](https://www.consumerfinance.gov/rules-policy/regulations/1005/10/)：web 实读 stop-payment 正文及正式解释。预授权 EFT 至少 3 个工作日前通知；口头后可要求 14 天书面确认，需当时提供要求和地址；未按要求确认的效力。本文明确限定这一支付类型。
22. [CFPB 停止自动付款](https://www.consumerfinance.gov/ask-cfpb/how-do-i-stop-automatic-payments-from-my-bank-account-en-2023/)：web 实读全文，reviewed 2026-08-28，modified 2026-08-31。通知商户与银行、保留书面记录、stop order 可能收费、撤销扣款不取消合同或债务。
23. [CFPB 投诉入口](https://www.consumerfinance.gov/complaint/)：web 实读主文，modified 2026-10-05。接收 checking/savings 和 money transfers、材料及转适合主管机关。正文没有把预计企业响应天数当作法定退款期限，也没有代读者发投诉。

## 冲突、失败与未展开边界

- Chase 搜索结果仍显示 2026-03-15 版摘要；实际下载原 PDF 为 **2026-06-14**，正文只采用实件日期。
- FDIC web 403 后公开 HTTPS 原站正常可读；CFPB 多处普通 HTTPS/正常代理 403，以成功 web 原文为准；FTC 假支票后续定位成功。未关闭 TLS、绕过挑战或登录私人账户。
- CFPB 较旧开户 checklist PDF 普通 HTTPS 返回 HTML，pypdf 无法读取；未将其材料清单、25—100 美元初始存款等写进稿件。CIP 原法与具名银行当前流程足以支持开户步骤。
- NCUA 2026-12-01 信托调整只提示复核，不写信托公式；商业、跨境、具体非银行产品与州法支票索赔留地图。
- 虚构余额例子独立计算：1,200 − 120 = 1,080；1,080 − 700 − 100 = 280；120 已扣一次，不再扣第二次。未使用真实银行个人信息。

## 2026-10-13 恢复修订与新增实读

原作者 documents；本轮修订者 `/root/static_editor`，由主控分派。修订前正文 SHA-256 为 `3fce0fead028faf8a294ed6cf8ab3de590a2b51af13678e5c0ccb6db77b3fabd`，修订后为 `2b42753157ed603aebc8b9a9eb4f5182c930d8410435cb6a8a7822f4219207e5`；均按 UTF-8 `split('---', 2)[2]` 计算，不含 frontmatter。

本轮在首次出现处补充 NRA／RA、adverse action notice、APY、routing number、hold notice 和临时贷记的中文释义，保留原文名称以便读者识别材料；税务身份链接既有 `/book/work/tax/tax-residency/`，未从签证名称判断税务身份。APY 新增定义原文链接。按独立事实审 banking_fact 指出的原页 required 条件，将制裁国家公民的合法在美居住证明改为该页明确要求；其余规则、资格、金额、日期和链接未改，frontmatter 保持 written / draft true、审阅字段空。

本轮修订者实际新读到的公开来源如下，不将这些作者阅读作为 banking_fact 的独立事实审：

- [Bank of America 国际专业人士开户页](https://info.bankofamerica.com/en/international/professional-bank-account)：web 实读主要开户步骤及相关 FAQ，尤其 Collect required documents and information 中 NRA／RA 的全称、两种地址要求、适用时税号及制裁国家公民的居住证明。原页对后者写 required，并要求可接受文件证明 lawful U.S. residence，支持本次措辞精确化；没有扩大到其他银行或所有非公民。
- [IRS 个人税务居民判定](https://www.irs.gov/individuals/international-taxpayers/determining-an-individuals-tax-residency-status)：web 实读正文的非公民居民／非居民、绿卡与实质居留测试、起止与例外提示及同年双重阶段；另完整读取既有 `content/book/work/tax/tax-residency.md`，确认它已 integrated / draft false，可作为主解释。本稿只补两种税务分类的名称及链接，没有复制税年算法或给具体读者定性。
- [CFPB 开户被拒](https://www.consumerfinance.gov/ask-cfpb/why-was-i-denied-a-checking-account-en-1113/)：web 完整实读主文；adverse action 通知段说明因报告拒绝后的机构联系方式与索取报告。仅增加“不利决定通知”的中文对应，不改原通知与纠错链。
- [Regulation DD §1030.2(c)](https://www.consumerfinance.gov/rules-policy/regulations/1030/2/)：web 实读 annual percentage yield 定义，按利率及复利频率表示一年利息收益；正文表内据此写“计入复利的年收益率”，没有写具体计算公式、利率或所有机构受相同法条约束的结论。
- [Chase 2026-06-14 存款协议](https://www.chase.com/content/dam/chase-ux/documents/personal/checking/deposit-account-agreement.pdf)：web 读取首页生效日期及协议物理／印刷第 18—19 页 Funds Availability Policy，尤其第 19 页 D 的 Notice 段，存款完成后决定延迟可用会寄 deposit hold notice。仅给既有 hold notice 增加“资金暂缓可用通知”释义，没有把该行各金额或延迟天数推广其他银行；未逐页阅读整份 32 页 PDF。
- [Regulation E §1005.11(c)(2)(i)—(ii)、(d)](https://www.consumerfinance.gov/rules-policy/regulations/1005/11/)：web 实读临时记款、调查期间可使用以及最终决定／扣回的有关条款。正文首次把临时贷记解释为“调查期间暂时记入账户供你使用的款项”，后文继续保留它不是最终结案的边界，未承诺每宗申诉必有此记款。

routing number 仅补“银行路由号码”的中文对应，没有新增位数、个人号码或所有付款渠道通用的主张。本轮没有重新全页回源，原有来源的采用／未展开边界保留；当前版本及实际差异交 banking_fact 对照复核，随后由 root 第三人静态审。修订者不兼任此稿第三人，不安装正式元数据、不构建、不提交，没有登录账户、发起付款或联系机构。

## B06 主控集成记录

documents原作者／static_editor修订；banking_fact独立事实审、root第三人静态审均PASS。当前正文2b427531；B06正式integrated／draft false，2026-10-13，见b06-integration.md。 本段仅登记实际完成的审阅与集成，不新增来源实读或个案核实声明；实际读到的范围与失败边界见对应事实审记录。
