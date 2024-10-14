# Standard Library
from abc import (
    ABC,
    abstractmethod,
)
from datetime import datetime


class AbstractSend(ABC):
    @abstractmethod
    def send(
        self,
        date: datetime,
    ) -> None:
        raise NotImplementedError("Method get not implemented")
