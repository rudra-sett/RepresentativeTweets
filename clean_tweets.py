import pandas as pd
import json
import nltk
from nltk import sent_tokenize, word_tokenize, corpus
from nltk.stem import WordNetLemmatizer
import contractions
import re
from string import punctuation
from collections import defaultdict

tweet_dict = json.load(open("tweets.txt", "r"))

wordnet_lemmatizer = WordNetLemmatizer()

stop_words = set(corpus.stopwords.words('english'))

tag_map = defaultdict(lambda : corpus.wordnet.NOUN)
tag_map['J'] = corpus.wordnet.ADJ
tag_map['V'] = corpus.wordnet.VERB
tag_map['R'] = corpus.wordnet.ADV


#TODO 
# most popular topics per person
# most common topics across everyone
# common topics democrats vs republicans
# possible complete unsupervised clustering?
# which politicians sound the most similar?
# how did each one handle the shooting? 
# look for all tweets from each person on a specific topic
  # then cluster those tweets, split by party, etc... 

# data is always mapped in a dictionary: {twitter handle : data}

# cleaning a tweet involves the following in this order:
# removing links
# lowercase everything
# expand contractions
# lemmatize words
# drop stopwords
# drop punctuation
# TODO: handle tagging other users in a better way



def remove_URL(text):    
    return re.sub(r"http\S+", "", text)

# cleans a single tweet
def clean_tweet(tweet):
  # remove urls
  tweet = remove_URL(tweet)
  # lowercase everything
  tweet = tweet.lower()
  # expand contractions
  tweet = contractions.fix(tweet)  
  tweet_expanded = nltk.word_tokenize(tweet)
  # replace you.s with usa
  tweet_expanded = [word if not word == "you.s" else "usa"for word in tweet_expanded ]
  # remove &amp
  tweet_expanded = [word for word in tweet_expanded if not word == "amp"]
  # remove stopwords
  tweet_expanded = [word for word in tweet_expanded if not word in stop_words]
  # lemmatize with POS tagging
  lemmatized = []
  for token, tag in nltk.pos_tag(tweet_expanded):
    lemmatized.append(wordnet_lemmatizer.lemmatize(token, tag_map[tag[0]]))
  #tweet_expanded = lemmatized
  # recreate tweet again
  tweet = " ".join(tweet_expanded)
  # drop punctuation
  tweet = "".join(c for c in tweet if not c in punctuation)
  return tweet


# cleans a single tweeter's tweets
def clean_many_tweets(tweet_list: list):
  for idx, tweet in enumerate(tweet_list):
    tweet_list[idx] = clean_tweet(tweet)


# take each tweeter's list of tweets and replace it with a cleaned version
def run():
  for tweeter, tweets in tweet_dict.items():
    clean_many_tweets(tweet_dict[tweeter])  

run()

with open("cleaned_tweets.txt", "x") as file:
  json.dump(tweet_dict,file)