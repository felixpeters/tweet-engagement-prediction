import sqlite3
from sqlite3 import Error

# define constants
CREATE_TWEETS_TABLE_SQL = """CREATE TABLE IF NOT EXISTS tweets (
tweet_id integer PRIMARY KEY,
text text NOT NULL,
user_id integer NOT NULL,
user_name text NOT NULL
);"""
CREATE_RETWEETS_TABLE_SQL = """CREATE TABLE IF NOT EXISTS retweets (
retweet_id integer PRIMARY KEY,
retweeted_status_id integer NOT NULL,
text text NOT NULL,
user_id integer NOT NULL,
user_name text NOT NULL,
FOREIGN KEY(retweeted_status_id) REFERENCES tweets(tweet_id)
);"""
CREATE_QUOTES_TABLE_SQL = """CREATE TABLE IF NOT EXISTS quotes (
quote_id integer PRIMARY KEY,
quoted_status_id integer NOT NULL,
text text NOT NULL,
user_id integer NOT NULL,
user_name text NOT NULL,
FOREIGN KEY (quoted_status_id) REFERENCES tweets(tweet_id)
);"""
CREATE_REPLIES_TABLE_SQL = """CREATE TABLE IF NOT EXISTS replies (
reply_id integer PRIMARY KEY,
replied_status_id integer NOT NULL,
text text NOT NULL,
user_id integer NOT NULL,
user_name text NOT NULL,
FOREIGN KEY (replied_status_id) REFERENCES tweets(tweet_id)
);"""

def create_connection(path):
    conn = sqlite3.connect(path)
    print("Connected to SQLite database created in {}".format(path))
    return conn

def create_tweets_table(conn):
    cur = conn.cursor()
    cur.execute(CREATE_TWEETS_TABLE_SQL)

def create_retweets_table(conn):
    cur = conn.cursor()
    cur.execute(CREATE_RETWEETS_TABLE_SQL)

def create_quotes_table(conn):
    cur = conn.cursor()
    cur.execute(CREATE_QUOTES_TABLE_SQL)

def create_replies_table(conn):
    cur = conn.cursor()
    cur.execute(CREATE_REPLIES_TABLE_SQL)

def save_tweet(conn, status):
    sql = """INSERT INTO tweets(tweet_id,text,user_id,user_name) 
    VALUES(?,?,?,?);"""
    cur = conn.cursor()
    cur.execute(sql, status)
    conn.commit()
    return cur.lastrowid
