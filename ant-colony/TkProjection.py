from multiprocessing import Queue
from tkinter import Tk, Canvas

from Ant import AntBorn, AntMoved
from Environment import EnvironmentCreated
from Food import FoodDropped
from Nest import NestCreated


class TKProjection:
    def __init__(self, event_queue: Queue):
        self.root = Tk()
        self.root.title("Ant Colony Simulator")
        self.root.bind("<Escape>", lambda quit: self.root.destroy())
        self.canvas = None
        self.objects = dict()
        self.event_queue = event_queue
        self.event_handlers = {
            'EnvironmentCreated': self.handle_environment_created,
            'NestCreated': self.handle_nest_created,
            'AntBorn': self.handle_ant_born,
            'AntMoved': self.handle_ant_moved,
            'FoodDropped': self.handle_food_dropped
        }

    def run(self):
        while True:
            event = self.event_queue.get()
            if event.__class__.__name__ == "EnvironmentCreated":
                self.update([event])
                break
            else:
                print("Environment not created, ignoring event: ", event.__class__.__name__)
                pass
        self.root.mainloop()

    def update(self, events):
        for event in events:
            event_type = event.__class__.__name__
            print("==> ", event)
            handler = self.event_handlers.get(event_type, lambda: "Unknown event %s" % event_type)
            handler(event)
            self.canvas.update()

    def handle_environment_created(self, event: EnvironmentCreated):
        self.canvas = Canvas(self.root, width=event.x, height=event.y, background="#010326", selectborderwidth=0,
                             highlightthickness=0, borderwidth=0)
        self.canvas.pack()
        self.root.after(0, self.next)

    def handle_nest_created(self, event: NestCreated):
        self.objects[event.id] = self.circle(event.x, event.y, 10, '#F27E1D')

    def handle_ant_born(self, event: AntBorn):
        self.objects[event.id] = self.circle(event.x, event.y, 2, "#AF0220")

    def handle_food_dropped(self, event: FoodDropped):
        self.objects[event.id] = self.circle(event.x, event.y, 7, "#04C3D9")

    def handle_ant_moved(self, event: AntMoved):
        self.canvas.move(self.objects[event.id], event.x_delta, event.y_delta)

    def circle(self, x, y, radius, color):
        return self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline='')

    def next(self):
        while not self.event_queue.empty():
            event = self.event_queue.get(block=False)
            self.update([event])
        process_events_every_ms = 20
        self.root.after(process_events_every_ms, self.next)
