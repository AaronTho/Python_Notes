class MyClass:
    pass


o1 = MyClass()
o2 = MyClass()

o1.x = 10
o2.y = [10, 20, 30]

# This is not a useful way to assign attributes.


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


o1 = MyClass(10, 20)

print(vars(o1))
