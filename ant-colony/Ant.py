import random
from dataclasses import dataclass

from Nest import Nest
from tools import create_id


@dataclass
class AntBorn(object):
    id: str
    x: int
    y: int
    nest_id: str


@dataclass
class AntMoved(object):
    id: str
    x_delta: int
    y_delta: int
    x: int
    y: int
    fromx: int
    fromy: int


class InvalidDirection(Exception):
    pass


class Ant:
    def __init__(self, id, x, y, nest_id):
        self.id = id
        self.posx, self.posy = x, y
        self.nest_id = nest_id

    @staticmethod
    def create(nest: Nest, id=create_id()):
        return Ant(id, nest.posx, nest.posy, nest.id), [AntBorn(id, nest.posx, nest.posy, nest.id)]

    def direction_to_delta(self, direction):
        deltas = {
            'n': (0, -1),
            'nw': (-1, -1),
            'w': (-1, 0),
            'sw': (-1, 1),
            's': (0, 1),
            'se': (1, 1),
            'e': (1, 0),
            'ne': (1, -1),
            'c': (0, 0)
        }
        if direction not in deltas:
            raise InvalidDirection(direction)
        return deltas[direction]

    def next(self, environment, actions):
        possible_movements = list(filter(
            lambda x: not environment[x] is None,
            ['n', 'nw', 'w', 'sw', 's', 'se', 'e', 'ne', 'c']))
        movement = random.choice(possible_movements)
        x_delta, y_delta = self.direction_to_delta(movement)
        fromx = self.posx
        fromy = self.posy
        self.posx, self.posy = actions['move'](self.posx + x_delta, self.posy + y_delta)
        return [AntMoved(self.id, x_delta, y_delta, self.posx, self.posy, fromx, fromy)]
