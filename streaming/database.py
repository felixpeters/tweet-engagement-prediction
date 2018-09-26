import sqlite3
from sqlite3 import Error

# define constants
CREATE_TWEETS_TABLE_SQL = """CREATE TABLE IF NOT EXISTS tweets (
tweet_id integer PRIMARY KEY,
created_at text NOT NULL,
text text NOT NULL,
lang text,
favorite_count integer NOT NULL,
retweet_count integer NOT NULL,
hashtag_count integer NOT NULL,
url_count integer NOT NULL,
mention_count integer NOT NULL,
media_count integer NOT NULL,
quoted_status boolean NOT NULL,
quoted_status_id integer,
quoted_user_id integer,
replied_status boolean NOT NULL,
replied_status_id integer,
replied_user_id integer,
user_id integer NOT NULL,
user_name text NOT NULL,
user_created_at text NOT NULL,
user_followers integer NOT NULL,
user_friends integer NOT NULL,
user_statuses integer NOT NULL,
user_listings integer NOT NULL,
user_verified boolean NOT NULL,
user_favorites integer NOT NULL,
user_utc_offset integer NOT NULL
);"""
CREATE_RETWEETS_TABLE_SQL = """CREATE TABLE IF NOT EXISTS retweets (
retweet_id integer PRIMARY KEY,
retweeted_status_id integer,
created_at text NOT NULL,
text text NOT NULL,
user_id integer NOT NULL,
user_name text NOT NULL,
user_created_at text NOT NULL,
user_followers integer NOT NULL,
user_friends integer NOT NULL,
user_statuses integer NOT NULL,
user_listings integer NOT NULL,
user_verified boolean NOT NULL,
user_favorites integer NOT NULL,
user_utc_offset integer NOT NULL
FOREIGN KEY(retweeted_status_id) REFERENCES tweets(tweet_id)
);"""
CREATE_QUOTES_TABLE_SQL = """CREATE TABLE IF NOT EXISTS quotes (
quote_id integer PRIMARY KEY,
quoted_status_id integer,
created_at text NOT NULL,
text text NOT NULL,
lang text,
favorite_count integer NOT NULL,
retweet_count integer NOT NULL,
hashtag_count integer NOT NULL,
url_count integer NOT NULL,
mention_count integer NOT NULL,
media_count integer NOT NULL,
user_id integer NOT NULL,
user_name text NOT NULL,
user_created_at text NOT NULL,
user_followers integer NOT NULL,
user_friends integer NOT NULL,
user_statuses integer NOT NULL,
user_listings integer NOT NULL,
user_verified boolean NOT NULL,
user_favorites integer NOT NULL,
user_utc_offset integer NOT NULL
FOREIGN KEY (quoted_status_id) REFERENCES tweets(tweet_id)
);"""
CREATE_REPLIES_TABLE_SQL = """CREATE TABLE IF NOT EXISTS replies (
reply_id integer PRIMARY KEY,
replied_status_id integer,
created_at text NOT NULL,
text text NOT NULL,
lang text,
favorite_count integer NOT NULL,
retweet_count integer NOT NULL,
hashtag_count integer NOT NULL,
url_count integer NOT NULL,
mention_count integer NOT NULL,
media_count integer NOT NULL,
user_id integer NOT NULL,
user_name text NOT NULL,
user_created_at text NOT NULL,
user_followers integer NOT NULL,
user_friends integer NOT NULL,
user_statuses integer NOT NULL,
user_listings integer NOT NULL,
user_verified boolean NOT NULL,
user_favorites integer NOT NULL,
user_utc_offset integer NOT NULL
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

def save_tweet(conn, tweet):
    sql = """INSERT INTO tweets(tweet_id,text,user_id,user_name) 
    VALUES(?,?,?,?);"""
    cur = conn.cursor()
    cur.execute(sql, tweet.as_tuple())
    conn.commit()
    return cur.lastrowid

def save_retweet(conn, retweet):
    sql = """INSERT INTO retweets(retweet_id,retweeted_status_id,text,user_id,user_name) 
    VALUES(?,?,?,?,?);"""
    cur = conn.cursor()
    cur.execute(sql, retweet.as_tuple())
    conn.commit()
    return cur.lastrowid

def save_quote(conn, quote):
    sql = """INSERT INTO quotes(quote_id,quoted_status_id,text,user_id,user_name) 
    VALUES(?,?,?,?,?);"""
    cur = conn.cursor()
    cur.execute(sql, quote.as_tuple())
    conn.commit()
    return cur.lastrowid

def save_reply(conn, reply):
    sql = """INSERT INTO replies(reply_id,replied_status_id,text,user_id,user_name) 
    VALUES(?,?,?,?,?);"""
    cur = conn.cursor()
    cur.execute(sql, reply.as_tuple())
    conn.commit()
    return cur.lastrowid
