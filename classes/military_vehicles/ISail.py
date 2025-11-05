from abc import ABC, abstractmethod

class ISail(ABC):

    @abstractmethod
    def sail(self):
        pass