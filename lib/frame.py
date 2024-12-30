from dataclasses import dataclass
from .rocket import Rocket
from .fountain import Fountain
import pygame as pg


@dataclass
class Frame:

    surface: pg.Surface
    rockets: list[Rocket]
    fountains: list[Fountain]

    cache_id: int

    @property
    def particles(self):
        particles = []
        for rocket in self.rockets:
            particles.extend(rocket.particles)
        for fountain in self.fountains:
            particles.extend(fountain.particles)
        return particles
