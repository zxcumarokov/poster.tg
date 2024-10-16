# Standard Library
from abc import (
    ABC,
    abstractmethod,
)

# My Stuff
from src.anounce.route import Route


class AbstractCreateRoute(ABC):
    @abstractmethod
    def create_route(self, route_properties: dict) -> Route:
        raise NotImplementedError("Method get not imple mented")
