import tweepy
import use_keys as keys
import json

user_ids = json.load(open("twitter_ids.txt","r"))

'''
with open("twitter_ids.txt") as id_file:
  for line in id_file.readlines():
    user_ids.append(line.rstrip())
'''

print("Got desired list of user ids")

client = tweepy.Client(
        bearer_token=keys.bearer_key,
        access_token=keys.api_key,
        access_token_secret=keys.api_secret,
    )

tweets = {}

print("Downloading tweets...")

for user in user_ids.items():
  id = user[1]
  name = user[0]
  tweet_data = client.get_users_tweets(id = id,max_results=100,exclude="retweets")
  tweets[name] = tweet_data.data
  print("Got %s tweets from %s" % (tweet_data.meta["result_count"], id))

def get_tweet_text_list(tweets_list):
  tweet_text_list = []
  for tweet in tweets_list:
    tweet_text_list.append(tweet.text)
  return tweet_text_list

for user in tweets.items():
  key = user[0]
  tweets_list = user[1]
  tweets[key] = get_tweet_text_list(tweets_list)

tweets_file = open("tweets.txt", "x")

json.dump(tweets,tweets_file)

print("Saved tweets to file")
