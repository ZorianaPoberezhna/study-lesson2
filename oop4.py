class Circle:
    pi = 3.14
    def __init__(self, radius):
        if not Circle.check_radius(radius):
            raise ValueError("Error: radius cannot be less than 0!")
        self.radius = radius


    def area(self):
        return Circle.pi * (self.radius ** 2)


    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)


    @staticmethod
    def check_radius(radius):
        return radius > 0

circle = Circle.from_diameter(10)
area = circle.area()
valid = Circle.check_radius(17)
