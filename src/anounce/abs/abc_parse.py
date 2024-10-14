# Standard Library
from abc import (
    ABC,
    abstractmethod,
)
from datetime import datetime

# My Stuff


class AbstractParseNotion(ABC):
    @abstractmethod
    def parse(self, date: datetime) -> dict:
        raise NotImplementedError("Method get not imple mented")
