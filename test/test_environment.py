import unittest

from antcolony.Ant import Ant
from antcolony.Environment import Environment, EnvironmentCreated, OutOfBorder
from antcolony.Nest import Nest
from antcolony.tools import create_id


class TestEnvironment(unittest.TestCase):
    def setUp(self):
        self.x = 1231
        self.y = 5432
        self.env_id = create_id()
        self.environment, self.events = Environment.create(size_x=self.x, size_y=self.y, id=self.env_id)

    def test_can_create_an_environment(self):
        self.assertEqual(self.x, self.environment.max_x)
        self.assertEqual(self.y, self.environment.max_y)
        self.assertIn(EnvironmentCreated(self.env_id, self.x, self.y), self.events)

    def test_can_add_objects(self):
        nest = Nest(create_id(), 100, 100)
        self.environment.add_nest(nest)
        self.assertIn(nest, self.environment.nests)

    def test_adding_objects_out_of_bounds_raise_exceptions(self):
        nest = Nest(create_id(), 10000, 100)
        with self.assertRaises(OutOfBorder):
            self.environment.add_nest(nest)
        nest = Nest(create_id(), 100, 10000)
        with self.assertRaises(OutOfBorder):
            self.environment.add_nest(nest)

    def test_build_environment_takes_into_account_left_up_borders(self):
        environment = self.environment.build_environment(1, 1)
        self.assertEqual(
            {'ne': None, 'n': None, 'nw': None, 'w': None, 'sw': None, 's': [], 'se': [], 'e': [], 'c': []},
            environment)

    def test_build_environment_takes_into_account_right_bottom_borders(self):
        environment = self.environment.build_environment(1230, 5431)
        self.assertEqual(
            {'ne': None, 'n': [], 'nw': [], 'w': [], 'sw': None, 's': None, 'se': None, 'e': None, 'c': []},
            environment)

    def test_moving_an_object_updates_map(self):
        nest, _ = Nest.create(50, 50, create_id())
        self.environment.add_nest(nest)
        ant, _ = Ant.create(nest, create_id())
        self.environment.add_ant(ant)
        self.assertIn(ant, self.environment.map[50, 50])
        self.environment.move(ant, 51, 51)
        self.assertIn(ant, self.environment.map[51, 51])
