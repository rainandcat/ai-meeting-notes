from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity 
    return "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
