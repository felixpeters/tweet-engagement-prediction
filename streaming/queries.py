CREATE_TWEETS_TABLE = """CREATE TABLE IF NOT EXISTS tweets (
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
CREATE_RETWEETS_TABLE = """CREATE TABLE IF NOT EXISTS retweets (
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
CREATE_QUOTES_TABLE = """CREATE TABLE IF NOT EXISTS quotes (
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
CREATE_REPLIES_TABLE = """CREATE TABLE IF NOT EXISTS replies (
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
INSERT_TWEET = ""
INSERT_RETWEET = ""
INSERT_QUOTE = ""
INSERT_REPLY = ""
