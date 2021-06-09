"""
Define a new type called Person
    -this type should have a name attribute
    -and a talk method
"""


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person('John Smith')
bob = Person('Bob Smith')
bob.talk()
john.talk()
