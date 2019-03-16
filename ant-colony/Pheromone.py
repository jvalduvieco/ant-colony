from dataclasses import dataclass

from tools import create_id


@dataclass
class PheromoneDropped(object):
    id: str
    x: int
    y: int
    life: int
    type: str


class Pheromone:
    def __init__(self, id, x, y, type):
        self.id = id
        self.posx, self.posy = x, y
        self.type = type
        self.life = 200

    @staticmethod
    def create(x, y, type, id = create_id()):
        pheromone = Pheromone(id, x, y, type)
        return pheromone, [PheromoneDropped(id, x, y, pheromone.life, type)]
