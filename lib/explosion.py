import pygame as pg
from .fvector import FVector
from .particle import PointParticle
from .color import RGBColor, DARK_BLACK
from .particle_handler import rocket_basic_explosion, rocket_image_explosion
import random as rd
from typing import Callable


class BasicExplosion:

    def __init__(self, colors: list[RGBColor], sizes: list[int] = [3, 4, 5, 6], scale: float = 1, strength: float = 1, handler: Callable = rocket_basic_explosion) -> None:

        self.colors = colors
        self.sizes = sizes
        self.scale = scale
        self.strength = strength
        self.handler = handler


    def generate_particles(self, pos: FVector) -> list[PointParticle]:

        particles: list[PointParticle] = []

        for i in range(self.strength * 400):
            particles.append(PointParticle(pos, FVector(rd.gauss(0, 1.2), rd.gauss(0, 1.2)) * self.scale,
                                           rd.choice(self.sizes), rd.choice(self.colors), self.handler, True))

        return particles

class ImageExplosion:

    def __init__(self, image: pg.Surface, sizes: list[int] = [3, 4, 5, 6], scale: float = 1, strength: float = 1, handler: Callable = rocket_image_explosion) -> None:

        self.image = image
        self.sizes = sizes
        self.scale = scale
        self.strength = strength
        self.handler = handler


    def generate_particles(self, pos: FVector) -> list[PointParticle]:

        particles: list[PointParticle] = []

        image_center: FVector = FVector(self.image.get_width() / 2, self.image.get_height() / 2)

        for x in range(self.image.get_width()):
            for y in range(self.image.get_height()):
                pixel: tuple[int, int, int, int] = self.image.get_at((x, y))
                color: RGBColor = RGBColor(pixel[0], pixel[1], pixel[2])
                if pixel[3] == 0 or color == DARK_BLACK:
                    continue
                vel: FVector = FVector(x - image_center.x, y - image_center.y) / (self.image.get_width() * self.image.get_height() / 200) * self.scale
                for i in range(self.strength * 5):
                    particles.append(PointParticle(pos, vel + FVector((rd.random() - 0.5) / 8, (rd.random() - 0.5) / 8),
                                                   rd.choice(self.sizes), color, self.handler, True))

        return particles
