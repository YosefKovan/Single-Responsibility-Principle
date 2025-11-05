from math import pi


class Circle:

    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r **2