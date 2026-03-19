---
name: novel-arc-recut
description: Recut, compress, and renumber a drafted novel arc after exploratory writing. Use when a fiction chapter range has become structurally loose, chapter order or titles are wrong, information is too scattered, or the user wants a repeatable process to rebuild a clean chapter sequence in a new directory. Part of the novel skill suite; sits between structure extraction and prose drafting. Supports creating a recut output folder, preserving the old directory, rewriting chapter files in a tighter order, and validating chapter length and continuity with a bundled Python checker.
---

# Novel Arc Recut

用这个 skill 把一段已经写散的章节，重组为一套更干净的新顺序。

## 默认流程
1. 先读旧稿范围
2. 决定新顺序和命名
3. 新建净版目录
4. 先写前几章
5. 跑检查脚本
6. 再分批往下补

## 核心规则
- 不一把梭
- 不直接破坏旧目录
- 按故事功能切章，不按旧文件数量切章
- 标题必须诚实
- 每完成一批就检查

## 参考文件
- `references/process.md`
- `scripts/check_chapter_lengths.py`
