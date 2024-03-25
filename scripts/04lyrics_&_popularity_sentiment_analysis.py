# -*- coding: utf-8 -*-
"""04Lyrics & Popularity_Sentiment Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11EzNsdJoCpNajOSn18gdRmCEua6_aKA_

##Use a multilingual model for sentiment analysis in Traditional Chinese and Emglish lyrics
"""

!pip install pandas

from transformers import pipeline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file containing English lyrics into a pandas DataFrame
english_df = pd.read_csv('https://raw.githubusercontent.com/Letieateat/Traditional-Chinese-English-Lyrics-and-songs-popularity/main/song-data/EN_songs.csv')

# Load the CSV file containing Traditional Chinese lyrics into a pandas DataFrame
chinese_df = pd.read_csv('https://raw.githubusercontent.com/Letieateat/Traditional-Chinese-English-Lyrics-and-songs-popularity/main/song-data/TW_songs.csv')

# Initialize the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", return_all_scores=True)

# Define a function to apply sentiment analysis to lyrics
def analyze_sentiment(tokens):
    # Join the tokens back into lyrics text
    lyrics = " ".join(tokens)
    # Truncate lyrics to 510 tokens to fit the tensor size (512)
    truncated_lyrics = " ".join(tokens[:510])
    # Apply sentiment analysis to each song
    sentiment_scores = sentiment_pipeline(truncated_lyrics)
    return sentiment_scores

# Apply sentiment analysis to English lyrics
english_df['sentiment'] = english_df['Lyrics'].apply(analyze_sentiment)

# Apply sentiment analysis to Traditional Chinese lyrics
chinese_df['sentiment'] = chinese_df['lyrics'].apply(analyze_sentiment)

# Extract sentiment scores and popularity scores for English lyrics
english_sentiment_data = english_df['sentiment'].apply(lambda x: x[0][0])
english_popularity_scores = english_df['Popularity']

# Extract sentiment scores and popularity scores for Traditional Chinese lyrics
chinese_sentiment_data = chinese_df['sentiment'].apply(lambda x: x[0][0])
chinese_popularity_scores = (101 - chinese_df['rankings']) / 100

# Initialize lists to store popularity scores corresponding to positive and negative sentiment scores for English lyrics
english_positive_scores=[]
english_negative_scores=[]
english_positive_popularity_scores = []
english_negative_popularity_scores = []

# Iterate through sentiment data to separate positive and negative scores for English lyrics
for sentiment, popularity in zip(english_sentiment_data, english_popularity_scores):
    if sentiment['label'] == 'positive':
        english_positive_scores.append(sentiment['score'])
        english_positive_popularity_scores.append(popularity)
    elif sentiment['label'] == 'negative':
        english_negative_scores.append(sentiment['score'])
        english_negative_popularity_scores.append(popularity)

# Plot the relationship between positive sentiment score and popularity for English lyrics
plt.figure(figsize=(6, 6))
plt.scatter(english_positive_scores, english_positive_popularity_scores, color='green', marker='X', label='English (Positive)')
plt.scatter(english_negative_scores, english_negative_popularity_scores, color='pink', marker='X', label='English (Negative)')
plt.xlabel('Sentiment Score')
plt.ylabel('Popularity Score')
plt.title('Relationship between Sentiment Score and Popularity (English Lyrics)')
plt.legend()
plt.grid(True)
plt.show()

# Initialize lists to store popularity scores corresponding to positive and negative sentiment scores for Traditional Chinese lyrics
chinese_positive_scores=[]
chinese_negative_scores=[]
chinese_positive_popularity_scores = []
chinese_negative_popularity_scores = []

# Iterate through sentiment data to separate positive and negative scores for Traditional Chinese lyrics
for sentiment, popularity in zip(chinese_sentiment_data, chinese_popularity_scores):
    if sentiment['label'] == 'positive':
        chinese_positive_scores.append(sentiment['score'])
        chinese_positive_popularity_scores.append(popularity)
    elif sentiment['label'] == 'negative':
        chinese_negative_scores.append(sentiment['score'])
        chinese_negative_popularity_scores.append(popularity)

# Plot the relationship between positive sentiment score and popularity for Traditional Chinese lyrics
plt.figure(figsize=(6, 6))
plt.scatter(chinese_positive_scores, chinese_positive_popularity_scores, color='green', marker='X', label='Traditional Chinese (Positive)')
plt.scatter(chinese_negative_scores, chinese_negative_popularity_scores, color='pink', marker='X', label='Traditional Chinese (Negative)')
plt.xlabel('Sentiment Score')
plt.ylabel('Popularity Score')
plt.title('Relationship between Sentiment Score and Popularity (Traditional Chinese Lyrics)')
plt.legend()
plt.grid(True)
plt.show()

"""##Use a different model (distilbert-base-uncased-emotion) to investigate English lyrics in 6 emotions."""

# Load the CSV file containing English lyrics into a pandas DataFrame
english_df = pd.read_csv('https://raw.githubusercontent.com/Letieateat/Traditional-Chinese-English-Lyrics-and-songs-popularity/main/song-data/EN_songs.csv')

# Initialize the sentiment analysis pipeline
classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)
# Function to apply sentiment analysis to lyrics
def analyze_sentiment(tokens):
    # Join the tokens back into lyrics text
    lyrics = " ".join(tokens)
    # Truncate lyrics to 510 tokens to fit the tensor size (512)
    truncated_lyrics = " ".join(tokens[:510])
    # Apply sentiment analysis to each lyric
    sentiment_scores = classifier(truncated_lyrics)
    return sentiment_scores

# Apply sentiment analysis to English lyrics
english_df['sentiment'] = english_df['Lyrics'].apply(analyze_sentiment)

# Extract sentiment scores and popularity scores for English lyrics
english_sentiment_data = english_df['sentiment'].apply(lambda x: {emotion['label']: emotion['score'] for emotion in x[0]})
english_popularity_scores = english_df['Popularity']

# Define a list of emotions
emotions = ['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']

# Assign colors to each emotion
emotion_colors = {
    'sadness': '#84C1FF',
    'joy': '#FFE66F',
    'love': '#009100',
    'anger': '#FF9797',
    'fear': '#DCB5FF',
    'surprise': '#D9B3B3'
}

# Plot the relationship between sentiment score and popularity for each emotion
plt.figure(figsize=(15, 10))

for emotion in emotions:
    sentiment_scores = [sentiment.get(emotion, 0) for sentiment in english_sentiment_data]
    plt.scatter(sentiment_scores, english_popularity_scores, label=emotion.capitalize(), color=emotion_colors[emotion])

plt.xlabel('Sentiment Score')
plt.ylabel('Popularity Score')
plt.title('Relationship between Sentiment Score and Popularity (English Lyrics)')
plt.legend()
plt.grid(True)
plt.show()