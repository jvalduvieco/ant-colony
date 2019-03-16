import unittest
from multiprocessing import Queue

from antcolony.World import World


class TestWorld(unittest.TestCase):

    def test_can_create_a_world(self):
        world = World(Queue())
        self.assertIsInstance(world, World)
