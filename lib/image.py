# IMPORTS

# Libraries
import pygame as pg
import cv2 as cv
import numpy as np
import multiprocessing as mp


# FUNCTIONS

# Pygame surface to opencv image
def pg_to_cv(pg_surface: pg.Surface) -> np.ndarray:
    return cv.cvtColor(pg.surfarray.array3d(pg_surface).transpose([1, 0, 2]), cv.COLOR_RGB2BGR)


# Opencv image to pygame surface
def cv_to_pg(cv_image: np.ndarray) -> pg.Surface:
    return pg.image.frombuffer(cv_image.tobytes(), (cv_image.shape[1], cv_image.shape[0]), "BGR")
