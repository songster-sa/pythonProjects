"""
PEP8 styling convention
Class and instance fundamentals
- class has its own copy of vars and instance has its own copy of vars
- u can pass self as explicit parameter in class methods, if u need to use both in the logic
  python will not evaluate self on its own in this case
- u can access all class and instance, variables and methods in each other like this
- u can call an instance method using cls... but pass self as object - python doesnt stop u
"""


class Car:
    wheels = 4

    def check_wheels(self):
        if Car.wheels == 4:
            print("car wheels is 4")
        else:
            print(f"car wheels is {Car.wheels}")
        if self.wheels != 4:
            print(f"self wheels is {self.wheels}")
        else:
            print("self wheels is 4")

    def __init__(self, col="blue"):
        self.color = col  # this var is available only to the instances created using this constructor
        # and as there is no overloading - we cannot have 2 definitions of init method valid at the same time

    def print_color(self):
        print(f"self color is {self.color}")
        # print("Car color is "+ Car.color) # AttributeError: class Car has no attribute 'color'

    @classmethod
    def make_sound(cls, change_wheels=10):  # i can have the self as parameter here but will have to pass it explicitly every time
        print("car always makes vroom vroom sound")
        cls.wheels = change_wheels;
        # cls.check_wheels() # complains abt missing self parameter
        # cls.print_color() # complains abt missing self parameter
        # print(f"inside call method {self.wheels} {self.color}")


car = Car()
car.check_wheels()
car.print_color()
car.make_sound()
print("-------------------------------")
car2 = Car("red")
car2.wheels = 6
car2.check_wheels()
car2.print_color()
car2.make_sound()
print("-------------------------------")
# Car.start() # TypeError: unbound method
# Car.print_color() # TypeError: unbound method
Car.wheels = 0
Car.color = "white"  # ignored? nothing happened? cannot add attribute like this?
Car.make_sound(3)

car.check_wheels()  # changes to the class variable wheels is immediately reflected - without re-instantiating the object
car.print_color()
car2.check_wheels()
car2.print_color()

"""
car wheels is 4
self wheels is 4
self color is blue
car always makes vroom vroom sound
-------------------------------
car wheels is 10
self wheels is 6
self color is red
car always makes vroom vroom sound
-------------------------------
car always makes vroom vroom sound
car wheels is 3
self wheels is 3
self color is blue
car wheels is 3
self wheels is 6
self color is red
"""
