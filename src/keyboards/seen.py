from src.models.bot import IKeyboard
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

class SeenKeyboard(IKeyboard):
    def get(self)->InlineKeyboardMarkup:
        button = InlineKeyboardButton(text='Увидел', callback_data='seen')
        keyboard = InlineKeyboardMarkup()
        keyboard.add(button)
        return keyboard
