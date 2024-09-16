from dotenv import load_dotenv
from os import getenv
import telebot
from src.handlers.start_message_handler import StartMessageHandler

load_dotenv()

token = getenv('BOT_TOKEN')
if not token:
    raise ValueError('Token is not set')
bot=telebot.TeleBot(token)

start_handler = StartMessageHandler(bot)
bot.register_message_handler(callback=start_handler.handle,commands=['start'],)

if __name__ == '__main__':
    bot.infinity_polling()


