from termcolor import colored

class Tweet():

    def __init__(self, status):
        self.tweet_id = status['id']
        self.created_at = status['created_at']
        self.text = status['text']
        self.lang = status['lang']
        self.favorite_count = status['favorite_count']
        self.retweet_count = status['retweet_count']
        self.hashtag_count = len(status['hashtags'])
        self.url_count = len(status['urls'])
        self.mention_count = len(status['user_mentions'])
        self.media_count = len(status['media'])
        self.quoted_status = (True if status['quoted_status'] != None else False)
        self.quoted_status_id = (status['quoted_status_id'] if status['quoted_status_id'] != None else None)
        self.quoted_user_id = (status['quoted_status']['user']['id'] if status['quoted_status'] != None else None)
        self.replied_status = (True if status['in_reply_to_status_id'] != None else False)
        self.replied_status_id = (status['in_reply_to_status_id'] if status['in_reply_to_status_id'] != None else None)
        self.replied_user_id = (status['in_reply_to_user_id'] if status['in_reply_to_user_id'] != None else None)
        self.user_id = status['user']['id']
        self.user_name = status['user']['screen_name']
        self.user_created_at = status['user']['created_at']
        self.user_followers = status['user']['followers']
        self.user_frieds = status['user']['friends']
        self.user_statuses = status['user']['statuses_count']
        self.user_listings = status['user']['listed_count']
        self.user_verified = status['user']['verified']
        self.user_favorites = status['user']['favourites_count']
        self.user_utc_offset = status['user']['utc_offset']

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
                self.user_frieds,
                self.user_statuses,
                self.user_listings,
                self.user_verified,
                self.user_favorites,
                self.user_utc_offset)

class Retweet():

    def __init__(self, status):
        self.retweet_id = status['id']
        self.retweeted_status_id = status['retweeted_status']['id']
        self.created_at = status['created_at']
        self.text = status['text']
        self.user_id = status['user']['id']
        self.user_name = status['user']['screen_name']
        self.user_created_at = status['user']['created_at']
        self.user_followers = status['user']['followers']
        self.user_frieds = status['user']['friends']
        self.user_statuses = status['user']['statuses_count']
        self.user_listings = status['user']['listed_count']
        self.user_verified = status['user']['verified']
        self.user_favorites = status['user']['favourites_count']
        self.user_utc_offset = status['user']['utc_offset']

    def __repr__(self):
        return colored(self.user_name, 'yellow') + ' ' + self.text

    def as_tuple(self):
        return (self.retweet_id,
                self.retweeted_status_id,
                self.created_at,
                self.text,
                self.user_id,
                self.user_name,
                self.user_created_at,
                self.user_followers,
                self.user_frieds,
                self.user_statuses,
                self.user_listings,
                self.user_verified,
                self.user_favorites,
                self.user_utc_offset)

class Quote():

    def __init__(self, status):
        self.quote_id = status['id']
        self.quoted_status_id = status['quoted_status']['id']
        self.text = status['text']
        self.user_id = status['user']['id']
        self.user_name = status['user']['screen_name']

    def __repr__(self):
        return colored(self.user_name, 'cyan') + ' ' + self.text

    def as_tuple(self):
        return (self.quote_id,
                self.quoted_status_id,
                self.text,
                self.user_id,
                self.user_name)

class Reply():

    def __init__(self, status):
        self.reply_id = status['id']
        self.replied_status_id = status['in_reply_to_status_id']
        self.text = status['text']
        self.user_id = status['user']['id']
        self.user_name = status['user']['screen_name']

    def __repr__(self):
        return colored(self.user_name, 'magenta') + ' ' + self.text

    def as_tuple(self):
        return (self.reply_id,
                self.replied_status_id,
                self.text,
                self.user_id,
                self.user_name)
