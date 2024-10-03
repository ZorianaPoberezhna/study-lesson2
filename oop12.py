from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3,14 * self.radius ** 2

rectangle = Rectangle(5,10)
cir_cle = Circle(7)

print(isinstance(rectangle, Rectangle))
print(isinstance(cir_cle, Circle))

rectangle.area()
cir_cle.area()


