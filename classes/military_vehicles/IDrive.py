from abc import ABC, abstractmethod


class IDrive(ABC):

    @abstractmethod
    def drive(self):
        pass