import tweepy
from telegram import Bot
import os
import time
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TWITTER_BEARER = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_USER_ID = os.getenv("TWITTER_USER_ID")

bot = Bot(token=TELEGRAM_TOKEN)
client = tweepy.Client(bearer_token=TWITTER_BEARER)

last_mention_id = None

def check_mentions():
    global last_mention_id
    mentions = client.get_users_mentions(id=TWITTER_USER_ID, since_id=last_mention_id)
    if mentions and mentions.data:
        for mention in reversed(mentions.data):
            msg = f"Упоминание от @{mention.author_id}:\n{mention.text}"
            bot.send_message(chat_id=CHAT_ID, text=msg)
            last_mention_id = mention.id

if __name__ == "__main__":
    while True:
        try:
            check_mentions()
        except Exception as e:
            print(f"Ошибка: {e}")
        time.sleep(60)