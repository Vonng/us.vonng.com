# B05 邀约文化：独立事实与英语语用审

审阅人：`/root/health`。作者：`/root/documents`。实际审阅日期：2026-10-13。

结论：**PASS**。未发现须返修的事实、研究外推或英语表达问题。本文可以进入第三人静态审；此结论不代表构建、渲染或正式集成通过。

- 路径：`content/book/foundations/culture/invitations-boundaries.md`
- 正文 SHA-256：`0307996d17b75c6d7eed21c999ed8d67e2e995e2325ea9546ccfc0ea4ba309a6`
- 计算方法：`sha256(text.split('---', 2)[2].encode('utf-8'))`。审阅开始及记录落盘时从实际文件计算；只绑定第二个 YAML 分隔符之后的正文。
- 审阅范围：全文、两段完整原创对话、表格及散布例句；作者地图与事实链已读，仅用于定位问题。下列一手资料均由本审阅者独立打开并读到相应原文。

## 独立回源

| 来源 | 本次实际读取、判断与适用边界 |
|---|---|
| [American English: Simple Ways to Incorporate Pragmatics in the EFL Classroom](https://americanenglish.state.gov/resources/teachers-corner-simple-ways-incorporate-pragmatics-efl-classroom) | `web.open` 成功，实读 What is pragmatics / Understanding Pragmatics / Teaching Pragmatics / 教学活动与 Conclusion，尤其正文行 30—41、51—57、68—77。原文明确同一语言群体中的情境、说话关系与意图差异。稿件用来解释语用，未把未具名 host country 习俗移植成美国规定，也未照搬年龄问题的泛化判断 |
| [Everyday Conversations 资源说明](https://americanenglish.state.gov/resources/everyday-conversations-learning-american-english) 及 [教材 PDF](https://americanenglish.state.gov/files/ae/resource_files/b_dialogues_everyday_conversations_english_lo_0.pdf) | 资源页 `web.open` 实读 intended sixth-/seventh-grade EFL/ESL 与目录；PDF `web.open` 因 20,402,562 字节超限失败，同日普通 HTTPS `urllib.request.urlopen` 得到 200，TLS 校验开启，内存 BytesIO + pypdf 成功。独立读 PDF 物理第 6—9 页（印刷 4—7），Dialogue 1-1、1-2 与全部对应 language notes：简短正式／非正式问候；See you later 可作 goodbye。没有读完整 72 页，也无此必要。稿件没有复制教材整段对话，没有把教材的握手时长等建议推广全国 |
| [Biesenbach-Lucas: Relationship between Speakers and Task Type](https://americanenglish.state.gov/files/ae/resource_files/biesenbach_0.pdf) | `web.open` PDF 13 页可读，独立读物理／印刷第 1—4、12 页。第 1—2 页提出 interlocutor relationship 与 task type；第 12 页 Invitations 网格列 do you want / would you like 等示例。支持稿件按关系和活动选句型，不形成全国唯一礼节。正文引第 1—2、12 页定位正确 |
| [Epley & Schroeder 原研究作者入口](https://julianaschroeder.com/publications/mistakenly-seeking-solitude) → [原始论文 PDF](https://juliana-schroeder-dev.squarespace.com/s/mistakenly-seeking-solitude.pdf) | 作者页面 `web.open` 成功，从真实 link 20 点击 PDF 成功；页面本身 2018 上架，论文封面明载 Online First 2014-07-14，稿件写 2014 发表正确。独立读摘要、Overview、Experiments 1a/1b 招募与方法、结果和 Discussion（物理页 2—6／正文 1—5）。1a 招募 Homewood, Illinois Metra 往芝加哥的单独通勤者，随机分 connection / solitude / control，结局是自报体验；1b 是另组预测。连接组比独处组体验更积极、预测方向相反，稿件没有把对 control 的不显著比较混写为结论。通过普通 HTTPS 在内存另读物理第 17—18 页，重点正文第 17 页 Qualifications：不证明所有陌生互动愉快，未测试特别长或反复的互动。稿件明确留有这些边界，没有推断所有陌生人都欢迎搭话、没有人数比例或人格因果外推。未声称完整复核九个实验 |
| [University of Iowa Housing: Styles of Communication](https://housing.uiowa.edu/styles-communication-0) | `web.open` 成功，独立读主体各 style 及 I-statements，行 50—84。I-statements 指具体感受、事件、想法和需要；assertive communication 不能保证总得到所求。稿件准确归为该校住宿学生沟通指南和可练习的方法，没有把它当全国调查或法律规则 |

研究论文的实际文件由原 URL 转向 `static1.squarespace.com` 托管，内容与作者页面链接相符。未存大原件、未通过搜索摘要代替阅读、未采用未读来源补空。

## 英语与场景核验

逐句核查语法、语义和对话衔接：

- small talk 的开场、接对方已提话题、简短真实回应和自然结束均可用；没有将 How are you 固定成只能答 Fine，也没有把 See you later 当明确约定。
- Maya／Lin 咖啡对话由 sometime 逐步形成 Sunday / ten / café 及一小时时长，答复顺序一致；maybe / I’ll let you know 保持未确认，不会误导读者先付不可退费用。
- 拒绝表中 pass、can’t make it、get back to you、join for dinner / leave by eight、取消与提出另一天的意思匹配中文。替代方案仅在真正想改约时使用；被拒绝后的回应不给对方增加解释义务。
- 到达／开饭、开放时段、入口、Pacific time、迟到、增加同伴与饮食表达均自然可理解；没有统一社交迟到分钟数或全美分账默认规则。
- 隐私例句语气从温和选择到明确边界，符合表内目的；身体接触和照片发布被标成协商，非法律许可结论。Where are you really from 的语用说明针对重新否定对方已给的回答，不推断所有人动机。
- Sam 临时来访短信里的重复拒绝和可选公园替代方案自然衔接；没有把社交边界当租约访客权利或住房强制执行。误解修复、结束反复施压和危险分流有实际出口。

全页例句与两段对话已明确教学虚构；不使用真实个人资料。无法从这些教学材料确认任何地区、世代、族群或宗教的普遍偏好，稿件没有作这种归纳。说法属于可用表达，非保证对方接受的技术。

## 未核范围与交接

没有新增调查代表性、当代全国社交行为比例、法律隐私权、劳动骚扰要件、租客访客权利或照片发布许可结论；这些并非本稿实际承诺的内容。未逐一验证与本文无关的教材章节、研究全部九个实验、各大学完整住宿政策；本次也未运行构建或渲染。

未请求作者修改，未改作者正文、frontmatter、地图、证据或共享账。全文最终 SHA 与收到冻结版本相同。任何后续正文变更都需按差异复核并重新绑定；新增群体归纳、研究百分比或法律结论时应补新的实际一手证据。
