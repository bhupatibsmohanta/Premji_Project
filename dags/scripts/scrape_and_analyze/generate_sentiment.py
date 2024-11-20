import random

def mock_api_call(row):
    sentiment_score = round(random.uniform(0, 1), 3)
    return sentiment_score  

def generate_sentiment(df):
    df['sentiment_score'] = df.apply(mock_api_call, axis=1)
    return df

