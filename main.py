from fetcher import fetch_news
from generator import score_and_filter, generate_all_tweets
from datetime import datetime

def run():
    print("🚀 AI Signal Agent 启动...")
    
    print("\n📡 第一步：抓取新闻...")
    articles = fetch_news()
    print(f"共抓取 {len(articles)} 条新闻")
    
    print("\n⭐ 第二步：评分筛选...")
    filtered = score_and_filter(articles)
    print(f"高价值新闻 {len(filtered)} 条")
    
    print("\n🐦 第三步：生成推文...")
    tweets = generate_all_tweets(filtered)
    
    # 保存到文件
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"tweets_{today}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"AI Signal Agent - {today}\n")
        f.write("=" * 50 + "\n\n")
        
        for i, item in enumerate(tweets, 1):
            f.write(f"【推文 {i}】评分：{item['score']}分\n")
            f.write(f"来源：{item['source']}\n")
            f.write(f"原文：{item['title']}\n")
            f.write(f"链接：{item['link']}\n")
            f.write(f"\n推文内容：\n{item['tweet']}\n")
            f.write("-" * 40 + "\n\n")
    
    print(f"\n✅ 完成！推文已保存到 {filename}")
    print(f"共生成 {len(tweets)} 条推文")

if __name__ == "__main__":
    run()