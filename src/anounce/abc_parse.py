# Standard Library
from abc import (
    ABC,
    abstractmethod,
)

# My Stuff
from src.models.notion_calendar.calendar import Ride


class AbstractParseNotion:
    @abstractmethod
    def parse(self) -> Ride:
        raise NotImplementedError("Method get not imple mented")
