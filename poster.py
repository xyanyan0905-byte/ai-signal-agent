import tweepy
import os

def post_tweets(tweets):
    auth = tweepy.OAuth1UserHandler(
        consumer_key=os.environ.get("TWITTER_API_KEY"),
        consumer_secret=os.environ.get("TWITTER_API_SECRET"),
        access_token=os.environ.get("TWITTER_ACCESS_TOKEN"),
        access_token_secret=os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
    )
    api = tweepy.API(auth)
    
    posted = 0
    for item in tweets[:3]:
        tweet_text = item["tweet"]
        
        if "【中文推文】" in tweet_text:
            start = tweet_text.find("【中文推文】") + len("【中文推文】")
            end = tweet_text.find("【英文推文】")
            chinese_tweet = tweet_text[start:end].strip()
        else:
            chinese_tweet = tweet_text[:280]
        
        if len(chinese_tweet) > 280:
            chinese_tweet = chinese_tweet[:277] + "..."
        
        try:
            api.update_status(chinese_tweet)
            print(f"✅ 发推成功: {chinese_tweet[:50]}...")
            posted += 1
        except Exception as e:
            print(f"❌ 发推失败: {e}")
    
    print(f"共发送 {posted} 条推文")