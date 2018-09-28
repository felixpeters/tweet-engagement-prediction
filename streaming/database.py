import sqlite3
from sqlite3 import Error
from .queries import CREATE_TWEETS_TABLE, CREATE_RETWEETS_TABLE, CREATE_QUOTES_TABLE, CREATE_REPLIES_TABLE, INSERT_TWEET, INSERT_RETWEET, INSERT_QUOTE, INSERT_REPLY

def create_connection(path):
    conn = sqlite3.connect(path)
    print("Connected to SQLite database created in {}".format(path))
    return conn

def create_tweets_table(conn):
    cur = conn.cursor()
    cur.execute(CREATE_TWEETS_TABLE)

def create_retweets_table(conn):
    cur = conn.cursor()
    cur.execute(CREATE_RETWEETS_TABLE)

def create_quotes_table(conn):
    cur = conn.cursor()
    cur.execute(CREATE_QUOTES_TABLE)

def create_replies_table(conn):
    cur = conn.cursor()
    cur.execute(CREATE_REPLIES_TABLE)

def save_tweet(conn, tweet):
    cur = conn.cursor()
    cur.execute(INSERT_TWEET, tweet.as_tuple())
    conn.commit()
    return cur.lastrowid

def save_retweet(conn, retweet):
    cur = conn.cursor()
    cur.execute(INSERT_RETWEET, retweet.as_tuple())
    conn.commit()
    return cur.lastrowid

def save_quote(conn, quote):
    cur = conn.cursor()
    cur.execute(INSERT_QUOTE, quote.as_tuple())
    conn.commit()
    return cur.lastrowid

def save_reply(conn, reply):
    cur = conn.cursor()
    cur.execute(INSERT_REPLY, reply.as_tuple())
    conn.commit()
    return cur.lastrowid
