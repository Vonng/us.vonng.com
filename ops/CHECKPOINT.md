# 恢复断点

更新：2026-10-13，B02验收通过／本地提交前。目标active，全书未完成。

- Git main，无远端；B01提交c292949。Hugo0.166.0 Extended，OINK1.2.0固定f8f476e660cf053a2645b7b923ae8d08d5448fce。原始PROMPT保留。
- 已集成12主题：B01医疗3、文件号码2、加州押金1、政府／信用／应急3；B02隔离民权史、税务居民、服务英语。9章导读、5部分、事项／地区／术语入口均为真实内容。SHA和三参与者绑定见acceptance.json。
- B02最新生产构建40 HTML／12正式主题，零警告，内部链接／锚点／搜索／打印检查通过。首列6rem修正手机表格后58页面／12搜索完整回归通过，实际截图／55页PDF抽查见b02-integration.md。public已同步路径、大小、SHA；未外部发布。
- B03三篇仍written/draft true：驾驶证e3ca87c7f5c1d773710f596dc266f7031ecd62551a98e8a8c92b5758ccc9c74b（作者documents／事实审civic通过）；工资0b21289995a0c69432629ae8231032d132c2593cdf21c3ddf4db029b89f21c0a（civic／health通过）；学校f3525f1b4dd6a652bc53c1ca7dcb434bb1ff470092e8113e035fd1eaa97697a8（health／documents通过）。root已全文预读三稿，须重读事实审与修订后静态结论。
- root已写B03三章导读（transport/school/employment）及NY/WA/TX地区页，全为草稿，尚未正式展示。不要误当已集成。
- B04：documents租赁流程，health失业／搬家医疗衔接，civic四州税务资料；完成B03审阅后开工，详见TASKS。恢复检查实际文件与代理，不继承旧句柄。

下一步：本地提交B02已完成源文件（排除B03在写稿）；root第三人静态审B03三稿并集成主题／导读／地区／入学路径，按变更检查同步提交；继续B04。四州地方链与生命周期、历史文化及多数领域仍有缺口，不以篇数宣称整书完成。

自建预览为127.0.0.1:1317，scripts/serve_preview.py HTTP/1.1；旧HTTP/1.0服务器已关闭。恢复时查真实进程；结束只关闭本项目自己创建的进程。所有缓存、截图、PDF、public均忽略。细节见ENGINEERING、reviews与分项地图。
