from project.animals.animal import Mammal
from project.food import *


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]

    @property
    def gained_weight(self):
        return 0.1

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.4

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def food_that_eats(self):
        return [Vegetable, Meat]

    @property
    def gained_weight(self):
        return 0.3

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1

    def make_sound(self):
        return "ROAR!!!"


