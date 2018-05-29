import os
import twitter
from dotenv import load_dotenv, find_dotenv

class AccountCollector():
    """
    Class for assembling Twitter lists comprising users whose tweets should
    be included in the data set.
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

    def load_users_from_file(self, fname):
        """
        Load user screen names from file with the given name and get account
        data via the API.
        """
        users = []
        with open(fname) as f:
            for username in f:
                user = self.get_user_by_name(username.strip())
                users.append(user)
        return users

    def get_user_by_name(self, name):
        """
        Lookup user with the given name in the API.
        """
        user = self.api.GetUser(screen_name=name)
        return user

    def create_new_list(self, name):
        """
        Create new Twitter list with given name.
        """
        return

    def copy_all_users(self, source, target):
        """
        Copy all users from the source to the target list.
        """
        return

    def add_to_list(self, users, target):
        """
        Add all given users to the target list.
        """
        return
