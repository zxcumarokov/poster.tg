# Standard Library
from abc import (
    ABC,
    abstractmethod,
)
from datetime import datetime
from typing import Dict


class AbstractParseNotion(ABC):
    @abstractmethod
    def parse(self, date: datetime) -> Dict:
        raise NotImplementedError("Method get not implemented")
