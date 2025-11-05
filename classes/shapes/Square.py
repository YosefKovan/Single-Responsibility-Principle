from classes.shapes.Shape import Shape


class Square(Shape):

    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a**2

