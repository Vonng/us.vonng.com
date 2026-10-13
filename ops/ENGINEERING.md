# 工程基线与验证

更新：2026-10-13。项目首次独立初始化；目标 `https://us.vonng.com/`，仅本地构建，未发布。

## 锁定版本

- 本机 `hugo v0.166.0+extended+withdeploy darwin/arm64`，Homebrew，实际命令 `hugo version`。
- OINK 1.2.0，以 Git 子模块 `themes/oink` 固定 `f8f476e660cf053a2645b7b923ae8d08d5448fce`。来源 [OINK 仓库](https://github.com/pgsty/oink)，实际查阅 [官方站](https://oink.pgsty.com/) 与此提交本地模板；未使用 latest 浮动版本。
- Python 检查依赖见 requirements-checks.txt。浏览器辅助使用 `.cache/browser` 中的 Playwright 1.64.0 与本机 Google Chrome，隔离临时 profile，不使用个人资料目录。
- 中文、America/New_York 时区；页面具体事件时间须标明当地时区。没有继承加拿大统计 ID、远端仓库或托管身份。

## 有选择的参考

从加拿大项目仅复用并审读：`editorial-meta.html`、after-header hook、Book print 元数据与链接转换、offline search 排除隐藏页的模板。没有复制正文、ops 历史、证据、配置服务身份或 Git 历史。递归目录重新简化；首页为 OINK hero 加少量元数据读取卡片，插画 `static/images/neighborhood.svg` 为项目原创矢量示意，非真实城市地图。

保留 `sidebar_menu_compact: false` 与 `sidebar_menu_foldable: true`，非当前章节叶子保留在 DOM，由展开控制显示。

## 命令

```sh
git submodule update --init
python3 -m pip install -r requirements-checks.txt
make check DESTINATION=.cache/production-review
make check-drafts
npm install --prefix .cache/browser --no-audit --no-fund playwright@1.64.0
make preview
# 另一个终端，在 127.0.0.1:1317 当前构建上运行
make browser
# 渲染及事实/静态审通过后
make sync
```

`make check` 在生产模式以 warning 为错误，检查全站已生成 HTML 的本地 href/src 与锚点、主题元数据、正文唯一 ID、中文加粗、搜索及打印覆盖、正文审核摘要与三名不同参与者。外链不由该命令测试。

`make check-drafts` 在 `.cache/draft-fixture/` 隔离源树里实测：Hugo draft 从 HTML/搜索/打印排除；隐藏页仍有直接页面，但从目录/搜索/打印排除；单独 `status: written` 仍会输出，所以项目检查器补上编辑状态门禁。已于 2026-10-13 实际运行通过。

`make sync` 只允许固定项目内 `.cache/production-review` → `public`，拒绝软链接目的地；核对所有路径、大小和 SHA-256。同步允许清理仅在本项目 public 中存在的旧构建文件；不碰源文件与加拿大项目。

## 当前验证

- 初始工程骨架 Hugo 生产构建：零警告通过，尚非正文集成结论。
- 草稿/隐藏/状态隔离实验：通过。
- B01 九主题正式生产构建、34页面浏览器检查、6搜索与主要交互通过，实际截图与38页PDF抽查通过；同步116路径SHA一致。详细范围见 [B01集成验收](reviews/b01-integration.md)。
- 本地预览由本会话启动端口 1317；结束时关闭所属进程。截图、PDF 和测试原始 JSON 仅存 `.cache/`。

## 模板预览（不代表正式集成）

2026-10-13 在 `.cache/author-preview` 中含草稿构建，通过自己创建的 1318 服务和临时 Chrome 检查首页、医疗账单、地区入口，1440/390px 共六个页面 DOM 无横向溢出、单个正文 H1。实际查看了桌面首页与手机账单截图，标题、范围框和中文 strong 正常；完整正式版本仍待后续验收。截图仅在 `.cache/render/draft-*`。

## 本地预览与异步验收修正

初次使用 Python 默认 HTTP/1.0 服务，Chrome 多个全新 context 的首页图标偶发 `ERR_SOCKET_NOT_CONNECTED`，六次独立复现实验中一次失败；HTTP 200 与SVG本体有效不能代替失败请求。改用同一目录的线程HTTP/1.1本地服务器后，六次图标实验和完整浏览器回归均通过。未改站点SVG或伪造重试成功。

剪贴板写入等实际完成反馈后读取；搜索等待查询结果、退出动画和真实不同地址跳转；深色截图等待有限动画完成后取图。早期失败运行保留为调试过程，不计通过。浏览器记录本地请求失败，忽略导航自身中止请求；使用隔离Chrome上下文，不接触个人账户。

## B02 增量

三篇和三章导读、报税准备入口集成后，40 HTML／12正式主题生产构建零警告。新表格首列设6rem最小宽度，避免手机短标签竖排。共享样式变化后完整58页面／12搜索回归通过；实际查看新主题和表格，55页PDF抽看第37、43页。一次中间浏览器退出未计通过，原因未确定；桌面／手机改各自新进程后完整通过。详见 reviews/b02-integration.md。

## B03 增量

50 HTML／15正式主题，新增入学事项及四州地区入口。实际手机工资表出现16.90被挤断，右对齐数字单元格设不换行、对应表头最小宽度6rem；正文和事实审SHA不变。新增`US_REVIEW_CONFIG`可传JSON路径/搜索范围，默认行为保留。共享样式变化后78页面／18搜索回归通过；地区页随后去重，追加2端检查。72页打印稿实际抽查第42、54页。151路径同步核对一致；详见reviews/b03-integration.md。
