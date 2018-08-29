from datetime import tzinfo, datetime
import numpy as np
from dateutil.parser import parse
from .utils import UTC
from .featureStore import *

class FeatureGenerator():
    """
    Class for extracting features from tweet objects.
    """

    def __init__(self):
        """
        Initialize feature documentation
        """
        self.structured_features = [
            ["URL count", "urls"],
            ["Hashtag count", "hashtags"],
            ["Mention count", "mentions"],
            ["Tweet length", "length"],
            ["Tweet sentiment", "sentiment"],
            ["Follower count", "followers"],
            ["Friend count", "friends"],
            ["Follower friend ratio", "follower_friend_ratio"],
            ["Verified user", "verified"],
            ["User listings", "listings"],
            ["User tweet count", "tweets"],
            ["User overall tweet frequency", "tweet_freq"],
            ["User favorite count", "favorites"],
            ["User overall favorite frequency", "favorite_freq"],
            ["User account age", "account_age"],
            ["Month of tweet creation", "month"],
            ["Day of tweet creation", "day"],
            ["Weekday of tweet creation", "weekday"],
            ["Hour of tweet creation", "hour"],
            ["Minute of tweet creation", "minute"],
            ["Quoted tweet", "quote"],
            ["Quoted tweet popularity", "quoted_popularity"],
            ["Quoted tweet sentiment", "quoted_sentiment"],
            ["Reply tweet", "reply"],
        ]

    def structured_feature_map(self):
        """
        Returns documentation of the simple features.

        Returns:
            Array of feature names
            Array of feature identifiers
        """
        features = np.array(self.structured_features)
        return (features[:, 0], features[:, 1])


    def extract_structured_features(self, tweets):
        """
        Returns all simple features for the given tweets.

        Args:
            tweets: Array of twitter.models.status instances
        Returns:
            Numpy array containing a row of features for every tweet.
        """
        features = np.zeros((len(tweets), len(self.structured_features)))
        for i, tweet in enumerate(tweets):
            features[i] = self.extract_structured_features_for_tweet(tweet)
        return features

    def extract_structured_features_for_tweet(self, tweet):
        """
        Extracts the simple features for a single tweet instance.

        Args:
            tweet: twitter.models.status instance
        Returns:
            One-dimensional numpy array containing the simple features
        """
        features = [
            urls(tweet),
            hashtags(tweet),
            mentions(tweet),
            length(tweet),
            sentiment(tweet),
            followers(tweet),
            friends(tweet),
            follower_friend_ratio(tweet),
            verified(tweet),
            listings(tweet),
            statuses(tweet),
            tweet_freq(tweet),
            favorites(tweet),
            fav_freq(tweet),
            account_age(tweet),
            creation_month(tweet),
            creation_day(tweet),
            creation_weekday(tweet),
            creation_hour(tweet),
            creation_minute(tweet),
            quoted(tweet),
            quoted_popularity(tweet),
            quoted_sentiment(tweet),
            replied(tweet),
        ]
        return features
