from error_notifier import send_error_email

def main():
    # 第一步：RSS抓取
    try:
        articles = fetch_news()
    except Exception as e:
        send_error_email("RSS抓取", e)
        return

    # 第二步：AI评分筛选
    try:
        scored = score_articles(articles)
    except Exception as e:
        send_error_email("AI评分筛选", e)
        return

    # 第三步：推文生成
    try:
        tweets = generate_tweets(scored)
    except Exception as e:
        send_error_email("推文生成", e)
        return

    # 第四步：保存输出
    try:
        save_output(tweets)
    except Exception as e:
        send_error_email("推文保存", e)
        return

if __name__ == "__main__":
    main()