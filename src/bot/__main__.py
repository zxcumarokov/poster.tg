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

# Функция для обработки коллбэков
@bot.callback_query_handler(func=lambda call: call.data == "seen")
def handle_callback(call):
    # Увеличиваем счетчик
    user_clicks["count"] += 1
    
    # Отправляем сообщение с обновленным счетчиком
    message, markup = create_message()
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=message,
        parse_mode="HTML",
        reply_markup=markup
    )

if __name__ == '__main__':
    bot.infinity_polling()


