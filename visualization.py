import matplotlib.pyplot as plt

def plot_sentiment_analysis(sentiment_counts):
    labels = sentiment_counts.keys()
    sizes = sentiment_counts.values()
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=["#4CAF50", "#FF5722", "#FFC107"])
    plt.title("Sentiment Analysis of Meeting Notes")
    return plt
