# 恢复断点

更新：2026-10-13，B04验收通过／本地提交前。目标active，全书未完成。

- Git main，无远端；已提交B01 c292949、B02 44d1094、B03 a81085f。Hugo0.166.0 Extended，OINK1.2.0固定f8f476e660cf053a2645b7b923ae8d08d5448fce。原始PROMPT保留；上级AGENTS不存在。
- 已集成18主题、12章、5部分。B04新增租房流程、医保衔接和跨州税務，已接入章节／四州／相关事项；三人审阅及最终正文SHA见 acceptance.json。不要使用旧草稿SHA。
- 最新53 HTML／18主题构建，32页面／18搜索／8交互通过；手机三表实看、89页PDF抽查第27、49、77页，详见b04-integration.md。public已同步157路径、大小、SHA。未外部发布。
- B05作者进行中：health地理生活regional-life、documents邀约文化invitations-boundaries、civic Tribal Nations tribal-nations。三篇分别在foundations下；主控拥有章导读与共享导航。root另写life/documents/address-changes，必须由documents事实审、civic第三人静态审；root不能自审。
- 地址稿尚未写文件；已实际读取USPS、USCIS改址／AR11／政策手册／保护案件路径、EOIR33、IRS、SSA及F1 I20第3页、J1报告段。缓存.cache/evidence/address-changes；失败的eCFR访问页与GovInfo找不到页不能当法规。学生和USCIS待办、EOIR必须分别交代。后续须把实际读源写入轻量证据。

下一步：本地提交B04，排除B05草稿。写完地址更新、安排三篇背景稿异人事实审，再第三人静态审、补章导读；地址审核完成后可建立搬家事项。构建渲染同步后逐批本地提交。生命周期、历史文化及多数领域仍有缺口，不以篇数宣称整书完成。

自建预览127.0.0.1:1317，scripts/serve_preview.py HTTP/1.1；恢复时查实际进程，不继承旧句柄。1318临时B04草稿服务器已关闭。所有缓存、截图、PDF、public均忽略。只关闭自己创建的浏览器或预览进程。细节见ENGINEERING与reviews。
