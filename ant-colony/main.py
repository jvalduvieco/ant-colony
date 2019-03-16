from multiprocessing import Queue

from TkProjection import TKProjection
from World import World

if __name__ == "__main__":
    try:
        event_queue = Queue()
        projection = TKProjection(event_queue)
        world = World(event_queue)
        world.start()
        projection.run()
    except KeyboardInterrupt:
        print("Exitting...")
        exit(0)
