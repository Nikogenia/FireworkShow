from .display import Display
from .frame import Frame
import threading as th
import pygame as pg
import time
import psutil
import signal


class Show:

    def __init__(self, animation,
                 name="Firework Show", version="1.0", author="Nikogenia",
                 cache=False, memory_limit=2000):

        self.name = name
        self.version = version
        self.author = author

        self.display = Display(self)

        self.animation = animation

        self.frames = [None] * (self.animation.length + 1)
        self.surface = pg.Surface(self.animation.size)
        self.cursor = 0
        self.last_cursor = 0
        self.playing = False
        self.clock = pg.time.Clock()

        self.cache = cache
        self.memory_limit = memory_limit
        if self.memory_limit < 200:
            print("Memory limit too low, proceeding with 200 MB")
            self.memory_limit = 200
        self.cache_id = 0
        self.last_cache_id = 0
        self.cache_thread = th.Thread(target=self.clean_cache, name="cache thread", daemon=True)

        self.process = psutil.Process()
        self.cpu_usage = 0
        self.memory_usage = 0

        self.timings_rocket_update = 0
        self.timings_fountain_update = 0
        self.timings_rocket_render = 0
        self.timings_fountain_render = 0
        self.timings_active_backend = 0
        self.timings_backend = 0

    @property
    def frame(self):
        return self.frames[self.cursor]

    def preview(self):

        signal.signal(signal.SIGINT, self.quit)

        self.display.start()
        self.cache_thread.start()

        timings_backend = time.perf_counter()

        while self.display.running:

            self.timings_backend = time.perf_counter() - timings_backend
            self.clock.tick(self.animation.fps)
            timings_backend = time.perf_counter()

            if self.playing:
                self.cursor += 1
                self.display.do_render = True

            if self.cursor > self.animation.length:
                self.cursor = 0

            timings_active_backend = time.perf_counter()

            if self.frame is not None:

                if self.frame.surface is not None:
                    self.surface = self.frame.surface
                    continue
                if self.last_cursor == self.cursor:
                    continue

                rockets = self.frame.rockets
                fountains = self.frame.fountains

            else:

                previous = self.frames[self.cursor - 1]
                if previous is not None and self.cursor > 0:
                    rockets = [rocket.copy(True) for rocket in previous.rockets]
                    fountains = [fountain.copy(True) for fountain in previous.fountains]
                else:
                    rockets = []
                    fountains = []

                if self.cursor in self.animation.rockets:
                    for rocket in self.animation.rockets[self.cursor]:
                        rockets.append(rocket.copy())
                if self.cursor in self.animation.fountains:
                    for fountain in self.animation.fountains[self.cursor]:
                        fountains.append(rocket.copy())

                timings_rocket_update = time.perf_counter()
                to_remove = []
                for rocket in rockets:
                    if not rocket.update():
                        to_remove.append(rocket)
                for rocket in to_remove:
                    rockets.remove(rocket)
                self.timings_rocket_update = time.perf_counter() - timings_rocket_update

                timings_fountain_update = time.perf_counter()
                to_remove = []
                for fountain in fountains:
                    if fountain.update():
                        to_remove.append(fountain)
                for fountain in to_remove:
                    fountains.remove(fountain)
                self.timings_fountain_update = time.perf_counter() - timings_fountain_update

            surface = pg.Surface(self.animation.size)

            timings_rocket_render = time.perf_counter()
            for rocket in rockets:
                rocket.render(surface)
            self.timings_rocket_render = time.perf_counter() - timings_rocket_render

            timings_fountain_render = time.perf_counter()
            for fountain in fountains:
                fountain.render(surface)
            self.timings_fountain_render = time.perf_counter() - timings_fountain_render

            frame = Frame(surface if self.cache else None, rockets, fountains, self.cache_id)
            if self.cache:
                self.cache_id += 1
            self.last_cursor = self.cursor

            self.frames[self.cursor] = frame

            self.surface = surface
            self.display.do_render = True

            self.timings_active_backend = time.perf_counter() - timings_active_backend

    def render(self):

        pass

    def toggle_cache(self):

        self.cache = not self.cache
        self.cache_id = 0
        self.last_cache_id = 0
        self.frames = [None] * (self.animation.length + 1)

    def clean_cache(self):

        next_clean = 0
        next_cpu = 0

        while self.display.running and th.main_thread().is_alive():

            self.memory_usage = self.process.memory_info().rss / 1024 / 1024
            
            if next_cpu < time.time():
                self.cpu_usage = self.process.cpu_percent()
                next_cpu = time.time() + 2

            self.display.do_render = True

            if not self.cache:
                time.sleep(1)
                continue

            if next_clean > time.time():
                time.sleep(0.3)
                continue

            if self.memory_usage < self.memory_limit:
                next_clean = time.time() + 1
                continue

            self.last_cache_id = min(self.last_cache_id + 15, self.cache_id - 5)
            for frame in self.frames:
                if frame is not None and frame.cache_id < self.last_cache_id:
                    frame.surface = None

    def quit(self, signum, frame):

        self.display.running = False
        self.display.join()
        self.cache_thread.join()
