class Point:
    def __init__(self, x, y):  # Use the init method to construct an object
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point)
point.x = 11
print(point.x)
