from abc import ABC, abstractmethod

class IAirSupportCaller(ABC):

    @abstractmethod
    def call_air_support(self):
        pass