# Standard Library
from abc import (
    ABC,
    abstractmethod,
)

# My Stuff
from src.models.notion_calendar.calendar import Ride
from src.models.notion_calendar.route import Route


class AbstractView(ABC):
    @abstractmethod
    def get(self, ride: Ride, route: Route) -> str:
        raise NotImplementedError("Method get not implemented")
