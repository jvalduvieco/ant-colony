from dataclasses import dataclass

from tools import create_id


@dataclass
class NestCreated(object):
    id: str
    x: int
    y: int


class Nest:
    def __init__(self, id, x, y):
        self.id = id
        self.posx, self.posy = x, y

    @staticmethod
    def create(x, y, id=create_id()):
        return Nest(id, x, y), [NestCreated(id, x, y)]
