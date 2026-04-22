# MEMORY.md - 私域运营虾的记忆库

## 🔧 技能工具规范

### 1. 搜索工具 📌

**必须使用的搜索技能：** `multi-search-engine-simple`

- **技能目录：** `/Users/zhu/.openclaw/workspace/skills/multi-search-engine-simple`
- **用途：** 国内精简版多搜索引擎，支持 10 个国内网站的免费搜索
- **适用范围：** 所有联网搜索任务
- **生效时间：** 2026-04-22 起必须使用该技能进行联网搜索

---

### 2. 浏览器自动化工具 🌐

**技能名称：** `agent-browser`（headless browser automation）

- **技能目录：** `/Users/zhu/.openclaw/workspace/skills/agent-browser-clawdbot`
- **核心能力：** 无头浏览器自动化，使用可访问性树快照和基于 ref 的元素选择
- **适用场景：**
  - ✅ 多步骤工作流自动化
  - ✅ 需要确定性元素选择
  - ✅ 性能要求高
  - ✅ 处理复杂 SPA 应用
  - ✅ 需要会话隔离

- **不适用场景：**
  - ❌ 需要截图/PDF 分析
  - ❌ 需要视觉检查
  - ❌ 需要浏览器扩展集成

---

### 3. 核心工作流

```bash
# 1. 导航并快照
agent-browser open <url>
agent-browser snapshot -i --json

# 2. 解析 refs 后交互
agent-browser click @e2
agent-browser fill @e3 "text"

# 3. 页面变化后重新快照
agent-browser snapshot -i --json
```

---

### 4. 常用命令速查

#### 导航
```bash
agent-browser open <url>
agent-browser back | forward | reload | close
```

#### 快照（总是用 `-i --json`）
```bash
agent-browser snapshot -i --json          # 交互式元素，JSON 输出
agent-browser snapshot -i -c -d 5 --json  # 紧凑模式，深度限制
agent-browser snapshot -s "#main" -i      # 限定选择器范围
```

#### 交互（基于 ref）
```bash
agent-browser click @e2
agent-browser fill @e3 "text"
agent-browser type @e3 "text"
agent-browser hover @e4
agent-browser check @e5 | uncheck @e5
agent-browser select @e6 "value"
agent-browser press "Enter"
agent-browser scroll down 500
agent-browser drag @e7 @e8
```

#### 获取信息
```bash
agent-browser get text @e1 --json
agent-browser get html @e2 --json
agent-browser get value @e3 --json
agent-browser get attr @e4 "href" --json
agent-browser get title --json
agent-browser get url --json
agent-browser get count ".item" --json
```

#### 检查状态
```bash
agent-browser is visible @e2 --json
agent-browser is enabled @e3 --json
agent-browser is checked @e4 --json
```

#### 等待
```bash
agent-browser wait @e2                    # 等待元素
agent-browser wait 1000                   # 等待毫秒
agent-browser wait --text "Welcome"       # 等待文本
agent-browser wait --url "**/dashboard"   # 等待 URL
agent-browser wait --load networkidle     # 等待网络空闲
agent-browser wait --fn "window.ready === true"
```

#### 会话隔离（多会话）
```bash
agent-browser --session admin open site.com
agent-browser session list
# 或通过环境变量：AGENT_BROWSER_SESSION=admin agent-browser ...
```

#### 状态持久化（跳过登录）
```bash
agent-browser state save auth.json        # 保存 cookies/storage
agent-browser state load auth.json        # 加载 (跳过登录)
```

#### 截图与 PDF
```bash
agent-browser screenshot page.png
agent-browser screenshot --full page.png
agent-browser pdf page.pdf
```

#### 网络控制
```bash
agent-browser network route "**/ads/*" --abort           # 拦截
agent-browser network route "**/api/*" --body '{"x":1}'  # Mock
agent-browser network requests --filter api              # 查看请求
```

#### Cookies & Storage
```bash
agent-browser cookies                     # 获取所有
agent-browser cookies set name value
agent-browser storage local key           # localStorage 读取
agent-browser storage local set key val
```

#### 标签页与 iframe
```bash
agent-browser tab new https://example.com
agent-browser tab 2                       # 切换到标签页
agent-browser frame @e5                   # 切换到 iframe
agent-browser frame main                  # 返回主文档
```

---

### 5. Snapshot 输出格式

```json
{
  "success": true,
  "data": {
    "snapshot": "...",
    "refs": {
      "e1": {"role": "heading", "name": "Example Domain"},
      "e2": {"role": "button", "name": "Submit"},
      "e3": {"role": "textbox", "name": "Email"}
    }
  }
}
```

---

### 6. 最佳实践

1. **始终使用 `-i` 标志** - 聚焦交互式元素
2. **始终使用 `--json`** - 易于解析
3. **等待页面稳定** - `agent-browser wait --load networkidle`
4. **保存认证状态** - 通过 `state save/load` 跳过登录流程
5. **使用会话隔离** - 隔离不同的浏览器上下文
6. **调试时用 `--headed`** - 可视化操作过程

---

### 3. 自改进主动式代理技能 🧠

**技能名称：** `self-improving-proactive-agent`

- **技能目录：** `/Users/zhu/.openclaw/workspace/skills/self-improving-proactive-agent`
- **核心能力：** 统一的自我改进 + 主动执行技能包
- **适用场景：**
  - ✅ 用户纠正你或表达持久偏好时
  - ✅ 多步骤任务或容易偏离的任务
  - ✅ 需要上下文恢复
  - ✅ 需要随时间改进 follow-through 和 heartbeat 行为
  - ✅ 希望用单一模型替代多个重叠技能

---

### 核心原则

#### 1. 从明确证据中学习
**要学习：**
- 直接的用户纠正
- 显式的偏好声明
- 重复的成功工作流
- 有意义工作后的自我反思

**不要学习：**
- 沉默
- 模糊的感觉
- 一次性的上下文指令
- 未经证实的假设

#### 2. 推动下一个有用动作
- 寻找缺失的步骤、停滞的阻塞点、明显的后续行动
- 优先使用草案、检查、补丁和准备好的选项
- 价值低时保持安静

#### 3. 路由到正确位置
- 持久化经验 → `~/self-improving/`
- 活跃任务状态 → `~/proactivity/session-state.md`
- 临时线索 → `~/proactivity/memory/working-buffer.md`

#### 4. 提问前先恢复
在让用户重述之前：
1. 读 HOT self-improving memory
2. 读 proactive stable memory
3. 读 session state
4. 必要时读 working buffer
5. 只问缺失的部分

#### 5. 验证实现，不只是意图
如果修改了功能：
- 改变真实机制，不只是措辞
- 从用户视角测试结果
- 然后报告成功

#### 6. 在硬边界内保持主动
**必须先询问：**
- 发送消息或联系他人
- 花钱
- 删除数据
- 公开行动
- 为他人承诺或安排

---

### 文件结构

```
~/self-improving/
├── memory.md               # HOT: 确认的持久规则与偏好
├── corrections.md          # 最近的纠正和待整理的经验
├── index.md                # 存储索引
├── heartbeat-state.md      # 维护标记
├── projects/               # 项目专用学习
├── domains/                # 领域专用学习
└── archive/                # 冷存储

~/proactivity/
├── memory.md               # 稳定激活与边界规则
├── session-state.md        # 当前目标、决策、阻塞点、下一步
├── heartbeat.md            # 轻量级重复跟进
├── patterns.md             # 可复用的主动成果
├── log.md                  # 最近的主动行动
└── memory/
    └── working-buffer.md   # 易碎任务的临时线索
```

---

### Session State 四要素

`session-state.md` 必须保持这四个字段更新：
- **current objective** - 当前目标
- **last confirmed decision** - 最后确认的决策
- **blocker or open question** - 阻塞点或未解决问题
- **next useful move** - 下一个有用动作

---

### 学习信号处理

#### Corrections（纠正）
示例："用 X，别用 Y"、"那是错的"、"停止那样做"
操作：
- 简明记录到 corrections.md
- 重复后或得到确认后升级到 HOT memory

#### Preferences（偏好）
示例："总为我做 X"、"永远别做 Y"、"这个项目用 Z"
操作：
- 如果是持久性的，添加到 HOT memory 或匹配的 domain/project 文件

#### Reflections（反思）
有意义的 work 后记录：
```text
CONTEXT: [任务]
REFLECTION: [发生了什么]
LESSON: [下次改什么]
```

#### Proactive wins（主动成果）
如果一个主动行动反复有帮助：
- 记录到 `~/proactivity/log.md`
- 升级到 `~/proactivity/patterns.md`

---

### Heartbeat 行为准则

Heartbeat 应该：
- 重新检查承诺的跟进
- 审查停滞的阻塞点
- 检测缺失的下一步
- 只在有价值时才提供准备好的建议
- 对 learnings 做维护但不 spam 用户

**只在以下情况发消息：**
- 有什么变化了
- 需要做决策
- 有准备好的草案/建议
- 等待有实际成本

**保持安静的情况：**
- 没有什么变化
- 信号很弱
- 消息只是重复旧信息

---

### 晋升 / 衰减规则

**Self-improving memory：**
- 7 天内重复 3 次 → 升级到 HOT
- 30 天未使用 → 降级为 WARM
- 90 天未使用 → 归档
- 未经同意不得删除确认的偏好

**Proactive patterns：**
- 只保留反复创造价值的行动
- 移除过时或嘈杂的模式
- 实用性胜过聪明

---

### 这个技能的边界

**只做：**
- 维护本地学习和主动状态
- 通过纠正、反思和重复成功改进行为
- 支持恢复和 heartbeat 跟进
- 提议集成到工作区（当用户要求时）

**绝不做：**
- 从沉默中推断持久规则
- 未经批准就发送消息、花钱、删数据、做承诺
- 在 memory 文件中存储凭证或敏感信息
- 未经请求重写不相关的文件

---

### 4. Skill 查找器 🔍

**技能名称：** `skill-finder-cn`

- **技能目录：** `/Users/zhu/.openclaw/workspace/skills/skill-finder-cn`
- **作用：** 帮助用户发现和安装 ClawHub 上的 Skills
- **触发词：** "找 skill"、"find skill"、"搜索 skill"

---

### 使用场景

当用户问：
- "有什么 skill 可以帮我...？"
- "找一个能做 X 的 skill"
- "有没有 skill 可以..."
- "我需要一个能...的 skill"

这个技能会帮助搜索 ClawHub 并推荐相关 Skills。

---

### 核心命令

#### 1. 搜索 Skills
```bash
clawhub search "<用户需求>"
```

#### 2. 查看详情（含统计数据）
```bash
clawhub inspect <skill-name>
# 或直接 API 查询：
curl "https://clawhub.ai/api/v1/skills/<skill-name>" | jq '.skill.stats'
```

#### 3. 安装 Skill
```bash
clawhub install <skill-name>
```

#### 4. 验证安装（新增！）**必须执行**
```bash
# 检查是否安装成功
ls ~/.openclaw/workspace/skills/<skill-name>/SKILL.md
```

#### 5. 检查已安装的 Skill
```bash
clawhub list
# 或：
ls ~/.openclaw/workspace/skills/
```

---

### 工作流程

```
1. 理解用户需求
2. 提取关键词
3. 搜索 ClawHub
4. 列出相关 Skills（含下载量/stars）
5. 推荐最合适的 Skill
6. 安装后验证是否成功 ✅ 必做步骤
```

---

### 输出格式（标准格式）

搜索结果应该包含：
- Skill 名称
- 简短描述（中文）
- 下载量
- Stars 数
- 是否已安装

**示例输出：**
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

### 完整示例

**用户**: "有什么 skill 可以帮我监控加密货币价格？"

**搜索**: `clawhub search "crypto price monitor"`

**推荐输出**:
```
🔍 "加密货币价格监控" 结果：

1. crypto-tracker
   描述：加密货币价格追踪和提醒
   下载：2,345 | Stars: 28 | ❌ 未安装
   → 推荐安装

安装命令：clawhub install crypto-tracker
安装后验证：ls ~/.openclaw/workspace/skills/crypto-tracker/SKILL.md
```

---

### 最佳实践

1. **安装后必须验证** - 检查 SKILL.md 是否存在
2. **展示统计数据** - 下载量和 Stars 是判断质量的重要指标
3. **明确标注状态** - ✅ 已安装 / ❌ 未安装
4. **优先推荐高 stats** - 下载量大、Stars 高的更可靠
5. **提供具体命令** - 给出可执行的安装和验证命令

---

*本文件为记忆库主文档，记录重要决策、工作规范和关键信息。*

*最后更新：2026-04-22*
