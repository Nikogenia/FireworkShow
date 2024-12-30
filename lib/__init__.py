import os
import ctypes
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = ""
if os.name == "nt":
    ctypes.windll.user32.SetProcessDPIAware()

from .animation import Animation
from .show import Show

from .vector import Vector
from .fvector import FVector
from . import font, draw, color, particle_handler, image

from .explosion import BasicExplosion, ImageExplosion
from .rocket import Rocket
from .fountain import Fountain
from .particle import PointParticle

from .display import Display
from .frame import Frame
