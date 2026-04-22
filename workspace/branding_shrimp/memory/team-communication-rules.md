# 品牌虾团队通信规则

## ⚠️ 重要通信规则

### 与团队成员通信
**规则**：与其他虾（团队内其他 Agent）进行通信时，**必须只用子代理模型**。

---

## 🧠 子代理模型 vs 主会话

| 场景 | 使用方式 |
|------|----------|
| 直接对话用户（主人） | 主会话模型 |
| **与团队其他虾协作** | **子代理模型 (subagent)** ← 必须 |
| 跨 session 消息传递 | `sessions_send` |
| 启动独立任务进程 | `sessions_spawn` |

---

## 📡 通信方法

### 1. 发送消息到已有 session

```bash
sessions_send(
    sessionKey: "目标 session",
    message: "要发送的内容"
)
```

### 2. 启动新 subagent

```bash
sessions_spawn(
    task: "任务描述",
    runtime: "subagent",
    agentId: "目标 agentID",
    mode: "session"  # 或 "run"
)
```

### 3. 管理 subagent

```bash
subagents(action="list")   # 查看所有子代理
subagents(action="steer")  # 指挥子代理
subagents(action="kill")   # 终止子代理
```

---

## ✅ 正确做法

```
❌ 错误：在同一个会话中直接与对方说话
✅ 正确：使用 sessions_send 发送到对方的 session
✅ 正确：启动 subagent 处理协作任务
```

---

## 💡 为什么？

1. **隔离性** - 每个代理有独立的上下文和记忆
2. **可追溯** - 清晰的通信路径和记录
3. **稳定性** - 避免会话污染和上下文混乱
4. **效率** - 并行处理多个协作任务

---

*最后更新：2026-04-22*
