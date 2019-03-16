import unittest
from multiprocessing import Queue

from Ant import AntBorn
from Environment import EnvironmentCreated
from Nest import NestCreated
from TkProjection import TKProjection
from tools import create_id


class TestApp(unittest.TestCase):

    def test_can_run_the_app(self):
        projection = TKProjection(Queue())
        projection.update([EnvironmentCreated(create_id(), 100, 100)])
        nest_id = create_id()
        projection.update([NestCreated(nest_id, 50, 50)])
        projection.update([AntBorn(create_id(), 10, 10, nest_id)])

