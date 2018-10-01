from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
import sqlite3
import sys
from dotenv import load_dotenv, find_dotenv

# define constants
load_dotenv(find_dotenv())
ARGS =  sys.argv
DB_PATH = ARGS[1]
TO_MAIL_ADDRESS = ARGS[2]
PROCESS_NAME = ARGS[3]
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
FROM_MAIL_ADDRESS = os.getenv("FROM_MAIL_ADDRESS")
FROM_MAIL_PASSWORD = os.getenv("FROM_MAIL_PASSWORD")

# connect to database
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# get stats
cur.execute('SELECT count(*) FROM tweets')
tweet_count = cur.fetchone()[0]
cur.execute('SELECT count(*) FROM retweets')
retweet_count = cur.fetchone()[0]
cur.execute('SELECT count(*) FROM quotes')
quote_count = cur.fetchone()[0]
cur.execute('SELECT count(*) FROM replies')
reply_count = cur.fetchone()[0]

# assemble message
msg = MIMEMultipart()
msg['From'] = FROM_MAIL_ADDRESS
msg['To'] = TO_MAIL_ADDRESS
msg['Subject'] = "[DAILY UPDATE] {}".format(PROCESS_NAME)
body = """
Hi,

this is your daily update of the Twitter stream you are monitoring.

Total tweets: {:,d}
Total retweets: {:,d}
Total quotes: {:,d}
Total replies: {:,d}

Check the logs for any errors that might have occurred during tweet collection.
""".format(tweet_count, retweet_count, quote_count, reply_count)
msg.attach(MIMEText(body, 'plain'))

# send email
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(FROM_MAIL_ADDRESS, FROM_MAIL_PASSWORD)
text = msg.as_string()
server.sendmail(FROM_MAIL_ADDRESS, TO_MAIL_ADDRESS, text)
server.quit()
