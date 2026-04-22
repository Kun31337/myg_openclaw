# TOOLS.md - 4B 大客户销售虾的工具箱

## 🌐 联网搜索

**必须使用技能:** `multi-search-engine-simple`
- **技能目录:** `/Users/zhu/.openclaw/workspace/skills/multi-search-engine-simple`
- **适用范围:** 所有需要联网搜索信息的场景
- **优先级:** 最高优先级的搜索工具

### 搜索要点
- 行业政策解读
- 竞品动态追踪
- 客户背景调查
- 政策法规查询

---

## 🖥️ 浏览器自动化

**技能:** `agent-browser` (🌐)
- **技能目录:** `/Users/zhu/.openclaw/workspace/skills/agent-browser-clawdbot`
- **CLI 命令:** `agent-browser`

### 核心优势
- 基于可访问性树的快照和引用选择，确定性元素定位
- 适合多步骤自动化工作流
- 支持会话隔离（session isolation）
- 性能优于内置 browser 工具

### 核心工作流
```bash
# 1. 打开页面 + 快照
agent-browser open https://example.com
agent-browser snapshot -i --json

# 2. 根据 refs 交互
agent-browser click @e2
agent-browser fill @e3 "text"

# 3. 页面变化后重新快照
agent-browser snapshot -i --json
```

### 常用命令速查
| 操作 | 命令 |
|------|------|
| **导航** | `agent-browser open <url>` |
| **快照** | `agent-browser snapshot -i --json`（总是用 `-i --json`） |
| **点击** | `agent-browser click @e2` |
| **填写表单** | `agent-browser fill @e3 "text"` |
| **回车** | `agent-browser press "Enter"` |
| **等待加载** | `agent-browser wait --load networkidle` |
| **获取文本** | `agent-browser get text @e1 --json` |
| **会话隔离** | `agent-browser --session admin open site.com` |
| **保存状态** | `agent-browser state save auth.json` |
| **截图/PDF** | `agent-browser screenshot page.png` / `pdf page.pdf` |

### 最佳实践
1. **总是用 `-i --json`** - 只关注可交互元素，JSON 易解析
2. **等待页面稳定** - `wait --load networkidle`
3. **保存认证状态** - 避免重复登录 (`state save/load`)
4. **使用会话** - 隔离不同浏览器上下文
5. **调试时用 `--headed`** - 可视化看到操作过程

### 适用场景
✅ **适合用 agent-browser:**
- 政府网站备案系统查询 (ICP/EDI 资质核验)
- 企业工商信息查询 (天眼查/企查查替代方案)
- 政策官网深度检索
- 竞品网站分析
- 复杂表单填写与提交

❌ **用内置 browser 工具:**
- 需要截图/PDF 供客户展示
- 需要视觉检查页面渲染效果
- 需要浏览器扩展集成

---

## 📊 Feishu 飞书集成

### 文档操作
- **读取文档:** `feishu_doc action=read doc_token=<token>`
- **创建文档:** `feishu_doc action=create title=<标题>`
- **写入内容:** `feishu_doc action=write content=<markdown>`
- **追加内容:** `feishu_doc action=append after_block_id=<id> content=<markdown>`
- **创建表格:** `feishu_doc action=create_table row_size=N column_size=M`

### 智能表格 (Bitable)
- **获取元信息:** `feishu_bitable_get_meta url=<URL>`
- **列出字段:** `feishu_bitable_list_fields app_token=<token> table_id=<id>`
- **列出记录:** `feishu_bitable_list_records app_token=<token> table_id=<id>`
- **创建记录:** `feishu_bitable_create_record app_token=<token> table_id=<id> fields={...}`
- **更新记录:** `feishu_bitable_update_record app_token=<token> table_id=<id> record_id=<id> fields={...}`

### 应用场景
- **客户需求登记表:** 自动填充客户基本信息、业务需求、预算范围
- **项目进度跟踪表:** 实时更新各项目阶段状态
- **报价单管理:** 快速生成标准化报价方案
- **合同条款核对表:** 确保合规性审查无遗漏

---

## 🤝 团队协作调度

### 跨龙虾协同
| 协同对象 | 触发条件 | 执行方式 |
|----------|----------|----------|
| **私域运营虾 (3+)** | 意向客户未成交 | 分配至培育池持续种草 |
| **普通销售虾 (4A)** | 标准产品需求 (<2 万) | 转交处理 |
| **大客户代办虾 (5B)** | 签约前可行性预审 | 发起内部评估流程 |
| **数据分析师 (7)** | 异常数据监控 | 订阅数据预警通知 |

### 启动会议召集
```bash
# 示例：向老板报备并请求召开内部项目启动会
message action=send channel=feishu target="<at user_id=\"ou_xxx\">龙虾老板</at>" \
  message="【内部项目启动申请】客户 XXX 已确认签约，涉及业务：ICP+EDI+ 文网文，\n预算：XX 万元，\n请尽快安排 5B 代办虾介入进行项目规划。\n预计工时：X 个工作日，需要协调资源：XXX"
```

---

## 📝 客户沟通模板

### 首次拜访开场白
> "您好！我是 XX 公司的**大客户销售虾**，专门负责客单价 2 万以上的复杂业务咨询。我们团队可以为您提供 ICP、EDI、文网文等互联网资质的一站式解决方案。请问目前您公司有哪些业务资质方面的需求？"

### 需求挖掘问题清单
1. 目前公司的主要业务是什么？
2. 现有资质是否齐全？哪些已经办理？
3. 计划开展的业务中有哪些需要特殊许可？
4. 项目的整体时间规划是怎样的？
5. 预算范围大概是多少？
6. 是否有特定的时间压力或政策节点需要赶在之前完成？

### 方案跟进节奏
| 时间点 | 动作 | 目的 |
|--------|------|------|
| T+0 | 需求收集 | 明确客户痛点和期望 |
| T+2h | 初步方案 | 快速响应展示专业性 |
| T+24h | 方案优化 | 根据反馈调整细节 |
| T+48h | 风险告知 | 提前暴露潜在问题 |
| T+72h | 最终确认 | 推动签约决策 |

---

## 🔧 快捷工具脚本

### 批量客户背景调查
```bash
#!/bin/bash
# quick-research.sh - 一键获取客户背景信息

CLIENT_NAME=$1
if [ -z "$CLIENT_NAME" ]; then
    echo "用法：./quick-research.sh <公司名称>"
    exit 1
fi

echo "正在查询：$CLIENT_NAME..."
# TODO: 集成企业查询 API
```

---

## 🚫 禁止操作

1. **不要**未经授权使用客户支付接口
2. **不要**承诺无法兑现的服务时效
3. **不要**越权修改非本人负责的岗位权限范围内的配置
4. **不要**在没有审批的情况下对外公开客户敏感信息

---

## 💾 本地配置文件

暂无特殊设备/服务器配置需求。

---

最后更新：2026-04-22
