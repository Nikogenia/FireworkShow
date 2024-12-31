from .display import Display, MODE_PREVIEW, MODE_RENDER_VIDEO, MODE_RENDER_IMAGE
from .frame import Frame
from .image import pg_to_cv
import threading as th
import pygame as pg
import cv2
import time
import os
import shutil
import traceback
import psutil
import signal
import queue
from moviepy import VideoFileClip, AudioFileClip   


class Show:

    def __init__(self, animation,
                 name="Firework Show", version="1.0", author="Nikogenia",
                 cache=False, memory_limit=2000, music_path=None, music_offset=0):

        self.name = name
        self.version = version
        self.author = author

        self.display = Display(self)

        self.animation = animation
        self.music_path = music_path
        self.music_offset = music_offset

        self.mode = MODE_PREVIEW
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
        self.music_thread = None

        self.process = psutil.Process()
        self.cpu_usage = 0
        self.memory_usage = 0

        self.timings_rocket_update = 0
        self.timings_fountain_update = 0
        self.timings_rocket_render = 0
        self.timings_fountain_render = 0
        self.timings_active_backend = 0
        self.timings_backend = 0
        self.timings_write = 0
        self.timings_convert = 0

        self.rocket_count = 0
        self.fountain_count = 0
        self.particle_count = 0

        self.save_queue = queue.Queue(30)

        signal.signal(signal.SIGINT, self.quit)

    @property
    def frame(self):
        return self.frames[self.cursor]

    def preview(self):

        self.display.start()
        self.cache_thread.start()

        timings_backend = time.perf_counter()

        while self.display.running:

            self.timings_backend = time.perf_counter() - timings_backend
            self.clock.tick(self.animation.fps)
            timings_backend = time.perf_counter()

            if self.mode == MODE_RENDER_VIDEO:
                self.render()
                continue
            if self.mode == MODE_RENDER_IMAGE:
                self.render(image=True)
                continue

            if self.playing:
                self.cursor += 1
                self.display.do_render = True

            if self.cursor > self.animation.length:
                self.cursor = 0            

            timings_active_backend = time.perf_counter()

            if self.frame is not None:

                if self.last_cursor == self.cursor:
                    continue

                if self.frame.surface is not None:

                    self.surface = self.frame.surface

                    self.last_cursor = self.cursor

                    self.timings_active_backend = self.frame.timings_active_backend
                    self.timings_rocket_update = self.frame.timings_rocket_update
                    self.timings_fountain_update = self.frame.timings_fountain_update
                    self.timings_rocket_render = self.frame.timings_rocket_render
                    self.timings_fountain_render = self.frame.timings_fountain_render

                    self.rocket_count = len(self.frame.rockets)
                    self.fountain_count = len(self.frame.fountains)
                    self.particle_count = len(self.frame.particles)

                    continue

                rockets = self.frame.rockets
                fountains = self.frame.fountains

                self.timings_rocket_update = self.frame.timings_rocket_update
                self.timings_fountain_update = self.frame.timings_fountain_update

            else:

                previous = self.frames[self.cursor - 1]
                if previous is not None and self.cursor > 0:
                    rockets = [rocket.copy(True) for rocket in previous.rockets]
                    fountains = [fountain.copy(True) for fountain in previous.fountains]
                else:
                    rockets = []
                    fountains = []

                self.backend_update(rockets, fountains)
            
            surface = self.backend_render(rockets, fountains)

            self.timings_active_backend = time.perf_counter() - timings_active_backend

            frame = Frame(surface if self.cache else None, rockets, fountains, self.cache_id,
                          self.timings_active_backend, self.timings_rocket_update, self.timings_fountain_update,
                          self.timings_rocket_render, self.timings_fountain_render)
            if self.cache:
                self.cache_id += 1
            self.last_cursor = self.cursor

            self.frames[self.cursor] = frame

            self.rocket_count = len(rockets)
            self.fountain_count = len(fountains)
            self.particle_count = len(frame.particles)

            self.surface = surface
            self.display.do_render = True

    def render(self, image=False):

        timings_backend = time.perf_counter()

        if image:
            self.mode = MODE_RENDER_IMAGE
            print(f"Start rendering {self.animation.length + 1} images to ./out/{self.name}")
            os.makedirs(f"./out/{self.name}", exist_ok=True)
            video = None
        else:
            self.mode = MODE_RENDER_VIDEO
            print(f"Start rendering {self.animation.length + 1} frames to ./out/{self.name}.mp4")
            os.makedirs("./out", exist_ok=True)
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            video = cv2.VideoWriter(f"./out/{self.name}.mp4", fourcc, self.animation.fps, self.animation.size)

        self.save_queue = queue.Queue(150)
        save_thread = th.Thread(target=self.save, name="save thread", daemon=True)
        save_thread.start()

        self.cache_id = 0
        self.last_cache_id = 0
        self.frames = [None] * (self.animation.length + 1)

        self.cursor = 0

        rockets = []
        fountains = []

        while self.cursor <= self.animation.length and self.display.running:

            timings_active_backend = time.perf_counter()

            self.backend_update(rockets, fountains)
            
            surface = self.backend_render(rockets, fountains)

            try:
                self.save_queue.put((image, video, self.cursor, self.surface), timeout=5)
            except queue.Full:
                print("Saving queue full for 5 seconds, stopping rendering")
                break

            self.rocket_count = len(rockets)
            self.fountain_count = len(fountains)
            particle_count = 0
            for rocket in rockets:
                particle_count += len(rocket.particles)
            for fountain in fountains:
                particle_count += len(fountain.particles)
            self.particle_count = particle_count

            self.timings_active_backend = time.perf_counter() - timings_active_backend

            self.surface = surface
            self.display.do_render = True

            self.cursor += 1

            self.timings_backend = time.perf_counter() - timings_backend

        self.save_queue.join()

        self.mode = MODE_PREVIEW

        if save_thread.is_alive():
            save_thread.join()

        if not image:
            video.release()

        print(f"Rendering finished in {self.timings_backend:.2f}s")        

        self.music_thread = th.Thread(target=self.music, name="music thread", daemon=True)
        self.music_thread.start()

    def backend_update(self, rockets, fountains):

        if self.cursor in self.animation.rockets:
            for rocket in self.animation.rockets[self.cursor]:
                rockets.append(rocket.copy())
        if self.cursor in self.animation.fountains:
            for fountain in self.animation.fountains[self.cursor]:
                fountains.append(fountain.copy())

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
            if not fountain.update():
                to_remove.append(fountain)
        for fountain in to_remove:
            fountains.remove(fountain)
        self.timings_fountain_update = time.perf_counter() - timings_fountain_update

    def backend_render(self, rockets, fountains):

        surface = pg.Surface(self.animation.size)

        timings_rocket_render = time.perf_counter()
        for rocket in rockets:
            rocket.render(surface)
        self.timings_rocket_render = time.perf_counter() - timings_rocket_render

        timings_fountain_render = time.perf_counter()
        for fountain in fountains:
            fountain.render(surface)
        self.timings_fountain_render = time.perf_counter() - timings_fountain_render

        return surface

    def save(self):
            
        while self.mode != MODE_PREVIEW:

            try:
                image, video, cursor, surface = self.save_queue.get(timeout=1)
            except queue.Empty:
                continue

            if image:

                timings_write = time.perf_counter()
                frame = str(cursor).zfill(len(str(self.animation.length)))
                pg.image.save(surface, f"./out/{self.name}/frame{frame}.png")
                self.timings_write = time.perf_counter() - timings_write

            else:

                timings_convert = time.perf_counter()
                cv_array = pg_to_cv(surface)
                self.timings_convert = time.perf_counter() - timings_convert

                timings_write = time.perf_counter()
                video.write(cv_array)
                self.timings_write = time.perf_counter() - timings_write

            self.save_queue.task_done()

    def music(self):

        if not self.music_path:
            return

        print(f"Adding music from {self.music_path} to the show")

        shutil.copyfile(f"./out/{self.name}.mp4", f"./out/{self.name} - no music.mp4")

        video = VideoFileClip(f"./out/{self.name} - no music.mp4")
        audio = AudioFileClip(self.music_path)

        audio = audio.subclipped(self.animation.offset + self.music_offset, video.duration)

        video = video.with_audio(audio)

        video.write_videofile(f"./out/{self.name}.mp4", codec="libx264", audio_codec="aac")

        print("Music added")

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
        if self.display.is_alive():
            self.display.join()
        if self.cache_thread.is_alive():
            self.cache_thread.join()
