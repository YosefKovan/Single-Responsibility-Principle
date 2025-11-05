from classes.soldiers.IShooter import IShooter
from classes.soldiers.INavigator import INavigator


class Infantry(IShooter, INavigator):

    def shoot(self):
        print("Infantry Shooting")

    def navigate(self):
        print("Infantry navigating")