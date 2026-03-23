from news import *
from sentiment import *

articles = fetch_news()

for i, article in enumerate(articles, start=1):

    title = article.get('title')
    result = analyze_sentiment(title)
    compound = result.get('compound')

    if compound >= 0.5:
        label = "POSITIVE"

    elif compound <= -0.5:
        label = "NEGATIVE"

    else:
        label = "NEUTRAL"

    print(f"{i}. {title}")
    print(f"    Source: {article.get('source', '')}")
    print(f"    Sentiment score: {compound}")
    print(f"    Label: {label}")