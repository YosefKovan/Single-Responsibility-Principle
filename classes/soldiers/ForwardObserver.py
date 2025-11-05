from classes.soldiers.IShooter import IShooter
from classes.soldiers.INavigator import INavigator


class ForwardObserver(IShooter, INavigator):

    def shoot(self):
        print("Forward observer shooting")

    def navigate(self):
        print("Forward observer navigating!")