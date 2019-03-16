from dataclasses import dataclass
from typing import Dict, Tuple, List, Any

from Ant import Ant
from Food import Food
from Nest import Nest
from Pheromone import Pheromone
from tools import create_id


@dataclass
class EnvironmentCreated(object):
    id: str
    x: int
    y: int


class OutOfBorder(Exception):
    pass


class Environment:
    def __init__(self, id, size_x, size_y):
        self.id = id
        self.max_x, self.max_y = size_x, size_y
        self.nests: List[Nest] = []
        self.food: List[Food] = []
        self.pheromones: List[Pheromone] = []
        self.ants: List[Ant] = []
        self.map: Dict[Tuple[int, int], List[Any]] = {}

    @staticmethod
    def create(size_x, size_y, id=create_id()):
        return Environment(id, size_x, size_y), [EnvironmentCreated(id, size_x, size_y)]

    def add_object(self, obj):
        if obj.posx < 0 or obj.posx > self.max_x:
            raise OutOfBorder()
        if obj.posy < 0 or obj.posy > self.max_y:
            raise OutOfBorder()
        contents: List[Any] = self.map.get((obj.posx, obj.posy), [])
        contents.append(obj)
        self.map[obj.posx, obj.posy] = contents

    def add_ant(self, ant: Ant):
        self.ants.append(ant)
        self.add_object(ant)

    def add_nest(self, nest: Nest):
        self.nests.append(nest)
        self.add_object(nest)

    def add_pheromone(self, pheromone):
        self.pheromones.append(pheromone)
        self.add_object(pheromone)

    def add_food(self, food):
        self.food.append(food)
        self.add_object(food)

    def get_cell_contents(self, x, y):
        if x >= self.max_x or x <= 0:
            return None
        if y >= self.max_y or y <= 0:
            return None
        return self.map.get((x, y), [])

    def build_environment(self, x, y):
        return {
            'ne': self.get_cell_contents(x + 1, y - 1),
            'n': self.get_cell_contents(x, y - 1),
            'nw': self.get_cell_contents(x - 1, y - 1),
            'w': self.get_cell_contents(x - 1, y),
            'sw': self.get_cell_contents(x - 1, y + 1),
            's': self.get_cell_contents(x, y + 1),
            'se': self.get_cell_contents(x + 1, y + 1),
            'e': self.get_cell_contents(x + 1, y),
            'c': self.get_cell_contents(x, y)
        }
