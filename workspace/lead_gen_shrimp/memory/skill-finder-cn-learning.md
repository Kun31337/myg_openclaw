# Skill Finder (中文) 技能学习笔记

**学习时间**: 2026-04-22  
**来源**: `/Users/zhu/.openclaw/workspace/skills/skill-finder-cn`  
**触发词**: 找 skill、find skill、搜索 skill

---

## 🎯 功能定位

帮助用户发现和安装 **ClawHub Skills**，当用户问：
- "有什么 skill 可以帮我...？"
- "找一个能做 X 的 skill"
- "有没有 skill 可以..."
- "我需要一个能...的 skill"

---

## 🔍 ClawHub CLI 核心命令

### 1. 搜索 Skills
```bash
clawhub search "<用户需求>"
```

### 2. 查看详情（含统计数据）
```bash
clawhub inspect <skill-name>
```

或 API 直接查询 stats：
```bash
curl "https://clawhub.ai/api/v1/skills/<skill-name>" | jq '.skill.stats'
```

### 3. 安装 Skill
```bash
clawhub install <skill-name>
```

### 4. 验证安装 ✅（重要！）
```bash
# 检查是否安装成功
ls ~/.openclaw/workspace/skills/<skill-name>/SKILL.md

# 如果文件存在 = 成功
# 如果不存在 = 失败
```

### 5. 检查已安装的 Skill
```bash
clawhub list

# 或者
ls ~/.openclaw/workspace/skills/
```

---

## 📋 标准工作流程

```
1. 理解用户需求
2. 提取关键词
3. 搜索 ClawHub → clawhub search "<关键词>"
4. 列出相关 Skills（含下载量/stars）
5. 推荐最合适的 Skill
6. 安装后验证是否成功 ← 关键步骤！
```

---

## 💡 输出格式优化版

搜索结果应该包含：
- ✅ Skill 名称
- ✅ 简短描述（中文）
- ✅ 下载量
- ✅ Stars 数
- ✅ 是否已安装

**示例输出**:
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

## 📝 实际示例

**用户问题**: "有什么 skill 可以帮我监控加密货币价格？"

**执行步骤**:
```bash
# 1. 搜索
clawhub search "crypto price monitor"

# 2. 推荐结果
🔍 "加密货币价格监控" 结果：

1. crypto-tracker
   描述：加密货币价格追踪和提醒
   下载：2,345 | Stars: 28 | ❌ 未安装
   → 推荐安装

# 3. 安装 + 验证
clawhub install crypto-tracker
ls ~/.openclaw/workspace/skills/crypto-tracker/SKILL.md  # ✅ 验证
```

---

## ⚠️ 重要注意事项

### v1.0.1 新增特性
- ✅ 安装后验证步骤（必须执行！）
- ✅ 搜索结果显示下载量/stars
- ✅ 检查是否已安装（避免重复安装）
- ✅ 中文输出优化

### 最佳实践
1. **永远不要假设安装成功** — 用 `ls .../SKILL.md` 验证
2. **显示统计信息** — 下载量和 stars 帮助判断质量
3. **优先推荐热门且评分高的**
4. **已安装的 Skill 要明确标识** — 避免重复安装
5. **API 查询 stats** 比 inspect 更快更直接

---

## 🔗 相关链接

- **ClawHub 官网**: https://clawhub.ai
- **API 端点**: https://clawhub.ai/api/v1/skills/<skill-name>
- **Skill 仓库**: `~/.openclaw/workspace/skills/`

---

**核心价值**: 降低 Skill 发现门槛，让用户能快速找到需要的工具，并确保安装成功！🔍✨
