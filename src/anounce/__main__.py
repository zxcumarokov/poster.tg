from dotenv import load_dotenv
from os import getenv
import telebot
from src.views import AnounceView
from src.keyboards import SeenKeyboard

load_dotenv()

token = getenv('BOT_TOKEN')
if not token:
    raise ValueError('Token is not set')
bot = telebot.TeleBot(token)

channel_id = getenv('CHANNEL_ID')
if not channel_id:
    raise ValueError ('Channel Id is not set')

anounce_view = AnounceView()
seen_keyboard = SeenKeyboard()

if __name__ == '__main__':
    bot.send_message(
        chat_id=channel_id, 
        text=anounce_view.get(), 
        parse_mode="HTML",
        reply_markup=seen_keyboard.get()
    )
