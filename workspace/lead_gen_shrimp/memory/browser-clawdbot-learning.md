# Agent-Browser (ClawDBot) 技能学习笔记

**学习时间**: 2026-04-22  
**来源**: `/Users/zhu/.openclaw/workspace/skills/agent-browser-clawdbot`

## 🧠 核心概念

这是一个**无头浏览器自动化工具**，专为 AI 代理优化：
- 使用 **Accessibility Tree** 快照
- **Ref-based element selection**（确定性元素选择）
- 支持 **Session 隔离**

## 🆚 vs 内置 Browser Tool

| agent-browser | 内置 Browser |
|---|---|
| ✅ 多步骤自动化工作流 | ✅ 截图/PDF 分析 |
| ✅ 确定性元素选择 | ✅ 视觉检查 |
| ✅ 性能优先 | ✅ 扩展集成 |
| ✅ Session 隔离 | |

## 🛠️ 核心命令

### 1. 导航
```bash
agent-browser open <url>
agent-browser back | forward | reload | close
```

### 2. Snapshot（关键！总是用 `-i --json`）
```bash
agent-browser snapshot -i --json          # 交互式元素，JSON 输出
agent-browser snapshot -i -c -d 5 --json  # compact + depth limit
agent-browser snapshot -s "#main" -i      # 限定到 selector
```

### 3. 交互（基于 Ref）
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

### 4. 获取信息
```bash
agent-browser get text @e1 --json
agent-browser get html @e2 --json
agent-browser get value @e3 --json
agent-browser get attr @e4 "href" --json
agent-browser get title --json
agent-browser get url --json
agent-browser get count ".item" --json
```

### 5. 状态检查
```bash
agent-browser is visible @e2 --json
agent-browser is enabled @e3 --json
agent-browser is checked @e4 --json
```

### 6. Wait
```bash
agent-browser wait @e2                    # 等待元素
agent-browser wait 1000                   # 等待毫秒
agent-browser wait --text "Welcome"       # 等待文本出现
agent-browser wait --url "**/dashboard"   # 等待 URL
agent-browser wait --load networkidle     # 等待网络空闲
agent-browser wait --fn "window.ready === true"
```

### 7. Sessions（隔离浏览器）
```bash
agent-browser --session admin open site.com
agent-browser --session user open site.com
agent-browser session list

# 或通过环境变量
AGENT_BROWSER_SESSION=admin agent-browser ...
```

### 8. State Persistence（保存登录态）
```bash
agent-browser state save auth.json        # 保存 cookies/storage
agent-browser state load auth.json        # 加载（跳过登录）
```

### 9. Screenshots & PDFs
```bash
agent-browser screenshot page.png
agent-browser screenshot --full page.png
agent-browser pdf page.pdf
```

### 10. Network Control
```bash
agent-browser network route "**/ads/*" --abort           # 拦截请求
agent-browser network route "**/api/*" --body '{"x":1}'  # Mock
agent-browser network requests --filter api              # 查看请求
```

### 11. Cookies & Storage
```bash
agent-browser cookies                     # 获取所有
agent-browser cookies set name value
agent-browser storage local key           # 获取 localStorage
agent-browser storage local set key val
```

### 12. Tabs & Frames
```bash
agent-browser tab new https://example.com
agent-browser tab 2                       # 切换到 tab 2
agent-browser frame @e5                   # 切换到 iframe
agent-browser frame main                  # 返回主文档
```

## 📋 核心工作流

```bash
# 1. 打开并快照
agent-browser open https://example.com
agent-browser snapshot -i --json

# 2. 解析 refs 后交互
agent-browser click @e2
agent-browser fill @e3 "text"

# 3. 页面变化后重新快照
agent-browser snapshot -i --json
```

## 💡 Snapshot 输出格式

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

## ⚠️ 最佳实践

1. **Always use `-i` flag** - 专注交互元素
2. **Always use `--json`** - 更容易解析
3. **Wait for stability** - `agent-browser wait --load networkidle`
4. **Save auth state** - 用 `state save/load` 跳过登录
5. **Use sessions** - 隔离不同浏览器上下文
6. **Use `--headed` for debugging** - 可视化调试

## 📝 示例：搜索并提取

```bash
agent-browser open https://www.google.com
agent-browser snapshot -i --json
# AI 识别出搜索框 @e1
agent-browser fill @e1 "AI agents"
agent-browser press Enter
agent-browser wait --load networkidle
agent-browser snapshot -i --json
# AI 识别结果 refs
agent-browser get text @e3 --json
agent-browser get attr @e4 "href" --json
```

## 🔧 安装

```bash
npm install -g agent-browser
agent-browser install                     # 下载 Chromium
agent-browser install --with-deps         # Linux: + system deps
```

---

**适用场景**：复杂网页自动化、多步骤操作、需要精确元素定位的场景
