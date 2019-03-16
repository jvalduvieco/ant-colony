import unittest

from Pheromone import Pheromone, PheromoneDropped
from tools import create_id


class TestPheromone(unittest.TestCase):

    def test_can_create_a_Pheromone(self):
        x = 123
        y = 345
        type = 'long'
        id = create_id()
        pheromone, events = Pheromone.create(x, y, type, id)
        self.assertEqual(x, pheromone.posx)
        self.assertEqual(y, pheromone.posy)
        self.assertEqual(id, pheromone.id)
        self.assertIn(PheromoneDropped(id, x, y, 200, type), events)
