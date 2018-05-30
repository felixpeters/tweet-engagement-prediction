from datetime import tzinfo, datetime
import numpy as np
from dateutil.parser import parse
from .utils import UTC

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
            ["Follower count", "followers"],
            ["Friend count", "friends"],
            ["Verified user", "verified"],
            ["User listings", "listings"],
            ["User tweet count", "tweets"],
            ["User overall tweet frequency", "tweet_freq"],
            ["User favorite count", "favorites"],
            ["User overall favorite frequency", "favorite_freq"],
            ["User account age", "account_age"],
            ["Hour of tweet creation", "hour"],
            ["Quoted tweet", "quote"]
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
        followers = (tweet.user.followers_count if tweet.user.followers_count != None else 0)
        friends = (tweet.user.friends_count if tweet.user.friends_count != None else 0)
        listings = (tweet.user.listed_count if tweet.user.listed_count != None else 0)
        statuses = (tweet.user.statuses_count if tweet.user.statuses_count != None else 0)
        favorites = (tweet.user.favourites_count if tweet.user.favourites_count != None else 0)
        features = [
            len(tweet.urls),
            len(tweet.hashtags),
            len(tweet.user_mentions),
            len(tweet.text),
            followers,
            friends,
            (1 if tweet.user.verified else 0),
            listings,
            statuses,
            float(statuses) / float(self.get_account_age(tweet.user)),
            favorites,
            float(favorites) / float(self.get_account_age(tweet.user)),
            self.get_account_age(tweet.user),
            self.get_creation_hour(tweet),
            (1 if tweet.quoted_status != None else 0)
        ]
        return features

    def get_account_age(self, user):
        """
        Returns the account age in days

        Args:
            user: twitter.models.user instance
        Returns:
            Integer representing the account age in days
        """
        td = datetime.now(tz=UTC()) - parse(user.created_at)
        return td.days
    
    def get_creation_hour(self, tweet):
        """
        Returns the hour the tweet was created in.

        Args:
            tweet: twitter.models.status instance
        Returns:
            Float representing the hour the tweet was created
        """
        date = parse(tweet.created_at)
        return date.hour

