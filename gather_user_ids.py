import use_keys as keys
import tweepy
import pandas as pd
import json

client = tweepy.Client(
        bearer_token=keys.bearer_key,
        access_token=keys.api_key,
        access_token_secret=keys.api_secret,
    )

data = pd.read_csv("SenateTwitters.csv")
twitter_handles = data["Twitter Handle"]
users_and_ids = {}
for person in twitter_handles:
  try:
    user_data = client.get_user(username=person[1:])
    users_and_ids[person] = user_data.data.id
  except AttributeError:
    print("Failed to get ID for %s" % person)


file_name = 'twitter_ids.txt'

with open(file_name,"a+") as file:
  json.dump(users_and_ids, file)