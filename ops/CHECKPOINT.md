# 恢复断点

更新：2026-10-13，B03验收通过／本地提交前。目标active，全书未完成。

- Git main，无远端；已提交B01 c292949、B02 44d1094。Hugo0.166.0 Extended，OINK1.2.0固定f8f476e660cf053a2645b7b923ae8d08d5448fce。原始PROMPT保留；上级`/Users/vonng/www/AGENTS.md`本次复查不存在。
- 已集成15主题，12章导读、5部分。B03新增四州驾驶证、工资／加班、公校入学；四州地区及入学事项已接入。最终SHA和三参与者绑定见acceptance.json，不用旧草稿SHA。
- 最新生产构建50 HTML／15正式主题，零警告，内部链接／锚点／搜索／打印检查通过。手机数字列修正后78页面／18搜索回归通过；地区页去重后2端增量检查及实看通过。72页PDF抽查第42、54页，详见b03-integration.md。public已同步151路径、大小、SHA；未外部发布。
- B04均保持草稿：租赁流程documents作者，已冻结375e0d1e24757938aa1acfd71d97a51ee3f37c004f82df1925c88d03839ad3f3，交health事实审；医保衔接health作者，已冻结1d44122b3a07b356bea7d94dee233430874512f917955dac32b373c8d1aaeaae，交civic事实审；四州税务civic作者，已冻结05d12b94c07756df34d5539d10f0292d898a6796808b11088a0337ac8a24a382，交documents事实审。root已全文预读租房和医保，最终修订后仍需第三人静态结论。
- B05三篇全国背景已排队：health地理生活比较、documents邀约文化、civic Tribal Nations；先收口各自B04写作／审阅，再开工，文件边界见TASKS。

下一步：本地提交B03已完成源文件，排除B04草稿；接收B04事实审，root静态审、补相关章节／四州／搬家路径，构建渲染同步提交；继续B05。生命周期、历史文化及多数领域仍有缺口，不以篇数宣称整书完成。

自建预览127.0.0.1:1317，scripts/serve_preview.py HTTP/1.1；恢复时查实际进程，不继承旧句柄。所有缓存、截图、PDF、public均忽略。浏览器只使用本会话隔离实例；结束只关自己创建的进程。细节见ENGINEERING与reviews。
