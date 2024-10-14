# Third Party Stuff
from telebot import TeleBot
from telebot.types import Message

# My Stuff
from src.models.bot import IMessageHandler


class CallBackHandler(IMessageHandler):
    def __init__(self, bot: TeleBot):
        self.bot = bot

    def handle(self, message: Message) -> None:
        self.bot.send_message(-1002366288749, "Привет")
