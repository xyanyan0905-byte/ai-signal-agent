from fetcher import fetch_news
from generator import score_and_filter, generate_all_tweets
from datetime import datetime

def run():
    print("AI Signal Agent 启动...")
    
    print("第一步：抓取新闻...")
    articles = fetch_news()
    print(f"共抓取 {len(articles)} 条新闻")

    print("第二步：AI评分筛选...")
    top_articles = score_and_filter(articles)
    print(f"筛选出 {len(top_articles)} 条高质量新闻")

    print("第三步：生成推文...")
    tweets = generate_all_tweets(top_articles)

    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"tweets_{today}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"AI Signal Agent - {today}\n")
        f.write("=" * 50 + "\n\n")
        for i, item in enumerate(tweets, 1):
            f.write(f"[推文 {i}] 评分：{item['score']} | 来源：{item['source']}\n")
            f.write(f"标题：{item['title']}\n")
            f.write(f"链接：{item['link']}\n")
            f.write("-" * 40 + "\n")
            f.write(item['tweet'])
            f.write("\n" + "=" * 50 + "\n\n")

    print(f"完成！推文已保存到 {filename}")
    print(f"共生成 {len(tweets)} 条推文！")

if __name__ == "__main__":
    run()