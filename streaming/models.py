from termcolor import colored

class Tweet():

    def __init__(self, status):
        self.tweet_id = status['id']
        self.text = status['text']
        self.user_id = status['user']['id']
        self.user_name = status['user']['screen_name']

    def __repr__(self):
        return colored(self.user_name, 'blue') + ' ' + self.text

    def as_tuple(self):
        return (self.tweet_id,
                self.text,
                self.user_id,
                self.user_name)

class Retweet():

    def __init__(self, status):
        self.retweet_id = status['id']
        self.text = status['text']
        self.user_id = status['user']['id']
        self.user_name = status['user']['screen_name']
        self.retweeted_status_id = status['retweeted_status']['id']

    def __repr__(self):
        return colored(self.user_name, 'yellow') + ' ' + self.text

    def as_tuple(self):
        return (self.retweet_id,
                self.retweeted_status_id,
                self.text,
                self.user_id,
                self.user_name)

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
