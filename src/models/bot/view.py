from abc import ABC, abstractmethod

class IView(ABC):
    @abstractmethod
    def get(self)-> str:
        """
        Return prepared anounce text
        """
        raise NotImplementedError

