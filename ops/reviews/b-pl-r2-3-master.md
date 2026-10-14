# B-PL-R2-3 主控差分验收记录

2026-10-14，root。对象：R2-3 批次（人生与健康，25 件）"说人话"第二轮语言校对差分；执行者 `B-PL-R2-3`。本记录是 root 的差分验收（acceptance.json 之 fact_record 指向此处），不是回源事实审——R2 规则明确语言修订不重跑事实审，root 只核红线与事实范围等同。

## 验收过程（实际执行）

- 基线核对：执行者动手前 25 件 body SHA 与 R2 账本逐件一致（执行者报告，root 复核账本行与新 SHA）。
- 机械红线检查（root 实跑脚本，对改动文件）：frontmatter 逐字节相同；链接多重集合一致（69 条）；表格行结构与加粗标记数不变。全部通过。
- root 逐 diff 通读改动（见下节），核对事实范围等同。
- 独立第三静态审：`B-PL-R2-THIRD` 另行审阅差分，记录 [b-pl-r2-3-third.md](b-pl-r2-3-third.md)，结论通过、无红线违规。
- 工程门禁：本批修订并入最终门禁——全部批次收口后实跑 `make check DESTINATION=.cache/production-review`（Hugo 零警告＋check_site 全绿）后 `make sync`；见 R2 账本验收行。

## 修订明细（1 件 processed，24 件 clean）

| 文件 | 处数 | 修订前 body SHA-256 | 修订后 body SHA-256 |
|---|---|---|---|
| `content/book/people/accessibility/mental-health.md` | 1 | `8b52a308ae7a27c57845818ad47800d86a0d89ce89123797893c8eaac45f05d4` | `4b81f5793c311b5ef5d933ccf2423c825464bc9050dd7d541a57acaa206c384e` |

唯一一处（甲类，即 R2 提示词判定示例 2 的预审改法）："其其他语言口译通过电话提供，不能据此期待中文短信服务"→"其他语言（含中文）的口译只经电话提供；短信服务不含中文口译"。root 核对：两句对读者的指引一致（中文口译仅经 988 电话、短信不含中文口译）；顺带消除原文"其其"叠字笔误；链接 69 条前后一致；行内 988／Mandarin／Cantonese／711 逐字未动。

其余 24 件零修订（clean）：执行者对存留否定式逐处写明保留理由（accommodations、advance-planning、coverage-changes、insurance-costs、medical-bills、school-support 等页均为程序性真否定或法定口径），root 抽读 accommodations、insurance-costs 两页保留判定，同意。

## 边界

未回源任何外部 URL（988lifeline.org 措辞以句上来源为准）；未重跑事实审；root 未逐字复读 25 件全文（依赖首轮 verified 基线＋本轮差分审＋第三静态审）；frontmatter 未动，verified／reviewed_by 保持首轮值。记账时序说明：本批账本 processed 行随 45f1580 先行入库，正文改动在本批验收提交中入库，最终状态一致。
