# Skill Finder CN (skill-finder-cn) 技能说明

## 📖 概述

**Skill 查找器 v1.0.1** — 帮助用户发现和安装 ClawHub 上的 Skills。

- **Emoji**: 🔍
- **作者**: 赚钱小能手
- **依赖**: `clawhub` CLI
- **触发词**: "找 skill"、"find skill"、"搜索 skill"

---

## 🎯 功能场景

当用户问：
- "有什么 skill 可以帮我...？"
- "找一个能做 X 的 skill"
- "有没有 skill 可以..."
- "我需要一个能...的 skill"

此技能会帮助搜索 ClawHub 并推荐相关的 Skills。

---

## ⚙️ 使用方法

### 1. 搜索 Skills

```bash
clawhub search "<用户需求>"
```

示例：
```bash
clawhub search "时间管理"
clawhub search "加密货币价格监控"
```

### 2. 查看详情（含统计数据）

```bash
clawhub inspect <skill-name>
```

或直接 API 查询 stats：
```bash
curl "https://clawhub.ai/api/v1/skills/<skill-name>" | jq '.skill.stats'
```

### 3. 安装 Skill

```bash
clawhub install <skill-name>
```

### 4. ✅ 验证安装（新增！）

安装后**必须验证**是否成功：

```bash
# 检查是否安装成功
ls ~/.openclaw/workspace/skills/<skill-name>/SKILL.md

# 如果文件存在 → 安装成功
# 如果文件不存在 → 安装失败
```

### 5. 检查已安装的 Skill

```bash
clawhub list
```

或：
```bash
ls ~/.openclaw/workspace/skills/
```

---

## 🔄 工作流程

```
1. 理解用户需求
   ↓
2. 提取关键词
   ↓
3. 搜索 ClawHub
   ↓
4. 列出相关 Skills（含下载量/stars）
   ↓
5. 推荐最合适的 Skill
   ↓
6. 安装后验证是否成功 ✅
```

---

## 📊 输出格式（优化版）

搜索结果应该包含：
- Skill 名称
- 简短描述（中文）
- 下载量
- Stars 数
- 是否已安装

**示例**：

```
🔍 "时间管理" 搜索结果：

1. time-management-2
   描述：有效管理时间，避免过度工作
   下载：1,234 | Stars: 15 | ✅ 已安装

2. productivity
   描述：生产力系统，包含目标/任务/习惯
   下载：5,678 | Stars: 42 | ❌ 未安装
```

---

## 💡 完整示例

**用户问题**: "有什么 skill 可以帮我监控加密货币价格？"

**执行步骤**:
```bash
# 1. 搜索
clawhub search "crypto price monitor"

# 2. 查看结果
🔍 "加密货币价格监控" 结果：

1. crypto-tracker
   描述：加密货币价格追踪和提醒
   下载：2,345 | Stars: 28 | ❌ 未安装
   → 推荐安装

# 3. 安装
clawhub install crypto-tracker

# 4. 验证
ls ~/.openclaw/workspace/skills/crypto-tracker/SKILL.md
✅ 如果显示文件列表 = 安装成功
❌ 如果报错 = 安装失败，需重试或人工检查
```

---

## ✨ v1.0.1 更新

| 功能 | 说明 |
|------|------|
| ✅ 安装后验证步骤 | 确保安装不是假成功 |
| ✅ 搜索结果显示下载量/stars | 帮助评估质量 |
| ✅ 检查是否已安装 | 避免重复安装 |
| ✅ 中文输出优化 | 更符合国内用户 |

---

## 🛠️ 本地笔记（tools.md 中维护）

可以将常用的技能推荐记录在这里：

```markdown
### 常用 Skill 推荐

| 需求 | 推荐 Skill | 状态 |
|------|-----------|------|
| 联网搜索 | multi-search-engine-simple | ✅ 已安装 |
| 浏览器自动化 | agent-browser | ✅ 已安装 |
| 自我改进 | self-improving-proactive-agent | ✅ 已安装 |
| Skill 查找 | skill-finder-cn | ✅ 已安装 |
```

---

## 📌 注意事项

1. **必须先有 clawhub CLI** — 否则无法搜索
2. **安装后必须验证** — `ls .../SKILL.md`
3. **依赖关系注意** — 有些 skill 需要其他前置条件（如 API Key）
4. **优先选高 stars + 高下载量** — 通常更稳定可靠

---

**参考资源**:
- Homepage: https://clawhub.ai
- 命令文档：`clawhub --help`

*帮助用户发现需要的 Skills 🔍*
