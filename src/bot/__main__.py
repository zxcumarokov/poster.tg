# Standard Library
from os import getenv

# Third Party Stuff
import telebot
from dotenv import load_dotenv

# My Stuff
from src.handlers.start_message_handler import (
    StartMessageHandler,
)
from src.views.anounce import AnounceView

load_dotenv()

token = getenv('BOT_TOKEN',)
if not token:
    raise ValueError('Token is not set')
bot=telebot.TeleBot(token)

start_handler = StartMessageHandler(bot)
bot.register_message_handler(callback=start_handler.handle,commands=['start'],)

# Функция для обработки коллбэков
@bot.callback_query_handler(func=lambda call: call.data == "seen")
def handle_callback(call):
    # Увеличиваем счетчик
    user_clicks = user_clicks_dict.get(call.from_user.id, {"count": 0})
    
    # Отправляем сообщение с обновленным счетчиком
    message = AnounceView().create_message( user_clicks["count"] + 1 )
    markup = telebot.types.InlineKeyboardMarkup()
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=message,
        parse_mode="HTML",
        reply_markup=markup
    )

if __name__ == '__main__':
    bot.infinity_polling()


