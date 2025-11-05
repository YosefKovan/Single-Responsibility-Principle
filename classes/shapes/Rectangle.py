from classes.shapes.Shape import Shape


class Rectangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height