from abc import ABC, abstractmethod
from telebot.types import InlineKeyboardMarkup

class IKeyboard(ABC):
    @abstractmethod
    def get(self)-> InlineKeyboardMarkup:
        raise NotImplementedError
