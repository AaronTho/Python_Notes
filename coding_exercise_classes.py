# Starter code
class Garage:
    def __init__(self, size, cars):
        self.size = size
        self.cars = cars

    def open_door(self):
        return "The door opens"


home = Garage(2, ["Ram", "Model 3"])
home.cars = []

get_cars = home.cars

print(vars(home))
