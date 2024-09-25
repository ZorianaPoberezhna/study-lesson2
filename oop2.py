class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length


    def square(self):
        return self.width * self.length


    def perimeter(self):
        return 2 * (self.length + self.width)


rect = Rectangle(2, 4)
square = rect.square()
perimeter = rect.perimeter()
