# OpenClaw Enterprise Multi-Agent Platform

> 企业级分布式 AI Agent 协作平台 · 基于 OpenClaw 框架构建的智能运营体系

---

## 📖 项目概述

**OpenClaw** 是一个高性能的分布式 AI Agent 编排平台，通过模块化设计实现多角色协同作业。本项目部署了 **13 个专业化业务代理（Agent）**，覆盖从获客、销售、运营到售后全流程的企业数字化转型场景。

### 核心特性

- 🏗️ **微服务架构** - 每个 Agent 独立运行，支持弹性扩展
- 🔐 **零信任安全** - API Key 统一通过环境变量管理
- 🤝 **跨平台集成** - 飞书 Lark 原生 WebSocket 连接
- ⚡ **高并发处理** - 单模型百万 tokens 上下文窗口
- 📊 **可观测性** - 完整日志链路与状态追踪

---

## 🎯 技术架构

```mermaid
graph TB
    subgraph "接入层"
        Feishu[飞书多渠道]
    end
    
    subgraph "网关层"
        Gateway[Gateway 18789]
        Auth[Token 认证]
        Bind[路由绑定规则]
    end
    
    subgraph "智能体层"
        Main[主会话 Agent]
        GM[总经理 Agent]
        Brand[品牌营销]
        Lead[获客引擎]
        Video[短视频运营]
        Private[私域运营]
        KA Sales[大客户经理]
        Std Proc[标准流程]
        After[售后服务]
        Data[数据分析]
        Support[全能支持]
    end
    
    subgraph "服务层"
        DashScope[阿里云通义千问]
        Search[搜索引擎聚合]
        Tools[工具生态系统]
    end
    
    Feishu --> Gateway
    Gateway --> Auth & Bind
    Auth --> Main & GM
    Main --> AgentList
    GM --> AgentList
    AgentList --> Search
    AgentList --> Tools
    AgentList --> DashScope
```

### 组件说明

| 层级 | 组件 | 功能描述 |
|------|------|---------|
| **Gateway** | `openclaw gateway` | 消息路由、认证鉴权、连接管理 |
| **Channel** | Feishu (WebSocket) | 企服 IM 集成，支持 DM + Group |
| **Model** | Qwen3.5-Flash | 64K 上下文，1M 长窗口推理 |
| **Agent Runtime** | Node.js 24+ | 运行时环境，支持子 Agent 动态创建 |
| **Memory Store** | Local FS | 持久化记忆与对话历史 |
| **Skills** | Plugin System | 可扩展技能插件系统 |

---

## 📁 目录结构详解

```
~/.openclaw/
│
├── openclaw.json                 # [核心] 主配置文件（见配置指南）
├── .env                          # [敏感] 环境变量（Git ignore）
├── .gitignore                    # Git 忽略规则
│
├── agents/                       # 🧠 代理定义层
│   └── {agent_id}/agent/models.json   # 每个 Agent 的模型上下文
│
├── workspace/                    # 💻 运行时工作区
│   ├── main/                     # 主会话工作空间
│   ├── general_manager_shrimp/   # 总经理代理工作空间
│   ├── branding_shrimp/          # ... 其他 12 个业务线
│   ├── skills/                   # 全局技能库
│   │   └── multi-search-engine-simple/
│   ├── memory/                   # 长期记忆存储
│   └── state/                    # 运行时状态快照
│
├── feishu/                       # 📱 飞书集成数据
│   └── dedup/                    # 消息去重索引
│
├── identity/                     # 👤 设备身份凭证
│   ├── device.json               # 设备注册信息
│   └── device-auth.json          # OAuth 授权令牌
│
├── completions/                  # ✨ 补全缓存
├── tasks/                        # ✅ 异步任务队列
├── subagents/                    # 🔗 子代理进程
├── memory/                       # 🧩 会话记忆片段
├── logs/                         # 📋 系统日志（可选）
│
└── browser/                      # 🌐 浏览器自动化数据
    └── openclaw/user-data/       # Chromium 用户配置
```

### 关键目录职责

| 路径 | 用途 | 安全级别 |
|------|------|---------|
| `agents/*/agent/models.json` | Agent 上下文状态 | 🔴 绝密 |
| `.env` | 所有 API Keys | 🔴 绝密 |
| `workspace/*/memory/` | Agent 个人记忆 | 🟠 内部 |
| `feishu/dedup/` | 消息索引 | 🟢 公开 |
| `identity/device*.json` | 设备凭证 | 🟠 内部 |

---

## ⚙️ 配置管理系统

### Configuration Schema (`openclaw.json`)

#### 1. **Agents Definition**

```jsonc
{
  "agents": {
    "defaults": {
      // Agent 默认行为配置
      "model": { "primary": "qwen3.5-flash" },
      "compaction": { "reserveTokensFloor": 1000000 },
      "workspace": "/Users/zhu/.openclaw/workspace"
    },
    "list": [
      {
        "id": "general_manager_shrimp",
        "name": "General_Manager_Shrimp",
        "workspace": "...",
        "agentDir": "/"
      }
      // ... 13 个 Agent 注册
    ]
  }
}
```

#### 2. **Gateway Settings**

```jsonc
{
  "gateway": {
    "mode": "local",           // local | tailscale | remote
    "port": 18789,
    "bind": "loopback",        // loopback | 0.0.0.0
    "auth": {
      "mode": "token",
      "token": "${OPENCLAW_GATEWAY_TOKEN}"
    },
    "nodes": {
      // 命令白名单/黑名单机制
      "denyCommands": ["camera.snap", "sms.send"]
    }
  }
}
```

#### 3. **Model Providers**

```jsonc
{
  "models": {
    "providers": {
      "custom-dashscope-aliyuncs-com": {
        "baseUrl": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "apiKey": "${DASHSCOPE_API_KEY}",
        "models": [{
          "id": "qwen3.5-flash",
          "contextWindow": 1000000,
          "maxTokens": 64000
        }]
      }
    }
  }
}
```

#### 4. **Channel Integrations**

```jsonc
{
  "channels": {
    "feishu": {
      "enabled": true,
      "connectionMode": "websocket",
      "dmPolicy": "open",
      "groupPolicy": "open",
      "accounts": {
        "default": { "appId": "...", "appSecret": "..." },
        "branding_shrimp": { "appId": "...", "appSecret": "..." }
        // ... 13 个飞书应用实例
      }
    }
  }
}
```

#### 5. **Binding Rules**

定义 Agent 与渠道的映射关系：

```jsonc
{
  "bindings": [
    {
      "agentId": "main",
      "match": { "channel": "feishu", "accountId": "default" }
    },
    {
      "agentId": "branding_shrimp",
      "match": { "channel": "feishu", "accountId": "branding_shrimp" }
    }
  ]
}
```

---

## 🔑 敏感信息管理

### Environment Variables (`.env`)

**警告**: 此文件包含所有生产密钥，**切勿提交到版本控制系统**。

| Variable | 用途 | 来源 |
|----------|------|------|
| `DASHSCOPE_API_KEY` | 通义千问 API | 阿里云百炼平台 |
| `FEISHU_*_APP_ID/SECRET` | 飞书应用凭证 | 飞书开发者后台 |
| `OPENCLAW_GATEWAY_TOKEN` | Gateway 认证 Token | `openclaw configure` 生成 |

#### 获取密钥指南

```bash
# 1. 阿里云 DashScope
# https://bailian.console.aliyun.com/
export DASHSCOPE_API_KEY=sk-your-key-here

# 2. 飞书开放平台
# https://open.feishu.cn/app
# 创建 "应用号" → 开发模式 → 记录 App ID & Secret
export FEISHU_BRANDING_SHRIMP_APP_ID=cli_xxx
export FEISHU_BRANDING_SHRIMP_APP_SECRET=xxx

# 3. OpenClaw Gateway Token
openclaw gateway status --show-token
export OPENCLAW_GATEWAY_TOKEN=c6ca8c...
```

#### 环境变量加载脚本

```bash
#!/bin/bash
# ~/.openclaw/load-env.sh
set -euo pipefail

ENV_FILE="$HOME/.openclaw/.env"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "❌ Error: $ENV_FILE not found!"
  exit 1
fi

source "$ENV_FILE"
export OPENCLAW_CONFIG_DIR="$HOME/.openclaw"

echo "✅ Loaded ${#FEISHU_*[@]} environment variables"
```

---

## 🚀 快速启动

### Prerequisites

| 依赖 | 版本要求 | 安装方式 |
|------|---------|---------|
| Node.js | >= 24.0.0 | `brew install node@24` |
| OpenClaw CLI | >= 2026.4.15 | `npm install -g openclaw` |
| macOS / Linux | Darwin 13+ / Ubuntu 22+ | N/A |

### Start Gateway

```bash
cd ~/.openclaw

# 加载环境变量
source load-env.sh

# 启动网关服务
openclaw gateway start

# 查看运行状态
openclaw gateway status

# 实时日志监控
openclaw gateway logs -f
```

### Verify Deployment

```bash
# 检查所有 Agent 是否就绪
for agent in $(jq -r '.agents.list[].id' openclaw.json); do
  if [[ -f "agents/$agent/agent/models.json" ]]; then
    echo "✓ $agent is ready"
  else
    echo "✗ $agent NOT FOUND"
  fi
done

# 测试 API 连通性
curl -X GET http://localhost:18789/api/status \
  -H "Authorization: Bearer $OPENCLAW_GATEWAY_TOKEN"

# 飞书连接测试
curl -X POST https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal \
  -H "Content-Type: application/json" \
  -d "{\"app_id\":\"$FEISHU_DEFAULT_APP_ID\",\"app_secret\":\"$FEISHU_DEFAULT_APP_SECRET\"}"
```

---

## 👥 Agent 矩阵

### Core Orchestration

| ID | Name | Scope | Workspace |
|----|------|-------|-----------|
| `main` | 主会话代理 | 路由分发、意图识别 | `/workspace/main` |
| `general_manager_shrimp` | 总经理代理 | 全局协调、决策分析 | `/workspace/general_manager_shrimp` |

### Marketing & Growth

| ID | Name | Focus | Key Features |
|----|------|-------|--------------|
| `branding_shrimp` | 品牌虾队 | 品牌形象、内容营销 | SOP 文案、海报联动 |
| `lead_gen_shrimp` | 获客虾队 | 线索挖掘、市场拓展 | 搜索聚合、客户画像 |
| `short_video_shrimp` | 短视频虾队 | 抖音/视频号运营 | 脚本创作、数据跟踪 |

### Sales & Customer Success

| ID | Name | Segment | KPI |
|----|------|---------|-----|
| `key_account_sales_shrimp` | 大客户销售 | 战略客户维护 | CRM 跟进 |
| `standard_sales_shrimp` | 标准销售 | 中小客户转化 | 商机推进 |
| `standard_processor_shrimp` | 标准处理 | 常规流程执行 | 工单处理 |
| `after_sales_shrimp` | 售后服务 | 客户服务、问题解决 | NPS 提升 |

### Operations & Analytics

| ID | Name | Domain | Capabilities |
|----|------|--------|--------------|
| `private_ops_shrimp` | 私域运营 | 社群/企微 | 活动运营、用户分层 |
| `data_analyst_shrimp` | 数据分析 | BI/洞察 | 报表生成、趋势预测 |
| `all_round_support_shrimp` | 全能支持 | 跨部门协同 | 知识检索、培训问答 |

---

## 🛠️ 运维手册

### Log Management

```bash
# 查看系统日志
tail -n 100 ~/.openclaw/logs/gateway.log

# 按 Agent 过滤日志
grep "branding_shrimp" ~/.openclaw/logs/*.log

# 错误统计
grep -c "ERROR" ~/.openclaw/logs/*.log
```

### Health Check

```bash
#!/bin/bash
# check-health.sh

check_agent() {
  local agent=$1
  if pgrep -f "$agent" > /dev/null; then
    echo "✅ $agent running"
  else
    echo "❌ $agent stopped"
  fi
}

check_gateway() {
  if nc -zv localhost 18789 2>&1 | grep -q "succeeded"; then
    echo "✅ Gateway port open"
  else
    echo "❌ Gateway port closed"
  fi
}

check_models() {
  for provider in dashscope; do
    curl -s "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation" \
      -H "Authorization: Bearer $DASHSCOPE_API_KEY" > /dev/null 2>&1 && \
      echo "✅ $provider available" || echo "❌ $provider offline"
  done
}

echo "=== OpenClaw Health Check ==="
check_gateway
check_agent "main"
check_agent "general_manager_shrimp"
check_models
```

### Backup Strategy

```bash
#!/bin/bash
# backup.sh - 每日增量备份

BACKUP_DIR="/backup/openclaw"
DATE=$(date +%Y%m%d)

mkdir -p "$BACKUP_DIR"

# 备份敏感配置
cp ~/.openclaw/.env "$BACKUP_DIR/.env.$DATE.bak"
gpg --symmetric --cipher-algo AES256 "$BACKUP_DIR/.env.$DATE.bak"

# 备份 Agent 记忆
tar -czf "$BACKUP_DIR/memory.$DATE.tar.gz" \
  ~/.openclaw/workspace/*/memory/ \
  ~/.openclaw/memory/

# 保留最近 30 天备份
find "$BACKUP_DIR" -name "*.bak" -mtime +30 -delete
find "$BACKUP_DIR" -name "*.tar.gz" -mtime +30 -delete

echo "✅ Backup completed: $DATE"
```

---

## 🔒 安全最佳实践

### Principle of Least Privilege

```yaml
# Gateway Commands Deny List
denyCommands:
  - camera.snap        # 禁止截图
  - camera.clip        # 禁止录屏
  - screen.record      # 禁止屏幕录制
  - contacts.add       # 禁止联系人操作
  - calendar.add       # 禁止日历写入
  - reminders.add      # 禁止提醒创建
  - sms.send           # 禁止短信发送
  - sms.search         # 禁止短信读取
```

### Credential Rotation Schedule

| 密钥类型 | 轮换周期 | 自动化程度 |
|---------|---------|-----------|
| Gateway Token | 每 30 天 | 手动 |
| DashScope API Key | 每 90 天 | 手动 |
| Feishu App Secret | 每 180 天 | 自动（OAuth 刷新） |

### Audit Checklist

- [ ] 定期检查 `.gitignore` 完整性
- [ ] 每月审计 `.env` 中的密钥有效期
- [ ] 每周清理过期日志文件
- [ ] 每季度更新 `openclaw.json` 配置
- [ ] 每年进行渗透测试

---

## 📈 性能指标

| Metric | Value | Unit |
|--------|-------|------|
| Model Context Window | 1,000,000 | tokens |
| Max Output Tokens | 64,000 | tokens |
| Concurrent Agents | 13 | instances |
| Channel Integration | 1 | platform (Feishu) |
| Latency (P95) | ~2 | seconds |
| Uptime Target | 99.9% | % |

---

## 🔄 版本控制

```
v2026.4.15     # Current stable release
├─ OpenClaw framework core
├─ qwen3.5-flash model integration
└─ 13 Agent configurations
```

### Changelog

**v2026.4.15 (2026-04-21)**
- 初始化部署，13 个业务 Agent 上线
- 飞书通道完整集成
- 环境变量安全管理方案实施

---

## 📞 支持与贡献

| 渠道 | 说明 |
|------|------|
| Issue Tracker | GitHub Issues (internal only) |
| Documentation | This README + inline comments |
| Emergency Contact | Admin team via Feishu |

### Contributing Guidelines

1. Fork the repository (internal access required)
2. Create feature branch: `feature/agent-name`
3. Update `.gitignore` before adding sensitive files
4. Submit PR with clear change description
5. Wait for security review

---

## 📄 License

**Proprietary - Internal Use Only**

© 2026 All rights reserved. Distribution prohibited without written permission.

---

*Last Updated: 2026-04-22T11:35 GMT+8*  
*Document Version: 2.0*
