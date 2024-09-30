# Standard Library
from os import getenv

# Third Party Stuff
import telebot
from dotenv import load_dotenv

# My Stuff
from src.anounce.parseroute import NotionDataFetcher
from src.keyboards import SeenKeyboard
from src.views import AnounceView

load_dotenv()

token = getenv('BOT_TOKEN')
if not token:
    raise ValueError('Token is not set')
bot = telebot.TeleBot(token)

channel_id = getenv('CHANNEL_ID')
if not channel_id:
    raise ValueError ('Channel Id is not set')



api_token = getenv('NOTION_API_TOKEN')
database_id = getenv('NOTION_DATABASE_ID')
fetcher = NotionDataFetcher(api_token, database_id)
anounce_view = AnounceView(fetcher)
seen_keyboard = SeenKeyboard()

if __name__ == '__main__':
    bot.send_message(
        chat_id=channel_id, 
        text=anounce_view.get(), 
        parse_mode="HTML",
        reply_markup=seen_keyboard.get()
    )
