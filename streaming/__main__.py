import os
import datetime
from twitter import Api, TwitterError
from dotenv import load_dotenv, find_dotenv
from termcolor import colored
from sqlite3 import IntegrityError
from tep.accountCollector import AccountCollector
from .database import create_connection, create_tweets_table, create_retweets_table, create_quotes_table, create_replies_table
from .processing import TweetProcessor
from .models import StreamError

# define constants
load_dotenv(find_dotenv())
CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET") 
ACCESS_TOKEN_KEY = os.getenv("TWITTER_ACCESS_TOKEN_KEY")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
USER_GROUP_PATH = os.getenv("USER_GROUP_PATH") or "data/user_ids.txt"
DB_PATH = os.getenv("DB_PATH") or "tweets.db"

# setup API connection
api = Api(CONSUMER_KEY,
          CONSUMER_SECRET,
          ACCESS_TOKEN_KEY,
          ACCESS_TOKEN_SECRET)

# setup DB connection
conn = create_connection(DB_PATH)
# create tables
create_tweets_table(conn)
create_retweets_table(conn)
create_quotes_table(conn)
create_replies_table(conn)

# create tweet processor
proc = TweetProcessor(conn)

# get user ids
ac = AccountCollector()
users = ac.load_user_ids(fname=USER_GROUP_PATH)
users_str = [str(u) for u in users]

def handle(tweet):
    if 'user' not in tweet:
        return
    user_id = tweet['user']['id']
    if user_id in users:
        proc.process_tweet(tweet)
    else:
        proc.process_engagement(tweet)

def handle_error(err_type, msg, tweet):
    tid = (tweet['id'] if ('id' in tweet) else None)
    err = StreamError(err_type, datetime.datetime.now(), msg, tid)
    print(err)


# run stream
def main():
    print(colored("Streaming tweets of {} users".format(len(users)), 'red'))
    for tweet in api.GetStreamFilter(follow=users_str):
        try:
            handle(tweet)
        except KeyError as err:
            handle_error('KeyError', err, tweet)
        except ValueError as err:
            handle_error('ValueError', err, tweet)
        except AttributeError as err:
            handle_error('AttributeError', err, tweet)
        except TwitterError as err:
            handle_error('TwitterError', err, tweet)
        except IntegrityError as err:
            handle_error('IntegrityError', err, tweet)
        except:
            handle_error('UnknownError', None, tweet)

if __name__ == '__main__':
    main()
