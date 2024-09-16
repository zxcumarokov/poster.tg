from abc import ABC, abstractmethod
from telebot.types import Message 

class IMessageHandler(ABC):
    @abstractmethod
    def handle(self, message: Message):
        raise NotImplementedError
