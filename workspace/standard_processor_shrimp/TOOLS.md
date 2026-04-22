# TOOLS.md - Local Notes

> 🦐 **普通资质代办虾的专属工具配置手册**

---

## Skills 目录

所有技能都安装在 `~/.openclaw/workspace/skills/` 目录下。

| Skill 名称 | 目录 | 用途 |
|-----------|------|------|
| `multi-search-engine-simple` | `/Users/zhu/.openclaw/workspace/skills/multi-search-engine-simple` | 联网搜索（必须使用） |
| `agent-browser-clawdbot` | `/Users/zhu/.openclaw/workspace/skills/agent-browser-clawdbot` | 浏览器自动化（政府网站、线上系统） |
| `self-improving-proactive-agent` | `/Users/zhu/.openclaw/workspace/skills/self-improving-proactive-agent` | 自我改进和主动推进 |
| `skill-finder-cn` | `/Users/zhu/.openclaw/workspace/skills/skill-finder-cn` | 查找和安装新技能 |

---

## 跨虾通信规范（必须遵守！）

### ⚠️ 核心规则
- **与其他龙虾岗位通信时，必须只使用子代理模型 (subagent)**
- 不得在主会话中直接与其他虾的 agentId 进行复杂交互
- 所有跨岗位协作通过 `sessions_spawn` (runtime="subagent") 或 `sessions_send` 执行

### ✅ 正确用法示例

```bash
# 向 4A 普通资质销售虾查询流程单状态
sessions_send(
    sessionKey="standard_sales_shrimp_session",
    message="请问流程单编号 XXX 目前进展到哪一步了？"
)

# 向 6 号售后维系虾移交项目
sessions_send(
    sessionKey="after_sales_shrimp_session",
    message="【项目移交】\n客户：XXX\n项目编号：XXX\n状态：已办结\n附件：完整档案.zip"
)
```

---

## 浏览器操作偏好

### 常用政府网站

| 网站 | URL | 用途 |
|------|-----|------|
| 国家企业信用信息公示系统 | https://www.gsxt.gov.cn | 企业查询、公示信息核验 |
| 政务服务网（各地） | https://www.**.gov.cn | 在线办事、进度查询 |
| 税务局电子税务局 | https://etax.**.chinatax.gov.cn | 税务相关事项办理 |

### 最佳实践
1. 始终使用 `-i --json` 标志获取可交互元素
2. 保存认证状态到 `state save auth.json` 避免重复登录
3. 关键步骤截图留存证据
4. 填写表单前先核对信息准确性

---

## 搜索关键词库

### 资质代办相关政策

| 主题 | 推荐关键词 |
|------|-----------|
| 公司注册 | "注册公司流程 2024", "注册资本认缴制", "公司经营范围登记规范" |
| 食品经营许可 | "食品经营许可证办理流程", "餐饮服务许可证要求" |
| 医疗器械备案 | "二类医疗器械备案材料", "三类医疗器械经营许可" |
| 劳务派遣许可 | "劳务派遣许可证申请条件", "劳务派遣经营许可规定" |

### 地方政策差异

不同地区可能有特殊要求，搜索时加上地名：
- `"北京 注册公司流程"`
- `"上海 食品经营许可证"`
- `"深圳 医疗器械备案"`

---

## SOP 检查表模板位置

所有 SOP 检查表存储在 `~/sop-checklists/` 目录下：

```
~/sop-checklists/
├── 公司注册_33 步清单.md
├── 食品经营许可证_25 步清单.md
├── 医疗器械备案_18 步清单.md
└── ...
```

每次创建流程单时，先根据业务类型选择对应的 SOP 模板。

---

## 归档模板

### 项目档案结构

```
~/archive/{客户名}/{项目编号}/
├── 01_原始材料/          # 客户提供的原始文件
├── 02_提交材料/          # 我们制作并提交的文件
├── 03_沟通记录/          # 与客户、相关部门的沟通截图/记录
├── 04_审批结果/          # 批文、证照扫描件
├── 05_费用明细/          # 收据、发票记录
└── README.md             # 项目概览 + 复盘小结
```

### README 模板

```markdown
# {客户名} - {项目名称}

| 字段 | 内容 |
|------|------|
| 项目编号 | {编号} |
| 客户姓名 | {姓名} |
| 经办虾 | 5A · 普通资质代办虾 |
| 受理日期 | {YYYY-MM-DD} |
| 办结日期 | {YYYY-MM-DD} |
| 整体耗时 | {X}个工作日 |

## 项目概况
{简要描述客户需求和办理内容}

## 关键节点
- {日期}：接收流程单
- {日期}：材料准备完成
- {日期}：提交申请
- {日期}：获得批复
- {日期}：领取证照

## 问题记录
{如有问题，记录解决过程}

## 复盘小结
{经验教训、优化建议}
```

---

## 应急响应联系人

| 情况 | 通知对象 | 通知方式 |
|------|----------|----------|
| 重大政策变动 | 龙虾老板 | sessions_spawn |
| 材料被驳回 | 4A/4B + 客户 | sessions_send |
| 可能延期 (>48h) | 4B 大客户销售虾 | sessions_send |
| 技术故障 | 8 号机动应急虾 | sessions_send |

---

*最后更新：2026-04-22*
