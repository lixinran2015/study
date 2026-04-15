# 附录：常见踩坑指南

> [← 上一章：第 5 章](./chapter-05-advanced.md) | [返回目录](./README.md) | [下一章：Prompt 速查表 →](./prompt-cheatsheet.md)

学习编程的路上，报错和卡住是常态。这个附录汇总了本教程读者最常遇到的问题，遇到问题可以先来这里查一查。

---

## 分类一：安装与环境类

### Claude Code 安装失败

**现象**：运行 `npm install -g @anthropic-ai/claude-code` 时报错

**原因 1：Node.js 版本低于 18**
- 解决：访问 [nodejs.org](https://nodejs.org) 下载安装最新版 LTS

**原因 2：权限不足（macOS/Linux 常见）**
- 解决：在命令前加 `sudo`，或使用 nvm 管理 Node 版本

**原因 3：网络被拦截**
- 解决：检查代理设置，或切换 npm 镜像源

### 终端里找不到 `claude` 命令

**现象**：安装成功了，但输入 `claude` 提示 "command not found"

**原因**：npm 全局安装的路径没有加到系统 Path 环境变量里

**解决**：
- **macOS/Linux**：检查 `~/.bashrc` 或 `~/.zshrc`，确保有 `export PATH="$PATH:$(npm config get prefix)/bin"`
- **Windows**：检查系统环境变量 Path 是否包含 npm 全局目录

### `python` 命令不存在

**现象**：终端里输入 `python` 提示找不到命令

**解决**：
- Windows 用户请使用 `py`
- macOS/Linux 用户请使用 `python3`
- 如果两个都没有，请访问 [python.org](https://python.org) 下载安装 Python 3

---

## 分类二：网络与模型类

### 连接国内模型后没有响应

**现象**：配置了 CLAUDE.md 里的国内模型，但 Claude Code 不回复或报错

**原因 1：`base_url` 填错了（末尾少了 `/v1` 或多了斜杠）**
- 解决：仔细核对服务商文档里的 API 地址

**原因 2：API Key 过期或未激活**
- 解决：重新生成 Key，或等待几分钟让 Key 生效

**原因 3：模型名称拼写错误**
- 解决：核对文档中准确的 model ID（如 `deepseek-chat` 而不是 `deepseek`）

### Claude Code 登录超时

**现象**：`claude login` 后浏览器打不开，或提示 timeout

**原因**：网络代理/防火墙拦截了 Anthropic 服务器

**解决**：检查系统代理设置，或配置国内模型后重试

---

## 分类三：运行与报错类

### HTML 文件打开是白板（空白页）

**现象**：双击 HTML 文件后，浏览器里什么都看不到

**原因 1：Vue CDN 加载失败（国内网络不稳定）**
- 解决：刷新几次，或尝试把 CDN 地址换成 `https://cdn.jsdelivr.net/npm/vue@3/dist/vue.global.js`

**原因 2：代码里有语法错误（比如标签没闭合、引号不匹配）**
- 解决：按 F12 打开 Console，把红色报错信息复制给 Claude Code

### Python 脚本提示 `ModuleNotFoundError`

**现象**：运行脚本时提示找不到某个模块（如 `requests`）

**原因**：使用了需要额外安装的第三方库

**解决**：本教程的示例优先使用 Python 标准库（如 `urllib`）。如果确实需要 `requests`，运行 `pip install requests` 安装

### 和风天气 API 返回错误码

**现象**：脚本运行后提示 "API 请求失败"

**原因 1：城市名包含特殊字符或错别字**
- 解决：检查输入，使用常见城市名（如"北京"而非"北京市"）

**原因 2：API Key 还没生效**
- 解决：和风天气免费 Key 有时需要等待 5-10 分钟

**原因 3：免费额度超限**
- 解决：查看控制台用量，或注册新账号

### localStorage 数据消失了

**现象**：刷新页面后，之前保存的记账记录不见了

**原因 1：浏览器开启了隐私/无痕模式**
- 解决：用普通模式打开 HTML 文件

**原因 2：手动清除了浏览器数据**

**原因 3：用不同方式打开了文件（如之前是 `file:///Users/...`，现在是 `file:///C:/...`），导致域名变化**
- 解决：尽量用同一种方式打开文件，或记住文件路径

---

## 分类四：与 AI 协作类

### Claude Code 给的代码跑不通

**解决步骤**：

1. 把完整的报错信息复制下来
2. 把报错信息和代码一起贴给 Claude Code
3. 明确说："这段代码运行时报了上面的错误，请帮我检查原因。"

### AI 改错了地方 / 没理解需求

**解决步骤**：

1. 不要只说"不对"，要指出具体哪里不对
2. 对比说明："我想要的是 XXX，但现在实现的是 YYY"
3. 给出更精确的修改指令

### Claude Code 把代码改乱了，想回到之前的状态

**解决**：如果你在用 Git（推荐），可以用以下命令查看改了什么、撤销修改：

```bash
git diff              # 查看修改内容
git checkout .        # 撤销所有未提交的修改（谨慎使用）
git log --oneline     # 查看历史提交
git checkout HEAD~1   # 回到上一个版本
```

💡 小提示：初学者不需要深入学 Git，但掌握 "撤销修改" 这个保命技能非常有用。

---

> [← 上一章：第 5 章](./chapter-05-advanced.md) | [返回目录](./README.md) | [下一章：Prompt 速查表 →](./prompt-cheatsheet.md)
