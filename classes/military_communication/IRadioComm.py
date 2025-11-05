from abc import abstractmethod, ABC

class IRadioComm(ABC):

    @abstractmethod
    def send_radio(self):
        pass

