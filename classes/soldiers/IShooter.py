from abc import ABC, abstractmethod

class IShooter(ABC):

    @abstractmethod
    def shoot(self):
        pass