from termcolor import colored
from .features import *

class Tweet():

    def __init__(self, status):
        self.tweet_id = status_id(status)
        self.created_at = tweet_creation_date(status)
        self.text = text(status)
        self.lang = lang(status)
        self.favorite_count = favorite_count(status)
        self.retweet_count = retweet_count(status)
        self.hashtag_count = hashtag_count(status)
        self.url_count = url_count(status)
        self.mention_count = mention_count(status)
        self.media_count = media_count(status)
        self.quoted_status = is_quote(status)
        self.quoted_status_id = quoted_status_id(status)
        self.quoted_user_id = quoted_user_id(status)
        self.replied_status = is_reply(status)
        self.replied_status_id = replied_status_id(status)
        self.replied_user_id = replied_user_id(status)
        self.user_id = user_id(status)
        self.user_name = user_name(status)
        self.user_created_at = user_creation_date(status)
        self.user_followers = user_followers(status)
        self.user_friends = user_friends(status)
        self.user_statuses = user_statuses(status)
        self.user_listings = user_listings(status)
        self.user_verified = user_verified(status)
        self.user_favorites = user_favorites(status)
        self.user_utc_offset = user_utc_offset(status)

    def __repr__(self):
        return colored(self.user_name, 'blue') + ' ' + self.text

    def as_tuple(self):
        return (self.tweet_id,
                self.created_at,
                self.text,
                self.lang,
                self.favorite_count,
                self.retweet_count,
                self.hashtag_count,
                self.url_count,
                self.mention_count,
                self.media_count,
                self.quoted_status,
                self.quoted_status_id,
                self.quoted_user_id,
                self.replied_status,
                self.replied_status_id,
                self.replied_user_id,
                self.user_id,
                self.user_name,
                self.user_created_at,
                self.user_followers,
                self.user_friends,
                self.user_statuses,
                self.user_listings,
                self.user_verified,
                self.user_favorites,
                self.user_utc_offset)

class Retweet():

    def __init__(self, status):
        self.retweet_id = status_id(status)
        self.retweeted_status_id = retweeted_status_id(status)
        self.created_at = tweet_creation_date(status)
        self.text = text(status)
        self.lang = lang(status)
        self.user_id = user_id(status)
        self.user_name = user_name(status)
        self.user_created_at = user_creation_date(status)
        self.user_followers = user_followers(status)
        self.user_friends = user_friends(status)
        self.user_statuses = user_statuses(status)
        self.user_listings = user_listings(status)
        self.user_verified = user_verified(status)
        self.user_favorites = user_favorites(status)
        self.user_utc_offset = user_utc_offset(status)

    def __repr__(self):
        return colored(self.user_name, 'yellow') + ' ' + self.text

    def as_tuple(self):
        return (self.retweet_id,
                self.retweeted_status_id,
                self.created_at,
                self.text,
                self.lang,
                self.user_id,
                self.user_name,
                self.user_created_at,
                self.user_followers,
                self.user_friends,
                self.user_statuses,
                self.user_listings,
                self.user_verified,
                self.user_favorites,
                self.user_utc_offset)

class Quote():

    def __init__(self, status):
        self.quote_id = status_id(status)
        self.quoted_status_id = quote_id(status)
        self.created_at = tweet_creation_date(status)
        self.text = text(status)
        self.lang = lang(status)
        self.favorite_count = favorite_count(status)
        self.retweet_count = retweet_count(status)
        self.hashtag_count = hashtag_count(status)
        self.url_count = url_count(status)
        self.mention_count = mention_count(status)
        self.media_count = media_count(status)
        self.user_id = user_id(status)
        self.user_name = user_name(status)
        self.user_created_at = user_creation_date(status)
        self.user_followers = user_followers(status)
        self.user_friends = user_friends(status)
        self.user_statuses = user_statuses(status)
        self.user_listings = user_listings(status)
        self.user_verified = user_verified(status)
        self.user_favorites = user_favorites(status)
        self.user_utc_offset = user_utc_offset(status)

    def __repr__(self):
        return colored(self.user_name, 'cyan') + ' ' + self.text

    def as_tuple(self):
        return (self.quote_id,
                self.quoted_status_id,
                self.created_at,
                self.text,
                self.lang,
                self.favorite_count,
                self.retweet_count,
                self.hashtag_count,
                self.url_count,
                self.mention_count,
                self.media_count,
                self.user_id,
                self.user_name,
                self.user_created_at,
                self.user_followers,
                self.user_friends,
                self.user_statuses,
                self.user_listings,
                self.user_verified,
                self.user_favorites,
                self.user_utc_offset)

class Reply():

    def __init__(self, status):
        self.reply_id = status_id(status)
        self.replied_status_id = replied_status_id(status)
        self.created_at = tweet_creation_date(status)
        self.text = text(status)
        self.lang = lang(status)
        self.favorite_count = favorite_count(status)
        self.retweet_count = retweet_count(status)
        self.hashtag_count = hashtag_count(status)
        self.url_count = url_count(status)
        self.mention_count = mention_count(status)
        self.media_count = media_count(status)
        self.user_id = user_id(status)
        self.user_name = user_name(status)
        self.user_created_at = user_creation_date(status)
        self.user_followers = user_followers(status)
        self.user_friends = user_friends(status)
        self.user_statuses = user_statuses(status)
        self.user_listings = user_listings(status)
        self.user_verified = user_verified(status)
        self.user_favorites = user_favorites(status)
        self.user_utc_offset = user_utc_offset(status)

    def __repr__(self):
        return colored(self.user_name, 'magenta') + ' ' + self.text

    def as_tuple(self):
        return (self.reply_id,
                self.replied_status_id,
                self.created_at,
                self.text,
                self.lang,
                self.favorite_count,
                self.retweet_count,
                self.hashtag_count,
                self.url_count,
                self.mention_count,
                self.media_count,
                self.user_id,
                self.user_name,
                self.user_created_at,
                self.user_followers,
                self.user_friends,
                self.user_statuses,
                self.user_listings,
                self.user_verified,
                self.user_favorites,
                self.user_utc_offset)

class StreamError():

    def __init__(self, err_type, timestamp, message, tweet_id=None):
        self.err_type = err_type
        self.timestamp = timestamp
        self.message = message
        self.tweet_id = tweet_id

    def __repr__(self):
        err = {
            'type': self.err_type,
            'time': self.timestamp,
            'message': self.message,
            'tweet': self.tweet_id,
        }
        return err
