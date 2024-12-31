import lib
from lib.color import *
import pygame as pg


def scene_1():

    animation.jump(frame=48, second=1)

    explosion = lib.BasicExplosion([DARK_RED, RED, LIGHT_RED, ORANGE], scale=1, strength=2)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 300, 400), lib.FVector(960 - 200, 1100), 105)
    animation.explode_rocket(rocket)
    animation.wait(25)

    explosion = lib.BasicExplosion([DARK_RED, RED, LIGHT_RED, PURPLE], scale=1, strength=2)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 300, 400 - 30), lib.FVector(960 + 200, 1100), 115)
    animation.explode_rocket(rocket)

    animation.jump(frame=5, second=3)

    explosion = lib.BasicExplosion([LIGHT_PURPLE, DARK_PURPLE, PURPLE], scale=1, strength=2)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 400, 400 + 60), lib.FVector(960 - 250, 1100), 120)
    animation.explode_rocket(rocket)
    animation.wait(25)

    explosion = lib.BasicExplosion([LIGHT_PURPLE, DARK_PURPLE, BLUE, PURPLE], scale=1, strength=2)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 50, 400 - 60), lib.FVector(960, 1100), 130)
    animation.explode_rocket(rocket)
    animation.wait(25)

    explosion = lib.BasicExplosion([DARK_PURPLE, BLUE, PURPLE], scale=1, strength=2)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 500, 400 + 50), lib.FVector(960 + 300, 1100), 140)
    animation.explode_rocket(rocket)

    animation.jump(frame=48, second=4)

    explosion = lib.LineExplosion([RED, ORANGE, YELLOW], scale=1, strength=1)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 500, 400 - 100), lib.FVector(960 - 200, 1100), 90)
    animation.explode_rocket(rocket)
    animation.wait(13)

    rocket = lib.Rocket([explosion], lib.FVector(960 - 200, 400 - 60), lib.FVector(960 + 200, 1100), 95)
    animation.explode_rocket(rocket)
    animation.wait(13)

    rocket = lib.Rocket([explosion], lib.FVector(960 + 150, 400 - 80), lib.FVector(960 - 300, 1100), 100)
    animation.explode_rocket(rocket)

    fountain = lib.Fountain(lib.FVector(0, 1200), 315, 20, [RED, ORANGE, YELLOW], [2, 3, 4], scale=1, strength=1)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(1920, 1200), 225, 20, [RED, ORANGE, YELLOW], [2, 3, 4], scale=1, strength=1)
    animation.spawn_fountain(fountain)

    animation.wait(25)

    rocket = lib.Rocket([explosion], lib.FVector(960 - 450, 400 - 90), lib.FVector(960 + 300, 1100), 95)
    animation.explode_rocket(rocket)

    animation.jump(frame=33, second=6)

    explosion = lib.BasicExplosion([PURPLE, DARK_PURPLE, BLUE], scale=1, strength=2)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 600, 400 + 160), lib.FVector(960 + 440, 1100), 80)
    animation.explode_rocket(rocket)
    animation.wait(25)

    explosion = lib.BasicExplosion([PURPLE, DARK_BLUE, BLUE], scale=1, strength=2)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 550, 400 + 180), lib.FVector(960 - 460, 1100), 90)
    animation.explode_rocket(rocket)

    animation.jump(frame=49, second=7)

    explosion = lib.BasicExplosion([BLUE, DARK_BLUE], scale=1, strength=2)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 700, 400 - 200), lib.FVector(960 + 850, 1100), 130)
    animation.explode_rocket(rocket)

    explosion = lib.BasicExplosion([DARK_BLUE, BLUE], scale=1, strength=2)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 750, 400 - 250), lib.FVector(960 - 900, 1100), 125)
    animation.explode_rocket(rocket)


def scene_2():

    animation.jump(frame=46, second=8)

    explosion = [lib.LineExplosion([DARK_YELLOW, YELLOW, LIGHT_YELLOW, WHITE], scale=2, strength=0.5),
                 lib.ImageExplosion(welcome_blue, scale=4, strength=0.5)]
    rocket = lib.Rocket(explosion, lib.FVector(960, 400 - 100), lib.FVector(960, 1100), 150)
    animation.explode_rocket(rocket)

    explosion = lib.BasicExplosion([BLUE, LIGHT_BLUE, DARK_AQUA, AQUA, LIGHT_AQUA], scale=1.5, strength=3)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 700, 400 - 200), lib.FVector(960 - 400, 1100), 120)
    animation.explode_rocket(rocket)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 740, 400 - 220), lib.FVector(960 + 400, 1100), 115)
    animation.explode_rocket(rocket)
    animation.wait(6)

    rocket = lib.Rocket([explosion], lib.FVector(960 - 620, 400 + 200), lib.FVector(960 - 450, 1100), 125)
    animation.explode_rocket(rocket)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 600, 400 + 150), lib.FVector(960 + 450, 1100), 130)
    animation.explode_rocket(rocket)

    animation.jump(frame=35, second=10)

    explosion = lib.LineExplosion([LIGHT_BLUE, LIGHT_AQUA, YELLOW, LIGHT_YELLOW, WHITE], lines=15, scale=1.5, strength=2)
    rocket = lib.Rocket([explosion], lib.FVector(960, 400 - 100), lib.FVector(960 + 50, 1100), 120)
    animation.explode_rocket(rocket)
    animation.wait(13)

    explosion = lib.LineExplosion([LIGHT_BLUE, LIGHT_AQUA, YELLOW, LIGHT_YELLOW, WHITE], lines=15, scale=1, strength=2)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 400, 400 + 100), lib.FVector(960 - 600, 1100), 120)
    animation.explode_rocket(rocket)
    animation.wait(6)

    rocket = lib.Rocket([explosion], lib.FVector(960 + 420, 400 - 50), lib.FVector(960 + 600, 1100), 125)
    animation.explode_rocket(rocket)

    animation.jump(frame=48, second=11)

    explosion = lib.BasicExplosion([DARK_LIME, AQUA, DARK_AQUA, LIME, LIGHT_LIME], scale=1, strength=1)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 400, 400 - 250), lib.FVector(960 - 200, 1100), 130)
    animation.explode_rocket(rocket)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 420, 400 - 230), lib.FVector(960 + 220, 1100), 135)
    animation.explode_rocket(rocket)
    animation.wait(6)

    explosion = lib.BasicExplosion([DARK_LIME, DARK_AQUA, LIME, LIGHT_LIME], scale=1.5, strength=1.5)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 550, 400 - 20), lib.FVector(960 - 320, 1100), 125)
    animation.explode_rocket(rocket)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 530, 400 - 50), lib.FVector(960 + 300, 1100), 120)
    animation.explode_rocket(rocket)
    animation.wait(6)

    explosion = lib.BasicExplosion([DARK_LIME, LIME, LIGHT_LIME], scale=2, strength=2)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 700, 400 + 280), lib.FVector(960 - 400, 1100), 130)
    animation.explode_rocket(rocket)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 720, 400 + 250), lib.FVector(960 + 410, 1100), 135)
    animation.explode_rocket(rocket)

    animation.jump(frame=34, second=13)

    explosion = lib.ImageExplosion(star4_yellow, scale=2.4, strength=0.4)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 400, 400 + 300), lib.FVector(960 - 600, 1100), 90)
    animation.explode_rocket(rocket)
    animation.wait(25)

    explosion = lib.ImageExplosion(star4_yellow, scale=1.8, strength=0.3)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 120, 400 + 150), lib.FVector(960 + 100, 1100), 95)
    animation.explode_rocket(rocket)
    animation.wait(50)

    explosion = lib.ImageExplosion(star4_yellow, scale=1.3, strength=0.2)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 440, 400 + 400), lib.FVector(960 + 650, 1100), 100)
    animation.explode_rocket(rocket)


def scene_3():

    animation.jump(frame=48, second=14)

    
if __name__ == '__main__':

    redhair = pg.image.load("./images/redhair.png")
    welcome_blue = pg.image.load("./images/welcome-blue.png")
    star4_yellow = pg.image.load("./images/star4-yellow.png")
    star5_yellow = pg.image.load("./images/star5-yellow.png")
    heart_red = pg.image.load("./images/heart-red.png")

    animation = lib.Animation(1920, 1080, 60, 1100, 0)

    scene_1() 
    scene_2()
    scene_3()

    show = lib.Show(animation,
                    name="Firework Show 2025",
                    version="1.0",
                    author="Nikogenia",
                    cache=False,
                    memory_limit=2000,
                    music_path="./music/new-year-bells-short.mp3")

    show.preview()
