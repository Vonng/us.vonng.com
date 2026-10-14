# B-PL-R2-2 主控差分验收记录

2026-10-14，root。对象：R2-2 批次（日常生活，21 件）"说人话"第二轮语言校对差分；执行者 `B-PL-R2-2`。本记录是 root 的差分验收（acceptance.json 之 fact_record 指向此处），不是回源事实审——R2 规则明确语言修订不重跑事实审，root 只核红线与事实范围等同。

## 验收过程（实际执行）

- 基线核对：执行者动手前 21 件 body SHA 与 R2 账本逐件一致（执行者报告，root 复核账本行与新 SHA）。
- 机械红线检查（root 实跑脚本，对全部改动文件）：frontmatter 逐字节相同；正文链接多重集合（URL＋数量，位置移动除外）一致；表格行结构与加粗标记数不变。全部通过。
- root 逐 diff 通读全部改动（`git diff`，见下节），核对每处改写事实范围与原句等同。
- 独立第三静态审：`B-PL-R2-THIRD` 另行审阅同一差分包，记录 [b-pl-r2-2-third.md](b-pl-r2-2-third.md)，结论通过、无红线违规。
- 工程门禁：R2 六批并行派发，本批验收安装后即提交（提交树内 acceptance 条目与正文一致）。本批安装后实跑 `make check DESTINATION=.cache/production-review`，错误清单仅含并行批次在途文件（预期内），本批 3 件无失配。全书零错误零警告的最终 `make check`＋`make sync` 在全部批次收口后作为最终门禁实跑（见 R2 账本验收行与 CHECKPOINT）。

## 修订明细（2 件 processed，19 件 clean）

| 文件 | 处数 | 修订前 body SHA-256 | 修订后 body SHA-256 |
|---|---|---|---|
| `content/book/life/documents/entry-return.md` | 1 | `8293f92189a7e8c44708dde97aec1d266f82bd123a860ec0121ce3a9149efd42` | `e0ea3b76c8ebb055d40e4b3bfc50b56939a311bf7b719295b93a552b90a1a363` |
| `content/book/life/documents/status-documents.md` | 1 | `16e535093fd8b475a697b10581a6e99d920b8424a71d5d80929c786a924c4721` | `c2897386c6b55d8f4c86541492660f55fd035ec3b0a40e5a832e37b426c8093d` |

两处均甲类否定式处理，root 逐义核对：

1. entry-return："这是诉讼期间救济，不能写成永久撤销"→"这是诉讼期间救济，不是永久撤销"。删去面向写作者的"写成"措辞；法院命令为诉讼期间暂缓、非永久撤销的命题不变，行内日期（2026-09-15／09-14）与 64 条链接逐字未动。
2. status-documents："D/S 并不意味着无需管理毕业、项目终止或授权工作的日期"→"写 D/S 时仍要管理毕业、项目终止或授权工作的日期"。双重否定改等值正面陈述，条件与三个管理对象逐字保留；13 条链接一致。

其余 19 件零修订（clean）：执行者对存留否定式逐处写明保留理由（多为程序性防错真否定），乙类六项全批无必要修订对象；root 抽读 phone-internet、address-changes、buying-home 保留判定，同意。

## 边界

未回源任何外部 URL；未重跑事实审；root 未逐字复读 21 件全文（依赖首轮 verified 基线 f6170ac＋本轮差分审＋第三静态审）；frontmatter 未动，verified／reviewed_by 保持首轮值。
