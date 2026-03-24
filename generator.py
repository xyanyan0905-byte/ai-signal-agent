from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def score_and_filter(articles):
    """给新闻打分，只保留高价值内容"""
    scored = []
    
    for article in articles:
        prompt = f"""你是一个AI行业分析师。
给以下新闻打重要性评分（1-10分）：
- 9-10分：重大突破，行业级影响
- 7-8分：重要进展，值得关注
- 5-6分：一般资讯
- 1-4分：低价值噪音

只返回一个数字，不要其他内容。

新闻标题：{article['title']}
新闻摘要：{article['summary']}
"""
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            score = int(response.choices[0].message.content.strip())
            article['score'] = score
            if score >= 7:
                scored.append(article)
                print(f"⭐ 评分{score}分: {article['title'][:50]}")
        except Exception as e:
            print(f"❌ 评分失败: {e}")
    
    return sorted(scored, key=lambda x: x['score'], reverse=True)

def generate_tweet(article):
    """生成有观点的推文"""
    prompt = f"""你是一个AI行业KOL，拥有独特观点和洞察力。
基于以下新闻，生成一条英文推文：

要求：
1. 不只是总结，要有自己的观点和判断
2. 指出这件事对普通人/开发者/行业的影响
3. 语气犀利、有洞察力
4. 长度控制在200字以内
5. 结尾加1-2个相关hashtag

新闻标题：{article['title']}
新闻摘要：{article['summary']}
"""
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

def generate_all_tweets(articles):
    """生成所有推文"""
    tweets = []
    
    for article in articles[:5]:  # 每次最多生成5条
        print(f"\n🐦 生成推文: {article['title'][:50]}")
        tweet = generate_tweet(article)
        tweets.append({
            "score": article['score'],
            "source": article['source'],
            "title": article['title'],
            "tweet": tweet,
            "link": article['link']
        })
    
    return tweets