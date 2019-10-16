"""
PEP8 styling convention
Class and instance fundamentals
- class has its own copy of vars and instance has its own copy of vars
"""

class Car:
    wheels = 4

    def start(self):
        if Car.wheels==4:
            print("car wheels is 4")
        if self.wheels!=4:
            print("self wheels not 4")
        else:
            print("self wheels is 4")

    def __init__(self, col="blue"):
        self.color = col # this var is available only to the instances created using this constructor
        # and as there is no overloading - we cannot have 2 definitions of init method valid at the same time

    def print_color(self):
        print("self color is "+ self.color)
        # print("Car color is "+ Car.color) # AttributeError: class Car has no attribute 'color'

car = Car()
car.start()
car.print_color()
print("-------------------------------")
car2 = Car("red")
car2.wheels = 6
car2.start()
car2.print_color()
print("-------------------------------")
# Car.start() # TypeError: unbound method
# Car.print_color() # TypeError: unbound method
Car.wheels = 0
Car.color = "white" # ignored? nothing happened? cannot add attribute like this?
car.start() # changes to the class variable wheels is immediately reflected - without re-instantiating the object
car.print_color()
car2.start()
car2.print_color()

"""
car wheels is 4
self wheels is 4
self color is blue
-------------------------------
car wheels is 4
self wheels not 4
self color is red
-------------------------------
self wheels not 4
self color is blue
self wheels not 4
self color is red
"""