import os
import sqlite3
from sqlite3 import Error
import tweepy
from dotenv import load_dotenv, find_dotenv
from termcolor import colored
from tep.accountCollector import AccountCollector

# override tweepy.StreamListener to add logic
class PersistListener(tweepy.StreamListener):

    def __init__(self, conn):
        super(PersistListener, self).__init__()
        self.conn = conn

    def save_tweet(self, status):
        sql = "INSERT INTO tweets(id,text,user) VALUES(?,?,?);"
        cur = self.conn.cursor()
        cur.execute(sql, (status.id, status.text, status.user.screen_name))
        self.conn.commit()
        return cur.lastrowid

    def on_status(self, status):
        print(colored(status.user.screen_name, 'green'), status.text)
        self.save_tweet(status)

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    print("SQLite database created in {}".format(db_file))
    return conn

def create_table(conn, create_table_sql):
    c = conn.cursor()
    c.execute(create_table_sql)

# constants
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

# setup API connection
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# setup DB connection
conn = create_connection(DB_PATH)
# create table
create_table(conn, CREATE_TABLE_SQL)

# get user ids
ac = AccountCollector()
users = ac.load_user_ids(fname=USER_IDS_PATH)
users = [str(u) for u in users]

# create stream and listener
listener = PersistListener(conn)
stream = tweepy.Stream(auth=api.auth, listener=listener)

# run stream
print(colored("Streaming tweets of {} users".format(len(users)), 'red'))
stream.filter(follow=users)
