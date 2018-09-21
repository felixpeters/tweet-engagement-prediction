from termcolor import colored
from .models import Tweet, Retweet, Reply, Quote

def process_tweet(tweet):
    tweet = Tweet(tweet)
    print(tweet)

def process_engagement(tweet):
    if 'retweeted_status' in tweet:
        retweet = Retweet(tweet)
        print(retweet)
    elif 'quoted_status' in tweet:
        quote = Quote(tweet)
        print(quote)
    elif 'in_reply_to_status_id' in tweet:
        reply = Reply(tweet)
        print(reply)
    else:
        print(colored('Unknown tweet type', 'red'), tweet['id'])
