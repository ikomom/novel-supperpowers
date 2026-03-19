# novel-superpowers

一组面向 **中文长篇/连载小说工作流** 的 OpenClaw skills。

这个仓库参考了多-skill 组合式仓库的思路，但聚焦在小说生产链路，而不是通用代理能力。

它解决的不是“怎么随手续一章”，而是更完整的一条线：

- 先从原文里提炼结构
- 再判断下一篇该写什么
- 如果某一段已经写散了，再重切章节
- 最后按结构稳定输出正文

---

## Included skills

### `novel-workbench`
总控 skill。

负责判断当前任务应该切到哪个子 skill：
- 提炼结构
- 设计下一篇
- 重切章节
- 按结构写正文

### `novel-structure-extract`
从原文、既有章节或某一段篇章里提炼：
- 人物线
- 事件推进
- 母题
- 转折点
- 章节功能
- 重写约束

### `novel-next-arc-design`
从上一篇余波里推出下一篇最值得写的 arc。

不是乱想点子，而是重点判断：
- 承接什么
- 新鲜点在哪里
- 哪些东西不能原样重复
- 哪个候选最值得写

### `novel-arc-recut`
当一段章节已经写散、写乱、写碎时，重新压缩与重组。

特点：
- 推荐新建净版目录，不直接破坏旧目录
- 提供 Python 检查脚本验证章号、标题、字数、缺号

### `novel-draft-from-structure`
按已有结构直接产出正文。

重点约束：
- 事件驱动
- 分析长在动作里
- 主角保持主动
- 章尾必须有真实推进力

---

## Repository layout

```text
novel-superpowers/
├── README.md
├── INSTALL.md
├── LICENSE
├── .gitignore
└── skills/
    ├── novel-workbench/
    ├── novel-structure-extract/
    ├── novel-next-arc-design/
    ├── novel-arc-recut/
    └── novel-draft-from-structure/
```

---

## Design principles

### 1. 外壳英文，内容中文
- skill 名、目录名、文件名统一英文
- 说明正文、模板、规则统一中文

这样更稳，也更适合中文小说工作流。

### 2. 一 skill 一职责
不要把“读、想、切、写”塞进一个大 skill。

这套仓库明确拆成：
- 结构提炼
- 下一篇设计
- 章节重切
- 正文生成

### 3. 旧稿默认不破坏
尤其是 `novel-arc-recut`，默认策略是：
- 保留旧目录
- 新建净版目录
- 让用户后续自行比对和清理

### 4. 可复现优先于灵感即兴
这个仓库不是只追求“写出来”，而是追求：
- 能复现
- 能检查
- 能迭代

---

## Recommended workflow

面对一段复杂小说任务时，优先按这个顺序使用：

1. `novel-structure-extract`
2. `novel-next-arc-design`
3. `novel-arc-recut`（仅当现有草稿已经散掉）
4. `novel-draft-from-structure`

或者直接先让 `novel-workbench` 做路由。

---

## Why this exists

很多小说工作流的问题，不在“模型不会写句子”，而在：
- 没先读明白
- 下一篇方向拍脑袋
- 写散之后没有稳定重组流程
- 按结构写正文时容易站桩解释

这组 skills 的目的，就是把这些环节拆开，并固化成可复用的工作方式。

---

## Installation

见：
- [INSTALL.md](./INSTALL.md)

---

## License

MIT
