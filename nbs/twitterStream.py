import os
import tweepy
from dotenv import load_dotenv, find_dotenv
from termcolor import colored
from tep.accountCollector import AccountCollector

# override tweepy.StreamListener to add logic
class PrintListener(tweepy.StreamListener):

    def on_status(self, status):
        print(colored(status.user.screen_name, 'green'), status.text)

# constants
load_dotenv(find_dotenv())
CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET") 
ACCESS_TOKEN_KEY = os.getenv("TWITTER_ACCESS_TOKEN_KEY")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
USER_IDS_PATH = "data/user_ids.txt"

# setup API connection
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# get user ids
ac = AccountCollector()
users = ac.load_user_ids(fname=USER_IDS_PATH)
users = [str(u) for u in users]

# create stream and listener
listener = PrintListener()
stream = tweepy.Stream(auth=api.auth, listener=listener)

# run stream
print(colored("Streaming tweets of {} users".format(len(users)), 'red'))
stream.filter(follow=users)
