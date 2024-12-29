import os
import ctypes
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = ""
if os.name == "nt":
    ctypes.windll.user32.SetProcessDPIAware()

from .vector import Vector
from .fvector import FVector
from .display import Display
from .show import Show
from .frame import Frame
from .animation import Animation
from . import font, draw, color
