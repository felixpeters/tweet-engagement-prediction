import os
from datetime import tzinfo, datetime
import twitter
from twitter.error import TwitterError
from dotenv import load_dotenv, find_dotenv
import numpy as np
from dateutil.parser import parse
from .utils import UTC

class UserAnalyzer():
    """
    Class for examining user accounts.
    """

    def __init__(self):
        """
        Initialize API connection
        """
        load_dotenv(find_dotenv())
        CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
        CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET") 
        ACCESS_TOKEN_KEY = os.getenv("TWITTER_ACCESS_TOKEN_KEY")
        ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        self.api = twitter.Api(
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            access_token_key=ACCESS_TOKEN_KEY,
            access_token_secret=ACCESS_TOKEN_SECRET,
            sleep_on_rate_limit=True
        )
        self.feature_map = [
            'followers',
            'friends',
            'verified',
            'listings',
            'age',
            'tweet_freq',
            'fav_freq'
        ]
        print(self.api.VerifyCredentials())

    def get_users(self, user_ids):
        """
        Lookup users for given IDs.
        """
        users = []
        for user_id in user_ids:
            try:
                user = self.api.GetUser(user_id=user_id)
                users.append(user)
            except TwitterError:
                print("Error occurred when collecting user account {0:d}".format(user_id))
        return users

    def extract_user_features(self, users):
        """
        Fetch structured features related to user, and return them as a
        numpy array.
        """
        features = np.zeros((len(users), len(self.feature_map)))
        for index, user in enumerate(users):
            followers = (user.followers_count if user.followers_count != None else 0)
            friends = (user.friends_count if user.friends_count != None else 0)
            verified = (1 if user.verified else 0)
            listings = (user.listed_count if user.listed_count != None else 0)
            age = self.get_account_age(user)
            statuses = (user.statuses_count if user.statuses_count != None else 0)
            favorites = (user.favourites_count if user.favourites_count != None else 0)
            tweet_freq = float(statuses) / float(age)
            fav_freq = float(favorites) / float(age)
            user_features = [
                followers,
                friends,
                verified,
                listings,
                age,
                tweet_freq,
                fav_freq
            ]
            features[index] = user_features
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
