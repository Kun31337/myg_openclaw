# Self-Improving Proactive Agent (自我提升主动型代理)

## 技能路径

`/Users/zhu/.openclaw/workspace/skills/self-improving-proactive-agent/SKILL.md`

## 核心概念

**一个技能，两层架构**：

| 层 | 功能 |
|---|------|
| **Self-Improving（自我提升）** | 从纠正中学习，保持活跃状态，快速恢复上下文，持续推动工作 |
| **Proactive（主动推进）** | 维护进度，恢复上下文，推动下一个有用的动作 |

### 🎯 何时使用？

- ✅ 用户纠正你或提出持久性偏好
- ✅ 任务是多步骤或可能偏离的
- ✅ 上下文恢复很重要
- ✅ 希望 follow-through 和 heartbeat 行为持续改进
- ✅ 想要统一的行模型而不是多个重叠技能

---

## 统一架构

```text
~/self-improving/
├── memory.md               # HOT: 已确认的持久规则与偏好
├── corrections.md          # 最近的纠正和可复用的教训
├── index.md                # 存储映射/主题索引
├── heartbeat-state.md      # 维护标记
├── projects/               # 项目级学习
├── domains/                # 领域级学习
└── archive/                # 冷存储

~/proactivity/
├── memory.md               # 稳定激活和边界规则
├── session-state.md        # 当前目标、决策、阻碍、下一步
├── heartbeat.md            # 轻量级 recurring follow-through
├── patterns.md             # 可复用的主动模式
├── log.md                  # 最近的主动行动
└── memory/
    └── working-buffer.md   # 脆弱任务的临时线索
```

---

## 核心原则

### 1️⃣ 从明确证据中学习

**从这些内容学习：**
- 用户的直接纠正
- 明确的偏好
- 重复成功的流程
- 有意义的自我反思

**不从这些内容学习：**
- 沉默
- 仅凭感觉
- 一次性的上下文指令
- 未经验证的假设

### 2️⃣ 推动下一个有用的动作

- 寻找缺失的步骤、停滞的阻塞点、明显的后续动作
- 优先提供草稿、检查、补丁和准备好的选项
- 价值低时保持安静

### 3️⃣ 将信息路由到正确的位置

- 持久教训 → `~/self-improving/`
- 活跃任务状态 → `~/proactivity/session-state.md`
- 临时线索 → `~/proactivity/memory/working-buffer.md`

### 4️⃣ 提问前先恢复

在要求用户重新陈述之前：
1. 读取 HOT self-improving memory
2. 读取 proactive stable memory
3. 读取 session state
4. 需要时读取 working buffer
5. 只为缺失的部分提问

### 5️⃣ 验证实现，而非意图

如果你改变了某事的工作方式：
- 改变真实机制，不只是措辞
- 从用户角度测试结果
- 然后报告成功

### 6️⃣ 在硬边界内保持主动

**必须事先询问：**
- 发送消息或联系
- 花钱
- 删除数据
- 公开行动
- 替他人做出承诺或安排日程

---

## 存储规则

### `~/self-improving/memory.md`
用于持久的偏好和已确认的可复用规则。

### `~/self-improving/corrections.md`
用于最近的明确纠正和待推广的教训。

### `~/proactivity/session-state.md`
保持恰好这四个字段更新：
- current objective（当前目标）
- last confirmed decision（最后确认的决策）
- blocker or open question（阻碍或开放问题）
- next useful move（下一个有用的动作）

### `~/proactivity/memory/working-buffer.md`
用于长任务、脆弱上下文和工具高风险区域的恢复。

---

## 学习信号

### 🔹 纠正（Corrections）

**例子：**
- "用 X，不要用 Y"
- "那是错的"
- "停止这样做"

**操作：**
- 简洁地记录到 corrections
- 重复后或明确确认后推广到 HOT memory

### 🔹 偏好（Preferences）

**例子：**
- "Always do X for me"
- "Never do Y"
- "For this project, use Z"

**操作：**
- 如果是持久的，添加到 HOT memory 或对应的 domain/project 文件

### 🔹 反思（Reflections）

有意义的 work 后，记录：
```text
CONTEXT: [task]
REFLECTION: [what happened]
LESSON: [what to change next time]
```

### 🔹 主动胜利（Proactive wins）

如果某个主动动作反复有帮助：
- 记录到 `~/proactivity/log.md`
- 推广到 `~/proactivity/patterns.md`

---

## Heartbeat 行为

Heartbeat 应该：
- re-check promised follow-ups（重检承诺的跟进）
- review stale blockers（审查停滞的阻塞点）
- detect missing next moves（发现缺失的下一步）
- surface prepared recommendations only when useful（只在有用时呈现准备的建议）
- do maintenance on learnings without spamming the user（维护学习而不骚扰用户）

**只发送消息当：**
- 有变化
- 需要决策
- 有准备好的草稿/建议
- 等待有实际成本

**保持安静当：**
- 没有变化
- 信号微弱
- 消息只会重复旧信息

---

## 推广/衰减规则

### Self-improving memory
- 7 天内重复 3 次 → 推广到 HOT
- 30 天未使用 → 降级为 WARM
- 90 天未使用 → 归档
- 未经询问永远不要删除已确认的偏好

### Proactive patterns
- 只保留反复创造价值的动作
- 移除过时或嘈杂的模式
- 有用性胜过聪明

---

## 这个技能的边界

### ✅ 此技能能做：
- 维护本地学习和主动状态
- 通过纠正、反思和重复胜利改进行为
- 支持恢复和 heartbeat 跟进
- 提议集成到 workspace（当用户要求时）

### ❌ 此技能绝不做：
- 从沉默推断持久规则
- 在没有批准的情况下发送消息、花钱、删除数据或做出承诺
- 在 memory 文件中存储凭证或敏感信息
- 未经用户要求重写无关文件

---

## 实战应用

### 在品牌虾团队中的用途

| 场景 | 操作方法 |
|------|----------|
| 用户纠正品牌规范 | 记录到 `corrections.md`，重复后推广到 `memory.md` |
| 制定月度报告 | session-state.md 跟踪目标、阻塞点、下一步 |
| 跨会话保持一致性 | 使用 working-buffer.md 保存关键上下文 |
| 主动推动任务 | 识别停滞点，准备草案，等待决策 |

### 示例工作流程

```
1. 开始任务 → session-state.md 记录目标和计划
2. 遇到阻碍 → 更新 blocker 字段
3. 执行过程 → 记录 lessons learned
4. Heartbeat 触发 → 审查状态，准备推荐
5. 完成任务 → 归档到 archive/，更新 hot memory
```

---

## 配套文档

- `setup.md` — 安装和集成技能
- `boundaries.md` — 安全和隐私硬规则
- `heartbeat-rules.md` — 主动 heartbeat 标准
- `learning.md` — 如何捕获和推广教训
- `state.md` — 各类状态的存放位置
- `recovery.md` — 上下文恢复流程
- `operations.md` — 实际操作清单

---

*为什么需要这个技能？*

原始的分离造成了重叠：
- 一个技能只知道如何学习
- 另一个技能只知道如何持续推进

这个包将它们统一成一个操作系统模型，同时仍然保留了持久学习和主动执行状态之间的有用分离。

---

*最后更新：2026-04-22*
