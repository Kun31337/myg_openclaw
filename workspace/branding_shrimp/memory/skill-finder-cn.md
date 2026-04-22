# Skill Finder (技能查找器)

## 技能路径

`/Users/zhu/.openclaw/workspace/skills/skill-finder-cn/SKILL.md`

## 功能说明

帮助用户**发现和安装 ClawHub 上的 Skills**。回答"有什么技能可以 X"、"找一个技能"、"搜索技能"等问题。

### 🔍 触发词
- "找 skill"
- "find skill"
- "搜索 skill"
- "有什么 skill 可以帮我..."
- "找一个能做 X 的 skill"
- "有没有 skill 可以..."
- "我需要一个能...的 skill"

---

## 使用方法

### 1️⃣ 搜索 Skills

```bash
clawhub search "<用户需求关键词>"
```

### 2️⃣ 查看详情（含统计数据）

```bash
clawhub inspect <skill-name>
```

或者直接 API 查询 stats：

```bash
curl "https://clawhub.ai/api/v1/skills/<skill-name>" | jq '.skill.stats'
```

### 3️⃣ 安装 Skill

```bash
clawhub install <skill-name>
```

### 4️⃣ **验证安装（新增！）** ⚠️

安装后必须验证是否成功：

```bash
# 检查是否安装成功
ls ~/.openclaw/workspace/skills/<skill-name>/SKILL.md

# ✅ 如果文件存在 = 安装成功
# ❌ 如果文件不存在 = 安装失败，需要重新尝试
```

### 5️⃣ 检查已安装的 Skill

```bash
# 方法 1: 使用 clawhub 命令
clawhub list

# 方法 2: 直接查看目录
ls ~/.openclaw/workspace/skills/
```

---

## 工作流程

```
1. 理解用户需求 → "我需要监控天气"
2. 提取关键词 → "weather", "monitor", "forecast"
3. 搜索 ClawHub → clawhub search "weather monitor"
4. 列出相关 Skills（含下载量/stars）
5. 推荐最合适的 Skill
6. 安装后验证是否成功 ← 关键步骤！
```

---

## 输出格式

搜索结果应该包含：

| 信息项 | 说明 |
|--------|------|
| Skill 名称 | 技能标识符 |
| 简短描述 | 中文描述功能 |
| 下载量 | 社区活跃度指标 |
| Stars 数 | 质量评分 |
| 状态 | ✅ 已安装 / ❌ 未安装 |

### 示例输出

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

## 实战示例

### 示例 1: 搜索加密货币监控技能

**用户需求**: "有什么 skill 可以帮我监控加密货币价格？"

**执行流程**:

```bash
# 1. 搜索
clawhub search "crypto price monitor"

# 2. 结果展示
🔍 "加密货币价格监控" 结果：

1. crypto-tracker
   描述：加密货币价格追踪和提醒
   下载：2,345 | Stars: 28 | ❌ 未安装
   → 推荐安装

# 3. 安装
clawhub install crypto-tracker

# 4. 验证安装
ls ~/.openclaw/workspace/skills/crypto-tracker/SKILL.md
```

### 示例 2: 品牌相关技能搜索

**用户需求**: "我需要一个能生成品牌报告的 skill"

**执行流程**:

```bash
# 1. 搜索
clawhub search "brand report generation"

# 2. 分析结果
# - 看下载量判断社区认可度
# - 看 stars 判断质量
# - 检查是否已安装避免重复

# 3. 推荐最优方案
# 4. 安装并验证
```

---

## 最佳实践

### ✅ 推荐做法

1. **先搜索再推荐** - 不要凭空猜测有哪些技能
2. **展示统计数据** - 下载量和 stars 帮助判断质量
3. **标注安装状态** - 避免重复安装
4. **安装后必须验证** - 这是 v1.0.1 新增的重要步骤
5. **提供完整命令** - 让用户可以直接复制执行

### ⚠️ 注意事项

1. **验证是关键** - `clawhub install` 可能失败而不报错
2. **区分已安装/未安装** - 避免重复操作
3. **中文输出优化** - 对用户友好
4. **考虑上下文** - 根据团队需求推荐合适技能

---

## ClawHub 简介

ClawHub ([clawhub.ai](https://clawhub.ai)) 是 OpenClaw 的技能市场平台，类似于 NPM 但专注于 AI agent 技能。

### 优势

- 🌟 社区共建共享
- 📊 下载量和 stars 公开透明
- 🔧 标准化技能接口
- 🚀 一键安装更新

---

## 在品牌虾团队中的应用

### 使用场景

| 场景 | 操作 |
|------|------|
| 新成员加入 | `/find-skill` 了解团队有哪些工具 |
| 新功能需求 | `/find-skill "品牌报告自动生成"` |
| 技能优化 | 搜索更优替代方案 |
| 排查问题 | `clawhub list` 确认已安装技能 |

### 团队协作建议

1. **常用技能集中管理** - 团队统一安装必要技能
2. **文档化推荐** - 将常用技能添加到本地笔记
3. **定期维护** - 清理无用技能，更新过期技能

---

## 配套命令速查

```bash
# 搜索
clawhub search "<关键词>"

# 查看详情
clawhub inspect <skill-name>

# 安装
clawhub install <skill-name>

# 验证安装
ls ~/.openclaw/workspace/skills/<skill-name>/SKILL.md

# 列出已安装
clawhub list

# 或直接查看
ls ~/.openclaw/workspace/skills/
```

---

*v1.0.1 - 安装验证 + 中文优化*

*最后更新：2026-04-22*
