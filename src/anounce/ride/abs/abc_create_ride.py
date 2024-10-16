# Standard Library
from abc import (
    ABC,
    abstractmethod,
)

# My Stuff
from src.anounce.ride import Ride


class AbstractCreateRide(ABC):
    @abstractmethod
    def create(self, ride_properties: dict) -> Ride:
        raise NotImplementedError("Method get not imple mented")
