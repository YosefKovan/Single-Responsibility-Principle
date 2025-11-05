from abc import abstractmethod, ABC

class IMorseComm(ABC):

    @abstractmethod
    def morse(self):
        pass