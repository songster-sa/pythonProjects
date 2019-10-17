"""
exploring multiple inheritance
fundamental 5

ImportError: attempted relative import with no known parent package
:(
"""

from .fun_four import Cat
from .fun_three import Car


class Autobot(Car, Cat):
    def do_nothing(self):
        print("do nothing")


hy1 = Autobot()
hy1.say_hello()
hy1.check_wheels()
hy1.make_sound()
