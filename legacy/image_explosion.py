# IMPORTS
import pygame as pg
from vector.vector import Vector
from vector.fvector import FVector
from particle import PointParticle
from color import RGBColor, DARK_BLACK
import random as rd
import particle_handler


# CLASSES

# Image explosion
class ImageExplosion:

    # CONSTRUCTOR
    def __init__(self, image: pg.Surface, scale: float = 1, strength: float = 1) -> None:

        # Set the image, scale and strength
        self.image: pg.Surface = image
        self.scale: float = scale
        self.strength: float = strength


    # METHODS

    # Generate particles
    def generate_particles(self, pos: FVector) -> list[PointParticle]:

        # Create a particle list
        particles: list[PointParticle] = []

        # Image center
        image_center: FVector = FVector(self.image.get_width() / 2, self.image.get_height() / 2)

        # Loop for all pixels in the image
        for x in range(self.image.get_width()):
            for y in range(self.image.get_height()):
                pixel: tuple[int, int, int, int] = self.image.get_at((x, y))
                color: RGBColor = RGBColor(pixel[0], pixel[1], pixel[2])
                if pixel[3] == 0 or color == DARK_BLACK:
                    continue
                vel: FVector = FVector(x - image_center.x, y - image_center.y) / (self.image.get_width() * self.image.get_height() / 200) * self.scale
                for i in range(int(rd.randint(0, self.image.get_width() * self.image.get_height() // 1000) * self.strength)):
                    particles.append(PointParticle(pos, vel + FVector((rd.random() - 0.5) / 6, (rd.random() - 0.5) / 6), rd.randint(2, 5), color, particle_handler.rocket_image_explosion, glow=True))

        # Return the particles
        return particles
