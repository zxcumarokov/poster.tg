# Standard Library
from abc import (
    ABC,
    abstractmethod,
)
from datetime import datetime

# My Stuff
from src.models.notion_calendar.calendar import Ride


class AbstractParseNotion(ABC):
    @abstractmethod
    def parse(self, date: datetime) -> Ride:
        raise NotImplementedError("Method get not implemented")
