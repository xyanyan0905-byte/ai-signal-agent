import feedparser
from datetime import datetime, timedelta
from config import RSS_FEEDS, MAX_PER_SOURCE

def fetch_news():
    """抓取24小时内的AI和Web3新闻"""
    articles = []
    yesterday = datetime.now() - timedelta(hours=24)
    
    for url in RSS_FEEDS:
        try:
            feed = feedparser.parse(url)
            count = 0
            for entry in feed.entries:
                if count >= MAX_PER_SOURCE:
                    break
                
                # 检查发布时间
                published = entry.get("published_parsed") or entry.get("updated_parsed")
                if published:
                    pub_date = datetime(*published[:6])
                    if pub_date < yesterday:
                        continue  # 跳过24小时前的新闻
                
                articles.append({
                    "title": entry.get("title", ""),
                    "summary": entry.get("summary", "")[:300],
                    "link": entry.get("link", ""),
                    "source": feed.feed.get("title", url),
                    "published": str(published)
                })
                count += 1
            print(f"✅ 抓取成功: {url} ({count}条24小时内新闻)")
        except Exception as e:
            print(f"❌ 抓取失败: {url} - {e}")
    
    return articles