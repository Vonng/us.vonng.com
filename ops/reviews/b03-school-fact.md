# B03 公立学校入学：独立事实审

审查人：documents；作者 health，为不同参与者。查阅日期：2026-10-13。对象：`content/book/people/school/school-enrollment.md`。

结论：事实审通过，无需正文事实修订。完整重读稿件后，作者又按第三人静态审将两处 CDE URL 的 `/CI/` 规范为本轮实际读取成功的 `/ci/`。审阅者重新核对：逆转这两处 URL 后哈希等于上一版，确认没有其他正文变化。最终正文 SHA-256：`b8a01b4ae60bdc4441c9ace62002b07b90dc47e629dd06653dea6868b1f03cc0`。计算方法为 `sha256(text.split('---', 2)[2].encode('utf-8'))`，不含 frontmatter。第三人静态审、候选元数据及构建由主控另行完成。

## 独立实际阅读及结论

阅读作者证据后独立打开以下来源，核对实际文本。web 返回 403 或不能正常取文时，使用普通 HTTPS 获取并以 BeautifulSoup 提取正文；没有把搜索摘要当作原文。联邦法阅读下列指定条款，不声称审过整章教育法。

| 来源 | 实际核对范围及判断 |
|---|---|
| [WA OSPI：移民学生入学权利](https://ospi.k12.wa.us/policy-funding/equity-and-civil-rights/immigrant-students-rights-attend-public-schools) | 入学权利、移民身份及 SSN 段：无合法身份本身不构成拒绝公立基础教育理由；SSN 请求须说明是否自愿、法律依据、用途，不能因不提供而拒收。稿件限定当地生活家庭，将专程留学另列，没有扩大到一切身份及教育类型。 |
| [WA OEO：School Enrollment](https://www.oeo.wa.gov/en/education-issues/school-enrollment) | 年龄替代证明、实际居住、父母缺席时照顾者登记、片区和满额、转校、无稳定住所及寄养段均实际阅读。稿件没有把法院监护手续设为一律必需，也没有把寄养自动等同于 McKinney–Vento。 |
| [CDE：Kindergarten FAQ](https://www.cde.ca.gov/ci/gs/em/kindergartenfaq.asp) | 页面更新 2025-12-18；普通入学五岁截止 9 月 1 日、满五岁后学区个别晚入学。初稿大写 `/CI/` 路径在本轮部分获取方式重定向失败，使用同一 CDE 页面的小写路径实际读到正文；最终稿两处均已换成该小写路径，不是凭搜索摘要核对。未将 TK 或个别提前安排与普通规则混写。 |
| [SFUSD：Apply](https://www.sfusd.edu/schools/enroll/apply) | 当前 2026–27 学年新生全年申请、Enrollment Center、ParentVUE 和纸质办理、身份/年龄/住址/健康与转学材料、优先顺序与空位。页面还预告 2027–28 轮次，稿件正确区分下一学年项目窗口与当前普通入学。 |
| [NY OAG 与 NYSED 联合指导](https://ag.ny.gov/education-students/safeguarding-rights-immigrant-students) | Enrollment and registration 正文：不得按移民身份或英语水平拒绝、接受多种住址证明、登记时不得要求 SSN 或揭示移民身份的信息。以共同发布机构 OAG 可读正文核对，并未把 NYSED 不可读页记作已读。 |
| [NY OAG：Free public education](https://ag.ny.gov/resources/individuals/education-students/free-public-education) | 居住证据替代材料、出生证明替代、拒绝居住认定的书面理由和申诉说明、投诉入口。页面还涉及疫苗期限，稿件未采纳该期限，本次也不以此代查临床补种条件。 |
| [NYC：Family Welcome Centers](https://www.schools.nyc.gov/enrollment/enrollment-help/family-welcome-centers) | 有片区学校 K–8 通常联系学校、无片区学校及需安置帮助联系 FWC、预约与线上/线下帮助。稿件没有承诺特定学校名额或统一入学日期。 |
| [Seattle：Enroll My Student](https://www.seattleschools.org/enroll/enroll-my-student/) | 2026–27、五岁截止 8 月 31 日、普通申请两份住址证明、年龄材料与替代、免疫记录、Admissions 帮助。页面中混有旧 2025–26 无家可归学生 hold 文案；下列联邦法及正式学区政策另行核对，稿件没有把网页排队提示转写为可延迟入学的权力。 |
| [WA DOH：School and Child Care Immunization](https://doh.wa.gov/community-and-environment/schools/immunization) | 实读 CIS/COE、医学核验记录、境外有医疗机构/人员印章记录及译文、不能只把记录订在空白 CIS、有条件入学及 homeless/foster 例外。稿件要求学校和医疗人员核验，没有把某州表格、补种日程或豁免理由推广到全国。 |
| [TEA：Enrollment in Public School](https://tea.texas.gov/about-tea/contact-us/general-inquiry/enrollment-public-school) | 地方学区负责具体学校边界及材料，州不持有各校正式边界图；转入私校、家庭教育、外州或境外学生的课程、成绩及评估材料。高中学分衔接表述是与校方核对的行动建议，不承诺特定学分承认结果。 |
| [Austin ISD：Enroll](https://www.austinisd.org/enroll) | 2026–27 普通 K–12 登记、Find Your School、Enroll Austin、帮助入口，转校与 magnet 等窗口分别处理。未登录个人报名账号或替虚构住址测试分配。 |
| [42 USC §11434a](https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap119-subchapVI-partB-sec11434a.htm) | 全部定义，重点 (1)、(2)、(6)：enroll 包括课堂及学校活动；固定、常规且适当夜间住所，经济困难借住/无替代旅馆等具体限制；无人陪伴青少年定义。稿件没有将普通合租或正常搬家短住自动认定为 homeless。 |
| [42 USC §11432](https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap119-subchapVI-partB-sec11432.htm) | 独立实际阅读 (g)(1) 至 (6)，重点 (1)(J)、(3)、(6)：学校选择按最佳利益，原学校推定及家庭意愿，缺件及错过期限立即入学，资格/择校/入学争议及申诉全程在请求学校立即就读，书面解释、联络员、原校交通和健康记录协助。各项保障在正文均保留适用条件。 |
| [Seattle Board Policy 3115](https://www.seattleschools.org/about/school-board/policies/3115-homeless-students-enrollment-rights-and-services/) | 完整政策实际阅读，页面载 2022-03-16 修订：学校选择、缺件、争议及交通规则与联邦法相符。用它核对当地权利，而不依旧网页 hold 提示推断实际处理方式。 |

## 边界

稿件是当地居住家庭进入公立 K–12 的办理指引，并非 F-1 学费或专程留学说明；州和学区例子均明确地点，未混成全国统一文件份数、生日门槛或申诉期限。材料表使用一般准备办法并要求当地确认。没有给出具体疫苗剂次、可用豁免诊断、个别 IEP/504 资格或具体学生应就读学校的结论。

未核实范围包括个案住址和学区边界、具体空位、某名学生最佳利益或 homeless 资格、地区系统内部实际处理速度、各州全部免疫与申诉细则。正文没有依赖这些未核实结论。学校入口中的旧学年杂项文案已经与当前页面、正式政策和法律区分；本次通过不代表认可其所有未引用内容。
