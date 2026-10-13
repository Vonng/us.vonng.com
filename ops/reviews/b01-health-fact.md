# B01 医疗三页独立事实审

- 审阅人：`/root/civic`；作者：`/root/health`。两者为不同参与者。
- 实际回源日期：2026-10-13。
- 审阅范围：下列三篇完整正文及其行动、金额、期限、适用对象、例外与真实来源；不代替第三人静态审、隔离构建或渲染验收。
- 结论：三篇在现有范围内 **事实审通过** ，没有待作者修改的阻断项。须由第三名参与者继续静态审，主控完成工程验收后才可安装正式核验元数据。

## 绑定的实际正文

SHA-256 按实际文件读取后的 `split('---', 2)[2]` 字符串，以 UTF-8 编码计算；不包含 front matter。2026-10-13 落审阅记录前重新计算，与本次回源审阅版本一致。

| 正文路径 | 正文 SHA-256 | 结论 |
|---|---|---|
| `content/book/people/health/insurance-costs.md` | `c9ffeddbe4ab79912751089ee35114d95e5264fa211a58e9dc3ac7be0a4c5d3b` | 通过 |
| `content/book/people/health/appointment-network.md` | `4c8d3b8551eb31ed9778e29a6a5b9724ee1fbe6bbf53f9d409e8e10c85b76de6` | 通过 |
| `content/book/people/health/medical-bills.md` | `485addc8f652f6ebe777814fa5527e8c43f406519cf50d0d809a74be90304fd0` | 通过 |

审阅者实际完整阅读了三篇文件，并分别打开以下官方正文。作者的 `ops/evidence/health.md` 用于识别待查断言，不作为已经核实的替代证据。表中短引文是本次实际读到的原文，定位使用页面标题或章节；页面改版后应重新定位，不能仅复用行号。

## 费用结构与文件

| 实际阅读来源、定位与原文锚点 | 独立核验结论 |
|---|---|
| [HealthCare.gov：SBC](https://www.healthcare.gov/health-care-law-protections/summary-of-benefits-and-coverage/)，`Does this apply to my plan?`：`including grandfathered plans`；`Where can I find a Summary of Benefits and Coverage?` | 个人与雇主计划的 SBC 要求、可向计划索取及术语表均有依据；正文没有把教学摘要当作个案报价。 |
| [CMS：完成的 SBC 样表 PDF](https://www.cms.gov/CCIIO/Resources/Forms-Reports-and-Other-Resources/Downloads/Sample-Completed-SBC-Accessible-Format-01-2020.pdf)，第 1 页：`Coverage Period`、`Coverage for`、`Plan Type`；第 2 页设施与医生收费条目 | 审阅者额外实际打开 5 页 PDF，核对首页确有计划、期间与承保对象字段。样表列 2025 承保期间，OMB 标示到期日 2026-05-31；仅验证字段存在，不用其日期、费率或资格代表当前保险产品。 |
| [HealthCare.gov：全年成本](https://www.healthcare.gov/choose-a-plan/your-total-costs/)，`Your total costs for health care`、`Compare estimated total costs`：`premium, deductible, and other out-of-pocket costs` | 保费、免赔额与其他自付应共同比较；稿件的低保费不必然低全年支出、年度情景比较有依据。 |
| [HealthCare.gov：Deductible](https://www.healthcare.gov/glossary/deductible/)，词条正文：`separate deductible`、`individual deductible`、`family deductible` | 某些服务可在满足免赔额前承保、药物可另设额度、家庭与个人额度并存有依据。稿件正确让读者继续查具体累计规则。 |
| [HealthCare.gov：Allowed amount](https://www.healthcare.gov/glossary/allowed-amount/)，定义与 balance billing 段：`can't balance bill you for covered services` | 认可金额与合同折让的解释可支持网络内承保算例；正文没有把它外推到所有网络外服务。 |
| [HealthCare.gov：Out-of-pocket maximum](https://www.healthcare.gov/glossary/out-of-pocket-maximum-limit/)，定义及排除项：`in-network care and services`、`Monthly premiums` | 通常累计项与保费、不承保、一般网络外费用等排除项对应原文。稿件限定 Marketplace 通常结构，并另引账单保护例外，没有宣称全家所有医疗费用绝对封顶。 |
| [HealthCare.gov：计划类型](https://www.healthcare.gov/choose-a-plan/plan-types/)，`Types of Marketplace plans` 下 EPO、HMO、POS、PPO 条目：`except in an emergency`、`without a referral` | 网络、急诊例外及转诊差异有依据；正文采用“通常／一般”，没有替某个产品作承保保证。 |

费用页虚构算例独立复算：`200 + (600 - 200) × 20% = 280`；计划份额 `400 × 80% = 320`。免赔额尚余、自付上限未触及、网络内承保的前提均在算例前明确。

## 预约、网络与急诊边界

| 实际阅读来源、定位与原文锚点 | 独立核验结论 |
|---|---|
| [HealthCare.gov：寻找计划内医生](https://www.healthcare.gov/using-marketplace-coverage/getting-medical-care/)，`Finding a doctor in your plan`：`provider directory`、`Call your doctor's office` | 目录、保险方电话与医生办公室的核对入口均真实存在。稿件要求核对具体计划、地点和日期属于合理行动建议，不是声称已经核实某位医生。 |
| [HealthCare.gov：Referral](https://www.healthcare.gov/glossary/referral/)，词条：`A written order from your primary care doctor` | PCP 书面转诊及许多 HMO 未转诊可能不付的解释有依据；没有写成所有计划统一规则。 |
| [HealthCare.gov：Preauthorization](https://www.healthcare.gov/glossary/preauthorization/)，词条及末句：`isn't a promise your health insurance or plan will cover the cost` | 医疗必要性事先决定、其他名称与批准不保证付款均有依据。谁提交、地点、次数、期间被写成应问本计划的问题，没有编造全国统一流程。 |
| [HealthCare.gov：急诊保护](https://www.healthcare.gov/health-care-law-protections/doctor-choice-emergency-room-access/)，`Emergency room access`、`Does this apply to my plan?`：`can't require prior approval` | ACA 急诊预批准限制与 grandfathered 适用边界都已进入正文；稿件没有把非急诊预约核对流程放到危及生命的就医之前。 |
| [CMS：使用保险的账单权利](https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/know-your-rights/insurance)，`Getting care from out-of-network providers at in-network facilities`、救护车说明：`ground ambulance services` | 网络内设施里可有网络外提供者，及联邦 NSA 对地面救护车的排除均可支持稿件。已实际继续阅读适用设施、计划排除、notice and consent 与不得豁免的服务说明。 |
| [CMS：不使用保险的权利](https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/know-your-rights/without-insurance)，good faith estimate 与争议段：`at least 3 business days`、`at least $400`、`120 days` | 不使用保险、预约／主动请求、急诊例外、现阶段各提供者及设施分别估算都有原文支持。正文未把这些权利扩展成使用保险患者的普遍报价保证。 |

口译、无障碍、是否接收新患者及预约取消规则被写成事先提出和核对的需求；没有承诺每个诊所均提供同一种服务。

## EOB、争议、申诉与经济援助

| 实际阅读来源、定位与原文锚点 | 独立核验结论 |
|---|---|
| [CMS：读懂 EOB](https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/get-help/guides-resources/read-explanation-benefits)，`What's an EOB?`、`What's on an EOB?`：`An EOB isn't a bill`；页面帮助热线：`1-800-985-3059` | 患者／理赔／日期字段、认可金额、计划支付、患者余额和备注均可回查；EOB 未必反映已付费用有依据。帮助热线号码与多语言支持在原文可见。 |
| [HealthCare.gov：内部申诉](https://www.healthcare.gov/appeal-insurance-company-decision/internal-appeals/)，提交说明与 `How long does an internal appeal take?`：`180 days`、`30 days`、`60 days` | 稿件正确区分申请期限与审查完成期限、已接受／尚未接受服务；书面理由、资料及副本保存路径完整。紧急情形可同时寻求内外审有依据。 |
| [HealthCare.gov：外部审查](https://www.healthcare.gov/appeal-insurance-company-decision/external-review/)，`Filing a request`、可外审决定、`How long does external review take?`：`4 months`、`45 days` | 4 个月与标准 45 天均在原文；医疗判断、试验性治疗等符合条件的范围已保留，没有把所有拒赔都说成可外审。州程序可能更有利的说明有依据。 |
| [Medicare：Filing an appeal](https://www.medicare.gov/providers-services/claims-appeals-complaints/appeals)，按 Original Medicare、health plan、drug plan 分流及帮助段：`free, personalized help` | SHIP 免费帮助和三类入口均实际可读。稿件明确不把 Marketplace 的 180 天／4 个月套用于 Medicare。 |
| [Medicaid：Where Can People Get Help with Medicaid & CHIP?](https://www.medicaid.gov/about-us/where-can-people-get-help-medicaid-chip)，页面开头与州联系目录：`Claims`、`State Medicaid Agency` | 州机构作为理赔等问题的实际联系入口有依据；稿件没有宣称各州听证或申诉期限统一。 |
| [CMS：使用保险的账单权利](https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/know-your-rights/insurance)，`What health insurance is covered?`、三种保护情形、`Notice and consent` | 已检查私人计划适用范围与排除项，以及医院、医院门诊和 ASC 场景。正文“多数私人”“特定”“适用的 notice and consent”保留了适用边界，没有把签字说成一律有效或所有服务都能放弃保护。 |
| [CMS：不使用保险的权利](https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/know-your-rights/without-insurance)，账单争议段及多个提供者说明 | 本文按同一提供者或设施对比估算与账单；至少高 400 美元和收到初始账单后 120 天的触发点正确。保留“检查资格”，没有保证个案必获减免。 |
| [IRS：Financial Assistance Policy，§501(r)(4)](https://www.irs.gov/charities-non-profits/financial-assistance-policy-and-emergency-medical-care-policy-section-501r4)，`Financial assistance policy` 与 provider list 要求：`facility-by-facility basis`、`which providers are covered` | 501(c)(3) 医院组织的医院须有书面 FAP，资格、申请、适用服务及其他提供者清单均有原文支持；正文不声称每所医院一律采用同一援助门槛。 |
| [CMS：申请经济援助](https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/get-help/guides-resources/apply-financial-assistance)，`Ask for information`、`What happens after you apply`、其他选项：`pause collections` | 取政策与表格、查询缺件／时长／期间账单、催收时请求暂停及其他支付安排均有对应原文。稿件正确写成“请求”，并未声称提交申请自动暂停所有时限。 |

账单页虚构算例独立复算：`1,000 - 400 = 600`；`600 × 80% = 480`；`600 × 20% = 120`；`120 - 50 = 70`。正文明确教学虚构、网络内承保、免赔额已满足等条件，没有伪造真实 EOB。

## 未核实范围与后续触发

- 本次没有核实任何真实产品的具体网络、待遇、事前授权清单、医院 FAP 收入线、患者金额或个案申诉期限；稿件也没有声称这些已经核实。
- 未逐州核查州保险法、Medicaid hearing、地面救护车保护或医院援助细则。站内尚未形成这些专页时，正文保留了回到本人计划、通知和州机构的动作。
- 未读取任何真实患者资料，也未操作保险、医院或 CMS 投诉账号。入口可读不等于个案资格获得确认。
- SBC PDF 是旧期间教学样表，只支持字段说明。外部审查页面仍有截至 2026-10-02 的特定延长公告，本次查阅日已过该日期；正文没有把它写作现行开放窗口。内外审紧急时限的页面表述不同，正文只保留加急入口，没有拼接成一个未经核实的统一时长。
- 加入年度金额、具体州／保险产品、雇主 ERISA 细节或 Medicare／Medicaid 程序时，应重新独立回源。当前审阅不覆盖未来扩展，也不能只修改 `verified` 日期沿用结论。
- 正文发生任何修改后，必须重新计算正文 SHA；若改动涉及事实、行动或范围，应重新复核相关断言。该记录不授权跳过第三人静态审或主控工程验收。
