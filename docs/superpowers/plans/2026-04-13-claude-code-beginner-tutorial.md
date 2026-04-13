# Claude Code 初学者教程 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 从零构建一本完整的 Claude Code 初学者教程小册子，含 6 章正文、代码示例、附录和 Prompt 速查表。

**Architecture:** 采用单文件分章节的小册子结构（每章一个 Markdown），所有配套代码独立放在 `examples/` 目录下。第 0-5 章按学习顺序递进，附录作为独立参考文档。代码示例均保持单文件/极简结构，降低新手门槛。

**Tech Stack:** Markdown（文档）、HTML + CSS + Vue 3 CDN（前端示例）、Python 3（脚本示例）

---

## File Structure

```
/Users/lxr/workspace/study/
└── tutorial/
    ├── README.md                       # 教程总入口：介绍、学习路径、目录
    ├── chapter-00-setup.md             # 第 0 章：准备工作
    ├── chapter-01-mood-card.md         # 第 1 章：心情记录卡片
    ├── chapter-02-modify-code.md       # 第 2 章：代码解释与修改
    ├── chapter-03-weather-script.md    # 第 3 章：天气查询脚本
    ├── chapter-04-accounting-app.md    # 第 4 章：记账小应用
    ├── chapter-05-advanced.md          # 第 5 章：进阶与日常技巧
    ├── appendix-troubleshooting.md     # 附录：常见踩坑指南
    ├── prompt-cheatsheet.md            # Prompt 示例速查表
    └── examples/                       # 配套代码
        ├── 01-mood-card.html
        ├── 01-mood-card-challenge.html
        ├── 03-weather.py
        ├── 03-weather-challenge.py
        ├── 04-accounting-app.html
        └── 04-accounting-app-challenge.html
```

---

### Task 1: Create `tutorial/README.md` (总入口)

**Files:**
- Create: `tutorial/README.md`

- [ ] **Step 1: Write the README with overview and table of contents**

```markdown
# Claude Code 初学者教程

> 面向完全编程新手的分章节学习小册子。你不需要任何编程基础，只需要一台电脑和好奇心。

## 你将学到什么

- 如何安装和配置 Claude Code
- 如何通过与 AI 对话来完成编程任务
- 如何描述需求、运行代码、排查错误
- 如何用 Vue 做简单网页，用 Python 写实用脚本

## 项目实战

1. **心情记录卡片** — 一个能记录心情的互动小网页
2. **天气查询脚本** — 用 Python 查天气并保存结果
3. **记账小应用** — 带统计和分类的完整记账工具

## 章节目录

- [第 0 章：准备工作](./chapter-00-setup.md)
- [第 1 章：第一次对话 — 心情记录卡片](./chapter-01-mood-card.md)
- [第 2 章：代码解释与修改](./chapter-02-modify-code.md)
- [第 3 章：走出浏览器 — 天气查询脚本](./chapter-03-weather-script.md)
- [第 4 章：综合实战 — 记账小应用](./chapter-04-accounting-app.md)
- [第 5 章：进阶与日常技巧](./chapter-05-advanced.md)
- [附录：常见踩坑指南](./appendix-troubleshooting.md)
- [Prompt 速查表](./prompt-cheatsheet.md)

## 如何使用本教程

建议按顺序阅读，每章跟着动手做一遍。遇到不懂的术语，可以直接复制 Prompt 问 Claude Code。
```

- [ ] **Step 2: Verify the README renders correctly**

Run: `cat tutorial/README.md | head -20`
Expected: Markdown file with proper headings and relative links.

- [ ] **Step 3: Commit**

```bash
git add tutorial/README.md
git commit -m "docs: add tutorial README with table of contents"
```

---

### Task 2: Write `tutorial/chapter-00-setup.md` (准备工作)

**Files:**
- Create: `tutorial/chapter-00-setup.md`

- [ ] **Step 1: Write the full chapter content**

Content must include:
1. 安装 Claude Code（macOS / Windows / Linux 分别的命令）
2. 注册与登录流程（`claude login`）
3. 连接国内模型：配置 `CLAUDE.md` 的示例
4. 为什么要有 `CLAUDE.md`（系统提示词 + 项目记忆）
5. `CLAUDE.md` 基础写法示例（YAML Frontmatter + Markdown）
6. 实战：写一条"请用中文回复，代码注释用中文"的规则
7. 验证配置是否生效
8. 终端基础：cd / ls / python3 / 运行 HTML 文件

- [ ] **Step 2: Verify content completeness**

Run: `grep -c "CLAUDE.md" tutorial/chapter-00-setup.md`
Expected: count >= 5

- [ ] **Step 3: Commit**

```bash
git add tutorial/chapter-00-setup.md
git commit -m "docs: add chapter 00 - setup and CLAUDE.md basics"
```

---

### Task 3: Write `tutorial/chapter-01-mood-card.md` + Example Code

**Files:**
- Create: `tutorial/chapter-01-mood-card.md`
- Create: `tutorial/examples/01-mood-card.html`
- Create: `tutorial/examples/01-mood-card-challenge.html`

- [ ] **Step 1: Write the basic mood card HTML example**

File: `tutorial/examples/01-mood-card.html`

Requirements:
- Single HTML file with Vue 3 via CDN
- Four mood emojis (开心/平静/难过/兴奋)
- Text input for description
- "生成卡片" button
- Cards displayed in a list below with timestamp

- [ ] **Step 2: Write the challenge version with color themes**

File: `tutorial/examples/01-mood-card-challenge.html`

Requirements:
- Same as basic but each mood has a background color:
  - 开心 = warm yellow (#fef3c7)
  - 平静 = light blue (#dbeafe)
  - 难过 = gray-blue (#e2e8f0)
  - 兴奋 = pink (#fce7f3)

- [ ] **Step 3: Write Chapter 1 markdown with full instructions**

File: `tutorial/chapter-01-mood-card.md`

Must include:
- 学习目标
- 项目效果描述
- Prompt 示例（可复制）
- Step-by-step 操作指引（新建文件→贴代码→保存→浏览器打开）
- 运行验证截图文字说明
- 本章挑战说明
- 指向 challenge HTML 的链接

- [ ] **Step 4: Verify files exist and chapter references examples correctly**

Run: `ls tutorial/examples/01-mood-card*.html && grep "01-mood-card" tutorial/chapter-01-mood-card.md`
Expected: Both HTML files exist and chapter references them.

- [ ] **Step 5: Commit**

```bash
git add tutorial/chapter-01-mood-card.md tutorial/examples/01-mood-card.html tutorial/examples/01-mood-card-challenge.html
git commit -m "docs: add chapter 01 - mood card project with examples"
```

---

### Task 4: Write `tutorial/chapter-02-modify-code.md`

**Files:**
- Create: `tutorial/chapter-02-modify-code.md`

- [ ] **Step 1: Write the full chapter content**

Must include three practical exercises based on Chapter 1:

1. **代码解释**
   - Prompt: "请逐段解释这个 HTML 文件里的代码是什么意思"
   - 解释 `<template>` / `<script>` / `<style>` 的分工说明

2. **修改样式**
   - Prompt: "我想让卡片在鼠标放上去的时候微微向上浮起，并加深阴影，请帮我改 CSS"
   - 提供完整的 CSS diff / 新增代码块

3. **添加功能**
   - Prompt: "给每张卡片右上角加一个删除按钮，点击后确认再删除"
   - 提供 Vue 方法 `removeCard(index)` 和确认逻辑代码

4. **教学重点小结**
   - 精确 Prompt vs 模糊 Prompt 对比
   - 小步迭代
   - 报错如何反馈给 AI

5. **本章挑战**
   - "清空所有记录"按钮 + 二次确认
   - 提供参考实现思路（不直接给完整代码，而是给关键函数提示）

- [ ] **Step 2: Verify the chapter contains all 3 exercise sections**

Run: `grep -c "## " tutorial/chapter-02-modify-code.md`
Expected: count >= 4

- [ ] **Step 3: Commit**

```bash
git add tutorial/chapter-02-modify-code.md
git commit -m "docs: add chapter 02 - code explanation and modification"
```

---

### Task 5: Write `tutorial/chapter-03-weather-script.md` + Example Code

**Files:**
- Create: `tutorial/chapter-03-weather-script.md`
- Create: `tutorial/examples/03-weather.py`
- Create: `tutorial/examples/03-weather-challenge.py`

- [ ] **Step 1: Write the basic weather script**

File: `tutorial/examples/03-weather.py`

Requirements:
- Uses standard library `urllib` to avoid pip install (or mentions `requests` as optional)
- Prompts user for city name via `input()`
- Calls 和风天气 API (or Open-Meteo as fallback) to fetch weather
- Prints weather info to terminal
- Saves result to `城市名-YYYY-MM-DD.txt`
- Includes error handling for network issues and invalid city names

- [ ] **Step 2: Write the challenge version (3-day forecast)**

File: `tutorial/examples/03-weather-challenge.py`

Requirements:
- Same as basic but queries 3-day forecast
- Writes all days into the same text file

- [ ] **Step 3: Write Chapter 3 markdown**

File: `tutorial/chapter-03-weather-script.md`

Must include:
- 脚本 vs 网页的区别说明
- API 通俗比喻（餐厅菜单与后厨）
- 和风天气 API Key 申请步骤（截图位置标记）
- 完整的 Prompt 示例和分步实现指引
- 常见报错排查（网络、编码、API Key）
- 本章挑战说明

- [ ] **Step 4: Verify files and references**

Run: `ls tutorial/examples/03-weather*.py && grep "03-weather" tutorial/chapter-03-weather-script.md`
Expected: Both Python files exist and chapter references them.

- [ ] **Step 5: Commit**

```bash
git add tutorial/chapter-03-weather-script.md tutorial/examples/03-weather.py tutorial/examples/03-weather-challenge.py
git commit -m "docs: add chapter 03 - weather script project with examples"
```

---

### Task 6: Write `tutorial/chapter-04-accounting-app.md` + Example Code

**Files:**
- Create: `tutorial/chapter-04-accounting-app.md`
- Create: `tutorial/examples/04-accounting-app.html`
- Create: `tutorial/examples/04-accounting-app-challenge.html`

- [ ] **Step 1: Write the basic accounting app HTML**

File: `tutorial/examples/04-accounting-app.html`

Requirements:
- Vue 3 via CDN, single HTML file
- Top section: 收入/支出/结余 statistics cards
- Middle section: form with type (income/expense), category dropdown, amount, note, date
- Bottom section: record list with delete button
- Income shown in green, expense in red
- Data persists in `localStorage`
- Categories: 餐饮, 交通, 娱乐, 购物, 工资, 其他

- [ ] **Step 2: Write the challenge version (month filter)**

File: `tutorial/examples/04-accounting-app-challenge.html`

Requirements:
- Same as basic but adds a month selector dropdown
- Statistics and list update based on selected month
- "全部" option to show everything

- [ ] **Step 3: Write Chapter 4 markdown**

File: `tutorial/chapter-04-accounting-app.md`

Must include:
- 学习目标
- 项目最终效果图文字描述
- 5-step 拆分实现路径，每步配有 Prompt 示例
  1. 搭建骨架
  2. 数据绑定
  3. 分类和颜色
  4. 统计区域
  5. 删除 + localStorage
- 用 Claude Code 审校代码的 Prompt 示例
- Bug 定位教学："加了删除后统计没更新"
- 本章挑战

- [ ] **Step 4: Verify files and references**

Run: `ls tutorial/examples/04-accounting-app*.html && grep "04-accounting-app" tutorial/chapter-04-accounting-app.md`
Expected: Both HTML files exist and chapter references them.

- [ ] **Step 5: Commit**

```bash
git add tutorial/chapter-04-accounting-app.md tutorial/examples/04-accounting-app.html tutorial/examples/04-accounting-app-challenge.html
git commit -m "docs: add chapter 04 - accounting app project with examples"
```

---

### Task 7: Write `tutorial/chapter-05-advanced.md`

**Files:**
- Create: `tutorial/chapter-05-advanced.md`

- [ ] **Step 1: Write the full advanced techniques chapter**

Must include:

1. **调试三板斧**
   - 粘贴报错信息
   - 让 AI 解释日志
   - Working Backwards：从预期反推

2. **重构与优化**
   - 代码太长怎么拆
   - 让 AI 起更好的变量名
   - "这段代码能更简洁吗？"

3. **更高效的 Prompt 技巧**
   - 提供上下文（"这是 Vue 3 单文件 HTML"）
   - 要求先给思路再写代码
   - 用 "请解释为什么这样改" 来学习
   - 每个技巧配 1-2 个可直接复制的 Prompt

4. **多文件项目管理**
   - 什么时候拆分文件
   - 让 Claude Code 整理目录结构
   - 批量修改多个文件

5. **Skills 速查**
   - 什么是内置 Skills
   - `/commit`, `/review-pr` 等常见 Skills
   - 如何查看可用 Skills 列表 (`/help` 或 `claude skills`)

6. **下一步学习建议**
   - 前端路径：HTML/CSS → JavaScript → Vue/React → 全栈
   - Python 路径：基础 → 爬虫/自动化 → 数据分析/后端
   - 持续练手建议

- [ ] **Step 2: Verify completeness**

Run: `grep -c "Prompt" tutorial/chapter-05-advanced.md`
Expected: count >= 6

- [ ] **Step 3: Commit**

```bash
git add tutorial/chapter-05-advanced.md
git commit -m "docs: add chapter 05 - advanced techniques and next steps"
```

---

### Task 8: Write `tutorial/appendix-troubleshooting.md`

**Files:**
- Create: `tutorial/appendix-troubleshooting.md`

- [ ] **Step 1: Write the complete troubleshooting appendix**

Must cover four categories:

1. **安装与环境类**
   - Claude Code 安装失败（Node.js 版本、网络、权限）
   - 终端找不到命令（Path 环境变量、Shell 差异）
   - `python` 不存在（Windows 用 `py`，macOS/Linux 用 `python3`）

2. **网络与模型类**
   - 国内模型无响应（Base URL、API Key、模型名）
   - Claude Code 登录超时（代理、防火墙）

3. **运行与报错类**
   - HTML 白板（CDN 加载失败、语法错误）
   - `ModuleNotFoundError`（库未安装、Python 2）
   - 和风天气 API 错误（编码、Key 未生效、额度）
   - localStorage 消失（隐私模式、清除数据、域名变化）

4. **与 AI 协作类**
   - 代码跑不通：怎么贴报错
   - AI 改错地方：怎么精确重述
   - 代码改乱了：Git 基础回退（`git diff`, `git checkout`）

Each problem must include:
- 现象描述
- 可能原因
- 解决步骤（1-2-3）

- [ ] **Step 2: Verify all 4 categories exist**

Run: `grep -c "### " tutorial/appendix-troubleshooting.md`
Expected: count >= 4

- [ ] **Step 3: Commit**

```bash
git add tutorial/appendix-troubleshooting.md
git commit -m "docs: add troubleshooting appendix"
```

---

### Task 9: Write `tutorial/prompt-cheatsheet.md`

**Files:**
- Create: `tutorial/prompt-cheatsheet.md`

- [ ] **Step 1: Write the prompt cheatsheet**

Must include at least 15 directly copyable prompts organized by scenario:

**需求描述类**
- "帮我写一个单文件的 HTML 网页，使用 Vue 3 CDN，功能是..."
- "给我一个 Python 脚本，运行后在终端询问用户输入，然后..."

**代码解释类**
- "请逐段解释这段代码是什么意思"
- "这段代码里的 `{{ variable }}` 是什么作用？"

**修改优化类**
- "我想让卡片在鼠标放上去时向上浮起并加深阴影，请改 CSS"
- "给这段代码加上删除功能，删除前要有确认提示"
- "这段代码能更简洁吗？请保留原有功能"

**调试排查类**
- "我运行代码时出现了以下报错，请帮我分析原因：```...```"
- "网页打开是空白的，请帮我检查这段代码哪里有问题"

**审校学习类**
- "请检查这段代码的结构，给我优化建议"
- "请解释你为什么要这样修改"
- "如果我要继续加 XXX 功能，应该从哪里入手？"

**项目管理类**
- "帮我整理一下这个项目的目录结构"
- "请批量修改这几个文件中的 XXX"

- [ ] **Step 2: Verify prompt count**

Run: `grep -c '"' tutorial/prompt-cheatsheet.md`
Expected: count >= 15

- [ ] **Step 3: Commit**

```bash
git add tutorial/prompt-cheatsheet.md
git commit -m "docs: add prompt cheatsheet"
```

---

### Task 10: Final Review and Consistency Check

**Files:**
- Read all: `tutorial/*.md`, `tutorial/examples/*`

- [ ] **Step 1: Verify internal links are consistent**

Run: `grep -o '\[.*\](\./.*\.md)' tutorial/README.md | wc -l`
Expected: 8 (all chapters + appendix + cheatsheet linked)

- [ ] **Step 2: Verify all example files are referenced in their chapters**

Run:
```bash
grep -l "examples/" tutorial/chapter-*.md
grep -c "examples/" tutorial/chapter-01-mood-card.md
grep -c "examples/" tutorial/chapter-03-weather-script.md
grep -c "examples/" tutorial/chapter-04-accounting-app.md
```
Expected: chapters 01, 03, 04 each have >= 2 references to example files.

- [ ] **Step 3: Final commit**

```bash
git add .
git commit -m "docs: complete Claude Code beginner tutorial v1.0"
```

---

## Spec Coverage Check

| Spec Requirement | Implementing Task |
|---|---|
| 6 章结构 | Tasks 2-7 |
| 心情记录卡片项目 | Task 3 |
| 代码解释与修改 | Task 4 |
| 天气查询脚本 | Task 5 |
| 记账小应用 | Task 6 |
| 进阶技巧 | Task 7 |
| CLAUDE.md 教学 | Task 2 |
| 常见踩坑指南 | Task 8 |
| Prompt 速查表 | Task 9 |
| 单文件/极简代码示例 | Tasks 3, 5, 6 |
| 每章 Prompt 示例 | Tasks 2-7 |

No gaps identified.

## Placeholder Scan

Plan contains:
- No TBD or TODO items
- No "implement later" or "fill in details"
- No vague "add validation" or "handle edge cases" without specifics
- All code steps show concrete file contents or functionality requirements
- All file paths are exact
