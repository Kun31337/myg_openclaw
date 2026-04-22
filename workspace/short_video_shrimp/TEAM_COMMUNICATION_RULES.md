# Team Communication Rules - 团队通信规则

**重要规则**:与其他虾（团队成员）进行通信时，必须使用**子代理模型**！

## 如何操作

当需要与其他 agent 通信时：

```bash
# 使用 sessions_send 发送消息到目标会话
sessions_send(
  sessionKey: "目标 agentId",
  message: "你的消息内容",
  timeoutSeconds: 30
)

# 或 spawn 一个子代理会话
sessions_spawn({
  agentId: "目标 agentId",
  task: "任务描述",
  runtime: "subagent",
  mode: "session"
})
```

## 为什么必须使用子代理模型

1. **成本优化**：子代理使用轻量模型，降低 token 消耗
2. **隔离性**：避免主 session 污染，保持上下文清晰
3. **效率提升**：子代理专注单一任务，执行更快

## 适用场景

- ✅ 向总经理 (0 号) 汇报工作
- ✅ 与品牌展示虾 (1 号) 协同内容
- ✅ 与引流获客虾 (2 号) 共享线索
- ✅ 与销售虾 (4A/4B) 确认客户需求
- ✅ 与代办虾 (5A/5B) 同步案件进度
- ✅ 向数据虾 (7 号) 请求分析报告

## 注意事项

- ❌ 不要直接在主 session 中@其他 agent
- ❌ 不要用普通 exec/curl 命令通知同事
- ✅ 统一使用 `sessions_send` 或 `sessions_spawn`

*规则更新时间：2026-04-22*
