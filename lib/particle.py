from .fvector import FVector
from .color import *
import pygame as pg
from typing import Callable, Self


class PointParticle:

    def __init__(self, pos: FVector, vel: FVector, size: float, color: RGBColor, handler: Callable, glow: bool = False) -> None:

        self.pos: FVector = pos
        self.vel: FVector = vel
        self.size: float = size
        self.color: RGBColor = color
        self.handler: Callable = handler
        self.glow: bool = glow

    def update(self) -> bool:

        self.handler(self)
        self.pos += self.vel

        return self.size >= 1

    def draw(self, surface: pg.Surface) -> None:

        pg.draw.circle(surface, self.color, self.pos, self.size)

        if self.glow:
            glow_size: float = self.size / 8
            surf: pg.Surface = pg.Surface(((self.size + glow_size) * 2, (self.size + glow_size) * 2))
            surf.set_colorkey(DARK_BLACK)
            pg.draw.circle(surf, self.color.modify((30, 30, 30)), (self.size + glow_size, self.size + glow_size), self.size + glow_size)
            surface.blit(surf, self.pos - (self.size + glow_size, self.size + glow_size), special_flags=pg.BLEND_RGB_ADD)

    def copy(self) -> Self:
        return PointParticle(self.pos, self.vel, self.size, self.color, self.handler, self.glow)

    def __repr__(self) -> str:
        return f"PointParticle[pos={self.pos}|vel={self.vel}|size={self.size}|color={self.color}|glow={self.glow}|ID={id(self)}]"
