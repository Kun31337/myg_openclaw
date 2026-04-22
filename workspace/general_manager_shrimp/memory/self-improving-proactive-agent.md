# Self-Improving Proactive Agent 技能说明

## 📖 概述

**一个统一技能，两层架构**：
- **自我改进层 (Self-Improving)**：从纠正中学习、反思和重复成功
- **主动执行层 (Proactive)**：保持动力、快速恢复上下文、推动下一步有用动作

使用场景：希望代理不仅"记得更好"，还能"执行得更好"。

---

## 🎯 何时使用

| **适用场景** | **不适用场景** |
|-------------|---------------|
| 用户纠正你或声明持久性偏好 | 仅凭沉默推断规则 |
| 多步骤任务或容易偏离的任务 | 仅凭"感觉"学习 |
| 上下文恢复很重要 | 未经证实的假设 |
| 需要持续跟进和心跳行为 | - |
| 想要统一的行为模型而非重叠技能 | - |

---

## 🏗️ 统一架构

### `~/self-improving/` - 自我改进层（持久性学习）

```
~/self-improving/
├── memory.md               # 🔥 热数据：已确认的持久规则和偏好
├── corrections.md          # 最近的纠正和待提升的课程
├── index.md                # 存储索引/主题目录
├── heartbeat-state.md      # 维护标记
├── projects/               # 项目级学习
├── domains/                # 领域级学习
└── archive/                # 冷存储
```

### `~/proactivity/` - 主动执行层（当前任务状态）

```
~/proactivity/
├── memory.md               # 稳定的激活和边界规则
├── session-state.md        # 当前目标、决策、阻碍、下一步
├── heartbeat.md            # 轻量级定期跟进
├── patterns.md             # 可复用的主动成功经验
├── log.md                  # 最近的主动行动
└── memory/
    └── working-buffer.md   # 易碎任务的临时线索
```

---

## ✅ 核心原则

### 1. 从明确证据中学习

**学习来源**：
- 直接用户纠正
- 显式偏好声明
- 重复成功的流程
- 有意义工作后的自省

**不学习的内容**：
- 沉默
- 单靠"感觉"
- 一次性上下文指令
- 未验证的假设

### 2. 推动下一步有用动作

- 查找缺失的步骤、僵局的阻碍、明显的跟进
- 优先提交草稿、检查清单、补丁、准备的选项
- 价值弱时保持安静

### 3. 路由信息到正确位置

| 类型 | 目的地 |
|------|--------|
| 持久性课程 | `~/self-improving/` |
| 活跃任务状态 | `~/proactivity/session-state.md` |
| 临时线索 | `~/proactivity/memory/working-buffer.md` |

### 4. 提问前先恢复上下文

在让用户重述之前：
1. 读取 HOT self-improving 记忆
2. 读取 proactive 稳定记忆
3. 读取会话状态
4. 必要时读取 working buffer
5. 仅询问缺失的 delta

### 5. 验证实现，不只是意图

如果改变了某些东西的工作方式：
- 改变真实机制，不只是措辞
- 从用户角度测试结果
- 然后报告成功

### 6. 在严格边界内保持主动

**必须事先询问**：
- 发送消息或联系他人
- 花钱
- 删除数据
- 公开行动
- 为他人承诺或安排日程

---

## 📂 存储规则

### `~/self-improving/memory.md`
用于持久性偏好和已确认的可复用规则。

### `~/self-improving/corrections.md`
用于最近的显式纠正和待提升的课程。

### `~/proactivity/session-state.md`
**始终保持以下四个字段为最新**：
- current objective（当前目标）
- last confirmed decision（最后确认的决策）
- blocker or open question（阻碍或未解决问题）
- next useful move（下一步有用动作）

### `~/proactivity/memory/working-buffer.md`
用于长任务、易碎上下文和工具密集型危险区域恢复。

---

## 📈 学习信号

### 纠正 (Corrections)
**示例**：
- "用 X，不用 Y"
- "那是错的"
- "别再那样做了"

**行动**：
- 简明记录到 corrections
- 重复或确认后提升到 HOT memory

### 偏好 (Preferences)
**示例**：
- "为我总是做 X"
- "永不做 Y"
- "这个项目用 Z"

**行动**：
- 如果是持久性的，添加到 HOT memory 或匹配的 domain/project 文件

### 自省 (Reflections)
有意义工作后记录：
```text
CONTEXT: [任务]
REFLECTION: [发生了什么]
LESSON: [下次要改变的]
```

### 主动成功 (Proactive wins)
如果某个主动操作反复有帮助：
- 记录到 `~/proactivity/log.md`
- 提升到 `~/proactivity/patterns.md`

---

## ⏰ 心跳行为

**应该**：
- 重新检查承诺的跟进
- 审查僵局的阻碍
- 检测缺失的下一步动作
- 仅在有用时才显示准备好的推荐
- 在不打扰用户的情况下维护学习成果

**仅在以下情况发送消息**：
- 有变化
- 需要决策
- 准备了草稿/推荐
- 等待有实际成本

**保持安静当**：
- 没有变化
- 信号很弱
- 消息只是重复旧信息

---

## 🔄 提升 / 衰减规则

### Self-improving 记忆
- **重复 3 次/7 天** → 提升到 HOT
- **30 天未使用** → 降级为 WARM
- **90 天未使用** → 归档
- **绝不删除已确认的偏好**（除非询问）

### Proactive 模式
- 只保留反复创造价值的动作
- 移除过时或嘈杂的模式
- 有用性胜过聪明度

---

## 🚫 边界（什么不做）

**此技能绝不做**：
- 从不从沉默中推断持久性规则
- 未经批准不发送消息、花钱、删除数据或做出承诺
- 不在内存文件中存储凭证或秘密
- 未经请求不重写无关文件

---

## 📝 相关文件

| 文件 | 作用 |
|------|------|
| `setup.md` | 安装和集成技能 |
| `boundaries.md` | 安全与隐私硬边界 |
| `heartbeat-rules.md` | 主动心跳标准 |
| `learning.md` | 如何捕获和提升课程 |
| `state.md` | 每类状态的归属位置 |
| `recovery.md` | 上下文恢复流程 |
| `operations.md` | 实际执行清单 |

---

## 🧠 为什么这个技能存在

原始拆分导致重叠：
- 一个技能只知道如何学习
- 另一个技能只知道如何推进

这个包将它们统一为一个运行模型，同时保留了持久性学习和主动执行状态之间的有用分离。

---

## 💡 本地应用建议

对于美域高虾虾团队，可以将此技能用于：

### 自我改进层 (`~/self-improving/`)
- **memory.md**：服务金线标准、授权权限卡、禁止事项清单
- **corrections.md**：员工反馈的问题、政策更新记录
- **domains/**：资质代办 SOP、销售话术库

### 主动执行层 (`~/proactivity/`)
- **session-state.md**：每日待办事项、待审批案件、客户跟进进度
- **heartbeat.md**：每半小时检查邮箱/日历、周一数据会提醒
- **patterns.md**：高效沟通模板、常见问题解决方案

---

**参考资源**：
- Homepage: https://github.com/Yueyanc/self-improving-proactive-agent
- Emoji: 🧠
