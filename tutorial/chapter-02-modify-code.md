# 第 2 章：代码解释与修改

> [← 上一章：第 1 章](./chapter-01-mood-card.md) | [返回目录](./README.md) | [下一章：第 3 章 →](./chapter-03-weather-script.md)

恭喜你已经完成了第一章！现在你的电脑上应该已经有了一个可以运行的心情记录卡片网页。这一章，我们来学习如何"读懂"代码，以及如何请 Claude Code 帮你修改它。

---

## 学习目标

学会请 AI 解释代码，并精确表达修改需求。

---

## 练习一：让 Claude Code 解释代码

当你拿到一段代码时，第一步不是急着改，而是先理解它。Claude Code 很擅长把复杂的代码翻译成大白话。

### Prompt 示例

你可以把下面这段话复制发给 Claude Code（记得把 `mood-card.html` 里的代码一起贴上去）：

```
请逐段解释这个 HTML 文件里的代码是什么意思。我不太懂 Vue，请用简单的话告诉我 <template>、<script>、<style> 分别做了什么。
```

### 简单说明

在单文件 HTML 里，这三部分通常是这样的分工：

- **`<template>`（模板部分，也就是 HTML 标签）**：决定页面上有什么元素、长什么样、怎么排列。比如按钮、输入框、卡片都放在这里。
- **`<script>`（脚本部分）**：存放数据和逻辑。比如用户选了什么心情、输入了什么文字、点击按钮后要做什么，都在这里定义。
- **`<style>`（样式部分）**：控制外观。比如颜色、大小、间距、圆角、阴影等，让页面变得好看。

💡 小提示：即使你现在还看不懂每一行代码，也没关系。先把"整体分工"搞清楚，后面就会越来越轻松。

---

## 练习二：修改样式 — 卡片悬浮效果

现在我们来做一点小改动：让卡片在鼠标放上去的时候，微微向上浮起，同时阴影加深，给人一种"被托起"的感觉。

### Prompt 示例

```
我想让卡片在鼠标放上去的时候微微向上浮起，并加深阴影，请帮我改 CSS。
```

### 可以直接用的 CSS 代码

把下面这段代码复制，替换掉你原来文件里的 `.card` 相关样式即可：

```css
.card {
  background-color: #ffffff;
  padding: 16px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  transition: transform 0.2s, box-shadow 0.2s;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}
```

改完后保存文件，刷新浏览器，把鼠标移到卡片上试试看！

💡 小提示：`transition` 的作用是让变化变得平滑。如果没有它，卡片会"啪"一下跳上去；有了它，就会优雅地飘起来。

---

## 练习三：添加删除功能

卡片越积越多，我们希望能删掉不需要的卡片。接下来，给每张卡片右上角加一个删除按钮。

### Prompt 示例

```
给每张卡片右上角加一个删除按钮，点击后弹出确认提示，确认后再删除这张卡片。
```

### 需要修改的地方

#### 1. HTML 模板：在卡片里添加删除按钮

找到 `.card-header` 那一块，改成下面这样：

```html
<div class="card-header">
  <span class="card-emoji">{{ card.emoji }}</span>
  <span class="card-time">{{ card.time }}</span>
  <button class="delete-btn" @click="removeCard(index)">×</button>
</div>
```

同时，在 `<style>` 里加上删除按钮的样式：

```css
.delete-btn {
  background: transparent;
  border: none;
  color: #94a3b8;
  font-size: 18px;
  cursor: pointer;
  padding: 0 4px;
  margin-left: 8px;
  line-height: 1;
  width: auto;
}

.delete-btn:hover {
  color: #ef4444;
}
```

#### 2. JavaScript：添加删除方法

在 `methods` 里，加上 `removeCard` 方法：

```javascript
methods: {
  addCard() {
    const mood = this.moods.find(m => m.name === this.selectedMood);
    const now = new Date();
    const timeStr = now.toLocaleString("zh-CN");
    this.cards.push({
      emoji: mood.emoji,
      text: this.description || "暂无描述",
      time: timeStr
    });
    this.description = "";
  },
  removeCard(index) {
    if (confirm("确定要删除这张卡片吗？")) {
      this.cards.splice(index, 1);
    }
  }
}
```

#### 3. 完整的 `<script>` 参考代码

如果你希望直接复制一整段，下面是基于第 1 章代码的完整 `<script>` 部分：

```html
<script>
  const { createApp } = Vue;

  createApp({
    data() {
      return {
        moods: [
          { name: "开心", emoji: "😊" },
          { name: "平静", emoji: "😌" },
          { name: "难过", emoji: "😢" },
          { name: "兴奋", emoji: "🤩" }
        ],
        selectedMood: "开心",
        description: "",
        cards: []
      };
    },
    methods: {
      addCard() {
        const mood = this.moods.find(m => m.name === this.selectedMood);
        const now = new Date();
        const timeStr = now.toLocaleString("zh-CN");
        this.cards.push({
          emoji: mood.emoji,
          text: this.description || "暂无描述",
          time: timeStr
        });
        this.description = "";
      },
      removeCard(index) {
        if (confirm("确定要删除这张卡片吗？")) {
          this.cards.splice(index, 1);
        }
      }
    }
  }).mount("#app");
</script>
```

保存后刷新页面，生成几张卡片，点击右上角的 "×" 试试看吧！

---

## 教学重点小结

### 精确的 Prompt 效果更好

对比一下这两句话：

- **模糊**："让它好看一点" → AI 不知道你的审美，可能会改得让你意外。
- **精确**："圆角从 8px 改到 16px，背景加淡淡渐变" → AI 能准确执行，结果更可控。

### 小步迭代

每次只改一个地方，保存、刷新、确认没问题后再改下一个。这样出了问题，你很快就能知道是哪一步导致的。

### 报错反馈

如果改完网页白屏了，或者按钮没反应了，不要慌。按键盘上的 `F12`（Mac 上是 `Cmd + Option + I`）打开浏览器的开发者工具，切换到 **Console** 标签页，把红色的报错信息复制下来，直接贴给 Claude Code。它通常能很快帮你定位问题。

💡 小提示：AI 不怕你问"蠢问题"，但它需要足够的信息才能帮到你。报错信息、你改了哪一行、想要的效果是什么，都是很有用的线索。

---

## 本章挑战

### 任务

加一个"清空所有记录"按钮，放在"生成卡片"按钮旁边，点击后有确认提示，避免误删。

### 实现思路提示

- 在 HTML 里加一个 `<button @click="clearAll">清空所有</button>`
- 在 `methods` 里写 `clearAll()` 方法，用 `confirm()` 确认后执行 `this.cards = []`
- 可以给清空按钮不同的颜色（比如灰色或红色），和"生成卡片"按钮区分开

💡 小提示：试着自己先写一写，遇到困难再把代码贴给 Claude Code，请它帮你检查哪里不对。

---

---

> [← 上一章：第 1 章](./chapter-01-mood-card.md) | [返回目录](./README.md) | [下一章：第 3 章 →](./chapter-03-weather-script.md)
