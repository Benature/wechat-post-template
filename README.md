# 微信公众号推送模板 Wechat Post Template

微信公众号推送 Markdown 转 HTML (markdown2html)

- 支持自定义样式，如 `h1`, `img` 等
- 运行结束后自动复制 HTML 格式到剪贴板

依赖：
- `pandoc`
- `sqlite3`
- 图床：[SM.MS](https://doc.sm.ms/#api-Image-Upload)

## 使用 Usage

```shell
# config.py
Authorization = "xxxxx" # SM.MS API Key
```


```shell
python main.py "path/to/post.md"
```

html 文件会创建在和 md 同级目录下。打开 html 文件后，复制全文，黏贴到公众号平台即可。