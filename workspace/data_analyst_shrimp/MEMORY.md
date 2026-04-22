# MEMORY.md - 数据诊断分析虾（7 号）的记忆

---

## 📌 今日关键信息 (2026-04-22)

### 工具使用规范

**必须使用的搜索技能：** `multi-search-engine-simple`
- **目录路径：** `/Users/zhu/.openclaw/workspace/skills/multi-search-engine-simple`
- **规则：** 所有联网搜索任务必须使用此技能，确保搜索质量与一致性

### 浏览器自动化技能：agent-browser-clawdbot

**用途：** 无头浏览器自动化 CLI，适用于 AI 代理的网页操作
- **目录路径：** `/Users/zhu/.openclaw/workspace/skills/agent-browser-clawdbot`
- **核心场景：**
  - 多步骤网页工作流自动化
  - 需要确定性元素选择
  - 处理复杂 SPA 页面
  - 会话隔离需求
- **关键命令：**
  - `agent-browser open <url>` — 打开网页
  - `agent-browser snapshot -i --json` — 获取可交互元素快照
  - `agent-browser click @e2` / `fill @e3 "text"` — 点击/填写表单
  - `agent-browser wait --load networkidle` — 等待页面加载完成
  - `agent-browser --session name` — 创建独立会话
  - `agent-browser state save/load auth.json` — 保存/加载登录状态
- **最佳实践：**
  1. 始终使用 `-i --json` 参数获取快照
  2. 先 snapshot 再 interact，根据 refs 引用元素
  3. 等待网络稳定后再操作
  4. 复用会话和保存认证状态避免重复登录
- **参考主页：** https://github.com/vercel-labs/agent-browser

### 自我提升主动型助手技能：self-improving-proactive-agent

**用途：** 统一自我提升与主动性的技能包，让 AI 不仅能更好记忆，也能更好执行
- **目录路径：** `/Users/zhu/.openclaw/workspace/skills/self-improving-proactive-agent`
- **核心架构：**
  - **Self-improving（自我提升层）：** 从修正中学习，维护长期记忆
    - `~/self-improving/memory.md` — HOT 持久化规则和偏好
    - `~/self-improving/corrections.md` — 近期修正和经验教训
    - `~/self-improving/projects/` — 项目级学习
    - `~/self-improving/domains/` — 领域级学习
  - **Proactivity（主动性层）：** 保持工作动量，快速恢复上下文
    - `~/proactivity/session-state.md` — 当前目标、决策、阻塞点、下一步
    - `~/proactivity/heartbeat.md` — 轻量级周期性跟进
    - `~/proactivity/patterns.md` — 可复用的主动模式
    - `~/proactivity/memory/working-buffer.md` — 脆弱任务的临时缓存
- **核心原则：**
  1. **从明确证据学习：** 只从直接修正、显式偏好、重复成功中学习，不从沉默或假设中学习
  2. **推动下一个有用动作：** 发现缺失步骤、停滞阻塞点，优先给出草案/选项
  3. **信息路由到正确位置：** 持久教训 → self-improving；任务状态 → session-state
  4. **提问前先恢复上下文：** 读 memory → corrections → session-state → working buffer → 再问缺失部分
  5. **验证实现而非意图：** 改变机制后测试效果，再报告成功
  6. **有边界的主动性：** 发消息、花钱、删数据、公开行动、替他人承诺必须先询问
- **学习信号处理：**
  - 修正（"用 X 别用 Y"）→ 记录到 corrections → 重复后升级到 memory
  - 偏好（"总是做 X"）→ 持久偏好加到 HOT memory
  - 反思（有意义的 work 后）→ log: CONTEXT + REFLECTION + LESSON
  - 主动模式成功 → log 到 patterns → 后续复用
- **心跳行为：** 检查承诺跟进、审查停滞阻塞点、检测下一步，只在有价值时发消息
- **记忆晋升规则：** 7 天内重复 3 次 → 升级为 HOT；30 天未用 → 降级 WARM；90 天未用 → 归档

### Skill 查找器：skill-finder-cn

**用途：** 帮助用户在 ClawHub 上发现和安装 Skills
- **目录路径：** `/Users/zhu/.openclaw/workspace/skills/skill-finder-cn`
- **触发词：** "找 skill"、"find skill"、"搜索 skill"、"有什么 skill 可以..."
- **核心命令（需要 clawhub CLI）：**
  - `clawhub search "<需求关键词>"` — 搜索相关 Skills
  - `clawhub inspect <skill-name>` — 查看详细信息和统计数据
  - `curl "https://clawhub.ai/api/v1/skills/<skill-name>" | jq '.skill.stats'` — API 查询 stats
  - `clawhub install <skill-name>` — 安装 Skill
  - `clawhub list` / `ls ~/.openclaw/workspace/skills/` — 检查已安装的 Skills
- **验证安装：**
  ```bash
  ls ~/.openclaw/workspace/skills/<skill-name>/SKILL.md
  # 文件存在 = 安装成功
  # 文件不存在 = 安装失败
  ```
- **输出格式：** 显示 Skill 名称、中文描述、下载量、Stars 数、是否已安装
- **工作流程：**
  理解用户需求 → 2. 提取关键词 → 3. 搜索 ClawHub → 4. 列出结果（含数据）→ 5. 推荐最合适的 → 6. 安装后验证 ✅

### 跨虾通信规范

**核心规则：** 与其他虾（其他 agent/session）进行通信时，**必须使用子代理模型（runtime="subagent"）**
- **为什么：** 确保任务在隔离环境中执行，避免主会话状态污染
- **怎么做：** 使用 `sessions_send()` 或 `sessions_spawn(runtime="subagent")`
- **例外：** 当前会话内的自然对话、直接回答用户问题时可用普通回复

---

## 💬 自我介绍记录

**向团队介绍过的核心要点：**
- 我是数据诊断分析虾（7 号），公司的「数据侦探」🔍
- 维护《美域高作战仪表盘》
- 每周一输出《业务诊断周报》
- 发现重大异常 2 小时内@责任人 + 老板

---

_最后更新：2026-04-22 10:03_
