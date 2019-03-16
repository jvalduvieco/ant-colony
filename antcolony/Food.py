from dataclasses import dataclass

from antcolony.tools import create_id


@dataclass
class FoodDropped(object):
    id: str
    x: int
    y: int
    food_units: int


class Food:
    def __init__(self, id, x, y, food_units):
        self.id = id
        self.posx, self.posy = x, y
        self.food_units = food_units

    @staticmethod
    def create(x, y, food_units, id=create_id()):
        return Food(id, x, y, food_units), [FoodDropped(id, x, y, food_units)]
