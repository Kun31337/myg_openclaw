# TOOLS.md - Local Notes (虾系专用)

## 📹 视频制作工具

### 拍摄设备
- **手机**: iPhone 15 Pro Max (主摄)
- **灯光**: 环形补光灯 + 柔光箱
- **收音**: 无线领夹麦克风

### 剪辑软件
- **移动端**: 剪映 (CapCut)
- **PC 端**: Adobe Premiere / Final Cut Pro

### 素材库位置
```
~/videos/
├── raw/              # 原始素材
├── drafts/           # 草稿工程
├── exports/          # 导出成品
└── templates/        # 模板文件
```

---

## 🔍 联网搜索配置

**强制使用技能**: `multi-search-engine-simple`
- **目录**: `/Users/zhu/.openclaw/workspace/skills/multi-search-engine-simple`
- **用途**: 所有内容创作相关的网络检索
- **注意事项**: 不可使用其他搜索工具替代

---

## 🌐 浏览器自动化

**技能**: `agent-browser`
- **目录**: `/Users/zhu/.openclaw/workspace/skills/agent-browser-clawdbot`
- **主要场景**:
  - 抖音/B 站数据抓取
  - 竞品账号分析
  - 热点话题监控

### 常用命令
```bash
agent-browser open <url>
agent-browser snapshot -i --json
agent-browser click @ref
agent-browser fill @ref "text"
agent-browser --session shrimp_session
```

### 状态保存
```bash
agent-browser state save --path ~/browser/state.json
agent-browser state load --path ~/browser/state.json
```

---

## 💬 飞书集成

### 群聊配置
- **群组 ID**: `oc_06bd0381650c08be8b7819c0e05e9e92`
- **用户 ID**: `ou_3d95f90eec4c4da94f0ba83231a886e9`
- **功能**: 团队沟通、进度同步

### Feishu API Token
*(存储在环境变量中，不在此记录)*

---

## 📊 数据分析对接

### 与 7 号数据虾协作
- **定期报告**: 每周视频数据复盘
- **异常预警**: 完播率骤降通知
- **需求对接**: 通过 `sessions_spawn` 子代理请求

---

## 🧩 工作流自动化

### Heartbeat 检查项
```json
{
  "daily": [
    "检查新评论回复",
    "查看今日播放量",
    "监控热点话题"
  ],
  "weekly": [
    "输出数据周报",
    "策划下周选题",
    "优化脚本模板"
  ]
}
```

### Cron 任务建议
| 时间 | 任务 |
|------|------|
| 每日 9:00 | 检查昨日数据 |
| 每周一 10:00 | 更新选题计划 |
| 每周五 18:00 | 输出周报复盘 |

---

## 🔐 安全须知

**权限边界**:
- ✅ 自主：常规视频内容生产
- ⚠️ 报备：涉及费用支出 (>200 元)
- ❓ 请示：战略级决策/事件营销

**不要做**:
- ❌ 未经同意发送外部消息
- ❌ 擅自承诺客户特殊服务
- ❌ 修改核心业务 SOP

---

## 📝 快速参考

### sessions_spawn 示例
```bash
# 向 0 号汇报
sessions_spawn(
  task="汇报本周视频数据:\n- 发布 3 条\n- 平均完播率 45%\n- 转化咨询 12 个",
  runtime="subagent",
  agentId="General_Manager_Shrimp"
)

# 与 7 号协作
sessions_spawn(
  task="请求分析上周视频数据，重点关注完播率流失点",
  runtime="subagent",
  agentId="Data_Analyst_Shrimp"
)
```

*最后更新：2026-04-22*
