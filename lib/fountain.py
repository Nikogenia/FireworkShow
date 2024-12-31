from .fvector import FVector
from .color import *
from .particle import PointParticle
from .particle_handler import fountain_basic
import random as rd
import pygame as pg
import math
from typing import Callable, Self


class Fountain:

    def __init__(self, pos: FVector, angle: int, duration: int,
                 colors: list[RGBColor], sizes: list[int] = [2, 3, 3, 4, 4, 5],
                 scale: float = 1, strength: float = 1, spread: float = 1,
                 handler: Callable = fountain_basic) -> None:

        self.pos = pos
        self.angle = angle
        self.duration = duration
        self.colors = colors
        self.sizes = sizes
        self.scale = scale
        self.strength = strength
        self.spread = spread
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
        
        vel = FVector(math.cos(math.radians(self.angle)), math.sin(math.radians(self.angle))) * self.scale * 8
        spread = FVector(math.cos(math.radians(self.angle + 90)), math.sin(math.radians(self.angle + 90))) * self.spread * 2
        for i in range(int(rd.random() * self.strength * 40)):
            self.particles.append(PointParticle(self.pos + FVector((rd.random() - 0.5) * 2, (rd.random() - 0.5) * 2),
                                                (vel * (rd.random() + 0.5)) + (spread * rd.gauss(0, 0.5)),
                                                rd.choice(self.sizes), rd.choice(self.colors),
                                                self.handler, True))

        self.cursor += 1

        return True

    def render(self, surface: pg.Surface) -> None:

        for particle in self.particles:
            particle.draw(surface)

    def copy(self, state=False) -> Self:
        fountain = Fountain(self.pos, self.angle, self.duration, self.colors, self.sizes,
                            self.scale, self.strength, self.spread, self.handler)
        if state:
            fountain.particles = [particle.copy() for particle in self.particles]
            fountain.cursor = self.cursor
        return fountain
    
    def __repr__(self) -> str:
        return f"Fountain[pos={self.pos}|angle={self.angle}|duration={self.duration}|cursor={self.cursor}|ID={id(self)}]"
