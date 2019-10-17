"""
exploring inheritance and related concepts
- only 1 constructor can be present - of course overloading is not allowed
- over ridding is allowed and works as expected
- sub class does not need a constructor at all
- super does not need to be the first call in the child constructor

QQ not able to import fun_three to resuse Car class :( - says no module named fun_three
"""


class Animal:
    name = "animal"
    limbs = 4

    def __init__(self, name, sound, food):
        print("inside super init")
        self.name = name
        self.sound = sound
        self.food = food

    def say_hello(self):
        print(f"inside super method {self.name} says hello")

    def make_noise(self):
        print(f"inside super method {self.name} says {self.sound}")

    def eat(self):
        print(f"inside super method {self.name} likes {self.food}")


class Cat(Animal):  # u cannot have an empty class :(
    def __init__1(self):
        print("do nothing")

    def __init__2(self, name, sound, food):
        # remove the 2 and it works sequential.. super does not need to be the first call
        print("inside CAT constructor before")
        super().__init__(name, sound, food)
        print("inside CAT constructor after")

    def make_noise(self):
        print(f"inside CAT method {self.name} says cat cat {self.sound}")


def with_init1():
    cat1 = Cat()  # only 1 constructor can be present...
    # cat1.make_noise()
    # cat1.eat()
    cat1.say_hello()


# cat2 = Cat("cat","meiow","milk") # TypeError: __init__() takes 1 positional argument but 4 were given
cat2 = Animal("cat", "meiow", "milk")
cat2.say_hello()
cat2.make_noise()
cat2.eat()

# cat3 = Animal() # TypeError: __init__() missing 3 required positional arguments: 'name', 'sound', and 'food'
print("-------------------------------")
cat4 = Cat("cat4", "mmmmeeoooww", "fish")  # created without cat constructor
cat4.say_hello()
cat4.make_noise()
cat4.eat()

"""
without any cat constructor:
inside super init
inside super method cat says hello
inside super method cat says meiow
inside super method cat likes milk
-------------------------------
inside super init
inside super method cat4 says hello
inside CAT method cat4 says cat cat mmmmeeoooww
inside super method cat4 likes fish
"""

"""
with Cat init2 constructor
inside super init
inside super method cat says hello
inside super method cat says meiow
inside super method cat likes milk
-------------------------------
inside CAT constructor before
inside super init
inside CAT constructor after
inside super method cat4 says hello
inside CAT method cat4 says cat cat mmmmeeoooww
inside super method cat4 likes fish
"""
