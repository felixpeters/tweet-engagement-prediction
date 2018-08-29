from datetime import tzinfo, datetime, timedelta
import numpy as np
from dateutil.parser import parse
from .utils import UTC
from textblob import TextBlob

def account_age(tweet):
    td = datetime.now(tz=UTC()) - parse(tweet.user.created_at)
    return td.days

def creation_month(tweet):
    date = parse(tweet.created_at) + timedelta(seconds=tweet.user.utc_offset)
    return date.month

def creation_day(tweet):
    date = parse(tweet.created_at) + timedelta(seconds=tweet.user.utc_offset)
    return date.day

def creation_weekday(tweet):
    date = parse(tweet.created_at) + timedelta(seconds=tweet.user.utc_offset)
    return date.weekday()
    
def creation_hour(tweet):
    date = parse(tweet.created_at) + timedelta(seconds=tweet.user.utc_offset)
    return date.hour

def creation_minute(tweet):
    date = parse(tweet.created_at) + timedelta(seconds=tweet.user.utc_offset)
    return date.minute

def followers(tweet):
    followers = (tweet.user.followers_count if tweet.user.followers_count != None else 0)
    return followers

def friends(tweet):
    friends = (tweet.user.friends_count if tweet.user.friends_count != None else 0)
    return friends

def follower_friend_ratio(tweet):
    ratio = 0.0
    followers = followers(tweet)
    friends = friends(tweet)
    if friends != 0:
        ratio = float(followers) / float(friends)
    return ratio

def listings(tweet):
    listed = (tweet.user.listed_count if tweet.user.listed_count != None else 0)
    return listed

def statuses(tweet):
    statuses = (tweet.user.statuses_count if tweet.user.statuses_count != None else 0)
    return statuses

def favorites(tweet):
    favs = (tweet.user.favourites_count if tweet.user.favourites_count != None else 0)
    return favs

def urls(tweet):
    return len(tweet.urls)

def hashtags(tweet):
    return len(tweet.hashtags)

def mentions(tweet):
    return len(tweet.user_mentions)

def length(tweet):
    return len(tweet.text)

def sentiment(tweet):
    sentiment, _ = TextBlob(tweet.text).sentiment
    return sentiment

def quoted(tweet):
    quoted = (1 if tweet.quoted_status != None else 0)
    return quoted

def quoted_sentiment(tweet):
    sentiment = 0.0
    if tweet.quoted_status != None:
        sentiment = TextBlob(tweet.quoted_status.text).sentiment
    return sentiment

def quoted_popularity(tweet):
    retweets = 0
    if tweet.quoted_status != None:
        retweets = tweet.quoted_status.retweet_count
    return retweets

def replied(tweet):
    replied = (1 if tweet.in_reply_to_status_id != None else 0)
    return replied

def verified(tweet):
    verified = (1 if tweet.user.verified else 0)
    return verified

def tweet_freq(tweet):
    freq = float(statuses(tweet)) / float(account_age(tweet))
    return freq

def fav_freq(tweet):
    freq = float(favorites(tweet)) / float(account_age(tweet))
    return freq
