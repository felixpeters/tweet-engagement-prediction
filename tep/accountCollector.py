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

        Args:
            name: string
        Returns:
            New twitter.models.List instance
        """
        new_list = self.api.CreateList(name)
        return new_list

    def copy_all_users(self, source, target):
        """
        Copy all users from the source to the target list.

        Args:
            source: twitter.models.List instance to copy
            target: twitter.models.List instance to add users to
        Returns:
            Target list
        """
        users = self.api.GetListMembers(list_id=source.id, skip_status=True, include_entities=False)
        target = self.add_to_list(users, target)
        return target

    def add_to_list(self, users, target):
        """
        Add all given users to the target list.

        Args:
            users: Array of twitter.models.User instances
            target: twitter.models.List instance
        Returns:
            Target list
        """
        for user in users:
            target = self.api.CreateListsMember(list_id=target.id, user_id=user.id)
        return target

    def get_all_lists(self):
        """
        Return all lists for the authenticated user.
        """
        return self.api.GetLists()

    def delete_list(self, twitter_list):
        """
        Remove the given list.

        Args:
            list: twitter.models.List instance
        """
        self.api.DestroyList(list_id=twitter_list.id)
        return
