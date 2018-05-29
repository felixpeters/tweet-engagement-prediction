import os
import twitter
from twitter.error import TwitterError
from dotenv import load_dotenv, find_dotenv
from .utils import is_newer_than, is_older_than

class TweetCollector():
    """
    Class for fetching tweets from the public Twitter API.
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
        print(self.api.VerifyCredentials())

    def get_tweets(self, user_ids, start, end, update_interval=50):
        """
        Fetches tweets from the given time frame for the specified users.

        Args:
            user_ids: Array of integers representing the users
            start: non-naive datetime (including timezone info)
            end: non-naive datetime (including timezone info)
            update_interval: Number of iterations before an update on current total will be displayed
        Returns:
            Array of twitter.models.Status instances
        """
        tweets = []
        print("Starting data collection...")
        for index, user_id in enumerate(user_ids, start=1):
            if index % update_interval == 1:
                print("Total tweets after {0:d} steps: {1:,d}".format(index-1, len(tweets)))
            try:
                tweets += self.get_tweets_for_time_frame(user_id, start, end)
            except TwitterError:
                print("Error occurred when collecting tweets for user {0:d}".format(user_id))
        print("Terminating data collection with total of {0:d} tweets".format(len(tweets)))
        return tweets

    def get_tweets_for_time_frame(self, user_id, start, end):
        """
        Fetches tweets within the given time frame for a single user.

        Args:
            user_id: Integer representing the desired user
            start: non-naive datetime (including timezone info)
            end: non-naive datetime (including timezone info)
        Returns:
            Array of twitter.models.Status instances
        """
        tweets = []
        max_id = None
        total_tweets = 0
        while True:
            page = self.api.GetUserTimeline(user_id=user_id, count=200, max_id=max_id)
            tweets += page
            total_tweets += len(page)
            if len(page) > 0 and is_newer_than(page[-1], start):
                max_id = page[-1].id - 1
            else:
                break
        tweets = [t for t in tweets if (is_newer_than(t, start) and is_older_than(t, end))]
        return tweets
