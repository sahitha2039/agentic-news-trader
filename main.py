from news import *
from sentiment import *

articles = fetch_news()

for i, article in enumerate(articles, start=1):
    title = article.get('title')
    result = analyze_sentiment(title)
    print(result)