# Agent Browser (clawdbot) 使用说明

## 技能路径

`/Users/zhu/.openclaw/workspace/skills/agent-browser-clawdbot/SKILL.md`

## 核心功能

基于**可访问性树快照**的无头浏览器自动化工具，专为 AI 代理优化，使用 ref-based 元素选择实现确定性交互。

### 🌐 当何时使用此工具

| agent-browser | built-in browser |
|---------------|------------------|
| ✅ 多步骤自动化工作流 | ✅ 截图/PDF分析 |
| ✅ 确定性的元素选择 | ✅ 视觉检查 |
| ✅ 性能优先 | ✅ 浏览器扩展集成 |
| ✅ 复杂 SPA 应用 | |
| ✅ 会话隔离 | |

---

## 核心工作流程

```bash
# 1. 打开页面并快照
agent-browser open <url>
agent-browser snapshot -i --json

# 2. 解析 JSON refs，然后交互
agent-browser click @e2
agent-browser fill @e3 "text"

# 3. 页面变化后重新快照
agent-browser snapshot -i --json
```

---

## 主要命令

### 🔹 导航控制

```bash
agent-browser open <url>              # 打开 URL
agent-browser back | forward | reload | close   # 后退/前进/刷新/关闭
```

### 🔹 快照（始终使用 `-i --json`）

```bash
agent-browser snapshot -i --json          # 交互式元素，JSON 输出
agent-browser snapshot -i -c -d 5 --json  # + 紧凑模式，深度限制
agent-browser snapshot -s "#main" -i      # 作用域到特定选择器
```

**最佳实践：**
- ✅ 始终使用 `-i` 标志聚焦交互式元素
- ✅ 始终使用 `--json` 便于解析
- ✅ 等待稳定性：`agent-browser wait --load networkidle`

### 🔹 交互操作（基于 Ref）

```bash
agent-browser click @e2                    # 点击
agent-browser fill @e3 "text"              # 填写文本
agent-browser type @e3 "text"              # 逐字输入
agent-browser hover @e4                    # 悬停
agent-browser check @e5 | uncheck @e5      # 勾选/取消勾选
agent-browser select @e6 "value"           # 下拉选择
agent-browser press "Enter"                # 按键
agent-browser scroll down 500              # 滚动
agent-browser drag @e7 @e8                 # 拖拽
```

### 🔹 获取信息

```bash
agent-browser get text @e1 --json         # 获取文本内容
agent-browser get html @e2 --json         # 获取 HTML
agent-browser get value @e3 --json        # 获取输入值
agent-browser get attr @e4 "href" --json  # 获取属性
agent-browser get title --json            # 获取标题
agent-browser get url --json              # 获取 URL
agent-browser get count ".item" --json    # 统计元素数量
```

### 🔹 状态检查

```bash
agent-browser is visible @e2 --json       # 是否可见
agent-browser is enabled @e3 --json       # 是否启用
agent-browser is checked @e4 --json       # 是否勾选
```

### 🔹 等待机制

```bash
agent-browser wait @e2                              # 等待元素出现
agent-browser wait 1000                             # 等待毫秒
agent-browser wait --text "Welcome"                 # 等待文本出现
agent-browser wait --url "**/dashboard"             # 等待 URL 匹配
agent-browser wait --load networkidle               # 等待网络空闲
agent-browser wait --fn "window.ready === true"     # 等待自定义条件
```

---

## 高级功能

### 🔸 会话隔离（多浏览器上下文）

```bash
# 创建独立会话
agent-browser --session admin open site.com
agent-browser --session user open site.com

# 查看所有会话
agent-browser session list

# 通过环境变量指定
AGENT_BROWSER_SESSION=admin agent-browser ...
```

### 🔸 状态持久化（免登录）

```bash
agent-browser state save auth.json    # 保存 cookies/storage
agent-browser state load auth.json    # 加载（跳过登录流程）
```

### 🔸 截图与 PDF

```bash
agent-browser screenshot page.png                  # 普通截图
agent-browser screenshot --full page.png           # 全页截图
agent-browser pdf page.pdf                         # 导出 PDF
```

### 🔸 网络控制

```bash
agent-browser network route "**/ads/*" --abort        # 屏蔽广告
agent-browser network route "**/api/*" --body '{"x":1}' # Mock API
agent-browser network requests --filter api           # 查看请求
```

### 🔸 Cookies 与存储

```bash
agent-browser cookies                     # 查看所有 cookies
agent-browser cookies set name value      # 设置 cookie
agent-browser storage local key           # 获取 localStorage
agent-browser storage local set key val   # 设置 localStorage
```

### 🔸 标签页与 iframe

```bash
agent-browser tab new https://example.com  # 新建标签页
agent-browser tab 2                        # 切换到标签页 2
agent-browser frame @e5                    # 切换到 iframe
agent-browser frame main                   # 返回主文档
```

---

## 实战示例

### 示例 1: 搜索并提取结果

```bash
agent-browser open https://www.google.com
agent-browser snapshot -i --json
# AI 识别搜索框 @e1
agent-browser fill @e1 "AI agents"
agent-browser press Enter
agent-browser wait --load networkidle
agent-browser snapshot -i --json
# AI 识别结果 refs
agent-browser get text @e3 --json
agent-browser get attr @e4 "href" --json
```

### 示例 2: 多会话测试

```bash
# Admin 会话
agent-browser --session admin open app.com
agent-browser --session admin state load admin-auth.json
agent-browser --session admin snapshot -i --json

# User 会话（同时进行）
agent-browser --session user open app.com
agent-browser --session user state load user-auth.json
agent-browser --session user snapshot -i --json
```

---

## Snapshot 输出格式示例

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

## 安装

```bash
npm install -g agent-browser
agent-browser install                     # 下载 Chromium
agent-browser install --with-deps         # Linux: 安装系统依赖
```

---

## 注意事项

- **调试时**：使用 `--headed` 参数查看浏览器界面
- **性能优先**：避免不必要的截图，减少网络请求监听
- **错误处理**：先 snapshot 确认页面状态再执行交互
- **元素定位**：优先使用 aria-ref（通过 `--ref aria` 或 snapshot 的 refs）

---

*最后更新：2026-04-22*
