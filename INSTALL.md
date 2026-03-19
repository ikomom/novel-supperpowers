# Install

这个仓库是一个 **OpenClaw skill collection**。

## 方式一：复制到工作区（最简单）

把 `skills/` 下面的各个 skill 目录复制到你的 OpenClaw 工作区：

```bash
cp -r skills/* ~/.openclaw/workspace-main/skills/
```

复制完成后，你的工作区应当包含：

```text
~/.openclaw/workspace-main/skills/
├── novel-workbench/
├── novel-structure-extract/
├── novel-next-arc-design/
├── novel-arc-recut/
└── novel-draft-from-structure/
```

## 方式二：开发时用符号链接

如果你准备长期迭代这个仓库，建议把每个 skill 目录符号链接进工作区，而不是每次复制。

示例：

```bash
ln -s /path/to/novel-superpowers/skills/novel-workbench ~/.openclaw/workspace-main/skills/novel-workbench
ln -s /path/to/novel-superpowers/skills/novel-structure-extract ~/.openclaw/workspace-main/skills/novel-structure-extract
ln -s /path/to/novel-superpowers/skills/novel-next-arc-design ~/.openclaw/workspace-main/skills/novel-next-arc-design
ln -s /path/to/novel-superpowers/skills/novel-arc-recut ~/.openclaw/workspace-main/skills/novel-arc-recut
ln -s /path/to/novel-superpowers/skills/novel-draft-from-structure ~/.openclaw/workspace-main/skills/novel-draft-from-structure
```

## 推荐使用顺序

通常按这条线使用：

1. `novel-structure-extract`
2. `novel-next-arc-design`
3. `novel-arc-recut`（当草稿已经写散时）
4. `novel-draft-from-structure`

或者直接先调用：
- `novel-workbench`

让它帮助决定下一步该切哪个子 skill。

## 额外说明

- skill 名与目录名使用英文，目的是保证稳定、可迁移、易维护
- skill 内容使用中文，目的是更贴近中文小说工作流
- `novel-arc-recut` 自带 Python 检查脚本，可用于验证章号、标题、字数、缺号
