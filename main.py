# Creator : https://GitHub.com/BXBotz >< https://telegram.me/BX_Botz [@BXBotz]

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
 
Telegram = Client(
    "Telegram ID Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@Telegram.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.id)
    reply_markup = START_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )

# COMMANDS

START_TEXT = """🆔 Your Telegram ID : `{}`"""

# BUTTONS

START_BUTTON = InlineKeyboardMarkup(
             [[
             InlineKeyboardButton('♻️ Updates Channel ♻️', url=f"https://telegram.me/{Config.UPDATE_CHANNEL}")
             ]]
        )

Telegram.run()
