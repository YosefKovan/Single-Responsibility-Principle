from abc import ABC, abstractmethod


class INavigator(ABC):

    @abstractmethod
    def navigate(self):
        pass