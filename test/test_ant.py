import unittest

from Ant import Ant, AntBorn
from Nest import Nest
from tools import create_id


class TestAnt(unittest.TestCase):

    def test_can_create_an_ant(self):
        nest = Nest(create_id(), 100, 100)
        id = create_id()
        ant, events = Ant.create(nest, id)
        self.assertEqual(nest.x, ant.posx)
        self.assertEqual(nest.y, ant.posy)
        self.assertEqual(nest.id, ant.nest_id)
        self.assertEqual(id, ant.id)
        self.assertIn(AntBorn(id, nest.posx, nest.posy, nest.id), events)
