"""
Inheritance allows you to not repeat code. You can fold one class into another and it inherits the attributes of that class. 
"""


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_aloof(self):
        print("be aloof")


cat1 = Cat()
dog1 = Dog()
cat1.be_aloof()

# This is wrong, fix it.
