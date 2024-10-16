# Standard Library
from abc import (
    ABC,
    abstractmethod,
)


class AbstractParseRoute(ABC):
    @abstractmethod
    def parse(self, route_database_id: str) -> dict:
        raise NotImplementedError("Method get not imple mented")
