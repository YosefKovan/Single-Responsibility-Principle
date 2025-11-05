from classes.soldiers.IShooter import IShooter
from classes.soldiers.IAirsupportCaller import IAirSupportCaller


class Pilot(IShooter, IAirSupportCaller):

    def shoot(self):
        print("Forward observer shooting")

    def call_air_support(self):
        print("Forward observer navigating!")
