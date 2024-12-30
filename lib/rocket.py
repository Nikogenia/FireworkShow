from .fvector import FVector
from .color import *
from .particle import PointParticle
from .explosion import BasicExplosion, ImageExplosion
from .particle_handler import rocket_launch
import random as rd
import pygame as pg
from typing import Callable, Self


ROCKET_LAUNCH_COLORS = [WHITE, LIGHT_YELLOW, YELLOW, DARK_YELLOW, ORANGE]


class Rocket:

    def __init__(self, explosion: BasicExplosion | ImageExplosion,
                 pos: FVector, start: FVector, duration: int,
                 curve: float = 2, launch_sizes: list[int] = [2, 3],
                 launch_colors: list[RGBColor] = ROCKET_LAUNCH_COLORS,
                 launch_handler: Callable = rocket_launch) -> None:

        self.explosion = explosion
        self.pos = pos
        self.start = start
        self.duration = duration
        self.curve = curve
        self.launch_sizes = launch_sizes
        self.launch_colors = launch_colors
        self.launch_handler = launch_handler

        self.particles: list[PointParticle] = []
        self.cursor: int = 0
        self.exploded: bool = False

    def update(self) -> bool:

        to_remove = []
        for particle in self.particles:
            if not particle.update():
                to_remove.append(particle)
        for particle in to_remove:
            self.particles.remove(particle)
        
        if self.cursor >= self.duration:

            if not self.exploded:
                self.exploded = True
                self.particles.extend(self.explosion.generate_particles(self.pos))
        
            return bool(self.particles)
        
        factor = (1 - self.cursor / self.duration) ** self.curve
        offset = (self.start - self.pos) * factor
        pos = self.pos + offset

        for i in range(int(rd.random() * factor * 30)):
            self.particles.append(PointParticle(pos, FVector(rd.random() * 1.5 - 0.75, rd.randint(2, 3)),
                                                rd.choice(self.launch_sizes), rd.choice(self.launch_colors),
                                                self.launch_handler))

        self.cursor += 1

        return True

    def render(self, surface: pg.Surface) -> None:

        for particle in self.particles:
            particle.draw(surface)

    def copy(self, state=False) -> Self:
        rocket = Rocket(self.explosion, self.pos, self.start, self.duration,
                        self.curve, self.launch_sizes, self.launch_colors, self.launch_handler)
        if state:
            rocket.cursor = self.cursor
            rocket.exploded = self.exploded
            rocket.particles = [particle.copy() for particle in self.particles]
        return rocket
    
    def __repr__(self) -> str:
        return f"Rocket[pos={self.pos}|start={self.start}|duration={self.duration}|cursor={self.cursor}|ID={id(self)}]"
