# TOOLS.md - 私域运营虾的工具箱

_skills define **how** tools work. This file is for **your** specifics — the stuff that's unique to your setup._

---

## 🔧 核心技能列表

### 1. 搜索工具 📌

| 技能名称 | 目录 | 用途 |
|---------|------|------|
| `multi-search-engine-simple` | `/Users/zhu/.openclaw/workspace/skills/multi-search-engine-simple` | 国内精简版多搜索引擎（10 个国内网站） |

**使用规范：** 所有联网搜索任务必须使用该技能

---

### 2. 浏览器自动化 🌐

| 技能名称 | 目录 | 用途 |
|---------|------|------|
| `agent-browser` | `/Users/zhu/.openclaw/workspace/skills/agent-browser-clawdbot` | 无头浏览器自动化，基于可访问性树和 ref 选择 |

**核心能力：**
- ✅ 多步骤工作流自动化
- ✅ 确定性元素选择
- ✅ 会话隔离 & 状态持久化
- ✅ Cookies & Storage 管理
- ✅ 网络请求拦截/Mock

**常用参数组合：** `agent-browser snapshot -i --json`

---

### 3. 自改进主动代理 🧠

| 技能名称 | 目录 | 用途 |
|---------|------|------|
| `self-improving-proactive-agent` | `/Users/zhu/.openclaw/workspace/skills/self-improving-proactive-agent` | 统一自我改进 + 主动执行能力 |

**记忆结构：**
```
~/self-improving/
├── memory.md              # HOT: 确认的持久规则与偏好
├── corrections.md         # 最近的纠正和经验
├── projects/              # 项目专用学习
└── archive/               # 冷存储

~/proactivity/
├── session-state.md       # 当前目标、决策、阻塞点、下一步
├── patterns.md            # 可复用的主动成果
└── log.md                 # 最近的主动行动
```

---

### 4. Skill 查找器 🔍

| 技能名称 | 目录 | 触发词 |
|---------|------|--------|
| `skill-finder-cn` | `/Users/zhu/.openclaw/workspace/skills/skill-finder-cn` | "找 skill" / "find skill" / "搜索 skill" |

**工作流程：**
```bash
clawhub search "<需求>"    # 搜索
clawhub install <name>     # 安装
ls ~/.openclaw/workspace/skills/<name>/SKILL.md  # 验证安装 ✅
```

---

## 🌐 API 密钥与凭证

_⚠️ 敏感信息不在此记录，请通过环境变量或安全 Vault 管理_

### 已配置的服务
| 服务 | 状态 | 备注 |
|------|------|------|
| Feishu (飞书) | ✅ | 已连接，群聊：`oc_06bd0381650c08be8b7819c0e05e9e92` |
| Tongyi Qianwen | ✅ | 模型：`qwen3.5-flash` |
| OpenClaw Gateway | ✅ | 运行时正常 |

---

## 🖥️ 运行环境

| 项目 | 值 |
|-----|-----|
| **主机** | zhu 的 MacBook Pro |
| **OS** | Darwin 23.3.0 (arm64) |
| **Node** | v24.14.0 |
| **Shell** | zsh |
| **时区** | Asia/Shanghai (UTC+8) |

---

## 📡 网络配置

### 可用平台/渠道
- [x] Feishu (飞书)
- [ ] Discord
- [ ] Slack
- [ ] WhatsApp
- [ ] Telegram
- [ ] Signal

### MCP 工具支持
- **企业微信 MCP:** `wecom-mcp-config.yaml` 已配置
  - 通讯录查询 (`wecom-contact-lookup`)
  - 文档管理 (`wecom-doc-manager`)
  - 待办事项 (`wecom-edit-todo`, `wecom-get-todo-list`, `wecom-get-todo-detail`)
  - 会议管理 (`wecom-meeting-create`, `wecom-meeting-manage`, `wecom-meeting-query`)
  - 消息发送 (`wecom-msg`, `wecome-send-template-card`)

---

## 🤖 数字员工清单

| ID | 名称 | 角色 | 状态 |
|----|------|------|------|
| `private_ops_shrimp` | 私域运营虾 | 私域运营专家 | ✅ 激活中 |

---

## 🛠️ 本地工具别名

_如有特殊命令别名或脚本，记录于此_

```bash
# 示例
alias claw-status="openclaw gateway status"
alias claw-start="openclaw gateway start"
```

---

## 📊 监控指标

_关键系统指标的阈值和告警规则_

| 指标 | 正常范围 | 告警阈值 |
|------|----------|----------|
| Gateway 状态 | Running | Stopped/Restarting |
| API 调用次数 | < 正常水平 80% | > 正常水平 120% |
| 响应延迟 | < 2s | > 5s |

---

## 🔄 维护日志

- **2026-04-22** - 完成初始工具配置和技能梳理
