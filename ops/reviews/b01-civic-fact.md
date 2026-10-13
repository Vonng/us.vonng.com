# B01 civic / finance / safety 独立事实审

审查人：documents（与作者 civic、第三人静态审 root 分离）。审查日期：2026-10-13。结论：三篇正文事实审通过，可交第三人静态审及主控构建；此记录不等于已发布或渲染验收。

## 冻结版本

SHA-256 仅绑定去掉 frontmatter 后的正文：`sha256(text.split('---', 2)[2].encode('utf-8'))`。主控只改审阅元数据不影响此绑定；正文再改应复核。

| 路径 | 正文 SHA-256 | 结论 |
|---|---|---|
| `content/book/foundations/government/which-government.md` | `2bba54971e426152ce774fce4804325aafdf25ed47371495eefaebe48a74dc7c` | 通过 |
| `content/book/work/finance/credit-records.md` | `6e17c15a7c69fa7f55055f41624f0d15ed206a93bf2ad5f2894d0986c2e71d23` | 通过 |
| `content/book/rights/safety/emergency-help.md` | `49a8d07854505ac39f6dc4463b7d8e36d06847089314403c8e507c5c469ee095` | 通过 |

完整重读三篇稿件，并独立打开以下一手资料的相关正文。作者证据只用来定位来源，没有以作者记录或搜索摘要代替本轮阅读。网页通过 web open 或普通 HTTPS 请求读取；PDF 通过原件文本读取。

## 政府分工与法源

| 实读来源 | 核对位置与结论 |
|---|---|
| [NARA 权利法案](https://www.archives.gov/founding-docs/bill-of-rights-transcript)、[USAGov 三部门](https://www.usa.gov/branches-of-government) | Amendment X 与三个部门正文；联邦制和机关分工表述没有把所有权限简单划成互斥范围。 |
| [联邦机关目录](https://www.usa.gov/agency-index)、[州与属地目录](https://www.usa.gov/state-governments)、[地方目录](https://www.usa.gov/local-governments) | 独立读到目录用途、州/属地条目及地方入口。稿件五个属地正确，没有将目录中的自由联系国误称属地。 |
| [Census 政府分类](https://www.census.gov/programs-surveys/gus/about/glossary.html)、[邮政城市与行政地理](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/usps_census_city.html) | County、school district、special district 等定义，以及正文首段和地址案例。稿件限定为政府统计分类，并指出邮寄城市不能确定行政或学区归属。 |
| [DC 政府组织](https://oca.dc.gov/page/dc-government-organization) | Home Rule、三部门及国会保留权力，支持特区不能套邻州手续。 |
| [BIA FAQ](https://www.bia.gov/frequently-asked-questions)、[Cherokee Nation Constitution](https://cherokee.gov/our-government/cherokee-nation-constitution/) | BIA 法律地位、联邦承认与主权段；Cherokee 页 framework 及 Executive/Judicial/Legislative 链接。稿件不把 Tribal Nations 当成县市下级，也不将 Cherokee 的结构推广给其他 Nation。 |
| [USAGov 法律检索](https://www.usa.gov/research-laws)、[OFR 法规制定指南](https://uploads.federalregister.gov/uploads/2013/09/The-Rulemaking-Process.pdf)、[GovInfo 行政命令](https://www.govinfo.gov/features/executive-orders) | 法律检索与 U.S. Code 说明；PDF 第 2、7、11 页授权、Effective Date/applicability、guidance 与司法审查；GovInfo About 段。稿件对议案、成文法、法规、指引、命令及个案法院命令的区分成立。 |

边界：核验的是文章所述制度与查找方法，没有核查任何具体地址的服务权限、个案诉讼命令或部落法院案件。Cherokee 的 www 网址多次超时，去掉 www 后官方同页正文成功读到；不以超时推断内容错误。

## 信用档案、冻结、争议与盗用

| 实读来源 | 核对位置与结论 |
|---|---|
| [CFPB report/score](https://www.consumerfinance.gov/ask-cfpb/what-is-the-difference-between-a-credit-report-and-a-credit-score-en-2069/) | 完整问答：报告记录与不同评分模型/资料/日期，支持先核对记录。 |
| [FTC 免费报告](https://consumer.ftc.gov/articles/free-credit-reports)、[CFPB 免费报告](https://www.consumerfinance.gov/ask-cfpb/how-do-i-get-a-free-copy-of-my-credit-reports-en-5/)、[实际申请表 PDF](https://www.annualcreditreport.com/assets/requestformfinal-BgD0iCRQ.pdf) | 每周免费服务与法定 12 个月区分；877-322-8228、邮寄地址、身份字段、旧地址两年、收到后 15 天处理寄出；不利决定通知后 60 天。稿件没有把处理寄出日当必然到达日。 |
| [CFPB 冻结](https://www.consumerfinance.gov/ask-cfpb/what-is-a-credit-freeze-or-security-freeze-on-my-credit-report-en-1341/)、[Experian 冻结](https://www.experian.com/help/credit-freeze/)、[TransUnion 冻结](https://www.transunion.com/credit-freeze) | 费用、分别办理、电话/电子 1 工作日设置和 1 小时解除、邮寄 3 工作日、protected consumers、已有债权人和就业/租客/保险例外；两家公司实际电话及邮寄入口。稿件对作用有边界，未照抄 FTC 的绝对阻止开户表述。 |
| [FTC 争议](https://consumer.ftc.gov/articles/disputing-errors-your-credit-reports)、[CFPB 争议](https://www.consumerfinance.gov/ask-cfpb/how-do-i-dispute-an-error-on-my-credit-report-en-314/)、[调查期限](https://www.consumerfinance.gov/ask-cfpb/how-long-does-it-take-to-repair-an-error-on-a-credit-report-en-1339/)、[CFPB 投诉](https://www.consumerfinance.gov/complaint/) | 准确负面记录与错误区分、向报告机构和供数方递交、材料副本、拒查理由、30/45 天调查与 5 工作日通知、当前入口的先直接争议要求。结果标志是更正字段和书面结果，不是分数变化。 |
| [CFPB 身份盗用](https://www.consumerfinance.gov/ask-cfpb/what-do-i-do-if-i-am-a-victim-of-identity-theft-en-31/)、[FTC 警示](https://consumer.ftc.gov/articles/credit-freezes-and-fraud-alerts)、[FTC 身份盗用](https://consumer.ftc.gov/articles/what-know-about-identity-theft) | 受影响账户直接处理；初始一年/延长七年及报告条件；一家警示通知其他两家；符合要求后四工作日屏蔽及拒绝/撤销条件；多语言报案 877-438-4338 按 3，口译 9–17 ET。 |

边界：没有登录征信门户、递交申请或电话实拨。无 SSN 的具体人工材料因公司而异，稿件只要求询问，没有承诺 ITIN 通用。未核各州另加保护，也未将示例逾期认定当成真实纠错结果。免费频率及公开服务渠道以此次查阅为截点。

## 911、988 与非紧急求助

| 实读来源 | 核对位置与结论 |
|---|---|
| [911 Calling](https://www.911.gov/calling-911/)、[911 FAQ](https://www.911.gov/calling-911/frequently-asked-questions/) | 何谓紧急、所需位置与电话、勿先挂断、误拨、短信与未送达提示、未激活无线电话/无法回拨、VoIP 地址、TTY、异地十位号码。稿件保留当地覆盖、可用信号及跨区转接边界。 |
| [Seattle CARE 实际指南](https://withcare.seattle.gov/2025/10/08/your-guide-to-calling-9-1-1-in-seattle/) | 问题顺序、消防转接、非紧急 206-625-5011、电话语言与短信、响应受资源影响。稿件明确城市案例，不把号码和语种推广全国；未引用网页尚有占位符的网上报案段。 |
| [988 为他人求助](https://988lifeline.org/help-someone-else/)、[接通后流程](https://988lifeline.org/get-help/what-to-expect/)、[语言口译](https://988lifeline.org/faq/calling-the-988-lifeline/faq-is-the-988-lifeline-available-in-other-languages-for-non-english-speakers/)、[短信语言](https://988lifeline.org/faq/texting-the-988-lifeline/faq-can-i-text-with-the-988-lifeline-in-my-preferred-language/) | 情绪困扰和亲友可求助、咨询员沟通、免费与全天语言接入、电话多语口译、短信/聊天仅英西语。稿件没有暗示中文短信已有口译。 |
| [988 听障入口](https://988lifeline.org/deaf-hard-of-hearing-hearing-loss/)、[保密](https://988lifeline.org/confidentiality/)、[连接困难](https://988lifeline.org/faq/calling-the-988-lifeline/faq-what-do-i-do-if-i-have-trouble-connecting-when-i-call/) | ASL 视频、TTY/711；可以不主动给姓名地址，但通常收到号码/IP，保密有例外且地方中心政策可能不同；无法电话接入可换短信/聊天，医疗急症用 911。 |

SAMHSA In Crisis 页本轮 web 和普通请求均 403，未记为成功阅读。其在文章中承担的危机分流、全天候和沟通流程断言由以上实际读到的 National 911 Program 与 988 运营方一手资料交叉核实。未实际拨热线或测试紧急短信；未承诺匿名、永不派警、到场时间或具体处理结果。

## 复核意见

未发现阻止进入静态审的事实错误。已有教学虚构标记、适用范围、受阻路径和结果记录要求。后续若增加具体法院命令、办理资格、收费、期限、服务语种或门户按钮，应重新回源；不能将本次审查扩展为对该机构所有业务的认可。
