from abc import ABC, abstractmethod


class IFly(ABC):

    @abstractmethod
    def fly(self):
        pass