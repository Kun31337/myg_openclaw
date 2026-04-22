#!/usr/bin/env python3
import requests
import json

# 巨量引擎即创平台相关 API
BASE_URL = "https://aic.oceanengine.com"

# 尝试访问数字人口播页面的静态资源
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://aic.oceanengine.com/"
}

# 获取首页内容
response = requests.get(f"{BASE_URL}/tools/smart_clip/digital_human?bpId=1793561373042699", headers=headers, timeout=10)
print(f"状态码：{response.status_code}")
print(f"页面大小：{len(response.text)} 字节")

# 检查是否包含特定关键词
if "收藏夹" in response.text or "袁伟" in response.text or "刘烨" in response.text:
    print("\n✓ 页面内容中包含目标关键词")
else:
    print("\n✗ 未找到目标关键词，可能需要登录后才能看到完整内容")

# 提取可能的 API 端点
import re
api_endpoints = list(set(re.findall(r'/api/agw/[a-zA-Z0-9_]+', response.text)))
print(f"\n发现 {len(api_endpoints)} 个 API 端点:")
for endpoint in api_endpoints[:20]:
    print(f"  - {endpoint}")
