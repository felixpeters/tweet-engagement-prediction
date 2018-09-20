import os
import sqlite3
from sqlite3 import Error
from twitter import Api, TwitterError
from dotenv import load_dotenv, find_dotenv
from termcolor import colored
from tep.accountCollector import AccountCollector

# define constants
load_dotenv(find_dotenv())
CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET") 
ACCESS_TOKEN_KEY = os.getenv("TWITTER_ACCESS_TOKEN_KEY")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
USER_IDS_PATH = "data/user_ids.txt"
DB_PATH = "tweets.db"
CREATE_TABLE_SQL = """CREATE TABLE IF NOT EXISTS tweets (
tweet_id integer PRIMARY KEY,
text text NOT NULL,
user text NOT NULL
);"""

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    print("SQLite database created in {}".format(db_file))
    return conn

def create_table(conn, create_table_sql):
    c = conn.cursor()
    c.execute(create_table_sql)

def save_tweet(self, conn, status):
    sql = "INSERT INTO tweets(id,text,user) VALUES(?,?,?);"
    cur = conn.cursor()
    cur.execute(sql, (status.id, status.text, status.user.screen_name))
    conn.commit()
    return cur.lastrowid

def handle(tweet):
    user = tweet['user']
    if in_user_group(user['id']):
        process_tweet(tweet)
    else:
        process_engagement(tweet)

def process_tweet(tweet):
    user_name = tweet['user']['screen_name']
    text = tweet['text']
    print(colored(user_name, 'blue'), text)

def process_engagement(tweet):
    user_name = tweet['user']['screen_name']
    text = tweet['text']
    tweet_id = tweet['id']
    if 'retweeted_status' in tweet:
        print(colored(user_name, 'yellow'), text)
    elif 'quoted_status' in tweet:
        print(colored(user_name, 'cyan'), text)
    elif 'in_reply_to_status_id' in tweet:
        print(colored(user_name, 'magenta'), text)
    else:
        print(colored('Unknown tweet type', 'red'), tweet_id)
        
def in_user_group(id):
    if id in users:
        return True
    else:
        return False

# setup API connection
api = Api(CONSUMER_KEY,
          CONSUMER_SECRET,
          ACCESS_TOKEN_KEY,
          ACCESS_TOKEN_SECRET)

# setup DB connection
conn = create_connection(DB_PATH)
# create table
create_table(conn, CREATE_TABLE_SQL)

# get user ids
ac = AccountCollector()
users = ac.load_user_ids(fname=USER_IDS_PATH)
users_str = [str(u) for u in users]

# run stream
def main():
    print(colored("Streaming tweets of {} users".format(len(users)), 'red'))
    for tweet in api.GetStreamFilter(follow=users_str):
        try:
            handle(tweet)
        except KeyError as err:
            print(colored('KeyError', 'red'), err)
        except TwitterError as err:
            print(colored('TwitterError', 'red'), err)
        except:
            print(colored('Unknown error', 'red'))

if __name__ == '__main__':
    main()
