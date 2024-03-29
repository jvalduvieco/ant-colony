import time
from multiprocessing import Queue
from threading import Thread
from typing import List, Any

from antcolony.Ant import Ant
from antcolony.Environment import Environment
from antcolony.Food import Food
from antcolony.Nest import Nest
from antcolony.tools import create_id


class World(Thread):
    def __init__(self, event_queue: Queue):
        Thread.__init__(self)
        self.event_queue = event_queue
        self.environment: Environment = None
        self.initialized = False

    def publish_events(self, events):
        for event in events:
            print("Publishing ", event.__class__.__name__)
            self.event_queue.put(event)

    def run(self):
        events = self.init()
        self.publish_events(events)
        while True:
            self.move_ants()
            time.sleep(0.1)

    def init(self) -> List[Any]:
        self.environment, environment_events = Environment.create(200, 200, create_id())
        nest, nest_events = Nest.create(50, 50, create_id())
        self.environment.add_nest(nest)
        ant, ant_events = Ant.create(nest, create_id())
        self.environment.add_ant(ant)
        food, food_events = Food.create(150, 150, create_id())
        self.environment.add_food(food)
        return environment_events + nest_events + ant_events + food_events

    def move_ants(self):
        for ant in self.environment.ants:
            events = ant.next(self.environment.build_environment(ant.posx, ant.posy),
                              {'move': lambda x, y: self.environment.move(ant, x, y),
                               'drop_pheromone': lambda pheromone: self.environment.add_pheromone(pheromone)
                               })
            self.publish_events(events)
