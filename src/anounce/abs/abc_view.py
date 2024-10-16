# Standard Library
from abc import (
    ABC,
    abstractmethod,
)

# My Stuff
from src.anounce.ride.model import Ride


class AbstractView(ABC):
    @abstractmethod
    def get(self, ride: Ride) -> str:
        raise NotImplementedError("Method get not implemented")
