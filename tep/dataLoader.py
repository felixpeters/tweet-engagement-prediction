import json
import random
from twitter import Status, Url, User, Hashtag

class DataLoader():
    """
    Class for loading and transforming data from json files
    """

    def load_from_file(self, filename, ignore_retweets=True, sample=False):
        """
        Loads tweets from a json-encoded file. Tweets need to be separated by
        newlines.

        Args:
            filename: String representing the filename
        Returns:
            Array of twitter.models.status instances
        """
        data = []
        with open(filename) as f:
            for line in f:
                data.append(json.loads(line))
        tweets = [self.new_tweet_from_json(d) for d in data]
        if ignore_retweets:
            tweets = self.filter_retweets(tweets)
        if sample:
            tweets = random.sample(tweets, sample)
        return tweets

    def filter_retweets(self, tweets):
        """
        Filters out retweets, keeping only native tweets and quotes.

        Args:
            tweets: Array of twitter.models.status instances
        Returns:
            Array of twitter.models.status instances
        """
        tweets = [t for t in tweets if t.retweeted_status == None]
        return tweets

    def new_tweet_from_json(self, data):
        """
        Converts a json string to a tweet instance.

        Args:
            data: json string containing twitter data
        Returns:
            twitter.models.status instance
        """
        tweet = Status.NewFromJsonDict(data)
        if 'urls' in data:
            tweet.urls = [Url.NewFromJsonDict(u) for u in data['urls']]
        else:
            tweet.urls = []
        if 'user_mentions' in data:
            tweet.user_mentions = [User.NewFromJsonDict(u) for u in data['user_mentions']]
        else:
            tweet.user_mentions = []
        if 'hashtags' in data:
            tweet.hashtags = [Hashtag.NewFromJsonDict(h) for h in data['hashtags']]
        else:
            tweet.hashtags = []
        return tweet
