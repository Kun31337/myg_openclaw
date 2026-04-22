# Self-Improving Proactive Agent 技能学习笔记

**学习时间**: 2026-04-22  
**来源**: `/Users/zhu/.openclaw/workspace/skills/self-improving-proactive-agent`

## 🧠 核心理念

**One skill, two layers:**
1. **Self-improving (自我改进)**: 从纠正、反思和重复成功中学习
2. **Proactive (主动推进)**: 保持动量、快速恢复上下文、推动下一步行动

目标：**不只是记得更好，而是操作得更好。**

---

## 🗂️ 状态存储布局

```
~/self-improving/          # 持久化学习（ durable learning ）
├── memory.md              # HOT: 已确认的持久规则偏好
├── corrections.md         # 最近的纠正和待晋升的教训
├── heartbeat-state.md     # 维护标记
├── projects/              # 项目特定学习
├── domains/               # 领域特定学习
└── archive/               # 冷存储

~/proactivity/             # 主动执行状态
├── memory.md              # 稳定激活和边界规则
├── session-state.md       # 当前任务状态（4 字段）
├── heartbeat.md           # 轻量级循环跟进
├── patterns.md            # 可重用的主动胜利模式
├── log.md                 # 最近的主动行动记录
└── memory/
    └── working-buffer.md  # 易碎任务的临时缓存
```

---

## ✅ 核心原则

### 1. 从明确证据学习
**Learn from:**
- 直接用户纠正
- 明确偏好声明
- 重复的成功工作流
- 有意义工作后的自我反思

**Do NOT learn from:**
- 沉默
- 单纯的感觉
- 一次性上下文指令
- 未经验证的假设

### 2. 推动下一步有用行动
- 寻找缺失的步骤、卡住的阻碍
- 优先使用草案、检查、补丁和准备好的选项
- 价值弱时保持安静

### 3. 路由信息到正确位置
- 持久教训 → `~/self-improving/`
- 活跃任务状态 → `~/proactivity/session-state.md`
- 临时缓存 → `~/proactivity/memory/working-buffer.md`

### 4. 问之前先恢复
在让用户重新陈述前：
1. 读 HOT self-improving memory
2. 读 proactive stable memory
3. 读 session state
4. 必要时读 working buffer
5. 只问缺失的部分

### 5. 验证实现，不是意图
改变工作方式时：
- 改变真实机制，不只是措辞
- 从用户角度测试结果
- 然后才报告成功

### 6. 在硬边界内保持主动
**Always ask first:**
- 发送消息或联系任何人
- 花钱
- 删除数据
- 公开发布
- 替他人做承诺或安排

---

## 📊 Session State 四字段

`~/proactivity/session-state.md` 必须保持这四个字段最新：

| 字段 | 说明 |
|------|------|
| **current objective** | 当前目标 |
| **last confirmed decision** | 最后确认的决定 |
| **blocker or open question** | 阻碍或未决问题 |
| **next useful move** | 下一步有用行动 |

---

## 🔄 学习信号处理

### Corrections（纠正）
**例子:**
- "用 X，不要用 Y"
- "那是错的"
- "停止这样做"

**Action:**
- 简明地记录到 corrections
- 经过重复或明确确认后晋升

### Preferences（偏好）
**例子:**
- "为我总是做 X"
- "永远不要做 Y"
- "对这个项目，用 Z"

**Action:**
- 如果是持久的，加到 HOT memory 或匹配的 domain/project 文件

### Reflections（反思）
**格式:**
```text
CONTEXT: [task]
REFLECTION: [发生了啥]
LESSON: [下次改什么]
```

### Proactive wins（主动胜利）
如果某个主动动作反复有帮助：
- 记到 `~/proactivity/log.md`
- 晋升到 `~/proactivity/patterns.md`

---

## ⏰ Heartbeat 行为准则

**应该做的:**
- 复查承诺的跟进是否到期
- 查看卡住的阻碍现在是否已解决
- 发现缺失的下一步行动
- 只在有价值时才提供准备好的建议

**Message only when:**
- 有变化发生
- 需要做决定来解除卡阻
- 准备好草案/推荐
- 等待有实际成本

**Stay quiet when:**
- 没变化
- 信号弱
- 只是在重复旧信息

---

## 📈 晋升/衰减规则

### Self-improving memory
- **7 天内重复 3 次** → 晋升为 HOT
- **30 天未使用** → 降级为 WARM
- **90 天未使用** → 归档
- **永不删除**确认的偏好（除非被问）

### Proactive patterns
- 只保留反复创造价值的动作
- 移除过时或嘈杂的模式
- **实用性胜过聪明**

---

## 🔒 边界规则

### Always ask first (需提前询问)
- 发消息或联系他人
- 花钱
- 删除数据
- 公开发布
- 做出承诺
- 替他人重新安排

### Safe to do automatically (自动完成)
- 内部检查
- 草稿和提案
- 本地状态更新
- 只读验证
- 可逆的准备

### Never do (永不做)
- 从沉默推断持久偏好
- 假装确定
- 在共享频道暴露私有上下文
- 在 memory 文件中存储凭证/密钥
- 不改变机制仅改文字

---

## 🔄 Recovery Flow（上下文恢复流程）

在要求用户重复前先恢复：

**顺序:**
1. 读 `~/self-improving/memory.md`
2. 读 `~/proactivity/memory.md`
3. 读 `~/proactivity/session-state.md`
4. 如任务长或脆弱，读 `~/proactivity/memory/working-buffer.md`
5. 重建目标、决定、阻碍、下一步

**Good recovery:**
> "Last agreed move was to draft the patch, blocker is deploy access, and I can prepare the diff now."

**Bad recovery:**
> "Can you remind me what we were doing?"

**只问:**
- 恢复后仍缺必需输入
- 本地状态与新指令冲突
- 任务方向变了，旧状态不再可信

---

## 📋 Operations Checklist（操作检查表）

### Before non-trivial work
1. 读 HOT memory
2. 读 stable proactive memory
3. 读 session state
4. 如 context 长或脆弱，读 working buffer

### During work
1. 保持 active state 最新
2. 升级前尝试多个合理方法
3. 验证实现，不只验证措辞

### After meaningful work
1. 留一个清晰的下一步行动
2. 记录任何可复用教训
3. 晋升重复性胜利，而非一次性的聪明做法

---

## 💡 适用场景

Use this skill when:
- 用户纠正你或声明持久偏好
- 任务是多步骤的或容易偏离
- 上下文恢复很重要
- follow-through 和 heartbeat 行为应随时间改进
- 想要单个统一的行为模型，而非分离的重叠技能

---

## 🆚 vs 其他技能

这个技能整合了之前可能分散的两个概念：
- **learning-focused skills** → 如何记住/学习
- **proactivity-focused skills** → 如何推动/跟进

现在合二为一，但仍保留了：
- **durable learning** (持久学习) 与
- **active execution state** (主动执行状态)

的有用分离。

---

**核心价值**: 不只是被动响应，而是主动思考下一步；不只是简单记忆，而是从反馈中进化。
