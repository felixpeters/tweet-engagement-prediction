from termcolor import colored

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
