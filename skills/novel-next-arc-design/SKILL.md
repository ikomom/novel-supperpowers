---
name: novel-next-arc-design
description: Design the next compelling story arc for a serialized novel based on existing chapters, current character state, unresolved pressures, thematic progression, and recent aftermath. Use when the user wants to decide what new story should come next, generate multiple candidate arcs, avoid repetitive follow-ups, and choose the most promising next arc before outlining or drafting prose.
---

# Novel Next Arc Design

用这个 skill 推出“下一篇到底该写什么”。

## 用途

不要从“上一篇结束了”直接跳到“随便来个新剧情”。

如果当前材料来自长篇或超长篇，先基于结构提炼结果做判断，不要假设自己已经稳定记住了全书。

下一篇应该从这些地方长出来：
- 人物当前状态
- 上一篇留下的后果
- 还没解决的压力
- 仍在发力的母题
- 新出现但尚未兑现的关系变化

先判断这次要解决的到底是：
- 补一章
- 补尾声
- 开一个中篇后续 arc
- 还是开启新的长篇阶段

范围没定，先不要急着提候选。

## 核心规则

一个好的新 arc，不只是新。

它还必须：
- 承接上一篇
- 在结构功能上不同于上一篇
- 能逼出人物新的选择
- 能快速长出具体场景，而不是停留在概念层

## 先做什么，再提候选

在提出候选 arc 之前，先弄清这七件事：
1. 上一篇到底改变了什么
2. 现在还在疼的地方是什么
3. 哪些压力还没解决
4. 哪些母题还有继续生长的空间
5. 哪些东西绝不能原样重复
6. 这部作品原本的结构重心是什么，主菜和调味分别是什么
7. 这次续写的范围有多大，第一步应该写到哪里为止

## 候选生成规则

除非用户明确只要一个，否则默认给 **3 个候选 arc**。

每个候选都要包含：
- 一句话核心
- 它如何承接上一篇
- 它真正的新鲜点
- 核心冲突
- 它会逼出主角哪一面
- 它靠什么具体场景/载体成立
- 它的风险点
- 预计篇幅

## 防重复规则

如果一个候选有下面这些问题，就降级或淘汰：
- 只是换皮重复上一段核心机制
- 只是放大规模，没有改变结构
- 还是让主角承受同一种测试
- 主要靠解释，不靠场景推进
- 复用了同一种空间、物件或威胁形式，却没有变形

## 优先选择的方向

更优的候选通常至少满足其中两条：
- 重解释上一篇的后果
- 强迫人物做新选择
- 重写某段关系
- 把旧母题换到新载体里
- 在不破坏连续性的前提下扩展世界
- 让主角刚获得的伤痕真正发挥作用

## 输出要求

列完候选后，要明确选出最优方案，并说明原因。

如果原文体量很大，先停在“候选 + 最优方案 + 第一阶段范围建议”，不要贪心把后面所有步骤揉在一起。

如果用户继续推进，再补：
- arc 主脊梁
- 预计章数
- 第一章怎么起
- 第一章的扰动点是什么

## 参考文件

### `references/selection-questions.md`

用来判断一个候选到底值不值得写。

### `references/output-template.md`

用来套默认候选输出格式。

### `references/source-mining.md`

用来从上一篇里挖出真正能继续长的东西。

## 交接

如果用户已经选定方向，接下来要做结构，交给 `novel-structure-extract` 或直接产出结构笔记。
如果用户要按选定结构写正文，交给 `novel-draft-from-structure`。