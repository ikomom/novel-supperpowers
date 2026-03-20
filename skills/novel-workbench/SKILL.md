---
name: novel-workbench
description: Coordinate a fiction-writing workflow across specialized novel subskills. Use when working on long-form serialized fiction and deciding whether to (1) extract structure from source chapters, (2) design the next story arc from existing material, (3) recut a messy drafted arc into a cleaner chapter sequence, or (4) draft prose from an existing structure. This is the router/orchestrator skill for the novel skill suite.
---

# Novel Workbench

把这个 skill 当成小说工作流的总控台。

## 用途

不要试图用一个大而全的流程处理所有小说任务。

先判断：现在到底是在做哪一种工作，然后再切到对应子 skill。

如果面对的是长篇、超长篇、或需要跨很多章节反复回钩的任务，默认先给出一个简短计划，不要直接开始大段阅读或正文。

## 子 skill

### 1. `novel-structure-extract`

适用于：先读已有章节，再提炼结构。

主要产出：
- 人物线
- 事件推进
- 母题
- 转折点
- 章节功能
- 可复用的结构笔记

### 2. `novel-next-arc-design`

适用于：当前问题不是“这一章怎么写”，而是“下一篇该写什么”。

主要任务：
- 从上一段余波里推出新 arc
- 生成多个候选方向
- 判断哪个方向最值得写
- 控制续写范围（补一章 / 补尾声 / 开中篇 / 开新长篇）

### 3. `novel-arc-recut`

适用于：一段已经写出来，但结构出了问题。

典型情况：
- 顺序不对
- 标题不对
- 信息太散
- 同一功能拆成太多章
- 需要另开净版目录重组

### 4. `novel-draft-from-structure`

适用于：结构已经有了，下一步是按结构写正文。

主要任务：
- 把提纲和章节功能转成真正可读的小说章节
- 保住节奏、角色声音和章尾推进力

## 路由规则

### 何时用 `novel-structure-extract`
- 用户说“先读完再写”
- 用户要总笔记、人物梳理、母题梳理、章节功能梳理
- 当前文本理解还不完整

### 何时用 `novel-next-arc-design`
- 用户问“接下来该写什么”
- 用户要多个新故事候选
- 用户要求“既承接前文，又不能重复上一段”
- 用户说“这个结局不满意，想继续写，但还没决定后续重点”
- 当前难点是想新故事，不是写现成章节

### 何时用 `novel-arc-recut`
- 用户说某一段太散、太长、太乱、太碎
- 需要重排顺序和标题
- 需要可复现的重组流程

### 何时用 `novel-draft-from-structure`
- 结构已经稳定
- 用户说“按这个提纲写正文”
- 用户已经接受了续写校准结果，且第一章范围已经明确
- 当前目标是章节文本，不是诊断

## 长篇任务默认策略

如果原文体量已经超出模型单次稳定理解范围，默认按这套顺序组织工作：

1. 先给出计划，说明这次只处理哪些范围
2. 先用脚本建立章节索引或故事地图
3. 只读取当前任务真正相关的章节
4. 先产出中间结果（结构笔记 / 续写校准 / arc 候选）
5. 最后才进入正文或重组

必要时，把这些步骤拆成子工作流：
- 一个步骤只做结构提炼
- 一个步骤只做后续方向设计
- 一个步骤只做正文起稿

不要把高成本阅读、结构判断和正文写作混成一个大动作。

## 推荐顺序

复杂篇章优先按这条线走：
1. 先提炼结构
2. 如果方向未定，再设计下一篇
3. 如果现有草稿写散了，再重切
4. 最后按结构写正文

如果用户是“接原作结局继续写”，优先按这条线：
1. 先用 `novel-structure-extract` 提炼结局前后的阶段状态
2. 如果原文很长，先做章节索引，只读相关范围
3. 再用 `novel-next-arc-design` 判断后续应该是补尾声、补一章，还是开新 arc
4. 只有范围和重心都明确后，才进入 `novel-draft-from-structure`

如果结构明显不稳，不要直接跳进正文。