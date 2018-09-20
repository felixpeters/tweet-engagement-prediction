import sqlite3
from sqlite3 import Error

# define constants
CREATE_TWEETS_TABLE = """CREATE TABLE IF NOT EXISTS tweets (
tweet_id integer PRIMARY KEY,
text text NOT NULL,
user text NOT NULL
);"""

def create_connection(path):
    conn = sqlite3.connect(path)
    print("Connected to SQLite database created in {}".format(path))
    return conn

def create_tweets_table(conn):
    cur = conn.cursor()
    cur.execute(CREATE_TWEETS_TABLE)

def save_tweet(conn, status):
    sql = "INSERT INTO tweets(id,text,user) VALUES(?,?,?);"
    cur = conn.cursor()
    cur.execute(sql, (status.id, status.text, status.user.screen_name))
    conn.commit()
    return cur.lastrowid
