class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')


# An object is an instance of a Class.

point1 = Point()
point1.x = 10
point1.y = 20
point1.draw()
point1.move()
