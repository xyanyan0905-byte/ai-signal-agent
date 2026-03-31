# -*- coding: utf-8 -*-
from groq import Groq
import os
client = Groq(api_key=os.environ.get("GROQ_API_KEY", ""))


def score_and_filter(articles):
    scored = []
    for article in articles:
        prompt = f"""给以下新闻打重要性评分（1-10分），只返回一个数字，不要其他内容：
标题：{article['title']}
摘要：{article['summary']}"""
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=5
            )
            score = int(response.choices[0].message.content.strip())
            article['score'] = score
            if score >= 7:
                scored.append(article)
                print(f"评分{score}分: {article['title'][:50]}")
        except Exception as e:
            print(f"评分失败: {e}")
    return sorted(scored, key=lambda x: x['score'], reverse=True)

def generate_tweet(article):
    prompt = f"""你是一个AI/Web3领域的中文KOL，风格犀利有观点，粉丝是创业者和投资人。

基于以下新闻生成推文，严格按照格式输出：

【中文推文】
第一行：一句让人停下来的hook（不超过20字）
空行
核心观点：解释为什么重要（2-3句，要有数据或具体细节）
空行
影响分析：对谁有影响？（1-2句）
空行
行动建议：读者现在可以做什么（1句）
空行
#hashtag1 #hashtag2 #hashtag3

【英文推文】
Hook line (max 15 words)

Core insight with data (2-3 sentences)

Impact + action (1-2 sentences)

#hashtag1 #hashtag2 #hashtag3

新闻标题：{article['title']}
新闻摘要：{article['summary']}"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800
    )
    return response.choices[0].message.content

def generate_all_tweets(articles):
    tweets = []
    for article in articles[:5]:
        print(f"生成推文: {article['title'][:50]}")
        tweet = generate_tweet(article)
        tweets.append({
            "score": article['score'],
            "source": article['source'],
            "title": article['title'],
            "tweet": tweet,
            "link": article['link']
        })
    return tweets
