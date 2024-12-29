from dataclasses import dataclass
import pygame as pg


@dataclass
class Frame:

    surface: pg.Surface
    rockets: list
    cache_id: int

    @property
    def particles(self):
        particles = []
        for rocket in self.rockets:
            particles.extend(rocket.particles)
        return particles
