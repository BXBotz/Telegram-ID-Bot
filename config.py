import os

class Config(object):

    # get bot token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    # The Telegram API things
    # Get these values from my.telegram.org
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    # Update Channel Username
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL")
