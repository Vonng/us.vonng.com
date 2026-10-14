# B-PL-R2-1 主控差分验收记录

2026-10-14，root。对象：R2-1 批次（认识美国，16 件）"说人话"第二轮语言校对差分；执行者 `B-PL-R2-1`。本记录是 root 的差分验收（acceptance.json 之 fact_record 指向此处），不是回源事实审——R2 规则明确语言修订不重跑事实审，root 只核红线与事实范围等同。

## 验收过程（实际执行）

- 基线核对：执行者动手前 16 件 body SHA 与 R2 账本逐件一致（执行者报告，root 复核账本行与新 SHA）。
- 机械红线检查（root 实跑脚本，对全部改动文件）：frontmatter 逐字节相同；正文链接多重集合（URL＋数量，位置移动除外）一致；表格行结构（每行管道符数序列）与加粗标记数不变。全部通过。
- root 逐 diff 通读全部改动（`git diff`，见下节），核对每处改写事实范围与原句等同。
- 独立第三静态审：`B-PL-R2-THIRD` 另行审阅同一差分包，记录 [b-pl-r2-1-third.md](b-pl-r2-1-third.md)，结论通过、无红线违规。
- 工程门禁：R2 六批并行派发，本批验收安装后即提交（提交树内 acceptance 条目与正文一致）。本批安装后实跑 `make check DESTINATION=.cache/production-review`，错误清单仅含并行批次在途文件（预期内），本批 3 件无失配。全书零错误零警告的最终 `make check`＋`make sync` 在全部批次收口后作为最终门禁实跑（见 R2 账本验收行与 CHECKPOINT）。python 依赖：首轮用 `.cache/checks-venv`（缓存已清理），本轮 bs4 装入当前 python3 环境（~/dev/.venv），PyYAML 原有。

## 修订明细（1 件 processed，15 件 clean）

| 文件 | 处数 | 修订前 body SHA-256 | 修订后 body SHA-256 |
|---|---|---|---|
| `content/book/foundations/culture/invitations-boundaries.md` | 1 | `56a9c74590f03b0447e5e46859b3ed18efcd44f2cfb1e62e2b1d77966d0297d1` | `b9f0e449db9e1128a7fb39345beb462079cc089a0e617acb40779c06f060abe8` |

唯一一处：整句删除"教学资料把说话者关系和任务类型放在一起分析，而不是规定所有邀请只能用一种句型。"（替引用来源辩护的元叙述，读者无从使用），引用链接 [Relationship between Speakers and Task Type，第 1—2、12 页] 移挂前句句末。root 核对：全文链接 8 条前后一致（5 外＋3 内）；删除不损失事实；与 R2 提示词判定示例 1 预审改法一致。

其余 15 件零修订（clean）：执行者对甲类命中（tribal-nations 9 处、public-participation 约 30 处等）逐处过判定并写明保留理由（均承载真范围／防错信息），root 抽读 tribal-nations、regional-life、public-participation 三件原句，同意全部保留判定。

## 边界

未回源任何外部 URL；未重跑事实审；root 未逐字复读 16 件全文（依赖首轮 verified 基线 f6170ac＋本轮差分审＋第三静态审）；frontmatter 未动，verified／reviewed_by 保持首轮值。
