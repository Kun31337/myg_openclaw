# Agent Browser (clawdbot) 技能说明

## 📖 概述

**agent-browser** 是一个专为 AI 代理优化的无头浏览器自动化工具 CLI，基于可访问性树快照和引用驱动的确定性元素选择。

---

## 🆚 何时使用 vs 内置 browser 工具

| **使用 agent-browser** | **使用内置 browser** |
|------------------------|----------------------|
| 多步骤自动化工作流 | 需要截图/PDF 用于分析 |
| 需要确定性元素选择 | 视觉检查需求 |
| 性能要求高 | 浏览器扩展集成 |
| 复杂单页应用 (SPA) | - |
| 需要会话隔离 | - |

---

## ⚡ 核心工作流

```bash
# 1. 导航 + 快照
agent-browser open https://example.com
agent-browser snapshot -i --json

# 2. 解析 refs 并交互
agent-browser click @e2
agent-browser fill @e3 "text"

# 3. 页面变化后重新快照
agent-browser snapshot -i --json
```

---

## 🔑 关键命令

### 导航控制
```bash
agent-browser open <url>                 # 打开 URL
agent-browser back | forward | reload    # 前进/后退/刷新
agent-browser close                      # 关闭
```

### 快照（始终用 `-i --json`）
```bash
agent-browser snapshot -i --json               # 交互式元素，JSON 输出
agent-browser snapshot -i -c -d 5 --json       # +紧凑模式，深度限制 5
agent-browser snapshot -s "#main" -i --json    # 指定作用域
```

### 元素交互（基于 Ref）
```bash
agent-browser click @e2                # 点击
agent-browser fill @e3 "text"          # 填充输入框
agent-browser type @e3 "text"          # 输入文本
agent-browser hover @e4                # 悬停
agent-browser check @e5 | uncheck @e5  # 勾选/取消勾选
agent-browser select @e6 "value"       # 下拉选择
agent-browser press "Enter"            # 按键
agent-browser scroll down 500          # 滚动
agent-browser drag @e7 @e8             # 拖拽
```

### 获取信息
```bash
agent-browser get text @e1 --json      # 获取文本
agent-browser get html @e2 --json      # 获取 HTML
agent-browser get value @e3 --json     # 获取值
agent-browser get attr @e4 "href"      # 获取属性
agent-browser get title --json         # 获取标题
agent-browser get url --json           # 获取 URL
agent-browser get count ".item"        # 计数
```

### 状态检查
```bash
agent-browser is visible @e2 --json    # 可见性
agent-browser is enabled @e3 --json    # 是否启用
agent-browser is checked @e4 --json    # 是否勾选
```

### 等待机制
```bash
agent-browser wait @e2                  # 等待元素出现
agent-browser wait 1000                 # 等待毫秒数
agent-browser wait --text "Welcome"     # 等待特定文本
agent-browser wait --url "**/dashboard" # 等待 URL 匹配
agent-browser wait --load networkidle   # 等待网络空闲
agent-browser wait --fn "window.ready"  # 自定义函数
```

---

## 🧩 会话管理（浏览器隔离）

```bash
# 创建独立会话
agent-browser --session admin open site.com
agent-browser --session user open site.com

# 查看会话列表
agent-browser session list

# 或通过环境变量
AGENT_BROWSER_SESSION=admin agent-browser ...
```

**用途**：同时运行多个浏览器上下文，如测试管理员 vs 普通用户权限。

---

## 💾 状态持久化

```bash
# 保存认证状态（cookies/storage）
agent-browser state save auth.json

# 加载跳过登录
agent-browser state load auth.json
```

**用途**：避免重复登录流程。

---

## 📸 截图 & PDF

```bash
agent-browser screenshot page.png           # 当前视口截图
agent-browser screenshot --full page.png    # 全页面截图
agent-browser pdf page.pdf                   # 导出 PDF
```

---

## 🌐 网络控制

```bash
# 路由拦截
agent-browser network route "**/ads/*" --abort        # 阻断广告
agent-browser network route "**/api/*" --body '{"x":1}' # Mock 响应

# 查看请求
agent-browser network requests --filter api
```

---

## 🍪 Cookies & 存储

```bash
agent-browser cookies                     # 获取所有 cookies
agent-browser cookies set name value      # 设置 cookie
agent-browser storage local key           # 读取 localStorage
agent-browser storage local set key val   # 写入 localStorage
```

---

## 📑 标签页与 Iframe

```bash
agent-browser tab new https://example.com  # 新建标签页
agent-browser tab 2                         # 切换到标签页 2
agent-browser frame @e5                     # 进入 iframe
agent-browser frame main                    # 返回主文档
```

---

## 📊 快照输出格式

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

**Ref 规则**：使用 `@e1`, `@e2` 等引用标识元素，确保确定性选择。

---

## ✅ 最佳实践

1. **始终用 `-i` 和 `--json` 标志** - 聚焦交互元素，易于解析
2. **等待稳定性** - `agent-browser wait --load networkidle`
3. **保存认证状态** - 避免重复登录
4. **使用会话隔离** - 不同场景用独立浏览器上下文
5. **调试时加 `--headed`** - 可视化界面便于排查问题

---

## 🎯 示例：搜索并提取结果

```bash
# 打开 Google
agent-browser open https://www.google.com

# 快照识别搜索框
agent-browser snapshot -i --json
# AI 识别出 @e1 为搜索框

# 输入并搜索
agent-browser fill @e1 "AI agents"
agent-browser press Enter

# 等待加载完成
agent-browser wait --load networkidle

# 重新快照获取结果
agent-browser snapshot -i --json
# 提取 @e3 的标题、@e4 的链接
agent-browser get text @e3 --json
agent-browser get attr @e4 "href" --json
```

---

## 🔧 安装

```bash
npm install -g agent-browser
agent-browser install              # 下载 Chromium
agent-browser install --with-deps  # Linux: 加系统依赖
```

---

## 📌 相关资源

- **Skill creator**: Yossi Elkrief ([@MaTriXy](https://github.com/MaTriXy))
- **CLI source**: [Vercel Labs/agent-browser](https://github.com/vercel-labs/agent-browser)
- **Homepage**: https://github.com/vercel-labs/agent-browser
