# B05 地址更新独立事实审

- 审阅者：documents；作者：root；查阅日期：2026-10-13。
- 路径：`content/book/life/documents/address-changes.md`。
- 正文 SHA-256：`0c4c7defe92930d2b243ef2e2de2f67112fde06bad99a8631e30755c74b05e11`。
- 摘要算法：UTF-8 文本 `split('---', 2)[2]`，不含 frontmatter。
- 结论：**PASS**。全文逐段对照，未发现需作者返修的实质事实问题。本记录不代表静态审、构建或发布。

## 独立实际阅读的资料

以下均实际打开正文或 PDF；没有把作者证据、搜索摘要或页面状态码当作已阅读。

1. [USCIS 改址主入口](https://www.uscis.gov/addresschange)，普通 HTTPS requests + BeautifulSoup 完整主文，页面更新 2026-08-04：10 天、A/G 与免签访客例外、在线账户、逐案 receipt number、纸件的限制、USPS 不同步且不转寄 USCIS 邮件、受保护人群分流。
2. [USCIS Policy Manual 1-A-10](https://www.uscis.gov/policy-manual/volume-1-part-a-chapter-10)，同方法完整 Guidance，页示 current as of 2026-10-02：没有待办申请也可报告；E-COA 更新实际与邮寄地址；纸件不具有近乎即时处理效果；进度询问中出现新地址不会代替明确改址请求；特殊人群例外。
3. [AR-11 页面](https://www.uscis.gov/ar-11)，同方法完整主文，更新 2026-06-03；[AR-11 PDF](https://www.uscis.gov/sites/default/files/document/forms/ar-11.pdf)，HTTPS 200 后 pypdf 实读两页，11/02/22 版。核对实际住址不接受 PO Box、签名、10 天和移民法庭须另报。正文没有硬编码可能变动的寄送地点。
4. [VAWA/T/U 与 I-751 虐待豁免专门程序](https://www.uscis.gov/forms/filing-guidance/how-to-change-your-address/change-of-address-procedures-for-vawatu-cases-and-form-i-751-abuse-waivers)，同方法完整主文，更新 2025-12-22：Contact Center、回执和申请副本、身份核验、安全消息及专门回电、实际办案中心、安全邮寄地址、其他 pending benefit 同样受保护、各案 G-28。
5. [I-865 当前入口](https://www.uscis.gov/i-865)，同方法完整主文，更新 2026-06-05；[I-865 说明](https://www.uscis.gov/sites/default/files/document/forms/i-865instr.pdf)，11/10/20 版实际读第 1—3 页。核对有效担保协议、30 天、每名担保人单独签交、LPR 另外履行 10 天义务、保留副本及寄送和收件证据。正文未将所有历史担保一律视为仍有效。
6. [8 CFR 214.2，LII 法规文本](https://www.law.cornell.edu/cfr/text/8/214.2)，HTTPS 正文实际读 `(f)(17)`、`(m)(18)`：10 天内按学校方式向 DSO 报告可满足 265.1；实际住址原则及不能在住所收信时的特别处理。[DHS I-20 示例](https://studyinthestates.dhs.gov/assets/sample_formi20.pdf) web 403，普通 HTTPS 下载成功；经已忽略路径保存，以 pdftoppm 渲染并实际看第 3 页，11/30/2025 版 Notice of Address 明确 10 天及 DSO 更新 SEVIS。
7. [USCIS Policy Manual 2-D-3](https://www.uscis.gov/policy-manual/volume-2-part-d-chapter-3)，web 403 后普通 HTTPS 正文成功，实际读 D 节及相关脚注：J-1 在 10 天内按 sponsor 程序告知 RO，通过 SEVIS 项目完成相应报告。正文没有使用来源间可能不同的 RO 内部录入时限。
8. [USPS Change of Address — The Basics](https://faq.usps.com/articles/Knowledge/Change-of-Address-The-Basics)，web 实读 article 000005313：身份核验与现场 PS 3575、在线验证费用、家庭与个人选项、旧址及新址确认、线上确认码、丢失确认码处理、未经本人申请的争议入口、邮件类别及寄件人退回指令。稿件范围限定普通境内住宅搬家，没有将此入口套给所有军邮、商业地址和国际迁居。
9. [EOIR 更新信息](https://www.justice.gov/eoir/update-respondent-or-alien-information)，web 完整相关主文，更新 2026-05-18；[Respondent Access EOIR-33/IC instructions](https://respondentaccess.eoir.justice.gov/en/forms/eoir33ic/)，web 实读指引。核对 5 个工作日、IC/BIA 区分、每个受影响当事人单交、DHS 副本及送达证明、其他动议或信函不代替 EOIR-33。
10. [ICE 机构联系资源](https://www.ice.gov/detain/attorney-information-resources)，普通 HTTPS 实读 Online Change of Address Tool 段：ICE 更新之后仍指引当事人另交 EOIR-33。[ICE Change of Venue handout](https://portal.ice.gov/videos/Video-ChangeofVenue/Handout-ChangeofVenue%28English%29.pdf)，HTTPS 200 后 pypdf 实读第 1、4 页，更新 2024-09-26：独立提出 venue motion，在获准并改排以前继续按原法院庭期出庭。
11. [EOIR Self-Help Legal Materials](https://www.justice.gov/eoir/self-help-materials)，web 完整相关主文，更新 2026-10-01：实际存在找律师、搬家及 missed hearing 专门入口；本稿仅作有问题时的转介，没有自行概括撤销缺席决定的法定期限。
12. [IRS Topic 157](https://www.irs.gov/taxtopics/tc157)，web 完整主文；[Form 8822 当前入口](https://www.irs.gov/forms-pubs/about-form-8822)，HTTPS 主文；[8822 PDF](https://www.irs.gov/pub/irs-pdf/f8822.pdf)，HTTPS 200 后 pypdf 实读两页，2021-02 版。核对报税时新地址处理后更新、8822/8822-B、签名书面通知或核验电话、联合申报与分居、孩子自己有税表时的单独通知、依旧址与类别选寄送地址。当前 Topic 157 的一般 45 天与旧表 4—6 周是处理预估差异；稿件明确采用当前网页且未写成法定期限。
13. [SSA Update Contact Information](https://www.ssa.gov/life-events/update-contact-information)，web 完整主文：地址和电话更新工具针对已经领取待遇的人，部分待遇需电话处理；电话及 TTY 数字相符。没有把所有 SSN 持有人写成同一种强制网页改址。

## 适用与审阅边界

核验的是境内个人搬家的具体成稿及必要上下文；没有登录任何个人账户、提交表格、验证读者个案，亦未将官方服务页面可读等同于线上申请全程可用。州驾照、学校、医保和税务衔接是已成稿主题的内部转介，本页没有另造地方期限。USCIS 特殊收养、领事处理、代理人办公地址与国际迁居细目没有展开，普通流程用“一般情况下”限定并直接链接列明特殊程序的官方主入口。

结果检查与受阻路径完整：按人、机构和案件留记录；未确认、漏回执、仍寄旧址继续处理；保护案件先解决安全地址；原庭期和补件期限不中断。只审阅和写本记录，未改作者正文。
