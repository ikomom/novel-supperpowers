---
name: novel-workbench
description: Coordinate a fiction-writing workflow across specialized novel subskills. Use when working on long-form serialized fiction and deciding whether to (1) extract structure from source chapters, (2) design the next story arc from existing material, (3) recut a messy drafted arc into a cleaner chapter sequence, or (4) draft prose from an existing structure. This is the router/orchestrator skill for the novel skill suite.
---

# Novel Workbench

把这个 skill 当成小说工作流的总控台。

## 用途

不要试图用一个大而全的流程处理所有小说任务。

先判断：现在到底是在做哪一种工作，然后再切到对应子 skill。

## 子 skill

### 1. `novel-structure-extract`
适用于：先读已有章节，再提炼结构。

### 2. `novel-next-arc-design`
适用于：当前问题不是“这一章怎么写”，而是“下一篇该写什么”。

### 3. `novel-arc-recut`
适用于：一段已经写出来，但结构出了问题。

### 4. `novel-draft-from-structure`
适用于：结构已经有了，下一步是按结构写正文。

## 路由规则

### 何时用 `novel-structure-extract`
- 用户说“先读完再写”
- 用户要总笔记、人物梳理、母题梳理、章节功能梳理
- 当前文本理解还不完整

### 何时用 `novel-next-arc-design`
- 用户问“接下来该写什么”
- 用户要多个新故事候选
- 用户要求“既承接前文，又不能重复上一段”
- 当前难点是想新故事，不是写现成章节

### 何时用 `novel-arc-recut`
- 用户说某一段太散、太长、太乱、太碎
- 需要重排顺序和标题
- 需要可复现的重组流程

### 何时用 `novel-draft-from-structure`
- 结构已经稳定
- 用户说“按这个提纲写正文”
- 当前目标是章节文本，不是诊断

## 推荐顺序

复杂篇章优先按这条线走：
1. 先提炼结构
2. 如果方向未定，再设计下一篇
3. 如果现有草稿写散了，再重切
4. 最后按结构写正文
