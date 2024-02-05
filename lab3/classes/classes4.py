class  Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"x - coordinate: {self.x}, y - coordinate: {self.y}")

    def move(self, x2, y2):
        self.x = x2
        self.y = y2

    def dist(self):
        print(self.x - self.y)

Mypoint = Point(3, 2)
Mypoint.show()
Mypoint.move(4, 3)
Mypoint.show()
Mypoint.dist()




    