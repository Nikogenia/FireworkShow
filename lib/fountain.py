from .fvector import FVector
from .color import *
from .particle import PointParticle
from .particle_handler import fountain_basic
import random as rd
import pygame as pg
from typing import Callable


class Fountain:

    def __init__(self, pos: FVector, angle: int, duration: int,
                 colors: list[RGBColor], sizes: list[int] = [3, 4, 5, 6],
                 scale: float = 1, strength: float = 1,
                 handler: Callable = fountain_basic) -> None:

        self.pos = pos
        self.angle = angle
        self.duration = duration
        self.colors = colors
        self.sizes = sizes
        self.scale = scale
        self.strength = strength
        self.handler = handler

        self.particles: list[PointParticle] = []
        self.cursor: int = 0

    def update(self) -> bool:

        to_remove = []
        for particle in self.particles:
            if not particle.update():
                to_remove.append(particle)
        for particle in to_remove:
            self.particles.remove(particle)
        
        if self.cursor >= self.duration:
            return bool(self.particles)
        
        for i in range(int(rd.random() * self.strength * 50)):
            self.particles.append(PointParticle(self.pos, FVector(rd.random() * 1.5 - 0.75, rd.randint(2, 3)),
                                                rd.choice(self.sizes), rd.choice(self.colors),
                                                self.handler, True))

        return True

    def render(self, surface: pg.Surface) -> None:

        for particle in self.particles:
            particle.draw(surface)
