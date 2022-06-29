import json
import nltk 
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from wordcloud import WordCloud

tweets_dict = {}

with open("cleaned_tweets.txt", "r") as file:  
  tweets_dict = json.load(file)

all_tweets = [item for sublist in list(tweets_dict.values()) for item in sublist]

tweet_data = pd.DataFrame(tweets_dict.items(), columns = ["Senator","Tweets"])

senator_data = pd.read_csv("SenateTwitters.csv")

combined = tweet_data.merge(senator_data, left_on="Senator", right_on="Twitter Handle")

dems = combined.where(combined["Party"] == "D").dropna()
repubs = combined.where(combined["Party"] == "R").dropna()

demcorpus = [item for sublist in list(dems["Tweets"]) for item in sublist]
repcorpus = [item for sublist in list(repubs["Tweets"]) for item in sublist]

split_dem_words = nltk.tokenize.word_tokenize(" ".join(demcorpus))
dem_word_dist = nltk.FreqDist(w.lower() for w in split_dem_words)

split_rep_words = nltk.tokenize.word_tokenize(" ".join(repcorpus))
rep_word_dist = nltk.FreqDist(w.lower() for w in split_rep_words)

print("most common words from Democrats: " + str([x[0]+", " for x in dem_word_dist.most_common(50)]))
print("most common words from Republicans: " + str([x[0]+", " for x in rep_word_dist.most_common(50)]))

dem_cloud = WordCloud(collocations = False, background_color = 'white').generate(" ".join(demcorpus))
rep_cloud = WordCloud(collocations = False, background_color = 'white').generate(" ".join(repcorpus))

dem_cloud.to_file("Democrat.png")
rep_cloud.to_file("Republican.png")

# count vectorizer
  # most popular topics per person
  # most common topics across everyone
  # common topics democrats vs republicans

# possible complete unsupervised clustering?
# which politicians sound the most similar?
# how did each one handle the shooting? 
# look for all tweets from each person on a specific topic
  # then cluster those tweets, split by party, etc... 