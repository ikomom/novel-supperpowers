---
name: novel-arc-recut
description: Recut, compress, and renumber a drafted novel arc after exploratory writing. Use when a fiction chapter range has become structurally loose, chapter order or titles are wrong, information is too scattered, or the user wants a repeatable process to rebuild a clean chapter sequence in a new directory. Part of the novel skill suite; sits between structure extraction and prose drafting. Supports creating a recut output folder, preserving the old directory, rewriting chapter files in a tighter order, and validating chapter length and continuity with a bundled Python checker.
---

# Novel Arc Recut

用这个 skill 把一段已经写散的章节，重组为一套更干净的新顺序。

## 核心规则

不要试图一把把所有东西收干净。

按阶段做：
1. 先看当前结构，确认真正的故事单元
2. 决定新的顺序和标题体系
3. 新建一个输出目录，不直接破坏旧目录
4. 按新结构重写或合并章节
5. 每完成一批就跑检查脚本
6. 等用户确认后，再由用户自己决定怎么清旧目录

## 默认流程

### 1. 先诊断，再动笔

阅读相关章节和必要笔记，只提炼这些事实：
- 哪些章节本来就稳，可以保留
- 哪些章节拆得过细
- 哪些章节只是重复同一层信息
- 哪些标题已经和实际功能不匹配
- 真正的转折点落在哪里

如果用户已经明确说“直接做”，就少解释，直接开始重组。

### 2. 在新目录里重建

优先新建类似这样的目录：
- `structured-recut/`
- `structured-v2/`
- `structured-clean/`

如果旧文件不能安全改名或删除，就保留旧目录不动，只在新目录里输出净版。

### 3. 按故事功能切章，不按旧文件数量切章

压缩章节时，按这些功能切：
- 起手 / 扰动
- 调查 / 追索
- 第一次翻面
- 核心对撞
- 代价 / 收束
- after

不要因为旧目录已经有很多章，就机械保留原章数。

### 4. 标题必须诚实

章名必须反映这一章现在真正承担的功能。

如果结构重组后分组变了，标题也必须跟着变。

优先用同一套风格，比如：
- `影子的病历（上）/（中）/（下）/（完）`
- `第一页病历（一）...（六）`
- `第一页病历after`

不要留下旧施工阶段那种已经不匹配的标题。

### 5. 收紧信息流，不要破坏原故事逻辑

重组时保住这些原则：
- 事件驱动
- 分析服务动作
- 真相在行动中露出来
- 抽象危险要落在具体载体上
- 主角仍然是行动中的思考者

如果同一层信息已经出现过，就不要只是换壳再讲一次，除非新的出现确实更深一层。

### 6. 用 Python 检查脚本兜底

每完成一批，就跑 `scripts/check_chapter_lengths.py`。

检查这些：
- 文件名顺序是否正确
- 内文标题是否和文件名对应
- 章节是否过短或过长
- 范围内是否缺号

如果脚本报异常，先修完再宣布重组完成。

## 推荐施工方式

当用户强调“这个过程要能复现”时，按这套节奏走：
1. 读旧稿范围
2. 决定新顺序和命名
3. 新建净版目录
4. 先写前几章
5. 跑检查
6. 给用户看新顺序
7. 再一批一批往下补

## 汇报要求

汇报时说明：
- 新写了哪些文件
- 旧目录是否保持不动
- 这一批做了哪些压缩或合并
- 检查脚本是否通过，若没通过卡在哪里

## 参考文件

### `references/process.md`

需要更详细的重组顺序时再读。

### `scripts/check_chapter_lengths.py`

需要确定章号、标题、字数、缺号是否正常时就运行。