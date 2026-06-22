import requests
import urllib.parse
from datetime import datetime

NEWS_API_KEY = "3d9d1ca3fdd94186a02a173fa4b0793b"
NICHE_KEYWORD = "artificial intelligence"

def fetch_news():
    url = f"https://newsapi.org/v2/everything?q={NICHE_KEYWORD}&sortBy=publishedAt&language=en&pageSize=5&apiKey={NEWS_API_KEY}"
    return requests.get(url).json().get("articles", [])

def generate_image_url(prompt):
    encoded = urllib.parse.quote(prompt)
    return f"https://image.pollinations.ai/prompt/{encoded}?width=1200&height=630&nologo=true"

def generate_post(title):
    hashtags = "#AI #Tech #News #MachineLearning #Innovation"
    return f"🚀 Breaking: {title}\n\n{hashtags}"

def run():
    print("🔍 Fetching news...")
    articles = fetch_news()
    if not articles:
        print("No articles found")
        return
    
    article = articles[0]
    title = article['title']
    print(f"📰 Story: {title}")
    
    post = generate_post(title)
    image_url = generate_image_url(title)
    
    print(f"\n🖼 Image: {image_url}")
    print(f"\n📝 Post:\n{post}")
    print(f"\n✅ Generated at {datetime.now()}")

if __name__ == "__main__":
    run()
