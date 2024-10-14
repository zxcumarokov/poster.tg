# Standard Library
from abc import (
    ABC,
    abstractmethod,
)

# Third Party Stuff
from telebot.types import Message


class IMessageHandler(ABC):
    @abstractmethod
    def handle(self, message: Message) -> None:
        raise NotImplementedError
