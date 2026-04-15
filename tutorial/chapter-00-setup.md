# 第 0 章：准备工作

> [← 返回目录](./README.md) | [下一章：第 1 章 →](./chapter-01-mood-card.md)

欢迎来到 Claude Code 初学者教程！在这一章里，我们要做的只有一件事：**把 Claude Code 跑通，建立最小可用的开发环境**。不需要任何编程基础，跟着步骤一步步来就好。

---

## 1. 安装 Claude Code

Claude Code 是一个命令行工具，我们需要先把它装到电脑上。安装方式很简单，不管你用的是 macOS、Windows 还是 Linux，命令都一样（前提是已经安装了 Node.js）。

### 安装前检查：Node.js 18+

Claude Code 需要 Node.js 18 或更高版本。在终端里输入下面这条命令，看看你的 Node 版本：

```bash
node --version
```

如果显示的数字大于等于 `v18.0.0`，就可以继续安装了。如果提示找不到命令，或者版本低于 18，请先访问 [nodejs.org](https://nodejs.org) 下载并安装最新版。

### 各平台安装命令

**macOS：**

```bash
npm install -g @anthropic-ai/claude-code
```

**Windows（PowerShell）：**

```powershell
npm install -g @anthropic-ai/claude-code
```

**Linux：**

```bash
npm install -g @anthropic-ai/claude-code
```

💡 小提示：`-g` 表示"全局安装"，装完之后，你在电脑的任何目录里都能使用 `claude` 这个命令。

### 验证安装

安装完成后，输入以下命令确认是否成功：

```bash
claude --version
```

如果看到类似 `claude 1.2.3` 的版本号，恭喜你，安装成功！

---

## 2. 注册与登录

安装完成后，第一次使用需要登录你的 Anthropic 账号。在终端中运行：

```bash
claude login
```

这时会自动打开你的浏览器，跳转到 Anthropic 的登录页面。按页面提示完成登录后，回到终端，你应该会看到"登录成功"的提示。

💡 小提示：如果浏览器没有自动打开，终端里通常会显示一个网址，你可以手动复制到浏览器里访问。

---

## 3. 连接国内模型

对于国内用户，直接连接 Anthropic 官方服务器有时会遇到网络不稳定或成本较高的问题。好消息是：**Claude Code 支持通过配置文件连接其他兼容 OpenAI API 格式的模型**，比如 DeepSeek、通义千问等国产大模型。

### 配置方式

你可以通过项目根目录下的 `CLAUDE.md` 文件，或者系统的环境变量来设置自定义的 Base URL 和模型名称。

### `CLAUDE.md` 配置示例

在你的项目文件夹里创建一个名为 `CLAUDE.md` 的文件，内容如下：

```markdown
---
model: deepseek-chat
base_url: https://api.deepseek.com/v1
api_key_name: DEEPSEEK_API_KEY
---

本项目使用 DeepSeek 模型。
```

如果你想用通义千问，可以这样写：

```markdown
---
model: qwen-max
base_url: https://dashscope.aliyuncs.com/compatible-mode/v1
api_key_name: DASHSCOPE_API_KEY
---

本项目使用通义千问模型。
```

💡 小提示：`api_key_name` 是指你放在"环境变量"里的密钥名称。请先在终端用 `export DEEPSEEK_API_KEY=你的密钥`（macOS/Linux）或 `$env:DEEPSEEK_API_KEY="你的密钥"`（Windows PowerShell）设置好，再运行 `claude`。

---

## 4. 为什么要有 CLAUDE.md

`CLAUDE.md` 是放在项目根目录下的一个特殊文件。你可以把它理解为：**给 Claude Code 的"系统提示词"和"项目记忆"**。

每次你在这个项目里和 Claude Code 对话时，它都会先读一读这个文件，了解你定的规矩。这就像是新员工入职时拿到的一本"员工手册"。

### 什么时候需要写 CLAUDE.md？

- **项目规范**：代码风格、文件命名规则、技术栈要求
- **常用命令**：项目里经常要跑的脚本或测试命令
- **个人偏好**：比如"请用中文回复"、"代码注释用中文"
- **模型配置**：自定义 Base URL、模型名称、API 密钥等

### 基础写法示例

`CLAUDE.md` 的顶部是 YAML Frontmatter（用三条横线包起来的配置区），下面就是普通的 Markdown 内容：

```markdown
---
model: deepseek-chat
---

## 项目规则

1. 所有回复请使用中文。
2. 代码注释请使用中文。
3. 优先使用简洁的写法。
```

### 实战小练习

请你现在就在项目文件夹里创建一个 `CLAUDE.md`，写下这条规则：

```markdown
---
---

请用中文回复我的所有问题，并且在代码注释中也使用中文。
```

保存后，下次运行 `claude` 时，它就会记住这个要求了。

---

## 5. 验证配置是否生效

配置好后，我们来验证一下。在终端运行：

```bash
claude
```

进入对话界面后，你可以直接问它：

```
你好，能自我介绍一下吗？
```

如果 Claude Code 用中文回复你，说明 `CLAUDE.md` 里的规则已经生效了。

另外，你也可以通过以下命令查看当前配置：

```bash
claude config list
```

这会让你看到当前生效的设置项，方便排查问题。

---

## 6. 认识终端/命令行

既然我们要用 Claude Code，就免不了和"终端"（也叫"命令行"）打交道。别担心，你只需要掌握几个最基础的指令就够了。

### 什么是终端？

终端（Terminal）就是一个**用键盘输入命令来操控电脑的界面**。我们平时用鼠标点击图标打开软件，而在终端里，我们用文字命令告诉电脑"我要做什么"。

### 常用基础命令

**切换目录** —— `cd`

```bash
cd 文件夹名称
```

比如进入桌面：

```bash
cd Desktop
```

返回上一级：

```bash
cd ..
```

**查看当前目录里的文件**

macOS / Linux：

```bash
ls
```

Windows：

```cmd
dir
```

**运行 Python 程序**

macOS / Linux：

```bash
python3 hello.py
```

Windows：

```cmd
py hello.py
```

**打开 HTML 文件**

最简单的方式就是找到那个 HTML 文件，用鼠标**双击**它，系统会自动用浏览器打开。不需要命令行也能做到。

### 如何查看报错信息

在终端里运行命令时，如果出错了，通常会看到红色的文字或者带有 `Error` 字样的提示。**不要慌，把这些文字完整复制下来**，去问 Claude Code 或者搜索引擎，大多数时候都能找到解决办法。

💡 小提示：报错信息是程序员最好的朋友。它不是在骂你，而是在告诉你"问题出在哪里"。

---

## 7. 本章小结

到这里，我们已经完成了：

- 安装并验证了 Claude Code
- 完成了登录授权
- 了解了如何通过 `CLAUDE.md` 连接国内模型和设置个人偏好
- 学会了几句最基础的终端命令

你的"最小可用开发环境"已经搭建好了！

---

> [← 返回目录](./README.md) | [下一章：第 1 章 →](./chapter-01-mood-card.md)
