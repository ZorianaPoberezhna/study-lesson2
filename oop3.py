class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return Circle.pi * (self.radius ** 2)

circle = Circle(10)
area = circle.area()
