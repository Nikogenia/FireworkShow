from .vector import Vector
from .fvector import FVector
from . import color, draw, font
import pygame as pg
import time
import threading as th


INFO_NONE = 0
INFO_STATS = 1
INFO_ALL = 2

MODE_PREVIEW = 0
MODE_RENDER_VIDEO = 1
MODE_RENDER_IMAGE = 2


class Display(th.Thread):

    def __init__(self, show):

        th.Thread.__init__(self, name="display thread", daemon=True)

        self.show = show
        self.window = None
        self.screen = None
        self.clock = pg.time.Clock()
        self.running = True
        self.do_render = True
        self.info = INFO_STATS
        self.render_request = 0
        self.fullscreen = False

    @property
    def width(self):
        return self.window.size[0]
    
    @property
    def height(self):
        return self.window.size[1]
    
    @property
    def size(self):
        return self.window.size

    def run(self):

        self.window = pg.Window(f"{self.show.name} {self.show.version} - {self.show.author}",
                                resizable=True)

        self.screen = self.window.get_surface()

        pg.key.set_repeat(400, 50)

        while self.running and th.main_thread().is_alive():

            self.clock.tick(60)

            for event in pg.event.get():
                self.process_event(event)

            if self.do_render:
                self.do_render = False
                self.render()

        self.window.destroy()

    def process_event(self, event):

        if event.type == pg.QUIT:
            self.running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                if time.time() - self.render_request < 10:
                    self.render_request = 0
                    self.do_render = True
                else:
                    self.running = False
            if event.key == pg.K_f:
                if self.fullscreen:
                    self.window.set_windowed()
                else:
                    self.window.set_fullscreen(desktop=True)
                self.fullscreen = not self.fullscreen
            if self.show.mode == MODE_PREVIEW:
                if event.key == pg.K_SPACE:
                    self.show.playing = not self.show.playing
                    self.do_render = True
                if event.key == pg.K_LEFT:
                    self.show.cursor = max(0, self.show.cursor - (self.show.animation.fps if pg.key.get_mods() & pg.KMOD_SHIFT else 1))
                    self.do_render = True
                if event.key == pg.K_RIGHT:
                    self.show.cursor = min(self.show.animation.length, self.show.cursor + (self.show.animation.fps if pg.key.get_mods() & pg.KMOD_SHIFT else 1))
                    self.do_render = True
                if event.key == pg.K_c:
                    self.show.toggle_cache()
                if event.key == pg.K_r:
                    self.render_request = time.time()
                    self.do_render = True
                if event.key == pg.K_v:
                    if time.time() - self.render_request < 10:
                        self.show.mode = MODE_RENDER_VIDEO
                        self.render_request = 0
                        self.do_render = True
            if event.key == pg.K_i:
                if time.time() - self.render_request < 10:
                    self.show.mode = MODE_RENDER_IMAGE
                    self.render_request = 0
                else:
                    self.info = (self.info + 1) % 3
                self.do_render = True

        if event.type == pg.WINDOWSIZECHANGED:
            self.do_render = True

    def render(self):

        self.screen.fill(color.BLACK)

        animation_width, animation_height = self.show.animation.size
        animation_ratio = animation_width / animation_height
        display_ratio = self.width / self.height

        if animation_ratio > display_ratio:
            scale = self.width / animation_width
        else:
            scale = self.height / animation_height
        
        surface = pg.transform.smoothscale_by(self.show.surface, scale)
        self.screen.blit(surface, ((self.width - surface.get_width()) // 2, (self.height - surface.get_height()) // 2))

        if self.info == INFO_ALL:
            draw.rect(self.screen, 3, self.height - 50, self.width - 6, 22, color.BLACK, 90)
            text = f"{1 / self.show.timings_active_backend:.1f} FPS"
            right_text, text_width, text_height = font.render_text(text, font.HP_SIMPLIFIED_18, color.WHITE)
            self.screen.blit(right_text, (self.width - 6 - text_width, self.height - 40 - text_height // 2))
            if self.show.mode == MODE_PREVIEW:
                text = f"TIMINGS    Backend: {self.show.timings_backend * 1000:.2f}ms / {self.show.timings_active_backend * 1000:.2f}ms"
            else:
                text = f"TIMINGS    Total: {self.show.timings_backend:.2f}s    Backend: {self.show.timings_active_backend * 1000:.2f}ms"
                text += f"    Encode: {self.show.timings_convert * 1000:.2f}ms / {self.show.timings_write * 1000:.2f}ms"
            text += f"    Update: {self.show.timings_rocket_update * 1000:.2f}ms / {self.show.timings_fountain_update * 1000:.2f}ms"
            text += f"    Render: {self.show.timings_rocket_render * 1000:.2f}ms / {self.show.timings_fountain_render * 1000:.2f}ms"
            char_width = font.HP_SIMPLIFIED_18.size(text)[0] // len(text)
            max_chars = (self.width - text_width - 80) // char_width
            if len(text) > max_chars:
                text = text[:max_chars] + "..."
            left_text, text_width, text_height = font.render_text(text, font.HP_SIMPLIFIED_18, color.WHITE)
            self.screen.blit(left_text, (6, self.height - 40 - text_height // 2))

        if self.info in (INFO_STATS, INFO_ALL):
            draw.rect(self.screen, 3, self.height - 25, self.width - 6, 22, color.BLACK, 90)
            if self.show.mode == MODE_PREVIEW:
                text = "PLAYING" if self.show.playing else "PAUSED"
            elif self.show.mode == MODE_RENDER_VIDEO:
                text = "RENDERING VIDEO"
            elif self.show.mode == MODE_RENDER_IMAGE:
                text = "RENDERING IMAGES"
            text += f"    Frame {self.show.cursor} / {self.show.animation.length}"
            text += f"    Time: {self.show.cursor / self.show.animation.fps:.2f}s / {self.show.animation.length / self.show.animation.fps:.2f}s"
            right_text, text_width, text_height = font.render_text(text, font.HP_SIMPLIFIED_18, color.WHITE)
            self.screen.blit(right_text, (self.width - 6 - text_width, self.height - 15 - text_height // 2))
            text = f"Particles: {self.show.particle_count}    Rockets: {self.show.rocket_count}    Fountains: {self.show.fountain_count}    "
            text += f"Display: {self.width} x {self.height}  {round(self.clock.get_fps())} FPS    "
            text += f"Animation: {self.show.animation.width} x {self.show.animation.height}  {self.show.animation.fps} FPS    "
            if self.show.mode == MODE_PREVIEW:
                if self.show.cache:
                    text += f"Cache: {self.show.last_cache_id} - {self.show.cache_id}    "
            else:
                text += f"Queue: {self.show.save_queue.qsize()} / {self.show.save_queue.maxsize}    "
            text += f"CPU: {self.show.cpu_usage:.1f}%    Memory: {self.show.memory_usage:.1f} MB"
            char_width = font.HP_SIMPLIFIED_18.size(text)[0] // len(text)
            max_chars = (self.width - text_width - 50) // char_width
            if len(text) > max_chars:
                text = text[:max_chars] + "..."
            left_text, text_width, text_height = font.render_text(text, font.HP_SIMPLIFIED_18, color.WHITE)
            self.screen.blit(left_text, (6, self.height - 15 - text_height // 2))

        if time.time() - self.render_request < 10:
            draw.rect(self.screen, self.width // 2 - 500, self.height // 2 - 250, 1000, 500, color.BLACK, 90)
            text = "RENDER OPTIONS"
            title_text, text_width, text_height = font.render_text(text, font.HP_SIMPLIFIED_30, color.LIGHT_WHITE)
            self.screen.blit(title_text, ((self.width - text_width) // 2, (self.height - text_height) // 2 - 80))
            text = "v - Render Video"
            key1_text, text_width, text_height = font.render_text(text, font.HP_SIMPLIFIED_30, color.LIGHT_WHITE)
            self.screen.blit(key1_text, ((self.width - text_width) // 2, (self.height - text_height) // 2 - 20))
            text = "i - Render Images"
            key2_text, text_width, text_height = font.render_text(text, font.HP_SIMPLIFIED_30, color.LIGHT_WHITE)
            self.screen.blit(key2_text, ((self.width - text_width) // 2, (self.height - text_height) // 2 + 20))
            text = "ESC - Cancel"
            key3_text, text_width, text_height = font.render_text(text, font.HP_SIMPLIFIED_30, color.LIGHT_WHITE)
            self.screen.blit(key3_text, ((self.width - text_width) // 2, (self.height - text_height) // 2 + 60))

        self.window.flip()
