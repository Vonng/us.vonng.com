# 医疗保险、就医与账单地图

主控状态（2026-10-13）：本文件所列B01已写主题均已独立核验、静态审、集成与本地构建／渲染通过，提交 c292949；正式版本见 reviews/acceptance.json。下方作者研究阶段记录保留，后续候选仍未完成。

当前状态（2026-10-13）：首批三个完整草稿已写入，作者 `/root/health`；待另一参与者独立事实审、第三人静态审与主控集成。未构建、未发布。只修改本批三个正文及本地图、证据文件。

| 页面问题与 description | 稳定路径 / page_id | 边界与对象 | 依赖 | 来源方向 | 状态 / 未确认项 |
|---|---|---|---|---|---|
| 医疗保险的钱怎样算；读懂保费、免赔额、共付、共保和自付上限，用计划文件估算看病成本 | `/book/people/health/insurance-costs/` / `people.health.insurance-costs` | 全国概念，个人与雇主常见结构；Marketplace 上限概念限定对象，不列全国统一年度金额 | 无；向预约与账单页交叉链接 | HealthCare.gov SBC、费用、术语、计划类型 | written；未确认个别计划、家庭累计条款和具体报价 |
| 预约看病前怎样查网络、转诊和预授权；确认就诊地点与手续 | `/book/people/health/appointment-network/` / `people.health.appointment-network` | 计划性就诊；急诊只保留立即求助与手续例外；保险合同及服务场所层次 | insurance-costs | HealthCare.gov 医生目录与术语；CMS No Surprises Act | written；未核实任何特定诊所目录、预约门户或授权清单 |
| 收到账单怎样核对、申诉和申请援助；读懂虚构 EOB 并区分纠错、拒赔和支付困难 | `/book/people/health/medical-bills/` / `people.health.medical-bills` | 全国核对方法；具体期限以 Marketplace 联邦说明为例，Medicare/Medicaid 分流；FAP 限适用医院 | insurance-costs、appointment-network | CMS EOB、NSA 与援助；HealthCare.gov 申诉；IRS 501(r)(4) | written；DOL 原文 403，未扩写雇主计划期限；州申诉和医院援助门槛留后续 |

## 后续候选（仅地图，不生成页面或正式导航）

| 问题 / 暂定描述 | 候选路径 | 必需范围与依赖 | 首轮资料 | 状态与缺口 |
|---|---|---|---|---|
| 从哪里取得医疗保障；分辨雇主、Marketplace、Medicare、Medicaid/CHIP 与学生／旅行保险 | `/book/people/health/coverage-options/` | 全国入口及适用对象，先讲渠道，再接 eligibility 与计划资格；依赖费用概念 | HealthCare.gov、Medicare、Medicaid、DOL；具体学校与保单 | planned；资格与投保窗口尚未研究 |
| 失业、换工作、迁州和家庭变化后的医疗衔接 | `/book/people/health/coverage-changes/` | 雇主终保、Marketplace SEP、COBRA、州延续保障及 Medicaid 转州；链接失业与搬家事项 | DOL、HealthCare.gov、重点州市场 | planned；结束与生效日期、资格、补件及空档必须回源 |
| 基层医生、urgent care、急诊与药房怎样分工 | `/book/people/health/care-options/` | 避免自我诊断，提供服务角色、预约可及性与紧急求助 | CMS、MedlinePlus、当地系统 | planned；乡村与偏远可及性、无保险就医、牙眼科另分支 |
| 处方药续配、药品目录、牙科眼科 | `/book/people/health/prescriptions/` | 药品层级、续配、药房、预授权与替代方案；牙眼科是否独立拆页待去重 | FDA、Medicare、实际计划 | planned；不写药物治疗建议 |
| 预防服务、疫苗、公共卫生、病历和知情同意 | `/book/people/health/prevention-records/` | 按年龄、服务、保险类型和实际政策分流；HIPAA 记录获取期限另核实 | CDC、HHS OCR、HealthCare.gov | planned；当前疫苗与预防政策尚未研究 |
| 加州、纽约州、华盛顿州、得州的保障、投诉和援助差异 | `/book/people/health/ca-coverage/` 等 | 按实际机构和计划监管范围，不能把州保险部门管辖套到所有自筹资雇主计划 | Covered California、NY State of Health、WA Healthplanfinder、TX DOI 与 Medicaid 机构 | planned；必须补四州主要路径及地方案例 |

本批交付证明的是费用—预约—账单的基础阅读链，不能据此认定医疗领域或全书覆盖完成。
