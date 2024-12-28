# IMPORTS
from vector.fvector import FVector
from color import *
import pygame as pg
from typing import Callable


# CLASSES

# Point particle
class PointParticle:

    # CONSTRUCTOR
    def __init__(self, pos: FVector, vel: FVector, size: float, color: RGBColor, handler: Callable, glow: bool = False) -> None:

        # Define particle information
        self.pos: FVector = pos
        self.vel: FVector = vel
        self.size: float = size
        self.color: RGBColor = color
        self.handler: Callable = handler
        self.glow: bool = glow


    # METHODS

    # Update
    def update(self, delta_time: float) -> None:

        # Call the handler
        self.handler(self, delta_time)

        # Apply the velocity to the position
        self.pos += self.vel * delta_time

    # Draw
    def draw(self, surface: pg.Surface) -> None:

        # Draw the circle for the particle
        pg.draw.circle(surface, self.color, self.pos, self.size)

        # Draw glow
        if self.glow:
            glow_size: float = self.size / 8
            surf: pg.Surface = pg.Surface(((self.size + glow_size) * 2, (self.size + glow_size) * 2))
            surf.set_colorkey(DARK_BLACK)
            pg.draw.circle(surf, self.color.modify((30, 30, 30)), (self.size + glow_size, self.size + glow_size), self.size + glow_size)
            surface.blit(surf, self.pos - (self.size + glow_size, self.size + glow_size), special_flags=pg.BLEND_RGB_ADD)


    # OVERRIDE METHODS

    # String
    def __str__(self) -> str:
        return f"PointParticle[pos={self.pos}|vel={self.vel}|size={self.size}|color={self.color}|glow={self.glow}|ID={id(self)}]"


# CLASSES

# Spark particle
class SparkParticle:

    # CONSTRUCTOR
    def __init__(self, pos: FVector, vel: FVector, size: float, color: RGBColor, handler: Callable, glow: bool = False) -> None:

        # Define particle information
        self.pos: FVector = pos
        self.vel: FVector = vel
        self.size: float = size
        self.color: RGBColor = color
        self.handler: Callable = handler
        self.glow: bool = glow


    # METHODS

    # Update
    def update(self, delta_time: float) -> None:

        # Call the handler
        self.handler(self, delta_time)

        # Apply the velocity to the position
        self.pos += self.vel * delta_time

    # Draw
    def draw(self, surface: pg.Surface) -> None:

        # Draw the circle for the particle
        pg.draw.circle(surface, self.color, self.pos, self.size)

        # Draw glow
        if self.glow:
            glow_size: float = self.size / 8
            surf: pg.Surface = pg.Surface(((self.size + glow_size) * 2, (self.size + glow_size) * 2))
            surf.set_colorkey(DARK_BLACK)
            pg.draw.circle(surf, self.color.modify((30, 30, 30)), (self.size + glow_size, self.size + glow_size), self.size + glow_size)
            surface.blit(surf, self.pos - (self.size + glow_size, self.size + glow_size), special_flags=pg.BLEND_RGB_ADD)


    # OVERRIDE METHODS

    # String
    def __str__(self) -> str:
        return f"PointParticle[pos={self.pos}|vel={self.vel}|size={self.size}|color={self.color}|glow={self.glow}|ID={id(self)}]"
