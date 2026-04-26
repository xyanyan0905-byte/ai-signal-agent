🤖 AI Signal Agent

> English | An AI agent that automatically collects AI/Web3 intelligence, scores content with LLM, and generates bilingual KOL tweets — saving content creators 2-3 hours of daily research.
> 自动抓取AI/Web3行业情报，AI评分筛选，生成中英双语KOL推文的智能体

🎯 项目简介

每天自动完成"信息收集 → AI分析 → 内容生成"全流程，解决AI内容创作者每天手动找选题、写推文耗时的问题。

⚙️ 工作流程

抓取新闻 → AI评分筛选 → 生成观点推文 → 保存输出

1. 抓取新闻 — 从 TechCrunch、CoinTelegraph、Decrypt 等5个RSS源抓取24小时内最新资讯
2. AI评分筛选 — 用 LLaMA3（via Groq）对每条新闻打1-10分，筛选7分以上内容
3. 生成推文 — 生成有Hook、核心观点、影响分析、行动建议的中英双语推文
4. 保存输出 — 按日期保存到 `tweets_YYYY-MM-DD.txt`

🛠️ 技术栈

- Python — 核心逻辑
- Groq API + LLaMA3-70B — AI评分与推文生成
- feedparser — RSS新闻抓取
- python-dotenv — 环境变量管理

📁 项目结构

ai-signal-agent/
├── main.py           主程序入口
├── fetcher.py        新闻抓取模块
├── generator.py      AI评分+推文生成模块
├── config.py         配置文件
└── requirements.txt


🚀 快速开始

1. 克隆项目
```bash
git clone https://github.com/xyanyan0905-byte/ai-signal-agent.git
cd ai-signal-agent
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置环境变量，创建 `.env` 文件
```
GROQ_API_KEY=your_groq_api_key
```

4. 运行
```bash
python main.py
```

## 📝 输出示例
```
【推文 1】评分：8 | 来源：TechCrunch
标题：Anthropic wins injunction against Trump administration
---
【中文推文】
这件事比你想的重要

联邦法院裁定特朗普政府必须撤回对Anthropic的限制...

#AI #Anthropic #科技政策

【英文推文】
This ruling changes everything for AI companies...

#AI #Anthropic #TechPolicy
```
🌐 实际运营

本项目已投入实际使用，每日自动生成内容并发布到 X（Twitter）：

👉 [@DougouBo0905](https://twitter.com/DougouBo0905)
🔮 后续规划

- [ ] 接入 Twitter/X API 自动发布
- [ ] 支持自定义新闻源
- [√ ] 添加 GitHub Actions 定时运行
