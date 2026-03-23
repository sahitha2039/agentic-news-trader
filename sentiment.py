from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text):
    sentiment_score = analyzer.polarity_scores(text)
    return sentiment_score