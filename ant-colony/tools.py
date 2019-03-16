from random import randrange
from uuid import uuid4


def get_random_coords(max_x, max_y):
    return randrange(50, max_x), randrange(50, max_y)


def create_id():
    return uuid4().hex
