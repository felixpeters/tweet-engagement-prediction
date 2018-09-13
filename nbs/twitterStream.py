import os
import tweepy
from dotenv import load_dotenv, find_dotenv

# constants
load_dotenv(find_dotenv())
CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET") 
ACCESS_TOKEN_KEY = os.getenv("TWITTER_ACCESS_TOKEN_KEY")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# setup API connection
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# get tweet from timeline
tweets = api.home_timeline()
for tweet in tweets:
    print(tweet.user.screen_name, ":", tweet.text)
