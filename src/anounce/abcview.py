# Standard Library
from abc import (
    ABC,
    abstractmethod,
)


class AbstractViev(ABC):
    @abstractmethod
    def get(self) -> str:
        raise NotImplementedError("Method get not implemented")
