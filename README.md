# 美利坚生活指南

面向中文读者的美国社会与生活参考书。唯一正文源在 `content/book/`；事项、地区、术语与阅读说明在 `content/docs/`。项目目标见 [PROMPT.md](PROMPT.md)，当前缺口与断点见 [ops/CHECKPOINT.md](ops/CHECKPOINT.md)。

使用 Hugo 0.166.0 Extended 和锁定版本的 OINK 1.2.0。

```sh
git submodule update --init
python3 -m pip install -r requirements-checks.txt
make check DESTINATION=.cache/production-review
make preview
```

正式主题必须经过异人事实审、第三人静态审与当前版本构建/渲染检查。详情见 [AGENTS.md](AGENTS.md) 和 [工程记录](ops/ENGINEERING.md)。普通本地工作已获授权；推送与发布另行授权。
