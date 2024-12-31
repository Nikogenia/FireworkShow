from .fvector import FVector
from .color import *
from .particle import PointParticle
from .explosion import BasicExplosion, ImageExplosion, LineExplosion
from .particle_handler import rocket_launch
import random as rd
import pygame as pg
from typing import Callable, Self


ROCKET_LAUNCH_COLORS = [WHITE, LIGHT_YELLOW, YELLOW, DARK_YELLOW, ORANGE]


class Rocket:

    def __init__(self, explosions: list[BasicExplosion | ImageExplosion | LineExplosion],
                 pos: FVector, start: FVector, duration: int,
                 curve_x: float = 1, curve_y: float = 4, launch_sizes: list[int] = [2, 3],
                 launch_colors: list[RGBColor] = ROCKET_LAUNCH_COLORS,
                 launch_handler: Callable = rocket_launch) -> None:

        self.explosions = explosions
        self.pos = pos
        self.start = start
        self.duration = duration
        self.curve_x = curve_x
        self.curve_y = curve_y	
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
                for explosion in self.explosions:
                    self.particles.extend(explosion.generate_particles(self.pos))
        
            return bool(self.particles)
        
        factor_increasing = (self.cursor / self.duration) ** self.curve_x
        factor_decreasing = (1 - self.cursor / self.duration) ** self.curve_y
        offset_x = (self.pos - self.start).x * factor_increasing
        offset_y = (self.start - self.pos).y * factor_decreasing
        pos = FVector(self.start.x + offset_x, self.pos.y + offset_y)

        for i in range(int(rd.random() * (factor_decreasing * 30 + 2))):
            self.particles.append(PointParticle(pos.update_y(rd.random() * 40 * factor_decreasing), FVector(rd.random() * 1.5 - 0.75, rd.random() * 5),
                                                rd.choice(self.launch_sizes), rd.choice(self.launch_colors),
                                                self.launch_handler))

        self.cursor += 1

        return True

    def render(self, surface: pg.Surface) -> None:

        for particle in self.particles:
            particle.draw(surface)

    def copy(self, state=False) -> Self:
        rocket = Rocket(self.explosions, self.pos, self.start, self.duration,
                        self.curve_x, self.curve_y, self.launch_sizes, self.launch_colors, self.launch_handler)
        if state:
            rocket.cursor = self.cursor
            rocket.exploded = self.exploded
            rocket.particles = [particle.copy() for particle in self.particles]
        return rocket
    
    def __repr__(self) -> str:
        return f"Rocket[pos={self.pos}|start={self.start}|duration={self.duration}|cursor={self.cursor}|ID={id(self)}]"
