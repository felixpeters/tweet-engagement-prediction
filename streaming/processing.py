from termcolor import colored
from .models import Tweet, Retweet, Reply, Quote
from .database import save_tweet, save_retweet, save_quote, save_reply

class TweetProcessor():

    def __init__(self, conn):
        self.conn = conn

    def process_tweet(self, tweet):
        # discard native retweets from user group
        if ('retweeted_status' in tweet) and tweet['retweeted_status'] != None:
            return
        tweet = Tweet(tweet)
        save_tweet(self.conn, tweet)

    def process_engagement(self, tweet):
        if 'retweeted_status' in tweet:
            retweet = Retweet(tweet)
            save_retweet(self.conn, retweet)
        elif 'quoted_status' in tweet:
            quote = Quote(tweet)
            save_quote(self.conn, quote)
        elif 'in_reply_to_status_id' in tweet:
            reply = Reply(tweet)
            save_reply(self.conn, reply)
        else:
            return
