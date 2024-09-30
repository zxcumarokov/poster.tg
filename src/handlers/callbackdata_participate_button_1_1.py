from src.models.bot import IMessageHandler
from telebot import TeleBot
from telebot.types import Message

class CallBackHandler(IMessageHandler):
    def __init__(self, bot: TeleBot):
        self.bot = bot

    def handle(self, message: Message):
        self.bot.send_message(-1002366288749, "Привет")
