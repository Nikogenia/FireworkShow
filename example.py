import lib
from lib.color import *
import pygame as pg


def scene_1():

    explosion = lib.BasicExplosion([RED, ORANGE, YELLOW], scale=1.2, strength=4)
    rocket = lib.Rocket([explosion], lib.FVector(1200, 400), lib.FVector(1140, 1100), 120)
    animation.spawn_rocket(rocket)

    animation.wait(40)

    rocket = lib.Rocket([explosion], lib.FVector(800, 400), lib.FVector(860, 1100), 120)
    animation.spawn_rocket(rocket)

    animation.wait(40)

    fountain = lib.Fountain(lib.FVector(400, 1080), 270, 200, [LIGHT_LIME, LIME, DARK_LIME, GREEN, DARK_GREEN], scale=1, strength=1, spread=2)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(1520, 1080), 270, 200, [LIGHT_LIME, LIME, DARK_LIME, GREEN, DARK_GREEN], scale=1, strength=1, spread=2)
    animation.spawn_fountain(fountain)

    animation.wait(100)

    explosion1 = lib.ImageExplosion(redhair, sizes=[3, 4, 5], scale=2, strength=0.6)
    explosion2 = lib.LineExplosion([YELLOW, DARK_YELLOW, LIGHT_YELLOW], scale=1.2, strength=0.8)
    rocket = lib.Rocket([explosion2, explosion1], lib.FVector(960, 400), lib.FVector(980, 1100), 100)
    animation.spawn_rocket(rocket)

    animation.wait(250)

    explosion = lib.LineExplosion([WHITE, LIGHT_YELLOW, YELLOW, DARK_YELLOW, ORANGE], scale=1, strength=1.4)
    rocket = lib.Rocket([explosion], lib.FVector(960, 400), lib.FVector(960, 1100), 140)
    animation.spawn_rocket(rocket)
    animation.wait(10)
    rocket = lib.Rocket([explosion], lib.FVector(700, 450), lib.FVector(740, 1100), 135)
    animation.spawn_rocket(rocket)
    rocket = lib.Rocket([explosion], lib.FVector(1220, 450), lib.FVector(1180, 1100), 135)
    animation.spawn_rocket(rocket)
    animation.wait(10)
    rocket = lib.Rocket([explosion], lib.FVector(440, 500), lib.FVector(500, 1100), 130)
    animation.spawn_rocket(rocket)
    rocket = lib.Rocket([explosion], lib.FVector(1480, 500), lib.FVector(1420, 1100), 130)
    animation.spawn_rocket(rocket)

    
if __name__ == '__main__':

    redhair = pg.image.load("./images/redhair.png")

    animation = lib.Animation(1920, 1080, 60, 900)

    scene_1()

    show = lib.Show(animation,
                    name="Example",
                    version="1.0",
                    author="Nikogenia",
                    cache=False,
                    memory_limit=2000,
                    music_path="./music/new-year-bells.mp3")

    show.preview()
