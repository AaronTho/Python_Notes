class Garage:
    def __init__(self, size):
        self._size = size
        self.cars = []

        @property
        def size(self):
            return self._size

    def open_door(self):
        return "The door opens"
