def status_id(status):
    return status['id']

def retweeted_status_id(status):
    return status['retweeted_status']['id']

def quote_id(status):
    return status['quoted_status']['id']

def tweet_creation_date(status):
    return status['created_at']

def text(status):
    return status['text']

def lang(status):
    return status['lang']

def favorite_count(status):
    count = (status['favorite_count'] if ('favorite_count' in status) else 0)
    return count

def retweet_count(status):
    count = (status['retweet_count'] if ('retweet_count' in status) else 0)
    return count

def hashtag_count(status):
    count = (len(status['hashtags']) if ('hashtags' in status) else 0)
    return count

def url_count(status):
    count = (len(status['urls']) if ('urls' in status) else 0)
    return count

def mention_count(status):
    count = (len(status['user_mentions']) if ('user_mentions' in status) else 0)
    return count

def media_count(status):
    count = (len(status['media']) if ('media' in status) else 0)
    return count

def is_quote(status):
    quote = (True if ('quoted_status' in status and (status['quoted_status'] != None)) else False)
    return quote

def quoted_status_id(status):
    qid = (status['quoted_status_id'] if ('quoted_status_id' in status) else None)
    return qid

def quoted_user_id(status):
    uid = (status['quoted_status']['user']['id'] if ('quoted_status' in status and (status['quoted_status'] != None)) else None)
    return uid

def is_reply(status):
    reply = (True if ('in_reply_to_status_id' in status and (status['in_reply_to_status_id'] != None)) else False)
    return reply

def replied_status_id(status):
    rid = (status['in_reply_to_status_id'] if ('in_reply_to_status_id' in status) else None)
    return rid

def replied_user_id(status):
    uid = (status['in_reply_to_user_id'] if ('in_reply_to_user_id' in status) else None)
    return uid

def user_id(status):
    return status['user']['id']

def user_name(status):
    return status['user']['screen_name']

def user_creation_date(status):
    return status['user']['created_at']

def user_followers(status):
    return status['user']['followers_count']

def user_friends(status):
    return status['user']['friends_count']

def user_statuses(status):
    return status['user']['statuses_count']

def user_listings(status):
    return status['user']['listed_count']

def user_verified(status):
    return status['user']['verified']

def user_favorites(status):
    return status['user']['favourites_count']

def user_utc_offset(status):
    offset = (status['user']['utc_offset'] or 0)
    return offset
