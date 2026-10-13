# B06 银行与支付独立事实审：暂停交接

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
