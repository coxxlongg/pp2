class Shape:
    def __init__(self):
        self.area = 0
        
    def printArea(self):
        print(self.area)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        self.area = self.width * self.length

Myshape = Rectangle(5,6)
Myshape.area()