from .vector import Vector
from .fvector import FVector
from . import color, draw, font
import pygame as pg
import threading as th


INFO_NONE = 0
INFO_STATS = 1
INFO_ALL = 2


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
                self.running = False
            if event.key == pg.K_SPACE:
                self.show.playing = not self.show.playing
                self.do_render = True
            if event.key == pg.K_LEFT:
                self.show.cursor = max(0, self.show.cursor - (30 if pg.key.get_mods() & pg.KMOD_SHIFT else 1))
                self.do_render = True
            if event.key == pg.K_RIGHT:
                self.show.cursor = min(self.show.animation.length, self.show.cursor + (30 if pg.key.get_mods() & pg.KMOD_SHIFT else 1))
                self.do_render = True
            if event.key == pg.K_c:
                self.show.toggle_cache()
            if event.key == pg.K_i:
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
            draw.rect(self.screen, 3, self.height - 50, self.width - 6, 22, color.BLACK, 100)
            text = f"TIMINGS    Backend: {self.show.timings_backend * 1000:.2f}ms / {self.show.timings_active_backend * 1000:.2f}ms"
            text += f"    Update: {self.show.timings_rocket_update * 1000:.2f}ms / {self.show.timings_fountain_update * 1000:.2f}ms"
            text += f"    Render: {self.show.timings_rocket_render * 1000:.2f}ms / {self.show.timings_fountain_render * 1000:.2f}ms"
            left_text, text_width, text_height = font.render_text(text, font.HP_SIMPLIFIED_18, color.WHITE)
            self.screen.blit(left_text, (6, self.height - 40 - text_height // 2))
            text = f"{1 / self.show.timings_active_backend:.1f} FPS"
            right_text, text_width, text_height = font.render_text(text, font.HP_SIMPLIFIED_18, color.WHITE)
            self.screen.blit(right_text, (self.width - 6 - text_width, self.height - 40 - text_height // 2))

        if self.info in (INFO_STATS, INFO_ALL):
            draw.rect(self.screen, 3, self.height - 25, self.width - 6, 22, color.BLACK, 100)
            particle_count = len(self.show.frame.particles) if self.show.frame else 0
            rocket_count = len(self.show.frame.rockets) if self.show.frame else 0
            text = f"Particles: {particle_count}    Rockets: {rocket_count}    "
            if self.width > 800:
                text += f"Display: {self.width} x {self.height}  {round(self.clock.get_fps())} FPS    "
            if self.width > 1050:
                text += f"Animation: {self.show.animation.width} x {self.show.animation.height}  {self.show.animation.fps} FPS    "
            if self.width > 1400:
                text += f"Cache: {self.show.last_cache_id} - {self.show.cache_id}    "
                text += f"CPU: {self.show.cpu_usage:.1f}%    Memory: {self.show.memory_usage:.1f} MB"
            left_text, text_width, text_height = font.render_text(text, font.HP_SIMPLIFIED_18, color.WHITE)
            self.screen.blit(left_text, (6, self.height - 15 - text_height // 2))
            text = "PLAYING" if self.show.playing else "PAUSED"
            text += f"    Frame {self.show.cursor} / {self.show.animation.length}"
            text += f"    Time: {self.show.cursor / self.show.animation.fps:.2f}s / {self.show.animation.length / self.show.animation.fps:.2f}s"
            right_text, text_width, text_height = font.render_text(text, font.HP_SIMPLIFIED_18, color.WHITE)
            self.screen.blit(right_text, (self.width - 6 - text_width, self.height - 15 - text_height // 2))

        self.window.flip()
