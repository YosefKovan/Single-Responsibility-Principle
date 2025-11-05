from abc import abstractmethod, ABC

class ISatelliteComm(ABC):

    @abstractmethod
    def send_satellite(self):
        pass
