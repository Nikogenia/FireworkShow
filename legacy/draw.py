# IMPORTS
import pygame as pg
from color import *


# FUNCTIONS

# Rectangle
def rect(surface: pg.Surface, x: int, y: int, width: int, height: int, color: RGBColor, alpha: int = 255) -> None:
    surf = pg.Surface((width, height))
    surf.fill(color)
    surf.set_colorkey(DARK_BLACK)
    surf.set_alpha(alpha)
    surface.blit(surf, (x, y))
