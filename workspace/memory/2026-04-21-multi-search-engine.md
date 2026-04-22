# multi-search-engine-simple

- **位置**: `skills/multi-search-engine-simple/SKILL.md`
- **功能**: 集成 10 个免费搜索引擎，支持国内可访问的搜索平台
- **搜索引擎**:
  - Baidu (`https://www.baidu.com/s?wd={keyword}`)
  - Bing CN / INT
  - 360
  - Sogou
  - WeChat 搜索 (`https://wx.sogou.com/weixin?type=2&query={keyword}`)
  - Toutiao
  - Jisilu
  - Ecosia
  - WolframAlpha
- **使用方式**: 将 `{keyword}` 替换为搜索词，构建 URL 后用 `web_fetch` 工具获取内容
- **适用场景**: 国内环境下的多平台信息检索
