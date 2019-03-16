import unittest

from antcolony.Nest import Nest, NestCreated
from antcolony.tools import create_id


class TestNest(unittest.TestCase):

    def test_can_create_a_nest(self):
        x = 123
        y = 345
        id = create_id()
        nest, events = Nest.create(x, y, id)
        self.assertEqual(x, nest.posx)
        self.assertEqual(y, nest.posy)
        self.assertEqual(id, nest.id)
        self.assertIn(NestCreated(id, x, y), events)
