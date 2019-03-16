import unittest

from antcolony.Ant import Ant, AntBorn
from antcolony.Nest import Nest
from antcolony.tools import create_id


class TestAnt(unittest.TestCase):

    def test_can_create_an_ant(self):
        nest = Nest(create_id(), 100, 100)
        id = create_id()
        ant, events = Ant.create(nest, id)
        self.assertEqual(nest.posx, ant.posx)
        self.assertEqual(nest.posy, ant.posy)
        self.assertEqual(nest.id, ant.nest_id)
        self.assertEqual(id, ant.id)
        self.assertIn(AntBorn(id, nest.posx, nest.posy, nest.id), events)
