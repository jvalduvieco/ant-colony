import unittest

from antcolony.Food import Food, FoodDropped
from antcolony.tools import create_id


class TestFood(unittest.TestCase):

    def test_can_create_a_Food(self):
        x = 123
        y = 345
        food_units = 100
        id = create_id()
        food, events = Food.create(x, y, food_units, id)
        self.assertEqual(x, food.posx)
        self.assertEqual(y, food.posy)
        self.assertEqual(id, food.id)
        self.assertIn(FoodDropped(id, x, y, food_units), events)
