import pandas as pd
from textblob import TextBlobC:\Users\hp\Desktop\sentiment_analyzer (ja

# Load the dataset
df = pd.read_csv("sample_reviews.csv")

# Function to get sentiment score
def get_sentiment(text):
    blob = TextBlob(str(text))
    return blob.sentiment.polarity

# Apply sentiment function
df['Sentiment Score'] = df['Review'].apply(get_sentiment)

# Label the sentiment
df['Sentiment'] = df['Sentiment Score'].apply(
    lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral')
)

# Save results to new CSV
df.to_csv("review_sentiment_output.csv", index=False)

print("✅ Sentiment analysis done! Check review_sentiment_output.csv")
