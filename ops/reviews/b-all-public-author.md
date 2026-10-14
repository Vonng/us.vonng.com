# 公共入口八处语言与行动修订：作者冻结

作者root；日期2026-10-14（Asia/Shanghai）。依据已实际完整读取的 `ops/reviews/b-all-public-language.md` 203行，只实施其P01—P08拟稿；八个canonical尚未改动，独立事实审、第三静态和主控工程待办。

root实际全文读取八个旧件与八个拟稿，各222行；单处替换及全部上下文已读。生成前从当前文件独算旧body／whole，与公共只读表一致；生成后逐件复算四摘要、准确位置逆验、frontmatter、数字和全部普通链接序列均一致。旧件与canonical逐字相等，不把旧全书78页的主控摘要核对表述为主控全读78个源文件。

冻结manifest `.cache/b-all-public-proposals/manifest.json` SHA `94e575d3ca6754ab471a879d741aca0797174330b7a40a261da18a91b822eb08`。每件实际缓存路径在manifest的original_file／proposed_file；original与proposed均按canonical的完整相对路径放置。

## 八处实际修订

| 编号 | canonical路径 | 原位置与修改目的 |
|---|---|---|
| P01 | `content/book/foundations/culture/_index.md` | L15只删全国性格比较旁白，关系／眼前安排和虚构例句入口仍在。 |
| P02 | `content/book/people/_index.md` | L16只删对家庭学校照护的泛指，医疗分担／预约／账单及各家庭入口保留。 |
| P03 | `content/book/work/employment/_index.md` | L19只删兜底句，L21实际工作关系、适用资格、雇主／州收入／工伤／EEO分别受理仍在。 |
| P04 | `content/book/people/education/_index.md` | L17把“继续顾问计划”改成与顾问确认学习计划，再注册、付款并开始上课。 |
| P05 | `content/docs/routes/food-cash-support.md` | L26只删食品申请对全部生活支持的比较，UI、医保、债务、住房服务及账单分流保留。 |
| P06 | `content/docs/routes/_index.md` | L34把“工作资格”改为“相应项目资格”，不删除实际经营／入职处的工作授权。 |
| P07 | `content/docs/routes/caregiving.md` | L28把“工作资格”改为“相应休假或收入支持资格”；家庭关系、雇主通知、收件和分别确认记录不变。 |
| P08 | `content/docs/routes/medical-care.md` | L21改为核账单／已付记录，保险使用者对EOB、未用保险者对书面估算；未齐资料联系相应机构并继续核付款／申诉期限。 |

## 主控实际读取的依据与边界

root真正全文读当前 `content/book/people/health/medical-bills.md` 1—35／36—71；L36处理未收到理赔或信息未齐，L43明确电话不自动暂停付款或申诉期限，L63说明未使用保险的书面估算路径。又实际读people拟稿L36—45；新增收费账务部门释义不改变L43。P08不增加具体期限或争议资格，不把普通计划性服务估算要求扩到急救，也不以书面估算保证争议受理。

root真正读当前 `content/book/work/employment/workplace-rights.md` L13—33：实际工作关系、雇员范围、人数门槛和雇主请求／州收入支持分别办理是P06／P07的源内依据；本轮root未重新全读该专题所有法律和州项目来源。P04承接继续学习正文已有顾问、学习计划及注册路径，没有新增统一校规或费用。

root另在2026-10-14实际打开并读以下一级页面；这是作者有界回源，不代替独立事实审：

| 普通一级链接 | 实际读到的范围与用途 |
|---|---|
| [CMS：未使用保险时的账单权利](https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/know-your-rights/without-insurance) | web主文L683—803；页标最后修改2026-10-05。未使用／没有保险对象，计划性估算及急救例外、收到后与账单比较，以及争议有起算和期限，支持P08分流和继续检查期限。未跟读PDF或实际启动程序。 |
| [HealthCare.gov：内部申诉](https://www.healthcare.gov/appeal-insurance-company-decision/internal-appeals/) | web当前60行全读，重点L18—37、48—55；拒赔通知后的起算、EOB和通话记录、书面结果属于相应保险申诉。P08未把这里的期限套到所有保障或付款安排。 |

DOL“how-to-talk-to-your-employer-about-leave”本轮web实际返回Internal Error，没有读到主文，不计成功来源；P06／P07独立事实审须自行实际核采用依据。首次合并输出曾截掉部分CMS尾段和HealthCare文本，root随后从保存的真实web返回按L764起完整显示CMS尾段及HealthCare60行，才登记上述实际读取范围；未以未显示内容当阅读。一次类型诊断误对返回字符串打印Object.keys产生无用截断输出，不支持任何结论。

## 八件原／拟冻结摘要

四列依次是original_body、original_whole、proposed_body、proposed_whole；body保留 `split('---',2)[2]` 的前导换行。

| 编号／路径 | old body | old whole | new body | new whole |
|---|---|---|---|---|
| P01 `content/book/foundations/culture/_index.md` | `3ade9ec9a7d42d100d985cac545ee4fd5ef8b1c951413a59472451ca867b6f8c` | `467d3f8ee977b45c0b9e26d6ffc6bea3ba65a838e7575c2ace0ee9f79c9fe145` | `5827b88118e4662af086d90ded49260fbe9fba134c47fb9ec7288db29cb8010a` | `4853a89546fff6e95699af7fbd9d002b8b6a8562ec4e49d818ed31c50a6803fd` |
| P02 `content/book/people/_index.md` | `681ba7a18dc62f311a105c9ab57863c318046b75486f1cb06e473f42810d07b1` | `a425ed92bc512a5ea368594e2e3e96fe2364a351b54f214110a4da5fa94f9ae8` | `ace9996fed0d24364dbed3d085502f82c44d088bc15547e80e5fe2b5898ed578` | `51bbe41829b53ee62540553029be6a13e1ba48a152f8b5c3638c0fac89664e34` |
| P03 `content/book/work/employment/_index.md` | `2d203079ebaadfc913a1f9e02298114b9383028343ef638c826a0f4f76e75909` | `7a6a5967899f196775c5999e3e0aa62a7183c1cea5507bdf74b0dfb7b677bce3` | `c507ff0c4bc22aa517f86c67bb00f7097ff378b711b80740e2c9a05a1bbf73ec` | `6b4a22db250628a257d90f23644d359896d803332072d31594e91f5edb1fe81a` |
| P04 `content/book/people/education/_index.md` | `2c5f5a5cebac1e616aed06065a910c8824a5f6bf2179b8796dbe268ec81f4625` | `ced47e0de84b34b9673369773659b78ea4336c57e8873141ba6e3d7695c89b0e` | `35115b431893661bff624459203da0f5156937a9fdd200e76238fed10ac85b63` | `8bf6a2e9bd26c670f6eaa796c67e06e434124635890adeaafdca39558531ffc2` |
| P05 `content/docs/routes/food-cash-support.md` | `7350135258949000e78a9d97bc15bd5865fea6a5527e0e7b95adf3e74b59a415` | `88ce98b0539e7b3ccaaf7cac799f805bbec7fef8f1191cb5fa203fba637d7302` | `bc2f2d2bbf0b8cb4d774b8e68a90f14ea97c22b9a281bb1d6dcbcb4f54b32bc7` | `23beebd7fd83baacc3f764c8b3561f9e6ad579549f424c88ab31d1b0e903e001` |
| P06 `content/docs/routes/_index.md` | `6fffc57d86d0be4cc426dcb6a708d932965034e748382303fed7d09f7d544d91` | `6ebfaba6090a162c412d3e4fc0a662a55be11d6fe1d34537cb685d142a9a4b08` | `17dcf23a991587046903c91b5a5823807bbe32dccc76e1d4da142f0fe9e43c98` | `84eb7144a7ccde4431dac88d03eff0717edf983ee89a4094a87bbd802b4d4e14` |
| P07 `content/docs/routes/caregiving.md` | `41f62afcb8520649bd438b802d9b0da97f91ce312e71e59946c7c2cd3037998c` | `33cef9f9c26438a18cc719d8ddb7a106ce8942a1ac93c01068a1599f21e74c98` | `365a82ad91c0d15642c33d9f2a41b83e0214f9a19763a89875bf2bce88cbff26` | `33185ceff6a8898fa661c739c273e152efa8d8581ab87d892f6542828ba34420` |
| P08 `content/docs/routes/medical-care.md` | `185b18d96404cc4c262d3e117ac873718fc98c307423fd487a74b968ae1411d4` | `43988a8533c57c176a15d845edf35404390a7b0675dc74a5cc28b9ee6c679924` | `18c8cdc3ff5292ae6b36db66570fd4beb0843dadfec63eb0970224011d877a1c` | `dda4b27ac397eb4fad97537763a54fba3a482c4edca2f37a62c12dd9ffcb8545` |

未核个人保险／项目资格、金额、机构付款或实际服务开始；70件无建议入口不因此自动登记语言或工程通过。作者root、独立FACT与第三审必须异人；拟稿若有必要修改，重新冻结新摘要后再审。
