import json
import nltk 
import matplotlib.pyplot as plt
import pandas as pd

tweets_dict = {}

with open("cleaned_tweets.txt", "r") as file:  
  tweets_dict = json.load(file)

search_items = [""]

def keep_tweets_with_search_terms(tweet_list: list):
  kept_tweets = []
  for tweet in tweet_list:
    for word in search_items:
      if word in tweet.split(" "):
        kept_tweets.append(tweet)
        break
  return kept_tweets

filtered_dict = {}
for user, tweets in tweets_dict.items():
  filtered_dict[user] = keep_tweets_with_search_terms(tweets)

with open("filtered_tweets.txt", "x") as output_file:
  json.dump(filtered_dict,output_file)