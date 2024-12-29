from .display import Display
from .frame import Frame
from . import color
import threading as th
import pygame as pg
import time
import psutil


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
        self.cache_thread = th.Thread(target=self.clean_cache, name="cache thread")

        self.process = psutil.Process()
        self.cpu_usage = 0
        self.memory_usage = 0

    @property
    def frame(self):
        return self.frames[self.cursor]

    def preview(self):

        self.display.start()
        self.cache_thread.start()

        while self.display.running:

            self.clock.tick(self.animation.fps)

            if self.playing:
                self.cursor += 1
                self.display.do_render = True

            if self.cursor > self.animation.length:
                self.cursor = 0

            if self.frame is not None:
                if self.frame.surface is not None:
                    self.surface = self.frame.surface
                    continue
                if self.last_cursor == self.cursor:
                    continue
                rockets = self.frame.rockets
            else:
                previous = self.frames[self.cursor - 1]
                rockets = previous.rockets if previous is not None and self.cursor > 0 else []            

            surface = pg.Surface(self.animation.size)

            #RENDER
        
            frame = Frame(surface if self.cache else None, rockets, self.cache_id)
            if self.cache:
                self.cache_id += 1
            self.last_cursor = self.cursor

            self.frames[self.cursor] = frame

            self.surface = surface
            self.display.do_render = True

    def render(self):

        pass

    def toggle_cache(self):

        if self.cache:
            self.cache = False
            self.cache_id = 0
            self.last_cache_id = 0
            self.frames = [None] * (self.animation.length + 1)
            print("Cache reset and disabled")
            return
        
        self.cache = True
        print("Cache reset and enabled")

    def clean_cache(self):

        next_clean = 0
        next_cpu = 0

        while self.display.running:

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
