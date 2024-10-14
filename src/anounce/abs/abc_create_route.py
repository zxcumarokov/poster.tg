# Standard Library
from abc import (
    ABC,
    abstractmethod,
)

# My Stuff
from src.models.notion_calendar.route import Route


class AbstractCreateRoute(ABC):
    @abstractmethod
    def create_route(self, route_properties: dict) -> Route:
        raise NotImplementedError
