# Standard Library
from abc import (
    ABC,
    abstractmethod,
)

# My Stuff
from src.models.notion_calendar.calendar import Ride


class AbstractCreateRide(ABC):
    @abstractmethod
    def create_ride(self, ride_properties: dict) -> Ride:
        raise NotImplementedError("Method get not implemented")
