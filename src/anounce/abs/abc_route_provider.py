# Standard Library
from abc import (
    ABC,
    abstractmethod,
)


class AbstractRouteProvider(ABC):
    @abstractmethod
    def get_route_id(self) -> int:
        raise NotImplementedError("Method get not imple mented")
