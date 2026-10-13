# 求职、录用核对与入职

更新：2026-10-13。B07 作者 banking_fact；独立事实审计划 static_editor，第三人静态审 root。本文合并领域地图的 `job-search` 与 `offer-onboarding`，沿同一次求职行动展开；不把导航、地图或来源清单登记为成稿。

| 页面与用途 | 对象和行动边界 | 已集成依赖 | 当前状态 |
|---|---|---|---|
| `content/book/work/career/job-search-onboarding.md`；`work.career.job-search-onboarding`。从已有经历选择岗位、准备申请和面试，核实招聘方、处理背景调查，确认录用条件并完成入职到第一笔工资。 | 普通成年私营雇员求职者，覆盖服务业及小时工；美国联邦手续及加州、纽约州、华盛顿州、得州公共就业服务和影响步骤的州分支。按雇员入职写；独立承包、职业执照、个别移民授权、政府职位和特殊行业须按相应制度另查。 | 工资、号码、身份文件、税务居民、医保衔接与费用、医生网络、银行付款、服务语言及法律求助的实际集成路径，见下方依赖。 | written / draft true；verified 与 reviewed_by 均为空。完整稿已完成作者逐项核对，正文 SHA 已冻结，待异人事实审；不登记独立 PASS、构建或正式集成。 |

## 正文冻结与依赖

正文 SHA-256：`f5c8738b3677bb8dca0c3ba73dcdf2d9c01f668360ff18de15ba570c618e42bc`。计算范围为 UTF-8 文件按 `split('---', 2)[2]` 取出的完整正文，不含 frontmatter。作者 banking_fact；事实审由 root 另派 static_editor，第三人静态审 root，三人身份不相互代替。

实际站内依赖：`/book/work/employment/pay-stub-overtime/`、`/book/life/documents/numbers/`、`/book/life/documents/status-documents/`、`/book/work/tax/tax-residency/`、`/book/people/health/coverage-changes/`、`/book/people/health/insurance-costs/`、`/book/people/health/appointment-network/`、`/book/work/finance/banking-payments/`、`/book/people/language/service-conversations/`、`/book/rights/legal/finding-help/`。这些目标正文实际存在；不链接未写主题。

## 已写入的行动链

1. 把工作经验、技能、可上班时间、交通范围和需要的协助对应到岗位；提供公共就业中心与四州实际入口，核对服务、预约及具体训练资格。
2. 让读者能够实际整理履历、填申请、练习面试和记录跟进；教学虚构示例不产生可提交表件。
3. 从雇主自己的联系方式核对职位、联系人和现场；识别付钱换工作、假支票购设备、包裹转寄与索取敏感资料的招聘诈骗。
4. 区分外部背景报告程序与雇主自行了解信息；写清书面授权、预不利决定材料、纠错回应和最终通知。州法改变犯罪记录询问顺序时放进此步，避免由一项制度推断另一项资格。
5. 接受前核对工资计算、实际工时与地点、条件和开始日、扣缴、福利生效、发薪和 direct deposit；工资与保障详细规则转给已集成主题。
6. 回源当前 I-9 版本、员工 Section 1 与雇主核验期限、员工文件选择、翻译协助及 SSN 边界；身份限定工作须在开始前核对真正授权。
7. 第一班与第一笔工资各有确认结果；被拒、延迟、报告有误、身份核验或语言协助受阻时有继续路径。

## 实际证据与尚未核实的边界

已实际读取 CareerOneStop、四州公共就业提供者、FTC / EEOC / CFPB、USCIS / DOJ IER / E-Verify 和 IRS 对应一手原文。各来源具体读取范围、版本、日期、失败及未读边界见 `ops/evidence/job-search-onboarding.md`。得州 TWC 主站机器人挑战未解决，正文采用已实际可读的 TWC LMCI 官方目录入口与 Gulf Coast 本地公共服务，明确当地服务边界；未冒用搜索摘要作主站已读。地方政府、职业许可、承包分类、个人移民资格及各雇主福利条款不预先承诺。

维护时复查 I-9 接受版本、核验规则、州公平招聘和薪资披露规则、公共就业入口；不把草案或未来生效规则写成当前义务。

## B07主控正式登记

2026-10-13，root。当前正文与独立事实／第三静态摘要相符，元数据安装后正文未变；已完成79 HTML生产检查、1440／390两端48次页面访问／20检索和实际关键视图、154页PDF的11页目视抽查，现登记正式集成。源前整文件摘要保留作者冻结版本；候选后整文件见 `ops/reviews/b07-integration.md`。public同步以该记录的实际后续核对为准；未外部发布。
