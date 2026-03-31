from dotenv import load_dotenv
load_dotenv()

import os

# Gemini API Key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
# 监控的AI新闻源
RSS_FEEDS = [
    "https://venturebeat.com/category/ai/feed/",
    "https://techcrunch.com/category/artificial-intelligence/feed/",
    "https://www.artificialintelligence-news.com/feed/",
    "https://cointelegraph.com/rss",
    "https://decrypt.co/feed",
]

# 每次抓取每个源的文章数
MAX_PER_SOURCE = 3