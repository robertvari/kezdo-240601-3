class Vehicle:
    def __init__(self, speed, weight, name):
        self.speed = speed
        self.weight = weight
        self.name = name

    def print(self):
        print(f"Name: {self.name}")
        print(f"Speed: {self.speed}")
        print(f"Weight: {self.weight}")

class Car(Vehicle):
    # override parent class __init__
    def __init__(self, speed, weight, name, wheels):
        # call parent class's __init__ to fill out the base attributes
        super().__init__(speed, weight, name)
        self.wheels = wheels

    # overrider parent class print()
    def print(self):
        print(f"Wheels: {self.wheels}")
        super().print()
        
class Boat(Vehicle):
    pass


my_car = Car(180, 600, "BMW", 4)
my_boat = Boat(40, 1200, "Sea King")

my_car.print()
my_boat.print()