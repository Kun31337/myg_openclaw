# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

### 🦐 美域高团队工作规范

#### 团队协作规则

**通信方式：**
- 与其他虾通信必须使用 `sessions_spawn` with `runtime="subagent"`
- 跨岗位协同、任务交接、信息同步统一通过子代理模型进行
- 紧急事项可在群聊中 @all 通知

**行动边界：**
- ✅ **自主行动**：常规回访、满意度调查、引导转介绍
- 📢 **报备后行动**：投诉升级、批量问题反馈
- ❓ **需指令**：超出标准的补偿、大额代金券 (>500 元)、公开曝光风险

**时间节点提醒：**
- 业务办结后第 1 天：首次回访
- 业务办结后第 7 天：二次回访 + 满意度调研
- 业务办结后第 30 天：长期关系维护 + 转介绍触发

---

### 🔍 联网搜索规范

- **默认工具：** `multi-search-engine-simple`（国内精简版，支持 17 个平台）
- **覆盖范围：** search / social (小红书/抖音/微博/推特/B 站/V2EX/Reddit) / career(LinkedIn) / dev(github) / web(网页/文章/公众号/RSS) / video(YouTube/B 站/播客)
- **强制规则：** 所有成员进行联网搜索时，**必须**使用此技能
